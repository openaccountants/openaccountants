#!/usr/bin/env python3
"""Build skills/REGISTER.csv and skills/REGISTER.md from index.json and each skill's frontmatter.

One row per skill: country, task, tax year, who signed, when last updated. Every count
on the site, the README and the coverage report should come from this file, not from a
fresh query. Run after scripts/build-index.py:

    python3 scripts/build-register.py

Task is read from the slug first, then the description (marked low confidence), so a
skill can be wrong here; fix it by giving the skill a `task:` frontmatter key, which wins.
"""
import collections
import csv
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
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
CORE = ["overview", "individual-tax", "corporate-tax", "vat-gst", "payroll", "withholding",
        "transfer-pricing", "cross-border", "accounting-reporting", "filing-deadlines"]
META = {"orchestrator", "patterns", "pattern", "template", "foundation", "integration", "intelligence", "vertical"}


def frontmatter(path):
    try:
        text = (ROOT / path).read_text(errors="ignore")
    except OSError:
        return {}
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if line and not line.startswith(" ") and ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def classify(skill, fm):
    if fm.get("task"):
        return fm["task"], "declared"
    if str(skill.get("category") or "") in META:
        return "meta:" + skill["category"], "high"
    slug = (skill["slug"] + " " + skill["name"]).lower()
    for task, pattern in TASKS:
        if re.search(pattern, slug):
            return task, "high"
    desc = fm.get("description", "").lower().replace(" ", "-")
    for task, pattern in TASKS:
        if re.search(pattern, desc):
            return task, "low"
    return "unclassified", "low"


def main():
    index = json.loads((ROOT / "index.json").read_text())
    rows = []
    for s in index["guides"]:
        fm = frontmatter(s["path"])
        task, conf = classify(s, fm)
        rows.append({
            "slug": s["slug"],
            "jurisdiction": s.get("jurisdiction") or fm.get("jurisdiction") or "?",
            "task": task,
            "task_confidence": conf,
            "tax_year": s.get("tax_year") or "",
            "tier": s["tier"],
            "label": fm.get("trust_label", ""),
            "review_status": fm.get("review_status", ""),
            "signed_by": (s.get("reviewed_by") or "") if s["tier"] == 1 else "",
            "authored_by": fm.get("authored_by", ""),
            "last_updated": s.get("last_updated") or "",
            "category_raw": s.get("category") or "",
            "path": s["path"],
        })
    rows.sort(key=lambda r: (r["jurisdiction"], r["task"], r["slug"]))

    out_csv = ROOT / "skills" / "REGISTER.csv"
    with out_csv.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    C = collections.Counter
    by_task = C(r["task"] for r in rows)
    signed = [r for r in rows if r["tier"] == 1]
    countries = C(r["jurisdiction"] for r in rows
                  if "-" not in r["jurisdiction"] and r["jurisdiction"] not in ("GLOBAL", "INTL", "?"))
    lines = [
        "# Skills register", "",
        f"Generated from `index.json` ({index.get('generated_at', '')[:10]}) by `scripts/build-register.py`. "
        "One row per skill in `REGISTER.csv`. This file is the summary.", "",
        "## Totals", "",
        f"- Skills: {len(rows)}",
        f"- Jurisdictions: {len(C(r['jurisdiction'] for r in rows))}",
        f"- Tax year 2026: {sum(1 for r in rows if r['tax_year'] == '2026')}; "
        f"still 2025: {sum(1 for r in rows if r['tax_year'] == '2025')}; "
        f"no year: {sum(1 for r in rows if not r['tax_year'])}",
        f"- Signed by a named accountant (tier 1): {len(signed)}, in "
        f"{', '.join(f'{k} ({v})' for k, v in C(r['jurisdiction'] for r in signed).most_common())}",
        f"- Task read from the slug: {sum(1 for r in rows if r['task_confidence'] == 'high')}; "
        f"from the description only: {sum(1 for r in rows if r['task_confidence'] == 'low' and r['task'] != 'unclassified')}; "
        f"unclassified: {by_task['unclassified']}", "",
        "## By task", "", "| Task | Skills | Signed |", "|---|---:|---:|",
    ]
    for task, n in by_task.most_common():
        lines.append(f"| {task} | {n} | {sum(1 for r in signed if r['task'] == task)} |")
    lines += ["", "## Country by task (top 40 by skill count)", "",
              "Count of skills; `*` means at least one is signed by a named accountant.", "",
              "| Country | " + " | ".join(CORE) + " | 2026 | Signed | Total |",
              "|---|" + "---:|" * (len(CORE) + 3)]
    for j, _ in countries.most_common(40):
        xs = [r for r in rows if r["jurisdiction"] == j]
        cells = []
        for c in CORE:
            n = sum(1 for r in xs if r["task"] == c)
            s = sum(1 for r in xs if r["task"] == c and r["tier"] == 1)
            cells.append((str(n) + ("*" if s else "")) if n else "")
        lines.append(f"| {j} | " + " | ".join(cells) +
                     f" | {sum(1 for r in xs if r['tax_year'] == '2026')} | {sum(1 for r in xs if r['tier'] == 1)} | {len(xs)} |")
    (ROOT / "skills" / "REGISTER.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {out_csv} ({len(rows)} rows) and skills/REGISTER.md")


if __name__ == "__main__":
    main()
