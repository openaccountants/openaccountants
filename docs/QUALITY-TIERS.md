# Skill quality states

Every skill shows **Built from the law**. When an approved accountant stands behind it, it also shows **Approved by [name]**. Otherwise it shows **Not yet approved**.

The numeric tiers remain frontmatter metadata:

| `tier` | What the file records |
|---|---|
| `1` | A named accountant's approval claim, recorded in `reviewed_by` and `reviewed_on`. The website resolves that name to a current approved accountant account before showing an approval. |
| `2` | No named accountant approval. Source verification and the independent review required before merge still apply. |

An approved accountant who writes and publishes a skill as their own professional work approves it themselves. They record their own name and approval date in the publishing PR. No second accountant or separate approval PR is required.

An unresolved name, a withdrawn account, an AI commit, a maintenance assignment or an old credit line does not establish publication of the current version as the accountant's own work. One thing does stand in for the accountant's own GitHub account: a review they made signed in on openaccountants.com (see "Approving on the website" below). Licence numbers remain private. Follow [CONTRIBUTING.md](../CONTRIBUTING.md) for the GitHub contribution steps.

## Rules

- `tier: 1` needs a reviewer name. `tier: 2` must not carry one. `scripts/validate-guides.py` errors on either mismatch.
- A reviewer name alone does not make a skill reviewed; `tier` must be `1` as well.
- `reviewed_by` can name the author. The author's own professional publication includes their approval; record it with `tier: 1` and `reviewed_on` in that same PR.
- A substantive edit to a reviewed skill sends it back to `pending_review` until the accountant signs off again.
- A tier-2 skill is a starting point. The reviewer brief in every output says so.

## Counts

Do not hand-type counts into any document. `python3 scripts/coverage-report.py --summary` gives the current number of skills, jurisdictions and reviewed skills; the `counts` block of `index.json` carries the same figures for machines. See [COVERAGE.md](COVERAGE.md) for which rounded claim to quote.

## What the user sees

```
Malta VAT Return
Built from the law
Approved by Name

France VAT Return (CA3)
Built from the law
Not yet approved
```

## Recording an accountant's approval

1. An approved accountant writes and publishes their own work, or approves an existing skill in their jurisdiction.
2. They check the rates, thresholds, forms and deadlines against current law and recompute the worked examples.
3. Their publishing PR records `tier: 1`, `reviewed_by` and `reviewed_on`. The independent source check required before merge can be done by a separate AI reviewer.
4. A maintainer listed in [OWNERS.md](OWNERS.md) merges. Delivery checks must pass before the platform reports the skill live.

The accountant is credited publicly on the skill and in [VERIFIERS.md](../VERIFIERS.md).

## Approving on the website

An accountant does not need a GitHub account to approve a skill. They can review it on openaccountants.com instead. Every change still goes through a pull request here.

1. The accountant signs in and opens the skill. The website shows the file as it is on `main`, alongside a checklist of detected figures, method steps and worked examples. The checklist cannot find every rule; the whole file and its sources are available to read.
2. They mark each item **Right**, or **Wrong** and type the fix. They cannot submit until every item is marked and they confirm that they read the whole Guide.
3. The website keeps the review as a record: who, which file, the file they reviewed, each item and verdict, and the exact file their approval covers.
4. The `accountant-review` workflow opens a pull request from the branch `accountant-review/<record id>`, labelled `accountant-review`. It sets `tier: 1`, `reviewed_by`, `reviewed_on` and changes only the lines the accountant fixed. The commit is the bot's. The PR body lists every item and verdict and links the record.
5. The `validate` check reads the website's signed proof for that record and passes only if it names the one file the PR changes, the name in `reviewed_by`, the date in `reviewed_on`, the file the PR started from, and, byte for byte, the file the PR carries. The receipt is read over HTTPS from the fixed website address. Pull-request jobs receive no private queue or signing key.
6. The worker requests a merge only after all four required checks succeed. Existing repository review rules still apply. After the merge, the website attaches the name only if the merged file is still exactly the file the accountant approved.

So the rule above still holds: the bot's commit proves nothing. The signed review record is the proof.

What the founder sets once:

- `REVIEW_PROOF_SECRET`: a long random value, set in the main-only production environment here and with the same value on the website's server.
- The existing `DERIVED_BUILD_TOKEN` opens the PR and requests the merge. No blanket permission for GitHub Actions to approve pull requests is needed. If repository rules require another GitHub review, the PR waits for it.

## Acceptable sources

A tier-2 skill cites official sources only:

- The tax authority's own publications, forms and instructions (HMRC, IRS, CRA, ATO, BZSt, DGFiP, AEAT, and so on).
- Primary legislation and statutory instruments.
- For the EU: the TEDB rates database and VIES, both at ec.europa.eu.
- OECD material, only for treaty and model-convention text.

Commentary from advisory firms, training-data recall and unsourced web pages are not sources for a figure.

## The skill shape

Tax skills follow the deep-tax shape in [skill-template.md](skill-template.md): who it applies to, rates and thresholds with sources, the base, deadlines, penalties, cross-border points, two worked examples that recompute, the questions to ask the client, and a `## Sources` section with read dates.

## Disclaimer

A quality state describes the review status of a skill, not a guarantee that any specific output is correct. LLMs hallucinate, tax law changes, and individual circumstances vary. Every output must be reviewed by a qualified professional before filing.
