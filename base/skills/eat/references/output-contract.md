# Output Contract

Use this contract whenever `eat` produces a proposal.

Template blocks below use English field names only to show structure. They are not a language requirement. Actual proposal language must follow the skill rules, which default user-visible proposal output to Chinese.

## Normal Mode

Start with the source set:

```md
## Source Set
- Target Root: `<exact path>`
- Source Mode: <explicit source | recent attachment group | current conversation>
- Processed Sources:
  - `<source>`: <processed | skipped: reason>
```

If this is `home` mode, also add:

```md
- Existing Shared Layer: `<root>/base`
- Existing Roles:
  - `<role>`
```

Then give the shortest useful summary for each source:

```md
## Source Summary: <source label>
- Source Type: <file | repo | image | pdf | document | url | pasted text | conversation>
- Key Takeaway: <1-3 sentence summary>
```

Every **writable candidate item** uses the same minimal structure:

```md
### 1. Candidate Knowledge: <short statement>
- Scope: <shared | role-specific:<role>>
- Knowledge Type: <AGENTS rule | note | skill | question>
- Recommended Path: `<exact path>`
- Why Here: <1-3 sentence explanation>
```

Additional fields appear only when needed:

- `note`: add `Note Kind`
- `AGENTS rule` / `note` / `question`: add `Draft`
- `skill`: add `Skill Handoff`
- if there is risk or unclear boundary: add `Risk`

Language rule:

- all user-visible proposal content defaults to Chinese, including section titles, field labels, `Why Here`, `Risk`, explanatory text under `Draft`, and natural-language content shown inside proposal previews
- template English indicates field structure only, not output language
- content defaults to English only when it is actually being persisted into repository files
- if future persisted English content must be previewed before writing, label it explicitly as `落库草稿预览（默认英文）` and do not present that English text as the main proposal body
- if the user explicitly requests another language, follow the user's request

`Skill Handoff` uses this minimal field set:

```md
- Skill Handoff:
  - Creator: `skill-creator-codex`
  - Goal: <what the skill should accomplish>
  - Trigger: <when it should trigger>
  - Target Path: `<path>`
  - Expected Output: <output shape>
  - Evidence:
    - <source or conversation evidence>
  - Open Questions:
    - <question | None>
```

Items that should not be stored are not numbered:

```md
### Candidate Knowledge: <short statement>
- Decision: Do Not Store
- Reason: <reason>
```

End with:

```md
## Application Summary
- Files To Create:
  - `<path>`
- Files To Update:
  - `<path>`
- Confirmation Required: `No files will be changed until the user explicitly confirms all numbered items or a selected subset.`
```

If there are writable candidate items, add one more line at the end:

```md
Confirmation examples: `approve all`, `approve 1`, `approve 1 3`
```

## Maintenance Mode

`/eat update` uses only the current conversation as evidence.
`/eat update all` uses the current conversation plus the `eat` maintenance assets currently on disk.

Maintenance mode always uses this format:

```md
## Failure Summary
- Issue: <what `eat` got wrong>
- Evidence Scope: <current context only | current context + existing eat assets>

## Root Cause
- <1-3 sentence explanation>

## Rule Changes
1. <proposed change>

## Files To Update
- `<path>`

## Patch Summary
- <what will be changed>
```

If there are multiple independent applicable changes, they must also be numbered so the user can confirm only a subset.
