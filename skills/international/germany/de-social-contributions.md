---
name: de-social-contributions
description: >
  Use this skill whenever asked about German social insurance contributions (Sozialversicherungsbeitraege) for self-employed individuals, freelancers (Freiberufler), or sole proprietors (Einzelunternehmer). Trigger on phrases like "German health insurance", "Krankenversicherung", "GKV", "PKV", "Pflegeversicherung", "Rentenversicherung", "KSK", "Kuenstlersozialkasse", "Berufsgenossenschaft", "Unfallversicherung", "social contributions Germany", "Krankenkasse debit", or any question about German social insurance obligations. Also trigger when classifying bank statement transactions showing Krankenkasse debits, KSK direct debits, Berufsgenossenschaft invoices, or Deutsche Rentenversicherung payments. ALWAYS read this skill before touching any German social contribution work.
version: 2.0
jurisdiction: DE
tax_year: 2025
category: international
depends_on:
  - social-contributions-workflow-base
---

# Germany Social Contributions (Sozialversicherung) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Germany (Bundesrepublik Deutschland) |
| Primary Legislation | SGB IV (general), SGB V (health), SGB VI (pension), SGB XI (care), SGB VII (accident), KSVG (artists) |
| Supporting Legislation | EStG Section 10 (Vorsorgeaufwendungen / tax deductibility) |
| Regulatory Bodies | GKV-Spitzenverband (health), Deutsche Rentenversicherung Bund (pension), Kuenstlersozialkasse (KSK), Berufsgenossenschaften (accident) |
| Rate Publisher | BMAS (annual Sozialversicherungsrechengroessen) |
| Currency | EUR only |
| GKV base rate (without sick pay) | 14.0% + avg. 2.5% Zusatzbeitrag = ~16.5% |
| GKV base rate (with sick pay) | 14.6% + avg. 2.5% Zusatzbeitrag = ~17.1% |
| GKV minimum base (monthly) | EUR 1,248.33 |
| GKV/PV contribution ceiling (monthly) | EUR 5,512.50 |
| Pension contribution ceiling (monthly) | EUR 8,050.00 |
| Pension rate | 18.6% |
| Pflegeversicherung base rate | 3.6% (childless 23+: 4.2%) |
| KSK levy rate (Verwerter) | 5.0% |
| GKV payment due | 15th of each month |
| Contributor | Open Accountants |
| Validated by | Pending -- requires sign-off by a licensed Steuerberater |
| Validation date | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown GKV or PKV | STOP -- do not compute without this |
| Unknown Zusatzbeitrag | Use average 2.5% |
| Unknown number of children | Apply childless surcharge (4.2% PV) |
| Unknown profession (pension obligation) | Assume voluntary; flag for reviewer |
| Unknown Hauptberuflich vs Nebenberuflich | Flag for reviewer |
| Unknown income for GKV | Apply minimum base (EUR 1,248.33/month) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- health insurance type (GKV or PKV), current or expected monthly income, and number of children.

**Recommended** -- GKV fund name (for Zusatzbeitrag), profession (for pension obligation check), age, Einkommensteuerbescheid for prior year.

**Ideal** -- complete Einkommensteuererklaerung, GKV contribution notice, KSK membership confirmation (if applicable), Berufsgenossenschaft invoice.

### Refusal catalogue

**R-DE-SC-1 -- GKV vs PKV unknown.** *Trigger:* client has not confirmed insurance type. *Message:* "The distinction between GKV and PKV fundamentally changes the calculation. Cannot proceed without this information."

**R-DE-SC-2 -- PKV premium computation.** *Trigger:* client asks for PKV premium calculation. *Message:* "PKV premiums are individual and risk-based. This skill does not compute PKV premiums. Advise client to obtain PKV quotes."

**R-DE-SC-3 -- Cross-border social security (A1).** *Trigger:* client works across EU borders. *Message:* "EU social security coordination (Regulation EC 883/2004) and A1 certificates require specialist advice. Escalate to Steuerberater."

**R-DE-SC-4 -- Versorgungswerk pension schemes.** *Trigger:* client is in a professional pension fund (Versorgungswerk). *Message:* "Versorgungswerk schemes have their own rate schedules. Out of scope -- escalate to Steuerberater."

**R-DE-SC-5 -- Scheinselbstaendigkeit determination.** *Trigger:* possible false self-employment. *Message:* "Statusfeststellungsverfahren and Scheinselbstaendigkeit determinations involve severe financial exposure. Escalate immediately."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to German social contributions.

### 3.1 Krankenkasse (GKV health insurance) debits

| Pattern | Treatment | Notes |
|---|---|---|
| TK, TECHNIKER KRANKENKASSE | EXCLUDE -- GKV contribution | Health + care combined debit |
| AOK, AOK PLUS, AOK BAYERN, AOK NORDWEST | EXCLUDE -- GKV contribution | Regional AOK variants |
| BARMER, BARMER GEK | EXCLUDE -- GKV contribution | |
| DAK, DAK-GESUNDHEIT | EXCLUDE -- GKV contribution | |
| IKK, IKK CLASSIC, IKK SUEDWEST | EXCLUDE -- GKV contribution | |
| HEK, HANSEATISCHE KRANKENKASSE | EXCLUDE -- GKV contribution | |
| KKH, KAUFMAENNISCHE KRANKENKASSE | EXCLUDE -- GKV contribution | |
| KNAPPSCHAFT | EXCLUDE -- GKV contribution | |
| BKK (various: BKK MOBIL OIL, BKK FIRMUS, VIACTIV) | EXCLUDE -- GKV contribution | Betriebskrankenkassen |
| KRANKENKASSE, KRANKENVERSICHERUNG | EXCLUDE -- GKV contribution | Generic pattern |
| GKV, GESETZLICHE KV | EXCLUDE -- GKV contribution | Generic abbreviation |

### 3.2 Private Krankenversicherung (PKV) debits

| Pattern | Treatment | Notes |
|---|---|---|
| ALLIANZ PKV, ALLIANZ PRIVATE | EXCLUDE -- PKV premium | Private health insurance |
| DEBEKA, DEBEKA KRANKENVERSICHERUNG | EXCLUDE -- PKV premium | |
| DKV, DEUTSCHE KRANKENVERSICHERUNG | EXCLUDE -- PKV premium | |
| SIGNAL IDUNA PKV | EXCLUDE -- PKV premium | |
| HALLESCHE | EXCLUDE -- PKV premium | |
| BARMENIA | EXCLUDE -- PKV premium | Could be supplementary |
| PRIVATE KRANKENVERSICHERUNG, PKV | EXCLUDE -- PKV premium | Generic |

### 3.3 KSK (Kuenstlersozialkasse) debits

| Pattern | Treatment | Notes |
|---|---|---|
| KSK, KUENSTLERSOZIALKASSE | EXCLUDE -- KSK contribution | Combined health + pension contribution |
| KUENSTLERSOZIALVERSICHERUNG | EXCLUDE -- KSK contribution | |

### 3.4 Deutsche Rentenversicherung (pension)

| Pattern | Treatment | Notes |
|---|---|---|
| DRV, DEUTSCHE RENTENVERSICHERUNG | EXCLUDE -- pension contribution | Voluntary or mandatory pension |
| RENTENVERSICHERUNG, RV BEITRAG | EXCLUDE -- pension contribution | |

### 3.5 Berufsgenossenschaft (accident insurance)

| Pattern | Treatment | Notes |
|---|---|---|
| BG, BERUFSGENOSSENSCHAFT | EXCLUDE -- accident insurance | Annual or quarterly BG invoice |
| BG BAU, BG ETEM, BGW, BGHM, BG VERKEHR | EXCLUDE -- BG contribution | Named BGs by sector |
| VBG, VERWALTUNGS-BG | EXCLUDE -- BG contribution | Office-based industries |
| UNFALLVERSICHERUNG | EXCLUDE -- accident insurance | Generic |

### 3.6 Arbeitslosenversicherung (unemployment -- voluntary)

| Pattern | Treatment | Notes |
|---|---|---|
| AGENTUR FUER ARBEIT, BUNDESAGENTUR | EXCLUDE -- voluntary unemployment | If self-employed opted in |
| ARBEITSLOSENVERSICHERUNG | EXCLUDE -- voluntary unemployment | Rare for self-employed |

### 3.7 Tax authority (NOT social contributions)

| Pattern | Treatment | Notes |
|---|---|---|
| FINANZAMT, FA (+ city name) | EXCLUDE -- income tax | Not a social contribution |
| UMSATZSTEUER, UST | EXCLUDE -- VAT | Not a social contribution |
| EINKOMMENSTEUER, EST | EXCLUDE -- income tax | Not a social contribution |
| GEWERBESTEUER | EXCLUDE -- trade tax | Not a social contribution |

---

## Section 4 -- Worked examples

Six bank statement classifications for a hypothetical self-employed German IT consultant (Freiberufler, GKV-insured, no children, age 35).

### Example 1 -- Monthly Krankenkasse debit (Techniker)

**Input line:**
`15.04.2025 ; TECHNIKER KRANKENKASSE ; LASTSCHRIFT ; BEITRAG APRIL 2025 ; -577.50 ; EUR`

**Reasoning:**
Matches "TECHNIKER KRANKENKASSE" (pattern 3.1). Amount EUR 577.50 = EUR 3,500 monthly income x 16.5% (14.0% + 2.5% Zusatzbeitrag). This is the April 2025 GKV contribution. Due on the 15th. Excludes Pflegeversicherung (billed separately or combined -- check).

**Classification:** EXCLUDE -- GKV health insurance contribution. Tax-deductible as Basiskrankenversicherung (fully deductible, no cap).

### Example 2 -- Pflegeversicherung (combined with GKV or separate)

**Input line:**
`15.04.2025 ; TECHNIKER KRANKENKASSE ; LASTSCHRIFT ; PV BEITRAG ; -147.00 ; EUR`

**Reasoning:**
Matches TK pattern. Amount EUR 147.00 = EUR 3,500 x 4.2% (childless surcharge, age 23+). This is the Pflegeversicherung contribution. Some Krankenkassen combine KV + PV in one debit; others split them. Either way, EXCLUDE.

**Classification:** EXCLUDE -- Pflegeversicherung. Fully deductible (no cap).

### Example 3 -- KSK debit (artist member)

**Input line:**
`15.03.2025 ; KUENSTLERSOZIALKASSE ; LASTSCHRIFT ; BEITRAG MAERZ ; -551.25 ; EUR`

**Reasoning:**
Matches "KUENSTLERSOZIALKASSE" (pattern 3.3). KSK collects combined health + pension contribution from the member. The member pays approximately 50% of health and pension, plus full Pflegeversicherung. Amount varies by declared income and Krankenkasse Zusatzbeitrag.

**Classification:** EXCLUDE -- KSK contribution. Tax treatment: health portion fully deductible as Basiskrankenversicherung; pension portion deductible as Altersvorsorgeaufwendungen.

### Example 4 -- Berufsgenossenschaft annual invoice

**Input line:**
`30.04.2025 ; VBG VERWALTUNGS-BG ; UEBERWEISUNG ; BEITRAG 2024 ; -85.00 ; EUR`

**Reasoning:**
Matches "VBG" (pattern 3.5). Annual BG contribution for 2024, paid in arrears. Office-based freelancer = low risk class. EUR 85 is typical for office-based Freiberufler.

**Classification:** EXCLUDE -- accident insurance. Deductible within EUR 2,800 sonstige Vorsorgeaufwendungen cap (but this cap is usually consumed by KV/PV).

### Example 5 -- Voluntary pension payment (Deutsche Rentenversicherung)

**Input line:**
`28.02.2025 ; DEUTSCHE RENTENVERSICHERUNG BUND ; UEBERWEISUNG ; FREIWILLIGER BEITRAG FEB ; -500.00 ; EUR`

**Reasoning:**
Matches "DEUTSCHE RENTENVERSICHERUNG" (pattern 3.4). Voluntary pension contribution of EUR 500/month (between minimum EUR 100.07 and maximum EUR 1,497.30). Self-employed person has chosen to contribute voluntarily.

**Classification:** EXCLUDE -- voluntary pension contribution. 100% deductible as Altersvorsorgeaufwendungen (within EUR 29,344 single / EUR 58,688 married cap).

### Example 6 -- Finanzamt (income tax, NOT social contribution)

**Input line:**
`10.03.2025 ; FINANZAMT MUENCHEN ; LASTSCHRIFT ; EST VORAUSZAHLUNG Q1 ; -3,200.00 ; EUR`

**Reasoning:**
Matches "FINANZAMT" (pattern 3.7). This is an income tax prepayment, NOT a social contribution. Do not classify as social insurance.

**Classification:** EXCLUDE -- income tax. NOT a social contribution.

---

## Section 5 -- Tier 1 rules

### Rule 1 -- GKV contribution formula

```
Monthly_GKV = clamp(monthly_income, EUR 1,248.33, EUR 5,512.50) x (base_rate + Zusatzbeitrag)
```

Self-employed pay the FULL rate (no employer share).

### Rule 2 -- GKV rates (2025)

| Component | Rate |
|---|---|
| Without sick pay (default for self-employed) | 14.0% + Zusatzbeitrag |
| With sick pay | 14.6% + Zusatzbeitrag |
| Average Zusatzbeitrag (2025) | 2.5% |

### Rule 3 -- Pflegeversicherung rates (2025)

| Children (under 25) | Rate |
|---|---|
| 0 (childless, age 23+) | 4.2% |
| 1 | 3.6% |
| 2 | 3.35% |
| 3 | 3.1% |
| 4 | 2.85% |
| 5+ | 2.6% |

Same assessment base as GKV (EUR 1,248.33 to EUR 5,512.50 monthly). Full rate for self-employed (no employer share).

### Rule 4 -- Pension (Rentenversicherung)

Rate: 18.6%. Ceiling: EUR 8,050/month. Voluntary minimum: EUR 100.07/month. Mandatory for: Handwerker (first 18 years), KSK members, teachers (selbstaendige Lehrer), midwives, arbeitnehmeraehnliche Selbstaendige. Voluntary for most Freiberufler and Gewerbetreibende.

### Rule 5 -- KSK members pay approximately half

KSK covers ~50% of health and pension. Member pays ~7.3% + 50% Zusatzbeitrag for health, 9.3% for pension, and FULL Pflegeversicherung (no 50% split on care).

### Rule 6 -- Kuenstlersozialabgabe (client/Verwerter)

Businesses commissioning artistic/literary/journalistic work pay 5.0% levy on fees paid. Bagatellgrenze: EUR 700/year. Reporting deadline: 31 March following year.

### Rule 7 -- GKV provisional and final assessment

Provisional contributions based on estimated income. Recalculated retroactively after Einkommensteuerbescheid. Overpayments refunded; underpayments demanded. Bescheid must be submitted to Krankenkasse within 3 years.

### Rule 8 -- Every person must have health insurance

There is no opt-out. Self-employed can freely choose GKV or PKV (the JAEG threshold applies only to employees).

### Rule 9 -- Tax deductibility (Vorsorgeaufwendungen)

| Contribution | Deductibility |
|---|---|
| Basiskrankenversicherung (GKV or PKV base) | Fully deductible, no cap |
| Pflegeversicherung | Fully deductible, no cap |
| Rentenversicherung (statutory or Ruerup) | 100% deductible (since 2023), within EUR 29,344 cap |
| Other insurance (accident, supplementary) | Within EUR 2,800 cap (self-employed) |

### Rule 10 -- Payment schedule

| Branch | Due | Method |
|---|---|---|
| GKV + PV | 15th of each month (for current month) | Lastschrift or bank transfer |
| Pension (voluntary) | End of each month | Bank transfer |
| KSK | Mid-month | KSK direct debit |
| BG | Annual (some quarterly) | BG invoice |

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Hauptberuflich vs Nebenberuflich (side business alongside employment)

**Trigger:** Client is employed full-time with a side freelance business.
**Issue:** If employment is hauptberuflich, GKV comes from employment; side income not separately assessed for GKV. If side business becomes main activity, full self-employed GKV contributions apply.
**Action:** Flag for reviewer. Case-specific assessment required.

### T2-2 -- PKV to GKV switching

**Trigger:** PKV client wants to switch to GKV.
**Issue:** Very restricted. Generally impossible after age 55. Must demonstrate becoming employed with income below JAEG.
**Action:** Escalate to Steuerberater. Do not advise switching is possible.

### T2-3 -- KSK eligibility determination

**Trigger:** Client's profession may or may not qualify for KSK.
**Issue:** KSK membership requires creative/artistic/literary/journalistic self-employment, EUR 3,900+ annual income (after 3-year Berufsanfaenger period), and no more than one employee.
**Action:** Flag for reviewer. Do not assume eligibility.

### T2-4 -- Scheinselbstaendigkeit (false self-employment)

**Trigger:** Client earns >5/6 of income from one client and has no employees.
**Issue:** Triggers arbeitnehmeraehnliche Selbstaendigkeit under SGB VI Section 2 (mandatory pension) and potential reclassification.
**Action:** Escalate immediately. Severe financial exposure.

### T2-5 -- Handwerker pension after 18 years

**Trigger:** Skilled craftsperson with 216+ months of mandatory pension.
**Issue:** May apply for exemption (Befreiungsantrag).
**Action:** Flag for reviewer to confirm eligibility.

### T2-6 -- GKV retroactive adjustment

**Trigger:** Einkommensteuerbescheid shows significant income deviation from provisional estimate.
**Issue:** Krankenkasse recalculates retroactively. Underpayments demanded.
**Action:** Advise client to submit Bescheid promptly and reserve funds.

---

## Section 7 -- Excel working paper template

```
GERMANY SOCIAL CONTRIBUTIONS -- WORKING PAPER
Client: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Insurance type:                [GKV / PKV]
  Krankenkasse name:             [____]
  Zusatzbeitrag:                 [____]%
  Monthly income:                EUR [____]
  Number of children (under 25): [____]
  Age:                           [____]
  Profession:                    [____]
  KSK member:                    [YES/NO]
  Pension: voluntary/mandatory:  [____]

GKV COMPUTATION
  Assessment base (clamped):     EUR [____]
  KV rate:                       [____]%
  Monthly KV:                    EUR [____]
  PV rate:                       [____]%
  Monthly PV:                    EUR [____]
  Total KV + PV monthly:         EUR [____]
  Total KV + PV annual:          EUR [____]

PENSION COMPUTATION
  Type: [Voluntary / Mandatory / KSK]
  Monthly contribution:          EUR [____]
  Annual contribution:           EUR [____]

OTHER
  BG contribution:               EUR [____]
  Arbeitslosenversicherung:      EUR [____]

TOTAL ANNUAL CONTRIBUTIONS:      EUR [____]

TAX DEDUCTIBILITY (ANLAGE VORSORGEAUFWAND)
  Basiskrankenversicherung:      EUR [____] (fully deductible)
  Pflegeversicherung:            EUR [____] (fully deductible)
  Rentenversicherung:            EUR [____] (deductible within cap)
  Other (BG, supplementary):     EUR [____] (within EUR 2,800 cap)

REVIEWER FLAGS
  [List any Tier 2 flags]
```

---

## Section 8 -- Bank statement reading guide

### How German social contribution debits appear

**GKV Krankenkasse debits:**
- Description: Krankenkasse name + "BEITRAG" or "LASTSCHRIFT" or "KV BEITRAG"
- Timing: 15th of each month (for the current month)
- Amount: Consistent monthly amount (changes only when income reassessed)
- Some Kassen combine KV + PV in one debit; others show two debits

**KSK debits:**
- Description: "KUENSTLERSOZIALKASSE" or "KSK"
- Timing: Mid-month
- Amount: Varies by declared income and chosen Krankenkasse

**Deutsche Rentenversicherung:**
- Description: "DEUTSCHE RENTENVERSICHERUNG" or "DRV BUND"
- Timing: Monthly (end of month for voluntary)
- Amount: Fixed chosen amount between EUR 100.07 and EUR 1,497.30

**Berufsgenossenschaft:**
- Description: BG name + "BEITRAG" + year
- Timing: Annual (typically Q1/Q2 for prior year)
- Amount: Varies by risk class and income

**Key identification tips:**
1. GKV debits are the most frequent -- monthly on the 15th
2. KSK debits combine health + pension (member share only)
3. BG debits are annual or quarterly and often reference the prior year
4. Finanzamt debits are TAX, not social contributions -- do not confuse
5. Provisional GKV amounts may be retroactively adjusted

---

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Scan for Krankenkasse debits** -- identify the health insurer and monthly amount
2. **Determine GKV or PKV** -- Krankenkasse names (TK, AOK, Barmer, etc.) = GKV; Allianz PKV, Debeka, DKV = PKV
3. **Identify KSK if present** -- KSK debits indicate artist/writer/journalist status
4. **Sum annual contributions** -- total GKV + PV + pension + BG
5. **Flag:** "Social contribution classification derived from bank statement patterns. Actual Zusatzbeitrag, income assessment base, and pension obligation type have not been independently verified. Reviewer must confirm before Anlage Vorsorgeaufwand is completed."

---

## Section 10 -- Reference material

### Contribution ceilings and minimums (2025)

| Parameter | KV/PV | Pension |
|---|---|---|
| BBG monthly | EUR 5,512.50 | EUR 8,050.00 |
| BBG annual | EUR 66,150.00 | EUR 96,600.00 |
| Minimum (monthly, GKV self-employed) | EUR 1,248.33 | EUR 100.07 (voluntary) |
| JAEG (employees only) | EUR 73,800.00 | N/A |

### Test suite

**Test 1:** GKV, no sick pay, 2.5% Zusatzbeitrag, income EUR 3,500/month, childless age 35. -> KV: EUR 577.50. PV: EUR 147.00. Total: EUR 724.50/month = EUR 8,694/year.

**Test 2:** GKV, minimum income, 2.5% Zusatzbeitrag, 1 child, age 30. -> KV: EUR 205.97. PV: EUR 44.94. Total: EUR 250.91/month.

**Test 3:** GKV, with sick pay, 2.5%, income EUR 9,000/month, 2 children. -> Capped at EUR 5,512.50. KV: EUR 942.64. PV: EUR 184.67. Total: EUR 1,127.31/month.

**Test 4:** KSK member, income EUR 30,000/year, childless age 28. -> KV share: ~EUR 213.75. RV share: EUR 232.50. PV full: EUR 105.00. Total: ~EUR 551.25/month.

**Test 5:** Handwerker, 5 years in, income EUR 4,500/month. -> Mandatory pension: EUR 837.00/month.

**Test 6:** Employed full-time + side freelance EUR 8,000/year. -> If nebenberuflich: no separate GKV on freelance income. Flag T2.

**Test 7:** Vorsorgeaufwendungen: paid EUR 10,500 KV + EUR 2,400 PV + EUR 5,580 RV. -> KV + PV fully deductible. RV within cap. Total deduction: EUR 18,480.

**Test 8:** Kuenstlersozialabgabe: agency paid EUR 15,000 to freelancers. -> 5.0% = EUR 750 due by 31 March.

### Prohibitions

- NEVER compute without knowing GKV or PKV
- NEVER apply 50% KSK subsidy to Pflegeversicherung -- KSK members pay full PV
- NEVER assume pension is voluntary without checking profession
- NEVER tell GKV self-employed they can contribute below minimum base
- NEVER advise PKV-to-GKV switching is straightforward
- NEVER compute PKV premiums -- they are individual and risk-based
- NEVER advise electing Pflichtversicherung auf Antrag without emphasizing it is IRREVOCABLE
- NEVER ignore the Zusatzbeitrag
- NEVER present GKV provisional contributions as final
- NEVER conflate KV/PV BBG (EUR 5,512.50) with RV BBG (EUR 8,050)
- NEVER advise on Scheinselbstaendigkeit without escalating

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftspruefer, or equivalent licensed practitioner in Germany) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
