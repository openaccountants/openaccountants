---
name: uk-payments-on-account
description: "UK Self Assessment payments on account for tax year 2026-27 (6 April 2026 to 5 April 2027), set from the 2025-26 return. Covers who must pay them (the GBP 1,000 threshold and the test that more than 80% was collected at source), the 31 January and 31 July due dates, the ordinary balancing payment on 31 January after the year, what is in the base (income tax and Class 4 NIC) and what is not (capital gains tax, student loans, voluntary Class 2), reducing payments with SA303 and the interest when the reduction was too big, coding out, Making Tax Digital for Income Tax, dated ordinary late-payment interest and referrals for specialist penalty rules. Trigger: 'payments on account', 'POA', 'SA303', 'reduce payments on account', 'July payment', 'balancing payment', '80% rule'. Out of scope: computing the tax itself (uk-income-tax-sa100, uk-self-employment-sa103, uk-scottish-income-tax), NIC rates (uk-national-insurance), capital gains (uk-capital-gains-sa108), non-residents (uk-non-resident-sa109)."
version: 3.6
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# UK payments on account (2026-27)

> **Source-cited draft.** No accountant has approved this version. Obtain professional review before filing or acting on it.

Payments on account are normally two advances towards the next Self Assessment bill, based on the preceding year's relevant amount. For 2026-27 they use the 2025-26 assessment. First obtain the SA302/return, HMRC statement, payment history, coding notices and any reduction claim; do not infer tax deductions or allocations from bank descriptions. Tax computation: `uk-income-tax-sa100`, `uk-self-employment-sa103` and `uk-national-insurance`.

## Who this applies to

- TMA 1970 s.59A applies to a person with a preceding-year income-tax self-assessment exceeding tax deducted at source, subject to both tests below. Residence alone is not an exemption. [s.59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml).
- With no preceding-year assessment establishing liability to payments on account, the first bill can instead be payable in full with the next year's first advance on the same January date. A missing or unfiled return does not itself establish exemption. [HMRC](https://www.gov.uk/understand-self-assessment-bill/payments-on-account).
- An HMRC officer can direct before 31 January following the tax year that s.59A does not apply for that year, with consequential adjustments. Do not assume such a direction exists. [s.59A(9)](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml).
- Partnerships and partner-level profit allocation (historical R-UK-POA-1), trusts (R-UK-POA-3), companies, tax-equalisation arrangements and contested assessments: **Check this point with one of our partner accountants.** Corporation tax route: `uk-corporation-tax`.

## Rates, bands and thresholds

| Item | Rate or amount | Period / condition | Official source |
|---|---|---|---|
| Threshold: relevant amount at or above which payments on account are due | GBP 1,000 | Both tests must be met; exactly GBP 1,000 is not exempt | https://www.gov.uk/understand-self-assessment-bill/payments-on-account ; https://www.legislation.gov.uk/uksi/2008/838/made/data.xml |
| At-source test: relevant amount must be at least this share of the assessed amount | 1 to 5 (20%); so more than 80% at source means no payments | Exactly 80% collected at source is not exempt under this test; 20% is computed from the statutory ratio | https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml ; https://www.legislation.gov.uk/uksi/1997/2491/made/data.xml ; https://www.gov.uk/understand-self-assessment-bill/payments-on-account |
| Each payment on account | 50% of the relevant amount | Before a valid reduction or other statutory adjustment; any odd penny goes on the second payment | https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml ; https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam1100 |
| First / second payments for 2026-27 | 31 January 2027 / 31 July 2027 | Ordinary s.59A dates | https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml |
| Balancing payment for 2026-27 | 31 January 2028 | Ordinary deadline; late-notice exception below | https://www.legislation.gov.uk/ukpga/1970/9/section/59B/data.xml |
| Ordinary late-payment interest | 8.00% from 24 November 2026; previously 7.75% from 9 January to 23 November 2026 | Actual period-specific rates, including future changes, must be used | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |
| Ordinary late-payment interest basis | Bank Rate plus 4% from 6 April 2025; plus 2.5% on or before 5 April 2025 | Use HMRC's effective dates, not the date of a Bank Rate announcement | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |

## The taxable base

- Start from the preceding year's income-tax and Class 4 liability after tax reliefs, with the statutory tax-at-source adjustments. Do not subtract payments on account already made when setting the next year's advances. HMRC's SAM1100 excludes CGT, tax deducted at source, underpayments transferred to the PAYE system, SA student/postgraduate loan repayments and Class 2. [SAM1100](https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam1100).
- relevant amount = assessed income tax and Class 4 for last year minus tax deducted at source
- each payment on account = 50% of the relevant amount
- Tax at source under s.59A(8) includes tax deducted/treated as deducted or paid for that year and amounts for that year to be coded out later, less amounts deducted in that year for previous years. A bank credit or PAYE salary amount does not prove any tax was deducted. [s.59A(8)](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml).
- **Excluded charges.** Voluntary Class 2 NIC is collected with the balancing payment and "will not be included in Payments on Account" (HMRC manual SAM121665). This refers to voluntary contributions actually elected and collected through SA, not an automatic charge for every week. Any remaining CGT and SA student/postgraduate loan charge belong in the annual reconciliation, with credit for amounts already paid or collected. [SAM121665](https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam121665); [SAM1100](https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam1100).
- **Reliefs.** Use each person's correctly computed assessment. Marriage Allowance transfers part of the transferor's allowance and gives the eligible recipient a tax reduction; the old claim that it reduces the transferor's tax and increases the recipient's was reversed. Gift Aid, pension relief, eligibility and any recomputation: **Check this point with one of our partner accountants.** [Marriage Allowance](https://www.gov.uk/marriage-allowance).
- **Coding out.** The ordinary facility requires a bill below GBP 3,000, existing PAYE taxation and a paper return by 31 October or online return by 30 December. It cannot be obtained by part-paying a bill of GBP 3,000 or more. It is unavailable if PAYE income is insufficient, tax would exceed 50% of PAYE income, or tax would more than double; it can also be declined on the return. Class 2 in this Guide cannot be collected this way. Use the actual coding decision in the s.59A(8) calculation. [HMRC coding conditions](https://www.gov.uk/pay-self-assessment-tax-bill/through-your-tax-code).
- **Balance / credit.** Reconcile the current-year assessment and excluded charges against statutory tax-at-source credits, payments already made and actual HMRC allocations. A negative balance is a potential repayment/credit, not a promise of immediate cash or interest. Under SA, repayments are requested; overpayments otherwise remain on the record until claimed or reallocated. Tax due within the next 45 days may absorb the refund. [s.59B(1)-(2)](https://www.legislation.gov.uk/ukpga/1970/9/section/59B/data.xml); [SAM111010](https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam111010); [refunds](https://www.gov.uk/self-assessment-tax-returns/claiming-a-tax-refund).
- **Allocation.** Match bank debits to HMRC's statement. HMRC normally allocates to overdue charges or those due within 45 days, earliest statutory due date first, then earliest tax year, then creation date. The 45-day parameter can vary. Do not split or designate a January debit as a particular advance without checking the allocation. [DMBM210160](https://www.gov.uk/hmrc-internal-manuals/debt-management-and-banking/dmbm210160).

## Deadlines and filing

The ordinary first/second advance dates are 31 January and 31 July: 2024-25 uses 31 January/31 July 2025; 2025-26 uses 31 January/31 July 2026; 2026-27 uses 31 January/31 July 2027. Ordinary balances are due 31 January 2026, 2027 and 2028 respectively. Thus January can combine the preceding year's balance and the current year's first advance. Ordinary online annual returns for 2025-26 and 2026-27 are due 31 January 2027 and 31 January 2028 respectively. [s.59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml); [s.59B](https://www.legislation.gov.uk/ukpga/1970/9/section/59B/data.xml); [return deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines).

- **Late notice.** If the s.7 notice was given within six months of the year-end but HMRC's s.8/8A notice was given after the following 31 October, s.59B(3) gives three months from that notice for the balance. This does not reschedule s.59A advances. Other unusual notices, amendments, discovery demands, payment dates or enquiries delaying repayments: **Check this point with one of our partner accountants.** [s.59B(3)-(6)](https://www.legislation.gov.uk/ukpga/1970/9/section/59B/data.xml).
- **Weekends / holidays.** The statutory interest date does not move merely because it is a non-business day. HMRC says payment should arrive by the preceding working day unless using Faster Payments or a debit/credit card. Allow the time required for the selected payment method. [s.86(3)](https://www.legislation.gov.uk/ukpga/1970/9/section/86/data.xml); [payment methods](https://www.gov.uk/pay-self-assessment-tax-bill).
- **SA303 reduction.** A claim before 31 January following the tax year must state grounds for believing that the year's assessed tax less statutory tax-at-source amounts will be lower. Under s.59A(4) each payment becomes half the stated lower relevant amount; under (3) it can be nil where the stated conditions hold. Lower earnings alone, cessation or departure does not establish a lower net liability, and inability to pay is not a valid reason. Apply through the online account's “Reduce payments on account” facility or send SA303. Simply paying less is not a claim. [s.59A(3)-(5)](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml); [SAM1040](https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam1040); [HMRC](https://www.gov.uk/understand-self-assessment-bill/payments-on-account).
- **Prior assessment changed.** Under s.59A(4A), a late assessment/amendment resets the affected payment to half the revised relevant amount, subject to reductions and (4B). A discovery assessment under s.29 adds half its tax to each payment under (4B), subject to reductions and subsequent variation. Under (5), repayment/further-payment adjustments give effect to these changes. Check the statement; do not presume processing is complete. [s.59A(4A)-(5)](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml).
- **Already paid one instalment?** The statutory reduction applies to each payment, with consequential credit/refund adjustments. Do not replace the second liability with “estimated annual tax minus the first cash payment” without reconciling both revised charges and the allocation. [s.59A(4)-(5)](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml).
- **MTD for Income Tax.** Quarterly updates are summaries, not tax returns or new tax payment dates. For standard 2026-27 periods the cumulative endpoints are 5 July / 5 October 2026 and 5 January / 5 April 2027, with deadlines 7 August / 7 November 2026 and 7 February / 7 May 2027. Payments on account retain their statutory January/July cycle. An already established 2025-26 July advance is not replaced by starting MTD on 6 April 2026. [quarterly updates](https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates); [s.59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml).
- **MTD scope and software (R-UK-POA-4).** The published qualifying-income phases are over GBP 50,000 in 2024-25 → 6 April 2026; over GBP 30,000 in 2025-26 → 6 April 2027; over GBP 20,000 in 2026-27 → 6 April 2028, for relevant sole traders/landlords, subject to exemptions. Individual qualifying-income, exemption, registration, compatible-software and annual-return procedures: **Check this point with one of our partner accountants.** [HMRC scope](https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax).
- **Unable to pay?** Contact HMRC about Time to Pay; do not treat this as a reduction in liability. Budget payments before a deadline and bank transfer, card or Direct Debit routes are described by HMRC. A plan's eligibility, interest, penalty consequences and any disputed allocation: **Check this point with one of our partner accountants.** [paying](https://www.gov.uk/pay-self-assessment-tax-bill).

## Penalties and interest

Late payments on account carry interest from the statutory date until payment, including where the due date is a non-business day. For actual charges use the ordinary income-tax rate for each period, not corporation-tax instalment rates or a forecast Bank Rate. The dated rates above apply to ordinary income-tax late-payment interest. [s.86(1)-(3)](https://www.legislation.gov.uk/ukpga/1970/9/section/86/data.xml); [HMRC rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates).

- **After a reduction.** For s.86(4)-(6), interest treats each advance as the lower of (a) the reduced advance plus half the qualifying income-tax balancing amount, and (b) the unreduced advance. This assumes both reduced advances were paid; CGT and other payments on account are excluded from the specified balancing amount. Do not use the total SA cash balance including loans/CGT as that statutory amount. [s.86(4)-(6)](https://www.legislation.gov.uk/ukpga/1970/9/section/86/data.xml).
- **Late-payment penalties do not apply to payments on account.** This does not protect an incorrect reduction claim: a fraudulent or negligent incorrect statement under s.59A(3)/(4) can attract a penalty up to the difference between the correct advance and that actually paid. [HMRC penalties](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax); [s.59A(6)](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml).
- **Ordinary balancing-payment penalties.** Under the current Self Assessment regime, HMRC states 5% of relevant unpaid tax at 30 days, six months and twelve months, plus interest. Determine the applicable tax year's regime, any plan and defences before calculating a penalty. [HMRC](https://www.gov.uk/self-assessment-tax-returns/penalties).
- **MTD penalties / late filing.** These are separate from POA interest. Joining MTD on 6 April 2026 does not move the 2025-26 return into the new penalties: HMRC states the new regime starts with the 2026-27 return deadline of 31 January 2028. Detailed late-payment percentages, first-year grace, volunteers, later-year changes, points, appeals and payment-plan effects: **Check this point with one of our partner accountants.** [HMRC MTD penalties](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax).
- **Repayment interest / remission / deductions.** Repayment interest requires a qualifying overpayment and qualifying dates; it is not automatic on all excess advances. Whether s.86(7)-(9) remits interest in a repayment case, and the deductibility of any interest or penalty: **Check this point with one of our partner accountants.** [SAM111010](https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam111010); [s.86](https://www.legislation.gov.uk/ukpga/1970/9/section/86/data.xml).

## Cross-border points

Non-residents, arrivals, departures and UK property/trade cases (historical R-UK-POA-2) still require the s.59A liability tests; residence alone does not answer them. Do not assume a departure stops UK income or reduces UK tax. Foreign tax credit relief, foreign tax's place in the assessed/at-source amounts, source deductions and any disposal-payment credits: **Check this point with one of our partner accountants.** Routes: `uk-statutory-residence-test`, `uk-non-resident-sa109`, `uk-foreign-tax-and-withholding`, `uk-capital-gains-sa108`. [s.59A](https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml).

## Worked examples

**Example 1: sole trader with a student loan (simple).** Priya is self-employed. Her 2025-26 return shows income tax and Class 4 of GBP 9,000. GBP 1,000 was deducted at source from a small PAYE job. She paid payments on account for 2025-26 of GBP 3,000 each. Her 2025-26 return also shows a student loan repayment of GBP 1,200 and capital gains tax of GBP 500.

The relevant amount is GBP 9,000 minus GBP 1,000 = GBP 8,000. That is over GBP 1,000. It is 8,000 / 9,000 = 88.9% of the assessed amount, well above one fifth, so both tests point to payments on account. Each 2026-27 payment is half of GBP 8,000 = GBP 4,000.

Her 2025-26 balancing payment is GBP 8,000 minus GBP 6,000 already paid, plus GBP 1,200 student loan and GBP 500 capital gains tax = GBP 3,700. On 31 January 2027 she pays GBP 3,700 plus the first 2026-27 payment of GBP 4,000 = GBP 7,700. On 31 July 2027 she pays GBP 4,000.

```oa-check
name: Payments on account for 2026-27 from a 2025-26 bill with student loan and CGT
inputs:
  assessed: 9000
  at_source: 1000
  poas_paid_2025_26: 6000
  student_loan: 1200
  cgt: 500
steps:
  - relevant: assessed - at_source
  - share_of_assessed: round(relevant / assessed, 4)
  - each_poa: relevant / 2
  - balancing_2025_26: relevant - poas_paid_2025_26 + student_loan + cgt
  - due_31_jan_2027: balancing_2025_26 + each_poa
  - due_31_jul_2027: each_poa
expected:
  relevant: 8000.00
  share_of_assessed: 0.8889
  each_poa: 4000.00
  balancing_2025_26: 3700.00
  due_31_jan_2027: 7700.00
  due_31_jul_2027: 4000.00
```

**Example 2: a reduction that went too far (edge case).** Tom's 2025-26 relevant amount was GBP 10,000, so his 2026-27 payments on account were GBP 5,000 each. Expecting a quiet year, he claimed in December 2026 to cut them to GBP 1,500 each (a stated amount of GBP 3,000). He paid GBP 1,500 on 31 January 2027 and GBP 1,500 on 31 July 2027. His 2026-27 return shows a relevant amount of GBP 6,000.

Assume no excluded charges, further credits, amended liabilities or other allocation changes. His balancing payment due 31 January 2028 is GBP 6,000 minus GBP 3,000 = GBP 3,000. Under s. 86(5), interest is worked out as if each payment on account had been the lower of GBP 1,500 plus half of GBP 3,000 (GBP 3,000) and the original GBP 5,000. That is GBP 3,000, so each payment was GBP 1,500 short. For comparison with the original example only, stipulate a constant **hypothetical** annual rate of 7.75%, a 365-day divisor and the original 365/184 charged-day assumptions. This gives GBP 116.25 and GBP 58.60, total GBP 174.85. These are arithmetic assumptions, **not the rates or a certified HMRC charge for 2027-28**: the current rate is already 8% from 24 November 2026, and future rate periods/day counts must be checked. No late-payment penalty applies to the POAs, but any fraudulent/negligent reduction penalty is a separate question. **Check this point with one of our partner accountants.**

```oa-check
name: Interest after an SA303 claim that was too low (TMA 1970 s. 86(5)), 2026-27
inputs:
  original_poa: 5000
  reduced_poa: 1500
  actual_relevant: 6000
  rate_pct: 7.75
  days_first: 365
  days_second: 184
steps:
  - balancing: actual_relevant - 2 * reduced_poa
  - deemed_poa: min(reduced_poa + balancing / 2, original_poa)
  - shortfall_each: deemed_poa - reduced_poa
  - interest_first: round(shortfall_each * rate_pct / 100 * days_first / 365, 2)
  - interest_second: round(shortfall_each * rate_pct / 100 * days_second / 365, 2)
  - interest_total: interest_first + interest_second
expected:
  balancing: 3000.00
  deemed_poa: 3000.00
  shortfall_each: 1500.00
  interest_first: 116.25
  interest_second: 58.60
  interest_total: 174.85
```

**Example 3: the two tests (threshold cases).** All figures are for the 2025-26 return, setting 2026-27 payments.
- Relevant amount GBP 850 (or GBP 980): under GBP 1,000, so no payments on account. The whole amount is paid with the balancing payment on 31 January 2027 (s. 59A(1)(c); reg 3).
- Assessed GBP 20,000, GBP 17,000 deducted at source, relevant amount GBP 3,000: 85% was collected at source, so no payments on account even though GBP 3,000 is over GBP 1,000 (s. 59A(1)(d); reg 4).
- An employee with a side trade: assessed GBP 18,000, GBP 14,000 through PAYE (the earlier EC3 also specified GBP 50,000 employment income and GBP 15,000 self-employment income; treat the assessed/deducted amounts as stipulated, not as a tax computation from those earnings). Only 77.8% at source, so payments on account apply: relevant amount GBP 4,000, each payment GBP 2,000.

```oa-check
name: The 80% at-source test, 2025-26 figures setting 2026-27 payments
inputs:
  assessed_a: 20000
  at_source_a: 17000
  assessed_b: 18000
  at_source_b: 14000
steps:
  - at_source_share_a: round(at_source_a / assessed_a, 4)
  - at_source_share_b: round(at_source_b / assessed_b, 4)
  - relevant_b: assessed_b - at_source_b
  - each_poa_b: relevant_b / 2
expected:
  at_source_share_a: 0.8500
  at_source_share_b: 0.7778
  relevant_b: 4000.00
  each_poa_b: 2000.00
```

**Example 4: excluded items taken out (edge case).** A 2025-26 return shows income tax and Class 4 of GBP 4,000, capital gains tax of GBP 3,000, an eligible voluntary Class 2 election for 52 weeks at the 2025-26 rate of GBP 3.50 a week (GBP 182; the rate is GBP 3.65 from 2026-27 in the HMRC rates table) and a student loan repayment of GBP 1,200. Assume no tax at source, previous payments, disposal-payment credits or other adjustments. The annual total before payments on account is GBP 8,382, but the base is GBP 4,000 only. Each 2026-27 payment on account is GBP 2,000, due 31 January 2027 and 31 July 2027. If the total had been used, each payment would wrongly be GBP 4,191. A student loan alone can also push a bill over GBP 1,000 when the income tax part is under it; then no payments on account are due.

```oa-check
name: Base with capital gains tax, voluntary Class 2 and student loan removed, 2026-27 payments
inputs:
  income_tax_and_class4: 4000
  cgt: 3000
  weekly_class2: 3.50
  weeks: 52
  student_loan: 1200
steps:
  - class2: weekly_class2 * weeks
  - total_due: income_tax_and_class4 + cgt + class2 + student_loan
  - each_poa: income_tax_and_class4 / 2
expected:
  class2: 182.00
  total_due: 8382.00
  each_poa: 2000.00
```

**Example 5: a late payment on account (interest illustration).** A first payment on account of GBP 3,000 due 31 January 2026 is paid on 15 April 2026, 74 days late. The ordinary rate for that historical period was 7.75% (Bank Rate 3.75% plus 4%). Using the original stipulated 74 days and 365-day divisor, the simple-interest illustration is GBP 3,000 x 7.75% x 74 / 365 = GBP 47.14 (the historical GBP 47.12 was an arithmetic error). This is not a certified account charge or a rate for a different period. No late-payment penalty applies to a late payment on account. Actual HMRC day counts, rounding and allocations: **Check this point with one of our partner accountants.**

```oa-check
name: Late payment interest on a payment on account paid 74 days late at 7.75%
inputs:
  overdue: 3000
  rate_pct: 7.75
  days: 74
steps:
  - interest: round(overdue * rate_pct / 100 * days / 365, 2)
expected:
  interest: 47.14
```

**Example 6: three years in cash (full cycle).** A contractor with no PAYE income, CGT, loan charges or Class 2 adjustments had a 2023-24 bill under GBP 1,000, so no payments on account for 2024-25. The 2024-25 relevant amount is GBP 12,000.
- 31 January 2026: 2024-25 balancing payment GBP 12,000 plus first 2025-26 payment GBP 6,000 = GBP 18,000. 31 July 2026: GBP 6,000.
- If 2025-26 comes to GBP 12,000: balancing payment nil; 31 January 2027 cash GBP 6,000 (first 2026-27 payment); 31 July 2027 GBP 6,000.
- If 2025-26 comes to GBP 14,000: balancing payment GBP 2,000 plus first 2026-27 payment GBP 7,000 = GBP 9,000 on 31 January 2027; GBP 7,000 on 31 July 2027.
- If 2025-26 comes to GBP 8,000: GBP 4,000 overpaid. The first 2026-27 payment is GBP 4,000. If the credit remains available and HMRC sets it against that advance, nothing is paid on 31 January 2027; otherwise reconcile the statement and refund position.
- Inside MTD for Income Tax from 6 April 2026 the quarterly updates add no payment dates; the same cash dates apply.

```oa-check
name: Three-year cash cycle, payments on account for 2025-26 and 2026-27
inputs:
  relevant_2024_25: 12000
  actual_high: 14000
  actual_low: 8000
steps:
  - jan_2026_cash: relevant_2024_25 + relevant_2024_25 / 2
  - poas_paid_2025_26: relevant_2024_25
  - jan_2027_cash_high: actual_high - poas_paid_2025_26 + actual_high / 2
  - overpaid_low: poas_paid_2025_26 - actual_low
  - jan_2027_cash_low: max(actual_low / 2 - overpaid_low, 0)
expected:
  jan_2026_cash: 18000.00
  jan_2027_cash_high: 9000.00
  overpaid_low: 4000.00
  jan_2027_cash_low: 0.00
```


**Historical inputs and identifiers retained.** These are stipulated tax figures, not computations of tax from earnings. Apply both tests and assume no other credits, charges, reductions or conflicting allocations unless stated. The statutory rules and HMRC sources above govern these cases.

- **Old Example 1 / Test 1:** relevant amount GBP 6,000 with no at-source exemption gives GBP 3,000 each; the original dated advances were 31 January and 31 July 2025 (2024-25), not 2026-27.
- **Old computation rows:** GBP 5,000 → GBP 2,500 each; GBP 12,000 → GBP 6,000 each; if the year's relevant amount matches, balance nil. GBP 800, GBP 850 (old Example 2 / Test 2) or GBP 980 (EC4) falls below the threshold; the corresponding amount remains in the ordinary annual balance.
- **Old Test 6:** GBP 4,000 + GBP 4,000 paid against GBP 6,500 relevant liability gives GBP 1,500 credit, subject to repayment/offset processing.
- **EC2:** a claim to nil followed by GBP 8,000 actual relevant liability gives GBP 8,000 balancing liability. The interest base per advance is the lower of GBP 4,000 and the original unreduced advance; that original advance is missing, so GBP 4,000 cannot be asserted unconditionally. **Check this point with one of our partner accountants.**
- **EC5 / EC9:** September cessation or a prior-year amendment requires a current liability forecast and the revised assessment/statement; neither automatically proves reduction eligibility or the cash refund date. **Check this point with one of our partner accountants.**
- **EC6:** original total GBP 20,000 including GBP 12,000 CGT gives GBP 8,000 relevant amount and GBP 4,000 each only if the other amounts are correctly classified and the at-source test is met. Ask HMRC to correct wrongly established charges; paying a lower amount alone does not amend them.
- **EC7:** GBP 600 relevant tax plus GBP 900 student loan gives GBP 1,500 total but no advance: the relevant tax is below GBP 1,000.
- **EC8:** a Saturday 31 January does not shift to Monday 2 February for interest. Use the payment-method/preceding-working-day rule above.
- **EC10:** the historical GBP 1,260 Marriage Allowance transfer is not a separate POA exclusion; use the correctly computed assessments, with the transferor/recipient roles corrected above. Eligibility and actual tax effects: **Check this point with one of our partner accountants.**
- **Old Example 4 / Test 4:** retain the original stipulated Class 2 GBP 179.40, alongside GBP 4,000 income tax/Class 4, GBP 3,000 CGT and GBP 1,200 loan: total GBP 8,379.40, relevant amount GBP 4,000, each advance GBP 2,000 if both tests apply. GBP 179.40 is not asserted as 52 weeks at the later rate; the dated 2025-26 version in Example 4 uses GBP 182.
- **Old Test 7:** the separate historical inputs Bank Rate 5.25% + 2.5%, GBP 3,000 and 74 days give a hypothetical 7.75% annual rate and GBP 47.14 using 365 days. No year was provided: do not apply that base-rate add-on to the dated 2026 case. **Check this point with one of our partner accountants.**
- **Old Test 8 / Example 7 B1:** retain GBP 12,000 relevant amounts for 2024-25, 2025-26 **and 2026-27**. With GBP 6,000 advances each year and no reductions or other adjustments, the 2026-27 balance is nil and 31 January 2028 cash is GBP 6,000 for the first 2027-28 advance.
- **Old Test 9 / EC11:** stipulated MTD entry on 6 April 2026 and preceding relevant amount GBP 10,000 gives GBP 5,000 on 31 January and 31 July 2027 if the at-source test is met. Quarterly updates do not settle those advances; ordinary 2026-27 annual reconciliation remains due 31 January 2028.

```oa-check
name: Historical retained arithmetic including old Test 6 and EC6 EC7
inputs:
  old_standard: 6000
  old_row: 5000
  paid_first: 4000
  paid_second: 4000
  actual_test6: 6500
  ec6_total: 20000
  ec6_cgt: 12000
  ec7_tax: 600
  ec7_loan: 900
  legacy_class2: 179.40
  income_tax_class4: 4000
  cgt: 3000
  loan: 1200
  mtd_relevant: 10000
steps:
  - standard_each: old_standard / 2
  - row_each: old_row / 2
  - credit_test6: paid_first + paid_second - actual_test6
  - ec6_relevant: ec6_total - ec6_cgt
  - ec6_each: ec6_relevant / 2
  - ec7_total: ec7_tax + ec7_loan
  - legacy_total: income_tax_class4 + cgt + legacy_class2 + loan
  - mtd_each: mtd_relevant / 2
expected:
  standard_each: 3000
  row_each: 2500
  credit_test6: 1500
  ec6_relevant: 8000
  ec6_each: 4000
  ec7_total: 1500
  legacy_total: 8379.40
  mtd_each: 5000
```

## Ask the client first

Read the existing records before asking: obtain the preceding assessment and statutory tax-at-source/coding breakdown; separate excluded charges and already paid amounts; obtain reduction claims and reasons, amended/discovery assessments, current-year forecasts and actual allocations. Confirm the tax year, notice dates, first-year/residence or departure issues and whether MTD applies to that year's return. Missing facts, disputed charges, unusual remissions or specialist cases: **Check this point with one of our partner accountants.**

## Sources

Completed SA100 / SA103 / National Insurance proof reads are reused only for identical operative claims. The following lists the exact parts read or reused; a successful link request alone is not a source read.

| Official source and part read | URL | Read / applicability |
|---|---|---|
| TMA 1970 s.59A, full operative section: tests, dates, reductions, amendments, penalties, coding, directions | https://www.legislation.gov.uk/ukpga/1970/9/section/59A/data.xml | 2026-11-26 |
| TMA 1970 s.59B(1)-(8), balance, credits and notice/payment exceptions | https://www.legislation.gov.uk/ukpga/1970/9/section/59B/data.xml | 2026-11-26 |
| TMA 1970 s.86(1)-(9), interest and reduction/repayment conditions | https://www.legislation.gov.uk/ukpga/1970/9/section/86/data.xml | 2026-11-26 |
| SI 1996/1654 regs 3/4 original text, read together with amending instruments below | https://www.legislation.gov.uk/uksi/1996/1654/regulation/3/data.xml ; https://www.legislation.gov.uk/uksi/1996/1654/regulation/4/data.xml | 2026-11-26; original text alone is not the current threshold |
| SI 2008/838 regs 1/2 and SI 1997/2491 regs 1/2, commencement and threshold/proportion amendments | https://www.legislation.gov.uk/uksi/2008/838/made/data.xml ; https://www.legislation.gov.uk/uksi/1997/2491/made/data.xml | 2026-11-26 |
| HMRC POA guidance, all calculation, first-year, reduction and interest sections | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | SA100-41 completed read 2026-11-26 reused; operative guidance also read here |
| SAM1100 calculation exclusions, automatic setup and odd penny; SAM1040 validity/reasons and incorrect claims | https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam1100 ; https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam1040 | 2026-11-26 |
| SAM121665 current opening notice and accounting, election/payment and coding sections; no obsolete mandatory-Class-2 rule used | https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam121665 | 2026-11-26 |
| PAYE coding: eligibility, exclusions and opt-out | https://www.gov.uk/pay-self-assessment-tax-bill/through-your-tax-code | 2026-11-26 |
| Payment overview: payment methods, lead times and weekend rule | https://www.gov.uk/pay-self-assessment-tax-bill | 2026-11-26 |
| Refunds: claim/45-day offset; SAM111010 qualifying repayment interest and dates; DMBM210160 allocation order and parameter | https://www.gov.uk/self-assessment-tax-returns/claiming-a-tax-refund ; https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam111010 ; https://www.gov.uk/hmrc-internal-manuals/debt-management-and-banking/dmbm210160 | 2026-11-26 |
| HMRC ordinary income-tax interest basis/current and historical rates, not corporation-tax instalment categories | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | Completed UKS131 / NI42 / SA100-47 read 2026-11-22 reused for 8% update; operative periods confirmed 2026-11-26; repayment dependency read 2026-11-26 |
| Ordinary annual deadlines and current SA late-payment penalties | https://www.gov.uk/self-assessment-tax-returns/deadlines ; https://www.gov.uk/self-assessment-tax-returns/penalties | Completed SA100-38/46 and NI53 reads 2026-11-26 reused |
| MTD scope: relevant sources, phased thresholds and exemption route | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax | 2026-11-26 |
| MTD quarterly summaries, cumulative standard periods and deadlines | https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates | 2026-11-26 |
| MTD penalties: commencement, POA exclusion, payment-plan and regime conditions; detailed charge computations referred | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax | 2026-11-26 |
| Marriage Allowance transferor allowance / recipient reduction, no reversed tax effect | https://www.gov.uk/marriage-allowance ; https://www.legislation.gov.uk/ukpga/2007/3/section/55B/data.xml | Completed SA100-55 read 2026-11-26 reused |
| Original case voluntary Class 2 rates: 2025-26 GBP 3.50, 2026-27 GBP 3.65; eligibility not inferred | https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions | Completed NI23/53 reads 2026-11-26 reused |
