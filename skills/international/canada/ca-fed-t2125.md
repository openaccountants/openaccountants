---
name: ca-fed-t2125
description: >
  Use this skill whenever asked about Canadian self-employment business income reported on Form T2125 (Statement of Business or Professional Activities). Trigger on phrases like "T2125", "business income Canada", "self-employed expenses", "CCA", "capital cost allowance", "home office Canada", "motor vehicle expenses CRA", "business-use-of-home", "sole proprietor Canada", "net business income", "business number BN", "fiscal year end", "GST ITC", or any question about computing, classifying, or reporting business income and expenses for a Canadian sole proprietor. Covers Parts 1-8 of T2125, allowable expenses, CCA classes and rates, AccII, business-use-of-home, motor vehicle expenses, GST/HST interaction, and net income computation. ALWAYS read this skill before touching any T2125 work.
version: 1.0
jurisdiction: CA-FED
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Canada Self-Employment (T2125) -- Sole Proprietor Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Canada -- Federal |
| Jurisdiction Code | CA-FED |
| Primary Legislation | Income Tax Act (ITA), R.S.C. 1985, c. 1 (5th Supp.) |
| Supporting Legislation | Income Tax Regulations (ITR); Excise Tax Act (ETA) for GST/HST; CRA Guide T4002 |
| Tax Authority | Canada Revenue Agency (CRA) |
| Filing Portal | CRA My Account / NETFILE / EFILE |
| Form | T2125 -- Statement of Business or Professional Activities |
| Contributor | Open Accountants Community |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: expense classification, CCA rates, tax bracket application, BN requirements, filing deadlines. Tier 2: mixed-use expense apportionment, home office, motor vehicle business %, reasonable expense judgement. Tier 3: partnerships, corporations, non-resident income, complex disposals, SR&ED. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. CPA/CA must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any business income figure, you MUST know:

1. **Legal name and business name** [T1] -- as registered with CRA
2. **Business Number (BN)** [T1] -- 9-digit BN + RT program account if GST/HST registered
3. **Industry code (NAICS)** [T1] -- 6-digit North American Industry Classification System code
4. **Fiscal year end** [T1] -- must be December 31 for sole proprietors (see Step 2)
5. **Gross business revenue** [T1] -- total sales/fees/commissions for the fiscal period
6. **Business expenses by category** [T1/T2] -- nature and amount of each expense
7. **Capital assets acquired or disposed of** [T1] -- type, cost, date acquired, CCA class
8. **Business-use-of-home** [T2] -- does the taxpayer work from home? Dedicated space?
9. **Motor vehicle usage** [T2] -- does the taxpayer use a vehicle for business? Log maintained?
10. **GST/HST registration status** [T1] -- registered or small supplier? Quick method?
11. **Method of accounting** [T1] -- accrual or cash (most sole proprietors may use either)
12. **Partnership or sole proprietor** [T1] -- this skill covers sole proprietors only

**If fiscal year end is not December 31 and no T1139 election exists, STOP. Confirm with the taxpayer.**

---

## Step 1: Business Number (BN) Requirements [T1]

**Legislation:** ITA s. 162(7.01); CRA RC2 Guide

| Requirement | Detail |
|-------------|--------|
| When required | Within 15 days of beginning any commercial activity if you are a GST/HST registrant; otherwise when the first T2125 is filed |
| Format | 9-digit BN (e.g., 123456789) + 2-letter program identifier + 4-digit account number (e.g., 123456789RT0001 for GST/HST) |
| Program accounts | RT (GST/HST), RC (corporate tax -- N/A for sole proprietors), RP (payroll), RZ (information returns) |
| How to register | Online via CRA Business Registration Online, by phone, or by mail (Form RC1) |
| Multiple businesses | One sole proprietor may have multiple T2125 forms attached to the same T1 return; each business gets its own BN or same BN with different program accounts |

---

## Step 2: Fiscal Year End [T1]

**Legislation:** ITA s. 249.1(1); ITA s. 34.1 (alternative method)

| Rule | Detail |
|------|--------|
| Default | Sole proprietors MUST use December 31 as fiscal year end |
| Alternative method | ITA s. 34.1 allows a non-calendar fiscal year end if Form T1139 is filed. An additional income amount is added to reconcile to the calendar year. This is rare and adds complexity. |
| First year | Fiscal period may be shorter than 12 months (from start date to December 31) |
| CCA in short year | CCA is NOT prorated for a short fiscal period (CRA's position) unless the property was available for use for only part of the year |
| Recommendation | [T2] If client has a non-December 31 fiscal year, flag for reviewer. The alternative method under s. 34.1 requires annual T1139 reconciliation. |

---

## Step 3: T2125 Structure -- Parts 1 through 8 [T1]

**Legislation:** CRA Form T2125; CRA Guide T4002

### Part 1 -- Identification

| Field | Content |
|-------|---------|
| Business name | Legal or trade name |
| Business address | Principal place of business |
| BN | 9-digit business number |
| Industry code | 6-digit NAICS code |
| Business activity | Brief description of main activity |
| Fiscal period | Start and end dates (normally Jan 1 -- Dec 31) |
| Accounting method | Cash or accrual |
| Partnership? | Yes/No (this skill: No -- sole proprietor only) |

### Part 2 -- Internet Business Activities

Website addresses and percentage of gross income from the internet.

### Part 3 -- Business Income

| Line | Description |
|------|-------------|
| 8000 | Gross sales, commissions, or fees |
| 8230 | Reserves deducted last year (add back) |
| 8290 | Other income (grants, subsidies, recoveries) |
| 8299 | Gross business income (sum of above) |

### Part 4 -- Cost of Goods Sold (if applicable)

| Line | Description |
|------|-------------|
| 8300 | Opening inventory |
| 8320 | Purchases during the year (net of personal portion) |
| 8340 | Direct wage costs |
| 8360 | Subcontracts |
| 8450 | Closing inventory |
| 8518 | Cost of goods sold = Opening + Purchases + Wages + Subcontracts - Closing |
| 8519 | Gross profit = Line 8299 - Line 8518 |

### Part 5 -- Net Income (Loss) before Adjustments

| Line | Description |
|------|-------------|
| 9369 | Total business expenses (from expense section below) |
| 9369 | Net income (loss) = Gross profit - Total expenses |

### Part 6 -- Your Net Income (Loss)

Adjustments for personal use, reserves, and other items to arrive at net business income reported on T1 line 13500 (business) or 13700 (professional).

### Part 7 -- Business-Use-of-Home Expenses (see Step 7)

### Part 8 -- Motor Vehicle Expenses (see Step 8)

---

## Step 4: Allowable Business Expenses [T1/T2]

**Legislation:** ITA s. 18(1)(a) -- general limitation; ITA s. 18(1)(h) -- personal/living expenses; ITA s. 67 -- reasonableness

### The Test [T1]

An expense is deductible if it was incurred to **earn business income**, is **reasonable in the circumstances**, and is **not a capital expenditure** (capital items go through CCA). Mixed-use expenses must be apportioned between business and personal.

### Deductible Expenses -- T2125 Lines

| T2125 Line | Expense Category | Tier | Treatment |
|------------|-----------------|------|-----------|
| 8521 | Advertising | T1 | Fully deductible. Canadian newspaper/broadcasting restrictions apply (ITA s. 19). |
| 8523 | Meals and entertainment | T1 | **50% deductible** only (ITA s. 67.1). Long-haul truckers: 80%. |
| 8590 | Bad debts | T2 | Deductible if previously included in income and genuinely uncollectible. Flag for reviewer. |
| 8690 | Insurance (business) | T1 | Fully deductible -- professional liability, property, business interruption. |
| 8710 | Interest and bank charges | T1 | Interest on money borrowed for business purposes. Personal portion excluded. |
| 8760 | Business taxes, licences, memberships | T1 | Fully deductible -- includes professional dues, municipal business licences. |
| 8810 | Office expenses | T1 | Fully deductible -- supplies, postage, stationery, small items. |
| 8811 | Office stationery and supplies | T1 | Fully deductible. |
| 8860 | Professional fees (legal, accounting) | T1 | Fully deductible if related to business operations. |
| 8871 | Management and administration fees | T1 | Fully deductible. |
| 8910 | Rent (business premises) | T1 | Fully deductible for dedicated business premises. |
| 8960 | Repairs and maintenance | T1 | Fully deductible if current expense (not capital improvement). |
| 9060 | Salaries, wages, benefits (to employees) | T1 | Fully deductible. Must issue T4 slips. |
| 9180 | Property taxes (business premises) | T1 | Fully deductible. |
| 9200 | Travel (transportation, lodging) | T1 | Fully deductible if wholly business purpose. Meals while travelling: 50%. |
| 9220 | Telephone and utilities | T1/T2 | Business portion only. Home phone: business % only. Dedicated business line: 100%. |
| 9224 | Fuel costs (except motor vehicle) | T1 | Heating fuel for business premises. |
| 9270 | Delivery, freight, express | T1 | Fully deductible. |
| 9275 | Motor vehicle expenses | T2 | Business portion only -- see Step 8. |
| 9281 | Capital cost allowance (CCA) | T1 | Per CCA schedule -- see Step 5. |
| 9270 | Other expenses | T1/T2 | Catch-all. Must be reasonable and business-related. |

### NOT Deductible [T1]

| Expense | Reason | Legislation |
|---------|--------|-------------|
| Personal or living expenses | Blocked | ITA s. 18(1)(h) |
| Club membership dues (golf, fitness, etc.) | Blocked even if business-related | ITA s. 18(1)(l) |
| Political contributions | Not business expense | ITA s. 18(1)(n) |
| Income tax or penalties paid to CRA | Cannot deduct tax on income | ITA s. 18(1)(t) |
| Capital expenditures (depreciable assets) | Must go through CCA | ITA s. 18(1)(b) |
| Drawings / owner withdrawals | Not an expense -- personal distribution | |
| Fines and penalties (government-imposed) | Blocked | ITA s. 67.6 |
| 50% of meals and entertainment | Only 50% is deductible | ITA s. 67.1 |
| Reserves (in excess of allowed amounts) | Restricted | ITA s. 18(1)(e) |

---

## Step 5: Capital Cost Allowance (CCA) [T1]

**Legislation:** ITA s. 20(1)(a); ITR Part XI, Schedule II

### Common CCA Classes and Rates (Declining Balance Unless Noted)

| Class | Rate | Assets Included |
|-------|------|-----------------|
| 1 | 4% | Buildings acquired after 1987 |
| 6 | 10% | Frame, log, stucco buildings; fences, greenhouses |
| 8 | 20% | Furniture, fixtures, appliances, tools >$500, equipment not elsewhere |
| 10 | 30% | Motor vehicles, automotive equipment, general-purpose electronic data processing equipment (pre-March 19, 2007) |
| 10.1 | 30% | Passenger vehicles costing more than prescribed limit ($38,000 before tax for 2025) -- each vehicle in separate class |
| 12 | 100% | Tools, utensils, kitchen equipment <$500; china, linen; computer software (packaged, not custom) |
| 13 | S/L | Leasehold improvements -- straight-line over remaining lease term + first renewal (min 5 yr, max 40 yr) |
| 14 | S/L | Patents, franchises, concessions, licences -- straight-line over remaining legal life |
| 14.1 | 5% | Goodwill and other eligible capital property (post-2016) |
| 43 | 30% | Manufacturing and processing machinery and equipment |
| 44 | 25% | Patents, licences to use patents (acquired after April 26, 1993) |
| 46 | 30% | Data network infrastructure equipment |
| 50 | 55% | General-purpose electronic data processing equipment (computers) acquired after March 18, 2007 |
| 52 | 100% | General-purpose electronic data processing equipment acquired after Jan 27, 2009 and before Feb 2011 (limited) |
| 53 | 50% | Manufacturing and processing machinery (acquired after 2015 and before 2026) |
| 54 | 30% | Zero-emission passenger vehicles (cost limit $61,000 before tax for 2025) |
| 55 | 40% | Zero-emission vehicles that would otherwise be Class 16 |

### Half-Year Rule [T1]

**Legislation:** ITR s. 1100(2)

- In the year a depreciable asset is acquired, only **50% of the net addition** to the class is eligible for CCA (the "half-year rule").
- Net addition = additions - disposals in the class for the year.
- The half-year rule applies to most classes. Exceptions: Class 12 (100%), Class 13, Class 14, Class 52.

### Accelerated Investment Incentive (AccII) [T1]

**Legislation:** ITR s. 1100(2)(a.2); ITA s. 1104(4)

| Period | Treatment |
|--------|-----------|
| Property available for use before 2024 | AccII applied: first-year CCA on 1.5x the net addition (effectively suspending the half-year rule and providing an enhanced deduction) |
| Property available for use in 2024-2025 | AccII continues at 1.5x for most classes |
| Property available for use in 2026-2027 | AccII reduced to 1.25x |
| Property available for use after 2027 | AccII expires; standard half-year rule applies |
| Classes 43.1, 43.2, 53 (M&P) | Full expensing (100% first-year writeoff) if available for use before 2026; not subject to AccII but to separate immediate expensing rules |
| Class 54, 55 (zero-emission vehicles) | Enhanced first-year: 1.5x for 2024-2025; phasing down after 2025 |

**Status check (2025):** AccII remains active for property becoming available for use in 2025. Bill C-15 (tabled November 2025) reinstates/extends accelerated CCA and immediate expensing for certain classes. Confirm with current legislation before applying.

### Immediate Expensing (Individuals) [T1]

**Legislation:** ITA s. 1100(0.1); ITR s. 1100(2)(a.3)

- For tax years ending after April 18, 2021 and before 2025: eligible individuals (sole proprietors) could immediately expense up to $1.5M of eligible property per year.
- For tax year 2025: the $1.5M immediate expensing for individuals has **expired** as of January 1, 2024. Standard CCA rules and AccII apply.
- [T2] Flag for reviewer if client asks about immediate expensing -- confirm whether any extension has been enacted.

### CCA Computation Rules [T1]

1. Group assets by CCA class
2. Opening UCC (undepreciated capital cost) = prior year UCC
3. Add: acquisitions during the year (capital cost of additions)
4. Subtract: lesser of (proceeds of disposition, original capital cost) for assets disposed
5. If result is negative: recapture (include in income)
6. If class is empty and UCC > 0: terminal loss (deduct from income)
7. Apply half-year rule (or AccII) to net additions
8. Compute CCA = rate x adjusted UCC base
9. CCA claimed may be any amount from $0 to the maximum -- it is discretionary
10. Closing UCC = Opening UCC + Additions - Disposals - CCA claimed

### Class 10.1 Special Rules [T1]

| Rule | Detail |
|------|--------|
| Cost limit (2025) | $38,000 before tax (GST/HST) |
| Separate class | Each Class 10.1 vehicle is its own class |
| No terminal loss | When disposed, no terminal loss or recapture |
| No recapture | Deemed disposition at cost = proceeds |
| Half-year in year of disposal | CCA allowed at 50% in the year of disposition |
| AccII applies | 1.5x in first year (2024-2025) |

---

## Step 6: GST/HST Interaction with Business Expenses [T1]

**Legislation:** Excise Tax Act (ETA); ITA s. 248(16); CRA Guide RC4022

### Small Supplier Threshold [T1]

| Item | Amount |
|------|--------|
| Small supplier threshold | $30,000 in taxable supplies over 4 consecutive calendar quarters |
| Consequence of exceeding | Must register for GST/HST within 29 days |
| Below threshold | Registration is optional (voluntary registration allows ITCs) |

### GST/HST and Expense Deductions [T1]

| Scenario | Income Tax Treatment |
|----------|---------------------|
| GST/HST registrant -- ITC claimed on expense | Deduct only the **net** (pre-tax) amount of the expense. The ITC recovers the GST/HST, so it is not a cost. |
| GST/HST registrant -- ITC NOT claimed (blocked) | Deduct the **gross** amount including GST/HST. Blocked ITCs: meals (50% ITC only), personal-use portion, exempt supplies. |
| GST/HST registrant -- Quick Method | Deduct the **gross** amount of expenses (no ITCs claimed except on capital property). |
| NOT registered (small supplier) | Deduct the **gross** amount of expenses including GST/HST paid. No ITCs available. |

### ITA s. 248(16) -- GST/HST Rebate/Refund Adjustment [T1]

When a GST/HST registrant claims ITCs, the cost of the asset or expense for income tax purposes is reduced by the ITC amount. This happens automatically if you record expenses net of GST/HST recovered.

### GST/HST on Revenue [T1]

- GST/HST collected is NOT business income. Exclude from T2125 line 8000.
- If using Quick Method: net GST/HST remitted is included in income (the difference between GST/HST collected and the reduced remittance is taxable income).

---

## Step 7: Business-Use-of-Home Expenses (T2125 Part 7) [T2]

**Legislation:** ITA s. 18(12)

### Eligibility Conditions [T1]

The home workspace must meet **one** of these two conditions:

1. It is your **principal place of business** (i.e., more than 50% of business is conducted there), OR
2. You use the workspace **exclusively** for earning business income AND you use it on a **regular and continuous basis** for meeting clients/customers.

If neither condition is met, no home office deduction is allowed.

### Deductible Home Expenses [T2]

| Expense | Renter | Owner | Apportionment |
|---------|--------|-------|---------------|
| Rent | Yes | N/A | Business % |
| Mortgage interest | N/A | Yes | Business % |
| Property taxes | N/A | Yes | Business % |
| Home insurance | Yes | Yes | Business % |
| Electricity | Yes | Yes | Business % |
| Heat (gas, oil, etc.) | Yes | Yes | Business % |
| Water | Yes | Yes | Business % |
| Internet | Yes | Yes | Business % |
| Maintenance and repairs (common areas) | Yes | Yes | Business % |
| Condo fees | Yes | N/A | Business % |

### Apportionment Method [T2]

- **Reasonable basis:** area of workspace / total area of home (square footage method is most common)
- Alternative: number of rooms used for business / total rooms (acceptable if rooms are similar size)
- [T2] Flag for reviewer: confirm the proportion claimed is reasonable and workspace genuinely meets the eligibility test

### Limitation [T1]

- Home office expenses **cannot create or increase a business loss** (ITA s. 18(12))
- Unused home office expenses carry forward to the next year (indefinitely) and can be applied against future business income from the same business
- CCA on the home is technically deductible but is **strongly discouraged** -- claiming CCA on a principal residence may trigger recapture on sale and jeopardize the principal residence exemption (ITA s. 40(2)(b))

### What Goes Where [T1]

Home office expenses are calculated in Part 7 of T2125 and then carried to the expense section. They are separate from rent on dedicated business premises (line 8910).

---

## Step 8: Motor Vehicle Expenses (T2125 Part 8) [T2]

**Legislation:** ITA s. 18(1)(r); ITR s. 7306; ITA s. 67.2, 67.3, 67.4

### Prescribed Limits (2025) [T1]

| Item | 2025 Limit |
|------|-----------|
| Class 10.1 passenger vehicle cost ceiling | $38,000 (before tax) |
| Class 54 zero-emission vehicle cost ceiling | $61,000 (before tax) |
| Deductible monthly lease cost ceiling | $1,050/month |
| Deductible interest on auto loan | $350/month |
| Tax-exempt per-km allowance -- first 5,000 km | $0.72/km |
| Tax-exempt per-km allowance -- additional km | $0.66/km |
| Tax-exempt per-km allowance (Yukon, NWT, Nunavut) -- first 5,000 km | $0.76/km |

### Kilometre Log Requirement [T1]

**CRA requires a detailed log for any motor vehicle expense claim.** The log must record:

| Field | Detail |
|-------|--------|
| Date of each trip | Day/month/year |
| Destination | Where you drove |
| Purpose | Business reason for the trip |
| Kilometres driven | For each trip |
| Odometer readings | At the start and end of the fiscal period |
| Total km for the year | Business km + personal km |

**No log = no claim.** CRA will disallow motor vehicle expenses on audit if no contemporaneous log is maintained.

### Deductible Motor Vehicle Expenses [T2]

| Expense | Treatment |
|---------|-----------|
| Fuel and oil | Business % of total |
| Insurance | Business % of total |
| Licence and registration | Business % of total |
| Maintenance and repairs | Business % of total |
| Lease payments | Business % of total (subject to lease ceiling) |
| Interest on auto loan | Business % of total (subject to interest ceiling) |
| Parking (business) | 100% deductible (not subject to business % -- specific to business trips) |
| Supplementary business insurance | 100% if business-only |
| CCA | Business % of CCA claimed on the vehicle |

### Business Percentage Calculation [T1]

Business % = Total business kilometres / Total kilometres driven in the fiscal period

### Motor Vehicle vs Passenger Vehicle [T1]

| Type | Definition | CCA Class |
|------|-----------|-----------|
| Motor vehicle | Designed to carry people/goods on streets; excludes vehicles designed to carry >8 passengers, ambulances, hearses, vans/pickup trucks used >50% for goods transport | Class 10 (30%) |
| Passenger vehicle | Motor vehicle designed to carry individuals on streets; includes most cars and SUVs. Pickups/vans that seat <3 and are used >50% for goods/equipment transport are excluded | Class 10 or 10.1 if over cost ceiling |

---

## Step 9: Net Income Computation Summary [T1]

| Step | Description | T2125 Lines |
|------|-------------|-------------|
| 1 | Gross business income | 8299 |
| 2 | Less: Cost of goods sold (if applicable) | 8518 |
| 3 | = Gross profit | 8519 |
| 4 | Less: Total business expenses (Steps 4-8) | 9369 |
| 5 | = Net income (loss) before adjustments | 9369 |
| 6 | Add back: personal-use portion of expenses | |
| 7 | Add back: reserves from prior year | |
| 8 | Less: current year reserves | |
| 9 | = Net business income (loss) | Line 13500 (business) or 13700 (professional) on T1 |

**This figure flows to the T1 return.** Business income goes to T1 line 13500 (or 13700 for professional income). Business losses can offset other income in the year or be carried back 3 years / forward 20 years (ITA s. 111).

---

## Step 10: Filing Requirements and Deadlines [T1]

**Legislation:** ITA s. 150(1)(d)

| Item | Deadline |
|------|----------|
| T1 filing deadline (self-employed) | June 15 of the following year |
| Balance owing deadline | April 30 of the following year (even though return is due June 15) |
| Penalty for late filing | 5% of balance owing + 1% per month (max 12 months) |
| Repeated late filing | 10% of balance owing + 2% per month (max 20 months) |
| Interest on balance owing | Prescribed rate, compounded daily |
| Instalment payments | Quarterly (March 15, June 15, Sept 15, Dec 15) if net tax owing exceeds $3,000 in current year AND either of the two prior years |

**CRITICAL:** While self-employed individuals have until June 15 to FILE, any balance owing accrues interest from **April 30**. The filing extension does not extend the payment deadline.

---

## Step 11: Record Keeping [T1]

**Legislation:** ITA s. 230(1)

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 6 years from the end of the last tax year they relate to |
| What to keep | All sales invoices, purchase receipts, bank statements, contracts, loan agreements, motor vehicle log, asset register |
| Format | Paper or electronic (CRA accepts digital records if complete and accessible) |
| CRA can request | Books and records must be available for inspection at any time |
| Failure to keep records | Penalty up to $2,500 per offence (ITA s. 162(6)) |

---

## Step 12: Edge Case Registry

### EC1 -- GST/HST collected included in business income [T1]
**Situation:** GST/HST registrant reports gross revenue of $113,000 which includes $13,000 GST/HST collected from clients.
**Resolution:** Line 8000 must show $100,000 only. The $13,000 GST/HST collected is a liability to CRA, not business income. Remove before computing net income.

### EC2 -- Non-registrant (small supplier) expense treatment [T1]
**Situation:** Sole proprietor below $30,000 threshold buys $1,000 of office supplies + $130 HST = $1,130 total.
**Resolution:** Full $1,130 is the deductible expense. No ITC is available since the proprietor is not GST/HST registered.

### EC3 -- Meals and entertainment over-deducted [T1]
**Situation:** Client deducts $4,000 in business meals at 100%.
**Resolution:** Only $2,000 is deductible (50% limitation under ITA s. 67.1). Reduce the expense by $2,000.

### EC4 -- Club membership dues [T1]
**Situation:** Client deducts $3,000 annual golf club membership claiming it is for client entertainment.
**Resolution:** NOT deductible under any circumstances. ITA s. 18(1)(l) blocks club dues regardless of business purpose.

### EC5 -- Capital item expensed directly [T1]
**Situation:** Client buys a $3,000 laptop and deducts it as office expense on line 8810.
**Resolution:** INCORRECT. The laptop is a capital asset (Class 50, 55% rate). Must be removed from expenses and added to the CCA schedule. First-year CCA (with AccII 2025): approximately $3,000 x 55% x 1.5 = $2,475 (or standard half-year: $3,000 x 55% x 50% = $825). Apply applicable rule.

### EC6 -- Home office creates a loss [T1]
**Situation:** Business income before home office expenses is $2,000. Home office expenses total $5,000.
**Resolution:** Home office expenses are limited to $2,000 (cannot create or increase a loss per ITA s. 18(12)). The remaining $3,000 carries forward to the next year.

### EC7 -- No motor vehicle log [T1]
**Situation:** Client claims 70% business use of vehicle but has no kilometre log.
**Resolution:** CRA will likely disallow the entire claim on audit. Advise client to start a log immediately. For the current year, [T2] flag for reviewer -- the claim cannot be confidently supported without a log.

### EC8 -- Class 10.1 vehicle disposed [T1]
**Situation:** Client sells a passenger vehicle that was in Class 10.1 (original cost $45,000, entered at prescribed limit $38,000).
**Resolution:** No recapture and no terminal loss applies to Class 10.1. In the year of disposition, CCA at 50% of the declining balance is allowed. The class is then closed with no further tax consequences.

### EC9 -- CCA on principal residence [T2]
**Situation:** Client working from home wants to claim CCA on the home office portion of their house.
**Resolution:** [T2] Flag for reviewer. While technically permitted, claiming CCA on a principal residence may trigger a recapture inclusion on sale and partially disqualify the principal residence exemption. Most advisors recommend AGAINST claiming CCA on the home. Deduct other home office expenses only.

### EC10 -- Quick Method GST/HST and income [T1]
**Situation:** Client uses the GST/HST Quick Method. They collected $5,250 GST on $105,000 revenue (5% GST province) and remit only $3,780 (3.6% quick method rate on $105,000).
**Resolution:** The difference of $1,470 ($5,250 - $3,780) is additional business income and must be included on line 8290 of T2125. Revenue line 8000 = $105,000 (excluding GST). Line 8290 includes the $1,470 Quick Method benefit.

### EC11 -- Fiscal year not December 31 [T2]
**Situation:** Client has historically used a March 31 fiscal year end with a T1139 election.
**Resolution:** [T2] Flag for reviewer. The additional business income calculation under ITA s. 34.1 must be computed. This adds an amount to the T1 representing the estimated income from April 1 to December 31. This is complex; confirm the T1139 is filed and the stub-period income estimate is reasonable.

### EC12 -- Mixing personal and business vehicle expenses [T2]
**Situation:** Client has one vehicle used for both business and personal. Claims 80% business use.
**Resolution:** [T2] Verify with kilometre log. An 80% business-use claim is high for a sole vehicle. Flag for reviewer to confirm the log supports the percentage and the claim is reasonable.

---

## Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: CPA/CA must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to CPA/CA. Document gap.
```

---

## Step 14: Test Suite

### Test 1 -- Standard sole proprietor, service business
**Input:** Sole proprietor, graphic designer. Gross revenue $95,000. Expenses: advertising $2,000, office supplies $1,500, software subscriptions $3,600, professional fees $2,500, internet (75% business) $1,200 x 75% = $900, meals with clients $2,000 (50% = $1,000). No COGS. CCA: laptop Class 50 acquired in 2025, cost $2,800, AccII applies (1.5x). GST/HST registrant (ITCs claimed, expenses recorded net).
**Expected:** Gross income = $95,000. Total expenses = $2,000 + $1,500 + $3,600 + $2,500 + $900 + $1,000 = $11,500. CCA: $2,800 x 55% x 1.5 = $2,310. Total deductions = $11,500 + $2,310 = $13,810. Net business income = $95,000 - $13,810 = $81,190 to T1 line 13500.

### Test 2 -- Home office limitation
**Input:** Sole proprietor, net business income before home office = $3,500. Home office expenses: rent $1,200/mo x 20% = $2,880. Insurance $100/mo x 20% = $240. Internet $100/mo x 20% = $240. Utilities $200/mo x 20% = $480. Total home office = $3,840.
**Expected:** Home office deduction limited to $3,500 (cannot create a loss). Carry forward $340 to next year. Net business income = $0.

### Test 3 -- Motor vehicle expense
**Input:** Sole proprietor. Vehicle cost $32,000 (Class 10, under $38,000 limit). Total km: 25,000. Business km: 18,000. Business % = 72%. Fuel $4,500. Insurance $2,400. Repairs $800. Licence $120. CCA on vehicle (first year, AccII): $32,000 x 30% x 1.5 = $14,400. Total vehicle operating = $7,820 x 72% = $5,630. CCA business portion = $14,400 x 72% = $10,368.
**Expected:** Total motor vehicle expense on T2125 = $5,630 + $10,368 = $15,998.

### Test 4 -- GST/HST Quick Method income inclusion
**Input:** Revenue $80,000 (5% GST province). GST collected $4,000. Quick Method rate 3.6%. Remittance = $80,000 x 1.05 x 3.6% = $3,024. Difference = $4,000 - $3,024 = $976.
**Expected:** T2125 line 8000 = $80,000. Line 8290 includes $976 Quick Method benefit. Gross income = $80,976.

### Test 5 -- Capital item incorrectly expensed
**Input:** Client includes $6,000 desk + chair as office expense.
**Expected:** Remove $6,000 from line 8810. Add to CCA Class 8 (20%). First-year CCA with AccII: $6,000 x 20% x 1.5 = $1,800. Net effect: expenses decrease by $6,000, CCA increases by $1,800. Net income increases by $4,200 compared to the incorrect treatment.

### Test 6 -- Non-registrant expense recording
**Input:** Small supplier (not GST/HST registered). Buys printer for $565 (including $65 HST).
**Expected:** Full $565 is the cost for income tax purposes. If capital asset, $565 enters CCA schedule. If expensed (under $500 net -- but gross is $565, so capitalize under Class 8 or 50 depending on type). [T2] Flag: confirm whether this is a capital asset or current expense given the gross amount.

---

## PROHIBITIONS

- NEVER include GST/HST collected on sales in business income (line 8000) for a regular GST/HST registrant
- NEVER deduct meals and entertainment at more than 50% (unless long-haul trucker exception applies)
- NEVER allow club membership dues as a deduction under any circumstances
- NEVER allow fines, penalties, or income tax as deductions
- NEVER expense capital assets directly -- they must go through CCA
- NEVER allow home office expenses to create or increase a business loss
- NEVER support a motor vehicle expense claim without a kilometre log
- NEVER recommend claiming CCA on a principal residence without flagging the principal residence exemption risk
- NEVER use a fiscal year end other than December 31 without confirming a valid T1139 election
- NEVER present figures as final -- always label as estimated and direct client to their CPA/CA for sign-off
- NEVER apply AccII rates without confirming the property was acquired in a year where AccII is active
- NEVER compute tax liability directly -- pass net business income to the T1 return skill for tax computation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
