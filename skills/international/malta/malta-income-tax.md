---
name: malta-income-tax
description: Use this skill whenever asked about Malta income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "TA24", "income tax return", "allowable deductions", "capital allowances", "provisional tax", "TA22 regime", "chargeable income", "tax credits", "self-employed tax Malta", or any question about filing or computing income tax for a self-employed or part-time self-employed client. Also trigger when preparing or reviewing a TA24 or TA22 return, computing deductible expenses, or advising on provisional tax instalments. This skill covers tax rates (single/married/parent), TA24 box structure, allowable deductions, capital allowances, provisional tax, TA22 regime, penalties, and interaction with VAT and SSC. ALWAYS read this skill before touching any income tax work.
---

# Malta Income Tax — Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Malta |
| Jurisdiction Code | MT |
| Primary Legislation | Income Tax Act, Chapter 123 |
| Supporting Legislation | Income Tax Management Act (Chapter 372); ITA Article 4C (TA22); ITA Article 14 (deductions); ITA Article 16 + 6th Schedule (capital allowances); ITMA Articles 44, 51, 52, 52A (penalties) |
| Tax Authority | Commissioner for Revenue (CFR) / MTCA, Malta |
| Filing Portal | MTCA e-Services |
| Contributor | Michael Cutajar, CPA (Warrant No. 125122), ACCA |
| Validated By | Michael Cutajar |
| Validation Date | March 2026 |
| Skill Version | 1.0 |
| Accora Integration | `generate_provisional_tax_installments()`, `provisional_tax_payments` table, Box 20 SSC deduction in `tax-return-service.ts` |
| Confidence Coverage | Tier 1: rate table application, box structure, capital allowance rates, provisional tax schedule, TA22 eligibility, penalty rates. Tier 2: mixed-use expense apportionment, home office deductions, motor vehicle business %, first-year provisional tax. Tier 3: group structures, non-resident income, complex capital disposals. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Warranted accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Marital status** [T1] -- single, married, or single parent. Determines which rate table applies.
2. **Employment status** [T1] -- fully self-employed (TA24) or employed + side income (TA22 eligible)
3. **Gross self-employment income** [T1] -- total invoiced/received in the year
4. **VAT registration type** [T1] -- Article 10 or Article 11 (affects how VAT is treated in P&L)
5. **Business expenses** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items)
6. **Capital assets acquired in the year** [T1] -- type, cost, date first used in business
7. **SSC paid in the year** [T1] -- Class 2 amount paid (goes to Box 20)
8. **Prior year tax liability** [T1] -- for provisional tax calculation. First year = no provisional tax.
9. **Other income** [T1] -- employment income, rental income, dividends, interest (Box 4)

**If marital status is unknown, STOP. Do not apply a rate table. Marital status is mandatory.**

---

## Step 1: Determine Applicable Rate Table [T1]

**Legislation:** Income Tax Act, Chapter 123, Tax Rate Schedule (2026)

### Single Rates

| Taxable Income (EUR) | Rate | Notes |
|---------------------|------|-------|
| 0 -- 9,100 | 0% | |
| 9,101 -- 14,500 | 15% | Cumulative tax at top of band: EUR 810 |
| 14,501 -- 19,500 | 25% | Cumulative tax at top of band: EUR 2,060 |
| 19,501 -- 60,000 | 25% | Cumulative tax at top of band: EUR 12,185 |
| 60,001+ | 35% | |

### Married Rates (joint computation)

| Taxable Income (EUR) | Rate | Notes |
|---------------------|------|-------|
| 0 -- 12,700 | 0% | |
| 12,701 -- 21,200 | 15% | Cumulative tax at top of band: EUR 1,275 |
| 21,201 -- 28,700 | 25% | Cumulative tax at top of band: EUR 3,150 |
| 28,701 -- 60,000 | 25% | Cumulative tax at top of band: EUR 10,975 |
| 60,001+ | 35% | |

### Parent Rates (single parent maintaining a child)

| Taxable Income (EUR) | Rate | Notes |
|---------------------|------|-------|
| 0 -- 10,500 | 0% | |
| 10,501 -- 15,800 | 15% | Cumulative tax at top of band: EUR 795 |
| 15,801 -- 21,200 | 25% | Cumulative tax at top of band: EUR 2,145 |
| 21,201 -- 60,000 | 25% | Cumulative tax at top of band: EUR 11,845 |
| 60,001+ | 35% | |

**Note (2026):** The first 0% band was increased by EUR 500 for all categories as part of the 2026 budget measures.

**Malta does not have a separate personal allowance -- the 0% band IS the personal allowance.**

---

## Step 2: TA24 Box Structure [T1]

**Legislation:** Income Tax Act Chapter 123; MTCA TA24 form guidance

| Box | Description | How to Populate |
|-----|-------------|-----------------|
| Box 1 | Gross income from self-employment | Total invoiced/received in the year |
| Box 2 | Less: Allowable deductions | Business expenses passing wholly and exclusively test |
| Box 3 | Net profit/loss | Box 1 minus Box 2 |
| Box 4 | Other income | Employment, rental, dividends, interest |
| Box 5 | Total income | Box 3 plus Box 4 |
| Box 15 | Capital allowances | Depreciation per 6th Schedule rates |
| Box 20 | SSC Class 2 | Amount actually paid in the tax year |
| Box 25 | Total deductions | Sum of all deduction boxes including Box 15 and Box 20 |
| Box 30 | Chargeable income | Box 5 minus Box 25 |
| Box 35 | Tax liability | Applied from rate table to Box 30 |
| Box 36 | Less: Provisional tax paid | Sum of 3 instalments paid during year |
| Box 37 | Less: Tax credits | Personal reliefs, green credits, disability credits |
| Box 40 | Tax due / refund | Box 35 minus Box 36 minus Box 37 |

**NEVER compute Box 35 using Claude -- pass chargeable income to the deterministic engine to apply the rate table.**

---

## Step 3: Allowable Deductions -- The Wholly and Exclusively Test [T1/T2]

**Legislation:** Income Tax Act, Article 14

### The Test [T1]
An expense is deductible only if incurred **wholly and exclusively** in the production of income. Mixed-use expenses must be apportioned. The apportionment method must be reasonable and documented.

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated) | T1 | Fully deductible |
| Professional insurance (PI) | T1 | Fully deductible |
| Accountancy fees | T1 | Fully deductible |
| Legal fees (business-related) | T1 | Fully deductible |
| Office supplies / stationery | T1 | Fully deductible |
| Software subscriptions (under EUR 1,160) | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Training / CPD related to business | T1 | Fully deductible |
| Trade subscriptions (MIA, ACCA, MIA etc.) | T1 | Fully deductible |
| Bad debts (genuinely irrecoverable, previously declared as income) | T2 | Flag for reviewer -- confirm write-off criteria met |
| SSC Class 2 | T1 | Deductible -- Box 20 |
| Utilities (home office) | T2 | Proportional only -- see home office rules |
| Phone / mobile | T2 | Business use portion only -- client to confirm % |
| Motor vehicle expenses | T2 | Business use portion only -- mileage log required |
| Travel (flights, hotels for business) | T1 | Fully deductible if wholly business purpose |
| Home office rent / mortgage interest | T2 | Proportional -- see home office rules |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Entertainment (client meals, events) | Blocked under Article 14 -- same block as VAT |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income cannot be deducted against income |
| Capital expenditure | Goes through capital allowances (Box 15), not Box 2 |
| Drawings / personal withdrawals | Not an expense |
| Personal car insurance (unapportioned) | Personal -- apportion business % only |

### Home Office Rules [T2]

**Legislation:** Income Tax Act, Article 14

- Calculate the proportion of home used for business: dedicated room(s) as percentage of total rooms or floor area
- Apply that percentage to: rent or mortgage interest, electricity, water, internet, maintenance
- Must be a dedicated workspace -- a dual-use room (kitchen table, living room) does not qualify
- Client must document the calculation and retain it for 6 years
- [T2] Flag for reviewer: confirm room count, floor area basis, and that workspace is genuinely dedicated

### Motor Vehicle Rules [T2]

- Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible
- Client must maintain a mileage log (business trips vs total mileage)
- [T2] Flag for reviewer: confirm business percentage claimed is reasonable and documented

---

## Step 4: Capital Allowances [T1]

**Legislation:** Income Tax Act, Article 16; 6th Schedule

### Depreciation Rates (Straight-Line on Cost)

| Asset Type | Annual Rate |
|-----------|-------------|
| Computer hardware | 25% |
| Computer software | 25% |
| Motor vehicles | 20% |
| Plant and machinery | 20% |
| Office equipment | 20% |
| Air conditioning | 20% |
| Furniture and fittings | 10% |
| Commercial buildings | 2% |
| Industrial buildings | 2% |

### Rules [T1]

- Depreciation starts in the year the asset is **first used** in the business
- Calculated on **cost price** -- straight-line, NOT reducing balance
- Claimed in **Box 15** of the TA24
- Motor vehicles: only the business-use proportion is claimable [T2]
- Low-value assets (under approximately EUR 700): some practitioners expense immediately -- [T2] flag for reviewer to confirm treatment

### Asset Disposal [T2]

- Sale proceeds minus written-down value = balancing charge (taxable) or balancing allowance (deductible)
- Flag for reviewer: confirm disposal proceeds and written-down value before computing

### Capital Allowances vs VAT Capital Goods -- Important Distinction [T1]

| System | Threshold | Purpose |
|--------|-----------|---------|
| VAT Capital Goods Scheme | EUR 1,160 gross | Determines VAT Box 30 treatment |
| Income Tax Capital Allowances | No threshold | ALL business assets depreciated |

A EUR 500 printer: depreciated for income tax (25% x EUR 500 = EUR 125/year) but does NOT go to VAT Box 30 (below EUR 1,160 threshold). These are entirely separate systems.

---

## Step 5: Provisional Tax [T1]

**Legislation:** Income Tax Management Act, Chapter 372

### Instalment Schedule

| Instalment | Percentage of Prior Year Tax | Deadline |
|-----------|------------------------------|----------|
| 1st | 20% | 30 April |
| 2nd | 30% | 31 August |
| 3rd | 50% | 21 December |

### Rules [T1]

- Always based on **prior year's final tax liability** -- not current year estimates
- First year of self-employment: no provisional tax due (no prior year)
- Second year: based on first year actual tax
- Provisional tax paid enters Box 36 of the TA24

### Reduced Rate (First 3 Years) [T2]

New self-employed persons may benefit from reduced provisional tax in their first 3 years. Conditions apply and availability should be confirmed with MTCA. Flag for reviewer.

**Accora integration:** `generate_provisional_tax_installments()` function, `provisional_tax_payments` table.

---

## Step 6: TA22 Regime -- Part-Time Self-Employment [T1]

**Legislation:** Income Tax Act, Article 4C

### Eligibility [T1]

| Condition | Requirement |
|-----------|-------------|
| Employment status | Must be in full-time employment with Class 1 SSC being paid |
| Net self-employment profit | Must not exceed EUR 12,000 |
| SSC | No additional Class 2 -- Class 1 from employment covers all |
| VAT | Can be Article 11 if under EUR 35,000 turnover |

### How It Works [T1]

1. Client is full-time employed (Class 1 SSC paid by employer)
2. Client has side self-employment income
3. File a TA22 instead of including self-employment income on TA24
4. Tax on self-employment net profit = flat 10%
5. No progressive rates applied -- employment income and self-employment income are taxed separately

### TA22 vs TA24 Decision [T1/T2]

- If net self-employment profit is under EUR 12,000 AND client is full-time employed: TA22 is almost always more favourable (flat 10% vs progressive rates)
- If net profit exceeds EUR 12,000: excess is taxed at normal TA24 progressive rates
- [T2] Flag for reviewer to confirm TA22 eligibility and whether flat 10% is genuinely more favourable given the client's total income profile

---

## Step 7: Interaction with VAT [T1]

**Legislation:** Income Tax Act, Article 14; VAT Act Chapter 406

| Scenario | Income Tax Treatment |
|----------|---------------------|
| VAT collected on sales (Article 10) | NOT income -- it is a liability to government. Exclude from Box 1. |
| Input VAT recovered (Article 10) | NOT an expense -- it is reclaimable. Exclude from Box 2. |
| Input VAT blocked/non-deductible (Article 10) | IS an expense -- adds to the cost of the purchase. Include in Box 2. |
| Article 11 client -- all VAT paid on purchases | IS an expense -- cannot reclaim any input VAT. Gross amount is the cost. |
| Foreign VAT (non-reclaimable) | IS an expense -- full gross including foreign VAT is the cost. |

**Key rule:** For Article 10 clients, only blocked or non-deductible VAT appears in the P&L. Reclaimable VAT is a balance sheet item only. For Article 11 clients, all VAT paid on purchases is a P&L expense.

---

## Step 8: Filing Deadlines [T1]

**Legislation:** Income Tax Management Act, Chapter 372

| Filing / Payment | Deadline |
|-----------------|----------|
| TA24 (self-employed annual return) | 30 June of following year |
| TA22 (part-time self-employment) | 30 June of following year |
| Provisional tax 1st instalment | 30 April |
| Provisional tax 2nd instalment | 31 August |
| Provisional tax 3rd instalment | 21 December |
| Balance of tax due | With the TA24, by 30 June |

---

## Step 9: Penalties [T1]

**Legislation:** ITMA Articles 44(1), 44(2A), 51, 52, 52A

| Offence | Penalty |
|---------|---------|
| Late filing of TA24 | EUR 50 + EUR 10/month (maximum EUR 500) |
| Late payment surcharge | 1% per month on unpaid tax -- UNCAPPED |
| Late payment interest | 0.6% per month -- capped at original tax amount |
| Combined late payment | 1.6% per month total |
| Incorrect return | Up to EUR 2,000 |
| Fraud / evasion | Up to EUR 5,000 + imprisonment |
| Out-of-court settlement | Available since 2025 under Article 52A |

**WARNING:** The 1%/month late payment surcharge is uncapped and can exceed the original tax owed. Combined with interest: 1.6%/month is severe. Any arrears situation must be escalated to a warranted accountant immediately.

---

## Step 10: Record Keeping [T1]

**Legislation:** Income Tax Act; Income Tax Management Act

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 6 years from end of the year of assessment |
| What to keep | All sales invoices, purchase invoices, bank statements, receipts, contracts, asset register |
| Format | Paper or digital (MTCA accepts digital) |
| Invoice requirements | Supplier name, VAT number, date, amount, description |
| Capital asset register | Date acquired, cost, depreciation claimed each year, written-down value |

---

## Step 11: Edge Case Registry

### EC1 -- VAT collected included in income [T1]
**Situation:** Article 10 client invoices EUR 1,180 (EUR 1,000 net + EUR 180 VAT). Client treats EUR 1,180 as gross income.
**Resolution:** Box 1 must show EUR 1,000 only. The EUR 180 VAT collected is a liability to CFR, not income. Correct before filing.

### EC2 -- Article 11 client expense treatment [T1]
**Situation:** Article 11 client purchases office supplies for EUR 59 (gross including 18% VAT = EUR 50 net).
**Resolution:** Full EUR 59 is the deductible expense. Article 11 clients cannot reclaim input VAT, so the gross amount is the cost.

### EC3 -- Entertainment expenses [T1]
**Situation:** Client takes a client to dinner and wants to deduct it.
**Resolution:** NOT deductible. Entertainment is blocked under Article 14, same as the VAT block. No partial deduction. No apportionment. Full block.

### EC4 -- Motor vehicle, mixed use [T2]
**Situation:** Client uses their personal car 60% for business, 40% personal. Annual running costs EUR 4,000. Car cost EUR 18,000.
**Resolution:** Deductible expenses: EUR 4,000 x 60% = EUR 2,400 running costs. Capital allowance: EUR 18,000 x 20% x 60% = EUR 2,160. [T2] Flag for reviewer: confirm business percentage is documented with mileage log and is reasonable.

### EC5 -- Capital item expensed directly [T1]
**Situation:** Client buys a laptop for EUR 1,500 and puts it in Box 2 as an expense.
**Resolution:** INCORRECT. Capital items must go through capital allowances (Box 15), not Box 2. EUR 1,500 laptop: 25% per year = EUR 375 per year in Box 15. Remove from Box 2.

### EC6 -- First year, no provisional tax [T1]
**Situation:** Client started self-employment in 2025. Now preparing 2025 TA24 in 2026.
**Resolution:** No provisional tax was due during 2025 (no prior year). Box 36 = EUR 0. Full tax liability is paid with the return by 30 June 2026. From 2026 onwards provisional tax applies based on 2025 final liability.

### EC7 -- SSC deductibility timing [T1]
**Situation:** Client paid 2025 SSC quarterly instalments during 2025. Preparing 2025 TA24.
**Resolution:** SSC paid during 2025 goes in Box 20 of the 2025 TA24. SSC paid = deduction in the same year it is paid.

### EC8 -- TA22 profit exceeds EUR 12,000 [T1]
**Situation:** TA22 client earns EUR 15,000 net from side business.
**Resolution:** First EUR 12,000 taxed at 10% on TA22 = EUR 1,200. Excess EUR 3,000 must be declared on TA24 at progressive rates combined with employment income. [T2] Flag for reviewer to compute the correct split and confirm progressive rate on the excess.

### EC9 -- Home office, dual-use room [T2]
**Situation:** Client works from the kitchen table and wants to deduct 20% of home expenses.
**Resolution:** NOT deductible. A dual-use room does not qualify. A dedicated room used exclusively for work is required. If client has no dedicated workspace, no home office deduction applies. [T2] Flag for reviewer to confirm workspace arrangement with client.

### EC10 -- Bad debt write-off [T2]
**Situation:** Client invoiced EUR 3,000 to a client who has not paid for 18 months and is now insolvent.
**Resolution:** Deductible as bad debt only if: (1) the income was previously declared (it was in Box 1 in a prior year), (2) all reasonable steps to recover have been taken, and (3) the debt is genuinely irrecoverable. [T2] Flag for reviewer to confirm all three conditions before allowing the deduction.

### EC11 -- Software capitalisation vs expensing [T1/T2]
**Situation:** Client pays EUR 2,400 for a 2-year software licence upfront.
**Resolution:** If the licence is under EUR 1,160 or is a recurring subscription, expense in Box 2 fully. If it is a capital software purchase over EUR 1,160, capitalise and depreciate at 25% per year. [T2] Flag for reviewer if the nature of the software licence is unclear (perpetual vs subscription).

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Warranted accountant must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to warranted accountant. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard single self-employed, mid-range income
**Input:** Single, born 1990, gross revenue EUR 45,000, allowable expenses EUR 13,000, capital allowances EUR 375, SSC paid EUR 3,000, provisional tax paid EUR 3,500.
**Expected output:** Box 3 = EUR 32,000, Box 15 = EUR 375, Box 20 = EUR 3,000, Box 25 = EUR 3,375, Box 30 = EUR 28,625. Tax: EUR 0 + EUR 810 + EUR 1,250 + EUR 2,281 = EUR 4,341. Box 36 = EUR 3,500. Box 40 = EUR 841 due.

### Test 2 -- Married, higher income, capped at 35%
**Input:** Married, gross revenue EUR 80,000, allowable expenses EUR 20,000, SSC paid EUR 4,362 (maximum), no provisional tax (first year).
**Expected output:** Box 3 = EUR 60,000, Box 20 = EUR 4,362, Box 30 = EUR 55,638. Tax: EUR 0 + EUR 1,275 + EUR 3,150 + EUR 6,735 + EUR (55,638-60,000 = negative, cap at 60,000 band) -- chargeable income is EUR 55,638 so stays within 25% band. Total tax = EUR 0 + EUR 1,275 + EUR 1,875 + EUR 6,735 = EUR 9,885. Box 40 = EUR 9,885 due.

### Test 3 -- TA22 eligible client
**Input:** Full-time employed, side income net profit EUR 8,000, Class 1 SSC paid through employer.
**Expected output:** TA22 applies. Tax = EUR 8,000 x 10% = EUR 800. No Class 2 SSC. No provisional tax instalments on side income.

### Test 4 -- Entertainment expense blocked
**Input:** Client includes EUR 2,000 client entertainment in Box 2.
**Expected output:** Remove EUR 2,000 from Box 2. Entertainment blocked under Article 14. Not deductible.

### Test 5 -- Capital item incorrectly expensed
**Input:** Laptop EUR 1,500 included in Box 2 as expense.
**Expected output:** Remove EUR 1,500 from Box 2. Add EUR 375 (25% x EUR 1,500) to Box 15 as capital allowance.

### Test 6 -- Article 11 client, VAT as expense
**Input:** Article 11 client. Purchase invoice EUR 236 gross (EUR 200 net + EUR 36 VAT).
**Expected output:** Box 2 deductible expense = EUR 236 (gross). Cannot reclaim VAT. Full gross is the cost.

### Test 7 -- Provisional tax calculation
**Input:** 2025 TA24 shows final tax liability EUR 6,000. Client asks for 2026 provisional tax schedule.
**Expected output:** 1st instalment 30 April 2026 = EUR 1,200 (20%). 2nd instalment 31 August 2026 = EUR 1,800 (30%). 3rd instalment 21 December 2026 = EUR 3,000 (50%).

### Test 8 -- VAT excluded from income correctly
**Input:** Article 10 client. Total receipts from clients EUR 53,100 (includes 18% VAT on all sales). Net sales = EUR 45,000.
**Expected output:** Box 1 = EUR 45,000. EUR 8,100 VAT collected is excluded -- it is a VAT liability, not income.

---

## PROHIBITIONS

- NEVER apply a rate table without knowing marital status
- NEVER compute Box 35 tax figures directly -- pass chargeable income to the deterministic engine
- NEVER allow entertainment expenses in Box 2
- NEVER allow income tax itself as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER include VAT collected on sales in Box 1 for Article 10 clients
- NEVER allow a capital item to be expensed directly in Box 2 -- it must go through Box 15 capital allowances
- NEVER use current year income for provisional tax -- always prior year final liability
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their accountant for confirmation
- NEVER advise on arrears situations without escalating to a warranted accountant

---

## Contribution Notes (For Non-Malta Jurisdictions)

If adapting this skill for another country:

1. Replace Chapter 123 references with the equivalent national income tax legislation.
2. Replace the rate tables (single/married/parent) with your jurisdiction's equivalent bands and rates.
3. Replace the TA24 box structure with your jurisdiction's equivalent self-assessment return form and box numbers.
4. Replace the "wholly and exclusively" test with your jurisdiction's equivalent deductibility standard.
5. Replace capital allowance rates (6th Schedule) with your jurisdiction's equivalent depreciation schedule.
6. Replace provisional tax percentages and deadlines with your jurisdiction's equivalent instalment system.
7. Replace the TA22 regime with your jurisdiction's equivalent simplified regime for part-time self-employment, if one exists.
8. Replace filing deadlines (30 June) and penalty rates with your jurisdiction's current figures.
9. Replace the VAT interaction rules based on your jurisdiction's VAT/GST system.
10. Have a licensed practitioner in your jurisdiction validate every T1 rule before publishing.
11. Add jurisdiction-specific edge cases to the Edge Case Registry.

**A skill may not be published without sign-off from a warranted practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
