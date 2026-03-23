---
name: github-actions
description: 实战编写与调试 GitHub Actions workflow：触发方式、job 依赖、条件执行、重试、secret/variable 注入、超时取消行为、调试技巧。触发条件：编写/调试 GitHub Actions workflow、CI/CD 配置、gh run 操作。
triggers:
  - "GitHub Actions"
  - "workflow"
  - "gh run"
  - "CI/CD"
  - "workflow_dispatch"
  - "needs"
  - "timeout-minutes"
  - "concurrency"
  - "rerun"
source:
  - roles/maintainer/experience/2026-03-07-github-actions-lab-plan.md
  - roles/maintainer/experience/2026-03-08-github-actions-lab-execution.md
---

# GitHub Actions 实战编写与调试

目标：快速编写正确的 GitHub Actions workflow，高效调试失败，理解平台行为边界。

> 实验仓库：`st1page/gh-actions-lab`（9 个场景的完整 workflow 示例）

## 1. 触发方式速查

| 触发 | `on:` 写法 | 典型用途 |
|------|-----------|---------|
| Push | `push: { branches: [main], paths: ["src/**"] }` | CI |
| PR | `pull_request: { branches: [main] }` | 代码审查 |
| 定时 | `schedule: [{ cron: "*/15 * * * *" }]` | 周期任务 |
| 手动 | `workflow_dispatch: { inputs: ... }` | 按需触发 |
| API | `repository_dispatch` 或 `gh workflow run` | 外部集成 |

**paths filter 边界**：只匹配 push 事件中实际变更的文件；如果 commit 没改 `src/**` 下的文件，即使 push 到 main 也不触发。`workflow_dispatch` 触发时 paths filter 不生效。

**cron 延迟**：GitHub 不保证 cron 准时触发，高峰期可延迟 5–30 分钟。Cron 只在 default branch 生效。

## 2. Job 依赖与条件执行

### needs DAG

```yaml
jobs:
  build: ...
  test-unit:
    needs: build        # build 完成后才跑
  test-integration:
    needs: build        # 与 test-unit 并行
  deploy:
    needs: [test-unit, test-integration]  # 两个都过才 deploy
```

`needs` 形成 DAG，同层无依赖的 job 自动并行。

### if 条件

```yaml
# commit message 包含 [deploy] 时才执行
- if: contains(github.event.head_commit.message, '[deploy]')

# 仅 PR 事件
- if: github.event_name == 'pull_request'

# 前置 job 失败也要跑（清理/汇报）
jobs:
  observer:
    needs: [job_a, job_b]
    if: always()    # 不管前置结果都跑
```

### concurrency 控制

```yaml
concurrency:
  group: deploy-${{ github.ref }}
  cancel-in-progress: true    # 新 run 自动取消旧 run
```

## 3. 重试策略

### Step 级重试（nick-fields/retry）

```yaml
- uses: nick-fields/retry@v3
  with:
    timeout_minutes: 2
    max_attempts: 3
    retry_wait_seconds: 5
    command: |
      # 可能偶发失败的命令
      curl -f https://example.com/api
```

### Run 级重跑

```bash
# 全量重跑（所有 job 重新执行）
gh run rerun <run-id>

# 仅重跑失败的 job（已成功的跳过）
gh run rerun <run-id> --failed
```

**run_attempt 递增**：每次 rerun，`github.run_attempt` +1（首次为 1）。可用于区分首次运行和重跑：

```yaml
- run: echo "Attempt ${{ github.run_attempt }}"
```

Artifact 名中带 attempt 可追踪每次运行的产物差异。

## 4. Secret & Variable 注入

### 设置

```bash
gh secret set API_KEY --body "xxx" -R owner/repo
gh variable set DEPLOY_TARGET --body "staging" -R owner/repo
```

### 在 workflow 中使用

```yaml
env:
  API_KEY: ${{ secrets.API_KEY }}       # 自动 mask，日志中显示 ***
steps:
  - run: echo "Target: ${{ vars.DEPLOY_TARGET }}"  # 明文，不 mask
```

**区别**：`secrets.*` 日志自动遮蔽；`vars.*` 明文输出。Secret 不能在 `if:` 条件中直接比较（始终为 `***`）。

### Environment-specific

可为 `production`/`staging` 等 environment 分别设置 secret 和 variable，job 级别指定 `environment:`。

## 5. 超时与取消行为

### 关键发现（实验验证）

| 场景 | job conclusion（API） | `needs.*.result` |
|------|---------------------|-----------------|
| `timeout-minutes` 超时 | `cancelled` | `cancelled` |
| `gh run cancel` 手动取消 | `cancelled` | `cancelled` |
| `exit 1` 正常失败 | `failure` | `failure` |
| `if: false` 跳过 | `skipped` | `skipped` |

**重要**：GitHub Actions 中 timeout 导致的 job conclusion 是 `cancelled`，**不是** `timed_out`。`timed_out` 只出现在 step 级别的 annotation 中。在 `needs` 上下文里，timeout 和手动 cancel 无法区分。

### 配置

```yaml
jobs:
  my_job:
    timeout-minutes: 10    # job 级超时（默认 360 分钟）
    steps:
      - timeout-minutes: 5  # step 级超时
        run: long-running-command
```

### 区分超时 vs 取消

如果需要区分，只能查看 run 的 annotation 或 log：
- 超时会有 annotation: `The job has exceeded the maximum execution time`
- 手动取消会有: `The run was canceled by @username`

## 6. 调试技巧

### 查看日志

```bash
# 列出最近运行
gh run list -R owner/repo

# 查看运行详情
gh run view <run-id>

# 查看完整日志
gh run view <run-id> --log

# 只看失败 job 的日志
gh run view <run-id> --log-failed

# 实时监控
gh run watch <run-id>
```

### Job Summary

在 step 中写入 `$GITHUB_STEP_SUMMARY`，结果显示在 GitHub UI 的 run summary 页面：

```yaml
- run: echo "## Results" >> "$GITHUB_STEP_SUMMARY"
```

### 手动触发调试

```bash
# 带参数触发
gh workflow run "workflow-name" -f key=value -R owner/repo

# 触发后获取 run ID
gh run list -R owner/repo --limit 1
```

### API 查询 job 详情

```bash
gh api repos/owner/repo/actions/runs/<run-id>/jobs \
  | jq '.jobs[] | {name, conclusion, started_at, completed_at}'
```

## 7. 常见陷阱

1. **cron 不准时**：schedule 延迟 5–30 分钟很正常，不要依赖精确时间
2. **paths filter + workflow_dispatch**：dispatch 触发时 paths filter 不生效（workflow 总是会跑）
3. **Required checks 配置**：需要在 repo settings → branch protection rule 中手动添加 workflow 名为 required status check
4. **Timeout conclusion 不是 timed_out**：job 级别的 conclusion 是 `cancelled`，不要在 `if: needs.*.result == 'timed_out'` 中判断
5. **Secret 不能用于 if 条件**：`if: secrets.X != ''` 不工作，需要通过 env 中转后在 shell 中判断
6. **concurrency cancel-in-progress**：新 run 会取消旧 run 中所有正在运行的 job，不仅仅是同名 job
7. **gh run rerun --failed 范围比名字暗示的更广**：重跑所有非 success 的 job（包括 `failure` 和 `cancelled`），不仅仅是 `failure`
8. **Artifact 名称冲突**：同一 run 的多次 attempt 产出的 artifact 需要用 `run_attempt` 区分名称

## Escalate to experience if

- Workflow 间需要共享数据（跨 workflow artifact 传递）
- 需要 matrix strategy 的复杂展开/排除逻辑
- 需要 reusable workflow 或 composite action 的封装模式
- 遇到 GITHUB_TOKEN 权限不足但不想用 PAT 的场景
