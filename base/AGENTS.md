# base

## Skills

| skill_name | description | trigger |
| --- | --- | --- |
| `skills/eat/` | Sediment current context into reusable knowledge, and decide whether it should become an AGENTS rule, note, skill, or question. | preserving reusable knowledge; `/eat`; post-task sedimentation |
| `skills/skill-creator-codex/` | Create, adapt, validate, and install Codex skills. | creating a new skill; adapting Claude/Anthropic skills; validating or installing a skill |

## Notes

| note_name | description | trigger |
| --- | --- | --- |
| `notes/check-conventions-first.md` | Check existing project conventions before adding new behavior to avoid style drift and rework. | new feature; naming conventions; migration scripts; CLI style |
| `notes/credential-safety.md` | Never commit, hardcode, or print credentials. | credentials; passwords; tokens; API keys |
| `notes/git-worktree.md` | Use isolated git worktrees for multi-agent collaboration and all write operations. | worktree; multi-agent work; branch isolation |
| `notes/knowledge-loading.md` | Define the default entrypoint loading order, resident context, and when to expand further on demand. | knowledge loading; persistent context; context compression; when to read base |
| `notes/knowledge-sedimentation.md` | Decide when knowledge should be sedimented and choose the smallest stable target. | sedimentation; when to write a note; note kind; question vs note |
| `notes/persistent-task-state-must-be-externalized.md` | Externalize any task state that must survive across sessions, agents, or handoffs. | cross-session work; handoff; long-running task; task log |
