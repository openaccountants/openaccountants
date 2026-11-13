---
jurisdiction: US-MA
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: ma-income-tax
  IT-CORP: ma-corporate-excise
  VAT: ma-sales-tax
  SC: us-ma-payroll
  PR: us-ma-payroll
partial:
  IT-IND: "Resident Form 1 only; nonresident and part-year Form 1-NR/PY and 2026 Form 1 line numbers not yet covered"
  IT-CORP: "Combined reporting ownership and election terms, 2026 corporate estimate percentages and financial institution excise detail not yet confirmed"
  PR: "DOR withholding return frequencies and due dates not yet confirmed"
  TP: "No Massachusetts transfer pricing skill; combined reporting is outlined in ma-corporate-excise only"
  XB: "No Massachusetts cross-border skill; nonresident and composite filing points sit in ma-income-tax and ma-corporate-excise"
---

# Massachusetts (US-MA): tax pack

Calendar tax year for individuals; corporations follow their federal year. Authority: the Massachusetts Department of Revenue (DOR), mass.gov/dor, with the Department of Unemployment Assistance (DUA) for unemployment insurance and EMAC, and the Department of Family and Medical Leave (DFML) for paid leave. Currency: US dollars. A US state: federal income tax, FICA and FUTA sit on top of every domain here.

Massachusetts taxes individuals at 5% (8.5% on short-term gains, 12% on long-term collectible gains) plus a 4% surtax on taxable income over $1,107,750 for 2026; corporations pay an excise of 8% of apportioned net income plus $2.60 per $1,000 of property or net worth, minimum $456; sales and use tax is 6.25% with no local tax on goods (local option on restaurant meals only). There is no local income tax and no separate gross receipts tax; the S corporation income measure (2% or 3% above $6 million of receipts) and the elective PTE excises (5% under chapter 63D, 4% under chapter 63E from 2026) are part of the corporate excise skill.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax and the 4% surtax | ma-income-tax | sourced from the law (partial) |
| IT-CORP, corporate excise and PTE excise | ma-corporate-excise | sourced from the law (partial) |
| VAT, sales and use tax | ma-sales-tax | sourced from the law |
| SC, unemployment insurance, EMAC and PFML | us-ma-payroll | sourced from the law |
| PR, state income tax withholding | us-ma-payroll | sourced from the law (partial) |

The payroll slug carries the `us-` prefix because `ma-payroll` is the Morocco payroll skill.

Out of scope for this pack: estate tax (Form M-706), room occupancy excise and short-term rental fees, cannabis excise, deeds excise, local property tax, trusts and estates (Form 2), partnership return detail (Form 3), amended returns.

All skills are **Built from the law. Not yet approved.** No accountant has reviewed them.

## Official sources

- DOR Tax Rates: https://www.mass.gov/info-details/massachusetts-tax-rates (read 2026-11-13)
- DOR 4% Surtax: https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000 (read 2026-11-13)
- DOR Guide to Sales and Use Tax: https://www.mass.gov/guides/sales-and-use-tax (read 2026-11-13)
- DOR Corporate Excise Tax Guide: https://www.mass.gov/info-details/corporate-excise-tax-guide (read 2026-11-13)
- DOR Elective Pass-through Entity Excise: https://www.mass.gov/info-details/elective-pass-through-entity-excise (read 2026-11-13)
- DOR Circular M 2026: https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download (read 2026-11-13)
- DUA Employer contributions: https://www.mass.gov/info-details/employer-contributions-to-unemployment (read 2026-11-13)
- DFML PFML contribution rates: https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator (read 2026-11-13)
