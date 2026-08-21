---
name: uk-payments-on-account
description: Use this skill whenever asked about UK Payments on Account (POA) for Self Assessment taxpayers. Trigger on phrases like "payments on account", "POA", "POA 2026", "January payment", "July payment", "balancing payment", "SA303", "claim to reduce", "reduce payments on account", "do I need to make payments on account", "POA threshold", "tax underpayment", "MTD ITSA payments on account", or any question about advance income tax payments under UK Self Assessment. Covers the two-payment schedule (31 January / 31 July), the GBP 1,000 threshold, the 80% PAYE test, balancing payment mechanics, SA303 claim to reduce, excluded items (Class 2 NIC, student loan, CGT), interest on late payments, the interaction with MTD ITSA quarterly updates from 6 April 2026, and interaction with tax codes. ALWAYS read this skill before touching any UK POA work.
version: 3.0
jurisdiction: GB
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Power
review_status: current
depends_on: - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Payments On Account

## UK Payments on Account (POA) -- Self Assessment Skill v3.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **James Power** on 2026-06-03.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Payments on Account

- **De minimis** — SA balance < £1,000 → no POA  _(TMA 1970 s.59A)_
- **PAYE dominance** — >80% of total tax via PAYE → no POA  _(TMA 1970 s.59A)_
- **1st POA** — 31 January in tax year (50% of prior year SA balance)  _(TMA 1970)_
- **2nd POA** — 31 July after tax year (50%)  _(TMA 1970)_
- **Balancing payment** — 31 January following tax year  _(TMA 1970)_
- **Items** — Class 2 NIC, student loan, postgraduate loan, CGT, marriage allowance  _(TMA 1970)_
- **Rate** — BoE base rate + 2.5%  _(TMA 1970 s.86)_
- **Type** — Simple interest (not compound)  _(TMA 1970)_

## Section 1 -- Quick reference

**Section 1 Quick reference table**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | United Kingdom |
| Tax | Income tax advance payments (Payments on Account / POA) |
| Primary legislation | Taxes Management Act 1970 (TMA 1970), Section 59A |
| Supporting legislation | Income Tax (Pay As You Earn) Regulations 2003; Finance Act 2024; Finance (No. 2) Act 2024; TMA 1970 s59B, s86 |
| Authority | HM Revenue & Customs (HMRC) |
| Portal | HMRC Self Assessment Online; from 6 April 2026 also MTD ITSA-compatible software for quarterly updates |
| Currency | GBP only |
| Payment schedule | Two POAs: 31 January (in tax year) + 31 July (after tax year); balancing payment 31 January following |
| Threshold | SA balance >= GBP 1,000 AND tax deducted at source < 80% of total tax |
| Excluded items | Class 2 NIC, student loan, postgraduate loan, CGT, marriage allowance |
| Contributor | Open Accountants Community |
| Validated by | Verified by James Power on 2026-06-03 |
| Validation date | Verified by James Power on 2026-06-03 |

### 1.1 Three-year comparison: variable elements

The POA structural rules (threshold, 50%-of-prior-year formula, two-instalment schedule, SA303 mechanism, excluded items) are UNCHANGED across all three years. Only the late payment interest rate and the surrounding reporting workflow shift.

**Three-year comparison table**

| Element | 2024-25 | 2025-26 | 2026-27 |
| --- | --- | --- | --- |
| Threshold (de minimis) | Prior year SA balance >= GBP 1,000 | Prior year SA balance >= GBP 1,000 | Prior year SA balance >= GBP 1,000 |
| Threshold (PAYE/deduction test) | < 80% of tax deducted at source | < 80% of tax deducted at source | < 80% of tax deducted at source |
| POA calculation | 50% of prior year SA balance, each instalment | 50% of prior year SA balance, each instalment | 50% of prior year SA balance, each instalment |
| 1st POA due | 31 January 2025 | 31 January 2026 | 31 January 2027 |
| 2nd POA due | 31 July 2025 | 31 July 2026 | 31 July 2027 |
| Balancing payment due | 31 January 2026 | 31 January 2027 | 31 January 2028 |
| Late payment interest rate | HMRC Bank Rate + 4 pp (approx. 7.75% late 2024 / 2025) | HMRC Bank Rate + 4 pp (track Bank Rate movements) | HMRC Bank Rate + 4 pp (track Bank Rate movements) |
| SA303 (claim to reduce) | Available; standard process | Available; standard process | Available; standard process |
| MTD ITSA quarterly reporting | Not in scope (most clients) | Not in scope (most clients) | MANDATORY from 6 April 2026 for qualifying SE/property income (does NOT replace POA) |
| Annual reconciliation | SA tax return | SA tax return | SA tax return / Final Declaration under MTD ITSA |

**Note on the 4 pp surcharge.** Finance (No. 2) Act 2024 increased the late payment interest add-on from 2.5 pp to 4 pp from 31 January late onwards (operative for sums overdue from the standard 2024-25 cycle and forward). All worked examples in this version use Bank Rate + 4 pp.

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

- **Refusal policy if minimum is missing** — SOFT WARN. If the prior year SA balance is unknown, flag that POA computation is unreliable and direct the client to obtain their SA302 from HMRC.

### Refusal catalogue

- **R-UK-POA-1 -- Partnerships with complex profit-sharing** — Trigger: client is in a partnership with non-standard profit-sharing ratios. Message: "Partnership POA allocation requires partner-level analysis. Please escalate to a qualified accountant."
- **R-UK-POA-2 -- Non-resident POA obligations** — Trigger: client is non-UK resident. Message: "Non-resident Self Assessment has different POA rules. Please escalate to a qualified accountant."
- **R-UK-POA-3 -- Trust POA** — Trigger: client asks about trust payments on account. Message: "Trust estimated tax is outside the scope of this skill."
- **R-UK-POA-4 -- MTD ITSA software selection / quarterly update preparation** — Trigger: client asks which MTD ITSA software to use, or how to file a quarterly update. Message: "MTD ITSA software selection and quarterly update mechanics are outside the scope of this POA skill. Please use the dedicated MTD ITSA skill or escalate to a qualified accountant."

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

**Input:** Prior year SA: income tax via SA = GBP 4,000, CGT = GBP 3,000, Class 2 NIC = GBP 179.40, student loan = GBP 1,200. Total SA balance = GBP 8,379.40.

**Computation:** POA basis = GBP 4,000 only (CGT, Class 2, student loan excluded). Each POA = GBP 2,000.

### Example 5 -- SA303 reduction

**Input:** Standard POA = GBP 5,000 each. Client expects current year SA balance = GBP 3,000. SA303 filed.

**Output:** Reduced POA = GBP 1,500 each. If actual liability = GBP 6,000, HMRC charges interest on GBP 3,500 shortfall per instalment from original due dates.

### Example 6 -- Late payment interest (Bank Rate + 4 pp)

**Input:** 1st POA of GBP 3,000 due 31 January 2026. Paid 15 April 2026 (74 days late). HMRC Bank Rate = 3.75% (illustrative).

**Computation:** Interest rate = 3.75% + 4.00% = 7.75%. Interest = GBP 3,000 x 7.75% / 365 x 74 = GBP 47.12.

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

**Step C event table**

| Date | Event | Cash impact |
| --- | --- | --- |
| 31 January 2027 | 1st POA 2026-27 + (any) 2025-26 balancing | GBP 6,000 (B1) |
| 5 August 2026 | Q1 MTD ITSA quarterly update due | No tax payment -- reporting only |
| 5 November 2026 | Q2 MTD ITSA quarterly update due | No tax payment -- reporting only |
| 5 February 2027 | Q3 MTD ITSA quarterly update due | No tax payment -- reporting only |
| 5 May 2027 | Q4 MTD ITSA quarterly update due | No tax payment -- reporting only |
| 31 July 2027 | 2nd POA 2026-27 | GBP 6,000 |
| 31 January 2028 | Final Declaration (replaces SA return) + 2026-27 balancing payment + 1st POA 2027-28 | Depends on final 2026-27 liability |

The four quarterly updates are reporting events only -- they do NOT generate new payment dates. POA cash flow continues unchanged.

### 4.1 From April 2026 -- MTD ITSA interaction

- **Headline rule** — Making Tax Digital for Income Tax Self Assessment (MTD ITSA) becomes mandatory from 6 April 2026 for sole traders and landlords with qualifying income above the relevant threshold (GBP 50,000 from April 2026; GBP 30,000 from April 2027; further phasing thereafter -- confirm current threshold for the client at the time of advice).

**MTD ITSA does NOT replace or alter the POA regime.** Specifically:

1. **POA dates remain 31 January and 31 July.** MTD quarterly updates (due 5 August, 5 November, 5 February, 5 May for a standard 6 April -- 5 April year) are SEPARATE reporting events. They do not collect tax.
2. **POA calculation remains 50% of prior year SA balance.** It does not switch to a quarterly profit-to-date basis.
3. **The annual reconciliation continues -- now called the Final Declaration.** This replaces the SA100 tax return for MTD-scope taxpayers and is due 31 January following the tax year, same as before. Balancing payment is due on the same 31 January date.
4. **SA303 (claim to reduce POAs) remains available.** The mechanism is unchanged.
5. **Excluded items continue to be excluded** (Class 2 NIC, student loan, CGT, etc.).

**Workflow change for the practitioner.** The data feeds underpinning the SA balance now flow through MTD-compatible software in quarterly batches. The POA worksheet (the part this skill produces) consumes the same SA balance figure from the prior year's Final Declaration that it previously consumed from the prior year SA return.

**Common client misconception to correct.** Clients in MTD ITSA from April 2026 often assume the quarterly updates settle their tax. They do not. The 31 January / 31 July POA pattern continues, and the Final Declaration is still required.

## Section 5 -- Computation rules

### 5.1 Threshold tests

- **Threshold tests** — POAs are NOT required if EITHER condition is met: - **Test 1 (de minimis):** Prior year SA balance < GBP 1,000 - **Test 2 (deduction dominance):** More than 80% of prior year total tax was collected via PAYE/deduction at source

### 5.2 SA balance definition

- **SA balance formula** — SA_balance = total_tax_and_class4_NIC - tax_deducted_at_source
- **Exclusions** — EXCLUDE from SA balance: Class 2 NIC, student loan repayments, postgraduate loan repayments, capital gains tax, marriage allowance adjustments.

### 5.3 POA computation

- **POA computation formula** — each_POA = SA_balance / 2

### 5.4 Balancing payment

- **Balancing payment formula** — balancing_payment = actual_tax_liability - POA_1 - POA_2
- **Excluded items in balancing payment** — The balancing payment includes all excluded items (Class 2 NIC, student loan, postgraduate loan, CGT) -- these are payable in full with the balancing payment.

### 5.5 SA303 claim to reduce

- **SA303 claim to reduce** — A taxpayer expecting lower current year income may file SA303 to reduce POAs to any amount including GBP 0. Risk: if the reduction is too aggressive, HMRC charges interest on the shortfall from the ORIGINAL due dates.
- **Reduced POA formula** — reduced_POA_each = estimated_current_year_SA_balance / 2

## Section 6 -- Penalties and interest

### 6.1 Late payment interest

**Late payment interest table**

| Element | Rule |
| --- | --- |
| Rate | HMRC Bank Rate + 4 percentage points (per Finance (No. 2) Act 2024 from 31 January late onwards). Approx. 7.75% as at late 2025 -- confirm current Bank Rate. |
| Runs from | Due date of the POA (31 Jan or 31 Jul) |
| Runs until | Date of payment |
| Compounding | Simple interest (not compound) |
| Tax deductibility | NOT tax deductible |

### 6.2 Interest computation

- **Interest computation formula** — interest = overdue_amount x (Bank_Rate + 4%) / 365 x days_overdue

There is no separate penalty for late POA payment -- only interest. A surcharge may apply if the balancing payment is more than 30 days late under the wider late payment penalty regime.

### 6.3 Time-to-Pay arrangements

- **Time-to-Pay (TTP) arrangements** — A taxpayer who cannot meet a POA on time may apply for a Time-to-Pay (TTP) arrangement with HMRC (online for liabilities under GBP 30,000, by phone above). The arrangement does NOT stop interest accruing, but it does stop further collection action and any late payment surcharge on the balancing payment provided the TTP is agreed before the surcharge trigger date. Process unchanged across 2024-25, 2025-26, 2026-27.

## Section 7 -- Interaction with tax codes and PAYE

- **coding out** — When HMRC collects SA underpayments via a PAYE tax code (coding out), this reduces the SA balance and therefore reduces POAs for the following year. Maximum coding out is GBP 3,000 for employed taxpayers. If HMRC is coding out underpayments, verify whether the coded amount has been correctly removed from the SA balance before computing POAs.

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

**EC11 -- Client enters MTD ITSA from 6 April 2026 mid-POA-cycle.** Existing 2025-26 POAs (due 31 Jan 2026 and 31 July 2026) are unchanged. From 6 April 2026 the client begins quarterly updates for the 2026-27 tax year. The 31 January 2027 cash event still combines the 2025-26 balancing payment (computed via Final Declaration or SA100 depending on scope) with the 1st POA for 2026-27.

## Section 9 -- Self-checks

Before delivering output, verify:

- [ ] Both threshold tests checked (GBP 1,000 and 80% deduction at source)
- [ ] Class 2 NIC, student loan, CGT, postgraduate loan excluded from SA balance
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

**Input:** Income tax via SA = GBP 4,000, CGT = GBP 3,000, Class 2 = GBP 179.40, student loan = GBP 1,200.
**Expected:** POA basis = GBP 4,000. Each POA = GBP 2,000.

### Test 5 -- SA303 reduction

**Input:** Standard POA = GBP 5,000 each. Estimated current year = GBP 3,000. SA303 filed.
**Expected:** Reduced POA = GBP 1,500 each. Interest risk flagged.

### Test 6 -- Balancing payment with overpayment

**Input:** POAs paid GBP 4,000 + GBP 4,000. Actual SA balance = GBP 6,500.
**Expected:** Overpayment = GBP 1,500. HMRC refunds or sets off.

### Test 7 -- Late payment interest (Bank Rate + 4 pp)

**Input:** POA GBP 3,000 due 31 Jan 2026. Paid 15 Apr 2026 (74 days). Bank Rate 3.75%.
**Expected:** Rate = 7.75%. Interest = GBP 3,000 x 7.75% / 365 x 74 = GBP 47.12.

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

- NEVER include Class 2 NIC, student loan, postgraduate loan, or CGT in the POA calculation
- NEVER compute POAs without checking both threshold tests (GBP 1,000 and 80% deduction at source)
- NEVER advise filing SA303 without flagging the interest risk on shortfalls
- NEVER use current year income to compute POAs -- always prior year SA balance
- NEVER ignore the 31 January double-payment impact (balancing + 1st POA)
- NEVER present POA figures as definitive until the prior year return is filed and processed
- NEVER assume HMRC has automatically adjusted POAs after a return amendment
- NEVER conflate POA interest (simple, Bank Rate + 4 pp) with late filing penalties (separate regime)
- NEVER use the legacy +2.5 pp interest add-on for periods of lateness running from 31 January 2025 onwards -- the rate is Bank Rate + 4 pp
- NEVER tell a client that MTD ITSA quarterly updates replace POAs -- they do not
- NEVER advise on penalty disputes without escalating to a qualified accountant

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
