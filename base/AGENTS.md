# base — 通用知识

这里存放所有角色共享的知识。角色私有知识见 `roles/<role>/`。

## 目录说明

| 目录/文件 | 内容 |
|---|---|
| `experience/` | 不绑定具体角色的经验素材和复盘 |
| `principles/` | 通用原则和稳定约束 |
| `skills/` | 通用技能，每个技能目录主入口为 `SKILL.md` |
| `insights/` | 跨角色可复用的规律性认知 |
| `knowledge-sedimentation.md` | 经验沉淀规范 |

## 当前共享技能

- `skills/eat/`：把对话、文档、仓库、图片、PDF 等来源转成可复用知识，并给出落库位置建议
- `skills/skill-creator/`：创建、迭代、评测和优化通用技能
- `skills/skill-creator-codex/`：为 Codex 创建、迁移、校验和安装技能

各子目录的详细索引见对应的 `AGENTS.md` 或 `SKILL.md`。目录级入口统一用 `AGENTS.md`，技能主入口统一用 `SKILL.md`。

## 修改规范

- 对 `base/` 的修改需要通过 review
- 新增文档应遵循现有格式
- 从角色私有知识提升到 `base/` 时，应去除角色特定部分，保留可跨角色复用的内容
