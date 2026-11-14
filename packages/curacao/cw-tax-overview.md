---
name: cw-tax-overview
description: "Overview of the Curacao tax system for tax year 2026. Which taxes exist (income tax, profit tax, turnover tax OB, wage tax and SVB premiums, inheritance tax), who administers them, the headline 2026 rates, the filing rhythm and where each job is covered in this pack. Use it to route a Curacao question to the right skill. Trigger phrases include Curacao taxes, tax system Curacao, Belastingdienst Curacao, Curacao tax rates 2026, doing business in Curacao tax."
version: "1.0"
jurisdiction: CW
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: situation-rules
---

# Curacao tax overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: calendar year 2026. Curacao is a country within the Kingdom of the Netherlands with its own tax laws. The Belastingdienst Curacao (Inspectie der Belastingen) administers income tax, profit tax, turnover tax and wage tax, and collects the AOV/AWW, AVBZ and BVZ premiums on its returns; the SVB sets the premiums and handles ZV, OV and cessantia. Amounts are Curacao guilders (ANG or NAf on older pages, XCG or Cg on newer ones).

## Who this applies to

Anyone asking which Curacao taxes apply and where to look. Each job has its own skill:

| Job | Skill |
|---|---|
| Personal income tax, penshonado | `cw-income-tax` |
| Profit tax for companies | `cw-corporate-income-tax` |
| Turnover tax (OB) | `cw-vat-gst` |
| Wage tax and social premiums | `cw-payroll-social` |
| Forming and registering a business | `cw-company-formation` |

Which tax a business pays depends on its legal form: a sole trader, V.O.F. or maatschap pays income tax on profit; a B.V., N.V. or a foundation or association running a business pays profit tax; every entrepreneur deals with OB, and employers with wage tax ([Tax Office Curacao, Startende ondernemers](https://belastingdienst.cw/ondernemer/themas/startende-ondernemers/)).

## Rates, bands and thresholds

Headline figures only; the owning skill holds the conditions.

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Income tax and wage tax rate range | 9.75% to 46.5% | Six bands; detail in `cw-income-tax` | 2026 | [Schijven tarief 2026](https://belastingdienst.cw/wp-content/uploads/2026/01/Schijven-tarief-2026.pdf) |
| Profit tax, general | 15% on the first 500,000, 22% above | Detail and special rates in `cw-corporate-income-tax` | 2026 | [Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/) |
| Turnover tax (OB) | 6% general, 7% insurance and short stays, 9% listed goods and services, exemptions | Detail in `cw-vat-gst` | 2026 | [Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/) |
| AOV premium | 15% (9% employer, 6% employee) | Up to XCG 100,000 premium income; detail in `cw-payroll-social` | 2026 | [SVB Tabel 2026](https://svbcur.org/wp-content/uploads/2026/01/Tabel-2026.pdf) |
| BVZ premium | 13.6% (9.3% employer, 4.3% employee) | Up to XCG 150,000 | 2026 | same |
| Inheritance tax (successiebelasting) | 2% to 24% | Not covered in this pack | 2026 | [Tax Office Curacao, Belastingtarieven](https://belastingdienst.cw/particulier/themas/belastingtarieven/) |

## The base

- **Income tax:** residents on worldwide income, non-residents on Curacao income ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)).
- **Profit tax:** legal persons on their profit, with an optional territoriality rule for foreign results ([Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/)).
- **OB:** a cumulative turnover tax on each supply, charged by the entrepreneur; not a VAT with input credit ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)).
- **Wage tax and premiums:** withheld by the withholding agent on wages in money and in kind ([Tax Office Curacao, Loonbelasting](https://belastingdienst.cw/ondernemer/themas/loonbelasting/)).

## Deadlines and filing

- All returns are filed online through the Belastingdienst portal; payments by bank only ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)).
- OB and wage tax: monthly (OB also quarterly or annual by turnover band), due by the 15th of the next month, or the next working day ([Inleverdata 2026](https://belastingdienst.cw/wp-content/uploads/2026/02/Inleverdata-aangiften-2026_huisstijl_ME-LB-OB.docx-2.pdf)).
- Profit tax: provisional return within 3 months of year end, final within 6 ([Tax Office Curacao, Winstbelasting](https://belastingdienst.cw/ondernemer/themas/winstbelasting/)).
- Income tax: within two months of the invitation, or within 36 months without one ([Tax Office Curacao, Inkomstenbelasting](https://belastingdienst.cw/particulier/themas/inkomstenbelasting/)).
- Records: keep 10 years ([Tax Office Curacao, Startende ondernemers](https://belastingdienst.cw/ondernemer/themas/startende-ondernemers/)).

## Penalties and interest

Each tax has default penalties that rise with repeat defaults; see the owning skill. OB and wage tax defaults are counted over the previous 9 periods ([Inleverdata 2026](https://belastingdienst.cw/wp-content/uploads/2026/02/Inleverdata-aangiften-2026_huisstijl_ME-LB-OB.docx-2.pdf)).

## Cross-border points

- A foreign entrepreneur supplying services in Curacao owes OB ([Tax Office Curacao, Omzetbelasting](https://belastingdienst.cw/ondernemer/themas/omzetbelasting/)).
- Relief from wage tax under a treaty or the tax arrangement for the Kingdom needs an Inspector's statement ([Tax Office Curacao, Startende ondernemers](https://belastingdienst.cw/ondernemer/themas/startende-ondernemers/)).
- Withholding taxes on dividends, interest and royalties, transfer pricing documentation and the Pillar Two minimum tax are not confirmed on an official page for this pack: refer.

## Two worked examples that recompute

**Case 1: a B.V. with profit of 300,000 and OB turnover.** Profit tax: 15% of 300,000 = 45,000 (all in the first band). Its 2026 sales of 1,200,000 at the 6% general rate carry OB of 72,000, paid monthly.

```oa-check
name: Curacao B.V. profit tax and OB, 2026
inputs:
  profit: 300000
  sales: 1200000
steps:
  - profit_tax: min(profit, 500000) * 0.15 + max(profit - 500000, 0) * 0.22
  - ob: sales * 0.06
expected:
  profit_tax: 45000.00
  ob: 72000.00
```

**Case 2: decision, sole trader or B.V. for a profit of 60,000.** As a sole trader the profit is income: 2026 table 5,767 + 23% of (60,000 less 52,127) = 7,577.79, less the basic credit 2,915 = 4,662.79. Through a B.V., profit tax is 15% of 60,000 = 9,000 before any salary or dividend, which then carries wage tax or the 19.5% substantial-interest rate. On these facts the sole trader pays less; the comparison changes with salary, dividends, premiums and liability, so take it to `cw-income-tax` and `cw-corporate-income-tax`.

```oa-check
name: Sole trader or B.V. at profit 60000
inputs:
  profit: 60000
steps:
  - sole_trader_tax: 5767 + (profit - 52127) * 0.23 - 2915
  - bv_profit_tax: profit * 0.15
  - difference: bv_profit_tax - sole_trader_tax
expected:
  sole_trader_tax: 4662.79
  bv_profit_tax: 9000.00
  difference: 4337.21
```

## Ask the client first

1. Individual or business? If a business, which legal form?
2. Resident in Curacao, and since when?
3. Employees, and how many?
4. Expected turnover (OB filing band) and profit.
5. Any foreign income, foreign customers or foreign group companies?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Office Curacao, Belastingtarieven: read for the income, wage, OB and inheritance tax rate ranges | https://belastingdienst.cw/particulier/themas/belastingtarieven/ | 2026-11-14 |
| Tax Office Curacao, Schijven tarief 2026: read for the 2026 bands | https://belastingdienst.cw/wp-content/uploads/2026/01/Schijven-tarief-2026.pdf | 2026-11-14 |
| Tax Office Curacao, Winstbelasting: read for profit tax rates and return deadlines | https://belastingdienst.cw/ondernemer/themas/winstbelasting/ | 2026-11-14 |
| Tax Office Curacao, Omzetbelasting: read for OB rates, the cumulative system, portal and bank payment | https://belastingdienst.cw/ondernemer/themas/omzetbelasting/ | 2026-11-14 |
| Tax Office Curacao, Inkomstenbelasting: read for residence and filing | https://belastingdienst.cw/particulier/themas/inkomstenbelasting/ | 2026-11-14 |
| Tax Office Curacao, Loonbelasting: read for the wage base | https://belastingdienst.cw/ondernemer/themas/loonbelasting/ | 2026-11-14 |
| Tax Office Curacao, Startende ondernemers: read for legal forms and their taxes, treaty statements and 10-year records | https://belastingdienst.cw/ondernemer/themas/startende-ondernemers/ | 2026-11-14 |
| SVB, Tabel 2026: read for the AOV and BVZ rates and ceilings | https://svbcur.org/wp-content/uploads/2026/01/Tabel-2026.pdf | 2026-11-14 |
| Tax Office Curacao, Inleverdata aangiften 2026: read for the 2026 due dates and default counting | https://belastingdienst.cw/wp-content/uploads/2026/02/Inleverdata-aangiften-2026_huisstijl_ME-LB-OB.docx-2.pdf | 2026-11-14 |

Not yet confirmed: withholding taxes on dividends, interest and royalties (the old file said none, citing a law firm); the Pillar Two minimum tax; the official ANG to XCG conversion notice (an image); inheritance tax detail (not covered).
