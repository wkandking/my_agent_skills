# Eat Skill Design

## Summary

`eat` is a shared skill for turning live task context and selected external sources into reusable repository knowledge. It supports a two-phase workflow: first extract candidate knowledge from the current conversation, attached source set, or explicit source path, classify each item by scope and type, recommend the correct destination, and draft markdown; then, after one explicit user confirmation, apply the approved changes to a target knowledge-root directory. It also supports proposal-first self-maintenance through `/eat update` and `/eat update all`.

## Goals

- Capture reusable knowledge before it is lost in task history.
- Distinguish shared guidance from role-specific guidance.
- Keep one-off incidents out of durable rule files.
- Support a short invocation convention: `/eat` and `/eat <folder>`.
- Support ingesting explicit or implicit sources such as files, repositories, images, PDFs, URLs, and pasted text.
- Support controlled self-maintenance through `/eat update` and `/eat update all`.
- Let the user review all proposed write operations before any file changes occur.

## Non-Goals

- Do not preserve every observation; reject narrow, unstable, or one-off notes when they are not worth storing.
- Do not write anything before explicit confirmation.
- Do not force every note into durable storage when `Do Not Store` is the correct result.

## Trigger Conditions

The skill should trigger when the user asks to summarize current context into durable knowledge, asks where new knowledge belongs, wants reusable lessons extracted from a task, wants draft text for `AGENTS.md`, `principles`, `insights`, `experience`, or role-specific knowledge files, wants to summarize a document, repository, image, PDF, URL, or other source into knowledge, uses the `/eat` or `/eat <folder>` shorthand, or asks `eat` to reflect on and fix its own mistakes.

## Invocation Model

- `/eat` means use the current project root as the target knowledge-root directory.
- `/eat <folder>` means:
  - if `<folder>` is exactly `home`, use `$HOME/my_agent_skills`
  - use `<folder>` directly when it is an absolute path
  - resolve `<folder>` under `$HOME` when it is only a folder name or a relative path
- `/eat <target> <source>` may be used when the user gives an explicit source path, URL, or other source descriptor after the target.
- `/eat update` means reflect only on the current conversation and propose a minimal repair to `eat`.
- `/eat update all` means review the current conversation plus existing `eat` maintenance assets and propose evidence-backed, minimal maintenance updates.
- If the user also names a different explicit target root in normal language, the explicit target wins over the shorthand default.
- The target root is a knowledge-root directory, not an arbitrary feature folder. `eat` should look for or create `AGENTS.md`, `principles/`, `insights/`, `experience/`, and `skills/` under that root after confirmation.
- The current project root is only the default when the folder argument is omitted entirely.
- For maintenance modes, `eat` must not modify itself until the user explicitly approves the proposal.

## Source Selection Model

For normal ingestion modes, choose the source set in this order:

1. Explicit source named by the user in the current message.
2. The most recent attachment group in the current conversation.
3. The current conversation context.

The most recent attachment group should be treated as a set. `eat` should summarize each source separately first, then produce a merged conclusion across the group.

Supported source types include:

- single files
- directories and code repositories
- attached images
- local image paths
- PDFs and attached documents
- URLs
- pasted text in the current conversation

If the recent group contains mixed source types, `eat` should process all sources it can read reliably and mark the rest as skipped with a reason.

## Classification Model

Each candidate knowledge item should be classified along two axes:

1. Scope
   - Shared across agents and roles
   - Specific to one role or a small set of roles

2. Knowledge type
   - Entry-point operating rule for `AGENTS.md`
   - Durable principle
   - Generalized insight
   - Concrete incident or decision record
   - Reusable workflow, which may indicate a new or updated skill

## Placement Rules

- Put short, high-signal operating rules in `<root>/AGENTS.md` or `<root>/roles/<role>/AGENTS.md`.
- Put stable rules with broader reasoning value in `<root>/principles/`.
- Put repeated patterns and heuristics in `<root>/insights/`.
- Put incidents, postmortems, and one-time decisions in `<root>/experience/`.
- Put repeatable workflows with steps and trigger conditions in `<root>/skills/`.

## Proposal Contract

Before confirmation, for each retained candidate, `eat` should output:

- `Candidate`
- `Scope`
- `Knowledge Type`
- `Recommended Path`
- `Why Here`
- `Draft`

If a candidate should not be stored, the skill should say so explicitly and explain why.

After listing candidates, `eat` should also output:

- per-source extraction results
- a merged conclusion across all processed sources
- target root
- files to create
- files to update
- a clear note that no files will be changed until the user confirms
- all draft content in Chinese

## Apply Contract

After confirmation, `eat` should:

- inspect each target file before editing
- create the minimal target-root structure if missing
- avoid duplicate insertions
- write the approved content only
- write all new content in Chinese unless the user explicitly requests another language
- report the files changed

For maintenance modes, after confirmation, `eat` should:

- update only the approved `eat` files
- keep the change set minimal and evidence-based
- reinstall the updated skill into the user Codex skills directory
- report both source-file changes and reinstall completion

## Initialization Rules

When the confirmed target root is missing the expected structure, `eat` should initialize:

- `<root>/AGENTS.md`
- `<root>/principles/`
- `<root>/insights/`
- `<root>/experience/`
- `<root>/skills/`

Role-specific directories should only be created when the approved candidates actually require a role path.

## Example

For a rule such as "when the network is broken, use the proxy on port 7741", the likely result is:

- Scope: shared
- Knowledge type: entry-point operating rule
- Recommended path: `<root>/AGENTS.md`
- Draft: a short rule the user can paste into or approve for the target root

## Validation

The implementation remains documentation-first, but the documented behavior now covers both proposal and apply phases:

- `base/skills/eat/SKILL.md`
- `base/skills/eat/references/knowledge-placement.md`
- `base/AGENTS.md` inventory text

Validation should include markdown inspection, `quick_validate.py` against the skill folder, and content checks for the `/eat` invocation and confirmation workflow.
