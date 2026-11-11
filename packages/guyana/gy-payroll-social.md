---
name: gy-payroll-social
description: "Guyana payroll for 2026: National Insurance Scheme (NIS) contributions and PAYE income tax withholding. Covers the 14% NIS contribution for employed persons (5.6% employee, 8.4% employer) on pay up to the insurable earnings ceiling of G$280,000 a month or G$64,615 a week, 12.5% for the self-employed and 9.3% for voluntary contributors, coverage from age 16 to 60, PAYE under the Income Tax Act, Cap. 81:01 with the 2026 personal allowance of G$1,680,000 a year (G$140,000 a month), the 25% and 35% rates, the child, overtime, second-job and insurance deductions, the primary employer rule, monthly Form 5 and payment within 14 days, annual Forms 2 and 7B slips, and penalties. Trigger on: Guyana payroll 2026, NIS contributions Guyana, NIS ceiling, PAYE Guyana, Form 5, Form 2, 7B slip, employer contributions Guyana. Out of scope: the employee's annual return in gy-income-tax, companies in gy-corporate-income-tax, NIS benefits."
version: 1.0
jurisdiction: GY
tax_year: 2026
last_updated: 2026-11-11
category: payroll
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
---

# Guyana: payroll, NIS contributions and PAYE (2026) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Which texts.** NIS contributions: the National Insurance Scheme's own statement of rates and ceiling ("Information on N.I.S Contributions", nis.org.gy), made under the National Insurance and Social Security Act, Cap. 36:01. The Act itself was not read for this version (see "Not yet confirmed"). PAYE: the Income Tax Act, Cap. 81:01 (ITA), GRA consolidation revised 1 April 2026, with the Fiscal Enactments (Amendment) Act 2026 (Act No. 3 of 2026), which applies the 2026 allowance and band from the year of income starting 1 January 2026, and the Deduction of Income Tax (Employment) Regulations in the same consolidation.

**Quick reference (2026).**

| Item | Figure |
|---|---|
| NIS, employed person | 14% of pay: 5.6% employee, 8.4% employer |
| NIS ceiling | G$280,000 a month or G$64,615 a week |
| NIS, self-employed / voluntary | 12.5% of declared income / 9.3% |
| PAYE free pay | G$140,000 a month (G$1,680,000 a year), primary employer only |
| PAYE rates | 25% up to G$280,000 a month of chargeable pay (G$3,360,000 a year), 35% above |
| PAYE paid to GRA | within 14 days after the end of the month, with Form 5 |

Related skills: the employee's annual return and all income tax deductions in [gy-income-tax](gy-income-tax.md); companies in [gy-corporate-income-tax](gy-corporate-income-tax.md).

## Who this applies to

- **Employers**: every person paying emoluments (salaries, wages, bonuses), including the Government, must deduct income tax from each payment (ITA s. 93(1); GRA, Do I Need to Submit PAYE). The employer also deducts the employee's NIS contribution and pays its own share (NIS).
- **NIS coverage**: compulsory for persons aged 16 to 60 in insurable employment. Employed persons outside that age range are covered for industrial benefits only. People who leave insurable employment before 60 can continue as voluntary contributors. Self-employed persons contribute but are not covered for industrial benefits (NIS, Information on Contributions).
- **Employees over 60**: NIS states that employee contributions stop at 60 and that the employer pays 1.5% to cover persons over 60 or under 16 for industrial benefits (NIS Mailbag, FAQ page).
- **Out of scope**: NIS benefits and pensions, the employee's own return, and special payroll regimes (Government pensions, gold and diamond miners).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| NIS, employed person, total | 14% of actual wage or salary, up to the ceiling | 2026 | https://www.nis.org.gy/information_on_contributions |
| NIS, employee share (deducted from pay) | 5.6% | 2026 | same |
| NIS, employer share | 8.4% | 2026 | same |
| NIS insurable earnings ceiling | G$280,000 a month; G$64,615 a week (in force since January 2020, stated as current) | 2026 | same; https://www.nis.org.gy/node/608 |
| NIS, self-employed | 12.5% of declared income | 2026 | https://www.nis.org.gy/information_on_contributions |
| NIS, voluntary contributor | 9.3% of insurable earnings from the last two years of employment | 2026 | same |
| NIS for employed persons over 60 or under 16 (industrial benefits only) | 1.5%, paid by the employer | 2026 | https://www.nis.org.gy/faq |
| PAYE personal allowance (free pay), ITA s. 20(1)(a) | G$1,680,000 a year or one third of total income, whichever is greater; G$140,000 for a full month | YI 2026 | https://officialegazette.gov.gy/publications/a09dd6c2-5a8b-429d-9dd6-c25a8b429d53 (Act No. 3 of 2026, s. 2(b)) |
| PAYE rate up to G$3,360,000 a year of chargeable income, ITA s. 36 | 25% | YI 2026 | same, s. 2(c) |
| PAYE rate above G$3,360,000 a year, ITA s. 36A | 35% | YI 2026 | same, s. 2(d) |
| Overtime deduction, ITA s. 20(1)(d) | up to G$50,000 a month (G$600,000 a year) of overtime pay | YI 2026 | https://www.gra.gov.gy/wp-content/uploads/2026/04/Income-Tax-Act-Revised-April-1-2026.pdf (s. 20(1)(d)) |
| Second-job deduction, ITA s. 20(1)(c) | up to G$50,000 a month (G$600,000 a year), given by the second employer | YI 2026 | same, s. 20(1)(c) |
| Child deduction, ITA s. 20(1)(b) | G$10,000 a month per child under 18 (G$120,000 a year), on the employee's Claim for Deduction in Respect of Child form | YI 2026 | same, s. 20(1)(b) |
| Medical and life insurance premiums, ITA s. 16(1)(l) | lower of premiums, 10% of income and G$600,000 a year | YI 2026 | same, s. 16(1)(l) |
| Employee NIS, ITA s. 16(1)(k) | deductible in computing chargeable pay | YI 2026 | same, s. 16(1)(k) |

**Monthly figures.** The law sets annual amounts and says the child, second-job and overtime deductions are apportioned to the earning period (s. 20(1)). G$140,000 and G$280,000 are the annual figures divided by 12. The GRA's PAYE Rates and Calculations page still shows the 2024 table (G$100,000 a month, 28% and 40%); the 2026 Act wins.

**Largest monthly NIS.** Employee: 5.6% of G$280,000 = G$15,680. Employer: 8.4% of G$280,000 = G$23,520. Total G$39,200.

## The base

**NIS** is charged on the actual wage or salary paid, up to the ceiling (NIS, Information on Contributions). Contributions run per contribution week, Monday 00:00 to Sunday 24:00 (NIS FAQ).

**PAYE, each pay period** (ITA s. 93; PAYE Return Guide v4.4 columns 11 to 25):
1. Salaries and wages (column 11) plus overtime (12).
2. Less the overtime deduction (14) and, for a secondary job only, the second-job deduction (13), to give adjusted salaries (15).
3. Add taxable allowances and board and lodging (16, 17) to give total income (19). Non-taxable allowances are reported (18) but not taxed; see gy-income-tax for the list.
4. Less the personal allowance (20), employee NIS (21), insurance premiums (22) and child deduction (23): total deductions (24).
5. Tax (25): 25% of chargeable pay up to the period's share of G$3,360,000, 35% above.

**Primary employer only.** The personal allowance is given only by the primary employer, not on each job (GRA, File a Return page). A second employer gives the second-job deduction instead, if the employee tells it about the primary job (GRA notice on 2025 deductions).

**Wrong deductions.** An employer who fails to deduct tax stays liable for it as if deducted (Regulations reg. 12). The employee squares the year in their own return, attaching the 7B slips (see gy-income-tax).

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| PAYE deducted in a month, with Form 5 (Return of Deductions of Tax by an Employer) | within 14 days after the end of the month | Regulations reg. 11(1), 13; GRA, File Your PAYE |
| Return of employees who stopped being paid in the month | 14th of the following month | Regulations reg. 10 |
| Annual Forms 2 (return of persons employed, with summary sheet and declaration) | yearly, in the year of assessment; date not confirmed | ITA s. 61(2); GRA, File Your PAYE |
| 7B emolument slip to each employee | after the year end, for the employee's 30 April 2027 return | GRA, 7B Generation |
| NIS contributions and schedule | monthly; due date not confirmed | NIS electronic schedule |

**How to file PAYE.**
1. Prepare the monthly file in the GRA's CSV format (PAYE Return Guide v4.4, Jan 2026), one row per employee, named `paye-[EmployerName]-[YYYY].csv`; the GRA's PAYE File Generator (from 2026) and File Format Validator (YA 2026) help.
2. Log in to GRA eServices at https://eservices.gra.gov.gy (or through a tax agent) and upload the file as the Form 5 for the month; one file per month.
3. Fix the errors the system reports and upload again; an email confirms a correct submission.
4. Pay the PAYE within 14 days after the month end.
5. After the year end, upload the Forms 2 file the same way, and issue 7B slips (the GRA's 7B Generator adds a QR code and emails them).

**How to file NIS.** Register on the NIS electronic schedule site (http://esched.nis.org.gy) with the employer registration number, fill the NIS Electronic Schedule 2026 spreadsheet, create the summary sheet online and attach the schedule. Self-employed persons can pay through Mobile Money Guyana (NIS, payments via MMG).

## Penalties and interest

- **PAYE not deducted, withheld or paid over**: an offence; the GRA states a penalty of 10% interest on the amount owed (GRA, PAYE Interest and Penalties). The employer remains liable for tax it failed to deduct (Regulations reg. 12).
- **Late payment of tax** generally: 2% a month or part of a month (ITA s. 99(1)), as for other income tax.
- **NIS late payment**: not confirmed.

## Cross-border points

- Pay for employment exercised in Guyana is taxable in Guyana wherever it is paid (ITA s. 6), so PAYE applies to foreign employers' staff working in Guyana where the employer pays emoluments in Guyana.
- Payments to non-resident individuals for personal services who are not employees are not PAYE; they fall under the 20% withholding tax (ITA s. 39(1)(b), s. 40(d)). See gy-income-tax.
- Treaty and social security agreement relief for NIS was not checked.

## Two worked examples that recompute

### Example 1: a monthly-paid employee with one child

Kemi is paid G$350,000 a month by her only employer. She has one child under 18 and has filed the child declaration.

- NIS: pay is above the ceiling, so 5.6% of 280,000 = G$15,680 from Kemi and 8.4% of 280,000 = G$23,520 from the employer.
- PAYE: 350,000 - 140,000 allowance - 15,680 NIS - 10,000 child = G$184,320 chargeable, all within the G$280,000 monthly band, so 25%: G$46,080.
- Net pay: 350,000 - 15,680 - 46,080 = G$288,240. Employer cost: 350,000 + 23,520 = G$373,520.
- The employer pays G$46,080 PAYE (Form 5) and G$39,200 NIS for the month.

```oa-check
name: GY payroll 2026, monthly G$350,000, one child
inputs:
  gross: 350000
  nis_ceiling: 280000
  free_pay: 140000
  child: 10000
  band: 280000
steps:
  - nis_employee: min(gross, nis_ceiling) * 0.056
  - nis_employer: min(gross, nis_ceiling) * 0.084
  - chargeable: gross - free_pay - nis_employee - child
  - paye: min(chargeable, band) * 0.25 + max(0, chargeable - band) * 0.35
  - net_pay: gross - nis_employee - paye
  - employer_cost: gross + nis_employer
  - total_nis: nis_employee + nis_employer
expected:
  nis_employee: 15680
  nis_employer: 23520
  chargeable: 184320
  paye: 46080
  net_pay: 288240
  employer_cost: 373520
  total_nis: 39200
```

### Example 2: overtime at the main job and a second job

Ravi's main employer pays him G$300,000 salary and G$80,000 overtime in June 2026. He also works evenings for a second employer for G$100,000 a month and has told it about his main job.

- Main job NIS: 5.6% of the G$280,000 ceiling = G$15,680 (on gross earnings of G$380,000).
- Main job PAYE: overtime deduction is the first G$50,000, so adjusted pay is 300,000 + 80,000 - 50,000 = G$330,000. Less G$140,000 allowance and G$15,680 NIS: G$174,320 chargeable, at 25% = G$43,580.
- Second job PAYE: no personal allowance (the main employer gives it), but the second-job deduction of G$50,000: 100,000 - 50,000 = G$50,000 at 25% = G$12,500. NIS on the second job is left out here (see "Not yet confirmed").

**Which employer gives what.** If Ravi wrongly let both employers give him the G$140,000 allowance, the second job would show no PAYE at all and he would owe the difference with his annual return. If he did not tell the second employer about his main job, it would give neither the allowance nor the second-job deduction, and PAYE would be G$25,000 that month, reclaimed only through his return.

```oa-check
name: GY payroll 2026, overtime deduction and second job
inputs:
  salary: 300000
  overtime: 80000
  second_job_pay: 100000
  nis_ceiling: 280000
  free_pay: 140000
  band: 280000
steps:
  - nis_main: min(salary + overtime, nis_ceiling) * 0.056
  - overtime_deduction: min(overtime, 50000)
  - adjusted_main: salary + overtime - overtime_deduction
  - chargeable_main: adjusted_main - free_pay - nis_main
  - paye_main: min(chargeable_main, band) * 0.25 + max(0, chargeable_main - band) * 0.35
  - second_job_deduction: min(second_job_pay, 50000)
  - paye_second: (second_job_pay - second_job_deduction) * 0.25
  - paye_second_no_notice: second_job_pay * 0.25
expected:
  nis_main: 15680
  overtime_deduction: 50000
  adjusted_main: 330000
  chargeable_main: 174320
  paye_main: 43580
  second_job_deduction: 50000
  paye_second: 12500
  paye_second_no_notice: 25000
```

## Ask the client first

1. How is each employee paid (daily, weekly, fortnightly, monthly), and is this their primary or second job?
2. Gross pay, overtime, taxable and non-taxable allowances for the period.
3. Children under 18 (child declaration form held?) and medical or life insurance premiums the employee pays.
4. Employee ages: anyone under 16 or over 60 (NIS)?
5. Is the employer registered with the GRA (TIN, eServices) and with NIS (employer registration number)?
6. For self-employed clients: declared income for NIS and how they pay it.

## Sources

| Source | URL | Read on |
|---|---|---|
| NIS, Information on N.I.S Contributions, read for the 14%, 5.6% and 8.4% rates, the G$280,000 / G$64,615 ceiling, 12.5% and 9.3%, ages 16 to 60, and the ceiling history | https://www.nis.org.gy/information_on_contributions | 2026-11-11 |
| NIS, Adjustments to Rates 2025, read for the ceiling in force from 1 January 2020 and the 2026 electronic schedule | https://www.nis.org.gy/node/608 | 2026-11-11 |
| NIS, FAQ (Mailbag), read for the 1.5% rate for persons over 60 or under 16 and the contribution week; its ceiling figure (G$256,800) is out of date | https://www.nis.org.gy/faq | 2026-11-11 |
| NIS, Self-Employed Contribution Payments via GTT Mobile Money, read for the payment route | https://www.nis.org.gy/node/1453 | 2026-11-11 |
| NIS, Electronic Schedule Submission site, read for the online submission steps | http://esched.nis.org.gy | 2026-11-11 |
| Fiscal Enactments (Amendment) Act 2026, Act No. 3 of 2026, Official Gazette (Extraordinary) 17 February 2026: s. 1(2) and s. 2(b) to (d); scanned PDF read in full by OCR | https://officialegazette.gov.gy/publications/a09dd6c2-5a8b-429d-9dd6-c25a8b429d53 | 2026-11-11 |
| Income Tax Act, Cap. 81:01, GRA consolidation revised 1 April 2026: s. 6, 16(1)(k),(l), 20, 36, 36A, 39, 40, 61, 93, 99; Deduction of Income Tax (Employment) Regulations reg. 10 to 13 | https://www.gra.gov.gy/wp-content/uploads/2026/04/Income-Tax-Act-Revised-April-1-2026.pdf | 2026-11-11 |
| GRA, PAYE Return Electronic Submission Guidelines v4.4 (Jan 2026), read for columns 1 to 31 and the file process | https://gra.gov.gy/storage/2026/05/PAYE-Return-Guide-v4.4.pdf | 2026-11-11 |
| GRA, File Your PAYE, read for Forms 2 and 5, eServices upload and the 14-day due date | https://gra.gov.gy/business/tax-operations-and-services/accounting-for-employees/file-your-paye/ | 2026-11-11 |
| GRA, 7B Generation, read for the 7B slip process | https://gra.gov.gy/business/tax-operations-and-services/accounting-for-employees/7b-generation/ | 2026-11-11 |
| GRA, PAYE Interest and Penalties, read for the 10% statement | https://gra.gov.gy/business/tax-operations-and-services/accounting-for-employees/interest-penalties/ | 2026-11-11 |
| GRA, PAYE Rates and Calculations, read for the PAYE table (still shows 2024 figures; superseded by the Act) | https://gra.gov.gy/business/tax-operations-and-services/accounting-for-employees/rates-calculations/ | 2026-11-11 |

Not yet confirmed: the National Insurance and Social Security Act, Cap. 36:01 and its contribution regulations were not read (the NIS rates come from the NIS's own pages); the due date for paying NIS contributions and NIS late payment penalties; whether the self-employed and voluntary rates are subject to the same ceiling; how the NIS ceiling applies to a person with two employers; the due date of the annual Forms 2 (s. 61(2) says "the prescribed day", not found); whether the one-third-of-income personal allowance is applied per pay period by employers; the regulation number for the 14-day PAYE rule (the GRA page says paragraph 12 of the regulations, the consolidation's regulation 11 carries the 14th-day payment rule).
