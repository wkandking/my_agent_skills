---
kind: insight
description: "同一查询在不同引擎上表现不一致时，先区分三层原因：结果语义、规划器重排、算子实现；不要把它们混成一个结论。"
triggers:
  - "跨引擎差异"
  - "multiplicity"
  - "路径条数"
  - "可达性"
  - "优化器重排"
  - "Distinct 算子"
source:
  - "roles/mechanism-analyst/insights/separate-semantics-planner-and-operator-effects.md"
---

# 先分离语义、规划器、算子三层原因

查询行为差异最常见的误判，是把三种不同层级的问题混成一个解释。

## 三层原因

第一层：结果语义

- 关注结果行数、集合语义、路径条数、`count(*)` 是否一致。

第二层：规划器重排

- 关注起始扫描点是否变化、是否新增 `Distinct` / `OrderedDistinct` / `Project`、前后执行路线是否改变。

第三层：算子实现

- 关注底层算子到底保留的是行流 multiplicity，还是只保留“是否可达”“是否命中”这类布尔语义。

## 使用方式

看到差异时，不要直接说“因为 DISTINCT”或“因为优化器”。

先问三次：

1. 结果到底哪里不一样？
2. 执行计划到底哪里变了？
3. 真正改变结果的，是计划重排，还是算子本身的实现语义？
