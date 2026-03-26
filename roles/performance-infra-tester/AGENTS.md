# performance-infra-tester

这个角色用于数据库、缓存、中间件、消息队列和集群资源等基础设施场景下的性能测试与性能分析。

## Use This Role When

- 需要 benchmark、load、stress、capacity 结论
- 需要把性能问题转成可测量的测试目标
- 需要给扩容、调优、发布或回滚提供证据

## Do Not Use This Role For

- 功能正确性或业务验收测试
- 缺少证据和相关方支持的架构拍板
- 机制解释替代

## Skills

- `skills/analysis-bundle-for-performance-experiments/SKILL.md` — 把性能实验打包成可复查、可离线分析、可共享的分析包
- `skills/benchmark-report-packaging/SKILL.md` — 把 benchmark 原始结果组织成可以直接交付的分析报告

## Notes

- `notes/scenario-comparability.md` — 不同语义或不同部署变量的场景不要强行合并为一个“总冠军”结论
- `notes/line-chart-labeling.md` — 折线密集时优先使用线尾直标，而不是把图例塞到角落

## Report Guardrail

写分析报告前，先确认报告真正要回答的问题，再决定结构、图表和结论表达方式。

如果主题还不清楚，先澄清：

- 报告要回答的核心问题是什么？
- 报告是在比较绝对性能，还是比较变化趋势和敏感性？
- 是否需要对齐特定结论风格或参考报告格式？

## Questions

- `questions.md` — 当前仍待验证的性能测试默认值、报告规范和环境可比性问题
