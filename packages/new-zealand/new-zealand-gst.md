---
name: new-zealand-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a New Zealand GST return (GST101A form) for a self-employed individual or small business in New Zealand. Trigger on phrases like "prepare GST return", "do the GST", "fill in GST101A", "create the return", "New Zealand GST", "NZ GST", or any request involving New Zealand GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill covers standard GST-registered persons under the invoice or payments basis. Financial services elections, GST groups, non-profit bodies, and complex change-of-use adjustments on high-value mixed-use assets are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any NZ GST work.
version: 2.0
---

# New Zealand GST Return Skill (GST101A) v2.0

## Section 1 — Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1 — follow that runbook with this skill providing the country-specific content.**

| Field | Value |
|---|---|
| Country | New Zealand |
| Standard rate | 15% (single rate — no reduced rates) |
| Zero rate | 0% (exports, going concerns, certain land transactions, financial services election, international transport) |
| Exempt | Financial services, residential rental, donated goods by nonprofits |
| Return form | GST101A (GST Return) |
| Filing portal | myIR (myir.ird.govt.nz) |
| Authority | Inland Revenue Department (IRD / Te Tari Taake) |
| Currency | NZD only |
| Filing frequencies | Monthly (taxable supplies > $24M or voluntary), 2-monthly (standard), 6-monthly (taxable supplies < $500,000) |
| Deadline | 28th of month following end of taxable period (except March period: 7 May; November period: 15 January) |
| Registration threshold | $60,000 taxable supplies in any 12-month period (compulsory); voluntary below threshold |
| Companion skill (Tier 1, workflow) | **vat-workflow-base v0.1 or later — MUST be loaded** |
| Contributor | Open Accounting Skills Community |
| Validation date | April 2026 |

**Key GST101A fields:**

| Field | Meaning |
|---|---|
| 5 | Total sales and income for the period (GST-exclusive if invoice basis, GST-inclusive if payments basis) |
| 6 | Zero-rated supplies (included in field 5) |
| 7 | Total output tax on sales (field 5 minus field 6, multiplied by 3/23) |
| 8 | Adjustments to output tax (e.g., change of use from non-taxable to taxable) |
| 9 | Total output tax (= field 7 + field 8) |
| 10 | Total purchases and expenses (GST-exclusive if invoice basis, GST-inclusive if payments basis) |
| 11 | Input tax claimed (field 10 multiplied by 3/23) |
| 12 | Adjustments to input tax (e.g., change of use from taxable to non-taxable) |
| 13 | Total input tax (= field 11 + field 12) |
| 15 | Difference (= field 9 minus field 13; positive = tax to pay, negative = refund) |

**The 3/23 formula.** New Zealand GST returns work on GST-inclusive amounts (for payments basis) or GST-exclusive amounts (for invoice basis). The 3/23 fraction extracts the GST component from a GST-inclusive amount: 15/115 = 3/23. For GST-exclusive amounts, multiply by 15% (3/20).

**Conservative defaults — NZ-specific values for the universal categories in `vat-workflow-base` Section 2:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 15% (only rate available) |
| Unknown GST status of a purchase | Not claimable (no input tax) |
| Unknown counterparty country | Domestic New Zealand |
| Unknown business-use proportion (vehicle, phone, home office) | 0% input tax |
| Unknown whether personal or business expense | Personal (no input tax) |
| Unknown non-resident supplier GST status | Assume not registered (no input tax claim) |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds — country slot values for the reviewer brief in `vat-workflow-base` Section 3:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | NZD 5,000 |
| HIGH tax-delta on a single conservative default | NZD 400 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net GST position | NZD 10,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the period in CSV, PDF, or pasted text. Must cover the full taxable period. Acceptable from any NZ or international business bank: ANZ NZ, Westpac NZ, ASB, BNZ, Kiwibank, TSB, Heartland Bank, Co-operative Bank, Revolut, Wise Business, or any other.

**Recommended** — sales invoices for the period (especially for zero-rated supplies and exports), purchase invoices (tax invoices) for any input tax claim above NZD 400, the client's IRD number.

**Ideal** — complete sales and purchase journal, prior period GST101A, Xero/MYOB trial balance export, reconciliation of any adjustments.

**Refusal policy if minimum is missing — SOFT WARN.** If no bank statement at all, hard stop. If bank statement only, proceed but record: "This GST101A was produced from bank statement alone. The reviewer must verify that input tax claims above NZD 400 are supported by compliant tax invoices and that all zero-rating conditions are met."

### NZ-specific refusal catalogue

If any trigger fires, stop, output the refusal message verbatim, end the conversation.

**R-NZ-1 — Financial services election (s.20F).** *Trigger:* client has elected to zero-rate financial services or asks about s.20F. *Message:* "The election to zero-rate financial services under s.20F of the GST Act requires complex calculations and specific conditions. This skill covers standard taxable and zero-rated supplies only. Please use a chartered accountant familiar with financial services GST."

**R-NZ-2 — GST groups.** *Trigger:* client is part of a GST group registration. *Message:* "GST group registrations require consolidated reporting and intra-group supply rules. Out of scope."

**R-NZ-3 — Non-profit bodies with donated goods.** *Trigger:* client is a non-profit using the donated goods exemption. *Message:* "Non-profit bodies have special GST rules for donated goods and services. Out of scope."

**R-NZ-4 — Complex change-of-use adjustments on high-value assets.** *Trigger:* client has a high-value mixed-use asset (e.g., holiday home used partly for Airbnb) requiring annual change-of-use adjustments under s.21–21H. *Message:* "Change-of-use adjustments for mixed-use assets with a value exceeding $5,000 require annual recalculation of the taxable-use proportion. This is too fact-sensitive for this skill. Please use a chartered accountant."

**R-NZ-5 — Compulsory zero-rating of land.** *Trigger:* client is selling or buying land between GST-registered persons. *Message:* "Land transactions between registered persons are subject to compulsory zero-rating under s.11(1)(mb). This requires specific contractual wording and a vendor/purchaser notification process. Please use a property lawyer and chartered accountant."

**R-NZ-6 — Secondhand goods input tax credit (s.24).** *Trigger:* client regularly buys secondhand goods from unregistered persons and claims input tax under s.24. *Message:* "The secondhand goods input tax credit under s.24 has specific documentation requirements and valuation rules. If this is a significant part of the business, please use a chartered accountant to confirm eligibility and amounts."

**R-NZ-7 — GST on imported services (s.8(4B)).** *Trigger:* client is a non-profit or makes significant exempt supplies and receives services from non-residents. *Message:* "The reverse charge on imported services under s.8(4B) applies when the recipient cannot claim a full input tax credit. For fully taxable businesses, there is no reverse charge obligation (the input tax offsets the output tax). If your business makes exempt supplies, please use a chartered accountant."

**R-NZ-8 — Payments basis with large accruals.** *Trigger:* client uses payments basis but has significant unpaid invoices at period end that may distort the return. *Message:* "Under the payments basis, GST is accounted for when payment is made or received, not when invoiced. If you have large outstanding invoices at period end, ensure only paid amounts are included. If you are unsure, confirm your accounting basis with your accountant."

---

## Section 3 — Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name. If multiple patterns match, use the most specific.

### 3.1 New Zealand banks (fees exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| ANZ, ANZ NEW ZEALAND, ANZ NZ | EXCLUDE for bank charges/fees | Financial service, exempt (s.14(a), s.3) |
| WESTPAC, WESTPAC NZ | EXCLUDE for bank charges/fees | Same |
| ASB, ASB BANK | EXCLUDE for bank charges/fees | Same |
| BNZ, BANK OF NEW ZEALAND | EXCLUDE for bank charges/fees | Same |
| KIWIBANK | EXCLUDE for bank charges/fees | Same |
| TSB BANK, HEARTLAND BANK, CO-OPERATIVE BANK | EXCLUDE for bank charges/fees | Same |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE for transaction/maintenance fees | Check for separate taxable subscription invoices |
| INTEREST, INT | EXCLUDE | Interest income/expense, exempt |
| MORTGAGE, LOAN | EXCLUDE | Loan principal movement, out of scope |

### 3.2 New Zealand government and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| IRD, INLAND REVENUE, TE TARI TAAKE | EXCLUDE | Tax payment (GST, income tax, PAYE) |
| ACC, ACCIDENT COMPENSATION | EXCLUDE | ACC levy — not a supply |
| NZTA, WAKA KOTAHI | EXCLUDE | Transport agency fees/levies |
| MINISTRY OF, DEPARTMENT OF | EXCLUDE | Government fees |
| COMPANIES OFFICE, NZBN | EXCLUDE | Registry fee |
| COUNCIL, CITY COUNCIL, DISTRICT COUNCIL | EXCLUDE for rates | Property rates — not a supply |
| COUNCIL (consent fees, building permits) | Domestic 15% | Regulatory services — taxable |

### 3.3 New Zealand utilities

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| MERCURY ENERGY, GENESIS ENERGY, CONTACT ENERGY | Domestic 15% | 10/11 | Electricity — overhead |
| MERIDIAN ENERGY, TRUSTPOWER, FLICK ELECTRIC | Domestic 15% | 10/11 | Electricity — overhead |
| NOVA ENERGY, ELECTRIC KIWI, POWERSHOP | Domestic 15% | 10/11 | Electricity — overhead |
| SPARK, SPARK NZ | Domestic 15% | 10/11 | Telecoms — overhead |
| VODAFONE NZ, VODAFONE NEW ZEALAND | Domestic 15% | 10/11 | Telecoms — overhead |
| 2DEGREES, TWO DEGREES | Domestic 15% | 10/11 | Telecoms — overhead |
| SKINNY MOBILE | Domestic 15% | 10/11 | Telecoms — overhead |
| CHORUS, ENABLE, ULTRAFAST FIBRE | Domestic 15% | 10/11 | Fibre broadband — overhead |
| WATERCARE, WELLINGTON WATER | Domestic 15% | 10/11 | Water — overhead |

### 3.4 Insurance (exempt — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| IAG, STATE INSURANCE, AMI, NZI | EXCLUDE | Insurance, exempt (s.14) |
| AA INSURANCE, TOWER INSURANCE | EXCLUDE | Same |
| SOUTHERN CROSS, PARTNERS LIFE, AIA NZ | EXCLUDE | Health/life insurance, exempt |
| INSURANCE, INS PREMIUM | EXCLUDE | All exempt |

### 3.5 Post and logistics

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| NZ POST, NEW ZEALAND POST | Domestic 15% | 10/11 | NZ Post is taxable (unlike some EU postal services) |
| COURIER POST, PACE | Domestic 15% | 10/11 | NZ Post courier service |
| FASTWAY, ARAMEX NZ, TOLL, MAINFREIGHT | Domestic 15% | 10/11 | Courier/freight services |
| DHL NZ, FEDEX NZ, UPS NZ | Domestic 15% | 10/11 | Express courier |

### 3.6 Transport

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| AIR NEW ZEALAND, AIR NZ (domestic) | Domestic 15% | 10/11 | Domestic flights taxable |
| AIR NEW ZEALAND (international) | Zero-rated | 6 | International transport — s.11A(1)(a) |
| JETSTAR NZ (domestic) | Domestic 15% | 10/11 | Domestic flights taxable |
| AT HOP, METLINK, METRO CANTERBURY | Domestic 15% | 10/11 | Public transport — taxable in NZ (not exempt like some countries) |
| UBER NZ | Domestic 15% | 10/11 | Ride-sharing — GST registered |
| OLA NZ | Domestic 15% | 10/11 | Ride-sharing |
| INTERISLANDER, BLUEBRIDGE | Domestic 15% (inter-island) | 10/11 | Cook Strait ferry — domestic |
| RENTAL CAR, BUDGET NZ, HERTZ NZ, AVIS NZ | Domestic 15% | 10/11 | Car rental |

### 3.7 Food retail (blocked unless hospitality business)

| Pattern | Treatment | Notes |
|---|---|---|
| COUNTDOWN, WOOLWORTHS NZ | Default BLOCK input tax | Personal provisioning. Zero-rated basic food + 15% non-food mix. Only deductible if hospitality business. |
| PAK'N SAVE, PAK N SAVE, PAKNSAVE | Default BLOCK | Same |
| NEW WORLD | Default BLOCK | Same |
| FOUR SQUARE | Default BLOCK | Same |
| FARRO, MOORE WILSONS | Default BLOCK | Same (though Moore Wilsons is popular with hospitality) |
| RESTAURANTS, CAFES, BARS (any named) | Default BLOCK | Entertainment — see Section 5.11 |

### 3.8 SaaS — non-resident suppliers (reverse charge or GST-registered)

In New Zealand, a reverse charge on imported services applies only when the recipient cannot claim a full input tax credit (s.8(4B)). For fully taxable businesses, there is NO reverse charge obligation — the supplier either charges NZ GST (if registered under the non-resident rules) or does not, and the recipient cannot claim input tax on a supply where no GST was charged. Many large non-resident digital suppliers are now GST-registered in NZ.

| Pattern | GST status | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | GST-registered in NZ | If NZ GST on invoice: domestic 15%, field 10/11 | Check invoice — Google NZ entity charges GST |
| MICROSOFT (365, Azure) | GST-registered in NZ | If NZ GST on invoice: domestic 15%, field 10/11 | Same |
| ADOBE | GST-registered in NZ | If NZ GST on invoice: domestic 15%, field 10/11 | Same |
| META, FACEBOOK ADS | GST-registered in NZ | If NZ GST on invoice: domestic 15%, field 10/11 | Same |
| SPOTIFY | GST-registered in NZ | If NZ GST on invoice: domestic 15%, field 10/11 | Same |
| NOTION | Not NZ-registered (US) | No GST charged, no input tax claim | Cost is a non-deductible GST expense |
| ANTHROPIC, CLAUDE | Not NZ-registered (US) | No GST charged, no input tax claim | Same |
| OPENAI, CHATGPT | Not NZ-registered (US) | No GST charged, no input tax claim | Same |
| GITHUB | Check invoice | If NZ GST charged: domestic 15%; if not: no claim | |
| FIGMA | Not NZ-registered (US) | No GST charged, no input tax claim | |
| CANVA | GST-registered in NZ (AU entity) | If NZ GST on invoice: domestic 15%, field 10/11 | Canva AU registered for NZ GST |
| SLACK, ATLASSIAN, ZOOM, DROPBOX | Check invoice | If NZ GST charged: 15%; if not: no claim | Some have registered, some not |

### 3.9 New Zealand SaaS / domestic suppliers

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| XERO | Domestic 15% | 10/11 | NZ-headquartered accounting software |
| STRIPE NZ, STRIPE PAYMENTS NZ | Check invoice | | Transaction fees may be exempt; subscription taxable |
| VEND (LIGHTSPEED) | Domestic 15% | 10/11 | POS software |
| TIMELY, UNLEASHED | Domestic 15% | 10/11 | NZ SaaS |
| PUSHPAY | Domestic 15% | 10/11 | NZ SaaS |
| TRADEME, TRADE ME | Domestic 15% | 10/11 | NZ marketplace fees |

### 3.10 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) | Payment processing fees are exempt financial services |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | Same |
| WINDCAVE, PAYMARK, DPS | EXCLUDE for transaction fees | Payment gateway — exempt financial service |
| EFTPOS NZ | EXCLUDE | Card processing fees — exempt |
| AFTERPAY, LAYBUY | Check invoice | Merchant fees may be exempt (financial service) |

### 3.11 Professional services (NZ)

| Pattern | Treatment | Field | Notes |
|---|---|---|---|
| CHARTERED ACCOUNTANT, CA, CPA | Domestic 15% | 10/11 | Always claimable |
| LAWYER, SOLICITOR, BARRISTER | Domestic 15% | 10/11 | Claimable if business purpose |
| SURVEYOR, VALUER, ENGINEER | Domestic 15% | 10/11 | Claimable if business purpose |
| COMPANIES OFFICE | EXCLUDE | | Government registry fee |

### 3.12 Payroll and statutory (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| SALARY, WAGES, PAY | EXCLUDE | Wages — outside GST scope |
| PAYE, IRD PAYE | EXCLUDE | PAYE tax remittance |
| KIWISAVER | EXCLUDE | Superannuation contribution |
| ACC LEVY | EXCLUDE | Accident compensation — not a supply |
| STUDENT LOAN | EXCLUDE | Loan repayment |

### 3.13 Property and rent

| Pattern | Treatment | Notes |
|---|---|---|
| RENT (commercial) | Domestic 15% | Commercial lease — GST on rent, input tax claimable |
| RENT (residential) | EXCLUDE | Residential rental exempt (s.14(c)) |
| BODY CORPORATE | EXCLUDE if residential | Residential body corporate exempt |
| RATES, COUNCIL RATES | EXCLUDE | Local authority rates — not a supply |

### 3.14 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFER, TFR, OWN ACCOUNT | EXCLUDE | Internal movement |
| DIVIDEND | EXCLUDE | Dividend, out of scope |
| LOAN REPAYMENT | EXCLUDE | Principal, out of scope |
| ATM, CASH WITHDRAWAL | TIER 2 — ask | Default exclude; ask what cash was for |
| DRAWINGS, OWNER DRAW | EXCLUDE | Owner withdrawal |

### 3.15 Specific NZ patterns

| Pattern | Treatment | Notes |
|---|---|---|
| BUNNINGS NZ | Domestic 15% | Hardware/tools — claimable if business purpose |
| THE WAREHOUSE | Default BLOCK | Likely personal — mixed retail |
| MITRE 10 | Domestic 15% if trade purchase | Hardware — claimable if business tools/materials |
| NOEL LEEMING, PB TECH, MIGHTY APE | Domestic 15% if business | Electronics — claimable if business asset |
| Z ENERGY, BP NZ, MOBIL NZ, CALTEX | Domestic 15% | Fuel — claimable to extent of business use |
| AA NZ (membership) | Domestic 15% | Automobile Association — claimable if business |

---

## Section 4 — Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of an Auckland-based self-employed software consultant.

### Example 1 — Non-resident SaaS, no NZ GST (Notion)

**Input line:**
`2026-04-03 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; NZD 26.18`

**Reasoning:**
Notion Labs Inc is a US entity not registered for NZ GST (Section 3.8). No GST on the invoice. In NZ, there is no reverse charge obligation for fully taxable businesses (s.8(4B) only applies to recipients who cannot claim full input tax). The NZD 26.18 is a business expense for income tax purposes but generates no GST input tax claim. Include in field 10 (purchases) but no input tax in field 11.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-03 | NOTION LABS INC | -26.18 | -26.18 | 0 | — | 10 (no GST) | N | — | — |

### Example 2 — Non-resident SaaS, NZ GST charged (Google Ads)

**Input line:**
`2026-04-10 ; GOOGLE NEW ZEALAND LTD ; DEBIT ; Google Ads April 2026 ; -920.00 ; NZD`

**Reasoning:**
Google is GST-registered in NZ and charges 15% GST. The NZD 920.00 is GST-inclusive. GST = 920 * 3/23 = 120.00. Net = 800.00. Full input tax claim on field 11.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-10 | GOOGLE NZ | -920.00 | -800.00 | -120.00 | 15% | 10/11 | N | — | — |

### Example 3 — Entertainment, 50% deduction

**Input line:**
`2026-04-15 ; THE GROVE RESTAURANT AUCKLAND ; DEBIT ; Client dinner ; -350.00 ; NZD`

**Reasoning:**
Restaurant transaction. In NZ, entertainment expenses are subject to the 50% deduction limitation under the Income Tax Act 2007, s.DD 1. For GST purposes, the input tax claim follows the entertainment limitation — only 50% of the GST is claimable (s.21(1) read with ITA s.DD 1). GST on full amount = 350 * 3/23 = 45.65. Claimable input tax = 22.83 (50%). Conservative default: block entirely as likely personal. If confirmed as business, 50% is claimable.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-15 | THE GROVE RESTAURANT | -350.00 | -350.00 | 0 | — | — | Y | Q1 | "Entertainment: blocked (conservative). If business, 50% claimable." |

### Example 4 — Capital asset (business equipment)

**Input line:**
`2026-04-18 ; PB TECH AUCKLAND ; DEBIT ; MacBook Pro 16 ; -4,599.00 ; NZD`

**Reasoning:**
NZD 4,599 GST-inclusive. GST = 4,599 * 3/23 = 599.87. Net = 3,999.13. This is a business asset. In NZ there is no separate capital goods line on the GST101A — all input tax goes to field 11. However, assets over $5,000 (GST-exclusive) are subject to change-of-use adjustment rules (s.21–21H). At $3,999.13 net, this is below the $5,000 threshold. Full input tax claim.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-18 | PB TECH | -4,599.00 | -3,999.13 | -599.87 | 15% | 10/11 | N | — | — |

### Example 5 — Export sale (zero-rated)

**Input line:**
`2026-04-22 ; ACME PTY LTD SYDNEY ; CREDIT ; Invoice NZ-2026-018 IT consulting March ; +8,500.00 ; NZD`

**Reasoning:**
Incoming NZD 8,500 from an Australian company. Client provides IT consulting services to a non-resident outside NZ. Under s.11A(1)(k), services supplied to a non-resident who is outside NZ at the time of supply are zero-rated (subject to conditions — the service must not be performed for a person in NZ or relate to NZ land/goods). Include in field 5 (total sales) and field 6 (zero-rated). No output tax in field 7.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-22 | ACME PTY LTD | +8,500.00 | +8,500.00 | 0 | 0% | 5 + 6 | Y | Q2 (HIGH) | "Verify non-resident and outside-NZ conditions for zero-rating" |

### Example 6 — Vehicle costs, no logbook

**Input line:**
`2026-04-28 ; Z ENERGY PARNELL ; DEBIT ; Fuel ; -102.00 ; NZD`

**Reasoning:**
Fuel purchase. In NZ, motor vehicle expenses are claimable to the extent of business use. IRD accepts a logbook kept for 3 consecutive months as evidence of the business-use percentage, which then applies for 3 years. Without a logbook, the conservative default is 0% input tax claim. If a logbook exists showing, say, 70% business use, then 70% of the GST is claimable.

**Output:**

| Date | Counterparty | Gross | Net | GST | Rate | Field | Default? | Question? | Excluded? |
|---|---|---|---|---|---|---|---|---|---|
| 2026-04-28 | Z ENERGY | -102.00 | -102.00 | 0 | — | — | Y | Q3 | "Vehicle fuel: 0% (no logbook). Provide 3-month logbook for partial claim." |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 15% (GST Act s.8(1))

The only positive GST rate in New Zealand. All taxable supplies of goods and services are taxed at 15%. There are no reduced rates. Sales → field 5 (total), output tax → field 7. Purchases → field 10, input tax → field 11.

### 5.2 Zero-rated supplies (GST Act s.11, s.11A, s.11AB)

Exports of goods (s.11(1)(a)): requires Customs export entry. Services to non-residents (s.11A(1)(k)): conditions — recipient must be non-resident, outside NZ at time of supply, service must not relate to NZ land or be performed for a person in NZ. Going concerns (s.11(1)(mb)): supply of a business as a going concern to a registered person. Land between registered persons (s.11(1)(mb)): compulsory zero-rating — R-NZ-5 fires. International transport (s.11A(1)(a)–(c)). Report in field 5 (total) and field 6 (zero-rated).

### 5.3 Exempt supplies (GST Act s.14)

Financial services (s.14(a), s.3): lending, currency exchange, life insurance, equity securities — exempt. Residential rental (s.14(c)): rental of a dwelling — exempt. Donated goods/services by nonprofits (s.14(ca)). Penalties, fines, and default interest (s.14). Exempt supplies do NOT go on the return. No output tax, no input tax on related costs.

### 5.4 Input tax credits (GST Act s.20(3))

Input tax is claimable on GST-inclusive purchases used in making taxable supplies. Must have a tax invoice (s.24). Tax invoice requirements: supplier name, GST number, date, description, consideration, and GST amount. For supplies under $50, a simplified tax invoice is acceptable. For supplies $50–$1,000, supplier name, date, description, and total (GST-inclusive) suffice. For supplies over $1,000, full details required.

### 5.5 No reverse charge for fully taxable businesses

Unlike the EU, NZ does not require a fully taxable business to self-assess GST on imported services. The reverse charge under s.8(4B) only applies when the recipient makes exempt supplies and therefore cannot claim full input tax. For a typical self-employed consultant making only taxable supplies, no reverse charge applies — either the non-resident supplier charges NZ GST (if registered) or no NZ GST applies and there is no input tax claim.

### 5.6 Non-resident supplier registration

Since October 2016, non-resident suppliers of remote services (digital services, streaming, SaaS) to NZ consumers must register for NZ GST if their supplies exceed $60,000. Many large suppliers (Google, Microsoft, Adobe, Meta, Spotify, Netflix, Canva) are now registered and charge NZ GST. Check the invoice: if NZ GST is on the invoice, treat as a domestic supply with input tax. If no NZ GST, no input tax claim.

### 5.7 Payments basis vs invoice basis

Invoice basis (accrual): account for GST when the invoice is issued (sales) or received (purchases), regardless of payment. Payments basis (cash): account for GST when payment is made or received. The bank statement naturally aligns with payments basis. For invoice basis clients, outstanding invoices at period end must be included even if not yet paid — ask for the invoice register.

### 5.8 Change-of-use adjustments (s.21–21H)

When an asset or expense changes its proportion of taxable use, an adjustment may be required. For assets under $5,000 (GST-exclusive), no adjustment is needed. For assets $5,000–$10,000, a one-off adjustment at first non-taxable use. For assets over $10,000, annual adjustments for up to 10 years (land: 10 years; other: useful life or 5 years). Report adjustments in field 8 (output) or field 12 (input). If complex → R-NZ-4 fires.

### 5.9 Secondhand goods (s.24(5))

A registered person who purchases goods from an unregistered seller can claim input tax based on the purchase price (not exceeding the open market value). Must maintain records: name/address of seller, date, description, and price. No tax invoice required from seller (since they are not registered). Claim on field 11.

### 5.10 Motor vehicles

No blanket block on motor vehicles in NZ (unlike Malta). ITCs are claimable to the extent of business use. IRD expects a logbook: keep for a 3-month representative period, then apply the resulting percentage for 3 years. FBT (fringe benefit tax) applies if a company provides a vehicle to an employee for private use — but FBT is outside GST scope.

### 5.11 Entertainment — 50% limitation

GST Act s.21(1) read with Income Tax Act 2007 subpart DD. Entertainment expenses (meals, functions, corporate hospitality) are subject to a 50% limitation. The GST input tax claim is limited to 50% of the GST component. This applies to: meals and drinks, corporate boxes, holiday accommodation for employees, entertainment allowances. Does NOT apply to: light refreshments at business meetings, meals while traveling on business overnight, conferences/seminars with incidental catering.

### 5.12 Goods and services purchased from non-residents

If the non-resident supplier is GST-registered in NZ and charges GST: treat as domestic purchase, claim input tax. If not registered and no GST charged: no input tax claim (for fully taxable businesses). The cost is still deductible for income tax. If the recipient makes exempt supplies: reverse charge under s.8(4B) may apply — R-NZ-7 fires.

### 5.13 Bad debts (s.26)

If a registrant has accounted for GST on a sale (invoice basis) and the debt becomes bad, an adjustment is made in field 12 (reduction of output tax previously returned). The adjustment is 3/23 of the bad debt written off. If the debt is later recovered, a reverse adjustment is required.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Vehicle costs

*Pattern:* Z Energy, BP, Mobil, Caltex, vehicle lease. *Default:* 0% (no logbook). *Question:* "Do you have a vehicle logbook? What is your business-use percentage?"

### 6.2 Entertainment

*Pattern:* restaurants, bars, cafes, catering. *Default:* block. *Question:* "Was this a business entertainment expense? If yes, 50% of GST is claimable."

### 6.3 Non-resident SaaS — GST status unknown

*Pattern:* SaaS charges from international brands without clear GST line. *Default:* no input tax claim. *Question:* "Does the invoice show NZ GST charged? If so, what is the supplier's NZ GST number?"

### 6.4 Round-number incoming transfers

*Pattern:* large round credit from owner name. *Default:* exclude as owner injection. *Question:* "Is this a customer payment, your own funds, or a loan?"

### 6.5 Incoming from individuals

*Pattern:* incoming from private names. *Default:* taxable sale at 15%, field 5/7. *Question:* "Was it a sale? What was supplied?"

### 6.6 Incoming from overseas

*Pattern:* foreign currency or non-NZ bank. *Default:* zero-rated (service to non-resident). *Question:* "Is the customer a non-resident outside NZ? Confirm zero-rating conditions."

### 6.7 Large purchases (potential high-value asset)

*Pattern:* single purchase > NZD 5,000. *Default:* include in field 10/11 but flag for change-of-use monitoring. *Question:* "Is this a capital asset? Will it be used 100% for business?"

### 6.8 Mixed-use phone, internet, home office

*Pattern:* Spark, Vodafone personal lines; home power bills. *Default:* 0% if mixed. *Question:* "Is this a dedicated business line or mixed-use?"

### 6.9 Outgoing to individuals

*Pattern:* outgoing to private names. *Default:* exclude as draws. *Question:* "Was this a contractor payment, salary, or personal transfer?"

### 6.10 Cash withdrawals

*Pattern:* ATM, cash withdrawal. *Default:* exclude. *Question:* "What was the cash used for?"

### 6.11 Rent payments

*Pattern:* monthly rent. *Default:* commercial (taxable, input tax claimable). *Question:* "Is this commercial or residential?"

### 6.12 Trade Me / marketplace sales

*Pattern:* Trade Me payouts. *Default:* taxable sale at 15%, field 5/7. Trade Me fees → domestic 15%, field 10/11. *Question:* "Are these business sales or personal item disposals?"

### 6.13 Airbnb income

*Pattern:* Airbnb payouts. *Default:* flag for reviewer — short-term accommodation is taxable at 15% but may trigger change-of-use issues if property was previously private. *Question:* "Is this a dedicated rental property or your private home? What is the taxable-use percentage?"

### 6.14 Secondhand goods purchases

*Pattern:* purchases from individuals, estate sales, auctions. *Default:* no input tax claim unless s.24 conditions met. *Question:* "Was this purchased from an unregistered seller? Do you have the seller's name and address?"

### 6.15 Foreign currency transactions

*Pattern:* non-NZD amounts. *Default:* convert to NZD at the RBNZ mid-rate on the transaction date. *Question:* "Confirm the NZD equivalent on the bank statement."

---

## Section 7 — Excel working paper template (NZ-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the NZ-specific overlay.

### Sheet "Transactions"

Columns A–L per the base. Column H ("Field code") accepts GST101A field numbers (5, 6, 10, etc.). NZ has a simpler structure — no reverse charge fields for fully taxable businesses.

### Sheet "Field Summary"

One row per GST101A field:

```
| 5  | Total sales and income | =SUM of all credit (sales) transactions |
| 6  | Zero-rated supplies | =SUMIFS(Transactions!D:D, Transactions!H:H, "6") |
| 7  | Output tax | =(C[5]-C[6]) * 3/23  [if payments basis, GST-inclusive] |
|    |            | OR =(C[5]-C[6]) * 0.15 [if invoice basis, GST-exclusive] |
| 8  | Adjustments to output tax | =manual entries only |
| 9  | Total output tax | =C[7]+C[8] |
| 10 | Total purchases and expenses | =SUM of all debit (purchase) transactions with GST |
| 11 | Input tax | =C[10] * 3/23  [if payments basis] |
|    |           | OR =C[10] * 0.15 [if invoice basis] |
| 12 | Adjustments to input tax | =manual entries (change of use, bad debts) |
| 13 | Total input tax | =C[11]+C[12] |
| 15 | GST to pay / refund | =C[9]-C[13] |
```

**Note on accounting basis:** If payments basis, fields 5 and 10 are GST-inclusive amounts and the 3/23 formula applies. If invoice basis, fields 5 and 10 are GST-exclusive and 15% (3/20) applies. Confirm the client's basis before building.

### Sheet "Return Form"

Final GST101A-ready figures:

```
Field 9  = Total output tax
Field 13 = Total input tax

Field 15 = Field 9 - Field 13

Positive Field 15 → GST to pay to IRD
Negative Field 15 → Refund due from IRD
```

### Mandatory recalc step

After building the workbook, run:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/nz-gst-<period>-working-paper.xlsx
```

---

## Section 8 — New Zealand bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these NZ-specific patterns.

**ANZ NZ export format.** CSV download from ANZ Internet Banking. Columns: Date (DD/MM/YYYY), Transaction Details, Amount, Balance. The Amount column uses negative for debits. Transaction Details combines type and payee (e.g., "Visa Purchase - PB Tech Auckland", "Direct Debit - Spark NZ").

**Westpac NZ export format.** CSV from Westpac One. Columns: Date, Amount, Other Party, Description, Reference, Particulars, Analysis Code. The "Other Party" field contains the counterparty name. "Particulars", "Reference", and "Description" are the three freeform fields from NZ bank payment references.

**ASB export format.** CSV from ASB FastNet Classic. Columns: Date, Unique Id, Tran Type, Cheque Number, Payee, Memo, Amount. Date format: YYYY-MM-DD.

**BNZ export format.** CSV from BNZ Online. Columns: Date, Amount, Payee, Particulars, Code, Reference, Tran Type, This Party Account. Date format: DD/MM/YYYY.

**Kiwibank export format.** CSV from Kiwibank Internet Banking. Columns: Date, Description, Amount, Balance. Simple format.

**Common NZ bank statement patterns:**

| Term | Meaning |
|---|---|
| Visa Purchase, EFTPOS | Card purchase (debit) |
| Direct Debit, D/D | Pre-authorized direct debit |
| Automatic Payment, A/P | Scheduled automatic payment |
| Direct Credit, D/C | Incoming direct credit |
| Transfer, TFR | Internal transfer |
| ATM W/D | Cash withdrawal |
| BNPL | Buy now pay later (Afterpay, Laybuy) |
| Particulars / Code / Reference | NZ-specific 3-field payment reference system |

**NZ payment reference system.** New Zealand bank payments have three freeform reference fields: Particulars (12 chars), Code (12 chars), Reference (12 chars). These often contain invoice numbers, account references, or payment descriptions. Always read all three fields when identifying a transaction.

**Internal transfers.** Own-account transfers between the client's ANZ, ASB, Westpac accounts. Labelled "transfer", "TFR", or matching account numbers. Always exclude.

**Sole trader draws.** A self-employed sole trader cannot pay themselves wages. Transfers to personal accounts are drawings. Exclude.

**ACC levies.** ACC (Accident Compensation Corporation) levies appear as direct debits. These are not a supply — exclude. They are deductible for income tax but generate no GST input tax.

**IRD payments.** GST payments, provisional tax, PAYE appear as "IRD" or "INLAND REVENUE". Always exclude — these are tax payments, not supplies.

**Refunds and reversals.** Identify by "refund", "reversal", "credit adj". Book as a negative in the same field as the original.

**Foreign currency.** Convert to NZD at the RBNZ (Reserve Bank of New Zealand) mid-rate on the transaction date. Note the rate in column L.

---

## Section 9 — Onboarding fallback (only when inference fails)

### 9.1 Entity type
*Inference rule:* personal name = sole trader; "Ltd", "Limited" = company; "LP" = limited partnership. *Fallback:* "Are you a sole trader, partnership, company, or look-through company?"

### 9.2 GST registration
*Inference rule:* if asking for a GST101A, they are registered. *Fallback:* "Are you GST-registered? What is your IRD number?"

### 9.3 Accounting basis
*Inference rule:* small businesses typically use payments basis. If Xero/MYOB export shows accrual data, likely invoice basis. *Fallback:* "Are you on the invoice basis (accrual) or payments basis (cash)?"

### 9.4 Filing period
*Inference rule:* transaction date range. 2-monthly is most common. *Fallback:* "Is this a 1-month, 2-month, or 6-month GST period? What are the dates?"

### 9.5 Industry
*Inference rule:* counterparty mix. *Fallback:* "In one sentence, what does the business do?"

### 9.6 Employees
*Inference rule:* PAYE/KiwiSaver/wages outgoing. *Fallback:* "Do you have employees?"

### 9.7 Exempt supplies
*Inference rule:* financial services, residential rental income patterns. *Fallback:* "Do you make any GST-exempt supplies (financial services, residential rental)?"

### 9.8 Zero-rated supplies
*Inference rule:* foreign currency incoming, Australian/overseas counterparties. *Fallback:* "Do you export goods or provide services to customers outside NZ?"

### 9.9 Prior period balance
*Not inferable. Always ask.* "Do you have any GST owing or refund due from the previous period?"

### 9.10 Vehicle use
*Inference rule:* fuel purchases, vehicle-related charges. *Fallback:* "Do you use a vehicle for business? Do you have a logbook?"

---

## Section 10 — Reference material

### Validation status

This skill is v2.0, rewritten in April 2026 to align with the three-tier Accora architecture. NZ-specific content (rates, field mappings, input tax rules, zero-rating conditions) is based on the Goods and Services Tax Act 1985 as of April 2026.

### Sources

**Primary legislation:**
1. Goods and Services Tax Act 1985 (NZ) — s.3 (definitions), s.8 (imposition), s.8(4B) (reverse charge), s.11/11A (zero-rating), s.14 (exempt), s.20 (calculation of tax), s.21–21H (change of use), s.24 (tax invoices and secondhand goods), s.26 (bad debts), s.51 (registration)
2. Tax Administration Act 1994 — filing and payment obligations
3. Income Tax Act 2007, subpart DD — entertainment limitation

**IRD guidance:**
4. GST101A form and guide — ird.govt.nz
5. IR375 GST guide — comprehensive GST guidance
6. IR546 Keeping records — record-keeping requirements
7. IS 24/07 (or current version) — non-resident digital services GST registration

**Other:**
8. RBNZ exchange rates — rbnz.govt.nz
9. Companies Office — companiesoffice.govt.nz (entity verification)
10. myIR — myir.ird.govt.nz (filing portal)

### Known gaps

1. Financial services election (s.20F) is refused — specialized skill needed.
2. Compulsory zero-rating of land is refused — requires property lawyer involvement.
3. Complex change-of-use adjustments on high-value mixed-use assets are refused — too fact-sensitive.
4. GST group registrations are refused.
5. The non-resident supplier GST registration landscape is evolving — always check the invoice for NZ GST before assuming no input tax claim.
6. The 3/23 formula vs 3/20 depends on the accounting basis — confirm before building the workbook.
7. The secondhand goods credit (s.24) has been subject to legislative tightening — verify current requirements.
8. Crypto/digital asset transactions have no specific GST guidance as of April 2026 — flag for reviewer.

### Change log

- **v2.0 (April 2026):** Full rewrite to align with three-tier Accora architecture. 10-section Malta v2.0 structure adopted. Supplier pattern library added (Section 3). Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template added (Section 7). Bank statement guide with ANZ/Westpac/ASB/BNZ formats added (Section 8). Onboarding moved to fallback (Section 9).
- **v1.1 (April 2026):** Previous version with inline tier tags. Superseded.

### Self-check (v2.0)

1. Quick reference at top with single-rate table and conservative defaults: yes (Section 1).
2. Supplier library as literal lookup tables: yes (Section 3, 15 sub-tables).
3. Worked examples (hypothetical Auckland IT consultant): yes (Section 4, 6 examples).
4. Tier 1 rules compressed: yes (Section 5, 13 rules).
5. Tier 2 catalogue compressed: yes (Section 6, 15 items).
6. Excel template with mandatory recalc: yes (Section 7).
7. Onboarding as fallback only: yes (Section 9, 10 items).
8. All 8 NZ-specific refusals present: yes (Section 2, R-NZ-1 through R-NZ-8).
9. Reference material at bottom: yes (Section 10).
10. No reverse charge for fully taxable businesses explicit: yes (Section 5.5 + Example 1).
11. Non-resident GST registration landscape documented: yes (Section 5.6 + Section 3.8).
12. Entertainment 50% limitation explicit: yes (Section 5.11 + Example 3).
13. Vehicle logbook requirement explicit: yes (Section 5.10 + Example 6).
14. 3/23 formula explained: yes (Section 1 + Section 7).
15. Payments vs invoice basis distinction explicit: yes (Section 5.7 + Section 7).

## End of New Zealand GST Return Skill v2.0

This skill is incomplete without the companion workflow file loaded alongside it: `vat-workflow-base` v0.1 or later (Tier 1, workflow architecture). Do not attempt to produce a GST101A without it loaded.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
