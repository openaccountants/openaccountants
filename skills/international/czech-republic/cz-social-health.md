---
name: cz-social-health
description: Use this skill whenever asked about Czech self-employed social and health insurance contributions. Trigger on phrases like "OSSZ", "Czech social insurance", "zdravotní pojištění OSVČ", "sociální pojištění", "paušální daň", "Czech self-employed contributions", "přehled OSSZ", or any question about social/health insurance obligations for a self-employed client in the Czech Republic. Covers social insurance (29.2% of 50% base), health insurance (13.5% of 50% base), minimum advances, and paušální daň. ALWAYS read this skill before touching any Czech social contributions work.
---

# Czech Social + Health Insurance -- Self-Employed (OSVČ) Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Czech Republic |
| Jurisdiction Code | CZ |
| Primary Legislation | Zákon č. 589/1992 Sb. (Social Insurance Premiums Act); Zákon č. 592/1992 Sb. (Health Insurance Premiums Act) |
| Supporting Legislation | Zákon č. 155/1995 Sb. (Pension Insurance Act); Zákon č. 187/2006 Sb. (Sickness Insurance Act) |
| Tax Authority | ČSSZ (Česká správa sociálního zabezpečení) for social; health insurance companies for health |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Czech daňový poradce |
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

1. **Is self-employment the main activity (hlavní) or secondary (vedlejší)?** [T1] -- thresholds differ significantly
2. **Gross income (příjmy) from self-employment** [T1]
3. **Deductible expenses** [T1] -- actual (skutečné) or flat-rate (paušální)?
4. **Which flat-rate percentage?** [T1] -- 40%, 60%, or 80% depending on activity type
5. **Voluntary sickness insurance?** [T1] -- optional for OSVČ
6. **Considering paušální daň (lump-sum tax)?** [T1] -- available if turnover < CZK 2,000,000

**If hlavní vs vedlejší is unknown, STOP. Minimum advance payments depend on this classification.**

---

## Step 1: Assessment Base [T1]

**Legislation:** §5b Zákona č. 589/1992 Sb.; §3a Zákona č. 592/1992 Sb.

```
daňový_základ = gross_income - expenses  (either actual or flat-rate)
assessment_base (vyměřovací základ) = daňový_základ × 50%
```

The assessment base is **50% of the difference between income and expenses** (the "profit base").

### Minimum Assessment Base (2025)

| Category | Social Insurance Min Monthly | Health Insurance Min Monthly |
|----------|-----------------------------|-----------------------------|
| Hlavní (main) activity | CZK 11,478 | CZK 23,041 |
| Vedlejší (secondary) activity | CZK 4,591 | No minimum (pay on actual) |

Note: Health insurance minimum for hlavní is set at 50% of the average wage. Social insurance minimum is 25% of the average wage.

---

## Step 2: Rates (2025) [T1]

### Social Insurance (ČSSZ)

| Component | Rate |
|-----------|------|
| Pension insurance (důchodové pojištění) | 28.00% |
| State employment policy (příspěvek na SPZ) | 1.20% |
| **Total social insurance** | **29.20%** |
| Sickness insurance (voluntary) | 2.10% |

### Health Insurance

| Component | Rate |
|-----------|------|
| Health insurance (zdravotní pojištění) | **13.50%** |

### Combined Mandatory Rates

| Component | Rate | Applied to |
|-----------|------|-----------|
| Social insurance | 29.20% | 50% of profit |
| Health insurance | 13.50% | 50% of profit |
| **Total** | **42.70%** | of 50% profit = **21.35% of total profit** |

---

## Step 3: Computation Steps [T1]

### Step 3.1 -- Calculate profit and assessment base

```
profit = gross_income - expenses
assessment_base = profit × 50%
assessment_base = max(assessment_base, minimum_assessment_base)
```

### Step 3.2 -- Annual social insurance

```
social_annual = assessment_base × 29.20%
social_annual = max(social_annual, minimum_monthly_social × 12)
```

Maximum assessment base for social insurance: CZK 2,234,736/year (48x average wage). No social insurance on income above this.

### Step 3.3 -- Annual health insurance

```
health_annual = assessment_base × 13.50%
health_annual = max(health_annual, minimum_monthly_health × 12)
```

No maximum assessment base for health insurance -- it applies without limit.

### Step 3.4 -- Monthly advance payments

```
monthly_social_advance = max(social_annual / 12, minimum_social_advance)
monthly_health_advance = max(health_annual / 12, minimum_health_advance)
```

### Step 3.5 -- Optional sickness insurance

```
IF voluntary_sickness:
    sickness_monthly = assessment_base_monthly × 2.10%
    # Minimum: CZK 216/month (2025)
```

---

## Step 4: Advance Payments and Filing [T1]

**Legislation:** §14a Zákona č. 589/1992 Sb.

### Minimum Monthly Advances (2025)

| Category | Social (monthly) | Health (monthly) |
|----------|-------------------|------------------|
| Hlavní OSVČ | CZK 3,852 | CZK 2,968 |
| Vedlejší OSVČ | CZK 1,413 | Actual (no minimum if below threshold) |

### Payment Schedule

- Monthly advances are due by the **20th of the following month** (for social) and by the **8th of the following month** (for health)
- Annual reconciliation via Přehled (overview) filed with ČSSZ and health insurance company
- Přehled deadline: **within 1 month of income tax filing deadline** (typically by 1 May or 1 July if filed by advisor)

### Vedlejší Activity Threshold

Vedlejší OSVČ need not pay social insurance if annual profit is below the threshold:

| Year | Threshold |
|------|-----------|
| 2025 | CZK 105,520 |

If profit is below this threshold, vedlejší OSVČ pays no social insurance (pension is voluntary). Health insurance is still due on actual income.

---

## Step 5: Paušální Daň (Lump-Sum Tax) [T1]

**Legislation:** §7a Zákona č. 586/1992 Sb. (as amended)

### Eligibility

- Annual turnover (příjmy) up to CZK 2,000,000
- Not a VAT payer (or only VAT-exempt supplies)
- Hlavní OSVČ only
- No employment income above exempt threshold

### 2025 Bands

| Band | Turnover Limit | Monthly Payment | Includes |
|------|----------------|-----------------|----------|
| Band 1 | Up to CZK 1,000,000 | CZK 7,498 | Income tax + social + health |
| Band 2 | CZK 1,000,001 -- 1,500,000 | CZK 16,745 | Income tax + social + health |
| Band 3 | CZK 1,500,001 -- 2,000,000 | CZK 27,139 | Income tax + social + health |

- Payment due by the 20th of each month
- No annual tax return required
- Pension entitlements are maintained

---

## Step 6: Tax Deductibility [T1]

| Question | Answer |
|----------|--------|
| Are social insurance contributions deductible? | Pension and state employment policy: NO (not deductible from income tax base) |
| Is health insurance deductible? | NO -- not deductible from income tax base |
| Are sickness insurance contributions deductible? | NO |
| Note | Czech contributions are NOT deductible from the income tax base. They are a separate obligation. |

---

## Step 7: Edge Case Registry

### EC1 -- First year of activity (hlavní) [T1]
**Situation:** Client started self-employment in September 2025.
**Resolution:** Pay minimum monthly advances from the month of registration. Pro-rate the annual reconciliation. No prior-year base available, so minimum advances apply until first Přehled is filed.

### EC2 -- Concurrent employment (vedlejší) [T1]
**Situation:** Client is employed full-time and has a side self-employment.
**Resolution:** Self-employment is vedlejší. If annual profit < CZK 105,520, no social insurance obligation (pension is voluntary). Health insurance paid on actual income (no minimum).

### EC3 -- Flat-rate expenses vs actual expenses [T1]
**Situation:** Client is unsure which expense method to use.
**Resolution:** Flat-rate percentages: 80% (agriculture, crafts), 60% (trade/business), 40% (other business), 30% (rental). Flat-rate is capped at CZK 1,600,000 (80%), CZK 1,200,000 (60%), CZK 800,000 (40%), CZK 600,000 (30%). Choice affects both income tax and the social/health insurance base.

### EC4 -- Exceeding social insurance maximum base [T1]
**Situation:** Client's assessment base exceeds CZK 2,234,736.
**Resolution:** Social insurance is capped at this maximum base. Health insurance has NO cap -- continues at 13.5% without limit.

### EC5 -- Voluntary sickness insurance [T1]
**Situation:** Client wants sickness benefit coverage.
**Resolution:** Self-employed can opt in to voluntary sickness insurance at 2.10% of the assessment base (minimum CZK 216/month). Provides sick pay from day 15 of illness. Must opt in actively.

### EC6 -- Switching from vedlejší to hlavní mid-year [T2]
**Situation:** Client's employment ends in June, self-employment continues as hlavní.
**Resolution:** From July, minimum advances increase to hlavní level. Annual reconciliation will apply hlavní minimums pro-rata for months classified as hlavní. [T2] -- confirm exact pro-rata calculation with ČSSZ.

### EC7 -- Paušální daň eligibility lost mid-year [T1]
**Situation:** Client registered for paušální daň but turnover exceeded CZK 2,000,000.
**Resolution:** Client exits paušální daň regime for the entire year. Must file regular income tax return and pay social/health on standard basis. All paušální payments made are credited.

### EC8 -- Non-resident OSVČ [T2]
**Situation:** Client is an EU citizen working as self-employed in the Czech Republic but resident elsewhere.
**Resolution:** Social/health insurance obligations depend on where the client is socially insured under EU Regulation 883/2004. [T2] -- A1 certificate required.

---

## Step 8: Test Suite

### Test 1 -- Standard hlavní, mid-range income
**Input:** Gross income CZK 1,200,000, flat-rate expenses 60%, hlavní, age 35.
**Expected output:** Expenses: CZK 720,000. Profit: CZK 480,000. Assessment base: CZK 240,000. Social: CZK 240,000 x 29.2% = CZK 70,080. Health: CZK 240,000 x 13.5% = CZK 32,400. Total: CZK 102,480/year. Monthly advances: social CZK 5,840, health CZK 2,700.

### Test 2 -- Minimum advances (hlavní, low income)
**Input:** Gross income CZK 300,000, flat-rate expenses 60%, hlavní, age 28.
**Expected output:** Profit: CZK 120,000. Assessment base: CZK 60,000 (below annual minimum). Apply monthly minimums. Social: CZK 3,852/month x 12 = CZK 46,224. Health: CZK 2,968/month x 12 = CZK 35,616. Total: CZK 81,840.

### Test 3 -- Vedlejší below threshold
**Input:** Gross income CZK 200,000, flat-rate expenses 60%, vedlejší, age 32.
**Expected output:** Profit: CZK 80,000. Below CZK 105,520 threshold. Social insurance: CZK 0 (voluntary). Health: CZK 40,000 x 13.5% = CZK 5,400.

### Test 4 -- High income, social cap applies
**Input:** Gross income CZK 8,000,000, actual expenses CZK 2,000,000, hlavní, age 45.
**Expected output:** Profit: CZK 6,000,000. Assessment base: CZK 3,000,000. Social capped at CZK 2,234,736 x 29.2% = CZK 652,543. Health: CZK 3,000,000 x 13.5% = CZK 405,000 (no cap). Total: CZK 1,057,543.

### Test 5 -- Paušální daň Band 1
**Input:** Turnover CZK 800,000, hlavní, not VAT registered.
**Expected output:** Eligible for Band 1. Monthly payment: CZK 7,498. Annual total: CZK 89,976. No tax return needed.

### Test 6 -- First year with minimum advances
**Input:** Started October 2025, hlavní, no prior income.
**Expected output:** Oct-Dec: minimum advances. Social: CZK 3,852 x 3 = CZK 11,556. Health: CZK 2,968 x 3 = CZK 8,904. Total for 3 months: CZK 20,460.

---

## PROHIBITIONS

- NEVER compute without knowing hlavní vs vedlejší status -- minimums differ dramatically
- NEVER forget that the assessment base is 50% of profit, not 50% of gross income
- NEVER state that Czech social/health contributions are tax-deductible -- they are NOT
- NEVER ignore the social insurance maximum cap at CZK 2,234,736
- NEVER forget that health insurance has NO maximum cap
- NEVER apply vedlejší minimums to a hlavní OSVČ
- NEVER advise on paušální daň without verifying all eligibility conditions
- NEVER present advance payment amounts as final -- annual reconciliation via Přehled determines the actual liability
- NEVER confuse flat-rate expense percentages -- 80%/60%/40%/30% depend on activity type

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
