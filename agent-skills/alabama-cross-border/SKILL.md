---
name: alabama-cross-border
description: "Use this skill whenever asked about Alabama cross-border taxation for tax year 2026: Alabama-source income of out-of-state corporations, single-sales-factor market sourcing, non-resident individuals with Alabama income (Form 40NR), part-year residency, nonresident real estate withholding, and remote-seller sales-tax registration. Trigger on \"Alabama nexus\", \"Alabama economic nexus\", \"Alabama non-resident income tax\", \"Alabama part-year resident\", \"Alabama remote seller\", \"Alabama Form 40NR\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/alabama-cross-border"
  jurisdiction: "US-AL"
  tax_year: "2026"
  last_updated: "2026-11-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Alabama cross-border taxation

> **Source-cited draft.** Built from the ALDOR Corporate Income Tax and Individual Income Tax pages, the 2025 Form 40 booklet, the ALDOR nonresident real property withholding page and the remote-seller FAQ, read 2026-11-13. No accountant has reviewed it. Do not rely on it without review by a qualified Alabama professional.

## Who this applies to

- **Out-of-state corporations:** Alabama income tax attaches to income derived from sources within Alabama (ALDOR Corporate Income Tax page, Amendment 212: "Taxes due by foreign corporations are to be based on income derived from sources within Alabama").
- **Remote sellers:** sales-tax economic nexus applies to remote sellers over the $250,000 retail-sales threshold, required to collect from October 1, 2018 (see `al-sales-tax` and the ALDOR remote-seller FAQ).
- **Non-resident individuals:** taxed on income earned from Alabama sources (ALDOR Individual Income Tax page); they file Form 40NR when Alabama-source gross income exceeds the prorated personal exemption (2025 Form 40 booklet, p.5).
- **Part-year residents:** file Form 40 for the resident period, and also Form 40NR if they had Alabama-source income while a nonresident (booklet, p.5).
- **Nonresident sellers of Alabama real property:** the buyer withholds under §40-18-86 (ALDOR nonresident withholding page).

## The method, step by step

1. **Classify the taxpayer for the period.** Resident all year (Form 40, all-source income), part-year resident (Form 40 for the resident period), nonresident (Form 40NR, Alabama-source income only), or both Form 40 and Form 40NR where a part-year resident also had Alabama-source income while a nonresident (booklet, p.5).
2. **Part-year resident on Form 40.** Report only income earned while resident. Prorate itemized deductions to expenses incurred while resident, and prorate the federal tax liability by the ratio of Alabama AGI to federal AGI for line 12. The full standard deduction and the full personal and dependent exemptions are allowed (booklet, p.5). Where both returns are filed, claim the whole personal and dependent exemptions on the part-year return and none on the nonresident return (booklet, p.5).
3. **Nonresident on Form 40NR.** Report Alabama-source income; prorate the personal exemption. A return is required if Alabama gross income exceeds the prorated exemption (booklet, p.5).
4. **Corporations.** Test whether the corporation has Alabama-source income. If so, compute net income after the federal income tax deduction, then apportion with the single sales factor (Alabama sales over total sales) for tax years beginning on or after January 1, 2021, and apply 6.5% (ALDOR Corporate Income Tax page; see `al-corporate-income-tax`).
5. **Real property sold by a nonresident.** Withhold 3 percent or 4 percent of the purchase price under §40-18-86 for sales or transfers on or after August 1, 2008, unless the seller gives an exemption affidavit (Form NR-AF1 residence, NR-AF3 exemption) or elects withholding on the gain with Form NR-AF2; report on Form WNR (ALDOR nonresident withholding page). Nonresidents here include individuals, trusts, partnerships, corporations, LLCs, LLPs and unincorporated organizations.
6. **Remote sellers.** Measure the prior calendar year's retail sales delivered into Alabama (direct retail sales only, taxable or not). Over $250,000: register and collect, either at the state and local rates or through the Simplified Sellers Use Tax program at 8% (ALDOR remote-seller FAQ).

## Rates, bands and thresholds

| Item | Rule or amount | Tax year | Source |
|---|---|---|---|
| Foreign corporation base | Alabama-source income only | 2026 | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Corporate rate and apportionment | 6.5%; single sales factor, tax years beginning on or after January 1, 2021 | 2026 | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Non-resident individuals | Taxed on income earned from Alabama sources | 2026 | [ALDOR Individual Income Tax page](https://revenue.alabama.gov/taxes-fees/individual-income-tax/) |
| Part-year resident filing threshold (while resident), 2025 | Single $4,500; head of family $8,200; married filing joint $11,500; married filing separate $5,750 | 2025 | [2025 Form 40 booklet, p.5](https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf) |
| Nonresident real property withholding (§40-18-86) | 3 percent or 4 percent of the purchase price, or withholding on the gain with Form NR-AF2 | 2026 | [ALDOR nonresident withholding page](https://www.revenue.alabama.gov/individual-corporate/nonresidentwh/) |
| Remote-seller sales-tax nexus | Over $250,000 of total retail sales delivered into Alabama the previous calendar year; collect and remit from October 1, 2018 | 2026 | [ALDOR remote-seller FAQ](https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/) |
| Simplified Sellers Use Tax | 8% flat on all sales into Alabama | 2026 | [ALDOR remote-seller FAQ](https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/) |

## Deadlines and filing

- Individual returns (resident, part-year, non-resident) are due "no later than the due date of the federal return," with an automatic extension to October 15, 2026 (2025 Form 40 booklet).
- Corporations: Form 20C is due one month after the federal due date (May 15 for calendar years) (see `al-corporate-income-tax`).

## Penalties and interest

- Individual late-filing penalty: 10% of the tax due or $50, whichever is greater; late payment: 1% a month to a maximum of 25% (2025 Form 40 booklet, p.17).
- Common failure modes: (1) assuming no Alabama filing because the entity has no office, when market sales can create Alabama-source income; (2) sourcing sales to the wrong state after the 2021 single-factor switch; (3) splitting exemptions between Form 40 and Form 40NR when the booklet puts them all on the part-year return; (4) closing a nonresident's Alabama property sale without the §40-18-86 withholding or an exemption affidavit.

## Worked examples

Client facts in these examples are hypothetical. Only figures from the table above are used.

**Example 1: non-resident corporate apportionment**

A Georgia company with $3,000,000 total sales, $450,000 delivered to Alabama customers, and a $700,000 base after the federal-tax deduction.

```oa-check
name: AL non-resident corporate apportionment
inputs:
  al_sales: 450000
  total_sales: 3000000
  base: 700000
  rate: 0.065
steps:
  - factor: al_sales / total_sales
  - apportioned: base * factor
  - tax: apportioned * rate
expected:
  factor: 0.15
  apportioned: 105000.00
  tax: 6825.00
```

**Example 2: part-year resident's federal tax deduction**

A single filer moved to Alabama during the year. Federal AGI is $120,000, Alabama AGI for the resident period is $30,000, and the federal tax liability is $14,000. Line 12 is prorated by Alabama AGI over federal AGI.

```oa-check
name: AL part-year federal tax deduction proration
inputs:
  al_agi: 30000
  federal_agi: 120000
  federal_tax: 14000
steps:
  - ratio: al_agi / federal_agi
  - line_12: federal_tax * ratio
expected:
  ratio: 0.25
  line_12: 3500.00
```

## Ask the client first

- Does anyone live or work in Alabama, or are goods delivered there? Has Alabama-source income been re-tested since the 2021 single-factor switch?
- For moving individuals: the residency dates and where income was earned in each period.
- Non-resident LLC members: is withholding or a composite election being used (see `al-payroll-withholding`)?
- Is any Alabama real property being sold by a nonresident, and has the seller signed an NR-AF affidavit?
- Remote sellers: were Alabama retail sales over $250,000 in the previous calendar year?

## Sources

| # | Source | URL | Read on |
|---|---|---|---|
| 1 | ALDOR Corporate Income Tax page, read for Alabama-source limitation, 6.5%, single sales factor | https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ | 2026-11-13 |
| 2 | ALDOR Individual Income Tax page, read for resident and non-resident base, Amendment 225 | https://revenue.alabama.gov/taxes-fees/individual-income-tax/ | 2026-11-13 |
| 3 | 2025 Alabama Form 40 booklet (Form 40NR and part-year rules, filing thresholds, due dates, automatic extension, penalties) | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf | 2026-11-13 |
| 4 | ALDOR Withholding Requirement on Sales/Transfers of Real Property by Nonresidents (§40-18-86, 3 or 4 percent, NR-AF forms, Form WNR) | https://www.revenue.alabama.gov/individual-corporate/nonresidentwh/ | 2026-11-13 |
| 5 | ALDOR remote-seller FAQ, read for Simplified Sellers Use Tax 8%, $250,000 threshold, October 1, 2018 | https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/ | 2026-11-13 |

Not yet confirmed: which nonresident sellers withhold at 3 percent and which at 4 percent under §40-18-86; the economic-nexus filing thresholds for out-of-state corporations and the scope of P.L. 86-272 protection; whether Alabama imposes any exit tax on departing residents (an earlier draft asserted none); the §40-18-166 situs rules for intangibles; the composite-return and pass-through withholding authority; the statutory window for reporting federal audit changes; the corporate penalty percentages.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `alabama-cross-border` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/alabama-cross-border. If neither is available, confirm every figure against the official source pages cited above before relying on it.
