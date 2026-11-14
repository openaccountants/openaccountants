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

import datetime
from collections import Counter
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
domains = _load("domains", "domains.py")
_build_index = _load("build_index", "build-index.py")
_coverage = _load("coverage_report", "coverage-report.py")
try:
    _check_examples = _load("check_examples", "check-examples.py")
    OA_CHECK_BLOCK_RE = _check_examples.BLOCK_RE
except Exception:  # pragma: no cover - the regex below is the same shape
    OA_CHECK_BLOCK_RE = re.compile(r"^```oa-check[ \t]*\n(.*?)^```[ \t]*$", re.MULTILINE | re.DOTALL)

#: The tax year the figures must apply to (rule 8). Bump each December.
CURRENT_TAX_YEAR = 2026

#: The seven shapes a skill may declare with ``type:`` (docs/skill-template.md, "The fixed core
#: and the seven shapes", 6 Nov 2026). The core checks apply to every shape; these settings only
#: change what the body must hold. A skill with no ``type:`` is checked exactly as before.
#:   min_examples  oa-check blocks required (check e)
#:   rates_table   True: a rates table is required (check c); False: one is optional
#:   headings      None: either canonical set (check d); a list: these headings, in order
SKILL_TYPES = {
    "situation-rules": {"min_examples": 2, "rates_table": True, "headings": None},
    "filing-howto": {"min_examples": 1, "rates_table": False, "headings": None},
    "computation": {"min_examples": 2, "rates_table": True, "headings": None},
    "decision": {"min_examples": 2, "rates_table": False, "headings": None},
    "rates-card": {"min_examples": 1, "rates_table": True, "headings": ["Rates, bands and thresholds", "Sources"]},
    "cross-country-method": {"min_examples": 1, "rates_table": False, "headings": ["The method, step by step", "Sources"]},
    "router": {"min_examples": 0, "rates_table": False, "headings": ["The method, step by step", "When to refuse or refer", "Sources"]},
}


#: A zero-example shape (router) that carries any of these headings is doing a tax skill's job,
#: so check e asks it for one example: declaring ``router`` must not dodge the example rule.
ZERO_EXAMPLE_GUARD_RE = re.compile(
    r"^##+\s*(?:\d+[.)]\s*)?(Deadlines and filing|Filing and payment|Rates, bands and thresholds|"
    r"Two worked examples that recompute|Worked examples|Worked cases|The base|The taxable base)\b",
    re.MULTILINE | re.IGNORECASE,
)


def skill_type(fm):
    """The declared shape, or None when ``type:`` is missing or not one of SKILL_TYPES."""
    value = str((fm or {}).get("type") or "").strip()
    return value if value in SKILL_TYPES else None


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
#: order; optional headings may sit between them. docs/skill-template.md line 7 lists both
#: sets; the shape test of 31 Oct 2026 measured them within noise of each other.
METHOD_HEADINGS = [
    "Scope",
    "Ask the client first",
    "The method, step by step",
    "Worked cases",
    "When to refuse or refer",
    "Sources",
]
METHOD_ALIASES = {"Scope": {"Scope and who this is for"}}

#: Skills that keep the general template (accounting packs). The checks still
#: run on them with the same fixed-core admission rules as other domains.
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
#: A cell that opens with this word marks the row unverified (rule 2). Only the
#: start of a cell counts, so "unverified payees" inside a rule is not a mark.
UNVERIFIED_MARK_RE = re.compile(r"^[\s*_`\[(]*unverified\b", re.IGNORECASE)
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
    for key in ("tax_year_notes", "reviewed_on", "version", "domain", "standard", "effective_date", "checked_on"):
        m = re.search(rf"^{key}:[ \t]*(.*)$", block, re.MULTILINE)
        if m:
            fields[key] = _build_index.clean_value(m.group(1))
    return {k: v for k, v in fields.items() if v is not None}


def admission_content_unchanged(old_text, new_text):
    """Approval-only edits may inherit legacy warnings; scope/date/shape edits may not."""
    import label_boilerplate
    if not label_boilerplate.same_content(old_text, new_text):
        return False
    old, new = read_frontmatter(old_text), read_frontmatter(new_text)
    keys = ("tax_year", "tax_year_notes", "domain", "type", "standard", "effective_date", "checked_on", "jurisdiction")
    return all(old.get(key) == new.get(key) for key in keys)


def approved_source_unchanged(old_text, new_text):
    """Professional approval binds the body and source-owned execution metadata.

    A description or stable-name repair need not inherit old body defects, but
    it still changes the version a professional approved. Credit-only changes
    remain exempt under the existing content-normalisation rules.
    """
    if not admission_content_unchanged(old_text, new_text):
        return False
    old, new = read_frontmatter(old_text), read_frontmatter(new_text)
    keys = ("name", "description", "category", "depends_on", "tags")
    return all(old.get(key) == new.get(key) for key in keys)


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


def names_a_tax(path, frontmatter):
    """True when the file name or category names a tax: a tax-domain word from
    scripts/coverage-report.py, or a word in the tax domain's ``slug_words``
    (docs/domains.yml). Such a skill is checked as tax whatever ``domain:`` says."""
    if domains_of(path, frontmatter):
        return True
    try:
        words = {str(w).lower() for w in domains.get(domains.TAX).get("slug_words") or []}
    except Exception:
        words = set()
    return bool(words & set(slug_of(path).lower().split("-")))


def applied_domain(path, frontmatter):
    """``(domain, status)``: the active non-tax domain whose rules apply (docs/domains.yml),
    or ``None`` when the skill is checked as before (tax rules). ``status`` is what
    ``domains.resolve`` said, ``website`` for a website value with none of the domain's
    date keys, or ``names-tax`` when a tax file name overrides the domain."""
    frontmatter = frontmatter or {}
    status, domain = domains.resolve(frontmatter.get("domain"))
    if status != "active" or domain["id"] == domains.TAX:
        return None, status
    if domains.is_website_value(domain["id"]) and not any(
        str(frontmatter.get(key) or "").strip() for key in domains.date_fields(domain)
    ):
        # payroll and bookkeeping are also values the website writes: a file the website
        # labelled is checked as before until it carries the domain's own date field.
        return None, "website"
    if names_a_tax(path, frontmatter):
        return None, "names-tax"
    return domain, status


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
    """(a) the skill says it is current, the way its domain dates things (docs/domains.yml).

    Tax, and every skill with no active non-tax domain: ``tax_year`` is the current
    year, or an explicit adjacent-year period in ``tax_year_notes`` starts in
    ``tax_year`` and includes the current year. A note alone cannot refresh old
    figures. Another active domain: the keys
    in its ``date_field`` are present (``standard`` and ``effective_date`` for an
    accounting or auditing standard, ``checked_on`` for the rest); a key ending in
    ``_date`` or ``_on`` is a YYYY-MM-DD date, and an ``_on`` date (the day a person
    checked it) is not in the future and not older than the domain's ``max_age_days``."""
    domain, _status = applied_domain(path, fm)
    fields = domains.date_fields(domain) if domain else ["tax_year"]
    if fields != ["tax_year"]:
        return _domain_date_problems(domain, fields, fm)
    year = fm.get("tax_year")
    if year is None or str(year).strip() == "":
        return ["no tax_year"]
    if str(year).strip() == str(CURRENT_TAX_YEAR):
        return []
    if _current_tax_period(year, fm.get("tax_year_notes")):
        return []
    if fm.get("tax_year_notes"):
        return [f"tax_year {year}: tax_year_notes must name an adjacent-year period starting in {year} and including {CURRENT_TAX_YEAR}"]
    return [f"tax_year {year} is not {CURRENT_TAX_YEAR} and no tax_year_notes"]


def _current_tax_period(year, notes):
    """Recognise fiscal labels such as 2025-26, 2025/2026 or FY 2025–2026.

    Dates of editing, provenance and a mention of a different year's figures do
    not establish the period covered. This is a label check, not a legal review.
    """
    if not str(year).isdigit():
        return False
    for match in re.finditer(r"(?<!\d)(\d{4})\s*[-–—/]\s*(\d{4}|\d{2})(?!\d)", str(notes or "")):
        start = int(match.group(1))
        end = int(match.group(2))
        if end < 100:
            end += (start // 100) * 100
            if end < start:
                end += 100
        if start == int(year) and end == start + 1 and start <= CURRENT_TAX_YEAR <= end:
            return True
    return False


def _domain_date_problems(domain, fields, fm):
    problems = []
    for key in fields:
        value = fm.get(key)
        value = "" if value is None else str(value).strip()
        if not value:
            problems.append(f"no {key} (domain {domain['id']} is dated by {' and '.join(fields)}, docs/domains.yml)")
        elif domains.is_date_key(key):
            if not DATE_RE.fullmatch(value) or not _real_date(value):
                problems.append(f"{key} {value!r} is not a YYYY-MM-DD date")
            elif key.endswith("_on") and value > _today():
                problems.append(f"{key} {value} is in the future")
            elif key.endswith("_on") and domain.get("max_age_days") is not None:
                age = (datetime.date.fromisoformat(_today()) - datetime.date.fromisoformat(value)).days
                if age > int(domain["max_age_days"]):
                    problems.append(f"{key} {value} is more than {domain['max_age_days']} days old "
                                    f"(domain {domain['id']}, max_age_days in docs/domains.yml)")
    return problems


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


def _rates_rows(text):
    """``(where, rows)``: the rates table, or failing that every amount table."""
    section = _section(text, lambda t: t.lower() == "rates, bands and thresholds")
    rows = _table_rows(section) if section else []
    if rows:
        return "rates table", rows
    return "amount table", [
        (h, c) for h, c in _table_rows(_body(text))
        if any(AMOUNT_COLUMN_RE.search(col) for col in h)
    ]


def _row_status(header, cells, previous):
    """``linked``, ``unverified`` or ``missing`` for one row.

    A cell that opens with the word ``unverified`` marks the row, and the mark
    beats a URL. ``same`` takes the status of the row above in the same table,
    so it can never lift a row above what it inherits; with nothing above it
    the row is missing."""
    if any(UNVERIFIED_MARK_RE.match(cell) for cell in cells):
        return "unverified"
    if URL_RE.search(" | ".join(cells)):
        return "linked"
    if cells and cells[-1].lower().startswith("same") and previous and previous[0] is header:
        return previous[1]
    return "missing"


def rates_row_counts(text):
    """Row counts for the rates table: total, linked, unverified, missing, and
    ``linked_pct`` and ``unverified_pct`` (of total; ``None`` with no rows)."""
    where, rows = _rates_rows(text)
    counts = {"linked": 0, "unverified": 0, "missing": 0}
    previous = None
    for header, cells in rows:
        status = _row_status(header, cells, previous)
        counts[status] += 1
        previous = (header, status)
    total = len(rows)
    return {
        "where": where,
        "total": total,
        "linked_pct": round(100 * counts["linked"] / total, 1) if total else None,
        "unverified_pct": round(100 * counts["unverified"] / total, 1) if total else None,
        **counts,
    }


def check_rates_rows_sourced(path, text, fm):
    """(c) every row of the rates table is linked to an official URL (``same``
    inherits the row above) and confirmed. An unverified row stays visible in audit counts but fails as guidance."""
    c = rates_row_counts(text)
    if not c["total"]:
        shape = skill_type(fm)
        if shape and not SKILL_TYPES[shape]["rates_table"]:
            return []
        domain, _status = applied_domain(path, fm)
        if domain and domain.get("rates_table") == "optional":
            return []
        return ["no rates table"]
    problems = []
    if c["missing"]:
        problems.append(
            f"{c['missing']} of {c['total']} {c['where']} row(s) without a URL or an unverified mark "
            f"({c['linked_pct']:g}% linked, {c['unverified_pct']:g}% unverified)"
        )
    if c["unverified"]:
        problems.append(f"{c['unverified']} unverified {c['where']} row(s); remove from usable guidance and list under Sources: Not yet confirmed")
    return problems


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
    shape = skill_type(fm)
    if shape and SKILL_TYPES[shape]["headings"]:
        own = _heading_set_problems(titles, SKILL_TYPES[shape]["headings"], HEADING_ALIASES)
        return [f"{shape} set: " + p for p in own]
    ref = _heading_set_problems(titles, CANONICAL_HEADINGS, HEADING_ALIASES)
    if not ref:
        return []
    method = _heading_set_problems(titles, METHOD_HEADINGS, METHOD_ALIASES)
    if not method:
        return []
    uses_method = "The method, step by step" in titles
    return [("method set: " if uses_method else "reference set: ") + p for p in (method if uses_method else ref)]


def required_example_count(text, fm):
    """The shape's example requirement, shared by admission and arithmetic CLI."""
    shape = skill_type(fm)
    need = SKILL_TYPES[shape]["min_examples"] if shape else 2
    if need == 0 and ZERO_EXAMPLE_GUARD_RE.search(text):
        need = 1
    return need


def check_two_oa_checks(path, text, fm):
    """(e) enough ```oa-check blocks (worked examples CI recomputes): two, or the number the
    declared ``type:`` sets in SKILL_TYPES."""
    need = required_example_count(text, fm)
    n = len(OA_CHECK_BLOCK_RE.findall(text))
    return [] if n >= need else [f"{n} oa-check block(s), need {need}"]


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
    """(j) a signed skill names a real, non-future approval date (rule 11).
    Blocks an invalid approval in PR mode, including metadata-only approval."""
    reviewed_by = _real(fm.get("reviewed_by"))
    reviewed_on = fm.get("reviewed_on")
    if reviewed_by:
        value = str(reviewed_on or "").strip()
        if not DATE_RE.fullmatch(value) or not _real_date(value):
            return ["reviewed_by set but no valid reviewed_on (YYYY-MM-DD)"]
        if value > _today():
            return [f"reviewed_on {value} is in the future"]
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


# ---------------------------------------------------------------------------
# Reviewer lessons: findings second readers kept repeating, as warnings. They run
# from validate-guides.py but stay out of CHECKS, so REGISTER.csv and its "pass
# all" number keep their meaning. All offline: check_year_matches_link reads
# the URL and the row, never the page.
# ---------------------------------------------------------------------------

#: At least this many dated source rows, all one date, is a bulk stamp.
BULK_DATE_MIN_ROWS = 6
#: A date in the last cell of a row, or straight after the word "read".
READ_ON_RE = re.compile(r"(?:\|\s*|\bread(?:\s+on)?\s+)(\d{4}-\d{2}-\d{2})\b", re.IGNORECASE)
#: A status code proves a server answered, not that anyone read the page.
STATUS_ONLY_RE = re.compile(r"\b(?:http|status)\s*(?:code\s*)?200\b", re.IGNORECASE)
#: A date cell may honestly say the page failed instead of giving a read date.
NOT_READ_NOTE_RE = re.compile(r"not read|not relied|could not|refused|timed out|\b40[34]\b|tried|n/a|none", re.IGNORECASE)
READ_SCOPE_RE = re.compile(
    r"\bart(?:icle)?s?\.?\s*\d|§|\bs(?:ec(?:tion)?)?s?\.?\s*\d|\bclauses?\b|\bbox\b|\bpart\b|\bread\s+(?:for|in)\b",
    re.IGNORECASE,
)
CROSS_BORDER_RE = re.compile(
    r"cross-border|cross_border|treaty|non-?resident|expat|foreign|migration|"
    r"exit-tax|-to-|withholding|transfer-pricing|fbar|fatca|dac\d|oss|pillar",
    re.IGNORECASE,
)
FOREIGN_LAW_ROW_RE = re.compile(r"treaty|convention|directive|protocol|DTA|DTT|OECD|EU\b", re.IGNORECASE)
#: Hosts rule 1 bars as a citation.
SECONDARY_HOSTS = (
    "pwc.com", "kpmg.com", "deloitte.com", "ey.com", "taxsummaries.pwc.com",
    "avalara.com", "taxfoundation.org", "wikipedia.org",
)
#: A name in the row, and the host that name publishes on.
AUTHORITY_HOSTS = {
    r"\bIRS\b": ("irs.gov", "govinfo.gov", "congress.gov", "cornell.edu"),
    r"\bHMRC\b": ("gov.uk",),
    r"\bATO\b": ("ato.gov.au",),
    r"\bCRA\b": ("canada.ca", "cra-arc.gc.ca", "gc.ca"),
    r"\bSARS\b": ("sars.gov.za", "gov.za"),
    r"\bIRAS\b": ("iras.gov.sg",),
    r"\bMTCA\b": ("cfr.gov.mt", "mtca.gov.mt", "gov.mt"),
    r"\bELSTER\b": ("elster.de",),
    r"\bBelastingdienst\b": ("belastingdienst.nl", "overheid.nl"),
    r"\bEUR-Lex\b": ("europa.eu",),
}
#: Currency and authority words that belong to one jurisdiction family.
JURISDICTION_TERMS = {
    "IN": [r"₹", r"\brupees?\b", r"\blakhs?\b", r"\bcrores?\b", r"\bCBDT\b", r"\bGSTN\b"],
    "US": [r"\bIRS\b", r"\bInternal Revenue Code\b"],
    "GB": [r"£", r"\bHMRC\b"],
    "AU": [r"\bATO\b", r"\bBAS\b"],
    "CA": [r"\bCRA\b"],
    "ZA": [r"\bSARS\b"],
    "SG": [r"\bIRAS\b"],
    "MT": [r"\bMTCA\b"],
    "DE": [r"\bFinanzamt\b", r"\bELSTER\b"],
    "IT": [r"\bAgenzia delle Entrate\b"],
    "ES": [r"\bAgencia Tributaria\b", r"\bAEAT\b"],
    "FR": [r"\bDGFiP\b"],
    "NL": [r"\bBelastingdienst\b"],
    "NG": [r"₦", r"\bFIRS\b"],
    "KE": [r"\bKRA\b"],
    "PK": [r"\bFBR\b"],
    "SA": [r"\bZATCA\b"],
    "BR": [r"R\$", r"\bReceita Federal\b"],
    "PH": [r"₱"],
    "IL": [r"₪"],
    "KR": [r"₩"],
}
#: Other jurisdictions where a family's words are at home.
TERM_SHARED_WITH = {
    "IN": {"PK", "LK", "NP", "MU", "SC", "BD", "MV", "BT"},  # rupee, lakh and crore
    "GB": {"GG", "JE", "IM", "GI", "FK", "SH"},  # pound, HMRC links
    # IRS is also the Portuguese personal income tax.
    "US": {"PR", "VI", "GU", "AS", "MP", "UM", "PT", "ST", "AO", "MZ", "CV", "GW", "TL", "PH"},
    "DE": {"AT", "CH", "LI"},
    "NL": {"CW", "SX", "AW", "BQ"},
    "CA": {"NG"},  # CRA is also Nigeria's Consolidated Relief Allowance
    "FR": {"GF"},  # French Guiana uses French tax law and DGFiP
    "AU": {"CX", "CC"},  # Christmas Island and Cocos (Keeling) Islands: Australian external territories, ATO
}
#: Territories that lawfully cite a neighbour's law and sites.
#: Christmas Island and the Cocos (Keeling) Islands cite Australian Commonwealth sites (legislation.gov.au, ato.gov.au),
#: and the Cook Islands, in free association with New Zealand, cite New Zealand dates its law adopts (govt.nz).
#: French overseas territories, the Pacific collectivities (NC, PF, WF) included, cite French state
#: sites (legifrance, impots.gouv, douane, the Wallis and Futuna prefecture at wallis-et-futuna.gouv.fr), and
#: Sint Maarten, Curacao and Aruba cite Dutch ones (overheid.nl) for Kingdom law.
NEIGHBOUR_TLDS = {"CX": {"au"}, "CC": {"au"}, "CK": {"nz"}, "GF": {"fr"}, "GP": {"fr"}, "MQ": {"fr"}, "RE": {"fr"}, "YT": {"fr"}, "MF": {"fr"}, "BL": {"fr"}, "PM": {"fr"}, "NC": {"fr"}, "PF": {"fr"}, "WF": {"fr"}, "SX": {"nl"}, "CW": {"nl"}, "AW": {"nl"}, "GG": {"uk"}, "IM": {"uk"}, "JE": {"uk"}, "GI": {"uk"}, "MC": {"fr"}, "SM": {"it"}, "VA": {"it"}, "LI": {"ch", "at"}, "SJ": {"no"}}
#: Jurisdiction values that name no single place.
NON_PLACE_JURISDICTIONS = {"", "GLOBAL", "INTL", "GENERAL", "EU", "EU-27", "EU/EEA/CH/UK", "?"}
#: Two-letter endings that say nothing about a country.
GENERIC_TLDS = {"io", "ai", "co", "me", "tv", "eu", "cc", "fm", "ly", "to", "gg", "im", "ws"}
YEAR_RE = re.compile(r"\b(20\d{2})\b")
URL_TAX_YEAR_RE = re.compile(
    r"(?:tax[-_]?years?|taxyear|tax[-_]?rates?|rates?|tables?|thresholds?|brackets?|income|allowances?)[-_/]*(20\d{2})(?:[-_/](?:20)?(\d{2}))?",
    re.IGNORECASE,
)
_jurisdiction_dirs = None


def _source_entries(text):
    """(line, url list) for each table row or list item in ``## Sources`` with a URL."""
    section = _section(text, lambda t: t.lower() == "sources")
    entries = []
    for line in section.splitlines():
        entry = line.lstrip()
        if entry.startswith(("|", "- ", "* ")) and URL_RE.search(entry):
            entries.append((entry, URL_RE.findall(entry)))
    return entries


def _host(url):
    m = re.match(r"https?://([^/:?#]+)", url)
    return m.group(1).lower() if m else ""


def _host_is(host, domain):
    return host == domain or host.endswith("." + domain)


def _is_cross_border(path, fm):
    return rel_path(path).startswith("skills/global/cross-border/") or bool(
        CROSS_BORDER_RE.search(slug_of(path) + " " + str(fm.get("category") or ""))
    )


def _home(path, fm):
    """Upper-case jurisdiction code from the frontmatter, '' when it names no one place."""
    code = str(fm.get("jurisdiction") or "").strip().upper()
    return "" if code in NON_PLACE_JURISDICTIONS else code


def check_read_date_evidence(path, text, fm):
    """(k) a read date stands for a page read: no future date, no date resting on
    a status code, and no one-day stamp over a whole table whose rows do not say
    what was read. A row that says the page failed is honest and passes."""
    entries = _source_entries(text)
    problems = []
    today = _today()
    future = sorted({
        d for line, _ in entries for d in READ_ON_RE.findall(URL_RE.sub("", line))
        if d > today and _real_date(d)
    })
    if future:
        problems.append(f"read date in the future: {', '.join(future[:3])}")
    status_only = sum(
        1 for line, _ in entries
        if STATUS_ONLY_RE.search(line) and "not read" not in line.lower()
    )
    if status_only:
        problems.append(f"{status_only} source row(s) dated on a status code alone")
    dated = [DATE_RE.findall(URL_RE.sub("", line)) for line, _ in entries]
    dated = [d for d in dated if d]
    days = {d[-1] for d in dated}
    if len(dated) >= BULK_DATE_MIN_ROWS and len(days) == 1:
        scoped = sum(1 for line, _ in entries if READ_SCOPE_RE.search(URL_RE.sub("", line)))
        if scoped * 2 < len(dated):
            problems.append(f"{len(dated)} source rows all dated {days.pop()}, most not saying what was read")
    return problems


def _today():
    return datetime.date.today().isoformat()


def _real_date(value):
    try:
        datetime.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def check_sources_columns(path, text, fm):
    """(l) each Sources table column holds what its header says: URLs under URL,
    dates under the date column. Misfilled rows shift a citation onto the wrong figure."""
    section = _section(text, lambda t: t.lower() == "sources")
    misfilled = 0
    for header, cells in _table_rows(section):
        if len(cells) != len(header):
            misfilled += 1
            continue
        for name, cell in zip(header, cells):
            label = name.lower()
            if label in ("url", "link", "official url") and not URL_RE.search(cell) and "][" not in cell:
                if not NOT_READ_NOTE_RE.search(cell) and not cell.lower().startswith("same"):
                    misfilled += 1
                    break
            if label in ("read", "read on", "date read", "read date") and not DATE_RE.search(cell) and not NOT_READ_NOTE_RE.search(cell):
                misfilled += 1
                break
    return [f"{misfilled} Sources row(s) with a misfilled column"] if misfilled else []


def check_source_hosts(path, text, fm):
    """(m) the URL host fits the row: no barred secondary host, a named authority
    links to its own site, and no other country's domain in a one-country skill.
    A skill in an active non-tax domain (docs/domains.yml) also cites only that
    domain's official hosts; a tax skill is checked exactly as before."""
    home = _home(path, fm)
    home_tld = {"GB": "uk"}.get(home.split("-")[0], home.split("-")[0].lower())
    cross_border = _is_cross_border(path, fm)
    secondary, wrong_authority, foreign = [], [], []
    for line, urls in _source_entries(text):
        hosts = [_host(u) for u in urls]
        label = URL_RE.sub("", line)
        secondary += [h for h in hosts if any(_host_is(h, d) for d in SECONDARY_HOSTS)]
        for pattern, owners in AUTHORITY_HOSTS.items():
            shared = home.split("-")[0] in TERM_SHARED_WITH["US"]
            if len(hosts) == 1 and re.search(pattern, label) and not shared and not any(_host_is(hosts[0], d) for d in owners):
                wrong_authority.append(hosts[0])
        if home and not cross_border and not FOREIGN_LAW_ROW_RE.search(label):
            for host in hosts:
                tld = host.rsplit(".", 1)[-1]
                if len(tld) == 2 and tld not in GENERIC_TLDS | NEIGHBOUR_TLDS.get(home, set()) | {home_tld}:
                    foreign.append(host)
    problems = []
    if secondary:
        problems.append(f"secondary host cited: {', '.join(sorted(set(secondary))[:3])}")
    if wrong_authority:
        problems.append(f"row names an authority but links elsewhere: {', '.join(sorted(set(wrong_authority))[:3])}")
    if foreign:
        problems.append(f"another country's domain: {', '.join(sorted(set(foreign))[:3])}")
    domain, _status = applied_domain(path, fm)
    if domain:
        unofficial = sorted({
            host for _line, urls in _source_entries(text) for host in map(_host, urls)
            if host and not domains.host_is_official(host, domain["id"])
        })
        if unofficial:
            problems.append(
                f"not an official source for domain {domain['id']} (docs/domains.yml): {', '.join(unofficial[:3])}"
            )
    return problems


def source_evidence_regressions(old_text, new_text, path=None, fm=None):
    """Objective new source defects only; unchanged legacy defects stay advisory.

    Inherited ``same`` rows retain the source status above them. Unknown official
    hosts and inferred library matches remain advisory, not automatic vetoes.
    """
    def defects(text):
        found = Counter()
        previous = None
        for header, cells in _rates_rows(text)[1]:
            status = _row_status(header, cells, previous)
            if status == "unverified":
                found["unverified figure in usable guidance; move to Sources: Not yet confirmed: " + " | ".join(cells)] += 1
            elif status == "missing":
                found["rate row without a source URL or unverified mark: " + " | ".join(cells)] += 1
            previous = (header, status)
        for line, urls in _source_entries(text):
            barred = sorted({_host(url) for url in urls if any(_host_is(_host(url), host) for host in SECONDARY_HOSTS)})
            if barred:
                found["secondary source citation: " + line.strip()] += 1
            context = read_frontmatter(text) or fm
            domain = applied_domain(path, context)[0] if path is not None else None
            if domain:
                unofficial = sorted({_host(url) for url in urls
                                     if _host(url) and not domains.host_is_official(_host(url), domain["id"])})
                if unofficial:
                    found[f"not an official source for domain {domain['id']}: " + line.strip()] += 1
        return found
    return list((defects(new_text) - defects(old_text)).elements())


def _jurisdiction_dir_codes():
    global _jurisdiction_dirs
    if _jurisdiction_dirs is None:
        import json
        with open(os.path.join(SCRIPTS_DIR, "data", "jurisdictions.json"), encoding="utf-8") as fh:
            _jurisdiction_dirs = {row["dir"]: row["code"] for row in json.load(fh) if row.get("dir")}
    return _jurisdiction_dirs


def check_jurisdiction_path(path, text, fm):
    """An explicit country/state path must agree with the declared jurisdiction.

    Unlike body-language heuristics, this is an objective identity check.
    """
    code = str(fm.get("jurisdiction") or "").strip().upper()
    rel = rel_path(path)
    problems = []
    state = re.match(r"skills/us/states/([a-z]{2})/", rel)
    if state:
        expected = "US-" + state.group(1).upper()
        if code not in (expected, "US"):
            problems.append(f"path says {expected}, frontmatter says {code or 'nothing'}")
    else:
        folder = "/".join(rel.split("/")[:2])
        expected = _jurisdiction_dir_codes().get(folder)
        if expected and code and code not in NON_PLACE_JURISDICTIONS and code.split("-")[0] != expected:
            problems.append(f"path says {expected}, frontmatter says {code}")
    return problems


def check_jurisdiction_body(path, text, fm):
    """(n) Warn when body currency/authority terms contradict the stated place."""
    rel = rel_path(path)
    state = re.match(r"skills/us/states/([a-z]{2})/", rel)
    problems = check_jurisdiction_path(path, text, fm)
    home = "US-" + state.group(1).upper() if state else _home(path, fm)
    if not home or home in NON_PLACE_JURISDICTIONS or _is_cross_border(path, fm):
        return problems
    family = home.split("-")[0]
    cut = text.find(CTA_MARKER)
    body = _body(text if cut == -1 else text[:cut])
    sources = re.search(r"^##\s+(?:\d+[.):]?\s*)?Sources\s*$", body, re.MULTILINE | re.IGNORECASE)
    if sources:
        body = body[: sources.start()]
    body = re.sub(r"\]\([^)]*\)|https?://\S+", "", FENCE_RE.sub("", body))
    count = lambda terms: sum(len(re.findall(t, body)) for t in terms)
    own = count(JURISDICTION_TERMS.get(family, []))
    for owner, terms in JURISDICTION_TERMS.items():
        if owner == family or family in TERM_SHARED_WITH.get(owner, ()):
            continue
        hits = count(terms)
        if hits >= 5 and hits > own * 2:
            problems.append(f"jurisdiction {home} but {hits} {owner} currency or authority terms against {own} of its own")
    return problems


def check_year_matches_link(path, text, fm):
    """(o) a row tagged with a tax year does not link a page whose address names
    an earlier one. Reads the URL only; the page itself is the reviewer's job."""
    rates = _section(text, lambda t: t.lower() == "rates, bands and thresholds")
    rows = [" | ".join(cells) for _, cells in _table_rows(rates)] + [line for line, _ in _source_entries(text)]
    file_year = str(fm.get("tax_year") or "").strip()
    stale = set()
    for row in rows:
        label = URL_RE.sub("", row)
        label = DATE_RE.sub("", label)
        tags = set(YEAR_RE.findall(label))
        if not tags:
            continue
        for url in URL_RE.findall(row):
            for m in URL_TAX_YEAR_RE.finditer(url):
                linked = {m.group(1)}
                if m.group(2):
                    linked.add(m.group(1)[:2] + m.group(2))
                if not linked & tags and max(tags) > max(linked) and (not file_year or file_year in tags):
                    stale.add(f"row {max(tags)} links {m.group(1)}")
    return [f"{len(stale)} row year(s) differ from the linked page: {'; '.join(sorted(stale)[:3])}"] if stale else []


#: Stamped on every skill: not an item of the loser.
BOILERPLATE_HEADINGS = {"talk to a verified accountant", "disclaimer"}


def merge_record_problems(loser_slug, loser_text, pr_body):
    """(errors, warnings) for one skill a PR deletes. The PR body carries ``## Moved``
    and ``## Not moved`` tables that name the loser's items (line 5)."""
    tables = {}
    for m in re.finditer(r"^##\s+(Moved|Not moved)\s*$(.*?)(?=^##\s|\Z)", pr_body, re.MULTILINE | re.DOTALL | re.IGNORECASE):
        tables[m.group(1).lower()] = m.group(2)
    errors = []
    if loser_slug not in pr_body:
        errors.append(f"{loser_slug} deleted but the PR body does not name it")
    for name in ("moved", "not moved"):
        if name not in tables:
            errors.append(f"{loser_slug} deleted but the PR body has no '## {name.capitalize()}' section")
        elif name == "moved" and not _table_rows(tables[name]) and not re.search(r"\bnone\b|\bnothing\b", tables[name], re.IGNORECASE):
            errors.append(f"{loser_slug}: '## Moved' lists no item")
    if errors:
        return errors, []
    record = " ".join(tables.values()).lower()
    words = lambda s: set(re.findall(r"[^\W\d_]{4,}", s.lower()))
    unlisted = []
    for title, _ in _headings(_body(loser_text)):
        wanted = words(title)
        if wanted and title.lower() not in BOILERPLATE_HEADINGS and not wanted & words(record):
            unlisted.append(title)
    warnings = [f"{loser_slug}: heading(s) not in Moved or Not moved: {', '.join(unlisted[:5])}"] if unlisted else []
    return [], warnings


def check_type_declared(path, text, fm):
    """(p) ``type:`` names one of the seven shapes, so the body is checked against its own job."""
    value = str((fm or {}).get("type") or "").strip()
    if not value:
        return ["no type: declared (one of " + ", ".join(SKILL_TYPES) + ")"]
    if value not in SKILL_TYPES:
        return [f"type {value!r} is not one of " + ", ".join(SKILL_TYPES)]
    return []


# ---------------------------------------------------------------------------
# The library (check q): library/<folder>/figures.json holds each figure once,
# proven by a verbatim quote on its official page (scripts/build-library.py).
# A skill's rates rows should state those figures. Warning only, and kept
# conservative: a row is compared with a library figure only when the match is
# plain (see check_figure_in_library), so a warning means "look at this row".
# ---------------------------------------------------------------------------

#: Where scripts/build-library.py writes: library/<folder under skills/>/figures.json.
LIBRARY_DIR = os.path.join(REPO_ROOT, "library")
_library_cache = {}
#: Share of the row label's words that must appear in the figure's item text.
LIBRARY_LABEL_SHARE = 0.6
LIBRARY_STOP_WORDS = {
    "this", "that", "with", "from", "than", "they", "their", "there", "which", "where", "when",
    "what", "will", "would", "shall", "must", "have", "been", "only", "also", "each", "other",
    "into", "over", "under", "above", "below", "more", "less", "same", "year", "years",
}
#: A number in a row, with an optional scale word ("EUR 1.5 million").
LIBRARY_NUMBER_RE = re.compile(
    r"(?<![\d.,])(\d+(?:[.,]\d+)*)(?:\s*(million|billion|thousand|lakh|crore|bn|m)\b|(?!\w)(?![.,]\d))",
    re.IGNORECASE,
)
#: The value shapes the implicit match compares: "EUR 1,270", "INR 20 lakh", "4.2%".
LIBRARY_VALUE_RE = re.compile(r"(?:([A-Z]{3}) )?(\d+(?:[.,]\d+)*)(?: (million|billion|thousand|lakh|crore))?(%?)")
LIBRARY_SCALE = {"million": 1e6, "m": 1e6, "billion": 1e9, "bn": 1e9, "thousand": 1e3, "lakh": 1e5, "crore": 1e7}
LIBRARY_ID_RE = re.compile(r"\b[a-z]{2}(?:\.[a-z0-9_-]+)+")
#: An announced figure (status set, not yet law) has the id of the figure in force
#: plus this suffix; a row stating either value of the pair passes (build-library.py).
LIBRARY_ANNOUNCED_SUFFIX = ".announced"
YEAR_IN_TEXT_RE = re.compile(r"\b(20\d{2})\b")


def value_in_text(value, text):
    """True when ``value`` appears in ``text`` exactly, as a whole figure: ``EUR 1,000``
    is not found in ``EUR 1,000,000`` and ``5%`` is not found in ``5.5%``."""
    value = str(value).strip()
    if not value:
        return False
    pre = r"(?<!\w)(?<!\d[.,])" if value[0].isalnum() else ""
    post = r"(?![\w%])(?![.,]\d)" if value[-1].isalnum() else ""
    return re.search(pre + re.escape(value) + post, text) is not None


def library_folder(path):
    """``ireland`` for skills/ireland/x.md, ``us/federal`` for skills/us/federal/x.md, else None."""
    parts = rel_path(path).split("/")
    if len(parts) < 3 or parts[0] != "skills":
        return None
    return "/".join(parts[1:-1])


def _words(text):
    return re.findall(r"[^\W_]+", str(text).lower())


def _numbers(text):
    """Every number in ``text`` as floats, read with English separators; a scale word
    adds the scaled number, and ``1.000`` (a European thousands point) adds 1000 too."""
    out = set()
    for m in LIBRARY_NUMBER_RE.finditer(text):
        raw = m.group(1)
        try:
            number = float(raw.replace(",", ""))
        except ValueError:
            continue
        out.add(number)
        if m.group(2):
            out.add(number * LIBRARY_SCALE[m.group(2).lower()])
        if re.fullmatch(r"\d{1,3}(?:\.\d{3})+", raw):
            out.add(float(raw.replace(".", "")))
    return out


def _value_unit(value):
    """``EUR``, ``%`` or None (a value the implicit match does not compare)."""
    m = LIBRARY_VALUE_RE.fullmatch(str(value).strip())
    if not m or bool(m.group(1)) == bool(m.group(4)):
        return None
    return m.group(1) or "%"


def _unit_count(unit, text):
    if unit == "%":
        return len(re.findall(r"\d\s?%", text))
    return len(re.findall(rf"\b{unit}\s?\d", text))


def _norm_url(url):
    url = url.strip().rstrip(".,;:'\"`*_").split("#")[0]
    return re.sub(r"^https?://(?:www\.)?", "", url, flags=re.IGNORECASE).rstrip("/").lower()


def library_figures(folder):
    """The prepared library for one folder (``None`` when it has no figures.json)."""
    key = (LIBRARY_DIR, folder)
    if key not in _library_cache:
        import json
        path = os.path.join(LIBRARY_DIR, *folder.split("/"), "figures.json")
        lib = None
        if folder and os.path.isfile(path):
            with open(path, encoding="utf-8") as fh:
                figures = json.load(fh).get("figures", [])
            for fig in figures:
                tail = fig["id"].split(".", 1)[-1]
                fig["_id_words"] = [w for w in re.split(r"[.\-_]", tail.lower()) if w]
                fig["_item_words"] = set(_words(fig.get("item", "")))
                fig["_unit"] = _value_unit(fig["value"])
                fig["_numbers"] = _numbers(fig["value"])
                fig["_url"] = _norm_url(fig.get("source_url", ""))
            by_id = {f["id"]: f for f in figures}
            for fig in figures:
                partner = (fig["id"][: -len(LIBRARY_ANNOUNCED_SUFFIX)]
                           if fig["id"].endswith(LIBRARY_ANNOUNCED_SUFFIX)
                           else fig["id"] + LIBRARY_ANNOUNCED_SUFFIX)
                fig["_partners"] = [by_id[partner]] if partner in by_id else []
            lib = {"figures": figures, "by_id": by_id}
        _library_cache[key] = lib
    return _library_cache[key]


def _covers(needed, have):
    """Every word in ``needed`` is in ``have`` (a word of 4+ letters may be a prefix: profit, profits)."""
    return all(any(h == w or (len(w) >= 4 and h.startswith(w)) for h in have) for w in needed)


def _label_share(label, item_words):
    words = [w for w in _words(label) if len(w) >= 4 and w.isalpha() and w not in LIBRARY_STOP_WORDS]
    if not words:
        return 0.0
    hit = sum(1 for w in words if any(i == w or (len(i) >= 4 and (w.startswith(i) or i.startswith(w))) for i in item_words))
    return hit / len(words)


def _same_year(row_years, fig):
    """False only when the row and the figure both name years and share none."""
    fig_years = set(YEAR_IN_TEXT_RE.findall(str(fig.get("tax_year", ""))))
    return not fig_years or bool(row_years & fig_years)


def check_figure_in_library(path, text, fm):
    """(q) where library/<folder>/figures.json exists, a rates row does not state a
    different number for a figure the library holds. Warning only.

    Explicit match: a row that names a library id (``ie.cgt.exemption.personal``) must
    hold that figure's value exactly, character for character.

    Implicit match, all of: the row links the figure's ``source_url`` (``same`` takes
    the URL of the row above); every word of the id after the country prefix is in
    the row or the skill's file name; at least 60% of the words of the row's first
    cell are in the figure's ``item``; the value is a currency amount or a percentage
    and the row states exactly one amount of that unit. The row passes when any number
    in it equals a matched figure, or any figure the library read on the same page
    (``4.20%`` equals ``4.2%``). A row whose years are all different from the figure's
    tax year is about another year and is skipped. Otherwise it warns, naming the most
    specific matched figure (the longest id).

    Announced figures: where the library holds both a figure in force and its
    announced change (same id plus ``.announced``, with a ``status``), a row stating
    either value passes, in both the explicit and the implicit match."""
    folder = library_folder(path)
    lib = library_figures(folder) if folder else None
    if not lib:
        return []
    slug_words = set(_words(slug_of(path)))
    found = []
    previous = None
    for header, cells in _rates_rows(text)[1]:
        row = " | ".join(cells)
        urls = URL_RE.findall(row)
        if not urls and previous and previous[0] is header and any(c.lower().startswith("same") for c in cells):
            urls = previous[1]
        previous = (header, urls)
        plain = re.sub(r"\]\([^)]*\)", "] ", URL_RE.sub(" ", row))
        named = [lib["by_id"][i] for i in LIBRARY_ID_RE.findall(plain) if i in lib["by_id"]]
        if named:
            for fig in named:
                if not any(value_in_text(f["value"], plain) for f in [fig, *fig["_partners"]]):
                    found.append(f"row names {fig['id']} but does not state {fig['value']}")
            continue
        page_urls = {_norm_url(u) for u in urls}
        if not page_urls:
            continue
        context = set(_words(plain)) | slug_words
        page = [f for f in lib["figures"] if f["_url"] in page_urls]
        matched = [
            f for f in page
            if f["_unit"] and _unit_count(f["_unit"], plain) == 1
            and _covers(f["_id_words"], context)
            and _label_share(cells[0] if cells else "", f["_item_words"]) >= LIBRARY_LABEL_SHARE
        ]
        if not matched:
            continue
        row_numbers = _numbers(plain)
        if any(f["_numbers"] & row_numbers for f in page if f["_unit"]):  # matched is part of page
            continue
        if any(p["_numbers"] & row_numbers for f in matched for p in f["_partners"]):
            continue
        row_years = set(YEAR_IN_TEXT_RE.findall(DATE_RE.sub("", plain)))
        if row_years:
            matched = [f for f in matched if _same_year(row_years, f)]
        if not matched:
            continue
        longest = max(len(f["_id_words"]) for f in matched)
        top = [f for f in matched if len(f["_id_words"]) == longest]
        if len({f["value"] for f in top}) != 1:
            continue
        label = re.sub(r"\s+", " ", cells[0])[:60] if cells else ""
        found.append(f"'{label}' differs from {top[0]['id']} ({top[0]['value']})")
    if not found:
        return []
    return [f"{len(found)} rates row(s) differ from library/{folder}/figures.json: " + "; ".join(found[:3])]


def check_domain_known(path, text, fm):
    """(r) a ``domain:`` value is an active domain in docs/domains.yml (or a value the
    website writes). Anything else warns and the skill is checked as before."""
    value = str((fm or {}).get("domain") or "").strip()
    status, _domain = domains.resolve(value)
    if status == "unknown":
        return [f"domain {value!r} is not in docs/domains.yml: propose it there "
                f"(open an issue \"Propose a domain: {value}\"); checked as before until then"]
    if status == "proposed":
        return [f"domain {value!r} is proposed, not active, in docs/domains.yml: checked as before until it is active"]
    if status == "unreadable":
        return ["docs/domains.yml could not be read: checked as before"]
    if applied_domain(path, fm)[1] == "names-tax":
        return [f"the file name names a tax, so it is checked as tax whatever domain {value!r} says"]
    return []


#: Outside the register. Heuristics warn in both modes; explicit path identity
#: is blocking on changed skills. Letters follow CHECKS.
LESSON_CHECKS = [
    ("k", "read_date_evidence", check_read_date_evidence),
    ("l", "sources_columns", check_sources_columns),
    ("m", "source_hosts", check_source_hosts),
    ("n", "jurisdiction_body", check_jurisdiction_body),
    ("o", "year_matches_link", check_year_matches_link),
    ("p", "type_declared", check_type_declared),
    ("q", "figure_in_library", check_figure_in_library),
    ("r", "domain_known", check_domain_known),
    ("s", "jurisdiction_path", check_jurisdiction_path),
]

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
    return {name: func(path, text, frontmatter) for _, name, func in CHECKS + LESSON_CHECKS}


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
        for letter, name, func in CHECKS + LESSON_CHECKS:
            problems = func(full, text, fm)
            status = "pass" if not problems else "FAIL " + "; ".join(problems)
            print(f"  ({letter}) {name:<20} {status}")
            failed += bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
