# cli-tool-dev

## 职责

开发面向开发者的 CLI/TUI 工具：

- 偏好单文件 Python 分发（顶部注释声明依赖）
- 关注交互体验和实用性
- 优先复用已有 CLI 工具（如 `gh`、`git`）作为数据源，避免重复实现认证/API 对接

## 使用的工具

- TUI 框架：`textual`（Python）
- 数据源：`gh` CLI、`git` 等系统工具（subprocess 调用）
- 开发/调试：`textual console`、`textual run --dev`

## 相关知识

- `AGENTS.md` — 多 agent 协作规则（worktree、禁止 push main、PR 流程）
- `base/principles/knowledge-loading.md`
- `base/knowledge-sedimentation.md`

## 角色知识索引

> 本索引是 agent 的**首要加载入口**。先读索引了解有哪些知识，再按需 `Read` 具体文件。不要一次性加载所有文档。
>
> 每条摘要必须包含**足够的关键词**，让 agent 能判断是否与当前任务相关。

### Skills

- `skills/textual-async-data-loading/SKILL.md` — textual TUI 异步数据加载完整模式：`@work(thread=True)` 后台执行阻塞 IO → `call_from_thread` 回主线程渲染 → `LoadingIndicator` 过渡 → `exclusive` group 防抖 → dict 缓存 + stale check 防竞态。含 headless 测试中等待 worker 的方法。

### Principles

- `principles/no-blocking-io-on-ui-thread.md` — TUI 开发中阻塞 IO（subprocess、HTTP、文件读写）必须在后台线程执行，UI 线程只做渲染和事件处理，否则界面冻结。

### Insights

- `insights/llm-fast-iterating-lib-verification.md` — 快速迭代库（如 textual）的 API 在 LLM 训练数据中版本混杂，生成代码高概率使用过时 API。编码后立即用 `python3 -c` + `hasattr` / `inspect.signature` 验证 API 存在性。含已知陷阱表。

### Experience（按需查阅，不常驻加载）

- `experience/2026-03-08-textual-tui-first-practice.md` — textual 8.x TUI 开发首次实践：API 版本陷阱（ComposeResult/update_cell_at）、`gh run view --log` 输出格式解析（tab 分隔、按 job name 过滤）、headless 测试（run_test + pilot）、Collapsible 折叠/展开、单文件工具代码组织。
- `experience/2026-03-08-textual-async-loading-cache.md` — textual TUI 性能优化：`@work(thread=True)` 异步加载（导入陷阱 `from textual import work`）、`call_from_thread` 回主线程、`exclusive=True` + `group` 请求防抖、`LoadingIndicator` 显示/隐藏模式、dict 缓存 + stale check 防竞态、headless 测试中轮询 `app.workers` 等 worker 完成。

### Questions（已知的未知）

- `questions.md` — 2 条待验证：`@work` vs `asyncio` subprocess 取舍、`gh` CLI failed step 检测方式

### Tools

- [st1page/gh-actions-tui](https://github.com/st1page/gh-actions-tui) — GitHub Actions TUI 查看器：基于 textual 的左右分栏界面，可浏览 Runs、Jobs 列表并查看 Job Log，数据通过 `gh` CLI 获取。
