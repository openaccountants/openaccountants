---
name: uk-self-employment-sa103
description: Use this skill whenever asked about UK self-employment income for sole traders filing SA103S (short) or SA103F (full) as part of Self Assessment. Trigger on phrases like "self-employment income", "SA103", "trading income", "sole trader tax", "allowable expenses UK", "capital allowances UK", "trading allowance", "basis period", "tax year basis", "simplified expenses", "Class 4 NIC", "Class 2 abolished", "MTD ITSA", "Making Tax Digital", "April 2026 sole trader", "loss relief self-employed", or any question about computing self-employment profits for a UK sole trader. Covers trading income computation, allowable expenses, capital allowances (AIA, WDA, FYA), simplified expenses, the trading allowance, the completed basis period reform, the MTD ITSA three-phase rollout from April 2026, loss relief, and Class 4 NIC interaction (including the post-2024 rate cut and Class 2 abolition). ALWAYS read this skill before touching any UK self-employment work.
version: 3.0
jurisdiction: GB
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Power
review_status: current
depends_on:
  - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK Self Employment Sa103

## UK Self-Employment (SA103) -- Sole Trader Skill v3.0

**Three-year scope:** Prior 2024-25 | Current 2025-26 | From April 2026 (2026-27)

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **James Power** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Self-Employment SA103

- **SA103S (short form)** — Turnover below £90,000  _(HMRC guidance)_
- **Trading allowance** — £1,000  _(ITTOIA 2005)_
- **AIA (Annual Investment Allowance)** — £1,000,000  _(CAA 2001)_
- **Cash basis** — Default from 2024/25 (no upper limit)  _(Finance Act 2024)_
- **Below £12,570** — 0%  _(SSCBA 1992)_
- **£12,570 – £50,270** — 6%  _(SSCBA 1992)_
- **Above £50,270** — 2%  _(SSCBA 1992)_
- **Car/van: first 10,000 miles** — 45p/mile  _(ITTOIA s.94A)_
- **Car/van: over 10,000 miles** — 25p/mile  _(ITTOIA s.94A)_
- **Motorcycle** — 24p/mile  _(ITTOIA s.94A)_
- **Home office: 25-50 hrs/month** — £10/month  _(ITTOIA s.94B)_
- **Home office: 51-100 hrs/month** — £18/month  _(ITTOIA s.94B)_
- **Home office: 101+ hrs/month** — £26/month  _(ITTOIA s.94B)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Kingdom (England, Wales, Scotland, Northern Ireland) |
| Tax | Income Tax on trading profits + Class 4 NIC |
| Currency | GBP only |
| Current tax year | 6 April 2025 -- 5 April 2026 (2025-26) |
| Primary legislation | Income Tax (Trading and Other Income) Act 2005 (ITTOIA 2005); Capital Allowances Act 2001 (CAA 2001) |
| Supporting legislation | Finance Act 2024 (basis period reform completion, Class 2 abolition, Class 4 cut); Finance (No.2) Act 2023 (MTD ITSA powers); Social Security Contributions and Benefits Act 1992 |
| Tax authority | HM Revenue & Customs (HMRC) |
| Filing portal | HMRC Self Assessment Online (MTD ITSA quarterly portal from April 2026 for mandated traders) |
| Filing deadline (2025-26, online) | 31 January 2027 |
| Filing deadline (2025-26, paper) | 31 October 2026 |
| Contributor | Open Accountants Community |
| Validated by | Verified by James Power on 2026-06-03 |
| Skill version | 3.0 |

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
- Phase 1 mandation in April 2026 is based on income reported in the 2024-25 return (filed by 31 Jan 2026). HMRC will notify mandated traders during 2025-26.
- Quarterly updates: 5 Aug, 5 Nov, 5 Feb, 5 May (standard quarters). End-of-period statement + final declaration replaces the SA103 line items but the overall liability process continues.
- Penalty regime: points-based late submission penalties under FA 2021 Sch 24/25 apply once mandated.
- Below threshold or out-of-scope traders continue with annual SA103 as before.

### Key Thresholds -- 3-Year Comparison [T1]

**Key Thresholds 3-Year Comparison**

| Item | 2024-25 (Prior) | 2025-26 (Current) | 2026-27 (From April 2026) |
| --- | --- | --- | --- |
| SA103S vs SA103F cutoff | Turnover GBP 90,000 | Turnover GBP 90,000 | Turnover GBP 90,000 (MTD finalisation for mandated traders) |
| Trading allowance | GBP 1,000 (frozen) | GBP 1,000 (frozen) | GBP 1,000 (frozen) |
| AIA (Annual Investment Allowance) | GBP 1,000,000 | GBP 1,000,000 | GBP 1,000,000 |
| Cash basis | Default (no upper limit; basis period reform complete) | Default | Default (continues under MTD) |
| Accruals basis | By election | By election | By election |
| Personal allowance | GBP 12,570 (frozen) | GBP 12,570 (frozen) | GBP 12,570 (frozen) |
| Basic rate band | To GBP 50,270 | To GBP 50,270 | To GBP 50,270 |
| Class 4 LPL | GBP 12,570 | GBP 12,570 | GBP 12,570 |
| Class 4 UPL | GBP 50,270 | GBP 50,270 | GBP 50,270 |
| Class 4 main rate | 6% (cut from 9% on 6 Apr 2024) | 6% | 6% |
| Class 4 additional rate | 2% | 2% | 2% |
| Class 2 NIC | Abolished from 6 Apr 2024 (voluntary only when profit < SPT) | Voluntary only | Voluntary only |
| Class 2 voluntary weekly rate | GBP 3.45 | GBP 3.50 (illustrative; HMRC sets annually) | TBC |
| Small Profits Threshold (SPT, for voluntary Class 2 / NI credits) | GBP 6,725 | GBP 6,725 | GBP 6,725 |
| MTD ITSA mandate | Not yet | Notification year (HMRC writes to GBP 50k+ traders) | Phase 1 LIVE for gross income > GBP 50k |

### Class 4 NIC Rates -- Applies All 3 Years [T1]

Post-6-April-2024 rate cut (Finance Act 2024) is now embedded. No further rate changes announced through 2026-27.

**Class 4 NIC Rates**

| Band | Rate |
| --- | --- |
| Below GBP 12,570 | 0% |
| GBP 12,570 -- GBP 50,270 | 6% (main rate) |
| Above GBP 50,270 | 2% (additional rate) |

### Class 2 NIC -- Abolished but Optionally Voluntary [T1]

- **Compulsory Class 2 abolished** — Compulsory Class 2 ABOLISHED from 6 April 2024. Self-employed with profits at or above the Lower Profits Threshold (GBP 12,570) receive Class 2 NI credit treated as paid without payment (since 2022-23). No Class 2 box on the SA103 from 2024-25 onwards for these traders.
- **Voluntary Class 2 still available** — Voluntary Class 2 still available when profits are below the Small Profits Threshold (SPT) of GBP 6,725 and the trader wishes to protect State Pension and contributory benefit entitlement. Paid through Self Assessment.
- **Applicability** — Applies identically across 2024-25, 2025-26, and 2026-27.

### Simplified Expenses Rates -- Applies All 3 Years [T1]

(Frozen rates; HMRC has not announced changes.)

**Simplified Expenses Rates**

| Category | Rate |
| --- | --- |
| Car/van: first 10,000 miles | 45p/mile |
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

- **R-UK-SE-1 -- Partnerships** — Partnership profits are computed on a separate partnership return (SA800) and allocated to partners via SA104. This skill covers sole traders only.
- **R-UK-SE-2 -- LLP members** — LLP members file SA104 (Partnership). Different rules apply. Out of scope.
- **R-UK-SE-3 -- CIS subcontractors (construction)** — CIS has specific deduction and verification rules. While SA103 is used, CIS-specific guidance is out of scope for this skill.
- **R-UK-SE-4 -- Non-resident traders** — Non-resident sole traders have different UK tax obligations. Escalate.
- **R-UK-SE-5 -- Overlap relief pre-reform residue** — Basis period reform completed 5 April 2024. Any residual overlap relief carried into 2024-25 onwards (where not used in 2023-24 transition) is a specialist computation. Escalate.
- **R-UK-SE-6 -- MTD ITSA software configuration** — This skill explains MTD ITSA rules and timing. Selecting, configuring, or operating MTD-compatible software for quarterly submissions is out of scope.

## Section 3 -- Transaction Pattern Library

(Unchanged across the three years -- the box structure of SA103 carries through to MTD ITSA quarterly categories.)

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns**

| Pattern | SA103F Box | Treatment | Notes |
| --- | --- | --- | --- |
| CLIENT INVOICE, [client name] PAYMENT, FEE PAYMENT | Box 9 (Turnover) | Business income | Core trading income |
| STRIPE PAYOUT, STRIPE TRANSFER | Box 9 | Business income | Match to underlying invoices |
| PAYPAL TRANSFER, PAYPAL PAYOUT | Box 9 | Business income | Match to underlying invoices |
| GOCARDLESS, BACS CREDIT [client] | Box 9 | Business income | Direct debit collection |
| WISE PAYOUT, WISE TRANSFER | Box 9 | Business income | International payment platform |
| HMRC REPAYMENT, TAX REFUND | EXCLUDE | Not trading income | Tax refund -- not taxable as trade income |
| INTEREST, SAVINGS INTEREST | EXCLUDE from SA103 | Savings income | Goes to SA100 savings section |
| DIVIDEND | EXCLUDE from SA103 | Dividend income | Goes to SA100 dividend section |
| GRANT, GOVERNMENT GRANT, BOUNCE BACK LOAN | Check | May be taxable | Trade-related grants generally taxable. Loan principal not income. |
| INTERNAL TRANSFER, OWN ACCOUNT | EXCLUDE | Not income | Transfer between own accounts |

### 3.2 Expense Patterns (Debits on Bank Statement)

**Expense Patterns**

| Pattern | SA103F Box | Tier | Treatment |
| --- | --- | --- | --- |
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
| ACCOUNTANT, BOOKKEEPER, ACCOUNTING FEE | Box 20 (Professional fees) | T1 | Fully deductible (includes MTD software costs) |
| MTD SOFTWARE (XERO, FREEAGENT, QUICKBOOKS subscription) | Box 22 | T1 | Fully deductible -- becomes essentially mandatory for 2026-27 Phase 1 traders |
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

**SaaS Subscriptions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| XERO, QUICKBOOKS, FREEAGENT, SAGE | Box 22 -- fully deductible | Accounting software (MTD-compatible from April 2026) |
| CANVA, FIGMA, MIRO, NOTION | Box 22 -- fully deductible | Business tools |
| GITHUB, AWS, HEROKU, DIGITAL OCEAN | Box 22 -- fully deductible | Developer tools/hosting |
| ZOOM, GOOGLE WORKSPACE, MICROSOFT 365 | Box 22 -- fully deductible | Communication/productivity |
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
- Capital allowances (AIA): laptop GBP 1,300
- Total deductions: 9,800 + 3,600 + 1,300 = GBP 14,700
- Taxable profit: 52,000 - 14,700 = GBP 37,300
- Class 4 NIC: (37,300 - 12,570) x 6% = GBP 1,483.80
- Class 2: NONE (abolished; profit > GBP 12,570 gives credit-as-paid)
- **MTD ITSA flag:** 2024-25 turnover was GBP 48,000 (below GBP 50k) -- not in Phase 1 for 2026-27. Re-test annually.

### Example 1B -- Same Trader, 2026-27 (MTD Phase 1 Mandated)

**Year:** 2026-27. Same trader, but 2024-25 turnover was GBP 62,000 (above the GBP 50,000 Phase 1 threshold). HMRC notified trader during 2025-26.

**Mechanics now:**
- Trader uses MTD-compatible software (e.g., FreeAgent) and submits four quarterly updates:
  - Q1: 6 Apr - 5 Jul 2026 → due 5 Aug 2026
  - Q2: 6 Jul - 5 Oct 2026 → due 5 Nov 2026
  - Q3: 6 Oct 2026 - 5 Jan 2027 → due 5 Feb 2027
  - Q4: 6 Jan - 5 Apr 2027 → due 5 May 2027
- End-of-period statement (EOPS) and final declaration replace SA103 line items; tax computation, Class 4, and SA100 finalisation continue on the same timeline (31 Jan 2028 for 2026-27).
- Rates unchanged: 6% / 2% Class 4 bands; trading allowance GBP 1,000.
- Late submission point-based penalties under FA 2021 apply per missed quarterly update.

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

**Year:** 2025-26. Applies identically 2024-25 and 2026-27.

**Input:** Part-time sole trader profit GBP 4,200 (below SPT GBP 6,725). Wants to preserve State Pension qualifying year.

**Computation:**
- Class 4: GBP 0 (profit below GBP 12,570)
- Compulsory Class 2: GBP 0 (abolished 6 Apr 2024)
- Voluntary Class 2: ~52 x GBP 3.50 ≈ GBP 182 (illustrative weekly rate; check HMRC published rate for the year)
- Tick the voluntary Class 2 box on SA103. Paid through Self Assessment.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Trading Income [T1]

- **Trading income taxable / basis of recognition** — All income from the trade is taxable. Cash basis is the default from 2024-25 (basis period reform completed); accruals available by election. Income recognised when received (cash) or when earned (accruals).  _(ITTOIA 2005, Part 2)_

### 5.2 Wholly and Exclusively Test [T1]

- **Wholly and exclusively test** — An expense is deductible only if incurred wholly and exclusively for the purposes of the trade. Mixed-use expenses: only the business element is deductible.  _(ITTOIA 2005, s34)_

### 5.3 Capital Allowances [T1]

**Capital Allowances**  _(CAA 2001)_

| Allowance | Rate | Eligible Assets |
| --- | --- | --- |
| AIA | 100% (to GBP 1m) | Most plant and machinery (NOT cars) |
| Main rate WDA | 18% reducing balance | Cars 1-50 g/km CO2, assets exceeding AIA |
| Special rate WDA | 6% reducing balance | Cars >50 g/km CO2, integral features, long-life assets |
| Zero-emission car FYA | 100% | New cars with 0 g/km CO2 |

- **Cars and AIA** — Cars are NEVER eligible for AIA. Always use WDA pools or FYA (if zero-emission). Rates unchanged across 2024-25, 2025-26, 2026-27.  _(CAA 2001)_

### 5.4 Basis Period Reform -- COMPLETED [T1]

- **Basis period reform completed** — Basis period reform completed on 5 April 2024. From 2024-25 onwards, all sole traders are on the tax-year basis (6 April to 5 April). No more "current year basis" overlap relief computations for new SE work.  _(Finance Act 2022 (introduced); Finance Act 2024 (completion).)_
- **Transition profit spreading** — Transition profit (computed in 2023-24) is being spread across 5 years (20% per year, 2023-24 through 2027-28). The 2025-26 return includes the third 20% instalment; the 2026-27 return includes the fourth. Any unused overlap relief brought forward into 2023-24 was used or written off in the transition. Residual issues are R-UK-SE-5 (escalate).  _(Finance Act 2022 (introduced); Finance Act 2024 (completion).)_

### 5.5 Loss Relief [T1]

**Loss Relief**

| Basis | Available Reliefs |
| --- | --- |
| Cash basis | Carry forward only (no sideways, no carry-back) |
| Accruals | Carry forward, sideways (s64 ITA 2007), carry-back, early years (s72), terminal (s89) |

- **Sideways relief cap** — Sideways relief cap: greater of GBP 50,000 or 25% of adjusted total income. Unchanged across the three years.

### 5.6 Filing and Payment -- 3-Year Schedule [T1]

**Filing and Payment Schedule**

| Item | 2024-25 (Prior) | 2025-26 (Current) | 2026-27 (From April 2026) |
| --- | --- | --- | --- |
| Paper SA filing deadline | 31 October 2025 | 31 October 2026 | 31 October 2027 (or MTD final declaration via software if mandated) |
| Online SA filing deadline | 31 January 2026 | 31 January 2027 | 31 January 2028 |
| Balancing payment | 31 January 2026 | 31 January 2027 | 31 January 2028 |
| POA1 (current year) | 31 January 2026 | 31 January 2027 | 31 January 2028 |
| POA2 (current year) | 31 July 2026 | 31 July 2027 | 31 July 2028 |
| MTD quarterly updates | N/A | N/A (notification year for Phase 1) | Q1: 5 Aug 2026; Q2: 5 Nov 2026; Q3: 5 Feb 2027; Q4: 5 May 2027 |
| MTD EOPS + final declaration | N/A | N/A | 31 January 2028 |

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

- **MTD ITSA points-based penalty regime** — MTD ITSA points-based penalty regime (from 2026-27 for mandated traders): each missed quarterly update accrues 1 point; threshold (4 points for quarterly filers) triggers GBP 200 penalty per subsequent failure. Late payment under MTD uses the FA 2021 Sch 26 percentage regime.  _(FA 2021 Sch 26)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office [T2]

**Home Office Methods**

| Method | Deduction | Requirements |
| --- | --- | --- |
| Simplified flat rate | GBP 10/18/26 per month by hours worked | Record hours monthly |
| Actual costs (proportional) | Room fraction of rent/mortgage interest, utilities, broadband, council tax, insurance | Dedicated workspace used exclusively for business |

- **Lock-in rule** — Cannot claim both. Once chosen for a year, must use same method all year.

**Flag for reviewer:** Confirm workspace arrangement and hours/room proportion.

### 6.2 Motor Vehicle [T2]

**Motor Vehicle Methods**

| Method | How It Works | Lock-in |
| --- | --- | --- |
| Mileage rate | 45p first 10k / 25p thereafter. No other car costs claimed. | Once chosen for a vehicle, cannot switch. |
| Actual costs | Fuel, insurance, repairs, road tax x business %. Plus capital allowances on purchase price. | Once chosen for a vehicle, cannot switch. |

- **Parking and tolls** — Parking and tolls are deductible under EITHER method.

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

## Section 7 -- Excel Working Paper Template (2025-26)

```
SA103 WORKING PAPER -- Tax Year 2025-26

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

F. TRANSITION PROFIT INSTALMENT (if applicable)
  F1. 2025-26 third 20% instalment                ___________

G. CLASS 4 NIC (2025-26 rates: 6% / 2%)
  G1. (E + F1 capped at 50,270 - 12,570) x 6%      ___________
  G2. (E + F1 - 50,270) x 2% (if applicable)       ___________
  G3. Total Class 4 NIC                            ___________

H. CLASS 2 NIC (voluntary only)
  H1. Voluntary Class 2 if profit < SPT GBP 6,725  ___________

I. MTD ITSA STATUS (for 2026-27 planning)
  I1. 2024-25 gross income (turnover + property)   ___________
  I2. Above GBP 50,000? Phase 1 mandated 6 Apr 2026  Y / N

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
11. Profits below GBP 6,725 -- do you want to pay voluntary Class 2 for State Pension credit?
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
| Class 4 NIC (6%/2% post-Apr-2024) | SSCBA 1992, s15; National Insurance Contributions (Reduction in Rates) Act 2024 |
| Class 2 abolition (compulsory) | National Insurance Contributions (Reduction in Rates) Act 2024 |
| Basis period reform | Finance Act 2022 ss 6-7 and Sch 1; Finance Act 2024 |
| MTD ITSA powers | Finance (No.2) Act 2017, ss 60-62; Finance Act 2021; Income Tax (Digital Requirements) Regulations 2021 (as amended) |
| MTD ITSA penalty regime | Finance Act 2021, Schs 24-26 |
| Filing/penalties (annual SA) | TMA 1970 |

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
- NEVER apply pre-2024-25 "current year basis" rules -- basis period reform is complete; all SE traders are on tax-year basis
- NEVER charge compulsory Class 2 NIC for 2024-25 onwards -- it is abolished (voluntary only when profits < SPT)
- NEVER use the pre-April-2024 Class 4 main rate of 9% for 2024-25 onwards -- the rate is 6%
- NEVER assume a trader is outside MTD ITSA for 2026-27 without checking 2024-25 gross income against the GBP 50,000 Phase 1 threshold
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
