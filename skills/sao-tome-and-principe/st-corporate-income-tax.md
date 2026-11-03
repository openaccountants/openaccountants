---
name: st-corporate-income-tax
description: "Use this skill for tax year 2026 working papers in Sao Tome and Principe (STP, jurisdiction ST). It covers IRC scope, general and simplified regimes, the 2026 minimum tax of 2 per 1000 of turnover with a Db 2,400 floor, returns by exempt bodies, billing software, the cash limit, incentives, and the older rate and withholding points that remain unverified. It says plainly which figures come from official texts and which remain unverified because the Finance Ministry site could not be opened. Trigger phrases: Sao Tome tax, STP tax, Direccao dos Impostos, dobras, Sao Tome e Principe imposto. It is general reference for working papers, not for filing without review by a qualified professional in the country."
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

# Sao Tome and Principe Corporate Income Tax v0.2

> **Sourced from the law, in part.** Tax year 2026. The Finance Ministry site refused access on 1 November 2026, so the tax codes themselves were not read. Rows marked unverified carry older figures that no official page has confirmed. No accountant has signed this version and it has had no independent review yet.

## Who this applies to

Companies, civil companies in commercial form, cooperatives, public enterprises and sports entities with a seat or effective management in STP, plus entities without one on income earned in STP ([Q3 2025 report](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN17-IIS.pdf)). The code is Law 16/2008 changed by Law 10/2009.

General regime (Group 1, art. 19): most taxpayers, including public companies, SA companies and non-residents with a permanent establishment. Simplified regime (Group 2, art. 20): small businesses without full accounts. Both come from a [Ministry presentation of 2025](https://www.britacom.org/zt/ThemeDay/Tenth/SEMINAR/202510/P020251021566751705880.pdf).

## Rates, bands and thresholds

| Item | Amount / treatment | Tax year | Official source |
|---|---|---|---|
| Minimum IRC | 2/1000 of turnover, at least Db 2,400 | 2026 | [debate of 11 Feb 2026, art. 8(10) as read and approved](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf) |
| Standard rate | unverified: older secondary source gave 25% | 2026 | unverified |
| New activity rate | unverified: older source gave 10% | 2026 | unverified |
| Agriculture, agro-industry, fisheries | unverified: older source gave 12.5% years 1 to 7, 20% years 8 to 9 | 2026 | unverified |
| International trading; local trading | unverified: older source gave 5%; and 12.5% first 5 years | 2026 | unverified |
| Withholding on dividends, interest, royalties | unverified: older source said about 15% on dividends; others unstated | 2026 | unverified |
| Billing software | Required from turnover of Db 1,000,000, or if organised accounts are required | 2026 | [2026 Budget art. 8(12)](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf) |
| Exempt bodies | Must still file annual returns if exempt under IRC code art. 16 | 2026 | [2026 Budget art. 8(14)](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf) |
| Cash limit | Db 10,000 or more barred with organised accounts; cost not deductible | 2026 | [2026 Budget art. 9](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf) |

## The base

Tax base: older point, unverified: accounting profit adjusted for tax; residents on worldwide profit, non-residents on STP income.

The floor changed often: Db 2,544 in the 2024 Budget, then back to Db 1,244 after a Constitutional Court ruling, per the Minister; the Bill for 2026 proposed Db 5,000 and the Assembly replaced it with Db 2,400 (Decree-Law 6/2016 art. 3(2)). Software cost is written off in one year (art. 8(13)).

Incentives rest on Decree-Law 15/2016 (Tax Benefits Code) and Decree-Law 19/2016 (Investment Code) per the Ministry presentation. Their rates were not read.

## Deadlines and filing

Older point, unverified: return within months of year end, commonly 31 March. Form and portal: unverified.

## Penalties and interest

Unverified. The Tax Directorate is the first instance for tax enforcement, per the Ministry presentation.

## Cross-border points

Non-residents with a permanent establishment fall in the general regime. Treaties: see [income tax](st-income-tax.md). Transfer pricing has no skill yet.

## Two worked examples that recompute

**Example 1.** Turnover of Db 5,000,000 with a tax loss.

```oa-check
name: Minimum IRC, large
inputs:
  turnover: 5000000
steps:
  - minimum: max(turnover * 0.002, 2400)
expected:
  minimum: 10000
```

**Example 2, edge.** Turnover of Db 500,000: 2/1000 gives Db 1,000, so the floor applies. Whether the floor sits on top of or instead of normal IRC depends on Decree-Law 6/2016, which was not read.

```oa-check
name: Minimum IRC, floor
inputs:
  turnover: 500000
steps:
  - minimum: max(turnover * 0.002, 2400)
expected:
  minimum: 2400
```

## Ask the client first

- Legal form and seat
- General or simplified regime
- Turnover and profit for the year
- Any incentive certificate
- Payments to non-residents

## Sources

| Source | URL | Read on |
|---|---|---|
| Assembly debate of 11 Feb 2026 on the Budget, art. 8 changes and final vote (pp. 315 to 321 read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf | 2026-11-01 |
| 2024 Budget text, art. on revenue, nos. 10 to 13 (only this part read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/3.a-sessao-legislativa/DAN25-IIS.pdf | 2026-11-01 |
| 2026 Budget Bill 51/XII/7.a/2025, art. 8 to 9 (only this part read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf | 2026-11-01 |
| Budget execution report Q3 2025, tax laws summary (pp. 384 to 385 read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN17-IIS.pdf | 2026-11-01 |

The Assembly of Sao Tome and Principe publishes its Diario on www2.camara.leg.br, hosted by the Brazilian Chamber of Deputies. The Ministry of Finance site (financas.gov.st) answered 403 by fetch and in a browser tab on 2026-11-01 and was not read.

Not yet confirmed: IRC code text; standard and incentive rates; withholding rates; filing date; penalties; Decree-Law 6/2016; Decree-Law 15/2016; published 2026 Budget law. Ministry presentation read 2026-11-01 at the link in Who this applies to.

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
