---
name: uk-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a UK VAT return (VAT100) for a self-employed individual or very small business in Great Britain. Trigger on phrases like "prepare VAT return", "do my VAT", "classify these for VAT", "VAT100", "9-box return", "MTD", "Making Tax Digital", "flat rate scheme", "FRS", "cash accounting VAT", "input tax", "output tax", "reverse charge construction", "CIS reverse charge", "bad debt relief", "Box 1 to Box 9", "reduced rate UK", "zero-rated UK", "exempt supply UK", "de minimis VAT", "annual accounting scheme", or any question about UK VAT obligations. Covers the VAT100 9-box structure, standard/reduced/zero rates, registration threshold (GBP 90,000), Flat Rate Scheme, cash accounting scheme, annual accounting scheme, MTD requirements, input tax blocked categories, partial exemption, bad debt relief, and reverse charge for construction (CIS). MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any UK VAT work.
version: 2.0
---

# UK VAT Return Skill (VAT100) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

| Field | Value |
|---|---|
| Country | United Kingdom of Great Britain and Northern Ireland |
| Standard rate | 20% |
| Reduced rate | 5% (domestic fuel and power, children's car seats, energy-saving materials installed in residential property, smoking cessation products, women's sanitary products) |
| Zero rate | 0% (most food, children's clothing and footwear, books and newspapers, public transport, new residential construction, exports, prescribed medicines) |
| Return form | VAT100 (9-box return) |
| Filing portal | HMRC VAT Online Services / MTD-compatible software (Xero, QuickBooks, FreeAgent, Sage, Kashflow, bridging software) |
| Authority | HM Revenue & Customs (HMRC) |
| Currency | GBP only |
| Filing frequencies | Quarterly (standard), Monthly (optional or required for regular repayment traders), Annual (annual accounting scheme) |
| Deadline | Quarterly/monthly: 1 month and 7 days after the end of the VAT period; Annual: 2 months after the year-end |
| Registration threshold | GBP 90,000 (rolling 12-month taxable turnover) |
| Deregistration threshold | GBP 88,000 |
| FRS entry threshold | GBP 150,000 (estimated taxable turnover excl. VAT, next 12 months) |
| FRS exit threshold | GBP 230,000 (total business income incl. VAT) |
| Cash accounting threshold | GBP 1,350,000 (entry); GBP 1,600,000 (exit) |
| Primary legislation | Value Added Tax Act 1994 (VATA 1994) |
| Supporting legislation | VAT Regulations 1995 (SI 1995/2518); Finance Act 2024; Finance Act 2025; The Value Added Tax (Flat Rate Scheme) Order 2004; The VAT (Input Tax) Order 1992 (SI 1992/3222); Making Tax Digital (VAT) Regulations 2018 |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a UK-qualified accountant (ACA/ACCA/CTA) |
| Validation date | Pending |

**Key VAT100 boxes (the boxes you will use most):**

| Box | Meaning |
|---|---|
| 1 | VAT due on sales and other outputs (output VAT charged to customers; reverse charge VAT due; postponed import VAT) |
| 2 | VAT due on acquisitions from EU (legacy — post-Brexit generally use postponed import VAT in Box 1) |
| 3 | Total VAT due (Box 1 + Box 2) — automatic sum |
| 4 | VAT reclaimed on purchases and other inputs (input VAT on allowable business purchases; import VAT recoverable; reverse charge VAT recoverable) |
| 5 | Net VAT to pay or reclaim (Box 3 minus Box 4) — positive = pay HMRC, negative = HMRC refunds |
| 6 | Total value of sales and all other outputs excluding VAT (all outputs: standard, reduced, zero, exempt) |
| 7 | Total value of purchases and all other inputs excluding VAT (all inputs including exempt and zero-rated) |
| 8 | Total value of supplies of goods to EU excluding VAT (post-Brexit: exports of goods to EU) |
| 9 | Total value of acquisitions of goods from EU excluding VAT (post-Brexit: imports of goods from EU) |

**Conservative defaults — UK-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 20% |
| Unknown VAT status of a purchase | Not deductible |
| Unknown counterparty country | Domestic UK |
| Unknown B2B vs B2C status for overseas customer | B2C, charge 20% |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown SaaS billing entity | Reverse charge from overseas (Box 6/7) |
| Unknown blocked-input status (entertainment, personal use) | Blocked |
| Unknown whether transaction is in scope | In scope |
| Unknown FRS Limited Cost Trader status | LCT at 16.5% (most conservative) |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | GBP 5,000 |
| HIGH tax-delta on a single conservative default | GBP 400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net VAT position | GBP 10,000 |

**Flat Rate Scheme — selected sector percentages (2025):**

| Sector | FRS % |
|---|---|
| Accountancy or bookkeeping | 14.5% |
| Advertising | 11.0% |
| Computer and IT consultancy | 14.5% |
| Computer repair | 10.5% |
| Estate agency or property management | 12.0% |
| Journalism or photography | 11.0% |
| Management consultancy | 14.0% |
| Publishing | 11.0% |
| Real estate | 14.0% |
| Secretarial services | 13.0% |
| Social worker | 11.0% |
| Transport or storage | 10.0% |
| Any other activity not listed | 12.0% |
| **Limited Cost Trader (any sector)** | **16.5%** |

First-year discount: new VAT registrations get a 1% reduction in the FRS percentage for the first year.

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full VAT period. Acceptable from any UK business bank: Barclays, HSBC UK, Lloyds, NatWest, Santander UK, Metro Bank, Starling, Monzo Business, Tide, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices for the period (especially for zero-rated exports and reverse charge services), purchase invoices for any input VAT claim above GBP 250, the client's VAT registration number (9-digit GB number), the prior period's VAT return (for Box 5 reconciliation and FRS comparison).

**Ideal** — complete invoice register, MTD-compatible digital records with digital links, reconciliation of prior period Box 5 position, confirmation of VAT scheme (standard, FRS, cash accounting, annual accounting).

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in the reviewer brief: "This VAT100 was produced from bank statement alone. The reviewer must verify, before approval, that input VAT claims above GBP 250 are supported by compliant tax invoices and that all reverse-charge classifications match the supplier's invoice."

### UK-specific refusal catalogue

These refusals apply on top of any universal refusals in `vat-workflow-base`. If any trigger fires, stop, output the refusal message verbatim, end the conversation. Refusal is a safety mechanism.

**R-UK-1 — Partial exemption beyond de minimis.** *Trigger:* client makes both taxable and exempt supplies and the exempt input VAT exceeds GBP 625 per month on average OR exceeds 50% of total input VAT. *Message:* "Your exempt input VAT exceeds the de minimis threshold. Partial exemption requires a formal calculation under the standard method (or a special method agreed with HMRC) including an annual adjustment. This is too fact-sensitive for this skill. Please use a qualified accountant (ACA/ACCA/CTA) to determine and confirm the recoverable proportion before input VAT is claimed."

**R-UK-2 — Transfer of a going concern (TOGC).** *Trigger:* the period contains a business transfer that may qualify as a TOGC under VATA 1994 s49. *Message:* "TOGCs are outside the scope of VAT but have strict conditions. Incorrect treatment can result in a significant VAT liability. Please use a qualified accountant to confirm TOGC status."

**R-UK-3 — Margin scheme (second-hand goods, tour operators).** *Trigger:* client deals in second-hand goods under the margin scheme or is a tour operator using TOMS. *Message:* "Margin scheme transactions require transaction-level margin computation. Tour Operators' Margin Scheme (TOMS) requires a year-end calculation. Out of scope for this skill."

**R-UK-4 — CIS reverse charge complex.** *Trigger:* the client receives or makes supplies of construction services within the Construction Industry Scheme where the end-user exemption, intermediary supplier status, or mixed supply classification is unclear. *Message:* "The CIS domestic reverse charge is fact-specific. End-user exemptions, intermediary supplier status, and mixed supply classification require professional judgement. Please confirm with a qualified accountant before applying or disapplying the reverse charge."

**R-UK-5 — VAT group.** *Trigger:* client is part of a VAT group or asks about group registration under VATA 1994 s43. *Message:* "VAT groups require consolidation across all group members. Intra-group supplies are disregarded. Out of scope for this skill."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment from the table directly. Do not second-guess. Do not consult Tier 1 rules — the table is authoritative for patterns it covers.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

**Post-Brexit note.** Since 1 January 2021, EU suppliers are treated identically to non-EU suppliers for UK VAT purposes. There is no intra-EU acquisition regime for the UK. Services received from both EU and non-EU suppliers trigger the reverse charge under the same rules. Goods imported from any country (including EU) are subject to import VAT (postponed or at border).

### 3.1 UK banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BARCLAYS, BARCLAYS BANK | EXCLUDE for bank charges/fees | Financial service, exempt |
| HSBC UK, HSBC BANK | EXCLUDE for bank charges/fees | Same |
| LLOYDS, LLOYDS BANK, LLOYDS TSB | EXCLUDE for bank charges/fees | Same |
| NATWEST, NATIONAL WESTMINSTER | EXCLUDE for bank charges/fees | Same |
| SANTANDER UK | EXCLUDE for bank charges/fees | Same |
| METRO BANK | EXCLUDE for bank charges/fees | Same |
| STARLING BANK | EXCLUDE for bank charges/fees | Same |
| MONZO, MONZO BANK | EXCLUDE for bank charges/fees | Same |
| TIDE, TIDE PLATFORM | EXCLUDE for bank charges/fees | Same |
| REVOLUT (fee lines), WISE (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, BANK INTEREST | EXCLUDE | Interest income/expense, out of scope |
| LOAN, BUSINESS LOAN, BOUNCE BACK LOAN | EXCLUDE | Loan principal movement, out of scope |
| OVERDRAFT FEE, ARRANGEMENT FEE | EXCLUDE | Exempt financial service |

### 3.2 HMRC and government (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| HMRC, HM REVENUE, HMRC VAT | EXCLUDE | Tax payment, not a supply |
| HMRC PAYE, HMRC NIC, HMRC CT | EXCLUDE | Tax payment |
| COMPANIES HOUSE, COMPANIES HSE | EXCLUDE | Statutory fee, not a supply |
| COUNCIL TAX, BUSINESS RATES | EXCLUDE | Local authority levy, outside scope |
| DVLA | EXCLUDE | Road tax, statutory fee |
| ICO, INFORMATION COMMISSIONER | Domestic 20% | Data protection fee — taxable supply, input VAT recoverable |
| TV LICENSING, BBC | EXCLUDE | Broadcasting licence, outside scope |
| LAND REGISTRY, HM LAND REGISTRY | EXCLUDE | Statutory fee |

### 3.3 UK utilities

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| BRITISH GAS, CENTRICA | 5% domestic fuel / 20% commercial | Box 7 / Box 4 | Domestic fuel and power = 5% reduced rate; commercial premises = 20%. Default: 5% unless confirmed commercial |
| EDF ENERGY, EDF | 5% domestic fuel / 20% commercial | Box 7 / Box 4 | Same |
| OCTOPUS ENERGY, BULB, OVO, SSE, SCOTTISH POWER, E.ON, NPOWER | 5% domestic fuel / 20% commercial | Box 7 / Box 4 | Same |
| THAMES WATER, SEVERN TRENT, UNITED UTILITIES, ANGLIAN WATER, WESSEX WATER, SOUTHERN WATER, YORKSHIRE WATER | 0% | Box 7 | Water supply is zero-rated in the UK |
| BT, BRITISH TELECOM, BT GROUP | Domestic 20% | Box 7 / Box 4 | Telecoms, standard rated |
| SKY, SKY UK | Domestic 20% | Box 7 / Box 4 | Telecoms/broadband, standard rated |
| VIRGIN MEDIA, VIRGIN MEDIA O2 | Domestic 20% | Box 7 / Box 4 | Telecoms/broadband, standard rated |
| VODAFONE, EE, THREE, O2 | Domestic 20% | Box 7 / Box 4 | Mobile telecoms, standard rated |
| OPENREACH | Domestic 20% | Box 7 / Box 4 | Line rental, standard rated |

### 3.4 UK insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| AVIVA, AVIVA INSURANCE | EXCLUDE | Insurance premium, exempt |
| DIRECT LINE, DIRECT LINE GROUP | EXCLUDE | Same |
| LEGAL & GENERAL, L&G | EXCLUDE | Same |
| ADMIRAL, ADMIRAL GROUP | EXCLUDE | Same |
| AXA UK, ZURICH UK, HISCOX | EXCLUDE | Same |
| RSA, MORE THAN, LV= | EXCLUDE | Same |
| INSURANCE, INSURANCE PREMIUM, IPT | EXCLUDE | All exempt (Insurance Premium Tax is outside VAT scope) |
| PROFESSIONAL INDEMNITY, PI INSURANCE | EXCLUDE | Exempt |

### 3.5 UK transport

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| TFL, TRANSPORT FOR LONDON, OYSTER | 0% | Box 7 | Public transport, zero-rated |
| NATIONAL RAIL, TRAINLINE, GWR, LNER, AVANTI, SOUTHEASTERN, THAMESLINK | 0% | Box 7 | Rail fares, zero-rated |
| UBER UK, UBER BV | Domestic 20% | Box 7 / Box 4 | Ride-hailing, standard rated. Uber invoices from NL entity — check if reverse charge applies |
| TAXI, ADDISON LEE, BOLT UK | Domestic 20% | Box 7 / Box 4 | Taxi services, standard rated |
| BRITISH AIRWAYS, BA, EASYJET, RYANAIR (international flights) | 0% | Box 7 | International flights, zero-rated |
| PARKING, NCP, APCOA, RINGGO | Domestic 20% | Box 7 / Box 4 | Car parking, standard rated |

### 3.6 UK food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| TESCO, SAINSBURYS, SAINSBURY'S, ASDA, MORRISONS, WAITROSE, ALDI, LIDL UK, CO-OP, M&S FOOD, MARKS AND SPENCER | Default BLOCK input VAT | Supermarket — personal provisioning. Deductible only if hospitality/catering business purchasing stock for resale |
| PRET, PRET A MANGER, COSTA, STARBUCKS, GREGGS, MCDONALDS, KFC, NANDOS, WAGAMAMA | Default BLOCK | Entertainment/personal. Client entertaining is blocked in UK (no exceptions). Staff entertainment may be recoverable — see Tier 2 |
| DELIVEROO, JUST EAT, UBER EATS | Default BLOCK | Entertainment/personal consumption |
| RESTAURANTS, CAFES, BARS (any named restaurant) | Default BLOCK | Client entertainment VAT is blocked — VATA 1994 s25; VAT (Input Tax) Order 1992. Exception: entertaining overseas customers IS recoverable |

### 3.7 SaaS — EU suppliers (reverse charge, Box 6/7)

Post-Brexit, EU suppliers are treated as overseas suppliers. Services received from EU-established businesses trigger the reverse charge. The UK recipient self-accounts: output VAT in Box 1 (and Box 6 for the net value), input VAT in Box 4 (and Box 7 for the net value). Net cash effect zero for a fully taxable business.

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | Box 1+6 / Box 4+7 | Reverse charge — post-Brexit, IE is overseas |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | Box 1+6 / Box 4+7 | Reverse charge |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | Box 1+6 / Box 4+7 | Reverse charge |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Box 1+6 / Box 4+7 | Reverse charge |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | Box 1+6 / Box 4+7 | Reverse charge |
| SPOTIFY | Spotify AB (SE) | Box 1+6 / Box 4+7 | Reverse charge |
| DROPBOX | Dropbox International Unlimited (IE) | Box 1+6 / Box 4+7 | Reverse charge |
| SLACK | Slack Technologies Ireland Ltd (IE) | Box 1+6 / Box 4+7 | Reverse charge |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | Box 1+6 / Box 4+7 | Reverse charge |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | Box 1+6 / Box 4+7 | Reverse charge |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | Box 1+6 / Box 4+7 | Transaction fees may be exempt — see 3.9 |
| XERO | Xero UK Ltd (UK entity) | Domestic 20% Box 7/4 | Xero bills from UK entity — standard domestic, NOT reverse charge |

### 3.8 SaaS — non-EU suppliers (reverse charge, Box 6/7)

Post-Brexit, both EU and non-EU suppliers trigger the same reverse charge mechanism. The distinction is academic for UK VAT purposes but listed separately for clarity of billing entity.

| Pattern | Billing entity | Box | Notes |
|---|---|---|---|
| AWS, AMAZON WEB SERVICES | Amazon Web Services Inc (US) or AWS EMEA SARL (LU) | Box 1+6 / Box 4+7 | Reverse charge. Check invoice — LU entity is also overseas post-Brexit |
| NOTION | Notion Labs Inc (US) | Box 1+6 / Box 4+7 | Reverse charge |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Box 1+6 / Box 4+7 | Reverse charge |
| OPENAI, CHATGPT | OpenAI Inc (US) | Box 1+6 / Box 4+7 | Reverse charge |
| GITHUB | GitHub Inc (US) | Box 1+6 / Box 4+7 | Check if billed by IE entity — still reverse charge post-Brexit |
| FIGMA | Figma Inc (US) | Box 1+6 / Box 4+7 | Reverse charge |
| CANVA | Canva Pty Ltd (AU) | Box 1+6 / Box 4+7 | Reverse charge |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE) | Box 1+6 / Box 4+7 | Reverse charge either way post-Brexit |
| TWILIO | Twilio Inc (US) | Box 1+6 / Box 4+7 | Reverse charge |
| APPLE (App Store, iCloud) | Apple Distribution International Ltd (IE) | Box 1+6 / Box 4+7 | Reverse charge post-Brexit |
| MAILCHIMP, INTUIT MAILCHIMP | Intuit Inc (US) or The Rocket Science Group LLC (US) | Box 1+6 / Box 4+7 | Reverse charge |

### 3.9 Payment processors (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| STRIPE (monthly subscription) | Reverse charge Box 1+6 / Box 4+7 | Stripe IE entity — separate from exempt transaction fees |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same — exempt financial services |
| GOCARDLESS | EXCLUDE (exempt) | Direct debit processing fees, exempt financial service |
| SUMUP, SQUARE, ZETTLE, IZETTLE | Check invoice | If UK entity: domestic 20%; if IE/EU entity: reverse charge. Transaction fees are exempt; hardware/subscription may be taxable |
| WORLDPAY, BARCLAYCARD MERCHANT | EXCLUDE (exempt) | Merchant service fees, exempt |

### 3.10 Professional services (UK domestic 20%)

| Pattern | Treatment | Box | Notes |
|---|---|---|---|
| Accountant names, ACCOUNTANT, CPA, ACCA, ACA, ICAEW, BOOKKEEPER | Domestic 20% | Box 7 / Box 4 | Always deductible |
| Solicitor names, SOLICITOR, LAWYER, LAW FIRM, LLP | Domestic 20% | Box 7 / Box 4 | Deductible if business legal matter. Disbursements may be zero-rated or exempt |
| BARRISTER, COUNSEL, QC, KC | Domestic 20% | Box 7 / Box 4 | Standard rated professional services |

### 3.11 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| RENT (commercial, with VAT on invoice) | Domestic 20% | Commercial lease where landlord has opted to tax — Box 7 / Box 4 |
| RENT (residential, no VAT) | EXCLUDE | Residential lease is exempt — no input VAT recovery |
| GROUND RENT, SERVICE CHARGE (residential) | EXCLUDE | Exempt |
| COMMERCIAL RENT, OFFICE RENT, REGUS, WEWORK, IWGSERVICED OFFICE | Domestic 20% | Serviced offices typically charge 20% |

### 3.12 Payroll and statutory payments (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| PAYE, PAY AS YOU EARN | EXCLUDE | Income tax remittance to HMRC |
| NIC, NATIONAL INSURANCE, EMPLOYERS NI | EXCLUDE | Statutory contribution, outside scope |
| SALARY, WAGES, NET PAY | EXCLUDE | Staff costs, outside VAT scope |
| PENSION, NEST, WORKPLACE PENSION, AUTO ENROLMENT | EXCLUDE | Pension contributions, outside scope |
| SSP, SMP, STATUTORY PAY | EXCLUDE | Statutory payments, outside scope |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a UK-based self-employed IT consultant. They illustrate the trickiest cases. Pattern-match against these when you encounter similar lines in any real statement.

### Example 1 — Overseas SaaS reverse charge (Notion)

**Input line:**
`03.04.2025 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; GBP 12.80`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.8). No VAT on the invoice. This is a service received from an overseas supplier. The UK recipient self-accounts for VAT under the reverse charge. Output VAT goes to Box 1 (GBP 2.56 = 12.80 x 20%) and Box 6 (GBP 12.80 net). Input VAT goes to Box 4 (GBP 2.56) and Box 7 (GBP 12.80 net). Net cash effect zero for a fully taxable business.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (output) | Box (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 03.04.2025 | NOTION LABS INC | -12.80 | -12.80 | 2.56 | 20% | Box 1+6 | Box 4+7 | N | — | — |

### Example 2 — EU service, reverse charge post-Brexit (Google Ads)

**Input line:**
`10.04.2025 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2025 ; -850.00 ; GBP`

**Reasoning:**
Google Ireland Limited is an IE entity. Post-Brexit, Ireland is overseas for UK VAT purposes — same treatment as any non-UK supplier. Reverse charge applies. Output VAT = GBP 170.00 (850 x 20%) to Box 1. Net GBP 850 to Box 6. Input VAT GBP 170.00 to Box 4. Net GBP 850 to Box 7. Net cash effect zero.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (output) | Box (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 10.04.2025 | GOOGLE IRELAND LIMITED | -850.00 | -850.00 | 170.00 | 20% | Box 1+6 | Box 4+7 | N | — | — |

### Example 3 — Client entertainment, fully blocked

**Input line:**
`15.04.2025 ; THE IVY RESTAURANT LONDON ; DEBIT ; Business dinner ; -220.00 ; GBP`

**Reasoning:**
Restaurant transaction. Client entertainment input VAT is fully blocked under VATA 1994 s25 and the VAT (Input Tax) Order 1992. Unlike some jurisdictions, the UK has no partial recovery for business meals with clients. The one exception: entertaining overseas customers IS recoverable. Default: full block unless confirmed overseas customer entertainment. The net value still goes to Box 7, but no VAT to Box 4.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (output) | Box (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 15.04.2025 | THE IVY RESTAURANT | -220.00 | -183.33 | 0 | — | — | Box 7 only | Y | Q1 | "Entertainment: blocked. Was this entertaining overseas customers?" |

### Example 4 — Domestic fuel (5% reduced rate)

**Input line:**
`18.04.2025 ; BRITISH GAS ; DEBIT ; Direct debit gas bill ; -95.00 ; GBP`

**Reasoning:**
Domestic fuel and power attracts the 5% reduced rate. If this is the client's home and they work from home, only the business-use proportion is recoverable. Default: 0% business use unless the client specifies a proportion. The gross amount includes 5% VAT: net = 95.00 / 1.05 = GBP 90.48, VAT = GBP 4.52.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (output) | Box (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 18.04.2025 | BRITISH GAS | -95.00 | -90.48 | 0 | 5% | — | Box 7 | Y | Q2 | "Home office: what % of this property is used for business?" |

### Example 5 — Zero-rated export sale

**Input line:**
`22.04.2025 ; ACME CORP INC NEW YORK ; CREDIT ; Invoice UK-2025-018 IT consultancy March ; +5,000.00 ; GBP`

**Reasoning:**
Incoming payment from a US company. B2B services to an overseas customer — place of supply is the customer's country (US) under the general rule. The client invoices at 0% (outside the scope of UK VAT). Report net amount in Box 6 (total outputs). No output VAT in Box 1. Confirm: (a) customer is a business, not a consumer; (b) the invoice shows no UK VAT with a note that the supply is outside the scope of UK VAT.

**Output:**

| Date | Counterparty | Gross | Net | VAT | Rate | Box (output) | Box (input) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 22.04.2025 | ACME CORP INC | +5,000.00 | +5,000.00 | 0 | 0% | Box 6 | — | Y | Q3 (HIGH) | "Verify: is this a B2B supply? Confirm customer is a business." |

### Example 6 — Flat Rate Scheme computation

**Input line:**
`Quarter total: gross (VAT-inclusive) turnover GBP 30,000. FRS sector: IT consultancy (14.5%). Goods purchased in quarter: GBP 200.`

**Reasoning:**
First check the Limited Cost Trader test. Goods spend = GBP 200. 2% of GBP 30,000 = GBP 600. GBP 200 < GBP 600, and GBP 200 < GBP 1,000 annualised. Client IS a Limited Cost Trader. Rate = 16.5%, not 14.5%. VAT payable = 30,000 x 16.5% = GBP 4,950. Under standard accounting: output VAT = GBP 5,000 (30,000 / 1.2 x 0.2), input VAT recovery would need to exceed GBP 50 to beat FRS. At 16.5% LCT, FRS is almost certainly worse than standard accounting. Flag for reviewer.

**Output:**

| Field | Value |
|---|---|
| FRS sector rate | 14.5% |
| LCT test | FAIL — goods spend GBP 200 < 2% of GBP 30,000 (GBP 600) |
| Applied rate | 16.5% (LCT) |
| Box 1 | GBP 4,950 |
| Box 6 | GBP 25,000 (net of VAT) |
| Reviewer flag | "LCT rate 16.5% applied. Client may be better off on standard accounting." |

---

## Section 5 — Tier 1 classification rules (compressed)

Each rule states the legal source and the box mapping. Apply silently if the data is unambiguous. For full doctrinal context, see the source citations in Section 10.

### 5.1 Standard rate 20% (VATA 1994 s2(1), Schedule 7A)

Default rate for any taxable supply unless a reduced rate, zero rate, or exemption applies. Most goods and services, professional fees, software, electronics, commercial property (where opted to tax). Sales output VAT to Box 1. Net sales to Box 6. Purchase input VAT to Box 4. Net purchases to Box 7.

### 5.2 Reduced rate 5% (VATA 1994 Schedule 7A)

Applies to: domestic fuel and power (gas, electricity for domestic use), children's car seats, energy-saving materials installed in residential property, smoking cessation products, contraceptive products, women's sanitary products (from January 2021). Purchases at 5%: extract VAT at 5/105 of the gross. Box 7 for net, Box 4 for input VAT (subject to business-use proportion for home office).

### 5.3 Zero rate 0% (VATA 1994 Schedule 8)

Applies to: most food (not catering, not hot takeaway, not confectionery, not alcohol, not soft drinks), children's clothing and footwear, books and newspapers (print and digital since May 2020), public transport fares, new residential construction (first grant of a major interest), exports of goods, prescribed medicines, water supply. Sales: no output VAT, but net value goes to Box 6. Purchases: no input VAT to claim, but net value goes to Box 7. Input VAT on costs attributable to zero-rated supplies IS recoverable.

**Key rate traps:**

| Item | Rate | Trap |
|---|---|---|
| Hot takeaway food | 20% | NOT zero-rated like cold food |
| Chocolate biscuits | 20% | Standard-rated confectionery |
| Plain biscuits | 0% | Zero-rated |
| Jaffa Cakes | 0% | Classified as cakes (zero-rated), not chocolate biscuits |
| E-books and digital newspapers | 0% | Zero-rated since 1 May 2020 |
| Catering (hot or cold) | 20% | Standard-rated even if the food itself would be zero-rated |
| Ice cream | 20% | Standard-rated confectionery |
| Fruit juice | 20% | Standard-rated (soft drink, not food) |
| Bottled water | 0% | Zero-rated (water) |
| Takeaway cold sandwich | 0% | Zero-rated (cold, not catering premises) |
| Coffee beans (unroasted) | 0% | Zero-rated (food ingredient) |
| Hot coffee drink | 20% | Standard-rated (hot beverage, catering) |

### 5.4 Exempt supplies (VATA 1994 Schedule 9)

No VAT charged, no input VAT recovery on attributable costs. Exempt supplies: insurance, financial services (interest, foreign exchange, securities dealing), education (by eligible bodies), health services (by registered practitioners), burial and cremation, postal services (Royal Mail universal service), land and property (unless opted to tax), membership subscriptions (certain professional bodies), betting and gaming.

If exempt supplies are significant, partial exemption rules apply — R-UK-1 refuses if beyond de minimis.

### 5.5 Outside scope (exclude from all boxes)

Wages, salaries, dividends, donations, non-business activities, statutory fees (road tax, council tax, business rates), HMRC tax payments, loan principal, drawings, internal transfers. Do NOT include in Box 6 or Box 7.

### 5.6 Reverse charge — services received from overseas suppliers

Post-Brexit, all non-UK suppliers (whether EU or non-EU) trigger the same reverse charge mechanism for services. The UK recipient self-accounts at 20%: output VAT to Box 1, net value to Box 6; input VAT to Box 4, net value to Box 7. Net cash effect zero for a fully taxable business. If the overseas supplier incorrectly charged their local VAT (e.g. Irish 23%), that foreign VAT is NOT recoverable as UK input tax — treat as a cost.

### 5.7 Reverse charge — CIS construction (VATA 1994 s55A)

For specified construction services between VAT-registered, CIS-registered businesses where the customer makes onward supplies of construction services: the customer (not the supplier) accounts for VAT. Supplier invoices net with annotation "Reverse charge: Customer to account to HMRC for VAT on this supply." Customer: output VAT to Box 1, input VAT to Box 4, net value to Box 7 only (not Box 6 — this is the customer's input, not output). End-user exemption: does NOT apply if the customer is an end user or intermediary supplier.

### 5.8 Input VAT — blocked categories (VATA 1994 s25; VAT (Input Tax) Order 1992)

The following input VAT CANNOT be reclaimed:

- Business entertainment: entertaining UK customers, suppliers, or other business contacts. **Exception:** entertaining overseas customers IS recoverable
- Motor cars: VAT on purchase or lease of cars NOT exclusively for business use. **Exception:** 100% business use (pool car, driving instructor car, taxi) = fully recoverable
- Car fuel (private element): if car has any private use, full input VAT on fuel is blocked UNLESS the fuel scale charge is applied
- Non-business expenditure: expenditure not wholly for business purposes

Partially recoverable items:
- Mobile phones: fully recoverable if business contract (even if some private use)
- Home office costs: apportion business vs private — recover business element only
- Mixed-use equipment: apportion on reasonable basis

### 5.9 Bad debt relief (VATA 1994 s36; VAT Regulations 1995 reg 168-172)

If a customer does not pay, the supplier can reclaim the output VAT already paid to HMRC. Conditions: debt at least 6 months old (from later of due date or supply date), debt written off in accounts, claim on VAT return for the period conditions are met, claim within 4 years 6 months of supply date. Relief amount added to Box 4. If customer later pays, relief must be reversed.

### 5.10 Flat Rate Scheme (VATA 1994 s26B)

Business charges 20% on invoices, pays HMRC a flat percentage of gross (VAT-inclusive) turnover. Key rule: ALWAYS run the Limited Cost Trader test first. If goods spend < 2% of gross turnover (or < GBP 1,000/year if greater), rate is 16.5% regardless of sector. "Relevant goods" excludes: capital goods over GBP 2,000, food/drink for staff, vehicles/fuel/vehicle parts. Under FRS, input VAT on capital goods costing GBP 2,000 or more (incl. VAT) CAN be reclaimed separately in Box 4.

### 5.11 Cash accounting scheme (VAT Regulations 1995 reg 56-65)

Account for VAT based on date of payment, not invoice date. Entry: estimated taxable turnover <= GBP 1,350,000. Exit: GBP 1,600,000. Built-in bad debt relief — no output VAT due on unpaid invoices.

### 5.12 Filing deadlines and penalties (Finance Act 2021, from Jan 2023)

Late submission: points-based. Quarterly filers: penalty threshold at 4 points (GBP 200 per late return once threshold reached). Points expire after 12 months of compliance. Late payment: no penalty for 1-15 days late; 2% of outstanding VAT at day 16-30; additional 2% at day 31+ plus daily rate of 4% per annum. Late payment interest: Bank of England base rate + 2.5%.

### 5.13 MTD requirements (all VAT-registered businesses since April 2022)

Must keep digital records, maintain digital links between software systems (no manual re-keying), and file via MTD-compatible software. HMRC's basic online portal is NOT compliant with MTD.

---

## Section 6 — Tier 2 catalogue (compressed)

For each ambiguity type: pattern, why the bank statement is insufficient, conservative default, question for the structured form.

### 6.1 Vehicle costs (fuel — business or private?)

*Pattern:* BP, SHELL, ESSO, TEXACO, TESCO FUEL, ASDA FUEL, fuel receipts. *Why insufficient:* vehicle type and business-use proportion unknown. If car with any private use → fuel input VAT blocked unless fuel scale charge applied. If van or commercial vehicle used exclusively for business → fully deductible. *Default:* 0% recovery. *Question:* "Is this fuel for a car (with private use — blocked) or a commercial vehicle used exclusively for business? Do you apply the fuel scale charge?"

### 6.2 Entertainment (client entertaining — blocked in UK)

*Pattern:* any named restaurant, cafe, bar, catering, hospitality. *Why insufficient:* client entertainment is blocked. Staff entertainment may be recoverable. Overseas customer entertainment IS recoverable. *Default:* block. *Question:* "Was this (a) entertaining a UK client/supplier (blocked), (b) entertaining an overseas customer (recoverable), or (c) a staff event (recoverable if not excessive)?"

### 6.3 Home office (electricity/gas — 5% domestic rate, but what % is office?)

*Pattern:* energy supplier names, BRITISH GAS, EDF, OCTOPUS, etc. *Why insufficient:* business proportion unknown. Domestic fuel is 5% VAT, but only the business-use percentage is recoverable. *Default:* 0% if mixed use without declared proportion, 100% if confirmed dedicated business premises. *Question:* "Is this a home office or a dedicated business premises? If home office, what percentage of the property is used exclusively for business? (Typical range: 10-25%)"

### 6.4 Cash withdrawals

*Pattern:* ATM, CASH WITHDRAWAL, CASHPOINT. *Why insufficient:* unknown what cash was spent on. *Default:* exclude as owner drawing. *Question:* "What was the cash used for?"

### 6.5 Amazon/eBay (business or personal?)

*Pattern:* AMAZON, AMAZON.CO.UK, AMAZON MARKETPLACE, AMZN, EBAY. *Why insufficient:* could be business stock/supplies or personal purchases. Amazon UK charges 20% VAT on most items. *Default:* block (personal). *Question:* "Was this a business purchase? If so, what was bought and do you have a VAT invoice?"

### 6.6 Mobile phone (business % unknown)

*Pattern:* VODAFONE, EE, THREE, O2, GiffGaff, MOBILE. *Why insufficient:* if the contract is in the business name, full input VAT is recoverable even with some private use. If personal contract used partly for business, only business proportion is recoverable. *Default:* 0% recovery (personal contract assumed). *Question:* "Is this a business contract in the business name, or a personal phone used for business?"

### 6.7 FRS Limited Cost Trader test (did goods spend exceed 2%?)

*Pattern:* any FRS client. *Why insufficient:* bank statement shows total spend but not whether individual purchases are "relevant goods" vs services/excluded items. *Default:* LCT at 16.5% (most conservative). *Question:* "For the FRS Limited Cost Trader test: how much did you spend on goods (physical items used exclusively for business, excluding capital goods over GBP 2,000, food/drink for staff, vehicles/fuel/vehicle parts) this quarter?"

### 6.8 Round-number incoming transfers from owner-named counterparties

*Pattern:* large round credit from a name matching the client's name. *Why insufficient:* could be a customer sale, owner injection, or family loan. *Default:* exclude as owner injection. *Question:* "The GBP X transfer from [name] — is this a customer payment, your own money going in, or a loan?"

### 6.9 Incoming transfers from individual names (not owner)

*Pattern:* incoming from private-looking counterparties. *Why insufficient:* could be B2C sale, B2B sale paid from personal account, refund. *Default:* domestic B2C sale at 20%, Box 6/1. *Question:* "For each: was it a sale? Business or consumer customer?"

### 6.10 Outgoing transfers to individuals

*Pattern:* outgoing to private-looking names. *Why insufficient:* could be contractor with invoice, wages, refund, drawings. *Default:* exclude as drawings. *Question:* "Was this a contractor you paid with an invoice, wages, a refund to a customer, or a personal transfer?"

### 6.11 Rent payments

*Pattern:* monthly RENT, LEASE to a landlord-sounding counterparty. *Why insufficient:* commercial vs residential, whether landlord has opted to tax. *Default:* no VAT, no deduction (residential default). *Question:* "Is this a commercial property? Does the landlord charge VAT on the rent (they will only charge VAT if they have opted to tax the property)?"

### 6.12 Foreign hotel and accommodation (non-UK)

*Pattern:* hotel or accommodation charged abroad. *Why insufficient:* place of supply is the location of the property — non-UK VAT paid at source, not recoverable as UK input tax. *Default:* exclude from input VAT. *Question:* "Was this a business trip?" (For income tax records, the expense may still be deductible.)

### 6.13 Platform sales (Amazon Seller, eBay, Etsy)

*Pattern:* incoming from Amazon Payments, Etsy Payments, PayPal, Stripe — settlement payouts. *Why insufficient:* aggregated settlement may include multi-country buyer mix. *Default:* treat gross as Box 6/1 at 20%. Platform fees as separate reverse charge (IE/US entity). *Question:* "Do you sell to buyers outside the UK? Total overseas sales for the year? Do you sell on Amazon EU marketplaces?"

---

## Section 7 — Excel working paper template (UK-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the UK-specific overlay.

### Sheet "Transactions"

Columns A-L per the base. Column H ("Box code") accepts only valid UK VAT100 box codes: 1, 2, 4, 6, 7, 8, 9. Use blank for excluded transactions. For reverse-charge transactions, enter the output and input boxes separated by a slash (e.g. "1+6/4+7").

### Sheet "Box Summary"

One row per box. Column A is the box number, column B is the description, column C is the value computed via formula. Mandatory rows:

```
| 1  | VAT due on sales and other outputs | =SUMIFS for output VAT entries |
| 2  | VAT due on EU acquisitions (legacy) | Generally 0 post-Brexit |
| 3  | Total VAT due | =Box1+Box2 |
| 4  | VAT reclaimed on purchases | =SUMIFS for input VAT entries |
| 5  | Net VAT to pay or reclaim | =Box3-Box4 |
| 6  | Total value of sales ex VAT | =SUMIFS for all output net values |
| 7  | Total value of purchases ex VAT | =SUMIFS for all input net values |
| 8  | Supplies of goods to EU ex VAT | =SUMIFS for EU goods exports |
| 9  | Acquisitions of goods from EU ex VAT | =SUMIFS for EU goods imports |
```

### Sheet "Return Form"

Final VAT100-ready figures. The bottom-line cell is Box 5:

```
IF Box 5 > 0: taxpayer PAYS this amount to HMRC
IF Box 5 < 0: HMRC REFUNDS this amount to the taxpayer
```

### FRS Sheet (if applicable)

If client is on FRS, add a separate sheet:

```
| Gross turnover (VAT-inclusive) | =SUM of all VAT-inclusive sales |
| Sector rate | [from Section 1 table] |
| LCT test: goods spend | [manual entry] |
| LCT test: 2% of gross | =Gross*2% |
| LCT status | =IF(goods_spend < MAX(2%_of_gross, 250), "LCT", "Not LCT") |
| Applied rate | =IF(LCT, 16.5%, sector_rate) |
| VAT payable (Box 1) | =Gross * applied_rate |
| Capital goods input VAT (Box 4) | [if any item >= GBP 2,000 incl VAT] |
| Box 5 | =Box1 - Box4 |
```

### Color and formatting conventions

Per the xlsx skill: blue for hardcoded values from the bank statement, black for formulas, green for cross-sheet references, yellow background for any row where Default? = "Y".

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/uk-vat-<period>-working-paper.xlsx
```

Check the JSON output. If `status` is `errors_found`, fix the formulas and re-run. If `status` is `success`, present via `present_files`.

---

## Section 8 — UK bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these UK-specific patterns.

**CSV format conventions.** UK banks export in various formats. Barclays: CSV with DD/MM/YYYY. HSBC UK: CSV or QIF. Lloyds: CSV with DD/MM/YYYY. NatWest: CSV or OFX. Starling: CSV with ISO dates. Monzo: CSV with ISO dates. Tide: CSV with DD/MM/YYYY. Common columns: Date, Description/Narrative, Debit/Credit or Amount, Balance. Always confirm which format before parsing.

**Internal transfers and exclusions.** Own-account transfers between the client's bank accounts. Labelled "transfer to savings", "internal transfer", "own account". Always exclude.

**Sole trader drawings.** A self-employed sole trader cannot pay themselves wages. Any transfer to their personal account is a drawing — exclude from VAT.

**Refunds and reversals.** Identify by "refund", "reversal", "chargeback", "credit note". Book as a negative in the same box as the original transaction. Correction is in the period the refund is booked, not by amending the original period.

**Foreign currency transactions.** Convert to GBP at the transaction date rate. Use the HMRC exchange rate for the period, or the rate shown on the bank statement. Note the rate used in the Transactions sheet column L (Notes).

**Cryptic card transactions.** Card purchases with only a merchant terminal code or card acquirer reference. If the counterparty cannot be identified from the description, ask the client. Do not classify unidentified transactions.

**Direct debit references.** Many UK bank statements show direct debits with only a mandate reference number. Cross-reference with the client's known suppliers. Common: energy suppliers, telecoms, HMRC, insurance.

---

## Section 9 — Onboarding fallback (only when inference fails)

The workflow in `vat-workflow-base` Section 1 mandates inferring the client profile from the data first and only confirming with the client as a fallback. The questionnaire below is a fallback — ask only the questions the data could not answer.

### 9.1 Entity type and trading name
*Inference rule:* sole trader names match the account holder name; company names end in "Ltd", "Limited", "LLP", "PLC". *Fallback question:* "Are you a self-employed sole trader, a limited company, or a partnership?"

### 9.2 VAT scheme
*Inference rule:* if the client mentions FRS, flat rate, or a percentage of turnover, they are FRS. If they mention cash basis or payment dates, they are cash accounting. Otherwise assume standard accrual. *Fallback question:* "Which VAT scheme are you on: standard accounting, Flat Rate Scheme, cash accounting, or annual accounting?"

### 9.3 VAT number
*Inference rule:* GB VAT numbers sometimes appear in invoice descriptions or payment references. *Fallback question:* "What is your VAT registration number? (9-digit GB number)"

### 9.4 Filing period
*Inference rule:* first and last transaction dates on the bank statement. Standard is quarterly. *Fallback question:* "Which VAT quarter does this cover? (e.g. April-June 2025)"

### 9.5 Industry and sector
*Inference rule:* counterparty mix, sales description patterns, invoice descriptions. IT, consultancy, construction, retail, hospitality are recognisable. Important for FRS sector rate. *Fallback question:* "In one sentence, what does the business do?"

### 9.6 FRS sector (if applicable)
*Inference rule:* infer from 9.5. *Fallback question:* "If you are on the Flat Rate Scheme, which HMRC sector category applies to your business?"

### 9.7 Exempt supplies
*Inference rule:* presence of financial/insurance/educational/residential rental income. *Fallback question:* "Do you make any VAT-exempt sales (financial services, insurance, education, health, residential lettings)?" If yes and non-de-minimis, R-UK-1 fires.

### 9.8 Construction / CIS
*Inference rule:* CIS references in payment descriptions, construction-related counterparties. *Fallback question:* "Are you registered under the Construction Industry Scheme (CIS)? Do you make or receive supplies of construction services?" If complex, R-UK-4 fires.

### 9.9 Prior period position
*Inference rule:* not inferable from a single period statement. Always ask. *Question:* "Do you have any underpayment or overpayment carried forward from the previous VAT period?"

### 9.10 Overseas customers
*Inference rule:* foreign IBANs or foreign currency on incoming, foreign-name customers. *Fallback question:* "Do you have customers outside the UK? Are they businesses (B2B) or consumers (B2C)?"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the Malta v2.0 architecture (vat-workflow-base + country skill). It supersedes v1.0 (2025, standalone monolithic skill). The UK-specific content (box mappings, rates, thresholds, blocked categories, FRS percentages) requires validation by a UK-qualified accountant (ACA/ACCA/CTA).

### Sources

**Primary legislation:**
1. Value Added Tax Act 1994 (VATA 1994) — legislation.gov.uk
2. VAT Regulations 1995 (SI 1995/2518)
3. Finance Act 2024; Finance Act 2025
4. The Value Added Tax (Flat Rate Scheme) Order 2004
5. The VAT (Input Tax) Order 1992 (SI 1992/3222)
6. Finance Act 2017 (Limited Cost Trader provisions)
7. The Value Added Tax (Section 55A) (Specified Services and Excepted Supplies) Order 2020 (CIS reverse charge)
8. Making Tax Digital (VAT) Regulations 2018 (SI 2018/261)
9. Finance Act 2021 (new penalty regime from January 2023)

**HMRC guidance:**
10. HMRC VAT Notice 700: The VAT Guide
11. HMRC VAT Notice 733: Flat Rate Scheme for small businesses
12. HMRC VAT Notice 731: Cash accounting
13. HMRC VAT Notice 732: Annual accounting
14. HMRC VAT Notice 735: Bad debt relief
15. HMRC VAT Notice 48: Extra-statutory concessions (business entertainment of overseas customers)
16. HMRC VAT Notice 708: Buildings and construction
17. HMRC VAT reverse charge for construction guidance

**Other:**
18. HMRC exchange rates — https://www.gov.uk/government/collections/exchange-rates-for-customs-and-vat
19. HMRC FRS trade sectors and percentages — https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay
20. HMRC MTD-compatible software list — https://www.gov.uk/guidance/find-software-thats-compatible-with-making-tax-digital-for-vat

### Known gaps

1. The supplier pattern library in Section 3 covers the most common UK and international counterparties but does not cover every regional supplier or SME.
2. The worked examples are drawn from a hypothetical IT consultant. They do not cover construction, retail, e-commerce, hospitality, or manufacturing specifically. A v2.1 should add sector-specific worked examples.
3. CIS reverse charge is simplified. The end-user exemption and intermediary supplier rules are highly fact-specific — R-UK-4 fires for complex cases.
4. Import VAT and postponed VAT accounting (PVA) for goods imports are not covered in detail. A future version should add import scenarios.
5. Partial exemption annual adjustment calculations are outside scope — R-UK-1 fires.
6. Red flag thresholds (GBP 5,000 single transaction, GBP 400 tax-delta, GBP 10,000 absolute position) are conservative starting values — not empirically calibrated.
7. Northern Ireland Protocol: Northern Ireland has a unique position for goods (still follows EU rules for goods). This skill treats NI as part of the UK for services but acknowledges that goods trade between NI and EU may require different treatment.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with Malta v2.0 architecture (vat-workflow-base + country skill). Quick reference moved to top (Section 1) with conservative defaults and FRS table. Supplier pattern library restructured as literal lookup tables (Section 3, 12 sub-tables). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue restructured to compressed format (Section 6, 13 items). Excel working paper specification added (Section 7). Bank statement reading guide added (Section 8). Onboarding moved to fallback role with inference rules (Section 9). Reference material moved to bottom (Section 10). Post-Brexit treatment unified: EU and non-EU suppliers both trigger reverse charge. Refusal catalogue added (R-UK-1 through R-UK-5). Companion skill reference added (vat-workflow-base v0.1).
- **v1.0 (2025):** Initial skill. Standalone monolithic document covering UK VAT Act 1994, box mappings, reverse charge mechanics, blocked categories, edge case registry, and test suite.

### Self-check (v2.0 of this document)

1. Quick reference at top with box table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 12 sub-tables).
3. Worked examples drawn from hypothetical IT consultant: yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 13 rules).
5. Tier 2 catalogue compressed with inference rules: yes (Section 6, 13 items).
6. Excel template specification with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only, inference rules first: yes (Section 9, 10 items).
8. All 5 UK-specific refusals present: yes (Section 2, R-UK-1 through R-UK-5).
9. Reference material at bottom: yes (Section 10).
10. Entertainment block explicit (overseas customer exception noted): yes (Section 5.8 + Example 3).
11. Motor vehicle block explicit: yes (Section 5.8).
12. FRS Limited Cost Trader test explicit with 16.5% trap: yes (Section 5.10 + Example 6).
13. Post-Brexit EU treatment unified with non-EU: yes (Section 3 header note + Section 5.6).
14. Key rate traps (chocolate biscuits vs cakes, hot takeaway vs cold): yes (Section 5.3).
15. CIS reverse charge covered with refusal for complex cases: yes (Section 5.7 + R-UK-4).

## End of UK VAT Return Skill v2.0

This skill is incomplete without the companion file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a VAT100 without both files loaded.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
