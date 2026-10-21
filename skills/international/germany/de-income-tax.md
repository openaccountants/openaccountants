---
name: de-income-tax
description: >
  Use this skill whenever asked about German income tax (Einkommensteuer) for self-employed individuals (Freiberufler or Gewerbetreibende). Trigger on phrases like "how much tax do I pay in Germany", "Einkommensteuer", "Einkommensteuererklarung", "Anlage S", "Anlage G", "Anlage EUR", "Freiberufler tax", "Gewerbetreibende", "Solidaritatszuschlag", "Kirchensteuer", "Vorauszahlungen", "Betriebsausgaben", "AfA", "Abschreibung", "hausliches Arbeitszimmer", "Fahrtkosten", "Bewirtungskosten", "Grundfreibetrag", or any question about filing or computing income tax for a self-employed client in Germany. Covers Einkommensteuer progressive rates, Solidaritatszuschlag, Kirchensteuer, Anlage S/G/EUR structure, allowable Betriebsausgaben, AfA depreciation, home office, vehicle expenses, quarterly Vorauszahlungen, Gewerbesteuer credit, and interaction with Umsatzsteuer. ALWAYS read this skill before touching any German income tax work.
version: 2.1
jurisdiction: DE
tax_year: 2025
tier: 2
last_updated: 2026-10-21
review_status: pending_review
category: international
depends_on:
  - income-tax-workflow-base
verified_by: pending
---

# Germany Income Tax (Einkommensteuer) -- Self-Employed Skill v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Germany (Bundesrepublik Deutschland) |
| Tax | Einkommensteuer (ESt) + Solidaritatszuschlag (SolZ) + Kirchensteuer (KiSt, if applicable) |
| Currency | EUR only |
| Tax year | Calendar year (Kalenderjahr) |
| Primary legislation | Einkommensteuergesetz (EStG) |
| Supporting legislation | Abgabenordnung (AO); Gewerbesteuergesetz (GewStG); Umsatzsteuergesetz (UStG) |
| Tax authority | Finanzamt (local tax office) |
| Filing portal | ELSTER (elster.de) |
| Filing deadline | 31 July of the following year (with Steuerberater: end of February of the year after next) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a German Steuerberater |
| Validation date | Pending |
| Skill version | 2.1 |

### Tax Rate Brackets (2025)

| Taxable Income (EUR) | Rate | Notes |
|---|---|---|
| 0 -- 12,084 | 0% | Grundfreibetrag (basic allowance) |
| 12,085 -- 17,005 | 14% -- 24% | Progressive zone 1 (linear-progressive) |
| 17,006 -- 66,760 | 24% -- 42% | Progressive zone 2 (linear-progressive) |
| 66,761 -- 277,825 | 42% | Proportionalzone (flat) |
| 277,826+ | 45% | Reichensteuer (wealth tax surcharge) |

**Germany uses a FORMULA-BASED progressive rate, not simple bracket multiplication. Each euro is taxed at its own marginal rate within zones 1 and 2. Do not compute manually -- pass to the deterministic engine.**

### Solidaritatszuschlag (SolZ)

| Item | Value |
|---|---|
| Rate | 5.5% of the Einkommensteuer |
| Exemption threshold (single) | ESt up to EUR 18,130 -- no SolZ |
| Exemption threshold (married/joint) | ESt up to EUR 36,260 -- no SolZ |
| Gleitzone (phase-in) | 11.9% marginal rate on ESt between threshold and full-rate zone |

### Kirchensteuer (KiSt)

| Item | Value |
|---|---|
| Rate (most Lander) | 9% of ESt |
| Rate (Bavaria, Baden-Wurttemberg) | 8% of ESt |
| Applicability | Only if taxpayer is a registered church member |

### Gewerbesteuer Credit

| Item | Value |
|---|---|
| Credit against ESt | Factor 4.0 x Gewerbesteuer-Messbetrag |
| Cap | Cannot exceed actual Gewerbesteuer paid |
| Applicability | Gewerbetreibende only -- Freiberufler do NOT pay Gewerbesteuer |

### Key Anlage EUR Lines

| Line | Description |
|---|---|
| Betriebseinnahmen | Gross business revenue (including collected USt per § 4 Abs. 3 EStG) |
| Raumkosten | Office costs (rent, utilities, home office) |
| Fahrzeugkosten | Vehicle costs (business portion) |
| Reisekosten | Travel expenses |
| Bewirtungskosten | Business entertainment (70% deductible) |
| Werbekosten | Marketing/advertising |
| AfA (Abschreibungen) | Depreciation |
| Nebenkosten Geldverkehr | Bank fees, payment processing |
| Gewinn/Verlust | Net profit/loss |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown filing status | Single (Einzelveranlagung) |
| Unknown church membership | No Kirchensteuer (0%) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown whether Freiberufler or Gewerbetreibende | Freiberufler (no Gewerbesteuer) until confirmed |
| Unknown expense category | Not deductible |
| Unknown depreciation useful life | Use official AfA-Tabelle |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of filing status (single/married/joint) and whether Freiberufler or Gewerbetreibende.

**Recommended** -- all Ausgangsrechnungen (outgoing invoices), Eingangsrechnungen (purchase invoices), Steuer-Identifikationsnummer, prior year Steuerbescheid (tax assessment).

**Ideal** -- complete Einnahmen-Uberschuss-Rechnung (EUR) from prior year, asset register (Anlageverzeichnis), Vorauszahlungsbescheid, all SSC (Sozialversicherung) contribution statements.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning.

### Refusal Catalogue

**R-DE-1 -- Corporations (GmbH, UG, AG).** "This skill covers Einkommensteuer for natural persons only. Kapitalgesellschaften file Korperschaftsteuer. Out of scope."

**R-DE-2 -- Partnerships (GbR, OHG, KG).** "Partnership income is determined at partnership level (gesonderte und einheitliche Feststellung) and allocated to partners. Out of scope."

**R-DE-3 -- Non-resident limited taxpayer (beschrankt steuerpflichtig).** "Non-resident taxation has different rules and rate tables. Out of scope."

**R-DE-4 -- Complex capital gains (Verausserungsgewinne).** "Business disposals, real estate gains, and share disposals beyond the Sparerpauschbetrag require specialised computation. Escalate."

**R-DE-5 -- Double taxation / foreign income.** "Cross-border income requires Doppelbesteuerungsabkommen (DBA) analysis. Escalate."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| KUNDENUEBERWEISUNG, KUNDENUBERWEISUNG, UBERWEISUNG [client name] | Betriebseinnahmen | Gross revenue on Anlage EUR | Collected USt must be included in Betriebseinnahmen for EÜR, but reported in a separate line on the form |
| HONORAR, HONORARNOTE, VERGUETUNG | Betriebseinnahmen | Revenue | Professional fees -- typical Freiberufler |
| PAYPAL PAYOUT, STRIPE PAYOUT, STRIPE TRANSFER | Betriebseinnahmen | Revenue | Platform payout -- match to underlying invoices |
| GEHALT, LOHN, ARBEITGEBER [name] | Einkuenfte aus nichtselbstaendiger Arbeit (Anlage N) | NOT self-employment income | Employment income -- separate Anlage N |
| MIETEINNAHME, MIETE ERHALTEN | Einkuenfte aus Vermietung (Anlage V) | NOT self-employment income | Rental income -- separate |
| ZINSEN, ZINSERTRAG, KAPITALERTRAG | Einkuenfte aus Kapitalvermogen (Anlage KAP) | NOT self-employment income | Capital income -- Abgeltungsteuer 25% |
| DIVIDENDE | Einkuenfte aus Kapitalvermogen | NOT self-employment income | Dividend |
| ERSTATTUNG FINANZAMT, STEUERERSTATTUNG | Identify the tax before classifying | VAT refund: EÜR receipt (2025 line 18); income tax or non-deductible trade tax refund: excluded | If the tax type is unknown, flag for reviewer classification. |
| GUTSCHRIFT [supplier name] | Check context | Could be credit note or refund | If refund of expense: reduce expense. If revenue: add to income |

### 3.2 Expense Patterns (Debits on Bank Statement)

| Pattern | Tax Line (Anlage EUR) | Treatment | Notes |
|---|---|---|---|
| MIETE BUERO, BUEROMIETE, OFFICE RENT | Raumkosten | Fully deductible | Dedicated business premises |
| ARBEITSZIMMER, HOME OFFICE | Raumkosten -- hausliches Arbeitszimmer | T2 -- see Section 6 | Max EUR 1,260/year Tagespauschale or actual |
| FAHRTKOSTEN, TANKSTELLE, ARAL, SHELL, TOTAL | Fahrzeugkosten | T2 -- business portion only | Fahrtenbuch or 1%-Regelung required |
| BAHNCARD, DEUTSCHE BAHN, DB FERNVERKEHR | Reisekosten | Fully deductible | Business travel |
| FLUG, LUFTHANSA, RYANAIR, EASYJET | Reisekosten | Fully deductible | Business purpose flights |
| BEWIRTUNG, RESTAURANT, GASTSTATTE | Bewirtungskosten | 70% deductible (ESt) | MUST have Bewirtungsbeleg |
| FACHLITERATUR, BUCH, AMAZON (books) | Betriebsausgaben | Fully deductible | Professional literature |
| FORTBILDUNG, SEMINAR, KURS, TRAINING | Fortbildungskosten | Fully deductible | Related to business activity |
| TELEFON, TELEKOM, VODAFONE, O2 | Telekommunikation | T2 -- business portion only | Default 0% if mixed use |
| INTERNET, DSL | Telekommunikation | T2 -- business portion only | |
| VERSICHERUNG, BERUFSHAFTPFLICHT | Versicherungen | Fully deductible | Professional liability only; personal = not deductible |
| STEUERBERATER, STEUERKANZLEI, BUCHHALTER | Beratungskosten | Fully deductible | |
| RECHTSANWALT, ANWALT, KANZLEI | Rechtskosten | Fully deductible | Business-related legal only |
| IHK, HANDWERKSKAMMER, BEITRAG | Beitrage | Fully deductible | Compulsory chamber fees |
| BUROMATERIAL, STAPLES, VIKING | Burobedarf | Fully deductible | |
| SOFTWARE, LIZENZ, SUBSCRIPTION | Betriebsausgaben (IT) | Fully deductible if under EUR 800 net | Over EUR 800: capitalise and depreciate |
| WERBUNG, MARKETING, GOOGLE ADS, META ADS | Werbekosten | Fully deductible | |
| KONTOFUHRUNGSGEBUHR, BANKGEBUHR | Nebenkosten Geldverkehr | Fully deductible | Business account |
| PAYPAL FEE, STRIPE FEE | Nebenkosten Geldverkehr | Fully deductible | Transaction fees |

### 3.3 Expense Patterns -- NOT Deductible as Betriebsausgaben

| Pattern | Correct Treatment | Notes |
|---|---|---|
| KRANKENKASSE, AOK, TK, BARMER, DAK | Sonderausgabe (Anlage Vorsorgeaufwand) | NOT a business expense |
| RENTENVERSICHERUNG, DRV | Sonderausgabe (Altersvorsorge) | NOT a business expense |
| KUENSTLERSOZIALKASSE, KSK | Sonderausgabe | NOT a business expense |
| FINANZAMT, EINKOMMENSTEUER, VORAUSZAHLUNG ESt | EXCLUDE | Income tax not deductible |
| GEWERBESTEUER, GewSt | Keine Betriebsausgabe | Not deductible (§ 4 Abs. 5b EStG). Subject to separate tax reduction under § 35 EStG. |
| PRIVATENTNAHME, EIGENBELEG PRIVAT | EXCLUDE | Drawings |
| UMSATZSTEUER ZAHLUNG, USt VORAUSZAHLUNG | Betriebsausgabe in EÜR | VAT paid to the Finanzamt is recorded separately; apply the cash-basis timing rules, including the ten-day rule where applicable. |
| SPENDE, DONATION | Sonderausgabe | NOT a business expense |

### 3.4 SaaS -- EU Suppliers (Reverse Charge for USt; fully deductible for ESt)

| Pattern | ESt Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META, SLACK, ZOOM | Betriebsausgaben (IT) | Net amount deductible. Reverse charge USt separate. |
| ATLASSIAN, DROPBOX, SPOTIFY (business) | Betriebsausgaben (IT) | Same |
| STRIPE (subscription fee) | Betriebsausgaben | Separate from transaction fees |

### 3.5 SaaS -- Non-EU Suppliers

| Pattern | ESt Treatment | Notes |
|---|---|---|
| NOTION, ANTHROPIC, OPENAI, GITHUB, FIGMA, CANVA | Betriebsausgaben (IT) | Net amount deductible. Non-EU reverse charge for USt. |
| AWS (check billing entity) | Betriebsausgaben (IT) | AWS EMEA SARL (LU) = EU; AWS Inc (US) = non-EU |

### 3.6 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| UMBUCHUNG, EIGENUEBERWEISUNG, INTERNAL TRANSFER | EXCLUDE | Internal movement between own accounts |
| DARLEHEN, KREDIT, TILGUNG | EXCLUDE | Loan principal -- not income or expense |
| ZINSEN DARLEHEN (paid) | Betriebsausgaben (Schuldzinsen) | Interest on business loan: deductible |
| BARGELDABHEBUNG, GELDAUTOMAT, ATM | T2 -- ask | Default exclude; ask what cash was spent on |

### 3.7 German Banks -- Statement Format Reference

| Bank | Format | Key Fields |
|---|---|---|
| Sparkasse, Volksbank | CSV, PDF | Buchungstag, Wertstellung, Verwendungszweck, Betrag |
| Deutsche Bank, Commerzbank | CSV, MT940 | Valuta, Buchungstext, Auftraggeber/Empfanger, Betrag |
| N26, Revolut | CSV | Date, Counterparty, Amount, Reference |
| ING DiBa | CSV | Buchung, Auftraggeber/Empfanger, Verwendungszweck, Betrag |

---

## Section 4 -- Worked Examples

### Example 1 -- Freiberufler, Standard Income

**Input line:**
`15.03.2025 ; KUNDENUEBERWEISUNG STUDIO KREBS GMBH ; CREDIT ; Honorar Maerz 2025 ; +4,500.00 ; EUR`

**Reasoning:**
Client payment for professional services. Freiberufler income. If USt-registered (Regelbesteuerung), EUR 4,500 may include 19% USt. Both the net revenue (EUR 3,781.51) and the collected USt (EUR 718.49) are Betriebseinnahmen under § 4 Abs. 3 EStG, but are reported on separate lines in the Anlage EÜR. If Kleinunternehmer (s19 UStG), full EUR 4,500 is income.

**Classification:** Betriebseinnahmen on Anlage EUR / Anlage S.

### Example 2 -- Bewirtung (Business Entertainment)

**Input line:**
`22.04.2025 ; RESTAURANT GOLDENER HIRSCH ; DEBIT ; Bewirtung Kundentreffen ; -180.00 ; EUR`

**Reasoning:**
For this example, the EUR 180 bill includes 19% USt, is reasonable and fully business-related, and meets the invoice and entertainment-record requirements. Deduct 70% of the net entertainment cost for ESt (§ 4(5) no. 2 EStG); record the deductible input VAT separately. [ELSTER, 2025 EÜR instructions, lines 57 and 63](https://www.elster.de/elsterweb/helpGlobal?themaGlobal=help_euer_ufa_77_2025). Without the required supporting records, flag the deduction for review rather than claiming it.

**Classification:** Net cost EUR 151.26; ESt entertainment deduction EUR 105.88 (70%), with EUR 45.38 not deductible. Deductible input VAT EUR 28.74 is a separate EÜR expense, not part of the 70% base. If VAT is not recoverable, use the EUR 180 gross cost instead: EUR 126 deductible entertainment expense, EUR 54 not deductible and no separate input-VAT deduction.

### Example 3 -- Home Office (Arbeitszimmer)

**Input line:**
`01.01.2025 ; VERMIETER MUELLER ; DEBIT ; Miete inkl. Nebenkosten ; -850.00 ; EUR`

**Reasoning:**
Monthly rent. Home office deduction depends on arrangement:
- **Tagespauschale:** EUR 6/day, max 210 days = EUR 1,260/year. Available regardless of room arrangement.
- **Dedicated room (Mittelpunkt):** If separate room, exclusively for work, AND centre of all professional activity, full actual costs deductible (proportional by floor area).
- **No dedicated room:** Tagespauschale only.

**Classification:** T2 -- ask client about room arrangement. Default: Tagespauschale EUR 1,260/year.

### Example 4 -- Vehicle Fuel

**Input line:**
`10.05.2025 ; ARAL TANKSTELLE BERLIN ; DEBIT ; Diesel ; -85.00 ; EUR`

**Reasoning:**
Fuel purchase. Vehicle expenses require either Fahrtenbuch (logbook), 1%-Regelung, or Kilometerpauschale. Without confirmed method: 0% deduction.

**Classification:** T2 -- ask which method. Default: 0% deduction until confirmed.

### Example 5 -- Software Subscription Under EUR 800

**Input line:**
`03.06.2025 ; ADOBE SYSTEMS ; DEBIT ; Creative Cloud Jahresabo ; -713.88 ; EUR`

**Reasoning:**
Annual subscription under EUR 800 net. Subscription (not perpetual licence) = Betriebsausgabe in full in year paid, regardless of EUR 800 threshold.

**Classification:** Betriebsausgaben (IT/Software). Fully deductible.

### Example 6 -- Health Insurance (NOT Business Expense)

**Input line:**
`15.01.2025 ; TECHNIKER KRANKENKASSE ; DEBIT ; Krankenversicherung Jan 2025 ; -450.00 ; EUR`

**Reasoning:**
Health insurance is a Sonderausgabe on the main return, NOT a Betriebsausgabe on Anlage EUR.

**Classification:** EXCLUDE from Anlage EUR. Record as Sonderausgabe (Anlage Vorsorgeaufwand).

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Betriebseinnahmen (Business Revenue)

**Legislation:** EStG s4 Abs.1, s15 (Gewerbebetrieb), s18 (freiberufliche Tatigkeit)

All business income is Betriebseinnahmen. For cash-basis EÜR under [§ 4(3) EStG](https://www.gesetze-im-internet.de/estg/__4.html), report net taxable receipts and VAT actually received separately. On the **2025** Anlage EÜR, these are lines 15 and 17; VAT refunded or set off by the Finanzamt goes to line 18. For Kleinunternehmer (§ 19 UStG), report gross receipts without separating USt. Use the form for the selected year, not a later year's line numbers. [ELSTER, 2025 EÜR instructions](https://www.elster.de/elsterweb/helpGlobal?themaGlobal=help_euer_ufa_77_2025).

### 5.2 Betriebsausgaben (Business Expenses)

**Legislation:** EStG s4 Abs.4

Expenses are deductible if caused by the business (betrieblich veranlasst). Germany allows apportionment of mixed-use expenses where business and private portions can be objectively separated.

For EÜR, deductible input VAT actually paid is a separate business expense (2025 line 57), as is VAT paid to the Finanzamt (2025 line 58). Enter the underlying expense net when its VAT is deductible, so the VAT is counted once. Non-recoverable VAT forms part of that item's cost and follows its deduction or depreciation rules. Apply [§ 11 EStG](https://www.gesetze-im-internet.de/estg/__11.html), including the ten-day rule for qualifying recurring payments. [ELSTER, 2025 EÜR instructions](https://www.elster.de/elsterweb/helpGlobal?themaGlobal=help_euer_ufa_77_2025).

### 5.3 Geringwertige Wirtschaftsguter (GWG / Low-Value Assets)

| Net Cost (excl. USt) | Treatment |
|---|---|
| Up to EUR 250 | Immediate full deduction, no asset register |
| EUR 250.01 -- EUR 800 | Immediate full deduction OR Sammelposten. Asset register required. |
| EUR 800.01 -- EUR 1,000 | Sammelposten option: pool, depreciate 5 years (20%/year) |
| Over EUR 1,000 | Normal AfA over useful life per AfA-Tabelle |

For the threshold test, subtract the VAT included in the acquisition cost even if the taxpayer cannot recover it. Non-recoverable VAT remains part of the amount deducted. A separately usable, qualifying office chair costing EUR 800 plus EUR 152 VAT can therefore meet the EUR 800 threshold and give a Kleinunternehmer a EUR 952 immediate deduction. This is not an EUR 800 gross ceiling. [§ 6(2) EStG](https://www.gesetze-im-internet.de/estg/__6.html).

### 5.4 AfA (Depreciation)

**Legislation:** EStG s7

| Asset Type | Useful Life | Annual Rate |
|---|---|---|
| Computer hardware (incl. peripherals) | 1 year (since 2021 BMF ruling) | 100% |
| Computer software | 1 year | 100% |
| Office furniture | 13 years | ~7.7% |
| Motor vehicles | 6 years | ~16.7% |
| Office equipment (printers, copiers) | 7 years | ~14.3% |
| Mobile phones | 5 years | 20% |
| Buildings (commercial) | 33 or 50 years | 3% or 2% |

**Computer hardware and software:** Since BMF ruling of 26.02.2021, digital assets can be written off in full in the year of acquisition regardless of cost.

### 5.5 Non-Deductible Expenses

| Expense | Reason |
|---|---|
| Einkommensteuer, SolZ, KiSt | Tax on income -- s12 Nr.3 EStG |
| Private living expenses | s12 Nr.1 EStG |
| Fines and penalties (Geldstrafen, Busgelder) | s4 Abs.5 Nr.8 EStG |
| Gifts to business partners over EUR 50/person/year | s4 Abs.5 Nr.1 EStG |
| 30% of Bewirtungskosten | s4 Abs.5 Nr.2 EStG |
| Personal insurance (life, household) | Sonderausgabe, not Betriebsausgabe |

### 5.6 Vorauszahlungen (Quarterly Prepayments)

**Legislation:** EStG s37

| Instalment | Deadline |
|---|---|
| Q1 | 10 March |
| Q2 | 10 June |
| Q3 | 10 September |
| Q4 | 10 December |

Based on most recent Steuerbescheid. First year: Finanzamt estimates.

### 5.7 Filing Deadlines

| Scenario | Deadline |
|---|---|
| Self-filed (without Steuerberater) | 31 July of following year |
| Filed by Steuerberater | End of February, year after next |
| USt Voranmeldungen | 10th of following month/quarter |

### 5.8 Penalties

| Offence | Penalty |
|---|---|
| Late filing (Verspatungszuschlag) | 0.25% of assessed tax per month, min EUR 25/month |
| Late payment (Saumiszuschlag) | 1% per commenced month on unpaid tax |
| Interest on late assessment | 0.15% per month (from 15 months after year end) |
| Incorrect return | Up to EUR 25,000; criminal penalties for fraud |

### 5.9 Interaction with Umsatzsteuer (USt)

| Scenario | Income Tax Treatment |
|---|---|
| USt actually collected (Regelbesteuerung) | Separate business receipt; 2025 EÜR line 17, in addition to net taxable receipts in line 15 |
| Deductible Vorsteuer actually paid | Separate business expense; 2025 EÜR line 57, with the underlying expense entered net |
| USt paid to the Finanzamt | Separate business expense; 2025 EÜR line 58, subject to cash-basis timing rules |
| USt refunded or set off by the Finanzamt | Separate business receipt; 2025 EÜR line 18 |
| Vorsteuer blocked | Part of the item's cost; follow that item's deduction or depreciation rules. The ESt entertainment limit does not itself block the same proportion of input VAT. |
| Kleinunternehmer (s19 UStG) | No USt charged; all costs gross including USt paid |
| Reverse-charge on imports | Net effect zero for USt; net cost deductible for ESt |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office (Hausliches Arbeitszimmer)

| Scenario | Deduction | Condition |
|---|---|---|
| No dedicated room | Tagespauschale: EUR 6/day, max EUR 1,260/year | Available to all who work from home |
| Dedicated room, not Mittelpunkt | Tagespauschale only (since 2023 reform) | Room exists but works elsewhere too |
| Dedicated room, Mittelpunkt der Tatigkeit | Full actual costs (pro-rata by floor area) | Centre of ALL professional activity |

**Flag for reviewer:** Confirm room arrangement, floor area ratio, Mittelpunkt status.

### 6.2 Vehicle Business Use

| Method | How It Works |
|---|---|
| Fahrtenbuch | Actual costs x (business km / total km). Must be contemporaneous, complete, unchangeable. |
| 1%-Regelung | Private use = 1% x Bruttolistenpreis/month added as income. All costs deductible. |
| Kilometerpauschale | EUR 0.30/km for business trips. No actual cost records needed. No Vorsteuer. |

**Flag for reviewer:** Confirm method and business-use percentage.

### 6.3 Phone / Internet Mixed Use

Default: 0% deduction. Options:
- **Flat rate:** 20% of phone/internet costs, capped EUR 20/month, without records
- **Actual records:** Higher % with 3-month representative usage log

### 6.4 Geschenke (Business Gifts)

- Deductible up to EUR 50 net per person per year (since 2024)
- Must record individually with recipient name
- Over EUR 50: entire amount non-deductible (not just excess)

---

## Section 7 -- Excel Working Paper Template

For a VAT-registered taxpayer, enter underlying costs net of separately deductible input VAT. Include non-recoverable VAT in the relevant cost and apply that cost's deduction or depreciation rules. Kleinunternehmer use gross receipts and costs without separate VAT rows. Apply the § 11 timing rules before assigning VAT payments or refunds to this year. The row labels below are working-paper labels, not official form line numbers.

```
EINNAHMEN-UBERSCHUSS-RECHNUNG (EUR) -- Working Paper
Tax Year: 2025
Client: ___________________________
Status: Freiberufler / Gewerbetreibende

A. BETRIEBSEINNAHMEN
  A1. Umsatzerlose (net of USt if registered)    ___________
  A2. Sonstige Betriebseinnahmen                  ___________
  A3. Vereinnahmte USt (2025 EÜR line 17)         ___________
  A4. USt-Erstattungen Finanzamt (line 18)        ___________
  A5. Total Betriebseinnahmen (A1 + A2 + A3 + A4) ___________

B. BETRIEBSAUSGABEN
  B1. Wareneinsatz / Fremdleistungen              ___________
  B2. Raumkosten (Miete, Nebenkosten)             ___________
  B3. Arbeitszimmer (Pauschale or actual)         ___________
  B4. Versicherungen (business only)              ___________
  B5. Fahrzeugkosten                              ___________
  B6. Reisekosten                                 ___________
  B7. Bewirtungskosten (70% of eligible cost)     ___________
  B8. Werbekosten                                 ___________
  B9. Buro- und Verwaltungskosten                 ___________
  B10. Telekommunikation (business %)             ___________
  B11. Fortbildungskosten                         ___________
  B12. Beratungskosten (StB, RA)                  ___________
  B13. Abschreibungen (AfA)                       ___________
  B14. Nebenkosten Geldverkehr (bank fees)        ___________
  B15. Sonstige Betriebsausgaben                  ___________
  B16. Abziehbare Vorsteuer paid (line 57)        ___________
  B17. USt paid to Finanzamt (line 58)            ___________
  B18. Total Betriebsausgaben (sum B1 through B17) ___________

C. GEWINN / VERLUST (A5 - B18)                    ___________

REVIEWER FLAGS:
  [ ] Freiberufler or Gewerbetreibende confirmed?
  [ ] Filing status confirmed (single/married)?
  [ ] Church membership confirmed?
  [ ] Home office method confirmed?
  [ ] Vehicle method confirmed?
  [ ] Bewirtungsbelege available?
  [ ] B7 uses net cost if VAT is separately deductible?
  [ ] VAT receipts, refunds and payments reconciled without duplication?
  [ ] Year-end VAT timing checked under section 11 EStG?
  [ ] All T2 items flagged for review?
```

---

## Section 8 -- Bank Statement Reading Guide

### German Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| Sparkasse, Volksbank | CSV, PDF | Buchungstag, Wertstellung, Verwendungszweck, Betrag |
| Deutsche Bank, Commerzbank | CSV, MT940 | Valuta, Buchungstext, Auftraggeber/Empfanger, Betrag |
| N26, Revolut | CSV | Date, Counterparty, Amount, Reference |
| ING DiBa | CSV | Buchung, Auftraggeber/Empfanger, Verwendungszweck, Betrag |

### Key German Banking Terms

| German Term | English | Classification Hint |
|---|---|---|
| Gutschrift | Credit (incoming) | Potential income |
| Lastschrift | Direct debit (outgoing) | Potential expense |
| Uberweisung | Bank transfer | Check direction |
| Dauerauftrag | Standing order | Regular expense |
| Kartenzahlung | Card payment | Expense |
| Bargeldabhebung | Cash withdrawal | Ask what it was for |
| Abschluss | Bank charges | Nebenkosten Geldverkehr |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all T2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- GERMANY INCOME TAX
1. Are you Freiberufler or Gewerbetreibende?
2. Filing status: Einzelveranlagung (single) or Zusammenveranlagung (joint)?
3. Church member (evangelisch, katholisch, other, or none)?
4. Home office: dedicated room or shared space?
5. Vehicle: Fahrtenbuch, 1%-Regelung, or Kilometerpauschale?
6. Phone/internet: what percentage is business use?
7. Do you have a Steuerberater filing on your behalf?
8. Prior year Steuerbescheid available?
```

---

## Section 10 -- Reference Material

### Key Legislation References

| Topic | Section |
|---|---|
| Business income (Gewerbebetrieb) | EStG s15 |
| Freiberufliche Tatigkeit | EStG s18 |
| Business expenses | EStG s4 Abs.4 |
| Non-deductible expenses | EStG s4 Abs.5, s12 |
| AfA depreciation | EStG s7 |
| GWG low-value assets | EStG s6 Abs.2 |
| Bewirtungskosten | EStG s4 Abs.5 Nr.2 |
| Geschenke (gifts) | EStG s4 Abs.5 Nr.1 |
| Arbeitszimmer | EStG s4 Abs.5 Nr.6b / Nr.6c (Tagespauschale) |
| Vorauszahlungen | EStG s37 |
| Solidaritatszuschlag | SolZG |
| Kirchensteuer | KiStG (Lander) |
| Gewerbesteuer credit | EStG s35 |

### Test Suite

**Test 1 -- Freiberufler, mid-range income.**
Input: Single, no church, Freiberufler, Betriebseinnahmen EUR 60,000, Betriebsausgaben EUR 15,000. Gewinn EUR 45,000.
Expected: Apply formula-based progressive rate to EUR 45,000. SolZ likely below exemption threshold. No GewSt.

**Test 2 -- Bewirtung correctly limited.**
Input: EUR 500 net Bewirtungskosten plus EUR 95 recoverable VAT, with all business-purpose and documentation requirements met.
Expected: EUR 350 entertainment deduction (70% of net); EUR 150 not deductible; EUR 95 input VAT separately deductible. For a taxpayer who cannot recover VAT, the same EUR 595 gross bill gives EUR 416.50 entertainment deduction and EUR 178.50 not deductible, with no separate input-VAT deduction.

**Test 3 -- Computer hardware full write-off.**
Input: Laptop EUR 2,500 purchased.
Expected: Full deduction in year of acquisition (BMF 2021 ruling). 100% AfA.

**Test 4 -- Health insurance excluded.**
Input: TK Krankenversicherung EUR 5,400.
Expected: EXCLUDE from Anlage EUR. Sonderausgabe on Anlage Vorsorgeaufwand.

**Test 5 -- Geschenke over limit.**
Input: EUR 80 gift to business partner.
Expected: Over EUR 50 limit. Entire EUR 80 non-deductible.

**Test 6 -- Kleinunternehmer gross reporting.**
Input: Kleinunternehmer, invoice EUR 1,000 (no USt charged).
Expected: Full EUR 1,000 is Betriebseinnahme. All purchase costs at gross.

**Test 7 -- VAT reconciles in cash-basis EÜR.**
Input: In the same year, EUR 10,000 net fees plus EUR 1,900 VAT received; EUR 2,000 deductible net expenses plus EUR 380 deductible input VAT paid; EUR 1,520 VAT paid to the Finanzamt. No year-end timing adjustment or other items.
Expected: Section 7 A1 EUR 10,000, A3 EUR 1,900 and A5 EUR 11,900; underlying B1-B15 costs EUR 2,000, B16 EUR 380, B17 EUR 1,520 and B18 EUR 3,900; C profit EUR 8,000. Excluding either input VAT or the remittance would overstate profit. For payments near year end, test § 11 EStG before assigning the year.

**Test 8 -- GWG threshold differs from deduction amount.**
Input: A Kleinunternehmer buys a separately usable office chair for EUR 800 plus EUR 152 VAT and elects immediate deduction under § 6(2) EStG; all other conditions are met.
Expected: Threshold-test cost EUR 800; immediate deduction EUR 952 because the VAT cannot be recovered. A price of EUR 800.01 before included VAT exceeds the immediate-deduction threshold.

**Test 9 -- Tax refund classification follows the tax type.**
Input: A bank credit labelled STEUERERSTATTUNG for EUR 500.
Expected: If the notice identifies VAT, enter a separate EÜR receipt (2025 line 18), subject to the timing rules. If it identifies income tax, exclude it from business receipts. Without the notice or another reliable tax-type match, flag the amount for review rather than excluding it automatically.

**Test 10 -- VAT refund has no offsetting current-year payment.**
Input: EUR 10,000 net fees and EUR 1,900 VAT collected; EUR 2,000 net expenses and EUR 380 deductible input VAT paid; EUR 500 VAT refund received from a prior period; no VAT remittance or timing adjustment in the year.
Expected: Section 7 A1 EUR 10,000, A3 EUR 1,900, A4 EUR 500 and A5 EUR 12,400; B1-B15 EUR 2,000, B16 EUR 380, B17 zero and B18 EUR 2,380; C profit EUR 10,020. Omitting VAT rows would incorrectly produce EUR 8,000.

**Test 11 -- Restaurant bill uses net cost once.**
Input: Example 2's eligible EUR 180 gross restaurant bill, including EUR 28.74 recoverable VAT, paid in the year.
Expected: B7 EUR 105.88, B16 EUR 28.74, total deductible expenses EUR 134.62 and non-deductible net entertainment cost EUR 45.38. If VAT cannot be recovered, B7 EUR 126, B16 zero and non-deductible cost EUR 54. Do not combine the gross entertainment deduction with a separate VAT deduction.

---

## PROHIBITIONS

- NEVER compute Einkommensteuer using simple bracket multiplication -- use formula-based progressive rate
- NEVER include Krankenversicherung or Rentenversicherung as Betriebsausgaben -- they are Sonderausgaben
- NEVER allow more than 70% of Bewirtungskosten as Betriebsausgabe
- NEVER allow Geschenke over EUR 50 per person per year
- NEVER allow Einkommensteuer, SolZ, or KiSt as deductible expenses
- NEVER allow fines or penalties as deductible
- NEVER apply Gewerbesteuer to a Freiberufler
- NEVER deduct vehicle expenses without confirming the method
- NEVER deduct home office beyond EUR 1,260 Tagespauschale without confirming Mittelpunkt
- NEVER present tax calculations as definitive -- direct client to Steuerberater

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
