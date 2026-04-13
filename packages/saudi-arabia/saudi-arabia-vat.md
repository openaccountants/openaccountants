---
name: saudi-arabia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Saudi Arabia VAT return for any client. Trigger on phrases like "prepare VAT return", "Saudi VAT", "ZATCA return", "KSA VAT", "fill in VAT return", "Fatoorah", "e-invoicing Saudi", or any request involving Saudi Arabia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers KSA only and only standard VAT-registered persons. VAT groups, profit margin schemes, partial exemption with significant exempt supplies, oil & gas sector special rules, and designated zone goods movement classifications are all in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any KSA VAT work.
version: 2.0
---

# Saudi Arabia VAT Return Skill v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

| Field | Value |
|---|---|
| Country | Kingdom of Saudi Arabia (KSA) |
| Standard rate | 15% (from 1 July 2020; previously 5% from 1 January 2018) |
| Zero rate | 0% (exports outside GCC, international transport, qualifying medicines, investment metals 99%+ purity, first residential property up to SAR 1,000,000 cap) |
| Exempt supplies | Financial services (interest/margin-based, Islamic finance equivalents), residential rental, life insurance |
| Return form | VAT return filed electronically via ZATCA portal |
| Filing portal | https://zatca.gov.sa (ZATCA portal) |
| Authority | Zakat, Tax and Customs Authority (ZATCA, formerly GAZT) |
| Currency | SAR only |
| Filing frequency | Monthly (annual taxable supplies > SAR 40,000,000); Quarterly (SAR 40,000,000 or less) |
| Deadline | Last day of the month following end of tax period |
| TIN format | 15-digit number starting with 3 and ending with 3 |
| E-invoicing | Phase 1 (generation) mandatory since 4 Dec 2021; Phase 2 (integration) rolling waves from 1 Jan 2023 |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Community |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key VAT return fields (the fields you will use most):**

| Field | Meaning |
|---|---|
| 1 | Standard-rated sales (15%) — VAT-exclusive amount |
| 2 | VAT on standard-rated sales (Field 1 x 15%) |
| 3 | Sales to GCC implementing states — VAT-exclusive amount |
| 4 | VAT on GCC sales |
| 5 | Zero-rated domestic sales — VAT-exclusive amount |
| 6 | Exports — VAT-exclusive amount |
| 7 | Exempt sales — VAT-exclusive amount |
| 8 | Standard-rated purchases (15%) — VAT-exclusive amount |
| 9 | VAT on standard-rated purchases (Field 8 x 15%) |
| 10 | Imports subject to VAT paid at Customs — VAT-exclusive amount |
| 11 | VAT paid at Customs |
| 12 | Imports via reverse charge — VAT-exclusive amount |
| 13 | VAT on reverse charge imports (Field 12 x 15%) |
| 14 | Zero-rated purchases — VAT-exclusive amount |
| 15 | Exempt purchases — VAT-exclusive amount |
| 16 | Adjustments to output VAT (credit notes, corrections) |
| 17 | Adjustments to input VAT (credit notes received, corrections) |
| 18 | Total output VAT (derived: Field 2 + Field 4 + Field 13 + Field 16) |
| 19 | Total input VAT (derived: Field 9 + Field 11 + Field 17) |
| 20 | Net VAT due (derived: Field 18 − Field 19) |

**E-invoicing phases summary:**

| Phase | Requirement | Status |
|---|---|---|
| Phase 1 (Generation) | All VAT-registered taxpayers must generate, store, and share e-invoices. XML or PDF/A-3 with embedded XML. QR code mandatory on simplified (B2C) invoices. Handwritten invoices prohibited. | Mandatory since 4 December 2021 |
| Phase 2 (Integration) | E-invoices reported to and validated by ZATCA platform (FATOORA) in near-real-time. ZATCA applies cryptographic stamp and UUID. QR code mandatory on ALL invoices. | Rolling waves from 1 January 2023. As of April 2026: Wave 24 (revenue > SAR 375K, deadline 30 Jun 2026). |

**Conservative defaults — KSA-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 15% (standard rate) |
| Unknown VAT status of a purchase | Not recoverable |
| Unknown counterparty location | Domestic KSA |
| Unknown business-use proportion (vehicle, phone) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (non-resident supplier) |
| Unknown blocked-input status (entertainment, motor vehicle, personal benefit) | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown GCC implementing state treatment | Treat as domestic 15% (transitional rules) |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | SAR 20,000 |
| HIGH tax-delta on a single conservative default | SAR 2,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | SAR 50,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full filing period. Acceptable from any Saudi business bank: Al Rajhi Bank, Saudi National Bank (SNB/NCB), Riyad Bank, Saudi British Bank (SABB), Banque Saudi Fransi (BSF), Arab National Bank (ANB), Alinma Bank, Bank AlJazira, Bank Albilad, or any other.

**Recommended** — sales invoices for the period (especially for zero-rated exports and international services), purchase invoices for any input tax claim above SAR 2,000, the client's TIN (15-digit, starting and ending with 3) in writing, Commercial Registration (CR) number.

**Ideal** — complete e-invoice register (from FATOORA system), VAT registration certificate, prior period VAT return, reconciliation of any excess input tax.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This VAT return was produced from bank statement alone. The reviewer must verify, before approval, that input tax claims above SAR 2,000 are supported by compliant e-invoices and that all reverse charge and zero-rating classifications match the supplier's/customer's documentation."

### KSA-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-SA-1 — Partial exemption with significant exempt supplies.** *Trigger:* client makes both taxable and exempt supplies and the exempt proportion is not trivial (more than incidental bank charges/interest). *Message:* "You make both taxable and exempt supplies. Your input tax must be apportioned under Article 50 of the VAT Law and IR Article 50. This skill cannot compute the apportionment ratio. Please engage a qualified tax consultant to determine and confirm the recovery rate before input tax is claimed."

**R-SA-2 — VAT group registration.** *Trigger:* client is part of a VAT group. *Message:* "VAT group registrations require consolidation across all group members. This skill covers single-entity VAT returns only. Please engage a qualified tax consultant."

**R-SA-3 — Oil and gas sector special rules.** *Trigger:* client operates in the oil and gas sector with specific VAT treatments for crude oil, refined products, or hydrocarbons. *Message:* "Oil and gas sector transactions have specific VAT rules including zero-rating conditions and reverse charge requirements that are highly fact-sensitive. Out of scope for this skill."

**R-SA-4 — Designated zone goods movement.** *Trigger:* client operates in a qualifying economic zone / designated zone and the transaction involves goods movement between zones or between a zone and the mainland. *Message:* "Designated zone goods movements have specific treatment under IR Article 39. Not all free zones are designated zones. This skill applies standard rules only. Please engage a qualified tax consultant to confirm zone treatment."

**R-SA-5 — Capital assets scheme adjustment.** *Trigger:* the period contains an adjustment to previously deducted input tax on a capital asset where input VAT exceeded SAR 250,000 (5-year adjustment for movable, 10-year for immovable). *Message:* "Capital assets scheme adjustments under IR Article 51 require tracking the original deduction, current and intended use, and computing the annual fraction. Out of scope for this skill."

**R-SA-6 — First supply of residential property (housing relief).** *Trigger:* client is selling residential property and claiming zero-rating under the SAR 1,000,000 housing relief cap. *Message:* "First supply of residential property with the SAR 1,000,000 housing VAT/RETT relief cap requires determining first-supply status, buyer eligibility (Saudi citizen, first home), and computing the relief. This is Tier 2 — flag for reviewer confirmation. If the transaction is straightforward, proceed with zero-rating in Field 5 up to SAR 1,000,000 and 15% on any excess, but the reviewer must verify eligibility."

**R-SA-7 — Deemed supplier for electronic marketplaces.** *Trigger:* client operates a digital platform facilitating sales by non-resident or unregistered suppliers (deemed supplier rules effective 1 January 2026 under amended IR Article 47 Para 3). *Message:* "Deemed supplier obligations for electronic marketplace operators require specific assessment. Out of scope."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific.

### 3.1 Saudi banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| AL RAJHI, ALRAJHI, مصرف الراجحي | EXCLUDE for bank charges/fees | Financial service, exempt |
| SNB, SAUDI NATIONAL BANK, NCB, البنك الأهلي | EXCLUDE for bank charges/fees | Same |
| RIYAD BANK, بنك الرياض | EXCLUDE for bank charges/fees | Same |
| SABB, SAUDI BRITISH BANK | EXCLUDE for bank charges/fees | Same |
| BSF, BANQUE SAUDI FRANSI | EXCLUDE for bank charges/fees | Same |
| ANB, ARAB NATIONAL BANK | EXCLUDE for bank charges/fees | Same |
| ALINMA, مصرف الإنماء | EXCLUDE for bank charges/fees | Same |
| BANK ALJAZIRA, بنك الجزيرة | EXCLUDE for bank charges/fees | Same |
| BANK ALBILAD, بنك البلاد | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE (fee lines) | EXCLUDE for transaction fees | Check for separate taxable subscription invoices |
| INTEREST, PROFIT, MURABAHA (margin) | EXCLUDE | Exempt financial service income/expense |
| LOAN, TAMWEEL, FINANCING (principal) | EXCLUDE | Loan/financing principal, out of scope |

### 3.2 Saudi government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| ZATCA, GAZT, هيئة الزكاة والضريبة والجمارك | EXCLUDE | Tax/zakat payment, not a supply |
| VAT PAYMENT, ضريبة القيمة المضافة | EXCLUDE | VAT payment |
| ZAKAT PAYMENT, زكاة | EXCLUDE | Zakat payment |
| CUSTOMS, جمارك | EXCLUDE for duty | Customs duty (but check for import VAT in Field 10/11) |
| GOSI, GENERAL ORGANIZATION FOR SOCIAL INSURANCE, التأمينات الاجتماعية | EXCLUDE | Social insurance, out of scope |
| MOC, MINISTRY OF COMMERCE, وزارة التجارة | EXCLUDE | Government fees, sovereign act |
| MOL, MINISTRY OF LABOR, HRSD | EXCLUDE | Government fees |
| MUNICIPALITY, BALADIYA, أمانة | EXCLUDE | Government fees |
| CITC, COMMUNICATIONS AND IT COMMISSION | EXCLUDE | Government licence fees |
| CMA, CAPITAL MARKET AUTHORITY | EXCLUDE | Regulatory fees |
| SADAD | EXCLUDE (payment channel) | Sadad is a bill payment system, not a supplier |
| ABSHER, MUQEEM, QIWA, MUDAD | EXCLUDE | Government digital platforms |

### 3.3 Saudi utilities

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| SEC, SAUDI ELECTRICITY COMPANY, الشركة السعودية للكهرباء | Domestic 15% | 8/9 | Electricity — overhead, input tax claimable |
| SWCC, SALINE WATER CONVERSION, المؤسسة العامة لتحلية المياه المالحة | Domestic 15% | 8/9 | Desalinated water |
| NATIONAL WATER COMPANY, NWC, شركة المياه الوطنية | Domestic 15% | 8/9 | Water services |
| MARAFIQ | Domestic 15% | 8/9 | Utilities (Jubail/Yanbu) |

### 3.4 Saudi telecoms

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| STC, SAUDI TELECOM, الاتصالات السعودية | Domestic 15% | 8/9 | Telecoms — overhead |
| MOBILY, ETIHAD ETISALAT, اتحاد اتصالات | Domestic 15% | 8/9 | Same |
| ZAIN, زين | Domestic 15% | 8/9 | Same |
| VIRGIN MOBILE KSA | Domestic 15% | 8/9 | MVNO |

### 3.5 Insurance (check type)

| Pattern | Treatment | Notes |
|---|---|---|
| TAWUNIYA, التعاونية | Check invoice | Life insurance/family takaful: exempt. General/motor/health: domestic 15% |
| BUPA ARABIA | Domestic 15% | Health insurance, standard rated |
| MEDGULF | Check invoice | Life: exempt. General: domestic 15% |
| MALATH, WALAA, AL RAJHI TAKAFUL | Check invoice | Life/family: exempt. General: domestic 15% |
| MOTOR INSURANCE, VEHICLE INSURANCE | Domestic 15% | General insurance standard rated (but input blocked if for blocked motor vehicle) |
| HEALTH INSURANCE, MEDICAL INSURANCE | Domestic 15% | Standard rated; input claimable unless employee personal benefit |

### 3.6 Transport

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| UBER SA, CAREEM KSA | Domestic 15% | 8/9 | Ride-hailing, standard rated |
| SAUDIA, SAUDI ARABIAN AIRLINES, الخطوط السعودية (international) | Zero-rated / EXCLUDE | 6 | International passenger transport |
| SAUDIA (domestic flights) | Domestic 15% | 8/9 or 1/2 | Domestic flights standard rated |
| FLYNAS, طيران ناس (international) | Zero-rated / EXCLUDE | 6 | International flights |
| FLYNAS (domestic) | Domestic 15% | 8/9 | Domestic flights standard rated |
| SAR, SAUDI RAILWAY, سار | Domestic 15% | 8/9 | Rail transport, standard rated |
| DHL KSA, ARAMEX KSA | Domestic 15% | 8/9 | Courier/express, standard rated |

### 3.7 Food retail and supermarkets

| Pattern | Treatment | Notes |
|---|---|---|
| PANDA, بنده | Default BLOCK input tax | Personal provisioning. Claimable only if F&B business purchasing stock-in-trade |
| CARREFOUR KSA, كارفور | Default BLOCK | Same |
| DANUBE, الدانوب | Default BLOCK | Same |
| TAMIMI MARKETS, التميمي | Default BLOCK | Same |
| OTHAIM, العثيم | Default BLOCK | Same |
| BIN DAWOOD, بن داود | Default BLOCK | Same |
| RESTAURANTS, CAFES (any named restaurant) | Default BLOCK | Entertainment blocked under IR Art. 49(4) |

### 3.8 SaaS — non-resident suppliers (reverse charge)

When the client receives services from a non-resident supplier not registered for KSA VAT: self-assess output VAT at 15% in Field 12/13 (reverse charge), claim input VAT (if entitled) in Field 9 or aggregated into Field 19. Net effect zero for fully taxable business.

| Pattern | Billing entity | Field | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) or Google LLC (US) | 12/13 | Non-resident, reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 12/13 | Non-resident, reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 12/13 | Non-resident, reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 12/13 | Non-resident, reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 12/13 | Non-resident, reverse charge |
| AWS, AMAZON WEB SERVICES | AWS Inc (US) or AWS EMEA SARL (LU) | 12/13 | Non-resident, reverse charge |
| NOTION | Notion Labs Inc (US) | 12/13 | Non-resident, reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 12/13 | Non-resident, reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 12/13 | Non-resident, reverse charge |
| GITHUB | GitHub Inc (US) | 12/13 | Non-resident, reverse charge |
| FIGMA | Figma Inc (US) | 12/13 | Non-resident, reverse charge |
| CANVA | Canva Pty Ltd (AU) | 12/13 | Non-resident, reverse charge |
| SLACK | Slack Technologies LLC (US) | 12/13 | Non-resident, reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Pty Ltd (AU) | 12/13 | Non-resident, reverse charge |
| ZOOM | Zoom Video Communications Inc (US) | 12/13 | Non-resident, reverse charge |
| HUBSPOT | HubSpot Inc (US) | 12/13 | Non-resident, reverse charge |
| STRIPE (subscription) | Stripe Inc (US) | 12/13 | Non-resident, reverse charge |
| SHOPIFY | Shopify Inc (CA) | 12/13 | Non-resident, reverse charge |
| TWILIO | Twilio Inc (US) | 12/13 | Non-resident, reverse charge |

### 3.9 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees, exempt financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| MADA, MADA PAYMENT | EXCLUDE | Debit card payment network fees — exempt financial service |
| HYPERPAY, MOYASAR, PAYFORT | Check invoice | If KSA entity: domestic 15%. If not: reverse charge |

### 3.10 Retail and office supplies (Saudi)

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| JARIR, مكتبة جرير | Domestic 15% | 8/9 | Office supplies, electronics — input claimable if business purpose |
| EXTRA, اكسترا | Domestic 15% | 8/9 | Electronics retail |
| IKEA KSA | Domestic 15% | 8/9 | Furniture/office |
| SACO, ساكو | Domestic 15% | 8/9 | Hardware/office supplies |

### 3.11 Professional services (Saudi)

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| LAW FIRM names, محاماة, LEGAL | Domestic 15% | 8/9 | Legal fees, input claimable if business purpose |
| ACCOUNTANT, AUDIT FIRM, محاسبة | Domestic 15% | 8/9 | Accounting/audit, always claimable |
| DELOITTE KSA, PwC KSA, KPMG KSA, EY KSA | Domestic 15% | 8/9 | Big 4 KSA entities, domestic |
| PRO SERVICES, TASHEEL, MUQEEM SERVICES | Domestic 15% | 8/9 | Government liaison services |

### 3.12 Payroll and statutory contributions (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| GOSI, SOCIAL INSURANCE | EXCLUDE | Social insurance contributions, out of scope |
| SALARY, WAGES, PAYROLL, WPS, رواتب | EXCLUDE | Employment, out of scope |
| IQAMA RENEWAL, VISA FEES | EXCLUDE | Government fees |
| END OF SERVICE, مكافأة نهاية الخدمة | EXCLUDE | Employment termination benefit |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| COMMERCIAL RENT, OFFICE RENT (with VAT invoice) | Domestic 15%, Field 8/9 | Commercial lease, input claimable |
| RESIDENTIAL RENT, APARTMENT RENT, إيجار سكني | EXCLUDE | Residential lease, exempt |
| EJAR, إيجار (residential) | EXCLUDE | Residential tenancy platform |
| WAREHOUSE, INDUSTRIAL RENT | Domestic 15%, Field 8/9 | Commercial/industrial lease |
| WAFI (residential off-plan sales platform) | See R-SA-6 | May involve first-supply housing relief |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL, BETWEEN ACCOUNTS | EXCLUDE | Internal movement |
| DIVIDEND, توزيعات | EXCLUDE | Dividend, out of scope |
| LOAN REPAYMENT, FINANCING REPAYMENT | EXCLUDE | Principal, out of scope |
| CASH WITHDRAWAL, ATM, سحب نقدي | TIER 2 — ask | Default exclude; ask what cash was spent on |
| PARTNER DRAWING, OWNER DRAWING | EXCLUDE | Drawing, out of scope |
| ZAKAT PAYMENT | EXCLUDE | Zakat, separate obligation from VAT |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a KSA-based self-employed IT consultant operating from Riyadh.

### Example 1 — Non-resident SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; SAR 60.00`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.8). No VAT on the invoice. This is a service received from a non-resident supplier not registered for KSA VAT. The client must self-assess reverse charge under Article 47: output VAT at 15% in Field 12/13, claim input VAT in Field 19 (via Field 9). Net effect zero for a fully taxable client. Both sides must appear on the return.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field (output) | Field (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -60.00 | -60.00 | 9.00 | 15% | 12/13 | 9 (via 19) | N | — | — |

### Example 2 — Zero-rated export of services

**Input line:**
`10.04.2026 ; TECHCORP INC DELAWARE ; CREDIT ; Invoice SA-2026-018 IT consultancy March ; +25,000.00 ; SAR`

**Reasoning:**
Incoming SAR 25,000 from a US company. The client provides IT consulting services to a non-resident with no KSA establishment. Under Article 33(2) and IR Article 33, this is a zero-rated export of services. Report in Field 6. No output VAT. Confirm: the customer has no establishment in KSA, the service is not related to goods or real estate in KSA.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | TECHCORP INC DELAWARE | +25,000.00 | +25,000.00 | 0 | 0% | 6 | Y | Q1 (HIGH) | "Verify customer has no KSA establishment" |

### Example 3 — Entertainment, blocked

**Input line:**
`15.04.2026 ; THE GLOBE RESTAURANT RIYADH ; DEBIT ; Client dinner ; -1,800.00 ; SAR`

**Reasoning:**
Restaurant transaction. Entertainment and hospitality expenses for non-business purposes are blocked under IR Article 49(4). Client entertainment is a hard block — the input VAT is irrecoverable. Default: full block.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | THE GLOBE RESTAURANT | -1,800.00 | -1,800.00 | 0 | — | — | Y | Q2 | "Entertainment: blocked under IR Art. 49(4)" |

### Example 4 — Domestic standard-rated purchase (office equipment)

**Input line:**
`18.04.2026 ; JARIR BOOKSTORE ; DEBIT ; Invoice JR-2026-441 Laptop HP ; -5,750.00 ; SAR`

**Reasoning:**
Jarir is a local retailer (Section 3.10). The gross amount is SAR 5,750 inclusive of 15% VAT. Net = 5,750 x (100/115) = SAR 5,000. VAT = SAR 750. Standard-rated domestic purchase used for business. Input tax claimable. Goes to Field 8 (purchases) and Field 9 (input tax).

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field (purchase) | Field (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | JARIR BOOKSTORE | -5,750.00 | -5,000.00 | -750.00 | 15% | 8 | 9 | N | — | — |

### Example 5 — Motor vehicle expense, blocked

**Input line:**
`22.04.2026 ; AL JAZIRAH VEHICLES ; DEBIT ; Monthly car lease ; -4,500.00 ; SAR`

**Reasoning:**
Car lease payment. Input VAT on motor vehicles (purchase, lease, running costs) is blocked under IR Article 49(3) unless the vehicle is essential to the business (taxi, delivery, car rental, transportation business). An IT consultant does not qualify. Default: full block.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | AL JAZIRAH VEHICLES | -4,500.00 | -4,500.00 | 0 | — | — | Y | Q3 | "Motor vehicle: blocked under IR Art. 49(3)" |

### Example 6 — Exempt financial service (bank charges)

**Input line:**
`28.04.2026 ; AL RAJHI BANK ; DEBIT ; Monthly account maintenance ; -50.00 ; SAR`

**Reasoning:**
Bank maintenance fee. Financial services based on interest or implicit margin are exempt under Article 29. No VAT is charged. No input tax to claim. Exclude from the return.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | AL RAJHI BANK | -50.00 | — | — | — | — | N | — | "Exempt financial service" |

---

## Section 5 — Tier 1 classification rules (compressed)

Each rule states the legal source and the field mapping. Apply silently if the data is unambiguous.

### 5.1 Standard rate 15% (VAT Law Art. 2; Royal Decree A/638)

Default rate for any taxable supply in KSA unless zero-rated or exempt. Sales go to Field 1/2. Purchases go to Field 8/9. The rate has been 15% since 1 July 2020. Do not apply the former 5% rate to supplies after that date (subject to transitional rules for pre-existing contracts entered before 11 May 2020).

### 5.2 Zero-rated supplies (Art. 33-37)

Exports of goods outside GCC implementing states with proof of export (customs declaration, bill of lading). Report in Field 6. Exports of services to non-resident outside KSA (no KSA establishment, service not related to goods/real estate in KSA). Report in Field 6. International transport of goods and passengers. Report in Field 6. Zero-rated domestic sales (qualifying medicines per SFDA list, investment metals 99%+ purity, supplies to diplomats). Report in Field 5. First supply of residential property within 3 years up to SAR 1,000,000 cap. Report in Field 5. No output VAT. Full input tax recovery on related costs.

### 5.3 Exempt supplies (Art. 29-30)

Financial services based on interest or implicit margin (lending, deposits, Islamic finance equivalents like murabaha profit margin). Residential rental. Life insurance premiums. Report in Field 7. No output VAT. No input tax recovery on directly attributable costs.

### 5.4 Out of scope

Salaries, wages, GOSI contributions, zakat, government fines/fees, dividends, loan principal, TOGC, government sovereign activities. Not reported on VAT return. Exclude entirely.

### 5.5 Reverse charge — services from non-resident (Art. 47)

When the client receives services or intangibles from a non-resident not registered for KSA VAT: self-assess output VAT at 15% in Field 12/13, claim input VAT in Field 19 (if entitled). Net effect zero for a fully taxable client. Both sides must appear.

### 5.6 Import of goods via Customs (Art. 47-49)

Goods imported and cleared at Customs. VAT paid at border. Report in Field 10 (value) and Field 11 (VAT). Input tax claimable in Field 19. Customs declaration is the supporting document.

### 5.7 Domestic purchases — standard rated

Input tax on a valid e-invoice from a KSA VAT-registered supplier is recoverable for purchases used in taxable business activity. Subject to blocked-input rules (5.9). Map to Field 8 (value) and Field 9 (input tax).

### 5.8 GCC implementing state supplies (Field 3/4)

Sales to customers in GCC implementing states (UAE, Bahrain, Oman) during transitional period: Field 3/4 at 15%. The GCC electronic service system for customs union is not yet fully operational — treat as domestic supply during transitional period.

### 5.9 Blocked input tax (IR Art. 49)

The following categories have zero VAT recovery:
- Motor vehicles: purchase, lease, running costs — IR Art. 49(3). Exception: vehicle is essential to the business (taxi, delivery fleet, car rental, transportation business).
- Entertainment, hospitality, recreation for non-business purposes — IR Art. 49(4). Exception: staff meals at workplace may be claimable.
- Employee personal benefits: housing, childcare (unless legally required) — IR Art. 49(5).
- Costs related to exempt supplies — Art. 46(1).

Blocked categories override any other recovery rule. Check blocked status before applying recovery.

### 5.10 E-invoicing compliance

All invoices must be electronic since 4 December 2021 (Phase 1). Phase 2 integration with FATOORA platform is rolling out in waves based on revenue thresholds. QR code is mandatory on all invoices in Phase 2 (and on simplified B2C invoices since Phase 1). A non-compliant invoice is still a valid invoice for VAT purposes but triggers penalties.

### 5.11 Credit notes and adjustments

Credit notes issued reduce output tax. Credit notes received reduce input tax. Enter in Field 16 (output adjustments) and Field 17 (input adjustments). For errors in prior returns: if VAT difference exceeds SAR 5,000, mandatory voluntary disclosure via ZATCA portal. If SAR 5,000 or less, correct in next return.

### 5.12 Penalty amnesty

ZATCA penalty cancellation initiative extended to 30 June 2026. Covers late registration, late filing, late payment, and correction penalties. Requires: taxpayer registered, all returns submitted, full principal tax paid.

### 5.13 Sales — domestic standard

Charge 15% on all local sales. Map to Field 1 (net) and Field 2 (output VAT).

### 5.14 Calculating VAT from gross amounts

```
Net = Gross / 1.15
VAT = Gross - Net  (or equivalently, Gross x 15/115)
```

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Motor vehicle vs commercial vehicle

*Pattern:* petrol station, parking, car rental, vehicle maintenance. *Why insufficient:* vehicle type unknown. Motor car expenses are blocked; vehicles essential to business (delivery fleet, taxi) may be claimable. *Default:* 0% recovery. *Question:* "Is this for a passenger car (blocked) or a vehicle essential to the business (delivery, transport)?"

### 6.2 Entertainment vs staff welfare

*Pattern:* restaurant, cafe, catering, event. *Why insufficient:* client entertainment is blocked; staff meals at workplace may be claimable. *Default:* block. *Question:* "Was this client entertainment (blocked) or a staff meal at the workplace?"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, AWS where the billing entity may be a KSA-registered entity or non-resident. *Default:* reverse charge (non-resident). *Question:* "Could you check the invoice for the legal entity name and TIN? If the supplier has a KSA TIN, this is domestic 15%; if not, reverse charge applies."

### 6.4 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit from a name matching the client's name. *Default:* exclude as owner injection. *Question:* "The SAR X transfer from [name] — is this a customer payment, your own money, or a loan?"

### 6.5 Incoming transfers from foreign counterparties

*Pattern:* foreign bank, foreign currency, international SWIFT. *Default:* domestic 15%. *Question:* "Was this a service to an overseas customer (potentially zero-rated)? Does the customer have a KSA establishment?"

### 6.6 Insurance type determination

*Pattern:* insurance premium payment to Tawuniya, MedGulf, etc. *Default:* exclude (exempt — life insurance default). *Question:* "Is this life/family takaful (exempt) or general/motor/health insurance (standard rated, input claimable)?"

### 6.7 Residential vs commercial property

*Pattern:* rent payment, Ejar platform. *Default:* residential (exempt). *Question:* "Is this a commercial property (VAT claimable with e-invoice) or residential (exempt)?"

### 6.8 Mixed-use phone, internet

*Pattern:* STC, Mobily, Zain personal lines. *Default:* 0% if mixed. *Question:* "Is this a dedicated business line or mixed-use? What business percentage?"

### 6.9 Cash withdrawals

*Pattern:* ATM, cash withdrawal. *Default:* exclude as owner drawing. *Question:* "What was the cash used for?"

### 6.10 Outgoing transfers to individuals

*Pattern:* outgoing to private-looking names. *Default:* exclude as salary/drawings. *Question:* "Was this a contractor payment (with e-invoice), salary, or personal transfer?"

### 6.11 GOSI deductions

*Pattern:* GOSI debit. *Default:* exclude (statutory, out of scope). No question needed.

### 6.12 Zakat vs VAT

*Pattern:* ZATCA payment that could be zakat or VAT. *Default:* exclude both — neither is a supply. *Question:* "Was this a VAT payment, a zakat payment, or both?"

---

## Section 7 — Excel working paper template (KSA-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the KSA-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Field code") accepts: 1, 5, 6, 7, 8, 10, 12, 14, 15, RC. Use blank for excluded transactions. For reverse-charge transactions, enter "RC" in column H.

### Sheet "Field Summary"

One row per field. Column A is the field number, column B is the description, column C is the value computed via formula.

```
Output:
| 1  | Standard-rated sales | =SUMIFS(Transactions!E:E, Transactions!H:H, "1") |
| 2  | VAT on standard-rated sales | =C[1_row]*0.15 |
| 5  | Zero-rated domestic sales | =SUMIFS(Transactions!E:E, Transactions!H:H, "5") |
| 6  | Exports | =SUMIFS(Transactions!E:E, Transactions!H:H, "6") |
| 7  | Exempt sales | =SUMIFS(Transactions!E:E, Transactions!H:H, "7") |
| 12 | Reverse charge imports | =SUMIFS(Transactions!E:E, Transactions!H:H, "RC") |
| 13 | VAT on reverse charge | =C[12_row]*0.15 |

Input:
| 8  | Standard-rated purchases | =SUMIFS(Transactions!E:E, Transactions!H:H, "8") |
| 9  | VAT on standard-rated purchases | =C[8_row]*0.15 |
| 10 | Imports at Customs | =SUMIFS(Transactions!E:E, Transactions!H:H, "10") |
| 11 | VAT paid at Customs | =C[10_row]*0.15 |
| 14 | Zero-rated purchases | =SUMIFS(Transactions!E:E, Transactions!H:H, "14") |
| 15 | Exempt purchases | =SUMIFS(Transactions!E:E, Transactions!H:H, "15") |

Totals:
| 18 | Total output VAT | =C[2_row]+C[13_row] |
| 19 | Total input VAT | =C[9_row]+C[11_row] |
| 20 | Net VAT due | =C[18_row]-C[19_row] |
```

### Sheet "Return Form"

```
Field 20 = Field 18 - Field 19

IF Field 20 > 0:
  VAT payable to ZATCA
ELSE:
  Excess input tax (refundable or carry forward)
```

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values, black for formulas, green for cross-sheet references, yellow background for rows where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/saudi-vat-<period>-working-paper.xlsx
```

---

## Section 8 — Saudi bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these KSA-specific patterns.

**Al Rajhi Bank statement format.** Al Rajhi online banking exports use CSV or Excel with DD/MM/YYYY (Gregorian) dates. Some statements also show Hijri dates. Common columns: Transaction Date, Description, Debit, Credit, Balance. The description field contains the counterparty name, sometimes in Arabic. SADAD bill payments show the biller name (e.g., "SADAD-STC", "SADAD-SEC"). SWIFT transfers show the beneficiary name separately.

**Saudi National Bank (SNB/NCB) statement format.** SNB exports use CSV with columns: Date, Description, Reference, Debit, Credit, Balance. Card purchases show the merchant name. Mada debit card payments show "MADA POS" followed by the merchant name. SWIFT transfers show the beneficiary bank and name.

**Riyad Bank statement format.** Riyad Bank online exports: Date, Narrative, Reference, Debit, Credit, Balance. The narrative field is the primary source for counterparty identification.

**Revolut / Wise Business.** ISO date format. Clear counterparty names. Separate fee lines — exclude fee lines (exempt financial service).

**Internal transfers and exclusions.** Own-account transfers between the client's banks. Labelled "transfer between accounts", "internal", "حوالة داخلية". Always exclude.

**WPS (Wage Protection System) entries.** Salary payments via WPS appear as "WPS", "SALARY TRANSFER", "رواتب", or individual employee names. Always exclude — employment, out of scope.

**SADAD entries.** SADAD is the national bill payment system. SADAD debits show the biller name (e.g., "SADAD-STC" = STC telecom bill, "SADAD-SEC" = electricity bill). Map to the appropriate category using Section 3 based on the biller name after the "SADAD-" prefix.

**Mada entries.** Mada is the national debit card network. Entries show "MADA" or "MADA POS" followed by the merchant name and city. The merchant name is the key for counterparty identification.

**Arabic language descriptions.** Some bank statement descriptions appear in Arabic. Common terms: مشتريات (purchases), مبيعات (sales), رواتب (salaries), إيجار (rent), كهرباء (electricity), مياه (water), اتصالات (telecom). Treat as the English equivalent.

**Foreign currency transactions.** Convert to SAR at the Saudi Central Bank (SAMA) exchange rate on the transaction date. Note the rate in column L (Notes). SAR is pegged to USD at approximately 3.75.

**GOSI entries.** GOSI (General Organization for Social Insurance) debits are statutory employer/employee contributions. Always out of scope. Exclude immediately.

**Zakat and tax entries.** ZATCA debits may be VAT payments, zakat payments, or both. Both are government payments, not supplies. Exclude. Do not confuse a VAT payment with a VAT-inclusive purchase.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type and trading name
*Inference rule:* "مؤسسة" (mu'assasa) = sole establishment; "شركة ذات مسؤولية محدودة" or "LLC" = limited liability company. *Fallback question:* "Are you a sole establishment, LLC, or other entity type?"

### 9.2 TIN and CR number
*Inference rule:* TIN may appear on e-invoices. CR number may appear on bank statement header. *Fallback question:* "What is your VAT TIN (15-digit, starts and ends with 3)? What is your CR number?"

### 9.3 Filing period and frequency
*Inference rule:* first and last transaction dates. Monthly if revenue > SAR 40M, otherwise quarterly. *Fallback question:* "Which period does this cover? Monthly (which month) or quarterly (Q1/Q2/Q3/Q4)?"

### 9.4 Industry and sector
*Inference rule:* counterparty mix, sales patterns. *Fallback question:* "In one sentence, what does the business do?"

### 9.5 Employees
*Inference rule:* WPS, GOSI, salary transfers. *Fallback question:* "Do you have employees?"

### 9.6 Exempt supplies
*Inference rule:* residential rental income, financial service income. *Fallback question:* "Do you make any VAT-exempt sales (residential rental, financial services, life insurance)?" *If yes and significant, R-SA-1 may fire.*

### 9.7 International customers
*Inference rule:* foreign bank credits, SWIFT inflows. *Fallback question:* "Do you have customers outside KSA? Are they businesses? Do any have a KSA establishment?"

### 9.8 E-invoicing phase
*Inference rule:* ZATCA wave notifications based on revenue. *Fallback question:* "Are you in Phase 2 of e-invoicing (integrated with FATOORA)? If not, which wave are you assigned to?"

### 9.9 Carried-forward excess input tax
*Inference rule:* not inferable from a single period. Always ask. *Question:* "Do you have any excess input tax carried forward from the previous period?"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the Malta v2.0 structure. It supersedes v1.0/v1.1.

### Sources

**Primary legislation:**
1. VAT Law (Royal Decree No. A/113, dated 2/11/1438H) — Articles 2, 9, 29-37, 46-51, 59-60, 62, 64
2. VAT Implementing Regulations (Board of Directors Resolution No. 3839) — Articles 7-10, 29-37, 39, 46-51, 53-54, 59, 62-63
3. E-Invoicing Regulation (issued 4/12/1442H)
4. Royal Decree A/638 (rate increase to 15%)
5. Royal Decree A/84 (housing VAT/RETT relief)
6. Unified VAT Agreement for the GCC States
7. Board Resolution No. 01-06-24 (April 2025 IR amendments)

**ZATCA guidance:**
8. ZATCA VAT return completion guide
9. ZATCA e-invoicing implementation guides (Phase 1, Phase 2)
10. ZATCA penalty waiver initiative guidance

**Other:**
11. ZATCA portal — https://zatca.gov.sa
12. FATOORA e-invoicing platform
13. SAMA exchange rates

### Known gaps

1. The supplier pattern library covers the most common Saudi and international counterparties but does not cover every local business.
2. The worked examples are drawn from a hypothetical IT consultant in Riyadh. They do not cover construction, oil & gas, real estate, or F&B specifically.
3. GCC inter-state supply rules (transitional provisions) are simplified — the GCC electronic service system is not yet fully operational.
4. The housing relief (first residential property, SAR 1,000,000 cap) is referred to R-SA-6 for reviewer confirmation rather than fully deterministic.
5. Real Estate Transaction Tax (RETT) at 5% for exempt real estate is referenced but not computed.
6. The deemed supplier rules for electronic marketplaces (effective 1 January 2026) are refused (R-SA-7) rather than handled.
7. Arabic-language patterns in the supplier library are limited to major brands — more Arabic variants should be added.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with Malta v2.0 structure. Quick reference with field table, e-invoicing phases summary, and conservative defaults at top (Section 1). Supplier pattern library with Saudi vendors (Al Rajhi, SNB, Riyad Bank, STC, Mobily, SEC, SWCC, Panda/Carrefour, Jarir, SAUDIA, ZATCA) in Section 3. Six worked examples (Section 4). Compressed Tier 1 rules (Section 5). Tier 2 catalogue (Section 6). Excel working paper (Section 7). Saudi bank statement guide with Al Rajhi/SNB formats, SADAD/Mada patterns, Arabic descriptions (Section 8). Onboarding fallback (Section 9). References (Section 10).
- **v1.1 (April 2026):** Updated with April 2025 IR amendments, penalty amnesty extension, e-invoicing wave 24.
- **v1.0 (April 2026):** Initial standalone skill covering VAT Law, field mappings, reverse charge, blocked categories, e-invoicing, registration, penalties.

### Self-check (v2.0 of this document)

1. Quick reference at top with field table and conservative defaults: yes (Section 1).
2. E-invoicing phases summary in quick reference: yes (Section 1).
3. Supplier library as literal lookup tables: yes (Section 3, 14 sub-tables).
4. Worked examples: yes (Section 4, 6 examples).
5. Tier 1 rules compressed: yes (Section 5, 14 rules).
6. Tier 2 catalogue compressed: yes (Section 6, 12 items).
7. Excel template specification with mandatory recalc: yes (Section 7).
8. Onboarding as fallback only: yes (Section 9, 9 items).
9. All 7 KSA-specific refusals present: yes (Section 2, R-SA-1 through R-SA-7).
10. Reference material at bottom: yes (Section 10).
11. Entertainment block explicit: yes (Section 5.9 + Example 3).
12. Motor vehicle block explicit: yes (Section 5.9 + Example 5).
13. Reverse charge for non-resident services explicit: yes (Example 1 + Section 5.5).
14. Zero-rated export and "no KSA establishment" test explicit: yes (Example 2 + Section 5.2).
15. Al Rajhi/SNB bank statement format guide with SADAD/Mada patterns: yes (Section 8).
16. Arabic language descriptions covered: yes (Section 8).
17. Penalty amnesty referenced: yes (Section 5.12).

## End of Saudi Arabia VAT Return Skill v2.0

This skill is incomplete without the companion file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a VAT return without both files loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax consultant, CPA, or equivalent practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
