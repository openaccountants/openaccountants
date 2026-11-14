---
name: ne-income-tax
description: "Nebraska 2026 resident wage and sole-proprietor computation: federal AGI adjustments, state deduction, $176 exemption credit, final bands, federal-tax limit and 1040N estimates. Load us-tax-workflow-base first."
version: "0.2"
jurisdiction: US-NE
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: state-tax
type: computation
---

# Nebraska individual income tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Nebraska uses 2026 rates of 2.46%, 3.51% and 4.55%, with four published bands because the upper two now share the same rate. Nebraska has its own standard deduction and a $176 credit per eligible personal exemption. The old assertion that no state deduction exists was wrong. [final 2026 calculation schedule](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/2026_tax_calculation_schedule.pdf); [final 2026 Form 1040N](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf).

## Scope

Ordinary full-year Nebraska residents with wages, sole-proprietor/disregarded single-member LLC profit, interest, rents and gains. Partial-year/nonresident allocation, complex K-1, asset/NOL and special credit work remain partial. Corporate and employer owners are `ne-corporate-tax` and `ne-payroll`. Load existing `us-form-1040-individual-return`, `us-schedule-c-and-se-computation`, `us-section-179-and-bonus-depreciation`, `us-self-employed-health-insurance`, `us-self-employed-retirement` and `us-qbi-deduction` for federal computations; do not restate federal tax figures here.

## Ask the client first

1. Domicile, permanent home, move dates, days/work in other states, federal filing status and resident-return eligibility?
2. Completed federal AGI and federal tax liability, wages/Schedule C/K-1/rental/gain statements and prior Nebraska returns?
3. Age/blindness, taxpayer/spouse dependent status, eligible dependents and federal deduction actually allowed/itemized expenses?
4. Bond issuers, state-tax refunds, Social Security/RRB/military or civil-service retirement, state depreciation/research/NOL records and any PTE election?
5. Other-state returns/tax paid, credit certification, Nebraska withholding, estimates, prior-year liability/AGI and extension evidence?

## The method, step by step

1. **Establish period and resident route.** Use the actual 2026 return and federal filing status. This computation assumes a full-year resident; move-date, military, nonresident and Schedule III cases require allocation review. Resident tax begins with federal AGI, not federal taxable income. Completed federal Schedule C, half-SE-tax, qualifying health-insurance and retirement deductions are already in AGI; do not deduct them again. QBI is below AGI. [1040N lines 1-5](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf); [77-2715(1)-(3)](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2715).
2. **Reconcile Nebraska adjustments.** Add non-Nebraska state/local-bond interest excluded federally and apply required related-expense reductions. Subtract qualifying U.S.-obligation interest and qualifying investment-company portions only when included in federal income and exempt under the governing rule. Subtract state income-tax refunds included in AGI where the statutory Nebraska-disallowance condition is met. Social Security benefits included in federal AGI are **100% subtracted from 2024 onward**, including 2026. RRB and qualifying military/civil-service amounts have separate supporting-document requirements; do not subtract all pensions by label. [77-2716(1),(3),(14),(15),(20)](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2716); [2026 Schedule I](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n_schs.pdf).
3. **Reconcile state business deductions.** The old blanket bonus-addback statement is not a current-year rule: section 77-2716(9)-(10) expressly concerns historical pre-2006 assets/years. Current qualified-property/improvement-property and research deductions require section 77-27,242 and Form 27242 reconciliation; no duplicate federal/state deduction. The final 2026 Schedule I separately lists related federal additions and Nebraska deductions. Stop for unresolved elections, basis, NOL or conformity rather than applying an old addback percentage. [historical depreciation provisions](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2716); [77-27,242](https://nebraskalegislature.gov/laws/statutes.php?statute=77-27,242); [Schedule I lines 13-14 and 47-48](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n_schs.pdf).
4. **Deduct the correct state amount.** Basic 2026 deductions are below. The standard deduction is limited by the federal deduction actually allowed; dependency and age/blindness can change it. If federal itemization applies, compare the eligible state standard amount with federal itemized deductions **less state/local income taxes before federal disallowance**, under the statute. The final form shows this comparison on lines 6-10. Taxable income = max(0, federal AGI - allowed Nebraska deduction + additions - subtractions). [77-2716.01(3)-(4)](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2716.01); [1040N lines 6-14](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf).
5. **Compute tax, credits, federal limit and settlement.** Use the final 2026 calculation schedule, then applicable state other taxes. Form 1040N line 16 calculates 29.6% of the specified federal lump-sum/early-distribution tax amounts; ordinary wage examples below assume none. Personal exemption credit = $176 x eligible count, applied as a nonrefundable credit, not an income deduction. Substantiate other credits. A federal-before-credit liability cap can apply under 77-2715(1). The opened **2025-2026 filing cycle** worksheet tests **net adjustments (additions minus subtractions) below $5,000**, then compares state tax after nonrefundable credits with its specified federal-tax result. Final 2026 worksheet details were not found; stop if the cap could reduce tax, rather than treating gross additions alone or an arbitrary federal-tax number as the test. Then reconcile withholding, estimates, refundable credits, use tax and any penalty. [1040N lines 16-60](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf); [77-2715(1)](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2715).

## Rates, bands and thresholds

Use Nebraska taxable income T and the exact official base-tax amounts. Although upper rates match, the published band bases include rounding; use the appropriate row rather than silently merging bands. [final 2026 schedule](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/2026_tax_calculation_schedule.pdf).

| Status | First band | Second band | Third band | Fourth band | Authority |
| --- | --- | --- | --- | --- | --- |
| Single / MFS | T through $4,130: .0246T | $4,130 through $24,760: $101.60+.0351(T-4,130) | $24,760 through $39,900: $825.71+.0455(T-24,760) | Above $39,900: $1,514.58+.0455(T-39,900) | [2026 schedule](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/2026_tax_calculation_schedule.pdf) |
| MFJ / qualifying surviving spouse | T through $8,250: .0246T | $8,250 through $49,530: $202.95+.0351(T-8,250) | $49,530 through $79,800: $1,651.88+.0455(T-49,530) | Above $79,800: $3,029.16+.0455(T-79,800) | [2026 schedule](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/2026_tax_calculation_schedule.pdf) |
| HOH | T through $7,700: .0246T | $7,700 through $39,620: $189.42+.0351(T-7,700) | $39,620 through $59,160: $1,309.81+.0455(T-39,620) | Above $59,160: $2,198.88+.0455(T-59,160) | [2026 schedule](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/2026_tax_calculation_schedule.pdf) |

| 2026 item | Amount/condition | Authority |
| --- | --- | --- |
| Basic standard deduction, single/MFS | $8,850, subject to dependency/federal-amount limit | [1040N line 6](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf) |
| Basic standard deduction, MFJ/QSS | $17,700, subject to eligibility | [1040N line 6](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf) |
| Basic standard deduction, HOH | $12,950, subject to eligibility | [1040N line 6](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf) |
| Personal exemption credit | $176 each eligible taxpayer/spouse/dependent; nonrefundable | [1040N lines 4/18](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf) |
| 2026 estimates ordinary trigger | $500 or more expected balance after withholding/credits; worksheet/safe-harbor conditions apply | [2026 estimates](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2025/f_1040N-ES.pdf) |

## Boundary table

| Fact | Treatment or stopping point |
| --- | --- |
| Age/blind or dependent deduction | The 2026 estimate booklet provides additional Nebraska age/blind amounts of $2,050 per condition for unmarried and $1,700 for married, with detailed spouse rules. Apply the federal-amount limit and final-return instructions; do not substitute federal amounts. Final 2026 full instructions/dependent worksheet were not found. [2026 estimate booklet p.5](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2025/f_1040N-ES.pdf); [77-2716.01](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2716.01). |
| Other-state income | Schedule II is the full-year-resident other-state credit, not a generic credits list. Credit is the least of total Nebraska tax, proportional Nebraska tax on qualifying income and tax actually due/paid to the other state; attach its complete return and use the conversion chart. Withholding is not the other state's tax. [2026 Schedule II](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n_schs.pdf). |
| Federal business/hobby or community-property facts | Use the completed federal result and correct federal allocation owner. Nebraska-specific hobby/community-property assertions in the old text were not independently reverified; do not create state rules from them. |
| Incentives / PTE / special capital gain | Nebraska Advantage and other credits need actual certification and current limits. K-1/PTET, special capital-gain election and asset-basis/NOL computations require specialist review, not automatic ordinary-income treatment. |
| Local income / inheritance | The old no-local-income-tax assertion was not reverified. County inheritance/property and estate/trust matters remain outside this computation; do not infer their absence from this skill. |
| Later year | The statute separately provides 2027 rates. Do not use them on 2026 taxable income. [77-2715.03(2)](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2715.03). |

## Worked cases

### Single wage earner

Single full-year resident, under 65, not blind/dependent, $60,000 federal AGI, no adjustments/itemization/other tax or credits beyond one personal exemption, and $2,000 withholding. The federal liability limit is assumed not to reduce the result. Taxable income is $51,150; gross state tax is $2,026.455; after the $176 credit, $1,850.455, leaving $149.545 illustrated overpayment before final whole-dollar return rounding.

```oa-check
name: NE resident wages 2026
inputs:
  agi: 60000
  withheld: 2000
steps:
  - taxable: max(0, agi - 8850)
  - gross: 1514.58 + (taxable - 39900) * 0.0455
  - tax: max(0, gross - 176)
  - overpayment: withheld - tax
expected:
  taxable: 51150
  gross: 2026.455
  tax: 1850.455
  overpayment: 149.545
```

### Joint return with Social Security already in federal AGI

MFJ full-year residents, both under 65, not blind/dependents, federal AGI $90,000 including $10,000 taxable Social Security. No other adjustments, itemization, additional taxes or credits except two personal exemptions; the federal tax limit does not reduce the result. Subtract only the $10,000 included in AGI. Taxable income is $62,300; gross tax $2,232.915, less $352 credit gives $1,880.915 before final return rounding.

```oa-check
name: NE joint taxable Social Security subtraction 2026
inputs:
  agi: 90000
  included_ss: 10000
  exemptions: 2
steps:
  - taxable: max(0, agi - included_ss - 17700)
  - gross: 1651.88 + (taxable - 49530) * 0.0455
  - credit: exemptions * 176
  - tax: max(0, gross - credit)
expected:
  taxable: 62300
  gross: 2232.915
  credit: 352
  tax: 1880.915
```

## When to refuse or refer

Refer disputed residence, part-year/nonresident Schedule III, complex other-state conversion, K-1/PTE, depreciation/research/NOL and certified incentive work, unresolved federal-liability limits, fiduciary/estate/inheritance and corporate matters. Amended returns use current 1040N with the Amended Return box, not an assumed old 1040XN route; this skill does not prepare them. [2026 amended-return page](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf).

## Filing and payment

The final 2026 form map replaces the old incorrect lines: AGI 5; state standard 6; itemized 7-9; selected deduction 10; additions 12/subtractions 13; taxable 14; tax 15/other 16; resident exemption credit 18; other-state credit 19; wages/other/K-1 withholding 36-38; PTET 39; estimates 40; total payments 54; use tax 59; due 60/overpayment 61. Schedule I holds adjustments; II is other-state credit; III is nonresident/partial-year computation. [2026 Form 1040N](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf); [2026 schedules](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n_schs.pdf).

The **2025-2026 filing cycle** booklet states the recurring April 15 calendar-year filing date; final 2027 calendar relief and full 2026 instructions remain unconfirmed. Current Form 4868N grants up to six months to file, with federal-extension and paid-preparer-e-file waiver conditions; otherwise file the state application by the original date. Payment is not extended and unpaid tax accrues interest. [2025 booklet, filing procedures](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2025/f_Individual_Income_Tax_Booklet.pdf); [current 4868N instructions](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_4868n.pdf).

Use the actual **2026** Form 1040N-ES booklet despite its 2025 directory: ordinary dates April 15, June 15, September 15, 2026 and January 15, 2027, subject to weekend/holiday relief. Required annual amount generally compares 90% current tax with 100% prior-year tax for a full 12-month year, increased to 110% when prior-year AGI exceeds $150,000 ($75,000 MFS per worksheet). Farming/ranching/fishing, first-time filers, no-prior-liability and annualization rules differ. Do not use the 2027 estimate form merely because its directory says 2026. [2026 estimate instructions/worksheet](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2025/f_1040N-ES.pdf).

## Completion checklist

Confirm resident/status and actual 2026 sources; reconcile AGI/deduction/state adjustments; count eligible exemptions; apply other tax and federal-liability limit where required; substantiate other-state/other credits; reconcile payments/use tax; resolve every partial area and filing-calendar gap before filing.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| Final 2026 calculation schedule; read for all four status-specific bands and official base amounts. | https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/2026_tax_calculation_schedule.pdf | 2026-11-13 |
| 77-2715.03; read for 2026 versus neighboring 2025/2027 rates and statutory indexing. | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2715.03 | 2026-11-13 |
| Final 2026 Form 1040N, updated October 15; read for deduction/exemption values, line map, other tax and amended-return route. | https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf | 2026-11-13 |
| Final 2026 Schedules I-II-III; read for adjustment lines, other-state credit and nonresident routing. | https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n_schs.pdf | 2026-11-13 |
| 77-2716.01; read for state deduction/federal cap, itemized income-tax exclusion, eligibility and indexing. | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2716.01 | 2026-11-13 |
| 77-2716; read for bond/refund/benefit modifications and neighboring historical depreciation provisions. | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2716 | 2026-11-13 |
| 77-27,242; read for state qualified-property/research deductions and no duplicate federal deduction. | https://nebraskalegislature.gov/laws/statutes.php?statute=77-27,242 | 2026-11-13 |
| 77-2715; read for resident/nonresident tax and federal-liability limitation. | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2715 | 2026-11-13 |
| 2026 Form 1040N-ES, in 2025 directory; read for trigger, safe harbor, dates, special cases and additional state deductions; not final-return rate authority. | https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2025/f_1040N-ES.pdf | 2026-11-13 |
| Current Form 4868N; read for application/waiver conditions, six-month filing extension and payment interest. | https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_4868n.pdf | 2026-11-13 |
| 2025 booklet, 2025-2026 filing cycle; read for recurring filing procedure only; not 2026 amount/line authority. | https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2025/f_Individual_Income_Tax_Booklet.pdf | 2026-11-13 |
| DOR individual form index; read for current general booklet still 2025. | https://revenue.nebraska.gov/about/forms/individual-income-tax-forms | 2026-11-13 |
| DOR 2026 final forms index; read for actual final 2026 individual form/schedule publication. | https://revenue.nebraska.gov/tax-professionals/2026-final-income-tax-forms | 2026-11-13 |

Not yet confirmed: full 2026 return instructions/dependent deduction and federal-tax-liability worksheet, final 2027 calendar relief; specialized asset/PTE/NOL/credit and nonresident calculations; legacy no-local-income/community-property/hobby and county inheritance details. No 2025 rate, credit or deduction is projected into 2026.
