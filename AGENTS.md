# Global Agent Rules

This repository stores reusable agent knowledge using a layered structure:

- `base/`: shared knowledge for all agents
- `roles/`: role-specific knowledge and private context

Knowledge should be classified before being added:

- `experience`: concrete incidents, postmortems, and decision records
- `skills`: reusable workflows and checklists
- `principles`: durable rules and behavioral constraints
- `insights`: generalized patterns learned from repeated work

Loading guidance:

1. Read [base/AGENTS.md](/Users/wangkang/my_agent_skills/base/AGENTS.md) for shared knowledge.
2. If working in a specific role, also read `roles/<role>/AGENTS.md`.
3. Load only the specific skill or reference material needed for the task.

Current shared skill inventory:

- [skill-creator](/Users/wangkang/my_agent_skills/base/skills/skill-creator/SKILL.md)

## Git 提交规则

- 进行 `git commit` 时，必须编写清晰的 `commit message`。
- `commit message` 应使用简洁的一行摘要，直接说明本次改动结果，不要写成模糊描述。
- 推荐格式：`<type>: <what changed>`。

常用 `type`：

- `feat`: 新增功能
- `fix`: 修复问题
- `docs`: 文档更新
- `refactor`: 重构但不改变行为
- `test`: 测试相关改动
- `chore`: 杂项维护

示例：

- `feat: add eat source ingestion for attachments`
- `fix: resolve eat target path under home`
- `docs: clarify eat update workflow`

如果一次改动包含多个不相关主题，应拆分提交，而不是用一条含糊的 `commit message` 混在一起。
