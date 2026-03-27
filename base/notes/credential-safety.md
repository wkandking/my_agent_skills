---
kind: principle
description: "Security rules for handling credentials during agent work: do not commit them, hardcode them, or print them."
triggers:
  - "credentials"
  - "password"
  - "token"
  - "API key"
  - "security"
---

# Credential Safety

## Background

Agents may come into contact with many kinds of credentials during work, such as API tokens, passwords, and SSH keys. Once a credential is committed to a git repository, it remains in git history even if later deleted, creating a lasting leak.

## Rules

1. **Do not commit credentials to the repository**: passwords, tokens, API keys, private keys, and similar secrets must not appear in any git-tracked file
2. **Read credentials from config files or environment variables**: load them at runtime from files under `~/.config/` or from environment variables; do not hardcode them into scripts or docs
3. **Use `.gitignore` as a safety net**: make sure files such as `config.toml`, `.env`, and `.env.*` are excluded in `.gitignore`
4. **Check before committing**: run `git diff --cached` to review staged content and verify that no credentials are included
5. **Use placeholders in docs**: when documentation refers to credentials, use placeholders such as `<password>` or `$TOKEN`, never real values

## Examples

Good:
```bash
# Read from an environment variable or config file
TOKEN=$(grep token ~/.config/my-tool/config.toml | cut -d'"' -f2)
curl -H "Authorization: Bearer $TOKEN" ...
```

Bad:
```bash
# Hardcoded plaintext password
curl -u "user:actual-password-here" ...
```
