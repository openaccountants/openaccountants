---
name: brunei-tax
description: Use this skill whenever asked about Brunei Darussalam tax obligations. Trigger on phrases like "Brunei tax", "Brunei VAT", "Brunei GST", "corporate tax Brunei", "MOFE filing". Brunei has NO VAT/GST and NO personal income tax. This skill covers corporate income tax at 18.5% and clarifies the absence of consumption tax. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Brunei tax work.
version: 2.0
---

# Brunei Darussalam Tax Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Brunei Darussalam |
| VAT/GST | NONE — Brunei does NOT have a VAT, GST, or any consumption tax |
| Personal income tax | NONE |
| Corporate income tax | 18.5% on chargeable income |
| Return form | Corporate income tax return (annual) |
| Filing portal | MOFE Revenue Division |
| Authority | Revenue Division, Ministry of Finance and Economy (MOFE) |
| Currency | BND (Brunei Dollar, pegged 1:1 to SGD) |
| Filing frequency | Annual (corporate tax only) |
| Deadline | Within 6 months of financial year-end |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**CRITICAL: Brunei has NO consumption tax.** There is no VAT return to prepare. This skill exists to prevent misclassification and to provide the corporate tax framework.

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown tax obligation | No consumption tax; corporate tax only if company |
| Unknown withholding tax | Check if payment to non-resident triggers WHT |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — financial statements for the year. Bank statements from: BIBD (Bank Islam Brunei Darussalam), Baiduri Bank, Standard Chartered Brunei, HSBC Brunei.

### Brunei-specific refusal catalogue

**R-BN-1 — Petroleum sector.** Trigger: client in oil/gas under Petroleum Income Tax Act. Message: "Petroleum companies are taxed under a separate regime (55% + 20% on profits). Please escalate."

**R-BN-2 — VAT/GST return request.** Trigger: user asks for VAT/GST return preparation. Message: "Brunei does NOT have a VAT/GST or any consumption tax. No consumption tax return exists. If you need corporate income tax assistance, this skill can help."

---

## Section 3 — Supplier pattern library

### 3.1 Brunei banks

| Pattern | Treatment | Notes |
|---|---|---|
| BIBD, BANK ISLAM BRUNEI | Bank charges are a deductible expense | No VAT component |
| BAIDURI, BAIDURI BANK | Same | Same |
| STANDARD CHARTERED BN, HSBC BN | Same | Same |
| INTEREST | Interest expense — deductible if for business | No VAT |

### 3.2 Government (exclude from expense claims where non-deductible)

| Pattern | Treatment | Notes |
|---|---|---|
| MOFE, REVENUE DIVISION | Tax payment — not deductible | Corporate tax |
| TAP, EMPLOYEE TRUST FUND | Pension — deductible | Tabung Amanah Pekerja |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| DES, DEPT OF ELECTRICAL SERVICES | Deductible expense | No consumption tax |
| DST, PROGRESIF, IMAGINE | Deductible expense | Telecoms |

### 3.4 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Deductible expense; check WHT on non-resident services | No consumption tax; WHT may apply |
| ZOOM, SLACK, CANVA | Same | Same |

### 3.5 Payroll

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES | Deductible expense | No income tax on employees |
| TAP CONTRIBUTION | Deductible | Mandatory employee savings |

---

## Section 4 — Worked examples

### Example 1 — No consumption tax applies

**Input line:** `05.04.2026 ; LOCAL CLIENT ; CREDIT ; Consulting fee ; BND 10,000`

**Reasoning:** Brunei has no VAT/GST. This is revenue for corporate tax purposes. No consumption tax to charge or report.

| Date | Counterparty | Gross | Net | Tax | Rate | Return field | Notes |
|---|---|---|---|---|---|---|---|
| 05.04.2026 | LOCAL CLIENT | +10,000 | +10,000 | 0 | N/A | Revenue | No consumption tax |

### Example 2 — Purchase from overseas vendor

**Input line:** `18.04.2026 ; AWS ; DEBIT ; Cloud hosting ; BND -500`

**Reasoning:** No VAT/GST to self-assess. Check if withholding tax applies on payment to non-resident (typically 10% on management/technical fees, 15% on royalties).

| Date | Counterparty | Gross | Net | Tax | Rate | Return field | Notes |
|---|---|---|---|---|---|---|---|
| 18.04.2026 | AWS | -500 | -500 | 0 | N/A | Expense | Check WHT |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 No consumption tax — Brunei has no VAT, GST, sales tax, or service tax.
### 5.2 Corporate income tax — 18.5% on chargeable income for companies.
### 5.3 No personal income tax — Individuals not taxed on income.
### 5.4 Withholding tax — 10% on management/technical fees to non-residents; 15% on royalties; other rates per treaty.
### 5.5 Stamp duty — Applies to certain documents (property transfers, share transfers).
### 5.6 Customs duty — Applies on imports (separate from any consumption tax, which does not exist).

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 WHT on non-resident payments — Default: flag. Question: "Is this a management/technical fee or royalty to a non-resident?"
### 6.2 Petroleum operations — Default: refuse (R-BN-1).
### 6.3 Tax treaty benefits — Default: flag. Question: "Does Brunei have a DTA with the recipient's country?"

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, adapted for corporate tax: Revenue, Deductible expenses, Non-deductible expenses, Chargeable income, Tax at 18.5%.

---

## Section 8 — Bank statement reading guide

BIBD and Baiduri exports CSV/PDF. BND primary (pegged to SGD). Malay language descriptions common. Internal transfers: exclude. No VAT extraction needed — all amounts are gross.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — "Company, sole proprietor, or partnership?" (Only companies pay corporate tax.)
### 9.2 Financial year — "What is your financial year-end?"
### 9.3 Petroleum sector — "Are you in oil and gas?" (If yes, R-BN-1 fires.)
### 9.4 Non-resident payments — "Do you pay management fees or royalties to non-residents?"

---

## Section 10 — Reference material

### Sources
1. Income Tax Act (Chapter 35). 2. Companies Income Tax Act (Chapter 97). 3. Petroleum Income Tax Act. 4. MOFE Revenue Division guidelines.

### Known gaps
1. Petroleum sector refused. 2. No consumption tax means most of the vat-workflow-base structure is inapplicable.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure. Emphasis on absence of VAT/GST.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
