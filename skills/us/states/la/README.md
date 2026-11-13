---
applicable: [IT-IND, IT-CORP, VAT, PR, SC]
covered_by:
  IT-IND: la-income-tax
  IT-CORP: la-corporate-tax
  VAT: la-sales-tax
  PR: la-payroll
  SC: la-payroll
partial:
  IT-IND: final 2026forms, complex conformity/credits and nonresident computation
  IT-CORP: final 2026forms, NOLs, elections and special industry factors
  VAT: actual local rates/bases and special transactions
  PR: exact assigned deposit days and special wages
  SC: UI liability exceptions/localization and assigned rate
---

# Louisiana state skills, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

Louisiana imposes individual and corporate income tax and state/local sales/use tax. Franchise tax is repealed for periods beginning 2026; this does not remove corporate income tax or older franchise liabilities. Payroll withholding and UI remain separate employer jobs. [Individual rate law](https://www.legis.la.gov/legis/Law.aspx?d=101946); [LDR corporate/repeal page](https://revenue.louisiana.gov/businesses/widely-used-tax-types/corporate-income-franchise-tax); [LDR sales/use page](https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax); [LWC 2026 UI table](https://www.laworks.net/Downloads/UI/WTS/2026RateTable.pdf).

## Domain map

| Core state job | Status and boundary | covered_by |
| --- | --- | --- |
| Individual wage/sole-proprietor income | Covered for ordinary full-year residents; final 2026 form lines, complex conformity/credits and nonresident work are partial | `la-income-tax` |
| Sales and use | Covered for ordinary state computation; actual local rate/base and special transactions require location research | `la-sales-tax` |
| Corporate/franchise | Covered for ordinary C-corporation computation and 2026 franchise repeal; entity elections/NOL/special apportionment are partial | `la-corporate-tax` |
| Employer withholding and SUI | Covered for ordinary formula, annual wage cap and assigned-rate reporting; coverage exceptions and exact deposit-day assignment are partial | `la-payroll` |

## Files

| File | Purpose |
| --- | --- |
| [la-income-tax.md](la-income-tax.md) | 3% income tax, final indexed deductions, exempt income, resident computation and estimates |
| [la-sales-tax.md](la-sales-tax.md) | 5% state rate, software access, sourcing, exemptions and state/local obligations |
| [la-corporate-tax.md](la-corporate-tax.md) | 5.5% ordinary corporation tax, $20,000 subtraction, franchise repeal and estimates |
| [la-payroll.md](la-payroll.md) | L-4 withholding formula, deposits/reconciliation and unemployment reporting |

Load the applicable federal owner skills alongside these state skills. Each core job has exactly one owner above. Existing income and sales slugs remain; no file is retired or renamed. New corporate/payroll slugs were checked against the full tracked skill tree.

## Source-year and approval boundaries

Built from the law. Not yet approved. A 2026 metadata tag is not evidence that every filing form is final. Final indexed 2026 personal return deductions are published in [RIB26-019](https://dam.ldr.la.gov/lawspolicies/RIB%2026-019.pdf); they differ from 2026 payroll deductions. The opened IT-540 and corporate income-form details retained from the **2025-2026 filing cycle** are explicitly labelled in their owning skills and cannot be silently used as final 2026 line numbers. Sources were read on 2026-11-13, with scope and unresolved items in each skill.

Not yet confirmed: final 2026 income/corporate return line maps, later-federal-law conformity, special credit/NOL/election computations, actual local sales rate/base and precise assigned payroll deposit days. The pack is partial on those facts. Franchise is not applicable only to periods beginning 2026+, as the official LDR repeal notice explains; there is no broad no-business-tax assertion.

## Outside this pack

Property tax, parish business/occupational taxes, partnership return preparation, severance/excise taxes and complex amended/controversy matters remain outside the four core jobs. Part-year/nonresident income and S/composite/PTE filings are identified boundaries, not omitted jobs claimed complete. Prior CIFT-620 and old reform figures remain historical topics in the owning skill's dated notes or unresolved list.
