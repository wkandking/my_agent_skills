---
kind: principle
description: "agent 工作中接触凭证时的安全原则：不提交、不硬编码、不打印"
triggers:
  - "凭证"
  - "密码"
  - "token"
  - "API key"
  - "安全"
---

# 凭证安全原则

## 背景

Agent 在工作过程中会接触各类凭证（API token、密码、SSH key 等）。一旦凭证被提交到 git 仓库，即使后续删除，也会永久留存在 git 历史中，造成泄漏。

## 内容

1. **禁止将凭证提交到仓库**：密码、token、API key、私钥等敏感信息不得出现在任何被 git 跟踪的文件中
2. **凭证从配置文件读取**：运行时从 `~/.config/` 下的配置文件或环境变量获取凭证，不要硬编码到脚本或文档中
3. **`.gitignore` 兜底**：确保 `config.toml`、`.env`、`.env.*` 等凭证文件已在 `.gitignore` 中排除
4. **提交前检查**：执行 `git diff --cached` 审查暂存内容，确认不包含凭证
5. **文档中使用占位符**：技能文档中引用凭证时使用 `<password>`、`$TOKEN` 等占位符，不得出现真实值

## 示例

正面：
```bash
# 从环境变量或配置文件读取
TOKEN=$(grep token ~/.config/my-tool/config.toml | cut -d'"' -f2)
curl -H "Authorization: Bearer $TOKEN" ...
```

反面：
```bash
# 硬编码明文密码
curl -u "user:actual-password-here" ...
```
