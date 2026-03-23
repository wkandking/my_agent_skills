# Base Knowledge Index

This directory contains knowledge shared across all agents.

## Directories

- `experience/`: shared postmortems and concrete lessons
- `principles/`: stable cross-role rules
- `skills/`: reusable operational workflows
- `insights/`: generalized observations distilled from repeated work

## Available Shared Skills

- [skill-creator](/Users/wangkang/my_agent_skills/base/skills/skill-creator/SKILL.md)
  Use when creating a new skill or updating an existing one.
- [skill-creator-codex](/Users/wangkang/my_agent_skills/base/skills/skill-creator-codex/SKILL.md)
  Use when creating or adapting skills for Codex and installing them locally.
- [eat](/Users/wangkang/my_agent_skills/base/skills/eat/SKILL.md)
  Use when extracting reusable knowledge from the current context, deciding where shared or role-specific guidance should live, and optionally writing approved knowledge into a target root.

## Usage Rules

1. Prefer `base/` knowledge unless the task clearly belongs to a specific role.
2. Keep `SKILL.md` concise; move long material into `references/` or `scripts/`.
3. Record one-off incidents in `experience/`, not in skills.
