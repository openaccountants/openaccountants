---
name: pakistan-sales-tax
description: Use this skill whenever asked to prepare, review, or classify transactions for a Pakistan Sales Tax return (federal or provincial) for any client. Trigger on phrases like "Pakistan sales tax", "FBR return", "IRIS portal", "Sindh sales tax", "Punjab sales tax", or any request involving Pakistan sales tax. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Pakistan sales tax work.
version: 2.0
---

# Pakistan Sales Tax Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Pakistan (Islamic Republic of Pakistan) |
| Federal Sales Tax rate (goods) | 18% (standard); 25% (luxury/sin goods); reduced rates via SRO |
| Provincial Sales Tax rate (services) | Varies: Sindh 13%, Punjab 16%, KP 15%, Balochistan 15% |
| Zero rate | 0% (exports, certain essential goods via SRO) |
| Exempt | Basic food (unprocessed), education, healthcare, financial services |
| Return form | Federal: monthly via IRIS; Provincial: via respective portals |
| Filing portal | https://iris.fbr.gov.pk (IRIS — federal); SRB/PRA/KPRA/BRA portals (provincial) |
| Authority | Federal Board of Revenue (FBR) — goods; SRB/PRA/KPRA/BRA — services |
| Currency | PKR (Pakistani Rupee) |
| Filing frequency | Monthly (federal and most provincial) |
| Deadline | Federal: 18th of following month; Provincial: varies (typically 15th-18th) |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**CRITICAL: Pakistan has SPLIT federal/provincial sales tax.** Federal covers goods (FBR). Provincial covers services (SRB for Sindh, PRA for Punjab, KPRA for KP, BRA for Balochistan). A single business may file BOTH.

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on goods | 18% (federal) |
| Unknown rate on services | Apply province rate based on client location |
| Unknown input tax status | Not deductible |
| Unknown counterparty location | Domestic Pakistan |
| Unknown business-use proportion | 0% recovery |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: HBL (Habib Bank), UBL (United Bank), MCB (Muslim Commercial Bank), Allied Bank, Bank Alfalah, Meezan Bank, Standard Chartered PK, or any other. JazzCash and Easypaisa statements also accepted.

**Recommended** — sales invoices, purchase invoices with supplier NTN/STRN, client's NTN and STRN.

### Pakistan-specific refusal catalogue

**R-PK-1 — Provincial service tax complexity.** Trigger: client provides services in multiple provinces. Message: "Multi-province service tax filing requires separate returns to each provincial authority. Please escalate for province-by-province analysis."

**R-PK-2 — Manufacturing under SRO regime.** Trigger: client is a manufacturer with SRO-based reduced rates or exemptions. Message: "SRO-based manufacturing exemptions require gazette-level verification. Please escalate."

**R-PK-3 — Withholding agent (sales tax).** Trigger: client is a designated withholding agent for sales tax. Message: "Withholding agent obligations require tracking of certificates and deposits. Please escalate."

**R-PK-4 — Export-oriented units (EOU).** Trigger: client in export-oriented unit with zero-rating facility. Message: "EOU zero-rating requires SRO-level verification. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Pakistani banks (fees — check)

| Pattern | Treatment | Notes |
|---|---|---|
| HBL, HABIB BANK | EXCLUDE for bank charges | Financial service (provincial ST may apply) |
| UBL, UNITED BANK | EXCLUDE for bank charges | Same |
| MCB, MUSLIM COMMERCIAL | EXCLUDE for bank charges | Same |
| ALLIED BANK, BANK ALFALAH | EXCLUDE for bank charges | Same |
| MEEZAN BANK | EXCLUDE for bank charges | Same |
| STANDARD CHARTERED PK | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Mobile financial services

| Pattern | Treatment | Notes |
|---|---|---|
| JAZZCASH, JAZZ CASH | EXCLUDE for transaction fees | Financial service |
| EASYPAISA, EASY PAISA | EXCLUDE for transaction fees | Same |
| NAYAPAY, SADAPAY | EXCLUDE for transaction fees | Same |

### 3.3 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| FBR, FEDERAL BOARD OF REVENUE | EXCLUDE | Tax payment |
| CUSTOMS, PAKISTAN CUSTOMS | EXCLUDE | Duty |
| SRB, SINDH REVENUE, PRA, PUNJAB REVENUE | EXCLUDE | Provincial tax payment |
| EOBI, SOCIAL SECURITY | EXCLUDE | Social security |
| SECP | EXCLUDE | Registration fee |

### 3.4 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| K-ELECTRIC, KESC, LESCO, FESCO, IESCO | Domestic 18% (federal ST on electricity) | Electricity |
| SSGC, SNGPL | Domestic 18% | Gas |
| PTCL, JAZZ, ZONG, TELENOR, UFONE | Provincial service tax applies | Telecoms |

### 3.5 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess (federal 18% on digital goods; provincial on services) | Non-resident |
| ZOOM, SLACK, CANVA, FIGMA | Self-assess | Same |

### 3.6 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| AUDIT, CA FIRM, ACCOUNTING | Provincial service tax | Check province |
| LAW FIRM, ADVOCATE | Provincial service tax | Same |
| CONSULTANT, ENGINEERING | Provincial service tax | Same |

### 3.7 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES, TANKHWAH | EXCLUDE | Outside sales tax scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal |
| CASH WITHDRAWAL, ATM | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Federal sales tax on goods at 18%

**Input line:** `05.04.2026 ; DOMESTIC BUYER LTD ; CREDIT ; Invoice PK-041 manufactured goods ; PKR 1,180,000`

**Reasoning:** Manufacturer selling taxable goods. Federal 18%. Net = PKR 1,000,000, ST = PKR 180,000.

| Date | Counterparty | Gross | Net | Tax | Rate | Authority | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | DOMESTIC BUYER | +1,180,000 | +1,000,000 | 180,000 | 18% | FBR | N | — |

### Example 2 — Provincial service tax (Sindh 13%)

**Input line:** `10.04.2026 ; CLIENT CO ; CREDIT ; Consulting fee ; PKR 226,000`

**Reasoning:** Service in Sindh. SRB 13%. Net = PKR 200,000, Tax = PKR 26,000.

| Date | Counterparty | Gross | Net | Tax | Rate | Authority | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | CLIENT CO | +226,000 | +200,000 | 26,000 | 13% | SRB | N | — |

### Example 3 — Export, zero-rated

**Input line:** `15.04.2026 ; US IMPORTER INC ; CREDIT ; Textile export ; PKR 5,000,000`

| Date | Counterparty | Gross | Net | Tax | Rate | Authority | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | US IMPORTER INC | +5,000,000 | +5,000,000 | 0 | 0% | FBR | N | — |

### Example 4 — Non-resident digital service

**Input line:** `18.04.2026 ; GOOGLE CLOUD ; DEBIT ; Cloud April ; PKR -50,000`

**Reasoning:** Non-resident digital service. Self-assess federal 18%. Input credit if for taxable supplies.

| Date | Counterparty | Gross | Net | Tax | Rate | Authority | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | GOOGLE CLOUD | -50,000 | -50,000 | 9,000 | 18% | FBR | N | — |

### Example 5 — JazzCash transfer fee

**Input line:** `25.04.2026 ; JAZZCASH ; DEBIT ; Transfer fee ; PKR -50`

| Date | Counterparty | Gross | Net | Tax | Rate | Authority | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 25.04.2026 | JAZZCASH | -50 | — | — | — | — | N | "Financial service" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Federal sales tax on goods — 18% standard. Manufacturers, importers, and specified retailers.
### 5.2 Provincial service tax — Varies by province (Sindh 13%, Punjab 16%, KP 15%, Balochistan 15%).
### 5.3 Zero rate — Exports (federal). Input tax credit available.
### 5.4 Exempt — Basic food (unprocessed), education, healthcare.
### 5.5 Input tax credit — Federal: available on goods. Provincial: varies. Valid invoice with NTN/STRN required.
### 5.6 Blocked input — Personal consumption, entertainment, passenger vehicles.
### 5.7 Imports — Federal sales tax at customs. Provincial not applicable at import.
### 5.8 Reverse charge — Non-resident services: self-assess.
### 5.9 Withholding — Designated agents withhold sales tax at prescribed rates.
### 5.10 Further tax / extra tax — Additional levies on sales to unregistered persons.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Federal vs provincial split — Default: flag. Question: "Is this goods (FBR) or services (provincial)?"
### 6.2 Province identification — Default: client's registered province. Question: "Which province is the service provided in?"
### 6.3 SaaS entities — Default: self-assess federal 18%. Question: "Goods or services? Check invoice."
### 6.4 Cash withdrawals ��� Default: exclude.
### 6.5 JazzCash/Easypaisa transactions — Default: classify underlying transaction, not payment method.

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Pakistan fields: Federal output 18%, Zero-rated, Exempt, Federal input, Provincial output (by province), Provincial input, Net payable (federal), Net payable (provincial).

---

## Section 8 — Bank statement reading guide

HBL, UBL, MCB exports CSV. PKR primary. JazzCash/Easypaisa exports also usable. Urdu descriptions possible. Internal transfers: exclude. Convert foreign currency at SBP rate.

---

## Section 9 — Onboarding fallback

### 9.1 NTN/STRN ��� "What is your FBR NTN? Provincial STRN?"
### 9.2 Province — "Where is the business registered?"
### 9.3 Registration type — "Federal (goods), provincial (services), or both?"
### 9.4 Filing period — Monthly. "Which month?"
### 9.5 Exports — "Do you export?"
### 9.6 Credit brought forward — Always ask.

---

## Section 10 — Reference material

### Sources
1. Sales Tax Act 1990 (federal, as amended). 2. Provincial sales tax acts (Sindh, Punjab, KP, Balochistan). 3. FBR IRIS portal. 4. SROs for exemptions and reduced rates.

### Known gaps
1. Multi-province filing refused. 2. SRO-based manufacturing exemptions refused. 3. Withholding agent obligations refused. 4. Provincial rate changes frequent — verify before filing.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure. Federal/provincial split emphasized.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).
