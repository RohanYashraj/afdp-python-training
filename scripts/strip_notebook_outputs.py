#!/usr/bin/env python3
"""Git clean filter: strip outputs and execution counts from a Jupyter notebook.

Reads a notebook from stdin and writes the cleaned notebook to stdout.
Registered in .gitattributes so that committed .ipynb files never carry
executed cell outputs; the copy in your working folder is left untouched.

One-time setup after cloning:
    git config filter.nbstrip.clean "python3 scripts/strip_notebook_outputs.py"
    git config filter.nbstrip.smudge cat
    git config filter.nbstrip.required true
"""
import json
import sys


def strip(nb: dict) -> dict:
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
        cell.get("metadata", {}).pop("execution", None)
        cell.get("metadata", {}).pop("collapsed", None)
        cell.get("metadata", {}).pop("scrolled", None)
    meta = nb.setdefault("metadata", {})
    meta.pop("widgets", None)
    # Normalise kernel details so a local venv name never lands in the repo
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
    json.dump(strip(nb), sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
