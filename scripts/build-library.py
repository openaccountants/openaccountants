#!/usr/bin/env python3
"""Build library/<country>/figures.json and sources.json from the research packs.

The library is the first layer of the data chain: each tax figure once, with the
official page it was read on and a verbatim quote from that page. Skills are the
second layer and should state the library value character for character
(check ``figure_in_library`` in scripts/skill_checks.py warns where they differ).

The packs are built in the private research library (one ``pack/<CC>.json`` per
country; see that repository's PACK.md). This script reads them from a path you
give it and publishes only the figure fields. Saved copies of the official pages,
pack notes and country notes stay private and are never read here.

    python3 scripts/build-library.py /path/to/oa-library            # dry run: counts only
    python3 scripts/build-library.py /path/to/oa-library --write    # write library/
    python3 scripts/build-library.py /path/to/oa-library --only IE --write

Which pack files are read: ``pack/<CC>.json`` only, the country's merged pack.
Family files (``DE.tax.json``, ``FR.payroll-company.json``, ``IN.gst.json``) are
the inputs the merged pack was assembled from, and versioned files (``DE.v1.json``)
are superseded copies, so both are skipped. Where a family file disagrees with the
merged pack the merged pack is the corrected one (France, CVAE relief, 19 Oct 2026).

Folder: the country's ``dir`` in scripts/data/jurisdictions.json with the leading
``skills/`` removed, so skills/ireland -> library/ireland and the federal-only US
pack skills/us/federal -> library/us/federal.

``used_by`` is best effort: the skills in that folder (not its subfolders) with a
rates-table row (``skill_checks._rates_rows``: the rates table, or failing that
every amount table) that contains the figure's exact value string, with number
boundaries so ``EUR 1,000`` does not match ``EUR 1,000,000`` and ``5%`` does not
match ``5.5%``. A common value such as ``20%`` will list skills that use 20% for
another rule; a skill that writes the same number another way (``4.20%`` for
``4.2%``) is not listed.

``sources.json`` lists every distinct http(s) URL cited by the skills in the folder
(text before the platform CTA block) plus every pack URL, with the skills and the
figures citing each.

``read_on`` is the pack's ``checked_at`` unless the entry carries its own
``read_on`` (an entry read again later than the rest of the pack).

An announced figure (a change a government has announced or put in a bill that is
not yet law) carries ``status``, one of ``STATUSES``, and its id is the id of the
figure in force plus ``.announced`` (``ie.cat.group-a.announced`` next to
``ie.cat.group-a``). The figure in force stays in the library unchanged; check
``figure_in_library`` accepts either value. Any other status, or a status on an id
without the suffix, is reported and the entry skipped.
"""

import argparse
import collections
import importlib.util
import json
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


sys.path.insert(0, SCRIPTS_DIR)
skill_checks = _load("skill_checks", "skill_checks.py")
_build_index = _load("build_index", "build-index.py")

#: The merged country pack: two capital letters and .json, nothing between.
PACK_FILE_RE = re.compile(r"^([A-Z]{2})\.json$")
#: The only pack entry fields that are published.
REQUIRED = ("pack_id", "item", "value", "source_url", "quote", "year")
#: The statuses an announced figure may carry; a figure in force has none.
STATUSES = ("announced, Finance Bill not yet enacted",)
#: The id of an announced figure is the id of the figure in force plus this.
ANNOUNCED_SUFFIX = ".announced"
TRAILING_PUNCT = ".,;:'\"`*_"


def clean_url(url):
    """A URL as cited, without the sentence punctuation the regex picks up."""
    url = url.strip()
    while url and url[-1] in TRAILING_PUNCT:
        url = url[:-1]
    return url


def country_folders():
    """``{code: folder under skills/}`` from scripts/data/jurisdictions.json."""
    with open(os.path.join(SCRIPTS_DIR, "data", "jurisdictions.json"), encoding="utf-8") as fh:
        rows = json.load(fh)
    return {r["code"]: r["dir"][len("skills/"):] for r in rows if str(r.get("dir", "")).startswith("skills/")}


def pack_dir(path):
    """Accept the research library root or its pack/ folder."""
    inner = os.path.join(path, "pack")
    return inner if os.path.isdir(inner) else path


def read_packs(path, only=None):
    """``[(code, filename, pack dict)]`` for every merged country pack, sorted by code."""
    out = []
    folder = pack_dir(path)
    for name in sorted(os.listdir(folder)):
        m = PACK_FILE_RE.match(name)
        if not m or (only and m.group(1) not in only):
            continue
        with open(os.path.join(folder, name), encoding="utf-8") as fh:
            out.append((m.group(1), name, json.load(fh)))
    return out


def skipped_pack_files(path):
    return sorted(n for n in os.listdir(pack_dir(path)) if n.endswith(".json") and not PACK_FILE_RE.match(n))


def skill_files(folder):
    """``[(slug, text)]`` for each skill directly in skills/<folder>: .md with frontmatter, not README."""
    base = os.path.join(REPO_ROOT, "skills", folder)
    out = []
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base)):
        full = os.path.join(base, name)
        if not name.endswith(".md") or name == "README.md" or not os.path.isfile(full):
            continue
        with open(full, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        if _build_index.extract_frontmatter(text) is None:
            continue
        out.append((name[:-3], text))
    return out


def rates_row_texts(text):
    """Each rates-table row of a skill as one string."""
    _where, rows = skill_checks._rates_rows(text)
    return [" | ".join(cells) for _header, cells in rows]


def cited_urls(text):
    """Distinct http(s) URLs in the writer's text (the platform CTA block is not theirs)."""
    cut = text.find(skill_checks.CTA_MARKER)
    own = text if cut == -1 else text[:cut]
    urls = []
    for raw in skill_checks.URL_RE.findall(own):
        url = clean_url(raw)
        if re.match(r"https?://[^/\s]+\.[^/\s]+", url) and url not in urls:
            urls.append(url)
    return urls


def build_country(code, pack, folder):
    """``(figures doc, sources doc, problems)`` for one country."""
    problems = []
    skills = skill_files(folder)
    rows = {slug: rates_row_texts(text) for slug, text in skills}
    figures = []
    seen = set()
    for entry in pack.get("entries", []):
        missing = [k for k in REQUIRED if entry.get(k) in (None, "")]
        if missing:
            problems.append(f"{entry.get('pack_id', '?')}: missing {', '.join(missing)}, skipped")
            continue
        if entry["pack_id"] in seen:
            problems.append(f"{entry['pack_id']}: duplicate id, second one skipped")
            continue
        status = entry.get("status")
        if status is not None and (status not in STATUSES or not entry["pack_id"].endswith(ANNOUNCED_SUFFIX)):
            problems.append(f"{entry['pack_id']}: status {status!r} needs one of {STATUSES} "
                            f"and an id ending {ANNOUNCED_SUFFIX}, skipped")
            continue
        seen.add(entry["pack_id"])
        value = str(entry["value"]).strip()
        used_by = [slug for slug, texts in rows.items() if any(skill_checks.value_in_text(value, t) for t in texts)]
        figure = {
            "id": entry["pack_id"],
            "item": entry["item"],
            "value": value,
            "tax_year": entry["year"],
            "source_url": entry["source_url"].strip(),
            "quote": entry["quote"],
            "read_on": entry.get("read_on") or pack.get("checked_at"),
        }
        if status is not None:
            figure["status"] = status
        figure["used_by"] = used_by
        figures.append(figure)
    figures_doc = {"country": folder, "code": code, "figure_count": len(figures), "figures": figures}

    by_url = collections.OrderedDict()
    for slug, text in skills:
        for url in cited_urls(text):
            by_url.setdefault(url, {"skills": [], "figures": []})["skills"].append(slug)
    for fig in figures:
        by_url.setdefault(fig["source_url"], {"skills": [], "figures": []})["figures"].append(fig["id"])
    sources = [{"url": url, **refs} for url, refs in sorted(by_url.items())]
    sources_doc = {"country": folder, "code": code, "url_count": len(sources), "sources": sources}
    return figures_doc, sources_doc, problems


def write_json(path, doc):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("packs", help="path to the research library (or its pack/ folder)")
    parser.add_argument("--write", action="store_true", help="write library/ (default: dry run, counts only)")
    parser.add_argument("--only", nargs="*", help="country codes to build, e.g. IE DE")
    args = parser.parse_args(argv)

    folders = country_folders()
    only = {c.upper() for c in args.only} if args.only else None
    packs = read_packs(args.packs, only)
    if not packs:
        print("no pack/<CC>.json found", file=sys.stderr)
        return 1
    print(f"{'code':<5} {'folder':<18} {'figures':>7} {'used':>5} {'skills':>6} {'urls':>5}  read_on")
    totals = collections.Counter()
    for code, name, pack in packs:
        folder = folders.get(code)
        if not folder:
            print(f"{code:<5} no folder in scripts/data/jurisdictions.json, skipped")
            continue
        figures_doc, sources_doc, problems = build_country(code, pack, folder)
        used = sum(1 for f in figures_doc["figures"] if f["used_by"])
        skills_using = {s for f in figures_doc["figures"] for s in f["used_by"]}
        print(f"{code:<5} {folder:<18} {figures_doc['figure_count']:>7} {used:>5} {len(skills_using):>6} "
              f"{sources_doc['url_count']:>5}  {pack.get('checked_at')}")
        for p in problems:
            print(f"      {p}")
        totals.update(figures=figures_doc["figure_count"], used=used, skills=len(skills_using), countries=1)
        if args.write:
            out = os.path.join(REPO_ROOT, "library", *folder.split("/"))
            write_json(os.path.join(out, "figures.json"), figures_doc)
            write_json(os.path.join(out, "sources.json"), sources_doc)
    print(f"{totals['countries']} countries, {totals['figures']} figures, {totals['used']} with a skill row "
          f"stating the exact value, {totals['skills']} skills using at least one")
    skipped = skipped_pack_files(args.packs)
    if skipped and not only:
        print("skipped (family or superseded files): " + ", ".join(skipped))
    if not args.write:
        print("dry run: nothing written (pass --write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
