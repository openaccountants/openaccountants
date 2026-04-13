---
name: de-income-tax
description: >
  Use this skill whenever asked about German income tax (Einkommensteuer) for self-employed individuals (Freiberufler or Gewerbetreibende). Trigger on phrases like "how much tax do I pay in Germany", "Einkommensteuer", "Einkommensteuererklarung", "Anlage S", "Anlage G", "Anlage EUR", "Freiberufler tax", "Gewerbetreibende", "Solidaritatszuschlag", "Kirchensteuer", "Vorauszahlungen", "Betriebsausgaben", "AfA", "Abschreibung", "hausliches Arbeitszimmer", "Fahrtkosten", "Bewirtungskosten", "Grundfreibetrag", or any question about filing or computing income tax for a self-employed client in Germany. Covers Einkommensteuer progressive rates, Solidaritatszuschlag, Kirchensteuer, Anlage S/G/EUR structure, allowable Betriebsausgaben, AfA depreciation, home office, vehicle expenses, quarterly Vorauszahlungen, Gewerbesteuer credit, and interaction with Umsatzsteuer. ALWAYS read this skill before touching any German income tax work.
version: 2.0
jurisdiction: DE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Germany Income Tax (Einkommensteuer) -- Self-Employed Skill v2.0

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
| Skill version | 2.0 |

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
| Betriebseinnahmen | Gross business revenue (net of USt if registered) |
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
| KUNDENUEBERWEISUNG, KUNDENUBERWEISUNG, UBERWEISUNG [client name] | Betriebseinnahmen | Gross revenue on Anlage EUR | If USt-registered, extract net (excl. 19% USt) |
| HONORAR, HONORARNOTE, VERGUETUNG | Betriebseinnahmen | Revenue | Professional fees -- typical Freiberufler |
| PAYPAL PAYOUT, STRIPE PAYOUT, STRIPE TRANSFER | Betriebseinnahmen | Revenue | Platform payout -- match to underlying invoices |
| GEHALT, LOHN, ARBEITGEBER [name] | Einkuenfte aus nichtselbstaendiger Arbeit (Anlage N) | NOT self-employment income | Employment income -- separate Anlage N |
| MIETEINNAHME, MIETE ERHALTEN | Einkuenfte aus Vermietung (Anlage V) | NOT self-employment income | Rental income -- separate |
| ZINSEN, ZINSERTRAG, KAPITALERTRAG | Einkuenfte aus Kapitalvermogen (Anlage KAP) | NOT self-employment income | Capital income -- Abgeltungsteuer 25% |
| DIVIDENDE | Einkuenfte aus Kapitalvermogen | NOT self-employment income | Dividend |
| ERSTATTUNG FINANZAMT, STEUERERSTATTUNG | EXCLUDE | Not income | Tax refund |
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
| GEWERBESTEUER, GewSt | Betriebsausgabe | Deductible since 2008 (for Gewerbetreibende) |
| PRIVATENTNAHME, EIGENBELEG PRIVAT | EXCLUDE | Drawings |
| UMSATZSTEUER ZAHLUNG, USt VORAUSZAHLUNG | EXCLUDE from P&L | USt is balance sheet for Regelbesteuerung |
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
Client payment for professional services. Freiberufler income. If USt-registered (Regelbesteuerung), EUR 4,500 may include 19% USt. Check invoice: if EUR 4,500 gross, net = EUR 3,781.51 (Betriebseinnahme) + EUR 718.49 (USt liability). If Kleinunternehmer (s19 UStG), full EUR 4,500 is income.

**Classification:** Betriebseinnahmen on Anlage EUR / Anlage S.

### Example 2 -- Bewirtung (Business Entertainment)

**Input line:**
`22.04.2025 ; RESTAURANT GOLDENER HIRSCH ; DEBIT ; Bewirtung Kundentreffen ; -180.00 ; EUR`

**Reasoning:**
Bewirtungskosten are 70% deductible for ESt (s4 Abs.5 Nr.2 EStG). The full Vorsteuer (19% USt) is recoverable for USt purposes if a proper Bewirtungsbeleg exists. Without Bewirtungsbeleg: 0% deductible.

**Classification:** ESt: EUR 180.00 x 70% = EUR 126.00 deductible. EUR 54.00 not deductible. USt: EUR 28.74 Vorsteuer 100% recoverable with proper Beleg.

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

All business income is Betriebseinnahmen. For USt-registered, report net of USt on Anlage EUR. For Kleinunternehmer (s19 UStG), report gross.

### 5.2 Betriebsausgaben (Business Expenses)

**Legislation:** EStG s4 Abs.4

Expenses are deductible if caused by the business (betrieblich veranlasst). Germany allows apportionment of mixed-use expenses where business and private portions can be objectively separated.

### 5.3 Geringwertige Wirtschaftsguter (GWG / Low-Value Assets)

| Net Cost (excl. USt) | Treatment |
|---|---|
| Up to EUR 250 | Immediate full deduction, no asset register |
| EUR 250.01 -- EUR 800 | Immediate full deduction OR Sammelposten. Asset register required. |
| EUR 800.01 -- EUR 1,000 | Sammelposten option: pool, depreciate 5 years (20%/year) |
| Over EUR 1,000 | Normal AfA over useful life per AfA-Tabelle |

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
| USt collected (Regelbesteuerung) | NOT income -- report net on Anlage EUR |
| Vorsteuer recovered | NOT an expense -- report net on Anlage EUR |
| Vorsteuer blocked (e.g., 30% Bewirtung for ESt, 100% for USt) | ESt and USt have DIFFERENT rules |
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

```
EINNAHMEN-UBERSCHUSS-RECHNUNG (EUR) -- Working Paper
Tax Year: 2025
Client: ___________________________
Status: Freiberufler / Gewerbetreibende

A. BETRIEBSEINNAHMEN
  A1. Umsatzerlose (net of USt if registered)    ___________
  A2. Sonstige Betriebseinnahmen                  ___________
  A3. Total Betriebseinnahmen (A1 + A2)           ___________

B. BETRIEBSAUSGABEN
  B1. Wareneinsatz / Fremdleistungen              ___________
  B2. Raumkosten (Miete, Nebenkosten)             ___________
  B3. Arbeitszimmer (Pauschale or actual)         ___________
  B4. Versicherungen (business only)              ___________
  B5. Fahrzeugkosten                              ___________
  B6. Reisekosten                                 ___________
  B7. Bewirtungskosten (70% of gross)             ___________
  B8. Werbekosten                                 ___________
  B9. Buro- und Verwaltungskosten                 ___________
  B10. Telekommunikation (business %)             ___________
  B11. Fortbildungskosten                         ___________
  B12. Beratungskosten (StB, RA)                  ___________
  B13. Abschreibungen (AfA)                       ___________
  B14. Nebenkosten Geldverkehr (bank fees)        ___________
  B15. Sonstige Betriebsausgaben                  ___________
  B16. Total Betriebsausgaben (B1-B15)            ___________

C. GEWINN / VERLUST (A3 - B16)                    ___________

REVIEWER FLAGS:
  [ ] Freiberufler or Gewerbetreibende confirmed?
  [ ] Filing status confirmed (single/married)?
  [ ] Church membership confirmed?
  [ ] Home office method confirmed?
  [ ] Vehicle method confirmed?
  [ ] Bewirtungsbelege available?
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
Input: EUR 500 Bewirtungskosten claimed.
Expected: EUR 350 deductible (70%). EUR 150 not deductible.

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

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
