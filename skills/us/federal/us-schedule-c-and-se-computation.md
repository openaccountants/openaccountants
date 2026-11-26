---
name: us-schedule-c-and-se-computation
description: Compute an ordinary US sole proprietor’s 2026 Schedule C profit, home-office deduction and Schedule SE tax, with the self-employment part of Form 8959. Includes disregarded single-member LLCs; federal only. Trigger on Schedule C, Schedule SE, self-employment tax, 1099 contractor tax, home-office deduction or Form 8829. Use us-sole-prop-bookkeeping first when transactions need classifying.
version: "3.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US Schedule C net profit and self-employment tax, tax year 2026

Obtain professional review before filing. The examples use hypothetical inputs; resolve the actual eligibility, accounting method, wages and other business income before using their calculations for a return.

**Answer first.** For ordinary covered 2026 self-employment, apply 12.4% Social Security and 2.9% Medicare to the Schedule SE earnings calculation, normally 92.35% of the person's combined eligible business profits and losses. The Social Security part stops at the **$184,500** wage/earnings base; the ordinary earnings floor is **$400**. Deduct half the regular SE tax on Schedule 1, line 15, excluding Additional Medicare Tax. The latter is 0.9% above the applicable $200,000 / $250,000 joint / $125,000 separate threshold after Medicare wages; a joint return combines both spouses' wages and positive SE income. Apply the separate steps and scope exceptions below. [1401](https://uscode.house.gov/us/usc/t26/s1401/); [1402](https://uscode.house.gov/us/usc/t26/s1402/); [2026 SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf).

## Scope and who this is for

In scope: one individual's Schedule C (Form 1040) for tax year 2026 (a sole proprietorship or a single-member LLC treated as disregarded), the home office deduction on line 30, and Schedule SE Part I. The result feeds Schedule 2, line 4 (self-employment tax), Schedule 1, line 15 (the deductible half) and Form 8959 (Additional Medicare Tax).

For statutory-employee income, nonresident/totalization coverage, an approved SE exemption, railroad compensation or other special coverage, check this with one of our partner accountants before applying the ordinary SE calculation. Statutory-employee Schedule C net income is not entered on SE line 2. [SE instructions](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf); [1401(c)](https://uscode.house.gov/us/usc/t26/s1401/); [1402(b)–(c)](https://uscode.house.gov/us/usc/t26/s1402/).

Out-of-scope calculations require a partner accountant. These related skills are navigation references, not a claim that their computations have been checked here:

| Topic | Skill |
| --- | --- |
| Classifying bank and card transactions into Schedule C lines | `us-sole-prop-bookkeeping` |
| Section 179 and bonus depreciation figures | `us-section-179-and-bonus-depreciation` |
| The qualified business income deduction | `us-qbi-deduction` |
| 1099-NEC and 1099-K thresholds and matching | `us-1099-nec-issuance`, `us-1099-k-and-payment-processors` |
| Self-employed health insurance and retirement plans | `us-self-employed-health-insurance`, `us-self-employed-retirement` |
| Paying the tax during the year | `us-quarterly-estimated-tax` |
| State income tax on the same profit | the state's income tax skill |

## Ask the client first

1. **Actual filing status and all business profits/losses for 2026.** Each spouse has a separate Schedule SE; obtain verified amounts from every business rather than ignoring a loss or another business. For joint Additional Medicare Tax, obtain both spouses' Medicare wages/tips and positive Schedule SE income. [SE instructions](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf); [8959](https://www.irs.gov/instructions/i8959).
2. **Wages and coverage:** all W-2 boxes 3, 5 and 7, unreported tips, Form 8919 wages and any railroad compensation. Resolve the special items with the partner before computing the available Social Security base or Medicare threshold. [SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf); [8959](https://www.irs.gov/instructions/i8959).
3. **Home office:** the qualifying principal-business/client-meeting/separate-structure route, dates and square feet of eligible use, total home area, substantiated costs, conversion-date adjusted basis/FMV and land value, prior depreciation/methods, and the proposed election. Square feet alone do not establish eligibility. Storage/daycare, shared space, rental use and multiple-business allocations require the partner's applicable calculation. [280A](https://uscode.house.gov/us/usc/t26/s280A/).
4. **Vehicle:** business miles driven 1 January to 30 June and 1 July to 31 December 2026 separately (the standard mileage rate changed on 1 July); owned or leased; the method chosen in its first business-use year; and any later actual-expense, depreciation, section 179, bonus-depreciation or simultaneous-fleet use.
5. **Prior-year Form 8829 carryovers** (operating expenses and excess casualty losses and depreciation not allowed in 2025).
6. **Losses and risk:** is any of the investment not at risk (nonrecourse debt, guarantees), and has the business had losses in most recent years?
7. **Accounting method:** establish cash/accrual/inventory treatment before determining the year's receipts or expenses. The received-income steps below are conditional on the cash method; for another method, check this with one of our partner accountants. [451(a)](https://uscode.house.gov/us/usc/t26/s451/).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Social Security part of self-employment tax | 12.4% | [26 U.S.C. 1401(a)](https://uscode.house.gov/us/usc/t26/s1401/) |
| Medicare part of self-employment tax | 2.9% | [26 U.S.C. 1401(b)(1)](https://uscode.house.gov/us/usc/t26/s1401/) |
| Additional Medicare Tax on self-employment income | 0.9% | [26 U.S.C. 1401(b)(2)](https://uscode.house.gov/us/usc/t26/s1401/) |
| Additional Medicare Tax threshold, single, head of household, qualifying surviving spouse | USD 200,000 | [26 U.S.C. 1401(b)(2)(A)(iii)](https://uscode.house.gov/us/usc/t26/s1401/) |
| Additional Medicare Tax threshold, married filing jointly | USD 250,000 | [26 U.S.C. 1401(b)(2)(A)(i)](https://uscode.house.gov/us/usc/t26/s1401/) |
| Additional Medicare Tax threshold, married filing separately | USD 125,000 (derived: half of the USD 250,000 joint threshold) | [26 U.S.C. 1401(b)(2)(A)(ii)](https://uscode.house.gov/us/usc/t26/s1401/) |
| Social Security wage base (wages plus net self-employment earnings) | USD 184,500 | [Schedule SE (Form 1040) 2026, line 7](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Net earnings factor (Schedule SE line 4a) | 92.35% | [Schedule SE (Form 1040) 2026, line 4a](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| No self-employment tax below this net earnings amount | USD 400 | [26 U.S.C. 1402(b)](https://uscode.house.gov/us/usc/t26/s1402/) |
| Deductible share of self-employment tax (Schedule SE line 13) | 50% | [Schedule SE (Form 1040) 2026, line 13](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Optional methods, maximum net earnings | USD 7,560 | [Schedule SE (Form 1040) 2026, Part II](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Nonfarm optional method: net nonfarm profits must be less than | USD 8,186 | [Schedule SE (Form 1040) 2026, Part II](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Nonfarm optional method: profits must also be less than this share of gross nonfarm income | 72.189% | [Schedule SE (Form 1040) 2026, Part II](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Simplified home office rate | USD 5 per square foot | [Rev. Proc. 2013-13, section 4.01](https://www.irs.gov/pub/irs-drop/rp-13-13.pdf) |
| Simplified home office area cap | 300 square feet | [Rev. Proc. 2013-13, section 4.01](https://www.irs.gov/pub/irs-drop/rp-13-13.pdf) |
| Standard mileage rate, business, 1 January to 30 June 2026 | 72.5 cents | [IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates) |
| Standard mileage rate, business, 1 July to 31 December 2026 | 76 cents | [IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates) |

### Schedule C: from gross receipts to net profit

1. **Line 1, gross receipts.** Under the established cash method, include actual and constructive business receipts for 2026 before processor fees. Constructive receipt includes amounts made available without substantial restrictions; another accounting method requires its own timing. Classify processor fees by their actual nature and the Schedule C instructions, without a universal line 27b assignment. Reconcile business records with all 1099-NEC/1099-K forms, report business income once, resolve errors/nonbusiness amounts and attach the required explanation where 1099-NEC totals exceed line 1. [451(a)](https://uscode.house.gov/us/usc/t26/s451/); [constructive receipt](https://www.ecfr.gov/current/title-26/section-1.451-2); [Schedule C line 1](https://www.irs.gov/instructions/i1040sc); [1099-K recipients](https://www.irs.gov/businesses/what-to-do-with-form-1099-k); [duplicate reporting FAQ Q11](https://www.irs.gov/newsroom/form-1099-k-faqs-third-party-filers-of-form-1099-k).
2. **Lines 2 to 7.** Subtract returns and allowances (line 2) and cost of goods sold from Part III (line 4); add other business income (line 6). Line 7 is gross income.
3. **Lines 8 to 27b, expenses.** Use substantiated ordinary and necessary business expenses, with capitalization and specific restrictions resolved before deduction. Line 9: eligible mileage for each half of 2026, or the applicable actual-cost method; first apply the vehicle-history conditions below. Line 13 depreciation/section 179 and line 27a Form 7205 need their applicable calculations; other expenses listed in Part V total to 27b. Ordinary eligible business meals on 24b generally have a 50% limit, not automatic eligibility: substantiate the business purpose, nonlavish amount and taxpayer/employee presence. For meals connected with entertainment, travel or a statutory exception, check the applicable conditions with one of our partner accountants. [162(a)](https://uscode.house.gov/us/usc/t26/s162/); [274(k)/(n)](https://uscode.house.gov/us/usc/t26/s274/); [Schedule C](https://www.irs.gov/instructions/i1040sc).
4. **Line 28** adds lines 8 to 27b. **Line 29**, tentative profit, is line 7 minus line 28.
5. **Line 30, home office.** First establish section 280A(c)(1) eligibility: regular exclusive use as the principal place of business, for client/customer/patient meetings in the normal business course, or in an unattached separate structure used in the business. A principal business location includes administration/management where no other fixed location conducts substantial administration/management. Storage/daycare exceptions, rental use and shared/multiple-business allocations require a partner accountant's calculation. [280A(c)](https://uscode.house.gov/us/usc/t26/s280A/).
   - **Simplified:** USD 5 × allowable square feet, maximum 300. For part-year or changing-area use, average monthly allowable square feet over the year's months, capped at 300 per month; count a month only with at least 15 days of qualifying use. Elect on a timely filed original return; irrevocable for that year. Only one home may use the method. No home depreciation or carryforward of an unused simplified amount; earlier actual-method carryovers are held for the next eligible actual-method year. Only independently allowable itemized home deductions remain on Schedule A, subject to their own limits. [Rev. Proc. 2013-13 sections 4.01, 4.03–4.08](https://www.irs.gov/pub/irs-drop/rp-13-13.pdf).
   - **Actual (Form 8829):** use costs during qualifying use, direct/indirect allocation and the supported business share. Allocate business-use gross income where work at other locations requires it. For conversion from personal use, use the lower of adjusted basis or fair market value at conversion, excluding land, to determine depreciable building basis; do not simply depreciate purchase cost. Ordinary MACRS nonresidential real property uses 39-year straight line and the mid-month convention; the first year's amount depends on the service month. For older property, another system or a change from simplified, check the applicable depreciation table with one of our partner accountants. [basis regulation](https://www.ecfr.gov/current/title-26/section-1.167(g)-1); [168(b)–(d)](https://uscode.house.gov/us/usc/t26/s168/); [Pub. 587](https://www.irs.gov/publications/p587).
   - Simplified: the deduction is limited to business-use gross income after the other business deductions; the unused simplified amount is not carried forward. Actual: apply the Form 8829 ordering. First separate only the business part of costs otherwise allowable as personal deductions, subject to their own limits. Mortgage interest and real estate taxes enter this first tier only to the extent otherwise deductible on Schedule A. For a client taking the standard deduction, the entire qualifying business share of those interest and tax costs instead joins the limited operating-cost tier; an itemizer’s excess interest and real estate taxes also join that tier. Interest must relate to loans used to buy, build or substantially improve the home. Apply the remaining business-use income limit to operating costs, then apply the final tier to excess casualty losses and home depreciation. The [2025 Form 8829 instructions, Lines 9 to 17](https://www.irs.gov/instructions/i8829), explain that standard-deduction filers “will not include any mortgage interest or real estate taxes on lines 10 and 11”; use that structural distinction without assuming the 2025 line numbers are final for 2026. Only the limited, unallowed actual costs carry forward, subject to the limit in a later actual-method year. Do not cap every actual cost indiscriminately at tentative profit. [26 U.S.C. 280A(b) and (c)(5)](https://uscode.house.gov/us/usc/t26/s280A/) distinguish independently deductible items from the limited expenses. [IRS Pub. 587, Deduction Limit](https://www.irs.gov/publications/p587), describes the limited costs as “otherwise nondeductible expenses” and specifies “with depreciation of your home taken last”.
6. **Line 31, net profit or loss** = line 29 minus line 30. Before using a loss, have the partner resolve any at-risk, passive-activity, excess-business-loss or NOL restrictions. Do not tick line 32a from an assumption about financing. [Schedule C loss instructions](https://www.irs.gov/instructions/i1040sc).

### Schedule SE Part I: self-employment tax

7. **Line 2** combines the person's eligible Schedule C profits and losses and any verified partnership SE amount. A loss in one business reduces income from another in that person's Schedule SE calculation; compute the combined tax on one Schedule SE. Obtain the partner's applicable farm/partnership/special-income figures before combining them; their computation is outside this skill. Do not offset one spouse's earnings against the other's on a single Schedule SE. [1402(a)](https://uscode.house.gov/us/usc/t26/s1402/); [SE instructions, More Than One Business / Joint Returns](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf).
8. **Line 4a** = line 3 times 92.35% (0.9235), if line 3 is more than zero. Source: [Schedule SE (Form 1040) 2026](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf).
9. **Line 4c**: if under USD 400, stop; no self-employment tax is due (church employee income excepted). Source: [26 U.S.C. 1402(b)](https://uscode.house.gov/us/usc/t26/s1402/).
10. **Lines 7 to 9**: line 7 is USD 184,500. Subtract the applicable line 8 wages/tips and other items, including the prescribed railroad tier 1 compensation on 8a where relevant. Obtain the partner's railroad/special-wage determination rather than silently treating ordinary W-2 boxes 3 and 7 as exhaustive. Line 9 is the remaining Social Security base, not below zero. [2026 Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf); [1402(b)](https://uscode.house.gov/us/usc/t26/s1402/).
11. **Line 10** = the smaller of line 6 or line 9, times 12.4%. **Line 11** = line 6 times 2.9%, with no cap.
12. **Line 12**, self-employment tax = line 10 plus line 11. It goes to Schedule 2, line 4.
13. **Line 13**, the deduction = line 12 times 50%, to Schedule 1, line 15. The deduction is one-half of the section 1401 taxes other than the 0.9% Additional Medicare Tax, so the 0.9% is never in the deductible half. Source: [26 U.S.C. 164(f)](https://uscode.house.gov/us/usc/t26/s164/).

### Form 8959: Additional Medicare Tax on self-employment income

14. Establish the actual filing status and inputs first. **For a joint return, the wages and SE income used in the calculation below are both spouses' combined Medicare wages/tips and the sum of their positive Schedule SE line 6 amounts.** Include applicable Form 4137/8919 wage/tip amounts and disregard a negative Schedule SE amount for Form 8959. Take the threshold for the filing status (USD 200,000, 250,000 or 125,000). Reduce it, not below zero, by the person's Medicare wages. Self-employment income (Schedule SE line 6) above the reduced threshold is taxed at 0.9%. A business loss may reduce that person's combined ordinary SE earnings under step 7 but does not reduce Medicare wages. RRTA compensation has a separate calculation and does not reduce this SE threshold: check it with one of our partner accountants. [1401(b)(2)](https://uscode.house.gov/us/usc/t26/s1401/); [regulation 1.1401-1(d)](https://www.ecfr.gov/current/title-26/section-1.1401-1); [8959](https://www.irs.gov/instructions/i8959).

### How the result flows on

The deductible half belongs on Schedule 1, not as an expense reducing Schedule C profit. For QBI, have the partner determine the qualified-business classification and the share of the deduction attributable to it; do not automatically subtract every SE deduction from every business's QBI. [164(f)](https://uscode.house.gov/us/usc/t26/s164/); [IRS QBI](https://www.irs.gov/newsroom/qualified-business-income-deduction).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Net earnings (line 4c) under USD 400 | No self-employment tax; Schedule SE not required for this person |
| Wages already at or above USD 184,500 | Line 9 is zero: only the 2.9% applies to self-employment earnings |
| Schedule C loss | Combine eligible profits/losses from all of that person’s businesses on one Schedule SE; a loss can reduce other SE income. It does not reduce Medicare wages or offset the other spouse’s positive SE income for Form 8959. [SE instructions](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf); [8959](https://www.irs.gov/instructions/i8959) |
| Home office costs larger than tentative profit | Simplified amount is limited and the unused amount does not carry forward. Actual costs require Form 8829 ordering: otherwise deductible personal items first; operating costs next, including all qualifying interest and real estate taxes for a standard-deduction filer and the excess for an itemizer; excess casualty losses and depreciation in the final tier. Limited excess carries to a later actual-method year |
| Home depreciation taken (actual method) | Section 121(d)(6) prevents excluding sale gain up to the relevant depreciation adjustments attributable to periods after 6 May 1997; it does not guarantee tax on every sale. For basis, actual gain/loss, allowed/allowable depreciation and a separate structure, check this with one of our partner accountants. [121(d)(6)](https://uscode.house.gov/us/usc/t26/s121/) |
| Vehicle used with the actual method in an earlier year | For an owned car, mileage must have been chosen in the first year the car was available for business use. If actual expenses were used in that first year, mileage cannot be adopted later. After a qualifying first-year mileage election, either method can be available in later years. When switching from mileage to actual expenses before the car is fully depreciated, estimate its remaining useful life and use straight-line depreciation over that remaining life, subject to the vehicle depreciation limits. Check disqualifiers: non-straight-line depreciation/MACRS, section 179, bonus depreciation, five or more cars used simultaneously, and actual expenses after 1997 for a leased car. For a lease, mileage must generally continue throughout the lease period. [IRS Pub. 463, Choosing the standard mileage rate](https://www.irs.gov/publications/p463): “Then, in later years, you can choose to use either the standard mileage rate or actual expenses.” |
| Married couple both self-employed | Two Schedules SE; each spouse has their own USD 184,500 base |
| Low earnings and the client wants Social Security credits | Nonfarm optional eligibility requires profits below USD 8,186 and below 72.189% of gross, plus actual net earnings of at least USD 400 in 2 of the preceding 3 years; maximum five taxable years. The elected amount is two-thirds of gross nonfarm income, limited to the available combined optional-method cap and not below actual nonfarm net earnings. USD 7,560 is a ceiling, not an automatic election. For a combined farm/nonfarm election or uncertain eligibility, check this with one of our partner accountants. [1402(a)/(h)/(l)](https://uscode.house.gov/us/usc/t26/s1402/); [2026 SE instructions Part II](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Wages/other businesses or coverage | Obtain all wage, business and coverage records; hold the affected SE/8959 result rather than assuming no wages or other income |
| Filing status | Establish the actual legal status and spouse facts; do not substitute Single |
| Prior-year Form 8829 carryover | Obtain the prior form and reconcile; do not invent zero. Simplified years hold actual-method carryovers for an eligible actual-method year |
| Building basis/FMV, land, service date or depreciation history | Hold depreciation until the proper basis, period, convention and applicable table are established |
| Simplified or actual home office method | Ask; do not choose for the client |
| At-risk status | Obtain support for the actual at-risk amount and partner review of the loss limits; do not default to line 32a |
| A loss large enough to create a net operating loss | Stop (R-SE-NOL) |
| Gross receipts below the 1099 totals received | Reconcile records and form discrepancies, including duplicate, nontaxable or erroneous amounts; do not assume omitted income. Attach the required 1099-NEC explanation where applicable |

## Worked cases

**Case 1, a decision: simplified or actual home office?** A single designer has 2026 tentative profit (line 29) of USD 60,000 and no wages. The office is 200 of the home's 2,000 square feet (10%). Indirect home expenses: mortgage interest USD 12,000, real estate tax USD 6,000, insurance USD 1,500, utilities USD 3,500 (USD 23,000 total). The building's basis is USD 300,000 and it is in a full year of 39-year straight-line depreciation (2.564%). Assume full-year eligible principal-business use, substantiated costs, a proper USD 300,000 depreciable building basis after the conversion/land rules, and the applicable full subsequent-year 2.564% rate; these are hypothetical assumptions, not verified client facts.

Simplified: 200 x USD 5 = USD 1,000. Actual: 10% x USD 23,000 = USD 2,300, plus depreciation 10% x USD 300,000 x 2.564% = USD 769.20, total USD 3,069.20. The profit limit does not bind. SE tax is USD 8,336.43 with simplified and USD 8,044.07 with actual expenses: USD 292.36 less on these inputs. The actual deduction is USD 2,069.20 larger, but the business USD 1,800 of interest/taxes is not also deductible on Schedule A, and USD 769.20 of depreciation affects basis and potentially taxable gain. Show both methods; the election depends on eligibility, substantiation, itemization/limits, carryovers and sale facts, not just an intention to retain the home.

```oa-check
name: Home office decision, simplified against actual (2026)
inputs:
  tentative_profit: 60000
  office_sqft: 200
  home_share: 0.10
  indirect_expenses: 23000
  building_basis: 300000
  depreciation_rate: 0.02564
steps:
  - simplified: min(office_sqft, 300) * 5
  - actual: home_share * indirect_expenses + home_share * building_basis * depreciation_rate
  - net_simplified: tentative_profit - min(simplified, tentative_profit)
  - net_actual: tentative_profit - min(actual, tentative_profit)
  - se_simplified: net_simplified * 0.9235 * 0.153
  - se_actual: net_actual * 0.9235 * 0.153
  - se_saving: se_simplified - se_actual
expected:
  simplified: 1000.00
  actual: 3069.20
  se_simplified: 8336.43
  se_actual: 8044.07
  se_saving: 292.36
```

The profit cap does not bind in Case 1. Its oa-check compares only the stated inputs; use the Form 8829 ordering above for an actual-expense case where the limit binds.

**Case 2, wages plus self-employment, single.** A single filer earns USD 100,000 of W-2 wages (boxes 3 and 5) and has Schedule C net profit of USD 120,000.

Line 4a: USD 120,000 x 92.35% = USD 110,820. Line 9: USD 184,500 minus USD 100,000 = USD 84,500 of Social Security base left. Line 10: the smaller of USD 110,820 and USD 84,500 is USD 84,500, times 12.4% = USD 10,478. Line 11: USD 110,820 x 2.9% = USD 3,213.78. Line 12, self-employment tax: USD 13,691.78. Line 13, deductible half: USD 6,845.89. Form 8959: the USD 200,000 threshold less USD 100,000 of wages leaves USD 100,000; self-employment income above it is USD 10,820, times 0.9% = USD 97.38 of Additional Medicare Tax, which is not part of the deductible half.

```oa-check
name: Wages plus Schedule C profit, single (2026)
inputs:
  wages: 100000
  schedule_c_profit: 120000
  wage_base: 184500
  threshold: 200000
steps:
  - line_4a: schedule_c_profit * 0.9235
  - line_9: max(wage_base - wages, 0)
  - line_10: min(line_4a, line_9) * 0.124
  - line_11: line_4a * 0.029
  - line_12: line_10 + line_11
  - line_13: line_12 * 0.5
  - additional_medicare: max(line_4a - max(threshold - wages, 0), 0) * 0.009
expected:
  line_4a: 110820.00
  line_10: 10478.00
  line_11: 3213.78
  line_12: 13691.78
  line_13: 6845.89
  additional_medicare: 97.38
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-SE-NOL | The loss produces a net operating loss for the year | Refer: section 172 computation is outside this skill |
| R-SE-ATRISK | Some investment is not at risk (Schedule C line 32b, Form 6198) | Refer: section 465 limits apply before the loss is used |
| R-SE-FARM | Farm income | Use Schedule F, not Schedule C |
| R-SE-CHURCH | Church employee income or a minister's earnings | Refer: special Schedule SE rules apply |
| R-SE-PARTNER | Partnership or multi-member LLC | Check entity elections and any applicable spousal/community-property classification with a partner accountant; do not assert that every LLC files Form 1065. [Schedule C entity instructions](https://www.irs.gov/instructions/i1040sc) |
| R-SE-HOBBY | Losses in most recent years and no profit motive evident | Flag: the activity may not be a business; a reviewer decides |

## Filing and payment

For an ordinary domestic calendar-year 2026 individual return, the filing date is **15 April 2027**. A timely obtained ordinary filing extension runs to **15 October 2027** and does not extend payment. Attach Schedule C, Schedule SE, Form 8829 and Form 8959 when their filing requirements apply; owing Additional Medicare Tax is not the only Form 8959 filing trigger. For overseas, nonresident, disaster or other special relief, check the operative date with one of our partner accountants. [6072(a)](https://uscode.house.gov/us/usc/t26/s6072/); [6081](https://uscode.house.gov/us/usc/t26/s6081/); [6151(a)](https://uscode.house.gov/us/usc/t26/s6151/); [IRS extension](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return); [8959 filing tests](https://www.irs.gov/instructions/i8959).

SE tax is part of the estimated-tax calculation, not a separate automatic duty to make four cash payments. Determine required installments after withholding, credits, the applicable safe harbour and exceptions. When required under the ordinary calendar-year schedule, dates are 15 April, 15 June and 15 September 2026, and 15 January 2027. The January installment exception applies if the 2026 return is filed and the full balance paid by **1 February 2027** (the January 31 statutory date falls on Sunday). For a safe-harbour, annualized-income or special-case calculation, check this with one of our partner accountants. [6654(c), (f)–(h)](https://uscode.house.gov/us/usc/t26/s6654/); [7503](https://uscode.house.gov/us/usc/t26/s7503/); [2026 1040-ES](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).

Apply all Form 8959 filing tests, including a single W-2 Medicare-wage or RRTA-compensation amount above USD 200,000 even if joint liability is zero; include the relevant spouse and special wage/tip amounts. [8959](https://www.irs.gov/instructions/i8959).

**Circular 230 §10.37 disclosure:** This is a computational aid, not an individualized tax opinion. A qualified US practitioner must review the client facts, assumptions, authorities and results before filing.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Schedule C line 1 instructions and 1099-K recipient guidance; gross receipts, reconciliation and incorrect/nonbusiness amounts. The Schedule C instructions currently display 2025; only unchanged structural rules are used, checked against the 2026 form. | https://www.irs.gov/instructions/i1040sc ; https://www.irs.gov/businesses/what-to-do-with-form-1099-k | 2026-11-22 |
| IRS third-party-filer 1099-K FAQ, Q11; no duplicate information reporting of the same transaction. | https://www.irs.gov/newsroom/form-1099-k-faqs-third-party-filers-of-form-1099-k | 2026-11-22 |
| IRS Pub. 463 (currently 2025), Choosing the standard mileage rate and Standard mileage rate not allowed; method history and disqualifiers, not the 2026 mileage amounts. | https://www.irs.gov/publications/p463 | 2026-11-22 |
| Current 26 U.S.C. 280A(b), (c)(5), and IRS Pub. 587 (currently 2025), Deduction Limit; independently deductible items, ordering and carryforward. | https://uscode.house.gov/us/usc/t26/s280A/ ; https://www.irs.gov/publications/p587 | 2026-11-22 |
| IRS Form 8829 instructions (currently 2025), Lines 9 to 17 and Line 29; standard-deduction versus itemized treatment, excess interest/taxes and excess casualty-loss ordering. Read for the structural rules; 2025 line numbers are source anchors, not a claim about final 2026 form lines. | https://www.irs.gov/instructions/i8829 | 2026-11-22 |
| Schedule SE (Form 1040) 2026. Read for lines 4a, 4c, 7 ($184,500), 8a to 13 and Part II optional-method amounts ($7,560, $8,186, 72.189%). | https://www.irs.gov/pub/irs-pdf/f1040sse.pdf | 2026-11-22 |
| Instructions for Schedule SE (Form 1040) 2026. Read for What's New (2026 maximum $184,500) and the optional-method conditions. | https://www.irs.gov/pub/irs-pdf/i1040sse.pdf | 2026-11-22 |
| Schedule C (Form 1040) 2026. Read for lines 1 to 32, line 27a (Form 7205) and Part V to line 27b. | https://www.irs.gov/pub/irs-pdf/f1040sc.pdf | 2026-11-22 |
| IRS Pub. 15 (2026). Read for the social security wage base ($184,500) and the 6.2% and 1.45% employee rates. | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-22 |
| Current 26 U.S.C. 1401; prior bounded audit read reused for (a) 12.4%, (b)(1) 2.9%, (b)(2) 0.9%, the thresholds and (b)(2)(B) reduction by wages. | https://uscode.house.gov/us/usc/t26/s1401/ | 2026-11-22 |
| Current 26 U.S.C. 1402; prior bounded audit read reused for (a)(12) deduction in computing net earnings and (b) the $400 floor. | https://uscode.house.gov/us/usc/t26/s1402/ | 2026-11-22 |
| Current 26 U.S.C. 164(f); prior bounded audit read reused for the one-half deduction, excluding the 1401(b)(2) tax. | https://uscode.house.gov/us/usc/t26/s164/ | 2026-11-22 |
| Current 26 U.S.C. 280A(c)(5); prior bounded audit read reused for the gross income limit and carryforward. | https://uscode.house.gov/us/usc/t26/s280A/ | 2026-11-22 |
| Rev. Proc. 2013-13. Read for section 4.01: $5 rate, 300 square feet. | https://www.irs.gov/pub/irs-drop/rp-13-13.pdf | 2026-11-22 |
| IRS standard mileage rates page. Read for 2026 business rates: 72.5 cents (1 Jan to 30 Jun, IR-2025-128) and 76 cents (1 Jul to 31 Dec, IR-2026-29). | https://www.irs.gov/tax-professionals/standard-mileage-rates | 2026-11-22 |
| Form 1040-ES (2026). Read for the four 2026 payment due dates. | https://www.irs.gov/pub/irs-pdf/f1040es.pdf | 2026-11-22 |

| Source | URL | Read on |
| --- | --- | --- |
| New bounded read: 451(a) accounting-method timing and regulation 1.451-2(a) constructive receipt; IRS Schedule C cash-method guidance supplies the matching saved proof passage. | https://uscode.house.gov/us/usc/t26/s451/ ; https://www.ecfr.gov/current/title-26/section-1.451-2 ; https://www.irs.gov/instructions/i1040sc | 2026-11-26 |
| New bounded read: 280A(c)(1) principal-business/client-meeting/separate-structure eligibility and administrative/management condition; earlier (b)/(c)(5) ordering reused. | https://uscode.house.gov/us/usc/t26/s280A/ | 2026-11-26 |
| New read of Rev. Proc. 2013-13 section 4.08(4)–(7): monthly averaging/15-day rule, shared and multiple business uses, one-home limit. Earlier election/limit/carryover reads reused. | https://www.irs.gov/pub/irs-drop/rp-13-13.pdf | 2026-11-26 |
| New bounded read: 162(a), 274(k)/(n), ordinary business-meal conditions and general 50% limit; special exceptions referred. | https://uscode.house.gov/us/usc/t26/s162/ ; https://uscode.house.gov/us/usc/t26/s274/ | 2026-11-26 |
| New bounded read: regulation 1.167(g)-1 conversion basis; 168(b)(3)/(c)/(d)(2) normal nonresidential straight-line/recovery/mid-month rules. Pub. 587's corresponding basis passage reused. | https://www.ecfr.gov/current/title-26/section-1.167(g)-1 ; https://uscode.house.gov/us/usc/t26/s168/ ; https://www.irs.gov/publications/p587 | 2026-11-26 |
| New bounded read: 121(d)(6), gain attributable to post-6-May-1997 depreciation; not a statement that every sale incurs tax. | https://uscode.house.gov/us/usc/t26/s121/ | 2026-11-26 |
| New bounded reads: 1402(a) aggregate business income/loss, (h)/(l) optional conditions; 2026 SE instructions More Than One Business, Joint Returns, Statutory Employee Income and nonfarm optional computation. | https://uscode.house.gov/us/usc/t26/s1402/ ; https://www.irs.gov/pub/irs-pdf/i1040sse.pdf | 2026-11-26 |
| New bounded read: regulation 1.1401-1(d), threshold/FICA coordination and joint example; Form 8959 joint/negative-income and filing-test passages reused. | https://www.ecfr.gov/current/title-26/section-1.1401-1 ; https://www.irs.gov/instructions/i8959 | 2026-11-26 |
| New bounded reads: 6072(a), 6081(a) and 6151(a) ordinary filing/extension/payment; 6654(c)/(f)–(h) installment calendar/withholding/January exception; 7503 operative text. Existing 1040-ES calendar/February exception read reused. | https://uscode.house.gov/us/usc/t26/s6072/ ; https://uscode.house.gov/us/usc/t26/s6081/ ; https://uscode.house.gov/us/usc/t26/s6151/ ; https://uscode.house.gov/us/usc/t26/s6654/ ; https://uscode.house.gov/us/usc/t26/s7503/ ; https://www.irs.gov/pub/irs-pdf/f1040es.pdf | 2026-11-26 |

Not yet confirmed: results for the referred cases. Obtain the partner accountant's applicable determination; no tax result for those cases is supplied here.
