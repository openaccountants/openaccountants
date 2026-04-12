---
name: pl-zus-contributions
description: Use this skill whenever asked about Polish ZUS (Zakład Ubezpieczeń Społecznych) social contributions for self-employed individuals. Trigger on phrases like "ZUS contributions", "składki ZUS", "Polish social insurance", "Mały ZUS Plus", "self-employed Poland contributions", "działalność gospodarcza ZUS", or any question about social/health insurance obligations for a self-employed client in Poland. Covers retirement 19.52%, disability 8%, sickness 2.45%, health 9%, and Mały ZUS Plus. ALWAYS read this skill before touching any Poland social contributions work.
version: 2.0
---

# Poland ZUS Contributions -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Poland (Republic of Poland) |
| Authority | ZUS (Zakład Ubezpieczeń Społecznych) |
| Primary legislation | Ustawa o systemie ubezpieczeń społecznych (13 Oct 1998) |
| Supporting legislation | Health Insurance Act; Prawo przedsiębiorców |
| Standard social base (2025) | 60% avg forecasted wage = PLN 4,694.40/month |
| Total social rate (with sickness) | 31.64% |
| Fundusz Pracy | 2.45% (when base >= min wage) |
| Health rate (PIT-36) | 9% of actual income |
| Health rate (PIT-36L) | 4.9% of actual income |
| Health rate (PIT-28 ryczałt) | 9% on fixed bracket base |
| DRA filing deadline | 20th of following month |
| Currency | PLN only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Polish doradca podatkowy |
| Validation date | Pending |

**Four contribution tiers:**

| Tier | Who | Social base |
|---|---|---|
| Ulga na start | First 6 months | No social (health only) |
| Preferencyjne | Months 7-30 | 30% of min wage (PLN 1,399.80) |
| Mały ZUS Plus | Revenue < PLN 120,000 prior year | Income-based (clamped) |
| Standard (Duży ZUS) | All others | 60% avg wage (PLN 4,694.40) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Business registration** -- registered działalność gospodarcza?
2. **Months in business** -- first 6 months (Ulga na start)? First 24 months after Ulga (Preferencyjne)?
3. **Prior-year revenue** -- determines Mały ZUS Plus eligibility
4. **Health insurance basis** -- which tax form (PIT-36, PIT-36L, PIT-28)?
5. **Voluntary sickness insurance?** -- chorobowe is optional
6. **Any concurrent employment?** -- may exempt from certain ZUS obligations

**If months in business is unknown, STOP. Different regimes apply based on tenure.**

### Refusal catalogue

**R-PL-ZUS-1 -- Cross-border EU worker.** Trigger: client works in Poland and another EU state. Message: "EU Regulation 883/2004 applies. A1 certificate required. Escalate to reviewer."

### Prohibitions

- NEVER compute health insurance without knowing the tax form -- rates differ between PIT-36, PIT-36L, and PIT-28
- NEVER apply Ulga na start or Preferencyjne to clients providing services to their former employer
- NEVER forget that sickness insurance (chorobowe) is VOLUNTARY for self-employed
- NEVER ignore the 36/60 month limit on Mały ZUS Plus usage
- NEVER state health contributions are fully tax-deductible -- deductibility depends on tax form
- NEVER apply Fundusz Pracy when the contribution base is below the minimum wage
- NEVER double social contributions for clients with multiple businesses
- NEVER present Ulga na start as risk-free -- the client has NO social coverage during this period

---

## Section 3 -- Social insurance rates (2025)

**Legislation:** Art. 22 Ustawy o sus

### Standard (Duży ZUS) rates

| Component | Rate | Monthly (base PLN 4,694.40) |
|---|---|---|
| Retirement (emerytalne) | 19.52% | PLN 916.35 |
| Disability (rentowe) | 8.00% | PLN 375.55 |
| Sickness (chorobowe) -- voluntary | 2.45% | PLN 115.01 |
| Accident (wypadkowe) | 1.67% | PLN 78.40 |
| **Total social (with sickness)** | **31.64%** | **PLN 1,485.31** |
| **Total social (without sickness)** | **29.19%** | **PLN 1,370.30** |
| Fundusz Pracy | 2.45% | PLN 115.01 |

### Preferencyjne ZUS (months 7-30)

| Parameter | Value (2025) |
|---|---|
| Base | 30% of minimum wage = PLN 1,399.80/month |
| Total social (with sickness) | PLN 442.90 |
| Fundusz Pracy | NOT required (base below min wage) |

---

## Section 4 -- Health insurance rates (2025)

| Tax form | Health rate | Base |
|---|---|---|
| PIT-36 (tax scale) | 9% | Actual monthly income (min 75% of min wage) |
| PIT-36L (flat 19%) | 4.9% | Actual monthly income (min 75% of min wage) |
| PIT-28 (ryczałt) | 9% | Fixed base by revenue bracket |

### Ryczałt health brackets

| Annual revenue | Monthly health (9%) |
|---|---|
| Up to PLN 60,000 | PLN 461.66 |
| PLN 60,001 -- 300,000 | PLN 769.43 |
| Above PLN 300,000 | PLN 1,384.97 |

---

## Section 5 -- Computation steps

### Step 5.1 -- Determine tier

```
IF months_in_business <= 6 AND ulga_na_start_used:
    tier = "ulga_na_start"
ELIF months_in_business <= 30 AND preferencyjne_eligible:
    tier = "preferencyjne"
ELIF prior_year_revenue < 120,000 AND maly_zus_eligible:
    tier = "maly_zus_plus"
ELSE:
    tier = "standard"
```

### Step 5.2 -- Calculate social contributions

```
social_base = base_for_tier
retirement = social_base x 19.52%
disability = social_base x 8.00%
sickness = social_base x 2.45%  (if opted in)
accident = social_base x 1.67%
fundusz_pracy = social_base x 2.45%  (only if base >= minimum wage)
total_social = retirement + disability + sickness + accident + fundusz_pracy
```

### Step 5.3 -- Calculate health insurance

```
IF tax_form == "PIT-36":
    health_base = max(actual_monthly_income, 75% of min_wage)
    health = health_base x 9%
ELIF tax_form == "PIT-36L":
    health_base = max(actual_monthly_income, 75% of min_wage)
    health = health_base x 4.9%
ELIF tax_form == "PIT-28":
    health = ryczałt_bracket_amount
```

### Step 5.4 -- Mały ZUS Plus base

```
annual_income = prior_year_income (profit, not revenue)
daily_base = annual_income x 30 / number_of_days_of_activity
monthly_base = daily_base x 30
monthly_base = clamp(30% of min_wage, monthly_base, 60% of avg_wage)
```

---

## Section 6 -- Payment schedule and tax deductibility

### Payment schedule

| Obligation | Due date |
|---|---|
| Monthly ZUS declaration (DRA) | 20th of the following month |
| Payment of contributions | 20th of the following month |

Payments via transfer to individual NRS account. Late payment: interest at 200% of Lombard rate / 365 x days late.

### Tax deductibility

| Contribution | Deductible? | How? |
|---|---|---|
| Retirement, disability, sickness, accident | YES | From income or from tax |
| Fundusz Pracy | YES | Business expense |
| Health (PIT-36) | Partially: 7.75% of base from tax | NOT from income |
| Health (PIT-36L) | Capped deduction from income (~PLN 12,900/year) | From income |
| Health (PIT-28) | 50% deductible from revenue | From revenue |

---

## Section 7 -- Ulga na start and special situations

### Ulga na start (first 6 months)

- NO social insurance contributions for first 6 full calendar months
- Health insurance is still mandatory
- Client has no pension/disability/sickness coverage during this period

### Concurrent full-time employment

If employment salary >= minimum wage: social contributions from business are voluntary. Health insurance still mandatory from the business.

### Services to former employer

In first 24 months: Preferencyjne ZUS NOT available. Ulga na start NOT available. Standard ZUS from day one. Mały ZUS Plus also excluded.

### Multiple businesses

ZUS contributions paid only once, on the higher base. Not doubled.

---

## Section 8 -- Edge case registry

### EC1 -- Ulga na start, no social coverage
**Situation:** Client in month 4 of activity.
**Resolution:** No social insurance. Only health due. Flag: NO pension, disability, or sickness coverage.

### EC2 -- Switching from Preferencyjne to Mały ZUS Plus
**Situation:** Client finishing 24 months of Preferencyjne, prior-year revenue under PLN 120,000.
**Resolution:** Can transition to Mały ZUS Plus if all conditions met. Must register by 31 January of the year.

### EC3 -- Income below health minimum
**Situation:** PIT-36 client, monthly income PLN 500.
**Resolution:** Health base = 75% of minimum wage (floor). Minimum applies regardless of actual income.

### EC4 -- Paušální daň equivalent (lump-sum ryczałt)
**Situation:** Client on ryczałt with annual revenue PLN 400,000.
**Resolution:** Health = PLN 1,384.97/month (180% bracket). Social at standard rates.

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
Action Required: Qualified doradca podatkowy must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified doradca podatkowy. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard ZUS (Duży ZUS)
**Input:** Established business, PIT-36, monthly income PLN 10,000, with sickness.
**Expected output:** Social: PLN 1,485.31. FP: PLN 115.01. Health: PLN 900.00. Total: PLN 2,500.32.

### Test 2 -- Ulga na start (month 3)
**Input:** Month 3, PIT-36, income PLN 8,000.
**Expected output:** Social: PLN 0. Health: PLN 720.00. Total: PLN 720.00.

### Test 3 -- Preferencyjne ZUS (month 10)
**Input:** Month 10, PIT-36L, income PLN 12,000, with sickness.
**Expected output:** Social: PLN 442.90. FP: PLN 0. Health: PLN 588.00. Total: PLN 1,030.90.

### Test 4 -- Mały ZUS Plus
**Input:** Prior-year revenue PLN 80,000, income PLN 40,000, 365 days active, PIT-36.
**Expected output:** Daily base = PLN 3,287.67. Social at 31.64%. Health on actual income.

### Test 5 -- Ryczałt, high revenue bracket
**Input:** Revenue PLN 400,000, PIT-28, standard ZUS.
**Expected output:** Social: PLN 1,485.31. Health: PLN 1,384.97. Total: PLN 2,870.28.

### Test 6 -- Concurrent employment
**Input:** Employed PLN 5,000/month, side business PLN 3,000, PIT-36.
**Expected output:** Social: PLN 0 (voluntary). Health: PLN 270.00. Total mandatory: PLN 270.00.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
