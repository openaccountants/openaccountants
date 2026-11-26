---
name: ca-pension-adjustment
description: "Calculate and report an ordinary 2026 pension adjustment (PA) for a single employer: money purchase RPP contributions, a simple defined benefit provision, DPSP contributions, rounding, T4 boxes 50 and 52, plan-limit checks and corrections to a reported PA. Trigger on pension adjustment, T4 box 52, box 50, pension credit, DPSP PA or amended PA. Specialist plans, service adjustments, RRSP room and Quebec slip mapping require individual advice."
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
category: payroll
type: computation
version: 1.1
---

# Canada: pension adjustment on the T4 (box 52) v1.1

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For an employer participating in an RPP or DPSP, the pension adjustment (PA) is the employee's total pension credits for the year with that employer. This Guide calculates ordinary 2026 credits for one employer and reports them on the T4. Specialist cases appear under referrals. [Regulations 8301(1)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8301.html), [CRA T4084, sections 1 and 3](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html).

A PA generally reduces the following year's RRSP/PRPP room; it is not an RRSP deduction or a calculation of available room. Individual or group RRSPs and PRPPs do not themselves produce a PA. [CRA T4084, introduction and section 1.1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html).

## Ask the client first

Obtain the plan documents and registration numbers; actual dated contributions and any transfers, refunds, forfeitures or surplus allocations; benefit formula and payment options; pensionable earnings and service; compensation for limit purposes; related-employer participation; death, leave, entry or exit dates; provinces of employment; and the year, original amount and reason for any correction. Do not assume missing eligibility facts.

## The method, step by step

### 2026 reference amounts

| Item | 2026 amount or rate | Official source |
|---|---|---|
| Money purchase limit | $35,390 | [CRA annual limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) |
| Defined benefit limit | $3,932.22 | [CRA annual limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) |
| DPSP dollar limit | $17,695 | [CRA annual limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) |
| PA offset | $600 | [Regulations 8300(1)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8300.html) |
| Defined benefit multiplier | 9 times benefit entitlement | [Regulations 8301(6)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8301.html) |

### 1. Ordinary contributions

For an ordinary money purchase (defined contribution) RPP provision, add the employee's and employer's contributions made in and relating to 2026. For a DPSP, count employer contributions; members cannot contribute. Employer contributions made in January or February 2027 that relate to 2026 count for 2026. These simple calculations assume no excluded or corrective contributions, transfers, allocations, refunds, repayments or special allocation method. For those items: Check this point with one of our partner accountants. [Regulations 8301(2), (4), (4.1), (11)](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8301.html), [CRA T4084, sections 4 and 5.1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html).

### 2. Simple defined benefit provision

For one full year of service under a single, unintegrated career-average provision, with no other provision or employer sharing the offset and no special benefit features, use the year's pensionable earnings multiplied by the plan's benefit rate. Count the benefit even if unvested. The credit is `max(0, 9 × benefit earned − 600)`. Check the plan's maximum-pension provision; if it binds or any of these assumptions fails, use the referral below rather than this simplified formula. [Regulations 8301(6) and 8302](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8302.html), [CRA T4084, glossary and section 5.2](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html).

### 3. Check plan limits; do not cap the calculated credit

For a single-employer RPP, the PA with that employer (including DPSP credits) is tested against the lesser of $35,390 and 18% of the member's compensation from that employer. This is a plan-revocability test, subject to regulatory exceptions, not authority to reduce the reported PA to the limit. For more than one employer, including non-arm's-length employers: Check this point with one of our partner accountants. [ITA 147.1(8)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-147.1.html).

Across the employer's DPSPs, total pension credits are tested against the lesser of $17,695 and 18% of compensation as defined in ITA 147.1(1), excluding paragraph (b) prescribed amounts. With one employer and no non-arm's-length employer participation, the total PA across RPPs and DPSPs must also satisfy the lesser of $35,390 and 18% of compensation. For related-employer aggregation, a doubtful compensation base or any excess: Check this point with one of our partner accountants. [ITA 147(5.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-147.html). The examples assume ordinary resident salary is both pensionable earnings and the relevant compensation, with no prescribed or other adjustments.

### 4. Round and report

- Round **each pension credit first** to the nearest dollar, taking an exact half-dollar upward. Then add the credits for the employer to obtain the PA. [Regulations 8311](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8311.html), [T4084, section 3.1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html).
- **T4 box 52:** report the PA in whole dollars. Leave it blank if the calculated PA is zero or negative, the employee died in the year, or the employee no longer accrues new pension credits in the year. [RC4120, box 52](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html).
- **T4 box 50:** enter the seven-digit CRA RPP/DPSP registration number, even for employer-only contributions. For union pension funds use the union's plan number; for multiple plans use the plan with the largest PA. It may be blank if the PA is zero and the member made no contributions. [RC4120, box 50](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html), [T4084, section 12](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html).
- **Multiple provinces/territories:** apportion the PA between the T4 slips; if it cannot be apportioned, report it all on one slip. [RC4120, box 52](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html).
- **Leave:** if still accruing pensionable service or credits, report the PA on a T4 even with no employment income; this reporting rule does not supply the leave calculation. Specialist plans and leave calculations are referred below. [RC4120, box 52](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html).
- **T4 Summary line 52:** total box 52 from all T4 slips. [RC4120, line 52](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html).

The box instructions above are from RC4120 Rev. 25. Use the applicable filing-year instructions and deadline before submission; this Guide does not file returns.

### 5. Correct an already reported PA

The administrative exception is a difference **less than $250** between a previously reported PA and its corrected amount, unless the employee or CRA asks for correction. It does not excuse an originally omitted PA. When amending a previously reported PA, show the full corrected year's PA, not the difference. [CRA T4084, section 12.1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html), [RC4120, changes to the pension adjustment](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html).

For a required correction within the last four years, issue amended T4 slips for the affected years. For earlier years, send CRA a list identifying the individuals, their SINs, original PAs and new PAs by year. Tell affected employees that RRSP/PRPP deductions may be reassessed and excess-contribution tax or withdrawals may result. Use T4084 section 12.1 for the older-year routing and current RC4120 for submission mechanics. [CRA T4084, section 12.1](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html).

## Worked cases

Both examples are hypothetical. They assume a living employee, one employer, ordinary resident salary equal to pensionable earnings and compensation, no related-employer or specialist arrangements, no other credits and no transfers, allocations, refunds or repayments. Confirm those facts before applying the results.

### Defined benefit plan, 1.5% of earnings

Assume full-year service in 2026, a career-average benefit of 1.5% of each year's pensionable earnings, no special payment options and no binding lower plan maximum. With $80,000 earnings, benefit earned is $1,200, below both 2% of earnings ($1,600) and the 2026 defined benefit limit ($3,932.22). The sole credit is 9 × $1,200 − $600 = $10,200. The PA limit is min($35,390, 18% × $80,000) = $14,400, leaving $4,200 headroom. Box 52 is 10200; box 50 carries the plan registration number. Sources: steps 2–4.

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

### Money purchase RPP plus DPSP, rounding and small correction

With $63,457 earnings in 2026, employee and employer RPP contributions at 5% each are $3,172.85 each. Assume all contributions were actually made in 2026 for 2026. The employer's DPSP contribution is $4,000. The RPP credit rounds from $6,345.70 to $6,346; the DPSP credit is $4,000. Box 52 is 10346. Box 50 carries the RPP number because that plan has the larger credit.

In 2027 the employer discovers an additional $200 DPSP contribution **actually made in 2026 for 2026**, omitted from the calculation of an already reported PA. Corrected DPSP credit is $4,200; corrected PA is $10,546. The DPSP limit is min($17,695, 18% × $63,457) = $11,422.26; the combined PA limit is also $11,422.26. Both the original and corrected amounts pass both tests. The $200 difference is less than $250, so amendment is not required unless the employee or CRA requests it; if requested, report the full $10,546. This is a reporting error, not a new late contribution. Sources: steps 1, 3–5.

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
  employee_contribution: earnings * rate_employee
  employer_contribution: earnings * rate_employer
  mp_credit: round(employee_contribution + employer_contribution)
  dpsp_limit: min(dpsp_limit_dollar, earnings * 0.18)
  dpsp_credit: dpsp_contribution
  box_52: mp_credit + dpsp_credit
  corrected_dpsp: dpsp_credit + missed_dpsp
  corrected_pa: mp_credit + corrected_dpsp
  difference: corrected_pa - box_52
  corrected_headroom: dpsp_limit - corrected_pa
expected:
  employee_contribution: 3172.85
  employer_contribution: 3172.85
  mp_credit: 6346
  dpsp_credit: 4000
  dpsp_limit: 11422.26
  box_52: 10346
  corrected_dpsp: 4200
  corrected_pa: 10546
  difference: 200
  corrected_headroom: 876.26
```

## When to refuse or refer

| Situation | Action |
|---|---|
| Forfeitures, their earnings, surplus, actuarial-surplus or other surplus transfers, excluded/corrective contributions, payouts, refunds or DPSP repayment adjustment | Check this point with one of our partner accountants. |
| More than one employer, non-arm's-length employers, multiple defined benefit provisions or sharing the PA offset | Check this point with one of our partner accountants. |
| Flat benefits, best/final-average or integrated CPP/QPP formulas, YMPE/YAMPE, indexing, bridging or early/postponed retirement features, payment options, binding maximum, part-year service, joining/leaving or leaving before vesting | Check this point with one of our partner accountants. |
| Past service/PSPA, PAR, multi-employer or specified multi-employer plans, foreign plans, specified or government-sponsored retirement arrangements, connected persons | Check this point with one of our partner accountants. |
| Leave calculations, retroactive service/contributions, filing deadlines, electronic/paper filing or detailed amendment mechanics | Check this point with one of our partner accountants. |
| Quebec RL-1 mapping of the PA or registration number; CPP/EI/QPP amounts | Check this point with one of our partner accountants. |
| Actual RRSP/PRPP room or contributions, compensation uncertainty or a plan-limit excess | Check this point with one of our partner accountants. |

## Sources

| Official source | Read for; date |
|---|---|
| [CRA annual limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) | 2026 MP, DB and DPSP row; applicable completed source read reused, 2026-11-26 |
| [CRA T4084](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4084/pension-adjustment-guide.html) | Introduction, sections 1, 3–5 and 12–12.1; read 2026-11-26 |
| [CRA RC4120, Rev. 25](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) | Boxes 50/52, Summary line 52 and amended PAs; read 2026-11-26; revision retained as published |
| [Regulations 8300](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8300.html), [8301](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8301.html), [8302](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8302.html), [8311](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-8311.html) | Offset, credits, contribution timing, benefit entitlement and rounding; read 2026-11-26 |
| [ITA 147(5.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-147.html), [147.1(1), (8)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-147.1.html) | Compensation and DPSP/RPP limit conditions; read 2026-11-26 |

Not yet confirmed: None within the stated scope; specialist topics are referred above.
