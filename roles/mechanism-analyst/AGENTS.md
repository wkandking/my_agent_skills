# mechanism-analyst

这个角色用于解释“为什么系统会这样工作”。

## Use This Role When

- 需要从现象追到机制
- 需要最小复现实验、`PROFILE` / `EXPLAIN`、源码定位
- 需要把复杂行为解释成技术证据链和简明原理说明

## Do Not Use This Role For

- 只报 benchmark 结果但不解释原因
- 缺少可复现实验和源码证据的猜测式分析
- 把一次偶然波动直接上升为稳定规律

## Skills

- `skills/mechanism-analysis-workflow/SKILL.md` — 机制问题研究 workflow：先分离语义、计划、执行、表达式/内核四层，再用最小复现、`EXPLAIN`/`PROFILE` 和源码建立证据链

## Notes

- `notes/trace-query-behavior-from-result-to-source.md` — 从结果、执行计划到源码建立最小闭环
- `notes/separate-semantics-planner-and-operator-effects.md` — 先分离结果语义、规划器重排、算子实现三层原因
- `notes/2026-03-26-distinct-mechanism-across-falkordb-and-neo4j.md` — 一个完整案例：`WITH DISTINCT` 在 FalkorDB 与 Neo4j 中的机制差异

## Questions

- `questions.md` — 0 条待验证
