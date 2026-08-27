---
name: nepal-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Nepal VAT return for any client. Trigger on phrases like "Nepal VAT", "IRD filing", "PAN registration", or any request involving Nepal VAT. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Nepal VAT work.
version: 2.0
jurisdiction: NP
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Ashish Bista
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nepal VAT

## Nepal VAT Return Skill v2.0

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ashish Bista** on 2026-06-06.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### VAT (IRD Return)

- **Standard rate** — 13%
- **Zero rate** — 0% (exports, goods to SEZ)
- **Exempt** — Basic agriculture, education, healthcare, financial services, public transport  _(VAT Act 2052 Sch.1)_
- **Concessional rate** — 5% on electricity (above 50 units) AND ride-sharing / ride-hailing services  _(Finance Act 2083 (amended VAT Act 2052 s.7))_
- **Registration threshold — goods/carriage** — NPR 5,000,000 (12-month turnover)  _(VAT Act 2052 s.10 (Baker Tilly/PKF))_
- **Registration threshold — services or mixed** — NPR 3,000,000 (raised from NPR 2M eff. 16 Jul 2024)  _(VAT Act 2052 s.10 (Baker Tilly))_
- **Filing frequency** — Monthly, within 25 days of the end of each Nepali calendar month  _(VAT Act 2052 (Baker Tilly))_
- **Imports** — VAT at 13% on CIF plus duty  _(VAT Act 2052)_
- **Reverse charge — non-resident services** — Self-assess 13%  _(VAT Act 2052)_
- **Input tax credit** — Valid VAT invoice with PAN; business purpose; IRD-approved billing software  _(VAT Act 2052)_
- **Blocked input** — Personal consumption, entertainment, passenger vehicles  _(VAT Act 2052)_
- **Digital Payment VAT Discount** — 10% instant VAT refund directly to consumers for making digital/cashless payments  _(Finance Act 2083 / VAT Act 2052)_
- **VAT Bill Lottery Scheme** — Every VAT bill automatically acts as a lottery ticket for consumers  _(Budget Speech 2083/84)_
- **Unpaid VAT / Tax Amnesty Settlement** — Settle pending VAT cases by paying outstanding principal tax + 1% fee (all other penalties waived)  _(Finance Act 2083 (Section 41/44))_

## Section 1 — Quick reference

- **Country** — Nepal (Federal Democratic Republic of Nepal)
- **Standard rate** — 13%
- **Zero rate** — 0% (exports, goods to SEZ)
- **Exempt** — Basic agricultural products, education, healthcare, financial services, public transport
- **Return form** — VAT return (monthly, via IRD e-filing)
- **Filing portal** — https://ird.gov.np (IRD e-filing)
- **Authority** — Inland Revenue Department (IRD)
- **Currency** — NPR (Nepalese Rupee)
- **Filing frequency** — Monthly (by 25th of following month)
- **Deadline** — 25th of the month following the tax period
- **Registration threshold** — NPR 5,000,000 (goods/carriage) · NPR 3,000,000 (services or mixed) — services/mixed raised from NPR 2M eff. Shrawan 1, 2081 (16 Jul 2024)
- **Companion skill** — vat-workflow-base v0.1 or later — MUST be loaded
- **Validated by** — Verified by Ashish Bista (ICAN: 1765) on 2026-06-06

**Section 1 quick reference table**

| Field | Value |
| --- | --- |
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
| Registration threshold | NPR 5,000,000 (goods/carriage) · NPR 3,000,000 (services or mixed) — services/mixed raised from NPR 2M eff. Shrawan 1, 2081 (16 Jul 2024) |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Verified by Ashish Bista (ICAN: 1765) on 2026-06-06 |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 13% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Nepal |
| Unknown business-use proportion | 0% recovery |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: Nabil Bank, NIC Asia Bank, Nepal Bank, Rastriya Banijya Bank, Himalayan Bank, Everest Bank, Standard Chartered Nepal, or any other.

### Nepal-specific refusal catalogue

- **R-NP-1 — Special Economic Zone entity** — Trigger: client in SEZ. Message: "SEZ entities have special VAT treatment. Please escalate."
- **R-NP-2 — Hydropower and infrastructure projects** — Trigger: client with government infrastructure concession. Message: "Infrastructure projects have bespoke VAT exemptions. Please escalate."

## Section 3 — Supplier pattern library

### 3.1 Nepalese banks (fees exempt — exclude)

**Nepalese banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NABIL, NABIL BANK | EXCLUDE for bank charges | Exempt |
| NIC ASIA, NIC ASIA BANK | EXCLUDE for bank charges | Same |
| NEPAL BANK, RASTRIYA BANIJYA | EXCLUDE for bank charges | Same |
| HIMALAYAN BANK, EVEREST BANK | EXCLUDE for bank charges | Same |
| STANDARD CHARTERED NP | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

**Government pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IRD, INLAND REVENUE | EXCLUDE | Tax payment |
| CUSTOMS, NEPAL CUSTOMS | EXCLUDE | Duty |
| SSF, SOCIAL SECURITY FUND | EXCLUDE | Social security |
| COMPANY REGISTRAR, OCR | EXCLUDE | Registration fee |

### 3.3 Utilities

**Utilities pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NEA, NEPAL ELECTRICITY | Domestic 13% | Electricity |
| KUKL, KATHMANDU WATER | Domestic 13% | Water |
| NTC, NEPAL TELECOM, NCELL | Domestic 13% | Telecoms |

### 3.4 Digital payments

**Digital payments pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ESEWA, KHALTI, IME PAY | EXCLUDE for fees | Financial service fees exempt |
| FONEPAY | EXCLUDE for fees | Same |

### 3.5 SaaS and international services

**SaaS and international services pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, META, AWS | Self-assess 13% | Non-resident |
| ZOOM, SLACK, CANVA | Self-assess 13% | Same |

### 3.6 Payroll and exclusions

**Payroll and exclusions pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES, TLAB | EXCLUDE | Outside VAT scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 13%

**Input line:** `05.04.2026 ; KATHMANDU TRADING ; CREDIT ; Invoice NP-041 ; NPR 113,000`

**Reasoning:** Domestic. 13%. Net = NPR 100,000, VAT = NPR 13,000.

**Example 1 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | KATHMANDU TRADING | +113,000 | +100,000 | 13,000 | 13% | Output | N | — |

### Example 2 — Export, zero-rated

**Input line:** `15.04.2026 ; INDIAN BUYER LTD ; CREDIT ; Exported handicrafts ; NPR 500,000`

**Example 2 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | INDIAN BUYER LTD | +500,000 | +500,000 | 0 | 0% | Zero-rated | N | — |

### Example 3 — Non-resident digital service

**Input line:** `18.04.2026 ; GOOGLE ; DEBIT ; Google Ads ; NPR -23,000`

**Example 3 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | GOOGLE | -23,000 | -23,000 | 2,990 | 13% | Output + Input | N | — |

### Example 4 — Bank charges

**Input line:** `30.04.2026 ; NABIL BANK ; DEBIT ; Service charge ; NPR -500`

**Example 4 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30.04.2026 | NABIL BANK | -500 | — | — | — | — | N | "Exempt" |

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 13% — Default for all taxable supplies.

- **Standard rate default** — Default for all taxable supplies.

### 5.2 Zero rate — Exports, supplies to SEZ.

- **Zero rate** — Exports, supplies to SEZ.

### 5.3 Exempt — Basic agriculture, education, healthcare, financial services, public transport.

- **Exempt** — Basic agriculture, education, healthcare, financial services, public transport.

### 5.4 Input tax credit — Valid VAT invoice with PAN required. Business purpose.

- **Input tax credit** — Valid VAT invoice with PAN required. Business purpose.

### 5.5 Blocked input — Personal consumption, entertainment, passenger vehicles.

- **Blocked input** — Personal consumption, entertainment, passenger vehicles.

### 5.6 Imports — VAT at 13% on CIF plus duty.

- **Imports** — VAT at 13% on CIF plus duty.

### 5.7 Reverse charge — Non-resident services: self-assess 13%.

- **Reverse charge** — Non-resident services: self-assess 13%.

### 5.8 VAT billing software — IRD requires use of approved billing software for invoice generation.

- **VAT billing software** — IRD requires use of approved billing software for invoice generation.

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — Default: 0%.

- **Vehicle costs** — Default: 0%.

### 6.2 Entertainment — Default: block.

- **Entertainment** — Default: block.

### 6.3 SaaS entities — Default: self-assess 13%.

- **SaaS entities** — Default: self-assess 13%.

### 6.4 Cash withdrawals — Default: exclude.

- **Cash withdrawals** — Default: exclude.

### 6.5 Mixed-use expenses — Default: 0% recovery.

- **Mixed-use expenses** — Default: 0% recovery.

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Nepal fields: Output 13%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT.

## Section 8 — Bank statement reading guide

Nabil and NIC Asia exports CSV. NPR primary. Devanagari script descriptions possible — treat transliterated equivalents the same. Internal transfers: exclude. Convert foreign currency at Nepal Rastra Bank rate.

## Section 9 — Onboarding fallback

### 9.1 PAN — "What is your Permanent Account Number?"

"What is your Permanent Account Number?"

### 9.2 Filing period — Monthly. "Which month?"

Monthly. "Which month?"

### 9.3 Industry — "What does the business do?"

"What does the business do?"

### 9.4 Exports — "Do you export?"

"Do you export?"

### 9.5 Credit brought forward — Always ask.

Always ask.

## Section 10 — Reference material

### Sources

1. Nepal Value Added Tax Act 2052 (1996, as amended). 2. IRD guidelines. 3. IRD e-filing portal.

### Known gaps

1. SEZ entities refused. 2. Hydropower/infrastructure refused.

### Change log

- v2.1 (June 2026): Added jurisdiction/verification frontmatter; added VAT registration thresholds (NPR 5M goods / 3M services, FY 2082/83); removed duplicate disclaimer; 13% rate re-confirmed for FY 2082/83.
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
