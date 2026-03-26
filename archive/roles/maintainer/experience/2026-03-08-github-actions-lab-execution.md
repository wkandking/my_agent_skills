# GitHub Actions 9 场景实验：执行记录与发现

日期: 2026-03-08

## Triggers
- "GitHub Actions" "workflow" "gh run" "timeout" "cancelled" "needs" "conclusion"
- "timed_out" "concurrency" "cancel-in-progress" "rerun" "run_attempt"

## 背景

按 [实验设计计划](2026-03-07-github-actions-lab-plan.md) 在 `st1page/gh-actions-lab` 公共仓库中运行 9 个 workflow，覆盖 GitHub Actions 核心场景。

- 实验仓库：https://github.com/st1page/gh-actions-lab
- 沉淀 skill：`roles/maintainer/skills/github-actions/SKILL.md`

## 证据与现象

### 全部 workflow 运行结果

| # | Workflow | 触发方式 | 结果 | 备注 |
|---|---------|---------|------|------|
| 01 | Dependent Jobs | push + dispatch | ✅ success | needs DAG 正常并行 |
| 02 | Conditional Trigger | push(src/) + dispatch | ✅ success | paths filter 对 dispatch 不生效 |
| 03 | Scheduled | dispatch | ✅ success | cron 已注册 |
| 04 | PR Check | pull_request | ✅ lint failed | shellcheck 正确拦截未引用变量 |
| 05 | Retry Flaky | dispatch | ✅ success | nick-fields/retry 重试后通过 |
| 06 | Parameterized | dispatch -f | ✅ success | choice/boolean/string 输入正常 |
| 07 | External Config | dispatch | ✅ success | vars + secrets 均读取成功 |
| 08 | Rerun & Compare | dispatch + rerun | ✅ success | attempt 从 1 递增到 2 |
| 09 | Timeout/Cancel/Fail | dispatch + cancel | ✅ 按预期失败 | 见下方详细分析 |

### 关键发现：timeout 的 job conclusion 是 `cancelled` 而非 `timed_out`

这是本次实验最重要的发现。实验过程：

1. **首次运行 09**（run 22813148774）：timeout_job 超时后，手动 `gh run cancel` 取消了整个 run
   - 所有未完成 job 的 conclusion 都变为 `cancelled`
   - 无法区分是 timeout 还是手动 cancel

2. **第二次运行 09**（run 22813252092）：改进后移除了 long_sleep job，让 run 自然完成
   - timeout_job conclusion = `cancelled`（不是 `timed_out`！）
   - normal_fail conclusion = `failure`
   - long_sleep conclusion = `skipped`（因为 `if: false`）

3. **API 确认**：
   ```bash
   gh api repos/st1page/gh-actions-lab/actions/runs/22813252092/jobs \
     | jq '.jobs[] | {name, conclusion}'
   # timeout_job: "cancelled"
   # normal_fail: "failure"
   ```

4. **`needs` 上下文确认**：observer job 的 `needs.timeout_job.result` 也是 `cancelled`

结论：GitHub Actions 在 job 级别不区分 timeout 和 cancel，两者 conclusion 都是 `cancelled`。`timed_out` 只出现在 step 级别的 annotation 中（`The job has exceeded the maximum execution time`）。

### 次要发现

- **`gh run cancel` 覆盖所有运行中的 job**：取消一个 run 会把所有还在跑的 job 设为 cancelled，包括已经 timeout 的 job（conclusion 被覆盖）
- **paths filter + workflow_dispatch**：workflow_dispatch 触发时完全忽略 `on.push.paths` 过滤条件
- **rerun --failed 的范围**：不仅重跑 `failure` 的 job，`cancelled` 的 job 也会被重跑
- **Artifact 名称**：同一 run 不同 attempt 的 artifact 需要用 `github.run_attempt` 区分，否则会命名冲突

### Workflow 09 设计迭代

初版设计中 `cancelled_job` 有 `sleep 300`，导致每次都需要手动 cancel 整个 run（覆盖了 timeout 结论）。改进后加了 `inputs.include_long_sleep` boolean 开关，默认关闭，需要时才启用。

## 关键决策

- **决策**：timeout_job 的 timeout-minutes 设为 1（最小可观测值）
  - 依据：GitHub Actions 最小 timeout 粒度是分钟；1 分钟足够观察超时行为，同时不浪费 runner 时间
- **决策**：将 cancelled_job 改为条件启用
  - 依据：长 sleep 导致每次实验都要等 5 分钟才能看到 observer 结果；加开关后默认只测 timeout vs failure
- **决策**：observer job 使用 `if: always()` 收集所有 job 结论
  - 依据：默认情况下 `needs` 中有失败 job 时后续 job 会跳过；`if: always()` 确保 observer 始终运行

## 结果

9 个 workflow 全部验证通过（或按预期失败）。

- 产出：
  - 实验仓库：https://github.com/st1page/gh-actions-lab
  - PR #1（lint check demo）：https://github.com/st1page/gh-actions-lab/pull/1
- 沉淀：
  - `roles/maintainer/skills/github-actions/SKILL.md`：覆盖触发方式、job 依赖、重试、secret 注入、超时取消、调试技巧、常见陷阱
