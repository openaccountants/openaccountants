---
name: us-self-employed-health-insurance
description: "Compute the 2026 US self-employed health insurance deduction under 26 U.S.C. 162(l) for a sole proprietor or single-member LLC owner, on Form 7206 or the Schedule 1 worksheet. Covers medical, dental, vision, Medicare and COBRA premiums, qualified long-term care premiums capped by age ($500, $930, $1,860, $4,960, $6,200 for 2026 under Rev. Proc. 2025-32), the earned income limit (net profit less the deductible half of self-employment tax and the retirement plan deduction), the month-by-month bar for any month the person could join a subsidized employer plan, children under 27, and the interaction with the premium tax credit. Trigger on \"self-employed health insurance\", \"Form 7206\", \"Schedule 1 line 17\", \"deduct my health premiums\", \"Medicare premiums self-employed\", \"long-term care premium limit\". Load after us-schedule-c-and-se-computation. Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-self-employed-health-insurance"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US self-employed health insurance deduction, tax year 2026

> **Source-cited draft.** Built from 26 U.S.C. 162(l), 213 and 36B, Rev. Proc. 2025-32, Form 7206 and Schedule 1 (Form 1040) as printed for 2025, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A self-employed person deducts health insurance premiums for themselves, their spouse, their dependants and any child under 27 at the end of 2026, as an adjustment to income (Schedule 1, line 17 on the 2025 form), not on Schedule C. The deduction cannot exceed the earned income from the business under which the plan is established: net profit, less the deductible half of self-employment tax, less the SEP, SIMPLE or qualified plan deduction for that business. No deduction is allowed for any month the person was **eligible** for a subsidized employer plan (their own, their spouse's, or a dependant's or under-27 child's employer), whether or not they enrolled. Long-term care premiums count only up to the 2026 age limit. The deduction does not reduce self-employment tax.

## Scope and who this is for

In scope: the 162(l) deduction of one individual for tax year 2026 who has net profit from a Schedule C business (sole proprietor or single-member LLC disregarded for federal tax). The result goes to Schedule 1 and reduces adjusted gross income.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Classifying the bank and card transactions | `us-sole-prop-bookkeeping` |
| Schedule C net profit and Schedule SE (the deductible half) | `us-schedule-c-and-se-computation` |
| The SEP, SIMPLE or solo 401(k) deduction that reduces the limit | `us-self-employed-retirement` |
| Form 8962, the premium tax credit and its repayment | `us-premium-tax-credit-8962` |
| QBI, which this deduction reduces | `us-qbi-deduction` |
| Putting the return together in the right order | `us-federal-return-assembly` |
| Partners and S corporation shareholders who own more than 2% | refer (see the refusal table) |

## Ask the client first

1. **Coverage by month for 2026:** who was covered (self, spouse, dependants, children under 27 at 31 December 2026), the premium paid for each month, and the insurer statements or Form 1095-A, 1095-B or 1095-C.
2. **Employer plan eligibility by month:** for each month, could the person join a subsidized health plan through their own job, their spouse's job, or the job of a dependant or under-27 child? Eligible counts even if declined. Ask separately about plans that include long-term care cover.
3. **Marketplace coverage:** was the plan bought on HealthCare.gov or a state exchange, and was advance premium tax credit paid?
4. **Long-term care:** is the policy a qualified long-term care insurance contract, what was paid, and the age of each insured person at 31 December 2026.
5. **Medicare:** Part B, Part D, Medigap and Medicare Advantage premiums, and any voluntary Part A premium. The Social Security benefit statement (SSA-1099) shows Part B and Part D amounts withheld.
6. **The business:** which business the plan is established under (if more than one Schedule C), and the SEP, SIMPLE or solo 401(k) deduction for that business.
7. **Other filings:** any Form 2555 (foreign earned income), and whether the spouse is also self-employed.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Share of eligible premiums deductible | 100%, up to the earned income limit | [26 U.S.C. 162(l)(1) and (2)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm) |
| Child covered whatever their dependency status, if not yet this age at year end | 27 | [26 U.S.C. 162(l)(1)(D)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm) |
| Eligible long-term care premium, age 40 or less at year end | USD 500 | [Rev. Proc. 2025-32, section 4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Eligible long-term care premium, age 41 to 50 | USD 930 | [Rev. Proc. 2025-32, section 4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Eligible long-term care premium, age 51 to 60 | USD 1,860 | [Rev. Proc. 2025-32, section 4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Eligible long-term care premium, age 61 to 70 | USD 4,960 | [Rev. Proc. 2025-32, section 4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Eligible long-term care premium, over 70 | USD 6,200 | [Rev. Proc. 2025-32, section 4.27](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Medical expense floor on Schedule A, for premiums the limit cuts off | 7.5% of adjusted gross income | [26 U.S.C. 213(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec213.htm) |

The long-term care limits are per insured person, by that person's age at the end of 2026. The 2026 Medicare premium amounts are not restated here: use the amounts on the person's own statements.

### Step 1: list the eligible premiums by month (Form 7206 lines 1 to 3)

1. Take each month of 2026. Drop any month in which the person was eligible to participate in a subsidized plan of any employer of the person, their spouse, a dependant or an under-27 child. The test is eligibility, not enrolment. It is run separately for plans with long-term care cover and plans without it, so eligibility for an employer medical plan does not bar long-term care premiums, and the reverse. Source: [26 U.S.C. 162(l)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm).
2. For the remaining months, add the premiums for medical, dental and vision cover for the person, spouse, dependants and under-27 children (line 1). Marketplace and off-exchange policies, short-term health policies, Medicare Part B, Part D (including any income-related surcharge), Medigap, Medicare Advantage and voluntary Part A premiums count. COBRA premiums the person pays count.
3. For a qualified long-term care contract, add the smaller of the premium paid and the 2026 age limit, per insured person (line 2). Source: [26 U.S.C. 162(l)(2)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm) and [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf).
4. With Marketplace cover and the premium tax credit, only the premium the person bears counts, and the credit and this deduction depend on each other (a lower AGI raises the credit, which lowers the premium borne). Resolve them together by the Pub. 974 simplified or iterative method in `us-premium-tax-credit-8962`. A dollar of premium is never both deducted and credited.
5. Line 3 = line 1 + line 2.

### Step 2: the earned income limit (Form 7206 lines 4 to 13)

6. Line 4: net profit (Schedule C line 31) from the business under which the plan is established.
7. Lines 5 to 7: with more than one business, the deductible half of self-employment tax (Schedule 1, line 15) is shared in proportion to net profits; with one business, line 7 is the whole deductible half.
8. Line 9: the SEP, SIMPLE or qualified plan deduction (Schedule 1, line 16) for that business. Compute it first in `us-self-employed-retirement`. The health insurance deduction is not subtracted in that computation, so there is no loop.
9. Line 10 = line 4 − line 7 − line 9. Line 12 takes out any Form 2555 exclusion attributable to that income. Line 13 is the limit. Source: [Form 7206](https://www.irs.gov/pub/irs-pdf/f7206.pdf).

### Step 3: the deduction

10. Line 14 = the smaller of line 3 and line 13. Enter it on Schedule 1 (line 17 on the 2025 form). Source: [Schedule 1 (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf).
11. Premiums over the limit are not carried forward. They can be medical expenses on Schedule A if the person itemizes, subject to the 7.5% floor. Premiums allowed under 162(l) are not counted again on Schedule A. Source: [26 U.S.C. 162(l)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm).
12. The deduction does not reduce net earnings from self-employment: Schedule SE still starts from full net profit. Source: [26 U.S.C. 162(l)(4)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm).
13. Pass the deduction to `us-qbi-deduction`: it is attributable to the business and reduces qualified business income. It also lowers the income used for the estimated tax in `us-quarterly-estimated-tax`.

### Form 7206 or the worksheet

The Schedule 1 worksheet in the Form 1040 instructions can be used for a simple case. Form 7206 is required if the person had more than one source of income subject to self-employment tax, files Form 2555, or uses amounts paid for qualified long-term care insurance. Source: [Form 7206](https://www.irs.gov/pub/irs-pdf/f7206.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Eligible for spouse's subsidized employer plan, declined it | No deduction for those months |
| Employer plan where the employer pays nothing (unsubsidized) | Does not bar the deduction |
| Employer medical plan available, long-term care bought privately | The bar is applied separately: the long-term care premium can still count |
| Spouse's new job, coverage available after a waiting period | The bar starts with the first month coverage is available, not the hire date |
| Child turns 27 on or before 31 December 2026 | Not covered by the under-27 rule for 2026; counts only if a dependant |
| Child is 26 at 31 December 2026 and files their own return | Covered for all of 2026 |
| Net profit is zero or a loss | No deduction; premiums may go to Schedule A |
| Premiums paid from the business bank account | Still Schedule 1, never Schedule C |
| Premiums for employees (not the owner) | Schedule C line 14, a different deduction |
| Policy in the spouse's name | Can count if it covers the self-employed person and the plan is established under the business |
| Both spouses self-employed, one family policy | Each deducts against their own business; split the premium by the cost of each spouse's cover, or equally if it cannot be separated |
| Part-year self-employment | Only months of self-employment with cover; the limit uses actual earned income, not annualized |
| Premium tax credit for some months, deduction for others | Pub. 974 method for the credit months; flag for review |
| Disability, life, or fixed-amount hospital indemnity policies | Not medical insurance: no deduction |
| Workers' compensation cover | A Schedule C line 15 business expense, not this deduction |
| Premiums already paid with pre-tax employer money | Already excluded from income: no deduction |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether any employer plan was available that month | Treat the month as barred; ask |
| Whether the spouse's employer offers cover | Treat as offered; ask |
| Premium amounts | Zero until a statement or Form 1095 is seen |
| Whether a policy is medical or another type | Not medical until the statement shows it |
| Long-term care premium above the age limit | Cap at the limit |
| Premium tax credit position unclear | Deduction only; flag the Form 8962 interaction |
| Advance premium tax credit received, amount unknown | Stop until Form 1095-A is seen |
| Months of cover unclear | Count only documented months |
| More than one Schedule C, plan not clearly under one | Use the business under which the policy was set up; if none is shown, the lower-profit business (smaller limit), and flag it |
| Medicare premium amounts | Take them from the SSA-1099 or plan statements; do not assume a standard amount |

### Red flags for the reviewer

| Flag | Why it matters |
| --- | --- |
| Deduction above USD 20,000 | Check every premium statement |
| Deduction cut by the earned income limit | Schedule A may help; record the cut |
| Marketplace cover with advance credit | Form 8962 reconciliation; the two amounts depend on each other |
| Employer plan available for some months | Month-by-month working paper needed |
| Long-term care premiums claimed | Age limit applied, and the policy is a qualified contract |
| Medicare premiums claimed | Amounts match SSA-1099 and plan statements, including any surcharge |
| A covered child aged 26 or 27 | Age at 31 December 2026 checked |

## Worked cases

**Case 1: long-term care cap and the earned income limit.** A single designer aged 55 has 2026 Schedule C net profit of USD 30,000, no wages and no employer plan in any month. She pays USD 9,600 of medical premiums and USD 3,000 for a qualified long-term care policy, and makes a USD 4,000 SEP contribution.

The deductible half of self-employment tax is USD 30,000 x 92.35% x 15.3% / 2 = USD 2,119.43. Line 3: USD 9,600 + the smaller of USD 3,000 and the age 51 to 60 limit of USD 1,860 = USD 11,460. Line 13: USD 30,000 − USD 2,119.43 − USD 4,000 = USD 23,880.57. The deduction is USD 11,460. The other USD 1,140 of long-term care premium is not deductible here; it may be a Schedule A medical expense.

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

**Case 2: employer plan from September, and the limit bites.** A married sole proprietor has 2026 net profit of USD 6,000 and no retirement plan. His individual policy costs USD 800 a month all year. His spouse's subsidized employer plan became available to him on 1 September 2026, and he kept his own policy.

January to August are eligible months: 8 x USD 800 = USD 6,400. September to December are barred. The deductible half of self-employment tax is USD 6,000 x 92.35% x 15.3% / 2 = USD 423.89, so the limit is USD 5,576.11. The deduction is USD 5,576.11. USD 823.89 of the eligible premiums, and all USD 3,200 for the barred months, may be Schedule A medical expenses if the couple itemizes.

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

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-SEHI-PTC | The client wants Form 8962 computed, or the credit and the deduction do not converge | Use `us-premium-tax-credit-8962`; refer if it does not settle |
| R-SEHI-HSA | Health savings account contributions | A separate deduction (Form 8889, Schedule 1 line 13 on the 2025 form), outside this skill |
| R-SEHI-SCHA | Premiums cut off by the limit, client itemizes | Schedule A medical expenses are outside this skill |
| R-SEHI-COBRA | COBRA election periods and qualifying events | Employment law, not tax: refer to the plan administrator |
| R-SEHI-LTCQ | Whether a long-term care policy is a qualified contract under section 7702B | Rely on the insurer's statement; refer a doubtful policy |
| R-SEHI-SCORP | S corporation shareholder owning more than 2%, or a partner | Different reporting (wages or guaranteed payments): refer |

Never put the owner's premiums on Schedule C. Never allow a month in which the person was eligible for a subsidized employer plan. Never let the premium tax credit and the deduction cover the same dollar of premium. Never carry an excess forward. Never skip Form 7206 when it is required.

## Filing and payment

The deduction is claimed on the 2026 Form 1040, Schedule 1, with Form 7206 attached when it is required. The return is due **15 April 2027**; Form 4868 extends filing to 15 October 2027, not payment. Form 8962 goes with the return whenever advance premium tax credit was paid. Keep the monthly working paper, insurer statements and Forms 1095 with the file.

## Completion checklist

- Every month of 2026 tested for employer plan eligibility, separately for long-term care cover.
- Children's ages at 31 December 2026 checked against 27.
- Long-term care premiums capped per person at the 2026 age limit.
- Retirement deduction computed first and entered on Form 7206 line 9.
- Deduction is the smaller of line 3 and line 13; any excess noted for Schedule A.
- Nothing for the owner's premiums on Schedule C, and Schedule SE uses full net profit.
- Marketplace cover passed to the Form 8962 skill.
- Amount passed to the QBI and estimated tax computations.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 26 U.S.C. 162 (govinfo). Read for subsection (l): (1) who is covered and the under-27 child, (2)(A) earned income limit, (2)(B) the monthly bar applied separately to long-term care plans, (2)(C) long-term care premiums, (3) no double count on Schedule A, (4) no effect on self-employment tax. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVI-sec162.htm | 2026-11-13 |
| 26 U.S.C. 213 (govinfo). Read for (a) the 7.5% floor and (d)(10) eligible long-term care premiums. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec213.htm | 2026-11-13 |
| Rev. Proc. 2025-32. Read for section 4.27, the 2026 eligible long-term care premium limits ($500, $930, $1,860, $4,960, $6,200). | https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | 2026-11-13 |
| Form 7206 (2025). Read for lines 1 to 14 and when the form is required. | https://www.irs.gov/pub/irs-pdf/f7206.pdf | 2026-11-13 |
| Schedule 1 (Form 1040) 2025. Read for lines 13, 15, 16 and 17. | https://www.irs.gov/pub/irs-pdf/f1040s1.pdf | 2026-11-13 |
| 26 U.S.C. 36B (govinfo). Read for the premium tax credit that interacts with this deduction. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapA-partIV-subpartC-sec36B.htm | 2026-11-13 |

Not yet confirmed: the 2026 Form 7206 and 2026 Schedule 1 were not published when read, so line numbers are from the 2025 editions; the 2026 Medicare Part B standard premium was not read, so no amount is stated; the premium tax credit rules for 2026 are left to `us-premium-tax-credit-8962`.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-self-employed-health-insurance` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-self-employed-health-insurance. If neither is available, confirm every figure against the official source pages cited above before relying on it.
