---
name: om-payroll-social
description: "Payroll and social contributions for Oman, tax year 2026: Social Protection Fund rates by branch and date, the OMR 3,000 ceiling, payment by the 15th, non-Omani workers, late charges, from the law and the Fund."
version: 1.1
jurisdiction: OM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oman Payroll & Social Contributions

## Who this applies to

Employers of Omani workers in Oman, Omani self-employed people, and employers of non-Omani workers for the branches that reach them. The Social Protection Fund runs the scheme under the Social Protection Law (RD 52/2023), in force from 1 January 2024 with staged branches (decree art. VI). No income tax is withheld from pay in 2026; see [income tax](om-income-tax.md).

## Rates, bands and thresholds

| Branch | Worker | Employer | Since | Official URL |
|---|---|---|---|---|
| Old age, disability and death | 7.5% | 11% | 1 Jan 2024 | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ |
| Work injury and occupational disease | 0% | 1% | 1 Jan 2024 | same |
| Employment security | 0.5% | 0.5% | 1 Jan 2024 | same |
| Sick and other leave | 0% | 1% | 1 Jul 2025 | same |
| Maternity leave | 0% | 1% | 1 Jul 2024 | same |
| Total | 8% | 14.5% | | same |

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Wage ceiling, old age and work injury branches | OMR 3,000 a month (art. 52) | 2026 | https://decree.om/2023/rd20230052/ |
| Non-Omani savings system | 9% of monthly basic wage (art. 139(1)), from a date set by the Board, no later than 3 years from 19 July 2023 (decree art. VI) | 2026 | same |
| Late or unpaid contributions | Additional 5.5% a year (art. 155) | 2026 | same |
| Income tax withholding on pay | None in 2026; starts 2028 | 2026 | https://qanoon.om/p/2025/rd2025056/ |

Art. 52 names only two branches for the ceiling, so the other three branches run on the full wage in the examples below.

## The base

Contributions are calculated on the monthly wage, on a daily basis (arts 70, 90, 116, 123, 128). The regulation defines exempt categories and surplus handling (art. 52).

## Deadlines and filing

Contributions are paid within the first 15 days of the month after the one they cover. The employer pays both shares and deducts the worker's share from the wage (art. 58, https://decree.om/2023/rd20230052/). Registration and upload screens are on the Fund's site, which refused most connections, so no portal how-to is given here.

## Penalties and interest

An employer that fails to register workers, understates wages, or pays late owes an additional 5.5% a year on the amounts due (art. 155), unless the Board's controls excuse it (https://decree.om/2023/rd20230052/).

## Cross-border points

The old age branch is compulsory for Omanis working in Oman, and covers Omanis under the GCC extension systems (art. 68). Non-Omani workers: the work injury branch reaches them from 3 years after issue, so from 19 July 2026, in the categories the Board decides (decree art. VI, art. 87). The sick leave branch reaches them by Board decision (art. 121). The savings system is compulsory for them at the art. 139(1) amount (art. 136); service before the start date stays under the Labour Law end-of-service rules (art. 138). Check the Board's decision before charging any of these.

## Two worked examples that recompute

**1. Omani worker on OMR 1,000 a month.** Employer pays OMR 145; worker pays OMR 80.

```oa-check
name: Omani wage 1000
inputs:
  wage: 1000
steps:
  - employer: wage * (0.11 + 0.01 + 0.005 + 0.01 + 0.01)
  - worker: wage * (0.075 + 0.005)
expected:
  employer: 145
  worker: 80
```

**2. Omani worker on OMR 4,000, above the ceiling.** The ceiling cuts the old age and injury shares. Employer pays OMR 460, worker OMR 245.

```oa-check
name: Omani wage 4000 with ceiling
inputs:
  wage: 4000
  ceiling: 3000
steps:
  - capped: min(wage, ceiling)
  - employer: capped * 0.12 + wage * 0.025
  - worker: capped * 0.075 + wage * 0.005
expected:
  employer: 460
  worker: 245
```

## Ask the client first

- Omani or non-Omani, and any GCC national?
- Monthly wage, and what it is made of?
- Contract type (temporary, training, part-time)?
- Date of joining?
- Any arrears or unregistered workers?

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Protection Fund, FAQ on contribution rates (whole page read) | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ | 2026-11-01 |
| Social Protection Law, RD 52/2023, Decree.om translation of the gazette text, a private publisher (decree arts V and VI; law arts 52, 58, 68, 70, 87, 90, 116, 121, 123, 128, 136, 139, and 155 read) | https://decree.om/2023/rd20230052/ | 2026-11-01 |
| Personal Income Tax Law, RD 56/2025, Arabic gazette text (issue 1602) on Qanoon.om, a private publisher (arts 1 to 61 read). The Tax Authority page for the law text was not found | https://qanoon.om/p/2025/rd2025056/ | 2026-11-01 |

Not yet confirmed: whether the Board has set the start date of the 9% savings system and its current status; the Board decision on work injury and sick leave for non-Omani workers (the old skill said 1% for all expatriates, not confirmed); whether a ceiling applies to employment security, sick leave and maternity branches; the wage definition in the regulation; Fund portal steps; GCC national contribution rates. The old skill’s employer total of 12.5% omitted the two leave branches and is replaced.

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
