---
name: uk-self-employment-sa103
description: >
  Use this skill whenever asked about UK self-employment income for sole traders filing SA103S (short) or SA103F (full) as part of Self Assessment. Trigger on phrases like "self-employment income", "SA103", "trading income", "sole trader tax", "allowable expenses UK", "capital allowances UK", "trading allowance", "basis period", "simplified expenses", "Class 4 NIC", "loss relief self-employed", or any question about computing self-employment profits for a UK sole trader. Covers trading income computation, allowable expenses, capital allowances (AIA, WDA, FYA), simplified expenses, the trading allowance, basis period reform, loss relief, and Class 4 NIC interaction. ALWAYS read this skill before touching any UK self-employment work.
version: 1.0
jurisdiction: GB
tax_year: 2024-25
category: international
depends_on:
  - income-tax-workflow-base
---

# UK Self-Employment (SA103) -- Sole Trader Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | United Kingdom (England, Wales, Northern Ireland; Scotland for non-savings, non-dividend income uses Scottish rates on SA100) |
| Jurisdiction Code | GB |
| Primary Legislation | Income Tax (Trading and Other Income) Act 2005 (ITTOIA 2005); Capital Allowances Act 2001 (CAA 2001); Income Tax Act 2007 (ITA 2007) |
| Supporting Legislation | Finance Act 2024 (basis period reform); Finance Act 2025 (capital allowances changes); Social Security Contributions and Benefits Act 1992 (Class 2/4 NIC) |
| Tax Authority | HM Revenue & Customs (HMRC) |
| Filing Portal | HMRC Self Assessment Online |
| Contributor | Open Accountants Community |
| Validated By | [Pending -- requires sign-off by a UK-qualified accountant (ACA/ACCA/CTA)] |
| Validation Date | [Pending] |
| Skill Version | 1.0 |
| Tax Year | 2024/25 (6 April 2024 to 5 April 2025) |
| Confidence Coverage | Tier 1: rate tables, AIA/WDA rates, trading allowance threshold, flat-rate simplified expenses, Class 4 NIC bands, filing deadlines, penalty structure. Tier 2: mixed-use expense apportionment, home office proportion, motor vehicle business %, loss relief election choices, basis period transitional adjustments. Tier 3: partnerships, non-resident traders, HMRC enquiries, complex capital disposals, overlap relief computations. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any self-employment profit figure, you MUST know:

1. **Tax year** [T1] -- confirm 2024/25 (6 April 2024 to 5 April 2025)
2. **Accounting basis** [T1] -- cash basis or accruals basis. From 2024/25, cash basis is the default for sole traders unless they elect for accruals.
3. **Gross turnover** [T1] -- total sales/revenue in the period
4. **SA103S or SA103F** [T1] -- SA103S if turnover below GBP 90,000; SA103F if GBP 90,000 or above
5. **Nature of trade** [T1] -- description of business activity (SIC code)
6. **Date trade commenced** [T1] -- relevant for basis period rules and early-years loss relief
7. **Accounting date** [T1/T2] -- if not 31 March or 5 April, basis period apportionment applies from 2024/25
8. **Business expenses** [T1/T2] -- nature and amount (T2 for mixed-use items)
9. **Capital expenditure in the year** [T1] -- type, cost, date acquired
10. **Simplified expenses election** [T1] -- whether client uses flat-rate mileage, home-use, or living-at-premises rates
11. **Other self-employments** [T1] -- each trade needs a separate SA103
12. **Prior year losses brought forward** [T1] -- amount and source trade
13. **Scottish taxpayer status** [T1] -- affects income tax rates on SA100 (not the SA103 computation itself)
14. **VAT registered** [T1] -- if VAT-registered, figures on SA103 should be net of VAT

**If gross turnover is unknown, STOP. Cannot determine SA103S vs SA103F or compute profit.**

---

## Step 1: Determine SA103 Version [T1]

**Legislation:** HMRC SA103S/SA103F Notes 2025

| Condition | Form |
|-----------|------|
| Annual turnover below GBP 90,000 | SA103S (Short) |
| Annual turnover GBP 90,000 or above | SA103F (Full) |

SA103F requires detailed expense breakdown by category. SA103S allows a single total expenses figure.

A separate SA103 is required for each self-employment carried on during the year.

---

## Step 2: Trading Income Computation [T1]

**Legislation:** ITTOIA 2005, Part 2

### Computation Structure

| Line | Description | Notes |
|------|-------------|-------|
| A | Turnover | Gross income from the trade |
| B | Less: Allowable expenses | See Step 3 |
| C | Net profit (A minus B) | Before capital allowances |
| D | Less: Capital allowances | See Step 4 |
| E | Plus: Balancing charges | On disposal of capital assets |
| F | Adjusted profit (C minus D plus E) | Trading profit for tax purposes |
| G | Less: Losses brought forward | From prior years (same trade only) |
| H | Taxable trading profit | Carried to SA100 |

### Cash Basis vs Accruals Basis [T1]

| Aspect | Cash Basis (default from 2024/25) | Accruals Basis |
|--------|----------------------------------|----------------|
| Income recognition | When received | When earned/invoiced |
| Expense recognition | When paid | When incurred |
| Capital allowances | AIA and WDA available | AIA and WDA available |
| Loss relief | Carry forward only (no sideways) | Sideways, carry-back, carry-forward |
| Interest deduction | GBP 500 limit | No limit |
| Turnover threshold | No upper limit from 2024/25 | N/A (available to all) |

**Important:** From 2024/25, cash basis is the DEFAULT. Traders must actively elect for accruals basis if they want it. Previously it was the other way round.

---

## Step 3: Allowable Expenses [T1/T2]

**Legislation:** ITTOIA 2005, ss 33-58

### The Test [T1]

An expense is deductible only if incurred **wholly and exclusively** for the purposes of the trade. Mixed-use expenses must be apportioned -- only the business element is deductible.

### Deductible Expenses

| Expense Category | SA103F Box | Tier | Treatment |
|-----------------|------------|------|-----------|
| Cost of goods sold / materials | Box 10 | T1 | Fully deductible |
| Construction Industry subcontractor costs | Box 11 | T1 | Fully deductible |
| Wages, salaries, staff costs | Box 12 | T1 | Fully deductible |
| Car, van, travel expenses | Box 13 | T1/T2 | Business portion only; or use simplified expenses mileage rate |
| Rent, rates, power, insurance | Box 14 | T1/T2 | Fully deductible if business premises; proportional if home office |
| Repairs and maintenance of property and equipment | Box 15 | T1 | Revenue repairs only (not improvements) |
| Phone, fax, stationery, other office costs | Box 16 | T1/T2 | Business portion only for dual-use items (e.g. personal mobile) |
| Advertising and business entertainment costs | Box 17 | T1 | Advertising: fully deductible. Entertainment of clients: NOT deductible (see Prohibitions) |
| Interest on business loans and bank charges | Box 18 | T1 | Fully deductible (cash basis: capped at GBP 500 interest) |
| Bank and credit card financial charges | Box 18 | T1 | Fully deductible |
| Irrecoverable debts written off | Box 19 | T2 | Flag for reviewer -- confirm debt genuinely irrecoverable |
| Accountancy, legal, professional fees | Box 20 | T1 | Fully deductible if business-related |
| Depreciation and loss/profit on sale | Box 21 | T1 | NOT deductible (accounting depreciation is disallowed; capital allowances claimed separately) |
| Other expenses | Box 22 | T1/T2 | Subscriptions, insurance, training related to trade |
| Total expenses | Box 23 | T1 | Sum of Boxes 10-22 |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Business entertainment (client meals, hospitality) | Blocked by ITTOIA 2005, s 45 |
| Personal living expenses | Not for purposes of the trade |
| Fines and penalties | Public policy |
| Income tax, Class 4 NIC | Tax on profits cannot be deducted against profits |
| Accounting depreciation | Replaced by capital allowances system |
| Capital expenditure | Goes through capital allowances, not revenue expenses |
| Private proportion of dual-use costs | Only business proportion deductible |
| Clothing (ordinary, suitable for everyday wear) | Not exclusively for trade -- see exception below |

### Clothing Exception [T1]

Protective clothing, uniforms, costumes required for the trade ARE deductible. Ordinary clothing that could be worn outside work is NOT deductible, even if purchased specifically for work.

### Home Office Rules [T2]

**Legislation:** ITTOIA 2005, s 34

Two methods available:

**Method 1 -- Actual costs (proportional):**
- Calculate proportion of home used exclusively for business (room count or floor area basis)
- Apply percentage to: mortgage interest/rent, council tax, utilities, insurance, broadband
- Must be a dedicated workspace used exclusively for business during working hours
- [T2] Flag for reviewer: confirm workspace arrangement and apportionment basis

**Method 2 -- Simplified expenses flat rate (see Step 5)**

---

## Step 4: Capital Allowances [T1]

**Legislation:** Capital Allowances Act 2001 (CAA 2001)

### Annual Investment Allowance (AIA) [T1]

| Item | Value |
|------|-------|
| AIA limit | GBP 1,000,000 per year |
| Eligible assets | Most plant and machinery (not cars) |
| Effect | 100% deduction in the year of purchase |

The AIA limit is GBP 1,000,000 permanently (set by Finance Act 2023).

### Writing Down Allowance (WDA) [T1]

For expenditure exceeding the AIA limit, or for assets not eligible for AIA:

| Pool | Rate | Assets |
|------|------|--------|
| Main rate pool | 18% (reducing balance) | Most plant and machinery, cars with CO2 emissions 1-50 g/km |
| Special rate pool | 6% (reducing balance) | Long-life assets, integral features, thermal insulation, cars with CO2 over 50 g/km |

**Note:** From April 2026 (i.e. 2026/27 tax year), the main rate WDA reduces from 18% to 14%. For 2024/25 and 2025/26, the rate remains 18%.

### First-Year Allowances (FYA) [T1]

| Allowance | Rate | Eligible Assets |
|-----------|------|-----------------|
| Full expensing | 100% | Main rate plant and machinery (companies only -- NOT available to sole traders) |
| Zero-emission car | 100% | New zero-emission cars (0 g/km CO2) |
| Zero-emission goods vehicle | 100% | New zero-emission vans |
| Electric charge point | 100% | New EV charge points (until 31 March 2025) |
| New 40% FYA (from 1 January 2026) | 40% | Certain qualifying assets -- available to unincorporated businesses |

**Important:** Full expensing (100% FYA on main rate assets) is for companies ONLY. Sole traders use the AIA instead.

### Cars [T1]

| CO2 Emissions | Treatment |
|---------------|-----------|
| 0 g/km (fully electric) | 100% FYA in year of purchase |
| 1-50 g/km | Main rate pool (18% WDA) |
| Over 50 g/km | Special rate pool (6% WDA) |

Business-use proportion only is claimable [T2]. Private use is excluded.

### Small Pools Allowance [T1]

If the balance on the main rate or special rate pool is GBP 1,000 or less, the full balance can be written off.

### Balancing Adjustments [T2]

On disposal of an asset:
- Proceeds > written-down value = balancing charge (added back as taxable income)
- Proceeds < written-down value = balancing allowance (additional deduction)
- [T2] Flag for reviewer: confirm disposal proceeds and written-down value

---

## Step 5: Simplified Expenses [T1]

**Legislation:** ITTOIA 2005, ss 94D-94H

Simplified expenses are optional flat-rate deductions that replace actual cost calculations. Available to sole traders and partnerships with no corporate partners.

### Vehicles -- Flat Rate Mileage [T1]

| Vehicle Type | First 10,000 miles | Over 10,000 miles |
|-------------|-------------------|-------------------|
| Cars and goods vehicles | 45p per mile | 25p per mile |
| Motorcycles | 24p per mile | 24p per mile |

- Once you use the mileage rate for a vehicle, you must continue using it for that vehicle
- Covers fuel, insurance, repairs, road tax -- no separate claim for these
- Business miles must be recorded

### Working from Home -- Flat Rate [T1]

| Hours worked at home per month | Flat rate per month |
|-------------------------------|-------------------|
| 25-50 hours | GBP 10 |
| 51-100 hours | GBP 18 |
| 101+ hours | GBP 26 |

- Covers additional household costs (heat, light, power)
- Does NOT cover business phone, broadband dedicated to business, or mortgage interest/rent -- these are claimed separately on actual cost basis
- Hours must be recorded

### Living at Business Premises -- Flat Rate Deduction for Private Use [T1]

| Number of occupants | Monthly flat rate deducted for private use |
|--------------------|------------------------------------------|
| 1 person | GBP 350 |
| 2 persons | GBP 500 |
| 3+ persons | GBP 650 |

- The flat rate is SUBTRACTED from total premises costs to arrive at the business portion
- You claim total premises costs minus the personal-use flat rate

### Choosing Simplified vs Actual [T1]

| Category | Can switch each year? |
|----------|----------------------|
| Vehicles | NO -- once chosen for a vehicle, must continue for that vehicle |
| Home use | YES -- can switch at start of each tax year |
| Business premises | YES -- can switch at start of each tax year |

---

## Step 6: Trading Allowance [T1]

**Legislation:** ITTOIA 2005, s 783A (inserted by Finance Act 2017)

| Item | Value |
|------|-------|
| Trading allowance | GBP 1,000 per tax year |

### How It Works [T1]

| Scenario | Treatment |
|----------|-----------|
| Gross trading income GBP 1,000 or less | Full relief -- no tax, no need to register for Self Assessment or report |
| Gross trading income over GBP 1,000 | Choose: (a) deduct actual expenses OR (b) deduct GBP 1,000 trading allowance instead of expenses |

### Rules [T1]

- The allowance is per person, not per trade
- It applies to gross income (turnover), not profit
- You CANNOT claim both the trading allowance AND actual expenses -- it is one or the other
- Does not apply to income from a connected party (e.g. your own company)
- Does not apply if the trade also receives other tax reliefs (e.g. overlap relief, loss relief)

---

## Step 7: Basis Period Reform -- Tax Year Basis [T1/T2]

**Legislation:** Finance Act 2024, ss 7-16; ITTOIA 2005 (as amended)

### Overview [T1]

From 2024/25, ALL sole traders and partners are taxed on the **tax year basis**. This means the taxable profit for 2024/25 is the profit arising in the period 6 April 2024 to 5 April 2025, regardless of the accounting date.

### Transition Year (2023/24) [T2]

2023/24 was the transition year. Businesses with accounting dates other than 31 March/5 April may have had additional "transition profits" brought into charge. These transition profits are spread over 5 years (2023/24 to 2027/28), with 20% taxed each year, unless the trader elects to accelerate.

| Item | Detail |
|------|--------|
| Transition year | 2023/24 |
| Spreading period | 5 years (2023/24 through 2027/28) |
| Default spread | 20% of transition profit per year |
| Acceleration | Trader can elect to bring more into charge earlier |
| Cessation | All remaining transition profit is taxed in the year the trade ceases |

### Non-Aligned Accounting Dates (from 2024/25) [T2]

If the accounting date is NOT 31 March or 5 April:
- Apportion profits from two sets of accounts to calculate the tax year profit
- Example: accounting date 30 June 2024 -- apportion 3/12 of year ended 30 June 2024 + 9/12 of year ended 30 June 2025
- [T2] Flag for reviewer: confirm apportionment calculation and whether estimated figures are used

### Practical Recommendation [T1]

Most sole traders should consider changing their accounting date to 31 March or 5 April to avoid annual apportionment complexity.

---

## Step 8: Loss Relief Options [T1/T2]

**Legislation:** ITA 2007, ss 64-90 (sideways); ITTOIA 2005, s 83 (carry-forward)

### Available Loss Reliefs

| Relief | Legislation | Effect | Restrictions |
|--------|-------------|--------|-------------|
| Carry forward | ITA 2007, s 83 | Set loss against future profits of the SAME trade | No time limit; no cap |
| Sideways relief (current year) | ITA 2007, s 64 | Set loss against total income of the SAME tax year | Accruals basis only (not cash basis); cap applies |
| Sideways relief (prior year) | ITA 2007, s 64 | Set loss against total income of the PREVIOUS tax year | Accruals basis only; cap applies |
| Early years relief | ITA 2007, s 72 | Carry back loss to the 3 preceding tax years (FIFO) | First 4 years of trade only; accruals basis only |
| Terminal loss relief | ITA 2007, s 89 | Carry back loss to the 3 preceding tax years | Final 12 months of trade only |
| Loss set against capital gains | ITA 2007, s 71 | After sideways relief used, excess set against CGT | Only if sideways relief claimed first |

### Sideways Relief Cap [T1]

Sideways and carry-back relief (ss 64, 72) is capped at the GREATER of:
- GBP 50,000, or
- 25% of adjusted total income

Any excess above the cap can only be carried forward against future trade profits.

### Cash Basis Loss Restriction [T1]

**If the trader uses cash basis:** Only carry-forward relief is available. No sideways relief, no carry-back, no capital gains relief.

### Loss Relief Decision [T2]

[T2] Flag for reviewer: the choice of loss relief has significant tax planning implications. Confirm which relief(s) the client should claim, considering:
- Current and prior year marginal tax rates
- Whether cash basis or accruals basis is used
- Whether the trade is in its first 4 years
- Whether the trade is ceasing

---

## Step 9: Class 4 NIC Interaction [T1]

**Legislation:** Social Security Contributions and Benefits Act 1992

### Class 4 NIC Rates (2024/25) [T1]

| Band | Rate |
|------|------|
| Profits below GBP 12,570 (Lower Profits Limit) | 0% |
| Profits GBP 12,570 to GBP 50,270 (Upper Profits Limit) | 6% |
| Profits above GBP 50,270 | 2% |

### Class 2 NIC (2024/25) [T1]

| Item | Value |
|------|-------|
| Weekly rate | GBP 3.45 |
| Small Profits Threshold | GBP 6,725 |
| Mandatory payment | NO -- from 6 April 2024, Class 2 NIC is no longer mandatory |
| Voluntary payment | Available for NIC credit purposes (state pension, contributory benefits) |

### Key Rules [T1]

- Class 4 NIC is calculated on the **same profit figure** as income tax (the taxable trading profit from SA103)
- Class 4 NIC is collected through Self Assessment
- Class 4 NIC is NOT deductible against trading profits
- If multiple self-employments, Class 4 NIC is on combined profits
- From 2024/25, self-employed persons no longer pay mandatory Class 2 NIC but receive NIC credits automatically if profits exceed the Small Profits Threshold

---

## Step 10: Filing Deadlines and Penalties [T1]

**Legislation:** TMA 1970, ss 8-12, 93, 97

### Filing Deadlines [T1]

| Deadline | Date |
|----------|------|
| Paper SA100 return (including SA103) | 31 October 2025 |
| Online SA100 return (including SA103) | 31 January 2026 |
| Payment of balance of tax + Class 4 NIC | 31 January 2026 |
| First payment on account for 2025/26 | 31 January 2026 |
| Second payment on account for 2025/26 | 31 July 2026 |

### Late Filing Penalties [T1]

| Delay | Penalty |
|-------|---------|
| 1 day late | GBP 100 (even if no tax owed) |
| 3 months late | GBP 10 per day for up to 90 days (max GBP 900) |
| 6 months late | Greater of GBP 300 or 5% of tax due |
| 12 months late | Greater of GBP 300 or 5% of tax due (additional) |

### Late Payment Penalties [T1]

| Delay | Penalty |
|-------|---------|
| 30 days late | 5% of tax unpaid |
| 6 months late | Additional 5% of tax still unpaid |
| 12 months late | Additional 5% of tax still unpaid |

Interest is charged on all late payments from the due date.

---

## Step 11: SA103 Box Summary -- Quick Reference [T1]

### SA103S (Short) -- Key Boxes

| Box | Description |
|-----|-------------|
| Box 9 | Turnover (sales/income) |
| Box 10 | Trading allowance (if used instead of expenses) |
| Box 11 | Total allowable expenses (if not using trading allowance) |
| Box 12 | Net profit or loss |
| Box 13 | Capital allowances |
| Box 14 | Balancing charges |
| Box 15 | Goods or services for own use |
| Box 16 | Total taxable profit (or net loss) |

### SA103F (Full) -- Key Boxes

| Box | Description |
|-----|-------------|
| Box 9 | Turnover |
| Boxes 10-22 | Detailed expense categories (see Step 3) |
| Box 23 | Total expenses |
| Box 24 | Net profit or loss |
| Box 25-27 | Capital allowances, balancing charges |
| Box 28 | Goods or services for own use |
| Box 29 | Total taxable profit (or net loss) |

---

## PROHIBITIONS

- NEVER compute taxable profit without confirming whether cash basis or accruals basis applies
- NEVER allow business entertainment as a deductible expense
- NEVER allow accounting depreciation as a deductible expense -- use capital allowances instead
- NEVER allow income tax or Class 4 NIC as a deductible expense
- NEVER allow fines or penalties as a deductible expense
- NEVER claim both the trading allowance AND actual expenses -- it is one or the other
- NEVER claim full expensing (100% FYA on main rate assets) for a sole trader -- that is companies only
- NEVER claim sideways or carry-back loss relief for a trader using cash basis
- NEVER apply capital allowances to a car at the AIA rate -- cars are excluded from AIA
- NEVER include VAT-inclusive figures on SA103 if the trader is VAT-registered -- use net-of-VAT figures
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their accountant for confirmation

---

## Step 12: Edge Case Registry

### EC1 -- Trading allowance vs actual expenses [T1]
**Situation:** Sole trader has turnover of GBP 3,000 and expenses of GBP 800.
**Resolution:** Compare: (a) actual expenses GBP 800 gives profit GBP 2,200; (b) trading allowance GBP 1,000 gives profit GBP 2,000. Trading allowance is more beneficial. But note: if expenses exceed GBP 1,000, actual expenses would be better. Client should compute both and choose the lower profit.

### EC2 -- Car purchased by sole trader [T1]
**Situation:** Sole trader buys a car for GBP 25,000 (120 g/km CO2) used 70% for business.
**Resolution:** Car goes to special rate pool (CO2 > 50 g/km). WDA = GBP 25,000 x 6% = GBP 1,500 x 70% business use = GBP 1,050. Cars are NOT eligible for AIA.

### EC3 -- Cash basis loss [T1]
**Situation:** Trader on cash basis makes a loss of GBP 5,000. Wants to offset against employment income.
**Resolution:** NOT ALLOWED. Cash basis losses can only be carried forward against future profits of the same trade. No sideways relief. If the trader wants sideways relief, they must elect for accruals basis.

### EC4 -- Non-aligned accounting date [T2]
**Situation:** Trader with 30 September year-end. Tax year 2024/25.
**Resolution:** Apportion: 6/12 of profits for y/e 30 September 2024 + 6/12 of profits for y/e 30 September 2025. If the second set of accounts is not finalised, use a reasonable estimate and amend later. [T2] Flag for reviewer.

### EC5 -- Transition profit from basis period reform [T2]
**Situation:** Trader has GBP 10,000 transition profit from 2023/24.
**Resolution:** GBP 2,000 (20%) is taxed in each of 2023/24, 2024/25, 2025/26, 2026/27, 2027/28. If the trader ceases trading in 2025/26, the remaining GBP 6,000 is taxed in 2025/26. [T2] Flag for reviewer to confirm amounts and spreading elections.

### EC6 -- Simplified expenses and actual expenses mixed [T1]
**Situation:** Trader wants to use mileage rate for car but actual costs for home office.
**Resolution:** ALLOWED. Simplified expenses can be used for some categories and actual costs for others. The restriction is per-category, not all-or-nothing. But once mileage rate is chosen for a specific vehicle, it must continue for that vehicle.

### EC7 -- Capital allowances on home office equipment [T1/T2]
**Situation:** Trader buys a GBP 1,200 laptop used 80% for business, 20% personal.
**Resolution:** Claim AIA on GBP 1,200. Private use adjustment: 20% is disallowed. Net allowance: GBP 1,200 x 80% = GBP 960. [T2] Flag for reviewer to confirm business-use percentage.

### EC8 -- Early years loss relief [T2]
**Situation:** Trader started business on 1 July 2023. Makes GBP 15,000 loss in 2024/25 on accruals basis.
**Resolution:** As trade started within the last 4 years, early years relief (s 72 ITA 2007) is available: carry back loss to the 3 preceding tax years (2021/22, 2022/23, 2023/24) on a FIFO basis. [T2] Flag for reviewer to confirm optimal use of loss and cap calculation.

### EC9 -- VAT flat rate scheme interaction [T1]
**Situation:** Trader is on VAT flat rate scheme. Receives GBP 12,000 inclusive of VAT. Pays GBP 1,200 to HMRC under flat rate scheme.
**Resolution:** Income on SA103 = GBP 12,000 (the gross receipt). The GBP 1,200 paid to HMRC is NOT an expense. The difference between VAT collected and VAT paid under the flat rate scheme is income. Report full gross receipts on SA103.

### EC10 -- Cessation and terminal loss relief [T2]
**Situation:** Trader ceases trading on 31 December 2024 with a loss in the final period.
**Resolution:** Terminal loss relief (s 89 ITA 2007) available: carry back loss to the 3 preceding tax years. Plus any remaining transition profit is taxed in the cessation year. [T2] Flag for reviewer to compute terminal loss and confirm carry-back allocation.

---

## Step 13: Test Suite

### Test 1 -- Standard sole trader, basic case
**Input:** Turnover GBP 45,000, allowable expenses GBP 12,000, AIA on laptop GBP 800, no losses, cash basis, no simplified expenses.
**Expected output:** SA103S. Net profit = GBP 45,000 - GBP 12,000 = GBP 33,000. Capital allowances = GBP 800. Taxable profit = GBP 32,200.
Class 4 NIC: (GBP 32,200 - GBP 12,570) x 6% = GBP 1,177.80.

### Test 2 -- Trading allowance used
**Input:** Turnover GBP 2,500, actual expenses GBP 600.
**Expected output:** Trading allowance (GBP 1,000) is more beneficial than actual expenses (GBP 600). Taxable profit = GBP 2,500 - GBP 1,000 = GBP 1,500.

### Test 3 -- Car capital allowances
**Input:** Sole trader buys car for GBP 30,000, CO2 75 g/km, 60% business use. No other capital expenditure.
**Expected output:** Car in special rate pool (CO2 > 50 g/km). WDA = GBP 30,000 x 6% = GBP 1,800 x 60% = GBP 1,080. NOT eligible for AIA.

### Test 4 -- Simplified expenses (mileage + home)
**Input:** 12,000 business miles in car. Works from home 120 hours per month for 10 months.
**Expected output:** Mileage: (10,000 x 45p) + (2,000 x 25p) = GBP 4,500 + GBP 500 = GBP 5,000. Home: 10 months x GBP 26 = GBP 260. Total simplified expenses = GBP 5,260.

### Test 5 -- Cash basis loss, no sideways relief
**Input:** Cash basis trader. Turnover GBP 8,000, expenses GBP 12,000, loss GBP 4,000. Employment income GBP 40,000.
**Expected output:** Loss GBP 4,000 carried forward only. Cannot offset against employment income because cash basis is used. Taxable trading profit = GBP 0. Loss memo: GBP 4,000 c/f.

### Test 6 -- Sideways loss relief (accruals basis)
**Input:** Accruals basis trader. Trading loss GBP 20,000. Employment income GBP 60,000. Total income GBP 60,000.
**Expected output:** Sideways relief cap = greater of GBP 50,000 or 25% x GBP 60,000 = GBP 15,000. Cap = GBP 50,000. Loss GBP 20,000 is within cap. Full GBP 20,000 offset against total income. Remaining total income = GBP 40,000.

### Test 7 -- Non-aligned accounting date
**Input:** Year-end 30 June. Profit y/e 30 June 2024 = GBP 36,000. Profit y/e 30 June 2025 = GBP 48,000. Tax year 2024/25.
**Expected output:** Apportionment: (3/12 x GBP 36,000) + (9/12 x GBP 48,000) = GBP 9,000 + GBP 36,000 = GBP 45,000 taxable in 2024/25. Plus any transition profit spreading instalment.

### Test 8 -- Class 4 NIC computation, higher earner
**Input:** Taxable trading profit GBP 80,000.
**Expected output:** Class 4 NIC: (GBP 50,270 - GBP 12,570) x 6% = GBP 2,262. Plus (GBP 80,000 - GBP 50,270) x 2% = GBP 594.60. Total Class 4 = GBP 2,856.60.

---

## Step 14: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified accountant must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified accountant. Document gap.
```

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
