# Goal: the number one tax repository in the world

Set 22 October 2026 by Michael Cutajar, Ryan Duguid and Jeff Watts. Milestone **Cover the world**, due **6 November 2026**.

## What "number one" means

Every jurisdiction in the catalogue has a **complete, verified, reviewed pack**, and nobody else has that. Three tests; all three must pass before a jurisdiction counts:

1. **Complete.** We go deep on tax first. The pack has one skill, in the deep-tax shape, for each applicable tax domain: IT-IND (individual income tax), IT-CORP (corporate income tax), VAT (VAT, GST or sales tax), SC (social contributions), PR (payroll withholding), TP (transfer pricing) and XB (cross-border: exit tax, treaties, non-residents). "Applicable" is decided per jurisdiction and written in the pack's `README.md` (`applicable:` and `not_applicable:` with a reason; template in [docs/pack-readme-template.md](docs/pack-readme-template.md)). A territory with no VAT has no VAT skill, and says so. Bookkeeping, e-invoicing, financial statements and tax optimisation are the second milestone, **Accounting packs**, and never count as missing here.
2. **Verified.** Every figure is tied to an official source that resolves, the two worked examples in every skill recompute, and the pack passes `scripts/validate-guides.py` and CI. A guide being present is not coverage. Source preparation is not coverage.
3. **Reviewed.** A named accountant has reviewed the pack (`tier: 1` with `reviewed_by` and `reviewed_on`). This is the last step and the slowest: we build and verify first, then bring accountants in per jurisdiction.

There are exactly two quality tiers: **Accountant-reviewed** (`tier: 1`) and `tier: 2`, named **Checked against the law** (built to the standard in docs/skill-template.md) or **Sourced from the law** (older skills not yet rebuilt). See [docs/QUALITY-TIERS.md](docs/QUALITY-TIERS.md). In prose we say "190+ jurisdictions" ([docs/COVERAGE.md](docs/COVERAGE.md)); the exact figures come from the report below, never from a hand count.

## Where we are

`python3 scripts/coverage-report.py --summary`, run on 2026-10-25 (tax-domain inventory only):

| Measure | Now |
|---|---|
| Skills | 2,250 |
| Jurisdiction units in the repository catalogue (countries, territories, US states and Canadian provinces; pseudo-codes such as GLOBAL and INTL excluded) | 266 |
| Jurisdictions with 7 skills or fewer | 184 |
| Tax-domain maps with no missing applicable domain | 33 |
| Packs with a README declaring applicability | 29 |
| Skills with a named reviewer (`tier: 1`) | 33 |

These are inventory counts, not comprehensive-coverage counts. The 33 tax-domain maps only show that the report found a skill for each applicable domain and no domain marked `partial`; the report does not verify sources, examples, independent pack review, or sign-off by a named accountant. It does not yet calculate how many packs pass all three goal tests.

The work is to finish each jurisdiction pack, verify it, and get it reviewed. A skill's presence, a source packet, or a row with no missing domain is not comprehensive coverage.

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

GitHub issues are the work board and the repository is the content record. Do not keep a second board or a shadow assignment list. There is one `[XX] Complete the pack` issue per jurisdiction, labelled `coverage` and `owner:<name>`. The issue records the owner, current gaps, handoffs, independent-review status and accountant-review status. Different countries can move in parallel; only one writer owns a country at a time. Record a handoff on that country's issue before another writer takes it.

Finish all applicable domains for one country locally, source-check every material claim, make sure every Guide has two recomputing worked examples, and run the relevant repository checks. Then get one independent review of the full pack and fix its findings. Publish one country batch, not one PR per Guide. Reuse the active consolidated PR when OWNERS.md assigns the workstream there. After source checks and the independent review are documented, queue the PR for GitHub's native auto-merge. GitHub must require the configured CI checks and reviewer approval before merging. If those protections are not configured, leave the PR pending a maintainer; never bypass the gates.

Sign-off by a named accountant is the final coverage gate. A merged source-cited batch can improve the public library, but it does not complete the country issue or count as comprehensive coverage until the full applicable pack is reviewed by a named accountant and the pack passes the other two goal tests. Use `Closes #N` only when the PR completes those gates; otherwise use `Refs #N` and leave the issue open.

Take an `owner:open` issue only after checking that no writer has an active claim. Record `taking` on the issue before drafting. Status comes from the GitHub issue and merged repository state, not memory or a file count.

## For agents

```
gh issue list -R openaccountants/openaccountants -l coverage -l owner:open -m "Cover the world" --state open --json number,title,body
```

Pick one available country issue, comment `taking`, and work on a country branch. Follow the issue checklist, README and [docs/skill-template.md](docs/skill-template.md). Do not open a PR until the complete country batch has passed source checks and independent pack review. Use `Closes #N` only for a country that also passes the named-accountant gate; otherwise reference the issue and leave it open.

## Owners

See [OWNERS.md](OWNERS.md).
