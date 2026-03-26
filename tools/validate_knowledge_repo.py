#!/usr/bin/env python3

from pathlib import Path


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
