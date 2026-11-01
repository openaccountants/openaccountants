---
name: cameroon-cross-border
description: "Cameroon cross-border tax for 2026: tax on non-resident payments (TSR 15%, 10%, 3%), digital significant economic presence, tax-haven rules and residence, under the CGI Edition 2026."
version: 0.1
jurisdiction: CM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cameroon cross-border tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Cameroon payers of non-residents, non-resident digital businesses, and individuals moving in or out. Treaties override the rates here (CGI art. 225).

## Rates, bands and thresholds

| Item | Rate or amount | Source |
|---|---|---|
| Special income tax (TSR), general | 15% | CGI art. 225 ter: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| TSR, one-off material services, firms waiving filing | 10% | same |
| TSR, reduced (public orders, digital audiovisual access, oil research phase, listed shipping, money transfer commissions) | 3% | same |
| CAC on TSR | 5% of principal | CGI Titre III, centimes additionnels: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Passive income to a tax haven | 30% | CGI art. 70(1): https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Digital presence, billing | Over XAF 50,000,000 a year | CGI art. 5 ter: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Digital presence, users | Over 1,000 | CGI art. 5 ter: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |
| Digital instalment | 3% of gross Cameroon revenue | CGI art. 21(1)f: https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf |

## The base

TSR applies to royalties, software, technical and financial assistance, consulting, equipment rental and, in general, sums paid abroad for services supplied or used in Cameroon (art. 225(1)). Charges with tax-haven parties are not deductible (art. 8 ter), save customs-cleared goods bought in their production country.

## Deadlines and filing

Digital non-residents file gross turnover monthly and pay by the 15th of the next month on the DGI portal (art. 23 bis). Other withheld tax follows its own article; the art. 226 to 228 dates were not read.

## Penalties and interest

Late withheld tax: 10% a month, cap 30%, plus interest of 1.5% a month, with a further fine in art. L 106(2).

## Cross-border points

An individual with a home, main stay, main activity or economic centre in Cameroon is domiciled there and taxed worldwide (art. 25). Non-residents pay on Cameroon-source income. The DGI lists treaties, including South Africa, China and the Czech Republic. Their texts were not read, so no treaty rate is given. If a treaty applies, read it before withholding.

## Two worked examples that recompute

```oa-check
name: Consulting fee 10 million to non-resident, no treaty
inputs:
  fee: 10000000
steps:
  - tsr: fee * 0.15
  - cac: tsr * 0.05
  - total: tsr + cac
expected:
  tsr: 1500000
  cac: 75000
  total: 1575000
```

```oa-check
name: Digital firm, 400 million Cameroon revenue, 3 percent
inputs:
  revenue: 400000000
steps:
  - over_limit: revenue - 50000000
  - instalment: revenue * 0.03
expected:
  over_limit: 350000000
  instalment: 12000000
```

## Ask the client first

1. Where is the payee resident, and does it have a Cameroon establishment?
2. What exactly is paid for?
3. Is a treaty certificate held?
4. For digital firms, Cameroon billings and user count?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code General des Impots, Edition 2026 (DGI): arts. 5 ter, 8 ter, 21, 23 bis, 25, 70, 225, 225 ter, L 106, CAC articles of Titre III | https://www.impots.cm/sites/default/files/documents/CODE%20GENERAL%20DES%20IMPOTS%202026%20SITE%20DGI%20VERSION%20FRANCAISE.pdf | 2026-11-01 |

Not yet confirmed: treaty texts and rates; exact article number of the 5% CAC on TSR; TSR payment date; whether the digital CAC applies; rules on dividends and interest paid to non-residents beyond art. 70.
