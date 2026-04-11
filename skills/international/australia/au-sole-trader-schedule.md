---
name: au-sole-trader-schedule
description: >
  Australian sole trader business schedule (Business and Professional Items Schedule for Individuals). Covers assessable business income, allowable deductions, home office (fixed rate 67c/hour or actual), motor vehicle (logbook or cents per km at 85c/km), depreciation (instant asset write-off, simplified pooling, general pooling), prepaid expenses, and trading stock.
version: 1.0
jurisdiction: AU
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Australia Sole Trader Business Schedule v1.0

## What this file is

**Obligation category:** IT (Income Tax)
**Functional role:** Bookkeeping + Computation
**Status:** Complete

This file covers the Business and Professional Items (BPI) schedule that sole traders attach to their individual income tax return. The BPI schedule feeds into the individual return at "Business income or loss" items.

**Tax year coverage.** This skill targets the **2024-25 income year** (1 July 2024 to 30 June 2025).

**The reviewer is the customer of this output.** This skill assumes a credentialed reviewer reviews and signs the return. The skill produces working papers and a brief, not a return.

---

## Section 1 — Scope statement

This skill covers:

- **Forms:** Business and Professional Items Schedule for Individuals (NAT 2816)
- **Entity types:** Sole proprietors operating a business or profession in their individual capacity
- All items P1 through P20 on the schedule

This skill does NOT cover:

- Partnerships (use partnership schedule)
- Companies, trusts, or superannuation funds
- Primary production-specific items (though basic rules noted)
- Personal services income (PSI) determinations in detail — flag for reviewer

---

## Section 2 — Filing requirements

### 2.1 Who must lodge

Any individual who carried on a business as a sole trader during the income year. Even if the business made a loss, the schedule must be lodged. Source: ITAA 1997 s 4-15, ATO instructions for BPI schedule.

### 2.2 Due dates

| Lodgement type | Due date |
|----------------|----------|
| Self-lodgers | 31 October 2025 |
| Tax agent lodgement | Per the ATO tax agent lodgement programme (typically March-May 2026 depending on client category) |

### 2.3 ABN requirement

A sole trader carrying on a business must have an ABN. If they do not have one, they cannot issue valid tax invoices and may face 47% withholding from payers. Source: A New Tax System (Australian Business Number) Act 1999.

---

## Section 3 — Rates and thresholds

| Item | Amount / Rate | Source |
|------|---------------|--------|
| Instant asset write-off threshold | $20,000 per asset (for small business entities with aggregated turnover < $10M) for assets first used or installed ready for use between 1 July 2024 and 30 June 2025 | ITAA 1997 s 328-180 (extended by Treasury Laws Amendment) |
| Small business entity threshold | Aggregated turnover < $10M | ITAA 1997 s 328-110 |
| Cents per km rate (motor vehicle) | 85 cents per km | ATO determination TD 2024/4 |
| Cents per km cap | 5,000 business km per car per year | ITAA 1997 s 28-25 |
| Home office fixed rate | 67 cents per hour | ATO PCG 2023/1 (revised method from 1 July 2022) |
| Trading stock threshold (change in value) | $5,000 — if the difference between opening and closing stock is < $5,000, the taxpayer can elect not to do a stocktake | ITAA 1997 s 70-35 |
| Prepaid expenses (SBE) | Immediately deductible if the service period is 12 months or less and ends on or before 30 June of the following year | ITAA 1997 s 328-225 |

---

## Section 4 — Computation rules

### 4.1 Business income (P8)

**Step 1.** Sum all gross business income received during the year:
- Sales of goods or services
- Government subsidies (e.g., any remaining COVID-era grants assessable)
- Insurance recoveries
- Commissions received

**Step 2.** Exclude amounts that are capital in nature (these go to the CGT schedule).

**Step 3.** Report at P8 on the schedule.

### 4.2 Cost of sales / Cost of goods sold

**Step 1.** Opening stock + Purchases - Closing stock = Cost of goods sold.

**Step 2.** Trading stock can be valued at cost, market selling value, or replacement value (ITAA 1997 s 70-45). The method can differ item by item.

**Step 3.** If the total value of trading stock at year-end differs from opening stock by less than $5,000, the taxpayer can elect to use the same value as opening stock (no stocktake required).

### 4.3 Allowable deductions

Deductions must satisfy the general deduction provision (ITAA 1997 s 8-1): incurred in gaining or producing assessable income, or necessarily incurred in carrying on a business for that purpose. Losses and outgoings of a capital, private, or domestic nature are not deductible (subject to specific provisions).

Key deduction categories on the schedule:

| Label | Category | Notes |
|-------|----------|-------|
| P9 | Motor vehicle expenses | See 4.4 below |
| P10 | Depreciation expenses | See 4.5 below |
| P11 | Repairs and maintenance | Must be revenue not capital |
| P12 | Interest (business portion) | Pro-rate if mixed-use loan |
| P13 | Rent on business premises | Not home office (see P14) |
| P14 | Other business expenses | Includes home office, travel, subscriptions, professional fees |

### 4.4 Motor vehicle expenses

Two methods available for sole traders:

#### Method 1 — Cents per kilometre

- Claim 85c per business km, up to 5,000 km per car per year.
- Maximum claim = 5,000 x $0.85 = $4,250 per car.
- No logbook or written evidence of individual trips required, but must be able to show how the estimate was calculated.

#### Method 2 — Logbook

- Maintain a logbook for a continuous 12-week period (valid for 5 years unless circumstances change).
- Calculate business-use percentage from logbook.
- Apply that percentage to total car expenses: fuel, insurance, registration, repairs, lease payments, depreciation.
- Depreciation of the car is capped at the car limit ($68,108 for 2024-25, ATO car limit determination).

### 4.5 Depreciation

#### Small business simplified depreciation (if SBE)

**Step 1.** Check eligibility: aggregated turnover < $10M.

**Step 2.** Instant asset write-off: assets costing less than $20,000 (excl GST if registered) first used or installed ready for use in the income year are fully deductible in that year.

**Step 3.** Assets costing $20,000 or more go into the small business pool:
- Pool is depreciated at 15% in the first year and 30% each year thereafter (diminishing value).
- If the pool balance falls below the instant asset write-off threshold at the end of the year, the entire pool is written off.

#### General depreciation (non-SBE or election out of simplified)

- Use the effective life determined by the ATO (TR 2024/3) or a self-assessed effective life.
- Choose diminishing value (rate = 200% / effective life) or prime cost (rate = 100% / effective life).
- Apply from the date the asset is first used or installed ready for use.

### 4.6 Home office expenses

#### Fixed rate method (67c per hour) — PCG 2023/1

- Covers energy expenses (electricity, gas), phone, internet, stationery, computer consumables.
- Must keep a record of actual hours worked from home (e.g., timesheets, diary, roster).
- Separately claim occupancy expenses (rent, mortgage interest, rates, insurance) only if the home is a place of business (rare for sole traders without a dedicated area).
- Cannot separately claim expenses already covered by the 67c rate.

#### Actual cost method

- Calculate the actual costs of running the home office.
- Apportion based on floor area of the dedicated work area as a percentage of total home area, and the proportion of the year the area is used for work.
- Keep receipts and records for every expense claimed.

### 4.7 Net business income or loss (P20)

**Step 1.** P20 = P8 (income) - total deductions (P9 through P14 plus any other deductions).

**Step 2.** If P20 is a loss, check the non-commercial business loss rules (ITAA 1997 Div 35):
- The loss can only be offset against other income if one of four tests is met: assessable income test ($20,000), profits test (3 of last 5 years), real property test ($500,000), or other assets test ($100,000).
- If no test is met, the loss is deferred to future years (quarantined).

**Step 3.** P20 feeds into the individual tax return at "Business income or loss."

---

## Section 5 — Edge cases and special rules

### 5.1 Personal services income (PSI)

If more than 80% of the sole trader's income from a contract is for their personal effort or skills, and no PSI determination has been obtained, the income may be PSI. PSI rules deny certain deductions (home office, entertainment, some car expenses). Source: ITAA 1997 Div 84-87. **Flag for reviewer.**

### 5.2 Mixed-use assets

Assets used partly for private and partly for business purposes: claim only the business-use percentage. Maintain records of the split (e.g., logbook for car, diary for home office).

### 5.3 Prepaid expenses (SBE)

Small business entities can immediately deduct prepaid expenses if the service period is 12 months or less and ends by 30 June of the following income year. Example: 12-month insurance premium paid in May 2025 covering May 2025 to April 2026 — fully deductible in 2024-25.

### 5.4 Capital vs revenue

Expenditure that creates a new asset or provides an enduring benefit is capital and not deductible under s 8-1. It may instead be depreciable or added to the cost base for CGT purposes. Common grey areas: website development, major software, business restructuring costs.

### 5.5 Hobby vs business

The ATO may deny deductions if the activity is a hobby, not a business. Indicators of a business: intention to make a profit, repetition and regularity, business-like organisation, size and scale, business plan. Source: ATO guidelines, TR 97/11.

---

## Section 6 — Self-checks

Before delivering output, verify:

- [ ] All income items trace to source documents (invoices, bank statements)
- [ ] Deductions satisfy s 8-1 nexus to assessable income
- [ ] Motor vehicle method is consistently applied (not both methods for same car)
- [ ] Depreciation method matches SBE or general rules as applicable
- [ ] Instant asset write-off threshold ($20,000) is correctly applied
- [ ] Home office hours are supported by records (if fixed rate method)
- [ ] Non-commercial loss rules checked if a loss is reported
- [ ] PSI risk flagged if applicable
- [ ] Trading stock valuation method is documented
- [ ] Rates and thresholds match the 2024-25 income year
- [ ] Output format matches the base skill spec

---

## Section 7 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
