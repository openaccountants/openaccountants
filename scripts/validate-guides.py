#!/usr/bin/env python3
"""
Validate guide files, the hand-authored us-federal set, and index.json.

Checks (ERROR = exit 1, WARN = printed summary only):
  1. Every guide file's frontmatter block is valid, unambiguous YAML (a file
     that opens `---` must close it). Files without any frontmatter are treated
     as docs, not guides, and skipped (same rule scripts/build-index.py uses).
  2. `name` and `description` are present — ERROR if missing, except for the
     frozen LEGACY_MISSING_DESCRIPTION baseline below (grandfathered; the
     list must only ever shrink).
  3. `tier` and `last_updated` are required — ERROR if missing (the one-time
     sweep was scripts/backfill-metadata.py). `tier` must be 1 or 2;
     `last_updated` must be YYYY-MM-DD — ERROR otherwise.
  3a. `jurisdiction` is required — ERROR if missing, except inside the
     JURISDICTION_OPTIONAL_DIRS below (dirs whose deliberate convention is
     "no jurisdiction key": jurisdiction-agnostic templates/engines and the
     EU-wide shared base). There it stays a WARN summary count.
  3b. `tax_year`, when present, must be a bare integer 2015-2035 — ERROR
     otherwise (no grandfathering; scripts/normalize-tax-year.py did the
     one-time sweep, and calendar/range/qualifier text belongs in
     `tax_year_notes`).
  4. ERROR if any file under packages/us-federal/ was deleted relative to
     git history (hand-authored, no builder — a deletion is unrecoverable).
     Skipped when git / origin/main is unavailable.
  5. ERROR if index.json is stale: regenerated index (ignoring generated_at)
     must match the committed one. Fix with: python3 scripts/build-index.py
  6. ERROR if a deprecated inventory file reappears (skills/manifest.json,
     packages/manifest.json). index.json is the single canonical inventory;
     the old manifests had no consumers and were removed so they can't drift.
  7. The mechanical lines of docs/skill-template.md (scripts/skill_checks.py):
     current tax_year, read dates in `## Sources`, two oa-check blocks, a
     numeric version, honest tier/reviewer keys, no em dash. ERROR on a PR
     (--changed-only) for a tax skill; WARN on the full tree and for
     accounting-pack and router files. Rates-row URLs, the nine canonical
     headings and the "Not yet confirmed" line WARN in both modes until the
     backlog is cleared. The full run prints a count of failures per check.
  8. PR mode only: one job in one country has one skill (docs/skill-template.md).
     ERROR if a NEW skill file lands in a (country, domain) cell that already
     holds a slug, unless the PR deletes that slug or the pack README's
     covered_by names the new slug for that domain. WARN when a new skill has
     no domain that can be classified.

Install scripts/requirements-validation.txt, then run:
python3 scripts/validate-guides.py
"""

import importlib.util
import json
import os
import re
import subprocess
import sys

import skill_checks
from frontmatter_yaml import FrontmatterError, load_frontmatter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_INDEX = os.path.join(REPO_ROOT, "scripts", "build-index.py")
COVERAGE_REPORT = os.path.join(REPO_ROOT, "scripts", "coverage-report.py")

#: scripts/skill_checks.py checks that fail a PR (changed-only mode) when a tax
#: skill breaks them. On the full tree they are warnings, so the backlog shows
#: without blocking the nightly run. Accounting-pack and router files only warn.
PR_ERROR_CHECKS = {
    "tax_year_current",    # (a)
    "sources_read_dates",  # (b)
    "two_oa_checks",       # (e)
    "version_numeric",     # (f)
    "tier_honest",         # (g)
    "no_em_dash",          # (h)
}
#: Warnings in both modes for now: rates_rows_sourced (c), canonical_headings (d),
#: not_yet_confirmed (i) and reviewed_on (j). They become errors once the backlog is cleared
#: (pass rates are in skills/REGISTER.md).

# Legacy guides that predate the description requirement. Grandfathered so CI
# can be strict for everything new. Never add to this list — remove entries as
# the files gain descriptions.
LEGACY_MISSING_DESCRIPTION = {
    "skills/cross-border/treaty-corridors/americas-corridors.md",
    "skills/cross-border/treaty-corridors/asia-pacific-corridors.md",
    "skills/cross-border/treaty-corridors/emerging-market-corridors.md",
    "skills/cross-border/treaty-corridors/eu-intra-rates.md",
    "skills/cross-border/treaty-corridors/uk-major-partners.md",
    "skills/cross-border/treaty-corridors/us-major-partners.md",
}

# Dirs whose deliberate convention is "no jurisdiction key" — the content is
# jurisdiction-agnostic (templates, intelligence engines, treaty corridor
# reference tables) or spans the whole EU (the shared eu-vat-base). Missing
# `jurisdiction` here is a WARN, not an ERROR. Everywhere else it is required
# (scripts/backfill-metadata.py did the one-time sweep).
JURISDICTION_OPTIONAL_DIRS = {
    "skills/cross-border/treaty-corridors",
    "skills/intelligence",
    "skills/templates",
    "skills/international/eu",
}


def load_build_index():
    spec = importlib.util.spec_from_file_location("build_index", BUILD_INDEX)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# `tax_year` must be a bare integer year, e.g. `tax_year: 2025`. Ranges,
# calendars, and qualifiers go in `tax_year_notes` (see
# scripts/normalize-tax-year.py, issue #49).
TAX_YEAR_RE = re.compile(r"^tax_year:[ \t]*(.*?)[ \t]*$", re.MULTILINE)
TAX_YEAR_MIN, TAX_YEAR_MAX = 2015, 2035


LAST_UPDATED_FMT = re.compile(r"\d{4}-\d{2}-\d{2}")
NON_REVIEWER_MARKERS = {"pending", "pending_review", "none", "no", "false", "-", "n/a", "tbd"}


def real_reviewer(value):
    """Whether a frontmatter reviewer field makes a real named claim."""
    return bool(value and str(value).strip().lower() not in NON_REVIEWER_MARKERS)


def check_quality_metadata(rel, fields, errors):
    """Enforce the fail-closed quality-tier contract for canonical sources."""
    tier = fields["tier"]
    reviewed_by = real_reviewer(fields["reviewed_by"])
    verified_by = real_reviewer(fields["verified_by"])
    if not tier:
        errors.append(f"{rel}: missing required frontmatter key `tier`")
    elif tier not in ("1", "2"):
        errors.append(f"{rel}: `tier` must be 1 or 2 (got {tier!r})")
    elif tier == "1" and not (reviewed_by or verified_by):
        errors.append(f"{rel}: tier 1 requires a real `reviewed_by` or `verified_by` value")
    elif tier == "2" and verified_by:
        errors.append(f"{rel}: tier 2 must not claim accountant verification in `verified_by`")


#: Slug tokens that mark a tax skill (the GOAL.md tax domains). These skills
#: must show where their figures come from.
TAX_SLUG_TOKENS = (
    "income-tax", "corporate", "vat", "gst", "sales-tax", "payroll", "social", "ssc",
    "withholding", "transfer-pricing", "exit", "departure", "treaty",
)
SOURCES_HEADING_RE = re.compile(r"^##+\s+Sources\b", re.MULTILINE | re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s)>\]]+")
STALE_DAYS = 365


def is_tax_skill(rel):
    slug = os.path.splitext(os.path.basename(rel))[0].lower()
    return rel.startswith("skills/") and any(token in slug for token in TAX_SLUG_TOKENS)


def check_sources(rel, text):
    """A tax skill needs a `## Sources` section with at least one URL.

    Returns a problem string or None. Provenance lives in the body, not in a
    frontmatter key, because the platform export re-renders frontmatter and
    drops keys it does not store (see docs/skill-template.md).
    """
    if not is_tax_skill(rel):
        return None
    match = SOURCES_HEADING_RE.search(text)
    if not match:
        return "no `## Sources` section"
    section = text[match.end():]
    next_heading = re.search(r"^##\s", section, re.MULTILINE)
    if next_heading:
        section = section[: next_heading.start()]
    if not URL_RE.search(section):
        return "`## Sources` section has no URL"
    return None


def check_staleness(fields, today):
    """Return a problem string when the figures are probably out of date."""
    from datetime import datetime
    problems = []
    last_updated = fields.get("last_updated")
    if last_updated and LAST_UPDATED_FMT.fullmatch(str(last_updated)):
        try:
            age = (today - datetime.strptime(str(last_updated), "%Y-%m-%d").date()).days
            if age > STALE_DAYS:
                problems.append(f"last_updated {last_updated} is {age} days old")
        except ValueError:
            pass
    tax_year = fields.get("tax_year")
    if tax_year and str(tax_year).isdigit() and int(tax_year) < today.year - 1:
        problems.append(f"tax_year {tax_year} is two or more years behind")
    return "; ".join(problems) or None


def changed_files_vs_main():
    """Files changed vs origin/main (PR mode). Empty list = nothing relevant."""
    import subprocess
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
        return [l.strip() for l in out.splitlines() if l.strip()]
    except Exception as e:  # pragma: no cover
        print(f"WARN: could not compute changed files ({e}); validating everything")
        return None


def added_and_deleted_vs_main():
    """(added paths, deleted paths) vs origin/main. A rename is one of each."""
    try:
        out = subprocess.run(
            ["git", "diff", "--name-status", "--no-renames", "origin/main...HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except Exception as e:  # pragma: no cover
        print(f"WARN: could not compute added files ({e}); skipping the one-skill-per-cell check")
        return set(), set()
    rows = [line.split("\t", 1) for line in out.splitlines() if "\t" in line]
    return {p for s, p in rows if s == "A"}, {p for s, p in rows if s == "D"}


def cell_conflicts(cov, guides, added, deleted, readme_for):
    """(errors, warnings) for the skills in `added`. `guides` is the tree at HEAD;
    `readme_for(guide)` returns the pack's covered_by map."""
    errors, warnings = [], []
    deleted_slugs = {os.path.splitext(os.path.basename(p))[0] for p in deleted}
    cells = {}
    for g in guides:
        if g["path"] in added or g["slug"] in deleted_slugs:
            continue
        code = str(g.get("jurisdiction") or "").upper()
        for d in cov.cell_domains(g, readme_for(g))[0]:
            cells.setdefault((code, d), []).append(g["slug"])
    for g in guides:
        code = str(g.get("jurisdiction") or "").upper()
        if g["path"] not in added or not code or code in cov.PSEUDO_CODES or g["slug"] in deleted_slugs:
            continue
        domains, named = cov.cell_domains(g, readme_for(g))
        if not domains:
            warnings.append(f"{g['path']}: no tax domain in the slug, so its country cell was not checked")
        for d in sorted(domains - named, key=cov.DOMAIN_CODES.index):
            holders = sorted(cells.get((code, d), []))
            if holders:
                errors.append(
                    f"{g['path']}: {code} {d} already holds {', '.join(holders)}. One job has one skill: "
                    f"merge into it, delete it in this PR, or name {g['slug']} under covered_by in the pack README"
                )
    return errors, warnings


def check_new_skill_cells(bi, errors, warnings):
    added, deleted = added_and_deleted_vs_main()
    if not added:
        return
    spec = importlib.util.spec_from_file_location("coverage_report", COVERAGE_REPORT)
    cov = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cov)
    with open(cov.DATA_PATH, encoding="utf-8") as fh:
        pack_dirs = {row["code"]: row.get("dir") or "" for row in json.load(fh)}

    def readme_for(guide):
        code = str(guide.get("jurisdiction") or "").upper()
        return cov.read_pack_readme(pack_dirs.get(code) or os.path.dirname(guide["path"]))[2]

    new_errors, new_warnings = cell_conflicts(cov, bi.build_index()["guides"], added, deleted, readme_for)
    errors.extend(new_errors)
    warnings.extend(new_warnings)


#: Bytes that may precede a frontmatter opener without being part of it:
#: a UTF-8 byte-order mark, spaces, tabs, and line breaks.
LEADING_JUNK = "\ufeff \t\r\n"


def misplaced_frontmatter(bi, text):
    """Whether a file carries a frontmatter block that does not start at byte 0.

    ``extract_frontmatter`` requires ``---`` in the first bytes, so a UTF-8 BOM,
    a leading blank line, or a leading space returns None while
    ``text.startswith("---")`` is also false: the file was counted as a doc and
    silently skipped the strict check. Only flagged when removing the leading
    bytes turns the file into a parseable block, so a doc opening on a `---`
    horizontal rule is not caught by mistake.
    """
    stripped = text.lstrip(LEADING_JUNK)
    if stripped == text or not stripped.startswith("---"):
        return False
    return bi.extract_frontmatter(stripped) is not None


def packages_files():
    """Repo-relative paths of generated package guides, sorted.

    build-index.py's GUIDE_TREES covers skills/ and the hand-authored
    packages/us-federal only, so the rest of the generated tree was validated by
    nothing, while sync-mcp.yml mirrors it to the MCP repo on every push to
    main.
    """
    paths = []
    base = os.path.join(REPO_ROOT, "packages")
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


LEGACY_DEPENDS_ON = re.compile(r"^(depends_on):[ \t]+(- .+)$", re.MULTILINE)


def normalize_legacy_depends_on(block):
    """Fold the legacy single-line `depends_on: - x` into a real YAML list.

    663 generated files (and their skills/ sources) predate the strict sweep and
    carry the flat form, which strict YAML rejects ("sequence entries are not
    allowed here"). The strictness is right for everything NEW; failing the
    whole tree on a format that shipped for months is not. Normalizing exactly
    this one known shape keeps the sweep strict for every other error while a
    format migration cleans the corpus (tracked separately). Never widen this
    to other keys - each legacy exception must earn its own entry.
    """
    return LEGACY_DEPENDS_ON.sub(lambda m: f"{m.group(1)}:\n  {m.group(2)}", block)


def check_packages_frontmatter(bi, errors, only_files=None):
    """Strict-YAML sweep over the whole generated packages/** tree."""
    already_checked = set(bi.guide_files())
    checked = 0
    for rel in packages_files():
        if rel in already_checked:
            continue  # packages/us-federal gets the full guide contract instead
        if only_files is not None and rel not in only_files:
            continue
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        block = bi.extract_frontmatter(text)
        if block is None:
            if text.startswith("---"):
                errors.append(f"{rel}: frontmatter opens with --- but never closes")
            elif misplaced_frontmatter(bi, text):
                errors.append(
                    f"{rel}: frontmatter `---` must be the first bytes of the file"
                )
            continue
        checked += 1
        try:
            load_frontmatter(normalize_legacy_depends_on(block))
        except FrontmatterError as exc:
            errors.append(f"{rel}: invalid YAML frontmatter: {exc}")
    print(f"checked {checked} generated package frontmatter block(s)")


def check_guides(bi, errors, warnings, only_files=None):
    from collections import Counter
    from datetime import date
    warn_counts = Counter({"jurisdiction (jurisdiction-agnostic dirs)": 0})
    check_counts = Counter()  # skill_checks failures that are warnings in this mode
    per_file_warnings = []
    today = date.today()
    guides = skipped = 0
    for rel in bi.guide_files():
        if only_files is not None and rel not in only_files:
            continue
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        block = bi.extract_frontmatter(text)
        if block is None:
            if text.startswith("---"):
                errors.append(f"{rel}: frontmatter opens with --- but never closes")
            elif misplaced_frontmatter(bi, text):
                errors.append(
                    f"{rel}: frontmatter `---` must be the first bytes of the file "
                    "(a byte-order mark, blank line, or leading whitespace before "
                    "it makes the file count as a doc and skip validation entirely)"
                )
            else:
                skipped += 1  # doc file, not a guide
            continue
        guides += 1
        try:
            load_frontmatter(block)
        except FrontmatterError as exc:
            errors.append(f"{rel}: invalid YAML frontmatter: {exc}")
            continue
        fields = bi.parse_known_keys(block)
        if not fields["name"]:
            errors.append(f"{rel}: missing required frontmatter key `name`")
        has_description = re.search(r"^description:", block, re.MULTILINE)
        if not has_description and rel not in LEGACY_MISSING_DESCRIPTION:
            errors.append(f"{rel}: missing required frontmatter key `description`")
        tax_year = TAX_YEAR_RE.search(block)
        if tax_year:
            value = tax_year.group(1)
            if not re.fullmatch(r"\d{4}", value) or not (TAX_YEAR_MIN <= int(value) <= TAX_YEAR_MAX):
                errors.append(
                    f"{rel}: `tax_year` must be a bare integer "
                    f"{TAX_YEAR_MIN}-{TAX_YEAR_MAX} (got {value!r}) — put "
                    "ranges/calendars/qualifiers in `tax_year_notes`"
                )
        check_quality_metadata(rel, fields, errors)
        last_updated = fields["last_updated"]
        if not last_updated:
            errors.append(f"{rel}: missing required frontmatter key `last_updated`")
        elif not LAST_UPDATED_FMT.fullmatch(last_updated):
            errors.append(
                f"{rel}: `last_updated` must be YYYY-MM-DD (got {last_updated!r})"
            )
        if not fields["jurisdiction"]:
            if os.path.dirname(rel) in JURISDICTION_OPTIONAL_DIRS:
                warn_counts["jurisdiction (jurisdiction-agnostic dirs)"] += 1
            else:
                errors.append(f"{rel}: missing required frontmatter key `jurisdiction`")
        # Provenance and freshness (GOAL.md): warnings for now, so the
        # backlog is visible before the rule becomes an error.
        problem = check_sources(rel, text)
        if problem:
            warn_counts["a `## Sources` section with a URL (tax skills)"] += 1
            if only_files is not None:
                per_file_warnings.append(f"{rel}: {problem}")
        problem = check_staleness(fields, today)
        if problem:
            warn_counts["fresh figures (last_updated within a year, tax_year current)"] += 1
            if only_files is not None:
                per_file_warnings.append(f"{rel}: {problem}")
        # The standard's mechanical lines (scripts/skill_checks.py). A PR that
        # touches a tax skill must pass PR_ERROR_CHECKS; everything else warns.
        frontmatter = skill_checks.read_frontmatter(text)
        scope = skill_checks.scope_of(rel, frontmatter)
        results = skill_checks.run_checks(rel, text, frontmatter)
        for letter, name, _func in skill_checks.CHECKS:
            problems = results[name]
            if not problems:
                continue
            message = f"{rel}: ({letter}) {name}: {'; '.join(problems)}"
            if only_files is not None and scope == "tax" and name in PR_ERROR_CHECKS:
                errors.append(message)
            else:
                check_counts[f"({letter}) {name}"] += 1
                if only_files is not None:
                    per_file_warnings.append(message)
    for key, count in sorted(warn_counts.items()):
        if count:
            warnings.append(f"{count} guides missing `{key}`")
    for key, count in sorted(check_counts.items()):
        warnings.append(f"{count} guides fail check {key}")
    warnings.extend(per_file_warnings)
    print(f"checked {guides} guides ({skipped} non-guide .md files skipped)")


def check_us_federal_deletions(errors):
    """The hand-authored us-federal package has no builder; a deleted file is gone."""
    for label, args in (
        ("origin/main...HEAD", ["git", "diff", "--name-status", "origin/main...HEAD", "--", "packages/us-federal"]),
        ("working tree vs HEAD", ["git", "diff", "--name-status", "HEAD", "--", "packages/us-federal"]),
    ):
        try:
            out = subprocess.run(args, cwd=REPO_ROOT, capture_output=True, text=True, timeout=60)
        except (OSError, subprocess.TimeoutExpired):
            print(f"skipping us-federal deletion check ({label}): git unavailable")
            continue
        if out.returncode != 0:
            print(f"skipping us-federal deletion check ({label}): {out.stderr.strip().splitlines()[:1]}")
            continue
        for line in out.stdout.splitlines():
            status, _, path = line.partition("\t")
            if status.startswith("D"):
                errors.append(f"hand-authored file deleted ({label}): {path}")


def check_index_fresh(errors):
    index_path = os.path.join(REPO_ROOT, "index.json")
    if not os.path.isfile(index_path):
        errors.append("index.json missing — run: python3 scripts/build-index.py")
        return
    try:
        spec = importlib.util.spec_from_file_location("build_index_module", BUILD_INDEX)
        if spec is None or spec.loader is None:
            raise ImportError("Could not load spec for build-index.py")
        bi_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bi_module)
        fresh = bi_module.build_index()
    except Exception as exc:
        errors.append(f"build-index.py failed while checking freshness: {exc}")
        return

    with open(index_path, encoding="utf-8") as fh:
        committed = json.load(fh)
    for section in ("counts", "guides"):
        if committed.get(section) != fresh.get(section):
            errors.append(
                f"index.json is stale (`{section}` differs) — regenerate with: "
                "python3 scripts/build-index.py"
            )
            return


# Deprecated inventories, removed 2026-07 (they had drifted and nothing read
# them — the MCP server indexes packages/**/*.md frontmatter directly, and the
# website sync works from files + frontmatter). index.json is canonical.
DEPRECATED_INVENTORY_FILES = (
    "skills/manifest.json",
    "packages/manifest.json",
)


def check_no_deprecated_manifests(errors):
    for rel in DEPRECATED_INVENTORY_FILES:
        if os.path.isfile(os.path.join(REPO_ROOT, rel)):
            errors.append(
                f"{rel} is deprecated and must not be committed — index.json is "
                "the canonical inventory (python3 scripts/build-index.py). "
                "Delete the file; see docs/REPO-LAYOUT.md."
            )


def check_llms_full_fresh(errors):
    """llms-full.txt embeds llms.txt, the index inventory, GOAL.md, and
    QUALITY-TIERS — it drifts silently when any of those change. Regenerate to
    a temp file and compare, mirroring the index.json staleness check."""
    import subprocess
    import tempfile

    committed = os.path.join(REPO_ROOT, "llms-full.txt")
    if not os.path.isfile(committed):
        errors.append("llms-full.txt is missing — run: python3 scripts/build-llms-full.py")
        return
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as tf:
        tmp = tf.name
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(REPO_ROOT, "scripts", "build-llms-full.py"),
             "--out", tmp],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            errors.append(f"build-llms-full.py failed during freshness check: {result.stderr.strip()}")
            return
        with open(committed, encoding="utf-8") as fh:
            a = fh.read()
        with open(tmp, encoding="utf-8") as fh:
            b = fh.read()
        if a != b:
            errors.append(
                "llms-full.txt is stale (its embedded docs or the guide inventory "
                "changed) — regenerate: python3 scripts/build-llms-full.py"
            )
    finally:
        os.unlink(tmp)


def main():
    # PR mode (--changed-only --no-index-check): validate only the files the PR
    # touches, and skip the derived-tree freshness checks. Rationale: index.json
    # and llms-full.txt are GENERATED by the platform's daily sync — the sync is
    # their only legitimate writer, so their staleness is the sync's bug, never a
    # contributor's. The old byte-match here made every two concurrent guide PRs
    # conflict on a 586KB generated file, and failed every doc-following external
    # PR. Full mode (no flags) is unchanged for the nightly/sync context.
    changed_only = "--changed-only" in sys.argv
    no_index_check = "--no-index-check" in sys.argv

    errors, warnings = [], []
    bi = load_build_index()
    only = None
    if changed_only:
        changed = changed_files_vs_main()
        if changed is not None:
            only = {f for f in changed if f.startswith(("skills/", "packages/"))}
            print(f"changed-only mode: validating {len(only)} changed guide file(s)")
            if not only:
                print("no guide files changed — validation passed")
                return
    check_guides(bi, errors, warnings, only_files=only)
    if changed_only:
        check_new_skill_cells(bi, errors, warnings)
    check_packages_frontmatter(bi, errors, only_files=only)
    check_us_federal_deletions(errors)
    if not no_index_check:
        check_index_fresh(errors)
    check_no_deprecated_manifests(errors)
    if not no_index_check:
        check_llms_full_fresh(errors)

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"\nvalidation FAILED: {len(errors)} error(s), {len(warnings)} warning group(s)")
        sys.exit(1)
    print(f"\nvalidation passed ({len(warnings)} warning group(s))")


if __name__ == "__main__":
    main()
