---
name: italy-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Piano dei Conti, financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, or day-to-day accounting for an Italian entity. Trigger on phrases like "piano dei conti", "chart of accounts Italy", "bilancio", "conto economico", "stato patrimoniale", "OIC principles", "Codice Civile accounting", "regime forfettario bookkeeping", "capitalise or expense Italy", "ammortamento", "depreciation Italy", "bank reconciliation Italy", "microimpresa", "bilancio abbreviato", "bookkeeping Italy", or any question about recording transactions, classifying expenses, or preparing accounts under Italian law. ALWAYS read this skill before touching any bookkeeping work for Italy.
version: 2.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-11-14
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: bookkeeping
type: situation-rules
---

# Bookkeeping in Italy: books, registers, accounting basis, chart of accounts and Civil Code formats

Which books an Italian business or professional keeps, registers, retention, cash versus accrual, chart of accounts and Civil Code layouts. Figures are for tax year 2026; Italy's tax year is the calendar year. Statutes were read on Normattiva as in force on 30 June 2026 (the new TUIR, D.Lgs. 117/2026, applies only from 1 January 2027). One source is dated another year: the IRAP rate is from the Agenzia's 2026 IRAP instructions, for 2025. The depreciation decree (D.M. 31 December 1988) was not read, so no rates are printed.


Companion to `it-income-tax`, `italy-vat-return` and `italy-einvoice`.

## Scope

This skill covers the books and registers an Italian business or professional keeps in tax year 2026: which accounting regime applies (forfettario, simplified, ordinary, professional), the registers each needs, cash versus accrual, a working chart of accounts (Piano dei Conti), the Civil Code layouts for the profit and loss account and balance sheet, the tax caps that turn bookkeeping into tax adjustments at year end, and how long records are kept. Italy's tax year is the calendar year; companies may use another 12-month period (TUIR art. 76 and art. 7).

Who is in: sole traders (ditta individuale), partnerships, S.r.l. and S.p.A. that are not listed, and self-employed professionals. Who is out: listed companies, banks, insurers and groups reporting under IFRS (D.Lgs. 38/2005 art. 2), agriculture, non-profit bodies and special IVA schemes. The income tax computation is in `it-income-tax` and `it-ires-corporate-tax`; VAT settlement is in `italy-vat-return`; e-invoices are in `italy-einvoice`; annual accounts are in `italy-financial-statements`.

### Quick reference

**Quick Reference table**

| Field | Value | Source |
| --- | --- |---|
| Financial year | Calendar year for individuals; companies may choose another 12-month period | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art76!vig=2026-06-30 and https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art7!vig=2026-06-30 |
| Accounting standards | OIC principles for non-listed entities (D.Lgs. 38/2005 art. 9-bis); IFRS for listed and other entities named in D.Lgs. 38/2005 art. 2 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-02-28;38~art2!vig=2026-06-30 |
| Record retention | Ten years from the last entry (Civil Code art. 2220), and until the year's tax assessments are final (D.P.R. 600/1973 art. 22). the section "Books, registers and retention" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2220!vig=2026-06-30 |

## Ask the client first

- Company, partnership, sole trader or professional?
- Revenue actually received last year, and is the main activity services or other?
- Forfettario, or an option for ordinary accounts (and when)?
- IVA registers with cash notes, or the registration-date option?
- Stock and depreciable assets held, with dates and costs?
- Companies: total assets, revenue and average staff for the last two years.

## The method, step by step

1. **Pick the regime**: company, ordinary; sole trader or partnership, simplified if last year's revenue is within the limits, unless it opts out (D.P.R. 600/1973 art. 18, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art18!vig=); forfettario if its conditions are met (https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/semplificazioni-e-adempimenti).
2. **Open the books** for that regime (see the section "Books, registers and retention"; D.P.R. 600/1973 art. 14, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art14!vig=2026-06-30).
3. **Record IVA documents on time** (D.P.R. 633/1972 art. 23, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art23!vig=2026-06-30).
4. **Year end**: apply the the section "Expense Classification" caps, update the asset register (D.P.R. 600/1973 art. 16, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art16!vig=2026-06-30), sign the inventory (Civil Code art. 2217, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2217!vig=2026-06-30).
5. **Prepare the financial statements** in the art. 2424 and 2425 schemes, then keep everything for the art. 2220 period (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2220!vig=2026-06-30).

### Rates, bands and thresholds

| Item | Figure | Tax year | Source |
| --- | --- | --- | --- |
| Forfettario: prior-year revenue or fees, annualised, not above | EUR 85,000 | 2026 | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- |
| Forfettario substitute tax (start-up rate 5% for the first five years if the conditions are met) | 15% | 2026 | same |
| Simplified accounts: prior-year revenue, service businesses, not above | EUR 500,000 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art18!vig= |
| Simplified accounts: prior-year revenue, other businesses, not above | EUR 800,000 | 2026 | same |
| Business asset deductible in full in year one, unit cost not above | EUR 516.46 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art102!vig=2026-06-30 |
| Telephone equipment and services, deductible share | 80% | 2026 | same |
| Professional's asset deductible in full, unit cost not above | EUR 516.40 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30 |
| Hotels, food and drink, deductible share | 75% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art109!vig=2026-06-30 |
| Entertainment cap, revenue up to EUR 10 million / part to EUR 50 million / part above | 1.5% / 0.6% / 0.4% of revenue | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art108!vig=2026-06-30 |
| Cars not used only for the business / agents / cars given to staff for mixed use | 20% / 80% / 70% deductible | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art164!vig=2026-06-30 |
| Net interest deductible up to this share of the risultato operativo lordo | 30% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art96!vig=2026-06-30 |
| IRES rate | 24% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig=2026-06-30 |
| Micro company (art. 2435-ter): total assets / revenue / average staff, not above two of | EUR 220,000 / EUR 440,000 / 5 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435ter!vig= |
| Abbreviated accounts (art. 2435-bis): total assets / revenue / average staff, not above two of | EUR 5,500,000 / EUR 11,000,000 / 50 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435bis!vig= |
| Retention of books, invoices and letters | 10 years from the last entry | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2220!vig=2026-06-30 |

IRAP is not restated here: its rate and base are in `it-irap`.

### Recommended Chart of Accounts (Piano dei Conti)

OpenAccountants' own suggestion, not an official chart; checked against Civil Code art. 2424 and 2425.

#### Assets (1xxx): Stato Patrimoniale, Attivo

| Code | Account | CC Art. 2424 Reference |
| --- | --- | --- |
| 1000 | Immobilizzazioni immateriali | B.I |
| 1010 | Software (opere dell'ingegno) | B.I.3 |
| 1015 | Concessioni, licenze, marchi | B.I.4 |
| 1020 | Avviamento | B.I.5 |
| 1030 | Immateriali in corso | B.I.6 |
| 1110 | Terreni e fabbricati | B.II.1 |
| 1120 | Impianti e macchinari | B.II.2 |
| 1130 | Attrezzature industriali e commerciali | B.II.3 |
| 1140 | Macchine d'ufficio, computer, mobili, automezzi | B.II.4 |
| 1170 | Materiali in corso | B.II.5 |
| 1199 | Fondi ammortamento | Contra-asset |
| 1210 | Partecipazioni | B.III.1 |
| 1220 | Crediti (long-term) | B.III.2 |
| 1310 | Materie prime | C.I.1 |
| 1320 | Prodotti finiti e merci | C.I.4 |
| 1400 | Crediti verso clienti | C.II.1 |
| 1410 | Crediti tributari | C.II.5-bis |
| 1420 | IVA a credito | C.II.5-bis |
| 1430 | Crediti verso altri | C.II.5-quater |
| 1440 | Ratei e risconti attivi | D |
| 1500 | Banca c/c and c/deposito | C.IV.1 |
| 1510 | Cassa | C.IV.3 |

#### Liabilities (2xxx): Stato Patrimoniale, Passivo

| Code | Account | CC Art. 2424 Reference |
| --- | --- | --- |
| 2000 | Fondi per rischi e oneri | B |
| 2010 | TFR | C |
| 2100 | Debiti verso banche | D.4 |
| 2200 | Debiti verso fornitori | D.7 |
| 2210 | Debiti tributari | D.12 |
| 2220 | IVA a debito | D.12 |
| 2230 | Debiti vs istituti previdenziali | D.13 |
| 2240 | Altri debiti | D.14 |
| 2300 | Ratei e risconti passivi | E |

#### Equity (3xxx): Patrimonio Netto

| Code | Account | CC Art. 2424 Reference |
| --- | --- | --- |
| 3000 | Capitale sociale | A.I |
| 3010 | Riserva legale | A.IV |
| 3020 | Altre riserve | A.VI |
| 3100 | Utili (perdite) portati a nuovo | A.VIII |
| 3200 | Utile (perdita) dell'esercizio | A.IX |

#### Revenue (4xxx): Conto Economico, Valore della Produzione (A)

| Code | Account | CC Art. 2425 Reference |
| --- | --- | --- |
| 4000 | Ricavi delle vendite e delle prestazioni | A.1 |
| 4010 | Variazioni rimanenze prodotti | A.2/3 |
| 4020 | Incrementi immobilizzazioni per lavori interni | A.4 |
| 4100 | Altri ricavi e proventi | A.5 |
| 4110 | Contributi in conto esercizio | A.5 (shown separately) |

#### Cost of Production (5xxx): Conto Economico, Costi della Produzione (B)

| Code | Account | CC Art. 2425 Reference |
| --- | --- | --- |
| 5000 | Acquisti materie prime e merci | B.6 |
| 5100 | Servizi: consulenze, utenze, manutenzioni, assicurazioni, pubblicità, trasporti, telefono, spese bancarie (sub-accounts 5110 to 5180) | B.7 |
| 5200 | Godimento beni di terzi | B.8 |
| 5300 | Salari e stipendi | B.9.a |
| 5310 | Oneri sociali | B.9.b |
| 5320 | TFR dell'esercizio | B.9.c |
| 5400 | Ammortamento immateriali | B.10.a |
| 5410 | Ammortamento materiali | B.10.b |
| 5420 | Svalutazione crediti | B.10.d |
| 5500 | Variazione rimanenze materie prime | B.11 |
| 5600 | Accantonamenti per rischi | B.12 |
| 5700 | Altri accantonamenti | B.13 |
| 5800 | Oneri diversi di gestione | B.14 |

#### Financial Income/Expenses (6xxx): Conto Economico: C & D

| Code | Account | CC Art. 2425 Reference |
| --- | --- | --- |
| 6000 | Proventi da partecipazioni | C.15 |
| 6100 | Interessi attivi | C.16 |
| 6200 | Interessi passivi | C.17 |
| 6300 | Utili/perdite su cambi | C.17-bis |
| 6400 | Rivalutazioni | D.18 |
| 6500 | Svalutazioni | D.19 |

#### Tax (7xxx)

**IRES rate**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig= |  |
| IRES, standard rate | 24% | "con l'aliquota del 24 per cento" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig= |

**IRAP ordinary rate**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |  |
| IRAP, ordinary rate (regions may vary it; some sectors pay more) | 3.9% | "l’aliquota del 3,9 per cento" | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |

**Tax chart of accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 7000 | IRES dell'esercizio | Rate in the IRES table |
| 7010 | IRAP dell'esercizio | Rate in the IRAP table; see `it-irap` |
| 7020 | Imposte differite e anticipate | Art. 2425 item 20 |
| 7030 | Acconti d'imposta | Credit against the tax liability |

### Revenue Recognition

**Revenue recognition scenarios**

| Scenario | Treatment |
| --- | --- |
| **Default (ordinary accounts)** | Accruals basis (competenza) |
| **Regime forfettario** | No accounting records for income tax (see the section "Books, registers and retention"); income = revenue received times the sector coefficient (`it-income-tax`) |
| **Regime ordinario** | Accruals, double entry |
| **Regime semplificato** | Revenue received less expenses paid in the year, plus some accrual items (TUIR art. 66(1)) |
| **Professionals** | Cash basis: fees received less costs paid (TUIR art. 54(1)); see `it-income-tax` |
| **IVA on sales** | Revenue net of IVA; IVA to 2220 |
| **Advance payments** | Risconti passivi (2300) until delivery |

#### Tax Regimes for Individuals/Small Businesses

**Forfettario**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- |  |
| Prior-year revenue or fees, annualised, not above | EUR 85,000 | "non superiori a 85.000 euro" | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- |
| Substitute tax | 15% | "nella misura del 15%" | same |
| Start-up rate, first five years, if conditions met | 5% | "ridotta al 5% per i primi cinque anni" | same |

**Simplified accounts limits**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art18!vig= |  |
| Revenue in a full year, service businesses, not above | EUR 500,000 | "non abbiano superato l'ammontare di 500.000 euro per le imprese aventi per oggetto prestazioni di servizi" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art18!vig= |
| Revenue in a full year, other businesses, not above | EUR 800,000 | "ovvero di 800.000 euro per le imprese aventi per oggetto altre attività" | same |

- **Semplificata is decided on last year's revenue received** (for a business leaving ordinary accounts, on that year's accrued revenue). Sole traders and partnerships (D.P.R. 600/1973 art. 13 letters c and d) within the limit keep simplified books the next year. Mixed businesses use the limit of the main activity; without separate records they count as "other activities" (art. 18(1)). It rolls over while the limits are not exceeded (art. 18(7)); a new business may use it in year one if expected annualised revenue is within the limit (art. 18(9)).
- **Companies always keep ordinary accounts**: art. 18 covers only letters c and d.

### Expense Classification

Business income (reddito d'impresa). Professionals follow TUIR art. 54 to 54-octies (`it-income-tax`).

**TUIR art. 102**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art102!vig=2026-06-30 |  |
| Telephone equipment and services, deductible share | 80% | "sono deducibili nella misura dell' 80 per cento" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art102!vig=2026-06-30 |
| Asset unit cost deductible in full in year one | EUR 516.46 | "non è superiore a 516,46 euro" | same |

**TUIR art. 109(5)**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art109!vig=2026-06-30 |  |
| Hotel services and food and drink, deductible share (not employees' business trips under art. 95(3)) | 75% | "sono deducibili nella misura del 75 per cento" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art109!vig=2026-06-30 |

**TUIR art. 108(2), entertainment cap as a share of revenue**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art108!vig=2026-06-30 |  |
| Revenue up to 10 million euro | 1.5% | "all'1,5 per cento dei ricavi e altri proventi fino a euro 10 milioni" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art108!vig=2026-06-30 |
| Part over 10 and up to 50 million euro | 0.6% | "allo 0,6 per cento dei ricavi e altri proventi per la parte eccedente" | same |
| Part over 50 million euro | 0.4% | "allo 0,4 per cento dei ricavi e altri proventi per la parte eccedente euro 50 milioni" | same |

**TUIR art. 164, cars**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art164!vig=2026-06-30 |  |
| Cars not used exclusively as business assets | 20% | "nella misura del 20 per cento relativamente alle autovetture" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art164!vig=2026-06-30 |
| Agents and commercial representatives | 80% | "Tale percentuale è elevata all'80 per cento" | same |
| Cars given to employees for mixed use for most of the tax period | 70% | "nella misura del 70 per cento per i veicoli dati in uso promiscuo ai dipendenti per la maggior parte del periodo d'imposta" | same |

The share applies only to the part of the purchase cost, lease or hire charge within the limits in art. 164, which the statute still prints in lire. Professionals working alone may deduct costs for one vehicle only.

**TUIR art. 96, interest**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art96!vig=2026-06-30 |  |
| Net interest deductible up to this share of the risultato operativo lordo | 30% | "il 30 per cento del risultato operativo lordo della gestione caratteristica" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art96!vig=2026-06-30 |

**Expense classification table**

| Expense Type | Code | Tax Deductibility |
| --- | --- | --- |
| Rent, utilities, fees, insurance, advertising, bank charges | 5200, 5100 | Fully deductible; apportion mixed use |
| Travel and accommodation | 5100 | Hotels and meals at the art. 109 share, except employees' business trips, which follow art. 95(3). Costs incurred in Italy (meals, lodging, taxi) are deductible only if paid by bank or postal transfer or another traceable method (art. 109(5-bis)) |
| Entertainment | 5800 | Within the art. 108 caps, and only if paid by bank or postal transfer or another traceable method (art. 108(2)) |
| Telephone | 5170 | Art. 102 share |
| Motor vehicle costs and fuel | 5100 | Art. 164 shares; agents at the higher share. |
| Interest expense | 6200 | Art. 96 limit (companies) |
| Fines and penalties | 5800 | NOT deductible |
| Depreciation | 5400/5410 | Up to the ministerial coefficients, halved in year one (art. 102(2)) |

### Asset vs Expense Thresholds

#### Capitalisation Rules

**Capitalisation rules table**

| Rule | Treatment |
| --- | --- |
| **Small assets, businesses** | Unit cost up to the art. 102(5) amount in the section "Expense Classification": deductible in full in the year bought |
| **Small assets, professionals** | Separate limit, table below |
| **Forfettario** | No depreciation; the coefficient covers costs |
| **Tax** | First-year depreciation at half the coefficient (art. 102(2)) |

**TUIR art. 54-quinquies**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30 |  |
| Professional: asset unit cost deductible in full | EUR 516.40 | "il cui costo unitario non sia superiore a euro 516,40" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30 |

#### Depreciation Rates (DM 31 December 1988: Coefficienti di Ammortamento)

Rates come from the decree by sector and asset group, halved in year one (TUIR art. 102(2)). The decree was not read, so no rates are given; refer.

- **Depreciation method** : straight-line within the coefficient. Accelerated depreciation (former art. 102(3)) was repealed by L. 244/2007. Any super-ammortamento is a separate law; check it first.

### P&L Format (Conto Economico)

Art. 2425 Codice Civile, for years starting from 1 January 2016 (D.Lgs. 139/2015), costs by nature. Current wording, including the derivatives lines:

~~~
A) VALORE DELLA PRODUZIONE: items 1 to 5. Totale
B) COSTI DELLA PRODUZIONE: items 6 to 14 (9 personale a to e;
   10 ammortamenti e svalutazioni a to d). Totale
Differenza tra valore e costi della produzione (A - B)
C) PROVENTI E ONERI FINANZIARI: 15, 16, 17, 17-bis
D) RETTIFICHE DI VALORE DI ATTIVITA E PASSIVITA FINANZIARIE:
   18 rivalutazioni, 19 svalutazioni (each with d strumenti derivati)
Risultato prima delle imposte (A - B +/- C +/- D)
20 imposte sul reddito dell'esercizio, correnti, differite e anticipate
21 utile (perdite) dell'esercizio
~~~

### Balance Sheet Format (Stato Patrimoniale)

Art. 2424 Codice Civile, main headings:

~~~
ATTIVO: A crediti verso soci; B immobilizzazioni (I immateriali,
  II materiali, III finanziarie); C attivo circolante (I rimanenze,
  II crediti, III attivita finanziarie, IV disponibilita liquide);
  D ratei e risconti
PASSIVO: A patrimonio netto (I capitale, II sovrapprezzo, III rivalutazione,
  IV legale, V statutarie, VI altre riserve, VII copertura flussi,
  VIII utili portati a nuovo, IX utile dell'esercizio, X azioni proprie);
  B fondi rischi e oneri; C TFR; D debiti; E ratei e risconti
~~~

### Bank Reconciliation Patterns

#### Italian Bank Statement Formats

**Bank statement formats table** (OpenAccountants' observation, not an official source)

| Bank | Format | Key Fields |
| --- | --- | --- |
| Intesa Sanpaolo, Banco BPM, BPER Banca | CBI, CSV | Data operazione, Descrizione, Importo |
| UniCredit | CBI, CSV, MT940 | Data contabile, Causale, Dare, Avere |
| Poste Italiane, Revolut, N26 | PDF, CSV | Date, description, amount |

#### Common Italian Transaction Descriptions

**Transaction descriptions table**

| Pattern | Likely Classification |
| --- | --- |
| BONIFICO / BON | Transfer: income or expense |
| ADDEBITO SDD / RID | Direct debit: utility, insurance |
| POS / CARTA | Card: check merchant |
| F24 / DELEGA UNICA | Tax payment: exclude from P&L |
| INPS / CONTRIBUTI | Contributions (5310) |
| CANONE / AFFITTO | Rent (5200) |
| RATA MUTUO | Split capital (2100) and interest (6200) |
| GIROCONTO | Internal transfer: exclude |

#### Fatturazione Elettronica (E-Invoicing)

Who must e-invoice through the SdI, and from when, forfettari included, is in `italy-einvoice`. Match bank lines to the SdI XML invoices.

### Micro-Entity / Small Business Simplifications

#### Codice Civile Size Thresholds (updated by D.Lgs. 125/2024)

The first year the raised limits apply is not settled: D.Lgs. 125/2024 art. 17 names no start year for small companies that are not listed. Test the company against both the raised and the earlier limits, as `italy-financial-statements` explains, and get advice if the results differ.

**Art. 2435-ter (micro)**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435ter!vig= |  |
| Total assets | EUR 220,000 | "220.000 euro" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435ter!vig= |
| Revenue | EUR 440,000 | "440.000 euro" | same |
| Average employees | 5 | "5 unità" | same |

**Art. 2435-bis (abbreviated)**

| What | Value | Note | Source |
| --- | --- | --- |---|
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435bis!vig= |  |
| Total assets | EUR 5,500,000 | "5.500.000 euro" | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435bis!vig= |
| Revenue | EUR 11,000,000 | "11.000.000 euro" | same |
| Average employees | 50 | "50 unità" | same |

**Size thresholds table**

| Criterion | Microimpresa | Bilancio abbreviato | Bilancio ordinario |
| --- | --- | --- | --- |
| Total assets | Up to EUR 220,000 | Up to EUR 5,500,000 | Above EUR 5,500,000 |
| Revenue | Up to EUR 440,000 | Up to EUR 11,000,000 | Above EUR 11,000,000 |
| Average employees | Up to 5 | Up to 50 | Above 50 |

- **Two-of-three criteria rule** : in the first year, or afterwards for two consecutive years, not exceeding two of the three limits ("per due esercizi consecutivi, non abbiano superato due dei seguenti limiti", art. 2435-bis).

#### Simplifications by Size

**Simplifications by size table**

| Requirement | Microimpresa | Bilancio abbreviato | Bilancio ordinario |
| --- | --- | --- | --- |
| Stato patrimoniale, conto economico | Abbreviated | Abbreviated | Full |
| Nota integrativa | Exempt if key information is at the foot of the balance sheet | Simplified | Full |
| Relazione sulla gestione | Exempt on the same condition | Exempt if the information is in the nota integrativa | Required |
| Rendiconto finanziario | Exempt | Exempt | Required |

#### Individual Tax Regimes

**Individual tax regimes table**

| Regime | Who Qualifies | Bookkeeping Obligation |
| --- | --- | --- |
| Forfettario | the section "Revenue Recognition" table | None for income tax; keep purchase invoices (see the section "Books, registers and retention") |
| Semplificato | the section "Revenue Recognition" table | Receipts and payments registers (see the section "Books, registers and retention") |
| Ordinario | Companies, above the limits, or by option | Full books (see the section "Books, registers and retention") |
| Professional | Arts and professions | Register of fees and expenses (see the section "Books, registers and retention") |

### Interaction with Tax Guides

**Interaction with tax Guides table**

| Tax Guide | How Bookkeeping Connects |
| --- | --- |
| **`it-income-tax`** | Professionals and forfettari |
| **IRES (companies)** | Risultato dell'esercizio is the start;  the section "Expense Classification" caps create permanent differences |
| **`italy-vat-return`** | 1420 and 2220 feed the liquidazione and the LIPE |
| **`it-irap`** | Base starts from the Differenza A-B |
| **`it-inps-contributions`** | Account 5310; self-employed contributions |

### Books, registers and retention

- **Ordinary accounts.** Libro giornale, day by day (Civil Code art. 2216); libro degli inventari (art. 2214); IVA registers; auxiliary records by category; stock records where required; registro dei beni ammortizzabili; company books of art. 2421 (D.P.R. 600/1973 art. 14).
- **Inventory.** At the start and every year, closed by the balance sheet and profit and loss account, signed within three months of the income tax return deadline (Civil Code art. 2217; D.P.R. 600/1973 art. 15).
- **Registro dei beni ammortizzabili.** By the return deadline: year bought, cost, revaluations, accumulated depreciation, coefficient, the year's charge, disposals (art. 16). Under simplified accounts depreciation is deductible only if it is kept (TUIR art. 66(2)).
- **Simplified accounts.** A register of revenue received and a separate register of expenses paid, in date order, with amount, counterparty and invoice reference (art. 18(2)). IVA registers can replace them if non-IVA items are noted separately; unpaid invoices are listed at year end and entered when settled (art. 18(4)). A three-year option lets IVA registers stand alone, with registration presumed to be payment (art. 18(5)). The ordinary-accounts option binds for that year and the next two (art. 18(8)).
- **Professionals.** One chronological register of sums received (gross, net, withholding suffered, payer, invoice) and deductible expenses; depreciable assets entered by the return deadline (art. 19).
- **Forfettari.** "esonerati dagli obblighi di registrazione e tenuta delle scritture contabili", but still keep registers required by non-tax laws, and number and keep purchase invoices and customs bills (Agenzia "Semplificazioni e adempimenti" page).
- **IVA registers.** Sales invoices in number order by the 15th of the month after the operation (D.P.R. 633/1972 art. 23); purchases before the settlement that deducts them and by the annual return deadline (art. 25); numbered pages under Civil Code art. 2219 (art. 39).
- **Form, timing, retention.** Tax books numbered page by page; chronological and stock entries within sixty days (D.P.R. 600/1973 art. 22). Keep ten years from the last entry, with invoices and letters, image copies allowed if always legible (Civil Code art. 2220); for tax, until the year's assessments are final, even beyond (D.P.R. 600/1973 art. 22); e-invoices stored electronically (D.P.R. 633/1972 art. 39). Same rule as `italy-einvoice`.

## Worked cases

### Case 1 (decision): simplified or ordinary accounts for 2026?

Facts. Two clients start 2026. Bianchi, a sole trader running an IT services business, received EUR 480,000 of revenue in 2025. Rossi & C. s.n.c., a partnership selling furniture, received EUR 820,000 in 2025. Neither has opted for ordinary accounts.

Rule. Sole traders and partnerships keep simplified accounts in the next year if last year's revenue did not exceed EUR 500,000 for services or EUR 800,000 for other activities (D.P.R. 600/1973 art. 18). The headroom below the limit decides it: positive means simplified, negative means ordinary.

Answer. Bianchi has EUR 20,000 of headroom, so simplified accounts (receipts and payments registers) for 2026. Rossi is EUR 20,000 over, so ordinary accounts (libro giornale, libro degli inventari) from 1 January 2026. Neither can use the forfettario: both are far above EUR 85,000.

```oa-check
name: Italy 2026, simplified accounts test for a services and a trading business
inputs:
  revenue_services: 480000
  revenue_trading: 820000
  limit_services: 500000
  limit_other: 800000
  limit_forfettario: 85000
steps:
  - headroom_services: limit_services - revenue_services
  - headroom_trading: limit_other - revenue_trading
  - forfettario_gap_services: revenue_services - limit_forfettario
expected:
  headroom_services: 20000.00
  headroom_trading: -20000.00
  forfettario_gap_services: 395000.00
```

### Case 2: year-end tax adjustments from the books

Facts. Alfa S.r.l. has 2026 revenue of EUR 2,000,000. Its books show entertainment EUR 40,000 (paid by bank transfer), fuel and running costs for a car not used only for the business EUR 10,000, hotels and meals EUR 4,000 and telephone EUR 1,500.

Working. Entertainment is deductible up to 1.5% of revenue up to EUR 10 million: EUR 30,000, so EUR 10,000 is added back (art. 108). Car running costs are deductible at 20%: EUR 2,000, EUR 8,000 added back (art. 164; the cost limits of art. 164 apply only to purchase, lease and hire). Hotels and meals at 75%: EUR 3,000, EUR 1,000 added back (art. 109). Telephone at 80%: EUR 1,200, EUR 300 added back (art. 102). Total add-back to the accounting profit: EUR 19,300, which costs EUR 4,632 of IRES at 24%.

```oa-check
name: Italy 2026, year-end add-backs for entertainment, car, hotels and phone
inputs:
  revenue: 2000000
  entertainment: 40000
  car_costs: 10000
  hotels_meals: 4000
  phone: 1500
  ires_rate: 0.24
steps:
  - ent_cap: min(revenue, 10000000) * 0.015
  - ent_addback: max(entertainment - ent_cap, 0)
  - car_addback: car_costs - car_costs * 0.20
  - hotel_addback: hotels_meals - hotels_meals * 0.75
  - phone_addback: phone - phone * 0.80
  - total_addback: ent_addback + car_addback + hotel_addback + phone_addback
  - extra_ires: total_addback * ires_rate
expected:
  ent_cap: 30000.00
  ent_addback: 10000.00
  car_addback: 8000.00
  total_addback: 19300.00
  extra_ires: 4632.00
```

## When to refuse or refer

- Listed companies, groups, banks, insurers, IFRS: outside this Guide.
- Audit limits and the first year of the raised size limits: not verified; refer.
- Sector depreciation rates: decree not read; refer.
- Tax audits, missing or destroyed books: refer to a commercialista.
- Agriculture, non-profit bodies, special IVA schemes: outside this Guide.

## Sources

Every page below was opened on 2026-11-14 and the figures this skill takes from it were found in the text.

| Source | URL | Read on |
| --- | --- | --- |
| Civil Code (art. 2214 to 2220, 2424, 2425, 2435-bis, 2435-ter). Read for books, inventory, retention (arts 2214 to 2220) and the layouts (arts 2424, 2425) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2220!vig=2026-06-30 | 2026-11-14 |
| D.P.R. 600/1973 (art. 14 to 22). Read for the books of arts 14 to 22, the 60-day entry rule and retention for tax | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art22!vig=2026-06-30 | 2026-11-14 |
| D.P.R. 633/1972 (art. 23, 25, 39). Read for IVA registers (arts 23, 25) and electronic storage (art. 39) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art39!vig=2026-06-30 | 2026-11-14 |
| TUIR (art. 54-quinquies, 66, 77, 96, 102, 108, 109, 164). Read for art. 66, simplified business income | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art66!vig=2026-06-30 | 2026-11-14 |
| Agenzia, forfettario. Read for the EUR 85,000 limit, the 15% and 5% rates and the bookkeeping exemption | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- | 2026-11-14 |
| TUIR art. 76. Read for the company tax period | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art76!vig=2026-06-30 | 2026-11-14 |
| TUIR art. 7. Read for the individual tax year | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art7!vig=2026-06-30 | 2026-11-14 |
| TUIR art. 77. Read for the individual tax year | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig= | 2026-11-14 |
| IRAP 2026 instructions. Read for the 3.9% ordinary IRAP rate | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 | 2026-11-14 |
| D.P.R. 600/1973 art. 18. Read for the EUR 500,000 and EUR 800,000 simplified accounts limits | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art18!vig= | 2026-11-14 |
| TUIR art. 102. Read for the EUR 516.46 small-asset rule, the 80% telephone share and half depreciation in year one | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art102!vig=2026-06-30 | 2026-11-14 |
| TUIR art. 109. Read for the 75% hotels and meals share and the traceable payment rule | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art109!vig=2026-06-30 | 2026-11-14 |
| TUIR art. 108. Read for the entertainment caps 1.5%, 0.6% and 0.4% | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art108!vig=2026-06-30 | 2026-11-14 |
| TUIR art. 164. Read for the 20%, 80% and 70% car shares | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art164!vig=2026-06-30 | 2026-11-14 |
| TUIR art. 96. Read for the 30% interest limit | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art96!vig=2026-06-30 | 2026-11-14 |
| TUIR art. 54-quinquies. Read for the EUR 516.40 professional small-asset rule | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30 | 2026-11-14 |
| Civil Code art. 2435-ter. Read for the micro company limits | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435ter!vig= | 2026-11-14 |
| Civil Code art. 2435-bis. Read for the abbreviated accounts limits | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435bis!vig= | 2026-11-14 |
| D.Lgs. 38/2005 art. 2. Read for which companies must use IFRS | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-02-28;38~art2!vig=2026-06-30 | 2026-11-14 |
| D.Lgs. 38/2005 art. 9-bis. Read for the OIC as the body that issues the national accounting principles | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-02-28;38~art9bis!vig=2026-06-30 | 2026-11-14 |

Not yet confirmed: that no chart of accounts is mandated (no source states it; the chart below is a working layout only); the sector depreciation coefficients (D.M. 31 December 1988, not read).

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista or revisore legale) before filing or acting upon.

> Contributed by OpenAccountants.
