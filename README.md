# Agent Knowledge Repo

This repository stores reusable knowledge for coding agents that work across many kinds of tasks.

The design goal is to keep the active system small:

- keep role entrypoints short
- keep executable workflows in `skills/`
- keep non-procedural knowledge in `notes/`
- keep unresolved uncertainties in `questions.md`

## Structure

```text
my_agent_skills/
├── AGENTS.md
├── README.md
├── base/
│   ├── AGENTS.md
│   ├── skills/
│   └── notes/
├── roles/
│   ├── generalist-engineer/
│   ├── mechanism-analyst/
│   └── performance-infra-tester/
└── tools/
```

## Active Roles

- `generalist-engineer`: default role for day-to-day engineering work
- `mechanism-analyst`: explains why a system behaves the way it does
- `performance-infra-tester`: handles benchmark, load, stress, and performance reporting work

## Knowledge Model

### `skills/`

Executable workflows. Read these when the main question is "how do I do this?"

### `notes/`

Non-procedural reusable knowledge. Each note keeps its semantic type in frontmatter:

- `kind: principle` for hard rules and constraints
- `kind: insight` for decision heuristics and reusable understanding
- `kind: experience` for concrete historical cases and evidence

### `questions.md`

Known unknowns that are worth keeping visible but are not yet stable enough to become active knowledge.

## Default Load Path

1. Read root `AGENTS.md`
2. Read the relevant role `AGENTS.md`
3. Read one relevant `skill` or `note`
4. Read one more `note` or `questions.md` only if the task still needs historical evidence or boundary detail

## Shared Skills Kept Active

- `base/skills/eat`
- `base/skills/skill-creator-codex`

## Collaboration

- All writes happen in a worktree
- Main workspace stays read-only for exploration
- Important changes should be reviewable as PR-sized diffs
