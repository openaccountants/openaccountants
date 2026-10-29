---
jurisdiction: ZA
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-CORP: za-corporate-income-tax
  SC: za-payroll-paye-uif-sdl
  PR: za-payroll-paye-uif-sdl
  XB: leaving-south-africa-tax-emigration
partial:
  IT-IND: "za-income-tax carries tax_year 2025 and has not been re-verified for the 2027 year of assessment (1 March 2026 to 28 February 2027)"
  TP: "south-africa-transfer-pricing carries tax_year 2025 and has no Sources section with read dates"
  XB: "leaving-south-africa-tax-emigration carries tax_year 2025 and has not been re-verified for 2026/27"
---

# South Africa: tax pack

Individuals' tax year runs from 1 March to the end of February. SARS calls 1 March 2026 to 28 February 2027 the "2027" year of assessment. A company's year of assessment is its financial year. The authority is the South African Revenue Service (SARS), and returns and payments go through eFiling. The currency is the rand.

Residents are taxed on worldwide income, non-residents on South African-source income. Companies pay a flat 27%, with lower bands for qualifying small business corporations. Individuals pay 18% to 45%. Employers pay PAYE, UIF (1% + 1% up to R17 712 a month) and SDL (1%) monthly on the EMP201. South Africa has no general social security contribution beyond UIF and SDL.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | za-income-tax, income-tax-rate-tables-by-year-of-assessment-2023-to-2027, za-provisional-tax | sourced from the law |
| IT-CORP, corporate income tax | za-corporate-income-tax (YAs ending 1 April 2026 to 31 March 2027: 27% rate, SBC bands from R99 000 and qualifying tests, s12E allowances, s20 assessed loss cap of the higher of R1 million and 80%, provisional tax, underestimation and late penalties, ITR14, TAA fixed penalties, dividends tax, non-resident withholding) | checked against the law |
| VAT | za-vat-return, south-africa-vat, cancelling-a-vat-registration-and-the-exit-vat-charge | sourced from the law |
| SC, social contributions | za-payroll-paye-uif-sdl (UIF 1% + 1% up to R17 712 a month and its exclusions; SDL 1% with the R500 000 exemption) | checked against the law |
| PR, payroll withholding | za-payroll-paye-uif-sdl (2027 PAYE tables, rebates, thresholds, medical credits, annual-equivalent method, retirement fund deduction, EMP201, directors, penalties) checked against the law; za-emp501-reconciliation-and-irp5-corrections-syfile sourced from the law | checked against the law |
| TP, transfer pricing | south-africa-transfer-pricing | sourced from the law |
| XB, cross-border | leaving-south-africa-tax-emigration, za-tax-residency, za-foreign-employment-exemption | sourced from the law |

"Checked against the law" applies once the independent review is recorded on the pull request.

## Official sources

- SARS, Companies, Trusts and SBC rates: https://www.sars.gov.za/tax-rates/income-tax/companies-trusts-and-small-business-corporations-sbc/ (read 2026-10-29)
- SARS, Rates of Tax for Individuals: https://www.sars.gov.za/tax-rates/income-tax/rates-of-tax-for-individuals/ (read 2026-10-29)
- SARS, PAYE-GEN-01-G21 Guide for Employers iro Employees' Tax for 2027: https://www.sars.gov.za/wp-content/uploads/Ops/Guides/PAYE-GEN-01-G21-Guide-for-Employers-iro-Employees-Tax-for-2027-External-Guide.pdf (read 2026-10-29)
- SARS, Budget 2026 FAQs: https://www.sars.gov.za/about/sars-tax-and-customs-system/budget/budget-2026-frequently-asked-questions/ (read 2026-10-29)
- Income Tax Act 58 of 1962, Tax Administration Act 28 of 2011, Skills Development Levies Act 9 of 1999 and Unemployment Insurance Contributions Act 4 of 2002, SARS-provided consolidations: https://sars.mylexisnexis.co.za/ (linked from https://www.sars.gov.za/legal-counsel/primary-legislation/) (read 2026-10-29)
