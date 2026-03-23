# Agent Skills

This repository is organized following the structure of the
[`agent-knowledge-framework`](https://github.com/st1page/agent-knowledge-framework):

```text
.
├── AGENTS.md
├── base/
│   ├── AGENTS.md
│   ├── experience/
│   ├── insights/
│   ├── principles/
│   └── skills/
└── roles/
    └── _template/
        ├── AGENTS.md
        ├── experience/
        ├── insights/
        ├── principles/
        ├── skills/
        └── questions.md
```

Current shared skills:

- `base/skills/skill-creator`
- `base/skills/skill-creator-codex`
- `base/skills/eat`

Knowledge types:

- `experience`: specific retrospectives, incidents, and decisions
- `skill`: reusable procedures and operational playbooks
- `principle`: stable rules and constraints
- `insight`: patterns distilled from repeated experience

Use `base/` for knowledge shared by all agents. Add role-specific knowledge
under `roles/<role-name>/`.
