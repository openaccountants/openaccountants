---
name: sz-tax-overview
description: "Eswatini Tax Overview for tax year 2026: rates, deadlines, how to file and worked examples, from official Eswatini sources. Use for questions about tax overview in Eswatini, ERS, TaxEase, emalangeni or SZL. Covers who it applies to, conditions and penalties. Items that official sources could not settle are listed as not yet confirmed."
jurisdiction: SZ
category: international
tax_year: 2026
tax_year_notes: "Year of assessment to 30 June 2026"
version: 0.4
last_updated: 2026-11-26
type: situation-rules
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
---

# Eswatini Tax Overview v0.4

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone needing the map of Eswatini tax before opening a specific skill. Tax year: the year of assessment 1 July 2025 to 30 June 2026. The latest amending law found is the Income Tax (Amendment) Act 2023. ERS says those amendments took effect on 1 July 2024. No 2026 amending law was found on the ERS site, and that absence is not proof that none exists. The authority is the Eswatini Revenue Service (Revenue Authority Act 2008). Currency: lilangeni (plural emalangeni, E or SZL). The old pack's 1:1 rand peg is on the Not yet confirmed line.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Top personal rate | 33% above E200,000 | 2026 | https://www.ers.org.sz/IncomeTax/RatesandThres |
| Company rate | 25% | 2026 | https://www.ers.org.sz/whatsnew-file/1753959572719-FULL_PAGE___Income_Tax_Returns_Notice_2025.pdf |
| VAT standard rate | 15% | 2026 | https://www.ers.org.sz/documents/VATRateAmendmentRegulation2018.pdf |
| VAT registration | See [VAT](sz-vat-gst.md); official pages conflict | 2026 | https://www.ers.org.sz/Registration |
| Presumptive tax | 1.75% of turnover, 0% to E50,000 | 2026 | https://www.ers.org.sz/IncomeTax/PresumptiveTax |
| ENPF 2026 | E215 employee + E215 employer maximum | 2026 | https://enpf.co.sz/ |

## The base

Tax is on income from a source within or deemed within Eswatini. Legislated year: 1 July to 30 June; companies may hold an approved other year.

## Deadlines and filing

Year ended 30 June 2026 (ERS notice): non-individual entities, businesses and presumptive taxpayers 31 October 2026; individuals in the listed segments 30 November 2026. All through TaxEase. PAYE by the 7th, withholding by the 15th. VAT: see [VAT](sz-vat-gst.md).

## Penalties and interest

Late return 20% of tax; late payment interest 18% a year.

## Cross-border points

Non-resident withholding is 15%, including dividends, interest and branch profits tax since 1 July 2024, subject to treaty relief. See [Corporate income tax](sz-corporate-income-tax.md).

## Two worked examples that recompute

Dividend of E100,000 to a South African company holding under 25%: 15% under s 21(2), as Act 20 of 2023 s 10 deleted the 12.5% proviso from 1 July 2024; the treaty also allows 15%. At 25% or more the treaty gives 10%.

```oa-check
name: Dividend withholding
inputs:
  dividend: 100000
steps:
  - tax: dividend * 0.15
expected:
  tax: 15000
```

Decision: sole trader or company on profit E300,000, all paid out. Sole trader E72,300; company plus 10% resident dividend E97,500. The sole trader pays less on this profit.

```oa-check
name: Sole trader or company, profit E300,000
inputs:
  profit: 300000
steps:
  - sole: 47500 + (profit - 200000) * 0.33 - 8200
  - cit: profit * 0.25
  - div: (profit - cit) * 0.10
  - company: cit + div
expected:
  sole: 72300
  company: 97500
```

## Ask the client first

1. Individual, company or branch?
2. Where is the income sourced?
3. What is turnover?
4. Any employees?
5. Any non-resident payments?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment) Act 2023 (Act 20 of 2023), scanned: read by OCR on 2026-11-01 for the Third Schedule and cited sections; ss 10, 11 and 14 (amending ss 21, 27 and 32E) re-read on 2026-11-26 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf | 2026-11-26 |
| ERS, Income Tax Order Changes 2024: read in full for the 1 July 2024 effective date and the 15% rates under ss 21, 27 and 32E | https://ers.org.sz/whatsnew-file/1726738466004-Income_Tax_Order_Changes__2024.pdf | 2026-11-26 |
| ERS, Public Notice, returns for tax year end 2025 (scan): read in full for the filing deadlines and the 25% and 1.75% rates | https://www.ers.org.sz/whatsnew-file/1753959572719-FULL_PAGE___Income_Tax_Returns_Notice_2025.pdf | 2026-11-14 |
| ERS, Public Notice, annual income tax return submission and payment for tax year end 2026: read in full for the deadlines, return thresholds and the 25% and 1.75% rates | https://ers.org.sz/whatsnew-file/1791462650754-1784270658474_Notice_for_Filing_Income_tax_Returns_Public_Notice_Final_Aligned.pdf | 2026-11-26 |
| Legal Notice 112 of 2018, VAT rate (scan): read in full, both pages, for the 15% rate from 1 August 2018 | https://www.ers.org.sz/documents/VATRateAmendmentRegulation2018.pdf | 2026-11-14 |
| ERS, VAT Registration: read in full | https://www.ers.org.sz/Registration | 2026-11-14 |
| ERS, Presumptive Tax: read in full | https://www.ers.org.sz/IncomeTax/PresumptiveTax | 2026-11-14 |
| ENPF home page, public notice reproducing Legal Notice 5 of 2025: read in full | https://enpf.co.sz/ | 2026-11-14 |

Not yet confirmed: The commencement notice for the 2023 Act was not opened; 1 July 2024 rests on the ERS Presumptive Tax page. The lilangeni and rand peg: the Central Bank source was not opened.
