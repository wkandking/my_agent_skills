# 经验沉淀规范

当用户要求「总结经验」「沉淀一下」时，不要无脑堆到一个文件里。**先判断这条知识的性质和受众，再决定放在哪里**。

## 知识分类与存放位置

| 类别 | 定义 | 存放位置 | 示例 |
|---|---|---|---|
| **experience** | 具体事件的复盘和洞察：踩过的坑、发现的有效做法、关键决策的上下文 | `roles/<role>/experience/` | 「改返回类型后遗漏了下游消费者的适配」「发布流程首次跑通的完整记录」 |
| **skill** | 可复用的操作流程：怎么做某类事、checklist、代码模式 | `roles/<role>/skills/` 或 `base/skills/` | 「跨层 API 重构的分层修改顺序」「FFI 方法接受多种类型的模式」 |
| **principle** | 抽象的行为准则：应该/不应该做什么，与具体技术无关 | `roles/<role>/principles/` 或 `base/principles/` | 「每个功能用独立 worktree」「集成测试必须跑」 |
| **insight** | 从多次 experience 中归纳出的规律性认知：不是操作步骤（skill），也不是行为准则（principle），而是对「为什么会这样」的理解 | `roles/<role>/insights/` 或 `base/insights/` | 「迭代式 review 比一次性修复更可靠」「Rust 做状态维护 + Python 做边界过滤的职责划分模式」 |

## 判断放 role 还是 base

- **只对本角色有意义** → `roles/<role>/`。例如某项目的 FFI 双层提取模式，只有该角色会用到
- **多个角色都可能遇到** → `base/`。例如「改了函数返回类型后要追踪所有消费者」「skip ≠ pass」，这些是通用工程经验

问自己：「如果另一个角色遇到类似情况，这条知识对他有用吗？」有用就放 base。

## 从 experience 提炼到 skill/principle/insight

experience 是原始素材，skill、principle 和 insight 是提炼后的可复用知识。沉淀时要做两步：

1. **先写 experience**：记录具体事件——不只是犯错，也包括有效的做法、关键决策的权衡过程、首次跑通某个流程的完整记录
2. **再看能否提炼**：从 experience 中抽取可复用的模式，补充到已有的 skill、principle 或 insight 文档中；如果是全新主题则新建文档

提炼方向的区分：
- **skill**：「下次遇到同类事该怎么操作？」→ 操作流程、checklist、代码模式
- **principle**：「下次遇到同类事该遵守什么准则？」→ 行为约束、设计原则
- **insight**：「为什么会这样？背后的规律是什么？」→ 规律性认知、架构模式、跨场景的泛化理解

**提炼不求大而全。** skill、principle、insight 都是 role private 的知识，扎根在角色的具体场景里就够了，不需要上升到普适真理。过度抽象反而丢失实用性——「改 API 返回类型后要追踪所有消费者」谁都知道，但「在多层架构下，改返回类型时最外层的间接消费者最容易遗漏」才是有价值的 insight。

不要只写 experience 不提炼——那只是日记。也不要只写 skill 不留 experience——丢失了具体上下文，后人无法理解「为什么有这条规则」和「当时是怎么做到的」。

## Experience 的唤醒（加载）策略：分层加载 + 少量直达

agent 的上下文窗口有限，experience 往往比 skill/principle/insight 更长、更语境化，所以默认不应把 experience 当成“第一入口”。推荐采用 **分层加载（layered retrieval）**：

1. **先从索引入手**：读 `roles/<role>/AGENTS.md` 的知识索引，定位可能相关的条目（skill/principle/insight/experience）。
2. **优先加载提炼知识**：先 `Read` skill/principle/insight（它们更短、更可执行，且包含 triggers）。
3. **再按条件升级到 experience**：当需要“证据/边界/反例/上下文”时，再继续加载 experience。

同时保留“少量直达”的例外：当出现明确的 **症状型线索**（特定报错/异常现象）或正在执行 **高风险任务**（数据迁移、发布/回滚、权限/凭证相关操作等）时，可以直接通过 triggers/关键词去命中某条 experience。

### 让 experience 能被正确唤醒：两处信号

- **在 skill/principle/insight 里写升级条件**：正文里加一个固定小节（推荐命名 `## Escalate to experience if`），列出“什么时候必须回溯 experience”（例如：遇到某类报错、需要做权衡、需要确认边界条件）。
- **experience 自身提供可检索线索（可选）**：experience 文件可在开头增加 `## Triggers（可选）` 小节，写 3-8 个真实关键词（报错片段、组件名、命令名、文件路径、API 名）。这不是为了“常驻加载”，而是为了在症状出现时能被 `rg` 快速命中。

## Questions：记录已知的未知（known unknowns）

四种知识类型（experience/skill/principle/insight）都是**某种程度上已确认的**知识。但工作中经常产生"注意到了、有假说、但没条件验证"的疑问——它不是 experience（还没发生过），不是 skill（不确定能不能这么做），也不适合勉强写成低信心的 insight。

`questions.md` 就是放这些东西的地方。它不是第五种 knowledge type，而是知识的**前体**——一个 question 最终要么被验证变成 experience → skill/principle/insight，要么长期保持 open 状态作为"我们知道自己不知道"的标记。

### 定位

- **不是 TODO**：question 没有 deadline，不要求"尽快解决"。有些疑问可能几个月甚至更久都没有验证机会，这是正常的。
- **不是垃圾场**：写 question 时要带足够的上下文（来源 session、背景、验证思路），让未来遇到相关场景的 agent 能判断"这个 question 和我当前的任务有关吗"。
- **有索引**：在角色 `AGENTS.md` 索引的 Questions 小节标注条目数，让 agent 知道有待验证的问题存在。

### 生命周期

```
session 中产生疑问 → 写入 questions.md（checkbox / ## 小节）
                         ↓ 未来某次 session 有机会验证
                     写 experience → 提炼 skill/principle/insight
                         ↓
                     回到 questions.md 勾 checkbox，注明去向
```

如果一个 question 长期 open，**不要因此删除它**。它的存在本身就是有价值的信号——下次有人碰到相关场景时，看到这个 question 会知道"这里有不确定性，小心"。

### 什么时候写 question

- session 中注意到某个行为"不确定是不是总是这样"但没时间深究
- 提炼 skill/principle 时信心不足（只有一个数据点），先记为 question
- 读文档/代码时发现矛盾或模糊之处，但当前任务不需要解决它

### 格式

存放在 `roles/<role>/questions.md`，模板见 `roles/_template/questions.md`。

## 自动沉淀：完成重要工作后主动反思

**不要等用户提醒才沉淀经验。** 完成以下类型的工作后，agent 应主动提出沉淀：

- PR review 修复（尤其是多轮迭代的）
- 跨层 bug 修复
- 首次跑通某个流程（发布、部署、新工具集成）
- 踩了非显而易见的坑

**具体做法**：工作完成后，主动问自己五个问题：
1. 这次有没有踩坑或发现反直觉的行为？→ 写 experience
2. 能不能提炼出可复用的 checklist 或模式？→ 写/更新 skill
3. 有没有值得记住的抽象原则？→ 写/更新 principle
4. 有没有跨场景可泛化的规律性认知？→ 写/更新 insight
5. 有没有注意到但没条件验证的疑问？→ 写入 questions.md

有内容就创建分支、写文档、提 PR。不需要用户说「沉淀一下」。

## 实操 Checklist（把沉淀当成”可复用产物”交付）

沉淀不是”写点总结”，而是产出让后人**可回溯、可执行、可检索**的知识：

- **证据先行**：命令/日志/样本量/时间范围/异常占比先写清楚，结论能复核。
- **可回溯引用（优先写”产出物”）**：优先补齐本次产出的 PR / commit / 文档（wiki、runbook、设计稿）引用；避免把”机器名/IP/路径”这类上下文硬塞到 References（它们更适合放在「背景/证据」里）。
- **写清决策依据**：关键决策不要只写”我觉得/项目惯例”，要落到「遵循了哪条 principle/insight」或「参考了哪条 experience/skill」，让后续维护者能复用你的判断逻辑。
- **三件套拆分**：experience（发生了什么+证据链）→ skill（下次怎么做）→ insight（为什么会这样）。
- **入口优先**：skill 首步先确认”问题是否存在/范围多大”（bench/基线/smoke/异常占比），再分层排查。
- **前置条件**：写清在哪台机器做、需要哪些权限、哪些步骤无权限就跳过；强调只读安全边界。
- **可检验判据**：每一步给可比较指标（p95、错误率、delta%、抖动幅度）。
- **可检索**：README 摘要与 triggers 覆盖真实关键词；PR 描述随 push 同步更新（自动化脚本避免 shell 误执行文本）。
- **联动更新（新建/修改文件后）**：
  - skill/principle/insight 的 front matter 必须有 `description` + `triggers`（对照本文 Front Matter 规范，不要只抄已有文件——已有文件可能本身不合规）
  - 更新角色 `AGENTS.md` 索引（新增条目、更新 questions 条目数）
  - 交叉引用：experience ↔ skill ↔ plan 之间的链接是否完整且不冗余
  - 通读改动区域：逐块修改后整体回看，检查是否有矛盾或重复

## Experience 写作建议（引用就地）

experience 不要求 YAML front matter，也**不强制**固定章节。重点是保证 **可复核**（证据）、**可回溯**（产出）、**可复用**（决策依据），并把链接/引用写在离它最近的位置：

- **产出物（PR/commit/doc）**：写在「结果」里（或紧挨着对应结论），不要为了凑结构单独加 References。
- **决策依据（principle/insight/skill/experience）**：写在对应的「关键决策」条目里，让读者能复用你的判断逻辑。
- **环境上下文（机器/IP/路径/参数）**：放在「背景/证据」里；这类信息不是“引用”，不要塞进 References 充数。

一个可参考的最小结构：

```markdown
# <一句话标题>

日期: YYYY-MM-DD

## Triggers（可选）
- "能让 `rg` 命中的真实关键词（报错/组件名/命令/路径）"

## 背景
发生在什么仓库/系统/环境？影响范围是什么？

## 证据与现象
贴命令/日志片段/样本范围/统计口径（不要只给结论）。

## 关键决策（含依据）
- 决策：做了什么选择？
  - 备选：还考虑过什么？为什么没选？
  - 依据：引用具体文档路径（principle/insight/skill/experience）或可验证证据

## 结果
最终怎么收敛？修复点/验证方式是什么？
- 产出（若有）：PR/commit/doc 链接或标识（优先写产出物）
- 沉淀（若有）：这次新增/更新了哪些 `skill/principle/insight`（写路径）

## 提炼检查
- [ ] Skill：能否提炼出可复用的 checklist/操作流程/代码模式？
- [ ] Principle：有没有值得记住的行为准则或硬性约束？
- [ ] Insight：有没有跨场景可泛化的规律性认知？
- [ ] Question：有没有注意到但没条件验证的疑问？
- [ ] AGENTS.md 索引：以上有产出时是否已同步更新？
```

### 写产出引用的底线（避免“找不到原始上下文”）

- 能贴 URL 就贴 URL（PR 页面、commit 页面、wiki 页面等）。
- 如果暂时还没产出 PR/文档：不要为了“看起来完整”硬写引用；可以先只写 `repo + branch + commit sha`，等产出物出现后再回填。

## Comment 已有 experience

agent 在工作中如果发现已有 experience 失效、需要补充、或与自己的经历相关，应在该 experience 文件末尾添加 comment。

### 触发场景

- **experience 失效**：系统升级、配置变更导致原有经验不再成立
- **跨角色关联**：另一个角色遇到了类似情况但结论不同

### 格式

在 experience 文件末尾添加 `## Comments` section（如果还没有），然后追加：

```markdown
## Comments

### <角色名> (<日期>)
简要说明（1-2 句），链接到相关文档。
```

### 边界

comment 是批注和索引，不是正文。如果 comment 内容开始包含深度分析或规律性归纳，应将其提炼为独立的知识产出（insight、skill 等），comment 里只留链接。

## 更新已有文档 vs 新建文档

- 如果已有文档覆盖了同一主题，**优先在已有文档中追加 section**，而不是新建文件
- 新建文件仅当主题完全独立时使用

## Front Matter 规范

skill、principle、insight 文件必须包含 YAML front matter，将 metadata 与正文分离。agent 通过 front matter 构建索引，决定是否加载全文。

```yaml
---
description: "1-2 句话描述，用于 AGENTS 索引"
triggers:
  - "触发加载的场景关键词"
source:
  - "roles/<role>/experience/xxx.md"
---
```

- **description**（必填）：简明描述这条知识是什么。直接复制到角色 `AGENTS.md` 的知识索引中
- **triggers**（必填）：列出应该加载这条知识的场景关键词。agent 匹配当前任务时用
- **source**（可选）：指向提炼出这条知识的 experience 文件路径。建立从提炼知识到原始素材的可追溯链

建议在正文里补一个固定小节（强烈推荐）：

- `## Escalate to experience if`：列出需要继续加载 experience 的条件（用于分层唤醒，避免“一上来就读长文档”或“永远不回溯导致踩坑复现”）。

示例：

```yaml
---
description: "四层接口（core → facade → binding → wrapper）改签名时的全链路同步流程和常见陷阱"
triggers:
  - "改公开方法签名"
  - "跨层重构"
  - "类型桩同步"
  - "re-export 检查"
source:
  - "roles/<role>/experience/YYYY-MM-DD-example.md"
---
```

experience 文件不需要 front matter——它的 metadata 已经由文件名中的日期和标题承载。

## 反模式

| 反模式 | 问题 | 正确做法 |
|---|---|---|
| 所有经验都堆到一个 experience 文件 | 后续检索困难，不同主题混杂 | 按主题拆分，一个事件一个文件 |
| 只写 experience 不提炼 skill | 知识停留在「那次踩了个坑」，不能指导未来行动 | experience 写完后审视：能否提炼出可复用的 checklist 或模式？ |
| 角色专有知识放到 base | 污染共享知识库，其他角色看了困惑 | 问「其他角色会用到吗？」不会就放 role 下 |
| 通用经验只放在 role 下 | 其他角色重复踩坑 | 通用工程经验（如 git、测试策略、CI）放 base |
