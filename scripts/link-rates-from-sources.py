#!/usr/bin/env python3
"""Fill unlinked rates rows of a country pack from its SOURCES.md.

Dry run by default; --apply writes. A row is linked only when its first cell
equals a stored label, its figure equals the stored figure, and the stored quote
holds that figure. Anything else is listed. Only the Source cell changes; a
figure is never edited.

    python3 scripts/link-rates-from-sources.py skills/germany [--apply] [--skip FILE ...]
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import skill_checks  # noqa: E402

NUMBER_RE = re.compile(r"\d+(?:[ ., ]\d+)*")
SOURCE_HEADER_RE = re.compile(r"^source", re.IGNORECASE)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split(" | ")]


def numbers(text):
    return {re.sub(r"[ ., ]", "", n).rstrip("0") or "0" for n in NUMBER_RE.findall(text)}


def parse_sources(text):
    """{label: [{url, figure, quote, year}]} from the sources table."""
    out = {}
    for line in text.splitlines():
        if not line.startswith("| http"):
            continue
        cells = split_row(line)
        if len(cells) != 7:
            raise ValueError(f"SOURCES.md row needs 7 cells: {line[:80]}")
        for entry in cells[6].split("<br>"):
            parts = entry.split(" :: ")
            if len(parts) != 3:
                raise ValueError(f"bad quote entry: {entry[:80]}")
            out.setdefault(parts[0].strip().lower(), []).append(
                {"url": cells[0], "year": cells[3], "figure": parts[1].strip(), "quote": parts[2].strip().strip('"')}
            )
    return out


def quote_holds(entry):
    if entry["figure"] in entry["quote"]:
        return True
    want = numbers(entry["figure"])
    return bool(want) and want <= numbers(entry["quote"])


def figure_matches(value, entry):
    plain = value.strip("` ")
    if entry["figure"] in plain:
        return True
    want = numbers(entry["figure"])
    return bool(want) and numbers(plain) == want


def match(cells, sources):
    """(url, None) or (None, reason)."""
    entries = sources.get(cells[0].lower())
    if not entries:
        return None, "no stored label"
    value = " | ".join(cells[1:-1])
    for entry in entries:
        if figure_matches(value, entry):
            if not quote_holds(entry):
                return None, f"stored quote does not hold {entry['figure']}"
            return entry["url"], None
    return None, f"figure differs from stored {entries[0]['figure']}"


def missing_rows(text):
    _, rows = skill_checks._rates_rows(text)
    previous = None
    for header, cells in rows:
        status = skill_checks._row_status(header, cells, previous)
        previous = (header, status)
        if status == "missing":
            yield header, cells


def link_text(text, sources):
    """(new_text, linked rows, mismatches)."""
    linked, mismatches = [], []
    for header, cells in missing_rows(text):
        if not SOURCE_HEADER_RE.match(header[-1]):
            mismatches.append((cells[0], "no Source column"))
            continue
        url, reason = match(cells, sources)
        if url is None:
            mismatches.append((cells[0], reason))
            continue
        pattern = re.compile(r"^(\|\s*" + re.escape(cells[0]) + r"\s*\|.*\|)[ \t]*" + re.escape(cells[-1]) + r"[ \t]*\|[ \t]*$", re.M)
        cell = f"{cells[-1]}, {url}" if cells[-1] else url
        text, count = pattern.subn(lambda m: f"{m.group(1)} {cell} |", text, count=1)
        (linked.append(cells[0]) if count else mismatches.append((cells[0], "row not found to edit")))
    return text, linked, mismatches


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pack")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--skip", nargs="*", default=[])
    args = ap.parse_args(argv)
    with open(os.path.join(args.pack, "SOURCES.md"), encoding="utf-8") as fh:
        sources = parse_sources(fh.read())
    totals = [0, 0]
    for name in sorted(os.listdir(args.pack)):
        if not name.endswith(".md") or skill_checks.is_not_skill(name) or name in args.skip:
            continue
        path = os.path.join(args.pack, name)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        new, linked, mismatches = link_text(text, sources)
        for row in linked:
            print(f"LINK {name}: {row}")
        for row, why in mismatches:
            print(f"MISMATCH {name}: {row}: {why}")
        totals[0] += len(linked)
        totals[1] += len(mismatches)
        if args.apply and new != text:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)
    print(f"{'linked' if args.apply else 'would link'} {totals[0]}, mismatches {totals[1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
