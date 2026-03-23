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

1. Read [base/AGENTS.md](base/AGENTS.md) for shared knowledge.
2. If working in a specific role, also read `roles/<role>/AGENTS.md`.
3. Load only the specific skill or reference material needed for the task.

Current shared skill inventory:

- [skill-creator](base/skills/skill-creator/SKILL.md)
- [skill-creator-codex](base/skills/skill-creator-codex/SKILL.md)
- [eat](base/skills/eat/SKILL.md)

## Git Commit Rules

- Every `git commit` must use a clear `commit message`.
- The `commit message` should be a concise one-line summary that states the result of the change directly, not a vague description.
- Recommended format: `<type>: <what changed>`.

Common `type` values:

- `feat`: add a new feature
- `fix`: resolve a bug or problem
- `docs`: update documentation
- `refactor`: restructure code without changing behavior
- `test`: add or update tests
- `chore`: maintenance or housekeeping work

Examples:

- `feat: add eat source ingestion for attachments`
- `fix: resolve eat target path under home`
- `docs: clarify eat update workflow`

If one set of changes includes multiple unrelated topics, split them into separate commits instead of combining them under one vague `commit message`.
