---
name: at-svs-contributions
description: Use this skill whenever asked about Austrian SVS (Sozialversicherungsanstalt der Selbständigen) social insurance contributions for self-employed individuals. Trigger on phrases like "SVS contributions", "Austrian social insurance", "GSVG", "self-employed Austria contributions", "Pensionsversicherung self-employed", "SVS Vorschreibung", or any question about social insurance obligations for a self-employed client in Austria. Covers pension (18.5%), health (6.8%), accident (flat monthly), and Selbständigenvorsorge. ALWAYS read this skill before touching any Austria social contributions work.
---

# Austria SVS Social Insurance Contributions -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Austria |
| Jurisdiction Code | AT |
| Primary Legislation | GSVG (Gewerbliches Sozialversicherungsgesetz) |
| Supporting Legislation | ASVG; FSVG (Freiberuflich); BSVG (Farmers) |
| Tax Authority | SVS (Sozialversicherungsanstalt der Selbständigen) |
| Rate Publisher | SVS (publishes annual contribution tables) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Austrian Steuerberater or Wirtschaftsprüfer |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate calculation, min/max bases, quarterly payment. Tier 2: voluntary opt-up, multiple activities, cross-border EEA. Tier 3: BSVG farmer regime, disability pension interaction, Svalbard equivalents. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any SVS figure, you MUST know:

1. **Registration status** [T1] -- is the client registered with SVS as Gewerbetreibender or Neue Selbständige?
2. **Income type** [T1] -- trade/business income (gewerbliche Einkünfte) or freelance income (freiberufliche Einkünfte)?
3. **Expected/prior-year income from self-employment** [T1] -- SVS uses prior-year tax assessment (Einkommensteuerbescheid) for final contribution base
4. **Start year** [T1] -- new entrants get provisional minimum base for first 3 years until tax assessment is available
5. **Any concurrent employment?** [T1] -- ASVG employment may cap combined contributions via Differenzvorschreibung
6. **Opting into Selbständigenvorsorge?** [T1] -- mandatory for new Gewerbetreibende since 2008, voluntary for Neue Selbständige

**If registration type is unknown, STOP. Do not compute. Registration type determines which provisions apply.**

---

## Step 1: Determine Contribution Base [T1]

**Legislation:** GSVG §25

### Provisional vs Final Base

SVS operates on a **provisional/final** system:

- **Provisional contributions** are based on the income from 3 years ago (latest available Einkommensteuerbescheid), adjusted for inflation
- **Final contributions** are recalculated once the current-year tax assessment is issued (typically 2-3 years later)
- **New entrants (first 3 years):** provisional base = statutory minimum contribution base

### Contribution Base Formula

```
contribution_base = income_from_self_employment + prescribed_social_contributions
```

The base is the income from self-employment PLUS the social contributions themselves (Hinzurechnung), creating a circular calculation that SVS resolves via published tables.

---

## Step 2: Rates and Thresholds (2025) [T1]

**Legislation:** GSVG §§25-27; SVS Beitragsgrundlagen 2025

| Component | Rate | Legislation |
|-----------|------|-------------|
| Pension insurance (Pensionsversicherung) | 18.50% | GSVG §27 |
| Health insurance (Krankenversicherung) | 6.80% | GSVG §27a |
| Accident insurance (Unfallversicherung) | EUR 11.35/month (flat) | ASVG §74 |
| Selbständigenvorsorge (self-employed provision) | 1.53% | BMSVG §§52-53 |

| Threshold | Monthly (2025) | Annual (2025) | Source |
|-----------|---------------|---------------|--------|
| Minimum contribution base | EUR 539.81 | EUR 6,477.72 | GSVG §25(4) |
| Maximum contribution base | EUR 7,070.00 | EUR 84,840.00 | GSVG §25(5) |
| Health insurance minimum (Gewerbetreibende) | EUR 539.81/month | EUR 6,477.72 | GSVG §25(4) |

### Minimum Monthly Contributions (at minimum base)

| Component | Monthly Minimum |
|-----------|----------------|
| Pension | EUR 99.87 (539.81 x 18.5%) |
| Health | EUR 36.71 (539.81 x 6.8%) |
| Accident | EUR 11.35 (flat) |
| **Total minimum (excl. Vorsorge)** | **EUR 147.93** |

### Maximum Monthly Contributions (at maximum base)

| Component | Monthly Maximum |
|-----------|----------------|
| Pension | EUR 1,307.95 (7,070.00 x 18.5%) |
| Health | EUR 480.76 (7,070.00 x 6.8%) |
| Accident | EUR 11.35 (flat) |
| **Total maximum (excl. Vorsorge)** | **EUR 1,800.06** |

---

## Step 3: Computation Steps [T1]

**Legislation:** GSVG §§25-27

### Step 3.1 -- Determine provisional monthly contribution base

```
IF new_entrant (years 1-3):
    provisional_base = minimum_contribution_base (EUR 539.81/month)
ELSE:
    provisional_base = income_from_3_years_ago / 12 (adjusted)
    provisional_base = max(provisional_base, minimum_base)
    provisional_base = min(provisional_base, maximum_base)
```

### Step 3.2 -- Compute monthly contributions

```
pension_monthly    = provisional_base × 18.50%
health_monthly     = provisional_base × 6.80%
accident_monthly   = EUR 11.35
vorsorge_monthly   = provisional_base × 1.53% (if applicable)

total_monthly = pension_monthly + health_monthly + accident_monthly + vorsorge_monthly
```

### Step 3.3 -- Compute quarterly payment

```
quarterly_payment = total_monthly × 3
```

SVS issues Vorschreibung (contribution notice) quarterly. Payments are due at end of each quarter: 28 Feb, 31 May, 31 Aug, 30 Nov.

### Step 3.4 -- Final reconciliation (Nachbemessung)

When the actual-year Einkommensteuerbescheid is available:

```
final_base = actual_self_employment_income + actual_social_contributions
final_base_monthly = final_base / 12
final_base_monthly = clamp(minimum_base, final_base_monthly, maximum_base)

final_annual = (final_base_monthly × 18.5% + final_base_monthly × 6.8% + 11.35) × 12
adjustment = final_annual - provisional_annual_paid

IF adjustment > 0: SVS issues Nachforderung (additional payment due)
IF adjustment < 0: SVS issues Gutschrift (credit/refund)
```

---

## Step 4: Payment Schedule [T1]

**Legislation:** GSVG §35

| Quarter | Covers | Due Date |
|---------|--------|----------|
| Q1 | Jan--Mar | 28 February |
| Q2 | Apr--Jun | 31 May |
| Q3 | Jul--Sep | 31 August |
| Q4 | Oct--Dec | 30 November |

- Late payment triggers Verzugszinsen (late interest) at currently ~3.88% per annum
- SVS issues the Vorschreibung before each quarter
- Contributions are tax-deductible as Betriebsausgaben (business expenses)

---

## Step 5: Tax Deductibility [T1]

**Legislation:** EStG §4(4)

| Question | Answer |
|----------|--------|
| Are SVS contributions deductible from taxable income? | YES -- as Betriebsausgaben |
| Which contributions are deductible? | Pension, health, accident, Selbständigenvorsorge -- all components |
| When are they deductible? | In the year they are paid (cash basis for contributions) |
| Does the Nachbemessung payment also get deducted? | YES -- in the year of payment |

---

## Step 6: Opting into Voluntary Higher Health Coverage [T2]

**Legislation:** GSVG §28a

Self-employed can opt into higher health insurance coverage:

| Option | Additional Rate |
|--------|----------------|
| Krankengeld opt-in (sickness cash benefit) | Additional 2.5% of contribution base |
| Total health rate with opt-in | 6.80% + 2.50% = 9.30% |

- Opt-in provides daily sickness cash benefit (Krankengeld) from day 43 of illness
- Must opt in by 31 December of the prior year
- Cannot opt out once elected until after a minimum period

**[T2] -- Confirm current Krankengeld waiting period and benefit amounts with SVS.**

---

## Step 7: Neue Selbständige vs Gewerbetreibende [T1]

**Legislation:** GSVG §2(1) vs FSVG

| Feature | Gewerbetreibende | Neue Selbständige |
|---------|------------------|-------------------|
| Registration | Gewerbeberechtigung (trade licence) | No trade licence; freelancers, IT contractors, etc. |
| Insurance obligation | Automatic on registration | Triggered when income exceeds threshold (EUR 6,221.28/year if no other insurance, EUR 39,005.40 if also employed) |
| Selbständigenvorsorge | Mandatory since 2008 | Voluntary |
| Accident insurance | Mandatory | Mandatory once insurance obligation triggered |

---

## Step 8: Edge Case Registry

### EC1 -- Concurrent ASVG employment (Differenzvorschreibung) [T1]
**Situation:** Client is employed (ASVG) and also self-employed (GSVG).
**Resolution:** Combined contribution base cannot exceed the maximum base (EUR 7,070/month). If ASVG base already reaches or exceeds the maximum, GSVG pension contributions are reduced or eliminated. Health insurance: client can choose SVS or GKK coverage. Accident insurance is always due separately.

### EC2 -- New entrant in first 3 years [T1]
**Situation:** Client started self-employment 18 months ago, no prior tax assessment available.
**Resolution:** Provisional base = minimum contribution base (EUR 539.81/month). Total monthly contributions approx EUR 147.93. Client MUST be warned: Nachbemessung will occur once actual income is assessed. If actual income is high, a significant back-payment will be due.

### EC3 -- Income below insurance threshold (Neue Selbständige) [T1]
**Situation:** Freelancer earned EUR 4,000 from self-employment and has no other employment.
**Resolution:** Below the Versicherungsgrenze of EUR 6,221.28/year for persons with no other coverage. No GSVG insurance obligation triggered. However, client has NO health or pension coverage -- flag this.

### EC4 -- Opting to increase provisional base [T2]
**Situation:** Client knows current-year income will be much higher than 3 years ago.
**Resolution:** Client can apply to SVS to increase the provisional contribution base voluntarily. This avoids a large Nachbemessung later. [T2] -- advise client of option but confirm mechanics with SVS.

### EC5 -- Multiple activities [T2]
**Situation:** Client has a Gewerbeberechtigung AND freelance (Neue Selbständige) income.
**Resolution:** All self-employed income is combined into one GSVG contribution base. No double insurance obligation. [T2] flag if the activities fall under different social insurance regimes (GSVG vs FSVG).

### EC6 -- Cross-border EEA worker [T2]
**Situation:** Client lives in Austria but performs work in Germany.
**Resolution:** Under EU Regulation 883/2004, social insurance is generally paid in only one member state. If the client works substantially (25%+) in Germany, German social insurance may apply. [T2] -- requires A1 certificate determination.

### EC7 -- Kleinstunternehmerregelung (small business exemption) [T1]
**Situation:** Client with annual turnover below EUR 35,000 (VAT small business exemption).
**Resolution:** The VAT Kleinstunternehmerregelung does NOT affect SVS obligations. Social insurance is based on income, not turnover. Even if exempt from VAT, SVS contributions remain fully applicable.

### EC8 -- Retirement while self-employed [T2]
**Situation:** Client is drawing ASVG pension but continues self-employment.
**Resolution:** Pension contributions to GSVG continue at 18.5% but accrue additional pension entitlements. Health insurance switches to pensioner rate or remains with SVS depending on coverage choice. [T2] -- confirm pension interaction with SVS.

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
Action Required: Qualified Steuerberater must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified Steuerberater. Document gap.
```

---

## Step 10: Test Suite

### Test 1 -- New entrant, minimum base
**Input:** Self-employed Gewerbetreibender, year 1, no prior income data, age 35.
**Expected output:** Monthly: pension EUR 99.87 + health EUR 36.71 + accident EUR 11.35 + Vorsorge EUR 8.26 = EUR 156.19. Quarterly: EUR 468.57.

### Test 2 -- Established self-employed, mid-range income
**Input:** Prior-year income EUR 40,000, Gewerbetreibender, age 42.
**Expected output:** Monthly base = EUR 40,000 / 12 = EUR 3,333.33. Pension: EUR 616.67. Health: EUR 226.67. Accident: EUR 11.35. Vorsorge: EUR 51.00. Monthly total: EUR 905.69. Quarterly: EUR 2,717.07.

### Test 3 -- High income, maximum base applies
**Input:** Prior-year income EUR 120,000, Gewerbetreibender, age 50.
**Expected output:** Monthly base capped at EUR 7,070.00. Pension: EUR 1,307.95. Health: EUR 480.76. Accident: EUR 11.35. Vorsorge: EUR 108.17. Monthly total: EUR 1,908.23. Quarterly: EUR 5,724.69.

### Test 4 -- Neue Selbständige below threshold
**Input:** Freelance income EUR 4,000, no other employment, age 28.
**Expected output:** Below Versicherungsgrenze (EUR 6,221.28). No GSVG obligation. Flag: client has no social insurance coverage.

### Test 5 -- Concurrent employment
**Input:** ASVG employment base EUR 5,000/month, self-employment income EUR 30,000/year, age 38.
**Expected output:** Combined base = EUR 5,000 + EUR 2,500 = EUR 7,500 exceeds maximum EUR 7,070. GSVG pension base reduced to EUR 2,070/month (7,070 - 5,000). Pension: EUR 382.95. Health: at minimum or based on GSVG base. Accident: EUR 11.35.

### Test 6 -- Nachbemessung scenario
**Input:** Provisional base was minimum (EUR 539.81/month) for 12 months. Actual income turns out to be EUR 50,000.
**Expected output:** Provisional pension paid: EUR 99.87 x 12 = EUR 1,198.44. Final pension: (EUR 4,166.67 x 18.5%) x 12 = EUR 9,250.00. Nachforderung pension alone: EUR 8,051.56. Plus health and Vorsorge adjustments.

### Test 7 -- Krankengeld opt-in
**Input:** Established self-employed, base EUR 3,000/month, opts into Krankengeld.
**Expected output:** Health rate = 9.30% (6.80% + 2.50%). Health monthly = EUR 279.00 (vs EUR 204.00 without opt-in). Additional cost: EUR 75.00/month.

---

## PROHIBITIONS

- NEVER compute SVS contributions without knowing the registration type (Gewerbetreibender vs Neue Selbständige)
- NEVER ignore the minimum/maximum contribution base -- all calculations must clamp to these bounds
- NEVER tell a new entrant their provisional contributions are final -- Nachbemessung WILL occur
- NEVER forget that accident insurance is a flat monthly amount, NOT percentage-based
- NEVER state that SVS contributions are NOT tax-deductible -- they ARE deductible as Betriebsausgaben
- NEVER confuse the Versicherungsgrenze (insurance threshold for Neue Selbständige) with the minimum contribution base
- NEVER apply GSVG rules to farmers (BSVG) or to employed persons (ASVG)
- NEVER advise on cross-border social insurance without flagging for reviewer (EU Regulation 883/2004)
- NEVER present SVS figures as final until the actual-year Einkommensteuerbescheid is issued

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
