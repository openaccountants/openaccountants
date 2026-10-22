#!/usr/bin/env python3
"""Build `agent-skills/` (and the Claude Code plugin's `skills/`) from `skills/**`.

Every published skill in this repo becomes one folder with a `SKILL.md` in the open
Agent Skills format (agentskills.io): `name` + `description` frontmatter, then the
skill text, then a short section telling the agent where today's figures live (the
OpenAccountants connector) and who stands behind the skill.

Why this exists (16 Oct 2026). An installed skill is read by the AI every time the
topic comes up; a connector in a directory is picked about 0.5% of the time. The
previous `agent-skills/` tree was a one-off snapshot from 21 July 2026 whose
generator was never committed, so it drifted from the library for three months.
This script runs in the nightly sync after `build-packages.py`, so the tree
follows the library.

Usage:
  python3 scripts/build-agent-skills.py                       # agent-skills/ for everything
  python3 scripts/build-agent-skills.py --plugin MT,NL,DE,IE,GB  # also plugins/openaccountants/skills/
  python3 scripts/build-agent-skills.py --check               # exit 1 if the tree is stale

Derived tree: never edit `agent-skills/<slug>/SKILL.md` by hand; edit `skills/**`.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frontmatter_yaml import FrontmatterError, load_frontmatter  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
OUT_DIR = REPO_ROOT / "agent-skills"
PLUGIN_SKILLS_DIR = REPO_ROOT / "plugins" / "openaccountants" / "skills"
SITE = "https://www.openaccountants.com"
LICENSE_LINE = "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"

# Content skills only. Foundation/orchestrator/templates/patterns are workflow scaffolding
# that the MCP assembles; they are not something a person installs on its own.
SOURCE_DIRS = ("international", "federal", "us-states", "cross-border", "verticals", "integrations", "financial-reporting")
KEEP_FILES = {"README.md", "LICENSE.md", "install.sh", "index.json"}
BAD_DESCRIPTIONS = {"", "---", ">", "|", "null", "none"}
GLOSS = "tax rules your AI follows"

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)


def split_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        meta = load_frontmatter(m.group(1))
    except FrontmatterError:
        meta = {}
    return meta, text[m.end():]


def first_heading(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def first_paragraph(body: str) -> str:
    seen_h1 = False
    buf: list[str] = []
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("# ") and not seen_h1:
            seen_h1 = True
            continue
        if not seen_h1:
            continue
        if not s:
            if buf:
                break
            continue
        if s.startswith(("#", "|", ">", "---", "- ", "* ", "```")):
            if buf:
                break
            continue
        buf.append(s)
    text = " ".join(buf)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links -> text
    text = re.sub(r"[*_`]", "", text)
    return text.strip()


def derive_description(meta: dict, body: str, slug: str) -> str:
    raw = str(meta.get("description") or "").strip()
    if raw.lower() not in BAD_DESCRIPTIONS and len(raw) >= 40:
        desc = raw
    else:
        title = first_heading(body) or slug.replace("-", " ")
        para = first_paragraph(body)
        desc = f"Use when asked about {title}. {para}".strip()
        # Legacy bodies still say "this Guide"; the skill's own description should not.
        desc = re.sub(r"\bGuides\b", "skills", desc)
        desc = re.sub(r"\bGuide\b", "skill", desc)
    desc = re.sub(r"\s+", " ", desc)
    return desc[:1000]


def yaml_quote(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)


def skill_md(slug: str, meta: dict, body: str) -> str:
    desc = derive_description(meta, body, slug)
    jurisdiction = str(meta.get("jurisdiction") or "").strip()
    trust = str(meta.get("trust_label") or "").strip()
    review = str(meta.get("review_status") or "").strip()
    tax_year = meta.get("tax_year")
    updated = str(meta.get("last_updated") or "").strip()
    authored = str(meta.get("authored_by") or "").strip()
    reviewed = str(meta.get("reviewed_by") or "").strip()
    lines = [
        "---",
        f"name: {slug}",
        f"description: {yaml_quote(desc)}",
        f"license: {yaml_quote(LICENSE_LINE)}",
        "metadata:",
        "  source: openaccountants",
        f"  openaccountants_url: {yaml_quote(f'{SITE}/skills/{slug}')}",
    ]
    if jurisdiction:
        lines.append(f"  jurisdiction: {yaml_quote(jurisdiction)}")
    if tax_year not in (None, ""):
        lines.append(f"  tax_year: {yaml_quote(str(tax_year))}")
    if updated:
        lines.append(f"  last_updated: {yaml_quote(updated)}")
    if authored:
        lines.append(f"  authored_by: {yaml_quote(authored)}")
    if reviewed:
        lines.append(f"  reviewed_by: {yaml_quote(reviewed)}")
    if trust:
        lines.append(f"  trust_label: {yaml_quote(trust)}")
    if review:
        lines.append(f"  review_status: {yaml_quote(review)}")
    lines.append("---")
    live = (
        "\n\n## Today's figures and who stands behind this skill\n\n"
        f"This file is an AI skill ({GLOSS}) from OpenAccountants, copied on {updated or 'the date in last_updated'}. "
        "Rates, thresholds and deadlines change. For the current version of this skill, its official sources and "
        "the named accountant (if any) who stands behind it, call `get_skill` with slug `" + slug + "` on the "
        f"OpenAccountants connector ({SITE}/connect), or read {SITE}/skills/{slug}. "
        "If neither is available, confirm every figure against the official source pages cited above before relying on it.\n"
    )
    return "\n".join(lines) + "\n\n" + body.strip() + live



def stamp_readme(text: str, built: dict, jurisdictions: list[str], reviewed: int | None = None) -> str:
    """Rewrite the counts block between the oa-skills-stats markers; the rest is hand-written.

    Two quality states only: accountant-reviewed (tier 1 with a named reviewer) and
    source-cited draft. `reviewed` is the tier-1 count from build(); when it is not
    given, a named reviewer in metadata is the fallback signal."""
    if reviewed is None:
        reviewed = sum(1 for v in built.values() if v.get("reviewed_by"))
    drafts = len(built) - reviewed
    block = (
        "<!-- oa-skills-stats:start -->\n"
        f"**{len(built):,} skills** across **{len(jurisdictions)} jurisdictions**. "
        f"{reviewed} are accountant-reviewed (a named accountant in `metadata.reviewed_by`); "
        f"the other {drafts:,} are source-cited drafts.\n"
        "<!-- oa-skills-stats:end -->"
    )
    return re.sub(r"<!-- oa-skills-stats:start -->.*?<!-- oa-skills-stats:end -->", block, text, flags=re.S)


def iter_source_files():
    for d in SOURCE_DIRS:
        base = SKILLS_DIR / d
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*.md")):
            if p.name.lower() in {"readme.md", "references.md"}:
                continue
            yield p


def build(plugin_countries: set[str], check_only: bool) -> int:
    built: dict[str, dict] = {}
    staged: dict[Path, str] = {}
    reviewed = 0  # tier 1 with a named reviewer: the only accountant-reviewed state
    for src in iter_source_files():
        text = src.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)
        slug = str(meta.get("name") or src.stem).strip()
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", slug):
            continue
        if slug in built:
            continue  # first occurrence wins; duplicates live in retired folders
        content = skill_md(slug, meta, body)
        staged[OUT_DIR / slug / "SKILL.md"] = content
        j = str(meta.get("jurisdiction") or "").strip()
        built[slug] = {
            "jurisdiction": j,
            "path": str(src.relative_to(REPO_ROOT)),
            "trust_label": str(meta.get("trust_label") or "").strip() or None,
            "authored_by": str(meta.get("authored_by") or "").strip() or None,
            "reviewed_by": str(meta.get("reviewed_by") or "").strip() or None,
            "tax_year": meta.get("tax_year"),
        }
        if str(meta.get("tier")).strip() == "1" and built[slug]["reviewed_by"]:
            reviewed += 1
        if j.split("-")[0] in plugin_countries:
            staged[PLUGIN_SKILLS_DIR / slug / "SKILL.md"] = content

    index = {
        "generated_by": "scripts/build-agent-skills.py",
        "count": len(built),
        "jurisdictions": sorted({v["jurisdiction"] for v in built.values() if v["jurisdiction"]}),
        "skills": [{"name": k, **v} for k, v in sorted(built.items())],
    }
    staged[OUT_DIR / "index.json"] = json.dumps(index, indent=1, ensure_ascii=False) + "\n"
    readme = OUT_DIR / "README.md"
    if readme.exists():
        staged[readme] = stamp_readme(readme.read_text(encoding="utf-8"), built, index["jurisdictions"], reviewed)

    # Stale folders (skills retired or renamed since the last build) go away.
    stale: list[Path] = []
    roots = [OUT_DIR] + ([PLUGIN_SKILLS_DIR] if plugin_countries else [])
    for root in roots:
        if not root.is_dir():
            continue
        for child in root.iterdir():
            if child.is_dir() and (child / "SKILL.md").exists() and (child / "SKILL.md") not in staged:
                stale.append(child)

    changed = [p for p, c in staged.items() if not p.exists() or p.read_text(encoding="utf-8") != c]
    if check_only:
        if changed or stale:
            print(f"agent-skills stale: {len(changed)} file(s) differ, {len(stale)} folder(s) to remove", file=sys.stderr)
            return 1
        print("agent-skills up to date")
        return 0

    for p, c in staged.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(c, encoding="utf-8")
    for d in stale:
        shutil.rmtree(d)
    trust_counts: dict[str, int] = {}
    for v in built.values():
        trust_counts[v["trust_label"] or "unlabelled"] = trust_counts.get(v["trust_label"] or "unlabelled", 0) + 1
    print(f"agent-skills: {len(built)} skills, {len(index['jurisdictions'])} jurisdictions, "
          f"{len(changed)} written, {len(stale)} removed; plugin countries {sorted(plugin_countries) or '-'}")
    for k, n in sorted(trust_counts.items(), key=lambda kv: -kv[1]):
        print(f"  {n:5d}  {k}")
    return 0


def main() -> int:
    args = sys.argv[1:]
    countries: set[str] = set()
    if "--plugin" in args:
        countries = {c.strip().upper() for c in args[args.index("--plugin") + 1].split(",") if c.strip()}
    return build(countries, "--check" in args)


if __name__ == "__main__":
    sys.exit(main())
