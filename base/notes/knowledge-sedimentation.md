---
kind: principle
description: "After important work, proactively consider sedimentation and choose the smallest stable target: AGENTS rule, note, skill, or question."
triggers:
  - "sedimentation"
  - "knowledge sedimentation"
  - "when to write a note"
  - "note kind"
  - "question vs note"
---

# Knowledge Sedimentation

Use `eat` when the user explicitly asks to preserve reusable knowledge, or explicitly triggers `/eat`.

Prefer user-triggered sedimentation over automatic post-task sedimentation. This keeps sedimentation deliberate and avoids filling the repository with low-signal summaries.

## Smallest Useful Targets

Choose the smallest target that preserves the value:

- `AGENTS.md` rule
  - short, high-frequency entry rules
  - repository layout hints
  - loading reminders needed at the start of work

- `note`
  - `kind: principle` for hard constraints and stable boundaries
  - `kind: insight` for reusable decision patterns and heuristics
  - `kind: experience` for concrete historical cases and evidence

- `skill`
  - multi-step workflows
  - repeatable runbooks
  - tasks with a stable input/output shape

- `questions.md`
  - known unknowns
  - things worth preserving before they are stable enough to become notes

## Placement

- shared knowledge goes under `base/`
- role-specific knowledge goes under `roles/<role>/`

Ask:

- would this help multiple roles?
- does it depend on a role-specific responsibility or interpretation standard?

If multiple roles would benefit, prefer `base/`.

## Extraction Flow

1. keep the concrete event or evidence in view
2. decide whether the reusable part is a rule, a heuristic, a historical case, a workflow, or an open question
3. store it in the smallest stable target
4. avoid creating multiple artifacts that repeat the same content

## Anti-Patterns

- writing a long historical summary when only one short rule is reusable
- turning a single anecdote into a universal principle too early
- storing a workflow as a note instead of a skill
- using `questions.md` as a generic TODO list
