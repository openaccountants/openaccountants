---
name: sh-paye-compliance
description: >
  Saint Helena island employer PAYE compliance for tax year 2026 (1 April 2026 to 31 March 2027). Covers employer registration (P1), tax codes and Free Pay Tables, deductions (P2), remittance and monthly return (P6) by the 15th, annual return (P7) by 30 April, certificates (P5), leavers (P8), the under-£300 small employer rule, records and penalties. Use for payroll, PAYE or employer questions on St Helena. Does not apply to Ascension or Tristan da Cunha.
version: 0.3
jurisdiction: SH
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Saint Helena island: employer PAYE compliance v0.3

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. It covers Saint Helena island only, not Ascension or Tristan da Cunha, which have separate laws.

## Who this applies to

Anyone who pays or becomes liable to pay employment income on Saint Helena island. There is no social contribution to run alongside PAYE: the Social Security Ordinance charges none (see the [pack README](README.md)). Employer duties are distinct from employees' return rules under ss.37 to 39.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Register employer | Within 30 days after the last day of the month of first payment or liability; address change or cessation within 30 days (Regulation 4) | 2026 | https://www.sainthelena.gov.sh/documents/Income-Tax-Ord-Updated-011021 |
| Remit PAYE | By the 15th of the month after deduction (Regulation 8) | 2026 | same |
| Monthly statement, P6 | Within 15 days of month end (Regulation 13) | 2026 | https://www.sainthelena.gov.sh/public-services/income-tax/ |
| Annual statement, P7 | Within one month of tax-year end, normally 30 April; within 15 days after cessation if employment ceased; or further time allowed (Regulation 14) | 2026 | https://www.sainthelena.gov.sh/documents/Income-Tax-Ord-Updated-011021 |
| Employee certificate, P5 | Within one month of tax-year end for continuing employment; on cessation date if employment ends; within a month if the employer ceases (Regulation 10(3)) | 2026 | same |
| Small employer | Annual liability less than £300: pay and file by the 15th day after months 3, 6, 9 and 12. Exactly £300 is outside. Nil liability may apply to file only the annual statement (Regulation 15) | 2026 | same |
| Records | 7 years from the end of the tax year (Regulation 12). Guide 13 says 6 years for P2 forms; the regulation wins | 2026 | same |
| Late statement | £100 plus £10 for each complete month (s.66) | 2026 | same |
| Late payment | 10% plus 1% a month after the first month (s.67) | 2026 | same |
| Offence | Fine of £500 or 6 months, or both (Regulation 16) | 2026 | same |

## The base

Deduct using the Commissioner's PAYE Tax Tables and the employee's code (Regulations 5, 6). Do not replace this with an annual figure divided by twelve. With more than one employer, the Commissioner directs the deduction. A variation under Regulation 7 needs approval or a notice. An agreement to pay free of tax is void, and the payment is treated as net (Regulation 9).

Taxable pay includes salary, wages, fees, leave pay, overtime, monetary allowances, bonus, commission, gratuities, pensions, redundancy pay and benefits in kind. Uniform or protective clothing and mileage allowance are excluded (Tax Guide 13).

Codes: NT means no tax; 0 means no free pay. The emergency code is 0 on a Week 1 or Month 1 basis, used if there is no code or no P8 Parts 2 and 3. Only the Tax Office changes a code, by form P3; the employer must act on it even if the employee disputes it. A one-off casual job uses code 0 on a week 1 basis if the office was not contacted (Tax Guide 13).

## Deadlines and filing

Starting:
1. Contact the Income Tax Office (PAYE Officer, 25880) as soon as you plan to employ anyone, even casually.
2. Complete form P1.
3. Give each employee's name, address, date of birth, pay, start date and employment type.
4. Ask for P8 Parts 2 and 3 from any earlier employer that tax year. If there is none, ask the office for a code.

Every pay day:
1. Record pay and tax on the employee's P2.
2. Deduct or refund using the code and Free Pay Tables, which come from the office.
3. Give the employee the pay and tax particulars (Regulation 10(7)).

Every month: by the 15th, pay the tax and send the P6 showing gross pay, tax deducted and tax remitted.

Leavers: complete the P8, send Part 1 to the office immediately, and give Parts 2 and 3 to the employee. The certificate and cessation rules above apply; do not postpone every leaver document until April.

Before 1 April: the office sends code lists and forms. Start a fresh P2 for each employee.

Year end: issue P5s, and send the P7 by 30 April reconciling each employee's income and deductions to total payments. Keep P2s; do not send them unless asked (Tax Guide 13). The employer must account for any deficiency (Regulation 14(2)).

For the ordinary year, Regulation 15 dates fall in July, October, January and April. Nil payroll deductions do not remove reporting duties unless approval is given.

The P6 and P8 are on the [Income Tax page](https://www.sainthelena.gov.sh/public-services/income-tax/).

## Penalties and interest

Statements: £100 plus £10 for each complete month. There is no waiver and no extension route for an employer statement (Tax Guide 5). Payments: 10%, plus 1% a month. An employer that fails to deduct is personally liable for the tax, and can recover it from the employee (Regulation 11). A further amount applies under s.69 as if the undeducted tax were a shortfall. If tax was deducted and not remitted, no action is taken against the employee (Regulation 11(6)).

## Cross-border points

Employment exercised in Saint Helena is within scope even if paid elsewhere (s.2). Non-ordinarily resident or temporary employees declare their expected stay (Regulation 6(4)). See [residence](sh-individual-tax-residence.md).

## Two worked examples that recompute

Example 1: £150 PAYE for March, paid 20 May, after the 15 April due date (Tax Guide 5 uses these figures).

```oa-check
name: Late payment penalty
inputs:
  tax: 150
steps:
  - flat: tax * 0.10
  - monthly: tax * 0.01
  - penalty: flat + monthly
expected:
  flat: 15.00
  monthly: 1.50
  penalty: 16.50
```

Example 2: P2 ledgers show £900 deducted; payments show £850. The £50 is a shortfall. Do not reduce the deduction ledger to make totals agree.

```oa-check
name: Annual reconciliation
inputs:
  deducted: 900
  remitted: 850
steps:
  - deficiency: deducted - remitted
expected:
  deficiency: 50.00
```


## Ask the client first

- Number of employees, and pay frequency?
- First pay date, and is the employer registered?
- Annual PAYE under £300?
- Benefits in kind?
- Any leavers, second jobs or temporary residents?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Ordinance 2012 and Income Tax Regulations 2012, consolidation authoritative at 1 October 2021, read for the sections and regulations cited | https://www.sainthelena.gov.sh/documents/Income-Tax-Ord-Updated-011021 | 2026-11-01 |
| Income Tax Office page (rates, key dates, forms), read in full | https://www.sainthelena.gov.sh/public-services/income-tax/ | 2026-11-01 |
| Tax Guide 5, Penalties (April 2024), read in full | https://www.sainthelena.gov.sh/documents/Tax-Guide-No.-5-Guide-to-Penalties-that-Apply-Under-the-Income-Tax-Law | 2026-11-01 |
| Tax Guide 13, Employer's Guide to PAYE (dated March 2016 inside), read to the leaver and year-end sections | https://www.sainthelena.gov.sh/documents/Tax-Guide-No.-13-2020-Employers-Guide-to-PAYE | 2026-11-01 |
| Social Security Ordinance 2010, consolidated, searched for contributions; regulation 4 read | https://www.sainthelena.gov.sh/documents/20250708_Social-Security-Ordinance_CONSOLIDATED | 2026-11-01 |

Not yet confirmed: Any instrument after the 1 October 2021 consolidation: the Laws index, press pages and 2026 Income Tax Office page show no enacted change to these rates, and a full Gazette audit was not done. An authenticated current PAYE table: the office issues them and they are not published. Valuing benefits in kind. How payments are made (the guides give no method). The 2026/27 minimum wage (ExCo Memo 10/2026): outside this skill, not read.

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
