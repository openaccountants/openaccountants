#!/usr/bin/env python3
"""
Build llms-full.txt at the repo root — the expanded companion to llms.txt.

Concatenates, in order:
  1. The current llms.txt (must exist; run after any llms.txt rewrite)
  2. A divider
  3. A compact one-line-per-guide inventory from index.json
     ("- <slug> | <jurisdiction> | tax year <year> | author <author or publisher>")
  4. A divider
  5. The full text of START-HERE.md and docs/QUALITY-TIERS.md

Stdlib only. index.json must be up to date first:
    python3 scripts/build-index.py && python3 scripts/build-llms-full.py
"""

import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(REPO_ROOT, "llms-full.txt")
DIVIDER = "\n\n" + "=" * 72 + "\n\n"


def read_text(rel_path):
    path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.isfile(path):
        sys.exit(f"error: required file missing: {rel_path}")
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def guide_inventory():
    index = json.loads(read_text("index.json"))
    lines = ["## Guide inventory "
             f"({index['counts']['guides']} guides, "
             f"{index['counts']['jurisdictions']} jurisdictions)", ""]
    for guide in index["guides"]:
        jurisdiction = guide.get("jurisdiction") or "-"
        tax_year = guide.get("tax_year") or "unspecified"
        author = guide.get("authored_by") or "OpenAccountants"
        lines.append(
            f"- {guide['slug']} | {jurisdiction} | tax year {tax_year} | author {author}"
        )
    return "\n".join(lines)


def build_text():
    parts = [
        read_text("llms.txt").rstrip("\n"),
        guide_inventory(),
        read_text("START-HERE.md").rstrip("\n"),
        read_text(os.path.join("docs", "QUALITY-TIERS.md")).rstrip("\n"),
    ]
    return DIVIDER.join(parts) + "\n"


def main():
    # --out <path> lets CI regenerate to a temp file for staleness comparison.
    out_path = OUT_PATH
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(build_text())
    print(f"{os.path.basename(out_path)} written ({os.path.getsize(out_path):,} bytes)")


if __name__ == "__main__":
    main()
