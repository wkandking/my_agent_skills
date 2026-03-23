---
name: skill-creator-codex
description: Use when creating a new Codex skill, adapting a Claude or Anthropic skill to Codex, validating a skill folder, or installing a finished skill into the local Codex skills directory.
---

# Skill Creator for Codex

Create or adapt skills for Codex without assuming Claude-specific tooling.

## Overview

Use this skill to:

- create a new skill folder with a valid `SKILL.md`
- adapt an Anthropic or Claude skill for Codex
- validate frontmatter and folder layout
- install a completed skill into Codex's local skills directory

Read [references/codex-usage.md](references/codex-usage.md) when you need
installation or verification details.

## When to Use

- the user wants a new Codex skill
- an existing Claude skill needs to be ported to Codex
- a skill folder exists but needs cleanup, validation, or installation
- the user asks why a skill is not being discovered by Codex

Do not use this skill for one-off prompts that do not need to become reusable.

## Workflow

1. Capture the job the skill should do.
2. Define trigger conditions for the `description` field.
3. Draft or update the skill folder.
4. Validate the folder with `scripts/quick_validate.py`.
5. Test the workflow in Codex with a baseline and a with-skill run.
6. Install the skill into Codex if the user wants automatic discovery.

## Capture Intent

Collect the minimum information needed before writing:

1. What task should the skill make easier or more reliable?
2. When should Codex load it?
3. What output shape does the user expect?
4. Does this skill need scripts or references, or is `SKILL.md` enough?

## Writing Rules

Keep the skill concise:

- put trigger conditions in frontmatter `description`
- keep procedural guidance in `SKILL.md`
- move long documentation to `references/`
- move deterministic helpers to `scripts/`

Prefer this shape:

```text
skill-name/
├── SKILL.md
├── references/
└── scripts/
```

## Validation

Run:

```bash
python3 scripts/quick_validate.py <path-to-skill>
```

This checks:

- `SKILL.md` exists
- frontmatter is valid YAML
- `name` and `description` are present
- naming and length constraints are respected

## Testing in Codex

Codex does not use the Claude-specific `claude -p` evaluation loop from the
original Anthropic skill. Use manual pressure tests instead:

1. Write 2-3 realistic prompts that should trigger the skill.
2. Run a baseline: solve the task without explicitly reading the skill.
3. Run a with-skill pass: ask Codex to read the skill file first, or install
   it into Codex and restart the app.
4. Compare correctness, completeness, and consistency.

When testing a newly installed skill, restart Codex before expecting automatic
discovery. In the current session, the reliable path is to point Codex at the
skill file explicitly.

## Installation

Install a finished skill into Codex with:

```bash
python3 scripts/install_to_codex.py <path-to-skill>
```

Optional flags:

- `--dest <path>` to override the target skills directory
- `--force` to replace an existing installed copy

Default install target:

- `$CODEX_HOME/skills`
- or `~/.codex/skills` if `CODEX_HOME` is unset

## Unsupported Claude-Only Automation

These files are kept for reference from the upstream Anthropic skill, but they
are not part of the Codex-native path:

- `scripts/run_eval.py`
- `scripts/run_loop.py`
- `scripts/improve_description.py`

They depend on the `claude` CLI and will exit with a clear message when that
tool is unavailable.

## Quick Reference

Validate:

```bash
python3 scripts/quick_validate.py /path/to/skill
```

Install:

```bash
python3 scripts/install_to_codex.py /path/to/skill --force
```

Package for external sharing if needed:

```bash
python3 -m scripts.package_skill /path/to/skill /tmp/dist
```
