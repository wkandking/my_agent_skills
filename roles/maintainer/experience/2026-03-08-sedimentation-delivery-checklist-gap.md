# 知识沉淀交付时遗漏联动更新

日期: 2026-03-08

## Triggers
- "AGENTS.md 索引" "front matter" "triggers" "交叉引用" "自查"

## 背景

在 `add-maintainer-role` 分支提交 GitHub Actions skill 和 experience 后，self-review 发现 4 个问题，全部属于"内容写完了但联动更新没做"。

## 证据与现象

| 问题 | 类别 | 原因 |
|------|------|------|
| AGENTS.md 索引缺 github-actions skill 和 experience 条目 | 联动遗漏 | 新建文件后没回到索引页更新 |
| github-actions/SKILL.md 和 installable-skill-hygiene/SKILL.md 都缺 `triggers` 字段 | 格式不合规 | 抄了已有文件的格式，但已有文件本身就缺 triggers |
| execution experience 中 plan 引用出现两次（相对链接 + 完整路径） | 冗余 | 分两步加引用，没回读整体 |
| SKILL.md 第 7 条陷阱自相矛盾（"只重跑 failure" + "cancelled 也会被重跑"） | 表述错误 | 脑中同时想着预期行为和实际行为，混在一句话里 |

## 关键决策

- **决策**：将"联动更新"补入 `base/knowledge-sedimentation.md` 的实操 Checklist，而不是新建独立 principle
  - 依据：这不是新主题，是已有 checklist 的覆盖盲区；加一条比新建文件更易被加载和执行

## 结果

- 修复 commit: `ec1f16a`
- 沉淀：更新 `base/knowledge-sedimentation.md` 实操 Checklist，增加"联动更新"条目

## 可复用模式

1. **不要只参考已有文件格式——回读规范文档确认必填字段**。已有文件可能本身不合规，复制格式等于复制缺陷。
2. **改完后通读整个改动区域**，不要逐块修改后直接提交。交叉引用的冗余和表述的矛盾只有在整体回看时才能发现。
3. **描述反直觉行为时，明确区分"名字暗示 X"和"实际是 Y"**，不要在同一句里放两个相反的陈述。
