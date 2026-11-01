---
name: st-tax-overview
description: "Use this skill for tax year 2026 working papers in Sao Tome and Principe (STP, jurisdiction ST). It maps the taxes, the authority, the currency, the main laws, the 2026 Budget changes, and what could and could not be verified, then points to each skill in the pack. It says plainly which figures come from official texts and which remain unverified because the Finance Ministry site could not be opened. Trigger phrases: Sao Tome tax, STP tax, Direccao dos Impostos, dobras, Sao Tome e Principe imposto. It is general reference for working papers, not for filing without review by a qualified professional in the country."
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

# Sao Tome and Principe Tax Overview v0.2

> **Sourced from the law, in part.** Tax year 2026. The Finance Ministry site refused access on 1 November 2026, so the tax codes themselves were not read. Rows marked unverified carry older figures that no official page has confirmed. No accountant has signed this version and it has had no independent review yet.

## Who this applies to

Anyone needing a first map of the STP system. The Direccao dos Impostos and the Autoridade Geral Aduaneira work under the Ministry of Economy and Finance ([Ministry presentation](https://www.britacom.org/zt/ThemeDay/Tenth/SEMINAR/202510/P020251021566751705880.pdf)). General Tax Code: Law 6/2007. Older points: calendar tax year; currency dobra (STN, Db) pegged to the euro; both unverified on a 2026 official page.

## Rates, bands and thresholds

| Item | Amount / treatment | Tax year | Official source |
|---|---|---|---|
| VAT | 15%, see [VAT](st-vat-gst.md) | 2026 | [VAT Code art. 16](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xi-legislatura-22-11-2018/ii-serie-a/2.a-sessao/DAN30-IIS.pdf) |
| Minimum company tax | 2/1000, floor Db 2,400 | 2026 | [debate 11 Feb 2026](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf) |
| Top personal band | 30%, status to confirm; see [income tax](st-income-tax.md) | 2026 | [2024 Budget no. 11](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/3.a-sessao-legislativa/DAN25-IIS.pdf) |
| Company tax rate | unverified: older source 25% | 2026 | unverified |
| INSS | 6% and 4% in the official text; 7% and 5% reported for 2025; see [payroll](st-payroll-social.md) | 2026 | [REPSO art. 101(3)](https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf) |
| Property, gifts, transfer, vehicles | Urban property tax Law 6/2008; inheritance and gifts Law 8/2007; SISA Law 5/2007; vehicles Decree-Law 13/93. Rates not read | 2026 | [Q3 2025 report](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN17-IIS.pdf) |

## The base

See each skill. The government holds a one-year power from the 2026 Budget to amend the customs tariff and the VAT, excise and IRS codes by decree ([art. 8(7)](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf)). Any such decree overrides figures here.

## Deadlines and filing

Older point, unverified: personal returns by 31 March. VAT monthly, by month end; INSS by the 10th.

## Penalties and interest

See each skill.

## Cross-border points

A new environmental import tax, IEI, appears in the 2026 Bill, art. 8 ([2026 Budget Bill 51/XII/7.a/2025](https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf)). Its rates were not read.

## Two worked examples that recompute

**Example 1.** A VAT line of Db 200,000 sales.

```oa-check
name: VAT line
inputs:
  sales: 200000
steps:
  - vat: sales * 0.15
expected:
  vat: 30000
```

**Example 2, decision on registration.** Prior-year turnover of Db 1,000,000 is not below the limit, so normal VAT applies; at Db 999,999 the exemption regime applies.

```oa-check
name: Limit gap
inputs:
  limit: 1000000
  turnover: 999999
steps:
  - gap: limit - turnover
expected:
  gap: 1
```

## Ask the client first

- Person or company
- Resident or not
- Turnover
- Staff
- Activity

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Code final text, Bill 05/XI/2.a/2019, arts. 3, 16, 27 to 30, 37, 44, 48 to 50 (later amendments not read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xi-legislatura-22-11-2018/ii-serie-a/2.a-sessao/DAN30-IIS.pdf | 2026-11-01 |
| Assembly debate of 11 Feb 2026 on the Budget, art. 8 changes and final vote (pp. 315 to 321 read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/i-serie/7.a-sessao-legislativa/DAN13-IS.pdf | 2026-11-01 |
| 2024 Budget text, art. on revenue, nos. 10 to 13 (only this part read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/3.a-sessao-legislativa/DAN25-IIS.pdf | 2026-11-01 |
| 2026 Budget Bill 51/XII/7.a/2025, art. 8 to 9 (only this part read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN14-IIS.pdf | 2026-11-01 |
| Decree-Law 19/2022 consolidated text, arts. 97 to 105, 131 | https://inss.gov.st/assets/Leis/Lei_n_19_2022.pdf | 2026-11-01 |
| Budget execution report Q3 2025, tax laws summary (pp. 384 to 385 read) | https://www2.camara.leg.br/saotomeeprincipe/diarios-da-an/xii-legislatura-8-11-22-a-8-11-26/ii-serie/7.a-sessao-legislativa-1/DAN17-IIS.pdf | 2026-11-01 |

The Assembly of Sao Tome and Principe publishes its Diario on www2.camara.leg.br, hosted by the Brazilian Chamber of Deputies. The Ministry of Finance site (financas.gov.st) answered 403 by fetch and in a browser tab on 2026-11-01 and was not read.

Not yet confirmed: All rows marked unverified; the Finance Ministry publications; Tax Directorate how-to pages; the euro peg in 2026.

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
