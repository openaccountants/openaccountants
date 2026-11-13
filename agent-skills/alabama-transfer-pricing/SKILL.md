---
name: alabama-transfer-pricing
description: "Use this skill whenever asked about Alabama transfer pricing and related-party arrangements for tax year 2026: how intercompany charges move income in and out of the Alabama single-sales-factor base, the Alabama consolidated return (Form 20C-C), and how a federal transfer-pricing adjustment flows through the federal income tax deduction. Trigger on \"Alabama transfer pricing\", \"Alabama consolidated return\", \"Alabama intercompany\", \"Alabama related party\", \"Alabama addback\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/alabama-transfer-pricing"
  jurisdiction: "US-AL"
  tax_year: "2026"
  last_updated: "2026-11-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Alabama transfer pricing and related-party arrangements

> **Source-cited draft.** Built from the ALDOR Corporate Income Tax page and Due Dates page, read 2026-11-13. The Alabama statutes on related-party expense addbacks and consolidated returns were not read, so their mechanics are on the Not yet confirmed line. No accountant has reviewed it.

## Who this applies to

- Alabama corporate taxpayers that pay or receive intercompany charges (management fees, royalties, interest, purchases) with affiliates, especially affiliates outside Alabama.
- Affiliated groups weighing the Alabama consolidated return, which is filed on Form 20C-C (ALDOR Due Dates page).

## Rates, bands and thresholds

| Item | Rule or amount | Tax year | Source |
|---|---|---|---|
| Corporate rate | 6.5% of annual net income, with a deduction for federal income tax paid or accrued | 2026 | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Apportionment | Single sales factor, tax years beginning on or after January 1, 2021 | 2026 | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Consolidated return | Form 20C-C, due on the Form 20C dates (May 15 for calendar years) | 2026 | [ALDOR Due Dates page](https://www.revenue.alabama.gov/individual-corporate/due-dates/) |

## The taxable base

- Federal taxable income is the starting point, so federal transfer-pricing results (including IRS section 482 adjustments) carry into Alabama net income.
- Alabama then allows a deduction for federal income tax paid or accrued (ALDOR Corporate Income Tax page). A federal adjustment that raises federal tax therefore raises the Alabama deduction too, so the Alabama increase is the adjustment less the extra federal tax.
- An intercompany charge paid by an Alabama-apportioning company to an affiliate with no Alabama sales lowers the payer's base; the Alabama tax effect is the charge times the payer's sales factor times 6.5%. This is the exposure Alabama's related-party addback rules and the consolidated election address; their mechanics are on the Not yet confirmed line.

## Deadlines and filing

- The consolidated return follows the corporate return calendar: May 15 for calendar-year groups, with the federal Form 7004 attached when extended (ALDOR Due Dates page; see `al-corporate-income-tax`).

## Penalties and interest

- No Alabama transfer-pricing documentation penalty was found on the pages read; exposure would run through the ordinary underpayment penalty and interest (percentages on the Not yet confirmed line).
- Common failure modes: (1) charging an out-of-state affiliate a management fee or royalty with no support, then finding it added back; (2) forgetting that a federal section 482 adjustment also changes the Alabama federal-tax deduction; (3) applying a pre-2021 three-factor fraction to the payer.

## Cross-border points

- Interstate only: Alabama's related-party surface is the single-sales-factor base of each company, the consolidated return and the addback rules (see `alabama-cross-border`).
- No Alabama counterpart to OECD-style transfer-pricing documentation was found on the pages read.

## Worked examples

Client facts in these examples are hypothetical. Only the 6.5% rate, the federal-tax deduction and the single sales factor from the table above are used. The examples ignore the federal-tax deduction where they say so, to isolate one effect.

**Example 1: management fee paid to an out-of-state affiliate**

OpCo has $900,000 of income before an intercompany fee, Alabama sales of $900,000 and total sales of $2,000,000. It pays a $200,000 management fee to MgmtCo, which has no Alabama sales. Ignoring the federal-tax deduction:

```oa-check
name: AL tax effect of an intercompany fee
inputs:
  income_before_fee: 900000
  fee: 200000
  al_sales: 900000
  total_sales: 2000000
  rate: 0.065
steps:
  - factor: al_sales / total_sales
  - tax_without_fee: income_before_fee * factor * rate
  - tax_with_fee: (income_before_fee - fee) * factor * rate
  - al_tax_reduction: tax_without_fee - tax_with_fee
expected:
  factor: 0.45
  tax_without_fee: 26325.00
  tax_with_fee: 20475.00
  al_tax_reduction: 5850.00
```

**Example 2: federal transfer-pricing adjustment flowing into Alabama**

The IRS adjusts an all-Alabama corporation's income up by $100,000, which raises its federal income tax by $21,000. Alabama allows the extra federal tax as a deduction:

```oa-check
name: AL effect of a federal TP adjustment
inputs:
  adjustment: 100000
  extra_federal_tax: 21000
  factor: 1
  rate: 0.065
steps:
  - al_base_change: adjustment - extra_federal_tax
  - al_tax_change: al_base_change * factor * rate
expected:
  al_base_change: 79000.00
  al_tax_change: 5135.00
```

## Ask the client first

- Which intercompany charges cross into or out of the Alabama filer, and is each supported by a benefit study or agreement?
- Does the group file an Alabama consolidated return (Form 20C-C), or should it?
- Any open federal section 482 adjustments that will change both Alabama income and the federal-tax deduction?
- Does every member's sales-factor numerator use market (delivery) sourcing?

## Sources

| # | Source | URL | Read on |
|---|---|---|---|
| 1 | ALDOR Corporate Income Tax page, read for single sales factor from tax years beginning 2021, 6.5% rate, federal-tax deduction | https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ | 2026-11-13 |
| 2 | ALDOR Due Dates page, read for Form 20C and 20C-C due dates, Form 7004 | https://www.revenue.alabama.gov/individual-corporate/due-dates/ | 2026-11-13 |

Not yet confirmed: Alabama's related-party addback of intercompany interest and intangible expenses and its exceptions (an earlier draft said "none found", which is not established); the consolidated-return eligibility and election rules and whether an election binds later years; whether Alabama requires combined unitary reporting in any case (an earlier draft cited §40-18-50 and ownership thresholds of more than 50% and 80% without a source); the water's-edge treatment of foreign affiliates; the statutory window for reporting federal audit changes; the corporate penalty percentages.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `alabama-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/alabama-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
