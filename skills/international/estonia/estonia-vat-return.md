---
name: estonia-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Estonian VAT return (KMD form) for any client. Trigger on phrases like "prepare VAT return", "do the KMD", "fill in KMD", "Estonian VAT", "kaibemaks", or any request involving Estonia VAT filing. This skill covers Estonia only and standard KM registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Estonian VAT work.
version: 2.0
---

# Estonia VAT Return Skill (KMD) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1.**

| Field | Value |
|---|---|
| Country | Estonia (Eesti) |
| Standard rate | 22% |
| Reduced rates | 13% (accommodation), 9% (books, pharmaceuticals, periodicals, medical devices) |
| Zero rate | 0% (exports, intra-EU B2B supplies, international transport) |
| Return form | KMD (Kaibemaksudeklaratsioon) |
| Filing portal | https://maasikas.emta.ee (e-MTA) |
| Authority | Maksu- ja Tolliamet (MTA — Estonian Tax and Customs Board) |
| Currency | EUR only |
| Filing frequencies | Monthly only |
| Deadline | 20th of month following period |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key KMD lines:**

| Line | Meaning |
|---|---|
| 1 | Taxable supplies at 22% — base |
| 1.1 | Taxable supplies at 13% — base |
| 1.2 | Taxable supplies at 9% — base |
| 2 | Total output KM (calculated) |
| 3 | Intra-EU supply of goods and services (0%) |
| 3.1 | Intra-EU supply of goods (subset) |
| 3.1.1 | Intra-EU supply of goods after processing |
| 3.2 | Intra-EU supply of services (subset) |
| 4 | Exports and 0% supplies |
| 5 | Tax-exempt supply (total) |
| 5.1 | Exempt with right of deduction |
| 5.2 | Exempt without right of deduction |
| 6 | Intra-EU acquisition of goods and services — base (reverse charge) |
| 6.1 | Intra-EU acquisition of goods (subset) |
| 7 | Acquisition of other goods/services subject to KM (non-EU reverse charge) |
| 8 | Margin scheme supplies |
| 5.3 | Input KM on passenger car (50% restriction) |
| 5.4 | Input KM on passenger car (100% — documented) |
| 9 | Total deductible input KM |
| 9.1 | Input KM domestic |
| 9.2 | Input KM intra-EU |
| 9.3 | Input KM imports |
| 9.4 | Input KM non-EU reverse charge |
| 10 | KM payable (Line 2 minus Line 9, if positive) |
| 11 | KM refundable (if Line 9 > Line 2) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 22% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Estonia |
| Unknown B2B vs B2C for EU customer | B2C, charge 22% |
| Unknown business-use proportion (vehicle) | 50% recovery (statutory default for cars) |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status | Blocked |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 3,000 |
| HIGH tax-delta on single default | EUR 200 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net KM position | EUR 5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: SEB Estonia, Swedbank Estonia, LHV Pank, Luminor, Coop Pank, Revolut Business, Wise Business.

**Recommended** — sales/purchase invoices, KMKR number (EE + 9 digits), prior KMD.

**Ideal** — complete register, KMD INF annex data (transaction-level reporting for large invoices), prior period reconciliation.

### Estonia-specific refusal catalogue

**R-EE-1 — Non-registered below threshold.** *Trigger:* turnover < EUR 40,000, not registered. *Message:* "Non-registered entities do not file KMD returns."

**R-EE-2 — Partial exemption.** *Trigger:* mixed taxable/exempt. *Message:* "Partial exemption under KMS Section 32 requires reviewer."

**R-EE-3 — E-resident special cases.** *Trigger:* e-resident company with no Estonian substance. *Message:* "E-resident companies without Estonian fixed establishment may have place-of-supply issues. Specialist review required."

**R-EE-4 — Special schemes.** *Message:* "Margin/travel agent schemes out of scope."

---

## Section 3 — Supplier pattern library

### 3.1 Estonian banks (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SEB, SEB PANK | EXCLUDE | Financial service, exempt |
| SWEDBANK, SWEDBANK AS | EXCLUDE | Same |
| LHV, LHV PANK | EXCLUDE | Same |
| LUMINOR | EXCLUDE | Same |
| COOP PANK | EXCLUDE | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscriptions |
| INTRESS, INTEREST | EXCLUDE | Interest |
| LAEN, LOAN | EXCLUDE | Loan principal |

### 3.2 Estonian government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MAKSU- JA TOLLIAMET, MTA, EMTA | EXCLUDE | Tax payment |
| SOTSIAALMAKS, SOCIAL TAX | EXCLUDE | Social tax |
| ARIREGISTER, BUSINESS REGISTER | EXCLUDE | Registration fee |
| PATENDIAMET | EXCLUDE | Patent office |

### 3.3 Estonian utilities

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| EESTI ENERGIA, ENEFIT | Domestic 22% | 9.1 | Electricity |
| ALEXELA | Domestic 22% | 9.1 | Gas/electricity |
| TALLINNA VESI | Domestic 22% | 9.1 | Water |
| TELIA EESTI | Domestic 22% | 9.1 | Telecoms |
| ELISA EESTI | Domestic 22% | 9.1 | Telecoms |
| TELE2 EESTI | Domestic 22% | 9.1 | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| IF KINDLUSTUS | EXCLUDE | Exempt |
| ERGO KINDLUSTUS | EXCLUDE | Same |
| SALVA KINDLUSTUS | EXCLUDE | Same |
| KINDLUSTUS, INSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Notes |
|---|---|---|
| OMNIVA, EESTI POST | EXCLUDE for standard post; 22% for parcel | Universal exempt; parcel taxable |
| DPD EESTI | Domestic 22% | Courier |
| ITELLA, SMARTPOST | Domestic 22% | Parcel terminal |
| DHL INTERNATIONAL | EU reverse charge | Check entity |

### 3.6 SaaS — EU suppliers (reverse charge, Line 6 + 9.2)

| Pattern | Billing entity | Notes |
|---|---|---|
| GOOGLE | Google Ireland Ltd (IE) | EU reverse charge |
| MICROSOFT | Microsoft Ireland (IE) | Reverse charge |
| ADOBE | Adobe Ireland (IE) | Reverse charge |
| META, FACEBOOK | Meta Ireland (IE) | Reverse charge |
| SPOTIFY | Spotify AB (SE) | EU reverse charge |
| DROPBOX | Dropbox Ireland (IE) | Reverse charge |
| SLACK | Slack Ireland (IE) | Reverse charge |
| ATLASSIAN | Atlassian BV (NL) | EU reverse charge |
| ZOOM | Zoom Ireland (IE) | Reverse charge |

### 3.7 SaaS — non-EU suppliers (reverse charge, Line 7 + 9.4)

| Pattern | Billing entity | Notes |
|---|---|---|
| AWS EMEA SARL | LU entity | EU reverse charge (Line 6) |
| NOTION | Notion Labs Inc (US) | Non-EU RC |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Non-EU RC |
| OPENAI, CHATGPT | OpenAI Inc (US) | Non-EU RC |
| GITHUB | GitHub Inc (US) | Check if IE |
| FIGMA | Figma Inc (US) | Non-EU RC |
| CANVA | Canva Pty Ltd (AU) | Non-EU RC |

### 3.8 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

### 3.9 Professional services

| Pattern | Treatment | Notes |
|---|---|---|
| NOTAR, NOTARY | Domestic 22% | Legal |
| RAAMATUPIDAJA, ACCOUNTANT | Domestic 22% | Accounting |
| ADVOKAAT, LAWYER | Domestic 22% | Legal |

### 3.10 Payroll (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SOTSIAALMAKS | EXCLUDE | Social tax |
| PALK, SALARY | EXCLUDE | Wages |
| TULUMAKS | EXCLUDE | Income tax |

### 3.11 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SISEUULEKANNE, OWN TRANSFER | EXCLUDE | Internal |
| DIVIDEND | EXCLUDE | Out of scope |
| LAENU TAGASIMAKSE, LOAN REPAYMENT | EXCLUDE | Loan principal |
| ATM, SULARAHA | Ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-EU SaaS reverse charge (Notion)
**Input:** `03.04.2026 ; NOTION LABS INC ; -14.68 EUR`
**Treatment:** Non-EU RC. Output KM self-assessed at 22%. Line 7 (base). Input in Line 9.4.

| Date | Counterparty | Net | KM | Rate | Line (input) | Line (output) | Default? |
|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | 3.23 | 22% | 9.4 | 7 | N |

### Example 2 — EU service reverse charge (Google Ads)
**Input:** `10.04.2026 ; GOOGLE IRELAND LIMITED ; -850.00 EUR`
**Treatment:** EU RC. Line 6 (base). Output KM at 22%. Input in Line 9.2.

### Example 3 — Entertainment
**Input:** `15.04.2026 ; RESTORAN TCHAIKOVSKY ; -220.00 EUR`
**Treatment:** Entertainment input KM not specifically blocked in Estonia (unlike Malta). Deductible if business purpose. Default: block (purpose unknown).

### Example 4 — Passenger vehicle (50% statutory restriction)
**Input:** `28.04.2026 ; CIRCLE K EESTI ; Fuel ; -60.00 EUR`
**Treatment:** Passenger car fuel. Estonia has statutory 50% input KM restriction on passenger vehicles (KMS Section 30(4)) unless 100% business use documented and MTA notified. Default: 50% recovery in Line 5.3.

| Date | Counterparty | Net | KM | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|
| 28.04.2026 | CIRCLE K EESTI | -50.85 | -5.59 | 22% (50%) | 5.3 | Y | "100% business use documented?" |

### Example 5 — EU B2B service sale
**Input:** `22.04.2026 ; STUDIO KREBS GMBH ; +3,500.00 EUR`
**Treatment:** B2B to DE. Line 3.2. 0%. Verify USt-IdNr.

### Example 6 — Capital goods
**Input:** `18.04.2026 ; EURONICS EESTI ; Laptop ; -1,595.00 EUR`
**Treatment:** Business equipment. Input KM at 22% in Line 9.1. No specific capital goods monetary threshold in Estonian KMD — track for adjustment period.

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard 22% (KMS Section 15(1))
Default. Sales: Line 1. Input: Line 9.1.

### 5.2 Reduced 13% (KMS Section 15(2))
Accommodation.

### 5.3 Reduced 9% (KMS Section 15(2))
Books, pharmaceuticals, periodicals, medical devices.

### 5.4 Zero rate / exports
Exports: Line 4. Intra-EU goods: Line 3.1. Intra-EU services: Line 3.2.

### 5.5 Exempt without credit (KMS Section 16)
Financial, insurance, healthcare, education, postal, gambling, residential rental.

### 5.6 Reverse charge — EU (KMS Section 3(4))
Base: Line 6. Input: Line 9.2.

### 5.7 Reverse charge — non-EU (KMS Section 3(5))
Base: Line 7. Input: Line 9.4.

### 5.8 Passenger vehicle 50% restriction (KMS Section 30(4))
All passenger vehicles: 50% input KM in Line 5.3. Exception: 100% in Line 5.4 if documented and MTA notified.

### 5.9 Blocked input
- Personal use: blocked
- Entertainment: not specifically blocked by statute (deductible if business purpose)
- Passenger vehicles: 50% default

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs — *Default:* 50%. *Question:* "100% documented?"
### 6.2 Entertainment — *Default:* block. *Question:* "Business purpose?"
### 6.3 SaaS entity — *Default:* non-EU RC. *Question:* "Check invoice."
### 6.4 Owner transfers — *Default:* exclude.
### 6.5 Individual incoming — *Default:* 22% domestic.
### 6.6 Foreign incoming — *Default:* 22%.
### 6.7 Large purchases — *Default:* deductible; flag capital.
### 6.8 E-resident company — *Default:* flag for reviewer.
### 6.9 Cash withdrawals — *Default:* exclude.

---

## Section 7 — Excel working paper template

Per `vat-workflow-base` Section 3. Column H accepts Estonian KMD line codes. Bottom-line: Line 10 (payable) or Line 11 (refundable).

---

## Section 8 — Estonia bank statement reading guide

**CSV conventions.** SEB and Swedbank use semicolons, DD.MM.YYYY. LHV exports CSV in EUR.

**Estonian language.** uuur (rent), palk (salary), intress (interest), ulekanne (transfer).

**IBAN prefix.** EE = Estonia.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type — *Inference:* OU = company; FIE = sole trader.
### 9.2 KM registration — *Fallback:* "KMKR holder?"
### 9.3 KMKR number — *Fallback:* "EE + 9 digits?"
### 9.4 Filing period — Monthly only.
### 9.5 E-resident status — *Fallback:* "Are you an e-resident company?"
### 9.6 Exempt supplies — *Fallback:* "Any exempt supplies?"
### 9.7 Vehicle ownership — *Fallback:* "Own/lease passenger vehicle? MTA notification filed?"

---

## Section 10 — Reference material

### Sources
1. Kaibemaksuseadus (KMS — VAT Act)
2. KMS Section 30(4) (vehicle restriction)
3. EU VAT Directive 2006/112/EC — via companion skill
4. VIES — https://ec.europa.eu/taxation_customs/vies/

### Change log
- **v2.0 (April 2026):** Full rewrite. Estonian banks (SEB EE, Swedbank EE, LHV).
- **v1.0 (April 2026):** Initial skill.

## End of Estonia VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
