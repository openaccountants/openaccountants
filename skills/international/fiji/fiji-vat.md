---
name: fiji-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Fiji VAT return for any client. Trigger on phrases like "Fiji VAT", "FRCS filing", "Fiji Revenue", or any request involving Fiji VAT. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Fiji VAT work.
version: 2.0
---

# Fiji VAT Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Fiji (Republic of Fiji) |
| Standard rate | 9% |
| Zero rate | 0% (exports, basic food items, prescription medicine, education supplies) |
| Exempt | Financial services, residential rent, medical, public transport |
| Return form | VAT return (monthly or quarterly via TPOS) |
| Filing portal | https://www.frcs.org.fj (Taxpayer Online Services) |
| Authority | Fiji Revenue and Customs Service (FRCS) |
| Currency | FJD (Fiji Dollar) |
| Filing frequencies | Monthly (turnover > FJD 500,000); Quarterly (others) |
| Deadline | Last business day of month following the period |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 9% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Fiji |
| Unknown business-use proportion | 0% recovery |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | FJD 10,000 |
| HIGH tax-delta on a single default | FJD 500 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period. Acceptable from: BSP (Bank of the South Pacific), HFC Bank, ANZ Fiji, Westpac Fiji, Bred Bank Fiji.

**Recommended** — sales invoices, purchase invoices with supplier TIN, client TIN.

### Fiji-specific refusal catalogue

**R-FJ-1 — Duty-free zone operations.** Trigger: client in tax-free zone or duty-free retail. Message: "Tax-free zone operations have special VAT treatment. Please escalate."

**R-FJ-2 — Tourism levies interaction.** Trigger: hotel/resort subject to STT/ECAL. Message: "STT and ECAL interact with VAT for tourism operators. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Fijian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BSP, BANK SOUTH PACIFIC | EXCLUDE for bank charges | Financial service, exempt |
| HFC BANK, HFC | EXCLUDE for bank charges | Same |
| ANZ FIJI, WESTPAC FIJI, BRED BANK | EXCLUDE for bank charges | Same |
| INTEREST, LOAN, REPAYMENT | EXCLUDE | Out of scope |

### 3.2 Government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| FRCS, FIJI REVENUE | EXCLUDE | Tax payment |
| FNPF, FIJI NATIONAL PROVIDENT | EXCLUDE | Pension contribution |
| CUSTOMS, FIJI CUSTOMS | EXCLUDE | Duty (import VAT separate) |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| EFL, ENERGY FIJI | Domestic 9% | Electricity |
| WAF, WATER AUTHORITY FIJI | Domestic 9% | Water (commercial) |
| VODAFONE FIJI, DIGICEL FIJI | Domestic 9% | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SUN INSURANCE, FMF, QBE FIJI | EXCLUDE | Exempt |

### 3.5 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 9% | Non-resident digital service |
| ZOOM, SLACK, CANVA, FIGMA | Self-assess 9% | Same |

### 3.6 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES | EXCLUDE | Outside VAT scope |
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| DIVIDEND, CASH WITHDRAWAL | EXCLUDE / TIER 2 | Out of scope |

---

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 9%

**Input line:** `05.04.2026 ; PACIFIC TRADING LTD ; CREDIT ; Invoice FJ-041 ; FJD 1,090`

**Reasoning:** Domestic sale. 9%. Net = FJD 1,000, VAT = FJD 90.

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | PACIFIC TRADING LTD | +1,090 | +1,000 | 90 | 9% | Output | N | — |

### Example 2 — Export, zero-rated

**Input line:** `15.04.2026 ; NZ IMPORTS LTD ; CREDIT ; Exported produce ; FJD 5,000`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | NZ IMPORTS LTD | +5,000 | +5,000 | 0 | 0% | Zero-rated | N | — |

### Example 3 — Non-resident digital service

**Input line:** `18.04.2026 ; MICROSOFT ; DEBIT ; Azure April ; FJD -218`

**Reasoning:** Non-resident. Self-assess 9%. Net = FJD 200, VAT = FJD 18.

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | MICROSOFT | -218 | -200 | 18 | 9% | Output + Input | N | — |

### Example 4 — Bank charges, excluded

**Input line:** `30.04.2026 ; BSP ; DEBIT ; Account fee ; FJD -25`

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | BSP | -25 | — | — | — | — | N | "Exempt" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 9% — Default for all taxable supplies.
### 5.2 Zero rate — Exports, basic foodstuffs (specified list), prescription medicines, educational materials.
### 5.3 Exempt — Financial services, residential rent, medical services, public transport.
### 5.4 Input tax credit — Valid tax invoice required. Business purpose. Apportionment if mixed.
### 5.5 Blocked input — Personal consumption, entertainment, passenger vehicles (unless taxi/rental).
### 5.6 Imports — VAT at 9% on CIF plus duty. Paid at customs.
### 5.7 Reverse charge — Non-resident services: self-assess 9%.
### 5.8 Credit notes — Reduce output/input in period issued.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — Default: 0%. Question: "Commercial vehicle exclusively for business?"
### 6.2 Entertainment — Default: block. Question: "Business purpose documented?"
### 6.3 SaaS entities — Default: self-assess 9%. Question: "Check invoice entity."
### 6.4 Tourism mixed supplies — Default: flag for STT/ECAL. Question: "Hotel/resort operator?"
### 6.5 Cash withdrawals — Default: exclude. Question: "Purpose?"

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Fiji fields: Output 9%, Zero-rated, Exempt, Input domestic, Input imports, Net VAT.

---

## Section 8 — Bank statement reading guide

BSP and HFC exports CSV with DD/MM/YYYY. FJD primary currency. Internal transfers between BSP/HFC/ANZ: exclude. Convert foreign currency at Reserve Bank of Fiji rate.

---

## Section 9 — Onboarding fallback

### 9.1 TIN — "What is your FRCS TIN?"
### 9.2 Filing period — Monthly or quarterly based on turnover.
### 9.3 Industry — "What does the business do?"
### 9.4 Exports — "Do you export?"
### 9.5 Credit brought forward — Always ask.

---

## Section 10 — Reference material

### Sources
1. Fiji VAT Act 1991 (as amended). 2. FRCS guidelines. 3. FRCS TPOS portal.

### Known gaps
1. Tourism sector (STT/ECAL) refused. 2. Supplier library covers major banks/utilities only.

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
