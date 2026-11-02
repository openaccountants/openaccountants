---
name: dj-income-tax
description: "Use for Djibouti personal income tax for tax year 2026: ITS salary tax bands 2% to 45%, the 50,000 exemption, withholding by the 10th, capital gains and non-residents."
version: 2.0
jurisdiction: DJ
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Djibouti Personal Income Tax

## Who this applies to

Employees and their employers: ITS covers all pay for activity in Djibouti, and since 1 January 2009 staff of free-zone firms. Exempt: diplomats in post, retirement pensions (art. 4), family allowances, refunded expenses on receipts (art. 5). Self-employed profit falls under the impot sur les benefices professionnels, see dj-corporate-income-tax. There is no separate general income tax return for salary in the texts read.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Band 1 | 2% | Monthly fraction below 30,000 (CGI art. 15 as rewritten by LF 2022 art. 7) | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ |
| Band 2 | 12% | 30,000 to 50,000 | same |
| Band 3 | 15% | 50,001 to 150,000 | same |
| Band 4 | 22% | 150,001 to 300,000 | same |
| Band 5 | 25% | 300,001 to 600,000 | same |
| Band 6 | 30% | 600,001 to 1,000,000 | same |
| Band 7 | 35% | 1,000,001 to 2,000,000 | same |
| Band 8 | 45% | Above 2,000,000 | same |
| Low-pay exemption | 50,000 a month | Art. 4 as completed 2016; not repealed in any law read, though the 2022 scale dropped the words "above 50,000" and still starts at 30,000. If salary is at or under 50,000, no ITS. Above it, apply the scale from the first franc | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n120-an-15-7eme-l-portant-budget-initial-de-letat-pour-lexercice-2016/ |
| Short engagement | 15% flat | Under one calendar month, on the whole pay above 50,000 (arts. 16, LF 2016 art. 8) | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n120-an-15-7eme-l-portant-budget-initial-de-letat-pour-lexercice-2016/ |
| Rounding | Fraction under 5,000 ignored | Art. 14 | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Company car benefit | 40,000 a month | Per vehicle and person (art. 17) | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Severance | 1,500,000 relief | LF 2022 art. 6, art. 5 al. 5 | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ |
| Capital gains on property and shares | 10% first sale; 15% built or unbuilt property second sale | Art. 67 b, LF 2022 art. 16; second-sale rate from 2020 rectified law art. 6 | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ |

## The base

Base: monthly pay including benefits in kind (art. 15), less pension withholdings and CNSS withholdings (art. 6). The bands are marginal: the law taxes each "fraction". Tax is set monthly (art. 9).

## Deadlines and filing

| Item | Date or rule | Source |
|---|---|---|
| ITS payment | Before the 10th of the next month, to the Tresorerie generale (art. 287, LF 2024 art. 23). The older ministry page says the 15th: the law wins | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n-64-an-23-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2024/ |

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Withholding not made | Fine equal to the tax not withheld, on top of the tax (art. 249) | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Late payment | 5% surcharge plus 0.5% interest per month; no 5% on audit assessments (art. 247) | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf |
| Late or missing return | Interest 5% (art. 246 as amended 2021; the earlier text was 0.5% per month) plus 10% if filed within 10 days of formal notice, 40% after that or never | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n111-an-20-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2021/ |

## Cross-border points

Pay for activity carried out in Djibouti is taxed; the law taxes "activity in the country". Foreign employee on a Djibouti posting: same scale. Agreements on French forces and teachers sit in the CGI annexes. Treaty relief: check whether a convention applies.

## Two worked examples that recompute

Example 1: salary 200,000. Employee CNSS 6% = 12,000 (art. 6). Taxable 188,000, rounded down to 185,000 (art. 14). ITS 25,700.

```oa-check
name: ITS on 200,000 a month
inputs:
  gross: 200000
steps:
  - cnss: gross * 0.06
  - base: floor((gross - cnss) / 5000) * 5000
  - tax: 30000*0.02 + 20000*0.12 + 100000*0.15 + (base-150000)*0.22
expected:
  tax: 25700.00
```

Example 2, the decision: is a 1,500,000 salary hit by the CNSS ceiling? Yes for care only: 2% on 400,000 = 8,000, pension 4% uncapped = 60,000. Taxable 1,432,000, rounded to 1,430,000. ITS 396,500.

```oa-check
name: ITS on 1,500,000 a month
inputs:
  gross: 1500000
steps:
  - cnss: 400000*0.02 + gross*0.04
  - base: floor((gross - cnss) / 5000) * 5000
  - tax: 600 + 2400 + 15000 + 33000 + 75000 + 120000 + (base-1000000)*0.35
expected:
  tax: 396500.00
```

## Ask the client first

- Monthly gross and benefits in kind.
- Is the job under one month?
- Is the person a diplomat, pensioner or free-zone employee?
- Employer CNSS registration.
- Any severance?
- Foreign resident or posted worker?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code general des impots, edition updated to the 2011 finance law, Ministry of Finance: articles cited read in the PDF text; later changes taken from the finance laws listed here | https://www.ministere-finances.dj/TVA/CGI%20%202010.pdf | 2026-11-01 |
| Loi de finances 142/AN/21/8eme L, budget 2022: Titre II read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n142-an-21-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2022/ | 2026-11-01 |
| Loi de finances 111/AN/20/8eme L, budget 2021: articles 6 to 20 read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n111-an-20-8eme-l-portant-budget-initial-de-letat-pour-lexercice-2021/ | 2026-11-01 |
| Loi de finances 120/AN/15/7eme L, budget 2016: articles 6 to 16 read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n120-an-15-7eme-l-portant-budget-initial-de-letat-pour-lexercice-2016/ | 2026-11-01 |
| Loi de finances 64/AN/23/9eme L, budget 2024: Titre II tax articles read | https://www.journalofficiel.dj/texte-juridique/loi-de-finances-n-64-an-23-9eme-l-portant-budget-initial-de-letat-pour-lexercice-2024/ | 2026-11-01 |
| Ministry of Finance ITS page (copyright 2010): scope and exemptions read; its 5-band scale is superseded | https://www.ministere-finances.dj/ITS%20IMPOTS%20DIRECT.html | 2026-11-01 |

Not yet confirmed: The CGI on the official site is the 2011 edition. No consolidated 2026 code could be opened (impots.dj, dgi.dj and economie.gouv.dj did not answer), so each rule is the 2011 text plus the finance laws read; the finance laws found in the gazette for 2013 to 2026 were scanned for tax articles, the 2012 law was not, so an amendment made only there or in a law the gazette search missed would not show. Whether the 50,000 exemption survives the 2022 rewrite is read from the texts, not stated by an authority. The old skill's residence test and treaty position remain unconfirmed; no Djibouti treaty list was opened. The older 5-band scale on the ministry page (to 30%) is out of date.

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
