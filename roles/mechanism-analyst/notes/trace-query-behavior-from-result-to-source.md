---
kind: principle
description: "查询或执行器行为差异排查时，先用最小复现实验钉住结果，再依次核对 PROFILE 与源码，避免跳步猜测。"
triggers:
  - "源码追因"
  - "执行计划差异"
  - "为什么这样工作"
  - "结果和预期不一致"
  - "数据库原理分析"
source:
  - "roles/mechanism-analyst/principles/trace-query-behavior-from-result-to-source.md"
---

# 从结果追到源码的最小闭环

解释系统行为时，先建立最小证据链，再下结论。

## 规则

1. 先用最小数据集和最小查询稳定复现现象。
2. 先比较结果层差异，例如行数、`count(*)`、是否保留 multiplicity。
3. 再比较 `PROFILE` 或 `EXPLAIN`，确认计划是否重排、是否新增算子。
4. 最后再读源码，确认差异发生在规划阶段、算子阶段，还是数据结构语义阶段。
5. 每一层只输出该层证据真正支持的结论，不用源码去猜结果，也不用结果去倒推未验证的实现细节。

## 不要这样做

- 只看源码，不先跑最小实验。
- 只看结果，不核对执行计划。
- 看到 `Distinct`、`Project`、`Conditional Traverse` 等算子名就直接推断全部语义。
- 把单次性能波动当成稳定机制。
