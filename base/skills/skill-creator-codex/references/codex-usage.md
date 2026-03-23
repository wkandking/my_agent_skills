# Codex Usage

## What works in Codex

- writing and updating `SKILL.md`
- validating a skill folder with `python3 scripts/quick_validate.py`
- copying a skill into Codex's local skills directory
- manual before/after testing with realistic prompts

## What does not translate directly from Claude

- `claude -p` based trigger evaluation
- automated description-optimization loops built around Claude CLI nesting
- Claude.ai specific packaging and browser assumptions

## Recommended verification loop

1. Pick 2-3 realistic user prompts.
2. Run a baseline without explicitly reading the skill.
3. Run a second pass after asking Codex to read `SKILL.md`.
4. Tighten the description if the skill should have applied but did not.
5. Tighten the body if Codex loaded the skill but still executed poorly.

## Installation notes

Install into:

- `$CODEX_HOME/skills`
- or `~/.codex/skills`

Then restart Codex so the new skill inventory is reloaded.

Within the current live session, newly installed skills may not appear
automatically. If you need immediate use, reference the skill path directly.
