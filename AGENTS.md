# Agent Knowledge Repo

Before starting any task, every agent must read this file and the relevant role `AGENTS.md` files.

## Repository Structure

- `base/` stores shared knowledge used across roles
- `roles/` stores role-specific knowledge and entrypoints

## Active Roles

- `generalist-engineer`
- `mechanism-analyst`
- `performance-infra-tester`

## Shared Layer

`base/AGENTS.md` is the shared entrypoint for cross-role knowledge.

## Load Rule

1. Read this file
2. Read the relevant role `AGENTS.md`
3. If the task touches shared concerns, read `base/AGENTS.md`
4. Read one relevant shared or role-specific `skill` or `note`
5. Read `questions.md` or one extra `note` only if needed

## Knowledge Model

- `skills/`: executable workflows
- `notes/`: rules, decision heuristics, and historical cases
- `questions.md`: known unknowns

## Collaboration

- Any write must happen in a worktree
- Do not develop in the main workspace
- Important changes go through PR review
