---
name: finland-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Finland VAT return (ALV-ilmoitus) for any client. Trigger on phrases like "prepare VAT return", "do the ALV", "fill in ALV", "Finnish VAT", "OmaVero", or any request involving Finland VAT filing. This skill covers Finland only and standard ALV registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Finnish VAT work.
version: 2.0
---

# Finland VAT Return Skill (ALV-ilmoitus) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1.**

| Field | Value |
|---|---|
| Country | Finland (Suomi) |
| Standard rate | 25.5% (from 1 September 2024; was 24%) |
| Reduced rates | 13.5% (was 14%: food, restaurant/catering, animal feed), 10% (books, newspapers, medicines, passenger transport, accommodation, cultural/sporting events) |
| Zero rate | 0% (exports, intra-EU B2B supplies, international transport) |
| Return form | ALV-ilmoitus (Arvonlisaveroilmoitus) |
| Filing portal | https://www.vero.fi/omavero (OmaVero / MyTax) |
| Authority | Verohallinto (Finnish Tax Administration / Vero Skatt) |
| Currency | EUR only |
| Filing frequencies | Monthly (turnover > EUR 100,000); Quarterly (EUR 30,001-100,000); Annual (<= EUR 30,000) |
| Deadline | Monthly: 12th of 2nd month after period. Quarterly: 12th of 2nd month after quarter. |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key ALV-ilmoitus field codes:**

| Code | Meaning |
|---|---|
| 301 | Domestic sales 25.5% — base |
| 302 | Domestic sales 13.5% — base |
| 303 | Domestic sales 10% — base |
| 305 | Output ALV on 25.5% sales |
| 306 | Output ALV on 13.5% sales |
| 318 | Output ALV on 10% sales |
| 309 | Intra-EU acquisition of goods — base (reverse charge) |
| 313 | EU services received (reverse charge) — base |
| 319 | Non-EU services received (reverse charge) — base |
| 320 | Construction reverse charge — base |
| 310 | Domestic exempt sales (without credit) |
| 311 | Intra-EU supply of goods |
| 312 | Intra-EU supply of services (B2B) |
| 314 | Exports to non-EU |
| 307 | Total deductible input ALV (single aggregate) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 25.5% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Finland |
| Unknown B2B vs B2C for EU customer | B2C, charge 25.5% |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 3,000 |
| HIGH tax-delta on single default | EUR 200 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net ALV position | EUR 5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: Nordea Finland, OP (Osuuspankki), Danske Bank Finland, S-Pankki, Handelsbanken FI, Aktia, Revolut Business, Wise Business.

**Recommended** — sales/purchase invoices, Y-tunnus (business ID), FI VAT number (FI + 8 digits), prior ALV-ilmoitus.

**Ideal** — complete register, prior period reconciliation, Aland Islands trade records if applicable.

### Finland-specific refusal catalogue

**R-FI-1 — Non-registered below threshold.** *Trigger:* turnover below EUR 15,000 (from 2025), not registered. *Message:* "Non-registered entities do not file ALV returns."

**R-FI-2 — Partial exemption.** *Trigger:* mixed supplies. *Message:* "Partial exemption under AVL Section 117 requires reviewer."

**R-FI-3 — Construction reverse charge (AVL Section 8c).** *Trigger:* construction services. *Message:* "Construction reverse charge requires specialist classification."

**R-FI-4 — Aland Islands goods trade.** *Trigger:* goods imported/exported to Aland. *Message:* "Aland is outside EU VAT territory for goods. Special import/export treatment required."

**R-FI-5 — Special schemes.** *Message:* "Margin/travel agent schemes out of scope."

---

## Section 3 — Supplier pattern library

### 3.1 Finnish banks (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| NORDEA, NORDEA FINLAND | EXCLUDE | Financial service, exempt |
| OP, OSUUSPANKKI, OP YRITYSPANKKI | EXCLUDE | Same |
| DANSKE BANK FI, DANSKE BANK FINLAND | EXCLUDE | Same |
| S-PANKKI | EXCLUDE | Same |
| HANDELSBANKEN FI | EXCLUDE | Same |
| AKTIA | EXCLUDE | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscriptions |
| KORKO, INTEREST | EXCLUDE | Interest |
| LAINA, LOAN | EXCLUDE | Loan principal |

### 3.2 Finnish government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| VEROHALLINTO, VERO, TAX ADMIN | EXCLUDE | Tax payment |
| KELA | EXCLUDE | Social insurance |
| TYEL, ELAKEVAKUUTUS | EXCLUDE | Pension insurance |
| PRH, KAUPPAREKISTERI | EXCLUDE | Trade register |

### 3.3 Finnish utilities

| Pattern | Treatment | Code | Notes |
|---|---|---|---|
| HELEN, HELSINGIN ENERGIA | Domestic 25.5% | 307 (input) | Electricity |
| FORTUM | Domestic 25.5% | 307 | Electricity |
| CARUNA | Domestic 25.5% | 307 | Grid distribution |
| HSY, VESILAITOS | Domestic 25.5% | 307 | Water |
| ELISA, DNA, TELIA FI | Domestic 25.5% | 307 | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| IF VAHINKOVAKUUTUS | EXCLUDE | Exempt |
| OP VAKUUTUS | EXCLUDE | Same |
| LAHITAPIOLA | EXCLUDE | Same |
| FENNIA | EXCLUDE | Same |
| VAKUUTUS, INSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Notes |
|---|---|---|
| POSTI, POSTI OY | EXCLUDE for standard post; 25.5% for parcel | |
| MATKAHUOLTO | Domestic 25.5% | Courier/parcel |
| DHL INTERNATIONAL | EU reverse charge | Check entity |

### 3.6 SaaS — EU suppliers (reverse charge, Code 313 + 307)

| Pattern | Billing entity | Notes |
|---|---|---|
| GOOGLE | Google Ireland Ltd (IE) | EU reverse charge |
| MICROSOFT | Microsoft Ireland (IE) | Reverse charge |
| ADOBE | Adobe Ireland (IE) | Reverse charge |
| META, FACEBOOK | Meta Ireland (IE) | Reverse charge |
| SPOTIFY | Spotify AB (SE) | EU reverse charge |
| DROPBOX | Dropbox Ireland (IE) | Reverse charge |
| SLACK | Slack Ireland (IE) | Reverse charge |
| ATLASSIAN | Atlassian BV (NL) | EU reverse charge |
| ZOOM | Zoom Ireland (IE) | Reverse charge |

### 3.7 SaaS — non-EU suppliers (reverse charge, Code 319 + 307)

| Pattern | Billing entity | Notes |
|---|---|---|
| AWS EMEA SARL | LU entity | EU RC (Code 313) |
| NOTION | Notion Labs Inc (US) | Non-EU RC |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Non-EU RC |
| OPENAI, CHATGPT | OpenAI Inc (US) | Non-EU RC |
| GITHUB | GitHub Inc (US) | Check if IE |
| FIGMA | Figma Inc (US) | Non-EU RC |
| CANVA | Canva Pty Ltd (AU) | Non-EU RC |

### 3.8 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

### 3.9 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| KIRJANPITAJA, TILITOIMISTO | Domestic 25.5% | Accounting |
| ASIANAJAJA, LAWYER | Domestic 25.5% | Legal |

### 3.10 Payroll (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TYEL, ELAKEVAKUUTUS | EXCLUDE | Pension |
| PALKKA, SALARY | EXCLUDE | Wages |
| TULOVERO | EXCLUDE | Income tax |

### 3.11 Food retail

| Pattern | Treatment | Notes |
|---|---|---|
| S-MARKET, PRISMA, K-CITYMARKET, LIDL FI | Default BLOCK | Personal provisioning |
| RAVINTOLA, RESTAURANT | Default BLOCK | Entertainment |

### 3.12 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OMA SIIRTO, OWN TRANSFER | EXCLUDE | Internal |
| OSINKO, DIVIDEND | EXCLUDE | Out of scope |
| LAINAN LYHENNYS | EXCLUDE | Loan repayment |
| ATM, KATEINEN | Ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-EU SaaS reverse charge (Notion)
**Input:** `03.04.2026 ; NOTION LABS INC ; -14.68 EUR`
**Treatment:** Non-EU RC. Code 319 (base). Self-assessed ALV at 25.5%. Input in Code 307.

### Example 2 — EU service reverse charge (Google Ads)
**Input:** `10.04.2026 ; GOOGLE IRELAND LIMITED ; -850.00 EUR`
**Treatment:** EU RC. Code 313 (base). Self-assessed at 25.5%. Input in Code 307.

### Example 3 — Entertainment
**Input:** `15.04.2026 ; RAVINTOLA NOKKA ; -220.00 EUR`
**Treatment:** Restaurant. In Finland, entertainment/representation: input ALV deductible at 50% for representation (AVL Section 114). Default: block (purpose unknown).

### Example 4 — Capital goods
**Input:** `18.04.2026 ; VERKKOKAUPPA.COM ; Laptop ; -1,595.00 EUR`
**Treatment:** Business equipment. Input ALV at 25.5% in Code 307.

### Example 5 — EU B2B service sale
**Input:** `22.04.2026 ; STUDIO KREBS GMBH ; +3,500.00 EUR`
**Treatment:** B2B to DE. Code 312. 0%. Verify USt-IdNr.

### Example 6 — Fuel
**Input:** `28.04.2026 ; NESTE ; Fuel ; -80.00 EUR`
**Treatment:** Vehicle fuel. In Finland, no statutory vehicle restriction like Estonia's 50%. Deductible if for business. Default: 0% (use unknown).

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard 25.5% (AVL Section 84)
Default. Sales: Code 301/305. Input: Code 307.

### 5.2 Reduced 13.5% (AVL Section 85)
Food, restaurant/catering, animal feed.

### 5.3 Reduced 10% (AVL Section 85a)
Books, newspapers, medicines, passenger transport, accommodation, cultural/sporting events.

### 5.4 Zero rate / exports
Exports: Code 314. Intra-EU goods: Code 311. Intra-EU services: Code 312.

### 5.5 Exempt without credit (AVL Sections 34-60)
Financial, insurance, healthcare, education, postal, gambling, residential rental.

### 5.6 Reverse charge — EU services (AVL Section 9/65)
Base: Code 313. Input: Code 307.

### 5.7 Reverse charge — EU goods (AVL Section 26a)
Base: Code 309. Input: Code 307.

### 5.8 Reverse charge — non-EU services
Base: Code 319. Input: Code 307.

### 5.9 Construction reverse charge (AVL Section 8c)
Base: Code 320. Flag R-FI-3 for reviewer.

### 5.10 Single input code
Finland aggregates ALL deductible input ALV into a single Code 307. No separate input codes by rate or source.

### 5.11 Representation 50% rule
Entertainment/representation: 50% of input ALV deductible (AVL Section 114). Requires documented business purpose.

### 5.12 Aland Islands (AVL Section 68a)
Goods to/from Aland treated as import/export. Services follow normal place-of-supply rules.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — *Default:* 0%. *Question:* "Business use?"
### 6.2 Entertainment — *Default:* block. *Question:* "Representation (50% deductible) or personal?"
### 6.3 SaaS entity — *Default:* non-EU RC. *Question:* "Check invoice."
### 6.4 Owner transfers — *Default:* exclude.
### 6.5 Individual incoming — *Default:* 25.5%.
### 6.6 Foreign incoming — *Default:* 25.5%.
### 6.7 Large purchases — *Default:* deductible; flag capital.
### 6.8 Mixed-use telecom — *Default:* 0%.
### 6.9 Cash withdrawals — *Default:* exclude.
### 6.10 Aland trade — *Default:* flag reviewer.

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3. Column H accepts Finnish ALV field codes. Bottom-line: output codes minus Code 307 = net payable/refundable.

---

## Section 8 — Finland bank statement reading guide

**CSV conventions.** Nordea and OP use semicolons, DD.MM.YYYY. OP may export in ISO format.

**Finnish language.** vuokra (rent), palkka (salary), korko (interest), siirto (transfer), kateinen (cash).

**IBAN prefix.** FI = Finland.

**Rate change note.** Standard rate changed from 24% to 25.5% on 1 September 2024. Verify invoice date for transactions near the transition.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Inference:* Oy = company; toiminimi = sole trader.
### 9.2 ALV registration — *Fallback:* "Are you ALV-registered?"
### 9.3 Y-tunnus — *Fallback:* "Y-tunnus? (NNNNNNN-N)"
### 9.4 Filing frequency — *Fallback:* "Monthly, quarterly, or annual?"
### 9.5 Exempt supplies — *Fallback:* "Any exempt supplies?"
### 9.6 Construction — *Fallback:* "Do you provide construction services?"
### 9.7 Aland — *Fallback:* "Do you trade with Aland Islands?"

---

## Section 10 — Reference material

### Sources
1. Arvonlisaverolaki (AVL, Act 1501/1993, as amended)
2. Act 1109/2023 and Act 817/2024 (rate changes)
3. EU VAT Directive 2006/112/EC — via companion skill
4. VIES — https://ec.europa.eu/taxation_customs/vies/

### Change log
- **v2.0 (April 2026):** Full rewrite. Finnish banks (Nordea FI, OP, Danske FI). 25.5% rate.
- **v1.0 (April 2026):** Initial skill.

## End of Finland VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
