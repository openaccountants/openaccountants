#!/usr/bin/env python3
"""Does every skill still say the line each calculator quotes?

Each calculator in calculators/engines/<engine>/rules.json lists its figures as rules with a
`slug`, a `section` and a `quote`: the line of that skill the figure was taken from. The app
refuses to run a calculator when the skill no longer states the quoted line, so a skill edit
that drops or rewords that line silently switches the calculator off. This check says so on
the pull request instead.

  python3 scripts/check-calculator-quotes.py                 # every rule
  python3 scripts/check-calculator-quotes.py --changed-only  # rules whose skill changed vs origin/$BASE_REF

The skill is the file under skills/ whose frontmatter `name:` is the slug. Matching mirrors the
app (src/lib/engines/quote-match.ts in the platform repo): both sides are normalised the same
way, so only typography is forgiven (whitespace, markdown emphasis and links, thousands
separators, dash and quote-mark variants, spacing around table pipes, case). "..." in a quote
skips text within ONE line; a quote of several lines matches when each line is found on a line
of the skill, in order. Read-only; exit 1 when any quote is not found.
"""

import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ELLIPSIS = re.compile(r"\s*(?:\.\.\.|…)\s*")
NAME = re.compile(r"(?m)^name:\s*['\"]?([^'\"\n]+?)['\"]?\s*$")


# ---- matching: a line-for-line port of quote-match.ts -------------------------------------

def normalise_text(s):
    s = re.sub(r"(\d)[,    ](?=\d{3}(?!\d))", r"\1", s)
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`]", "", s)
    s = s.replace("\\|", "|")
    s = re.sub(r"[‘’‚′]", "'", s)
    s = re.sub(r"[“”„″]", '"', s)
    s = re.sub(r"\s*(?:-{2,3}|[‐‑‒–—―−-])\s*", "-", s)
    s = re.sub(r"\s*\|\s*", " | ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def normalise_lines(text):
    return [n for n in (normalise_text(l) for l in re.split(r"\r?\n", text)) if n]


def _index_of_whole(line, p, start):
    """Where p occurs in line from `start`, never splitting a number ("5.95%" is not in "15.95%")."""
    digit_start = bool(re.match(r"[\d.]", p))
    digit_end = bool(re.search(r"\d$", p))
    i = line.find(p, start)
    while i >= 0:
        before = line[max(0, i - 1):i]
        after = line[i + len(p):i + len(p) + 2]
        if not (digit_start and re.search(r"\d", before)) and not (digit_end and re.match(r"(\d|[.,]\d)", after)):
            return i
        i = line.find(p, i + 1)
    return -1


def _line_matches(pieces, line):
    at = 0
    for p in pieces:
        i = _index_of_whole(line, p, at)
        if i < 0:
            return False
        at = i + len(p)
    return True


def quote_found(quote, lines):
    quote_lines = [
        pieces for pieces in
        ([n for n in (normalise_text(x) for x in ELLIPSIS.split(q)) if n] for q in re.split(r"\r?\n", quote))
        if pieces
    ]
    if not quote_lines:
        return False
    start = 0
    for pieces in quote_lines:
        hit = next((i for i in range(start, len(lines)) if _line_matches(pieces, lines[i])), -1)
        if hit < 0:
            return False
        start = hit + 1
    return True


# ---- repo ---------------------------------------------------------------------------------

def split_frontmatter(text):
    """(frontmatter, body). The app serves the skill's sections, not its frontmatter."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end >= 0:
            return text[3:end], text[end + 4:]
    return "", text


def slug_of(text):
    m = NAME.search(split_frontmatter(text)[0])
    return m.group(1).strip() if m else None


def skill_index(root):
    """slug -> list of skill files (relative paths) with that frontmatter name."""
    out = {}
    for f in sorted((root / "skills").rglob("*.md")):
        if f.name == "README.md":
            continue
        slug = slug_of(f.read_text(encoding="utf-8", errors="replace"))
        if slug:
            out.setdefault(slug, []).append(f.relative_to(root).as_posix())
    return out


def load_rules(root):
    """[(engine, rule)] for every rule with a slug and a quote."""
    out = []
    for f in sorted((root / "calculators" / "engines").glob("*/rules.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        engine = data.get("engine") or f.parent.name
        for r in data.get("rules", []):
            if isinstance(r, dict) and str(r.get("slug") or "").strip() and str(r.get("quote") or "").strip():
                out.append((engine, r))
    return out


def changed_slugs(root):
    """Slugs of skill files the PR adds, edits, deletes or renames, read from both sides."""
    base = "origin/" + os.environ.get("BASE_REF", "main")
    diff = subprocess.run(["git", "diff", "--no-renames", "--name-only", f"{base}...HEAD", "--", "skills/"],
                          cwd=root, capture_output=True, text=True, check=True).stdout.split("\n")
    slugs = set()
    for path in filter(None, (p.strip() for p in diff)):
        if not path.endswith(".md"):
            continue
        head = root / path
        if head.exists():
            s = slug_of(head.read_text(encoding="utf-8", errors="replace"))
            if s:
                slugs.add(s)
        old = subprocess.run(["git", "show", f"{base}:{path}"], cwd=root, capture_output=True, text=True)
        if old.returncode == 0:
            s = slug_of(old.stdout)
            if s:
                slugs.add(s)
    return slugs


def check(root, only_slugs=None):
    """[(engine, rule, problem)] for every rule whose quote is not in its skill."""
    index = skill_index(root)
    cache = {}
    broken = []
    for engine, rule in load_rules(root):
        slug = rule["slug"].strip()
        if only_slugs is not None and slug not in only_slugs:
            continue
        files = index.get(slug)
        if not files:
            broken.append((engine, rule, "no skill under skills/ has this name"))
            continue
        found = False
        for f in files:
            if f not in cache:
                body = split_frontmatter((root / f).read_text(encoding="utf-8", errors="replace"))[1]
                cache[f] = normalise_lines(body)
            if quote_found(rule["quote"], cache[f]):
                found = True
                break
        if not found:
            broken.append((engine, rule, "quoted line not found in " + ", ".join(files)))
    return broken


def report(broken, checked_note):
    lines = ["## Calculator quotes", "", checked_note, ""]
    if not broken:
        lines.append("Every quoted line is still in its skill.")
        return "\n".join(lines)
    for engine in sorted({e for e, _, _ in broken}):
        lines.append(f"**This change removes a line calculator `{engine}` quotes; keep the line word for word, "
                     "or update the calculator in the app repo first.**")
    lines.append("")
    for engine, rule, problem in broken:
        lines.append(f"- `{engine}` rule `{rule.get('name', '?')}`, skill `{rule['slug']}` "
                     f"(section: {rule.get('section', '?')}): {problem}")
        for q in str(rule["quote"]).splitlines():
            lines.append(f"  > {q}")
    lines.append("")
    lines.append(f"{len(broken)} quoted line(s) not found. Matching forgives spacing, case, markdown and "
                 "thousands separators only; figures, words and their order must stay the same.")
    return "\n".join(lines)


def main(argv, root=ROOT):
    only = None
    note = "Checked every calculator rule."
    if "--changed-only" in argv:
        only = changed_slugs(root)
        note = ("Checked rules quoting the skills this PR changes: " + ", ".join(f"`{s}`" for s in sorted(only))
                if only else "This PR changes no skill files.")
    broken = check(root, only) if only is None or only else []
    text = report(broken, note)
    print(text)
    for engine, rule, _ in broken:
        print(f"::error::This change removes a line calculator {engine} quotes ({rule.get('name')}, "
              f"skill {rule['slug']}); keep the line word for word, or update the calculator in the app repo first.")
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(text + "\n")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
