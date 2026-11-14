---
name: malta-payroll
description: Use this skill whenever asked about Malta payroll for employed persons in 2026. Trigger on phrases like Malta payroll, FSS deduction, employee SSC, Class 1 contributions, FS4, FS5, FS3, FS7, payslip Malta, net salary Malta, PAYE Malta, tax withholding Malta, employer SSC Malta, Maternity Leave Fund, COLA Malta, minimum wage Malta, overtime Malta, gross to net Malta, statutory bonus Malta. Covers payer registration, the FS4, the Final Settlement System (FSS) methods (Main cumulative formula or tables, Part-Time, 15% Overtime, 20% Other Emoluments), euro rounding and the 50% cap, the 2026 Class 1 categories and caps, the employer-only 0.3% Maternity Leave Fund, the 2026 minimum wage and EUR 4.66 cost-of-living increase, statutory bonuses and weekly allowances, leave rules that touch payroll, and the FS5, FS3 and FS7 deadlines and Schedule C additional tax. Income tax rate tables are in malta-income-tax.
version: "2.0"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Malta payroll 2026: FSS tax withholding, Class 1, Maternity Leave Fund, bonuses and the FS forms

## Scope

What a Maltese employer (the "payer") does for its employees (the "payees") for **emoluments paid in calendar 2026** (year of assessment 2027): register, withhold income tax under the Final Settlement System (FSS Rules, S.L. 372.14), pay Class 1 social security and the Maternity Leave Fund contribution (Social Security Act, Cap. 318), pay the minimum wage, the cost-of-living increase and the statutory bonuses, and file the FS5, FS3 and FS7.

The article 56(1) income tax rate tables that FSS applies (as replaced by Act III of 2026 from year of assessment 2027) live in [malta-income-tax](malta-income-tax.md) and are not restated here. Class 2 for the self-employed: [malta-ssc](malta-ssc.md).

**Not covered:** the employee's own return, part-time final tax and personal reliefs ([malta-income-tax](malta-income-tax.md)); fringe-benefit valuation; the expatriate regimes (from 1 January 2026 the Tax Treatment of Highly Skilled Individuals Rules, L.N. 20 of 2026); sector Regulation Orders beyond what is named.

Built from the law: not yet approved by an accountant.

## Ask the client first

1. Is the employer registered as an FSS payer? When did emoluments first start to accrue? How many **full-time payees** (ten or more makes the cumulative formula compulsory)?
2. For each employee: a completed **FS4**, with which status (single, married joint, parent, qualifying-child)? For a qualifying-child status: custody or maintenance, child's age, EU/EEA or long-term resident status, and if neither is EU/EEA, was the child born and resident in Malta?
3. Is this the employee's **main** source, registered **part-time** work, or **other** emoluments?
4. Date of birth (on or before 31 December 1961, or from 1 January 1962) and age (under 17, 17, 18+).
5. The **basic** weekly wage or weekly equivalent of the basic monthly salary, before overtime, bonuses, allowances, benefits in kind and commissions.
6. Overtime: managerial post? Basic weekly wage at or below EUR 375? Opted out of the 15% method? Any fringe benefits, net-pay deals, termination payments, late FS5s or missing forms?

## The method, step by step

1. **Register as a payer** "within fifteen days" of the first emoluments starting to accrue (FSS rule 4(1)); a buyer of a going concern with employees has the same duty.
2. **Collect the FS4** within seven days of a new source or a change (rule 3(1)). From 1 January 2026 the form is the one "publicly available on the appropriate website" (L.N. 176 of 2026). The payer files the original by the last working day of the following month (rule 3(3)).
3. **No FS4: deduct at the maximum rate** of art. 56(1), 35% (rule 3(2)); still file the form to the best of your knowledge (rule 3(4)).
4. **Pick the method** per payment (rule 6(1)): **Main** for the one source the FS4 names as main and local pensions (rule 7); **Part-Time** under art. 90A (rule 8); **Overtime** at 15 cents per euro (rule 7A); **Other Emoluments** at 20% (rule 9).
5. **Main tax**: the cumulative formula (Schedule B Part I) with the 2026 art. 56(1) table for the FS4 status. A payer with fewer than ten full-time payees may use the Commissioner's Main Tax Deduction Tables instead, never both in one year (rule 7(4)).
6. **Round**: "disregard any fraction of a euro being equal to or less than fifty cents, and round up to one euro any fraction of a euro exceeding fifty cents" (rule 6(3)).
7. **Cap** the deduction at 50% of the cash part of the pay, unless the payee consents or a listed exception applies (rule 11); termination payments are not capped (rule 34).
8. **Class 1** on the basic weekly wage: employee share, matching employer share, and the employer's Maternity Leave Fund contribution (Cap. 318 art. 7, Tenth Schedule; MTCA 2026 table).
9. **Pay statement** to each payee: gross pay by category (fringe benefits separately) and tax deducted (rule 19).
10. **Remit and file the FS5** by the last working day of the next month (rules 15, 20).
11. **Year end**: FS3 to each payee by 31 January; FS7 with the FS3 originals by 15 February (rules 21, 22).

Order matters: split out qualifying overtime and part-time pay before the Main formula, or they are taxed twice; compute Class 1 on basic pay only, or both sides are overcharged.

### The cumulative formula (FSS Schedule B)

| Step | Formula | Meaning |
|---|---|---|
| 1 | A = (E / C) x N | Projected annual emoluments: main emoluments to date (E) / current pay period (C) x periods in the year (N) |
| 2 | P | Projected annual tax: the art. 56(1) table for the FS4 status applied to A |
| 3 | D = (P / N) x C | Tax due to date |
| 4 | L = D - X | This period's deduction: tax due to date less tax already deducted (X); nil if negative |

The 2026 Main Tax Deduction Tables are published by the Commissioner, not in the law (see Not yet confirmed). The cumulative formula re-computes tax to date each period, so the Act III of 2026 tables (assented 10 March 2026) unwind any January and February difference.

**Parent with one qualifying child above EUR 60,000.** The Act sets the subtraction at EUR 10,270 (Cap. 123 art. 56(1)(b)(iv)); MTCA's 2026 table shows EUR 10,275. Follow [malta-income-tax](malta-income-tax.md) on which figure to use, and tell the employee the difference is EUR 5 a year.

**Who may use which status** (the payer applies the FS4; a wrong FS4 gives the employee a year-end bill): married tables need a resident couple taxed jointly (an EU/EEA national with a non-resident spouse may qualify where at least 90% of the couple's world income is from Malta); the parent table needs custody of, or maintenance for, a child not over 18, or not over 23 in full-time education; the qualifying-child tables add the EU/EEA or long-term resident test, or the child born and resident in Malta. Detail: [malta-income-tax](malta-income-tax.md).

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| No FS4 | Deduct at the art. 56(1) maximum rate (35%) | Until the default ends | FSS rule 3(2): https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 |
| Other Emoluments | 20% | Payee may direct higher; pensioners and full-time students may direct nil or lower; others need written approval | FSS rule 9: https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 |
| Qualifying overtime | 15 cents per euro, final | Rule 7A; not chargeable income, not creditable, not refundable | same |
| Overtime eligibility | Basic weekly wage not over EUR 375; not managerial; full-time employment registered with Jobsplus | Up to the lower of EUR 10,000 and hours x maxrate (twice the hourly equivalent of basic; hourly = basic / 40) | Tax on Overtime Rules, S.L. 123.200: https://legislation.mt/getpdf/62026ae5c9c73a144cfb58eb |
| Deduction cap | 50% of the cash part of the emoluments | Unless the payee consents or the listed exceptions apply; not on termination payments | FSS rule 11: https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 |
| Class 1, Category A (under 18) | EUR 6.62 employee and employer; Maternity EUR 0.20 | Basic weekly wage EUR 0.10 to EUR 229.44 | MTCA Class 1 rates 2026: https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 |
| Class 1, Category B (18+) | EUR 22.94 each, or 10% if the employee chooses; Maternity EUR 0.69 | Basic weekly wage EUR 0.10 to EUR 229.44 | same |
| Class 1, Category C, born by 31 December 1961 | 10% each; Maternity 0.3% | EUR 229.45 to EUR 490.38 | same |
| Class 1, Category D, born by 31 December 1961 | EUR 49.04 each; Maternity EUR 1.47 | EUR 490.39 and over | same |
| Class 1, Category C, born from 1 January 1962 | 10% each; Maternity 0.3% | EUR 229.45 to EUR 559.30 | same |
| Class 1, Category D, born from 1 January 1962 | EUR 55.93 each; Maternity EUR 1.68 | EUR 559.31 and over | same |
| Class 1, Category E (students under 18) | 10%, maximum EUR 4.38 each; Maternity 0.3%, maximum EUR 0.13 | Qualifying student schemes | same |
| Class 1, Category F (students 18+) | 10%, maximum EUR 7.94 each; Maternity 0.3%, maximum EUR 0.24 | same | same |
| National minimum wage, 18+ | EUR 229.44 a week | From 1 January 2026; age 17 EUR 222.66; under 17 EUR 219.82 | L.N. 289 of 2025: https://legislation.mt/getpdf/696e2f8c52ff32215ce13d7b |
| Cost-of-living increase | EUR 4.66 a week | Whole-time employees from 1 January 2026; part-time pro rata | L.N. 290 of 2025: https://legislation.mt/getpdf/696e3268cc8c701d50c97020 |
| Statutory bonus | EUR 135.10 end of June and 15 to 23 December | Part bonus EUR 0.74 per calendar day | DIER: https://dier.gov.mt/en/services/employment-conditions/wages/bonus-and-weekly-allowances/ |
| Weekly allowance (income supplement) | EUR 121.16 end of March and end of September | Part allowance EUR 4.66 per working week or proportion | same |
| Annual leave | Four weeks and thirty-two hours on a forty-hour week (192 hours) | Plus a day for each public holiday on a rest day | S.L. 452.87 reg. 8: https://legislation.mt/getpdf/67516323b52f3e3cf890a2e0 |
| Maximum average working time | 48 hours per seven days, including overtime | Seventeen-week reference period by default | S.L. 452.87 reg. 7: https://legislation.mt/getpdf/67516323b52f3e3cf890a2e0 |
| Maternity leave | Eighteen weeks uninterrupted | From 1 January 2013 | S.L. 452.91 reg. 6: https://legislation.mt/getpdf/6022592fbc8272018c0edf9a |
| FSS additional tax, FS4 not submitted | EUR 2 per form, or EUR 23 where a month's defaults do not exceed ten | Maximum EUR 1,000 per default | FSS Schedule C: https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 |
| FSS additional tax, failure to register | EUR 115 | same | same |
| FSS additional tax, FS5 late or wrong manner | EUR 15 | same | same |
| FSS additional tax, FS7 with FS3s not filed | EUR 200 | same; doubles on each further notice up to the cap | same |

### Class 1 and the Maternity Leave Fund: the rules

- "Three contributions per week shall be payable ... one by the employed person, one by his employer, and one out of the Consolidated Fund" (Cap. 318 art. 7(1)); the State adds 50% of the combined contribution. The employer is liable for both shares in the first instance (art. 8(1)) and recovers the employee's share only from that week's wages (art. 8(3)). Deducting its own share from the employee "shall be guilty of an offence" (art. 8(2)).
- **Base**: the basic weekly wage, "excluding any remuneration for overtime, any form of bonus, any extra allowances, any remuneration in kind and commissions" (art. 2). Two insurable jobs: the one with the higher basic wage (art. 7(1) proviso). Percentages to the nearest cent.
- **Low earners**: a part-time employee whose part-time basic earnings do not exceed the National Minimum Wage may pay 10% instead of the Category B flat rate (from 1 January 2018); paying less may reduce contributory benefits. From 1 January 2022 a person with more than one part-time job and no full-time job may pay on all part-time jobs up to forty hours a week (art. 7(2)(a)).
- **Change of employer mid-week**: the former employer pays that week (art. 7(3)).
- **Maternity Leave Fund**: employer only, "0.3% calculated to the nearest cent of their basic weekly wage", flat at the bottom and capped at Category D. Nothing is deducted from the employee.
- **Late Class 1**: from 1 January 2026 the further contribution under art. 116(1)(c) and (d) is replaced by interest at the ITMA art. 44(2A) rate (0.6% a month or part).

### Minimum wage, cost of living and bonuses

- Part-timers get the hourly rate of a comparable whole-timer under the Wage Regulation Order; with none, at least the weekly minimum "divided by forty (40)" (EUR 5.736 an hour at 18+). Sector Order wages for 2026 may not be below 2025 wages plus the cost-of-living increase.
- The EUR 4.66 increase is part of wages: taxable under FSS and part of the basic weekly wage for Class 1. It is not the bonus.
- **Statutory bonuses** to every whole-time employee "between the 15th and the 30th day of the month of June and between the 15th and 23rd day of the month of December", each not less than half the Government's announced amount (Cap. 452 art. 23(1)). **Income supplements** are a separate duty "in the amount and at the times as may be established by legal notice". Under a year's service: proportionate "on the basis of the annual hours worked"; reduced-hours whole-timers pro rata (art. 24).
- An earlier version called the sum of bonuses and supplements a quarterly tax-free "COLA": wrong. Bonuses and supplements go through FSS; any exemption is not confirmed. They are excluded from the Class 1 base.

## Boundary and exception table

| Situation | Rule | Source |
|---|---|---|
| No FS4 | 35% until the default ends; payer still files the form | FSS rule 3(2), (4), (5) |
| FS4 unacceptable, not corrected within fourteen days | Maximum rate until the Commissioner directs otherwise | Rule 3(7) |
| Payer files an FS4 late, incomplete or wrong | Schedule C additional tax, plus liability for under-deduction not recovered by 31 December | Rule 3(6) |
| Ten or more full-time payees | Cumulative formula compulsory; fewer may use Tables, not both in a year | Rule 7(4) |
| More than one employment | One main source; others at 20% | Rules 7(1), 9 |
| Deduction above 50% of cash pay | Limited to 50% unless consent or ITA art. 71 or ITMA art. 46 | Rule 11(1) |
| Termination payment | Rule 6 and/or rule 10, no 50% limit | Rule 34 |
| Employer pays the employee's tax | Gross up: emoluments = net pay + tax | Rule 33 |
| Agreement not to deduct | Void (except rule 33) | Rule 36 |
| Payer failed to deduct but paid the tax | Recover only that amount, as the Commissioner approves | Rule 16 |
| Over-deduction remitted | Repay the payee, then set off or claim a refund | Rule 17 |
| Basic over EUR 375 or managerial | Overtime taxed under Main | S.L. 123.200 rule 2 |
| Payment after death or after the contract ended | Deduction rules still apply | Rule 12 |
| Employer recovers its own Class 1 share | Offence | Cap. 318 art. 8(2) |

## Worked cases

All employees are invented; the income tax bands used are the 2026 single and married tables in [malta-income-tax](malta-income-tax.md) ([MTCA 2026 rates](https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026): single 25% less EUR 3,400; married 25% less EUR 4,550, both from the 25% band to EUR 60,000).

### Case 1: single employee, cumulative formula, two months

Basic salary EUR 2,500 a month, FS4 single, twelve periods. Month 1: A = EUR 30,000; P = EUR 30,000 x 25% less EUR 3,400 = EUR 4,100; D = EUR 341.67, rounded up to EUR 342. Month 2: D = EUR 683.33; L = EUR 341.33, rounded down to EUR 341. With a married joint FS4, P = EUR 2,950 and month 1 is EUR 246: the status saves EUR 1,150 a year.

```oa-check
name: Single FSS cumulative formula, EUR 2,500 a month, two months with euro rounding (2026)
inputs:
  salary: 2500
steps:
  - annual_tax: salary * 12 * 0.25 - 3400
  - month_one: ceil(annual_tax / 12)
  - month_two: floor(annual_tax / 12 * 2 - month_one)
  - married_annual: salary * 12 * 0.25 - 4550
  - status_saving: annual_tax - married_annual
expected:
  annual_tax: 4100
  month_one: 342
  month_two: 341
  married_annual: 2950
  status_saving: 1150
```

### Case 2: Class 1 above the cap, born from 1962

Weekly basic EUR 700, born 1985: Category D. Employee EUR 55.93; employer EUR 55.93; Maternity EUR 1.68 (0.3% would be EUR 2.10). Employer cost on top of wages EUR 57.61 a week. At EUR 400 basic (Category C) the figures are EUR 40.00, EUR 40.00 and EUR 1.20.

```oa-check
name: Class 1 2026, born from 1962, weekly basic EUR 700 above the cap
inputs:
  weekly_basic: 700
steps:
  - employee: min(weekly_basic * 0.10, 55.93)
  - employer: min(weekly_basic * 0.10, 55.93)
  - maternity: min(weekly_basic * 0.003, 1.68)
  - employer_extra: employer + maternity
expected:
  employee: 55.93
  employer: 55.93
  maternity: 1.68
  employer_extra: 57.61
```

### Further cases (prose)

- **No FS4.** EUR 2,500 a month: 35% = EUR 875, under the 50% cap (EUR 1,250).
- **Qualifying overtime.** Basic EUR 360 a week, non-managerial, Jobsplus-registered; 40 overtime hours at EUR 13.50 = EUR 540. Hourly basic EUR 9.00, maxrate cap EUR 18.00: within it. 15% = EUR 81.00 final, reported separately on the FS5 and FS3, kept out of the Main formula.
- **Second job.** EUR 1,000 in a month as Other Emoluments: 20% = EUR 200, unless a higher or (pensioner, student) lower rate was directed.

## When to refuse or refer

- The employee's own return, part-time final tax, reliefs, disputed child conditions: [malta-income-tax](malta-income-tax.md) or a warranted accountant.
- Expatriate regimes (L.N. 20 of 2026), cross-border workers, posted workers (A1), directors' fees.
- Do not extrapolate caps, bonuses or tables to another year; the Main Tax Deduction Tables, sector terms and form layouts need the year's official publication.
- Refuse any arrangement not to deduct FSS tax (rule 36).
- Sector pay rates, overtime premiums and other leave: the applicable (Conditions of Work) Regulation Order and DIER.

## Filing and payment

| What | Who gets it | Deadline | Rule |
|---|---|---|---|
| Payer registration | Commissioner | Within fifteen days of first emoluments accruing | 4(1) |
| FS4 | Payee to payer; payer files the original | Payee within seven days; payer by the last working day of the following month | 3(1), 3(3) |
| FS5 with the tax deducted (nil advices too) | Commissioner | Last working day of the month after payment | 15(1), 20 |
| FS3 | Payee (two copies) | 31 January of the following year, or within seven days of termination | 21(1)(b) |
| FS7 with the FS3 originals | Commissioner | 15 February of the following year | 22(1) |
| FS7 when the payer stops paying emoluments | Commissioner | Last working day of the month after the last payment | 22(1) proviso |

The FS5 shows payees, gross emoluments split into part-time, qualifying overtime and other, fringe benefits separately, and tax by method plus rule 10 arrears. Class 1 is paid monthly in arrears as the Director determines (Cap. 318 art. 9). Tax deducted is a debt to Government from the last working day of the following month; late payment carries ITMA art. 44(2A) interest (rule 25(1)). Schedule C defaults: the payer rectifies and pays "within ten days" of the notice, may contest within ten days, and each further notice doubles the charge up to EUR 1,000 (rule 24). Keep a record per payee (name, address, ID or tax number, payment dates, gross pay with fringe benefits separate, tax monthly and cumulative) for the ITMA art. 23(12) period (rule 18).

**2025 year end.** The 2025 FS3s were due by 31 January 2026 and the FS7 by 15 February 2026; file any still outstanding. 2025 pay used the Act IX of 2025 tables, without the qualifying-child tables.

## Completion checklist

- [ ] Payer registered within fifteen days.
- [ ] FS4 for every payee, status checked; 35% where missing.
- [ ] Method per payment; formula or Tables, never mixed.
- [ ] 2026 art. 56(1) table from malta-income-tax; euro rounding and the 50% cap.
- [ ] Overtime tested (EUR 375, non-managerial, EUR 10,000 and maxrate) at 15%.
- [ ] Class 1 on basic only, 2026 MTCA categories; Maternity 0.3% with 2026 caps; employer share never recovered.
- [ ] Minimum wage and EUR 4.66 increase applied; bonuses and allowances scheduled.
- [ ] FS5 monthly; FS3 by 31 January; FS7 by 15 February.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read for FSS Rules, S.L. 372.14, rules 3, 4, 6, 7, 7A, 9, 11, 15, 16, 17, 18, 19, 20 to 22, 24, 25, 33, 34, 36, Schedules B and C | https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 | 2026-11-14 |
| Read for L.N. 176 of 2026 (FS4 published on the website) | https://legislation.mt/getpdf/6a6c4e3652fe433f00006353 | 2026-11-14 |
| Read for Tax on Overtime Rules, S.L. 123.200 (EUR 375, EUR 10,000, maxrate) | https://legislation.mt/getpdf/62026ae5c9c73a144cfb58eb | 2026-11-14 |
| Read for MTCA Class 1 rates 2026 (categories A to F, employee, employer, maternity) | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 | 2026-11-14 |
| Read for Cap. 318 arts 2, 7, 8, 9 and 116(1) proviso | https://legislation.mt/eli/cap/318/eng/pdf | 2026-11-14 |
| Read for Cap. 123 art. 56(1)(b)(iv) (EUR 10,270 in the Act) | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c | 2026-11-14 |
| Read for MTCA Tax Rates 2026 (single and married bands used in Case 1; EUR 10,275 shown for parent with one child) | https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026 | 2026-11-14 |
| Read for L.N. 289 of 2025 (minimum wage 2026) | https://legislation.mt/getpdf/696e2f8c52ff32215ce13d7b | 2026-11-14 |
| Read for L.N. 290 of 2025 (EUR 4.66 cost-of-living increase) | https://legislation.mt/getpdf/696e3268cc8c701d50c97020 | 2026-11-14 |
| Read for Cap. 452 arts 23 and 24 (bonus windows, income supplements, pro rata) | https://legislation.mt/getpdf/69faf83e2eb86e24207539ec | 2026-11-14 |
| Read for DIER bonus and weekly allowance amounts (EUR 135.10, EUR 121.16, EUR 0.74, EUR 4.66) | https://dier.gov.mt/en/services/employment-conditions/wages/bonus-and-weekly-allowances/ | 2026-11-14 |
| Read for S.L. 452.87 regs 7 and 8 (48 hours, four weeks and thirty-two hours) | https://legislation.mt/getpdf/67516323b52f3e3cf890a2e0 | 2026-11-14 |
| Read for S.L. 452.91 reg. 6 (eighteen weeks maternity leave) | https://legislation.mt/getpdf/6022592fbc8272018c0edf9a | 2026-11-14 |

Not yet confirmed: the 2026 Main Tax Deduction Tables; MTCA's instruction for January and February 2026 before Act III of 2026; the monthly-to-weekly conversion MTCA prescribes for Class 1; how Class 1 shows on the FS5 and the FS5 layout; whether any bonus or supplement is tax-exempt; payslip rules under Cap. 452; the service supplements of S.L. 452.71 after L.N. 289 of 2025; part-time bonus entitlement; the maternity pay split and 2026 benefit rate; the electronic filing threshold for FS3s (MTCA reporting page not re-read).
