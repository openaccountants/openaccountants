---
name: dj-tax-overview
description: "Use as the starting map of Djibouti tax for 2026: IBP 25%, IMF 1%, ITS to 45%, VAT 10%, CNSS 21.7%, dividends 5%, and the main dates."
version: 2.0
jurisdiction: DJ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Djibouti Tax Overview

## Who this applies to

Anyone starting a Djibouti question. The tax authority is the Direction Generale des Impots, under the Ministry of the Budget. The law is the Code General des Impots plus each year's finance law. Currency: Djibouti franc (FD, FDJ). This skill points to the others and does not replace them.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Company profits | 25% | Art. 56; dj-corporate-income-tax | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Minimum tax | 1%, floor 120,000 | Arts. 60, 61 | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Top ITS band | 45% | Above 2,000,000 a month | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ |
| VAT | 10% | Art. 187 | https://www.journalofficiel.dj/texte-juridique/loi-n82-an-14-7eme-l-portant-budget-initial-de-letat-pour-lexercice-2015/ |
| CNSS | 21.7% | Employer 15.7%, employee 6% | https://cnss.dj/declaration-et-versement-des-cotisations/ |
| Dividends | 5% | Art. 90L | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n-64-an-23-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2024/ |
| Non-resident payments | 25% | Art. 75 as amended by LF 2024 art. 26 | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n-64-an-23-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2024/ |

## The base

Tax year: calendar year (art. 27). Profits tax reaches profits made in Djibouti, including exports (art. 25); foreign-source treatment beyond that was not confirmed. Other taxes: patentes, licences, property, registration and stamp duty, all in the CGI. LF 2026 made no direct tax rate change: its Titre II keeps the 2025 rectified measures and changes customs rules.

## Deadlines and filing

| Item | Date or rule | Source |
|---|---|---|
| CNSS | By the 10th | https://cnss.dj/affiliation-employeur/ |
| ITS | Before the 10th | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n-64-an-23-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2024/ |
| VAT | By the 20th | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| IBP return | Before 1 April | https://www.journalofficiel.dj/texte-juridique/loi-n82-an-14-7eme-l-portant-budget-initial-de-letat-pour-lexercice-2015/ |
| Instalments | April, August, November | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n181-an-22-8eme-l-portant-budget-initial-de-letat-de-lexercice-2023/ |

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late payment | 5% surcharge plus 0.5% interest per month; no 5% on audit assessments (art. 247) | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Late or missing return | Interest 5% (art. 246 as amended 2021; the earlier text was 0.5% per month) plus 10% if filed within 10 days of formal notice, 40% after that or never | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n111-an-20-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2021/ |

## Cross-border points

Non-residents: 25% on service fees, 5% on dividends. VAT: representative needed. Conventions override (art. 25).

## Two worked examples that recompute

Example 1: trader with 200,000,000 turnover, profit 10,000,000: tax 2,500,000, not IMF.

```oa-check
name: Tax due
inputs:
  profit: 10000000
  turnover: 200000000
steps:
  - due: max(profit*0.25,turnover*0.01)
expected:
  due: 2500000.00
```

Example 2, the decision: consultant billing 11,000,000 sets a 10% VAT line because the 10,000,000 limit is passed.

```oa-check
name: VAT on invoice
inputs:
  fees: 11000000
steps:
  - vat: fees*0.10
expected:
  vat: 1100000.00
```

## Ask the client first

- Who is the taxpayer: person or company?
- Activity and turnover.
- Employees?
- Foreign payments or owners?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition updated to the 2011 finance law, Ministry of Finance: articles cited read in the PDF text; later changes taken from the finance laws listed here | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf | 2026-11-01 |
| Loi de finances 203/AN/25/9eme L, budget 2026 (JO 31/12/2025): Titre II read; direct tax: rectified 2025 measures stay in force, no CGI rate change | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n203-an-25-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2026/ | 2026-11-01 |
| Loi de finances 64/AN/23/9eme L, budget 2024: Titre II tax articles read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n-64-an-23-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2024/ | 2026-11-01 |
| Loi de finances 181/AN/22/8eme L, budget 2023: Titre II read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n181-an-22-8eme-l-portant-budget-initial-de-letat-de-lexercice-2023/ | 2026-11-01 |
| Loi de finances 142/AN/21/8eme L, budget 2022: Titre II read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ | 2026-11-01 |
| Loi de finances 111/AN/20/8eme L, budget 2021: articles 6 to 20 read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n111-an-20-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2021/ | 2026-11-01 |
| Loi 82/AN/14/7eme L, budget 2015: articles 8 to 29 read | https://www.journalofficiel.dj/texte-juridique/loi-n82-an-14-7eme-l-portant-budget-initial-de-letat-pour-lexercice-2015/ | 2026-11-01 |
| CNSS, Declaration et versement des cotisations: full page read | https://cnss.dj/declaration-et-versement-des-cotisations/ | 2026-11-01 |
| CNSS, Affiliation employeur: full page read | https://cnss.dj/affiliation-employeur/ | 2026-11-01 |

Not yet confirmed: The CGI on the official site is the 2011 edition. No consolidated 2026 code could be opened (impots.dj, dgi.dj and economie.gouv.dj did not answer), so each rule is the 2011 text plus the finance laws read; the finance laws found in the gazette for 2013 to 2026 were scanned for tax articles, the 2012 law was not, so an amendment made only there or in a law the gazette search missed would not show. Peg of the franc to the US dollar was in the old skill, not checked in a Central Bank text. The old statement that Djibouti follows OHADA rules was removed: the Code de commerce and the texts read make no such link, and membership was not checked at OHADA itself. Accounting standard: a Plan Comptable General 2012 is linked on the ministry site, not opened.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
