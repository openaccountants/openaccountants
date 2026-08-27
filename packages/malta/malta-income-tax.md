---
name: malta-income-tax
description: "Use this skill whenever asked about Malta income tax for self-employed individuals. Trigger on phrases like \"how much tax do I pay\", \"income tax return\", \"self-assessment\", \"allowable deductions\", \"capital allowances\", \"provisional tax\", \"TA22 regime\", \"TA24\", \"chargeable income\", \"tax credits\", \"self-employed tax Malta\", or any question about filing or computing income tax for a self-employed or part-time self-employed client. Also trigger when preparing or reviewing the annual income tax return or a TA22, computing deductible expenses, or advising on provisional tax instalments. NOTE: TA24 is the 15% final tax form for RENTAL income (ITA Art. 31D) — if the user means rental income, see Section 5.11; the self-employed annual filing is the personal Income Tax Return. This skill covers tax rates (single/married/parent), the return working-paper structure, allowable deductions, capital allowances, provisional tax, the TA22 part-time regime, penalties, and interaction with VAT and SSC. ALWAYS read this skill before touching any income tax work."
version: 2.0
jurisdiction: MT
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Michael Cutajar, CPA (Malta)
review_status: current
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Malta Income Tax

## malta-income-tax

Depends on: income-tax-workflow-base.
Content revision: 2.1-draft (correction pass — unverified; frontmatter `version` is the platform revision counter).

## Section 1 -- Quick Reference

**Quick Reference**  _([ITA Cap. 123; ITMA Cap. 372](https://legislation.mt/eli/cap/372/eng))_

| Field | Value |
| --- | --- |
| Country | Malta (Republic of Malta) |
| Tax | Income Tax (Taxxa fuq id-Dħul) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December); "basis year" precedes the "year of assessment" |
| Primary legislation | Income Tax Act, Chapter 123 (ITA) |
| Supporting legislation | Income Tax Management Act, Chapter 372 (ITMA); ITA Art. 90A + Part-Time Work Rules (TA22 regime); ITA Arts. 14 and 26 (allowed / disallowed deductions); ITA Art. 14(1)(f) and (j), Art. 24 and S.L. 123.01 (capital allowances); ITA Art. 31D (15% rental final tax, form TA24); ITMA Art. 44 and the Schedule to ITA Art. 56(12)(c) (interest, additional tax); S.L. 372.18 (Provisional Tax Rules) |
| Tax authority | Malta Tax and Customs Administration (MTCA), formerly Commissioner for Revenue (CFR) |
| Filing portal | MTCA online services (myTax) |
| Filing deadlines | Personal Income Tax Return: **30 June** of the following year (online filing routinely extended by MTCA notice — e.g. 31 July 2026 for basis 2025). TA22 (part-time self-employed): **30 April**. TA24 (rental 15%): **30 April** |
| Validated by | Pending — requires sign-off by a Maltese warranted accountant |
| Validation date | Pending |

### What form does a self-employed person actually file?

**Filing form by situation**  _([ITA Art. 31D](https://legislation.mt/eli/cap/123/eng))_

| Situation | Filing |
| --- | --- |
| Fully self-employed (trade, business, profession, vocation) | **Personal Income Tax Return with self-assessment** (electronic via myTax), including the self-employment profit-and-loss section. There is no form called "TA24" for this. |
| Part-time self-employed alongside full-time employment / pension / full-time studies | Optional **TA22** (10% final-style computation on first EUR 12,000 of net profit) by 30 April — see Section 5.8 |
| Rental income, optional 15% final tax on gross rents | **TA24** (ITA Art. 31D) by 30 April — out of this skill's computation scope, see Section 5.11 |

### Tax Rate Brackets — basis year 2025 (Budget 2025 widened bands, effective 1 January 2025)

Tax = (chargeable income x rate) - subtract amount for the band containing the chargeable income.

**Single Rates**  _(Budget 2025, effective 1 January 2025)_

| Taxable Income (EUR) | Rate | Subtract (EUR) | Cumulative Tax at Top |
| --- | --- | --- | --- |
| 0 -- 12,000 | 0% | 0 | EUR 0 |
| 12,001 -- 16,000 | 15% | 1,800 | EUR 600 |
| 16,001 -- 60,000 | 25% | 3,400 | EUR 11,600 |
| 60,001+ | 35% | 9,400 | -- |

**Married Rates (joint computation)**  _(Budget 2025, effective 1 January 2025)_

| Taxable Income (EUR) | Rate | Subtract (EUR) | Cumulative Tax at Top |
| --- | --- | --- | --- |
| 0 -- 15,000 | 0% | 0 | EUR 0 |
| 15,001 -- 23,000 | 15% | 2,250 | EUR 1,200 |
| 23,001 -- 60,000 | 25% | 4,550 | EUR 10,450 |
| 60,001+ | 35% | 10,550 | -- |

**Parent Rates (maintaining a child / paying maintenance)**  _(Budget 2025, effective 1 January 2025)_

| Taxable Income (EUR) | Rate | Subtract (EUR) | Cumulative Tax at Top |
| --- | --- | --- | --- |
| 0 -- 13,000 | 0% | 0 | EUR 0 |
| 13,001 -- 17,500 | 15% | 1,950 | EUR 675 |
| 17,501 -- 60,000 | 25% | 3,700 | EUR 11,300 |
| 60,001+ | 35% | 9,700 | -- |

Malta does not have a separate personal allowance -- the 0% band IS the personal allowance.

**2026 note (Budget 2026, announced 27 October 2025, effective 1 January 2026).** The base single/married/parent bands above are unchanged for basis year 2026, but four NEW categories were added for taxpayers with qualifying children (child under 18, or 18–23 in full-time education):

**2026 new qualifying-children categories**  _(Budget 2026, announced 27 October 2025, effective 1 January 2026)_

| Category | 0% band | 15% band (subtract) | 25% band (subtract) | 35% (subtract) |
| --- | --- | --- | --- | --- |
| Married, 1 qualifying child | 0 -- 17,500 | 17,501 -- 26,500 (2,625) | 26,501 -- 60,000 (5,275) | 60,001+ (11,275) |
| Married, 2+ qualifying children | 0 -- 22,500 | 22,501 -- 32,000 (3,375) | 32,001 -- 60,000 (6,575) | 60,001+ (12,575) |
| Parent, 1 qualifying child | 0 -- 14,500 | 14,501 -- 21,000 (2,175) | 21,001 -- 60,000 (4,275) | 60,001+ (10,275) |
| Parent, 2+ qualifying children | 0 -- 18,500 | 18,501 -- 25,500 (2,775) | 25,501 -- 60,000 (5,325) | 60,001+ (11,325) |

Further widenings were announced for 2027 and 2028. For basis year 2025 computations, use ONLY the three base tables.

### Working-Paper Lines (WP)

The MTCA electronic return's own field numbering changes between years and is not reproduced here — map these working-paper lines to the live return at filing time (reviewer task).

**Working-Paper Lines**  _(S.L. 123.01)_

| Line | Description |
| --- | --- |
| WP1 | Gross income from self-employment |
| WP2 | Less: Allowable deductions (revenue expenses) |
| WP3 | Net profit/loss (WP1 - WP2) |
| WP4 | Other income (employment, rental at progressive rates, dividends, interest) |
| WP5 | Total income (WP3 + WP4) |
| WP15 | Capital allowances (wear and tear per S.L. 123.01; initial allowance where due) |
| WP25 | Total statutory deductions (WP15 + any other statutory deductions) |
| WP30 | Chargeable income (WP5 - WP25) |
| WP35 | Tax liability (rate table applied to WP30 — deterministic engine only) |
| WP36 | Less: Provisional tax paid |
| WP37 | Less: Tax credits |
| WP40 | Tax due / refund (WP35 - WP36 - WP37) |

Note: SSC Class 2 has NO line in the tax computation — it is not deductible (Section 5.5). Record it memo-only for the reviewer.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown marital status | STOP -- do not apply a rate table without marital status |
| Unknown filing status (full return vs TA22) | Full Income Tax Return (fully self-employed) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT registration type | Article 10 (standard) |
| Unknown asset useful life | Use S.L. 123.01 minimum-years rates |
| Unknown whether expense is entertainment | Treat as entertainment (blocked -- conservative default, Section 5.6) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of marital status (single/married/parent) and employment status (fully self-employed full return, or part-time TA22).

**Recommended** -- all sales invoices, purchase invoices/receipts, SSC Class 2 payment records (memo only), prior year return or tax statement, VAT registration type (Article 10 or Article 11).

**Ideal** -- complete income and expenditure account, asset register with capital allowances schedule, provisional tax payment confirmations, employment income details (if TA22).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This return was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that the wholly-and-exclusively test is met."

### Refusal Catalogue

- **R-MT-1 -- Marital status unknown** — "Marital status determines the applicable rate table. This skill cannot compute tax without knowing whether the client is single, married, or a parent. Please confirm before proceeding."
- **R-MT-2 -- Group structures or partnerships** — "This skill covers sole proprietors and part-time self-employed individuals only. Group structures, partnerships, and companies file separate returns. Escalate to a warranted accountant."
- **R-MT-3 -- Non-resident income** — "Non-resident and dual-resident taxation has different rules. Out of scope. Escalate to a warranted accountant."
- **R-MT-4 -- Capital gains / property disposals** — "Capital gains computations under Article 5A or property transfers require specialised analysis. Escalate to a warranted accountant."  _([Article 5A](https://legislation.mt/eli/cap/123/eng))_
- **R-MT-5 -- Arrears / enforcement** — "Client has outstanding tax arrears or is subject to MTCA enforcement action. Late payment attracts additional tax of 1% per month (no statutory cap) plus interest of 0.6% per month (capped at the amount of the tax) under ITMA Art. 44. Do not advise. Escalate to a warranted accountant immediately."  _([ITMA Art. 44](https://legislation.mt/eli/cap/372/eng))_
- **R-MT-6 -- VAT return requested** — "This skill covers income tax only. For Malta VAT, use the malta-vat-return skill."
- **R-MT-7 -- Rental 15% final tax (TA24) computation requested** — "TA24 is the optional 15% final tax on gross rental income under ITA Art. 31D, due 30 April. This skill flags it but does not compute it -- confirm whether the 15% option or progressive rates are better for the client with a warranted accountant."  _([ITA Art. 31D](https://legislation.mt/eli/cap/123/eng))_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns**

| Pattern | WP Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | WP1 (gross revenue) | Business income | If Article 10 VAT-registered, extract net (excl. 18% VAT) |
| HONORARJU, FEES, PROFESSIONAL FEES, CONSULTANCY | WP1 | Business income | Professional fees -- typical for self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | WP1 | Business income | Platform payout -- match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | WP1 | Business income | Platform payout -- verify against invoices |
| WISE PAYOUT, WISE TRANSFER | WP1 | Business income | International platform payout |
| REVOLUT PAYOUT | WP1 | Business income | Check if business or personal Revolut |
| UPWORK, FIVERR, TOPTAL | WP1 | Business income | Freelance platform -- net of platform commission |
| PAGA, SALARY, STIPENDJU, EMPLOYER [name] | WP4 (other income) | Employment income | NOT self-employment -- goes to WP4 |
| KIRI, RENT RECEIVED | WP4 or TA24 | Rental income | Not self-employment income; if the client opts for the 15% Art. 31D final tax it goes on TA24 and stays OUT of this computation (Section 5.11) |
| INTERESSI, INTEREST RECEIVED | WP4 | Investment income | Interest income (investment-income withholding rules may apply -- reviewer) |
| DIVIDENDI, DIVIDEND | WP4 | Investment income | Dividend income |
| CFR REFUND, TAX REFUND, RISTORN | EXCLUDE | Not income | Tax refund from prior year |
| BONUS GVERN, GOVERNMENT GRANT, MALTA ENTERPRISE | EXCLUDE unless revenue grant | Check nature | Capital grants EXCLUDE; revenue grants = WP1 |

### 3.2 Expense Patterns (Debits on Bank Statement) -- Fully Deductible (WP2)

**Fully Deductible Expense Patterns**  _([ITA Art. 14(1)(b)](https://legislation.mt/eli/cap/123/eng))_

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| KIRI UFFICCJU, OFFICE RENT, RENT [commercial address] | Office rent | WP2 -- fully deductible | Dedicated business premises (ITA Art. 14(1)(b)) |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | WP2 -- fully deductible |  |
| ACCOUNTANT, AUDITOR, BOOKKEEP, CPA, ACCA FEES | Accountancy fees | WP2 -- fully deductible |  |
| AVUKAT, LAWYER, LEGAL, NOTARY (business) | Legal fees | WP2 -- fully deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES, VIKING | Office supplies | WP2 -- fully deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing/advertising | WP2 -- fully deductible |  |
| TRAINING, CPD, COURSE, SEMINAR, CONFERENCE | Training/CPD | WP2 -- fully deductible | Must relate to current business |
| MIA, ACCA SUBSCRIPTION, PROFESSIONAL BODY | Professional subscriptions | WP2 -- fully deductible |  |
| BOV CHARGE, HSBC CHARGE, BANK FEE, MAINTENANCE FEE | Bank charges | WP2 -- fully deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | WP2 -- fully deductible |  |
| POSTAGE, MALTAPOST (business) | Postage | WP2 -- fully deductible | Business correspondence |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure (services) | WP2 -- fully deductible | Recurring services = revenue expense; purchased HARDWARE = capital (WP15), no de minimis |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software Patterns**  _(S.L. 123.01)_

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | WP2 -- fully deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | WP2 -- fully deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | WP2 -- fully deductible |  |
| SOFTWARE LICENCE (perpetual) | Capital item | WP15 -- capitalise at 25%/year (4-year minimum, S.L. 123.01) | Capital by nature regardless of amount -- no de minimis |

### 3.4 Expense Patterns (Debits) -- Utilities (WP2, may need apportionment)

**Utilities Patterns**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ARMS, ARMS LTD, ENEMALTA | Electricity/water | T2 if home office | 100% if dedicated office; proportional if home |
| MELITA, GO PLC, EPIC | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |
| VODAFONE, MOBILE, GO MOBILE | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AIR MALTA, RYANAIR, WIZZ AIR, EASYJET | Flights | WP2 if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | WP2 if business travel |  |
| BOLT, UBER, ECABS, TAXI | Local transport | WP2 if business purpose |  |
| FUEL, ENEMED, PETROL | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING, CVA, MCP PARKING | Parking | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible Patterns**  _([ITA Art. 14(1) / Art. 26(a)-(b)](https://legislation.mt/eli/cap/123/eng))_

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, DINNER, LUNCH, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible (conservative default) | Fails wholly-and-exclusively, ITA Art. 14(1) / Art. 26(a)-(b); no statutory partial deduction. Reviewer may allow substantiated genuine business entertainment -- flag, never auto-allow |
| PERSONAL, GROCERIES, SUPERMARKET, LIDL, PAVI | Personal expenses | NOT deductible | Domestic/private (ITA Art. 26(a)) |
| FINE, PENALTY, MULTA, PARKING FINE | Fines/penalties | NOT deductible | Public policy |
| CFR PAYMENT, MTCA PAYMENT, INCOME TAX, TAX PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| SSC, CLASS 2, SOCIAL SECURITY | SSC Class 2 | NOT deductible -- memo only | No deduction in Cap. 123 for SSC (Section 5.5). Record the annual total for the reviewer |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (WP15)

Rates are the straight-line maximum implied by the S.L. 123.01 minimum-years schedule.

**Capital Items Patterns**  _(S.L. 123.01)_

| Pattern | Category | Min years / Annual Rate | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, IMAC, DESKTOP | Computers and electronic equipment | 4 years / 25% | WP15 |
| PRINTER, SCANNER, COPIER | Computers and electronic equipment | 4 years / 25% | WP15 (classification as electronic equipment -- reviewer confirm) |
| FURNITURE, DESK, CHAIR, FILING CABINET | Furniture, fixtures, fittings | 10 years / 10% | WP15 |
| VEHICLE, CAR (business) | Motor vehicle | 5 years / 20% | WP15, business % only; non-commercial cars: allowances computed on max cost EUR 14,000 |
| AIR CONDITIONING, AC UNIT | Air conditioners | 6 years / 16.67% | WP15 |

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, SELF-EMPLOYED LOAN, PERSONAL LOAN | EXCLUDE | Loan principal movement |
| SSC, CLASS 2, SOCIAL SECURITY | EXCLUDE from computation -- memo total for reviewer | NOT deductible against income tax (Section 5.5) |
| VAT PAYMENT, CFR VAT, MTCA VAT | EXCLUDE | VAT liability payment, not expense |
| PROVISIONAL TAX, PT INSTALMENT | WP36 (provisional tax paid) | Not an expense -- credit against liability |

### 3.9 Maltese Banks -- Statement Format Reference

**Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BOV (Bank of Valletta) | TRANSFER, DD, SO, CHQ, CHARGES | PDF/CSV; booking date format DD/MM/YYYY |
| HSBC Malta | PAYMENT, TRF, D/D, FEE | PDF/CSV; counterparty in description field |
| APS Bank | TRANSFER, DIRECT DEBIT, CHARGE | PDF; less common CSV export |
| Revolut Business | PAYMENT, TRANSFER, CARD PAYMENT | CSV; clean counterparty names |
| Wise Business | TRANSFER, CONVERSION, FEE | CSV; multi-currency -- use EUR amounts |

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (Article 10, VAT-registered, Maltese B2B client)

**Input line:**
`15/03/2025 ; BOV TRANSFER IN ; BORG & VELLA ADVOCATES ; PAYMENT INV-2025-003 ; +1,180.00 ; EUR`

**Reasoning:**
Client payment for services to a Maltese business client. The taxpayer is Article 10 VAT-registered, so EUR 1,180 includes 18% Malta VAT. Net = 1,180 / 1.18 = EUR 1,000 (WP1). EUR 180 is VAT collected (excluded from income -- it is a liability to MTCA). NOTE: if the client were a foreign EU business, the supply would typically be reverse-charge (no Malta VAT in the price) -- do not blindly extract 18% from cross-border B2B receipts.

**Classification:** WP1 = EUR 1,000. VAT EUR 180 excluded.

### Example 2 -- SaaS Subscription (Fully Deductible)

**Input line:**
`01/04/2025 ; HSBC DD ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD APR ; -29.99 ; EUR`

**Reasoning:**
Monthly recurring SaaS subscription = operating expense by nature (not a capital acquisition). Fully deductible. For Article 10 clients, the net amount (excl. recoverable VAT) is the expense. If Article 11, gross amount is the cost.

**Classification:** WP2 = EUR 29.99 (or net if Article 10 with recoverable input VAT).

### Example 3 -- Entertainment (Blocked)

**Input line:**
`22/04/2025 ; BOV CARD ; WATERBISCUIT RESTAURANT ; CLIENT DINNER ; -85.00 ; EUR`

**Reasoning:**
Client entertainment. Conservative default: blocked -- fails the wholly-and-exclusively test (ITA Art. 14(1)) and the negative test (Art. 26(a)/(b)). Malta has no statutory partial-deduction regime for entertainment. Flag for reviewer: a warranted accountant may allow genuinely business-purposed, substantiated entertainment -- never auto-allow.

**Classification:** NOT deductible. Remove from WP2 entirely. Reviewer flag.

### Example 4 -- SSC Class 2 Payment

**Input line:**
`10/01/2025 ; BOV DD ; CFR SSC CLASS 2 ; Q4 2024 ; -1,090.50 ; EUR`

**Reasoning:**
SSC Class 2 payment. NOT deductible against income tax -- the ITA Art. 14 positive list contains no deduction for social security contributions and Art. 26(a) disallows private expenses not specifically allowed. Exclude from the tax computation; record the annual total as a memo item for the reviewer and for cash-flow planning.

**Classification:** EXCLUDE from computation. Memo: SSC paid EUR 1,090.50.

### Example 5 -- Laptop Purchase (Capital Item)

**Input line:**
`03/06/2025 ; HSBC CARD ; APPLE STORE MALTA ; MACBOOK PRO ; -1,899.00 ; EUR`

**Reasoning:**
Capital asset. Computers and electronic equipment: minimum 4 years per S.L. 123.01, i.e. max 25% straight-line. EUR 1,899 x 25% = EUR 474.75 per year in WP15. Do NOT put in WP2.

**Classification:** WP15 = EUR 474.75/year. NOT WP2.

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`15/05/2025 ; BOV TRANSFER ; OWN ACCOUNT - SAVINGS ; ; -2,000.00 ; EUR`

**Reasoning:**
Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 The Wholly and Exclusively Test

- **Wholly and Exclusively Test** — An expense is deductible only if incurred wholly and exclusively in the production of the income (Art. 14(1)), and not disallowed by Art. 26 (domestic/private expenses, capital, recoverable amounts, voluntary payments, etc.). Mixed-use expenses must be apportioned. The apportionment method must be reasonable and documented.  _([ITA Art. 14(1) (positive test) and Art. 26 (negative test)](https://legislation.mt/eli/cap/123/eng))_

### 5.2 Revenue Recognition

- **Revenue Recognition** — All business income goes to WP1. For Article 10 clients, report net of VAT. For Article 11 clients, report gross (no VAT charged). VAT collected on sales is NOT income.

### 5.3 Capital vs Revenue

- **Capital vs Revenue** — Capital items must go through WP15 (capital allowances), not WP2 (ITA Art. 26 disallows capital expenditure as a revenue deduction; Art. 14(1)(f) allows wear and tear instead). There is no de minimis threshold -- business assets are depreciated per S.L. 123.01 regardless of cost. The VAT Capital Goods Scheme threshold (EUR 1,160) is a separate VAT system and is never an income-tax capitalisation test.  _([ITA Art. 26; Art. 14(1)(f); S.L. 123.01](https://legislation.mt/eli/cap/123/eng))_

### 5.4 Capital Allowance Rates (S.L. 123.01 -- Deduction for Wear and Tear of Plant and Machinery Rules)

S.L. 123.01 prescribes MINIMUM depreciation periods; the rates below are the straight-line maxima they imply.

**Capital Allowance Rates**  _(S.L. 123.01 -- Deduction for Wear and Tear of Plant and Machinery Rules)_

| Asset Type | Min Years | Max Annual Rate |
| --- | --- | --- |
| Computers and electronic equipment | 4 | 25% |
| Computer software | 4 | 25% |
| Motor vehicles (non-commercial: cost capped at EUR 14,000) | 5 | 20% |
| Other machinery | 5 | 20% |
| Air conditioners | 6 | 16.67% |
| Catering equipment | 6 | 16.67% |
| Furniture, fixtures, fittings and soft furnishings | 10 | 10% |
| Other plant | 10 | 10% |
| Industrial buildings and structures (incl. hotels; prescribed car parks and offices per S.L. 123.173) | -- | 2% p.a. + 10% initial allowance in year of first use (ITA Art. 14(1)(j), new or first used in Malta) |

Depreciation is straight-line on cost, starting in the year the asset is first used in the business. Total allowances may never exceed cost. Unclaimed allowances may be carried forward. Legal basis: ITA Art. 14(1)(f) and (j); balancing statements on disposal under ITA Art. 24. Ordinary commercial buildings that do not meet the industrial-buildings/S.L. 123.173 definitions get NO buildings allowance -- reviewer decision.

### 5.5 SSC Class 2 -- NOT Deductible

- **SSC Class 2 not deductible** — SSC Class 2 (self-occupied persons' contributions, 15% of prior-year net income, paid three times a year) is **not deductible** in computing chargeable income. The ITA Art. 14 list of allowable deductions contains no provision for social security contributions, and Art. 26(a) disallows private expenses not specifically allowed by the Act. Record the amounts paid as a memo item only. > Reviewer note: this is the single highest-impact rule in this skill. It was verified against the full text of Cap. 123 (no SSC deduction provision exists) but no explicit MTCA statement was located -- warranted-accountant confirmation required before Q1 promotion.  _([ITA Art. 14; Art. 26(a); Cap. 123](https://legislation.mt/eli/cap/123/eng))_

### 5.6 Non-Deductible Expenses

**Non-Deductible Expenses**  _([ITA Art. 14(1); Art. 26](https://legislation.mt/eli/cap/123/eng))_

| Expense | Reason |
| --- | --- |
| Entertainment (client meals, events) | Conservative block -- fails wholly-and-exclusively (Art. 14(1)); Art. 26(a)/(b); no statutory partial deduction. Reviewer may allow substantiated business cases |
| Personal living expenses | Domestic/private -- Art. 26(a) |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| SSC Class 2 | No deduction provision in Cap. 123 (Section 5.5) |
| Capital expenditure | Goes through WP15 -- Art. 26 |
| Drawings / personal withdrawals | Not an expense |
| Personal car insurance (unapportioned) | Personal |

### 5.7 VAT Interaction

**VAT Interaction**

| Scenario | Income Tax Treatment |
| --- | --- |
| VAT collected on sales (Article 10) | NOT income -- exclude from WP1 |
| Input VAT recovered (Article 10) | NOT an expense -- exclude from WP2 |
| Input VAT blocked/non-deductible (Article 10) | IS an expense -- include in WP2 |
| Article 11 client -- all VAT paid on purchases | IS an expense -- gross amount is cost |
| Foreign VAT (non-reclaimable) | IS an expense -- full gross is cost |

### 5.8 TA22 Regime (Part-Time Self-Employment)

**Legislation:** ITA Art. 90A (tax on part-time work) and the prescribed Part-Time Work Rules; operative rate and cap per MTCA guidance for basis year 2025.

**TA22 Regime conditions**  _([ITA Art. 90A + Part-Time Work Rules; MTCA guidance basis year 2025](https://legislation.mt/eli/cap/123/eng))_

| Condition | Requirement |
| --- | --- |
| Status | Full-time employed, OR pensioner, OR full-time student/apprentice |
| Registration | Part-time activity registered with Jobsplus; VAT-registered if obliged to register |
| Employees | Not more than 2 employees, and only on a part-time basis |
| Records | Proper books of account |
| Independence | Part-time work performed for someone other than the full-time employer |
| Net self-employment profit | Flat **10%** on the first **EUR 12,000** of net profit (revenue less directly incurred expenses) |
| Excess over EUR 12,000 | Declare the excess in the Income Tax Return at progressive rates |
| Form / deadline | TA22, filed and paid electronically by **30 April** of the following year |

The TA22 election is optional -- the taxpayer may instead declare everything in the return at progressive rates (ITA Art. 90A(2)), with any part-time tax paid available as a credit/refund.

SSC: do NOT assert that "Class 1 covers all". Class 2 liability for a person who is simultaneously employed and self-occupied is governed by the Social Security Act (Cap. 318) and depends on the person's contribution status -- flag for the reviewer in every TA22 case.

### 5.9 Provisional Tax

**Legislation:** Provisional Tax (P.T.) Rules, S.L. 372.18 (under ITMA, Cap. 372)

**Provisional Tax instalments**  _([Provisional Tax (P.T.) Rules, S.L. 372.18](https://legislation.mt/eli/sl/372.18/eng))_

| Instalment | % of PT benchmark | Deadline |
| --- | --- | --- |
| 1st | 20% | 30 April |
| 2nd | 30% | 31 August |
| 3rd | 50% | 21 December |

The PT benchmark is based on the latest self-assessment (last filed return), as adjusted by any PT reduction claim accepted by MTCA -- never the current year's projected income. In practice a newly registered self-employed person receives no PT demand in the first year (no benchmark exists) and settles the first year's tax in full with the return -- reviewer to confirm against the client's PT statement.

### 5.10 Filing Deadlines and Penalties

**Filing Deadlines and Penalties**  _([ITMA Art. 44; Schedule to ITA Art. 56(12)(c)](https://legislation.mt/eli/cap/372/eng))_

| Item | Detail |
| --- | --- |
| Income Tax Return deadline | **30 June** of the following year; online filing routinely extended by MTCA notice (basis 2024: electronic extended to 8 Aug 2025; basis 2025: manual AND electronic extended to 31 July 2026) |
| TA22 deadline | **30 April** of the following year (tax paid with the form) |
| TA24 (rental 15%) deadline | **30 April** of the following year |
| Late return -- additional tax (individuals) | Fixed banded scale, Table A, Schedule to ITA Art. 56(12)(c): EUR 10 (within 6 months) / 50 (6-12m) / 100 (12-18m) / 150 (18-24m) / 200 (24-36m) / 300 (36-48m) / 400 (48-60m) / 500 (over 60m). Remittable for reasonable excuse (insufficiency of funds and reliance on an agent do NOT count) |
| Late payment -- additional tax | 1% of the unpaid tax per month or part month (ITMA Art. 44(1)(a)); no cap stated in the statute; remittable at the Commissioner's discretion in limited cases |
| Late payment -- interest | 0.6% per month or part month for tax payable on/after 31 Aug 2022 (ITMA Art. 44(2A)); "the total interest shall not exceed the amount of the said tax" |
| Omission from a return | Additional tax of 1.5% per month of the endangered tax, max 60 months (items 5 and 7, Schedule to Art. 56(12)(c)); reduced to nil (rectified within 12 months, pre-enquiry), 0.1%/month (pre-enquiry, later), or 0.75%/month (post-enquiry-notice, pre-assessment) on voluntary rectification; no interest runs on this additional tax |

### 5.11 TA24 -- What It Actually Is (Out of Computation Scope)

- **TA24 explanation** — TA24 is the prescribed form for the OPTIONAL 15% final tax on **gross rental income** under ITA Art. 31D, payable by 30 April of the following year. No deductions are allowed against the gross rent; the tax is final (no set-off or refund); income taxed this way is excluded from the return. If the option is not exercised, rental income is declared in the return at progressive rates (with limited deductions). Choosing between the two is a reviewer decision -- raise R-MT-7.  _([ITA Art. 31D](https://legislation.mt/eli/cap/123/eng))_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

**Legislation:** ITA Art. 14(1)

- Calculate proportion of home used for business: dedicated room(s) as percentage of total rooms or floor area
- Apply that percentage to: rent or mortgage interest, electricity, water, internet, maintenance
- Must be a dedicated workspace -- a dual-use room (kitchen table, living room) does NOT qualify
- Client must document the calculation and retain for 6 years

**Conservative default:** 0% deduction until reviewer confirms room arrangement.

**Flag for reviewer:** Confirm room count, floor area basis, and that workspace is genuinely dedicated.

### 6.2 Motor Vehicle Business Use

- Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible
- Client must maintain a mileage log (business trips vs total mileage)
- Capital allowance on vehicle: 20% straight-line (5-year minimum), multiplied by business %; non-commercial vehicles computed on a maximum cost of EUR 14,000

**Conservative default:** 0% business use until mileage log provided.

**Flag for reviewer:** Confirm business percentage is documented and reasonable.

### 6.3 Phone / Internet Mixed Use

- Business use portion only
- Client must provide reasonable estimate of business vs personal use

**Conservative default:** 0% deduction until business percentage confirmed.

### 6.4 Bad Debt Write-Off

**Legislation:** ITA Art. 14(1)(d) and the Commissioner's Bad Debt Guidelines

- Deductible only if: (1) income was previously declared in WP1, (2) the debt is proved to the Commissioner's satisfaction to have become bad in the basis year (insolvency, untraceable debtor, statute-barred, all legal steps exhausted, etc.), (3) any later recovery is taxed as a receipt
- Flag for reviewer to confirm the conditions

### 6.5 Software Capitalisation vs Expensing

- Recurring subscriptions (monthly/annual): expense in WP2 fully
- Perpetual licence: capital -- WP15 at 25%/year (4-year minimum), regardless of amount
- Flag for reviewer if nature of licence is unclear

### 6.6 Low-Value Asset Treatment

- Strictly there is NO statutory de minimis: all business assets are depreciated per S.L. 123.01
- Some practitioners expense trivial-value assets immediately as a practical simplification; this has no statutory basis
- Flag for reviewer to confirm the firm's policy before expensing any asset

### 6.7 Asset Disposal (Balancing Statements)

**Legislation:** ITA Art. 24

- On disposal/scrapping, submit a balancing statement with the return: cost, allowances claimed, proceeds
- Proceeds above tax written-down value = balancing charge (taxable, capped at allowances claimed); below = balancing allowance (deductible)
- Rollover relief may defer a balancing charge against a replacement asset
- Flag for reviewer to confirm disposal proceeds and written-down value

## Section 7 -- Excel Working Paper Template

```
MALTA INCOME TAX -- SELF-EMPLOYED WORKING PAPER (maps to the MTCA Income Tax Return)
Tax Year (basis): 2025
Client: ___________________________
Marital Status: Single / Married / Parent

A. WP1 -- GROSS SELF-EMPLOYMENT INCOME
  A1. Client payments (net of VAT if Art.10)    ___________
  A2. Platform payouts (Stripe, PayPal, etc.)   ___________
  A3. Other business income                      ___________
  A4. TOTAL WP1                                  ___________

B. WP2 -- ALLOWABLE DEDUCTIONS
  B1. Office rent                                ___________
  B2. Professional insurance                     ___________
  B3. Accountancy / legal fees                   ___________
  B4. Office supplies / stationery               ___________
  B5. Software subscriptions                     ___________
  B6. Marketing / advertising                    ___________
  B7. Bank charges / payment processing fees     ___________
  B8. Training / CPD / professional subs         ___________
  B9. Travel (flights, hotels, transport)        ___________
  B10. Telecoms (business % of phone/internet)   ___________
  B11. Home office (% of utilities/rent)         ___________
  B12. Vehicle expenses (business %)             ___________
  B13. Other allowable expenses                  ___________
  B14. TOTAL WP2                                 ___________

C. WP3 -- NET PROFIT (A4 - B14)                 ___________

D. WP4 -- OTHER INCOME
  D1. Employment income                          ___________
  D2. Rental income (progressive option only --
      15% Art.31D rents go on TA24, NOT here)    ___________
  D3. Investment income                          ___________
  D4. TOTAL WP4                                  ___________

E. WP5 -- TOTAL INCOME (C + D4)                 ___________

F. STATUTORY DEDUCTIONS
  F1. WP15 -- Capital allowances                 ___________
  F2. WP25 -- Total deductions (F1)              ___________

G. WP30 -- CHARGEABLE INCOME (E - F2)           ___________

H. TAX COMPUTATION (pass to deterministic engine)
  H1. WP35 -- Tax liability                      ___________
  H2. WP36 -- Provisional tax paid               ___________
  H3. WP37 -- Tax credits                        ___________
  H4. WP40 -- Tax due / refund                   ___________

MEMO (not in computation):
  M1. SSC Class 2 paid in year (NOT deductible)  ___________

REVIEWER FLAGS:
  [ ] Marital status confirmed?
  [ ] VAT registration type confirmed (Art.10/11)?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/internet business % confirmed?
  [ ] All T2 items flagged for review?
  [ ] Entertainment expenses excluded (or reviewer-approved)?
  [ ] Capital items in WP15 (not WP2)?
  [ ] SSC excluded from deductions (memo only)?
  [ ] WP lines mapped to the current MTCA return fields?
```

## Section 8 -- Bank Statement Reading Guide

### Maltese Bank Statement Formats

**Maltese Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BOV (Bank of Valletta) | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description contains counterparty + reference |
| HSBC Malta | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant name |
| APS Bank | PDF | Date, Particulars, Withdrawals, Deposits | Less common CSV; shorter descriptions |
| Revolut Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data; multi-currency possible |
| Wise Business | CSV | Date, Description, Amount, Currency, Running Balance | Multi-currency; conversion fees separate line |

### Key Maltese Banking Terms

**Key Maltese Banking Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRASFERIMENT / TRF | Transfer | Check direction for income/expense |
| DEBIT DIRETT / DD | Direct debit | Regular expense (utility, subscription) |
| STANDING ORDER / SO | Standing order | Regular expense (rent, loan) |
| KARTA / CARD | Card payment | Expense -- check merchant |
| HLAS / DEPOSIT | Deposit | Potential income |
| SPEJJEZ / CHARGES | Bank charges | Deductible (WP2) |
| INTERESSI | Interest | Interest income (WP4) or bank charge |
| SELF-SERVICE / ATM | Cash withdrawal | Ask what cash was spent on |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- MALTA INCOME TAX
1. Marital status: single, married, or parent (maintaining a child)?
2. Employment status: fully self-employed (full return) or employed/pensioner/student
   with side income (TA22 option)?
3. VAT registration: Article 10 or Article 11?
4. Home office: dedicated room or shared space? If dedicated, what % of floor area?
5. Vehicle: do you use a car for business? If yes, what % is business use? Do you keep a mileage log?
6. Phone/internet: what % is business use?
7. SSC Class 2: total amount paid in the tax year? (memo only -- not deductible)
8. Provisional tax: total amount paid in the tax year?
9. Any other income (employment, rental, dividends, interest)? If rental: 15% TA24 option or progressive?
10. Any capital assets purchased during the year?
```

## Section 10 -- Reference Material

### Key Legislation References

**Key Legislation References**  _([ITA Cap. 123; ITMA Cap. 372](https://legislation.mt/eli/cap/372/eng))_

| Topic | Reference |
| --- | --- |
| Income tax rates | ITA Cap. 123, Art. 56(1); annual rate amendments via Budget Measures Implementation Acts; MTCA published rate tables |
| Allowable deductions | ITA Art. 14 (positive test) |
| Disallowed deductions | ITA Art. 26 (negative test: domestic/private, capital, recoverable, voluntary) |
| Capital allowances | ITA Art. 14(1)(f) and (j); S.L. 123.01 (Wear and Tear Rules); S.L. 123.173 (Industrial Buildings -- offices definition); ITA Art. 24 (balancing statements) |
| Part-time regime (TA22) | ITA Art. 90A + Part-Time Work Rules; MTCA guidance (10% / EUR 12,000, basis 2025) |
| Rental 15% final tax (TA24) | ITA Art. 31D |
| Provisional tax | Provisional Tax (P.T.) Rules, S.L. 372.18 |
| Filing deadlines | ITMA Cap. 372; MTCA Tax Return Cycle and annual extension notices |
| Penalties / interest | ITMA Art. 44(1)(a) and (2A); Schedule to ITA Art. 56(12)(c) (Tables A/B, items 5-9) |
| Record keeping | ITA / ITMA (6-year retention) |

### Capital Allowances vs VAT Capital Goods -- Important Distinction

**Capital Allowances vs VAT Capital Goods**

| System | Threshold | Purpose |
| --- | --- | --- |
| VAT Capital Goods Scheme | EUR 1,160 gross | VAT capital-goods reporting only |
| Income Tax Capital Allowances | No threshold | ALL business assets depreciated via WP15 |

A EUR 500 printer: depreciated for income tax (25% x EUR 500 = EUR 125/year in WP15, electronic equipment, 4-year minimum) but does NOT enter the VAT capital goods reporting (below EUR 1,160). These are entirely separate systems.

### Test Suite

Expected tax figures are engine-derived reference outputs computed from the Section 1 tables (formula: chargeable x rate - subtract). Regenerate from the deterministic engine whenever the rate tables change; never hand-edit them.

**Test 1 -- Standard single, mid-range income.**
Input: Single, gross revenue EUR 45,000, allowable expenses EUR 13,000, capital allowances EUR 375, SSC paid EUR 3,000, provisional tax EUR 3,500.
Derivation:
- WP3 = 45,000 - 13,000 = 32,000
- WP15 = 375; SSC 3,000 = memo only (NOT deductible)
- WP30 = 32,000 - 375 = **31,625**
- WP35 (single, 2025): 31,625 falls in 16,001-60,000 band: 31,625 x 0.25 - 3,400 = 7,906.25 - 3,400 = **4,506.25**
  (bracket check: 12,000 @ 0% = 0; 4,000 @ 15% = 600; 15,625 @ 25% = 3,906.25; total 4,506.25)
- WP40 = 4,506.25 - 3,500 = **1,006.25 due**

**Test 2 -- Married, higher income.**
Input: Married, gross EUR 80,000, expenses EUR 20,000, SSC paid EUR 4,362, no provisional tax (first year).
Derivation:
- WP3 = 80,000 - 20,000 = 60,000; SSC 4,362 = memo only
- WP30 = **60,000**
- WP35 (married, 2025): 60,000 x 0.25 - 4,550 = 15,000 - 4,550 = **10,450**
  (bracket check: 15,000 @ 0% = 0; 8,000 @ 15% = 1,200; 37,000 @ 25% = 9,250; total 10,450)
- WP40 = **10,450 due**

**Test 3 -- TA22 eligible.**
Input: Full-time employed, side net profit EUR 8,000, registered with Jobsplus.
Expected: TA22 at 10% = 8,000 x 0.10 = **EUR 800**, paid by 30 April. SSC Class 2 position NOT asserted -- flag to reviewer (Cap. 318 question).

**Test 4 -- Entertainment blocked.**
Input: EUR 2,000 client entertainment in WP2.
Expected: Remove from WP2 (conservative default). Reviewer flag raised; no partial deduction applied.

**Test 5 -- Capital item in wrong line.**
Input: Laptop EUR 1,500 in WP2.
Expected: Remove from WP2. Add 1,500 x 25% = **EUR 375** to WP15 (computers, 4-year minimum).

**Test 6 -- Article 11 VAT as expense.**
Input: Article 11 client. Invoice EUR 236 gross (EUR 200 + EUR 36 VAT at 18%).
Expected: WP2 = **EUR 236** (full gross). Cannot reclaim VAT.

**Test 7 -- SSC misclassified as deduction (regression for the 2025-10 correction).**
Input: SSC Class 2 EUR 3,000 placed in a deduction line.
Expected: Remove from all deduction lines; memo only. Chargeable income unchanged by SSC.

## PROHIBITIONS

- NEVER apply a rate table without knowing marital status
- NEVER compute WP35 tax figures directly -- pass chargeable income to the deterministic engine
- NEVER deduct SSC Class 2 (or any social security contribution) anywhere in the computation
- NEVER allow entertainment expenses in WP2 without an explicit reviewer override
- NEVER allow income tax itself as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER include VAT collected on sales in WP1 for Article 10 clients
- NEVER allow a capital item in WP2 -- it must go through WP15 (no de minimis)
- NEVER call TA24 the self-employed return -- TA24 is the Art. 31D rental 15% form
- NEVER use current year income for provisional tax -- always the latest self-assessment benchmark
- NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
