---
name: uk-payments-on-account
description: "UK Self Assessment payments on account for tax year 2026-27 (6 April 2026 to 5 April 2027), set from the 2025-26 return. Covers who must pay them (the GBP 1,000 threshold and the test that more than 80% was collected at source), the 31 January and 31 July due dates, the balancing payment on 31 January after the year, what is in the base (income tax and Class 4 NIC) and what is not (capital gains tax, student loans, voluntary Class 2), reducing payments with SA303 and the interest when the reduction was too big, coding out, Making Tax Digital for Income Tax, late payment interest at Bank Rate plus 4% and late payment penalties. Trigger: 'payments on account', 'POA', 'SA303', 'reduce payments on account', 'July payment', 'balancing payment', '80% rule'. Out of scope: computing the tax itself (uk-income-tax-sa100, uk-self-employment-sa103, uk-scottish-income-tax), NIC rates (uk-national-insurance), capital gains (uk-capital-gains-sa108), non-residents (uk-non-resident-sa109)."
version: 3.3
jurisdiction: GB
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK payments on account (2026-27)

> **Source-cited draft.** Built from the Taxes Management Act 1970 (TMA 1970) ss. 59A, 59B and 86, the Income Tax (Payments on Account) Regulations 1996 (SI 1996/1654) as amended in 1997 and 2008, Finance Act 2009 Schedule 56 and HMRC pages on GOV.UK, all read on 2026-10-24 or 2026-10-26. No accountant has reviewed it. Do not file from it without review by a qualified UK professional.

Payments on account are two advance payments towards this year's Self Assessment bill, each half of last year's bill. This skill works out whether they are due, how much, and what happens when they are too high, too low or late. The tax itself is computed in `uk-income-tax-sa100` (with `uk-self-employment-sa103` for trading profit and `uk-national-insurance` for Class 4). Their dates match this skill.

## Who this applies to

- **Anyone assessed under Self Assessment.** TMA 1970 s. 59A(1) applies to "any person" who, for the year before, was assessed to income tax under s. 9 (the self-assessment) in an amount that exceeds the tax deducted at source. The rule has no residence test.
- **The excess is the "relevant amount".** It is last year's assessed income tax (and Class 4 NIC) minus tax deducted at source. Tax deducted at source means PAYE and other tax deducted or treated as paid for the year, plus amounts to be coded out in later years, less amounts coded in from earlier years (s. 59A(8)).
- **Two tests take a person out.** No payments on account are due if:
  - the relevant amount is under GBP 1,000 (s. 59A(1)(c); SI 1996/1654 reg 3, raised from GBP 500 to GBP 1,000 by SI 2008/838 from 2009-10), or
  - the relevant amount is less than one fifth of the assessed amount (s. 59A(1)(d); reg 4, "one to five" since SI 1997/2491). Put another way: more than 80% of last year's tax was collected at source.
- **First year in Self Assessment.** With no assessment for the year before, s. 59A does not apply. The whole bill is paid as one balancing payment, and the first payment on account for the next year falls on the same 31 January.
- **HMRC can switch it off.** An officer can direct, before 31 January after the year, that s. 59A does not apply to a person for that year (s. 59A(9)).
- **Out of scope here:** partnerships (each partner's own return carries their share; the partnership pays nothing), trustees (s. 59A also applies to them, but trust returns are not covered by this skill), and companies (corporation tax has its own instalment rules, see `uk-corporation-tax`).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Threshold: relevant amount at or above which payments on account are due | GBP 1,000 | 2009-10 onwards, so 2026-27 | https://www.legislation.gov.uk/uksi/2008/838/made |
| At-source test: relevant amount must be at least this share of the assessed amount | 1 to 5 (20%); so more than 80% at source means no payments | 2026-27 | https://www.legislation.gov.uk/uksi/1996/1654/regulation/4 ; https://www.legislation.gov.uk/uksi/1997/2491/made |
| Each payment on account | 50% of the relevant amount | 2026-27 | https://www.legislation.gov.uk/ukpga/1970/9/section/59A |
| First payment on account for 2026-27 | 31 January 2027 | 2026-27 | https://www.legislation.gov.uk/ukpga/1970/9/section/59A |
| Second payment on account for 2026-27 | 31 July 2027 | 2026-27 | https://www.legislation.gov.uk/ukpga/1970/9/section/59A |
| Balancing payment for 2026-27 | 31 January 2028 | 2026-27 | https://www.legislation.gov.uk/ukpga/1970/9/section/59B |
| Late payment interest | Bank of England base rate plus 4% (plus 2.5% on or before 5 April 2025) | from 6 April 2025 | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |
| Late payment interest rate in force | 7.75% from 9 January 2026 (Bank Rate 3.75%, held on 17 September 2026) | 2026-27 | same HMRC page; https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate |
| Repayment interest rate in force | 2.75% from 9 January 2026 (base rate minus 1%, floor 0.5%) | 2026-27 | same HMRC page |
| Late payment penalty, not in MTD | 5% of unpaid tax at 30 days, 6 months and 12 months (balancing payment only) | 2026-27 | https://www.gov.uk/self-assessment-tax-returns/penalties ; https://www.legislation.gov.uk/ukpga/2009/10/schedule/56 |
| Late payment penalty, in MTD for Income Tax | 2026-27: 3% at day 15, 3% more at day 30, then 10% a year from day 31; first year: no penalty if paid or a plan agreed within 30 days. 2027-28: 4% and 4%, then 10% a year | 2026-27, 2027-28 | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax |
| Coding out limit | Balance under GBP 3,000, online return by 30 December | 2026-27 | https://www.gov.uk/pay-self-assessment-tax-bill/through-your-tax-code |
| MTD for Income Tax start | From 6 April 2026 if 2024-25 qualifying income over GBP 50,000; 6 April 2027 if 2025-26 over GBP 30,000; 6 April 2028 if 2026-27 over GBP 20,000 | 2026-27 onwards | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax |

## The taxable base

- **What goes in.** The relevant amount is last year's income tax and Class 4 NIC assessed through Self Assessment, minus tax deducted at source (s. 59A(1), (8)). GOV.UK confirms Class 4 is included: payments on account are "payments towards your next tax bill (including Class 4 National Insurance if you're self-employed)".
- **What stays out.** Capital gains tax and student loan (and postgraduate loan) repayments are paid with the balancing payment, not on account (GOV.UK payments on account page). Voluntary Class 2 NIC is collected with the balancing payment and "will not be included in Payments on Account" (HMRC manual SAM121665). Capital gains tax is also left out when s. 86 works out interest after a claim (s. 86(6)(b)).
- **Reliefs that change the tax itself** change the base. A Marriage Allowance transfer lowers the transferor's tax and raises the recipient's; each person's payments on account follow their own net figure. Gift Aid and pension relief work the same way through the computed tax.
- **Coding out.** Where a balance under GBP 3,000 is collected through next year's PAYE code, that amount counts as tax deducted at source for the year it relates to (s. 59A(8)(b)). It does not form part of the relevant amount, so it can take the person under GBP 1,000 or over the 80% line. A part payment to get under GBP 3,000 does not qualify.
- **Formula.**
  - relevant amount = assessed income tax and Class 4 for last year minus tax deducted at source
  - each payment on account = 50% of the relevant amount
  - balancing payment = this year's assessed income tax and Class 4, minus tax at source, minus both payments on account, plus capital gains tax, student loan and any voluntary Class 2.
- **If last year's figure changes.** If last year's return is filed or amended after a payment date, each payment is reset to 50% of the new relevant amount and treated as always having been that (s. 59A(4A)). A discovery assessment for last year adds 50% of the extra tax to each payment (s. 59A(4B)). Adjustments are made by repayment or further payment (s. 59A(5)).
- **Too much paid.** If both payments on account exceed this year's bill, the difference is repaid with repayment interest, or set against the next amount due (s. 59B(4); HMRC interest page).

## Deadlines and filing

| Event | 2025-26 bill | 2026-27 bill |
|---|---|---|
| First payment on account | 31 January 2026 | 31 January 2027 |
| Second payment on account | 31 July 2026 | 31 July 2027 |
| Return due online | 31 January 2027 | 31 January 2028 |
| Balancing payment (with the first payment on account for the next year) | 31 January 2027 | 31 January 2028 |

Sources: TMA 1970 ss. 59A(2) and 59B(4); [payments on account](https://www.gov.uk/understand-self-assessment-bill/payments-on-account).

- **31 January carries two payments.** The balancing payment for last year and the first payment on account for this year fall on the same day. A single large HMRC debit around 31 January is usually both. Split it before booking it.
- **Late notice to file.** If HMRC gave notice to file after 31 October and the person registered by 5 October, the balancing payment is due 3 months after the notice (s. 59B(3)). The payments on account dates do not move.
- **Weekends and holidays.** Interest runs from the due date even if it is not a business day (s. 86(3)). Payments not made by Faster Payments or card should reach HMRC by the last working day before.
- **Reducing payments: SA303.** If this year's bill will be lower, the person can claim, before 31 January after the year, that the payments be cut to 50% of a stated lower amount, or to nil (s. 59A(3), (4)). The claim states the grounds. It is made online ("Reduce payments on account" in the HMRC online account) or on form SA303 by post. HMRC repays or adjusts amounts already paid (s. 59A(5)).
- **A wrong claim costs interest.** If the bill turns out higher, interest runs from the original dates as if each payment had been the lower of (a) the reduced payment plus half the balancing payment and (b) the payment that was due before the claim (s. 86(4)-(5)). A fraudulent or negligent claim also carries a penalty up to the shortfall it caused (s. 59A(6)).
- **Making Tax Digital for Income Tax.** From 6 April 2026 sole traders and landlords with 2024-25 qualifying income over GBP 50,000 send quarterly updates through software (thresholds in the table above). The quarterly updates report figures; they do not collect tax. Payments on account stay on 31 January and 31 July, the base stays last year's bill, the year still ends with a return due 31 January, and SA303 claims still work.
- **Paying.** HMRC online account, bank transfer, card, Direct Debit, or a budget payment plan ahead of the date. Anyone who cannot pay should contact HMRC about a Time to Pay arrangement; interest still runs ([pay your Self Assessment bill](https://www.gov.uk/pay-self-assessment-tax-bill)).

## Penalties and interest

- **Interest on payments on account.** A late payment on account carries interest from its due date until paid (s. 86(1)(a), (2)). The rate is set under Finance Act 1989 s. 178: base rate plus 4% from 6 April 2025, 7.75% from 9 January 2026. It is simple interest, worked daily.
- **Interest after a claim to reduce.** See SA303 above (s. 86(4)-(6)). When the year ends in a repayment, interest on a payment on account is remitted except to the extent the payment due was more than half the final figure (s. 86(7)-(8)).
- **No penalty on a late payment on account.** Late payment penalties under FA 2009 Sch. 56 attach to the balancing payment under s. 59B(3) or (4) (Sch. 56 table, item 1), not to payments under s. 59A. HMRC's MTD penalty guidance says the same for the new regime: "Late payment penalties do not apply to any payments on account."
- **Late balancing payment, not in MTD.** 5% of the tax unpaid at 30 days, again at 6 months and again at 12 months, plus interest ([SA penalties](https://www.gov.uk/self-assessment-tax-returns/penalties)).
- **Late balancing payment, in MTD for Income Tax.** For 2026-27: nothing up to day 15; 3% of the tax owed at day 15 if paid between day 16 and day 30; a further 3% of the tax owed at day 30 if paid later, plus 10% a year charged daily from day 31 for up to 2 years. In the first year in the new regime there is no penalty if the tax is paid, or a payment plan agreed, within 30 days. For 2027-28 the two charges are 4% each ([MTD penalties](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax)).
- **Late filing** is a separate penalty regime (GBP 100 and upwards, or points under MTD). See `uk-income-tax-sa100`.
- **Interest and penalties are not deductible** against profits.

## Cross-border points

- **Non-residents and arrivals.** s. 59A has no residence condition. A non-resident who files a Self Assessment return (UK rent, UK trade) makes payments on account on the same tests. Tax deducted at source on UK income counts towards the 80% line. Residence rules are in `uk-statutory-residence-test`; the non-resident return in `uk-non-resident-sa109`.
- **Leaving the UK.** If UK income stops after departure, this year's bill is usually lower than last year's. A claim under s. 59A(3) or (4) cuts the payments. Without one, HMRC repays the excess after the return, which can be a year later.
- **Foreign tax.** Foreign tax credit relief reduces the UK tax assessed, so it reduces the base for next year's payments. Foreign tax is not UK "tax deducted at source" for the 80% test. See `uk-foreign-tax-and-withholding`.
- **Capital gains on a move.** Gains (including UK land disposals by non-residents) stay out of payments on account.

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

His balancing payment due 31 January 2028 is GBP 6,000 minus GBP 3,000 = GBP 3,000. Under s. 86(5), interest is worked out as if each payment on account had been the lower of GBP 1,500 plus half of GBP 3,000 (GBP 3,000) and the original GBP 5,000. That is GBP 3,000, so each payment was GBP 1,500 short. Interest at 7.75% runs on GBP 1,500 from 31 January 2027 to 31 January 2028 (365 days), GBP 116.25, and on GBP 1,500 from 31 July 2027 to 31 January 2028 (184 days), GBP 58.60. Total GBP 174.85, assuming the rate stays at 7.75% and he pays the balance on 31 January 2028. No penalty applies to the shortfall on the payments on account.

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

## Ask the client first

1. What was last year's Self Assessment bill, and how much of the tax was collected at source (PAYE, coding out, tax on interest)? This sets both tests.
2. Was last year's figure inflated by capital gains tax, student loan or voluntary Class 2? These come out of the base.
3. Will this year's income be lower than last year's, and why? This decides whether a reduction claim is worth the interest risk.
4. Has last year's return been filed, amended or reopened by HMRC since the payments were set?
5. Are they inside Making Tax Digital for Income Tax for 2026-27? This decides which late payment penalty regime applies to the balancing payment.
6. Are they leaving or arriving in the UK this year, or is this their first Self Assessment year?

## Sources

| Source | URL | Read on |
|---|---|---|
| Taxes Management Act 1970 s. 59A (payments on account) | https://www.legislation.gov.uk/ukpga/1970/9/section/59A | 2026-10-26 |
| Taxes Management Act 1970 s. 59B (balancing payment) | https://www.legislation.gov.uk/ukpga/1970/9/section/59B | 2026-10-24 |
| Taxes Management Act 1970 s. 86 (interest) | https://www.legislation.gov.uk/ukpga/1970/9/section/86 | 2026-10-26 |
| Income Tax (Payments on Account) Regulations 1996, reg 3 | https://www.legislation.gov.uk/uksi/1996/1654/regulation/3 | 2026-10-26 |
| Income Tax (Payments on Account) Regulations 1996, reg 4 | https://www.legislation.gov.uk/uksi/1996/1654/regulation/4 | 2026-10-26 |
| Income Tax (Payments on Account) (Amendment) Regulations 1997 (four to five) | https://www.legislation.gov.uk/uksi/1997/2491/made | 2026-10-26 |
| Income Tax (Payments on Account) (Amendment) Regulations 2008 (GBP 500 to GBP 1,000) | https://www.legislation.gov.uk/uksi/2008/838/made | 2026-10-26 |
| Finance Act 2009 Sch. 56 (late payment penalties) | https://www.legislation.gov.uk/ukpga/2009/10/schedule/56 | 2026-10-24 |
| GOV.UK, Understand your Self Assessment bill: payments on account | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-10-26 |
| HMRC Self Assessment Manual SAM121665 (Class 2 not in payments on account) | https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam121665 | 2026-10-26 |
| GOV.UK, Pay your Self Assessment bill through your tax code | https://www.gov.uk/pay-self-assessment-tax-bill/through-your-tax-code | 2026-10-26 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-24 |
| Bank of England, Bank Rate | https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate | 2026-10-24 |
| GOV.UK, Self Assessment penalties | https://www.gov.uk/self-assessment-tax-returns/penalties | 2026-10-24 |
| GOV.UK, Penalties for Making Tax Digital for Income Tax | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax | 2026-10-26 |
| GOV.UK, Find out if and when you need to use Making Tax Digital for Income Tax | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax | 2026-10-24 |

Not yet confirmed: whether late payment interest for taxpayers inside Making Tax Digital for Income Tax moves from TMA 1970 s. 86 to the Finance Act 2021 Sch. 29 interest rules from 2026-27 (HMRC's MTD page says late payment interest is charged from the first day, but the commencement order was not read); the Bank Rate after the 5 November 2026 decision; the online payment plan limit for Self Assessment debts; and the treatment of foreign tax credit relief in the s. 59A assessed amount (stated from the structure of s. 59A(1), not from an HMRC page). Carried from v3.2: the bank statement pattern library (now the 31 January note under Deadlines) and the refusal list (now the out of scope lines under Who this applies to).

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
