---
name: new-zealand-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a New Zealand GST return (GST101A form) for a self-employed individual or small business in New Zealand. Trigger on phrases like "prepare GST return", "do the GST", "fill in GST101A", "create the return", "New Zealand GST", "NZ GST", or any request involving New Zealand GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill covers standard GST-registered persons under the invoice or payments basis. Financial services elections, GST groups, non-profit bodies, and complex change-of-use adjustments on high-value mixed-use assets are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any NZ GST work.
version: 2.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand GST

## New Zealand GST Guide (GST101A)

New Zealand goods and services tax (GST) for a self-employed person or small business: registration, the rate, taxable, zero-rated and exempt supplies, accounting basis, filing frequency and due dates, adjustments, records and penalties, plus a transaction classifier for the GST101A. Figures are for tax year 2026. In New Zealand that is the income year from 1 April 2026 to 31 March 2027, which Inland Revenue calls the 2027 income year. GST has no tax year of its own: it runs by taxable period, and the rules below stand until changed. This Guide covers the GST taxable periods that fall inside that year (for a 31 March balance date and two-monthly filing, the periods ending 31 May 2026 to 31 March 2027). The figures come from Inland Revenue (IRD) pages read on 22 September 2026, from the IR375 GST guide (March 2026 edition), from the IR295 guide (April 2026 edition) and from IRD interpretation statement IS 25/21 (8 October 2025). For box-by-box return preparation, use the sibling Guide `nz-gst-return`.

## Section 1: Quick reference

**Read this whole section before classifying anything. The workflow runbook is in `vat-workflow-base` Section 1. Follow that runbook with this Guide providing the country-specific content.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | New Zealand |
| Standard rate | See the rate table below; no reduced rates |
| Zero rate | See the IR375 table below (exports, going concerns, certain land sales) |
| Exempt | Financial services, renting a dwelling as a private home, donated goods and services sold by not-for-profit bodies, penalty interest |
| Return form | GST101A (GST Return) |
| Filing portal | myIR |
| Authority | Inland Revenue (IRD, Te Tari Taake) |
| Currency | NZD only |
| Filing frequencies | Monthly, 2-monthly or 6-monthly. Limits in the filing frequency table below |
| Deadline | 28th of the month after the taxable period ends. Period ending 31 March: 7 May. Period ending 30 November: 15 January. No extension of time is available |
| Registration threshold | See the registration tables below |
| Companion Guide (workflow) | `vat-workflow-base` v0.1 or later, must be loaded |
| Contributor | OpenAccountants community |
| Validation date | September 2026 source refresh |

**GST rate**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf |
| GST standard rate | 15% | IR295: "The current rate is 15%." |

**IR375: supplies, tax fraction and records**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| Zero-rated supplies are taxed at | 0% | "Some goods and services are not exempt supplies, but GST is charged at 0%." |
| Tax fraction (GST inside a GST-inclusive amount) | 3/23 | "15% of the GST exclusive amount or 3/23rds of the GST inclusive amount" |
| Registration test as IR375 words it | NZD 60,000 | "was over" ... "for the last 12 months, or is expected to go over" ... "for the next 12 months" |
| Records | 7 years | "Keep business records for 7 years." |

**Registration: the IRD web page**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/gst/registering-for-gst |
| Compulsory registration line (web page wording) | NZD 60,000 | "your turnover was at least" ... "in the last 12 months" |
| Voluntary registration below the line | NZD 60,000 | "You can choose to register for GST if your turnover from a taxable activity is less than" the amount |

**Registration: the Act as IRD's technical library states it**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-21.pdf?modified=20251023203446 |
| Section 51(1) threshold | NZD 60,000 | IS 25/21: "section 51(1)(a) which provides a person is liable to register for GST where the value of supplies" ... "exceeds" the amount "in a 12-month period" |
| Proviso: one-off spike | NZD 60,000 | "the Commissioner is satisfied that the value of supplies in the next 12-month period will not exceed" it |

**How to read the registration line.** The Act, as IRD's own interpretation statement and IR375 both word it, makes registration compulsory when supplies from all taxable activities **exceed** the amount in the tables above in the last 12 months, or are expected to exceed it in the next 12 months. The IRD web page says "at least". The wordings differ only at exactly the threshold amount. This Guide does not decide that case: refer a client at exactly that figure to an accountant. The test is a rolling 12 months, back or forward, not a tax-year total, and counts all the person's taxable activities together, including certain imported services the person receives. Anyone who carries on a taxable activity and adds GST to their prices must register whatever the turnover. If a one-off sale pushed the past 12 months over the line, registration is not compulsory where IRD (the Commissioner) is satisfied that supplies in the next 12 months will not exceed it.

**GST101A boxes** (full return work is in `nz-gst-return`; box wording from IR375)

| Box | Meaning |
| --- | --- |
| 5 | Total sales and income for the period, including GST and including zero-rated supplies |
| 6 | Zero-rated supplies (already included in Box 5) |
| 7 | Box 5 minus Box 6 |
| 8 | Box 7 multiplied by 3 and divided by 23 |
| 9 | Debit adjustments from the calculation sheet |
| 10 | Total GST collected on sales and income (Box 8 plus Box 9) |
| 11 | Total purchases and expenses, including GST, excluding imported goods |
| 12 | Box 11 multiplied by 3 and divided by 23 |
| 13 | Credit adjustments from the calculation sheet (for example bad debts) |
| 14 | Total GST credit for purchases and expenses (Box 12 plus Box 13) |
| 15 | Difference between Box 10 and Box 14. Box 10 bigger: GST to pay. Box 14 bigger: refund |

- **The tax fraction.** The GST101A uses GST-inclusive amounts on every basis; the basis decides only WHEN an item goes on the return. The GST inside an amount is the tax fraction in the IR375 table above.

**Conservative defaults**  _(NZ-specific values for the universal categories in vat-workflow-base Section 2)_

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Standard rate (the only positive rate) |
| Unknown GST status of a purchase | Not claimable (no input tax) |
| Unknown counterparty country | Domestic New Zealand |
| Unknown business-use proportion (vehicle, phone, home office) | No input tax |
| Unknown whether personal or business expense | Personal (no input tax) |
| Unknown non-resident supplier GST status | Assume not registered (no input tax claim) |
| Unknown whether transaction is in scope | In scope |

**Red flag thresholds**  _(country slot values for the reviewer brief in vat-workflow-base Section 3)_

The legacy amounts here were house heuristics, not IRD figures, and were removed. Always flag: a purchase over the change-of-use line in Section 5.8, any zero-rated sale, a material conservative default, and heavy reliance on one counterparty.

## Section 2: Required inputs and refusal catalogue

### Required inputs

- **Minimum viable.** Bank statement covering the full taxable period (CSV, PDF or pasted text), from any NZ or international bank.
- **Recommended.** Sales records for the period (especially for zero-rated supplies and exports), taxable supply information for purchases (see Section 5.4), the client's IRD number and GST number.
- **Ideal.** Complete sales and purchase journal, prior period GST101A, Xero or MYOB trial balance export, reconciliation of any adjustments.
- **Refusal policy if minimum is missing: SOFT WARN.** If no bank statement at all, hard stop. If bank statement only, proceed but record: "This GST101A was produced from bank statement alone. The reviewer must check that input tax claims are supported by the taxable supply information IR375 requires for the purchase size, and that all zero-rating conditions are met."

### NZ-specific refusal catalogue

If any trigger fires, stop, output the refusal message, end the conversation.

- **R-NZ-1: Financial services election (s.20F).** Trigger: client has elected to zero-rate financial services or asks about s.20F. Message: "Zero-rating financial services under s.20F needs specialist calculations. Please use a chartered accountant familiar with financial services GST."
- **R-NZ-2: GST groups.** Trigger: client is part of a GST group registration. Message: "GST group registrations require consolidated reporting and intra-group supply rules. Out of scope."
- **R-NZ-3: Non-profit bodies with donated goods.** Trigger: client is a non-profit using the donated goods exemption. Message: "Non-profit bodies have special GST rules for donated goods and services. Out of scope."
- **R-NZ-4: Complex change-of-use adjustments on high-value assets.** Trigger: client has a high-value mixed-use asset (for example a holiday home used partly for short-stay guests) requiring change-of-use adjustments under s.21 to 21H. Message: "Change-of-use adjustments for mixed-use assets above the IR375 line in Section 5.8 need a recalculation of taxable use every adjustment period. This is too fact-sensitive for this Guide. Please use a chartered accountant."
- **R-NZ-5: Compulsory zero-rating of land.** Trigger: client is selling or buying land between GST-registered persons. Message: "Land sales between registered persons are compulsorily zero-rated (s.11(1)(mb)) and need specific contract wording and notifications. Please use a property lawyer and chartered accountant."
- **R-NZ-6: Secondhand goods input tax credit.** Trigger: client regularly buys secondhand goods from unregistered persons and claims input tax on them. Message: "The secondhand goods credit has specific record and valuation rules. Please use a chartered accountant to confirm eligibility and amounts."
- **R-NZ-7: GST on imported services (s.8(4B)).** Trigger: client is a non-profit or makes significant exempt supplies and receives services from non-residents. Message: "The reverse charge on imported services under s.8(4B) applies when the recipient's taxable use falls below the threshold in Section 5.5. If your business makes exempt supplies, please use a chartered accountant."
- **R-NZ-8: Payments basis with large accruals.** Trigger: client uses payments basis but has significant unpaid invoices at period end that may distort the return. Message: "On the payments basis, GST follows payment, not invoicing. Include only paid amounts, and confirm your accounting basis with your accountant if unsure."

## Section 3: Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. Match by case-insensitive substring on the counterparty name; if several patterns match, use the most specific. If none match, fall through to Section 5. "Domestic 15%" means the standard rate in the Section 1 rate table; claimable purchases go in Box 11. Supplier names and GST status are a working list, not IRD data: the supplier's taxable supply information decides.

### 3.1 New Zealand banks (fees exempt, exclude)

**NZ banks table**

| Pattern | Treatment |
| --- | --- |
| ANZ, WESTPAC, ASB, BNZ, BANK OF NEW ZEALAND, KIWIBANK, TSB BANK, HEARTLAND BANK, CO-OPERATIVE BANK | EXCLUDE bank charges and fees (exempt financial service) |
| REVOLUT, WISE, N26 (fee lines) | EXCLUDE fees; check for separate taxable subscription invoices |
| INTEREST, INT | EXCLUDE, exempt |
| MORTGAGE, LOAN | EXCLUDE, principal is out of scope |

### 3.2 New Zealand government and statutory bodies (exclude entirely)

**Government bodies table**

| Pattern | Treatment |
| --- | --- |
| IRD, INLAND REVENUE, TE TARI TAAKE | EXCLUDE, tax payment |
| ACC, ACCIDENT COMPENSATION | EXCLUDE, levy is not a supply (see `nz-acc-levies`) |
| NZTA, WAKA KOTAHI, MINISTRY OF, DEPARTMENT OF, COMPANIES OFFICE, NZBN | EXCLUDE, government fees and levies |
| COUNCIL, CITY COUNCIL, DISTRICT COUNCIL (rates) | Read the rates invoice; IR375 treats rates as a cost carrying claimable GST |
| COUNCIL (consent fees, building permits) | Domestic 15% |

### 3.3 New Zealand utilities

**Utilities table**

| Pattern | Treatment |
| --- | --- |
| MERCURY, GENESIS, CONTACT, MERIDIAN, TRUSTPOWER, FLICK, NOVA, ELECTRIC KIWI, POWERSHOP | Domestic 15%, electricity |
| SPARK, VODAFONE NZ, ONE NZ, 2DEGREES, SKINNY, CHORUS, ENABLE, ULTRAFAST FIBRE | Domestic 15%, telecoms and broadband |
| WATERCARE, WELLINGTON WATER | Domestic 15%, water |

### 3.4 Insurance (read the invoice)

**Insurance table**

| Pattern | Treatment |
| --- | --- |
| IAG, STATE, AMI, NZI, AA INSURANCE, TOWER | General insurance: claim the GST shown on the invoice (IR375 treats insurance as a cost carrying GST) |
| SOUTHERN CROSS, PARTNERS LIFE, AIA NZ | Life cover is a financial service: EXCLUDE unless the invoice shows GST |
| INSURANCE, INS PREMIUM | Read the invoice |

### 3.5 Post and logistics

**Post and logistics table**

| Pattern | Treatment |
| --- | --- |
| NZ POST, COURIER POST, PACE, FASTWAY, ARAMEX NZ, TOLL, MAINFREIGHT, DHL NZ, FEDEX NZ, UPS NZ | Domestic 15% |

### 3.6 Transport

**Transport table**

| Pattern | Treatment |
| --- | --- |
| AIR NEW ZEALAND, JETSTAR (domestic) | Domestic 15% |
| AIR NEW ZEALAND (international) | Zero-rated, no GST to claim |
| AT HOP, METLINK, METRO CANTERBURY, UBER NZ, OLA NZ, INTERISLANDER, BLUEBRIDGE | Domestic 15% |
| RENTAL CAR, BUDGET NZ, HERTZ NZ, AVIS NZ | Domestic 15% |

### 3.7 Food retail (blocked unless hospitality business)

**Food retail table**

| Pattern | Treatment |
| --- | --- |
| COUNTDOWN, WOOLWORTHS NZ, PAK'N SAVE, PAKNSAVE, NEW WORLD, FOUR SQUARE, FARRO, MOORE WILSONS | Default BLOCK as personal. Food is standard-rated in NZ (it is not on IR375's zero-rated list); claim only if bought for the business |
| RESTAURANTS, CAFES, BARS | Default BLOCK, entertainment (Section 5.11) |

### 3.8 SaaS: non-resident suppliers (reverse charge or GST-registered)

- **Reverse charge explanation.** A fully taxable business has no reverse charge on imported services (Section 5.5). The overseas supplier either charges NZ GST (if registered, Section 5.6) or does not, and no claim arises where no GST was charged. An overseas supplier need not register if it only supplies GST-registered NZ businesses for business use, so a business customer that gives its GST number will often see no NZ GST.

**SaaS non-resident table** (working list; the invoice decides)

| Pattern | Treatment |
| --- | --- |
| GOOGLE, MICROSOFT, ADOBE, META, FACEBOOK ADS, SPOTIFY, CANVA | Often charge NZ GST: if on the invoice, domestic 15% |
| NOTION, ANTHROPIC, CLAUDE, OPENAI, CHATGPT, FIGMA | Often no NZ GST: no claim, cost is GST-free |
| GITHUB, SLACK, ATLASSIAN, ZOOM, DROPBOX | Check invoice: NZ GST charged, domestic 15%; not charged, no claim |

### 3.9 New Zealand SaaS / domestic suppliers

**NZ SaaS table**

| Pattern | Treatment |
| --- | --- |
| XERO, VEND (LIGHTSPEED), TIMELY, UNLEASHED, PUSHPAY, TRADE ME | Domestic 15% |
| STRIPE NZ | Check invoice: transaction fees may be exempt, subscription taxable |

### 3.10 Payment processors

**Payment processors table**

| Pattern | Treatment |
| --- | --- |
| STRIPE, PAYPAL, WINDCAVE, PAYMARK, DPS, EFTPOS NZ, AFTERPAY, LAYBUY | Check invoice: card and transaction fees are often exempt financial services; terminal rental and subscriptions are usually taxable |

### 3.11 Professional services (NZ)

**Professional services table**

| Pattern | Treatment |
| --- | --- |
| CHARTERED ACCOUNTANT, CA, CPA, LAWYER, SOLICITOR, BARRISTER, SURVEYOR, VALUER, ENGINEER | Domestic 15% if business purpose |

### 3.12 Payroll and statutory (exclude entirely)

**Payroll table**

| Pattern | Treatment |
| --- | --- |
| SALARY, WAGES, PAY, PAYE, KIWISAVER, ACC LEVY, STUDENT LOAN | EXCLUDE, outside GST |

### 3.13 Property and rent

**Property and rent table**

| Pattern | Treatment |
| --- | --- |
| RENT (commercial) | Domestic 15% |
| RENT (residential) | EXCLUDE, renting a dwelling as a private home is exempt |
| BODY CORPORATE | EXCLUDE if residential; read the levy invoice |
| RATES, COUNCIL RATES | Read the rates invoice (see 3.2) |

### 3.14 Internal transfers and exclusions

**Internal transfers table**

| Pattern | Treatment |
| --- | --- |
| TRANSFER, TFR, OWN ACCOUNT, DIVIDEND, LOAN REPAYMENT, DRAWINGS, OWNER DRAW | EXCLUDE |
| ATM, CASH WITHDRAWAL | Tier two: default exclude, ask what the cash was for |

### 3.15 Specific NZ patterns

**Specific NZ patterns table**

| Pattern | Treatment |
| --- | --- |
| BUNNINGS NZ, Mitre 10 | Domestic 15% if business tools or materials |
| THE WAREHOUSE | Default BLOCK, likely personal |
| NOEL LEEMING, PB TECH, MIGHTY APE | Domestic 15% if business asset |
| Z ENERGY, BP NZ, MOBIL NZ, CALTEX | Domestic 15% to the extent of business use |
| AA NZ (membership) | Domestic 15% if business |

## Section 4: Worked examples

Six classifications from a hypothetical Auckland software consultant's bank statement, payments basis, amounts in NZD.

### Example 1: Non-resident SaaS, no NZ GST (Notion)

**Input line:**
`2026-04-03 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; 16.00 US dollars ; 26.18 NZ dollars`

**Reasoning:**
No NZ GST on the invoice and no reverse charge for a fully taxable business (Section 5.5). An income tax expense only. Leave it out of Box 11, which is multiplied by the tax fraction.

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-03 | NOTION LABS INC | -26.18 | -26.18 | 0 | none | not in Box 11 | N | none | GST-free |

### Example 2: Non-resident SaaS, NZ GST charged (Google Ads)

**Input line:**
`2026-04-10 ; GOOGLE NEW ZEALAND LTD ; DEBIT ; Google Ads April 2026 ; -920.00`

**Reasoning:**
The invoice shows NZ GST at the standard rate. The 920.00 is GST-inclusive. GST = 920 x 3/23 = 120.00. Net = 800.00. Include 920.00 in Box 11; Box 12 picks up the GST.

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-10 | GOOGLE NZ | -920.00 | -800.00 | -120.00 | 15% | 11 | N | none | none |

### Example 3: Entertainment, full claim then annual adjustment

**Input line:**
`2026-04-15 ; THE GROVE RESTAURANT AUCKLAND ; DEBIT ; Client dinner ; -350.00`

**Reasoning:**
Private: no claim. Business entertainment: full cost in Box 11 now, then one annual GST adjustment for the part not deductible for income tax (Section 5.11). Conservative default: block until the business purpose is confirmed.

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-15 | THE GROVE RESTAURANT | -350.00 | -350.00 | 0 | none | none | Y | Q1 | "Entertainment: blocked until business purpose confirmed" |

### Example 4: Capital asset (business equipment)

**Input line:**
`2026-04-18 ; PB TECH AUCKLAND ; DEBIT ; MacBook Pro 16 ; -4,599.00`

**Reasoning:**
GST = 4,599 x 3/23 = 599.87. Net = 3,999.13. No separate capital goods box: the full amount goes in Box 11. The GST-exclusive cost is under the change-of-use line in Section 5.8, so no adjustment periods apply. If also used privately, the client uses the principal purpose or apportionment method (Section 5.8).

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-18 | PB TECH | -4,599.00 | -3,999.13 | -599.87 | 15% | 11 | N | none | none |

### Example 5: Export sale (zero-rated)

**Input line:**
`2026-04-22 ; ACME PTY LTD SYDNEY ; CREDIT ; Invoice NZ-2026-018 IT consulting March ; +8,500.00`

**Reasoning:**
IT consulting for an Australian company. Services to a non-resident outside NZ when performed can be zero-rated (s.11A(1)(k) in the legacy text) if not delivered to a third party in NZ and not related to NZ land or goods. Include in Box 5 and Box 6.

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-22 | ACME PTY LTD | +8,500.00 | +8,500.00 | 0 | 0% | 5 and 6 | Y | Q2 (HIGH) | "Check non-resident and outside-NZ conditions for zero-rating" |

### Example 6: Vehicle costs, no logbook

**Input line:**
`2026-04-28 ; Z ENERGY PARNELL ; DEBIT ; Fuel ; -102.00`

**Reasoning:**
GST on vehicle costs is claimable to the extent of business use, usually shown by a logbook (method in `nz-motor-vehicle-expenses-logbook-business-use`). No evidence: no claim. With a logbook: claim that share.

**Output table**

| Date | Counterparty | Gross | Net | GST | Rate | Box | Default? | Question? | Excluded? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-04-28 | Z ENERGY | -102.00 | -102.00 | 0 | none | none | Y | Q3 | "Vehicle fuel: no claim without a logbook or other evidence" |

## Section 5: Tier 1 classification rules (compressed)

### 5.1 Standard rate 15% (GST Act s.8(1))

- **Standard rate.** The rate in the Section 1 rate table is the only positive GST rate in New Zealand. There are no reduced rates. Sales go in Box 5; purchases with GST go in Box 11.

### 5.2 Zero-rated supplies (GST Act s.11, s.11A, s.11AB)

- **Zero-rated supplies.** IR375 lists exported goods, sales of going concerns (a business sold so that it will keep running as the same type of business), and sale of land where certain criteria are met; IR375 also treats international travel as a zero-rated supply. Financial services are exempt; zero-rating them is an election that R-NZ-1 refuses. Services to a non-resident outside NZ can be zero-rated if the conditions in Example 5 are met. Land between registered persons is compulsorily zero-rated: R-NZ-5 fires. A business with zero-rated supplies can still claim GST on its expenses. Report zero-rated sales in Box 5 and again in Box 6.

### 5.3 Exempt supplies (GST Act s.14)

- **Exempt supplies.** IR375 lists financial services (such as interest on loans and bank fees), donated goods and services sold by not-for-profit bodies, penalty interest, renting a dwelling for use as a private home, and residential accommodation under a head lease. GST is not charged on exempt supplies and they are not included in the GST return. You cannot claim GST on expenses relating to exempt supplies.

### 5.4 Input tax credits (GST Act s.20(3))

- **Taxable supply information, not tax invoices.** From 1 April 2023 the tax invoice requirement was replaced by a requirement to provide and keep **taxable supply information** (TSI). It no longer needs to be one physical document: invoices, contracts and records can together hold it. What the buyer must hold depends on the GST-inclusive size of the supply:

**Taxable supply information bands**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| No TSI needs to be given at or below | NZD 200 | "(including GST), you do not need to provide taxable supply information to the buyer"; both sides still keep records |
| Middle band upper limit | NZD 1,000 | Seller name, GST number, date, description, and either the GST-exclusive amount, GST amount and GST-inclusive amount, or the GST-inclusive amount with a statement that GST is included |
| Full details above | NZD 1,000 | As above, plus the buyer's name and one contact detail if the buyer is GST registered |

Claim GST only when you hold the TSI for that band. On the payments basis, claim when paid; on the invoice basis, when invoiced (Section 5.7).

### 5.5 No reverse charge for fully taxable businesses

- **No reverse charge for fully taxable businesses.** NZ does not require a fully taxable business to self-assess GST on imported services. The reverse charge in s.8(4B) catches a recipient whose taxable use of the imported services is below the threshold in the table below, for example a business that also makes exempt supplies. For a self-employed consultant making only taxable supplies, no reverse charge applies.

**Reverse charge threshold**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.taxtechnical.ird.govt.nz/new-legislation/act-articles/taxation-annual-rates-returns-filing-and-remedial-matters-act-2012/gst/reverse-charge-for-imported-services |
| Threshold for the intended-use and actual-use tests | 95% | "to bring this threshold in line for the initial test of "percentage intended use"" |

### 5.6 Non-resident supplier registration

- **Non-resident supplier registration.** An overseas business supplying remote services (digital content, apps, software, consultancy and similar) to NZ resident consumers must register and charge GST once its supplies to NZ customers pass the line in the table below. It need not register if it only supplies GST-registered NZ businesses for their business use. Check the invoice: if NZ GST is on it and you hold the TSI, treat it as a domestic purchase. If there is no NZ GST, there is no claim.

**Remote services registration**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/gst/gst-for-overseas-businesses/supplying-remote-services-into-new-zealand |
| Overseas supplier must register when supplies to NZ customers pass | NZD 60,000 | "in the last 12 months, or are expected to be more than" the amount "in the next 12 months" |

### 5.7 Payments basis vs invoice basis

- **Payments basis vs invoice basis.** Invoice basis: GST when you invoice (or are paid first) and when a supplier invoices you, paid or not. Payments basis: GST when paid or received. Hybrid: invoice basis for sales, payments basis for purchases; IRD says small businesses rarely use it because of the cashflow cost. For invoice-basis clients, ask for the invoice register.

**Accounting basis and filing frequency**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use |
| Payments basis allowed if total sales are at or below | NZD 2 million | Or likely to be in "any 12-month period beginning on the first day of a month" |
| Monthly filing compulsory above | NZD 24 million | "You must file monthly if your sales are over" it; anyone may choose monthly |
| 2-monthly filing allowed below | NZD 24 million | "Anyone with sales under" it "in any 12-month period" |
| 6-monthly filing allowed below | NZD 500,000 | "Anyone with sales under" it "in any 12-month period" |

For a GST group each limit applies to the group as a whole. With a 31 March balance date, 2-monthly filers file for periods ending in odd months (May, July, September, November, January, March), and 6-monthly filers for periods ending 30 September and 31 March.

**Due dates.** A return is needed for every taxable period, even a nil one, and payment is due the same day as the return. See the deadline row in Section 1 and the page https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst ("The GST return for the taxable period ending 31 March is due by 7 May.").

### 5.8 Change-of-use adjustments (s.21-21H)

- **Change-of-use adjustments.** When goods or services are used partly for taxable and partly for private or exempt purposes, IR375 sets these rules:
  - Costing the GST-exclusive line in the table below or less: choose the principal purpose method (claim all the GST if the main purpose is business, none if not) or the apportionment method. Once you choose apportionment you must use it for all such purchases for a minimum of 24 months. No later adjustment is needed.
  - Costing more: claim on intended use, then compare actual use at the end of each adjustment period. No adjustment is needed if the change in taxable use is less than the percentage in the table AND the adjustment is the dollar figure in the table or less. A permanent change of use needs an adjustment even inside that threshold.
  - Debit adjustments go in Box 9, credit adjustments in Box 13. If complex, R-NZ-4 fires.

**Change-of-use thresholds and adjustment periods**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| Principal purpose or apportionment choice, GST-exclusive cost up to | NZD 10,000 | "(excluding GST)"; adjustment periods "Not required" |
| Cost from NZD 10,001 to NZD 20,000 | 2 adjustment periods | IR375 adjustment periods table |
| Cost from NZD 20,001 to NZD 500,000 | 5 adjustment periods | same table |
| Over NZD 500,000 or land of any value | 10 adjustment periods | "or land (of any value)" |
| No adjustment if the change in use is less than | 10% | "within the 10% or" dollar "threshold" |
| and the adjustment is at most | NZD 1,000 | same sentence |

### 5.9 Secondhand goods (s.24(5))

- **Secondhand goods.** A registered person buying secondhand goods from an unregistered seller may be able to claim a GST credit. IR375 requires the buyer to keep the seller's name and address, the date, a description and the consideration. Claim through Box 11. The section number in the heading is legacy and unchecked.

### 5.10 Motor vehicles

- **Motor vehicles.** No blanket block. GST is claimable to the extent of business use, under the Section 5.8 rules for the vehicle's cost. Logbook method: `nz-motor-vehicle-expenses-logbook-business-use`. Fringe benefit tax is outside this Guide.

### 5.11 Entertainment: full claim, annual adjustment

- **Entertainment.** You cannot claim GST on private entertainment. For business entertainment, IR375 says to keep showing the total cost in Box 11 during the year, then make one GST adjustment a year on the part that is not deductible for income tax. The adjustment is the percentage in the table below applied to the GST-exclusive non-deductible amount. Show it on the IR372 calculation sheet under entertainment expenses and carry it to Box 9. Timing: the return covering the earlier of the income tax return's due date or filing date (no tax agent); the earlier of filing or 31 March after the due date (tax agent); the actual filing date (tax agent with an extension). Bodies not liable for income tax, such as charities, make no adjustment. Which items are limited is an income tax question (IRD guide IR268).

**Entertainment**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf |
| Share of business entertainment usually deductible for income tax | 50% | "only 50% of business entertainment expenses are deductible for income tax" (column text interleaved in the PDF) |
| Annual GST adjustment | 15% | "make a GST adjustment of 15% of the GST-exclusive non-deductible amount once a year" (column text interleaved) |

### 5.12 Goods and services purchased from non-residents

- **Goods and services purchased from non-residents.** If the non-resident supplier charges NZ GST: treat as a domestic purchase and claim, holding the TSI. If no GST is charged: no claim for a fully taxable business; the cost is still deductible for income tax. If the recipient makes exempt supplies, the reverse charge in Section 5.5 may apply: R-NZ-7 fires. Imported goods are excluded from Box 11; GST paid to Customs on imports is outside this Guide.

### 5.13 Bad debts (s.26)

- **Bad debts.** A registered person on the invoice or hybrid basis who has returned GST on a sale and later writes off all or part of the debt makes a credit adjustment in the period of the write-off: 3/23 of the amount written off, in Box 13. Keep a record of the steps taken to recover the debt. If the debt is later recovered, include 3/23 of the amount recovered as a debit adjustment in Box 9. On the payments basis, no GST was returned on an unpaid sale, so there is normally nothing to adjust; IR375 allows an adjustment for door-to-door sales and hire purchase agreements on the payments basis.

### 5.14 Penalties and interest

- **Late filing.** The GST late filing penalty depends on the accounting basis when the return is due. There is no extension of time for a GST return.
- **Late payment.** A penalty the day after the due date, then another on the 7th day on the remaining tax including penalties. The monthly late payment penalty that applies to other taxes does **not** apply to GST. Use-of-money interest runs on unpaid GST.

**Late filing penalties**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties |
| Late filing, payments basis, per return | NZD 50 | "if you&rsquo;re on the payments basis" |
| Late filing, invoice or hybrid basis, per return | NZD 250 | "penalty for late filing on the hybrid or invoice basis" |

**Late payment penalties**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties |
| Day after the due date | 1% | "1% penalty on the day after payment due date" |
| 7th day after the due date, on remaining tax including penalties | 4% | "4% penalty for remaining tax including penalties on 7th day after payment due date" |
| Monthly penalty | does not apply to GST | "(except for GST, income tax including provisional tax, and Working for Families overpayments)" |

A first late payment in a 2-year period may get a grace period before penalties are charged.

**Use-of-money interest**

| What | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments |
| Rate IRD charges on underpaid tax, from 16 January 2026 | 8.97% | "16 January 2026 8.97% 2.25%" |
| Rate IRD pays on overpaid tax, from 16 January 2026 | 2.25% | same row |
| No interest on amounts under | NZD 100 | "amounts under" |

The rates change over time; read the newest row of the IRD table.

### 5.15 Records

- **Records.** Keep business records for the period in the Section 1 IR375 table: TSI, supply correction information (which replaced credit and debit notes), bank statements and the cashbook.

## Section 6: Tier 2 catalogue (compressed)

### 6.1 Vehicle costs

- Pattern: Z Energy, BP, Mobil, Caltex, vehicle lease. Default: no claim (no logbook). Question: "Do you have a vehicle logbook? What is your business-use share?"

### 6.2 Entertainment

- Pattern: restaurants, bars, cafes, catering. Default: block. Question: "Was this business entertainment? If yes, it goes in full in Box 11 and an annual adjustment follows (Section 5.11)."

### 6.3 Non-resident SaaS: GST status unknown

- Pattern: overseas SaaS with no clear GST line. Default: no claim. Question: "Does the invoice show NZ GST? What is the supplier's NZ GST number?"

### 6.4 Round-number incoming transfers

- Pattern: large round credit from the owner. Default: exclude as capital. Question: "Is this a customer payment, your own funds, or a loan?"

### 6.5 Incoming from individuals

- Pattern: incoming from private names. Default: taxable sale at the standard rate, Box 5. Question: "Was it a sale? What was supplied?"

### 6.6 Incoming from overseas

- Pattern: foreign currency or non-NZ bank. Default: zero-rated, Boxes 5 and 6. Question: "Is the customer a non-resident outside NZ? Confirm zero-rating conditions."

### 6.7 Large purchases (potential high-value asset)

- Pattern: single purchase above the change-of-use line in Section 5.8. Default: include in Box 11 and flag for adjustment periods. Question: "Is this a capital asset? Will it be used only for business?"

### 6.8 Mixed-use phone, internet, home office

- Pattern: Spark, One NZ personal lines; home power bills. Default: no claim if mixed. Question: "Is this a dedicated business line or mixed-use? Do you use the principal purpose or apportionment method?"

### 6.9 Outgoing to individuals

- Pattern: outgoing to private names. Default: exclude as drawings. Question: "Was this a contractor payment, salary, or personal transfer?"

### 6.10 Cash withdrawals

- ATM, cash withdrawal. Default: exclude. Ask what the cash was for.

### 6.11 Rent payments

- Pattern: monthly rent. Default: commercial (taxable, claimable). Question: "Is this commercial or residential?"

### 6.12 Trade Me / marketplace sales

- Pattern: Trade Me payouts. Default: taxable sale, Box 5. Trade Me fees: domestic, Box 11. Question: "Are these business sales or personal item disposals?" Sales of private property are not included in a GST return.

### 6.13 Airbnb income

- Pattern: Airbnb payouts. Default: flag for reviewer; change-of-use rules may apply if the property was private. Question: "Is this a dedicated rental property or your private home? What is the taxable-use share?"

### 6.14 Secondhand goods purchases

- Pattern: purchases from individuals, estate sales, auctions. Default: no claim unless the Section 5.9 conditions and records are met. Question: "Was this bought from an unregistered seller? Do you have the seller's name and address?"

### 6.15 Foreign currency transactions

- Pattern: non-NZD amounts. Default: use the NZD amount on the bank statement. Question: "Confirm the NZD equivalent on the bank statement."

## Section 7: Excel working paper template (NZ-specific)

The base specification is in `vat-workflow-base` Section 3. This section provides the NZ-specific overlay.

### Sheet "Transactions"

Columns A to L per the base. Column H ("Box") accepts GST101A box numbers (5, 6, 11 and so on). NZ has no reverse charge boxes for fully taxable businesses.

### Sheet "Field Summary"

One row per GST101A box. All amounts are GST-inclusive, whatever the accounting basis:

~~~
| 5 | Total sales and income (incl. GST) | =SUM of all sales transactions |
| 6 | Zero-rated supplies | =SUMIFS(Transactions!D:D, Transactions!H:H, "6") |
| 7 | Box 5 minus Box 6 | =C[5]-C[6] |
| 8 | GST on sales | =C[7]*3/23 |
| 9 | Debit adjustments | =manual entries only |
| 10 | Total GST collected | =C[8]+C[9] |
| 11 | Purchases and expenses (incl. GST) | =SUM of purchases carrying NZ GST |
| 12 | GST on purchases | =C[11]*3/23 |
| 13 | Credit adjustments | =manual entries (bad debts, change of use) |
| 14 | Total GST credit | =C[12]+C[13] |
| 15 | GST to pay or refund | =C[10]-C[14] | ~~~

**Note on accounting basis:** the basis decides which transactions fall in the period, not whether amounts include GST.

### Sheet "Return Form"

Final GST101A-ready figures:

~~~
Box 10 = Total GST collected
Box 14 = Total GST credit

Box 15 = difference between Box 10 and Box 14

Box 10 bigger: GST to pay to IRD
Box 14 bigger: refund due from IRD
~~~

### Mandatory recalc step

After building the workbook, run:

~~~bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/nz-gst-PERIOD-working-paper.xlsx
~~~

## Section 8: New Zealand bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these NZ-specific patterns.

**Export formats (legacy, not checked against the banks).** ANZ: Date (DD/MM/YYYY), Transaction Details, Amount (negative for debits), Balance. Westpac: Date, Amount, Other Party (the counterparty), Description, Reference, Particulars, Analysis Code. ASB: Date (YYYY-MM-DD), Unique Id, Tran Type, Cheque Number, Payee, Memo, Amount. BNZ: Date (DD/MM/YYYY), Amount, Payee, Particulars, Code, Reference, Tran Type, This Party Account. Kiwibank: Date, Description, Amount, Balance.

**Common NZ bank statement patterns**

| Term | Meaning |
| --- | --- |
| Visa Purchase, EFTPOS | Card purchase (debit) |
| Direct Debit, D/D | Pre-authorised direct debit |
| Automatic Payment, A/P | Scheduled automatic payment |
| Direct Credit, D/C | Incoming direct credit |
| Transfer, TFR | Internal transfer |
| ATM W/D | Cash withdrawal |
| BNPL | Buy now pay later (Afterpay, Laybuy) |
| Particulars / Code / Reference | NZ-specific 3-field payment reference system |

**NZ payment reference system.** Particulars, Code and Reference: three freeform fields of 12 characters each, often holding invoice numbers. Read all three.

**Internal transfers.** "transfer", "TFR" or matching account numbers: exclude.

**Sole trader draws.** Transfers to personal accounts are drawings: exclude.

**ACC levies.** Not a supply: exclude (`nz-acc-levies`).

**IRD payments.** "IRD" or "INLAND REVENUE" (GST, provisional tax, PAYE): exclude (`nz-provisional-tax`).

**Refunds and reversals.** "refund", "reversal", "credit adj": book as a negative in the original box.

**Foreign currency.** Use the NZD amount the bank debited or credited; note the rate in column L.

## Section 9: Onboarding fallback (only when inference fails)

### 9.1 Entity type

- Inference rule: personal name = sole trader; "Ltd", "Limited" = company; "LP" = limited partnership. Fallback: "Are you a sole trader, partnership, company, or look-through company?"

### 9.2 GST registration

- Inference rule: if asking for a GST101A, they are registered. Fallback: "Are you GST-registered? What is your GST number?" If not registered, test the registration line in Section 1.

### 9.3 Accounting basis

- Inference rule: small businesses often use the payments basis. If a Xero or MYOB export shows accrual data, likely invoice basis. Fallback: "Are you on the invoice, payments or hybrid basis?"

### 9.4 Filing period

- Inference rule: transaction date range. 2-monthly is most common. Fallback: "Is this a 1-month, 2-month, or 6-month GST period? What are the dates?"

### 9.5 Industry

- Inference rule: counterparty mix. Fallback: "In one sentence, what does the business do?"

### 9.6 Employees

- Inference rule: PAYE, KiwiSaver or wages outgoing. Fallback: "Do you have employees?"

### 9.7 Exempt supplies

- Inference rule: financial services, residential rental income patterns. Fallback: "Do you make any GST-exempt supplies (financial services, residential rental)?"

### 9.8 Zero-rated supplies

- Inference rule: foreign currency incoming, overseas counterparties. Fallback: "Do you export goods or provide services to customers outside NZ?"

### 9.9 Prior period balance

- Not inferable. Always ask. "Do you have any GST owing or refund due from the previous period?"

### 9.10 Vehicle use

- Inference rule: fuel purchases, vehicle-related charges. Fallback: "Do you use a vehicle for business? Do you have a logbook?"

## Section 10: Reference material

### Validation status

Version 2.1, September 2026. Section numbers of the GST Act in headings are legacy; the consolidated Act could not be read, and only s.8(4B) and s.51 were seen quoted on an IRD page.

### Sources

Official pages: see Sources at the end. Legislation: Goods and Services Tax Act 1985; Tax Administration Act 1994; Income Tax Act 2007 subpart DD.

### Known gaps

1. Financial services election (s.20F) is refused.
2. Compulsory zero-rating of land is refused.
3. Complex change-of-use adjustments on high-value mixed-use assets are refused.
4. GST group registrations are refused.
5. The overseas-supplier landscape changes: always check the invoice for NZ GST before assuming no claim.
6. The secondhand goods credit has specific record rules: check current requirements.
7. Crypto and digital asset transactions: flag for reviewer (see `new-zealand-crypto-tax`).
8. GST on imported goods paid to Customs is not covered.

### Change log

- **v2.1 (September 2026):** Refresh against IRD pages: GST101A boxes, taxable supply information, change-of-use thresholds, entertainment, penalties and interest, registration wording.
- **v2.0 (April 2026):** Rewrite to the three-tier OpenAccountants architecture.
- **v1.1 (April 2026):** Superseded.

### Self-check (v2.0)

Kept from v2.0: quick reference, 15 supplier sub-tables, 6 worked examples, Tier 1 and Tier 2 rules, Excel template, bank guide, onboarding fallback, 8 refusals. Explicit: no reverse charge for fully taxable businesses, overseas supplier registration, entertainment, vehicle business use, tax fraction, payments vs invoice basis.

## The method, step by step

1. **Registration.** Test whether the person must be registered: supplies from all taxable activities over a rolling 12 months, back and forward, against the line in the registration tables in Section 1 (s.51 as quoted in IRD's IS 25/21, https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-21.pdf?modified=20251023203446). Registered persons continue.
2. **Basis and period.** Confirm the accounting basis and filing frequency the person chose, and check they still qualify under the limits in Section 5.7 (https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use). This fixes which transactions fall in the period.
3. **Classify.** Classify every transaction with Section 3, then Section 5: standard-rated, zero-rated, exempt, or outside GST. Drop exempt and out-of-scope items. For purchases, claim only where the taxable supply information for the size band is held (IR375, https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf).
4. **Adjustments.** Work out adjustments on the IR375 calculation sheet: change of use (Section 5.8), bad debts (Section 5.13), the annual entertainment adjustment (Section 5.11). Debit adjustments to Box 9, credit adjustments to Box 13.
5. **Complete the GST101A.** Fill Boxes 5 to 15 with GST-inclusive amounts and the tax fraction, per IR375 (https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf). Box-by-box detail is in `nz-gst-return`.
6. **File and pay by the due date.** File and pay by the 28th of the month after the period, 7 May for a period ending 31 March, 15 January for a period ending 30 November (https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst). Late returns and payments attract the penalties and interest in Section 5.14.

## Ask the client first

- Are you GST-registered, and if not, what were your sales in the last 12 months and what do you expect in the next 12? (Decides whether registration is compulsory.)
- Are you on the payments, invoice or hybrid basis, and how often do you file? (Decides which transactions fall in the period.)
- Do you make any exempt supplies, such as residential rent or financial services? (Blocks related claims and can trigger the reverse charge on imported services.)
- Do any sales go to overseas customers, and were those customers outside New Zealand when you did the work? (Decides zero-rating.)
- Do you use any asset or expense partly for private purposes, and did you choose the principal purpose or apportionment method? (Decides change-of-use treatment.)
- Did you spend money on business entertainment this year, and when is your income tax return due or filed? (Decides the annual entertainment adjustment and its timing.)

## When to refuse or refer

- Any trigger in the Section 2 refusal catalogue (financial services election, GST groups, not-for-profit donated goods, high-value mixed-use assets, land between registered persons, regular secondhand goods claims, imported services with exempt supplies).
- Turnover sitting at exactly the registration amount: the IRD web page and the Act as IRD quotes it word the test differently. Refer to an accountant.
- Imported goods and Customs GST, non-resident registrations, short-stay accommodation with private use.
- Income tax questions (entertainment items, vehicle logbooks, provisional tax): route to `nz-income-tax-ir3`, `nz-motor-vehicle-expenses-logbook-business-use` or `nz-provisional-tax`.
- A disputed default assessment or an IRD audit.

## Sources

- https://www.ird.govt.nz/gst/registering-for-gst
- https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use
- https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst
- https://www.ird.govt.nz/gst/gst-for-overseas-businesses/supplying-remote-services-into-new-zealand
- https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties
- https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties
- https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments
- https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf
- https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir200---ir299/ir295/ir295.pdf
- https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-21.pdf?modified=20251023203446
- https://www.taxtechnical.ird.govt.nz/new-legislation/act-articles/taxation-annual-rates-returns-filing-and-remedial-matters-act-2012/gst/reverse-charge-for-imported-services

## End of New Zealand GST Guide

This Guide works with the companion workflow file `vat-workflow-base` v0.1 or later. Do not produce a GST101A without it loaded.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The latest version of this Guide is kept on the OpenAccountants website, where you can also request a professional review from a licensed accountant and track updates as tax law changes.

> Contributed by OpenAccountants.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
