---
name: maldives-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Maldives GST return for any client. Trigger on phrases like "Maldives GST", "MIRA filing", "tourism GST", or any request involving Maldives GST. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Maldives GST work.
version: 2.0
---

# Maldives GST Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Maldives (Republic of Maldives) |
| Tourism sector rate | 16% (tourism goods and services) |
| General sector rate | 8% (non-tourism goods and services) |
| Zero rate | 0% (exports) |
| Exempt | Financial services, residential rent, healthcare, education |
| Return form | GST return (monthly) |
| Filing portal | https://www.mira.gov.mv (MIRAconnect) |
| Authority | Maldives Inland Revenue Authority (MIRA) |
| Currency | MVR (Maldivian Rufiyaa); USD widely used in tourism |
| Filing frequency | Monthly |
| Deadline | 28th of the month following the tax period |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate (tourism context) | 16% |
| Unknown rate (general context) | 8% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Maldives |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: BML (Bank of Maldives), MIB (Maldives Islamic Bank), SBI Maldives, HDFC Maldives, or any other.

### Maldives-specific refusal catalogue

**R-MV-1 — Resort lease and TGST complexity.** Trigger: client is a resort operator with complex lease arrangements and dual-rate (tourism/general) supplies. Message: "Resort operators with mixed tourism/general supplies require specialist TGST analysis. Please escalate."

**R-MV-2 — Green tax and service charge interaction.** Trigger: client subject to Green Tax and mandatory 10% service charge alongside GST. Message: "Green Tax and service charge interact with GST base in complex ways for tourism. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Maldivian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BML, BANK OF MALDIVES | EXCLUDE for bank charges | Exempt |
| MIB, MALDIVES ISLAMIC BANK | EXCLUDE for bank charges | Same |
| SBI MALDIVES, HDFC MALDIVES | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MIRA, INLAND REVENUE | EXCLUDE | Tax payment |
| CUSTOMS, MALDIVES CUSTOMS | EXCLUDE | Duty |
| PENSION, MRPS | EXCLUDE | Pension contribution |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| STELCO, STATE ELECTRIC | Domestic 8% | Electricity (general) |
| FENAKA | Domestic 8% | Utility (outer islands) |
| MWSC, MALE WATER | Domestic 8% | Water |
| DHIRAAGU, OOREDOO MALDIVES | Domestic 8% | Telecoms |

### 3.4 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 8% | Non-resident (general rate) |
| ZOOM, SLACK, CANVA | Self-assess 8% | Same |

### 3.5 Tourism-specific

| Pattern | Treatment | Notes |
|---|---|---|
| BOOKING.COM, EXPEDIA, AGODA | Platform fee at 16% (tourism) | Verify billing entity |
| TRIPADVISOR | Marketing cost at 16% if tourism | Same |

### 3.6 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES | EXCLUDE | Outside GST scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Tourism service at 16%

**Input line:** `05.04.2026 ; RESORT GUEST ; CREDIT ; Room revenue ; USD 1,160`

**Reasoning:** Tourism supply. 16%. Net = USD 1,000, GST = USD 160.

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | RESORT GUEST | +1,160 | +1,000 | 160 | 16% | Output (tourism) | N | — |

### Example 2 — General service at 8%

**Input line:** `10.04.2026 ; LOCAL CLIENT ; CREDIT ; Consulting ; MVR 108,000`

**Reasoning:** Non-tourism. 8%. Net = MVR 100,000, GST = MVR 8,000.

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | LOCAL CLIENT | +108,000 | +100,000 | 8,000 | 8% | Output (general) | N | — |

### Example 3 — Export, zero-rated

**Input line:** `15.04.2026 ; SRI LANKAN BUYER ; CREDIT ; Exported fish ; MVR 500,000`

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | SRI LANKAN BUYER | +500,000 | +500,000 | 0 | 0% | Zero-rated | N | — |

### Example 4 — Bank charges, excluded

**Input line:** `30.04.2026 ; BML ; DEBIT ; Monthly fee ; MVR -200`

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | BML | -200 | — | — | — | — | N | "Exempt" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Tourism rate 16% — Tourism goods and services (resort accommodation, diving, excursions, etc.).
### 5.2 General rate 8% — All other taxable supplies not in tourism sector.
### 5.3 Zero rate — Exports.
### 5.4 Exempt — Financial services, residential rent, healthcare, education.
### 5.5 Input tax credit — Available. Apportionment required if mixed tourism/general/exempt.
### 5.6 Imports — GST at applicable rate on CIF plus duty.
### 5.7 Reverse charge — Non-resident services: self-assess at applicable rate.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Tourism vs general classification — Default: flag if unclear. Question: "Is this a tourism or general sector supply?"
### 6.2 Green tax and service charge base — Default: flag. Question: "Confirm GST base after service charge inclusion."
### 6.3 USD vs MVR transactions — Default: convert at MMA rate. Question: "Confirm exchange rate."
### 6.4 Cash withdrawals — Default: exclude. Question: "Purpose?"

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Maldives fields: Output tourism 16%, Output general 8%, Zero-rated, Exempt, Input domestic, Input imports, Net GST.

---

## Section 8 — Bank statement reading guide

BML and MIB exports CSV. Dual currency (MVR and USD). Tourism sector predominantly USD. Convert at Maldives Monetary Authority (MMA) rate. Internal transfers: exclude.

---

## Section 9 — Onboarding fallback

### 9.1 TIN — "What is your MIRA TIN?"
### 9.2 Sector — "Tourism or general sector (or both)?"
### 9.3 Filing period — Monthly. "Which month?"
### 9.4 Credit brought forward — Always ask.

---

## Section 10 — Reference material

### Sources
1. Maldives GST Act (Law No. 10/2011, as amended). 2. MIRA guidelines. 3. Tourism rate amendments.

### Known gaps
1. Resort TGST complexity refused. 2. Green tax/service charge interaction refused.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).
