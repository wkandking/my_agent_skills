---
description: "textual TUI 异步数据加载完整模式：@work(thread=True) 后台执行阻塞 IO → call_from_thread 回主线程渲染 → LoadingIndicator 过渡 → exclusive group 防抖 → dict 缓存 + stale check 防竞态"
triggers:
  - "textual"
  - "@work"
  - "call_from_thread"
  - "LoadingIndicator"
  - "UI 卡"
  - "界面冻结"
  - "异步加载"
  - "防抖"
  - "缓存"
  - "stale check"
source:
  - "roles/cli-tool-dev/experience/2026-03-08-textual-async-loading-cache.md"
---

# textual TUI 异步数据加载模式

目标：在 textual TUI 中执行阻塞 IO（subprocess、HTTP）时，保持 UI 响应，同时避免竞态和重复请求。

## 核心三件套

### 1. `@work(thread=True)` — 阻塞 IO 移出 UI 线程

```python
from textual import work  # 注意：不是 from textual.work import work

@work(thread=True)
def _fetch_data(self) -> None:
    result = subprocess.run(...)  # 在后台线程执行
    self.app.call_from_thread(self._render, result)  # 回主线程更新 UI
```

**陷阱**：`from textual.work import work` 会 `ModuleNotFoundError`。

### 2. `LoadingIndicator` — 加载过渡

compose 时同时 yield 数据 widget 和 loading indicator，用 `display` 属性互斥切换：

```python
def compose(self) -> ComposeResult:
    yield LoadingIndicator(id="loading")
    yield DataTable(id="table", cursor_type="row")

def on_mount(self) -> None:
    self.query_one("#table").display = False  # 初始隐藏数据

def _render(self, data) -> None:
    self.query_one("#loading").display = False
    self.query_one("#table").display = True
    # ... 填充数据
```

### 3. `call_from_thread` — worker 回调回主线程

worker 线程中不能直接操作 UI widget。必须通过 `self.app.call_from_thread(callback, *args)` 调度回主线程。

## 增强模式

### 4. exclusive worker group — 高频触发防抖

光标快速移动时，每次触发数据请求。用 `exclusive=True` + `group` 自动取消旧请求：

```python
@work(thread=True, exclusive=True, group="jobs")
def _fetch_jobs(self, run_id: int) -> None:
    ...
```

效果：连续触发只执行最后一个请求。

### 5. dict 缓存 + stale check

简单 dict 缓存已请求过的数据；异步回调时检查数据是否仍然是当前需要的：

```python
_cache: dict[int, Data] = {}

@work(thread=True, exclusive=True, group="jobs")
def _fetch_jobs(self, run_id: int) -> None:
    if run_id in self._cache:
        self.app.call_from_thread(self._render_jobs, run_id, self._cache[run_id])
        return
    result = fetch(run_id)
    self._cache[run_id] = result
    # stale check：渲染前确认用户没有切走
    if self._selected_run_id == run_id:
        self.app.call_from_thread(self._render_jobs, run_id, result)
```

刷新时清空整个 cache（CLI 工具生命周期短，不需要 TTL）。

## headless 测试中等待 worker

`pilot.pause()` 只处理事件队列，不等 worker 线程。必须轮询：

```python
async def wait_workers(app, pilot, timeout=15):
    import asyncio
    for _ in range(int(timeout / 0.1)):
        await pilot.pause()
        if all(w.is_finished for w in app.workers):
            return
        await asyncio.sleep(0.1)
    raise TimeoutError("workers not finished")
```

## Escalate to experience if

- 遇到 `@work` 的 import 路径报错或 `call_from_thread` 在测试中行为异常
- exclusive group 取消旧 worker 后出现数据丢失
- 需要评估缓存策略（TTL vs 手动刷新 vs LRU）
