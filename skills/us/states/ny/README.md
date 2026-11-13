---
jurisdiction: US-NY
applicable: [IT-IND, IT-CORP, VAT, SC, PR, XB]
not_applicable:
  TP: "no separate transfer pricing documentation regime; related-party rules sit in the Article 9-A corporate skill"
covered_by:
  IT-IND: ny-it-201-resident-return
  IT-CORP: ny-corporate-franchise-article-9a
  VAT: new-york-sales-tax
  SC: ny-payroll
  PR: ny-payroll
  XB: ny-residency-leaving-new-york
---

# New York (US-NY): tax pack

Calendar tax year for individuals. Authorities: the New York State Department of Taxation and Finance (tax.ny.gov) for state income tax, the New York City and Yonkers income taxes, the MCTMT and sales tax; the New York City Department of Finance (nyc.gov/finance) for the unincorporated business tax; the Department of Labor for unemployment insurance. Currency: US dollars. For 2026 the state income tax runs from 3.90% to 10.9% (the first five brackets were cut from 2026), New York City residents add 3.078% to 3.876%, Yonkers residents add a 16.75% surcharge, the self-employed in the twelve-county MCTD pay the MCTMT once a zone's earnings exceed $150,000, and New York City taxes unincorporated businesses at 4%. A US state: federal income tax, FICA and FUTA sit on top of every domain here.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax (full-year residents, Form IT-201) | ny-it-201-resident-return | checked against the law |
| IT-IND, estimated tax (Form IT-2105) | ny-estimated-tax | checked against the law |
| IT-IND, New York City unincorporated business tax | nyc-ubt | checked against the law |
| IT-IND, freelancer intake and return assembly (routers) | us-ny-freelance-intake, us-ny-return-assembly | checked against the law |
| IT-CORP, corporate franchise tax (Article 9-A) | ny-corporate-franchise-article-9a | sourced from the law |
| VAT / sales and use tax | new-york-sales-tax | sourced from the law |
| SC and PR, unemployment insurance and withholding | ny-payroll | sourced from the law |
| MCTMT (employers and the self-employed) | ny-mctmt | sourced from the law |
| Pass-through entity tax | ny-pte-tax-ptet | sourced from the law |
| LLC filing fee (Form IT-204-LL) | ny-llc-filing-fee-it-204-ll | sourced from the law |
| Formation | ny-formation | sourced from the law |
| XB, residency, leaving New York, part-year returns (IT-203) | ny-residency-leaving-new-york | checked against the law |

The folder also holds `ny-sales-tax.md` and `ny-llc-filing-fee.md`, which cover the same jobs as `new-york-sales-tax` and `ny-llc-filing-fee-it-204-ll`; they are being reviewed in a separate change. The New York City unincorporated business tax used to have a second copy in `skills/us/states/ny-nyc/`; it was folded into `nyc-ubt` on 13 November 2026.

Out of scope for this pack: property tax; estate tax; the New York City commercial rent tax; the New York City general corporation and business corporation taxes; partnership UBT (Form NYC-204); fiduciary returns; industry taxes (petroleum, highway use and the like).

## Official sources

- IT-2105-I (2026), 2026 rate schedules, MCTMT and estimated tax: https://www.tax.ny.gov/pdf/current_forms/it/it2105i.pdf (read 2026-11-13)
- IT-201-I (2025), resident return: https://www.tax.ny.gov/pdf/current_forms/it/it201i.pdf (read 2026-11-13)
- IT-203-I (2025), part-year and nonresident return: https://www.tax.ny.gov/pdf/current_forms/it/it203i.pdf (read 2026-11-13)
- Tax Law § 605, resident defined: https://www.nysenate.gov/legislation/laws/TAX/605 (read 2026-11-13)
- NYC Department of Finance, unincorporated business tax: https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page (read 2026-11-13)
- Form NYC-202 instructions (2025): https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf (read 2026-11-13)
