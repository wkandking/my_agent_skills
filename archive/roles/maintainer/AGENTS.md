# maintainer

## 职责

维护 agent 知识仓库的可发布与可维护性，重点覆盖：

- `installable-skills/` 的结构与发布质量（可装、可触发、可迁移、自包含）
- skill 的"入口清晰 + 引用闭包"（避免安装后出现坏链接/缺文件/依赖仓库根目录布局）
- 文档/示例的最小漂移：source-of-truth 明确、internal/public 分叉可控

## 使用的工具

- 搜索/批量校验：`rg`、`python`
- Git 协作：`git worktree`、`git fetch`/`rev-list`
- skill 安装与验证：`npx skills add`、`quick_validate.py`（如可用）

## 相关知识

- `AGENTS.md` — 多 agent 协作规则（worktree、禁止 push main、PR 流程）
- `base/principles/git-worktree.md`
- `base/principles/knowledge-loading.md`
- `base/knowledge-sedimentation.md`

## 角色知识索引

> 本索引是 agent 的**首要加载入口**。先读索引了解有哪些知识，再按需 `Read` 具体文件。不要一次性加载所有文档。
>
> 每条摘要必须包含**足够的关键词**，让 agent 能判断是否与当前任务相关。

### Skills

- `skills/installable-skill-hygiene/SKILL.md` — installable skill "发布前检查"清单：禁止引用 skill 目录外路径、引用闭包自检、`rg` 快速扫描，以及"单文件 vs references/"两种发布口径的取舍。
- `skills/github-actions/SKILL.md` — GitHub Actions workflow 实战编写与调试：触发方式速查（push/pr/schedule/dispatch）、`needs` DAG 与 `if` 条件执行、`nick-fields/retry` 重试、secret/variable 注入、timeout/cancel/failure 的 conclusion 差异（timeout 在 job 级别是 `cancelled` 不是 `timed_out`）、`gh run` 调试命令。

### Principles

### Insights

### Experience（按需查阅，不常驻加载）

- `experience/2026-03-07-github-actions-lab-plan.md` — `st1page/gh-actions-lab` 实验仓库的 9 个 workflow 设计计划与验证清单。
- `experience/2026-03-08-github-actions-lab-execution.md` — 9 个 workflow 的执行记录：关键发现 timeout conclusion 是 `cancelled`、`gh run cancel` 覆盖行为、paths filter 与 dispatch 交互、rerun --failed 范围。
- `experience/2026-03-08-sedimentation-delivery-checklist-gap.md` — 知识沉淀交付时遗漏联动更新（AGENTS.md 索引、front matter triggers、交叉引用冗余、表述矛盾），根因是"抄已有文件格式而非回读规范"和"逐块修改不回看整体"。

### Questions（已知的未知）

- `questions.md` — 0 条待验证
