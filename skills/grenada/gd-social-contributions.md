---
name: gd-social-contributions
description: >
  Grenada National Insurance Scheme (NIS) contributions for 2026. Covers the 13.5%
  combined rate for 2026 under the reform timetable (rising 0.25% a side each year to
  16% in 2031), the 2024 employer and employee split (the 2026 split is not yet confirmed), the EC$5,200 monthly and EC$1,200
  weekly insurable earnings ceilings, insurable earnings, payment at month end with the
  14-day grace, the 10% surcharge and 1% a month interest, and the self-employed rules
  (13.5%, 1% employment injury over 65, EC$907 to EC$8,424 a year). Trigger phrases
  include Grenada NIS, Grenada national insurance, NIS contributions Grenada.
version: 1.0
jurisdiction: GD
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Grenada National Insurance contributions 2026

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

National Insurance Scheme (NIS) contributions in Grenada for 2026, as published by NIS Grenada. Covers employees and employers, the self-employed and voluntary contributors, the ceilings, insurable earnings and remittance. Amounts are EC$. The NIS contributors page did not load today; its January 2025 web.archive.org copy is used for the earnings list, the weekly ceiling and the 2024 split. Annual stamp tax and VAT: [gd-annual-stamp-tax](gd-annual-stamp-tax.md), [gd-vat-registration](gd-vat-registration.md).

## Ask the client first

1. Employee, self-employed or voluntary contributor? Age (pensionable age rules are changing; employment injury only over 65 for the self-employed)?
2. Monthly or weekly pay, and every earnings component.
3. Employer and employee registration numbers.
4. For the self-employed: gross earnings, and whether they pay monthly or as an annual lump sum.
5. Is the employee also self-employed elsewhere?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Combined rate, 2026 | 13.5% (13% in 2025; 14% scheduled for 2027) | [NIS 2023 adjustments](https://nisgrenada.org/2023-adjustments/) |
| Yearly increase | 0.25% employer and 0.25% employee each year from 2024 to 2031 (16% in 2031) | same |
| 2024 split (12.5%) | Employer 6.75%, employee 5.75% | [NIS contributors page, archived 23 January 2025](https://web.archive.org/web/20250123161437/https://www.nisgrenada.org/contributors/) |
| Ceiling, monthly | EC$5,200 | [NIS home page](https://nisgrenada.org/) |
| Ceiling, weekly | EC$1,200 | [NIS contributors page, archived 23 January 2025](https://web.archive.org/web/20250123161437/https://www.nisgrenada.org/contributors/) |
| Payment | Due at the end of each month; grace of up to 14 days with penalty and interest | same |
| Late payment | 10% surcharge plus 1% interest for each month or part month outstanding | same |
| Self-employed rate | 13.5% of gross earnings, earnings up to EC$5,200 a month | [NIS home page](https://nisgrenada.org/) |
| Self-employed over 65 | 1% of gross earnings, for employment injury benefit | same |
| Self-employed payments from 1 July 2023 | Monthly or an annual lump sum; any amount from EC$907 to EC$8,424 a year qualifies for all benefits; no penalties or interest for late payment | same |
| Voluntary contributors | Ages 16 to pensionable age (stated as currently 63) | same |

### Steps

1. **Register** each employee (birth certificate, picture ID, supporting documents).
2. **Insurable earnings:** all earnings including overtime, cost of living bonus, dependant payments, long service supplements, commission, employer-paid gratuities, night or shift pay, service charges, liabilities paid by the employer, holiday pay and danger money.
3. **Cap** at EC$5,200 a month or EC$1,200 a week; use the weekly rule for weekly pay, not four weeks a month.
4. **Contributions:** 13.5% combined of capped earnings for 2026 ([NIS 2023 adjustments](https://nisgrenada.org/2023-adjustments/)). How the 13.5% splits between employer and employee in 2026 is not on a current NIS page read: confirm it with NIS before deducting the employee share (see Not yet confirmed).
5. **Remit** through the NIS web portal (my.nisgrenada.org) by month end, listing each employee's earnings (weekly amounts for weekly workers) and contributions.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Archived contributors page shows 6.75% and 5.75% (12.5%) | 2024 split only; the 2026 split is not yet confirmed (see Not yet confirmed) | [NIS contributors page, archived 23 January 2025](https://web.archive.org/web/20250123161437/https://www.nisgrenada.org/contributors/) |
| Paid within the 14-day grace | Penalty and interest still apply; pay by month end | [NIS contributors, archived](https://web.archive.org/web/20250123161437/https://www.nisgrenada.org/contributors/) |
| Self-employed person also employed elsewhere | May still make self-employed payments, up to EC$8,424 a year in total | [NIS home page](https://nisgrenada.org/) |
| Self-employed in 2026 wanting benefits in 2027 | Must contribute in 2026 | same |
| Pensionable age | Rising from 60 to 65 over 2024 to 2029; pension still payable from 60 with a reduction | [NIS 2023 adjustments](https://nisgrenada.org/2023-adjustments/) |

## Worked cases

### Case 1: employee at and above the ceiling

At EC$4,000 a month the combined 13.5% is 540. At EC$6,000 the base is capped at 5,200 and the combined contribution is 702. The split between employee and employer waits for the 2026 split (see Not yet confirmed).

```oa-check
name: Grenada NIS 2026 combined, 4,000 and 6,000 a month
inputs:
  pay_low: 4000
  pay_high: 6000
  ceiling: 5200
steps:
  - low_total: min(pay_low, ceiling) * 0.135
  - high_base: min(pay_high, ceiling)
  - high_total: high_base * 0.135
expected:
  low_total: 540
  high_base: 5200
  high_total: 702
```

### Case 2 (decision): self-employed, pay the full amount or the minimum?

A self-employed person earns EC$6,000 a month. Contributions on the ceiling are 5,200 x 12 x 13.5% = 8,424 a year, the top of the published range. The minimum that qualifies for all benefits is 907, which is 13.5% of about 6,719 of annual earnings. Paying the minimum keeps benefit eligibility but benefits are earnings-related, so the lower payment buys lower benefits. Decide on the cover wanted, and pay in 2026 to qualify in 2027.

```oa-check
name: Grenada NIS self-employed, ceiling against minimum
inputs:
  ceiling: 5200
  minimum: 907
steps:
  - full_year: ceiling * 12 * 0.135
  - gap: full_year - minimum
  - minimum_earnings: round(minimum / 0.135, 0)
expected:
  full_year: 8424
  gap: 7517
  minimum_earnings: 6719
```

## When to refuse or refer

- Benefit amounts and claims, special contribution classes and the pensionable age for each birth year.
- Multiple employers: not set out on the NIS pages read.
- Self-employed earnings below the minimum or partial years: ask NIS.

## Filing and payment

1. Register the employer and employees with NIS.
2. Submit the monthly remittance on my.nisgrenada.org with employer and employee names and numbers, earnings (by week for weekly workers) and contributions; pay by month end ([NIS contributors, archived](https://web.archive.org/web/20250123161437/https://www.nisgrenada.org/contributors/)).
3. Self-employed: pay monthly or as a lump sum within the year.
4. Keep the classification, earnings schedule and receipts.

## Completion checklist

- All earnings components in; ceiling applied by pay period.
- 13.5% combined applied for 2026; the employee and employer shares confirmed with NIS.
- Remitted by month end.

## Sources

| Source | URL | Read on |
|---|---|---|
| NIS 2023 adjustments page: read for the contribution rate table (13% 2025, 13.5% 2026, 14% 2027, 0.25% a side each year) and the pensionable age change | https://nisgrenada.org/2023-adjustments/ | 2026-11-14 |
| NIS home page: read for the self-employed 13.5% rate, the 1% over 65, the EC$5,200 monthly maximum, the 1 July 2023 rules (EC$907 to EC$8,424), the voluntary contributor ages and the online portal | https://nisgrenada.org/ | 2026-11-14 |
| NIS contributors page (web.archive.org copy of 23 January 2025; the live page did not load): read for the 2024 split (6.75% employer, 5.75% employee), the EC$5,200 and EC$1,200 maxima, insurable earnings, the month-end due date, the 14-day grace, the 10% surcharge and 1% interest | https://web.archive.org/web/20250123161437/https://www.nisgrenada.org/contributors/ | 2026-11-14 |

Not yet confirmed: the 2026 employer and employee split (no current NIS page read shows it; the archived 2024 split of 6.75% employer and 5.75% employee plus the published 0.25% a side yearly steps would give 7.25% and 6.25%, but that is a derivation from a 2024 archive, not a published 2026 figure); the weekly ceiling for 2026 (only the January 2025 copy shows it); the National Insurance Act and regulations (not opened); rules for multiple employers.
