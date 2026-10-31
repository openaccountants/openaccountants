# Skill quality states

Every skill in this repository is in exactly one of two tiers. There is no third. Tier 2 has two names, depending on how the skill was built.

| `tier` | Label | What it means |
|---|---|---|
| `1` | **Accountant-reviewed** | A named, licensed accountant (CPA, CA, EA, Steuerberater, expert-comptable, or the local equivalent) has reviewed the whole skill and put their name and credential on it: `reviewed_by` and `reviewed_on` in frontmatter. The reviewer is credited on the skill and at openaccountants.com. |
| `2` | **Checked against the law** | Built to the standard in [skill-template.md](skill-template.md) (deep-tax shape, `## Sources` table with read dates, independent review before merge). Every figure is cited to the law and checked against the statute by an independent review before merge. No accountant has signed it off yet. |
| `2` | **Sourced from the law** | An older skill not yet rebuilt to that standard. Every figure is cited to an official source. No accountant has signed it off yet. |

The stored identifiers do not change: frontmatter uses `tier: 1` or `tier: 2`, and the legacy `verified_by` key keeps its spelling. In prose, say "Accountant-reviewed" for tier 1, and "Checked against the law" or "Sourced from the law" for tier 2, and nothing else. The retired name "source-cited draft" is not used.

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
Malta VAT Return v1.0
ACCOUNTANT-REVIEWED
Reviewed by: Name, Credential (Malta) · Reviewed on: YYYY-MM-DD

France VAT Return (CA3) v0.1
CHECKED AGAINST THE LAW
Sources: impots.gouv.fr, CGI (read 2026-04-12) · No accountant has signed it off yet
```

## How a tier-2 skill becomes reviewed

1. A licensed accountant in the jurisdiction picks up the skill.
2. They check the rates, thresholds, forms and deadlines against current law and recompute the worked examples.
3. They submit corrections by pull request, or through openaccountants.com.
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
