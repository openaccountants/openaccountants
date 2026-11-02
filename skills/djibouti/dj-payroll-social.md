---
name: dj-payroll-social
description: "Use for Djibouti payroll for tax year 2026: CNSS 21.7% (employer 15.7%, employee 6%), the 400,000 ceiling, filing by the 10th, ITS withholding and penalties."
version: 2.0
jurisdiction: DJ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Djibouti Payroll and Social Contributions

## Who this applies to

Every employer with staff, public or private, and domestic employers. Employers join the CNSS within 48 hours of opening or of hiring domestic staff. Self-employed pay care only.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Total | 21.7% | Of total pay | https://cnss.dj/declaration-et-versement-des-cotisations/ |
| Family benefits | 5.5% | Employer only | same |
| Pension | 8% | Employer 4%, employee 4%. No ceiling | same |
| Care | 7% | Employer 5%, employee 2% | same |
| Work injury | 1.2% | Employer only. Derived: page states 8.2% for care and injury, 7% care. The CNSS table on the financing page shows 1%; see below |  same |
| Employer total | 15.7% | 5.5 + 4 + 5 + 1.2 | same |
| Employee total | 6% | 4 + 2 | same |
| Self-employed | 7% | Care only | https://cnss.dj/financement-de-la-cnss/ |
| Ceiling | 400,000 a month | All schemes except pension (Arrete 2015-605 art. 1) | https://www.journalofficiel.dj/texte-juridique/arrete-n2015-605-pr-mtra-portant-modification-du-plafonnement-des-remunerations-entrant-en-compte-pour-la-determination-de-lassiette-des-cotisations-dues-a-la-cnss-et-revalorisation-du-bareme/ |
| Floor, business | 20,000 | Minimum pay counted | https://cnss.dj/declaration-et-versement-des-cotisations/ |
| Floor, domestic | 15,850 | Minimum pay counted | same |
| ITS withholding | 2% to 45% | See dj-income-tax for bands | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ |

## The base

Base: all direct and indirect pay: wages, paid leave, allowances, bonuses and the cash value of benefits in kind. Benefits are valued by the Arrete 2015-605 scale, inside the ceiling.

## Deadlines and filing

| Item | Date or rule | Source |
|---|---|---|
| CNSS | Within the first 10 days of the next month, with a signed named list, even if unpaid (arts. 134, 135 of Arrete 69-1883). The old skill said the 15th | https://cnss.dj/affiliation-employeur/ |
| ITS | Before the 10th of the next month | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n-64-an-23-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2024/ |
| Join CNSS | 48 hours | https://cnss.dj/affiliation-employeur/ |

Steps:
1. Affiliate the employer and register each employee at the CNSS.
2. Run pay, cap care, family and injury bases at 400,000.
3. File the named list and pay by the 10th. A tele-declaration service is listed on the CNSS site.
4. Withhold ITS on pay after employee CNSS and remit before the 10th.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late contributions | 10% from the 10th; a further 3% after one more month | https://cnss.dj/penalites-sanctions-et-poursuites/ |
| No named list | 400 per employee per month or part, capped at 40,000 a month | https://cnss.dj/penalites-sanctions-et-poursuites/ |
| No affiliation | Criminal offence: Arrete 69-1883 art. 122, Loi 188/AN/85 art. 10 | https://cnss.dj/affiliation-employeur/ |

## Cross-border points

Pay for work in Djibouti is in scope. Foreign posted staff: no social security agreement was found in the texts read.

## Two worked examples that recompute

Example 1: salary 200,000. Employer 15.7% = 31,400; employee 6% = 12,000.

```oa-check
name: CNSS on 200,000
inputs:
  pay: 200000
steps:
  - er: pay*0.157
  - ee: pay*0.06
  - total: er+ee
expected:
  total: 43400.00
```

Example 2, the decision: salary 1,000,000. Only pension runs past the 400,000 ceiling. Employer 400,000 x 11.7% + 1,000,000 x 4% = 86,800.

```oa-check
name: Employer cost above ceiling
inputs:
  pay: 1000000
  cap: 400000
steps:
  - capped: cap*0.117
  - pension: pay*0.04
  - er: capped+pension
expected:
  er: 86800.00
```

## Ask the client first

- Monthly pay and benefits.
- Business or domestic employer.
- Any pay above 400,000.
- Date CNSS affiliation was made.
- Foreign staff.

## Sources

| Source | URL | Read on |
|---|---|---|
| CNSS, Declaration et versement des cotisations: full page read | https://cnss.dj/declaration-et-versement-des-cotisations/ | 2026-11-01 |
| CNSS, Financement: rate table read | https://cnss.dj/financement-de-la-cnss/ | 2026-11-01 |
| CNSS, Penalites, sanctions et poursuites: full page read | https://cnss.dj/penalites-sanctions-et-poursuites/ | 2026-11-01 |
| CNSS, Affiliation employeur: full page read | https://cnss.dj/affiliation-employeur/ | 2026-11-01 |
| Arrete 2015-605/PR/MTRA on the CNSS ceiling: articles 1 and 2 read | https://www.journalofficiel.dj/texte-juridique/arrete-n2015-605-pr-mtra-portant-modification-du-plafonnement-des-remunerations-entrant-en-compte-pour-la-determination-de-lassiette-des-cotisations-dues-a-la-cnss-et-revalorisation-du-bareme/ | 2026-11-01 |
| Loi de finances 142/AN/21/8eme L, budget 2022: Titre II read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ | 2026-11-01 |
| Loi de finances 64/AN/23/9eme L, budget 2024: Titre II tax articles read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n-64-an-23-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2024/ | 2026-11-01 |

Not yet confirmed: The CGI on the official site is the 2011 edition. No consolidated 2026 code could be opened (impots.dj, dgi.dj and economie.gouv.dj did not answer), so each rule is the 2011 text plus the finance laws read; the finance laws found in the gazette for 2013 to 2026 were scanned for tax articles, the 2012 law was not, so an amendment made only there or in a law the gazette search missed would not show. The CNSS pages are undated (site copyright 2022) and no 2026 text confirms the rates. CNSS's own two pages differ on work injury: 1.2% (implied by 8.2% and the 21.7% total) against 1%. The 2015 ceiling is the latest found. Minimum wage not confirmed.

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
