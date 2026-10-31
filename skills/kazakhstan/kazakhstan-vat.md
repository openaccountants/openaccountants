---
name: kazakhstan-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Kazakhstan VAT (NDS) return (Form 300.00) for any client. Trigger on phrases like "Kazakhstan VAT", "NDS return", "Form 300", "KGD filing", or any request involving Kazakh VAT. This skill covers standard NDS payers filing quarterly returns. Simplified declaration and special tax regimes are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Kazakhstan VAT work.
version: 2.0
jurisdiction: KZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kazakhstan VAT

## Section 1 — Quick reference

**Quick reference field/value table**

| Field | Value |
| --- | --- |
| Country | Kazakhstan (Republic of Kazakhstan) |
| Tax name | NDS (Nalog na Dobavlennuyu Stoimost / VAT) |
| Standard rate | 12% |
| Reduced rates | None (single standard rate for domestic) |
| Zero rate | 0% (exports, international transport, certain agricultural) |
| Return form | Form 300.00 (quarterly NDS declaration) |
| Filing portal | https://cabinet.salyk.kz |
| Authority | Committee of State Revenue (KGD) under Ministry of Finance |
| Currency | KZT (Kazakhstani Tenge) only |
| Filing frequency | Quarterly |
| Deadline | 15th of the second month following the quarter end |
| EAEU membership | Yes — special rules for intra-EAEU trade (Russia, Belarus, Armenia, Kyrgyzstan) |
| Companion skill | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | April 2026 |

**Key Form 300.00 lines**

| Line | Meaning |
| --- | --- |
| 300.00.001 | Taxable turnover at 12% |
| 300.00.002 | Zero-rated turnover (exports) |
| 300.00.003 | Exempt turnover |
| 300.00.004 | Reverse charge on imported services |
| 300.00.005 | EAEU goods imports |
| 300.00.006 | Total output NDS |
| 300.00.007 | Input NDS on domestic purchases |
| 300.00.008 | Import NDS (customs) |
| 300.00.009 | EAEU import NDS |
| 300.00.010 | Input NDS on reverse charge |
| 300.00.011 | Total input NDS |
| 300.00.012 | Net NDS payable or excess |
| 300.00.013 | Excess carried forward |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 12% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Kazakhstan |
| Unknown EAEU vs non-EAEU origin | Non-EAEU (customs) |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (300.00.004/010) |
| Unknown blocked-input status | Blocked |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | KZT 5,000,000 |
| HIGH tax-delta on a single default | KZT 300,000 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net NDS position | KZT 10,000,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Minimum viable inputs** — Bank statement for the quarter. Acceptable from: Halyk Bank, Kaspi Bank, Forte Bank, Jusan Bank, Bank CenterCredit, Otbasy Bank, or any other.
- **Recommended inputs** — Electronic invoices (ESF from esf.gov.kz), client BIN/IIN.
- **Ideal inputs** — Complete ESF register, EAEU import documentation, Form 328.00 (EAEU import declaration), prior Form 300.00.

### Refusal catalogue

- **R-KZ-1 — Simplified declaration** — "Simplified declaration entities have different NDS rules. Out of scope." (Trigger: client on simplified regime)
- **R-KZ-2 — Special tax regime (patent, fixed)** — "Special regimes may not require NDS returns. Out of scope." (Trigger: patent or fixed deduction regime)
- **R-KZ-3 — Partial exemption** — "Input NDS apportionment required." (Trigger: mixed taxable and exempt)
- **R-KZ-4 — EAEU complex transactions** — "Complex EAEU transactions require specialist. Out of scope." (Trigger: EAEU triangulation/tolling)
- **R-KZ-5 — Income tax** — "This skill handles NDS only." (Trigger: user asks about CIT/PIT)

## Section 3 — Supplier pattern library

### 3.1 Kazakh banks (fees exempt — exclude)

**Kazakh banks pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| HALYK BANK, HALYK | EXCLUDE | Financial service, exempt |
| KASPI BANK, KASPI | EXCLUDE | Same |
| FORTE BANK, JUSAN BANK | EXCLUDE | Same |
| BANK CENTERCREDIT, OTBASY BANK | EXCLUDE | Same |
| PROTSENTY, INTEREST | EXCLUDE | Interest |
| KREDIT, ZAIM | EXCLUDE | Loan principal |

### 3.2 Government and statutory bodies (exclude)

**Government and statutory bodies pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| KGD, SALYK, TAX COMMITTEE | EXCLUDE | Tax payment |
| TAMOZHNYA, CUSTOMS | EXCLUDE | Duty (import NDS separate) |
| SOCIAL FUND, GFSS | EXCLUDE | Social contributions |
| GOVERNMENT OF RK | EXCLUDE | Government fee |

### 3.3 Utilities

**Utilities pattern table**

| Pattern | Treatment | Box | Notes |
| --- | --- | --- | --- |
| SAMRUK-ENERGO, KEGOC, AREK | Domestic 12% | 300.00.007 | Electricity |
| ALMATY SU, ASTANA SU | Domestic 12% | 300.00.007 | Water |
| KAZAKHTELECOM, KCELL, BEELINE KZ, TELE2 KZ | Domestic 12% | 300.00.007 | Telecoms |

### 3.4 Insurance (exempt — exclude)

**Insurance pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| EURASIA INSURANCE, KAZKOM STRAKHOVANIE | EXCLUDE | Exempt |
| STRAKHOVANIE, INSURANCE | EXCLUDE | Same |

### 3.5 Food and entertainment (blocked)

**Food and entertainment pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MAGNUM, SMALL, RAMSTORE | Default BLOCK | Personal provisioning |
| RESTORAN, KAFE, BAR | Default BLOCK | Entertainment blocked |

### 3.6 SaaS — non-resident (reverse charge)

**SaaS non-resident pattern table**

| Pattern | Box | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META | 300.00.004/010 | Reverse charge at 12% |
| SLACK, ZOOM, NOTION, AWS, ANTHROPIC, OPENAI | 300.00.004/010 | Same |

### 3.7 EAEU suppliers

**EAEU suppliers pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Russian, Belarusian, Armenian, Kyrgyz suppliers | EAEU import — 300.00.005/009 | Form 328.00 required |

### 3.8 Professional services

**Professional services pattern table**

| Pattern | Treatment | Box | Notes |
| --- | --- | --- | --- |
| NOTER, NOTARY | Domestic 12% | 300.00.007 | If business purpose |
| AUDITOR, BUKHGALTER | Domestic 12% | 300.00.007 | Deductible |
| ADVOKAT, LAWYER | Domestic 12% | 300.00.007 | If business matter |

### 3.9 Payroll and exclusions

**Payroll and exclusions pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ZARPLATA, SALARY | EXCLUDE | Wages |
| DIVIDEND | EXCLUDE | Out of scope |
| VNUTRENNIY, INTERNAL | EXCLUDE | Internal |
| BANKOMAT, ATM | TIER 2 — ask | Default exclude |

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge

**Example 1 worked table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03.04.2026 | NOTION LABS INC | -7,520 | -7,520 | 902 | 12% | 010 | 004 | N |

**Input line:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; USD 16.00 ; KZT 7,520`

**Reasoning:** US entity. Reverse charge at 12%. 300.00.004 (base/output), 300.00.010 (input credit). Net zero.

### Example 2 — Domestic utility

**Example 2 worked table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | KAZAKHTELECOM | -18,500 | -16,518 | -1,982 | 12% | 007 | N |

**Input line:** `10.04.2026 ; KAZAKHTELECOM ; DEBIT ; Internet Q2 ; -18,500 ; KZT`

### Example 3 — Entertainment blocked

**Example 3 worked table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | RESTORAN ZHETI KAZYNA | -35,000 | -35,000 | 0 | — | — | Y | "Entertainment: blocked" |

**Input line:** `15.04.2026 ; RESTORAN ZHETI KAZYNA ; DEBIT ; Dinner ; -35,000 ; KZT`

### Example 4 — Export (zero-rated)

**Example 4 worked table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22.04.2026 | TECHCORP GMBH | +2,850,000 | +2,850,000 | 0 | 0% | 002 | Y | "Verify export docs" |

**Input line:** `22.04.2026 ; TECHCORP GMBH ; CREDIT ; IT services ; +2,850,000 ; KZT`

### Example 5 — EAEU import (from Russia)

**Example 5 worked table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | OOO TECHNOPARK | -1,500,000 | -1,500,000 | 180,000 | 12% | 009 | 005 | N |

**Input line:** `18.04.2026 ; OOO TECHNOPARK ; DEBIT ; Equipment ; -1,500,000 ; KZT`

**Reasoning:** Russian supplier, EAEU protocol. Self-assess NDS. Form 328.00 required.

### Example 6 — Motor vehicle blocked

**Example 6 worked table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28.04.2026 | ASTANA MOTORS | -450,000 | -450,000 | 0 | — | — | Y | "Vehicle: blocked" |

**Input line:** `28.04.2026 ; ASTANA MOTORS ; DEBIT ; Car lease ; -450,000 ; KZT`

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 12% (Tax Code Article 422)

- **Unknown rate on a sale** — 12%

### 5.2 Zero rate

- **Zero rate application** — Exports, international transport, certain agricultural produce. 300.00.002.

### 5.3 Exempt supplies

- **Exempt supply categories** — Financial, insurance, medical, educational, residential rental, public transport.

### 5.4 Reverse charge — non-resident services

- **Reverse charge treatment** — Self-assess at 12%. 300.00.004 (output), 300.00.010 (input). Net zero.

### 5.5 EAEU imports

- **EAEU imports treatment** — From Russia, Belarus, Armenia, Kyrgyzstan. Self-assessed NDS, not at customs. 300.00.005/009. Form 328.00 by 20th of month following import.

### 5.6 Non-EAEU imports

- **Non-EAEU imports treatment** — At customs. 12%. 300.00.008. Recoverable.

### 5.7 Blocked input NDS

- **Blocked input categories** — Passenger vehicles, entertainment, personal consumption, no valid ESF/invoice.

### 5.8 Electronic invoicing (ESF)

- **ESF requirement** — Mandatory electronic invoices via esf.gov.kz. Input NDS requires valid ESF.

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel/vehicles — *Default:* 0%. *Question:* "Car or commercial?"

- **Fuel/vehicles default and question** — Default: 0%. Question: "Car or commercial?"

### 6.2 Entertainment — *Default:* block.

- **Entertainment default** — Default: block.

### 6.3 SaaS entities — *Default:* reverse charge at 12%.

- **SaaS entities default** — Default: reverse charge at 12%.

### 6.4 EAEU vs non-EAEU — *Default:* non-EAEU. *Question:* "EAEU country supplier?"

- **EAEU vs non-EAEU default and question** — Default: non-EAEU. Question: "EAEU country supplier?"

### 6.5 Owner transfers — *Default:* exclude.

- **Owner transfers default** — Default: exclude.

### 6.6 Foreign incoming — *Default:* zero-rated. *Question:* "Export docs?"

- **Foreign incoming default and question** — Default: zero-rated. Question: "Export docs?"

### 6.7 Large purchases — *Question:* "Fixed asset?"

- **Large purchases question** — Question: "Fixed asset?"

### 6.8 Cash withdrawals — *Default:* exclude.

- **Cash withdrawals default** — Default: exclude.

### 6.9 Rent — *Default:* no NDS. *Question:* "Commercial with NDS?"

- **Rent default and question** — Default: no NDS. Question: "Commercial with NDS?"

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3 with Kazakhstan Form 300.00 line codes.

## Section 8 — Kazakh bank statement reading guide

**CSV conventions.** Halyk Bank and Kaspi Bank export with semicolons, DD.MM.YYYY. Kaspi app exports may be in JSON or XLS.

- **Russian/Kazakh terms** — Zarplata (salary), protsenty (interest), kredit (loan), nalichnye (cash), vnutrenniy (internal), tamozhnya (customs).

**Kaspi specifics.** Kaspi Bank statements may show Kaspi Gold card transactions mixed with business. Separate personal from business carefully.

- **Internal transfers** — Between client's accounts. Always exclude.
- **Foreign currency** — Convert to KZT at National Bank of Kazakhstan rate.
- **EAEU indicators** — Payments to/from RU, BY, AM, KG IBANs or counterparties.

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Fallback:* "IE or company (TOO/AO)?"

- **Entity type fallback** — Fallback: "IE or company (TOO/AO)?"

### 9.2 NDS registration — *Fallback:* "Standard NDS payer?"

- **NDS registration fallback** — Fallback: "Standard NDS payer?"

### 9.3 BIN/IIN — *Fallback:* "What is your BIN or IIN?"

- **BIN/IIN fallback** — Fallback: "What is your BIN or IIN?"

### 9.4 Period — *Inference:* statement dates (quarterly).

- **Period inference** — Inference: statement dates (quarterly).

### 9.5 Industry — *Fallback:* "What does the business do?"

- **Industry fallback** — Fallback: "What does the business do?"

### 9.6 EAEU trade — *Fallback:* "Trade with EAEU countries?"

- **EAEU trade fallback** — Fallback: "Trade with EAEU countries?"

### 9.7 Credit B/F — *Always ask.*

- **Credit B/F rule** — Always ask.

### 9.8 Cross-border — *Fallback:* "Customers outside Kazakhstan?"

- **Cross-border fallback** — Fallback: "Customers outside Kazakhstan?"

## Section 10 — Reference material

### Sources

- **Reference sources list** — 1. Tax Code of Kazakhstan — Chapter 46-50 (NDS) 2. EAEU Treaty, Annex on Indirect Taxes 3. KGD — https://cabinet.salyk.kz 4. ESF portal — https://esf.gov.kz 5. National Bank of Kazakhstan — https://www.nationalbank.kz

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure.

## End of Kazakhstan VAT (NDS) Skill v2.0

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
