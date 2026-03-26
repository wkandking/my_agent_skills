# 通用原则

团队共享的原则和规范。

## 索引

- [credential-safety.md](credential-safety.md) — agent 工作中接触凭证时的安全原则：不提交、不硬编码、不打印
- [git-worktree.md](git-worktree.md) — 多 agent 并行开发时使用 git worktree 隔离工作目录的规范
- [check-conventions-first.md](check-conventions-first.md) — 添加新功能前先查项目已有惯例（命名、迁移脚本、CLI 风格），避免风格不一致返工
- [knowledge-loading.md](knowledge-loading.md) — 知识加载策略详述：分层加载、常驻 vs 按需判断标准、experience 唤醒、context 压缩后重新加载、摘要写法
- [let-it-crash.md](let-it-crash.md) — 禁止静默 fallback/兜底：内部错误应 crash 暴露而非吞掉；只在系统边界做防御；fallback 需求本身是 bug 信号
- [let-it-crash-for-batch-jobs.md](let-it-crash-for-batch-jobs.md) — batch job 错误处理应区分'可预期的业务异常'和'不可预期的系统故障'：前者在代码中处理并正常退出，后者让任务直接崩溃由调度器重启
- [persistent-task-state-must-be-externalized.md](persistent-task-state-must-be-externalized.md) — 需要跨 session、跨 agent 保留的任务状态，必须外显到文件、branch、日志或标准 CLI 产物
- [explicit-tmpdir-for-long-jobs.md](explicit-tmpdir-for-long-jobs.md) — 长任务/高并行任务禁止依赖默认 /tmp；必须显式指定 TMPDIR 到可控路径

## 文档格式约定

每个原则文档应包含：

- **标题**：简明描述原则名称
- **背景**：为什么需要这个原则
- **内容**：原则的具体描述
- **示例**：正面和反面示例（可选）
