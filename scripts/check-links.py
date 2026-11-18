#!/usr/bin/env python3
"""Fail when a Markdown file links to a repo path that does not exist.

Covers relative links in skills/**, docs/*.md and the root *.md files. Web links
(http, https, mailto) and same-page anchors are not checked. A broken relative link
also breaks on the website, which rewrites skill links to github.com/.../blob/main/...

    python3 scripts/check-links.py                 # every file
    python3 scripts/check-links.py --changed-only  # files changed against origin/$BASE_REF (CI)
"""
import argparse
import os
import re
import subprocess
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
SKIP = ("http://", "https://", "mailto:", "#", "tel:")


def files(changed_only):
    if changed_only:
        base = os.environ.get("BASE_REF", "main")
        out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AMR", f"origin/{base}...HEAD"],
                             cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
        return [f for f in out if f.endswith(".md") and in_scope(f)]
    out = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    return [f for f in out if in_scope(f)]


def in_scope(path):
    return path.startswith("skills/") or (path.startswith("docs/") and path.count("/") == 1) or "/" not in path


def broken_links(path):
    with open(os.path.join(ROOT, path), encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    text = re.sub(r"```.*?```", "", text, flags=re.S)  # links inside code blocks are examples
    base = os.path.dirname(os.path.join(ROOT, path))
    for target in LINK.findall(text):
        target = target.strip("<>")
        if target.startswith(SKIP) or "{" in target:
            continue
        clean = urllib.parse.unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not clean:
            continue
        full = os.path.normpath(os.path.join(ROOT, clean.lstrip("/")) if clean.startswith("/") else os.path.join(base, clean))
        if not full.startswith(ROOT) or not os.path.exists(full):
            yield target


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--changed-only", action="store_true")
    args = ap.parse_args(argv)
    bad = [(f, t) for f in files(args.changed_only) for t in broken_links(f)]
    for f, t in bad:
        print(f"::error file={f}::link to a path that does not exist: {t}")
    print(f"{len(bad)} broken relative link(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
