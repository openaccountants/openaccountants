---
name: at-svs-contributions
description: Use this skill whenever asked about Austrian SVS (Sozialversicherungsanstalt der Selbständigen) social insurance contributions for self-employed individuals. Trigger on phrases like "SVS contributions", "Austrian social insurance", "GSVG", "self-employed Austria contributions", "Pensionsversicherung self-employed", "SVS Vorschreibung", or any question about social insurance obligations for a self-employed client in Austria. Covers pension (18.5%), health (6.8%), accident (flat monthly), and Selbständigenvorsorge. ALWAYS read this skill before touching any Austria social contributions work.
version: 2.0
---

# Austria SVS Social Insurance Contributions -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Austria (Republic of Austria) |
| Authority | SVS (Sozialversicherungsanstalt der Selbständigen) |
| Primary legislation | GSVG (Gewerbliches Sozialversicherungsgesetz) |
| Supporting legislation | ASVG; FSVG (Freiberuflich); BSVG (Farmers); BMSVG (Selbständigenvorsorge); EStG |
| Pension rate | 18.50% of contribution base |
| Health rate | 6.80% of contribution base |
| Accident insurance | EUR 11.35/month (flat) |
| Selbständigenvorsorge | 1.53% of contribution base (Gewerbetreibende mandatory since 2008; Neue Selbständige voluntary) |
| Minimum monthly base (2025) | EUR 539.81 |
| Maximum monthly base (2025) | EUR 7,070.00 |
| Payment frequency | Quarterly (Vorschreibung) |
| Due dates | 28 Feb, 31 May, 31 Aug, 30 Nov |
| Currency | EUR only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Austrian Steuerberater or Wirtschaftsprüfer |
| Validation date | Pending |

**Minimum monthly contributions (at minimum base EUR 539.81):**

| Component | Monthly |
|---|---|
| Pension | EUR 99.87 |
| Health | EUR 36.71 |
| Accident | EUR 11.35 |
| Total (excl. Vorsorge) | EUR 147.93 |

**Maximum monthly contributions (at maximum base EUR 7,070.00):**

| Component | Monthly |
|---|---|
| Pension | EUR 1,307.95 |
| Health | EUR 480.76 |
| Accident | EUR 11.35 |
| Total (excl. Vorsorge) | EUR 1,800.06 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any SVS figure, you MUST obtain:

1. **Registration status** -- is the client registered with SVS as Gewerbetreibender or Neue Selbständige?
2. **Income type** -- trade/business income (gewerbliche Einkünfte) or freelance income (freiberufliche Einkünfte)?
3. **Expected/prior-year income from self-employment** -- SVS uses the prior-year tax assessment (Einkommensteuerbescheid) for the final contribution base
4. **Start year** -- new entrants get provisional minimum base for first 3 years until tax assessment is available
5. **Any concurrent employment?** -- ASVG employment may cap combined contributions via Differenzvorschreibung
6. **Opting into Selbständigenvorsorge?** -- mandatory for Gewerbetreibende since 2008, voluntary for Neue Selbständige

**If registration type is unknown, STOP. Do not compute. Registration type determines which provisions apply.**

### Refusal catalogue

**R-AT-SVS-1 -- BSVG farmer regime.** Trigger: client's activity falls under BSVG (farmers/agriculture). Message: "BSVG farmer social insurance is outside this skill's scope. Refer to a qualified Steuerberater with agricultural expertise."

**R-AT-SVS-2 -- Disability pension interaction.** Trigger: client receiving or applying for disability pension while self-employed. Message: "Disability pension interaction with GSVG contributions requires specialist review. Escalate to qualified Steuerberater."

**R-AT-SVS-3 -- Cross-border determination.** Trigger: client works in multiple EU/EEA member states. Message: "Cross-border social insurance determination requires A1 certificate analysis under EU Regulation 883/2004. Escalate to qualified adviser."

### Prohibitions

- NEVER compute SVS contributions without knowing the registration type (Gewerbetreibender vs Neue Selbständige)
- NEVER ignore the minimum/maximum contribution base -- all calculations must clamp to these bounds
- NEVER tell a new entrant their provisional contributions are final -- Nachbemessung WILL occur
- NEVER forget that accident insurance is a flat monthly amount, NOT percentage-based
- NEVER state that SVS contributions are NOT tax-deductible -- they ARE deductible as Betriebsausgaben
- NEVER confuse the Versicherungsgrenze (insurance threshold for Neue Selbständige) with the minimum contribution base
- NEVER apply GSVG rules to farmers (BSVG) or to employed persons (ASVG)
- NEVER present SVS figures as final until the actual-year Einkommensteuerbescheid is issued

---

## Section 3 -- Contribution base

**Legislation:** GSVG Section 25

### Provisional vs final base

SVS operates on a provisional/final system:

- **Provisional contributions** are based on the income from 3 years ago (latest available Einkommensteuerbescheid), adjusted for inflation
- **Final contributions** are recalculated once the current-year tax assessment is issued (typically 2-3 years later)
- **New entrants (first 3 years):** provisional base = statutory minimum contribution base

### Contribution base formula

```
contribution_base = income_from_self_employment + prescribed_social_contributions
```

The base is the income from self-employment PLUS the social contributions themselves (Hinzurechnung), creating a circular calculation that SVS resolves via published tables.

### Gewerbetreibende vs Neue Selbständige

| Feature | Gewerbetreibende | Neue Selbständige |
|---|---|---|
| Registration | Gewerbeberechtigung (trade licence) | No trade licence; freelancers, IT contractors, etc. |
| Insurance obligation | Automatic on registration | Triggered when income exceeds threshold (EUR 6,221.28/year if no other insurance, EUR 39,005.40 if also employed) |
| Selbständigenvorsorge | Mandatory since 2008 | Voluntary |
| Accident insurance | Mandatory | Mandatory once insurance obligation triggered |

---

## Section 4 -- Rates and thresholds (2025)

**Legislation:** GSVG Sections 25-27; SVS Beitragsgrundlagen 2025

| Component | Rate | Legislation |
|---|---|---|
| Pension insurance (Pensionsversicherung) | 18.50% | GSVG Section 27 |
| Health insurance (Krankenversicherung) | 6.80% | GSVG Section 27a |
| Accident insurance (Unfallversicherung) | EUR 11.35/month (flat) | ASVG Section 74 |
| Selbständigenvorsorge | 1.53% | BMSVG Sections 52-53 |

| Threshold | Monthly (2025) | Annual (2025) |
|---|---|---|
| Minimum contribution base | EUR 539.81 | EUR 6,477.72 |
| Maximum contribution base | EUR 7,070.00 | EUR 84,840.00 |

### Voluntary higher health coverage (Krankengeld opt-in)

**Legislation:** GSVG Section 28a

| Option | Additional rate |
|---|---|
| Krankengeld opt-in (sickness cash benefit) | Additional 2.5% of contribution base |
| Total health rate with opt-in | 6.80% + 2.50% = 9.30% |

- Opt-in provides daily sickness cash benefit (Krankengeld) from day 43 of illness
- Must opt in by 31 December of the prior year
- Confirm current waiting period and benefit amounts with SVS before advising

---

## Section 5 -- Computation steps

**Legislation:** GSVG Sections 25-27

### Step 5.1 -- Determine provisional monthly contribution base

```
IF new_entrant (years 1-3):
    provisional_base = minimum_contribution_base (EUR 539.81/month)
ELSE:
    provisional_base = income_from_3_years_ago / 12 (adjusted)
    provisional_base = max(provisional_base, minimum_base)
    provisional_base = min(provisional_base, maximum_base)
```

### Step 5.2 -- Compute monthly contributions

```
pension_monthly    = provisional_base x 18.50%
health_monthly     = provisional_base x 6.80%
accident_monthly   = EUR 11.35
vorsorge_monthly   = provisional_base x 1.53% (if applicable)

total_monthly = pension_monthly + health_monthly + accident_monthly + vorsorge_monthly
```

### Step 5.3 -- Compute quarterly payment

```
quarterly_payment = total_monthly x 3
```

### Step 5.4 -- Final reconciliation (Nachbemessung)

When the actual-year Einkommensteuerbescheid is available:

```
final_base = actual_self_employment_income + actual_social_contributions
final_base_monthly = final_base / 12
final_base_monthly = clamp(minimum_base, final_base_monthly, maximum_base)

final_annual = (final_base_monthly x 18.5% + final_base_monthly x 6.8% + 11.35) x 12
adjustment = final_annual - provisional_annual_paid

IF adjustment > 0: SVS issues Nachforderung (additional payment due)
IF adjustment < 0: SVS issues Gutschrift (credit/refund)
```

---

## Section 6 -- Payment schedule and tax deductibility

**Legislation:** GSVG Section 35; EStG Section 4(4)

### Payment schedule

| Quarter | Covers | Due date |
|---|---|---|
| Q1 | Jan--Mar | 28 February |
| Q2 | Apr--Jun | 31 May |
| Q3 | Jul--Sep | 31 August |
| Q4 | Oct--Dec | 30 November |

- Late payment triggers Verzugszinsen (late interest) at currently ~3.88% per annum
- SVS issues the Vorschreibung before each quarter
- Contributions are tax-deductible as Betriebsausgaben (business expenses)

### Tax deductibility

| Question | Answer |
|---|---|
| Are SVS contributions deductible from taxable income? | YES -- as Betriebsausgaben |
| Which contributions are deductible? | Pension, health, accident, Selbständigenvorsorge -- all components |
| When are they deductible? | In the year they are paid (cash basis for contributions) |
| Does the Nachbemessung payment also get deducted? | YES -- in the year of payment |

---

## Section 7 -- Special regimes and concurrent activity

### Kleinstunternehmerregelung (small business exemption)

Client with annual turnover below EUR 35,000 (VAT small business exemption): the VAT Kleinstunternehmerregelung does NOT affect SVS obligations. Social insurance is based on income, not turnover. Even if exempt from VAT, SVS contributions remain fully applicable.

### Concurrent ASVG employment (Differenzvorschreibung)

Client is employed (ASVG) and also self-employed (GSVG): combined contribution base cannot exceed the maximum base (EUR 7,070/month). If ASVG base already reaches or exceeds the maximum, GSVG pension contributions are reduced or eliminated. Health insurance: client can choose SVS or GKK coverage. Accident insurance is always due separately.

### Retirement while self-employed

Client drawing ASVG pension but continuing self-employment: pension contributions to GSVG continue at 18.5% but accrue additional pension entitlements. Health insurance switches to pensioner rate or remains with SVS depending on coverage choice. Confirm pension interaction with SVS before advising.

---

## Section 8 -- Edge case registry

### EC1 -- New entrant in first 3 years
**Situation:** Client started self-employment 18 months ago, no prior tax assessment available.
**Resolution:** Provisional base = minimum contribution base (EUR 539.81/month). Total monthly contributions approx EUR 147.93. Client MUST be warned: Nachbemessung will occur once actual income is assessed. If actual income is high, a significant back-payment will be due.

### EC2 -- Income below insurance threshold (Neue Selbständige)
**Situation:** Freelancer earned EUR 4,000 from self-employment and has no other employment.
**Resolution:** Below the Versicherungsgrenze of EUR 6,221.28/year for persons with no other coverage. No GSVG insurance obligation triggered. However, client has NO health or pension coverage -- flag this.

### EC3 -- Opting to increase provisional base
**Situation:** Client knows current-year income will be much higher than 3 years ago.
**Resolution:** Client can apply to SVS to increase the provisional contribution base voluntarily. This avoids a large Nachbemessung later. Advise client of option but confirm mechanics with SVS.

### EC4 -- Multiple activities
**Situation:** Client has a Gewerbeberechtigung AND freelance (Neue Selbständige) income.
**Resolution:** All self-employed income is combined into one GSVG contribution base. No double insurance obligation. Flag if activities fall under different social insurance regimes (GSVG vs FSVG).

### EC5 -- Cross-border EEA worker
**Situation:** Client lives in Austria but performs work in Germany.
**Resolution:** Under EU Regulation 883/2004, social insurance is generally paid in only one member state. If the client works substantially (25%+) in Germany, German social insurance may apply. Requires A1 certificate determination. Escalate to reviewer.

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
Action Required: Qualified Steuerberater must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified Steuerberater. Document gap.
```

---

## Section 10 -- Test suite

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

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
