---
name: us-quarterly-estimated-tax
description: Work out whether a US individual must pay 2026 federal estimated tax on Form 1040-ES, how much is required each quarter, and what the Form 2210 underpayment penalty costs. Covers the USD 1,000 test, the safe harbours in 26 U.S.C. 6654(d) (90% of 2026 tax, or 100% of 2025 tax, 110% where 2025 AGI was over USD 150,000 or USD 75,000 married filing separately), the four 2026 due dates (15 April, 15 June, 15 September 2026, 15 January 2027), the annualized income installment method (Form 2210 Schedule AI, Pub. 505 Worksheet 2-9), withholding treated as paid evenly, the farmer and fisherman rule, waivers and the 2026 underpayment rates. Trigger on "1040-ES", "estimated tax", "quarterly tax", "safe harbor", "underpayment penalty", "Form 2210", "annualized income", "how much should I pay each quarter". Federal only.
version: "3.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US federal estimated tax for individuals (Form 1040-ES), tax year 2026

> **Source-cited draft.** Built from the 2026 Form 1040-ES, IRS Pub. 505 (2026), the 2025 Form 2210 and its instructions, the IRS quarterly interest rates page and 26 U.S.C. 275, 6621, 6622 and 6654, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** An individual must pay 2026 estimated tax if they expect to owe at least **USD 1,000** after withholding and refundable credits, and their withholding and refundable credits will be less than the smaller of **90%** of the 2026 tax or **100%** of the 2025 tax (**110%** if 2025 AGI was more than **USD 150,000**, or USD 75,000 if married filing separately for 2026). The required annual payment is paid in four equal parts on **15 April 2026, 15 June 2026, 15 September 2026 and 15 January 2027**. The fourth payment is not needed if the 2026 return is filed and paid in full by **1 February 2027**. The penalty is simple interest at the underpayment rate (7%, 6%, 7%, 7% for the four quarters of 2026) on each late or short installment.

## Scope and who this is for

In scope: one US citizen or resident alien (or a married couple paying jointly) working out 2026 federal estimated income tax on Form 1040-ES: whether payments are required, the required annual payment, the four installments, the annualized income installment method, how withholding counts, and the Form 2210 underpayment penalty for 2026. The tax that estimated payments cover is income tax, self-employment tax, Additional Medicare Tax, net investment income tax and the other Schedule 2 taxes, less nonrefundable and refundable credits ([26 U.S.C. 6654(f)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm)).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Self-employment tax figures and Schedule SE | `us-schedule-c-and-se-computation` |
| The 2026 income tax brackets, standard deduction, Additional Medicare Tax and net investment income tax on the return | `us-federal-income-tax-return-1040` |
| The qualified business income deduction | `us-qbi-deduction` |
| State estimated tax | `us-state-estimated-tax-safe-harbors-matrix` and the state's income tax skill |
| Corporate estimated tax (Form 1120-W, section 6655) | `us-form-1120-c-corp` |
| Penalty abatement requests, notices and collection | `us-irs-collections-and-controversy` |
| Classifying bank and card transactions | `us-sole-prop-bookkeeping` |

## Ask the client first

1. **The 2025 return:** total tax as figured for line 12b of the 2026 Estimated Tax Worksheet, the AGI on it, whether it covered 12 months, and whether it was a joint return. With no 2025 return or a short 2025 year, only the 90% current-year test is available.
2. **Filing status for 2026**, and whether the spouses will pay jointly. A change between joint and separate from 2025 to 2026 changes how the 2025 tax is split.
3. **Expected 2026 income by period:** 1 January to 31 March, to 31 May, to 31 August and to 31 December. Uneven income (a seasonal business, a large gain late in the year) points to the annualized method.
4. **Withholding for 2026** from every source (W-2 wages, pensions, IRA distributions, backup withholding), and whether it can still be increased with a new Form W-4 or W-4P.
5. **Payments already made for 2026**, with dates, and any 2025 overpayment applied to 2026.
6. **Special facts:** at least two-thirds of gross income from farming or fishing in 2025 or 2026; retirement after age 62 or disability in 2025 or 2026; a casualty or disaster; a qualified farmland sale with a section 1062 election.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| No penalty if 2026 tax minus withholding is less than | USD 1,000 | [26 U.S.C. 6654(e)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Current-year safe harbour: share of the 2026 tax | 90% | [26 U.S.C. 6654(d)(1)(B)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Prior-year safe harbour: share of the 2025 tax | 100% | [26 U.S.C. 6654(d)(1)(B)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Prior-year safe harbour where 2025 AGI exceeds the limit below | 110% | [26 U.S.C. 6654(d)(1)(C)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| 2025 AGI limit for 100% (110% above it) | USD 150,000 | [26 U.S.C. 6654(d)(1)(C)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| 2025 AGI limit, married filing separately for 2026 | USD 75,000 | [26 U.S.C. 6654(d)(1)(C)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Each regular installment | 25% of the required annual payment | [26 U.S.C. 6654(d)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| 1st installment due | 15 April 2026 | [Form 1040-ES (2026), Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| 2nd installment due | 15 June 2026 | [Form 1040-ES (2026), Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| 3rd installment due | 15 September 2026 | [Form 1040-ES (2026), Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| 4th installment due | 15 January 2027 | [Form 1040-ES (2026), Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| 4th installment not needed if the 2026 return is filed and paid in full by | 1 February 2027 | [Form 1040-ES (2026), Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| Annualized method, applicable percentages for installments 1 to 4 | 22.5%, 45%, 67.5%, 90% | [26 U.S.C. 6654(d)(2)(C)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Annualized method, periods and annualization amounts | 1 Jan to 31 Mar 2026: 4; to 31 May: 2.4; to 31 Aug: 1.5; to 31 Dec: 1 | [Pub. 505 (2026), Worksheet 2-9](https://www.irs.gov/pub/irs-pdf/p505.pdf) |
| Annualized method, prorated Social Security limit for the four periods | USD 46,125; 76,875; 123,000; 184,500 | [Pub. 505 (2026), Worksheet 2-9, line 34](https://www.irs.gov/pub/irs-pdf/p505.pdf) |
| Farmer or fisherman: share of gross income from farming or fishing (2025 or 2026) | at least two-thirds | [26 U.S.C. 6654(i)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Farmer or fisherman: current-year percentage (no 110% rule) | 66 2/3% | [26 U.S.C. 6654(i)(1)(C)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Farmer or fisherman: single installment due, or file and pay in full by | 15 January 2027, or 1 March 2027 | [Form 1040-ES (2026), Farming and fishing](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| Underpayment rate, 1 January to 31 March 2026 | 7% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Underpayment rate, 1 April to 30 June 2026 | 6% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Underpayment rate, 1 July to 30 September 2026 | 7% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Underpayment rate, 1 October to 31 December 2026 | 7% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Underpayment rate formula | federal short-term rate plus 3 percentage points | [26 U.S.C. 6621(a)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap67-subchapC-sec6621.htm) |

None of the percentages, the USD 1,000 test or the USD 150,000 and USD 75,000 AGI limits is indexed for inflation; the One Big Beautiful Bill Act (Public Law 119-21) did not amend sections 6621, 6622 or 6654. The underpayment rate is reset each quarter. A due date that falls on a Saturday, Sunday or legal holiday moves to the next business day; none of the four 2026 dates does.

### Step 1: is anything required?

1. **Estimate the 2026 total tax** on the 2026 Estimated Tax Worksheet in [Form 1040-ES (2026)](https://www.irs.gov/pub/irs-pdf/f1040es.pdf): expected AGI (line 1, after the deductible half of self-employment tax), less deductions (line 2d), tax from the 2026 Tax Rate Schedules (line 4), alternative minimum tax (line 5), less credits (line 7), plus self-employment tax (line 9) and other taxes such as Additional Medicare Tax and net investment income tax (line 10), less refundable credits (line 11b). Line 11c is the total 2026 estimated tax. The brackets, deductions and other-tax figures come from `us-federal-income-tax-return-1040`; self-employment tax from `us-schedule-c-and-se-computation`.
2. **The USD 1,000 test** (line 14b): line 11c minus expected withholding (line 13). Under USD 1,000: no estimated payments are required.
3. **The zero-tax exception:** no payments are required if the person was a US citizen or resident alien for all of 2025, the 2025 tax year was 12 months, and they had no tax liability for 2025 (total tax was zero, or no return was required). Source: [26 U.S.C. 6654(e)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm).

### Step 2: the required annual payment

4. **Current-year amount** (line 12a): 90% of line 11c (66 2/3% for a farmer or fisherman).
5. **Prior-year amount** (line 12b): 100% of the 2025 tax, or 110% if 2025 AGI was more than USD 150,000 (USD 75,000 if married filing separately for 2026). The 2025 tax is Form 1040 line 24, reduced by the items listed in the 1040-ES line 12b instructions (unreported Social Security and Medicare tax, tax on excess contributions to tax-favoured accounts, the taxes in Exception 2, and refundable credits). If the 2025 year was less than 12 months or no 2025 return was filed, there is no prior-year amount: use line 12a.
6. **Joint and separate years.** 2025 separate returns and a 2026 joint return: add both spouses' 2025 tax. A 2025 joint return and 2026 separate returns: each spouse's share is the joint tax times (their 2025 tax figured separately over the total of both spouses' separate taxes). Source: [Pub. 505 (2026), chapter 2](https://www.irs.gov/pub/irs-pdf/p505.pdf).
7. **Required annual payment** (line 12c) = the smaller of line 12a and line 12b. Paying it through withholding and estimated payments on time avoids the penalty even if more tax is due with the return.

### Step 3: the installments

8. **Regular method:** each installment is 25% of line 12c, minus the share of withholding treated as paid by that date (step 10). Line 15 of the worksheet is one-quarter of line 14a (line 12c minus withholding), less any 2025 overpayment applied.
9. **Annualized income installment method** (for uneven income): for each period, annualize the income to date (times 4, 2.4, 1.5, 1), figure the tax on it, take the applicable percentage (22.5%, 45%, 67.5%, 90%), and subtract the installments already required. The installment is the smaller of that annualized amount and the regular installment plus any saving carried from an earlier installment; a saving taken early is recaptured by raising the next regular installment ([26 U.S.C. 6654(d)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm)). During 2026 use Pub. 505 Worksheet 2-9; at filing, Form 2210 Schedule AI, which must then be used for all four due dates and filed with the return even if no penalty is owed.
10. **Withholding counts as paid evenly**: one-quarter of the year's withholding is treated as paid on each due date, whatever the actual dates, unless the taxpayer elects actual dates (Form 2210 box D). Wage withholding and other withholding can be treated separately. Source: [26 U.S.C. 6654(g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm). So a W-4 increase late in the year cures earlier shortfalls; a late estimated payment does not.
11. **Changing the estimate mid-year:** refigure line 12c, subtract what has been paid, and spread the rest over the remaining due dates (Pub. 505 chapter 2, Amended estimated tax). An earlier installment below one-quarter of the amended amount may still carry a penalty.

### Step 4: the underpayment penalty (Form 2210)

12. **Underpayment per installment** = required installment minus the amount paid by its due date. Payments are credited to unpaid installments in due-date order, so a late payment first cures the oldest shortfall. Source: [26 U.S.C. 6654(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm).
13. **Period:** from the due date to the date paid, or 15 April 2027 if earlier.
14. **Penalty** = underpayment times the underpayment rate times days unpaid over 365, for each rate period. It is simple interest: daily compounding does not apply to the section 6654 addition ([26 U.S.C. 6622(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap67-subchapC-sec6622.htm)). The 1 January to 31 March 2027 rate also applies from 1 to 15 April 2027 ([26 U.S.C. 6621(b)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap67-subchapC-sec6621.htm)).
15. **Who files Form 2210:** if none of boxes A to E applies, the IRS figures the penalty and bills it; box C (annualized method) and box D (actual withholding dates) require the full form; box A or B requests a waiver. The penalty is reported on the "Estimated tax penalty" line of Form 1040. The 2025 form is the current edition; the 2026 form is expected to follow the same structure ([Form 2210 (2025)](https://www.irs.gov/pub/irs-pdf/f2210.pdf)).
16. **Waivers:** the IRS may waive the penalty for a casualty, disaster or other unusual circumstance where it would be inequitable, or where the taxpayer retired after age 62 or became disabled in 2025 or 2026 and the underpayment was due to reasonable cause and not wilful neglect ([26 U.S.C. 6654(e)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm)). The IRS also waives the part of the penalty attributable to a qualified farmland sale with a section 1062 election (Notice 2026-3, per Form 1040-ES (2026)).

### Recognising estimated payments in bank data

| Bank line | Treatment |
| --- | --- |
| IRS, IRS DIRECT PAY, EFTPS, US TREASURY, 1040-ES, EST TAX, dated 10 to 20 April, June, September or January | Federal estimated tax payment for the installment of that month |
| State tax payees (CA FTB, NYS, state DOR) | Not federal: state estimated tax |
| IRS PENALTY, IRS INTEREST | Not an estimated payment |
| IRS refund, 1040 balance due | Flag for the reviewer: a refund or a prior-year balance, not a 2026 installment |

Federal income tax payments, estimated or not, are not deductible on Schedule C or anywhere else ([26 U.S.C. 275(a)(1)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec275.htm)). W-2 withholding appears on pay stubs, not as separate bank debits.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| 2025 AGI exactly USD 150,000 | 100%: the 110% rule applies only where AGI exceeds USD 150,000 |
| Married filing separately for 2026, 2025 AGI over USD 75,000 | 110% of the 2025 tax |
| 2025 return not filed, or 2025 a short year | Prior-year safe harbour not available: only 90% of 2026 tax |
| No tax liability for a full 12-month 2025, citizen or resident all year | No penalty for 2026, whatever the 2026 tax |
| 2026 tax minus withholding under USD 1,000 | No penalty |
| Prior-year AGI not known | Use 110% until the 2025 return is in hand |
| Withholding alone at or above the required annual payment | No estimated payments needed |
| W-2 job plus self-employment | Increase withholding with Form W-4 (Step 4(c)) to cover both; withholding counts as paid evenly, so a late-year increase still cures early quarters |
| No income subject to estimated tax until after 31 March 2026 | Use the annualized method; file Form 2210 with Schedule AI with the 2026 return |
| Income heavily in the last months (seasonal business, December capital gain) | Annualized method lowers the early installments; the shortfall shows as a large fourth installment |
| Farmer or fisherman (two-thirds of gross income, 2025 or 2026) | One installment of 66 2/3% of 2026 tax or 100% of 2025 tax (no 110%) by 15 January 2027, or file and pay in full by 1 March 2027 |
| Overpayment on the 2025 return applied to 2026 | Treated as paid on 15 April 2026 (Form 2210 instructions, Table 1) |
| Payment made after a due date | Credited to the earliest unpaid installment first; it stops that shortfall accruing from the payment date |
| Spouses who are legally separated, have different tax years, or where one is a nonresident alien (no election) | Cannot pay jointly; each pays on their own estimated income |
| Registered domestic partners or civil union partners | Cannot pay jointly; each takes credit only for their own payments |
| Federally declared disaster with postponed deadlines | Use the postponed date the IRS announces for that area |
| Fiscal-year individual | Installments due the 15th day of the 4th, 6th and 9th months of the fiscal year and the 1st month of the next |

## Worked cases

**Case 1, a decision: pay by the prior-year safe harbour or by the current-year estimate?** A single freelancer had 2025 AGI of USD 180,000 and 2025 tax (as figured for line 12b) of USD 40,000. Business is growing and the 2026 tax is estimated at USD 60,000. There is no withholding.

Prior-year: 2025 AGI is over USD 150,000, so 110% x USD 40,000 = USD 44,000, or USD 11,000 a quarter. Current-year: 90% x USD 60,000 = USD 54,000, or USD 13,500 a quarter. The required annual payment is the smaller, USD 44,000. Paying USD 11,000 on each of the four dates avoids any penalty however high 2026 income turns out, keeps USD 10,000 in the business until April 2027, and leaves USD 16,000 to pay with the return by 15 April 2027 (set that aside). The current-year route is the cheaper one only if the 2026 tax is below USD 48,888.89 (90% of which is USD 44,000), and it carries risk: if the real 2026 tax is higher than estimated, 90% of the real figure is what counts. Recommend the prior-year route when income is rising. When income is falling sharply (for example a 2026 tax of USD 30,000, giving a 90% figure of USD 27,000), the current-year route is cheaper, but recheck the estimate before each due date.

```oa-check
name: Prior-year against current-year safe harbour, single, 2026
inputs:
  prior_year_tax: 40000
  prior_year_agi: 180000
  expected_2026_tax: 60000
  withholding: 0
steps:
  - prior_year_amount: prior_year_tax * 1.10
  - current_year_amount: expected_2026_tax * 0.90
  - required_annual_payment: min(prior_year_amount, current_year_amount)
  - quarterly_installment: (required_annual_payment - withholding) / 4
  - cash_kept_until_filing: current_year_amount - required_annual_payment
  - balance_due_with_return: expected_2026_tax - required_annual_payment
  - break_even_2026_tax: prior_year_amount / 0.90
expected:
  prior_year_amount: 44000.00
  current_year_amount: 54000.00
  required_annual_payment: 44000.00
  quarterly_installment: 11000.00
  cash_kept_until_filing: 10000.00
  balance_due_with_return: 16000.00
  break_even_2026_tax: 48888.89
```

**Case 2, the penalty on late installments, with the crediting order.** The required annual payment is USD 20,000, so each installment is USD 5,000. There is no withholding. Nothing is paid on 15 April 2026; USD 5,000 is paid on 15 June, USD 5,000 on 15 September and USD 10,000 on 31 December 2026.

The June payment goes to the April installment, which was USD 5,000 short for 61 days, all at 6%: USD 50.14. The June installment is then unpaid until the September payment: 15 days to 30 June at 6% (USD 12.33) and 77 days to 15 September at 7% (USD 73.84). The September installment is unpaid until 31 December: 107 days at 7% (USD 102.60). The December payment covers the September installment and the January 2027 installment early. Total penalty USD 238.91, figured as simple interest. The fourth installment has no shortfall, so no 2027 rate is needed.

```oa-check
name: Penalty on late 2026 installments, crediting order
inputs:
  installment: 5000
  rate_q2_2026: 0.06
  rate_q3_2026: 0.07
  rate_q4_2026: 0.07
  days_apr15_to_jun15: 61
  days_jun15_to_jun30: 15
  days_jun30_to_sep15: 77
  days_sep15_to_dec31: 107
steps:
  - penalty_first: round(installment * rate_q2_2026 * days_apr15_to_jun15 / 365, 2)
  - penalty_second_q2: round(installment * rate_q2_2026 * days_jun15_to_jun30 / 365, 2)
  - penalty_second_q3: round(installment * rate_q3_2026 * days_jun30_to_sep15 / 365, 2)
  - penalty_third: round(installment * rate_q3_2026 * 15 / 365 + installment * rate_q4_2026 * (days_sep15_to_dec31 - 15) / 365, 2)
  - total_penalty: penalty_first + penalty_second_q2 + penalty_second_q3 + penalty_third
expected:
  penalty_first: 50.14
  penalty_second_q2: 12.33
  penalty_second_q3: 73.84
  penalty_third: 102.60
  total_penalty: 238.91
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-US-ET-1 | Corporation (Form 1120-W, section 6655) | Refer: `us-form-1120-c-corp` |
| R-US-ET-2 | Trust or estate (Form 1041-ES) | Refuse: different rules on AGI and installments |
| R-US-ET-3 | State estimated tax | Refer: `us-state-estimated-tax-safe-harbors-matrix` and the state skill |
| R-US-ET-4 | Nonresident alien (Form 1040-ES (NR), three installments under section 6654(j)) | Refuse: outside this skill |
| R-US-ET-5 | Penalty waiver request | Compute only; a reviewer decides whether to request it (Form 2210 box A or B) |
| R-US-ET-6 | Section 965 net tax liability, section 1062 farmland installment election, or subpart F income in the annualized method | Refer: special rules in the Form 2210 instructions and Notice 2026-3 |
| R-US-ET-7 | The taxpayer died during 2026 | Refer: which installments remain due after death is a reviewer point |

Never make or schedule payments for the client, never recommend deliberate underpayment, never promise that a mid-year plan removes every penalty, and label all amounts as estimates until a reviewer confirms them.

## Filing and payment

Pay through IRS Online Account, IRS Direct Pay (free, from a bank account), EFTPS (enrolment needed), electronic funds withdrawal when e-filing, or debit or credit card or digital wallet (provider fee). By mail, use the 2026 Form 1040-ES voucher with a check or money order payable to "United States Treasury"; a mailed payment counts as paid on the USPS postmark date, which is the date the item is processed at a facility, not always the day it was posted. Payments must be in US dollars; digital assets are not accepted. More than four payments are allowed as long as each period's total reaches the amount due. Source: [Form 1040-ES (2026)](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).

Payments are claimed on the 2026 Form 1040, due **15 April 2027**; an extension extends filing, not payment. Form 2210 (with Schedule AI where used) is attached to that return.

## Completion checklist

- 2026 total tax includes self-employment tax, Additional Medicare Tax, net investment income tax and other Schedule 2 taxes, less refundable credits.
- USD 1,000 test and the zero-tax 2025 exception checked.
- 2025 tax figured per the line 12b instructions, 12-month year and filed return confirmed, 100% or 110% chosen on 2025 AGI (and the MFS limit).
- Joint and separate changes between 2025 and 2026 handled.
- Both safe harbours shown, the smaller taken, and the decision explained.
- Withholding from every source counted as paid evenly unless actual dates help.
- Annualized method offered where income is uneven, and Schedule AI filed if used.
- Four 2026 dates given, and the 1 February 2027 option mentioned.
- Penalty, if any, figured per installment at the 2026 quarterly rates, simple interest.
- State estimated tax passed to the state skill.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Form 1040-ES (2026). Read for the General Rule (USD 1,000, 90%, 100%), Higher income taxpayers (USD 150,000, USD 75,000, 110%), Payment Due Dates (15 April, 15 June, 15 September 2026, 15 January 2027, 1 February 2027), farming and fishing (15 January 2027, 1 March 2027), fiscal-year dates, postmark rule, payment methods and the 2026 Estimated Tax Worksheet lines 1 to 15. | https://www.irs.gov/pub/irs-pdf/f1040es.pdf | 2026-11-13 |
| IRS Pub. 505 (2026). Read for chapter 2: Figure 2-A, married taxpayers and joint payments, the joint and separate split of the 2025 tax, amended estimated tax, and Worksheet 2-9 (annualization amounts 4, 2.4, 1.5, 1; 22.5% to 90%; prorated Social Security limits USD 46,125, 76,875, 123,000, 184,500). | https://www.irs.gov/pub/irs-pdf/p505.pdf | 2026-11-13 |
| Form 2210 (2025). Read for Part I, Part II boxes A to E and Schedule AI (the current edition; the 2026 form is not yet published). | https://www.irs.gov/pub/irs-pdf/f2210.pdf | 2026-11-13 |
| Instructions for Form 2210 (2025). Read for Waiver of Penalty, Table 1 (an applied overpayment is treated as paid on 15 April), the penalty worksheet day count, and the rule that Schedule AI used for one due date must be used for all. | https://www.irs.gov/pub/irs-pdf/i2210.pdf | 2026-11-13 |
| IRS quarterly interest rates page. Read for the 2026 underpayment rates: 7% (1st quarter, IRB 2025-48), 6% (2nd, IRB 2026-8), 7% (3rd, IRB 2026-22), 7% (4th, IRB 2026-36). | https://www.irs.gov/payments/quarterly-interest-rates | 2026-11-13 |
| 26 U.S.C. 6654 (govinfo). Read for (a) the addition to tax, (b) amount, period and order of crediting, (c) due dates, (d) required annual payment, 110% and USD 75,000, annualized installments, (e) the USD 1,000, no-liability and waiver exceptions, (f) meaning of tax, (g) withholding treated as paid evenly, (h) the January 31 rule, (i) farmers and fishermen, (j) nonresident aliens. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm | 2026-11-13 |
| 26 U.S.C. 6621 (govinfo). Read for (a)(2) the underpayment rate (federal short-term rate plus 3 points) and (b)(2)(B) the first 15 days of April. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap67-subchapC-sec6621.htm | 2026-11-13 |
| 26 U.S.C. 6622 (govinfo). Read for (b): no daily compounding for the section 6654 addition. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap67-subchapC-sec6622.htm | 2026-11-13 |
| 26 U.S.C. 275 (govinfo). Read for (a)(1): no deduction for federal income taxes. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partIX-sec275.htm | 2026-11-13 |
| Public Law 119-21 (One Big Beautiful Bill Act). Read to confirm it does not amend sections 6621, 6622 or 6654. | https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm | 2026-11-13 |

Not yet confirmed: the underpayment rate for 1 January to 31 March 2027 (which also applies to 1 to 15 April 2027 for 2026 penalties) was not yet published when read, so no penalty in this skill runs into 2027; the 2026 Form 2210 and its instructions were not yet published, so 2026 Form 2210 line numbers are not quoted; the old rule that installments stop at death was not found on an official page today and is now a referral (R-US-ET-7).
