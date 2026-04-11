---
name: uk-payments-on-account
description: >
  Use this skill whenever asked about UK Payments on Account (POA) for Self Assessment taxpayers. Trigger on phrases like "payments on account", "POA", "January payment", "July payment", "balancing payment", "SA303", "claim to reduce", "reduce payments on account", "do I need to make payments on account", "POA threshold", "tax underpayment", or any question about advance income tax payments under UK Self Assessment. Covers the two-payment schedule (31 January / 31 July), the GBP 1,000 threshold, the 80% PAYE test, balancing payment mechanics, SA303 claim to reduce, excluded items (Class 2 NIC, student loan, CGT), interest on late payments, and interaction with tax codes. ALWAYS read this skill before touching any UK POA work.
version: 1.0
jurisdiction: GB
tax_year: 2024-25
category: international
depends_on:
  - income-tax-workflow-base
---

# UK Payments on Account (POA) -- Self Assessment Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | United Kingdom |
| Jurisdiction Code | GB |
| Primary Legislation | Taxes Management Act 1970 (TMA 1970), Section 59A |
| Supporting Legislation | Income Tax (Pay As You Earn) Regulations 2003; Finance Act 2024 |
| Tax Authority | HM Revenue & Customs (HMRC) |
| Filing Portal | HMRC Self Assessment Online |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a UK-qualified accountant (ACA/ACCA/CTA) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2024/25 (6 April 2024 to 5 April 2025) |
| Confidence Coverage | Tier 1: POA schedule, threshold tests, balancing payment computation, SA303 mechanics, excluded items, interest rates. Tier 2: optimal timing of SA303 claim, interaction with coding adjustments, POA after year of cessation. Tier 3: partnerships with complex profit-sharing ratios, non-resident POA obligations, trusts. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any POA figure, you MUST know:

1. **Tax year** [T1] -- confirm which tax year (e.g., 2024/25)
2. **Prior year Self Assessment liability** [T1] -- total tax and Class 4 NIC from the prior year SA return
3. **Prior year tax deducted at source** [T1] -- PAYE, tax deducted from interest, dividends tax credits
4. **Prior year SA balance** [T1] -- the amount that was NOT collected at source (this is the POA basis)
5. **Any Class 2 NIC, student loan, or CGT in the prior year** [T1] -- these are excluded from the POA calculation
6. **Has the client filed an SA303 claim to reduce?** [T2] -- if so, the reduced amount applies
7. **Current year income expectations** [T2] -- relevant only if considering SA303

---

## Step 1: Do POAs Apply? -- Threshold Tests [T1]

**Legislation:** TMA 1970, s59A(1)-(2)

POAs are NOT required if EITHER of the following conditions is met:

| Test | Condition | Result |
|------|-----------|--------|
| Test 1: De minimis | Prior year SA balance < GBP 1,000 | No POA required |
| Test 2: PAYE dominance | More than 80% of prior year total tax liability was collected via PAYE/deduction at source | No POA required |

### SA Balance Definition

```
SA_balance = total_tax_and_class4_NIC - tax_deducted_at_source
```

Where `tax_deducted_at_source` includes PAYE, tax on savings interest (if deducted), and any other amounts collected before the return is filed.

**EXCLUDE from SA balance:** Class 2 NIC, student loan repayments, postgraduate loan repayments, capital gains tax. These are paid with the balancing payment only.

### 80% PAYE Test

```
PAYE_percentage = tax_deducted_at_source / total_tax_liability × 100
if PAYE_percentage > 80%: no POA required
```

---

## Step 2: POA Computation [T1]

**Legislation:** TMA 1970, s59A(3)

Each POA = 50% of the prior year SA balance.

### Formula

```
POA_each = SA_balance / 2
```

### Payment Schedule

| Payment | Due Date | Amount |
|---------|----------|--------|
| 1st POA | 31 January in the tax year | 50% of prior year SA balance |
| 2nd POA | 31 July after the tax year | 50% of prior year SA balance |
| Balancing payment | 31 January following the tax year (same date as next year's 1st POA) | Actual liability minus POAs paid |

### Example Timeline (Tax Year 2024/25)

| Date | Payment |
|------|---------|
| 31 January 2025 | 1st POA for 2024/25 + balancing payment for 2023/24 |
| 31 July 2025 | 2nd POA for 2024/25 |
| 31 January 2026 | Balancing payment for 2024/25 + 1st POA for 2025/26 |

**WARNING:** 31 January is a triple-impact date: balancing payment for prior year + 1st POA for current year. Clients must be warned about this cash flow pinch point.

### Calculation Examples

| Prior Year SA Balance | Each POA (50%) | Total POA | Balancing Payment (if actual = same) |
|-----------------------|----------------|-----------|--------------------------------------|
| GBP 5,000 | GBP 2,500 | GBP 5,000 | GBP 0 |
| GBP 12,000 | GBP 6,000 | GBP 12,000 | GBP 0 |
| GBP 800 | N/A | N/A | GBP 800 (below threshold, no POA) |

---

## Step 3: Balancing Payment [T1]

**Legislation:** TMA 1970, s59B

After the SA return for the year is filed:

```
balancing_payment = actual_tax_liability - POA_1_paid - POA_2_paid
if balancing_payment > 0: amount due by 31 January following the tax year
if balancing_payment < 0: HMRC issues a refund (or sets off against next year's POA)
```

The balancing payment includes ALL items excluded from POA:
- Class 2 NIC
- Student loan repayments
- Postgraduate loan repayments
- Capital gains tax

---

## Step 4: Claim to Reduce -- SA303 [T2]

**Legislation:** TMA 1970, s59A(3A)-(4)

If the taxpayer expects current year income to be lower than the prior year, they may claim to reduce POAs.

| Aspect | Detail |
|--------|--------|
| Form | SA303 (online or paper) |
| Timing | Can be filed at any time before the balancing payment is due (31 January following the tax year) |
| Basis | Taxpayer's reasonable estimate of current year liability |
| Online | Available via HMRC Self Assessment online account |
| Reduce to | Any amount, including GBP 0 |

### Risk of Reducing

| Scenario | Consequence |
|----------|-------------|
| Reduction correct | No penalty. Interest saved on overpayment. |
| Reduction too aggressive (actual > reduced) | Interest charged on the shortfall from original due date |
| Deliberate understatement | HMRC may charge a penalty under TMA 1970 s59A(5) |

**[T2] Always flag for reviewer before submitting SA303. Incorrect reduction triggers interest from the ORIGINAL due date, not from when the shortfall is identified.**

### SA303 Mechanics

```
reduced_POA_each = estimated_current_year_SA_balance / 2
```

If one POA has already been paid at the full amount:
```
reduced_POA_2 = max(0, estimated_current_year_SA_balance - POA_1_already_paid)
```

---

## Step 5: Items Excluded from POA Calculation [T1]

**Legislation:** TMA 1970, s59A(1)

The following are NOT included when computing the SA balance for POA purposes:

| Excluded Item | Treatment |
|---------------|-----------|
| Class 2 NIC | Paid with balancing payment only |
| Student loan repayment (Plan 1, 2, 4, 5) | Paid with balancing payment only |
| Postgraduate loan repayment | Paid with balancing payment only |
| Capital gains tax | Paid with balancing payment only |
| Marriage allowance adjustments | Not included in POA basis |

**These items are payable in FULL with the balancing payment on 31 January following the tax year.**

---

## Step 6: Interest on Late POAs [T1]

**Legislation:** TMA 1970, s86; Finance Act 2009, Sch 53

| Item | Rate |
|------|------|
| Late payment interest rate | Bank of England base rate + 2.5% (check current rate; approximately 7.0-7.5% as of 2024/25) |
| Interest runs from | The due date of the POA (31 Jan or 31 Jul) |
| Interest runs until | The date of payment |
| Compounding | Simple interest (not compound) |
| Tax deductibility | Late payment interest is NOT tax deductible |

### Interest Computation

```
interest = overdue_amount × (base_rate + 2.5%) / 365 × days_overdue
```

**HMRC charges interest automatically. There is no penalty for late POA payment per se -- only interest. However, a surcharge may apply if the balancing payment is more than 30 days late.**

---

## Step 7: Interaction with Tax Codes and PAYE [T2]

**Legislation:** PAYE Regulations 2003

| Scenario | POA Impact |
|----------|------------|
| HMRC collects SA balance via tax code (coding out) | Reduces POAs for the following year |
| Maximum coding out | GBP 3,000 for employed taxpayers (HMRC will not code out more) |
| Client opts out of coding | POAs revert to standard calculation |

**[T2] If HMRC is coding out underpayments, verify whether the coded amount has been correctly removed from the SA balance before computing POAs.**

---

## Step 8: Edge Case Registry

### EC1 -- First year of Self Assessment [T1]
**Situation:** Client registers for SA for the first time. No prior year return exists.
**Resolution:** No POAs in the first year. All tax due as a single balancing payment on 31 January. POAs begin from the second year based on the first year's SA balance.

### EC2 -- Client reduces POA to zero, then income increases [T2]
**Situation:** Client filed SA303 reducing POA to GBP 0. Actual SA balance = GBP 8,000.
**Resolution:** Balancing payment of GBP 8,000 due 31 January. HMRC charges interest on GBP 4,000 from 31 January (when 1st POA was due) and GBP 4,000 from 31 July (when 2nd POA was due). Interest runs at base rate + 2.5%.

### EC3 -- Client has both employment and self-employment [T1]
**Situation:** Client earns GBP 50,000 PAYE employment + GBP 15,000 self-employment. Total tax = GBP 18,000 of which GBP 14,000 collected via PAYE.
**Resolution:** SA balance = GBP 4,000. 80% test: GBP 14,000/GBP 18,000 = 77.8% < 80%, so POAs apply. Each POA = GBP 2,000.

### EC4 -- Prior year SA balance just below GBP 1,000 [T1]
**Situation:** Prior year SA balance = GBP 980.
**Resolution:** Below GBP 1,000 threshold. No POAs required. Full amount due as balancing payment.

### EC5 -- Client stops trading mid-year [T2]
**Situation:** Client ceases self-employment in September. POAs were set based on prior year.
**Resolution:** Client may file SA303 to reduce remaining POA. If 1st POA already paid and actual liability is low, overpayment will be refunded with the balancing payment. [T2] flag for reviewer.

### EC6 -- Prior year included one-off capital gain [T2]
**Situation:** Prior year SA balance was GBP 20,000, of which GBP 12,000 was CGT.
**Resolution:** CGT is excluded from POA calculation. SA balance for POA = GBP 8,000. Each POA = GBP 4,000. Client should NOT be making POAs based on GBP 20,000. If HMRC has set POAs at the higher amount, file SA303 to reduce.

### EC7 -- Student loan pushed SA balance above GBP 1,000 [T1]
**Situation:** Prior year: tax = GBP 600 via SA, student loan repayment = GBP 900. Total SA balance = GBP 1,500.
**Resolution:** Student loan is excluded. SA balance for POA test = GBP 600. Below GBP 1,000 threshold. No POAs required.

### EC8 -- 31 January falls on a weekend [T1]
**Situation:** 31 January is a Saturday.
**Resolution:** Payment deadline moves to the next working day (Monday 2 February). Interest does not accrue for the weekend days. HMRC's published guidance confirms this.

### EC9 -- Client receives tax refund but POAs already set [T2]
**Situation:** HMRC processes an amendment to the prior year return, reducing the liability. POAs already calculated on old figures.
**Resolution:** HMRC should automatically adjust POA amounts. If not, client can file SA303 referencing the amended return. [T2] flag for reviewer to confirm HMRC has processed the amendment.

### EC10 -- Marriage allowance transfer affects POA basis [T2]
**Situation:** Client transferred GBP 1,260 of personal allowance to spouse. This reduced their prior year tax.
**Resolution:** Marriage allowance reduces the transferor's tax liability and increases the recipient's. POAs are based on the NET SA balance after marriage allowance. Verify the prior year SA calculation includes the correct marriage allowance treatment.

---

## Step 9: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified accountant must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified accountant. Document gap.
```

---

## Step 10: Test Suite

### Test 1 -- Standard POA computation
**Input:** Prior year SA balance = GBP 6,000 (no excluded items).
**Expected output:** Each POA = GBP 3,000. 1st POA due 31 January. 2nd POA due 31 July. Total POA = GBP 6,000.

### Test 2 -- Below GBP 1,000 threshold
**Input:** Prior year SA balance = GBP 850.
**Expected output:** No POA required. Full GBP 850 due as balancing payment on 31 January following the tax year.

### Test 3 -- 80% PAYE test met
**Input:** Total tax liability = GBP 20,000. PAYE collected = GBP 17,000. SA balance = GBP 3,000.
**Expected output:** PAYE% = 85% > 80%. No POA required despite SA balance exceeding GBP 1,000.

### Test 4 -- Excluded items removed from POA basis
**Input:** Prior year SA: income tax via SA = GBP 4,000, CGT = GBP 3,000, Class 2 NIC = GBP 179.40, student loan = GBP 1,200. Total SA balance = GBP 8,379.40.
**Expected output:** POA basis = GBP 4,000 only. Each POA = GBP 2,000. CGT, Class 2, and student loan paid with balancing payment.

### Test 5 -- SA303 reduction
**Input:** Standard POA = GBP 5,000 each (based on prior year). Client expects current year SA balance = GBP 3,000. SA303 filed.
**Expected output:** Reduced POA = GBP 1,500 each. If actual liability = GBP 6,000, interest charged on GBP 3,500 shortfall per instalment from original due dates.

### Test 6 -- Balancing payment with overpayment
**Input:** POAs paid: GBP 4,000 + GBP 4,000 = GBP 8,000. Actual SA balance = GBP 6,500.
**Expected output:** Overpayment = GBP 1,500. HMRC issues refund or sets off against next year's POA.

### Test 7 -- Late payment interest
**Input:** 1st POA of GBP 3,000 due 31 January. Paid 15 April (74 days late). Base rate = 5.25%.
**Expected output:** Interest rate = 7.75% (5.25% + 2.5%). Interest = GBP 3,000 x 7.75% / 365 x 74 = GBP 47.12.

---

## PROHIBITIONS

- NEVER include Class 2 NIC, student loan, postgraduate loan, or CGT in the POA calculation
- NEVER compute POAs without first checking both threshold tests (GBP 1,000 and 80% PAYE)
- NEVER advise filing SA303 without flagging the interest risk on shortfalls
- NEVER use current year income to compute POAs -- POAs are always based on PRIOR year SA balance
- NEVER ignore the 31 January double-payment impact (balancing + 1st POA)
- NEVER present POA figures as definitive until the prior year return has been filed and processed
- NEVER assume HMRC has automatically adjusted POAs after a return amendment -- verify
- NEVER conflate POA interest (simple, base+2.5%) with late filing penalties (separate regime)
- NEVER advise on penalty disputes without escalating to a qualified accountant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
