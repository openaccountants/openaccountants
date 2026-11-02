---
name: ls-corporate-income-tax
description: "Corporate income tax, advance corporation tax, withholding tax and transfer pricing for companies in Lesotho. Covers Lesotho tax year 2026-27 (1 April 2026 to 31 March 2027), figures read from Revenue Services Lesotho and gazetted law on 1 November 2026. Use when someone asks about lesotho corporate income tax in Lesotho, what applies, what the rate or threshold is, when to file or pay, what a late filing costs, or how an amount is worked out. Not signed off by an accountant. It states which points could not be read at source so they are not relied on."
jurisdiction: LS
category: international
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
version: 0.2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lesotho Corporate Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Resident companies, statutory corporations and Lesotho branches of non-resident companies. Partnerships and trusts are not companies. Residents are taxed on worldwide income; non-residents on Lesotho-source income.

Lesotho's tax year runs 1 April to 31 March. This skill covers 2026-27, from 1 April 2026.

## Rates, bands and thresholds

| Item | Figure | Conditions | Official URL |
|---|---|---|---|
| Standard rate | 25% | All income not listed below; also branch profits | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf |
| Manufacturing and farming | 10% | Manufacturing income, income from farming operations | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf |
| Exports outside SACU | unverified: 10% or 0% | RSL guide shows 10%; the Third Schedule in the 2012 Act copy shows 0%. Ask before relying on either | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf |
| Advance corporation tax | 25/75 of the dividend (33.33%) | On dividends distributed; creditable, see the base | https://www.rsl.org.ls/sites/default/files/2026-09/Advanced%20Corporation%20Tax%20Guide.pdf |
| Dividend WHT, non-resident | 25%, or 0% from concessional manufacturing income | s.107(1),(2) | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Interest, royalty, natural resource payment, management charge, non-resident | 25% | s.107(1) | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Same, for manufacturing use only | 15% | Interest, royalties and management charges solely for concessional manufacturing income, s.107(3) | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Lesotho-source services contract, non-resident | 10% | Not management charges, s.108 | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Branch repatriated income | 25% | In addition to income tax on the branch, s.111 | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |
| Interest to residents | 10% |  | https://www.rsl.org.ls/sites/default/files/2026-09/Withholding%20Tax%20Public%20Ruling_2.pdf |
| Resident contractors | 5% | No withholding where the total fee is under M3,000; not for an individual's principal residence, s.157 | https://www.rsl.org.ls/sites/default/files/2026-09/Withholding%20Tax%20Public%20Ruling_2.pdf |
| Liquidator payments | 10% | s.160 | https://www.rsl.org.ls/sites/default/files/2026-09/Withholding%20Tax%20Public%20Ruling_2.pdf |

## The base

Chargeable income is gross income less allowed deductions. Only 50% of otherwise allowable entertainment or meals expenses is deductible (s.35). Company losses carry forward. Losses from concessional manufacturing income carry forward only against later manufacturing income (s.47(3),(4)). Gains on assets go into chargeable income. Transfer pricing: between associates the Commissioner General may reallocate income, deductions and credits, and adjust intangible income (s.113). No separate documentation rule was found in the sections read.

## Deadlines and filing

- Return: by 30 June (s.128), or the last day of the third month after an approved substituted year.
- Provisional tax: three instalments of 30% of last year's liability, 30 September, 31 December, 31 March; for a substituted year, last day of the 6th, 9th and 12th months (s.150).
- Dividend return: within 7 days of paying the dividend (s.154).
- Withholding statement: within 28 days after the year ends.

## Penalties and interest

The additional tax rate for late filing and late payment is 22% per twelve-month period as stated by RSL. It also applies to under-estimation and tax not withheld (Income Tax Act Part on additional tax, s.192 onward), where the specified rate is the rate RSL publishes. Poor records: additional tax equal to double the tax involved, as the Act words it.

## Cross-border points

RSL lists agreements with South Africa, the United Kingdom, Mauritius, Botswana and Eswatini, and information exchange agreements with Guernsey and the Isle of Man. The RSL ruling gives treaty rates of 5%, 10% and 12.5% for dividends, 15% for interest, and 7.5% or 10% for management fees and royalties; the rate depends on the treaty, so open the treaty before applying one.

## Two worked examples that recompute

Example 1: company with M1,000,000 of ordinary income pays 25%, M250,000.

```oa-check
name: Ordinary company M1,000,000
inputs:
  profit: 1000000
steps:
  - tax: profit * 0.25
expected:
  tax: 250000.00
```

Example 2, a decision: does M1,000,000 of qualifying manufacturing income beat ordinary income? Yes: 10% is M100,000, a saving of M150,000, and a dividend from it carries no non-resident withholding.

```oa-check
name: Manufacturing saving
inputs:
  profit: 1000000
steps:
  - mfg: profit * 0.10
  - std: profit * 0.25
  - saving: std - mfg
expected:
  saving: 150000.00
```

## Ask the client first

1. Resident company or branch?
2. Manufacturing or farming income, and any exports outside SACU?
3. Year end: 31 March or substituted?
4. Payments to non-residents, and to which country?
5. Dividends paid this year?
6. Dealings with associates?

## Sources

| Source | URL | Read on |
|---|---|---|
| RSL Corporate Income Tax Guide; read in full | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf | 2026-11-01 |
| RSL Advanced Corporation Tax Guide; read in full | https://www.rsl.org.ls/sites/default/files/2026-09/Advanced%20Corporation%20Tax%20Guide.pdf | 2026-11-01 |
| Income Tax Act 1993, RSL copy updated to 1 April 2012; read the sections cited; later amendments are not in this copy | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf | 2026-11-01 |
| RSL Withholding Tax Public Ruling; read the rate tables | https://www.rsl.org.ls/sites/default/files/2026-09/Withholding%20Tax%20Public%20Ruling_2.pdf | 2026-11-01 |
| RSL Tax Guide on Provisional Tax; read in full | https://www.rsl.org.ls/sites/default/files/2024-05/Tax%20Guide%20on%20Provisional%20Tax%20%281%29.pdf | 2026-11-01 |
| RSL Tax Treaties page; read the list of agreements only, not the treaty texts | https://www.rsl.org.ls/tax-treaties | 2026-11-01 |

Not yet confirmed: export manufacturing rate (10% against 0%); treaty texts not read; thin capitalisation rules; the crediting mechanics of advance corporation tax; 2026-27 income tax amendments announced in the budget speech.

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
