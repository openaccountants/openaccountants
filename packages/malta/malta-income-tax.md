---
name: malta-income-tax
description: >
  Use this skill whenever asked about Malta income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "TA24", "income tax return", "allowable deductions", "capital allowances", "provisional tax", "TA22 regime", "chargeable income", "tax credits", "self-employed tax Malta", or any question about filing or computing income tax for a self-employed or part-time self-employed client. Also trigger when preparing or reviewing a TA24 or TA22 return, computing deductible expenses, or advising on provisional tax instalments. This skill covers tax rates (single/married/parent), TA24 box structure, allowable deductions, capital allowances, provisional tax, TA22 regime, penalties, and interaction with VAT and SSC. ALWAYS read this skill before touching any income tax work.
version: 2.0
jurisdiction: MT
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Malta Income Tax -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Malta (Republic of Malta) |
| Tax | Income Tax (Einkommensteuer equivalent) |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Income Tax Act, Chapter 123 |
| Supporting legislation | Income Tax Management Act (Chapter 372); ITA Article 4C (TA22); ITA Article 14 (deductions); ITA Article 16 + 6th Schedule (capital allowances); ITMA Articles 44, 51, 52, 52A (penalties) |
| Tax authority | Commissioner for Revenue (CFR) / MTCA, Malta |
| Filing portal | MTCA e-Services |
| Filing deadline | 30 June of the following year (TA24 and TA22) |
| Contributor | Michael Cutajar, CPA (Warrant No. 125122), ACCA |
| Validated by | Michael Cutajar |
| Validation date | March 2026 |
| Skill version | 2.0 |

### Tax Rate Brackets (2025/2026)

**Single Rates**

| Taxable Income (EUR) | Rate | Cumulative Tax at Top |
|---|---|---|
| 0 -- 9,100 | 0% | EUR 0 |
| 9,101 -- 14,500 | 15% | EUR 810 |
| 14,501 -- 19,500 | 25% | EUR 2,060 |
| 19,501 -- 60,000 | 25% | EUR 12,185 |
| 60,001+ | 35% | -- |

**Married Rates (joint computation)**

| Taxable Income (EUR) | Rate | Cumulative Tax at Top |
|---|---|---|
| 0 -- 12,700 | 0% | EUR 0 |
| 12,701 -- 21,200 | 15% | EUR 1,275 |
| 21,201 -- 28,700 | 25% | EUR 3,150 |
| 28,701 -- 60,000 | 25% | EUR 10,975 |
| 60,001+ | 35% | -- |

**Parent Rates (single parent maintaining a child)**

| Taxable Income (EUR) | Rate | Cumulative Tax at Top |
|---|---|---|
| 0 -- 10,500 | 0% | EUR 0 |
| 10,501 -- 15,800 | 15% | EUR 795 |
| 15,801 -- 21,200 | 25% | EUR 2,145 |
| 21,201 -- 60,000 | 25% | EUR 11,845 |
| 60,001+ | 35% | -- |

**Note (2026):** The first 0% band was increased by EUR 500 for all categories as part of the 2026 budget measures.

**Malta does not have a separate personal allowance -- the 0% band IS the personal allowance.**

### TA24 Key Boxes

| Box | Description |
|---|---|
| Box 1 | Gross income from self-employment |
| Box 2 | Less: Allowable deductions |
| Box 3 | Net profit/loss (Box 1 - Box 2) |
| Box 4 | Other income (employment, rental, dividends, interest) |
| Box 5 | Total income (Box 3 + Box 4) |
| Box 15 | Capital allowances (depreciation per 6th Schedule) |
| Box 20 | SSC Class 2 (amount actually paid in the tax year) |
| Box 25 | Total deductions (sum of all deduction boxes including Box 15 and Box 20) |
| Box 30 | Chargeable income (Box 5 - Box 25) |
| Box 35 | Tax liability (applied from rate table to Box 30) |
| Box 36 | Less: Provisional tax paid |
| Box 37 | Less: Tax credits |
| Box 40 | Tax due / refund (Box 35 - Box 36 - Box 37) |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown marital status | STOP -- do not apply a rate table without marital status |
| Unknown filing status (TA24 vs TA22) | TA24 (full self-employed) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown VAT registration type | Article 10 (standard) |
| Unknown asset useful life | Use 6th Schedule rates |
| Unknown whether expense is entertainment | Treat as entertainment (blocked) |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of marital status (single/married/parent) and employment status (fully self-employed TA24 or part-time TA22).

**Recommended** -- all sales invoices, purchase invoices/receipts, SSC Class 2 payment records, prior year TA24 or tax assessment, VAT registration type (Article 10 or Article 11).

**Ideal** -- complete income and expenditure account, asset register with capital allowances schedule, provisional tax payment confirmations, employment income details (if TA22).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This TA24 was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that the wholly-and-exclusively test is met."

### Refusal Catalogue

**R-MT-1 -- Marital status unknown.** "Marital status determines the applicable rate table. This skill cannot compute tax without knowing whether the client is single, married, or a single parent. Please confirm before proceeding."

**R-MT-2 -- Group structures or partnerships.** "This skill covers sole proprietors and part-time self-employed individuals only. Group structures, partnerships, and companies file separate returns. Escalate to a warranted accountant."

**R-MT-3 -- Non-resident income.** "Non-resident and dual-resident taxation has different rules. Out of scope. Escalate to a warranted accountant."

**R-MT-4 -- Capital gains / property disposals.** "Capital gains computations under Article 5A or property transfers require specialised analysis. Escalate to a warranted accountant."

**R-MT-5 -- Arrears / enforcement.** "Client has outstanding tax arrears or is subject to MTCA enforcement action. The 1.6%/month combined late payment charges are severe and uncapped. Do not advise. Escalate to a warranted accountant immediately."

**R-MT-6 -- VAT return requested.** "This skill covers income tax (TA24/TA22) only. For Malta VAT, use the malta-vat-return skill."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | TA24 Line | Treatment | Notes |
|---|---|---|---|
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Box 1 (gross revenue) | Business income | If Article 10 VAT-registered, extract net (excl. 18% VAT) |
| HONORARJU, FEES, PROFESSIONAL FEES, CONSULTANCY | Box 1 | Business income | Professional fees -- typical for self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Box 1 | Business income | Platform payout -- match to underlying invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Box 1 | Business income | Platform payout -- verify against invoices |
| WISE PAYOUT, WISE TRANSFER | Box 1 | Business income | International platform payout |
| REVOLUT PAYOUT | Box 1 | Business income | Check if business or personal Revolut |
| UPWORK, FIVERR, TOPTAL | Box 1 | Business income | Freelance platform -- net of platform commission |
| PAGA, SALARY, STIPENDJU, EMPLOYER [name] | Box 4 (other income) | Employment income | NOT self-employment -- goes to Box 4 |
| KIRI, RENT RECEIVED | Box 4 | Rental income | Not self-employment income |
| INTERESSI, INTEREST RECEIVED | Box 4 | Investment income | Interest income |
| DIVIDENDI, DIVIDEND | Box 4 | Investment income | Dividend income |
| CFR REFUND, TAX REFUND, RISTORN | EXCLUDE | Not income | Tax refund from prior year |
| BONUS GVERN, GOVERNMENT GRANT, MALTA ENTERPRISE | EXCLUDE unless revenue grant | Check nature | Capital grants EXCLUDE; revenue grants = Box 1 |

### 3.2 Expense Patterns (Debits on Bank Statement) -- Fully Deductible (Box 2)

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| KIRI UFFICCJU, OFFICE RENT, RENT [commercial address] | Office rent | Box 2 -- fully deductible | Dedicated business premises |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Professional insurance | Box 2 -- fully deductible | |
| ACCOUNTANT, AUDITOR, BOOKKEEP, CPA, ACCA FEES | Accountancy fees | Box 2 -- fully deductible | |
| AVUKAT, LAWYER, LEGAL, NOTARY (business) | Legal fees | Box 2 -- fully deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES, VIKING | Office supplies | Box 2 -- fully deductible | |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing/advertising | Box 2 -- fully deductible | |
| TRAINING, CPD, COURSE, SEMINAR, CONFERENCE | Training/CPD | Box 2 -- fully deductible | Must relate to current business |
| MIA, ACCA SUBSCRIPTION, PROFESSIONAL BODY | Professional subscriptions | Box 2 -- fully deductible | |
| BOV CHARGE, HSBC CHARGE, BANK FEE, MAINTENANCE FEE | Bank charges | Box 2 -- fully deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, TRANSACTION FEE | Payment processing fees | Box 2 -- fully deductible | |
| POSTAGE, MALTAPOST (business) | Postage | Box 2 -- fully deductible | Business correspondence |
| DOMAIN, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Box 2 -- fully deductible | Under EUR 1,160 = expense; over = capital |

### 3.3 Expense Patterns (Debits) -- SaaS and Software (Box 2 if under EUR 1,160)

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Box 2 -- fully deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Box 2 -- fully deductible | |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Box 2 -- fully deductible | |
| SOFTWARE LICENCE (perpetual, over EUR 1,160) | Capital item | Box 15 -- capitalise at 25%/year | Perpetual licence above threshold |

### 3.4 Expense Patterns (Debits) -- Utilities (Box 2, may need apportionment)

| Pattern | Category | Tier | Notes |
|---|---|---|---|
| ARMS, ARMS LTD, ENEMALTA | Electricity/water | T2 if home office | 100% if dedicated office; proportional if home |
| MELITA, GO PLC, EPIC | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |
| VODAFONE, MOBILE, GO MOBILE | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| AIR MALTA, RYANAIR, WIZZ AIR, EASYJET | Flights | Box 2 if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Box 2 if business travel | |
| BOLT, UBER, ECABS, TAXI | Local transport | Box 2 if business purpose | |
| FUEL, ENEMED, PETROL | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARKING, CVA, MCP PARKING | Parking | T2 -- business % only | |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| RESTAURANT, DINNER, LUNCH, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Blocked under Article 14 -- no partial deduction |
| PERSONAL, GROCERIES, SUPERMARKET, LIDL, PAVI | Personal expenses | NOT deductible | Private living costs |
| FINE, PENALTY, MULTA, PARKING FINE | Fines/penalties | NOT deductible | Public policy |
| CFR PAYMENT, INCOME TAX, TAX PAYMENT | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (Box 15)

| Pattern | Category | Annual Rate | Notes |
|---|---|---|---|
| LAPTOP, COMPUTER, MACBOOK, IMAC, DESKTOP | Computer hardware | 25% | Box 15 |
| PRINTER, SCANNER, COPIER | Office equipment | 20% | Box 15 |
| FURNITURE, DESK, CHAIR, FILING CABINET | Furniture/fittings | 10% | Box 15 |
| VEHICLE, CAR (business) | Motor vehicle | 20% | Box 15, business % only |
| AIR CONDITIONING, AC UNIT | A/C equipment | 20% | Box 15 |

### 3.8 Exclusions (Neither Income nor Expense)

| Pattern | Treatment | Notes |
|---|---|---|
| INTERNAL TRANSFER, OWN ACCOUNT, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, SELF-EMPLOYED LOAN, PERSONAL LOAN | EXCLUDE | Loan principal movement |
| SSC, CLASS 2, SOCIAL SECURITY | Box 20 (SSC deduction) | Deductible in Box 20, NOT Box 2 |
| VAT PAYMENT, CFR VAT | EXCLUDE | VAT liability payment, not expense |
| PROVISIONAL TAX, PT INSTALMENT | Box 36 (provisional tax paid) | Not an expense -- credit against liability |

### 3.9 Maltese Banks -- Statement Format Reference

| Bank | Common Patterns | Notes |
|---|---|---|
| BOV (Bank of Valletta) | TRANSFER, DD, SO, CHQ, CHARGES | PDF/CSV; Buchungstag format DD/MM/YYYY |
| HSBC Malta | PAYMENT, TRF, D/D, FEE | PDF/CSV; counterparty in description field |
| APS Bank | TRANSFER, DIRECT DEBIT, CHARGE | PDF; less common CSV export |
| Revolut Business | PAYMENT, TRANSFER, CARD PAYMENT | CSV; clean counterparty names |
| Wise Business | TRANSFER, CONVERSION, FEE | CSV; multi-currency -- use EUR amounts |

---

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (Article 10, VAT-registered)

**Input line:**
`15/03/2025 ; BOV TRANSFER IN ; STUDIO KREBS GMBH ; PAYMENT INV-2025-003 ; +1,180.00 ; EUR`

**Reasoning:**
Client payment for services. Client is Article 10 VAT-registered, so EUR 1,180 includes 18% VAT. Net = EUR 1,000 (Box 1). EUR 180 is VAT collected (excluded from income -- it is a liability to CFR).

**Classification:** Box 1 = EUR 1,000. VAT EUR 180 excluded.

### Example 2 -- SaaS Subscription (Fully Deductible)

**Input line:**
`01/04/2025 ; HSBC DD ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD APR ; -29.99 ; EUR`

**Reasoning:**
Monthly SaaS subscription. Under EUR 1,160, recurring. Fully deductible as operating expense. For Article 10 clients, the net amount (excl. recoverable VAT) is the expense. If Article 11, gross amount is the cost.

**Classification:** Box 2 = EUR 29.99 (or net if Article 10 with recoverable input VAT).

### Example 3 -- Entertainment (Blocked)

**Input line:**
`22/04/2025 ; BOV CARD ; WATERBISCUIT RESTAURANT ; CLIENT DINNER ; -85.00 ; EUR`

**Reasoning:**
Client entertainment. Blocked under Article 14. No partial deduction. No apportionment. Full block. Same as VAT treatment.

**Classification:** NOT deductible. Remove from Box 2 entirely.

### Example 4 -- SSC Class 2 Payment

**Input line:**
`10/01/2025 ; BOV DD ; CFR SSC CLASS 2 ; Q4 2024 ; -1,090.50 ; EUR`

**Reasoning:**
SSC Class 2 payment. Deductible, but in Box 20, NOT Box 2. SSC paid in 2025 = deduction in 2025 TA24.

**Classification:** Box 20 = EUR 1,090.50.

### Example 5 -- Laptop Purchase (Capital Item)

**Input line:**
`03/06/2025 ; HSBC CARD ; APPLE STORE MALTA ; MACBOOK PRO ; -1,899.00 ; EUR`

**Reasoning:**
Capital asset. Computer hardware depreciated at 25% per year (6th Schedule). EUR 1,899 x 25% = EUR 474.75 per year in Box 15. Do NOT put in Box 2.

**Classification:** Box 15 = EUR 474.75. NOT Box 2.

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`15/05/2025 ; BOV TRANSFER ; OWN ACCOUNT - SAVINGS ; ; -2,000.00 ; EUR`

**Reasoning:**
Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 The Wholly and Exclusively Test

**Legislation:** Income Tax Act, Article 14

An expense is deductible only if incurred wholly and exclusively in the production of income. Mixed-use expenses must be apportioned. The apportionment method must be reasonable and documented.

### 5.2 Revenue Recognition

All business income goes to Box 1. For Article 10 clients, report net of VAT. For Article 11 clients, report gross (no VAT charged). VAT collected on sales is NOT income.

### 5.3 Capital vs Revenue

Capital items must go through Box 15 (capital allowances), not Box 2. There is no de minimis threshold -- all business assets are depreciated per the 6th Schedule. The VAT Capital Goods Scheme threshold (EUR 1,160) is a separate system.

### 5.4 Capital Allowance Rates (6th Schedule)

| Asset Type | Annual Rate |
|---|---|
| Computer hardware | 25% |
| Computer software | 25% |
| Motor vehicles | 20% |
| Plant and machinery | 20% |
| Office equipment | 20% |
| Air conditioning | 20% |
| Furniture and fittings | 10% |
| Commercial buildings | 2% |
| Industrial buildings | 2% |

Depreciation is straight-line on cost. Starts in the year first used in business.

### 5.5 SSC Class 2 Deduction

SSC Class 2 paid during the tax year is deductible in Box 20 of the TA24. It is deducted in the year it is paid (cash basis).

### 5.6 Non-Deductible Expenses

| Expense | Reason |
|---|---|
| Entertainment (client meals, events) | Blocked under Article 14 |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Capital expenditure | Goes through Box 15 |
| Drawings / personal withdrawals | Not an expense |
| Personal car insurance (unapportioned) | Personal |

### 5.7 VAT Interaction

| Scenario | Income Tax Treatment |
|---|---|
| VAT collected on sales (Article 10) | NOT income -- exclude from Box 1 |
| Input VAT recovered (Article 10) | NOT an expense -- exclude from Box 2 |
| Input VAT blocked/non-deductible (Article 10) | IS an expense -- include in Box 2 |
| Article 11 client -- all VAT paid on purchases | IS an expense -- gross amount is cost |
| Foreign VAT (non-reclaimable) | IS an expense -- full gross is cost |

### 5.8 TA22 Regime (Part-Time Self-Employment)

**Legislation:** Income Tax Act, Article 4C

| Condition | Requirement |
|---|---|
| Employment status | Must be in full-time employment with Class 1 SSC |
| Net self-employment profit | Must not exceed EUR 12,000 |
| Tax rate | Flat 10% on net self-employment profit |
| SSC | No additional Class 2 -- Class 1 covers all |

If net profit exceeds EUR 12,000: first EUR 12,000 at 10% on TA22, excess at progressive rates on TA24.

### 5.9 Provisional Tax

**Legislation:** Income Tax Management Act, Chapter 372

| Instalment | % of Prior Year Tax | Deadline |
|---|---|---|
| 1st | 20% | 30 April |
| 2nd | 30% | 31 August |
| 3rd | 50% | 21 December |

Always based on prior year's final liability. First year = no provisional tax due.

### 5.10 Filing Deadline and Penalties

| Item | Detail |
|---|---|
| TA24/TA22 filing deadline | 30 June of following year |
| Late filing | EUR 50 + EUR 10/month (max EUR 500) |
| Late payment surcharge | 1% per month -- UNCAPPED |
| Late payment interest | 0.6% per month -- capped at original tax |
| Combined late payment | 1.6% per month total |
| Incorrect return | Up to EUR 2,000 |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

**Legislation:** Income Tax Act, Article 14

- Calculate proportion of home used for business: dedicated room(s) as percentage of total rooms or floor area
- Apply that percentage to: rent or mortgage interest, electricity, water, internet, maintenance
- Must be a dedicated workspace -- a dual-use room (kitchen table, living room) does NOT qualify
- Client must document the calculation and retain for 6 years

**Conservative default:** 0% deduction until reviewer confirms room arrangement.

**Flag for reviewer:** Confirm room count, floor area basis, and that workspace is genuinely dedicated.

### 6.2 Motor Vehicle Business Use

- Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible
- Client must maintain a mileage log (business trips vs total mileage)
- Capital allowance on vehicle: 20% straight-line on cost, multiplied by business %

**Conservative default:** 0% business use until mileage log provided.

**Flag for reviewer:** Confirm business percentage is documented and reasonable.

### 6.3 Phone / Internet Mixed Use

- Business use portion only
- Client must provide reasonable estimate of business vs personal use

**Conservative default:** 0% deduction until business percentage confirmed.

### 6.4 Bad Debt Write-Off

- Deductible only if: (1) income was previously declared in Box 1, (2) all reasonable recovery steps taken, (3) debt is genuinely irrecoverable
- Flag for reviewer to confirm all three conditions

### 6.5 Software Capitalisation vs Expensing

- Recurring subscriptions (monthly/annual): expense in Box 2 fully
- Perpetual licence over EUR 1,160: capitalise at 25%/year in Box 15
- Flag for reviewer if nature of licence is unclear

### 6.6 Low-Value Asset Treatment

- Some practitioners expense assets under approximately EUR 700 immediately
- Flag for reviewer to confirm treatment -- strictly, all assets should be depreciated per 6th Schedule

### 6.7 Asset Disposal

- Sale proceeds minus written-down value = balancing charge (taxable) or balancing allowance (deductible)
- Flag for reviewer to confirm disposal proceeds and written-down value

---

## Section 7 -- Excel Working Paper Template

```
MALTA INCOME TAX -- TA24 WORKING PAPER
Tax Year: 2025
Client: ___________________________
Marital Status: Single / Married / Parent

A. BOX 1 -- GROSS SELF-EMPLOYMENT INCOME
  A1. Client payments (net of VAT if Art.10)    ___________
  A2. Platform payouts (Stripe, PayPal, etc.)   ___________
  A3. Other business income                      ___________
  A4. TOTAL Box 1                                ___________

B. BOX 2 -- ALLOWABLE DEDUCTIONS
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
  B14. TOTAL Box 2                               ___________

C. BOX 3 -- NET PROFIT (A4 - B14)               ___________

D. BOX 4 -- OTHER INCOME
  D1. Employment income                          ___________
  D2. Rental income                              ___________
  D3. Investment income                          ___________
  D4. TOTAL Box 4                                ___________

E. BOX 5 -- TOTAL INCOME (C + D4)               ___________

F. DEDUCTIONS
  F1. Box 15 -- Capital allowances               ___________
  F2. Box 20 -- SSC Class 2                      ___________
  F3. Box 25 -- Total deductions (F1 + F2)       ___________

G. BOX 30 -- CHARGEABLE INCOME (E - F3)         ___________

H. TAX COMPUTATION (pass to deterministic engine)
  H1. Box 35 -- Tax liability                    ___________
  H2. Box 36 -- Provisional tax paid             ___________
  H3. Box 37 -- Tax credits                      ___________
  H4. Box 40 -- Tax due / refund                 ___________

REVIEWER FLAGS:
  [ ] Marital status confirmed?
  [ ] VAT registration type confirmed (Art.10/11)?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/internet business % confirmed?
  [ ] All T2 items flagged for review?
  [ ] Entertainment expenses excluded?
  [ ] Capital items in Box 15 (not Box 2)?
  [ ] SSC in Box 20 (not Box 2)?
```

---

## Section 8 -- Bank Statement Reading Guide

### Maltese Bank Statement Formats

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| BOV (Bank of Valletta) | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description contains counterparty + reference |
| HSBC Malta | PDF, CSV | Value Date, Description, Amount, Balance | Card transactions show merchant name |
| APS Bank | PDF | Date, Particulars, Withdrawals, Deposits | Less common CSV; shorter descriptions |
| Revolut Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data; multi-currency possible |
| Wise Business | CSV | Date, Description, Amount, Currency, Running Balance | Multi-currency; conversion fees separate line |

### Key Maltese Banking Terms

| Term | English | Classification Hint |
|---|---|---|
| TRASFERIMENT / TRF | Transfer | Check direction for income/expense |
| DEBIT DIRETT / DD | Direct debit | Regular expense (utility, subscription) |
| STANDING ORDER / SO | Standing order | Regular expense (rent, loan) |
| KARTA / CARD | Card payment | Expense -- check merchant |
| HLAS / DEPOSIT | Deposit | Potential income |
| SPEJJEZ / CHARGES | Bank charges | Deductible (Box 2) |
| INTERESSI | Interest | Interest income (Box 4) or bank charge |
| SELF-SERVICE / ATM | Cash withdrawal | Ask what cash was spent on |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper (Section 7) with clear flags
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- MALTA INCOME TAX
1. Marital status: single, married, or single parent?
2. Employment status: fully self-employed (TA24) or employed + side income (TA22)?
3. VAT registration: Article 10 or Article 11?
4. Home office: dedicated room or shared space? If dedicated, what % of floor area?
5. Vehicle: do you use a car for business? If yes, what % is business use? Do you keep a mileage log?
6. Phone/internet: what % is business use?
7. SSC Class 2: total amount paid in the tax year?
8. Provisional tax: total amount paid in the tax year?
9. Any other income (employment, rental, dividends, interest)?
10. Any capital assets purchased during the year?
```

---

## Section 10 -- Reference Material

### Key Legislation References

| Topic | Reference |
|---|---|
| Income tax rates | Income Tax Act, Chapter 123, Tax Rate Schedule |
| Allowable deductions | ITA Article 14 |
| Capital allowances | ITA Article 16 + 6th Schedule |
| TA22 part-time regime | ITA Article 4C |
| Provisional tax | ITMA Chapter 372 |
| Filing deadlines | ITMA Chapter 372 |
| Penalties | ITMA Articles 44, 51, 52, 52A |
| Record keeping | ITA; ITMA (6-year retention) |

### Capital Allowances vs VAT Capital Goods -- Important Distinction

| System | Threshold | Purpose |
|---|---|---|
| VAT Capital Goods Scheme | EUR 1,160 gross | Determines VAT Box 30 treatment |
| Income Tax Capital Allowances | No threshold | ALL business assets depreciated via Box 15 |

A EUR 500 printer: depreciated for income tax (25% x EUR 500 = EUR 125/year in Box 15) but does NOT go to VAT Box 30 (below EUR 1,160 threshold). These are entirely separate systems.

### Test Suite

**Test 1 -- Standard single, mid-range income.**
Input: Single, gross revenue EUR 45,000, allowable expenses EUR 13,000, capital allowances EUR 375, SSC EUR 3,000, provisional tax EUR 3,500.
Expected: Box 3 = EUR 32,000, Box 15 = EUR 375, Box 20 = EUR 3,000, Box 25 = EUR 3,375, Box 30 = EUR 28,625. Tax = EUR 4,341. Box 40 = EUR 841 due.

**Test 2 -- Married, higher income.**
Input: Married, gross EUR 80,000, expenses EUR 20,000, SSC EUR 4,362, no provisional tax (first year).
Expected: Box 3 = EUR 60,000, Box 20 = EUR 4,362, Box 30 = EUR 55,638. Tax = EUR 9,885. Box 40 = EUR 9,885 due.

**Test 3 -- TA22 eligible.**
Input: Full-time employed, side net profit EUR 8,000, Class 1 SSC through employer.
Expected: TA22 at 10% = EUR 800. No Class 2 SSC.

**Test 4 -- Entertainment blocked.**
Input: EUR 2,000 client entertainment in Box 2.
Expected: Remove from Box 2. Not deductible.

**Test 5 -- Capital item in wrong box.**
Input: Laptop EUR 1,500 in Box 2.
Expected: Remove from Box 2. Add EUR 375 (25%) to Box 15.

**Test 6 -- Article 11 VAT as expense.**
Input: Article 11 client. Invoice EUR 236 gross (EUR 200 + EUR 36 VAT).
Expected: Box 2 = EUR 236 (full gross). Cannot reclaim VAT.

---

## PROHIBITIONS

- NEVER apply a rate table without knowing marital status
- NEVER compute Box 35 tax figures directly -- pass chargeable income to the deterministic engine
- NEVER allow entertainment expenses in Box 2
- NEVER allow income tax itself as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER include VAT collected on sales in Box 1 for Article 10 clients
- NEVER allow a capital item in Box 2 -- it must go through Box 15
- NEVER put SSC in Box 2 -- it goes in Box 20
- NEVER use current year income for provisional tax -- always prior year final liability
- NEVER present tax calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
