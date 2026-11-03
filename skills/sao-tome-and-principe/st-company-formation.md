---
name: st-company-formation
description: "Use this skill for tax year 2026 working papers in Sao Tome and Principe (STP, jurisdiction ST). It covers Lda, SA and sole trader choices, Law 17/2009 minimum capital, single-member companies, commercial registry law, tax and social registration after formation, annual compliance, and the steps that remain unverified. It says plainly which figures come from official texts and which remain unverified because the Finance Ministry site could not be opened. Trigger phrases: Sao Tome tax, STP tax, Direccao dos Impostos, dobras, Sao Tome e Principe imposto. It is general reference for working papers, not for filing without review by a qualified professional in the country."
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

# Sao Tome and Principe Company Formation v0.2

> **Sourced from the law, in part.** Tax year 2026. The Finance Ministry site refused access on 1 November 2026, so the tax codes themselves were not read. Rows marked unverified carry older figures that no official page has confirmed. No accountant has signed this version and it has had no independent review yet.

## Who this applies to

Founders choosing an entity in STP. Older points, unverified: Lda (quotas, liability limited to subscribed quota), SA (shares, larger ventures), sole trader (unlimited liability), company law of Portuguese origin. Decree-Law 43843 of 5 August 1961 regulates quota companies ([Law 17/2009](https://dgrn.gov.st/leis/Lei/Altera_Lei_Socieades_quotas.pdf)).

## Rates, bands and thresholds

| Item | Amount / treatment | Tax year | Official source |
|---|---|---|---|
| Lda minimum capital | Dbs. 150,000,000 in the text of 2009; old dobras, before the later re-denomination. Current-dobra value unverified | 2009, no later change seen | [Law 17/2009](https://dgrn.gov.st/leis/Lei/Altera_Lei_Socieades_quotas.pdf) |
| Minimum members | Capital equals the sum of partners' quotas, except in single-member companies, so single-member companies exist. Older two-member point: unverified | 2026 | [Law 17/2009](https://dgrn.gov.st/leis/Lei/Altera_Lei_Socieades_quotas.pdf) |
| EUR equivalent | unverified: older source said about EUR 6,000. The 2009 gazette set a buying rate of 24,500 dobras per euro | 2026 | [same gazette](https://dgrn.gov.st/leis/Lei/Altera_Lei_Socieades_quotas.pdf) |
| Timeline | unverified: older World Bank source, several days to weeks | 2026 | unverified |

## The base

Registry: Commercial Registry Code, Law 13/2018 ([gazette](https://dgrn.gov.st/leis/Lei/Codigos_Registo_Predial_Comercial.pdf)). Licensing rules sit in the [DGRN law list](https://dgrn.gov.st/Legislacao.php). One-stop Guiche Unico route: unverified; guicheunico.st did not answer.

## Deadlines and filing

Older sequence, unverified: name, articles, capital deposit, registry, tax number, INSS, licences. Then file a VAT start declaration 15 days before activity ([VAT](st-vat-gst.md)) and register with INSS ([payroll](st-payroll-social.md)). Annual accounts and monthly filings continue whatever the activity level (older point, unverified as to accounts).

## Penalties and interest

Unverified.

## Cross-border points

Foreign founders: exchange and investment rules are in Decree-Law 19/2016, not read.

## Two worked examples that recompute

**Example 1.** Two partners with equal quotas on the 2009 figure.

```oa-check
name: Equal quotas
inputs:
  capital: 150000000
steps:
  - each: capital / 2
expected:
  each: 75000000
```

**Example 2, decision.** A sole founder compares a single-member company with a sole trader; a company adds minimum IRC of at least Db 2,400 a year ([IRC](st-corporate-income-tax.md)). At turnover of Db 2,000,000 the minimum is Db 4,000.

```oa-check
name: Company minimum
inputs:
  turnover: 2000000
steps:
  - minimum: max(turnover * 0.002, 2400)
expected:
  minimum: 4000
```

## Ask the client first

- Number of founders
- Activity and licence
- Foreign ownership
- Planned capital
- Staff from day one

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 17/2009, private company capital (Gazette 90, 31 Dec 2009) | https://dgrn.gov.st/leis/Lei/Altera_Lei_Socieades_quotas.pdf | 2026-11-01 |
| Law 13/2018, Commercial Registry Code (sumario only read) | https://dgrn.gov.st/leis/Lei/Codigos_Registo_Predial_Comercial.pdf | 2026-11-01 |
| Decree-Law 11/2011 gazette, on the commercial licensing file (first page only read) | https://dgrn.gov.st/leis/Lei/actividade_comercial_seu_licenciamento.pdf | 2026-11-01 |

The Assembly of Sao Tome and Principe publishes its Diario on www2.camara.leg.br, hosted by the Brazilian Chamber of Deputies. The Ministry of Finance site (financas.gov.st) answered 403 by fetch and in a browser tab on 2026-11-01 and was not read.

Not yet confirmed: Commercial code text; capital in current dobras; registry fees; one-stop steps; timeline; SA capital.

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
