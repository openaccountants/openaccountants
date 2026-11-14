---
name: hk-tax-overview
description: "Use this skill to orient a Hong Kong tax question for the year of assessment 2026/27 (1 April 2026 to 31 March 2027) and route it to the right Hong Kong skill. It gives the system at a glance (territorial basis, IRD, no VAT, no capital gains tax, no withholding tax on dividends or interest), the headline salaries tax and profits tax rates, and the 2025/26 filing cycle dates. Built from the law, not reviewed by an accountant."
jurisdiction: HK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27, the year that contains most of 2026. Filing dates are the 2025/26 cycle published by the IRD in 2026."
version: "2.0"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: router
---

# Hong Kong tax overview and routing (year of assessment 2026/27)

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by a qualified professional in Hong Kong.

## Scope

Hong Kong operates a low-rate, territorial (source-based) tax system administered by the Inland Revenue Department (IRD) under the Inland Revenue Ordinance (Cap. 112). Only profits and income arising in or derived from Hong Kong are chargeable; there is no VAT or GST, no capital gains tax and no withholding tax on dividends or interest. The year of assessment runs 1 April to 31 March: 2026/27 is 1 April 2026 to 31 March 2027. Currency: Hong Kong dollar (HKD). The main direct taxes are profits tax (business profits), salaries tax (employment income) and property tax (rental income); there is no comprehensive personal income tax, although an individual may elect personal assessment.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Salaries tax, progressive rates | 2%, 6%, 10%, 14% on successive HKD 50,000 bands, 17% on the remainder | Net chargeable income (after allowances); YA 2020/21 onwards | https://www.gov.hk/en/residents/taxes/taxfiling/taxrates/salariesrates.htm |
| Salaries tax, standard rate | 15% on the first HKD 5,000,000 of net income, 16% above | Applies if lower than the progressive result; YA 2024/25 onwards | same |
| Basic allowance | HKD 145,000 | From YA 2026/27 (HKD 132,000 for 2025/26) | https://www.ird.gov.hk/eng/tax/budget.htm |
| Profits tax, corporations | 8.25% on the first HKD 2,000,000, 16.5% above | Two-tiered rates; one nominated entity per connected group | https://www.ird.gov.hk/eng/tax/bus_pft.htm |
| Profits tax, unincorporated businesses | 7.5% on the first HKD 2,000,000, 15% above | Same | same |
| Property tax | 15% of net assessable value | After a 20% statutory allowance for repairs and outgoings | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf |
| MPF mandatory contributions deduction | HKD 18,000 a year | Salaries tax deduction cap, 2019/20 onwards | same |
| Profits tax return, 2025/26, code "D" | Due 17 August 2026 | Represented taxpayers, 31 December 2025 year ends | https://www.ird.gov.hk/eng/pdf/bel26e.pdf |
| Profits tax return, 2025/26, code "M" | Due 16 November 2026 | Represented, 1 January to 31 March 2026 year ends | same |
| Tax return for individuals (BIR60), 2025/26 | Issued 4 May 2026; represented cases extended to 4 July 2026, or 5 October 2026 with sole proprietorship accounts | Represented taxpayers (block extension) | same |

## The method, step by step

1. **Name the income.** Employment income: `hk-salaries-tax`. Business profits (company or unincorporated): `hk-corporate-income-tax`. Mandatory Provident Fund: `hk-mpf`. Setting up a company: `hk-company-formation`. VAT, GST, hotel tax and stamp duty on shares: `hk-vat-gst`. Property tax, stamp duty on property, the wider system and anti-avoidance: `hong-kong-tax`.
2. **Check source.** Ask where the work is done or where the profits are made; offshore income is generally outside tax, subject to the FSIE regime for multinational group entities (`hk-corporate-income-tax`).
3. **Pick the year.** Use YA 2026/27 figures for income of 1 April 2026 to 31 March 2027; use 2025/26 figures for returns being filed in 2026.
4. **Mainland China, Macao and Taiwan** are separate tax systems: use the `china` and `taiwan` packs.

### Worked case: routing check with a salaries tax figure

A single employee earns HKD 600,000 in 2026/27 and pays HKD 18,000 of mandatory MPF. Route: `hk-salaries-tax`. Net chargeable income = 600,000 less 18,000 less the HKD 145,000 basic allowance = 437,000. Progressive tax: 1,000 + 3,000 + 5,000 + 7,000 on the first 200,000, plus 17% of 237,000 = 40,290; total HKD 56,290. Standard rate check: 15% of 582,000 = 87,300. The lower, HKD 56,290, is payable.

```oa-check
name: HK 2026/27 single employee HKD 600,000, progressive vs standard
inputs:
  income: 600000
  mpf: 18000
  basic: 145000
steps:
  - nci: income - mpf - basic
  - progressive: 50000 * 0.02 + 50000 * 0.06 + 50000 * 0.10 + 50000 * 0.14 + (nci - 200000) * 0.17
  - standard: (income - mpf) * 0.15
  - tax: min(progressive, standard)
expected:
  nci: 437000
  progressive: 56290
  standard: 87300
  tax: 56290
```

## When to refuse or refer

- Questions on Mainland China tax: refer to the `china` pack; Hong Kong residence does not end Mainland liability (`china-to-singapore-relocation-tax` explains the domicile test for movers).
- Offshore claims, FSIE exceptions, Pillar Two top-up tax, transfer pricing disputes: refer to a Hong Kong tax representative.
- Any request to hide income or file a false return: refuse.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| GovHK, tax rates of salaries tax and personal assessment. Read for the progressive scale and the 15% and 16% standard rates | https://www.gov.hk/en/residents/taxes/taxfiling/taxrates/salariesrates.htm | 2026-11-14 |
| IRD, 2026-27 Budget tax measures. Read for the YA 2026/27 allowances | https://www.ird.gov.hk/eng/tax/budget.htm | 2026-11-14 |
| IRD, profits tax page. Read for the two-tiered rates | https://www.ird.gov.hk/eng/tax/bus_pft.htm | 2026-11-14 |
| IRD, A brief guide to taxes 2025/26 (PDF). Read for territorial basis, property tax 15% and 20% allowance, MPF deduction cap | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf | 2026-11-14 |
| IRD, block extension letter for 2025/26 returns (PDF). Read for profits tax and BIR60 dates | https://www.ird.gov.hk/eng/pdf/bel26e.pdf | 2026-11-14 |

Not yet confirmed: the due date for unrepresented individuals (normally one month after issue; not read on an official page in this pass); the 2026/27 filing cycle dates (returns issue in April and May 2027 under a new letter).
