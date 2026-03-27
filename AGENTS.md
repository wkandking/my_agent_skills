# Agent Knowledge Repo

Before starting any task, every agent must read this file and the relevant role `AGENTS.md` files.

## Repository Structure

```text
agent-knowledge-framework/
├── AGENTS.md                  # root entrypoint
├── base/                      # shared knowledge across roles
│   ├── AGENTS.md              # shared entrypoint
│   ├── skills/                # shared executable workflows
│   └── notes/                 # shared principles / insights / experiences
├── roles/                     # role-specific knowledge
│   ├── generalist-engineer/
│   ├── mechanism-analyst/
│   ├── performance-infra-tester/
│   └── <role>/
│       ├── AGENTS.md          # role description + index
│       ├── skills/            # role-specific workflows
│       ├── notes/             # role-specific principles / insights / experiences
│       └── questions.md       # known unknowns
├── tools/                     # validation and maintenance scripts
└── archive/                   # inactive or historical knowledge
```

## Active Roles

- `generalist-engineer`
- `mechanism-analyst`
- `performance-infra-tester`

## Shared Layer

`base/AGENTS.md` is the shared entrypoint for cross-role knowledge.

## Load Rule

1. Read this file
2. Read the relevant role `AGENTS.md`
3. If the task touches shared concerns, read `base/AGENTS.md`
4. Read one relevant shared or role-specific `skill` or `note`
5. Read `questions.md` or one extra `note` only if needed

## Knowledge Loading and Sedimentation

- Persistent context: this file plus the relevant role `AGENTS.md` files
- Layered loading: entrypoints first, then one relevant `skill` or `note`, then one more only if needed
- Direct access for symptoms or high-risk work: when a task has a concrete failure mode or higher operational risk, go directly to the most relevant shared or role-specific `note`
- After context compression: if you are no longer sure about the active roles, shared layer, or loading order, re-read this file, the relevant role `AGENTS.md`, and `base/AGENTS.md` when shared concerns apply
- After important work: proactively consider sedimentation when a task exposed a reusable rule, decision pattern, or historical lesson worth keeping

## Knowledge Model

- `skills/`: executable workflows
- `notes/`: rules, decision heuristics, and historical cases
- `questions.md`: known unknowns

## Collaboration

- Any write must happen in a worktree
- Do not develop in the main workspace
- Important changes go through PR review
