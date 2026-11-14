---
name: nc-payroll
description: "North Carolina employer payroll for 2026, state income tax withholding and state unemployment insurance. Covers withholding at 4.09% (the 3.99% 2026 rate plus 0.1%) under the NCDOR NC-30 percentage method, with the per-period standard deduction and $2,500 allowances, the 4.09% flat supplemental wage rate, Forms NC-4, NC-4 EZ and NC-4 NRA, quarterly, monthly or semiweekly deposits by average monthly withholding ($250 and $2,000 lines, G.S. 105-163.6), Form NC-3 and W-2s by January 31, 4% withholding from nonresident and ITIN contractors paid over $1,500, and NC unemployment insurance through DES (2026 taxable wage base $34,200, new employer rate 1%, experience rates 0.06% to 5.76%, quarterly reports due the last day of the month after the quarter). Trigger on \"North Carolina payroll\", \"NC withholding\", \"NC-30\", \"NC-4\", \"NC-5\", \"NC-3\", \"NC SUTA\", \"NC unemployment tax\", \"DES NCSUITS\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nc-payroll"
  jurisdiction: "US-NC"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# North Carolina payroll: withholding and unemployment insurance, 2026

> **Source-cited draft.** Built from the NCDOR 2026 NC-30 Income Tax Withholding Tables and Instructions for Employers (published 15 December 2025), G.S. 105-153.7, 105-163.1 and 105-163.6, and the NC Division of Employment Security (DES) pages on tax rates, liability and the quarterly tax and wage report, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, North Carolina withholding is figured at **4.09%** (the 3.99% income tax rate plus 0.1%) on wages after the per-period share of the NC standard deduction ($12,750 a year for single or married, $19,125 head of household) and $2,500 a year for each NC-4 allowance. Bonuses paid separately may be withheld at a flat **4.09%**. Unemployment insurance is paid by the employer only, to DES: **1%** for a new employer on the first **$34,200** of each employee's 2026 wages; experienced employers pay **0.06% to 5.76%**. Quarterly DES reports and NCDOR withholding returns are due by the last day of the month after each quarter (monthly withholding filers by the 15th).

## Scope and who this is for

In scope: an employer paying wages in North Carolina, or to NC residents working elsewhere, in 2026: NC income tax withholding, deposits and returns with NCDOR; withholding from nonresident and ITIN contractors; NC unemployment insurance with DES.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal income tax withholding, FICA, FUTA, Forms 941 and 940 | `us-form-941-940-payroll` |
| Other states' payroll rules | `us-state-payroll-matrix` |
| The employee's own NC return | `nc-income-tax` |
| 1099-NEC issuance | `us-1099-nec-issuance` |
| Wage and hour law, final pay, new hire reporting, leave | not covered in this rewrite; refer |

## Ask the client first

1. **Where each employee lives and works.** NC withholds from nonresidents for work in NC and from residents working outside NC (G.S. 105-163.1(4)).
2. **Each employee's NC-4, NC-4 EZ or NC-4 NRA** (federal W-4 does not count), pay frequency and filing status.
3. **Average NC income tax withheld per month** over the year. It sets the quarterly, monthly or semiweekly schedule.
4. **Payments to nonresident performers or entertainers, or to contractors with an ITIN or no valid TIN**, and how much each was paid in 2026.
5. **DES account number and 2026 rate notice (NCUI 104)**, or the date the first employee was hired.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Individual income tax rate for 2026 | 3.99% | [G.S. 105-153.7(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html) |
| Withholding rate used in the NC-30 formula (3.99% plus 0.1%) | 4.09% | [NCDOR NC-30 (2026), page 16](https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open) |
| Supplemental wages, flat method | 4.09% | [NCDOR NC-30 (2026), section 12](https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open) |
| Weekly standard deduction, single or married / head of household | $245.19 / $367.79 | [NCDOR NC-30 (2026), page 16](https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open) |
| Biweekly standard deduction, single or married / head of household | $490.38 / $735.58 | [NCDOR NC-30 (2026), page 16](https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open) |
| Semimonthly standard deduction, single or married / head of household | $531.25 / $796.88 | [NCDOR NC-30 (2026), page 17](https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open) |
| Monthly standard deduction, single or married / head of household | $1,062.50 / $1,593.75 | [NCDOR NC-30 (2026), page 17](https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open) |
| Value of one allowance, weekly | $48.08 | [NCDOR NC-30 (2026), page 16](https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open) |
| Quarterly withholding filer: average NC tax withheld per month under | $250 | [G.S. 105-163.6(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.6.html) |
| Monthly filer: average per month at least $250 and under | $2,000 | [G.S. 105-163.6(c)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.6.html) |
| Semiweekly payer: average per month at least | $2,000 | [G.S. 105-163.6(d)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.6.html) |
| Withholding from a nonresident contractor or ITIN contractor paid more than $1,500 in the year: rate on the compensation | 4% | [NCDOR NC-30 (2026), withholding from nonwage compensation](https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open) |
| UI taxable wage base, 2026 | $34,200 | [DES tax rate information](https://des.nc.gov/employers/tax-rate-information) |
| UI rate for a beginning employer | 1% | [DES tax rate information](https://des.nc.gov/employers/tax-rate-information) (G.S. 96-9.2(b)) |
| UI experience rate range, 2026 | 0.06% to 5.76% | [DES tax rate information](https://des.nc.gov/employers/tax-rate-information) (G.S. 96-9.2(c)) |
| UI base rate, 2026 (contribution rate is 1.9% minus the employer's reserve ratio percentage while the trust fund is above 1.25% of insured wages) | 1.9% | [DES tax rate information](https://des.nc.gov/employers/tax-rate-information) |
| UI surtax, only in a year the UI trust fund is under $1 billion | 20% of contributions | [DES tax rate information](https://des.nc.gov/employers/tax-rate-information) (G.S. 96-9.7(b)) |
| UI liability, general employer: quarterly wages of at least | $1,500 | [DES am I required to pay taxes](https://des.nc.gov/employers/am-i-required-pay-taxes) |

The 2025 wage base was $32,600; the new employer rate has been 1% since at least 2021 (DES table).

### Step 1: collect the certificate

When an employee is hired, get Form NC-4, NC-4 EZ or NC-4 NRA; federal certificates are not acceptable. An employee claiming exemption (for example a military spouse under the Servicemembers Civil Relief Act) must give a new NC-4 EZ each year; if none arrives by February 16, withhold as single with no allowances (NC-30, calendar of employer's duties).

### Step 2: withhold from each wage payment (percentage method)

For each pay period: wages, minus the period's standard deduction for the employee's status, minus allowances times the period value ($48.08 weekly, which is $2,500 a year), times **4.09%**, rounded to the nearest whole dollar. NC-30 also has wage bracket tables that give the same result.

**Supplemental wages** (bonuses, commissions) paid separately: withhold a flat 4.09%, or add them to the regular wages of the most recent period, compute as one payment and subtract what was already withheld. If no tax was withheld from regular wages, the aggregate method must be used. Vacation pay paid on its own is a regular wage payment (NC-30 section 12).

### Step 3: withhold from nonwage payments

A payer who pays more than **$1,500** in 2026 to a nonresident contractor (a nonresident person or entity performing in NC in connection with a performance, entertainment, athletic event, speech, or film, radio or television program), to an ITIN contractor, or to a payee who gives no valid TIN, withholds **4%** of the compensation (G.S. 105-163.1; NC-30).

### Step 4: deposit and file withholding

NCDOR assigns the schedule from the average withheld per month ([G.S. 105-163.6](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.6.html)):

| Average withheld per month | Return and payment |
| --- | --- |
| Under $250 | Quarterly return and payment, due the last day of the month after the quarter |
| $250 to under $2,000 | Monthly return and payment by the 15th of the next month; December's is due January 31 |
| $2,000 or more | Quarterly return, with payments semiweekly: paydays Wednesday to Friday pay by the next Wednesday; Saturday to Tuesday by the next Friday; one extra business day for each holiday in the three weekdays after the period |

Follow NCDOR's written direction until told to change. NCDOR may close an account with no withholding for 18 months.

### Step 5: year end

By **January 31, 2027**: give each employee Form W-2 and each payee Form NC-1099M (or federal 1099-MISC or 1099-NEC), and electronically file **Form NC-3**, Annual Withholding Reconciliation, with the State copies of the W-2s and 1099s. A business that closes files NC-3 by the last day of the month after the quarter it closed (NC-30, calendar of employer's duties).

### Step 6: unemployment insurance (DES)

1. Register in **NCSUITS** once liable (for a general employer: quarterly wages of $1,500 or more, or at least one worker in 20 different weeks in a year; also anyone liable for federal FUTA). DES issues an employer ID and a liability date ([DES](https://des.nc.gov/employers/am-i-required-pay-taxes)).
2. Pay the assigned rate (1% when new) on each employee's wages up to **$34,200** for 2026. UI tax is not deducted from wages.
3. File the **Quarterly Tax and Wage Report** for every quarter from the first quarter with employment, with each employee's name, SSN and wages, even if zero. Ten or more employee wage items must be filed online ([DES quarterly report](https://des.nc.gov/employers/file-adjust-or-review-quarterly-tax-wage-report)).
4. The rate notice (NCUI 104) arrives in the NCSUITS inbox each November or December; a protest must be made in writing before May 1 of the following year.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| NC resident working in another state | Still an "employee" for NC withholding (G.S. 105-163.1(4)); credit questions go to the employee's return |
| Nonresident working in NC | Withhold NC tax on wages for NC services |
| Nonresident employee doing disaster work for a critical infrastructure company during a disaster period | Not "wages" for NC withholding (G.S. 105-163.1(13)) |
| Military spouse meeting the three SCRA conditions with a current NC-4 EZ | No NC withholding; new NC-4 EZ each year |
| Nonresident alien employee | Form NC-4 NRA; NC-30 limits the extra withholding to 4.09% of wages at or below $245 weekly, $490 biweekly, $531 semimonthly or $1,062 monthly |
| Employee gives no certificate | Withhold as single with no allowances |
| Bonus paid with no regular withholding that period | Use the aggregate method, not the flat 4.09% |
| UI trust fund below $1 billion | 20% surtax on contributions; DES then certifies only 83.33% of the total paid for the FUTA credit |
| Ten or more employee wage items on the DES report | Must file online; a paper filer is charged $25 |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| No NC-4 on file | Single, no allowances |
| Filing schedule letter not seen | Use the average-withholding test and confirm with NCDOR |
| DES rate notice not seen for a new employer | 1% |

## Worked cases

### Case 1: weekly pay, a bonus and unemployment insurance

A single employee with no allowances earns $1,200 a week. Withholding: ($1,200 minus $245.19) × 4.09% = $39.05, rounded to **$39**. A separate $5,000 bonus with the flat method: **$204.50** (rounded on payment to $205). The employer is new to DES, at 1%, and the employee earns $62,400 in 2026: UI tax on $34,200 is **$342**.

```oa-check
name: NC 2026 weekly withholding, supplemental, UI
inputs:
  weekly_wages: 1200
  weekly_std: 245.19
  rate: 0.0409
  bonus: 5000
  annual_wages: 62400
  wage_base: 34200
  ui_rate: 0.01
steps:
  - weekly_tax: round((weekly_wages - weekly_std) * rate, 0)
  - bonus_tax: bonus * rate
  - ui: min(annual_wages, wage_base) * ui_rate
expected:
  weekly_tax: 39
  bonus_tax: 204.50
  ui: 342
```

### Case 2: which deposit schedule applies

A small employer withholds $18,000 of NC income tax across 2026: $1,500 a month on average. That is at least $250 and under $2,000, so it files and pays **monthly**, by the 15th of the next month (December's by January 31). If headcount doubles and average monthly withholding rises to $3,000, NCDOR moves it to **semiweekly** payments with quarterly returns.

```oa-check
name: NC withholding deposit schedule
inputs:
  annual_withheld: 18000
  grown_annual: 36000
steps:
  - avg: annual_withheld / 12
  - quarterly: min(max(250 - avg, 0), 1)
  - semiweekly: min(max(avg - 1999.99, 0), 1)
  - monthly: 1 - quarterly - semiweekly
  - grown_avg: grown_annual / 12
  - grown_semiweekly: min(max(grown_avg - 1999.99, 0), 1)
expected:
  avg: 1500
  quarterly: 0
  semiweekly: 0
  monthly: 1
  grown_semiweekly: 1
```

## When to refuse or refer

| Situation | Action |
| --- | --- |
| Pension or annuity withholding (Form NC-4P) | Refer; not covered here |
| Worker classification disputes (employee or contractor) for NC tax or UI | Refer to a reviewer |
| UI rate protests, voluntary contributions, successor (acquisition) accounts and SUTA dumping | Refer to DES guidance |
| Wage payment law, final pay, leave, new hire reporting | Refer; not tax, and not re-checked in this rewrite |
| Multistate sourcing of remote employees' wages beyond the two rules in the table | Refer |

## Filing and payment

| Obligation | When | Source |
| --- | --- | --- |
| NC withholding, quarterly filer | Last day of the month after the quarter | [G.S. 105-163.6(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.6.html) |
| NC withholding, monthly filer | 15th of the next month; December by January 31 | [G.S. 105-163.6(c)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.6.html) |
| NC withholding, semiweekly payer | Payments per payday rule; return quarterly | [G.S. 105-163.6(d)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.6.html) |
| W-2s, NC-1099M or 1099s to workers; NC-3 with State copies (electronic) | January 31, 2027 | [NCDOR NC-30 (2026)](https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open) |
| DES Quarterly Tax and Wage Report and payment | April 30, July 31, October 31, January 31 | [DES quarterly report](https://des.nc.gov/employers/file-adjust-or-review-quarterly-tax-wage-report) |
| DES late filing / late payment | 5% of the tax due per month or part, up to 25%; 10% of the tax due; interest at the G.S. 105-241.21 rate | [DES quarterly report](https://des.nc.gov/employers/file-adjust-or-review-quarterly-tax-wage-report) |
| NCDOR late filing / late payment of withholding | 5% a month up to 25%; 5% of the tax | [G.S. 105-236(a)(3), (4)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html) |

## Completion checklist

- [ ] Every employee has an NC-4, NC-4 EZ or NC-4 NRA
- [ ] Payroll software uses 4.09% and the 2026 per-period standard deductions
- [ ] Supplemental method chosen per payment
- [ ] Nonresident and ITIN contractors over $1,500 withheld at 4%
- [ ] Deposit schedule matches NCDOR's assignment
- [ ] DES rate from NCUI 104 (or 1% new) on wages up to $34,200
- [ ] NC-3, W-2s and 1099s filed by January 31, 2027

## Sources

| Source | URL | Read for | Read on |
| --- | --- | --- | --- |
| NCDOR NC-30, 2026 Income Tax Withholding Tables and Instructions for Employers (PDF, 15 December 2025) | https://www.ncdor.gov/income-tax-withholding-tables-and-instructions-employers/open | Read for 4.09%, per-period deductions, allowances, supplemental wages, contractor withholding, year-end duties | 2026-11-13 |
| G.S. 105-153.7 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html | Read for the 3.99% 2026 rate and later triggers | 2026-11-13 |
| G.S. 105-163.1 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.1.html | Read for employee, wages, nonresident and ITIN contractor definitions | 2026-11-13 |
| G.S. 105-163.6 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-163.6.html | Read for quarterly, monthly and semiweekly schedules | 2026-11-13 |
| G.S. 105-236 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html | Read for NCDOR penalties | 2026-11-13 |
| DES tax rate information | https://des.nc.gov/employers/tax-rate-information | Read for the $34,200 wage base, 1% new rate, 0.06% to 5.76%, base rate, surtax | 2026-11-13 |
| DES am I required to pay taxes | https://des.nc.gov/employers/am-i-required-pay-taxes | Read for liability tests and NCSUITS registration | 2026-11-13 |
| DES file, adjust or review quarterly tax and wage report | https://des.nc.gov/employers/file-adjust-or-review-quarterly-tax-wage-report | Read for due dates, electronic filing and penalties | 2026-11-13 |

Not yet confirmed: whether the 20% UI surtax applies in 2026 (it depends on the trust fund balance, not stated on the DES page); the wage bracket tables (the percentage method is used here); the 2026 forms NC-5, NC-5P and NC-5Q (names used before; the return forms themselves were not opened); whether NCDOR requires electronic filing of NC-5 returns.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nc-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nc-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
