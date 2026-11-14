---
name: wi-income-tax
description: Use this skill whenever asked about Wisconsin individual income tax, Wisconsin Form 1, Wisconsin graduated tax rates, Wisconsin self-employment income tax at the state level, Wisconsin sliding-scale standard deduction, or any Wisconsin personal income tax question for sole proprietors. Trigger on phrases like "Wisconsin income tax", "WI income tax", "Wisconsin Form 1", "Wisconsin tax brackets", "Wisconsin 7.65%", "Wis. Stat. 71", or any request involving Wisconsin state individual income tax computation or filing.
version: "0.2"
jurisdiction: US-WI
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
category: state-tax
type: computation
---

# Wisconsin individual income tax, 2026

> **General reference only.** This skill produces a Wisconsin computation and filing brief for professional review. It has not been approved by an accountant. Circular 230 section 10.37: apply the law to verified facts, identify assumptions and unresolved issues, and obtain qualified review before filing or acting.

## Scope

Wisconsin (US-WI) full-year resident individuals, including sole proprietors and disregarded single-member LLC owners. The 2026 WT-4A worksheet publishes actual 2026 brackets, standard-deduction formulas and exemptions. These support 2026 estimates; final 2026 Form 1 tax-table cells and line mappings have not been confirmed. Filing mechanics and any expressly dated 2025 amounts below are the **2025-2026 filing cycle**, not new 2026 final-return instructions. DOR administers chapter 71.

Load `us-form-1040-individual-return` and `us-schedule-c-and-se-computation` for the federal computation; federal figures stay there. Use `wi-corporate-tax` for corporations, `wi-payroll` for employer withholding/UI and `wisconsin-sales-tax` for consumption tax. Do not use withholding tables to compute the individual's return, or individual brackets to run payroll.

## Ask the client first

- What were each spouse's domicile and move dates, and did either spouse live or work outside Wisconsin?
- What filing status, ages and dependent status apply, including whether someone else can claim either taxpayer?
- What is the completed federal AGI, and which assets, business deductions, losses or pass-through items differ under Wisconsin law?
- What Wisconsin additions/subtractions, retirement income, U.S. obligation interest and college savings contributions are supported by records?
- Which credits and other-state taxes apply, with supporting schedules and refund/credit eligibility?
- What withholding, prior-year tax, estimated-payment dates and gross income determine filing and underpayment obligations?

## The method, step by step

### 1. Choose the return and establish domicile

The 2025 Form 1 instructions, p.3, define domicile as the true, fixed permanent home to which the person intends to return. Changing it requires intent/actions to abandon the old domicile, intent/actions to acquire the new one, and physical presence in the new domicile. Physical presence alone does not establish a new domicile. Full-year residents use Form 1. If either spouse was domiciled elsewhere at any time, use Form 1NPR unless a military residence election permits Form 1. Do not apply the old draft's unsupported generic 183-day Wisconsin resident test. [2025 instructions](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

The 2025-2026 filing-cycle gross-income thresholds are below. Gross income is before expenses and excludes items exempt in Wisconsin, such as Social Security benefits and U.S. government interest. Check the additional filing rules even below a threshold and file to recover Wisconsin withholding, estimates or eligible refundable credits. These are not 2026 filing thresholds. [2025 instructions, pp.3-4](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

| 2025 filing status / age | Gross income requiring a return, 2025-2026 filing cycle | Official source |
|---|---|---|
| Single, under 65 / 65 or older | $14,260 / $14,510 or more | https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf |
| Joint, neither / one / both spouses 65 or older | $26,510 / $26,760 / $27,010 or more | https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf |
| Separate, under 65 / 65 or older | $12,630 / $12,880 or more per spouse | https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf |
| Head of household, under 65 / 65 or older | $18,220 / $18,470 or more | https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf |
| Nonresident/part-year, including combined spouses' gross income | $2,000 or more, subject to sourcing/reciprocity exclusions | https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf |
| Dependent with unearned income, 2025 | Gross income over $1,350 including at least $451 unearned income; the instructions also impose earned/total-income limits by status | https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf |

Other 2025 filing triggers include tax on certain retirement plans, health accounts or recapture; consult the page 3 list rather than testing only the ordinary gross-income threshold. A dependent's separate total-income thresholds are $13,560 single, $17,520 head of household, $25,110 joint and $11,930 separate in that cycle. The previous version incorrectly called the ordinary filing thresholds maximum standard deductions. [2025 instructions, p.3](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

### 2. Reconcile federal AGI to Wisconsin income

Start from the completed federal adjusted gross income. Wisconsin does not start from federal taxable income, so the federal standard deduction and QBI deduction are not automatically carried into this calculation. Federal Schedule C net profit, the federal self-employment-tax adjustment, retirement-plan deductions, self-employed health insurance and home-office results enter through federal AGI, subject to the Wisconsin conformity reconciliation. Obtain their computations from the federal owner skills; do not presume that every federal adjustment is allowed unchanged in Wisconsin. [2025 instructions, pp.13-15](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

The **2025-2026 filing-cycle** mapping is: Form 1 line 1 federal AGI; line 2 Schedule I net adjustment; line 3 adjusted federal AGI; line 4 Schedule AD additions; line 5 subtotal; line 6 Schedule SB subtractions; line 7 Wisconsin income; line 8 standard deduction; line 9 income after deduction; line 10 exemptions; line 11 taxable income; line 12 tax. The earlier version's line 2/additions, line 4/subtractions, line 7/deduction and line 9/exemptions map was wrong. Keep the cycle label when using these boxes. [2025 instructions, pp.13-16](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

Wisconsin's 2025 instructions use the IRC amended to December 31, 2022 with specific exceptions and require Schedule I for nonconforming provisions. Depreciation differences, business-interest limits and later federal law require reconciliation. Continue an old Schedule I depreciation/basis adjustment until the asset is fully depreciated or disposed of; the instructions separately discuss the December 31, 2013 basis rule. Do not use a single generic bonus-depreciation addback for every asset vintage. Section 179 eligibility and limits need the year-specific Schedule I rather than an assumption of complete conformity. [2025 instructions, pp.13-14](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

Maintain an asset-by-asset federal/Wisconsin basis register with acquisition date, placed-in-service year, federal and state method, current depreciation, carryforwards and disposition differences. Additions on Schedule AD include applicable state/municipal interest, federal NOL, pass-through/entity-election differences, related-entity expenses and certain credit-related items. A taxable state income-tax refund is among Schedule SB subtractions, not a new Wisconsin addition merely because it was deducted federally. U.S. government interest, Social Security adjustments, qualifying retirement income, college savings, Wisconsin NOL and other listed subtractions use Schedule SB and their own conditions. [2025 instructions, pp.14-15](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

The supplier-pattern handoff is therefore: Schedule C/home-office income and AGI adjustments start in federal AGI; QBI/federal standard deduction do not; U.S. obligations, taxable state refund and Social Security require the applicable Wisconsin subtraction; bonus depreciation and pass-throughs require their Wisconsin reconciliation. Do not duplicate an item already removed from federal AGI. The size of the federal QBI deduction alone does not establish the exact difference between federal and Wisconsin taxable income. [2025 instructions](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

### 3. Use the actual 2026 standard-deduction formula

Let W be full-year Wisconsin income, before standard deduction and exemptions. These formulas come from the **2026** WT-4A worksheet, reverse side. A standard deduction cannot be negative. Do not substitute the earlier draft's filing thresholds as deductions. The worksheet is an estimate document; final-return table rounding may differ. [2026 WT-4A](https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf).

| Status / Wisconsin income W | 2026 deduction amount | Official source |
|---|---|---|
| Single, W <= $20,119 | $13,960 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Single, $20,119 < W < $136,453 | $13,960 minus 12% of (W minus $20,120), floored at zero | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Single, W >= $136,453 | $0 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Head of household, W <= $20,119 | $18,030 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Head of household, $20,119 < W <= $58,827 | $18,030 minus 22.515% of (W minus $20,120) | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Head of household, $58,827 < W < $136,453 | $13,960 minus 12% of (W minus $20,120), floored at zero | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Head of household, W >= $136,453 | $0 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Joint, W <= $29,039 | $25,840 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Joint, $29,039 < W < $159,690 | $25,840 minus 19.778% of (W minus $29,040), floored at zero | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Joint, W >= $159,690 | $0 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Separate, W <= $13,779 | $12,280 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Separate, $13,779 < W < $75,869 | $12,280 minus 19.778% of (W minus $13,780), floored at zero | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Separate, W >= $75,869 | $0 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Exemption, eligible self, joint spouse and each dependent | $700 each; no self exemption if claimed by another taxpayer | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Additional age exemption | $250 for each eligible taxpayer/spouse age 65 or older | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |

Dependent standard deductions, short tax years and special exclusions need their own worksheet. In the verified 2025-2026 filing cycle, a dependent's deduction is the smaller of the status-table deduction and the greater of $1,350 or earned income plus $450; short-period filers and federal Form 4563 filers receive no standard deduction. Do not carry those 2025 indexed dependent amounts into 2026 without confirmation. The age exemption requires eligibility for the ordinary self exemption. [2025 instructions, pp.15-16](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

### 4. Rates, bands and thresholds: compute 2026 gross tax

T = max(W minus allowed state standard deduction minus allowed exemptions, 0). Use the 2026 status schedule below for estimates. The rates are marginal; each base amount already includes earlier bands. Dollar boundaries are the published 2026 values, not the 2025 schedule silently carried forward. [2026 WT-4A, reverse](https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf).

| Filing status / taxable income T | 2026 gross tax amount | Official source |
|---|---|---|
| Single/head of household, T <= $15,110 | 3.5% of T | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Single/head of household, $15,110 < T <= $51,950 | $528.85 + 4.4% of excess over $15,110 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Single/head of household, $51,950 < T <= $332,720 | $2,149.81 + 5.3% of excess over $51,950 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Single/head of household, T > $332,720 | $17,030.62 + 7.65% of excess over $332,720 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Joint, T <= $20,150 | 3.5% of T | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Joint, $20,150 < T <= $69,260 | $705.25 + 4.4% of excess over $20,150 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Joint, $69,260 < T <= $443,630 | $2,866.09 + 5.3% of excess over $69,260 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Joint, T > $443,630 | $22,707.70 + 7.65% of excess over $443,630 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Separate, T <= $10,080 | 3.5% of T | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Separate, $10,080 < T <= $34,630 | $352.80 + 4.4% of excess over $10,080 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Separate, $34,630 < T <= $221,820 | $1,433.00 + 5.3% of excess over $34,630 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |
| Separate, T > $221,820 | $11,354.07 + 7.65% of excess over $221,820 | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf |

For an actual 2025 Form 1, the instructions require the tax table below $100,000 taxable income and the tax computation worksheet at $100,000 or more. Use that year's rates/table, not the 2026 estimate schedule. Final 2026 Form 1 tax-table treatment must be confirmed before filing. [2025 instructions, p.16](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

### 5. Credits, other-state income and specialist subtractions

Use the credit's own schedule, distinguish refundable from nonrefundable amounts, and apply credit ordering before calculating payments/refund. The 2025 Form 1 instructions cover the itemized-deduction credit on Schedule 1, which is a credit computation rather than an unrestricted state itemized deduction. A taxpayer may need a Wisconsin-labelled federal Schedule A even when not itemizing federally. [2025 instructions, p.16](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

For the **2025-2026 filing cycle**, Schedule SB line 16 allows federally taxable qualified retirement-plan/IRA income not already subtracted on lines 12-15: up to $24,000 for an eligible individual age 67 by year-end, or $48,000 on a joint return when both spouses qualify, regardless of which spouse received it. Claiming this subtraction forfeits all Schedule CR and Form 1 lines 13-20 and 30-35 credits, including use of prior credit carryforwards and creation of current credits for later use. Compare the whole return with and without the subtraction; do not automatically choose the largest income exclusion. The separate age-65 $5,000 subtraction is income-restricted and uses its own worksheet after other retirement exclusions. [2025 Schedule SB pp.7-8](https://www.revenue.wi.gov/TaxForms2025/2025-ScheduleSB-Inst.pdf).

The same cycle's Wisconsin EIC requires a qualifying child and full-year legal residence, with the stated married-separate/head-of-household exception. Recompute the federal credit under Wisconsin conformity/Schedule I where necessary; use its result, not an unreconciled federal figure. Multiply by 4% for one qualifying child, 11% for two, and 34% for three or more. Enter this refundable credit on line 30 with the required Schedule EIC/preparer support. No child gives no Wisconsin EIC. The old phrase partially refundable is replaced by its actual placement in the refundable-credit/payment section. Final 2026 credit instructions remain to be confirmed. [2025 Form 1 pp.26-27](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

College savings remains a distinct subtraction: the account owner or an authorized contributor may qualify; eligible inbound plan rollovers use principal, not investment earnings. Complete Schedule CS rather than reuse an old annual cap. Manufacturing/agriculture, Schedule OS, AMT, farmland preservation, amended-return recovery and pass-through elections require their specific calculations. [2025 Schedule SB p.6](https://www.revenue.wi.gov/TaxForms2025/2025-ScheduleSB-Inst.pdf).

Reciprocity covers qualifying employee compensation with Illinois, Indiana, Kentucky and Michigan; it does not exempt a Wisconsin sole proprietor's business profit. January 2026 Publication 121 is explicitly for the **2025-2026 filing cycle**. It includes dual-residence exceptions for particular agreements and distinguishes withholding declarations from return obligations. Wisconsin residents still report reciprocal-state wages on Wisconsin returns. Do not treat an out-of-state address as evidence of domicile or assume reciprocity also determines UI. [Publication 121, pp.3-5](https://www.revenue.wi.gov/DOR%20Publications/pb121.pdf).

## Boundary and exception table

| Situation | Treatment / destination |
|---|---|
| Full-year Wisconsin resident sole proprietor | Compute federal AGI, Wisconsin adjustments, state deduction/exemptions and tax in order. |
| Move during year or spouse domiciled elsewhere | Form 1NPR; source/allocation and prorated deductions/exemptions need its instructions. The WT-4A notes prorated brackets for nonresidents/part-year residents. |
| Business assets or nonconforming federal provisions | Schedule I/basis reconciliation; never assume federal bonus or retirement changes automatically apply. |
| Dependent or short-period filer | Use the special deduction rule; ordinary full-year deduction is not automatic. |
| Other-state taxed business income | Analyze sourcing and Schedule OS; employee reciprocity is not a business-income exemption. |
| Corporation, sales tax, employer withholding/UI | `wi-corporate-tax`, `wisconsin-sales-tax`, `wi-payroll`, respectively. |
| Estate/inheritance tax, local income-tax claims | Outside this income computation; the old README's broad absence claims were not independently confirmed here. |

## Worked cases

### Case 1: single sole proprietor, 2026 estimate

An invented full-year resident under 65 has reconciled Wisconsin income of $150,000, cannot be claimed by another taxpayer and has no dependents, credits, AMT or special modifications remaining. The 2026 deduction is zero at this income. Taxable income is $149,300 and gross estimated tax is $7,309.36. This uses the actual 2026 schedule, not a 2025 final return.

```oa-check
name: Wisconsin single 2026 estimate
inputs:
  wisconsin_income: 150000
  standard_deduction: 0
  exemption: 700
steps:
  - taxable: max(wisconsin_income - standard_deduction - exemption, 0)
  - gross_tax: 2149.81 + (taxable - 51950) * 0.053
expected:
  taxable: 149300
  gross_tax: 7309.36
```

### Case 2: joint deduction and the zero-base decision

An invented joint full-year resident couple, both under 65 and neither claimed by anyone else, has $25,000 Wisconsin income and no special deduction restriction. The deduction plus their exemptions exceeds income. Taxable income and gross tax are zero. This does not decide the 2026 filing duty: test that year's filing rules and any refund/credit entitlement separately, rather than equating no tax with no return.

```oa-check
name: Wisconsin joint zero-base decision
inputs:
  wisconsin_income: 25000
  standard_deduction: 25840
  exemptions: 1400
steps:
  - taxable: max(wisconsin_income - standard_deduction - exemptions, 0)
  - gross_tax: taxable * 0.035
expected:
  taxable: 0
  gross_tax: 0
```

## When to refuse or refer

Refer unresolved domicile, military elections, Form 1NPR allocation, marital-property differences, nonconforming business deductions, related-entity adjustments, Schedule OS credit, manufacturing/agriculture credits, farmland/homestead claims, AMT, amended returns and audit notices. Retain the ordinary calculation and identify which issue prevents completion. Never represent a missing 2026 form/table as verified, or a source-cited draft as accountant approval.

## Filing and payment

For the **2025-2026 filing cycle**, Form 1 is due April 15, 2026. A federal extension provision can be used for Wisconsin even if the federal return was filed on time; include the federal extension or explanatory statement when filing. It extends filing, not payment. Use the year's Form 1-ES for an extension payment, including when e-filing; the instructions say not to use Form PV for that purpose. Unpaid tax during the extension generally bears 1% monthly interest, with special disaster/combat exceptions. [2025 instructions, p.4](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

The actual **2026 Form 1-ES** requires estimates when expected tax after withholding/credits is at least $500 and expected withholding is less than the smallest of 90% of 2026 tax, 100% of qualifying twelve-month 2025 tax, or 90% under annualization. Use the latest adjusted/amended prior-year tax. A full-year Wisconsin resident with no liability for the twelve-month 2025 year is exempt from estimates. Do not import a federal high-income 110% rule. [2026 Form 1-ES pp.1-2](https://www.revenue.wi.gov/TaxForms2026/2026-Form1-ES-Inst.pdf).

| 2026 estimate item / condition | Amount or date | Official source |
|---|---|---|
| Ordinary calendar-year installments | April 15, June 15, September 15, 2026; January 15, 2027 | https://www.revenue.wi.gov/TaxForms2026/2026-Form1-ES-Inst.pdf |
| Liability first arises after March 31/before June 1 | June 15, one-half required estimate | https://www.revenue.wi.gov/TaxForms2026/2026-Form1-ES-Inst.pdf |
| First arises after May 31/before September 1 | September 15, three-quarters | https://www.revenue.wi.gov/TaxForms2026/2026-Form1-ES-Inst.pdf |
| First arises after August 31 | January 15, all | https://www.revenue.wi.gov/TaxForms2026/2026-Form1-ES-Inst.pdf |
| Qualifying farmer/fisher | At least two-thirds gross income in 2025 or 2026; pay estimate in full January 15, 2027 or file/pay by March 1, 2027 | https://www.revenue.wi.gov/TaxForms2026/2026-Form1-ES-Inst.pdf |

Use next business day for a weekend/legal holiday. The return-as-final-installment exception requires filing/paying by January 31, 2027 and no September/prior installment obligation; it does not erase earlier underpayments. Fiscal years use the specified fourth/sixth/ninth/next-first-month dates. Recompute changed estimates on the worksheet, apply withholding and prior overpayment without duplication and retain vouchers or separate online payment receipts. Use Schedule U for installment underpayment interest. [2026 Form 1-ES, all pages](https://www.revenue.wi.gov/TaxForms2026/2026-Form1-ES-Inst.pdf).

For the verified cycle, prepare the federal return first, reconcile state schedules and use Wisconsin e-file software or WisTax only if its eligibility conditions are met. WisTax eligibility includes full-year residence, Wisconsin identification/prior filing and limited allowed adjustments/credits; it is not universal business-return software. MTA manages payments, notices and estimates. Preserve the accepted return, payment confirmation and reconciled W-2/estimate records separately. Tax withheld or credited is a payment, not a deduction from the taxable base. [2025 instructions, pp.4-5,26](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

Late-payment and underpayment interest are different. The 2025 instructions state 12% annual interest on an amount due from the original due date and describe Schedule U underpayment interest even where the return produces a refund. Ordinary late-filing/negligence/fraud penalties, disaster dates and final 2026 payment deadlines remain unconfirmed; do not substitute a federal penalty. [2025 instructions, pp.32-33](https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf).

## Completion checklist

- Confirm residence and return type for both spouses, status, dependency and ages.
- Tie federal AGI to the federal return; separately reconcile Schedule I, AD, SB and asset bases without duplicate deductions.
- Label every rate, form line and indexed deduction by its actual tax year.
- Recompute deduction, exemptions, taxable income and marginal-band gross tax; use the required final-return table when available.
- Keep credits, other-state tax, estimates and withholding separate, and test filing duty even where computed tax is zero.
- Produce a source-linked calculation, assumptions, missing items and payment/filing brief for professional review.

## Sources

| Official source / section read | URL | Read on |
|---|---|---|
| DOR 2026 W-234 WT-4A worksheet, both pages. Read for 2026 deduction formulas, status brackets, exemptions, proration and its estimate-only purpose. | https://www.revenue.wi.gov/TaxForms2017through2019/w-234f.pdf | 2026-11-13 |
| DOR 2025 Form 1 instructions, pp.3-5,9,13-16,26-27,32-33. Read for domicile/filing triggers, cycle-specific form mapping, conformity, modifications, deduction exceptions, tax-table boundary, payment and underpayment rules. | https://www.revenue.wi.gov/TaxForms2025/2025-Form1-Inst.pdf | 2026-11-13 |
| DOR Publication 121, January 2026, pp.3-5. Read for the 2025-2026 filing-cycle employee-compensation agreements, business-income exclusion, dual-residence and return/refund boundaries. | https://www.revenue.wi.gov/DOR%20Publications/pb121.pdf | 2026-11-13 |

| DOR 2026 Form 1-ES, all three pages. Read for current estimate tests, exceptions, dates/fractions, worksheet and 2026 indexed figures matching WT-4A. | https://www.revenue.wi.gov/TaxForms2026/2026-Form1-ES-Inst.pdf | 2026-11-13 |
| DOR 2025 Schedule SB instructions, pp.1-2,6-8, retained 2025-2026 filing cycle. Read for state refund/U.S. interest/Social Security subtractions, college-savings eligibility and retirement exclusion/credit forfeiture. | https://www.revenue.wi.gov/TaxForms2025/2025-ScheduleSB-Inst.pdf | 2026-11-13 |

Not yet confirmed: final 2026 Form 1/1NPR instructions, tax-table cells, indexed dependent rules, filing thresholds and final-return payment dates; all current Schedule I conformity exceptions and section 179 limits; 2026 retirement-subtraction form details (the 2025-2026 cycle includes the credit forfeiture above); the 2026 Edvest/Tomorrow's Scholar cap (old $5,130 not carried forward); final 2026 EIC instructions (the verified 2025-2026 cycle rules are above); Schedule OS limits and adjustments; manufacturing/agriculture, farmland, homestead and AMT computations; amendments and refund claims; special Schedule U waiver/annualization details; generic 183-day residence, local income tax and estate/inheritance absence assertions; full current late-filing, negligence and fraud penalty rules. These gaps are not usable numerical guidance.
