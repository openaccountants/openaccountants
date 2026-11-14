---
name: bb-tax-overview
description: >
  Overview of the Barbados tax system for income year 2026, to route a question
  to the right skill. The Barbados Revenue Authority collects personal income
  tax (11.5% and 27.5% from 2026 after a BBD 25,000 allowance), corporation tax
  (9%, 5.5% for approved small businesses), VAT (17.5%, 7.5% accommodation, 22%
  telecoms, BBD 200,000 threshold) and PAYE; NISSS collects National Insurance
  (private sector 11.00% employee, 12.75% employer to BBD 5,360 a month). Trigger
  on Barbados tax overview, BRA, Barbados tax system. Not reviewed by an
  accountant.
version: 1.0
jurisdiction: BB
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: situation-rules
---

# Barbados Tax Overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone needing the shape of Barbados tax for 2026 (calendar income year) before loading a detailed skill. The Barbados Revenue Authority (BRA) runs income tax, corporation tax, VAT and PAYE through TAMIS; the National Insurance and Social Security Service (NISSS) runs NIS. Amounts are BBD.

| Question | Skill |
|---|---|
| Personal or self-employed income tax | `bb-income-tax` |
| Corporation tax | `bb-corporate-income-tax` |
| VAT | `barbados-vat` |
| PAYE and NIS | `bb-payroll-social` |
| Forming a company | `bb-company-formation` |

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| Personal income tax | 11.5% on taxable income to BBD 50,000, 27.5% above | From income year 2026, after the BBD 25,000 allowance | BRA, Policy Note OGC No. 001/2026: https://bra.gov.bb/attachment?file=Attachments%2FPolicy+Note+2026_Reduction+in+Personal+Income+Tax+Rates_April+2026.pdf&name=Policy+Note+2026_Reduction+in+Personal+Income+Tax+Rates_April+2026 |
| Corporation tax | 9%; 5.5% approved small business | From income year 2024 | Income Tax (Amendment and Validation) Act, 2024-15: https://bra.gov.bb/attachment?file=Attachments%2fIncome+Tax+(Amendment+and+Validation)+Act%2c+2024-15.pdf&name=Income+Tax+(Amendment+and+Validation)+Act%2c+2024-15 |
| VAT | 17.5%; 7.5% tourism accommodation; 22% telecoms | Threshold BBD 200,000 a year | BRA, VAT rates: https://bra.gov.bb/Popular-Topics/Value-Added-Tax/VAT-Rates |
| NIS, private sector | Employee 11.00%, employer 12.75% | Ceiling BBD 5,360 a month in 2026 | NIS, contribution rates: https://www.nis.gov.bb/contribution-rates/ |
| Personal return | 30 April | TAMIS | BRA, personal income tax: https://bra.gov.bb/Popular-Topics/Employed-Retired-Persons/PIT |
| Company return | 15 March or 15 June, by year end | Monthly prepayments from 2025 | BRA, companies filing and payment: https://bra.gov.bb/Popular-Topics/Companies/Filing-and-Payment |

## The base

Income tax is levied on residents and non-residents; there is no tax on capital; the system is self-assessment (BRA). Companies pay on taxable income. VAT is charged on taxable supplies with zero-rated and exempt supplies.

## Deadlines and filing

PAYE by the 15th of the following month; company prepayments by the 15th of each month; personal returns by 30 April; company returns by 15 March or 15 June.

## Penalties and interest

See each skill; not confirmed in this version.

## Cross-border points

Withholding at 15% on payments to non-treaty non-residents (BRA withholding page); in-scope multinational groups pay the Corporation Top-up Tax.

## Two worked examples that recompute

### Example 1: Employee earning BBD 100,000 in 2026

Taxable BBD 75,000: BBD 5,750 + BBD 6,875 = BBD 12,625 (BRA's example).

```oa-check
name: BB 2026 overview employee 100k
inputs:
  pay: 100000
  allowance: 25000
steps:
  - taxable: pay - allowance
  - tax: min(taxable, 50000) * 0.115 + max(taxable - 50000, 0) * 0.275
expected:
  taxable: 75000
  tax: 12625
```

### Example 2: Company profit BBD 500,000 at 9% or 5.5%

BBD 45,000 at 9%; BBD 27,500 as an approved small business.

```oa-check
name: BB 2026 overview company 9% vs 5.5%
inputs:
  profit: 500000
steps:
  - general: profit * 0.09
  - small: profit * 0.055
expected:
  general: 45000
  small: 27500
```

## Ask the client first

1. Individual, self-employed or company?
2. Resident and domiciled in Barbados?
3. Income or turnover for the year?
4. Employees?
5. Payments abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| BRA, Policy Note OGC No. 001/2026: read for the 2026 personal rates | https://bra.gov.bb/attachment?file=Attachments%2FPolicy+Note+2026_Reduction+in+Personal+Income+Tax+Rates_April+2026.pdf&name=Policy+Note+2026_Reduction+in+Personal+Income+Tax+Rates_April+2026 | 2026-11-14 |
| Income Tax (Amendment and Validation) Act, 2024-15: read for s. 43(8) and (9) | https://bra.gov.bb/attachment?file=Attachments%2fIncome+Tax+(Amendment+and+Validation)+Act%2c+2024-15.pdf&name=Income+Tax+(Amendment+and+Validation)+Act%2c+2024-15 | 2026-11-14 |
| BRA, VAT rates: read for rates and threshold | https://bra.gov.bb/Popular-Topics/Value-Added-Tax/VAT-Rates | 2026-11-14 |
| NIS, contribution rates (via Firecrawl): read for category R | https://www.nis.gov.bb/contribution-rates/ | 2026-11-14 |
| BRA, personal income tax: read for the 30 April date | https://bra.gov.bb/Popular-Topics/Employed-Retired-Persons/PIT | 2026-11-14 |
| BRA, companies filing and payment: read for return dates | https://bra.gov.bb/Popular-Topics/Companies/Filing-and-Payment | 2026-11-14 |

Not yet confirmed: residence and domicile rules (earlier version: resident and domiciled taxed on worldwide income, resident non-domiciled on Barbados-source and remitted income); the currency peg statement; penalties and interest.
