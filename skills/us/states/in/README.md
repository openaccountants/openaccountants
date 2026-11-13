---
jurisdiction: US-IN
applicable: [IT-IND, IT-CORP, VAT, SC, PR, XB]
not_applicable:
  TP: "No standalone state transfer-pricing documentation job in this pack; related-party federal/state adjustments remain corporate work."
covered_by:
  IT-IND: in-income-tax
  IT-CORP: in-corporate-tax
  VAT: in-sales-tax
  SC: in-payroll
  PR: in-payroll
  XB: in-income-tax
partial:
  IT-IND: "2026 rate and selected enacted deductions; final annual forms, full modifications, credits, county computation and estimates remain unconfirmed."
  IT-CORP: "General AGI tax and estimate mechanics; complete apportionment, FIT base, group returns, PTET, credits and final 2026 forms remain unconfirmed."
  VAT: "General sales/use and selected product boundaries; full filing calendar, certificates, special taxes and classifications remain unconfirmed."
  SC: "Employer UI base, rate and filing mechanics; coverage exceptions, full penalties and appeal rules remain unconfirmed."
  PR: "State/county withholding and employer filing; annual WH-1 deadline conflict, full nonresident rules and employment-law topics remain unconfirmed."
  XB: "Selected reciprocity and residence boundaries; full allocation, other-state credits and international cases remain unconfirmed."
---

# Indiana: 2026 state tax skills

Indiana has separate individual, corporate, sales/use and employer payroll taxes. County income tax is distinct from state tax. The payroll notice read is effective October 1, 2026; final annual 2026 return packets were not confirmed. Existing annual catalogues remain labelled 2025, the 2025-2026 filing cycle, and their lines have not been relabelled 2026. Built from the law; Not yet approved.

## Domains

| Job | Skill | Status |
|---|---|---|
| Individual income tax | `in-income-tax` | checked against the law; partial as above |
| Corporate AGI tax; FIT boundary | `in-corporate-tax` | checked against the law; partial as above |
| Sales and use tax | `in-sales-tax` | checked against the law; partial as above |
| Payroll withholding and UI | `in-payroll` | checked against the law; partial as above |

Each job has one owner. Payroll covers both PR and employer SC; it is one combined workflow. Existing sales/payroll slugs stay. Federal 1040, Schedule C/SE, Form 1120, payroll and multistate nexus rules remain in their federal owner skills.

## Official sources

- [DOR tax library](https://www.in.gov/dor/resources/tax-library/information-bulletins/), [individual forms](https://www.in.gov/dor/tax-forms/individual/current/) and [corporate forms](https://www.in.gov/dor/tax-forms/corporate/current-corporatepartnership/), read November 13, 2026 for current bulletin versions and published form years.
- [Departmental Notice 1](https://www.in.gov/dor/files/dn01.pdf), read November 13, 2026 for the 2026 rate and October county withholding notice.
- [DWD employer manual](https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/), read November 13, 2026 for the linked UI rate, report and registration pages.
- Each skill records the particular source, reading scope and date. Annual form-host 403 failures and conflicting annual WH-1 dates are disclosed.

## Other existing topics

Pass-through IT-65/IT-20S, complete part-year/nonresident returns, property tax, historical inheritance-tax repeal, amended IT-40X returns and full county annual tables remain outside the completed scope. Their presence in the old README was not evidence of a researched rule. Employment-law topics from the old payroll file remain explicitly unconfirmed there. Load the applicable federal skills alongside this pack.
