---
name: sc-income-tax
description: "South Carolina 2026 wage and sole-proprietor income: federal AGI starting point, SCIAD phased deduction and rounding, 1.99 and 5.21 percent bands, capped EITC and bounded active-business 3 percent election."
version: "0.2"
jurisdiction: US-SC
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# South Carolina resident individual income tax, tax year 2026

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal figures and computations belong to the linked federal owner skills.

**Answer first.** For tax year 2026, SC starts from **federal AGI**, replaces federal below-AGI deductions with its own income-adjusted deduction (SCIAD), and applies 1.99% below USD 30,000 taxable income or 5.21% of taxable income less USD 966 at USD 30,000 or more. The old federal-taxable-income/0%-3%-6% method belongs to 2025, not 2026. SC also has a state EITC; the old assertion that none exists is wrong. Sources: [sections 12-6-50, 510(C), 1140(15) and 3632](https://www.scstatehouse.gov/code/t12c006.php); [Information Letter 26-20](https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf).

## Scope

Ordinary full-year SC resident employees, sole proprietors and disregarded single-member LLC owners. State residents/nonresidents test filing using SC income and current requirements; nonresidents/part-year residents need Schedule NR and allocation outside this ordinary resident computation. Federal AGI/filing belongs to `us-form-1040-individual-return`; Schedule C/SE to `us-schedule-c-and-se-computation`. Sales/use is in `sc-sales-tax`, corporate income/license fees in `sc-corporate-tax`, and employer WH/UI in `sc-payroll`.

## Ask the client first

1. Domicile/residence dates, federal filing status, ages and SC/non-SC sources.
2. Federal AGI, W-2 s, Schedule C/K-1 and supporting federal deduction workpapers.
3. Dependents and state additions/subtractions, bond interest, refunds, retirement and military income.
4. Active business versus personal-services income, reasonable compensation, losses and any entity-level election.
5. Federal EIC, other-state taxes and supported SC credit certificates.
6. Withholding, estimates, prior-year SC liability and extension/payment records.

## The method, step by step

### Rates, bands and thresholds

| Tax year 2026 item | Rate, amount and conditions | Official source |
|---|---|---|
| SC taxable income below USD 30,000 | 1.99% of taxable income | [12-6-510(C)](https://www.scstatehouse.gov/code/t12c006.php) |
| SC taxable income USD 30,000 or more | 5.21% of taxable income minus USD 966 | [12-6-510(C)](https://www.scstatehouse.gov/code/t12c006.php) |
| SCIAD single/separate | USD 15,000 through federal AGI USD 40,000; phases out over USD 55,000; zero at USD 95,000 | [12-6-1140(15)](https://www.scstatehouse.gov/code/t12c006.php) |
| SCIAD head of household | USD 22,500 through AGI USD 60,000; phases out over USD 82,500; zero at USD 142,500 | [12-6-1140(15)](https://www.scstatehouse.gov/code/t12c006.php) |
| SCIAD joint/surviving spouse | USD 30,000 through AGI USD 80,000; phases out over USD 110,000; zero at USD 190,000 | [12-6-1140(15)](https://www.scstatehouse.gov/code/t12c006.php) |
| SCIAD reduction rounding | Round the **reduction** down to next USD 10; no deduction when fraction reaches one | [12-6-1140(15)(b/c)](https://www.scstatehouse.gov/code/t12c006.php); [SCIAD table and rounding](https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf) |
| State EITC | Nonrefundable; 125% of qualifying federal EITC, limited to USD 200 and SC tax; full-year resident requirement | [12-6-3632](https://www.scstatehouse.gov/code/t12c006.php) |
| Active trade/business election | 3% only on qualifying separated income, after exclusions and allocations | [12-6-545](https://www.scstatehouse.gov/code/t12c006.php) |

1. Prepare federal AGI. Beginning after 2025, SC does not adopt IRC sections 63(b) through (g): federal standard/itemized deductions, senior/tips/overtime/car-loan deductions, QBI and nonitemizer charitable deduction do not simply reduce the SC base. Do not start with federal Form 1040 taxable income or deduct SCIAD on top of federal deductions. Source: [Federal Deductions section](https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf).
2. Reconcile SC additions/subtractions to the new AGI starting point. The old state-income-tax add-back was tied to a federal Schedule A deduction already embedded in **2025** federal taxable income; in 2026 that below-AGI deduction is not part of the starting point, so do not double add it. Preserve separate state refund, bond, loss and conformity workpapers and obtain final 2026 SC1040 line instructions before final filing. Sources: [12-6-50/1120/1130/1140](https://www.scstatehouse.gov/code/t12c006.php); [2025 modification instructions, filing-cycle context only](https://dor.sc.gov/sites/dor/files/forms/SC1040Instr_2025.pdf).
3. Compute SCIAD from federal AGI/status. For single/separate AGI between USD 40,000 and USD 95,000, reduction = USD 15,000 x (AGI -40,000)/55,000, rounded **down** to a multiple of USD 10; SCIAD = USD 15,000 less that reduction. Use corresponding joint/HOH values in the table. At/above the full phase-out ceiling, deduction is zero. Nonresidents further prorate SCIAD by SC AGI/federal AGI. Source: [12-6-1140(15)](https://www.scstatehouse.gov/code/t12c006.php); [SCIAD worksheet rules](https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf).
4. Determine dependent and other SC deductions separately. The verified **2025-2026 filing cycle** dependent exemption is USD 4,930 each, but annual inflation adjustment means the final 2026 amount is **Not yet confirmed** here. Do not carry the 2025 value into a 2026 return as current. Current statutory retirement deduction is up to USD 3,000 before age 65 or USD 10,000 from age 65 for eligible qualifying retirement income; age-65 deduction up to USD 15,000 is reduced by retirement deduction, with separate spouse/survivor rules. Qualifying military retirement may be deducted in full under section 1171, replacing the old unconfirmed USD 30,600 limit; coordinating reductions still apply. Source: [12-6-1140(13), 1170 and 1171](https://www.scstatehouse.gov/code/t12c006.php); [2025 dependent amount distinguished from new-2026 section](https://dor.sc.gov/iit).
5. Evaluate **I-335** under section 12-6-545; do not put all Schedule C net profit at 3% merely because the owner works in the business. Exclude passive investment income, capital gains/losses, guaranteed payments for services and amounts reasonably related to personal services. An owner not reasonably compensated can have all pass-through income presumed personal-services income. Where total qualifying pass-through SC taxable income is USD 100,000 or less, the statute offers an election treating 50% of active-business income as unrelated to personal services, subject to its conditions. Active-business losses first offset active-business income. Keep the elected base outside the graduated base to avoid double taxation. Source: [12-6-545(A) to (F)](https://www.scstatehouse.gov/code/t12c006.php).
6. Compare the 3% election with the actual reformed graduated calculation and SCIAD allocation: 3% is **not automatically better** than a 1.99% band. The old USD 100,000 Schedule C example that assumed all profit taxable at 3% versus USD 5,358 at 6% was not a valid 2026 election analysis. For a partnership/S corporation entity-level election, confirm qualified entity/owner conditions, return/payment and owner exclusion; sole proprietors do not qualify as an electing entity under subsection G merely because they qualify for the individual election. Source: [12-6-545(B/E/G)](https://www.scstatehouse.gov/code/t12c006.php).
7. Apply supported credits, withholding and estimates. Full-year residents can claim nonrefundable SC EITC equal to min(125% federal EITC, USD 200, otherwise available SC tax). Document federal eligibility; do not make an automatic USD 200 payment. Two-wage-earner and other-state credits require separate worksheets; avoid assuming final 2026 limits. Sources: [12-6-3632 and credit sections](https://www.scstatehouse.gov/code/t12c006.php); [Earned Income Credit](https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf).

### Filing threshold and historical transition

Information Letter 26-20 lists SC gross-income filing thresholds: under-65 single/separate over USD 15,000, HOH over USD 22,500, joint with both under 65 over USD 30,000; age 65+ single/separate over USD 30,000, HOH over USD 37,500, joint with one age 65+ over USD 45,000 or both over USD 60,000. Check statutory status/special filing/refund requirements, rather than treating a zero computed tax as no filing requirement. Source: [Filing Requirements](https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf).

Top-rate history in the old skill remains historical context: 7% through 2021, 6.5% in 2022, 6.4% in 2023, 6.2% in 2024 and 6% in 2025, as confirmed by the current IIT page. The 2025 unverified bracket approximations and USD 642 shortcut are superseded for this 2026 skill. Future triggered rate reductions begin from 2027 under the statute; do not project a lower future rate or assume deferring income always saves tax. Source: [historical rates](https://dor.sc.gov/iit); [12-6-510(C) trigger mechanism](https://www.scstatehouse.gov/code/t12c006.php).

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Wages only | Apply AGI, SCIAD and statutory resident calculation; 3% active-business election does not apply to wages |
| Federal itemizer | Federal below-AGI deduction no longer flows into 2026 SC starting base |
| Dependents or under-six deduction | Obtain final 2026 indexed amount and eligibility; no 2025 carry-forward assumed |
| Personal-services sole proprietor or passive rental | Do not assume whole-profit 3%; separate compensation/passive exceptions and I-335 eligibility |
| Retired freelancer/military retiree | Apply qualifying income, age and coordinating deduction rules; no double deduction |
| Nonresident/part-year | Schedule NR and SCIAD proration needed; refer complex allocation |
| OBBBA/HR1 depreciation/section 179 | Reconcile SC conformity separately; final 2026 schedule treatment Not yet confirmed |

## Worked cases

**Case 1, ordinary wages with SCIAD.** Invented single resident under 65 has federal AGI USD 50,000, no dependents/other adjustments/credits and USD 1,100 SC withholding. SCIAD reduction = USD 15,000 x 10,000/55,000 = USD 2,727.2727, rounded down to USD 2,720. SCIAD USD 12,280 leaves taxable USD 37,720; tax 5.21% x 37,720 -966 = **USD 999.212** before return rounding, refund USD 100.788. No federal below-AGI deduction is subtracted.

```oa-check
name: South Carolina 2026 wages and rounded SCIAD
inputs:
  federal_agi: 50000
  withholding: 1100
steps:
  - reduction: floor((15000 * (federal_agi - 40000) / 55000) / 10) * 10
  - sciad: 15000 - reduction
  - taxable: federal_agi - sciad
  - tax: taxable * 0.0521 - 966
  - refund: withholding - tax
expected:
  reduction: 2720
  sciad: 12280
  taxable: 37720
  tax: 999.212
  refund: 100.788
```

**Case 2, phase-out ceiling decision.** Invented single wage earner compares AGI USD 94,999 and USD 95,000, with no other deductions/credits. Just below the ceiling, reduction rounds down to USD 14,990, leaving USD 10 SCIAD; at the ceiling SCIAD is zero. Taxable bases are USD 94,989 and USD 95,000, taxes USD 3,982.9269 and USD 3,983.50 before return rounding. One dollar AGI increases taxable income by USD 11 because of the last deduction step.

```oa-check
name: South Carolina SCIAD complete phaseout boundary
inputs:
  agi_below: 94999
  agi_at: 95000
steps:
  - reduction_below: floor((15000 * (agi_below - 40000) / 55000) / 10) * 10
  - deduction_below: 15000 - reduction_below
  - taxable_below: agi_below - deduction_below
  - tax_below: taxable_below * 0.0521 - 966
  - tax_at: agi_at * 0.0521 - 966
expected:
  deduction_below: 10
  taxable_below: 94989
  tax_below: 3982.9269
  tax_at: 3983.5
```

## When to refuse or refer

Refer domicile/NR sourcing, I-335 personal-services allocation, entity-level elections, unusual retirement, complex credits and uncertain conformity. Do not file using old 2025 SC1040 line numbers for the new AGI/SCIAD model. Ordinary wage computations above assume no unconfirmed indexed deductions.

## Filing and payment

The Department's 2026 reform notice states tax-year 2026 returns due **15 April 2027**. Use approved SC1040 e-file/software or permitted paper, select residency/status, enter federal AGI and current SC adjustments/SCIAD, attach required I-335/NR/credit schedules, reconcile withholding/SC1040ES payments and retain acceptance plus separate payment proof. The old blanket 2025 extension to October 2026 does not extend the 2026 return. Final 2026 form/extension instructions and estimate safe-harbor calculations remain **Not yet confirmed**. Source: [SCDOR reform notice, 2026 return due date](https://dor.sc.gov/news/information-about-h-4216); [filing resources](https://dor.sc.gov/iit).

The old 2025 mapping (line 1 federal taxable income, additions/subtractions, line 8 I-335, later credits/payments) is retained only as **2025-2026 filing cycle** history. Final 2026 line mapping, SCIAD allocation with I-335, retirement and dependent schedules must be checked before filing; do not describe line 16 as tax after withholding without the actual form. Source: [2025 SC1040 instructions](https://dor.sc.gov/sites/dor/files/forms/SC1040Instr_2025.pdf).

## Completion checklist

- Resident wage/business facts and federal AGI established for 2026.
- SCIAD status, phase-out and USD 10 reduction rounding recomputed; no duplicate federal deduction.
- I-335 base/compensation and capped nonrefundable EITC tested where relevant.
- Final form, indexed deductions and conformity gaps resolved before filing; acceptance/payment saved.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for Current code: 12-6-50, 510(C) and neighboring older subsections, 545(A-G), 1140(13/15), 1170/1171, 3632 and 4910. Effective dates and 2026 amendment notes read. | https://www.scstatehouse.gov/code/t12c006.php | 2026-11-13 |
| Read for IL26-20, all four pages: 2026 effective period, brackets, federal deductions decoupled, SCIAD three-status fractions/rounding, EITC cap, filing thresholds and withholding transition. | https://dor.sc.gov/sites/dor/files/policies/IL26-20.pdf | 2026-11-13 |
| Read for IIT page: historical 2021-2025 rates and 2025 dependent figure; separate new-2026 AGI/SCIAD section read to avoid mixing periods. | https://dor.sc.gov/iit | 2026-11-13 |
| Read for 2025 SC1040 instructions: federal taxable starting point, additions/subtractions, retirement/dependents, credits/form mapping; 2025-2026 filing cycle only. | https://dor.sc.gov/sites/dor/files/forms/SC1040Instr_2025.pdf | 2026-11-13 |

| Read for SCDOR reform notice dated 15 April 2026: 2026 applicability and 15 April 2027 return due date; separate 2025 extension paragraph read. | https://dor.sc.gov/news/information-about-h-4216 | 2026-11-13 |

Not yet confirmed: final 2026 SC1040/NR/I-335 line mapping, SCIAD allocation with mixed active-business income, 2026 indexed dependent/under-six amounts, final OBBBA/HR1 conformity including bonus/179, other-credit limits, estimates/safe-harbors/extension mechanics and local income-tax assertion. Legacy claims of no SC EITC, blanket whole-profit 3% and limited military-retirement deduction are corrected by current law; old approximate 2025 brackets are not republished as current.
