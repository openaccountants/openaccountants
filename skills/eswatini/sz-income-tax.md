---
name: sz-income-tax
description: "Eswatini Personal Income Tax for tax year 2026: rates, deadlines, how to file and worked examples, from official Eswatini sources. Use for questions about personal income tax in Eswatini, ERS, TaxEase, emalangeni or SZL. Covers who it applies to, conditions and penalties. Items that official sources could not settle are listed as not yet confirmed."
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

# Eswatini Personal Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Natural persons with Eswatini-source income. Tax year: the year of assessment 1 July 2025 to 30 June 2026. The latest amending law found is the Income Tax (Amendment) Act 2023. ERS says those amendments took effect on 1 July 2024. No 2026 amending law was found on the ERS site, and that absence is not proof that none exists.

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Up to E100,000 | 20% | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| E100,000 to E150,000 | E20,000 + 25% of the excess | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| E150,000 to E200,000 | E32,500 + 30% of the excess | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Above E200,000 | E47,500 + 33% of the excess | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Rebate | E8,200 a year, apportioned for a part year. Effective threshold E41,000 of taxable income | 2026 | https://www.ers.org.sz/IncomeTax/RatesandThres |
| Extra rebate, over 60 on the last day of the year | E2,700, total E10,900 | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Redundancy or retirement lump sum above the exempt amount | 25% to E330,000, then E82,500 + 30% of the excess. No rebate. The ERS page still shows older bands; the Act wins | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Resident dividends, natural person | 10%, final per ERS guide | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Resident interest, natural person | 10%, final, no deduction, no refund (s 32C) | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Non-resident natural person minimum | Not below 10% of taxable income, or 3% on pension income | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Trust | 33% | 2026 | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf |
| Small business presumptive tax | Turnover to E50,000: 0%. Above E50,000 and below E500,000: 1.75% of total turnover. Excludes professionals and persons with investment income | 2026 | https://www.ers.org.sz/IncomeTax/PresumptiveTax |

## The base

Tax is on income from a source within or deemed within Eswatini. Non-residents use the same table, subject to the minimum above. Pension contributions are deductible up to 15% of pensionable salary (s 14(1)(i) as amended). A gain on a business asset is taxable under Division X (ss 32I onward), with immovable property indexed after 12 months. Leaving residence is a deemed disposal of business assets at market value unless the Commissioner exempts it against security.

## Deadlines and filing

Self-assessment applies to all taxpayers; pay on or before the return due date. For the year ended 30 June 2025 the notice set 31 October 2025 for presumptive taxpayers and 30 November 2025 for individuals with employment income above E3 million, with employment and other income, and high net worth individuals. A single-employer employee taxed on the Final Deduction System with gross employment income under E3 million does not file. Directors, clergy, partners, professionals, and people with several employers or with bank interest or dividends do file.

### How to file
1. Register for a TIN using the ERS form at a Service Centre; registration takes 4 working days.
2. Log in to TaxEase at https://taxease.ers.org.sz/ . The notice says returns go through TaxEase only.
3. Complete the return and attach documents. It stands as your assessment, so no notice of assessment follows.
4. Pay by EFT, speed point at a Service Centre, MoMo Pay or bank deposit, quoting the reference. Cash is not accepted.

Provisional tax, for persons with non-remuneration income above E1,000: first payment by 31 December, second by 30 June, third by the return date.

## Penalties and interest

Late return: 20% of tax payable, or E20 a day on a loss. Late payment: 18% a year. Late provisional payment or an estimate under 90% of actual income: 20%. Keep records 5 years, in English or siSwati.

## Cross-border points

Withholding on payments to non-residents is in [Corporate income tax](sz-corporate-income-tax.md). Treaties are published by ERS for Botswana, Lesotho, Mauritius, Seychelles, South Africa, Taiwan and the United Kingdom.

## Two worked examples that recompute

Employee, taxable income E180,000: E32,500 + 30% of E30,000, less the rebate.

```oa-check
name: Taxable income E180,000
inputs:
  income: 180000
steps:
  - gross: 32500 + (income - 150000) * 0.30
  - tax: gross - 8200
expected:
  tax: 33300
```

Decision: a trader with turnover E300,000 and profit E120,000 compares presumptive tax with normal tax. Presumptive is E5,250; normal is E16,800. Presumptive wins unless profit is low. Check that the person is not a professional and has no investment income.

```oa-check
name: Presumptive or normal, turnover E300,000, profit E120,000
inputs:
  turnover: 300000
  profit: 120000
steps:
  - presumptive: turnover * 0.0175
  - normal: 20000 + (profit - 100000) * 0.25 - 8200
  - saving: normal - presumptive
expected:
  presumptive: 5250
  normal: 16800
  saving: 11550
```

## Ask the client first

1. Is the income from an Eswatini source, and are you ordinarily resident?
2. Is employment your only income, from one employer, and under E3 million?
3. What is your age on 30 June?
4. Do you trade, and is turnover below E500,000? Is the work professional?
5. Do you hold bank interest, dividends or rental income?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment) Act 2023 (Act 20 of 2023); scanned, read by OCR, Third Schedule pages checked by eye; cited sections read | https://www.ers.org.sz/documents/IncomeTaxAmendmentAct2023.pdf | 2026-11-01 |
| ERS, Rates and Thresholds; whole page read | https://www.ers.org.sz/IncomeTax/RatesandThres | 2026-11-01 |
| ERS, Presumptive Tax; whole page read | https://www.ers.org.sz/IncomeTax/PresumptiveTax | 2026-11-01 |
| ERS, Public Notice, returns for tax year end 2025 (scanned, OCR); cited sections read | https://www.ers.org.sz/whatsnew-file/1753959572719-FULL_PAGE___Income_Tax_Returns_Notice_2025.pdf | 2026-11-01 |
| ERS, Income Tax Returns; whole page read | https://www.ers.org.sz/IncomeTax/IncomeTaxReturn | 2026-11-01 |
| ERS, Self Assessment; whole page read | https://www.ers.org.sz/IncomeTax/SelfAssessment | 2026-11-01 |
| ERS, Step-by-Step Guide for New Businesses; whole page read | https://www.ers.org.sz/documents/Step-ByStepGuideforNewBusinesses.pdf | 2026-11-01 |
| Income Tax Order 1975, ERS consolidated copy to the 2013 amendments; sections cited were read; cited sections read | https://www.ers.org.sz/documents/IncomeTaxOrder1975.pdf | 2026-11-01 |

Not yet confirmed: The commencement notice for the 2023 Act was not opened; 1 July 2024 rests on the ERS Presumptive Tax page. The ERS notice for returns for the year ended 30 June 2026 was not found, so 2025 dates are given as the latest published. The ERS Income Tax Returns page still gives E1.2 million; the 2025 notice says E3 million and the notice is used here. The guide gives E2 million for TIN registration, unresolved. The old pack's residence day-count test has no source: the Order uses "ordinarily resident" and no day count was found. The Third Schedule text names the year ended 30 June 2023 and no later schedule was found. The exempt lump sum under s 14(1)(l)(iii) was not extracted.

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
