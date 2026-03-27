---
name: eat
description: 当用户希望把当前上下文、文件、仓库、URL、图片、PDF 或其他来源沉淀为可复用知识，或明确触发 `/eat` 时使用。
---

# Eat

## 概述

这个技能用于把当前上下文中真正值得长期复用的部分沉淀成知识。

目标不是“保存一切”，而是：

- 判断哪些内容值得保留
- 判断应放在共享层还是角色层
- 选择最合适的知识类型
- 生成可复用草稿或下游交接信息

开始提案前先读取：

- `base/notes/knowledge-sedimentation.md`：沉淀边界、目标类型、shared vs role 判断
- `references/knowledge-placement.md`：根目录解析、路径映射、落盘规则
- `references/output-contract.md`：正常模式和维护模式的输出格式

## Modes

- `/eat` 或 `/eat project`：目标根目录是当前项目根目录
- `/eat home`：目标根目录是 `$HOME/my_agent_skills`
- `/eat update`：只基于当前会话反思 `eat`
- `/eat update all`：基于当前会话 + 当前磁盘上的 `eat` 维护资产一起反思

`project` 和 `home` 是保留别名，不接受任意路径参数。

## Core Rules

### 1. 先提案，后写入

无论是普通沉淀还是维护 `eat`：

- 第一次回复只给分析和提案，不直接改文件
- 所有可写入候选项必须编号为 `1. 2. 3.`
- 只有在用户明确确认后，才执行写入
- 用户可以确认全部，也可以只确认部分，例如 `1 同意`、`1 3 同意`

### 2. 优先处理最合适的来源

普通模式按以下顺序选来源：

1. 用户当前消息里明确指定的来源
2. 最近一组附件
3. 当前会话上下文

对混合来源：

- 尽量处理所有可读来源
- 对不可读或不支持的来源标记 `skipped: <reason>`
- 不因为一个来源失败就放弃整组来源

### 3. 不值得长期复用的内容不要存

是否应沉淀、应存成什么类型，遵循 `base/notes/knowledge-sedimentation.md`。

### 4. `skill` 交给 `skill-creator-codex`

当候选知识被判定为 `skill` 时：

- `eat` 只负责判断、路径建议和 handoff
- `eat` 不直接产出最终 `SKILL.md`
- 用户确认后，必须切换到 `skill-creator-codex`

## Decision Step

对每个候选项都先完成两个判断：

1. 它是否值得沉淀
2. 如果值得，应该落到什么目标与什么路径

具体判断标准不要在这里重复定义：

- 目标类型与 shared / role 归属：看 `base/notes/knowledge-sedimentation.md`
- 目标根目录与精确路径：看 `references/knowledge-placement.md`

## Output

普通模式和维护模式的输出格式，统一遵循 `references/output-contract.md`。

## Write Phase

用户确认后再执行写入：

1. 如果目标文件已存在，先读取
2. 尽量局部追加或合并，不整文件重写
3. 复用目标文件已有语气和标题风格
4. 明显同题的候选项合并到一个文件
5. 与现有稳定规则重复的内容跳过，并说明原因
6. 只写入用户明确确认过的编号项
7. 如果确认表达无法唯一映射到编号项，先复述识别到的编号并等待澄清
8. 若确认写入的是 `skill`，切换到 `skill-creator-codex`

对 `eat` 自维护：

- 以 `$HOME/my_agent_skills` 下的源技能为准
- 先改源技能，再同步已安装副本
- 修改完成后检查源技能与已安装副本是否一致
- 未完成一致性校验前，不要宣称 `eat` 已更新完成
