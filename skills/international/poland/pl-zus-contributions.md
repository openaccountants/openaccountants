---
name: pl-zus-contributions
description: Use this skill whenever asked about Polish ZUS (Zakład Ubezpieczeń Społecznych) social contributions for self-employed individuals. Trigger on phrases like "ZUS contributions", "składki ZUS", "Polish social insurance", "Mały ZUS Plus", "self-employed Poland contributions", "działalność gospodarcza ZUS", or any question about social/health insurance obligations for a self-employed client in Poland. Covers retirement 19.52%, disability 8%, sickness 2.45%, health 9%, and Mały ZUS Plus. ALWAYS read this skill before touching any Poland social contributions work.
---

# Poland ZUS Contributions -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Poland |
| Jurisdiction Code | PL |
| Primary Legislation | Ustawa o systemie ubezpieczeń społecznych (Social Insurance System Act, 13 Oct 1998) |
| Supporting Legislation | Ustawa o świadczeniach opieki zdrowotnej (Health Insurance Act); Ustawa Prawo przedsiębiorców |
| Tax Authority | ZUS (Zakład Ubezpieczeń Społecznych) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Polish doradca podatkowy |
| Validation Date | Pending |
| Skill Version | 1.0 |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

Before computing, you MUST know:

1. **Business registration** [T1] -- registered działalność gospodarcza (sole proprietorship)?
2. **Months in business** [T1] -- first 6 months? (Ulga na start) First 24 months after Ulga? (Preferencyjne ZUS)
3. **Prior-year revenue** [T1] -- determines eligibility for Mały ZUS Plus
4. **Health insurance basis** [T1] -- which tax form? (PIT-36, PIT-36L, PIT-28?)
5. **Voluntary sickness insurance?** [T1] -- chorobowe is optional for self-employed
6. **Any concurrent employment?** [T1] -- may exempt from certain ZUS obligations

**If months in business is unknown, STOP. Different regimes apply based on tenure.**

---

## Step 1: ZUS Contribution Tiers [T1]

**Legislation:** Art. 18a, 18c Ustawy o sus

Poland has FOUR contribution tiers for self-employed:

| Tier | Who | Social Contribution Base |
|------|-----|------------------------|
| 1. Ulga na start | First 6 months of activity | NO social contributions (only health) |
| 2. Preferencyjne ZUS | Months 7-30 (24 months after Ulga) | 30% of minimum wage |
| 3. Mały ZUS Plus | Revenue < PLN 120,000 in prior year + conditions | Based on prior-year income |
| 4. Standard (Duży ZUS) | All others | 60% of average forecasted wage |

---

## Step 2: Standard ZUS Rates (Duży ZUS, 2025) [T1]

**Legislation:** Art. 22 Ustawy o sus

### Social Insurance Contributions

| Component | Rate | Base: 60% avg wage = PLN 4,694.40/month (2025) | Monthly Amount |
|-----------|------|------------------------------------------------|----------------|
| Retirement (emerytalne) | 19.52% | PLN 4,694.40 | PLN 916.35 |
| Disability (rentowe) | 8.00% | PLN 4,694.40 | PLN 375.55 |
| Sickness (chorobowe) -- voluntary | 2.45% | PLN 4,694.40 | PLN 115.01 |
| Accident (wypadkowe) | 1.67% | PLN 4,694.40 | PLN 78.40 |
| **Total social (with sickness)** | **31.64%** | | **PLN 1,485.31** |
| **Total social (without sickness)** | **29.19%** | | **PLN 1,370.30** |

### Labour Fund (Fundusz Pracy)

| Component | Rate | Monthly |
|-----------|------|---------|
| Fundusz Pracy | 2.45% | PLN 115.01 |

Labour Fund is due when the contribution base exceeds the minimum wage.

### Health Insurance (Składka zdrowotna)

Health insurance rate and base depend on the tax form:

| Tax Form | Health Rate | Base |
|----------|------------|------|
| PIT-36 (tax scale, 12%/32%) | 9% | Actual monthly income (min = 75% of min wage) |
| PIT-36L (flat tax 19%) | 4.9% | Actual monthly income (min = 75% of min wage) |
| PIT-28 (ryczałt, lump-sum) | 9% | Fixed base by revenue bracket |

### Health Insurance -- Ryczałt Brackets (2025)

| Annual Revenue | Monthly Health Base | Monthly Health (9%) |
|----------------|--------------------|--------------------|
| Up to PLN 60,000 | 60% of avg wage | PLN 461.66 |
| PLN 60,001 -- 300,000 | 100% of avg wage | PLN 769.43 |
| Above PLN 300,000 | 180% of avg wage | PLN 1,384.97 |

---

## Step 3: Preferential ZUS (Months 7-30) [T1]

**Legislation:** Art. 18a Ustawy o sus

| Parameter | Value (2025) |
|-----------|-------------|
| Base | 30% of minimum wage = PLN 1,399.80/month |
| Retirement (19.52%) | PLN 273.24 |
| Disability (8.00%) | PLN 111.98 |
| Sickness (2.45%) | PLN 34.30 |
| Accident (1.67%) | PLN 23.38 |
| **Total social** | **PLN 442.90** |
| Fundusz Pracy | NOT required (base below minimum wage) |
| Health insurance | Separately at standard health rates |

---

## Step 4: Mały ZUS Plus [T1]

**Legislation:** Art. 18c Ustawy o sus

### Eligibility

- Revenue in prior year < PLN 120,000
- Activity for at least 60 days in prior year
- Not providing services to former employer
- Not used Mały ZUS Plus for 36 of last 60 months

### Base Calculation

```
annual_income = prior_year_income (profit, not revenue)
daily_base = annual_income × 30 / number_of_days_of_activity
monthly_base = daily_base × 30
monthly_base = clamp(30% of min_wage, monthly_base, 60% of avg_wage)
```

The base cannot be below Preferencyjne level (30% of min wage) or above Standard level (60% of avg wage).

---

## Step 5: Ulga na Start (First 6 Months) [T1]

**Legislation:** Art. 18 Prawo przedsiębiorców

- NO social insurance contributions for first 6 full calendar months
- Health insurance is still mandatory
- Client has no pension/disability/sickness coverage during this period
- Optional: client can voluntarily pay social contributions

---

## Step 6: Computation Steps [T1]

### Step 6.1 -- Determine tier

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

### Step 6.2 -- Calculate social contributions

```
social_base = base_for_tier
retirement = social_base × 19.52%
disability = social_base × 8.00%
sickness = social_base × 2.45%  # if opted in
accident = social_base × 1.67%
fundusz_pracy = social_base × 2.45%  # only if base >= minimum wage
total_social = retirement + disability + sickness + accident + fundusz_pracy
```

### Step 6.3 -- Calculate health insurance

```
IF tax_form == "PIT-36":
    health_base = max(actual_monthly_income, 75% of min_wage)
    health = health_base × 9%
ELIF tax_form == "PIT-36L":
    health_base = max(actual_monthly_income, 75% of min_wage)
    health = health_base × 4.9%
ELIF tax_form == "PIT-28":
    health = ryczałt_bracket_amount  # from bracket table
```

### Step 6.4 -- Total monthly ZUS

```
total_monthly = total_social + health
```

---

## Step 7: Payment Schedule [T1]

| Obligation | Due Date |
|------------|----------|
| Monthly ZUS declaration (DRA) | 20th of the following month |
| Payment of contributions | 20th of the following month |

- Payments via transfer to individual NRS (Numer Rachunku Składkowego) account
- Late payment: interest at 200% of Lombard rate / 365 x days late
- DRA filing via PUE ZUS (electronic platform)

---

## Step 8: Tax Deductibility [T1]

| Contribution | Deductible from Income Tax? | How? |
|-------------|---------------------------|------|
| Retirement (emerytalne) | YES | Deducted from income (business expense) or from tax |
| Disability (rentowe) | YES | Same |
| Sickness (chorobowe) | YES | Same |
| Accident (wypadkowe) | YES | Same |
| Fundusz Pracy | YES | Business expense |
| Health (zdrowotna) -- PIT-36 | Partially: 7.75% of base deductible from tax | NOT from income, from TAX directly |
| Health (zdrowotna) -- PIT-36L | Capped deduction from income (max PLN 12,900/year approx) | From income, not tax |
| Health (zdrowotna) -- PIT-28 | 50% deductible from revenue | From revenue |

---

## Step 9: Edge Case Registry

### EC1 -- Ulga na start, no social coverage [T1]
**Situation:** Client in month 4 of activity using Ulga na start.
**Resolution:** No social insurance. Only health insurance due. Flag: client has NO pension, disability, or sickness coverage. If client falls ill, no ZUS sickness benefit available.

### EC2 -- Switching from Preferencyjne to Mały ZUS Plus [T1]
**Situation:** Client finishing 24 months of Preferencyjne, prior-year revenue under PLN 120,000.
**Resolution:** Client can transition to Mały ZUS Plus if all eligibility conditions are met. Must register by 31 January of the year. Otherwise defaults to Standard ZUS.

### EC3 -- Concurrent full-time employment [T1]
**Situation:** Client is employed full-time (at least minimum wage) and runs a side business.
**Resolution:** If employment salary >= minimum wage: social contributions from business are voluntary (not mandatory). Health insurance is still mandatory from the business. Retirement/disability paid through employment.

### EC4 -- Services to former employer [T1]
**Situation:** Client left employment and provides same services as self-employed to former employer.
**Resolution:** In the first 24 months: Preferencyjne ZUS is NOT available. Ulga na start is NOT available. Client must pay Standard ZUS from day one. Mały ZUS Plus also excluded if services are to former employer.

### EC5 -- Multiple businesses [T1]
**Situation:** Client operates two separate działalności.
**Resolution:** ZUS contributions are paid only once, on the higher base. Not doubled for multiple businesses.

### EC6 -- Sickness during Ulga na start [T1]
**Situation:** Client gets sick during Ulga na start period.
**Resolution:** No ZUS sickness benefit (zasiłek chorobowy) is available. Client bears full financial risk. This is the trade-off of Ulga na start.

### EC7 -- Income below health minimum [T1]
**Situation:** Client on PIT-36 has monthly income of PLN 500.
**Resolution:** Health base = 75% of minimum wage (floor). Health contribution = PLN 3,499.50 x 9% = PLN 314.96/month. The minimum applies regardless of actual income.

### EC8 -- Cross-border EU worker [T2]
**Situation:** Client lives in Poland, performs some work in Germany.
**Resolution:** Under EU Regulation 883/2004, social insurance in one country. [T2] -- A1 certificate required.

---

## Step 10: Test Suite

### Test 1 -- Standard ZUS (Duży ZUS)
**Input:** Established business (>30 months), PIT-36 tax form, monthly income PLN 10,000, with voluntary sickness.
**Expected output:** Social: PLN 1,485.31. Fundusz Pracy: PLN 115.01. Health: PLN 10,000 x 9% = PLN 900.00. Total monthly: PLN 2,500.32.

### Test 2 -- Ulga na start (month 3)
**Input:** Month 3, PIT-36, income PLN 8,000.
**Expected output:** Social: PLN 0. Health: PLN 8,000 x 9% = PLN 720.00. Total: PLN 720.00.

### Test 3 -- Preferencyjne ZUS (month 10)
**Input:** Month 10, PIT-36L flat tax, income PLN 12,000, with sickness.
**Expected output:** Social: PLN 442.90. Fundusz Pracy: PLN 0 (base < min wage). Health: PLN 12,000 x 4.9% = PLN 588.00. Total: PLN 1,030.90.

### Test 4 -- Mały ZUS Plus
**Input:** Prior-year revenue PLN 80,000, prior-year income PLN 40,000, 365 days active, PIT-36.
**Expected output:** Daily base = PLN 40,000 x 30 / 365 = PLN 3,287.67. Monthly base = PLN 3,287.67 (within bounds). Social at 31.64% = PLN 1,039.80. Health on actual income.

### Test 5 -- Ryczałt, high revenue bracket
**Input:** Annual revenue PLN 400,000, ryczałt (PIT-28), standard ZUS.
**Expected output:** Social: PLN 1,485.31. Health: PLN 1,384.97/month (180% bracket). Total: PLN 2,870.28/month.

### Test 6 -- Concurrent employment
**Input:** Employed at PLN 5,000/month (above min wage), side business income PLN 3,000, PIT-36.
**Expected output:** Social: PLN 0 (voluntary, employment covers minimum). Health: PLN 3,000 x 9% = PLN 270.00. Total mandatory: PLN 270.00.

---

## PROHIBITIONS

- NEVER compute health insurance without knowing the tax form (PIT-36 vs PIT-36L vs PIT-28) -- rates differ
- NEVER apply Ulga na start or Preferencyjne to clients providing services to their former employer
- NEVER forget that sickness insurance (chorobowe) is VOLUNTARY for self-employed
- NEVER ignore the 36/60 month limit on Mały ZUS Plus usage
- NEVER state health contributions are fully tax-deductible -- deductibility depends on tax form and has limits
- NEVER apply Fundusz Pracy when the contribution base is below the minimum wage
- NEVER double social contributions for clients with multiple businesses
- NEVER present Ulga na start as risk-free -- the client has NO social coverage during this period
- NEVER advise on cross-border situations without flagging for reviewer

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
