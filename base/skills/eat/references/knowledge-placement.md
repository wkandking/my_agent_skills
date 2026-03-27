# Knowledge Placement Guide

Use this guide when deciding where extracted knowledge should go.

All target paths must be resolved under the selected knowledge root.

## Target Root Resolution

Resolve the target root using these rules:

1. If the user runs `/eat` with no argument, the target root is the current project root
2. If the user runs `/eat project`, the target root is the current project root
3. If the user runs `/eat home`, the target root is `$HOME/my_agent_skills`
4. In `home` mode, `$HOME/my_agent_skills` is treated as the container root:
   - shared knowledge usually goes under `base/`
   - role-specific knowledge usually goes under `roles/<role>/`
5. `eat` does not accept arbitrary path arguments or plain directory names as target roots
6. Only `project` and `home` are valid explicit target aliases

Examples:

- `/eat` -> the current project root
- `/eat project` -> the current project root
- `/eat home` -> `$HOME/my_agent_skills`

## What This Reference Is Responsible For

This document only handles three things:

1. resolving the target root
2. mapping an already-chosen knowledge target to an exact path
3. constraining where confirmed writes should land

The following judgments are intentionally not redefined here:

- whether something is worth sedimenting
- whether it is shared or role-specific
- whether it should be an `AGENTS rule`, `note`, `skill`, `question`, or `Do Not Store`
- how to choose a `note kind`

Those decisions are governed by `base/notes/knowledge-sedimentation.md`.

## Path Templates

If the target root itself is a lightweight knowledge repo:

- shared entry rules: `<root>/AGENTS.md`
- shared note: `<root>/notes/<topic>.md`
- shared skill: `<root>/skills/<skill-name>/SKILL.md`
- shared questions: `<root>/questions.md`

- role entry rules: `<root>/roles/<role>/AGENTS.md`
- role note: `<root>/roles/<role>/notes/<topic>.md`
- role skill: `<root>/roles/<role>/skills/<skill-name>/SKILL.md`
- role questions: `<root>/roles/<role>/questions.md`

## `home` Mode Mapping

When the target root is `$HOME/my_agent_skills`, map paths to the current repository structure:

- shared entry rules: `<root>/base/AGENTS.md`
- shared note: `<root>/base/notes/<topic>.md`
- shared skill: `<root>/base/skills/<skill-name>/SKILL.md`

- role entry rules: `<root>/roles/<role>/AGENTS.md`
- role note: `<root>/roles/<role>/notes/<topic>.md`
- role skill: `<root>/roles/<role>/skills/<skill-name>/SKILL.md`
- role questions: `<root>/roles/<role>/questions.md`

In `home` mode, proposals should actively inspect the roles already present under `<root>/roles/`, and explicitly explain why content belongs in `base` or in a specific role directory.

## Root Initialization

If the target knowledge root is missing required structure and the user has confirmed writes, initialize only the pieces that are actually needed:

- `<root>/AGENTS.md`
- `<root>/notes/`
- `<root>/skills/`
- `<root>/questions.md`

If a role layer is needed, create these only as required:

- `<root>/roles/<role>/AGENTS.md`
- `<root>/roles/<role>/notes/`
- `<root>/roles/<role>/skills/`
- `<root>/roles/<role>/questions.md`

Do not create role directories in advance unless content actually lands there.

## Path Recommendation Rules

When recommending a target path:

1. Recommend the narrowest path that fits the current repo structure
2. Prefer existing entrypoint files for high-frequency short rules
3. If the best target file does not exist, recommend a new file path directly instead of forcing content into the wrong file
4. If the target is a `note`, include the `kind`
5. Explain why this target is better than nearby alternatives
