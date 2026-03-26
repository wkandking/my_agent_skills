---
description: "知识加载策略详述：分层加载、常驻 vs 按需判断标准、experience 唤醒、context 压缩后重新加载、摘要写法"
triggers:
  - "知识加载"
  - "分层加载"
  - "常驻 context"
  - "按需加载"
  - "experience 唤醒"
  - "context 压缩"
  - "compaction"
  - "写摘要"
  - "索引摘要"
---

# 知识加载策略

角色知识文档会持续增长，不能全部塞进 context。采用**索引→按需**的两层加载：

1. **始终加载**：`roles/<role>/AGENTS.md`。角色 `AGENTS.md` 包含职责和知识索引，每条知识附带 2-3 句摘要，足以判断是否需要读全文
2. **按需加载（分层）**：优先 `Read` skill/principle/insight（更短、更可执行）；当需要"证据/边界条件/反例/权衡上下文"时，再升级加载 experience（通常从提炼知识里的 `source` 或 "Escalate to experience if" 进入）

## Experience 的唤醒（加载）策略（推荐）

- **默认分层**：`roles/<role>/AGENTS.md` → skill/principle/insight → experience（按升级条件回溯）
- **少量直达**：出现明确症状（特定报错/异常现象）或正在做高风险任务（迁移、发布/回滚、权限/凭证相关）时，可直接用关键词检索并 `Read` 某条 experience
- 详细规范：`base/knowledge-sedimentation.md`

## 哪些知识应该"常驻 context"（原则）

把知识是否常驻 context 视为一个工程权衡：**高频 + 高风险 + 短小稳定** 的内容更适合常驻；**低频 + 语境化 + 易过时 + 体量大** 的内容更适合按需加载。

### 常驻（强烈建议每次任务都确保在 context）

- `AGENTS.md`：协作规则、工作流、安全底线、加载策略（本文件）
- `roles/<role>/AGENTS.md`：角色职责 + 知识索引（决定后续读什么）

> 经验法则：如果某条规则"做错一次就会造成不可逆损失/大范围误导"，而且能压缩成几条 bullet，就应该进入 `AGENTS.md` 或 `roles/<role>/AGENTS.md`（而不是散落在长文档里）。

### 按需加载（默认）

- **skill / principle / insight**：通过 `AGENTS.md` 索引摘要 + front matter 的 `triggers` 命中后加载
- **experience**：默认不常驻；作为"证据/边界/反例/决策上下文"在需要时升级加载

### 触发式"优先加载"（不要求常驻，但建议尽早 Read）

当任务命中这些场景时，相关文档应尽早加载（通常在 `AGENTS.md` 中只保留入口/提醒，正文放 skill/principle）：

- **接触凭证 / 权限 / token**：`base/principles/credential-safety.md`
- **任何写操作**（多 agent 并行）："worktree"相关规范（见 `AGENTS.md` 与 `base/principles/git-worktree.md`）

### 不建议常驻（应该按需）

- 长篇背景材料、完整排障流水账、历史日志等（应归入 experience，并提供 triggers / 可复用 checklist）
- 容易过期的"事实快照"（环境路径、版本号、集群状态等）：更适合写在 experience 的证据里并带日期，或写在项目 runbook/README 中并明确验证方式

## Context 压缩后重新加载

长 session 中 context 会被自动压缩（compaction），压缩后根 `AGENTS.md` 和角色 `AGENTS.md` 的内容可能被摘要掉。**agent 在感知到 context 被压缩后，必须重新 `Read` 以下文件**：

1. `AGENTS.md`（本文件）
2. `roles/<role>/AGENTS.md`（角色知识索引）

判断依据：如果你发现自己不确定当前角色的知识索引内容、或不记得协作规则的细节，说明 context 已被压缩，立即重新加载。

## 写摘要的要求

索引中每条知识的摘要必须包含**足够的关键词**，让 agent 能判断是否与当前任务相关。不要只写「跨层 API 重构」，要写「四层修改顺序、Python 三处间接调用、参数重排序陷阱」——这样 agent 在做相关修改时能命中关键词。

## Escalate to experience if

- 需要理解"分层加载"在实际 session 中如何运作（具体的加载顺序决策案例）
- 需要判断某条知识是否应该从 role 提升到 base
