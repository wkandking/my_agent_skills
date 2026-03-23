# Knowledge Placement Guide

Use this guide when deciding where extracted knowledge belongs.

All destination paths should be resolved under the chosen knowledge-root directory.

## Target Root Resolution

Resolve the target root like this:

1. If the user uses `/eat` with no argument, use the current project root.
2. If the user uses `/eat project`, use the current project root.
3. If the user uses `/eat home`, resolve it to `$HOME/my_agent_skills`.
4. In `home` mode, `$HOME/my_agent_skills` is a container root:
   - shared knowledge should normally go under `base/`
   - role-specific knowledge should go under `roles/<role>/`
5. `eat` does not accept arbitrary path arguments or ordinary folder names as target roots.
6. Only `project` and `home` are valid explicit target aliases.

Examples:

- `/eat` -> current project root
- `/eat project` -> current project root
- `/eat home` -> `$HOME/my_agent_skills`

## Source Ingestion Rules

Choose sources in this order:

1. explicit source named by the user
2. the most recent attachment group
3. the current conversation

Supported source types:

- files
- directories and repositories
- attached images
- local image paths
- PDFs and documents
- URLs
- pasted text

For the most recent attachment group:

- treat the group as a set rather than a single last attachment
- summarize each source separately
- then produce one merged conclusion

For mixed groups:

- process the readable source types
- skip unsupported or unreadable sources with a brief reason
- do not drop the whole group because one source failed

## First Decision: Shared Or Role-Specific

Choose shared knowledge when the rule, pattern, or workflow can help many agents regardless of role.

Choose role-specific knowledge when it depends on:

- a role's scope or ownership
- tools mainly used by one role
- domain-specific interpretation rules
- reporting or evidence standards unique to one role

If the item is useful only inside one role, prefer `<root>/roles/<role>/...` over shared root-level files.

## Destination Guide

### `AGENTS.md`

Use `AGENTS.md` for entry-point guidance that an agent should see early:

- repository layout rules
- loading rules
- short operating notes
- common environment workarounds
- rules about where to store knowledge

Good fit:

- "If network access fails, retry through the proxy on port `7741`."
- "Load shared guidance before role-specific knowledge."

Bad fit:

- long rationale-heavy essays
- one-time incidents
- full workflows with many steps

### `principles/`

Use `principles/` for durable rules that should remain true across many tasks:

- decision rules
- interpretation rules
- strong behavioral constraints
- evidence standards

Good fit:

- "Prefer shared knowledge unless the task is clearly role-specific."
- "Do not treat environment drift as proof of a product defect."

Bad fit:

- temporary operational tips
- historical narratives

### `insights/`

Use `insights/` for generalized patterns learned from repeated work:

- heuristics
- common failure modes
- tradeoff patterns
- signals that often predict a class of problem

Good fit:

- "When a user correction changes scope twice, capture the stable constraint separately before continuing."
- "Repeated benchmark variance often points to environment noise before application regressions."

Bad fit:

- single incidents with no broader pattern
- rules that should be phrased as hard constraints

### `experience/`

Use `experience/` for concrete history:

- incidents
- postmortems
- one-time decisions
- retrospectives

Good fit:

- "Proxy port `7741` was required during the March 2026 outage because direct network access was blocked."
- "A previous plan overfit to one role and had to be split into shared and role-specific guidance."

Bad fit:

- generic advice without a specific incident
- workflows intended for reuse

### `skills/`

Use `skills/` for repeatable workflows that future agents should follow:

- multi-step procedures
- review checklists
- operating playbooks
- tasks where output shape should be standardized

Good fit:

- "Summarize context into reusable knowledge and recommend where it should live."
- "Validate a skill folder and install it into Codex."

Bad fit:

- single standalone rules
- facts without a procedure

## Shared Vs Role-Specific Path Examples

- Shared operating rule: `<root>/AGENTS.md`
- Shared principle: `<root>/principles/<topic>.md`
- Shared insight: `<root>/insights/<topic>.md`
- Shared incident record: `<root>/experience/<topic>.md`
- Shared workflow: `<root>/skills/<skill-name>/SKILL.md`

- Role operating rule: `<root>/roles/<role>/AGENTS.md`
- Role principle: `<root>/roles/<role>/principles/<topic>.md`
- Role insight: `<root>/roles/<role>/insights/<topic>.md`
- Role incident record: `<root>/roles/<role>/experience/<topic>.md`
- Role workflow: `<root>/roles/<role>/skills/<skill-name>/SKILL.md`

## Home Mode Mapping

When the target root is `$HOME/my_agent_skills`, do not write shared knowledge directly under the container root when `base/` and `roles/` exist.

Use this mapping:

- Shared operating rule: `<root>/base/AGENTS.md`
- Shared principle: `<root>/base/principles/<topic>.md`
- Shared insight: `<root>/base/insights/<topic>.md`
- Shared incident record: `<root>/base/experience/<topic>.md`
- Shared workflow: `<root>/base/skills/<skill-name>/SKILL.md`

- Role operating rule: `<root>/roles/<role>/AGENTS.md`
- Role principle: `<root>/roles/<role>/principles/<topic>.md`
- Role insight: `<root>/roles/<role>/insights/<topic>.md`
- Role incident record: `<root>/roles/<role>/experience/<topic>.md`
- Role workflow: `<root>/roles/<role>/skills/<skill-name>/SKILL.md`

For `home` mode, the proposal should inspect the existing role list under `<root>/roles/` and explicitly explain why an item goes to `base` or to a specific role.

## Root Initialization

If the target knowledge root is missing expected structure and the user has confirmed the write, initialize only what is needed:

- `<root>/AGENTS.md`
- `<root>/principles/`
- `<root>/insights/`
- `<root>/experience/`
- `<root>/skills/`

Do not create role-specific directories unless approved content actually targets them.

When creating a new root-level `AGENTS.md`, seed it with a minimal index:

```md
# 知识索引

## 目录

- `principles/`: 持久规则
- `insights/`: 重复出现的模式与启发
- `experience/`: 具体事件与决策
- `skills/`: 可复用工作流
```

Keep the initial file minimal. The point is to make later writes coherent, not to invent a full framework.

## Drafting Guidance

When you recommend a destination:

1. Give the narrowest path that matches the current repository layout.
2. Prefer existing entry-point files when the rule is short and high frequency.
3. If the best destination file does not exist yet, propose a file path rather than forcing the content into the wrong file.
4. Explain why the destination matches better than the nearby alternatives.

## Write Rules

When applying approved drafts:

1. Read the destination file first if it exists.
2. Append or merge surgically instead of replacing whole files.
3. Reuse the file's local tone and heading style.
4. If multiple approved items belong in one new file, consolidate them when they clearly share a topic.
5. If a candidate would duplicate an existing rule, skip the write and report that it was already covered.
6. All newly drafted or appended content should be written in Chinese unless the user explicitly asks for another language.

## Eat Maintenance Rules

Use these rules when `eat` is updating itself.

1. `/eat update` may rely only on the current conversation unless the user explicitly adds more material to the context.
2. `/eat update all` may read current `eat` maintenance assets on disk in addition to the current conversation.
3. Both modes must produce a proposal before modifying any `eat` file.
4. Both modes require explicit user approval before changing `eat` source files.
5. When `eat` updates itself, treat the source skill under `$HOME/my_agent_skills` as the source of truth. Update source files first, then sync the installed copy under `$HOME/.codex/skills/`.
6. If approved, both modes should reinstall the updated skill into the user Codex skills directory after the source updates are complete.
7. Keep maintenance changes evidence-based and minimal. Avoid unsupported rewrites.
