---
name: laos-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Laos VAT return for any client. Trigger on phrases like "Laos VAT", "Lao PDR tax", "Tax Department filing", or any request involving Laos VAT. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Laos VAT work.
version: 2.0
---

# Laos VAT Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Laos (Lao People's Democratic Republic) |
| Standard rate | 10% (effective 2024; previously 7%) |
| Zero rate | 0% (exports) |
| Exempt | Financial services, education, healthcare, public transport, unprocessed agricultural products |
| Return form | Monthly VAT return |
| Filing portal | Tax Department online system |
| Authority | Tax Department, Ministry of Finance |
| Currency | LAK (Lao Kip) |
| Filing frequency | Monthly |
| Deadline | 20th of the month following the tax period |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 10% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Laos |
| Unknown business-use proportion | 0% recovery |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: BCEL (Banque pour le Commerce Exterieur Lao), LDB (Lao Development Bank), JDB, Phongsavanh Bank, BFL, or any other.

### Laos-specific refusal catalogue

**R-LA-1 — Special Economic Zone (SEZ) entity.** Trigger: client in SEZ with tax incentives. Message: "SEZ entities have special VAT exemptions. Please escalate."

**R-LA-2 — Concession agreement enterprise.** Trigger: client with government concession (mining, hydropower). Message: "Concession agreements have bespoke tax terms. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Lao banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BCEL, BANQUE COMMERCE EXTERIEUR | EXCLUDE for bank charges | Exempt |
| LDB, LAO DEVELOPMENT BANK | EXCLUDE for bank charges | Same |
| JDB, JOINT DEVELOPMENT BANK | EXCLUDE for bank charges | Same |
| PHONGSAVANH BANK, BFL | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TAX DEPARTMENT, MOF | EXCLUDE | Tax payment |
| CUSTOMS, LAO CUSTOMS | EXCLUDE | Customs duty (import VAT separate) |
| LSSO, SOCIAL SECURITY | EXCLUDE | Social security |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| EDL, ELECTRICITE DU LAOS | Domestic 10% | Electricity |
| NPLAOS, LAO WATER | Domestic 10% | Water (commercial) |
| LTC, UNITEL, ETL | Domestic 10% | Telecoms |

### 3.4 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 10% | Non-resident |
| ZOOM, SLACK, CANVA | Self-assess 10% | Same |

### 3.5 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES | EXCLUDE | Outside VAT scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 10%

**Input line:** `05.04.2026 ; LAO TRADING CO ; CREDIT ; Invoice LA-041 ; LAK 11,000,000`

**Reasoning:** Domestic. 10%. Net = LAK 10,000,000, VAT = LAK 1,000,000.

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | LAO TRADING CO | +11,000,000 | +10,000,000 | 1,000,000 | 10% | Output | N | — |

### Example 2 — Export, zero-rated

**Input line:** `15.04.2026 ; THAI BUYER CO ; CREDIT ; Exported wood ; LAK 50,000,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | THAI BUYER CO | +50,000,000 | +50,000,000 | 0 | 0% | Zero-rated | N | — |

### Example 3 — Non-resident digital service

**Input line:** `18.04.2026 ; GOOGLE ; DEBIT ; Google Ads ; LAK 2,200,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | GOOGLE | -2,200,000 | -2,000,000 | 200,000 | 10% | Output + Input | N | — |

### Example 4 — Bank charges, excluded

**Input line:** `30.04.2026 ; BCEL ; DEBIT ; Monthly fee ; LAK -50,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | BCEL | -50,000 | — | — | — | — | N | "Exempt" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 10% — Default for all taxable supplies.
### 5.2 Zero rate — Exports with customs documentation.
### 5.3 Exempt — Financial services, education, healthcare, public transport, unprocessed agriculture.
### 5.4 Input tax credit — Valid tax invoice with TIN required. Business purpose.
### 5.5 Blocked input — Personal consumption, entertainment, passenger vehicles.
### 5.6 Imports — VAT at 10% on CIF plus duty.
### 5.7 Reverse charge — Non-resident services: self-assess 10%.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — Default: 0%. Question: "Commercial vehicle for business?"
### 6.2 Entertainment — Default: block.
### 6.3 SaaS entities — Default: self-assess 10%.
### 6.4 Cash withdrawals — Default: exclude. Question: "Purpose?"
### 6.5 Rent — Default: no credit without VAT invoice. Question: "Does landlord charge VAT?"

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Laos fields: Output 10%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT.

---

## Section 8 — Bank statement reading guide

BCEL and LDB exports CSV. LAK primary currency; USD/THB common for cross-border. Convert at Bank of Lao PDR official rate. Internal transfers between BCEL/LDB/JDB: exclude.

---

## Section 9 — Onboarding fallback

### 9.1 TIN — "What is your Tax Identification Number?"
### 9.2 Filing period — Monthly. "Which month?"
### 9.3 Industry — "What does the business do?"
### 9.4 Exports — "Do you export?"
### 9.5 Credit brought forward — Always ask.

---

## Section 10 — Reference material

### Sources
1. Lao Tax Law (as amended). 2. Tax Department guidelines. 3. Rate increase to 10% effective 2024.

### Known gaps
1. SEZ and concession enterprises refused. 2. Rate recently changed from 7% to 10% — verify for transitional periods.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).
