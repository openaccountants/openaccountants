---
name: us-qbi-deduction
description: Compute the US federal section 199A deduction for a Schedule C business in 2026, with separately dated 2025 cases. Covers QBI adjustments, SSTB status, wage and property limits, loss netting, the taxable income cap and active-business minimum. Trigger on QBI, 199A, pass-through deduction, Form 8995, Form 8995-A or SSTB.
version: "1.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US qualified business income deduction (section 199A), tax year 2026

The final One Big Beautiful Bill Act (Public Law 119-21, section 70105) kept the 20% rate, removed the end-2025 expiry, and introduced wider phase-in ranges and an active-business minimum for taxable years beginning after 31 December 2025. Use the year-specific table below; the ordinary deduction remains subject to the taxable income cap and the minimum has its own eligibility test.

## Scope and who this is for

For an individual with a sole proprietorship or federally disregarded single-member LLC: establish a section 162 trade or business, US effectively connected qualified items and their inclusion or allowance in taxable income. Schedule C profit is not automatically all QBI. This Guide computes the ordinary Schedule C component; specialist topics below require a separate determination. Material participation is required for the new minimum, not for the ordinary QBI deduction.

The 2026 form mappings below are planning references to IRS drafts, **not filing instructions**. Do not file draft forms. The draft Form 8995 instructions route the result to Form 1040 **line 13b**, replacing this Guide's earlier line 13a reference. Final-year forms must be confirmed before filing.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Classifying transactions into Schedule C lines | `us-sole-prop-bookkeeping` |
| Schedule C net profit, self-employment tax and its deductible half | `us-schedule-c-and-se-computation` |
| Self-employed health insurance deduction (section 162(l)) | `us-self-employed-health-insurance` |
| SEP, SIMPLE and solo 401(k) contributions and their limits | `us-self-employed-retirement` |
| Standard deduction and the rest of taxable income | `us-federal-income-tax-return-1040` |
| No tax on tips (section 224) and the other 2026 changes | `us-2026-federal-tax-changes` |
| Whether to elect S corporation status to create W-2 wages | `us-s-corp-election-decision` |
| Rental real estate as a trade or business, material participation | `us-real-estate-professional-and-short-term-rentals` |
| QBI from partnerships and S corporations (Schedule K-1) | `us-form-1065-partnership`; refer (R-QBI-K1) |
| Paying the tax during the year | `us-quarterly-estimated-tax` |
| Putting the return together | `us-federal-return-assembly` |
| State QBI conformity or add-backs | the state's income tax skill (for California, `us-ca-return-assembly`) |

This skill loads on top of `us-tax-workflow-base`.

## Ask the client first

Obtain the tax year and filing status; actual activities and gross receipts split; each business's Schedule C profit and attributable deductible SE tax, health insurance and retirement contributions; prior-year QBI losses; taxable income before QBI; net capital gain and qualified dividends; documented common-law employee wages and SSA filing dates; property basis, business-use percentage, placed-in-service date and year-end availability; and material-participation evidence. Ask whether the taxpayer previously did substantially the same work as an employee of the customer or a related person.

Missing filing status, business eligibility, classification, wages, property, carryforwards or participation is an **unresolved input**, not zero. Obtain the records before a usable computation. Label any requested sensitivity calculation conditional. Review all threshold-sensitive, loss, mixed-activity, large-deduction and minimum-deduction cases; the former USD 5,000/10,000 proximity and USD 15,000 deduction triggers were internal triage policies, not tax thresholds.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Deduction rate on QBI | 20% (the 23% in the House-passed bill was not enacted) | [26 U.S.C. 199A(b)(2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm); [Public Law 119-21, section 70105](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Overall cap | 20% of (taxable income before the QBI deduction minus net capital gain, with qualified dividends added to net capital gain) | [26 U.S.C. 199A(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm); [Form 8995 (2026 draft), lines 11 to 14](https://www.irs.gov/pub/irs-dft/f8995--dft.pdf) |
| Threshold amount, all other returns (single, head of household, qualifying surviving spouse) | USD 201,750 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Threshold amount, married filing separately | USD 201,775 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Threshold amount, married filing jointly | USD 403,500 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| End of phase-in range, all other returns | USD 276,750 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| End of phase-in range, married filing separately | USD 276,775 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| End of phase-in range, married filing jointly | USD 553,500 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Phase-in range width, every return except joint (was USD 50,000 to 2025) | USD 75,000 | [Public Law 119-21, section 70105(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Phase-in range width, joint return (was USD 100,000 to 2025) | USD 150,000 | [Public Law 119-21, section 70105(a)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| Tax year 2025 (prior year, for 2025 returns): Taxable income threshold (single / HoH / QSS) | $197,300 | [Rev. Proc. 2024-40, section 3.27](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| Tax year 2025 (prior year, for 2025 returns): Taxable income threshold (MFJ) | $394,600 | [Rev. Proc. 2024-40, section 3.27](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| Tax year 2025 (prior year, for 2025 returns): Taxable income threshold (MFS) | $197,300 | [Rev. Proc. 2024-40, section 3.27](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) |
| Wage limit, first alternative | 50% of W-2 wages | [26 U.S.C. 199A(b)(2)(B)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm) |
| Wage limit, second alternative | 25% of W-2 wages plus 2.5% of UBIA of qualified property | [26 U.S.C. 199A(b)(2)(B)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm) |
| Depreciable period for UBIA | later of 10 years from placed in service or the last full year of the section 168 recovery period (ignoring 168(g)) | [26 U.S.C. 199A(b)(6)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm) |
| W-2 wages count only if filed with SSA within | 60 days after the due date (with extensions) | [26 U.S.C. 199A(b)(4)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm) |
| Minimum deduction, taxable years beginning after 31 December 2025 | USD 400 | [Rev. Proc. 2025-32, section 2.12](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Public Law 119-21, section 70105(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| QBI needed for the minimum, from active businesses (material participation, section 469(h)) | USD 1,000 | [Rev. Proc. 2025-32, section 2.12](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf); [Public Law 119-21, section 70105(b)](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm) |
| SSTB de minimis, gross receipts USD 25 million or less | not an SSTB if under 10% of gross receipts are from the specified service | [Treas. Reg. 1.199A-5(c)(1)(i)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-5) |
| SSTB de minimis, gross receipts over USD 25 million | under 5% | [Treas. Reg. 1.199A-5(c)(1)(ii)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-5) |
| Former employee presumed still an employee for the same services | 3 years | [Treas. Reg. 1.199A-5(d)(3)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.199A-5) |

The rate, the 50%, 25% and 2.5% factors and the phase-in widths are statutory and not indexed. The thresholds are indexed every year. The USD 400 and USD 1,000 are indexed only for taxable years beginning after 2026, in multiples of USD 5 (Public Law 119-21, section 70105(b), new section 199A(i)(3)).

### Step 1: qualified business income for each business

For an ordinary Schedule C business whose profit contains only qualified items, and with no other attributable adjustments:

**QBI = Schedule C line 31 minus the deductible half of self-employment tax (Schedule 1) minus the self-employed health insurance deduction minus the deduction for contributions to SEP, SIMPLE or solo 401(k) plans for the owner.**

Only allowable deductions attributable to the business are subtracted. Allocate the section 164(f), 162(l) and 404 deductions to the extent each business's gross income was used in calculating the deduction, proportionately to that gross income (Treas. Reg. 1.199A-3(b)(1)(vi)). Do not automatically allocate using net Schedule C profit. Obtain upstream deduction amounts first; testing taxable income **before** QBI avoids the old iterative threshold loop.

Exclude capital gains/losses (including section 1231 items treated as capital), dividends and dividend equivalents, interest not allocable to the business, and annuities unconnected with it. Employee wages are excluded; statutory-employee wages are an exception. An owner's draw does not create QBI or qualified employee wages. Section 224 tip amounts excluded from business net profit are not QBI; this exclusion is not solely a new 2026 rule. Other commodities, currency and notional-contract exclusions, personal IRA/Roth deductions and state-tax allocation: **Check this point with one of our partner accountants.**

Losses suspended by another Code provision enter QBI only when allowed in taxable income; pre-2018 losses generally are not qualified. Track qualified/nonqualified portions, with an SSTB suspended loss's status and applicable percentage fixed in its originating year. For detailed suspended-loss ordering: **Check this point with one of our partner accountants.**

**Net before calculating each business's component:** offset negative QBI against positive businesses in proportion to their positive QBI. Do not transfer the loss business's wages or UBIA. Include the qualified prior-year loss as a separate business, even if the original business has ceased. If combined QBI remains negative, the ordinary QBI component is zero and the loss carries to the next year; this carryover does not change the loss's treatment elsewhere. Track the 2025 loss brought into 2026 and any 2026 balance carried to 2027 (Treas. Reg. 1.199A-1(d)(2)(iii)).

### Step 2: taxable income before the QBI deduction

Section 199A(e)(1), as amended by Public Law 119-21 section 70111, measures taxable income **without the QBI deduction and without the section 68 itemized-deduction limitation**. Use Form 1040 line 11a (adjusted gross income) minus the standard or itemized deduction and the other deductions the 2026 draft Form 8995 instructions list for line 11. For the draft's itemizers, use the specified Schedule A amounts before section 68 plus the specified other deduction; do not substitute the final section-68-reduced deduction. The draft's non-itemizer formula is line 11a minus lines 12e, 12f and 13a. These are draft-year locators only.

### Step 3: where taxable income sits

| Taxable income before the QBI deduction | What applies | Form |
| --- | --- | --- |
| At or below the threshold (USD 201,750 / 201,775 / 403,500) | 20% of QBI for every business, SSTB or not; no wage or UBIA limit | Form 8995 (unless a cooperative patron) |
| Above the threshold, up to the end of the range (USD 276,750 / 276,775 / 553,500) | SSTB items cut to the applicable percentage; wage and UBIA limit phased in | Form 8995-A with Part III, and Schedule A for an SSTB |
| Above the end of the range | SSTB: no deduction. Other businesses: the smaller of 20% of QBI and the wage and UBIA limit | Form 8995-A |

The phase-in fraction is (taxable income minus the threshold) divided by USD 75,000 (USD 150,000 joint) (Form 8995-A (2026 draft), lines 20 to 24). The applicable percentage for an SSTB is 100% minus that fraction, not below zero (section 199A(d)(3)(B)).

### Step 4: SSTB status

The listed SSTB fields are health, law, accounting, actuarial science, performing arts, consulting, athletics, financial services, brokerage, investing/investment management, trading/dealing in securities, partnership interests or commodities, and the defined reputation/skill activities. Engineering and architecture are excluded from the statutory list. Financial planning/advisory, accounting and legal services in the cases below fall within their respective fields (Treas. Reg. 1.199A-5(b)).

Consulting means professional advice and counsel to help clients achieve goals and solve problems, including lobbying. Sales, training and educational courses are excluded from consulting; embedded/ancillary consulting in an otherwise non-SSTB sale or service is excluded only with **no separate payment**. Producing code, a report, design or another deliverable does **not** by itself establish non-SSTB status. For software/web development, UX/UI or graphic design, data science/analytics, IT/marketing consulting and mixed advice/deliverables: **Check this point with one of our partner accountants.**

For the former detailed classifications of healthcare professionals versus clubs/spas/payment processing/drug or device sales; bookkeeping; deposit-taking/lending; stock versus real-estate/insurance brokerage; and endorsements, name/likeness licensing or appearance fees: **Check this point with one of our partner accountants.** Do not infer the whole business's classification merely because an activity is excluded from one field.

**De minimis:** a business with annual gross receipts at most USD 25 million is not an SSTB if **less than 10%** of receipts are attributable to specified services; use **less than 5%** above USD 25 million. Activity incident to the specified service counts toward its receipts. Equality fails the test. Apply the actual business's annual receipts; business-character changes or a failed/mixed test require R-QBI-SSTB-MIXED, not an assumed all-year classification (Treas. Reg. 1.199A-5(c)(1)).

**Former employee:** substantially the same services for the former employer or a related person create a three-year presumption of employee services, including indirect provision through an entity. Rebuttal requires records establishing nonemployee status under federal law, upon IRS notice. R-QBI-EMPLOYEE: **Check this point with one of our partner accountants.**

### Step 5: W-2 wages and UBIA

**W-2 wages:** use qualifying section 6051(a)(3) and (8) employee amounts paid in the calendar year ending in the tax year, properly allocable to QBI and included on SSA returns within 60 days after their due date including extensions. A payroll provider's wages may count for the business's own common-law employees; wages earned at another job and the owner's draws are not that business's wages (section 199A(b)(4); Treas. Reg. 1.199A-2(b)(2)).

**UBIA:** use placed-in-service basis, reduced for nonbusiness use, of tangible depreciable property held and available for business use at year end, used during the year to produce QBI and within its depreciable period. That period ends on the later of the exact tenth anniversary of first placed-in-service or the last day of the last full applicable section 168 recovery year, ignoring 168(g). Depreciation and section 179 expensing do not reduce UBIA; land is not qualifying depreciable property. For the original USD 3,499 MacBook/laptop placed in service in 2025 with a five-year recovery period and wholly business use, expensing alone does not remove its USD 3,499 UBIA. It can qualify at each year end through 2034 if all conditions continue; whether it also qualifies at year end 2035 depends on its exact placed-in-service date. Acquisitions, dispositions, short years or non-cost-basis transactions: **Check this point with one of our partner accountants.**

### Step 6: the deduction for each business

Per business, before the cap (section 199A(b)(2) and (3); Form 8995-A (2026 draft), Parts II and III):

1. **At or below the threshold:** 20% x QBI.
2. **SSTB above the threshold:** first multiply QBI, W-2 wages and UBIA by the applicable percentage (Schedule A, Form 8995-A). Above the end of the range the applicable percentage is zero and so is the deduction.
3. **Tentative amount** (line 3): 20% x QBI (after step 2 for an SSTB).
4. **Wage and UBIA limit** (line 10): the greater of 50% x W-2 wages, or 25% x W-2 wages plus 2.5% x UBIA.
5. **Above the end of the range:** the smaller of line 3 and line 10 (line 11).
6. **Inside the range, where line 10 is less than line 3:** reduction = (line 3 minus line 10) x phase-in fraction; the deduction is line 3 minus that reduction (lines 17 to 26). For a sole proprietor with no employees and no property, line 10 is zero, so the deduction is 20% x QBI x (1 minus the fraction), and for an SSTB that is applied to QBI already cut to the applicable percentage.

### Step 7: combine, cap, then the minimum

1. Sum the business components **after** loss netting and any SSTB/wage limitations.
2. REIT/PTP income, losses and their separate component/carryforward require R-QBI-REIT: **Check this point with one of our partner accountants.** Do not silently assume none.
3. **Cap:** ordinary deduction = smaller of the combined components and `20% × max(0, taxable income before QBI − (net capital gain + qualified dividends))`. Add qualified dividends to net capital gain **before subtracting the total**, not to taxable income (section 199A(a); draft Form 8995 lines 11–15).
4. **Minimum (new for 2026):** if aggregate QBI from all businesses the taxpayer materially participated in is at least USD 1,000, the deduction is the greater of the step 3 result and USD 400. Here businesses means **qualified** active trades or businesses, with material participation under section 469(h), and the amount must be the active QBI taken into account for this computation. The law makes the minimum an exception to subsection (a); do not describe the taxable income cap as absolute after this comparison. Do not apply the minimum to 2025. Confirm participation and eligible active QBI before using it; do not assume every profitable SSTB remains qualified above its phase-out. For zero/negative taxable income, mixed active/passive losses or uncertain minimum eligibility: **Check this point with one of our partner accountants.**

### Form 8995 (simplified), 2026 draft line by line

Use it when taxable income before the QBI deduction is at or below USD 201,750 (USD 201,775 married filing separately, USD 403,500 joint) and the client is not an agricultural/horticultural cooperative patron. Multiple businesses or a below-threshold SSTB do not alone require the detailed form. Aggregation requires the specialist review below; the IRS instructions require Schedule B or a similar schedule if aggregating.

| Line | Entry |
| --- | --- |
| 1i to 1v | Business name, TIN (the LLC's EIN, or the owner's tax identification number if none), QBI or loss |
| 2 | Total QBI |
| 3 | Qualified business loss carryforward from 2025 (negative) |
| 4 | Lines 2 plus 3; zero if negative |
| 5 | Line 4 x 20% |
| 6 to 9 | REIT and PTP amounts and the 20% component |
| 10 | Lines 5 plus 9 |
| 11 | Taxable income before the QBI deduction |
| 12 | Net capital gain plus qualified dividends |
| 13 | Line 11 minus line 12, not below zero |
| 14 | Line 13 x 20% |
| 15 | Smaller of line 10 or line 14 (new label: before the minimum deduction) |
| 16 | Minimum deduction for active QBI (new for 2026): USD 400 if active QBI on line 1 is at least USD 1,000 |
| 17 | Greater of line 15 or line 16; draft instructions route to Form 1040 line 13b |
| 18 | QBI loss carryforward to 2027 (lines 2 plus 3, if negative) |
| 19 | REIT and PTP loss carryforward |
| 20 | Box for an electing small business trust (new) |

### Form 8995-A (detailed), 2026 draft

Use it when taxable income before the QBI deduction is above the threshold, or the client is a cooperative patron. An SSTB below the threshold, or several businesses below the threshold, do not on their own require Form 8995-A. Schedule A carries the SSTB applicable percentage, Schedule B the aggregation, Schedule C loss netting and carryforwards, Schedule D the patron reduction. Part II lines 2 to 16 run Step 6 per business, Part III lines 17 to 26 the phase-in, Part IV lines 27 to 41 the cap, the section 199A(g) amount and the minimum (lines 39 to 41).

## Boundary and exception table

At the threshold, use below-threshold rules; the first excess dollar enters the phase-in. At the range end, the SSTB applicable percentage is zero and the ordinary wage/property limit is fully effective. For a non-SSTB above the range with no qualified wages, property can still supply the 2.5% UBIA alternative. With neither wages nor property its **ordinary business component** is zero; assess the active-business minimum separately. Lack of material participation does not itself eliminate the ordinary deduction. A loss is not automatically a permanent bar to the minimum from other active businesses; use the referral in Step 7. Community-property allocations and statutory-employee wage-limit treatment: **Check this point with one of our partner accountants.**

## Worked cases

All cases are conditional worksheets: the stated upstream deductions must be independently allowable, business items qualified and carryforwards/other components confirmed. Where a case does not state a capital-gain/dividend amount, the displayed cap assumes none; obtain the facts before applying it to a return. They compare QBI deductions, not a person's final tax liability. Keep intermediate precision and round displayed amounts to cents. The original rounded upstream inputs are preserved.


**Case 1, a decision: does a financial planner just above the threshold get a partial deduction, and is an extra USD 5,100 SEP contribution worth making?** A single financial planner (financial services, an SSTB) has 2026 Schedule C net profit of USD 270,000, no employees and no qualifying property. From the upstream skills: deductible half of self-employment tax USD 15,054.50, self-employed health insurance USD 12,000, SEP contribution USD 20,000 (option A). No other income; standard deduction USD 16,100 (2026, from `us-federal-income-tax-return-1040`). Option B raises the SEP contribution by USD 5,100 to USD 25,100, subject to independent confirmation that the additional deduction is allowable under the plan.

Option A: QBI = 270,000 minus 15,054.50 minus 12,000 minus 20,000 = USD 222,945.50. Taxable income before the QBI deduction = USD 206,845.50, which is USD 5,095.50 above the USD 201,750 threshold. Phase-in fraction = 5,095.50 / 75,000 = 6.794%; applicable percentage = 93.206%. The SSTB is still a qualified business, cut to 93.206%: 20% x 222,945.50 x 93.206% = USD 41,559.72 (Form 8995-A line 3). Line 10 is zero, so the phase-in reduction is 41,559.72 x 6.794% = USD 2,823.57, leaving USD 38,736.15. The cap is 20% x 206,845.50 = USD 41,369.10, not binding. **Deduction USD 38,736.15**, a partial deduction, not zero. Taxable income after it: USD 168,109.35.

Option B: QBI = USD 217,845.50 and taxable income before the QBI deduction = USD 201,745.50, at or below the threshold, so SSTB status no longer matters and Form 8995 applies. 20% of QBI is USD 43,569.10, but the cap is 20% x 201,745.50 = USD 40,349.10, which binds. **Deduction USD 40,349.10.** Taxable income after it: USD 161,396.40.

The figure that decides: the extra USD 5,100 contribution cuts taxable income by USD 6,712.95 (USD 1,612.95 more QBI deduction on top of the USD 5,100). This compares taxable income only, not tax saved or investment suitability. Check this point with one of our partner accountants before recommending a contribution. Either way, a planner USD 5,095.50 over the threshold keeps most of the deduction.

```oa-check
name: SSTB just above the 2026 threshold, with and without an extra SEP contribution (single)
inputs:
  schedule_c_profit: 270000
  half_se_tax: 15054.50
  se_health: 12000
  sep_a: 20000
  sep_b: 25100
  std_deduction: 16100
  threshold: 201750
  phase_range: 75000
steps:
  - qbi_a: schedule_c_profit - half_se_tax - se_health - sep_a
  - ti_a: qbi_a - std_deduction
  - phase_a: clamp((ti_a - threshold) / phase_range, 0, 1)
  - applicable_a: 1 - phase_a
  - line3_a: 0.20 * qbi_a * applicable_a
  - after_phase_a: line3_a - (line3_a - 0) * phase_a
  - deduction_a: min(after_phase_a, 0.20 * ti_a)
  - qbi_b: schedule_c_profit - half_se_tax - se_health - sep_b
  - ti_b: qbi_b - std_deduction
  - deduction_b: min(0.20 * qbi_b, 0.20 * ti_b)
  - taxable_after_a: ti_a - deduction_a
  - taxable_after_b: ti_b - deduction_b
  - saving_in_taxable_income: taxable_after_a - taxable_after_b
expected:
  qbi_a: 222945.50
  ti_a: 206845.50
  line3_a: 41559.72
  deduction_a: 38736.15
  ti_b: 201745.50
  deduction_b: 40349.10
  taxable_after_a: 168109.35
  taxable_after_b: 161396.40
  saving_in_taxable_income: 6712.95
```

**Case 2, the new USD 400 minimum.** A single employee earns USD 30,000 of wages and runs a small weekend photography business she works in herself for more than 500 hours a year (material participation). Schedule C net profit is USD 1,500; the deductible half of self-employment tax is USD 105.97 (from `us-schedule-c-and-se-computation`); no health insurance or retirement deduction. Standard deduction USD 16,100.

QBI = 1,500 minus 105.97 = USD 1,394.03. Taxable income before the QBI deduction = 30,000 plus 1,394.03 minus 16,100 = USD 15,294.03, below the threshold, so Form 8995. Line 5: 20% x 1,394.03 = USD 278.81. Line 14: 20% x 15,294.03 = USD 3,058.81. Line 15: USD 278.81. Active QBI of USD 1,394.03 is at least USD 1,000, so line 16 is USD 400 and line 17 is **USD 400**. Holding the stated taxable income and QBI fixed, the pre-minimum result is USD 278.81; this is not a recomputation of a 2025 return. Had she not materially participated, or had QBI been under USD 1,000, it would stay at line 15.

```oa-check
name: Minimum deduction for active QBI (2026, single)
inputs:
  wages: 30000
  schedule_c_profit: 1500
  half_se_tax: 105.97
  std_deduction: 16100
  minimum: 400
  minimum_qbi: 1000
steps:
  - qbi: schedule_c_profit - half_se_tax
  - taxable_income: wages + qbi - std_deduction
  - line_5: 0.20 * qbi
  - line_14: 0.20 * taxable_income
  - line_15: min(line_5, line_14)
  - line_16: minimum * clamp(floor(qbi / minimum_qbi), 0, 1)
  - line_17: max(line_15, line_16)
expected:
  qbi: 1394.03
  taxable_income: 15294.03
  line_5: 278.81
  line_14: 3058.81
  line_15: 278.81
  line_16: 400.00
  line_17: 400.00
```

**Case 3, 2026 wage limit above the range.** A married couple filing jointly have taxable income before the QBI deduction of USD 600,000, above the USD 553,500 end of the range. Her landscaping business (not an SSTB) has QBI of USD 300,000, paid USD 60,000 of W-2 wages to two employees and holds equipment with UBIA of USD 200,000. 20% of QBI is USD 60,000. The limit is the greater of 50% x 60,000 = USD 30,000 and 25% x 60,000 plus 2.5% x 200,000 = USD 20,000, so USD 30,000. The deduction is the smaller of USD 60,000 and USD 30,000: **USD 30,000**; the cap (20% x 600,000 = USD 120,000) does not bind. For an SSTB at this income, its ordinary QBI component would be zero; any minimum must separately satisfy qualified active-business eligibility.

### Historical 2025 examples, retained with their original inputs

These are **2025**, not 2026 calculations. No active-business minimum applies. The basic single deduction used in the corrected 2025 examples is USD 15,750; the corresponding MFJ amount is USD 31,500 (IRS Publication 501, Table 6). Business classification above the threshold needs actual facts; a job title alone is not proof.

**Example 1 — Maria Hernandez, single, freelance UX designer, Austin TX (2025).** Original upstream inputs: profit USD 62,644; deductible SE tax USD 4,427; health USD 8,400; employee retirement deferral USD 23,500 plus employer USD 7,264 = USD 30,764. QBI = 62,644 − 4,427 − 8,400 − 30,764 = **USD 19,053**. Taxable income = 19,053 − 15,750 = **USD 3,303**. Tentative deduction USD 3,810.60; cap USD 660.60; **deduction USD 660.60** (USD 661 whole dollars), Form 8995. This does not establish retirement eligibility or the designer's SSTB status, which does not limit the deduction below this threshold.

**Example 2 — James Chen, single, freelance software developer, San Francisco (2025).** Profit USD 150,000; deductible SE tax USD 10,597; health USD 9,600; SEP USD 26,081; basic deduction USD 15,750. QBI **USD 103,722**; taxable income **USD 87,972**; tentative USD 20,744.40; cap and **deduction USD 17,594.40**, Form 8995. No categorical software non-SSTB conclusion is required below the threshold.

**Example 3 — Sarah Kim, MFJ, financial adviser (2025).** Profit USD 380,000; deductible SE tax USD 16,007; health USD 14,400; retirement USD 58,000; spouse wages USD 165,000; basic deduction USD 31,500; no other income; no employees or qualifying property. QBI = **USD 291,593**; AGI = USD 456,593; taxable income before QBI = **USD 425,093**. Phase fraction = (425,093 − 394,600) / 100,000 = **30.493%**, applicable percentage **69.507%**. Adjusted QBI USD 202,677.54651; tentative USD 40,535.509302; after the second phase-in factor, **deduction USD 28,175.02**, below the USD 85,018.60 cap. The old USD 28,177 answer used premature intermediate rounding.

**Test 1 — Basic 2025 below-threshold computation.** Profit USD 80,000; deductible SE tax USD 5,652; health USD 6,000; SEP USD 13,470; single; basic deduction USD 15,750; no capital gains. QBI USD 54,878; tentative USD 10,975.60; taxable income USD 39,128; cap and **deduction USD 7,825.60** (USD 7,826 whole dollars).

**Test 2 — 2025 loss.** Schedule C loss USD 15,000; deductible SE tax zero; single. With no other QBI/REIT/PTP component, ordinary deduction **zero** and qualified loss carried to 2026 **USD 15,000**. The 2025 Form 8995 loss locator is line 16, not the older line 13 reference.

**Test 3 — 2025 non-SSTB with no qualified wages/property.** Profit USD 300,000; deductible SE tax USD 14,935; health USD 12,000; retirement USD 55,000; nonbusiness taxable interest USD 7,685; single; basic deduction USD 15,750. QBI USD 218,065; AGI USD 225,750; taxable income USD 210,000. Fraction (210,000 − 197,300) / 50,000 = 25.4%; tentative USD 43,613; reduction USD 11,077.702; **deduction USD 32,535.30**, below the USD 42,000 cap. The older version supplied USD 210,000 directly; the later USD 7,685 interest reconciles it without changing that input.

The original upstream SE-tax illustration in Test 3 used the 2025 Social Security base USD 176,100, 92.35% earnings factor, 12.4% capped Social Security and 2.9% Medicare: 300,000 × .9235 = 277,050; .124 × 176,100 = 21,836.40; .029 × 277,050 = 8,034.45; half of their sum = USD 14,935.425, explaining the original whole-dollar USD 14,935 input. Sarah's USD 380,000 illustration similarly gives earnings USD 350,930, Medicare USD 10,176.97 and regular SE tax USD 32,013.37, whose half USD 16,006.685 explains the supplied USD 16,007. These are dated upstream illustrations; do not use the 2025 base for 2026 or ignore the same person's employment wages when establishing their remaining base.

**Test 4 — 2025 SSTB above the range.** Accounting-firm profit USD 350,000; single; taxable income before QBI USD 260,000. It exceeds the USD 247,300 completion point; **ordinary deduction zero**. No 2026 minimum applies.

**Test 5 — 2025 below-threshold legal consulting.** Profit USD 100,000; deductible SE tax USD 7,065; health USD 7,200; retirement USD 30,000; single; basic deduction USD 15,750; no other income. QBI USD 55,735; taxable income USD 39,985; tentative USD 11,147; cap and **deduction USD 7,997**.

**Test 6 — 2025 taxable income cap.** Profit USD 50,000; no retirement or health deduction; deductible SE tax USD 3,532; single; stipulated allowable mortgage/SALT/charitable itemized deduction USD 30,000. QBI USD 46,468; taxable income USD 16,468; tentative USD 9,293.60; cap and **deduction USD 3,293.60** (USD 3,294 whole dollars). Itemized-deduction eligibility is an upstream condition.

**Superseded historical variants — preserve and reconcile, do not file from them.** The earliest Test 1 used USD 15,000 rather than the enacted 2025 USD 15,750 basic deduction: its stipulated arithmetic gives taxable income USD 39,878 and cap USD 7,975.60; applying the enacted amount gives Test 1 above. Earliest Test 3 used deductible SE tax USD 20,405, profit USD 300,000, health USD 12,000, retirement USD 55,000 and separately stipulated taxable income USD 210,000: QBI USD 212,595, tentative USD 42,519 and phased result USD 31,719.17. That upstream SE-tax input is not established by this Guide; the later USD 14,935 version is shown separately. Earliest Test 5 independently stipulated taxable income USD 45,000 with the same USD 55,735 QBI: cap/result USD 9,000; it cannot also follow from the later no-other-income inputs without an additional USD 5,015 taxable-income item. Retain both as distinct conditional scenarios.

The earlier Sarah Kim version used spouse wages **USD 120,000** and separately stated taxable income **USD 425,000**, with profit USD 380,000, health USD 14,400 and retirement USD 58,000. With deductible SE tax USD 16,007 and the 2025 USD 31,500 deduction, those listed inputs instead give taxable income **USD 380,093**; reaching the stipulated USD 425,000 requires **USD 44,907** of additional net taxable-income items. The separately stipulated USD 425,000 scenario has phase 30.4% and, with QBI USD 291,593 and no wages/property, deduction **USD 28,250.46**. The earlier **USD 23,886** SE-tax input instead gives QBI USD 283,714 and listed-input taxable income USD 372,214 (a **USD 52,786** gap to USD 425,000); treating USD 425,000 as independently stipulated gives deduction **USD 27,487.12**. Both SE-tax eligibility and missing-income reconciliation are holds: **Check this point with one of our partner accountants.** The later USD 165,000 spouse-wage case above is kept as its own version, not substituted into these historical inputs.

```oa-check
name: Original 2025 examples and tests, retaining stipulated upstream amounts
inputs:
  maria_profit: 62644
  maria_se: 4427
  maria_health: 8400
  maria_employee: 23500
  maria_employer: 7264
  james_profit: 150000
  james_se: 10597
  james_health: 9600
  james_sep: 26081
  sarah_profit: 380000
  sarah_se: 16007
  sarah_health: 14400
  sarah_retirement: 58000
  spouse: 165000
  standard_single: 15750
  standard_joint: 31500
  joint_threshold: 394600
  joint_range: 100000
steps:
  - maria_qbi: maria_profit - maria_se - maria_health - maria_employee - maria_employer
  - maria_ti: maria_qbi - standard_single
  - maria_deduction: min(0.2 * maria_qbi, 0.2 * maria_ti)
  - james_qbi: james_profit - james_se - james_health - james_sep
  - james_ti: james_qbi - standard_single
  - james_deduction: min(0.2 * james_qbi, 0.2 * james_ti)
  - sarah_qbi: sarah_profit - sarah_se - sarah_health - sarah_retirement
  - sarah_ti: sarah_qbi + spouse - standard_joint
  - sarah_phase: (sarah_ti - joint_threshold) / joint_range
  - sarah_deduction: min(0.2 * sarah_qbi * (1 - sarah_phase) * (1 - sarah_phase), 0.2 * sarah_ti)
  - test1_deduction: 0.2 * (80000 - 5652 - 6000 - 13470 - standard_single)
  - test2_carryforward: max(0, 15000)
  - test3_deduction: 0.2 * (300000 - 14935 - 12000 - 55000) * (1 - (210000 - 197300) / 50000)
  - test4_applicable: 1 - clamp((260000 - 197300) / 50000, 0, 1)
  - test5_deduction: 0.2 * (100000 - 7065 - 7200 - 30000 - standard_single)
  - test6_deduction: 0.2 * (50000 - 3532 - 30000)
expected:
  maria_qbi: 19053
  maria_ti: 3303
  maria_deduction: 660.60
  james_qbi: 103722
  james_ti: 87972
  james_deduction: 17594.40
  sarah_qbi: 291593
  sarah_ti: 425093
  sarah_deduction: 28175.02
  test1_deduction: 7825.60
  test2_carryforward: 15000
  test3_deduction: 32535.30
  test4_applicable: 0
  test5_deduction: 7997
  test6_deduction: 3293.60
```

## When to refuse or refer

For every following specialist topic, the action is: **Check this point with one of our partner accountants.** Stop the affected computation pending that determination; retain the code in the handoff.

- **R-QBI-MULTI:** aggregation election, common ownership, shared operations, reporting and consistency; multiple businesses are not automatically aggregated.
- **R-QBI-K1:** partnership/S corporation QBI, reasonable compensation, guaranteed/service payments and entity wages/property.
- **R-QBI-REIT:** qualified REIT/PTP component and its separate loss carryforward.
- **R-QBI-NOL:** NOL and QBI ordering.
- **R-QBI-SSTB-MIXED:** mixed receipts, uncertain field classification or mid-year character changes.
- **R-QBI-COOP:** agricultural/horticultural cooperative patron and section 199A(g).
- **R-QBI-RENTAL:** rental trade/business and safe-harbor eligibility; use `us-real-estate-professional-and-short-term-rentals` for intake.
- **R-QBI-EMPLOYEE:** former employee/contractor classification and rebuttal.
- **R-QBI-TRUST:** estate, trust, ESBT and allocation.

## Filing and payment

Attach the final applicable Form 8995 or Form 8995-A and required schedules to the return. For ordinary domestic calendar-year individuals, the 2026 filing/payment date is **15 April 2027**; a timely ordinary filing extension gives **15 October 2027**, not extra time to pay. Special deadlines: **Check this point with one of our partner accountants.** The QBI deduction reduces taxable income for federal income tax, not adjusted gross income or self-employment earnings; feed the resulting income-tax computation to `us-quarterly-estimated-tax`. Retain activity/receipts and participation evidence, prior losses, wage filings, the asset register and a year-labelled calculation.

## Sources

Bounded operative sections below were read on **2026-11-26**; unchanged completed US1040/Schedule C source reads were reused after checking the year and conditions. Law controls over forms. Older regulations are used for structural rules, not obsolete year amounts.

| Source and sections actually read | Official URL | Read on |
| --- | --- | --- |
| Section 199A(a)–(f): definitions, cap, wages, property, threshold exception, phase-in, loss carryover, income-tax-only treatment; read with enacted amendments below | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec199A.htm | 2026-11-26 |
| Public Law 119-21 sections 70105 and 70111: post-2025 ranges, replacement minimum and effective dates; section 68 coordination | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-26 |
| Rev. Proc. 2025-32 sections 4.14 and 4.26: 2026 basic standard deductions and QBI thresholds | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-26 |
| Rev. Proc. 2024-40 section 3.27: 2025 QBI thresholds | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-26 |
| Publication 501 Table 6: 2025 basic deductions, with its age/blindness/dependent caveats; completed US1040 read reused | https://www.irs.gov/publications/p501 | 2026-11-26 |
| Schedule SE 2025 lines 4a and 7–13: earnings factor, combined wage base, regular rates and deductible half in historical upstream calculations | https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf | 2026-11-26 |
| Publication 925 material-participation tests: more than 500 hours | https://www.irs.gov/publications/p925 | 2026-11-26 |
| Form 8995 instructions: section 162/US-connected items, excluded wages/tips, QBI adjustments, suspended losses, prior loss and aggregation schedule; 2025-year figures used only for 2025 | https://www.irs.gov/instructions/i8995 | 2026-11-26 |
| Treas. Reg. 1.199A-1(d)(2)(iii): proportional loss netting, separate-business loss carryover and exclusion of loss-business wages/property | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol4/xml/CFR-2025-title26-vol4-sec1-199A-1.xml | 2026-11-26 |
| Treas. Reg. 1.199A-2(b)(2), (c)(3)(i): payroll-provider wages and UBIA business-use/expensing adjustments | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol4/xml/CFR-2025-title26-vol4-sec1-199A-2.xml | 2026-11-26 |
| Treas. Reg. 1.199A-3(b)(1)(vi): gross-income attribution of deductible SE tax, health and retirement | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol4/xml/CFR-2025-title26-vol4-sec1-199A-3.xml | 2026-11-26 |
| Treas. Reg. 1.199A-5(b), (c)(1), (d)(3): listed fields, consulting, de minimis and former employees | https://www.govinfo.gov/content/pkg/CFR-2025-title26-vol4/xml/CFR-2025-title26-vol4-sec1-199A-5.xml | 2026-11-26 |
| Form 8995 2026 draft: threshold and arithmetic lines 1–20; DO NOT FILE | https://www.irs.gov/pub/irs-dft/f8995--dft.pdf | 2026-11-26 |
| Form 8995-A 2026 draft: threshold and Parts I–IV; DO NOT FILE | https://www.irs.gov/pub/irs-dft/f8995a--dft.pdf | 2026-11-26 |
| Form 8995 2026 draft instructions: lines 11, 12, 16–19 and draft Form 1040 line 13b | https://www.irs.gov/pub/irs-dft/i8995--dft.pdf | 2026-11-26 |
| IRS 2026 calendar-year individual deadline and ordinary extension | https://www.irs.gov/individual-tax-filing and https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return | 2026-11-26 |

Not yet confirmed: final 2026 form locators are not established by the draft reads; do not use draft lines for filing. Minimum-deduction cases with zero/negative taxable income, mixed active/passive losses or uncertain qualified active QBI, plus the specialist topics expressly referred above, are non-usable pending partner determination. Historical superseded inputs below are preserved for reconciliation and are not claims of actual deduction eligibility.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).
