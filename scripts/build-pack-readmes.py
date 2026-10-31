#!/usr/bin/env python3
"""Build the plain-English README for each country pack.

Dry run by default; pass --apply to write.

A README is rebuilt if it is missing or still carries the "This map is generated"
marker. Its frontmatter is kept byte for byte, because scripts read it. Hand-written
READMEs are left alone unless --labels is passed, which changes only the first
column of the Domain table to the plain names.

Everything here is read from the skill files, the README frontmatter and the open
"[XX] Complete the pack" issues. Whether a tax truly does not apply in a country is
a statement of law, so it is never guessed: a tax with no skill reads Missing, and
the file says nobody has checked yet that it applies.

    python3 scripts/build-pack-readmes.py --skip australia,malta [--labels] [--apply]
"""
import argparse
import collections
import importlib.util
import json
import pathlib
import re
import subprocess

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
    "IT-IND": "Income tax", "IT-CORP": "Company tax", "VAT": "VAT or sales tax",
    "SC": "Social contributions", "PR": "Payroll", "TP": "Transfer pricing", "XB": "Cross-border",
}
OLD_LABELS = {
    "Domain": "Tax", "IT-IND, individual income tax": "Income tax", "IT-IND": "Income tax",
    "IT-CORP, corporate income tax": "Company tax", "IT-CORP": "Company tax",
    "VAT": "VAT or sales tax", "VAT, indirect tax": "VAT or sales tax",
    "SC, social contributions": "Social contributions", "SC": "Social contributions",
    "PR, payroll withholding": "Payroll", "PR": "Payroll",
    "TP, transfer pricing": "Transfer pricing", "TP": "Transfer pricing",
    "XB, cross-border": "Cross-border", "XB": "Cross-border",
    "SC, PR": "Social contributions, payroll", "SC / PR": "Social contributions, payroll",
}
MARKER = "This map is generated"
UPPER = {"uk", "uae", "dr", "eu", "us"}
ACRONYMS = {
    "vat": "VAT", "gst": "GST", "paye": "PAYE", "cit": "CIT", "pit": "PIT", "cgt": "CGT", "hst": "HST",
    "itbis": "ITBIS", "igv": "IGV", "iva": "IVA", "isr": "ISR", "wht": "WHT", "uif": "UIF", "sdl": "SDL",
    "cfc": "CFC", "dta": "DTA", "ct": "CT", "mpf": "MPF", "nhi": "NHI", "sst": "SST", "usn": "USN", "tds": "TDS",
    "gct": "GCT", "cpf": "CPF", "epf": "EPF", "socso": "SOCSO", "sscl": "SSCL", "inss": "INSS", "isv": "ISV",
    "itbms": "ITBMS", "rett": "RETT", "gosi": "GOSI", "bvi": "BVI", "eobi": "EOBI", "png": "PNG", "pf": "PF",
    "esi": "ESI", "pcb": "PCB", "npd": "NPD", "sme": "SME", "tgca": "TGCA", "ait": "AIT", "ama": "AMA", "mli": "MLI", "pe": "PE", "sez": "SEZ", "ssnit": "SSNIT", "nssf": "NSSF",
}


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out = {}
    if m:
        for line in m.group(1).split("\n"):
            kv = re.match(r"([a-z_]+):\s*(.*)$", line)
            if kv:
                out[kv.group(1)] = kv.group(2).strip().strip("\"'")
    return out


def name_of(pack):
    return " ".join(w.upper() if w in UPPER else w.capitalize() for w in pack.name.split("-"))


def readable(slug, pack, code):
    """A skill's name from its slug, without the country prefix."""
    words = slug.split("-")
    prefix = pack.name.split("-")
    if words[: len(prefix)] == prefix:
        words = words[len(prefix):]
    elif words[0] == code.lower():
        words = words[1:]
    if not words:
        return name_of(pack)
    text = " ".join(ACRONYMS.get(w, w) for w in words).replace("VAT GST", "VAT or GST")
    return text[0].upper() + text[1:]


def split_frontmatter(text):
    m = re.match(r"---\n.*?\n---\n", text, re.S)
    return m.group(0) if m else None


def open_issues():
    """{code: url} for the open "[XX] Complete the pack" issues. Empty without gh."""
    try:
        out = subprocess.run(
            ["gh", "issue", "list", "-R", "openaccountants/openaccountants", "--state", "open",
             "--search", "Complete the pack in:title", "--limit", "500", "--json", "title,url"],
            capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return {}
    found = {}
    for issue in json.loads(out):
        m = re.fullmatch(r"\[([A-Z-]+)\] Complete the pack", issue["title"])
        if m:
            found[m.group(1)] = issue["url"]
    return found


def plural(n):
    return f"{n} skill" if n == 1 else f"{n} skills"


def build(pack, issues):
    path = pack / "README.md"
    old = path.read_text() if path.exists() else ""
    head = split_frontmatter(old)
    skills = []
    for f in sorted(pack.glob("*.md")):
        if not f.name.lower().startswith("readme"):
            skills.append((f, frontmatter(f.read_text(errors="ignore"))))
    codes = collections.Counter(fm["jurisdiction"] for _, fm in skills if fm.get("jurisdiction"))
    if not codes:
        return None
    code = codes.most_common(1)[0][0]
    if head is None:
        head = (f"---\njurisdiction: {code}\napplicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]\n"
                "not_applicable: {}\ncovered_by: {}\npartial: {}\n---\n")
    rel = str(pack.relative_to(ROOT))
    _, not_applicable, covered_by, partial = coverage.read_pack_readme(rel)
    rows, other, years = collections.defaultdict(list), [], collections.Counter()
    for f, fm in skills:
        slug = f.stem
        guide = {"slug": slug, "name": slug, "category": fm.get("category", ""),
                 "domain": fm.get("domain", ""), "path": f"{rel}/{f.name}"}
        years[fm.get("tax_year") or "not stated"] += 1
        found, _ = coverage.cell_domains(guide, covered_by)
        item = (slug, fm.get("tax_year") or "not stated", coverage.on_current_year(guide))
        for d in found & set(DOMAIN_NAMES):
            rows[d].append(item)
        if not found & set(DOMAIN_NAMES):
            other.append(item)

    year_line = ", ".join(f"{y} ({plural(n)})" for y, n in sorted(years.items(), reverse=True))
    lines = [f"# {name_of(pack)}: tax pack", "", f"<!-- {MARKER} by scripts/build-pack-readmes.py. Do not edit by hand. -->",
             "", f"Tax years: {year_line}.", "", "| Tax | Skill | Tax year | Status |", "|---|---|---|---|"]
    todo = []
    link = lambda slug: f"[{readable(slug, pack, code)}]({slug}.md)"
    any_missing = False
    for d, label in DOMAIN_NAMES.items():
        found = rows.get(d, [])
        if d in not_applicable:
            lines.append(f"| {label} | | | Does not apply: {not_applicable[d]} |")
            continue
        if not found:
            any_missing = True
            lines.append(f"| {label} | | | Missing |")
            todo.append(f"Write the {label if d == 'VAT' else label.lower()} skill.")
            continue
        stale = [s for s, _, current in found if not current]
        if d in partial:
            status = f"Partly covered: {partial[d]}"
            todo.append(f"{label}: finish what is left out ({partial[d]}).")
        elif stale:
            status = "Needs updating"
            todo.append(f"{label}: bring {', '.join(link(s) for s in stale)} up to the current tax year.")
        else:
            status = "Ready"
        cell = ", ".join(link(s) for s, _, _ in found)
        yrs = ", ".join(sorted({y for _, y, _ in found}, reverse=True))
        lines.append(f"| {label} | {cell} | {yrs} | {status} |")
    lines += ["", "Ready means the skill is on the current tax year. It does not mean an accountant has reviewed it."]
    if any_missing:
        lines[-1] += " Missing means we have no skill yet; nobody has checked yet that the tax applies here."
    lines += ["", "## What still needs doing", ""]
    lines += [f"- {t}" for t in todo] or ["Nothing is missing or out of date."]
    if code in issues:
        lines += ["", f"Tracked in [\\[{code}\\] Complete the pack]({issues[code]})."]
    if other:
        lines += ["", "## Other skills", "", *[f"- {link(s)} ({y})" for s, y, _ in other]]
    return head + "\n" + "\n".join(lines) + "\n"


def relabel(text):
    """Change only the first column of the Domain table."""
    out, in_table = [], False
    for line in text.split("\n"):
        m = re.match(r"\|\s*([^|]*?)\s*\|(.*)$", line)
        if not m:
            in_table = False
        elif m.group(1) == "Domain":
            in_table = True
        if in_table and m and m.group(1) in OLD_LABELS:
            line = f"| {OLD_LABELS[m.group(1)]} |{m.group(2)}"
        out.append(line)
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--labels", action="store_true", help="also relabel hand-written READMEs")
    ap.add_argument("--skip", default="")
    a = ap.parse_args()
    skip = {s for s in a.skip.split(",") if s}
    issues = open_issues()
    wrote, labelled, empty = 0, 0, []
    for pack in repo_layout.country_dirs(SKILLS):
        path = pack / "README.md"
        if pack.name in skip:
            continue
        if path.exists() and MARKER not in path.read_text():
            new = relabel(path.read_text())
            if a.labels and new != path.read_text():
                labelled += 1
                if a.apply:
                    path.write_text(new)
            continue
        text = build(pack, issues)
        if text is None:
            empty.append(pack.name)
            continue
        wrote += 1
        if a.apply:
            path.write_text(text)
    print(f"{'wrote' if a.apply else 'would write'} {wrote} READMEs, relabelled {labelled}; "
          f"no skills found in: {empty or 'none'}")


if __name__ == "__main__":
    main()
