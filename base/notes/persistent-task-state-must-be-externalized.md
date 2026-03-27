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
  - "TODO.md"
  - "PLAN.md"
  - "sub-agent"
  - "MCP"
---

# Persistent Task State Must Be Externalized

## Rule

If task state must survive beyond the current turn, it must be externalized into inspectable artifacts.

State that exists only inside the current session is fragile. It breaks when:

- the session is interrupted
- context is compressed
- another agent or a human needs to take over
- a long-running command keeps running after the current turn ends

If others cannot inspect the current state from the repository, logs, or task artifacts, the task is not truly handoff-safe.

## Acceptable External State

- Repository state: branches, commits, and worktrees
- Task records: `PLAN.md`, `TODO.md`, implementation notes, and PR descriptions
- Long-task records: launch command, important parameters, log location, output location, and how progress is verified
- Stable knowledge artifacts: `AGENTS.md`, `notes/`, `skills/`, and `questions.md`

## What Not To Rely On

Do not treat the following as the only source of truth:

- temporary mental state inside the current session
- tool-local hidden state
- implicit progress that only the current agent knows
- harness-internal state that cannot be directly inspected or exported

plan mode, MCP, sub-agents, and background shells may help execution, but they cannot carry the only persistent task state.

## Practical Requirements

### For multi-step work

At minimum, write down:

- the current goal
- the current stage
- what is done
- what remains
- what still looks risky

Short-term breakdowns should go into `TODO.md`; multi-step implementation plans should go into `PLAN.md`, the PR description, or an equivalent document.

### For long-running or background work

You must externalize:

- the launch command
- important parameters and environment assumptions
- the log location
- the output location
- how to verify current progress

For background execution, prefer `tmux`, schedulers, or other standard runtimes rather than relying only on the current harness session.

### Handoff Check

Assume the next person taking over cannot see your current session and can only see:

- the repository
- branches and commits
- docs and notes
- logs and task artifacts

If that is still not enough, the task state is still under-externalized.

## Especially Relevant For

- long-running tasks
- background services or watchers
- cross-session implementation plans
- multi-agent handoff
- any task where losing state would force expensive rediscovery
