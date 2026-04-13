---
name: at-income-tax
description: >
  Use this skill whenever asked about Austrian income tax (Einkommensteuer) for self-employed individuals filing form E1. Trigger on phrases like "Einkommensteuer", "ESt", "E1 Erklarung", "Gewinnfreibetrag", "Betriebsausgabenpauschale", "Absetzbetrge", "Sonderausgaben", "selbstandig Steuer Osterreich", "Austrian income tax", "self-employed tax Austria", or any question about computing or filing income tax for a self-employed person in Austria. This skill covers progressive tax brackets (0--55%), Gewinnfreibetrag, Betriebsausgabenpauschale, Sonderausgaben, aussergewohnliche Belastungen, Absetzbetrge, SV deductibility, and E1/E1a structure. ALWAYS read this skill before touching any Austrian income tax work.
version: 2.0
jurisdiction: AT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Austria Income Tax (ESt E1) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Austria (Republik Osterreich) |
| Tax | Einkommensteuer (ESt) |
| Currency | EUR only |
| Tax year | Calendar year |
| Primary legislation | Einkommensteuergesetz 1988 (EStG 1988) |
| Supporting legislation | Bundesabgabenordnung (BAO); GSVG; UStG 1994 |
| Tax authority | Bundesministerium fur Finanzen (BMF) |
| Filing portal | FinanzOnline (finanzonline.bmf.gv.at) |
| Filing deadline | 30 April (paper) / 30 June (FinanzOnline) / end Feb year+2 (with Steuerberater) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by Austrian Steuerberater or Wirtschaftsprufer |
| Validation date | Pending |
| Skill version | 2.0 |

### Progressive Tax Brackets (2025, adjusted for cold progression)

| Taxable Income (EUR) | Marginal Rate |
|---|---|
| 0 -- 13,308 | 0% |
| 13,309 -- 21,617 | 20% |
| 21,618 -- 35,836 | 30% |
| 35,837 -- 69,166 | 40% |
| 69,167 -- 103,072 | 48% |
| 103,073 -- 1,000,000 | 50% |
| Above 1,000,000 | 55% |

**The 55% rate was originally temporary (2016-2025) and remains in effect for 2025.**

### Gewinnfreibetrag (Profit Allowance)

| Profit Range (EUR) | Rate | Investment Required? |
|---|---|---|
| 0 -- 33,000 | 15% | No (Grundfreibetrag, automatic) |
| 33,001 -- 178,000 | 13% | Yes (qualifying assets/securities) |
| 178,001 -- 353,000 | 7% | Yes |
| 353,001 -- 583,000 | 4.5% | Yes |

Maximum GFB: EUR 46,400. Grundfreibetrag (15% of first EUR 33,000 = max EUR 4,950) is automatic.

### Betriebsausgabenpauschale (Flat-Rate Expenses)

| Category | Rate | Cap |
|---|---|---|
| Gewerbebetrieb | 12% of turnover | EUR 26,400 |
| Certain professions (writers, scientists, consultants) | 6% of turnover | EUR 13,200 |

### Key E1/E1a Lines

| Line | Description |
|---|---|
| Betriebseinnahmen | Gross business revenue |
| Betriebsausgaben | Business expenses (actual or Pauschale) |
| Gewinn | Net profit |
| Gewinnfreibetrag | Profit allowance deduction |
| Sonderausgaben | Special expenses (church tax, donations) |
| Absetzbetrge | Tax credits |
| Einkommensteuer | Tax payable |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown income type | Gewerbebetrieb (12% Pauschale) |
| Unknown expense method | Betriebsausgabenpauschale |
| Unknown business-use % | 0% deduction |
| Unknown investment for GFB | Grundfreibetrag only (EUR 4,950 max) |
| Unknown motor vehicle cost | Cap at EUR 40,000 (Luxustangente) |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year, plus confirmation of income type (Gewerbebetrieb vs selbstandige Arbeit) and expense method (actual vs Pauschale).

**Recommended** -- all invoices, SVS contribution statements, prior year Steuerbescheid, asset register.

**Ideal** -- complete E/A-Rechnung from prior year, Anlageverzeichnis, Vorauszahlungsbescheid, qualifying investment documentation for GFB.

**Refusal if minimum is missing -- SOFT WARN.** No bank statement = hard stop.

### Refusal Catalogue

**R-AT-1 -- Corporations (GmbH, AG).** "This skill covers natural persons only. Kapitalgesellschaften file Korperschaftsteuer. Out of scope."

**R-AT-2 -- Partnerships (OG, KG).** "Partnership income requires separate determination. Out of scope."

**R-AT-3 -- Non-resident.** "Non-resident taxation has different rules. Escalate."

**R-AT-4 -- Group taxation.** "Group structures are out of scope."

**R-AT-5 -- Finanzamt audit / appeal.** "Escalate to Steuerberater."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| UBERWEISUNG [client], ZAHLUNG, HONORAR | Betriebseinnahmen | Business income | Extract net if USt-registered |
| GEHALT, LOHN, DIENSTGEBER | Einkünfte nichtselbstandige Arbeit | NOT self-employment | Employment -- separate |
| MIETEINNAHME | Einkünfte Vermietung | NOT self-employment | Rental income |
| ZINSEN, KAPITALERTRAG, DIVIDENDE | Einkünfte Kapitalvermögen | NOT self-employment | Capital income -- KESt 27.5% |
| STRIPE PAYOUT, PAYPAL PAYOUT | Betriebseinnahmen | Business income | Platform payout |
| FINANZAMT GUTSCHRIFT, STEUERERSTATTUNG | EXCLUDE | Not income | Tax refund |

### 3.2 Expense Patterns (Debits) -- Fully Deductible

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| BÜROMIETE, GESCHÄFTSLOKAL, OFFICE RENT | Raumkosten | Fully deductible | Dedicated premises |
| BERUFSHAFTPFLICHT, VERSICHERUNG (business) | Versicherung | Fully deductible | Professional insurance |
| STEUERBERATER, WIRTSCHAFTSPRÜFER, BUCHHALTER | Beratungskosten | Fully deductible | |
| RECHTSANWALT, NOTAR (business) | Rechtskosten | Fully deductible | |
| BÜROMATERIAL, SCHREIBWAREN | Bürobedarf | Fully deductible | |
| WERBUNG, MARKETING, GOOGLE ADS | Werbekosten | Fully deductible | |
| FORTBILDUNG, SEMINAR, KURS | Fortbildungskosten | Fully deductible | Current profession |
| KAMMERBEITRAG, WKO | Pflichtbeiträge | Fully deductible | Compulsory chamber |
| KONTOFÜHRUNG, BANKSPESEN | Bankspesen | Fully deductible | Business account |
| STRIPE FEE, PAYPAL FEE | Transaktionskosten | Fully deductible | |
| SOFTWARE, LIZENZ, SUBSCRIPTION (under EUR 1,000) | IT-Kosten | Fully deductible | GWG if under EUR 1,000 |

### 3.3 Expense Patterns -- SVS (Sozialversicherung)

| Pattern | Treatment | Notes |
|---|---|---|
| SVS, SVA, SOZIALVERSICHERUNG | Fully deductible as Betriebsausgabe | Deducted BEFORE Gewinnfreibetrag |
| KRANKENVERSICHERUNG (SVS) | Fully deductible | Part of SVS |
| PENSIONSVERSICHERUNG (SVS) | Fully deductible | Part of SVS |
| UNFALLVERSICHERUNG (SVS) | Fully deductible | Fixed monthly amount |

### 3.4 Expense Patterns -- Travel

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| FLUG, AUA, RYANAIR, EASYJET | Reisekosten | Fully deductible | Business purpose |
| HOTEL, BOOKING.COM | Reisekosten | Fully deductible | Business travel |
| ÖBB, WESTBAHN | Reisekosten | Fully deductible | Business travel |
| TAXI, UBER, BOLT | Reisekosten | Fully deductible | Business purpose |
| TAGESGELD, DIÄTEN | Reisekosten | EUR 26.40/day domestic | Per diem rates |
| TANKSTELLE, OMV, BP, SHELL | Kfz-Kosten | T2 -- business % only | |

### 3.5 Expense Patterns -- NOT Deductible

| Pattern | Treatment | Notes |
|---|---|---|
| RESTAURANT (purely social) | NOT deductible | Entertainment without Werbezweck |
| BEWIRTUNG (with Werbezweck) | 50% deductible | Must document business purpose |
| PRIVAT, LEBENSMITTEL, SUPERMARKT | NOT deductible | Personal living costs |
| STRAFE, GELDBUSSE | NOT deductible | Fines |
| EINKOMMENSTEUER, ESt VORAUSZAHLUNG | NOT deductible | Tax on income |
| PRIVATENTNAHME | NOT deductible | Drawings |

### 3.6 Capital Items

| Pattern | Useful Life | Annual Rate | Notes |
|---|---|---|---|
| COMPUTER, LAPTOP, PC | 3 years | 33.3% | |
| DRUCKER, SCANNER | 5 years | 20% | |
| BÜROMÖBEL, SCHREIBTISCH | 10 years | 10% | |
| KFZ, AUTO (business) | 8 years | 12.5% | Luxustangente: cap EUR 40,000 |
| GEBÄUDE (commercial) | 33 years | 3% | |
| GWG (under EUR 1,000 net) | Immediate | 100% | Geringwertiges Wirtschaftsgut |

### 3.7 Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| EIGENÜBERWEISUNG, INTERNAL | EXCLUDE | Own-account transfer |
| DARLEHEN, KREDIT, TILGUNG | EXCLUDE | Loan principal |
| KREDITZINSEN (business) | Deductible | Business loan interest |
| USt ZAHLUNG | EXCLUDE from P&L | USt is balance sheet |
| ESt VORAUSZAHLUNG | EXCLUDE | Not expense; tracked for assessment |

### 3.8 Austrian Banks -- Statement Format Reference

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| Erste Bank, Sparkasse | CSV, PDF | Buchungsdatum, Text, Betrag, Saldo | George online banking export |
| Raiffeisen | CSV, PDF | Datum, Buchungstext, Betrag | Raiffeisen ELBA export |
| Bank Austria (UniCredit) | CSV, PDF | Datum, Verwendungszweck, Betrag | |
| BAWAG, easybank | CSV, PDF | Datum, Text, Betrag | |
| N26, Revolut | CSV | Date, Counterparty, Amount | Clean data |

---

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (USt-registered)

**Input line:**
`15.03.2025 ; Erste Bank Gutschrift ; DESIGN STUDIO WIEN ; Honorar März ; +3,600.00 ; EUR`

**Reasoning:**
Client payment. If USt-registered (20% USt), EUR 3,600 gross. Net = EUR 3,000 (Betriebseinnahme) + EUR 600 USt. If Kleinunternehmer, full EUR 3,600.

**Classification:** Betriebseinnahmen = EUR 3,000 (or EUR 3,600 if Kleinunternehmer).

### Example 2 -- SVS Contribution

**Input line:**
`15.02.2025 ; Raiffeisen Lastschrift ; SVS BEITRAG Q1 ; -2,150.00 ; EUR`

**Reasoning:**
SVS (social insurance). Fully deductible as Betriebsausgabe. Deducted before computing Gewinnfreibetrag.

**Classification:** Betriebsausgabe -- SVS. Fully deductible.

### Example 3 -- Bewirtung (50% Deductible)

**Input line:**
`22.04.2025 ; Erste Kartenzahlung ; RESTAURANT STEIRERECK ; Geschäftsessen ; -180.00 ; EUR`

**Reasoning:**
Business entertainment. In Austria, 50% deductible IF clear Werbezweck (advertising/business purpose) is documented. Purely social = 0%.

**Classification:** T2 -- 50% deductible (EUR 90) if business purpose documented. Flag for reviewer.

### Example 4 -- GWG Immediate Expensing

**Input line:**
`03.06.2025 ; Bank Austria Karte ; IKEA WIEN ; BÜROSTUHL ; -790.00 ; EUR`

**Reasoning:**
Office chair EUR 790 net. Under EUR 1,000 GWG threshold. Immediate full deduction.

**Classification:** Betriebsausgabe. Fully deductible in year of purchase.

### Example 5 -- Luxustangente (Vehicle)

**Input line:**
`01.07.2025 ; Raiffeisen ; KFZ LEASING GMBH ; Leasingrate PKW ; -650.00 ; EUR`

**Reasoning:**
Vehicle leasing. For AfA purposes, cost capped at EUR 40,000 (Luxustangente). If car costs EUR 55,000, only EUR 40,000 / 8 years = EUR 5,000/year x business %. Running costs also limited proportionally.

**Classification:** T2 -- confirm vehicle cost, Luxustangente application, and business %.

### Example 6 -- Kirchenbeitrag (Sonderausgabe)

**Input line:**
`15.03.2025 ; Erste Lastschrift ; ERZDIÖZESE WIEN ; Kirchenbeitrag ; -400.00 ; EUR`

**Reasoning:**
Church tax. Sonderausgabe, capped at EUR 600/year. NOT a Betriebsausgabe.

**Classification:** Sonderausgabe (EUR 400, within EUR 600 cap). NOT in Betriebsausgaben.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Profit Computation

Revenue minus Betriebsausgaben (actual or Pauschale, not both) minus SVS = Gewinn. Then apply Gewinnfreibetrag.

### 5.2 Betriebsausgabenpauschale Rules

- Alternative to actual expenses. Choose one, not both.
- Still deduct SVS and GFB on top of Pauschale.
- 12% for Gewerbebetrieb (max EUR 26,400); 6% for certain professions (max EUR 13,200).

### 5.3 AfA Rates

| Asset | Life | Rate |
|---|---|---|
| Computer hardware/software | 3 years | 33.3% |
| Office furniture | 10 years | 10% |
| Motor vehicles | 8 years | 12.5% |
| Plant/machinery | 5-15 years | 6.7%-20% |
| Commercial buildings | 33 years | 3% |
| GWG (under EUR 1,000 net) | Immediate | 100% |

Halbjahresregel: if acquired in second half of year, only half-year AfA.

### 5.4 Luxustangente

Motor vehicle AfA capped at EUR 40,000. If car costs EUR 55,000, AfA on EUR 40,000 only.

### 5.5 Sonderausgaben

| Item | Limit |
|---|---|
| Kirchenbeitrag | EUR 600/year |
| Spenden (listed organisations) | 10% of prior year income |
| Steuerberatungskosten | Unlimited (also qualifies as Betriebsausgabe) |
| Sonderausgabenpauschale (default) | EUR 60/year |

### 5.6 Absetzbetrge (Tax Credits)

| Credit | EUR | Conditions |
|---|---|---|
| Alleinverdienerabsetzbetrag | 572 (no child) to 746+ | Partner income max EUR 6,937 |
| Alleinerzieherabsetzbetrag | 572+ | Single parent |
| Verkehrsabsetzbetrag | 463 | Commuters (if also employed) |
| Kindermehrbetrag | Up to 700 | Low-income with children |

### 5.7 Vorauszahlungen (Quarterly)

Deadlines: 15 Feb, 15 May, 15 Aug, 15 Nov. Based on most recent Bescheid.

### 5.8 Penalties

| Offence | Penalty |
|---|---|
| Late filing (Verspatungszuschlag) | Up to 10% of assessed tax |
| Late payment (Sumniszuschlag) | 2% first instance |
| Repeated late payment | +1% each (2nd, 3rd) |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Investitionsbedingter Gewinnfreibetrag

Requires purchase of qualifying physical assets (4+ year life) or qualifying Wertpapiere. Flag for reviewer to confirm investments.

### 6.2 Home Office (Arbeitszimmer)

Must be dedicated room, centre of professional activity. Dual-use does not qualify. Proportional by floor area.

### 6.3 Vehicle Business Use

Luxustangente EUR 40,000. Business % requires documentation. Running costs apportioned.

### 6.4 Bewirtung

50% deductible if Werbezweck documented. 0% if purely social. Flag for reviewer.

### 6.5 Pauschale vs Actual Comparison

Flag for reviewer if actual expenses may produce better result than Pauschale.

### 6.6 Aussergewohnliche Belastungen

Deductible above Selbstbehalt (6-12% of income). Medical, disability, catastrophe. Documentation required.

---

## Section 7 -- Excel Working Paper Template

```
AUSTRIA INCOME TAX -- E1 WORKING PAPER
Tax Year: 2025
Client: ___________________________
Income Type: Gewerbebetrieb / Selbständige Arbeit
Expense Method: Actual / Pauschale

A. BETRIEBSEINNAHMEN
  A1. Umsatzerlöse (net of USt if registered)    ___________
  A2. Sonstige Einnahmen                          ___________
  A3. Total                                        ___________

B. BETRIEBSAUSGABEN
  B1. SVS Beiträge                                ___________
  B2. Actual expenses OR Pauschale (12%/6%)       ___________
  B3. AfA (Abschreibungen)                        ___________
  B4. Total Betriebsausgaben                      ___________

C. GEWINN (A3 - B4)                               ___________

D. GEWINNFREIBETRAG
  D1. Grundfreibetrag (15% x first EUR 33,000)   ___________
  D2. Investitionsbedingter GFB                    ___________
  D3. Total GFB                                    ___________

E. SONDERAUSGABEN
  E1. Kirchenbeitrag (max EUR 600)                ___________
  E2. Spenden                                      ___________
  E3. Total                                        ___________

F. EINKOMMEN (C - D3 - E3)                        ___________

G. TAX (apply brackets to F)                       ___________

H. ABSETZBETRÄGE                                   ___________

I. EINKOMMENSTEUER (G - H)                         ___________

REVIEWER FLAGS:
  [ ] Income type confirmed (Gewerbe/Selbständig)?
  [ ] Expense method confirmed (actual/Pauschale)?
  [ ] SVS contributions confirmed?
  [ ] Qualifying investments for GFB confirmed?
  [ ] Luxustangente applied if vehicle?
  [ ] Bewirtung documented with Werbezweck?
```

---

## Section 8 -- Bank Statement Reading Guide

### Austrian Bank Statement Formats

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| Erste Bank / Sparkasse | CSV, PDF (George) | Buchungsdatum, Text, Betrag | George export is clean CSV |
| Raiffeisen | CSV, PDF (ELBA) | Datum, Buchungstext, Betrag | Regional Raiffeisen banks vary |
| Bank Austria (UniCredit) | CSV, PDF | Datum, Verwendungszweck, Betrag | |
| BAWAG / easybank | CSV, PDF | Datum, Text, Betrag | |
| N26 / Revolut | CSV | Date, Counterparty, Amount | Neobank format |

### Key Austrian Banking Terms

| Term | English | Hint |
|---|---|---|
| Gutschrift | Credit | Potential income |
| Lastschrift | Direct debit | Expense |
| Überweisung | Transfer | Check direction |
| Dauerauftrag | Standing order | Regular expense |
| Bankomat | ATM withdrawal | Ask purpose |
| Kontoführung | Account maintenance | Bank charge |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- AUSTRIA INCOME TAX
1. Income type: Gewerbebetrieb or selbständige Arbeit?
2. Expense method: actual Betriebsausgaben or Pauschale?
3. Family status: single, Alleinverdiener, Alleinerzieher?
4. SVS contributions: total paid in the year?
5. Home office: dedicated room? Floor area %?
6. Vehicle: Luxustangente applicable? Business %?
7. Qualifying investments for Gewinnfreibetrag?
8. Kirchenbeitrag paid?
9. Other income (employment, rental, capital)?
10. Prior year Steuerbescheid available?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Tax brackets | EStG 1988, s.33 (cold progression adjusted) |
| Gewinnfreibetrag | EStG 1988, s.10 |
| Betriebsausgabenpauschale | EStG 1988, s.17 |
| Betriebsausgaben | EStG 1988, s.4 Abs 4 |
| AfA | EStG 1988, s.7, s.8 |
| GWG | EUR 1,000 net threshold |
| Luxustangente | EUR 40,000 |
| Sonderausgaben | EStG 1988, s.18 |
| Absetzbetrge | EStG 1988, s.33 |
| SVS deductibility | GSVG; EStG s.4 Abs 4 |
| Filing deadlines | BAO; EStG |

### Test Suite

**Test 1 -- Mid-range, actual expenses.**
Input: Gewerbebetrieb, turnover EUR 60,000, expenses EUR 12,000, SVS EUR 8,000.
Expected: Profit EUR 40,000. GFB Grundfreibetrag EUR 4,950. Taxable ~EUR 35,050.

**Test 2 -- Pauschale comparison.**
Input: Gewerbebetrieb, turnover EUR 50,000, actual expenses EUR 4,000, SVS EUR 6,500.
Expected: Pauschale EUR 6,000 > actual EUR 4,000. Pauschale method better.

**Test 3 -- Luxustangente.**
Input: Car EUR 60,000, 80% business.
Expected: AfA capped EUR 40,000 / 8 = EUR 5,000 x 80% = EUR 4,000.

**Test 4 -- GWG immediate.**
Input: EUR 900 office chair.
Expected: Full deduction in year of purchase.

**Test 5 -- Kirchenbeitrag cap.**
Input: EUR 800 Kirchenbeitrag.
Expected: Sonderausgabe capped at EUR 600.

**Test 6 -- GFB with investment.**
Input: Profit EUR 80,000, qualifying investments EUR 10,000.
Expected: Grundfreibetrag EUR 4,950 + investment GFB EUR 6,110 = EUR 11,060.

---

## PROHIBITIONS

- NEVER apply brackets without confirming income type
- NEVER allow both Pauschale AND actual expenses (except SVS and GFB)
- NEVER apply investitionsbedingter GFB without confirmed qualifying investments
- NEVER apply vehicle AfA above EUR 40,000 Luxustangente
- NEVER allow income tax as a deduction
- NEVER allow fines as deductions
- NEVER allow GWG over EUR 1,000 to be expensed immediately (unless elected)
- NEVER present calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
