---
description: 发布/维护 installable skill（installable-skills/{name}）时的结构与引用卫生：自包含、禁止引用 skill 目录外路径、校验 front matter/YAML、以及发布口径（单文件 vs references/）取舍。触发条件：新增/更新 installable-skills、技能发布、安装后坏链接排查。
triggers:
  - "installable-skills"
  - "skill 发布"
  - "坏链接"
  - "引用闭包"
  - "npx skills add"
  - "quick_validate"
---

# Installable Skill Hygiene（发布质量与引用卫生）

目标：让 `installable-skills/<skill-name>/` **安装后仍然可用**（不依赖原仓库布局/当前工作目录），并且可维护（变更可 review、可回滚）。

## 核心约束（必须）

1. **自包含**：skill 安装后只应依赖 `installable-skills/<skill-name>/` 目录内的文件。
2. **禁止"逃逸路径"**：`SKILL.md`（以及被它引导打开的文件）不得引用 `../` 等跳出 skill 根目录的路径；不得要求读 `base/`、`roles/`、仓库根 `README.md` 这类"在原仓库里存在、安装后可能不存在"的路径。
3. **入口可读**：`SKILL.md` 里要能让读者在不打开别的文件的情况下理解"要做什么 + 怎么做 + 何时触发"。

## 发布口径（两种都允许，选其一）

### A）单文件口径（最稳）

把必要内容尽量内嵌在 `SKILL.md`。适用于：
- skill 短小、步骤清晰
- 不希望出现任何跨文件引用（包括 `references/...`）

代价：`SKILL.md` 会变长，维护时更容易出现"改一点动全篇"。

### B）skill 内部引用口径（更可维护）

允许使用 **skill 目录内部** 的相对引用，例如：
- `references/...`
- `scripts/...`
- `assets/...`

适用于：
- 需要附带 API 参考/长文档/示例配置
- 需要脚本提高确定性

注意：这里的"相对路径"只允许 **相对于 skill 根目录** 的内部路径；不要出现任何 `../` 逃逸。

## 发布前检查（推荐顺序）

### 1）front matter 基本校验（YAML）

如果本机有 skill-creator 的 `quick_validate.py`，优先跑：

```bash
python <path-to-skill-creator>/scripts/quick_validate.py installable-skills/<skill-name>
```

### 2）引用闭包扫描（禁止逃逸 + 禁止仓库根依赖）

在 skill 目录下扫一遍可疑引用（按需加关键字）：

```bash
rg -n "(^|\\s)(\\.\\./|/base/|\\broles/|\\binstallable-skills/\\b|README\\.md\\b|AGENTS\\.md\\b)" -S installable-skills/<skill-name>
```

解释：
- `../`：大概率是"逃逸路径"
- `base/`、`roles/`：大概率是"依赖原仓库布局"
- `installable-skills/`：skill 内不应再写全局路径（安装后不稳定）
- `README.md`、`AGENTS.md`：常见误指向仓库根文件（除非它们位于 skill 目录内）

### 3）安装体验抽查（可选）

在仓库的 `installable-skills/` 目录下执行：

```bash
npx skills add . --skill='<skill-name>' -g -y
```

## Escalate to experience if

- 安装后出现坏链接/缺文件，但在原仓库里"看起来没问题"
- 需要同时维护 internal/public 两个仓库的 installable skills，且希望 diff 可控
- 文档附录对比出现"附录 diff 远大于正文"的异常现象
