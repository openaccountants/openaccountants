---
name: singapore-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Singapore GST return (GST F5 form) for any client. Trigger on phrases like "prepare GST return", "do the GST", "fill in GST F5", "create the return", "Singapore GST", "IRAS filing", or any request involving Singapore GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill covers Singapore only and only standard GST-registered persons filing GST F5. Group registrations, partial exemption with non-de-minimis exempt supplies, Approved 3rd Party Logistics schemes, and Major Exporter Scheme applications are all in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any Singapore GST work.
version: 2.0
---

# Singapore GST Return Skill (GST F5) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

| Field | Value |
|---|---|
| Country | Singapore (Republic of Singapore) |
| Standard rate | 9% (from 1 January 2024) |
| Prior rates | 8% (1 Jan 2023 – 31 Dec 2023), 7% (before 1 Jan 2023) |
| Zero rate | 0% (exports of goods, prescribed international services under Fifth Schedule) |
| Exempt supplies | Financial services (Fourth Schedule Part I), residential property (Part II), investment precious metals (Part III), digital payment tokens (Part IV) |
| Return form | GST F5 (standard quarterly return) |
| Filing portal | https://mytax.iras.gov.sg (myTax Portal) — electronic only, no paper filing |
| Authority | Inland Revenue Authority of Singapore (IRAS) |
| Currency | SGD only |
| Filing frequency | Quarterly (standard); Monthly (by special arrangement with IRAS, typically major exporters) |
| Deadline | One month after end of prescribed accounting period |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key GST F5 boxes (the boxes you will use most):**

| Box | Meaning |
|---|---|
| 1 | Total value of standard-rated supplies (net, before GST) |
| 2 | Total value of zero-rated supplies (exports, international services) |
| 3 | Total value of exempt supplies |
| 4 | Total value of supplies (derived: 1 + 2 + 3) |
| 5 | Total value of taxable purchases (net, before GST — informational for IRAS cross-check) |
| 6 | Output tax due (GST on Box 1 at 9%, plus reverse charge output, plus adjustments) |
| 7 | Input tax and refunds claimed (input GST on business purchases, bad debt relief, pre-registration claims) |
| 8 | Net GST to be paid to / (refunded by) IRAS (derived: 6 − 7) |
| 9 | Total value of goods imported under MES / Approved 3PL / other import GST suspension schemes |
| 10 | Tourist Refund Scheme claims (Yes/No) |
| 11 | Bad debt relief / reverse charge refund claims (Yes/No) |
| 12 | Pre-registration input tax claims (Yes/No) |
| 13 | Revenue (gross sales/income — informational) |
| 14 | Value of imported services / low-value goods subject to reverse charge |

**Conservative defaults — Singapore-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 9% (standard rate) |
| Unknown VAT status of a purchase | Not claimable |
| Unknown counterparty location | Domestic Singapore |
| Unknown whether customer "belongs" overseas (for zero-rating) | Belongs in Singapore, charge 9% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (non-resident supplier) |
| Unknown blocked-input status (motor car, club, entertainment) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | SGD 5,000 |
| HIGH tax-delta on a single conservative default | SGD 300 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net GST position | SGD 10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the quarter in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Singapore business bank: DBS, OCBC, UOB, Standard Chartered, HSBC Singapore, Citibank Singapore, Maybank Singapore, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices for the period (especially for zero-rated international services and exports), purchase invoices for any input tax claim above SGD 300, the client's GST registration number in writing (UEN format or M-format).

**Ideal** — complete invoice register, GST registration certificate, prior period GST F5, reconciliation of any brought-forward excess input tax.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This GST F5 was produced from bank statement alone. The reviewer must verify, before approval, that input tax claims above SGD 300 are supported by valid tax invoices and that all zero-rating and reverse charge classifications match the supplier's invoice."

### Singapore-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-SG-1 — Partial exemption with non-de-minimis exempt supplies.** *Trigger:* client makes both taxable and exempt supplies and the exempt input tax exceeds SGD 5,000 per quarter OR exceeds 5% of total input tax (i.e., de minimis test fails). *Message:* "Your exempt input tax exceeds the de minimis thresholds (SGD 5,000/quarter and 5% of total input tax). Input tax apportionment is required under Regulation 29 of the GST (General) Regulations. This skill cannot compute the apportionment ratio. Please engage a GST-registered tax agent to determine and confirm the recovery rate before input tax is claimed."

**R-SG-2 — GST group registration.** *Trigger:* client is part of a GST group registration. *Message:* "GST group registrations require consolidation across all group members and disregard of intra-group supplies. This skill covers single-entity GST F5 returns only. Please engage a GST-registered tax agent."

**R-SG-3 — Major Exporter Scheme (MES) or Approved 3PL.** *Trigger:* client is approved under MES or Approved 3PL scheme and is claiming import GST suspension. *Message:* "MES and Approved 3PL schemes have specific reporting and compliance requirements that go beyond standard GST F5 filing. This skill covers standard filing only. Please engage a GST-registered tax agent."

**R-SG-4 — Customer accounting for prescribed goods.** *Trigger:* client supplies or acquires prescribed goods (investment precious metals in non-qualifying form, mobile phones, memory cards above SGD 10,000). *Message:* "Customer accounting for prescribed goods requires specific Box 1/Box 6/Box 7 entries that differ from standard classification. Out of scope for this skill."

**R-SG-5 — Margin scheme.** *Trigger:* client deals in second-hand goods under the gross margin scheme. *Message:* "Margin scheme transactions require transaction-level margin computation. Out of scope."

**R-SG-6 — Voluntary disclosure of errors exceeding SGD 1,500.** *Trigger:* user wants to correct errors in a prior period that exceed the SGD 1,500 administrative concession threshold. *Message:* "Errors exceeding SGD 1,500 net GST per period cannot be corrected in the current return. A GST F7 voluntary disclosure must be filed separately. Please engage a GST-registered tax agent."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific.

### 3.1 Singapore banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| DBS, DEVELOPMENT BANK OF SINGAPORE, POSB | EXCLUDE for bank charges/fees | Financial service, exempt (Fourth Schedule Part I) |
| OCBC, OVERSEA-CHINESE BANKING | EXCLUDE for bank charges/fees | Same |
| UOB, UNITED OVERSEAS BANK | EXCLUDE for bank charges/fees | Same |
| STANDARD CHARTERED SG, STANCHART | EXCLUDE for bank charges/fees | Same |
| HSBC SINGAPORE | EXCLUDE for bank charges/fees | Same |
| CITIBANK SINGAPORE, CITI | EXCLUDE for bank charges/fees | Same |
| MAYBANK SINGAPORE | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, ASPIRE (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, INT EARNED, INT CHARGED | EXCLUDE | Interest income/expense, exempt financial service |
| LOAN, TERM LOAN, CREDIT FACILITY | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Singapore government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| IRAS, INLAND REVENUE | EXCLUDE | Tax payment, not a supply |
| GST PAYMENT, GST REFUND | EXCLUDE | GST payment/refund, not a supply |
| ACRA, ACCOUNTING AND CORPORATE REGULATORY | EXCLUDE | Registration/filing fees, government sovereign act |
| CPF, CENTRAL PROVIDENT FUND | EXCLUDE | Statutory contributions, out of scope |
| MOM, MINISTRY OF MANPOWER | EXCLUDE | Government levy (foreign worker levy, etc.) |
| CUSTOMS, SINGAPORE CUSTOMS | EXCLUDE for duty | Customs duty (but check for import GST — see Section 5.10) |
| GOVTECH, GOVERNMENT TECHNOLOGY AGENCY | EXCLUDE | Government fees |
| LTA, LAND TRANSPORT AUTHORITY | EXCLUDE | Government fees, COE, road tax |
| HDB, HOUSING DEVELOPMENT BOARD | EXCLUDE | Government housing, sovereign act |
| NEA, NATIONAL ENVIRONMENT AGENCY | EXCLUDE | Licence fees, government |
| EDB, ECONOMIC DEVELOPMENT BOARD | EXCLUDE | Government grants/fees |
| ENTERPRISE SINGAPORE, ESG | EXCLUDE | Government grants |

### 3.3 Singapore telecoms and utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| SINGTEL, SINGAPORE TELECOMMUNICATIONS | Domestic 9% | 5 (purchase) / 1 (if selling) | Telecoms — overhead, input tax claimable on business line |
| STARHUB | Domestic 9% | 5 / 1 | Same |
| M1, M1 LIMITED | Domestic 9% | 5 / 1 | Same |
| SIMBA TELECOM, CIRCLES.LIFE | Domestic 9% | 5 / 1 | MVNO telecoms |
| SP SERVICES, SP GROUP, SINGAPORE POWER | Domestic 9% | 5 | Electricity, gas, water — overhead |
| SEMBCORP POWER, GENECO, KEPPEL ELECTRIC | Domestic 9% | 5 | Electricity retailer — overhead |
| PUB, PUBLIC UTILITIES BOARD | Domestic 9% | 5 | Water — overhead |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| GREAT EASTERN, GE LIFE | EXCLUDE | Life insurance exempt (Fourth Schedule) |
| PRUDENTIAL SINGAPORE | EXCLUDE | Life insurance exempt |
| AIA SINGAPORE | EXCLUDE | Life insurance exempt |
| NTUC INCOME, INCOME INSURANCE | EXCLUDE | Life insurance exempt; general insurance is standard-rated — check invoice |
| AVIVA, SINGLIFE | EXCLUDE | Life insurance exempt |
| INSURANCE PREMIUM, LIFE INSURANCE | EXCLUDE | Default exempt unless clearly general/property insurance |

### 3.5 Transport (Singapore domestic)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| GRAB, GRABCAR, GRABTAXI | Domestic 9% | 5 | Ride-hailing, taxable. Check: platform fee vs ride fare on invoice |
| GOJEK, GOJEK SG | Domestic 9% | 5 | Same |
| COMFORTDELGRO, COMFORT TAXI, CITYCAB | Domestic 9% | 5 | Taxi, standard rated |
| SMRT, SMRT CORPORATION | Domestic 9% | 5 | Taxi/bus services standard rated |
| EZ-LINK, EZLINK, TRANSITLINK | Domestic 9% | 5 | Top-up for public transport |
| SINGAPORE AIRLINES, SIA (domestic) | Domestic 9% if domestic charter | 1 / 5 | International flights — see 3.6 |
| BUS, MRT (generic transport labels) | Domestic 9% | 5 | Standard rated local transport |

### 3.6 Airlines and international transport (zero-rated or exclude)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| SINGAPORE AIRLINES, SIA (international) | Zero-rated / EXCLUDE | 2 (if selling) | International passenger transport zero-rated |
| SCOOT, SCOOT TIGERAIR | Zero-rated / EXCLUDE | 2 | Same |
| JETSTAR ASIA | Zero-rated / EXCLUDE | 2 | International flights |
| CATHAY PACIFIC, EMIRATES, QANTAS | EXCLUDE | | Foreign airline, international flight |

### 3.7 Food retail (blocked unless hospitality/F&B business)

| Pattern | Treatment | Notes |
|---|---|---|
| NTUC FAIRPRICE, FAIRPRICE | Default BLOCK input tax | Personal provisioning. Claimable only if F&B/hospitality business purchasing stock-in-trade |
| COLD STORAGE, GIANT, SHENG SIONG | Default BLOCK | Same |
| RESTAURANTS, CAFES (any named restaurant) | Default BLOCK | Entertainment blocked unless staff welfare meal at workplace |
| FOODPANDA, DELIVEROO | Default BLOCK | Food delivery — personal provisioning default |

### 3.8 SaaS — non-resident suppliers (reverse charge)

From 1 January 2020, imported services from non-resident suppliers to GST-registered persons are subject to reverse charge under Section 14(2) of the GST Act. The recipient self-assesses output tax in Box 6 and claims input tax in Box 7 (net zero for fully taxable business). Report value in Box 14.

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Asia Pacific Pte Ltd (SG) or Google Ireland Ltd (IE) or Google LLC (US) | Check invoice | If SG entity: domestic 9%, Box 5. If non-resident: reverse charge, Box 14/6/7 |
| MICROSOFT (365, Azure) | Microsoft Regional Sales Pte Ltd (SG) or Microsoft Ireland Operations Ltd (IE) | Check invoice | If SG entity: domestic 9%. If non-resident: reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) or Adobe Inc (US) | 14/6/7 | Typically non-resident, reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 14/6/7 | Non-resident, reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 14/6/7 | Non-resident, reverse charge |
| AWS, AMAZON WEB SERVICES | Amazon Web Services Inc (US) or AWS Singapore entity | Check invoice | US entity: reverse charge. SG entity: domestic 9% |
| NOTION | Notion Labs Inc (US) | 14/6/7 | Non-resident, reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 14/6/7 | Non-resident, reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 14/6/7 | Non-resident, reverse charge |
| GITHUB | GitHub Inc (US) | 14/6/7 | Non-resident, reverse charge |
| FIGMA | Figma Inc (US) | 14/6/7 | Non-resident, reverse charge |
| CANVA | Canva Pty Ltd (AU) | 14/6/7 | Non-resident, reverse charge |
| SLACK | Slack Technologies LLC (US) or Salesforce SG | Check invoice | US: reverse charge. SG entity: domestic 9% |
| ATLASSIAN (Jira, Confluence) | Atlassian Pty Ltd (AU) or Atlassian Inc (US) | 14/6/7 | Non-resident, reverse charge |
| ZOOM | Zoom Video Communications Inc (US) | 14/6/7 | Non-resident, reverse charge |
| HUBSPOT | HubSpot Inc (US) | 14/6/7 | Non-resident, reverse charge |
| STRIPE (subscription fees) | Stripe Inc (US) | 14/6/7 | Non-resident, reverse charge |
| TWILIO | Twilio Inc (US) | 14/6/7 | Non-resident, reverse charge |
| SHOPIFY | Shopify Inc (CA) | 14/6/7 | Non-resident, reverse charge |

### 3.9 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing / financial intermediation, exempt |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| STRIPE (monthly subscription) | Reverse charge Box 14/6/7 | US entity — separate from exempt transaction fees |
| HITPAY, ATOME | Check invoice | If SG entity: domestic 9%. If not: reverse charge |

### 3.10 Retail and supermarkets (Singapore)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| NTUC FAIRPRICE, FAIRPRICE | Domestic 9% | 5 | Input claimable only for business stock-in-trade purchases |
| COLD STORAGE, MARKETPLACE | Domestic 9% | 5 | Same |
| GIANT, SHENG SIONG | Domestic 9% | 5 | Same |
| GUARDIAN, WATSONS | Domestic 9% | 5 | Pharmacy/personal care |
| DON DON DONKI, DAISO | Domestic 9% | 5 | Retail |

### 3.11 Professional services (Singapore)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| LAW FIRM names, ADVOCATES, SOLICITORS | Domestic 9% | 5 | Legal fees, input claimable if business purpose |
| ACCOUNTANT, CPA, AUDIT FIRM | Domestic 9% | 5 | Accounting/audit, always claimable |
| CORPORATE SECRETARY, BOARDROOM | Domestic 9% | 5 | Company secretarial, claimable |
| ACRA (filing fees) | EXCLUDE | | Government fee |

### 3.12 Payroll and statutory contributions (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| CPF, CENTRAL PROVIDENT FUND | EXCLUDE | Statutory CPF contributions |
| SALARY, WAGES, PAYROLL | EXCLUDE | Employment, out of scope |
| SDL, SKILLS DEVELOPMENT LEVY | EXCLUDE | Statutory levy |
| FWL, FOREIGN WORKER LEVY | EXCLUDE | Government levy |
| BONUS, COMMISSION (to employees) | EXCLUDE | Employment, out of scope |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| COMMERCIAL RENT, OFFICE RENT (with GST invoice) | Domestic 9%, Box 5 | Commercial property lease, input claimable |
| HDB RENT (residential) | EXCLUDE | Residential lease, exempt (Fourth Schedule Part II) |
| RESIDENTIAL RENT, CONDO RENT | EXCLUDE | Residential lease, exempt |
| SERVICED APARTMENT, HOTEL (short-stay) | Domestic 9%, Box 5 | Hotel/serviced apartment is standard rated, not exempt |
| JTC, JURONG TOWN CORPORATION | Domestic 9%, Box 5 | Industrial property, standard rated |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL, ACCOUNT TRANSFER | EXCLUDE | Internal movement |
| DIVIDEND, DIV PAYMENT | EXCLUDE | Dividend, out of scope |
| LOAN REPAYMENT, REPAYMENT | EXCLUDE | Loan principal, out of scope |
| CASH WITHDRAWAL, ATM | TIER 2 — ask | Default exclude; ask what cash was spent on |
| DIRECTOR FEE (paid to director as employee) | EXCLUDE | Employment relationship, out of scope |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Singapore-based self-employed IT consultant. They illustrate the trickiest cases.

### Example 1 — Non-resident SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; SGD 21.44`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.8). No GST on the invoice. This is an imported service from a non-resident supplier. Under Section 14(2), the recipient must self-assess reverse charge: output tax in Box 6, input tax in Box 7. Report the value in Box 14. Net effect zero for a fully taxable business. Also include in Box 5 (taxable purchases).

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Box (input) | Box (output) | Box 14 | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -21.44 | -21.44 | 1.93 | 9% | 7 | 6 | 21.44 | N | — | — |

### Example 2 — Zero-rated international service sale

**Input line:**
`10.04.2026 ; TECHCORP PTY LTD ; CREDIT ; Invoice SG-2026-018 IT consultancy March ; +5,000.00 ; SGD`

**Reasoning:**
Incoming SGD 5,000 from an Australian company. The client provides IT consulting services. The customer "belongs" outside Singapore (no GST registration in SG, no SG establishment). Under Fifth Schedule Para 1, this is a zero-rated international service — provided the service is not performed on goods in Singapore and does not directly benefit a person in SG other than the overseas customer. Report in Box 2. No output tax. Confirm: the customer has no SG establishment and the service has no direct SG benefit.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | TECHCORP PTY LTD | +5,000.00 | +5,000.00 | 0 | 0% | 2 | Y | Q1 (HIGH) | "Verify customer belongs overseas — no SG establishment?" |

### Example 3 — Motor car expense, permanently blocked

**Input line:**
`15.04.2026 ; SHELL SINGAPORE ; DEBIT ; Petrol ; -120.00 ; SGD`

**Reasoning:**
Petrol purchase. Input tax on motor car expenses (purchase, hire, running costs including petrol, maintenance, parking, ERP) is permanently blocked under Regulation 26(1) of the GST (General) Regulations. The only exceptions are taxis, private hire cars used exclusively for chauffeured transport, motor dealers' stock-in-trade, and driving schools. An IT consultant does not qualify. Default: full block, no input tax recovery.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | SHELL SINGAPORE | -120.00 | -120.00 | 0 | — | — | Y | Q2 | "Motor car expense: blocked under Reg 26(1)" |

### Example 4 — Domestic standard-rated purchase (office equipment)

**Input line:**
`18.04.2026 ; COURTS SINGAPORE ; DEBIT ; Invoice CT-2026-441 Office desk ; -856.00 ; SGD`

**Reasoning:**
Courts Singapore is a local retailer. The gross amount is SGD 856 inclusive of 9% GST. Net = 856 x (100/109) = SGD 785.32. GST = SGD 70.68. Standard-rated domestic purchase used for business. Input tax claimable. Goes to Box 5 (taxable purchases) and Box 7 (input tax).

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Box (purchase) | Box (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | COURTS SINGAPORE | -856.00 | -785.32 | -70.68 | 9% | 5 | 7 | N | — | — |

### Example 5 — Club membership, permanently blocked

**Input line:**
`22.04.2026 ; SINGAPORE RECREATION CLUB ; DEBIT ; Annual subscription ; -3,200.00 ; SGD`

**Reasoning:**
Club membership fee. Input tax on club membership fees (country club, golf club, recreation club subscriptions) is permanently blocked under Regulation 27(1)(a). No exceptions. Default: full block.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | SINGAPORE RECREATION CLUB | -3,200.00 | -3,200.00 | 0 | — | — | Y | Q3 | "Club membership: blocked under Reg 27(1)(a)" |

### Example 6 — Exempt financial service (bank charges)

**Input line:**
`28.04.2026 ; DBS BANK ; DEBIT ; Monthly account maintenance fee ; -15.00 ; SGD`

**Reasoning:**
Bank maintenance fee. Financial services are exempt under Fourth Schedule Part I. No GST is charged by the bank. No input tax to claim. Exclude from the return.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | DBS BANK | -15.00 | — | — | — | — | N | — | "Exempt financial service" |

---

## Section 5 — Tier 1 classification rules (compressed)

Each rule states the legal source and the box mapping. Apply silently if the data is unambiguous.

### 5.1 Standard rate 9% (GST Act Section 7, Section 16)

Default rate for any taxable supply in Singapore unless zero-rated or exempt. Sales go to Box 1. Output tax goes to Box 6. Purchases go to Box 5. Input tax goes to Box 7.

### 5.2 Zero-rated supplies (GST Act Section 21, 22; Fifth Schedule)

Exports of goods physically shipped out of Singapore with export documentation. International services meeting Fifth Schedule conditions (especially Para 1 — service to overseas person, not performed on goods in SG, no direct SG benefit). Sales go to Box 2. No output tax. Input tax on related purchases is claimable.

### 5.3 Exempt supplies (Fourth Schedule)

Prescribed financial services (interest, currency exchange, securities, life insurance, bank account operation). Residential property sale or lease (not hotel/serviced apartment). Investment precious metals meeting purity standards. Digital payment tokens. Sales go to Box 3. No output tax. No input tax recovery on directly attributable costs.

### 5.4 Out of scope

Salaries, wages, CPF contributions, government grants/subsidies, dividends, loan principal, private transactions, TOGC, statutory penalties. Not reported on GST F5. Exclude entirely.

### 5.5 Reverse charge — imported services (GST Act Section 14(2))

From 1 January 2020, when the client receives services from a non-resident supplier who is not GST-registered in SG: self-assess output tax at 9% in Box 6, claim input tax in Box 7 (if entitled), report value in Box 14. Net effect zero for a fully taxable business. Applies to all services and from 1 January 2023, also to imported low-value goods (value not exceeding SGD 400).

### 5.6 Domestic purchases — standard rated

Input tax on a valid tax invoice from a GST-registered Singapore supplier is claimable for purchases used in taxable business activity. Subject to blocked-input rules (5.8) and the five conditions in Section 20. Report in Box 5 (value) and Box 7 (input tax).

### 5.7 Import of goods

Goods imported via Singapore Customs. Import GST is paid at the border (or deferred under IGDS for approved businesses). Report in Box 5 (value). Input GST claimed in Box 7. Customs import permit is the supporting document (not a tax invoice).

### 5.8 Blocked input tax (GST (General) Regulations, Reg 26-27)

The following categories have zero GST recovery with no exceptions unless specifically noted:
- Motor cars: purchase, hire, import of motor cars and related running expenses (petrol, maintenance, parking, ERP) — Reg 26(1). Exception: taxis, private hire cars for chauffeured transport, motor dealers' stock-in-trade, driving schools.
- Club membership fees: country club, golf club, recreation club — Reg 27(1)(a). No exceptions.
- Medical expenses for employees — Reg 27(1)(b). Exception: medical expenses required under Work Injury Compensation Act or Employment Act.
- Family benefits for employees/directors' family members — Reg 27(1)(c). No exceptions.
- Costs of non-business transactions — Reg 26(2). No exceptions.

Blocked categories override any other recovery rule. Check blocked status before applying recovery.

### 5.9 Deemed supplies

Gifts exceeding SGD 200 per recipient in a 12-month period — deemed supply, output tax due at 9% on cost. Private use of business assets — deemed supply if not insignificant. Report in Box 1 (value) and Box 6 (output tax).

### 5.10 Transitional rate rules (8% to 9%, 1 January 2024)

Supply made before 1 Jan 2024: apply 8%. Supply made on/after 1 Jan 2024: apply 9%. Spanning supplies: apportion. For current periods (2024 onward), always use 9%.

### 5.11 Sales — domestic standard

Charge 9% on all local sales of goods and services. No distinction between B2B and B2C for domestic supplies. Map to Box 1 (net) and Box 6 (output tax).

### 5.12 Sales — zero-rated export of goods

Goods physically shipped out of Singapore. Retain export documentation (export permit, bill of lading, airway bill). Map to Box 2. No output tax.

### 5.13 Sales — zero-rated international services (Fifth Schedule)

Service to customer who "belongs" outside Singapore. Customer must not be GST-registered in SG, must have no SG establishment, must have usual residence outside SG. The service must not be performed on goods in SG (unless goods are subsequently exported), and must not directly benefit a person in SG other than the overseas customer. Map to Box 2. No output tax.

### 5.14 Credit notes and adjustments

Credit notes issued reduce output tax. Credit notes received reduce input tax. Adjust in the period the credit note is issued/received. For errors in prior periods: if net GST error does not exceed SGD 1,500, adjust in the next return. If exceeds SGD 1,500, file GST F7.

---

## Section 6 — Tier 2 catalogue (compressed)

For each ambiguity type: pattern, why the bank statement is insufficient, conservative default, question for the structured form.

### 6.1 Motor car vs commercial vehicle

*Pattern:* Shell, SPC, Esso, petrol, parking, ERP, car wash. *Why insufficient:* vehicle type unknown. Motor car expenses are permanently blocked; commercial vehicle (van, lorry, motorcycle) expenses are claimable. *Default:* 0% recovery (assume motor car). *Question:* "Is this for a motor car (blocked) or a commercial vehicle/motorcycle used for business?"

### 6.2 Entertainment and hospitality

*Pattern:* restaurant, cafe, bar, catering, event. *Why insufficient:* entertainment for non-business purposes is blocked; staff welfare meals at workplace may be claimable. *Default:* block. *Question:* "Was this entertainment (blocked) or a staff welfare meal at the workplace?"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, AWS, Slack, Shopify where the legal entity is not visible. *Why insufficient:* some brands have Singapore entities (domestic 9%) and overseas entities (reverse charge). *Default:* reverse charge (non-resident). *Question:* "Could you check the invoice for the legal entity name? I need to know if it is a Singapore-registered entity or an overseas company."

### 6.4 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit from a name matching the client's name. *Why insufficient:* could be a customer sale, owner injection, or loan. *Default:* exclude as owner injection. *Question:* "The SGD X transfer from [name] — is this a customer payment, your own money going in, or a loan?"

### 6.5 Incoming transfers from individual names (not owner)

*Pattern:* incoming from private-looking counterparties. *Why insufficient:* could be B2C sale, refund, loan. *Default:* domestic sale at 9%, Box 1/6. *Question:* "For each: was it a sale? Business or consumer? Local or overseas customer?"

### 6.6 Incoming transfers from foreign counterparties

*Pattern:* foreign bank, foreign currency. *Why insufficient:* could be zero-rated service, domestic supply paid from overseas, refund. *Default:* domestic 9%. *Question:* "What was this — a service to an overseas customer (potentially zero-rated), a domestic sale, or something else? Does the customer have any SG establishment?"

### 6.7 Medical expenses

*Pattern:* clinic, hospital, medical, dental, health insurance. *Why insufficient:* medical expenses for employees are blocked under Reg 27(1)(b) unless required by Work Injury Compensation Act or Employment Act. *Default:* blocked. *Question:* "Is this medical expense required by statute (Work Injury Compensation Act)? If so, input tax may be claimable."

### 6.8 Mixed-use phone, internet, home office

*Pattern:* Singtel, StarHub, M1 personal lines; home electricity. *Why insufficient:* business proportion unknown. *Default:* 0% if mixed without declared %, 100% if confirmed pure business line. *Question:* "Is this a dedicated business line or mixed-use? What business percentage would you estimate?"

### 6.9 Outgoing transfers to individuals

*Pattern:* outgoing to private-looking names. *Why insufficient:* could be contractor payment, wages, refund, drawings. *Default:* exclude as drawings. *Question:* "Was this a contractor you paid (with invoice), wages, a refund to a customer, or a personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* ATM, cash withdrawal. *Why insufficient:* unknown what cash was spent on. *Default:* exclude as owner drawing. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* monthly rent to a landlord-sounding counterparty. *Why insufficient:* commercial vs residential. *Default:* no GST, exclude (residential default). *Question:* "Is this commercial property rent (GST claimable with tax invoice) or residential (exempt)?"

### 6.12 Insurance payments

*Pattern:* insurance premium payments. *Why insufficient:* life insurance is exempt; general insurance (property, motor, health, travel) is standard-rated at 9%. *Default:* exclude (life insurance default). *Question:* "Is this life insurance (exempt) or general/property/motor insurance (standard-rated, input tax claimable)?"

---

## Section 7 — Excel working paper template (Singapore-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Singapore-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Box code") accepts only valid Singapore GST F5 box codes from Section 1 of this skill: 1, 2, 3, 5, 6, 7, 14. Use blank for excluded transactions. For reverse-charge transactions, enter "RC" in column H and the value will feed into Box 6 (output), Box 7 (input), and Box 14 (value).

### Sheet "Box Summary"

One row per box. Column A is the box number, column B is the description, column C is the value computed via formula. Mandatory rows:

```
Supply boxes:
| 1  | Standard-rated supplies | =SUMIFS(Transactions!E:E, Transactions!H:H, "1") |
| 2  | Zero-rated supplies | =SUMIFS(Transactions!E:E, Transactions!H:H, "2") |
| 3  | Exempt supplies | =SUMIFS(Transactions!E:E, Transactions!H:H, "3") |
| 4  | Total supplies | =Box_Summary!C[1_row]+C[2_row]+C[3_row] |

Purchase box:
| 5  | Total taxable purchases | =SUMIFS(Transactions!E:E, Transactions!H:H, "5")+SUMIFS(Transactions!E:E, Transactions!H:H, "RC") |

Tax boxes:
| 6  | Output tax due | =C[1_row]*0.09 + SUMIFS(Transactions!E:E, Transactions!H:H, "RC")*0.09 |
| 7  | Input tax claimed | =SUMIFS(Transactions!F:F, Transactions!H:H, "5") + SUMIFS(Transactions!E:E, Transactions!H:H, "RC")*0.09 |
| 8  | Net GST | =C[6_row]-C[7_row] |

Reporting boxes:
| 14 | Reverse charge value | =SUMIFS(Transactions!E:E, Transactions!H:H, "RC") |
```

### Sheet "Return Form"

Final GST F5-ready figures. The bottom-line cell is Box 8:
```
Box 8 = Box 6 - Box 7

IF Box 8 > 0:
  GST payable to IRAS
ELSE:
  GST refundable by IRAS
```

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values from the bank statement (column D of Transactions), black for formulas (everything in Box Summary and Return Form), green for cross-sheet references (Return Form referencing Box Summary), yellow background for any row in Sheet "Transactions" where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/singapore-gst-<period>-working-paper.xlsx
```

Check the JSON output. If `status` is `errors_found`, fix the formulas and re-run. If `status` is `success`, present via `present_files`.

---

## Section 8 — Singapore bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Singapore-specific patterns.

**DBS / POSB statement format.** DBS Business banking exports typically use CSV with DD/MM/YYYY or YYYY-MM-DD dates. Common columns: Transaction Date, Reference, Debit Amount, Credit Amount, Transaction Ref1, Transaction Ref2. The description field is often split across Ref1 and Ref2 — concatenate them for counterparty identification. DBS ibanking exports may use "CR" and "DR" labels. POSB business accounts follow the same format as DBS.

**OCBC statement format.** OCBC Velocity exports use CSV with columns: Transaction date, Value date, Description, Withdrawals, Deposits, Balance. Description field contains the counterparty name and reference. Cheque numbers appear as separate entries. FAST/PayNow transfers show as "FAST PAYMENT" or "PAYNOW" with the recipient name in the description.

**UOB statement format.** UOB BIBPlus exports use CSV with columns: Transaction Date, Transaction Description, Withdrawal, Deposit, Balance. The description field is a single concatenated field. GIRO payments appear as "GIRO" with the beneficiary name.

**Revolut / Wise Business.** ISO date format (YYYY-MM-DD). Revolut shows counterparty name clearly. Wise shows the recipient name and currency conversion details. Both may have separate fee lines — exclude fee lines (exempt financial service).

**Internal transfers and exclusions.** Own-account transfers between the client's DBS, OCBC, UOB, Revolut accounts. Labelled "own transfer", "internal transfer", "IBT" (inter-bank transfer). Always exclude.

**Sole proprietor draws.** A self-employed sole trader cannot pay themselves wages. Any transfer to their personal account is a drawing. Exclude. A director of a company receiving director fees: exclude from GST (out of scope) but flag for income tax records.

**Refunds and reversals.** Identify by "refund", "reversal", "chargeback", "returned". Book as a negative in the same box as the original transaction. Correction is in the period the refund is booked.

**PayNow and FAST transfers.** PayNow transfers appear as "PAYNOW-" followed by mobile number or UEN. FAST transfers show "FAST" or "FAST PAYMENT". The counterparty name may be truncated — if unidentifiable, ask the client.

**Foreign currency transactions.** Convert to SGD at the exchange rate on the transaction date. Use the MAS exchange rate or the rate shown on the bank statement. Note the rate used in the Transactions sheet column L (Notes).

**CPF, SDL, FWL entries.** These are statutory contributions and levies, always out of scope. Exclude immediately without further analysis.

**GIRO entries.** GIRO debits for recurring payments (rent, utilities, insurance). The description usually contains the beneficiary name. Map to the appropriate category using Section 3.

---

## Section 9 — Onboarding fallback (only when inference fails)

The workflow in `vat-workflow-base` Section 1 mandates inferring the client profile from the data first and only confirming with the client in Step 4. The questionnaire below is a fallback.

### 9.1 Entity type and trading name
*Inference rule:* sole proprietor names often match the account holder name; company names include "Pte Ltd", "Pte. Ltd.", "LLP". *Fallback question:* "Are you a sole proprietor, a private limited company (Pte Ltd), or a partnership/LLP?"

### 9.2 GST registration status
*Inference rule:* if the client is asking for a GST F5, they are GST-registered. *Fallback question:* "Confirm you are GST-registered? What is your GST registration number (UEN format)?"

### 9.3 Filing period
*Inference rule:* first and last transaction dates on the bank statement. Standard is quarterly (calendar quarters). *Fallback question:* "Which quarter does this cover? Q1 (Jan–Mar), Q2 (Apr–Jun), Q3 (Jul–Sep), or Q4 (Oct–Dec)?"

### 9.4 Industry and sector
*Inference rule:* counterparty mix, sales description patterns. IT, consultancy, F&B, retail, logistics are recognisable. *Fallback question:* "In one sentence, what does the business do?"

### 9.5 Employees
*Inference rule:* CPF, salary, SDL, FWL outgoing transfers. *Fallback question:* "Do you have employees? If so, how many?"

### 9.6 Exempt supplies
*Inference rule:* presence of financial service income, residential rental income, precious metals trading. *Fallback question:* "Do you make any GST-exempt sales (financial services, residential property, investment precious metals)?" *If yes and non-de-minimis, R-SG-1 refuses.*

### 9.7 International customers
*Inference rule:* foreign bank credits, foreign currency, overseas company names. *Fallback question:* "Do you have customers outside Singapore? Are they businesses or consumers? Do any of them have an establishment in Singapore?"

### 9.8 Brought-forward excess input tax
*Inference rule:* not inferable from a single period statement. Always ask. *Question:* "Do you have any excess input tax carried forward from the previous quarter?"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the Malta v2.0 structure (quick reference at top, supplier library as lookup tables, worked examples, compressed rules, bank statement guide, onboarding fallback). It supersedes v1.0.

### Sources

**Primary legislation:**
1. Goods and Services Tax Act 1993 (Cap. 117A) — Sections 7, 14, 16, 20, 21, 22, 25; First Schedule (registration); Fourth Schedule (exempt); Fifth Schedule (international services)
2. GST (General) Regulations — Regulations 26-29 (blocked input tax, apportionment), 29A (de minimis), 40 (pre-registration claims), 46 (returns)
3. GST (Amendment) Act 2022 (rate change to 8% and 9%)

**IRAS guidance:**
4. IRAS e-Tax Guide "GST: General Guide for Businesses"
5. IRAS e-Tax Guide "GST: Guide on Imports"
6. IRAS e-Tax Guide "GST: Reverse Charge"
7. IRAS e-Tax Guide "GST: Rate Change (2024)"
8. IRAS e-Tax Guide "GST: Voluntary Disclosure of Errors"

**Other:**
9. myTax Portal — https://mytax.iras.gov.sg
10. MAS exchange rates — https://www.mas.gov.sg/statistics/exchange-rates

### Known gaps

1. The supplier pattern library covers the most common Singapore and international counterparties but does not cover every local SME or regional brand.
2. The worked examples are drawn from a hypothetical IT consultant. They do not cover F&B, retail, e-commerce, or construction specifically.
3. The de minimis test (SGD 5,000 / 5%) is referenced as a refusal trigger but the longer-period annual adjustment is not computed by this skill.
4. InvoiceNow (e-invoicing) requirements for voluntary registrants (from November 2025 / April 2026) are not covered in detail.
5. Customer accounting for prescribed goods (mobile phones, memory cards, IPM) is refused, not handled.
6. The OVR regime for non-resident suppliers is referenced but not a filing scenario this skill supports.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with Malta v2.0 structure. Quick reference moved to top (Section 1). Supplier pattern library restructured as literal lookup tables (Section 3) with Singapore-specific vendors (DBS, OCBC, UOB, Singtel, StarHub, M1, NTUC FairPrice, Grab, ComfortDelGro, GovTech, IRAS). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue restructured (Section 6). Excel working paper specification added (Section 7). Singapore bank statement reading guide added with DBS/OCBC format details (Section 8). Onboarding moved to fallback role (Section 9). Reference material moved to bottom (Section 10). Companion skill reference updated to vat-workflow-base v0.1.
- **v1.0 (April 2026):** Initial skill. Standalone document covering GST Act, box mappings, reverse charge, blocked categories, registration, filing deadlines, and penalties.

### Self-check (v2.0 of this document)

1. Quick reference at top with box table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 14 sub-tables).
3. Worked examples drawn from hypothetical IT consultant: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 14 rules).
5. Tier 2 catalogue compressed with inference rules: yes (Section 6, 12 items).
6. Excel template specification with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only, inference rules first: yes (Section 9, 8 items).
8. All 6 Singapore-specific refusals present: yes (Section 2, R-SG-1 through R-SG-6).
9. Reference material at bottom: yes (Section 10).
10. Motor car hard-block explicit: yes (Section 5.8 + Example 3).
11. Club membership hard-block explicit: yes (Section 5.8 + Example 5).
12. Reverse charge for imported services (Section 14(2)) explicit: yes (Example 1 + Section 5.5).
13. Zero-rated international service and "belongs" test explicit: yes (Example 2 + Section 5.13).
14. DBS/OCBC bank statement format guide: yes (Section 8).

## End of Singapore GST Return Skill v2.0

This skill is incomplete without the companion file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a GST F5 without both files loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, accredited tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
