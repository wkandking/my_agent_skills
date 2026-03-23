---
description: "TUI 开发中阻塞 IO（subprocess、HTTP、文件读写）必须在后台线程执行，UI 线程只做渲染和事件处理，否则界面冻结。"
triggers:
  - "UI 卡"
  - "界面冻结"
  - "subprocess"
  - "阻塞"
  - "TUI"
  - "textual"
source:
  - "roles/cli-tool-dev/experience/2026-03-08-textual-async-loading-cache.md"
---

# UI 线程禁止阻塞 IO

## 内容

在 TUI（textual 等框架）开发中，**所有阻塞 IO 操作必须移出 UI 线程**。

违反此原则的症状：用户每次移动光标、切换选项时界面冻结 1-2 秒，完全无法交互。

## 执行方式（textual）

使用 `@work(thread=True)` 将阻塞操作移到后台线程，通过 `call_from_thread` 回到主线程更新 UI。

详见 skill: `skills/textual-async-data-loading/SKILL.md`

## 边界

- **纯 CPU 计算**（如格式化字符串、排序小列表）可以在 UI 线程做，延迟通常 <10ms，用户无感知
- **首次加载**也不能在 `on_mount` 中同步执行——用 LoadingIndicator 过渡

## Escalate to experience if

- 需要评估某个操作是否"足够快"可以留在 UI 线程
