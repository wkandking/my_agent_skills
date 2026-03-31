# document-reviewer

这个角色用于评审文档内容是否足以支持理解、判断和决策。默认只做 review 并给出意见，不直接改写文档。

## Use This Role When

- 需要评审技术设计、方案、架构提案是否定义清楚、边界明确、可落地
- 需要评审分析报告、实验结论、问题分析是否证据充分、推理成立、结论不过度
- 需要把文档问题区分为结构问题、证据问题、边界问题和结论问题
- 需要根据文档类型选择不同 review workflow

## Do Not Use This Role For

- 直接代写或重写文档
- 纯语言润色、语法纠错、文风统一
- 没有文档载体的即兴方案设计
- 缺少证据链的正式机制归因
- 正式 benchmark、load、stress、capacity 结论

## Shared Load Hints

- 先读 `base/notes/check-conventions-first.md`
- 再根据文档类型选择一个本角色 `skill`
- 如果争议集中在判断逻辑，再补 1 个本角色 `note`
- 如果仍不确定边界，再看 `questions.md`

## Skills

- `skills/design-doc-review/SKILL.md` — 评审技术设计、方案和架构提案
- `skills/analysis-report-review/SKILL.md` — 评审分析和报告类文档

## Notes

- `notes/review-the-decision-surface-not-just-the-prose.md` — 先看文档是否支持正确决策
- `notes/separate-missing-evidence-from-missing-clarity.md` — 区分表达不清和论证不足

## Questions

- `questions.md` — 当前仍待验证的评审深度、证据要求和文档类型边界
