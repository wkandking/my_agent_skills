# Performance Infra Tester Role Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a new `performance-infra-tester` role skeleton under `roles/` for infrastructure-focused performance testing.

**Architecture:** The role is introduced as a documentation-first package under `roles/performance-infra-tester/`. `AGENTS.md` defines purpose, scope, inputs, outputs, and operating rules; `questions.md` captures unresolved standards; placeholder files keep the knowledge directories tracked in git.

**Tech Stack:** Markdown, repository role conventions

---

### Task 1: Write the approved design and execution docs

**Files:**
- Create: `docs/plans/2026-03-23-performance-infra-tester-design.md`
- Create: `docs/plans/2026-03-23-performance-infra-tester.md`
- Verify: `docs/plans/2026-03-23-performance-infra-tester-design.md`
- Verify: `docs/plans/2026-03-23-performance-infra-tester.md`

**Step 1: Write the approved design doc**

Create `docs/plans/2026-03-23-performance-infra-tester-design.md` with the validated role positioning, directory structure, ownership boundaries, and initialization scope.

**Step 2: Write the implementation plan**

Create `docs/plans/2026-03-23-performance-infra-tester.md` with exact file paths, creation steps, and verification commands for the new role package.

**Step 3: Verify both files exist**

Run: `test -f /Users/wangkang/my_agent_skills/docs/plans/2026-03-23-performance-infra-tester-design.md && test -f /Users/wangkang/my_agent_skills/docs/plans/2026-03-23-performance-infra-tester.md`
Expected: command exits successfully with no output.

### Task 2: Create the role definition files

**Files:**
- Create: `roles/performance-infra-tester/AGENTS.md`
- Create: `roles/performance-infra-tester/questions.md`

**Step 1: Write the role definition**

Create `roles/performance-infra-tester/AGENTS.md` with sections for `Purpose`, `When To Use`, `Inputs`, `Outputs`, `Private Knowledge Layout`, and `Operating Notes`.

**Step 2: Write the initial open questions**

Create `roles/performance-infra-tester/questions.md` with unresolved questions around benchmark tooling, metadata standards, reporting expectations, and environment comparability.

**Step 3: Verify the role files are readable**

Run: `sed -n '1,220p' /Users/wangkang/my_agent_skills/roles/performance-infra-tester/AGENTS.md && sed -n '1,200p' /Users/wangkang/my_agent_skills/roles/performance-infra-tester/questions.md`
Expected: both files print the intended markdown content.

### Task 3: Track the role knowledge directories

**Files:**
- Create: `roles/performance-infra-tester/principles/.gitkeep`
- Create: `roles/performance-infra-tester/skills/.gitkeep`
- Create: `roles/performance-infra-tester/experience/.gitkeep`
- Create: `roles/performance-infra-tester/insights/.gitkeep`

**Step 1: Add placeholder files**

Create `.gitkeep` files inside each role-specific knowledge directory so the structure is preserved in git.

**Step 2: Verify the directory layout**

Run: `find /Users/wangkang/my_agent_skills/roles/performance-infra-tester -maxdepth 2 -type f | sort`
Expected: the output lists `AGENTS.md`, `questions.md`, and the four `.gitkeep` files.

### Task 4: Final verification

**Files:**
- Verify: `roles/performance-infra-tester/AGENTS.md`
- Verify: `roles/performance-infra-tester/questions.md`
- Verify: `roles/performance-infra-tester/principles/.gitkeep`
- Verify: `roles/performance-infra-tester/skills/.gitkeep`
- Verify: `roles/performance-infra-tester/experience/.gitkeep`
- Verify: `roles/performance-infra-tester/insights/.gitkeep`

**Step 1: Check for the required operating rules**

Run: `rg -n "Confirm baseline|Define the load model|Tie every conclusion|Prefer baseline|Separate system bottlenecks|Report enough detail" /Users/wangkang/my_agent_skills/roles/performance-infra-tester/AGENTS.md`
Expected: six matching lines covering the role's operating notes.

**Step 2: Check for the expected open questions**

Run: `rg -n "benchmark tools|metadata|required|report template|hardware|cloud" /Users/wangkang/my_agent_skills/roles/performance-infra-tester/questions.md`
Expected: matches confirming the seeded question list.

**Step 3: Commit**

Run:

```bash
git add docs/plans/2026-03-23-performance-infra-tester-design.md \
  docs/plans/2026-03-23-performance-infra-tester.md \
  roles/performance-infra-tester
git commit -m "feat: add performance infra tester role"
```

Expected: a commit containing the new role skeleton and planning docs.
