#!/usr/bin/env python3
"""Rewrite the generated blocks in README.md from the skill files.

Two blocks, each between HTML comment markers, so the numbers and names on the front
page come from the same frontmatter the site reads and cannot drift:

    <!-- oa-stats:start --> ... <!-- oa-stats:end -->
    <!-- oa-accountants:start --> ... <!-- oa-accountants:end -->

An approval counts here exactly as it does on the site: `tier: 1` plus `reviewed_by`
in the skill's frontmatter (scripts/coverage-report.py `is_reviewed`). Names are shown
as written in the approving accountant's own pull request; this script never edits them.

    python3 scripts/build-readme-blocks.py           # print the blocks
    python3 scripts/build-readme-blocks.py --write   # rewrite README.md
    python3 scripts/build-readme-blocks.py --check   # exit 1 if README.md is out of date
"""
import argparse
import collections
import importlib.util
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(REPO_ROOT, "README.md")


def load_report():
    spec = importlib.util.spec_from_file_location("coverage_report", os.path.join(REPO_ROOT, "scripts", "coverage-report.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.build_report()


def blocks(report):
    people = collections.defaultdict(lambda: {"skills": 0, "places": set()})
    for row in report["rows"]:
        for a in row.get("approved", []):
            name = (a.get("by") or "").strip()
            if not name:
                continue
            people[name]["skills"] += 1
            people[name]["places"].add(row["name"])
    places = {p for v in people.values() for p in v["places"]}
    covered = sum(1 for r in report["rows"] if r["skills"] > 0)

    stats = (
        f"**{len(people)} named accountants** approving skills in **{len(places)} countries and states** · "
        f"skills for **{covered:,} countries, states and territories** · every figure linked to its official source"
    )
    by_place = collections.defaultdict(set)
    for name, v in people.items():
        for p in v["places"]:
            by_place[p].add(name)
    lines = ["| Country or state | Accountants |", "|---|---|"]
    for place in sorted(by_place, key=str.lower):
        lines.append(f"| {place} | {', '.join(sorted(by_place[place], key=str.lower))} |")
    return stats, "\n".join(lines)


def replace(text, key, body):
    pattern = re.compile(rf"(<!-- oa-{key}:start -->\n)(?:.*?\n)?(<!-- oa-{key}:end -->)", re.S)
    if not pattern.search(text):
        raise SystemExit(f"README.md has no oa-{key} markers")
    return pattern.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text, count=1)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    stats, table = blocks(load_report())
    if not (args.write or args.check):
        print(stats + "\n\n" + table)
        return 0
    with open(README, encoding="utf-8") as fh:
        old = fh.read()
    new = replace(replace(old, "stats", stats), "accountants", table)
    if args.check:
        if new != old:
            print("README.md generated blocks are out of date: run python3 scripts/build-readme-blocks.py --write")
            return 1
        return 0
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(new)
    return 0


if __name__ == "__main__":
    sys.exit(main())
