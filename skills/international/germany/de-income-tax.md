---
name: de-income-tax
description: Use this skill whenever asked about German income tax (Einkommensteuer) for self-employed individuals (Freiberufler and Gewerbetreibende). Trigger on phrases like "how much tax do I pay in Germany", "Einkommensteuererklärung", "ESt", "Anlage S", "Anlage G", "EÜR", "Einnahmenüberschussrechnung", "Grundfreibetrag", "Solidaritätszuschlag", "Kirchensteuer", "Betriebsausgaben", "AfA", "Abschreibung", "GWG", "Vorsorgeaufwendungen", "Sonderausgaben", "German income tax return", "self-employed tax Germany", or any question about filing or computing income tax for a self-employed client in Germany. Also trigger when preparing or reviewing an Einkommensteuererklärung, computing deductible expenses, or advising on Vorauszahlungen (advance tax payments). This skill covers progressive tax rates (Grundtarif/Splittingtarif), EÜR structure, allowable Betriebsausgaben, AfA (depreciation), Vorsorgeaufwendungen, Sonderausgaben, Solidaritätszuschlag, Kirchensteuer, filing deadlines, and penalties. ALWAYS read this skill before touching any German income tax work.
---

# Germany Income Tax (Einkommensteuer) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Germany (Bundesrepublik Deutschland) |
| Jurisdiction Code | DE |
| Primary Legislation | Einkommensteuergesetz (EStG) |
| Supporting Legislation | Einkommensteuer-Durchführungsverordnung (EStDV); Solidaritätszuschlaggesetz (SolzG); Kirchensteuergesetze der Länder; Abgabenordnung (AO); Gewerbesteuergesetz (GewStG); Umsatzsteuergesetz (UStG) |
| Tax Authority | Bundeszentralamt für Steuern (BZSt) / Finanzamt (local tax office) |
| Filing Portal | ELSTER (elster.de) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Steuerberater or Wirtschaftsprüfer |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: rate table application, Grundfreibetrag, EÜR structure, GWG thresholds, AfA rates, filing deadlines, penalty rates. Tier 2: mixed-use expense apportionment, Arbeitszimmer, Bewirtungskosten, Reisekosten, Kirchensteuer rate by Bundesland, first-year Vorauszahlungen. Tier 3: Gewerbesteuer interaction, international income, complex depreciation (Sonder-AfA), partnership structures. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified tax professional (Steuerberater) must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Self-employment type** [T1] -- Freiberufler (freelancer, Anlage S) or Gewerbetreibender (trade/business, Anlage G). Determines which Anlage to file and whether Gewerbesteuer applies.
2. **Marital status** [T1] -- single (Grundtarif) or married/civil partnership filing jointly (Splittingtarif). Determines which tariff applies.
3. **Gross business revenue (Betriebseinnahmen)** [T1] -- total received/invoiced in the year.
4. **Business expenses (Betriebsausgaben)** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items).
5. **Capital assets acquired in the year** [T1] -- type, cost (net of deductible Vorsteuer), date first used in business.
6. **Vorsorgeaufwendungen** [T1] -- pension contributions (gesetzliche Rentenversicherung, Rürup/Basisrente), health insurance (Krankenversicherung), long-term care insurance (Pflegeversicherung).
7. **Kirchensteuer status** [T2] -- whether the client is a member of a church that levies Kirchensteuer, and which Bundesland (8% or 9%).
8. **Other income** [T1] -- employment income (Einkünfte aus nichtselbständiger Arbeit), rental income, capital income, etc.
9. **Vorauszahlungen paid** [T1] -- advance tax payments already made during the year.
10. **Umsatzsteuer regime** [T1] -- Regelbesteuerung (standard VAT) or Kleinunternehmerregelung (small business exemption under §19 UStG). Affects whether VAT is included in income/expenses.

**If self-employment type (Freiberufler vs Gewerbetreibender) is unknown, STOP. This determines the entire filing structure.**

---

## Step 1: Freiberufler vs Gewerbetreibender -- Anlage S vs Anlage G [T1/T2]

**Legislation:** EStG §18 (Freiberufler), EStG §15 (Gewerbetreibender), GewStG

### Freiberufler (Freelancer) -- Anlage S [T1]

| Criterion | Detail |
|-----------|--------|
| Legal basis | EStG §18 |
| Activities | Wissenschaftliche, künstlerische, schriftstellerische, unterrichtende, erzieherische Tätigkeit; Ärzte, Rechtsanwälte, Steuerberater, Architekten, Ingenieure, IT-Berater (catalogue professions and similar) |
| Gewerbesteuer | NOT subject to Gewerbesteuer |
| Trade registration | No Gewerbeanmeldung required |
| Filing form | Anlage S attached to ESt 1 A |
| Profit determination | EÜR (Einnahmenüberschussrechnung) unless voluntary Bilanz |

### Gewerbetreibender (Trader/Business) -- Anlage G [T1]

| Criterion | Detail |
|-----------|--------|
| Legal basis | EStG §15 |
| Activities | Any commercial, trade, or manufacturing activity not qualifying as freiberuflich |
| Gewerbesteuer | Subject to Gewerbesteuer (BUT Anrechnung on ESt via §35 EStG) [T3 for computation] |
| Trade registration | Gewerbeanmeldung required |
| Filing form | Anlage G attached to ESt 1 A |
| Profit determination | EÜR if revenue under EUR 600,000 AND profit under EUR 60,000; otherwise Bilanz (double-entry) required |

### Key Distinction [T2]

If the client's activity is ambiguous (e.g., IT consultant who also sells products), flag for reviewer. The Finanzamt may reclassify a Freiberufler as Gewerbetreibender if the activity includes significant commercial elements. This triggers Gewerbesteuer liability retroactively.

**Gewerbesteuer computation is [T3] -- do not compute. Escalate to Steuerberater. Note only that Gewerbetreibende receive a partial Anrechnung (credit) of Gewerbesteuer against Einkommensteuer under §35 EStG (factor 4.0 x Gewerbesteuer-Messbetrag, capped at actual ESt).**

---

## Step 2: EÜR -- Einnahmenüberschussrechnung (Cash-Basis Profit Computation) [T1]

**Legislation:** EStG §4(3); EStDV §60(4); Anlage EÜR (standardised form)

### Principle [T1]

Profit = Betriebseinnahmen (business receipts) minus Betriebsausgaben (business expenses).

Cash basis: income is recognised when received, expenses when paid. Exceptions: AfA (depreciation) follows its own schedule regardless of cash flow.

### Anlage EÜR Structure (Key Lines) [T1]

| Line Area | Description | How to Populate |
|-----------|-------------|-----------------|
| Lines 11-13 | Betriebseinnahmen (business revenue) | Total received in the year. For Regelbesteuerung: net of USt. For Kleinunternehmer: gross (no USt charged). |
| Line 14 | Vereinnahmte Umsatzsteuer | USt collected on sales (Regelbesteuerung only) |
| Lines 23-65 | Betriebsausgaben (business expenses) | Each expense category on its designated line |
| Lines 28-34 | AfA (depreciation) | Computed per AfA tables |
| Line 49 | Bewirtungskosten (entertainment) | 70% of business entertainment (see Step 3) |
| Line 63 | Gezahlte Vorsteuerbeträge | Input VAT paid on purchases (Regelbesteuerung only) |
| Line 64 | An das Finanzamt gezahlte USt | USt remitted to Finanzamt |
| Line 86 | Gewinn/Verlust (profit/loss) | Betriebseinnahmen minus Betriebsausgaben |

### Electronic Filing [T1]

The Anlage EÜR must be submitted electronically via ELSTER. A separate EÜR is required for each business activity. Paper filing is only permitted in hardship cases upon application.

### USt Treatment in EÜR [T1]

| Regime | Income Treatment | Expense Treatment |
|--------|-----------------|-------------------|
| Regelbesteuerung (standard VAT) | Revenue = net amount; collected USt goes to Line 14 as separate income; paid USt to Finanzamt is a Betriebsausgabe (Line 64) | Expenses = net amount; input VAT (Vorsteuer) goes to Line 63 as separate expense |
| Kleinunternehmerregelung (§19 UStG) | Revenue = gross (no USt charged) | Expenses = gross (no Vorsteuer deduction; full gross is the cost) |

---

## Step 3: Betriebsausgaben -- Business Expenses [T1/T2]

**Legislation:** EStG §4(4), §4(5), §12

### The Test [T1]

An expense is deductible if it is **betrieblich veranlasst** (caused by the business). Expenses of a private nature (Lebensführung) under §12 EStG are not deductible. Mixed-use expenses must be apportioned.

### Deductible Expenses

| Expense | Tier | Treatment | EÜR Line |
|---------|------|-----------|----------|
| Office rent (Büromiete) | T1 | Fully deductible | Line 45 |
| Professional insurance (Berufshaftpflicht) | T1 | Fully deductible | Line 46 |
| Steuerberatungskosten (tax advisor fees) | T1 | Fully deductible (business portion) | Line 65 |
| Rechts- und Beratungskosten (legal/consulting fees) | T1 | Fully deductible | Line 65 |
| Office supplies (Bürobedarf) | T1 | Fully deductible | Line 51 |
| Software subscriptions | T1 | Fully deductible if annual/recurring | Line 51 |
| Marketing / advertising (Werbekosten) | T1 | Fully deductible | Line 47 |
| Fortbildungskosten (professional development) | T1 | Fully deductible if business-related | Line 44 |
| Telefon-/Internetkosten | T2 | Business-use portion only; client must document %. Flat-rate: 20% of total bill, max EUR 20/month accepted without detailed proof | Line 48 |
| Reisekosten (business travel) | T1/T2 | See Reisekosten rules below | Lines 40-43 |
| Bewirtungskosten (business entertainment) | T1 | **70% deductible** (30% non-deductible under §4(5) Nr. 2 EStG). Proper receipt required with names of guests, business reason, date, location. | Line 49 |
| Geschenke (business gifts) | T1 | Max EUR 50 net per person per year (§4(5) Nr. 1 EStG). Above EUR 50: fully non-deductible | Line 50 |
| Kfz-Kosten (motor vehicle) | T2 | Business-use portion only; Fahrtenbuch or 1%-Regelung | Lines 58-60 |
| Arbeitszimmer (home office) | T2 | See Arbeitszimmer rules below | Line 52 |
| Homeoffice-Pauschale | T1 | EUR 6/day, max 210 days = EUR 1,260/year (§4(5) Nr. 6c EStG). Alternative to Arbeitszimmer deduction. | Line 53 |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Private Lebensführung (personal expenses) | §12 EStG -- private/personal |
| Einkommensteuer, Solidaritätszuschlag, Kirchensteuer | §12 Nr. 3 EStG -- personal taxes |
| Geldstrafen, Geldbußen (fines/penalties) | §4(5) Nr. 8 EStG -- public policy |
| Bestechungsgelder (bribes) | §4(5) Nr. 10 EStG |
| Private Entnahmen (drawings) | Not an expense -- equity withdrawal |
| Bewirtungskosten -- 30% portion | §4(5) Nr. 2 -- only 70% deductible |
| Geschenke above EUR 50/person/year | §4(5) Nr. 1 -- fully blocked above threshold |
| Unangemessene Aufwendungen (unreasonable expenditure) | §4(5) Nr. 7 EStG |

### Reisekosten Rules [T1/T2]

**Legislation:** EStG §4(5) Nr. 5, §9(1) Nr. 4a, R 9.4-9.8 LStR

| Component | Rule |
|-----------|------|
| Verpflegungsmehraufwand (meal allowance) | Absence 8-24h: EUR 14/day. Absence 24h+: EUR 28/day. Arrival/departure day: EUR 14. |
| Übernachtungskosten (accommodation) | Actual cost, fully deductible with receipt |
| Fahrtkosten (travel costs) | Actual cost or EUR 0.30/km (first 20 km) + EUR 0.38/km (from 21st km) for car |
| Foreign travel | Country-specific per diem rates per BMF letter (updated annually) [T2] |

### Bewirtungskosten (Business Entertainment) [T1]

- **70% deductible** of the net amount (before USt)
- Receipt must state: date, location, names of all attendees, business reason, cost breakdown (food/drink)
- The receipt must be a Bewirtungsbeleg from the restaurant (not a self-written note)
- Missing documentation = fully non-deductible
- Bewirtung of employees only (no external guests) = 100% deductible as Aufmerksamkeiten

### Arbeitszimmer (Home Office) Rules [T2]

**Legislation:** EStG §4(5) Nr. 6b

| Scenario | Treatment |
|----------|-----------|
| Arbeitszimmer is the **Mittelpunkt der gesamten beruflichen Tätigkeit** (centre of entire professional activity) | Fully deductible: proportional rent/mortgage interest, utilities, insurance, maintenance, depreciation of building portion |
| No Arbeitszimmer or not the Mittelpunkt | Use Homeoffice-Pauschale instead: EUR 6/day, max EUR 1,260/year |
| Dual-use room (also used privately) | NOT deductible. Room must be used (nearly) exclusively for business. |

**[T2]** Flag for reviewer: confirm room is separately identifiable, used (nearly) exclusively for business, and whether it qualifies as Mittelpunkt. The Mittelpunkt test considers where the core of the taxpayer's work is performed (qualitative, not quantitative).

### Kfz (Motor Vehicle) Rules [T2]

**Legislation:** EStG §6(1) Nr. 4, §4(5) Nr. 6

| Method | Description |
|--------|-------------|
| Fahrtenbuch | Full log of all business and private trips. Business % applied to total costs (fuel, insurance, repairs, depreciation, tax). |
| 1%-Regelung | Private use = 1% of Bruttolistenpreis (gross list price) per month added as taxable income. Only for vehicles used >50% for business. |
| Kilometerpauschale | For occasional business trips: EUR 0.30/km (simpler, no full cost tracking) |

**[T2]** Flag for reviewer: confirm business-use percentage and method choice. The Finanzamt may reject a Fahrtenbuch if it contains inconsistencies.

---

## Step 4: AfA -- Absetzung für Abnutzung (Depreciation) [T1]

**Legislation:** EStG §7, §6(2), §6(2a); AfA-Tabellen (BMF)

### Depreciation Methods [T1]

| Method | Applicability |
|--------|---------------|
| Lineare AfA (straight-line) | Standard method. Cost / useful life = annual amount. §7(1) EStG. |
| Degressive AfA (declining balance) | Available for assets acquired after 31 March 2024 and before 1 January 2025: up to 2x linear rate, max 20%. Check availability for 2025 acquisitions. [T2] |
| GWG Sofortabschreibung (immediate write-off) | Assets up to EUR 800 net. §6(2) EStG. |
| Sammelposten (pool depreciation) | Assets EUR 250.01 to EUR 1,000 net. 5-year pool, 20%/year. §6(2a) EStG. |

### Common Useful Lives (AfA-Tabellen) [T1]

| Asset Type | Useful Life (Years) | Annual Linear Rate |
|-----------|---------------------|-------------------|
| Computer hardware (PC, laptop, monitor) | 1 year (since BMF 2021-02-26) | 100% (immediate write-off in year of acquisition) |
| Computer software (standard) | 1 year (since BMF 2021-02-26) | 100% (immediate write-off in year of acquisition) |
| Mobile phones | 5 years | 20% |
| Office furniture (Büromöbel) | 13 years | 7.7% |
| Motor vehicles (Pkw) | 6 years | 16.67% |
| Office equipment (printers, copiers) | 7 years | 14.3% |
| Buildings (commercial, masonry) | 33 years | 3% |
| Buildings (residential, new from 2023) | 33 years | 3% |

**Note (Computer hardware/software):** Since BMF letter dated 26.02.2021, the useful life for computer hardware and software has been set to 1 year, permitting immediate full write-off in the year of acquisition regardless of cost. This applies to both GWG and non-GWG items. This is NOT GWG treatment -- it is a special AfA rule.

### GWG -- Geringwertige Wirtschaftsgüter (Low-Value Assets) [T1]

**Legislation:** EStG §6(2)

| Threshold (Net of USt) | Treatment |
|------------------------|-----------|
| Up to EUR 250 | Immediate expense. No asset register entry required. |
| EUR 250.01 to EUR 800 | GWG: immediate full write-off in year of acquisition. Must be recorded in asset register (Anlageverzeichnis) with acquisition cost, date, description. |
| EUR 250.01 to EUR 1,000 | Alternative: Sammelposten. Pool all items, depreciate 20%/year over 5 years. §6(2a) EStG. Once chosen for a year, applies to ALL assets in this range for that year. |

**GWG vs Sammelposten choice [T1]:** The taxpayer chooses one method per year. If GWG is chosen, assets up to EUR 800 are written off immediately, and assets EUR 800.01+ follow normal AfA. If Sammelposten is chosen, ALL assets EUR 250.01-1,000 go into the pool (no individual GWG write-off).

### AfA Pro-Rata Rule [T1]

For assets acquired mid-year: depreciation is calculated pro-rata by month. The month of acquisition counts as a full month (§7(1) S.4 EStG). Exception: GWG and computer hardware/software (1-year rule) are written off in full in the year of acquisition regardless of acquisition date.

---

## Step 5: Einkommensteuer-Tarif (Tax Rates) -- Grundtarif [T1]

**Legislation:** EStG §32a (as amended for 2025)

### Tax Zones (Single -- Grundtarif) [T1]

| Zone | Taxable Income (EUR) | Rate | Description |
|------|---------------------|------|-------------|
| 1 | 0 to 12,096 | 0% | Grundfreibetrag -- tax-free subsistence minimum |
| 2 | 12,097 to 17,443 | 14% to ~24% | Progressive zone 1 (formula-based, not flat steps) |
| 3 | 17,444 to 68,480 | ~24% to 42% | Progressive zone 2 (formula-based, not flat steps) |
| 4 | 68,481 to 277,825 | 42% | Spitzensteuersatz (top rate) |
| 5 | 277,826+ | 45% | Reichensteuer (wealth tax surcharge rate) |

### Progressive Formula (§32a Abs. 1 EStG, 2025) [T1]

Germany does NOT use simple flat brackets. Zones 2 and 3 use quadratic formulas for smooth progression:

**Zone 1** (zvE up to EUR 12,096): ESt = 0

**Zone 2** (zvE EUR 12,097 to EUR 17,443):
- y = (zvE - 12,096) / 10,000
- ESt = (922.98 * y + 1,400) * y

**Zone 3** (zvE EUR 17,444 to EUR 68,480):
- z = (zvE - 17,443) / 10,000
- ESt = (181.19 * z + 2,397) * z + 869.32

**Zone 4** (zvE EUR 68,481 to EUR 277,825):
- ESt = 0.42 * zvE - 10,911.92

**Zone 5** (zvE EUR 277,826+):
- ESt = 0.45 * zvE - 19,246.67

Where zvE = zu versteuerndes Einkommen (taxable income), rounded down to full euros.

**NEVER compute ESt manually using these formulas -- pass zvE to the deterministic engine.**

### Splittingtarif (Married/Joint Filing) [T1]

**Legislation:** EStG §32a(5)

For married couples or registered civil partners filing jointly (Zusammenveranlagung):
1. Divide combined zvE by 2
2. Apply Grundtarif formula to the halved amount
3. Double the result

This effectively doubles all zone thresholds. Grundfreibetrag becomes EUR 24,192.

---

## Step 6: Solidaritätszuschlag [T1]

**Legislation:** Solidaritätszuschlaggesetz (SolzG)

| Parameter | Value (2025) |
|-----------|-------------|
| Rate | 5.5% of Einkommensteuer |
| Freigrenze (single) | EUR 19,950 of ESt |
| Freigrenze (married/joint) | EUR 39,900 of ESt |
| Milderungszone | For ESt slightly above the Freigrenze, Soli is phased in (not full 5.5% immediately) |

### Rules [T1]

- If ESt is at or below the Freigrenze: Soli = EUR 0
- If ESt exceeds the Freigrenze: Soli is capped at 11.9% of the amount by which ESt exceeds the Freigrenze (Milderungszone), OR 5.5% of ESt -- whichever is LOWER
- Once ESt is sufficiently above the Freigrenze, full 5.5% applies
- **Effectively abolished for the vast majority of taxpayers since 2021.** Only applies to high earners (roughly above EUR 100,000 single / EUR 200,000 married taxable income depending on deductions)

---

## Step 7: Kirchensteuer (Church Tax) [T2]

**Legislation:** Kirchensteuergesetze der Länder

| Parameter | Value |
|-----------|-------|
| Rate | 8% of ESt (Bayern, Baden-Württemberg) or 9% of ESt (all other Bundesländer) |
| Applies to | Members of a recognised Religionsgemeinschaft (Catholic, Protestant, some others) |
| Non-members | No Kirchensteuer. Confirm church membership status (Konfession on Lohnsteuerkarte or self-declaration). |
| Deductibility | Kirchensteuer paid is a Sonderausgabe and reduces zvE for the FOLLOWING year (or current year if paid in advance) |

**[T2]** Always confirm: (1) Is the client a church member? (2) Which Bundesland? If the client left the church (Kirchenaustritt) mid-year, Kirchensteuer applies pro-rata.

---

## Step 8: Vorsorgeaufwendungen (Pension/Insurance Deductions) [T1/T2]

**Legislation:** EStG §10

### Altersvorsorgeaufwendungen (Old-Age Pension Contributions) [T1]

| Type | Deductibility (2025) | Maximum |
|------|---------------------|---------|
| Gesetzliche Rentenversicherung (statutory pension) | 100% deductible (since 2023) | Max EUR 29,344 (single) / EUR 58,688 (married) |
| Rürup-Rente / Basisrente | 100% deductible | Combined with above maximum |
| Versorgungswerk (professional pension) | 100% deductible | Combined with above maximum |

### Sonstige Vorsorgeaufwendungen (Other Insurance Contributions) [T1]

| Type | Deductibility | Maximum |
|------|---------------|---------|
| Krankenversicherung (health insurance -- Basisbeiträge) | Fully deductible (Basisabsicherung only) | No cap for Basisbeiträge |
| Pflegeversicherung (long-term care insurance) | Fully deductible | No cap |
| Krankenversicherung (Wahlleistungen, Zusatzversicherungen) | Limited deductibility | Within EUR 2,800 (self-employed) cap for sonstige Vorsorge |
| Arbeitslosenversicherung | Limited deductibility | Within sonstige Vorsorge cap |
| Haftpflichtversicherung (private liability) | Limited deductibility | Within sonstige Vorsorge cap |
| Berufsunfähigkeitsversicherung (disability insurance) | Limited deductibility | Within sonstige Vorsorge cap |

**Sonstige Vorsorgeaufwendungen cap (self-employed):** EUR 2,800/year. However, Basisbeiträge for Kranken- and Pflegeversicherung are ALWAYS fully deductible, even if they exceed this cap. The cap only applies to other sonstige Vorsorge items, and in practice the Basisbeiträge often consume the entire cap, leaving no room for other items.

---

## Step 9: Sonderausgaben (Special Expenses) [T1/T2]

**Legislation:** EStG §10, §10b

| Type | Deductibility | Notes |
|------|---------------|-------|
| Kirchensteuer paid | Fully deductible | §10(1) Nr. 4 |
| Spenden (charitable donations) | Up to 20% of Gesamtbetrag der Einkünfte | §10b. Requires Spendenbescheinigung (donation receipt) |
| Steuerberatungskosten (private portion) | NOT deductible since 2006 | Only business-related portion is Betriebsausgabe |
| Schulgeld (school fees, private schools) | 30%, max EUR 5,000/child | §10(1) Nr. 9 |
| Sonderausgaben-Pauschbetrag | EUR 36 (single) / EUR 72 (married) | Minimum deduction if no higher Sonderausgaben claimed |

---

## Step 10: Computation Flow -- From Gross Revenue to Tax Due [T1]

### Step-by-step:

```
 1. Betriebseinnahmen (gross business revenue)
    - For Regelbesteuerung: net of USt
    - For Kleinunternehmer: gross amount

 2. MINUS Betriebsausgaben (business expenses per Step 3)
    = Gewinn aus selbständiger Arbeit (Anlage S)
      OR Gewinn aus Gewerbebetrieb (Anlage G)

 3. ADD other Einkünfte (employment, rental, capital, etc.)
    = Summe der Einkünfte

 4. MINUS Altersentlastungsbetrag (if applicable, born before 1975)
    = Gesamtbetrag der Einkünfte

 5. MINUS Vorsorgeaufwendungen (Step 8)
 6. MINUS Sonderausgaben (Step 9)
 7. MINUS Außergewöhnliche Belastungen (if applicable) [T2]
    = Zu versteuerndes Einkommen (zvE)

 8. APPLY Grundtarif or Splittingtarif (Step 5)
    = Tarifliche Einkommensteuer

 9. MINUS Steuerermäßigungen (tax reductions)
    - §35 EStG Gewerbesteuer-Anrechnung (Gewerbetreibende only) [T3]
    - §35a EStG haushaltsnahe Dienstleistungen [T2]
    = Festzusetzende Einkommensteuer

10. ADD Solidaritätszuschlag (Step 6)
11. ADD Kirchensteuer (Step 7)
    = Gesamte Steuerlast

12. MINUS Vorauszahlungen (advance payments made)
13. MINUS Anrechenbare Lohnsteuer (if any employment income)
    = Abschlusszahlung (tax due) or Erstattung (refund)
```

---

## Step 11: Vorauszahlungen (Advance Tax Payments) [T1]

**Legislation:** EStG §37

### Schedule [T1]

| Instalment | Due Date | Percentage |
|-----------|----------|------------|
| 1st quarter | 10 March | 25% |
| 2nd quarter | 10 June | 25% |
| 3rd quarter | 10 September | 25% |
| 4th quarter | 10 December | 25% |

### Rules [T1]

- Based on the **most recent Einkommensteuerbescheid** (tax assessment notice) -- NOT the most recent return filed
- The Finanzamt sets the Vorauszahlungen by Vorauszahlungsbescheid
- First year of self-employment: the Finanzamt estimates based on projected income declared in the Fragebogen zur steuerlichen Erfassung [T2]
- Taxpayer can apply to reduce (Herabsetzungsantrag) or increase Vorauszahlungen if income changes significantly
- Vorauszahlungen include ESt, Soli, and Kirchensteuer combined
- Minimum Vorauszahlung: EUR 400/year (EUR 100/quarter). Below this, no Vorauszahlungen are set.

---

## Step 12: Filing Deadlines [T1]

**Legislation:** AO §149

### For Tax Year 2025 [T1]

| Scenario | Deadline |
|----------|----------|
| Self-filing (without Steuerberater) | **31 July 2026** |
| With Steuerberater or Lohnsteuerhilfeverein | **28 February 2027** (extended to 1 March 2027 since 28 Feb is a Sunday) |
| Voluntary filing (Antragsveranlagung) | 4-year window: until 31 December 2029 |

### Mandatory Filing (Pflichtveranlagung) [T1]

Self-employed individuals (both Freiberufler and Gewerbetreibende) are ALWAYS required to file (§149 AO, §25(3) EStG, §46(2) Nr. 1-8 EStG). There is no threshold below which filing is optional for self-employed persons.

---

## Step 13: Penalties [T1]

**Legislation:** AO §152, §233a, §240

| Offence | Penalty |
|---------|---------|
| Verspätungszuschlag (late filing surcharge) | 0.25% of festgesetzte Steuer per month late, minimum EUR 25/month. Automatically assessed after 14 months (self-filers) or 19 months (with Steuerberater). |
| Verspätungszuschlag maximum | 25,000 EUR (AO §152(10)) |
| Nachzahlungszinsen (late payment interest) | 0.15% per month (1.8% per year) on the tax owed, beginning 15 months after end of tax year (§233a AO, as amended 2022) |
| Säumniszuschlag (delinquency surcharge on payment) | 1% per month on unpaid tax rounded down to nearest EUR 50 (§240 AO) |
| Steuerhinterziehung (tax evasion) | Up to 5 years imprisonment + fine (§370 AO) |
| Leichtfertige Steuerverkürzung (negligent underpayment) | Up to EUR 50,000 fine (§378 AO) |

**WARNING:** The Säumniszuschlag of 1%/month is severe and uncapped. Combined with Nachzahlungszinsen, total penalties accumulate rapidly. Any arrears situation must be escalated to a Steuerberater immediately.

---

## Step 14: Record Keeping [T1]

**Legislation:** AO §147

| Requirement | Detail |
|-------------|--------|
| Retention period -- Bücher, Aufzeichnungen, Bilanzen | 10 years |
| Retention period -- receipts, invoices, bank statements, all other documents | 8 years |
| Format | Paper or digital (GoBD-compliant digital archiving accepted) |
| GoBD compliance | Digitally archived documents must be unalterable, timestamped, and searchable (BMF letter on GoBD, 28.11.2019) |
| What to keep | All Einnahmen- and Ausgabenbelege, bank statements, contracts, asset register (Anlageverzeichnis), EÜR working papers, Vorauszahlungsbescheide |

---

## Step 15: Edge Case Registry

### EC1 -- Kleinunternehmer income treatment [T1]
**Situation:** Client is Kleinunternehmer (§19 UStG, no USt charged). They receive EUR 50,000 in total payments. How does this enter the EÜR?
**Resolution:** Full EUR 50,000 is Betriebseinnahmen (Line 11). No USt is collected, so Line 14 = EUR 0. Expenses are also gross (no Vorsteuer deduction).

### EC2 -- Bewirtungskosten without proper receipt [T1]
**Situation:** Client spent EUR 300 on a business dinner but only has a normal Kassenbon (no names of guests, no business reason documented).
**Resolution:** NOT deductible. Bewirtungskosten require a Bewirtungsbeleg with date, location, names of all attendees, business reason, and cost breakdown. Without proper documentation, the full amount is non-deductible. Not even 70%.

### EC3 -- Geschenke exceeding EUR 50 [T1]
**Situation:** Client gives a business gift costing EUR 60 net to a client.
**Resolution:** Fully non-deductible. The EUR 50 threshold under §4(5) Nr. 1 EStG is a Freigrenze (not a Freibetrag). Exceeding EUR 50 net per person per year makes the ENTIRE amount non-deductible, not just the excess.

### EC4 -- Computer hardware purchased for EUR 2,500 [T1]
**Situation:** Client buys a laptop for EUR 2,500 net in July 2025. How is it depreciated?
**Resolution:** Since BMF letter 26.02.2021, computer hardware has a 1-year useful life. The full EUR 2,500 is deductible in 2025 as AfA (not as GWG -- this is a separate rule based on the 1-year useful life). Enter in AfA lines of EÜR.

### EC5 -- GWG vs Sammelposten choice conflict [T1]
**Situation:** Client buys a desk for EUR 600 net and a chair for EUR 900 net in the same year.
**Resolution:** If GWG method chosen: desk (EUR 600, under EUR 800) = immediate write-off. Chair (EUR 900, above EUR 800) = normal AfA over 13 years. If Sammelposten chosen: both go into the 5-year pool (both are between EUR 250 and EUR 1,000). The choice applies to ALL such assets in the year. [T2] Flag for reviewer: evaluate which method is more beneficial.

### EC6 -- Freiberufler reclassified as Gewerbetreibender [T2]
**Situation:** IT consultant also sells hardware to clients. The Finanzamt argues this is a gewerbliche Tätigkeit.
**Resolution:** If the commercial element is not trivial, the ENTIRE activity may be reclassified as Gewerbe (Abfärbetheorie -- §15(3) Nr. 1 EStG), triggering Gewerbesteuer on all income. [T3] Escalate to Steuerberater. This can have retroactive consequences.

### EC7 -- Solidaritätszuschlag near threshold [T1]
**Situation:** Client's ESt is EUR 20,500 (single). Is Soli due?
**Resolution:** Yes, but in the Milderungszone. Soli = lesser of (5.5% x EUR 20,500 = EUR 1,127.50) and (11.9% x (EUR 20,500 - EUR 19,950) = EUR 65.45). Soli = EUR 65.45. The Milderungszone prevents a cliff effect at the Freigrenze.

### EC8 -- Kirchensteuer deductibility [T1]
**Situation:** Client paid EUR 3,000 Kirchensteuer during 2025. Where does it go?
**Resolution:** Kirchensteuer paid is a Sonderausgabe (§10(1) Nr. 4 EStG). It reduces the zvE. Enter in the Sonderausgaben section of the ESt return. It is NOT a Betriebsausgabe.

### EC9 -- Mixed Anlage S and Anlage G income [T2]
**Situation:** Client is a freelance designer (Freiberufler) AND runs a small online shop (Gewerbetreibender).
**Resolution:** Two separate EÜRs required, one for each activity. Design income goes to Anlage S. Shop income goes to Anlage G. Gewerbesteuer applies only to the shop income. Expenses must be allocated to the correct activity. [T2] Flag for reviewer: confirm expense allocation and separation of activities.

### EC10 -- Homeoffice-Pauschale vs Arbeitszimmer [T2]
**Situation:** Client works from a dedicated room at home. Should they claim the Arbeitszimmer deduction or the Homeoffice-Pauschale?
**Resolution:** If the room is the Mittelpunkt der gesamten beruflichen Tätigkeit AND is used (nearly) exclusively for business, the full Arbeitszimmer deduction (actual costs, proportional) will typically exceed the Pauschale (max EUR 1,260). However, the Arbeitszimmer requires extensive documentation. [T2] Flag for reviewer: compare both options, confirm Mittelpunkt status.

### EC11 -- First-year Vorauszahlungen [T2]
**Situation:** Client started self-employment in 2025. The Finanzamt sends a Vorauszahlungsbescheid based on estimated income of EUR 80,000.
**Resolution:** The Finanzamt's estimate may be too high or too low. Client can file a Herabsetzungsantrag (request to reduce) with supporting documentation (contracts, invoices to date). [T2] Flag for reviewer: assess whether the estimate is reasonable and whether an adjustment request is warranted.

---

## Step 16: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Steuerberater must confirm before filing.
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

## Step 17: Test Suite

### Test 1 -- Standard single Freiberufler, mid-range income
**Input:** Single, Freiberufler (Anlage S), gross revenue EUR 60,000, Betriebsausgaben EUR 12,000, no other income, Vorsorgeaufwendungen EUR 8,000 (Basiskrankenversicherung EUR 5,000, Rentenversicherung EUR 3,000), Sonderausgaben EUR 500 (Spenden), Vorauszahlungen paid EUR 5,000, no Kirchensteuer.
**Expected computation:** EÜR profit = EUR 48,000. zvE = EUR 48,000 - EUR 8,000 - EUR 500 = EUR 39,500. Apply Grundtarif Zone 3 formula. ESt approx EUR 8,687. Soli: ESt below EUR 19,950 Freigrenze, so Soli = EUR 0. Total tax = approx EUR 8,687. Minus Vorauszahlungen EUR 5,000. Abschlusszahlung approx EUR 3,687.

### Test 2 -- Married Gewerbetreibender, higher income
**Input:** Married (Zusammenveranlagung), spouse has no income, Gewerbetreibender (Anlage G), gross revenue EUR 120,000, Betriebsausgaben EUR 30,000, Vorsorgeaufwendungen EUR 12,000, Sonderausgaben EUR 1,000, no Vorauszahlungen (first year), no Kirchensteuer.
**Expected computation:** EÜR profit = EUR 90,000. zvE = EUR 90,000 - EUR 12,000 - EUR 1,000 = EUR 77,000. Splittingtarif: halve to EUR 38,500, apply Grundtarif, double result. ESt approx EUR 16,134. Soli: ESt below EUR 39,900 Freigrenze (married), so Soli = EUR 0. Gewerbesteuer-Anrechnung applies [T3 -- do not compute, flag]. Total due approx EUR 16,134 before GewSt credit.

### Test 3 -- GWG immediate write-off
**Input:** Freiberufler buys office chair EUR 700 net in March 2025, desk EUR 250 net, printer EUR 350 net.
**Expected output:** Desk EUR 250 = immediate expense (under EUR 250, no register). Chair EUR 700 = GWG, immediate write-off, record in Anlageverzeichnis. Printer EUR 350 = GWG, immediate write-off, record in Anlageverzeichnis. Total AfA/GWG deduction = EUR 1,300.

### Test 4 -- Bewirtungskosten correctly limited to 70%
**Input:** Client has EUR 1,000 net business entertainment expenses with proper Bewirtungsbelege.
**Expected output:** Deductible amount = EUR 700 (70%). Non-deductible = EUR 300. Enter EUR 700 in EÜR Line 49. The EUR 300 is an add-back (nicht abziehbare Betriebsausgabe).

### Test 5 -- Solidaritätszuschlag in Milderungszone
**Input:** Single, ESt = EUR 20,200.
**Expected output:** ESt exceeds Freigrenze of EUR 19,950 by EUR 250. Milderungszone Soli = 11.9% x EUR 250 = EUR 29.75. Full Soli would be 5.5% x EUR 20,200 = EUR 1,111. Apply lower amount: Soli = EUR 29.75.

### Test 6 -- Kirchensteuer computation (Bayern)
**Input:** Single, church member in Bayern, ESt = EUR 15,000.
**Expected output:** Kirchensteuer = 8% x EUR 15,000 = EUR 1,200. This EUR 1,200 is also a Sonderausgabe reducing zvE for the same or following year.

### Test 7 -- Computer hardware full write-off
**Input:** Freiberufler buys a MacBook Pro for EUR 3,200 net in October 2025.
**Expected output:** Full EUR 3,200 deductible as AfA in 2025 (1-year useful life per BMF 2021-02-26 letter). This is NOT GWG treatment; it is standard AfA with a 1-year useful life. No pro-rata reduction.

### Test 8 -- Homeoffice-Pauschale
**Input:** Freiberufler works from home 200 days in 2025. No dedicated Arbeitszimmer (works from living room).
**Expected output:** Homeoffice-Pauschale = 200 days x EUR 6 = EUR 1,200. Maximum allowed = EUR 1,260 (210 days). EUR 1,200 is within the limit. Deductible amount = EUR 1,200.

---

## PROHIBITIONS

- NEVER compute Einkommensteuer manually using the §32a formulas -- pass zvE to the deterministic engine
- NEVER apply Grundtarif to a married couple filing jointly -- use Splittingtarif (Ehegattensplitting)
- NEVER allow Bewirtungskosten above 70% deduction
- NEVER allow Geschenke above EUR 50 net per person per year as deductible
- NEVER allow Einkommensteuer, Solidaritätszuschlag, or Kirchensteuer as a Betriebsausgabe
- NEVER allow fines (Geldstrafen/Geldbußen) as a Betriebsausgabe
- NEVER include collected Umsatzsteuer in Betriebseinnahmen for Regelbesteuerung clients (it goes to Line 14 separately)
- NEVER allow a dual-use room (not exclusively business) as an Arbeitszimmer deduction
- NEVER compute Gewerbesteuer or Gewerbesteuer-Anrechnung -- this is [T3], escalate to Steuerberater
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Steuerberater for confirmation
- NEVER advise on arrears situations without escalating to a Steuerberater
- NEVER confuse GWG treatment with the 1-year computer hardware/software AfA rule -- they are separate mechanisms
- NEVER file an EÜR on paper without a hardship exemption from the Finanzamt

---

## Contribution Notes (For Adaptation)

If adapting this skill for another jurisdiction:

1. Replace EStG references with the equivalent national income tax legislation.
2. Replace the §32a progressive formula with your jurisdiction's equivalent rate table or formula.
3. Replace the EÜR structure with your jurisdiction's equivalent simplified profit computation form.
4. Replace Betriebsausgaben rules (Bewirtung 70%, Geschenke EUR 50) with your jurisdiction's equivalent deductibility limits.
5. Replace AfA tables and GWG thresholds with your jurisdiction's equivalent depreciation rules.
6. Replace Vorsorgeaufwendungen and Sonderausgaben with your jurisdiction's equivalent personal deductions.
7. Replace Solidaritätszuschlag and Kirchensteuer with any equivalent surcharges in your jurisdiction.
8. Replace filing deadlines and penalty rates with your jurisdiction's current figures.
9. Replace Vorauszahlungen schedule with your jurisdiction's equivalent instalment system.
10. Have a licensed practitioner in your jurisdiction validate every T1 rule before publishing.

**A skill may not be published without sign-off from a qualified practitioner (Steuerberater or equivalent) in the relevant jurisdiction.**

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater, Wirtschaftsprüfer, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
