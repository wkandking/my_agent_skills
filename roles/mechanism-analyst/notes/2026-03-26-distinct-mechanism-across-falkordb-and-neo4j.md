---
kind: experience
description: "一个完整案例：`WITH DISTINCT` 在 FalkorDB 与 Neo4j 中为什么会表现出不同的路径条数与可达性语义。"
triggers:
  - "WITH DISTINCT"
  - "multiplicity"
  - "可达性"
  - "OrderedDistinct"
  - "Conditional Traverse"
  - "GxB_ANY_PAIR_BOOL"
---

# 2026-03-26 FalkorDB 与 Neo4j 中 `WITH DISTINCT` 的机制差异

日期: 2026-03-26

## 背景

目标是解释同一类查询在 FalkorDB 和 Neo4j 中为什么会产生不同结果。

核心例子：

```cypher
MATCH (u)-[:FOLLOWS]->(f)-[:LIKES]->(p)
WITH p
MATCH (p)-[:TAGGED_AS]->(t)
RETURN count(*)
```

## 证据与现象

Neo4j 上：

- `WITH p` 会保留重复的 `p` 行。
- 因此前半段 2 行 `p`，后半段每行再扩成 2 个 tag，最终 `count(*) = 4`。

FalkorDB 上：

- 同一数据下，`WITH p` 也只得到 2 行最终结果，`count(*) = 2`。
- `PROFILE` 显示前半段被压成了 `Conditional Traverse | (u)->(p:Post)`。

## 结果

最终解释框架：

- Neo4j 更接近逐行保留 multiplicity 的执行方式。
- FalkorDB 在这类查询上会把未引用中间节点压入布尔矩阵表达式，结果更接近“是否可达”。
- 因此，两条 `Alice -> ... -> Post101` 路径在 Neo4j 中会保留成两行，在 FalkorDB 中可能被合并成一次命中。
