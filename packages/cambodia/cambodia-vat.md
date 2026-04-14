---
name: cambodia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Cambodia VAT return for any client. Trigger on phrases like "Cambodia VAT", "GDT filing", "tax on value added", or any request involving Cambodia VAT. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Cambodia VAT work.
version: 2.0
---

# Cambodia VAT Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Cambodia (Kingdom of Cambodia) |
| Standard rate | 10% |
| Zero rate | 0% (exports, international transport) |
| Exempt | Financial services, public postal, medical, education, electricity/water (residential) |
| Return form | Monthly VAT return (Form submitted via E-Filing) |
| Filing portal | https://www.tax.gov.kh (GDT E-Filing) |
| Authority | General Department of Taxation (GDT), Ministry of Economy and Finance |
| Currency | KHR (Cambodian Riel); USD widely used |
| Filing frequency | Monthly |
| Deadline | 20th of the month following the tax period |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending local practitioner validation |

**Key return fields:**

| Field | Meaning |
|---|---|
| Output tax | VAT on domestic sales at 10% |
| Zero-rated output | Exports and qualifying supplies at 0% |
| Exempt output | Exempt supplies (reported but no VAT) |
| Input tax — domestic | VAT on local purchases with proper tax invoice |
| Input tax — imports | VAT paid at customs |
| Net VAT | Output tax minus total input tax |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 10% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty location | Domestic Cambodia |
| Unknown business-use proportion | 0% recovery |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | USD 5,000 |
| HIGH tax-delta on a single default | USD 500 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: ABA Bank, ACLEDA Bank, Canadia Bank, Prince Bank, Wing Bank, or any other.

**Recommended** — sales invoices, purchase invoices with supplier TIN, client's TIN.

**Ideal** — complete purchase/sales registers, prior period return, credit brought forward reconciliation.

### Cambodia-specific refusal catalogue

**R-KH-1 — Qualified Investment Project (QIP) entity.** Trigger: client holds a QIP certificate from Council for the Development of Cambodia. Message: "QIP entities have special VAT exemptions and incentive periods. Please escalate to a qualified Cambodian tax practitioner."

**R-KH-2 — Special Economic Zone (SEZ) enterprise.** Trigger: client operates in an SEZ. Message: "SEZ enterprises have special import/export VAT treatment. Out of scope."

**R-KH-3 — Non-resident tax obligations.** Trigger: non-resident entity with Cambodian obligations. Message: "Non-resident tax obligations require specialist analysis. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Cambodian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ABA BANK, ABA | EXCLUDE for bank charges/fees | Financial service, exempt |
| ACLEDA, ACLEDA BANK | EXCLUDE for bank charges/fees | Same |
| CANADIA BANK, PRINCE BANK | EXCLUDE for bank charges/fees | Same |
| WING, WING BANK | EXCLUDE for transfer fees | Mobile money, exempt |
| ANZ ROYAL, J TRUST ROYAL | EXCLUDE for bank charges | Same |
| INTEREST, INCOME INTEREST | EXCLUDE | Out of scope |
| LOAN, REPAYMENT | EXCLUDE | Loan principal, out of scope |

### 3.2 Government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| GDT, GENERAL DEPARTMENT OF TAXATION | EXCLUDE | Tax payment |
| CUSTOMS, GDCE | EXCLUDE | Customs duty (import VAT separate) |
| MOC, MINISTRY OF COMMERCE | EXCLUDE | Registration/licence fees |
| NSSF, SOCIAL SECURITY | EXCLUDE | Social security contribution |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| EDC, ELECTRICITE DU CAMBODGE | Domestic 10% | Electricity (commercial) |
| PHNOM PENH WATER SUPPLY | Domestic 10% | Water (commercial use) |
| SMART, CELLCARD, METFONE | Domestic 10% | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| FORTE INSURANCE, CAMBODIA RE | EXCLUDE | Insurance, exempt |
| INFINITY GENERAL, ASIA INSURANCE | EXCLUDE | Same |

### 3.5 Digital payments

| Pattern | Treatment | Notes |
|---|---|---|
| WING TRANSFER FEE | EXCLUDE | Financial service fee, exempt |
| PI PAY, TRUE MONEY, BAKONG | EXCLUDE for fees | Same |

### 3.6 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, FACEBOOK | Self-assess 10% (reverse charge) | Non-resident digital service |
| AWS, AMAZON, ZOOM, SLACK | Self-assess 10% | Same |
| CANVA, FIGMA, NOTION, OPENAI | Self-assess 10% | Same |

### 3.7 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| LAW FIRM, LEGAL, ADVOCATE | Domestic 10% | Deductible if business purpose |
| AUDIT, ACCOUNTING, CONSULTANT | Domestic 10% | Professional overhead |

### 3.8 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| RENT, OFFICE RENT | Domestic 10% | Commercial lease with VAT invoice |
| RESIDENTIAL RENT | EXCLUDE | Residential, exempt |

### 3.9 Payroll (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES, BONUS | EXCLUDE | Outside VAT scope |
| NSSF CONTRIBUTION | EXCLUDE | Social security |

### 3.10 Internal transfers

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Out of scope |
| CASH WITHDRAWAL, ATM | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Standard domestic sale at 10%

**Input line:**
`05.04.2026 ; XYZ TRADING CO ; CREDIT ; Invoice KH-2026-041 ; USD 1,100`

**Reasoning:** Domestic sale. Standard 10%. Net = USD 1,000, VAT = USD 100. Output tax.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | XYZ TRADING CO | +1,100 | +1,000 | 100 | 10% | Output tax | N | — |

### Example 2 — Local purchase with input credit

**Input line:**
`10.04.2026 ; ACLEDA SUPPLIES ; DEBIT ; Office equipment ; USD -550`

**Reasoning:** Local purchase with valid tax invoice. Net = USD 500, VAT = USD 50.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | ACLEDA SUPPLIES | -550 | -500 | 50 | 10% | Input — domestic | N | — |

### Example 3 — Export, zero-rated

**Input line:**
`15.04.2026 ; THAI IMPORTS CO ; CREDIT ; Exported garments ; USD 8,000`

**Reasoning:** Export. Zero-rated. Full input recovery on related purchases.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | THAI IMPORTS CO | +8,000 | +8,000 | 0 | 0% | Zero-rated output | N | — |

### Example 4 — Non-resident digital service

**Input line:**
`18.04.2026 ; GOOGLE CLOUD ; DEBIT ; Cloud services April ; USD -200`

**Reasoning:** Non-resident service. Self-assess 10%. Output VAT = USD 20. Input credit = USD 20 if fully taxable. Net zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | GOOGLE CLOUD | -200 | -200 | 20 | 10% | Output + Input | N | — |

### Example 5 — Bank charges, excluded

**Input line:**
`30.04.2026 ; ABA BANK ; DEBIT ; Monthly service fee ; USD -15`

**Reasoning:** Bank fee. Exempt financial service. Exclude.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | ABA BANK | -15 | — | — | — | — | N | "Exempt" |

### Example 6 — Salary payment, excluded

**Input line:**
`25.04.2026 ; EMPLOYEE SOPHEAK ; DEBIT ; April salary ; USD -800`

**Reasoning:** Wages. Outside VAT scope. Exclude.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 25.04.2026 | EMPLOYEE SOPHEAK | -800 | — | — | — | — | N | "Wages — out of scope" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 10% (Law on Taxation)
Default rate for all taxable supplies. Sales = output tax. Purchases with valid tax invoice = input tax.

### 5.2 Zero rate
Exports with customs documentation. International transport services. Input VAT on related purchases fully recoverable.

### 5.3 Exempt supplies
Financial services (banking, insurance), public postal services, medical/dental, educational, residential electricity/water, public transport. No output VAT, no input recovery on related costs.

### 5.4 Input tax credit — eligibility
Purchase must relate to taxable supplies. Valid tax invoice with supplier TIN required. Input tax on purchases related to exempt supplies is not recoverable.

### 5.5 Input tax credit — apportionment
If mixed taxable and exempt supplies: apportion based on ratio. Annual adjustment required. Flag for reviewer.

### 5.6 Blocked input VAT
Personal consumption, entertainment, passenger vehicles (unless transport business). Check blocked FIRST.

### 5.7 Imports
VAT at 10% on CIF value plus customs duty. Paid at customs. Input credit claimable if for taxable supplies.

### 5.8 Reverse charge on imported services
Non-resident service provider: self-assess 10%. Input credit claimable if for taxable supplies.

### 5.9 Credit notes
Reduce output/input VAT in the period issued. Must reference original invoice.

### 5.10 Time of supply
VAT due at the earlier of: invoice, payment, or delivery.

### 5.11 Withholding tax interaction
Cambodia has withholding tax on certain payments (separate from VAT). Do not confuse WHT with VAT. WHT is excluded from VAT return.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle and fuel costs
Default: 0% recovery. Question: "Is this a commercial vehicle used exclusively for business?"

### 6.2 Entertainment
Default: block. Question: "Was this a documented business entertainment expense?"

### 6.3 SaaS billing entities
Default: self-assess 10%. Question: "Check invoice for legal entity and country."

### 6.4 Round-number incoming transfers
Default: exclude as owner injection. Question: "Customer payment, capital injection, or loan?"

### 6.5 USD vs KHR transactions
Default: USD amounts as-is; KHR converted at NBC official rate. Question: "Confirm currency for dual-currency transactions."

### 6.6 Cash withdrawals
Default: exclude. Question: "What was the cash used for?"

### 6.7 Rent payments
Default: no input credit without VAT invoice. Question: "Does landlord charge VAT on rent?"

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3, with Cambodia-specific return fields: Output tax, Zero-rated output, Exempt output, Input tax domestic, Input tax imports, Net VAT.

---

## Section 8 — Bank statement reading guide

**Currency.** Cambodia uses dual currency (KHR and USD). Most business transactions in USD. Convert KHR at National Bank of Cambodia (NBC) official rate.

**ABA Bank exports** typically CSV with Date, Description, Debit, Credit, Balance in USD. ACLEDA exports similar format.

**Internal transfers.** Own-account transfers between ABA, ACLEDA, Wing. Always exclude.

**Mobile money.** Wing, Pi Pay, True Money transfers. Classify based on underlying transaction, not payment method.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type
Inference: "Ltd", "Co., Ltd" = company. Fallback: "Sole proprietor, partnership, or company?"

### 9.2 TIN
Fallback: "What is your GDT Tax Identification Number?"

### 9.3 Filing period
Inference: transaction date range. Monthly. Fallback: "Which month?"

### 9.4 Industry
Inference: counterparty mix. Fallback: "What does the business do?"

### 9.5 Exports
Inference: foreign currency incoming. Fallback: "Do you export goods or services?"

### 9.6 Credit brought forward
Always ask: "Excess credit from prior period?"

---

## Section 10 — Reference material

### Sources
1. Law on Taxation (as amended, 2023)
2. Prakas on VAT — GDT ministerial orders
3. GDT E-Filing Portal — https://www.tax.gov.kh

### Known gaps
1. QIP and SEZ treatment refused. 2. Supplier library covers major banks/utilities only. 3. Withholding tax interaction not fully mapped.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.
- v1.1: Previous monolithic version.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
