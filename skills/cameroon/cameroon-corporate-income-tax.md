---
name: cameroon-corporate-income-tax
description: "Cameroon company income tax (impot sur les societes) for 2026: 30% and 25% rates, CAC, 2.2% instalments and minimum tax, loss carry-forward, return dates and penalties, under the CGI Edition 2026."
version: 0.1
jurisdiction: CM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cameroon company income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies and other bodies liable under CGI art. 2 to 5. Profit made in Cameroon is taxable, including a complete commercial cycle there (art. 5). A non-resident digital business with significant economic presence is covered in `cameroon-cross-border`.

## Rates, bands and thresholds

| Item | Rate or amount | Source |
|---|---|---|
| Standard rate | 30% | CGI art. 17(1): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Turnover up to XAF 3 billion | 25% | CGI art. 17 bis: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| CAC on instalments and minimum | 10% | CGI art. 21, 22(2): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Monthly instalment, real regime | 2% of turnover (2.2% with CAC) | CGI art. 21(1)a: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Distributors of price-margin products | 14% of gross margin plus CAC | CGI art. 21: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Not on a tax centre file | 10%; forestry without permit 20% | CGI art. 21(1)e: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Minimum tax | 2% or 14% of base plus CAC; 5% simplified regime as written | CGI art. 22(2): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Cash payment not deductible | XAF 100,000 or more per operation | CGI art. 8 bis: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Loss carry-forward | Up to the 4th following year; 6th for banks and State firms in restructuring | CGI art. 12: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |

## The base

Net profit after charges directly needed for the taxable activity (art. 7). Not deductible: cash payments above the limit, invoices without required details or outside the e-invoice system, payments to taxpayers not on the active file (art. 8 bis), and tax-haven charges (art. 8 ter), save goods bought in their country of production and customs-cleared. Round taxable profit down to XAF 1,000 (art. 17(3)). The minimum uses prior-year turnover, excluding tax, rounded down to XAF 1,000 (art. 23).

## Deadlines and filing

| Taxpayer | Return |
|---|---|
| Large enterprises unit | 15 March (art. 18) |
| Medium and specialised tax centres | 15 April |
| Local tax centres | 15 May |

Monthly instalments fall due on the 15th of the next month. The return follows OHADA accounting and comes with the DIPE staff document (art. 18(3)). Portal steps were not traced, so none are given.

## Penalties and interest

| Item | Amount | Source |
|---|---|---|
| Late self-assessed filing or payment | 10% a month, cap 30%; interest 1.5% a month | LPF art. L 106: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Understatement | 30%, 100%, 150%; interest capped at 50% | LPF art. L 95, L 96: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| No return after notice | Plus 100%, 150% on repeat | LPF art. L 97: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| DSF not filed, large enterprise | XAF 5,000,000 | LPF art. L 99(3): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |

## Cross-border points

Related-party profit shifting is added back (art. 19); see `cameroon-transfer-pricing`. Payments abroad: see `cameroon-cross-border`.

## Two worked examples that recompute

```oa-check
name: Turnover 2 billion, profit 200 million, 2026
inputs:
  turnover: 2000000000
  profit: 200000000
steps:
  - tax: profit * 0.25
  - instalments: turnover * 0.022
  - balance: tax - instalments
expected:
  tax: 50000000
  instalments: 44000000
  balance: 6000000
```

```oa-check
name: Turnover 5 billion, profit 40 million, minimum applies, 2026
inputs:
  turnover: 5000000000
  profit: 40000000
steps:
  - tax: profit * 0.30
  - minimum: turnover * 0.022
  - due: max(tax, minimum)
expected:
  tax: 12000000
  minimum: 110000000
  due: 110000000
```

The examples apply no CAC to the 25% or 30% rate.

## Ask the client first

1. Turnover excluding tax for the year?
2. Which tax office manages the company?
3. Any special or incentive regime?
4. Any price-margin activity?
5. Losses brought forward and from which years?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code General des Impots, Edition 2026 (DGI): arts. 2, 5, 7, 8 bis, 8 ter, 12, 17, 17 bis, 18, 21 to 23, L 95 to L 99, L 106 | https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf | 2026-11-01 |

Not yet confirmed: whether CAC is added to the 25% or 30% rate (art. 17 does not state it; the old VAT skill's 33% is not confirmed for companies); depreciation rates; the Finance Law 2026 circular, a scan not read; portal steps.
