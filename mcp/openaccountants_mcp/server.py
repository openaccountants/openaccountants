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
                          ``0.0.0.0`` when an HTTP transport is selected,
                          ``127.0.0.1`` otherwise.
MCP_PORT                  Bind port for HTTP transports.  Defaults to ``8000``.
MCP_STREAMABLE_HTTP_PATH  Path the Streamable-HTTP endpoint is mounted at.
                          Defaults to ``/mcp``.  Set to ``/`` when fronted by a
                          reverse proxy that strips the upstream path prefix.
"""

from __future__ import annotations

import os
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

# ---------------------------------------------------------------------------
# Resolve repo root + packages directory
# ---------------------------------------------------------------------------

_DEFAULT_ROOT = Path(__file__).resolve().parents[2]  # mcp/openaccountants_mcp/ -> mcp/ -> repo
REPO_ROOT = Path(os.environ.get("OPENACCOUNTANTS_ROOT", str(_DEFAULT_ROOT))).resolve()
PACKAGES_DIR = REPO_ROOT / "packages"

MAX_FILE_BYTES = 2 * 1024 * 1024  # 2 MB safety cap
SEARCH_LIMIT = 25
SOURCE_BASE = "https://openaccountants.com/skills"

# ---------------------------------------------------------------------------
# Path safety
# ---------------------------------------------------------------------------


def _safe_resolve(packages_dir: Path, *segments: str) -> Path:
    """Resolve *segments* under *packages_dir* and reject escapes."""
    joined = packages_dir.joinpath(*segments).resolve()
    try:
        joined.relative_to(packages_dir)
    except ValueError:
        raise ValueError(f"Path escapes allowed root: {joined}")
    return joined


# ---------------------------------------------------------------------------
# Frontmatter + markdown parsing
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Split a markdown file into (frontmatter dict, body)."""
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    if not isinstance(meta, dict):
        meta = {}
    return meta, m.group(2)


def _first_h1(body: str) -> str | None:
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# ") and not s.startswith("## "):
            return s[2:].strip()
    return None


def _real_verifier(meta: dict[str, Any]) -> str | None:
    """The named verifier, or None. Treats the 'pending' placeholder (and blanks)
    as no verifier so a skill awaiting sign-off isn't claimed as verified."""
    v = meta.get("verified_by")
    if isinstance(v, str):
        v = v.strip()
        if v and v.lower() != "pending":
            return v
    return None


def _quality_tier(meta: dict[str, Any]) -> str:
    """A named verifier means accountant-verified; otherwise research-verified."""
    return "accountant-verified" if _real_verifier(meta) else "research-verified"


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
def _index() -> dict[str, dict[str, Any]]:
    """Map skill slug -> metadata record.

    A file counts as a skill when its YAML frontmatter carries a ``name``.
    Shared files that appear in several country bundles collapse to a single
    entry (first one wins) so each slug is listed once.
    """
    out: dict[str, dict[str, Any]] = {}
    if not PACKAGES_DIR.is_dir():
        return out

    # Pass 1: parse every skill file; tally each directory's declared codes.
    rows: list[dict[str, Any]] = []
    dir_codes: dict[str, Counter] = defaultdict(Counter)
    for path in sorted(PACKAGES_DIR.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        meta, body = _parse_frontmatter(text)
        slug = meta.get("name")
        if not slug or not isinstance(slug, str):
            continue
        topdir = path.relative_to(PACKAGES_DIR).parts[0]
        own = str(meta.get("jurisdiction") or "").strip().upper()
        if own:
            dir_codes[topdir][own] += 1
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        rows.append({
            "slug": slug,
            "title": _first_h1(body) or slug,
            "own_jur": own,
            "topdir": topdir,
            "category": str(meta.get("category") or ""),
            "quality_tier": _quality_tier(meta),
            "verified_by": _real_verifier(meta),
            "last_updated": mtime.date().isoformat(),
            "relpath": str(path.relative_to(PACKAGES_DIR)),
        })

    # Pass 2: resolve jurisdiction (own field wins; else inherit from dir).
    for r in rows:
        if r["slug"] in out:
            continue
        r["jurisdiction"] = r["own_jur"] or _dir_jurisdiction(r["topdir"], dir_codes[r["topdir"]])
        out[r["slug"]] = r
    return out


def _read_skill(slug: str) -> tuple[dict[str, Any], str]:
    """Return (index record, body markdown) for a slug or raise ValueError."""
    rec = _index().get(slug)
    if rec is None:
        raise ValueError(f"Skill '{slug}' not found")
    fpath = _safe_resolve(PACKAGES_DIR, rec["relpath"])
    size = fpath.stat().st_size
    if size > MAX_FILE_BYTES:
        raise ValueError(f"File too large ({size:,} bytes, limit {MAX_FILE_BYTES:,})")
    _, body = _parse_frontmatter(fpath.read_text(encoding="utf-8"))
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
# environment here ourselves).
_HTTP_HOST = os.environ.get("MCP_HOST", "0.0.0.0" if _TRANSPORT != "stdio" else "127.0.0.1")
_HTTP_PORT = int(os.environ.get("MCP_PORT", "8000"))
_STREAMABLE_HTTP_PATH = os.environ.get("MCP_STREAMABLE_HTTP_PATH", "/mcp")

mcp = FastMCP(
    "OpenAccountants",
    instructions=(
        "OpenAccountants MCP — open-source tax & accounting skills for AI agents "
        "across 130+ countries. Use list_skills to discover skills (optionally by "
        "jurisdiction/category), search_skills to find a concept by keyword, "
        "get_skill to read a skill's full markdown, and get_skill_sections to read "
        "it section by section. Each skill reports a quality tier: research-verified "
        "(drafted from authoritative sources, awaiting credentialed sign-off) or "
        "accountant-verified (a named licensed practitioner has signed off). Always "
        "advise the user to have output reviewed by a qualified professional before "
        "filing, and cite the skill (and its verifier where accountant-verified)."
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
    return {"skills": skills, "total": len(skills)}


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
    }


@mcp.tool(annotations=_READONLY)
def get_skill_sections(slug: str) -> dict[str, Any]:
    """Fetch a skill parsed into sections (heading + content + level).

    Args:
        slug: Skill slug (e.g. "malta-income-tax").
    """
    _, body = _read_skill(slug)
    return {"slug": slug, "sections": _split_sections(body)}


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
    return {"results": results, "total": len(results)}


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
    today = datetime.now(tz=timezone.utc).date().isoformat()
    return f"""You just used the {skill_slug} skill for {country} to help a user with their taxes.

Ask the user:
1. "Did the rates and thresholds look correct to you?"
2. "Was anything missing that you expected to see?"
3. "Were any transactions classified in a way that surprised you?"
4. "Any other feedback on the skill?"

Compile their responses into a structured feedback summary:
- Skill: {skill_slug}
- Country: {country}
- Date: {today}
- Accuracy rating: [1-5 based on response to Q1]
- Missing items: [from Q2]
- Classification issues: [from Q3]
- Other: [from Q4]

Then call submit_skill_feedback with this summary (if the tool is available).
If submit_skill_feedback is not available, display the summary and say:
"Please share this feedback at github.com/openaccountants/openaccountants/issues so we can improve the skill."."""


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
