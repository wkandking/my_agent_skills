# 2026-03-07: GitHub Actions 实验仓库设计计划

## 背景

目标：在一个新建的公共实验仓库中系统性学习 GitHub Actions 的 9 个核心场景，最终沉淀为 `skills/github-actions/SKILL.md`。

## 实验仓库

- 仓库：`st1page/gh-actions-lab`（公共，仅用于实验，不连接生产环境）

## 9 个 Workflow 设计

### 1. `01-dependent-jobs.yml` — job 依赖关系
- 3 个 job: build → test → deploy，用 `needs` 串联
- deploy 依赖 build + test 同时完成，演示 DAG 语义

### 2. `02-conditional-trigger.yml` — 条件触发
- `on.push.paths`: 只在 `src/**` 变更时触发
- `on.push.branches`: 只在 `main` 分支
- step 级别用 `if: contains(github.event.head_commit.message, '[deploy]')` 条件执行

### 3. `03-scheduled.yml` — 定时运行
- `on.schedule: cron: '*/15 * * * *'`（每 15 分钟）
- 打印时间戳，输出到 Job Summary

### 4. `04-pr-check.yml` — PR 检查 + 阻塞合并
- `on: pull_request`，运行 lint 检查
- 配合 branch protection rule 的 required status check

### 5. `05-retry-flaky.yml` — 偶发失败自动重试
- 用 `nick-fields/retry@v3` 包裹 50% 概率失败命令
- `max_attempts: 3`, `retry_wait_seconds: 5`
- 对比有重试 vs 无重试的 step

### 6. `06-parameterized.yml` — 参数化 workflow
- `on: workflow_dispatch` with inputs（environment choice, debug boolean, version string）
- 不同 input 走不同 `if` 分支
- `gh workflow run` 触发

### 7. `07-external-config.yml` — 外部配置注入
- 读取 `vars.DEPLOY_TARGET`（repository variable）
- 读取 `secrets.API_KEY`（repository secret）
- 演示 environment-specific 配置

### 8. `08-rerun-compare.yml` — 重跑与比较
- 记录 `github.run_attempt`、时间戳
- 输出到 Job Summary + artifact
- 比较 `gh run rerun` vs `gh run rerun --failed`（全量重跑 vs 仅失败 job 重跑）

### 9. `09-timeout-cancel.yml` — 超时、中断与失败差异
- 3 个 job: timeout（`timeout-minutes: 1` + `sleep 120`）、cancelled（concurrency group 或手动取消）、normal_fail（`exit 1`）
- 观察 conclusion 差异：`timed_out` vs `cancelled` vs `failure`

## 执行计划

1. 创建仓库，一次性提交所有 workflow + 辅助文件
2. `gh workflow run` / `gh api` 触发
3. `gh run list` / `gh run watch` 实时监控
4. `gh run view --log` 导出日志
5. 逐个验证 → 修复 → 重跑

## 验证清单

- [x] 每个 workflow 至少成功运行一次（或按预期失败）
- [x] PR check 阻塞合并
- [x] scheduled workflow 被注册
- [x] retry 最终成功
- [x] timeout/cancel/failure 的 conclusion 差异可观测
- [x] rerun attempt number 递增

> 执行记录见 [2026-03-08-github-actions-lab-execution.md](2026-03-08-github-actions-lab-execution.md)

## 产出

- `roles/maintainer/skills/github-actions/SKILL.md` — GitHub Actions 实战编写与调试 skill
- `roles/maintainer/experience/2026-03-08-github-actions-lab-execution.md` — 执行记录与关键发现
