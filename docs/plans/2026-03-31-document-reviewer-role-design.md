# Document Reviewer Role Design

## Goal

为知识库新增一个专门的文档评审角色，使 agent 在面对技术设计文档和分析/报告类文档时，能够先进入稳定的评审视角，再按文档类型加载对应 skill，输出结构化 review 意见，而不是直接代写或泛化为普通工程角色。

## Why a New Role

现有角色覆盖的是：

- `generalist-engineer`：日常工程推进
- `mechanism-analyst`：解释系统为什么这样工作
- `performance-infra-tester`：生成性能证据与性能判断

它们都可能“顺手评审文档”，但都不是以“文档内容是否足以支持理解、判断和决策”为核心职责。

这会带来两个问题：

1. 技术设计文档 review 容易退化成普通代码评审思路，缺少对范围、约束、风险、验证路径的显式检查
2. 分析/报告类文档 review 容易混淆表达问题、证据问题和结论外推问题

因此需要一个独立角色，把文档评审从“附带动作”提升为“稳定入口”。

## Recommended Role Shape

推荐新增单一角色：`document-reviewer`

默认职责：

- 只做 review 并给出意见
- 不直接改写文档
- 先按文档类型选择 skill，再按需要补 1 个 note

这样做的原因：

- 符合仓库当前按“核心输出风险”建模角色的方式
- 与你的目标一致：一个角色承接多类文档 review，通过不同 skill 路由
- 后续新增文档类型时，只需要扩 skill，不需要反复拆角色

## Role Boundary

### Use This Role When

- 需要评审技术设计、方案、架构提案是否定义清楚、边界明确、可落地
- 需要评审分析报告、实验结论、问题分析是否证据充分、推理成立、结论不过度
- 需要把文档问题拆分成结构问题、证据问题、边界问题和结论问题
- 需要按文档类型选择不同 review workflow，而不是统一 checklist

### Do Not Use This Role For

- 直接代写或重写文档
- 纯语言润色、语法纠错、文风统一
- 没有文档载体的即兴方案设计
- 缺少可验证证据链的正式机制归因
- 正式 benchmark、load、stress、capacity 性能结论

## Initial Repository Layout

```text
roles/document-reviewer/
├── AGENTS.md
├── questions.md
├── skills/
│   ├── design-doc-review/
│   │   └── SKILL.md
│   └── analysis-report-review/
│       └── SKILL.md
└── notes/
    ├── review-the-decision-surface-not-just-the-prose.md
    └── separate-missing-evidence-from-missing-clarity.md
```

第一版先保持最小可用集：

- 2 个主 skill
- 2 个核心 note
- 1 个问题清单

`dont-upgrade-local-observations-into-general-rules.md` 可以作为第二阶段再补，因为它更像是分析报告 review 试跑后沉淀出来的稳定经验。

## Skill Design

### `skills/design-doc-review/SKILL.md`

适用对象：

- 技术设计文档
- 改造方案
- 架构提案
- ADR 风格决策文档

核心检查维度：

- 问题定义是否清楚
- 范围与非目标是否明确
- 约束、依赖、假设是否写清
- 方案是否真正回应问题，而不是绕开问题
- 是否覆盖主要失败模式和边界场景
- 是否给出验证、发布、回滚路径

建议输出结构：

- `Summary`
- `Findings`
- `Open Questions`
- `What Looks Solid`

这个 skill 的核心价值是：帮助 reviewer 判断文档是否能支持实现与评审，而不是只看“写得顺不顺”。

### `skills/analysis-report-review/SKILL.md`

适用对象：

- 分析报告
- 实验结论
- 问题归纳报告
- 复盘文档中的分析部分

核心检查维度：

- 证据是否支撑结论
- 样本和对比场景是否可比
- 是否混淆观察、解释、结论、建议
- 是否把相关性写成因果性
- 是否把局部现象写成普遍规律
- 是否遗漏限制条件、反例和适用边界

建议输出结构：

- `Summary`
- `Findings`
- `Assumptions To Verify`
- `Confidence Notes`

这个 skill 的核心价值是：帮助 reviewer 守住证据链和结论边界，而不是只挑报告表达方式。

## Note Design

### `notes/review-the-decision-surface-not-just-the-prose.md`

用途：提醒 reviewer 首先评估文档是否支持正确决策，而不只是语言是否通顺。

它回答的问题是：

- 这份文档是否让读者知道应该如何判断？
- 这份文档是否遗漏影响决策的关键条件？

### `notes/separate-missing-evidence-from-missing-clarity.md`

用途：区分“表达不清”和“论证没站住”。

它回答的问题是：

- 这是作者没说清楚，还是作者其实没有证据？
- 我给的反馈应该是“补写结构”，还是“补证据/收缩结论”？

## Questions to Keep Explicit

第一版建议保留这些未决项，而不是过早固化：

- 技术设计文档 review 默认是否必须覆盖测试与回滚
- 分析报告 review 默认是否要求原始数据或原始证据可复查
- 是否要单独支持“对外说明文档 / 教程文档”这一支

## Loading Model

`document-reviewer` 的默认加载顺序：

1. 读 `roles/document-reviewer/AGENTS.md`
2. 根据文档类型二选一：
   - `skills/design-doc-review/SKILL.md`
   - `skills/analysis-report-review/SKILL.md`
3. 如果争议集中在“判断逻辑”，再补 1 个 note
4. 如果边界仍不清楚，再看 `questions.md`

这个顺序保持了仓库的轻量原则：入口短、skill 负责执行、note 负责判断框架。

## Validation Plan

这个角色真正落地时，至少需要通过以下验证：

- `README.md` 的 `Active Roles` 包含 `document-reviewer`
- `tools/validate_knowledge_repo.py` 的 `ACTIVE_ROLES` 包含 `document-reviewer`
- `roles/document-reviewer/AGENTS.md` 引用的 skill、note、questions 路径都真实存在
- 新增 note 都带有 `kind`、`description`、`triggers` frontmatter
- `python3 tools/validate_knowledge_repo.py` 通过

## Non-Goals

第一版不做这些事：

- 不把所有文档类型一次性塞进角色
- 不做“自动改写文档”的职责
- 不把 note 写成 skill 的重复 checklist
- 不把 reviewer 角色和 `mechanism-analyst` / `performance-infra-tester` 的专门判断混为一体

## Rollout Recommendation

建议分两步推进：

1. 先落 `AGENTS.md`、两个 `SKILL.md`、两篇 `note`、`questions.md`
2. 用两到三个真实文档试跑，再决定是否新增更窄的 skill 或第三篇经验型 note

这个推进顺序比较稳：我们先把入口和评审动作做对，再根据真实 review 反馈补判断框架，而不是一开始就把目录堆满。
