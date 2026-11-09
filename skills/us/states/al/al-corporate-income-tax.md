---
name: al-corporate-income-tax
description: >
  Use this skill whenever asked about Alabama corporate income tax
  for tax year 2026 -- the flat 6.5% rate with the deduction for
  federal income tax paid, single sales factor apportionment for tax
  years beginning on or after 2021, Form 20C mechanics, and the
  franchise-tax authority. Trigger on "Alabama corporate tax",
  "Alabama 6.5 percent", "Alabama Form 20C", "Alabama combined
  reporting", "Alabama single sales factor", "Ala Code 40-18".
jurisdiction: US-AL
category: corporate
domain: corporate
type: rates-card
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - al-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Alabama corporate income tax

> **Source-cited draft.** Built from the Alabama Department of Revenue Corporate Income Tax page (read 2026-10-28), citing Sections 40-18-1 through 40-18-59 and 40-18-160 through 40-18-176, and Sections 40-27-1 through 40-27-6, Code of Alabama 1975, and constitutional Amendments 212 and 662. No accountant has reviewed it. Do not rely on it without review by a qualified Alabama professional.

## Who this applies to

- Corporations with net taxable income from business within Alabama, and foreign (out-of-state) corporations on income derived from sources within Alabama (ALDOR Corporate Income Tax page: "Corporations – Net taxable income from business within the state"; Amendment 212: "Taxes due by foreign corporations are to be based on income derived from sources within Alabama").
- For tax years beginning on or after January 1, 2021, Alabama income is determined by single sales factor apportionment (ALDOR page: "For tax years beginning on or after January 1, 2021, Alabama income is determined by a single sales factor apportionment").
- Unitary groups: combined reporting is discussed in `al-transfer-pricing`; the statutory mandate and its text are unconfirmed.
- S corporations and pass-throughs pay the composite/pass-through tax on members' Alabama income rather than entity-level income tax (mechanics unconfirmed).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Corporate income tax | 6.5% of annual net income | current | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Base modification | Deduction allowed for federal income tax paid or accrued | current | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Apportionment | Single sales factor for tax years beginning on or after January 1, 2021 | TYB >= 2021 | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Statutory authority | Sections 40-18-1 to 40-18-59 and 40-18-160 to 40-18-176, Code of Alabama 1975 | current | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Franchise-tax authority | Sections 40-27-1 to 40-27-6, Code of Alabama 1975 | current | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Rate history | Amendment 212 (ratified December 18, 1963) raised the allowable maximum to 5 percent with the federal-tax deduction; Amendment 662 (ratified June 19, 2000) raised the rate to 6.5 percent beginning calendar year 2001 | current | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |

The distinctive base feature: "Rate 6.5 percent of annual net income with a deduction allowed for federal income tax paid or accrued" (ALDOR page). The Alabama effective rate therefore moves with the federal bill -- a restructuring that changes federal tax changes Alabama tax even with identical net income.

## The taxable base

- Net taxable income from business within the state (ALDOR page, Application).
- A deduction is allowed for federal income tax paid or accrued (ALDOR page, Amendment 212 language: "increased the allowable maximum corporate income tax rate to 5 percent, with deduction allowed for all federal income taxes paid").
- Foreign corporations: taxes due are based on income derived from sources within Alabama (Amendment 212, as published on the ALDOR page).
- The specific state modifications under §§40-18-7 et seq. are unconfirmed.

## Deadlines and filing

- Form 20C is the Alabama corporate income tax return. Its due date, extension rules and estimated-tax installment percentages are unconfirmed before advising a client on filing dates.
- Franchise tax filings run under §§40-27-1 to 40-27-6 (ALDOR page, Authority); rates and due dates are unconfirmed.

## Penalties and interest

- Late-filing and late-payment penalties and interest run under the general provisions of Title 40 (percentages unconfirmed).
- Common failure modes to check for: (1) forgetting the federal-income-tax deduction when projecting Alabama cost on a restructuring that changes the federal bill; (2) apportioning with a pre-2021 multi-factor spreadsheet; (3) missing the franchise tax while focused on the income tax.

## Cross-border points

- Foreign (out-of-state) corporations are taxed only on income derived from sources within Alabama (Amendment 212, ALDOR page).
- Single sales factor means market-state sourcing of sales drives the apportionment fraction -- see `al-cross-border` and `al-transfer-pricing`.
- Alabama has no income tax treaty; interstate allocation under §40-18-160+ (Uniform Division of Income for Tax Purposes Act) is unconfirmed.

## Worked examples

Client facts in these examples are hypothetical. Only rates from the confirmed table above are used (6.5% rate, federal-tax deduction, single sales factor).

**Example 1: domestic corporation, federal-tax deduction**

A domestic corporation (hypothetical) with $500,000 federal taxable income and $60,000 federal income tax paid, 100% Alabama sales.

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

Same corporation (hypothetical), total sales $5,000,000, Alabama sales $1,200,000.

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

- Is the federal-income-tax deduction modeled in state projections (it moves with federal credits, NOLs, capitalization)?
- Post-2021 apportionment: is the sales-factor numerator market-based and complete (delivery state for tangible goods)?
- Is the franchise tax being filed alongside the income tax?
- Any unitary affiliates that may trigger combined reporting (see `al-transfer-pricing`)?

## Sources

| Source | URL | Read on |
|---|---|---|
| ALDOR Corporate Income Tax page (rate 6.5% with federal-tax deduction, single sales factor from TYB 2021-01-01, authority sections, Amendments 212 and 662) | https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ | 2026-10-28 |

Not yet confirmed: the Form 20C due date and extension rules (previously carried as "follows the federal due date, April 15 for calendar-year filers"); the corporate estimated-tax installment percentages and safe harbor; the minimum tax; franchise-tax rates and due dates; the §40-18-7 state-modification provisions; the combined-reporting mandate and unitary-group definition under §40-18-50; the S-corporation composite/pass-through mechanics; the §40-2A-1 penalty percentages; the Uniform Division of Income for Tax Purposes Act text under §40-18-160+; Code of Alabama section text (the legislative mirror was not retrievable this run -- the ALDOR page's citation of the sections is archived, the section text is not).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
