---
name: netherlands-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (jaarrekening) for a Dutch company. Trigger on phrases like "jaarrekening", "KvK filing", "Kamer van Koophandel", "BW2 Titel 9", "Dutch GAAP", "RJ richtlijnen", "deponeren", "annual accounts Netherlands", "audit Netherlands", "small BV", "micro BV", or any question about preparing and filing statutory accounts under Dutch law. Covers Dutch GAAP (RJ guidelines), size thresholds, required statements, formats, notes, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: NL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Netherlands Financial Statements

## Netherlands Financial Statements Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Netherlands (Koninkrijk der Nederlanden) |
| Currency | EUR |
| Filing authority | Kamer van Koophandel (KvK) — Chamber of Commerce |
| Primary legislation | Burgerlijk Wetboek Boek 2, Titel 9 (BW2 Title 9), Articles 2:360–2:446 |
| Supporting guidelines | Richtlijnen voor de Jaarverslaggeving (RJ — Dutch Accounting Standards Board) |
| Accounting standards | Dutch GAAP (Title 9 BW2 + RJ guidelines); IFRS-EU optional for individual accounts |
| Financial year | Usually calendar year; any 12-month period permitted |
| Filing deadline | 8 days after adoption; adoption within 5 months (+6 months extension possible = max 12 months from year-end) |
| Late filing penalty | Director liability exposure (Art. 2:248 BW2) — presumption of mismanagement in bankruptcy |
| Digital filing | SBR (Standard Business Reporting) via Digipoort; mandatory for small/micro from 2024 |

## Section 2 -- Reporting Framework

**Reporting Framework**

| Entity type | Applicable standard |
| --- | --- |
| All BVs, NVs, cooperatives, mutual guarantee associations | BW2 Title 9 + RJ guidelines |
| Micro entities (Art. 2:395a) | Minimal requirements; very limited disclosure |
| Small entities (Art. 2:396) | Reduced preparation and publication requirements |
| Medium entities (Art. 2:397) | Full preparation; some filing exemptions |
| Large entities | Full Title 9 requirements |
| Listed groups (consolidated) | IFRS-EU mandatory |
| Non-listed (individual or consolidated) | Dutch GAAP or IFRS-EU (choice, with restrictions) |

## Section 3 -- Size Thresholds

Effective for financial years beginning on or after 1 January 2024 (Implementatiewet):

**Size Thresholds**

| Criterion | Micro (Art. 2:395a) | Klein/Small (Art. 2:396) | Middelgroot/Medium (Art. 2:397) | Groot/Large |
| --- | --- | --- | --- | --- |
| Balanstotaal (Total assets) | ≤ EUR 450,000 | ≤ EUR 7,500,000 | ≤ EUR 25,000,000 | > EUR 25,000,000 |
| Netto-omzet (Net turnover) | ≤ EUR 900,000 | ≤ EUR 15,000,000 | ≤ EUR 50,000,000 | > EUR 50,000,000 |
| Werknemers (Employees) | < 10 | < 50 | < 250 | ≥ 250 |

- **Size classification rule** — Must satisfy 2 out of 3 criteria on balance sheet dates of two consecutive financial years.

## Section 4 -- Required Financial Statements

**Required Financial Statements**

| Document | Micro | Small | Medium | Large |
| --- | --- | --- | --- | --- |
| Balans (Balance sheet) | Required (very simple) | Required (abbreviated) | Required (full) | Required (full) |
| Winst-en-verliesrekening (P&L) | Not required to file | Not required to file | Required (abridged ok) | Required (full) |
| Kasstroomoverzicht (Cash flow statement) | Not required | Not required | Required | Required |
| Toelichting (Notes) | Minimal | Abbreviated | Required | Required (full) |
| Bestuursverslag (Management report) | Not required | Not required to file | Required | Required |
| Accountantsverklaring (Auditor's report) | Not required | Not required | Required | Required |

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | Netherlands-specific notes |
| --- | --- | --- |
| 1 | Afschrijvingen (Depreciation) | RJ 212; systematic over useful life; componentisation |
| 2 | Voorzieningen (Provisions) | RJ 252; best estimate of expenditure; discounting if time value material |
| 3 | Overlopende activa/passiva (Accruals) | Transitoria; strict matching |
| 4 | Voorziening dubieuze debiteuren (Bad debts) | Individual assessment + statistical allowance |
| 5 | Voorraden (Inventory) | RJ 220; lower of cost (FIFO/weighted average) and net realisable value; no LIFO |
| 6 | Latente belastingen (Deferred tax) | RJ 272; balance sheet liability method; Vpb rate 25.8% (>EUR 200k) / 19% (≤EUR 200k) |
| 7 | Vreemde valuta (Foreign currency) | RJ 122; closing rate for monetary items |
| 8 | Leasing | RJ 292; finance/operating distinction (similar to IAS 17, not IFRS 16) |
| 9 | Pensioenen (Pensions) | RJ 271; contribution-based or obligation-based |
| 10 | Jubileumvoorziening (Anniversary provision) | Required if obligation exists |
| 11 | Onderhoud voorziening (Maintenance) | Big maintenance provision (RJ 212.442+) |
| 12 | Wettelijke reserve (Statutory reserves) | Required for capitalised development costs, participations, FX translation |

## Section 6 -- Winst-en-verliesrekening Format (P&L)

- **P&L Format (categoriale model)** — BW2 Art. 2:377 — model by nature (categoriale model): ``` Netto-omzet (Net turnover) Wijziging in voorraden gereed product en onderhanden werk Geactiveerde productie eigen bedrijf Overige bedrijfsopbrengsten Kosten van grond- en hulpstoffen (Raw materials) Kosten uitbesteed werk (Subcontracted work) Lonen en salarissen (Wages and salaries) Sociale lasten (Social security costs) Afschrijvingen (Depreciation and amortisation) Overige bedrijfskosten (Other operating expenses) ─── Bedrijfsresultaat (Operating result) ─── Opbrengst van vorderingen (Interest income) Opbrengst van effecten (Investment income) Rentebaten en soortgelijke opbrengsten Rentelasten en soortgelijke kosten (Interest expense) Waardeveranderingen financiële vaste activa ─── Resultaat uit gewone bedrijfsuitoefening vóór belastingen ─── Belastingen resultaat uit gewone bedrijfsuitoefening (Tax) ─── Resultaat uit gewone bedrijfsuitoefening ná belastingen ─── Buitengewone baten (Extraordinary income) Buitengewone lasten (Extraordinary expenses) Belastingen buitengewoon resultaat ─── Resultaat na belastingen (Net result) ─── ```  _(BW2 Art. 2:377)_

## Section 7 -- Balans Format (Balance Sheet)

- **Balance Sheet Format** — BW2 Art. 2:364 — standard format: ``` ACTIVA (Assets) Vaste activa (Fixed assets) Immateriële vaste activa (Intangible fixed assets) Kosten van ontwikkeling Concessies, vergunningen, intellectuele eigendom Goodwill Materiële vaste activa (Tangible fixed assets) Bedrijfsgebouwen en -terreinen Machines en installaties Andere vaste bedrijfsmiddelen Vaste bedrijfsmiddelen in uitvoering Financiële vaste activa (Financial fixed assets) Deelnemingen Vorderingen op groepsmaatschappijen Overige effecten Vlottende activa (Current assets) Voorraden (Inventories) Vorderingen (Receivables) Effecten (Securities) Liquide middelen (Cash) ───────────────────────────────────── PASSIVA (Equity and Liabilities) Eigen vermogen (Equity) Gestort en opgevraagd kapitaal (Share capital) Agio (Share premium) Wettelijke reserves (Statutory reserves) Overige reserves (Other reserves) Onverdeeld resultaat (Retained earnings) Voorzieningen (Provisions) Pensioenvoorzieningen Belastingvoorzieningen Overige voorzieningen Langlopende schulden (Long-term liabilities) Kortlopende schulden (Current liabilities) ```  _(BW2 Art. 2:364)_

## Section 8 -- Toelichting (Notes to Accounts)

**Toelichting (Notes to Accounts)**

| # | Disclosure | Micro | Small | Medium | Large |
| --- | --- | --- | --- | --- | --- |
| 1 | Accounting policies | Not required | Required | Required | Required |
| 2 | Fixed asset movements | Not required | Required (summary) | Required | Required |
| 3 | Maturity of long-term debts | Not required | Required | Required | Required |
| 4 | Contingent liabilities/guarantees | Required | Required | Required | Required |
| 5 | Related party transactions | Not required | Required (RJ 330) | Required | Required |
| 6 | Employee numbers | Not required | Average number | By category | By category |
| 7 | Directors' remuneration | Not required | Not required (small) | Required | Required |
| 8 | Auditor fees | Not required | Not required | Required | Required |
| 9 | Financial instruments | Not required | If applicable | Required | Required |
| 10 | Tax reconciliation | Not required | Not required | Required | Required |
| 11 | Statutory reserves specification | Not required | Required | Required | Required |
| 12 | Subsequent events | Not required | Required | Required | Required |

## Section 9 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Filing authority | Kamer van Koophandel (KvK) — Handelsregister |
| Filing method | SBR (Standard Business Reporting) via Digipoort — mandatory for most entities |
| Adoption deadline | 5 months after balance sheet date (extendable by shareholder resolution by further 5 months — max 10 months) |
| If not adopted in time | File draft accounts within 2 months of the 5+5 month deadline (i.e., max 12 months) |
| Filing deadline | 8 days after adoption (Art. 2:394) |
| Maximum from year-end | 12 months + 8 days (if full extension used) |
| Late filing consequence | Presumption of mismanagement by directors in case of bankruptcy (Art. 2:248) |
| No monetary fine | But exposure to personal liability is severe |
| Language | Dutch (English permitted for certain entities under specific conditions) |

### What must be filed by size

**What must be filed by size**

| Size | Documents to file (deponeren) |
| --- | --- |
| Micro | Balance sheet + limited notes only |
| Small | Balance sheet + abbreviated notes (no P&L, no management report) |
| Medium | Balance sheet + abridged P&L + notes + auditor's report |
| Large | Full accounts + management report + auditor's report |

## Section 10 -- Audit Requirements

**Audit Requirements**

| Category | Audit requirement |
| --- | --- |
| Micro entity | Exempt |
| Small entity (Art. 2:396) | Exempt |
| Medium entity (Art. 2:397) | Mandatory (Art. 2:393) |
| Large entity | Mandatory |
| Listed / Public Interest Entity (OOB) | Mandatory; AFM-registered auditor |
| 403-declaration entity | Exempt if parent guarantees liabilities and files consolidated accounts |

### Art. 2:403 Group exemption

- **Group exemption conditions** — A subsidiary may be exempt from filing individual accounts and audit if: Parent company issues a liability declaration (403-verklaring); Consolidated accounts are filed at KvK; Shareholders consent (or do not object within deadline).  _(Art. 2:403)_

### Auditor qualification

- **Auditor qualification** — Registeraccountant (RA) or Accountant-Administratieconsulent (AA) with audit authority, registered with the NBA (Koninklijke Nederlandse Beroepsorganisatie van Accountants). For OOB entities, auditor must hold AFM licence.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
