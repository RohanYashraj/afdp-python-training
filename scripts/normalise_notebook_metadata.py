#!/usr/bin/env python3
"""Git clean filter: normalise Jupyter notebook metadata.

Reads a notebook from stdin and writes it to stdout with cell outputs kept
intact but machine-specific metadata (local kernel/venv name, Python version,
execution timestamps) reset, so commits contain only meaningful changes.

One-time setup after cloning:
    git config filter.nbnorm.clean "python3 scripts/normalise_notebook_metadata.py"
    git config filter.nbnorm.smudge cat
    git config filter.nbnorm.required true
"""
import json
import sys


def normalise(nb: dict) -> dict:
    for cell in nb.get("cells", []):
        cell.get("metadata", {}).pop("execution", None)
    meta = nb.setdefault("metadata", {})
    meta.pop("widgets", None)
    if "kernelspec" in meta:
        meta["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    if "language_info" in meta:
        meta["language_info"] = {"name": "python"}
    return nb


def main() -> None:
    raw = sys.stdin.read()
    try:
        nb = json.loads(raw)
    except json.JSONDecodeError:
        sys.stdout.write(raw)  # not valid JSON: pass through unchanged
        return
    json.dump(normalise(nb), sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
