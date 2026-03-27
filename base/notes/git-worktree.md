---
kind: principle
description: "Rules for isolating working directories with git worktree during multi-agent parallel development."
triggers:
  - "worktree"
  - "multi-agent"
  - "parallel development"
  - "branch isolation"
  - "write code"
---

# Git Worktree Rules for Multi-Agent Collaboration

## Background

Multiple agents may read from and write to this repository at the same time. If they share one working directory, file conflicts, dirty state, and merge confusion become likely. Git worktree allows multiple isolated working directories to be created from the same repository, so each agent can work in its own worktree without interfering with others.

## Core Rules

1. **Quick read-only checks** may be done directly in the main worktree (`main` branch); but if exploration may turn into editing, start in an isolated worktree from the beginning
2. **All write operations** must happen in an isolated worktree and be merged through a PR
3. Each worktree must have its own branch, and the branch name must include an agent identifier

## Workflow

### Create a worktree

```bash
# Run from the repository root
git fetch origin
git worktree add .agents/worktrees/<topic> -b <agent>/<topic> origin/main

# Example
git worktree add .agents/worktrees/add-new-skill -b alice/add-new-skill origin/main
```

### Work inside the worktree

```bash
cd .agents/worktrees/add-new-skill
# Edit and commit normally
git add ...
git commit -m "..."
git push -u origin alice/add-new-skill
```

### Open a PR and clean up

```bash
# Create a PR after pushing
git push -u origin alice/add-new-skill
# Create PR -> review -> merge

# Clean up the worktree after merge
cd /path/to/main-worktree
git worktree remove .agents/worktrees/add-new-skill
git branch -d alice/add-new-skill
```

### Sync the latest changes from main

```bash
# Update main inside the worktree
git fetch origin
git rebase origin/main
```

## Branch Naming Convention

```
<agent-name>/<topic>
```

Examples:
- `alice/add-new-skill`
- `bob/update-docs`
- `charlie/promote-principle`

## Anti-Pattern: Moving Changes Across Branches with Stash

Do **not** use `git stash` + `git checkout` + `git stash pop` to move changes from one branch to another, especially when the two branches have different file layouts.

### Correct Approaches

**Method 1: worktree (recommended)**

Work in a worktree from the start for full isolation:

```bash
git worktree add .agents/worktrees/update-docs -b codex/update-docs origin/main
cd .agents/worktrees/update-docs
# Edit, commit, and push directly
# This avoids stash-related conflicts entirely
```

**Method 2: checkout only the exact file**

If you already stashed changes, do not `stash pop`; use `git checkout` to restore only the file you need:

```bash
git stash
git worktree add .agents/worktrees/update-docs -b codex/update-docs origin/main
cd .agents/worktrees/update-docs
git checkout stash -- path/to/file.md   # restore only one file
git stash drop
```

### Summary

| Situation | Recommended | Avoid |
|---|---|---|
| Split part of existing changes into a new branch | worktree or `git checkout stash -- <file>` | `git stash pop` (restore everything) |
| Two branches have different file layouts | worktree | cross-branch stash transfer |
| Only one file needs to be moved | `git show stash:path > file` or `git checkout stash -- path` | `stash pop` followed by manual cleanup |

## Notes

- The same branch cannot be checked out in multiple worktrees at the same time; git will reject it
- Submodules inside a worktree must be initialized separately: `git submodule update --init`
- Clean up worktrees after finishing to avoid leaving disk-consuming leftovers behind
- If a worktree is deleted unexpectedly without `git worktree remove`, run `git worktree prune` to clean the records
- **Always run `git fetch origin` before creating a worktree** and base it on `origin/main`, not local `main`, or you may start from stale code and create PR conflicts
- **Any exploration that may turn into editing should happen in a worktree**, because exploration often turns into real development, and moving changes afterward is tedious and easy to get wrong
