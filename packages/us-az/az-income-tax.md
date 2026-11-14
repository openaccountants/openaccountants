---
name: az-income-tax
description: Compute Arizona individual income tax for tax year 2026 on Form 140, 140PY or 140NR for residents, part-year residents and nonresidents, including sole proprietors. Covers the 2.5% flat rate, the Arizona standard deduction and its new charitable increase (actual contributions up to $1,000 single or $2,000 joint from 2026), the Arizona subtractions for Social Security, US government interest, federal tips, overtime and senior deductions, the dependent credit of $125 and $25, and the estimated tax rule (Arizona gross income over $75,000 or $150,000 joint in both this year and last). Trigger on "Arizona income tax", "AZ income tax", "Form 140", "Arizona estimated tax", "140ES", "Arizona flat tax", "A.R.S. 43-1011". Federal figures live in the federal skills.
version: "1.1"
jurisdiction: US-AZ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Arizona individual income tax, tax year 2026

> **Source-cited draft.** Built from A.R.S. 43-105, 43-501, 43-581, 43-1022, 43-1023, 43-1041 and 43-1073.01 on azleg.gov and the Arizona Department of Revenue (ADOR) withholding page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Arizona taxes 2026 taxable income at a flat **2.5%** for every filing status. Start from federal adjusted gross income, add and subtract the Arizona items, take the Arizona standard deduction (or itemize), then apply 2.5%. From 2026 the standard deduction is increased by the taxpayer's actual charitable contributions, capped at **$1,000** (single or separate) or **$2,000** (joint). The dependent credit is **$125** per dependent under 17 and **$25** for older dependents. Estimated payments are required only when Arizona gross income is over **$75,000** ($150,000 joint) in **both** 2026 and 2025.

## Scope and who this is for

In scope: one individual (or a married couple) filing the 2026 Arizona Form 140 (resident), with the same method on Form 140PY (part-year) and Form 140NR (nonresident); Schedule C, wage and investment income flowing through federal AGI; Arizona estimated tax on Form 140ES.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal AGI, Schedule C and self-employment tax | `us-schedule-c-and-se-computation` |
| Federal figures (tips, overtime and senior deduction amounts, federal standard deduction) | `us-form-1040-individual-return` |
| Arizona employer withholding (Form A-4, A1-QRT) and unemployment insurance | `az-payroll` |
| Arizona corporate tax and the partnership or S corporation entity-level election | `az-corporate-tax` |
| Arizona transaction privilege (sales) tax | `az-sales-tax` |
| Federal estimated tax | `us-quarterly-estimated-tax` |

## Ask the client first

1. Filing status, and were they an Arizona resident for all of 2026? Part-year and nonresident filers use 140PY or 140NR and allocate income.
2. Federal AGI from the 2026 Form 1040, and the federal tips, overtime and senior (age 65 or older) deductions claimed.
3. Social Security or railroad retirement benefits included in federal AGI; interest on US government obligations; interest on non-Arizona municipal bonds.
4. Charitable contributions paid in 2026, and whether they itemize.
5. Dependents, their ages at 31 December 2026, and federal AGI against the $200,000 / $400,000 credit phase-out.
6. Arizona gross income for 2025 and expected for 2026, Arizona withholding to date, and the 2025 Arizona tax (for the estimated tax rule).
7. Any income taxed by another state (credit on Form 309), any Arizona tax credits claimed (school, charitable, foster care), any Arizona net operating loss.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Source |
| --- | --- | --- |
| Tax rate, all filing statuses | 2.5% of Arizona taxable income ("for tax year 2023 and beyond, the tax rate for Arizona taxable income is 2.5%") | [ADOR withholding page](https://azdor.gov/individuals/withholding-tax-individual) |
| Standard deduction, single or married filing separately | $15,750 (2025-2026 filing cycle; ADOR adjusts it for inflation as the federal amount is adjusted, and has not published a 2026 figure) | [A.R.S. 43-1041(A)(1), (H)](https://www.azleg.gov/ars/43/01041.htm) |
| Standard deduction, head of household | $23,625 (2025-2026 filing cycle) | [A.R.S. 43-1041(A)(2), (H)](https://www.azleg.gov/ars/43/01041.htm) |
| Standard deduction, married filing jointly | $31,500 (2025-2026 filing cycle) | [A.R.S. 43-1041(A)(3), (H)](https://www.azleg.gov/ars/43/01041.htm) |
| Charitable increase to the standard deduction (2026 on) | Total charitable contributions under IRC 170(c), up to $1,000 single or separate, $2,000 joint | [A.R.S. 43-1041(I)(2)](https://www.azleg.gov/ars/43/01041.htm) |
| Exemption for age 65 or over, or blind | $1,500 each | [A.R.S. 43-1023(A)](https://www.azleg.gov/ars/43/01023.htm) |
| Dependent credit, federal AGI under $200,000 ($400,000 joint) | $125 per dependent under 17; $25 per dependent 17 or older | [A.R.S. 43-1073.01(B)](https://www.azleg.gov/ars/43/01073-01.htm) |
| Dependent credit phase-out | Each credit reduced by five percent for each $1,000 (or part) of federal AGI over the threshold | [A.R.S. 43-1073.01(C)](https://www.azleg.gov/ars/43/01073-01.htm) |
| Estimated tax required | Arizona gross income over $75,000 ($150,000 joint) in 2026 **and** over that amount in 2025 | [A.R.S. 43-581(A)](https://www.azleg.gov/ars/43/00581.htm) |
| Estimated tax safe harbour | Payments plus withholding of at least ninety percent of 2026 tax or one hundred percent of 2025 tax | [A.R.S. 43-581(A)](https://www.azleg.gov/ars/43/00581.htm) |
| No underpayment penalty | Tax due on the return (after withholding and credits) under $1,000 | [A.R.S. 43-581(E)(2)](https://www.azleg.gov/ars/43/00581.htm) |
| Internal Revenue Code conformity for 2026 | The Code as in effect on 1 January 2026, so the July 2025 federal law is included unless Arizona decouples | [A.R.S. 43-105(A)](https://www.azleg.gov/ars/43/00105.htm) |

### Step 1: federal AGI

Take federal AGI from the 2026 Form 1040. Self-employment items (half of self-employment tax, self-employed health insurance, SEP and solo 401(k) contributions, the home office deduction inside Schedule C) are already in it. The federal qualified business income deduction is below AGI, so it never reaches Arizona.

### Step 2: Arizona additions and subtractions

Main subtractions under [A.R.S. 43-1022](https://www.azleg.gov/ars/43/01022.htm):

| Item | Paragraph |
| --- | --- |
| Social Security and railroad retirement benefits included in federal AGI | (10) |
| Qualified tips deducted federally under IRC 224, to the extent not already excluded | (31), from 2025 |
| Qualified overtime deducted federally under IRC 225, to the extent not already excluded | (32), from 2025 |
| Federal senior deduction under IRC 151(d)(5)(C) | (35), from 2025 |
| Car loan interest deducted under IRC 163(h)(4) | (36), 2025 only, so not for 2026 |
| Distributions from an IRC 530A account | (33), from 2026 |
| Child and dependent care expenses over the federal IRC 21 credit received | (34), from 2026 |

The federal tips, overtime and senior deductions sit below federal AGI, so Arizona gives the same relief through its own subtraction. Use the amounts actually deducted on the federal return; the federal limits are in `us-form-1040-individual-return`. Interest on US government obligations is also subtracted and interest on other states' municipal bonds is added; check the 2026 Form 140 instructions for the full lists when published.

### Step 3: deduction and exemptions

Arizona AGI less the standard deduction (plus the charitable increase) or Arizona itemized deductions, less $1,500 for each age 65 or blind exemption. The charitable increase is only for those who take the standard deduction. Compare standard and itemized every year.

### Step 4: tax and credits

Arizona taxable income x 2.5%. Subtract the dependent credit, the credit for taxes paid to another state (Form 309) and other Arizona credits.

### Step 5: estimated tax

Apply the two-year gross income test of A.R.S. 43-581(A). If both years are over the threshold, pay four installments on the federal due dates totalling the smaller of 90% of 2026 tax and 100% of 2025 tax, less withholding. No penalty applies if the balance due on the return is under $1,000.

### How the result flows on

Tax after credits, less withholding (W-2 box 17) and estimated payments, gives the balance due or refund on Form 140.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Gross income over $75,000 in 2026 but not in 2025 | Estimated payments not required (both years must exceed); voluntary payments allowed under 43-581(B) |
| Charitable gifts of $3,000 by a single filer taking the standard deduction | Increase limited to $1,000 for 2026 (the percentage method ended with 2025) |
| Taxpayer itemizes | No charitable increase; charitable gifts go in itemized deductions |
| Federal tips or overtime deduction | Subtract the same amount in Arizona; never subtract tips or overtime that never entered federal AGI |
| Small business income (Form 140-SBI) election | Separate regime; refer (R-AZ-SBI) |
| Nonresident who worked in Arizona | Form 140NR; Arizona taxes Arizona-source income |
| Partnership or S corporation elected entity-level tax | See `az-corporate-tax` for the owner's side |
| Dependent credit, federal AGI $205,500 single, one child under 17 | $125 less 5% x 6 (six $1,000 steps or part) = $87.50 |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Residency for part of the year | Do not compute; ask (it changes the form) |
| Charitable contributions | Assume none; say so |
| 2025 Arizona gross income | Do not conclude estimates are not required; ask |
| 2026 standard deduction figure | Use the 2025-2026 filing cycle amount and say it may be adjusted |

### Red flags to raise with the client

| Flag | Why |
| --- | --- |
| Withholding at the 2.0% default with large non-wage income | Underpaid by year end; estimates may be required |
| Charitable increase above $1,000 / $2,000 | 2026 cap |
| Social Security not subtracted | Over-taxation |
| Federal car loan interest subtracted for 2026 | The Arizona subtraction was for 2025 only |

## Worked cases

**Case 1, a single sole proprietor.** A single Phoenix web designer has 2026 federal AGI of $80,000, all from Schedule C, no Arizona additions or subtractions, takes the standard deduction ($15,750, 2025-2026 filing cycle figure) and gave $800 to charity. The charitable increase is $800 (under the $1,000 cap). Arizona taxable income: $80,000 less $15,750 less $800 = $63,450. Tax at 2.5%: $1,586.25.

```oa-check
name: AZ 2026 single sole proprietor, standard deduction plus charitable increase
inputs:
  federal_agi: 80000
  standard_deduction: 15750
  charity: 800
  charity_cap: 1000
  rate: 0.025
steps:
  - increase: min(charity, charity_cap)
  - taxable: federal_agi - standard_deduction - increase
  - tax: taxable * rate
expected:
  increase: 800.00
  taxable: 63450.00
  tax: 1586.25
```

**Case 2, a decision: must this couple pay Arizona estimated tax, and how much?** A married couple filing jointly had Arizona gross income of $160,000 in 2025 and expect $170,000 in 2026 (federal AGI $170,000, no Arizona modifications). They take the joint standard deduction ($31,500), have two children under 17, $1,000 of Arizona withholding, and their 2025 Arizona tax was $3,000. Both years are over $150,000, so estimates are required. 2026 tax: ($170,000 less $31,500) x 2.5% = $3,462.50, less the $250 dependent credit = $3,212.50. Required annual payment: the smaller of 90% x $3,212.50 = $2,891.25 and $3,000, so $2,891.25. Less $1,000 withholding leaves $1,891.25, or $472.81 a quarter. Without estimates the balance due would be $2,212.50, over the $1,000 no-penalty line. Decision: pay four installments of $472.81 on the federal dates.

```oa-check
name: AZ 2026 joint estimated tax requirement and installment
inputs:
  federal_agi: 170000
  standard_deduction: 31500
  children_under_17: 2
  withholding: 1000
  prior_year_tax: 3000
  rate: 0.025
steps:
  - tax: (federal_agi - standard_deduction) * rate
  - net_tax: tax - children_under_17 * 125
  - required: min(net_tax * 0.9, prior_year_tax)
  - installment: round((required - withholding) / 4, 2)
  - balance_without_estimates: net_tax - withholding
expected:
  tax: 3462.50
  net_tax: 3212.50
  required: 2891.25
  installment: 472.81
  balance_without_estimates: 2212.50
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-AZ-MULTI | Multistate business activity needing apportionment | Refer |
| R-AZ-PY | Part-year resident with complex sourcing (140PY) | Refer, or compute only with the allocation given |
| R-AZ-SBI | Small business income tax election (Form 140-SBI) cost and benefit | Refer |
| R-AZ-CREDITS | Arizona credits (school tuition, charitable, foster care, solar, research) beyond the dependent credit | Refer; each has its own form and cap |
| R-AZ-NOL | Arizona net operating loss carryforward | Refer |
| R-AZ-TPT | Transaction privilege tax questions | Use `az-sales-tax` |
| R-AZ-AUDIT | Audit, protest or controversy | Refer to an Arizona-licensed practitioner |
| R-AZ-EVADE | Any fraudulent, evasive or aggressive position | Refuse |

## Filing and payment

The 2026 return is due **15 April 2027** ([A.R.S. 43-501](https://www.azleg.gov/ars/43/00501.htm)). File through AZTaxes.gov or approved e-file software. Estimated payments use Form 140ES on the federal installment dates (15 April, 15 June, 15 September 2026 and 15 January 2027). On a bank statement, payments show as "AZ DEPT OF REVENUE", "AZDOR", "ARIZONA DOR" or "AZTAXES.GOV".

## Completion checklist

- Residency and form (140, 140PY or 140NR) settled.
- Social Security, tips, overtime and senior subtractions matched to the federal return.
- Standard deduction flagged as the 2025-2026 filing cycle amount until ADOR publishes 2026.
- Charitable increase capped at $1,000 / $2,000.
- Dependent credit phase-out tested against federal AGI.
- Estimated tax two-year test applied.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| ADOR, Withholding Tax: Individual. Read for "for tax year 2023 and beyond, the tax rate for Arizona taxable income is 2.5%". | https://azdor.gov/individuals/withholding-tax-individual | 2026-11-13 |
| A.R.S. 43-1041. Read for (A) $15,750, $23,625, $31,500, (H) inflation adjustment and (I)(2) the 2026 charitable increase capped at $1,000 / $2,000. | https://www.azleg.gov/ars/43/01041.htm | 2026-11-13 |
| A.R.S. 43-1022. Read for subtractions (10) and (31) to (36). | https://www.azleg.gov/ars/43/01022.htm | 2026-11-13 |
| A.R.S. 43-1023. Read for the $1,500 age and blindness exemption. | https://www.azleg.gov/ars/43/01023.htm | 2026-11-13 |
| A.R.S. 43-1073.01. Read for the $125 / $25 credit and the 5% phase-out over $200,000 / $400,000. | https://www.azleg.gov/ars/43/01073-01.htm | 2026-11-13 |
| A.R.S. 43-581. Read for the $75,000 / $150,000 two-year test, 90% / 100% and the $1,000 no-penalty line. | https://www.azleg.gov/ars/43/00581.htm | 2026-11-13 |
| A.R.S. 43-105. Read for conformity to the Code as of 1 January 2026. | https://www.azleg.gov/ars/43/00105.htm | 2026-11-13 |
| A.R.S. 43-501. Read for the 15 April due date. | https://www.azleg.gov/ars/43/00501.htm | 2026-11-13 |

Not yet confirmed: the 2026 inflation-adjusted Arizona standard deduction (ADOR has not published it; the 2025-2026 filing cycle amounts are shown); 2026 Form 140 line numbers (the 2026 form is not out, so none are quoted); the statutory text of the 2.5% rate in A.R.S. 43-1011 (azleg.gov served an older version of the section, so the rate is cited to ADOR).
