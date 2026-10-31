#!/usr/bin/env python3
"""Write a README.md map for every country pack that has none.

Dry run by default; pass --apply to write. Never overwrites a README.

The README is the pack's registry: one row per GOAL.md domain naming the skills
that cover it. Everything here is read from the skill files. Whether a domain
truly does not apply in a country is a statement of law, so it is never guessed:
every generated README lists all seven domains as applicable until someone has
checked and says otherwise, and the file says that plainly.

    python3 scripts/build-pack-readmes.py --skip australia,eu [--apply]
"""
import argparse
import collections
import importlib.util
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


coverage = _load("coverage_report", "coverage-report.py")
repo_layout = _load("repo_layout", "repo_layout.py")
DOMAIN_NAMES = {
    "IT-IND": "individual income tax", "IT-CORP": "corporate income tax", "VAT": "indirect tax",
    "SC": "social contributions", "PR": "payroll withholding", "TP": "transfer pricing", "XB": "cross-border",
}
INDIVIDUAL = re.compile(r"individual|personal|pit\b|self-employed|freelanc|capital-gain")
UPPER = {"uk", "uae", "dr", "eu", "us"}


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for line in m.group(1).split("\n"):
            kv = re.match(r"([a-z_]+):\s*(.*)$", line)
            if kv:
                out[kv.group(1)] = kv.group(2).strip().strip("\"'")
    return out


def domains(slug, fm):
    """The same rule coverage-report.py uses, so the map and the report agree."""
    guide = {"slug": slug, "name": slug, "category": fm.get("category", ""), "domain": fm.get("domain", ""), "path": slug}
    try:
        found = set(coverage.domains_of(guide))
    except Exception:
        return []
    # "income-tax" in a corporate slug, or a VAT skill filed under an income category,
    # is not an individual income tax skill.
    if found & {"IT-CORP", "VAT"} and not INDIVIDUAL.search(slug):
        found.discard("IT-IND")
    return sorted(found)


def status(fm):
    if str(fm.get("tier")) == "1":
        return "accountant-reviewed"
    return "sourced from the law"


def build(pack):
    rows, codes, years = collections.defaultdict(list), collections.Counter(), collections.Counter()
    other = []
    for f in sorted(pack.glob("*.md")):
        if f.name.lower().startswith("readme"):
            continue
        fm = frontmatter(f.read_text(errors="ignore"))
        slug = f.stem
        if fm.get("jurisdiction"):
            codes[fm["jurisdiction"]] += 1
        if fm.get("tax_year"):
            years[fm["tax_year"]] += 1
        ds = [d for d in domains(slug, fm) if d in DOMAIN_NAMES]
        for d in ds:
            rows[d].append((slug, status(fm), fm.get("tax_year", "not stated")))
        if not ds:
            other.append(slug)
    if not codes:
        return None
    code = codes.most_common(1)[0][0]
    name = " ".join(w.upper() if w in UPPER else w.capitalize() for w in pack.name.split("-"))
    year_line = ", ".join(f"{n} on {y}" for y, n in sorted(years.items(), reverse=True)) or "no tax year stated"
    lines = [
        "---", f"jurisdiction: {code}", "applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]",
        "not_applicable: {}", "covered_by: {}", "partial: {}", "---", "",
        f"# {name}: tax pack", "",
        "This map is generated from the skill files. All seven domains are listed as applicable until "
        "someone has checked which ones exist here against the law.", "",
        f"Tax years in this pack: {year_line}.", "", "## Domains", "",
        "| Domain | Skill | Status |", "|---|---|---|",
    ]
    for d, label in DOMAIN_NAMES.items():
        found = rows.get(d)
        if found:
            skills = ", ".join(f"{s} ({y})" for s, _, y in found)
            st = "; ".join(sorted({x for _, x, _ in found}))
            lines.append(f"| {d}, {label} | {skills} | {st} |")
        else:
            lines.append(f"| {d}, {label} | (missing) | |")
    if other:
        lines += ["", "## Other skills", "", *[f"- {s}" for s in other]]
    lines += ["", "## Official sources", "", "Each skill lists its own sources with the date last read.", ""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--skip", default="")
    a = ap.parse_args()
    skip = {s for s in a.skip.split(",") if s}
    wrote, empty = 0, []
    for pack in repo_layout.country_dirs(SKILLS):
        if pack.name in skip or (pack / "README.md").exists():
            continue
        text = build(pack)
        if text is None:
            empty.append(pack.name)
            continue
        wrote += 1
        if a.apply:
            (pack / "README.md").write_text(text)
    print(f"{'wrote' if a.apply else 'would write'} {wrote} READMEs; no skills found in: {empty or 'none'}")


if __name__ == "__main__":
    main()
