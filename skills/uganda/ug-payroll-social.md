---
name: ug-payroll-social
description: >
  Uganda payroll and social contributions, tax year 2026-27: NSSF at 5% employee and 10% employer, the PAYE bands in force from 1 July 2026, the amendment of July and August returns, remittance by the 15th and Local Service Tax. Use for Uganda questions from URA taxpayers, employers, advisers and foreign investors, including rates, thresholds, filing dates, the URA portal and worked computations. Figures for tax year 2026-27 come from Uganda Revenue Authority pages and the law, and items that could not be opened are named as unverified in the Sources section. Not reviewed by a licensed accountant.
version: 0.2
jurisdiction: UG
category: payroll
tax_year: 2026
tax_year_notes: "2026-27 (1 July 2026 to 30 June 2027)"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uganda Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026-27 (year of income 1 July 2026 to 30 June 2027).

## Who this applies to

All employers, irrespective of number of employees, for employees aged 16 to 55, except those under the Government Pensions scheme (NSSF page). Self-employed people may join voluntarily.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| NSSF employee | 5% of total gross monthly wage | 2026 page | https://www.nssfug.org/about-us/membership/ |
| NSSF employer | 10% of total gross monthly wage | 2026 page | same |
| NSSF total | 15% | 2026 page | same |
| PAYE, to 335,000 a month | Nil | 2026-27 | https://ura.go.ug/en/changes-to-paye-return-form-following-the-income-tax-amendment-act-2026/ |
| 335,001 to 410,000 | 20% over 335,000 | 2026-27 | same |
| 410,001 to 485,000 | 15,000 + 25% over 410,000 | 2026-27 | same |
| 485,001 to 10,000,000 | 33,750 + 30% over 485,000 | 2026-27 | same |
| Above 10,000,000 | As above + 10% over 10,000,000 | 2026-27 | same |

Non-resident bands: see the [income tax skill](ug-income-tax.md).

## The base

NSSF is on total gross monthly wage. PAYE is on total monthly income, salary and other payments (https://ura.go.ug/en/domestic-taxes/paye-rates/).

## Deadlines and filing

NSSF: by the 15th day of the following month (https://www.nssfug.org/about-us/membership/). PAYE return: 15th of the following month (https://ura.go.ug/en/domestic-taxes/returns/).

If July or August 2026 was declared at old rates: download a new PAYE return template from the URA portal, amend the affected returns, use the resulting credit in the next PAYE return, and refund employees, which may be through the next payroll (https://ura.go.ug/en/changes-to-paye-return-form-following-the-income-tax-amendment-act-2026/).

## Penalties and interest

Tax withheld and not paid: 2% a month (https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/, s.136).

## Cross-border points

A non-resident employee has no nil band: see the table in the [income tax skill](ug-income-tax.md). URA treats status by the rules on its PAYE page (https://ura.go.ug/en/domestic-taxes/paye-rates/).

## Two worked examples that recompute

Example 1. Gross UGX 2,000,000 a month. PAYE 33,750 + 30% of 1,515,000 = 488,250. NSSF 100,000 employee and 200,000 employer.

```oa-check
name: Gross 2,000,000
inputs:
  gross: 2000000
steps:
  - paye: 33750 + (gross - 485000) * 0.30
  - employee: gross * 0.05
  - employer: gross * 0.10
  - net: gross - paye - employee
expected:
  paye: 488250.00
  employee: 100000.00
  employer: 200000.00
  net: 1411750.00
```

Example 2. A decision: was July 2026 overpaid? URA's case, salary UGX 500,000: old 52,000, new 38,250, overpaid 13,750, so amend and refund.

```oa-check
name: July overpayment
inputs:
  salary: 500000
steps:
  - old: 25000 + (salary - 410000) * 0.30
  - new: 33750 + (salary - 485000) * 0.30
  - over: old - new
expected:
  old: 52000.00
  new: 38250.00
  over: 13750.00
```

## Ask the client first

- Resident or non-resident employee?
- Age, and any Government Pensions cover?
- Total gross pay including benefits?
- Were July and August 2026 filed at old rates?

## Sources

| Source | URL | Read on |
|---|---|---|
| NSSF, Membership page | https://www.nssfug.org/about-us/membership/ | 2026-11-01 |
| URA notice, Changes to PAYE return form, 7 Sep 2026 | https://ura.go.ug/en/changes-to-paye-return-form-following-the-income-tax-amendment-act-2026/ | 2026-11-01 |
| URA, PAYE rates page | https://ura.go.ug/en/domestic-taxes/paye-rates/ | 2026-11-01 |
| URA, File a Tax Return page (still shows the old UGX 2,820,000 threshold) | https://ura.go.ug/en/domestic-taxes/returns/ | 2026-11-01 |
| URA compendium of domestic tax laws, as of July 2021: ITA Cap 340, VAT Act Cap 349 (only the sections cited; old numbering) | https://ura.go.ug/en/download/compendium-for-various-domestic-tax-laws/ | 2026-11-01 |

Not yet confirmed: no statutory upper NSSF cap (old file; not stated on the page read); the 2021 NSSF amendment and the Act cap number beyond the page's reference to Cap 230; Local Service Tax UGX 5,000 to 100,000 a year, banded by income, paid to the local council (old file cited a secondary source; the law was not opened); NSSF late penalties.

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
