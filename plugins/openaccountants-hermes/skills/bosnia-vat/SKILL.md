---
name: bosnia-vat
description: "Use this skill whenever asked to prepare, review, or classify transactions for a Bosnia and Herzegovina VAT (PDV) return for any client. Trigger on phrases like \"Bosnia VAT\", \"BiH VAT\", \"PDV return\", \"ITA filing\", or any request involving Bosnian VAT. Bosnia has a unique single-rate system at 17%. This skill covers standard PDV payers filing monthly returns. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Bosnian VAT work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bosnia-vat"
  jurisdiction: "BA"
  tax_year: "2025"
  last_updated: "2026-07-13"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Bosnia VAT

## Section 1 — Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Bosnia and Herzegovina (BiH) |
| Tax name | PDV (Porez na Dodatu Vrijednost) |
| Standard rate | 17% (single rate — lowest in Europe) |
| Reduced rates | None |
| Zero rate | 0% (exports, international transport) |
| Return form | Monthly PDV declaration (PDV-MO form) |
| Filing portal | https://www.uino.gov.ba (ITA e-portal) |
| Authority | Indirect Taxation Authority (ITA / UIO — Uprava za Indirektno Oporezivanje) |
| Currency | BAM / KM (Convertible Mark) only — pegged to EUR at 1.95583 |
| Filing frequency | Monthly |
| Deadline | 10th of the month following the reporting month |
| Companion skill | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending local practitioner validation |
| Validation date | April 2026 |

**Key PDV return boxes**

| Box | Meaning |
| --- | --- |
| 11 | Domestic taxable supplies at 17% — base |
| 12 | Output PDV at 17% |
| 21 | Zero-rated supplies (exports) |
| 22 | Exempt supplies |
| 31 | Reverse charge on imported services — base |
| 32 | Output PDV on reverse charge |
| 41 | Total output PDV |
| 51 | Input PDV on domestic purchases |
| 52 | Import PDV (paid at customs) |
| 53 | Input PDV on reverse charge (creditable) |
| 61 | Total input PDV |
| 71 | Net PDV payable or credit |
| 72 | Credit brought forward |
| 73 | Net payable |

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 17% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic BiH |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (Box 31/32/53) |
| Unknown blocked-input status | Blocked |

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | BAM 6,000 |
| HIGH tax-delta on a single default | BAM 400 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net PDV position | BAM 10,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: UniCredit Bank BiH, Raiffeisen Bank BiH, Intesa Sanpaolo BiH, NLB Banka, Sparkasse Bank, ASA Banka, or any other.

**Recommended** — invoices, client ID number (IDB/JIB), prior PDV return.

**Ideal** — complete invoice register, customs documentation, prior period credit.

### Refusal catalogue

- **R-BA-1 — Non-registered entity** — Trigger: client not PDV registered (below BAM 50,000 threshold and not voluntarily registered). Message: "Non-registered entities cannot file PDV returns. Out of scope."  _(R-BA-1)_
- **R-BA-2 — Partial exemption** — Trigger: mixed taxable and exempt supplies. Message: "Input PDV apportionment required. Use a qualified practitioner."  _(R-BA-2)_
- **R-BA-3 — Income tax** — Trigger: user asks about income tax. Message: "This skill handles PDV only. Note: income tax is at entity level (Federation, RS, Brcko)."  _(R-BA-3)_
- **R-BA-4 — Entity-level tax (FBiH vs RS vs Brcko)** — Trigger: entity-level tax question. Message: "Direct taxes are administered by entity authorities (FBiH, RS, Brcko), not the ITA. Out of scope."  _(R-BA-4)_

## Section 3 — Supplier pattern library

### 3.1 BiH banks (fees exempt — exclude)

**BiH banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UNICREDIT BA, UNICREDIT BANK BIH | EXCLUDE | Financial service, exempt |
| RAIFFEISEN BA, RAIFFEISEN BANK BIH | EXCLUDE | Same |
| INTESA SANPAOLO BIH, NLB BANKA | EXCLUDE | Same |
| SPARKASSE, ASA BANKA | EXCLUDE | Same |
| KAMATA, INTEREST | EXCLUDE | Interest |
| KREDIT, LOAN | EXCLUDE | Loan principal |

### 3.2 Government and statutory bodies (exclude)

**Government and statutory bodies table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UIO, ITA, UINO | EXCLUDE | PDV payment |
| CARINA, CUSTOMS | EXCLUDE | Duty (import PDV separate) |
| PIO, PENSION, ZDRAVSTVO, HEALTH INSURANCE | EXCLUDE | Social/health contributions |
| POREZNA UPRAVA | EXCLUDE | Entity tax authority |

### 3.3 Utilities

**Utilities table**

| Pattern | Treatment | Box | Notes |
| --- | --- | --- | --- |
| ELEKTROPRIVREDA, EP BIH, EP RS, EP HZHB | Domestic 17% | 51 | Electricity |
| VODOVOD, VODOKANAL | Domestic 17% | 51 | Water |
| BH TELECOM, M:TEL, HT ERONET | Domestic 17% | 51 | Telecoms |
| SARAJEVOGAS, GASPROMET | Domestic 17% | 51 | Gas |

### 3.4 Insurance (exempt — exclude)

**Insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SARAJEVO OSIGURANJE, TRIGLAV BH, UNIQA BH | EXCLUDE | Exempt |
| OSIGURANJE, INSURANCE | EXCLUDE | Same |

### 3.5 Food and entertainment (blocked)

**Food and entertainment table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BINGO, KONZUM, MERCATOR BH | Default BLOCK | Personal provisioning |
| RESTORAN, KAFANA, BAR, KAFIC | Default BLOCK | Entertainment blocked |

### 3.6 SaaS — non-resident (reverse charge)

**SaaS non-resident table**

| Pattern | Box | Notes |
| --- | --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META | 31/32/53 | Reverse charge at 17% |
| SLACK, ZOOM, NOTION, AWS, ANTHROPIC, OPENAI | 31/32/53 | Same |

### 3.7 Professional services

**Professional services table**

| Pattern | Treatment | Box | Notes |
| --- | --- | --- | --- |
| NOTAR, NOTARY | Domestic 17% | 51 | If business purpose |
| REVIZOR, AUDITOR, KNJIGOVODJA | Domestic 17% | 51 | Deductible |
| ADVOKAT, LAWYER | Domestic 17% | 51 | If business matter |

### 3.8 Payroll and exclusions

**Payroll and exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PLATA, SALARY | EXCLUDE | Wages |
| DIVIDENDA | EXCLUDE | Out of scope |
| INTERNI, INTERNAL | EXCLUDE | Internal transfer |
| BANKOMAT, ATM | TIER 2 — ask | Default exclude |

## Section 4 — Worked examples

### Example 1 — Non-resident SaaS reverse charge

**Input line:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Subscription ; USD 16.00 ; BAM 29.60`

**Reasoning:** US entity. Reverse charge at 17%. Box 31 (base), Box 32 (output), Box 53 (input credit). Net zero.

**Example 1 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (in) | Box (out) | Default? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 03.04.2026 | NOTION LABS INC | -29.60 | -29.60 | 5.03 | 17% | 53 | 31/32 | N |

### Example 2 — Domestic utility

**Input line:** `10.04.2026 ; BH TELECOM ; DEBIT ; Internet April ; -58.50 ; BAM`

**Example 2 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | BH TELECOM | -58.50 | -50.00 | -8.50 | 17% | 51 | N |

### Example 3 — Entertainment blocked

**Input line:** `15.04.2026 ; RESTORAN PARK PRINCEVA ; DEBIT ; Business dinner ; -175.00 ; BAM`

**Example 3 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | RESTORAN PARK PRINCEVA | -175.00 | -175.00 | 0 | — | — | Y | "Entertainment: blocked" |

### Example 4 — Export (zero-rated)

**Input line:** `22.04.2026 ; TECHCORP GMBH ; CREDIT ; IT services ; +6,800.00 ; BAM`

**Example 4 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22.04.2026 | TECHCORP GMBH | +6,800 | +6,800 | 0 | 0% | 21 | Y | "Verify export docs" |

### Example 5 — Motor vehicle blocked

**Input line:** `28.04.2026 ; ASA AUTO ; DEBIT ; Car lease ; -650.00 ; BAM`

**Example 5 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28.04.2026 | ASA AUTO | -650.00 | -650.00 | 0 | — | — | Y | "Vehicle: blocked" |

### Example 6 — Import of goods

**Input line:** `25.04.2026 ; CUSTOMS/CARINA ; DEBIT ; Import PDV ; -2,500 ; BAM`

**Example 6 table**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 25.04.2026 | CUSTOMS | -2,500 | -2,137 | -363 | 17% | 52 | N |

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 17% (Law on PDV Article 24)

- **Standard rate 17%** — 17% percent (Single rate — simplest in region. No reduced rates. Sales to Box 11/12. Purchases to Box 51.)  _(Law on PDV Article 24)_

### 5.2 Zero rate

- **Zero rate** — Exports, international transport. Box 21. Requires customs documentation.  _(Section 5.2)_

### 5.3 Exempt supplies

- **Exempt supplies** — Financial, insurance, medical, educational, residential rental, postal, cultural.  _(Section 5.3)_

### 5.4 Reverse charge — non-resident services (Article 12)

- **Reverse charge non-resident services** — Self-assess at 17%. Box 31/32 (output), Box 53 (input). Net zero.  _(Article 12)_

### 5.5 Import PDV

- **Import PDV** — At customs. Base = customs value + duties. 17%. Box 52. Recoverable.  _(Section 5.5)_

### 5.6 Blocked input PDV

- **Blocked input PDV** — Passenger vehicles, entertainment, personal consumption, no valid invoice.  _(Section 5.6)_

### 5.7 Credit notes

- **Credit notes** — Both adjust in current period.  _(Section 5.7)_

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel/vehicles

- **Fuel/vehicles** — Default: 0%. Question: "Car or commercial?"  _(Section 6.1)_

### 6.2 Entertainment

- **Entertainment** — Default: block.  _(Section 6.2)_

### 6.3 SaaS entities

- **SaaS entities** — Default: reverse charge at 17%.  _(Section 6.3)_

### 6.4 Owner transfers

- **Owner transfers** — Default: exclude.  _(Section 6.4)_

### 6.5 Foreign incoming

- **Foreign incoming** — Default: zero-rated. Question: "Export docs?"  _(Section 6.5)_

### 6.6 Large purchases

- **Large purchases** — Question: "Fixed asset?"  _(Section 6.6)_

### 6.7 Mixed-use phone

- **Mixed-use phone** — Default: 0%.  _(Section 6.7)_

### 6.8 Cash withdrawals

- **Cash withdrawals** — Default: exclude.  _(Section 6.8)_

### 6.9 Rent

- **Rent** — Default: no PDV. Question: "Commercial with PDV?"  _(Section 6.9)_

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3 with BiH-specific box codes.

## Section 8 — BiH bank statement reading guide

**CSV conventions.** UniCredit BA and Raiffeisen BA use semicolons, DD.MM.YYYY dates.

**Bosnian/Croatian/Serbian terms.** Plata (salary), kamata (interest), kredit (loan), gotovina (cash), interni (internal), carina (customs), osiguranje (insurance), revizor (auditor).

**Currency note.** BAM/KM is pegged to EUR at 1.95583. Some statements show EUR equivalents.

**Internal transfers.** Between client's accounts. Always exclude.

**IBAN prefix.** BA = Bosnia and Herzegovina.

## Section 9 — Onboarding fallback

### 9.1 Entity type

- **Entity type** — Fallback: "Sole trader or company (DOO/DD)?"  _(Section 9.1)_

### 9.2 PDV registration

- **PDV registration** — Fallback: "PDV payer?"  _(Section 9.2)_

### 9.3 IDB/JIB

- **IDB/JIB** — Fallback: "What is your identification number?"  _(Section 9.3)_

### 9.4 Period

- **Period** — Inference: statement dates.  _(Section 9.4)_

### 9.5 Industry

- **Industry** — Fallback: "What does the business do?"  _(Section 9.5)_

### 9.6 Entity location

- **Entity location** — Fallback: "Federation, RS, or Brcko?" (affects entity-level taxes only)  _(Section 9.6)_

### 9.7 Credit B/F

- **Credit B/F** — Always ask.  _(Section 9.7)_

### 9.8 Cross-border

- **Cross-border** — Fallback: "Customers outside BiH?"  _(Section 9.8)_

## Section 10 — Reference material

### Sources

1. Law on VAT of BiH (Zakon o PDV-u) — Official Gazette BiH
2. ITA — https://www.uino.gov.ba
3. Central Bank of BiH rates — https://www.cbbh.ba

### Known gaps

1. Entity-level taxation (FBiH/RS/Brcko) not covered. 2. Partial exemption not covered.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 10-section structure.

## End of Bosnia and Herzegovina VAT (PDV) Skill v2.0

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bosnia-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bosnia-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
