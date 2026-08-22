#!/usr/bin/env python3
"""
Build index.json — a machine-readable inventory of every Guide in the repo.

Walks skills/**/*.md and packages/us-federal/*.md (the hand-authored federal
set), skips READMEs and files without frontmatter, and writes index.json at
the repo root:

{
  "generated_at": "<UTC ISO>",
  "counts": { "guides": N, "jurisdictions": N, "accountant_reviewed": N },
  "guides": [ { "slug", "path", "name", "jurisdiction", "category", "tier",
                "verified_by", "reviewed_by", "tax_year", "last_updated" }, ... ]
}

Dependency-free (stdlib only). Frontmatter is parsed with a simple ---block
line scanner; malformed YAML is tolerated by regex-extracting the known keys.

Usage:
    python3 scripts/build-index.py            # write index.json at repo root
    python3 scripts/build-index.py --out PATH # write elsewhere (used by CI)
"""

import json
import os
import re
import sys
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories walked for guide files.
GUIDE_TREES = [
    "skills",
    os.path.join("packages", "us-federal"),
]

# Frontmatter keys lifted into the index (in output order).
KNOWN_KEYS = [
    "name",
    "jurisdiction",
    "category",
    "tier",
    "verified_by",
    "reviewed_by",
    "tax_year",
    "last_updated",
]

# `key: value` at column 0. Tolerates malformed YAML elsewhere in the block.
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*)$")

# Jurisdiction values that look like codes get uppercased (MT, US, US-CA, CA-ON).
CODE_RE = re.compile(r"^[A-Za-z]{2,3}(-[A-Za-z0-9]{1,4})*$")


def extract_frontmatter(text):
    """Return the raw frontmatter block (str) or None if the file has none."""
    if not text.startswith("---"):
        return None
    first_nl = text.find("\n")
    if first_nl == -1 or text[:first_nl].strip() != "---":
        return None
    end = re.search(r"^(---|\.\.\.)\s*$", text[first_nl + 1:], re.MULTILINE)
    if not end:
        return None
    return text[first_nl + 1: first_nl + 1 + end.start()]


def clean_value(raw):
    """Normalize a scalar frontmatter value; None for empty/block scalars."""
    value = raw.strip()
    if value in ("", ">", "|", ">-", "|-", ">+", "|+"):
        return None
    # Strip a trailing YAML comment only when the value is unquoted.
    if value[0] in "\"'":
        quote = value[0]
        if len(value) >= 2 and value.rstrip().endswith(quote):
            value = value.strip()[1:-1].strip()
    else:
        value = re.sub(r"\s+#.*$", "", value).strip()
    if value == "" or value.lower() in ("null", "~"):
        return None
    return value


def parse_known_keys(block):
    """Regex-extract KNOWN_KEYS from a frontmatter block, malformed or not."""
    fields = {key: None for key in KNOWN_KEYS}
    for line in block.splitlines():
        match = KEY_RE.match(line)
        if not match:
            continue
        key = match.group(1)
        if key not in fields or fields[key] is not None:
            continue
        fields[key] = clean_value(match.group(2))
    return fields


def guide_files():
    """Yield repo-relative paths of candidate guide files, sorted."""
    paths = []
    for tree in GUIDE_TREES:
        base = os.path.join(REPO_ROOT, tree)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames.sort()
            for filename in sorted(filenames):
                if not filename.endswith(".md"):
                    continue
                if filename.lower().startswith("readme"):
                    continue
                full = os.path.join(dirpath, filename)
                paths.append(os.path.relpath(full, REPO_ROOT).replace(os.sep, "/"))
    return sorted(set(paths))


def build_index():
    guides = []
    for rel_path in guide_files():
        with open(os.path.join(REPO_ROOT, rel_path), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        block = extract_frontmatter(text)
        if block is None:
            continue  # not a guide (no frontmatter)
        fields = parse_known_keys(block)

        jurisdiction = fields["jurisdiction"]
        if jurisdiction and CODE_RE.match(jurisdiction):
            jurisdiction = jurisdiction.upper()

        tier = fields["tier"]
        if isinstance(tier, str) and tier.isdigit():
            tier = int(tier)

        guides.append({
            "slug": os.path.splitext(os.path.basename(rel_path))[0],
            "path": rel_path,
            "name": fields["name"],
            "jurisdiction": jurisdiction,
            "category": fields["category"],
            "tier": tier,
            "verified_by": fields["verified_by"],
            "reviewed_by": fields["reviewed_by"],
            "tax_year": fields["tax_year"],
            "last_updated": fields["last_updated"],
        })

    guides.sort(key=lambda g: g["path"])

    jurisdictions = {g["jurisdiction"] for g in guides if g["jurisdiction"]}
    unreviewed_markers = {"pending", "none", "no", "false", "-", "n/a", "tbd"}

    def is_reviewed(guide):
        # Same rule as the MCP server's `_quality_tier`: only an explicit
        # `tier: 1` plus a named reviewer counts. A reviewer name alone never
        # implies sign-off, or this inventory reports guides as
        # accountant-reviewed that the MCP server serves as research-verified.
        if str(guide["tier"] or "").strip() != "1":
            return False
        for key in ("reviewed_by", "verified_by"):
            value = guide[key]
            if value and str(value).strip().lower() not in unreviewed_markers:
                return True
        return False

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "counts": {
            "guides": len(guides),
            "jurisdictions": len(jurisdictions),
            "accountant_reviewed": sum(1 for g in guides if is_reviewed(g)),
        },
        "guides": guides,
    }


def main():
    out_path = os.path.join(REPO_ROOT, "index.json")
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]
    index = build_index()
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(index, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    counts = index["counts"]
    print(f"index written to {out_path}")
    print(f"  guides: {counts['guides']}")
    print(f"  jurisdictions: {counts['jurisdictions']}")
    print(f"  accountant_reviewed: {counts['accountant_reviewed']}")


if __name__ == "__main__":
    main()
