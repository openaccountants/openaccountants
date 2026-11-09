---
name: al-cross-border
description: >
  Use this skill whenever asked about Alabama cross-border taxation
  for tax year 2026 -- nexus standards for out-of-state corporations,
  single-sales-factor market sourcing, non-resident individuals with
  Alabama income, part-year residency, and remote-seller sales-tax
  registration. Trigger on "Alabama nexus", "Alabama economic nexus",
  "Alabama non-resident income tax", "Alabama part-year resident",
  "Alabama remote seller". Source-cited draft; ALDOR corporate and
  individual income tax pages read 2026-10-28.
jurisdiction: US-AL
category: cross-border
domain: cross-border
type: cross-country-method
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - al-income-tax
  - al-corporate-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Alabama cross-border taxation

> **Source-cited draft.** Built from the ALDOR Corporate Income Tax and Individual Income Tax pages and the 2025 Form 40 booklet, read 2026-10-28. No accountant has reviewed it. Do not rely on it without review by a qualified Alabama professional.

## Who this applies to

- **Out-of-state corporations:** Alabama income tax attaches to income derived from sources within Alabama (ALDOR Corporate Income Tax page, Amendment 212: "Taxes due by foreign corporations are to be based on income derived from sources within Alabama"). The thresholds at which economic activity creates a filing duty, and the scope of P.L. 86-272 protection, are unconfirmed.
- **Remote sellers:** sales-tax economic nexus applies to remote sellers over the $250,000 retail-sales threshold, required to collect from October 1, 2018 (see `al-sales-tax` and the ALDOR remote-seller FAQ).
- **Non-resident individuals:** taxed on income earned from Alabama sources (ALDOR Individual Income Tax page: taxable income "earned from Alabama sources by non-residents"); the Form 40NR filing threshold is unconfirmed.
- **Part-year residents:** file Form 40 covering the resident period; the proration mechanics are unconfirmed.

## Rates, bands and thresholds

| Item | Rule | Tax year | Source |
|---|---|---|---|
| Foreign corporation base | Alabama-source income only | current | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Apportionment | Single sales factor, tax years beginning on or after January 1, 2021 | TYB >= 2021 | [ALDOR Corporate Income Tax page](https://revenue.alabama.gov/taxes-fees/corporate-income-tax/) |
| Non-resident individuals | Taxed on income earned from Alabama sources | current | [ALDOR Individual Income Tax page](https://revenue.alabama.gov/taxes-fees/individual-income-tax/) |
| Remote-seller sales-tax nexus | Over $250,000 of total retail sales delivered into Alabama the previous calendar year; collect and remit from October 1, 2018 | current | [ALDOR remote-seller FAQ](https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/) |

## The taxable base

- Residents: taxable net income earned from all sources (ALDOR Individual Income Tax page, Application).
- Non-residents: income earned from Alabama sources (same page).
- A federal income tax deduction applies to individual taxpayers (Amendment 225, as published on the ALDOR Individual Income Tax page) -- see `al-income-tax`.
- Composite returns / withholding on non-resident pass-through members (A-6 vehicle) are covered in `al-payroll-withholding`; the statutory trigger is unconfirmed.

## Deadlines and filing

- Individual returns (resident, part-year, non-resident) are due "no later than the due date of the federal return" (2025 Form 40 booklet); an automatic extension to October 15, 2026 applies (booklet).
- Corporations: the Form 20C due date is unconfirmed (see `al-corporate-income-tax`).
- The statutory window for notifying Alabama of federal changes is unconfirmed.

## Penalties and interest

- The general Title 40 penalty provisions apply (percentages unconfirmed).
- Common failure modes: (1) assuming no Alabama filing because the entity has no office -- employees or market sales can create nexus; (2) sourcing services to the wrong state after the 2021 single-factor switch; (3) non-resident members of an LLC ignoring withholding/composite mechanics and filing nothing.

## Cross-border points

- Single sales factor (TYB >= 2021) means market-state sourcing of sales drives the corporate apportionment fraction.
- Remote sellers below the $250,000 threshold "may still apply to participate in the simplif[ied] sellers use tax program" (ALDOR remote-seller FAQ).
- An Alabama exit tax: the prior draft carried "none -- Alabama does not tax departing residents on deferred gains"; that is not confirmed against an archived primary source -- see Not yet confirmed.
- P.L. 86-272 protection, in-state capital-gains situs rules (§40-18-166) and the composite-return authority (§40-18-411): all unconfirmed.

## Worked examples

Client facts in these examples are hypothetical. Only rates from the confirmed table above are used (6.5% corporate rate, single sales factor).

**Example 1: non-resident corporate apportionment**

A Georgia company (hypothetical) with $3,000,000 total sales, $450,000 delivered to Alabama customers, $700,000 Alabama-apportionable base after the federal-tax deduction.

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

**Example 2: non-resident individual income ratio**

A non-resident individual (hypothetical) with $120,000 total income, $30,000 Alabama-source wages -- the Alabama fraction of income:

```oa-check
name: AL non-resident income ratio
inputs:
  al_income: 30000
  total_income: 120000
steps:
  - ratio: al_income / total_income
expected:
  ratio: 0.25
```

## Ask the client first

- Does anyone live or work in Alabama, or are goods/services delivered there -- has nexus been re-tested since the 2021 single-factor switch?
- For moving individuals: the residency dates and where income was earned each period (the part-year allocation mechanics are unconfirmed here).
- Non-resident LLC members: is withholding or a composite election being used (see `al-payroll-withholding`)?
- Remote sellers: were Alabama retail sales over $250,000 in the previous calendar year?

## Sources

| Source | URL | Read on |
|---|---|---|
| ALDOR Corporate Income Tax page (Alabama-source limitation, single sales factor) | https://revenue.alabama.gov/taxes-fees/corporate-income-tax/ | 2026-10-28 |
| ALDOR Individual Income Tax page (rates, resident/non-resident base, Amendment 225) | https://revenue.alabama.gov/taxes-fees/individual-income-tax/ | 2026-10-28 |
| ALDOR remote-seller FAQ (Simplified Sellers Use Tax, $250,000 threshold, October 1, 2018) | https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/ | 2026-10-28 |
| 2025 Alabama Form 40 booklet (due dates, automatic extension) | https://www.revenue.alabama.gov/wp-content/uploads/2026/01/25f40bk.pdf | 2026-10-28 |

Not yet confirmed: the economic-nexus filing thresholds for out-of-state corporations and the scope of P.L. 86-272 protection; the Form 40NR filing threshold for non-resident individuals; the part-year proration mechanics (standard deduction and exemption proration by resident days); whether Alabama imposes an exit tax on departing residents (the prior draft asserted none -- confirm against statute); the §40-18-166 situs rules for intangibles; the composite-return authority §40-18-411; the statutory window for reporting federal audit changes; the general penalty percentages under §40-2A-1; Code of Alabama section text (legislative mirror not retrievable this run).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
