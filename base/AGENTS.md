# base

## Skills

| skill_name | description | trigger |
| --- | --- | --- |
| `eat` | Sediment current context into reusable knowledge, and decide whether it should become an AGENTS rule, note, skill, or question. | preserving reusable knowledge; `/eat`; post-task sedimentation |
| `skill-creator-codex` | Create, adapt, validate, and install Codex skills. | creating a new skill; adapting Claude/Anthropic skills; validating or installing a skill |

## Notes

| note_name | description | trigger |
| --- | --- | --- |
| `check-conventions-first.md` | Check existing project conventions before adding new behavior to avoid style drift and rework. | new feature; naming conventions; migration scripts; CLI style |
| `credential-safety.md` | Never commit, hardcode, or print credentials. | credentials; passwords; tokens; API keys |
| `explicit-tmpdir-for-long-jobs.md` | Long-running or highly parallel jobs must use an explicit temporary directory instead of default `/tmp`. | TMPDIR; tempfile; `/tmp`; OOM kill; exit code 137 |
| `git-worktree.md` | Use isolated git worktrees for multi-agent collaboration and all write operations. | worktree; multi-agent work; branch isolation |
| `knowledge-loading.md` | Define the default entrypoint loading order, resident context, and when to expand further on demand. | knowledge loading; persistent context; context compression; when to read base |
| `knowledge-sedimentation.md` | Decide when knowledge should be sedimented and choose the smallest stable target. | sedimentation; when to write a note; note kind; question vs note |
| `persistent-task-state-must-be-externalized.md` | Externalize any task state that must survive across sessions, agents, or handoffs. | cross-session work; handoff; long-running task; task log |
| `visible-workflow-state-over-hidden-agent-features.md` | Prefer files, CLI, and logs over hidden agent state for workflow control and environment knowledge. | MCP; TODO/PLAN files; sub-agents; tmux; observability |
