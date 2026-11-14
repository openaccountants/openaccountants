---
name: bb-corporate-income-tax
description: "Barbados corporation tax for income year 2026. Covers the 9% rate (from income year 2024), 5.5% for approved small businesses with gross income of BBD 2 million or less, the tiered rates on international shipping income, monthly prepayments of one twelfth by the 15th of each month from income year 2025, filing by 15 March or 15 June depending on the year end, the economic substance rules for companies taxed below 9% from 2025, the Corporation Top-up Tax, and 15% withholding for non-treaty payments abroad. Trigger on Barbados corporation tax, BRA company return, 9% Barbados, small business 5.5%, monthly prepayments Barbados. Built from the Income Tax Act amendments and BRA pages; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bb-corporate-income-tax"
  jurisdiction: "BB"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Barbados Corporation Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies liable to tax under the Income Tax Act, Cap. 73, for income year 2026, filing in TAMIS with the Barbados Revenue Authority (BRA). Amounts are BBD.

- **In:** resident companies on the general rate; approved small businesses; international shipping; prepayments and filing.
- **Out (refer):** insurance companies and exempt insurance, qualifying IP income, in-scope multinational groups for the Corporation Top-up Tax computation, banks under the Bank (Tax on Assets) Act.

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| General rate | 9% of taxable income | From income year 2024 (s. 43(8)) | Income Tax (Amendment and Validation) Act, 2024-15: https://bra.gov.bb/attachment?file=Attachments%2fIncome+Tax+(Amendment+and+Validation)+Act%2c+2024-15.pdf&name=Income+Tax+(Amendment+and+Validation)+Act%2c+2024-15 |
| Approved small business | 5.5% | Gross income BBD 2,000,000 or less and registered under the Small Business Development Act (s. 43(9)(a)) | same |
| International shipping | 5.5% to BBD 1,000,000; 3% to BBD 20,000,000; 2.5% to BBD 30,000,000; 1% above | s. 43(9)(b) | same |
| Monthly prepayments | One twelfth of the tax payable, by the 15th of each calendar month | Every company from income year 2025 (s. 64B.1(3)) | same |
| Group relief | Only for companies taxed at 9% | s. 23X | same |
| Filing, year ends 1 January to 30 September | By 15 March of the following year | | BRA, companies filing and payment: https://bra.gov.bb/Popular-Topics/Companies/Filing-and-Payment |
| Filing, year ends 1 October to 31 December | By 15 June of the following year | | same |
| Withholding, non-treaty | 15% | Treaty ranges: dividends 0 to 15%, interest 5 to 15%, royalties 5 to 15%, management fees 0 to 15% | BRA, withholding tax: https://bra.gov.bb/Popular-Topics/Companies/Withholding-Tax |
| Economic substance | Required for companies taxed below 9% under ss. 43A(3A), 43(9)(b) or 43B | Income year 2025 onwards | Income Tax (Amendment) Act, 2025-30: https://bra.gov.bb/attachment?file=Attachments%2fIncome+Tax+(Amendment)+Act%2c+2025-30.pdf&name=Income+Tax+(Amendment)+Act%2c+2025-30 |

BRA's filing page still describes the older 50% prepayment pattern (September and March, or December and March); the 2024-15 Act's monthly prepayments apply from income year 2025.

## The base

- Taxable income is assessable income less allowable deductions; trading losses carry forward under the Act (see BRA trading losses page).
- Dividends paid by one local company to another are exempt (BRA dividends page).
- Financial statements must accompany the return.
- Qualifying IP income uses a nexus ratio with a 30% uplift on qualifying expenditure (2024-15 Act); refer.

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | TIN and TAMIS web user for the company | After incorporation |
| 2 | Monthly prepayment of one twelfth of the estimated tax | By the 15th of each month |
| 3 | Corporation tax return with financial statements in TAMIS | 15 March or 15 June, by year end |
| 4 | Balance of tax | On filing |

## Penalties and interest

Not confirmed on the pages read for this version; see Not yet confirmed.

## Cross-border points

- 15% withholding on payments to non-treaty non-residents; treaty rates lower.
- In-scope multinational groups (consolidated revenue of EUR 750 million or more) are subject to the Corporation Top-up Tax Act, 2024-16; refer.

## Two worked examples that recompute

### Example 1: Taxable income BBD 1,000,000, general rate or approved small business

At 9% the tax is BBD 90,000 (BBD 7,500 a month in prepayments). An approved small business with gross income of BBD 2,000,000 or less pays 5.5%: BBD 55,000. The approval saves BBD 35,000.

```oa-check
name: BB 2026 company 9% vs approved small business 5.5%
inputs:
  taxable: 1000000
steps:
  - tax_general: taxable * 0.09
  - monthly_prepayment: tax_general / 12
  - tax_small: taxable * 0.055
  - saving: tax_general - tax_small
expected:
  tax_general: 90000
  monthly_prepayment: 7500
  tax_small: 55000
  saving: 35000
```

### Example 2: Shipping company with taxable income BBD 25,000,000

5.5% x BBD 1,000,000 = BBD 55,000; 3% x BBD 19,000,000 = BBD 570,000; 2.5% x BBD 5,000,000 = BBD 125,000. Total BBD 750,000, against BBD 2,250,000 at 9%.

```oa-check
name: BB 2026 international shipping tiers
inputs:
  taxable: 25000000
steps:
  - tier1: min(taxable, 1000000) * 0.055
  - tier2: max(min(taxable, 20000000) - 1000000, 0) * 0.03
  - tier3: max(min(taxable, 30000000) - 20000000, 0) * 0.025
  - tier4: max(taxable - 30000000, 0) * 0.01
  - total: tier1 + tier2 + tier3 + tier4
  - at_general: taxable * 0.09
expected:
  tier1: 55000
  tier2: 570000
  tier3: 125000
  tier4: 0
  total: 750000
  at_general: 2250000
```

## Ask the client first

1. Year end, and gross income for the year?
2. Is the company an approved small business?
3. Shipping, insurance, IP or banking activity?
4. Part of a multinational group with revenue of EUR 750 million or more?
5. Prepayments made each month in 2026?
6. Payments to non-residents and the treaty country.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax (Amendment and Validation) Act, 2024-15: read for s. 43(8) and (9), s. 23X and s. 64B.1 | https://bra.gov.bb/attachment?file=Attachments%2fIncome+Tax+(Amendment+and+Validation)+Act%2c+2024-15.pdf&name=Income+Tax+(Amendment+and+Validation)+Act%2c+2024-15 | 2026-11-14 |
| Income Tax (Amendment) Act, 2025-30: read for the economic substance division, s. 52A | https://bra.gov.bb/attachment?file=Attachments%2fIncome+Tax+(Amendment)+Act%2c+2025-30.pdf&name=Income+Tax+(Amendment)+Act%2c+2025-30 | 2026-11-14 |
| BRA, companies filing and payment: read for the 15 March and 15 June dates | https://bra.gov.bb/Popular-Topics/Companies/Filing-and-Payment | 2026-11-14 |
| BRA, withholding tax: read for 15% non-treaty and treaty ranges | https://bra.gov.bb/Popular-Topics/Companies/Withholding-Tax | 2026-11-14 |
| BRA, dividends page: read for the inter-company dividend exemption | https://bra.gov.bb/Popular-Topics/Companies/Dividends | 2026-11-14 |

Not yet confirmed: insurance company rates (earlier version: 0% to 2% by class) and the 4.5% qualifying IP rate; the Qualified Domestic Minimum Top-Up Tax details; domestic withholding rates on dividends to residents (earlier version: 0% to companies, 15% to individuals), interest to resident individuals (15%, 0% for pensioners 60+), and the earlier version's 0% to 5% non-resident dividend and 0% royalty rates; trading loss carry-forward limits; penalties and interest; the earlier version's 31 July 2025 extended deadline for 2024 returns.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bb-corporate-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bb-corporate-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
