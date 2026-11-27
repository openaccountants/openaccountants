---
name: us-self-employed-health-insurance
description: Compute the 2026 federal self-employed health insurance deduction for a Schedule C sole proprietor or disregarded single-member LLC. Covers the business earned-income limit, monthly subsidized-employer-plan bar, family coverage, Medicare, qualified long-term care age caps, Form 7206 and Schedule 1. Marketplace credit coordination and specialist cases have explicit holds. Includes historical 2025 examples separately. Load after us-schedule-c-and-se-computation.
version: "1.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US self-employed health insurance deduction, tax year 2026

**Answer first.** Deduct eligible premiums paid for medical insurance established under the business, up to that business's earned-income limit, as an adjustment to income. Test subsidized employer-plan eligibility month by month, even if coverage was declined. Apply the separate long-term care test and age cap. The deduction does not reduce self-employment tax. [26 U.S.C. 162(l)](https://uscode.house.gov/us/usc/t26/s162/).

## Scope and who this is for

One Schedule C sole proprietor or owner of a disregarded single-member LLC, using the regular Schedule SE method. Personal services must be a material income-producing factor under [section 401(c)(2)](https://uscode.house.gov/us/usc/t26/s401/). Federal tax year 2026; the historical cases below remain 2025. Partners, more-than-2% S corporation shareholders, farming, optional SE methods and clergy are outside this computation: Check this point with one of our partner accountants.

Use `us-sole-prop-bookkeeping` for transaction classification, `us-schedule-c-and-se-computation` for profit and the deductible half of SE tax, and `us-self-employed-retirement` for the business retirement deduction. Pass the result to `us-qbi-deduction`, `us-quarterly-estimated-tax` and `us-federal-return-assembly`; `us-ca-return-assembly` receives the federal result only. State mandates and credits remain outside scope.

**Form status.** The [2026 Form 7206](https://www.irs.gov/pub/irs-dft/f7206--dft.pdf) and [2026 Schedule 1](https://www.irs.gov/pub/irs-dft/f1040s1--dft.pdf) read here are drafts, not forms for filing. The line locators below match those drafts and the final 2025 editions. Use the final 2026 forms before filing; no final 2026 box is certified here.

## Ask the client first

Get the monthly premium statements, payment evidence, insured persons and year-end ages; actual employer eligibility dates, including waiting periods, through the taxpayer, spouse, dependants and under-27 children; and whether each employer plan includes long-term care. Obtain the policyholder and business-establishment evidence, all businesses' profits/losses, the actual deductible half of SE tax, the attributable retirement deduction and any Form 2555. For Marketplace coverage obtain Form 1095-A and the credit/reconciliation computation. For Medicare use actual SSA-1099 and insurer statements; for long-term care obtain the insurer's qualification evidence and each insured person's age.

Missing eligibility, premiums, months, policy type, business attribution or credit information means **no usable final deduction until resolved**. Do not assume employer cover exists, select the highest- or lowest-profit business, insert standard Medicare premiums, or default to a deduction without coordinating a possible credit.

## The method, step by step

### Rates, bands and thresholds

| Item and condition | Amount, 2026 | Source |
| --- | --- | --- |
| Eligible paid premiums, before the earned-income cap | 100% | [162(l)(1)–(2)](https://uscode.house.gov/us/usc/t26/s162/) |
| Nondependent child must be below this age at year end | 27 | [162(l)(1)(D)](https://uscode.house.gov/us/usc/t26/s162/) |
| Qualified LTC, attained age 40 or less at year end, per person | USD 500 | [Rev. Proc. 2025-32 §4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Qualified LTC, age 41–50 | USD 930 | [Rev. Proc. 2025-32 §4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Qualified LTC, age 51–60 | USD 1,860 | [Rev. Proc. 2025-32 §4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Qualified LTC, age 61–70 | USD 4,960 | [Rev. Proc. 2025-32 §4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Qualified LTC, age over 70 | USD 6,200 | [Rev. Proc. 2025-32 §4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Schedule A qualifying unreimbursed medical expenses, if itemizing | Only excess over 7.5% of AGI | [213(a)](https://uscode.house.gov/us/usc/t26/s213/) |

1. **Establish the plan.** A Schedule C policy may be in the business's or individual's name. Identify the actual business under which it is established. Use a separate Form 7206 for each business with its own plan; the same person's LTC cap is shared across forms. [Form 7206 instructions](https://www.irs.gov/instructions/i7206).
2. **Remove barred months.** Any eligibility during a month for a subsidized health plan maintained by an employer of the taxpayer, spouse, dependant or under-27 child bars that month's deduction, whether enrolled or not. A waiting period ends when eligibility actually starts. Apply separately to plans including qualified LTC coverage and plans without it; an unsubsidized plan alone does not trigger the statutory bar. [162(l)(2)(B)](https://uscode.house.gov/us/usc/t26/s162/); [instructions, Other coverage](https://www.irs.gov/instructions/i7206).
3. **Eligible premiums (lines 1–3).** Include amounts actually paid for medical, dental and vision cover for self, spouse, dependants and a child under 27 at year end even if not dependent. Add qualified LTC premiums only up to the smaller of actual eligible payments and the per-person age cap. Do not double-count a payment or include excluded retired-public-safety-officer distributions. Medicare premiums voluntarily paid for insurance in the individual's name similar to qualifying private insurance can count; there is nothing to deduct for premium-free coverage. [162(l)(1), (2)(C)](https://uscode.house.gov/us/usc/t26/s162/); [7206 instructions](https://www.irs.gov/instructions/i7206).
4. **Marketplace hold.** Marketplace coverage, APTC, a possible premium tax credit or part-year credit/deduction coordination requires `us-premium-tax-credit-8962`. The deduction and credit affect each other; their combined benefit cannot cover more than the premiums. The 2025 Pub. 974 supplies simplified and iterative methods, not the final 2026 credit rules. Do not use the old deduction-only default, a marginal-rate cutoff or a homemade iteration. Until the 2026 credit position and method are resolved, no usable final deduction for this case: Check this point with one of our partner accountants. [Pub. 974, Self-Employed Health Insurance Deduction and PTC](https://www.irs.gov/pub/irs-pdf/p974.pdf).
5. **Earned-income limit (lines 4–13).** For the ordinary Schedule C case, start with that business's net profit (line 4). Line 5 totals profits of profitable businesses and the specified other allocable earned income, **excluding net losses**. Line 6 is line 4 divided by line 5; line 7 allocates the actual deductible half of SE tax using that proportion. SE tax itself is computed upstream using the applicable profit/loss aggregation; do not ignore a loss in that upstream calculation. Subtract line 7 and the allowable SEP, SIMPLE or qualified-plan deduction attributable to this same business (line 9). Subtract any Form 2555 line 45 amount attributable to the business (line 12). A zero/negative available limit gives no deduction in this ordinary case; optional-method cases are held above. [401(c)(2)](https://uscode.house.gov/us/usc/t26/s401/); [2026 draft Form 7206 lines 4–13](https://www.irs.gov/pub/irs-dft/f7206--dft.pdf).
6. **Deduct the smaller** of eligible premiums (line 3) and the available earned-income limit (line 13); line 14 flows to Schedule 1 line 17. This is the owner's adjustment to income, not a Schedule C expense. It does not reduce Schedule SE earnings. Compute any attributable QBI adjustment in `us-qbi-deduction`, rather than assuming every deduction automatically reduces every business's QBI. [162(l)(2)–(4)](https://uscode.house.gov/us/usc/t26/s162/); [2025 Form 7206](https://www.irs.gov/pub/irs-prior/f7206--2025.pdf).
7. **Unused premiums.** There is no section 162(l) carryforward of premiums disallowed for this year. Otherwise qualifying, uncompensated medical premiums not deducted here may enter Schedule A if itemizing, subject to section 213's own covered-person test and 7.5% AGI floor. The under-27 rule does **not** automatically extend to Schedule A. LTC premiums above the age cap are excluded there too. Never deduct the same premium here and on Schedule A. [162(l)(1)–(3)](https://uscode.house.gov/us/usc/t26/s162/); [213(a), (d)(1), (10)](https://uscode.house.gov/us/usc/t26/s213/); [Pub. 502, Child under age 27](https://www.irs.gov/pub/irs-pdf/p502.pdf).

Generally the Form 1040-instructions worksheet suffices, but Form 7206 is required for more than one source of SE-tax income, Form 2555, or qualified LTC premiums. [Form 7206 instructions, How to figure the deduction](https://www.irs.gov/instructions/i7206).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Spouse's subsidized plan declined, or eligibility begins partway through a month | Entire eligible month barred; waiting months before actual eligibility are not automatically barred |
| Child turns 27 by year end | No under-27 entitlement; dependency must be established separately |
| Child is 26 at year end and files their own return | Under-27 rule still applies, subject to all the other conditions |
| Income-replacement disability or life cover, or guaranteed weekly hospitalization payments | Do not treat these as medical premiums; [Pub. 502, Insurance Premiums You Can't Include](https://www.irs.gov/pub/irs-pdf/p502.pdf) |
| Premiums already paid with excluded employer money or reimbursed tax-free | No second deduction; [Pub. 502, Employer-Sponsored Health Insurance Plan](https://www.irs.gov/pub/irs-pdf/p502.pdf) |
| Spouse-named policy; both spouses self-employed with family coverage | Do not use an automatic equal or cost allocation, or assume business establishment. No usable result for this issue: Check this point with one of our partner accountants. |
| COBRA continuation eligibility/premiums, short-term or mixed medical/indemnity policies | No blanket eligibility conclusion; confirm policy terms and subsidy/business conditions. Check this point with one of our partner accountants. |
| Part-year business, premiums before/after trading, or a partial month | Do not annualize profits or infer qualifying months from a generic rule. No usable case conclusion here: Check this point with one of our partner accountants. |
| Specific Medicare Part A/B/C/D, Medigap, IRMAA or SSA-1099 allocation uncertainty | Use actual statements and the general voluntary-premium rule; no standard amount or automatic surcharge entitlement. Check this point with one of our partner accountants. |
| Employee health insurance or workers' compensation premiums | Separate business-expense issue for `us-sole-prop-bookkeeping`; no owner-premium deduction under this method. Check this point with one of our partner accountants. |

## Worked cases

All amounts are USD. The two current cases assume an established business plan, no Marketplace credit, no Form 2555, no other SE businesses, regular SE computation and no Social Security wages. Retirement amounts are allowable deductions already established upstream. The illustrative half-SE formula is profit × 0.9235 × 0.153 ÷ 2 for these below-wage-base inputs; use the actual Schedule SE result in a return. [Schedule SE](https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf); unchanged computation dependency in `us-schedule-c-and-se-computation`.

**Case 1 (2026).** Single designer, age 55, profit 30,000; no wages/employer plan; medical 9,600, qualified LTC 3,000 and allowable SEP 4,000. Half SE = 2,119.43; premiums = 9,600 + 1,860 = 11,460; limit = 30,000 − 2,119.43 − 4,000 = 23,880.57; deduction = 11,460. Excess LTC 1,140 is not a Schedule A medical premium either.

```oa-check
name: Long-term care cap and earned income limit (2026)
inputs:
  net_profit: 30000
  medical_premiums: 9600
  ltc_paid: 3000
  ltc_limit_age_51_60: 1860
  sep_deduction: 4000
steps:
  - half_se: net_profit * 0.9235 * 0.153 / 2
  - line_3: medical_premiums + min(ltc_paid, ltc_limit_age_51_60)
  - line_13: net_profit - half_se - sep_deduction
  - deduction: min(line_3, line_13)
expected:
  half_se: 2119.43
  line_3: 11460
  line_13: 23880.57
  deduction: 11460
```

**Case 2 (2026).** Married sole proprietor, profit 6,000, no retirement deduction, own policy 800/month all year. Spouse's subsidized coverage becomes available 1 September. Eight eligible months give 6,400; half SE = 423.89, limit and deduction = 5,576.11. Remaining eligible premiums 823.89 plus barred-month premiums 3,200 are only potential Schedule A expenses, subject to that deduction's separate conditions.

```oa-check
name: Month-by-month bar and earned income limit (2026)
inputs:
  net_profit: 6000
  monthly_premium: 800
  eligible_months: 8
steps:
  - line_3: monthly_premium * eligible_months
  - half_se: net_profit * 0.9235 * 0.153 / 2
  - line_13: net_profit - half_se
  - deduction: min(line_3, line_13)
  - cut_by_limit: line_3 - deduction
expected:
  line_3: 6400
  half_se: 423.89
  line_13: 5576.11
  deduction: 5576.11
  cut_by_limit: 823.89
```

### Historical 2025 cases, keep these inputs in 2025

These retain the earlier examples and tests. Except the explicit holds, results assume a qualifying established plan, no employer bar beyond stated months, no PTC/APTC, no Form 2555, no other SE business/wages and no retirement deduction. Missing original eligibility facts must be confirmed before using a result. Stated Medicare premiums are hypothetical actual payments, not a standard rate for 2026. For historical LTC only, [Rev. Proc. 2024-40 §2.28](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf) gives 480 / 900 / 1,800 / 4,810 / 6,020 across the same five age bands.

- **Example 1:** Maria Hernandez, single, 34, freelance UX designer; profit 62,644, off-exchange 700/month = 8,400, no employer plan/PTC. Half SE 4,425.66, limit 58,218.34; deduction 8,400.
- **Example 2:** Alex Rivera, single, 28, freelance graphic designer; profit 12,000, Marketplace 450/month = 5,400, no PTC claimed. Conditional no-credit arithmetic: half SE 847.77, limit 11,152.23, deduction 5,400. Original alternative profit 4,000: half SE 282.59, limit/deduction 3,717.41, unused premiums 1,682.59, not 1,400. These are **non-usable filing conclusions** until credit eligibility/reconciliation is resolved: Check this point with one of our partner accountants.
- **Example 3:** Sarah Kim, MFJ, 45, freelance financial adviser; spouse's job starts 1 July 2025, family coverage effective 1 August; own premium 900/month. January–July = 7 × 900 = 6,300; August–December = 4,500 barred. Profit/retirement facts were not supplied: **6,300 is a premium subtotal, not a proven deduction**. Check this point with one of our partner accountants.
- **Example 4:** Robert Garcia, single, 68, freelance consultant; profit 95,000; Part B 185/month, Medigap Plan F 220/month, Part D 35/month; no employer plan. Conditional qualifying voluntary premiums = 2,220 + 2,640 + 420 = 5,280; half SE 6,711.54, limit 88,288.46; deduction 5,280.
- **Example 5:** Lisa Park, MFJ, 61; profit 180,000; medical 12,000, LTC paid 6,000. Historical eligible LTC 4,810; deduction 16,810, correcting 16,770. Half SE 12,716.60, limit 167,283.41 (unrounded half SE 12,716.595). Excess LTC 1,190 is not deductible on Schedule A either.
- **Test 1:** profit 80,000, 600/month = 7,200, no employer plan/PTC: half SE 5,651.82, limit 74,348.18, deduction 7,200.
- **Test 2:** profit 5,000, 500/month = 6,000, no employer plan: half SE 353.24, limit/deduction 4,646.76, unused premiums 1,353.24, correcting the old 5,000 deduction.
- **Test 3:** profit 60,000, 800/month, spouse's subsidized plan eligible July–December: six months = 4,800; half SE 4,238.87, limit 55,761.14, deduction 4,800 (compute the limit before rounding intermediate cents).
- **Test 4:** profit 50,000; Part B 185/month, Medigap 150/month, Part D 40/month; no employer plan: conditional qualifying voluntary premiums 12 × 375 = 4,500; half SE 3,532.39, limit 46,467.61, deduction 4,500.
- **Test 5:** profit 100,000, medical 10,000, LTC paid 5,000, age 55, no employer plan: eligible LTC 1,800, deduction 11,800, correcting 11,790; half SE 7,064.78, limit 92,935.23. Excess LTC 3,200 is outside Schedule A too.
- **Test 6:** profit zero, 500/month = 6,000: ordinary-method deduction zero; optional-method cases remain referred. Schedule A needs its separate eligibility tests.
- **Test 7:** profit 120,000, family cover self/spouse/25-year-old child, 1,800/month = 21,600, no employer plan: half SE 8,477.73, limit 111,522.27, deduction 21,600.

## When to refuse or refer

These boundaries preserve the original catalogue; each is a non-usable hold for the specialist outcome, not a substitute for the core computation above.

| Code | Boundary and action |
| --- | --- |
| R-SEHI-PTC | Full Form 8962, credit eligibility, repayment, nonconvergence and part-year credits: `us-premium-tax-credit-8962`. Check this point with one of our partner accountants. |
| R-SEHI-HSA | HSA/HDHP qualification, contribution limits and last-month rule; no inherited 2025 amounts may be used for 2026. Check this point with one of our partner accountants. |
| R-SEHI-SCHA (historical R-SEHI-SCHEDULE-A) | Actual Schedule A calculation and covered-person eligibility. Check this point with one of our partner accountants. |
| R-SEHI-COBRA (historical R-SEHI-COBRA-ADMIN) | COBRA elections, qualifying events, administration and policy-specific deduction eligibility. Check this point with one of our partner accountants. |
| R-SEHI-LTCQ (historical R-SEHI-LTC-QUALIFIED) | Whether the actual contract meets section 7702B; an insurer label is not a legal determination. Check this point with one of our partner accountants. |
| R-SEHI-SCORP | Partners, more-than-2% S corporation shareholders and their reporting. Check this point with one of our partner accountants. |

## Filing and payment

For a domestic calendar-year individual without special relief, the 2026 return is ordinarily due 15 April 2027; a properly completed, timely Form 4868 with the required tax estimate gives six additional months to 15 October 2027 for filing, not payment. [6072(a)](https://uscode.house.gov/us/usc/t26/s6072/); [Form 4868 instructions](https://www.irs.gov/pub/irs-pdf/f4868.pdf). Overseas, disaster or other special deadlines are held: Check this point with one of our partner accountants. Keep the monthly eligibility working paper and premium/payment evidence with the return file. Use the final 2026 forms and resolve the Marketplace hold before filing.

## Completion checklist

Confirm actual plan establishment, payments, covered people and employer eligibility for every month; separately test LTC and apply the per-person cap; establish the actual SE-tax and retirement deductions before the earned-income limit; resolve any credit; distinguish unused medical premiums from ineligible LTC excess; pass the allowable adjustment to return assembly and QBI. The historical USD 20,000 attention trigger was an internal review convention, not a statutory threshold; premium evidence is required regardless of size.

**Circular 230 §10.37:** This is computational guidance on the stated facts. Obtain the missing facts and qualified professional review before filing; no conclusion here assumes an audit will not occur.

## Sources

| Source and portion actually read | URL | Read on |
| --- | --- | --- |
| Read for Current 26 U.S.C. 162(l)(1)–(5), covered people, earned income, monthly bar, separate LTC treatment and deduction coordination | https://uscode.house.gov/us/usc/t26/s162/ | 2026-11-27 |
| Read for 401(c)(1)–(2), self-employment and earned-income dependencies | https://uscode.house.gov/us/usc/t26/s401/ | 2026-11-27 |
| Read for 213(a), (d)(1), (6), (10), medical care, own covered-person test, LTC cap and indexing | https://uscode.house.gov/us/usc/t26/s213/ | 2026-11-27 |
| Read for Rev. Proc. 2025-32 §4.27, five 2026 LTC limits | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-27 |
| Read for 2026 draft 7206, cover warning and lines 1–14; provisional locators only | https://www.irs.gov/pub/irs-dft/f7206--dft.pdf | 2026-11-27 |
| Read for 2026 draft Schedule 1, cover warning and adjustments lines 15–17 | https://www.irs.gov/pub/irs-dft/f1040s1--dft.pdf | 2026-11-27 |
| Read for Final 2025 Form 7206, lines 1–14 and footnotes; historical cases | https://www.irs.gov/pub/irs-prior/f7206--2025.pdf | 2026-11-27 |
| Read for Form 7206 instructions (2025), purpose, business establishment, Medicare, required form, multiple plans, other coverage and Schedule A/SE effects | https://www.irs.gov/instructions/i7206 | 2026-11-27 |
| Read for Rev. Proc. 2024-40 §2.28, historical 2025 LTC caps only | https://www.irs.gov/pub/irs-drop/rp-24-40.pdf | 2026-11-27 |
| Read for 2025 Schedule SE, lines 2–13; regular-SE arithmetic for historical examples; unchanged factors reused for current low-profit cases | https://www.irs.gov/pub/irs-prior/f1040sse--2025.pdf | 2026-11-27 |
| Read for Pub. 974 (2025), self-employed deduction/PTC, simplified/iterative methods and part-year examples; no 2026 credit parameters certified | https://www.irs.gov/pub/irs-pdf/p974.pdf | 2026-11-27 |
| Read for Pub. 502 (2025), insurance premiums, employer exclusions, self-employed persons and nondependent-child Schedule A restriction | https://www.irs.gov/pub/irs-pdf/p502.pdf | 2026-11-27 |
| Read for 1402(a), aggregation of business income/loss and regular-SE dependency | https://uscode.house.gov/us/usc/t26/s1402/ | 2026-11-27 |
| Read for 6072(a) calendar-year ordinary return deadline | https://uscode.house.gov/us/usc/t26/s6072/ | 2026-11-27 |
| Read for Form 4868 instructions, six-month extension and payment warning | https://www.irs.gov/pub/irs-pdf/f4868.pdf | 2026-11-27 |

Not yet confirmed: final 2026 Form 7206/Schedule 1 locators, 2026 Marketplace credit parameters and all expressly held specialist outcomes. No usable final result for a held issue: Check this point with one of our partner accountants.
