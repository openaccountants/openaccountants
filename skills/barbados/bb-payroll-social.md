---
name: bb-payroll-social
description: >
  Barbados employer payroll for 2026, PAYE and National Insurance. Gives the
  private sector NIS rates (employee 11.00%, employer 12.75% of insurable
  earnings), the 2026 ceiling of BBD 5,360 a month or BBD 1,238 a week, the
  Resilience and Regeneration Fund of 0.25% each on gross earnings, PAYE after the BBD 25,000
  allowance with tax codes (2026 band rates held as not yet confirmed),
  and remittance by the 15th of the following month. Trigger on Barbados payroll,
  PAYE Barbados, NIS Barbados, NISSS, Resilience and Regeneration Fund. Built
  from BRA and NIS pages; not reviewed by an accountant.
version: 1.0
jurisdiction: BB
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
tier: 2
domain: payroll
type: computation
---

# Barbados Payroll and Social Contributions v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Private sector employers in Barbados paying wages and salaries in 2026. PAYE goes to the Barbados Revenue Authority (BRA); NIS contributions to the National Insurance and Social Security Service (NISSS). Amounts are BBD.

Out of scope: government employees (categories P and T), apprentices, foreign embassies, voluntary contributors; the employee's own return (use `bb-income-tax`).

## Rates, bands and thresholds

| Item | Employee | Employer | Conditions | Source |
|---|---|---|---|---|
| National Insurance | 6.75% | 6.75% | Private sector employees, category R, on insurable earnings | NIS, contribution rates and earnings ceilings: https://www.nis.gov.bb/contribution-rates/ |
| Non-contributory | 2.00% | 2.00% | same | same |
| Unemployment | 0.75% | 0.75% | same | same |
| Employment injury | 0.00% | 0.75% | same | same |
| Severance | 0.00% | 0.50% | same | same |
| Training levy | 0.50% | 0.50% | same | same |
| Health service contribution | 1.00% | 1.50% | same | same |
| Total, category R | 11.00% | 12.75% | Total 23.75% | same |
| Resilience and Regeneration Fund | 0.25% | 0.25% | On gross earnings, from 1 April 2025 | same |
| Pensionable age or under 16, category E | 0.50% | 1.25% | Employment injury and training levy only | same |
| Insurable earnings ceiling 2026 | BBD 5,360 a month | BBD 1,238 a week | Monthly from 1 January 2026; weekly from 5 January 2026 | NIS, increase in earnings ceiling 2026: https://www.nis.gov.bb/increase-in-earnings-ceiling-2026/ |
| PAYE starting point | Over BBD 481 a week or BBD 2,083 a month | | | BRA, guide to PAYE: https://bra.gov.bb/Popular-Topics/Employing-People/Guide-to-PAYE |
| PAYE remittance | | By the 15th of the month after deduction | Monthly PAYE return through TAMIS | same |

## The base

- **Insurable earnings** are capped at the ceiling; the Resilience and Regeneration Fund is on gross earnings, uncapped.
- **PAYE** uses the employee's tax code from claimed allowances (250M for the BBD 25,000 basic allowance, monthly) and BRA's tax tables (effective income year 2020 instructions; the 2026 band rates are under Not yet confirmed).
- **Basic salary** for the PAYE upload is total remuneration less taxable allowances and benefits.
- **Employee TINs** must be 13 digits on the monthly return.
- The earlier version's note that employer components summed to 13.00% was wrong: NIS lists 12.75% for category R.

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | Register as an employer with NIS and with BRA for PAYE | Before the first payroll |
| 2 | Deduct PAYE, NIS and the Resilience and Regeneration Fund | Each pay |
| 3 | File the monthly PAYE return (BRA upload template) and pay | By the 15th of the following month |
| 4 | Pay NIS contributions | See Not yet confirmed |

## Penalties and interest

Not confirmed on the pages read for this version; see Not yet confirmed.

## Cross-border points

Social security agreements and non-resident employees: not covered; refer.

## Two worked examples that recompute

### Example 1: Monthly pay BBD 6,000 in 2026, standard allowance

Insurable earnings capped at BBD 5,360: employee NIS 11% = BBD 589.60, employer 12.75% = BBD 683.40. Resilience and Regeneration Fund 0.25% of BBD 6,000 = BBD 15.00 each. PAYE: taxable BBD 6,000 - BBD 2,083.33 = BBD 3,916.67, all within the monthly lower band of BBD 4,166.67; the PAYE on it waits for the 2026 band rates (see Not yet confirmed).

```oa-check
name: BB 2026 monthly payroll, gross 6000
inputs:
  gross: 6000
  ceiling: 5360
  allowance_month: 2083.33
steps:
  - nis_employee: min(gross, ceiling) * 0.11
  - nis_employer: min(gross, ceiling) * 0.1275
  - rrf_each: gross * 0.0025
  - taxable: gross - allowance_month
expected:
  nis_employee: 589.60
  nis_employer: 683.40
  rrf_each: 15
  taxable: 3916.67
```

### Example 2: Employee over pensionable age or regular employee, same pay

For a category E employee (over pensionable age) on BBD 6,000 the employer pays 1.25% x BBD 5,360 = BBD 67.00 instead of BBD 683.40, and the employee 0.50% = BBD 26.80 instead of BBD 589.60. The age category saves the employer BBD 616.40 a month.

```oa-check
name: BB 2026 NIS category R vs E, insurable 5360
inputs:
  insurable: 5360
steps:
  - employer_r: insurable * 0.1275
  - employer_e: insurable * 0.0125
  - employee_e: insurable * 0.005
  - employer_saving: employer_r - employer_e
expected:
  employer_r: 683.40
  employer_e: 67
  employee_e: 26.80
  employer_saving: 616.40
```

## Ask the client first

1. Category of each worker (private sector R, apprentice, over pensionable age or under 16)?
2. Pay frequency and gross pay, including taxable allowances and bonuses.
3. Each employee's tax code and TIN.
4. Was each month's PAYE paid by the 15th?
5. Any non-resident or seconded staff?

## Sources

| Source | URL | Read on |
|---|---|---|
| NIS, contribution rates and earnings ceilings (via Firecrawl): read for categories R, E, P, T, A, S and the Resilience and Regeneration Fund | https://www.nis.gov.bb/contribution-rates/ | 2026-11-14 |
| NIS, increase in earnings ceiling 2026 (via Firecrawl): read in full | https://www.nis.gov.bb/increase-in-earnings-ceiling-2026/ | 2026-11-14 |
| BRA, guide to PAYE: read for the threshold, tax codes, basic salary and remittance date | https://bra.gov.bb/Popular-Topics/Employing-People/Guide-to-PAYE | 2026-11-14 |
| BRA, Policy Note OGC No. 001/2026: read for the 2026 rates and the monthly worked example | https://bra.gov.bb/attachment?file=Attachments%2FPolicy+Note+2026_Reduction+in+Personal+Income+Tax+Rates_April+2026.pdf&name=Policy+Note+2026_Reduction+in+Personal+Income+Tax+Rates_April+2026 | 2026-11-14 |
| BRA, Income Tax Act legislation page: read for the list of amending Acts (latest 2025-30; no 2026 amending Act listed) | https://bra.gov.bb/About/Legislation-Regulations/Income-Tax-Act | 2026-11-14 |
| Parliament of Barbados, bills and resolutions list: read for 2026 bills (no Income Tax (Amendment) Bill or Act, 2026 listed) | https://www.barbadosparliament.com/bills/ | 2026-11-14 |
| Provisional Collection of Taxes Act, Cap. 85: read for s. 3 (provisional effect of a new tax or rate increase in budget proposals) | https://bra.gov.bb/attachment?file=Attachments%2fProvisional+Collection+of+Taxes+Act%2c+Cap.+85.pdf&name=Provisional+Collection+of+Taxes+Act%2c+Cap.+85 | 2026-11-14 |

Not yet confirmed: the 2026 personal income tax rates: BRA's Policy Note OGC No. 001/2026 says BRA applies 11.5% (taxable income to BBD 50,000) and 27.5% (above) from income year 2026, down from 12.5% and 28.5%, following the 16 March 2026 budget, but no Income Tax (Amendment) Act, 2026 appears on BRA's Income Tax Act legislation page or on Parliament's bills list (both read 14 Nov 2026), and the Provisional Collection of Taxes Act, Cap. 85, s. 3 gives provisional effect only to a new tax or a rate increase, not a cut; the earlier 12.5% and 28.5% rates were not found in an enactment read for this version either, so confirm the rates with BRA before computing or filing; the NIS payment due date (earlier version: 15th of the following month); penalties and interest on late PAYE and NIS; the NIS age range of 16 to 67 in the earlier version; the 2027 ceiling announced by NIS (not read).
