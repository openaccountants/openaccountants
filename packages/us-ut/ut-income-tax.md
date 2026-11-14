---
name: ut-income-tax
description: "Utah 2026 enacted 4.45 percent rate, federal AGI bridge, verified 2025-2026 filing-cycle taxpayer credit and TC-40 filing; explicit limits for unpublished 2026 annual amounts."
version: "0.2"
jurisdiction: US-UT
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Utah resident individual income tax, tax year 2026

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal figures and computations belong to the linked federal owner skills.

**Answer first.** Utah starts with **federal adjusted gross income**, not federal taxable income. Apply state additions/subtractions, then the enacted **4.45%** rate for tax years beginning on or after 1 January 2026 and supported credits. The ordinary taxpayer credit is a percentage of an eligible deduction/exemption base, reduced by an income phase-out; it is not a fixed USD 966 credit. Final 2026 annual credit amounts/forms are **Not yet confirmed** here. Sources: [enrolled SB 60 sections 3-5](https://le.utah.gov/~2026/bills/sbillenr/SB0060.pdf); [TC-40 lines 4-22, verified 2025-2026 filing cycle](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).

## Scope

Full-year Utah resident employees, sole proprietors and disregarded single-member LLC owners. The enacted 2026 rate is verified; detailed annual-return mechanics below are labeled **2025-2026 filing cycle** where they come from final 2025 instructions. Do not substitute those indexed amounts for 2026 amounts. Federal return owner: `us-form-1040-individual-return`; Schedule C and SE owner: `us-schedule-c-and-se-computation`. `ut-sales-tax` owns sales/use, `ut-corporate-tax` owns corporate franchise/income tax, and `ut-payroll` owns employer withholding/SUI. TC-41 trusts/estates and specialist credits are outside the ordinary computation.

## Ask the client first

1. Tax year, domicile/residence dates, filing status, age, dependents and Utah/non-Utah work.
2. Federal AGI and return workpapers, W-2s, Schedule C/SE, K-1s and deduction details.
3. Bond interest, state refunds, lump-sum distributions, military, railroad and Social Security income.
4. Eligible standard/itemized deduction credit base and Utah additions/subtractions by code.
5. Credit evidence, other-state returns, retirement benefits and any pass-through tax election.
6. Utah withholding, voluntary prepayments, prior liability, extension and amendment history.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or amount and year limitation | Official source |
|---|---|---|
| 2026 resident tax | 4.45% of state taxable income before credits/exempt-taxpayer rule | [SB 60 sections 3-5](https://le.utah.gov/~2026/bills/sbillenr/SB0060.pdf) |
| 2025-2026 filing cycle tax | 4.50%; 2024 4.55%, 2023 4.65%, 2022 4.85% historical only | [historical table](https://incometax.utah.gov/file-pay/tax-rates/) |
| 2025-2026 filing cycle dependent credit-base amount | USD 2,111 per qualifying dependent count; not a dollar-for-dollar credit | [lines 2 and 11](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf) |
| 2025-2026 filing cycle initial taxpayer credit | 6% of eligible federal standard/itemized deduction plus dependent base, less specified state-income-tax itemized amount | [lines 11-16](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf) |
| 2025-2026 filing cycle phase-out base | Single/separate USD 18,213; head of household USD 27,320; joint/qualifying surviving spouse USD 36,426 | [lines 17-20](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf) |
| 2025-2026 filing cycle phase-out | 1.3% of positive excess of Utah taxable income over status base; credit cannot be negative | [lines 18-20](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf) |
| 2026 indexed dependent/phase-out amounts | Not yet confirmed; do not roll forward the 2025 amounts | [current final instructions are 2025](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf) |

1. Establish residence and filing requirement before computing. Domicile has statutory tests and exceptions; physical days alone do not settle every case. Part-year/nonresident filers use **TC-40 with TC-40B**, rather than treating TC-40B as a separate return. Obtain residence/sourcing analysis for mobile workers and spouses. Source: [residence and TC-40B instructions, 2025-2026 filing cycle](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).
2. Enter **federal AGI** on TC-40 line 4 under the verified 2025-2026 filing-cycle mapping. Add TC-40A Part 1 on line 5; subtract the federal-included state tax refund on line 7 and TC-40A Part 2 on line 8 to reach line 9 Utah taxable income. A below-AGI federal QBI deduction does not automatically reduce Utah's AGI base. Federal standard/itemized deductions enter the **credit base**, not the Utah income base. Source: [lines 4-20](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).
3. Schedule C net profit and federal adjustments for deductible SE tax, eligible self-employed retirement/health-insurance contributions and home-office expenses flow through the completed federal AGI to the extent included there. Do not deduct them a second time. Reconcile any Utah-specific conformity/code adjustment separately; blanket claims of no adjustment for every plan/year are not established here. Hobby-versus-business treatment and federal calculations belong to the federal owner skills. Source: [federal AGI line 4 and adjustments schedules](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).
4. Review additions, including municipal bond interest, qualifying lump-sum distributions, MSA/my529 addbacks, child/trust income, PPP and pass-through tax adjustments. Other-state municipal interest is not subject to a universal addback: bond date and reciprocal exemption conditions matter. Utah municipal/U.S. obligation interest and railroad retirement can have specified subtractions; military pay depends on residence/service rules. The old generic adoption-expense addback is **Not yet confirmed** and must not be invented. Source: [TC-40A Parts 1-2 and line 5/8 lists](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).
5. Multiply positive Utah taxable income by 4.45% for 2026 under SB 60, using actual supported 2026 credits. For the **2025-2026 filing cycle**, calculate taxpayer credit as max(6% x eligible base - 1.3% x max(Utah taxable income - status phase-out base,0),0). Eligible base is dependent amount plus federal standard/itemized deduction, less the line-14 state-income-tax itemized adjustment. The old USD 966/1,932 fixed-credit and USD 16,464/32,928 phase-out figures are superseded by the fetched final 2025 instructions. Source: [2026 rate](https://le.utah.gov/~2026/bills/sbillenr/SB0060.pdf); [2025 lines 11-22](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).
6. Apply qualified-exempt-taxpayer worksheet **before concluding tax is owed**. For the 2025-2026 filing cycle, line 21 worksheet compares AGI against the allowed federal standard deduction plus eligible federal enhanced senior deduction; age/blindness and nonresident special rules need the actual worksheet. Do not reproduce federal deduction dollar amounts here; use the federal owner and return inputs. Final 2026 worksheet is Not yet confirmed. Source: [line 21 worksheet and line 22](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).
7. Social Security is **not a blanket full subtraction**. In the 2025-2026 filing cycle, taxable benefits may qualify for nonrefundable code AH credit, reduced for higher modified income, and coordinated against retirement credit code 18. Retirement credit is a separate credit, not a subtraction from income; the old up-to-USD 450 statement needs age/birth-date and income worksheet conditions, with 2026 values Not yet confirmed. Military retirement also has a separate credit and coordination. A health-insurance credit cannot reuse premiums already deducted federally. Source: [Part 3 codes 18,23, AH, AJ](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).
8. Other-state income-tax credit uses TC-40A Part 4 **code 17** with its worksheet and common-income limits; it is not automatic reimbursement of every tax paid elsewhere. The verified 2025-2026 filing cycle also provides a nonrefundable earned-income credit based on qualifying federal EITC and Utah W-2 wages; a Schedule C-only taxpayer does not satisfy that wage condition. Final 2026 credit instructions/changes remain Not yet confirmed. Source: [Part 3 code AM and Part 4 code 17](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).
9. Subtract supported nonrefundable credits subject to tax limits, then refundable credits/payments to determine balance/refund. Do not mix consumer use tax into the individual income-tax rate; TC-40 line 31 is a separate use-tax item when not reporting it on a sales-tax account. Source: [lines 23-40 and use-tax worksheet](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).

### Boundaries and corrected form map

| Situation | Decision |
|---|---|
| Federal taxable income supplied alone | Obtain federal AGI; QBI/standard deduction cannot be silently imported into state income base |
| Dependent exemption base | Apply credit percentage and phase-out; do not subtract USD 2,111 from tax |
| Social Security or retirement | Test actual credit worksheet and coordination; no blanket exemption |
| Part-year/nonresident | TC-40 plus TC-40B allocation; refer residency/source disputes |
| Amended return | Amend TC-40 with reason code; TC-40A is additions/subtractions/credits schedule, not the amended return |
| Corporate or fiduciary | TC-20 owner `ut-corporate-tax`; TC-41 fiduciary computation outside this skill |
| Historic preservation, renewable energy, mining/extraction | Retain topic as specialist referral; eligibility, certifications and 2026 amounts Not yet confirmed |
| Separate state SE tax / only state obligation | No separate SE computation established here; sales/use, payroll and industry obligations must still be tested |

Source for form/credit distinctions: [amendment section and schedules, 2025-2026 filing cycle](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).

## Worked cases

**Case 1, ordinary 2026 wage taxpayer with no credits.** Invented full-year resident has verified AGI USD 200,000, no Utah modifications, no applicable credits after documented review, and USD 9,000 withholding. Utah taxable income USD 200,000 produces USD 8,900 income tax and USD 100 refund before any use tax or other return items. This isolates the enacted 2026 rate; it does not establish missing annual credit thresholds.

```oa-check
name: Utah enacted2026 resident rate and payments
inputs:
  federal_agi: 200000
  additions: 0
  subtractions: 0
  withholding: 9000
steps:
  - utah_taxable: federal_agi + additions - subtractions
  - income_tax: max(utah_taxable, 0) * 0.0445
  - refund: max(withholding - income_tax, 0)
expected:
  utah_taxable: 200000
  income_tax: 8900
  refund: 100
```

**Case 2, credit decision, verified 2025-2026 filing cycle only.** Invented single taxpayer has USD 40,000 Utah taxable income and an eligible credit base of USD 10,000 from actual supported return inputs, no dependents or other credits, and is not exempt under line 21. Initial credit USD 600 less phase-out USD 283.231 gives USD 316.769 credit and USD 1,483.231 tax before whole-dollar return rounding. These are 2025 mechanics and amounts, not a 2026 credit computation.

```oa-check
name: Utah2025cycle taxpayer credit not fixed966
inputs:
  utah_taxable: 40000
  eligible_credit_base: 10000
steps:
  - initial_credit: eligible_credit_base * 0.06
  - phase_out: max(utah_taxable - 18213, 0) * 0.013
  - taxpayer_credit: max(initial_credit - phase_out, 0)
  - net_tax: max(utah_taxable * 0.045 - taxpayer_credit, 0)
expected:
  initial_credit: 600
  phase_out: 283.231
  taxpayer_credit: 316.769
  net_tax: 1483.231
```

## When to refuse or refer

Refer unresolved 2026 credit/form amounts, domicile disputes, nonresident allocation, unusual bond reciprocity, pass-through elections, amended multi-state returns, trust/estate TC-41, mining and certified historic/renewable credits. Obtain current primary authority before claiming the old unsupported exemptions or addbacks.

## Filing and payment

The **2025-2026 filing cycle** calendar return/payment was due 15 April 2026; fiscal returns ordinarily due 15th day of fourth month, with weekend/holiday next-business-day rule and any official federal-linked change. Utah grants an automatic six-month filing extension **without an extension form or federal extension requirement**; this does not extend payment. For that cycle, original-due-date prepayment test is 90% current liability or 100% prior liability; first/no-prior-liability filer uses 90% current. Interest runs on unpaid tax from original due date. Utah **does not require quarterly individual estimated payments**; voluntary prepay through TAP or TC-546. The old USD 1,000 threshold/federal quarterly schedule was wrong. Use TAP https://tap.tax.utah.gov, retain return acceptance, payment receipt and TC-40W withholding support. TC-547 is return payment coupon. **Final 2026 calendar dates/forms and any relief are Not yet confirmed.** Source: [When to File and Pay; Extension; Payment Options](https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf).

## Completion checklist

- Residence, year and federal AGI reconciled; no QBI/standard deduction double subtraction.
- State adjustment codes, credit base, phase-out and exempt-taxpayer worksheet supported for the actual year.
- Social Security/retirement and other-state credits coordinated; withholding/payment reconciled.
- Final current-year form and accepted return/payment evidence retained; unresolved gaps referred.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for SB 60 enrolled full two pages, corporate and individual rate amendments, May 6 effective date and retrospective tax years beginning January 1,2026. | https://le.utah.gov/~2026/bills/sbillenr/SB0060.pdf | 2026-11-13 |
| Read for Final 2025 TC-40 instructions: filing/extension and no estimated mandate, residency/amendment, lines 4-40, TC-40A additions/subtractions, taxpayer-credit and exemption worksheets, retirement/SS/military/EITC/other-state credit sections; 2025-2026 filing cycle only. | https://files.tax.utah.gov/tax/forms/current/tc-40inst.pdf | 2026-11-13 |
| Read for Current official historical rate table 2022-2025; its 2025-current 4.5 label is not authority overriding enacted 2026 SB 60. | https://incometax.utah.gov/file-pay/tax-rates/ | 2026-11-13 |

Not yet confirmed: final 2026 TC-40/TC-40A/TC-40B line instructions, dependent and phase-out indexed amounts, exempt-taxpayer and senior coordination,2026 credit amendments/amounts, filing calendar/relief, full residency exceptions, bond reciprocity by issue, old adoption addback, specific mining/renewable/historic credits and standalone state-SE claim. Ordinary 2026 rate and verified 2025 filing-cycle mechanics are supported; this is partial annual 2026 coverage.
