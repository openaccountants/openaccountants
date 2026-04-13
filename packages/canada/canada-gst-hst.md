---
name: canada-gst-hst
description: Use this skill whenever asked to prepare, review, or classify transactions for a Canadian GST/HST return (Form GST34) for a self-employed individual or small business in Canada. Trigger on phrases like "prepare GST return", "file HST", "Canadian sales tax", "GST/HST return", "Form GST34", "input tax credits", "ITC claim", or any request involving Canadian GST/HST filing. Also trigger when classifying transactions for GST/HST purposes from bank statements, invoices, or other source data. This skill covers federal GST and harmonized HST provinces only under the regular method. Quebec QST, Saskatchewan PST, Manitoba RST, British Columbia PST, Quick Method, and simplified method for charities are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any Canadian GST/HST work.
version: 2.0
---

# Canada GST/HST Return Skill (Form GST34) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

| Field | Value |
|---|---|
| Country | Canada |
| Federal GST rate | 5% |
| HST rates by province | ON 13%, NS 14% (effective Apr 1 2025), NB 15%, NL 15%, PE 15% |
| GST-only provinces | AB, BC, SK, MB, QC, NT, NU, YT (5% GST; BC/SK/MB/QC have separate provincial sales taxes) |
| Zero rate | 0% (basic groceries, prescription drugs, medical devices, exports) |
| Exempt | Financial services, residential rent, most health/dental/legal aid, childcare |
| Return form | GST34 (GST/HST Return for Registrants) |
| Filing portal | CRA My Business Account (canada.ca) |
| Authority | Canada Revenue Agency (CRA) |
| Currency | CAD only |
| Filing frequencies | Annual (taxable supplies <= $1.5M), Quarterly ($1.5M–$6M), Monthly (> $6M or voluntary election) |
| Deadline | Monthly/quarterly: 1 month after period end; Annual: 3 months after fiscal year end (individuals: June 15 but payment due April 30) |
| Small supplier threshold | $30,000 in any single calendar quarter or in the last four consecutive calendar quarters (ETA s.148) |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Community |
| Validation date | April 2026 |

**Key GST34 lines:**

| Line | Meaning |
|---|---|
| 101 | Total sales and other revenue (before GST/HST) |
| 103 | GST/HST collected or collectible |
| 104 | Adjustments to GST/HST (e.g., bad debt recovery, change-in-use) |
| 105 | Total GST/HST and adjustments (= 103 + 104) |
| 106 | Input tax credits (ITCs) |
| 107 | Adjustments to ITCs (e.g., recapture of ITCs on large business inputs — expired 2018) |
| 108 | Total ITCs and adjustments (= 106 + 107) |
| 109 | Net tax (= 105 − 108; positive = owing, negative = refund) |
| 110 | Instalments paid |
| 111 | Rebates claimed |
| 112 | Total other credits (= 110 + 111) |
| 113 | Balance (= 109 − 112; positive = amount owing) |
| 114 | Refund claimed |
| 115 | Amount owing |

**GST/HST rates by province (complete):**

| Province/Territory | Rate | Components | Effective |
|---|---|---|---|
| Alberta (AB) | 5% | GST only | — |
| British Columbia (BC) | 5% GST + 7% PST | Separate PST (not on GST34) | — |
| Manitoba (MB) | 5% GST + 7% RST | Separate RST (not on GST34) | — |
| New Brunswick (NB) | 15% HST | Harmonized | — |
| Newfoundland & Labrador (NL) | 15% HST | Harmonized | — |
| Northwest Territories (NT) | 5% | GST only | — |
| Nova Scotia (NS) | 14% HST | Harmonized | Apr 1, 2025 |
| Nunavut (NU) | 5% | GST only | — |
| Ontario (ON) | 13% HST | Harmonized | — |
| Prince Edward Island (PE) | 15% HST | Harmonized | — |
| Quebec (QC) | 5% GST + 9.975% QST | Separate QST (filed with Revenu Quebec) | — |
| Saskatchewan (SK) | 5% GST + 6% PST | Separate PST (not on GST34) | — |
| Yukon (YT) | 5% | GST only | — |

**Conservative defaults — Canada-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | HST at rate of province of supply (default ON 13% if province unknown) |
| Unknown GST/HST status of a purchase | Not eligible for ITC |
| Unknown province of supply | Province of registration |
| Unknown business-use proportion (vehicle, phone, home office) | 0% ITC |
| Unknown whether personal or business expense | Personal (no ITC) |
| Unknown blocked-input status (club dues, personal) | Blocked |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | CAD 5,000 |
| HIGH tax-delta on a single conservative default | CAD 400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net tax position | CAD 10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Canadian or international business bank: RBC, TD, Scotiabank, BMO, CIBC, National Bank, Desjardins, Tangerine, Simplii, EQ Bank, Revolut Business, Wise Business, or any other.

**Recommended** — sales invoices for the period (especially for zero-rated exports and interprovincial supplies), purchase invoices for any ITC claim above CAD 400, the client's GST/HST Business Number (BN format: 123456789RT0001).

**Ideal** — complete sales journal, purchase journal, prior period GST34, Quick Method election (if applicable — but then R-CA-3 fires).

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement is available at all, hard stop. If bank statement only without invoices, proceed but record in reviewer brief: "This GST34 was produced from bank statement alone. The reviewer must verify that ITC claims above CAD 400 are supported by compliant invoices containing the supplier's BN and that place-of-supply determinations are correct."

### Canada-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-CA-1 — Quebec QST.** *Trigger:* client is in Quebec or asks about QST filing. *Message:* "Quebec Sales Tax (QST) is administered by Revenu Quebec and filed separately from the federal GST return. This skill covers federal GST/HST (Form GST34) only. For QST, please use a CPA familiar with Quebec tax administration."

**R-CA-2 — Provincial sales tax (BC PST, SK PST, MB RST).** *Trigger:* client asks about BC PST, Saskatchewan PST, or Manitoba RST filing. *Message:* "Provincial sales taxes (BC PST, SK PST, MB RST) are separate from GST/HST and filed with the respective provincial authority. This skill covers the federal GST/HST return only."

**R-CA-3 — Quick Method.** *Trigger:* client has elected the Quick Method of accounting (GST74). *Message:* "The Quick Method calculates GST/HST remittance as a percentage of GST/HST-included revenue rather than tracking actual ITCs. This skill covers the regular method only. For Quick Method returns, apply the prescribed remittance rate for your sector and province."

**R-CA-4 — Simplified method for charities/NPOs.** *Trigger:* client is a registered charity, NPO, or public service body using the simplified method or net tax calculation. *Message:* "Charities, NPOs, and public service bodies have special GST/HST rules including the net tax calculation and public service body rebates. Out of scope."

**R-CA-5 — First Nations exemptions.** *Trigger:* client asks about tax exemptions under the Indian Act or supplies on reserve. *Message:* "First Nations tax exemptions under the Indian Act (section 87) have specific rules that are outside the scope of this skill. Please consult a tax professional experienced in Indigenous tax matters."

**R-CA-6 — GST/HST groups (closely related corporations).** *Trigger:* client is part of a GST/HST group election under ETA s.156. *Message:* "Closely related group elections under s.156 involve intercompany supply rules that are out of scope. Please use a CPA."

**R-CA-7 — Non-resident simplified registration.** *Trigger:* non-resident registrant under the simplified registration framework. *Message:* "The simplified registration framework for non-resident digital economy businesses has different rules. Out of scope."

**R-CA-8 — Real property transactions.** *Trigger:* client is buying/selling real property (land, buildings) with self-supply or change-of-use implications. *Message:* "Real property transactions involve self-supply rules (s.191), change-of-use rules, and rebate calculations that are too fact-sensitive for this skill. Please use a CPA."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name. If multiple patterns match, use the most specific.

### 3.1 Canadian banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| RBC, ROYAL BANK OF CANADA | EXCLUDE for bank charges/fees | ETA Schedule V, Part VII: financial service, exempt |
| TD, TORONTO-DOMINION, TD CANADA TRUST | EXCLUDE for bank charges/fees | Same |
| SCOTIABANK, BANK OF NOVA SCOTIA | EXCLUDE for bank charges/fees | Same |
| BMO, BANK OF MONTREAL | EXCLUDE for bank charges/fees | Same |
| CIBC, CANADIAN IMPERIAL | EXCLUDE for bank charges/fees | Same |
| NATIONAL BANK, BNC, BANQUE NATIONALE | EXCLUDE for bank charges/fees | Same |
| DESJARDINS, CAISSE POPULAIRE | EXCLUDE for bank charges/fees | Same |
| TANGERINE, SIMPLII, EQ BANK | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, INTERET | EXCLUDE | Interest income/expense, exempt |
| MORTGAGE, HYPOTHEQUE, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 Canadian government and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| CRA, CANADA REVENUE AGENCY, RECEIVER GENERAL | EXCLUDE | Tax payment (GST remittance, income tax instalment) |
| REVENU QUEBEC | EXCLUDE | QST or income tax payment |
| CPP, CANADA PENSION PLAN | EXCLUDE | Pension contribution, not a supply |
| EI, EMPLOYMENT INSURANCE | EXCLUDE | Employment insurance premium |
| WSIB, WCB, CNESST | EXCLUDE | Workers compensation |
| SERVICE CANADA, SERVICE ONTARIO | EXCLUDE | Government fees, sovereign act |
| CITY OF, VILLE DE, MUNICIPAL | EXCLUDE | Municipal tax/fee |

### 3.3 Canadian utilities

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| HYDRO ONE, TORONTO HYDRO, BC HYDRO, HYDRO-QUEBEC | Taxable | GST/HST at provincial rate | Electricity — overhead |
| ENBRIDGE, FORTISBC, ATCO GAS | Taxable | GST/HST at provincial rate | Gas — overhead |
| TELUS | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| ROGERS, ROGERS COMMUNICATIONS | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| BELL, BELL CANADA, BELL MOBILITY | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| SHAW, COGECO, VIDEOTRON | Taxable | GST/HST at provincial rate | Telecoms — overhead |
| FIDO, KOODO, VIRGIN PLUS, FREEDOM MOBILE | Taxable | GST/HST at provincial rate | Telecoms — overhead |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| MANULIFE, SUN LIFE, GREAT-WEST LIFE, CANADA LIFE | EXCLUDE | Insurance, exempt (ETA Schedule V, Part VII) |
| INTACT, AVIVA, DESJARDINS ASSURANCE | EXCLUDE | Same |
| CO-OPERATORS, WAWANESA, ECONOMICAL | EXCLUDE | Same |
| INSURANCE, ASSURANCE | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| CANADA POST, POSTES CANADA | EXCLUDE for standard letter mail | | Exempt (ETA Schedule V, Part VII.1) |
| CANADA POST (courier, Xpresspost, Priority) | Taxable | GST/HST | Non-universal services are taxable |
| PUROLATOR | Taxable | GST/HST | Express courier |
| FEDEX CANADA, UPS CANADA, DHL CANADA | Taxable | GST/HST | Courier services |
| CANPAR, DICOM, LOOMIS | Taxable | GST/HST | Courier services |

### 3.6 Transport

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| VIA RAIL | Taxable | GST/HST | Domestic passenger rail |
| GO TRANSIT, TTC, STM, TRANSLINK, OC TRANSPO | EXCLUDE or zero-rated | | Municipal transit — zero-rated per ETA Schedule VI, Part VII |
| UBER CANADA | Taxable | GST/HST | Ride-sharing; platform is GST-registered |
| LYFT | Taxable | GST/HST | Same |
| AIR CANADA (international) | Zero-rated | 0% | International transport — Schedule VI, Part VII |
| AIR CANADA (domestic) | Taxable | GST/HST | Domestic air |
| WESTJET (international) | Zero-rated | 0% | International |
| WESTJET (domestic) | Taxable | GST/HST | Domestic air |
| ENTERPRISE, HERTZ, AVIS, BUDGET (car rental) | Taxable | GST/HST at location rate | Car rental — ITC restricted if personal use |

### 3.7 Food retail (generally zero-rated basic groceries — but personal)

| Pattern | Treatment | Notes |
|---|---|---|
| TIM HORTONS, TIMS | Default BLOCK ITC | Restaurant/prepared food is taxable at GST/HST, but personal unless hospitality business |
| STARBUCKS, MCDONALDS, SUBWAY, A&W | Default BLOCK ITC | Same — prepared food/beverages are taxable but likely personal |
| LOBLAWS, NO FRILLS, REAL CANADIAN, SUPERSTORE | Default BLOCK ITC | Grocery — mix of zero-rated and taxable items; personal provisioning default |
| METRO, SOBEYS, SAFEWAY, IGA, SAVE-ON-FOODS | Default BLOCK ITC | Same |
| COSTCO, WALMART (grocery) | Default BLOCK ITC | Mixed supply — personal default |
| CANADIAN TIRE (non-food) | Taxable | GST/HST — ITC eligible if business purpose confirmed |

### 3.8 SaaS — non-resident suppliers (self-assessment under ETA s.218)

Non-resident digital services suppliers to Canadian businesses: the Canadian registrant must self-assess GST/HST on imported taxable supplies under ETA s.218. Report on Line 405 of GST34 and claim offsetting ITC on Line 106.

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) or Google LLC (US) | Self-assess GST/HST s.218 | Report on Line 405, claim ITC Line 106 |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | Self-assess GST/HST s.218 | Same |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | Self-assess GST/HST s.218 | Same |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | Self-assess GST/HST s.218 | Same |
| NOTION | Notion Labs Inc (US) | Self-assess GST/HST s.218 | Same |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | Self-assess GST/HST s.218 | Same |
| OPENAI, CHATGPT | OpenAI Inc (US) | Self-assess GST/HST s.218 | Same |
| FIGMA | Figma Inc (US) | Self-assess GST/HST s.218 | Same |
| CANVA | Canva Pty Ltd (AU) | Self-assess GST/HST s.218 | Same |
| SLACK | Slack Technologies Ltd (various) | Self-assess GST/HST s.218 | Check if registered in Canada |
| ZOOM | Zoom Video Communications Inc (US) | Self-assess GST/HST s.218 | Same |
| ATLASSIAN | Atlassian Pty Ltd (AU) | Self-assess GST/HST s.218 | Same |
| DROPBOX | Dropbox Inc (US) | Self-assess GST/HST s.218 | Same |

**Note:** Many non-resident digital services suppliers have registered for GST/HST under the simplified registration framework (effective July 2021) and now charge GST/HST directly. If the invoice shows GST/HST charged with a valid BN, treat as a regular domestic purchase with ITC. If no GST/HST is charged, self-assess under s.218.

### 3.9 Canadian SaaS / domestic suppliers (ITC-eligible)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| SHOPIFY | Taxable domestic | GST/HST (ON entity, 13% HST) | Platform subscription — ITC eligible |
| STRIPE PAYMENTS CANADA | Taxable domestic or exempt | Check invoice | Transaction fees may be exempt financial service; subscription taxable |
| WEALTHSIMPLE | EXCLUDE (exempt) | — | Financial service |
| FRESHBOOKS | Taxable domestic | GST/HST | Accounting software |
| WAVE FINANCIAL | Taxable domestic | GST/HST | Accounting software (now owned by H&R Block) |
| HOOTSUITE | Taxable domestic | GST/HST | Social media management |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| SQUARE, MONERIS, GLOBAL PAYMENTS | Check invoice | Transaction fees exempt; hardware/subscription taxable |
| INTERAC | EXCLUDE (exempt) | Interac fees are financial services |

### 3.11 CRA payments and refunds

| Pattern | Treatment | Notes |
|---|---|---|
| CRA GST PAYMENT, RECEIVER GENERAL GST | EXCLUDE | GST remittance — not a supply |
| CRA INCOME TAX, INSTALMENT PAYMENT | EXCLUDE | Income tax — not a supply |
| CRA REFUND, GST REFUND | EXCLUDE | Government refund — not a supply |
| CRA CEBA, CEWS, CERS | EXCLUDE | Government subsidy — not a supply (but may have GST implications on repayment) |

### 3.12 Professional services (Canada)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| CPA, CHARTERED PROFESSIONAL ACCOUNTANT | Taxable | GST/HST | Always ITC-eligible |
| LAWYER, LAW OFFICE, BARRISTERS | Taxable | GST/HST | ITC-eligible if business purpose |
| NOTARY, NOTAIRE | Taxable | GST/HST | ITC-eligible if business purpose |
| CONSULTANT, CONSULTING | Taxable | GST/HST | ITC-eligible if business purpose |

### 3.13 Payroll (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| PAYROLL, SALARY, WAGES | EXCLUDE | Wages — outside GST/HST scope |
| CPP CONTRIBUTION | EXCLUDE | Pension contribution |
| EI PREMIUM | EXCLUDE | Employment insurance |
| CERIDIAN, ADP, PAYWORKS | EXCLUDE for payroll runs | Payroll processing fee itself may be taxable |

### 3.14 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| RENT, LOYER (commercial) | Taxable | Commercial lease — GST/HST on rent, ITC eligible |
| RENT, LOYER (residential) | EXCLUDE | Residential lease exempt (ETA Schedule V, Part I) |
| CONDO FEES, STRATA FEES | EXCLUDE if residential | Residential condo fees exempt |
| PROPERTY TAX, MUNICIPAL TAX | EXCLUDE | Government levy, not a supply |

### 3.15 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFER, E-TRANSFER (own accounts) | EXCLUDE | Internal movement |
| INTERAC E-TRANSFER (to self) | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Dividend payment, out of scope |
| LOAN REPAYMENT | EXCLUDE | Loan principal, out of scope |
| ATM WITHDRAWAL | TIER 2 — ask | Default exclude; ask what cash was spent on |
| OWNER DRAW, SHAREHOLDER LOAN | EXCLUDE | Owner withdrawal |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of an Ontario-based self-employed software consultant.

### Example 1 — Non-resident SaaS, self-assessment (Notion)

**Input line:**
`2026-04-03 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; CAD 21.89`

**Reasoning:**
Notion Labs Inc is a US entity (Section 3.8). No GST/HST on the invoice. This is an imported taxable supply under ETA s.218. The registrant must self-assess GST/HST at the applicable rate. Client is in Ontario → 13% HST. Self-assess HST of CAD 2.85 (21.89 * 0.13). Report on Line 405 (tax on imported supplies) and claim offsetting ITC on Line 106. Net effect zero.

**Output:**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line (self-assess) | Line (ITC) | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-04-03 | NOTION LABS INC | -21.89 | -21.89 | 2.85 | 13% HST | 405 | 106 | N | — | — |

### Example 2 — Domestic purchase with HST (Shopify)

**Input line:**
`2026-04-10 ; SHOPIFY COMMERCE INC ; DEBIT ; Monthly plan ; -49.00 ; CAD`

**Reasoning:**
Shopify is an Ontario-headquartered Canadian company. They charge 13% HST. The CAD 49.00 is the HST-inclusive price. Net = 49.00 / 1.13 = 43.36. HST = 5.64. Full ITC eligible on Line 106 for business software.

**Output:**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-10 | SHOPIFY | -49.00 | -43.36 | -5.64 | 13% HST | 106 | N | — | — |

### Example 3 — Entertainment, restricted ITC

**Input line:**
`2026-04-15 ; THE KEG STEAKHOUSE ; DEBIT ; Client dinner ; -285.00 ; CAD`

**Reasoning:**
Restaurant meal. Under ETA s.67.1 (via Income Tax Act cross-reference), meals and entertainment expenses are limited to 50% for income tax purposes. However, the full GST/HST ITC is claimable on the portion that is deductible for income tax (i.e., 50% of the GST/HST). Conservative default: block entirely as likely personal. If confirmed as business entertainment, 50% of ITC is claimable.

**Output:**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-15 | THE KEG STEAKHOUSE | -285.00 | -285.00 | 0 | — | — | Y | Q1 | "Meals/entertainment: blocked (conservative)" |

### Example 4 — Capital asset (over $30,000)

**Input line:**
`2026-04-18 ; APPLE STORE YORKDALE ; DEBIT ; MacBook Pro 16 ; -3,729.00 ; CAD`

**Reasoning:**
CAD 3,729 including HST. Net = 3,729 / 1.13 = 3,300.88. HST = 428.12. This is a capital asset used in the business. Full ITC is claimable on Line 106. Capital assets are reported on Line 106 the same as current expenses in Canada (no separate capital line on GST34). However, if the asset is a passenger vehicle exceeding the CCA Class 10.1 ceiling (CAD 37,000 + tax for 2025/2026), the ITC is limited to the ceiling amount.

**Output:**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-18 | APPLE STORE | -3,729.00 | -3,300.88 | -428.12 | 13% HST | 106 | N | — | — |

### Example 5 — Export sale (zero-rated)

**Input line:**
`2026-04-22 ; ACME CORP USA ; CREDIT ; Invoice CA-2026-018 IT consulting March ; +5,500.00 ; CAD`

**Reasoning:**
Incoming CAD 5,500 from a US company. The client provides IT consulting services to a non-resident. Under ETA Schedule VI, Part V, s.5, services performed for a non-resident who is not registered for GST/HST and not a consumer in Canada are zero-rated. Report as revenue on Line 101 but zero-rated (no GST/HST on Line 103). Full ITC recovery on related inputs is preserved.

**Output:**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-22 | ACME CORP USA | +5,500.00 | +5,500.00 | 0 | 0% | 101 (zero-rated) | Y | Q2 (HIGH) | "Verify non-resident status and zero-rating conditions" |

### Example 6 — Vehicle costs, restricted ITC

**Input line:**
`2026-04-28 ; PETRO-CANADA ; DEBIT ; Fuel ; -92.00 ; CAD`

**Reasoning:**
Fuel purchase. In Canada, there is no blanket block on vehicle expenses (unlike Malta). ITCs are claimable to the extent of business use. For a passenger vehicle, the taxpayer must track business vs personal kilometers. Conservative default: 0% ITC (personal use assumed). If the taxpayer maintains a logbook showing, say, 60% business use, 60% of the GST/HST is claimable.

**Output:**

| Date | Counterparty | Gross | Net | GST/HST | Rate | Line | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-28 | PETRO-CANADA | -92.00 | -92.00 | 0 | — | — | Y | Q3 | "Vehicle fuel: 0% ITC (no logbook). Provide km logbook for partial ITC." |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 GST at 5% (ETA s.165(1))

Federal component of all taxable supplies. Applies in GST-only provinces (AB, BC, SK, MB, NT, NU, YT). In these provinces, only 5% GST applies on the GST34. Provincial taxes (BC PST, SK PST, MB RST) are separate filings.

### 5.2 HST at harmonized rates (ETA s.165(2))

In harmonized provinces (ON 13%, NS 14%, NB 15%, NL 15%, PE 15%), the HST replaces GST. The full HST amount is reported on the GST34. There is no separate provincial filing for HST provinces.

### 5.3 Place of supply (SOR/2010-117)

The rate depends on where the supply is made. For tangible personal property: province where delivery occurs. For services: generally the province of the recipient's business address. For intangible personal property: province where the property may be used. Interprovincial supplies require transaction-level place-of-supply determination.

### 5.4 Zero-rated supplies (ETA Schedule VI)

Basic groceries (Part III), prescription drugs (Part I), medical devices (Part II), exports of goods (Part V), services to non-residents (Part V, s.5 — conditions apply), international transport (Part VII), agricultural products (Part IV), financial services to non-residents (Part IX). Zero-rated means 0% tax but full ITC eligibility on related inputs.

### 5.5 Exempt supplies (ETA Schedule V)

Financial services (Part VII), residential rent (Part I), health care services (Part II — but only listed services), educational services (Part III), childcare (Part IV), legal aid (Part V), public sector (Part VI). Exempt means no GST/HST charged and NO ITC on related inputs. If exempt supplies are significant → mixed-use apportionment required.

### 5.6 Input tax credits (ETA s.169)

ITCs are claimable on GST/HST paid on purchases used in commercial (taxable + zero-rated) activities. Documentation requirements (ETA Input Tax Credit Information Regulations): purchases under $30 need vendor name and amount; $30–$149.99 need vendor name, BN, date, amount, GST/HST; $150+ need all of the above plus purchaser name/address. Report on Line 106.

### 5.7 Self-assessment on imported taxable supplies (ETA s.218)

When a registrant receives a taxable supply from a non-resident who did not charge GST/HST: self-assess on Line 405 and claim offsetting ITC on Line 106. Net effect zero for fully taxable registrants. This is the Canadian equivalent of EU reverse charge.

### 5.8 Capital personal property / passenger vehicles (ETA s.201–202)

ITCs on passenger vehicles are limited by the Income Tax Act CCA ceiling (Class 10.1: $37,000 + tax for 2025/2026). For luxury vehicles, ITC is capped at GST/HST on the ceiling amount. Leased vehicles: ITC limited proportionally. Business-use percentage applies on top.

### 5.9 Blocked ITCs (ETA s.170)

- Club memberships (golf, fitness, social clubs) — ETA s.170(1)(a) — fully blocked
- Personal expenses — ETA s.170(1)(b) — fully blocked
- Gifts over $50 (except food/drink) — limited
- Passenger vehicles: not blocked per se but limited to business-use proportion and CCA ceiling

### 5.10 Meals and entertainment — 50% rule

ETA s.236(1) cross-references ITA s.67.1: the GST/HST ITC on meals and entertainment is limited to 50% of the GST/HST paid. This is not a full block — it is a 50% restriction. The 50% rule does NOT apply to: meals provided at a remote work camp, meals included in convention fees, meals provided for fundraising, or meals for which the full cost is reimbursed by the client.

### 5.11 Change in use — capital property (ETA s.195–199)

When a capital asset changes from business to personal use (or vice versa), a deemed supply/acquisition occurs. The registrant must self-assess or claim ITC based on the FMV at the time of change. Flag for reviewer.

### 5.12 Small supplier threshold (ETA s.148)

$30,000 in any single calendar quarter or in four consecutive calendar quarters. Below threshold: no obligation to register or charge GST/HST (but may voluntarily register). Above threshold: must register within 29 days.

### 5.13 Bad debts (ETA s.231)

If a registrant has previously reported GST/HST on a sale and the receivable becomes uncollectable, the GST/HST can be recovered via Line 107 (adjustment). Must be written off in the registrant's books. Recovery if the debt is later collected.

### 5.14 Reporting sales on Line 101

Line 101 includes all revenue — taxable, zero-rated, and exempt. It also includes GST/HST collected. This is a gross-inclusive line. Line 103 is the GST/HST collected portion.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs

*Pattern:* Petro-Canada, Shell, Esso, Canadian Tire (auto), car payments. *Default:* 0% ITC (no logbook). *Question:* "Do you have a vehicle logbook showing business vs personal kilometers?"

### 6.2 Meals and entertainment

*Pattern:* restaurants, Tim Hortons, Starbucks, The Keg. *Default:* block. *Question:* "Was this a business meal? If yes, 50% of the GST/HST is claimable as ITC."

### 6.3 Home office expenses

*Pattern:* utility bills, internet at home. *Default:* 0% ITC. *Question:* "Do you work from home? What percentage of your home is used exclusively for business?"

### 6.4 Round-number incoming transfers

*Pattern:* large round credit from owner name. *Default:* exclude as owner injection. *Question:* "Is this a customer payment, owner contribution, or loan?"

### 6.5 Incoming from individuals

*Pattern:* incoming from private names. *Default:* taxable sale at provincial HST rate, Line 101/103. *Question:* "Was it a sale? What was supplied?"

### 6.6 Interprovincial sales

*Pattern:* incoming from counterparty in different province. *Default:* rate of recipient's province. *Question:* "Confirm the province of the customer for place-of-supply determination."

### 6.7 Large purchases (potential capital asset)

*Pattern:* single purchase > CAD 1,000. *Default:* current expense on Line 106. *Question:* "Is this a capital asset with useful life > 1 year?"

### 6.8 Mixed-use phone, internet

*Pattern:* Rogers, Bell, Telus personal lines. *Default:* 0% if mixed. *Question:* "Is this a dedicated business line or mixed-use?"

### 6.9 Outgoing to individuals

*Pattern:* outgoing to private names. *Default:* exclude as draws. *Question:* "Was this a contractor payment, salary, refund, or personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* ATM, cash withdrawal. *Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* monthly rent to landlord. *Default:* commercial (taxable, ITC eligible). *Question:* "Is this a commercial or residential lease?"

### 6.12 Amazon.ca purchases

*Pattern:* Amazon.ca, AMZN. *Default:* taxable domestic at HST rate. *Question:* "Was this a business purchase? Check invoice for GST/HST breakdown."

### 6.13 Stripe/PayPal incoming

*Pattern:* Stripe payouts, PayPal transfers. *Default:* sales revenue at provincial rate, Line 101/103. *Question:* "Are these customer payments? What province are your customers in?"

### 6.14 Tips and gratuities

*Pattern:* restaurant charges with tip component. *Default:* GST/HST only on pre-tip amount. *Question:* "Confirm pre-tip amount for ITC calculation."

### 6.15 US dollar transactions

*Pattern:* USD amounts on bank statement. *Default:* convert to CAD at Bank of Canada daily rate. *Question:* "Confirm the CAD equivalent shown on the bank statement."

---

## Section 7 — Excel working paper template (Canada-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the Canada-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Line code") accepts GST34 line references (101, 103, 106, 405, etc.). Column I adds the GST/HST rate used (5%, 13%, 14%, 15%). For self-assessed imports, enter "405" in column H.

### Sheet "Line Summary"

One row per GST34 line. Column A is the line number, column B is the description, column C is the value.

```
| 101 | Total sales and revenue | =SUM of all credit transactions (sales, zero-rated, exempt) |
| 103 | GST/HST collected | =SUMIFS(Transactions!F:F, Transactions!G:G, "SALE") |
| 105 | Total GST/HST and adjustments | =C[103]+C[104] |
| 106 | Input tax credits | =SUMIFS(Transactions!F:F, Transactions!G:G, "ITC") |
| 108 | Total ITCs and adjustments | =C[106]+C[107] |
| 109 | Net tax | =C[105]-C[108] |
| 405 | Tax on imported supplies (s.218) | =SUMIFS(Transactions!F:F, Transactions!H:H, "405") |
```

### Sheet "Return Form"

Final GST34-ready figures:

```
Line 105 = Total GST/HST collected + adjustments
Line 108 = Total ITCs + adjustments
Line 109 = Line 105 - Line 108   [net tax]
Line 113 = Line 109 - Line 112   [balance]

Positive Line 113 → amount owing to CRA
Negative Line 113 → refund claimed
```

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/canada-gst-hst-<period>-working-paper.xlsx
```

---

## Section 8 — Canadian bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these Canada-specific patterns.

**RBC Royal Bank online export format.** CSV export from RBC Online Banking. Columns: Account Type, Account Number, Transaction Date, Cheque Number, Description 1, Description 2, CAD$, USD$. Date format: MM/DD/YYYY. Amounts are positive for credits, negative for debits. Description 1 contains the transaction type (e.g., "POS Purchase", "Online Banking Transfer", "Direct Deposit"). Description 2 contains the counterparty/payee name.

**TD Canada Trust online export format.** CSV from EasyWeb. Columns: Date, Transaction Description, Debit, Credit, Balance. Date format: MM/DD/YYYY. The Transaction Description field combines type and payee (e.g., "POS W/D SHOPIFY COMMERCE INC", "INTERAC E-TRANSFER FROM JOHN SMITH"). "POS W/D" = point-of-sale withdrawal (debit). "PREAUTH PYMT" = pre-authorized payment.

**Scotiabank export format.** CSV from Scotia OnLine. Columns: Date, Description, Withdrawals, Deposits, Balance. Date format: DD/MM/YYYY (different from RBC/TD).

**BMO export format.** CSV from BMO Online Banking. Columns: Transaction Date, Description, Amount. Single amount column (negative for debits).

**CIBC export format.** CSV or QFX from CIBC Online. Columns: Date, Description, Debit, Credit. Date format: YYYY-MM-DD.

**Common Canadian bank statement patterns:**

| Term | Meaning |
|---|---|
| POS, POS W/D, POS PURCHASE | Point-of-sale debit card purchase |
| PREAUTH, PREAUTH PYMT, PAP | Pre-authorized payment (direct debit) |
| INTERAC E-TRANSFER | Interac e-Transfer (incoming or outgoing) |
| ONLINE BANKING TRANSFER, TFR | Online transfer |
| DIRECT DEPOSIT, DIR DEP | Direct deposit (incoming) |
| CRA FED, RECEIVER GENERAL | CRA tax payment |
| NSF, NSF FEE | Non-sufficient funds fee (bank charge — exempt) |
| MONTHLY FEE, SERVICE CHARGE | Bank account fees (exempt) |
| INTL PURCHASE, FX FEE | International purchase and foreign exchange fee |
| ABM W/D, ATM | Cash withdrawal |

**Internal transfers.** Own-account transfers between client's RBC, TD, savings accounts. Labelled "online banking transfer", "TFR", or matching account numbers. Always exclude.

**Self-employed draws.** Transfers from business account to personal account labelled with the owner's name. Exclude.

**HST on bank statement lines.** Canadian invoices are GST/HST-inclusive on the bank statement. To extract the GST/HST component: Tax = Gross * Rate / (1 + Rate). Example: CAD 113.00 at 13% HST → Tax = 113 * 0.13 / 1.13 = 13.00.

**Interac e-Transfers.** Very common in Canada for B2B and B2C. The description shows "INTERAC E-TRANSFER FROM [name]" for incoming and "INTERAC E-TRANSFER TO [name]" for outgoing. Default treatment: incoming = potential sale (ask), outgoing = potential contractor payment or personal (ask).

**Foreign currency.** Convert to CAD using the Bank of Canada daily exchange rate. Note the rate in column L.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference rule:* "Inc", "Corp", "Ltd" = corporation; personal name = sole proprietor. *Fallback:* "Are you a sole proprietor, partnership, or corporation?"

### 9.2 GST/HST registration
*Inference rule:* if asking for a GST34, they are registered. *Fallback:* "Are you registered for GST/HST? What is your Business Number (BN)?"

### 9.3 Province
*Inference rule:* bank branch, counterparty mix, area codes in descriptions. *Fallback:* "What province is your principal place of business?"

### 9.4 Filing period
*Inference rule:* transaction date range. *Fallback:* "Is this for a monthly, quarterly, or annual period? What are the period dates?"

### 9.5 Accounting method
*Inference rule:* if no mention of Quick Method, assume regular. *Fallback:* "Are you using the regular method or the Quick Method (election GST74)?"

### 9.6 Industry
*Inference rule:* counterparty mix. *Fallback:* "In one sentence, what does the business do?"

### 9.7 Employees
*Inference rule:* CPP/EI/payroll outgoing. *Fallback:* "Do you have employees?"

### 9.8 Exempt supplies
*Inference rule:* financial/medical/educational/residential rental income patterns. *Fallback:* "Do you make any GST/HST-exempt supplies?"

### 9.9 Interprovincial sales
*Inference rule:* counterparties in multiple provinces. *Fallback:* "Do you sell to customers in provinces other than your own?"

### 9.10 Prior period balance
*Not inferable. Always ask.* "Do you have any GST/HST balance owing or credit from the previous period?"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the three-tier Accora architecture. Canada-specific content (rates, line mappings, ITC rules, place of supply) is based on the Excise Tax Act as of April 2026 including the Nova Scotia HST rate change to 14% effective April 1, 2025.

### Sources

**Primary legislation:**
1. Excise Tax Act (R.S.C., 1985, c. E-15), Part IX — s.123 (definitions), s.148 (small supplier), s.165 (imposition), s.169 (ITCs), s.170 (restrictions), s.218 (self-assessment), Schedule V (exempt), Schedule VI (zero-rated)
2. Input Tax Credit Information (GST/HST) Regulations — documentation thresholds
3. Place of Supply (GST/HST) Regulations (SOR/2010-117)
4. New Harmonized Value-added Tax System Regulations

**CRA guidance:**
5. GST34 form and guide (RC4022) — canada.ca
6. Quick Method guide (RC4058)
7. GST/HST Memoranda Series — various technical interpretations
8. GST/HST Info Sheets — place of supply, ITCs, specific industries

**Other:**
9. Bank of Canada daily exchange rates — bankofcanada.ca
10. CRA My Business Account — business registration verification

### Known gaps

1. Quebec QST is entirely refused — a separate skill is needed.
2. BC PST, SK PST, MB RST are refused — separate provincial skills needed.
3. Quick Method is refused — could be added as a v2.1 feature.
4. First Nations exemptions are refused — specialized knowledge required.
5. Real property self-supply rules (s.191) are refused — too fact-sensitive.
6. The NS HST rate changed to 14% on April 1, 2025 — verify no further rate changes.
7. Interprovincial place-of-supply for digital services is evolving — flag for reviewer if significant.
8. The s.218 self-assessment landscape is changing as more non-residents register voluntarily — always check the invoice first.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with three-tier Accora architecture. 10-section Malta v2.0 structure adopted. Supplier pattern library added (Section 3). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template added (Section 7). Bank statement guide with RBC/TD/BMO/CIBC formats added (Section 8). Onboarding moved to fallback (Section 9).
- **v2.0 (prior, April 2026):** Previous version with inline tier tags. Superseded.

### Self-check (v2.0)

1. Quick reference at top with rate table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples (hypothetical ON IT consultant): yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 14 rules).
5. Tier 2 catalogue compressed: yes (Section 6, 15 items).
6. Excel template with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only: yes (Section 9, 10 items).
8. All 8 Canada-specific refusals present: yes (Section 2, R-CA-1 through R-CA-8).
9. Reference material at bottom: yes (Section 10).
10. Self-assessment s.218 explicit: yes (Section 3.8 + Section 5.7 + Example 1).
11. Meals 50% rule explicit: yes (Section 5.10 + Example 3).
12. Vehicle logbook requirement explicit: yes (Example 6).
13. Place of supply rules documented: yes (Section 5.3).
14. HST rate table complete with NS 14%: yes (Section 1).
15. Zero-rated vs exempt distinction explicit: yes (Section 5.4–5.5).

## End of Canada GST/HST Return Skill v2.0

This skill is incomplete without the companion workflow file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a GST34 without it loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
