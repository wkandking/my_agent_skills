---
kind: principle
description: "不同语义或不同部署变量的 benchmark 场景，不要强行合并成一个总体赢家结论。"
triggers:
  - "benchmark 场景"
  - "总体赢家"
  - "可比性"
  - "部署变量"
source:
  - "roles/performance-infra-tester/principles/scenario-comparability.md"
---

# 场景可比性规则

- 不要把语义不同的 benchmark 场景硬压成一个“总体赢家”结论。
- 像 `no-distinct` 和分步 `DISTINCT` 这样的查询语义变化，应被视为主要解释变量，而不是细枝末节的变体。
- 像 `numa0` 这样的部署变量，应与数据库引擎变量分开分析。
- 写结论时，先给每个场景独立判断，再总结它们之间共享的模式。
