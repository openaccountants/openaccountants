---
name: myanmar-ct
description: Use this skill whenever asked to prepare, review, or classify transactions for a Myanmar Commercial Tax (CT) return for any client. Trigger on phrases like "Myanmar CT", "commercial tax", "IRD filing Myanmar", or any request involving Myanmar commercial tax. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Myanmar CT work.
version: 2.0
---

# Myanmar Commercial Tax Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Myanmar (Republic of the Union of Myanmar) |
| Standard rate | 5% (commercial tax on most goods and services) |
| Higher rates | 8%-100% on specified goods (alcohol, tobacco, gems, vehicles, fuel) |
| Zero rate | 0% (exports) |
| Exempt | Basic foodstuffs, agricultural products, education, healthcare |
| Return form | Monthly CT return |
| Filing portal | IRD Myanmar (Internal Revenue Department) |
| Authority | Internal Revenue Department (IRD), Ministry of Planning and Finance |
| Currency | MMK (Myanmar Kyat) |
| Filing frequency | Monthly |
| Deadline | 10th of the month following the tax period |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Note:** Myanmar uses Commercial Tax, not VAT. There is no input tax credit mechanism for most businesses. CT is a turnover-based tax for most sectors.

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 5% |
| Unknown input credit eligibility | No credit (single-stage for most) |
| Unknown counterparty location | Domestic Myanmar |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: KBZ (Kanbawza Bank), CB Bank (Co-operative Bank), AYA Bank, Yoma Bank, Myanmar Citizens Bank, or any other.

### Myanmar-specific refusal catalogue

**R-MM-1 — Special goods with high CT rates.** Trigger: client deals in gems, jade, alcohol, tobacco, vehicles, or fuel. Message: "Goods with enhanced CT rates (8%-100%) require product-level classification. Please escalate."

**R-MM-2 — Special Economic Zone (SEZ).** Trigger: client in Thilawa SEZ or other SEZ. Message: "SEZ entities have bespoke tax treatment. Please escalate."

**R-MM-3 — Foreign company branch.** Trigger: foreign company branch in Myanmar. Message: "Branch operations have specific CT and income tax obligations. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Myanmar banks (fees — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| KBZ, KANBAWZA | EXCLUDE for bank charges | Financial charges |
| CB BANK, CO-OPERATIVE BANK | EXCLUDE for bank charges | Same |
| AYA BANK, YOMA BANK | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| IRD, INTERNAL REVENUE | EXCLUDE | Tax payment |
| CUSTOMS, MYANMAR CUSTOMS | EXCLUDE | Duty |
| SSB, SOCIAL SECURITY BOARD | EXCLUDE | Social security |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| YESC, ELECTRICITY SUPPLY | Domestic 5% | Electricity |
| MPT, OOREDOO MM, TELENOR MM, ATOM | Domestic 5% | Telecoms |

### 3.4 Digital payments

| Pattern | Treatment | Notes |
|---|---|---|
| WAVE MONEY, KBZ PAY, OK$ | EXCLUDE for fees | Financial service |

### 3.5 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 5% | Non-resident |
| ZOOM, SLACK | Self-assess 5% | Same |

### 3.6 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES | EXCLUDE | Outside CT scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 5%

**Input line:** `05.04.2026 ; YANGON TRADING CO ; CREDIT ; Invoice MM-041 ; MMK 10,500,000`

**Reasoning:** Domestic. 5%. Net = MMK 10,000,000, CT = MMK 500,000.

| Date | Counterparty | Gross | Net | CT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | YANGON TRADING CO | +10,500,000 | +10,000,000 | 500,000 | 5% | Output | N | — |

### Example 2 — Export, zero-rated

**Input line:** `15.04.2026 ; THAI BUYER CO ; CREDIT ; Exported goods ; MMK 50,000,000`

| Date | Counterparty | Gross | Net | CT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | THAI BUYER CO | +50,000,000 | +50,000,000 | 0 | 0% | Zero-rated | N | — |

### Example 3 — Bank charges

**Input line:** `30.04.2026 ; KBZ ; DEBIT ; Service fee ; MMK -5,000`

| Date | Counterparty | Gross | Net | CT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | KBZ | -5,000 | — | — | — | — | N | "Financial charge" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 5% — Default for most goods and services.
### 5.2 Higher rates — 8% (select processed goods), 25%-100% (alcohol, tobacco, gems, vehicles, fuel).
### 5.3 Zero rate — Exports.
### 5.4 Exempt — Basic food, agriculture, education, healthcare.
### 5.5 Input tax credit — LIMITED. Only available in specific manufacturing/production chain scenarios. Most businesses: no credit.
### 5.6 Imports — CT at applicable rate on CIF plus duty.
### 5.7 Reverse charge — Non-resident services: self-assess 5%.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Product classification — Default: 5%. Question: "Is this a special-rate product (alcohol, tobacco, gems, vehicles)?"
### 6.2 Input credit eligibility — Default: no credit. Question: "Are you in a qualifying production chain?"
### 6.3 SaaS entities — Default: self-assess 5%.
### 6.4 Cash withdrawals — Default: exclude.

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Myanmar fields: Output 5%, Output higher rates, Zero-rated, Exempt, Input (if applicable), Net CT.

---

## Section 8 — Bank statement reading guide

KBZ and CB Bank exports CSV/PDF. MMK primary. Burmese script descriptions possible. Internal transfers: exclude. Convert foreign currency at CBM reference rate.

---

## Section 9 — Onboarding fallback

### 9.1 Registration — "Are you registered for Commercial Tax?"
### 9.2 Filing period — Monthly. "Which month?"
### 9.3 Industry — "What goods/services do you deal in?"
### 9.4 Exports — "Do you export?"
### 9.5 Credit brought forward — Ask if applicable.

---

## Section 10 — Reference material

### Sources
1. Myanmar Commercial Tax Law (as amended). 2. IRD guidelines. 3. Union Tax Law (annual rates).

### Known gaps
1. Special goods rates refused. 2. SEZ refused. 3. Input credit eligibility narrow and poorly documented.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).
