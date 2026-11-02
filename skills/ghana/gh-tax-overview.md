---
name: gh-tax-overview
description: >
  Use this skill for a map of Ghana tax for 2026: the year of assessment, currency, the Ghana Revenue Authority, how residents and non-residents are taxed, the top personal rate from 1 September 2026, the 25% company rate, VAT at 15% plus levies under Act 1151, pensions, the main due dates, and which Ghana skill to load next. Trigger on "Ghana tax overview", "taxes in Ghana", "how does tax work in Ghana", "Ghana tax system", or any general Ghana tax question. Figures are owned by the linked skills.
version: 0.2
jurisdiction: GH
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ghana Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone asking how Ghana taxes people and businesses in 2026, before picking a detailed skill. GRA administers the taxes. Three changes matter in 2026: Act 1151 replaced the VAT Act from 1 January; SSNIT ceilings rose on 1 January; Act 1178 changed individual bands from 1 September.

## Rates, bands and thresholds

| Topic | Position | Owner skill | Tax year | Official URL |
|---|---|---|---|---|
| Top personal rate | 35% above GHS 600,000 of annual chargeable income, from 1 September 2026 | [ghana-pit](ghana-pit.md) | 2026 | https://gra.gov.gh/wp-content/uploads/2026/09/Amendments-To-The-Income-Tax-2015-Act-896_Updated-1.pdf |
| Company rate | 25% general; sector rates apply | [gh-corporate-income-tax](gh-corporate-income-tax.md) | 2026 | https://gra.gov.gh/domestic-tax/tax-types/corporate-income-tax/ |
| VAT | 15% plus NHIL 2.5% and GETFund 2.5%, 20% in total | [ghana-vat](ghana-vat.md) | 2026 | https://gra.gov.gh/domestic-tax/tax-types/vat/ |
| Pensions | 18.5% of basic salary | [gh-payroll-social](gh-payroll-social.md) | 2026 | https://www.ssnit.org.gh/faqs/ |

## The base

Residents are taxed on worldwide income, non-residents on income from Ghana ([GRA](https://gra.gov.gh/domestic-tax/personal-income-tax/)). The year of assessment is the calendar year; a company can have another basis period. The currency is the Ghana cedi (GHS). Other taxes on the GRA site include Communications Service Tax, excise, stamp duty, gift tax, capital gains, rent income tax and vehicle income tax.

## Deadlines and filing

Annual income tax returns are due four months after the year: 30 April ([Act 896 s.124](https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf)). PAYE and withholding are monthly by the 15th; VAT is monthly by the last working day. All returns go through www.etax.gra.gov.gh ([ITAS](https://gra.gov.gh/itas-faqs/)).

## Penalties and interest

Late return: GHS 500 plus GHS 10 a day. Late payment: 125% of the Bank of Ghana policy rate, compounded monthly ([Act 915](https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf)).

## Cross-border points

Withholding and treaties are in [gh-cross-border](gh-cross-border.md); related parties in [gh-transfer-pricing](gh-transfer-pricing.md); setting up in [gh-company-formation](gh-company-formation.md).

## Two worked examples that recompute

**Example 1: VAT on a GHS 1,000 sale.** VAT 150, levies 50, price GHS 1,200.

```oa-check
name: Sale of 1,000
inputs:
  price: 1000
steps:
  - tax: price * 0.20
  - total: price + tax
expected:
  total: 1200.00
```

**Example 2: sole trader or company, on GHS 800,000 profit?** Company tax at 25% is GHS 200,000, before 8% on dividends paid out. An individual on the bands pays GHS 6,258 + 48,000 + 109,195.20 + 70,000 = GHS 233,453.20. The company is cheaper while profit stays in it; if all GHS 600,000 is distributed, GHS 48,000 more makes GHS 248,000, and the individual route wins. Non-tax matters then decide.

```oa-check
name: Company against individual at 800,000 profit
inputs:
  profit: 800000
steps:
  - company: profit * 0.25
  - dividend_tax: (profit - company) * 0.08
  - company_all: company + dividend_tax
  - person: 960 * 0.05 + 1200 * 0.10 + 34800 * 0.175 + 192000 * 0.25 + 363984 * 0.30 + (profit - 600000) * 0.35
expected:
  company_all: 248000.00
  person: 233453.20
```

## Ask the client first

1. Individual or company.
2. Resident or not.
3. Type of income or activity.
4. Turnover and staff.
5. The tax year in question.

## Sources

| Source | URL | Read on |
|---|---|---|
| GRA notice, Income Tax (Amendment) Act, 2026 (Act 1178), whole notice | https://gra.gov.gh/wp-content/uploads/2026/09/Amendments-To-The-Income-Tax-2015-Act-896_Updated-1.pdf | 2026-11-01 |
| GRA, Corporate Income Tax page, page read in full | https://gra.gov.gh/domestic-tax/tax-types/corporate-income-tax/ | 2026-11-01 |
| GRA, VAT page (2026 reforms), page read in full | https://gra.gov.gh/domestic-tax/tax-types/vat/ | 2026-11-01 |
| SSNIT FAQs (contribution rates and remittance), page read in full | https://www.ssnit.org.gh/faqs/ | 2026-11-01 |
| GRA, Personal Income Tax page, page read in full | https://gra.gov.gh/domestic-tax/personal-income-tax/ | 2026-11-01 |
| Income Tax Act, 2015 (Act 896), OCR of scan; ss 33, 101, 102, 112, 121, 124, 125 read | https://gra.gov.gh/wp-content/uploads/2020/09/INCOME-TAX-ACT-2015-ACT-896.pdf | 2026-11-01 |
| GRA, ITAS FAQs, page read in full | https://gra.gov.gh/itas-faqs/ | 2026-11-01 |
| Revenue Administration Act, 2016 (Act 915); ss 27 to 30, 46, 47, 70 to 73 read | https://gra.gov.gh/wp-content/uploads/2023/01/Revenue-Administration-Act-2016-.pdf | 2026-11-01 |

Not yet confirmed: Items are flagged in the linked skills. Stamp duty and excise figures were not refreshed and no skill here covers them.

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
