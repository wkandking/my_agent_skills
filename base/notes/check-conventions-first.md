---
kind: principle
description: "Check existing project conventions before adding new behavior, such as naming, migration scripts, and CLI style, to avoid rework caused by inconsistency."
triggers:
  - "new feature"
  - "conventions"
  - "naming conventions"
  - "migration scripts"
---

# Check Project Conventions Before Making Changes

## Background

When adding new behavior to a project, such as a database column, a migration script, or a CLI command, failing to check the project's existing conventions often leads to an implementation that does not match the surrounding style and later has to be redone.

## Rules

1. **Review historical implementations of similar features before adding a new one**: search git history for similar PRs or commits to learn the project's conventions
2. **Prefer reusing existing patterns**: if the project already has a standard migration style, config-loading approach, or test framework, follow it instead of inventing a new one
3. **Ask when unsure**: if you cannot find a precedent, confirm the approach with the reviewer before implementing it

## Examples

Good: before adding a database column, review the last PR that added one and notice that migration logic is consistently placed in a `migrate()` function that test scripts call automatically. Append the new migration to the end of the same function.

Bad: create a separate migration script without checking history first, which forces tests to run an extra manual step and adds another deployment step, only to be deleted and redone later.
