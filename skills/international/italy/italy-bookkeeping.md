---
name: italy-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Piano dei Conti, financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, or day-to-day accounting for an Italian entity. Trigger on phrases like "piano dei conti", "chart of accounts Italy", "bilancio", "conto economico", "stato patrimoniale", "OIC principles", "Codice Civile accounting", "regime forfettario bookkeeping", "capitalise or expense Italy", "ammortamento", "depreciation Italy", "bank reconciliation Italy", "microimpresa", "bilancio abbreviato", "bookkeeping Italy", or any question about recording transactions, classifying expenses, or preparing accounts under Italian law. ALWAYS read this skill before touching any bookkeeping work for Italy.
version: 1.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bookkeeping in Italy: books, registers, accounting basis, chart of accounts and Civil Code formats

Which books an Italian business or professional keeps, registers, retention, cash versus accrual, chart of accounts and Civil Code layouts. Figures are for tax year 2026; Italy's tax year is the calendar year. Statutes were read on Normattiva as in force on 30 June 2026 (the new TUIR, D.Lgs. 117/2026, applies only from 1 January 2027). One source is dated another year: the IRAP rate is from the Agenzia's 2026 IRAP instructions, for 2025. The depreciation decree (D.M. 31 December 1988) was not read, so no rates are printed.

## Italy Bookkeeping Guide v1.0

Companion to `it-income-tax`, `italy-vat-return` and `italy-einvoice`.

## Section 1: Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Currency | EUR |
| Financial year | Calendar year for individuals; companies may choose another 12-month period |
| Accounting standards | OIC principles for non-listed entities; IFRS for listed entities |
| Standard chart of accounts | None mandated |
| Record retention | Ten years from the last entry (Civil Code art. 2220), and until the year's tax assessments are final (D.P.R. 600/1973 art. 22). Section 11 |

## Section 2: Recommended Chart of Accounts (Piano dei Conti)

OpenAccountants' own suggestion, not an official chart; checked against Civil Code art. 2424 and 2425.

### Assets (1xxx): Stato Patrimoniale, Attivo

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

### Liabilities (2xxx): Stato Patrimoniale, Passivo

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

### Equity (3xxx): Patrimonio Netto

| Code | Account | CC Art. 2424 Reference |
| --- | --- | --- |
| 3000 | Capitale sociale | A.I |
| 3010 | Riserva legale | A.IV |
| 3020 | Altre riserve | A.VI |
| 3100 | Utili (perdite) portati a nuovo | A.VIII |
| 3200 | Utile (perdita) dell'esercizio | A.IX |

### Revenue (4xxx): Conto Economico, Valore della Produzione (A)

| Code | Account | CC Art. 2425 Reference |
| --- | --- | --- |
| 4000 | Ricavi delle vendite e delle prestazioni | A.1 |
| 4010 | Variazioni rimanenze prodotti | A.2/3 |
| 4020 | Incrementi immobilizzazioni per lavori interni | A.4 |
| 4100 | Altri ricavi e proventi | A.5 |
| 4110 | Contributi in conto esercizio | A.5 (shown separately) |

### Cost of Production (5xxx): Conto Economico, Costi della Produzione (B)

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

### Financial Income/Expenses (6xxx): Conto Economico: C & D

| Code | Account | CC Art. 2425 Reference |
| --- | --- | --- |
| 6000 | Proventi da partecipazioni | C.15 |
| 6100 | Interessi attivi | C.16 |
| 6200 | Interessi passivi | C.17 |
| 6300 | Utili/perdite su cambi | C.17-bis |
| 6400 | Rivalutazioni | D.18 |
| 6500 | Svalutazioni | D.19 |

### Tax (7xxx)

**IRES rate**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig= |
| IRES, standard rate | 24% | "con l'aliquota del 24 per cento" |

**IRAP ordinary rate**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |
| IRAP, ordinary rate (regions may vary it; some sectors pay more) | 3.9% | "l’aliquota del 3,9 per cento" |

**Tax chart of accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 7000 | IRES dell'esercizio | Rate in the IRES table |
| 7010 | IRAP dell'esercizio | Rate in the IRAP table; see `it-irap` |
| 7020 | Imposte differite e anticipate | Art. 2425 item 20 |
| 7030 | Acconti d'imposta | Credit against the tax liability |

## Section 3: Revenue Recognition

**Revenue recognition scenarios**

| Scenario | Treatment |
| --- | --- |
| **Default (ordinary accounts)** | Accruals basis (competenza) |
| **Regime forfettario** | No accounting records for income tax (Section 11); income = revenue received times the sector coefficient (`it-income-tax`) |
| **Regime ordinario** | Accruals, double entry |
| **Regime semplificato** | Revenue received less expenses paid in the year, plus some accrual items (TUIR art. 66(1)) |
| **Professionals** | Cash basis: fees received less costs paid (TUIR art. 54(1)); see `it-income-tax` |
| **IVA on sales** | Revenue net of IVA; IVA to 2220 |
| **Advance payments** | Risconti passivi (2300) until delivery |

### Tax Regimes for Individuals/Small Businesses

**Forfettario**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020- |
| Prior-year revenue or fees, annualised, not above | EUR 85,000 | "non superiori a 85.000 euro" |
| Substitute tax | 15% | "nella misura del 15%" |
| Start-up rate, first five years, if conditions met | 5% | "ridotta al 5% per i primi cinque anni" |

**Simplified accounts limits**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art18!vig= |
| Revenue in a full year, service businesses, not above | EUR 500,000 | "non abbiano superato l'ammontare di 500.000 euro per le imprese aventi per oggetto prestazioni di servizi" |
| Revenue in a full year, other businesses, not above | EUR 800,000 | "ovvero di 800.000 euro per le imprese aventi per oggetto altre attività" |

- **Semplificata is decided on last year's revenue received** (for a business leaving ordinary accounts, on that year's accrued revenue). Sole traders and partnerships (D.P.R. 600/1973 art. 13 letters c and d) within the limit keep simplified books the next year. Mixed businesses use the limit of the main activity; without separate records they count as "other activities" (art. 18(1)). It rolls over while the limits are not exceeded (art. 18(7)); a new business may use it in year one if expected annualised revenue is within the limit (art. 18(9)).
- **Companies always keep ordinary accounts**: art. 18 covers only letters c and d.

## Section 4: Expense Classification

Business income (reddito d'impresa). Professionals follow TUIR art. 54 to 54-octies (`it-income-tax`).

**TUIR art. 102**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art102!vig=2026-06-30 |
| Telephone equipment and services, deductible share | 80% | "sono deducibili nella misura dell' 80 per cento" |
| Asset unit cost deductible in full in year one | EUR 516.46 | "non è superiore a 516,46 euro" |

**TUIR art. 109(5)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art109!vig=2026-06-30 |
| Hotel services and food and drink, deductible share (not employees' business trips under art. 95(3)) | 75% | "sono deducibili nella misura del 75 per cento" |

**TUIR art. 108(2), entertainment cap as a share of revenue**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art108!vig=2026-06-30 |
| Revenue up to 10 million euro | 1.5% | "all'1,5 per cento dei ricavi e altri proventi fino a euro 10 milioni" |
| Part over 10 and up to 50 million euro | 0.6% | "allo 0,6 per cento dei ricavi e altri proventi per la parte eccedente" |
| Part over 50 million euro | 0.4% | "allo 0,4 per cento dei ricavi e altri proventi per la parte eccedente euro 50 milioni" |

**TUIR art. 164, cars**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art164!vig=2026-06-30 |
| Cars not used exclusively as business assets | 20% | "nella misura del 20 per cento relativamente alle autovetture" |
| Agents and commercial representatives | 80% | "Tale percentuale è elevata all'80 per cento" |
| Cars given to employees for mixed use for most of the tax period | 70% | "nella misura del 70 per cento per i veicoli dati in uso promiscuo ai dipendenti per la maggior parte del periodo d'imposta" |

The share applies only to the part of the purchase cost, lease or hire charge within the limits in art. 164, which the statute still prints in lire. Professionals working alone may deduct costs for one vehicle only.

**TUIR art. 96, interest**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art96!vig=2026-06-30 |
| Net interest deductible up to this share of the risultato operativo lordo | 30% | "il 30 per cento del risultato operativo lordo della gestione caratteristica" |

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

## Section 5: Asset vs Expense Thresholds

### Capitalisation Rules

**Capitalisation rules table**

| Rule | Treatment |
| --- | --- |
| **Small assets, businesses** | Unit cost up to the art. 102(5) amount in Section 4: deductible in full in the year bought |
| **Small assets, professionals** | Separate limit, table below |
| **Forfettario** | No depreciation; the coefficient covers costs |
| **Tax** | First-year depreciation at half the coefficient (art. 102(2)) |

**TUIR art. 54-quinquies**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art54quinquies!vig=2026-06-30 |
| Professional: asset unit cost deductible in full | EUR 516.40 | "il cui costo unitario non sia superiore a euro 516,40" |

### Depreciation Rates (DM 31 December 1988: Coefficienti di Ammortamento)

Rates come from the decree by sector and asset group, halved in year one (TUIR art. 102(2)). The decree was not read, so no rates are given; refer.

- **Depreciation method** : straight-line within the coefficient. Accelerated depreciation (former art. 102(3)) was repealed by L. 244/2007. Any super-ammortamento is a separate law; check it first.

## Section 6: P&L Format (Conto Economico)

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

## Section 7: Balance Sheet Format (Stato Patrimoniale)

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

## Section 8: Bank Reconciliation Patterns

### Italian Bank Statement Formats

**Bank statement formats table** (OpenAccountants' observation, not an official source)

| Bank | Format | Key Fields |
| --- | --- | --- |
| Intesa Sanpaolo, Banco BPM, BPER Banca | CBI, CSV | Data operazione, Descrizione, Importo |
| UniCredit | CBI, CSV, MT940 | Data contabile, Causale, Dare, Avere |
| Poste Italiane, Revolut, N26 | PDF, CSV | Date, description, amount |

### Common Italian Transaction Descriptions

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

### Fatturazione Elettronica (E-Invoicing)

Who must e-invoice through the SdI, and from when, forfettari included, is in `italy-einvoice`. Match bank lines to the SdI XML invoices.

## Section 9: Micro-Entity / Small Business Simplifications

### Codice Civile Size Thresholds (updated by D.Lgs. 125/2024)

The first year the raised limits apply is not settled: D.Lgs. 125/2024 art. 17 names no start year for small companies that are not listed. Test the company against both the raised and the earlier limits, as `italy-financial-statements` explains, and get advice if the results differ.

**Art. 2435-ter (micro)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435ter!vig= |
| Total assets | EUR 220,000 | "220.000 euro" |
| Revenue | EUR 440,000 | "440.000 euro" |
| Average employees | 5 | "5 unità" |

**Art. 2435-bis (abbreviated)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435bis!vig= |
| Total assets | EUR 5,500,000 | "5.500.000 euro" |
| Revenue | EUR 11,000,000 | "11.000.000 euro" |
| Average employees | 50 | "50 unità" |

**Size thresholds table**

| Criterion | Microimpresa | Bilancio abbreviato | Bilancio ordinario |
| --- | --- | --- | --- |
| Total assets | Up to EUR 220,000 | Up to EUR 5,500,000 | Above EUR 5,500,000 |
| Revenue | Up to EUR 440,000 | Up to EUR 11,000,000 | Above EUR 11,000,000 |
| Average employees | Up to 5 | Up to 50 | Above 50 |

- **Two-of-three criteria rule** : in the first year, or afterwards for two consecutive years, not exceeding two of the three limits ("per due esercizi consecutivi, non abbiano superato due dei seguenti limiti", art. 2435-bis).

### Simplifications by Size

**Simplifications by size table**

| Requirement | Microimpresa | Bilancio abbreviato | Bilancio ordinario |
| --- | --- | --- | --- |
| Stato patrimoniale, conto economico | Abbreviated | Abbreviated | Full |
| Nota integrativa | Exempt if key information is at the foot of the balance sheet | Simplified | Full |
| Relazione sulla gestione | Exempt on the same condition | Exempt if the information is in the nota integrativa | Required |
| Rendiconto finanziario | Exempt | Exempt | Required |

### Individual Tax Regimes

**Individual tax regimes table**

| Regime | Who Qualifies | Bookkeeping Obligation |
| --- | --- | --- |
| Forfettario | Section 3 table | None for income tax; keep purchase invoices (Section 11) |
| Semplificato | Section 3 table | Receipts and payments registers (Section 11) |
| Ordinario | Companies, above the limits, or by option | Full books (Section 11) |
| Professional | Arts and professions | Register of fees and expenses (Section 11) |

## Section 10: Interaction with Tax Guides

**Interaction with tax Guides table**

| Tax Guide | How Bookkeeping Connects |
| --- | --- |
| **`it-income-tax`** | Professionals and forfettari |
| **IRES (companies)** | Risultato dell'esercizio is the start; Section 4 caps create permanent differences |
| **`italy-vat-return`** | 1420 and 2220 feed the liquidazione and the LIPE |
| **`it-irap`** | Base starts from the Differenza A-B |
| **`it-inps-contributions`** | Account 5310; self-employed contributions |

## Section 11: Books, registers and retention

- **Ordinary accounts.** Libro giornale, day by day (Civil Code art. 2216); libro degli inventari (art. 2214); IVA registers; auxiliary records by category; stock records where required; registro dei beni ammortizzabili; company books of art. 2421 (D.P.R. 600/1973 art. 14).
- **Inventory.** At the start and every year, closed by the balance sheet and profit and loss account, signed within three months of the income tax return deadline (Civil Code art. 2217; D.P.R. 600/1973 art. 15).
- **Registro dei beni ammortizzabili.** By the return deadline: year bought, cost, revaluations, accumulated depreciation, coefficient, the year's charge, disposals (art. 16). Under simplified accounts depreciation is deductible only if it is kept (TUIR art. 66(2)).
- **Simplified accounts.** A register of revenue received and a separate register of expenses paid, in date order, with amount, counterparty and invoice reference (art. 18(2)). IVA registers can replace them if non-IVA items are noted separately; unpaid invoices are listed at year end and entered when settled (art. 18(4)). A three-year option lets IVA registers stand alone, with registration presumed to be payment (art. 18(5)). The ordinary-accounts option binds for that year and the next two (art. 18(8)).
- **Professionals.** One chronological register of sums received (gross, net, withholding suffered, payer, invoice) and deductible expenses; depreciable assets entered by the return deadline (art. 19).
- **Forfettari.** "esonerati dagli obblighi di registrazione e tenuta delle scritture contabili", but still keep registers required by non-tax laws, and number and keep purchase invoices and customs bills (Agenzia "Semplificazioni e adempimenti" page).
- **IVA registers.** Sales invoices in number order by the 15th of the month after the operation (D.P.R. 633/1972 art. 23); purchases before the settlement that deducts them and by the annual return deadline (art. 25); numbered pages under Civil Code art. 2219 (art. 39).
- **Form, timing, retention.** Tax books numbered page by page; chronological and stock entries within sixty days (D.P.R. 600/1973 art. 22). Keep ten years from the last entry, with invoices and letters, image copies allowed if always legible (Civil Code art. 2220); for tax, until the year's assessments are final, even beyond (D.P.R. 600/1973 art. 22); e-invoices stored electronically (D.P.R. 633/1972 art. 39). Same rule as `italy-einvoice`.

## The method, step by step

1. **Pick the regime**: company, ordinary; sole trader or partnership, simplified if last year's revenue is within the limits, unless it opts out (D.P.R. 600/1973 art. 18, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art18!vig=); forfettario if its conditions are met (https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/semplificazioni-e-adempimenti).
2. **Open the books** for that regime (Section 11; D.P.R. 600/1973 art. 14, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art14!vig=2026-06-30).
3. **Record IVA documents on time** (D.P.R. 633/1972 art. 23, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art23!vig=2026-06-30).
4. **Year end**: apply the Section 4 caps, update the asset register (D.P.R. 600/1973 art. 16, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art16!vig=2026-06-30), sign the inventory (Civil Code art. 2217, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2217!vig=2026-06-30).
5. **Prepare the financial statements** in the art. 2424 and 2425 schemes, then keep everything for the art. 2220 period (https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2220!vig=2026-06-30).

## Ask the client first

- Company, partnership, sole trader or professional?
- Revenue actually received last year, and is the main activity services or other?
- Forfettario, or an option for ordinary accounts (and when)?
- IVA registers with cash notes, or the registration-date option?
- Stock and depreciable assets held, with dates and costs?
- Companies: total assets, revenue and average staff for the last two years.

## When to refuse or refer

- Listed companies, groups, banks, insurers, IFRS: outside this Guide.
- Audit limits and the first year of the raised size limits: not verified; refer.
- Sector depreciation rates: decree not read; refer.
- Tax audits, missing or destroyed books: refer to a commercialista.
- Agriculture, non-profit bodies, special IVA schemes: outside this Guide.

## Sources

- Civil Code (art. 2214 to 2220, 2424, 2425, 2435-bis, 2435-ter): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2220!vig=2026-06-30
- D.P.R. 600/1973 (art. 14 to 22): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art22!vig=2026-06-30
- D.P.R. 633/1972 (art. 23, 25, 39): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art39!vig=2026-06-30
- TUIR (art. 54-quinquies, 66, 77, 96, 102, 108, 109, 164): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art66!vig=2026-06-30
- Agenzia, forfettario: https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020-

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista or revisore legale) before filing or acting upon.

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
