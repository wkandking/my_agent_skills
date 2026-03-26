---
kind: principle
description: "多 agent 并行开发时使用 git worktree 隔离工作目录的规范"
triggers:
  - "worktree"
  - "多 agent"
  - "并行开发"
  - "分支隔离"
source:
  - "base/principles/git-worktree.md"
---

# Git Worktree 多 Agent 协作规范

## 背景

多个 agent 可能同时对本仓库进行读写操作。如果共用同一个工作目录，会产生文件冲突、脏状态和 merge 混乱。Git worktree 允许从同一个仓库创建多个独立的工作目录，每个 agent 在自己的 worktree 中工作，互不干扰。

## 核心规则

1. **只读操作**可以直接在主 worktree（`main` 分支）进行
2. **写操作**必须在独立 worktree 中进行，完成后通过 PR 合并
3. 每个 worktree 对应一个独立分支，分支命名需包含 agent 标识

## 工作流

### 创建 worktree

```bash
# 在仓库根目录执行
git fetch origin
git worktree add .claude/worktrees/<topic> -b <agent>/<topic> origin/main

# 示例
git worktree add .claude/worktrees/add-new-skill -b alice/add-new-skill origin/main
```

### 在 worktree 中工作

```bash
cd .claude/worktrees/add-new-skill
# 正常编辑、commit
git add ...
git commit -m "..."
git push -u origin alice/add-new-skill
```

### 提交 PR 并清理

```bash
# 推送后创建 PR
git push -u origin alice/add-new-skill
# 创建 PR → review → merge

# 合并后清理 worktree
cd /path/to/main-worktree
git worktree remove .claude/worktrees/add-new-skill
git branch -d alice/add-new-skill
```

### 同步 main 的最新变更

```bash
# 在 worktree 中拉取 main 的更新
git fetch origin
git rebase origin/main
```

## 分支命名约定

```
<agent-name>/<topic>
```

示例：
- `alice/add-new-skill`
- `bob/update-docs`
- `charlie/promote-principle`

## 反模式：用 stash 跨分支搬改动

**不要**用 `git stash` + `git checkout` + `git stash pop` 把改动从一个分支搬到另一个分支，尤其当两个分支的文件结构不同时。

### 正确做法

**方法一：worktree（推荐）**

从一开始就在 worktree 里操作，完全隔离：

```bash
git worktree add .claude/worktrees/update-docs -b claude/update-docs origin/main
cd .claude/worktrees/update-docs
# 直接编辑文件，commit，push
# 不会碰到任何 stash/冲突问题
```

**方法二：精确 checkout 单个文件**

如果已经 stash 了，不要 `stash pop`，用 `git checkout` 只取需要的文件：

```bash
git stash
git worktree add .claude/worktrees/update-docs -b claude/update-docs origin/main
cd .claude/worktrees/update-docs
git checkout stash -- path/to/file.md   # 只取一个文件
git stash drop
```

### 经验总结

| 场景 | 推荐做法 | 避免 |
|---|---|---|
| 从已有分支拆出部分改动到新分支 | worktree 或 `git checkout stash -- <file>` | `git stash pop`（整体弹出） |
| 两个分支文件结构不同 | worktree | stash 跨分支搬运 |
| 只有一个文件要搬 | `git show stash:path > file` 或 `git checkout stash -- path` | `stash pop` 后手动清理 |

## 注意事项

- 同一分支不能同时被多个 worktree checkout，git 会拒绝
- worktree 中的 submodule 需要单独初始化：`git submodule update --init`
- 完成工作后务必清理 worktree，避免残留占用磁盘
- 如果 worktree 被意外删除（未用 `git worktree remove`），用 `git worktree prune` 清理记录
- **创建 worktree 前必须 `git fetch origin`**，基于 `origin/main` 而非本地 `main`，否则可能基于过时代码开发导致 PR 冲突
- **即使是「先探索一下」也应该在 worktree 里做**，因为探索很容易变成正式开发，事后再搬改动到 worktree 步骤繁琐且容易遗漏文件
