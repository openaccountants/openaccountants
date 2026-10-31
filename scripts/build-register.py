#!/usr/bin/env python3
"""Build skills/REGISTER.csv and skills/REGISTER.md from the skill tree and each skill's text.

One row per skill: country, GOAL.md domain, tax year, who signed, when last updated,
and one pass/fail column per mechanical line of the standard (scripts/skill_checks.py).
Every count on the site, the README and the coverage report should come from this
file, not from a fresh query. The inventory is built in memory through
scripts/build-index.py (the same walk that writes index.json), so it never lags the
committed index.json, which only the platform sync rewrites:

    python3 scripts/build-register.py

The domain is the GOAL.md code (IT-IND, IT-CORP, VAT, SC, PR, TP, XB) read the same
way scripts/coverage-report.py reads it: slug tokens and category through
``domains_of()``, plus the pack README's ``covered_by`` map. A skill in a country whose
README has no domain model also gets ``task_guess``, the old slug guess, as a fallback.

``duplicate`` marks a skill that shares a (country, domain) cell with another skill
while the README's ``covered_by`` does not name it: two skills for one job, and the
README has not said which one an AI should load.
"""
import collections
import csv
import importlib.util
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


build_index = _load("build_index", "build-index.py")
coverage = _load("coverage_report", "coverage-report.py")
skill_checks = _load("skill_checks", "skill_checks.py")
DOMAIN_CODES = coverage.DOMAIN_CODES
PSEUDO_CODES = coverage.PSEUDO_CODES

NEARLY_DONE_PER_COUNTRY = 3

# Old slug guess, kept only as `task_guess` for countries whose README has no
# domain model. The domain column is the GOAL.md code; this is a hint.
TASKS = [
    ("overview", r"overview|tax-system|at-a-glance|tax-guide$|tax-basics"),
    ("vat-gst", r"\bvat\b|\bgst\b|sales-tax|sales tax|\bhst\b|\bpst\b|\bqst\b|value-added|value added|\boss\b|\bioss\b|e-?invoic|reverse-charge|consumption-tax|\bjct\b"),
    ("payroll", r"payroll|\bpaye\b|pay-as-you|wage-tax|employer-contribution|social-security|social-insurance|social-contribution|\bssc\b|national-insurance|superannuation|\bcpp\b|employment-income|employer"),
    ("transfer-pricing", r"transfer-pricing|\btp\b|arms-length|cbcr|country-by-country"),
    ("withholding", r"withholding|\bwht\b|1099"),
    ("cross-border", r"cross-border|treaty|\bdta\b|expat|non-resident|nonresident|residency|relocat|permanent-establishment|exit-tax|digital-nomad|remote-work|foreign-income|double-tax"),
    ("crypto", r"crypto|bitcoin|digital-asset|virtual-asset"),
    ("corporate-tax", r"corporate|\bcit\b|company-tax|corporation-tax|business-tax|franchise-tax|\bcorp\b|\bcfc\b|participation-exemption|minimum-tax|pillar|business-income|trade-tax|profits-tax"),
    ("individual-tax", r"individual|personal-income|income-tax|\bpit\b|self-employ|freelanc|sole-trader|sole-prop|capital-gains|dividend|rental|inheritance|estate|gift-tax|1040|schedule-|tax-optimi|wealth-tax|property-tax|stamp"),
    ("accounting-reporting", r"bookkeep|financial-statement|annual-accounts|ifrs|gaap|audit|financial-report|year-end|month-end|ledger|chart-of-accounts"),
    ("formation-registration", r"formation|incorporat|registration|company-law|entity-choice|\bllc\b|startup|set-?up"),
    ("filing-deadlines", r"deadline|calendar|filing|return\b|compliance|tax-return"),
]


def task_guess(skill, fm):
    slug = (skill["slug"] + " " + str(skill.get("name") or "")).lower()
    for task, pattern in TASKS:
        if re.search(pattern, slug):
            return task
    desc = str(fm.get("description") or "").lower().replace(" ", "-")
    for task, pattern in TASKS:
        if re.search(pattern, desc):
            return task
    return "unclassified"


def nearly_done(tax_rows):
    """Per country, the skills closest to check (c): fewest rows missing, then most rows."""
    by_country = collections.defaultdict(list)
    for r in tax_rows:
        if r["_rates_missing"] and r["jurisdiction"] not in PSEUDO_CODES and r["jurisdiction"] != "?":
            by_country[r["jurisdiction"]].append(r)
    out = []
    for code in sorted(by_country):
        ranked = sorted(by_country[code], key=lambda r: (r["_rates_missing"], -r["rates_rows_total"], r["slug"]))
        out += ranked[:NEARLY_DONE_PER_COUNTRY]
    return out


def load_jurisdiction_dirs():
    with open(SCRIPTS / "data" / "jurisdictions.json", encoding="utf-8") as fh:
        return {row["code"]: row.get("dir") or "" for row in json.load(fh)}


def main():
    index = build_index.build_index()
    pack_dirs = load_jurisdiction_dirs()
    readmes = {}  # pack dir -> (applicable, not_applicable, covered_by, partial)

    def readme_for(code, path):
        pack_dir = pack_dirs.get(code) or os.path.dirname(path)
        if pack_dir not in readmes:
            readmes[pack_dir] = coverage.read_pack_readme(pack_dir)
        return readmes[pack_dir]

    rows = []
    for s in index["guides"]:
        text = (ROOT / s["path"]).read_text(encoding="utf-8", errors="replace")
        fm = skill_checks.read_frontmatter(text)
        code = str(s.get("jurisdiction") or fm.get("jurisdiction") or "?").upper()
        applicable, not_applicable, covered_by, partial = readme_for(code, s["path"])
        has_model = applicable is not None or bool(not_applicable) or bool(covered_by)
        domains, named = coverage.cell_domains(s, covered_by)
        results = skill_checks.run_checks(s["path"], text, fm)
        rates = skill_checks.rates_row_counts(text)
        row = {
            "slug": s["slug"],
            "jurisdiction": code,
            "domain": "+".join(sorted(domains, key=DOMAIN_CODES.index)),
            "domain_source": "readme" if named else ("slug" if domains else ""),
            "task_guess": "" if has_model else task_guess(s, fm),
            "scope": skill_checks.scope_of(s["path"], fm),
            "tax_year": s.get("tax_year") or "",
            "tier": s["tier"],
            "label": fm.get("trust_label", ""),
            "review_status": fm.get("review_status", ""),
            "signed_by": (s.get("reviewed_by") or "") if s["tier"] == 1 else "",
            "authored_by": fm.get("authored_by", ""),
            "last_updated": s.get("last_updated") or "",
            "category_raw": s.get("category") or "",
            "path": s["path"],
            "rates_rows_total": rates["total"],
            "rates_rows_linked": rates["linked"],
            "rates_rows_unverified": rates["unverified"],
            "rates_linked_pct": "" if rates["linked_pct"] is None else rates["linked_pct"],
            "rates_unverified_pct": "" if rates["unverified_pct"] is None else rates["unverified_pct"],
            "_rates_missing": rates["missing"],
            "_domains": domains,
            "_named": named,
        }
        for name in skill_checks.CHECK_NAMES:
            problems = results[name]
            row["check_" + name] = "pass" if not problems else "fail: " + "; ".join(problems)
        row["passed"] = sum(1 for name in skill_checks.CHECK_NAMES if not results[name])
        rows.append(row)

    # Duplicates: 2+ skills in one (country, domain) cell, and the README's
    # covered_by does not name this one. Pseudo-codes are not countries.
    cell = collections.defaultdict(list)
    for r in rows:
        if r["jurisdiction"] in PSEUDO_CODES or r["jurisdiction"] == "?":
            continue
        for d in r["_domains"]:
            cell[(r["jurisdiction"], d)].append(r)
    for r in rows:
        dup = []
        for d in sorted(r["_domains"], key=DOMAIN_CODES.index):
            others = [x for x in cell.get((r["jurisdiction"], d), []) if x is not r]
            if others and d not in r["_named"]:
                dup.append(d)
        r["duplicate"] = "+".join(dup)
    dup_cells = {(r["jurisdiction"], d) for r in rows for d in r["duplicate"].split("+") if d}

    rows.sort(key=lambda r: (r["jurisdiction"], r["domain"], r["slug"]))
    fieldnames = [k for k in rows[0].keys() if not k.startswith("_")]
    out_csv = ROOT / "skills" / "REGISTER.csv"
    with out_csv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    C = collections.Counter
    signed = [r for r in rows if r["tier"] == 1]
    tax_rows = [r for r in rows if r["scope"] == "tax"]
    countries = C(r["jurisdiction"] for r in rows
                  if r["jurisdiction"] not in PSEUDO_CODES and r["jurisdiction"] != "?")
    by_domain = C()
    for r in rows:
        for d in r["_domains"]:
            by_domain[d] += 1
    no_domain = sum(1 for r in rows if not r["_domains"])
    dup_skills = [r for r in rows if r["duplicate"]]

    lines = [
        "# Skills register", "",
        f"Generated from the skill tree on {index.get('generated_at', '')[:10]} by `scripts/build-register.py`. "
        "One row per skill in `REGISTER.csv`. This file is the summary.", "",
        "## Totals", "",
        f"- Skills: {len(rows)}",
        f"- Jurisdictions: {len(C(r['jurisdiction'] for r in rows))} ({len(countries)} countries or states, the rest pseudo-codes)",
        f"- Tax year 2026: {sum(1 for r in rows if r['tax_year'] == '2026')}; "
        f"still 2025: {sum(1 for r in rows if r['tax_year'] == '2025')}; "
        f"no year: {sum(1 for r in rows if not r['tax_year'])}",
        f"- Signed by a named accountant (tier 1): {len(signed)}, in "
        f"{', '.join(f'{k} ({v})' for k, v in C(r['jurisdiction'] for r in signed).most_common())}",
        f"- Scope: {len(tax_rows)} tax skills (deep-tax shape applies), "
        f"{sum(1 for r in rows if r['scope'] == 'general')} accounting-pack skills (general template), "
        f"{sum(1 for r in rows if r['scope'] == 'other')} other (routers, templates, patterns)",
        f"- Domain from the README `covered_by`: {sum(1 for r in rows if r['domain_source'] == 'readme')}; "
        f"from the slug: {sum(1 for r in rows if r['domain_source'] == 'slug')}; no tax domain: {no_domain}",
        f"- Pass all {len(skill_checks.CHECK_NAMES)} checks: {sum(1 for r in tax_rows if r['passed'] == len(skill_checks.CHECK_NAMES))} of {len(tax_rows)} tax skills",
        f"- Duplicates: {len(dup_skills)} skills in {len(dup_cells)} (country, domain) cells where the README does not name which skill covers the job",
        "",
        "## Pass rate per check", "",
        "Tax skills only (the deep-tax shape applies to them). One column per check in `REGISTER.csv`; "
        "the letters are the order in `scripts/skill_checks.py`.", "",
        "| | Check | Pass | Fail | Pass rate |", "|---|---|---:|---:|---:|",
    ]
    for letter, name, func in skill_checks.CHECKS:
        passed = sum(1 for r in tax_rows if r["check_" + name] == "pass")
        failed = len(tax_rows) - passed
        rate = (100 * passed / len(tax_rows)) if tax_rows else 0
        lines.append(f"| ({letter}) | `{name}` | {passed} | {failed} | {rate:.0f}% |")
    rates_total = sum(r["rates_rows_total"] for r in tax_rows)
    rates_linked = sum(r["rates_rows_linked"] for r in tax_rows)
    rates_unverified = sum(r["rates_rows_unverified"] for r in tax_rows)
    lines += ["", "## Rates rows", "",
              f"Tax skills only: {rates_total} rows, {rates_linked} linked "
              f"({100 * rates_linked / max(rates_total, 1):.1f}%), {rates_unverified} marked unverified "
              f"({100 * rates_unverified / max(rates_total, 1):.1f}%), "
              f"{rates_total - rates_linked - rates_unverified} neither. "
              "A row marked unverified is not counted as linked.", ""]
    lines += ["", "## By domain", "", "A skill covering two domains counts in both.", "",
              "| Domain | Skills | Signed |", "|---|---:|---:|"]
    for d in DOMAIN_CODES:
        lines.append(f"| {d} | {by_domain[d]} | {sum(1 for r in signed if d in r['_domains'])} |")
    lines.append(f"| (no tax domain) | {no_domain} | {sum(1 for r in signed if not r['_domains'])} |")
    lines += ["", "## Country by domain", "",
              "Count of skills in each (country, domain) cell. `*` means at least one is signed by a named "
              "accountant; `!` means two or more skills share the cell and the README does not name which "
              "one covers it (a duplicate).", "",
              "| Country | " + " | ".join(DOMAIN_CODES) + " | All pass | 2026 | Signed | Total |",
              "|---|" + "---:|" * (len(DOMAIN_CODES) + 4)]
    for j, _ in sorted(countries.items(), key=lambda kv: (-kv[1], kv[0])):
        xs = [r for r in rows if r["jurisdiction"] == j]
        cells = []
        for d in DOMAIN_CODES:
            in_cell = [r for r in xs if d in r["_domains"]]
            if not in_cell:
                cells.append("")
                continue
            mark = str(len(in_cell))
            if any(r["tier"] == 1 for r in in_cell):
                mark += "*"
            if (j, d) in dup_cells:
                mark += "!"
            cells.append(mark)
        lines.append(f"| {j} | " + " | ".join(cells) +
                     f" | {sum(1 for r in xs if r['scope'] == 'tax' and r['passed'] == len(skill_checks.CHECK_NAMES))}"
                     f" | {sum(1 for r in xs if r['tax_year'] == '2026')} | {sum(1 for r in xs if r['tier'] == 1)} | {len(xs)} |")
    lines += ["", "## Duplicates", "",
              "Skills that share a (country, domain) cell with another skill and are not named in the pack "
              "README's `covered_by`. Fix by naming one in the README or merging the skills.", ""]
    if dup_skills:
        lines += ["| Country | Domain | Skill |", "|---|---|---|"]
        for r in dup_skills:
            lines.append(f"| {r['jurisdiction']} | {r['duplicate']} | `{r['slug']}` |")
    else:
        lines.append("None.")
    lines += ["", "## Nearly done", "",
              f"For each country, the {NEARLY_DONE_PER_COUNTRY} tax skills with the fewest rates rows "
              "neither linked nor marked unverified. A skill with no rates table or none missing is not listed.", ""]
    nearly = nearly_done(tax_rows)
    if nearly:
        lines += ["| Country | Skill | Missing | Rows | Linked % | Unverified % |", "|---|---|---:|---:|---:|---:|"]
        for r in nearly:
            lines.append(f"| {r['jurisdiction']} | `{r['slug']}` | {r['_rates_missing']} | {r['rates_rows_total']} "
                         f"| {r['rates_linked_pct']} | {r['rates_unverified_pct']} |")
    else:
        lines.append("None.")
    (ROOT / "skills" / "REGISTER.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {out_csv} ({len(rows)} rows) and skills/REGISTER.md")
    print(f"tax skills: {len(tax_rows)}; duplicates: {len(dup_skills)} skills in {len(dup_cells)} cells")
    for letter, name, _ in skill_checks.CHECKS:
        passed = sum(1 for r in tax_rows if r["check_" + name] == "pass")
        print(f"  ({letter}) {name:<20} {passed:>5} / {len(tax_rows)} pass")


if __name__ == "__main__":
    main()
