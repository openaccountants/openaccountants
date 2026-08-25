---
name: germany-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Kontenrahmen, SKR03, SKR04, financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, GWG, or day-to-day accounting for a German entity. Trigger on phrases like "Kontenrahmen", "SKR03", "SKR04", "HGB", "Buchhaltung", "chart of accounts Germany", "EÜR", "Einnahmen-Überschussrechnung", "Bilanz", "GuV", "capitalise or expense Germany", "GWG threshold", "Geringwertige Wirtschaftsgüter", "depreciation Germany", "AfA", "bank reconciliation Germany", "Kleinunternehmer", "bookkeeping Germany", or any question about recording transactions, classifying expenses, or preparing accounts under German law. ALWAYS read this skill before touching any bookkeeping work for Germany.
version: 1.0
jurisdiction: DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany Bookkeeping

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Germany (Bundesrepublik Deutschland) |
| Currency | EUR |
| Financial year | Calendar year (1 Jan -- 31 Dec) for sole traders and partnerships; companies may choose any 12-month period |
| Accounting standards | HGB (Handelsgesetzbuch) — German Commercial Code |
| GAAP framework | German GAAP (GoB — Grundsätze ordnungsmäßiger Buchführung) |
| Standard chart of accounts | SKR03 (process-oriented) and SKR04 (financial-statement-oriented), published by DATEV |
| Governing body | Bundesanstalt für Finanzdienstleistungsaufsicht (BaFin) for public entities; Finanzamt for tax |
| Key legislation | HGB §§ 238--342e; EStG (Einkommensteuergesetz); UStG (Umsatzsteuergesetz); AO (Abgabenordnung) |
| Record retention | 10 years for books and records; 6 years for business correspondence (AO § 147) |
| Digital requirements | GoBD compliance mandatory — all digital records must be tamper-proof and auditable |

## Section 2 -- Standard Chart of Accounts (SKR04 — Abschlussgliederungsprinzip)

SKR04 is organised to mirror the balance sheet and income statement structure. SKR03 (process-oriented) is also widely used, especially by sole traders and EÜR filers. The mapping below uses SKR04 with SKR03 equivalents noted.

### Class 0: Non-Current Assets (Anlagevermögen)

**Class 0: Non-Current Assets (Anlagevermögen)**

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 0027 | 0027 | Goodwill (Geschäfts- oder Firmenwert) |  |
| 0030 | 0030 | Software and licences |  |
| 0200 | 0210 | Technical equipment and machinery |  |
| 0320 | 0320 | Motor vehicles (Fuhrpark) |  |
| 0400 | 0410 | Office equipment (Betriebs- und Geschäftsausstattung) |  |
| 0420 | 0420 | Computer hardware (EDV-Anlagen) |  |
| 0440 | 0440 | Furniture and fittings (Büromöbel) |  |
| 0500 | 0510 | Buildings on own land (Bauten auf eigenen Grundstücken) |  |

### Class 1: Current Assets (Umlaufvermögen)

**Class 1: Current Assets (Umlaufvermögen)**

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 1200 | 1200 | Trade receivables (Forderungen aus L.u.L.) |  |
| 1400 | 1400 | VAT receivable (Vorsteuer) | Input VAT |
| 1406 | 1406 | VAT receivable 19% | Standard rate |
| 1410 | 1571 | VAT receivable 7% | Reduced rate |
| 1460 | 1580 | VAT receivable (reverse charge) |  |
| 1600 | 1600 | VAT payable (Umsatzsteuer) | Output VAT |
| 1800 | 1200 | Bank (Kasse / Bank) | Main bank account |
| 1810 | 1210 | Bank account 2 |  |
| 1890 | 1000 | Cash in hand (Kasse) |  |

### Class 2: Equity (Eigenkapital)

**Class 2: Equity (Eigenkapital)**

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 2000 | 0800 | Share capital / registered capital (Gezeichnetes Kapital) |  |
| 2050 | 0850 | Capital reserves (Kapitalrücklage) |  |
| 2970 | 0860 | Retained earnings (Gewinnvortrag) |  |
| 2978 | 0868 | Loss carried forward (Verlustvortrag) |  |

### Class 3: Liabilities (Fremdkapital)

**Class 3: Liabilities (Fremdkapital)**

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 3300 | 1600 | Trade payables (Verbindlichkeiten aus L.u.L.) |  |
| 3500 | 0630 | Bank loans (long-term) |  |
| 3510 | 0640 | Bank loans (short-term) |  |
| 3700 | 1740 | VAT payable (Umsatzsteuerverbindlichkeit) |  |
| 3790 | 1790 | Other tax liabilities |  |
| 3800 | 1700 | Accruals (Rückstellungen) |  |
| 3900 | 1900 | Deferred income (Rechnungsabgrenzung passiv) |  |

### Class 4: Revenue (Betriebliche Erträge)

**Class 4: Revenue (Betriebliche Erträge)**

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 4000 | 8000 | Revenue from goods (Umsatzerlöse) | 19% VAT |
| 4100 | 8100 | Revenue — reduced rate | 7% VAT |
| 4125 | 8125 | Revenue — tax-free with input VAT deduction | Intra-EU, exports |
| 4130 | 8130 | Revenue — tax-free without input VAT deduction | §4 UStG exempt |
| 4200 | 8200 | Revenue — reverse charge services | §13b UStG |
| 4400 | 8400 | Other operating income (Sonstige betriebliche Erträge) |  |

### Class 5 & 6: Operating Expenses (Betriebliche Aufwendungen)

**Class 5 & 6: Operating Expenses (Betriebliche Aufwendungen)**

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 5000 | 3000 | Cost of materials / goods purchased (Wareneinkauf) |  |
| 5400 | 3400 | Purchased services (Fremdleistungen) | Subcontractors |
| 6000 | 4000 | Salaries (Löhne und Gehälter) |  |
| 6010 | 4010 | Wages |  |
| 6100 | 4100 | Social security employer share |  |
| 6200 | 4200 | Rent and lease expenses (Miete) |  |
| 6300 | 4300 | Insurance (Versicherungen) |  |
| 6310 | 4360 | Motor vehicle insurance |  |
| 6320 | 4500 | Motor vehicle costs (Kfz-Kosten) | Fuel, repairs, tax |
| 6400 | 4600 | Advertising (Werbekosten) |  |
| 6420 | 4610 | Travel expenses (Reisekosten) |  |
| 6430 | 4620 | Entertainment — deductible portion | 70% deductible, 30% add-back |
| 6440 | 4630 | Entertainment — non-deductible portion | Always add back |
| 6500 | 4800 | Repairs and maintenance (Instandhaltung) |  |
| 6600 | 4900 | Miscellaneous expenses (Sonstige Aufwendungen) |  |
| 6800 | 4830 | Office supplies (Bürobedarf) |  |
| 6805 | 4806 | Telephone and internet (Telekommunikation) |  |
| 6810 | 4921 | Professional fees — accountant |  |
| 6815 | 4925 | Professional fees — legal |  |
| 6820 | 4940 | Bank charges (Bankgebühren) |  |
| 6830 | 4964 | Software subscriptions |  |
| 6850 | 4970 | Training and education (Fortbildung) |  |
| 6220 | 4822 | GWG immediate write-off (under EUR 800) | § 6 Abs. 2 EStG |
| 6221 | 4862 | GWG pool depreciation (EUR 250--1,000) | 5-year pool, 20% p.a. |

### Class 7: Other Income/Expenses (Weitere Erträge und Aufwendungen)

**Class 7: Other Income/Expenses (Weitere Erträge und Aufwendungen)**

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 7000 | 2600 | Interest income (Zinserträge) |  |
| 7100 | 2100 | Interest expense (Zinsaufwand) |  |
| 7200 | 2300 | Exchange gains/losses |  |
| 7300 | 2500 | Extraordinary items | Rare under HGB |
| 7600 | 4830 | Depreciation — fixed assets (AfA Sachanlagen) |  |
| 7610 | 4835 | Depreciation — intangible assets (AfA immaterielle) |  |

### Tax Accounts (Class 7/9)

**Tax Accounts (Class 7/9)**

| SKR04 | SKR03 | Account | Notes |
| --- | --- | --- | --- |
| 7600 | 2200 | Income tax expense (Ertragsteuern) |  |
| 7610 | 2204 | Trade tax expense (Gewerbesteuer) | If applicable |
| 7620 | 2208 | Solidarity surcharge (Solidaritätszuschlag) |  |

## Section 3 -- Revenue Recognition

**Section 3 -- Revenue Recognition**

| Scenario | Treatment |
| --- | --- |
| **Default (HGB § 252)** | Accruals basis — revenue when realised (Realisationsprinzip), expenses when incurred |
| **EÜR (Einnahmen-Überschussrechnung)** | Cash basis — available to Freiberufler and businesses with revenue ≤ EUR 800,000 and profit ≤ EUR 80,000 |
| **Kleinunternehmer (§ 19 UStG)** | No VAT charged; revenue recorded gross. Threshold: prior year ≤ EUR 25,000 AND current year ≤ EUR 100,000 |
| **Advance payments received** | Deferred income (3900) until performance obligation met |
| **Construction contracts** | Percentage-of-completion not permitted under HGB; completed-contract method required |
| **EU cross-border services** | Reverse charge (§ 13b UStG) — no VAT on invoice; buyer accounts for VAT |

### EÜR vs Double-Entry Bookkeeping

**EÜR vs Double-Entry Bookkeeping**

| Criterion | EÜR | Double-Entry (Bilanzierung) |
| --- | --- | --- |
| Who must use | Freiberufler; businesses under thresholds | All Kaufleute registered in Handelsregister; businesses exceeding revenue EUR 800,000 or profit EUR 80,000 |
| Revenue recognition | Cash basis | Accruals basis |
| Balance sheet | Not required | Required (HGB § 242) |
| Filing | Anlage EÜR with Einkommensteuererklärung | Bilanz + GuV + E-Bilanz (electronic submission) |

## Section 4 -- Expense Classification

**Section 4 -- Expense Classification**

| Expense Type | SKR04 | Tax Treatment | Notes |
| --- | --- | --- | --- |
| Office rent | 6200 | Fully deductible |  |
| Home office (Arbeitszimmer) | 6200 | Up to EUR 1,260/year lump sum or proportional costs if dedicated room | Since 2023 |
| Motor vehicle (business) | 6320 | Business % deductible; 1% rule or logbook | Fahrtenbuch recommended |
| Entertainment (business meals) | 6430/6440 | 70% deductible for tax (100% VAT input if > EUR 150 gross) | 30% always non-deductible |
| Gifts to business partners | 6600 | Deductible up to EUR 50 net per person per year | Pauschalversteuerung § 37b EStG applies |
| Travel expenses | 6420 | Fully deductible; per-diem rates (Verpflegungspauschale): EUR 14 (8-24h), EUR 28 (24h+) |  |
| Software subscriptions | 6830 | Fully deductible as operating expense |  |
| Professional fees | 6810/6815 | Fully deductible |  |
| Bank charges | 6820 | Fully deductible |  |
| Training | 6850 | Fully deductible | Must relate to current business |
| Fines and penalties | — | NOT deductible | § 4 Abs. 5 Nr. 8 EStG |
| Private withdrawals (Privatentnahme) | 2100 (SKR04) | NOT deductible | Equity movement |

## Section 5 -- Asset vs Expense Thresholds (GWG Rules)

### GWG (Geringwertige Wirtschaftsgüter) — § 6 Abs. 2/2a EStG

**GWG (Geringwertige Wirtschaftsgüter) — § 6 Abs. 2/2a EStG**  _(§ 6 Abs. 2/2a EStG)_

| Net Value (excl. USt) | Treatment | Recording |
| --- | --- | --- |
| ≤ EUR 250 | Immediate expense; no asset register required | Direct to expense account |
| EUR 250.01 -- EUR 800 | Immediate expense OR depreciate over useful life; asset register required | 6222 / asset account |
| EUR 250.01 -- EUR 1,000 | Alternative: pool depreciation (Sammelposten) over 5 years at 20% p.a. | Must be applied uniformly per year for all assets in range |
| > EUR 1,000 | Capitalise and depreciate over useful life per AfA-Tabelle | Asset accounts (Class 0) |

- **GWG thresholds net of VAT** — The EUR 250 / 800 / 1,000 thresholds are always net of VAT, even for Kleinunternehmer.  _(§ 6 Abs. 2/2a EStG)_

### Standard Depreciation Rates (AfA-Tabelle)

**Standard Depreciation Rates (AfA-Tabelle)**

| Asset Category | Useful Life (Years) | Annual Rate |
| --- | --- | --- |
| Computer hardware | 3 | 33% |
| Computer software (standard) | 3 | 33% |
| Motor vehicles (cars) | 6 | ~17% |
| Motor vehicles (trucks) | 9 | ~11% |
| Office furniture (Büromöbel) | 13 | ~8% |
| Office equipment | 8 | 12.5% |
| Buildings (commercial) | 33 | 3% |
| Buildings (residential, post-2022) | 33 | 3% |
| Telephone systems | 8 | 12.5% |

- **Computers and software useful life simplification** — Since 2021, computers and software have a useful life of 1 year (immediate write-off) per BMF guidance, regardless of cost. This is a tax simplification — for HGB book depreciation, the standard useful life still applies.  _(BMF guidance)_

### Declining Balance Option (2025--2027)

- **Declining balance depreciation option** — For movable fixed assets acquired after 30 June 2025 and before 1 January 2028: up to 30% declining-balance depreciation, capped at 3x the straight-line rate.  _(Declining Balance Option (2025--2027))_

## Section 6 -- P&L Format (GuV — Gewinn- und Verlustrechnung)

HGB § 275 prescribes two formats. The **Gesamtkostenverfahren** (total cost method / nature of expense) is standard for SMEs:

```
GEWINN- UND VERLUSTRECHNUNG (Gesamtkostenverfahren)
Für das Geschäftsjahr [date]

 1. Umsatzerlöse (Revenue)                                   xxx
 2. Erhöhung/Verminderung des Bestands (Inventory changes)   xxx
 3. Andere aktivierte Eigenleistungen                        xxx
 4. Sonstige betriebliche Erträge                            xxx
                                                            -----
    Gesamtleistung                                           xxx

 5. Materialaufwand (Cost of materials)
    a) Roh-, Hilfs- und Betriebsstoffe                      (xxx)
    b) Bezogene Leistungen                                  (xxx)
 6. Personalaufwand (Personnel costs)
    a) Löhne und Gehälter                                   (xxx)
    b) Soziale Abgaben                                      (xxx)
 7. Abschreibungen (Depreciation)                           (xxx)
 8. Sonstige betriebliche Aufwendungen                      (xxx)
                                                            -----
    BETRIEBSERGEBNIS (Operating result)                      xxx

 9. Erträge aus Beteiligungen                                xxx
10. Sonstige Zinsen und Erträge                              xxx
11. Abschreibungen auf Finanzanlagen                        (xxx)
12. Zinsen und ähnliche Aufwendungen                        (xxx)
                                                            -----
    FINANZERGEBNIS                                           xxx
                                                            -----
    ERGEBNIS DER GEWÖHNLICHEN GESCHÄFTSTÄTIGKEIT             xxx

13. Steuern vom Einkommen und Ertrag                        (xxx)
14. Sonstige Steuern                                        (xxx)
                                                            -----
    JAHRESÜBERSCHUSS / JAHRESFEHLBETRAG                      xxx
```

Small companies (Kleinstkapitalgesellschaft) may use a heavily simplified format with just revenue, other income, materials, personnel, depreciation, other expenses, and result.

## Section 7 -- Balance Sheet Format (Bilanz)

HGB § 266 prescribes a two-sided (T-account / horizontal) format for the Bilanz. Small entities may use an abbreviated version.

```
AKTIVA (Assets)                        PASSIVA (Equity & Liabilities)

A. Anlagevermögen (Non-current)        A. Eigenkapital (Equity)
   I.  Immaterielle Vermögensgeg.         I.   Gezeichnetes Kapital
   II. Sachanlagen                        II.  Kapitalrücklage
   III.Finanzanlagen                      III. Gewinnrücklagen
                                          IV.  Gewinn-/Verlustvortrag
B. Umlaufvermögen (Current)               V.   Jahresüberschuss/-fehlbetrag
   I.  Vorräte
   II. Forderungen                     B. Rückstellungen (Provisions)
   III.Wertpapiere
   IV. Kassenbestand, Bankguthaben     C. Verbindlichkeiten (Liabilities)

C. Rechnungsabgrenzungsposten          D. Rechnungsabgrenzungsposten
   (Prepaid expenses)                     (Deferred income)
```

Small companies (§ 267a HGB — Kleinstkapitalgesellschaft): may aggregate line items and need not publish a full balance sheet or prepare notes.

## Section 8 -- Bank Reconciliation Patterns

### German Bank Statement Formats

**German Bank Statement Formats**

| Bank | Format | Standard | Key Fields |
| --- | --- | --- | --- |
| Sparkasse | MT940 / CAMT.053 | ISO 20022 | Buchungsdatum, Betrag, Verwendungszweck |
| Deutsche Bank | MT940 / CSV |  | Wertstellungsdatum, Buchungstext, Betrag |
| Commerzbank | CAMT.053 / CSV | ISO 20022 | Buchungsdatum, Name, Verwendungszweck, Betrag |
| Volksbank/Raiffeisenbank | MT940 / CAMT.053 |  | Buchungstag, Empfänger/Auftraggeber, Betrag |
| N26 / Online banks | CSV | Proprietary | Date, Payee, Amount, Reference |

### Common German Transaction Descriptions

**Common German Transaction Descriptions**

| Pattern | Likely Classification |
| --- | --- |
| GUTSCHRIFT / HABEN | Credit — income or refund |
| LASTSCHRIFT / SOLL | Direct debit — expense |
| DAUERAUFTRAG | Standing order — rent, insurance |
| KARTENZAHLUNG / EC-KARTE | Card payment — check merchant |
| GEHALT / LOHN | Salary payment to employee (6000) |
| FINANZAMT / STEUERZAHLUNG | Tax payment — exclude from P&L |
| MIETE | Rent payment (6200) |
| VERSICHERUNG | Insurance (6300) |
| KRANKENKASSE / SOZIALVERSICHERUNG | Social security contribution (6100) |
| ÜBERTRAG / UMBUCHUNG | Internal transfer — exclude |

### DATEV Import

Most German accountants use DATEV. Bank transactions are imported via DATEV Unternehmen Online or the DATEV CSV format. The mapping from bank categories to SKR03/SKR04 accounts is the core bookkeeping task.

## Section 9 -- Micro-Entity / Small Business Simplifications

### HGB Size Classification (§ 267/267a)

**HGB Size Classification (§ 267/267a)**  _(§ 267/267a HGB)_

| Criterion | Kleinstkapitalgesellschaft | Kleine Kapitalgesellschaft | Mittelgroße | Große |
| --- | --- | --- | --- | --- |
| Balance sheet total | ≤ EUR 450,000 | ≤ EUR 7,500,000 | ≤ EUR 25,000,000 | > EUR 25,000,000 |
| Revenue | ≤ EUR 900,000 | ≤ EUR 15,000,000 | ≤ EUR 50,000,000 | > EUR 50,000,000 |
| Employees | ≤ 10 | ≤ 50 | ≤ 250 | > 250 |

- **Two-of-three criteria requirement** — Must meet 2 of 3 criteria for two consecutive years to qualify for a given category.  _(§ 267/267a HGB)_

### Simplifications by Size

**Simplifications by Size**

| Requirement | Kleinstkapitalgesellschaft | Kleine | Mittelgroße |
| --- | --- | --- | --- |
| Balance sheet | Heavily abbreviated | Abbreviated | Full |
| GuV (P&L) | Simplified (2 lines of expense) | Abbreviated | Full |
| Notes (Anhang) | NOT required | Simplified | Required |
| Management report (Lagebericht) | NOT required | NOT required | Required |
| Audit | NOT required | NOT required | Required |
| Publication | Deposit at Bundesanzeiger | Abbreviated balance sheet only | Full publication |
| E-Bilanz | Required for tax | Required for tax | Required for tax |

### Sole Traders and Freelancers

**Sole Traders and Freelancers**

| Revenue | Profit | Obligation |
| --- | --- | --- |
| ≤ EUR 800,000 | ≤ EUR 80,000 | EÜR (cash-basis simplified accounts) |
| > EUR 800,000 | > EUR 80,000 | Full double-entry bookkeeping + Bilanz |
| Freiberufler (any size) | Any | EÜR permitted regardless of size (unless they opt for Bilanz) |

## Section 10 -- Interaction with Tax Skills

**Section 10 -- Interaction with Tax Skills**

| Tax Skill | How Bookkeeping Connects |
| --- | --- |
| **de-income-tax** | Profit from GuV/EÜR feeds Anlage G (Gewerbe) or Anlage S (Freiberufler) of the Einkommensteuererklärung. Non-deductible items (entertainment 30%, gifts > EUR 50, fines) must be added back. |
| **de-vat-return** | VAT accounts (1400/1406/1600 in SKR04) feed the Umsatzsteuer-Voranmeldung. Monthly or quarterly filing via ELSTER. Input VAT (Vorsteuer) netted against output VAT (Umsatzsteuer). |
| **de-trade-tax** | Gewerbesteuer calculated from adjusted trade profit. Certain add-backs (Hinzurechnungen): 25% of rent, 25% of interest, etc. applied to the commercial profit. |
| **de-crypto-tax** | Crypto disposal gains feed Anlage SO if held < 1 year. Bookkeeping must track acquisition cost (FIFO) per wallet/exchange. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Steuerberater or Wirtschaftsprüfer) before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
