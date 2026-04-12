---
name: uk-payments-on-account
description: >
  Use this skill whenever asked about UK Payments on Account (POA) for Self Assessment taxpayers. Trigger on phrases like "payments on account", "POA", "January payment", "July payment", "balancing payment", "SA303", "claim to reduce", "reduce payments on account", "do I need to make payments on account", "POA threshold", "tax underpayment", or any question about advance income tax payments under UK Self Assessment. Covers the two-payment schedule (31 January / 31 July), the GBP 1,000 threshold, the 80% PAYE test, balancing payment mechanics, SA303 claim to reduce, excluded items (Class 2 NIC, student loan, CGT), interest on late payments, and interaction with tax codes. ALWAYS read this skill before touching any UK POA work.
version: 2.0
jurisdiction: GB
tax_year: 2024-25
category: international
depends_on:
  - income-tax-workflow-base
---

# UK Payments on Account (POA) -- Self Assessment Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | United Kingdom |
| Tax | Income tax advance payments (Payments on Account / POA) |
| Primary legislation | Taxes Management Act 1970 (TMA 1970), Section 59A |
| Supporting legislation | Income Tax (Pay As You Earn) Regulations 2003; Finance Act 2024; TMA 1970 s59B, s86 |
| Authority | HM Revenue & Customs (HMRC) |
| Portal | HMRC Self Assessment Online |
| Currency | GBP only |
| Payment schedule | Two POAs: 31 January (in tax year) + 31 July (after tax year); balancing payment 31 January following |
| Threshold | SA balance >= GBP 1,000 AND PAYE < 80% of total tax |
| Excluded items | Class 2 NIC, student loan, postgraduate loan, CGT, marriage allowance |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by UK-qualified accountant (ACA/ACCA/CTA) |
| Validation date | Pending |

**Payment schedule summary (tax year 2024/25):**

| Payment | Due date | Amount |
|---|---|---|
| 1st POA | 31 January 2025 | 50% of prior year SA balance |
| 2nd POA | 31 July 2025 | 50% of prior year SA balance |
| Balancing payment | 31 January 2026 | Actual liability minus POAs paid |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| SA balance uncertain | Pay full POA -- do not reduce without SA303 |
| Prior year return not yet filed | Use last known SA balance; flag for reviewer |
| CGT included in SA balance | Exclude CGT before computing POA |
| Student loan included | Exclude before computing POA |
| HMRC coding out unclear | Verify coded amount removed from SA balance |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- prior year Self Assessment tax return showing total tax/Class 4 NIC liability, tax deducted at source, and any excluded items.

**Recommended** -- the HMRC statement or tax calculation showing the SA balance, any SA303 filing history, current year income expectations.

**Ideal** -- the full SA302 tax calculation from HMRC, prior year payment history, and any coding adjustment letters.

**Refusal policy if minimum is missing -- SOFT WARN.** If the prior year SA balance is unknown, flag that POA computation is unreliable and direct the client to obtain their SA302 from HMRC.

### Refusal catalogue

**R-UK-POA-1 -- Partnerships with complex profit-sharing.** Trigger: client is in a partnership with non-standard profit-sharing ratios. Message: "Partnership POA allocation requires partner-level analysis. Please escalate to a qualified accountant."

**R-UK-POA-2 -- Non-resident POA obligations.** Trigger: client is non-UK resident. Message: "Non-resident Self Assessment has different POA rules. Please escalate to a qualified accountant."

**R-UK-POA-3 -- Trust POA.** Trigger: client asks about trust payments on account. Message: "Trust estimated tax is outside the scope of this skill."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions. When a debit matches a pattern below, classify it as a POA payment.

### 3.1 HMRC Self Assessment debits

| Pattern | Treatment | Notes |
|---|---|---|
| HMRC, HM REVENUE, HMRC SELF ASSESSMENT | POA payment | Match with January/July timing |
| HMRC CUMBERNAULD, HMRC SHIPLEY | POA payment | HMRC processing centres |
| SELF ASSESSMENT, SA PAYMENT | POA payment | Explicit description |
| PAYMENT ON ACCOUNT, POA | POA payment | Self-identified |

### 3.2 Timing-based identification

| Debit date range | Likely payment | Confidence |
|---|---|---|
| 15 January -- 5 February | 1st POA + prior year balancing payment | High if payee is HMRC |
| 15 July -- 5 August | 2nd POA | High if payee is HMRC |
| Any other date to HMRC SA | Late payment, voluntary payment, or balancing | Flag for reviewer |

### 3.3 Related but NOT POA payments

| Pattern | Treatment | Notes |
|---|---|---|
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

---

## Section 4 -- Worked examples

### Example 1 -- Standard POA computation

**Input:** Prior year SA balance = GBP 6,000. No excluded items.

**Computation:** Each POA = GBP 6,000 / 2 = GBP 3,000.

| Payment | Due date | Amount |
|---|---|---|
| 1st POA | 31 January 2025 | GBP 3,000 |
| 2nd POA | 31 July 2025 | GBP 3,000 |

### Example 2 -- Below GBP 1,000 threshold

**Input:** Prior year SA balance = GBP 850.

**Output:** Below GBP 1,000 threshold. No POAs required. Full GBP 850 due as balancing payment on 31 January following the tax year.

### Example 3 -- 80% PAYE test met

**Input:** Total tax liability = GBP 20,000. PAYE collected = GBP 17,000. SA balance = GBP 3,000.

**Computation:** PAYE% = 17,000 / 20,000 = 85% > 80%. No POA required despite SA balance exceeding GBP 1,000.

### Example 4 -- Excluded items removed

**Input:** Prior year SA: income tax via SA = GBP 4,000, CGT = GBP 3,000, Class 2 NIC = GBP 179.40, student loan = GBP 1,200. Total SA balance = GBP 8,379.40.

**Computation:** POA basis = GBP 4,000 only (CGT, Class 2, student loan excluded). Each POA = GBP 2,000.

### Example 5 -- SA303 reduction

**Input:** Standard POA = GBP 5,000 each. Client expects current year SA balance = GBP 3,000. SA303 filed.

**Output:** Reduced POA = GBP 1,500 each. If actual liability = GBP 6,000, HMRC charges interest on GBP 3,500 shortfall per instalment from original due dates.

### Example 6 -- Late payment interest

**Input:** 1st POA of GBP 3,000 due 31 January. Paid 15 April (74 days late). Bank of England base rate = 5.25%.

**Computation:** Interest rate = 5.25% + 2.5% = 7.75%. Interest = GBP 3,000 x 7.75% / 365 x 74 = GBP 47.12.

---

## Section 5 -- Computation rules

### 5.1 Threshold tests

POAs are NOT required if EITHER condition is met:
- **Test 1 (de minimis):** Prior year SA balance < GBP 1,000
- **Test 2 (PAYE dominance):** More than 80% of prior year total tax was collected via PAYE/deduction at source

### 5.2 SA balance definition

```
SA_balance = total_tax_and_class4_NIC - tax_deducted_at_source
```

EXCLUDE from SA balance: Class 2 NIC, student loan repayments, postgraduate loan repayments, capital gains tax, marriage allowance adjustments.

### 5.3 POA computation

```
each_POA = SA_balance / 2
```

### 5.4 Balancing payment

```
balancing_payment = actual_tax_liability - POA_1 - POA_2
```

The balancing payment includes all excluded items (Class 2 NIC, student loan, postgraduate loan, CGT) -- these are payable in full with the balancing payment.

### 5.5 SA303 claim to reduce

A taxpayer expecting lower current year income may file SA303 to reduce POAs to any amount including GBP 0. Risk: if the reduction is too aggressive, HMRC charges interest on the shortfall from the ORIGINAL due dates.

```
reduced_POA_each = estimated_current_year_SA_balance / 2
```

---

## Section 6 -- Penalties and interest

### 6.1 Late payment interest

| Element | Rule |
|---|---|
| Rate | Bank of England base rate + 2.5% (approx. 7.0-7.5% for 2024/25) |
| Runs from | Due date of the POA (31 Jan or 31 Jul) |
| Runs until | Date of payment |
| Compounding | Simple interest (not compound) |
| Tax deductibility | NOT tax deductible |

### 6.2 Interest computation

```
interest = overdue_amount x (base_rate + 2.5%) / 365 x days_overdue
```

There is no separate penalty for late POA payment -- only interest. A surcharge may apply if the balancing payment is more than 30 days late.

---

## Section 7 -- Interaction with tax codes and PAYE

When HMRC collects SA underpayments via a PAYE tax code (coding out), this reduces the SA balance and therefore reduces POAs for the following year. Maximum coding out is GBP 3,000 for employed taxpayers.

If HMRC is coding out underpayments, verify whether the coded amount has been correctly removed from the SA balance before computing POAs.

---

## Section 8 -- Edge cases

**EC1 -- First year of Self Assessment.** No prior year return. No POAs in the first year. All tax due as a single balancing payment. POAs begin from the second year.

**EC2 -- SA303 reduction to zero, then income increases.** Balancing payment of full amount due 31 January. HMRC charges interest on the shortfall from each original POA due date.

**EC3 -- Employment plus self-employment.** GBP 50,000 PAYE + GBP 15,000 SE. Total tax GBP 18,000, PAYE GBP 14,000. PAYE% = 77.8% < 80%. POAs apply. SA balance = GBP 4,000, each POA = GBP 2,000.

**EC4 -- Prior year SA balance just below GBP 1,000.** GBP 980. No POAs required. Full amount due as balancing payment.

**EC5 -- Client stops trading mid-year.** May file SA303 to reduce. Overpayment refunded with balancing payment.

**EC6 -- Prior year included one-off capital gain.** CGT excluded from POA calculation. If HMRC set POAs at the higher amount, file SA303 to correct.

**EC7 -- Student loan pushed SA balance above GBP 1,000.** Student loan excluded. SA balance for POA test = income tax via SA only. If that is below GBP 1,000, no POAs.

**EC8 -- 31 January falls on a weekend.** Deadline moves to next working day. No interest for the weekend days.

**EC9 -- HMRC amendment reduces prior year liability.** HMRC should adjust POAs automatically. If not, file SA303 referencing the amendment.

**EC10 -- Marriage allowance transfer.** Reduces transferor's tax, increases recipient's. POAs based on NET SA balance after marriage allowance.

---

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Both threshold tests checked (GBP 1,000 and 80% PAYE)
- [ ] Class 2 NIC, student loan, CGT, postgraduate loan excluded from SA balance
- [ ] POA computed as 50% of SA balance (not 50% of total tax)
- [ ] 31 January double-payment impact noted (balancing + 1st POA)
- [ ] SA303 interest risk flagged if reduction is recommended
- [ ] Prior year return status confirmed
- [ ] Coding out adjustments verified if applicable
- [ ] Weekend/holiday due date adjustments checked
- [ ] Balancing payment includes all excluded items
- [ ] Output labelled as estimated until prior year return is filed and processed

---

## Section 10 -- Test suite

### Test 1 -- Standard POA computation
**Input:** Prior year SA balance = GBP 6,000.
**Expected:** Each POA = GBP 3,000. 1st due 31 Jan, 2nd due 31 Jul.

### Test 2 -- Below GBP 1,000 threshold
**Input:** Prior year SA balance = GBP 850.
**Expected:** No POA. Full GBP 850 due as balancing payment.

### Test 3 -- 80% PAYE test met
**Input:** Total tax = GBP 20,000. PAYE = GBP 17,000. SA balance = GBP 3,000.
**Expected:** PAYE% = 85% > 80%. No POA required.

### Test 4 -- Excluded items removed
**Input:** Income tax via SA = GBP 4,000, CGT = GBP 3,000, Class 2 = GBP 179.40, student loan = GBP 1,200.
**Expected:** POA basis = GBP 4,000. Each POA = GBP 2,000.

### Test 5 -- SA303 reduction
**Input:** Standard POA = GBP 5,000 each. Estimated current year = GBP 3,000. SA303 filed.
**Expected:** Reduced POA = GBP 1,500 each. Interest risk flagged.

### Test 6 -- Balancing payment with overpayment
**Input:** POAs paid GBP 4,000 + GBP 4,000. Actual SA balance = GBP 6,500.
**Expected:** Overpayment = GBP 1,500. HMRC refunds or sets off.

### Test 7 -- Late payment interest
**Input:** POA GBP 3,000 due 31 Jan. Paid 15 Apr (74 days). Base rate 5.25%.
**Expected:** Rate = 7.75%. Interest = GBP 3,000 x 7.75% / 365 x 74 = GBP 47.12.

---

## Prohibitions

- NEVER include Class 2 NIC, student loan, postgraduate loan, or CGT in the POA calculation
- NEVER compute POAs without checking both threshold tests (GBP 1,000 and 80% PAYE)
- NEVER advise filing SA303 without flagging the interest risk on shortfalls
- NEVER use current year income to compute POAs -- always prior year SA balance
- NEVER ignore the 31 January double-payment impact (balancing + 1st POA)
- NEVER present POA figures as definitive until the prior year return is filed and processed
- NEVER assume HMRC has automatically adjusted POAs after a return amendment
- NEVER conflate POA interest (simple, base+2.5%) with late filing penalties (separate regime)
- NEVER advise on penalty disputes without escalating to a qualified accountant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
