#!/usr/bin/env python3
"""Mechanical checks for one skill file, one function per line of the standard.

The standard is docs/skill-template.md. Each check here is one line of it that a
script can test without reading the law: it takes ``(path, text, frontmatter)``
and returns a list of problem strings (empty means pass). ``run_all(path)``
runs every check on one file and returns ``{check_name: [problems]}``.

Two callers share these: scripts/build-register.py (one column per check in
skills/REGISTER.csv, a pass rate per check in REGISTER.md) and
scripts/validate-guides.py (errors on a PR, warnings on the backlog). No AI,
no network: text and regex only, so a result is the same on every machine.

    python3 scripts/skill_checks.py skills/slovakia/slovakia-pit.md
"""

import importlib.util
import os
import re
import sys

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, os.path.join(SCRIPTS_DIR, filename))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


repo_layout = _load("repo_layout", "repo_layout.py")
_build_index = _load("build_index", "build-index.py")
_coverage = _load("coverage_report", "coverage-report.py")
try:
    _check_examples = _load("check_examples", "check-examples.py")
    OA_CHECK_BLOCK_RE = _check_examples.BLOCK_RE
except Exception:  # pragma: no cover - the regex below is the same shape
    OA_CHECK_BLOCK_RE = re.compile(r"^```oa-check[ \t]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)

#: The tax year the figures must apply to (rule 8). Bump each December.
CURRENT_TAX_YEAR = 2026

#: The nine section headings of the deep-tax shape, in order, as
#: docs/skill-template.md lists them. A numbering prefix ("## 1.") is tolerated.
CANONICAL_HEADINGS = [
    "Who this applies to",
    "Rates, bands and thresholds",
    "The base",
    "Deadlines and filing",
    "Penalties and interest",
    "Cross-border points",
    "Two worked examples that recompute",
    "Ask the client first",
    "Sources",
]
#: Wording the packs built to the standard shipped with before the heading
#: strings were fixed verbatim. Accepted until the template settles the nine
#: strings (plan step 3); then this map goes and only CANONICAL_HEADINGS pass.
HEADING_ALIASES = {
    "The base": {"The taxable base"},
    "Two worked examples that recompute": {"Worked examples"},
}
#: The second canonical set (the October method shape, ~250 skills). Six required headings, in
#: order; three optional ones may sit between them. docs/skill-template.md line 7 lists both
#: sets; the shape test of 31 Oct 2026 measured them within noise of each other.
METHOD_HEADINGS = [
    "Scope",
    "Ask the client first",
    "The method, step by step",
    "Worked cases",
    "When to refuse or refer",
    "Talk to a verified accountant",
]
METHOD_ALIASES = {"Scope": {"Scope and who this is for"}}

#: Skills that keep the general template (accounting packs). The checks still
#: run on them, but the caller treats a failure as a warning, never an error.
GENERAL_TEMPLATE_CATEGORIES = {
    "bookkeeping", "invoicing", "financial-statements", "financial-reporting", "tax-optimization",
}
#: Router, template and pattern files: not tax skills, not accounting packs.
META_CATEGORIES = {
    "orchestrator", "patterns", "pattern", "template", "foundation", "integration",
    "intelligence", "vertical",
}

NON_REVIEWER_MARKERS = {"pending", "pending_review", "none", "no", "false", "-", "n/a", "tbd"}
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
URL_RE = re.compile(r"https?://[^\s)>\]|]+")
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)
NUMBER_PREFIX_RE = re.compile(r"^(?:section\s+)?\d+[.):]?\s*(?:[-:]\s*)?", re.IGNORECASE)
FENCE_RE = re.compile(r"^```.*?^```[ \t]*$", re.MULTILINE | re.DOTALL)
AMOUNT_COLUMN_RE = re.compile(r"amount|rate|figure|value|threshold", re.IGNORECASE)
EM_DASH = "—"


# ---------------------------------------------------------------------------
# Reading a file
# ---------------------------------------------------------------------------

def read_frontmatter(text):
    """Return the frontmatter as a dict (``{}`` when the file has none).

    Strict YAML first (the same loader validate-guides.py uses); the tolerant
    key scanner from build-index.py when the block is malformed, so a check can
    still say what it sees.
    """
    block = _build_index.extract_frontmatter(text)
    if block is None:
        return {}
    try:
        from frontmatter_yaml import load_frontmatter
        data = load_frontmatter(block)
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    fields = _build_index.parse_known_keys(block)
    for key in ("tax_year_notes", "reviewed_on", "version"):
        m = re.search(rf"^{key}:[ \t]*(.*)$", block, re.MULTILINE)
        if m:
            fields[key] = _build_index.clean_value(m.group(1))
    return {k: v for k, v in fields.items() if v is not None}


def rel_path(path):
    path = os.path.abspath(path) if not os.path.isabs(path) else path
    try:
        return os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")
    except ValueError:
        return path.replace(os.sep, "/")


def slug_of(path):
    return os.path.splitext(os.path.basename(path))[0]


def domains_of(path, frontmatter):
    """GOAL.md domain codes this skill covers, by coverage-report's rule."""
    return _coverage.domains_of({"slug": slug_of(path), "category": frontmatter.get("category") or ""})


def scope_of(path, frontmatter):
    """``tax`` (deep-tax shape applies), ``general`` (accounting pack) or ``other``."""
    rel = rel_path(path)
    category = str(frontmatter.get("category") or "").strip().lower()
    if category in GENERAL_TEMPLATE_CATEGORIES:
        return "general"
    if category in META_CATEGORIES:
        return "other"
    if domains_of(path, frontmatter) or (repo_layout.is_country_path(rel) and not rel.startswith("skills/us/federal/")):
        return "tax"
    return "other"


FRONTMATTER_RE = re.compile(r"\A---[ \t]*\n.*?^(?:---|\.\.\.)[ \t]*$\n?", re.MULTILINE | re.DOTALL)


def _body(text):
    """The file without its frontmatter block."""
    return FRONTMATTER_RE.sub("", text, count=1)


def _headings(text):
    """``[(normalised heading text, offset)]`` for every ``## `` heading outside a fence."""
    body = FENCE_RE.sub("", text)
    out = []
    for m in HEADING_RE.finditer(body):
        raw = m.group(1).strip()
        raw = NUMBER_PREFIX_RE.sub("", raw).strip()
        out.append((raw, m.start()))
    return out


def _section(text, title_match):
    """Text of the ``## `` section whose heading satisfies ``title_match``; '' if absent."""
    for m in HEADING_RE.finditer(text):
        title = NUMBER_PREFIX_RE.sub("", m.group(1).strip()).strip()
        if title_match(title):
            rest = text[m.end():]
            nxt = re.search(r"^##\s", rest, re.MULTILINE)
            return rest[: nxt.start()] if nxt else rest
    return ""


def _table_rows(section):
    """Data rows of every markdown table in ``section``: list of lists of cells."""
    rows = []
    lines = section.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            header = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append((header, cells))
                i += 1
        else:
            i += 1
    return rows


# ---------------------------------------------------------------------------
# The checks: (path, text, frontmatter) -> [problem, ...]
# ---------------------------------------------------------------------------

def check_tax_year_current(path, text, fm):
    """(a) ``tax_year`` is the current year, or ``tax_year_notes`` explains the label."""
    year = fm.get("tax_year")
    if year is None or str(year).strip() == "":
        return ["no tax_year"]
    if str(year).strip() == str(CURRENT_TAX_YEAR):
        return []
    if fm.get("tax_year_notes"):
        return []
    return [f"tax_year {year} is not {CURRENT_TAX_YEAR} and no tax_year_notes"]


def check_sources_read_dates(path, text, fm):
    """(b) a ``## Sources`` section exists and every table row (or list item) with a URL carries a YYYY-MM-DD read date."""
    section = _section(text, lambda t: t.lower() == "sources")
    if not section:
        return ["no ## Sources section"]
    undated = 0
    for line in section.splitlines():
        entry = line.lstrip()
        if not entry.startswith(("|", "- ", "* ")):
            continue  # prose, such as the "Not yet confirmed:" line
        if URL_RE.search(entry) and not DATE_RE.search(entry):
            undated += 1
    if not URL_RE.search(section):
        return ["## Sources has no URL"]
    if undated:
        return [f"{undated} source line(s) without a read date"]
    return []


def check_rates_rows_sourced(path, text, fm):
    """(c) every row of the rates table carries an official URL (``same`` inherits the row above)."""
    section = _section(text, lambda t: t.lower() == "rates, bands and thresholds")
    rows = _table_rows(section) if section else []
    where = "rates table"
    if not rows:
        where = "amount table"
        rows = [
            (h, c) for h, c in _table_rows(_body(text))
            if any(AMOUNT_COLUMN_RE.search(col) for col in h)
        ]
    if not rows:
        return ["no rates table"]
    unsourced = 0
    for _header, cells in rows:
        line = " | ".join(cells)
        if URL_RE.search(line):
            continue
        if cells and cells[-1].lower().startswith("same"):
            continue
        unsourced += 1
    if unsourced:
        return [f"{unsourced} of {len(rows)} {where} row(s) without a URL"]
    return []


def _heading_set_problems(titles, required, aliases):
    positions = []
    missing = []
    for canon in required:
        accepted = {canon} | aliases.get(canon, set())
        idx = next((i for i, t in enumerate(titles) if t in accepted), None)
        if idx is None:
            missing.append(canon)
        else:
            positions.append(idx)
    problems = []
    if missing:
        problems.append(f"missing heading(s): {', '.join(missing)}")
    if positions != sorted(positions):
        problems.append("headings out of order")
    return problems


def check_canonical_headings(path, text, fm):
    """(d) the headings are one of the two canonical sets, verbatim, in order.

    The reference set is the nine CANONICAL_HEADINGS; the method set is the six
    METHOD_HEADINGS. A skill passes if either set passes. The failure message
    reports the set it came closest to."""
    titles = [t for t, _ in _headings(text)]
    ref = _heading_set_problems(titles, CANONICAL_HEADINGS, HEADING_ALIASES)
    if not ref:
        return []
    method = _heading_set_problems(titles, METHOD_HEADINGS, METHOD_ALIASES)
    if not method:
        return []
    uses_method = "The method, step by step" in titles
    return [("method set: " if uses_method else "reference set: ") + p for p in (method if uses_method else ref)]


def check_two_oa_checks(path, text, fm):
    """(e) at least two ```oa-check blocks (the two worked examples CI recomputes)."""
    n = len(OA_CHECK_BLOCK_RE.findall(text))
    return [] if n >= 2 else [f"{n} oa-check block(s), need 2"]


def check_version_numeric(path, text, fm):
    """(f) ``version`` is present and a dotted number such as 0.1 or 2.0."""
    version = fm.get("version")
    if version is None or str(version).strip() == "":
        return ["no version"]
    if re.fullmatch(r"\d+(\.\d+)*", str(version).strip()):
        return []
    return [f"version {version!r} is not numeric"]


def _real(value):
    return bool(value) and str(value).strip().lower() not in NON_REVIEWER_MARKERS


def check_tier_honest(path, text, fm):
    """(g) ``reviewed_by`` implies ``tier: 1``; ``tier: 1`` implies ``reviewed_by`` (rule 10)."""
    tier = str(fm.get("tier") or "").strip()
    reviewed_by = _real(fm.get("reviewed_by"))
    problems = []
    if reviewed_by and tier != "1":
        problems.append(f"reviewed_by set but tier is {tier or 'missing'}")
    if tier == "1" and not reviewed_by:
        problems.append("tier 1 without reviewed_by")
    return problems


def check_reviewed_on(path, text, fm):
    """(j) a signed skill names the date it was signed (rule 10). No file carries
    ``reviewed_on`` yet, so this warns until the 184 signed files are backfilled."""
    reviewed_by = _real(fm.get("reviewed_by"))
    reviewed_on = fm.get("reviewed_on")
    if reviewed_by and (not reviewed_on or not DATE_RE.fullmatch(str(reviewed_on).strip())):
        return ["reviewed_by set but no reviewed_on (YYYY-MM-DD)"]
    return []


CTA_MARKER = "<!-- openaccountants-cta-block -->"


def check_no_em_dash(path, text, fm):
    """(h) no em dash character in the writer's text (the platform-stamped CTA block is not theirs)."""
    cut = text.find(CTA_MARKER)
    own = text if cut == -1 else text[:cut]
    n = own.count(EM_DASH)
    return [] if n == 0 else [f"{n} em dash(es)"]


def check_not_yet_confirmed(path, text, fm):
    """(i) a "Not yet confirmed" line in or after ``## Sources`` (rule 6)."""
    m = re.search(r"^##\s+(?:\d+[.):]?\s*)?Sources\s*$", text, re.MULTILINE | re.IGNORECASE)
    if not m:
        return ["no ## Sources section"]
    if re.search(r"not yet confirmed", text[m.end():], re.IGNORECASE):
        return []
    return ["no 'Not yet confirmed' line after ## Sources"]


#: (letter in the standard's list, column name, function). Order is the report order.
CHECKS = [
    ("a", "tax_year_current", check_tax_year_current),
    ("b", "sources_read_dates", check_sources_read_dates),
    ("c", "rates_rows_sourced", check_rates_rows_sourced),
    ("d", "canonical_headings", check_canonical_headings),
    ("e", "two_oa_checks", check_two_oa_checks),
    ("f", "version_numeric", check_version_numeric),
    ("g", "tier_honest", check_tier_honest),
    ("h", "no_em_dash", check_no_em_dash),
    ("i", "not_yet_confirmed", check_not_yet_confirmed),
    ("j", "reviewed_on", check_reviewed_on),
]
CHECK_NAMES = [name for _, name, _ in CHECKS]


def run_checks(path, text, frontmatter):
    """``{check_name: [problems]}`` for text already in memory."""
    return {name: func(path, text, frontmatter) for _, name, func in CHECKS}


def run_all(path):
    """Read one skill file and run every check. ``{check_name: [problems]}``."""
    full = path if os.path.isabs(path) else os.path.join(REPO_ROOT, path)
    with open(full, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    return run_checks(path, text, read_frontmatter(text))


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        print(__doc__)
        return 2
    failed = 0
    for path in argv:
        full = path if os.path.isabs(path) else os.path.join(REPO_ROOT, path)
        with open(full, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        fm = read_frontmatter(text)
        print(f"{rel_path(full)} (scope: {scope_of(full, fm)})")
        for letter, name, func in CHECKS:
            problems = func(full, text, fm)
            status = "pass" if not problems else "FAIL " + "; ".join(problems)
            print(f"  ({letter}) {name:<20} {status}")
            failed += bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
