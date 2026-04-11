---
name: za-provisional-tax
description: Use this skill whenever asked about South African provisional tax (IRP6) for self-employed individuals. Trigger on phrases like "IRP6", "provisional tax", "SARS provisional", "estimated tax South Africa", "first provisional period", "second provisional period", "third provisional", "underestimation penalty", or any question about South African provisional tax obligations for self-employed persons. Covers first period (Aug 31), second period (Feb 28), voluntary third period (Sep 30), underestimation penalties, basic amount rules, and edge cases. ALWAYS read this skill before touching any South African provisional tax work.
---

# South Africa Provisional Tax (IRP6) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | South Africa |
| Jurisdiction Code | ZA |
| Primary Legislation | Income Tax Act 58 of 1962, Fourth Schedule (provisional tax) |
| Supporting Legislation | Tax Administration Act 28 of 2011, SARS Interpretation Notes |
| Tax Authority | SARS (South African Revenue Service) |
| Rate Publisher | SARS (annual tax tables, Fourth Schedule parameters) |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: payment periods, estimation rules, basic amount, underestimation thresholds. Tier 2: mid-year commencement, cessation, turnover tax election. Tier 3: tax disputes, objections to penalties, s89quat interest calculations. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified tax practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any provisional tax figure, you MUST know:

1. **Is the client a provisional taxpayer?** [T1] -- anyone receiving income not subject to PAYE (employees' tax) where taxable income exceeds the tax threshold
2. **Year of assessment** [T1] -- standard: March 1 to February 28/29
3. **Prior year taxable income** [T1] -- determines the "basic amount"
4. **Estimated current year taxable income** [T1] -- for first and second period estimates
5. **Any PAYE credits (employees' tax withheld)?** [T1] -- offset against provisional tax
6. **Is taxable income expected to exceed R1,000,000?** [T1] -- different underestimation threshold

**If the client is unsure whether they are a provisional taxpayer, check: do they receive any income not subject to employees' tax (e.g., freelance, rental, business income)?**

---

## Step 1: Who is a Provisional Taxpayer? [T1]

**Legislation:** ITA Fourth Schedule, paragraph 1

| Category | Provisional Taxpayer? |
|----------|----------------------|
| Self-employed / sole proprietor | YES |
| Freelancer / contractor | YES |
| Rental income recipient | YES (if taxable income exceeds threshold) |
| Director receiving director's fees | YES |
| Salaried employee ONLY (all income under PAYE) | NO |
| Person under 65 with taxable income <= R95,750 (2025) | NO (below tax threshold) |

### Exemption from Provisional Tax

A natural person is NOT a provisional taxpayer if:

- No income from carrying on a business
- Taxable income from interest, foreign dividends, rental, and remuneration that does not exceed R30,000 for the year

---

## Step 2: Payment Periods and Due Dates [T1]

**Legislation:** ITA Fourth Schedule, paragraphs 21-25

### Year of Assessment: 1 March 2024 to 28 February 2025

| Period | Covers | Due Date | Requirement |
|--------|--------|----------|-------------|
| First provisional (IRP6) | First 6 months (Mar-Aug) | 31 August 2025 | Estimate full year taxable income; pay half of estimated tax |
| Second provisional (IRP6) | Full year (Mar-Feb) | 28 February 2026 | Estimate full year taxable income; pay balance after first period credit |
| Third provisional (voluntary) | Full year top-up | 30 September 2026 | Optional; avoids interest on underpayment; must be within 12 months of year-end |

### Payment Calculation

```
first_period_payment = estimated_annual_tax / 2 - PAYE_credits_to_date
second_period_payment = estimated_annual_tax - first_period_payment - PAYE_credits
third_period_payment = actual_tax - first_payment - second_payment - PAYE_credits
```

---

## Step 3: The Basic Amount [T1]

**Legislation:** ITA Fourth Schedule, paragraph 19(1)(d)

The "basic amount" is the taxable income assessed for the latest preceding year of assessment. It serves as a safe harbour benchmark.

| Situation | Basic Amount |
|-----------|-------------|
| Prior year assessed | Prior year taxable income |
| No prior year assessment | Zero (no safe harbour available) |
| Prior year loss | Zero |

**The basic amount is critical for underestimation penalty protection. See Step 5.**

---

## Step 4: Estimation Rules [T1]

**Legislation:** ITA Fourth Schedule

### First Period (Aug 31)

| Rule | Detail |
|------|--------|
| Minimum estimate | Should reflect reasonable estimate of full-year taxable income |
| Safe harbour | No formal safe harbour for first period; but using basic amount avoids SARS scrutiny |
| Penalty risk | No underestimation penalty on first period (penalty applies only to second period) |

### Second Period (Feb 28)

| Rule | Detail |
|------|--------|
| Accuracy requirement | Estimate must be within accuracy thresholds (see Step 5) |
| Underestimation penalty | YES -- penalty applies if estimate is too low |
| Basic amount benchmark | Using basic amount as estimate protects against penalty |

---

## Step 5: Underestimation Penalties [T1]

**Legislation:** ITA Fourth Schedule, paragraph 20

### Thresholds

| Taxable Income Level | Penalty Trigger |
|---------------------|----------------|
| R1,000,000 or less | Penalty if second period estimate < 90% of actual taxable income AND estimate < basic amount |
| Above R1,000,000 | Penalty if second period estimate < 80% of actual taxable income |

### Penalty Calculation

```
penalty = 20% × (tax_on_80%_of_actual - tax_on_estimated)
```

For taxable income > R1M:
```
penalty = 20% × (tax_on_80%_of_actual_income - provisional_tax_paid_for_second_period)
```

### Safe Harbour Rules

| Taxable Income | Safe Harbour |
|----------------|-------------|
| <= R1,000,000 | Use basic amount (prior year taxable income) as estimate -- NO penalty even if actual is higher |
| > R1,000,000 | No safe harbour from basic amount; must estimate within 80% of actual |

**For clients with taxable income > R1M, accuracy is critical. There is no basic amount safe harbour.**

---

## Step 6: Third Provisional Payment (Voluntary) [T1]

**Legislation:** ITA Fourth Schedule, paragraph 23

| Item | Detail |
|------|--------|
| Due date | 30 September (7 months after year-end for Feb year-end) |
| Purpose | Top up underpayments to reduce s89quat interest |
| Mandatory? | NO -- voluntary |
| Who benefits? | Clients whose actual income exceeded second period estimate |
| Effect | Reduces or eliminates interest on underpayment |

---

## Step 7: Interest on Underpayment [T1]

**Legislation:** ITA s89quat

| Item | Detail |
|------|--------|
| Rate | SARS prescribed rate (currently ~10.75% per annum, updated periodically) |
| When charged | If provisional tax paid is insufficient |
| First period shortfall | Interest runs from August 31 to payment date |
| Second period shortfall | Interest runs from February 28 to payment date |
| How to avoid | Third provisional payment by September 30; accurate estimates |

---

## Step 8: Registration and Filing [T1]

| Requirement | Detail |
|-------------|--------|
| Registration | Register as provisional taxpayer on eFiling or at SARS branch |
| Filing | IRP6 submitted via SARS eFiling |
| Payment | EFT to SARS, eFiling payment, or at bank |
| Tax reference number | Required for all submissions |

---

## Step 9: Edge Case Registry

### EC1 -- New self-employed, no prior year assessment [T1]
**Situation:** Client started freelancing in June 2024, no prior year tax return.
**Resolution:** Basic amount is zero. No safe harbour. Must estimate current year income as accurately as possible. No underestimation penalty protection from basic amount.

### EC2 -- Taxable income just above R1M [T1]
**Situation:** Client's actual taxable income is R1,050,000.
**Resolution:** Above R1M threshold. Must estimate within 80% (R840,000+). Basic amount safe harbour does NOT apply. If second period estimate was R800,000, penalty applies.

### EC3 -- Client had a loss year followed by profitable year [T2]
**Situation:** Prior year taxable income was a loss (basic amount = zero). Current year taxable income is R500,000.
**Resolution:** Basic amount is zero. Cannot rely on basic amount safe harbour. Must estimate accurately. [T2] flag -- ensure client understands no safe harbour exists.

### EC4 -- Mid-year commencement of trade [T2]
**Situation:** Client started a business in October 2024 (mid-year).
**Resolution:** Still required to file second provisional by February 28. First period may have already passed (August 31). [T2] flag for reviewer -- confirm whether late registration triggers penalties or whether SARS permits late first period filing.

### EC5 -- Client with both employment and self-employment income [T1]
**Situation:** Client earns R800,000 salary (PAYE) and R400,000 freelance income.
**Resolution:** Provisional taxpayer because of freelance income. Estimated taxable income = R1,200,000. PAYE credits offset provisional tax. Since total > R1M, 80% accuracy rule applies (no safe harbour). Estimate must be >= R960,000.

### EC6 -- Underestimation by more than 20% but below R1M [T1]
**Situation:** Client estimated R400,000 but actual was R700,000. Basic amount (prior year) was R450,000.
**Resolution:** Since taxable income <= R1M: penalty only if estimate < 90% of actual (R630,000) AND estimate < basic amount (R450,000). Estimate R400,000 < basic amount R450,000, so penalty applies. Had client used R450,000 as estimate, no penalty.

### EC7 -- Third period payment timing [T1]
**Situation:** Client realizes in August that second period estimate was too low.
**Resolution:** File third provisional payment by September 30 to reduce interest. This does NOT eliminate the underestimation penalty (which is locked in at second period), but it reduces s89quat interest.

### EC8 -- Cessation of trade mid-year [T2]
**Situation:** Client closes their business in November 2024.
**Resolution:** Still required to file second provisional by February 28 for the year ending February 2025. Final assessment covers full year. [T2] flag for reviewer -- confirm no special filing required for cessation.

### EC9 -- Company vs. individual provisional tax [T1]
**Situation:** Client asks about provisional tax for their company.
**Resolution:** This skill covers individual provisional tax only. Companies have different periods (June/December year-end) and different rules. Refer to corporate provisional tax skill.

---

## Step 10: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified tax practitioner must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified tax practitioner. Document gap.
```

---

## Step 11: Test Suite

### Test 1 -- Standard first period payment
**Input:** Estimated annual taxable income R600,000. No PAYE. First period.
**Expected output:** Tax on R600,000 per SARS tables. First period = estimated annual tax / 2.

### Test 2 -- Second period with basic amount safe harbour
**Input:** Prior year taxable income R500,000. Actual current year R700,000. Second period estimate = R500,000 (basic amount).
**Expected output:** No underestimation penalty. R500,000 >= basic amount. Taxable income <= R1M, so safe harbour applies.

### Test 3 -- Second period penalty triggered (below R1M)
**Input:** Basic amount R400,000. Second period estimate R350,000. Actual R800,000.
**Expected output:** 90% of actual = R720,000. Estimate R350,000 < R720,000 AND < basic amount R400,000. Penalty = 20% x (tax on R640,000 - tax on R350,000).

### Test 4 -- Above R1M, no safe harbour
**Input:** Actual taxable income R1,500,000. Second period estimate R1,000,000. Basic amount R1,200,000.
**Expected output:** 80% of actual = R1,200,000. Estimate R1,000,000 < R1,200,000. Penalty applies regardless of basic amount. Penalty = 20% x (tax on R1,200,000 - tax on R1,000,000).

### Test 5 -- Third period reducing interest
**Input:** Second period estimate R500,000. Actual R800,000. Third payment of R100,000 made by Sep 30.
**Expected output:** Underestimation penalty calculated on second period (if applicable). Third payment reduces s89quat interest from Sep 30, not the penalty.

### Test 6 -- Employee with side income
**Input:** Salary R900,000 (PAYE). Freelance R300,000. Total R1,200,000.
**Expected output:** Provisional taxpayer. Estimate must include total R1,200,000. PAYE on R900,000 credited. Above R1M so 80% accuracy rule applies.

### Test 7 -- New taxpayer, no basic amount
**Input:** First year self-employed. No prior assessment. Estimated R400,000.
**Expected output:** Basic amount = zero. No safe harbour. If actual exceeds estimate by >10%, penalty may apply. Estimate carefully.

---

## PROHIBITIONS

- NEVER estimate taxable income without asking about ALL income sources (employment + self-employment + rental + investment)
- NEVER tell a client with taxable income above R1M that the basic amount protects them -- it does not
- NEVER ignore PAYE credits when computing provisional tax payments
- NEVER confuse the underestimation penalty (locked at second period) with s89quat interest (reducible via third period)
- NEVER assume the third provisional period is mandatory -- it is voluntary
- NEVER present provisional tax as a separate tax -- it is a prepayment of normal income tax
- NEVER compute underestimation penalties without knowing both the estimate AND the actual taxable income
- NEVER advise on objections to SARS penalties without escalating to a qualified tax practitioner
- NEVER use outdated SARS prescribed interest rates -- verify the current rate

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
