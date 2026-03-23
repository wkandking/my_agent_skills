---
description: "文档的格式暴露类型错配：对比表/选型指南是 insight，不是 skill；skill 必须有可执行的操作流程（步骤/checklist），否则 agent 读了知道'该选什么'但不知道'怎么做'"
triggers:
  - "知识分类"
  - "skill 还是 insight"
  - "对比表"
  - "选型指南"
  - "文档格式"
  - "knowledge type"
---

# Insight: 文档格式暴露知识类型错配

## 观察

一份工具对比的"skill"文档，内容是对比表 + 场景推荐 + 常用参数。用户看完后指出"这不像常规意义上的 skill"。

问题在于：读完这份文档，agent 知道"什么场景选什么工具"，但不知道"拿到一个任务该怎么一步步执行"。前者是认知（insight），后者才是操作（skill）。

## 规律

**文档的结构形式是类型的强信号**：

| 你写出来的结构 | 实际是什么类型 | 不是什么类型 |
|---|---|---|
| 对比表、选型矩阵、优劣分析 | insight（规律性认知） | skill |
| 步骤流程、checklist、命令序列 | skill（操作流程） | insight |
| "做了什么 → 发现什么 → 怎么修" | experience（事件复盘） | skill/insight |
| "应该/不应该做 X" | principle（行为准则） | skill |

如果一份文档标了 skill 但里面全是对比表，说明它的**内容是 insight，需要补充操作流程才能成为 skill**。

## 修复方法

把 insight 升级为 skill 的关键：加上**可执行的步骤流程**。

例如：
- 原版：工具 A vs 工具 B 对比表 + 场景推荐 → 这是 insight
- 重写：Step 1 选工具 → Step 2 dry-run → Step 3 执行 → Step 4 校验 → 常见陷阱 → 这是 skill

对比表可以保留在 skill 内部（作为 Step 1 的决策依据），但不能是文档的全部内容。

## 反过来也成立

如果一份 insight 文档里全是操作步骤，它可能更适合标为 skill。类型和内容应该一致，否则检索时会找错位置。
