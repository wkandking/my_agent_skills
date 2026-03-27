---
kind: insight
description: "对 coding agent 来说，任务状态、环境知识与长任务控制应优先外显到文件、CLI 与日志，而不是藏在 TODO/plan/MCP/sub-agent 黑盒里"
triggers:
  - "MCP"
  - "TODO.md"
  - "PLAN.md"
  - "sub-agent"
  - "background bash"
  - "tmux"
  - "可观察性"
  - "黑盒 agent"
  - "上下文工程"
---

# Insight: 外显工作状态优于黑盒 agent 特性

## 规律

对 coding agent 来说，凡是涉及 **持久状态、协作交接、环境特定知识** 的能力，优先外显到 **文件 + 标准 CLI + 显式日志**，而不是隐藏在 harness 的内建特性里。

内建能力最适合做**窄而透明的原语**（读文件、改文件、跑命令、展示 diff / event），不适合偷偷承载大块隐式状态。

## 为什么

1. **可观察**：`AGENTS.md`、skill README、`TODO.md`、`PLAN.md`、job log 都是用户和后续 agent 可直接检查的产物；隐藏在 plan mode、MCP 注入、sub-agent context 里的状态更难审计
2. **可恢复**：session 中断、context compaction、换人接手后，文件和 `tmux`/任务日志仍然存在；黑盒 state 往往随会话一起消失
3. **按需付费**：README/skill 允许 progressive disclosure，需要时再读；把整套工具 schema 或环境说明默认塞进上下文，会持续消耗 token
4. **可协作**：文档可 diff/review，worktree 可隔离改动，`tmux` 可交接运行中的任务；黑盒 feature 只能依赖当前 harness UI
5. **失败模式清晰**：文件过期、日志缺失、分支脏了都能直接定位；隐藏 orchestration 出错时，往往只表现为 agent "突然变笨"，很难判断是 prompt、tool 还是 runtime 问题

## 什么时候不要急着内建

若一个新 feature 同时满足以下任两条，应优先考虑"文件/CLI 化"，而不是做成黑盒 harness 特性：

- 需要跨 session 保留
- 需要多人/多 agent 接手
- 需要版本管理或 code review
- 只在少数任务里才会用到
- 强依赖当前 repo 或环境约定

## 但也不要走向另一个极端

这不等于"内建 feature 都没用"。内建能力仍然有价值，前提是它：

- **状态可见**：用户能看到当前 plan、event、tool call 与产物
- **结果可落盘**：必要时能导出为文件、日志或 diff
- **按需暴露**：没用到的说明不要默认占据上下文
- **失败可诊断**：出问题时能分清是 prompt、tool 还是 harness runtime

## 来源

- Mario Zechner, `pi: A coding agent that doesn't try to launch you to Mars`（2025-11-30）：强调 minimal tools、file-based task state、CLI/README over MCP、`tmux` over background shell、谨慎看待黑盒 sub-agent
