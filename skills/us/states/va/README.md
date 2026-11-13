---
jurisdiction: US-VA
applicable: [IT-IND, IT-CORP, VAT, SC, PR, XB]
not_applicable:
  TP: "no separate Virginia transfer pricing regime; intercompany addbacks and filing methods sit in the corporate skill"
covered_by:
  IT-CORP: va-corporate-tax-and-bpol
  VAT: va-sales-tax
  SC: va-payroll
  PR: va-payroll
  XB: va-income-tax
partial:
  XB: "residents only; part-year residents (Form 760PY) and nonresidents (Form 763) are referred out"
---

# Virginia (US-VA): tax pack

Calendar tax year for individuals; corporations follow their federal year. Authorities: the Virginia Department of Taxation (Virginia Tax, tax.virginia.gov) for income, corporate, sales and withholding taxes; the Virginia Employment Commission (VEC) for unemployment insurance; each county, city and town for the BPOL license tax. Currency: US dollars. Virginia taxes individuals at 2% to 5.75% (5.75% above $17,000, Va. Code § 58.1-320), corporations at 6% (§ 58.1-400), offers a 5.75% elective pass-through entity tax (§ 58.1-390.3), and charges retail sales tax of 5.3%, 6%, 6.3% or 7% depending on the locality, with 1% on food for home consumption. There is no state franchise or gross receipts tax; the local BPOL tax is a gross receipts license tax. Virginia (US-VA) is not the US Virgin Islands, which have their own pack in `skills/us-virgin-islands`. A US state: federal income tax, FICA and FUTA sit on top of every domain here.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | va-income-tax | checked against the law |
| IT-CORP, corporate income tax, PTET and local BPOL | va-corporate-tax-and-bpol | checked against the law |
| VAT / sales and use tax | va-sales-tax | checked against the law |
| SC, social contributions (unemployment insurance, VEC) | va-payroll | checked against the law |
| PR, payroll withholding | va-payroll | checked against the law |
| TP, transfer pricing | not applicable, see above | |
| XB, cross-border (residency, reciprocity, other-state credit) | va-income-tax | checked against the law (partial) |

Out of scope for this pack: real estate, personal property and machinery and tools taxes (local); the bank franchise tax; insurance premiums and public service taxes; motor vehicle, aircraft, watercraft and communications taxes; local meals and lodging taxes; each locality's BPOL rates (set by ordinance); estate tax (Virginia has none).

## Official sources

- Va. Code § 58.1-320 (individual rates): https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-320/ (read 2026-11-13)
- Va. Code § 58.1-400 (corporate rate): https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-400/ (read 2026-11-13)
- Va. Code § 58.1-3706 (BPOL rate caps): https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3706/ (read 2026-11-13)
- Virginia Tax, Retail Sales and Use Tax: https://www.tax.virginia.gov/retail-sales-and-use-tax (read 2026-11-13)
- Virginia Tax, Withholding Tax: https://www.tax.virginia.gov/withholding-tax (read 2026-11-13)
- 2025 Form 500 instructions: https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf (read 2026-11-13)
- 2026 Form 760ES: https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2026/760es-2026.pdf (read 2026-11-13)
- VEC, How are tax rates assigned?: https://www.vec.virginia.gov/FAQs/employers/how-are-tax-rates-assigned (read 2026-11-13)
