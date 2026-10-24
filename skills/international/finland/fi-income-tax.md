---
name: fi-income-tax
description: >
  Prepare Finnish resident individual income-tax workpapers for tax year 2026,
  including the state earned-income scale, capital-income bands, ordinary sole-trader
  profit allocation and the YEL deduction election. Distinguish taxable income from
  gross receipts and state tax from the complete assessment. Use when checking
  Finnish self-employed income, business versus freelance classification, entrepreneur
  deduction ordering, capital-income allocation, personal filing sanctions or MyTax
  reconciliation. Includes executable examples and primary-source read dates. Municipal
  and church amounts, detailed deductions, asset-specific income rules, international
  cases and full statutory and named Finnish accountant review remain open.
version: 1.3
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland individual income tax v1.3

## Who this applies to

This source-cited draft prepares 2026 workpapers for a resident individual and an ordinary sole trader in mainland Finland. Åland requires a separate computation: Income Tax Act section 124 provides a state-scale adjustment for taxpayers whose statutory home municipality is there. Establish the income category before choosing the return: Vero distinguishes miscellaneous income-producing activities, including some freelance receipts, from income reported as a self-employed business. A freelance label does not itself establish business treatment. [Income Tax Act, section 124][income-law]; [personal return instructions][personal-return]

Collect the residence decision, all income categories, municipality, church membership, household facts and deductions before estimating the full assessment. Use the [residence Guide](fi-individual-cross-border-residence.md) for the separate residence screen and the [payroll Guide](fi-employer-payroll.md) for withholding. Neither withholding nor the calculation below establishes final tax.

## Rates, bands and thresholds

The following state scale applies to **taxable earned income for 2026**, not gross wages or business revenue. Municipal and applicable church taxation are additional components with their own bases and deductions. [Act 1140/2025, section 1][scale-law]; [Vero earned-income table][earned]

| Taxable earned income, EUR | State tax at lower limit, EUR | Rate on excess | Source |
|---|---:|---:|---|
| 0 to 22,000 | 0 | 12.64% | [2026 scale, section 1][scale-law] |
| 22,000 to 32,600 | 2,780.80 | 19% | [2026 scale, section 1][scale-law] |
| 32,600 to 40,100 | 4,794.80 | 30.25% | [2026 scale, section 1][scale-law] |
| 40,100 to 52,100 | 7,063.55 | 33.25% | [2026 scale, section 1][scale-law] |
| Above 52,100 | 11,053.55 | 37.50% | [2026 scale, section 1][scale-law] |

| Taxable capital income, EUR | Rate | Source |
|---|---:|---|
| First 30,000 | 30% | [Vero capital income][capital] |
| Excess over 30,000 | 34% | [Vero capital income][capital] |

Apply the capital bands to the established annual taxable capital-income total. Identify exempt portions, deductible costs, losses and special regimes before that step. A gross dividend, sale proceeds or bank receipt is not automatically the taxable capital-income base. [Vero capital income][capital]

## Establish the base and deduction route

For an ordinary sole trader, reconcile receipts and legally deductible costs to the accounts. Vero applies the **5% entrepreneur deduction after allowable prior-year business losses and before dividing the remaining profit between earned and capital income**. It does not create or enlarge a business loss. [Entrepreneur deduction][entrepreneur]

Vero's Form 5 instructions use an ordinary **20% annual return on prior-year business net worth** for the capital portion, with requested alternatives of 10% or all earned income. They add 30% of qualifying wages paid during the preceding 12 months to the net-worth calculation. Fixed-asset real-estate/securities gains can impose a minimum capital portion. Start-up periods, asset valuation, spouse allocation and exceptions need separate checking before using this simplified route. [Form 5 instructions][form5]

Income Tax Act sections 30a, 38 and 41 support these core rules. Section 38 uses the start-up year's closing net worth when business begins during the tax year and requires the alternative allocation request before assessment finishes. Check the gain minimum even when all-earned treatment is requested. Section 96 prevents a duplicate personal pension deduction where the same policy contributions were deducted from business/agriculture. [Income Tax Act][income-law]

**YEL contributions are not restricted to the personal return.** A sole trader can claim eligible paid contributions through Form 5, their personal return or their spouse's return. Choose one route. If booked costs are claimed personally or by the spouse, add them back on Form 5 to prevent a double deduction. See the [YEL Guide](fi-yel-social.md) for insurance eligibility and contribution preparation. [Vero YEL deduction instructions][yel]

Prepare a separate schedule for each deduction, with legal basis, evidence, claimed amount and return location. Current employment deductions, home-office rules, travel, depreciation and health contributions are not quantified here. Obtain the actual municipal and church inputs; an unknown membership or municipality is an unresolved fact.

## Deadlines and filing

Form 5 is required annually, including years without activity. Follow the current return instructions and allocated MyTax deadline. Vero's page states **1 April 2026 for the 2025 return cycle**; that date is not a filing deadline for 2026 income. The reviewed material has not established the 2027 filing calendar. [Self-employed filing page][filing]

The 2026 individual timeline places receipt of the pre-completed personal return in March 2027 and requires corrections by its stated due date. Preserve the submitted return and acknowledgement, then reconcile the assessment with claims and prepayments. For forecast changes, use the [prepayments Guide](fi-prepayments.md). [Reporting timeline][timeline]

## Penalties and interest

Vero distinguishes a **EUR 50 individual late fee** for relevant voluntary late reporting before assessment ends from a punitive tax increase for outstanding omissions or errors. Its summary gives a **EUR 75 minimum** increase and percentage routes based on added taxable income (0.5–10%) or, where that basis cannot be used, added tax (2–50%). The facts determine the route; these are not automatic interchangeable percentages. [Individual sanctions][sanctions]

For ordinary tax paid late, the official calculator lists **9.5% annual late-payment interest in 2026**, from the day after the due date through the payment date. Reduced interest associated with back taxes/additional prepayments is a different mechanism. Use the actual tax type, dates and decision; do not apply a late-payment rate to every pre-assessment balance. [Interest calculator][interest]

## Cross-border points

Separate residence from source and treaty allocation. A resident computation still needs foreign-income classification and double-tax relief; a nonresident needs the applicable income-specific treatment. Use the [individual cross-border Guide](fi-individual-cross-border-residence.md) as an evidence screen. This domestic workpaper supplies no universal treaty rate, day-count exemption or foreign-credit eligibility conclusion.

## Worked examples

### 1. State scale before credits and other components

Assume correctly established taxable earned income of EUR 80,000. State scale tax is EUR 21,516.05. This is before applicable credits and excludes municipal/church taxes, public-broadcasting tax and insurance contributions. It is not total tax on EUR 80,000 gross earnings.

```oa-check
name: Finland 2026 state earned income scale top band
inputs:
  taxable_earned_income: 80000
  band_floor: 52100
  tax_at_floor: 11053.55
  marginal_rate: 0.375
steps:
  excess: taxable_earned_income - band_floor
  state_scale_tax: tax_at_floor + excess * marginal_rate
expected:
  excess: 27900
  state_scale_tax: 21516.05
```

### 2. Capital-income bands

Assume EUR 45,000 of established taxable capital income, with no further reductions. The two bands produce EUR 14,100. This does not establish which receipts or losses enter the base.

```oa-check
name: Finland taxable capital income bands
inputs:
  taxable_capital_income: 45000
  lower_limit: 30000
  lower_rate: 0.30
  upper_rate: 0.34
steps:
  lower_base: min(taxable_capital_income, lower_limit)
  upper_base: max(0, taxable_capital_income - lower_limit)
  capital_income_tax: lower_base * lower_rate + upper_base * upper_rate
expected:
  lower_base: 30000
  upper_base: 15000
  capital_income_tax: 14100
```

### 3. Ordinary sole-trader allocation

Assume revenue of EUR 100,000, deductible costs of EUR 40,000, allowable earlier losses of EUR 10,000 and a correctly established capital-allocation base of EUR 20,000. Assume a full-year ordinary 20% route, no spouse allocation, no fixed-asset gain minimum and no other exceptions. The entrepreneur deduction is EUR 2,500; EUR 47,500 remains, split EUR 4,000 capital and EUR 43,500 earned income. These feed the person's wider assessment; no final tax is calculated.

```oa-check
name: Finland assumed sole trader deduction and split
inputs:
  revenue: 100000
  deductible_costs: 40000
  allowable_prior_losses: 10000
  entrepreneur_rate: 0.05
  established_capital_base: 20000
  assumed_allocation_rate: 0.20
steps:
  business_profit: revenue - deductible_costs
  profit_after_losses: business_profit - allowable_prior_losses
  entrepreneur_deduction: profit_after_losses * entrepreneur_rate
  distributable_income: profit_after_losses - entrepreneur_deduction
  capital_portion: min(distributable_income, established_capital_base * assumed_allocation_rate)
  earned_portion: distributable_income - capital_portion
expected:
  business_profit: 60000
  profit_after_losses: 50000
  entrepreneur_deduction: 2500
  distributable_income: 47500
  capital_portion: 4000
  earned_portion: 43500
```

## Ask the client first

- What establishes residence, income classification and the relevant period?
- Which municipality, church and household facts apply?
- What income, deductions, prior losses and prepayments are supported?
- Which business assets, wage amounts, spouse work and capital-allocation elections apply?
- Who paid YEL, where was it booked and where is the deduction claimed?
- Which return deadline, assessment end date or authority notice is involved?

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Sources and review limits

Read on 23 October 2026. Direct Vero earned/capital pages and indexed official instructions support the preparation rules. Act 1140/2025 sections 1–2 and Income Tax Act sections 30a, 38, 41, 96 and 124 were subsequently read directly from official HTML statutory content after the browser reader returned navigation shells. Every numeric cell in the statutory scale was retained and matched to Vero's table. Selected-section retrieval is not a full Income Tax Act or Business Income Tax Act audit.

- [2026 state scale Act, section 1][scale-law]; [Vero earned-income table][earned].
- [Income Tax Act][income-law], selected sections listed above; retrieval hashes are in the country research record.
- [Capital income][capital]; [entrepreneur deduction][entrepreneur].
- [Form 5 instructions][form5]; [YEL deduction routes][yel].
- [Self-employed filing page][filing]; [personal return instructions][personal-return]; [individual reporting timeline][timeline].
- [Individual sanctions][sanctions]; [official interest calculator][interest].

Not yet confirmed: full statutory/amendment chain; all deductions, credits, municipal/church amounts and income-specific exclusions; business asset valuation and exceptional allocations; 2027 filing dates; specialist cross-border treatment; live filing; named Finnish accountant review. The individual-tax domain remains partial.

[scale-law]: https://www.finlex.fi/fi/lainsaadanto/2025/1140
[income-law]: https://www.finlex.fi/fi/lainsaadanto/1992/1535
[earned]: https://www.vero.fi/henkiloasiakkaat/verokortti-ja-veroilmoitus/tulot/ansiotulot/
[capital]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/income/capital-income/
[entrepreneur]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/deductions/deduction-for-entrepreneurs/
[form5]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/instructions-for-filing/
[yel]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/deductions/pension-premiums-yel/
[filing]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/
[personal-return]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/your_tax_return_and_tax_assessment_deci/instructions-for-filing/
[timeline]: https://vero.fi/en/individuals/tax-cards-and-tax-returns/your_tax_return_and_tax_assessment_deci/tax-decision/when-can-i-report-income-or-deductions-for-my-tax-assessment/
[sanctions]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/your_tax_return_and_tax_assessment_deci/forgotten-to-report-important-details/late-fee-and-tax-increase/
[interest]: https://vero.fi/en/businesses-and-corporations/taxes-and-charges/payments/interest-on-late-payments/interest-calculator/
