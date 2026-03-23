# Script Inventory

Use this directory as three separate buckets rather than one flat toolchain.

## Codex-native helpers

These are part of the intended Codex workflow:

- `quick_validate.py`
- `install_to_codex.py`
- `package_skill.py`

## General reporting helpers

These can still be useful locally, but they are not required for the core
Codex create/validate/install flow:

- `aggregate_benchmark.py`
- `generate_report.py`

## Retained Claude-only reference automation

These files are carried over from the upstream Anthropic skill for reference.
They depend on the `claude` CLI and are not part of the Codex-native path:

- `run_eval.py`
- `run_loop.py`
- `improve_description.py`

Treat them as legacy reference assets unless you are intentionally working in a
Claude-compatible environment.
