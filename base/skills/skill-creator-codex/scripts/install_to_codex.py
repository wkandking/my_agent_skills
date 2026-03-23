#!/usr/bin/env python3
from __future__ import annotations

"""Install a skill folder into Codex's local skills directory."""

import argparse
import os
import shutil
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.quick_validate import validate_skill


def default_dest() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "skills"
    return Path.home() / ".codex" / "skills"


def install_skill(skill_path: Path, dest_root: Path, force: bool) -> Path:
    skill_path = skill_path.resolve()
    dest_root = dest_root.expanduser().resolve()

    valid, message = validate_skill(skill_path)
    if not valid:
        raise ValueError(message)

    dest_root.mkdir(parents=True, exist_ok=True)
    target = dest_root / skill_path.name

    if target.exists():
        if not force:
            raise FileExistsError(
                f"Destination already exists: {target}. Use --force to replace it."
            )
        shutil.rmtree(target)

    shutil.copytree(skill_path, target)
    return target


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install a skill folder into Codex's local skills directory."
    )
    parser.add_argument("skill_path", help="Path to the skill folder")
    parser.add_argument(
        "--dest",
        default=None,
        help="Override the destination skills directory",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing installed copy",
    )
    args = parser.parse_args()

    skill_path = Path(args.skill_path)
    dest = Path(args.dest) if args.dest else default_dest()

    try:
        target = install_skill(skill_path, dest, args.force)
    except Exception as exc:
        print(f"Install failed: {exc}", file=sys.stderr)
        return 1

    print(f"Installed skill to: {target}")
    print("Restart Codex to pick up the new skill.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
