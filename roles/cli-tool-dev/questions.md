# 开放问题

> 记录已知的未知：注意到了但还没验证的疑问、假说和不确定性。
>
> - Question 不是 TODO，允许长期存在。
> - 简单问题可直接写一行 checkbox；需要背景时可展开成 `##` 小节。
> - 解决后勾选并注明去向（例如某条 `experience`、`skill` 或 `insight`）。
> - 新增问题后，记得同步更新角色 `AGENTS.md` 的 Questions 条目数。

- [ ] textual `@work(thread=True)` 与 `asyncio.create_subprocess_exec`：当数据源是 subprocess 时，使用 asyncio 原生协程是否会比 thread worker 更高效？当前选择 `@work`，是因为它自带 worker 管理能力（cancel/exclusive/group），但仍需要在真实场景中验证。
- [ ] `gh` CLI failed step 检测：目前用启发式方法（检查最后 20 行是否含 error/fail/exit code）判断 step 是否失败。`gh api` 的 checks/steps endpoint 是否能直接返回 step 级别的 `conclusion` 字段？如果可以，可以替代当前启发式方案。
