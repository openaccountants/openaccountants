---
name: ke-nhif-nssf
description: Use this skill whenever asked about Kenyan social contributions for self-employed individuals -- SHIF (formerly NHIF) health insurance and NSSF pension. Trigger on phrases like "NHIF self-employed", "SHIF contributions", "NSSF Tier I", "NSSF Tier II", "Kenya social security", "Kenya health insurance", or any question about Kenyan social contribution obligations for self-employed persons. Covers the SHIF 2.75% rate (replacing NHIF brackets from October 2024), NSSF Tier I/II structure, voluntary registration, and edge cases. ALWAYS read this skill before touching any Kenyan social contribution work.
---

# Kenya SHIF (formerly NHIF) and NSSF Contributions -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Kenya |
| Jurisdiction Code | KE |
| Primary Legislation | Social Health Insurance Act 2023 (SHIF), NSSF Act 2013 |
| Supporting Legislation | NHIF Act 1998 (legacy, replaced by SHIF Oct 2024), Employment Act 2007 |
| Tax Authority | SHA (Social Health Authority, replacing NHIF), NSSF (National Social Security Fund) |
| Rate Publisher | SHA (SHIF rates), NSSF (contribution tables) |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: SHIF rate, NSSF Tier I/II calculation, payment schedule. Tier 2: informal sector registration, income declaration disputes, transitional rules. Tier 3: court challenges to SHIF, bilateral agreements, disability claims. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any contribution figure, you MUST know:

1. **Employment status** [T1] -- self-employed, informal sector, or voluntary contributor
2. **Monthly declared income** [T1] -- determines SHIF and NSSF amounts
3. **Is client registered with SHA (formerly NHIF)?** [T1] -- registration status
4. **Is client registered with NSSF?** [T1] -- registration status
5. **Any formal employment alongside self-employment?** [T1] -- dual status rules
6. **Sector** [T2] -- formal vs. informal (affects NSSF enforcement)

**If monthly income is unknown, request an estimate. SHIF uses declared household income for self-employed.**

---

## Step 1: SHIF (Social Health Insurance Fund) -- Replacing NHIF [T1]

**Legislation:** Social Health Insurance Act 2023 (effective October 2024)

### Key Change: NHIF to SHIF

| Item | Old System (NHIF) | New System (SHIF, from Oct 2024) |
|------|-------------------|----------------------------------|
| Rate structure | Fixed bracket-based (KES 150-1,700/month) | Percentage-based: 2.75% of income |
| Self-employed | Flat KES 500/month | 2.75% of declared household income |
| Minimum | KES 150/month | KES 300/month |
| Maximum | KES 1,700/month | No cap (percentage-based) |

### SHIF Calculation for Self-Employed (2025)

```
shif_monthly = max(declared_monthly_income × 2.75%, KES 300)
```

### Legacy NHIF Brackets (for reference only -- pre-October 2024)

| Monthly Income (KES) | Monthly Premium (KES) |
|----------------------|----------------------|
| Up to 5,999 | 150 |
| 6,000 - 7,999 | 300 |
| 8,000 - 11,999 | 400 |
| 12,000 - 14,999 | 500 |
| 15,000 - 19,999 | 600 |
| 20,000 - 24,999 | 750 |
| 25,000 - 29,999 | 850 |
| 30,000 - 34,999 | 900 |
| 35,000 - 39,999 | 950 |
| 40,000 - 44,999 | 1,000 |
| 45,000 - 49,999 | 1,100 |
| 50,000 - 59,999 | 1,200 |
| 60,000 - 69,999 | 1,300 |
| 70,000 - 79,999 | 1,400 |
| 80,000 - 89,999 | 1,500 |
| 90,000 - 99,999 | 1,600 |
| 100,000+ | 1,700 |

**These brackets are NO LONGER APPLICABLE from October 2024. Use the 2.75% SHIF rate.**

---

## Step 2: NSSF Contributions [T1]

**Legislation:** NSSF Act 2013

### Tier Structure (effective February 2025)

| Tier | Earnings Band | Employee Contribution | Employer Contribution |
|------|--------------|----------------------|----------------------|
| Tier I | Up to KES 8,000 (Lower Earnings Limit) | 6% of pensionable earnings | 6% of pensionable earnings |
| Tier II | KES 8,001 to KES 72,000 (Upper Earnings Limit) | 6% of pensionable earnings in this band | 6% of pensionable earnings in this band |

### Self-Employed NSSF

For self-employed individuals:

| Item | Detail |
|------|--------|
| Registration | Voluntary but strongly encouraged |
| Contribution | Same structure as employed -- 6% of declared pensionable earnings |
| Self-employed pays | Both "employee" and "employer" portions (total 12%) |
| Minimum monthly (Tier I only) | KES 480 (6% x KES 8,000) x 2 = KES 960 |
| Maximum monthly (Tier I + II) | KES 4,320 (6% x KES 72,000) x 2 = KES 8,640 |

### Calculation

```
tier_i = min(declared_income, KES 8,000) × 6% × 2
tier_ii = max(0, min(declared_income, KES 72,000) - KES 8,000) × 6% × 2
total_nssf = tier_i + tier_ii
```

### Examples

| Declared Monthly Income | Tier I | Tier II | Total NSSF |
|------------------------|--------|---------|------------|
| KES 5,000 | KES 600 | KES 0 | KES 600 |
| KES 8,000 | KES 960 | KES 0 | KES 960 |
| KES 30,000 | KES 960 | KES 2,640 | KES 3,600 |
| KES 72,000 | KES 960 | KES 7,680 | KES 8,640 |
| KES 150,000 | KES 960 | KES 7,680 | KES 8,640 (capped) |

---

## Step 3: Payment Schedule [T1]

| Contribution | Due Date | Frequency |
|-------------|----------|-----------|
| SHIF | 9th of following month | Monthly |
| NSSF | 9th of following month | Monthly |

### Payment Channels

| Channel | Detail |
|---------|--------|
| M-Pesa | Paybill number for SHA / NSSF |
| Bank | Direct deposit to SHA / NSSF accounts |
| Online | SHA portal, NSSF portal |

---

## Step 4: Registration [T1]

| Requirement | SHIF | NSSF |
|-------------|------|------|
| Mandatory? | Yes (all Kenyan residents) | Voluntary for self-employed (mandatory for formal employees) |
| Registration | SHA portal or office | NSSF portal or office |
| ID required | National ID or passport | National ID or passport |
| KRA PIN | Required | Required |
| Dependants | Register dependants for health cover | N/A |

---

## Step 5: Interaction with Income Tax [T1]

| Question | Answer |
|----------|--------|
| Is SHIF deductible? | YES -- health insurance contributions qualify for relief under ITA |
| Is NSSF deductible? | YES -- pension contributions qualify for tax relief up to KES 30,000/month |
| Insurance relief | Available on SHIF contributions (15% of premiums, capped at KES 60,000/year) |
| Where reported? | Annual income tax return (iTax) |

---

## Step 6: Penalties [T1]

| Penalty | SHIF | NSSF |
|---------|------|------|
| Late payment | 2.5% per month on outstanding amount | 5% of contribution per month |
| Non-registration | Denial of healthcare services | No immediate penalty but loss of benefits |
| Persistent default | Legal action by SHA | Legal action by NSSF |

---

## Step 7: Edge Case Registry

### EC1 -- Informal sector worker with irregular income [T2]
**Situation:** Jua kali (informal sector) worker with no fixed monthly income.
**Resolution:** SHIF requires declaration of household income. If income varies, declare average monthly estimate. Minimum KES 300/month applies. [T2] flag for reviewer -- how to estimate for PILA-equivalent declaration.

### EC2 -- Self-employed with formal employment [T1]
**Situation:** Client is employed (employer deducts SHIF/NSSF) and also self-employed.
**Resolution:** Employer handles SHIF/NSSF for employment income. Self-employed income may require additional SHIF contribution on the additional income. NSSF is already covered if employment earnings exceed KES 72,000.

### EC3 -- Transition from NHIF to SHIF [T2]
**Situation:** Client was paying KES 500/month NHIF and asks about new rates.
**Resolution:** From October 2024, NHIF brackets replaced by SHIF 2.75%. If client's declared income is KES 20,000, new rate = KES 550 (was KES 750 under NHIF). Transition may involve re-registration with SHA. [T2] flag -- verify transition status.

### EC4 -- Non-citizen resident [T2]
**Situation:** Foreign national living and working in Kenya as self-employed.
**Resolution:** SHIF applies to all residents. NSSF registration is voluntary for self-employed. Work permit holders should register. [T2] flag for reviewer to confirm residency and permit status.

### EC5 -- Client above NSSF Upper Earnings Limit [T1]
**Situation:** Client earns KES 200,000/month.
**Resolution:** NSSF capped at KES 72,000 Upper Earnings Limit. Maximum total NSSF = KES 8,640. SHIF = KES 200,000 x 2.75% = KES 5,500 (no cap).

### EC6 -- Court challenges to SHIF [T3]
**Situation:** Client references ongoing court cases challenging the constitutionality of SHIF.
**Resolution:** [T3] Escalate. There have been multiple court challenges to the Social Health Insurance Act. Status of these challenges affects enforceability. Do not advise on constitutional matters.

### EC7 -- Voluntary NSSF contributor wanting to withdraw [T2]
**Situation:** Self-employed client wants to stop NSSF contributions.
**Resolution:** Voluntary contributors may stop contributing but cannot withdraw accumulated funds until retirement age (60) or qualifying event. [T2] flag for reviewer on withdrawal rules.

### EC8 -- Household income declaration for SHIF [T2]
**Situation:** SHIF is based on "household income" but client's spouse also earns.
**Resolution:** SHIF is assessed on household income for self-employed in informal sector. The definition of household income and how spousal income is factored is still being clarified by SHA. [T2] flag for reviewer.

---

## Step 8: Reviewer Escalation Protocol

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

## Step 9: Test Suite

### Test 1 -- Standard self-employed, moderate income
**Input:** Declared monthly income KES 50,000. Registered SHIF and voluntary NSSF. 2025.
**Expected output:** SHIF = KES 50,000 x 2.75% = KES 1,375. NSSF Tier I = KES 960, Tier II = (50,000 - 8,000) x 12% = KES 5,040. Total NSSF = KES 6,000. Grand total = KES 7,375.

### Test 2 -- Minimum income
**Input:** Declared monthly income KES 5,000. SHIF only.
**Expected output:** SHIF = KES 5,000 x 2.75% = KES 137.50, but minimum KES 300 applies. SHIF = KES 300.

### Test 3 -- High income, NSSF capped
**Input:** Declared monthly income KES 200,000. SHIF + NSSF. 2025.
**Expected output:** SHIF = KES 5,500 (2.75% x 200,000). NSSF = KES 8,640 (capped at UEL KES 72,000). Total = KES 14,140.

### Test 4 -- Employed + self-employed dual status
**Input:** Employment salary KES 80,000 (employer handles). Self-employed income KES 40,000.
**Expected output:** Employer handles SHIF/NSSF on KES 80,000. Additional SHIF may be due on self-employed income: KES 40,000 x 2.75% = KES 1,100. NSSF already at maximum through employment.

### Test 5 -- Informal sector, low income
**Input:** Jua kali worker, estimated income KES 10,000/month. SHIF only.
**Expected output:** SHIF = KES 10,000 x 2.75% = KES 275, but minimum KES 300 applies. SHIF = KES 300.

### Test 6 -- NSSF only, no SHIF yet
**Input:** Self-employed, KES 30,000/month, voluntary NSSF only, has not registered for SHIF.
**Expected output:** NSSF = Tier I (KES 960) + Tier II (22,000 x 12% = KES 2,640) = KES 3,600. Advise client to register for SHIF (mandatory for all residents).

### Test 7 -- At NSSF Lower Earnings Limit
**Input:** Declared income KES 8,000/month. NSSF only.
**Expected output:** Tier I only. NSSF = KES 8,000 x 12% = KES 960. No Tier II.

---

## PROHIBITIONS

- NEVER use the old NHIF bracket table for periods from October 2024 onward -- SHIF 2.75% applies
- NEVER tell a self-employed client that NSSF is mandatory -- it is voluntary for self-employed (but recommended)
- NEVER ignore the KES 300 SHIF minimum -- even at very low income, minimum applies
- NEVER assume NSSF contributions are uncapped -- the Upper Earnings Limit (KES 72,000) caps the base
- NEVER conflate SHIF household income with individual income without clarifying the SHA definition
- NEVER advise on the constitutionality or enforceability of SHIF -- court challenges are ongoing [T3]
- NEVER present old NSSF rates (pre-February 2025) -- Tier I limit increased to KES 8,000 and Tier II to KES 72,000
- NEVER compute penalties without confirming current SHA/NSSF penalty rates
- NEVER assume foreign residents are exempt from SHIF -- residency, not citizenship, triggers obligation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
