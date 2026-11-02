---
name: et-corporate-income-tax
description: "Ethiopia corporate income tax for tax year 2026: rates, minimum alternative tax, undistributed profit, withholding and filing, from the gazetted law."
version: 0.2
jurisdiction: ET
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ethiopia Corporate Income Tax

## Who this applies to

Bodies, all Category A whatever their turnover (art. 3). Limited liability partnerships and registered collective investment funds pay no corporate tax but withhold on distributions (art. 19(3)). Income from 8 July 2025 follows Proc. 1395/2025 (art. 4).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate; Proc. 1395/2025 left art. 19(1) of Proc. 979/2016 unchanged | unverified 30% | 2026 | unverified |
| Minimum alternative tax: on turnover; banks on net banking income; insurers on gross premium; price-regulated bodies on commission (art. 23(2)) | 2.5% | 2026 | https://www.hopr.gov.et/admin/Files/2026/4/8/5fc57d68-d0f6-4bf1-91b4-5b23abd0df72%E1%8C%88%E1%89%A2%20%E1%8C%8D%E1%89%A5%E1%88%AD%20%201395.pdf |
| Credit for minimum tax (art. 23(5)) | up to 5 years | 2026 | same |
| Undistributed profit not reinvested within 12 months of year end (art. 64) | 15% | 2026 | same |
| Repatriated profit of a permanent establishment (art. 65) | 15% | 2026 | same |
| Dividend (art. 57); group distributions and dividends on a 12.5% controlling holding are out (arts 57(3), 68(1)(t)) | 15% | 2026 | same |
| Interest (art. 58) | 10% | 2026 | same |
| Royalty: art and culture / other (art. 56) | 5% / 10% | 2026 | same |
| Withholding on goods over ETB 20,000 and services of ETB 10,000 (art. 97(1)); 30% without TIN and licence | 3% | 2026 | same |
| Mining rate, sector rule | unverified 25% | 2026 | unverified |

## The base

Net business profit as adjusted for tax. Minimum tax is measured after incentives (art. 23(7)). Liquidation and debt restructuring are out (art. 23(6)). Investment incentives stand only under the Council of Ministers regulations (art. 105). Payments over ETB 50,000 outside bank channels are not deductible (art. 29(1)(o)).

## Deadlines and filing

1. File within 4 months of year end (Proc. 979/2016 art. 83(4)).
2. Pay the balance at filing, net of advances (art. 89(2)(b)).
3. Pay 25% of last year's tax within 30 working days of each quarter end (art. 89(2)(a)). A new taxpayer pays at filing in its first year (art. 89(5)).
4. Overpaid advances are refunded (art. 89(2)(c)).
5. Forms are on the [Ministry page](https://www.mor.gov.et/forms), with balance sheet and annexes.

## Penalties and interest

See [payroll](ethiopia-payroll.md#penalties-and-interest). Assessment limits: 5 years, 10 with tax fraud (Proc. 983/2016 art. 28 as amended by 1434/2026). Appeals to the Commission: 30 days (art. 105). Conciliation and conditional tax clearance are new (arts 61 to 71, 72(6)).

## Cross-border points

Permanent establishment at over 91 days (art. 4). Non-resident withholding: insurance premium 15%, royalty 10%, dividend 15%, interest 10%, management or technical fee 15% (art. 52(2)). Digital service tax at up to 5% (art. 53). Banks need tax clearance before a foreign investor repatriates (Proc. 1434/2026, art. 72(11)). Transfer pricing has a Ministry directive, not yet covered by a skill.

## Two worked examples that recompute

Simple case: profit ETB 100,000, turnover ETB 10,000,000, so minimum tax applies at the 30% rate marked unverified.

```oa-check
name: Minimum alternative tax
inputs:
  p: 100000
  t: 10000000
steps:
  - normal: p * 0.30
  - minimum: t * 0.025
  - payable: max(normal, minimum)
expected:
  normal: 30000.00
  minimum: 250000.00
  payable: 250000.00
```

Decision: after-tax profit of ETB 3,500,000, kept idle or put into capital within 12 months. Kept idle costs 525,000; capitalised costs nil.

```oa-check
name: Keep or capitalise
inputs:
  p: 3500000
steps:
  - idle: p * 0.15
  - capitalised: 0
  - saving: idle - capitalised
expected:
  idle: 525000.00
  capitalised: 0.00
  saving: 525000.00
```

## Ask the client first

- Turnover and profit for the year?
- Bank, insurer or price-regulated?
- Any incentive, liquidation or restructuring?
- Dividends paid or capital increased within 12 months of year end?
- Foreign owners or a permanent establishment?

## Sources

| Source | URL | Read on | What was read |
|---|---|---|---|
| Income Tax (Amendment) Proclamation 1395/2025, Federal Negarit Gazette 31st Year No. 64 | https://www.hopr.gov.et/admin/Files/2026/4/8/5fc57d68-d0f6-4bf1-91b4-5b23abd0df72%E1%8C%88%E1%89%A2%20%E1%8C%8D%E1%89%A5%E1%88%AD%20%201395.pdf | 2026-11-01 | Whole text read (English column) |
| Federal Income Tax Proclamation 979/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/979.pdf | 2026-11-01 | Declaration, payment, withholding and exemption articles read in Amharic; article numbers are those before the 1395/2025 renumbering |
| Federal Tax Administration Proclamation 983/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/983.pdf | 2026-11-01 | Penalty articles and art. 37 read in Amharic |
| Tax Administration (Amendment) Proclamation 1434/2026, Federal Negarit Gazette 32nd Year No. 48, 30 July 2026, listed by the Ministry of Revenues | https://www.mor.gov.et/domestic-law-proclamation | 2026-11-01 | Whole text read; adds 17 to the penalty article numbers of 983/2016 |
| Ministry of Revenues forms list | https://www.mor.gov.et/forms | 2026-11-01 | Titles of the published forms read; the form boxes were not read |

Not yet confirmed: the 30% rate and the mining rate: the rate article of Proc. 979/2016 was not read, so both stay marked unverified; the Council of Ministers income tax regulation that sets the digital service tax rate (capped at 5%) was not found; the e-tax portal steps and the box numbers on the Ministry forms were not read, so no box numbers are given as law; the Ministry directives on undistributed profit and advance tax were not read.


> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
