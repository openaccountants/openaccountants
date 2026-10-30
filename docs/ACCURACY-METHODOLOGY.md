# Accuracy methodology

How OpenAccountants skills are built, reviewed and corrected, and what "reviewed" does not mean.

## The problem we are solving

General-purpose LLMs hallucinate tax law: they invent rates, misremember thresholds, cite forms that do not exist, and apply last year's rules to this year. OpenAccountants skills replace the model's guesswork with content drafted from official sources and, where a named accountant has reviewed it, signed off by that person.

## Two quality tiers

See [QUALITY-TIERS.md](QUALITY-TIERS.md) for the full definitions. In short:

| State | Standard | Who |
|---|---|---|
| **Checked against the law** (`tier: 2`) | Built to the standard in [skill-template.md](skill-template.md): every figure cited to the law and checked against the statute by an independent review before merge | No accountant has signed it off yet |
| **Sourced from the law** (`tier: 2`) | Older skill not yet rebuilt to the standard: every figure cited to an official source (tax-authority publications and primary legislation) | No accountant has signed it off yet |
| **Accountant-reviewed** (`tier: 1`) | A licensed accountant has reviewed the whole skill and put their name and credential on it | Named CPA / CA / EA / Steuerberater / local equivalent |

The honest headline is "checked against the law or sourced from the law here, accountant-reviewed where a name is on the file", never a blanket "reviewed by accountants". Most skills in this repo are tier 2 (no accountant sign-off). `python3 scripts/coverage-report.py --summary` gives the exact split; see [COVERAGE.md](COVERAGE.md).

## Sources

Skills are drafted from, and cite, official sources only:

- Tax-authority publications (IRS, HMRC, CRA, ATO, and so on)
- Primary legislation and statutory instruments
- Official forms and their instructions
- OECD material, only for treaty and model-convention text

Training-data recall, commentary from advisory firms and unsourced web results are not acceptable sources for a rate or threshold.

## Conservative by design

When the correct treatment is genuinely uncertain, skills assume the higher-tax, more-compliant position and flag the uncertainty rather than guess in the taxpayer's favour. Every skill surfaces **audit flash points**: the specific spots where a real practitioner should look before anything is filed.

## The gates

CI runs these on every pull request; run them locally with `--changed-only` before you push:

- `scripts/validate-guides.py` checks the frontmatter contract (`tier`, `last_updated`, `jurisdiction`, the reviewer rule) and the generated inventories. The `ws:accuracy` workstream in [GOAL.md](../GOAL.md) extends it to require a `## Sources` section with read dates on every tax skill and to warn when a figure is stale against its source.
- `scripts/check-examples.py` recomputes every `oa-check` block (the two worked examples in each tax skill in the deep-tax shape) and fails on any that does not reproduce its expected figures. It lands with the first packs in that shape; until then the examples are checked by the reviewer.
- `scripts/detect-contradictions.py` flags two skills that state different figures for the same item and year. Run it by hand before a batch merge; it is not yet a CI gate.

A skill that fails a gate is not merged. A skill that passes is still a draft until a named accountant reviews it.

## The correction loop

Accuracy improves in the open. When a skill produces something wrong:

1. Anyone can open an issue or PR with the correct figure and its official source, or email info@openaccountants.com.
2. The fix is applied and the contributor gets public credit.
3. With a licensed accountant's full review, the skill moves from tier 2 to accountant-reviewed (tier 1).

## What "reviewed" does not mean

- It is not tax advice and not a filed return. Every output is a working paper for a human to check.
- A tier-2 skill (checked against the law, or sourced from the law) has not been reviewed by a credentialed practitioner.
- A review reflects the rules as of the skill's stated date; tax law changes, so check the date.
- Coverage of a jurisdiction does not imply coverage of every edge case within it.

The product is designed around this honesty: the AI produces a working paper and, when the user asks, hands it to a person with the hosted tool `share_with_openaccountants` and `request_review: true`.
