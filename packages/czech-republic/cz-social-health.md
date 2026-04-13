---
name: cz-social-health
description: Use this skill whenever asked about Czech self-employed social and health insurance contributions. Trigger on phrases like "OSSZ", "Czech social insurance", "zdravotní pojištění OSVČ", "sociální pojištění", "paušální daň", "Czech self-employed contributions", "přehled OSSZ", or any question about social/health insurance obligations for a self-employed client in the Czech Republic. Covers social insurance (29.2% of 50% base), health insurance (13.5% of 50% base), minimum advances, and paušální daň. ALWAYS read this skill before touching any Czech social contributions work.
version: 2.0
---

# Czech Social + Health Insurance -- Self-Employed (OSVČ) Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Czech Republic |
| Authority | ČSSZ (social); health insurance companies (health) |
| Primary legislation | Zákon č. 589/1992 Sb. (Social); Zákon č. 592/1992 Sb. (Health) |
| Supporting legislation | Zákon č. 155/1995 Sb. (Pension); Zákon č. 187/2006 Sb. (Sickness) |
| Assessment base | 50% of profit (income minus expenses) |
| Social insurance rate | 29.20% of assessment base |
| Health insurance rate | 13.50% of assessment base |
| Combined effective rate | ~21.35% of total profit |
| Social max base (2025) | CZK 2,234,736/year |
| Health max base | None (no cap) |
| Min social advance (hlavní) | CZK 3,852/month |
| Min health advance (hlavní) | CZK 2,968/month |
| Vedlejší social threshold | CZK 105,520/year profit |
| Paušální daň Band 1 | CZK 7,498/month (turnover <= CZK 1M) |
| Currency | CZK only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Czech daňový poradce |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Is self-employment hlavní (main) or vedlejší (secondary)?** -- thresholds differ significantly
2. **Gross income (příjmy) from self-employment**
3. **Deductible expenses** -- actual (skutečné) or flat-rate (paušální)?
4. **Which flat-rate percentage?** -- 40%, 60%, or 80% depending on activity
5. **Voluntary sickness insurance?** -- optional for OSVČ
6. **Considering paušální daň?** -- available if turnover < CZK 2,000,000

**If hlavní vs vedlejší is unknown, STOP.**

### Refusal catalogue

**R-CZ-SOC-1 -- Non-resident OSVČ.** Trigger: EU citizen working as self-employed in Czech Republic but resident elsewhere. Message: "Social/health obligations depend on EU Regulation 883/2004. A1 certificate required. Escalate."

### Prohibitions

- NEVER compute without knowing hlavní vs vedlejší -- minimums differ dramatically
- NEVER forget that the assessment base is 50% of profit, not 50% of gross income
- NEVER state that Czech social/health contributions are tax-deductible -- they are NOT
- NEVER ignore the social insurance maximum cap at CZK 2,234,736
- NEVER forget that health insurance has NO maximum cap
- NEVER apply vedlejší minimums to a hlavní OSVČ
- NEVER advise on paušální daň without verifying all eligibility conditions
- NEVER present advance payments as final -- annual reconciliation via Přehled determines actual liability
- NEVER confuse flat-rate expense percentages -- 80%/60%/40%/30% depend on activity type

---

## Section 3 -- Assessment base

**Legislation:** Section 5b Zákona č. 589/1992 Sb.; Section 3a Zákona č. 592/1992 Sb.

```
profit = gross_income - expenses (actual or flat-rate)
assessment_base = profit x 50%
```

### Flat-rate expense percentages

| Activity | Flat-rate % | Cap |
|---|---|---|
| Agriculture, crafts | 80% | CZK 1,600,000 |
| Trade/business | 60% | CZK 1,200,000 |
| Other business | 40% | CZK 800,000 |
| Rental | 30% | CZK 600,000 |

---

## Section 4 -- Rates and thresholds (2025)

### Social insurance (ČSSZ)

| Component | Rate |
|---|---|
| Pension (důchodové pojištění) | 28.00% |
| State employment policy (příspěvek na SPZ) | 1.20% |
| **Total social** | **29.20%** |
| Sickness (voluntary) | 2.10% |

### Health insurance

| Component | Rate |
|---|---|
| Health (zdravotní pojištění) | **13.50%** |

### Minimum monthly advances (2025)

| Category | Social | Health |
|---|---|---|
| Hlavní OSVČ | CZK 3,852 | CZK 2,968 |
| Vedlejší OSVČ | CZK 1,413 | Actual (no minimum) |

### Vedlejší threshold

Vedlejší OSVČ pay no social insurance if annual profit < CZK 105,520. Health is still due on actual income.

### Paušální daň (lump-sum tax)

| Band | Turnover limit | Monthly payment |
|---|---|---|
| Band 1 | Up to CZK 1,000,000 | CZK 7,498 |
| Band 2 | CZK 1,000,001 -- 1,500,000 | CZK 16,745 |
| Band 3 | CZK 1,500,001 -- 2,000,000 | CZK 27,139 |

Eligibility: turnover up to CZK 2,000,000, not VAT payer, hlavní OSVČ only. No annual tax return required.

---

## Section 5 -- Computation steps

### Step 5.1 -- Calculate profit and assessment base

```
profit = gross_income - expenses
assessment_base = profit x 50%
assessment_base = max(assessment_base, minimum_assessment_base)
```

### Step 5.2 -- Annual social insurance

```
social_annual = assessment_base x 29.20%
social_annual = max(social_annual, minimum_monthly_social x 12)
```

Maximum assessment base for social: CZK 2,234,736/year.

### Step 5.3 -- Annual health insurance

```
health_annual = assessment_base x 13.50%
health_annual = max(health_annual, minimum_monthly_health x 12)
```

No maximum for health.

### Step 5.4 -- Monthly advance payments

```
monthly_social_advance = max(social_annual / 12, minimum_social_advance)
monthly_health_advance = max(health_annual / 12, minimum_health_advance)
```

---

## Section 6 -- Payment schedule and tax deductibility

### Payment schedule

- Social advances due by the **20th of the following month**
- Health advances due by the **8th of the following month**
- Annual reconciliation via Přehled filed with ČSSZ and health insurance company
- Přehled deadline: within 1 month of income tax filing deadline (typically by 1 May or 1 July if filed by advisor)

### Tax deductibility

| Question | Answer |
|---|---|
| Are social contributions deductible? | NO |
| Is health insurance deductible? | NO |
| Are sickness contributions deductible? | NO |

Czech contributions are NOT deductible from the income tax base. They are a separate obligation.

---

## Section 7 -- Voluntary sickness and special situations

### Voluntary sickness insurance

Self-employed can opt in at 2.10% of assessment base (minimum CZK 216/month). Provides sick pay from day 15 of illness.

### Switching from vedlejší to hlavní mid-year

From the month classification changes, minimum advances increase to hlavní level. Annual reconciliation applies hlavní minimums pro-rata. Flag for reviewer to confirm exact calculation with ČSSZ.

### Paušální daň eligibility lost mid-year

Client exits paušální daň regime for the entire year. Must file regular income tax return and pay social/health on standard basis. All paušální payments credited.

---

## Section 8 -- Edge case registry

### EC1 -- First year of activity (hlavní)
**Situation:** Started self-employment in September 2025.
**Resolution:** Minimum advances from registration month. No prior-year base available.

### EC2 -- Concurrent employment (vedlejší)
**Situation:** Employed full-time, side self-employment.
**Resolution:** Vedlejší. If profit < CZK 105,520, no social insurance (voluntary). Health on actual income.

### EC3 -- High income, social cap applies
**Situation:** Assessment base exceeds CZK 2,234,736.
**Resolution:** Social capped. Health continues at 13.5% without limit.

### EC4 -- Voluntary sickness insurance
**Situation:** Client wants sickness benefit coverage.
**Resolution:** Opt in at 2.10%, minimum CZK 216/month. Must opt in actively.

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
Action Required: Qualified daňový poradce must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified daňový poradce. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard hlavní, mid-range
**Input:** Gross CZK 1,200,000, flat-rate 60%, hlavní, age 35.
**Expected output:** Expenses CZK 720,000. Profit CZK 480,000. Base CZK 240,000. Social CZK 70,080. Health CZK 32,400. Total CZK 102,480. Monthly: social CZK 5,840, health CZK 2,700.

### Test 2 -- Minimum advances (hlavní, low income)
**Input:** Gross CZK 300,000, flat-rate 60%, hlavní.
**Expected output:** Profit CZK 120,000. Base CZK 60,000 (below annual minimum). Social CZK 46,224. Health CZK 35,616. Total CZK 81,840.

### Test 3 -- Vedlejší below threshold
**Input:** Gross CZK 200,000, flat-rate 60%, vedlejší.
**Expected output:** Profit CZK 80,000. Below CZK 105,520. Social CZK 0. Health CZK 5,400.

### Test 4 -- High income, social cap
**Input:** Gross CZK 8,000,000, actual expenses CZK 2,000,000, hlavní.
**Expected output:** Profit CZK 6,000,000. Base CZK 3,000,000. Social capped at CZK 652,543. Health CZK 405,000. Total CZK 1,057,543.

### Test 5 -- Paušální daň Band 1
**Input:** Turnover CZK 800,000, hlavní, not VAT registered.
**Expected output:** Band 1. Monthly CZK 7,498. Annual CZK 89,976.

### Test 6 -- First year with minimum advances
**Input:** Started October 2025, hlavní.
**Expected output:** Social CZK 11,556 (3 months). Health CZK 8,904. Total CZK 20,460.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
