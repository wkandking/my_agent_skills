# Agent 协作规则

每个 agent 在开始任何任务前，必须先通读本文件和相关角色的 `AGENTS.md`，再开始动手。

## 仓库结构

```text
agent-knowledge-framework/
├── AGENTS.md
├── base/
│   ├── AGENTS.md
│   ├── experience/
│   ├── principles/
│   ├── skills/
│   ├── insights/
│   └── knowledge-sedimentation.md
├── doc/
└── roles/
    ├── _template/
    ├── cli-tool-dev/
    ├── maintainer/
    ├── performance-infra-tester/
    └── <role>/
```

## 知识加载与沉淀

- 常驻 context：`AGENTS.md` + `roles/<role>/AGENTS.md`
- 按需加载：先读索引，再按需读取 `skill`、`principle`、`insight`，必要时回溯 `experience`
- 症状或高风险场景可直达 `experience`
- 如果不确定索引内容、协作规则或加载顺序，说明 context 可能已被压缩，应立即重读本文件和角色 `AGENTS.md`

详细加载策略见 `base/principles/knowledge-loading.md`。
详细沉淀规则见 `base/knowledge-sedimentation.md`。

## 角色补充规则

- `role` 是知识的组织单元，不是 agent 的固定身份。
- 一次任务如果同时涉及多个视角，应同时读取相关 `roles/<role>/AGENTS.md`，不要为了“只选一个角色”而丢失必要上下文。

## 当前共享技能

- `base/skills/eat/`
- `base/skills/skill-creator/`
- `base/skills/skill-creator-codex/`

## 多 Agent 协作规则

本仓库假定多个 coding agent 可能同时修改，所有写操作必须遵守以下规则。

Agent 工作中涉及两类仓库，规则同样适用：

- Agent 目录：本仓库，存放角色知识、经验和技能文档
- 工作目录：实际代码仓库

### 1. 所有写操作必须在 worktree 中进行，禁止直接在主工作目录上开发

始终创建 worktree，不要在主工作目录中直接 `git checkout -b` 后开始编辑。只读操作可以在主 worktree 上进行。

常见违规模式：

- `git checkout -b <branch>` 后直接在主工作目录编辑
- “先探索一下，之后再搬到 worktree”

正确流程：

```bash
git fetch origin
git worktree add .claude/worktrees/<topic> -b <agent>/<topic> origin/main
cd .claude/worktrees/<topic>
# ... 编辑、commit ...
git push -u origin <agent>/<topic>
```

关键点：永远基于 `origin/main` 创建 worktree，不要基于可能落后的本地 `main`。

### 2. 通过 PR 合并，agent 不自行 merge

- push 分支后创建 PR，由人工 review 后合并
- agent 不得自行 merge PR
- push 前如有冲突，先 `git fetch origin && git rebase origin/main`

### 3. push 后同步更新 PR 标题和描述

向已有 PR 的分支 push 新 commit 后，必须更新 PR 标题和描述，使其反映分支的完整变更。

### 4. 完成后清理 worktree

```bash
git worktree remove .claude/worktrees/<topic>
git branch -d <agent>/<topic>
```

## Git 提交规范

- 每次 `git commit` 都必须写清晰的提交信息
- 提交信息应直接说明结果，不要写成模糊描述
- 推荐格式：`<type>: <what changed>`

常用 `type`：

- `feat`
- `fix`
- `docs`
- `refactor`
- `test`
- `chore`

示例：

- `feat: add eat source ingestion for attachments`
- `fix: resolve eat target path under home`
- `docs: clarify eat update workflow`

如果同一组改动包含多个无关主题，应拆分成多个 commit。

## 开工 Preflight

### 1. 先进入角色

每个任务的第一条回复都应明确当前使用的角色，并说明已读取对应 `roles/<role>/AGENTS.md`。

### 2. 路径必须先验证

先用 `ls`、`rg` 等命令确认真实路径，再打开或引用文件。找不到时要明确说明仓库中不存在该路径，并给出最接近的候选项。

### 3. 触发型知识先读

- 接触凭证、权限、token：先读 `base/principles/credential-safety.md`
- 长任务、批处理、大量实验：先读相关原则或技能

### 4. 确认本地是否最新

在开工前、push/提 PR 前、遇到奇怪冲突或缺文件时，对 Agent 目录和工作目录都要检查：

```bash
git fetch origin
git rev-list --left-right --count main...origin/main
git pull --rebase origin main
```

写操作仍以 `origin/main` 创建 worktree 为准，不依赖本地 `main`。
