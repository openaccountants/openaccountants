#!/usr/bin/env python3
"""Move the repo to the country-first layout. Dry run unless --apply.

    python3 scripts/migrate-layout.py            # print the plan, change nothing
    python3 scripts/migrate-layout.py --apply    # git mv, fix relative links, write docs/PATH-MOVES.md

Every move is a git mv. File text changes in one way only: a relative link whose
target moved is rewritten so it still resolves. A plain path in prose is left alone.
Run from a clean checkout with origin/main at its tip, before any other change.
"""

import os
import re
import subprocess
import sys
from pathlib import PurePosixPath

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RENAMED_COUNTRIES = {
    "bvi": "british-virgin-islands",
    "united-arab-emirates": "uae",
    "cura-ao": "curacao",
    "s-o-tom-and-pr-ncipe": "sao-tome-and-principe",
}
# Same names as CA_PROVINCE_DIRS in build-packages.py.
CA_PROVINCE_DIRS = {
    "ab": "alberta", "bc": "british-columbia", "mb": "manitoba", "nb": "new-brunswick",
    "nl": "newfoundland", "ns": "nova-scotia", "nt": "northwest-territories", "nu": "nunavut",
    "on": "ontario", "pe": "pei", "qc": "quebec", "sk": "saskatchewan", "yt": "yukon",
}
INTL = "skills/international/"
# Generated trees are rebuilt by the sync; their links follow the sources.
NO_LINK_FIX = ("packages/", "agent-skills/", "plugins/openaccountants/skills/", "docs/PATH-MOVES.md")
LINK_RE = re.compile(r"(\]\()(<?)([^)\s>]+)|^(\[[^\]]+\]:[ \t]+)(<?)(\S+?)>?$", re.M)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def new_path(path):
    """The new home of a tracked file, or None if it stays."""
    if path.startswith("ledgers/"):
        return "evidence/" + path
    if path.startswith("skills/research/"):
        return "evidence/research/" + path[len("skills/research/"):]
    if path.startswith("skills/federal/"):
        return "skills/us/" + path[len("skills/"):]
    if path.startswith("skills/us-states/"):
        return "skills/us/states/" + path[len("skills/us-states/"):]
    if not path.startswith(INTL):
        return None
    rest = path[len(INTL):]
    if rest == "README.md":  # skills/README.md already exists
        return "skills/COUNTRIES.md"
    folder, _, tail = rest.partition("/")
    if folder == "alberta":
        return f"skills/canada/alberta/{tail}"
    if folder == "ca-chartered-accountant":
        province = CA_PROVINCE_DIRS[tail.split("-", 1)[0]]
        return f"skills/canada/{province}/{tail}"
    return f"skills/{RENAMED_COUNTRIES.get(folder, folder)}/{tail}"


def build_moves(files):
    moves = {p: n for p in files if (n := new_path(p))}
    targets = {}
    existing = set(files) - set(moves)
    for old, new in moves.items():
        if new in existing or new in targets:
            raise SystemExit(f"collision: {old} and {targets.get(new, 'an existing file')} both land on {new}")
        targets[new] = old
    return moves


def normal(path):
    return os.path.normpath(path).replace(os.sep, "/")


def fix_links(text, old_file, moves, moved_dirs, known):
    """Rewrite relative links that a move would break. Returns (text, count)."""
    new_file = moves.get(old_file, old_file)
    old_dir = str(PurePosixPath(old_file).parent)
    new_dir = str(PurePosixPath(new_file).parent)
    count = 0

    def resolve(target):
        if target in moves:
            return moves[target]
        for old, new in moved_dirs:
            if target == old:
                return new
            if target.startswith(old + "/"):
                return new + target[len(old):]
        return target

    def replace(match):
        nonlocal count
        raw = match.group(3) if match.group(3) is not None else match.group(6)
        if re.match(r"[a-z][a-z0-9+.-]*:|#|/", raw, re.I):
            return match.group(0)
        target, hash_, frag = raw.partition("#")
        trailing = "/" if target.endswith("/") else ""
        resolved = normal(os.path.join(old_dir, target.rstrip("/")))
        if resolved not in known:
            return match.group(0)
        rel = os.path.relpath(resolve(resolved), new_dir).replace(os.sep, "/")
        if normal(os.path.join(new_dir, target.rstrip("/"))) == resolve(resolved):
            return match.group(0)
        count += 1
        return match.group(0).replace(raw, rel + trailing + hash_ + frag, 1)

    return LINK_RE.sub(replace, text), count


def moved_directories(files, moves):
    """Old folder to new folder, where every file in the old folder went to one place."""
    seen = {}
    for path in files:
        parent = str(PurePosixPath(path).parent)
        while parent != ".":
            seen.setdefault(parent, set())
            new = moves.get(path)
            suffix = path[len(parent):]
            seen[parent].add(new[: -len(suffix)] if new and new.endswith(suffix) else None)
            parent = str(PurePosixPath(parent).parent)
    pairs = [(d, next(iter(v))) for d, v in seen.items() if len(v) == 1 and None not in v]
    # Merged folders: a link to the folder itself goes to the folder that took its files.
    for old, new in (
        ("skills/international/bvi", "skills/british-virgin-islands"),
        ("skills/international/united-arab-emirates", "skills/uae"),
        ("skills/international/alberta", "skills/canada/alberta"),
        ("skills/international/ca-chartered-accountant", "skills/canada"),
        ("skills/international", "skills"),
    ):
        pairs.append((old, new))
    return sorted(set(pairs), key=lambda p: -len(p[0]))


def write_path_moves(moves):
    lines = [
        "# Path moves", "",
        "Every file moved by `scripts/migrate-layout.py`: old path, new path. Slugs did not change.",
        "Use this to update `skills.github_path` on the platform.", "",
        "| Old path | New path |", "|---|---|",
    ]
    lines += [f"| {old} | {new} |" for old, new in sorted(moves.items())]
    with open(os.path.join(ROOT, "docs/PATH-MOVES.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


def main():
    apply = "--apply" in sys.argv
    files = git("ls-files", "-z").split("\0")[:-1]
    moves = build_moves(files)
    dirs = moved_directories(files, moves)
    known = set(files)
    for path in files:
        parent = str(PurePosixPath(path).parent)
        while parent != ".":
            known.add(parent)
            parent = str(PurePosixPath(parent).parent)

    edits = {}
    total_links = 0
    for path in files:
        if not path.endswith(".md") or path.startswith(NO_LINK_FIX):
            continue
        with open(os.path.join(ROOT, path), encoding="utf-8", newline="") as fh:
            text = fh.read()
        fixed, count = fix_links(text, path, moves, dirs, known)
        if count:
            edits[path] = fixed
            total_links += count

    print(f"{len(moves)} files move, {total_links} relative links change in {len(edits)} files")
    groups = {}
    for old, new in moves.items():
        depth = 3 if old.startswith(INTL) else 2
        key = "/".join(old.split("/")[:depth]), "/".join(new.split("/")[:depth])
        groups[key] = groups.get(key, 0) + 1
    for (old, new), n in sorted(groups.items()):
        print(f"  {old} -> {new} ({n})")
    if not apply:
        print("dry run, nothing changed. Pass --apply to move.")
        return

    pending = dict(moves)
    # Whole folders first: one git mv per folder is far faster than one per file.
    for old, new in sorted(dirs, key=lambda p: len(p[0])):
        if os.path.isdir(os.path.join(ROOT, old)):
            members = [p for p in pending if p.startswith(old + "/")]
            if not members or not os.path.dirname(new) or os.path.exists(os.path.join(ROOT, new)):
                continue
            if old == "skills/international" or any(pending[p] != new + p[len(old):] for p in members):
                continue
            os.makedirs(os.path.join(ROOT, os.path.dirname(new)), exist_ok=True)
            git("mv", old, new)
            for p in members:
                del pending[p]
    for old, new in pending.items():
        os.makedirs(os.path.dirname(os.path.join(ROOT, new)), exist_ok=True)
        git("mv", old, new)
    for old, text in edits.items():
        with open(os.path.join(ROOT, moves.get(old, old)), "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
    write_path_moves(moves)
    print("moved. Now rebuild the skills/ reports and run the tests.")


if __name__ == "__main__":
    main()
