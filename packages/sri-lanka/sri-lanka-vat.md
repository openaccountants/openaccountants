---
name: sri-lanka-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Sri Lanka VAT return for any client. Trigger on phrases like "Sri Lanka VAT", "IRD return", "CGIR filing", or any request involving Sri Lanka VAT. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Sri Lanka VAT work.
version: 2.0
---

# Sri Lanka VAT Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Sri Lanka (Democratic Socialist Republic of Sri Lanka) |
| Standard rate | 18% (effective 1 January 2024) |
| Zero rate | 0% (exports, specified essential goods) |
| Exempt | Financial services, healthcare, education, residential rent, unprocessed agriculture |
| Return form | Monthly VAT return (via IRD e-filing) |
| Filing portal | https://www.ird.gov.lk (IRD e-Services) |
| Authority | Inland Revenue Department (IRD) |
| Currency | LKR (Sri Lankan Rupee) |
| Filing frequency | Monthly |
| Deadline | Last business day of the month following the tax period |
| Registration threshold | LKR 80 million per annum (or LKR 20 million per quarter) |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 18% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Sri Lanka |
| Unknown business-use proportion | 0% recovery |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: BOC (Bank of Ceylon), People's Bank, Commercial Bank, HNB (Hatton National Bank), Sampath Bank, Seylan Bank, DFCC, NDB, Nations Trust, or any other.

### Sri Lanka-specific refusal catalogue

**R-LK-1 — BOI enterprise.** Trigger: client under Board of Investment agreement with tax holidays. Message: "BOI enterprises have bespoke tax exemptions. Please escalate."

**R-LK-2 — Social Security Contribution Levy (SSCL) interaction.** Trigger: SSCL applies alongside VAT. Message: "SSCL is a separate levy that may affect pricing and compliance. Verify current status (SSCL was suspended/reintroduced periodically)."

**R-LK-3 — Simplified VAT regime.** Trigger: client on simplified regime. Message: "Simplified VAT has different filing requirements. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Sri Lankan banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BOC, BANK OF CEYLON | EXCLUDE for bank charges | Exempt |
| PEOPLES BANK, PEOPLE'S BANK | EXCLUDE for bank charges | Same |
| COMMERCIAL BANK, COMBANK | EXCLUDE for bank charges | Same |
| HNB, HATTON NATIONAL | EXCLUDE for bank charges | Same |
| SAMPATH, SEYLAN, NDB, DFCC | EXCLUDE for bank charges | Same |
| NATIONS TRUST | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| IRD, INLAND REVENUE | EXCLUDE | Tax payment |
| CUSTOMS, SRI LANKA CUSTOMS | EXCLUDE | Duty |
| EPF, ETF | EXCLUDE | Employee provident/trust fund |
| COMPANY REGISTRAR | EXCLUDE | Registration fee |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| CEB, CEYLON ELECTRICITY | Domestic 18% | Electricity |
| LECO | Domestic 18% | Electricity (Colombo) |
| NWS&DB, NATIONAL WATER | Domestic 18% | Water |
| SLT, SRI LANKA TELECOM, DIALOG, MOBITEL | Domestic 18% | Telecoms |
| HUTCH, AIRTEL LK | Domestic 18% | Same |

### 3.4 Digital payments

| Pattern | Treatment | Notes |
|---|---|---|
| FRIMI, GENIE, IPAY | EXCLUDE for fees | Financial service |

### 3.5 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 18% | Non-resident |
| ZOOM, SLACK, CANVA | Self-assess 18% | Same |

### 3.6 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES | EXCLUDE | Outside VAT scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| DIVIDEND | EXCLUDE | Out of scope |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 18%

**Input line:** `05.04.2026 ; COLOMBO TRADING PVT ; CREDIT ; Invoice LK-041 ; LKR 1,180,000`

**Reasoning:** Domestic. 18%. Net = LKR 1,000,000, VAT = LKR 180,000.

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | COLOMBO TRADING | +1,180,000 | +1,000,000 | 180,000 | 18% | Output | N | — |

### Example 2 — Export, zero-rated

**Input line:** `15.04.2026 ; UK BUYER LTD ; CREDIT ; Tea export ; LKR 5,000,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | UK BUYER LTD | +5,000,000 | +5,000,000 | 0 | 0% | Zero-rated | N | — |

### Example 3 — Non-resident digital service

**Input line:** `18.04.2026 ; AWS ; DEBIT ; Cloud hosting ; LKR -60,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | AWS | -60,000 | -60,000 | 10,800 | 18% | Output + Input | N | — |

### Example 4 — Bank charges

**Input line:** `30.04.2026 ; BOC ; DEBIT ; Monthly charge ; LKR -1,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | BOC | -1,000 | — | — | — | — | N | "Exempt" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 18% — Default for all taxable supplies (from 1 Jan 2024; previously 15%).
### 5.2 Zero rate — Exports, specified essential goods.
### 5.3 Exempt — Financial services, healthcare, education, residential rent, unprocessed agriculture.
### 5.4 Input tax credit — Valid tax invoice with TIN required. Business purpose. Apportionment if mixed.
### 5.5 Blocked input — Personal consumption, entertainment, passenger vehicles.
### 5.6 Imports — VAT at 18% on CIF plus duty.
### 5.7 Reverse charge — Non-resident services: self-assess 18%.
### 5.8 Registration — Mandatory if turnover exceeds LKR 80M/year or LKR 20M/quarter.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — Default: 0%.
### 6.2 Entertainment — Default: block.
### 6.3 SaaS entities — Default: self-assess 18%.
### 6.4 BOI enterprise status — Default: flag. Question: "BOI agreement in force?"
### 6.5 SSCL interaction — Default: flag. Question: "Is SSCL currently in force?"
### 6.6 Cash withdrawals — Default: exclude.

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Sri Lanka fields: Output 18%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT.

---

## Section 8 — Bank statement reading guide

BOC, People's Bank, Commercial Bank exports CSV/PDF. LKR primary. Sinhala/Tamil descriptions possible. Internal transfers: exclude. Convert foreign currency at CBSL rate.

---

## Section 9 — Onboarding fallback

### 9.1 TIN — "What is your IRD TIN?"
### 9.2 Filing period — Monthly. "Which month?"
### 9.3 Industry — "What does the business do?"
### 9.4 Exports — "Do you export?"
### 9.5 BOI status — "Are you under a BOI agreement?"
### 9.6 Credit brought forward — Always ask.

---

## Section 10 — Reference material

### Sources
1. Sri Lanka Value Added Tax Act No. 14 of 2002 (as amended). 2. Inland Revenue (Amendment) Act. 3. IRD e-Services portal.

### Known gaps
1. BOI enterprises refused. 2. SSCL status changes frequently. 3. Rate changed from 15% to 18% in Jan 2024 — verify for transitional periods.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).
