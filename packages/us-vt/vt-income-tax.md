---
name: vt-income-tax
description: Use this skill whenever asked about Vermont individual income tax, Vermont Form IN-111, Vermont graduated tax rates, Vermont self-employment income tax at the state level, Vermont earned income tax credit, or any Vermont personal income tax question for sole proprietors. Trigger on phrases like "Vermont income tax", "VT income tax", "Form IN-111", "Vermont tax brackets", "Vermont 8.75%", "32 V.S.A. Chapter 151", or any request involving Vermont state individual income tax computation or filing.
version: "0.3"
jurisdiction: US-VT
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
category: state-tax
---

# Vermont individual income tax: 2026 framework and 2025-2026 filing-cycle figures

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. General reference for AI-assisted working papers. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider all relevant facts and circumstances; do not assume missing facts or base advice on audit risk.

**Answer first.** Vermont starts from federal adjusted gross income and uses its own indexed deductions, exemptions and graduated bands. The final 2026 individual rate schedule was not available at its expected official URL when checked. The retained figures and worked cases below are **2025-2026 filing cycle** reference only. They must not be presented as 2026 indexed amounts. Current 2026 capital-gain changes are separately sourced below.

## Scope

Full-year Vermont resident individuals, including wages, sole proprietors and individual owners of disregarded LLCs. Nonresident/part-year IN-113 allocations are referred. Corporate income uses `vt-corporate-tax`, employer withholding/UI uses `vt-payroll`, sales/use uses `vt-sales-tax`. Federal Schedule C, SE, QBI, health-insurance and retirement limits remain in their federal skills; no federal indexed figures are repeated.

## Ask the client first

1. Exact tax year, filing status, dependent status, age/blindness boxes and spouse's income.
2. Domicile, permanent home and day count; Vermont and other-state work/source records.
3. Federal AGI, US-obligation interest, non-Vermont municipal interest and state depreciation schedules.
4. Capital-gain asset, acquisition/sale dates, qualified-small-business-stock exclusion and previous Vermont basis adjustments.
5. Eligible children, care costs, federal credits, charitable gifts and other-state tax.
6. Vermont estimates, withholding, self-employment location and prior-year tax.

## The method, step by step

### Current law changes applicable in 2026

Under [32 V.S.A. 5811(21)(A)(v) and (B)(ii)](https://legislature.vermont.gov/statutes/section/32/151/05811), 2026 adds back income/gain excluded federally as qualified small business stock under section 1202(a). Such added gains may enter the Vermont capital-gain exclusion notwithstanding the usual financial-instrument restriction; the adjusted net gain, AGI and taxable-income amounts used for that exclusion must include the add-back. The statute retains the choice of a USD 5,000 exclusion or qualifying 40% exclusion subject to the statutory asset, holding-period and cap conditions. Do not merely copy the pre-2026 stock exclusion result.

Current [5811(21)(A)(iv), (B)(viii)-(x)](https://legislature.vermont.gov/statutes/section/32/151/05811) also distinguishes eligible small-business research expensing from noneligible taxpayer add-backs and historical-amortization subtractions, with transition elections and recovery limits. Obtain the eligibility and prior-year expenditure schedules before applying a federal research deduction to the Vermont base.

Resident status in [5811(11)](https://legislature.vermont.gov/statutes/section/32/151/05811) includes domicile or a permanent abode plus **more than** 183 days, correcting the old 183-or-more shorthand. Current statutory minimum tax under [5822(a)(6)](https://legislature.vermont.gov/statutes/section/32/151/05822) applies when federal AGI exceeds USD 150,000: compare regular tax with 3% of federal AGI, with the published form's US-obligation treatment separately checked. The read 2025 form subtracts US-obligation interest for this comparison; final 2026 instructions remain unconfirmed.

### Rates, bands and thresholds: verified 2025-2026 filing cycle only


All bracket amounts below are verified **2025-2026 filing cycle** amounts, not confirmed 2026 brackets, from the 2025 Vermont Tax Rate Schedules. Vermont indexes them each year. The Department's instructions say to use the tax tables when Vermont taxable income is under $75,000; do not substitute a continuous-band approximation when the published tables are required.

### Tax brackets -- Single filers (2025, Schedule X)

**Single filer brackets**

| Vermont taxable income | Marginal rate | Source |
| --- | --- | --- |
| $0 - $49,400 | 3.35% | https://tax.vermont.gov/sites/tax/files/documents/TaxRateSched-2025.pdf |
| $49,400 - $119,700 | 6.60% | same |
| $119,700 - $249,700 | 7.60% | same |
| Over $249,700 | 8.75% | same |

### Tax brackets -- Married filing jointly / qualifying widow(er) (2025, Schedule Y-1)

**MFJ brackets**

| Vermont taxable income | Marginal rate | Source |
| --- | --- | --- |
| $0 - $82,500 | 3.35% | https://tax.vermont.gov/sites/tax/files/documents/TaxRateSched-2025.pdf |
| $82,500 - $199,450 | 6.60% | same |
| $199,450 - $304,000 | 7.60% | same |
| Over $304,000 | 8.75% | same |

### Tax brackets -- Married filing separately (2025, Schedule Y-2)

**MFS brackets**

| Vermont taxable income | Marginal rate | Source |
| --- | --- | --- |
| $0 - $41,250 | 3.35% | https://tax.vermont.gov/sites/tax/files/documents/TaxRateSched-2025.pdf |
| $41,250 - $99,725 | 6.60% | same |
| $99,725 - $152,000 | 7.60% | same |
| Over $152,000 | 8.75% | same |

### Tax brackets -- Head of household (2025, Schedule Z)

**HOH brackets**

| Vermont taxable income | Marginal rate | Source |
| --- | --- | --- |
| $0 - $66,200 | 3.35% | https://tax.vermont.gov/sites/tax/files/documents/TaxRateSched-2025.pdf |
| $66,200 - $171,000 | 6.60% | same |
| $171,000 - $276,850 | 7.60% | same |
| Over $276,850 | 8.75% | same |

Rate schedule base tax at each threshold (2025, source 1): Single $1,655.00 at $49,400, $6,295.00 at $119,700, $16,175.00 at $249,700. MFJ $2,764.00 at $82,500, $10,482.00 at $199,450, $18,428.00 at $304,000. MFS $1,382.00 at $41,250, $5,241.00 at $99,725, $9,214.00 at $152,000. HOH $2,218.00 at $66,200, $9,135.00 at $171,000, $17,179.00 at $276,850.

### Key thresholds

**Key thresholds table**

| Item | Amount (2025) | Source |
| --- | --- | --- |
| Starting point | Federal adjusted gross income (IN-111 Line 1) | https://tax.vermont.gov/sites/tax/files/documents/IN-111-Instr-2025.pdf |
| Vermont standard deduction | Single $7,650; MFJ / QW $15,300; MFS $7,650; HOH $11,450; plus $1,250 per federal age 65 / blind box | https://tax.vermont.gov/sites/tax/files/documents/IN-111-Instr-2025.pdf (Line 4) |
| Vermont personal exemption | $5,300 per exemption | https://tax.vermont.gov/sites/tax/files/documents/IN-111-Instr-2025.pdf (Line 5 e) |
| Minimum tax | If federal AGI > $150,000, tax is the greater of the schedule tax or 3% of federal AGI less US obligation interest | https://legislature.vermont.gov/statutes/section/32/151/05822 |
| Charitable contribution credit | 5% of the first $20,000 of contributions (max $1,000), nonrefundable | https://tax.vermont.gov/sites/tax/files/documents/IN-111-Instr-2025.pdf (Lines 11-13) |
| Child Care Contribution | 0.11% of Vermont-source net self-employment earnings (Schedule SE Line 6) | https://tax.vermont.gov/sites/tax/files/documents/IN-111-Instr-2025.pdf (Line 21) |
| Filing deadline | Same as the federal original due date (April 15, 2026 for TY 2025) | https://legislature.vermont.gov/statutes/section/32/151/05861 |
| Extension | To the federal extended date (Oct. 15, 2026) if a federal extension was granted; Form IN-151 only if paying | https://legislature.vermont.gov/statutes/section/32/151/05868 |
| Estimated tax safe harbour | Lesser of 90% of current-year tax or 100% of prior-year tax; no penalty if tax due less withholding is under $500 | https://legislature.vermont.gov/statutes/section/32/151/05851 and https://tax.vermont.gov/sites/tax/files/documents/IN-111-Instr-2025.pdf (Line 31) |
| VT Earned Income Tax Credit | 38% of federal EITC with qualifying children; 100% with no qualifying children (refundable) | https://legislature.vermont.gov/statutes/section/32/151/05828b |
| VT Child and Dependent Care Credit | 72% of the federal credit (refundable) | https://legislature.vermont.gov/statutes/section/32/151/05828c |
| VT Child Tax Credit | $1,000 per qualifying child aged 6 or under (refundable, phases out by income) | https://legislature.vermont.gov/statutes/section/32/151/05830f |
| Use tax rate | 6% | https://tax.vermont.gov/sites/tax/files/documents/IN-111-Instr-2025.pdf (Line 22) |



### Compute the return using the correct year's final documents

#### How this skill works with the federal return

Vermont starts from **federal adjusted gross income** (Form 1040, Line 11), not federal taxable income. Vermont applies its own standard deduction and personal exemptions; the federal standard or itemized deduction and the federal QBI deduction do not carry over.

**Flow (2025 Form IN-111):**
1. Federal Form 1040 is completed (including Schedule C, SE, and all adjustments to income).
2. Federal AGI flows to Form IN-111, Line 1.
3. Net modifications from Schedule IN-112, Part I go on Line 2 (additions such as non-Vermont state and local bond interest and bonus depreciation; subtractions such as US obligation interest and the capital gains exclusion).
4. Line 4 is the Vermont standard deduction; Line 5 e is $5,300 per personal exemption.
5. Line 7 is Vermont taxable income (Line 3 minus Line 6, not below zero).
6. Line 8 is the tax from the rate schedule or tax table, or the 3% minimum tax if federal AGI exceeds $150,000 and that is higher.
7. Nonrefundable credits (charitable credit, credit for tax paid to other states, IN-119 credits) reduce the tax; the Child Care Contribution and use tax are added; refundable credits (EITC, child and dependent care credit, child tax credit) go on Line 26 c via Schedule IN-112, Part II.

**Key structural point:** Because Vermont starts from federal AGI, the federal QBI deduction (§199 A) gives no Vermont benefit, and the federal standard or itemized deduction is replaced by the Vermont standard deduction and exemptions.

#### Self-employed specific rules

#### Self-employment tax deduction

- **Self-employment tax deduction** -- The federal deduction for the deductible share of self-employment tax (see `us-schedule-c-and-se-computation`) reduces federal AGI and so flows through to Vermont automatically.

#### Retirement contributions

- **Retirement contributions** -- SEP-IRA, SIMPLE IRA and solo 401(k) contributions reduce federal AGI and flow through automatically.

#### Health insurance deduction

- **Health insurance deduction** -- The self-employed health insurance deduction reduces federal AGI and flows through automatically.

#### QBI deduction (§199 A)

- **QBI deduction (§199 A)** -- No Vermont effect. The QBI deduction is taken after federal AGI, and Vermont starts from federal AGI.

#### Home office deduction

- **Home office deduction** -- Reduces Schedule C net profit, so it reduces federal AGI and flows through.

#### Child Care Contribution

- **Child Care Contribution** -- Individuals with Vermont-source self-employment income pay 0.11% of net earnings from self-employment (Schedule SE, Line 6, less earnings for work performed outside Vermont) on IN-111, Line 21.

#### Estimated tax payments

- **Estimated tax payments** -- Pay 90% of current-year tax or 100% of prior-year tax to avoid underpayment charges; no penalty applies if the tax due less withholding is under $500. Due dates follow federal: April 15, June 15, September 15, January 15 (Form IN-114).

#### Computation rules

- **Tax computation** -- Apply the graduated rate schedule (or tax table under $75,000) to Vermont taxable income for the filing status. If federal AGI exceeds $150,000, Line 8 is the greater of that tax and 3% of federal AGI less interest from US obligations.
- **Starting point** -- Begin with federal adjusted gross income from Form 1040. Enter on Form IN-111, Line 1.
- **Deductions** -- Subtract the Vermont standard deduction (Single $7,650; MFJ $15,300; MFS $7,650; HOH $11,450; plus $1,250 per federal age 65 / blind box) and $5,300 per personal exemption.
- **Vermont additions (Schedule IN-112, Part I)** -- Common additions: state and local bond interest from non-Vermont issuers; federal bonus depreciation under IRC §168(k) or (n) (32 V.S.A. §5811(21)(A)).
- **Vermont subtractions (Schedule IN-112, Part I)** -- Common subtractions: interest from US government obligations; Vermont depreciation on bonus-depreciation property; and for TY 2025 the capital gains exclusion (32 V.S.A. §5811(21)(B)(ii)): either the first $5,000 of adjusted net capital gain, or 40% of adjusted net capital gain from assets held more than three years, capped at the lesser of 40% of federal taxable income or $350,000. The 40% option excludes gains on residences, publicly traded stocks and bonds and other financial instruments, and depreciable personal property other than farm property and standing timber.
- **Vermont Earned Income Tax Credit** -- 38% of the federal EITC for a filer with qualifying children; 100% for a filer with no qualifying children. Refundable; claimed on Schedule IN-112, Part II.
- **Filing due date** -- The federal original due date (April 15, 2026 for TY 2025). A federal extension extends the Vermont return to the federal extended date (October 15, 2026); Form IN-151 is needed only when making an extension payment. Payment is still due by April 15.
- **Estimated tax payments** -- Required annual payment is the lesser of 90% of current-year tax or 100% of prior-year tax. Quarterly due dates: April 15, June 15, September 15, January 15. Form IN-114 (voucher).
- **Use tax reporting** -- Form IN-111, Line 22 reports use tax (6%) on taxable out-of-state, online, phone or mail-order purchases. Businesses report use tax on Form SUT-451 or SU-452 instead.

#### Conditions requiring judgment

- **Residency determination** -- Vermont defines a resident as a person domiciled in Vermont or maintaining a permanent home in Vermont and spending more than 183 days there. Domicile requires intent analysis. Freelancers splitting time between VT and another state need careful documentation.
- **Bonus depreciation add-back** -- Vermont requires add-back of federal §168(k) bonus depreciation and allows the depreciation that would have been allowed without bonus. This creates timing differences. Reviewer must track the Vermont depreciation schedule separately and ensure proper subtraction in subsequent years.
- **Capital gains exclusion** -- Choosing between the flat $5,000 exclusion and the 40% exclusion needs a holding-period and asset-type review (see T 1-VT-5). The 2026 version is addressed in the current-law section above; qualified-small-business-stock gains added back under the new rule enter that exclusion analysis.
- **Multi-state credit** -- Vermont allows a credit for income taxes paid to other states or Canadian provinces (Schedule IN-117, one per state). The credit is the lesser of: (a) tax paid to the other state, or (b) Vermont tax attributable to the income taxed by the other state.
- **Renter credit / property tax credit** -- Vermont offers a property tax credit (via HS-122) and renter credit for eligible residents. Income limits and homestead value limits apply. These interact with overall VT tax liability.

#### Supplier pattern library

**Supplier pattern library table**

| Income/deduction type | Vermont treatment | Notes |
| --- | --- | --- |
| Schedule C net profit | Included via federal AGI | No adjustment |
| Self-employment tax deduction | Included via federal AGI | No adjustment |
| SEP/SIMPLE/solo 401(k) | Included via federal AGI | No adjustment |
| QBI deduction (§199 A) | No Vermont effect | Taken below federal AGI |
| Self-employed health insurance | Included via federal AGI | No adjustment |
| Home office deduction | Included via Schedule C | No adjustment |
| Federal bonus depreciation (§168(k)) | Add back, substitute VT depreciation | Timing difference |
| US government bond interest | Subtract | Exempt from state tax |
| Non-Vermont state / municipal bond interest | Add back | Excluded federally, taxable in Vermont |
| Capital gains (assets held > 3 years) | $5,000 or 40% exclusion (TY 2025 rule) | Must verify asset type and cap |
| Vermont-source net SE earnings | Child Care Contribution 0.11% | IN-111 Line 21 |

#### Form mapping

**Form mapping table (2025 Form IN-111)**

| IN-111 Line | Description | Source |
| --- | --- | --- |
| Line 1 | Federal adjusted gross income | Form 1040 |
| Line 2 | Net modifications to federal AGI | Schedule IN-112, Part I |
| Line 3 | Federal AGI with modifications | Line 1 + Line 2 |
| Line 4 | Vermont standard deduction | Chart in instructions |
| Line 5 e | Personal exemptions x $5,300 | Computed |
| Line 7 | Vermont taxable income | Line 3 - Line 6 |
| Line 8 | Vermont income tax (schedule, table or 3% minimum) | Rate schedule |
| Line 9 | Net adjustment to Vermont tax | Schedule IN-119, Part I |
| Lines 11-13 | Charitable contribution credit (5%, max $1,000) | Computed |
| Line 17 | Credit for tax paid to other state or province | Schedule IN-117 |
| Line 18 | Vermont tax credits | Schedule IN-119, Part II |
| Line 21 | Child Care Contribution (0.11% of SE earnings) | Worksheet |
| Line 22 | Use tax | Use Tax Worksheet |
| Line 26 b | Estimated payments and extension payment | IN-114, IN-151 |
| Line 26 c | Refundable credits (EITC, child and dependent care, child tax credit) | Schedule IN-112, Part II |
| Line 31 | Underpayment interest and penalty | IN-152 / IN-152 A |



## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| 2026 indexed computation requested | Obtain final 2026 brackets, deductions and exemption before calculating; 2025 numbers below are not a forecast |
| 2026 qualified small business stock gain | Reconcile federal exclusion add-back and amended state gain exclusion |
| Federal bonus depreciation | Track the state add-back/substitute depreciation and recovery on disposition |
| Part-year/nonresident or other-state credit | IN-113/IN-117 allocation and credit caps need source working papers |
| Property/renter credit or estate | Separate applications/returns; no amount inferred from this skill |

## Worked cases

These original cases are deliberately preserved as **2025-2026 filing cycle**, not 2026 bracket illustrations. Case B is a decision between the ordinary schedule and the minimum-tax floor. Published base-tax amounts, rather than unrounded integral bands, govern these computations.



Example A: single filer, one personal exemption, federal AGI $100,000, no Vermont modifications. Vermont taxable income = 100,000 - 7,650 - 5,300 = 87,050. Schedule X: 1,655.00 + 6.6% x (87,050 - 49,400) = 4,139.90. Federal AGI is not over $150,000, so the minimum tax does not apply.

```oa-check
name: VT 2025 single, federal AGI 100,000
inputs:
  federal_agi: 100000
  standard_deduction: 7650
  exemptions: 1
steps:
  - vt_taxable: federal_agi - standard_deduction - exemptions * 5300
  - schedule_tax: 1655 + (vt_taxable - 49400) * 0.066
expected:
  vt_taxable: 87050
  schedule_tax: 4139.90
```

Example B: married filing jointly, four children (six exemptions), federal AGI $160,000, no modifications and no US obligation interest. Vermont taxable income = 160,000 - 15,300 - 6 x 5,300 = 112,900. Schedule Y-1: 2,764.00 + 6.6% x (112,900 - 82,500) = 4,770.40. Federal AGI exceeds $150,000, so the minimum tax is 3% x 160,000 = 4,800.00, and Line 8 is the greater, 4,800.00.

```oa-check
name: VT 2025 MFJ, AGI 160,000, minimum tax applies
inputs:
  federal_agi: 160000
  standard_deduction: 15300
  exemptions: 6
steps:
  - vt_taxable: federal_agi - standard_deduction - exemptions * 5300
  - schedule_tax: 2764 + (vt_taxable - 82500) * 0.066
  - minimum_tax: federal_agi * 0.03
  - line_8_tax: max(schedule_tax, minimum_tax)
expected:
  vt_taxable: 112900
  schedule_tax: 4770.40
  minimum_tax: 4800
  line_8_tax: 4800
```



## When to refuse or refer



**Refusal catalogue table**

| ID | Refusal | Reason |
| --- | --- | --- |
| R-VT-1 | Part-year resident return | Requires allocation computation (Schedule IN-113) |
| R-VT-2 | Nonresident return | Different sourcing rules (Schedule IN-113) |
| R-VT-3 | Vermont corporate income tax (Form CO-411) | Different tax type |
| R-VT-4 | Vermont estate tax | Different form and threshold analysis |
| R-VT-5 | Vermont meals and rooms tax | Separate tax system (9%) |
| R-VT-6 | Homestead declaration / property tax credit | Requires property valuation analysis |
| R-VT-7 | Amended returns | Requires additional procedures |
| R-VT-8 | Farm income averaging | Specialized computation |


## Filing and payment

[5861](https://legislature.vermont.gov/statutes/section/32/151/05861) ties the return to the federal original filing date, ordinarily April 15, 2027 for calendar 2026. [5868](https://legislature.vermont.gov/statutes/section/32/151/05868) grants the federal extended filing date when a federal extension exists, without extending payment. Use myVTax and retain acceptance and payment references. IN-151 is the read 2025-2026-cycle extension-payment voucher, not a basis for assuming final 2026 form lines.

Use IN-114 for individual estimates and the required annual payment in [5851](https://legislature.vermont.gov/statutes/section/32/151/05851); the statutory Vermont safe harbour is the lesser of 90% of current-year or 100% of qualifying prior-year tax. The read instructions use April 15, June 15, September 15 and January 15, with business-day adjustments. IN-152/IN-152 A handles underpayment; the read 2025-2026 cycle excludes balances below USD 500 after withholding. Confirm final 2026 form instructions, penalty and annually set interest before implementation.

## Completion checklist

- Correct year stated beside every indexed figure and worked case.
- AGI modifications, state deduction/exemptions and depreciation reconciled.
- Minimum tax and 2026 stock-gain add-back considered.
- Charitable/other-state/refundable credits supported and self-employed CCC addressed.
- Final current-year forms, estimates, withholding, acceptance and payment checked.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2025 Vermont Tax Rate Schedules, 2025-2026 filing cycle. Read for all filing-status bands, rounded base taxes, USD 75,000 table cutover and minimum-tax comparison. | https://tax.vermont.gov/sites/tax/files/documents/TaxRateSched-2025.pdf | 2026-11-13 |
| 2025 IN-111 instructions, 2025-2026 filing cycle. Read for AGI base, state deductions/exemptions, form mapping, CCC, use-tax routing, estimates and credits. | https://tax.vermont.gov/sites/tax/files/documents/IN-111-Instr-2025.pdf | 2026-11-13 |
| 32 V.S.A. 05822. Read for rates, indexing, minimum tax and charitable credit. | https://legislature.vermont.gov/statutes/section/32/151/05822 | 2026-11-13 |
| 32 V.S.A. 05811. Read for residence, state base, depreciation and capital-gain changes effective 2026. | https://legislature.vermont.gov/statutes/section/32/151/05811 | 2026-11-13 |
| 32 V.S.A. 05861. Read for filing obligation and federal due-date alignment. | https://legislature.vermont.gov/statutes/section/32/151/05861 | 2026-11-13 |
| 32 V.S.A. 05868. Read for federal extension and payment distinction. | https://legislature.vermont.gov/statutes/section/32/151/05868 | 2026-11-13 |
| 32 V.S.A. 05851. Read for required annual estimate payment. | https://legislature.vermont.gov/statutes/section/32/151/05851 | 2026-11-13 |
| 32 V.S.A. 05828 b. Read for EITC percentages, residency and identification-number exception. | https://legislature.vermont.gov/statutes/section/32/151/05828b | 2026-11-13 |
| 32 V.S.A. 05828 c. Read for refundable care-credit percentage and residency. | https://legislature.vermont.gov/statutes/section/32/151/05828c | 2026-11-13 |
| 32 V.S.A. 05830 f. Read for refundable child credit, age, phaseout and residency. | https://legislature.vermont.gov/statutes/section/32/151/05830f | 2026-11-13 |

Not yet confirmed: final 2026 indexed personal bands, standard/additional deductions, exemption amounts, tax tables and IN-111/IN-112 line mappings; minimum-tax US-obligation treatment on final 2026 form; 2026 underpayment interest/penalty implementation and child-credit advance-payment contingency. Expected TaxRateSched-2026.pdf returned 404; no 2026 indexed amount was guessed. The verified 2025 amounts remain only for the 2025-2026 filing cycle. Detailed homestead/renter, estate, amended-return and farm-averaging procedures remain outside scope.
