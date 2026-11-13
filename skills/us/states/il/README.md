---
jurisdiction: US-IL
applicable: [IT-IND, IT-CORP, VAT, SC, PR]
not_applicable: {}
covered_by:
  IT-IND: il-income-tax
  IT-CORP: il-pprt
  VAT: illinois-sales-tax
  SC: il-payroll
  PR: il-payroll
partial:
  IT-CORP: "unitary combined returns (Schedule UB), insurance, financial and transportation companies, and the S corporation standard exemption are not covered"
  SC: "Secure Choice default contribution rate and enrollment deadlines, and Chicago and Cook County leave ordinances, not yet confirmed"
---

# Illinois (US-IL): tax pack

Calendar tax year for individuals; corporations and partnerships follow their federal year. Authority: the Illinois Department of Revenue (IDOR), tax.illinois.gov, and for unemployment insurance the Illinois Department of Employment Security (IDES), ides.illinois.gov. Currency: US dollars. Illinois taxes individuals at a flat 4.95% of net income (35 ILCS 5/201(b)(5.4)), with a 2026 exemption allowance of $2,925 (IDOR Bulletin FY 2026-15); C corporations at 7% income tax plus 2.5% Personal Property Replacement Income Tax (201(b)(14), 201(d)); S corporations, partnerships and trusts at 1.5% replacement tax (201(d)); and retail sales at a 6.25% State rate (1% on drugs and medical appliances) plus local taxes, with no State tax on groceries from 1 January 2026 (IDOR Bulletin FY 2026-03). Illinois has no franchise tax on income and no gross receipts tax. A US state: federal income tax, FICA and FUTA sit on top of every domain here.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax (Form IL-1040) | il-income-tax | sourced from the law, 2026 |
| IT-IND, estimated tax for individuals (Form IL-1040-ES) | il-estimated-tax | sourced from the law, 2026 |
| IT-CORP, corporate income tax and replacement tax (IL-1120, IL-1120-ST, IL-1065), and the pass-through entity tax | il-pprt | sourced from the law, 2026 (partial) |
| VAT / sales and use tax (Form ST-1) | illinois-sales-tax | sourced from the law, 2026 |
| SC, unemployment insurance (IDES) | il-payroll | sourced from the law, 2026 |
| PR, payroll withholding (IL-941) | il-payroll | sourced from the law, 2026 |

`il-sales-tax` was retired on 13 November 2026 and folded into `illinois-sales-tax`. There is no separate individual return-assembly skill: `il-income-tax` covers the whole IL-1040.

Out of scope for this pack: property tax (administered by counties); estate tax; excise taxes (motor fuel, tobacco, liquor, cannabis); hotel, automobile renting and telecommunications taxes; taxes Chicago and other local governments collect themselves; part-year and nonresident individual returns (Schedule NR); trusts and estates (IL-1041); unitary combined returns.

## Official sources

- 35 ILCS 5/201 (rates, replacement tax, pass-through entity tax): https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K201 (read 2026-11-13)
- 35 ILCS 5/204 (exemption): https://www.ilga.gov/legislation/ilcs/fulltext.asp?DocName=003500050K204 (read 2026-11-13)
- IDOR Bulletin FY 2026-15, What's New for Illinois Income Taxes: https://tax.illinois.gov/research/publications/bulletins/fy-2026-15.html (read 2026-11-13)
- IDOR Bulletin FY 2026-03, grocery tax changes: https://tax.illinois.gov/research/publications/bulletins/fy-2026-03.html (read 2026-11-13)
- Booklet IL-700-T (2026 withholding tables): https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/withholding/documents/currentyear/il-700-t.pdf (read 2026-11-13)
- IDES 2026 Historical Rate Chart: https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf (read 2026-11-13)
