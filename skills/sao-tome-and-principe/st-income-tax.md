---
name: st-income-tax
description: "Use this skill for tax year 2026 working papers in Sao Tome and Principe (STP, jurisdiction ST). It covers IRS categories A to D, the 30% top band with its Db 45,048 deduction, the special IERS history, lottery exemption, the 2026 cash limit and software duty, and the older residence, band and filing points that remain unverified. It says plainly which figures come from official texts and which remain unverified because the Finance Ministry site could not be opened. Trigger phrases: Sao Tome tax, STP tax, Direccao dos Impostos, dobras, Sao Tome e Principe imposto. It is general reference for working papers, not for filing without review by a qualified professional in the country."
jurisdiction: ST
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.2
category: international
---

# Sao Tome and Principe Personal Income Tax v0.2

> **Sourced from the law, in part.** Tax year 2026. The Finance Ministry site refused access on 1 November 2026, so the tax codes themselves were not read. Rows marked unverified carry older figures that no official page has confirmed. No accountant has signed this version and it has had no independent review yet.

## Who this applies to

Individuals with income in categories A (employment and pensions), B (business and professional), C (capital) and D (capital gains) ([Q3 2025 execution report](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN17-IIS.pdf)). The code is Law 17/2008 as changed by Law 11/2009 ([2024 Budget no. 11](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/3.a-sessao-legislativa/DAN25-IIS.pdf)).

Older points, all unverified: residents taxed on worldwide income, non-residents on STP income, usually by withholding; residence after more than 183 days or a habitual home; employers withhold on wages.

## Rates, bands and thresholds

| Item | Amount / treatment | Tax year | Official source |
|---|---|---|---|
| Top band | 30% on income of Db 420,000 or more, less Db 45,048 | 2024, kept per Minister's statement 11 Feb 2026 | [2024 Budget no. 11](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/3.a-sessao-legislativa/DAN25-IIS.pdf); [debate p. 315](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf) |
| Lower bands and exempt band | unverified: older secondary sources gave 0%, 10%, 13%, 15%, 20%, 25% and a Db 11,700,000 exempt band, in conflict with each other | 2026 | unverified |
| Special tax, IERS | 20% on disposable income above Db 50,000 a month in 2024 and in the 2025 Bill. The Minister said on 11 Feb 2026 it was dropped in 2025. Not in the 2026 Bill part read | 2026 | [2025 Bill no. 18](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/5.a-sessao-legislativa/DAN15-IIS.pdf); [debate p. 316](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf) |
| Lottery prizes, category D | Exempt up to Db 25,000 | 2026 | [2026 Budget art. 8(18)](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf) |
| Cash limit | Taxpayers with organised accounts may not pay or receive Db 10,000 or more in cash; the expense is not deductible | 2026 | [2026 Budget art. 9](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf) |
| Personal and family allowances | unverified: amounts not read | 2026 | unverified |

## The base

Cash and benefits in kind are both taxed, in any currency, even if the income came from unlawful acts ([Q3 2025 report](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN17-IIS.pdf)). The table sits in art. 66 of the code. Whether Db 420,000 is a yearly or monthly figure is not stated in the Budget text, so confirm it in art. 66 before computing.

A Constitutional Court ruling on the 2024 measures was mentioned in the 11 February 2026 debate; the ruling was not read, and the Minister said the 2024 changes were reset. He also said the government "decided to keep" the 30% rate. Treat the 30% band as in force only after checking the gazette.

## Deadlines and filing

Older point, unverified: annual return by 31 March of the following year. No official text read gives this date. Form and portal: unverified.

## Penalties and interest

Rates of penalty: unverified. The Tax Process Code and General Tax Code (Law 6/2007) apply; neither was read.

## Cross-border points

A Cabo Verde tax treaty went to the Assembly in 2021 as Resolution Bill 44/XI/5.a/2021; whether it is in force, and all treaty rates, are unverified. See [corporate income tax](st-corporate-income-tax.md) for the withholding gaps.

## Two worked examples that recompute

**Example 1, top band.** Income of Db 500,000 in the band period.

```oa-check
name: Top band
inputs:
  income: 500000
steps:
  - tax: income * 0.30 - 45048
expected:
  tax: 104952
```

**Example 2, edge of the band and decision on cash.** Income of exactly Db 420,000 is inside the band ("equal or above"). A Db 9,000 cash expense stays deductible; a split payment for one deal is added together under art. 9(3).

```oa-check
name: Band edge
inputs:
  income: 420000
steps:
  - tax: income * 0.30 - 45048
expected:
  tax: 80952
```

## Ask the client first

- Resident or not, and days in the country
- Income by category A to D
- Period of the income, month or year
- Whether organised accounts are kept
- Foreign tax paid

## Sources

| Source | URL | Read on |
|---|---|---|
| 2024 Budget text, art. on revenue, nos. 10 to 13 (only this part read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/3.a-sessao-legislativa/DAN25-IIS.pdf | 2026-11-01 |
| 2025 Budget Bill, revenue article nos. 12 to 19 (only this part read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/5.a-sessao-legislativa/DAN15-IIS.pdf | 2026-11-01 |
| 2026 Budget Bill 51/XII/7.a/2025, art. 8 to 9 (only this part read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf | 2026-11-01 |
| Assembly debate of 11 Feb 2026 on the Budget, art. 8 changes and final vote (pp. 315 to 321 read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf | 2026-11-01 |
| Budget execution report Q3 2025, tax laws summary (pp. 384 to 385 read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN17-IIS.pdf | 2026-11-01 |

The Assembly of Sao Tome and Principe publishes its Diario on www2.camara.leg.br, hosted by the Brazilian Chamber of Deputies. The Ministry of Finance site (financas.gov.st) answered 403 by fetch and in a browser tab on 2026-11-01 and was not read.

Not yet confirmed: IRS code text and full band table; whether the 30% band survives the Constitutional Court ruling; band period; allowances; filing date; residence test; withholding rates; penalties; treaties.

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
