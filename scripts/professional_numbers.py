"""Recognise private professional identifiers, not tax figures or software licences.

Admission compares occurrences with the base file: existing approved prose must
not be rewritten just to remove an identifier. The app hides those at display.
"""
from collections import Counter
import re

ID = r"(?:[A-Z]{1,8}[-./ ]*)?\d{2,}[A-Z0-9./-]*\b"
LABELLED = re.compile(r"\b(?:licen[cs]e|warrant)\s*(?:(?:number|no\.?)\s*[:#]?|[:#])\s*\**(" + ID + r")", re.I)
CREDENTIAL = re.compile(r"\b(?:CPA|EA|ACCA|ACPA|ICAEW|ICAI|CRC(?:-[A-Z]{2})?)\s*(?:\([A-Z]+\)\s*)?(?:licen[cs]e\s*)?(?:number|no\.?|[:#])\s*[:#]?\s*(" + ID + r")", re.I)
CREDIT = re.compile(r"^[ \t>*|]*(?:(?:contributed|approved|reviewed|verified|authored|written|maintained|validated)\s+by\b|(?:reviewed_by|verified_by|author)\s*:)", re.I)
CREDIT_ID = re.compile(r"\b(?:CRC-[A-Z]{2}\s+\d{3,}[A-Z0-9/.-]*|[A-Z]{1,5}[- ]\d{3,}[A-Z0-9/.-]*|\d{2,}(?:[./-][A-Z0-9]+)+|\d{3,})\b")


def professional_numbers(text):
    """Return a counter so duplicating an old number still counts as a new leak."""
    found = Counter()
    for line in text.splitlines():
        spans = []
        for pattern in (LABELLED, CREDENTIAL):
            for match in pattern.finditer(line):
                start, end = match.span(1)
                if not any(start < b and end > a for a, b in spans):
                    spans.append((start, end))
        if CREDIT.match(line):
            for match in CREDIT_ID.finditer(line):
                token = match.group()
                if re.fullmatch(r"\d{4}-\d{2}-\d{2}|(?:19|20)\d{2}", token):
                    continue
                if re.search(r"(?:https?://\S*|(?:Form|section|Act|tax year|on|em|el)\s+)$", line[:match.start()], re.I):
                    continue
                if not any(match.start() < b and match.end() > a for a, b in spans):
                    spans.append(match.span())
        for start, end in spans:
            found[line[start:end].upper()] += 1
    return found


def new_professional_numbers(text, old_text):
    return professional_numbers(text) - professional_numbers(old_text)
