"""
OpenAccountants MCP server.

Exposes read-only tools and guided-workflow prompts that let an MCP client
(Claude Desktop, Cursor, etc.) discover, search, and read tax-skill content
from the bundled ``packages/`` tree.

This mirrors the tool/prompt surface of the hosted server at
``https://www.openaccountants.com/api/mcp`` so both stay in sync:

    Tools    list_skills, get_skill, get_skill_sections, search_skills
    Prompts  skill-review, tax-return, vat-check, find-deductions,
             skill-feedback, compare-jurisdictions

Where the hosted server reads from the OpenAccountants database, this one
reads the open-source markdown packages on disk, so results reflect whatever
checkout you point it at.

Environment
-----------
OPENACCOUNTANTS_ROOT      Path to the repo checkout.  Defaults to two directories
                          above this file (i.e. the repo root when this package
                          lives at ``mcp/openaccountants_mcp/``).
MCP_TRANSPORT             ``stdio`` (default), ``streamable-http``, or ``sse``.
                          HTTP transports let remote MCP clients connect via a
                          reverse proxy (Caddy, nginx, ngrok…).
MCP_HOST                  Bind host for HTTP transports.  Defaults to
                          ``127.0.0.1``.  Set this explicitly (for example,
                          ``MCP_HOST=0.0.0.0``) only when a reverse proxy or
                          other network boundary is intentionally exposing it.
MCP_PORT                  Bind port for HTTP transports.  Defaults to ``8000``.
MCP_STREAMABLE_HTTP_PATH  Path the Streamable-HTTP endpoint is mounted at.
                          Defaults to ``/mcp``.  Set to ``/`` when fronted by a
                          reverse proxy that strips the upstream path prefix.
"""

from __future__ import annotations

import logging
import os
import re
from hashlib import sha256
from collections import Counter, defaultdict
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

import yaml
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Resolve repo root + packages directory
# ---------------------------------------------------------------------------

_DEFAULT_ROOT = Path(__file__).resolve().parents[2]  # mcp/openaccountants_mcp/ -> mcp/ -> repo
REPO_ROOT = Path(os.environ.get("OPENACCOUNTANTS_ROOT", str(_DEFAULT_ROOT))).resolve()
PACKAGES_DIR = REPO_ROOT / "packages"

MAX_FILE_BYTES = 2 * 1024 * 1024  # 2 MB safety cap
SEARCH_LIMIT = 25
SOURCE_BASE = "https://openaccountants.com/skills"

# Feedback flows construct a GitHub New Issue URL the user opens themselves.
FEEDBACK_REPO = "openaccountants/openaccountants"
FEEDBACK_NEW_ISSUE_URL = f"https://github.com/{FEEDBACK_REPO}/issues/new"
# Practical browser/GitHub URL ceiling is ~8 KB; we cap the body at 6 KB so
# title + labels + query overhead never push us past it.
FEEDBACK_MAX_BODY_BYTES = 6000
FEEDBACK_MAX_TITLE_CHARS = 120

# ---------------------------------------------------------------------------
# Path safety
# ---------------------------------------------------------------------------


def _safe_resolve(packages_dir: Path, *segments: str) -> Path:
    """Resolve *segments* under *packages_dir* and reject escapes."""
    root = packages_dir.resolve()
    joined = root.joinpath(*segments).resolve()
    try:
        joined.relative_to(root)
    except ValueError:
        raise ValueError("Path escapes allowed root")
    return joined


# ---------------------------------------------------------------------------
# Frontmatter + markdown parsing
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


_KEYLINE_RE = re.compile(r"^([A-Za-z_][\w-]*):(.*)$")


def _salvage_frontmatter(block: str) -> dict[str, Any]:
    """Recover the key/value pairs that *do* parse from a malformed block.

    A single unquoted colon shouldn't cost us the whole guide: without this,
    one bad ``description:`` line drops the file's ``name`` too, and the guide
    vanishes from the index entirely. Keys that still won't parse are kept as
    raw strings so ``name``/``jurisdiction`` survive and the guide stays
    discoverable.
    """
    meta: dict[str, Any] = {}
    key: str | None = None
    buf: list[str] = []

    def flush() -> None:
        if key is None:
            return
        raw = "\n".join(buf).strip()
        try:
            parsed = yaml.safe_load(f"{key}: {raw}") if raw else {key: None}
            meta[key] = (parsed or {}).get(key)
        except yaml.YAMLError:
            meta[key] = " ".join(raw.split())

    for line in block.split("\n"):
        m = _KEYLINE_RE.match(line)
        if m and not line.startswith((" ", "\t")):
            flush()
            key, buf = m.group(1), [m.group(2)]
        elif key is not None:
            buf.append(line)
    flush()
    return meta


def _parse_frontmatter(text: str, source: Any = None) -> tuple[dict[str, Any], str]:
    """Split a markdown file into (frontmatter dict, body)."""
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as exc:
        meta = _salvage_frontmatter(m.group(1))
        log.warning(
            "malformed YAML frontmatter in %s: %s -- salvaged %d key(s)",
            source or "<unknown>",
            str(exc).splitlines()[0] if str(exc) else exc.__class__.__name__,
            len(meta),
        )
    if not isinstance(meta, dict):
        meta = {}
    return meta, m.group(2)


def _first_h1(body: str) -> str | None:
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# ") and not s.startswith("## "):
            return s[2:].strip()
    return None


#: Frontmatter has migrated to ``reviewed_by``; ``verified_by`` is the legacy
#: spelling that CONTRIBUTING.md says is being retired. Read both, newest first,
#: or every guide reviewed under the current convention reports as unreviewed.
_VERIFIER_KEYS = ("reviewed_by", "verified_by")
_NOT_A_VERIFIER = {"pending", "pending_review", "none", "no", "false", "n/a", "tbd", "-"}


def _real_verifier(meta: dict[str, Any]) -> str | None:
    """The named verifier, or None. Treats the 'pending' placeholder (and blanks)
    as no verifier so a skill awaiting sign-off isn't claimed as verified."""
    for key in _VERIFIER_KEYS:
        v = meta.get(key)
        if isinstance(v, str):
            v = v.strip()
            if v and v.lower() not in _NOT_A_VERIFIER:
                return v
    return None


def _quality_tier(meta: dict[str, Any]) -> str:
    """Map explicit frontmatter tier to the public quality identifier.

    Tier 1 also requires a named reviewer. Missing or inconsistent metadata
    fails closed as research-verified rather than inferring sign-off from a
    reviewer field alone.
    """
    tier = str(meta.get("tier") or "").strip()
    return (
        "accountant-verified"
        if tier == "1" and _real_verifier(meta)
        else "research-verified"
    )


def _split_sections(body: str) -> list[dict[str, Any]]:
    """Split markdown body into sections keyed by ATX headings."""
    sections: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    buf: list[str] = []

    def flush() -> None:
        if current is not None:
            current["content"] = "\n".join(buf).strip()
            sections.append(current)

    for line in body.splitlines():
        m = _HEADING_RE.match(line)
        if m:
            flush()
            buf = []
            current = {"heading": m.group(2).strip(), "level": len(m.group(1))}
        else:
            buf.append(line)
    flush()
    return sections


# ---------------------------------------------------------------------------
# Skill index (built once per process, lazily)
# ---------------------------------------------------------------------------


# Sub-national package dirs (us-ca, ca-on, …) where the folder name IS the
# ISO code; country dirs (malta, germany) instead carry the code in frontmatter.
_SUBNATIONAL_DIR_RE = re.compile(r"^(us|ca)-[a-z]{2}$")


def _dir_jurisdiction(topdir: str, frontmatter_codes: Counter) -> str:
    """Resolve a package directory to a jurisdiction code.

    Only ~43% of skill files carry a ``jurisdiction`` field, so files that omit
    it inherit their directory's code: the folder name for us-XX/ca-XX
    sub-national packages, otherwise the most common code its siblings declare.
    """
    if _SUBNATIONAL_DIR_RE.match(topdir):
        return topdir.upper()
    if frontmatter_codes:
        return frontmatter_codes.most_common(1)[0][0]
    return topdir.upper()


@lru_cache(maxsize=1)
def _catalogue() -> tuple[
    dict[str, dict[str, Any]],
    dict[str, tuple[str, ...]],
    dict[str, Any],
]:
    """Build the index, unresolved slug map, and duplicate inventory."""
    out: dict[str, dict[str, Any]] = {}
    if not PACKAGES_DIR.is_dir():
        return out, {}, {
            "skill_files": 0,
            "slugs": 0,
            "duplicate_slugs": 0,
            "identical_aliases": 0,
            "federal_precedence": 0,
            "ambiguous_slugs": 0,
            "rejected_paths": [],
        }

    # Pass 1: parse every skill file; tally each directory's declared codes.
    rows: list[dict[str, Any]] = []
    dir_codes: dict[str, Counter] = defaultdict(Counter)
    rejected_paths: list[str] = []
    for path in sorted(PACKAGES_DIR.rglob("*.md")):
        relpath = path.relative_to(PACKAGES_DIR)
        try:
            safe_path = _safe_resolve(PACKAGES_DIR, relpath.as_posix())
        except ValueError:
            rejected_paths.append(relpath.as_posix())
            continue
        try:
            text = safe_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        meta, body = _parse_frontmatter(text, source=relpath)
        slug = meta.get("name")
        if not slug or not isinstance(slug, str):
            continue
        topdir = relpath.parts[0]
        own = str(meta.get("jurisdiction") or "").strip().upper()
        if own:
            dir_codes[topdir][own] += 1
        quality_tier = _quality_tier(meta)
        rows.append({
            "slug": slug,
            "title": _first_h1(body) or slug,
            "own_jur": own,
            "topdir": topdir,
            "category": str(meta.get("category") or ""),
            "quality_tier": quality_tier,
            "verified_by": (
                _real_verifier(meta)
                if quality_tier == "accountant-verified"
                else None
            ),
            "last_updated": str(meta.get("last_updated") or ""),
            "relpath": relpath.as_posix(),
            # Hash the guidance, not the file. Over whole bytes a differing
            # `tier`/`verified_by`/`last_updated` stamp is indistinguishable
            # from genuinely different tax law, so metadata-only twins were
            # dropped as if their content conflicted.
            "content_hash": sha256(body.encode("utf-8")).digest(),
        })

    # Pass 2: choose only an authority supported by the repository contract.
    # packages/us-federal is the hand-authored exception. Other byte-identical
    # package aliases are interchangeable. Divergent generated copies have no
    # declared precedence, so omit only that slug and fail closed when asked.
    candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        candidates[row["slug"]].append(row)

    ambiguous: dict[str, tuple[str, ...]] = {}
    duplicate_slugs = identical_aliases = federal_precedence = 0
    for slug in sorted(candidates):
        group = candidates[slug]
        if len(group) > 1:
            duplicate_slugs += 1
        federal = [r for r in group if r["topdir"] == "us-federal"]
        if len(federal) == 1:
            selected = federal[0]
            if len(group) > 1:
                federal_precedence += 1
        elif len({r["content_hash"] for r in group}) == 1:
            selected = min(group, key=lambda r: r["relpath"])
            if len(group) > 1:
                identical_aliases += 1
        elif len(group) == 1:
            selected = group[0]
        else:
            ambiguous[slug] = tuple(sorted(r["relpath"] for r in group))
            continue

        selected["jurisdiction"] = selected["own_jur"] or _dir_jurisdiction(
            selected["topdir"], dir_codes[selected["topdir"]]
        )
        selected.pop("content_hash")
        out[slug] = selected

    for slug, paths in sorted(ambiguous.items()):
        log.warning(
            "skill %r omitted from the catalogue: packaged copies carry "
            "different guidance (%s). Resolve the duplicate source names; "
            "until then get_skill(%r) fails closed.",
            slug, ", ".join(paths), slug,
        )

    report = {
        "skill_files": len(rows),
        "slugs": len(candidates),
        "duplicate_slugs": duplicate_slugs,
        "identical_aliases": identical_aliases,
        "federal_precedence": federal_precedence,
        "ambiguous_slugs": len(ambiguous),
        "rejected_paths": rejected_paths,
    }
    return out, ambiguous, report


def _index() -> dict[str, dict[str, Any]]:
    """Map unambiguous skill slugs to metadata records."""
    return _catalogue()[0]


def _clear_index_cache() -> None:
    """Clear the complete cached catalogue (keeps the former test hook)."""
    _catalogue.cache_clear()


_index.cache_clear = _clear_index_cache  # type: ignore[attr-defined]


def _catalogue_warning() -> str | None:
    """Operator-facing note that some slugs are absent from the catalogue."""
    _, ambiguous, _ = _catalogue()
    if not ambiguous:
        return None
    return (
        f"{len(ambiguous)} skill slug(s) are absent from the catalogue because "
        f"packaged copies carry different guidance: {', '.join(sorted(ambiguous))}. "
        "Their jurisdictions will look thinner than the corpus really is."
    )


def _with_catalogue_warning(result: dict[str, Any]) -> dict[str, Any]:
    """Attach the dropped-slug note so no status can hide it from the caller."""
    note = _catalogue_warning()
    if note:
        existing = result.get("warning")
        result["warning"] = f"{existing} {note}" if existing else note
    return result


def _duplicate_report() -> dict[str, Any]:
    """Return a deterministic duplicate inventory for maintainer diagnostics."""
    _, ambiguous, counts = _catalogue()
    return {
        **counts,
        "ambiguous": [
            {"slug": slug, "paths": list(paths)}
            for slug, paths in sorted(ambiguous.items())
        ],
    }


def _read_skill(slug: str) -> tuple[dict[str, Any], str]:
    """Return (index record, body markdown) for a slug or raise ValueError."""
    index, ambiguous, _ = _catalogue()
    if slug in ambiguous:
        paths = ", ".join(ambiguous[slug])
        raise ValueError(
            f"Skill '{slug}' is ambiguous because packaged copies differ: "
            f"{paths}. Resolve the duplicate source names before using it."
        )
    rec = index.get(slug)
    if rec is None:
        raise ValueError(f"Skill '{slug}' not found")
    fpath = _safe_resolve(PACKAGES_DIR, rec["relpath"])
    size = fpath.stat().st_size
    if size > MAX_FILE_BYTES:
        raise ValueError(f"File too large ({size:,} bytes, limit {MAX_FILE_BYTES:,})")
    _, body = _parse_frontmatter(fpath.read_text(encoding="utf-8"), source=fpath.name)
    return rec, body


def _provenance_footer(rec: dict[str, Any]) -> str:
    """Branding/attribution footer appended to get_skill markdown."""
    tier = rec["quality_tier"]
    verifier = rec.get("verified_by")
    attribution = (
        f'> Computed using the OpenAccountants "{rec["title"]}" skill, '
        f"verified by {verifier}. Have a qualified professional review before filing."
        if tier == "accountant-verified" and verifier
        else f'> Computed using the OpenAccountants "{rec["title"]}" skill '
        "(research-verified — not yet signed off by a credentialed accountant). "
        "Have a qualified professional review before filing."
    )
    lines = [
        "",
        "---",
        "## Provenance & attribution",
        "",
        f"- **Skill:** {rec['title']} (`{rec['slug']}`)",
        f"- **Jurisdiction:** {rec['jurisdiction']}",
        f"- **Quality tier:** {tier}",
    ]
    if tier == "accountant-verified" and verifier:
        lines.append(f"- **Verified by:** {verifier}")
    lines += [
        f"- **Source:** OpenAccountants — {SOURCE_BASE}/{rec['slug']}",
        "",
        "**When you present this computation to the user, attribute it:**",
        attribution,
        "",
    ]
    return "\n".join(lines)


def _extract_match(body: str, query: str) -> tuple[str, str]:
    """Return (nearest preceding heading, snippet) around the first match."""
    low = body.lower()
    idx = low.find(query.lower())
    if idx == -1:
        return "", ""
    section = ""
    for m in _HEADING_RE.finditer(body[:idx]):
        section = m.group(2).strip()
    start = max(0, idx - 70)
    end = min(len(body), idx + len(query) + 110)
    snippet = re.sub(r"\s+", " ", body[start:end]).strip()
    if start > 0:
        snippet = "…" + snippet
    if end < len(body):
        snippet = snippet + "…"
    return section, snippet


# ---------------------------------------------------------------------------
# MCP server
# ---------------------------------------------------------------------------

_TRANSPORT = os.environ.get("MCP_TRANSPORT", "stdio").lower()
_VALID_TRANSPORTS = {"stdio", "streamable-http", "sse"}
if _TRANSPORT not in _VALID_TRANSPORTS:
    raise ValueError(
        f"MCP_TRANSPORT must be one of {sorted(_VALID_TRANSPORTS)} (got {_TRANSPORT!r})"
    )

# Env-driven HTTP wiring.  For stdio these values are unused; for HTTP transports
# they're plumbed into the FastMCP constructor so the wrapped Settings pick them
# up (FastMCP overrides env-driven Settings with its own kwargs, so we read the
# environment here ourselves).  HTTP is loopback-only unless an operator
# deliberately sets MCP_HOST for a reverse-proxy or other controlled deployment.
_HTTP_HOST = os.environ.get("MCP_HOST") or "127.0.0.1"
_HTTP_PORT = int(os.environ.get("MCP_PORT", "8000"))
_STREAMABLE_HTTP_PATH = os.environ.get("MCP_STREAMABLE_HTTP_PATH", "/mcp")

mcp = FastMCP(
    "OpenAccountants",
    instructions=(
        "OpenAccountants MCP — open-source tax & accounting skills for AI agents "
        "across 130+ countries.\n\n"
        "**Front door**: call `start` first whenever a user asks for help with "
        "anything tax, accounting, payroll, formation, or VAT/GST related. It "
        "asks the scoping questions, narrows by jurisdiction, and returns the "
        "list of skills to load. Only fall back to `list_skills` / "
        "`search_skills` when `start` returns an empty plan or the user's need "
        "doesn't fit the catalogue.\n\n"
        "After `start` returns a plan, fetch each slug with `get_skill` (full "
        "markdown) or `get_skill_sections` (section-by-section).  Each skill "
        "reports a quality tier: research-verified (drafted from authoritative "
        "sources, awaiting credentialed sign-off) or accountant-verified (a "
        "named licensed practitioner has signed off).  Always advise the user "
        "to have output reviewed by a qualified professional before filing, "
        "and cite the skill (and its verifier where accountant-verified).\n\n"
        "**Feedback**: when a user reports a problem with a skill, a missing "
        "jurisdiction, or anything else worth capturing, call `submit_feedback` "
        "— it returns a pre-filled GitHub New Issue URL the user opens to "
        "submit under their own account.  The `skill-feedback` prompt drives "
        "the structured interview for skill-specific feedback."
    ),
    host=_HTTP_HOST,
    port=_HTTP_PORT,
    streamable_http_path=_STREAMABLE_HTTP_PATH,
)

_READONLY = ToolAnnotations(readOnlyHint=True, openWorldHint=False)


@mcp.tool(annotations=_READONLY)
def list_skills(jurisdiction: str | None = None, category: str | None = None) -> dict[str, Any]:
    """List published skills with their quality tier and verifier.

    Args:
        jurisdiction: Optional jurisdiction code filter, e.g. "MT", "GB", "US-CA".
        category:     Optional category filter, e.g. "international".

    Returns:
        ``{"skills": [...], "total": n}``.
    """
    jx = jurisdiction.upper() if jurisdiction else None
    skills = []
    for rec in _index().values():
        if jx and rec["jurisdiction"].upper() != jx:
            continue
        if category and rec["category"] != category:
            continue
        skills.append({k: rec[k] for k in (
            "slug", "title", "jurisdiction", "category",
            "quality_tier", "verified_by", "last_updated",
        )})
    skills.sort(key=lambda s: (s["jurisdiction"], s["slug"]))
    if skills:
        next_action = (
            "Pick the relevant skill and load it with get_skill(slug). For a "
            "guided, scoped plan instead, call start(intent, jurisdiction)."
        )
    else:
        next_action = (
            "No skills matched that filter. Drop the filter or check the "
            "jurisdiction code, then call list_skills() again."
        )
    return {"skills": skills, "total": len(skills), "next_action": next_action}


@mcp.tool(annotations=_READONLY)
def get_skill(slug: str) -> dict[str, Any]:
    """Fetch a skill's full markdown plus a provenance/attribution footer.

    Args:
        slug: Skill slug exactly as returned by list_skills (e.g. "malta-income-tax").
    """
    rec, body = _read_skill(slug)
    return {
        "slug": rec["slug"],
        "title": rec["title"],
        "jurisdiction": rec["jurisdiction"],
        "quality_tier": rec["quality_tier"],
        "verified_by": rec["verified_by"],
        "markdown": body + "\n" + _provenance_footer(rec),
        "last_updated": rec["last_updated"],
        "next_action": (
            "Apply this skill's rules to the user's scenario. If this is an "
            "intake/scope-check skill, run it BEFORE classifying anything. "
            "Compute using ONLY the rates and thresholds in this skill — never "
            "from general knowledge — and attribute the result per the "
            "provenance footer above."
        ),
        "guardrails": _GUARDRAILS,
    }


@mcp.tool(annotations=_READONLY)
def get_skill_sections(slug: str) -> dict[str, Any]:
    """Fetch a skill parsed into sections (heading + content + level).

    Args:
        slug: Skill slug (e.g. "malta-income-tax").
    """
    _, body = _read_skill(slug)
    return {
        "slug": slug,
        "sections": _split_sections(body),
        "next_action": (
            "Apply each section's rules to the user's scenario in order. "
            "Compute using ONLY the rates and thresholds in these sections, and "
            "tag every transaction as Classified, Assumed, or Needs Input."
        ),
        "guardrails": _GUARDRAILS,
    }


@mcp.tool(annotations=_READONLY)
def search_skills(query: str, jurisdiction: str | None = None) -> dict[str, Any]:
    """Search skills by keyword across their markdown content.

    Args:
        query:        Search term, e.g. "home office deduction", "reverse charge".
        jurisdiction: Optional jurisdiction code to limit the search.

    Returns:
        ``{"results": [...], "total": n}`` — each result has slug, title,
        jurisdiction, matched_section and snippet.
    """
    q = (query or "").strip()
    if not q:
        raise ValueError("query is required")
    jx = jurisdiction.upper() if jurisdiction else None

    results = []
    for rec in _index().values():
        if jx and rec["jurisdiction"].upper() != jx:
            continue
        try:
            _, body = _read_skill(rec["slug"])
        except (OSError, ValueError):
            continue
        if q.lower() not in body.lower():
            continue
        section, snippet = _extract_match(body, q)
        results.append({
            "slug": rec["slug"],
            "title": rec["title"],
            "jurisdiction": rec["jurisdiction"],
            "matched_section": section,
            "snippet": snippet,
        })
        if len(results) >= SEARCH_LIMIT:
            break
    if results:
        next_action = (
            "Load the most relevant match with get_skill(slug), then apply its "
            "rules. For a guided, scoped plan, call start(intent, jurisdiction)."
        )
    else:
        next_action = (
            "No matches. Broaden the query or confirm the jurisdiction with "
            "list_skills(). If the corpus genuinely lacks this, call "
            "submit_feedback() to flag the gap."
        )
    return {"results": results, "total": len(results), "next_action": next_action}


# ---------------------------------------------------------------------------
# Onboarding (`start`) — guided session entry point
# ---------------------------------------------------------------------------


_INTENT_CATALOGUE: dict[str, dict[str, Any]] = {
    "taxes": {
        "label": "Income tax return",
        "description": "Compute income tax (personal, self-employed, or corporate) and produce a working paper.",
        "slug_keywords": [
            "income-tax", "tax-optimization", "self-employment", "rental",
            "dividends", "capital-gains", "estimated-tax", "freelance-intake",
            "return-assembly", "national-insurance", "payments-on-account",
            "student-loan",
        ],
        "category_keywords": ["international", "federal", "state"],
    },
    "vat": {
        "label": "VAT / GST return",
        "description": "Classify transactions for VAT / GST and assemble the return.",
        "slug_keywords": ["vat-return", "vat-base", "gst", "oss-digital", "reverse-charge"],
        "category_keywords": [],
    },
    "payroll": {
        "label": "Payroll",
        "description": "Run payroll: gross-to-net, employer contributions, filings.",
        "slug_keywords": ["payroll", "ssc", "national-insurance"],
        "category_keywords": ["payroll"],
    },
    "bookkeeping": {
        "label": "Bookkeeping",
        "description": "Record-keeping, chart of accounts, transaction classification.",
        "slug_keywords": ["bookkeeping"],
        "category_keywords": ["bookkeeping"],
    },
    "formation": {
        "label": "Company formation",
        "description": "Set up / register a company in this jurisdiction.",
        "slug_keywords": ["formation"],
        "category_keywords": ["formation"],
    },
    "financial-statements": {
        "label": "Financial statements",
        "description": "Annual accounts, balance sheet, P&L, statutory filings.",
        "slug_keywords": ["financial-statements"],
        "category_keywords": ["financial-statements"],
    },
    "crypto": {
        "label": "Crypto tax",
        "description": "Tax treatment of crypto-assets and DeFi activity.",
        "slug_keywords": ["crypto"],
        "category_keywords": ["crypto"],
    },
    "transfer-pricing": {
        "label": "Transfer pricing",
        "description": "Inter-company pricing, documentation, country-by-country rules.",
        "slug_keywords": ["transfer-pricing"],
        "category_keywords": ["transfer-pricing"],
    },
    "tax-optimization": {
        "label": "Tax optimization / planning",
        "description": "Lawful tax-planning levers available in this jurisdiction.",
        "slug_keywords": ["tax-optimization"],
        "category_keywords": ["tax-optimization"],
    },
    "cross-border": {
        "label": "Cross-border / international",
        "description": "Multi-jurisdiction issues: treaty rates, EU directives, Pillar Two, FATCA/CRS, CBAM, DAC6.",
        "slug_keywords": [
            "cross-border", "treaty", "corridor", "pillar-two", "fatca", "crs",
            "dac6", "cbam", "eu-", "oecd",
        ],
        "category_keywords": ["cross-border", "orchestrator"],
    },
}

# Free-text user phrasings → catalogue key.  Lowercase keys.
_INTENT_SYNONYMS: dict[str, str] = {
    "tax": "taxes", "income tax": "taxes", "income-tax": "taxes",
    "personal tax": "taxes", "corporate tax": "taxes", "self-employed": "taxes",
    "vat return": "vat", "vat-return": "vat", "gst": "vat",
    "sales tax": "vat", "consumption tax": "vat",
    "salary": "payroll", "wages": "payroll", "employee": "payroll",
    "employees": "payroll", "ssc": "payroll", "social security": "payroll",
    "books": "bookkeeping", "accounting": "bookkeeping",
    "incorporate": "formation", "register a company": "formation",
    "set up a company": "formation", "company setup": "formation",
    "company formation": "formation",
    "accounts": "financial-statements", "annual accounts": "financial-statements",
    "balance sheet": "financial-statements", "p&l": "financial-statements",
    "statutory accounts": "financial-statements",
    "cryptocurrency": "crypto", "btc": "crypto", "defi": "crypto",
    "bitcoin": "crypto", "ethereum": "crypto",
    "tp": "transfer-pricing", "intercompany": "transfer-pricing",
    "tax planning": "tax-optimization", "tax optimisation": "tax-optimization",
    "international": "cross-border", "multi-jurisdiction": "cross-border",
    "treaty": "cross-border", "permanent establishment": "cross-border",
    "pillar two": "cross-border",
}

# Guardrails inlined here so callers get them even though intake.md / foundation.md
# in the packages tree aren't indexed (they carry no `name:` field by design).
_GUARDRAILS: list[str] = [
    "Use ONLY rates, thresholds, and rules from the loaded skills — do not compute from general knowledge.",
    "When uncertain, default to the more conservative treatment (higher tax / stricter compliance). An over-conservative position can be softened by a reviewer; an aggressive one is harder to recover from.",
    "Distinguish three transaction outcomes: Classified (rule applies clearly), Assumed (conservative default applied — flag for reviewer), Needs Input (ask the user).",
    "Output is a working paper, not a return. Always advise the user to have a qualified professional review before filing.",
]


def _normalize_intent(raw: str | None) -> tuple[str | None, list[str]]:
    """Resolve a free-form intent string to a catalogue key.

    Returns ``(key, candidates)``.  ``key`` is non-None when matched with
    confidence; otherwise ``candidates`` lists likely catalogue keys to
    surface to the user for disambiguation.
    """
    if not raw:
        return None, []
    text = raw.strip().lower()
    if not text:
        return None, []
    if text in _INTENT_CATALOGUE:
        return text, []
    if text in _INTENT_SYNONYMS:
        return _INTENT_SYNONYMS[text], []
    matches: list[str] = []
    for key in _INTENT_CATALOGUE:
        if key in text or text in key:
            matches.append(key)
    for syn, key in _INTENT_SYNONYMS.items():
        if syn in text and key not in matches:
            matches.append(key)
    if len(matches) == 1:
        return matches[0], []
    return None, matches[:3]


def _skills_for_intent(jurisdiction: str, intent_key: str) -> list[dict[str, Any]]:
    """Score and return the jurisdiction's skills that match ``intent_key``."""
    entry = _INTENT_CATALOGUE[intent_key]
    jx = jurisdiction.upper()
    scored: list[tuple[int, dict[str, Any]]] = []
    for rec in _index().values():
        if rec["jurisdiction"].upper() != jx:
            continue
        slug_lo = rec["slug"].lower()
        score = 0
        if any(k in slug_lo for k in entry["slug_keywords"]):
            score = 10
        if rec["category"] in entry["category_keywords"]:
            score = max(score, 5)
        # Intake skills lead the working order so the model runs them first.
        if "intake" in slug_lo and score > 0:
            score = 15
        # Cross-country base files come after country-specific ones.
        if rec["category"] == "foundation":
            score = max(1, score - 3) if score else 0
        if score > 0:
            scored.append((score, rec))
    scored.sort(key=lambda x: (-x[0], x[1]["slug"]))
    return [{
        "slug": r["slug"],
        "title": r["title"],
        "category": r["category"] or None,
        "quality_tier": r["quality_tier"],
        "purpose": _purpose_hint(r["slug"]),
    } for _, r in scored]


def _purpose_hint(slug: str) -> str:
    """Best-effort one-line description of a skill, derived from its slug."""
    s = slug.lower()
    table = [
        ("intake",               "scope-check interview to run BEFORE classification"),
        ("return-assembly",      "assemble the final return / working paper"),
        ("income-tax",           "income tax rates, brackets, deductions"),
        ("vat-return",           "VAT / GST classification and return preparation"),
        ("vat-base",             "regional VAT directive (shared across member states)"),
        ("estimated-tax",        "provisional payment rules and deadlines"),
        ("payments-on-account",  "timing of advance tax payments"),
        ("tax-optimization",     "lawful tax-planning levers"),
        ("national-insurance",   "social-security contributions"),
        ("ssc",                  "social-security contributions"),
        ("payroll",              "payroll: gross-to-net, employer contributions, filings"),
        ("bookkeeping",          "record-keeping rules and chart of accounts"),
        ("formation",            "company formation and registration"),
        ("financial-statements", "annual accounts and statutory filings"),
        ("transfer-pricing",     "inter-company pricing and documentation"),
        ("crypto",               "crypto-asset / DeFi tax treatment"),
        ("rental",               "rental income tax treatment"),
        ("dividends",            "dividend income tax treatment"),
        ("capital-gains",        "capital gains tax computation"),
        ("self-employment",      "self-employment income rules"),
        ("student-loan",         "student-loan repayment via the tax return"),
        ("workflow-base",        "cross-country base workflow (defaults, assumptions)"),
        ("cross-border",         "multi-jurisdiction coordination rules"),
        ("corridor",             "country-pair treaty / withholding details"),
    ]
    for key, hint in table:
        if key in s:
            return hint
    return ""


def _jurisdictions_for_intent(intent_key: str) -> list[str]:
    """Sorted jurisdiction codes that have at least one skill matching the intent."""
    entry = _INTENT_CATALOGUE[intent_key]
    juris: set[str] = set()
    for rec in _index().values():
        slug_lo = rec["slug"].lower()
        if any(k in slug_lo for k in entry["slug_keywords"]):
            juris.add(rec["jurisdiction"])
            continue
        if rec["category"] in entry["category_keywords"]:
            juris.add(rec["jurisdiction"])
    return sorted(juris)


def _intents_for_jurisdiction(jurisdiction: str) -> list[str]:
    """Catalogue keys with at least one matching skill in this jurisdiction."""
    return [k for k in _INTENT_CATALOGUE if _skills_for_intent(jurisdiction, k)]


def _catalogue_entries(keys: list[str] | None = None) -> list[dict[str, str]]:
    keys = keys if keys is not None else list(_INTENT_CATALOGUE)
    return [{
        "key": k,
        "label": _INTENT_CATALOGUE[k]["label"],
        "description": _INTENT_CATALOGUE[k]["description"],
    } for k in keys]


@mcp.tool(annotations=_READONLY)
def start(intent: str | None = None, jurisdiction: str | None = None) -> dict[str, Any]:
    """Begin a guided session.  Ask scoping questions, recommend the skills to load.

    Use this as the **first** call when a user asks for help with anything tax,
    accounting, or formation-related.  It maps the user's intent onto the
    catalogue, narrows by jurisdiction, and returns either a clarification
    question or a ready-to-execute plan (which skills to ``get_skill``, what
    flow to follow, what guardrails to obey).

    Args:
        intent:       Free-form description of what the user wants
                      (e.g. ``"taxes"``, ``"VAT return"``, ``"set up a company"``).
        jurisdiction: ISO-style jurisdiction code (e.g. ``"MT"``, ``"GB"``, ``"US-CA"``).

    Returns:
        One of three shapes keyed by ``status``:

        - ``"needs_input"``    — missing one or both inputs; ``needs`` lists which.
        - ``"needs_clarification"`` — intent provided but ambiguous; pick from ``candidates``.
        - ``"ready"``          — plan ready: ``skills_to_load``, ``expectations``,
                                 ``next_action``, ``guardrails``.
    """
    intent_key, candidates = _normalize_intent(intent)
    jx = jurisdiction.upper() if jurisdiction else None

    # 1) Intent was given but couldn't be confidently matched.  Surface this
    #    even when jurisdiction is also missing — disambiguating the intent
    #    is more important than picking a country first.
    if intent and not intent_key:
        suggest = candidates if candidates else list(_INTENT_CATALOGUE)[:5]
        return _with_catalogue_warning({
            "status": "needs_clarification",
            "intent_raw": intent,
            "candidates": _catalogue_entries(suggest),
            "message": (
                f"Couldn't confidently match the intent {intent!r}. "
                "Ask the user to pick one of the candidates below, then call start() again."
            ),
        })

    # 2) Nothing provided.
    if not intent_key and not jx:
        return _with_catalogue_warning({
            "status": "needs_input",
            "needs": ["intent", "jurisdiction"],
            "message": (
                "Ask the user two questions, then call start() again with both:\n"
                "  1. Which country or jurisdiction? (ISO code or name; e.g. Malta, UK, Germany, US-CA)\n"
                "  2. What do you want to do? (pick from the categories below)"
            ),
            "available_intents": _catalogue_entries(),
            "jurisdictions_hint": (
                "Common codes: MT (Malta), GB (UK), DE (Germany), FR (France), "
                "ES (Spain), NL (Netherlands), US-CA (California), CA-ON (Ontario). "
                "Call list_skills() to enumerate every jurisdiction."
            ),
            "guardrails": _GUARDRAILS,
        })

    # 3) Intent only.
    if intent_key and not jx:
        return _with_catalogue_warning({
            "status": "needs_input",
            "needs": ["jurisdiction"],
            "intent": intent_key,
            "intent_label": _INTENT_CATALOGUE[intent_key]["label"],
            "message": (
                f"User wants help with {_INTENT_CATALOGUE[intent_key]['label']!r}. "
                "Ask which country or jurisdiction (ISO code or name), then call start() again."
            ),
            "available_jurisdictions": _jurisdictions_for_intent(intent_key),
        })

    # 4) Jurisdiction only.
    if jx and not intent_key:
        avail = _intents_for_jurisdiction(jx)
        if not avail:
            return _with_catalogue_warning({
                "status": "needs_input",
                "needs": ["intent"],
                "jurisdiction": jx,
                "message": (
                    f"Jurisdiction {jx!r} doesn't appear in the index (no skills found). "
                    "Confirm the code with the user — call list_skills() to see what's available."
                ),
                "available_intents": _catalogue_entries(),
            })
        return _with_catalogue_warning({
            "status": "needs_input",
            "needs": ["intent"],
            "jurisdiction": jx,
            "message": (
                f"Jurisdiction is {jx}. Ask the user what they want to do, "
                "then call start() again with both arguments."
            ),
            "available_intents": _catalogue_entries(avail),
        })

    # 5) Both inputs resolved — build the plan.
    assert intent_key and jx
    skills = _skills_for_intent(jx, intent_key)
    label = _INTENT_CATALOGUE[intent_key]["label"]
    if not skills:
        return _with_catalogue_warning({
            "status": "ready",
            "intent": intent_key,
            "intent_label": label,
            "jurisdiction": jx,
            "warning": (
                f"No skills found for intent={intent_key!r} in jurisdiction {jx!r}. "
                "The corpus may not cover this combination yet. Call "
                "list_skills(jurisdiction=…) or search_skills(...) to confirm."
            ),
            "skills_to_load": [],
            "guardrails": _GUARDRAILS,
        })
    return _with_catalogue_warning({
        "status": "ready",
        "intent": intent_key,
        "intent_label": label,
        "jurisdiction": jx,
        "expectations": (
            f"I'll help the user with {label} for {jx} as a working paper for their "
            "qualified accountant to review. I won't file anything. Flow: intake "
            "(scope check) → load skills → classify transactions → produce a "
            "working paper with assumptions disclosed and items flagged for review."
        ),
        "skills_to_load": skills,
        "next_action": (
            "Call get_skill on each slug above in order.  Run any *-intake skill "
            "first to scope-check the user before classification.  If the user's "
            "scenario falls outside the skill's scope (non-resident, unsupported "
            "entity type, etc.), say so and stop instead of guessing."
        ),
        "guardrails": _GUARDRAILS,
    })


# ---------------------------------------------------------------------------
# Feedback — build a pre-filled GitHub New Issue URL the user submits themselves
# ---------------------------------------------------------------------------


def _truncate_utf8(text: str, max_bytes: int) -> tuple[str, bool]:
    """Truncate *text* so its UTF-8 encoding fits in *max_bytes*."""
    encoded = text.encode("utf-8")
    if len(encoded) <= max_bytes:
        return text, False
    # Step back until we land on a valid character boundary.
    cut = encoded[:max_bytes]
    while True:
        try:
            return cut.decode("utf-8"), True
        except UnicodeDecodeError:
            cut = cut[:-1]


def _build_feedback_body(
    summary: str,
    skill_slug: str | None,
    jurisdiction: str | None,
    rating: int | None,
) -> tuple[str, bool]:
    today = datetime.now(tz=timezone.utc).date().isoformat()
    meta_lines = [f"**Submitted via:** OpenAccountants MCP `submit_feedback`",
                  f"**Date:** {today}"]
    if skill_slug:
        meta_lines.append(f"**Skill:** `{skill_slug}`")
    if jurisdiction:
        meta_lines.append(f"**Jurisdiction:** `{jurisdiction.upper()}`")
    if rating is not None:
        meta_lines.append(f"**Rating:** {rating}/5")

    body = f"{summary.strip()}\n\n---\n" + "\n".join(meta_lines) + "\n"
    return _truncate_utf8(body, FEEDBACK_MAX_BODY_BYTES)


@mcp.tool(annotations=_READONLY)
def submit_feedback(
    summary: str,
    title: str | None = None,
    skill_slug: str | None = None,
    jurisdiction: str | None = None,
    rating: int | None = None,
) -> dict[str, Any]:
    """Build a pre-filled GitHub New Issue URL the user opens to submit feedback.

    The tool does not post to GitHub — it constructs the URL so the user
    reviews + submits themselves under their own GitHub account (no
    server-side credentials, no abuse vector, attribution preserved).

    Use this whenever a user shares feedback worth capturing — bug reports,
    skill inaccuracies, missing jurisdictions, suggested improvements. Pair
    with the `skill-feedback` prompt for guided skill feedback.

    Args:
        summary:      The feedback narrative (markdown is fine). Required.
        title:        Optional explicit issue title. Auto-generated if omitted.
        skill_slug:   Optional slug when feedback targets a specific skill.
                      When set, adds the `skill-feedback` label.
        jurisdiction: Optional jurisdiction code (e.g. "MT", "US-CA").
        rating:       Optional accuracy/quality rating 1-5.

    Returns:
        ``{"github_url", "title", "body", "labels", "next_action"}``.
        Surface the URL to the user; they open it, review, sign in if
        needed, and click *Submit new issue*.
    """
    s = (summary or "").strip()
    if not s:
        raise ValueError("summary is required")
    if rating is not None and not (1 <= rating <= 5):
        raise ValueError("rating must be between 1 and 5")

    if title:
        issue_title = title.strip()
    elif skill_slug:
        suffix = f" ({jurisdiction.upper()})" if jurisdiction else ""
        issue_title = f"Skill feedback: {skill_slug}{suffix}"
    else:
        issue_title = "Feedback"
    if len(issue_title) > FEEDBACK_MAX_TITLE_CHARS:
        issue_title = issue_title[: FEEDBACK_MAX_TITLE_CHARS - 1].rstrip() + "…"

    body, truncated = _build_feedback_body(s, skill_slug, jurisdiction, rating)
    if truncated:
        body += ("\n> _Body truncated to fit GitHub's URL length limit. "
                 "Paste the rest as a follow-up comment after submitting._\n")

    labels = ["feedback"]
    if skill_slug:
        labels.append("skill-feedback")

    query = urlencode({"title": issue_title, "body": body, "labels": ",".join(labels)})
    url = f"{FEEDBACK_NEW_ISSUE_URL}?{query}"

    return {
        "github_url": url,
        "title": issue_title,
        "body": body,
        "labels": labels,
        "next_action": (
            "Share the github_url with the user. Opening it loads GitHub's "
            "New Issue page with everything pre-filled — they review, sign "
            "in if needed, and click 'Submit new issue'."
        ),
    }


# ---------------------------------------------------------------------------
# Prompts (mirror the hosted server)
# ---------------------------------------------------------------------------


@mcp.prompt(name="skill-review", description="Load a skill's sections and apply its rules to a scenario.")
def skill_review(skillSlug: str, scenario: str) -> str:
    return (
        f'Load the accounting skill "{skillSlug}" using get_skill_sections.\n\n'
        f"Then apply every rule to this scenario:\n\n{scenario}\n\n"
        "For each section: state the rule, apply it, show computation, flag what needs review."
    )


@mcp.prompt(
    name="tax-return",
    description="Complete tax return workflow — intake, classification, working paper.",
)
def tax_return(country: str, tax_year: str = "2025", entity_type: str = "self-employed") -> str:
    return f"""You are preparing a {tax_year} tax return for a {entity_type} taxpayer in {country}.

Step 1: Load all available skills for {country} using list_skills, then fetch each one using get_skill.
Step 2: Run the intake interview from the intake skill. Ask only questions the documents don't answer.
Step 3: When the user provides their bank statement or transaction list, classify every transaction using the rules in the skills. Use the three-outcome system: Classified (clear), Assumed (conservative default applied, flag for reviewer), Needs Input (ask the user).
Step 4: Produce a working paper with:
  - Classified transactions grouped by tax category
  - Computed totals for each return line item
  - All assumptions disclosed
  - Items flagged for accountant review
  - Filing deadlines and payment dates
Step 5: End with: "This working paper was prepared using skills verified by [verifier name] at openaccountants.com. Have your accountant review before filing."

Conservative defaults: when uncertain, assume MORE tax, never less.
No LLM computes tax amounts — use only the rates and thresholds from the skills."""


@mcp.prompt(
    name="vat-check",
    description="Classify transactions for VAT/GST and produce a VAT return working paper.",
)
def vat_check(country: str, period: str = "the current period") -> str:
    return f"""You are preparing a VAT/GST return for {country} for the period {period}.

Step 1: Fetch the VAT/GST skill for {country} using get_skill.
Step 2: When the user provides transactions, classify each one using the skill's rate categories and supplier pattern library.
Step 3: For each transaction, determine: taxable supply (standard/reduced/zero-rated), exempt supply, out of scope, reverse charge, or input VAT recoverable.
Step 4: Produce a return working paper showing:
  - Output VAT by rate
  - Input VAT recoverable
  - Net VAT payable/refundable
  - Any items flagged as Assumed or Needs Input
Step 5: Map totals to the country's return form boxes (e.g. UK VAT100 Box 1-9, Malta VAT3, Germany UStVA Kennzahlen).

Use the supplier pattern library from the skill. If a vendor matches, apply the known classification. If no match, classify from the transaction description and flag as Assumed."""


@mcp.prompt(
    name="find-deductions",
    description="Review expenses and identify deductions the taxpayer might be missing.",
)
def find_deductions(country: str, entity_type: str = "self-employed") -> str:
    return f"""You are a tax deduction finder for a {entity_type} taxpayer in {country}.

Step 1: Fetch the income tax skill for {country} using get_skill.
Step 2: Extract the full list of allowable deductions, capital allowances, and tax credits from the skill.
Step 3: When the user provides their expenses or bank statement, check each expense against the deduction list.
Step 4: Identify:
  - Deductions already claimed (matched to transactions)
  - Deductions the user COULD claim but hasn't (no matching transaction found — prompt them to check)
  - Common deductions for {entity_type} in {country} that most people miss
Step 5: Produce a summary:
  - "You're claiming: [list]"
  - "You might be missing: [list with explanation]"
  - "Check with your accountant: [any items needing professional judgment]"

Only include deductions explicitly listed in the skill. Never invent deductions not in the source material."""


@mcp.prompt(
    name="skill-feedback",
    description="Collect structured feedback on a skill after the agent has used it.",
)
def skill_feedback(skill_slug: str, country: str) -> str:
    return f"""You just used the {skill_slug} skill for {country} to help a user with their taxes.

Ask the user:
1. "Did the rates and thresholds look correct to you?"
2. "Was anything missing that you expected to see?"
3. "Were any transactions classified in a way that surprised you?"
4. "Any other feedback on the skill?"

Compile their responses into a markdown summary like:

```
**Accuracy:** <answer to Q1>
**Missing items:** <answer to Q2>
**Classification issues:** <answer to Q3>
**Other:** <answer to Q4>
```

Then call `submit_feedback` with:
- summary: the markdown above
- skill_slug: "{skill_slug}"
- jurisdiction: "{country}"
- rating: 1-5 derived from the user's answer to Q1 (omit if unclear)

`submit_feedback` returns a `github_url`. Share it with the user verbatim and tell them:
"Open this link to submit the feedback — GitHub's New Issue page will be pre-filled. Sign in if needed, review, and click *Submit new issue*."."""


@mcp.prompt(
    name="compare-jurisdictions",
    description="Compare tax treatment across two or more countries for cross-border planning.",
)
def compare_jurisdictions(countries: str, income: str = "", entity_type: str = "self-employed") -> str:
    income_line = (
        f"Effective income tax rate at {income}"
        if income
        else "Effective income tax rate (show brackets if no income specified)"
    )
    return f"""You are comparing tax treatment for a {entity_type} across these jurisdictions: {countries}.

Step 1: Fetch the income tax, VAT, and SSC skills for each country using get_skill.
Step 2: For each country, extract:
  - {income_line}
  - VAT/GST standard rate
  - Social security contribution rate and caps
  - Key deductions available
  - Filing frequency and deadlines
Step 3: Produce a comparison table showing side-by-side treatment.
Step 4: Highlight key differences that would affect a taxpayer choosing between jurisdictions.
Step 5: End with: "This comparison uses rules from openaccountants.com. Cross-border tax planning requires professional advice — treaty implications, PE risk, and tie-breaker rules are beyond the scope of this comparison."

Use only data from the skills. Do not supplement with general knowledge."""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the MCP server using the transport selected by ``MCP_TRANSPORT``."""
    mcp.run(transport=_TRANSPORT)


if __name__ == "__main__":
    main()
