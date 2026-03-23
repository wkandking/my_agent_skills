# Agent 知识框架

这是一个用于管理 AI coding agent 团队知识的仓库。它采用“共享知识 + 角色私有知识”的分层结构，让多个 agent 能持续积累、检索和复用工程经验。

## 解决的问题

长期协作中，agent 会反复踩到相同的坑、重复发现相同的模式。这个框架提供：

- 结构化知识管理：把流程、原则、洞察、经验分开存放
- 按需加载：通过索引和触发条件只加载当前任务需要的知识
- 多 agent 协作规范：通过 worktree、PR 和显式规则降低并行修改冲突

## 目录结构

```text
agent-knowledge-framework/
├── AGENTS.md
├── README.md
├── LICENSE
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

## 知识分类

| 类别 | 定义 | 示例 |
|---|---|---|
| `experience` | 具体事件的复盘、踩坑记录、关键决策上下文 | 某次发布流程首次跑通的完整记录 |
| `skill` | 可复用的操作流程、checklist、操作剧本 | 压测报告打包流程 |
| `principle` | 稳定的行为准则和强约束 | 每个功能使用独立 worktree |
| `insight` | 从多次经验中归纳出的规律性认知 | 多轮 review 比一次性大修更可靠 |

详细分类标准和沉淀规则见 `base/knowledge-sedimentation.md`。

## 当前共享技能

- `base/skills/eat`
- `base/skills/skill-creator`
- `base/skills/skill-creator-codex`

## 当前角色

- `roles/cli-tool-dev`
- `roles/maintainer`
- `roles/performance-infra-tester`

## 快速开始

### 新建角色

```bash
cp -r roles/_template roles/<role-name>
```

然后按实际角色职责填写 `roles/<role-name>/AGENTS.md`。

### 知识加载顺序

1. 读取仓库根 `AGENTS.md`
2. 读取目标角色的 `roles/<role>/AGENTS.md`
3. 按索引和触发条件按需读取 `skill`、`principle`、`insight`
4. 需要证据、边界或上下文时再回溯 `experience`

### 协作流程

本仓库假定多个 coding agent 可能同时修改，写操作通过 worktree + PR 进行：

```bash
git fetch origin
git worktree add .claude/worktrees/<topic> -b <agent>/<topic> origin/main
cd .claude/worktrees/<topic>
# ... 编辑、commit ...
git push -u origin <agent>/<topic>
```

完整规则见 `AGENTS.md` 和 `base/principles/git-worktree.md`。
