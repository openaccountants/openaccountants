---
name: zw-corporate-income-tax
description: >
  Zimbabwe corporate income tax, tax year 2026: 25% plus 3% AIDS levy, reduced rates for exporters, mining, licensed investors and special economic zones, BKPO services at 15%, the domestic minimum top-up tax, quarterly payment dates, the ITF12C return, the 50:50 currency rule, new permanent establishment tests and new credits and deductions from Finance Act 7 of 2025. Use for questions on company tax in Zimbabwe, QPD dates, ZIMRA corporate rates or withholding tax on dividends.
version: 1.0
jurisdiction: ZW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zimbabwe corporate income tax

## Who this applies to

Companies, trusts and pension funds with income from a Zimbabwe source or deemed source. Multinational groups with EUR 750 million revenue in two of the last four years are also in the top-up tax.

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Company or trust | 25% | 2026 | s.14(2c) | https://www.zimra.co.zw/domestic-taxes/corporate/tax-rates |
| AIDS levy | 3% of tax | 2026 | Effective 25.75% | same |
| Pension fund, trade or investment | 15% | 2026 | s.14(2)d | same |
| Licensed investor | 0%, then 25% | 2026 | First five years, then after | same |
| Special mining lease | 15% | 2026 | s.14(2)(f) | same |
| Mining company or trust | 25% | 2026 | s.14(2)g | same |
| BOOT or BOT arrangement | 0%, then 15% | 2026 | First five years, second five | same |
| Industrial park developer | 0%, then 25% | 2026 | Before, after fifth year | same |
| Tourist facility in approved zone | 0%, then 25% | 2026 | Before, after fifth year | same |
| Manufacturer exporting 30% to 41% | 20% | 2026 | s.14(3)(a) | same |
| Manufacturer exporting 41% to 51% | 17.5% | 2026 | s.14(3)(b) | same |
| Manufacturer exporting more than 51% | 15% | 2026 | s.14(3)(c) | same |
| Dividends from a foreign company | 20% | 2026 | s.14(5) | same |
| Special economic zone | 0%, then 15% | 2026 | First five years, then after | same |
| BKPO service | 15% | 2026 | On that income; Act ss.5, 6 | https://www.veritaszim.net/sites/veritas_d/files/Finance%20Act%2C%20Act%20No.%207%20of%202025.pdf |
| Top-up tax | to 15% | 2026 | Combined effective rate below 15% | same |
| Levy on coal, lithium, granite, stone | 3% | 2026 | Gross value | same |
| Gaming operators tax | 20% | 2026 | Gross monthly takings, final tax | same |
| Sports credit | up to USD 10,000 | 2026 | Registered, tax compliant, NSSA compliant | same |
| Special capital gains tax | 20% | 2026 | Offshore transfer of land-holding entity interests | same |
| Dividend WHT, ZSE, VFEX, unlisted | unverified: 10%, 5%, 15% | 2026 | Earlier version, not reconfirmed | unverified |
| Royalties and interest to non-residents | unverified: 15% | 2026 | Earlier version, not reconfirmed | unverified |

## The base

Taxable income is gross income from a Zimbabwe source less exemptions and allowed deductions. New from 2026: IMTT is deductible for a registered, tax-cleared taxpayer; film capital allowances doubled; BKPO capital expenditure 100% in the first year; public sports facilities 150%. Digital services withholding and export tax are not deductible (Act ss.16, 17). Mineral exports may be priced by the Quoted Price Method (Act s.31).

## Deadlines and filing

QPD returns: 10% by 20 March, 25% by 20 June, 30% by 20 September, 35% by 15 December, with the fourth payment by 20 December (Public Notice 58 of 2026). The first three payment days are not stated in that notice; the earlier version gave the 25th (unverified). Other accounting years follow dates the Commissioner approves. The ITF12C goes through mytaxselfservice.zimra.co.zw four months after year end, with financial statements attached.

1. Log in and select your TIN.
2. Tax Return Management, Pending Returns.
3. Choose the Provisional Return or Self-Assessment Return - Business. Enter the sports credit under Tax Credits if you qualify.
4. Submit, then pay with TIN and name. If over 50% of estimated income is foreign currency, use 50:50 for the estimate.

## Penalties and interest

Unregistered businesses in listed sectors pay deemed QPDs, from USD 5,000 for lodges to USD 15,000 for car dealers and hardware. No return evidence and no tax clearance means 30% withholding on invoices. Other penalty rates were not opened.

## Cross-border points

A fixed place for 90 days in 12 months, services through staff over 90 days, or a building site from its start is a permanent establishment (Act s.18). The USD 500,000 limit in s.12A(2) is gone (Act s.14). Treaty relief must be claimed; rates were not read.

## Two worked examples that recompute

Profit USD 100,000: tax 25,000, levy 750, total 25,750.

```oa-check
name: Standard company
inputs:
  profit: 100000
steps:
  - total: profit * 0.25 * 1.03
expected:
  total: 25750.00
```

Decision: a manufacturer on USD 100,000 deciding if exporting over 51% matters: 15% gives 15,450 against 25,750, a saving of 10,300.

```oa-check
name: Exporter rate against standard
inputs:
  profit: 100000
steps:
  - saving: profit * (0.25 - 0.15) * 1.03
expected:
  saving: 10300.00
```

## Ask the client first

1. Sector and any investment licence or zone.
2. Share of output exported.
3. Currency share of income.
4. Accounting year end.
5. Group revenue, for top-up tax.

## Sources

| Source | URL | Read on |
|---|---|---|
| Finance Act No. 7 of 2025 (Veritas copy of the Government Printer text), whole Act | https://www.veritaszim.net/sites/veritas_d/files/Finance%20Act%2C%20Act%20No.%207%20of%202025.pdf | 2026-11-01 |
| ZIMRA Public Notices 5, 7, 11, 49, 50, 58, 61 of 2026 (list page; each PDF opened) | https://www.zimra.co.zw/public-notices | 2026-11-01 |
| ZIMRA Tax Rates page, whole table; undated | https://www.zimra.co.zw/domestic-taxes/corporate/tax-rates | 2026-11-01 |
| ZIMRA Self Assessment Return Notes | https://www.zimra.co.zw/domestic-taxes/corporate/self-assessment-return-notes | 2026-11-01 |

Not yet confirmed: payment days of QPDs 1 to 3; whether the ZIMRA rates table reflects all 2026 changes; withholding rates; the 2026 start date of non-residents' tax on interest; mining rate notes; treaty rates; penalties and interest; approved SEZ terms beyond the table.

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
