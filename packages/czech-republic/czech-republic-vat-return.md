---
name: czech-republic-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Czech Republic VAT return (Priznani k DPH) or Control Statement (Kontrolni hlaseni) for any client. Trigger on phrases like "prepare VAT return", "do the DPH", "fill in DPH", "Czech VAT", "kontrolni hlaseni", or any request involving Czech VAT filing. This skill covers Czech Republic only and standard DPH registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Czech VAT work.
version: 2.0
---

# Czech Republic VAT Return Skill (Priznani k DPH) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1.**

| Field | Value |
|---|---|
| Country | Czech Republic (Czechia) |
| Standard rate | 21% |
| Reduced rates | 12% (consolidated from former 15%/10%: food, beverages, water, restaurant/catering, accommodation, books, medicines, medical devices, newspapers, passenger transport, cultural/sporting events, cleaning, hairdressing, minor repairs) |
| Zero rate | 0% (exports, intra-EU supplies of goods) |
| Return form | Priznani k DPH (VAT return); Kontrolni hlaseni (Control Statement, mandatory alongside) |
| Filing portal | https://www.mojedane.cz |
| Authority | Financni sprava Ceske republiky (Financial Administration) |
| Currency | CZK (Czech Koruna) |
| Filing frequencies | Monthly (default, mandatory if turnover > CZK 15M); Quarterly (turnover <= CZK 15M for 2 years, not newly registered) |
| Deadline | 25th of month following period |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Contributor | Michael Cutajar, CPA (Warrant No. 125122), ACCA |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key return rows:**

| Row | Meaning |
|---|---|
| 1 | Domestic taxable supplies at 21% — base and VAT |
| 2 | Domestic taxable supplies at 12% — base and VAT |
| 3 | Intra-EU acquisition of goods — base |
| 4 | Intra-EU acquisition of services (reverse charge) — base |
| 5 | Services received from non-EU (reverse charge) — base |
| 6 | Other domestic reverse charge supplies (construction Sec. 92e) — base |
| 7-8 | Self-assessed output DPH on rows 3-6 |
| 9-10 | Exempt supplies (with/without credit) |
| 20 | Intra-EU supplies of goods |
| 21 | Exports |
| 22 | Intra-EU B2B services supplied |
| 40 | Input DPH on domestic purchases at 21% |
| 41 | Input DPH on domestic purchases at 12% |
| 43 | Input DPH on intra-EU acquisitions |
| 44 | Input DPH on imports |
| 45-46 | Adjustments |
| 47 | Correction of input DPH (Sec. 44) |
| 50 | Total output DPH |
| 51 | Total input DPH (nadmerny odpocet if negative) |
| 62 | Net DPH payable |
| 63 | Excess credit (nadmerny odpocet) |
| 64 | Change in excess credit |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 21% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Czech Republic |
| Unknown B2B vs B2C for EU customer | B2C, charge 21% |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | CZK 75,000 |
| HIGH tax-delta on single default | CZK 5,000 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net DPH position | CZK 125,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: CSOB, Komercni banka, Fio banka, Ceska sporitelna, Raiffeisenbank CZ, mBank, Revolut Business, Wise Business.

**Recommended** — sales/purchase invoices, DIC (CZ + 8-10 digits), prior period return.

**Ideal** — complete invoice register, control statement data, prior Kontrolni hlaseni.

### Czech-specific refusal catalogue

**R-CZ-1 — Identifikovana osoba only.** *Trigger:* client is registered only for EU acquisition purposes (identifikovana osoba), not a full DPH payer. *Message:* "Identified persons file limited returns. This skill covers standard DPH payers only."

**R-CZ-2 — Partial exemption.** *Trigger:* mixed taxable/exempt supplies. *Message:* "Partial exemption requires koeficient calculation under Sec. 76. Use a danovy poradce."

**R-CZ-3 — Construction domestic reverse charge (Sec. 92e).** *Trigger:* construction services. *Message:* "Construction domestic reverse charge requires specialist classification."

**R-CZ-4 — Special schemes.** *Message:* "Margin/travel agent schemes out of scope."

**R-CZ-5 — VAT group.** *Message:* "Group registration out of scope."

---

## Section 3 — Supplier pattern library

### 3.1 Czech banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| CSOB, CESKOSLOVENSKA OBCHODNI BANKA | EXCLUDE | Financial service, exempt |
| KOMERCNI BANKA, KB | EXCLUDE | Same |
| FIO BANKA, FIO | EXCLUDE | Same |
| CESKA SPORITELNA | EXCLUDE | Same |
| RAIFFEISENBANK CZ | EXCLUDE | Same |
| MBANK | EXCLUDE | Same |
| MONETA MONEY BANK | EXCLUDE | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscriptions |
| UROK, UROKOVY, INTEREST | EXCLUDE | Interest, out of scope |
| UVER, LOAN, PUJCKA | EXCLUDE | Loan principal |

### 3.2 Czech government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| FINANCNI URAD, TAX OFFICE | EXCLUDE | Tax payment |
| CSSZ, OSSZ, SOCIAL SECURITY | EXCLUDE | Social contributions |
| VZP, HEALTH INSURANCE | EXCLUDE | Health insurance |
| OBCHODNÍ REJSTRIK, COMPANY REGISTER | EXCLUDE | Registration fee |

### 3.3 Czech utilities

| Pattern | Treatment | Row | Notes |
|---|---|---|---|
| CEZ PRODEJ, CEZ DISTRIBUCE | Domestic 21% | 40 | Electricity |
| PRAZSKA PLYNARENSKA, INNOGY, E.ON CZ | Domestic 21% | 40 | Gas/electricity |
| PRAZSKE VODOVODY, VODARNA | Domestic 12% | 41 | Water at 12% |
| O2 CZECH REPUBLIC, O2 CZ | Domestic 21% | 40 | Telecoms |
| T-MOBILE CZ | Domestic 21% | 40 | Telecoms |
| VODAFONE CZ | Domestic 21% | 40 | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| CESKA POJISTOVNA | EXCLUDE | Exempt |
| KOOPERATIVA | EXCLUDE | Same |
| ALLIANZ CZ | EXCLUDE | Same |
| GENERALI CZ | EXCLUDE | Same |
| POJISTENI, INSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Notes |
|---|---|---|
| CESKA POSTA | EXCLUDE for standard post; Domestic 21% for courier/parcel | Universal exempt; non-universal taxable |
| PPL CZ | Domestic 21% | Courier |
| DPD CZ, GEIS | Domestic 21% | Courier |
| DHL INTERNATIONAL | EU reverse charge | Check entity |

### 3.6 SaaS — EU suppliers (reverse charge, Row 4/7-8 + 43)

| Pattern | Billing entity | Notes |
|---|---|---|
| GOOGLE | Google Ireland Ltd (IE) | EU reverse charge |
| MICROSOFT | Microsoft Ireland (IE) | Reverse charge |
| ADOBE | Adobe Ireland (IE) | Reverse charge |
| META, FACEBOOK | Meta Ireland (IE) | Reverse charge |
| LINKEDIN | LinkedIn Ireland (IE) | Reverse charge |
| SPOTIFY | Spotify AB (SE) | EU reverse charge |
| DROPBOX | Dropbox Ireland (IE) | Reverse charge |
| SLACK | Slack Ireland (IE) | Reverse charge |
| ATLASSIAN | Atlassian BV (NL) | EU reverse charge |
| ZOOM | Zoom Ireland (IE) | Reverse charge |

### 3.7 SaaS — non-EU suppliers (reverse charge, Row 5/7-8 + input)

| Pattern | Billing entity | Notes |
|---|---|---|
| AWS EMEA SARL | LU entity | EU reverse charge |
| NOTION | Notion Labs Inc (US) | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | Non-EU reverse charge |
| GITHUB | GitHub Inc (US) | Check if IE |
| FIGMA | Figma Inc (US) | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | Non-EU reverse charge |

### 3.8 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

### 3.9 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| NOTAR, NOTARY | Domestic 21% | Legal |
| UCETNI, ACCOUNTANT | Domestic 21% | Accounting |
| ADVOKAT, LAWYER | Domestic 21% | Legal |

### 3.10 Payroll (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| CSSZ, OSSZ | EXCLUDE | Social security |
| VZP, ZDRAVOTNI POJISTENI | EXCLUDE | Health insurance |
| MZDA, PLAT, SALARY | EXCLUDE | Wages |

### 3.11 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| VLASTNI PREVOD, OWN TRANSFER | EXCLUDE | Internal |
| DIVIDENDA | EXCLUDE | Out of scope |
| SPLATKA UVERU, LOAN REPAYMENT | EXCLUDE | Loan principal |
| ATM, VYBER, CASH WITHDRAWAL | Ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-EU SaaS reverse charge (Notion)
**Input:** `03.04.2026 ; NOTION LABS INC ; -16 USD / -371 CZK`
**Treatment:** Non-EU reverse charge. Output in Row 5, self-assessed DPH at 21% in Row 7-8. Input DPH claimed. Net zero.

| Date | Counterparty | Net | DPH | Rate | Row (input) | Row (output) | Default? |
|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -371 | 77.91 | 21% | input | 5/7-8 | N |

### Example 2 — EU service reverse charge (Google Ads)
**Input:** `10.04.2026 ; GOOGLE IRELAND LIMITED ; -21,500 CZK`
**Treatment:** EU reverse charge. Row 4 base, Row 7-8 output DPH, Row 43 input.

### Example 3 — Entertainment, restricted
**Input:** `15.04.2026 ; RESTAURACE U FLEKU ; -5,560 CZK`
**Treatment:** In Czech Republic, entertainment/representation expenses: input DPH IS deductible if business purpose documented. However, default block if purpose unclear.

### Example 4 — Capital goods (> CZK 80,000)
**Input:** `18.04.2026 ; ALZA.CZ ; Laptop ; -40,320 CZK`
**Treatment:** Below CZK 80,000 threshold for capital goods. Treat as overhead. Input DPH at 21%.

### Example 5 — EU B2B service sale
**Input:** `22.04.2026 ; STUDIO KREBS GMBH ; +88,500 CZK`
**Treatment:** B2B service to DE. Row 22. 0%. Verify USt-IdNr.

### Example 6 — Motor vehicle fuel
**Input:** `28.04.2026 ; MOL CZ ; Fuel ; -2,020 CZK`
**Treatment:** Vehicle fuel. In CZ, input DPH on passenger car fuel is deductible if for business. Default: 0% (use unknown).

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard 21% (Sec. 47(1)(a))
Default. Sales: Row 1. Purchases: Row 40.

### 5.2 Reduced 12% (Sec. 47(1)(b))
Food, beverages, water, accommodation, restaurant, books, medicines, transport, events.

### 5.3 Zero rate / exempt with credit
Exports: Row 21. Intra-EU goods: Row 20. Intra-EU B2B services: Row 22.

### 5.4 Exempt without credit (Sec. 51-62)
Financial, insurance, healthcare, education, postal, residential rental > 2 years, gambling.

### 5.5 Reverse charge — EU services (Sec. 108(1)(c))
Output: Row 4/7-8. Input: Row 43.

### 5.6 Reverse charge — EU goods (Sec. 25)
Output: Row 3/7-8. Input: Row 43.

### 5.7 Reverse charge — non-EU services
Output: Row 5/7-8. Input claimed.

### 5.8 Capital goods (Sec. 78-78e)
Movable > CZK 80,000 with life > 1 year: 5-year adjustment. Immovable: 10-year.

### 5.9 Blocked input
- Passenger vehicles: deductible if for business (no hard block like Malta)
- Entertainment: deductible if business purpose (unlike Malta hard block)
- Personal use: blocked
- Representation gifts > CZK 500 without advertising: blocked

### 5.10 Control statement (Kontrolni hlaseni)
Mandatory alongside the return. Lists individual transactions. Must be filed even if nil. Penalty for late filing: CZK 10,000-500,000.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs
*Default:* 0%. *Question:* "Vehicle type? Business use?"

### 6.2 Restaurants
*Default:* block. *Question:* "Business purpose? (Deductible in CZ if documented.)"

### 6.3 SaaS billing entity
*Default:* non-EU RC. *Question:* "Check invoice entity."

### 6.4 Owner transfers
*Default:* exclude. *Question:* "Sale, own money, or loan?"

### 6.5 Large purchases
*Default:* if > CZK 80,000, capital goods. *Question:* "Confirm total."

### 6.6 Mixed-use phone/internet
*Default:* 0%. *Question:* "Business or mixed?"

### 6.7 Cash withdrawals
*Default:* exclude. *Question:* "Purpose?"

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3. Column H accepts CZ DPH row codes. Bottom-line: Row 62 (payable) or Row 63 (excess credit).

---

## Section 8 — Czech bank statement reading guide

**CSV conventions.** CSOB and KB use semicolons, DD.MM.YYYY. Fio exports CSV with CZK amounts.

**Czech language.** najem (rent), mzda/plat (salary), urok (interest), prevod (transfer).

**Currency.** CZK. Convert foreign amounts at CNB (Czech National Bank) rate.

**IBAN prefix.** CZ = Czech Republic.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type
*Inference:* s.r.o. = company; OSVC = sole trader. *Fallback:* "OSVC or s.r.o.?"

### 9.2 DPH registration
*Fallback:* "Are you platce DPH?"

### 9.3 DIC
*Fallback:* "DIC? (CZ + 8-10 digits)"

### 9.4 Filing period
*Fallback:* "Monthly or quarterly? Which period?"

### 9.5 Control statement
*Fallback:* "Do you file Kontrolni hlaseni?"

### 9.6 Exempt supplies
*Fallback:* "Any exempt supplies?"

### 9.7 Credit brought forward
*Fallback:* "Nadmerny odpocet from prior period?"

---

## Section 10 — Reference material

### Sources
1. VAT Act No. 235/2004 Coll. (as amended by 349/2023 Coll.)
2. Control Statement Regulation
3. EU VAT Directive 2006/112/EC — via companion skill
4. VIES — https://ec.europa.eu/taxation_customs/vies/

### Change log
- **v2.0 (April 2026):** Full rewrite. Czech banks (CSOB, Komercni banka, Fio).
- **v1.0 (April 2026):** Initial skill.

## End of Czech Republic VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
