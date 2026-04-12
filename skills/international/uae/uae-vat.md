---
name: uae-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a UAE VAT return (VAT201 form) for any client. Trigger on phrases like "prepare VAT return", "do the VAT", "fill in VAT201", "create the return", "UAE VAT filing", "FTA return", or any request involving UAE VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers the UAE only and only standard VAT-registered persons filing VAT201. VAT groups, profit margin schemes, partial exemption with non-trivial exempt supplies, and Designated Zone goods movement classifications are all in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any UAE VAT work.
version: 2.0
---

# UAE VAT Return Skill (VAT201) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

| Field | Value |
|---|---|
| Country | United Arab Emirates |
| Standard rate | 5% |
| Zero rate | 0% (exports, international transport, first residential property within 3 years, qualifying education, qualifying healthcare, investment precious metals 99%+ purity, crude oil and natural gas) |
| Exempt supplies | Financial services (interest/margin-based), residential property resale/lease after first supply, bare land, local passenger transport, life insurance |
| Return form | VAT201 (filed via FTA e-Services portal) |
| Filing portal | https://eservices.tax.gov.ae (FTA e-Services Portal) — electronic only |
| Authority | Federal Tax Authority (FTA), United Arab Emirates |
| Currency | AED only |
| Filing frequency | Quarterly (default, annual turnover < AED 150M); Monthly (assigned by FTA, turnover >= AED 150M) |
| Deadline | 28th day of the month following end of tax period |
| VAT introduction date | 1 January 2018 |
| TRN format | 15-digit numeric |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Registry |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |

**Key VAT201 boxes/fields (the fields you will use most):**

| Field | Meaning |
|---|---|
| 1 (1a–1g) | Standard-rated supplies, broken down by Emirate (Abu Dhabi, Dubai, Sharjah, Ajman, UAQ, RAK, Fujairah) — net value + 5% VAT |
| 2 | Tax refunds provided to tourists (Tourist Refund Scheme) |
| 3 | Supplies subject to reverse charge — value of taxable supplies received from non-resident suppliers + 5% VAT |
| 4 | Zero-rated supplies — net value |
| 5 | Exempt supplies — net value |
| 6 | Goods imported into the UAE — CIF value + 5% VAT |
| 7 | Adjustments to output tax (credit notes, corrections, bad debt relief) |
| 8 | Total output tax due (derived: VAT on Box 1 + Box 2 + VAT on Box 3 + VAT on Box 6 + Box 7) |
| 9 | Standard-rated expenses — net value + 5% VAT |
| 10 | Reverse charge input tax — VAT recoverable on reverse charge supplies from Box 3 |
| 11 | Total recoverable input tax (derived: VAT on Box 9 + Box 10 − blocked input tax adjustments) |

**Net VAT payable = Box 8 − Box 11. Positive = payable to FTA. Negative = refundable or carried forward.**

**Conservative defaults — UAE-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 5% (standard rate) |
| Unknown VAT status of a purchase | Not recoverable |
| Unknown counterparty location | Domestic UAE |
| Unknown Emirate for Box 1 breakdown | Flag for reviewer — Emirate must be determined |
| Unknown business-use proportion (vehicle, phone) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge (non-resident supplier) |
| Unknown blocked-input status (entertainment, motor vehicle, personal benefit) | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown Designated Zone involvement | Treat as mainland (standard VAT rules) |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | AED 20,000 |
| HIGH tax-delta on a single conservative default | AED 1,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | AED 25,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the quarter in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any UAE business bank: Emirates NBD, First Abu Dhabi Bank (FAB), Abu Dhabi Commercial Bank (ADCB), Mashreq Bank, Dubai Islamic Bank, RAKBANK, Commercial Bank of Dubai, HSBC UAE, Standard Chartered UAE, Citibank UAE, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices for the period (especially for zero-rated supplies and exports), purchase invoices for any input tax claim above AED 1,000, the client's TRN (15-digit number) in writing, and the Emirate of the client's establishment.

**Ideal** — complete invoice register, VAT registration certificate from FTA, prior period VAT201, reconciliation of any excess input tax carried forward.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This VAT201 was produced from bank statement alone. The reviewer must verify, before approval, that input tax claims above AED 1,000 are supported by valid tax invoices, that all reverse charge and zero-rating classifications match the supplier's/customer's documentation, and that the Emirate breakdown in Box 1 is correct."

### UAE-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-AE-1 — Partial exemption with significant exempt supplies.** *Trigger:* client makes both taxable and exempt supplies and the exempt proportion is not trivial (more than incidental bank charges/interest). *Message:* "You make both taxable and exempt supplies. Your input tax must be apportioned under Articles 55-56 of the VAT Decree-Law. This skill cannot compute the apportionment ratio. Please engage a registered tax agent to determine and confirm the recovery rate before input tax is claimed."

**R-AE-2 — VAT group registration.** *Trigger:* client is part of a VAT group (Tax Group). *Message:* "VAT group registrations require consolidation across all group members and disregard of intra-group supplies. This skill covers single-entity VAT201 returns only. Please engage a registered tax agent."

**R-AE-3 — Designated Zone goods movement classification.** *Trigger:* client operates in a Designated Zone and the transaction involves movement of goods between Designated Zones, or from a Designated Zone to mainland, or vice versa. *Message:* "Designated Zone goods movements have specific import/export treatment under Article 51 of the VAT Decree-Law. The classification depends on the specific zone's designation status and the direction of movement. This skill applies standard mainland rules only. Please engage a registered tax agent to confirm the Designated Zone treatment."

**R-AE-4 — Profit margin scheme.** *Trigger:* client deals in second-hand goods, art, or collectables under the profit margin scheme. *Message:* "Profit margin scheme transactions require transaction-level margin computation under Article 29 of the Executive Regulation. Out of scope."

**R-AE-5 — Capital assets scheme adjustment.** *Trigger:* the period contains an adjustment to previously deducted input tax on a capital asset under Article 57 (assets exceeding AED 5,000,000 for buildings or 5-year useful life for other assets). *Message:* "Capital assets scheme adjustments are too fact-sensitive for this skill. They require tracking the original deduction, current use, and computing the annual fraction over 10 years (buildings) or 5 years (other assets). Please engage a registered tax agent."

**R-AE-6 — Concerned goods (hydrocarbons) reverse charge.** *Trigger:* client supplies or acquires crude oil, refined petroleum products, hydrocarbons, or natural gas between VAT-registered persons under Article 48(2). *Message:* "Concerned goods reverse charge under Cabinet Decision No. 25 of 2018 has specific reporting requirements. Out of scope."

**R-AE-7 — Tourist Refund Scheme operator.** *Trigger:* client is a retailer or central refund agency operating the Tourist Refund Scheme and needs to report Box 2 amounts. *Message:* "Tourist Refund Scheme reporting requires specific Box 2 entries from approved operator reports (Planet/Fintrax). This skill does not compute TRS amounts. Obtain the operator report and enter Box 2 directly."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific.

### 3.1 UAE banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| EMIRATES NBD, ENBD | EXCLUDE for bank charges/fees | Financial service, exempt |
| FAB, FIRST ABU DHABI BANK, NBAD | EXCLUDE for bank charges/fees | Same |
| ADCB, ABU DHABI COMMERCIAL BANK | EXCLUDE for bank charges/fees | Same |
| MASHREQ, MASHREQBANK | EXCLUDE for bank charges/fees | Same |
| DUBAI ISLAMIC BANK, DIB | EXCLUDE for bank charges/fees | Same |
| RAKBANK, NATIONAL BANK OF RAK | EXCLUDE for bank charges/fees | Same |
| CBD, COMMERCIAL BANK OF DUBAI | EXCLUDE for bank charges/fees | Same |
| HSBC UAE, HSBC MIDDLE EAST | EXCLUDE for bank charges/fees | Same |
| STANDARD CHARTERED UAE | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, PROFIT RATE, MURABAHA | EXCLUDE | Interest/profit income/expense, exempt financial service |
| LOAN, FINANCING, IJARA (principal) | EXCLUDE | Loan/financing principal movement, out of scope |

### 3.2 UAE government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| FTA, FEDERAL TAX AUTHORITY | EXCLUDE | Tax payment, not a supply |
| VAT PAYMENT, TAX PAYMENT | EXCLUDE | VAT/tax payment |
| ZATCA (if cross-border payment to Saudi authority) | EXCLUDE | Foreign tax payment |
| CUSTOMS, DUBAI CUSTOMS, ABU DHABI CUSTOMS | EXCLUDE for customs duty | Customs duty is not VAT (but check for import VAT in Box 6) |
| DED, DEPARTMENT OF ECONOMIC DEVELOPMENT | EXCLUDE | Trade licence fees, government sovereign act |
| DMCC, DAFZA, JAFZA, SAIF ZONE (licence fees) | EXCLUDE | Free zone authority fees, government |
| DIFC, ADGM | EXCLUDE for registration/licence fees | Financial centre authority fees |
| MOHRE, MINISTRY OF HUMAN RESOURCES | EXCLUDE | Government labour fees |
| IMMIGRATION, GDRFA | EXCLUDE | Visa/immigration fees |
| MUNICIPALITY, BALADIYA | EXCLUDE | Government fees |
| RTA, ROADS AND TRANSPORT AUTHORITY | EXCLUDE | Government fees (Salik tolls are out of scope) |

### 3.3 UAE utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| DEWA, DUBAI ELECTRICITY AND WATER | Domestic 5% | 9 | Electricity and water — overhead, input tax claimable |
| ADDC, ABU DHABI DISTRIBUTION COMPANY | Domestic 5% | 9 | Same |
| SEWA, SHARJAH ELECTRICITY AND WATER | Domestic 5% | 9 | Same |
| FEWA, FEDERAL ELECTRICITY AND WATER | Domestic 5% | 9 | Same (covers Ajman, UAQ, Fujairah) |
| AADC, AL AIN DISTRIBUTION COMPANY | Domestic 5% | 9 | Same |
| DISTRICT COOLING, EMPOWER, TABREED | Domestic 5% | 9 | District cooling services |

### 3.4 UAE telecoms

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| DU, EMIRATES INTEGRATED TELECOM, EITC | Domestic 5% | 9 | Telecoms/broadband — overhead |
| ETISALAT, E&, EMIRATES TELECOM | Domestic 5% | 9 | Same |
| VIRGIN MOBILE UAE | Domestic 5% | 9 | MVNO telecoms |

### 3.5 Insurance (check type)

| Pattern | Treatment | Notes |
|---|---|---|
| LIFE INSURANCE, METLIFE, ZURICH LIFE | EXCLUDE | Life insurance exempt |
| SALAMA, TAKAFUL, ISLAMIC INSURANCE (life) | EXCLUDE | Life/family takaful exempt |
| MOTOR INSURANCE, VEHICLE INSURANCE | Domestic 5% | General insurance is standard-rated, input claimable (unless for blocked motor vehicle) |
| HEALTH INSURANCE, MEDICAL INSURANCE | Domestic 5% | Standard-rated; input claimable unless employee personal benefit |
| PROPERTY INSURANCE, FIRE INSURANCE | Domestic 5% | Standard-rated, input claimable |
| OMAN INSURANCE, AXA GULF, RSA (general) | Domestic 5% | General insurance standard-rated |

### 3.6 Transport

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| CAREEM, UBER UAE | Domestic 5% | 9 | Ride-hailing, standard rated |
| RTA TAXI, DUBAI TAXI, ABU DHABI TAXI | EXCLUDE | Local passenger transport, exempt |
| METRO, TRAM, BUS (RTA public transport) | EXCLUDE | Local passenger transport, exempt |
| SALIK, TOLL | EXCLUDE | Road toll, government fee |
| EMIRATES (airline, international) | Zero-rated / EXCLUDE | International passenger transport zero-rated |
| FLY DUBAI, FLYDUBAI | Zero-rated / EXCLUDE | International flights |
| ETIHAD AIRWAYS | Zero-rated / EXCLUDE | International flights |
| AIR ARABIA | Zero-rated / EXCLUDE | International flights |
| DHL EXPRESS UAE, ARAMEX | Domestic 5% | 9 | Courier/express, standard rated |
| DHL INTERNATIONAL | Reverse charge | 3/10 | Non-resident supplier — check invoice entity |

### 3.7 Food retail and supermarkets

| Pattern | Treatment | Notes |
|---|---|---|
| CARREFOUR, CARREFOUR UAE, MAF | Default BLOCK input tax | Personal provisioning. Claimable only if F&B/hospitality business purchasing stock-in-trade |
| LULU, LULU HYPERMARKET | Default BLOCK | Same |
| SPINNEYS, WAITROSE UAE | Default BLOCK | Same |
| CHOITHRAMS | Default BLOCK | Same |
| NOON DAILY, NOON.COM (grocery) | Default BLOCK | Same |
| RESTAURANTS, CAFES (any named restaurant) | Default BLOCK | Entertainment blocked under Exec. Reg. Art. 53(1)(a) |

### 3.8 SaaS — non-resident suppliers (reverse charge)

When the client receives services from a non-resident supplier who is not VAT-registered in UAE: report in Box 3 (value + 5% VAT output side), claim input in Box 10 (if entitled). Net effect zero for fully taxable business.

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) or Google LLC (US) | 3/10 | Non-resident, reverse charge |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | 3/10 | Non-resident, reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | 3/10 | Non-resident, reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | 3/10 | Non-resident, reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | 3/10 | Non-resident, reverse charge |
| AWS, AMAZON WEB SERVICES | AWS Inc (US) or AWS EMEA SARL (LU) | 3/10 | Non-resident, reverse charge |
| NOTION | Notion Labs Inc (US) | 3/10 | Non-resident, reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | 3/10 | Non-resident, reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | 3/10 | Non-resident, reverse charge |
| GITHUB | GitHub Inc (US) | 3/10 | Non-resident, reverse charge |
| FIGMA | Figma Inc (US) | 3/10 | Non-resident, reverse charge |
| CANVA | Canva Pty Ltd (AU) | 3/10 | Non-resident, reverse charge |
| SLACK | Slack Technologies LLC (US) | 3/10 | Non-resident, reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Pty Ltd (AU) | 3/10 | Non-resident, reverse charge |
| ZOOM | Zoom Video Communications Inc (US) | 3/10 | Non-resident, reverse charge |
| HUBSPOT | HubSpot Inc (US) | 3/10 | Non-resident, reverse charge |
| STRIPE (subscription) | Stripe Inc (US) | 3/10 | Non-resident, reverse charge |
| SHOPIFY | Shopify Inc (CA) | 3/10 | Non-resident, reverse charge |
| TWILIO | Twilio Inc (US) | 3/10 | Non-resident, reverse charge |

### 3.9 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees, exempt financial service |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| TELR, NETWORK INTERNATIONAL, PAYFORT (AMAZON PAYMENT SERVICES) | Check invoice | If UAE entity: domestic 5%. Fees may be exempt financial service |

### 3.10 Freezone suppliers

| Pattern | Treatment | Notes |
|---|---|---|
| Supplier in Designated Zone (goods) | See R-AE-3 — may trigger refusal | Goods from Designated Zone to mainland = import (Box 6) |
| Supplier in Designated Zone (services) | Domestic 5%, Box 9 | Services in/from Designated Zones follow standard VAT rules |
| Supplier in non-Designated free zone | Domestic 5%, Box 9 | Non-designated free zones follow standard UAE VAT rules for all supplies |

### 3.11 E-commerce and retail platforms

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| NOON, NOON.COM | Domestic 5% | 9 | UAE marketplace, standard rated |
| AMAZON.AE, SOUQ.COM | Domestic 5% | 9 | UAE marketplace |
| NAMSHI | Domestic 5% | 9 | Fashion retail |

### 3.12 Professional services (UAE)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| LAW FIRM names, ADVOCATES, LEGAL | Domestic 5% | 9 | Legal fees, input claimable if business purpose |
| ACCOUNTANT, AUDIT FIRM, CPA | Domestic 5% | 9 | Accounting/audit, always claimable |
| PRO SERVICES, TYPING CENTRE | Domestic 5% | 9 | Government liaison services |
| NOTARY, NOTARIZATION | Domestic 5% | 9 | Notarial services |

### 3.13 Payroll and employee costs (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES, PAYROLL, WPS | EXCLUDE | Employment, out of scope |
| END OF SERVICE, GRATUITY, EOSB | EXCLUDE | Employment termination benefit, out of scope |
| VISA FEES, LABOUR CARD | EXCLUDE | Government fees |
| HEALTH INSURANCE (employee mandatory) | Domestic 5% | Mandatory employee health insurance is standard rated and input claimable |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| COMMERCIAL RENT, OFFICE RENT (with VAT invoice) | Domestic 5%, Box 9 | Commercial property lease, input claimable |
| RESIDENTIAL RENT, APARTMENT RENT | EXCLUDE | Residential lease, exempt |
| EJARI, TAWTHEEQ (residential) | EXCLUDE | Residential tenancy registration |
| WAREHOUSE, INDUSTRIAL RENT | Domestic 5%, Box 9 | Commercial/industrial lease, standard rated |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| OWN TRANSFER, INTERNAL, BETWEEN ACCOUNTS | EXCLUDE | Internal movement |
| DIVIDEND, DIV PAYMENT | EXCLUDE | Dividend, out of scope |
| LOAN REPAYMENT, FINANCING REPAYMENT | EXCLUDE | Principal, out of scope |
| CASH WITHDRAWAL, ATM | TIER 2 — ask | Default exclude; ask what cash was spent on |
| PARTNER DRAWING, OWNER DRAWING | EXCLUDE | Drawing, out of scope |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a UAE-based self-employed IT consultant operating from Dubai.

### Example 1 — Non-resident SaaS reverse charge (Notion)

**Input line:**
`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; AED 58.72`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.8). No VAT on the invoice. This is a service received from a non-resident supplier not registered for UAE VAT. The client must self-assess reverse charge under Article 48: output VAT at 5% in Box 3/Box 8, input VAT in Box 10/Box 11. Net effect zero for a fully taxable client.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (output) | Box (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2026 | NOTION LABS INC | -58.72 | -58.72 | 2.94 | 5% | 3 / 8 | 10 / 11 | N | — | — |

### Example 2 — Zero-rated export of services

**Input line:**
`10.04.2026 ; TECHCORP LLC DELAWARE ; CREDIT ; Invoice UAE-2026-018 IT consultancy March ; +18,000.00 ; AED`

**Reasoning:**
Incoming AED 18,000 from a US company. The client provides IT consulting services to a non-resident customer with no UAE establishment. Under Article 31(1)(a) and Article 45, this is a zero-rated export of services. Report in Box 4. No output VAT. Confirm: the customer has no place of residence in the UAE.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | TECHCORP LLC DELAWARE | +18,000.00 | +18,000.00 | 0 | 0% | 4 | Y | Q1 (HIGH) | "Verify customer has no UAE establishment" |

### Example 3 — Entertainment, blocked

**Input line:**
`15.04.2026 ; PIERCHIC RESTAURANT DUBAI ; DEBIT ; Client dinner ; -1,200.00 ; AED`

**Reasoning:**
Restaurant transaction. Client entertainment is blocked under Executive Regulation Article 53(1)(a). Unlike staff meals at the workplace (which may be claimable), client entertainment is a hard block. The input VAT is irrecoverable. Default: full block. No input tax recovery.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | PIERCHIC RESTAURANT | -1,200.00 | -1,200.00 | 0 | — | — | Y | Q2 | "Entertainment: blocked under Art. 53(1)(a)" |

### Example 4 — Domestic standard-rated purchase (office equipment)

**Input line:**
`18.04.2026 ; SHARAF DG ELECTRONICS ; DEBIT ; Invoice SH-2026-441 Laptop Dell ; -4,200.00 ; AED`

**Reasoning:**
Sharaf DG is a UAE retailer. The gross amount is AED 4,200 inclusive of 5% VAT. Net = 4,200 x (100/105) = AED 4,000. VAT = AED 200. Standard-rated domestic purchase used for business. Input tax claimable. Goes to Box 9 (purchases) and Box 11 (input tax).

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (purchase) | Box (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | SHARAF DG ELECTRONICS | -4,200.00 | -4,000.00 | -200.00 | 5% | 9 | 11 | N | — | — |

### Example 5 — Motor vehicle expense, blocked

**Input line:**
`22.04.2026 ; HERTZ UAE ; DEBIT ; Monthly car rental ; -3,500.00 ; AED`

**Reasoning:**
Car rental payment. Input VAT on motor vehicles (purchase, rental, lease, and running costs) is blocked under Executive Regulation Article 53(1)(b). The exceptions are: vehicle is stock-in-trade (car dealership), used for licensed taxi service, used for a vehicle rental business (where renting is the business), or designed exclusively for business goods transport. An IT consultant does not qualify. Default: full block.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | HERTZ UAE | -3,500.00 | -3,500.00 | 0 | — | — | Y | Q3 | "Motor vehicle: blocked under Art. 53(1)(b)" |

### Example 6 — Residential rent (exempt, excluded)

**Input line:**
`01.04.2026 ; EMAAR PROPERTIES ; DEBIT ; April apartment rent ; -8,000.00 ; AED`

**Reasoning:**
Residential apartment rent. Residential property lease is exempt under Article 46(2). No VAT is charged. No input tax to claim. Exclude from the return entirely.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 01.04.2026 | EMAAR PROPERTIES | -8,000.00 | — | — | — | — | N | — | "Residential rent: exempt" |

---

## Section 5 — Tier 1 classification rules (compressed)

Each rule states the legal source and the box mapping. Apply silently if the data is unambiguous.

### 5.1 Standard rate 5% (VAT Decree-Law Art. 2, 5)

Default rate for any taxable supply in the UAE unless zero-rated or exempt. Sales go to Box 1 (with Emirate breakdown 1a–1g). Output tax goes to Box 8. Purchases go to Box 9. Input tax goes to Box 11.

### 5.2 Zero-rated supplies (Art. 45)

Exports of goods outside UAE with proof of export (customs declaration, bill of lading). Exports of services to non-resident with no UAE establishment. International passenger/freight transport. First supply of residential property within 3 years of completion. Qualifying education and healthcare from recognised/licensed providers. Investment precious metals (99%+ purity). Crude oil and natural gas. All go to Box 4. No output VAT. Full input tax recovery on related costs.

### 5.3 Exempt supplies (Art. 46)

Financial services based on interest or implicit margin (lending, deposits, Islamic finance equivalents). Residential property resale/lease after first supply. Bare (undeveloped) land. Local passenger transport (taxis, buses, metro within UAE — not limousine/luxury hire). Life insurance and reinsurance. Go to Box 5. No output VAT. No input tax recovery on directly attributable costs.

### 5.4 Out of scope

Salaries, wages, end-of-service gratuity, dividends, government fines/penalties, loan principal, TOGC, Salik tolls, government licence fees. Not reported on VAT201. Exclude entirely.

### 5.5 Reverse charge — services from non-resident (Art. 48)

When the client receives services from a non-resident supplier who does not have a place of residence in UAE and is not UAE VAT-registered: self-assess output VAT at 5% in Box 3, claim input tax in Box 10 (if entitled). Net effect zero for a fully taxable client.

### 5.6 Reverse charge — import of goods (Art. 47-49)

Goods imported via customs: VAT paid at border (or deferred under customs scheme). Report in Box 6 (value + VAT). Input tax claimable in Box 11. Customs declaration is the supporting document.

### 5.7 Domestic purchases — standard rated

Input tax on a valid tax invoice from a UAE VAT-registered supplier is recoverable for purchases used in taxable business activity. Subject to blocked-input rules (5.9). Map to Box 9 (value) and Box 11 (input tax).

### 5.8 Box 1 Emirate breakdown

Goods: allocate to the Emirate where goods are delivered or made available. Services: allocate to the Emirate where the supplier's establishment providing the service is located. If multiple establishments, allocate to the most directly concerned. Each sub-box (1a–1g) carries its own net value and VAT column.

### 5.9 Blocked input tax (Exec. Reg. Art. 53)

The following categories have zero VAT recovery:
- Entertainment, hospitality, and recreation for non-business purposes — Art. 53(1)(a). Exception: staff meals at the workplace are claimable.
- Motor vehicles: purchase, hire, lease, and running costs (fuel, maintenance, insurance) — Art. 53(1)(b). Exceptions: stock-in-trade (car dealership), licensed taxi service, vehicle rental business, vehicles designed exclusively for business goods transport, emergency vehicles.
- Employee personal benefits: gym, personal phone, personal accommodation (unless required by law) — Art. 53(1)(c).

Blocked categories override any other recovery rule. Check blocked status before applying recovery.

### 5.10 Free samples and gifts

Gifts not exceeding AED 500 per recipient per year: no deemed supply. Above AED 500: deemed supply, output VAT at 5% due on cost. Report in Box 1.

### 5.11 Credit notes and adjustments

Credit notes issued reduce output tax. Credit notes received reduce input tax. Enter in Box 7 (adjustments to output tax). For errors in prior returns: if tax difference exceeds AED 10,000, mandatory Voluntary Disclosure. If AED 10,000 or less, adjust in next return.

### 5.12 Sales — domestic standard

Charge 5% on all local sales of goods and services. Map to Box 1 (with Emirate breakdown) and Box 8 (output tax).

### 5.13 Sales — zero-rated exports

Goods exported outside UAE: Box 4. Services to non-resident with no UAE establishment: Box 4. Evidence required: customs export declaration, bill of lading, proof of delivery outside UAE, or contract with non-resident.

### 5.14 Local passenger transport (exempt)

Taxis, buses, metro, tram within UAE: exempt under Art. 46(4). Not standard rated. Limousine and luxury car hire: standard rated. This distinction is important — Careem/Uber ride-hailing is standard rated (not local passenger transport exemption).

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Motor vehicle vs commercial vehicle

*Pattern:* petrol station, parking, car wash, car rental, vehicle maintenance. *Why insufficient:* vehicle type unknown. Motor car expenses are blocked; commercial vehicles (delivery vans, trucks designed for goods) may be claimable. *Default:* 0% recovery. *Question:* "Is this for a passenger car (blocked) or a commercial vehicle designed exclusively for business goods transport?"

### 6.2 Entertainment vs staff welfare

*Pattern:* restaurant, cafe, catering, event venue. *Why insufficient:* client entertainment is blocked; staff meals at the workplace are claimable. *Default:* block. *Question:* "Was this client entertainment (blocked) or a staff meal at the workplace (claimable)?"

### 6.3 Ambiguous SaaS billing entities

*Pattern:* Google, Microsoft, AWS where the billing entity may be a UAE-registered entity or a non-resident. *Default:* reverse charge (non-resident). *Question:* "Could you check the invoice for the legal entity name and TRN? If the supplier has a UAE TRN, this is domestic 5%; if not, reverse charge applies."

### 6.4 Emirate allocation for Box 1

*Pattern:* sales where the delivery Emirate or establishment Emirate is unclear. *Why insufficient:* Box 1 requires breakdown by Emirate. *Default:* flag for reviewer. *Question:* "In which Emirate were these goods delivered / where is the establishment that provided this service?"

### 6.5 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit from a name matching the client's name. *Default:* exclude as owner injection. *Question:* "The AED X transfer from [name] — is this a customer payment, your own money going in, or a loan?"

### 6.6 Incoming transfers from foreign counterparties

*Pattern:* foreign bank, foreign currency. *Default:* domestic 5%. *Question:* "Was this a service to an overseas customer (potentially zero-rated)? Does the customer have a place of residence in the UAE?"

### 6.7 Insurance type determination

*Pattern:* insurance premium payment. *Why insufficient:* life insurance is exempt; general insurance (motor, property, health) is standard rated. *Default:* exclude (exempt default). *Question:* "Is this life insurance (exempt) or general/property/motor insurance (standard rated, input claimable)?"

### 6.8 Residential vs commercial property

*Pattern:* rent payment, property-related payment. *Why insufficient:* residential lease is exempt; commercial lease is standard rated. *Default:* residential (exempt). *Question:* "Is this a commercial property (VAT claimable) or residential (exempt)?"

### 6.9 Designated Zone involvement

*Pattern:* counterparty in a known free zone (JAFZA, DAFZA, KIZAD, etc.). *Why insufficient:* treatment depends on whether the zone is a Designated Zone and whether the transaction involves goods or services. *Default:* treat as mainland (standard 5%). *Question:* "Is this supplier in a Designated Zone? Is the transaction for goods or services?"

### 6.10 Employee health insurance

*Pattern:* health/medical insurance premium. *Why insufficient:* mandatory employee health insurance is claimable; additional voluntary benefits may be blocked as personal employee benefit. *Default:* claimable (mandatory DHA/HAAD requirement). *Question:* "Is this mandatory employee health insurance required by law, or voluntary additional coverage?"

### 6.11 Cash withdrawals

*Pattern:* ATM, cash withdrawal. *Default:* exclude as owner drawing. *Question:* "What was the cash used for?"

### 6.12 Outgoing transfers to individuals

*Pattern:* outgoing to private-looking names. *Default:* exclude as drawings/salary. *Question:* "Was this a contractor payment (with invoice), salary, or personal transfer?"

---

## Section 7 — Excel working paper template (UAE-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the UAE-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Box code") accepts: 1a, 1b, 1c, 1d, 1e, 1f, 1g, 3, 4, 5, 6, 9, 10, RC. Use blank for excluded transactions. Column M: Emirate (for Box 1 entries). For reverse-charge transactions, enter "RC" in column H.

### Sheet "Box Summary"

```
Output:
| 1a | Standard-rated supplies — Abu Dhabi | =SUMIFS(Transactions!E:E, Transactions!M:M, "Abu Dhabi") |
| 1b | Standard-rated supplies — Dubai | =SUMIFS(Transactions!E:E, Transactions!M:M, "Dubai") |
| 1c | Standard-rated supplies — Sharjah | =SUMIFS(...) |
| 1d-1g | (Ajman, UAQ, RAK, Fujairah) | =SUMIFS(...) |
| 1  | Total standard-rated supplies | =SUM(1a:1g) |
| 3  | Reverse charge supplies | =SUMIFS(Transactions!E:E, Transactions!H:H, "RC") |
| 4  | Zero-rated supplies | =SUMIFS(Transactions!E:E, Transactions!H:H, "4") |
| 5  | Exempt supplies | =SUMIFS(Transactions!E:E, Transactions!H:H, "5") |
| 6  | Goods imported | =SUMIFS(Transactions!E:E, Transactions!H:H, "6") |
| 8  | Total output tax | =C[1_row]*0.05 + C[3_row]*0.05 + C[6_row]*0.05 |

Input:
| 9  | Standard-rated expenses | =SUMIFS(Transactions!E:E, Transactions!H:H, "9") |
| 10 | Reverse charge input tax | =C[3_row]*0.05 |
| 11 | Total recoverable input tax | =C[9_row]*0.05 + C[10_row] |
```

### Sheet "Return Form"

```
Net VAT = Box 8 - Box 11

IF Box 8 > Box 11:
  VAT payable to FTA
ELSE:
  Excess input tax (refundable or carry forward)
```

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values, black for formulas, green for cross-sheet references, yellow background for rows where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/uae-vat-<period>-working-paper.xlsx
```

---

## Section 8 — UAE bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these UAE-specific patterns.

**Emirates NBD statement format.** Emirates NBD business banking exports use CSV or Excel with DD/MM/YYYY dates. Common columns: Transaction Date, Value Date, Description, Cheque No, Debit, Credit, Balance. The description field contains the counterparty name and transaction reference. SWIFT transfers show beneficiary name separately. Direct debits show the beneficiary/collector name.

**First Abu Dhabi Bank (FAB) statement format.** FAB exports use CSV with columns: Transaction Date, Description, Reference, Debit, Credit, Balance. International payments show the beneficiary bank and name. The description may be truncated for card transactions — check the reference field for additional detail.

**ADCB statement format.** ADCB online banking exports include columns: Date, Narrative, Reference Number, Debit, Credit, Balance. The narrative field is the primary source for counterparty identification.

**Mashreq statement format.** Mashreq exports: Date, Description, Debit, Credit, Balance. Card purchases show the merchant name. SWIFT transfers show the beneficiary name.

**Revolut / Wise Business.** ISO date format. Clear counterparty names. Separate fee lines — exclude fees (exempt financial service). Currency conversion details included.

**Internal transfers and exclusions.** Own-account transfers between the client's Emirates NBD, FAB, ADCB accounts. Labelled "own transfer", "internal transfer", "between accounts". Always exclude.

**WPS (Wage Protection System) entries.** Salary payments via WPS appear as "WPS SALARY", "SALARY TRANSFER", or individual employee names. Always exclude — employment, out of scope.

**Salik (road toll).** Salik top-ups and toll deductions appear as "SALIK", "RTA SALIK". These are government fees, out of scope. Exclude.

**Foreign currency transactions.** Convert to AED at the UAE Central Bank exchange rate on the transaction date. Note the rate used in column L (Notes).

**Card purchases with merchant terminal codes.** Some card purchases show only a merchant terminal code (e.g., "POS 1234567 DUBAI"). If the counterparty cannot be identified, ask the client. Do not classify unidentified transactions.

**DEWA/ADDC housing fee component.** DEWA and ADDC bills include a municipality housing fee (5% of annual rent for Dubai/Abu Dhabi). The housing fee component is a government fee, out of scope. The electricity/water component is standard-rated at 5%. If the statement shows a single DEWA amount, treat the full amount as standard-rated 5% (conservative — the housing fee is a small proportion and is not VAT-deductible anyway).

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type and trading name
*Inference rule:* "LLC" = limited liability company; "sole establishment" or personal name = sole proprietor; "FZCO", "FZE", "FZ-LLC" = free zone entity. *Fallback question:* "Are you a mainland LLC, sole establishment, free zone company, or branch?"

### 9.2 TRN
*Inference rule:* TRN may appear on bank statement descriptions (rare) or invoices. *Fallback question:* "What is your Tax Registration Number (TRN)? (15-digit number)"

### 9.3 Filing period
*Inference rule:* first and last transaction dates on bank statement. Quarterly is default. *Fallback question:* "Which quarter does this cover? Q1 (Jan–Mar), Q2 (Apr–Jun), Q3 (Jul–Sep), or Q4 (Oct–Dec)?"

### 9.4 Emirate of establishment
*Inference rule:* utility bills (DEWA = Dubai, ADDC = Abu Dhabi, SEWA = Sharjah), commercial rent, trade licence issuer. *Fallback question:* "Which Emirate is your business established in? (For Box 1 allocation of service sales)"

### 9.5 Industry and sector
*Inference rule:* counterparty mix, sales patterns. *Fallback question:* "In one sentence, what does the business do?"

### 9.6 Employees
*Inference rule:* WPS salary payments, visa fees, health insurance. *Fallback question:* "Do you have employees?"

### 9.7 Exempt supplies
*Inference rule:* residential rental income, financial service income. *Fallback question:* "Do you make any VAT-exempt sales (residential property, financial services, life insurance)?" *If yes and significant, R-AE-1 may fire.*

### 9.8 Designated Zone
*Inference rule:* free zone trade licence, JAFZA/DAFZA/KIZAD in address. *Fallback question:* "Is your business in a Designated Zone (e.g., JAFZA, DAFZA, KIZAD)? Do you move goods in/out of the zone?"

### 9.9 Carried-forward excess input tax
*Inference rule:* not inferable from a single period statement. Always ask. *Question:* "Do you have any excess input tax carried forward from the previous period?"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the Malta v2.0 structure. It supersedes v1.0/v2.0 standalone versions.

### Sources

**Primary legislation:**
1. Federal Decree-Law No. 8 of 2017 on Value Added Tax (VAT Decree-Law) — Articles 2-7, 25-34, 45-57, 59-60
2. Cabinet Decision No. 52 of 2017 (Executive Regulation) — Articles 14-21, 30-50, 53, 59, 62, 69
3. Federal Decree-Law No. 7 of 2017 on Tax Procedures — Articles 26, 28-30
4. Cabinet Decision No. 40 of 2017 (Designated Zones)
5. Cabinet Decision No. 59 of 2017 (Designated Zones list, as amended)
6. Cabinet Decision No. 49 of 2021 (Penalties)
7. Cabinet Decision No. 129 of 2025 (Revised penalties, effective 14 April 2026)
8. Cabinet Decision No. 106 of 2025 (E-invoicing)

**FTA guidance:**
9. VAT Public Clarification VATP002 (residential property)
10. VAT Public Clarification VATP011 (financial services)
11. FTA VAT201 form completion guide

**Other:**
12. FTA e-Services portal — https://eservices.tax.gov.ae
13. UAE Central Bank exchange rates

### Known gaps

1. The supplier pattern library covers the most common UAE and international counterparties but does not cover every local business.
2. The worked examples are drawn from a hypothetical IT consultant in Dubai. They do not cover construction, oil & gas, real estate, or F&B specifically.
3. The Designated Zone treatment (R-AE-3) is refused rather than handled — future versions should add deterministic rules for common Designated Zone goods movements.
4. E-invoicing requirements (from mid-2026 / January 2027) are referenced but compliance specifics are not detailed.
5. The Tourist Refund Scheme (Box 2) is refused (R-AE-7) — only relevant for qualifying retailers.
6. GCC inter-state supply rules (UAE to Bahrain, Oman, Saudi) are not covered in detail due to ongoing transitional provisions.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with Malta v2.0 structure. Quick reference with Box/Field table and conservative defaults at top (Section 1). Supplier pattern library with UAE vendors (Emirates NBD, FAB, ADCB, Mashreq, du, Etisalat, DEWA/ADDC, Carrefour, Noon, Emirates, Freezone suppliers) in Section 3. Six worked examples (Section 4). Compressed Tier 1 rules (Section 5). Tier 2 catalogue (Section 6). Excel working paper (Section 7). UAE bank statement guide with Emirates NBD/FAB formats (Section 8). Onboarding fallback (Section 9). References (Section 10).
- **v1.0 (April 2026):** Initial standalone skill covering VAT Decree-Law, box mappings, reverse charge, blocked categories, Designated Zones, e-invoicing, registration, penalties.

### Self-check (v2.0 of this document)

1. Quick reference at top with field/box table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 14 rules).
5. Tier 2 catalogue compressed: yes (Section 6, 12 items).
6. Excel template specification with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only: yes (Section 9, 9 items).
8. All 7 UAE-specific refusals present: yes (Section 2, R-AE-1 through R-AE-7).
9. Reference material at bottom: yes (Section 10).
10. Entertainment block explicit: yes (Section 5.9 + Example 3).
11. Motor vehicle block explicit: yes (Section 5.9 + Example 5).
12. Reverse charge for non-resident services explicit: yes (Example 1 + Section 5.5).
13. Zero-rated export and "no UAE establishment" test explicit: yes (Example 2 + Section 5.13).
14. Emirate breakdown (Box 1a–1g) explicit: yes (Section 5.8 + Tier 2 item 6.4).
15. Emirates NBD/FAB bank statement format guide: yes (Section 8).

## End of UAE VAT Return Skill v2.0

This skill is incomplete without the companion file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a VAT201 without both files loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax agent, CPA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
