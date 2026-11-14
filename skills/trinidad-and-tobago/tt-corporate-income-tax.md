---
name: tt-corporate-income-tax
description: >
  Trinidad and Tobago corporation tax for the 2026 year of income. Covers the 30%
  standard rate, 35% for banks and for petrochemical, LNG, gas processing,
  transmission and petroleum wholesale companies, 15% on long-term insurance
  business, the SME listed company holiday, the approved small company exemption,
  business levy of 0.6% (exempt in the first twelve months and below TT$360,000),
  Green Fund Levy of 0.3%, quarterly instalments, the 30 April return (2025
  returns extended to 2 November 2026), the TT$1,000 late filing penalty and
  withholding on payments to non-residents. Trigger on Trinidad corporation tax,
  TT company tax, business levy, Green Fund Levy, BIR company return. Built from
  the Corporation Tax Act and IRD pages; not reviewed by an accountant.
version: 1.0
jurisdiction: TT
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: computation
---

# Trinidad and Tobago Corporation Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Companies liable to corporation tax under the Corporation Tax Act, Chap. 75:02, for the **2026 year of income**, administered by the Board of Inland Revenue (BIR, Inland Revenue Division). Amounts are TT$. Each company sets its Established Accounting Terminal Date (EATD) at registration.

- **In:** resident and non-resident companies with chargeable profits; business levy and Green Fund Levy.
- **Out:** petroleum production companies under the Petroleum Taxes Act (refer); individuals (use `tt-income-tax`); VAT (use `trinidad-vat`); PAYE (use `tt-payroll-social`).

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| Standard corporation tax rate | 30% | First Schedule para. 1; since income year 2018 | Corporation Tax Act, Chap. 75:02 (IRD 2024 consolidation): https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.02-Corporation-Tax-Act--2024.pdf |
| Long-term insurance business | 15% | Profits transferred to shareholders' account taxed at 25% | same |
| Petrochemical and gas companies | 35% | LNG, petrochemicals, gas separation and processing, gas transmission and distribution, wholesale marketing of petroleum products, other prescribed activities (First Schedule para. 3) | same |
| Banks | 35% | Licensed under the Financial Institutions Act (First Schedule para. 4) | same |
| SME listed company | 0% for five years from listing, then 50% of the standard rate for five years | Issued share capital TT$5 million to TT$50 million; at least 25 unconnected shareholders holding 30% of new shares; listed within 60 days (s. 3) | same |
| Approved small company | Exempt for six years from 1 January 2023 | Ministerial approval under ss. 16A to 16E | same |
| Business levy | 0.6% of gross sales or receipts | Payable where it exceeds corporation tax; not in the first twelve months after registration, nor where prior-year gross receipts were TT$360,000 or less (s. 3A) | same |
| Green Fund Levy | 0.3% of gross sales or receipts, exempt income included | From 21 January 2016 | IRD, corporations page: https://www.ird.gov.tt/corporations |
| Quarterly instalments | End of March, June, September and December | Corporation tax, business levy, Green Fund Levy | same |
| 2025 corporation tax return deadline | 2 November 2026 | IRD public notice | IRD, public notice on the 2025 filing deadline: https://www.ird.gov.tt/news/public-notice-self-employed-sole-traders-and-companies |
| Late filing penalty, companies | TT$1,000 for every six months or part | | same |
| Withholding on distributions to non-residents | 8%, or 3% to a parent company | Unless a treaty sets a lower rate | Income Tax Act, Chap. 75:01, Third Schedule Part II: https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.01-Income-Tax-Act--2024.pdf |
| Withholding on other payments to non-residents | 15% | Interest, royalties, management charges and similar; treaty rates may be lower | same |

### Formula

```
chargeable profits = gross sales and receipts - allowable deductions and business expenses
corporation tax    = chargeable profits x rate (30%, 35% or 15%)
business levy      = 0.6% x gross receipts (unless exempt)
pay the higher of corporation tax and business levy
Green Fund Levy    = 0.3% x gross receipts (in addition, not credited)
```

## The base

- Chargeable profits are the accounts profit adjusted under the Act; wear and tear allowances replace depreciation (IRD wear and tear schedule).
- Promotional expenses qualify for a 150% deduction (IRD corporations page).
- Exempt income still counts in the Green Fund Levy base.
- Manufacturing companies' export sales taxed at the First Schedule para. 1 rate are outside business levy (s. 3A(2)(h)).

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | BIR file number; EATD set at registration | On incorporation |
| 2 | Quarterly instalments of corporation tax, business levy and Green Fund Levy | End of March, June, September, December |
| 3 | Annual corporation tax return with accounts, through e-Tax | 30 April following the year of income (2025 returns: 2 November 2026) |
| 4 | PAYE and health surcharge account if there are employees | See `tt-payroll-social` |
| 5 | VAT registration if commercial supplies exceed TT$600,000 in 12 months | See `trinidad-vat` |
| 6 | Withholding tax account for payments abroad; pay within 30 days | IRD withholding tax page |

## Penalties and interest

- Late return: TT$1,000 for each six months or part.
- Interest on late corporation tax: see Not yet confirmed.

## Cross-border points

- Withholding on payments to non-residents: 8% distributions (3% to a parent), 15% other payments, or the treaty rate; non-residents must visit the IRD International Tax Unit for evaluation.
- Double taxation relief by credit under treaties (Income Tax Act Fifth Schedule, applied to corporation tax by the Act).

## Two worked examples that recompute

### Example 1: Trading company, gross receipts TT$10,000,000, chargeable profits TT$2,000,000

Corporation tax 30% = TT$600,000, higher than business levy TT$60,000, so TT$600,000 is paid. Green Fund Levy TT$30,000 is added. Total TT$630,000.

```oa-check
name: TT 2026 company, corporation tax vs business levy, plus Green Fund Levy
inputs:
  receipts: 10000000
  profits: 2000000
steps:
  - corporation_tax: profits * 0.30
  - business_levy: receipts * 0.006
  - main_charge: max(corporation_tax, business_levy)
  - green_fund: receipts * 0.003
  - total: main_charge + green_fund
expected:
  corporation_tax: 600000
  business_levy: 60000
  main_charge: 600000
  green_fund: 30000
  total: 630000
```

### Example 2: Loss-making company with the same receipts, in its first year or later

No chargeable profit. In its second year or later it pays business levy TT$60,000 plus Green Fund Levy TT$30,000 = TT$90,000. In its first twelve months after registration business levy does not apply, so only TT$30,000 of Green Fund Levy.

```oa-check
name: TT 2026 loss-making company, business levy exemption both ways
inputs:
  receipts: 10000000
steps:
  - later_year: receipts * 0.006 + receipts * 0.003
  - first_year: receipts * 0.003
  - difference: later_year - first_year
expected:
  later_year: 90000
  first_year: 30000
  difference: 60000
```

## Ask the client first

1. What does the company do (banking, petrochemicals, gas, insurance, petroleum production)? This sets the rate.
2. When was it registered, and what were last year's gross receipts (business levy exemption)?
3. Is it an approved small company or an SME listed company?
4. Gross receipts including exempt income for the year (Green Fund Levy).
5. Payments to non-residents (withholding), and treaty country.
6. Quarterly instalments paid; was the 2025 return filed by 2 November 2026?

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporation Tax Act, Chap. 75:02 (IRD 2024 consolidation): read for ss. 3, 3A, 16A and the First Schedule paras. 1 to 4 | https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.02-Corporation-Tax-Act--2024.pdf | 2026-11-14 |
| IRD, corporations page: read for rates, business levy, Green Fund Levy, quarterly dates, VAT threshold, PAYE and the 150% promotional deduction | https://www.ird.gov.tt/corporations | 2026-11-14 |
| IRD, public notice on the 2025 filing deadline: read in full | https://www.ird.gov.tt/news/public-notice-self-employed-sole-traders-and-companies | 2026-11-14 |
| Income Tax Act, Chap. 75:01: read for the Third Schedule Part II withholding rates | https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.01-Income-Tax-Act--2024.pdf | 2026-11-14 |
| IRD, withholding tax page: read for the 30-day payment rule and the International Tax Unit | https://www.ird.gov.tt/withholding-tax | 2026-11-14 |
| Ministry of Finance, Budget Statement FY2026: read for the proposed 0.25% asset levy on commercial banks from 1 January 2026 | https://www.finance.gov.tt/wp-content/uploads/2025/10/Budget-Statement-FY-2026-2.pdf | 2026-11-14 |

Not yet confirmed: whether the proposed 0.25% asset levy on banks and insurers and other FY2026 budget measures were enacted (the Act read is the 2024 consolidation); the interest rate on late corporation tax; the Special Economic Zone 15% rate in the earlier version; the petroleum production rates (earlier version: 50%, 30% deep water); the Green Fund Levy rule in the Miscellaneous Taxes Act itself (IRD page relied on); the earlier version's 10% dividend and 10% or 8% interest withholding rates, which the 2024 Act does not show (it gives 8% and 15%); whether the approved small company and business levy rules changed after 2024.
