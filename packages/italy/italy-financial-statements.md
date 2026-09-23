---
name: italy-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (bilancio d'esercizio) for an Italian company. Trigger on phrases like "bilancio", "deposito bilancio", "Camera di Commercio", "Registro delle Imprese", "XBRL Italy", "codice civile 2423", "bilancio abbreviato", "micro imprese", "OIC", "revisione legale", "collegio sindacale", "nota integrativa", or any question about preparing and filing statutory accounts under Italian civil code. Covers OIC standards, size thresholds, required statements, formats, notes, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Annual financial statements in Italy (bilancio d'esercizio)

How an Italian company prepares, approves and files its annual financial statements under the Civil Code: which form it may use (ordinary, abbreviated or micro), what each form must contain, the approval and filing deadlines, and when an S.r.l. must appoint a control body or auditor. For S.r.l. and S.p.A. companies and their accountants. Figures are for tax year 2026, from the Civil Code text in force on Normattiva on 22 September 2026. D.Lgs. 125/2024 raised the size limits; the first year they apply from is not stated plainly on any page read (Section 3).

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Currency | EUR |
| Filing authority | Registro delle Imprese (via Camera di Commercio) |
| Primary legislation | Codice Civile, Articles 2423 to 2435-ter; for S.r.l. also Articles 2477 and 2478-bis |
| Supporting legislation | D.Lgs. 127/1991 (consolidated); D.Lgs. 39/2010 (audit); D.Lgs. 139/2015 (EU transposition, years from 1 January 2016); D.Lgs. 38/2005 (IFRS); D.Lgs. 125/2024 (raised size limits) |
| Accounting standards | OIC (Organismo Italiano di Contabilità): Italian GAAP. OIC standards are not published on an official host this Guide may cite |
| Financial year | Usually calendar year (January to December) |
| Approval deadline | By the date in the bylaws, not more than 120 days from year-end; up to 180 days if the bylaws allow it and the case qualifies (art. 2364). For an S.r.l., art. 2478-bis sets the same limits for presenting the accounts to the members |
| Filing deadline | Within 30 days of approval (art. 2435; art. 2478-bis) |
| Filing fee | Not stated on an allowed host. The legacy amounts were removed; ask the Camera di Commercio |
| Digital filing | Electronic processable format (XBRL) required by D.L. 223/2006 art. 37(21-bis); taxonomy version set by the business register, not an allowed host |

## Section 2: Reporting Framework

| Entity type | Applicable standard |
| --- | --- |
| All companies (individual accounts) | Civil Code rules, applied through the OIC standards |
| Micro-imprese (Art. 2435-ter) | Abbreviated form with the micro exemptions |
| Bilancio in forma abbreviata (Art. 2435-bis) | Abbreviated form with reduced notes |
| Listed companies and groups | IFRS as adopted by the EU (mandatory; D.Lgs. 38/2005 arts. 3 and 4) |
| Non-listed groups (consolidated) | Civil Code and OIC, or IFRS by option for companies D.Lgs. 38/2005 art. 2 lists (art. 3(2)); not normally revocable |
| Banks and supervised financial institutions | IFRS (mandatory, individual and consolidated, D.Lgs. 38/2005 arts. 2 to 4) |

D.Lgs. 38/2005 art. 4: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-02-28;38~art4!vig=

## Section 3: Size Thresholds

The Civil Code in force prints the limits below. A company qualifies if, in its first financial year or afterwards for two consecutive years, it did not exceed two of the three limits. It must switch to the larger form when it exceeds two limits for the second consecutive year. Companies with securities traded on regulated markets cannot use the abbreviated form.

**Art. 2435-ter (micro)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435ter!vig= |
| Total assets (totale dell'attivo) | EUR 220,000 | "220.000 euro" |
| Revenue (ricavi delle vendite e delle prestazioni) | EUR 440,000 | "440.000 euro" |
| Average employees | 5 | "5 unità" |

**Art. 2435-bis (abbreviated)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435bis!vig= |
| Total assets | EUR 5,500,000 | "5.500.000 euro" |
| Revenue | EUR 11,000,000 | "11.000.000 euro" |
| Average employees | 50 | "50 unità" |

**Limits before D.Lgs. 125/2024 (use these if the raised limits do not yet apply to the company's year)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-09-06;125~art16!vig= |
| Abbreviated, total assets, replaced | EUR 4,400,000 | Art. 16(1)(a): "4.400.000" replaced by "5.500.000" |
| Abbreviated, revenue, replaced | EUR 8,800,000 | "8.800.000" replaced by "11.000.000" |
| Micro, total assets, replaced | EUR 175,000 | Art. 16(1)(b): "175.000" replaced by "220.000" |
| Micro, revenue, replaced | EUR 350,000 | "350.000" replaced by "440.000" |

**Section 3: Size Thresholds**  _(Art. 2435-ter; Art. 2435-bis Codice Civile)_

| Criterion | Micro (Art. 2435-ter) | Abbreviato (Art. 2435-bis) | Ordinario (two of three exceeded) |
| --- | --- | --- | --- |
| Totale attivo (Total assets) | Up to EUR 220,000 | Up to EUR 5,500,000 | Above EUR 5,500,000 |
| Ricavi delle vendite (Revenue) | Up to EUR 440,000 | Up to EUR 11,000,000 | Above EUR 11,000,000 |
| Dipendenti medi (Employees) | Up to 5 | Up to 50 | Above 50 |

This table uses the raised limits printed in the Civil Code in force. Until the first year of the raised limits is confirmed (bullet below), test total assets and revenue against both sets. The employee limits are the same in both sets.

- **Threshold exceedance rule**: must not exceed 2 of the 3 limits in the first financial year, or for two consecutive financial years afterwards (art. 2435-bis, first paragraph).
- **When the raised limits start**: Read literally, art. 17 is a closed list: it does not name small or micro companies whose securities are not listed, so it gives them no start year at all. Whether the raised limits already apply to such a company's 2026 accounts, and to the earlier year used in the two-year test, is therefore not settled by the Italian text. Confirm before relying on the raised limits; a company between the old and new limits should get advice. Art. 17: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-09-06;125~art17!vig=

## Section 4: Required Financial Statements

| Document | Micro | Abbreviato | Ordinario |
| --- | --- | --- | --- |
| Stato Patrimoniale (Balance sheet) | Required (abbreviated) | Required (abbreviated: letters and Roman numerals only) | Required (full) |
| Conto Economico (P&L) | Required (abbreviated) | Required (abbreviated, some items grouped) | Required (full) |
| Rendiconto Finanziario (Cash flow statement) | Not required | Not required | Required |
| Nota Integrativa (Notes) | Not required if the information in art. 2427 numbers 9 and 16 is given at the foot of the balance sheet | Required (reduced list) | Required (full) |
| Relazione sulla gestione (Management report) | Not required if the information in art. 2428 numbers 3 and 4 is given at the foot of the balance sheet | Not required if that information is given in the nota integrativa | Required |
| Relazione del revisore (Audit report) | If an auditor is appointed or required | If an auditor is appointed or required | If an auditor is appointed or required (Section 10) |

Sources: art. 2435-bis and art. 2435-ter (Section 3).

A micro company is a company that could use the abbreviated form (no securities traded on a regulated market). It may not depart from a rule under art. 2423 fifth paragraph and may not apply art. 2426 number 11-bis (derivatives at fair value). The micro rules do not apply to investment entities and financial holding companies. The micro "Exempt" entries in Section 8 hold only when numbers 9 and 16 of art. 2427 are given at the foot of the balance sheet.

## Section 5: Year-End Adjustments Checklist

| # | Adjustment | Italy-specific notes |
| --- | --- | --- |
| 1 | Ammortamenti (Depreciation) | OIC no. 16; systematic plan; fiscal rates (DM 1988 coefficients) commonly used |
| 2 | TFR (Trattamento di fine rapporto) | Mandatory employee severance provision. The balance sheet shows the amount calculated under art. 2120 (art. 2424-bis), not an actuarial value; actuarial measurement is an IFRS approach |
| 3 | Fondi rischi e oneri (Provisions) | OIC no. 31; only for losses or debts of a definite nature, certain or probable, with amount or date uncertain (art. 2424-bis) |
| 4 | Ratei e risconti (Accruals/prepayments) | OIC no. 18; only for costs and income common to two or more years that vary with time (art. 2424-bis) |
| 5 | Svalutazione crediti (Bad debts) | OIC no. 15; specific and portfolio-based allowance |
| 6 | Rimanenze (Inventory) | OIC no. 13; lower of cost (weighted average, FIFO or LIFO for fungible goods) and realisable value (art. 2426 numbers 9 and 10) |
| 7 | Imposte differite (Deferred tax) | OIC no. 25; temporary differences; see the IRES and IRAP rate tables below (regional variations and sector surcharges apply) |
| 8 | Operazioni in valuta estera (FX) | OIC no. 26; monetary items at the closing spot rate; a net FX gain goes to a reserve that cannot be distributed until realised (art. 2426 number 8-bis) |
| 9 | Leasing (locazione finanziaria) | OIC: off-balance sheet (operating method), unlike IFRS 16; the effects of the financial method are disclosed in the notes (art. 2427 number 22) |
| 10 | Rivalutazioni (Revaluations) | Only if permitted by specific law (legge di rivalutazione) |
| 11 | Contributi pubblici (Government grants) | OIC no. 16 (assets) / OIC no. 12 (income); systematic recognition |
| 12 | Lavori in corso su ordinazione (Construction) | OIC no. 23; percentage-of-completion or completed-contract (art. 2426 number 11) |

The OIC numbers are legacy content. OIC standards are published by the Organismo Italiano di Contabilità, not on an allowed host, and were not checked.

**IRES rate**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig= |
| IRES standard rate (TUIR art. 77) | 24% | "con l'aliquota del 24 per cento" |

**IRAP rate**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 |
| IRAP ordinary rate | 3.9% | "aliquota del 3,9 per cento" |

For the tax computations behind these rates, see `it-irap`. Art. 2424-bis: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2424bis!vig= and art. 2426: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2426!vig=

## Section 6: Conto Economico Format (P&L)

Art. 2425 Codice Civile, classification by nature, for years starting from 1 January 2016. Source: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2425!vig=

~~~
A) VALORE DELLA PRODUZIONE (Value of production)
   1) Ricavi delle vendite e delle prestazioni
   2) Variazioni rimanenze prodotti in lavorazione, semilavorati, finiti
   3) Variazioni lavori in corso su ordinazione
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
   11) Variazioni rimanenze materie prime
   12) Accantonamenti per rischi
   13) Altri accantonamenti
   14) Oneri diversi di gestione

   DIFFERENZA (A - B)

C) PROVENTI E ONERI FINANZIARI (Financial income/expenses)
   15) Proventi da partecipazioni
   16) Altri proventi finanziari
   17) Interessi e altri oneri finanziari
   17-bis) Utili e perdite su cambi

D) RETTIFICHE DI VALORE DI ATTIVITA E PASSIVITA FINANZIARIE
   18) Rivalutazioni (a to c, and d strumenti finanziari derivati)
   19) Svalutazioni (a to c, and d strumenti finanziari derivati)

   RISULTATO PRIMA DELLE IMPOSTE (A - B +/- C +/- D)
   20) Imposte sul reddito dell'esercizio, correnti, differite e anticipate
   21) Utile (perdite) dell'esercizio
~~~

## Section 7: Stato Patrimoniale Format (Balance Sheet)

Art. 2424 Codice Civile. Source: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2424!vig=

~~~
ATTIVO (Assets)

A) Crediti verso soci per versamenti ancora dovuti

B) Immobilizzazioni (Fixed assets)
   I.   Immobilizzazioni immateriali
   II.  Immobilizzazioni materiali
   III. Immobilizzazioni finanziarie

C) Attivo circolante (Current assets)
   I.   Rimanenze
   II.  Crediti
   III. Attivita finanziarie che non costituiscono immobilizzazioni
   IV.  Disponibilita liquide

D) Ratei e risconti attivi

PASSIVO (Equity and Liabilities)

A) Patrimonio netto (Equity)
   I.    Capitale
   II.   Riserva da sovrapprezzo delle azioni
   III.  Riserve di rivalutazione
   IV.   Riserva legale
   V.    Riserve statutarie
   VI.   Altre riserve
   VII.  Riserva per operazioni di copertura dei flussi finanziari attesi
   VIII. Utili (perdite) portati a nuovo
   IX.   Utile (perdita) dell'esercizio
   X.    Riserva negativa per azioni proprie in portafoglio

B) Fondi per rischi e oneri (Provisions)

C) Trattamento di fine rapporto di lavoro subordinato (TFR)

D) Debiti (Liabilities)

E) Ratei e risconti passivi
~~~

## Section 8: Nota Integrativa (Notes to Accounts)

The ordinary notes follow art. 2427. The abbreviated notes give only the items listed in art. 2435-bis (art. 2427 numbers 1, 2, 6 for debts only, 8, 9, 13, 15, 16, 22-bis, 22-ter, 22-quater, 22-sexies, and art. 2427-bis number 1). A micro company needs no notes if numbers 9 and 16 appear at the foot of the balance sheet.

| # | Disclosure | Micro | Abbreviato | Ordinario |
| --- | --- | --- | --- | --- |
| 1 | Accounting policies (criteri di valutazione) | Exempt | Required (n. 1) | Required |
| 2 | Fixed asset movements | Exempt | Required (n. 2) | Required |
| 3 | Receivables/payables by maturity | Exempt | Debts only, without geographic split (n. 6) | Required |
| 4 | Related party transactions | Exempt | Required (n. 22-bis); may be limited to major shareholders, board members and investees | Required |
| 5 | Commitments and guarantees | At foot of balance sheet (n. 9) | Required (n. 9) | Required |
| 6 | Employee numbers | Exempt | Average, category split may be omitted (n. 15) | By category |
| 7 | Directors' and auditors' remuneration | At foot of balance sheet (n. 16) | Required (n. 16) | Required |
| 8 | Financial instruments (fair value) | Exempt | Derivatives (art. 2427-bis n. 1) | Required |
| 9 | Deferred tax breakdown | Exempt | Not in the abbreviated list (n. 14 not listed) | Required |
| 10 | Revenue by activity/geography | Exempt | Not required | Required |
| 11 | Intercompany transactions | Exempt | Through n. 22-bis (related parties) | Required |
| 12 | Share capital and equity movements | Exempt | Not in the abbreviated list (n. 4 and n. 7-bis not listed) | Required |

Source: art. 2435-bis (link in Section 3); art. 2427: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2427!vig=

## Section 9: Filing Requirements

Before the meeting, the directors give the draft accounts and their report to the collegio sindacale and the auditor at least thirty days before the meeting date, and the accounts stay deposited at the company's seat for the fifteen days before the meeting (art. 2429). After approval, the directors file a copy with the Registro delle Imprese within thirty days, with the management report, the auditors' reports and the approval minutes (art. 2435).

**Late filing penalty (art. 2630)**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2630!vig= |
| Administrative fine, lower end | EUR 103 | "da 103 euro a 1.032 euro" |
| Administrative fine, upper end | EUR 1,032 | "da 103 euro a 1.032 euro" |

The fine is set for each person who was obliged to file because of their office. The whole range is reduced to one third if the filing is made within thirty days after the deadline, and increased by one third where the accounts (bilanci) are not filed.

| Item | Detail |
| --- | --- |
| Filing method | Online, digitally signed. Legacy Guide named the DIRE platform; a business-register tool, not checked here |
| Format | Electronic processable format (XBRL) under D.L. 223/2006 art. 37(21-bis). Legacy PCI taxonomy date removed as unverified; use the taxonomy the business register currently requires |
| Approval deadline | Not more than 120 days from year-end; up to 180 days where the bylaws allow it for a company that prepares consolidated accounts or has particular needs linked to its structure and object. The directors must explain the delay in the management report (art. 2364) |
| Filing deadline | 30 days after approval (art. 2435; art. 2478-bis for S.r.l.) |
| List of shareholders | Companies without listed shares also file the list of shareholders within 30 days of approval (art. 2435) |
| Effective latest filing | The approval deadline plus 30 days. Legacy calendar dates removed; no page read prints them |
| Late filing penalty | The fine in the table above (art. 2630) |
| Language | Italian |
| Double format | XBRL, plus PDF/A if the taxonomy cannot represent the company's situation (legacy, unchecked) |

Art. 2364: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2364!vig= · art. 2435: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435!vig= · art. 2429: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2429!vig= · D.L. 223/2006 art. 37: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2006-07-04;223~art37!vig=

## Section 10: Audit Requirements

### Mandatory appointment of revisore legale or società di revisione

- **Control body or auditor for S.r.l.**: an S.r.l. must appoint a control body (organo di controllo, one member unless the bylaws say otherwise) or an auditor (revisore) if it exceeded at least one of the limits below for two consecutive financial years. The meeting that approves the accounts in which the limits are exceeded must appoint within thirty days; otherwise the court appoints on request of any interested party or on report of the business register. _(Art. 2477 CC)_

**Mandatory audit thresholds**  _(Art. 2477 CC)_

| Criterion | Threshold | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2477!vig= |
| Totale attivo (Total assets) | EUR 4 million | "4 milioni di euro" |
| Ricavi (Revenue) | EUR 4 million | "4 milioni di euro" |
| Dipendenti medi (Average employees) | 20 | "20 unità" |

- **Obligation cessation rule**: the obligation ends when none of the limits is exceeded for three consecutive years.
- These are not the art. 2435-bis limits. An S.r.l. can use the abbreviated form and still have to appoint a control body or auditor.

### Other mandatory cases

- **S.p.A. audit**: from 29 April 2026 the rule is in art. 2396-novies of the Civil Code, added by D.Lgs. 27 marzo 2026 n. 47, which also repealed the first paragraph of art. 2409-bis: the statutory audit of the company is carried out by a registered revisore legale or società di revisione. The remaining paragraph of art. 2409-bis still lets an S.p.A. that does not prepare consolidated accounts give the audit to the collegio sindacale, made up of registered auditors. Art. 2396-novies: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2396novies!vig= ; art. 2409-bis: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2409bis!vig=
- **S.r.l. preparing consolidated accounts**: appointment mandatory (art. 2477(2)(a))
- **S.r.l. controlling audited company**: appointment mandatory if it controls a company that must have a statutory audit (art. 2477(2)(b))
- **Public interest entities**: full audit with extra oversight under D.Lgs. 39/2010 (unchecked)

### Auditor qualification

- **Auditor qualification**: revisore legale registered in the Registro dei Revisori Legali (kept by the Ministry of Economy and Finance) or a società di revisione registered in the same register (legacy, unchecked).

## The method, step by step

1. Test the size of the company against art. 2435-ter and art. 2435-bis for the current and previous year (two-of-three rule), and note the start-date question in Section 3: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435bis!vig=
2. Prepare the balance sheet and P&L in the art. 2424 and art. 2425 layouts (abbreviated where allowed), with the year-end adjustments in Section 5: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2425!vig=
3. Write the nota integrativa (art. 2427, or the reduced art. 2435-bis list) and, unless exempt, the management report: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2427!vig=
4. Give the draft to the collegio sindacale and auditor at least thirty days before the meeting, and deposit it at the seat for the fifteen days before (art. 2429): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2429!vig=
5. Hold the approval within 120 days of year-end, or 180 days where the bylaws allow and the case qualifies (art. 2364; art. 2478-bis): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2478bis!vig=
6. File the approved accounts in XBRL with the Registro delle Imprese within 30 days of approval, with the reports, the minutes and, for companies without listed shares, the shareholder list (art. 2435): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2435!vig=
7. For an S.r.l., check the art. 2477 limits for the last two years; if exceeded, appoint a control body or auditor at the approving meeting or within thirty days: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2477!vig=

## Ask the client first

- Is it an S.r.l. or an S.p.A., and does it have securities traded on a regulated market?
- What were total assets, revenue and average employees for this year and the last two years?
- Is the company part of a group that prepares consolidated accounts, or does it control an audited company?
- What do the bylaws say about the approval deadline, and is there a reason for the 180-day extension?
- Does the company already have a sindaco, collegio sindacale or auditor, and since when?
- Has the company opted for IFRS, or is it a bank, insurer or listed company?

## When to refuse or refer

- Consolidated accounts (D.Lgs. 127/1991) and IFRS financial statements.
- Banks, insurers, investment firms and other public interest entities.
- Sustainability reporting under D.Lgs. 125/2024.
- A company between the old and new size limits whose form depends on the start-date question in Section 3.
- S.p.A. governance and control questions after the April 2026 reform (D.Lgs. 47/2026).
- Revaluations under a special law, extraordinary transactions, going-concern doubts, or accounts not approved or filed on time.

## Sources

- Civil Code arts. 2364, 2396-novies, 2424, 2424-bis, 2425, 2426, 2427, 2429, 2435, 2435-bis, 2435-ter, 2409-bis, 2477, 2478-bis, 2630 on Normattiva (links above)
- D.Lgs. 125/2024 arts. 16 and 17: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-09-06;125~art16!vig=
- D.Lgs. 38/2005 art. 4: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-02-28;38~art4!vig=
- D.L. 223/2006 art. 37: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2006-07-04;223~art37!vig=
- TUIR art. 77: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art77!vig=
- IRAP 2026 instructions: https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
