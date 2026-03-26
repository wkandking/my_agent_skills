# 2026-03-26 FalkorDB 与 Neo4j 中 `WITH DISTINCT` 的机制差异

日期: 2026-03-26

## Triggers

- "WITH DISTINCT"
- "multiplicity"
- "可达性"
- "OrderedDistinct"
- "Conditional Traverse"
- "GxB_ANY_PAIR_BOOL"

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

## 关键决策（含依据）

- 决策：不要把差异直接归因于 `WITH` 或 `DISTINCT` 语法。
  - 依据：先用最小数据集比较结果，再比较 `PROFILE`，最后读源码。

- 决策：把 FalkorDB 的差异定位为“未引用中间变量时，路径被压成 algebraic expression”。
  - 依据：`algebraic_expression_construction.c` 中，未被引用的中间 alias 不会强制拆分表达式。

- 决策：把 FalkorDB 的语义定位为“布尔可达性”，而不是“路径条数”。
  - 依据：`algebraic_expression_mul.c` 使用 `GxB_ANY_PAIR_BOOL` 进行矩阵乘法，保留的是是否存在命中，不累计路径条数。

## 结果

最终解释框架：

- Neo4j 更接近逐行保留 multiplicity 的执行方式。
- FalkorDB 在这类查询上会把未引用中间节点压入布尔矩阵表达式，结果更接近“是否可达”。
- 因此，两条 `Alice -> ... -> Post101` 路径在 Neo4j 中会保留成两行，在 FalkorDB 中可能被合并成一次命中。

## 提炼检查

- [x] Principle：已经可提炼为“从结果追到源码的最小闭环”
- [x] Insight：已经可提炼为“先分离语义、规划器、算子三层原因”
- [ ] Skill：暂不提炼，当前更像解释框架，不是固定操作流程
- [ ] Question：暂无
