---
description: "batch job 错误处理应区分'可预期的业务异常'和'不可预期的系统故障'：前者在代码中处理并正常退出，后者让任务直接崩溃由调度器重启，不要用防御性代码掩盖未知故障"
triggers:
  - "let it crash"
  - "错误处理"
  - "重启策略"
  - "exit code"
  - "batch job 失败"
  - "防御性编程"
  - "fault tolerance"
source:
  - "https://ferd.ca/the-zen-of-erlang.html"
---

# 批量任务的 Let It Crash 原则

## 核心思想

来自 Erlang 社区的 "let it crash" 理念：与其到处写防御性错误处理试图恢复未知状态，不如让进程崩溃、由上层 supervisor 重启到已知良好状态。**crash 不是灾难，而是一种可控的恢复手段。**

应用到批量任务调度中：

## 区分两类错误

| 类型 | 例子 | 处理方式 |
|---|---|---|
| **可预期的业务异常** | 数据校验不通过、某个分区为空、输入格式不匹配 | 在代码中处理，记录日志，**正常退出（exit 0）** |
| **不可预期的系统故障** | OOM、网络超时、依赖服务不可用、未知异常 | **不要 try-catch 吞掉**，让任务崩溃（exit != 0），由调度器按 restart policy 重启 |

### 为什么不要 catch 所有异常

```python
# 反模式：吞掉所有异常，任务"成功"但结果不可靠
try:
    process(data)
except Exception as e:
    logger.error(f"failed: {e}")
    # 继续执行下一批...状态可能已经损坏
```

这种做法的问题：
- 进程可能已处于**损坏的中间状态**，后续输出不可信
- 调度器认为任务成功，不会重试
- 错误被淹没在日志里，没人注意到

```python
# 正确做法：只处理已知的、可恢复的异常
try:
    process(data)
except ValidationError as e:
    logger.warning(f"skipped invalid partition: {e}")
    # 已知异常，可以安全跳过
except Exception:
    # 未知异常，让它崩溃，调度器会重启
    raise
```

## 让调度器当 Supervisor

批量任务调度器的 restart 机制天然扮演 Erlang supervisor 的角色：

- **restart policy**：设置合理的重试次数和间隔（如 3 次，间隔递增）
- **隔离性**：每个任务独立运行，一个崩溃不影响其他
- **升级（escalation）**：重试耗尽后标记 failed，由人介入判断

关键：**任务必须支持幂等重启**。调度器重启时，任务要能从上次中断的地方安全继续，或从头重跑而不产生重复数据。实现方式：
- 按分区写 `_SUCCESS` marker，跳过已完成分区
- 输出天然幂等（覆盖写而非追加写）
- 支持 `--resume` 从 state 文件续跑

## 边界：什么时候不该 crash

- **有明确恢复路径的已知错误**：网络超时可以重试 3 次再放弃，不需要杀掉整个任务
- **部分失败可接受的批处理**：处理 1000 个分区，3 个格式异常，记录后跳过比整体崩溃更合理
- **有昂贵的前置计算**：如果崩溃意味着从头开始 2 小时的计算，应该做 checkpoint 而非简单 crash

## 与 let-it-crash.md 的关系

`let-it-crash.md` 聚焦于代码层面的"禁止静默 fallback"——内部错误不应被吞掉。本文档是其在**批量任务调度**场景的延伸：不仅代码层面不吞错误，还要利用调度器的 restart 机制作为恢复手段。

## 总结

| 原则 | 做法 |
|---|---|
| 已知异常 → 处理 | 校验失败、空数据等在代码中优雅处理，exit 0 |
| 未知异常 → crash | 不要 catch-all，让调度器重启恢复到已知状态 |
| 任务必须幂等 | 支持重跑/续跑，crash 后重启不产生脏数据 |
| 调度器当 supervisor | 设 restart policy、隔离任务、重试耗尽再升级 |

## Escalate to experience if

- 需要了解 exit code 语义映射的具体案例（"发现问题"vs"任务失败"的区分）
- 需要 restart policy 的具体配置示例
