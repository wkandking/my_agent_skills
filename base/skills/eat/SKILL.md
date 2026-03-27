---
name: eat
description: Use when the user wants to sediment the current context, files, repositories, URLs, images, PDFs, or other sources into reusable knowledge, or explicitly triggers `/eat`.
---

# Eat

## Overview

This skill is for sedimenting the parts of the current context that are truly worth reusing over time.

The goal is not to save everything, but to:

- decide what is worth preserving
- decide whether it belongs in the shared layer or a role layer
- choose the right knowledge type
- produce reusable drafts or downstream handoff information

Before proposing anything, read:

- `base/notes/knowledge-sedimentation.md`: sedimentation boundaries, target types, and shared-vs-role judgment
- `references/knowledge-placement.md`: target root resolution, path mapping, and write placement rules
- `references/output-contract.md`: output formats for normal mode and maintenance mode

## Modes

- `/eat` or `/eat project`: the target root is the current project root
- `/eat home`: the target root is `$HOME/my_agent_skills`
- `/eat update`: reflect on `eat` using only the current conversation
- `/eat update all`: reflect on `eat` using the current conversation plus the `eat` maintenance assets currently on disk

`project` and `home` are reserved aliases. Arbitrary path arguments are not accepted.

## Core Rules

### 1. Propose first, write later

Whether in normal sedimentation mode or while maintaining `eat` itself:

- the first response must contain analysis and proposals only, with no file edits
- all writable candidate items must use stable numbering like `1. 2. 3.`
- writing happens only after explicit user confirmation
- the user may confirm everything or only a subset, such as `1 approve` or `1 3 approve`
- in normal mode, all user-visible proposal output defaults to Chinese, including titles, field labels, `Why Here`, `Risk`, explanatory text under `Draft`, and natural-language content shown inside draft previews
- persisted content written into the knowledge repository defaults to English only at the actual write stage unless the user explicitly requests another language
- if future persisted English content must be previewed before writing, label it explicitly as `落库草稿预览（默认英文）` instead of using it as the main proposal body

### 2. Prefer the best available sources

In normal mode, choose sources in this order:

1. sources explicitly named in the current user message
2. the most recent attachment group
3. the current conversation context

For mixed-source sets:

- process all readable sources when possible
- mark unreadable or unsupported sources as `skipped: <reason>`
- do not abandon the whole set just because one source failed

### 3. Do not store content that is not worth reusing

Whether something should be sedimented and what type it should become is governed by `base/notes/knowledge-sedimentation.md`.

### 4. Hand off `skill` items to `skill-creator-codex`

When a candidate item is classified as a `skill`:

- `eat` only handles classification, path recommendation, and handoff
- `eat` does not produce the final `SKILL.md` directly
- after user confirmation, switch to `skill-creator-codex`

## Decision Step

For each candidate item, make two decisions first:

1. whether it is worth sedimenting
2. if yes, what target and path it should use

Do not redefine the detailed criteria here:

- for target type and shared-vs-role scope, see `base/notes/knowledge-sedimentation.md`
- for target root and exact path mapping, see `references/knowledge-placement.md`

## Output

Both normal mode and maintenance mode must follow `references/output-contract.md`.

## Write Phase

After the user confirms, execute writes with these rules:

1. If the target file already exists, read it first
2. Prefer local append/merge over whole-file rewrites
3. Reuse the local tone and heading style of the target file
4. Merge clearly same-topic candidate items into one file
5. Skip content that duplicates existing stable rules, and explain why
6. Write only the items the user explicitly confirmed
7. If a confirmation cannot be mapped unambiguously to item numbers, restate the recognized set and wait for clarification
8. If the confirmed target is a `skill`, switch to `skill-creator-codex`
9. Unless the user explicitly requests another language, keep all user-visible proposal and confirmation communication in Chinese; switch to English by default only for content that is actually being persisted into repository files

For `eat` self-maintenance:

- treat the source skill under `$HOME/my_agent_skills` as the source of truth
- update the source skill first, then sync the installed copy
- verify that the source skill and installed copy are consistent after changes
- do not claim `eat` is fully updated before consistency has been checked
