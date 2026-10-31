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
    "US": {"PR", "VI", "GU", "AS", "MP", "PT", "ST", "AO", "MZ", "CV", "GW", "TL", "PH"},
    "DE": {"AT", "CH", "LI"},
    "NL": {"CW", "SX", "AW", "BQ"},
    "CA": {"NG"},  # CRA is also Nigeria's Consolidated Relief Allowance
}
#: Territories that lawfully cite a neighbour's law and sites.
NEIGHBOUR_TLDS = {"GG": {"uk"}, "IM": {"uk"}, "JE": {"uk"}, "GI": {"uk"}, "MC": {"fr"}, "SM": {"it"}, "VA": {"it"}, "LI": {"ch", "at"}}
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
    return rel_path(path).startswith("skills/cross-border/") or bool(
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
    links to its own site, and no other country's domain in a one-country skill."""
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
    return problems


def _jurisdiction_dir_codes():
    global _jurisdiction_dirs
    if _jurisdiction_dirs is None:
        import json
        with open(os.path.join(SCRIPTS_DIR, "data", "jurisdictions.json"), encoding="utf-8") as fh:
            _jurisdiction_dirs = {row["dir"]: row["code"] for row in json.load(fh) if row.get("dir")}
    return _jurisdiction_dirs


def check_jurisdiction_body(path, text, fm):
    """(n) path, frontmatter and body agree on the place. A US state file carrying
    another code, or a skill written in another jurisdiction's currency and
    authorities (Indiana with rupees), warns."""
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
    home = expected if state else _home(path, fm)
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


#: Warnings in both modes, outside the register. Letters follow CHECKS.
LESSON_CHECKS = [
    ("k", "read_date_evidence", check_read_date_evidence),
    ("l", "sources_columns", check_sources_columns),
    ("m", "source_hosts", check_source_hosts),
    ("n", "jurisdiction_body", check_jurisdiction_body),
    ("o", "year_matches_link", check_year_matches_link),
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
