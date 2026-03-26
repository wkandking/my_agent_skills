---
kind: principle
description: "需要跨 session、跨 agent 保留的任务状态，必须外显到文件、branch、日志或标准 CLI 产物；不要只依赖 harness 的隐式状态"
triggers:
  - "任务状态"
  - "TODO.md"
  - "PLAN.md"
  - "harness"
  - "sub-agent"
  - "MCP"
  - "可观察性"
source:
  - "base/principles/persistent-task-state-must-be-externalized.md"
  - "base/insights/visible-workflow-state-over-hidden-agent-features.md"
---

# 持久任务状态必须外显

## 背景

Agent 在单个 session 内维护 plan、上下文和工具状态很方便，但一旦出现以下情况，隐藏状态就会立刻变脆：

- session 中断或 context 被压缩
- 需要另一个 agent 或人类接手
- 需要 review、审计或事后复盘
- 运行中的后台任务要跨 terminal/机器继续跟踪

如果任务状态只存在于 harness 内部，就会出现"事情在推进，但没人说得清现在到哪一步了"的问题。

## 内容

1. **凡是需要跨 session / 跨 agent 保留的状态，必须落盘**
   - 计划写到 `PLAN.md` 或等价文档
   - 待办写到 `TODO.md` 或 PR description
   - 关键环境知识写到 `AGENTS.md`、README、skill 文档

2. **内建 feature 不能作为唯一事实源**
   - plan mode、MCP 注入、sub-agent、后台 shell 可以辅助工作
   - 但如果它们的状态不能被直接检查、导出或交接，就不能承载唯一任务状态

3. **长任务必须依赖标准运行时与日志**
   - 后台运行优先用 `tmux`、系统服务等显式机制
   - 关键参数、日志位置、产物路径必须写入可检索文档或任务记录

4. **协作状态必须进入版本化介质**
   - 分支、worktree、commit、PR title/description、任务日志，都是可审计的协作状态
   - "只有当前 agent 知道"的状态不算完成交接

## Guidance

- **短期任务分解**：写 `TODO.md`，而不是把 todo 只留在会话里
- **多步骤实施计划**：写 `PLAN.md` 或 PR description，确保中断后可恢复
- **环境特定知识**：写到 `AGENTS.md`、role README、skill 文档
- **长时间命令/后台任务**：交给 `tmux` / 调度器，并把日志和产物路径落盘
- **交接前检查**：假设下一个接手的人看不到你的 session，只能看到 repo、PR、日志和任务系统；若这还不够，说明状态外显不完整

## Escalate to insight if

- 需要解释"为什么黑盒 agent feature 会在真实协作里失效"
- 需要判断某个新 harness feature 应该内建，还是应优先文件/CLI 化
- 需要论证可观察性、可恢复性、token 成本之间的取舍

## 进一步阅读

- `base/notes/visible-workflow-state-over-hidden-agent-features.md`
- `base/notes/git-worktree.md`
