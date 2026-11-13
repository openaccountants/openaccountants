---
applicable: [IT-IND, IT-CORP, VAT, PR, SC]
covered_by:
  IT-IND: me-income-tax
  IT-CORP: me-corporate-tax
  VAT: me-sales-tax
  PR: me-payroll
  SC: me-payroll
partial:
  IT-IND: final 2026 forms, pension phaseout, credits and nonresident work
  IT-CORP: final 2026 forms, extension conflict, group/factor and financial-institution bases
  VAT: local-levy absence, special sourcing and transaction definitions
  PR: special wages, exemptions and employer-specific submission schedules
  SC: assigned rate, special coverage and electronic submission assignment
---

# Maine state skills, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

Maine has individual and corporate income tax, state sales/use tax and employer withholding/UI. Financial institutions have a separate franchise tax; the old blanket no-franchise statement was wrong. [individual law](https://legislature.maine.gov/statutes/36/title36sec5111.html); [corporate law](https://legislature.maine.gov/statutes/36/title36sec5200.html); [sales law](https://legislature.maine.gov/statutes/36/title36sec1811.html); [financial-institution franchise law](https://legislature.maine.gov/statutes/36/title36sec5206.html).

## Domain map

| Core job | Coverage boundary | covered_by |
| --- | --- | --- |
| Individual wages/sole proprietor | Resident computation; final forms, pension phaseout, credits and nonresidents partial | `me-income-tax` |
| Sales/use | Ordinary classifications/rates and use tax; special sourcing/local-levy absence partial | `me-sales-tax` |
| Corporate/franchise | Ordinary corporate bands and tax-before-factor; financial-institution routing only, bases partial | `me-corporate-tax` |
| Employer withholding/SUI | Ordinary 2026 withholding and UI cap/components; assigned rates and special coverage partial | `me-payroll` |

## Files and use

Use [me-income-tax.md](me-income-tax.md), [me-sales-tax.md](me-sales-tax.md), [me-corporate-tax.md](me-corporate-tax.md) and [me-payroll.md](me-payroll.md) with their named federal owners. Exactly one skill owns each core job. Both existing slugs/licence metadata remain. No file was retired.

## Source-year and approval boundaries

Built from the law. Not yet approved. Sources were opened/read on 2026-11-13. The revised 2026 income schedule, phaseout/estimate worksheets, August payroll instructions and 2026 UI array provide current figures. The corporate procedural booklet and franchise form overview explicitly concern the **2025-2026 filing cycle**; they do not establish final 2026 form lines. Current statutory rate and apportionment rules are separately sourced.

Not yet confirmed: final 2026 individual/corporate return instructions and 2027 filing calendar; indexed pension phaseout and detailed credits; conflicting corporate extension descriptions; specialized group/NOL/factor and franchise income/assets bases; local sales-levy absence and special sourcing; employer-specific UI/submission and special wage facts. The 2026 tag does not mean these gaps are complete.

## Outside this pack

Estate/trust, insurance premiums, municipal property tax, PTE elections, complex amended/controversy work, paid-leave and other payroll programs are outside the four computations. Nonresident/part-year and multistate allocation are identified boundaries. The prior SST/nonlocal-tax assertions are not reverified; do not use them as current law.
