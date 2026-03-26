---
kind: principle
description: "默认使用 generalist-engineer，除非任务的核心风险是机制解释或性能证据。"
triggers:
  - "default role"
  - "which role"
  - "general coding"
  - "日常开发"
---

# 默认工程角色边界

当任务不明显属于某个专门视角时，优先使用 `generalist-engineer`。

## 使用这个角色

- 常规 feature、bugfix、refactor
- 一般代码 review
- 知识库中的普通结构调整和文档改动

## 不要继续停留在这个角色

- 如果真正的问题是“为什么会这样工作”，升级到 `mechanism-analyst`
- 如果真正的问题是“性能证据是否成立”，升级到 `performance-infra-tester`
