---
name: de-trade-tax
description: >
  Use this skill whenever asked about German Trade Tax (Gewerbesteuer / GewSt) for self-employed Gewerbetreibende. Trigger on phrases like "Gewerbesteuer", "trade tax Germany", "GewSt", "Hebesatz", "Gewerbeertrag", "Steuermessbetrag", "Freibetrag 24500", "Gewerbesteuer Anrechnung", "§35 EStG", "trade tax credit", "Hinzurechnungen", "Kürzungen", "GewSt 1 A", or any question about German municipal trade tax obligations. Covers the Gewerbeertrag computation, EUR 24,500 Freibetrag, 3.5% Steuermesszahl, Hebesatz by municipality, Anrechnung on Einkommensteuer (4.0x credit under §35 EStG), Hinzurechnungen and Kürzungen, effective rate analysis, and Vorauszahlungen. ALWAYS read this skill before touching any Gewerbesteuer work.
version: 1.0
jurisdiction: DE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Germany Trade Tax (Gewerbesteuer / GewSt) -- Gewerbetreibende Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Germany (Bundesrepublik Deutschland) |
| Jurisdiction Code | DE |
| Primary Legislation | Gewerbesteuergesetz (GewStG) |
| Supporting Legislation | Einkommensteuergesetz (EStG) §35 (Anrechnung); Gewerbesteuer-Durchführungsverordnung (GewStDV); Gewerbesteuer-Richtlinien (GewStR); Abgabenordnung (AO) |
| Tax Authority | Finanzamt (assessment) + Gemeinde/Stadt (collection) |
| Filing Portal | ELSTER (elster.de) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Steuerberater or Wirtschaftsprüfer |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: Freibetrag, Steuermesszahl, Hebesatz application, Anrechnung formula, filing deadlines. Tier 2: Hinzurechnungen classification, Kürzungen computation, multi-municipality apportionment. Tier 3: Organschaft, international PE allocation, Zerlegung between multiple Gemeinden, partnership GewSt. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Steuerberater must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any Gewerbesteuer figure, you MUST know:

1. **Is the client a Gewerbetreibender or Freiberufler?** [T1] -- GewSt applies ONLY to Gewerbetreibende (trade/business). Freiberufler (freelancers) are EXEMPT.
2. **Municipality (Gemeinde/Stadt)** [T1] -- determines the Hebesatz. MUST know the exact municipality.
3. **Gewinn aus Gewerbebetrieb (profit from trade)** [T1] -- from Anlage G / EÜR or Bilanz
4. **Any Hinzurechnungen (add-backs)?** [T2] -- interest on debt, rent, royalties, etc.
5. **Any Kürzungen (reductions)?** [T2] -- e.g., Grundbesitz (real property) owned
6. **Legal form** [T1] -- Einzelunternehmen (sole proprietor) or Personengesellschaft (partnership). Determines Freibetrag eligibility.
7. **Gewerbesteuer Vorauszahlungen already paid** [T1] -- advance GewSt payments made during the year

**If the client is a Freiberufler, STOP. Gewerbesteuer does not apply. Confirm Freiberufler status with the Finanzamt classification letter (Fragebogen zur steuerlichen Erfassung).**

---

## Step 1: Who Must Pay Gewerbesteuer? [T1]

**Legislation:** GewStG §2

| Category | GewSt Obligation |
|----------|-----------------|
| Gewerbetreibende (traders, retailers, manufacturers, service businesses) | YES -- GewSt applies |
| Freiberufler (doctors, lawyers, architects, engineers, IT consultants, artists, journalists) | NO -- exempt under §18 EStG |
| Mixed activity (Gewerbe + Freiberuf) | [T2] -- if activities are inseparable, entire income may be treated as Gewerbe (Abfärbetheorie / Infektionstheorie). Flag for Steuerberater. |

### Freiberufler vs Gewerbetreibender -- Key Distinction

The classification is determined by the Finanzamt based on the Fragebogen zur steuerlichen Erfassung filed at registration. The Finanzamt's classification letter is definitive.

**WARNING:** An IT consultant may be classified as Freiberufler (if providing intellectual/creative services) or Gewerbetreibender (if reselling software/hardware). The boundary is fact-specific. [T2] if classification is unclear.

---

## Step 2: Gewerbeertrag Computation [T1]

**Legislation:** GewStG §7

The Gewerbeertrag (trade income) is the adjusted profit from the Gewerbebetrieb.

### Formula

```
Gewerbeertrag = Gewinn_aus_Gewerbebetrieb
              + Hinzurechnungen (§8 GewStG)
              - Kürzungen (§9 GewStG)
```

### Starting Point

| Legal Form | Starting Point |
|------------|---------------|
| Einzelunternehmen (sole proprietor) | Gewinn from Anlage G (EÜR or Bilanz) |
| Personengesellschaft | Gewinn from gesonderte und einheitliche Feststellung |

---

## Step 3: Hinzurechnungen (Add-Backs) [T2]

**Legislation:** GewStG §8

Certain financing and rental costs that were already deducted as Betriebsausgaben must be partially added back.

| Category | Add-Back Rate | Threshold |
|----------|--------------|-----------|
| Interest on debt (Entgelte für Schulden) | 100% of amount | Subject to Freibetrag below |
| Rent for movable assets (Mieten für bewegliche WG) | 20% of rent | Subject to Freibetrag below |
| Rent for immovable assets (Mieten für unbewegliche WG) | 50% of rent | Subject to Freibetrag below |
| Royalties and licence fees (Lizenzgebühren) | 25% of amount | Subject to Freibetrag below |

### Hinzurechnungen Freibetrag

```
total_hinzurechnungen = interest_100% + movable_rent_20% + immovable_rent_50% + royalties_25%
if total_hinzurechnungen <= EUR 200,000: no add-back
if total_hinzurechnungen > EUR 200,000: add back 25% of the excess over EUR 200,000
```

**Simplified:** Most sole proprietors with modest financing costs fall below the EUR 200,000 threshold. Hinzurechnungen are relevant primarily for capital-intensive businesses.

**[T2] Flag for reviewer whenever Hinzurechnungen exceed EUR 50,000 (approaching threshold territory).**

---

## Step 4: Kürzungen (Reductions) [T2]

**Legislation:** GewStG §9

| Kürzung | Amount | Condition |
|---------|--------|-----------|
| Grundbesitzkürzung (real property) | 1.2% of Einheitswert of owned business property | Property must be owned by the Gewerbetreibender and used in the business |
| Extended Grundbesitzkürzung | Actual income from property | Only for Grundstücksunternehmen (property management companies) -- [T3] |

**Most sole proprietors:** Only the standard 1.2% Grundbesitzkürzung applies, and only if they own the business premises. If renting, no Kürzung.

---

## Step 5: Freibetrag [T1]

**Legislation:** GewStG §11 Abs. 1

| Entity Type | Freibetrag |
|-------------|-----------|
| Natürliche Personen (sole proprietors) | EUR 24,500 |
| Personengesellschaften | EUR 24,500 |
| Kapitalgesellschaften (GmbH, AG) | EUR 0 (no Freibetrag) |

```
gewerbeertrag_after_freibetrag = max(0, Gewerbeertrag - 24,500)
```

**If Gewerbeertrag <= EUR 24,500, GewSt = EUR 0. No trade tax is due.**

---

## Step 6: Steuermessbetrag [T1]

**Legislation:** GewStG §11 Abs. 2

```
Steuermessbetrag = gewerbeertrag_after_freibetrag × 3.5%
```

The Steuermesszahl (tax measurement rate) is a federal constant: **3.5%**.

The Finanzamt issues the Gewerbesteuermessbescheid (assessment notice) stating the Steuermessbetrag. The municipality then applies its Hebesatz.

---

## Step 7: Hebesatz and Final GewSt [T1]

**Legislation:** GewStG §16

```
Gewerbesteuer = Steuermessbetrag × Hebesatz / 100
```

The Hebesatz is set by each municipality. Minimum Hebesatz: 200%.

### Hebesätze -- Major Cities (2025)

| City | Hebesatz |
|------|----------|
| Berlin | 410% |
| Munich (München) | 490% |
| Hamburg | 470% |
| Frankfurt am Main | 460% |
| Cologne (Köln) | 475% |
| Düsseldorf | 440% |
| Stuttgart | 420% |
| Leipzig | 460% |
| Dresden | 450% |
| Monheim am Rhein | 250% (lowest major rate in Germany) |

**WARNING:** Hebesätze change. Always verify the current Hebesatz with the municipality (Gemeindeverwaltung) or Steuerberater. The rates above are indicative for 2025.

---

## Step 8: Anrechnung on Einkommensteuer (§35 EStG) [T1]

**Legislation:** EStG §35 Abs. 1

Sole proprietors and partners can credit GewSt against their income tax. This is the key mechanism that makes GewSt effectively neutral for many businesses.

### Formula

```
Anrechnungsbetrag = min(Steuermessbetrag × 4.0, actual_ESt_on_gewerbliche_Einkünfte)
```

The credit is **4.0 times the Steuermessbetrag**, capped at the actual income tax attributable to the Gewerbe income.

### Effective Rate Analysis

```
GewSt_rate = Hebesatz × 3.5% / 100
Anrechnung_rate = 4.0 × 3.5% = 14.0%
Net_effective_GewSt = GewSt_rate - 14.0%
```

| Hebesatz | GewSt Rate | Anrechnung | Net Effective Rate |
|----------|-----------|------------|-------------------|
| 200% | 7.0% | 14.0% | 0% (fully offset) |
| 300% | 10.5% | 14.0% | 0% (fully offset) |
| 400% | 14.0% | 14.0% | 0% (fully offset) |
| 410% (Berlin) | 14.35% | 14.0% | 0.35% |
| 440% (Düsseldorf) | 15.4% | 14.0% | 1.4% |
| 470% (Hamburg) | 16.45% | 14.0% | 2.45% |
| 490% (Munich) | 17.15% | 14.0% | 3.15% |

**Key insight:** For municipalities with Hebesatz <= 400%, GewSt is effectively free for sole proprietors (fully offset by §35 credit). Above 400%, only the excess costs real money.

### Limitations on Anrechnung

| Limitation | Detail |
|-----------|--------|
| Cap | Cannot exceed the actual ESt on gewerbliche Einkünfte |
| Low income | If ESt is low (e.g., income near Grundfreibetrag), the credit may exceed the ESt, creating a partial loss of credit |
| No carryforward | Unused Anrechnung is lost -- it cannot be carried forward |
| Solidaritätszuschlag | The Anrechnung does NOT reduce Solidaritätszuschlag -- only ESt |

---

## Step 9: GewSt Vorauszahlungen (Advance Payments) [T1]

**Legislation:** GewStG §19

| Aspect | Detail |
|--------|--------|
| Frequency | Quarterly: 15 February, 15 May, 15 August, 15 November |
| Basis | Prior year's GewSt (Gewerbesteuermessbescheid) |
| Each payment | 25% of the annual GewSt |
| Minimum | No Vorauszahlung if annual GewSt < EUR 50 |
| Adjustment | Finanzamt adjusts Vorauszahlungen when a new Messbescheid is issued |

---

## Step 10: Filing and Deadlines [T1]

**Legislation:** GewStG §14a; AO §149

| Requirement | Deadline |
|-------------|----------|
| Gewerbesteuererklärung (GewSt 1 A) | 31 July of the following year (with Steuerberater: extended to end of February of the year after) |
| Filing method | ELSTER (electronic, mandatory) |
| Supporting forms | GewSt 1 A main form + Anlage EMU (if Hinzurechnungen/Kürzungen apply) |

---

## Step 11: Full Computation Walkthrough [T1]

### Example: Sole Proprietor in Berlin, Profit EUR 80,000

```
Step 1: Gewinn aus Gewerbebetrieb         = EUR 80,000
Step 2: + Hinzurechnungen                 = EUR 0 (below EUR 200,000 threshold)
Step 3: - Kürzungen                       = EUR 0 (rents business premises)
Step 4: = Gewerbeertrag                   = EUR 80,000
Step 5: - Freibetrag                      = EUR 24,500
Step 6: = Gewerbeertrag (taxable)         = EUR 55,500
Step 7: × Steuermesszahl 3.5%             = EUR 1,942.50
Step 8: × Hebesatz 410% (Berlin)          = EUR 7,964.25
Step 9: ESt Anrechnung (4.0 × EUR 1,942.50) = EUR 7,770.00
Step 10: Net effective GewSt cost         = EUR 7,964.25 - EUR 7,770.00 = EUR 194.25
```

**Net cost of GewSt for this Berlin sole proprietor: EUR 194.25** (effectively 0.24% of the Gewerbeertrag above Freibetrag).

---

## Step 12: Edge Case Registry

### EC1 -- Freiberufler reclassified as Gewerbetreibender [T2]
**Situation:** IT consultant was treated as Freiberufler for 3 years. Finanzamt reclassifies as Gewerbetreibender after a Betriebsprüfung (tax audit).
**Resolution:** GewSt becomes due retroactively for all open years. §35 Anrechnung can be claimed retroactively on amended ESt returns. [T2] flag for Steuerberater -- significant financial and compliance impact.

### EC2 -- Gewerbeertrag below Freibetrag [T1]
**Situation:** Sole proprietor with Gewinn = EUR 18,000.
**Resolution:** Gewerbeertrag EUR 18,000 < Freibetrag EUR 24,500. GewSt = EUR 0. No GewSt return required if Finanzamt has not requested one, but recommended to file anyway.

### EC3 -- Abfärbetheorie (infection theory) for mixed activity [T2]
**Situation:** Freiberufler (architect) also sells building materials (Gewerbe). Revenue from materials = EUR 5,000, total revenue = EUR 100,000.
**Resolution:** If the gewerbliche activity exceeds the de minimis threshold (3% of total revenue AND EUR 24,500 absolute), the ENTIRE income may be reclassified as gewerblich. EUR 5,000 / EUR 100,000 = 5% > 3%. [T2] flag for Steuerberater. Separation into distinct businesses (sachliche Trennung) may be possible.

### EC4 -- Anrechnung exceeds ESt on Gewerbe income [T1]
**Situation:** Sole proprietor in low-Hebesatz municipality. Gewerbeertrag = EUR 30,000. ESt on this income (marginal) = EUR 3,000. Anrechnung = EUR 770. GewSt = EUR 385 (Hebesatz 200%).
**Resolution:** Anrechnung (EUR 770) > GewSt paid (EUR 385). Credit is limited to actual GewSt paid. BUT: Anrechnung is also limited to ESt on gewerbliche Einkünfte. Excess Anrechnung over ESt is lost.

### EC5 -- Client moves municipality mid-year [T2]
**Situation:** Business relocates from Munich (490%) to Leipzig (460%) in June.
**Resolution:** Zerlegung (apportionment) applies if the business had Betriebsstätten in both municipalities during the year. GewSt is apportioned based on payroll (Arbeitslöhne) in each municipality. For sole proprietors without employees, the municipality where the business is registered at year-end typically applies. [T2] flag for Steuerberater.

### EC6 -- GewSt Vorauszahlung significantly exceeds actual liability [T1]
**Situation:** Vorauszahlungen paid: EUR 8,000. Actual GewSt = EUR 3,000.
**Resolution:** Overpayment of EUR 5,000. The Gemeinde issues a refund after the Gewerbesteuerbescheid is finalised. Processing time varies by municipality.

### EC7 -- Sole proprietor with significant interest expenses [T2]
**Situation:** Business loan interest = EUR 50,000. All deducted as Betriebsausgaben in EÜR.
**Resolution:** Hinzurechnung: 100% of EUR 50,000 = EUR 50,000 (below EUR 200,000 Freibetrag for Hinzurechnungen). No add-back. But if combined with rent and royalties, total may exceed threshold. [T2] flag if total Hinzurechnungen approach EUR 150,000+.

### EC8 -- Gewerbeanmeldung vs Finanzamt registration [T1]
**Situation:** Client registered Gewerbe with the Gewerbeamt but forgot to register with the Finanzamt.
**Resolution:** GewSt obligation arises from the Gewerbeanmeldung, regardless of Finanzamt registration. The Gewerbeamt forwards the registration to the Finanzamt. Client should proactively register with Finanzamt (Fragebogen zur steuerlichen Erfassung) to avoid penalties.

### EC9 -- Kirchensteuer interaction with GewSt Anrechnung [T1]
**Situation:** Client is a church member. Does the §35 Anrechnung also reduce Kirchensteuer?
**Resolution:** No. The §35 credit reduces only the Einkommensteuer. Kirchensteuer (8% or 9% of ESt) is computed on the ESt BEFORE the §35 Anrechnung. Solidaritätszuschlag is also computed before Anrechnung.

---

## Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Steuerberater must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Steuerberater. Document gap.
```

---

## Step 14: Test Suite

### Test 1 -- Standard computation, Berlin
**Input:** Sole proprietor, Berlin (Hebesatz 410%), Gewinn = EUR 80,000, no Hinzurechnungen/Kürzungen.
**Expected output:** Gewerbeertrag = EUR 80,000. After Freibetrag = EUR 55,500. Messbetrag = EUR 1,942.50. GewSt = EUR 7,964.25. Anrechnung = EUR 7,770.00. Net cost = EUR 194.25.

### Test 2 -- Below Freibetrag
**Input:** Sole proprietor, Hamburg (470%), Gewinn = EUR 20,000.
**Expected output:** Gewerbeertrag EUR 20,000 < Freibetrag EUR 24,500. GewSt = EUR 0. No Anrechnung needed.

### Test 3 -- Low Hebesatz, full offset
**Input:** Sole proprietor, Monheim am Rhein (250%), Gewinn = EUR 60,000. Sufficient ESt liability.
**Expected output:** Gewerbeertrag after Freibetrag = EUR 35,500. Messbetrag = EUR 1,242.50. GewSt = EUR 3,106.25. Anrechnung = EUR 4,970.00. Net cost = EUR 0 (fully offset, excess Anrechnung lost).

### Test 4 -- Munich, high Hebesatz
**Input:** Sole proprietor, Munich (490%), Gewinn = EUR 100,000, no Hinzurechnungen/Kürzungen.
**Expected output:** After Freibetrag = EUR 75,500. Messbetrag = EUR 2,642.50. GewSt = EUR 12,948.25. Anrechnung = EUR 10,570.00. Net cost = EUR 2,378.25.

### Test 5 -- Freiberufler (no GewSt)
**Input:** Freelance architect, classified as Freiberufler by Finanzamt, Gewinn = EUR 90,000.
**Expected output:** GewSt does NOT apply. EUR 0. No GewSt return required.

### Test 6 -- Vorauszahlungen computation
**Input:** Prior year GewSt = EUR 6,000.
**Expected output:** Quarterly Vorauszahlungen = EUR 1,500 each. Due: 15 Feb, 15 May, 15 Aug, 15 Nov.

### Test 7 -- Anrechnung limited by low ESt
**Input:** Sole proprietor, Berlin (410%), Gewerbeertrag after Freibetrag = EUR 10,000. ESt on gewerbliche Einkünfte = EUR 1,200.
**Expected output:** Messbetrag = EUR 350. GewSt = EUR 1,435. Anrechnung = min(EUR 1,400, EUR 1,200) = EUR 1,200. Net cost = EUR 235.

---

## PROHIBITIONS

- NEVER apply Gewerbesteuer to a Freiberufler -- GewSt is ONLY for Gewerbetreibende
- NEVER use a Hebesatz without verifying it with the specific municipality -- rates change annually
- NEVER forget the EUR 24,500 Freibetrag for sole proprietors and partnerships
- NEVER apply the §35 Anrechnung to Solidaritätszuschlag or Kirchensteuer -- it reduces only ESt
- NEVER assume Hinzurechnungen apply without checking the EUR 200,000 aggregate threshold
- NEVER carry forward unused Anrechnung -- it is lost if it exceeds the ESt cap
- NEVER classify a mixed-activity client without flagging Abfärbetheorie risk for Steuerberater review
- NEVER compute GewSt for a Kapitalgesellschaft using the EUR 24,500 Freibetrag -- Freibetrag is zero for GmbH/AG
- NEVER present Hebesatz figures as definitive -- always note they are subject to annual municipal decision

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
