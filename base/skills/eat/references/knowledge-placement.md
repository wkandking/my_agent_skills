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

## 这份参考只负责什么

这份文档只负责三件事：

1. 解析目标根目录
2. 把已选定的知识目标映射到精确路径
3. 约束确认后如何落盘

以下判断不在这里重复定义：

- 是否值得沉淀
- 属于 shared 还是 role
- 应该是 `AGENTS rule`、`note`、`skill`、`question` 还是 `Do Not Store`
- `note kind` 的选择

这些统一遵循 `base/notes/knowledge-sedimentation.md`。

## 路径模板

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

## 路径推荐规则

当你推荐目标路径时：

1. 给出符合当前仓库结构的最窄路径
2. 高频短规则优先落到现有入口文件
3. 如果最佳目标文件不存在，直接推荐新文件路径，而不是硬塞到错误文件里
4. 如果是 `note`，必须同时给出 `kind`
5. 解释为什么该目标比附近替代项更合适
