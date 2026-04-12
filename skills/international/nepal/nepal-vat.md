---
name: nepal-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Nepal VAT return for any client. Trigger on phrases like "Nepal VAT", "IRD filing", "PAN registration", or any request involving Nepal VAT. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Nepal VAT work.
version: 2.0
---

# Nepal VAT Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Nepal (Federal Democratic Republic of Nepal) |
| Standard rate | 13% |
| Zero rate | 0% (exports, goods to SEZ) |
| Exempt | Basic agricultural products, education, healthcare, financial services, public transport |
| Return form | VAT return (monthly, via IRD e-filing) |
| Filing portal | https://ird.gov.np (IRD e-filing) |
| Authority | Inland Revenue Department (IRD) |
| Currency | NPR (Nepalese Rupee) |
| Filing frequency | Monthly (by 25th of following month) |
| Deadline | 25th of the month following the tax period |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 13% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Nepal |
| Unknown business-use proportion | 0% recovery |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: Nabil Bank, NIC Asia Bank, Nepal Bank, Rastriya Banijya Bank, Himalayan Bank, Everest Bank, Standard Chartered Nepal, or any other.

### Nepal-specific refusal catalogue

**R-NP-1 — Special Economic Zone entity.** Trigger: client in SEZ. Message: "SEZ entities have special VAT treatment. Please escalate."

**R-NP-2 — Hydropower and infrastructure projects.** Trigger: client with government infrastructure concession. Message: "Infrastructure projects have bespoke VAT exemptions. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Nepalese banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| NABIL, NABIL BANK | EXCLUDE for bank charges | Exempt |
| NIC ASIA, NIC ASIA BANK | EXCLUDE for bank charges | Same |
| NEPAL BANK, RASTRIYA BANIJYA | EXCLUDE for bank charges | Same |
| HIMALAYAN BANK, EVEREST BANK | EXCLUDE for bank charges | Same |
| STANDARD CHARTERED NP | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| IRD, INLAND REVENUE | EXCLUDE | Tax payment |
| CUSTOMS, NEPAL CUSTOMS | EXCLUDE | Duty |
| SSF, SOCIAL SECURITY FUND | EXCLUDE | Social security |
| COMPANY REGISTRAR, OCR | EXCLUDE | Registration fee |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| NEA, NEPAL ELECTRICITY | Domestic 13% | Electricity |
| KUKL, KATHMANDU WATER | Domestic 13% | Water |
| NTC, NEPAL TELECOM, NCELL | Domestic 13% | Telecoms |

### 3.4 Digital payments

| Pattern | Treatment | Notes |
|---|---|---|
| ESEWA, KHALTI, IME PAY | EXCLUDE for fees | Financial service fees exempt |
| FONEPAY | EXCLUDE for fees | Same |

### 3.5 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 13% | Non-resident |
| ZOOM, SLACK, CANVA | Self-assess 13% | Same |

### 3.6 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES, TLAB | EXCLUDE | Outside VAT scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 13%

**Input line:** `05.04.2026 ; KATHMANDU TRADING ; CREDIT ; Invoice NP-041 ; NPR 113,000`

**Reasoning:** Domestic. 13%. Net = NPR 100,000, VAT = NPR 13,000.

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | KATHMANDU TRADING | +113,000 | +100,000 | 13,000 | 13% | Output | N | — |

### Example 2 — Export, zero-rated

**Input line:** `15.04.2026 ; INDIAN BUYER LTD ; CREDIT ; Exported handicrafts ; NPR 500,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | INDIAN BUYER LTD | +500,000 | +500,000 | 0 | 0% | Zero-rated | N | — |

### Example 3 — Non-resident digital service

**Input line:** `18.04.2026 ; GOOGLE ; DEBIT ; Google Ads ; NPR -23,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | GOOGLE | -23,000 | -23,000 | 2,990 | 13% | Output + Input | N | — |

### Example 4 — Bank charges

**Input line:** `30.04.2026 ; NABIL BANK ; DEBIT ; Service charge ; NPR -500`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | NABIL BANK | -500 | — | — | — | — | N | "Exempt" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 13% — Default for all taxable supplies.
### 5.2 Zero rate — Exports, supplies to SEZ.
### 5.3 Exempt — Basic agriculture, education, healthcare, financial services, public transport.
### 5.4 Input tax credit — Valid VAT invoice with PAN required. Business purpose.
### 5.5 Blocked input — Personal consumption, entertainment, passenger vehicles.
### 5.6 Imports — VAT at 13% on CIF plus duty.
### 5.7 Reverse charge — Non-resident services: self-assess 13%.
### 5.8 VAT billing software — IRD requires use of approved billing software for invoice generation.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — Default: 0%.
### 6.2 Entertainment — Default: block.
### 6.3 SaaS entities — Default: self-assess 13%.
### 6.4 Cash withdrawals — Default: exclude.
### 6.5 Mixed-use expenses — Default: 0% recovery.

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Nepal fields: Output 13%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT.

---

## Section 8 — Bank statement reading guide

Nabil and NIC Asia exports CSV. NPR primary. Devanagari script descriptions possible — treat transliterated equivalents the same. Internal transfers: exclude. Convert foreign currency at Nepal Rastra Bank rate.

---

## Section 9 — Onboarding fallback

### 9.1 PAN — "What is your Permanent Account Number?"
### 9.2 Filing period — Monthly. "Which month?"
### 9.3 Industry — "What does the business do?"
### 9.4 Exports — "Do you export?"
### 9.5 Credit brought forward — Always ask.

---

## Section 10 — Reference material

### Sources
1. Nepal Value Added Tax Act 2052 (1996, as amended). 2. IRD guidelines. 3. IRD e-filing portal.

### Known gaps
1. SEZ entities refused. 2. Hydropower/infrastructure refused.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).
