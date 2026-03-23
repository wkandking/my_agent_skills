# Role Template

This directory is a scaffold only. Do not load `_template` as a real role.
Copy it to `roles/<role-name>/` and customize it before use.

Replace `<role-name>` with the actual role and customize this file.

## Purpose

Describe what this role owns, what it does not own, and when it should be used.

## Private Knowledge Layout

- `experience/`: role-specific incidents and retrospectives
- `principles/`: role-specific rules and preferences
- `skills/`: role-specific workflows
- `insights/`: recurring patterns learned by this role
- `questions.md`: unresolved questions worth revisiting

## Operating Notes

1. Reuse `base/` knowledge first.
2. Add role-private material only when it would add noise to shared knowledge.
3. Promote repeated role-local patterns into `base/` when they become broadly useful.
