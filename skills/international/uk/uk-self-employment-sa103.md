---
name: uk-self-employment-sa103
description: Use this skill whenever asked about UK self-employment income for sole traders filing SA103S (short) or SA103F (full) as part of Self Assessment. Trigger on phrases like "self-employment income", "SA103", "trading income", "sole trader tax", "allowable expenses UK", "capital allowances UK", "trading allowance", "basis period", "tax year basis", "simplified expenses", "Class 4 NIC", "Class 2 abolished", "MTD ITSA", "Making Tax Digital", "April 2026 sole trader", "loss relief self-employed", or any question about computing self-employment profits for a UK sole trader. Covers trading income computation, allowable expenses, capital allowances (AIA, WDA, FYA), simplified expenses, the trading allowance, the completed basis period reform, the MTD ITSA three-phase rollout from April 2026, loss relief, and Class 4 NIC interaction (including the post-2024 rate cut and Class 2 abolition). ALWAYS read this skill before touching any UK self-employment work.
version: 3.2
jurisdiction: GB
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
verified_by: pending
source_checked: 2026-10-23
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Self Employment Sa103

## UK Self-Employment (SA103) -- Sole Trader Skill v3.2

**Three-year scope:** 2024-25 | 2025-26 | 2026-27 (working year, 6 April 2026 to 5 April 2027)

## Rates and thresholds, 2026/27

> Source-cited draft: not reviewed by an accountant.

### Self-employment, 2026/27

- **SA103S (short form)**: turnover below £90,000  _(SA103F 2026 form: "If your annual turnover was below £90,000, you may just put your total expenses in box 31")_
- **Trading allowance**: £1,000  _(ITTOIA 2005 s.783A)_
- **AIA (Annual Investment Allowance)**: £1,000,000  _(CAA 2001 s.51A)_
- **Main pool writing-down allowance**: 14% from 6 April 2026 (18% before); special rate pool 6%  _(Finance Act 2026 s.28; https://www.gov.uk/work-out-capital-allowances/rates-and-pools)_
- **Zero-emission car first-year allowance**: 100% for new cars bought before April 2027  _(Finance Act 2026 s.30)_
- **Main-rate first-year allowance**: 40% for new and unused main-rate plant or machinery bought on or after 1 January 2026; not cars, not second-hand, not special rate; open to sole traders (no company condition)  _(CAA 2001 ss.45U, 46 and 52, inserted by Finance Act 2026 s.29)_
- **Class 4 NIC**: 0% to £12,570; 6% from £12,570 to £50,270; 2% above  _(https://www.gov.uk/self-employed-national-insurance-rates)_
- **Class 2 NIC**: not payable; treated as paid if profits are £7,105 or more; voluntary £3.65 a week below that  _(same page)_
- **Simplified mileage, cars and goods vehicles**: 55p a mile for the first 10,000 business miles in 2026-27 (45p before 6 April 2026); 25p after  _(https://www.gov.uk/simpler-income-tax-simplified-expenses/print)_
- **Simplified mileage, motorcycles**: 24p a mile  _(same page)_
- **Working from home flat rate**: £10 / £18 / £26 a month for 25-50 / 51-100 / 101+ hours  _(same page)_
- **Making Tax Digital for Income Tax**: from 6 April 2026 if 2024/25 qualifying income was over £50,000; from 6 April 2027 over £30,000; from 6 April 2028 over £20,000  _(https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Kingdom (England, Wales, Scotland, Northern Ireland) |
| Tax | Income Tax on trading profits + Class 4 NIC |
| Currency | GBP only |
| Current tax year | 6 April 2026 -- 5 April 2027 (2026-27) |
| Primary legislation | Income Tax (Trading and Other Income) Act 2005 (ITTOIA 2005); Capital Allowances Act 2001 (CAA 2001) |
| Supporting legislation | Finance Act 2022 s.7 and Sch 1 (basis period reform); National Insurance Contributions (Reduction in Rates) Act 2023, s.3 (Class 2 no longer payable from 6 April 2024); National Insurance Contributions (Reduction in Rates) Act 2024, s.1(3) (Class 4 main rate 9% to 6% from 6 April 2024; s.1(4) treats the 2023 Act s.2 cut to 8% as never having had effect); Finance (No.2) Act 2017 ss.60-62 (MTD powers); Finance Act 2026 ss.28-30 (capital allowances); Social Security Contributions and Benefits Act 1992 s.15 |
| Tax authority | HM Revenue & Customs (HMRC) |
| Filing portal | HMRC Self Assessment Online (MTD ITSA quarterly portal from April 2026 for mandated traders) |
| Filing deadline (2026-27, online) | 31 January 2028 |
| Filing deadline (2026-27, paper) | 31 October 2027 |
| Status | Source-cited draft: not reviewed by an accountant |
| Skill version | 3.2 |

### MTD ITSA Timeline -- The Biggest 2026-27 Change [T1]

Making Tax Digital for Income Tax Self Assessment (MTD ITSA) phases in mandatory quarterly digital updates for sole traders and landlords. Three thresholds, three start dates -- assessed on gross income (turnover + gross rental income), NOT net profit.

**MTD ITSA Timeline**

| Phase | Mandation date | Gross income threshold | Test year (look-back) | What changes |
| --- | --- | --- | --- | --- |
| Phase 1 | 6 April 2026 | > GBP 50,000 | Assessed on 2024-25 SA103/SA105 | Mandatory quarterly updates + year-end finalisation; MTD-compatible software required |
| Phase 2 | 6 April 2027 | > GBP 30,000 | Assessed on 2025-26 SA103/SA105 | Same rules extend to more traders |
| Phase 3 | 6 April 2028 | > GBP 20,000 | Assessed on 2026-27 SA103/SA105 | Smaller traders brought in |

**Critical points:**
- Threshold is gross income (turnover), NOT profit. A trader with GBP 60,000 turnover and GBP 5,000 profit IS in Phase 1.
- Combined gross income across self-employment AND property is aggregated for the threshold test.
- Phase 1 mandation in April 2026 is based on income reported in the 2024-25 return (filed by 31 Jan 2026). HMRC wrote to traders over the threshold.
- Quarterly updates: 7 Aug, 7 Nov, 7 Feb, 7 May (standard quarters). End-of-period statement + final declaration replaces the SA103 line items but the overall liability process continues.
- Penalty regime: points-based late submission penalties (FA 2021 Sch 24) and percentage late payment penalties (FA 2021 Sch 26) apply once mandated. There are no penalties for missing a quarterly update deadline for 2026-27; late tax returns still get points.
- Below threshold or out-of-scope traders continue with annual SA103 as before.

### Key Thresholds -- 3-Year Comparison [T1]

**Key Thresholds 3-Year Comparison**  _(https://www.gov.uk/income-tax-rates)_

| Item | 2024-25 (Prior) | 2025-26 (Current) | 2026-27 (From April 2026) |
| --- | --- | --- | --- |
| SA103S vs SA103F cutoff | Turnover GBP 90,000 | Turnover GBP 90,000 | Turnover GBP 90,000 (MTD finalisation for mandated traders) |
| Trading allowance | GBP 1,000 (frozen) | GBP 1,000 (frozen) | GBP 1,000 (frozen) |
| AIA (Annual Investment Allowance) | GBP 1,000,000 | GBP 1,000,000 | GBP 1,000,000 |
| Cash basis | Default (no upper limit; basis period reform complete) | Default | Default (continues under MTD) |
| Accruals basis | By election | By election | By election |
| Personal allowance | GBP 12,570 (frozen) | GBP 12,570 (frozen) | GBP 12,570 (frozen) |
| Basic rate band (not Scotland; Scottish bands differ) | To GBP 50,270 | To GBP 50,270 | To GBP 50,270 |
| Class 4 LPL | GBP 12,570 | GBP 12,570 | GBP 12,570 |
| Class 4 UPL | GBP 50,270 | GBP 50,270 | GBP 50,270 |
| Class 4 main rate | 6% (cut from 9% on 6 Apr 2024) | 6% | 6% |
| Class 4 additional rate | 2% | 2% | 2% |
| Class 2 NIC | Abolished from 6 Apr 2024 (voluntary only when profit < SPT) | Voluntary only | Voluntary only |
| Class 2 voluntary weekly rate | GBP 3.45 | GBP 3.50 | GBP 3.65 |
| Small Profits Threshold (SPT, for voluntary Class 2 / NI credits) | GBP 6,725 | GBP 6,845 | GBP 7,105 |
| MTD ITSA mandate | Not yet | Notification year (HMRC writes to GBP 50k+ traders) | Phase 1 LIVE for gross income > GBP 50k |

### Class 4 NIC Rates -- Applies All 3 Years [T1]

The main rate fell from 9% to 6% from 6 April 2024 (National Insurance Contributions (Reduction in Rates) Act 2024 s.1(3)). The 2023 Act s.2 cut to 8% never took effect: s.1(4) of the 2024 Act treats it as never having had effect. The rates are unchanged for 2026-27 (GOV.UK, read 2026-10-23).

**Class 4 NIC Rates**

| Band | Rate |
| --- | --- |
| Below GBP 12,570 | 0% |
| GBP 12,570 -- GBP 50,270 | 6% (main rate) |
| Above GBP 50,270 | 2% (additional rate) |

### Class 2 NIC -- Abolished but Optionally Voluntary [T1]

- **Compulsory Class 2 abolished**: Compulsory Class 2 ABOLISHED from 6 April 2024. Self-employed with profits at or above the Small Profits Threshold (GBP 7,105 for 2026 to 2027) receive Class 2 NI credit treated as paid without payment (since 2022-23). No Class 2 box on the SA103 from 2024-25 onwards for these traders.  _(https://www.gov.uk/self-employed-national-insurance-rates)_
- **Voluntary Class 2 still available**: Voluntary Class 2 still available when profits are below the Small Profits Threshold (SPT) (GBP 6,725 for 2024-25, GBP 6,845 for 2025-26, GBP 7,105 for 2026-27) and the trader wishes to protect State Pension and contributory benefit entitlement. Paid through Self Assessment.  _(https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions/rates-and-allowances-national-insurance-contributions)_
- **Applicability**: Applies identically across 2024-25, 2025-26, and 2026-27.

### Simplified Expenses Rates -- Applies All 3 Years [T1]

(Car/van rate for the first 10,000 miles rises from 45p to 55p for 2026-2027; other rates unchanged.)

**Simplified Expenses Rates**  _(https://www.gov.uk/simpler-income-tax-simplified-expenses/print)_

| Category | Rate |
| --- | --- |
| Car/van: first 10,000 miles | 45p/mile (before 6 April 2026); 55p/mile (2026-2027) |
| Car/van: over 10,000 miles | 25p/mile |
| Motorcycle | 24p/mile |
| Home office: 25-50 hrs/month | GBP 10/month |
| Home office: 51-100 hrs/month | GBP 18/month |
| Home office: 101+ hrs/month | GBP 26/month |

### Conservative Defaults [T1]

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown accounting basis | Cash basis (default from 2024-25 onwards) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown whether expense is capital or revenue | Capital (claim via AIA, not revenue expense) |
| Unknown expense category | Not deductible |
| Unknown entertainment purpose | Not deductible (entertainment is always blocked) |
| Unknown mixed-use proportion | 0% business |
| Unknown MTD ITSA status (2026-27 prep) | Check 2024-25 gross income > GBP 50k -- if yes, assume Phase 1 mandated |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year (6 April to 5 April) in CSV, PDF, or pasted text, plus confirmation of whether the trade uses cash basis or accruals.

**Recommended** -- all sales invoices, purchase invoices/receipts, mileage log, home office hours log, prior year SA103. For 2026-27: confirmation of MTD ITSA mandation status and software in use.

**Ideal** -- complete bookkeeping records, asset register, prior year losses memo, VAT return (if registered), MTD-compatible software access (Xero, FreeAgent, QuickBooks, etc.) for mandated traders.

### Refusal Catalogue

- **R-UK-SE-1 -- Partnerships**: Partnership profits are computed on a separate partnership return (SA800) and allocated to partners via SA104. This skill covers sole traders only.
- **R-UK-SE-2 -- LLP members**: LLP members file SA104 (Partnership). Different rules apply. Out of scope.
- **R-UK-SE-3 -- CIS subcontractors (construction)**: CIS has specific deduction and verification rules. While SA103 is used, CIS-specific guidance is out of scope for this skill.
- **R-UK-SE-4 -- Non-resident traders**: Non-resident sole traders have different UK tax obligations. Escalate.
- **R-UK-SE-5 -- Overlap relief pre-reform residue**: Basis period reform completed 5 April 2024. Any residual overlap relief carried into 2024-25 onwards (where not used in 2023-24 transition) is a specialist computation. Escalate.
- **R-UK-SE-6 -- MTD ITSA software configuration**: This skill explains MTD ITSA rules and timing. Selecting, configuring, or operating MTD-compatible software for quarterly submissions is out of scope.

## Section 3 -- Transaction Pattern Library

(Unchanged across the three years -- the box structure of SA103 carries through to MTD ITSA quarterly categories.)

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns**  _(https://assets.publishing.service.gov.uk/media/69c26565cfa346b9d4704b35/SA103F_Notes_2026.pdf)_

| Pattern | SA103F Box | Treatment | Notes |
| --- | --- | --- | --- |
| CLIENT INVOICE, [client name] PAYMENT, FEE PAYMENT | Box 15 (Turnover) | Business income | Core trading income |
| STRIPE PAYOUT, STRIPE TRANSFER | Box 15 | Business income | Match to underlying invoices; gross up for fees |
| PAYPAL TRANSFER, PAYPAL PAYOUT | Box 15 | Business income | Match to underlying invoices |
| GOCARDLESS, BACS CREDIT [client] | Box 15 | Business income | Direct debit collection |
| WISE PAYOUT, WISE TRANSFER | Box 15 | Business income | International payment platform |
| HMRC REPAYMENT, TAX REFUND | EXCLUDE | Not trading income | Tax refund -- not taxable as trade income |
| INTEREST, SAVINGS INTEREST | EXCLUDE from SA103 | Savings income | Goes to SA100 savings section |
| DIVIDEND | EXCLUDE from SA103 | Dividend income | Goes to SA100 dividend section |
| GRANT, GOVERNMENT GRANT, BOUNCE BACK LOAN | Box 16 if taxable | Check | Trade-related grants are business income. Loan principal is not income. |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Not income | Transfer between own accounts |

### 3.2 Expense Patterns (Debits on Bank Statement)

**Expense Patterns**  _(https://www.gov.uk/government/publications/expanding-the-income-tax-cash-basis-for-self-employed-individuals-and-partnerships/expanding-the-cash-basis)_

| Pattern | SA103F Box | Tier | Treatment |
| --- | --- | --- | --- |
| RENT, OFFICE RENT, SERVICED OFFICE, REGUS, WEWORK | Box 21 (Rent, rates, power and insurance) | T1 | Fully deductible if dedicated business premises |
| BUSINESS RATES, WATER RATES (business premises) | Box 21 | T1 | Fully deductible for business premises |
| ELECTRICITY, GAS, BRITISH GAS, EDF, OCTOPUS | Box 21 | T2 | If home: business proportion only (or the flat rate). If business premises: fully deductible |
| BROADBAND, BT, VIRGIN MEDIA, SKY | Box 23 (Phone, stationery, office) | T2 | Business portion only for home broadband |
| MOBILE, VODAFONE, EE, THREE, O2 | Box 23 | T2 | Business portion only if personal phone |
| PROPERTY INSURANCE (business premises) | Box 21 | T1 | Fully deductible if business premises |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Box 28 (Professional fees and indemnity insurance) | T1 | Fully deductible |
| SUBSCRIPTIONS, MEMBERSHIP, PROFESSIONAL BODY, TRADE JOURNALS | Box 30 (Other business expenses) | T1 | Fully deductible if related to trade |
| ADOBE, MICROSOFT 365, SLACK, NOTION, FIGMA | Box 23 | T1 | Computer software -- fully deductible |
| GOOGLE ADS, META ADS, FACEBOOK ADS, LINKEDIN ADS | Box 24 (Advertising) | T1 | Advertising -- fully deductible |
| RESTAURANT, CAFE, MEALS (client entertainment) | Box 24, and the same amount in box 39 | T1 | BLOCKED. Client entertainment is NOT deductible. |
| HOTEL, MEALS (overnight business trip) | Box 20 (Car, van and travel) | T1 | Hotel and meals on overnight business trips: deductible |
| TRAINLINE, NATIONAL RAIL, TFL | Box 20 | T1 | Business travel -- fully deductible |
| UBER, BOLT, TAXI | Box 20 | T1/T2 | Deductible if business travel. Ask if personal. |
| FUEL, PETROL, DIESEL, BP, SHELL | Box 20 | T2 | If using actual costs: business % only. If simplified: use mileage rate instead. |
| CAR INSURANCE, MOT, SERVICE | Box 20 | T2 | If using mileage rate: NOT separately deductible. If actual costs: business % only. |
| PARKING, NCP | Box 20 | T1 | Business parking -- deductible even if using mileage rate |
| ACCOUNTANT, BOOKKEEPER, ACCOUNTING FEE | Box 28 (Accountancy, legal and other professional fees) | T1 | Fully deductible |
| MTD SOFTWARE (XERO, FREEAGENT, QUICKBOOKS subscription) | Box 23 | T1 | Fully deductible -- needed for 2026-27 MTD traders |
| SOLICITOR, LEGAL FEE | Box 28 | T1 | Deductible if business-related (not legal costs of buying property or large equipment) |
| BANK CHARGES, CARD FEE | Box 26 (Bank, credit card and other financial charges) | T1 | Fully deductible for business account |
| STRIPE FEE, PAYPAL FEE, GOCARDLESS FEE | Box 26 | T1 | Transaction fees -- fully deductible |
| INTEREST (business loan) | Box 25 (Interest on bank and other loans) | T1 | Deductible. Cash basis: no cap from 2024 to 2025 (the old £500 interest restriction was removed). |
| HMRC, INCOME TAX, CLASS 4 NIC | EXCLUDE | Not deductible | Tax on profits is not a deductible expense |
| HMRC VAT PAYMENT | EXCLUDE from SA103 | Not a trade expense | VAT is separate (net figures on SA103 if registered) |
| PENSION, SIPP, SELF-INVESTED | EXCLUDE from SA103 | Not a trade expense | Pension relief claimed on SA100, not SA103 |
| SALARY, WAGES, PAYROLL | Box 19 (Staff costs) | T1 | Employee wages -- fully deductible |
| MATERIALS, SUPPLIES, STOCK | Box 17 (Cost of goods) | T1 | Fully deductible |
| LOAN REPAYMENT, MORTGAGE | EXCLUDE | Not deductible | Capital repayments are not expenses |
| DRAWINGS, PERSONAL | EXCLUDE | Not deductible | Personal drawings |
| AMAZON (check) | T2 -- ask | Could be business supplies or personal | Default: not deductible until confirmed |
| COMPUTER, LAPTOP, DELL, APPLE | Cash basis: allowable expense. Accruals: Box 49 AIA | T1 | Cash basis (the default): deduct the cost as a normal allowable expense, not a capital allowance. Accruals basis: capital item, claim AIA (100% in year), not a revenue expense. |

### 3.3 SaaS Subscriptions (Common UK Patterns)

**SaaS Subscriptions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| XERO, QUICKBOOKS, FREEAGENT, SAGE | Box 23 -- fully deductible | Accounting software (MTD-compatible from April 2026) |
| CANVA, FIGMA, MIRO, NOTION | Box 23 -- fully deductible | Business tools |
| GITHUB, AWS, HEROKU, DIGITAL OCEAN | Box 23 -- fully deductible (or Box 30) | Developer tools/hosting |
| ZOOM, GOOGLE WORKSPACE, MICROSOFT 365 | Box 23 -- fully deductible | Communication/productivity |
| SPOTIFY, NETFLIX, DISNEY+ | EXCLUDE | Personal entertainment -- not deductible |
| APPLE ONE, ICLOUD STORAGE | T2 -- ask | Could be personal or business |

### 3.4 Internal Transfers and Exclusions

**Internal Transfers and Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER OWN ACCOUNT, SAVINGS | EXCLUDE | Internal movement |
| INVESTMENT, SHARES, ISA | EXCLUDE | Investment, not trade |
| RENT RECEIVED | EXCLUDE from SA103 | Property income -- SA105 (aggregates with SE for MTD threshold) |
| CHILD BENEFIT, UNIVERSAL CREDIT | EXCLUDE | Not trading income |
| CASH WITHDRAWAL, ATM | T2 -- ask | Default exclude. Ask what cash was for. |

## Section 4 -- Worked Examples

### Example 1 -- Standard Sole Trader (IT Freelancer), 2025-26

**Year:** 2025-26 (current). Tax-year basis (basis period reform complete).

**Input:** Turnover GBP 52,000. Actual expenses: office rent GBP 6,000, software (incl. Xero) GBP 1,200, accountant GBP 800, phone (50% business) GBP 600, train travel GBP 1,500, laptop GBP 1,300. Cash basis. 8,000 business miles (mileage rate).

**Computation:**
- Turnover: GBP 52,000
- Revenue expenses: 6,000 + 1,200 + 800 + 300 (50% of 600) + 1,500 = GBP 9,800
- Mileage: 8,000 x 45p = GBP 3,600
- Laptop: GBP 1,300, deducted as an allowable expense (on the cash basis, equipment other than cars is an expense, not a capital allowance)
- Total deductions: 9,800 + 3,600 + 1,300 = GBP 14,700
- Taxable profit: 52,000 - 14,700 = GBP 37,300
- Class 4 NIC: (37,300 - 12,570) x 6% = GBP 1,483.80
- Class 2: NONE (not payable; profit of GBP 6,845 or more gives credit-as-paid)
- **MTD ITSA flag:** 2024-25 turnover was GBP 48,000 (below GBP 50k) -- not in Phase 1 for 2026-27. Re-test annually.

```oa-check
name: IT freelancer, turnover 52,000, cash basis (2025-26)
inputs:
  turnover: 52000
  revenue_expenses: 9800
  miles: 8000
  laptop: 1300
steps:
  - mileage: miles * 0.45
  - profit: turnover - revenue_expenses - mileage - laptop
  - class4: (min(profit, 50270) - 12570) * 0.06
expected:
  mileage: 3600.00
  profit: 37300.00
  class4: 1483.80
```

### Example 1B -- Same Trader, 2026-27 (MTD Phase 1 Mandated)

**Year:** 2026-27. Same trader, but 2024-25 turnover was GBP 62,000 (above the GBP 50,000 Phase 1 threshold). HMRC notified trader during 2025-26.

**Mechanics now:**
- Trader uses MTD-compatible software (e.g., FreeAgent) and submits four quarterly updates:
  - Q1: 6 Apr - 5 Jul 2026 → due 7 Aug 2026
  - Q2: 6 Jul - 5 Oct 2026 → due 7 Nov 2026
  - Q3: 6 Oct 2026 - 5 Jan 2027 → due 7 Feb 2027
  - Q4: 6 Jan - 5 Apr 2027 → due 7 May 2027
- A tax return submitted through MTD software replaces SA103 line items; tax computation, Class 4, and SA100 finalisation continue on the same timeline (31 Jan 2028 for 2026-27).
- Rates unchanged: 6% / 2% Class 4 bands; trading allowance GBP 1,000.
- Late submission point-based penalties under FA 2021 apply per missed quarterly update after the 2026 to 2027 tax year. HMRC will not apply penalty points for late quarterly updates during the 2026 to 2027 tax year (late tax returns still attract points).

**Computation for 2026-27** (same turnover, expenses, mileage and laptop as Example 1; trader lives in England):
- Mileage: 8,000 x 55p = GBP 4,400 (the 2026-27 rate)
- Taxable profit: 52,000 - 9,800 - 4,400 - 1,300 = GBP 36,500
- Income tax: (36,500 - 12,570) x 20% = GBP 4,786.00
- Class 4 NIC: (36,500 - 12,570) x 6% = GBP 1,435.80
- Class 2: none (profit above the GBP 7,105 small profits threshold, so treated as paid)

```oa-check
name: Same freelancer in 2026-27 with 55p mileage
inputs:
  turnover: 52000
  revenue_expenses: 9800
  miles: 8000
  laptop: 1300
  personal_allowance: 12570
steps:
  - mileage: miles * 0.55
  - profit: turnover - revenue_expenses - mileage - laptop
  - income_tax: (profit - personal_allowance) * 0.20
  - class4: (min(profit, 50270) - 12570) * 0.06
expected:
  mileage: 4400.00
  profit: 36500.00
  income_tax: 4786.00
  class4: 1435.80
```

### Example 2 -- Trading Allowance vs Actual Expenses

(Applies identically in 2024-25, 2025-26, and 2026-27 -- allowance frozen at GBP 1,000.)

**Input:** Side income GBP 4,000 from occasional consulting. Actual expenses GBP 700.

**Computation:**
- Option A (actual): 4,000 - 700 = GBP 3,300 profit
- Option B (trading allowance): 4,000 - 1,000 = GBP 3,000 profit
- Trading allowance is more beneficial. Use GBP 1,000 deduction.
- MTD: gross income GBP 4,000 is below all phase thresholds -- not mandated.

### Example 3 -- Entertainment Blocked

(Unchanged across years.)

**Input:** GBP 500 claimed for client dinner at restaurant.

**Classification:** NOT deductible. Client entertainment is blocked by ITTOIA 2005, s45. Remove from expenses. Staff entertainment (Christmas party, team meals) may be deductible -- but client-facing entertainment never is.

### Example 4 -- Home Office (Simplified vs Actual)

(Unchanged across years.)

**Input:** Works from home 130 hours/month for 11 months. Alternatively, has a dedicated room (1 of 5 rooms). Annual household costs: rent GBP 12,000, utilities GBP 2,400, broadband GBP 480.

**Computation:**
- Simplified: 11 months x GBP 26 = GBP 286
- Actual: 1/5 of (12,000 + 2,400 + 480) = GBP 2,976
- Actual method is significantly more beneficial in this case.
- [T2] Flag: confirm dedicated room used exclusively for business during working hours.

### Example 5 -- Voluntary Class 2 (Low Profits, Pension Credit)

**Year:** 2026-27.

**Input:** Part-time sole trader profit GBP 4,200 (below the 2026-27 SPT of GBP 7,105). Wants to preserve State Pension qualifying year.

**Computation:**
- Class 4: GBP 0 (profit below GBP 12,570)
- Compulsory Class 2: GBP 0 (no longer payable from 6 Apr 2024)
- Voluntary Class 2: 52 x GBP 3.65 = GBP 189.80 (2026-27 weekly rate)
- Tick the voluntary Class 2 box on SA103. Paid through Self Assessment.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Trading Income [T1]

- **Trading income taxable / basis of recognition**: All income from the trade is taxable. Cash basis is the default from 2024-25 (basis period reform completed); accruals available by election. Income recognised when received (cash) or when earned (accruals).  _(ITTOIA 2005, Part 2)_

### 5.2 Wholly and Exclusively Test [T1]

- **Wholly and exclusively test**: An expense is deductible only if incurred wholly and exclusively for the purposes of the trade. Mixed-use expenses: only the business element is deductible.  _(ITTOIA 2005, s34)_

### 5.3 Capital Allowances [T1]

**Capital Allowances**  _([CAA 2001](https://www.gov.uk/work-out-capital-allowances/rates-and-pools))_

| Allowance | Rate | Eligible Assets |
| --- | --- | --- |
| AIA (box 49) | 100% (to GBP 1m) | Most plant and machinery (NOT cars) |
| Main rate WDA (box 50) | 14% reducing balance from 6 April 2026 (18% before) | Cars 1-50 g/km CO2, assets exceeding AIA |
| Special rate WDA (box 51) | 6% reducing balance | Cars >50 g/km CO2, integral features, long-life assets |
| Zero-emission car FYA (box 52.1) | 100% | New cars with 0 g/km CO2 bought before April 2027 (Finance Act 2026 s.30) |

- **Cars and AIA**: Cars are NEVER eligible for AIA. Always use WDA pools or FYA (if zero-emission). Main rate WDA changed from 18% to 14% on 6 April 2026 (2026-27); special rate 6% unchanged.  _([CAA 2001](https://www.gov.uk/work-out-capital-allowances/rates-and-pools))_

### 5.4 Basis Period Reform -- COMPLETED [T1]

- **Basis period reform completed**: Basis period reform completed on 5 April 2024. From 2024-25 onwards, all sole traders are on the tax-year basis (6 April to 5 April). No more "current year basis" overlap relief computations for new SE work.  _(Finance Act 2022 s.7 and Sch 1.)_
- **Transition profit spreading**: Transition profit (computed in 2023-24) is spread across 5 years (20% per year, 2023-24 through 2027-28) unless the trader elects to bring more in. The 2025-26 return includes the third 20% instalment; the 2026-27 return includes the fourth. Any unused overlap relief brought forward into 2023-24 was used in the transition. Residual issues are R-UK-SE-5 (escalate).  _(Finance Act 2022 Sch 1.)_

### 5.5 Loss Relief [T1]

**Loss Relief**  _(https://www.gov.uk/government/publications/expanding-the-income-tax-cash-basis-for-self-employed-individuals-and-partnerships/expanding-the-cash-basis)_

| Basis | Available Reliefs |
| --- | --- |
| Cash basis | From 2024 to 2025: same as accruals (carry forward, sideways, carry-back) |
| Accruals | Carry forward, sideways (s64 ITA 2007), carry-back, early years (s72), terminal (s89) |

- **Sideways relief cap**: Sideways relief cap: greater of GBP 50,000 or 25% of adjusted total income. Unchanged across the three years.

### 5.6 Filing and Payment -- 3-Year Schedule [T1]

**Filing and Payment Schedule**  _(https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates)_

| Item | 2024-25 (Prior) | 2025-26 (Current) | 2026-27 (From April 2026) |
| --- | --- | --- | --- |
| Paper SA filing deadline | 31 October 2025 | 31 October 2026 | 31 October 2027 (or MTD final declaration via software if mandated) |
| Online SA filing deadline | 31 January 2026 | 31 January 2027 | 31 January 2028 |
| Balancing payment | 31 January 2026 | 31 January 2027 | 31 January 2028 |
| 1st payment on account for the year | 31 January 2025 | 31 January 2026 | 31 January 2027 |
| 2nd payment on account for the year | 31 July 2025 | 31 July 2026 | 31 July 2027 |
| MTD quarterly updates | N/A | N/A (notification year for Phase 1) | Q1: 7 Aug 2026; Q2: 7 Nov 2026; Q3: 7 Feb 2027; Q4: 7 May 2027 |
| MTD tax return (via MTD software) | N/A | N/A | 31 January 2028 |

### 5.7 Penalties [T1]

**Penalties**

| Offence | Penalty |
| --- | --- |
| 1 day late filing | GBP 100 |
| 3 months late | GBP 10/day for 90 days (max GBP 900) |
| 6 months late | Greater of GBP 300 or 5% of tax due |
| 12 months late | Greater of GBP 300 or 5% of tax due (additional) |
| Late payment (30 days) | 5% of unpaid tax |
| Late payment (6 months) | Additional 5% |
| Late payment (12 months) | Additional 5% |

- **MTD ITSA points-based penalty regime**: MTD ITSA points-based penalty regime (for mandated traders; HMRC will not apply penalty points for late quarterly updates during the 2026 to 2027 tax year): each missed quarterly update accrues 1 point; threshold (4 points for quarterly filers) triggers GBP 200 penalty per subsequent failure. Late payment under MTD uses the FA 2021 Sch 26 percentage regime: for 2026-27, nothing up to 15 days late; 3% of the tax owed at day 15 (none at this point in the first year); a further 3% at day 30; then 10% a year from day 31. For 2027-28 the two charges rise to 4% each.  _([GOV.UK penalties for MTD for Income Tax](https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax))_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office [T2]

**Home Office Methods**

| Method | Deduction | Requirements |
| --- | --- | --- |
| Simplified flat rate | GBP 10/18/26 per month by hours worked | Record hours monthly |
| Actual costs (proportional) | Room fraction of rent/mortgage interest, utilities, broadband, council tax, insurance | Dedicated workspace used exclusively for business |

- **Lock-in rule**: Cannot claim both. Once chosen for a year, must use same method all year.

**Flag for reviewer:** Confirm workspace arrangement and hours/room proportion.

### 6.2 Motor Vehicle [T2]

**Motor Vehicle Methods**  _(https://www.gov.uk/simpler-income-tax-simplified-expenses/print)_

| Method | How It Works | Lock-in |
| --- | --- | --- |
| Mileage rate | 45p first 10k (55p from 2026-2027) / 25p thereafter. No other car costs claimed. | Once chosen for a vehicle, cannot switch. |
| Actual costs | Fuel, insurance, repairs, road tax x business %. Plus capital allowances on purchase price. | Once chosen for a vehicle, cannot switch. |

- **Parking and tolls**: Parking and tolls are deductible under EITHER method.

**Flag for reviewer:** Confirm method choice and business mileage/percentage.

### 6.3 Basis Period Transition Profit Instalment [T2]

For 2025-26: third 20% instalment of any transition profit computed in 2023-24.
For 2026-27: fourth 20% instalment.
For 2027-28 (out of scope here but flag forward): fifth and final instalment.

**Flag for reviewer:** Confirm transition profit running total and instalment amount, and consider acceleration election where beneficial.

### 6.4 Loss Relief Election [T2]

Choice of loss relief has significant planning implications. Consider: marginal rates, cash vs accruals, first 4 years of trade, cessation.

**Flag for reviewer:** Confirm which relief(s) to claim.

### 6.5 MTD ITSA Mandation Status [T2 -- New for 2025-26 / 2026-27]

For any client whose 2024-25 gross income (turnover plus gross rental income) approaches or exceeds GBP 50,000:

- Confirm whether HMRC has issued a mandation notice during 2025-26.
- Confirm MTD-compatible software selection and digital records compliance from 6 April 2026.
- Plan the quarterly cadence and assign internal review checkpoints.

For 2026-27 returns: if the client crosses the GBP 30,000 line in 2025-26 reporting, Phase 2 mandation kicks in from 6 April 2027 -- prepare in advance.

**Flag for reviewer:** Confirm mandation status, software choice, and quarterly update calendar.

## Section 7 -- Excel Working Paper Template (2026-27)

```
SA103 WORKING PAPER -- Tax Year 2026-27

A. TURNOVER
  A1. Total sales/revenue                         ___________

B. EXPENSES (SA103F boxes)
  B1. Cost of goods sold (Box 17)                  ___________
  B2. Staff costs (Box 19)                         ___________
  B3. Car/van/travel (Box 20)                      ___________
  B4. Rent/rates/power/insurance (Box 21)          ___________
  B5. Repairs and maintenance (Box 22)             ___________
  B6. Phone/fax/stationery/office (Box 23)         ___________
  B7. Advertising (Box 24)                         ___________
  B8. Bank charges/interest (Boxes 25-26)               ___________
  B9. Bad debts (Box 27)                           ___________
  B10. Professional fees (Box 28)                  ___________
  B11. Other expenses (Box 30)                     ___________
  B12. Total expenses (Box 31)                     ___________

C. NET PROFIT (A1 - B12)                           ___________

D. CAPITAL ALLOWANCES
  D1. AIA claims                                   ___________
  D2. WDA (main rate pool, 14%)                    ___________
  D3. WDA (special rate pool)                      ___________
  D4. Total capital allowances                     ___________

E. TAXABLE PROFIT (C - D4)                         ___________

F. TRANSITION PROFIT INSTALMENT (if applicable)
  F1. 2026-27 fourth 20% instalment               ___________

G. CLASS 4 NIC (2026-27 rates: 6% / 2%)
  G1. (E + F1 capped at 50,270 - 12,570) x 6%      ___________
  G2. (E + F1 - 50,270) x 2% (if applicable)       ___________
  G3. Total Class 4 NIC                            ___________

H. CLASS 2 NIC (voluntary only)
  H1. Voluntary Class 2 if profit < SPT GBP 7,105 (GBP 3.65/week)  ___________

I. MTD ITSA STATUS
  I1. 2024-25 qualifying income (turnover + gross property income)   ___________
  I2. Above GBP 50,000? In MTD from 6 Apr 2026      Y / N
  I3. 2025-26 qualifying income above GBP 30,000? In MTD from 6 Apr 2027  Y / N

REVIEWER FLAGS:
  [ ] Cash basis or accruals confirmed?
  [ ] Mileage rate or actual costs for vehicle?
  [ ] Home office method confirmed?
  [ ] All entertainment removed?
  [ ] Transition profit instalment correctly stated?
  [ ] MTD ITSA mandation status confirmed?
  [ ] Voluntary Class 2 election considered if profit < SPT?
  [ ] All T2 items flagged?
```

## Section 8 -- Bank Statement Reading Guide

### UK Bank Statement Formats

**UK Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| Barclays, HSBC, Lloyds, NatWest | CSV, PDF | Date, Description, Amount, Balance |
| Monzo, Starling, Tide | CSV | Date, Name, Amount, Category, Notes |
| Revolut Business | CSV | Date started, Description, Amount, Currency |
| Wise Business | CSV | Date, Description, Amount, Currency |

### Key UK Banking Terms

**Key UK Banking Terms**

| Term | Classification Hint |
| --- | --- |
| BACS | Bank transfer -- check direction |
| FPS / Faster Payment | Bank transfer |
| DD / Direct Debit | Regular outgoing -- likely expense |
| SO / Standing Order | Regular outgoing |
| Card Payment / POS | Expense |
| Interest | Savings income -- not trade income |
| Dividend | Not trade income |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer all onboarding questions:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all T2 items as "PENDING"
3. Apply conservative defaults (Section 1)
4. Generate working paper with flags
5. Present questions:

```
ONBOARDING QUESTIONS -- UK SELF-EMPLOYMENT
1. Cash basis or accruals basis? (Cash is default from 2024-25)
2. Is your turnover above or below GBP 90,000? (determines SA103S vs SA103F)
3. Are you VAT registered? (figures should be net of VAT if so)
4. Vehicle: mileage rate or actual costs?
5. Home office: simplified flat rate or actual costs?
6. Any capital purchases this year? (computers, equipment, vehicles)
7. Any losses brought forward from prior years?
8. Do you have any other self-employments or rental property? (counts toward MTD threshold)
9. What was your 2024-25 gross income (turnover + gross rents)? (determines 2026-27 MTD Phase 1)
10. Have you received an HMRC MTD ITSA mandation notice?
11. Profits below the SPT (GBP 6,845 for 2025-26; GBP 7,105 for 2026-27) -- do you want to pay voluntary Class 2 for State Pension credit?
12. Any transition profit instalments still running from basis period reform?
```

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| Trading income | ITTOIA 2005, Part 2 |
| Wholly and exclusively test | ITTOIA 2005, s34 |
| Entertainment block | ITTOIA 2005, s45 |
| Simplified expenses | ITTOIA 2005, ss 94D-94H |
| Trading allowance | ITTOIA 2005, s783A |
| Capital allowances | CAA 2001 |
| AIA | CAA 2001, ss 38A-38B |
| Cash basis (default from 2024-25) | ITTOIA 2005, Part 2 Ch 3A as amended by FA 2024 |
| Loss relief | ITA 2007, ss 64-90 |
| Class 4 NIC (6%/2% from 6 Apr 2024) | SSCBA 1992, s15; National Insurance Contributions (Reduction in Rates) Act 2024 s.1(3) (9% to 6%) and s.1(4) (2023 Act s.2 treated as never having had effect): https://www.legislation.gov.uk/ukpga/2024/5/section/1 |
| Class 2 abolition (compulsory) | National Insurance Contributions (Reduction in Rates) Act 2023, s.3 (in force 6 April 2024): https://www.legislation.gov.uk/ukpga/2023/57/section/3 |
| Basis period reform | Finance Act 2022 s.7 and Sch 1 |
| Capital allowances 2026 changes | Finance Act 2026 ss.28-30: https://www.legislation.gov.uk/ukpga/2026/11/contents |
| MTD ITSA powers | Finance (No.2) Act 2017, ss 60-62; Finance Act 2021; Income Tax (Digital Requirements) Regulations 2021 (as amended) |
| MTD ITSA penalty regime | Finance Act 2021, Sch 24 (late submission) and Sch 26 (late payment) |
| Filing/penalties (annual SA) | TMA 1970 |

## PROHIBITIONS

- NEVER allow business entertainment as a deductible expense
- NEVER allow accounting depreciation -- use capital allowances instead
- NEVER allow income tax or Class 4 NIC as deductible
- NEVER allow fines or penalties as deductible
- NEVER claim both trading allowance AND actual expenses
- NEVER claim AIA on cars -- cars are excluded from AIA
- NEVER claim full expensing for sole traders -- companies only (the 40% main-rate first-year allowance under CAA 2001 s.45U is not limited to companies)
- NEVER claim sideways loss relief on cash basis for years before 2024 to 2025 (the restriction was removed from 2024 to 2025)
- NEVER include VAT-inclusive figures if VAT-registered
- NEVER separately claim fuel/insurance when using mileage rate
- NEVER compute profit without confirming cash or accruals basis
- NEVER apply pre-2024-25 "current year basis" rules -- basis period reform is complete; all SE traders are on tax-year basis
- NEVER charge compulsory Class 2 NIC for 2024-25 onwards -- it is abolished (voluntary only when profits < SPT)
- NEVER use the pre-April-2024 Class 4 main rate of 9% for 2024-25 onwards -- the rate is 6%
- NEVER assume a trader is outside MTD ITSA for 2026-27 without checking 2024-25 gross income against the GBP 50,000 Phase 1 threshold
- NEVER present tax calculations as definitive -- always label as estimated

## Sources

| Source | URL | Read on |
|---|---|---|
| NIC (Reduction in Rates) Act 2023 s.2 (superseded, never had effect) | https://www.legislation.gov.uk/ukpga/2023/57/section/2 | 2026-10-23 |
| NIC (Reduction in Rates) Act 2023 contents (s.3 Class 2) | https://www.legislation.gov.uk/ukpga/2023/57/contents | 2026-10-23 |
| NIC (Reduction in Rates) Act 2024 s.1 (Class 4 9% to 6%) | https://www.legislation.gov.uk/ukpga/2024/5/section/1 | 2026-10-23 |
| Finance Act 2026 s.28 (main pool 18% to 14%) | https://www.legislation.gov.uk/ukpga/2026/11/section/28 | 2026-10-23 |
| Finance Act 2026 s.29 (40% first-year allowance, CAA 2001 s.45U) | https://www.legislation.gov.uk/ukpga/2026/11/section/29 | 2026-10-23 |
| GOV.UK, Cash basis (equipment as an expense) | https://www.gov.uk/simpler-income-tax-cash-basis | 2026-10-23 |
| Finance Act 2026 contents (ss.28-30 capital allowances) | https://www.legislation.gov.uk/ukpga/2026/11/contents | 2026-10-23 |
| Finance Act 2026 s.30 (zero-emission car FYA to 2027) | https://www.legislation.gov.uk/ukpga/2026/11/section/30 | 2026-10-23 |
| GOV.UK, Self-employed National Insurance rates | https://www.gov.uk/self-employed-national-insurance-rates | 2026-10-23 |
| GOV.UK, Simplified expenses (55p from 2026-27) | https://www.gov.uk/simpler-income-tax-simplified-expenses/print | 2026-10-23 |
| GOV.UK, Capital allowances rates and pools (14%) | https://www.gov.uk/work-out-capital-allowances/rates-and-pools | 2026-10-23 |
| GOV.UK, First-year allowances | https://www.gov.uk/capital-allowances/first-year-allowances | 2026-10-23 |
| SA103F 2026 form (box numbers) | https://assets.publishing.service.gov.uk/media/69c2635b13101e9908704b36/SA103F_2026.pdf | 2026-10-23 |
| SA103F 2026 notes (what goes in each box) | https://assets.publishing.service.gov.uk/media/69c26565cfa346b9d4704b35/SA103F_Notes_2026.pdf | 2026-10-23 |
| GOV.UK, Find out if and when you need to use MTD for Income Tax | https://www.gov.uk/guidance/find-out-if-and-when-you-need-to-use-making-tax-digital-for-income-tax | 2026-10-23 |
| GOV.UK, Send quarterly updates | https://www.gov.uk/guidance/use-making-tax-digital-for-income-tax/send-quarterly-updates | 2026-10-23 |
| GOV.UK, Penalties for MTD for Income Tax | https://www.gov.uk/guidance/penalties-for-making-tax-digital-for-income-tax | 2026-10-23 |

Not yet confirmed: which SA103F box takes the 40% main-rate first-year allowance; the 2026-27 SA103F form (the box numbers above are from the 2025-26 form, SA103F 2026, and its box 50 still says 18%).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
