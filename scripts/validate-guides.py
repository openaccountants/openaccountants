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
     fixed core (domain dates, source read dates, shape examples, numeric version,
     honest approval) ERROR on changed content in every domain, WARN on backlog.
     New files must meet their declared shape. Existing shape failures remain
     warnings, but a check that passed on main may not regress. New or changed
     unsourced/unverified rate rows and barred citations ERROR in every domain.
     Metadata-only relabels do not inherit old body defects; honest tier checks
     still apply. Typography and inferred-source heuristics stay advisory.
     docs/domains.yml supplies each active domain's dates and official hosts;
     tax-looking filenames always retain tax dating. Unknown domains warn.
  8. PR mode only: one job in one jurisdiction has one skill
     (docs/skill-template.md, scripts/job_identity.py). ERROR if an added or
     renamed skill has the job or stripped name of another skill there, unless
     the PR deletes that skill. WARN if its (country, domain) cell is occupied by
     a different job, or no domain can be classified. Pass --duplicates-report to
     write skills/DUPLICATES.md; existing groups are one WARN line on a full run.
  9. PR mode only: a PR that deletes a skill is a merge or a retirement. ERROR
     unless the PR body names it and has `## Moved` and `## Not moved` tables;
     WARN for a heading of the deleted skill those tables do not cover. Outside
     GitHub Actions there is no PR body, so it WARNs.
 10. Sanctioned countries (scripts/data/sanctioned.yml: Russia, Belarus, Cuba,
     Iran, North Korea, Syria). ERROR for any file the PR adds or edits under
     skills/, library/ or evidence/ in one of their folders, or a skill or
     library file whose `jurisdiction:` is one of their codes. A deletion is
     fine. The full run (no --changed-only) checks the whole tree the same way.
 11. Deliverable to the website. After a merge, scripts/deliver-to-platform.py
     sends only `skills/**/<name>.md` files, and the website refuses a skill
     over PLATFORM_MAX_SKILL_BYTES. Both used to fail silently after the
     merge. PR mode: ERROR for an added or edited file under skills/ that is
     not a `.md` file (or the generated skills/REGISTER.csv), for a skill file
     whose name is not lowercase letters, digits and hyphens, a description below
     the website's 40-character minimum, and a skill file over the size limit; each message says what to rename or split. The
     full run WARNs for the same files, so old content never fails on them.

Install scripts/requirements-validation.txt, then run:
python3 scripts/validate-guides.py
"""

import importlib.util
import json
import os
import re
import subprocess
import sys

import job_identity
import label_boilerplate
import repo_layout
import sanctioned
import skill_checks
from frontmatter_yaml import FrontmatterError, load_frontmatter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_INDEX = os.path.join(REPO_ROOT, "scripts", "build-index.py")
COVERAGE_REPORT = os.path.join(REPO_ROOT, "scripts", "coverage-report.py")

#: Fixed-core checks apply to every domain. On the full tree they stay warnings;
#: metadata-only relabels do not inherit old body defects.
PR_ERROR_CHECKS = {
    "tax_year_current",    # (a)
    "sources_read_dates",  # (b)
    "two_oa_checks",       # (e)
    "version_numeric",     # (f)
    "tier_honest",         # (g)
    "reviewed_on",         # (j): approval must have a real, non-future date
}
#: New skills must meet their declared shape. Existing files may improve legacy
#: shape defects incrementally, but may not break a check they previously passed.
PR_SHAPE_CHECKS = {"rates_rows_sourced", "canonical_headings", "not_yet_confirmed", "type_declared"}

# Legacy guides that predate the description requirement. Grandfathered so CI
# can be strict for everything new. Never add to this list — remove entries as
# the files gain descriptions.
LEGACY_MISSING_DESCRIPTION = {
    "skills/global/cross-border/treaty-corridors/americas-corridors.md",
    "skills/global/cross-border/treaty-corridors/asia-pacific-corridors.md",
    "skills/global/cross-border/treaty-corridors/emerging-market-corridors.md",
    "skills/global/cross-border/treaty-corridors/eu-intra-rates.md",
    "skills/global/cross-border/treaty-corridors/uk-major-partners.md",
    "skills/global/cross-border/treaty-corridors/us-major-partners.md",
}

# Dirs whose deliberate convention is "no jurisdiction key" — the content is
# jurisdiction-agnostic (templates, intelligence engines, treaty corridor
# reference tables) or spans the whole EU (the shared eu-vat-base). Missing
# `jurisdiction` here is a WARN, not an ERROR. Everywhere else it is required
# (scripts/backfill-metadata.py did the one-time sweep).
JURISDICTION_OPTIONAL_DIRS = {
    "skills/global/cross-border/treaty-corridors",
    "skills/global/planning-tools",
    "skills/eu",
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
JOB_RE = re.compile(r"^job:[ \t]*(\S+)[ \t]*$", re.MULTILINE)
DUPLICATES_REPORT = os.path.join(REPO_ROOT, "skills", "DUPLICATES.md")


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


def check_staleness(fields, today, dated_by_tax_year=True):
    """Return a problem string when the figures are probably out of date.

    ``dated_by_tax_year`` is False for a skill in an active non-tax domain
    (docs/domains.yml): its date rule is check (a), so a leftover `tax_year`
    is not judged here."""
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
    if dated_by_tax_year and tax_year and str(tax_year).isdigit() and int(tax_year) < today.year - 1:
        problems.append(f"tax_year {tax_year} is two or more years behind")
    return "; ".join(problems) or None


def body_unchanged_vs_main(rel, text):
    """True when only the frontmatter or old label text changed against origin/main.

    A relabel (who approved a skill) must not fail on content checks the
    content itself predates: those stay warnings until the body is edited.
    """
    try:
        old = subprocess.run(
            ["git", "show", f"origin/main:{rel}"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except Exception:  # new file, or no git: treat as changed
        return False
    return skill_checks.admission_content_unchanged(old, text)


def check_approval_resets(rel, text, errors):
    """An approval covers one version (docs/skill-template.md line 11).

    PR mode: if an approved skill's body changes, the PR must either drop the
    approval (no reviewed_by, tier 2) or re-approve it (a new reviewed_on).
    Keeping the old approval on new text would put a name on words that
    person never saw.
    """
    try:
        old = subprocess.run(
            ["git", "show", f"origin/main:{rel}"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except Exception:
        return  # new file: nothing approved yet
    if skill_checks.approved_source_unchanged(old, text):
        return
    key = lambda t, k: (re.search(rf"^{k}:[ \t]*\"?([^\"\n]*)", t, re.M) or [None, ""])[1].strip()
    if not real_reviewer(key(old, "reviewed_by")) or not real_reviewer(key(text, "reviewed_by")):
        return
    if key(text, "reviewed_on") == key(old, "reviewed_on"):
        errors.append(
            f"{rel}: the text or source-owned metadata of an approved skill changed, so the approval no longer covers it. "
            "Either remove `reviewed_by` and `reviewed_on` and set `tier: 2`, or have the approver "
            "re-approve by setting a new `reviewed_on`."
        )


SOURCE_LINK_RE = re.compile(r"https?://(?!(?:www\.)?(?:openaccountants\.com|github\.com))[^\s)>\]]+")


def has_source_link(text):
    """Any link outside our own site and GitHub, in the body."""
    return bool(SOURCE_LINK_RE.search(label_boilerplate.body_of(text)))


def needs_sources(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return bool(m and re.search(r"^status:\s*needs_sources\s*$", m.group(1), re.M))


def changed_files_vs_main():
    """Files changed vs origin/main (PR mode). Empty list = nothing relevant."""
    import subprocess
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", "--no-renames", "--diff-filter=d", "origin/main...HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
        status = subprocess.run(
            ["git", "diff", "--name-status", "-M100%", "origin/main...HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
        moved = repo_layout.pure_moves(status)
        return [l.strip() for l in out.splitlines() if l.strip() and l.strip() not in moved]
    except Exception as e:  # pragma: no cover
        print(f"WARN: could not compute changed files ({e}); validating everything")
        return None


def added_or_edited_vs_main():
    """Every path the PR adds or edits vs origin/main, moves included (a move shows
    as its new path), deletions left out. None when git cannot say."""
    try:
        out = subprocess.run(
            ["git", "diff", "--name-only", "--no-renames", "--diff-filter=d", "origin/main...HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except Exception as e:  # pragma: no cover
        print(f"WARN: could not compute changed files ({e}); checking the whole tree for sanctioned countries")
        return None
    return [line.strip() for line in out.splitlines() if line.strip()]


def _read_or_none(rel):
    try:
        with open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return None


def sanctioned_tree_paths():
    """Every file under skills/, library/ and evidence/ in the working tree."""
    out = []
    for root in ("skills", "library", "evidence"):
        for dirpath, _dirs, files in os.walk(os.path.join(REPO_ROOT, root)):
            for name in files:
                out.append(os.path.relpath(os.path.join(dirpath, name), REPO_ROOT).replace(os.sep, "/"))
    return sorted(out)


def check_sanctioned(errors, paths=None, read=_read_or_none):
    """Line 10: no file for a sanctioned country. `paths` are the PR's added or
    edited files; None checks the whole tree."""
    paths = sanctioned_tree_paths() if paths is None else paths
    for rel in sorted(paths):
        if not rel.startswith(sanctioned.GUARDED_ROOTS):
            continue
        # Only skills and library files carry a jurisdiction worth reading.
        text = read(rel) if rel.startswith(("skills/", "library/")) and rel.endswith((".md", ".json")) else None
        message = sanctioned.problem(rel, text)
        if message:
            errors.append(message)


#: The website refuses a skill file larger than this, after the merge
#: (the limit in its ingest lint). Mirror of the platform's value: change both
#: together. Checked here so the contributor hears it on the PR instead.
#: 110 KB since 11 Nov 2026 (was 100 KB). A split preserves content in distinct
#: linked base/companion jobs, with independent no-loss review; never truncate.
PLATFORM_MAX_SKILL_BYTES = 112_640
PLATFORM_MIN_DESCRIPTION_CHARS = 40

#: Files under skills/ that are not skills and not Markdown. Generated.
NON_MARKDOWN_ALLOWED = {"skills/REGISTER.csv"}

SKILL_FILENAME_RE = re.compile(r"[a-z0-9][a-z0-9-]*\.md")
FRONTMATTER_NAME_RE = re.compile(r"^name:[ \t]*[\"']?([^\"'\n#]+?)[\"']?[ \t]*$", re.MULTILINE)


def is_delivered_skill(rel):
    """Same rule as is_skill in scripts/deliver-to-platform.py: what the website receives."""
    if not re.fullmatch(r"skills/.+/[^/]+\.md", rel):
        return False
    basename = rel.rsplit("/", 1)[-1].lower()
    return not (basename.startswith("readme") or basename == "references.md"
                or re.search(r"/_?templates/", rel))


def _kebab(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def suggested_skill_filename(rel, text):
    """`<name>.md` from the file's own `name:` when it is a usable slug, else from the file name."""
    match = FRONTMATTER_NAME_RE.search(text or "")
    name = match.group(1).strip() if match else ""
    if re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
        return f"{name}.md"
    basename = rel.rsplit("/", 1)[-1]
    stem = basename[:-3] if basename.lower().endswith(".md") else basename
    return f"{_kebab(stem) or 'skill'}.md"


def _size_or_none(rel):
    try:
        return os.path.getsize(os.path.join(REPO_ROOT, rel))
    except OSError:
        return None


def deliverable_problems(paths, read=_read_or_none, size=_size_or_none):
    """Line 11: why a file under skills/ would never reach the website, one message each."""
    problems = []
    for rel in sorted(paths):
        if not rel.startswith("skills/") or rel in NON_MARKDOWN_ALLOWED:
            continue
        folder, basename = rel.rsplit("/", 1)
        if not basename.lower().endswith(".md"):
            target = f"{folder}/{suggested_skill_filename(rel, read(rel))}"
            problems.append(
                f"{rel}: this file is not a `.md` file, so the website will never receive it. "
                f"Rename `{rel}` to `{target}`"
            )
            continue
        if not is_delivered_skill(rel):
            continue  # READMEs, references, templates and the generated lists
        text = read(rel)
        if text is not None:
            description = str(skill_checks.read_frontmatter(text).get("description") or "").strip()
            if len(description) < PLATFORM_MIN_DESCRIPTION_CHARS:
                problems.append(
                    f"{rel}: description has {len(description)} characters; the website team-revision path requires "
                    f"at least {PLATFORM_MIN_DESCRIPTION_CHARS}. Describe the actual job before merging"
                )
        if not SKILL_FILENAME_RE.fullmatch(basename):
            target = f"{folder}/{suggested_skill_filename(rel, read(rel))}"
            problems.append(
                f"{rel}: a skill file name is lowercase letters, digits and hyphens, ending in `.md`. "
                f"Rename `{rel}` to `{target}`"
            )
        nbytes = size(rel)
        if nbytes is not None and nbytes > PLATFORM_MAX_SKILL_BYTES:
            problems.append(
                f"{rel}: the skill is {nbytes:,} bytes and the website's limit is "
                f"{PLATFORM_MAX_SKILL_BYTES:,} bytes, so it would be refused after the merge. "
                f"Split it into a base skill and a child skill that depends on it "
                f"(`depends_on:` in the child), each under the limit"
            )
    return problems


def check_deliverable(errors, warnings, paths=None, read=_read_or_none, size=_size_or_none):
    """`paths` are the PR's added or edited files (errors); None checks the whole tree (warnings)."""
    if paths is None:
        warnings.extend(deliverable_problems(sanctioned_tree_paths(), read, size))
    else:
        errors.extend(deliverable_problems(paths, read, size))


def added_and_deleted_vs_main():
    """(added paths, deleted paths) vs origin/main. A rename to a new filename is
    one of each; a move that keeps the filename keeps the slug and is neither."""
    try:
        out = subprocess.run(
            ["git", "diff", "--name-status", "-M90%", "origin/main...HEAD"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except Exception as e:  # pragma: no cover
        print(f"WARN: could not compute added files ({e}); skipping the one-job-one-skill check")
        return set(), set()
    added, deleted = set(), set()
    for line in out.splitlines():
        fields = line.split("\t")
        if fields[0] == "A":
            added.add(fields[1])
        elif fields[0] == "D":
            deleted.add(fields[1])
        elif fields[0].startswith("R") and os.path.basename(fields[1]) != os.path.basename(fields[2]):
            deleted.add(fields[1])
            added.add(fields[2])
    return added, deleted


def job_conflicts(cov, guides, added, deleted, readme_for, words):
    """(errors, warnings) for the skills in `added`. `guides` is the tree at HEAD;
    `readme_for(guide)` returns the pack's covered_by map."""
    errors, warnings = [], []
    deleted_slugs = {os.path.splitext(os.path.basename(p))[0] for p in deleted}
    live = [g for g in guides if g["path"] not in deleted and (g["slug"] not in deleted_slugs or g["path"] in added)]
    reported = set()
    for g in live:
        code = str(g.get("jurisdiction") or "").upper()
        if g["path"] not in added or not code or code in cov.PSEUDO_CODES:
            continue
        others = [o for o in live if o["slug"] != g["slug"] and str(o.get("jurisdiction") or "").upper() == code]
        same = sorted({o["slug"] for o in others if job_identity.same_job(g, o, words)})
        fresh = [slug for slug in same if frozenset((slug, g["slug"])) not in reported]
        reported.update(frozenset((slug, g["slug"])) for slug in same)
        if fresh:
            errors.append(
                f"{g['path']}: {code} already has this job in {', '.join(fresh)}. One job has one skill: "
                f"merge into it or delete it in this PR. If the work differs, declare a distinct `job:` and rename"
            )
        domains, named = cov.cell_domains(g, readme_for(g))
        if not domains:
            warnings.append(f"{g['path']}: no tax domain in the slug, so its country cell was not checked")
        for d in sorted(domains - named, key=cov.DOMAIN_CODES.index):
            holders = sorted({
                o["slug"] for o in others
                if o["slug"] not in same and d in cov.cell_domains(o, readme_for(o))[0]
            })
            if holders:
                warnings.append(f"{g['path']}: {code} {d} also holds {', '.join(holders)}, with a different job")
    return errors, warnings


def load_coverage():
    spec = importlib.util.spec_from_file_location("coverage_report", COVERAGE_REPORT)
    cov = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cov)
    return cov


def guides_with_jobs(bi):
    """The index rows plus any `job:` frontmatter. The key stays out of index.json."""
    guides = bi.build_index()["guides"]
    for g in guides:
        with open(os.path.join(REPO_ROOT, g["path"]), encoding="utf-8") as fh:
            block = bi.extract_frontmatter(fh.read()) or ""
        match = JOB_RE.search(block)
        if match:
            g["job"] = match.group(1).strip("'\"")
    return guides


def check_new_skill_jobs(bi, errors, warnings):
    added, deleted = added_and_deleted_vs_main()
    if not added:
        return
    cov = load_coverage()
    with open(cov.DATA_PATH, encoding="utf-8") as fh:
        pack_dirs = {row["code"]: row.get("dir") or "" for row in json.load(fh)}
    covered_by = {}

    def readme_for(guide):
        code = str(guide.get("jurisdiction") or "").upper()
        folder = pack_dirs.get(code) or os.path.dirname(guide["path"])
        if folder not in covered_by:
            covered_by[folder] = cov.read_pack_readme(folder)[2]
        return covered_by[folder]

    words = job_identity.load_jurisdiction_words()
    new_errors, new_warnings = job_conflicts(cov, guides_with_jobs(bi), added, deleted, readme_for, words)
    errors.extend(new_errors)
    warnings.extend(new_warnings)


def pull_request_body():
    """The PR description from the Actions event file; None outside a pull_request run."""
    event = os.environ.get("GITHUB_EVENT_PATH")
    if not event or not os.path.exists(event):
        return None
    with open(event, encoding="utf-8") as fh:
        pull_request = json.load(fh).get("pull_request")
    return None if pull_request is None else pull_request.get("body") or ""


def check_merge_records(errors, warnings, pr_body=None, deleted=None, old_text=None):
    """Line 5: a deleted skill's items are all accounted for in the PR body."""
    deleted = added_and_deleted_vs_main()[1] if deleted is None else deleted
    pr_body = pull_request_body() if pr_body is None else pr_body
    for rel in sorted(deleted):
        if not rel.startswith("skills/") or not rel.endswith(".md") or os.path.basename(rel) == "README.md":
            continue
        slug = os.path.splitext(os.path.basename(rel))[0]
        if pr_body is None:
            warnings.append(f"{rel}: deleted; list its items under ## Moved and ## Not moved in the PR body")
            continue
        text = old_text(rel) if old_text else subprocess.run(
            ["git", "show", f"origin/main:{rel}"], cwd=REPO_ROOT, capture_output=True, text=True,
        ).stdout
        problems, notes = skill_checks.merge_record_problems(slug, text, pr_body)
        errors.extend(f"{rel}: {p}" for p in problems)
        warnings.extend(f"{rel}: {n}" for n in notes)


def same_job_report(bi):
    return job_identity.same_job_groups(
        guides_with_jobs(bi), job_identity.load_jurisdiction_words(), load_coverage().PSEUDO_CODES
    )


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


def is_pr_error(name, scope, dated_by_tax_year, content_untouched):
    """In PR mode, whether a failed skill_checks check is an ERROR rather than a warning.

    The fixed core is the same in tax and non-tax domains. Body checks apply
    only when the text changes; label checks always apply."""
    label_check = name in ("tier_honest", "reviewed_on")
    return name in PR_ERROR_CHECKS and (label_check or not content_untouched)


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
        frontmatter = skill_checks.read_frontmatter(text)
        dated_by_tax_year = skill_checks.applied_domain(rel, frontmatter)[0] is None
        problem = check_staleness(fields, today, dated_by_tax_year)
        if problem:
            warn_counts["fresh figures (last_updated within a year, tax_year current)"] += 1
            if only_files is not None:
                per_file_warnings.append(f"{rel}: {problem}")
        # The standard's mechanical lines (scripts/skill_checks.py). A PR that
        # touches a tax skill must pass PR_ERROR_CHECKS; everything else warns.
        scope = skill_checks.scope_of(rel, frontmatter)
        results = skill_checks.run_checks(rel, text, frontmatter)
        content_untouched = only_files is not None and body_unchanged_vs_main(rel, text)
        previous_results = None
        if only_files is not None and not content_untouched:
            check_approval_resets(rel, text, errors)
            try:
                old_text = subprocess.run(["git", "show", f"origin/main:{rel}"], cwd=REPO_ROOT,
                                          capture_output=True, text=True, check=True).stdout
            except subprocess.CalledProcessError:
                old_text = ""  # A new file has no legacy source defects.
            previous_results = skill_checks.run_checks(rel, old_text, skill_checks.read_frontmatter(old_text)) if old_text else {}
            for defect in skill_checks.source_evidence_regressions(old_text, text, rel, frontmatter):
                errors.append(f"{rel}: source evidence regression: {defect}")
            # A tax skill with figures and no source link must say so (status: needs_sources).
            # The site keeps a flagged skill off the site and out of the AI plugin.
            if scope == "tax" and not has_source_link(text) and not needs_sources(text):
                errors.append(
                    f"{rel}: a tax skill with no source link. Add official sources, or set "
                    "`status: needs_sources` in the frontmatter so it stays off the site until they are added."
                )
        for letter, name, _func in skill_checks.CHECKS + skill_checks.LESSON_CHECKS:
            problems = results[name]
            if not problems:
                continue
            message = f"{rel}: ({letter}) {name}: {'; '.join(problems)}"
            shape_regression = (name in PR_SHAPE_CHECKS and previous_results is not None
                                and not previous_results.get(name))
            if only_files is not None and (is_pr_error(name, scope, dated_by_tax_year, content_untouched) or shape_regression):
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
    if "--duplicates-report" in sys.argv:
        groups = same_job_report(bi)
        with open(DUPLICATES_REPORT, "w", encoding="utf-8") as fh:
            fh.write(job_identity.render_report(groups))
        print(f"wrote skills/DUPLICATES.md: {len(groups)} same-job groups")
        return
    only = None
    # Line 10 runs first, on every added or edited path (library and evidence
    # included), so a PR that touches no guide cannot skip it.
    touched = added_or_edited_vs_main() if changed_only else None
    check_sanctioned(errors, touched)
    # Line 11 runs here too: a file that is not `.md` is not a guide, so no
    # later check would ever look at it.
    check_deliverable(errors, warnings, touched)
    if changed_only:
        changed = changed_files_vs_main()
        if changed is not None:
            only = {f for f in changed if f.startswith(("skills/", "packages/"))}
            print(f"changed-only mode: validating {len(only)} changed guide file(s)")
            if not only:
                check_merge_records(errors, warnings)
                if errors:
                    print("\n".join(f"ERROR: {e}" for e in errors))
                    sys.exit(1)
                print("no guide files changed — validation passed")
                return
    check_guides(bi, errors, warnings, only_files=only)
    if changed_only:
        check_new_skill_jobs(bi, errors, warnings)
        check_merge_records(errors, warnings)
    else:
        groups = same_job_report(bi)
        warnings.append(f"{len(groups)} same-job groups, see skills/DUPLICATES.md")
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
