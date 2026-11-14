---
name: az-corporate-tax
description: "Arizona corporate income tax for tax years beginning in 2026 on Form 120. The rate is 4.9% of Arizona taxable income with a $50 minimum. Covers conformity to the Internal Revenue Code as of 1 January 2026, apportionment by election between the double-weighted sales three-factor formula and the sales factor alone, estimated tax when liability is $1,000 or more (90% of this year or 100% of last year), due dates (15th day of the fourth month, S corporations the 15th day of the third month) and the partnership and S corporation entity-level tax election at the top individual rate. Arizona has no franchise or gross receipts tax. Trigger on \"Arizona corporate tax\", \"AZ Form 120\", \"Arizona corporate income tax rate\", \"Arizona apportionment\", \"Arizona sales factor election\", \"Arizona PTE tax\", \"A.R.S. 43-1111\". Federal corporate figures live in us-form-1120-c-corp."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/az-corporate-tax"
  jurisdiction: "US-AZ"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Arizona corporate income tax, tax year 2026

> **Source-cited draft.** Built from A.R.S. 43-105, 43-501, 43-582, 43-1014, 43-1111 and 43-1139 on azleg.gov, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A corporation taxable in Arizona pays **4.9%** of its Arizona taxable income, or **$50** if that is more ([A.R.S. 43-1111](https://www.azleg.gov/ars/43/01111.htm)). A multistate corporation apportions business income by electing either the three-factor formula with the sales factor counted twice, or the sales factor alone ([A.R.S. 43-1139](https://www.azleg.gov/ars/43/01139.htm)). Estimated tax is due when the year's liability is **$1,000** or more. A calendar-year Form 120 is due **15 April 2027**. Arizona has no separate franchise or gross receipts tax.

## Scope and who this is for

In scope: C corporations (and LLCs taxed as corporations) filing Arizona Form 120 for tax years beginning in 2026; the rate and minimum; apportionment election; estimated tax; due dates; and the entity-level tax election open to partnerships and S corporations.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Federal taxable income (Form 1120) | `us-form-1120-c-corp` |
| Federal extension (Form 7004) | `us-corporate-extension-form-7004-and-the` |
| The owner's Arizona individual return | `az-income-tax` |
| Transaction privilege tax | `az-sales-tax` |
| Combined and consolidated returns (Form 120 with unitary groups), insurers, banks with special rules, tax-exempt organizations' unrelated business income | Refer |

## Ask the client first

1. Entity type and federal classification; tax year end.
2. Federal taxable income from the 2026 Form 1120.
3. Is all activity in Arizona? If not: property, payroll and sales in Arizona and everywhere, and the apportionment election made in past years.
4. Is the corporation part of a unitary group (combined or consolidated filing)?
5. Arizona credits claimed, and 2025 Arizona tax (for estimated tax).
6. For partnerships and S corporations: do the owners want the entity-level tax election?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Source |
| --- | --- | --- |
| Corporate rate (tax years beginning after 31 December 2016) | 4.9% of net income | [A.R.S. 43-1111(5)](https://www.azleg.gov/ars/43/01111.htm) |
| Minimum tax | $50 ("the greater of fifty dollars or" the rate) | [A.R.S. 43-1111](https://www.azleg.gov/ars/43/01111.htm) |
| Apportionment (tax years beginning after 31 December 2016) | Elect (a) (property + payroll + 2 x sales) / 4, or (b) the sales factor | [A.R.S. 43-1139(A)(7)](https://www.azleg.gov/ars/43/01139.htm) |
| Estimated tax required | Liability (tax less credits) of $1,000 or more | [A.R.S. 43-582(A)](https://www.azleg.gov/ars/43/00582.htm) |
| Required annual payment | Lesser of 90% of this year's tax and 100% of last year's (last year's not usable after a short year or no return; large corporations use 90% of this year except for the first installment) | [A.R.S. 43-582(B), (C)](https://www.azleg.gov/ars/43/00582.htm) |
| Due date, C corporation | 15 April for calendar years; 15th day of the fourth month after a fiscal year end | [A.R.S. 43-501](https://www.azleg.gov/ars/43/00501.htm) |
| Due date, S corporation | 15th day of the third month after year end | [A.R.S. 43-501(1)](https://www.azleg.gov/ars/43/00501.htm) |
| Code conformity for tax years beginning in 2026 | The Internal Revenue Code as in effect on 1 January 2026 | [A.R.S. 43-105(A)](https://www.azleg.gov/ars/43/00105.htm) |
| Partnership or S corporation entity-level tax | Elective, at the highest individual rate under A.R.S. 43-1011 (2.5%) on income of resident owners and Arizona-source income | [A.R.S. 43-1014(A)](https://www.azleg.gov/ars/43/01014.htm) |

### Step 1: start from federal taxable income

Arizona taxable income starts from federal taxable income under the Code as of 1 January 2026, with the Arizona additions and subtractions shown on Form 120 (for example, Arizona's own depreciation and interest adjustments). Check the 2026 Form 120 instructions when published for the line list.

### Step 2: apportion

If the corporation does business both in and outside Arizona, compute business income apportioned to Arizona under both formulas in A.R.S. 43-1139(A)(7) and elect the one that suits the corporation (usually the lower result, but the election should also be weighed against future years). Non-business income is allocated separately.

### Step 3: tax

Arizona taxable income x 4.9%, with a floor of $50. Subtract Arizona credits.

### Step 4: estimated tax and filing

If the year's liability is $1,000 or more, pay estimates on the federal installment pattern totalling the lesser of 90% of this year's tax and 100% of last year's. File Form 120 by the due date.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Arizona taxable income $800 | 4.9% is $39.20; the $50 minimum applies |
| Loss year | The $50 minimum still applies to a corporation subject to tax |
| Large Arizona sales, property and payroll mostly outside | The sales factor election usually raises Arizona's share; compare both |
| Mostly Arizona sales, property and payroll largely elsewhere | The sales factor election usually lowers it |
| Liability $900 | No estimated tax required |
| S corporation | Form 120S, due the 15th day of the third month; owners pay unless the entity-level election is made |
| Partnership or S corporation elects entity-level tax | Tax at 2.5% at entity level on resident owners' share and Arizona-source income; estimated tax if prior-year taxable income exceeded $150,000 (A.R.S. 43-581(C)) |
| Franchise tax or gross receipts tax question | Arizona has neither for corporations; transaction privilege tax is separate (`az-sales-tax`) |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Apportionment factors | Do not compute; ask |
| Prior-year election | Compare both formulas and flag |
| Unitary group facts | Do not compute; refer |

### Red flags to raise with the client

| Flag | Why |
| --- | --- |
| Rate of 6.968% or 5.5% used | Pre-2017 rates; 4.9% applies |
| No return filed because of a loss | The $50 minimum still applies |
| S corporation filing on 15 April | Due the 15th day of the third month |

## Worked cases

**Case 1, a decision: which apportionment formula?** A corporation has $1,000,000 of business income. Arizona holds 40% of its property, 50% of its payroll and 20% of its sales. Three-factor with double sales: (0.40 + 0.50 + 2 x 0.20) / 4 = 32.5%, so $325,000 apportioned and $15,925.00 of tax. Sales factor alone: 20%, so $200,000 and $9,800.00. Decision: elect the sales factor; it saves $6,125.00 this year.

```oa-check
name: AZ 2026 apportionment election, double-weighted three-factor against sales factor
inputs:
  income: 1000000
  property: 0.40
  payroll: 0.50
  sales: 0.20
  rate: 0.049
steps:
  - three_factor: (property + payroll + 2 * sales) / 4
  - tax_three_factor: income * three_factor * rate
  - tax_sales_factor: income * sales * rate
  - saving: tax_three_factor - tax_sales_factor
expected:
  three_factor: 0.325
  tax_three_factor: 15925.00
  tax_sales_factor: 9800.00
  saving: 6125.00
```

**Case 2, the minimum tax.** A small Arizona-only corporation has Arizona taxable income of $800. Tax at 4.9% is $39.20, below the minimum, so it owes $50.00. Its liability is under $1,000, so no estimated tax was required.

```oa-check
name: AZ 2026 corporate tax with the 50 dollar minimum
inputs:
  taxable_income: 800
  rate: 0.049
  minimum: 50
steps:
  - computed: taxable_income * rate
  - tax: max(minimum, computed)
expected:
  computed: 39.20
  tax: 50.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-AZ-CT-1 | Unitary group, combined or consolidated return | Refer |
| R-AZ-CT-2 | Non-business income allocation, special industry apportionment (airlines, railroads, pipelines) | Refer |
| R-AZ-CT-3 | Arizona credits (research, renewable energy, school tuition) | Refer |
| R-AZ-CT-4 | Arizona net operating loss history | Refer |
| R-AZ-CT-5 | Audit, protest or voluntary disclosure | Refer to an Arizona-licensed practitioner |

## Filing and payment

File Form 120 (Form 120S for S corporations, Form 165 for partnerships) through approved e-file software or AZTaxes.gov where available, and pay through AZTaxes.gov. A calendar-year 2026 C corporation return is due 15 April 2027; an S corporation return 15 March 2027. Estimated payments follow the federal corporate installment months. Check the 2026 Form 120 instructions for the Arizona extension rules.

## Completion checklist

- Federal taxable income taken under the 1 January 2026 Code.
- Apportionment computed both ways and the election recorded.
- 4.9% applied, $50 minimum tested.
- Estimated tax test at $1,000.
- Correct due date for the entity type.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| A.R.S. 43-1111. Read for "the greater of fifty dollars or" 4.9% for years beginning after 31 December 2016. | https://www.azleg.gov/ars/43/01111.htm | 2026-11-13 |
| A.R.S. 43-1139. Read for (A)(7), the election between (property + payroll + 2 x sales) / 4 and the sales factor. | https://www.azleg.gov/ars/43/01139.htm | 2026-11-13 |
| A.R.S. 43-582. Read for the $1,000 threshold and the 90% / 100% required payment. | https://www.azleg.gov/ars/43/00582.htm | 2026-11-13 |
| A.R.S. 43-501. Read for the 15th day of the fourth month and, for S corporations, the third month. | https://www.azleg.gov/ars/43/00501.htm | 2026-11-13 |
| A.R.S. 43-105. Read for conformity to the Code as of 1 January 2026. | https://www.azleg.gov/ars/43/00105.htm | 2026-11-13 |
| A.R.S. 43-1014. Read for the partnership and S corporation entity-level election at the highest individual rate. | https://www.azleg.gov/ars/43/01014.htm | 2026-11-13 |

Not yet confirmed: the 2026 Form 120 and its instructions (not opened: ADOR's site blocks scripts and the corporate page could not be found), so no line numbers, Arizona additions and subtractions list or extension rule are quoted; the ADOR corporate e-file requirement.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `az-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/az-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
