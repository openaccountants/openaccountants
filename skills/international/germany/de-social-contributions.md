---
name: de-social-contributions
description: >
  Use this skill whenever asked about German social insurance contributions (Sozialversicherungsbeitraege) for self-employed individuals, freelancers (Freiberufler), or sole proprietors (Einzelunternehmer). Trigger on phrases like "German health insurance", "Krankenversicherung", "GKV", "PKV", "Pflegeversicherung", "Rentenversicherung", "KSK", "Kuenstlersozialkasse", "Berufsgenossenschaft", "Unfallversicherung", "social contributions Germany", "how much health insurance do I pay in Germany", "German pension self-employed", or any question about German social insurance obligations for a self-employed client. Also trigger when preparing a German income tax return (Einkommensteuererklaerung) where Vorsorgeaufwendungen deductibility is relevant. This skill covers GKV vs PKV health insurance, long-term care insurance, pension insurance (voluntary and mandatory), KSK for artists/writers, accident insurance, contribution ceilings, payment schedules, and tax deductibility. ALWAYS read this skill before touching any German social contribution work.
version: 1.0
jurisdiction: DE
tax_year: 2025
category: international
depends_on:
  - social-contributions-workflow-base
---

# Germany Social Contributions (Sozialversicherung) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Germany (Bundesrepublik Deutschland) |
| Jurisdiction Code | DE |
| Primary Legislation | SGB IV (general), SGB V (health), SGB VI (pension), SGB XI (long-term care), SGB VII (accident), KSVG (artists' social insurance) |
| Supporting Legislation | EStG Section 10 (Vorsorgeaufwendungen / tax deductibility of contributions) |
| Regulatory Bodies | GKV-Spitzenverband (health), Deutsche Rentenversicherung Bund (pension), Kuenstlersozialkasse (KSK), Berufsgenossenschaften (accident) |
| Rate Publisher | BMAS (Bundesministerium fuer Arbeit und Soziales) publishes annual Sozialversicherungsrechengroessen |
| Contributor | Open Accountants |
| Validated By | Pending -- requires sign-off by a licensed Steuerberater |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: GKV rate calculation, contribution ceilings, payment schedule, KSK subsidy mechanics. Tier 2: GKV vs PKV switching, KSK eligibility edge cases, Handwerker mandatory pension. Tier 3: disability exemptions, cross-border social security (A1), Versorgungswerk pension schemes. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Licensed Steuerberater must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any social contribution figure, you MUST know:

1. **Employment status** [T1] -- fully self-employed (Freiberufler or Gewerbetreibender), side business alongside employment (Nebenberuf), or dual status
2. **Health insurance type** [T1] -- GKV (gesetzliche Krankenversicherung / statutory) or PKV (private Krankenversicherung / private)
3. **GKV fund name** [T1] -- needed to determine the specific Zusatzbeitrag (supplementary contribution rate)
4. **Number of children** [T1] -- affects Pflegeversicherung rate (childless surcharge)
5. **Age** [T1] -- childless surcharge applies from age 23
6. **Current or expected annual income** [T1] -- contributions are income-based for GKV
7. **Profession** [T2] -- determines whether pension insurance is mandatory (Handwerker, Kuenstler, Lehrer, Hebammen, etc.)
8. **KSK membership** [T1] -- if artist, writer, or journalist, are they KSK-insured?
9. **Has an Einkommensteuerbescheid (income tax assessment) been issued for the prior year?** [T1] -- GKV uses the most recent assessment for final contribution calculation

**If health insurance type (GKV or PKV) is unknown, STOP. Do not compute contributions. This distinction fundamentally changes the calculation.**

---

## Step 1: Overview of German Social Insurance Branches [T1]

**Legislation:** SGB IV (Sozialgesetzbuch IV)

Germany has five branches of social insurance. Self-employed individuals have varying obligations across each:

| Branch | German Name | Self-Employed Obligation | Legislation |
|--------|-------------|------------------------|-------------|
| Health Insurance | Krankenversicherung | Mandatory (GKV or PKV) | SGB V |
| Long-Term Care Insurance | Pflegeversicherung | Mandatory (follows health insurance choice) | SGB XI |
| Pension Insurance | Rentenversicherung | Voluntary for most; mandatory for certain professions | SGB VI |
| Accident Insurance | Unfallversicherung | Voluntary for most; mandatory for certain sectors | SGB VII |
| Unemployment Insurance | Arbeitslosenversicherung | Voluntary opt-in available within first 3 months | SGB III |

**Key principle: Every person residing in Germany must have health insurance (Versicherungspflicht). There is no opt-out.**

---

## Step 2: Krankenversicherung -- Health Insurance [T1]

**Legislation:** SGB V; GKV-Spitzenverband rate announcements

### GKV vs PKV Decision

| Factor | GKV (Statutory) | PKV (Private) |
|--------|-----------------|---------------|
| Who can join | Anyone (self-employed have free choice) | Anyone (self-employed have free choice regardless of income) |
| Contribution basis | Income-based (percentage of income) | Risk-based (age, health, coverage level) |
| Family coverage | Free Familienversicherung for spouse/children without own income | Each family member needs own policy |
| Switching back | Difficult after age 55 or if income stays above JAEG | N/A |

**Self-employed persons can freely choose between GKV and PKV regardless of income level. The income threshold (Jahresarbeitsentgeltgrenze / JAEG) only applies to employees.**

### GKV Rates for Self-Employed (2025) [T1]

| Component | Rate | Notes |
|-----------|------|-------|
| General contribution rate (allgemeiner Beitragssatz) | 14.6% | For self-employed WITH Krankengeldanspruch (sick pay entitlement) |
| Reduced rate (ermaessigter Beitragssatz) | 14.0% | For self-employed WITHOUT sick pay entitlement (default) |
| Zusatzbeitrag (supplementary contribution) | avg. 2.5% (2025) | Varies by fund; check specific Krankenkasse |
| **Typical total (without sick pay)** | **~16.5%** | 14.0% + ~2.5% Zusatzbeitrag |
| **Typical total (with sick pay)** | **~17.1%** | 14.6% + ~2.5% Zusatzbeitrag |

**Self-employed in GKV pay the FULL contribution themselves (no employer share). Employees split 50/50 with employer.**

### GKV Income Thresholds (2025) [T1]

| Threshold | Monthly | Annual | Purpose |
|-----------|---------|--------|---------|
| Mindestbemessungsgrundlage (minimum assessment base) | EUR 1,248.33 | EUR 14,979.96 | Floor for contribution calculation |
| Beitragsbemessungsgrenze (contribution ceiling) | EUR 5,512.50 | EUR 66,150.00 | Cap -- income above this is not assessed |

### GKV Contribution Calculation [T1]

```
Monthly_GKV = clamp(monthly_income, 1248.33, 5512.50) x (base_rate + Zusatzbeitrag)
```

| Income Level | Rate Used | Monthly Contribution (approx.) | Annual (approx.) |
|-------------|-----------|-------------------------------|-------------------|
| Below EUR 1,248.33/mo | Min base applies | ~EUR 206 | ~EUR 2,472 |
| EUR 3,000/mo | Actual income | ~EUR 495 | ~EUR 5,940 |
| EUR 5,512.50/mo (ceiling) | Capped | ~EUR 909 | ~EUR 10,910 |
| EUR 8,000/mo | Capped at BBG | ~EUR 909 | ~EUR 10,910 |

*Calculations assume 14.0% + 2.5% Zusatzbeitrag = 16.5% total*

### GKV Provisional and Final Assessment [T1]

1. Self-employed initially pay **provisional contributions** based on estimated income.
2. After the Einkommensteuerbescheid (income tax assessment) is issued, the Krankenkasse recalculates contributions retroactively.
3. Overpayments are refunded; underpayments must be paid.
4. The Einkommensteuerbescheid must be submitted to the Krankenkasse within **three years**.

### PKV for Self-Employed [T2]

PKV contributions are NOT income-based. They depend on:
- Age at entry
- Health status at entry
- Chosen coverage level (deductible, room type, etc.)
- Actuarial reserves (Alterungsrueckstellungen)

**This skill does NOT compute PKV premiums.** PKV is individual and requires a specific insurance quote. Flag [T2] and advise client to obtain PKV quotes for comparison.

---

## Step 3: Pflegeversicherung -- Long-Term Care Insurance [T1]

**Legislation:** SGB XI; Pflegeversicherungs-Beitragssatzanpassungsgesetz

### Rates (2025) [T1]

| Category | Rate | Notes |
|----------|------|-------|
| Base rate | 3.6% | Of income up to BBG (EUR 5,512.50/mo) |
| Childless surcharge (Kinderlosenzuschlag) | +0.6% | Applies to persons aged 23+ with no children |
| **Total for childless (23+)** | **4.2%** | |
| **Total with children** | **3.6%** | |
| Reduction for 2+ children (kinderreiche Entlastung) | -0.25% per child from 2nd to 5th child (ages under 25) | Minimum rate 2.6% |

### Kinderreiche Entlastung Detail [T1]

Since 1 July 2023, parents with multiple children receive a reduction:

| Number of Children (under 25) | Rate |
|-------------------------------|------|
| 0 (childless, age 23+) | 4.2% |
| 1 child | 3.6% |
| 2 children | 3.35% |
| 3 children | 3.1% |
| 4 children | 2.85% |
| 5+ children | 2.6% |

**The reduction for multiple children applies only while the children are under 25. Once a child turns 25, the reduction for that child lapses, and the rate adjusts upward.**

**Self-employed in GKV pay the FULL Pflegeversicherung rate themselves (no employer share).**

### Pflegeversicherung Assessment Base [T1]

Same as Krankenversicherung:
- Minimum: EUR 1,248.33/month
- Maximum: EUR 5,512.50/month (BBG)

---

## Step 4: Rentenversicherung -- Pension Insurance [T1/T2]

**Legislation:** SGB VI; Handwerkerversicherungsgesetz

### Rate (2025) [T1]

| Item | Value |
|------|-------|
| Contribution rate | 18.6% |
| Beitragsbemessungsgrenze (contribution ceiling) | EUR 8,050/month = EUR 96,600/year |
| Minimum voluntary contribution | EUR 100.07/month (2025) |
| Maximum contribution | EUR 1,497.30/month (18.6% x EUR 8,050) |

**Since 2025, the BBG is uniform across all of Germany (no more Ost/West distinction).**

### Obligation by Self-Employment Type [T2]

| Category | Pension Obligation | Details |
|----------|-------------------|---------|
| Most Freiberufler (freelancers) | **Voluntary** | Can opt in via Antrag auf Pflichtversicherung (within 5 years of starting) |
| Gewerbetreibende (traders) | **Voluntary** | Same as above |
| Handwerker (skilled craftspeople in Handwerksrolle) | **Mandatory** for first 18 years | 18.6% of income; can apply for half-rate after 18 years |
| Artists/writers/journalists via KSK | **Mandatory** via KSK | 50% subsidized (see Step 5) |
| Teachers (selbstaendige Lehrer) | **Mandatory** | If regularly teaching |
| Midwives (Hebammen) | **Mandatory** | Full 18.6% |
| Home workers (Heimarbeiter) | **Mandatory** | |
| Seelotsen (maritime pilots) | **Mandatory** | |
| Self-employed with one client (arbeitnehmeraehnliche Selbstaendige) | **Mandatory** | If >5/6 of income from one client and no employees |

**If the client's profession falls into a mandatory category, flag [T2] and confirm with Steuerberater before advising that pension is voluntary.**

### Voluntary Pension Contributions [T1]

Self-employed persons who are NOT in a mandatory category can:
- Choose any monthly amount between EUR 100.07 and EUR 1,497.30 (2025)
- Pay monthly or make lump-sum payments
- Application: "Antrag auf freiwillige Versicherung" at Deutsche Rentenversicherung

**Once a voluntary Pflichtversicherung (voluntary mandatory insurance) is elected, it is IRREVOCABLE. Advise clients to consider carefully.**

---

## Step 5: Kuenstlersozialkasse (KSK) [T1/T2]

**Legislation:** KSVG (Kuenstlersozialversicherungsgesetz)

### What KSK Does [T1]

The KSK provides self-employed artists, writers, and journalists with social insurance coverage equivalent to an employee -- the KSK acts as the "employer" and pays approximately 50% of health, pension, and long-term care contributions.

### KSK Member Contributions (2025) [T1]

KSK members pay approximately **half** of the standard contribution rates:

| Branch | Full Rate | KSK Member Pays | KSK/Federal Subsidy Covers |
|--------|-----------|-----------------|---------------------------|
| Krankenversicherung | ~14.6% + Zusatzbeitrag | ~7.3% + 50% Zusatzbeitrag | ~7.3% + 50% Zusatzbeitrag |
| Pflegeversicherung | 3.6% (or 4.2% childless) | Full rate (no 50% split) | Nothing -- member pays 100% |
| Rentenversicherung | 18.6% | 9.3% | 9.3% |

**Important: For Pflegeversicherung, the KSK member pays the FULL rate. The 50% subsidy does NOT apply to long-term care insurance.**

### KSK Assessment Base [T1]

- KSK contributions are based on **estimated annual income** (Schaetzung des voraussichtlichen Jahreseinkommens), declared by the member each year.
- KSK verifies against tax returns.
- Minimum income for KSK eligibility: EUR 3,900/year (Geringfuegigkeitsgrenze).

### Kuenstlersozialabgabe -- Client/Verwerter Rate (2025) [T1]

| Item | Value |
|------|-------|
| Abgabesatz (levy rate) | **5.0%** |
| Bagatellgrenze (de minimis threshold) | EUR 700/calendar year |
| Who pays | Businesses (Verwerter) that commission artistic/literary/journalistic work |
| Reporting deadline | 31 March of following year |

**Businesses commissioning work from artists/writers/journalists must pay the 5.0% Kuenstlersozialabgabe on top of fees paid. This is the client's obligation, not the artist's.**

### KSK Eligibility [T2]

To qualify for KSK membership, the individual must:
1. Be self-employed (not employed)
2. Work in the fields of visual arts, performing arts, music, writing/journalism, or related creative professions
3. Earn at least EUR 3,900/year from artistic/journalistic/literary activity (exception for first 3 years: Berufsanfaenger)
4. Not regularly employ more than one employee (one geringfuegig Beschaeftigter / mini-jobber is allowed)

**KSK eligibility is a [T2] question. If uncertain whether the client's profession qualifies, do not assume eligibility. Flag for Steuerberater review.**

---

## Step 6: Unfallversicherung -- Accident Insurance [T1/T2]

**Legislation:** SGB VII

### Berufsgenossenschaft Membership [T1]

| Status | Obligation |
|--------|-----------|
| Employees | Mandatory -- employer must register and pay |
| Most self-employed | **Voluntary** -- can opt into Berufsgenossenschaft |
| Self-employed in agriculture/forestry | **Mandatory** |
| Self-employed in construction (certain trades) | **Mandatory** |
| Self-employed in healthcare (certain professions) | **Mandatory** |

### Cost [T1]

- Contributions vary by industry (Gefahrklasse / risk class) and declared income/turnover.
- Typical range for office-based freelancers: EUR 5 -- EUR 15/month.
- Higher-risk trades (construction, manufacturing): significantly more.
- Each Berufsgenossenschaft publishes its own rate table.

**This skill does NOT compute Unfallversicherung contributions. They are too variable by industry. Advise client to contact the relevant Berufsgenossenschaft for a quote.**

---

## Step 7: Arbeitslosenversicherung -- Unemployment Insurance [T1]

**Legislation:** SGB III Section 28a

| Item | Value |
|------|-------|
| Rate | 2.6% (2025) |
| Obligation for self-employed | **Voluntary** (Freiwillige Weiterversicherung) |
| Eligibility to opt in | Within 3 months of starting self-employment; must have had at least 12 months of mandatory insurance in the prior 30 months |
| Assessment base (if voluntary) | Fixed notional amount set annually |

**Most self-employed do not opt in. This is informational only. If the client asks about voluntary unemployment insurance, flag [T2] for case-specific advice.**

---

## Step 8: Contribution Ceilings and Minimums Summary (2025) [T1]

| Parameter | Health + Care (KV/PV) | Pension (RV) |
|-----------|-----------------------|-------------|
| Beitragsbemessungsgrenze (monthly) | EUR 5,512.50 | EUR 8,050.00 |
| Beitragsbemessungsgrenze (annual) | EUR 66,150.00 | EUR 96,600.00 |
| Mindestbemessungsgrundlage (monthly, GKV self-employed) | EUR 1,248.33 | EUR 100.07 (voluntary minimum) |
| Versicherungspflichtgrenze / JAEG (employees only) | EUR 73,800.00 | N/A |

---

## Step 9: Payment Schedule [T1]

| Branch | Frequency | Due Date | Method |
|--------|-----------|----------|--------|
| GKV (Krankenversicherung) | Monthly | 15th of each month (for current month) | Direct debit (Lastschrift) or bank transfer |
| Pflegeversicherung | Monthly | Collected together with GKV | Same as GKV |
| Rentenversicherung (voluntary) | Monthly | By end of each month | Bank transfer to Deutsche Rentenversicherung |
| KSK contributions | Monthly | KSK collects via direct debit, typically mid-month | Direct debit managed by KSK |
| Berufsgenossenschaft | Annually (some quarterly) | Varies by BG; typically due in arrears | Invoice from BG |

**GKV contributions are due on the 15th of the month for which they apply (not in arrears).**

---

## Step 10: Tax Deductibility of Contributions (Vorsorgeaufwendungen) [T1]

**Legislation:** EStG Section 10

### Deductibility Rules (2025) [T1]

| Contribution Type | Tax Treatment | Limit |
|-------------------|--------------|-------|
| Rentenversicherung (statutory or Ruerup/Basisrente) | 100% deductible as Sonderausgaben (since 2023) | EUR 29,344/year (single); EUR 58,688 (married, joint filing) |
| Krankenversicherung (Basiskrankenversicherung) | Fully deductible | No cap on Basisabsicherung |
| Pflegeversicherung | Fully deductible | No cap |
| KV supplementary coverage (Wahlleistungen, Zusatzversicherung) | Deductible within cap | Subject to EUR 2,800 cap (self-employed) |
| Unfallversicherung | Deductible within cap | Subject to EUR 2,800 cap (self-employed) |
| Arbeitslosenversicherung | Deductible within cap | Subject to EUR 2,800 cap (self-employed) |

### Key Points [T1]

1. **Basiskrankenversicherung contributions are FULLY deductible with no cap.** This is the core health insurance coverage (not supplementary add-ons).
2. **The EUR 2,800 cap applies to self-employed persons** for "sonstige Vorsorgeaufwendungen" (other insurance contributions). Employees have a lower cap of EUR 1,900 because their employer pays half.
3. **Pension contributions (Altersvorsorgeaufwendungen) have a separate, higher cap** and are NOT subject to the EUR 2,800 limit.
4. **Interaction with income tax skill:** When preparing the Einkommensteuererklaerung, enter contributions in Anlage Vorsorgeaufwand. The Basiskrankenversicherung and Pflegeversicherung amounts often consume the entire EUR 2,800 cap, meaning additional insurance (liability, accident) may yield no further deduction.

---

## Step 11: Edge Case Registry

### EC1 -- Hauptberuflich vs Nebenberuflich self-employment alongside employment [T2]
**Situation:** Client is employed full-time and has a side freelance business.
**Resolution:** If the employment is the main occupation (hauptberuflich), GKV coverage comes from the employment. The side income is not separately assessed for GKV IF the side activity is clearly secondary (fewer hours, lower income than employment). If the side business becomes the main activity, the client must pay full self-employed GKV contributions. [T2] -- the determination of hauptberuflich vs nebenberuflich requires case-specific assessment.

### EC2 -- Switching from PKV to GKV [T2]
**Situation:** Self-employed client in PKV wants to switch to GKV.
**Resolution:** Switching is very restricted. Generally impossible after age 55. Must demonstrate either (a) becoming employed with income below JAEG, or (b) other narrow exceptions. [T2] escalate to Steuerberater. Do not advise that switching is possible without confirmation.

### EC3 -- KSK member with income below Geringfuegigkeitsgrenze [T1]
**Situation:** KSK member earns less than EUR 3,900 in a year.
**Resolution:** After the initial 3-year Berufsanfaenger period, the member will lose KSK coverage if income stays below EUR 3,900. They must then arrange own health/pension insurance. Flag if approaching this threshold.

### EC4 -- Self-employed with one client (Scheinselbstaendigkeit risk) [T2]
**Situation:** Freelancer earns >5/6 of income from a single client and has no employees.
**Resolution:** This triggers arbeitnehmeraehnliche Selbstaendigkeit under SGB VI Section 2. Pension insurance becomes MANDATORY at 18.6%. Additionally, the Statusfeststellungsverfahren (employment status determination) may reclassify the relationship as de facto employment (Scheinselbstaendigkeit), triggering full social insurance obligations. [T2] -- escalate immediately. Significant financial exposure.

### EC5 -- Handwerker after 18 years of mandatory pension [T1]
**Situation:** Skilled craftsperson (in Handwerksrolle) has paid 216 months (18 years) of mandatory pension contributions.
**Resolution:** Can apply for exemption from mandatory pension insurance (Befreiungsantrag). After exemption, pension becomes voluntary. The 18-year clock counts from first registration in the Handwerksrolle.

### EC6 -- GKV retroactive adjustment after Einkommensteuerbescheid [T1]
**Situation:** Self-employed person's actual income differs significantly from estimated income used for provisional GKV contributions.
**Resolution:** The Krankenkasse recalculates retroactively upon receipt of the Einkommensteuerbescheid. Underpayments must be paid; overpayments are refunded. The assessment can go back up to 3 years. Advise clients to submit their Bescheid promptly and reserve funds for potential underpayments.

### EC7 -- Kuenstler eligible for both KSK and Versorgungswerk [T2]
**Situation:** A self-employed architect who also does artistic work could qualify for KSK and for the architects' Versorgungswerk (professional pension fund).
**Resolution:** KSK membership and Versorgungswerk membership are not necessarily mutually exclusive, but the pension component may overlap. [T2] -- requires Steuerberater analysis of which scheme applies to which income.

### EC8 -- Voluntary pension: Pflichtversicherung auf Antrag is irrevocable [T1]
**Situation:** Self-employed person elected voluntary mandatory pension insurance (Pflichtversicherung auf Antrag).
**Resolution:** This election is IRREVOCABLE. The person must continue paying 18.6% on income up to the BBG for as long as they remain self-employed. Do NOT advise electing this without explicit client understanding and Steuerberater confirmation.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Licensed Steuerberater must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed Steuerberater. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard GKV self-employed, mid-range income, childless
**Input:** Self-employed freelancer, GKV (no sick pay), Zusatzbeitrag 2.5%, income EUR 3,500/month, age 35, no children.
**Expected output:**
- KV: EUR 3,500 x 16.5% = EUR 577.50/month
- PV: EUR 3,500 x 4.2% = EUR 147.00/month (childless surcharge applies)
- Total KV + PV: EUR 724.50/month = EUR 8,694.00/year

### Test 2 -- GKV self-employed at minimum income
**Input:** Self-employed, GKV (no sick pay), Zusatzbeitrag 2.5%, income EUR 800/month, age 30, 1 child.
**Expected output:**
- Minimum base applies: EUR 1,248.33
- KV: EUR 1,248.33 x 16.5% = EUR 205.97/month
- PV: EUR 1,248.33 x 3.6% = EUR 44.94/month
- Total KV + PV: EUR 250.91/month = EUR 3,010.92/year

### Test 3 -- GKV self-employed above contribution ceiling
**Input:** Self-employed consultant, GKV (with sick pay), Zusatzbeitrag 2.5%, income EUR 9,000/month, age 45, 2 children (both under 25).
**Expected output:**
- Capped at BBG: EUR 5,512.50
- KV: EUR 5,512.50 x 17.1% (14.6% + 2.5%) = EUR 942.64/month
- PV: EUR 5,512.50 x 3.35% (2 children) = EUR 184.67/month
- Total KV + PV: EUR 1,127.31/month = EUR 13,527.72/year

### Test 4 -- KSK member artist
**Input:** Freelance graphic designer, KSK member, estimated annual income EUR 30,000, age 28, no children.
**Expected output:**
- KSK handles enrollment; member pays ~50% of KV and RV, full PV
- Monthly income for KSK purposes: EUR 2,500
- KV (member share): ~EUR 2,500 x ~8.55% (half of ~17.1%) = ~EUR 213.75/month
- RV (member share): EUR 2,500 x 9.3% = EUR 232.50/month
- PV (full, childless): EUR 2,500 x 4.2% = EUR 105.00/month
- Approximate total: ~EUR 551.25/month = ~EUR 6,615/year
- Note: Exact KV depends on chosen Krankenkasse Zusatzbeitrag

### Test 5 -- Mandatory pension for Handwerker
**Input:** Self-employed master electrician registered in Handwerksrolle, 5 years in, income EUR 4,500/month.
**Expected output:**
- Pension is MANDATORY (fewer than 18 years)
- RV: EUR 4,500 x 18.6% = EUR 837.00/month = EUR 10,044.00/year
- Pension contributions fully deductible as Altersvorsorgeaufwendungen (within EUR 29,344 cap)

### Test 6 -- Employed full-time with side freelance income
**Input:** Full-time employee (EUR 55,000/year salary, employer pays KV/PV/RV) with EUR 8,000/year freelance income on the side.
**Expected output:**
- If side business is clearly nebenberuflich: no separate GKV/PV contributions on freelance income (covered by employment)
- No mandatory pension on side income (assuming not in a mandatory self-employed category)
- [T2] flag: confirm nebenberuflich status (fewer hours and lower income than employment)

### Test 7 -- Vorsorgeaufwendungen tax deduction
**Input:** Self-employed, paid EUR 10,500 GKV (Basiskrankenversicherung), EUR 2,400 PV, EUR 5,580 voluntary RV in 2025. Single filer.
**Expected output:**
- Basiskrankenversicherung (EUR 10,500): fully deductible, no cap
- Pflegeversicherung (EUR 2,400): fully deductible, no cap
- Rentenversicherung (EUR 5,580): 100% deductible as Altersvorsorgeaufwendungen (within EUR 29,344 cap)
- Total deduction: EUR 18,480 on Anlage Vorsorgeaufwand
- Note: The EUR 2,800 cap for sonstige Vorsorgeaufwendungen is already exceeded by KV+PV, so any additional insurance (liability, accident) yields no further deduction in that category

### Test 8 -- Kuenstlersozialabgabe for client/Verwerter
**Input:** Marketing agency paid EUR 15,000 in fees to freelance designers and copywriters in 2025.
**Expected output:**
- Kuenstlersozialabgabe due: EUR 15,000 x 5.0% = EUR 750.00
- Must be reported to KSK by 31 March 2026
- Threshold: exceeds EUR 700 Bagatellgrenze, so obligation applies

---

## PROHIBITIONS

- NEVER compute contributions without knowing whether the client is in GKV or PKV -- the calculation is fundamentally different
- NEVER apply the 50% KSK subsidy to Pflegeversicherung -- KSK members pay the FULL Pflegeversicherung rate
- NEVER assume pension insurance is voluntary without checking the client's profession against the mandatory categories (Handwerker, Kuenstler/KSK, Lehrer, Hebammen, arbeitnehmeraehnliche Selbstaendige)
- NEVER tell a self-employed GKV member they can contribute below the Mindestbemessungsgrundlage -- the minimum always applies even at zero income
- NEVER advise a PKV member that switching to GKV is straightforward -- it is heavily restricted, especially after age 55
- NEVER compute PKV premiums -- they are individual and risk-based, not formula-driven
- NEVER advise electing Pflichtversicherung auf Antrag (voluntary mandatory pension) without emphasizing it is IRREVOCABLE
- NEVER ignore the Zusatzbeitrag when computing GKV contributions -- it varies by fund and significantly affects the total
- NEVER present GKV provisional contributions as final -- they are subject to retroactive adjustment based on the Einkommensteuerbescheid
- NEVER conflate the KV/PV Beitragsbemessungsgrenze (EUR 5,512.50/mo) with the RV Beitragsbemessungsgrenze (EUR 8,050/mo) -- they are different
- NEVER advise on Scheinselbstaendigkeit (false self-employment) determinations without escalating to a Steuerberater -- the financial exposure is severe

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftspruefer, or equivalent licensed practitioner in Germany) before filing or acting upon.

German social insurance law is complex and fact-specific. Rates, thresholds, and rules change annually via the Sozialversicherungsrechengroessenverordnung. Always verify figures against the current year's BMAS publication.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
