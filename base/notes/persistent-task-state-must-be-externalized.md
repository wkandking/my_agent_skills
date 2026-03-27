---
kind: principle
description: "Any task state that must survive across sessions, agents, or handoffs must be externalized into files, branches, logs, or other inspectable artifacts."
triggers:
  - "persistent task state"
  - "cross-session"
  - "handoff"
  - "long-running task"
  - "task log"
  - "observability"
source:
  - "base/principles/persistent-task-state-must-be-externalized.md"
  - "base/insights/visible-workflow-state-over-hidden-agent-features.md"
---

# Persistent Task State Must Be Externalized

## Why This Exists

State that only exists inside the current agent session is fragile.

It breaks as soon as:

- the session is interrupted
- context is compressed
- another agent or a human needs to continue the work
- a long-running command keeps running after the current turn ends

If nobody can inspect the current state from the repository, logs, or task artifacts, then the task is not truly handoff-safe.

## Rule

If task state must survive beyond the current turn, it must be externalized into inspectable artifacts.

Acceptable external state includes:

- repository state such as branches, commits, and worktrees
- written task records such as plan documents, implementation notes, or PR descriptions
- logs, output paths, and runtime parameters for long-running jobs
- stable knowledge artifacts such as `AGENTS.md`, `notes/`, `skills/`, or `questions.md`

## What Not To Rely On

Do not rely on any hidden or session-local state as the only source of truth, including:

- temporary mental state inside the current session
- tool-local hidden state
- implicit progress that is only obvious to the current agent

Those mechanisms may help execution, but they are not sufficient as the only persistent task record.

## Guidance

### For multi-step work

Write down enough state that a new agent can continue without reconstructing the whole task from memory.

Examples:

- current goal
- current stage
- what is done
- what remains
- what still looks risky

### For long-running or background work

Externalize:

- launch command
- important flags and environment assumptions
- log location
- output location
- how to verify current progress

### For handoffs

Assume the next agent cannot see your current session and only has:

- the repository
- branches and commits
- docs and notes
- logs and task artifacts

If that is not enough, then the task state is still under-externalized.

## Escalate

This note is especially relevant when the task involves:

- long-running jobs
- background services or watchers
- cross-session implementation plans
- multi-agent handoff
- any task where losing the current state would force expensive re-discovery

## Related Notes

- `base/notes/git-worktree.md`
- `base/notes/explicit-tmpdir-for-long-jobs.md`
