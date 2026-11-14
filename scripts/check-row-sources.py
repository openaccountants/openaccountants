#!/usr/bin/env python3
"""Row-by-row figure check: is every figure in a linked table row on the page that row links to?

For each table row above `## Worked cases` that carries a link (or says `same`, meaning
the link of the row above), every dollar-style amount and every percentage in the row
must appear on one of the pages linked in that row. Pages are fetched with curl;
PDFs go through pdftotext, Excel files are read from their XML. A page that cannot be
read (blocked, empty, image only) is reported as UNREADABLE, never as a miss.

Worked-case arithmetic is not checked here: check-examples.py recomputes it.
A figure the page does not print but that follows from it (half of a joint threshold,
the difference of two rates) is marked in the row with the word `derived` or `computed`
(for example "USD 125,000 (derived: half of the USD 250,000 joint threshold)"); figures in
such a row are reported as derived, not as misses, and zero amounts are ignored.

Usage:
  python3 scripts/check-row-sources.py FILE...          # report, exit 1 if any miss
  python3 scripts/check-row-sources.py --changed-only   # skills/**.md changed vs origin/$BASE_REF
Writes a markdown report to $GITHUB_STEP_SUMMARY when set.
"""
import html
import io
import json
import os
import re
import subprocess
import sys
import zipfile

LINK_RE = re.compile(r"https?://[^\s)|>\"\]]+")
# Identifiers that look like numbers but are not figures (statute and form numbers).
IDENT_RE = re.compile(
    r"(?i)\b(section|sec\.|§|art\.|article|rcw|a\.r\.s\.|ilcs|mcl|g\.s\.|r\.c\.|k\.s\.a\.|n\.d\.c\.c\.|nrs|cite=|"
    r"form|line|schedule|pub\.?|publication|notice|rev\. ?proc\.?|rev\. ?rul\.?|act|chapter|ch\.|p\.l\.|"
    r"public law|regulation|reg\.|no\.)\s*[\d.\-:()a-z]+"
)
FIG_RE = re.compile(r"\$\s?\d[\d,]*(?:\.\d+)?|\b\d{1,3}(?:,\d{3})+(?:\.\d+)?\b|\b\d+(?:\.\d+)?\s?%")
NUM_RE = re.compile(r"\d[\d.,]*\d|\d")


def table_rows(text):
    """Yield (row_text, urls) for linked table rows before ## Worked cases. `same` inherits."""
    body = re.split(r"(?m)^##\s+Worked cases", text)[0]
    last = []
    for line in body.splitlines():
        s = line.strip()
        if not s.startswith("|") or re.fullmatch(r"\|[\s:|-]+\|?", s):
            if not s.startswith("|"):
                last = []
            continue
        urls = [u.rstrip(".,;") for u in LINK_RE.findall(s) if "openaccountants" not in u]
        if not urls and re.search(r"\|\s*same\s*\|?\s*$", s, re.I):
            urls = list(last)
        if urls:
            last = urls
            yield s, urls


def figures(row):
    """Dollar amounts with a thousands separator or a $ sign, and percentages, minus identifiers."""
    t = re.sub(r"\]\([^)]*\)", "]", row)
    t = LINK_RE.sub("", t)
    t = IDENT_RE.sub("", t)
    return [f.strip() for f in FIG_RE.findall(t)]


def _value(s):
    s = s.replace("$", "").replace(",", "").replace("%", "").strip()
    try:
        return float(s)
    except ValueError:
        return None


# A space, no-break space or thin space between digit groups ("1 234,56").
GROUP_SPACE_RE = re.compile(r"(?<=\d)[ \u00a0\u202f\u2009](?=\d{3}\b)")


def page_values(page_text):
    """Every number on the page, read the English way (1,234.56) and the European way
    (1.234,56, 1 234,56, 2,25 %), so a page that writes figures with a decimal comma is
    not reported as a miss."""
    vals = set()
    found_nums = NUM_RE.findall(page_text) + NUM_RE.findall(GROUP_SPACE_RE.sub("", page_text))
    for m in found_nums:
        v = _value(m)
        if v is not None:
            vals.add(round(v, 6))
        try:
            vals.add(round(float(m.replace(".", "").replace(",", ".")), 6))
        except ValueError:
            pass
    return vals


def found(fig, vals):
    v = _value(fig)
    if v is None:
        return True
    if round(v, 6) in vals:
        return True
    if fig.endswith("%") and round(v / 100, 6) in vals:  # 5.2% written 0.052 (rate sheets)
        return True
    return False


def read_bytes(raw):
    """Bytes of a fetched URL to plain text."""
    if raw[:4] == b"%PDF":
        r = subprocess.run(["pdftotext", "-layout", "-", "-"], input=raw, capture_output=True)
        return r.stdout.decode("utf-8", "replace")
    if raw[:2] == b"PK":
        try:
            z = zipfile.ZipFile(io.BytesIO(raw))
            xml = " ".join(z.read(n).decode("utf-8", "ignore") for n in z.namelist() if n.endswith(".xml"))
            return re.sub(r"<[^>]+>", " ", xml)
        except zipfile.BadZipFile:
            return ""
    t = raw.decode("utf-8", "replace")
    flight = next_flight_text(t)
    # Some sites (vero.fi) keep a table as JSON inside a long attribute value: keep that text too.
    attrs = " ".join(html.unescape(a) for a in re.findall(r'="([^"]{50,})"', t))
    t = re.sub(r"(?s)<script.*?</script>|<style.*?</style>", " ", t)
    return html.unescape(re.sub(r"<[^>]+>", " ", t)) + flight + (" " + attrs if attrs else "")


# Next.js sites (finlex.fi and others) ship the page text inside
# <script>self.__next_f.push([1,"..."])</script> blocks, not in the HTML body.
NEXT_F_RE = re.compile(r'self\.__next_f\.push\(\[\d+,("(?:[^"\\]|\\.)*")\]\)')


def next_flight_text(page):
    """The text carried in Next.js data blocks, or "" when the page has none."""
    parts = []
    for lit in NEXT_F_RE.findall(page):
        try:
            parts.append(json.loads(lit))
        except ValueError:
            continue
    if not parts:
        return ""
    return " " + html.unescape(re.sub(r"<[^>]+>", " ", "".join(parts)))


_cache = {}


def fetch(url):
    """Return page text, or None when the page cannot be read."""
    if url in _cache:
        return _cache[url]
    r = subprocess.run(["curl", "-sL", "-m", "45", "-A", "Mozilla/5.0 (OpenAccountants figure check)",
                        "-w", "\n%{http_code}", url], capture_output=True)
    raw, code = r.stdout[:-4], r.stdout[-3:].decode("ascii", "replace")
    text = read_bytes(raw) if code.startswith("2") else ""
    _cache[url] = text if len(text) >= 400 else None
    return _cache[url]


def check_text(text, fetcher=fetch):
    """Return (rows_checked, misses, unreadable). misses: (figure, urls, row)."""
    misses, unreadable, n = [], [], 0
    for row, urls in table_rows(text):
        figs = figures(row)
        if not figs:
            continue
        n += 1
        pages = [fetcher(u) for u in urls]
        readable = [p for p in pages if p]
        if not readable:
            unreadable.append((urls, row))
            continue
        vals = set().union(*(page_values(p) for p in readable))
        derived = bool(re.search(r"(?i)\b(derived|computed)\b", row))
        for f in figs:
            if _value(f) == 0 or derived:
                continue
            if not found(f, vals):
                misses.append((f, urls, row))
    return n, misses, unreadable


def changed_files():
    base = os.environ.get("BASE_REF", "main")
    out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AM", f"origin/{base}...HEAD", "--", "skills/"],
                         capture_output=True, text=True).stdout.split()
    return [f for f in out if f.endswith(".md") and not f.endswith("README.md")]


def main(argv):
    files = changed_files() if "--changed-only" in argv else [a for a in argv if not a.startswith("--")]
    lines, total_miss = ["## Row-by-row figure check", ""], 0
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read()
        if re.search(r"(?m)^reviewed_by:", text.split("\n---", 1)[0]):
            continue
        n, misses, unreadable = check_text(text)
        total_miss += len(misses)
        lines.append(f"**{f}**: {n} rows checked, {len(misses)} figure(s) not found on the linked page, "
                     f"{len(unreadable)} row(s) whose page could not be read")
        for fig, urls, row in misses:
            lines.append(f"- MISS `{fig}` not on {' '.join(urls)} | row: {row[:160]}")
        for urls, row in unreadable:
            lines.append(f"- UNREADABLE {' '.join(urls)} | row: {row[:120]}")
        lines.append("")
    if not files:
        lines.append("No changed skill files.")
    lines.append(f"Total misses: {total_miss}. A miss is a figure that is not on the page its row links to: "
                 "fix the figure or the link, or write the figure the way the page writes it.")
    report = "\n".join(lines)
    print(report)
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as fh:
            fh.write(report + "\n")
    return 1 if total_miss else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
