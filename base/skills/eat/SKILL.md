---
name: eat
description: Use when the user wants to extract reusable knowledge from the current context or from documents, repositories, images, PDFs, URLs, or other provided sources, asks what should be kept from a task, asks where new knowledge belongs, wants draft text for shared or role-specific AGENTS, principles, insights, experience, or skills files, or uses /eat to capture and apply approved knowledge into a target root.
---

# Eat

## Overview

Use this skill to eat the current context and turn it into reusable knowledge. The job is not to preserve everything. The job is to keep what is likely to matter again, place it in the right layer, draft markdown the user can reuse immediately, and, after explicit confirmation, write the approved content into a target knowledge-root directory.

Read `references/knowledge-placement.md` before deciding where a knowledge item belongs.

## Invocation

Support these shorthand forms:

- `/eat`
- `/eat <folder>`
- `/eat <target> <source>`
- `/eat update`
- `/eat update all`

Interpret them like this:

- `/eat` means the target knowledge root is the current project root.
- `/eat <folder>` means:
  - if `<folder>` is exactly `home`, use `$HOME/my_agent_skills`
  - if `<folder>` is an absolute path, use it directly
  - if `<folder>` is only a folder name or a relative path, resolve it under `$HOME`
- `/eat <target> <source>` means use `<target>` as the knowledge root and `<source>` as an explicit source path, URL, or source descriptor.
- If the user gives a different explicit target root in the message, use that explicit root.

Examples:

- `/eat my_agent_skills` -> `$HOME/my_agent_skills`
- `/eat home` -> `$HOME/my_agent_skills`
- `/eat knowledge/base` -> `$HOME/knowledge/base`
- `/eat /tmp/kb` -> `/tmp/kb`

Interpret the maintenance forms like this:

- `/eat update` means reflect only on the current conversation and the most recent `eat` correction discussed in this context.
- `/eat update all` means review the current conversation plus the existing `eat` maintenance assets on disk.

The target root is a knowledge-root directory. It should contain or be allowed to create:

- `AGENTS.md`
- `principles/`
- `insights/`
- `experience/`
- `skills/`

Do not write anything during the first response. First produce the proposal, then wait for one explicit confirmation covering all retained items.
For `/eat update` and `/eat update all`, this same confirmation rule applies before modifying any `eat` files or reinstalling the skill.

## Source Selection

For normal ingestion modes, choose the source set in this order:

1. An explicit source named by the user in the current message.
2. The most recent attachment group in the current conversation.
3. The current conversation context.

Treat the most recent attachment group as a set. Summarize each source separately first, then produce one merged conclusion across the processed group.

Supported source types include:

- single files
- directories and code repositories
- attached images
- local image paths
- PDFs and attached documents
- URLs
- pasted text in the current conversation

When sources are mixed:

- process every source type you can read reliably
- mark unreadable or unsupported sources as skipped with a short reason
- do not fail the entire run only because one source in the group is unusable

## What Counts As Input

Look at the selected source set plus any current-conversation context that explains what was learned:

- user requirements and corrections
- troubleshooting steps and workarounds
- repeated constraints or operating rules
- decisions about what belongs in shared vs role-specific knowledge
- concrete incidents, postmortems, or reversals
- patterns that appeared more than once during the task
- extracted content from documents, repositories, images, PDFs, URLs, or pasted text

## Filter Before You Keep

Reject or mark `Do Not Store` when the item is:

- too specific to one temporary situation
- likely to expire soon
- only a restatement of the current task
- missing enough context to be reused safely
- already represented by an existing stable rule with no meaningful refinement

If an item is borderline, say so and explain the risk of storing it.

## Maintenance Modes

Use these modes when the user wants `eat` to improve itself.

### `/eat update`

Use only the current conversation as evidence. Do not proactively load existing `eat` maintenance assets unless the user explicitly includes them in the current context.

The goal is to capture:

- what `eat` got wrong in this conversation
- the corrected rule or behavior
- the smallest set of `eat` files that should change

### `/eat update all`

Use the current conversation plus the current `eat` maintenance assets on disk, such as:

- `base/skills/eat/SKILL.md`
- `base/skills/eat/references/knowledge-placement.md`
- `base/skills/eat/references/`
- `base/skills/eat/evals/`
- other directly related `eat` files

Make only evidence-backed, minimal changes. Do not rewrite large sections without a clear reason supported by the current conversation or existing maintenance assets.

For both maintenance modes:

- always produce a proposal first
- never modify `eat` before explicit user confirmation
- if approved, update the relevant source `eat` files under `$HOME/my_agent_skills` first, then reinstall the skill into the user Codex directory

## Classification Flow

For each candidate knowledge item:

1. Decide whether it is shared or role-specific.
2. Decide whether it is best represented as:
   - an entry-point operating rule in `AGENTS.md`
   - a durable rule in `principles/`
   - a repeated pattern in `insights/`
   - a concrete incident in `experience/`
   - a reusable workflow in `skills/`
3. Recommend the exact destination path.
4. Draft markdown the user can paste there directly.

When a workflow deserves a skill, say whether it should live under `<root>/skills/` or `<root>/roles/<role>/skills/`.

Resolve each recommended path under the chosen target root, not under the repository that contains this skill unless the user selected that repository as the target root.
Never resolve `/eat <folder>` relative to the current project root. The current project root is only the default when the user omits the folder argument entirely.

## Placement Rules

Use these rules consistently:

- Put short, high-frequency operating guidance in `<root>/AGENTS.md` or `<root>/roles/<role>/AGENTS.md`.
- Put stable rules that should survive many tasks in `<root>/principles/`.
- Put generalized patterns learned from repeated work in `<root>/insights/`.
- Put concrete incidents, exceptions, and decision records in `<root>/experience/`.
- Put repeatable multi-step workflows in `<root>/skills/`.

## Proposal Output Format

For normal ingestion modes, first describe the processed source set:

## Source Set
- Target Root: `<exact path>`
- Source Mode: <explicit source | recent attachment group | current conversation>
- Processed Sources:
  - `<source>`: <processed | skipped: reason>

Then, for each processed source, use this exact structure:

## Source Summary: <source label>
- Source Type: <file | repo | image | pdf | document | url | pasted text | conversation>
- Key Takeaway: <1-3 sentences in Chinese>

For each retained item under that source, use this exact structure:

### Candidate: <short statement>
- Scope: <shared | role-specific:<role>>
- Knowledge Type: <AGENTS rule | principle | insight | experience | skill>
- Recommended Path: `<exact repository path>`
- Why Here: <1-3 sentences>
- Draft:

```md
<paste-ready markdown>
```

If the item should not be stored, use this structure instead:

### Candidate: <short statement>
- Scope: <shared | role-specific:<role> | unclear>
- Decision: Do Not Store
- Reason: <why it is too narrow, unstable, redundant, or incomplete>

After all candidates, add this summary:

## Merged Conclusion
- Summary: <cross-source conclusion in Chinese>
- Cross-Source Notes:
  - <note>

## Apply Summary
- Target Root: `<exact path>`
- Files To Create:
  - `<path>`
- Files To Update:
  - `<path>`
- Confirmation Required: `No files will be changed until the user explicitly confirms the full write.`

If nothing should be stored, say so directly and do not ask for confirmation.

For `/eat update` and `/eat update all`, use this structure instead:

## Failure Summary
- Issue: <what `eat` got wrong>
- Evidence Scope: <current context only | current context + existing eat assets>

## Root Cause
- <1-3 sentences>

## Rule Changes
- <proposed rule change>

## Files To Update
- `<path>`

For maintenance proposals, list source skill files first. Do not list the installed copy under `/Users/wangkang/.codex/skills/eat` as the primary maintenance target.

## Patch Draft

```md
<succinct patch summary or paste-ready replacement text in Chinese>
```

## Reinstall Plan
- Source Skill Path: `/Users/wangkang/my_agent_skills/base/skills/eat`
- Installed Skill Path: `/Users/wangkang/.codex/skills/eat`
- Confirmation Required: `No eat files or installed copies will be changed until the user explicitly confirms the full update.`

## Apply Phase

Only enter apply mode after a single explicit user confirmation for the full proposal.

In apply mode:

1. Reuse the approved target root from the proposal unless the user changes it explicitly.
2. Inspect each destination file before editing it.
3. Create the minimal root structure if needed:
   - `<root>/AGENTS.md`
   - `<root>/principles/`
   - `<root>/insights/`
   - `<root>/experience/`
   - `<root>/skills/`
4. Create role-specific directories only when an approved item requires them.
5. Avoid duplicate insertions by searching for equivalent content before writing.
6. Preserve existing structure and tone instead of replacing full files.
7. Write all newly drafted or appended content in Chinese unless the user explicitly asks for another language.
8. If this is `/eat update` or `/eat update all`, first update the source skill files under `/Users/wangkang/my_agent_skills/base/skills/eat`, then reinstall the updated skill into `/Users/wangkang/.codex/skills/eat` after the source changes are complete.
9. Report the files created or updated after writing.

## Drafting Rules

- Write the draft in the tone already used by the target file.
- Always write the draft itself in Chinese.
- Prefer small, paste-ready text over long essays.
- If the destination file does not exist yet, recommend the most likely path and state that it is a proposed file.
- Do not invent incidents or repeated patterns that are not supported by the current context.
- Before confirmation, do not modify files.
- After confirmation, write only the approved items.
- When creating or updating files during apply mode, write the new content in Chinese.
- For maintenance modes, do not modify `eat` itself or reinstall it until the user has explicitly approved the proposal.

## Example

### Candidate: Network issues should use the proxy on port 7741
- Scope: shared
- Knowledge Type: AGENTS rule
- Recommended Path: `/path/to/knowledge-root/AGENTS.md`
- Why Here: This is a short operating rule that may help any agent recover from a common environment problem quickly.
- Draft:

```md
- If network access fails, retry through the proxy on port `7741` before assuming the remote service is unavailable.
```

## Apply Summary
- Target Root: `/path/to/knowledge-root`
- Files To Create:
  - `/path/to/knowledge-root/AGENTS.md`
- Files To Update:
  - None
- Confirmation Required: `No files will be changed until the user explicitly confirms the full write.`
