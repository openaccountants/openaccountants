---
name: ie-income-tax-form11
description: >
  Use this skill whenever asked about Irish income tax for self-employed individuals filing Form 11. Trigger on phrases like "Form 11", "self-assessment Ireland", "Case I profits", "Case II profits", "USC", "PRSI Class S", "preliminary tax Ireland", "earned income credit", "trading profits", "self-employed tax Ireland", "ROS filing", or any question about computing or filing income tax for a self-employed person in Ireland. This skill covers income tax rates (20%/40%), USC bands, PRSI Class S, personal tax credits, allowable deductions, capital allowances, preliminary tax, and Form 11 structure. ALWAYS read this skill before touching any Irish income tax work.
version: 1.0
jurisdiction: IE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Ireland Income Tax (Form 11) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Ireland |
| Jurisdiction Code | IE |
| Primary Legislation | Taxes Consolidation Act 1997 (TCA 1997) |
| Supporting Legislation | Finance Act 2024 (Budget 2025 measures); Social Welfare Consolidation Act 2005 (PRSI); USC legislation (Part 18D TCA 1997) |
| Tax Authority | Revenue Commissioners (revenue.ie) |
| Filing Portal | Revenue Online Service (ROS) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Chartered Accountant or Chartered Tax Adviser (CTA) practising in Ireland |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, USC computation, PRSI Class S, personal credits, capital allowance rates, preliminary tax rules, filing deadlines. Tier 2: mixed-use expense apportionment, home office deductions, motor vehicle business %, bad debt write-offs, cessation relief. Tier 3: partnerships, rental income interactions, CGT, non-resident income, Revenue audits, appeals. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Filing status** [T1] -- single, married (one earner), married (two earners), or single parent (one-parent family credit). Determines which standard rate band applies.
2. **Employment status** [T1] -- fully self-employed or employed with side self-employment income.
3. **Gross self-employment income** [T1] -- total turnover/receipts in the year (Case I trade or Case II profession).
4. **Business expenses** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items).
5. **Capital assets acquired in the year** [T1] -- type, cost, date first used in business.
6. **PRSI Class S paid** [T1] -- amount paid in the year (minimum EUR 650).
7. **Prior year tax liability** [T1] -- for preliminary tax calculation.
8. **Other income** [T1] -- employment income (PAYE), rental income, investment income, foreign income.
9. **Age** [T1] -- relevant for USC reduced rates (over 70) and age credit.

**If filing status is unknown, STOP. Do not apply a rate band. Filing status is mandatory.**

---

## Step 1: Determine Applicable Income Tax Rates and Standard Rate Band [T1]

**Legislation:** TCA 1997, as amended by Finance Act 2024 (Budget 2025)

### Income Tax Rates

| Rate | Name |
|------|------|
| 20% | Standard rate |
| 40% | Higher rate |

### Standard Rate Band (2025)

| Filing Status | Standard Rate Band (20%) | Balance at 40% |
|---------------|--------------------------|-----------------|
| Single person | EUR 44,000 | All income above EUR 44,000 |
| Married couple (one earner) | EUR 53,000 | All income above EUR 53,000 |
| Married couple (two earners) | EUR 53,000 + EUR 35,000 (max EUR 88,000 combined) | All income above the combined band |
| Single parent (one-parent family) | EUR 48,000 | All income above EUR 48,000 |

**Note:** The standard rate band was increased by EUR 2,000 for all categories in Budget 2025.

---

## Step 2: Universal Social Charge (USC) [T1]

**Legislation:** TCA 1997, Part 18D

### USC Exemption

If total income does not exceed EUR 13,000, no USC is payable. Once income exceeds EUR 13,000, USC applies to ALL income from the first euro.

### Standard USC Rates (2025)

| Band | Rate |
|------|------|
| First EUR 12,012 | 0.5% |
| EUR 12,012.01 -- EUR 27,382 | 2% |
| EUR 27,382.01 -- EUR 70,044 | 3% (was 4% -- reduced in Budget 2025) |
| Above EUR 70,044 | 8% |

### USC Surcharge on Self-Employment Income [T1]

An additional 3% USC surcharge applies to individuals with non-PAYE income exceeding EUR 100,000 in aggregate. This brings the effective USC rate on the portion above EUR 70,044 to 11% (8% + 3%) for affected self-employed individuals.

### Reduced USC Rates

Individuals aged 70+ OR holders of a full medical card with total income not exceeding EUR 60,000 qualify for reduced rates. [T2] Flag for reviewer if client may qualify.

---

## Step 3: PRSI Class S [T1]

**Legislation:** Social Welfare Consolidation Act 2005

### Rates (2025)

| Period | Rate | Minimum |
|--------|------|---------|
| 1 Jan -- 30 Sep 2025 | 4.1% | EUR 650 |
| 1 Oct -- 31 Dec 2025 | 4.2% | EUR 650 |
| Blended annual rate (2025) | 4.125% | EUR 650 |

### Rules [T1]

- PRSI Class S applies to self-employed individuals with income from all sources of EUR 5,000 or more per year.
- Charged on gross income (before deductions, but after capital allowances).
- Minimum contribution: EUR 650 per year regardless of income level (if income exceeds EUR 5,000).
- PRSI is NOT a deductible expense for income tax purposes -- it is computed on taxable income and paid separately.

---

## Step 4: Personal Tax Credits [T1]

**Legislation:** TCA 1997, as amended by Finance Act 2024

### Main Credits (2025)

| Credit | Amount (EUR) |
|--------|-------------|
| Single Person's Credit | 2,000 |
| Married Person's Credit | 4,000 |
| Earned Income Credit (self-employed) | 2,000 |
| Employee (PAYE) Credit | 2,000 |
| One Parent Family Credit | 1,800 |
| Home Carer Credit | 1,950 |
| Age Credit (single, 65+) | 245 |
| Age Credit (married, 65+) | 490 |

### Rules [T1]

- The Earned Income Credit (EUR 2,000) is available to self-employed individuals. It is NOT available if the individual already claims the full PAYE Employee Credit on the same income.
- Where a person has both employment and self-employment income, they may claim BOTH the PAYE Credit and the Earned Income Credit, but the combined total cannot exceed EUR 2,000 per person (increased to EUR 2,000 each in 2025).
- Tax credits reduce the tax payable, NOT the taxable income. They are deducted after computing gross tax.

---

## Step 5: Case I / Case II Trading Profits Computation [T1/T2]

**Legislation:** TCA 1997, Schedule D, Cases I and II

### The Computation Structure

| Line | Description |
|------|-------------|
| 1 | Gross turnover / fees received |
| 2 | Less: Cost of sales (if applicable) |
| 3 | Gross profit |
| 4 | Less: Allowable revenue deductions |
| 5 | Net profit before capital allowances |
| 6 | Less: Capital allowances |
| 7 | Adjusted Case I/II profit |

### Allowable Revenue Deductions [T1/T2]

**The Test:** An expense is deductible if incurred "wholly and exclusively" for the purposes of the trade or profession (TCA 1997, s.81).

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated business premises) | T1 | Fully deductible |
| Professional indemnity insurance | T1 | Fully deductible |
| Accountancy / audit fees | T1 | Fully deductible |
| Legal fees (business-related) | T1 | Fully deductible |
| Office supplies / stationery | T1 | Fully deductible |
| Software subscriptions | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Professional body subscriptions | T1 | Fully deductible |
| Travel and subsistence (business purpose) | T1 | Fully deductible (civil service rates for subsistence) |
| Bad debts (specific, previously included in income) | T2 | Flag for reviewer -- confirm write-off criteria |
| Phone / broadband | T2 | Business use portion only -- client to confirm % |
| Motor vehicle running costs | T2 | Business use portion only -- mileage log required |
| Home office expenses | T2 | Proportional -- see home office rules |
| Use of personal car (mileage basis) | T2 | Civil service mileage rates may apply -- flag for reviewer |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Entertainment (client meals, hospitality) | Blocked under s.840 TCA 1997 |
| Personal living expenses | Not business-related |
| Fines, penalties, or surcharges | Public policy |
| Income tax, USC, PRSI | Tax on income |
| Capital expenditure | Goes through capital allowances, not revenue deductions |
| Drawings / personal withdrawals | Not an expense |
| General provisions (non-specific bad debts) | Must be specific and documented |

---

## Step 6: Capital Allowances [T1]

**Legislation:** TCA 1997, Part 9 (ss.283-321)

### Wear and Tear Allowances (Straight-Line on Cost)

| Asset Type | Annual Rate | Recovery Period |
|-----------|-------------|-----------------|
| Plant and machinery | 12.5% | 8 years |
| Motor vehicles (max cost EUR 24,000) | 12.5% | 8 years |
| Computer equipment | 12.5% | 8 years |
| Office furniture and fittings | 12.5% | 8 years |
| Industrial buildings | 4% | 25 years |
| Energy-efficient equipment (ACA) | 100% | Year 1 (Accelerated Capital Allowance) |

### Rules [T1]

- Wear and tear allowances are calculated on the **cost price** at 12.5% per annum (straight-line).
- Motor vehicles: cost is capped at EUR 24,000 for capital allowance purposes. If the car costs EUR 30,000, allowances are calculated on EUR 24,000 only.
- Motor vehicles: only the business-use proportion is claimable [T2].
- Industrial buildings: 4% per annum over 25 years.
- Accelerated Capital Allowances (ACA): 100% first-year allowance available for qualifying energy-efficient equipment (SEAI list).
- Allowances start in the year the asset is first used in the trade.

### Balancing Allowances / Charges [T2]

- On disposal of an asset: if sale proceeds exceed written-down value, a balancing charge (taxable) arises.
- If sale proceeds are less than written-down value, a balancing allowance (deductible) arises.
- Flag for reviewer to confirm disposal proceeds and written-down value.

---

## Step 7: Preliminary Tax [T1]

**Legislation:** TCA 1997, s.952-959

### Rules

Preliminary tax for the current year must be paid by the filing deadline (31 October, or mid-November via ROS) of that year. To avoid interest charges, preliminary tax must equal or exceed the lower of:

| Method | Amount |
|--------|--------|
| Option 1: Prior year basis | 100% of the prior year's final tax liability |
| Option 2: Current year basis | 90% of the current year's actual tax liability |

### First Year of Self-Employment

No preliminary tax is due in respect of the first year of self-employment (there is no prior year liability). Full tax for the first year is due with the filing of the return.

### Direct Debit Option

If paying by monthly direct debit, the taxpayer must pay 105% of the pre-preceding year's liability spread over the year.

---

## Step 8: Form 11 Structure [T1]

**Legislation:** TCA 1997; Revenue Form 11 (2025)

### Key Panels

| Panel | Description | Notes |
|-------|-------------|-------|
| Panel A | Personal details | Name, PPS number, marital status |
| Panel B | Self-employment (Case I/II) | Turnover, net profit, capital allowances |
| Panel C | Other Irish income | Employment (PAYE), rental, investment |
| Panel D | Foreign income | Employment, self-employment, pensions |
| Panel E | Tax credits and reliefs claimed | Personal credits, health expenses, pension contributions |
| Panel F | Capital gains | CGT events in the year [T3] |
| Panel G | Property details | Owned or rented property [T2/T3] |
| Panel H | Self-assessment | Computed tax, preliminary tax paid, balance due/refund |

**NEVER compute final tax figures directly -- pass taxable income to the deterministic engine to apply rates, USC, PRSI, and credits.**

---

## Step 9: Computation Walkthrough [T1]

### Step-by-Step

1. **Compute Case I/II adjusted profit** (Step 5 above).
2. **Add other income** (employment, rental, investment, foreign).
3. **Total income** = sum of all sources.
4. **Less: Deductions** (pension contributions, losses forward).
5. **Taxable income** = total income minus deductions.
6. **Apply income tax** at 20%/40% per standard rate band (Step 1).
7. **Less: Personal tax credits** (Step 4).
8. **Income tax payable** = gross tax minus credits.
9. **Compute USC** on gross income (Step 2).
10. **Compute PRSI Class S** on gross income (Step 3).
11. **Total tax liability** = income tax payable + USC + PRSI.
12. **Less: Preliminary tax paid** and any withholding tax (PAYE).
13. **Balance due / refund**.

---

## Step 10: Filing Deadlines [T1]

**Legislation:** TCA 1997, s.959I

| Filing / Payment | Deadline |
|-----------------|----------|
| Form 11 (paper filing) | 31 October of the following year |
| Form 11 (ROS e-filing) | Mid-November of the following year (typically 14-18 November) |
| Preliminary tax for current year | Same deadline as Form 11 filing |
| Balance of tax for prior year | Same deadline as Form 11 filing |
| CGT (gains 1 Jan -- 30 Nov) | 15 December of the same year |
| CGT (gains 1 Dec -- 31 Dec) | 31 January of the following year |

### Late Filing Surcharge [T1]

| Delay | Surcharge |
|-------|-----------|
| Filed within 2 months of deadline | 5% of tax due (max EUR 12,695) |
| Filed more than 2 months late | 10% of tax due (max EUR 63,485) |

### Interest on Late Payment [T1]

Interest on overdue tax: 0.0219% per day (approximately 8% per annum). Interest runs from the due date until the date of payment.

---

## Step 11: Penalties [T1]

**Legislation:** TCA 1997, Part 47

| Offence | Penalty |
|---------|---------|
| Late filing surcharge | 5% or 10% (see Step 10) |
| Late payment interest | 0.0219% per day |
| Failure to make a return | Revenue may raise an estimated assessment |
| Incorrect return (no fraud) | Tax-geared penalty up to 100% of underpaid tax |
| Deliberate default / fraud | Penalty up to 100% of tax + publication + possible prosecution |
| Failure to keep records | Up to EUR 3,000 per offence |

---

## Step 12: Record Keeping [T1]

**Legislation:** TCA 1997, s.886

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 6 years from the end of the year of assessment |
| What to keep | All sales invoices, purchase invoices, bank statements, receipts, contracts, asset register, mileage logs |
| Format | Paper or digital (Revenue accepts digital records) |

---

## Step 13: Edge Case Registry

### EC1 -- USC exemption threshold [T1]
**Situation:** Client has total income of EUR 12,500.
**Resolution:** Total income does not exceed EUR 13,000. No USC is payable. Do not apply any USC.

### EC2 -- USC surcharge on self-employment income [T1]
**Situation:** Self-employed client has non-PAYE income of EUR 120,000.
**Resolution:** The 3% USC surcharge applies on all income above EUR 100,000 in addition to the standard 8% rate. Effective rate on income above EUR 100,000 = 11%. Compute standard USC on full income, then add 3% surcharge on the excess above EUR 100,000.

### EC3 -- Motor vehicle cost cap [T1]
**Situation:** Client buys a car for EUR 35,000 and claims 12.5% capital allowance on EUR 35,000.
**Resolution:** INCORRECT. Capital allowances on motor vehicles are capped at a cost of EUR 24,000. Annual allowance = EUR 24,000 x 12.5% = EUR 3,000 (before business-use apportionment).

### EC4 -- Entertainment expenses [T1]
**Situation:** Client includes EUR 1,500 for client entertainment in deductions.
**Resolution:** NOT deductible. Entertainment is blocked under s.840 TCA 1997. Remove from allowable deductions entirely.

### EC5 -- Both PAYE Credit and Earned Income Credit [T1]
**Situation:** Client has employment income and self-employment income. Claims EUR 2,000 PAYE Credit and EUR 2,000 Earned Income Credit.
**Resolution:** Both credits may be claimed on different sources of income. However, the combined total of PAYE Credit and Earned Income Credit cannot exceed EUR 2,000 per person (note: in 2025, EUR 2,000 each is available where there are genuinely separate sources). Flag for reviewer to confirm allocation.

### EC6 -- First year, no preliminary tax [T1]
**Situation:** Client commenced self-employment in 2025. Filing first Form 11.
**Resolution:** No preliminary tax was due for 2025 (no prior year). Full 2025 tax is payable by 31 Oct 2026 (or ROS extended deadline). Preliminary tax for 2026 becomes due at that same deadline.

### EC7 -- PRSI income threshold [T1]
**Situation:** Client has total income of EUR 4,500 from self-employment.
**Resolution:** Total income from all sources is under EUR 5,000. No PRSI Class S is payable.

### EC8 -- Capital item expensed directly [T1]
**Situation:** Client includes a EUR 2,000 laptop as a revenue expense.
**Resolution:** INCORRECT. Capital items must go through capital allowances at 12.5% per annum over 8 years. EUR 2,000 x 12.5% = EUR 250 per year. Remove from revenue deductions and add to capital allowances.

### EC9 -- Married couple, two earners, band allocation [T2]
**Situation:** Married couple where spouse A earns EUR 60,000 (self-employed) and spouse B earns EUR 25,000 (employed). How is the standard rate band allocated?
**Resolution:** Combined band = EUR 53,000 + lower of (EUR 35,000 or spouse B income EUR 25,000) = EUR 78,000 at 20%. Balance of EUR 7,000 (EUR 85,000 - EUR 78,000) at 40%. [T2] Flag for reviewer to confirm band split and credit allocation between spouses.

### EC10 -- Loss relief [T2]
**Situation:** Client has a trading loss of EUR 8,000 in 2025.
**Resolution:** Trading losses may be set off against other income of the same year (s.381 TCA 1997) or carried forward against future profits of the same trade (s.382). [T2] Flag for reviewer to determine optimal loss utilisation strategy.

### EC11 -- Pension contributions [T2]
**Situation:** Self-employed client makes personal pension contributions.
**Resolution:** Deductible within age-related percentage limits (15% of net relevant earnings for under-30s, scaling to 40% for 60+). Annual earnings cap of EUR 115,000 applies. [T2] Flag for reviewer to confirm age bracket and contribution limits.

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
Action Required: Qualified practitioner must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified practitioner. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Standard single self-employed, mid-range income
**Input:** Single, gross revenue EUR 60,000, allowable expenses EUR 15,000, capital allowances EUR 1,250, no other income, no preliminary tax paid (first year).
**Expected output:** Adjusted profit = EUR 43,750. Income tax: EUR 43,750 x 20% = EUR 8,750. Credits: EUR 2,000 (single) + EUR 2,000 (earned income) = EUR 4,000. Tax payable = EUR 4,750. USC: EUR 12,012 x 0.5% + EUR 15,370 x 2% + EUR 16,368 x 3% = EUR 60.06 + EUR 307.40 + EUR 491.04 = EUR 858.50 (on gross EUR 43,750 -- note: USC applies to gross income, adjust accordingly). PRSI: EUR 43,750 x 4.125% = EUR 1,804.69 (above min EUR 650). Total liability = income tax + USC + PRSI.

### Test 2 -- Married one earner, higher income
**Input:** Married (one earner), gross revenue EUR 100,000, allowable expenses EUR 25,000, capital allowances EUR 3,000. No preliminary tax (first year).
**Expected output:** Adjusted profit = EUR 72,000. Income tax: EUR 53,000 x 20% + EUR 19,000 x 40% = EUR 10,600 + EUR 7,600 = EUR 18,200. Credits: EUR 4,000 (married) + EUR 2,000 (earned income) = EUR 6,000. Tax payable = EUR 12,200. Compute USC and PRSI on EUR 72,000.

### Test 3 -- Entertainment expense blocked
**Input:** Client includes EUR 3,000 client entertainment in deductions.
**Expected output:** Remove EUR 3,000 from allowable deductions. Entertainment blocked under s.840 TCA 1997.

### Test 4 -- Motor vehicle cost cap applied
**Input:** Client buys car for EUR 40,000, claims 100% business use.
**Expected output:** Capital allowance capped at EUR 24,000. Annual allowance = EUR 24,000 x 12.5% = EUR 3,000.

### Test 5 -- Preliminary tax computation
**Input:** 2024 final tax liability was EUR 12,000. Client asks for 2025 preliminary tax.
**Expected output:** Preliminary tax due by 31 Oct 2025 (or ROS mid-Nov). Pay at least EUR 12,000 (100% of prior year) or 90% of estimated 2025 liability, whichever is lower.

### Test 6 -- USC surcharge applies
**Input:** Self-employed, non-PAYE income EUR 150,000.
**Expected output:** Standard USC on EUR 150,000 + 3% surcharge on EUR 50,000 (amount above EUR 100,000) = EUR 1,500 additional USC.

### Test 7 -- PRSI below threshold
**Input:** Client has total income of EUR 4,000 from self-employment.
**Expected output:** No PRSI Class S payable. Income below EUR 5,000 threshold.

---

## PROHIBITIONS

- NEVER apply a standard rate band without knowing the client's filing status (single / married / single parent)
- NEVER compute final tax figures directly -- pass taxable income to the deterministic engine to apply rates, credits, USC, and PRSI
- NEVER allow entertainment expenses as a deduction
- NEVER allow income tax, USC, or PRSI as a deduction against trading profits
- NEVER allow fines or penalties as a deduction
- NEVER apply capital allowances on motor vehicles above the EUR 24,000 cost cap
- NEVER allow a capital item to be expensed directly as a revenue deduction -- it must go through capital allowances
- NEVER ignore the USC surcharge for self-employed individuals with non-PAYE income over EUR 100,000
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their practitioner for confirmation
- NEVER advise on Revenue audit or appeal situations without escalating to a qualified practitioner

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
