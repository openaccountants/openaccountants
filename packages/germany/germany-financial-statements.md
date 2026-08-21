---
name: germany-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (Jahresabschluss) for a German company. Trigger on phrases like "Jahresabschluss", "HGB", "Handelsgesetzbuch", "Bundesanzeiger", "Unternehmensregister", "Offenlegung", "Bilanz", "GuV", "GmbH accounts", "Kapitalgesellschaft", "audit Germany", "Kleinstkapitalgesellschaft", "kleine Kapitalgesellschaft", or any question about preparing and filing statutory accounts under German commercial law. Covers HGB frameworks, size thresholds, required statements, formats, notes, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: DE
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Germany Financial Statements

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Germany (Bundesrepublik Deutschland) |
| Currency | EUR |
| Filing authority | Unternehmensregister (Company Register) — formerly Bundesanzeiger |
| Primary legislation | Handelsgesetzbuch (HGB), §§ 242–342e |
| Supporting legislation | GmbHG; AktG; PublG (Publizitätsgesetz) |
| Accounting standards | HGB (German GAAP); IFRS permitted for consolidated accounts of listed companies |
| Financial year | Any 12-month period (calendar year most common) |
| Filing deadline | 12 months from balance sheet date |
| Late filing penalty | EUR 2,500 minimum (Ordnungsgeld); up to EUR 25,000 per offence |
| Digital filing | Electronic submission via publikations-plattform.de |

## Section 2 -- Reporting Framework

**Reporting Framework**

| Entity type | Applicable standard |
| --- | --- |
| Kapitalgesellschaften (GmbH, AG, KGaA) | HGB §§ 264–335 |
| Personenhandelsgesellschaften (OHG, KG without natural person as general partner) | HGB §§ 264a–264c |
| Listed companies (consolidated) | IFRS as adopted by the EU (mandatory) |
| Listed companies (individual) | HGB (mandatory); supplementary IFRS for information |
| Einzelkaufleute below thresholds | Simplified per § 241a HGB (no publication if turnover ≤ EUR 800,000 and profit ≤ EUR 80,000) |

## Section 3 -- Size Thresholds

Effective for financial years beginning on or after 1 January 2024 (§§ 267, 267a HGB):

**Size Thresholds**  _(§§ 267, 267a HGB)_

| Criterion | Kleinst (Micro) § 267a | Klein (Small) § 267(1) | Mittelgroß (Medium) § 267(2) | Groß (Large) |
| --- | --- | --- | --- | --- |
| Bilanzsumme (Balance sheet total) | ≤ EUR 450,000 | ≤ EUR 7,500,000 | ≤ EUR 25,000,000 | > EUR 25,000,000 |
| Umsatzerlöse (Revenue) | ≤ EUR 900,000 | ≤ EUR 15,000,000 | ≤ EUR 50,000,000 | > EUR 50,000,000 |
| Arbeitnehmer (Employees) | ≤ 10 | ≤ 50 | ≤ 250 | > 250 |

- **Size classification rule** — Classification requires that a company does not exceed 2 out of 3 thresholds on balance sheet dates of two consecutive financial years.  _(§§ 267, 267a HGB)_

## Section 4 -- Required Financial Statements

**Required Financial Statements**

| Document | Kleinst | Klein | Mittelgroß | Groß |
| --- | --- | --- | --- | --- |
| Bilanz (Balance sheet) | Required (abridged) | Required (abridged) | Required (full) | Required (full) |
| GuV (Profit and loss) | Required (abridged) | Required (abridged) | Required (full) | Required (full) |
| Anhang (Notes) | Not required | Required (reduced) | Required | Required (full) |
| Lagebericht (Management report) | Not required | Not required | Required | Required |
| Kapitalflussrechnung (Cash flow statement) | Not required | Not required | Not required | Required |
| Eigenkapitalspiegel (Statement of changes in equity) | Not required | Not required | Not required | Required |

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | Germany-specific notes |
| --- | --- | --- |
| 1 | Depreciation (planmäßige AfA) | § 253(3) HGB; straight-line over useful life; tax depreciation (AfA-Tabellen) often applied |
| 2 | Accruals (Rückstellungen) | § 249 HGB; mandatory for uncertain liabilities, pending losses, maintenance |
| 3 | Prepayments (RAP) | § 250 HGB; Rechnungsabgrenzungsposten on both sides |
| 4 | Provisions for pensions | § 253(1) HGB; discounted at average market rate (10-year Bundesbank rate) |
| 5 | Bad debts (Wertberichtigung) | Individual and general allowances; strict impairment test |
| 6 | Inventory (Vorräte) | Lower of cost/market principle (§ 253(4)); FIFO, LIFO, or weighted average permitted |
| 7 | Deferred tax (latente Steuern) | § 274 HGB; temporary differences approach; option for small companies |
| 8 | Foreign currency | § 256a HGB; closing rate for monetary items; unrealised gains limited to 1 year |
| 9 | Impairment (außerplanmäßige AfA) | § 253(3) sentence 5–6; mandatory for permanent, optional for temporary impairment |
| 10 | Anniversary provisions (Jubiläumsrückstellungen) | Required when legally or contractually committed |
| 11 | Tax provisions | Gewerbesteuer and Körperschaftsteuer provisions |
| 12 | Construction contracts | Percentage-of-completion not allowed under HGB (completed contract only) |

## Section 6 -- Profit and Loss Account Format (GuV)

- **Gesamtkostenverfahren format (§ 275 HGB)** — § 275 HGB provides two formats. Gesamtkostenverfahren (by nature — most common): ``` 1.  Umsatzerlöse (Revenue) 2.  Erhöhung/Verminderung des Bestands (Change in inventories of FG/WIP) 3.  Andere aktivierte Eigenleistungen (Own work capitalised) 4.  Sonstige betriebliche Erträge (Other operating income) 5.  Materialaufwand (Cost of materials) a) Roh-, Hilfs- und Betriebsstoffe b) Bezogene Leistungen 6.  Personalaufwand (Personnel expenses) a) Löhne und Gehälter b) Soziale Abgaben 7.  Abschreibungen (Depreciation/amortisation) 8.  Sonstige betriebliche Aufwendungen (Other operating expenses) ─── Betriebsergebnis (Operating result) ─── 9.  Erträge aus Beteiligungen (Income from investments) 10. Erträge aus Wertpapieren (Income from securities) 11. Sonstige Zinsen und ähnliche Erträge (Interest income) 12. Abschreibungen auf Finanzanlagen (Write-downs on financial assets) 13. Zinsen und ähnliche Aufwendungen (Interest expense) ─── Finanzergebnis ─── 14. Steuern vom Einkommen und Ertrag (Income taxes) 15. Ergebnis nach Steuern (Result after tax) 16. Sonstige Steuern (Other taxes) 17. Jahresüberschuss/Jahresfehlbetrag (Net profit/loss) ```  _(§ 275 HGB)_

## Section 7 -- Balance Sheet Format (Bilanz)

- **Bilanz format** — § 266 HGB — Kontoform (T-account) or Staffelform (vertical): ``` AKTIVA (Assets) A. Anlagevermögen (Fixed assets) I.   Immaterielle Vermögensgegenstände (Intangible assets) II.  Sachanlagen (Tangible assets) III. Finanzanlagen (Financial assets) B. Umlaufvermögen (Current assets) I.   Vorräte (Inventories) II.  Forderungen und sonstige Vermögensgegenstände (Receivables) III. Wertpapiere (Securities) IV.  Kassenbestand, Guthaben bei Kreditinstituten (Cash) C. Rechnungsabgrenzungsposten (Prepaid expenses) D. Aktive latente Steuern (Deferred tax assets) E. Aktiver Unterschiedsbetrag aus Vermögensverrechnung ───────────────────────────────────────── PASSIVA (Equity and Liabilities) A. Eigenkapital (Equity) I.   Gezeichnetes Kapital (Subscribed capital) II.  Kapitalrücklage (Capital reserves) III. Gewinnrücklagen (Revenue reserves) IV.  Gewinn-/Verlustvortrag (Retained profits/losses) V.   Jahresüberschuss/Jahresfehlbetrag (Net profit/loss) B. Rückstellungen (Provisions) C. Verbindlichkeiten (Liabilities) D. Rechnungsabgrenzungsposten (Deferred income) E. Passive latente Steuern (Deferred tax liabilities) ```  _(§ 266 HGB)_

## Section 8 -- Notes to Accounts (Anhang)

**Notes to Accounts (Anhang)**

| # | Disclosure | Klein | Mittelgroß | Groß |
| --- | --- | --- | --- | --- |
| 1 | Accounting policies | Required | Required | Required |
| 2 | Fixed asset movements (Anlagenspiegel) | Not required to file | Required | Required |
| 3 | Maturity analysis of liabilities | Required (simplified) | Required | Required |
| 4 | Secured liabilities | Required | Required | Required |
| 5 | Related party transactions | Not required | Not required | Required (§ 285 Nr. 21) |
| 6 | Employee numbers | Average only | By category | By category |
| 7 | Directors' and supervisory board remuneration | Not required | Required | Required |
| 8 | Contingent liabilities (Haftungsverhältnisse) | Required | Required | Required |
| 9 | Off-balance sheet arrangements | Not required | Required | Required |
| 10 | Auditor fees | Not required | Not required | Required |
| 11 | Subsidiaries/investments | Required (name, seat, share) | Required (full) | Required (full) |
| 12 | Deferred tax explanation | Not required | Required | Required |

## Section 9 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Filing authority | Unternehmensregister (via publikations-plattform.de) |
| Method | Electronic XML/XBRL submission |
| Filing deadline | 12 months from balance sheet date |
| Operator verification | Bundesanzeiger Verlag checks completeness and timeliness |
| Enforcement | Bundesamt für Justiz (BfJ) issues Ordnungsgeldverfahren |
| Minimum penalty | EUR 2,500 per infringement |
| Maximum penalty | EUR 25,000 per infringement (repeated: up to EUR 25,000 each time) |

### What must be filed (Offenlegung) by size

**What must be filed (Offenlegung) by size**

| Size | Documents to disclose |
| --- | --- |
| Kleinst (Micro) | Bilanz only (Hinterlegung — deposit, not publication) |
| Klein (Small) | Bilanz + Anhang (abbreviated); no GuV required |
| Mittelgroß (Medium) | Bilanz + GuV (abbreviated) + Anhang + Lagebericht |
| Groß (Large) | Full Jahresabschluss + Lagebericht + Prüfungsbericht |

## Section 10 -- Audit Requirements

**Audit Requirements**

| Category | Audit requirement |
| --- | --- |
| Kleinstkapitalgesellschaft (Micro) | Exempt |
| Kleine Kapitalgesellschaft (Small) | Exempt |
| Mittelgroße Kapitalgesellschaft (Medium) | Mandatory statutory audit (Jahresabschlussprüfung) |
| Große Kapitalgesellschaft (Large) | Mandatory statutory audit |
| Listed companies (kapitalmarktorientiert) | Mandatory; APAS oversight |
| PublG companies (exceed PublG thresholds) | Mandatory regardless of legal form |

### PublG Thresholds (Publizitätsgesetz)

- **PublG applicability thresholds** — Applies to all enterprises (including sole traders, partnerships) exceeding 2 of 3 for three consecutive years: Balance sheet total > EUR 65,000,000; Revenue > EUR 130,000,000; Employees > 5,000  _(Publizitätsgesetz (PublG))_

### Auditor qualification

- **Auditor qualification** — Wirtschaftsprüfer (WP) or Wirtschaftsprüfungsgesellschaft registered with the Wirtschaftsprüferkammer (WPK). Vereidigte Buchprüfer may audit medium-sized GmbHs.  _(Wirtschaftsprüferkammer (WPK))_

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
