---
name: uk-self-employment-sa103
description: >
  Use this skill whenever asked about UK self-employment income for sole traders filing SA103S (short) or SA103F (full) as part of Self Assessment. Trigger on phrases like "self-employment income", "SA103", "trading income", "sole trader tax", "allowable expenses UK", "capital allowances UK", "trading allowance", "basis period", "simplified expenses", "Class 4 NIC", "loss relief self-employed", or any question about computing self-employment profits for a UK sole trader. Covers trading income computation, allowable expenses, capital allowances (AIA, WDA, FYA), simplified expenses, the trading allowance, basis period reform, loss relief, and Class 4 NIC interaction. ALWAYS read this skill before touching any UK self-employment work.
version: 2.0
jurisdiction: GB
tax_year: 2024-25
category: international
depends_on:
  - income-tax-workflow-base
---

# UK Self-Employment (SA103) -- Sole Trader Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | United Kingdom (England, Wales, Scotland, Northern Ireland) |
| Tax | Income Tax on trading profits + Class 4 NIC |
| Currency | GBP only |
| Tax year | 6 April 2024 -- 5 April 2025 |
| Primary legislation | Income Tax (Trading and Other Income) Act 2005 (ITTOIA 2005); Capital Allowances Act 2001 (CAA 2001) |
| Supporting legislation | Finance Act 2024 (basis period reform); Social Security Contributions and Benefits Act 1992 |
| Tax authority | HM Revenue & Customs (HMRC) |
| Filing portal | HMRC Self Assessment Online |
| Filing deadline (online) | 31 January 2026 |
| Filing deadline (paper) | 31 October 2025 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a UK-qualified accountant (ACA/ACCA/CTA) |
| Skill version | 2.0 |

### Key Thresholds [T1]

| Item | Value |
|---|---|
| SA103S (short form) | Turnover below GBP 90,000 |
| SA103F (full form) | Turnover GBP 90,000+ |
| Trading allowance | GBP 1,000 (alternative to actual expenses) |
| AIA (Annual Investment Allowance) | GBP 1,000,000 |
| Cash basis | Default from 2024/25 (no upper limit) |
| Class 4 NIC lower profits limit | GBP 12,570 |
| Class 4 NIC upper profits limit | GBP 50,270 |

### Class 4 NIC Rates (2024/25) [T1]

| Band | Rate |
|---|---|
| Below GBP 12,570 | 0% |
| GBP 12,570 -- GBP 50,270 | 6% |
| Above GBP 50,270 | 2% |

### Simplified Expenses Rates [T1]

| Category | Rate |
|---|---|
| Car/van: first 10,000 miles | 45p/mile |
| Car/van: over 10,000 miles | 25p/mile |
| Motorcycle | 24p/mile |
| Home office: 25-50 hrs/month | GBP 10/month |
| Home office: 51-100 hrs/month | GBP 18/month |
| Home office: 101+ hrs/month | GBP 26/month |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Unknown accounting basis | Cash basis (default from 2024/25) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown whether expense is capital or revenue | Capital (claim via AIA, not revenue expense) |
| Unknown expense category | Not deductible |
| Unknown entertainment purpose | Not deductible (entertainment is always blocked) |
| Unknown mixed-use proportion | 0% business |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year (6 April to 5 April) in CSV, PDF, or pasted text, plus confirmation of whether the trade uses cash basis or accruals.

**Recommended** -- all sales invoices, purchase invoices/receipts, mileage log, home office hours log, prior year SA103.

**Ideal** -- complete bookkeeping records, asset register, prior year losses memo, VAT return (if registered).

### Refusal Catalogue

**R-UK-SE-1 -- Partnerships.** "Partnership profits are computed on a separate partnership return (SA800) and allocated to partners via SA104. This skill covers sole traders only."

**R-UK-SE-2 -- LLP members.** "LLP members file SA104 (Partnership). Different rules apply. Out of scope."

**R-UK-SE-3 -- CIS subcontractors (construction).** "CIS has specific deduction and verification rules. While SA103 is used, CIS-specific guidance is out of scope for this skill."

**R-UK-SE-4 -- Non-resident traders.** "Non-resident sole traders have different UK tax obligations. Escalate."

**R-UK-SE-5 -- Overlap relief pre-reform.** "Complex overlap relief calculations from pre-2024/25 basis period rules require specialist computation. Escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | SA103F Box | Treatment | Notes |
|---|---|---|---|
| CLIENT INVOICE, [client name] PAYMENT, FEE PAYMENT | Box 9 (Turnover) | Business income | Core trading income |
| STRIPE PAYOUT, STRIPE TRANSFER | Box 9 | Business income | Match to underlying invoices |
| PAYPAL TRANSFER, PAYPAL PAYOUT | Box 9 | Business income | Match to underlying invoices |
| GOCARDLESS, BACS CREDIT [client] | Box 9 | Business income | Direct debit collection |
| WISE PAYOUT, WISE TRANSFER | Box 9 | Business income | International payment platform |
| HMRC REPAYMENT, TAX REFUND | EXCLUDE | Not trading income | Tax refund -- not taxable as trade income |
| INTEREST, SAVINGS INTEREST | EXCLUDE from SA103 | Savings income | Goes to SA100 savings section |
| DIVIDEND | EXCLUDE from SA103 | Dividend income | Goes to SA100 dividend section |
| GRANT, GOVERNMENT GRANT, BOUNCE BACK LOAN | Check | May be taxable | COVID grants generally taxable. Loan principal not income. |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Not income | Transfer between own accounts |

### 3.2 Expense Patterns (Debits on Bank Statement)

| Pattern | SA103F Box | Tier | Treatment |
|---|---|---|---|
| RENT, OFFICE RENT, SERVICED OFFICE, REGUS, WEWORK | Box 14 (Rent/rates/power) | T1 | Fully deductible if dedicated business premises |
| COUNCIL TAX (business premises) | Box 14 | T1 | Fully deductible for business premises |
| ELECTRICITY, GAS, BRITISH GAS, EDF, OCTOPUS | Box 14 | T2 | If home: proportional only. If business premises: fully deductible |
| BROADBAND, BT, VIRGIN MEDIA, SKY | Box 16 (Phone/office) | T2 | Business portion only for home broadband |
| MOBILE, VODAFONE, EE, THREE, O2 | Box 16 | T2 | Business portion only if personal phone |
| INSURANCE, PROFESSIONAL INDEMNITY, PI INSURANCE | Box 22 (Other) | T1 | Fully deductible if business insurance |
| SUBSCRIPTIONS, MEMBERSHIP, PROFESSIONAL BODY | Box 22 | T1 | Fully deductible if related to trade |
| ADOBE, MICROSOFT 365, SLACK, NOTION, FIGMA | Box 22 | T1 | Software subscriptions -- fully deductible |
| GOOGLE ADS, META ADS, FACEBOOK ADS, LINKEDIN ADS | Box 17 (Advertising) | T1 | Advertising -- fully deductible |
| RESTAURANT, CAFE, MEALS (client entertainment) | Box 17 | T1 | BLOCKED. Client entertainment is NOT deductible. |
| RESTAURANT, CAFE (business travel meal) | Box 13 (Travel) | T1 | Subsistence while on business travel: deductible |
| TRAINLINE, NATIONAL RAIL, TFL | Box 13 | T1 | Business travel -- fully deductible |
| UBER, BOLT, TAXI | Box 13 | T1/T2 | Deductible if business travel. Ask if personal. |
| FUEL, PETROL, DIESEL, BP, SHELL | Box 13 | T2 | If using actual costs: business % only. If simplified: use mileage rate instead. |
| CAR INSURANCE, MOT, SERVICE | Box 13 | T2 | If using mileage rate: NOT separately deductible. If actual costs: business % only. |
| PARKING, NCP | Box 13 | T1 | Business parking -- deductible even if using mileage rate |
| ACCOUNTANT, BOOKKEEPER, ACCOUNTING FEE | Box 20 (Professional fees) | T1 | Fully deductible |
| SOLICITOR, LEGAL FEE | Box 20 | T1 | Deductible if business-related |
| BANK CHARGES, CARD FEE | Box 18 (Bank charges) | T1 | Fully deductible for business account |
| STRIPE FEE, PAYPAL FEE, GOCARDLESS FEE | Box 18 | T1 | Transaction fees -- fully deductible |
| INTEREST (business loan) | Box 18 | T1 | Deductible. Cash basis: capped at GBP 500 interest. |
| HMRC, INCOME TAX, CLASS 4 NIC | EXCLUDE | Not deductible | Tax on profits is not a deductible expense |
| HMRC VAT PAYMENT | EXCLUDE from SA103 | Not a trade expense | VAT is separate (net figures on SA103 if registered) |
| PENSION, SIPP, SELF-INVESTED | EXCLUDE from SA103 | Not a trade expense | Pension relief claimed on SA100, not SA103 |
| SALARY, WAGES, PAYROLL | Box 12 (Staff costs) | T1 | Employee wages -- fully deductible |
| MATERIALS, SUPPLIES, STOCK | Box 10 (Cost of goods) | T1 | Fully deductible |
| LOAN REPAYMENT, MORTGAGE | EXCLUDE | Not deductible | Capital repayments are not expenses |
| DRAWINGS, PERSONAL | EXCLUDE | Not deductible | Personal drawings |
| AMAZON (check) | T2 -- ask | Could be business supplies or personal | Default: not deductible until confirmed |
| COMPUTER, LAPTOP, DELL, APPLE | Capital allowance (Box 13 AIA) | T1 | Capital item -- claim AIA (100% in year). Do NOT put in revenue expenses. |

### 3.3 SaaS Subscriptions (Common UK Patterns)

| Pattern | Treatment | Notes |
|---|---|---|
| XERO, QUICKBOOKS, FREEAGENT, SAGE | Box 22 -- fully deductible | Accounting software |
| CANVA, FIGMA, MIRO, NOTION | Box 22 -- fully deductible | Business tools |
| GITHUB, AWS, HEROKU, DIGITAL OCEAN | Box 22 -- fully deductible | Developer tools/hosting |
| ZOOM, GOOGLE WORKSPACE, MICROSOFT 365 | Box 22 -- fully deductible | Communication/productivity |
| SPOTIFY, NETFLIX, DISNEY+ | EXCLUDE | Personal entertainment -- not deductible |
| APPLE ONE, ICLOUD STORAGE | T2 -- ask | Could be personal or business |

### 3.4 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFER OWN ACCOUNT, SAVINGS | EXCLUDE | Internal movement |
| INVESTMENT, SHARES, ISA | EXCLUDE | Investment, not trade |
| RENT RECEIVED | EXCLUDE from SA103 | Property income -- SA105 |
| CHILD BENEFIT, UNIVERSAL CREDIT | EXCLUDE | Not trading income |
| CASH WITHDRAWAL, ATM | T2 -- ask | Default exclude. Ask what cash was for. |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Sole Trader (IT Freelancer)

**Input:** Turnover GBP 52,000. Actual expenses: office rent GBP 6,000, software GBP 1,200, accountant GBP 800, phone (50% business) GBP 600, train travel GBP 1,500, laptop GBP 1,300. Cash basis. 8,000 business miles (mileage rate).

**Computation:**
- Turnover: GBP 52,000
- Revenue expenses: 6,000 + 1,200 + 800 + 300 (50% of 600) + 1,500 = GBP 9,800
- Mileage: 8,000 x 45p = GBP 3,600
- Capital allowances (AIA): laptop GBP 1,300
- Total deductions: 9,800 + 3,600 + 1,300 = GBP 14,700
- Taxable profit: 52,000 - 14,700 = GBP 37,300
- Class 4 NIC: (37,300 - 12,570) x 6% = GBP 1,483.80

### Example 2 -- Trading Allowance vs Actual Expenses

**Input:** Side income GBP 4,000 from occasional consulting. Actual expenses GBP 700.

**Computation:**
- Option A (actual): 4,000 - 700 = GBP 3,300 profit
- Option B (trading allowance): 4,000 - 1,000 = GBP 3,000 profit
- Trading allowance is more beneficial. Use GBP 1,000 deduction.

### Example 3 -- Entertainment Blocked

**Input:** GBP 500 claimed for client dinner at restaurant.

**Classification:** NOT deductible. Client entertainment is blocked by ITTOIA 2005, s45. Remove from expenses. Staff entertainment (Christmas party, team meals) may be deductible -- but client-facing entertainment never is.

### Example 4 -- Home Office (Simplified vs Actual)

**Input:** Works from home 130 hours/month for 11 months. Alternatively, has a dedicated room (1 of 5 rooms). Annual household costs: rent GBP 12,000, utilities GBP 2,400, broadband GBP 480.

**Computation:**
- Simplified: 11 months x GBP 26 = GBP 286
- Actual: 1/5 of (12,000 + 2,400 + 480) = GBP 2,976
- Actual method is significantly more beneficial in this case.
- [T2] Flag: confirm dedicated room used exclusively for business during working hours.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Trading Income [T1]

**Legislation:** ITTOIA 2005, Part 2

All income from the trade is taxable. Cash basis (default from 2024/25): income recognised when received. Accruals: when earned.

### 5.2 Wholly and Exclusively Test [T1]

**Legislation:** ITTOIA 2005, s34

An expense is deductible only if incurred wholly and exclusively for the purposes of the trade. Mixed-use expenses: only the business element is deductible.

### 5.3 Capital Allowances [T1]

**Legislation:** CAA 2001

| Allowance | Rate | Eligible Assets |
|---|---|---|
| AIA | 100% | Most plant and machinery (NOT cars) |
| Main rate WDA | 18% reducing balance | Cars 1-50 g/km CO2, assets exceeding AIA |
| Special rate WDA | 6% reducing balance | Cars >50 g/km CO2, integral features, long-life assets |
| Zero-emission car FYA | 100% | New cars with 0 g/km CO2 |

Cars are NEVER eligible for AIA. Always use WDA pools or FYA (if zero-emission).

### 5.4 Loss Relief [T1]

| Basis | Available Reliefs |
|---|---|
| Cash basis | Carry forward only (no sideways, no carry-back) |
| Accruals | Carry forward, sideways (s64 ITA 2007), carry-back, early years (s72), terminal (s89) |

Sideways relief cap: greater of GBP 50,000 or 25% of adjusted total income.

### 5.5 Filing and Payment [T1]

| Item | Date |
|---|---|
| Online filing deadline | 31 January 2026 |
| Paper filing deadline | 31 October 2025 |
| Payment of tax + Class 4 NIC | 31 January 2026 |
| POA1 for 2025/26 | 31 January 2026 |
| POA2 for 2025/26 | 31 July 2026 |

### 5.6 Penalties [T1]

| Offence | Penalty |
|---|---|
| 1 day late filing | GBP 100 |
| 3 months late | GBP 10/day for 90 days (max GBP 900) |
| 6 months late | Greater of GBP 300 or 5% of tax due |
| 12 months late | Greater of GBP 300 or 5% of tax due (additional) |
| Late payment (30 days) | 5% of unpaid tax |
| Late payment (6 months) | Additional 5% |
| Late payment (12 months) | Additional 5% |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office [T2]

**Two methods:**

| Method | Deduction | Requirements |
|---|---|---|
| Simplified flat rate | GBP 10/18/26 per month by hours worked | Record hours monthly |
| Actual costs (proportional) | Room fraction of rent/mortgage interest, utilities, broadband, council tax, insurance | Dedicated workspace used exclusively for business |

Cannot claim both. Once chosen for a year, must use same method all year.

**Flag for reviewer:** Confirm workspace arrangement and hours/room proportion.

### 6.2 Motor Vehicle [T2]

| Method | How It Works | Lock-in |
|---|---|---|
| Mileage rate | 45p first 10k / 25p thereafter. No other car costs claimed. | Once chosen for a vehicle, cannot switch. |
| Actual costs | Fuel, insurance, repairs, road tax x business %. Plus capital allowances on purchase price. | Once chosen for a vehicle, cannot switch. |

Parking and tolls are deductible under EITHER method.

**Flag for reviewer:** Confirm method choice and business mileage/percentage.

### 6.3 Basis Period Apportionment [T2]

From 2024/25, all traders are on tax year basis. Non-31 March/5 April year-ends require apportionment from two sets of accounts. Transition profit from 2023/24 is spread over 5 years (20%/year, 2023/24 through 2027/28).

**Flag for reviewer:** Confirm apportionment calculation and transition profit instalment.

### 6.4 Loss Relief Election [T2]

Choice of loss relief has significant planning implications. Consider: marginal rates, cash vs accruals, first 4 years of trade, cessation.

**Flag for reviewer:** Confirm which relief(s) to claim.

---

## Section 7 -- Excel Working Paper Template

```
SA103 WORKING PAPER -- Tax Year 2024/25

A. TURNOVER
  A1. Total sales/revenue                         ___________

B. EXPENSES (SA103F boxes)
  B1. Cost of goods sold (Box 10)                  ___________
  B2. Staff costs (Box 12)                         ___________
  B3. Car/van/travel (Box 13)                      ___________
  B4. Rent/rates/power/insurance (Box 14)          ___________
  B5. Repairs and maintenance (Box 15)             ___________
  B6. Phone/fax/stationery/office (Box 16)         ___________
  B7. Advertising (Box 17)                         ___________
  B8. Bank charges/interest (Box 18)               ___________
  B9. Bad debts (Box 19)                           ___________
  B10. Professional fees (Box 20)                  ___________
  B11. Other expenses (Box 22)                     ___________
  B12. Total expenses (Box 23)                     ___________

C. NET PROFIT (A1 - B12)                           ___________

D. CAPITAL ALLOWANCES
  D1. AIA claims                                   ___________
  D2. WDA (main rate pool)                         ___________
  D3. WDA (special rate pool)                      ___________
  D4. Total capital allowances                     ___________

E. TAXABLE PROFIT (C - D4)                         ___________

F. CLASS 4 NIC
  F1. (E - 12,570) x 6% (up to 50,270)            ___________
  F2. (E - 50,270) x 2% (if applicable)           ___________
  F3. Total Class 4 NIC                            ___________

REVIEWER FLAGS:
  [ ] Cash basis or accruals confirmed?
  [ ] Mileage rate or actual costs for vehicle?
  [ ] Home office method confirmed?
  [ ] All entertainment removed?
  [ ] All T2 items flagged?
```

---

## Section 8 -- Bank Statement Reading Guide

### UK Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| Barclays, HSBC, Lloyds, NatWest | CSV, PDF | Date, Description, Amount, Balance |
| Monzo, Starling, Tide | CSV | Date, Name, Amount, Category, Notes |
| Revolut Business | CSV | Date started, Description, Amount, Currency |
| Wise Business | CSV | Date, Description, Amount, Currency |

### Key UK Banking Terms

| Term | Classification Hint |
|---|---|
| BACS | Bank transfer -- check direction |
| FPS / Faster Payment | Bank transfer |
| DD / Direct Debit | Regular outgoing -- likely expense |
| SO / Standing Order | Regular outgoing |
| Card Payment / POS | Expense |
| Interest | Savings income -- not trade income |
| Dividend | Not trade income |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer all onboarding questions:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all T2 items as "PENDING"
3. Apply conservative defaults (Section 1)
4. Generate working paper with flags
5. Present questions:

```
ONBOARDING QUESTIONS -- UK SELF-EMPLOYMENT
1. Cash basis or accruals basis?
2. Is your turnover above or below GBP 90,000? (determines SA103S vs SA103F)
3. Are you VAT registered? (figures should be net of VAT if so)
4. Vehicle: mileage rate or actual costs?
5. Home office: simplified flat rate or actual costs?
6. Any capital purchases this year? (computers, equipment, vehicles)
7. Any losses brought forward from prior years?
8. Do you have any other self-employments?
9. Accounting date (if not 31 March or 5 April)?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Trading income | ITTOIA 2005, Part 2 |
| Wholly and exclusively test | ITTOIA 2005, s34 |
| Entertainment block | ITTOIA 2005, s45 |
| Simplified expenses | ITTOIA 2005, ss 94D-94H |
| Trading allowance | ITTOIA 2005, s783A |
| Capital allowances | CAA 2001 |
| AIA | CAA 2001, ss 38A-38B |
| Cash basis | ITTOIA 2005, Part 2 Ch 3A |
| Loss relief | ITA 2007, ss 64-90 |
| Class 4 NIC | SSCBA 1992 |
| Basis period reform | Finance Act 2024, ss 7-16 |
| Filing/penalties | TMA 1970 |

---

## PROHIBITIONS

- NEVER allow business entertainment as a deductible expense
- NEVER allow accounting depreciation -- use capital allowances instead
- NEVER allow income tax or Class 4 NIC as deductible
- NEVER allow fines or penalties as deductible
- NEVER claim both trading allowance AND actual expenses
- NEVER claim AIA on cars -- cars are excluded from AIA
- NEVER claim full expensing for sole traders -- companies only
- NEVER claim sideways loss relief on cash basis
- NEVER include VAT-inclusive figures if VAT-registered
- NEVER separately claim fuel/insurance when using mileage rate
- NEVER compute profit without confirming cash or accruals basis
- NEVER present tax calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
