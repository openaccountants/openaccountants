---
jurisdiction: US-IA
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  IT-IND: ia-income-tax
  IT-CORP: ia-corporate-tax
  VAT: ia-sales-tax
  SC: ia-payroll
  PR: ia-payroll
partial:
  IT-IND: "Final 2026 form mappings and school/EMS surtax table still require confirmation."
  IT-CORP: "Ordinary C-corporation computation covered; financial-institution franchise rate/scope only, full bank base and return workflow missing."
  PR: "Regular withholding and UI covered; detailed formula low-wage/rounding and special payroll regimes need confirmation."
  TP: "No separate Iowa transfer-pricing skill."
  XB: "Basic sourcing boundaries only; no dedicated cross-border skill."
---

# Iowa: 2026 state tax skills

Iowa has individual income tax on wages and business income, ordinary corporate income tax, financial-institution franchise tax, sales/use tax, employee income-tax withholding and employer unemployment insurance. Federal taxes remain separate. There is no broad state gross-receipts tax described by this pack. The former README incorrectly marked franchise tax absent: financial institutions are taxed under Iowa Code 422.60 and 422.63.

| Job | covered_by | Coverage and state |
| --- | --- | --- |
| Individual income tax | `ia-income-tax` | 2026 rate/base and core decisions; final form/surtax gap above |
| Sales and use tax | `ia-sales-tax` | State tax, local option sales tax, purchaser use tax and common exemptions |
| Corporate/franchise | `ia-corporate-tax` | Ordinary corporations plus franchise scope/rate; detailed bank computation partial |
| Payroll withholding and UI | `ia-payroll` | Regular withholding, UI base/rates, registration and reporting; special-case gaps above |

All four skills are **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. Reference mappings from read 2025 instructions are explicitly labelled the 2025-2026 filing cycle and must not be presented as final 2026 forms.

Separate specialist work remains for pass-through/PTET returns, detailed farm/employee-owner capital-gain elections, special corporate credits, property/homestead relief, inheritance administration and complex multistate allocations. Each skill ends with its precise unconfirmed items. No person's professional approval is claimed.

Official sources read 2026-11-13: [Iowa Department of Revenue](https://revenue.iowa.gov/), [Iowa Code chapter 422](https://www.legis.iowa.gov/docs/code/2026/422.5.pdf), [Iowa sales tax law](https://www.legis.iowa.gov/docs/code/2026/423.3.pdf) and [Iowa Workforce Development](https://workforce.iowa.gov/employers/unemployment-insurance/ui-tax-and-audit/unemployment-insurance-taxes). The skills record sections and read purposes for each individual source.
