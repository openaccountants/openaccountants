---
name: mongolia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Mongolia VAT return for any client. Trigger on phrases like "Mongolia VAT", "MTA filing", "NUAT", or any request involving Mongolia VAT. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Mongolia VAT work.
version: 2.0
jurisdiction: MN
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mongolia VAT

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Mongolia |
| Standard rate | 10% |
| Zero rate | 0% (exports) |
| Exempt | Financial services, residential rent, healthcare, education, public transport |
| Return form | Monthly VAT return |
| Filing portal | https://e-tax.mta.mn (E-Tax system) |
| Authority | Mongolian Tax Authority (MTA) |
| Currency | MNT (Mongolian Tugrik) |
| Filing frequency | Monthly |
| Deadline | 10th of the month following the tax period |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Conservative defaults:**

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 10% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Mongolia |
| Unknown business-use proportion | 0% recovery |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Minimum viable input** — Minimum viable — bank statement for the month. Acceptable from: Khan Bank, Golomt Bank, TDB (Trade and Development Bank), XacBank, State Bank, or any other.

### Mongolia-specific refusal catalogue

- **R-MN-1 — Mining and natural resources** — Trigger: client in mining sector with special tax regime. Message: "Mining sector has bespoke VAT and royalty rules. Please escalate."  _(R-MN-1)_
- **R-MN-2 — Free trade zone entity** — Trigger: client in Altanbulag or Zamiin-Uud FTZ. Message: "Free trade zone entities have special VAT treatment. Please escalate."  _(R-MN-2)_

## Section 3 — Supplier pattern library

### 3.1 Mongolian banks (fees exempt — exclude)

**Mongolian banks pattern table**  _(Exempt)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KHAN BANK, XAAH BAHK | EXCLUDE for bank charges | Exempt |
| GOLOMT, GOLOMT BANK | EXCLUDE for bank charges | Same |
| TDB, TRADE AND DEVELOPMENT | EXCLUDE for bank charges | Same |
| XACBANK, STATE BANK | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

**Government pattern table**  _(Tax payment)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MTA, TAX AUTHORITY | EXCLUDE | Tax payment |
| CUSTOMS, MONGOLIAN CUSTOMS | EXCLUDE | Duty |
| SOCIAL INSURANCE, NDSH | EXCLUDE | Social insurance |

### 3.3 Utilities

**Utilities pattern table**  _(Electricity)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UBEDN, CENTRAL ELECTRICITY | Domestic 10% | Electricity |
| USUG, WATER SUPPLY | Domestic 10% | Water |
| MOBICOM, UNITEL, SKYTEL | Domestic 10% | Telecoms |

### 3.4 SaaS and international services

**SaaS pattern table**  _(Non-resident)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, META, AWS | Self-assess 10% | Non-resident |
| ZOOM, SLACK, CANVA | Self-assess 10% | Same |

### 3.5 Payroll and exclusions

**Payroll and exclusions pattern table**  _(Outside VAT scope)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARY, WAGES | EXCLUDE | Outside VAT scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| CASH WITHDRAWAL | TIER 2 — ask | Default exclude |

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 10%

**Input line:** `05.04.2026 ; MONGOLIAN TRADING LLC ; CREDIT ; Invoice MN-041 ; MNT 11,000,000`

**Reasoning:** Domestic. 10%. Net = MNT 10,000,000, VAT = MNT 1,000,000.

**Example 1 table**  _(—)_

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | MONGOLIAN TRADING LLC | +11,000,000 | +10,000,000 | 1,000,000 | 10% | Output | N | — |

### Example 2 — Export, zero-rated

**Input line:** `15.04.2026 ; CHINESE BUYER CO ; CREDIT ; Cashmere export ; MNT 80,000,000`

**Example 2 table**  _(—)_

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | CHINESE BUYER CO | +80,000,000 | +80,000,000 | 0 | 0% | Zero-rated | N | — |

### Example 3 — Non-resident digital service

**Input line:** `18.04.2026 ; GOOGLE ; DEBIT ; Google Workspace ; MNT -500,000`

**Example 3 table**  _(—)_

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | GOOGLE | -500,000 | -500,000 | 50,000 | 10% | Output + Input | N | — |

### Example 4 — Bank charges

**Input line:** `30.04.2026 ; KHAN BANK ; DEBIT ; Service fee ; MNT -15,000`

**Example 4 table**  _("Exempt")_

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30.04.2026 | KHAN BANK | -15,000 | — | — | — | — | N | "Exempt" |

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 10% — Default for all taxable supplies.

- **Standard rate default** — Standard rate 10% — Default for all taxable supplies.

### 5.2 Zero rate — Exports with customs documentation.

- **Zero rate** — Zero rate — Exports with customs documentation.

### 5.3 Exempt — Financial services, residential rent, healthcare, education, public transport.

- **Exempt categories** — Exempt — Financial services, residential rent, healthcare, education, public transport.

### 5.4 Input tax credit — Valid VAT invoice with TIN. Business purpose. Apportionment if mixed.

- **Input tax credit** — Input tax credit — Valid VAT invoice with TIN. Business purpose. Apportionment if mixed.

### 5.5 Blocked input — Personal consumption, entertainment, passenger vehicles.

- **Blocked input** — Blocked input — Personal consumption, entertainment, passenger vehicles.

### 5.6 Imports — VAT at 10% on CIF plus duty.

- **Imports** — Imports — VAT at 10% on CIF plus duty.

### 5.7 Reverse charge — Non-resident services: self-assess 10%.

- **Reverse charge** — Reverse charge — Non-resident services: self-assess 10%.

### 5.8 E-barimt system — All sales must be registered through the E-barimt electronic invoicing system.

- **E-barimt system** — E-barimt system — All sales must be registered through the E-barimt electronic invoicing system.

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — Default: 0%. Question: "Commercial vehicle for business?"

- **Vehicle costs** — Vehicle costs — Default: 0%. Question: "Commercial vehicle for business?"

### 6.2 Entertainment — Default: block.

- **Entertainment** — Entertainment — Default: block.

### 6.3 SaaS entities — Default: self-assess 10%.

- **SaaS entities** — SaaS entities — Default: self-assess 10%.

### 6.4 Cash withdrawals — Default: exclude.

- **Cash withdrawals** — Cash withdrawals — Default: exclude.

### 6.5 E-barimt compliance — Default: required. Question: "All sales registered on E-barimt?"

- **E-barimt compliance** — E-barimt compliance — Default: required. Question: "All sales registered on E-barimt?"

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Mongolia fields: Output 10%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT.

## Section 8 — Bank statement reading guide

Khan Bank and Golomt exports CSV. MNT primary. Cyrillic descriptions common — treat transliterated equivalents the same. Internal transfers: exclude. Convert foreign currency at Bank of Mongolia rate.

## Section 9 — Onboarding fallback

### 9.1 TIN — "What is your MTA TIN?"

- **TIN question** — TIN — "What is your MTA TIN?"

### 9.2 Filing period — Monthly. "Which month?"

- **Filing period question** — Filing period — Monthly. "Which month?"

### 9.3 Industry — "What does the business do?"

- **Industry question** — Industry — "What does the business do?"

### 9.4 Exports — "Do you export?"

- **Exports question** — Exports — "Do you export?"

### 9.5 Credit brought forward — Always ask.

- **Credit brought forward** — Credit brought forward — Always ask.

## Section 10 — Reference material

### Sources

1. Mongolia VAT Law (revised). 2. MTA guidelines. 3. E-barimt system requirements.

### Known gaps

1. Mining sector refused. 2. FTZ refused. 3. E-barimt integration not fully mapped.

### Change log

- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).

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
