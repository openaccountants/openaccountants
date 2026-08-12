---
name: italy-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Piano dei Conti, financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, or day-to-day accounting for an Italian entity. Trigger on phrases like "piano dei conti", "chart of accounts Italy", "bilancio", "conto economico", "stato patrimoniale", "OIC principles", "Codice Civile accounting", "regime forfettario bookkeeping", "capitalise or expense Italy", "ammortamento", "depreciation Italy", "bank reconciliation Italy", "microimpresa", "bilancio abbreviato", "bookkeeping Italy", or any question about recording transactions, classifying expenses, or preparing accounts under Italian law. ALWAYS read this skill before touching any bookkeeping work for Italy.
version: 1.0
jurisdiction: IT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italy Bookkeeping

## Italy Bookkeeping Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Currency | EUR |
| Financial year | Calendar year (1 Jan -- 31 Dec) for tax; companies may choose any 12-month period for statutory purposes |
| Accounting standards | OIC (Organismo Italiano di Contabilità) principles for non-listed entities; IFRS for listed/PIE entities |
| Governing body | OIC; Agenzia delle Entrate (tax); CONSOB (listed entities) |
| Key legislation | Codice Civile (Art. 2423--2435-ter); D.Lgs. 139/2015 (EU Directive transposition); TUIR (DPR 917/1986, income tax); DM 31/12/1988 (depreciation tables) |
| Standard chart of accounts | No legally mandated chart — entities design their own Piano dei Conti to map to Codice Civile balance sheet (Art. 2424) and income statement (Art. 2425) schemas |
| Record retention | 10 years (Art. 2220 Codice Civile; Art. 22 DPR 600/1973) |

## Section 2 -- Recommended Chart of Accounts (Piano dei Conti)

Italy does not mandate a standard chart of accounts. The following is a recommended structure aligned with the Codice Civile financial statement schemas (Art. 2424 for Stato Patrimoniale, Art. 2425 for Conto Economico).

### Assets (1xxx) — Stato Patrimoniale: Attivo

**Assets chart of accounts**  _(Art. 2424 Codice Civile)_

| Code | Account | CC Art. 2424 Reference |
| --- | --- | --- |
| 1000 | Immobilizzazioni immateriali | B.I |
| 1010 | Software e licenze | B.I.3 |
| 1020 | Avviamento (Goodwill) | B.I.5 |
| 1030 | Immobilizzazioni immateriali in corso | B.I.6 |
| 1100 | Immobilizzazioni materiali | B.II |
| 1110 | Terreni e fabbricati | B.II.1 |
| 1120 | Impianti e macchinari | B.II.2 |
| 1130 | Attrezzature industriali e commerciali | B.II.3 |
| 1140 | Macchine d'ufficio e computer | B.II.4 (altri beni) |
| 1150 | Mobili e arredi | B.II.4 |
| 1160 | Automezzi | B.II.4 |
| 1170 | Immobilizzazioni materiali in corso | B.II.5 |
| 1199 | Fondi ammortamento (accumulated depreciation) | Contra-asset |
| 1200 | Immobilizzazioni finanziarie | B.III |
| 1210 | Partecipazioni | B.III.1 |
| 1220 | Crediti (long-term) | B.III.2 |
| 1300 | Rimanenze (Inventories) | C.I |
| 1310 | Materie prime | C.I.1 |
| 1320 | Prodotti finiti e merci | C.I.4/5 |
| 1400 | Crediti verso clienti (Trade receivables) | C.II.1 |
| 1410 | Crediti tributari | C.II.5-bis |
| 1420 | IVA a credito (Input VAT) | C.II.5-bis |
| 1430 | Crediti verso altri | C.II.5-quater |
| 1440 | Ratei e risconti attivi (Prepayments) | D |
| 1500 | Banca c/c (Bank current account) | C.IV.1 |
| 1510 | Cassa (Cash in hand) | C.IV.3 |
| 1520 | Banca c/deposito (Savings) | C.IV.1 |

### Liabilities (2xxx) — Stato Patrimoniale: Passivo

**Liabilities chart of accounts**  _(Art. 2424 Codice Civile)_

| Code | Account | CC Art. 2424 Reference |
| --- | --- | --- |
| 2000 | Fondi per rischi e oneri (Provisions) | B |
| 2010 | TFR (Trattamento di fine rapporto) | C |
| 2100 | Debiti verso banche (Bank loans) | D.4 |
| 2110 | Debiti verso banche (short-term) | D.4 |
| 2200 | Debiti verso fornitori (Trade payables) | D.7 |
| 2210 | Debiti tributari (Tax liabilities) | D.12 |
| 2220 | IVA a debito (Output VAT) | D.12 |
| 2230 | Debiti vs istituti previdenziali (Social security) | D.13 |
| 2240 | Altri debiti | D.14 |
| 2300 | Ratei e risconti passivi (Deferred income) | E |

### Equity (3xxx) — Patrimonio Netto

**Equity chart of accounts**  _(Art. 2424 Codice Civile)_

| Code | Account | CC Art. 2424 Reference |
| --- | --- | --- |
| 3000 | Capitale sociale | A.I |
| 3010 | Riserva legale | A.IV |
| 3020 | Altre riserve | A.VI/VII |
| 3100 | Utili (perdite) portati a nuovo | A.VIII |
| 3200 | Utile (perdita) dell'esercizio | A.IX |

### Revenue (4xxx) — Conto Economico: Valore della Produzione (A)

**Revenue chart of accounts**  _(Art. 2425 Codice Civile)_

| Code | Account | CC Art. 2425 Reference |
| --- | --- | --- |
| 4000 | Ricavi delle vendite e delle prestazioni | A.1 |
| 4010 | Variazioni rimanenze prodotti | A.2/3 |
| 4020 | Incrementi immobilizzazioni per lavori interni | A.4 |
| 4100 | Altri ricavi e proventi | A.5 |
| 4110 | Contributi in conto esercizio | A.5 (with separate indication) |

### Cost of Production (5xxx) — Conto Economico: Costi della Produzione (B)

**Cost of production chart of accounts**  _(Art. 2425 Codice Civile)_

| Code | Account | CC Art. 2425 Reference |
| --- | --- | --- |
| 5000 | Acquisti materie prime e merci | B.6 |
| 5100 | Servizi (Services purchased) | B.7 |
| 5110 | Consulenze professionali | B.7 |
| 5120 | Utenze (utilities) | B.7 |
| 5130 | Manutenzioni e riparazioni | B.7 |
| 5140 | Assicurazioni | B.7 |
| 5150 | Pubblicità e marketing | B.7 |
| 5160 | Trasporti e spedizioni | B.7 |
| 5170 | Spese telefoniche e internet | B.7 |
| 5180 | Spese bancarie e commissioni | B.7 |
| 5200 | Godimento beni di terzi (Rent/leases) | B.8 |
| 5300 | Salari e stipendi | B.9.a |
| 5310 | Oneri sociali (Employer social charges) | B.9.b |
| 5320 | TFR dell'esercizio | B.9.c |
| 5400 | Ammortamento immobilizzazioni immateriali | B.10.a |
| 5410 | Ammortamento immobilizzazioni materiali | B.10.b |
| 5420 | Svalutazione crediti | B.10.d |
| 5500 | Variazione rimanenze materie prime | B.11 |
| 5600 | Accantonamenti per rischi | B.12 |
| 5700 | Altri accantonamenti | B.13 |
| 5800 | Oneri diversi di gestione | B.14 |

### Financial Income/Expenses (6xxx) — Conto Economico: C & D

**Financial income/expenses chart of accounts**  _(Art. 2425 Codice Civile)_

| Code | Account | CC Art. 2425 Reference |
| --- | --- | --- |
| 6000 | Proventi da partecipazioni | C.15 |
| 6100 | Interessi attivi (Interest income) | C.16 |
| 6200 | Interessi passivi (Interest expense) | C.17 |
| 6300 | Utili/perdite su cambi | C.17-bis |
| 6400 | Rivalutazioni attività finanziarie | D.18 |
| 6500 | Svalutazioni attività finanziarie | D.19 |

### Tax (7xxx)

**Tax chart of accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 7000 | IRES dell'esercizio | Corporate income tax (24%) |
| 7010 | IRAP dell'esercizio | Regional tax on productive activities (3.9% standard) |
| 7020 | Imposte differite (Deferred tax) |  |
| 7030 | Acconti d'imposta (Tax prepayments) | Credit against tax liability |

## Section 3 -- Revenue Recognition

**Revenue recognition scenarios**  _(OIC 12; OIC 23)_

| Scenario | Treatment |
| --- | --- |
| **Default (OIC 12)** | Accruals basis (competenza economica) — revenue when goods delivered or service performed |
| **Regime forfettario (flat-rate)** | Cash basis for tax; no formal financial statements required; simplified bookkeeping |
| **Regime ordinario** | Full accruals basis with double-entry bookkeeping |
| **Regime semplificato** | Simplified bookkeeping; presumption of cash-basis for certain items |
| **IVA on sales** | Revenue recorded net of IVA; IVA goes to 2220 (IVA a debito) |
| **Advance payments** | Deferred as ratei/risconti passivi (2300) until service delivered |
| **Long-term contracts** | Percentage-of-completion method required under OIC 23 for contracts in progress |

### Tax Regimes for Individuals/Small Businesses

**Tax regimes table**

| Regime | Revenue Threshold | Tax Rate | Bookkeeping |
| --- | --- | --- | --- |
| Forfettario | ≤ EUR 85,000 | 15% flat (5% first 5 years) | Cash receipts/invoices register only |
| Semplificato | ≤ EUR 500,000 (services) / 800,000 (goods) | Progressive IRPEF | Simplified registers |
| Ordinario | No limit | Progressive IRPEF / 24% IRES | Full double-entry |

## Section 4 -- Expense Classification

**Expense classification table**  _(TUIR Art. 96; TUIR Art. 102; DM 31/12/1988)_

| Expense Type | Piano dei Conti Code | Tax Deductibility | Notes |
| --- | --- | --- | --- |
| Office/commercial rent | 5200 | Fully deductible |  |
| Utilities | 5120 | Fully deductible (business premises) | Apportion if mixed |
| Professional fees (commercialista) | 5110 | Fully deductible |  |
| Insurance (business) | 5140 | Fully deductible |  |
| Advertising and marketing | 5150 | Fully deductible |  |
| Travel and accommodation | 5100 | Deductible with limits; hotels 100%, meals 75% |  |
| Entertainment (spese di rappresentanza) | 5800 | Deductible up to 1.5% of revenue (first EUR 10M) | Subject to annual limits |
| Telephone | 5170 | 80% deductible for tax | Fixed by TUIR Art. 102 |
| Motor vehicle costs | 5100 | 20% deductible (40% for agents); max acquisition cost EUR 18,076 | Cars not exclusively for business |
| Motor vehicle fuel | 5100 | 20% deductible | Traceable payments only |
| Bank charges | 5180 | Fully deductible |  |
| Interest expense | 6200 | Deductible subject to thin-cap (30% EBITDA rule per TUIR Art. 96) |  |
| Fines and penalties | 5800 | NOT deductible |  |
| Depreciation | 5400/5410 | Deductible per DM 31/12/1988 coefficients | Half-rate in first year |

## Section 5 -- Asset vs Expense Thresholds

### Capitalisation Rules

**Capitalisation rules table**  _(DM 31/12/1988)_

| Rule | Treatment |
| --- | --- |
| **No statutory de minimis threshold** | All assets with useful life > 1 year should be capitalised under OIC principles |
| **Practical tolerance** | Items under ~EUR 516.46 are often expensed immediately (inherited from old Lira threshold of 1,000,000 ITL) |
| **Small businesses (regime forfettario)** | No capitalisation required — all costs deducted via flat-rate coefficient |
| **Tax treatment** | First-year depreciation at half the normal rate (DM 31/12/1988) |

### Depreciation Rates (DM 31 December 1988 — Coefficienti di Ammortamento)

Rates are fiscal maximums applied to historical cost. The first year of use, only 50% of the rate is allowed.

**Depreciation rates table**  _(DM 31/12/1988)_

| Asset Category | Max Annual Rate | First-Year Rate |
| --- | --- | --- |
| Industrial buildings (fabbricati) | 3% | 1.5% |
| Light constructions (tettoie, baracche) | 10% | 5% |
| General plant and machinery (impianti generici) | 10% | 5% |
| Specific machinery (impianti specifici) | Varies by industry (15--25%) | Half |
| Office furniture and ordinary equipment (mobili e macchine ordinarie d'ufficio) | 12% | 6% |
| Computers and electronic office equipment (macchine d'ufficio elettroniche, computers) | 20% | 10% |
| Heavy transport vehicles (autoveicoli da trasporto) | 20% | 10% |
| Cars and motorcycles (autovetture, motoveicoli) | 25% | 12.5% |
| Miscellaneous small equipment (attrezzatura varia e minuta) | 15--40% | Half |

- **Depreciation method** — Depreciation method is straight-line (ammortamento ordinario). Accelerated depreciation is permitted in the first 3 years for certain assets (ammortamento anticipato — now largely abolished, except via super-ammortamento incentives when enacted).  _(DM 31/12/1988)_

## Section 6 -- P&L Format (Conto Economico)

Art. 2425 Codice Civile prescribes a scalare (vertical/list) format with costs classified by nature:

```
CONTO ECONOMICO
Esercizio chiuso al [date]

A) VALORE DELLA PRODUZIONE
   1) Ricavi delle vendite e delle prestazioni               xxx
   2) Variazione rimanenze prodotti in corso/finiti          xxx
   3) Variazione lavori in corso su ordinazione              xxx
   4) Incrementi immobilizzazioni per lavori interni         xxx
   5) Altri ricavi e proventi                                xxx
                                                            -----
   TOTALE (A)                                                xxx

B) COSTI DELLA PRODUZIONE
   6) Materie prime, sussidiarie, consumo e merci           (xxx)
   7) Servizi                                               (xxx)
   8) Godimento beni di terzi                               (xxx)
   9) Personale:
      a) Salari e stipendi                                  (xxx)
      b) Oneri sociali                                      (xxx)
      c) TFR                                                (xxx)
      d) Trattamento quiescenza e simili                    (xxx)
      e) Altri costi                                        (xxx)
  10) Ammortamenti e svalutazioni:
      a) Ammortamento immobilizzazioni immateriali          (xxx)
      b) Ammortamento immobilizzazioni materiali            (xxx)
      c) Altre svalutazioni delle immobilizzazioni          (xxx)
      d) Svalutazioni crediti                               (xxx)
  11) Variazione rimanenze materie prime                    (xxx)
  12) Accantonamenti per rischi                             (xxx)
  13) Altri accantonamenti                                  (xxx)
  14) Oneri diversi di gestione                             (xxx)
                                                            -----
   TOTALE (B)                                               (xxx)

   DIFFERENZA TRA VALORE E COSTI DELLA PRODUZIONE (A-B)     xxx

C) PROVENTI E ONERI FINANZIARI
  15) Proventi da partecipazioni                             xxx
  16) Altri proventi finanziari                              xxx
  17) Interessi e altri oneri finanziari                    (xxx)
  17-bis) Utili e perdite su cambi                          ±xxx
                                                            -----
   TOTALE (C)                                                xxx

D) RETTIFICHE DI VALORE DI ATTIVITÀ FINANZIARIE
  18) Rivalutazioni                                          xxx
  19) Svalutazioni                                          (xxx)
                                                            -----
   TOTALE (D)                                                xxx

   RISULTATO PRIMA DELLE IMPOSTE (A-B±C±D)                   xxx

  20) Imposte sul reddito dell'esercizio                    (xxx)
                                                            -----
   UTILE (PERDITA) DELL'ESERCIZIO                            xxx
```

## Section 7 -- Balance Sheet Format (Stato Patrimoniale)

Art. 2424 Codice Civile prescribes a two-section format:

```
STATO PATRIMONIALE
Al [date]

ATTIVO                                  PASSIVO

A) CREDITI VERSO SOCI                  A) PATRIMONIO NETTO
                                           I.    Capitale              xxx
B) IMMOBILIZZAZIONI                        IV.   Riserva legale       xxx
   I.   Immateriali          xxx           VII.  Altre riserve        xxx
   II.  Materiali            xxx           VIII. Utili portati a nuovo xxx
   III. Finanziarie          xxx           IX.   Utile dell'esercizio xxx
                            -----                                    -----
                             xxx                                      xxx

C) ATTIVO CIRCOLANTE                    B) FONDI PER RISCHI E ONERI   xxx
   I.   Rimanenze            xxx
   II.  Crediti              xxx        C) TFR                        xxx
   III. Attività finanziarie xxx
   IV.  Disponibilità liquide xxx       D) DEBITI                     xxx
                            -----
                             xxx        E) RATEI E RISCONTI PASSIVI   xxx

D) RATEI E RISCONTI ATTIVI  xxx                                     -----
                            -----      TOTALE PASSIVO                 xxx
TOTALE ATTIVO                xxx
```

## Section 8 -- Bank Reconciliation Patterns

### Italian Bank Statement Formats

**Bank statement formats table**

| Bank | Format | Key Fields |
| --- | --- | --- |
| Intesa Sanpaolo | CBI / CSV | Data operazione, Data valuta, Descrizione, Importo, Saldo |
| UniCredit | CBI / CSV / MT940 | Data contabile, Causale, Descrizione, Dare, Avere |
| Banco BPM | CBI / CSV | Data, Descrizione, Importo, Divisa |
| BPER Banca | CBI / CSV | Data operazione, Causale ABI, Descrizione, Importo |
| Poste Italiane (BancoPosta) | PDF / CSV | Data, Descrizione, Addebiti, Accrediti |
| Revolut / N26 | CSV | Date, Counterparty, Amount, Currency |

### Common Italian Transaction Descriptions

**Transaction descriptions table**

| Pattern | Likely Classification |
| --- | --- |
| BONIFICO / BON | Bank transfer — check if income or expense |
| ADDEBITO SDD / RID | Direct debit — utility, insurance |
| POS / CARTA | Card payment — check merchant |
| ASSEGNO | Cheque |
| STIPENDIO / COMPENSO | Salary or professional fee payment |
| F24 / DELEGA UNICA | Tax payment (IVA, IRES, IRAP, INPS) — exclude from P&L |
| INPS / CONTRIBUTI | Social security contributions (5310) |
| CANONE / AFFITTO | Rent payment (5200) |
| RATA MUTUO | Loan instalment — split capital (2100) and interest (6200) |
| COMMISSIONI / SPESE | Bank charges (5180) |
| GIROCONTO | Internal transfer — exclude |

### Fatturazione Elettronica (E-Invoicing)

Since 2019, all B2B and B2C invoices must be transmitted electronically via the SDI (Sistema di Interscambio). This provides a built-in reconciliation source: match bank transactions to XML invoices received/sent through SDI.

## Section 9 -- Micro-Entity / Small Business Simplifications

### Codice Civile Size Thresholds (updated by D.Lgs. 125/2024, effective 1 Jan 2024)

**Size thresholds table**  _(D.Lgs. 125/2024; Art. 2435-ter; Art. 2435-bis Codice Civile)_

| Criterion | Microimpresa (Art. 2435-ter) | Bilancio abbreviato (Art. 2435-bis) | Bilancio ordinario |
| --- | --- | --- | --- |
| Total assets | ≤ EUR 220,000 | ≤ EUR 5,500,000 | > EUR 5,500,000 |
| Revenue | ≤ EUR 440,000 | ≤ EUR 11,000,000 | > EUR 11,000,000 |
| Average employees | ≤ 5 | ≤ 50 | > 50 |

- **Two-of-three criteria rule** — Must not exceed 2 of 3 criteria for two consecutive years.  _(D.Lgs. 125/2024)_

### Simplifications by Size

**Simplifications by size table**  _(Art. 2435-bis; Art. 2424; Art. 2425 Codice Civile; OIC 10)_

| Requirement | Microimpresa | Bilancio abbreviato | Bilancio ordinario |
| --- | --- | --- | --- |
| Stato patrimoniale | Abbreviated (Art. 2435-bis format) | Abbreviated | Full (Art. 2424) |
| Conto economico | Abbreviated | Abbreviated | Full (Art. 2425) |
| Nota integrativa | EXEMPT (if key info in footnotes to SP) | Simplified | Full |
| Relazione sulla gestione | EXEMPT (if key info in footnotes to SP) | Exempt | Required |
| Rendiconto finanziario | EXEMPT | Exempt | Required (OIC 10) |
| Audit (revisione legale) | Not required (unless PIE) | Not required | Required if exceeding thresholds |
| Filing (Registro Imprese) | Abbreviated filing | Abbreviated filing | Full filing |

### Individual Tax Regimes

**Individual tax regimes table**

| Regime | Who Qualifies | Bookkeeping Obligation |
| --- | --- | --- |
| Forfettario | Revenue ≤ EUR 85,000 | Invoice register + cash receipts only; no double-entry |
| Semplificato | Revenue ≤ EUR 500K (services) / 800K (goods) | Simplified registers (IVA, incassi, pagamenti) |
| Ordinario | Anyone (mandatory above thresholds) | Full double-entry; all ledgers |

## Section 10 -- Interaction with Tax Skills

**Interaction with tax skills table**

| Tax Skill | How Bookkeeping Connects |
| --- | --- |
| **italy-income-tax (IRES/IRPEF)** | Risultato dell'esercizio from conto economico is the starting point. Non-deductible items (fines, excess entertainment, excess vehicle costs, telephone 20% add-back) generate permanent differences. First-year half-depreciation creates timing difference. |
| **italy-vat-return** | IVA accounts (1420 credito, 2220 debito) feed the Liquidazione IVA (monthly or quarterly). Annual IVA declaration reconciles to the ledger. Electronic invoices via SDI are the primary source documents. |
| **italy-irap** | IRAP base is derived from the Differenza A-B of the conto economico, with specific adjustments (personnel costs are generally not deductible for IRAP, except for certain deductions). |
| **italy-social-contributions** | INPS contributions in account 5310 (employer share) and employee deductions. Gestione separata for self-employed. Cassa professionale for regulated professions. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista or revisore legale) before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — **no liability on either side until you and the accountant sign a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

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
