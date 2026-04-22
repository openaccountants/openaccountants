---
name: cyprus-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a Cyprus VAT return (VAT4 form) for any client. Trigger on phrases like "prepare Cyprus VAT return", "do the Cyprus VAT", "fill in VAT4", "create the return", "Cyprus VAT filing", or any request involving Cyprus VAT filing. This skill covers Cyprus only and standard VAT registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Cyprus VAT work.
version: 2.0
---

# Cyprus VAT Return Skill (VAT4 Form) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1.**

| Field | Value |
|---|---|
| Country | Cyprus (Republic of Cyprus) |
| Standard rate | 19% |
| Reduced rates | 9% (accommodation, restaurant/catering), 5% (food, pharmaceuticals, books, newspapers, water), 3% (specific social housing) |
| Zero rate | 0% (exports, intra-EU B2B supplies of goods, international transport) |
| Return form | VAT4 |
| Filing portal | https://taxisnet.mof.gov.cy (TAXISnet / TFA portal) |
| Authority | Cyprus Tax Department, Ministry of Finance |
| Currency | EUR only |
| Filing frequencies | Quarterly (standard); Monthly (option for large exporters) |
| Deadline | 10th of second month after quarter end (e.g. 10 May for Q1) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Companion skill (Tier 2, EU directive) | **eu-vat-directive v0.1 or later — MUST be loaded** |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key VAT4 boxes:**

| Box | Meaning |
|---|---|
| 1 | VAT due on sales and other outputs (all rates combined) |
| 2 | VAT due on acquisitions from EU + services from abroad (reverse charge output) |
| 3 | Total output VAT (Box 1 + Box 2) |
| 4 | VAT reclaimed on purchases and inputs (all deductible input VAT) |
| 5 | Net VAT payable or refundable (Box 3 minus Box 4) |
| 6 | Total value of sales and outputs (excl. VAT) |
| 7 | Total value of purchases and inputs (excl. VAT) |
| 8A | Value of intra-EU supplies of goods |
| 8B | Value of B2B services supplied to other EU states |
| 9 | Value of zero-rated outputs (exports, other zero-rated not in 8A/8B) |
| 10 | Sales outside CY VAT scope with right of deduction |
| 11A | Value of goods acquired from EU |
| 11B | Value of services received from EU (reverse charge) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 19% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic Cyprus |
| Unknown B2B vs B2C for EU customer | B2C, charge 19% |
| Unknown business-use proportion | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from non-EU |
| Unknown blocked-input status | Blocked |
| Unknown whether in scope | In scope |

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | EUR 3,000 |
| HIGH tax-delta on single default | EUR 200 |
| MEDIUM counterparty concentration | >40% |
| MEDIUM conservative-default count | >4 |
| LOW absolute net VAT position | EUR 5,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the quarter. Acceptable from: Bank of Cyprus, Hellenic Bank, RCB Bank, Eurobank Cyprus, Astrobank, Revolut Business, Wise Business.

**Recommended** — sales invoices (intra-EU B2B, exports), purchase invoices for input VAT claims above EUR 200, CY VAT number (CY + 8 digits + letter).

**Ideal** — complete invoice register, prior VAT4, VIES listings, credit brought forward reconciliation.

### Cyprus-specific refusal catalogue

**R-CY-1 — Non-registered entity.** *Trigger:* not registered, turnover below EUR 15,600. *Message:* "Non-registered entities do not file VAT4 returns."

**R-CY-2 — Partial exemption.** *Trigger:* mixed taxable/exempt supplies. *Message:* "Mixed supplies require pro-rata input VAT apportionment under Section 26. Use a licensed accountant."

**R-CY-3 — Domestic reverse charge (construction Section 11B).** *Trigger:* construction services received/supplied. *Message:* "Construction domestic reverse charge requires specialist classification."

**R-CY-4 — Ship management / international services.** *Trigger:* shipping or maritime services. *Message:* "Ship management and tonnage tax structures require specialist advice."

**R-CY-5 — Special schemes (TOMS, margin).** *Message:* "Tour operator margin scheme and second-hand goods margin scheme require specialist computation."

**R-CY-6 — Immovable property classification.** *Trigger:* property transactions with option to tax. *Message:* "Immovable property VAT classification under the Eighth Schedule requires specialist review."

---

## Section 3 — Supplier pattern library

Match by case-insensitive substring. Most specific match wins.

### 3.1 Cypriot banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BANK OF CYPRUS, BOC | EXCLUDE for bank charges/fees | Exempt financial service |
| HELLENIC BANK | EXCLUDE for bank charges/fees | Same |
| RCB BANK | EXCLUDE for bank charges/fees | Same |
| EUROBANK CYPRUS | EXCLUDE for bank charges/fees | Same |
| ASTROBANK | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE | Check for taxable subscription invoices |
| TOKOI, INTEREST | EXCLUDE | Interest, out of scope |
| DANEIO, LOAN | EXCLUDE | Loan principal, out of scope |

### 3.2 Cypriot government and statutory bodies (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| TAX DEPARTMENT, TMHMA FOROLOGIAS | EXCLUDE | Tax payment |
| SOCIAL INSURANCE, KOINONIKON ASFALISION | EXCLUDE | Social security |
| REGISTRAR OF COMPANIES | EXCLUDE | Registration fees |
| CYPRUS STOCK EXCHANGE | EXCLUDE | Regulatory fee |

### 3.3 Cypriot utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| EAC, ELECTRICITY AUTHORITY CYPRUS | Domestic 19% | 4 (input) | Electricity |
| WATER BOARD, SYMVOULIO YDATOPROMITHEIAS | Domestic 5% | 4 (input) | Water at 5% |
| CYTA, CYTANET | Domestic 19% | 4 (input) | Telecoms |
| EPIC, PRIMETEL | Domestic 19% | 4 (input) | Telecoms |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| GENERAL INSURANCE CYPRUS | EXCLUDE | Exempt |
| CNP CYPRIALIFE | EXCLUDE | Same |
| ALLIANZ CYPRUS | EXCLUDE | Same |
| ATLANTIC INSURANCE | EXCLUDE | Same |
| ASFALEIA, INSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Notes |
|---|---|---|
| CYPRUS POST, KYPRIAKO TACHYDROMEIO | EXCLUDE for standard post | Universal service, exempt |
| CYPRUS POST (parcel/courier) | Domestic 19% | Non-universal |
| AKIS EXPRESS, ACS COURIER CY | Domestic 19% | Courier |
| DHL INTERNATIONAL | EU reverse charge | Check invoice entity |

### 3.6 Transport

| Pattern | Treatment | Notes |
|---|---|---|
| TRAVEL EXPRESS, INTERCITY BUSES | Domestic 19% | Bus |
| TAXI | Domestic 19% | Local |
| RYANAIR, WIZZ AIR (international) | EXCLUDE / 0% | International flight |

### 3.7 Food retail (blocked unless hospitality)

| Pattern | Treatment | Notes |
|---|---|---|
| ALPHAMEGA, PAPANTONIOU, LIDL CY, CARREFOUR CY | Default BLOCK | Personal provisioning |
| RESTAURANT, ESTIATORIO, TAVERNA | Default BLOCK | Entertainment |

### 3.8 SaaS — EU suppliers (reverse charge, Box 2 output + Box 4 input)

| Pattern | Billing entity | Notes |
|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | EU reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Reverse charge |
| LINKEDIN | LinkedIn Ireland Unlimited (IE) | Reverse charge |
| SPOTIFY | Spotify AB (SE) | EU reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | Reverse charge |
| ATLASSIAN | Atlassian Network Services BV (NL) | EU reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | Reverse charge |

### 3.9 SaaS — non-EU suppliers (reverse charge, Box 2 output + Box 4 input)

| Pattern | Billing entity | Notes |
|---|---|---|
| AWS EMEA SARL | AWS EMEA SARL (LU) | LU = EU reverse charge |
| NOTION | Notion Labs Inc (US) | Non-EU reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Non-EU reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | Non-EU reverse charge |
| GITHUB | GitHub Inc (US) | Check if billed by IE |
| FIGMA | Figma Inc (US) | Non-EU reverse charge |
| CANVA | Canva Pty Ltd (AU) | Non-EU reverse charge |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |

### 3.11 Professional services (Cyprus)

| Pattern | Treatment | Notes |
|---|---|---|
| DIKIGOROS, LAWYER, ADVOCATE | Domestic 19% | Legal |
| LOGISTIS, ACCOUNTANT, AUDITOR | Domestic 19% | Accounting |
| SYMVOLAIOGRAFOS, NOTARY | Domestic 19% | Notary |

### 3.12 Payroll and social security (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| KOINONIKES ASFALISIS, SOCIAL INSURANCE | EXCLUDE | Social contributions |
| SALARY, MISTHOS | EXCLUDE | Wages |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| ENOIKIO, RENT (commercial with VAT) | Domestic 19% | Commercial lease |
| ENOIKIO, RENT (residential) | EXCLUDE | Exempt |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL | EXCLUDE | Internal movement |
| MERISMA, DIVIDEND | EXCLUDE | Out of scope |
| LOAN REPAYMENT | EXCLUDE | Loan principal |
| ATM, CASH WITHDRAWAL | Ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Non-EU SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`

**Reasoning:**
US entity. Self-assess output VAT at 19% in Box 2. Claim input in Box 4. Net zero. Box 11B value not applicable (non-EU service — use Box 7 only).

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (input) | Box (output) | Default? | Question? |
|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -14.68 | -14.68 | 2.79 | 19% | 4 | 2 | N | — |

### Example 2 — EU service reverse charge (Google Ads)

**Input line:**
`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads ; -850.00 ; EUR`

**Reasoning:**
IE entity. EU reverse charge. Output in Box 2, input in Box 4. Value in Box 11B.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (input) | Box (output) | Default? | Question? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 161.50 | 19% | 4 | 2 | N | — |

### Example 3 — Entertainment

**Input line:**
`15.04.2026 ; COLUMBIA STEAK HOUSE LIMASSOL ; DEBIT ; Business dinner ; -220.00 ; EUR`

**Reasoning:**
Restaurant. Entertainment input VAT is blocked in Cyprus under the general "not for business use" principle. Default: block.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | COLUMBIA STEAK HOUSE | -220.00 | -220.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked" |

### Example 4 — Capital goods

**Input line:**
`18.04.2026 ; LOGITECH CYPRUS ; DEBIT ; Laptop ; -1,595.00 ; EUR`

**Reasoning:**
Business equipment. Input VAT deductible at 19%. No specific capital goods threshold in Cyprus VAT4 (unlike Malta). Goes to Box 4.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | LOGITECH CYPRUS | -1,595.00 | -1,340.34 | -254.66 | 19% | 4 | N | — |

### Example 5 — EU B2B service sale

**Input line:**
`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; IT consultancy ; +3,500.00 ; EUR`

**Reasoning:**
B2B service to Germany. Place of supply = Germany. 0% in Box 8B. Verify USt-IdNr.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | STUDIO KREBS GMBH | +3,500.00 | +3,500.00 | 0 | 0% | 8B | Y | Q2 (HIGH) "Verify USt-IdNr" |

### Example 6 — Motor vehicle

**Input line:**
`28.04.2026 ; PETROLINA STATIONS ; DEBIT ; Fuel ; -60.00 ; EUR`

**Reasoning:**
Fuel. In Cyprus, input VAT on motor vehicle fuel is deductible if vehicle is used for business. Unlike Malta's hard block, Cyprus allows deduction proportional to business use. Default: 0% (business use unknown).

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | PETROLINA STATIONS | -60.00 | -60.00 | 0 | — | — | Y | Q3 "Vehicle business-use %?" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 19% (VAT Law Section 17)
Default rate. Output: Box 1. Input: Box 4.

### 5.2 Reduced rate 9% (Fifth Schedule Part II)
Accommodation, restaurant/catering services.

### 5.3 Reduced rate 5% (Fifth Schedule Part III)
Food, pharmaceuticals, books, newspapers, water supply, medical devices.

### 5.4 Reduced rate 3%
Specific social housing.

### 5.5 Zero rate (Sixth Schedule)
Exports, intra-EU B2B goods (Box 8A), intra-EU B2B services (Box 8B), international transport.

### 5.6 Exempt without credit (Seventh Schedule)
Financial services, insurance, healthcare, education, postal, gambling, residential rental.

### 5.7 Reverse charge — EU services received (Section 11A)
Output VAT at 19% in Box 2, input in Box 4. Value in Box 11B.

### 5.8 Reverse charge — EU goods received (Section 11)
Output in Box 2, input in Box 4. Value in Box 11A.

### 5.9 Reverse charge — non-EU services (Section 11A)
Same mechanism: output Box 2, input Box 4.

### 5.10 Domestic reverse charge — construction (Section 11B)
Output and input both reported by recipient. Flag for reviewer — R-CY-3.

### 5.11 Blocked input VAT
- Entertainment: blocked (no specific statutory list like Malta's 10th Schedule; follows general business-use principle)
- Personal use: blocked
- Motor vehicles: proportional deduction based on business use (not hard-blocked like Malta)

### 5.12 Cyprus consolidated Box structure
Unlike Malta's ~45-box periodic VAT return, Cyprus VAT4 has only 11 boxes plus sub-boxes. All rates are aggregated into Box 1 (output) and Box 4 (input).

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Fuel and vehicle costs
*Default:* 0%. *Question:* "Vehicle type and business-use percentage?"

### 6.2 Entertainment
*Default:* block. *Question:* "Business purpose? (Note: blocked regardless in most cases.)"

### 6.3 Ambiguous SaaS
*Default:* non-EU reverse charge. *Question:* "Check invoice entity."

### 6.4 Owner transfers
*Default:* exclude. *Question:* "Customer payment, own money, or loan?"

### 6.5 Individual incoming
*Default:* domestic B2C at 19%. *Question:* "Sale? Country?"

### 6.6 Foreign incoming
*Default:* 19%. *Question:* "B2B? Country? VAT number?"

### 6.7 Large purchases
*Default:* deductible; flag if capital. *Question:* "Useful life > 1 year?"

### 6.8 Mixed-use telecom/home office
*Default:* 0%. *Question:* "Business line or mixed?"

### 6.9 Outgoing to individuals
*Default:* exclude. *Question:* "Contractor, wages, or personal?"

### 6.10 Cash withdrawals
*Default:* exclude. *Question:* "Cash purpose?"

### 6.11 Rent
*Default:* exempt (residential). *Question:* "Commercial or residential?"

---

## Section 7 — Excel working paper template (Cyprus-specific)

Per `vat-workflow-base` Section 3. Column H accepts CY VAT4 box codes (1-11B). Sheet "Box Summary" maps directly to the VAT4 form. Bottom-line: Box 5 (net payable/refundable = Box 3 minus Box 4).

---

## Section 8 — Cyprus bank statement reading guide

**CSV conventions.** Bank of Cyprus and Hellenic Bank typically use comma delimiters, DD/MM/YYYY dates.

**Greek language variants.** Enoikio (rent), misthos (salary), tokoi (interest), metafora (transfer). Treat as English equivalent.

**Internal transfers.** "Own transfer", "esoteriki metafora". Exclude.

**IBAN prefix.** CY = Cyprus. IE, DE, NL = EU. US, GB = non-EU.

---

## Section 9 — Onboarding fallback

### 9.1 Entity type
*Inference:* Ltd = company; sole trader. *Fallback:* "Company or self-employed?"

### 9.2 VAT registration
*Fallback:* "Are you VAT-registered?"

### 9.3 VAT number
*Fallback:* "CY VAT number? (CY + 8 digits + letter)"

### 9.4 Filing period
*Inference:* quarterly by default. *Fallback:* "Which quarter?"

### 9.5 Industry
*Fallback:* "What does the business do?"

### 9.6 Exempt supplies
*Fallback:* "Any exempt supplies?" *If yes: R-CY-2.*

### 9.7 Credit brought forward
*Fallback:* "Excess VAT credit from prior quarter?"

### 9.8 Cross-border customers
*Fallback:* "Customers outside Cyprus?"

---

## Section 10 — Reference material

### Sources
1. VAT Law N.95(I)/2000 (as amended)
2. Fifth-Ninth Schedules (rates, exemptions, special schemes)
3. Sections 11, 11A-11E (reverse charge provisions)
4. EU VAT Directive 2006/112/EC — via companion skill
5. VIES — https://ec.europa.eu/taxation_customs/vies/

### Known gaps
1. Ship management/maritime sector not covered.
2. Construction domestic reverse charge (Section 11B) flagged as refusal.
3. Immovable property special rules not detailed.

### Change log
- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. Cypriot banks (Bank of Cyprus, Hellenic Bank, RCB).
- **v1.0 (April 2026):** Initial skill.

## End of Cyprus VAT Return Skill v2.0

This skill is incomplete without BOTH companion files: `vat-workflow-base` v0.1+ AND `eu-vat-directive` v0.1+.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
