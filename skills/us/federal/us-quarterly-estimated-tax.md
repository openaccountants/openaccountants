---
name: us-quarterly-estimated-tax
description: Compute US individual federal estimated tax for 2026 using Form 1040-ES, the USD 1,000 test, 90% current-year and 100% or 110% prior-year safe harbours, regular or annualized installments, withholding and Form 2210 penalties. Includes dated 2025 historical cases. Trigger on estimated tax, quarterly tax, safe harbor, 1040-ES, Form 2210 or annualized income. Federal only.
version: "3.2"
jurisdiction: US
category: federal
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# US federal estimated tax for individuals (Form 1040-ES), tax year 2026

An individual generally needs estimated payments if expected tax after withholding is at least USD 1,000 and withholding does not cover the required annual payment, subject to the exceptions below. Use the IRS worksheet so refundable credits are counted once. [Form 1040-ES (2026), General Rule and worksheet](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).

## Who this applies to

US citizens and resident aliens computing individual federal estimated tax, including sole proprietors and owners of disregarded single-member LLCs. This Guide computes amounts for professional review; it does not execute payments. Corporations, trusts, estates, nonresident aliens and state payments are routed below.

## Rates, bands and thresholds

Ordinary calendar-year rules, after checking the zero-tax and farming/fishing exceptions. “Tax” means the worksheet tax after its specified credits, excluding withholding; do not subtract refundable credits twice.

| Item | Amount or rule | Official source |
| --- | --- | --- |
| No estimated payments if worksheet tax minus withholding is less than | USD 1,000 | [Form 1040-ES, line 14b](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| Current-year safe harbour: share of the 2026 tax | 90% | [26 U.S.C. 6654(d)(1)(B)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Prior-year safe harbour: share of the 2025 tax | 100% | [26 U.S.C. 6654(d)(1)(B)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Prior-year safe harbour where 2025 AGI exceeds the limit below | 110% | [26 U.S.C. 6654(d)(1)(C)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| 2025 AGI limit for 100% (110% above it) | USD 150,000 | [26 U.S.C. 6654(d)(1)(C)(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| 2025 AGI limit, married filing separately for 2026 | USD 75,000 | [26 U.S.C. 6654(d)(1)(C)(ii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Each regular installment | 25% of the required annual payment | [26 U.S.C. 6654(d)(1)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| 1st installment due | 15 April 2026 | [Form 1040-ES, Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| 2nd installment due | 15 June 2026 | [Form 1040-ES, Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| 3rd installment due | 15 September 2026 | [Form 1040-ES, Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| 4th installment due | 15 January 2027 | [Form 1040-ES, Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| Fourth payment exception | File the 2026 return and pay the entire balance by 1 February 2027; this does not forgive earlier shortfalls | [Form 1040-ES, Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| Annualized cumulative percentages | 22.5%, 45%, 67.5%, 90% | [Pub. 505, Worksheet 2-9 line 22](https://www.irs.gov/publications/p505) |
| Annualized cumulative periods and income factors | January–March: 4; January–May: 2.4; January–August: 1.5; January–December: 1 | [Pub. 505, Worksheet 2-9](https://www.irs.gov/publications/p505) |
| Annualized prorated Social Security limits | USD 46,125; 76,875; 123,000; 184,500, before actual wages reduce the limit | [Pub. 505, Worksheet 2-9 lines 34–36](https://www.irs.gov/publications/p505) |
| Farmer/fisher eligibility | At least two-thirds of gross income from farming or fishing in 2025 or 2026 | [26 U.S.C. 6654(i)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm) |
| Farmer/fisher required payment | Smaller of 66 2/3% of 2026 tax and eligible 100% of 2025 tax; no 110% uplift | [Form 1040-ES, Special Rules](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| Farmer/fisher dates | One payment by 15 January 2027, or file and pay all tax by 1 March 2027 | [Form 1040-ES, Farming and fishing](https://www.irs.gov/pub/irs-pdf/f1040es.pdf) |
| Underpayment rate, January–March 2026 | 7% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Underpayment rate, April–June 2026 | 6% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Underpayment rate, July–September 2026 | 7% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Underpayment rate, October–December 2026 | 7% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |
| Historical individual underpayment rates | All four quarters of 2025: 7% | [IRS quarterly interest rates](https://www.irs.gov/payments/quarterly-interest-rates) |

## The base and required annual payment

1. Use the **2026 Estimated Tax Worksheet**: expected AGI after adjustments; deductions on lines 2a–2d, including QBI and eligible Schedule 1-A deductions; tax on line 4, AMT and any other line 6 taxes; subtract line 7 credits; add SE tax on line 9 and permitted line 10 taxes; subtract the refundable credits on line 11b to reach line 11c. Qualified dividends, capital gains and foreign earned income require the special tax worksheets. Line 10 has exclusions; do not include every Schedule 2 tax automatically. Household employment taxes are included only if withholding exists or estimates would otherwise be required. Use the line 10 instructions for the complete exclusions. [1040-ES, worksheet and lines 4/10 instructions](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).
2. **The zero-tax exception: no payments are required if the person was a US citizen or resident alien for all of 2025, the 2025 tax year was 12 months, and they had no tax liability for 2025** (total tax zero or no return required). Merely not filing a return does not establish this exception. [1040-ES, Exception](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).
3. Line 12a is the current-year amount; line 12b is the applicable prior-year amount. For line 12b, start with 2025 Form 1040 line 24 and make **all** reductions in “Figuring your 2025 tax,” including specified unreported payroll taxes, specified tax-favoured-account taxes, Exception 2 taxes and the listed refundable credits. Do not use the prior balance due or withholding as prior-year tax. [1040-ES, line 12b](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).
4. Line 12c is the smaller available amount. Line 14a subtracts expected withholding; zero or less means no estimates. Line 14b subtracts withholding from line 11c; less than the threshold means no estimates. Otherwise, where the first payment is due in April, line 15 is one-quarter of line 14a minus the overpayment actually applied to that installment. Credit it once. Timely payments must cover **each** required installment, not just the annual total. [1040-ES, worksheet](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).

### Boundary and exception table

| Situation | Treatment |
| --- | --- |
| 2025 AGI exactly USD 150,000 (or exactly USD 75,000 for MFS) | No high-income uplift; the statute says “exceeds” |
| 2025 return not filed, or 2025 a short year | Prior-year safe harbour not available: only 90% of 2026 tax under the ordinary rule; check the zero-tax exception first and farmer/fisher rules separately |
| Prior-year AGI or tax unknown | No usable prior-year safe-harbour result until established; a provisional higher-percentage budget is not proof of eligibility |
| Income estimate uncertain or withholding plus self-employment | Compute all taxes and withholding explicitly, label estimates and recheck before each due date; no automatic buffer or assumption that wages cover SE tax |

Authority: [26 U.S.C. 6654(d)–(e)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm).

### Spouses, withholding and uneven income

- When separate 2025 returns become a joint 2026 return, combine both spouses’ prior-year taxes. When a joint 2025 return becomes separate 2026 returns, apportion the joint tax using each spouse’s hypothetical separate 2025 tax **with the filing status used for 2026**, divided by their combined hypothetical separate taxes. Establish the applicable AGI test as well. [1040-ES, line 12b](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).
- Joint estimates are unavailable for spouses legally separated under a decree, spouses with different tax years, or a nonresident-alien spouse without an election to resident treatment. Registered domestic/civil-union partners who are not married under state law cannot pay jointly and claim only their own payments. [Pub. 505, Married Taxpayers](https://www.irs.gov/publications/p505).
- Withholding normally counts one-quarter on each due date, even if increased late in the year. Actual withholding dates can instead be established; wage and other withholding may be treated separately. A sufficient W-4 increase (or W-4P for periodic pensions) can therefore address earlier shortfalls. A late estimated payment stops accrual only when paid. Do not promise relief unless the amounts actually cover the requirements. [26 U.S.C. 6654(g)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm); [1040-ES, Increase Your Withholding](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).
- For seasonal income, a late capital gain, a mid-year move from wages to SE income, or no estimated-tax income in the first period, use **Pub. 505 Worksheet 2-9** to test annualization. Include period-specific deductions, credits, AMT, SE tax and other applicable taxes. Compute the cumulative percentage of annualized tax, subtract earlier **required installments**, and compare with the regular installment plus unrecovered earlier reductions. Then subtract prior payments and withholding as the worksheet directs. File Form 2210 with Schedule AI for all four periods when using this method, even if no penalty results. [Pub. 505, Annualized Income Installment Method and Worksheet 2-9](https://www.irs.gov/publications/p505); [1040-ES, No income subject to estimated tax during first payment period](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).
- If the annual estimate changes, use **Pub. 505 Worksheet 2-12**, not equal division of the remaining balance. The next payment catches up to the cumulative percentage for that due date, less previous estimates; the worksheet then allocates the remainder. Earlier shortfalls can still carry a penalty. [Pub. 505, Change in estimated tax and Worksheet 2-12](https://www.irs.gov/publications/p505).
- An elected prior-year overpayment generally counts from April 15 if the prior-year tax was fully paid before that date. If a later payment generated it, use that later payment date. This matters before using it to cure early installments. [Form 2210 instructions, line 11](https://www.irs.gov/instructions/i2210).

## Deadlines and filing

Ordinary calendar-year 2026 return and balance: **15 April 2027**, subject to applicable relief; an extension extends filing, not payment. [26 U.S.C. 6072(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm); [IRS filing extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return).

Fiscal-year individuals use the fifteenth day of months four, six and nine of the current year and month one of the following year. Weekend/legal-holiday dates move to the next business day. Check the specific IRS disaster announcement for the taxpayer’s eligibility, covered actions and postponed dates. [1040-ES, Fiscal year taxpayers](https://www.irs.gov/pub/irs-pdf/f1040es.pdf); [Form 2210 instructions, Federally declared disaster](https://www.irs.gov/instructions/i2210).

Payment options include IRS Online Account, free bank-account Direct Pay, EFTPS (enrolment required), electronic funds withdrawal with e-filing, and card/digital-wallet providers (fee charged). A mailed check/money order uses the correct-year voucher payable to “United States Treasury.” Use the US postmark date, which can differ from the day deposited. Payments are in USD; digital assets are not accepted. More than four payments are allowed if sufficient amounts are paid by each due date. [1040-ES, How To Pay and Payment Due Dates](https://www.irs.gov/pub/irs-pdf/f1040es.pdf).

## Penalties and interest

For each installment, underpayment is the positive excess of the required amount over timely payments. Credit later payments against the **oldest** unpaid installment. The period ends when that portion is paid or on 15 April 2027, whichever is earlier. [26 U.S.C. 6654(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm).

For each rate period: underpayment × annual rate × days unpaid / 365 for these non-leap-year cases. This is simple interest: section 6622(b) excludes section 6654 additions from daily compounding. The rate is the federal short-term rate plus three percentage points. The January–March rate also governs the first fifteen days of April for this penalty. **No 2027 rate is proved in this Guide: a penalty running into 2027 is on hold until the applicable published rate is read. Never carry forward a rate by assumption.** [26 U.S.C. 6621(a)(2), (b)(2)(B)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap67-subchapC-sec6621.htm); [26 U.S.C. 6622(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap67-subchapC-sec6622.htm); [Form 2210 instructions, penalty worksheet](https://www.irs.gov/instructions/i2210).

The 2025 Form 2210 was the edition read. It lets the IRS compute the penalty in ordinary cases; boxes B (partial waiver), C (annualization) and D (actual withholding dates) require self-computation and attachment, while A (full waiver) and E (different joint/separate filing status with a lower prior-year base) require page one under its flowchart. Use the final **2026** form and instructions when available for a 2026 filing; do not assume unchanged box or line numbers. [2025 Form 2210](https://www.irs.gov/pub/irs-prior/f2210--2025.pdf).

The IRS decides waivers for casualty/disaster/unusual circumstances where imposing the addition would be inequitable, or retirement after reaching age 62/disability in 2025 or 2026 with reasonable cause and no wilful neglect. A waiver is not automatic. For the request and documentation: **Check this point with one of our partner accountants.** [26 U.S.C. 6654(e)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm).

## Cross-border points and referrals

| Code/topic | Action |
| --- | --- |
| R-US-ET-1: corporations | Use `us-form-1120-c-corp` |
| R-US-ET-2: trusts and estates | Outside this individual computation. Check this point with one of our partner accountants. |
| R-US-ET-3: state estimates | Use `us-state-estimated-tax-safe-harbors-matrix` and the state Guide |
| R-US-ET-4: nonresident aliens | Outside this computation; use Form 1040-ES (NR). Check this point with one of our partner accountants. |
| R-US-ET-5: waiver requests | Check this point with one of our partner accountants. |
| R-US-ET-6: section 965, section 1062 farmland election, subpart F annualization | No usable special-rule calculation here. Check this point with one of our partner accountants. |
| R-US-ET-7: death during the year | No conclusion about remaining installments or estate liability. Check this point with one of our partner accountants. |
| Premium tax credit reconciliation, AMT calculation, foreign earned income | Use the applicable return/form computation; if facts or treatment are unresolved, check this point with one of our partner accountants. |

Use `us-schedule-c-and-se-computation` for Schedule C/SE and the deductible half of SE tax; `us-form-1040-individual-return` or the applicable current-year return Guide for underlying income tax, AMT, Additional Medicare Tax and NIIT; `us-qbi-deduction` for QBI; and `us-sole-prop-bookkeeping` for transactions. Do not apply 2025 return amounts to 2026 estimates. Higher investment income may affect estimates through the computed NIIT; this Guide does not compute NIIT from a bank description.

## Recognising payments in bank data

IRS, INTERNAL REVENUE SERVICE, IRS DIRECT PAY, EFTPS, ELECTRONIC FED TAX, US TREASURY, TREASURY 310, 1040-ES/1040ES and ESTIMATED TAX PAYMENT/EST TAX are **candidates only**. Timing around April/June/September/January 10–20 is a clue. Confirm the tax type, taxpayer, designated year and payment date against the IRS payment record; a payee or date alone is not classification evidence. Separate state payees (STATE TAX, CA FTB, NYS, IL DOR), FICA/Social Security, penalties/interest, refunds and annual 1040 balances. W-2 withholding comes from payroll records, not an assumed separate bank debit.

Confirmed personal federal income-tax payments are not Schedule C deductions. [IRS Pub. 334, Taxes](https://www.irs.gov/publications/p334).

## Worked cases

Unless a case says otherwise, the supplied “tax” is already figured on the applicable estimated-tax worksheet, the prior return was filed for twelve months and the taxpayer qualifies for the ordinary individual rules. A hypothetical payment scheduled after the read date is an arithmetic scenario, not evidence it occurred.

**Case 1, a decision: pay by the prior-year safe harbour or by the current-year estimate?** A single freelancer had 2025 AGI of USD 180,000 and 2025 tax (as figured for line 12b) of USD 40,000. Business is growing and the 2026 tax is estimated at USD 60,000. There is no withholding.

Prior-year: 2025 AGI is over USD 150,000, so 110% x USD 40,000 = USD 44,000, or USD 11,000 a quarter. Current-year: 90% x USD 60,000 = USD 54,000, or USD 13,500 a quarter. The required annual payment is the smaller, USD 44,000. Paying USD 11,000 on each of the four dates avoids the estimated-tax penalty if the 2025 return is filed for a full 12-month year and the prior-year tax is correctly figured, however high 2026 income turns out, keeps USD 10,000 in the business until April 2027, and leaves USD 16,000 to pay with the return by 15 April 2027 (set that aside). The current-year route is the cheaper one only if the 2026 tax is below USD 48,888.89 (90% of which is USD 44,000), and it carries risk: if the real 2026 tax is higher than estimated, 90% of the real figure is what counts. Recommend the prior-year route when income is rising. When income is falling sharply (for example a 2026 tax of USD 30,000, giving a 90% figure of USD 27,000), the current-year route is cheaper, but recheck the estimate before each due date.

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


### Historical 2025 cases: original inputs retained

These cases use the 2025 rules and dates, not the 2026 calendar above. [2025 Form 1040-ES](https://www.irs.gov/pub/irs-prior/f1040es--2025.pdf).

| 2025 installment | Due date | Source |
| --- | --- | --- |
| 1st | April 15, 2025 | [2025 Form 1040-ES](https://www.irs.gov/pub/irs-prior/f1040es--2025.pdf) |
| 2nd | June 16, 2025 | [2025 Form 1040-ES](https://www.irs.gov/pub/irs-prior/f1040es--2025.pdf) |
| 3rd | September 15, 2025 | [2025 Form 1040-ES](https://www.irs.gov/pub/irs-prior/f1040es--2025.pdf) |
| 4th | January 15, 2026 | [2025 Form 1040-ES](https://www.irs.gov/pub/irs-prior/f1040es--2025.pdf) |

Filing the 2025 return and paying the entire balance by **February 2, 2026** avoids only the fourth installment penalty. An eligible 2025 farmer/fisher instead has the **March 2, 2026** filing-and-full-payment alternative. [2025 Form 1040-ES, Payment Due Dates and Farming and fishing](https://www.irs.gov/pub/irs-prior/f1040es--2025.pdf).

**Historical examples 1–4 / tests 1–4 and 6:** single, 2024 AGI USD 95,000, 2024 tax USD 18,000, 2025 expected tax USD 22,000, no withholding: required USD 18,000, quarterly USD 4,500. MFJ, 2024 AGI USD 210,000, tax USD 42,000, 2025 expected USD 55,000, no withholding: required USD 46,200, quarterly USD 11,550. MFJ, 2024 AGI USD 120,000, tax USD 20,000, spouse withholding USD 25,000 and original 2025 expected tax USD 28,000: withholding covers the USD 20,000 prior-year base; no estimates. Single, 2025 expected tax USD 5,200 and part-time withholding USD 4,500: net USD 700, no estimates.

```oa-check
name: Original 2025 safe-harbour and threshold cases
inputs:
  single_2024_agi: 95000
  single_2024_tax: 18000
  single_2025_tax: 22000
  single_withholding: 0
  joint_2024_agi: 210000
  joint_2024_tax: 42000
  joint_2025_tax: 55000
  joint_withholding: 0
  wages_case_2024_agi: 120000
  wages_case_2024_tax: 20000
  wages_case_2025_tax: 28000
  spouse_withholding: 25000
  small_2025_tax: 5200
  part_time_withholding: 4500
steps:
  - single_current: single_2025_tax * 0.90
  - single_required: min(single_2024_tax, single_current)
  - single_quarter: (single_required - single_withholding) / 4
  - joint_prior: joint_2024_tax * 1.10
  - joint_current: joint_2025_tax * 0.90
  - joint_required: min(joint_prior, joint_current)
  - joint_quarter: (joint_required - joint_withholding) / 4
  - wages_required: min(wages_case_2024_tax, wages_case_2025_tax * 0.90)
  - wages_estimates: max(0, wages_required - spouse_withholding)
  - small_net: small_2025_tax - part_time_withholding
expected:
  single_current: 19800
  single_required: 18000
  single_quarter: 4500
  joint_prior: 46200
  joint_current: 49500
  joint_required: 46200
  joint_quarter: 11550
  wages_required: 20000
  wages_estimates: 0
  small_net: 700
```

**Historical example 5, bank classification:** `04/15/2025 ; IRS DIRECT PAY EST TAX ; DEBIT ; -4,500.00 ; USD`. Candidate first 2025 installment of USD 4,500; confirm the designated taxpayer, year and tax type. If confirmed personal federal income tax, exclude from Schedule C deductions. [Pub. 334](https://www.irs.gov/publications/p334).

**Historical test 5, penalty:** required annual USD 20,000 / USD 5,000 each; actual payments USD 3,000, USD 5,000, USD 5,000 and USD 5,000 (total USD 18,000), assumed paid on the four 2025 due dates. Preserve the original 7% rate assumption. If the residual USD 2,000 is paid on 15 April 2026, the total penalty is USD 140. The shortfall moves from April to June to September to January as each later payment first clears the older balance; it is incorrect to say later installments have no shortfall. Actual payment dates or relief change the result. [26 U.S.C. 6654(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm); [IRS rates](https://www.irs.gov/payments/quarterly-interest-rates).

```oa-check
name: Original 2025 penalty with oldest-first allocation
inputs:
  annual_required: 20000
  quarterly_required: 5000
  q1_paid: 3000
  q2_paid: 5000
  q3_paid: 5000
  q4_paid: 5000
  rate: 0.07
  days_to_june16: 62
  days_june16_to_sep15: 91
  days_sep15_to_jan15: 122
  days_jan15_to_apr15: 90
steps:
  - total_paid: q1_paid + q2_paid + q3_paid + q4_paid
  - first_shortfall: quarterly_required - q1_paid
  - june_shortfall: first_shortfall + quarterly_required - q2_paid
  - september_shortfall: june_shortfall + quarterly_required - q3_paid
  - january_shortfall: september_shortfall + quarterly_required - q4_paid
  - penalty: (first_shortfall * days_to_june16 + june_shortfall * days_june16_to_sep15 + september_shortfall * days_sep15_to_jan15 + january_shortfall * days_jan15_to_apr15) * rate / 365
expected:
  total_paid: 18000
  first_shortfall: 2000
  june_shortfall: 2000
  september_shortfall: 2000
  january_shortfall: 2000
  penalty: 140
```

**Historical first-year / annualized test:** original 2025 single taxpayer, no prior return, income Q1 USD 5,000, Q2 USD 8,000, Q3 USD 12,000, Q4 USD 75,000, total SE income USD 100,000, expected tax USD 25,000, no withholding. The current-year annual amount is USD 22,500. **No usable zero-payment conclusion follows from “no prior return.”** Establish the full-year citizenship/residence and zero-liability exception. If it does not apply, no prior-year safe harbour is available. The four calendar-quarter income figures also do not identify the March/May/August cumulative bases, deductions or credits needed for annualization. Exact installments are on hold until those inputs are established. This also corrects the shortened historical test “first year, no prior return.” [2025 Form 1040-ES, Exception and General Rule](https://www.irs.gov/pub/irs-prior/f1040es--2025.pdf); [Form 2210, Schedule AI instructions](https://www.irs.gov/instructions/i2210).

**Historical farmer test:** at least two-thirds farming income, expected 2025 tax USD 25,000. The current-year component is USD 16,666.67; the eligible prior-year tax could make the required amount lower. Confirm the gross-income eligibility year and prior-year tax. No usable final installment amount until then. If eligible, pay by 15 January 2026 or file and pay the entire tax by 2 March 2026. [2025 Form 1040-ES](https://www.irs.gov/pub/irs-prior/f1040es--2025.pdf); [26 U.S.C. 6654(i)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm).

```oa-check
name: Original 2025 first-year and farmer arithmetic, conditional outputs
inputs:
  q1_income: 5000
  q2_income: 8000
  q3_income: 12000
  q4_income: 75000
  first_year_expected_tax: 25000
  first_year_withholding: 0
  farmer_expected_tax: 25000
steps:
  - total_se_income: q1_income + q2_income + q3_income + q4_income
  - current_year_component: first_year_expected_tax * 0.90
  - farmer_current_component: farmer_expected_tax * 2 / 3
expected:
  total_se_income: 100000
  current_year_component: 22500
  farmer_current_component: 16666.67
```

**Historical seasonal edge case:** USD 20,000 earned in Q1–Q3 combined and a USD 180,000 project payment in Q4 (USD 200,000 combined). The original case did not give a tax year, period breakdown, deductions, withholding or prior-year tax. Preserve those unknowns: no usable installment amounts or conclusion that either method is better. Test annualization once the cumulative periods and tax inputs are established; **Check this point with one of our partner accountants.**

## Ask the client first

Obtain the immediately preceding return and transcript where needed (filed status, full-year coverage, correctly adjusted tax, AGI and joint/separate status); current-year filing status; expected income, deductions, credits and withholding for the cumulative periods; dated estimates and overpayment funding; farming/fishing gross income; residency, fiscal-year, disaster, death, retirement/disability and special-election facts. Read available records before asking. Hold any result that depends on an unknown fact.

Before delivery, check each exception, the year of every input and rate, both available annual bases, timely coverage of each installment, withholding allocation, annualization/recapture where relevant, and any state referral. Never schedule payments, recommend deliberate underpayment or apply a discretionary waiver yourself. Label outputs as estimates until professional review.

**Circular 230 §10.37:** this computational Guide uses the stated facts and assumptions. Consider all relevant facts, resolve missing or conflicting inputs, and obtain qualified professional review before filing or acting; no filing position or penalty protection is promised.

## Sources

| Official source and passages actually read | Read date |
| --- | --- |
| [Form 1040-ES (2026)](https://www.irs.gov/pub/irs-pdf/f1040es.pdf): General Rule, exceptions, higher income, withholding, special taxes, line 12b reductions/split, worksheet, dates, farming/fishing, fiscal years, payment methods/postmark and section 1062 boundary | 2026-11-26 |
| [Pub. 505 (2026)](https://www.irs.gov/publications/p505): Married Taxpayers, annualization, Worksheets 2-9 and 2-12 including catch-up and recapture | 2026-11-26 |
| [Form 1040-ES (2025)](https://www.irs.gov/pub/irs-prior/f1040es--2025.pdf): historical general/zero-tax/farming rules, dates and filing alternatives | 2026-11-26 |
| [2025 Form 2210](https://www.irs.gov/pub/irs-prior/f2210--2025.pdf) and [instructions](https://www.irs.gov/instructions/i2210): flowchart, boxes, annualization, waiver, disaster, overpayment funding dates, oldest-first payment allocation and day-count worksheet. Final 2026 filing details remain on hold | 2026-11-26 |
| [IRS quarterly rates](https://www.irs.gov/payments/quarterly-interest-rates): 2025 and 2026 individual underpayment rows. No 2027 rate relied on | 2026-11-26 |
| [26 U.S.C. 6654](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap68-subchapA-partI-sec6654.htm): (b)–(i), checked against operative 2026 IRS instructions above | 2026-11-26 |
| [26 U.S.C. 6621](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap67-subchapC-sec6621.htm): (a)(2) and (b)(2)(B); [6622(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap67-subchapC-sec6622.htm): simple-interest exception | 2026-11-26 |
| [26 U.S.C. 6072(a)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleF-chap61-subchapA-partV-sec6072.htm) and [IRS extensions](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return): ordinary filing date and payment boundary | 2026-11-26 |
| [Pub. 334, Taxes](https://www.irs.gov/publications/p334): no federal income-tax deduction; exact completed quote reused from `us-sole-prop-bookkeeping` proof | 2026-11-26 |
