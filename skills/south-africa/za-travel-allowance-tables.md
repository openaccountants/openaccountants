---
name: za-travel-allowance-tables
description: >
  South African travel allowance and logbook rate tables for the 2027 year of assessment (1 March 2026 to 28 February 2027, written 2026/27) and the 2026 year of assessment, each row linked to the SARS page it was read on. Holds the cost scale (fixed cost, fuel cost and maintenance cost by vehicle value) used for the deemed-cost business travel deduction under section 8(1)(b), the simplified rate per kilometre for reimbursive allowances, and the 80 percent and 20 percent PAYE inclusion rules. Use for any South African travel allowance, logbook claim, rate per kilometre, company car versus allowance, or ITR12 travel deduction question for 2026/27 or 2025/26. Earlier years sit in the accountant-approved travel allowance tables file.
version: 1.0
jurisdiction: ZA
tax_year: 2026
tax_year_notes: "2026-27, the 2027 year of assessment (1 March 2026 to 28 February 2027); the 2026 year of assessment (2025-26) is kept for returns now being filed"
last_updated: 2026-11-14
depends_on:
  - workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: rates-card
---

# South Africa: travel allowance and logbook rate tables, years of assessment 2026 and 2027

The SARS cost scale and the simplified rate per kilometre. Data only, with one worked example: this file states the rates and where they come from. How to apportion business kilometres in a return belongs to `za-income-tax`; payroll treatment belongs to `za-payroll-paye-uif-sdl`. The years of assessment 2023, 2024 and 2025 are in the accountant-approved file `travel-allowance-and-logbook-rate-tables-2023-to-2027`; they were not reopened on a SARS page today and are not restated here.

**Current year:** the 2027 year of assessment, 1 March 2026 to 28 February 2027 (commonly written 2026/27). SARS numbers a year of assessment by the calendar year in which it ends.

## Scope

- The **cost scale** (s 8(1)(b)(ii) and (iii)): fixed cost, fuel cost and maintenance cost by the value of the vehicle, used for the deemed-cost travel deduction against an allowance or advance where actual costs are not claimed.
- The **simplified rate per kilometre** (cost scale para 1.4) for a reimbursive allowance paid on actual business kilometres.
- The PAYE inclusion of a fixed travel allowance.

Not covered: whether a logbook meets SARS's standard, actual-cost claims, company car fringe benefits, subsistence allowances, and the IRP5 codes 3701, 3702 and 3703.

## Rates, bands and thresholds

### Cost scale, YoA 2027 (2026/27), effective 1 March 2026

Fixed cost is an annual rand amount. Fuel and maintenance are in **cents per kilometre**. The band is set by the **value** of the vehicle as the schedule defines it (cost including VAT, excluding finance charges, for a vehicle bought at arm's length).

| Value of the vehicle (R) | Fixed cost (R a year) | Fuel cost (c/km) | Maintenance cost (c/km) | Source |
| --- | --- | --- | --- | --- |
| 0 to 115,000 | 38,344 | 132.9 | 49.1 | https://www.sars.gov.za/wp-content/uploads/Docs/PAYE/Tables/tables2026/PAYE-GEN-01-G03-A01-Rate-per-Kilometre-Schedule-External-Annexure.pdf |
| 115,001 to 230,000 | 68,487 | 148.4 | 61.4 | same |
| 230,001 to 345,000 | 98,689 | 161.2 | 67.8 | same |
| 345,001 to 460,000 | 125,393 | 173.4 | 74.0 | same |
| 460,001 to 575,000 | 152,097 | 185.5 | 86.9 | same |
| 575,001 to 690,000 | 180,078 | 212.8 | 102.0 | same |
| 690,001 to 805,000 | 208,106 | 216.5 | 114.5 | same |
| 805,001 to 920,000 (maintenance: see note) | 237,679 | 220.1 | see note below the table | same |
| exceeding 920,000 | 237,679 | 220.1 | 126.9 | same |

Note on the 805,001 to 920,000 band: the SARS schedule (PAYE-GEN-01-G03-A01, Revision 19) gives **126.1 c/km** for maintenance; the SARS Budget Tax Guide 2026 gives **126.9 c/km** for the same band. The Government Notice fixing the rate (the law text) was not opened today, so the figure is listed under "Not yet confirmed" and neither value is used here. For a vehicle in that band, read the notice before claiming maintenance cost.

### Cost scale, YoA 2026 (2025/26), from 1 March 2025

| Value of the vehicle (R) | Fixed cost (R a year) | Fuel cost (c/km) | Maintenance cost (c/km) | Source |
| --- | --- | --- | --- | --- |
| 0 to 100,000 | 33,940 | 146.7 | 47.4 | https://www.sars.gov.za/budget-tax-guide-21-may-2025/ |
| 100,001 to 200,000 | 60,688 | 163.8 | 59.3 | same |
| 200,001 to 300,000 | 87,497 | 177.9 | 65.4 | same |
| 300,001 to 400,000 | 111,273 | 191.4 | 71.4 | same |
| 400,001 to 500,000 | 135,048 | 204.8 | 83.9 | same |
| 500,001 to 600,000 | 159,934 | 234.9 | 98.5 | same |
| 600,001 to 700,000 | 184,867 | 238.9 | 110.5 | same |
| 700,001 to 800,000 | 211,121 | 242.9 | 122.5 | same |
| exceeding 800,000 | 211,121 | 242.9 | 122.5 | same |

### Simplified rate per kilometre and PAYE inclusion

| Item | YoA 2027 (2026/27) | YoA 2026 (2025/26) | Source |
| --- | --- | --- | --- |
| Simplified rate per kilometre (reimbursive allowance, no other vehicle compensation except parking or tolls) | 495 cents (R4.95) | R4.76 | https://www.sars.gov.za/wp-content/uploads/Docs/PAYE/Tables/tables2026/PAYE-GEN-01-G03-A01-Rate-per-Kilometre-Schedule-External-Annexure.pdf (2027); https://www.sars.gov.za/budget-tax-guide-21-may-2025/ (2026) |
| Share of a fixed travel allowance included in remuneration for PAYE | 80% | 80% | https://www.sars.gov.za/tax-rates/employers/rates-per-kilometre/ |
| Reduced share where the employer is satisfied business use is at least 80% | 20% | 20% | same |

### How the cost scale is applied

The rate per kilometre is the sum of: the fixed cost divided by the **total** kilometres travelled in the year (private and business); the fuel cost, only if the recipient bore the full cost of fuel; and the maintenance cost, only if the recipient bore the full cost of maintenance (repairs, servicing, lubrication, tyres). A vehicle under a maintenance plan carries no maintenance cost. Where the vehicle was used for business for less than the full year, the fixed cost is reduced in the ratio of the days of business use to 365. Business kilometres must be proven by a logbook. The deduction is the rate per kilometre times business kilometres, set against the allowance.

### Edge cases and traps

- **The rate can go down.** The simplified rate was R4.76 for YoA 2026 and 495 cents for YoA 2027, and the approved sibling file shows it fell into YoA 2026. A table that only ever rises is wrong.
- **The open top band does not always repeat the band below.** In the 2027 schedule the open band carries 126.9 c/km maintenance; the band below is in dispute between two SARS documents (see the note). Never "tidy" a top band to match the one beneath it: read the schedule for the year.
- **Band widths changed in YoA 2027**, from R100,000 steps to R115,000 steps. Do not carry a prior-year band structure forward.
- **Value, not market value today**, sets the band: the schedule's definition (para 1.3) uses original cost including VAT for a vehicle bought at arm's length, the cash value under an instalment credit lease, or market value plus notional VAT in other cases.
- **The simplified rate is not available** if any other allowance or reimbursement (other than parking or tolls) is paid for the same vehicle.

### Self-checks

1. **Band continuity.** Each band floor is the previous band ceiling plus R1.
2. **Year check.** The cost scale changes on 1 March; the year of assessment, not the calendar year, picks the table.
3. **Fuel and maintenance only if borne in full.** If the employer pays fuel by card, the fuel column is zero.

### Worked example: fixed allowance, YoA 2027

An employee receives a fixed travel allowance. The vehicle cost R400,000 including VAT, so it sits in the R345,001 to R460,000 band. The logbook shows 30,000 km in total for the year, 12,000 km of them for business. The employee pays all fuel and maintenance and used the car for business all year.

- Fixed cost per km: R125,393 / 30,000 = R4.17977.
- Rate per km: R4.17977 + R1.734 (fuel) + R0.740 (maintenance) = R6.65377.
- Deduction: 12,000 x R6.65377 = **R79,845.20** against the allowance.

```oa-check
name: YoA 2027 fixed travel allowance, vehicle R400,000, 12,000 business km of 30,000
inputs:
  fixed_cost: 125393
  fuel_c_per_km: 173.4
  maintenance_c_per_km: 74.0
  total_km: 30000
  business_km: 12000
steps:
  - fixed_per_km: fixed_cost / total_km
  - rate_per_km: fixed_per_km + fuel_c_per_km / 100 + maintenance_c_per_km / 100
  - deduction: rate_per_km * business_km
expected:
  deduction: 79845.20
```

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| SARS, PAYE-GEN-01-G03-A01 Rate per Kilometre Schedule (2027 Tax Year), Revision 19, effective 1 March 2026: read for paras 1.1 to 1.4, the cost scale, the value definition and the 495 cents simplified rate | https://www.sars.gov.za/wp-content/uploads/Docs/PAYE/Tables/tables2026/PAYE-GEN-01-G03-A01-Rate-per-Kilometre-Schedule-External-Annexure.pdf | 2026-11-14 |
| SARS, Rates per kilometre page (updated 26 February 2026): read for the 80% and 20% PAYE inclusion and the fuel, maintenance and pro rata rules | https://www.sars.gov.za/tax-rates/employers/rates-per-kilometre/ | 2026-11-14 |
| SARS, Budget Tax Guide 2026: read for the 2026/27 travelling allowance table (cross-check; differs on the 805,001 to 920,000 maintenance cost) and the R4.95 simplified rate | https://www.sars.gov.za/budget-tax-guide-2026-online-version-for-printing/ | 2026-11-14 |
| SARS, Budget Tax Guide 21 May 2025 (1 March 2025 to 28 February 2026): read for the YoA 2026 travelling allowance table and the R4.76 rate | https://www.sars.gov.za/budget-tax-guide-21-may-2025/ | 2026-11-14 |
| SARS, PAYE-GEN-01-G03 Guide for Employers in respect of Allowances: read for the general allowance rules (opened, not quoted for any figure) | https://www.sars.gov.za/wp-content/uploads/Ops/Guides/PAYE-GEN-01-G03-Guide-for-Employers-in-respect-of-Allowances-External-Guide.pdf | 2026-11-14 |

Not yet confirmed: the maintenance cost for the 805,001 to 920,000 band in YoA 2027 (SARS schedule Revision 19 says 126.1 c/km; SARS Budget Tax Guide 2026 says 126.9 c/km; the Government Notice under s 8(1)(b)(ii) and (iii) was not found on the SARS income tax notices pages, which returned errors). The YoA 2023, 2024 and 2025 cost scales and simplified rates were not reopened today: they stay in `travel-allowance-and-logbook-rate-tables-2023-to-2027`.

## Disclaimer

> **General reference only.** This file is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status or local procedures. Do not rely on it to file, pay, amend or take a tax position without review by a qualified professional in South Africa.

> Contributed by Brandon Iverach.
