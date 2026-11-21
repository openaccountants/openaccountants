---
name: ca-pension-adjustment
description: "Compute and report the pension adjustment (PA) on the T4 slip for tax year 2026: what a PA is, the pension credit for a money purchase (defined contribution) RPP provision, for a defined benefit provision (9 times the benefit entitlement minus the 600 dollar PA offset, Income Tax Regulations s. 8301(6)) and for a DPSP; rounding to the dollar; when box 52 stays blank; the plan registration number in box 50; the 2026 money purchase limit (35,390 dollars) and the DPSP and PA limits; and correcting a PA already reported. Trigger on: pension adjustment, PA, T4 box 52, box 50, RPP registration number, pension credit, money purchase limit, PA offset, DPSP PA, amended PA. Out of scope: computing RRSP deduction room (ca-fed-t1-return, canada-tax-optimization), PSPA and PAR, multi-employer and specified multi-employer plans, foreign plans, CPP and EI amounts (canada-payroll), slip correction mechanics (ca-t4-rl1-amended-cancelled)."
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-21
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
category: payroll
type: computation
version: 1.0
---

# Canada: pension adjustment on the T4 (box 52) v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

An employer that sponsors or takes part in a registered pension plan (RPP) or a deferred profit sharing plan (DPSP) must work out a pension adjustment (PA) for each member employee and report it on the T4. This skill covers the 2026 PA for a single-employer plan: the money purchase (defined contribution) pension credit, the defined benefit pension credit, the DPSP pension credit, rounding, boxes 50 and 52, the 2026 limits that cap the PA, and how to correct a PA after the slip is filed.

A PA is the total of the member's pension credits for the year with respect to the employer, under DPSPs and the benefit provisions of RPPs (and, in specialist cases, foreign plans and specified retirement arrangements) (Income Tax Regulations s. 8301(1)). CRA guide T4084 explains that a PA "reduces the amount that they can contribute to an RRSP and a PRPP in the next year". This skill stops at the PA figure: RRSP deduction room belongs to the individual's return ([ca-fed-t1-return](ca-fed-t1-return.md), [canada-tax-optimization](canada-tax-optimization.md)). Group RRSPs and pooled registered pension plans produce no PA (T4084).

Out of scope: past service pension adjustments (PSPA, guide T4104), pension adjustment reversals (PAR, guide RC4137), multi-employer and specified multi-employer plans, foreign plans, specified and government-sponsored retirement arrangements, leaves of absence and retroactive service, and connected persons. Slip correction mechanics are in `ca-t4-rl1-amended-cancelled`; CPP and EI amounts in [canada-payroll](canada-payroll.md).

## Ask the client first

1. Which plans does the employee belong to through this employer: an RPP money purchase provision, an RPP defined benefit provision, a DPSP, or more than one? Get each plan's seven-digit CRA registration number.
2. For a money purchase provision or DPSP: the employer and employee contributions made in 2026 for 2026 (including employer contributions made by the end of February 2027 that relate to 2026), and any forfeitures or surplus allocated to the member in 2026.
3. For a defined benefit provision: the plan's benefit formula, the employee's 2026 pensionable earnings and service, and any overriding maximum-pension provision.
4. Did the employee die in 2026, stop accruing benefits, join or leave the plan, or work in more than one province?
5. The employee's 2026 compensation from the employer (for the 18% limit checks).
6. Is this an original PA or a correction to a PA already reported, and for which year?

## The method, step by step

### 2026 limits [CRA, MP, DB, RRSP, DPSP, ALDA, TFSA limits, YMPE and the YAMPE](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html)

| Item | 2026 amount or rate | Official source |
|---|---|---|
| Money purchase limit | $35,390 | [CRA annual limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) |
| Defined benefit limit (per year of service) | $3,932.22 | [CRA annual limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) |
| DPSP limit (half the money purchase limit) | $17,695 | [CRA annual limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) |
| PA offset for years after 1996 | $600 | [Income Tax Regulations s. 8300(1)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8300.html) |
| Defined benefit multiplier | 9 times the benefit entitlement | [Income Tax Regulations s. 8301(6)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8301.html) |
| RPP PA limit, single-employer plan | Lesser of the money purchase limit and 18% of the member's compensation from the employer | [ITA s. 147.1(8)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-147.1.html) |
| DPSP pension credit limit | Lesser of 1/2 of the money purchase limit and 18% of compensation from the employer | [ITA s. 147(5.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-147.html) |

The money purchase limit for each year after 2009 is the greater of the 2009 limit indexed to the average wage (rounded to the nearest $10) and the previous year's limit (ITA s. 147.1(1), "money purchase limit"). The CRA publishes the resulting figure; use the table above rather than recomputing it. A PA over the limit does not change the PA reported: it makes the plan revocable (ITA s. 147.1(8)), so stop and refer.

### Step 1: money purchase provision of an RPP [Income Tax Regulations s. 8301(4)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8301.html)

The pension credit is the total of the contributions made under the provision in the year by the employee and by the employer for the employee, plus the part of amounts allocated to the employee in the year that comes from forfeitures and their earnings, surplus, or transferred actuarial surplus. Excluded contributions and the other contributions s. 8301(4)(a) names are left out. T4084 adds the practical rules: count employer contributions made by the end of February that relate to the previous year as contributions for that previous year, and do not count amounts transferred into the plan from an RRSP, RPP, PRPP or DPSP.

### Step 2: defined benefit provision of an RPP [Income Tax Regulations ss. 8301(6), 8302](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8301.html)

For a year after 1989 the pension credit is A minus B, where A is 9 times the employee's benefit entitlement under the provision for the year and B is the PA offset ($600), reduced by any offset already used under another defined benefit provision of the same or a non-arm's length employer (s. 8301(6)(a)). The benefit entitlement is defined in s. 8302. T4084 states it as "(9 × benefit earned) – $600 = pension credit" and "If the calculation results in a negative amount, the pension credit is zero."

T4084 gives the practical rules for the benefit earned: use the full benefit even if not vested; for a percentage-of-earnings formula, multiply the year's pensionable earnings by the benefit rate; for a flat benefit, take the year's flat amount; use the current year's earnings and YMPE; leave out bridging benefits, indexing of earnings, early-retirement reductions and the other exclusions the guide lists. If the plan has an overriding maximum-pension provision that binds, use it (T4084, section 11.1). The benefit earned cannot be more than the lesser of 2% of the year's earnings and the defined benefit limit (T4084, glossary).

### Step 3: deferred profit sharing plan [Income Tax Regulations s. 8301(2)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8301.html)

The pension credit is A minus B. A is the employer's contributions to the plan in the year for the employee plus the part of amounts allocated to the employee in the year that comes from forfeited amounts and their earnings (unless counted for another employer or paid to the employee in the year). B is nil unless all the s. 8301(2.1) conditions are met: the DPSP credits are no more than 50% of the money purchase limit, more than 18% of this year's compensation and no more than 18% of last year's compensation, and amounts derived from them were paid out in the year or the first two months of the next year. Employees cannot contribute to a DPSP (T4084).

### Step 4: total, round and report [Income Tax Regulations ss. 8301(1), 8311](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8311.html); [RC4120, Box 50 and Box 52](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html)

1. Add the pension credits from every RPP provision and DPSP the employer takes part in for the employee. That total is the PA for box 52.
2. Round each pension credit to the nearest dollar; a credit exactly halfway goes to the higher dollar (Reg. s. 8311). Box 52 is reported "in dollars only" (RC4120).
3. Box 50: the seven-digit CRA registration number of the RPP or DPSP under which the PA is reported, even if the plan needs only employer contributions. For union pension funds, enter the union's plan number. If the employee is in more than one plan, enter only the number of the plan with the largest PA (RC4120). T4084 adds that box 50 may be left empty when the PA is zero and the member made no contributions.
4. Leave box 52 blank when the PA is negative or zero, when the employee died during the year, or when the employee is still a member but no longer accrues new pension credits (RC4120).
5. More than one province of employment: report the PA proportionately on each T4; if it cannot be apportioned, put the total on one slip (RC4120).
6. Employee on leave who still accrues pensionable service: report the PA on a T4 even with no employment income in the year (RC4120).
7. T4 Summary line 52 is the total of box 52 from all slips (RC4120). The slip is due by the last day of February (Income Tax Regulations s. 205(1)); for 2026 slips see `ca-t4-rl1-amended-cancelled`.

### Correcting a PA already reported [T4084, section 12.1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html); [RC4120, Changes to the pension adjustment](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html)

| Situation | Action | Official source |
|---|---|---|
| Wrong or missing PA within the last four years | Issue amended T4 slips for each affected year; electronically use summary and slip report type code "A" | [T4084, 12.1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html) |
| Wrong PA for a year before the last four | Send the CRA a list: names, SINs, original PA and new PA for each year | [T4084, 12.1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html) |
| Difference under $250 | No amended PA needed, unless the employee wants it corrected or the CRA asks | [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |
| Amended slip where a PA was already reported for that year | Show the total PA for the year on the amended slip, not the difference | [RC4120](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) |

Tell affected employees that a changed PA can lead to reassessed RRSP or PRPP deductions and tax on excess contributions (T4084, 12.1). T4084 (page dated 2023-05-20) still says only employers filing fewer than 50 slips may file on paper; the current rule is the threshold of more than five slips in Income Tax Regulations s. 205.1(1), covered in `ca-t4-rl1-amended-cancelled`.

### Quebec employees

The PA is a federal figure reported on the T4. Whether and where the RL-1 slip carries a pension adjustment or the plan registration number is set in Revenu Quebec's guide RL-1.G-V, which this skill could not read (see Not yet confirmed). Do not copy box 52 onto the RL-1 without that guide.

## Boundary and exception table

| Situation | Action |
|---|---|
| Plan is a multi-employer or specified multi-employer plan | Out of scope; the administrator's figures and Reg. s. 8301(5), (8) govern |
| Member credited with past service | PSPA (guide T4104), not this skill |
| Member left before vesting | Report the PA as usual and consider a PAR (guide RC4137); out of scope |
| PA above the money purchase limit or 18% of compensation | Plan can become revocable (ITA s. 147.1(8)); refer to the plan administrator |
| Retroactive benefits for a leave of absence | Different reporting deadline and rules (T4084, section 11.5); refer |
| Group RRSP or PRPP only | No PA; box 52 blank |
| Employee asks how much RRSP room is left | Not computed here; use the individual's notice of assessment and the T1 skills |

## Worked cases

All amounts are hypothetical inputs. 2026 limits from the table above.

### Defined benefit plan, 1.5% of earnings

The plan pays 1.5% of each year's pensionable earnings for each year of service. In 2026 the employee earns $80,000 and works the full year. The benefit earned is $1,200, below both 2% of earnings ($1,600) and the defined benefit limit ($3,932.22). The pension credit is 9 times $1,200, less the $600 offset: $10,200. That is under the PA limit, the lesser of $35,390 and 18% of $80,000 ($14,400). Box 52 shows 10200; box 50 shows the plan's registration number.

```oa-check
name: Defined benefit PA, 1.5% career average, 2026
inputs:
  earnings: 80000
  benefit_rate: 0.015
  pa_offset: 600
  mp_limit: 35390
  db_limit: 3932.22
steps:
  benefit_earned: min(earnings * benefit_rate, earnings * 0.02, db_limit)
  pension_credit: max(0, 9 * benefit_earned - pa_offset)
  pa_limit: min(mp_limit, earnings * 0.18)
  headroom: pa_limit - pension_credit
expected:
  benefit_earned: 1200
  pension_credit: 10200
  pa_limit: 14400
  headroom: 4200
```

### Money purchase RPP plus DPSP, rounding, and a later small correction

The employee earns $63,457. The RPP money purchase provision takes 5% from the employee and 5% from the employer: $3,172.85 each. The employer also puts $4,000 into a DPSP. The DPSP credit is within its limit, the lesser of $17,695 and 18% of $63,457 ($11,422.26). The money purchase credit rounds from $6,345.70 to $6,346 and the DPSP credit is $4,000, so box 52 shows 10346. Box 50 shows the RPP number, the plan with the larger PA.

In 2027 the employer finds a $200 DPSP contribution for 2026 that was left out. The corrected PA would be $10,546, a difference of $200. Because the difference is under $250, no amended slip is required unless the employee wants one or the CRA asks. If the employee does ask, the amended slip shows the full $10,546, not $200.

```oa-check
name: Money purchase plus DPSP PA with rounding and the 250 dollar rule
inputs:
  earnings: 63457
  rate_employee: 0.05
  rate_employer: 0.05
  dpsp_contribution: 4000
  dpsp_limit_dollar: 17695
  missed_dpsp: 200
steps:
  mp_credit: round(earnings * rate_employee + earnings * rate_employer)
  dpsp_limit: min(dpsp_limit_dollar, earnings * 0.18)
  dpsp_credit: min(dpsp_contribution, dpsp_limit)
  box_52: mp_credit + dpsp_credit
  corrected_pa: box_52 + missed_dpsp
  difference: corrected_pa - box_52
expected:
  mp_credit: 6346
  dpsp_limit: 11422.26
  box_52: 10346
  corrected_pa: 10546
  difference: 200
```

## When to refuse or refer

Refer to the plan administrator or actuary when the defined benefit formula is integrated with CPP or QPP, depends on best or final average earnings with part-year service, has an overriding maximum that binds, or when the employee works for more than one participating employer. Refer whenever the PA would exceed the limits, for past service, PAR, multi-employer plans, foreign plans and specified retirement arrangements. Do not compute the employee's RRSP room or advise on RRSP contributions here. This skill does not file or amend slips.

## Sources

| Source | URL | Read for; read on |
|---|---|---|
| CRA, MP, DB, RRSP, DPSP, ALDA, TFSA limits, YMPE and the YAMPE (page dated 2026-10-28) | https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html | 2026 money purchase, defined benefit and DPSP limits; read 2026-11-21 in a browser and with a fetch tool (the site refuses scripted downloads) |
| CRA, T4084 Pension Adjustment Guide (web page dated 2023-05-20; the latest edition) | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html | What a PA is, glossary (PA offset, benefit earned, DPSP limit), sections 3, 4, 5.1, 5.2, 11.1, 12 and 12.1; read 2026-11-21 in a browser |
| CRA, RC4120 Employers' Guide, Filing the T4 Slip and Summary, Rev. 25 (2025 slips; 2026 edition not yet published) | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html | Box 50, box 52, line 52, changes to the PA and the $250 rule; read 2026-11-21 in a browser |
| Income Tax Regulations, ss. 8300(1) (PA offset), 8301(1), (2), (2.1), (4), (6), 8302, 8311, 205(1), 205.1(1) (current to 2026-10-29) | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/FullText.html | PA definition, pension credit formulas, rounding, filing date; read 2026-11-21 |
| Income Tax Act, ss. 147(5.1), 147.1(1) (money purchase limit), 147.1(8) (current to 2026-10-29) | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/FullText.html | DPSP and RPP PA limits, money purchase limit rule; read 2026-11-21 |

Not yet confirmed: whether the RL-1 slip carries a pension adjustment or RPP registration number, and in which box (Revenu Quebec's guide RL-1.G-V could not be read: revenuquebec.ca returned a bot-protection page and the archive copy was refused on 2026-11-21). The benefit entitlement rules of Income Tax Regulations s. 8302 were not read in full; the skill relies on T4084 for the benefit-earned method. The 2026 PA offset is the statutory $600; no 2026-specific CRA notice was found or needed.
