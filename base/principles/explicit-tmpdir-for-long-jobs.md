---
description: "长任务/高并行任务禁止依赖默认 /tmp；必须显式指定 TMPDIR/临时目录到可控路径，并把清理设计成可独立执行（假设随时 SIGKILL）"
triggers:
  - "TMPDIR"
  - "tempfile"
  - "TemporaryDirectory"
  - "/tmp"
  - "OOM kill"
  - "Exit Code 137"
---

# 长任务必须显式指定临时目录（禁止默认 `/tmp`）

## 背景

长任务（>30min）或高并行任务在 cgroup/调度系统里更容易遇到 OOM kill。被 `SIGKILL` 时，进程内清理逻辑（`finally`/`__exit__`/`atexit`）不可靠，默认 `/tmp` 极易泄漏并拖垮节点磁盘。

## 规则

当任务满足任一条件时，**必须**显式指定临时目录：

- 预计运行超过 30 分钟
- 可能产生大量临时文件（下载缓存、中间件、大文件解压/落盘）
- 并行度 > 4 或单文件 > 50 MB（容易瞬时堆积）

## 推荐做法

1) 选择一个可控路径（优先放到任务归档目录或持久化存储）：

- `<project-dir>/long-tasks/<YYYY-MM-DD>-<topic>/tmp/`
- 或其他可控的持久化路径

2) 显式设置 `TMPDIR`（或在代码里指定 `dir=`）：

```bash
export TMPDIR="<project-dir>/long-tasks/<YYYY-MM-DD>-<topic>/tmp"
mkdir -p "$TMPDIR"
```

3) 清理要可独立执行（不要只靠"任务结束自动清理"）：

- 把临时文件前缀设计成可 grep 的模式（如 `<topic>_tmp_*`）
- 需要时用单独的清理任务做清理（避免依赖主任务 finally）
