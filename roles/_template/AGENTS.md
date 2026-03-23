# <角色名称>

## 职责

<!-- 描述该角色的主要职责 -->

## 使用的工具

<!-- 列出该角色常用的工具 -->

## 相关知识

<!-- 列出该角色依赖的 base 知识 -->

## 角色知识索引

> 本索引是 agent 的**首要加载入口**。先读索引了解有哪些知识，再按需 `Read` 具体文件。不要一次性加载所有文档。
>
> 每条摘要必须包含**足够的关键词**，让 agent 能判断是否与当前任务相关。

### Skills
<!-- - `skills/<skill-name>/SKILL.md` — 关键词丰富的摘要（2-3 句） -->

### Principles
<!-- - `principles/xxx.md` — 关键词丰富的摘要（2-3 句） -->

### Insights
<!-- - `insights/xxx.md` — 关键词丰富的摘要（2-3 句） -->

### Experience（按需查阅，不常驻加载）
<!--
- `experience/xxx.md` — 关键词丰富的摘要（2-3 句）；写作结构可参考 `experience/TEMPLATE.md`

建议的“唤醒路径”：
1) 默认：先命中 skill/principle/insight（triggers）→ 再在其中通过 source / “Escalate to experience if” 升级加载 experience
2) 例外：当出现明确症状（报错/异常现象）或是高风险任务（迁移/发布/回滚/权限）时，可直接用关键词命中 experience
-->

### Questions（已知的未知）

- `questions.md` — N 条待验证（简单疑问一行 checkbox，需要背景的展开为 `##` 小节）
