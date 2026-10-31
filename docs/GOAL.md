# Goal: the number one tax repository in the world

Set 22 October 2026 by Michael Cutajar, Ryan Duguid and Jeff Watts. Milestone **Cover the world**, due **6 November 2026**.

## What "number one" means

Every jurisdiction in the catalogue has a **complete, verified, reviewed pack**, and nobody else has that. Three tests; all three must pass before a jurisdiction counts:

1. **Complete.** We go deep on tax first. The pack has one skill, in the deep-tax shape, for each applicable tax domain: IT-IND (individual income tax), IT-CORP (corporate income tax), VAT (VAT, GST or sales tax), SC (social contributions), PR (payroll withholding), TP (transfer pricing) and XB (cross-border: exit tax, treaties, non-residents). "Applicable" is decided per jurisdiction and written in the pack's `README.md` (`applicable:` and `not_applicable:` with a reason; template in [docs/pack-readme-template.md](pack-readme-template.md)). A territory with no VAT has no VAT skill, and says so. Bookkeeping, e-invoicing, financial statements and tax optimisation are the second milestone, **Accounting packs**, and never count as missing here.
2. **Verified.** Every figure is tied to an official source that resolves, the two worked examples in every skill recompute, and the pack passes `scripts/validate-guides.py` and CI. A guide being present is not coverage. Source preparation is not coverage.
3. **Reviewed.** A named accountant has reviewed the pack (`tier: 1` with `reviewed_by` and `reviewed_on`). This is the last step and the slowest: we build and verify first, then bring accountants in per jurisdiction.

There are exactly two quality tiers: **Accountant-reviewed** (`tier: 1`) and `tier: 2`, named **Checked against the law** (built to the standard in docs/skill-template.md) or **Sourced from the law** (older skills not yet rebuilt). See [docs/QUALITY-TIERS.md](QUALITY-TIERS.md). In prose we say "190+ jurisdictions" ([docs/COVERAGE.md](COVERAGE.md)); the exact figures come from the report below, never from a hand count.

## Where we are

`python3 scripts/coverage-report.py --summary`, run on 2026-10-22 (tax domains only):

| Measure | Now |
|---|---|
| Skills | 2,134 |
| Jurisdictions (real codes; pseudo-codes such as GLOBAL and INTL excluded) | 266 |
| Jurisdictions with 7 skills or fewer | 193 |
| Complete tax packs (no applicable tax domain missing) | 4 |
| Packs with a README declaring applicability | 0 |
| Skills with a named reviewer (`tier: 1`) | 33 |

So the work is not "add countries". It is going deep on tax: turning 266 thin or partial packs into complete, verified ones, then getting them reviewed.

## Workstreams

Coverage is one of seven. Each has a label; every issue carries one workstream label and one `owner:` label.

| Label | Workstream | Done when |
|---|---|---|
| `coverage` | Packs | Every jurisdiction's `[XX] Complete the pack` issue is closed by a merged PR |
| `ws:accuracy` | Arithmetic and sources | Worked examples recompute in CI; contradictions and dead links fail CI; stale figures are flagged |
| `ws:provenance` | Where each number came from | Every guide carries `sources: [{url, title, as_of}]`; reviews carry a date and credential |
| `ws:evals` | Proof | A public question set per jurisdiction, a scorer, and `evals/RESULTS.md` refreshed monthly |
| `ws:docs` | Honest docs | No doc contradicts another, the counts, or the two quality states |
| `ws:marketing` | Being found | True badges, every listing quoting the same claim |
| `ws:hygiene` | Trust in the repo | CI gates on every PR, pentest done, CODEOWNERS matches OWNERS.md |

## How work moves

- One issue per jurisdiction, `[XX] Complete the pack`, labelled `coverage` and `owner:<name>`, on the milestone. The issue body lists the domains missing.
- The owner, or their agent, drafts, verifies sources, and opens a PR per jurisdiction or small batch with `Closes #N`. A maintainer merges. Nothing counts until merged.
- A newcomer takes an `owner:open` issue, or asks for one.
- Status is read from the milestone and the Monday coverage report, never from memory.

## For agents

```
gh issue list -R openaccountants/openaccountants -l coverage -l owner:open -m "Cover the world" --state open --json number,title,body
```

Pick one, comment `taking`, branch `pack/<code>`, follow the checklist in the issue body, open a PR with `Closes #N`. The issue body, the pack README and [docs/skill-template.md](skill-template.md) are the whole spec.

## Owners

See [OWNERS.md](OWNERS.md).
