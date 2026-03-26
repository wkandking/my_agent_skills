---
description: "快速迭代库（如 textual）的 API 在 LLM 训练数据中版本混杂，生成的代码高概率使用过时 API。必须在编码后立即用运行时验证（import + hasattr + inspect.signature）确认 API 存在性，而非等到集成测试才发现。"
triggers:
  - "textual"
  - "ImportError"
  - "AttributeError"
  - "API 版本"
  - "过时 API"
  - "hasattr"
source:
  - "roles/cli-tool-dev/experience/2026-03-08-textual-tui-first-practice.md"
---

# Insight: 快速迭代库的 LLM 生成代码需要运行时验证

## 规律

LLM 训练数据混杂了快速迭代库的多个版本 API。这类库的特征是：
- 版本间 class/method 名称频繁变更（如 textual 的 `ComposeWidget` → `ComposeResult`）
- 文档更新快但 LLM 训练数据滞后
- 同名 API 签名可能在不同版本间不兼容

结果：LLM 生成的代码看起来合理，但运行时报 `ImportError` / `AttributeError`。

## 应对

写完使用这类库的代码后，立即做最小验证：

```bash
# 验证 import 是否存在
python3 -c "from textual.app import ComposeResult; print('OK')"

# 验证方法签名
python3 -c "from textual.widgets import DataTable; import inspect; print(inspect.signature(DataTable.update_cell_at))"

# 验证属性是否存在
python3 -c "from textual.widgets import DataTable; print(hasattr(DataTable, 'update_cell_at'))"
```

代价极低（几秒），但能把 API 不存在的问题从"集成测试/运行时崩溃"前移到"编码阶段"。

## 已知的高风险库

| 库 | 典型陷阱 |
|---|---|
| textual | `ComposeWidget` vs `ComposeResult`、`update_cell_by_row_index` vs `update_cell_at`、`from textual.work import work` vs `from textual import work` |

（随着更多 experience 积累扩充此表）

## Escalate to experience if

- 遇到具体的 API 版本不兼容问题，需要查看完整的踩坑过程和替代方案
