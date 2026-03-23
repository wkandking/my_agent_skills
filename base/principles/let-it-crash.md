---
description: "禁止静默 fallback/兜底：内部错误应 crash 暴露而非吞掉；只在系统边界做防御；fallback 需求本身是 bug 信号"
triggers:
  - "fallback"
  - "兜底"
  - "降级"
  - "unwrap_or"
  - "try except"
  - "catch"
  - "default value"
  - "silent"
  - "静默"
  - "error handling"
---

# Let It Crash：禁止静默 fallback

## 背景

Agent 写代码时倾向于在每个可能出错的地方加 `try-except` / `unwrap_or(default)` / `catch` 兜底。动机是"让系统不要挂"，但实际效果是：

1. **错误被隐藏** — 调用者以为成功了
2. **系统进入半死不活的状态** — 不是彻底不工作（那反而容易发现），而是"工作但结果不对"
3. **排查成本指数级放大** — 问题在远离根因的地方才暴露

这与 Erlang 的 "Let It Crash" 哲学相悖：写纠正错误的代码（corrective code），而不是掩盖错误的代码（defensive code）。

## 内容

### 1. 内部逻辑错误必须 crash，不要 fallback

内部函数调内部函数时，如果出错说明有 bug，应该立刻暴露（抛异常 / 返回 Err / panic），而不是返回默认值继续跑。

### 2. 只在系统边界做防御

以下场景可以 catch + 有意义的处理：
- 解析用户输入
- 调用外部 API / 网络请求
- 读取外部文件 / 数据库

内部模块间调用不应加 try-except。

### 3. catch 了必须做有意义的事

- `log + re-raise` — 可以
- `return None / 默认值` — 不行（除非这是明确的业务需求且调用者知道这个语义）
- 区分 transient（网络超时 → log warning + retry）和 permanent（逻辑错误 → crash）

### 4. 不要假装有 fallback

如果 fallback 路径的状态不再被更新，或者 fallback 值与原值语义不同，删掉 fallback 代码，而不是留着。

### 5. seed / 初始化阶段绝对禁止静默降级

初始化失败但"继续跑"，后面所有结果都不可信。启动失败就 crash，让上层决定怎么办。

### 6. "需要 fallback 才能工作"是 bug 信号

看到 `unwrap_or(0)` / `or None` / `catch: pass` 时，不要加更多 fallback，而要反向追问"为什么会出错？"并修掉根因。

## 示例

反面（静默 fallback）：
```rust
// 缺字段 → 返回 0 → 下游排序被污染
let ts = event.timestamp_ns().unwrap_or(0);
```

```python
# catch all 并 skip → transient error 无法排查
try:
    process_one(key)
except Exception:
    continue
```

正面（fail-fast）：
```rust
// 缺字段 → 明确报错 → 立刻发现
let ts = event.timestamp_ns()
    .ok_or(Error::MissingTimestamp)?;
```

```python
# 区分 transient / permanent
try:
    process_one(key)
except (ConnectionError, TimeoutError) as e:
    logger.warning("transient error for %s: %s", key, e)
    continue
# 其他异常不 catch，让它 crash
```

## 参考

- [Let It Crash — wiki.c2.com](https://wiki.c2.com/?LetItCrash)
- [Joe Armstrong on Let It Crash](https://dev.to/adolfont/the-let-it-crash-error-handling-strategy-of-erlang-by-joe-armstrong-25hf)
