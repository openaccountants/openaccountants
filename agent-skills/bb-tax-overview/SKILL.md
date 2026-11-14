---
name: bb-tax-overview
description: "Overview of the Barbados tax system for income year 2026, to route a question to the right skill. The Barbados Revenue Authority collects personal income tax (after a BBD 25,000 allowance; 2026 band rates held as not yet confirmed), corporation tax (9%, 5.5% for approved small businesses), VAT (17.5%, 7.5% accommodation, 22% telecoms, BBD 200,000 threshold) and PAYE; NISSS collects National Insurance (private sector 11.00% employee, 12.75% employer to BBD 5,360 a month). Trigger on Barbados tax overview, BRA, Barbados tax system. Not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bb-tax-overview"
  jurisdiction: "BB"
  tax_year: "2026"
  last_updated: "2026-11-14"
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

Taxable BBD 75,000 after the BBD 25,000 allowance: BBD 50,000 in the lower band and BBD 25,000 in the upper band. The tax waits for the 2026 band rates (see Not yet confirmed).

```oa-check
name: BB 2026 overview employee 100k
inputs:
  pay: 100000
  allowance: 25000
steps:
  - taxable: pay - allowance
  - lower_band: min(taxable, 50000)
  - upper_band: max(taxable - 50000, 0)
expected:
  taxable: 75000
  lower_band: 50000
  upper_band: 25000
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
| BRA, Income Tax Act legislation page: read for the list of amending Acts (latest 2025-30; no 2026 amending Act listed) | https://bra.gov.bb/About/Legislation-Regulations/Income-Tax-Act | 2026-11-14 |
| Parliament of Barbados, bills and resolutions list: read for 2026 bills (no Income Tax (Amendment) Bill or Act, 2026 listed) | https://www.barbadosparliament.com/bills/ | 2026-11-14 |
| Provisional Collection of Taxes Act, Cap. 85: read for s. 3 (provisional effect of a new tax or rate increase in budget proposals) | https://bra.gov.bb/attachment?file=Attachments%2fProvisional+Collection+of+Taxes+Act%2c+Cap.+85.pdf&name=Provisional+Collection+of+Taxes+Act%2c+Cap.+85 | 2026-11-14 |
| Income Tax (Amendment and Validation) Act, 2024-15: read for s. 43(8) and (9) | https://bra.gov.bb/attachment?file=Attachments%2fIncome+Tax+(Amendment+and+Validation)+Act%2c+2024-15.pdf&name=Income+Tax+(Amendment+and+Validation)+Act%2c+2024-15 | 2026-11-14 |
| BRA, VAT rates: read for rates and threshold | https://bra.gov.bb/Popular-Topics/Value-Added-Tax/VAT-Rates | 2026-11-14 |
| NIS, contribution rates (via Firecrawl): read for category R | https://www.nis.gov.bb/contribution-rates/ | 2026-11-14 |
| BRA, personal income tax: read for the 30 April date | https://bra.gov.bb/Popular-Topics/Employed-Retired-Persons/PIT | 2026-11-14 |
| BRA, companies filing and payment: read for return dates | https://bra.gov.bb/Popular-Topics/Companies/Filing-and-Payment | 2026-11-14 |

Not yet confirmed: the 2026 personal income tax rates: BRA's Policy Note OGC No. 001/2026 says BRA applies 11.5% (taxable income to BBD 50,000) and 27.5% (above) from income year 2026, down from 12.5% and 28.5%, following the 16 March 2026 budget, but no Income Tax (Amendment) Act, 2026 appears on BRA's Income Tax Act legislation page or on Parliament's bills list (both read 14 Nov 2026), and the Provisional Collection of Taxes Act, Cap. 85, s. 3 gives provisional effect only to a new tax or a rate increase, not a cut; the earlier 12.5% and 28.5% rates were not found in an enactment read for this version either, so confirm the rates with BRA before computing or filing; residence and domicile rules (earlier version: resident and domiciled taxed on worldwide income, resident non-domiciled on Barbados-source and remitted income); the currency peg statement; penalties and interest.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bb-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bb-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
