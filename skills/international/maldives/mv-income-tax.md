---
name: maldives-income-tax
description: Use this skill whenever asked about Maldives (Maldivian) personal/individual income tax for self-employed individuals, sole proprietors, or employees. Trigger on phrases like "how much income tax do I pay in the Maldives", "MIRA", "EWT", "employee withholding tax", "MIRA 601", "income tax return Maldives", "interim payment", "tax-free threshold MVR 720,000", "MVR 60,000 a month", "MRPS", "pension contribution Maldives", "self-employed tax Maldives", "income tax registration threshold", or any question about filing or computing income tax for a self-employed or employed client in the Maldives. Also trigger when preparing or reviewing the individual income tax return or an EWT return, computing the progressive income-tax bands, or advising on interim payments and pension. Despite stale secondary sources that claim "the Maldives has no income tax", the Maldives DOES levy a personal income tax under the Income Tax Act (Law No. 25/2019). This skill covers the progressive income-tax brackets, employee withholding tax (EWT), interim/final filing for the self-employed, registration thresholds, the Maldives Retirement Pension Scheme (MRPS), GST context, and penalties. ALWAYS read this skill before touching any Maldives income tax work.
jurisdiction: MV
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# maldives-income-tax

## Maldives Income Tax -- Self-Employed Skill v0.1

> **CRITICAL — the Maldives DOES have a personal income tax.** Some secondary aggregators (e.g. TaxAtlas) still state "the Maldives has no personal income tax." That is **WRONG**. The Maldives introduced a personal/individual income tax under the **Income Tax Act, Law No. 25/2019** (ratified 17 December 2019). Income tax commenced 1 January 2020; taxation of remuneration (employment income) began 1 April 2020. The country has no historical tradition of income tax, which is why stale summaries claim none exists. Treat the **Income Tax Act (Law No. 25/2019)** and the **Maldives Inland Revenue Authority (MIRA)** as the governing authority.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Maldives |
| Tax | Individual / Personal Income Tax |
| Currency | Maldivian Rufiyaa (MVR). Approx. USD 1 ≈ MVR 15.4 (pegged band) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act, Law No. 25/2019 (ratified 17 Dec 2019; income tax from 1 Jan 2020; remuneration from 1 Apr 2020) |
| Supporting legislation | Income Tax Regulation; Tax Administration Act & Tax Administration Regulation (penalties); GST Act, Law No. 10/2011 (7th Amendment, Law ratified 5 Nov 2024); Maldives Pension Act (MRPS) |
| Tax authority | Maldives Inland Revenue Authority (MIRA), mira.gov.mv |
| Pension authority | Maldives Pension Administration Office (MPAO), pension.gov.mv |
| Filing portal | MIRAconnect |
| Tax-free threshold | MVR 720,000 / year (= MVR 60,000 / month) — built into the bracket structure [Income Tax Act, Law No. 25/2019; RCO Lawyers guide] |
| Validated by | Pending — requires sign-off by a Maldives-qualified tax practitioner |
| Validation date | Pending |
| Skill version | 0.1 |

### Individual Income Tax — Annual Brackets (Tax Year 2025)

**Individual Income Tax — Annual Brackets (Tax Year 2025)**  _(Income Tax Act, Law No. 25/2019)_

| Annual taxable income (MVR) | Rate | Tax within band | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0 – 720,000 | 0% | MVR 0 | MVR 0 |
| 720,001 – 1,200,000 | 5.5% | 5.5% × 480,000 = 26,400 | MVR 26,400 |
| 1,200,001 – 1,800,000 | 8% | 8% × 600,000 = 48,000 | MVR 74,400 |
| 1,800,001 – 2,400,000 | 12% | 12% × 600,000 = 72,000 | MVR 146,400 |
| Above 2,400,000 | 15% | — | — |

- **Resident vs non-resident tax base** — Residents are taxed on worldwide income; non-residents / temporary residents are taxed on Maldives-source income only.  _(Income Tax Act, Law No. 25/2019)_
- **Tax-free threshold** — MVR 720,000 / year (= MVR 60,000 / month). Built into the bracket structure — there is no separate personal allowance.  _(Income Tax Act, Law No. 25/2019; RCO Lawyers, Current Tax Rates in Maldives)_
- **Tax computation method** — Tax is computed by allocating total taxable income across the bands and applying each marginal rate.

Bracket source: RCO Lawyers (rcolawyers.com/guides/2-current-tax-rates-in-maldives/). Authority page: MIRA (mira.gov.mv/Pages/View/ictindividuals). The MVR 720,000 / 5.5% / 8% / 12% / 15% structure is internally consistent with the monthly EWT bands below (annual = monthly × 12), which cross-confirms it.

**[RESEARCH GAP — reviewer to confirm]** The live MIRA page returns HTTP 403 to automated fetches. The annual bracket figures above come from a Maldives law-firm guide (RCO Lawyers), corroborated by the independently-sourced monthly EWT brackets, but were not read directly off the rendered MIRA page or the Income Tax Act PDF. A human should re-check against the Income Tax Act PDF (mira.gov.mv/Legislations/View/Incometaxact) before relying on the exact statutory bands.

### Employee Withholding Tax (EWT) — Monthly Brackets

**Employee Withholding Tax (EWT) — Monthly Brackets**  _(MIRA, EWT rates and brackets, mira.gov.mv/Pages/View/ictewt; mira.gov.mv/Guides/View/wt_rates_and_brackets; launch announcement edition.mv/news/15888)_

| Monthly remuneration (MVR) | EWT rate |
| --- | --- |
| 0 – 60,000 | 0% (exempt) |
| 60,000 – 100,000 | 5.5% |
| 100,000 – 150,000 | 8% |
| 150,000 – 200,000 | 12% |
| 200,000+ | 15% |

- **EWT withholding scope** — The employer withholds only on the portion of monthly remuneration above MVR 60,000.
- **EWT form & deadline** — File EWT Return MIRA 601 online via MIRAconnect; due the 15th day of the following month, with payment by the same date. Monthly returns are required for every month once an employer has any EWT obligation, even nil months thereafter.  _(MIRA, mira.gov.mv/Pages/View/ewtfile; form mira.gov.mv/Forms/View/mira-601-Employee-Withholding-Tax-Return)_

**WARNING — do NOT use Rivermate's EWT table.** Rivermate (rivermate.com/guides/maldives/taxes) publishes a different, conflicting EWT table (5%/10%/15%/20% on MVR 5,000–16,667 monthly bands). It does not match the official Income Tax Act structure and appears fabricated/outdated. Use the 5.5% / 8% / 12% / 15% set above.

### Maldives Retirement Pension Scheme (MRPS) — Contributions

**Maldives Retirement Pension Scheme (MRPS) — Contributions**  _(Maldives Pension Act; MPAO, pension.gov.mv/en/mrps)_

| Party | Contribution |
| --- | --- |
| Employee | 7% of pensionable wage |
| Employer | 7% of pensionable wage (minimum) |
| **Total** | **14%** |

*Self-check: 7% (employee) + 7% (employer) = 14% total. ✓*

- **Employer election to pay full contribution** — The employer may elect to pay the full 14% without deducting the employee share, but must pay at least 7%.  _(MPAO)_
- **Pensionable wage** — The basic salary stated in the employment contract (definition effective 1 May 2010; set by the Pension Office Board). Allowances are generally excluded.  _(MPAO, old.pension.gov.mv/en/scheme/maldives-retirement-pension-scheme-en)_

**Self-employed contributors:** annual contributions must not exceed the annual mandatory contribution of the highest-paid state employee (effective ceiling). **[RESEARCH GAP — reviewer to confirm]** No general statutory floor/ceiling for standard (non-self-employed) employees was found on the official MPAO page.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency | STOP — do not pick a tax base without confirming resident vs non-resident/temporary |
| Unknown employment vs self-employment | Treat employment income via EWT; self-employment via the individual return |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether income is Maldives-source (non-resident) | Treat as Maldives-source (taxable) until confirmed |
| Unknown GST registration status | Assume not registered; flag if turnover near MVR 1,000,000 |
| Unknown pensionable wage | Use the contractual basic salary only |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of (a) residency status (resident / non-resident / temporary resident) and (b) income type (employment via EWT vs self-employment / sole proprietor).

**Recommended** — all sales invoices, purchase invoices/receipts, EWT statements from employers (for employees), MRPS contribution records, prior-year income tax return or MIRA assessment, GST registration status.

**Ideal** — complete income and expenditure account, asset register, interim payment confirmations, employment income details and EWT already withheld.

**Refusal if minimum is missing — SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This Maldives income tax computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that the wholly-and-exclusively-for-business test is met."

### Refusal Catalogue

- **R-MV-1 — Residency unknown** — "Residency determines the tax base — residents are taxed on worldwide income, non-residents and temporary residents on Maldives-source income only. This skill cannot compute tax without confirmed residency status. Please confirm before proceeding."
- **R-MV-2 — Companies, partnerships, banks** — "This skill covers individuals (employees, sole proprietors, self-employed) only. Company/business income tax (15% above MVR 500,000; 25% for banks) and partnership returns are out of scope. Escalate to a Maldives-qualified tax practitioner."
- **R-MV-3 — Non-resident withholding tax (NWT)** — "Non-resident withholding tax on dividends, interest, royalties, and management/service fees (typically 5–10%) is a separate regime. Out of scope. Escalate to a qualified practitioner."
- **R-MV-4 — Tourism sector specifics** — "Tourism-sector taxation (TGST at 17% from 1 July 2025, green tax, tourism-specific rules) requires specialised analysis. For income tax it is in scope, but TGST/tourism levies are not. Escalate where tourism-specific levies are involved."
- **R-MV-5 — Arrears / enforcement** — "Client has outstanding tax arrears or is subject to MIRA enforcement. Late-payment penalties (0.05%/day, capped at the greater of twice the tax or MVR 250,000) are severe. Do not advise. Escalate to a qualified practitioner immediately."
- **R-MV-6 — GST return requested** — "This skill covers income tax and EWT only. For Maldives GST (GGST 8% / TGST 17%, MIRA 105/return), use a dedicated GST skill or escalate."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. Maldivian statements are usually in English (with some Dhivehi terms); amounts are in MVR unless flagged USD (common for tourism / TGST).

### 3.1 Income Patterns (Credits on Bank Statement)

**3.1 Income Patterns (Credits on Bank Statement)**

| Pattern | Return Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Business income | Self-employment revenue | If GST-registered, extract net of GST (8% GGST) |
| FEES, PROFESSIONAL FEES, CONSULTANCY, SERVICE FEE | Business income | Self-employment revenue | Typical for self-employed |
| STRIPE PAYOUT, PAYPAL PAYOUT, WISE PAYOUT | Business income | Platform payout | Match to underlying invoices; net of platform commission |
| UPWORK, FIVERR, TOPTAL | Business income | Freelance platform | Net of platform commission |
| SALARY, REMUNERATION, EMPLOYER [name], MUSAARA | Employment income | Remuneration (subject to EWT, not the self-employed return) | EWT withheld by employer at source |
| RENT RECEIVED, KUYYEE | Rental income | Other income | Not self-employment income |
| INTEREST RECEIVED | Investment income | Other income | Interest income |
| DIVIDEND | Investment income | Other income | Dividend income (may be subject to NWT for non-residents) |
| MIRA REFUND, TAX REFUND | EXCLUDE | Not income | Tax refund from prior period |
| GOVERNMENT GRANT, SUBSIDY | EXCLUDE unless revenue grant | Check nature | Capital grants EXCLUDE; revenue grants = business income |

### 3.2 Expense Patterns (Debits) — Fully Deductible (business expenses)

**3.2 Expense Patterns (Debits) — Fully Deductible (business expenses)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, COMMERCIAL RENT | Office rent | Deductible | Dedicated business premises |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Deductible |  |
| ACCOUNTANT, AUDITOR, BOOKKEEP, ACCA, CA FEES | Accountancy fees | Deductible |  |
| LAWYER, LEGAL, ADVOCATE (business) | Legal fees | Deductible | Must be business-related |
| OFFICE SUPPLIES, STATIONERY | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing/advertising | Deductible |  |
| TRAINING, CPD, COURSE, SEMINAR, CONFERENCE | Training/CPD | Deductible | Must relate to current business |
| BANK FEE, BANK CHARGE, SERVICE CHARGE (business a/c) | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Deductible |  |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Deductible | Recurring = operating expense |

### 3.3 Expense Patterns (Debits) — SaaS and Software

**3.3 Expense Patterns (Debits) — SaaS and Software**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| PERPETUAL SOFTWARE LICENCE (high value) | Capital item | Capitalise / capital allowance | **[RESEARCH GAP — reviewer to confirm]** capital-allowance rate; review Income Tax Regulation |

### 3.4 Expense Patterns (Debits) — Utilities (may need apportionment)

**3.4 Expense Patterns (Debits) — Utilities (may need apportionment)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| STELCO, FENAKA, MWSC | Electricity / water | T2 if home office | 100% if dedicated office; proportional if home; default 0% if mixed |
| DHIRAAGU, OOREDOO | Telecoms / broadband | T2 | Business-use portion only; default 0% if mixed |
| MOBILE, DHIRAAGU MOBILE, OOREDOO MOBILE | Phone | T2 | Business-use portion only |

### 3.5 Expense Patterns (Debits) — Travel

**3.5 Expense Patterns (Debits) — Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| MALDIVIAN, FLYME, EMIRATES, QATAR AIRWAYS | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, GUESTHOUSE, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| FERRY, MTCC FERRY, SPEEDBOAT, TAXI | Local transport | Deductible if business purpose | Inter-island ferry/speedboat is common |
| FUEL, PETROL, DIESEL | Vehicle/vessel fuel | T2 — business % only | Requires usage log |

### 3.6 Expense Patterns (Debits) — NOT Deductible

**3.6 Expense Patterns (Debits) — NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, CAFE, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible (flag) | **[RESEARCH GAP — reviewer to confirm]** entertainment treatment under Income Tax Regulation; default to non-deductible until confirmed |
| PERSONAL, GROCERIES, SUPERMARKET | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, MIRA FINE | Fines/penalties | NOT deductible | Public policy |
| INCOME TAX, MIRA TAX PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) — Capital Items

**3.7 Expense Patterns (Debits) — Capital Items**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | Capital allowance | **[RESEARCH GAP — reviewer to confirm]** exact capital-allowance rates under Income Tax Regulation |
| PRINTER, SCANNER, COPIER | Office equipment | Capital allowance | **[RESEARCH GAP — reviewer to confirm]** rate |
| FURNITURE, DESK, CHAIR | Furniture/fittings | Capital allowance | **[RESEARCH GAP — reviewer to confirm]** rate |
| VEHICLE, CAR, VESSEL, DHONI (business) | Motor vehicle / vessel | Capital allowance, business % only | **[RESEARCH GAP — reviewer to confirm]** rate |

### 3.8 Exclusions (Neither Income nor Expense)

**3.8 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, PERSONAL LOAN | EXCLUDE | Loan principal movement |
| MRPS, PENSION CONTRIBUTION, MPAO | Pension contribution | Employee 7% / employer 7%; treat per Section 5.5 — not a general Box-2 expense |
| GST PAYMENT, MIRA GST | EXCLUDE | GST liability payment, not an income-tax expense |
| EWT PAYMENT, MIRA 601 | Credit against tax (employees) | Tax withheld at source — credit, not an expense |
| INTERIM PAYMENT, MIRA INCOME TAX INTERIM | Credit against final liability | Not an expense — credit against the final return |

### 3.9 Maldivian Banks — Statement Format Reference

**3.9 Maldivian Banks — Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BML (Bank of Maldives) | TRANSFER, DD, SO, CARD, CHARGES | PDF/CSV; description contains counterparty + reference; date DD/MM/YYYY |
| MIB (Maldives Islamic Bank) | TRANSFER, PROFIT, CHARGE | Islamic-finance terminology (profit, not interest) |
| HBL Maldives, SBI Maldives | PAYMENT, TRF, FEE | Counterparty in description field |
| BML USD account | CARD PAYMENT, TRANSFER (USD) | Tourism / TGST receipts often in USD — convert at the applicable rate |

## Section 4 -- Worked Examples

> All examples use Maldivian Rufiyaa (MVR) and the Tax Year 2025 brackets from Section 1. Amounts are recomputed end-to-end below.

### Example 1 — Self-employed, annual taxable income MVR 1,500,000

**Computation:**
- Band 0–720,000: 0% → MVR 0
- Band 720,001–1,200,000: 5.5% × 480,000 = MVR 26,400
- Band 1,200,001–1,500,000: 8% × 300,000 = MVR 24,000
- **Total income tax = 26,400 + 24,000 = MVR 50,400**

*Self-check: 0 + 26,400 + 24,000 = 50,400. ✓*

### Example 2 — Self-employed, annual taxable income MVR 900,000

**Computation:**
- Band 0–720,000: 0% → MVR 0
- Band 720,001–900,000: 5.5% × 180,000 = MVR 9,900
- **Total income tax = MVR 9,900**

*Self-check: 5.5% × 180,000 = 9,900. ✓*

### Example 3 — Employee, monthly remuneration MVR 120,000 (EWT)

**Input line:**
`28/02/2025 ; BML CREDIT ; EMPLOYER ATOLL CONSULTING PVT LTD ; SALARY FEB ; +116,200.00 ; MVR`

**Reasoning:** Employment income. Employer applies EWT monthly bands (Section 1):
- First MVR 60,000: 0% → MVR 0
- 60,000–100,000 (MVR 40,000 at 5.5%): MVR 2,200
- 100,000–120,000 (MVR 20,000 at 8%): MVR 1,600
- **Monthly EWT withheld = 2,200 + 1,600 = MVR 3,800**

Net salary in this example also reflects MRPS employee 7% on pensionable wage; see Example 6. The credit of MVR 116,200 = MVR 120,000 gross − MVR 3,800 EWT (MRPS handled separately by the employer here).

*Self-check: EWT 0 + 2,200 + 1,600 = 3,800; gross 120,000 − 3,800 = 116,200. ✓*

**Classification:** Employment income (EWT regime). Employer files **MIRA 601** by the 15th of the following month.

### Example 4 — Consulting fee received (self-employed, GST-registered)

**Input line:**
`15/03/2025 ; BML TRANSFER IN ; RESORT HOLDINGS PVT LTD ; INV-2025-007 ; +108,000.00 ; MVR`

**Reasoning:** Self-employment revenue. Client is GST-registered and the MVR 108,000 includes 8% GGST. Net business income = 108,000 ÷ 1.08 = MVR 100,000. GST of MVR 8,000 is a liability to MIRA, excluded from income.

*Self-check: 108,000 ÷ 1.08 = 100,000; 100,000 × 8% = 8,000; 100,000 + 8,000 = 108,000. ✓*

**Classification:** Business income = MVR 100,000. GST MVR 8,000 excluded.

### Example 5 — Software subscription (fully deductible)

**Input line:**
`01/04/2025 ; BML CARD ; ADOBE SYSTEMS ; CREATIVE CLOUD APR ; -462.00 ; MVR`

**Reasoning:** Monthly SaaS subscription, recurring, wholly for business. Fully deductible operating expense.

**Classification:** Deductible business expense = MVR 462.00.

### Example 6 — MRPS pension contribution (basic salary MVR 80,000)

**Input line:**
`05/03/2025 ; BML DD ; MPAO MRPS CONTRIBUTION ; FEB ; -5,600.00 ; MVR`

**Reasoning:** MRPS employee contribution = 7% of pensionable wage (contractual basic salary). 7% × 80,000 = MVR 5,600. The employer separately contributes a matching 7% (MVR 5,600), so total to the scheme is MVR 11,200.

*Self-check: 7% × 80,000 = 5,600 (employee); 7% × 80,000 = 5,600 (employer); total 11,200. ✓*

**Classification:** Pension contribution (MRPS), not a general business expense — treat per Section 5.5.

### Example 7 — Internal transfer (exclude)

**Input line:**
`15/05/2025 ; BML TRANSFER ; OWN ACCOUNT — SAVINGS ; ; -20,000.00 ; MVR`

**Reasoning:** Transfer between own accounts. Neither income nor expense.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 The Wholly-and-Exclusively Test

- **Wholly-and-exclusively test** — An expense is deductible only if incurred wholly and exclusively in the production of business income. Mixed-use expenses must be apportioned on a reasonable, documented basis. **[RESEARCH GAP — reviewer to confirm]** the precise allowable-expense and deduction rules in the Income Tax Regulation were not fully captured; review directly.  _(Income Tax Act, Law No. 25/2019 (and Income Tax Regulation))_

### 5.2 Residency and Source

- **Resident individuals** — Resident individuals: taxed on worldwide income.  _(Income Tax Act, Law No. 25/2019)_
- **Non-resident / temporary resident individuals** — Non-resident / temporary resident individuals: taxed on Maldives-source income only.
- **Residency confirmation requirement** — Confirm residency before computing — see Refusal R-MV-1.

### 5.3 The Tax-Free Threshold

- **Tax-free threshold** — The first MVR 720,000 of annual taxable income (= MVR 60,000/month) is taxed at 0%. This is built into the bracket structure; there is no separate personal allowance.  _(Income Tax Act, Law No. 25/2019; RCO Lawyers guide)_

### 5.4 Income Tax Registration Thresholds

- **Registration threshold — single payer** — Average monthly gross income over any 12-month period exceeds MVR 60,000 (i.e. > MVR 720,000/year).  _(MIRA FAQ, mira.gov.mv/Pages/View/FAQ_IncomeTax)_
- **Registration threshold — multiple payers** — MVR 40,000/month where the person derives remuneration from more than one payer and has not been registered by any of them.  _(MIRA FAQ, mira.gov.mv/Pages/View/FAQ_IncomeTax)_

### 5.5 MRPS Pension Contributions

- **MRPS contribution rate** — Employee 7% + employer 7% (minimum) of pensionable wage (contractual basic salary) = 14% total.  _(MPAO, Maldives Pension Act)_
- **Employer paying full contribution** — The employer may pay the full 14% without deducting the employee share but must pay at least 7%.

**[RESEARCH GAP — reviewer to confirm]** whether/how the employee MRPS contribution is deductible against taxable income for income-tax purposes, and the self-employed contribution ceiling mechanics — review the Income Tax Regulation and Pension Act directly.

### 5.6 Employee Withholding Tax (EWT)

- **EWT withholding basis** — Employers withhold EWT on monthly remuneration above MVR 60,000 using the monthly bands (Section 1).  _(MIRA)_
- **MIRA 601 filing** — File MIRA 601 via MIRAconnect by the 15th of the following month, with payment by the same date. Nil returns are required once an EWT obligation has arisen.  _(MIRA, mira.gov.mv/Pages/View/ewtfile)_
- **EWT as credit for employees** — For employees, EWT already withheld is a credit against the individual's final income tax.

### 5.7 Self-Employed / Business Income — Filing & Payment

**Self-Employed / Business Income — Filing & Payment schedule**  _(RCO Lawyers, Maldives Income Tax; MIRA, mira.gov.mv/Pages/View/ictindividualshowtofile)_

| Step | Deadline |
| --- | --- |
| First interim payment | 31 July of the tax year |
| Second interim payment | 31 January of the following year |
| Final return + payment (annual reconciliation) | 30 June of the following year |

- **Self-employed filing method** — Self-employed individuals and sole proprietors file the individual income tax return (not EWT). Tax is paid over two interim payments plus a final filing.  _(RCO Lawyers, Maldives Income Tax; MIRA, mira.gov.mv/Pages/View/ictindividualshowtofile)_

### 5.8 Non-Deductible Expenses

**5.8 Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Drawings / personal withdrawals | Not an expense |
| Entertainment (client meals) | **[RESEARCH GAP — reviewer to confirm]** — default to non-deductible until the Income Tax Regulation is checked |

### 5.9 GST Interaction (context)

**5.9 GST Interaction (context)**

| Scenario | Income Tax Treatment |
| --- | --- |
| GST collected on sales (GST-registered) | NOT income — exclude from business income |
| Input GST recovered | NOT an expense — exclude |
| GST not recoverable (unregistered / blocked) | IS an expense — gross is the cost |

- **GST rates and thresholds** — GGST 8%; TGST 17% (increased from 16% effective 1 July 2025, 7th Amendment to the GST Act, Law No. 10/2011, ratified 5 Nov 2024). GST registration threshold: taxable supplies > MVR 1,000,000 in the past/projected 12 months; tourism-sector businesses must register regardless of turnover. Returns + payment due by the 28th of the month following the taxable period (Form MIRA 105 to register; monthly if supply ≥ MVR 1,000,000, otherwise quarterly). TGST is paid in USD; GGST in MVR.  _(RCO Lawyers, Maldives Goods and Services Tax; MIRA circular on TGST rate; Crowe, TGST rate to increase from 1 July 2025)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- **Home office deduction rules** — Apportion home costs (rent, electricity STELCO/FENAKA, water MWSC, internet) to the dedicated business-use proportion. Must be a genuinely dedicated workspace; dual-use rooms do not qualify. **Conservative default:** 0% deduction until reviewer confirms arrangement. **[RESEARCH GAP — reviewer to confirm]** the precise home-office rules under the Income Tax Regulation.

### 6.2 Vehicle / Vessel Business Use

- **Vehicle/vessel business use rules** — Only the business-use percentage of fuel, insurance, maintenance, and capital allowance is deductible. Vessels (dhoni/speedboat) are common business assets in the Maldives. Client must maintain a usage/mileage log. **Conservative default:** 0% business use until a log is provided.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use rules** — Business-use portion only (Dhiraagu / Ooredoo). **Conservative default:** 0% deduction until business percentage confirmed.

### 6.4 Capital Allowances

- **Capital allowances treatment** — Capital assets are not expensed in full; they are written down via capital allowances. **[RESEARCH GAP — reviewer to confirm]** the capital-allowance rates and asset classes under the Income Tax Regulation were not captured. Flag every capital item for the reviewer and do not assert a rate.

### 6.5 Bad Debt Write-Off

- **Bad debt write-off rules** — Deductible only if income was previously declared, all reasonable recovery steps were taken, and the debt is genuinely irrecoverable. Flag for reviewer.

### 6.6 Foreign Tax Credit (residents)

- **Foreign tax credit rules** — Residents are taxed on worldwide income; relief for foreign tax may be available. **[RESEARCH GAP — reviewer to confirm]** foreign-tax-credit mechanics under the Income Tax Act/Regulation. Flag for reviewer.

## Section 7 -- Excel Working Paper Template

```
MALDIVES INDIVIDUAL INCOME TAX -- WORKING PAPER
Tax Year: 2025                Currency: MVR
Client: ___________________________
Residency: Resident / Non-resident / Temporary resident
Income type: Self-employed / Employee (EWT) / Both

A. BUSINESS / SELF-EMPLOYMENT INCOME
  A1. Client payments (net of GST if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, etc.)      ___________
  A3. Other business income                         ___________
  A4. TOTAL business income                         ___________

B. ALLOWABLE DEDUCTIONS
  B1. Office rent                                   ___________
  B2. Professional insurance                        ___________
  B3. Accountancy / legal fees                      ___________
  B4. Office supplies                               ___________
  B5. Software subscriptions                        ___________
  B6. Marketing / advertising                       ___________
  B7. Bank / payment processing fees                ___________
  B8. Training / CPD                                ___________
  B9. Travel (flights, ferry, accommodation)        ___________
  B10. Telecoms (business % of phone/internet)      ___________
  B11. Home office (% of utilities/rent)            ___________
  B12. Vehicle/vessel expenses (business %)         ___________
  B13. Capital allowances [RATE — reviewer]         ___________
  B14. Other allowable expenses                     ___________
  B15. TOTAL deductions                             ___________

C. NET BUSINESS PROFIT (A4 - B15)                   ___________

D. OTHER INCOME
  D1. Employment income (gross, before EWT)         ___________
  D2. Rental income                                 ___________
  D3. Investment income                             ___________
  D4. TOTAL other income                            ___________

E. TOTAL TAXABLE INCOME (C + D4)                    ___________
   (residents: worldwide; non-residents: MV-source)

F. INCOME TAX (apply annual bands — Section 1)
   0–720,000           @ 0%   = 0
   720,001–1,200,000   @ 5.5%                       ___________
   1,200,001–1,800,000 @ 8%                         ___________
   1,800,001–2,400,000 @ 12%                        ___________
   above 2,400,000     @ 15%                        ___________
  F1. TOTAL income tax                              ___________

G. CREDITS
  G1. EWT already withheld (employees)              ___________
  G2. Interim payments made                         ___________
  G3. Foreign tax credit [reviewer]                 ___________
  G4. TOTAL credits                                 ___________

H. TAX DUE / REFUND (F1 - G4)                        ___________

REVIEWER FLAGS:
  [ ] Residency confirmed (resident / non-resident)?
  [ ] Income tax registration threshold checked (MVR 60k/40k)?
  [ ] GST registration status confirmed (MVR 1,000,000)?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle/vessel business % confirmed with log?
  [ ] Phone/internet business % confirmed?
  [ ] Capital allowance rates confirmed against Income Tax Regulation?
  [ ] MRPS contributions correct (7%/7% of basic salary)?
  [ ] Entertainment treatment confirmed?
  [ ] EWT (MIRA 601) filings up to date if employer?
```

## Section 8 -- Bank Statement Reading Guide

### Maldivian Bank Statement Formats

**Maldivian Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BML (Bank of Maldives) | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description holds counterparty + reference; DD/MM/YYYY |
| MIB (Maldives Islamic Bank) | PDF | Date, Particulars, Withdrawal, Deposit | Islamic terms — "profit" not "interest" |
| HBL Maldives | PDF, CSV | Value Date, Description, Amount, Balance | Counterparty in description |
| SBI Maldives | PDF | Date, Narration, Debit, Credit |  |
| BML USD account | CSV | Date, Description, Amount (USD), Balance | Tourism/TGST receipts in USD — convert |

### Key Maldivian / Dhivehi Banking Terms

**Key Maldivian / Dhivehi Banking Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| MUSAARA | Salary / wage | Employment income (EWT) |
| KUYYEE | Rent | Rental income (in) or office rent (out) |
| FAISA / TRANSFER | Money / transfer | Check direction for income/expense |
| MRPS / MPAO | Pension scheme / pension office | Pension contribution (7%/7%) |
| EWT / MIRA 601 | Employee Withholding Tax | Tax withheld at source — credit |
| GST / MIRA 105 | Goods & Services Tax | GST liability — exclude from income tax |
| STELCO / FENAKA | Electricity utilities | Utility expense (apportion if home office) |
| DHIRAAGU / OOREDOO | Telecoms | Telecoms expense (business % only) |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- MALDIVES INCOME TAX
1. Residency: resident in the Maldives, non-resident, or temporary resident?
2. Income type: self-employed / sole proprietor, employee (EWT), or both?
3. Are you registered for income tax with MIRA? (Threshold: avg > MVR 60,000/month,
   or MVR 40,000/month if income from more than one payer.)
4. Are you registered for GST? (Threshold: taxable supplies > MVR 1,000,000 / 12 months;
   tourism sector must register regardless.)
5. Home office: dedicated space? If yes, what % of floor area?
6. Vehicle/vessel: used for business? What % is business use? Do you keep a log?
7. Phone/internet: what % is business use?
8. MRPS: are pension contributions (7% employee / 7% employer) being made?
9. Employees only — what EWT has already been withheld by your employer(s)?
10. Have you made any interim income tax payments (31 July / 31 January)?
11. Any other income (employment, rental, dividends, interest)?
12. Any capital assets purchased during the year?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**

| Topic | Reference |
| --- | --- |
| Personal income tax (existence, brackets, residency) | Income Tax Act, Law No. 25/2019 (ratified 17 Dec 2019; income tax from 1 Jan 2020; remuneration from 1 Apr 2020). Brackets corroborated via RCO Lawyers, *Current Tax Rates in Maldives* |
| Tax-free threshold MVR 720,000/yr (MVR 60,000/mo) | Income Tax Act, Law No. 25/2019; RCO Lawyers guide |
| EWT monthly bands & MIRA 601 (due 15th of following month) | MIRA: mira.gov.mv/Pages/View/ictewt; mira.gov.mv/Pages/View/ewtfile; edition.mv/news/15888 |
| Income tax registration thresholds (MVR 60,000 / MVR 40,000) | MIRA FAQ: mira.gov.mv/Pages/View/FAQ_IncomeTax |
| Self-employed interim/final deadlines (31 Jul / 31 Jan / 30 Jun) | RCO Lawyers, *Maldives Income Tax*; MIRA: mira.gov.mv/Pages/View/ictindividualshowtofile |
| MRPS contributions (7% / 7% / 14% of basic salary) | MPAO: pension.gov.mv/en/mrps; old.pension.gov.mv/en/scheme/maldives-retirement-pension-scheme-en; Maldives Pension Act |
| GST: GGST 8%; TGST 17% from 1 Jul 2025; threshold MVR 1,000,000; return due 28th | GST Act, Law No. 10/2011, 7th Amendment (ratified 5 Nov 2024); MIRA circular; RCO Lawyers; Crowe |
| Company/business income tax (15% > MVR 500,000; banks 25%); NWT 5–10% | RCO Lawyers, *Current Tax Rates in Maldives*; formix.live corporate guide |
| Penalties (late filing / late payment) | Tax Administration Regulation: mira.gov.mv/Legislations/View/Tax-Administration-Regulation-consolidated; apexlaw.co; MIRA fine calculators (ictfinecalculator, gstfinecalculator) |

### Penalties (MIRA)

**Penalties (MIRA)**

| Event | Penalty |
| --- | --- |
| Late filing of return (with tax payable) | MVR 50 per day + 0.5% of the tax payable [Tax Administration Regulation; apexlaw.co] |
| Late filing (no tax liability) | MVR 50/day, capped at a maximum of MVR 125,000 [Tax Administration Regulation; apexlaw.co] |
| Late payment of tax | 0.05% per day of the outstanding amount, capped at the **greater of** twice the outstanding tax **or** MVR 250,000 [Tax Administration Regulation; apexlaw.co] |
| Failure to register / failure to withhold | **[RESEARCH GAP — reviewer to confirm]** — specific amounts not found in a clean authoritative form |

### Minimum Wage (Maldivian nationals only; 2025)

**Minimum Wage (Maldivian nationals only; 2025)**  _(Minimum Wage Order, trade.gov.mv/wp-content/uploads/2023/05/minimum-wage-order-en-v01.pdf; remotepeople.com)_

| Employer category | Monthly minimum (MVR) |
| --- | --- |
| Small business | 4,500 |
| Medium business | 7,000 |
| Large business (100+ employees / MVR 20M+ revenue) | 8,000 |
| Tourism sector (any size) | 7,000 |

Set by the Minimum Wage Order. **Applies only to Maldivian nationals — foreign/expat workers are explicitly excluded.** A national revision was underway during 2025; verify currency at point of use.

### Test Suite

Input: Resident, annual taxable income MVR 1,500,000.
Expected: 0 (first 720,000) + 5.5% × 480,000 (26,400) + 8% × 300,000 (24,000) = **MVR 50,400** income tax.

Input: Resident, annual taxable income MVR 720,000.
Expected: **MVR 0** income tax (entirely within the 0% band).

Input: Resident, annual taxable income MVR 3,000,000.
Expected: 26,400 + 48,000 + 72,000 + 15% × 600,000 (90,000) = **MVR 236,400** income tax.
*Self-check: 26,400 + 48,000 + 72,000 + 90,000 = 236,400. ✓*

Input: Resident, annual taxable income MVR 900,000.
Expected: 5.5% × 180,000 = **MVR 9,900** income tax.

Input: Employee, monthly remuneration MVR 120,000.
Expected: 0 (first 60,000) + 5.5% × 40,000 (2,200) + 8% × 20,000 (1,600) = **MVR 3,800** EWT withheld; employer files MIRA 601 by the 15th of the following month.

Input: Basic salary MVR 80,000/month.
Expected: Employee 7% = MVR 5,600; employer 7% = MVR 5,600; total to scheme = **MVR 11,200**.

Input: GST-registered self-employed; receipt MVR 108,000 incl. 8% GGST.
Expected: Business income = MVR 100,000; GST MVR 8,000 excluded from income.

Input: Resident, annual taxable income MVR 2,000,000.
Expected: 26,400 + 48,000 + 12% × 200,000 (24,000) = **MVR 98,400** income tax.
*Self-check: 26,400 + 48,000 + 24,000 = 98,400. ✓*

## PROHIBITIONS

- NEVER state that "the Maldives has no personal income tax" — it does, under the Income Tax Act (Law No. 25/2019)
- NEVER use the Rivermate EWT table (5%/10%/15%/20%) — use the official 5.5% / 8% / 12% / 15% bands
- NEVER compute tax without confirmed residency (resident = worldwide; non-resident = Maldives-source only)
- NEVER assert a capital-allowance rate — it is a RESEARCH GAP; flag for the reviewer
- NEVER include GST collected on sales in business income for GST-registered clients
- NEVER allow income tax itself, fines, penalties, or drawings as a deduction
- NEVER treat MRPS as a general business expense — it is the 7%/7% pension contribution
- NEVER present tax calculations as definitive — always label as estimated, pending reviewer sign-off
- NEVER rely on the annual brackets without the human re-check noted in Section 1 (MIRA page is bot-blocked)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
