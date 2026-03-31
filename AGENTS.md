# Agent Knowledge Repo

Before starting any task, every agent must read this file, `base/AGENTS.md`, and the relevant role `AGENTS.md` files.

## Repository Structure

```text
agent-knowledge-framework/
├── AGENTS.md                  # root entrypoint
├── base/                      # shared knowledge across roles
│   ├── AGENTS.md              # shared entrypoint
│   ├── skills/                # shared executable workflows
│   └── notes/                 # shared principles / insights / experiences
├── roles/                     # role-specific knowledge
│   ├── document-reviewer/
│   ├── generalist-engineer/
│   ├── mechanism-analyst/
│   ├── performance-infra-tester/
│   └── <role>/
│       ├── AGENTS.md          # role description + index
│       ├── skills/            # role-specific workflows
│       ├── notes/             # role-specific principles / insights / experiences
│       └── questions.md       # known unknowns
└── tools/                     # validation and maintenance scripts
```

## Knowledge Loading and Sedimentation

- Persistent context: `AGENTS.md` (this file), `base/AGENTS.md`, and the relevant role `AGENTS.md` files
- Layered loading: entrypoints first, then one relevant `skill` or `note`, then one more only if needed
- Direct access for symptoms or high-risk work: when a task has a concrete failure mode or higher operational risk, go directly to the most relevant shared or role-specific `note`
- After context compression: if you are no longer sure about the active roles or loading order, re-read this file, `base/AGENTS.md`, and the relevant role `AGENTS.md`

Detailed loading strategy (persistent vs on-demand context, layered escalation, and compression recovery) is documented in `base/notes/knowledge-loading.md`.

When the user explicitly asks to preserve reusable knowledge, or explicitly triggers `/eat`, use `base/skills/eat/` to perform sedimentation.

## Collaboration

- Any write must happen in a worktree
- Do not develop in the main workspace

See `base/notes/git-worktree.md` for the detailed workflow and guardrails.
