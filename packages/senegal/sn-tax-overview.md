---
version: 1.0
name: sn-tax-overview
description: "Tax overview for Senegal, tax year 2026. Main rates (income tax top band 43 percent, company tax 30 percent, minimum tax 0.5 percent, VAT 18 percent, CFCE 3 percent, CGU 5 or 2 percent, money transfer tax) and the main annual deadlines, from the Code general des impots and the DGID. Use it to route a Senegal question to the right skill and to answer a quick rate or deadline question."
jurisdiction: SN
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Senegal tax overview

## Who this applies to

Anyone with a Senegal tax question for tax year 2026 (calendar year, amounts in XOF, the CFA franc). The Code general des impots (CGI) is administered by the Direction generale des Impots et des Domaines (DGID).

- Individuals with a tax home (domicile fiscal) in Senegal are taxed on worldwide income; others only on Senegal-source income (CGI art. 48, subject to tax treaties).
- Companies and other legal persons pay company tax (IS) on profit, with the minimum tax (IMF) as a floor.
- Small individual businesses (turnover TTC up to XOF 50 million) may fall in the CGU, a single flat contribution; landlords with gross rent under XOF 30 million in the CGF.
- Loi n. 2025-19, the finance law for 2026, was searched in full and does not change the rates below.

Details: [income tax](senegal-income-tax.md), [company tax](sn-corporate-income-tax.md), [VAT](senegal-vat.md), [payroll](senegal-payroll.md), [social contributions](senegal-social-contributions.md), [company formation](sn-company-formation.md).

## Rates, bands and thresholds

| Item | Figure | Tax year | Source |
|---|---|---|---|
| Income tax, top band | 43% on taxable income above XOF 50,000,000 (art. 173) | 2026 | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Income tax, lower bands | 0% to 630,000; 20% to 1,500,000; 30% to 4,000,000; 35% to 8,000,000; 37% to 13,500,000; 40% to 50,000,000 (art. 173) | 2026 | same |
| Company tax (IS) | 30% of taxable profit (art. 36) | 2026 | same |
| Minimum tax (IMF) | 0.5% of prior-year turnover excluding VAT, capped at XOF 5,000,000 (art. 40) | 2026 | same |
| VAT, standard | 18% (art. 369) | 2026 | same |
| VAT, approved tourist lodging | 10% (art. 369) | 2026 | same |
| CGU, service providers | 5% of turnover, minimum XOF 30,000 (art. 141) | 2026 | same |
| CGU, traders and producers | 2% of turnover, minimum XOF 25,000 (art. 141) | 2026 | same |
| CGU eligibility | Individuals with annual turnover TTC up to XOF 50 million | 2026 | https://www.dgid.sn/particuliers |
| CGF eligibility | Landlords with gross annual rent under XOF 30 million | 2026 | same |
| CFCE, employer flat contribution | 3% | 2026 | https://www.dgid.sn/loi-reglement |
| Money transfer tax | 0.5%, capped at XOF 2,000 (Loi 2025-17) | 2026 | same |

## The base

- Income tax: the global net income of the year, rounded down to the thousand francs, run through the art. 173 scale. Capital income has its own withholding rates (art. 173(2)); see [income tax](senegal-income-tax.md).
- Company tax: taxable profit, fractions under XOF 1,000 ignored (art. 36). The IMF is due on the turnover excluding VAT of the year before the tax year (art. 40); the company pays the higher of IS and IMF.
- VAT: supplies of goods and services in Senegal and imports; see [VAT](senegal-vat.md).
- CGU: the whole turnover of 1 January to 31 December of the previous year (art. 143); it stands in for income tax on business profit, the minimum tax and the local economic contribution, among others (art. 134).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Individual income tax return | Before 1 May each year for the previous year's income (art. 60) | https://www.dgid.sn/storage/docs/CGI-2025.pdf |
| Company tax return and financial statements | 30 April each year for the previous year (arts. 30, 31) | same |
| VAT | By the 15th of the month after the taxable event (art. 363) | same |
| Salary withholding | By the 15th of the next month; real simplified and CGU employers quarterly, by the 15th of January, April, July and October (art. 185) | same |
| CGU instalments | One third each, in the first 15 days of March and May (art. 144) | same |

Other annual dates (land taxes, the yearly salary summary, distributions): the DGID calendar of annual filings in Sources. Online filing runs through SENTAX; from 1 October 2026 it is open to CME1, CME2 and CPR taxpayers.

## Penalties and interest

Penalty figures sit in the domain skills: see [income tax](senegal-income-tax.md), [company tax](sn-corporate-income-tax.md) and [VAT](senegal-vat.md). This overview restates none of them (one figure, one home).

## Cross-border points

- Non-residents are taxed only on Senegal-source income (art. 48), subject to the tax treaties listed by the DGID.
- Companies active in Senegal and abroad also declare their total worldwide profit by 30 April (art. 30(2)).
- Withholding on payments abroad and treaty relief: see [company tax](sn-corporate-income-tax.md) and [income tax](senegal-income-tax.md).

## Two worked examples that recompute

Example 1: a sale of XOF 1,000,000 before VAT at 18% (art. 369). VAT is 180,000.

```oa-check
name: VAT at the standard rate
inputs:
  sale: 1000000
steps:
  - vat: sale * 0.18
expected:
  vat: 180000.00
```

Example 2, a decision (which tax is due, IS or IMF): profit of XOF 40,000,000 at 30% (art. 36), with prior-year turnover of XOF 500,000,000. The IMF would be 2,500,000 (art. 40), so IS of 12,000,000 is due because it is higher.

```oa-check
name: IS above IMF
inputs:
  profit: 40000000
  turnover: 500000000
steps:
  - imf: min(turnover * 0.005, 5000000)
  - tax: max(profit * 0.30, imf)
expected:
  tax: 12000000.00
```

## Ask the client first

- Individual or company, and for an individual, where the tax home is.
- Turnover of the previous year (decides CGU or real regime, and the IMF).
- Kind of activity: services, trade or production (CGU rate), or rent (CGF).
- Whether the business employs staff (CFCE, withholding, social contributions).
- Whether any income or payment crosses the border.

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition January 2025 (DGID): read arts. 30, 31, 36, 40, 48, 60, 134, 141, 143, 144, 173, 185, 363 and 369 in the PDF text for the rates, scale and deadlines above | https://www.dgid.sn/storage/docs/CGI-2025.pdf | 2026-11-14 |
| DGID, Lois et reglements: read the rates table (IS, IMF, VAT, CFCE, CGU, income tax scale) and the Loi 2025-17 measures (money transfer tax 0.5%, cap XOF 2,000) | https://www.dgid.sn/loi-reglement | 2026-11-14 |
| DGID, Particuliers page: read the CGU (turnover TTC up to XOF 50 million) and CGF (rent under XOF 30 million) eligibility lines | https://www.dgid.sn/particuliers | 2026-11-14 |
| Loi n. 2025-19, finance law for 2026 (scan, read by OCR, all 64 pages searched): no CGI amendment found; art. 19 adds a cashew export duty (not reopened) | https://budget.sec.gouv.sn/documents/public_download/69556841-a9d4-4658-8c1e-fe230a2a028a/telechargement | 2026-11-01 |
| DGID calendar of annual filings: read the table of annual filing dates by tax and CGI article | https://www.dgid.sn/storage/docs/calendrier-declarations-annuelles.pdf | 2026-11-14 |
| DGID SENTAX user guide v1.1, 2026: contents and filing steps read (not reopened) | https://www.dgid.sn/storage/uploads/guide-utilisateur-espace-connecte-1790609363.pdf | 2026-11-01 |
| DGID communique: SENTAX open to CME1, CME2 and CPR taxpayers from 1 October 2026, full text read (not reopened) | https://www.dgid.sn/storage/uploads/communique-ouverture-de-la-plateforme-sentax-aux-contribuables-du-cme1-cme2-et-du-cpr-1790699194.pdf | 2026-11-01 |
| DGID Entreprises page: read the descriptions of the online portals | https://www.dgid.sn/entreprises | 2026-11-14 |

Not yet confirmed: the text of Loi 2025-17 was not opened; only the DGID summary of it was read, so any CGI change it made beyond that summary is not reflected.
