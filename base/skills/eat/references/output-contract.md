# 输出格式合同

当 `eat` 产出提案时，统一使用本合同。

## 普通模式

先输出来源集合：

```md
## Source Set
- Target Root: `<exact path>`
- Source Mode: <explicit source | recent attachment group | current conversation>
- Processed Sources:
  - `<source>`: <processed | skipped: reason>
```

如果是 `home` 模式，再补：

```md
- Existing Shared Layer: `<root>/base`
- Existing Roles:
  - `<role>`
```

然后每个来源只给最短总结：

```md
## 来源总结：<source label>
- Source Type: <file | repo | image | pdf | document | url | pasted text | conversation>
- Key Takeaway: <1-3 句总结>
```

每个**可写入候选项**都用同一最小结构：

```md
### 1. 候选知识：<short statement>
- Scope: <shared | role-specific:<role>>
- Knowledge Type: <AGENTS rule | note | skill | question>
- Recommended Path: `<exact path>`
- Why Here: <1-3 句说明>
```

补充字段只在需要时出现：

- `note`：再加 `Note Kind`
- `AGENTS rule` / `note` / `question`：再加 `Draft`
- `skill`：再加 `Skill Handoff`
- 如有风险或边界不清：再加 `Risk`

`Skill Handoff` 使用最小字段集：

```md
- Skill Handoff:
  - Creator: `skill-creator-codex`
  - Goal: <skill 应完成什么>
  - Trigger: <何时触发>
  - Target Path: `<path>`
  - Expected Output: <结果形态>
  - Evidence:
    - <source or conversation evidence>
  - Open Questions:
    - <question | None>
```

不应保存的项不编号：

```md
### 候选知识：<short statement>
- Decision: Do Not Store
- Reason: <原因>
```

最后补：

```md
## 应用摘要
- Files To Create:
  - `<path>`
- Files To Update:
  - `<path>`
- Confirmation Required: `No files will be changed until the user explicitly confirms all numbered items or a selected subset.`
```

如果存在可写入候选项，最后再补一行：

```md
可确认方式示例：`全部同意`、`1 同意`、`1 3 同意`
```

## 维护模式

`/eat update` 只使用当前会话作为证据来源。  
`/eat update all` 使用当前会话 + 当前磁盘上的 `eat` 维护资产。

维护模式统一输出：

```md
## 失败摘要
- Issue: <eat 做错了什么>
- Evidence Scope: <current context only | current context + existing eat assets>

## 根因
- <1-3 句说明>

## 规则变更
1. <拟议变更>

## 待更新文件
- `<path>`

## 补丁摘要
- <准备怎么改>
```

如果存在多个独立可应用的变更项，也必须编号，并允许用户只确认其中一部分。
