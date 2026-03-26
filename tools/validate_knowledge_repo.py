#!/usr/bin/env python3

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTIVE_ROLES = [
    "generalist-engineer",
    "mechanism-analyst",
    "performance-infra-tester",
]
ACTIVE_SHARED_SKILLS = [
    "eat",
    "skill-creator-codex",
]
NOTE_KEYS = ["kind", "description", "triggers"]
PATH_RE = re.compile(r"`([^`]+)`")
FENCED_BLOCK_RE = re.compile(r"```.*?```", re.S)


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def ok(msg: str) -> None:
    print(f"OK: {msg}")


def read_text(path: Path) -> str:
    return path.read_text()


def section_items(text: str, header: str) -> list[str]:
    pattern = re.compile(rf"^## {re.escape(header)}\n(.*?)(?=^## |\Z)", re.M | re.S)
    match = pattern.search(text)
    if not match:
        return []
    return re.findall(r"- `([^`]+)`", match.group(1))


def active_role_dirs() -> list[str]:
    return sorted(
        p.name
        for p in (ROOT / "roles").iterdir()
        if p.is_dir() and not p.name.startswith("_")
    )


def assert_active_roles() -> None:
    actual = active_role_dirs()
    if actual != ACTIVE_ROLES:
        fail(f"active roles mismatch: expected {ACTIVE_ROLES}, got {actual}")
    ok("active roles match expected directories")


def assert_shared_skills() -> None:
    skills_dir = ROOT / "base" / "skills"
    actual = sorted(
        p.name for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith(".")
    )
    if actual != ACTIVE_SHARED_SKILLS:
        fail(f"active shared skills mismatch: expected {ACTIVE_SHARED_SKILLS}, got {actual}")
    ok("active shared skills match expected directories")


def assert_root_entrypoints() -> None:
    for path in [ROOT / "AGENTS.md", ROOT / "README.md", ROOT / "base" / "AGENTS.md"]:
        if not path.exists():
            fail(f"missing required root entrypoint: {path}")
    readme_roles = sorted(section_items(read_text(ROOT / "README.md"), "Active Roles"))
    if readme_roles != ACTIVE_ROLES:
        fail(f"README active roles mismatch: expected {ACTIVE_ROLES}, got {readme_roles}")
    agents_roles = sorted(section_items(read_text(ROOT / "AGENTS.md"), "Active Roles"))
    if agents_roles != ACTIVE_ROLES:
        fail(f"AGENTS active roles mismatch: expected {ACTIVE_ROLES}, got {agents_roles}")
    ok("root entrypoints list the correct active roles")


def assert_role_files() -> None:
    for role in ACTIVE_ROLES:
        role_dir = ROOT / "roles" / role
        for path in [role_dir / "AGENTS.md", role_dir / "questions.md", role_dir / "notes"]:
            if not path.exists():
                fail(f"missing required role path: {path}")
    ok("active roles contain required files and notes directories")


def assert_no_old_bucket_dirs() -> None:
    disallowed = ["principles", "insights", "experience"]
    active_dirs = [ROOT / "base"]
    active_dirs.extend(ROOT / "roles" / role for role in ACTIVE_ROLES)
    active_dirs.append(ROOT / "roles" / "_template")
    for parent in active_dirs:
        for name in disallowed:
            if (parent / name).exists():
                fail(f"old bucket directory still active: {parent / name}")
    ok("old bucket directories are absent from active tree")


def extract_frontmatter(text: str, path: Path) -> str:
    if not text.startswith("---\n"):
        fail(f"note missing opening frontmatter fence: {path}")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        fail(f"note missing closing frontmatter fence: {path}")
    return parts[0]


def assert_note_frontmatter() -> None:
    note_files = sorted((ROOT / "base" / "notes").glob("*.md"))
    for role in ACTIVE_ROLES:
        note_files.extend(sorted((ROOT / "roles" / role / "notes").glob("*.md")))
    for path in note_files:
        text = read_text(path)
        frontmatter = extract_frontmatter(text, path)
        for key in NOTE_KEYS:
            if f"{key}:" not in frontmatter:
                fail(f"note missing frontmatter key '{key}': {path}")
    ok("all active notes include required frontmatter keys")


def iter_reference_checked_entrypoints() -> list[Path]:
    paths = [ROOT / "AGENTS.md", ROOT / "README.md", ROOT / "base" / "AGENTS.md"]
    for role in ACTIVE_ROLES:
        role_dir = ROOT / "roles" / role
        paths.append(role_dir / "AGENTS.md")
    return paths


def iter_bucket_checked_docs() -> list[Path]:
    paths = [
        ROOT / "AGENTS.md",
        ROOT / "README.md",
        ROOT / "base" / "AGENTS.md",
        ROOT / "base" / "skills" / "eat" / "SKILL.md",
        ROOT / "base" / "skills" / "eat" / "references" / "knowledge-placement.md",
    ]
    for role in ACTIVE_ROLES:
        paths.append(ROOT / "roles" / role / "AGENTS.md")
    return paths


def resolve_ref(text: str, source: Path) -> list[Path]:
    text = FENCED_BLOCK_RE.sub("", text)
    refs = []
    for candidate in PATH_RE.findall(text):
        if candidate in ACTIVE_ROLES:
            continue
        if candidate.startswith("<") or candidate.startswith("$") or candidate.startswith("kind:"):
            continue
        if source in {ROOT / "AGENTS.md", ROOT / "README.md"} and candidate in {
            "skills/",
            "notes/",
            "questions.md",
        }:
            continue
        if not ("/" in candidate or candidate.endswith(".md")):
            continue
        if candidate.startswith(("http://", "https://")):
            continue
        if candidate.startswith(("base/", "roles/", "tools/", "AGENTS.md", "README.md")):
            refs.append(ROOT / candidate)
        else:
            refs.append((source.parent / candidate).resolve())
    return refs


def assert_agents_refs_exist() -> None:
    for path in iter_reference_checked_entrypoints():
        text = read_text(path)
        for ref in resolve_ref(text, path):
            try:
                rel = ref.relative_to(ROOT)
            except ValueError:
                fail(f"reference escapes repository: {path} -> {ref}")
            if not ref.exists():
                fail(f"broken reference: {path} -> {rel}")
    ok("active entrypoints reference existing files")


def assert_no_archive_refs() -> None:
    for path in iter_bucket_checked_docs():
        text = FENCED_BLOCK_RE.sub("", read_text(path))
        if "archive/" in text:
            fail(f"active entrypoint references archive: {path}")
    ok("active entrypoints do not reference archive")


def assert_no_old_bucket_paths() -> None:
    pattern = re.compile(r"(principles/|insights/|experience/|knowledge-sedimentation)")
    for path in iter_bucket_checked_docs():
        text = FENCED_BLOCK_RE.sub("", read_text(path))
        if pattern.search(text):
            fail(f"active entrypoint still references old knowledge buckets: {path}")
    ok("active entrypoints no longer reference old bucket paths")


def main() -> None:
    assert_active_roles()
    assert_shared_skills()
    assert_root_entrypoints()
    assert_role_files()
    assert_no_old_bucket_dirs()
    assert_note_frontmatter()
    assert_agents_refs_exist()
    assert_no_archive_refs()
    assert_no_old_bucket_paths()
    print("PASS: lightweight knowledge repo layout is valid")


if __name__ == "__main__":
    main()
