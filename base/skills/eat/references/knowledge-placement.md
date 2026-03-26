# 知识放置指南

当你决定提取出的知识该放到哪里时，使用本指南。

所有目标路径都应在选定的知识根目录下解析。

## 目标根目录解析

按以下规则解析目标根目录：

1. 用户使用 `/eat` 且不带参数时，目标根目录是当前项目根目录
2. 用户使用 `/eat project` 时，目标根目录是当前项目根目录
3. 用户使用 `/eat home` 时，目标根目录解析为 `$HOME/my_agent_skills`
4. 在 `home` 模式下，`$HOME/my_agent_skills` 是容器根：
   - 共享知识通常放到 `base/`
   - 角色知识通常放到 `roles/<role>/`
5. `eat` 不接受任意路径参数或普通目录名作为目标根目录
6. 只有 `project` 和 `home` 是合法的显式目标别名

示例：

- `/eat` -> 当前项目根目录
- `/eat project` -> 当前项目根目录
- `/eat home` -> `$HOME/my_agent_skills`

## 来源摄取规则

按以下顺序选择来源：

1. 用户明确点名的来源
2. 最近一组附件
3. 当前会话

支持的来源类型：

- 文件
- 目录和代码仓库
- 附件图片
- 本地图像路径
- PDF 和文档
- URL
- 粘贴文本

对混合来源：

- 处理所有可可靠读取的来源
- 对不支持或不可读来源给出简短跳过原因
- 不要因为一个来源失败就放弃整组

## 第一层判断：共享还是角色私有

符合以下情况时，应视为共享知识：

- 规则、模式或流程对多个角色都有帮助
- 不依赖特定角色的职责或解释口径

符合以下情况时，应视为角色知识：

- 依赖某个角色的职责边界
- 主要使用某个角色特有工具
- 依赖特定领域解释规则
- 依赖某个角色独有的报告或证据标准

## 目标位置指南

### `AGENTS.md`

把以下类型内容放到 `AGENTS.md`：

- 入口级加载规则
- 仓库布局规则
- 高频、短小的操作提示
- 默认加载顺序

不适合：

- 长篇背景解释
- 一次性事件
- 多步骤完整流程

### `notes/`

`notes/` 用于所有**非流程型**知识。放到 `notes/` 后，再用 frontmatter `kind` 指定语义：

- `kind: principle`
  - 稳定约束
  - 强行为规则
  - 决策边界

- `kind: insight`
  - 启发式
  - 规律性认知
  - 可复用判断框架

- `kind: experience`
  - 具体历史事件
  - 复盘
  - 一次性案例和证据链

### `skills/`

放可复用的多步骤流程：

- 操作流程
- review checklist
- 运行手册
- 输出结构需要标准化的任务

### `questions.md`

放已知未知：

- 暂时还不稳定，不足以写成 `note`
- 需要保留下来提醒未来任务的疑问
- 还没有足够证据升级成原则、insight 或经验案例

## 共享与角色路径示例

如果目标根目录本身就是一个轻量知识库：

- 共享入口规则：`<root>/AGENTS.md`
- 共享 note：`<root>/notes/<topic>.md`
- 共享技能：`<root>/skills/<skill-name>/SKILL.md`
- 共享问题：`<root>/questions.md`

- 角色入口规则：`<root>/roles/<role>/AGENTS.md`
- 角色 note：`<root>/roles/<role>/notes/<topic>.md`
- 角色技能：`<root>/roles/<role>/skills/<skill-name>/SKILL.md`
- 角色问题：`<root>/roles/<role>/questions.md`

## `home` 模式映射

当目标根目录是 `$HOME/my_agent_skills` 时，应按当前仓库结构映射：

- 共享入口规则：`<root>/base/AGENTS.md`
- 共享 note：`<root>/base/notes/<topic>.md`
- 共享技能：`<root>/base/skills/<skill-name>/SKILL.md`

- 角色入口规则：`<root>/roles/<role>/AGENTS.md`
- 角色 note：`<root>/roles/<role>/notes/<topic>.md`
- 角色技能：`<root>/roles/<role>/skills/<skill-name>/SKILL.md`
- 角色问题：`<root>/roles/<role>/questions.md`

在 `home` 模式下，提案应主动查看 `<root>/roles/` 下已有角色，并明确说明为什么内容应放到 `base` 或某个角色目录。

## 根目录初始化

如果目标知识根目录缺少必要结构，并且用户已确认写入，只初始化真正需要的部分：

- `<root>/AGENTS.md`
- `<root>/notes/`
- `<root>/skills/`
- `<root>/questions.md`

如果需要角色层，再按需创建：

- `<root>/roles/<role>/AGENTS.md`
- `<root>/roles/<role>/notes/`
- `<root>/roles/<role>/skills/`
- `<root>/roles/<role>/questions.md`

不要提前创建没有被内容命中的角色目录。

## 起草规则

当你推荐目标路径时：

1. 给出符合当前仓库结构的最窄路径
2. 高频短规则优先落到现有入口文件
3. 如果最佳目标文件不存在，直接推荐新文件路径，而不是硬塞到错误文件里
4. 如果是 `note`，必须同时给出 `kind`
5. 解释为什么该目标比附近替代项更合适

## 写入规则

执行已确认写入时：

1. 如果目标文件存在，先读一遍
2. 尽量局部追加或合并，不整体覆盖
3. 复用文件已有的局部语气和标题风格
4. 多个候选项若明显同题，应合并写入一个文件
5. 若候选内容会重复已有规则，则跳过写入并说明原因
6. 默认所有新增或追加内容都应使用中文，除非用户明确要求其他语言

## Eat 自维护规则

当 `eat` 更新自己时：

1. `/eat update` 只依赖当前会话，除非用户明确补充更多材料
2. `/eat update all` 可以读取当前 `eat` 维护资产 + 当前会话
3. 两种模式都必须先出提案，再改文件
4. 两种模式都必须得到用户明确批准
5. 源技能以 `$HOME/my_agent_skills` 下的版本为准，先改源，再同步安装副本
