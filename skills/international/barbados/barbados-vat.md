---
name: barbados-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Barbados VAT return for any client. Trigger on phrases like "Barbados VAT", "BRA filing", "Barbados Revenue Authority", or any request involving Barbados VAT. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Barbados VAT work.
version: 2.0
---

# Barbados VAT Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Barbados |
| Standard rate | 17.5% |
| Reduced rate | 7.5% (hotel accommodation) |
| Zero rate | 0% (exports, basic food items, prescription drugs) |
| Exempt | Financial services, residential rent, education, medical, insurance |
| Return form | VAT return (bimonthly) |
| Filing portal | https://bra.gov.bb (BRA Tax Administration Management Information System, TAMIS) |
| Authority | Barbados Revenue Authority (BRA) |
| Currency | BBD (Barbados Dollar, pegged 2:1 to USD) |
| Filing frequency | Bimonthly |
| Deadline | 21st of the month following the bimonthly period |
| Registration threshold | BBD 200,000 annual turnover |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 17.5% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Barbados |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: CIBC FirstCaribbean Barbados, Republic Bank Barbados, First Citizens Barbados, Scotiabank BB, or any other.

### Barbados-specific refusal catalogue

**R-BB-1 — International business company (IBC).** Trigger: client is an IBC or international financial entity. Message: "IBCs have bespoke tax treatment. Please escalate."

**R-BB-2 — Tourism levy interaction.** Trigger: client subject to tourism levies alongside VAT. Message: "Tourism levy interaction with VAT requires specialist analysis. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Barbadian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| CIBC FIRSTCARIBBEAN BB, CIBC BB | EXCLUDE | Exempt financial service |
| REPUBLIC BANK BB, REPUBLIC BANK BARBADOS | EXCLUDE | Same |
| FIRST CITIZENS BB | EXCLUDE | Same |
| SCOTIABANK BB | EXCLUDE | Same |
| INTEREST, LOAN | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BRA, BARBADOS REVENUE | EXCLUDE | Tax payment |
| NIS, NATIONAL INSURANCE | EXCLUDE | Social security |
| CUSTOMS | EXCLUDE | Duty |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| BL&P, BARBADOS LIGHT AND POWER, EMERA | Domestic 17.5% | Electricity |
| BWA, BARBADOS WATER | Domestic 17.5% | Water |
| FLOW, DIGICEL BB | Domestic 17.5% | Telecoms |

### 3.4 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 17.5% | Non-resident |
| ZOOM, SLACK, CANVA | Self-assess 17.5% | Same |

### 3.5 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES | EXCLUDE | Outside VAT scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 17.5%

**Input line:** `05.04.2026 ; BRIDGETOWN TRADING ; CREDIT ; Invoice BB-041 ; BBD 1,175`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | BRIDGETOWN TRADING | +1,175 | +1,000 | 175 | 17.5% | Output | N | — |

### Example 2 — Hotel accommodation at 7.5%

**Input line:** `10.04.2026 ; HOTEL GUEST ; CREDIT ; Room charge ; BBD 1,075`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | HOTEL GUEST | +1,075 | +1,000 | 75 | 7.5% | Output (reduced) | N | — |

### Example 3 — Export, zero-rated

**Input line:** `15.04.2026 ; US BUYER ; CREDIT ; Exported rum ; BBD 10,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | US BUYER | +10,000 | +10,000 | 0 | 0% | Zero-rated | N | — |

### Example 4 — Bank charges

**Input line:** `30.04.2026 ; CIBC BB ; DEBIT ; Service fee ; BBD -50`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | CIBC BB | -50 | — | — | — | — | N | "Exempt" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 17.5% — Default for all taxable supplies.
### 5.2 Reduced rate 7.5% — Hotel accommodation.
### 5.3 Zero rate — Exports, basic food items, prescription drugs.
### 5.4 Exempt — Financial services, residential rent, education, medical, insurance.
### 5.5 Input tax credit — Available. Valid tax invoice required. Apportionment if mixed.
### 5.6 Blocked input — Entertainment, personal vehicles, personal consumption.
### 5.7 Imports — VAT at 17.5% on CIF plus duty.
### 5.8 Reverse charge — Non-resident services: self-assess 17.5%.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Hotel vs standard rate — Question: "Is this accommodation (7.5%) or other (17.5%)?"
### 6.2 Tourism levies — Default: flag.
### 6.3 SaaS entities — Default: self-assess 17.5%.
### 6.4 Cash withdrawals — Default: exclude.

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3: Output 17.5%, Output 7.5%, Zero-rated, Exempt, Input, Net VAT.

---

## Section 8 — Bank statement reading guide

CIBC BB and Republic Bank BB exports CSV/PDF. BBD primary (2:1 to USD). Internal transfers: exclude.

---

## Section 9 — Onboarding fallback

### 9.1 TIN — "BRA TIN?"
### 9.2 Filing period — Bimonthly.
### 9.3 Industry — "What does the business do?"
### 9.4 Exports — "Do you export?"
### 9.5 Credit brought forward — Always ask.

---

## Section 10 — Reference material

### Sources
1. Barbados VAT Act. 2. BRA guidelines. 3. TAMIS portal.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).
