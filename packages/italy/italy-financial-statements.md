---
name: italy-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (bilancio d'esercizio) for an Italian company. Trigger on phrases like "bilancio", "deposito bilancio", "Camera di Commercio", "Registro delle Imprese", "XBRL Italy", "codice civile 2423", "bilancio abbreviato", "micro imprese", "OIC", "revisione legale", "collegio sindacale", "nota integrativa", or any question about preparing and filing statutory accounts under Italian civil code. Covers OIC standards, size thresholds, required statements, formats, notes, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: IT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italy Financial Statements

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Currency | EUR |
| Filing authority | Registro delle Imprese (via Camera di Commercio) |
| Primary legislation | Codice Civile, Articles 2423–2435-ter |
| Supporting legislation | D.Lgs. 127/1991 (consolidated); D.Lgs. 39/2010 (audit); D.Lgs. 139/2015 (EU directive transposition) |
| Accounting standards | OIC (Organismo Italiano di Contabilità) — Italian GAAP |
| Financial year | Usually calendar year (January–December) |
| Filing deadline | 30 days after shareholder approval |
| Approval deadline | 120 days from year-end (extendable to 180 days) |
| Filing fee | EUR 62.70 (diritti di segreteria) + EUR 65 (bollo) |
| Digital filing | XBRL mandatory (tassonomia PCI 2018-11-04) via piattaforma DIRE |

## Section 2 -- Reporting Framework

**Section 2 -- Reporting Framework**

| Entity type | Applicable standard |
| --- | --- |
| All companies (individual accounts) | OIC (Italian GAAP based on Codice Civile) |
| Micro-imprese (Art. 2435-ter) | Simplified OIC with exemptions |
| Bilancio in forma abbreviata (Art. 2435-bis) | OIC with reduced disclosures |
| Listed groups (consolidated) | IFRS as adopted by the EU (mandatory) |
| Non-listed groups (consolidated) | OIC or IFRS (choice) |
| Banks and financial institutions | IFRS (mandatory, individual and consolidated) |

## Section 3 -- Size Thresholds

Effective for financial years beginning on or after 1 January 2024 (D.Lgs. 125/2024):

**Section 3 -- Size Thresholds**  _(D.Lgs. 125/2024)_

| Criterion | Micro (Art. 2435-ter) | Abbreviato (Art. 2435-bis) | Ordinario (Full) |
| --- | --- | --- | --- |
| Totale attivo (Total assets) | ≤ EUR 220,000 | ≤ EUR 5,000,000 | > EUR 5,000,000 |
| Ricavi delle vendite (Revenue) | ≤ EUR 440,000 | ≤ EUR 10,000,000 | > EUR 10,000,000 |
| Dipendenti medi (Employees) | ≤ 5 | ≤ 50 | > 50 |

- **Threshold exceedance rule** — Must not exceed 2 out of 3 thresholds in the first financial year, or for two consecutive financial years thereafter.

## Section 4 -- Required Financial Statements

**Section 4 -- Required Financial Statements**

| Document | Micro | Abbreviato | Ordinario |
| --- | --- | --- | --- |
| Stato Patrimoniale (Balance sheet) | Required (simplified) | Required (abridged) | Required (full) |
| Conto Economico (P&L) | Required (simplified) | Required (abridged) | Required (full) |
| Rendiconto Finanziario (Cash flow statement) | Not required | Not required | Required |
| Nota Integrativa (Notes) | Not required | Required (reduced) | Required (full) |
| Relazione sulla gestione (Management report) | Not required | Not required (with conditions) | Required |
| Relazione del revisore (Audit report) | If appointed | If appointed | Required |

## Section 5 -- Year-End Adjustments Checklist

**Section 5 -- Year-End Adjustments Checklist**

| # | Adjustment | Italy-specific notes |
| --- | --- | --- |
| 1 | Ammortamenti (Depreciation) | OIC 16; systematic plan; fiscal rates (DM 1988 coefficients) commonly used |
| 2 | TFR (Trattamento di fine rapporto) | Mandatory employee severance provision (Art. 2120 CC); actuarial valuation |
| 3 | Fondi rischi e oneri (Provisions) | OIC 31; probable, reliably estimable |
| 4 | Ratei e risconti (Accruals/prepayments) | OIC 18; strict time-proportion basis |
| 5 | Svalutazione crediti (Bad debts) | OIC 15; specific + portfolio-based allowance |
| 6 | Rimanenze (Inventory) | OIC 13; lower of cost (FIFO/LIFO/weighted average) and realisable value |
| 7 | Imposte differite (Deferred tax) | OIC 25; temporary differences; IRES 24% + IRAP 3.9% |
| 8 | Operazioni in valuta estera (FX) | OIC 26; monetary items at closing rate; unrealised gains to reserve |
| 9 | Leasing (locazione finanziaria) | OIC: off-balance sheet (operating method) — unlike IFRS 16 |
| 10 | Rivalutazioni (Revaluations) | Only if permitted by specific law (legge di rivalutazione) |
| 11 | Contributi pubblici (Government grants) | OIC 16 (assets) / OIC 12 (income); systematic recognition |
| 12 | Lavori in corso su ordinazione (Construction) | OIC 23; percentage-of-completion or completed-contract |

## Section 6 -- Conto Economico Format (P&L)

Art. 2425 Codice Civile — classification by nature:

```
A) VALORE DELLA PRODUZIONE (Value of production)
   1) Ricavi delle vendite e prestazioni
   2) Variazione rimanenze prodotti in lavorazione, semilavorati, finiti
   3) Variazione lavori in corso su ordinazione
   4) Incrementi di immobilizzazioni per lavori interni
   5) Altri ricavi e proventi

B) COSTI DELLA PRODUZIONE (Cost of production)
   6) Materie prime, sussidiarie, di consumo e merci
   7) Per servizi
   8) Per godimento beni di terzi
   9) Per il personale
      a) Salari e stipendi
      b) Oneri sociali
      c) Trattamento di fine rapporto
      d) Trattamento quiescenza e simili
      e) Altri costi
   10) Ammortamenti e svalutazioni
      a) Ammortamento immobilizzazioni immateriali
      b) Ammortamento immobilizzazioni materiali
      c) Altre svalutazioni delle immobilizzazioni
      d) Svalutazione crediti
   11) Variazione rimanenze materie prime
   12) Accantonamenti per rischi
   13) Altri accantonamenti
   14) Oneri diversi di gestione

   DIFFERENZA (A - B)

C) PROVENTI E ONERI FINANZIARI (Financial income/expenses)
   15) Proventi da partecipazioni
   16) Altri proventi finanziari
   17) Interessi e altri oneri finanziari
   17-bis) Utili e perdite su cambi

D) RETTIFICHE DI VALORE DI ATTIVITÀ FINANZIARIE
   18) Rivalutazioni
   19) Svalutazioni

   RISULTATO PRIMA DELLE IMPOSTE
   20) Imposte sul reddito dell'esercizio (correnti, differite, anticipate)
   21) UTILE (PERDITA) DELL'ESERCIZIO
```

## Section 7 -- Stato Patrimoniale Format (Balance Sheet)

Art. 2424 Codice Civile:

```
ATTIVO (Assets)

A) Crediti verso soci per versamenti ancora dovuti

B) Immobilizzazioni (Fixed assets)
   I.   Immobilizzazioni immateriali
   II.  Immobilizzazioni materiali
   III. Immobilizzazioni finanziarie

C) Attivo circolante (Current assets)
   I.   Rimanenze
   II.  Crediti
   III. Attività finanziarie (non immobilizzazioni)
   IV.  Disponibilità liquide

D) Ratei e risconti attivi

─────────────────────────────────────

PASSIVO (Equity and Liabilities)

A) Patrimonio netto (Equity)
   I.    Capitale sociale
   II.   Riserva da sovrapprezzo azioni
   III.  Riserve di rivalutazione
   IV.   Riserva legale
   V.    Riserve statutarie
   VI.   Altre riserve
   VII.  Riserva per operazioni di copertura
   VIII. Utili (perdite) portati a nuovo
   IX.   Utile (perdita) dell'esercizio

B) Fondi per rischi e oneri (Provisions)

C) Trattamento di fine rapporto di lavoro subordinato (TFR)

D) Debiti (Liabilities)

E) Ratei e risconti passivi
```

## Section 8 -- Nota Integrativa (Notes to Accounts)

**Section 8 -- Nota Integrativa (Notes to Accounts)**

| # | Disclosure | Micro | Abbreviato | Ordinario |
| --- | --- | --- | --- | --- |
| 1 | Accounting policies (criteri di valutazione) | Exempt | Required | Required |
| 2 | Fixed asset movements | Exempt | Simplified | Required |
| 3 | Receivables/payables by maturity | Exempt | Required | Required |
| 4 | Related party transactions | Exempt | If material | Required |
| 5 | Commitments and guarantees | Exempt | Required | Required |
| 6 | Employee numbers | Exempt | Average | By category |
| 7 | Directors' and auditors' remuneration | Exempt | Required | Required |
| 8 | Financial instruments (fair value) | Exempt | Simplified | Required |
| 9 | Deferred tax breakdown | Exempt | Required | Required |
| 10 | Revenue by activity/geography | Exempt | Not required | Required |
| 11 | Intercompany transactions | Exempt | If material | Required |
| 12 | Share capital and equity movements | Exempt | Required | Required |

## Section 9 -- Filing Requirements

**Section 9 -- Filing Requirements**

| Item | Detail |
| --- | --- |
| Filing authority | Registro delle Imprese (via Camera di Commercio locale) |
| Filing method | Online via piattaforma DIRE (digitally signed) |
| Format | XBRL (tassonomia PCI 2018-11-04) for financial statements; PDF/A for other documents |
| Approval deadline | 120 days from year-end (standard); 180 days (if statutory extension applies) |
| Filing deadline | 30 days after shareholder approval |
| Effective latest filing | 30 May (120 days) or 30 July (180 days) for calendar-year companies |
| Filing fee | EUR 62.70 (segreteria) + EUR 65.00 (bollo) = EUR 127.70 approx. |
| Late filing penalty | Administrative fine EUR 274.66 to EUR 549.33 (per Art. 2630 CC) |
| Language | Italian |
| Double format | XBRL + PDF/A if XBRL taxonomy cannot adequately represent the company's situation |

## Section 10 -- Audit Requirements

### Mandatory appointment of revisore legale or società di revisione

- **Statutory audit trigger for S.r.l.** — For S.r.l. (Art. 2477 CC), statutory audit is mandatory if the company exceeds any one of the following thresholds for two consecutive financial years.  _(Art. 2477 CC)_

**Mandatory audit thresholds**  _(Art. 2477 CC)_

| Criterion | Threshold |
| --- | --- |
| Totale attivo (Total assets) | EUR 4,000,000 |
| Ricavi (Revenue) | EUR 4,000,000 |
| Dipendenti medi (Average employees) | 20 |

- **Obligation cessation rule** — The obligation ceases if none of the thresholds are exceeded for three consecutive years.

### Other mandatory cases

- **S.p.A. audit** — S.p.A.: audit always mandatory  _(Art. 2409-bis CC)_
- **S.r.l. preparing consolidated accounts** — S.r.l. preparing consolidated accounts: audit mandatory
- **S.r.l. controlling audited company** — S.r.l. controlling a company subject to audit: audit mandatory
- **Public interest entities** — Public interest entities: full audit with additional oversight

### Auditor qualification

- **Auditor qualification** — Revisore legale iscritto nel Registro dei Revisori Legali (MEF) or società di revisione registered with the same registry.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

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
