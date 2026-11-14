---
name: nd-transfer-pricing
description: >-
  Use when a corporate group with North Dakota nexus needs the 2026 answer
  on North Dakota connected-party and unitary rules, namely worldwide combined
  reporting for a unitary business, the water's-edge election under
  N.D.C.C. 57-38.4-02 with its 3.5% additional tax and its foreign-dividend
  and 80/20 inclusion shares, the equally weighted three-factor formula with
  the single-sales-factor election under 57-38.1-09(4), and alternative
  apportionment under 57-38.1-18. Trigger on North Dakota combined return,
  ND unitary, water's edge surtax, 57-38.4-02, 57-38.1-18, ND intercompany,
  ND addback.
jurisdiction: US-ND
type: decision
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-11-14
version: "1.1"
---

# North Dakota transfer pricing (combined reporting, water's edge, apportionment), tax year 2026

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Answer first.** North Dakota does not police intercompany prices mainly through separate-entity transfer pricing adjustments. A corporation in a unitary business with other corporations, wherever they are, must file using the worldwide combined report method, so intercompany income and charges largely wash out inside the group. A group can elect the water's-edge method instead, binding for five years, at the price of an additional 3.5% tax on North Dakota taxable income. Where the formula does not fairly represent the business in North Dakota, the taxpayer may petition for, or the Tax Commissioner may require, separate accounting or another method under N.D.C.C. 57-38.1-18. The ordinary corporate rate schedule is owned by `nd-corporate-tax`.

## Who this applies to

C corporations filing North Dakota Form 40 that belong to a group under common control (more than 50% of voting stock) with intercompany debt, intangibles, management fees or factoring, and any multinational choosing between worldwide and water's-edge combined reporting. The [2025 Form 40 instructions](https://www.tax.nd.gov/sites/default/files/documents/forms/business/corporate-income/2025-corp/28714-corp-income-tax-booklet-2025.pdf) (2025-2026 filing cycle) say: "A corporation engaged in a unitary business with one or more corporations (irrespective of the country or countries in which the corporations conduct business) must file using the combined report method."

A unitary business transfers value among its parts through unity of ownership (common control of more than 50% of voting stock by a group member), unity of operation (functional integration, economies of scale) and unity of use (centralized management and policy). With unity of ownership, the same general line of business, steps in a vertically structured enterprise, or centralized management create a presumption of a unitary business (same instructions).

## Rates, bands and thresholds

The graduated corporate schedule (1.41%, 3.55%, 4.31%) is owned by `nd-corporate-tax`; the worked examples below use it as published on the [Tax Commissioner's corporate page](https://www.tax.nd.gov/corporate-income-tax). The connected-party figures are:

| Item | Amount, tax year 2026 | Official source |
| --- | --- | --- |
| Additional tax on a water's-edge elector, on top of the 57-38-30(1) tax | 3.5% of taxable income | [N.D.C.C. 57-38.4-02(3)](https://ndlegis.gov/cencode/t57c38-4.pdf); [Tax Commissioner corporate page](https://www.tax.nd.gov/corporate-income-tax) |
| Water's-edge election: binding period | five consecutive taxable years | [N.D.C.C. 57-38.4-02(1)(b)](https://ndlegis.gov/cencode/t57c38-4.pdf) |
| Water's-edge inclusion, existing corporation: foreign dividends / income from 80/20 corporations | Fifty percent / sixty percent | [N.D.C.C. 57-38.4-02(2)(a)](https://ndlegis.gov/cencode/t57c38-4.pdf) |
| Water's-edge inclusion, new corporation, or existing corporation raising threshold activity by twenty-five percent or more | 30% / 30% | [N.D.C.C. 57-38.4-02(2)(a) and (b)](https://ndlegis.gov/cencode/t57c38-4.pdf) |
| Any electing corporation, taxable years after 1994, may reduce the inclusion to | 30% / 30% | [N.D.C.C. 57-38.4-02(2)(c)](https://ndlegis.gov/cencode/t57c38-4.pdf) |
| Water's-edge group: US-incorporated affiliate included if property and payroll inside the US exceed | 20% | [N.D.C.C. 57-38.4-01(7)(a)](https://ndlegis.gov/cencode/t57c38-4.pdf) |
| Affiliated corporation: voting stock owned by the parent or group | More than fifty percent | [N.D.C.C. 57-38.4-01(1)](https://ndlegis.gov/cencode/t57c38-4.pdf) |
| Default apportionment fraction | (property + payroll + sales) / 3 | [N.D.C.C. 57-38.1-09(1)](https://ndlegis.gov/cencode/t57c38-1.pdf) |
| Single-sales-factor election (non-passthrough taxpayer, years after 2018): binding period | five consecutive taxable years, then lapses | [N.D.C.C. 57-38.1-09(4)(c)](https://ndlegis.gov/cencode/t57c38-1.pdf) |
| Waiting period before a new single-sales-factor election if not renewed in the next year | three taxable years on the default formula | [N.D.C.C. 57-38.1-09(4)(d)](https://ndlegis.gov/cencode/t57c38-1.pdf) |
| Corporation estimated tax required when both the prior-year liability and the expected current liability exceed | Five thousand dollars | [N.D.C.C. 57-38-62(2)](https://ndlegis.gov/cencode/t57c38.pdf) |
| Interest on underpaid corporate estimates | 12% per annum | [2026 Form 40-ES, kept in the agency's 2025-corp folder](https://www.tax.nd.gov/sites/www/files/documents/forms/business/corporate-income/2025-corp/28716-form-40-es-2026.pdf) |

## The base

1. **Starting point:** federal taxable income. If the combined report excludes a corporation that was in the federal consolidated return, start from the pro forma federal taxable income of the combined group members that were in the federal consolidated return. Nonconsolidated affiliates added to the North Dakota combined group bring their federal taxable income as actually reported; federal consolidated return rules are not reapplied to the larger group ([2025 Form 40 instructions](https://www.tax.nd.gov/sites/default/files/documents/forms/business/corporate-income/2025-corp/28714-corp-income-tax-booklet-2025.pdf)).
2. **Treaties:** North Dakota does not recognize treaty adjustments to federal taxable income; a Form 1120-F filer prepares a pro forma Form 1120 without the treaty position (same instructions).
3. **Combine and eliminate:** on the combined report, intercompany income and expense among unitary members is eliminated, so a royalty, interest or management charge between members does not move income out of the combined base. Use the pro forma or by-company figures the instructions require.
4. **Water's-edge election if made:** include the water's-edge group defined in 57-38.4-01(7) (US affiliates with more than 20% of property and payroll inside the US, DISCs and FSCs, export trade corporations, foreign corporations to the extent of US real property gains, and foreign-incorporated majority-owned affiliates with more than 20% of payroll and property assignable inside the US), plus the inclusion shares of foreign dividends and 80/20 income in the table. Then add the 3.5% tax.
5. **Apportion:** the equally weighted three-factor default, or the single sales factor if elected, applying to all companies in the unitary group ([57-38.1-09(4)(b)](https://ndlegis.gov/cencode/t57c38-1.pdf)).
6. **Alternative methods:** if the allocation and apportionment rules do not fairly represent the business activity in North Dakota, the taxpayer may petition for, or the Commissioner may require, separate accounting, excluding a factor, adding a factor, or any other method for an equitable result ([N.D.C.C. 57-38.1-18](https://ndlegis.gov/cencode/t57c38-1.pdf)). For a water's-edge group, the Commissioner may impose other conditions, short of worldwide combination, to prevent tax avoidance or clearly reflect income ([N.D.C.C. 57-38.4-03](https://ndlegis.gov/cencode/t57c38-4.pdf)).

## Deadlines and filing

- **Form 40:** the ordinary and extended due dates are owned by `nd-corporate-tax` (generally the 15th day of the 4th month after year end for calendar filers).
- **Water's-edge election:** made on the return as originally and timely filed ([57-38.4-02(1)(a)](https://ndlegis.gov/cencode/t57c38-4.pdf)); the instructions say "must be made on the return as originally filed and is binding for five consecutive tax years" ([2025 Form 40 instructions](https://www.tax.nd.gov/sites/default/files/documents/forms/business/corporate-income/2025-corp/28714-corp-income-tax-booklet-2025.pdf)).
- **Single-sales-factor election:** made on the return as originally and timely filed, in the form the Commissioner prescribes ([57-38.1-09(4)(a)](https://ndlegis.gov/cencode/t57c38-1.pdf)).
- **Estimated payments:** Form 40-ES, not the individual `nd-estimated-tax` skill. Required when both the prior-year net tax liability and the expected current-year tax exceed USD 5,000; pay the lesser of 90% of the current year or 100% of the prior year ([57-38-62(2)](https://ndlegis.gov/cencode/t57c38.pdf); [2026 Form 40-ES](https://www.tax.nd.gov/sites/www/files/documents/forms/business/corporate-income/2025-corp/28716-form-40-es-2026.pdf)).

## Penalties and interest

- **Underpaid estimates:** interest at 12% per annum from the installment due date to the earlier of the payment date or the due date (without extension) of the return; it applies if a quarter's payment is less than 90% of the quarterly liability or less than the prior year's net tax liability divided by four; computed on Form 40-UT ([2026 Form 40-ES](https://www.tax.nd.gov/sites/www/files/documents/forms/business/corporate-income/2025-corp/28716-form-40-es-2026.pdf)).
- **Late payment and late filing:** 5% of unpaid tax or USD 5; late filing 5% per month or part up to 25%; interest 1% per month or part, excluding the month due; a corporation that still fails to file 30 days after notice can be assessed up to USD 500 per failure ([N.D.C.C. 57-38-45(1), (2) and (7)](https://ndlegis.gov/cencode/t57c38.pdf)).
- **Audit theme:** intercompany intangible, interest and management-fee charges are the usual target; the Commissioner's tools are unitary combination and 57-38.1-18 alternative apportionment.

## Cross-border points

- **Foreign affiliates:** the water's-edge election is the gate between worldwide and mostly US-only combined reporting; the 3.5% additional tax and the foreign-dividend and 80/20 inclusions are its price.
- **Federal related-party rules** (section 267 deferrals, section 163(j) interest limits, section 482 adjustments) change federal taxable income and therefore the North Dakota starting point; they belong to the federal skills.
- **Treaties:** not recognized for North Dakota corporate income (see The base, point 2).
- **Joyce and Finnigan:** how the factors of a non-nexus member enter the North Dakota sales fraction was not established from the sources read for this skill. Flag for a multistate specialist.

## Two worked examples that recompute

**Example 1: standalone North Dakota corporation, USD 100,000 North Dakota taxable income, no water's-edge election.** Using the corporate page's schedule (owned by `nd-corporate-tax`): USD 352.50 on the first USD 25,000, 3.55% on the next USD 25,000, then 4.31% above USD 50,000.

```oa-check
name: ND corporate tax, 100,000 taxable income
inputs:
  ti: 100000
steps:
  - b1: 352.50
  - b2: (min(ti, 50000) - 25000) * 0.0355
  - b3: (ti - 50000) * 0.0431
  - tax: b1 + b2 + b3
expected:
  tax: 3395.00
```

**Example 2: decision, worldwide combined report or water's-edge election?** A group's North Dakota taxable income is USD 260,000 on a worldwide combined report. On a water's-edge basis, excluding low-taxed foreign affiliates but including the required share of foreign dividends, it would be USD 200,000 (figures invented for the example). Worldwide tax: 1,240 + (260,000 - 50,000) x 4.31% = USD 10,291.00. Water's-edge tax: 1,240 + (200,000 - 50,000) x 4.31% = USD 7,705.00, plus 3.5% x 200,000 = USD 7,000.00, total USD 14,705.00.

- **The figure that decides:** water's edge costs USD 4,414.00 more here. Taxable income would have to fall well below USD 200,000 on the water's-edge base before the 3.5% additional tax is paid back, and the choice binds for five years. Model each of the five years before electing.

```oa-check
name: ND worldwide combined versus water's-edge election
inputs:
  ti_worldwide: 260000
  ti_waters_edge: 200000
steps:
  - tax_worldwide: 1240 + (ti_worldwide - 50000) * 0.0431
  - base_we: 1240 + (ti_waters_edge - 50000) * 0.0431
  - additional_we: ti_waters_edge * 0.035
  - tax_waters_edge: base_we + additional_we
  - extra_cost_of_election: tax_waters_edge - tax_worldwide
expected:
  tax_worldwide: 10291.00
  base_we: 7705.00
  additional_we: 7000.00
  tax_waters_edge: 14705.00
  extra_cost_of_election: 4414.00
```

## Ask the client first

1. Is the group unitary: common control of more than 50% of voting stock, plus functional integration or centralized management?
2. Worldwide or water's edge? If elected, in which year, and when does the five-year binding period end? Is the corporation "existing" or "new" for the inclusion shares?
3. Are intercompany interest, royalties and management fees documented, and between which members (inside or outside the combined group)?
4. Has the group made the single-sales-factor election, and when does its five-year period end?
5. Do other states' combined-reporting rules include or exclude the same members differently (keep both computations in the file)?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| N.D.C.C. chapter 57-38.4. Read for sections 57-38.4-01 (definitions, water's-edge group), 57-38.4-02 (election, inclusion shares, three and one-half percent additional tax) and 57-38.4-03 (conditions). | https://ndlegis.gov/cencode/t57c38-4.pdf | 2026-11-14 |
| N.D.C.C. chapter 57-38.1. Read for section 57-38.1-09 (three-factor default, single-sales-factor election and its binding and waiting periods), 57-38.1-18 (alternative methods) and 57-38.1-19 (a uniformity purpose clause, not combined reporting). | https://ndlegis.gov/cencode/t57c38-1.pdf | 2026-11-14 |
| N.D.C.C. chapter 57-38. Read for sections 57-38-30 (corporate rates), 57-38-45 (penalties and interest) and 57-38-62(2) (corporate estimated tax). | https://ndlegis.gov/cencode/t57c38.pdf | 2026-11-14 |
| 2025 Form 40 instructions, 2025-2026 filing cycle. Read for the combined report requirement, unitary business definition and presumptions, pro forma starting point, treaty rule and the water's-edge election paragraph. | https://www.tax.nd.gov/sites/default/files/documents/forms/business/corporate-income/2025-corp/28714-corp-income-tax-booklet-2025.pdf | 2026-11-14 |
| 2026 Form 40-ES, kept in the agency's 2025-corp folder. Read for the USD 5,000 tests, the quarterly interest conditions, Form 40-UT and the 12% per annum interest. | https://www.tax.nd.gov/sites/www/files/documents/forms/business/corporate-income/2025-corp/28716-form-40-es-2026.pdf | 2026-11-14 |
| Tax Commissioner corporate income tax page. Read for the rate table, the 3.5% water's-edge surtax sentence and "Corporate tax rates have remained unchanged since 2015." | https://www.tax.nd.gov/corporate-income-tax | 2026-11-14 |

Not yet confirmed: the 2026 Form 40 line for the water's-edge additional tax and the 2026 instructions (the 2025 instructions are used, labelled 2025-2026 filing cycle); North Dakota's Joyce or Finnigan position for the sales factor of non-nexus members; whether North Dakota offers a pass-through entity tax election for 2026 (the old file's "no PTET" statement is not carried as a rule); the statute that makes worldwide combination mandatory beyond the instructions and 57-38.4-02's opening sentence.
