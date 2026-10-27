#!/usr/bin/env python3
"""
Open (or with --update, rewrite) one "[XX] Complete the pack" issue per real jurisdiction, from the
coverage report. Idempotent: a jurisdiction that already has an open issue
with that title is skipped. Needs the gh CLI, logged in.

Usage:
    python3 scripts/open-coverage-issues.py --dry-run        # preview local candidates; no GitHub query
    python3 scripts/open-coverage-issues.py                  # open them
    python3 scripts/open-coverage-issues.py --owner ryan     # one owner only
"""

import argparse
import json
import os
import subprocess
import sys
import time

REPO = "openaccountants/openaccountants"
MILESTONE = "Cover the world"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOMAIN_LABELS = {
    "IT-IND": "individual income tax", "IT-CORP": "corporate income tax", "VAT": "VAT / GST / sales tax",
    "SC": "social contributions", "PR": "payroll withholding", "TP": "transfer pricing",
    "XB": "cross-border: exit, treaties, non-residents",
}


def report(owner=None):
    cmd = [sys.executable, os.path.join(REPO_ROOT, "scripts", "coverage-report.py"), "--json"]
    if owner:
        cmd += ["--owner", owner]
    return json.loads(subprocess.check_output(cmd))


def existing_issues():
    out = subprocess.check_output([
        "gh", "issue", "list", "-R", REPO, "--state", "open", "--label", "coverage",
        "--limit", "1000", "--json", "title,number",
    ])
    return {row["title"]: row["number"] for row in json.loads(out)}


def fmt(codes):
    return ", ".join(f"{c} ({DOMAIN_LABELS[c]})" for c in codes) if codes else "none"


def body_for(row):
    na = "\n".join(f"- {k}: {v}" for k, v in row["not_applicable"].items()) or "none declared yet (add them to the pack README)"
    return f"""Pack: `{row['dir']}`
Owner: {row['owner']}  Region: {row['region']}
Skills now: {row['skills']}  Reviewed: {row['reviewed']}  Stale (>365 days): {row['stale']}

This issue is the GitHub work record for the country. The counts below are inventory only: Guide presence and source preparation do not establish comprehensive coverage.

**Domains present:** {fmt(row['present'])}
**Domains missing:** {fmt(row['missing'])}
**Not applicable:**
{na}

Done when:
- [ ] `{row['dir']}/README.md` declares `applicable:` and `not_applicable:` (with reasons)
- [ ] one skill per applicable tax domain, in the deep-tax shape from docs/skill-template.md (rules, figures with sources, deadlines, penalties, two worked examples that recompute)
- [ ] every material claim is checked against current official sources, with source URLs and read dates in the Guides
- [ ] `python3 scripts/check-examples.py --changed-only --require` passes for the country batch
- [ ] `python3 scripts/validate-guides.py --changed-only` and the required CI checks pass
- [ ] one independent reviewer has checked the full country pack against its sources and examples; all findings are fixed
- [ ] the complete country batch is published in one country PR, not separate PRs for individual Guides
- [ ] after source checks and independent review are recorded, GitHub native auto-merge is enabled only with required CI and reviewer approval protections; otherwise leave the PR for a maintainer
- [ ] a named accountant has reviewed the full applicable pack and each applicable domain is marked Accountant-reviewed (`tier: 1`, `reviewed_by`, `reviewed_on`)
- [ ] `python3 scripts/coverage-report.py --owner {row['owner']}` shows no missing applicable tax domains
- [ ] the PR uses `Closes #N` only after all gates pass; while accountant review is open, use `Refs #N` and leave this issue open
- [ ] maintainer closes this issue only after every gate above passes

See GOAL.md for the three goal tests and the country-batch workflow. A tax-domain map with no missing domain is still not comprehensive coverage until source, example, independent-review and accountant-review gates pass.
"""


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="preview local candidates without querying GitHub")
    ap.add_argument("--owner")
    ap.add_argument("--update", action="store_true", help="rewrite the body of issues that already exist")
    args = ap.parse_args(argv)

    rows = report(args.owner)["rows"]
    if args.dry_run:
        for row in rows:
            title = f"[{row['code']}] Complete the pack"
            labels = f"coverage,owner:{row['owner']}"
            print(f"candidate: {title}  [{labels}]  missing: {', '.join(row['missing']) or 'none'}")
        print("GitHub issue state was not queried; candidates may already have an open issue.")
        return 0

    have = existing_issues()
    opened = skipped = updated = 0
    for row in rows:
        title = f"[{row['code']}] Complete the pack"
        if title in have:
            if args.update and not args.dry_run:
                for attempt in range(4):
                    r = subprocess.run(["gh", "issue", "edit", "-R", REPO, str(have[title]), "--body", body_for(row)],
                                       stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
                    if r.returncode == 0:
                        break
                    time.sleep(5 * (attempt + 1))
                updated += 1
                time.sleep(1)
            else:
                skipped += 1
            continue
        labels = f"coverage,owner:{row['owner']}"
        cmd = [
            "gh", "issue", "create", "-R", REPO, "--title", title, "--label", labels,
            "--milestone", MILESTONE, "--body", body_for(row),
        ]
        # GitHub's GraphQL endpoint fails transiently under a burst of creates.
        for attempt in range(4):
            result = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                break
            time.sleep(5 * (attempt + 1))
        else:
            print("FAILED:", title, result.stderr.strip()[:200], file=sys.stderr)
            continue
        print("opened:", title)
        opened += 1
        time.sleep(1)
    print(f"{'would open' if args.dry_run else 'opened'} {opened}, updated {updated}, skipped {skipped} already open")
    return 0


if __name__ == "__main__":
    sys.exit(main())
