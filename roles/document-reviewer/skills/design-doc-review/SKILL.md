---
name: design-doc-review
description: Use when reviewing technical design docs, proposals, or architecture notes for scope, assumptions, feasibility, risks, and validation paths.
---

# Design Doc Review

## Goal

评审技术设计文档是否足以支持实现决策，而不是只判断文字是否通顺。

## Use This Skill When

- 评审技术设计、方案、架构提案、ADR 风格文档

## Core Review Dimensions

- 问题定义是否清楚
- 范围与非目标是否明确
- 约束、依赖、假设是否写清
- 方案是否真正回应问题，而不是绕开问题
- 是否覆盖主要失败模式和边界场景
- 是否给出验证、发布、回滚路径

## Workflow

1. 重述文档要解决的核心问题
2. 提取范围、非目标、假设和约束
3. 检查方案是否真正回答了问题
4. 检查实现、风险、发布和回滚覆盖是否完整
5. 将阻塞性问题和建议性问题分开

## Output Shape

```md
Summary
- ...

Findings
- P1: ...

Open Questions
- ...

What Looks Solid
- ...
```
