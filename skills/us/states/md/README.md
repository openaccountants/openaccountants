---
jurisdiction: US-MD
applicable: [IT-IND, IT-CORP, VAT, SC, PR, XB]
not_applicable:
  TP: "No separate state transfer-pricing documentation pack; related-party state adjustments belong in the corporate skill."
covered_by:
  IT-IND: md-income-tax
  IT-CORP: md-corporate-tax
  VAT: md-sales-tax
  SC: md-payroll
  PR: md-payroll
  XB: md-income-tax
partial:
  IT-IND: "Full-year residents and published 2026 estimates; final indexed annual deduction/pension amounts and final 2026 forms pending."
  IT-CORP: "Ordinary Form500 and 2026 estimates; full Form510/511 PTE, special-industry apportionment and digital-advertising computations pending."
  VAT: "Core sales/use and dated technology changes; specialized product regimes and exact late-charge schedules pending."
  SC: "UI coverage, base, notices, 2026 administrative fee and quarterly filing; employer-specific starter/construction rate and Work Sharing pending."
  PR: "Withholding method, certificates and returns covered; detailed leave/remedies, new-hire penalties, FAMLI and final wage-file details pending."
  XB: "Resident credits and reciprocity routing; full nonresident/part-year, military and split-jurisdiction returns pending."
---

# Maryland: 2026 state tax pack

Maryland imposes individual state and county income taxes, corporation income tax, sales/use tax, employer withholding and unemployment insurance. The ordinary 6% sales rate has no local increment; specified products/services have different state rates. A separate Digital Advertising Gross Revenues Tax also exists and is outside this pack's computations. Currency: USD. Annual instructions not yet published for 2026 are labelled 2025-2026 filing cycle.

| Job | Skill | Status |
| --- | --- | --- |
| Individual income tax | `md-income-tax` | checked against the law; partial as above |
| Sales and use tax | `md-sales-tax` | checked against the law; partial as above |
| Corporation income tax | `md-corporate-tax` | checked against the law; partial as above |
| Withholding and UI | `md-payroll` | checked against the law; partial as above |

Official sources read 2026-11-13: [Comptroller publications](https://www.marylandcomptroller.gov/), [General Assembly statutes](https://mgaleg.maryland.gov/mgawebsite/Laws/Statutes), [DOL UI rates/reporting](https://www.labor.md.gov/unemployment-insurance/employer-agent/tax-rate.shtml). Each skill identifies its actual source and read scope. These are source-cited drafts awaiting independent review.

Other jobs outside the four-skill scope include SDAT annual reports/property tax, estate/inheritance tax, full PTE returns and amended/specialist returns. Federal computations remain in `skills/us/federal/`.
