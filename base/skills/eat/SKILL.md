---
name: eat
description: 当用户希望从当前上下文、文档、仓库、图片、PDF、URL 或其他来源中提取可复用知识，判断知识该放在哪里，起草 AGENTS、principles、insights、experience、skills 文档，或使用 /eat、/eat update、/eat update all 维护知识时使用。
---

# Eat

## 概述

这个技能用于“吃掉”当前上下文，把真正值得长期复用的内容沉淀成知识。

目标不是把所有内容都保存下来，而是：

- 识别哪些内容值得保留
- 判断它应该放在共享层还是角色层
- 选择合适的知识类型
- 产出可以直接复用的 Markdown 草稿
- 在获得用户明确确认后，再把内容写入目标知识库

决定落库位置前，先读取 `references/knowledge-placement.md`。

## 调用方式

支持以下简写：

- `/eat`
- `/eat project`
- `/eat home`
- `/eat update`
- `/eat update all`

解释规则：

- `/eat` 等同于 `/eat project`
- `/eat project`：目标知识根目录为当前项目根目录
- `/eat home`：目标知识根目录为 `$HOME/my_agent_skills`
- `/eat update`：只基于当前会话，反思 `eat` 在这次对话中的问题
- `/eat update all`：基于当前会话 + 当前磁盘上的 `eat` 维护资产一起反思

`project` 和 `home` 是保留别名，不接受任意路径参数。

## 核心规则

### 1. 第一次回复只给方案，不直接写文件

无论是普通沉淀还是维护 `eat` 自身：

- 第一次回复只给分析和提案
- 不直接修改任何文件
- 只有在用户明确确认后，才执行写入

### 2. 优先选择最合适的来源

普通沉淀模式按以下顺序选择来源：

1. 用户在当前消息里明确指定的来源
2. 最近一组附件
3. 当前会话上下文

混合来源时：

- 尽可能处理所有可读来源
- 不可读或不支持的来源要标记为跳过，并给出简短原因
- 不因为其中一个来源失败就放弃整组来源

### 3. 不是所有内容都该保存

以下情况通常不应沉淀：

- 只适用于一次临时情境
- 很快会失效
- 只是当前任务的重复表述
- 缺少足够上下文，后续无法安全复用
- 已经被现有稳定规则覆盖，没有新增价值

边界不清时，要明确说明风险。

### 4. 明确区分共享知识和角色知识

先判断内容属于：

- 共享知识：跨角色通用
- 角色知识：强依赖某个角色的职责、工具、解释口径或输出标准

如果是在 `home` 模式下：

- 共享知识默认写入 `base/`
- 角色知识默认写入 `roles/<role>/`

## 知识分类流程

对每个候选知识项，依次判断：

1. 它属于共享还是角色私有
2. 它更适合写成：
   - `AGENTS.md` 中的入口规则
   - `principles/` 中的稳定原则
   - `insights/` 中的规律性认知
   - `experience/` 中的具体事件记录
   - `skills/` 中的可复用流程
3. 给出精确推荐路径
4. 输出可直接粘贴的 Markdown 草稿

## 正常模式的输出格式

先描述来源集合：

```md
## Source Set
- Target Root: `<exact path>`
- Source Mode: <explicit source | recent attachment group | current conversation>
- Processed Sources:
  - `<source>`: <processed | skipped: reason>
```

如果目标是 `home`，还要额外说明：

```md
- Existing Shared Layer: `<root>/base`
- Existing Roles:
  - `<role>`
- Placement Default:
  - `shared -> base`
  - `role-specific -> roles/<role>`
```

然后对每个来源输出：

```md
## 来源总结：<source label>
- Source Type: <file | repo | image | pdf | document | url | pasted text | conversation>
- Key Takeaway: <1-3 句中文总结>
```

对每个保留项输出：

```md
### 候选知识：<short statement>
- Scope: <shared | role-specific:<role>>
- Knowledge Type: <AGENTS rule | principle | insight | experience | skill>
- Recommended Path: `<exact repository path>`
- Why Here: <1-3 句说明>
- Draft:

```md
<paste-ready markdown>
```
```

对不应保存的项输出：

```md
### 候选知识：<short statement>
- Scope: <shared | role-specific:<role> | unclear>
- Decision: Do Not Store
- Reason: <原因>
```

最后补：

```md
## 合并结论
- Summary: <中文总结>
- Cross-Source Notes:
  - <note>

## 应用摘要
- Target Root: `<exact path>`
- Files To Create:
  - `<path>`
- 待更新文件:
  - `<path>`
- Confirmation Required: `No files will be changed until the user explicitly confirms the full write.`
```

如果没有任何内容值得保存，就直接说明，不要求确认。

## 维护模式

### `/eat update`

只使用当前会话作为证据来源，不主动读取现有 `eat` 维护资产，除非用户明确要求。

### `/eat update all`

使用当前会话 + 当前磁盘上的 `eat` 维护资产，例如：

- `base/skills/eat/SKILL.md`
- `base/skills/eat/references/knowledge-placement.md`
- 其他直接相关的 `eat` 文件

两种模式都必须：

- 先给提案
- 不提前改文件
- 只有在用户明确确认后才修改
- 若修改通过，应先更新 `$HOME/my_agent_skills` 下的源技能，再同步已安装副本

维护模式下使用以下格式：

```md
## 失败摘要
- Issue: <eat 做错了什么>
- Evidence Scope: <current context only | current context + existing eat assets>

## 根因
- <1-3 句说明>

## 规则变更
- <拟议规则变化>

## 待更新文件
- `<path>`

## 补丁草稿
```

## 放置规则

- 高频、短小、开工即需的规则：放 `AGENTS.md`
- 稳定约束：放 `principles/`
- 可泛化模式：放 `insights/`
- 具体事件和复盘：放 `experience/`
- 多步骤可复用流程：放 `skills/`

## 写入规则

在用户确认后执行写入时：

1. 如果目标文件已存在，先读取
2. 尽量局部追加或合并，不整文件重写
3. 复用目标文件的局部语气和标题风格
4. 主题明显一致时，把多个候选项合并到一个新文件中
5. 若发现候选内容与现有规则重复，应跳过写入并说明已覆盖

## 自维护边界

`eat` 更新自己时，以 `$HOME/my_agent_skills` 下的源技能为准，不要把已安装副本当成唯一真相。
