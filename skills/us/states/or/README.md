---
jurisdiction: US-OR
covered_by:
  income-tax: or-income-tax
  corporate-tax: or-corporate-tax
  gross-receipts-tax: or-cat
  payroll: or-payroll
partial:
  income-tax: "Final 2026 return forms/tables/credits and complete conformity unavailable; final 2025-2026 filing-cycle rules and labeled 2026 estimates/planning supplied. Nonresident, reduced-rate and local calculations are boundaries."
  corporate-tax: "Ordinary rate/minimum computation and 2025-2026 filing-cycle map supplied; final 2026 forms/conformity, complete losses, sourcing and special regimes remain unconfirmed."
  gross-receipts-tax: "Core CAT computation, thresholds and reporting supplied; statutory/DOR nexus and registration-equality conflicts explicit; final 2026 forms and special exclusion amendment audit incomplete."
  payroll: "2026 core withholding/UI/STT/transit/leave/WBF and reporting supplied; multistate localization, special coverage, successors, exact withholding tie, full penalties and upload specifications remain boundaries."
---

# Oregon tax skills, 2026

Oregon has individual income tax, corporate excise/income tax, CAT and employer payroll obligations. Each job has one owner, preserving existing slugs. There is no general sales or use/transaction tax, so no general sales-tax skill is created; vehicle and other specific taxes require separate analysis. [DOR sales-tax statement](https://www.oregon.gov/dor/programs/businesses/pages/sales-tax.aspx), read 2026-11-13.

| Job | Owner | Coverage |
|---|---|---|
| Individual income | `or-income-tax` | Federal AGI bridge, Oregon deductions/credits, final 2025-2026 filing-cycle table/chart, current 2026 estimate rules and labeled planning figures. |
| Corporate excise/income | `or-corporate-tax` | Separate tax from CAT; ordinary C-corp rate/minimum, group gate, estimates and return workflow. |
| Corporate Activity Tax | `or-cat` | Applies beyond corporations; separate registration/filing/payment decisions, source/exclusion and labor/COGS subtraction. |
| Payroll | `or-payroll` | Actual 2026 withholding/UI/STT, employer TriMet/LTD, Paid Leave/WBF and combined reporting. |
| General sales/use | None | No general state tax. Specific vehicle taxes and other states' collection obligations are not absent merely because Oregon has no general tax. |

All skills have `tax_year: 2026`. That metadata does not turn 2025 return boxes into final 2026 figures. Each skill identifies its actual periods, official sources/read dates and unresolved matters. The early 2026 estimate publication and later payroll publication disagree on some indexed amounts; the individual skill identifies later published deductions while keeping provisional estimates and payroll constants distinct.

CAT and corporate income tax are different jobs; their groups, nexus, receipts, tax bases, filing dates and estimates must not be interchanged. Existing CAT examples and all four former payroll employee scenarios are retained with corrected 2026 arithmetic. Local Portland/Multnomah/Metro income/business taxes, district self-employment taxes, estate taxes and special entity regimes are separate referrals, not claims that those taxes do not exist.

Federal return, payroll and business computations are loaded by the actual slugs named in each skill. No accountant review is claimed. No duplicate skill is retired in this Oregon pack.
