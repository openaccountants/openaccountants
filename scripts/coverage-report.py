#!/usr/bin/env python3
"""
Coverage report: tax-domain inventory for each jurisdiction pack.

Tax packs only (GOAL.md): reads the skill tree through build-index.py
(in memory, so it never lags the committed index.json), groups guides by jurisdiction
code, and reports which taxonomy domains appear present or missing. A domain-complete
row is an inventory result only. It does not verify sources, calculations, independent
pack review or named-accountant attestation, so it must not be presented as comprehensive
coverage.
Pseudo-codes (GLOBAL, INTL, EU variants, templates) are reported separately
and never counted as jurisdictions.

Owner, region and display name come from scripts/data/jurisdictions.json.
A pack README.md with an `applicable:` / `not_applicable:` block narrows the
domains that count as missing for that jurisdiction.

Usage:
    python3 scripts/coverage-report.py               # full table
    python3 scripts/coverage-report.py --summary     # counts only
    python3 scripts/coverage-report.py --missing-only
    python3 scripts/coverage-report.py --owner ryan
    python3 scripts/coverage-report.py --markdown    # for the weekly issue
    python3 scripts/coverage-report.py --json        # for open-coverage-issues.py
"""

import argparse
import collections
import importlib.util
import json
import os
import re
import sys
from datetime import date, datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(REPO_ROOT, "scripts", "data", "jurisdictions.json")

# Codes that are not jurisdictions. Canonical list; docs/COVERAGE.md points here.
PSEUDO_CODES = {"NONE", "GENERAL", "GLOBAL", "INTL", "EU", "EU-27", "EU/EEA/CH/UK", "EG-AE", "EG-SA"}

# Taxonomy domains (docs/SKILL-TAXONOMY.md) and how a guide is recognised as
# covering one: by category, or by tokens in its slug. Category is empty on
# most guides, so the slug tokens do most of the work.
DOMAINS = [
    ("IT-IND", "Individual income tax",
     {"income-tax", "individual", "personal", "pit", "self-employed", "freelance", "capital-gain", "capital-gains", "return"},
     {"federal-tax", "state"}),
    ("IT-CORP", "Corporate income tax",
     {"corporate", "corporation", "company-tax", "cit", "corporate-tax", "corporate-income"}, set()),
    ("VAT", "VAT / GST / sales tax", {"vat", "gst", "sales-tax", "consumption"}, set()),
    ("SC", "Social contributions", {"social", "ssc", "contribution", "contributions", "nic", "superannuation", "super"}, set()),
    ("PR", "Payroll withholding", {"payroll", "paye", "withholding"}, {"payroll"}),
    ("TP", "Transfer pricing", {"transfer-pricing"}, {"transfer-pricing"}),
    ("XB", "Cross-border (exit, treaties, non-residents)",
     {"exit", "departure", "treaty", "treaties", "non-resident", "nonresident", "expat", "leaving", "cross-border", "relocation"},
     {"cross-border"}),
]
# Later milestone, not counted as missing: BK bookkeeping, EI e-invoicing, FS financial statements, TO tax optimisation.
DOMAIN_CODES = [d[0] for d in DOMAINS]

STALE_DAYS = 365


def load_build_index():
    spec = importlib.util.spec_from_file_location("build_index", os.path.join(REPO_ROOT, "scripts", "build-index.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def slug_tokens(slug):
    # "malta-income-tax" -> {"malta", "income", "tax", "income-tax", "malta-income", ...}
    parts = slug.lower().split("-")
    tokens = set(parts)
    for i in range(len(parts) - 1):
        tokens.add(parts[i] + "-" + parts[i + 1])
    return tokens


def domains_of(guide):
    tokens = slug_tokens(guide["slug"])
    category = (guide.get("category") or "").lower()
    found = set()
    for code, _label, slug_hits, category_hits in DOMAINS:
        if category in category_hits or tokens & slug_hits:
            found.add(code)
    return found


def _domain_map(block, key):
    """Read an indented `KEY:\n  CODE: value` block from README frontmatter."""
    out = {}
    m = re.search(rf"^{key}:\s*\n((?:[ \t]+.*\n?)+)", block, re.MULTILINE)
    if m:
        for line in m.group(1).splitlines():
            km = re.match(r"\s*([A-Z-]+):\s*(.*)", line)
            if km:
                out[km.group(1)] = km.group(2).strip().strip("'\"")
    return out


def read_pack_readme(pack_dir):
    """Return (applicable, not_applicable, covered_by, partial) from a pack README frontmatter.

    covered_by maps a domain code to the slug that covers it when the slug
    tokens would not say so (for example IT-CORP: mt-company-tax).
    partial maps a domain code to what its skills leave out (for example
    SC: self-employed only); such a domain counts as missing until the gap
    is closed, because a skill's presence is not coverage."""
    if not pack_dir:
        return None, {}, {}, {}
    path = os.path.join(REPO_ROOT, pack_dir, "README.md")
    if not os.path.isfile(path):
        return None, {}, {}, {}
    with open(path, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    if not text.startswith("---"):
        return None, {}, {}, {}
    block = text.split("---", 2)[1] if text.count("---") >= 2 else ""
    applicable = None
    covered_by = _domain_map(block, "covered_by")
    partial = _domain_map(block, "partial")
    m = re.search(r"^applicable:\s*\[([^\]]*)\]", block, re.MULTILINE)
    if m:
        applicable = [x.strip().strip("'\"") for x in m.group(1).split(",") if x.strip()]
    not_applicable = _domain_map(block, "not_applicable")
    return applicable, not_applicable, covered_by, partial


def is_stale(guide, today):
    raw = guide.get("last_updated")
    if not raw:
        return True
    try:
        updated = datetime.strptime(str(raw)[:10], "%Y-%m-%d").date()
    except ValueError:
        return True
    return (today - updated).days > STALE_DAYS


def build_report(today=None):
    today = today or date.today()
    bi = load_build_index()
    index = bi.build_index()
    with open(DATA_PATH, encoding="utf-8") as fh:
        meta = {row["code"]: row for row in json.load(fh)}

    by_code = collections.defaultdict(list)
    for g in index["guides"]:
        by_code[str(g["jurisdiction"] or "NONE").upper()].append(g)

    rows = []
    pseudo = {}
    for code, guides in by_code.items():
        if code in PSEUDO_CODES:
            pseudo[code] = len(guides)
            continue
        info = meta.get(code, {})
        dirs = collections.Counter(os.path.dirname(g["path"]) for g in guides)
        pack_dir = info.get("dir") or dirs.most_common(1)[0][0]
        present = set()
        for g in guides:
            present |= domains_of(g)
        applicable, not_applicable, covered_by, partial = read_pack_readme(pack_dir)
        slugs = {g["slug"] for g in guides}
        present |= {code for code, slug in covered_by.items() if slug in slugs}
        present -= set(partial)
        required = set(applicable) if applicable is not None else set(DOMAIN_CODES)
        required -= set(not_applicable)
        missing = sorted(required - present, key=DOMAIN_CODES.index)
        rows.append({
            "code": code,
            "name": info.get("name") or code,
            "region": info.get("region") or "unassigned",
            "owner": info.get("owner") or "open",
            "dir": pack_dir,
            "skills": len(guides),
            "reviewed": sum(1 for g in guides if str(g.get("tier")) == "1" and g.get("reviewed_by")),
            "stale": sum(1 for g in guides if is_stale(g, today)),
            "present": sorted(present, key=DOMAIN_CODES.index),
            "missing": missing,
            "not_applicable": not_applicable,
            "partial": partial,
            "has_readme": applicable is not None or bool(not_applicable),
            "domain_complete": not missing,
        })
    # Jurisdictions listed in the data file but with no guide at all.
    for code, info in meta.items():
        if code not in by_code and code not in PSEUDO_CODES:
            rows.append({
                "code": code, "name": info.get("name") or code, "region": info.get("region") or "unassigned",
                "owner": info.get("owner") or "open", "dir": info.get("dir") or "", "skills": 0, "reviewed": 0,
                "stale": 0, "present": [], "missing": list(DOMAIN_CODES), "not_applicable": {}, "partial": {},
                "has_readme": False, "domain_complete": False,
            })
    rows.sort(key=lambda r: (r["owner"], r["region"], r["code"]))
    return {
        "generated_on": today.isoformat(),
        "guides": index["counts"]["guides"],
        "jurisdictions": len(rows),
        "pseudo_codes": pseudo,
        "domain_complete": sum(1 for r in rows if r["domain_complete"]),
        "with_readme": sum(1 for r in rows if r["has_readme"]),
        "reviewed_skills": index["counts"]["accountant_reviewed"],
        "comprehensive_packs": None,
        "comprehensive_packs_note": "Not computed: source verification, worked examples, independent pack review and full-pack accountant attestation require separate checks.",
        "rows": rows,
    }


def summary_lines(report):
    rows = report["rows"]
    lines = [
        f"Tax-domain inventory report, {report['generated_on']}",
        f"Skills: {report['guides']:,}  Jurisdiction units: {report['jurisdictions']}  "
        f"Tax-domain maps with no missing domain: {report['domain_complete']}  Packs with README: {report['with_readme']}  "
        f"Reviewed skills: {report['reviewed_skills']}",
        "Comprehensive packs: not computed by this inventory report.",
        f"Pseudo-codes (not jurisdictions): {', '.join(f'{k} ({v})' for k, v in sorted(report['pseudo_codes'].items()))}",
        "",
        f"{'Owner':<9}{'Juris':>6}{'Domain OK':>10}{'Thin(<=7)':>11}{'No skills':>11}{'Stale skills':>14}",
    ]
    for owner in sorted({r["owner"] for r in rows}):
        rs = [r for r in rows if r["owner"] == owner]
        lines.append(
            f"{owner:<9}{len(rs):>6}{sum(1 for r in rs if r['domain_complete']):>10}"
            f"{sum(1 for r in rs if 0 < r['skills'] <= 7):>11}{sum(1 for r in rs if r['skills'] == 0):>11}"
            f"{sum(r['stale'] for r in rs):>14}"
        )
    return lines


def table_lines(rows, markdown=False):
    if markdown:
        out = [
            "> Inventory only: domain presence does not verify sources, calculations, independent review or accountant attestation. Comprehensive coverage is not computed.",
            "",
            "| Owner | Region | Code | Name | Skills | Reviewed | Stale | Missing domains |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for r in rows:
            out.append(f"| {r['owner']} | {r['region']} | {r['code']} | {r['name']} | {r['skills']} | {r['reviewed']} | {r['stale']} | {', '.join(r['missing']) or 'none'} |")
        return out
    out = [f"{'owner':<9}{'region':<13}{'code':<9}{'skills':>7}{'rev':>5}{'stale':>7}  missing"]
    for r in rows:
        out.append(f"{r['owner']:<9}{r['region']:<13}{r['code']:<9}{r['skills']:>7}{r['reviewed']:>5}{r['stale']:>7}  {', '.join(r['missing']) or '-'}")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--missing-only", action="store_true")
    ap.add_argument("--owner")
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    report = build_report()
    rows = report["rows"]
    if args.owner:
        rows = [r for r in rows if r["owner"].lower() == args.owner.lower()]
    if args.missing_only:
        rows = [r for r in rows if r["missing"]]

    if args.json:
        report["rows"] = rows
        json.dump(report, sys.stdout, indent=1)
        sys.stdout.write("\n")
        return 0
    if args.markdown:
        print("## " + summary_lines(report)[0])
        print()
        print("```")
        print("\n".join(summary_lines(report)[1:]))
        print("```")
        print()
        print("\n".join(table_lines(rows, markdown=True)))
        return 0
    print("\n".join(summary_lines(report)))
    if not args.summary:
        print()
        print("\n".join(table_lines(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
