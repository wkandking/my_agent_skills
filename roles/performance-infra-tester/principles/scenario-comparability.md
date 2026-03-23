# Scenario Comparability Rules

- Do not collapse benchmark scenarios with different semantics into a single "overall winner" conclusion.
- Query semantic changes such as `no-distinct` versus stepwise `DISTINCT` should be treated as primary explanatory variables, not minor variants.
- Deployment variables such as `numa0` should be analyzed separately from database engine variables.
- When writing conclusions, give each scenario its own judgment first, then summarize the shared patterns across scenarios.
