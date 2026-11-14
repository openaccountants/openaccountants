---
name: tt-tax-overview
description: >
  Overview of the Trinidad and Tobago tax system for the 2026 year of income, to
  route a question to the right skill. The Board of Inland Revenue collects
  income tax (25% to TT$1,000,000 of chargeable income, 30% above, personal
  allowance TT$90,000), corporation tax (30%, 35% for banks and petrochemical
  companies), business levy 0.6%, Green Fund Levy 0.3%, VAT 12.5% (threshold
  TT$600,000) and PAYE; NIBTT collects National Insurance at 16.2% from January
  2026 (subject to all legislative approvals, per NIBTT). Trigger on Trinidad tax overview, TT tax system, BIR, IRD Trinidad. Not
  reviewed by an accountant.
version: 1.0
jurisdiction: TT
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
tier: 2
domain: income-tax
type: situation-rules
---

# Trinidad and Tobago Tax Overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone needing the shape of Trinidad and Tobago tax for the 2026 year of income (calendar year) before loading a detailed skill. The Board of Inland Revenue, through the Inland Revenue Division (IRD) of the Ministry of Finance, administers income tax, corporation tax, levies, VAT and PAYE; the National Insurance Board (NIBTT) runs National Insurance. Amounts are TT$.

| Question | Skill |
|---|---|
| Individual or self-employed income tax | `tt-income-tax` |
| Corporation tax, business levy, Green Fund Levy | `tt-corporate-income-tax` |
| VAT | `trinidad-vat` |
| PAYE, health surcharge, NIS | `tt-payroll-social` |
| Incorporating a company | `tt-company-formation` |

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| Individual rates | 25% to TT$1,000,000 of chargeable income, 30% above | Persons other than companies | Income Tax Act, Chap. 75:01: https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.01-Income-Tax-Act--2024.pdf |
| Personal allowance | TT$90,000 | Residents | same |
| Corporation tax | 30%; 35% banks and petrochemical and gas companies | First Schedule | Corporation Tax Act, Chap. 75:02: https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.02-Corporation-Tax-Act--2024.pdf |
| Business levy | 0.6% of gross receipts, if higher than income or corporation tax | Exemptions apply | same |
| Green Fund Levy | 0.3% of gross receipts | Companies and partnerships | IRD, corporations page: https://www.ird.gov.tt/corporations |
| VAT | 12.5%; registration above TT$600,000 in 12 months | Two-month periods for most | IRD, VAT page: https://www.ird.gov.tt/VAT |
| National Insurance | 16.2% of insurable earnings from 5 January 2026 | One third employee, two thirds employer; NIBTT says subject to all legislative approvals, see Not yet confirmed | NIBTT: https://www.nibtt.net/Contribution_Rates/rates.html |
| Annual returns | 30 April; 2025 returns of self-employed and companies extended to 2 November 2026 | | IRD, public notice: https://www.ird.gov.tt/news/public-notice-self-employed-sole-traders-and-companies |

## The base

- Residents are taxed on income from all sources; a person not ordinarily resident or not domiciled is taxed on foreign income only when received in the country (Income Tax Act s. 5(2)).
- Companies pay corporation tax on chargeable profits, or business levy on gross receipts where higher, plus Green Fund Levy.
- VAT is charged on commercial supplies of goods and services, with zero-rated and exempt supplies.

## Deadlines and filing

Quarterly instalments at the end of March, June, September and December; annual returns by 30 April; PAYE and health surcharge by the 15th of each month; VAT within 25 days after each tax period. All through IRD e-Tax.

## Penalties and interest

Late returns: TT$100 (individuals) or TT$1,000 (companies) for every six months; unpaid income tax after 30 April: 20% a year; late VAT: 8% plus 2% a month.

## Cross-border points

Withholding on payments to non-residents: 8% on distributions (3% to a parent company) and 15% on other payments unless a treaty applies (Income Tax Act Third Schedule Part II).

## Two worked examples that recompute

### Example 1: Resident employee, total income TT$1,300,000, personal allowance only

Chargeable income TT$1,210,000. Tax 25% x TT$1,000,000 + 30% x TT$210,000 = TT$313,000.

```oa-check
name: TT 2026 overview, resident income 1.3m
inputs:
  income: 1300000
  allowance: 90000
steps:
  - chargeable: income - allowance
  - tax: min(chargeable, 1000000) * 0.25 + max(chargeable - 1000000, 0) * 0.30
expected:
  chargeable: 1210000
  tax: 313000
```

### Example 2: Company with chargeable profits TT$100,000 on receipts TT$20,000,000: corporation tax or business levy?

Corporation tax TT$30,000; business levy TT$120,000. The levy is higher, so TT$120,000 is paid, plus Green Fund Levy TT$60,000.

```oa-check
name: TT 2026 overview, corporation tax vs business levy
inputs:
  profits: 100000
  receipts: 20000000
steps:
  - corporation_tax: profits * 0.30
  - business_levy: receipts * 0.006
  - main_charge: max(corporation_tax, business_levy)
  - green_fund: receipts * 0.003
expected:
  corporation_tax: 30000
  business_levy: 120000
  main_charge: 120000
  green_fund: 60000
```

## Ask the client first

1. Individual, self-employed or company?
2. Resident, ordinarily resident and domiciled?
3. Gross receipts and profits for the year?
4. Employees?
5. Payments to or from abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Chap. 75:01 (2024 consolidation): read for rates, personal allowance, s. 5(2) and withholding rates | https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.01-Income-Tax-Act--2024.pdf | 2026-11-14 |
| Corporation Tax Act, Chap. 75:02 (2024 consolidation): read for the First Schedule and business levy | https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.02-Corporation-Tax-Act--2024.pdf | 2026-11-14 |
| IRD, corporations page: read for the Green Fund Levy and quarterly dates | https://www.ird.gov.tt/corporations | 2026-11-14 |
| IRD, VAT page: read for the rate and threshold | https://www.ird.gov.tt/VAT | 2026-11-14 |
| NIBTT, contribution rates page: read for the 2026 and 2027 rates | https://www.nibtt.net/Contribution_Rates/rates.html | 2026-11-14 |
| NIBTT, Acts and amendments page: read for the contribution orders and legal notices listed (latest contribution amendment 2008; none for 2025 or 2026) | https://www.nibtt.net/Amendments/NIBTTAct_amend.html | 2026-11-14 |
| IRD, public notice on the 2025 filing deadline: read in full | https://www.ird.gov.tt/news/public-notice-self-employed-sole-traders-and-companies | 2026-11-14 |

Not yet confirmed: whether NIBTT's 16.2% NIS rate from 5 January 2026 received all legislative approvals (NIBTT's 2026 table says it is subject to them; no enacting legal notice found on NIBTT's legislation page, read 14 Nov 2026); Finance Act changes for 2026 after the 2024 consolidations; the FY2026 budget proposals (0.25% asset levy on banks and insurers, landlord surcharge of 2.5% and 3.5% on gross rent); interest on late corporation tax.
