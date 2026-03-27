---
kind: principle
description: "Detailed knowledge-loading strategy: layered loading, resident vs on-demand criteria, trigger-based priority loading, and reload behavior after context compression."
triggers:
  - "knowledge loading"
  - "layered loading"
  - "resident context"
  - "on-demand loading"
  - "context compression"
  - "compaction"
---

# Knowledge Loading

Role-specific and shared knowledge will keep growing, so not everything should be loaded into context.
The default strategy is "load entrypoints first, then expand bodies on demand": read the root / base / role entrypoints to determine scope, then open only the `skill` or `note` bodies the current task actually needs.

## Default Loading Path

The default order is:

1. Read the root `AGENTS.md`
2. Read the shared-layer `base/AGENTS.md`
3. Read the relevant role `roles/<role>/AGENTS.md`

### Recommended Resident Context

These files should, in principle, be loaded for every task:

- Root `AGENTS.md`: collaboration rules, repository structure, and the global entrypoint
- Shared-layer `base/AGENTS.md`: the shared skills / notes index
- `roles/<role>/AGENTS.md`: role responsibilities and the role-layer knowledge index

### Default On-Demand Loading

The following are loaded on demand by default:

- `skill`: read after it is matched via indexes, summaries, or `triggers` in `AGENTS.md`
- `note`: read on demand by default; prefer `kind: principle` when you need stronger rules, and `kind: insight` when you need decision framing or heuristics
- More specific `note`: escalate further when you need evidence, boundary conditions, counterexamples, or decision context; if the repo contains `kind: experience`, that layer is usually read here

### Not Recommended As Resident Context

These usually should not remain resident:

- Long background material
- Full troubleshooting journals
- Historical logs and one-off evidence
- Fast-expiring fact snapshots, such as environment paths, versions, or cluster state

These are better stored in more specific `note`s, runbooks, READMEs, or other inspectable artifacts that can be dated and verified.

## When To Escalate

Read beyond the minimum set when any of the following is true:

- The task already has a concrete failure mode or symptom
- The task has unusually high operational risk
- The already-loaded `skill` or `note` is still not enough to justify the next action
- You need a known unknown from `roles/<role>/questions.md`

Do not bulk-load multiple notes by default. Prefer gradual escalation over pulling the whole knowledge base into context.

## Reload After Context Compression

In long sessions, context may be compressed. After compression, entrypoints and indexes may be reduced to summaries, and important details may be lost.

If you are no longer sure about the following:

- Which roles are currently active
- What the correct loading order is
- Whether a shared rule lives in an entrypoint or in a body note

then context has likely been compressed. Re-read:

1. The root `AGENTS.md`
2. The shared-layer `base/AGENTS.md`
3. The relevant role `roles/<role>/AGENTS.md`
