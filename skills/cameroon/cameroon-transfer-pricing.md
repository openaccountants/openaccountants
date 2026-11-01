---
name: cameroon-transfer-pricing
description: "Cameroon transfer pricing for 2026: the 25% link test, profit add-back, annual declaration, documentation limits, country-by-country report and XAF 50 million fine, under the CGI Edition 2026."
version: 0.1
jurisdiction: CM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: transfer-pricing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cameroon transfer pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies dependent on, or controlling, companies in or outside Cameroon (CGI art. 19). A link exists at 25% of capital or votes, by actual decision power, or under common control (art. 19 bis). No link is needed for transfers to a tax haven or privileged regime (art. 19(2)).

## Rates, bands and thresholds

| Item | Rate or amount | Source |
|---|---|---|
| Link test | 25% of capital or votes | CGI art. 19 bis: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Documentation limit | Turnover or gross assets of XAF 1 billion or more; or a holding over 25% tied to such a firm | LPF art. L 19 bis: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Country-by-country group limit | Consolidated turnover of XAF 492 billion or more | CGI art. 18 quater: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Country-by-country deadline | 12 months after year end | CGI art. 18 quater: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Fine for arts. 18 ter, 18 quater, L 6 bis | XAF 50,000,000 | LPF art. L 104(2): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Tax-haven test | Tax under one third of Cameroon's, or non-cooperative | CGI art. 8 ter: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |

## The base

Profits moved through prices or otherwise are added back, by comparison with what independent firms would have earned (art. 19(1)).

## Deadlines and filing

Large enterprises unit members file the annual transfer pricing declaration electronically by the art. 18 date, 15 March (art. 18 ter). Documentation must be ready in electronic form when an audit starts (art. L 19 bis). Its content is set by the arrete printed in the CGI annexes.

## Penalties and interest

A missing, late, incomplete or non-compliant declaration draws the XAF 50,000,000 fine (art. 18 ter(3), L 104(2)). Tax on the add-back carries the normal penalties (art. L 95, L 96).

## Cross-border points

Treaties may give a mutual agreement route; check the treaty. An advance agreement on method exists in the LPF; its article was not read in full.

## Two worked examples that recompute

```oa-check
name: Royalty 500 million, arm's length 300 million, 33 percent with CAC
inputs:
  paid: 500000000
  arm: 300000000
steps:
  - addback: paid - arm
  - tax: addback * 0.33
expected:
  addback: 200000000
  tax: 66000000
```

```oa-check
name: Same add-back at 25 percent, good faith penalty
inputs:
  addback: 200000000
steps:
  - tax: addback * 0.25
  - penalty: tax * 0.30
  - cac: (tax + penalty) * 0.10
  - total: tax + penalty + cac
expected:
  tax: 50000000
  penalty: 15000000
  cac: 6500000
  total: 71500000
```

## Ask the client first

1. Group chart and holdings at 25%?
2. Turnover and gross assets of each Cameroon entity?
3. Which tax office manages the company?
4. Group consolidated turnover?
5. Any payee in a low-tax place?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code General des Impots, Edition 2026 (DGI): arts. 8 ter, 18 ter, 18 quater, 19, 19 bis, L 19 bis, L 104, documentation arrete in annexes | https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf | 2026-11-01 |

Not yet confirmed: the DGI transfer pricing instruction (a scan, 47 pages, not read); the methods list; the advance agreement article; the audit-limit extension.
