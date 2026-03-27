---
kind: principle
description: "Use layered loading by default, escalate only when needed, and proactively consider sedimentation after important work."
triggers:
  - "knowledge loading"
  - "layered loading"
  - "context compression"
  - "sedimentation"
  - "when to read base"
---

# Loading and Sedimentation

This repository uses layered loading to keep context small while preserving access to shared and role-specific knowledge.

## Default Loading Path

1. Read the root `AGENTS.md`
2. Read the relevant role `AGENTS.md`
3. If the task touches shared concerns, read `base/AGENTS.md`
4. Read one relevant `skill` or `note`
5. Read one more `note` or `questions.md` only if the task still needs more context

## Persistent Context

The default persistent context is:

- root `AGENTS.md`
- the relevant role `AGENTS.md`

Add `base/AGENTS.md` when the task touches shared concerns such as:

- write operations and worktree workflow
- credentials or secrets
- long-running or cross-session task state
- knowledge sedimentation
- skill creation
- shared repository workflow rules

## When to Escalate

Read beyond the minimum set when:

- the task has a concrete failure mode or symptom
- the task has unusually high operational risk
- the first `skill` or `note` is not enough to justify the next action
- you need a known unknown from `questions.md`

Do not bulk-load multiple notes by default.

## After Context Compression

If you are no longer sure about:

- which roles are active
- whether the task should use the shared layer
- what the loading order is

re-read:

1. root `AGENTS.md`
2. the relevant role `AGENTS.md`
3. `base/AGENTS.md` when shared concerns apply

## Sedimentation Trigger

After important work, proactively consider sedimentation when the task exposed:

- a reusable rule or guardrail
- a stable decision pattern
- a historical lesson worth preserving
- a known unknown that should move into `questions.md`

Use `eat` when the task is to convert source material into reusable knowledge.
