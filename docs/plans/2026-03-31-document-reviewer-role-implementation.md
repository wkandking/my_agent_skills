# Document Reviewer Role Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a new `document-reviewer` role that reviews design docs and analysis/report docs by routing into specialized skills while keeping the role itself review-only.

**Architecture:** Extend the repository's active role list to include `document-reviewer`, create one lightweight role entrypoint plus two review skills and two decision-framework notes, then update repository metadata and validation so the new role is treated as a first-class active role. Keep the initial scope intentionally small and Chinese-first.

**Tech Stack:** Markdown, Git worktree workflow, Python 3 validator, ripgrep

---

## Preconditions

- Work only in a dedicated worktree created from `origin/main`
- Do not edit the main workspace
- Keep the initial role scope limited to review-only behavior
- Default all new role-facing text to Chinese unless a file already establishes English conventions
- Use `python3` instead of `python`

## Repository-Wide Verification Contract

After each task, run the smallest relevant check. Before the final commit, this command must pass:

```bash
python3 tools/validate_knowledge_repo.py
```

Support checks:

```bash
rg -n "document-reviewer" AGENTS.md README.md tools/validate_knowledge_repo.py roles/document-reviewer
find roles/document-reviewer -maxdepth 3 -type f | sort
```

### Task 1: Extend the Repository Contract to Expect the New Role

**Files:**
- Modify: `tools/validate_knowledge_repo.py`
- Modify: `README.md`

**Step 1: Add the new active role to the validator**

Edit `tools/validate_knowledge_repo.py` so `ACTIVE_ROLES` becomes:

```python
ACTIVE_ROLES = [
    "document-reviewer",
    "generalist-engineer",
    "mechanism-analyst",
    "performance-infra-tester",
]
```

Do not change any other validation logic in this step.

**Step 2: Run the validator to confirm the repo now fails for the missing role**

Run:

```bash
python3 tools/validate_knowledge_repo.py
```

Expected:
- FAIL with an active-role mismatch or missing required role path for `roles/document-reviewer`

**Step 3: Update the README role list and structure overview**

Edit `README.md` so it:

- adds `document-reviewer` under `## Active Roles`
- adds `roles/document-reviewer/` to the structure example
- describes the role as reviewing design docs and analysis/report docs

Use wording close to:

```md
- `document-reviewer`: reviews design docs and analysis/report docs for scope, evidence, and decision quality
```

**Step 4: Commit the repository contract change**

```bash
git add tools/validate_knowledge_repo.py README.md
git commit -m "docs: reserve active role slot for document reviewer"
```

### Task 2: Create the Role Skeleton and Entry Point

**Files:**
- Create: `roles/document-reviewer/AGENTS.md`
- Create: `roles/document-reviewer/questions.md`
- Create: `roles/document-reviewer/skills/design-doc-review/SKILL.md`
- Create: `roles/document-reviewer/skills/analysis-report-review/SKILL.md`
- Create: `roles/document-reviewer/notes/review-the-decision-surface-not-just-the-prose.md`
- Create: `roles/document-reviewer/notes/separate-missing-evidence-from-missing-clarity.md`

**Step 1: Create the role directories**

Run:

```bash
mkdir -p roles/document-reviewer/skills/design-doc-review
mkdir -p roles/document-reviewer/skills/analysis-report-review
mkdir -p roles/document-reviewer/notes
```

Expected:
- the `roles/document-reviewer/` tree exists with `skills/` and `notes/`

**Step 2: Write `roles/document-reviewer/AGENTS.md`**

Use this structure:

```md
# document-reviewer

这个角色用于评审文档内容是否足以支持理解、判断和决策。默认只做 review 并给出意见，不直接改写文档。

## Use This Role When

- 需要评审技术设计、方案、架构提案是否定义清楚、边界明确、可落地
- 需要评审分析报告、实验结论、问题分析是否证据充分、推理成立、结论不过度
- 需要把文档问题区分为结构问题、证据问题、边界问题和结论问题
- 需要根据文档类型选择不同 review workflow

## Do Not Use This Role For

- 直接代写或重写文档
- 纯语言润色、语法纠错、文风统一
- 没有文档载体的即兴方案设计
- 缺少证据链的正式机制归因
- 正式 benchmark、load、stress、capacity 结论

## Shared Load Hints

- 先读 `base/notes/check-conventions-first.md`
- 再根据文档类型选择一个本角色 `skill`
- 如果争议集中在判断逻辑，再补 1 个本角色 `note`
- 如果仍不确定边界，再看 `questions.md`

## Skills

- `skills/design-doc-review/SKILL.md` — 评审技术设计、方案和架构提案
- `skills/analysis-report-review/SKILL.md` — 评审分析和报告类文档

## Notes

- `notes/review-the-decision-surface-not-just-the-prose.md` — 先看文档是否支持正确决策
- `notes/separate-missing-evidence-from-missing-clarity.md` — 区分表达不清和论证不足

## Questions

- `questions.md` — 当前仍待验证的评审深度、证据要求和文档类型边界
```

**Step 3: Write `roles/document-reviewer/questions.md`**

Use:

```md
# Questions

- [ ] 技术设计文档 review 默认是否必须覆盖测试、发布和回滚路径？
- [ ] 分析报告 review 默认是否要求关键原始证据可复查？
- [ ] 是否需要在未来把对外说明文档 / 教程文档拆成独立 skill？
```

**Step 4: Run the validator to confirm the next missing pieces are skills or notes content, not the role skeleton**

Run:

```bash
python3 tools/validate_knowledge_repo.py
```

Expected:
- FAIL on missing referenced files or note frontmatter, which means the role skeleton is now visible to the validator

**Step 5: Commit the role skeleton**

```bash
git add roles/document-reviewer
git commit -m "docs: add document reviewer role skeleton"
```

### Task 3: Implement the Design-Doc Review Skill

**Files:**
- Modify: `roles/document-reviewer/skills/design-doc-review/SKILL.md`

**Step 1: Write the skill frontmatter**

Use:

```yaml
---
name: design-doc-review
description: Use when reviewing technical design docs, proposals, or architecture notes for scope, assumptions, feasibility, risks, and validation paths.
---
```

**Step 2: Write the skill body with a stable review workflow**

Required sections:

- `# Design Doc Review`
- `## Goal`
- `## Use This Skill When`
- `## Core Review Dimensions`
- `## Workflow`
- `## Output Shape`

The workflow should explicitly do these things in order:

1. restate the document's target problem
2. extract scope, non-goals, assumptions, and constraints
3. check whether the proposal actually answers the problem
4. inspect implementation, risk, rollout, and rollback coverage
5. separate blocking findings from suggestions

Use Chinese in the prose, but keep section headings and the output labels stable enough to reuse.

**Step 3: Add the expected output template**

Include an output block shaped like:

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

**Step 4: Run a reference check**

Run:

```bash
rg -n "check-conventions-first|Summary|Findings|Open Questions|What Looks Solid" roles/document-reviewer/skills/design-doc-review/SKILL.md
```

Expected:
- all core sections and output labels are present

**Step 5: Commit the design-doc review skill**

```bash
git add roles/document-reviewer/skills/design-doc-review/SKILL.md
git commit -m "docs: add design doc review skill"
```

### Task 4: Implement the Analysis-Report Review Skill

**Files:**
- Modify: `roles/document-reviewer/skills/analysis-report-review/SKILL.md`

**Step 1: Write the skill frontmatter**

Use:

```yaml
---
name: analysis-report-review
description: Use when reviewing analysis docs, experiment reports, or investigation summaries for evidence quality, comparability, inference quality, and conclusion boundaries.
---
```

**Step 2: Write the skill body with a stable review workflow**

Required sections:

- `# Analysis Report Review`
- `## Goal`
- `## Use This Skill When`
- `## Core Review Dimensions`
- `## Workflow`
- `## Output Shape`

The workflow should explicitly do these things in order:

1. restate the core question the report is trying to answer
2. list the report's observations, explanations, conclusions, and recommendations separately
3. check sample comparability and evidence completeness
4. flag causal leaps, over-generalization, and missing boundaries
5. distinguish high-confidence findings from assumptions to verify

**Step 3: Add the expected output template**

Include an output block shaped like:

```md
Summary
- ...

Findings
- P1: ...

Assumptions To Verify
- ...

Confidence Notes
- ...
```

**Step 4: Run a reference check**

Run:

```bash
rg -n "Summary|Findings|Assumptions To Verify|Confidence Notes" roles/document-reviewer/skills/analysis-report-review/SKILL.md
```

Expected:
- all core output labels are present

**Step 5: Commit the analysis-report review skill**

```bash
git add roles/document-reviewer/skills/analysis-report-review/SKILL.md
git commit -m "docs: add analysis report review skill"
```

### Task 5: Add the Initial Decision-Framework Notes

**Files:**
- Modify: `roles/document-reviewer/notes/review-the-decision-surface-not-just-the-prose.md`
- Modify: `roles/document-reviewer/notes/separate-missing-evidence-from-missing-clarity.md`

**Step 1: Write `review-the-decision-surface-not-just-the-prose.md` with valid frontmatter**

Use frontmatter shaped like:

```yaml
---
kind: principle
description: "Review documents for whether they support the reader's decision, not just whether the prose sounds smooth."
triggers:
  - "document review"
  - "design doc"
  - "report review"
  - "decision quality"
---
```

Body requirements:

- explain that review targets decision quality, not surface polish
- include examples of missing decision inputs, such as constraints, risks, or boundary conditions
- keep the prose in Chinese

**Step 2: Write `separate-missing-evidence-from-missing-clarity.md` with valid frontmatter**

Use frontmatter shaped like:

```yaml
---
kind: insight
description: "Separate unclear writing from unsupported claims so review feedback points to the real problem."
triggers:
  - "evidence"
  - "clarity"
  - "analysis report"
  - "review feedback"
---
```

Body requirements:

- explain how to tell structure problems apart from evidence problems
- include examples of the wrong feedback loop created when they are mixed together
- keep the prose in Chinese

**Step 3: Run the validator to confirm note frontmatter and references are correct**

Run:

```bash
python3 tools/validate_knowledge_repo.py
```

Expected:
- PASS, or a final failure that points only to a remaining broken reference in the new role files

**Step 4: Commit the notes**

```bash
git add roles/document-reviewer/notes
git commit -m "docs: add document reviewer decision notes"
```

### Task 6: Final Consistency Pass

**Files:**
- Modify: `AGENTS.md`
- Modify: `README.md`
- Modify: `roles/document-reviewer/AGENTS.md`
- Modify: `tools/validate_knowledge_repo.py`

**Step 1: Update the root structure example if it still omits the new active role**

Edit `AGENTS.md` only if needed so the repository structure example shows `document-reviewer/` alongside the other active roles.

**Step 2: Run the full repository validation**

Run:

```bash
python3 tools/validate_knowledge_repo.py
find roles/document-reviewer -maxdepth 3 -type f | sort
git diff --stat
```

Expected:
- validator PASS
- role tree shows exactly the intended files
- diff is limited to the new role and metadata updates

**Step 3: Stage and commit the final integration**

```bash
git add AGENTS.md README.md tools/validate_knowledge_repo.py roles/document-reviewer
git commit -m "feat: add document reviewer role"
```

## Suggested Execution Order

If implementing in one pass, keep this order:

1. Task 1
2. Task 2
3. Task 3
4. Task 4
5. Task 5
6. Task 6

That order keeps the validator acting as the main guardrail and avoids writing role content that the repository still does not formally recognize.
