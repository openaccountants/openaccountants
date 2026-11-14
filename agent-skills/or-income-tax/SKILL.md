---
name: or-income-tax
description: "Oregon resident individual income tax: federal AGI bridge, Oregon deductions and credits, final 2025-2026 filing-cycle tax tables, published 2026 planning figures and actual 2026 estimates."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/or-income-tax"
  jurisdiction: "US-OR"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Oregon individual income tax, 2026 planning and 2025-2026 filing cycle

> **General reference only.** This skill provides working papers and a filing brief, not accountant approval. Apply cited law to verified facts, identify assumptions and unresolved issues, and obtain qualified professional review before filing or acting. Circular 230 section 10.37 requires reasonable factual and legal analysis.

## Scope

Oregon (US-OR) individual income tax for resident sole proprietors and disregarded single-member LLC owners. Federal income is an input; this skill owns Oregon adjustments, deductions, tax and credits. It covers actual 2026 estimated-payment rules and published 2026 planning figures. Final-return boxes, finalized tax tables and credits below are explicitly the **2025-2026 filing cycle** until final 2026 Form OR-40 instructions are read. Do not label those figures final 2026 return law.

Use `us-federal-income-tax-return-1040` and `us-federal-return-assembly` for federal AGI and return reconciliation, `us-schedule-c-and-se-computation` for business profit and federal self-employment tax, and `us-child-tax-credit-and-eitc` for federal EITC. Federal deductions, rates, wage bases and credit ceilings are not repeated here. `or-cat` owns CAT, `or-corporate-tax` corporate excise/income tax and `or-payroll` employer withholding, UI and transit payroll taxes.

## Ask the client first

- What domicile, permanent homes, move dates, Oregon days, military facts and resident/nonresident periods apply?
- What federal AGI, schedules, business income, asset differences and Oregon additions/subtractions are supported?
- What filing status, dependents, ages, disability, immigration status and spouse deduction election apply?
- What federal tax liability after credits, Oregon itemized deductions, benefit income and state refunds are included?
- What current/prior-year tax, credits, withholding, estimated payments and change in marital status affect credits and installments?
- Where were services performed or delivered, and what Portland-area, transit district or other-state obligations require separate work?

## The method, step by step

### 1. Establish the return and period

The 2025 instructions distinguish domicile from physical presence. A person domiciled in Oregon generally remains resident while temporarily away. A nondomiciliary with a permanent Oregon abode and more than 200 Oregon days can be resident unless the statutory temporary/transitory exception applies. Domiciliaries meeting the separate no-Oregon-home, outside-home and no-more-than-30-Oregon-days conditions may be nonresidents. Review military and foreign-residence exceptions individually. Full-year residents use OR-40; part-year residents use OR-40-P and nonresidents OR-40-N with Oregon-source allocation. Do not apply the resident computation to a mover simply because a mailing address is in Oregon. [2025-2026 filing-cycle instructions pp.6-8](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

Confirm filing need using the year's status/age/dependency filing chart, not just positive taxable income. Claiming a refund or kicker may require a return even without a normal filing requirement. This skill does not reproduce a complete resident filing-threshold chart. Return obligations, a nonresident employer's withholding exception and estimated-payment requirements are different tests. [OR-40 pp.6-8,18](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf); [2026 combined payroll p.4](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf).

### 2. Reconcile from federal AGI, once

**Start at federal adjusted gross income, not federal taxable income.** In the 2025-2026 filing-cycle map, OR-40 line 7 takes federal Form 1040/1040-SR line 11a. The Oregon standard or itemized deduction is then taken once on the Oregon return. There is no second deduction layered on federal taxable income. Include the required federal return and schedules with the Oregon filing. [OR-40 p.14](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

| 2025-2026 filing-cycle field | Workpaper input / operation | Official source |
|---|---|---|
| OR-40 line 7 | Federal AGI, not federal taxable income | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 8, then line 9 | Add Schedule OR-ASC section A total; total income is lines 7 + 8 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 10 | Allowed federal tax liability subtraction from its worksheet/phase-out | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 11 | Taxable Social Security and tier 1 Railroad Retirement benefits included federally | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 12 | Oregon income tax refund included in federal income | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 13 | Other allowed OR-ASC section B subtractions | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 14 | Total subtractions; line 15 is line 9 less line 14 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 16 | Oregon itemized deductions from Schedule OR-A, not copied federal itemization | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 17, then line 18 | Oregon standard deduction, then allowed standard/itemized deduction | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 19 | Oregon taxable income after the deduction, floored at zero | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 20 | Tax table below $50,000; status-specific rate chart at/above $50,000 | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Lines 21-23 | Applicable installment-sale interest, recaptures and total tax before credits | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Line 25 | Allowed exemption credit; other credit/payment fields follow the actual form | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |

Do not mechanically add back every federal deduction. Income-tax conformity, depreciation/basis, business interest, research costs, federal new deductions and additions must be reconciled item by item to OR-ASC/OR-17. A federal deduction already below federal AGI is not automatically an Oregon AGI subtraction. Other-state municipal interest, federal obligation interest and asset basis differences need the correct year's specific codes; unsupported OBBBA/bonus/section 179/174A adjustments are not defaulted to zero or invented. [OR-40 pp.14-16](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

The 2025 federal tax liability subtraction uses federal income tax after credits other than EITC, not estimated payments, withholding, a refund or federal self-employment tax. Its worksheet addresses Form 4972, excess advance premium credit repayment, fiscal years, allocation to income Oregon taxes and prior-year changes. Do not substitute cash tax paid. [OR-40 pp.14-15](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

| Item / condition | Rate, amount or threshold | Official source |
|---|---|---|
| 2025 federal liability subtraction, single; also MFS phase-out bands | Federal AGI below $125,000: $8,500 cap; $125,000-<130,000: $6,800; $130,000-<135,000: $5,100; $135,000-<140,000: $3,400; $140,000-<145,000: $1,700; at least $145,000: zero. MFS caps are half these amounts. | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| 2025 federal liability subtraction, joint/HOH/qualifying surviving spouse | AGI below $250,000: $8,500; $250,000-<260,000: $6,800; $260,000-<270,000: $5,100; $270,000-<280,000: $3,400; $280,000-<290,000: $1,700; at least $290,000: zero. | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| 2025 ordinary standard deduction | Single/MFS $2,835; joint/qualifying surviving spouse $5,670; HOH $4,560, subject to dependent, age/blindness, immigration and separate-spouse exceptions. | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| Published 2026 ordinary standard deduction, later combined-payroll publication | Single/MFS $2,910; joint/qualifying surviving spouse $5,820; HOH $4,685. These replace the earlier estimated $2,900/$5,800/$4,650 amounts in the 2026 estimate publication. | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf; https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf |
| 2025 exemption credit | Eligible exemptions x $256. Zero above federal AGI $100,000 for single/MFS or $200,000 for other statuses. Additional disability credit has its own $100,000 limit. | https://www.oregon.gov/dor/programs/individuals/pages/credits.aspx |

### 3. Choose the Oregon deduction and calculate tax

Compare allowed Oregon Schedule OR-A deductions with the Oregon standard deduction. Oregon may differ from federal itemization, including state income tax treatment. Married-separate taxpayers cannot use a standard deduction if the spouse itemizes. Dependents have an earned-income/minimum worksheet and cap; age/blindness additions have status-specific amounts. Non-U.S. citizens without permanent resident status may have a zero standard deduction under these instructions. Use the actual applicable worksheet rather than the ordinary amounts above. [OR-40 p.16](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

The following final-return chart is **2025-2026 filing cycle** only. Below $50,000, use the published tax-table income interval and status column. The old low-band formulas are not carried forward: they did not reproduce the required tax table. At/above $50,000 use the published chart, including its stated rounded base rather than constructing a new base from nominal marginal bands. [OR-40 pp.17,30-32](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

| Item / condition | Rate, amount or threshold | Official source |
|---|---|---|
| 2025 single/MFS taxable income $50,000 through $125,000 | $4,065 + 8.75% x (income - $50,000) | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| 2025 single/MFS taxable income above $125,000 | $10,627 + 9.9% x (income - $125,000) | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| 2025 joint/HOH/qualifying surviving spouse income $50,000 through $250,000 | $3,756 + 8.75% x (income - $50,000) | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| 2025 joint/HOH/qualifying surviving spouse above $250,000 | $21,256 + 9.9% x (income - $250,000) | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| 2026 estimate Chart S, single/MFS | Up to $4,550: 4.75%; >$4,550-11,400: $216 + 6.75% excess over $4,550; >$11,400-125,000: $678 + 8.75% excess over $11,400; >$125,000: $10,618 + 9.9% excess over $125,000. Planning chart, not final return tax table. | https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf |
| 2026 estimate Chart J, joint/HOH/qualifying surviving spouse | Up to $9,100: 4.75%; >$9,100-22,800: $432 + 6.75% excess over $9,100; >$22,800-250,000: $1,357 + 8.75% excess over $22,800; >$250,000: $21,237 + 9.9% excess over $250,000. Planning chart only. | https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf |
| Early 2026 estimate publication credit and federal subtraction | Estimated exemption credit $260; federal liability subtraction $0-$8,750. Final 2026 return credit and complete phase-out must be confirmed separately; the payroll allowance is not an individual-return credit determination. | https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf |

For 2026 planning use later published standard deductions above instead of copying the early estimate publication's provisional deductions. Keep the tax chart's estimate label and reconcile to final 2026 instructions before return preparation. The 2026 payroll formula is a different algorithm; its allowance, constant and withholding deduction must not be used to produce a Form OR-40 liability. [2026 estimate p.3](https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf); [2026 combined payroll p.4](https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf).

Farm averaging, qualifying farm-asset capital gains and the Oregon qualified business income reduced rate are separate Oregon methods. The ordinary marginal chart is not compulsory for every business owner. The OR-PTE reduced-rate election has material-participation and other conditions, is made on the original return and is irrevocable after the original-return election. It is not the federal QBI deduction. Eligibility and complete reduced-rate computation remain outside this ordinary-return calculation. [OR-40 p.17](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

### 4. Apply credits with their actual eligibility

The exemption credit has an income cutoff, not a gradual phase-out beginning at that amount. Determine eligible exemptions from the return, including whether another person can claim the taxpayer. Limit nonrefundable credits to tax as directed; preserve carryforwards separately. [OR-40 pp.12-13,17-18](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf); [DOR credits](https://www.oregon.gov/dor/programs/individuals/pages/credits.aspx).

| Item / condition | Rate, amount or threshold | Official source |
|---|---|---|
| 2025 Oregon refundable EIC | 9% of qualifying federal EITC; 12% if the taxpayer has a dependent younger than 3 at year-end. Part-year/nonresident credit is multiplied by Oregon percentage. | https://www.oregon.gov/dor/programs/individuals/pages/credits.aspx |
| 2025 higher education savings plan contribution credit | Refundable up to $180, or $360 joint, subject to contribution and income-percentage rules. It is a credit, not a subtraction. | https://www.oregon.gov/dor/programs/individuals/pages/credits.aspx |
| 2025 kicker | 9.863% of qualifying 2024 Oregon personal income tax liability, using the worksheet and status-change rules. This is not a 2026 recurring credit. | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf |
| 2026 individual estimated-payment trigger | Generally at least $1,000 tax after withholding and all credits, with required-payment tests. | https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf |
| 2026 regular estimate alternatives | Lesser of 90% current-year tax after all credits or 100% qualifying prior-year tax after all credits, less withholding; annualized method is separate. | https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf |

ITIN users cannot simply claim federal EITC. Oregon's earned income credit for ITIN filers has its own eligibility and calculation; use its worksheet before claiming a state equivalent. Federal numerical limits remain with `us-child-tax-credit-and-eitc`, and ITIN procedure with `us-itin-form-w-7`. Do not treat all self-employment income as automatically eligible earned income. [DOR credits, ITIN EIC](https://www.oregon.gov/dor/programs/individuals/pages/credits.aspx).

The 2025 higher-education savings contribution deadline is the earlier of filing the return or its unextended due date, including qualifying contributions made after year-end. Compute its income-based percentage, not simply every contribution up to the maximum; ABLE is a separate qualifying account credit. K-12 withdrawals have separate Oregon treatment. Contributions and distributions must be documented. [DOR credits](https://www.oregon.gov/dor/programs/individuals/pages/credits.aspx); [OR-40 p.4](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

For the 2025 kicker, file 2024 first and establish a qualifying 2024 tax liability before filing 2025. The base is Oregon tax before payments/credits other than the mutually-taxed other-state credit. Same-status/same-spouse taxpayers generally multiply that base by the stated percentage. Joint-to-separate, separate-to-joint and spouse changes require worksheet allocation/combination, not the entire joint amount twice. The return permits claiming all or donating all to the State School Fund; the election becomes irrevocable after the return due date including extensions. [OR-40 pp.18-20](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

### 5. Estimates, locality and filing workpaper

For ordinary 2026 estimates use the source's lesser required annual payment, subtract expected withholding, then split the remaining requirement across the applicable installment dates. Prior-year safe harbor requires a qualifying non-short prior year and filing that return before the current return. There is no imported federal high-income percentage here. Uneven earnings require the OR-10 annualized worksheet; farming/fishing exceptions require their own gross-income and filing/payment tests. Recompute remaining installments when facts change. [2026 estimate pp.1-6](https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf).

Calendar-year 2026 ordinary estimated installments are April 15, June 15, September 15, 2026 and January 15, 2027. First becoming subject later in the year changes the installment pattern. A full qualifying payment with a return by the source's January filing date can replace the last installment only if its conditions are met. Use the actual installment calendar and retain allocation of joint/separate payments. [2026 estimate pp.5-6](https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf).

Oregon has no general sales/use tax. That does not remove vehicle-specific taxes or another state's sales-tax nexus. For a Portland-area freelancer, separately screen TriMet/LTD self-employment transit, Metro SHS and Multnomah PFA on actual residence and business/source facts. Do not decide all local liabilities solely from residence, add a fabricated combined marginal rate, or apply employer payroll rates mechanically to net self-employment income. **Statewide transit tax does not tax self-employment income.** Its wage-based procedure belongs to `or-payroll`. [DOR sales tax](https://www.oregon.gov/dor/programs/businesses/pages/sales-tax.aspx); [transit publication p.2](https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf); [STT page](https://www.oregon.gov/dor/programs/businesses/pages/statewide-transit-tax.aspx).

## Boundary and exception table

| Facts | Treatment / next work |
|---|---|
| Federal taxable income supplied without AGI | Obtain AGI and schedules; do not add an Oregon deduction to that federal taxable figure. |
| Oregon return below tax-chart threshold | Use tax-table interval, not interpolated marginal tax. |
| 2026 planning figures | Keep publication/period labels; do not certify final 2026 return fields. |
| Federal taxable Social Security or Oregon refund | Subtract only amounts actually included in federal AGI; no double exclusion. |
| Another state's municipal interest / federal obligations | Determine eligible addition/subtraction and source documentation; no blanket bond label. |
| High-income exemption claimant | Apply cutoff, not an invented percentage phase-out. |
| Part-year/nonresident, registered domestic partners, military or foreign residence | Use appropriate separate instructions and allocations. |
| Local taxes, reduced business rate, PTET or CAT | Separate computations/owners; no combined guessed liability. |

## Worked cases

### Case 1: resident AGI bridge, 2025-2026 filing cycle

An invented single full-year resident has $90,000 federal AGI, $1,000 supported additions, $7,000 allowable federal tax liability subtraction, no other subtractions and the ordinary $2,835 Oregon deduction. Oregon taxable income is $81,165. Chart S gives $6,791.9375 before rounding and $6,792 whole-dollar tax. One eligible $256 exemption credit leaves $6,536 before other credits/payments. The input federal liability is already determined by the federal workpaper and confirmed eligible, not estimated from AGI. No kicker or business reduced-rate election is assumed.


```oa-check
name: Oregon resident AGI bridge 2025 cycle
inputs:
  agi: 90000
  additions: 1000
  allowed_federal_subtraction: 7000
  deduction: 2835
  exemption: 256
steps:
  - taxable: max(agi + additions - allowed_federal_subtraction - deduction, 0)
  - raw_tax: 4065 + (taxable - 50000) * 0.0875
  - whole_tax: round(raw_tax, 0)
  - net_tax: max(whole_tax - exemption, 0)
expected:
  taxable: 81165
  raw_tax: 6791.9375
  whole_tax: 6792
  net_tax: 6536
```

### Case 2: estimated-payment decision, actual 2026 rule

An invented full-year resident expects $6,000 tax after all credits, has qualifying $4,000 prior-year tax, and $2,000 expected withholding. Required annual payment is the lesser of $5,400 and $4,000. After withholding, $2,000 remains, ordinarily $500 each of four installments. An otherwise identical scenario with $3,500 withholding leaves $500, below the $1,000 trigger; no ordinary estimated installments are required under those facts. Neither computation decides late-payment interest without dated payments.


```oa-check
name: Oregon 2026 estimated-payment alternatives
inputs:
  current_tax_after_credits: 6000
  qualifying_prior_tax: 4000
  withholding: 2000
  alternative_withholding: 3500
steps:
  - required_annual: min(current_tax_after_credits * 0.9, qualifying_prior_tax)
  - remaining: max(required_annual - withholding, 0)
  - regular_installment: remaining / 4
  - alternative_remaining: max(required_annual - alternative_withholding, 0)
expected:
  required_annual: 4000
  remaining: 2000
  regular_installment: 500
  alternative_remaining: 500
```

### Case 3: kicker stays tied to its year

An invented taxpayer with unchanged filing/spouse status has a qualifying 2024 kicker base of $5,000. The 2025 credit is $493.15 before return rounding. A new 2026 liability of $7,000 does not replace the 2024 base for this credit.

```oa-check
name: Oregon 2025 kicker year lock
inputs:
  qualifying_2024_base: 5000
steps:
  - kicker: qualifying_2024_base * 0.09863
expected:
  kicker: 493.15
```

## When to refuse or refer

Refer incomplete domicile/source records, unresolved federal conformity or basis, OR-PTE/farm elections, multistate credits, local SHS/PFA/transit self-employment, PTET, CAT, estates/trusts, audits and material amendments. Report unresolved adjustments instead of assuming no difference. Payroll liability and individual income tax are separate workpapers.

## Filing and payment

The 2025-2026 filing-cycle OR-40 was due April 15, 2026. File electronically using a supported Oregon filing option or mail the correct year's signed return with required schedules/federal copy. Revenue Online payments and account messages are not by themselves an accepted income tax return. An extension to file does not extend payment. Retain acceptance, payment dates, account reconciliation and all credit worksheets. Detailed final 2026 filing date/extension fields and mailing instructions must be taken from the final year's instructions, not this prior-cycle map. [OR-40 pp.8-10,25-29](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf).

Late tax/filing and estimated underpayment are separate computations. The 2025 instructions state annual interest of 9% for 2025 and 8% for 2026; do not charge the older annual rate to an entire balance crossing the year boundary. The complete penalty/interest timing calculation and OR-10 underpayment exceptions need the appropriate year's instructions and dated payments. [OR-40 p.17, penalty/interest sections](https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf); [2026 estimate](https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf).

## Completion checklist

- Identify resident status, correct form and actual period.
- Tie federal AGI and Oregon adjustments to schedules; take Oregon deduction once.
- Separate final 2025-cycle tables from 2026 planning figures and payroll formulas.
- Test credits, income cutoffs, kicker year and alternative methods.
- Reconcile estimates/withholding and each actual payment date.
- Produce a brief with filing/payment evidence, referrals and unresolved issues.

## Sources

| Official source / section read | URL | Read on |
|---|---|---|
| DOR 2025 Form OR-40 instructions, pp.4,6-10,12-20,30-32; 2025-2026 filing cycle. Read for resident gates, AGI bridge, deductions, federal liability worksheet, final tax tables/charts, credits and kicker. | https://www.oregon.gov/dor/forms/FormsPubs/form-or-40-inst_101-040-1_2025.pdf | 2026-11-13 |
| DOR 2026 Publication OR-ESTIMATE, all six pages, early estimated indexed figures. Read for actual payment trigger, prior/current-year alternatives, installment calendar and estimate-only rate charts. | https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf | 2026-11-13 |
| DOR 2026 Combined Payroll Tax Report, p.4. Read for later published 2026 ordinary individual standard deductions, superseding provisional estimate deductions. | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | 2026-11-13 |
| DOR Credits page, personal exemption, EIC/ITIN and education savings sections. Read for 2025 credit conditions, credit versus subtraction, contribution deadline. | https://www.oregon.gov/dor/programs/individuals/pages/credits.aspx | 2026-11-13 |
| DOR Sales Tax in Oregon. Read for absence of general sales/use tax and vehicle-tax exception. | https://www.oregon.gov/dor/programs/businesses/pages/sales-tax.aspx | 2026-11-13 |
| DOR transit payroll publication, p.2. Read for separate self-employment district tax routing. | https://www.oregon.gov/dor/forms/FormsPubs/transit-payroll-taxes_211-503.pdf | 2026-11-13 |
| DOR Statewide Transit Tax page. Read for self-employment exclusion and separate wage tax. | https://www.oregon.gov/dor/programs/businesses/pages/statewide-transit-tax.aspx | 2026-11-13 |

Not yet confirmed: final 2026 OR-40/OR-40-N/OR-40-P instructions, final tax tables, exemption credit and complete federal-liability subtraction phase-out; reconciliation of early 2026 estimated credit with the later payroll allowance (different computations, not assumed interchangeable); complete 2026 federal conformity/OBBBA, bonus/section 179/174A and asset adjustments; full filing-threshold/dependent/age/blindness tables; detailed other-state credit, federal-obligation codes and fiscal-year federal allocation; ITIN EIC worksheet; final 2026 education savings credit; OR-PTE/farm reduced-rate calculations, PTET, local SHS/PFA/self-employment transit rates and geographic rules; complete late-filing/payment penalty and interest timing. Unsupported older local rates, combined marginal-rate claims, automatic bonus addbacks and 529 subtractions are withdrawn as usable rules.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `or-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/or-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
