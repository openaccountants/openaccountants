---
name: us-schedule-c-and-se-computation
description: Compute a US sole proprietor's 2026 Schedule C net profit, the home office deduction (simplified method or Form 8829), and Schedule SE self-employment tax, with the Form 8959 Additional Medicare Tax on self-employment income. Covers single-member LLCs disregarded for federal tax. 2026 figures from the 2026 Schedule SE and IRS Pub. 15, including the Social Security wage base of $184,500, the 92.35% net earnings factor, 12.4% plus 2.9%, the $400 floor, the 0.9% Additional Medicare Tax with its threshold reduced by wages, and the deductible half under section 164(f). Trigger on "Schedule C", "self-employment tax", "SE tax", "Schedule SE", "1099 contractor tax", "home office deduction", "Form 8829", "sole proprietor profit". Load after us-sole-prop-bookkeeping when transactions still need classifying. Federal only.
version: "3.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US Schedule C net profit and self-employment tax, tax year 2026

> **Source-cited draft.** Built from the 2026 Schedule C and Schedule SE (Form 1040), IRS Pub. 15 (2026), Rev. Proc. 2013-13, the IRS standard mileage rates page and 26 U.S.C. 164(f), 280A(c)(5), 1401 and 1402, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, self-employment tax is 15.3% (12.4% Social Security plus 2.9% Medicare) on 92.35% of Schedule C net profit. The 12.4% part stops once wages plus net self-employment earnings reach **$184,500**. Below **$400** of net earnings, no self-employment tax is due. Half of the tax (not counting the 0.9% Additional Medicare Tax) is deducted on Schedule 1, line 15. The 0.9% Additional Medicare Tax applies above $200,000 (single), $250,000 (joint) or $125,000 (separate), and that threshold is first reduced by the person's wages.

## Scope and who this is for

In scope: one individual's Schedule C (Form 1040) for tax year 2026 (a sole proprietorship or a single-member LLC treated as disregarded), the home office deduction on line 30, and Schedule SE Part I. The result feeds Schedule 2, line 4 (self-employment tax), Schedule 1, line 15 (the deductible half) and Form 8959 (Additional Medicare Tax).

Out of scope, and where it goes:

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

1. **Filing status for 2026**, and whether the spouse also has self-employment income. Each spouse files a separate Schedule SE; the Additional Medicare Tax threshold depends on filing status.
2. **W-2 wages for 2026** (Form W-2 box 3 Social Security wages and box 5 Medicare wages, for every job). Wages use up the $184,500 Social Security base first and reduce the Additional Medicare Tax threshold.
3. **Home office:** square feet used regularly and only for the business, total square feet of the home, and whether the client wants the simplified method or actual expenses this year.
4. **Vehicle:** business miles driven 1 January to 30 June and 1 July to 31 December 2026 separately (the standard mileage rate changed on 1 July), and whether the actual-cost method was used for this vehicle in an earlier year.
5. **Prior-year Form 8829 carryovers** (operating expenses and excess casualty losses and depreciation not allowed in 2025).
6. **Losses and risk:** is any of the investment not at risk (nonrecourse debt, guarantees), and has the business had losses in most recent years?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Social Security part of self-employment tax | 12.4% | [26 U.S.C. 1401(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Medicare part of self-employment tax | 2.9% | [26 U.S.C. 1401(b)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Additional Medicare Tax on self-employment income | 0.9% | [26 U.S.C. 1401(b)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Additional Medicare Tax threshold, single, head of household, qualifying surviving spouse | USD 200,000 | [26 U.S.C. 1401(b)(2)(A)(iii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Additional Medicare Tax threshold, married filing jointly | USD 250,000 | [26 U.S.C. 1401(b)(2)(A)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Additional Medicare Tax threshold, married filing separately | USD 125,000 | [26 U.S.C. 1401(b)(2)(A)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm) |
| Social Security wage base (wages plus net self-employment earnings) | USD 184,500 | [Schedule SE (Form 1040) 2026, line 7](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Net earnings factor (Schedule SE line 4a) | 92.35% | [Schedule SE (Form 1040) 2026, line 4a](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| No self-employment tax below this net earnings amount | USD 400 | [26 U.S.C. 1402(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm) |
| Deductible share of self-employment tax (Schedule SE line 13) | 50% | [Schedule SE (Form 1040) 2026, line 13](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Optional methods, maximum net earnings | USD 7,560 | [Schedule SE (Form 1040) 2026, Part II](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Nonfarm optional method: net nonfarm profits must be less than | USD 8,186 | [Schedule SE (Form 1040) 2026, Part II](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Nonfarm optional method: profits must also be less than this share of gross nonfarm income | 72.189% | [Schedule SE (Form 1040) 2026, Part II](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Simplified home office rate | USD 5 per square foot | [Rev. Proc. 2013-13, section 4.01](https://www.irs.gov/pub/irs-drop/rp-13-13.pdf) |
| Simplified home office area cap | 300 square feet | [Rev. Proc. 2013-13, section 4.01](https://www.irs.gov/pub/irs-drop/rp-13-13.pdf) |
| Standard mileage rate, business, 1 January to 30 June 2026 | 72.5 cents | [IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates) |
| Standard mileage rate, business, 1 July to 31 December 2026 | 76 cents | [IRS standard mileage rates](https://www.irs.gov/tax-professionals/standard-mileage-rates) |

None of the statutory rates or the Additional Medicare Tax thresholds is indexed for inflation. The wage base, the optional-method amounts and the mileage rate change each year.

### Schedule C: from gross receipts to net profit

1. **Line 1, gross receipts.** Total business income received in 2026, before fees. Payment processor payouts are grossed up to the amount the customer paid; the processor fee goes on line 27b. Line 1 should be at least the total of every 1099-NEC and 1099-K the client received; the IRS matches them. Source: [Schedule C (Form 1040) 2026](https://www.irs.gov/pub/irs-pdf/f1040sc.pdf).
2. **Lines 2 to 7.** Subtract returns and allowances (line 2) and cost of goods sold from Part III (line 4); add other business income (line 6). Line 7 is gross income.
3. **Lines 8 to 27b, expenses.** Ordinary and necessary business expenses by line, from the bookkeeping working paper. Line 9 car and truck expenses: either business miles times the standard mileage rate for each half of 2026, or actual costs times business-use share. Line 13: depreciation and section 179 (see `us-section-179-and-bonus-depreciation` for the 2026 figures). Line 24b: business meals at 50%. Line 27a is the energy efficient commercial buildings deduction (Form 7205); everything else listed in Part V totals to line 27b.
4. **Line 28** adds lines 8 to 27b. **Line 29**, tentative profit, is line 7 minus line 28.
5. **Line 30, home office.** Choose one method for the year (either can be used in any year):
   - Simplified: square feet used regularly and exclusively for business, up to 300, times USD 5. No depreciation, no carryover, and the home's mortgage interest and taxes stay in full on Schedule A. Source: [Rev. Proc. 2013-13](https://www.irs.gov/pub/irs-drop/rp-13-13.pdf).
   - Actual expenses (Form 8829): business share of the home (office area divided by total area) times indirect expenses (mortgage interest, real estate taxes, insurance, utilities, repairs, rent), plus direct expenses for the office, plus depreciation on the business share of the building (39-year straight line; land is never depreciated). The business share of mortgage interest and taxes moves from Schedule A to Form 8829.
   - Under either method the deduction cannot exceed the gross income from the business use minus the other business deductions, so it cannot create or increase a loss. Under the actual method the excess carries forward to 2027 on Form 8829; under the simplified method it is lost. Source: [26 U.S.C. 280A(c)(5)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec280A.htm).
6. **Line 31, net profit or loss** = line 29 minus line 30. A loss goes to Schedule 1 but first meets the at-risk rules (line 32; see the refusal table).

### Schedule SE Part I: self-employment tax

7. **Line 2** = Schedule C line 31 (plus any partnership self-employment income, which is outside this skill).
8. **Line 4a** = line 3 times 92.35% (0.9235), if line 3 is more than zero. Source: [Schedule SE (Form 1040) 2026](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf).
9. **Line 4c**: if under USD 400, stop; no self-employment tax is due (church employee income excepted). Source: [26 U.S.C. 1402(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm).
10. **Lines 7 to 9**: line 7 is USD 184,500. Subtract Social Security wages and tips (line 8a, W-2 boxes 3 and 7) and other items on lines 8b and 8c. Line 9 is the Social Security base left for self-employment earnings (not below zero).
11. **Line 10** = the smaller of line 6 or line 9, times 12.4%. **Line 11** = line 6 times 2.9%, with no cap.
12. **Line 12**, self-employment tax = line 10 plus line 11. It goes to Schedule 2, line 4.
13. **Line 13**, the deduction = line 12 times 50%, to Schedule 1, line 15. The deduction is one-half of the section 1401 taxes other than the 0.9% Additional Medicare Tax, so the 0.9% is never in the deductible half. Source: [26 U.S.C. 164(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec164.htm).

### Form 8959: Additional Medicare Tax on self-employment income

14. Take the threshold for the filing status (USD 200,000, 250,000 or 125,000). Reduce it, not below zero, by the person's Medicare wages. Self-employment income (Schedule SE line 6) above the reduced threshold is taxed at 0.9%. A loss does not reduce the threshold. Source: [26 U.S.C. 1401(b)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm).

### How the result flows on

The deductible half on Schedule 1 reduces adjusted gross income, not Schedule C profit. It also reduces qualified business income for the section 199A deduction: see `us-qbi-deduction`.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Net earnings (line 4c) under USD 400 | No self-employment tax; Schedule SE not required for this person |
| Wages already at or above USD 184,500 | Line 9 is zero: only the 2.9% applies to self-employment earnings |
| Schedule C loss | No self-employment tax from this business; the loss does not reduce wages for Additional Medicare Tax |
| Home office deduction larger than tentative profit | Capped at the profit (280A(c)(5)); actual method carries the excess forward, simplified method loses it |
| Home depreciation taken (actual method) | The depreciation allowed or allowable is taxed on a later sale of the home and is not covered by the home sale exclusion: tell the client before choosing |
| Vehicle used with the actual method in an earlier year | Cannot switch that vehicle to the standard mileage rate |
| Married couple both self-employed | Two Schedules SE; each spouse has their own USD 184,500 base |
| Low earnings and the client wants Social Security credits | Optional methods (Schedule SE Part II): nonfarm method only if net profits are under USD 8,186 and under 72.189% of gross, with at least USD 400 of net earnings in 2 of the prior 3 years; at most five times in a lifetime |

## Worked cases

**Case 1, a decision: simplified or actual home office?** A single designer has 2026 tentative profit (line 29) of USD 60,000 and no wages. The office is 200 of the home's 2,000 square feet (10%). Indirect home expenses: mortgage interest USD 12,000, real estate tax USD 6,000, insurance USD 1,500, utilities USD 3,500 (USD 23,000 total). The building's basis is USD 300,000 and it is in a full year of 39-year straight-line depreciation (2.564%).

Simplified: 200 x USD 5 = USD 1,000. Actual: 10% x USD 23,000 = USD 2,300, plus depreciation 10% x USD 300,000 x 2.564% = USD 769.20, total USD 3,069.20. Neither exceeds the profit, so no cap applies. Self-employment tax is USD 8,336.43 with the simplified method and USD 8,044.07 with actual expenses: USD 292.36 less, before the income tax saving on a USD 2,069.20 larger deduction. Against that, under the actual method USD 1,800 of the mortgage interest and taxes leaves Schedule A (it matters only if the client itemizes), and the USD 769.20 of depreciation is taxed when the home is sold. Recommend actual expenses if the client does not itemize and plans to keep the home; show both if they itemize.

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
| R-SE-PARTNER | Partnership or LLC with more than one member | Refer: Form 1065 and Schedule K-1 self-employment rules (`us-form-1065-partnership`) |
| R-SE-HOBBY | Losses in most recent years and no profit motive evident | Flag: the activity may not be a business; a reviewer decides |

## Filing and payment

Schedule C, Schedule SE, Form 8829 (actual method) and Form 8959 (if owed) are attached to the 2026 Form 1040, due **15 April 2027**; an extension to 15 October 2027 extends filing, not payment. Self-employment tax is paid through estimated tax during 2026: 15 April, 15 June and 15 September 2026, and 15 January 2027. Source: [Form 1040-ES (2026)](https://www.irs.gov/pub/irs-pdf/f1040es.pdf). The safe-harbour rules are in `us-quarterly-estimated-tax`.

## Completion checklist

- Line 1 is at least the total of the 1099-NEC and 1099-K forms received, or the difference is explained.
- Mileage split between the two 2026 rates.
- Home office method chosen, with the 280A(c)(5) cap applied and any Form 8829 carryover recorded.
- Schedule SE line 8a uses W-2 boxes 3 and 7 from every job.
- Deductible half on Schedule 1 line 15, excluding the 0.9%.
- Form 8959 run whenever wages plus self-employment income could pass the threshold.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Schedule SE (Form 1040) 2026. Read for lines 4a, 4c, 7 ($184,500), 8a to 13 and Part II optional-method amounts ($7,560, $8,186, 72.189%). | https://www.irs.gov/pub/irs-pdf/f1040sse.pdf | 2026-11-13 |
| Instructions for Schedule SE (Form 1040) 2026. Read for What's New (2026 maximum $184,500) and the optional-method conditions. | https://www.irs.gov/pub/irs-pdf/i1040sse.pdf | 2026-11-13 |
| Schedule C (Form 1040) 2026. Read for lines 1 to 32, line 27a (Form 7205) and Part V to line 27b. | https://www.irs.gov/pub/irs-pdf/f1040sc.pdf | 2026-11-13 |
| IRS Pub. 15 (2026). Read for the social security wage base ($184,500) and the 6.2% and 1.45% employee rates. | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-13 |
| 26 U.S.C. 1401 (govinfo). Read for (a) 12.4%, (b)(1) 2.9%, (b)(2) 0.9%, the thresholds and (b)(2)(B) reduction by wages. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1401.htm | 2026-11-13 |
| 26 U.S.C. 1402 (govinfo). Read for (a)(12) deduction in computing net earnings and (b) the $400 floor. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap2-sec1402.htm | 2026-11-13 |
| 26 U.S.C. 164(f) (govinfo). Read for the one-half deduction, excluding the 1401(b)(2) tax. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec164.htm | 2026-11-13 |
| 26 U.S.C. 280A(c)(5) (govinfo). Read for the gross income limit and carryforward. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec280A.htm | 2026-11-13 |
| Rev. Proc. 2013-13. Read for section 4.01: $5 rate, 300 square feet. | https://www.irs.gov/pub/irs-drop/rp-13-13.pdf | 2026-11-13 |
| IRS standard mileage rates page. Read for 2026 business rates: 72.5 cents (1 Jan to 30 Jun, IR-2025-128) and 76 cents (1 Jul to 31 Dec, IR-2026-29). | https://www.irs.gov/tax-professionals/standard-mileage-rates | 2026-11-13 |
| Form 1040-ES (2026). Read for the four 2026 payment due dates. | https://www.irs.gov/pub/irs-pdf/f1040es.pdf | 2026-11-13 |

Not yet confirmed: the 2026 instructions for Form 8829 and Form 8959 were not yet published when read; the Form 8959 method above is taken from 26 U.S.C. 1401(b)(2)(B), and Form 8959 line numbers are not quoted for that reason.
