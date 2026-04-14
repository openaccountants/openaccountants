---
name: switzerland-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Swiss VAT return (MWST/TVA/IVA Abrechnung) for a self-employed individual or small business in Switzerland. Trigger on phrases like "prepare Swiss VAT return", "MWST Abrechnung", "Swiss VAT", "Saldosteuersatz", "Bezugsteuer", or any request involving Swiss VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Switzerland only and only the effektive Abrechnungsmethode (effective method). Saldosteuersatz (flat-rate), Pauschalsteuersatz, and Gruppenbesteuerung are in the refusal catalogue. Switzerland is NOT in the EU — there are no intra-community acquisitions. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). Do NOT load eu-vat-directive — it does not apply to Switzerland. ALWAYS read this skill before touching any Swiss VAT work.
version: 2.0
---

# Switzerland VAT Return Skill (MWST Abrechnung) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content. Do NOT load eu-vat-directive — Switzerland is not in the EU.**

| Field | Value |
|---|---|
| Country | Switzerland (Schweizerische Eidgenossenschaft) + Liechtenstein (customs union) |
| Standard rate | 8.1% |
| Reduced rate | 2.6% (food, non-alcoholic beverages, books, newspapers, medicines, seeds, plants, animal feed, fertilisers) |
| Special rate | 3.8% (accommodation/hotel services only) |
| Zero rate | **None — Switzerland does not have a zero rate. Exports and certain supplies are EXEMPT WITH CREDIT (Art. 23 MWSTG), not zero-rated.** |
| Return form | MWST-Abrechnung (Ziffern 200–910) |
| Filing portal | https://www.estv.admin.ch (ESTV SuisseTax / ePortal) |
| Authority | ESTV (Eidgenössische Steuerverwaltung) / AFC (Administration fédérale des contributions) |
| Currency | CHF (some transactions in EUR — convert) |
| Filing frequencies | Quarterly (standard); Half-yearly (by ESTV approval); Monthly (by election) |
| Deadline | 60 days after quarter end (i.e. end of May, Aug, Nov, Feb) |
| Bezugsteuer | Acquisition tax / reverse charge on services from abroad (Art. 45 MWSTG) — applies to ALL foreign services, not just EU |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (EU directive) | **NOT APPLICABLE — Switzerland is not in the EU** |
| Contributor | Open Accountants |
| Validated by | Pending — requires Swiss tax adviser validation |
| Validation date | Pending |

**CRITICAL: Switzerland is NOT in the EU.**
- There are NO intra-community acquisitions. ALL goods from ALL countries (including EU) are IMPORTS subject to import MWST at the border, collected by BAZG/OFDF.
- Bezugsteuer (acquisition tax / reverse charge) applies to services received from abroad under Art. 45 MWSTG — from any country, not just EU.
- Liechtenstein is in a customs union with Switzerland and treated as domestic territory.
- The EU VAT Directive does not apply. Do not load eu-vat-directive.

**Key MWST-Abrechnung Ziffern (boxes):**

| Ziffer | Meaning |
|---|---|
| 200 | Total turnover (Gesamtumsatz) |
| 205 | Non-taxable services (Art. 21), exempt (Art. 23), notional turnover |
| 220 | Exempt supplies with credit (exports, Art. 23) |
| 221 | Supplies to beneficiaries under Art. 107(1)(b) |
| 225 | Transfers under notification procedure (Art. 38) |
| 230 | Supplies abroad (place of supply not in Switzerland) |
| 235 | Reduction in tax base (discounts, returns, bad debts) |
| 280 | Other deductions |
| 289 | Net taxable turnover |
| 299 | **Taxable turnover** (289 minus exempt items) |
| 300 | Supplies at 8.1% — tax amount |
| 310 | Supplies at 2.6% — tax amount |
| 340 | Supplies at 3.8% — tax amount |
| 380 | Total tax on supplies (300+310+340) |
| 381 | Bezugsteuer (acquisition tax on services from abroad) |
| 382 | Total tax due (380+381) |
| 399 | **Total tax due** |
| 400 | Input tax on cost of materials and services (Vorsteuer auf Materialaufwand) |
| 405 | Input tax on investments and other operating costs (Investitionen) |
| 410 | Dé-taxation (Einlageentsteuerung — Art. 32) |
| 415 | Correction of input tax (mixed use, own use, Art. 33) |
| 420 | Reduction of input tax deduction (non-business, exempt, Art. 33) |
| 479 | **Total deductible input tax** |
| 500 | Amount owed to ESTV (if 399 > 479) |
| 510 | Credit balance (if 479 > 399) |
| 900 | Subsidies, tourist taxes, disposal charges, etc. |
| 910 | Other cash flows (securities, payments not representing consideration) |

**Conservative defaults — Switzerland-specific:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 8.1% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Switzerland |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Bezugsteuer (foreign service, Ziffer 381) |
| Unknown blocked-input status | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown whether export evidence exists | Domestic taxable (no export treatment) |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | CHF 5,000 |
| HIGH tax-delta on a single conservative default | CHF 300 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | CHF 8,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the quarter in CSV, PDF, or pasted text. Acceptable from: UBS, Credit Suisse (now UBS), ZKB (Zürcher Kantonalbank), PostFinance, Raiffeisen, BCGE, BCV, Migros Bank, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices (especially for exports and foreign services), purchase invoices for input tax claims above CHF 300, MWST-Nummer (UID), customs declarations (Veranlagungsverfügungen) for imports.

**Ideal** — complete invoice register, prior period MWST-Abrechnung, customs declaration register, Bezugsteuer journal.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement → hard stop. If bank statement only → reviewer brief warning.

### Switzerland-specific refusal catalogue

**R-CH-1 — Saldosteuersatz (flat-rate method).** *Trigger:* client uses the Saldosteuersatz (Art. 37 MWSTG) — turnover < CHF 5,005,000 and tax < CHF 103,000. *Message:* "Saldosteuersatz uses a simplified flat-rate calculation. This skill covers the effektive Abrechnungsmethode only. Please use a tax adviser for Saldosteuersatz."

**R-CH-2 — Pauschalsteuersatz.** *Trigger:* client uses Pauschalsteuersatz (local authorities, associations). *Message:* "Pauschalsteuersatz is a simplified method for specific entities. Out of scope."

**R-CH-3 — Gruppenbesteuerung (group taxation).** *Trigger:* client is part of a MWST group under Art. 13 MWSTG. *Message:* "Group taxation requires consolidation. Out of scope."

**R-CH-4 — Partial use / mixed-use apportionment.** *Trigger:* client uses assets for both business and non-business purposes, or makes both taxable and exempt supplies, with non-de-minimis exempt proportion. *Message:* "Mixed-use apportionment under Art. 30-33 MWSTG requires annual adjustment calculations. Please use a tax adviser."

**R-CH-5 — Margenbesteuerung (margin scheme).** *Trigger:* second-hand goods, art, antiques under margin scheme (Art. 24a MWSTG). *Message:* "Margin scheme requires transaction-level margin computation. Out of scope."

**R-CH-6 — Real estate option to tax (Option).** *Trigger:* commercial property where the owner opted to charge MWST. *Message:* "Real estate option to tax has complex entry/exit rules. Please use a tax adviser."

**R-CH-7 — Income tax instead of MWST.** *Trigger:* user asks about income tax. *Message:* "This skill handles MWST only."

**R-CH-8 — Below registration threshold.** *Trigger:* client has turnover below CHF 100,000 and is not voluntarily registered. *Message:* "Businesses with turnover below CHF 100,000 are not required to register for MWST unless they voluntarily opt in. If you are not registered, no MWST return is required."

---

## Section 3 — Supplier pattern library (the lookup table)

Match by case-insensitive substring. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Swiss banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| UBS | EXCLUDE for bank charges/fees | Financial service, exempt Art. 21 Abs. 2 Ziff. 19 MWSTG |
| CREDIT SUISSE, CS | EXCLUDE | Same (now part of UBS) |
| ZKB, ZÜRCHER KANTONALBANK | EXCLUDE | Same |
| POSTFINANCE | EXCLUDE for fees | Account fees exempt. Some postal services may be taxable. |
| RAIFFEISEN | EXCLUDE | Same |
| KANTONALBANK (any cantonal bank) | EXCLUDE | Same |
| MIGROS BANK | EXCLUDE | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscriptions |
| ZINS, INTEREST | EXCLUDE | Interest, out of scope |
| DARLEHEN, KREDIT, LOAN | EXCLUDE | Loan principal, out of scope |

### 3.2 Swiss government and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ESTV, EIDG. STEUERVERWALTUNG, AFC | EXCLUDE | Tax payment |
| MWST (as payment to ESTV) | EXCLUDE | VAT payment |
| BAZG, OFDF, ZOLL | EXCLUDE for duty | Customs duty. Import MWST goes to Ziffer 405 input. |
| AHV, AVS, IV, AUSGLEICHSKASSE | EXCLUDE | Social security contributions |
| BVG, PENSIONSKASSE | EXCLUDE | Pension fund |
| SUVA | EXCLUDE | Accident insurance (mandatory) |
| HANDELSREGISTER, REGIST DU COMMERCE | EXCLUDE | Registry fees |

### 3.3 Swiss utilities

| Pattern | Treatment | Ziffer | Notes |
|---|---|---|---|
| SWISSCOM | Domestic 8.1% | 400 (input) | Telecoms — overhead |
| SUNRISE, SALT, YALLO | Domestic 8.1% | 400 (input) | Mobile telecoms |
| EWZ, CKW, BKW, AEW, AXPO | Domestic 8.1% or 2.6% | 400 (input) | Electricity — check rate on invoice |
| SIG, GAZNAT | Domestic 8.1% or 2.6% | 400 (input) | Gas — check rate |
| WASSERVERSORGUNG, WATER | Domestic 2.6% | 400 (input) | Water supply at reduced rate |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MOBILIAR, ZURICH VERSICHERUNG, AXA SCHWEIZ | EXCLUDE | Insurance, exempt Art. 21 Abs. 2 Ziff. 18 |
| HELVETIA, BASLER, BÂLOISE, ALLIANZ SUISSE | EXCLUDE | Same |
| VERSICHERUNG, ASSURANCE, POLIZZA | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Ziffer | Notes |
|---|---|---|---|
| POST CH, DIE POST, LA POSTE | EXCLUDE for standard postage (letters under 50g) | | Universal postal service, exempt Art. 21 Abs. 2 Ziff. 1 |
| POST CH (parcels, express) | Domestic 8.1% | 400 | Non-universal services taxable |
| DPD CH, DHL SCHWEIZ, PLANZER | Domestic 8.1% | 400 | Courier, taxable |

### 3.6 Transport (Switzerland domestic)

| Pattern | Treatment | Ziffer | Notes |
|---|---|---|---|
| SBB, CFF, FFS | Domestic 8.1% | 400 | Rail at standard rate (Swiss transport is NOT reduced like in EU) |
| POSTAUTO | Domestic 8.1% | 400 | Bus at standard rate |
| ZVV, BVB, TPG, TL, BERNMOBIL | Domestic 8.1% | 400 | Local transport at 8.1% |
| TAXI | Domestic 8.1% | 400 | Taxi at 8.1% |
| SWISS, EASYJET CH (international) | Exempt with credit | 220 | International flights — exempt with credit (Art. 23 Abs. 2 Ziff. 8) |

**Note on Swiss transport:** Unlike the EU, Switzerland does NOT have a reduced rate for passenger transport. All domestic transport is at 8.1%.

### 3.7 Food retail and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| MIGROS | Default BLOCK | Supermarket — personal provisioning. If food for resale: 2.6% input. |
| COOP, COOP CITY | Default BLOCK | Same |
| DENNER, ALDI CH, LIDL CH, VOLG | Default BLOCK | Same |
| RESTAURANTS, CAFES, BARS | Default BLOCK | Business entertainment — Swiss law allows Vorsteuer deduction if genuinely business-related, but documentation required. Default: block. |

**Note on Swiss entertainment:** Switzerland allows input tax deduction on business entertainment if properly documented with business purpose (Geschäftliche Bewirtung). There is no hard block. However, excessive or personal entertainment is not deductible. Default: block. [T2] flag if documented.

### 3.8 SaaS — foreign suppliers (ALL are Bezugsteuer — Art. 45 MWSTG)

**In Switzerland, ALL foreign services (EU and non-EU alike) trigger Bezugsteuer.** There is no EU/non-EU distinction for the Abrechnung. All go to Ziffer 381.

| Pattern | Billing entity | Ziffer | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | 381 (Bezugsteuer) / 400 (input) | Foreign service — Bezugsteuer |
| MICROSOFT (365, Azure) | Microsoft Ireland (IE) | 381 / 400 | Bezugsteuer |
| ADOBE | Adobe Ireland (IE) | 381 / 400 | Bezugsteuer |
| META, FACEBOOK ADS | Meta Ireland (IE) | 381 / 400 | Bezugsteuer |
| LINKEDIN | LinkedIn Ireland (IE) | 381 / 400 | Bezugsteuer |
| SPOTIFY | Spotify AB (SE) | 381 / 400 | Bezugsteuer |
| DROPBOX | Dropbox Ireland (IE) | 381 / 400 | Bezugsteuer |
| SLACK | Slack Ireland (IE) | 381 / 400 | Bezugsteuer |
| ATLASSIAN | Atlassian BV (NL) | 381 / 400 | Bezugsteuer |
| ZOOM | Zoom Ireland (IE) | 381 / 400 | Bezugsteuer |
| NOTION | Notion Labs Inc (US) | 381 / 400 | Bezugsteuer |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 381 / 400 | Bezugsteuer |
| OPENAI, CHATGPT | OpenAI Inc (US) | 381 / 400 | Bezugsteuer |
| GITHUB | GitHub Inc (US) | 381 / 400 | Bezugsteuer |
| FIGMA | Figma Inc (US) | 381 / 400 | Bezugsteuer |
| CANVA | Canva Pty Ltd (AU) | 381 / 400 | Bezugsteuer |
| AWS | AWS EMEA SARL (LU) | 381 / 400 | Bezugsteuer (LU is foreign to CH) |
| STRIPE (subscription) | Stripe IE | 381 / 400 | Bezugsteuer. Transaction fees: see 3.10. |

**IMPORTANT: Bezugsteuer threshold.** Art. 45 Abs. 2 MWSTG: Bezugsteuer is only due if the total value of services received from abroad exceeds CHF 10,000 per year. Below this threshold, no Bezugsteuer obligation. Default: assume threshold is exceeded if any Bezugsteuer items are present.

### 3.9 SaaS — Swiss suppliers (domestic)

| Pattern | Treatment | Ziffer | Notes |
|---|---|---|---|
| INFOMANIAK | Domestic 8.1% | 400 | Swiss hosting company |
| CYON | Domestic 8.1% | 400 | Swiss hosting |
| THREEMA | Domestic 8.1% | 400 | Swiss messaging |
| PROTON, PROTONMAIL, PROTON VPN | Domestic 8.1% | 400 | Swiss — check if invoice shows MWST |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing exempt financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| TWINT (merchant fees) | Check invoice | Swiss payment system — fees may be exempt |
| SIX PAYMENT SERVICES | Check invoice | Acquirer fees — likely exempt |

### 3.11 Professional services (Switzerland)

| Pattern | Treatment | Ziffer | Notes |
|---|---|---|---|
| RECHTSANWALT, ADVOKAT, ANWALT | Domestic 8.1% | 400 | Legal — deductible if business |
| TREUHÄNDER, TREUHAND, REVISOR | Domestic 8.1% | 400 | Accountant/trustee — always deductible |
| NOTAR | Domestic 8.1% | 400 | Notary |
| HANDELSREGISTERAMT | EXCLUDE | Government fee |

### 3.12 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| AHV/IV, AVS/AI, AUSGLEICHSKASSE | EXCLUDE | Social security (1st pillar) |
| BVG, LPP, PENSIONSKASSE | EXCLUDE | Pension (2nd pillar) |
| SUVA, UVG | EXCLUDE | Accident insurance |
| LOHN, SALAIRE, GEHALT (outgoing) | EXCLUDE | Wages |
| QUELLENSTEUER | EXCLUDE | Withholding tax on foreign workers |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| MIETE, LOYER (commercial, with MWST) | Domestic 8.1% | Commercial lease where landlord opted for MWST (Art. 22 MWSTG) |
| MIETE, LOYER (residential, no MWST) | EXCLUDE | Residential lease, exempt Art. 21 Abs. 2 Ziff. 21 |
| NEBENKOSTEN, CHARGES | Check invoice | Ancillary costs — may include taxable and exempt items |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| ÜBERTRAG, EIGENES KONTO, INTERN | EXCLUDE | Internal movement |
| DIVIDENDE | EXCLUDE | Dividend, out of scope |
| DARLEHEN, RÜCKZAHLUNG | EXCLUDE | Loan repayment |
| BARGELDBEZUG, BANCOMAT, ATM | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

Six fully worked classifications from a hypothetical Swiss self-employed IT consultant.

### Example 1 — Foreign SaaS, Bezugsteuer (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; CHF 13.92`

**Reasoning:**
US entity. Foreign service → Bezugsteuer under Art. 45 MWSTG. Report 8.1% on CHF 13.92 = CHF 1.13 in Ziffer 381 (tax due). Same CHF 1.13 as input tax in Ziffer 400. Net effect zero for fully taxable business. Note: same treatment whether supplier is EU or non-EU — Switzerland does not distinguish.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ziffer (output) | Ziffer (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -13.92 | -13.92 | 1.13 | 8.1% | 381 | 400 | N | — | — |

### Example 2 — Foreign SaaS, EU entity (Google — still Bezugsteuer)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April ; -850.00 ; CHF`

**Reasoning:**
Google Ireland is an IE entity — but Switzerland is NOT in the EU. This is a foreign service. Bezugsteuer applies exactly the same as for a US entity. CHF 850 in Ziffer 381, 8.1% = CHF 68.85. Input tax CHF 68.85 in Ziffer 400.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ziffer (output) | Ziffer (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 68.85 | 8.1% | 381 | 400 | N | — | — |

### Example 3 — Business entertainment, default block

**Input line:**
`15.04.2026 ; RESTAURANT KRONENHALLE ; DEBIT ; Client dinner ; -420.00 ; CHF`

**Reasoning:**
Restaurant. Swiss law allows Vorsteuer deduction on genuine business entertainment (Geschäftliche Bewirtung), unlike Malta's hard block. But documentation required (attendees, business purpose). Default: block. [T2] flag.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ziffer | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | RESTAURANT KRONENHALLE | -420.00 | -420.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked by default — deductible if documented business purpose" |

### Example 4 — Domestic purchase at standard rate

**Input line:**
`18.04.2026 ; DIGITEC GALAXUS ; DEBIT ; Laptop Dell XPS 15 ; -1,595.00 ; CHF`

**Reasoning:**
Swiss electronics retailer. CHF 1,595 incl. 8.1% MWST. Net = CHF 1,595 / 1.081 = CHF 1,475.49. MWST = CHF 119.51. Input tax in Ziffer 405 (investment/other operating cost) if capital item, or Ziffer 400 if overhead. For a laptop, likely Ziffer 405.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ziffer | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | DIGITEC GALAXUS | -1,595.00 | -1,475.49 | -119.51 | 8.1% | 405 | N | — | — |

### Example 5 — Export service sale (B2B foreign client)

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice CH-2026-018 IT consultancy March ; +3,500.00 ; CHF`

**Reasoning:**
Incoming from German company. IT consulting services to a foreign client. Place of supply: recipient's domicile (Germany) under Art. 8 Abs. 1 MWSTG — service is NOT subject to Swiss MWST. Report in Ziffer 230 (Leistungen im Ausland). No output tax. The invoice must state "Leistung nicht der schweizerischen MWST unterliegend" or equivalent.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ziffer | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | n/a | 230 | N | — | — |

### Example 6 — Import of goods (customs)

**Input line:**
`28.04.2026 ; BAZG/OFDF ; DEBIT ; Import MWST Veranlagungsverfügung 2026-1234 ; -162.00 ; CHF`

**Reasoning:**
Import MWST paid at customs. This is a payment to BAZG (Federal Customs). The Veranlagungsverfügung (customs assessment) shows the MWST amount. CHF 162 is the import MWST paid. This can be claimed as input tax in Ziffer 405 (if it's a business purchase). The underlying goods value is on the customs declaration.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Ziffer | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | BAZG/OFDF | -162.00 | 0 | -162.00 | 8.1% | 405 | N | — | "Import MWST — verify Veranlagungsverfügung" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 8.1% (Art. 25 Abs. 1 MWSTG)

Default rate. Sales → Ziffer 300 (tax amount), included in Ziffer 200/299. Purchases → Ziffer 400 (materials/services) or 405 (investments/other operating costs).

### 5.2 Reduced rate 2.6% (Art. 25 Abs. 2 MWSTG, Art. 25 Abs. 2bis)

Food and non-alcoholic beverages (NOT restaurant meals — those are 8.1%), books, newspapers, periodicals, electronic publications (from 2018), medicines, seeds, plants, animal feed, fertilisers, water supply. Sales → Ziffer 310.

### 5.3 Special rate 3.8% (Art. 25 Abs. 4 MWSTG)

Hotel accommodation (Beherbergungsleistungen) ONLY. Includes room + breakfast if included in room rate. Meals served separately are at 8.1%. Sales → Ziffer 340.

### 5.4 Exempt with credit (Art. 23 MWSTG)

Exports of goods (Art. 23 Abs. 2 Ziff. 1 — requires customs export declaration). Services to foreign recipients where place of supply is abroad (Art. 8 Abs. 1 — recipient principle for services). International transport (Art. 23 Abs. 2 Ziff. 8). → Ziffer 220 or 230. Input tax remains deductible.

### 5.5 Exempt without credit (Art. 21 MWSTG)

Medical/dental, social care, education, cultural/sporting events (certain), financial services, insurance, real estate (residential rent, sale), gambling, postal universal service (<50g letters). If significant → **R-CH-4 fires**.

### 5.6 Bezugsteuer — services from abroad (Art. 45 MWSTG)

ALL services received from foreign suppliers (EU and non-EU alike): compute MWST at applicable rate (usually 8.1%) on the service value. Report in Ziffer 381 (tax due). Deduct same amount in Ziffer 400 (input tax) if purchase is for taxable business activity. Net effect zero for fully taxable business. **Threshold: CHF 10,000/year aggregate — below this, no Bezugsteuer obligation.**

### 5.7 Import of goods

ALL goods from ALL countries are imports. Import MWST is assessed by BAZG at the border. Rates: 8.1% (standard), 2.6% (reduced for food etc.). The Veranlagungsverfügung is the deduction document. Input tax → Ziffer 405.

### 5.8 Blocked / restricted input tax

- Private use: fully blocked (eigenverbrauch adjustment via Ziffer 415/420)
- Entertainment: deductible if genuinely business-related, but documentation required. No hard block. Default: block.
- Motor vehicles: no hard block in Switzerland. Business use proportion deductible. Private portion must be adjusted via Ziffer 415/420 (ESTV uses lump-sum private share of 0.9% of vehicle purchase price per month, or 9.6% per year).
- Tobacco, alcohol: no specific statutory block for input tax (unlike Malta/Germany). But if for personal consumption, blocked as private use.
- Gifts to staff and business partners: deductible up to CHF 500 per person per year.
- Real estate for residential use: blocked (exempt supply).

### 5.9 Input tax split — Ziffer 400 vs 405

Ziffer 400: input tax on Materialaufwand und Dienstleistungen (cost of materials and services — operational expenses). Ziffer 405: input tax on Investitionen und übriger Betriebsaufwand (investments and other operating costs — capital/fixed assets, rent, utilities). The distinction matters for ESTV statistics but both are fully deductible.

### 5.10 Eigenverbrauch (own use / deemed supply — Art. 31 MWSTG)

Withdrawal of goods or services for non-business purposes triggers deemed supply. Must be accounted at market value. Report as output tax. For motor vehicles, ESTV applies the 0.9%/month lump sum.

### 5.11 Sales — domestic

Charge 8.1%, 2.6%, or 3.8% as applicable. Report in Ziffer 200 (total turnover) and 300/310/340 (tax).

### 5.12 Sales — foreign (services)

If place of supply is abroad (recipient principle, Art. 8 Abs. 1): no Swiss MWST. Report in Ziffer 230. Input tax remains deductible.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs

*Pattern:* Migrol, BP Schweiz, Shell CH, SOCAR, Avia. *Default:* 0% if vehicle use unclear. *Question:* "Business vehicle or personal? What business-use proportion? (ESTV lump-sum: 0.9%/month of purchase price for private share.)"

### 6.2 Entertainment

*Default:* block. *Question:* "Documented business purpose with attendees?"

### 6.3 Ambiguous foreign SaaS

*Default:* Bezugsteuer Ziffer 381/400. *Question:* "Confirm foreign entity. If Swiss entity, domestic 8.1%."

### 6.4 Round-number owner transfers

*Default:* exclude. *Question:* "Customer payment, capital, or loan?"

### 6.5 Incoming from individuals

*Default:* domestic 8.1%, Ziffer 200/300. *Question:* "Sale? What was supplied?"

### 6.6 Foreign counterparty incoming

*Default:* check if service is supplied abroad (Ziffer 230) or domestic. *Question:* "Where is the customer located? What service was provided?"

### 6.7 Large one-off purchases

*Default:* Ziffer 405. *Question:* "Confirm invoice amount."

### 6.8 Mixed-use phone/internet

*Default:* 0% if mixed. *Question:* "Dedicated business line? Business percentage?"

### 6.9 Outgoing to individuals

*Default:* exclude as drawings. *Question:* "Contractor, wages, refund, or personal?"

### 6.10 Cash withdrawals

*Default:* exclude. *Question:* "What was cash used for?"

### 6.11 Rent payments

*Default:* no MWST (residential). *Question:* "Commercial with MWST (Option nach Art. 22)?"

### 6.12 Foreign hotel

*Default:* exclude from input tax (foreign VAT not recoverable). *Question:* "Business trip?"

### 6.13 Bezugsteuer threshold check

*Pattern:* multiple small foreign services. *Default:* assume threshold exceeded. *Question:* "Total foreign services for the year — above or below CHF 10,000?"

### 6.14 Import vs Bezugsteuer classification

*Pattern:* foreign purchase that could be goods (import MWST via BAZG) or services (Bezugsteuer). *Default:* Bezugsteuer (services). *Question:* "Was this a physical good imported through customs, or a service?"

---

## Section 7 — Excel working paper template (Switzerland-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Switzerland-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Ziffer") accepts valid Ziffer codes from Section 1.

### Sheet "Box Summary"

```
Turnover:
| 200 | Total turnover | =SUM of all sales |
| 220 | Exempt with credit (exports) | =SUMIFS(...) |
| 230 | Supplies abroad | =SUMIFS(...) |
| 289 | Net taxable turnover | =C[200]-C[205]-C[220]-C[225]-C[230]-C[235]-C[280] |

Tax on supplies:
| 300 | Tax at 8.1% | =taxable base at 8.1% * 0.081 |
| 310 | Tax at 2.6% | =taxable base at 2.6% * 0.026 |
| 340 | Tax at 3.8% | =taxable base at 3.8% * 0.038 |
| 380 | Total tax on supplies | =C[300]+C[310]+C[340] |
| 381 | Bezugsteuer | =SUM of Bezugsteuer items * 0.081 |
| 399 | Total tax due | =C[380]+C[381] |

Input tax:
| 400 | Input tax on materials/services | =SUMIFS(...) |
| 405 | Input tax on investments/operating | =SUMIFS(...) |
| 479 | Total deductible input tax | =C[400]+C[405]+C[410]-C[415]-C[420] |

Bottom line:
| 500 | Amount owed | =IF(C[399]>C[479], C[399]-C[479], 0) |
| 510 | Credit balance | =IF(C[479]>C[399], C[479]-C[399], 0) |
```

### Mandatory recalc step

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/switzerland-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Switzerland bank statement reading guide

**CSV format conventions.** UBS exports use semicolons with DD.MM.YYYY dates. PostFinance uses tab-separated. ZKB uses semicolons. Common columns: Datum/Date, Buchungstext/Text, Betrag/Montant, Saldo/Solde.

**Multilingual descriptions.** Switzerland has four languages. Common variants: Miete/Loyer/Affitto (rent), Lohn/Salaire/Salario (salary), Zins/Intérêt/Interesse (interest), Überweisung/Virement/Bonifico (transfer). Treat as English equivalents.

**Internal transfers.** Labelled "Umbuchung", "Eigenkonto", "Intern". Always exclude.

**Owner draws.** Einzelunternehmen (sole trader) transfers to personal account are Privatbezüge — exclude.

**Refunds.** Identify by "Gutschrift", "Rückerstattung", "Stornierung". Book as negative.

**Currency.** Most transactions in CHF. EUR transactions are common for international suppliers. Convert at the transaction date rate from SNB (Swiss National Bank) or the bank statement rate. For Bezugsteuer valuation, use the rate on the invoice date.

**IBAN prefix.** CH = Switzerland. LI = Liechtenstein (domestic). DE, FR, IT, AT = EU (foreign for Swiss purposes). US, GB = non-EU.

**Import MWST.** BAZG Veranlagungsverfügungen are the deduction document for import MWST. Match customs declarations to bank debits from BAZG. The MWST amount on the Veranlagungsverfügung is the deductible input tax, NOT the bank debit (which includes duties).

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference rule:* Einzelunternehmen vs GmbH vs AG vs Kollektivgesellschaft. *Fallback:* "Are you Einzelunternehmen (sole trader), GmbH, AG, or other?"

### 9.2 MWST registration and method
*Inference rule:* if asking for Abrechnung, they are registered. *Fallback:* "Effektive Methode or Saldosteuersatz?" *If Saldosteuersatz → R-CH-1 fires.*

### 9.3 UID (MWST-Nummer)
*Fallback:* "What is your UID / MWST-Nummer? (CHE-xxx.xxx.xxx MWST)"

### 9.4 Filing period
*Fallback:* "Quarterly, half-yearly, or monthly? Which period?"

### 9.5 Industry
*Fallback:* "What does the business do?"

### 9.6 Employees
*Inference rule:* AHV, Lohn outgoing. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Fallback:* "Do you make MWST-exempt sales?" *If yes → R-CH-4 may fire.*

### 9.8 Foreign services aggregate
*Fallback:* "Do your total foreign service purchases exceed CHF 10,000/year? (Bezugsteuer threshold)"

### 9.9 Foreign customers
*Fallback:* "Do you provide services to customers abroad?"

### 9.10 Vehicle
*Fallback:* "Business vehicle? What private-use proportion?"

---

## Section 10 — Reference material

### Validation status

v2.0, rewritten April 2026. Awaiting validation by Swiss licensed tax adviser.

### Sources

1. MWSTG (SR 641.20) — https://www.admin.ch/opc/de/classified-compilation/20081110/
2. MWSTV (SR 641.201) — implementing ordinance
3. ESTV Praxisfestlegungen — https://www.estv.admin.ch
4. ESTV MWST-Info publications (especially MWST-Info 08 — Bezugsteuer)
5. BAZG customs/import documentation
6. SNB exchange rates — https://www.snb.ch

### Known gaps

1. Saldosteuersatz is entirely excluded — covers a large number of Swiss small businesses.
2. Bezugsteuer CHF 10,000 threshold is annual aggregate — mid-year it may not be clear whether threshold will be reached. Default: assume exceeded.
3. Vehicle private-use lump sum (0.9%/month) may be updated by ESTV — verify annually.
4. The distinction between Ziffer 400 and 405 is not always clear-cut — the skill provides guidance but the allocation is ultimately an accounting judgement.
5. Import MWST via BAZG requires matching customs declarations to bank debits, which cannot always be done from bank data alone.
6. Liechtenstein is treated as domestic but suppliers there may have different UID formats.

### Change log

- **v2.0 (April 2026):** Full rewrite to three-tier Accora architecture (without eu-vat-directive, as Switzerland is not in the EU).
- **v1.0 (April 2026):** Initial draft. Standalone document.

### Self-check (v2.0)

1. Quick reference with Ziffer table and conservative defaults: yes (Section 1).
2. Supplier library with Swiss patterns (including multilingual): yes (Section 3, 14 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 12 rules).
5. Tier 2 catalogue: yes (Section 6, 14 items).
6. Excel template with recalc: yes (Section 7).
7. Onboarding as fallback: yes (Section 9, 10 items).
8. All 8 Switzerland-specific refusals: yes (R-CH-1 through R-CH-8).
9. Reference material at bottom: yes (Section 10).
10. NOT-EU status emphasized: yes (Section 1, throughout).
11. Three rates (8.1%/2.6%/3.8%) correctly mapped: yes.
12. Bezugsteuer applies to ALL foreign services (EU and non-EU): yes (Section 3.8, Examples 1-2, Section 5.6).
13. Bezugsteuer CHF 10,000 threshold documented: yes (Section 3.8, Section 5.6).
14. Import MWST via BAZG documented: yes (Section 5.7, Example 6).
15. No zero rate — exempt with credit instead: yes (Section 1).


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
