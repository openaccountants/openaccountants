---
name: us-schedule-c-and-se-computation
description: Tier 2 content skill for computing Schedule C bottom line, Form 8829 home office (actual method), and Schedule SE self-employment tax for US sole proprietors and single-member LLCs disregarded for federal tax. Covers tax year 2025 with the 2025 Social Security wage base of $176,100, the 92.35% net SE earnings adjustment under §1402(a)(12), the 12.4% OASDI rate, the 2.9% Medicare rate, and the 0.9% Additional Medicare Tax thresholds. Handles Schedule C Lines 1-32, the §280A home office gross income limitation and carryover, Form 8829 indirect expense allocation, the §1402 net SE earnings computation, the optional methods under §1402(a)(15) and §1402(l), the deductible half of SE tax under §164(f), and the at-risk indicators on Line 32. Consumes classified transactions from us-sole-prop-bookkeeping. Defers QBI, retirement, SE health insurance, and quarterly estimated tax to companion skills. MUST be loaded alongside us-tax-workflow-base v0.1+. Federal only.
version: 0.2
---

# US Schedule C and SE Computation Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It computes the bottom-line Schedule C numbers, the Form 8829 home office deduction (actual method), and the Schedule SE self-employment tax for tax year 2025. It does not classify transactions — that comes from `us-sole-prop-bookkeeping`. It does not compute QBI, retirement contributions, self-employed health insurance, or quarterly estimated tax — those are separate content skills.

**Where this skill fits in the pipeline:**

```
Bank statement / source data
        ↓
us-sole-prop-bookkeeping (classifies every transaction into a Schedule C line)
        ↓
us-schedule-c-and-se-computation (THIS SKILL — aggregates, runs Form 8829, computes net profit, computes SE tax)
        ↓
us-form-1040-self-employed-positions (QBI, SE health insurance, retirement, OBBBA personal deductions)
        ↓
us-quarterly-estimated-tax (safe harbor for following year)
```

This skill is the second step in the chain. It assumes the bookkeeping skill has run successfully and produced classified totals for Lines 1 through 27b. Its job is to compute Lines 28 through 32, the Form 8829 detail (if actual method is used for home office), and the full Schedule SE.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). Year-specific figures are independently verified against Notice 2024-80 (retirement limits referenced for context), the Social Security Administration's 2025 wage base announcement, and IRC sections in force for 2025.

**The reviewer is the customer of this output.** The skill produces a computation worksheet and a brief that the reviewing Enrolled Agent or CPA can audit and sign off on. The skill does not file anything.

---

## Section 1 — Scope statement

This skill covers, for tax year 2025:

- **Schedule C aggregation** — Lines 1 through 7 (income), Line 28 (total expenses), Line 29 (tentative profit), Line 30 (home office deduction), Line 31 (net profit or loss), Line 32 (at-risk indicators)
- **Form 8829 computation** — for taxpayers using the actual home office method, including the gross income limitation under §280A(c)(5) and the carryover of disallowed expenses
- **Simplified home office method** — for taxpayers using the simplified method under Rev. Proc. 2013-13, computing the deduction directly without Form 8829
- **Schedule SE Part I** — net SE earnings, the 92.35% adjustment, the SE tax computation (OASDI + Medicare + Additional Medicare Tax), the deductible half flowing to Schedule 1
- **Schedule SE Part II optional methods** — farm and nonfarm optional methods under §1402(a)(15) and §1402(l), where applicable for low-income taxpayers
- **At-risk and basis indicators** — flagging Schedule C Line 32a (all investment is at risk) vs Line 32b (some investment is not at risk), with Form 6198 referral if needed

This skill does NOT cover:

- Transaction classification — handled by `us-sole-prop-bookkeeping` (upstream)
- The QBI deduction — handled by `us-form-1040-self-employed-positions` (downstream)
- Self-employed health insurance deduction — handled by `us-form-1040-self-employed-positions` (downstream)
- Self-employed retirement contribution computation — handled by `us-form-1040-self-employed-positions` (downstream)
- Quarterly estimated tax computation — handled by `us-quarterly-estimated-tax` (downstream)
- The new OBBBA personal deductions (qualified tips, qualified overtime, auto loan interest, senior) — these flow through Schedule 1-A on the personal side, handled by `us-form-1040-self-employed-positions`
- Any state tax — out of scope for the entire US tax stack
- Form 1040 line items beyond Schedule 1 line 15 (deductible half of SE tax) and Line 23 (SE tax itself flows through Schedule 2) — those are personal-return line items handled in `us-form-1040-self-employed-positions`

---

## Section 2 — Year coverage and currency

**Tax year covered:** 2025 (returns due April 15, 2026, or October 15, 2026 with extension).

**Currency date:** April 2026.

**Legislation reflected:**
- Internal Revenue Code as in force for tax year 2025
- One Big Beautiful Bill Act (P.L. 119-21, July 4 2025) — note: OBBBA did NOT change Schedule SE mechanics, the 92.35% adjustment, the OASDI / Medicare rates, or the §280A home office structure. OBBBA's effects on this skill are limited to the depreciation rules that flow into Form 8829's home depreciation component (only relevant for actual-method taxpayers who elect home depreciation, which is uncommon).
- SECURE 2.0 provisions in effect for 2025 (referenced for context only — retirement contributions are computed downstream)
- Treasury Regulations as in force for tax year 2025
- IRS Publications updated for tax year 2025 (Pub 334, 587, 535 historical content, 946)
- Form Instructions for tax year 2025 (Schedule C, Schedule SE, Form 8829, Form 6198)

**Currency limitations:**
- The 2025 inflation-adjusted figures (Social Security wage base, retirement limits) come from the 2024 announcements (SSA Press Release October 2024; Notice 2024-80 for retirement plans). These were settled before OBBBA and were not changed by it.
- The Additional Medicare Tax thresholds ($200K single, $250K MFJ, $125K MFS) are statutory under §3101(b)(2) / §1401(b)(2) and are NOT indexed for inflation. They have been the same since enacted in 2013.
- The $400 minimum SE earnings threshold is statutory under §1402(b)(2) and is NOT indexed.

---

## Section 3 — Year-specific figures table for tax year 2025

All dollar thresholds, rates, percentages, and figures the skill relies on, with primary source citations.

### Self-employment tax core figures

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Net SE earnings adjustment factor | 92.35% | IRC §1402(a)(12); Schedule SE Instructions (2025) |
| OASDI (Social Security) tax rate | 12.4% | IRC §1401(a) |
| Medicare tax rate | 2.9% | IRC §1401(b)(1) |
| Social Security wage base | $176,100 | SSA Annual Announcement (October 2024); IRC §1402(b)(1) referencing §3121(a)(1) |
| Combined OASDI + Medicare base SE tax rate | 15.3% | IRC §1401(a) + §1401(b)(1) |
| Additional Medicare Tax rate | 0.9% | IRC §1401(b)(2); IRC §3101(b)(2) |
| Additional Medicare Tax threshold (single, HoH, QSS) | $200,000 | IRC §3101(b)(2)(C); statutory, NOT indexed |
| Additional Medicare Tax threshold (MFJ) | $250,000 | IRC §3101(b)(2)(A); statutory, NOT indexed |
| Additional Medicare Tax threshold (MFS) | $125,000 | IRC §3101(b)(2)(B); statutory, NOT indexed |
| Minimum net SE earnings to trigger SE tax | $400 | IRC §1402(b)(2); statutory, NOT indexed |
| Church employee income special threshold | $108.28 | IRC §1402(j)(2)(B); statutory |
| Deductible portion of SE tax | 50% | IRC §164(f); flows to Schedule 1 line 15 |

### Schedule SE optional methods (for low-income taxpayers)

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Maximum SE earnings under farm optional method | $7,320 | IRC §1402(a)(14) and §1402(l); inflation-adjusted; equals 2 × Social Security minimum credit thresholds |
| Nonfarm optional method gross income threshold | $10,380 minimum gross | IRC §1402(l)(2)(A); see Schedule SE Instructions |
| Nonfarm optional method profit threshold | < $7,320 net AND < 72.189% of gross | IRC §1402(l) |
| Nonfarm optional method maximum SE earnings | $7,320 | IRC §1402(l) |
| Nonfarm optional method 5-year limit | Yes | IRC §1402(l)(3) |

(Note: the optional method figures change annually with Social Security indexing. The 2025 figures are based on 4 quarters of coverage at $1,830 each. Confirm against Schedule SE Instructions (2025) before relying.)

### Schedule SE / Schedule C interaction figures

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Self-employment income flows to | Schedule 1 line 3 (business income) | Form 1040 Instructions (2025) |
| SE tax flows to | Schedule 2 line 4 | Form 1040 Instructions (2025) |
| Deductible half of SE tax flows to | Schedule 1 line 15 | Form 1040 Instructions (2025); IRC §164(f) |

### Form 8829 home office (actual method) figures

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| §280A(c)(5) gross income limitation | Yes | IRC §280A(c)(5); deduction cannot exceed gross income from the business minus other business deductions |
| Carryover of disallowed expenses | Yes | IRC §280A(c)(5); Form 8829 lines 43-44 |
| Depreciation method for home (residential rental property held for business use) | Straight-line, mid-month convention, 39-year recovery | IRC §168(c); Pub 587 (2025); Form 8829 Instructions (2025) |
| Depreciable basis | Lesser of adjusted basis or FMV at conversion to business use, allocated to business-use percentage | Pub 587 (2025) |

### Simplified home office method figures (for cross-reference; primary source same as bookkeeping skill)

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| Simplified method rate | $5.00 per square foot | Rev. Proc. 2013-13 |
| Simplified method square footage cap | 300 sq ft | Rev. Proc. 2013-13 |
| Simplified method maximum deduction | $1,500 | Derived |
| Simplified method gross income limitation | Yes | Rev. Proc. 2013-13 §4.10; Pub 587 (2025) |
| Simplified method carryover | NO carryover allowed | Rev. Proc. 2013-13 §4.10 |

### At-risk and basis figures

| Figure | Value for TY2025 | Primary source |
|---|---|---|
| At-risk threshold | At-risk amount equals taxpayer's investment + recourse debt | IRC §465 |
| Form 6198 required when | Loss is generated AND any investment is not at risk | IRC §465; Form 6198 Instructions (2025) |

---

## Section 4 — Primary source library

Sources cited by this skill, in addition to those in `us-sole-prop-bookkeeping` (which the reviewer should also have on hand for upstream questions).

### Statute (Internal Revenue Code)

- **IRC §61** — Gross income definition
- **IRC §62(a)(1)** — Trade or business deductions as adjustment to AGI
- **IRC §164(f)** — Deductible half of self-employment tax
- **IRC §168(c)** — Recovery periods (39-year nonresidential real property for home office depreciation)
- **IRC §183** — Activities not engaged in for profit (referenced for net loss context)
- **IRC §195** — Start-up expenditures (referenced for first-year businesses)
- **IRC §280A** — Disallowance of expenses in connection with business use of home
- **IRC §280A(c)(1)** — Exclusive and regular use, principal place of business
- **IRC §280A(c)(5)** — Gross income limitation for home office deductions
- **IRC §280A(g)** — Special rules for personal use exceeding business use (residence rented fewer than 15 days, etc., not relevant to sole prop home office)
- **IRC §465** — At-risk limitations
- **IRC §469** — Passive activity loss limitations (referenced; Schedule C is generally active, not passive)
- **IRC §1401** — Rate of tax (self-employment tax)
- **IRC §1401(a)** — OASDI rate (12.4%)
- **IRC §1401(b)(1)** — Medicare rate (2.9%)
- **IRC §1401(b)(2)** — Additional Medicare Tax (0.9%)
- **IRC §1402** — Net earnings from self-employment definition
- **IRC §1402(a)** — Net earnings from self-employment, including the §1402(a)(12) 92.35% adjustment
- **IRC §1402(a)(12)** — The deduction equivalent to half of SE tax in computing net earnings (the source of the 92.35% factor: 1 − 7.65% = 92.35%)
- **IRC §1402(a)(14)** — Farm optional method definitions
- **IRC §1402(b)** — Self-employment income
- **IRC §1402(b)(1)** — Wage base reference
- **IRC §1402(b)(2)** — $400 minimum threshold
- **IRC §1402(j)** — Church employee income
- **IRC §1402(l)** — Nonfarm optional method
- **IRC §3101(b)(2)** — Additional Medicare Tax thresholds (statutory, parallel to §1401(b)(2))
- **IRC §3121(a)(1)** — Reference for Social Security wage base
- **IRC §6017** — Self-employment tax returns

### Treasury Regulations

- **Treas. Reg. §1.280A-1, §1.280A-2** — Business use of home
- **Treas. Reg. §1.183-1, §1.183-2** — Hobby loss factors
- **Treas. Reg. §1.465-1 et seq.** — At-risk rules
- **Treas. Reg. §1.1402(a)-1, et seq.** — Net earnings from self-employment
- **Treas. Reg. §1.1402(b)-1** — Self-employment income

### Revenue Procedures and Notices

- **Rev. Proc. 2013-13** — Simplified home office method (referenced; primary application in bookkeeping skill)
- **Rev. Proc. 2024-40** — 2025 inflation adjustments (referenced for context; SE-related figures come from SSA, not Rev. Proc.)
- **SSA Press Release (October 2024)** — 2025 Social Security wage base ($176,100)

### IRS Publications

- **Pub 334 (2025)** — Tax Guide for Small Business
- **Pub 587 (2025)** — Business Use of Your Home
- **Pub 946 (2025)** — How to Depreciate Property (for home depreciation under actual method)
- **Pub 525 (2025)** — Taxable and Nontaxable Income (referenced)

### Form Instructions

- **Schedule C (Form 1040) Instructions (2025)** — Lines 1 through 32
- **Schedule SE (Form 1040) Instructions (2025)** — Self-employment tax computation, optional methods
- **Form 8829 Instructions (2025)** — Expenses for Business Use of Your Home
- **Form 6198 Instructions (2025)** — At-Risk Limitations
- **Form 1040 Instructions (2025)** — How Schedule C and Schedule SE flow to the personal return

### Court decisions

- **Commissioner v. Soliman, 506 U.S. 168 (1993)** — Principal place of business test (largely superseded by 1997 §280A(c)(1) amendment)
- **Welch v. Helvering, 290 U.S. 111 (1933)** — "Ordinary and necessary" standard (referenced for context)

---

## Section 5 — The Schedule C aggregation rules (Lines 1 through 32)

Once `us-sole-prop-bookkeeping` has classified every transaction, this skill aggregates the line totals and computes the bottom line. The rules:

### Lines 1 through 7 — Income

**Line 1 — Gross receipts or sales.**
Sum of all classified business income transactions. Includes:
- Cash and check receipts from clients/customers
- ACH and wire deposits from clients
- Payment processor payouts (Stripe, Square, PayPal — gross receipts before processor fees, since fees are an expense on Line 27b)
- Form 1099-K reported amounts (cross-check with payment processor data)
- Form 1099-NEC and 1099-MISC reported amounts (cross-check with deposits)

Excludes:
- Transfers from owner's personal accounts (capital contributions, not income)
- Loan proceeds (debt, not income)
- Refunds of business expenses (offset against the original expense, not income)
- Sales tax collected from customers (unless the business is on the gross method, in which case collected sales tax is gross receipts AND a deduction on Line 23 — net effect zero)

**Reconciliation requirement:** The skill cross-references gross receipts on Line 1 against any 1099-NEC, 1099-MISC, or 1099-K forms the taxpayer received. A material discrepancy (deposits less than 1099 totals) is a reviewer attention flag — the IRS computer-matches these and underreporting is a high-audit risk.

**Line 2 — Returns and allowances.**
Refunds issued to customers, chargebacks, sales credits. Captured by the bookkeeping skill as a separate transaction type (refund issued, not a personal transfer).

**Line 3 — Subtract line 2 from line 1.** Mechanical.

**Line 4 — Cost of goods sold (from line 42).** Comes from Part III. Zero for service businesses without inventory.

**Line 5 — Gross profit.** Line 3 minus line 4. Mechanical.

**Line 6 — Other income.** Includes state fuel tax credits, interest on business accounts (sometimes; depends on classification), recapture of prior depreciation, etc. Generally small or zero for sole props.

**Line 7 — Gross income.** Line 5 plus line 6. This is the figure used in the §280A(c)(5) gross income limitation for home office deductions.

### Lines 8 through 27b — Expenses

These come directly from the bookkeeping skill's classification. The aggregation is mechanical: sum all transactions classified to each line. The skill verifies:

1. **Every line has the correct sum** computed from the underlying transactions.
2. **No transaction appears in two lines** (cross-check).
3. **No classified transaction is missing from the aggregation** (count check: classified transaction count = sum of per-line counts).
4. **Default-applied flags carry through** — every transaction with a default flag in the bookkeeping working paper is reflected in the brief's "Conservative defaults applied" section with its dollar effect.

### Line 28 — Total expenses

Sum of Lines 8 through 27b. Mechanical.

### Line 29 — Tentative profit

Line 7 minus Line 28. This is the profit BEFORE the home office deduction. The §280A gross income limitation uses this number (more precisely, it uses gross income from the business reduced by all OTHER business deductions — so Line 7 minus Line 28 in practice equals the tentative profit, which is what's available to absorb a home office deduction).

### Line 30 — Expenses for business use of your home

This is where Form 8829 (actual method) or the simplified method enters the computation. Section 6 below covers the home office computation in detail.

The number on Line 30 cannot exceed Line 29 (the §280A(c)(5) gross income limitation). If the home office deduction would exceed Line 29, the deduction is capped at Line 29 and the excess is either carried over (actual method) or lost (simplified method).

### Line 31 — Net profit or loss

Line 29 minus Line 30. This is the bottom line that flows to:
- Schedule 1 line 3 (business income on the personal return)
- Schedule SE line 2 (net earnings from self-employment, before the 92.35% adjustment)
- The QBI computation (handled in `us-form-1040-self-employed-positions`)

If Line 31 is a loss (negative), additional considerations apply:
- The at-risk rules under §465 may limit the loss
- The hobby loss rules under §183 may disallow the loss entirely (flagged by the bookkeeping skill if there's a 3+ year loss streak)
- An NOL may be generated, triggering R-US-NOL (refusal under base catalogue) and R-BOOK-NOL (refusal under bookkeeping skill catalogue)

### Line 32 — At-risk indicator

Line 32a: All investment is at risk.
Line 32b: Some investment is not at risk (Form 6198 required).

For most sole proprietors, all investment is at risk because they personally fund the business with their own money and recourse debt. Line 32a is the default. Flag for reviewer if:
- The taxpayer has nonrecourse debt financing the business
- The taxpayer has third-party investors or partners (which would also trigger R-US-PARTNERSHIP)
- Any indication that some portion of the investment is shielded from personal liability

If Line 32b would be checked, refer to Form 6198 and flag the at-risk computation as out of scope for this skill (refusal R-COMP-ATRISK).

---

## Section 6 — Form 8829 (actual home office method)

If the taxpayer is using the actual method for home office, this skill computes Form 8829. If the taxpayer is using the simplified method, skip to Section 7.

### Form 8829 structure (2025)

**Part I — Part of Your Home Used for Business**

- **Line 1:** Area used regularly and exclusively for business (square feet)
- **Line 2:** Total area of home (square feet)
- **Line 3:** Business percentage (Line 1 ÷ Line 2, expressed as a percentage)
- **Lines 4-6:** Daycare facility computation (skip; daycare is out of scope)
- **Line 7:** Business percentage (carry from Line 3 unless daycare)

**Part II — Figure Your Allowable Deduction**

- **Line 8:** Gross income from the business use of the home — generally equals Schedule C Line 29 (tentative profit), which represents the income available to absorb the home office deduction under §280A(c)(5)

The next several lines split direct expenses (100% deductible) from indirect expenses (allocated by business percentage):

- **Line 9 (a/b):** Casualty losses (a = direct, b = indirect) — generally not relevant
- **Line 10 (a/b):** Deductible mortgage interest — only the portion attributable to the home; if the taxpayer itemizes on Schedule A, special interaction rules apply
- **Line 11 (a/b):** Real estate taxes — same interaction with Schedule A
- **Line 12:** Add lines 9-11
- **Line 13:** Multiply line 12 column (b) by line 7 (apply business percentage to indirect)
- **Line 14:** Add line 12 column (a) and line 13 — total mortgage interest, real estate taxes, and casualty allocation
- **Line 15:** Excess mortgage interest (if itemizing on Schedule A would have allowed more than what's allocated to business) — generally rare
- **Line 16:** Excess real estate taxes (similar) — generally rare
- **Line 17 (a/b):** Insurance — homeowner's or renter's insurance allocated by business percentage on indirect; direct (e.g., separate office insurance) on direct
- **Line 18 (a/b):** Rent — for renters, the allocated portion of monthly rent; direct expenses for renting an office area
- **Line 19 (a/b):** Repairs and maintenance — office-specific direct repairs (100%) vs. home-wide indirect (business %)
- **Line 20 (a/b):** Utilities — typically gas, electric, water, sewer, trash; allocated by business %
- **Line 21 (a/b):** Other expenses — security system, lawn care, etc., generally indirect
- **Line 22:** Add lines 17-21
- **Line 23:** Multiply line 22 column (b) by line 7
- **Line 24:** Carryover of operating expenses from prior year (Form 8829 line 43)
- **Line 25:** Add lines 22 column (a), line 23, and line 24
- **Line 26:** Allowable operating expenses — smaller of line 25 or (line 15 minus line 16), bounded by available gross income
- **Line 27:** Limit on excess casualty losses and depreciation — line 15 minus line 26
- **Line 28:** Excess casualty losses (smaller of line 9 column (a)+(b) × business % or line 27)
- **Line 29 (a/b):** Depreciation of home — see depreciation subsection below
- **Line 30:** Carryover of excess casualty losses and depreciation from prior year (line 44)
- **Line 31:** Add lines 28-30
- **Line 32:** Allowable excess casualty losses and depreciation — smaller of line 31 or line 27 minus line 28
- **Line 33:** Add lines 14, 26, and 32
- **Line 34:** Casualty loss portion (if any) flows to Form 4684, not Schedule C
- **Line 35:** Allowable expenses for business use of home (line 33 minus line 34) — flows to Schedule C Line 30

**Part III — Depreciation of Your Home (only if claiming home depreciation)**

- **Line 36:** Smaller of adjusted basis or FMV of home at conversion to business use
- **Line 37:** Value of land (subtracted; land is not depreciable)
- **Line 38:** Basis of building (line 36 minus line 37)
- **Line 39:** Business basis of building (line 38 × business %)
- **Line 40:** Depreciation percentage from Pub 946 tables — for nonresidential real property (which is what business-use portion of a home is treated as for tax purposes), the 2025 first-year depreciation depends on the month placed in service and uses the mid-month convention. For continuing use (not first year), the standard is 2.564% per year (1/39) under the straight-line method.
- **Line 41:** Depreciation allowable (line 39 × line 40)

**Part IV — Carryover of Unallowed Expenses to 2026**

- **Line 43:** Operating expenses (line 25 minus line 26, if positive)
- **Line 44:** Excess casualty losses and depreciation (line 31 minus line 32, if positive)

### The §280A(c)(5) gross income limitation

This is the key limit. Per IRC §280A(c)(5), the home office deduction cannot exceed the gross income from the business use of the home, reduced by all deductible expenses other than the home office deduction itself.

In Schedule C terms: the home office deduction on Line 30 cannot exceed Line 29 (tentative profit). If it would, the deduction is capped at Line 29, Line 31 becomes zero, and the disallowed portion is carried over to next year on Form 8829 lines 43 and 44.

**The ordering rule under §280A(c)(5):** When the limit applies, the categories of expenses are deducted in this order:
1. First, expenses that are otherwise deductible regardless of business use (mortgage interest, real estate taxes, casualty losses) — these are deducted first because they would have been deductible on Schedule A anyway
2. Then, operating expenses (utilities, insurance, repairs, etc.)
3. Then, depreciation

This ordering matters because it preserves depreciation as the LAST item to be limited, which is favorable to the taxpayer (depreciation can be carried forward; the pre-limit items cannot be carried in the same way).

### The carryover

Disallowed home office expenses carry forward indefinitely under §280A(c)(5) but can only be used against future home office gross income, not against other income. Form 8829 tracks the carryover on lines 43 (operating expense carryover) and 44 (depreciation carryover).

If the prior-year Form 8829 had a carryover, it enters this year's Form 8829 on line 24 (operating) and line 30 (depreciation). The bookkeeping skill's intake (slot 18k) asks the user for prior-year carryovers. If no prior-year Form 8829 is available, the skill assumes zero carryover and flags for reviewer.

### Depreciation of the home — the §1250 recapture warning

Taking depreciation on the home under the actual method creates two consequences:

1. **Annual depreciation deduction.** Modest, since the home is depreciated over 39 years straight-line. For a $400K home with $100K land value and a 10% business-use percentage, annual depreciation is roughly $300K × 10% / 39 = $769/year.

2. **Section 1250 recapture on sale.** When the home is eventually sold, the depreciation taken (or "allowed or allowable") must be recaptured as unrecaptured §1250 gain, taxed at a maximum 25% rate. The §121 home sale exclusion does NOT shelter the depreciation recapture portion. This is the single biggest "gotcha" of the actual method, and many sole props don't realize they're trading current-year deduction for future-year recapture.

**The skill flags this prominently** for any taxpayer using the actual method who claims home depreciation. The reviewer should confirm that the taxpayer understands the trade-off.

**Skill default on home depreciation:** The skill computes home depreciation when the actual method is used because Pub 587 says depreciation is "allowed or allowable" — meaning the recapture happens on sale whether or not the taxpayer claims it. Skipping the depreciation does not avoid recapture; it just gives up the current-year deduction without escaping the future tax. Best to claim the depreciation that would be recaptured anyway. Flag this reasoning for the reviewer.

### What the bookkeeping skill provides as input

The bookkeeping skill captures the following Form 8829 inputs in its working paper (Sheet "Form 8829 Detail"):

- Square footage of office (Form 8829 Line 1)
- Total square footage of home (Form 8829 Line 2)
- Annual mortgage interest paid on the home (split between business % and Schedule A)
- Annual real estate taxes (split, with SALT cap interaction noted)
- Annual homeowner's insurance (or renter's insurance)
- Annual rent (for renters)
- Annual utilities (gas, electric, water, sewer, trash, internet)
- Annual home repairs and maintenance (direct vs indirect)
- Date the home was placed in business use (for depreciation)
- Adjusted basis of home at that date (for depreciation)
- FMV at that date (for depreciation, take the lower)
- Land value (subtracted from depreciable basis)
- Prior-year Form 8829 carryovers (lines 43 and 44)

### Conservative defaults for Form 8829

| Ambiguity | Conservative default |
|---|---|
| Square footage of office not measured | Default to a low estimate (e.g., 100 sq ft), flag for measurement |
| Total square footage of home not stated | Default to a high estimate (reduces business %), flag |
| Mortgage interest amount not documented | $0 (no deduction) |
| Real estate taxes not documented | $0 |
| Insurance not documented | $0 |
| Utilities not documented | $0 |
| Home depreciation: basis not documented | $0 depreciation (but flag the §1250 recapture risk anyway) |
| Prior-year carryover not provided | $0 (but flag — may be material if prior years had limitation) |
| Whether the home was used for business the full year | Assume only the months documented; pro-rate down |

### When to switch to the simplified method

If the actual method computation is complex, undocumented, or near the §280A gross income limit, the skill flags whether the simplified method would produce a similar or better result without the recapture risk. The reviewer makes the call — the skill does not automatically switch methods, since the election is the taxpayer's.

Note: per IRS rules, the method can be changed year-to-year. If the simplified method was used last year, actual is permitted this year, and vice versa. There is no lock-in for home office method.

---

## Section 7 — Simplified home office method

If the taxpayer is using the simplified method under Rev. Proc. 2013-13, the computation is simple:

**Deduction = $5 × (smaller of office square feet or 300)**

Maximum: $1,500.

### Gross income limitation under the simplified method

The simplified method is also subject to the §280A(c)(5) gross income limitation. The deduction cannot exceed the gross income from the business use of the home minus other business expenses. In Schedule C terms: cannot exceed Line 29.

**Difference from actual method:** Under the simplified method, if the limit applies, the disallowed portion is **NOT carried over.** It's lost. This is a meaningful difference from the actual method's indefinite carryover.

### What the simplified method does NOT allow

- No depreciation of the home (and consequently no §1250 recapture from simplified-method years)
- No carryover of disallowed expenses
- Itemized deductions for mortgage interest and real estate taxes are NOT reduced by the business-use portion (the taxpayer still claims the full Schedule A amount)

### Form 8829 is NOT required for the simplified method

The deduction is computed directly on a worksheet in the Schedule C Instructions and entered on Schedule C Line 30. The skill produces this worksheet as part of its output.

### Switching between methods

A taxpayer can switch between the simplified method and the actual method from year to year. Each year is a separate election. There is no lock-in.

---

## Section 8 — Schedule SE computation

Once Schedule C Line 31 (net profit or loss) is computed, the skill computes Schedule SE.

### Schedule SE Part I — Self-Employment Tax

**Line 1a — Net farm profit or (loss).** Skip; this skill does not handle farm income.

**Line 1b — Social Security retirement / disability benefits.** Skip.

**Line 2 — Net profit or (loss) from Schedule C line 31.** Carries directly from the Schedule C aggregation.

**Line 3 — Combine lines 1a, 1b, and 2.** For sole props with no farm income, this equals Line 2.

**Line 4a — If line 3 > 0, multiply by 92.35%.** This is the §1402(a)(12) adjustment. The 92.35% factor is derived as 1 − 0.0765, where 0.0765 is half of the 15.3% combined SE tax rate. The mechanics: SE tax is computed on a base that excludes the deductible half of SE tax itself, which is mathematically equivalent to multiplying net SE earnings by 92.35%.

**Line 4b — If using optional methods.** See Section 9 below.

**Line 4c — Combine lines 4a and 4b.** This is the net earnings from self-employment subject to SE tax.

**Line 5a — Church employee income.** Skip.

**Line 5b — Multiply line 5a by 92.35%.** Skip.

**Line 6 — Add lines 4c and 5b.** Equals line 4c for non-church-employee taxpayers.

**Line 7 — Maximum amount of combined wages and self-employment earnings subject to Social Security tax.** $176,100 for 2025.

**Line 8a — Total Social Security wages and tips.** From Form W-2 box 3 if the taxpayer also has W-2 wages from another job. Affects the Social Security portion calculation because the $176,100 cap applies to combined earnings.

**Line 8b — Unreported tips subject to Social Security tax.** Generally zero.

**Line 8c — Wages subject to Social Security tax (RRTA).** Generally zero.

**Line 8d — Add lines 8a, 8b, 8c.** Sum.

**Line 9 — Subtract line 8d from line 7.** This is the remaining Social Security base available for SE earnings. If line 8d already exceeds line 7 (taxpayer earned more than $176,100 in W-2 wages), line 9 is zero and no Social Security portion of SE tax applies — only the Medicare portion.

**Line 10 — Multiply the smaller of line 6 or line 9 by 12.4%.** This is the Social Security portion of SE tax.

**Line 11 — Multiply line 6 by 2.9%.** This is the Medicare portion of SE tax. Note: no cap on Medicare.

**Line 12 — Self-employment tax. Add lines 10 and 11.** This is the base SE tax. Flows to Schedule 2 line 4 on the personal return.

**Line 13 — Deduction for one-half of self-employment tax. Multiply line 12 by 50%.** Per §164(f), half of SE tax is deductible. Flows to Schedule 1 line 15 as an above-the-line deduction.

### Additional Medicare Tax (separate from Schedule SE)

The Additional Medicare Tax under §1401(b)(2) and §3101(b)(2) is **NOT computed on Schedule SE.** It is computed on **Form 8959 (Additional Medicare Tax)** and flows to Schedule 2 line 11.

The Additional Medicare Tax applies to combined earned income (wages + SE earnings) exceeding the threshold for the filing status:
- Single, HoH, QSS: $200,000
- MFJ: $250,000
- MFS: $125,000

The tax is 0.9% on the excess. Form 8959 coordinates withholding (employers withhold the additional 0.9% on wages above $200K regardless of filing status, which may over- or under-withhold depending on actual situation), W-2 wages, and SE earnings.

**This skill flags Form 8959 applicability.** When net SE earnings + W-2 wages (if any) exceed the filing-status threshold, the brief notes that Form 8959 will be required and computes the expected Additional Medicare Tax. The actual Form 8959 mechanics involve coordinating with employer withholding, which the skill flags for reviewer attention rather than computing in full.

### The deductible half of SE tax flows where

The deductible half (Schedule SE line 13) flows to **Schedule 1 line 15** as an adjustment to income. This is NOT a Schedule C expense — it does NOT reduce Schedule C net profit, and it does NOT reduce QBI. It is an above-the-line deduction that reduces AGI directly.

The ordering matters for downstream skills: QBI is computed on a base that includes the SE tax deduction's effect (because QBI references taxable income, which is AGI minus deductions), but the SE tax deduction does not reduce the §1402 net SE earnings used for retirement contribution computation. The interaction is handled by `us-form-1040-self-employed-positions`.

### Common SE tax computation errors to check

The skill self-checks against these common errors:

1. **Forgetting the 92.35% adjustment.** Computing SE tax on the full Schedule C net profit instead of 92.35% of it. Always apply the §1402(a)(12) adjustment.

2. **Wrong wage base year.** Using the prior or next year's Social Security wage base. For 2025, it's $176,100. For 2024 it was $168,600. For 2026 it will be different.

3. **Coordinating with W-2 wages.** If the taxpayer also has W-2 income, the Social Security cap applies to combined earnings. Not coordinating leads to over-payment (the SS portion is double-collected).

4. **Computing Additional Medicare Tax on Schedule SE.** The 0.9% is on Form 8959, not Schedule SE. Schedule SE includes only the base 2.9% Medicare.

5. **Failing the $400 minimum threshold check.** If net SE earnings × 92.35% < $400, no SE tax is due. The taxpayer files Schedule SE only if SE earnings are $400 or more (or church employee income is $108.28 or more).

6. **Net loss handling.** If Schedule C Line 31 is negative, no SE tax is due (the 92.35% of a negative number is still negative, and the SE tax is only on positive earnings). However, the loss does carry to the personal return as a Schedule 1 line 3 negative.

---

## Section 9 — Optional methods for low-income SE earners

The optional methods under IRC §1402(a)(15) (farm) and §1402(l) (nonfarm) allow low-income self-employed individuals to elect to pay more SE tax than they otherwise would, in order to qualify for Social Security credits in years when actual earnings would not.

### Why anyone would do this

Social Security retirement benefits depend on quarters of coverage. Each year, you can earn up to 4 quarters of coverage by having sufficient earnings. For 2025, one quarter requires $1,810 in earnings; four quarters require $7,240. (These figures change annually.)

A self-employed individual whose net earnings are below the 4-quarter threshold can elect an optional method to "buy" credits at the cost of paying SE tax on a higher amount than actual. This is generally only worthwhile for someone close to retirement age trying to fully insure for Social Security benefits, or someone who needs the credits for disability insurance qualification.

For most sole props, the optional methods are NOT used. The skill's default is to skip them unless the taxpayer specifically asks.

### Nonfarm optional method (IRC §1402(l))

Eligible if all of:
1. Net nonfarm earnings (regular method) are less than $7,320 for 2025
2. Net nonfarm earnings are less than 72.189% of gross nonfarm income
3. The taxpayer has had net SE earnings of at least $400 in 2 of the 3 prior years
4. The taxpayer has not used this method more than 5 prior times (lifetime cap)

If eligible and elected, net SE earnings are deemed to be the smaller of:
- Two-thirds of gross nonfarm income, or
- $7,320

### Farm optional method (IRC §1402(a)(15))

Skip — this skill does not handle farm income. Refer to a farm-experienced practitioner.

### When to flag

The skill flags the nonfarm optional method as a planning option if:
- Net SE earnings under the regular method are below $7,320
- The taxpayer is near retirement age (within 10 years of full retirement age)
- The taxpayer's goal is to maximize Social Security credits

Otherwise, the regular method is the default and the skill does not raise the optional method.

---

## Section 10 — Conservative defaults table

| Ambiguity | Conservative default |
|---|---|
| Net SE earnings calculation skipped | Compute it; never silent |
| 92.35% adjustment forgotten | Apply it; defensive check |
| Additional Medicare Tax thresholds | Use statutory ($200K/$250K/$125K), NOT inflation-adjusted (they aren't) |
| 2025 SS wage base unknown | Use $176,100 (verified) |
| W-2 wage coordination unknown | Assume no W-2 (full SS base available for SE) — flag for reviewer |
| Filing status unknown | Single (highest tax in most cases) |
| Form 8829 prior-year carryover unknown | Assume zero — flag |
| Home depreciation basis undocumented | $0 depreciation, but flag §1250 recapture risk anyway |
| Whether actual or simplified home office method was used last year | Ask; do not assume |
| Whether the taxpayer is at-risk for the full investment | Yes (at-risk indicator Line 32a), unless evidence to the contrary |
| Net loss large enough to trigger NOL | Refuse (R-COMP-NOL → R-US-NOL) |
| Hobby loss exposure (3+ year loss streak) | Flag, do not refuse |
| Optional methods applicability | Skip; do not raise unless taxpayer asks |
| Gross receipts < 1099 totals received | Flag — IRS computer match risk |

---

## Section 11 — Topical refusal catalogue

Refusals on top of the global catalogue in `us-tax-workflow-base` Section 6 and the bookkeeping skill's R-BOOK-XXX catalogue.

**R-COMP-NOL — Net operating loss generated.**
Trigger: Schedule C Line 31 produces a loss large enough that the taxpayer's overall income would be negative, indicating an NOL.
Output: "A Schedule C loss large enough to create a net operating loss requires §172 analysis (the 80% taxable income limitation, post-TCJA carryback rules, NOL tracking schedule for future years). This is outside the scope of this skill. The base catalogue refusal R-US-NOL applies. Please consult a CPA or Enrolled Agent with NOL experience."

**R-COMP-ATRISK — At-risk limitation potentially applies (Form 6198).**
Trigger: The taxpayer has a Schedule C loss AND any indication that some portion of investment is not at risk (nonrecourse debt, third-party investors, sheltered investments).
Output: "When a Schedule C loss is generated and not all investment is at risk under §465, Form 6198 is required to compute the allowable loss. This skill does not compute Form 6198. Please consult a CPA or Enrolled Agent for at-risk analysis."

**R-COMP-FORM8959-COMPLEX — Additional Medicare Tax with complex W-2 coordination.**
Trigger: The taxpayer has substantial W-2 wages from another job AND net SE earnings, with combined earnings near the Additional Medicare Tax threshold, AND the W-2 employer's additional withholding (the 0.9% above $200K) creates timing or over-withholding issues.
Output: "Form 8959 (Additional Medicare Tax) coordination between employer withholding and self-employment earnings can be complex when both income streams are substantial. The skill computes the basic Additional Medicare Tax liability but flags this scenario for reviewer attention to verify the withholding coordination."

(Note: this is a flag, not a hard refusal — the skill computes the basic figure and lets the reviewer verify.)

**R-COMP-FARM — Farm income.**
Trigger: The taxpayer has farm income reportable on Schedule F or has net farm earnings flowing to Schedule SE Line 1a.
Output: "Farm income is reported on Schedule F, not Schedule C, and has its own SE tax treatment under the farm optional method. This skill does not handle farm income. Please consult a CPA or Enrolled Agent with agricultural tax experience."

**R-COMP-CHURCH — Church employee income.**
Trigger: The taxpayer has church employee income subject to SE tax under §1402(j) (e.g., a minister or member of a religious order).
Output: "Church employee income, ministerial income, and the §1402(j) special rules require specialized analysis. This skill does not handle these situations. Please consult a CPA or Enrolled Agent with experience in clergy taxation."

**R-COMP-PRIORYEAR — No prior-year return available for context.**
Trigger: Form 8829 carryover or other prior-year-dependent figures need to be verified, but no prior-year return is available.
Output: "This skill needs the prior-year Form 1040, Schedule C, Schedule SE, and Form 8829 (if applicable) to verify carryovers and the consistency of prior elections. Please provide the prior-year return."

(Note: this is a soft refusal — the skill can proceed with assumptions if the user confirms there are no carryovers, but should flag the absence of prior-year data clearly.)

---

## Section 12 — Reviewer attention thresholds

In addition to the base thresholds in `us-tax-workflow-base` Section 5 and the bookkeeping skill's thresholds:

| Threshold | Trigger | Rationale |
|---|---|---|
| Schedule C Line 31 (net profit) ≥ $200,000 | Always flag | Approaches Additional Medicare Tax threshold for single filers |
| Schedule C Line 31 ≤ -$5,000 | Always flag | Loss territory; check at-risk and hobby loss |
| Form 8829 home office deduction ≥ $5,000 | Always flag | Material; substantiation review |
| Home office actual method depreciation taken | Always flag | §1250 recapture risk on future home sale |
| Home office deduction limited by §280A(c)(5) | Always flag | Limit triggered; reviewer should confirm carryover treatment |
| Net SE earnings × 92.35% near $176,100 wage base | Always flag | Approaching SS cap; verify W-2 coordination if applicable |
| Combined SE + W-2 income ≥ Additional Medicare Tax threshold | Always flag | Form 8959 required |
| Schedule C gross receipts (Line 1) < 1099-K + 1099-NEC + 1099-MISC totals | Always flag | IRS computer match risk |
| Optional method (Schedule SE Line 4b) used | Always flag | Reviewer should confirm taxpayer wants to pay more SE tax |
| Prior-year carryover applied | Always flag | Reviewer should verify carryover from prior return |

---

## Section 13 — Worked examples

Continuing with the hypothetical client Maria Hernandez (freelance UX designer, single, sole prop, Austin TX, calendar year 2025, no employees, no inventory, cash method, qualifying home office).

### Example 1 — Schedule C aggregation

**Input from bookkeeping skill (classified totals):**
- Line 1 (Gross receipts): $87,500
- Line 2 (Returns and allowances): $0
- Line 4 (COGS): $0 (service business, no inventory)
- Line 7 (Gross income): $87,500
- Line 8 (Advertising): $480
- Line 9 (Car and truck — standard mileage, 4,200 business miles × $0.70): $2,940
- Line 11 (Contract labor — paid Alex Rodriguez $5,200 throughout year): $5,200
- Line 13 (Depreciation/§179 — MacBook Pro $3,499 with 100% bonus, full first-year): $3,499
- Line 15 (Insurance — business liability): $720
- Line 17 (Legal and professional — LegalZoom trademark + tax prep): $1,150
- Line 18 (Office expense — desk, supplies, etc.): $2,134
- Line 20a (Vehicle/equipment lease): $0
- Line 20b (Coworking — WeWork annual): $3,588
- Line 22 (Supplies): $246
- Line 23 (Taxes and licenses): $0
- Line 24a (Travel — flights, hotels, conference fees, ground transport): $4,287
- Line 24b (Meals — business meals at 50%): $1,840 (gross; the form mechanically applies 50% to arrive at $920 deductible)
- Line 25 (Utilities — N/A; home office covers utilities via Form 8829): $0
- Line 27b (Other expenses — software subscriptions, AI APIs, dues, bank fees, processor fees): $4,892

**Computation:**
- Line 7 (gross income): $87,500
- Line 28 (total expenses, sum of lines 8-27b, with Line 24b at 50%): $480 + 2,940 + 5,200 + 3,499 + 720 + 1,150 + 2,134 + 3,588 + 246 + 4,287 + 920 + 4,892 = **$30,056**
- Line 29 (tentative profit): $87,500 − $30,056 = **$57,444**

Now home office. Maria has a 150 sq ft office in a 1,200 sq ft home. Business percentage = 12.5%. Last year she used the simplified method. This year she's electing to switch to the actual method to capture more deduction.

Form 8829 inputs:
- Mortgage interest: $14,200 (annual)
- Real estate taxes: $7,800
- Homeowner's insurance: $1,440
- Utilities (gas, electric, water, internet): $3,600
- Repairs: $0 (no home repairs this year)
- Adjusted basis of home at conversion (Jan 2024): $385,000
- FMV at conversion: $410,000 (use the lesser, $385,000)
- Land value: $80,000
- Depreciable basis of building: $385,000 − $80,000 = $305,000
- Business basis: $305,000 × 12.5% = $38,125
- Depreciation rate (39-year SL, full year): 1/39 = 2.564%
- Annual depreciation: $38,125 × 2.564% = $977
- Prior-year carryover: $0 (used simplified method last year, no carryover)

Form 8829 computation:
- Indirect expenses: $14,200 + $7,800 + $1,440 + $3,600 = $27,040
- Business portion of indirect: $27,040 × 12.5% = $3,380
- Direct expenses: $0
- Operating expenses subtotal: $3,380
- Depreciation: $977
- Total tentative home office deduction: $3,380 + $977 = **$4,357**

Gross income limitation check: tentative deduction $4,357 vs Line 29 of $57,444 → no limitation, full deduction allowed.

- Line 30 (home office deduction): **$4,357**
- Line 31 (net profit): $57,444 − $4,357 = **$53,087**
- Line 32: 32a (all investment is at risk)

**Reviewer attention flags:**
- Home office actual method with depreciation taken — flag the §1250 recapture on future home sale
- Home office method change from simplified (prior year) to actual (current year) — confirm the change is intentional and the reviewer agrees
- Form 8829 line 41 depreciation creates the recapture exposure; reviewer should confirm the taxpayer understands

### Example 2 — Schedule SE computation

**Input:** Schedule C Line 31 = $53,087. Maria has no W-2 wages, no farm income, single filer, age 32.

**Schedule SE Part I:**
- Line 1a: $0 (no farm)
- Line 2: $53,087 (from Schedule C Line 31)
- Line 3: $53,087
- Line 4a: $53,087 × 92.35% = **$49,026**
- Line 4b: $0 (no optional method)
- Line 4c: $49,026
- Line 5b: $0 (no church employee income)
- Line 6: $49,026
- Line 7: $176,100 (2025 SS wage base)
- Line 8a: $0 (no W-2 wages)
- Line 8d: $0
- Line 9: $176,100 − $0 = $176,100
- Line 10: smaller of $49,026 or $176,100 = $49,026 × 12.4% = **$6,079** (Social Security portion)
- Line 11: $49,026 × 2.9% = **$1,422** (Medicare portion)
- Line 12: SE tax = $6,079 + $1,422 = **$7,501**
- Line 13: Deductible half = $7,501 × 50% = **$3,750** (flows to Schedule 1 line 15)

**Additional Medicare Tax check:** Maria's combined earned income is $49,026 (SE only) + $0 (W-2) = $49,026. Single threshold is $200,000. $49,026 < $200,000 → No Additional Medicare Tax. Form 8959 not required.

**Outputs to downstream skills:**
- Schedule C Line 31: $53,087 → flows to Schedule 1 line 3 and to QBI computation in `us-form-1040-self-employed-positions`
- Schedule SE Line 12 (SE tax): $7,501 → flows to Schedule 2 line 4
- Schedule SE Line 13 (deductible half): $3,750 → flows to Schedule 1 line 15
- Net SE earnings (Line 4c): $49,026 → used as the base for SEP-IRA / Solo 401(k) contribution computation in `us-form-1040-self-employed-positions`

**Reviewer attention flags for Schedule SE:**
- None — Maria is well below the SS wage base, well below the Additional Medicare Tax threshold, and has no optional method or W-2 coordination issues. The Schedule SE is mechanical.

### Example 3 — Higher income with W-2 coordination

**Hypothetical change:** Suppose Maria also worked part-time as a W-2 employee at a design agency in early 2025 before going full-time freelance, earning $90,000 in W-2 wages. Her Schedule C net profit is the same $53,087.

**Schedule SE recomputation:**
- Line 6: $49,026 (same)
- Line 7: $176,100
- Line 8a: $90,000 (W-2 SS wages)
- Line 8d: $90,000
- Line 9: $176,100 − $90,000 = $86,100 (remaining SS base)
- Line 10: smaller of $49,026 or $86,100 = $49,026 × 12.4% = $6,079 (same as before — full SS portion)
- Line 11: $49,026 × 2.9% = $1,422 (Medicare unchanged)
- Line 12: $7,501 (same)
- Line 13: $3,750 (same)

**Additional Medicare Tax check:** Combined earned income = $90,000 + $49,026 = $139,026. Single threshold = $200,000. Still below. No Additional Medicare Tax.

**Now suppose W-2 was $180,000 instead.** Combined earned income = $180,000 + $49,026 = $229,026. Excess over $200,000 = $29,026. Additional Medicare Tax = $29,026 × 0.9% = $261.

But wait — the W-2 employer started withholding the additional 0.9% on wages above $200,000 (employer is required to do so on a per-employee basis without regard to filing status). On $180,000 of wages, no additional withholding by the employer (because $180K < $200K). So the entire $261 of Additional Medicare Tax is collected via Form 8959 on the personal return.

The Schedule SE itself is unchanged. The $261 is on Form 8959, not Schedule SE.

**Reviewer attention flags for the high-W-2 scenario:**
- Form 8959 required (Additional Medicare Tax)
- W-2 SS wages at $180K + SE earnings at $49K means the SS portion of SE tax is constrained — Line 9 = $176,100 − $180,000 = negative, so Line 9 = $0, and Line 10 (SS portion of SE tax) = $0. Only the Medicare portion of SE tax applies. **This is the W-2 coordination case the skill flags.**
- Recomputation: Line 10 = $0 (no SS portion because the wage base was already met by W-2). Line 11 = $1,422 (Medicare unchanged). Line 12 = $1,422. Line 13 = $711.

That changes the SE tax dramatically — from $7,501 down to $1,422 because the SS portion is fully covered by W-2 wages. The skill must do this coordination correctly. Defensive check.

### Example 4 — Net loss scenario

**Hypothetical change:** Suppose Maria's Schedule C produces a $12,000 loss instead of a profit (slow first year, big equipment purchases).

**Schedule C:**
- Line 31: ($12,000)

**Schedule SE:**
- Line 2: ($12,000)
- Line 3: ($12,000)
- Line 4a: not computed (only positive amounts × 92.35%; loss flows through as zero SE earnings)
- Line 12: $0 (no SE tax on a loss)
- Line 13: $0

**The loss flows to Schedule 1 line 3 as ($12,000).** It reduces AGI on the personal return.

**Reviewer attention flags:**
- Schedule C net loss: trigger hobby loss check (R-COMP-HOBBY if 3+ year streak — defer to bookkeeping skill flag)
- Net loss + other income < $0: trigger R-US-NOL / R-COMP-NOL check
- At-risk: confirm Line 32a (all at risk) — if any portion is not at risk, R-COMP-ATRISK fires
- Schedule SE: zero SE tax computed correctly; flag that no Social Security credits are earned this year

### Example 5 — Simplified home office method

**Hypothetical change:** Maria uses the simplified method instead of actual.

**Simplified computation:**
- Office square footage: 150 (under the 300 cap)
- Deduction = 150 × $5 = **$750**
- Maximum: $1,500 (not approached)
- Gross income limitation: $750 vs Line 29 tentative profit $57,444 → no limit

**Line 30: $750**
**Line 31: $57,444 − $750 = $56,694**

Net profit is higher under simplified ($56,694 vs $53,087) because the simplified method gives less deduction here. But Maria avoids the §1250 recapture exposure on the home depreciation. The reviewer should compare both methods and confirm Maria's preference. Without §1250 exposure, simplified is sometimes the better long-run choice even if the current-year deduction is smaller.

**Reviewer attention flags:**
- Simplified method election — confirm the user understands the trade-off vs. actual method
- No carryover available under simplified (the disallowed portion of any limit is lost)

---

## Section 14 — Output format extensions

### Extension 1 — Schedule C / SE computation worksheet

A markdown or Excel worksheet (Excel preferred when working alongside the bookkeeping working paper) with the following sheets:

**Sheet "Schedule C Computation"** — Lines 1 through 32 with formulas referencing the bookkeeping working paper:

| Line | Description | Source | Amount | Notes |
|---|---|---|---|---|
| 1 | Gross receipts | Bookkeeping Sheet "Schedule C Summary" Line 1 | $X | |
| 2 | Returns and allowances | Bookkeeping Sheet | $X | |
| 3 | Subtract | Formula | $X | |
| 4 | Cost of goods sold | Bookkeeping Sheet Part III | $X | |
| 5 | Gross profit | Formula | $X | |
| 6 | Other income | Bookkeeping Sheet | $X | |
| 7 | Gross income | Formula | $X | |
| 8-27b | Expense lines | Bookkeeping Sheet line by line | $X each | |
| 28 | Total expenses | SUM formula | $X | |
| 29 | Tentative profit | Line 7 - Line 28 | $X | |
| 30 | Home office | From Form 8829 sheet OR simplified worksheet | $X | Method noted |
| 31 | Net profit | Line 29 - Line 30 | $X | **BOTTOM LINE** |
| 32a/b | At-risk indicator | Reviewer judgment | a or b | |

**Sheet "Form 8829" (if actual method)** — Form 8829 line by line with all computations.

**Sheet "Simplified Home Office Worksheet" (if simplified method)** — the worksheet from Schedule C Instructions.

**Sheet "Schedule SE"** — Lines 1 through 13 with the 92.35% adjustment, the SS cap coordination, the Medicare computation, and the deductible half.

**Sheet "Form 8959 Estimate" (if applicable)** — Additional Medicare Tax computation when combined earned income exceeds the threshold.

**Sheet "Downstream Outputs"** — A summary of values that flow to other skills:
- Schedule 1 line 3 (business income): from Schedule C Line 31
- Schedule 1 line 15 (deductible half of SE tax): from Schedule SE Line 13
- Schedule 2 line 4 (SE tax): from Schedule SE Line 12
- Net SE earnings (for retirement contribution computation downstream): Schedule SE Line 4c
- Tentative QBI (for QBI computation downstream): Schedule C Line 31, possibly with adjustments handled by the QBI skill

**File location:** `/mnt/user-data/outputs/<taxpayer-identifier>-schedule-c-se-2025-computation.xlsx`

### Extension 2 — Computation summary in the reviewer brief

In addition to the base brief template and the bookkeeping skill's Schedule C line summary, this skill adds:

```markdown
## Schedule C bottom line

| Line | Description | Amount |
|---|---|---|
| 7 | Gross income | $X |
| 28 | Total expenses | $X |
| 29 | Tentative profit | $X |
| 30 | Home office (method: actual / simplified) | $X |
| 31 | Net profit (or loss) | $X |
| 32 | At-risk indicator | a (all at risk) / b (Form 6198) |

## Form 8829 detail (actual method only)

[Full Form 8829 computation, line by line, with the §280A(c)(5) gross income limitation check and any carryover]

## Schedule SE computation

| Line | Description | Amount |
|---|---|---|
| 2 | Net profit from Schedule C Line 31 | $X |
| 4a | Net SE earnings (Line 3 × 92.35%) | $X |
| 6 | Net SE earnings subject to SS portion | $X |
| 7 | 2025 SS wage base | $176,100 |
| 8d | W-2 wages already subject to SS | $X |
| 9 | Remaining SS base for SE | $X |
| 10 | Social Security portion (smaller of Line 6 or 9 × 12.4%) | $X |
| 11 | Medicare portion (Line 6 × 2.9%) | $X |
| 12 | Total SE tax | $X |
| 13 | Deductible half of SE tax | $X |

## Additional Medicare Tax check

Combined earned income (W-2 + SE): $X
Filing status threshold: $X
Above threshold? Y/N
If yes: Additional Medicare Tax owed: $X (Form 8959)

## Outputs flowing to downstream skills

- To `us-form-1040-self-employed-positions`:
  - Schedule C Line 31 (net profit): $X
  - Net SE earnings (Schedule SE Line 4c): $X (used for retirement contribution base)
  - Deductible half of SE tax (Schedule SE Line 13): $X

- To `us-quarterly-estimated-tax`:
  - Current-year Schedule C Line 31: $X (for current-year safe harbor)
  - Current-year SE tax: $X
```

---

## Section 15 — Intake form additions

### Upstream prerequisite check (NEW in v0.2)

**Before asking any intake questions, this skill verifies that the upstream `us-sole-prop-bookkeeping` skill has produced a valid working paper.** The computation skill consumes classified transactions from the bookkeeping working paper — if the working paper does not exist or is incomplete, computation cannot start.

Execute these checks in order at the beginning of Step 6 of the base workflow:

1. **Locate the upstream working paper.** Check `/mnt/user-data/outputs/` for a file matching `<taxpayer-identifier>-schedule-c-<year>-working-paper.xlsx`. If multiple files match, use the most recent. If none match, check `/home/claude/` for an in-progress version.

2. **If no upstream working paper exists:**
   - If the current conversation has not yet run the bookkeeping skill, stop and tell the user: "I need the bookkeeping classification to run first. Do you want me to run `us-sole-prop-bookkeeping` on your transaction data, then continue with the computation? Or do you already have a classified working paper from a previous session that I should load?"
   - If the user provides classified totals directly (e.g., "here are the Schedule C line totals, just compute the bottom line"), accept them as a fallback but flag prominently in the brief that the upstream bookkeeping work was not independently validated by this skill and the reviewer should confirm the source of the totals.
   - Do not proceed past this point without either a working paper or user-provided totals.

3. **Open the working paper and verify structural integrity.** Use the xlsx skill to read the file. Confirm:
   - Sheet "Transactions" exists and has at least one row of data
   - Sheet "Schedule C Summary" exists with Line 1-27b totals (or their SUMIFS formulas)
   - Sheet "Form 4562 Detail" exists if any capital items were classified
   - Sheet "Form 8829 Detail" exists if home office actual method was used
   - Sheet "Downstream Items" exists if any items were identified for downstream skills (NEW in v0.2 bookkeeping skill)
   - The working paper's header or metadata states the tax year and taxpayer identifier, and they match the current engagement

4. **Verify the upstream passed its own self-checks.** The bookkeeping skill's brief (generated alongside the working paper) includes a self-check section. If the brief is available in the conversation context or in `/mnt/user-data/outputs/`, confirm the 10 bookkeeping self-checks all passed. If the brief is not available or any check failed, flag prominently and ask the user whether to proceed with incomplete upstream work.

5. **Read the Downstream Items sheet** (if present). This sheet lists transactions the bookkeeping skill identified as belonging to downstream skills. For this skill's scope, note which items flow to `us-schedule-c-and-se-computation` (none — everything that belongs here is already on Schedule C lines), and surface the rest in the brief's "Downstream items deferred" section so the reviewer sees what's pending for other skills.

6. **Only after the upstream check clears, proceed to the intake questions below.**

### Computation-specific intake questions

Per slot 18 of the base intake form, this skill adds the following questions IF NOT already answered by the bookkeeping skill's intake. (Most overlap with the bookkeeping skill's intake — this skill should not re-ask questions already answered.)

**Computation-specific intake (slot 18 additions, beyond what bookkeeping asks):**

18m. **Prior-year Form 8829 (if home office actual method):** Do you have a copy of last year's Form 8829? It's needed to identify any operating expense or depreciation carryover.

18n. **Prior-year Schedule C and Schedule SE:** Do you have a copy of last year's Schedule C and Schedule SE? Needed for the safe harbor computation and to identify any prior-year elections that carry over (depreciation method, §179 election history, etc.).

18o. **W-2 wages from another job in 2025 (if not already known):** Do you (or your spouse, if filing jointly) have W-2 wages from any job in 2025? If yes, what's the total of Box 3 (Social Security wages) on each W-2? This affects the Social Security portion of SE tax through wage base coordination.

18p. **Home office method election:** If you have a home office, do you want to use the simplified method ($5/sq ft, max $1,500, no depreciation, no carryover) or the actual method (Form 8829, allows depreciation but creates §1250 recapture exposure)? If you used a method last year, do you want to switch this year? Either is permitted; there is no lock-in.

18q. **At-risk status:** Is all of your investment in this business at risk (your own money plus recourse debt), or is some portion sheltered (nonrecourse loans, third-party investors, etc.)? For most sole props the answer is "all at risk" — if anything else, please explain.

18r. **Form 1099-K, 1099-NEC, 1099-MISC received:** Did you receive any 1099 forms reporting income to you in 2025? If yes, please provide them — the gross receipts on Schedule C Line 1 must be cross-checked against the 1099 totals to avoid IRS computer match issues.

---

## Section 16 — Self-check additions

In addition to the 17 base self-checks (updated in v0.2 of the workflow base) and the 10 bookkeeping skill self-checks, this skill adds:

**Check 26 — Schedule C aggregation matches bookkeeping output.** Every Schedule C line (1 through 27b) computed in the worksheet matches the corresponding line total from the bookkeeping working paper. The aggregation is consistent. No transactions are dropped or double-counted between the two skills.

**Check 27 — Line 28 equals sum of Lines 8 through 27b.** Mechanical check. Tolerance zero (whole dollars).

**Check 28 — Line 29 = Line 7 minus Line 28.** Mechanical.

**Check 29 — Line 31 = Line 29 minus Line 30.** Mechanical.

**Check 30 — Line 30 ≤ Line 29.** The §280A(c)(5) gross income limitation. The home office deduction cannot exceed tentative profit. If it does, the deduction must be capped and the excess carried over (actual) or lost (simplified).

**Check 31 — 92.35% adjustment applied to Schedule SE Line 4a.** Defensive check against the most common SE tax computation error. If Line 4a is computed as Line 3 × 1.0 instead of × 0.9235, the check fails.

**Check 32 — SS wage base coordination correct.** If the taxpayer has W-2 wages, Schedule SE Line 9 = $176,100 minus W-2 SS wages. Line 10 uses the smaller of Line 6 or Line 9. If the taxpayer has no W-2, Line 9 = $176,100.

**Check 33 — Additional Medicare Tax NOT computed on Schedule SE.** Defensive check. The 0.9% must be on Form 8959, not blended into Schedule SE. Schedule SE Line 11 uses 2.9% only.

**Check 34 — Deductible half of SE tax = Line 12 × 50%.** Mechanical.

**Check 35 — $400 minimum threshold respected.** If net SE earnings (Line 4c) are less than $400, no SE tax is due. Schedule SE Line 12 should be zero. If the skill computed SE tax on a sub-$400 amount, the check fails.

**Check 36 — Net loss handling.** If Schedule C Line 31 is negative, Schedule SE Line 4a, Line 12, and Line 13 should all be zero (no SE tax on a loss). The loss still flows to Schedule 1 line 3 as a negative.

**Check 37 — Form 8829 §280A(c)(5) limitation applied if needed.** If actual method home office tentative deduction exceeds Line 29 tentative profit, the limit is applied, the deduction is capped at Line 29, and the carryover is computed correctly on Form 8829 lines 43-44.

**Check 38 — Home depreciation §1250 recapture warning included.** If actual method home office is used and depreciation is taken (or "allowable"), the brief includes a prominent warning about §1250 recapture on future home sale.

**Check 39 — Downstream outputs section present.** The brief explicitly states the values that will flow to `us-form-1040-self-employed-positions` and `us-quarterly-estimated-tax`. Without this section, the downstream skills won't have a clean handoff.

**Check 40 — At-risk indicator stated.** Line 32a or 32b is explicitly stated. If 32b, R-COMP-ATRISK fires.

**Check 41 — Upstream bookkeeping working paper exists and was read (NEW in v0.2).** Before any computation was performed, the upstream `us-sole-prop-bookkeeping` working paper (or user-provided totals as a flagged fallback) was located, opened, and validated per Section 15's upstream prerequisite check. The brief's "Source data referenced" header lists the exact filename of the upstream working paper. If the upstream was missing or incomplete, the brief's high-flags section prominently states that the computation was performed on user-provided totals rather than on independently-classified transactions.

**Check 42 — Upstream self-check status captured (NEW in v0.2).** If the upstream bookkeeping brief was available, the bookkeeping skill's 10 self-checks all passed. The computation brief's refusal trace section notes "Upstream bookkeeping self-checks: 10/10 passed" or states which checks failed and how. If any upstream check failed and the user authorized proceeding anyway, the authorization is recorded verbatim in the brief.

---

## Section 17 — Cross-skill references

**Inputs from `us-sole-prop-bookkeeping`:**
- Schedule C line totals (Lines 1 through 27b)
- COGS line total (Part III line 42)
- Form 8829 input data (square footage, mortgage interest, taxes, insurance, utilities, depreciation basis) if actual method
- Reviewer attention flags from the bookkeeping working paper (carry through to the computation brief)
- Default-applied flags from the bookkeeping working paper (carry through)
- Prior-year carryover information (from bookkeeping intake slot 18k)

**Outputs to `us-form-1040-self-employed-positions`:**
- Schedule C Line 31 (net profit) — used as the base for QBI, SE health insurance limit, retirement contribution base
- Schedule SE Line 4c (net SE earnings) — used as the base for retirement contribution computation
- Schedule SE Line 13 (deductible half of SE tax) — flows to Schedule 1 line 15
- Schedule SE Line 12 (total SE tax) — flows to Schedule 2 line 4

**Outputs to `us-quarterly-estimated-tax`:**
- Current-year Schedule C Line 31
- Current-year Schedule SE Line 12
- Combined with downstream income tax computation, drives the safe harbor for next year

**This skill does not consume outputs from other content skills downstream.** It is in the middle of the chain.

---

## Section 18 — Reference material

### Validation status

This file is v0.1 of `us-schedule-c-and-se-computation`, drafted in April 2026 as the second content skill on top of `us-tax-workflow-base` v0.1. Year-specific figures verified against:
- SSA 2025 wage base announcement (October 2024) for the $176,100 figure
- Notice 2024-80 for retirement plan figures referenced for context
- IRC sections in force for 2025
- Schedule SE Instructions (2025) and Form 8829 Instructions (2025) for line-by-line mechanics
- IRS Publication 587 (2025) for home office rules

OBBBA P.L. 119-21 was reviewed for impact on this skill. **OBBBA does not change Schedule SE mechanics, the 92.35% adjustment, the OASDI / Medicare rates, the Additional Medicare Tax thresholds, the §280A home office structure, or the §1402 net SE earnings definition.** OBBBA's only relevance to this skill is the depreciation rules that affect Form 8829's home depreciation component (which is covered by the bookkeeping skill's depreciation discussion under Line 13, and is straight-line 39-year for the home itself, unaffected by bonus depreciation since real property doesn't qualify for bonus).

### Origin

Drafted from training-cutoff knowledge of US federal tax law plus targeted verification of 2025-specific figures via web search of authoritative sources (IRS.gov, SSA.gov, Big 4 firm summaries). The workflow assumptions are inherited from `us-tax-workflow-base`. The classification work is inherited from `us-sole-prop-bookkeeping`.

### Known gaps

1. **Form 8829 depreciation** uses the simple full-year straight-line approximation (cost basis × 12.5% business × 1/39 = annual). The actual Form 8829 instructions use a depreciation table from Pub 946 that takes into account the month placed in service via the mid-month convention. For first-year and disposition-year computations, the table-based approach is more accurate. The skill's simplification is acceptable for full-year continuing use but should be flagged for first-year and disposition-year cases.

2. **Form 8959 Additional Medicare Tax computation** is approximate. The skill computes the basic figure (combined earned income above threshold × 0.9%) but does not handle the full Form 8959 mechanics including employer withholding coordination on Part II. For taxpayers with substantial W-2 wages and SE earnings, R-COMP-FORM8959-COMPLEX flags this for reviewer attention.

3. **The optional methods (Section 9)** are documented but not aggressively integrated into the workflow. Most sole props don't use them; the skill's default is to skip them unless the user asks. A future v0.2 could add automatic detection of low-income near-retirement taxpayers and proactively raise the optional method as a planning option.

4. **Net loss handling** triggers refusal R-COMP-NOL when the loss is large enough to create an actual NOL, but the threshold for "creates an NOL" requires knowing the taxpayer's other income, which this skill doesn't compute. The handoff to `us-form-1040-self-employed-positions` is needed to confirm whether an NOL actually exists. Until the personal return is computed, R-COMP-NOL is a "potential NOL" flag rather than a confirmed refusal.

5. **At-risk computation** (Form 6198) is refused (R-COMP-ATRISK) rather than handled. For most sole props this never matters because they're fully at risk. A future v0.2 could add basic at-risk computation for the simple cases where everything is at risk and Form 6198 is just confirming that.

6. **Hobby loss flagging** is delegated to the bookkeeping skill (which knows the loss history). This skill carries through the flag but doesn't independently assess.

7. **The §280A(c)(5) gross income limitation** can in unusual cases create an interaction with the §1402(a)(12) computation: a home office deduction limited by §280A(c)(5) reduces Schedule C Line 31, which reduces SE earnings. The skill handles this correctly (compute Line 31 first, then Schedule SE), but the interaction should be flagged when Form 8829 carryovers exist because the carryover represents future SE earnings impact too.

### Change log

- **v0.1 (April 2026):** Initial draft. Tax year 2025. Built on `us-tax-workflow-base` v0.1 and consumes output from `us-sole-prop-bookkeeping` v0.1. Reflects pre-OBBBA Schedule SE structure (unchanged by OBBBA).

### Self-check (v0.1 of this document, not the runtime self-check in Section 16)

1. Loads on top of `us-tax-workflow-base`: yes.
2. Consumes output from `us-sole-prop-bookkeeping`: yes (Section 17).
3. Year-specific figures table provided: yes (Section 3).
4. Primary source library provided: yes (Section 4).
5. Schedule C aggregation rules: yes (Section 5).
6. Form 8829 actual method computation: yes (Section 6).
7. Simplified home office method: yes (Section 7).
8. Schedule SE computation: yes (Section 8).
9. Optional methods covered: yes (Section 9).
10. Conservative defaults table: yes (Section 10).
11. Topical refusal catalogue: yes (Section 11).
12. Reviewer attention thresholds: yes (Section 12).
13. Worked examples (5 examples drawn from hypothetical client Maria Hernandez): yes (Section 13).
14. Output format extensions: yes (Section 14).
15. Intake form additions: yes (Section 15).
16. Self-check additions: yes (Section 16).
17. Cross-skill references: yes (Section 17).
18. Reference material: yes (Section 18).
19. Citation discipline maintained: every position rule cites a primary source.
20. 2025 SS wage base ($176,100) verified.
21. 92.35% adjustment correctly applied throughout.
22. Additional Medicare Tax thresholds correctly stated as statutory non-indexed.
23. OBBBA impact assessment: confirmed OBBBA does not change Schedule SE mechanics or the §280A home office structure.
24. Form 8959 vs Schedule SE separation: defensive check #33.
25. Net loss handling: covered in Example 4 and check #36.

## End of US Schedule C and SE Computation Skill v0.1

This skill is incomplete without `us-tax-workflow-base` v0.1 or later loaded alongside it, AND without `us-sole-prop-bookkeeping` v0.1 or later providing classified transaction inputs. If you are reading this without both companion files loaded, ask the user to load them before proceeding.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
