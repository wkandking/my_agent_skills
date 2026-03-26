# textual TUI 工具开发首次实践

日期: 2026-03-08

## Triggers
- "textual" "TUI" "ComposeResult" "DataTable" "Collapsible" "headless test" "gh run" "log parsing"

## 背景

为 `cli-tool-dev` 角色开发首个工具：GitHub Actions TUI 查看器（`gh-actions-tui.py`），基于 textual 框架，单文件 Python，通过 `gh` CLI 获取数据。目标是左右分栏浏览 Runs/Jobs + 全屏查看 Log。

## 证据与现象

### 1. textual API 版本陷阱

| 错误用法 | 正确用法 (textual 8.x) | 症状 |
|----------|------------------------|------|
| `from textual.app import ComposeWidget` | `from textual.app import ComposeResult` | `ImportError: cannot import name 'ComposeWidget'` |
| `DataTable.update_cell_by_row_index(row, col, val)` | `DataTable.update_cell_at(Coordinate(row, col), val)` | `AttributeError` |

**根因**：LLM 训练数据中混杂了 textual 不同版本的 API。textual 迭代速度快，class/method 名称在 0.x → 1.x 期间频繁变更。

**验证方法**：在编码后立即用 `python3 -c "import ...; print(hasattr(...))"` 检查 API 是否存在，而非等到运行时才发现。

### 2. `gh run view --log` 输出格式

格式为 `<job-name>\t<step-name>\t<timestamp> <message>`，三列 tab 分隔：

```
format-check	Set up job	2026-03-08T03:48:13.71Z Current runner version: '2.332.0'
format-check	Set up job	2026-03-08T03:48:13.72Z ...
lint	Run lint	2026-03-08T03:48:15.00Z error: ...
```

关键点：
- **所有 job 的 log 混在一起输出**，必须按第一列 job name 过滤才能得到单个 job 的 log
- step name 是第二列，可用于分组显示
- 同一 run 的不同 job 的 log 行交错排列

### 3. textual headless 测试模式

textual 提供 `app.run_test()` 用于无终端环境下的自动化测试：

```python
async with app.run_test(size=(120, 30)) as pilot:
    await pilot.pause()          # 等待渲染
    await pilot.press("enter")   # 模拟按键
    table = app.query_one("#id", DataTable)
    assert table.row_count > 0
```

- `run_test()` 不需要真实终端，CI/SSH 环境可用
- `pilot.pause()` 等待事件循环处理完当前事件
- 可以用 `app.query_one()` 直接检查组件状态
- 可以用 `app.screen_stack` 验证 Screen 跳转

### 4. 失败 step 检测的启发式方法

`gh` CLI 不直接标记哪个 step 失败。采用启发式检测（检查最后 20 行是否含 `error`/`fail`/`FAIL`/`exit code`）来决定 Collapsible 的默认展开状态。这不完美但实用。

## 关键决策

| 决策 | 依据 |
|------|------|
| 用 `gh` CLI subprocess 而非 GitHub REST API | 复用已有 `gh auth` 认证，零配置；单文件不想引入 `requests`/`httpx` 依赖 |
| Log 视图用 `Collapsible` 而非 `Tree` | Collapsible 天然支持展开/折叠 UI，不需要自己实现；Tree 更适合层级数据 |
| 用 `DataTable` 而非 `ListView` | DataTable 内置多列对齐、row cursor，适合表格式数据 |
| 左栏加 `›` marker 列 | 用 `update_cell_at` 动态更新第 0 列，比 custom render 简单 |

## 结果

- 工具可正常运行，三个视图状态（Runs/Jobs 分栏 → Jobs 聚焦 → Log 全屏）切换正常
- headless 测试通过：数据加载、焦点切换、Screen 推入/弹出全部验证

## 可复用模式

1. **textual API 先验证再用**：写完代码后，用 `python3 -c "from textual... import X"` 验证 import 是否存在，用 `hasattr` / `inspect.signature` 检查方法签名。textual 版本间 API 差异大。
2. **`gh` CLI 作为数据源**：`gh run list --json` 和 `gh run view --json jobs` 返回结构化 JSON，是 TUI 工具的理想数据源。但 `--log` 是纯文本混合输出，需要自己按 job name 过滤和按 step name 分组。
3. **textual headless 测试**：`app.run_test()` + `pilot` 可以在无终端环境中完整测试 TUI 交互流程，包括按键、焦点切换、Screen 导航。
4. **单文件 TUI 工具结构**：数据层（subprocess 调用）→ 辅助函数（格式化）→ Screen/Widget → App，从底到顶组织，保持可读性。
