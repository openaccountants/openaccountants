---
name: at-income-tax
description: Use this skill whenever asked about Austrian income tax (Einkommensteuer) for self-employed individuals filing form E1. Trigger on phrases like "Einkommensteuer", "ESt", "E1 Erklarung", "Gewinnfreibetrag", "Betriebsausgabenpauschale", "Absetzbetrge", "Sonderausgaben", "selbstandig Steuer Osterreich", "Austrian income tax", "self-employed tax Austria", or any question about computing or filing income tax for a self-employed person in Austria. This skill covers progressive tax brackets (0--55%), Gewinnfreibetrag, Betriebsausgabenpauschale, Sonderausgaben, aussergewohnliche Belastungen, Absetzbetrge, SV deductibility, and E1/E1a structure. ALWAYS read this skill before touching any Austrian income tax work.
version: 2.0
jurisdiction: AT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austrian income tax for the self-employed (Einkommensteuer, form E 1)

How Austria taxes the profit of one self-employed person: the tariff, the profit allowance (Gewinnfreibetrag), the flat expense rate (Basispauschalierung), special expenses, tax credits (Absetzbeträge), the E 1 return, deadlines and prepayments. Figures are for tax year 2026; the calendar year, assessed in 2027. Most figures come from the ministry's USP business portal, pages dated 1 January 2026. Steuerbuch 2026 covers the 2025 assessment (labelled); the flat-rate turnover limit is from a USP news item of 28 August 2025.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Austria (Republik Österreich) |
| Tax | Einkommensteuer (ESt) |
| Currency | EUR only |
| Tax year | Calendar year |
| Who is covered | Resident individuals with § 22 or § 23 EStG income |
| Primary legislation | Einkommensteuergesetz 1988 (EStG 1988) |
| Supporting legislation | Bundesabgabenordnung (BAO); GSVG; UStG 1994 |
| Tax authority | Finanzamt Österreich (BMF) |
| Filing portal | FinanzOnline (finanzonline.bmf.gv.at) |
| Filing deadline | 30 June via FinanzOnline, next year; paper by 30 April only if e-filing is unreasonable (Section 5.9) |
| Status | Not yet reviewed by an accountant |

### Progressive Tax Brackets (2026, adjusted for cold progression)

Re-indexed yearly; this is the page's 2026 block. Each person is taxed alone.

| Taxable yearly income | Marginal rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/tarifstufen.html |
| Up to and including EUR 13,539 | 0% | "13.539 und darunter 0 Prozent" |
| Over EUR 13,539 up to EUR 21,992 | 20% |  |
| Over EUR 21,992 up to EUR 36,458 | 30% |  |
| Over EUR 36,458 up to EUR 70,365 | 40% |  |
| Over EUR 70,365 up to EUR 104,859 | 48% |  |
| Over EUR 104,859 up to EUR 1,000,000 | 50% |  |
| Over EUR 1,000,000 | 55% | Temporary, years 2016 to 2029: "Befristet bis zum Jahr 2029" |
| 2026 uplift of the limits | 1.7333% | Two thirds of inflation; the EUR 1,000,000 step is not indexed |
| Official example: tariff tax on EUR 40,000 in 2026, before credits | EUR 7,447.20 | "Einkommensteuer 2026 7.447,20 Euro" |

Each rate taxes only its slice; credits (Section 5.6) come off the tax.

### Gewinnfreibetrag (Profit Allowance)

Deducted as the last business expense from the provisional profit. Rates for business years from 1 January 2024.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/gewinnfreibetrag.html |
| Grundfreibetrag: profit covered, no investment needed | EUR 33,000 | Once per person, even with several businesses |
| Grundfreibetrag rate | 15% | "Gewinne bis zu 33.000 Euro: 15 Prozent" |
| Grundfreibetrag maximum | EUR 4,950 | Also with any flat-rate method |
| Next EUR 145,000 of profit (investment needed) | 13% | "die nächsten 145.000 Euro: 13 Prozent" |
| Next EUR 175,000 | 7% | "die nächsten 175.000 Euro: 7 Prozent" |
| Next EUR 230,000 | 4.5% | "die nächsten 230.000 Euro: 4,5 Prozent" |
| No allowance on profit above | EUR 583,000 | "Für Gewinne über 583.000 Euro" |
| Maximum total allowance | EUR 46,400 | "somit 46.400 Euro" |
| Official example, case 1: profit EUR 40,000, investment EUR 6,000 | EUR 5,860 | Grundfreibetrag EUR 4,950 plus investment-based EUR 910 |

The investment-based part equals qualifying asset cost bought in the year: new depreciable assets with at least four years' life, or securities under § 14(7) no. 4 EStG. Not cars, used assets or GWG. Assets leaving within four years are taxed again. Never with a flat rate or on business sale gains.

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/investitionsfreibetrag.html |
| Investitionsfreibetrag on cost falling from 1 November 2025 to 31 December 2026 | 20% | On top of depreciation; assets of at least four years' life |
| The same for listed green assets | 22% | "bzw. 22 Prozent" |

Not with a flat rate, and not on an asset already used for the investment-based Gewinnfreibetrag; not cars (zero emission cars qualify), used assets or GWG. Assets leaving within four years are taxed again.

### Betriebsausgabenpauschale (Flat-Rate Expenses)

The Basispauschalierung (§ 17 EStG) replaces most actual expenses with a share of turnover.

| What | Value | Note |
| --- | --- | --- |
| Prior-year turnover limit from 2026 | EUR 420,000 | "ab 2026 sogar bei 420.000 Euro" (https://www.usp.gv.at/aktuelles/newsliste/basispauschalierung-hoehere-grenzen-ab-2025-und-2026.html) |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/pauschalierung-weitere-infos/basispauschalierung-einkommensteuer.html |
| Rate for commercial or technical consulting, asset managers, supervisory boards, shareholder employees with a stake over a quarter, lecturers, scientists, writers, teaching and educational work | 6% | "Gesellschafter-Dienstnehmer (Beteiligung > 25 Prozent)" |
| Maximum flat expenses at the lower rate in 2026 | EUR 25,200 | "höchstens 25.200 Euro (im Jahr 2025: 19.200 Euro" |
| Rate for all other activities from 2026 | 15% | "15 Prozent (im Jahr 2025: 13,5 Prozent" |
| Maximum flat expenses at the general rate from 2026 | EUR 63,000 | "höchstens 63.000 Euro (im Jahr 2025: 43.200 Euro" |

The same 15% is also the Grundfreibetrag rate: separate rules.

### Key E1/E1a Lines

Cash basis: schedule E 1a. Bookkeepers attach accounts.

| Line | Description |
| --- | --- |
| Betriebseinnahmen | Gross business revenue |
| Betriebsausgaben | Business expenses (actual or Pauschale) |
| Gewinn | Net profit |
| Gewinnfreibetrag | Profit allowance deduction |
| Sonderausgaben | Special expenses (church contributions, donations) |
| Absetzbeträge | Tax credits |
| Einkommensteuer | Tax payable |

### Conservative Defaults

| Ambiguity | Default |
| --- | --- |
| Unknown income type | Gewerbebetrieb (general flat rate) |
| Unknown expense method | Pauschale, if the turnover limit is met |
| Unknown business-use share | No deduction |
| Unknown investment for GFB | Grundfreibetrag only (EUR 4,950 max) |
| Unknown motor vehicle cost | Cap at EUR 40,000 (Section 5.4) |

## Section 2: Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable**: full-year bank statement, income type, expense method. **Recommended**: invoices, SVS statements, prior Steuerbescheid, asset register. **Ideal**: prior E/A-Rechnung, Vorauszahlungsbescheid, GFB investment documents.

**Missing minimum: SOFT WARN.** No bank statement is a hard stop.

### Refusal Catalogue

- **R-AT-1**: Corporations (GmbH, AG). **R-AT-2**: Partnerships (OG, KG). **R-AT-3**: Non-residents. **R-AT-4**: Group taxation. **R-AT-5**: Audits and appeals. All out of scope; see last section.

## Section 3: Transaction Pattern Library

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| UBERWEISUNG [client], ZAHLUNG, HONORAR | Betriebseinnahmen | Business income | Net if USt-registered |
| GEHALT, LOHN, DIENSTGEBER | Nichtselbständige Arbeit | NOT self-employment | Employment |
| MIETEINNAHME | Vermietung | NOT self-employment | Schedule E 1b |
| ZINSEN, KAPITALERTRAG, DIVIDENDE | Kapitalvermögen | NOT self-employment | Special rates, Section 5.6 |
| STRIPE PAYOUT, PAYPAL PAYOUT | Betriebseinnahmen | Business income | Platform payout |
| FINANZAMT GUTSCHRIFT, STEUERERSTATTUNG | EXCLUDE | Not income | Tax refund |

### 3.2 Expense Patterns (Debits): Fully Deductible

All fully deductible.

| Pattern | Category | Notes |
| --- | --- | --- |
| BÜROMIETE, GESCHÄFTSLOKAL | Raumkosten | Dedicated premises |
| BERUFSHAFTPFLICHT | Versicherung | Personal insurance is private |
| STEUERBERATER, RECHTSANWALT, NOTAR | Beratung | Business matters |
| BÜROMATERIAL, WERBUNG, GOOGLE ADS | Büro, Werbung |  |
| FORTBILDUNG, SEMINAR | Fortbildung | Current profession |
| KAMMERBEITRAG, WKO | Pflichtbeiträge |  |
| KONTOFÜHRUNG, STRIPE FEE, PAYPAL FEE | Bankspesen | Business account only |
| SOFTWARE, LIZENZ (up to EUR 1,000) | IT-Kosten | GWG, Section 5.3 |

### 3.3 Expense Patterns: SVS (Sozialversicherung)

All fully deductible.

| Pattern | Notes |
| --- | --- |
| SVS, SOZIALVERSICHERUNG | Before Gewinnfreibetrag; also next to the Pauschale |
| KRANKEN-, PENSIONS-, UNFALLVERSICHERUNG (SVS) | Amounts in `at-svs-contributions` |
| SELBSTÄNDIGENVORSORGE | Also next to the Pauschale |

### 3.4 Expense Patterns: Travel

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| FLUG, ÖBB, TAXI, UBER | Reisekosten | Fully deductible | Business purpose |
| HOTEL, BOOKING.COM | Reisekosten | Fully deductible | Actual cost or night flat rate |
| TAGESGELD, DIÄTEN | Reisekosten | Daily rate, Section 5.3 | Only on a "Reise" |
| TANKSTELLE, OMV, SHELL | Kfz-Kosten | T2: business share only | Section 5.4 |

### 3.5 Expense Patterns: NOT Deductible

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RESTAURANT (purely social) | NOT | No Werbezweck |
| BEWIRTUNG (with Werbezweck) | Half deductible | Section 6.4 |
| GESCHENKE an Geschäftsfreunde | NOT | Repräsentation |
| PRIVAT, SUPERMARKT | NOT | Living costs |
| STRAFE, GELDBUSSE | NOT | Fines |
| EINKOMMENSTEUER, ESt VORAUSZAHLUNG | NOT | Tax on income |
| PRIVATENTNAHME | NOT | Drawings |

### 3.6 Capital Items

Depreciation follows normal useful life; only buildings, goodwill and cars have statutory lives (Section 5.3). Other lives are legacy practice values; no allowed page prints them.

| Pattern | Useful Life | Notes |
| --- | --- | --- |
| COMPUTER, LAPTOP | 3 years (unconfirmed) |  |
| DRUCKER, SCANNER | 5 years (unconfirmed) |  |
| BÜROMÖBEL | 10 years (unconfirmed) |  |
| KFZ, AUTO (business) | 8 years, set by law | Limit EUR 40,000 |
| GEBÄUDE (business) | Rate set by law, Section 5.3 |  |
| GWG (not more than EUR 1,000) | Immediate |  |

### 3.7 Exclusions

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EIGENÜBERWEISUNG | EXCLUDE | Own transfer |
| DARLEHEN, TILGUNG | EXCLUDE | Loan principal |
| KREDITZINSEN (business) | Deductible | Business loan interest |
| USt ZAHLUNG | EXCLUDE (P&L) | Net system; an expense under the gross system |
| ESt VORAUSZAHLUNG | EXCLUDE | Credited in the assessment |

### 3.8 Austrian Banks: Statement Format Reference

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Erste Bank, Sparkasse | CSV, PDF | Buchungsdatum, Text, Betrag, Saldo | George export |
| Raiffeisen | CSV, PDF | Datum, Buchungstext, Betrag | ELBA export |
| Bank Austria (UniCredit) | CSV, PDF | Datum, Verwendungszweck, Betrag |  |
| BAWAG, easybank | CSV, PDF | Datum, Text, Betrag |  |
| N26, Revolut | CSV | Date, Counterparty, Amount |  |

## Section 4: Worked Examples

### Example 1: Client Payment (USt-registered)

`15.03.2026 ; Erste Bank Gutschrift ; DESIGN STUDIO WIEN ; Honorar März ; +3,600.00 ; EUR`

Net system: VAT is not income; a Kleinunternehmer books the whole receipt (`at-vat-return`). **Class:** Betriebseinnahmen, net amount.

### Example 2: SVS Contribution

`15.02.2026 ; Raiffeisen Lastschrift ; SVS BEITRAG Q1 ; -2,150.00 ; EUR`

Social insurance: fully deductible, also next to the Pauschale, before the GFB. **Class:** Betriebsausgabe.

### Example 3: Bewirtung (Half Deductible)

`22.04.2026 ; Erste Kartenzahlung ; RESTAURANT STEIRERECK ; Geschäftsessen ; -180.00 ; EUR`

Half deductible if it serves advertising and business far outweighs. Social: nothing. **Class:** T2. Flag for reviewer.

### Example 4: GWG Immediate Expensing

`03.06.2026 ; Bank Austria Karte ; IKEA WIEN ; BÜROSTUHL ; -790.00 ; EUR`

Below the GWG limit (Section 5.3). Cash basis: deduct in the year of payment. **Class:** Betriebsausgabe in full.

### Example 5: Luxustangente (Vehicle)

`01.07.2026 ; Raiffeisen ; KFZ LEASING GMBH ; Leasingrate PKW ; -650.00 ; EUR`

Car cost counts only up to the limit in Section 5.4, so depreciation or the matching leasing share is cut. Running costs count only if business trips exceed half the kilometres. **Class:** T2.

### Example 6: Kirchenbeitrag (Sonderausgabe)

`15.03.2026 ; Erste Lastschrift ; ERZDIÖZESE WIEN ; Kirchenbeitrag ; -400.00 ; EUR`

Sonderausgabe up to the cap in Section 5.5; the church reports it to the tax office. **Class:** Sonderausgabe.

## Section 5: Tier 1 Rules (When Data Is Clear)

### 5.1 Profit Computation

- **Profit Computation**: Revenue minus Betriebsausgaben (actual or Pauschale, not both) minus SVS = provisional Gewinn. Deduct the GFB, add other income, deduct Sonderausgaben and außergewöhnliche Belastungen, apply the tariff, subtract credits.

### 5.2 Betriebsausgabenpauschale Rules

- **Betriebsausgabenpauschale Rules**: Only if there is no duty to keep books and no books are kept voluntarily (condition not checked on an official page for this Guide), within the turnover limit (Section 1). Covers depreciation, rent, energy, advice, insurance, car and travel costs. On top at actual cost: goods for resale, wages, outside labour, social insurance, reimbursed travel, the Arbeitsplatzpauschale, half a business transport pass, the Grundfreibetrag. Leaving it locks it out for five business years.

### 5.3 AfA Rates

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/gesetzliche-afa-saetze.html |
| Business buildings since 2016 (40 years) | 2.5% | "einheitlich 2,5 Prozent" |
| Business buildings let for housing | 1.5% | "Ein Satz von 1,5 Prozent" |
| Goodwill of a trade or farm | 15 years | Fixed by law; a freelance practice is judged case by case |
| Cars and estate cars | 8 years | Not driving school cars or taxis |

| What | Value | Note |
| --- | --- | --- |
| GWG: asset costing not more than this is expensed at once | EUR 1,000 | Net with input VAT deduction, gross for an exempt small business (https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/geringwertige-wirtschaftsgueter.html) |

- **Halbjahresregel**: If acquired in second half of year, only half-year AfA.

| Travel (domestic) | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/reisekosten.html |
| Tagesgeld per 24 hours (after three hours one twelfth per started hour, full after 11 hours) | EUR 30 | "maximal 30 Euro (bis zum Jahr 2024: 26,40 Euro)" |
| Night flat rate incl. breakfast, instead of the bill | EUR 17 | "Pauschalbetrag in Höhe von 17 Euro" |
| Per km, private car used for business less than half the time | EUR 0.50 | "0,50 Euro (bis zum Jahr 2024: 0,42 Euro)" |

A "Reise" needs a point at least 25 km from the centre of activity.

### 5.4 Luxustangente

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/aktuelles/newsreihen/steuerrechtsreihe/steuerrechtsreihe-teil-7-besteuerung-von-kfz.html |
| Angemessenheitsgrenze: highest car cost recognised | EUR 40,000 | Cars and estate cars, not listed small vans |
| Highest yearly depreciation | EUR 5,000 | "höchstens 40.000/8 = 5.000 Euro" |
| Running costs deductible only if business km exceed | 50% | "mehr als 50 Prozent der jährlichen Kilometer" |

- **Luxustangente**: Value-based costs (comprehensive insurance, financing) cut in proportion.

### 5.5 Sonderausgaben

| Item | Limit | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/sonderausgaben-und-aussergewoehnliche-belastungen.html |
| Kirchenbeitrag, per year | EUR 600 | "bis höchstens 600 Euro" |
| Private donations to listed bodies | 10% | Of the same year's total income: "10 Prozent des Gesamtbetrags der Einkünfte" |
| Steuerberatungskosten | No cap printed | Normally a business expense instead |

Donations from business assets are business expenses. Voluntary continued insurance in the statutory pension scheme (including buying back periods), annuities and loss carry-forward are also Sonderausgaben.

### 5.6 Absetzbeträge (Tax Credits)

Credits reduce the tax, not the income.

| Credit, per year | EUR | Conditions |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/steuerabsetzbetraege.html |
| Alleinverdiener- or Alleinerzieherabsetzbetrag, one child | EUR 612 | Needs the Kinderabsetzbetrag for a child for more than six months of the year. Alleinverdiener: partner for more than six months, partner income limit below. Alleinerzieher: no partner |
| The same, two children | EUR 828 |  |
| Each further child | EUR 273 |  |
| Familienbonus Plus per minor child | EUR 2,000.16 |  |
| Familienbonus Plus per adult child with family allowance | EUR 700.08 |  |
| Kindermehrbetrag per child | EUR 700 | Low earners |
| Verkehrsabsetzbetrag | EUR 496 | Employees only |
| Supplement to it | EUR 804 | Employees, assessment only: full to income of EUR 19,761, nil at EUR 30,259 |

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.bmf.gv.at/dam/jcr:436f8c01-38e0-41bf-b904-c0e62a862bf1/251117_Steuerbuch2026_DE_BF.pdf |
| Alleinverdiener: highest partner income, 2026 | EUR 7,411 | Steuerbuch (2025 assessment) prints "(2026: 7.411 Euro)" |
| KESt special rates (bank deposits; other capital income) | 25% or 27.5% | Steuerbuch, 2025 assessment; generally final |
| Selbstbehalt (extraordinary expenses), income up to EUR 7,300 | 6% | Steuerbuch, 2025 assessment. Disability costs: none |
| Selbstbehalt, more than EUR 7,300 | 8% | Same source |
| Selbstbehalt, more than EUR 14,600 | 10% | Same source |
| Selbstbehalt, more than EUR 36,400 | 12% | Same source |

### 5.7 Vorauszahlungen (Quarterly)

- **Vorauszahlungen (Quarterly)**: Due 15 February, 15 May, 15 August, 15 November. First year: a profit estimate. Reduction on reasoned request until 30 September. Balances carry Anspruchszinsen interest from 1 October of the next year. A notice balance is due within one month.

| What | Value | Note |
| --- | --- | --- |
| Exemption limit for Anspruchszinsen | EUR 50 | "Freigrenze von 50 Euro" (https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuervorauszahlungen.html) |

### 5.8 Penalties

The pages print these rates in words.

| Offence | Penalty | Note |
| --- | --- | --- |
| Source | all rates below | https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/fristen-und-faelligkeiten.html |
| Late payment (Säumniszuschlag) | Two percent | Waived if at most five days late with a clean six months |
| Still unpaid three and six months after enforceability | One percent each | Second and third surcharge |

Late filing (Verspätungszuschlag): up to ten percent of the tax, if the delay is not excusable (late filing page in Sources).

### 5.9 Filing the E 1

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuererklaerung.html |
| Return due if income has no wages and exceeds (2026) | EUR 13,539 | Same number as the zero bracket, a separate rule. Bookkeepers always file |
| With wages: other income of more than | EUR 730 | AND income above the next row |
| Income limit where wages are present (2026) | EUR 14,769 | "14.769 Euro (im Jahr 2026)" |
| Foreign capital income without KESt, special rate | 27.5% | Must be declared |

Deadlines: 30 June of the next year via FinanzOnline, which is the rule; 30 April on paper, allowed only where electronic filing is not reasonable; extension on request, longer with a tax adviser. Filing in a loss year is advised, so the loss is set for carry-forward. Schedules: E 1a, E 1b (letting), E 1kv (capital), L 1k (children), L 1ab. Appeal within one month.

## Section 6: Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Investitionsbedingter Gewinnfreibetrag

- **Investitionsbedingter Gewinnfreibetrag**: Qualifying assets, listed in asset register, kept four years. Flag.

### 6.2 Home Office (Arbeitszimmer)

- **Home Office (Arbeitszimmer)**: Only if the room is centre of the whole activity; pro rata by floor area. Otherwise the Arbeitsplatzpauschale (not quantified).

### 6.3 Vehicle Business Use

- **Vehicle Business Use**: Section 5.4. Logbook needed. Running costs apportioned.

### 6.4 Bewirtung

- **Bewirtung**: Half deductible with documented Werbezweck and overwhelming business reason; nothing if social. Flag for reviewer.

### 6.5 Pauschale vs Actual Comparison

- **Pauschale vs Actual Comparison**: Flag if actual expenses may beat Pauschale; mind the five-year lock.

### 6.6 Aussergewohnliche Belastungen

- **Aussergewohnliche Belastungen**: Above Selbstbehalt (Section 5.6). Documents required.

## Section 7: Excel Working Paper Template

~~~
Austrian income tax: E 1 working paper
Tax Year: 2026
Client: __
Income Type: Gewerbebetrieb / Selbständige Arbeit
Expense Method: Actual / Pauschale

A. BETRIEBSEINNAHMEN
  A1. Umsatzerlöse (net of USt) __
  A2. Sonstige Einnahmen __
  A3. Total __

B. BETRIEBSAUSGABEN
  B1. SVS Beiträge __
  B2. Actual OR Pauschale (15%/6%) __
  B3. AfA (Abschreibungen) __
  B4. Total Betriebsausgaben __

C. GEWINN (A3 - B4) __

D. GEWINNFREIBETRAG
  D1. Grundfreibetrag (15% up to EUR 33,000) __
  D2. Investitionsbedingter GFB (not with Pauschale) __
  D3. Total GFB __

E. SONDERAUSGABEN
  E1. Kirchenbeitrag (max EUR 600) __
  E2. Spenden __
  E3. Total __

F. EINKOMMEN (C - D3 - E3) __
G. TAX (2026 brackets on F) __
H. ABSETZBETRÄGE __
I. EINKOMMENSTEUER (G - H) __

REVIEWER FLAGS:
  [ ] Income type confirmed?
  [ ] Expense method confirmed?
  [ ] SVS contributions confirmed?
  [ ] GFB investments confirmed?
  [ ] Car limit applied?
  [ ] Bewirtung Werbezweck documented?
~~~

## Section 8: Bank Statement Reading Guide

### Austrian Bank Statement Formats

**Austrian Bank Statement Formats**: as in Section 3.8. Regional Raiffeisen banks vary.

### Key Austrian Banking Terms

| Term | English | Hint |
| --- | --- | --- |
| Gutschrift | Credit | Potential income |
| Lastschrift | Direct debit | Expense |
| Überweisung | Transfer | Check direction |
| Dauerauftrag | Standing order | Regular expense |
| Bankomat | ATM withdrawal | Ask purpose |
| Kontoführung | Account maintenance | Bank charge |

## Section 9: Onboarding Fallback

~~~
Onboarding questions for Austrian income tax:
1. Income type: Gewerbebetrieb or selbständige Arbeit?
2. Expense method: actual or Pauschale?
3. Family status and children?
4. SVS contributions paid in the year?
5. Home office: dedicated room? Floor share?
6. Vehicle: cost and business share?
7. Qualifying investments for Gewinnfreibetrag?
8. Kirchenbeitrag paid?
9. Other income (employment, rental, capital)?
10. Prior year Steuerbescheid available?
~~~

## Section 10: Reference Material

### Key Legislation

| Topic | Reference |
| --- | --- |
| Tariff, credits; allowance; flat rate | §§ 33, 10, 17 EStG |
| Expenses; AfA; GWG | §§ 4, 20, 7, 8, 13 EStG |
| Sonderausgaben; außergewöhnliche Belastungen | §§ 18, 4a, 34, 35 EStG |
| Prepayments; deadlines; surcharges | § 45 EStG; §§ 134, 135, 217 BAO |

### Test Suite

Repeats the official worked examples already tabulated above: the 2026 tariff on EUR 40,000, the GFB case 1 allowance, car depreciation (at most EUR 5,000, less the private share), the church contributions cap and the turnover limit.

## The method, step by step

1. **Check return duty and income type** (§§ 22, 23, 42 EStG): https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuererklaerung.html
2. **Choose profit method**: actual expenses or the Basispauschalierung (§ 17 EStG): https://www.usp.gv.at/aktuelles/newsliste/basispauschalierung-hoehere-grenzen-ab-2025-und-2026.html
3. **Compute profit, then deduct the Gewinnfreibetrag** (§ 10 EStG): https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/gewinnfreibetrag.html
4. **Deduct Sonderausgaben and außergewöhnliche Belastungen** (§§ 18, 34 EStG): https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/sonderausgaben-und-aussergewoehnliche-belastungen.html
5. **Apply 2026 tariff, subtract credits** (§ 33 EStG): https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/tarifstufen.html
6. **File E 1 with E 1a via FinanzOnline by 30 June** of the next year, then check the prepayment notice (§ 45 EStG): https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuervorauszahlungen.html

## Ask the client first

- Which activity exactly? The flat rate differs.
- Bookkeeping duty, and last year's turnover? Decides the flat rate.
- New qualifying assets bought, kept four years? Decides the investment-based allowance.
- Partner, children, or a job too? Changes credits and the return duty.
- Car business share of kilometres?
- Flat rate left within the last five years?

## When to refuse or refer

- Companies: `at-corporate-income-tax`; formation: `at-company-formation`.
- Partnerships, non-residents, moves abroad, treaty cases: refer.
- VAT and the small business exemption: `at-vat-return`. Social insurance: `at-svs-contributions`. All taxes: `at-tax-overview`.
- Farming, sector flat rates, Kleinunternehmerpauschalierung, business sales, real estate gains, audits, appeals, years other than 2026: refer.

## PROHIBITIONS

- NEVER apply brackets without confirming income type
- NEVER allow both Pauschale AND actual expenses (except the items allowed on top)
- NEVER apply investitionsbedingter GFB without confirmed investments, or with a Pauschale
- NEVER apply car AfA above the EUR 40,000 limit
- NEVER allow income tax or fines as deductions
- NEVER expense GWG over EUR 1,000 immediately
- NEVER reuse a prior year's brackets or credits
- NEVER present calculations as definitive

## Sources

- https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/tarifstufen.html
- https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/steuerabsetzbetraege.html
- https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuererklaerung.html
- https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuervorauszahlungen.html
- https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/sonderausgaben-und-aussergewoehnliche-belastungen.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/gewinnfreibetrag.html
- https://www.usp.gv.at/aktuelles/newsliste/basispauschalierung-hoehere-grenzen-ab-2025-und-2026.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/pauschalierung-weitere-infos/basispauschalierung-einkommensteuer.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/gesetzliche-afa-saetze.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/geringwertige-wirtschaftsgueter.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/nichtabzugsfaehige-ausgaben.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/reisekosten.html
- https://www.usp.gv.at/aktuelles/newsreihen/steuerrechtsreihe/steuerrechtsreihe-teil-7-besteuerung-von-kfz.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/fristen-und-faelligkeiten.html
- https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/einreichen-von-steuererklaerungen.html
- https://www.bmf.gv.at/dam/jcr:436f8c01-38e0-41bf-b904-c0e62a862bf1/251117_Steuerbuch2026_DE_BF.pdf

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

> Contributed by OpenAccountants.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
