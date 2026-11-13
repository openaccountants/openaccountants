---
name: al-corporate-income-tax
description: "Use this skill whenever asked about Alabama corporate income tax for tax year 2026: the flat 6.5% rate with the deduction for federal income tax paid or accrued, single sales factor apportionment for tax years beginning on or after 2021, the Form 20C due date, and the business privilege tax rate range. Trigger on \"Alabama corporate tax\", \"Alabama 6.5 percent\", \"Alabama Form 20C\", \"Alabama single sales factor\", \"Alabama business privilege tax\", \"Ala Code 40-18\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/al-corporate-income-tax"
  jurisdiction: "US-AL"
  tax_year: "2026"
  last_updated: "2026-11-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Alabama corporate income tax

> **Source-cited draft.** Built from the Alabama Department of Revenue Corporate Income Tax page, Due Dates page and Business Privilege Tax Incentives page, read 2026-11-13. No accountant has reviewed it. Do not rely on it without review by a qualified Alabama professional.

## Who this applies to

- Corporations with net taxable income from business within Alabama, and foreign (out-of-state) corporations on income derived from sources within Alabama (ALDOR Corporate Income Tax page: "Corporations - Net taxable income from business within the state"; Amendment 212: "Taxes due by foreign corporations are to be based on income derived from sources within Alabama").
- For tax years beginning on or after January 1, 2021, Alabama income is determined by single sales factor apportionment (ALDOR Corporate Income Tax page).
- Corporations and other entities also file the Alabama business privilege tax, a separate tax on net worth in Alabama (ALDOR Business Privilege Tax Incentives page).
- Affiliated groups: an Alabama consolidated return is filed on Form 20C-C (ALDOR Due Dates page); see `alabama-transfer-pricing`.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate income tax | 6.5% of annual net income | 2026 | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Base modification | Deduction allowed for federal income tax paid or accrued | 2026 | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Apportionment | Single sales factor for tax years beginning on or after January 1, 2021 | 2021 onward | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Form 20C due date, calendar-year C corporation | Return May 15 (one month after the federal due date, Act 2022-53); the tax itself is due without that extra month | 2026 | [ALDOR Due Dates page](https://www.revenue.alabama.gov/individual-corporate/due-dates/) |
| Form 20C due date, fiscal year (not June 30) | 15th day of the 5th month after the fiscal year end; June 30 year end: October 15 | 2026 | [ALDOR Due Dates page](https://www.revenue.alabama.gov/individual-corporate/due-dates/) |
| Business privilege tax rate | $0.25 to $1.75 for each $1,000 of net worth in Alabama, graduated by federal taxable income apportioned to Alabama | 2026 | [ALDOR Business Privilege Tax Incentives page](https://www.revenue.alabama.gov/tax-incentives/business-privilege-tax-incentives/) |
| Business privilege tax return due date, C corporation | Same date as the federal income tax return: 15th day of the 4th month after the start of the taxable year (fiscal year June 30: 15th day of the 3rd month) | 2026 | [ALDOR Due Dates page](https://www.revenue.alabama.gov/individual-corporate/due-dates/) |
| Business privilege tax minimum / maximum | Minimum $50; maximum $15,000 for most entities ($3 million for financial institutions, financial institution groups and insurance companies) | 2026 | [ALDOR Business Privilege Tax Incentives page](https://www.revenue.alabama.gov/tax-incentives/business-privilege-tax-incentives/) |

Statutory authority (ALDOR Corporate Income Tax page): Sections 40-18-1 to 40-18-59 and 40-18-160 to 40-18-176, Code of Alabama 1975; franchise-tax authority Sections 40-27-1 to 40-27-6. Rate history: Amendment 212 (ratified December 18, 1963) raised the allowable maximum to 5 percent with the federal-tax deduction; Amendment 662 (ratified June 19, 2000) raised the rate to 6.5 percent beginning calendar year 2001.

The distinctive base feature: "6.5 percent of annual net income with a deduction allowed for federal income tax paid or accrued" (ALDOR page). The Alabama effective rate therefore moves with the federal bill: a restructuring that changes federal tax changes Alabama tax even with identical net income.

## The taxable base

- Net taxable income from business within the state (ALDOR page, Application).
- A deduction is allowed for federal income tax paid or accrued (ALDOR page).
- Foreign corporations: taxes due are based on income derived from sources within Alabama (Amendment 212, as published on the ALDOR page).
- Multistate corporations apportion with the single sales factor (Alabama sales over total sales).

## Deadlines and filing

- Form 20C, calendar year: return due May 15. The one-month extra time from Act 2022-53 is "an extension for filing purposes ONLY. The full amount of the tax liability is due on or by the original due date of the return without the benefit of the additional one-month extension" (ALDOR Due Dates page). Fiscal year other than June 30: the 15th day of the 5th month after year end; June 30 year end: October 15. Form 1120-F filers: July 15 for calendar years (ALDOR Due Dates page).
- Extensions: "If an extension has been granted for federal purposes, the extension is also granted for Alabama purposes; the Federal Form 7004 must be submitted with the Form 20C or Form 20C-C" (ALDOR Due Dates page).
- An Alabama consolidated return is filed on Form 20C-C, on the same dates (ALDOR Due Dates page).
- Business privilege tax returns: C corporations on the federal return date (15th day of the 4th month for calendar years); S corporations and limited liability entities on the federal return date, the 15th day of the 3rd month after the start of the taxable year (ALDOR Due Dates page).

## Penalties and interest

- Late-filing and late-payment penalties and interest run under the general provisions of Title 40; the percentages are on the Not yet confirmed line.
- Common failure modes to check for: (1) forgetting the federal-income-tax deduction when projecting Alabama cost on a restructuring that changes the federal bill; (2) apportioning with a pre-2021 multi-factor spreadsheet; (3) missing the business privilege tax while focused on the income tax; (4) paying the tax with the return on May 15, when the tax was due without the Act 2022-53 extra month, or filing an extended return without the federal Form 7004.

## Cross-border points

- Foreign (out-of-state) corporations are taxed only on income derived from sources within Alabama (Amendment 212, ALDOR page).
- Single sales factor means market-state sourcing of sales drives the apportionment fraction; see `alabama-cross-border` and `alabama-transfer-pricing`.

## Worked examples

Client facts in these examples are hypothetical. Only figures from the table above are used (6.5% rate, federal-tax deduction, single sales factor).

**Example 1: domestic corporation, federal-tax deduction**

A domestic corporation with $500,000 federal taxable income and $60,000 federal income tax paid, 100% Alabama sales.

```oa-check
name: AL corporate tax with federal tax deduction
inputs:
  fti: 500000
  fed_tax: 60000
  rate: 0.065
steps:
  - al_base: fti - fed_tax
  - tax: al_base * rate
expected:
  al_base: 440000.00
  tax: 28600.00
```

**Example 2: multistate single sales factor**

Same corporation, total sales $5,000,000, Alabama sales $1,200,000.

```oa-check
name: AL single sales factor apportionment
inputs:
  al_sales: 1200000
  total_sales: 5000000
  al_base: 440000
  rate: 0.065
steps:
  - factor: al_sales / total_sales
  - apportioned: al_base * factor
  - tax: apportioned * rate
expected:
  factor: 0.24
  apportioned: 105600.00
  tax: 6864.00
```

## Ask the client first

- Is the federal-income-tax deduction modelled in state projections (it moves with federal credits, NOLs, capitalization)?
- Post-2021 apportionment: is the sales-factor numerator market-based and complete (delivery state for tangible goods)?
- Is the business privilege tax return being filed alongside the income tax?
- Is the group filing separately or on an Alabama consolidated return (Form 20C-C)?
- Fiscal year end, and has a federal extension (Form 7004) been filed?

## Sources

| # | Source | URL | Read on |
|---|---|---|---|
| 1 | ALDOR Corporate Income Tax page, read for rate 6.5% with federal-tax deduction, single sales factor from tax years beginning 2021-01-01, authority sections, Amendments 212 and 662 | https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ | 2026-11-13 |
| 2 | ALDOR Due Dates page, read for Form 20C and 20C-C due dates, Act 2022-53, payment timing, Form 7004 extension, business privilege tax due dates | https://www.revenue.alabama.gov/individual-corporate/due-dates/ | 2026-11-13 |
| 3 | ALDOR Business Privilege Tax Incentives page, read for rate $0.25 to $1.75 per $1,000 of net worth, $50 minimum, $15,000 maximum | https://www.revenue.alabama.gov/tax-incentives/business-privilege-tax-incentives/ | 2026-11-13 |

Not yet confirmed: the corporate estimated-tax installment rules and safe harbor; any minimum corporate income tax; the business privilege tax bands linking each rate to apportioned federal taxable income; the Alabama consolidated-return eligibility and election rules; the §40-18-7 state-modification provisions; the S-corporation composite/pass-through mechanics; the §40-2A-11 penalty percentages for corporate returns; the Uniform Division of Income for Tax Purposes Act text under §40-18-160 onward.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `al-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/al-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
