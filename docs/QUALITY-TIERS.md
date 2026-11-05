# Skill quality states

Every skill shows **Built from the law**. When an approved accountant stands behind it, it also shows **Approved by [name]**. Otherwise it shows **Not yet approved**.

The numeric tiers remain frontmatter metadata:

| `tier` | What the file records |
|---|---|
| `1` | A named accountant's approval claim, recorded in `reviewed_by` and `reviewed_on`. The website resolves that name to a current approved accountant account before showing an approval. |
| `2` | No named accountant approval. Source verification and the independent review required before merge still apply. |

An unresolved name, a withdrawn account or historical authorship does not establish approval. Licence numbers remain private. Follow [CONTRIBUTING.md](../CONTRIBUTING.md) for the GitHub contribution steps.

## Rules

- `tier: 1` needs a reviewer name. `tier: 2` must not carry one. `scripts/validate-guides.py` errors on either mismatch.
- A reviewer name alone does not make a skill reviewed; `tier` must be `1` as well.
- An author line (`authored_by`) says who wrote the skill. It is not a review and does not change the state.
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

## How a tier-2 skill becomes reviewed

1. A licensed accountant in the jurisdiction picks up the skill.
2. They check the rates, thresholds, forms and deadlines against current law and recompute the worked examples.
3. They submit corrections by pull request to this repository.
4. A maintainer listed in [OWNERS.md](OWNERS.md) merges; the skill gets `tier: 1`, `reviewed_by` and `reviewed_on`.

The accountant is credited publicly on the skill and in [VERIFIERS.md](../VERIFIERS.md).

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
