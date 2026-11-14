---
jurisdiction: US-NJ
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  IT-IND: nj-income-tax
  IT-CORP: nj-cbt-and-bait
  VAT: nj-sales-tax
  SC: nj-payroll
  PR: nj-payroll
  TP: nj-cbt-and-bait
  XB: nj-income-tax
partial:
  IT-IND: "2026 rates and exemptions verified from the 2026 NJ-1040-ES; 2026 NJ-1040 instructions, line numbers, Child Tax Credit and NJEITC amounts not yet published, so 2025-2026 filing-cycle figures are labelled"
  IT-CORP: "2026 CBT-150 and 2026 PTE-100 verified; 2026 CBT-100 instructions not yet published, so the 2025 set is used; banks, insurers, utilities, REITs and special regimes referred"
  VAT: "Salem County reduced rate and the current TB-72 revision on SaaS not confirmed; hotel, vehicle and excise taxes out of scope"
  TP: "No transfer pricing documentation regime; combined reporting and related-party points sit in nj-cbt-and-bait and are referred beyond the basics"
  XB: "Residency, nonresident returns and the other-state credit are in nj-income-tax; complex multi-state and convenience-rule cases are referred"
---

# New Jersey (US-NJ): tax skills, 2026

**Built from the law. Not yet approved. Written by Claude. Not reviewed by an accountant.** New Jersey has an individual gross income tax, a Corporation Business Tax with a Corporate Transit Fee, an elective pass-through entity tax (BAIT), a 6.625% State Sales and Use Tax with no local sales taxes, and employer payroll withholding with unemployment, disability and family leave contributions. The Division of Taxation administers the revenue taxes; the Department of Labor and Workforce Development (NJDOL) administers the contributions. Currency is US dollars.

| Job | Sole skill owner | What it covers |
| --- | --- | --- |
| Individual income, including sole proprietors, residents and nonresidents | `nj-income-tax` | NJ-1040 and NJ-1040NR, income categories, NJ-BUS-1, retirement exclusions, property tax deduction or credit, 2026 rate tables, NJ-COJ, credits, estimates |
| Corporate income and pass-through entity tax | `nj-cbt-and-bait` | CBT rates and minimum tax, Corporate Transit Fee, combined reporting, NOLs, CBT-150; BAIT election, brackets and the owner's credit |
| Sales and use | `nj-sales-tax` | Rate, UEZ and Salem County, taxability including SaaS, remote sellers, ST-50, certificates, Use Tax |
| Payroll withholding and employer contributions | `nj-payroll` | NJ-W4, NJ-WT, NJ-500, NJ-927, WR-30, NJ-W-3, 2026 UI, WF/SWF, TDI and FLI rates and wage bases, minimum wage |

`new-jersey-sales-tax` was a second sales tax skill for the same job. Its content was folded into `nj-sales-tax` and the file was retired in November 2026.

Not covered by this pack: local property tax, inheritance tax (New Jersey still taxes transfers to some heirs; its estate tax was repealed from 2018), realty transfer fees, hotel occupancy fees and the Newark hotel surcharge, motor vehicle, alcohol, cigarette, hemp and cannabis excise taxes, and insurance premium tax.

Federal computations are owned by the federal skills named in each file, such as `us-sales-tax`, `us-multi-state-residency-and-allocation` and `us-pte-state-matrix`. Do not restate federal figures here.
