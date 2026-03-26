# Lightweight Knowledge Repo Restructure Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Reduce the repository to a smaller, role-preserving knowledge system with stable entrypoints, a unified `notes/` model, and a minimal validation harness.

**Architecture:** Keep the `base/` vs `roles/` split, but collapse `principles/`, `insights/`, and `experience/` into a single `notes/` directory keyed by frontmatter `kind`. Replace low-value governance sprawl with shorter root entrypoints and one repository validator script. Archive low-frequency roles and oversized self-maintenance assets instead of deleting them.

**Tech Stack:** Markdown, Git moves, Python 3 validation script, YAML frontmatter, ripgrep

---

## Preconditions

- Work only in a dedicated worktree created from `origin/main`
- Do not edit the main workspace
- Treat the current `roles/mechanism-analyst/` changes in the main workspace as unrelated user work; do not touch or revert them
- Use `git mv` for file moves so history remains traceable
- Use `python3` instead of `python`

## Target Structure

```text
AGENTS.md
README.md
base/
  AGENTS.md
  skills/
    eat/
    skill-creator-codex/
  notes/
roles/
  generalist-engineer/
    AGENTS.md
    skills/
    notes/
    questions.md
  mechanism-analyst/
    AGENTS.md
    skills/
    notes/
    questions.md
  performance-infra-tester/
    AGENTS.md
    skills/
    notes/
    questions.md
tools/
  validate_knowledge_repo.py
archive/
```

## Repository-Wide Verification Contract

Every implementation task should keep this command green or make it fail for the intended next missing step only:

```bash
python3 tools/validate_knowledge_repo.py
```

The validator should check at minimum:

- root `README.md` role list matches the actual active role directories
- every active role has `AGENTS.md` and `questions.md`
- every `notes/*.md` file has frontmatter keys `kind`, `description`, and `triggers`
- every active `AGENTS.md` references only files that exist
- archived files are not referenced from active entrypoints

### Task 1: Create the New Skeleton and Validator Harness

**Files:**
- Create: `tools/validate_knowledge_repo.py`
- Create: `archive/.gitkeep`
- Create: `base/notes/.gitkeep`
- Create: `roles/generalist-engineer/AGENTS.md`
- Create: `roles/generalist-engineer/questions.md`
- Create: `roles/generalist-engineer/skills/.gitkeep`
- Create: `roles/generalist-engineer/notes/.gitkeep`
- Modify: `.gitignore`

**Step 1: Add any missing ignored directories**

Run:

```bash
rg -n "archive|docs/plans" .gitignore
```

Expected:
- `.claude/worktrees/` is already ignored
- add ignore entries only if the new structure introduces generated or throwaway paths that should stay untracked

**Step 2: Write the failing validator skeleton**

Create `tools/validate_knowledge_repo.py` with a CLI that exits non-zero while the repo is still in the old layout:

```python
#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_ROLES = [
    "generalist-engineer",
    "mechanism-analyst",
    "performance-infra-tester",
]

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)

def main() -> None:
    for role in ACTIVE_ROLES:
        role_dir = ROOT / "roles" / role
        if not role_dir.exists():
            fail(f"missing role directory: {role_dir}")
    print("validator placeholder")

if __name__ == "__main__":
    main()
```

**Step 3: Run validator to confirm it fails for the right reason**

Run:

```bash
python3 tools/validate_knowledge_repo.py
```

Expected:
- FAIL on missing `roles/generalist-engineer/`

**Step 4: Create the new directories and placeholder files**

Run:

```bash
mkdir -p archive base/notes roles/generalist-engineer/{skills,notes}
touch archive/.gitkeep base/notes/.gitkeep roles/generalist-engineer/skills/.gitkeep roles/generalist-engineer/notes/.gitkeep
printf '%s\n' '# generalist-engineer' '' 'TODO' > roles/generalist-engineer/AGENTS.md
printf '%s\n' '# Questions' > roles/generalist-engineer/questions.md
```

**Step 5: Commit**

```bash
git add .gitignore tools/validate_knowledge_repo.py archive/.gitkeep base/notes/.gitkeep roles/generalist-engineer
git commit -m "chore: add lightweight repo skeleton and validator scaffold"
```

### Task 2: Rewrite the Root Entry Points

**Files:**
- Modify: `AGENTS.md`
- Modify: `README.md`

**Step 1: Replace the current root `AGENTS.md` with a short entrypoint**

Required content:

```md
# Agent Knowledge Repo

This repository stores reusable role knowledge and shared skills for coding agents.

## Active Roles
- `generalist-engineer`
- `mechanism-analyst`
- `performance-infra-tester`

## Load Rule
1. Read this file
2. Read the relevant role `AGENTS.md`
3. Read one relevant `skill` or `note`
4. Read `questions.md` or one extra `note` only if needed

## Knowledge Model
- `skills/`: executable workflows
- `notes/`: rules, decision heuristics, and historical cases
- `questions.md`: known unknowns

## Collaboration
- Any write must happen in a worktree
- Do not develop in the main workspace
- Important changes go through PR review
```

**Step 2: Rewrite `README.md` to match the new model**

Required changes:
- describe only the active roles
- explain `skills/`, `notes/`, and `questions.md`
- remove references to `principles/`, `insights/`, and `experience/` as first-class top-level buckets
- remove references to archived roles

**Step 3: Run validator and basic grep checks**

Run:

```bash
python3 tools/validate_knowledge_repo.py || true
rg -n "cli-tool-dev|maintainer|principles/|insights/|experience/" AGENTS.md README.md
```

Expected:
- validator may still fail on later tasks
- root docs should no longer claim old active roles or old knowledge buckets

**Step 4: Commit**

```bash
git add AGENTS.md README.md
git commit -m "docs: replace root entrypoints with lightweight model"
```

### Task 3: Simplify the Shared Base Layer

**Files:**
- Modify: `base/AGENTS.md`
- Create: `base/notes/git-worktree.md`
- Create: `base/notes/credential-safety.md`
- Create: `base/notes/check-conventions-first.md`
- Create: `base/notes/explicit-tmpdir-for-long-jobs.md`
- Create: `base/notes/persistent-task-state-must-be-externalized.md`
- Create: `base/notes/visible-workflow-state-over-hidden-agent-features.md`
- Move to archive: `base/principles/*`
- Move to archive: `base/insights/*`
- Move to archive: `base/experience/*`
- Move to archive or remove from active flow: `base/knowledge-sedimentation.md`

**Step 1: Rewrite `base/AGENTS.md`**

Required content:

```md
# base

Shared knowledge used across roles.

## Skills
- `skills/eat/`
- `skills/skill-creator-codex/`

## Notes
- short bullet list of the shared notes kept active
```

**Step 2: Recreate the selected shared notes under `base/notes/`**

For each active shared note, preserve the core content but convert frontmatter to:

```yaml
---
kind: principle
description: "..."
triggers:
  - "..."
source:
  - "old/path.md"
---
```

Use `kind: insight` for `visible-workflow-state-over-hidden-agent-features.md`.

**Step 3: Archive the old base buckets**

Run:

```bash
mkdir -p archive/base
git mv base/principles archive/base/principles
git mv base/insights archive/base/insights
git mv base/experience archive/base/experience
```

For `base/knowledge-sedimentation.md`, choose one of:
- archive it as historical reference, or
- shrink it into a much shorter `base/notes/knowledge-model.md`

Default choice for this refactor: archive it.

**Step 4: Verify active base references**

Run:

```bash
rg -n "base/(principles|insights|experience|knowledge-sedimentation)" AGENTS.md README.md base roles
python3 tools/validate_knowledge_repo.py || true
```

Expected:
- only archived references remain in `archive/`
- validator may still fail until role migration completes

**Step 5: Commit**

```bash
git add base archive/base
git commit -m "refactor: collapse shared principles insights and experience into notes"
```

### Task 4: Create the Generalist Role and Absorb Default Engineering Work

**Files:**
- Modify: `roles/generalist-engineer/AGENTS.md`
- Modify: `roles/generalist-engineer/questions.md`
- Create: `roles/generalist-engineer/notes/default-engineering-boundaries.md`
- Optionally create: `roles/generalist-engineer/skills/.gitkeep`

**Step 1: Write the new role entrypoint**

Required content:

```md
# generalist-engineer

Default role for day-to-day feature work, bugfixes, refactors, ordinary reviews, and repository changes.

## Use This Role When
- the task is not primarily performance analysis
- the task is not primarily mechanism explanation

## Do Not Use This Role For
- deep mechanism analysis
- formal performance testing and capacity conclusions

## Load Order
1. `base/skills/`
2. `base/notes/`
3. this role's `skills/` or `notes/`
4. `questions.md` if needed
```

**Step 2: Seed one note that defines the role boundary**

Create `roles/generalist-engineer/notes/default-engineering-boundaries.md`:

```yaml
---
kind: principle
description: "Use the generalist role by default unless the task's core risk is mechanism explanation or performance evidence."
triggers:
  - "default role"
  - "which role"
  - "general coding"
---
```

**Step 3: Add starter questions**

Populate `roles/generalist-engineer/questions.md` with a short template:
- how much review depth should be default
- whether to keep a dedicated release-oriented note later

**Step 4: Commit**

```bash
git add roles/generalist-engineer
git commit -m "feat: add generalist engineer role"
```

### Task 5: Migrate `mechanism-analyst` to the New Model

**Files:**
- Modify: `roles/mechanism-analyst/AGENTS.md`
- Create: `roles/mechanism-analyst/notes/*.md`
- Move to archive: `roles/mechanism-analyst/principles/*`
- Move to archive: `roles/mechanism-analyst/insights/*`
- Move to archive: `roles/mechanism-analyst/experience/*`

**Step 1: Create `roles/mechanism-analyst/notes/`**

Run:

```bash
mkdir -p roles/mechanism-analyst/notes
```

**Step 2: Recreate active notes with `kind` frontmatter**

Migrate these files into `notes/`:
- `decompose-mechanism-questions.md` -> `kind: principle`
- `control-one-variable-at-a-time.md` -> `kind: principle`
- `minimum-mechanism-evidence-chain.md` -> `kind: principle`
- `trace-query-behavior-from-result-to-source.md` -> `kind: principle`
- `separate-local-cost-from-global-effect.md` -> `kind: insight`
- `noise-first-for-short-runs.md` -> `kind: insight`
- `separate-semantics-planner-and-operator-effects.md` -> `kind: insight`
- `2026-03-26-general-mechanism-analysis-patterns.md` -> `kind: experience`
- `2026-03-26-distinct-mechanism-across-falkordb-and-neo4j.md` -> `kind: experience`

Use `source:` to point to the original paths while migrating.

**Step 3: Rewrite the role `AGENTS.md`**

Keep:
- role responsibility
- use / do-not-use boundary
- a single `Notes` section instead of separate `Principles / Insights / Experience`
- `Questions`

**Step 4: Archive the old subdirectories**

Run:

```bash
mkdir -p archive/roles/mechanism-analyst
git mv roles/mechanism-analyst/principles archive/roles/mechanism-analyst/principles
git mv roles/mechanism-analyst/insights archive/roles/mechanism-analyst/insights
git mv roles/mechanism-analyst/experience archive/roles/mechanism-analyst/experience
```

**Step 5: Commit**

```bash
git add roles/mechanism-analyst archive/roles/mechanism-analyst
git commit -m "refactor: migrate mechanism analyst to unified notes"
```

### Task 6: Migrate `performance-infra-tester` to the New Model

**Files:**
- Modify: `roles/performance-infra-tester/AGENTS.md`
- Create: `roles/performance-infra-tester/notes/*.md`
- Keep: `roles/performance-infra-tester/skills/analysis-bundle-for-performance-experiments/SKILL.md`
- Keep: `roles/performance-infra-tester/skills/benchmark-report-packaging/SKILL.md`
- Move to archive: `roles/performance-infra-tester/principles/*`
- Move to archive: `roles/performance-infra-tester/insights/*`
- Move to archive: `roles/performance-infra-tester/experience/*`

**Step 1: Create the active notes**

Recreate:
- `scenario-comparability.md` -> `kind: principle`
- `line-chart-labeling.md` -> `kind: insight`

If there is no valuable role-specific experience yet, do not invent any.

**Step 2: Rewrite the role `AGENTS.md`**

Keep:
- role responsibility
- use / do-not-use boundary
- explicit report guardrail section
- active skill list
- one `Notes` section
- `Questions`

**Step 3: Archive the old bucket directories**

Run:

```bash
mkdir -p archive/roles/performance-infra-tester
git mv roles/performance-infra-tester/principles archive/roles/performance-infra-tester/principles
git mv roles/performance-infra-tester/insights archive/roles/performance-infra-tester/insights
```

Only move `experience/` if it contains non-placeholder content.

**Step 4: Commit**

```bash
git add roles/performance-infra-tester archive/roles/performance-infra-tester
git commit -m "refactor: migrate performance infra tester to unified notes"
```

### Task 7: Archive Low-Frequency Roles and Non-Core Shared Assets

**Files:**
- Move to archive: `roles/cli-tool-dev/`
- Move to archive: `roles/maintainer/`
- Move to archive: `base/skills/skill-creator/`
- Modify: any active `AGENTS.md` that still references archived content

**Step 1: Move the directories**

Run:

```bash
mkdir -p archive/roles archive/base/skills
git mv roles/cli-tool-dev archive/roles/cli-tool-dev
git mv roles/maintainer archive/roles/maintainer
git mv base/skills/skill-creator archive/base/skills/skill-creator
```

**Step 2: Remove stale references**

Run:

```bash
rg -n "cli-tool-dev|maintainer|skill-creator(?!-codex)" AGENTS.md README.md base roles
```

Fix all matches outside `archive/`.

**Step 3: Commit**

```bash
git add archive AGENTS.md README.md base roles
git commit -m "refactor: archive low-frequency roles and non-core shared assets"
```

### Task 8: Finish the Validator and Run Full Repository Verification

**Files:**
- Modify: `tools/validate_knowledge_repo.py`

**Step 1: Replace the placeholder validator with real checks**

Minimum implementation shape:

```python
def read_text(path: Path) -> str: ...
def active_roles() -> list[str]: ...
def assert_role_files() -> None: ...
def assert_readme_roles() -> None: ...
def assert_note_frontmatter() -> None: ...
def assert_no_archive_refs() -> None: ...
def assert_agents_refs_exist() -> None: ...
```

The script should print one line per passed check and exit `1` on the first failure with a precise path.

**Step 2: Run repository verification**

Run:

```bash
python3 tools/validate_knowledge_repo.py
rg -n "principles/|insights/|experience/" AGENTS.md README.md base roles
rg -n "cli-tool-dev|maintainer" AGENTS.md README.md base roles
```

Expected:
- validator passes
- no active references to old bucket names
- no active references to archived roles

**Step 3: Optional smoke check for active layout**

Run:

```bash
find base roles -maxdepth 3 -type f | sort
```

Expected:
- only the active roles appear under `roles/`
- notes exist under `base/notes/` and active roles' `notes/`

**Step 4: Commit**

```bash
git add tools/validate_knowledge_repo.py AGENTS.md README.md base roles
git commit -m "test: add repository validation for lightweight knowledge model"
```

### Task 9: Final Cleanup and Review Pass

**Files:**
- Modify: any remaining active docs with stale wording

**Step 1: Run final grep sweep**

Run:

```bash
rg -n "knowledge-sedimentation|principles/|insights/|experience/|cli-tool-dev|maintainer" AGENTS.md README.md base roles
```

Expected:
- no matches outside `archive/`, except allowed historical mentions inside note `source:` fields

**Step 2: Review diffs for readability**

Run:

```bash
git diff --stat origin/main...
git diff -- AGENTS.md README.md base/AGENTS.md roles
```

Check:
- root docs are shorter
- role entrypoints are structurally consistent
- active references point only to active files

**Step 3: Final commit if cleanup changes were needed**

```bash
git add AGENTS.md README.md base roles
git commit -m "docs: clean up lightweight knowledge repo wording"
```

## Risks and Guardrails

- Do not delete archived knowledge; move it under `archive/`
- Do not keep active references to archived files
- Do not invent role-specific notes just to fill space
- Keep `mechanism-analyst` and `performance-infra-tester` narrow; let `generalist-engineer` absorb the default workload
- Keep `eat` active from day one; it is the main bridge from conversation to reusable knowledge

## Definition of Done

- Active root model uses only `skills/`, `notes/`, and `questions.md`
- Only three active roles remain
- `maintainer` and `cli-tool-dev` are archived
- `base/skills/eat/` and `base/skills/skill-creator-codex/` remain active
- `python3 tools/validate_knowledge_repo.py` passes
- Root and role entrypoints no longer require reading long governance docs before useful work can start
