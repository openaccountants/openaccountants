---
jurisdiction: US-MI
applicable: [IT-IND, IT-CORP, VAT, SC, PR]
not_applicable:
  TP: no Michigan transfer pricing documentation regime; related-party rules sit in the corporate skill and the federal skills
  XB: reciprocity states and residency are in mi-income-tax; part-year and nonresident returns are out of scope
covered_by:
  IT-IND: mi-income-tax
  IT-CORP: mi-corporate-income-tax
  VAT: mi-sales-tax
  SC: mi-payroll
  PR: mi-payroll
partial:
  IT-IND: "2026 MI-1040, Schedule 1, Form 4884 and MI-1040CR not yet published, so 2025 line numbers are used; homestead credit limits and some special exemptions are 2025-2026 filing cycle figures; Detroit uses the 2025 forms; part-year and nonresident returns not covered"
  IT-CORP: "2026 Small Business Alternative Credit income limit (Form 4893) not yet published; Flow-Through Entity Tax figures and services sourcing not confirmed"
  VAT: "remote seller threshold, item-by-item taxability, filing frequency thresholds and penalty rates not confirmed"
  SC: "unemployment insurance report due dates, late penalties and registration thresholds on MiUI not confirmed"
  PR: "SUW filing frequency thresholds and late penalty and interest rates not confirmed"
---

# Michigan (US-MI): tax pack

Calendar tax year for individuals. Authority: the Michigan Department of Treasury (michigan.gov/treasury and michigan.gov/taxes), which also administers the City of Detroit income tax. Currency: US dollars. Michigan taxes individuals at a flat 4.25% for 2026 (Treasury notice of 15 April 2026; MCL 206.51), after a $5,900 personal exemption per person (2026 Withholding Guide). From 2026 every retiree may subtract retirement benefits up to $67,610 single or $135,220 joint (Public Act 4 of 2023, fully phased in). 2025 PA 24 decoupled Michigan from the federal 2025 changes to bonus depreciation, section 179, research expensing and the business interest limit, and added Michigan deductions for federally claimed qualified tips and overtime for 2026 to 2028. C corporations pay the corporate income tax at 6% of apportioned business income (MCL 206.623, see `mi-corporate-income-tax`), and retail sales of tangible personal property bear the 6% sales tax (see `mi-sales-tax`). Michigan has reciprocity with Illinois, Indiana, Kentucky, Minnesota, Ohio and Wisconsin. A US state: federal income tax, FICA and FUTA sit on top of every domain here.

**City income taxes.** Michigan cities may levy an income tax under the City Income Tax Act. Detroit (2.4% resident, 1.2% nonresident, $600 exemption) is covered by `mi-detroit-individual-return`; other cities are out of scope.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | mi-income-tax | checked against the law (partial) |
| IT-IND, retirement and pension subtraction | mi-pension-retirement-subtraction | checked against the law |
| IT-IND, homestead property tax credit | mi-homestead-credit | checked against the law (2025 limits) |
| IT-IND, estimated tax | mi-estimated-tax | checked against the law |
| IT-IND, City of Detroit individual return | mi-detroit-individual-return | checked against the law (2025 forms) |
| IT-IND, return assembly (router) | mi-return-assembly | checked against the law |
| IT-CORP, corporate income tax | mi-corporate-income-tax | checked against the law (partial) |
| VAT / sales and use tax | mi-sales-tax | checked against the law (partial) |
| SC, unemployment insurance | mi-payroll | checked against the law (partial) |
| PR, payroll withholding | mi-payroll | checked against the law (partial) |
| TP, transfer pricing | not applicable, see above | |
| XB, cross-border | not applicable as a separate skill, see above | |

Out of scope for this pack: part-year and nonresident returns (Schedule NR); city income taxes other than Detroit; the home heating credit (MI-1040CR-7) and the veterans and blind credit (MI-1040CR-2); property tax and the principal residence exemption (local assessors); estates and trusts (MI-1041). Michigan has no estate tax. The Michigan Business Tax was replaced by the corporate income tax.

## Official sources

- Treasury notice, 4.25% rate for 2026: https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year (read 2026-11-13)
- 2026 Michigan Income Tax Withholding Guide (Form 446): https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf (read 2026-11-13)
- Treasury notice, decoupling from certain IRC provisions: https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/02/25/decoupling-michigan-income-taxes-from-certain-internal-revenue-code-provisions (read 2026-11-13)
- Revenue Administrative Bulletin 2026-1 (retirement income): https://www.michigan.gov/taxes/rep-legal/rab/2026-revenue-administrative-bulletins/revenue-administrative-bulletin-2026-1 (read 2026-11-13)
- 2026 MI-1040ES: https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/IIT/TY2025/MI-1040ES-(2026).pdf (read 2026-11-13)
- 2025 Homestead Property Tax Credit Information: https://www.michigan.gov/taxes/iit/tax-guidance/credits-exemptions/hptc/tax-year-credit-information/2025 (read 2026-11-13)
- City of Detroit Income Tax Information: https://detroitmi.gov/departments/office-chief-financial-officer/ocfo-divisions/office-treasury/income-tax/income-tax-information (read 2026-11-13)
