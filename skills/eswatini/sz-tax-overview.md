---
name: sz-tax-overview
description: "Eswatini Tax Overview for tax year 2026: rates, deadlines, how to file and worked examples, from official Eswatini sources. Use for questions about tax overview in Eswatini, ERS, TaxEase, emalangeni or SZL. Covers who it applies to, conditions and penalties. Items that official sources could not settle are listed as not yet confirmed."
jurisdiction: SZ
category: international
tax_year: 2026
tax_year_notes: "Year of assessment to 30 June 2026"
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eswatini Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone needing the map of Eswatini tax before opening a specific skill. Tax year: the year of assessment 1 July 2025 to 30 June 2026. The latest amending law found is the Income Tax (Amendment) Act 2023. ERS says those amendments took effect on 1 July 2024. No 2026 amending law was found on the ERS site, and that absence is not proof that none exists. The authority is the Eswatini Revenue Service (Revenue Authority Act 2008). Currency: lilangeni (plural emalangeni, E or SZL). The old pack's 1:1 rand peg is on the Not yet confirmed line.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Top personal rate | 33% above E200,000 | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Company rate | 25% | 2026 | https://www.ers.org.sz/whatsnew-file/1753959572719-FULL_PAGE___Income_Tax_Returns_Notice_2025.pdf |
| VAT standard rate | 15% | 2026 | https://www.ers.org.sz/documents/VATRateAmendmentRegulation2018.pdf |
| VAT registration | See [VAT](sz-vat-gst.md); official pages conflict | 2026 | https://www.ers.org.sz/Registration |
| Presumptive tax | 1.75% of turnover, 0% to E50,000 | 2026 | https://www.ers.org.sz/IncomeTax/PresumptiveTax |
| ENPF 2026 | E215 employee + E215 employer maximum | 2026 | https://enpf.co.sz/ |

## The base

Tax is on income from a source within or deemed within Eswatini. Legislated year: 1 July to 30 June; companies may hold an approved other year.

## Deadlines and filing

Latest published: companies 31 October 2025; individuals 31 October or 30 November 2025 by segment. All through TaxEase. PAYE by the 7th, withholding by the 15th. VAT: see [VAT](sz-vat-gst.md).

## Penalties and interest

Late return 20% of tax; late payment interest 18% a year.

## Cross-border points

Non-resident withholding is mostly 15%, interest 10%. See [Corporate income tax](sz-corporate-income-tax.md).

## Two worked examples that recompute

Dividend of E100,000 to a qualifying South African company without treaty: 12.5%.

```oa-check
name: Dividend withholding
inputs:
  dividend: 100000
steps:
  - tax: dividend * 0.125
expected:
  tax: 12500
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
| Income Tax (Amendment) Act 2023 (Act 20 of 2023); scanned, read by OCR, Third Schedule pages checked by eye; cited sections read | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf | 2026-11-01 |
| ERS, Public Notice, returns for tax year end 2025 (scanned, OCR); cited sections read | https://www.ers.org.sz/whatsnew-file/1753959572719-FULL_PAGE___Income_Tax_Returns_Notice_2025.pdf | 2026-11-01 |
| Legal Notice 112 of 2018, VAT rate; cited sections read | https://www.ers.org.sz/documents/VATRateAmendmentRegulation2018.pdf | 2026-11-01 |
| ERS, VAT Registration; whole page read | https://www.ers.org.sz/Registration | 2026-11-01 |
| ERS, Presumptive Tax; whole page read | https://www.ers.org.sz/IncomeTax/PresumptiveTax | 2026-11-01 |
| ENPF home page, public notice reproducing Legal Notice 5 of 2025; whole page read | https://enpf.co.sz/ | 2026-11-01 |

Not yet confirmed: The commencement notice for the 2023 Act was not opened; 1 July 2024 rests on the ERS Presumptive Tax page. The ERS notice for returns for the year ended 30 June 2026 was not found, so 2025 dates are given as the latest published. The lilangeni and rand peg: the Central Bank source was not opened.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
