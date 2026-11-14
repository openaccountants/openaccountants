---
name: ia-income-tax
description: "Compute Iowa resident individual income tax for wages and sole-proprietor income in 2026. Covers the 3.8% flat rate, federal taxable-income starting point, state modifications, personal exemption credits, low-income and alternate-tax decisions, nonresident boundaries and estimated payments. Trigger on Iowa income tax, IA 1040, Iowa self-employed tax and Iowa estimated tax."
version: "0.3"
jurisdiction: US-IA
category: state-tax
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Iowa individual income tax, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. General reference for AI-assisted working papers; a qualified professional must review the facts, computations and filings. Circular 230 section 10.37: apply the law to established facts, consider relevant circumstances and do not rely on audit risk or assume facts that have not been supplied.

**Answer first.** Iowa taxes individual taxable income at 3.8%. Start with federal **taxable income**, then apply Iowa modifications. Do not use the old state standard-deduction table or deduct federal QBI a second time. Estimated-tax rules change in 2026: the statutory threshold is USD 1,000. [Iowa Code 422.5, 422.7 and 422.16](https://www.legis.iowa.gov/docs/code/2026/422.16.pdf).

## Scope

Individuals with Iowa wages, Schedule C income or other individual income; residents report all income subject to state modifications. Nonresidents and part-year residents use IA 126 allocation. C corporations use `ia-corporate-tax`; employers use `ia-payroll`; federal Schedule C, self-employment tax and QBI belong to `us-schedule-c-and-se-computation` and `us-qbi-deduction`.

## Ask the client first

1. Residency dates, work locations, Iowa-source income and other states' returns.
2. Filing status, dependent status, age, blindness, spouse's income and dependents.
3. Completed federal taxable-income working paper and underlying deductions.
4. Retirement distributions, Social Security, military income, bond interest, farm or employee-owned stock sales and pre-2023 NOL carryovers.
5. School district and county of residence, tax credits and any nonresident allocation.
6. Iowa withholding, estimated payments, prior-year tax and the timing of nonwage income.

## The method, step by step

### Rates, bands and thresholds

| Item and condition | Amount | Official source |
| --- | --- | --- |
| Regular individual tax, 2026 | three and eight-tenths percent of Iowa taxable income | [422.5(1)(a)](https://www.legis.iowa.gov/docs/code/2026/422.5.pdf) |
| Low-income exemption, under 65: single/MFS; joint/HOH/surviving spouse | nine thousand dollars; thirteen thousand five hundred dollars of specially adjusted net income; spouse/dependent restrictions apply | [422.5(2)](https://www.legis.iowa.gov/docs/code/2026/422.5.pdf) |
| Low-income exemption, age 65 or older: single/MFS; joint/HOH/surviving spouse | twenty-four thousand dollars; thirty-two thousand dollars; one eligible spouse suffices | [422.5(3)](https://www.legis.iowa.gov/docs/code/2026/422.5.pdf) |
| Alternate tax, joint/HOH/surviving spouse above relevant exemption | Compare regular tax with four and three-tenths percent of specially adjusted net income above thirteen thousand five hundred dollars, or thirty-two thousand dollars where eligible; use lower result | [422.5(2)(b), (3)(b)](https://www.legis.iowa.gov/docs/code/2026/422.5.pdf) |
| Nonrefundable personal exemption credits | USD 40 single/MFS; USD 80 joint/HOH; USD 40 each dependent; additional USD 20 for each qualifying age-65 or blind individual | [422.12(2)(a)](https://www.legis.iowa.gov/docs/code/2026/422.12.pdf) |
| Estimated-tax statutory trigger, 2026 | Expected Iowa income tax liability of one thousand dollars or more; apply withholding/payment exceptions before deciding installments | [422.16(12)](https://www.legis.iowa.gov/docs/code/2026/422.16.pdf) |
| Nonresident or part-year filing screen, 2025-2026 filing cycle | Iowa-source net income at least USD 1,000, unless below overall filing thresholds; lump-sum tax independently triggers filing | [2025 instructions, Who Must File](https://revenue.iowa.gov/media/4435/download?inline=) |

### Compute and reconcile the base

1. Complete the federal working paper first. Iowa Code 422.7 starts from federal taxable income. Federal standard/itemized deductions, QBI, self-employed health insurance, retirement contributions and Schedule C home-office deductions already affect that federal result as applicable; use the federal slugs for their limits. Do not create a second Iowa standard deduction or duplicate a deduction.
2. Apply Iowa Schedule 1 additions/subtractions with a reconciliation. Under 422.7(1)-(3), subtract federal-securities interest included federally, add federally exempt non-Iowa municipal interest unless a state statutory exception applies, and add back federal NOL carryovers from pre-2023 years. Under [422.9](https://www.legis.iowa.gov/docs/code/2026/422.9.pdf), separately consider remaining pre-2023 Iowa NOL carryovers; the blanket old claim that all federal NOLs are added back is incorrect.
3. Subtract eligible retirement income under 422.7(19), generally when the recipient is at least 55, disabled or an eligible survivor. Qualified-plan distributions, including qualifying Roth conversions, can be fully excluded; the old USD 6,000/12,000 cap is obsolete. Nonqualified annuities and nonqualified deferred compensation do not automatically qualify. Social Security and military retirement exclusions are separately in 422.7(20)-(21). Deduct only amounts included in the federal starting point.
4. Capital-gain relief is conditional, not a general exemption for any long-held business asset. 422.7(13) covers qualifying farming property and specified retired-farmer livestock cases; 422.7(42) covers a qualifying employee-owner's one-corporation lifetime stock election. Farm holding, participation, relative-sale and election restrictions must be checked before using IA 100. Do not apply the legacy blanket deduction to ordinary business stock or partnership interests.
5. Apply the regular rate, nonrefundable credits and any IA 126 allocation in the prescribed order. Record a full reconciliation through tax, school district/EMS surtax where applicable, other credits, payments and balance/refund. The legacy statement that Iowa has no local income-tax addition is unsafe: the school-district/EMS surtax must be checked.
6. Separately test low-income exemption, income-retention reduction and alternate tax. For these tests, reconstruct specially adjusted net income by adding back federal standard/itemized, personal-exemption and QBI deductions as required by 422.5; include both spouses' income where required. A dependent does not receive an unconditional low-income exemption. Separate filers using alternate tax use combined spousal income; a spouse electing an NOL carryback/carryforward can disqualify that alternative.

**Form map, explicitly 2025-2026 filing cycle:** the read 2025 IA 1040 puts federal AGI in 1c, deductions in 1d/1e, federal taxable income in 2, net Iowa modifications in 3, Iowa taxable income in 4 and tax in 5; Schedule 1 holds state modifications. These are reference mappings until the final 2026 form is checked. Negative federal taxable income may need reconstruction instead of importing the federal zero floor. Bank descriptions such as IOWA DEPT OF REVENUE, STATE OF IOWA TAX, IA TAX REFUND and IDR IOWA PMT are matching clues only: reconcile the tax account, period and confirmation before classifying a payment or refund.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Retirement income, either spouse below qualifying age | Test each recipient and plan separately; exclude only qualifying amounts |
| Nonresident/part-year | IA 126 allocation, including the overall-income screen; complex multistate sourcing needs review |
| Business/farm sale, NOL or alternate tax | Obtain prior-year records and elections; no automatic capital-gain relief |
| Federal/state deduction or depreciation difference | Reconcile under current Iowa law and form instructions; no unsourced automatic add-back |
| Other-state income tax | Review IA 130 resident credit and Iowa sourcing; credit is not necessarily equal to withholding |

## Worked cases

**Case 1.** An invented single Iowa resident under 65 has federal taxable income of USD 60,000, USD 2,000 federally exempt out-of-state municipal interest and USD 1,000 included federal-securities interest. No other modifications, surtax, dependent or special credit is assumed. Iowa taxable income is USD 61,000; tax is USD 2,318 less the USD 40 credit, or USD 2,278 before payments.

```oa-check
name: Iowa resident regular tax with bond modifications
inputs:
  federal_taxable: 60000
  municipal_addition: 2000
  federal_interest_subtraction: 1000
steps:
  - iowa_taxable: federal_taxable + municipal_addition - federal_interest_subtraction
  - regular_tax: iowa_taxable * 0.038
  - after_personal_credit: max(regular_tax - 40, 0)
expected:
  iowa_taxable: 61000
  regular_tax: 2318
  after_personal_credit: 2278
```

**Case 2, decision.** A joint couple under 65 has already reconciled Iowa taxable income of USD 16,000 and specially adjusted net income of USD 25,000. Assume no NOL disqualification, no surtax and only the USD 80 personal credit. Regular tax before that credit is USD 608. Alternate tax is (25,000 - 13,500) x 4.3% = USD 494.50. Choose alternate tax; after the credit, USD 414.50 remains, compared with USD 528 on the regular method.

```oa-check
name: Iowa joint alternate-tax decision
inputs:
  iowa_taxable: 16000
  adjusted_net: 25000
steps:
  - regular_before_credit: iowa_taxable * 0.038
  - alternate_before_credit: max(adjusted_net - 13500, 0) * 0.043
  - selected_after_credit: max(min(regular_before_credit, alternate_before_credit) - 80, 0)
  - regular_after_credit: max(regular_before_credit - 80, 0)
expected:
  regular_before_credit: 608
  alternate_before_credit: 494.50
  selected_after_credit: 414.50
  regular_after_credit: 528
```

## When to refuse or refer

Refer complex IA 126 allocation, pre-2023 NOL tracking, capital-gain/farm elections, pass-through IA K-1 or PTET credits, unusual state/federal conformity and contested residency. Corporate and financial-institution returns are separate jobs. Property-tax/homestead relief and inheritance administration are outside this individual computation. Do not treat an unsigned tax output as filing authority.

## Filing and payment

Under [422.21(1)](https://www.legis.iowa.gov/docs/code/2026/422.21.pdf), a calendar-year 2026 IA 1040 is due April 30, 2027. Pay tax by the original due date. For the **2025-2026 filing cycle**, the read instructions allow an automatic six-month filing extension when at least 90% of correct tax is timely paid; interest still applies to the unpaid balance. Confirm final 2026 extension instructions before relying on the corresponding filing date.

2026 installments follow [422.16(12)(b)](https://www.legis.iowa.gov/docs/code/2026/422.16.pdf): April 30, June 30, September 30, and January 31 after year-end, moving a weekend/holiday to the next business day. Thus the final nominal January 31, 2027 date moves to February 1, 2027. Use GovConnectIowa to pay, record period/SSN and confirmation, then reconcile payments to the return. IA 2210 and the statute import federal underpayment methods and exceptions; use `us-quarterly-estimated-tax` for federal figures rather than duplicating them here. Farmer/fisher and annualized-income cases require their state worksheets.

Late filing and late payment can each add 5% of unpaid tax when less than 90% was timely paid, subject to statutory waivers; see [421.27](https://www.legis.iowa.gov/docs/code/2026/421.27.pdf). Interest for overdue payments during calendar 2026 is 10% annually, 0.8% monthly and 0.027397% daily under [the 2026 notice](https://revenue.iowa.gov/press-release/2025-10-21/idr-announces-2026-individual-income-tax-and-interest-rates). Use the rate for the period of delinquency, not the return's tax year.

## Completion checklist

- Federal taxable-income starting point reconciled, with no double deductions.
- Iowa adjustments, retirement qualifications and historical NOL schedules supported.
- All filing, low-income, alternate-tax and dependent tests completed.
- IA 126, resident credit, surtax and credits addressed or escalated.
- Withholding and payments matched to account confirmations; final 2026 forms checked before filing.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Iowa Code 422.5. Read for 3.8% rate, low-income exemptions, income-retention and alternate-tax conditions. | https://www.legis.iowa.gov/docs/code/2026/422.5.pdf | 2026-11-13 |
| Iowa Code 422.7. Read for federal taxable-income base, securities, historical NOL, retirement, farm and employee-owner capital-gain modifications. | https://www.legis.iowa.gov/docs/code/2026/422.7.pdf | 2026-11-13 |
| Iowa Code 422.9. Read for pre-2023 Iowa NOL carryovers. | https://www.legis.iowa.gov/docs/code/2026/422.9.pdf | 2026-11-13 |
| Iowa Code 422.12. Read for personal, dependent, age and blindness credits. | https://www.legis.iowa.gov/docs/code/2026/422.12.pdf | 2026-11-13 |
| Iowa Code 422.16. Read for 2026 estimated-tax trigger, installment order and underpayment methods. | https://www.legis.iowa.gov/docs/code/2026/422.16.pdf | 2026-11-13 |
| Iowa Code 422.21. Read for return due date and school-district reporting. | https://www.legis.iowa.gov/docs/code/2026/422.21.pdf | 2026-11-13 |
| Iowa Code 421.27. Read for failure-to-file/pay penalties and waiver conditions. | https://www.legis.iowa.gov/docs/code/2026/421.27.pdf | 2026-11-13 |
| IDR 2026 rate announcement. Read for 2026 individual and delinquent-tax interest rates. | https://revenue.iowa.gov/press-release/2025-10-21/idr-announces-2026-individual-income-tax-and-interest-rates | 2026-11-13 |
| IDR 2025 Expanded Instructions, 2025-2026 filing cycle. Read for IA 1040 lines 1-5, Who Must File, alternate-tax decision, IA 126, IA 130, school/EMS surtax and extension. | https://revenue.iowa.gov/media/4435/download?inline= | 2026-11-13 |
| IDR retirement-income guidance. Read for qualified recipients/plans and exclusions for nonqualified annuities and deferred compensation. | https://revenue.iowa.gov/taxes/tax-guidance/individual-income-tax/retirement-income-tax-guidance | 2026-11-13 |

Not yet confirmed: final 2026 IA 1040, IA 126 and IA 2210 line mappings and final 2026 school-district/EMS surtax table; the legacy blanket business-asset capital-gain deduction is not confirmed and must not be used; detailed IA 100 farm and employee-owner elections, IA K-1/PTET credits, depreciation conformity and homestead/inheritance administration need their separate source review. The old USD 2,130/5,240 state deductions, USD 6,000/12,000 retirement cap, USD 200 estimated-tax trigger, all-NOL add-back and no-local-surtax claim are replaced, not carried forward as 2026 rules.
