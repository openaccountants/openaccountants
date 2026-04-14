---
name: bahamas-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Bahamas VAT return for any client. Trigger on phrases like "Bahamas VAT", "DIR Bahamas", "Department of Inland Revenue Bahamas", or any request involving Bahamas VAT. The Bahamas has NO income tax — VAT is the primary tax. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Bahamas VAT work.
version: 2.0
---

# Bahamas VAT Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | The Bahamas (Commonwealth of The Bahamas) |
| Standard rate | 10% |
| Reduced rate | 5% (food in food stores from April 2025; medications, diapers, hygiene from September 2025) |
| Zero rate | 0% (exports, international transport) |
| Exempt | Financial services, residential rent, education, medical, public transport |
| Return form | VAT return (frequency based on turnover) |
| Filing portal | https://inlandrevenue.finance.gov.bs |
| Authority | Department of Inland Revenue (DIR) |
| Currency | BSD (Bahamian Dollar, pegged 1:1 to USD) |
| Filing frequencies | Monthly (>BSD 5M), Bimonthly (BSD 400K–5M), Quarterly (BSD 100K–400K), Annual (voluntary) |
| Deadline | 21st of the month following the period |
| Registration threshold | BSD 100,000 mandatory; BSD 50,000 voluntary |
| No income tax | The Bahamas has NO income tax of any kind |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 10% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Bahamas |
| Unknown food classification (store vs restaurant) | 10% (restaurant/prepared) |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | BSD 10,000 |
| HIGH tax-delta on a single default | BSD 500 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: CIBC FirstCaribbean, RBC Bahamas (Royal Bank), Scotiabank Bahamas, Commonwealth Bank, Fidelity Bank, or any other.

### Bahamas-specific refusal catalogue

**R-BS-1 — Grand Bahama Freeport.** Trigger: client operates within Grand Bahama Port Authority area. Message: "Freeport operations under the Hawksbill Creek Agreement have special VAT provisions requiring specialist analysis. Please escalate."

**R-BS-2 — Investment fund structures.** Trigger: client is an investment fund. Message: "Investment fund VAT treatment requires specialist analysis. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Bahamian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| CIBC FIRSTCARIBBEAN, CIBC FC | EXCLUDE for bank charges | Financial service, exempt |
| RBC BAHAMAS, ROYAL BANK | EXCLUDE for bank charges | Same |
| SCOTIABANK BS, COMMONWEALTH BANK | EXCLUDE for bank charges | Same |
| FIDELITY BANK | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| DIR, DEPT INLAND REVENUE | EXCLUDE | Tax payment |
| CUSTOMS, BAHAMAS CUSTOMS | EXCLUDE | Duty (import VAT separate) |
| BUSINESS LICENCE, BL FEE | EXCLUDE | Government fee |
| NIB, NATIONAL INSURANCE | EXCLUDE | National insurance |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| BPL, BAHAMAS POWER AND LIGHT | Domestic 10% | Electricity |
| WSC, WATER AND SEWERAGE | Domestic 10% | Water |
| BTC, BAHAMAS TELECOMMUNICATIONS | Domestic 10% | Telecoms |
| ALIV | Domestic 10% | Mobile |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BAHAMAS FIRST, COLINA, J.S. JOHNSON | EXCLUDE | Exempt |
| SUMMIT INSURANCE | EXCLUDE | Same |

### 3.5 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 10% (reverse charge) | Non-resident |
| ZOOM, SLACK, CANVA | Self-assess 10% | Same |

### 3.6 Tourism

| Pattern | Treatment | Notes |
|---|---|---|
| HOTEL, RESORT, ATLANTIS | Domestic 10% (output) | Tourism supply |
| BOOKING.COM, EXPEDIA, AIRBNB | Platform fee — verify entity | May require reverse charge |

### 3.7 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES | EXCLUDE | No income tax; outside VAT scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| DIVIDEND | EXCLUDE | No income tax |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 10%

**Input line:** `05.04.2026 ; NASSAU TRADING CO ; CREDIT ; Invoice BS-041 ; BSD 1,100`

**Reasoning:** Domestic. 10%. Net = BSD 1,000, VAT = BSD 100.

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | NASSAU TRADING CO | +1,100 | +1,000 | 100 | 10% | Output | N | — |

### Example 2 — Food in food store at 5% (from April 2025)

**Input line:** `10.04.2026 ; SUPER VALUE FOOD STORE ; DEBIT ; Groceries ; BSD -105`

**Reasoning:** Food in food store, reduced 5% rate from April 2025. Net = BSD 100, VAT = BSD 5.

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | SUPER VALUE FOOD STORE | -105 | -100 | 5 | 5% | Input | N | — |

### Example 3 — Export, zero-rated

**Input line:** `15.04.2026 ; US BUYER INC ; CREDIT ; Exported conch ; BSD 5,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | US BUYER INC | +5,000 | +5,000 | 0 | 0% | Zero-rated | N | — |

### Example 4 — Non-resident service (reverse charge)

**Input line:** `18.04.2026 ; US CONSULTING FIRM ; DEBIT ; Advisory ; BSD -3,000`

**Reasoning:** Reverse charge. Self-assess 10% output = BSD 300. Claim input BSD 300 if fully taxable.

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | US CONSULTING FIRM | -3,000 | -3,000 | 300 | 10% | Output + Input | N | — |

### Example 5 — Bank charges, excluded

**Input line:** `30.04.2026 ; CIBC FIRSTCARIBBEAN ; DEBIT ; Monthly fee ; BSD -25`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | CIBC FIRSTCARIBBEAN | -25 | — | — | — | — | N | "Exempt" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 10% — Default for most taxable supplies.
### 5.2 Reduced rate 5% — Food in food stores (from Apr 2025), medications, diapers, hygiene products (from Sep 2025). Moving to 0% for unprepared food from April 2026 — verify.
### 5.3 Zero rate — Exports, international transport.
### 5.4 Exempt — Financial services, residential rent, education, medical, public transport.
### 5.5 Input tax credit — Available on purchases for taxable supplies. Apportionment if mixed.
### 5.6 Blocked input — Entertainment, personal vehicles, personal consumption.
### 5.7 Imports — VAT at 10% on CIF plus duties. Paid at customs.
### 5.8 Reverse charge — Non-resident services: self-assess 10%. Claim input if for taxable supplies.
### 5.9 No income tax — The Bahamas has no income tax. VAT is primary revenue source.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Food classification — Default: 10% unless in food store. Question: "Is this food in a food store (5%) or prepared food/restaurant (10%)?"
### 6.2 Freeport operations — Default: refuse (R-BS-1).
### 6.3 Tourism sector — Default: 10%. Question: "Hotel occupancy tax separate from VAT?"
### 6.4 SaaS entities — Default: self-assess 10%.
### 6.5 Cash withdrawals — Default: exclude.

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Bahamas fields: Output 10%, Output 5%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT.

---

## Section 8 — Bank statement reading guide

CIBC FirstCaribbean and RBC exports CSV/PDF. BSD primary (= USD). Internal transfers: exclude. No foreign currency conversion needed for USD (BSD pegged 1:1).

---

## Section 9 — Onboarding fallback

### 9.1 TIN — "What is your DIR TIN?"
### 9.2 Filing frequency — Based on turnover. "Annual turnover bracket?"
### 9.3 Industry — "What does the business do?"
### 9.4 Exports — "Do you export?"
### 9.5 Freeport — "Are you in Grand Bahama Freeport?" (If yes, R-BS-1 fires.)
### 9.6 Credit brought forward — Always ask.

---

## Section 10 — Reference material

### Sources
1. Value Added Tax Act 2014 (as amended). 2. DIR guidelines. 3. Rate history: 7.5% (2015), 12% (2018), 10% (2022), 5% reduced (2025).

### Known gaps
1. Freeport refused. 2. Food 0% transition (April 2026) — verify current status. 3. No income tax confirmation must be stated clearly.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
