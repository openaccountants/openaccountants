---
name: uk-payments-on-account
description: "Use this skill whenever asked about UK Payments on Account (POA) for Self Assessment taxpayers. Trigger on phrases like \"payments on account\", \"POA\", \"POA 2026\", \"January payment\", \"July payment\", \"balancing payment\", \"SA303\", \"claim to reduce\", \"reduce payments on account\", \"do I need to make payments on account\", \"POA threshold\", \"tax underpayment\", \"MTD ITSA payments on account\", or any question about advance income tax payments under UK Self Assessment. Covers the two-payment schedule (31 January / 31 July), the GBP 1,000 threshold, the 80% PAYE test, balancing payment mechanics, SA303 claim to reduce, excluded items (voluntary Class 2 NIC, student loan, CGT), interest on late payments, the interaction with MTD ITSA quarterly updates from 6 April 2026, and interaction with tax codes. ALWAYS read this skill before touching any UK POA work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uk-payments-on-account"
  jurisdiction: "GB"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# UK Payments On Account

## UK Payments on Account (POA) -- Self Assessment Skill v3.2

## Rates and thresholds, 2026/27 (6 April 2026 to 5 April 2027)

> Source-cited draft: not reviewed by an accountant.

### Payments on account for 2026/27

- **De minimis**: prior year (2025/26) SA balance under £1,000 means no POA  _(TMA 1970 s.59A(1)(c); Income Tax (Payments on Account) Regulations 1996 reg 3, £500 raised to £1,000 by SI 2008/838 from 2009-10)_
- **Tax deducted at source**: if more than 80% of last year's tax was collected outside Self Assessment (PAYE, tax deducted at source), no POA  _(TMA 1970 s.59A(1)(d); SI 1996/1654 reg 4; https://www.gov.uk/understand-self-assessment-bill/payments-on-account)_
- **1st POA for 2026/27**: 31 January 2027, 50% of the 2025/26 SA balance  _(TMA 1970 s.59A(2))_
- **2nd POA for 2026/27**: 31 July 2027, 50%  _(TMA 1970 s.59A(2))_
- **Balancing payment for 2026/27**: 31 January 2028  _(TMA 1970 s.59B)_
- **Not in the POA base**: student loan and postgraduate loan repayments, capital gains tax, voluntary Class 2 NIC; these are paid with the balancing payment  _(https://www.gov.uk/understand-self-assessment-bill/payments-on-account; Class 2: HMRC Self Assessment Manual SAM121665)_
- **Late payment interest**: Bank of England base rate + 4% from 6 April 2025 (was + 2.5% before); 7.75% from 9 January 2026  _(https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates)_
- **Type**: simple interest (not compound)  _(TMA 1970 s.86)_
- **Making Tax Digital for Income Tax**: from 6 April 2026 if 2024/25 qualifying income was over £50,000; from 6 April 2027 over £30,000 (2025/26); from 6 April 2028 over £20,000 (2026/27). POA dates do not change  _(https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax)_

## Section 1 -- Quick reference

**Section 1 Quick reference table**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Tax | Income tax advance payments (Payments on Account / POA) |
| Primary legislation | Taxes Management Act 1970 (TMA 1970), Section 59A; Income Tax (Payments on Account) Regulations 1996 (SI 1996/1654) regs 3 and 4 |
| Supporting legislation | Income Tax (Pay As You Earn) Regulations 2003; Finance Act 2024; Finance (No. 2) Act 2024; TMA 1970 s59B, s86 |
| Authority | HM Revenue & Customs (HMRC) |
| Portal | HMRC Self Assessment Online; from 6 April 2026 also MTD ITSA-compatible software for quarterly updates |
| Currency | GBP only |
| Payment schedule | Two POAs: 31 January (in tax year) + 31 July (after tax year); balancing payment 31 January following |
| Threshold | SA balance >= GBP 1,000 AND tax deducted at source < 80% of total tax |
| Excluded items | Voluntary Class 2 NIC, student loan, postgraduate loan, CGT |
| Status | Source-cited draft: not reviewed by an accountant |

### 1.1 Three-year comparison: variable elements

The POA structural rules (threshold, 50%-of-prior-year formula, two-instalment schedule, SA303 mechanism, excluded items) are UNCHANGED across all three years. Only the late payment interest rate and the surrounding reporting workflow shift.

**Three-year comparison table**  _(https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates)_

| Element | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| Threshold (de minimis) | Prior year SA balance >= GBP 1,000 | Prior year SA balance >= GBP 1,000 | Prior year SA balance >= GBP 1,000 |
| Threshold (PAYE/deduction test) | < 80% of tax deducted at source | < 80% of tax deducted at source | < 80% of tax deducted at source |
| POA calculation | 50% of prior year SA balance, each instalment | 50% of prior year SA balance, each instalment | 50% of prior year SA balance, each instalment |
| 1st POA due | 31 January 2025 | 31 January 2026 | 31 January 2027 |
| 2nd POA due | 31 July 2025 | 31 July 2026 | 31 July 2027 |
| Balancing payment due | 31 January 2026 | 31 January 2027 | 31 January 2028 |
| Late payment interest rate | HMRC Bank Rate + 2.5 pp on or before 5 April 2025; Bank Rate + 4 pp from 6 April 2025 | HMRC Bank Rate + 4 pp (track Bank Rate movements) | HMRC Bank Rate + 4 pp (track Bank Rate movements) |
| SA303 (claim to reduce) | Available; standard process | Available; standard process | Available; standard process |
| MTD ITSA quarterly reporting | Not in scope | Not in scope | Required from 6 April 2026 where 2024/25 qualifying income (self-employment plus property) was over GBP 50,000 (does NOT replace POA) |
| Annual reconciliation | SA tax return | SA tax return | SA tax return / Final Declaration under MTD ITSA |

**Note on the 4 pp surcharge.** The late payment interest add-on increased from 2.5 pp to 4 pp from 6 April 2025 (it was plus 2.5% on or before 5 April 2025). All worked examples in this version use Bank Rate + 4 pp.

**Payment schedule summary (illustrative for 2025-26 tax year)**

| Payment | Due date | Amount |
| --- | --- | --- |
| 1st POA | 31 January 2026 | 50% of 2024-25 SA balance |
| 2nd POA | 31 July 2026 | 50% of 2024-25 SA balance |
| Balancing payment | 31 January 2027 | Actual 2025-26 liability minus POAs paid |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| SA balance uncertain | Pay full POA -- do not reduce without SA303 |
| Prior year return not yet filed | Use last known SA balance; flag for reviewer |
| CGT included in SA balance | Exclude CGT before computing POA |
| Student loan included | Exclude before computing POA |
| HMRC coding out unclear | Verify coded amount removed from SA balance |
| MTD ITSA from April 2026 | Confirm scope and software; POA cycle still applies in parallel |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- prior year Self Assessment tax return showing total tax/Class 4 NIC liability, tax deducted at source, and any excluded items.

**Recommended** -- the HMRC statement or tax calculation showing the SA balance, any SA303 filing history, current year income expectations.

**Ideal** -- the full SA302 tax calculation from HMRC, prior year payment history, any coding adjustment letters, and (from April 2026) the MTD ITSA quarterly update submissions to date.

- **Refusal policy if minimum is missing**: SOFT WARN. If the prior year SA balance is unknown, flag that POA computation is unreliable and direct the client to obtain their SA302 from HMRC.

### Refusal catalogue

- **R-UK-POA-1 -- Partnerships with complex profit-sharing**: Trigger: client is in a partnership with non-standard profit-sharing ratios. Message: "Partnership POA allocation requires partner-level analysis. Please escalate to a qualified accountant."
- **R-UK-POA-2 -- Non-resident POA obligations**: Trigger: client is non-UK resident. Message: "Non-resident Self Assessment has different POA rules. Please escalate to a qualified accountant."
- **R-UK-POA-3 -- Trust POA**: Trigger: client asks about trust payments on account. Message: "Trust estimated tax is outside the scope of this skill."
- **R-UK-POA-4 -- MTD ITSA software selection / quarterly update preparation**: Trigger: client asks which MTD ITSA software to use, or how to file a quarterly update. Message: "MTD ITSA software selection and quarterly update mechanics are outside the scope of this POA skill. Please use the dedicated MTD ITSA skill or escalate to a qualified accountant."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a POA payment.

### 3.1 HMRC Self Assessment debits

**HMRC Self Assessment debits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HMRC, HM REVENUE, HMRC SELF ASSESSMENT | POA payment | Match with January/July timing |
| HMRC CUMBERNAULD, HMRC SHIPLEY | POA payment | HMRC processing centres |
| SELF ASSESSMENT, SA PAYMENT | POA payment | Explicit description |
| PAYMENT ON ACCOUNT, POA | POA payment | Self-identified |

### 3.2 Timing-based identification

**Timing-based identification table**

| Debit date range | Likely payment | Confidence |
| --- | --- | --- |
| 15 January -- 5 February | 1st POA + prior year balancing payment | High if payee is HMRC |
| 15 July -- 5 August | 2nd POA | High if payee is HMRC |
| Any other date to HMRC SA | Late payment, voluntary payment, or balancing | Flag for reviewer |

### 3.3 Related but NOT POA payments

**Related but NOT POA payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HMRC VAT | EXCLUDE from POA | VAT payment |
| HMRC PAYE, HMRC RTI | EXCLUDE from POA | Employer PAYE payment |
| HMRC NIC, CLASS 2 | EXCLUDE from POA | NIC direct collection |
| STUDENT LOAN, SLC | EXCLUDE from POA | Student loan repayment |
| HMRC CGT, CAPITAL GAINS | EXCLUDE from POA | CGT payment (separate regime) |
| HMRC PENALTY, HMRC INTEREST | EXCLUDE from POA | Penalty/interest charge |

### 3.4 January double-payment identification

31 January is a critical date where multiple payments coincide. A single large HMRC debit on or near 31 January likely includes:
- Balancing payment for the prior year
- 1st POA for the current year

If the total debit is substantially larger than one POA instalment, it is likely the combined payment. Flag for reviewer to split.

## Section 4 -- Worked examples

### Example 1 -- Standard POA computation

**Input:** Prior year SA balance = GBP 6,000. No excluded items.

**Computation:** Each POA = GBP 6,000 / 2 = GBP 3,000.

**Example 1 payment table**

| Payment | Due date | Amount |
| --- | --- | --- |
| 1st POA | 31 January 2025 | GBP 3,000 |
| 2nd POA | 31 July 2025 | GBP 3,000 |

### Example 2 -- Below GBP 1,000 threshold

**Input:** Prior year SA balance = GBP 850.

**Output:** Below GBP 1,000 threshold. No POAs required. Full GBP 850 due as balancing payment on 31 January following the tax year.

### Example 3 -- 80% deduction-at-source test met

**Input:** Total tax liability = GBP 20,000. PAYE/tax deducted at source = GBP 17,000. SA balance = GBP 3,000.

**Computation:** Deducted-at-source % = 17,000 / 20,000 = 85% > 80%. No POA required despite SA balance exceeding GBP 1,000.

### Example 4 -- Excluded items removed

**Input:** Prior year (2025/26) SA: income tax and Class 4 via SA = GBP 4,000, CGT = GBP 3,000, voluntary Class 2 NIC = GBP 182 (52 weeks x GBP 3.50), student loan = GBP 1,200. Total amount due = GBP 8,382.

**Computation:** POA basis = GBP 4,000 only (CGT, Class 2, student loan excluded). Each POA for 2026/27 = GBP 2,000, due 31 January 2027 and 31 July 2027.

```oa-check
name: POA base with excluded items removed (2026/27 POAs)
inputs:
  income_tax_and_class4: 4000
  cgt: 3000
  weekly_class2: 3.50
  weeks: 52
  student_loan: 1200
steps:
  - class2: weekly_class2 * weeks
  - total_due: income_tax_and_class4 + cgt + class2 + student_loan
  - poa_base: income_tax_and_class4
  - each_poa: poa_base / 2
expected:
  class2: 182.00
  total_due: 8382.00
  each_poa: 2000.00
```

### Example 5 -- SA303 reduction

**Input:** Standard POA = GBP 5,000 each. Client expects current year SA balance = GBP 3,000. SA303 filed.

**Output:** Reduced POA = GBP 1,500 each. If the actual SA balance = GBP 6,000, each POA is treated for interest as the lower of the original POA (GBP 5,000) and the reduced POA plus half the balancing amount (GBP 1,500 + 50% x GBP 3,000 = GBP 3,000). HMRC charges interest on a GBP 1,500 shortfall per instalment from the original due dates (TMA 1970 s.86(4)-(6)).

```oa-check
name: Interest base after an SA303 reduction (TMA 1970 s.86(5))
inputs:
  original_poa: 5000
  reduced_poa: 1500
  actual_balance: 6000
steps:
  - balancing: actual_balance - 2 * reduced_poa
  - deemed_poa: min(original_poa, reduced_poa + balancing / 2)
  - shortfall_each: deemed_poa - reduced_poa
expected:
  balancing: 3000.00
  deemed_poa: 3000.00
  shortfall_each: 1500.00
```

### Example 6 -- Late payment interest (Bank Rate + 4 pp)

**Input:** 1st POA of GBP 3,000 due 31 January 2026. Paid 15 April 2026 (74 days late). HMRC Bank Rate = 3.75% (illustrative).

**Computation:** Interest rate = 3.75% + 4.00% = 7.75% (the HMRC late payment rate from 9 January 2026). Interest = GBP 3,000 x 7.75% / 365 x 74 = GBP 47.14.

```oa-check
name: Late payment interest on a 3,000 POA paid 74 days late at 7.75%
inputs:
  overdue: 3000
  rate_pct: 7.75
  days: 74
steps:
  - interest: round(overdue * rate_pct / 100 / 365 * days, 2)
expected:
  interest: 47.14
```

### Example 7 -- Full 3-year cycle (the headline worked example)

**Client profile:** Self-employed software contractor. No PAYE income. No CGT, no student loan, no Class 2 NIC adjustments in scope. Prior year (2023-24) SA balance fell below GBP 1,000, so 2024-25 had NO opening POAs.

**Step A -- Tax year 2024-25 (filed January 2026).**

The client's 2024-25 SA return shows an SA balance of GBP 12,000 (income tax + Class 4 NIC). No POAs were due in advance (because 2023-24 was below threshold).

Payments due on the 31 January 2026 deadline:
- Balancing payment for 2024-25: GBP 12,000
- 1st POA for 2025-26: GBP 6,000 (= 50% of GBP 12,000)
- Total cash due on 31 January 2026: **GBP 18,000**

**Step A payment table**

| Payment | Due date | Amount |
| --- | --- | --- |
| 2024-25 balancing payment | 31 January 2026 | GBP 12,000 |
| 1st POA for 2025-26 | 31 January 2026 | GBP 6,000 |
| 2nd POA for 2025-26 | 31 July 2026 | GBP 6,000 |

**Step B -- Tax year 2025-26 (POAs of GBP 6,000 each already in motion).**

By 31 July 2026 the client has paid GBP 12,000 in POAs (GBP 6,000 + GBP 6,000) toward the 2025-26 liability.

Three scenarios on the actual 2025-26 liability:

**Scenario B1 -- Liability exactly matches.** Actual 2025-26 SA balance = GBP 12,000.
- POAs paid: GBP 12,000.
- Balancing payment 31 January 2027: GBP 0.
- 1st POA for 2026-27 due 31 January 2027: GBP 6,000 (= 50% of GBP 12,000).
- Cash due 31 January 2027: **GBP 6,000**.

**Scenario B2 -- Liability higher.** Actual 2025-26 SA balance = GBP 14,000.
- POAs paid: GBP 12,000.
- Balancing payment 31 January 2027: GBP 2,000.
- 1st POA for 2026-27: GBP 7,000 (= 50% of GBP 14,000).
- Cash due 31 January 2027: **GBP 9,000**.
- 2nd POA for 2026-27 due 31 July 2027: GBP 7,000.

**Scenario B3 -- Liability lower (refund position).** Actual 2025-26 SA balance = GBP 8,000.
- POAs paid: GBP 12,000.
- Overpayment: GBP 4,000 (HMRC refunds or sets off against 2026-27).
- 1st POA for 2026-27: GBP 4,000 (= 50% of GBP 8,000).
- If HMRC sets off the overpayment: cash due 31 January 2027 = GBP 0; the GBP 4,000 overpayment covers the 1st POA for 2026-27 entirely.

**Step C -- Tax year 2026-27 (the first year inside MTD ITSA scope, see Section 4.1).**

Assume Scenario B1 (POAs of GBP 6,000 each for 2026-27). The client is in MTD ITSA from 6 April 2026 and submits quarterly updates through compatible software, but the POA cash flow is unchanged:

**Step C event table**  _(https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates)_

| Date | Event | Cash impact |
| --- | --- | --- |
| 31 January 2027 | 1st POA 2026-27 + (any) 2025-26 balancing | GBP 6,000 (B1) |
| 7 August 2026 | Q1 MTD ITSA quarterly update due | No tax payment -- reporting only |
| 7 November 2026 | Q2 MTD ITSA quarterly update due | No tax payment -- reporting only |
| 7 February 2027 | Q3 MTD ITSA quarterly update due | No tax payment -- reporting only |
| 7 May 2027 | Q4 MTD ITSA quarterly update due | No tax payment -- reporting only |
| 31 July 2027 | 2nd POA 2026-27 | GBP 6,000 |
| 31 January 2028 | Final Declaration (replaces SA return) + 2026-27 balancing payment + 1st POA 2027-28 | Depends on final 2026-27 liability |

The four quarterly updates are reporting events only -- they do NOT generate new payment dates. POA cash flow continues unchanged.

### 4.1 From April 2026 -- MTD ITSA interaction

- **Headline rule**: Making Tax Digital for Income Tax applies from 6 April 2026 to sole traders and landlords whose 2024/25 qualifying income was over GBP 50,000; from 6 April 2027 where 2025/26 qualifying income was over GBP 30,000; and from 6 April 2028 where 2026/27 qualifying income was over GBP 20,000 (GOV.UK eligibility guidance, read 2026-10-23).

**MTD ITSA does NOT replace or alter the POA regime.** Specifically:

1. **POA dates remain 31 January and 31 July.** MTD quarterly updates (due 7 August, 7 November, 7 February, 7 May for a standard 6 April -- 5 April year) are SEPARATE reporting events. They do not collect tax.
2. **POA calculation remains 50% of prior year SA balance.** It does not switch to a quarterly profit-to-date basis.
3. **The annual reconciliation continues -- now called the Final Declaration.** This replaces the SA100 tax return for MTD-scope taxpayers and is due 31 January following the tax year, same as before. Balancing payment is due on the same 31 January date.
4. **SA303 (claim to reduce POAs) remains available.** The mechanism is unchanged.
5. **Excluded items continue to be excluded** (voluntary Class 2 NIC, student loan, CGT).

**Workflow change for the practitioner.** The data feeds underpinning the SA balance now flow through MTD-compatible software in quarterly batches. The POA worksheet (the part this skill produces) consumes the same SA balance figure from the prior year's Final Declaration that it previously consumed from the prior year SA return.

**Common client misconception to correct.** Clients in MTD ITSA from April 2026 often assume the quarterly updates settle their tax. They do not. The 31 January / 31 July POA pattern continues, and the Final Declaration is still required.

## Section 5 -- Computation rules

### 5.1 Threshold tests

- **Threshold tests**: POAs are NOT required if EITHER condition is met: - **Test 1 (de minimis):** Prior year SA balance < GBP 1,000 - **Test 2 (deduction dominance):** More than 80% of prior year total tax was collected via PAYE/deduction at source

### 5.2 SA balance definition

- **SA balance formula**: SA_balance = total_income_tax_and_class4_NIC - tax_deducted_at_source
- **Exclusions**: EXCLUDE from SA balance: voluntary Class 2 NIC, student loan repayments, postgraduate loan repayments, capital gains tax. Marriage allowance is not an exclusion: it changes the income tax figure itself (see EC10).

### 5.3 POA computation

- **POA computation formula**: each_POA = SA_balance / 2

### 5.4 Balancing payment

- **Balancing payment formula**: balancing_payment = actual_tax_liability - POA_1 - POA_2
- **Excluded items in balancing payment**: The balancing payment includes all excluded items (voluntary Class 2 NIC, student loan, postgraduate loan, CGT) -- these are payable in full with the balancing payment.

### 5.5 SA303 claim to reduce

- **SA303 claim to reduce**: A taxpayer expecting lower current year income may file SA303 to reduce POAs to any amount including GBP 0. Risk: if the reduction is too aggressive, HMRC charges interest on the shortfall from the ORIGINAL due dates.
- **Reduced POA formula**: reduced_POA_each = estimated_current_year_SA_balance / 2

## Section 6 -- Penalties and interest

### 6.1 Late payment interest

**Late payment interest table**  _(https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates)_

| Element | Rule |
| --- | --- |
| Rate | Bank of England base rate + 4 percentage points (from 6 April 2025). 7.75% from 9 January 2026 (current on the HMRC page read 2026-10-23). |
| Runs from | Due date of the POA (31 Jan or 31 Jul) |
| Runs until | Date of payment |
| Compounding | Simple interest (not compound) |
| Tax deductibility | NOT tax deductible |

### 6.2 Interest computation

- **Interest computation formula**: interest = overdue_amount x (Bank_Rate + 4%) / 365 x days_overdue

There is no separate penalty for late POA payment -- only interest. Outside Making Tax Digital, a late payment penalty of 5% applies if the balancing payment is more than 30 days late, with further 5% charges at 6 and 12 months. If you are using Making Tax Digital for Income Tax, new late payment penalties replace this from the tax year you join, and they do not apply to payments on account. For 2026/27 they are: nothing up to 15 days; 3% of the tax owed at day 15 (no penalty at this point in your first year); a further 3% at day 30; then 10% a year from day 31. For 2027/28 the two charges are 4% each (https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax).

### 6.3 Time-to-Pay arrangements

- **Time-to-Pay (TTP) arrangements**: A taxpayer who cannot pay on time can ask HMRC for a payment plan (Time to Pay) (https://www.gov.uk/pay-self-assessment-tax-bill). Late payment interest still runs. Under Making Tax Digital for Income Tax, if a plan is agreed and kept, late payment penalties are paused from the date the taxpayer contacted HMRC (https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax).

## Section 7 -- Interaction with tax codes and PAYE

- **coding out**: When HMRC collects SA underpayments via a PAYE tax code (coding out), this reduces the SA balance and therefore reduces POAs for the following year. Coding out is only available if you owe less than GBP 3,000 on your tax bill (you cannot make a part payment to meet this threshold) and you already pay tax through PAYE. If HMRC is coding out underpayments, verify whether the coded amount has been correctly removed from the SA balance before computing POAs.  _(https://www.gov.uk/pay-self-assessment-tax-bill/through-your-tax-code)_

## Section 8 -- Edge cases

**EC1 -- First year of Self Assessment.** No prior year return. No POAs in the first year. All tax due as a single balancing payment. POAs begin from the second year.

**EC2 -- SA303 reduction to zero, then income increases.** Balancing payment of full amount due 31 January. HMRC charges interest on the shortfall from each original POA due date.

**EC3 -- Employment plus self-employment.** Employee with a side trade. Total income tax and Class 4 GBP 18,000, of which GBP 14,000 deducted through PAYE. PAYE% = 77.8% < 80%. POAs apply. SA balance = GBP 4,000, each POA = GBP 2,000.

**EC4 -- Prior year SA balance just below GBP 1,000.** GBP 980. No POAs required. Full amount due as balancing payment.

**EC5 -- Client stops trading mid-year.** May file SA303 to reduce. Overpayment refunded with balancing payment.

**EC6 -- Prior year included one-off capital gain.** CGT excluded from POA calculation. If HMRC set POAs at the higher amount, file SA303 to correct.

**EC7 -- Student loan pushed SA balance above GBP 1,000.** Student loan excluded. SA balance for POA test = income tax via SA only. If that is below GBP 1,000, no POAs.

**EC8 -- 31 January falls on a weekend.** Make sure your payment reaches HMRC on the last working day before (unless you are paying by Faster Payments or by debit or credit card).

**EC9 -- HMRC amendment reduces prior year liability.** HMRC should adjust POAs automatically. If not, file SA303 referencing the amendment.

**EC10 -- Marriage allowance transfer.** Reduces transferor's tax, increases recipient's. POAs based on NET SA balance after marriage allowance.

**EC11 -- Client enters MTD ITSA from 6 April 2026 mid-POA-cycle.** Existing 2025-26 POAs (due 31 Jan 2026 and 31 July 2026) are unchanged. From 6 April 2026 the client begins quarterly updates for the 2026-27 tax year. The 31 January 2027 cash event still combines the 2025-26 balancing payment (computed via Final Declaration or SA100 depending on scope) with the 1st POA for 2026-27.

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Both threshold tests checked (GBP 1,000 and 80% deduction at source)
- [ ] Voluntary Class 2 NIC, student loan, CGT, postgraduate loan excluded from SA balance
- [ ] POA computed as 50% of SA balance (not 50% of total tax)
- [ ] 31 January double-payment impact noted (balancing + 1st POA)
- [ ] SA303 interest risk flagged if reduction is recommended
- [ ] Prior year return status confirmed
- [ ] Coding out adjustments verified if applicable
- [ ] Weekend/holiday due date adjustments checked
- [ ] Balancing payment includes all excluded items
- [ ] Late payment interest computed at Bank Rate + 4 pp (not the old + 2.5 pp)
- [ ] If the year is 2026-27 or later, MTD ITSA scope confirmed and client reminded that POAs continue alongside quarterly updates
- [ ] Output labelled as estimated until prior year return is filed and processed

## Section 10 -- Test suite

### Test 1 -- Standard POA computation

**Input:** Prior year SA balance = GBP 6,000.
**Expected:** Each POA = GBP 3,000. 1st due 31 Jan, 2nd due 31 Jul.

### Test 2 -- Below GBP 1,000 threshold

**Input:** Prior year SA balance = GBP 850.
**Expected:** No POA. Full GBP 850 due as balancing payment.

### Test 3 -- 80% deduction test met

**Input:** Total tax = GBP 20,000. PAYE = GBP 17,000. SA balance = GBP 3,000.
**Expected:** PAYE% = 85% > 80%. No POA required.

### Test 4 -- Excluded items removed

**Input:** Income tax via SA = GBP 4,000, CGT = GBP 3,000, voluntary Class 2 = GBP 182, student loan = GBP 1,200.
**Expected:** POA basis = GBP 4,000. Each POA = GBP 2,000.

### Test 5 -- SA303 reduction

**Input:** Standard POA = GBP 5,000 each. Estimated current year = GBP 3,000. SA303 filed.
**Expected:** Reduced POA = GBP 1,500 each. Interest risk flagged.

### Test 6 -- Balancing payment with overpayment

**Input:** POAs paid GBP 4,000 + GBP 4,000. Actual SA balance = GBP 6,500.
**Expected:** Overpayment = GBP 1,500. HMRC refunds or sets off.

### Test 7 -- Late payment interest (Bank Rate + 4 pp)

**Input:** POA GBP 3,000 due 31 Jan 2026. Paid 15 Apr 2026 (74 days). Bank Rate 3.75%.
**Expected:** Rate = 7.75%. Interest = GBP 3,000 x 7.75% / 365 x 74 = GBP 47.14.

### Test 8 -- Full 3-year cycle, B1 scenario

**Input:** 2024-25 SA balance = GBP 12,000; 2025-26 actual = GBP 12,000; 2026-27 actual = GBP 12,000. No prior POAs entering 2024-25.
**Expected:**
- 31 Jan 2026 cash: GBP 18,000 (12,000 balancing + 6,000 1st POA).
- 31 Jul 2026 cash: GBP 6,000 (2nd POA).
- 31 Jan 2027 cash: GBP 6,000 (1st POA 2026-27; 2025-26 balancing = 0).
- 31 Jul 2027 cash: GBP 6,000 (2nd POA 2026-27).
- 31 Jan 2028 cash: GBP 6,000 (1st POA 2027-28; 2026-27 balancing = 0).

### Test 9 -- MTD ITSA does not change POA cash flow

**Input:** Client in MTD ITSA from 6 April 2026 with prior year SA balance = GBP 10,000.
**Expected:** 1st POA for 2026-27 = GBP 5,000 due 31 Jan 2027; 2nd POA = GBP 5,000 due 31 Jul 2027; quarterly updates do not generate tax payments.

## Prohibitions

- NEVER include voluntary Class 2 NIC, student loan, postgraduate loan, or CGT in the POA calculation
- NEVER compute POAs without checking both threshold tests (GBP 1,000 and 80% deduction at source)
- NEVER advise filing SA303 without flagging the interest risk on shortfalls
- NEVER use current year income to compute POAs -- always prior year SA balance
- NEVER ignore the 31 January double-payment impact (balancing + 1st POA)
- NEVER present POA figures as definitive until the prior year return is filed and processed
- NEVER assume HMRC has automatically adjusted POAs after a return amendment
- NEVER conflate POA interest (simple, Bank Rate + 4 pp) with late filing penalties (separate regime)
- NEVER use the legacy +2.5 pp interest add-on for periods of lateness running from 6 April 2025 onwards -- the rate is Bank Rate + 4 pp
- NEVER tell a client that MTD ITSA quarterly updates replace POAs -- they do not
- NEVER advise on penalty disputes without escalating to a qualified accountant

## Sources

| Source | URL | Read on |
|---|---|---|
| TMA 1970 s.59A (payments on account) | https://www.legislation.gov.uk/ukpga/1970/9/section/59A | 2026-10-23 |
| Income Tax (Payments on Account) Regulations 1996 reg 3 (amount) | https://www.legislation.gov.uk/uksi/1996/1654/regulation/3 | 2026-10-23 |
| Income Tax (Payments on Account) Regulations 1996 reg 4 (proportion) | https://www.legislation.gov.uk/uksi/1996/1654/regulation/4 | 2026-10-23 |
| Income Tax (Payments on Account) (Amendment) Regulations 2008 (GBP 500 to GBP 1,000) | https://www.legislation.gov.uk/uksi/2008/838/made | 2026-10-23 |
| GOV.UK, Understand your Self Assessment tax bill: payments on account | https://www.gov.uk/understand-self-assessment-bill/payments-on-account | 2026-10-23 |
| HMRC interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-23 |
| GOV.UK, Find out if and when you need to use Making Tax Digital for Income Tax | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax | 2026-10-23 |
| GOV.UK, Send quarterly updates (MTD for Income Tax) | https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates | 2026-10-23 |
| GOV.UK, Penalties for Making Tax Digital for Income Tax | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax | 2026-10-23 |
| GOV.UK, Self-employed National Insurance rates (voluntary Class 2) | https://www.gov.uk/self-employed-national-insurance-rates | 2026-10-23 |
| GOV.UK, Pay your Self Assessment bill through your tax code | https://www.gov.uk/pay-self-assessment-tax-bill/through-your-tax-code | 2026-10-23 |
| TMA 1970 s.86 (interest after a claim to reduce, s.86(4)-(6)) | https://www.legislation.gov.uk/ukpga/1970/9/section/86 | 2026-10-23 |
| HMRC Self Assessment Manual SAM121665 (Class 2 not in payments on account) | https://www.gov.uk/hmrc-internal-manuals/self-assessment-manual/sam121665 | 2026-10-23 |

Not yet confirmed: the Bank of England base rate after 9 January 2026 (the HMRC page read today still shows 7.75% as current); the online payment plan limit for Self Assessment debts (removed from section 6.3; not found on the GOV.UK pages read today).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uk-payments-on-account` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uk-payments-on-account. If neither is available, confirm every figure against the official source pages cited above before relying on it.
