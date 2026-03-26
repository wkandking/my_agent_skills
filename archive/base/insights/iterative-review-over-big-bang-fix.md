---
description: "跨层改动应逐层 review 多轮迭代，每轮发现的问题往往是前一轮修复引入的"
triggers:
  - "跨层 review"
  - "迭代修复"
  - "多轮 review"
---

# Insight: 跨层改动应逐层 review，多轮迭代是正常的

## 观察

在多层架构的改动中（如 Core → Binding → Wrapper → Types → Tests），一次性修完所有层再 review 容易遗漏问题。每轮 review 发现的问题往往是前一轮修复引入或暴露的。

## 泛化

跨层改动的修复应该：
- **每修一层后立即 review**，而非全部改完再 review
- **每轮 review 聚焦当前层的一致性**，不要试图同时验证所有层
- **接受多轮迭代是正常的**，不是效率低的表现

适用场景：
- API → Service → Repository → DB migration
- 前端组件 → API 调用 → 后端接口 → 数据模型
- 任何涉及 3 层以上的改动
