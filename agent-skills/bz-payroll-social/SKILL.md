---
name: bz-payroll-social
description: "Belize payroll for employers in tax year 2026, social security contributions to the Social Security Board (SSB) and income tax withheld under PAYE. Contributions are a fixed weekly amount by wage band, 10% in total of insurable earnings up to the BZD 520 weekly wage ceiling, split between employer and employee, paid by the employer within fourteen days after the month. Covers who is covered (ages 14 to 65), the full 2022 contribution schedule still in force, the employment-injury-only contribution for older workers, insurable earnings, PAYE at 25% after the BZD 20,000 basic deduction and the employer's remittance forms. Trigger phrases include Belize social security, SSB contributions, Belize payroll, Belize PAYE and Belize wage ceiling."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bz-payroll-social"
  jurisdiction: "BZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Belize payroll and social security v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** A Belize employer pays Social Security Board contributions for every employee aged 14 to 65 who works eight hours or more in a contribution week (Monday to Sunday). The weekly contribution is a fixed amount by wage band, **10% of insurable earnings in total**, up to a **weekly wage ceiling of BZD 520** (BZD 23.40 employee and BZD 28.60 employer at the top band), under the schedule effective **4 April 2022**. The employer pays the whole amount, deducting the employee's share from pay, **no later than fourteen days after the end of the month**. Income tax on wages is withheld under PAYE at 25% of chargeable income: see [bz-income-tax](bz-income-tax.md). Tax year: calendar year 2026. Currency: BZD.

## Who this applies to

- **Employers** of employees aged 14 to 65, for each contribution week in which the employee works eight hours or more ([SSB contributions page](https://www.socialsecurity.org.bz/contributions/)).
- **Employees aged 60 to 64 who have received or are receiving a Social Security benefit, and all persons 65 and older:** only the employer's BZD 2.60 weekly employment-injury contribution is paid ([SSB Contribution and Benefit Schedule, note (A) and (B)](https://socialsecurity.org.bz/wp-content/uploads/2022/03/Cont_Ben_Schedule.jpg)).
- **Self-employed persons and voluntary contributors** have their own SSB arrangements (out of scope; see the SSB self-employed pages).
- **Not in this skill:** business tax of the employer ([bz-corporate-income-tax](bz-corporate-income-tax.md)).

## Rates, bands and thresholds

Weekly contributions by wage band, SSB Contribution and Benefit Schedule effective Monday 4 April 2022 (still the schedule SSB publishes on its contributions page in November 2026). Total contribution is 10% of the weekly insurable earnings in every band.

| Weekly earnings (BZD) | Weekly insurable earnings | Employee | Employer | Total | Source |
|---|---|---|---|---|---|
| Under 70.00 | 55.00 | 1.03 | 4.47 | 5.50 | [SSB Contribution and Benefit Schedule](https://socialsecurity.org.bz/wp-content/uploads/2022/03/Cont_Ben_Schedule.jpg) |
| 70.00 to 109.99 | 90.00 | 1.69 | 7.31 | 9.00 | same |
| 110.00 to 139.99 | 130.00 | 2.44 | 10.56 | 13.00 | same |
| 140.00 to 179.99 | 160.00 | 3.94 | 12.06 | 16.00 | same |
| 180.00 to 219.99 | 200.00 | 5.94 | 14.06 | 20.00 | same |
| 220.00 to 259.99 | 240.00 | 7.94 | 16.06 | 24.00 | same |
| 260.00 to 299.99 | 280.00 | 9.94 | 18.06 | 28.00 | same |
| 300.00 to 339.99 | 320.00 | 11.94 | 20.06 | 32.00 | same |
| 340.00 to 379.99 | 360.00 | 13.98 | 22.02 | 36.00 | same |
| 380.00 to 419.99 | 400.00 | 16.15 | 23.85 | 40.00 | same |
| 420.00 to 459.99 | 440.00 | 18.45 | 25.55 | 44.00 | same |
| 460.00 to 499.99 | 480.00 | 20.86 | 27.14 | 48.00 | same |
| 500.00 and over | 520.00 (wage ceiling) | 23.40 | 28.60 | 52.00 | same |
| Ages 60 to 64 already receiving a benefit, and 65 and over | n/a | 0.00 | 2.60 | 2.60 (employment injury only) | same |
| Total contribution rate and wage ceiling history | 10% and BZD 520 a week from 4 April 2022 (9% and BZD 480 from 6 January 2020; 8.5% and BZD 440 from 1 July 2019) | | | | [SSB 2019 contribution reform page](https://socialsecurity.org.bz/2019-contribution-reform/) |
| Payment deadline | No later than fourteen days after the end of the month; if the 14th is a weekend or holiday, the first working day after | | | | [SSB contributions page](https://www.socialsecurity.org.bz/contributions/) |
| PAYE rate | 25% of chargeable income; BZD 20,000 basic deduction above BZD 29,000 of total income | | | | [Act No. 40 of 2024, s.3 and s.4](https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf) |

## The base

1. **Contribution week:** Monday to Sunday. A contribution is due for any week with eight hours or more of work. The contribution year runs from the first Monday of the calendar year (52 or 53 weeks).
2. **Insurable earnings** are gross earnings, including overtime, cost of living bonus, dependants' allowances, long-service and efficiency supplements, production bonuses, service charges, commissions, gratuities other than once-a-year ones, dirty or dangerous work pay, shift and night pay, free-meal deductions, tax paid by the employer for the employee, and holiday pay (Social Security (Collection of Contributions) Regulations 1980, as SSB lists them) ([SSB contributions page](https://www.socialsecurity.org.bz/contributions/)).
3. **Find the band** for the employee's actual weekly earnings, then take the fixed employee and employer amounts from the schedule. Earnings above BZD 500 a week sit in the top band (insurable BZD 520).
4. **Deduct the employee share** from pay at the time of payment for that period only; recovering the employer's share from the employee is an offence. Give the employee a monthly receipt or payslip showing the deduction.
5. **No contribution** for a week with no work and no pay, or a week credited for sickness or maternity benefit. Contributions are due for paid holidays. Pay in lieu of notice creates no contribution after employment ends.
6. **PAYE:** compute each employee's income tax per [bz-income-tax](bz-income-tax.md), deduct from emoluments and remit to BTS with form BTS200 (monthly remittance of income tax withheld). An employer who fails to deduct and remit is liable for the amount ([Cap. 55, PAYE provisions](https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf)).

## Deadlines and filing

| Step | What to do | Source |
|---|---|---|
| Register as employer | Register with SSB as an employer and with BTS for a TIN on IRIS Belize | [SSB contributions page](https://www.socialsecurity.org.bz/contributions/); [BTS registration guide](https://bts.gov.bz/guide/registration) |
| Monthly SSB payment | Pay the total contributions for all employees, with a complete Contribution Statement (FIN15A) showing each employee's social security number, no later than fourteen days after the month | [SSB contributions page](https://www.socialsecurity.org.bz/contributions/) |
| Register of employees | Keep each employee's name, address, social security number, start and end dates, each payment of earnings and each weekly deduction; SSB may inspect | same |
| PAYE | Remit income tax withheld to BTS with BTS200; employees with only emoluments need not file BTS203 unless claiming a refund or asked to | [BTS tax resources](https://bts.gov.bz/tax_resources); [Cap. 55 s.31(2)](https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf) |
| Refunds of contributions | Paid in error: apply within two years after the contribution year; paid by two or more employers for the same week: within twelve months (form DP7) | [SSB contributions page](https://www.socialsecurity.org.bz/contributions/) |

## Penalties and interest

- SSB charges interest on unpaid or late contributions when the employer fails to pay within the prescribed time ([SSB contributions page](https://www.socialsecurity.org.bz/contributions/)). The rate was not stated on the page read.
- PAYE: late income tax bears 1.5% a month (Cap. 55 s.55(a)).

## Cross-border points

- Contributions are due for every employee in Belize aged 14 to 65 working eight hours or more a week; the SSB page read makes no exception for foreign nationals.
- Employment income derived from a trade, business or profession outside Belize is outside Belize income tax (Cap. 55 s.6(4) as replaced in 2024).

## Two worked examples that recompute

**Example 1: employee earning BZD 600 a week (simple).** Earnings are above BZD 500, so the top band applies: insurable earnings BZD 520, employee BZD 23.40, employer BZD 28.60, total BZD 52.00 a week. Over a four-week month the employer pays SSB BZD 208.00, of which BZD 93.60 is deducted from the employee.

```oa-check
name: Belize SSB, top band, four weeks
inputs:
  employee_weekly: 23.40
  employer_weekly: 28.60
  weeks: 4
  insurable: 520
steps:
  - total_weekly: employee_weekly + employer_weekly
  - total_rate_check: total_weekly / insurable
  - employee_month: employee_weekly * weeks
  - employer_month: employer_weekly * weeks
  - month_total: employee_month + employer_month
expected:
  total_weekly: 52.00
  total_rate_check: 0.10
  employee_month: 93.60
  employer_month: 114.40
  month_total: 208.00
```

**Example 2: part-time employee, and a worker aged 66 (edge case).** A part-timer earns BZD 150 a week: band 140.00 to 179.99, insurable BZD 160, employee BZD 3.94, employer BZD 12.06, total BZD 16.00. A worker aged 66 on the same payroll costs the employer only the BZD 2.60 employment-injury contribution and nothing is deducted from pay. For four weeks the employer pays BZD 64.00 for the part-timer and BZD 10.40 for the older worker.

```oa-check
name: Belize SSB, low band and over-65 worker
inputs:
  pt_employee: 3.94
  pt_employer: 12.06
  over65_employer: 2.60
  weeks: 4
steps:
  - pt_weekly_total: pt_employee + pt_employer
  - pt_month: pt_weekly_total * weeks
  - over65_month: over65_employer * weeks
  - payroll_ssb_total: pt_month + over65_month
expected:
  pt_weekly_total: 16.00
  pt_month: 64.00
  over65_month: 10.40
  payroll_ssb_total: 74.40
```

## Ask the client first

1. Each employee's weekly gross earnings (all the items counted as insurable earnings).
2. Each employee's age, and whether anyone aged 60 to 64 already receives an SSB benefit.
3. Hours worked each week (eight hours or more triggers a contribution).
4. Is the employer registered with SSB and with BTS, and are FIN15A statements and BTS200 remittances up to date?
5. Each employee's total annual income for PAYE (see [bz-income-tax](bz-income-tax.md)).

## Sources

| Source | URL | Read on |
|---|---|---|
| SSB Contribution and Benefit Schedule effective 4 April 2022 (image published on the contributions page), read for every wage band, insurable earnings, employee, employer and total weekly contributions, percentages and the note on workers 60 to 64 and 65 and over | https://socialsecurity.org.bz/wp-content/uploads/2022/03/Cont_Ben_Schedule.jpg | 2026-11-14 |
| SSB contributions page, read for coverage (ages 14 to 65, eight hours a week), the lowest band example, deduction rules, the fourteen-day payment deadline, FIN15A, the employee register, insurable earnings, refunds and leave rules | https://www.socialsecurity.org.bz/contributions/ | 2026-11-14 |
| SSB 2019 contribution reform page, read for the rate and wage ceiling steps (8.5% and BZD 440, 9% and BZD 480, 10% and BZD 520 from 4 April 2022) | https://socialsecurity.org.bz/2019-contribution-reform/ | 2026-11-14 |
| Income and Business Tax (Amendment) Act No. 40 of 2024, read for the 25% rate and the BZD 29,000 and BZD 20,000 amounts used by PAYE | https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf | 2026-11-14 |
| Income and Business Tax Act, Cap. 55, Revised Edition 2011, read for the PAYE liability of employers, s.31(2) and s.55 | https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf | 2026-11-14 |
| BTS registration guide and tax resources page, read for TIN registration and the BTS200 and BTS203 forms | https://bts.gov.bz/tax_resources | 2026-11-14 |

Not yet confirmed: the interest rate SSB charges on late contributions; the PAYE remittance due date to BTS (the payment rules on the BTS site are a scanned image); whether any SSB schedule change took effect in 2025 or 2026 (none appears on the SSB pages read); the old file's statement that a move to a percentage-of-salary model has been proposed.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bz-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bz-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
