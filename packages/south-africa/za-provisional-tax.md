---
name: za-provisional-tax
description: Use this skill whenever asked about South African provisional tax (IRP6) for self-employed individuals. Trigger on phrases like "IRP6", "provisional tax", "SARS provisional", "estimated tax South Africa", "first provisional period", "second provisional period", "third provisional", "underestimation penalty", or any question about South African provisional tax obligations for self-employed persons. Covers first period (Aug 31), second period (Feb 28), voluntary third period (Sep 30), underestimation penalties, basic amount rules, and edge cases. ALWAYS read this skill before touching any South African provisional tax work.
version: 2.0
---

# South Africa Provisional Tax (IRP6) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | South Africa |
| Authority | SARS (South African Revenue Service) |
| Primary legislation | Income Tax Act 58 of 1962, Fourth Schedule |
| Supporting legislation | Tax Administration Act 28 of 2011 |
| Year of assessment | 1 March to 28/29 February |
| First period due | 31 August |
| Second period due | 28/29 February |
| Third period (voluntary) | 30 September |
| Underestimation threshold (<= R1M) | 90% of actual AND >= basic amount |
| Underestimation threshold (> R1M) | 80% of actual (no safe harbour) |
| Penalty rate | 20% of shortfall |
| Interest rate (s89quat) | ~10.75% p.a. (verify current) |
| Tax threshold (under 65, 2025) | R95,750 |
| Filing method | SARS eFiling (IRP6) |
| Currency | ZAR only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by South African tax practitioner |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Is client a provisional taxpayer?** -- receives income not subject to PAYE?
2. **Year of assessment**
3. **Prior year taxable income** -- determines "basic amount"
4. **Estimated current year taxable income**
5. **PAYE credits?** -- offset against provisional tax
6. **Expected taxable income above R1,000,000?** -- different threshold

### Refusal catalogue

**R-ZA-PROV-1 -- Tax dispute / objection.** Trigger: client wants to object to SARS penalty. Message: "Objections to SARS penalties require qualified tax practitioner review. Escalate."

**R-ZA-PROV-2 -- Company provisional tax.** Trigger: question about company (not individual) provisional tax. Message: "This skill covers individuals only. Companies have different rules."

### Prohibitions

- NEVER estimate without asking about ALL income sources
- NEVER tell a client with income > R1M that basic amount protects them -- it does not
- NEVER ignore PAYE credits
- NEVER confuse underestimation penalty (locked at second period) with s89quat interest (reducible via third period)
- NEVER assume third period is mandatory -- it is voluntary
- NEVER present provisional tax as a separate tax -- it is a prepayment
- NEVER compute penalties without both estimate AND actual
- NEVER use outdated SARS interest rates

---

## Section 3 -- Who is a provisional taxpayer

**Legislation:** ITA Fourth Schedule, paragraph 1

| Category | Provisional taxpayer? |
|---|---|
| Self-employed / sole proprietor | YES |
| Freelancer / contractor | YES |
| Rental income recipient | YES (if above threshold) |
| Director receiving director's fees | YES |
| Salaried employee ONLY (all PAYE) | NO |
| Under 65, taxable income <= R95,750 | NO |

Exemption: no business income AND taxable income from interest, foreign dividends, rental, and remuneration <= R30,000.

---

## Section 4 -- Payment periods, basic amount, and estimation

### Payment periods

| Period | Covers | Due date | Requirement |
|---|---|---|---|
| First (IRP6) | First 6 months | 31 August | Estimate full year; pay half of estimated tax |
| Second (IRP6) | Full year | 28 February | Estimate full year; pay balance |
| Third (voluntary) | Top-up | 30 September | Avoids interest on underpayment |

### Basic amount

The "basic amount" = prior year's assessed taxable income. Safe harbour benchmark for underestimation.

| Situation | Basic amount |
|---|---|
| Prior year assessed | Prior year taxable income |
| No prior assessment | Zero |
| Prior year loss | Zero |

### Estimation rules

First period: no underestimation penalty (penalty applies only to second period).

Second period: accuracy thresholds apply (see Section 5).

---

## Section 5 -- Underestimation penalties

**Legislation:** ITA Fourth Schedule, paragraph 20

### Thresholds

| Taxable income | Penalty trigger |
|---|---|
| <= R1,000,000 | If estimate < 90% of actual AND estimate < basic amount |
| > R1,000,000 | If estimate < 80% of actual |

### Safe harbour

| Income | Safe harbour |
|---|---|
| <= R1M | Use basic amount as estimate -- NO penalty even if actual is higher |
| > R1M | No safe harbour -- must estimate within 80% |

### Penalty calculation

```
penalty = 20% x (tax_on_80%_of_actual - tax_on_estimated)
```

---

## Section 6 -- Third period and interest

### Third provisional payment (voluntary)

| Item | Detail |
|---|---|
| Due | 30 September |
| Purpose | Reduce s89quat interest |
| Mandatory? | NO |
| Effect | Reduces interest, NOT the underestimation penalty |

### Interest on underpayment (s89quat)

Rate ~10.75% p.a. (verify current). Runs from period due date to payment date.

---

## Section 7 -- Registration, filing, and payment calculation

### Registration

Register as provisional taxpayer on eFiling or at SARS branch.

### Payment calculation

```
first_period = estimated_annual_tax / 2 - PAYE_credits_to_date
second_period = estimated_annual_tax - first_payment - PAYE_credits
third_period = actual_tax - first - second - PAYE_credits
```

---

## Section 8 -- Edge case registry

### EC1 -- New self-employed, no prior assessment
**Situation:** First year, no basic amount.
**Resolution:** Basic amount = zero. No safe harbour. Must estimate accurately.

### EC2 -- Just above R1M
**Situation:** Actual R1,050,000.
**Resolution:** Must estimate within 80% (R840,000+). No basic amount safe harbour.

### EC3 -- Loss year followed by profit
**Situation:** Prior year loss, current R500,000.
**Resolution:** Basic amount = zero. No safe harbour.

### EC4 -- Employee with side income
**Situation:** Salary R800,000 + freelance R400,000 = R1,200,000.
**Resolution:** Provisional taxpayer. Above R1M, 80% accuracy required. PAYE credited.

### EC5 -- Underestimation below R1M
**Situation:** Basic amount R400,000, estimate R350,000, actual R700,000.
**Resolution:** Estimate < basic amount, so penalty applies. Had client used R450,000 (basic amount), no penalty.

### EC6 -- Third period timing
**Situation:** Realizes in August that second estimate too low.
**Resolution:** Third payment by Sep 30 reduces interest but not penalty.

### EC7 -- Mid-year commencement
**Situation:** Started business October 2024.
**Resolution:** Still must file second provisional by February 28. Flag for reviewer on first period.

### EC8 -- Cessation mid-year
**Situation:** Closes business November 2024.
**Resolution:** Still files second provisional by February 28.

---

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

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

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified tax practitioner. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard first period
**Input:** Estimated annual taxable income R600,000. No PAYE.
**Expected output:** First period = estimated annual tax / 2.

### Test 2 -- Second period, basic amount safe harbour
**Input:** Prior year R500,000. Actual R700,000. Estimate = R500,000.
**Expected output:** No penalty. Safe harbour applies (<= R1M, estimate >= basic amount).

### Test 3 -- Second period penalty (below R1M)
**Input:** Basic amount R400,000. Estimate R350,000. Actual R800,000.
**Expected output:** Estimate < basic amount. Penalty = 20% x (tax on R640,000 - tax on R350,000).

### Test 4 -- Above R1M, no safe harbour
**Input:** Actual R1,500,000. Estimate R1,000,000. Basic amount R1,200,000.
**Expected output:** 80% of actual = R1,200,000. Estimate < R1,200,000. Penalty applies.

### Test 5 -- Third period reducing interest
**Input:** Second estimate R500,000. Actual R800,000. Third payment R100,000 by Sep 30.
**Expected output:** Third reduces interest, not penalty.

### Test 6 -- Employee with side income
**Input:** Salary R900,000 (PAYE) + freelance R300,000 = R1,200,000.
**Expected output:** Above R1M. 80% accuracy. PAYE credited.

### Test 7 -- New taxpayer
**Input:** First year. No prior. Estimated R400,000.
**Expected output:** Basic amount = zero. No safe harbour.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
