---
name: tt-income-tax
description: >
  Trinidad and Tobago personal income tax for the 2026 year of income, for
  resident and non-resident individuals, employees and the self-employed. Covers
  the 25% rate on chargeable income up to TT$1,000,000 and 30% above, the
  TT$90,000 personal allowance, tertiary education and other deductions, the
  business levy of 0.6% for the self-employed, health surcharge, quarterly
  instalments, the 30 April return date (2025 returns extended to 2 November
  2026), late filing penalties and 20% interest, and the remittance basis for
  persons not ordinarily resident. Trigger on Trinidad income tax, TT personal
  allowance, BIR, IRD Trinidad, self-employed Trinidad, business levy individual.
  Built from the Income Tax Act and IRD pages; not reviewed by an accountant.
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

# Trinidad and Tobago Personal Income Tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals liable to Trinidad and Tobago income tax under the Income Tax Act, Chap. 75:01, for the **2026 year of income** (calendar year). The Board of Inland Revenue (BIR) administers it through the Inland Revenue Division (IRD) of the Ministry of Finance. Amounts are TT$.

- **In:** residents (income from all sources), non-residents with Trinidad and Tobago income, employees under PAYE, self-employed persons and sole traders, partners.
- **Out:** companies (use `tt-corporate-income-tax`), employer PAYE mechanics and NIS (use `tt-payroll-social`), VAT (use `trinidad-vat`), petroleum taxes.
- **Not ordinarily resident or not domiciled:** income arising outside Trinidad and Tobago is taxed on the amount received in the country, but employment exercised in Trinidad and Tobago is taxed in full (Income Tax Act s. 5(2)).

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| Rate up to TT$1,000,000 of chargeable income | 25% | Persons other than companies (Third Schedule Part I para. 1) | Income Tax Act, Chap. 75:01 (2024 consolidation): https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.01-Income-Tax-Act--2024.pdf |
| Rate above TT$1,000,000 | 30% | Every dollar over TT$1,000,000 | same |
| Personal allowance | TT$90,000 | Residents (s. 17) and non-residents receiving Trinidad and Tobago pension income (s. 18) | same |
| Small-income relief | No tax where chargeable income does not exceed TT$5,000; marginal relief to TT$8,500 | Residents (Third Schedule Part I para. 2) | same |
| Exempt total income | Total income not over TT$60,000 | Resident individual (s. 8(1)(k)) | same |
| Withholding on distributions to non-residents | 8%, or 3% to a parent company | Unless a treaty sets a lower rate (Third Schedule Part II) | same |
| Withholding on other payments to non-residents | 15% | Individuals and companies, unless a treaty sets a lower rate | same |
| Tertiary education expenses | Up to TT$72,000 | From 1 January 2019; foreign institutions only, conditions on the IRD page | IRD, deductions and supporting documents: https://www.ird.gov.tt/individual/deductions-and-required-supporting-documents |
| Business levy, self-employed | 0.6% of gross sales or receipts | Payable where it exceeds income tax; exemption for the first three years from registration of the business per IRD | IRD, self-employed and sole traders: https://www.ird.gov.tt/self-employed-sole-trader |
| Health surcharge, self-employed | TT$8.25 a week (receipts averaging over TT$469.99 a month) or TT$4.80 a week | Paid with quarterly instalments | same |
| Tax credits | 30% of investment in a venture capital company; 25% of solar water heating and CNG kit costs (each capped at TT$10,000); 25% of National Tax-Free Savings Bonds of 5, 7 or 10 years | Claimed on the return | same |
| Quarterly instalments | End of March, June, September and December | Income tax, business levy, health surcharge | same |
| Annual return and balance | 30 April following the year of income; interest at 20% a year from 1 May | Employees assess their liability by 30 April | IRD, first-time employee: https://www.ird.gov.tt/first-time-employee |
| 2025 return deadline (self-employed, sole traders) | 2 November 2026 | IRD public notice | IRD, public notice on the 2025 filing deadline: https://www.ird.gov.tt/news/public-notice-self-employed-sole-traders-and-companies |
| Late filing penalty | TT$100 (individuals) for every six months or part the return is late | | same |
| Quarterly instalment where non-emolument income exceeds 25% of total income | Required | Persons with mixed income | IRD, small business person: https://www.ird.gov.tt/small-business-person |

The personal allowance has been TT$90,000 since 1 January 2023 (TT$72,000 to 2020, TT$84,000 for 2021 and 2022, per IRD's table). The FY2026 budget statement read for this version proposed no change.

### Formula

```
chargeable profit (self-employed) = sales and receipts - allowable expenses (wholly and exclusively)
chargeable income = total income - personal allowance - deductions
                    (tertiary education, first-time home owner, covenants, alimony,
                     approved annuity or pension contributions)
tax = 25% x min(chargeable income, 1,000,000) + 30% x (chargeable income - 1,000,000, not below 0)
      - tax credits
self-employed: pay the higher of income tax and business levy (0.6% x gross receipts)
```

## The base

- **Income from all sources** for a resident goes on one return for the year.
- **Allowable expenses** are verifiable and wholly and exclusively incurred in producing the income; private-use costs (rent, motor vehicle) are apportioned. Wear and tear allowance replaces depreciation; buildings completed from 1 January 1995 and used in the business get 10% on the reducing balance (IRD small business page).
- **Promotional expenses** may be deducted at 150% (IRD corporations page, for qualifying spend).
- **Entertainment**: IRD's small business example allows 25% of entertainment.
- **Deductions** that need prior IRD approval on the TD1 for employees: tertiary education, first-time home acquisition, alimony or maintenance, deferred annuity or pension contributions, venture capital investment.
- **Exempt**: Christmas salary and other exemptions follow the Act; total income of a resident not over TT$60,000 is exempt (s. 8(1)(k)).

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | Obtain a BIR file number (before taking up employment or starting a business) | Before income starts |
| 2 | Employees: give the BIR number and a TD1 to the employer; a new TD1 within 7 days of a change | On starting work |
| 3 | Self-employed: quarterly instalments of income tax or business levy and health surcharge | End of March, June, September, December |
| 4 | Annual individual return with TD4 certificates and supporting documents, through e-Tax | 30 April 2027 for 2026 (2025 returns: 2 November 2026) |
| 5 | Pay any balance | With the return; interest at 20% a year from 1 May |

## Penalties and interest

- Late return: TT$100 for each six months or part (individuals), per IRD's notice.
- Unpaid tax after 30 April: interest at 20% a year from 1 May until paid.

## Cross-border points

- Non-residents generally get no personal allowance, except for Trinidad and Tobago pension income (s. 18).
- Withholding on payments to non-residents: 8% on distributions (3% to a parent company) and 15% on other payments, reduced by treaty (Third Schedule Part II); withholding is paid within 30 days after the payment is made or credited (IRD withholding tax page).
- Remittance basis for foreign income of persons not ordinarily resident or not domiciled (s. 5(2)).
- Double taxation relief by credit (Fifth Schedule).

## Two worked examples that recompute

### Example 1: Sole trader, 2026, sales TT$500,000

IRD's own layout: sales TT$500,000, cost of goods TT$200,000, expenses TT$21,000, net profit TT$279,000. Less personal allowance TT$90,000: chargeable income TT$189,000, tax TT$47,250. Business levy would be 0.6% x TT$500,000 = TT$3,000, lower than the tax, so income tax is paid.

```oa-check
name: TT 2026 sole trader, income tax vs business levy
inputs:
  sales: 500000
  cost_of_goods: 200000
  expenses: 21000
  allowance: 90000
steps:
  - net_profit: sales - cost_of_goods - expenses
  - chargeable: net_profit - allowance
  - income_tax: min(chargeable, 1000000) * 0.25 + max(chargeable - 1000000, 0) * 0.30
  - business_levy: sales * 0.006
  - payable: max(income_tax, business_levy)
expected:
  net_profit: 279000
  chargeable: 189000
  income_tax: 47250
  business_levy: 3000
  payable: 47250
```

### Example 2: Low-margin trader or high earner, which charge applies?

Case A: gross receipts TT$5,000,000 but chargeable income only TT$20,000: income tax TT$5,000, business levy TT$30,000, so the levy is paid (after the first three years). Case B: chargeable income TT$1,200,000: tax TT$250,000 + 30% x TT$200,000 = TT$310,000.

```oa-check
name: TT 2026 business levy decision and top band
inputs:
  receipts_a: 5000000
  chargeable_a: 20000
  chargeable_b: 1200000
steps:
  - tax_a: chargeable_a * 0.25
  - levy_a: receipts_a * 0.006
  - payable_a: max(tax_a, levy_a)
  - tax_b: min(chargeable_b, 1000000) * 0.25 + max(chargeable_b - 1000000, 0) * 0.30
expected:
  tax_a: 5000
  levy_a: 30000
  payable_a: 30000
  tax_b: 310000
```

## Ask the client first

1. Resident, ordinarily resident and domiciled in Trinidad and Tobago in 2026? Any foreign income, and was it remitted?
2. Employed, self-employed, or both? Gross receipts and the date the business was registered (business levy exemption)?
3. Which deductions: tertiary education, first home, pension or annuity contributions, alimony, covenants? Are they approved on a TD1?
4. TD4 certificates, quarterly instalments paid, and any withholding suffered?
5. Tax credit items: venture capital, solar water heating, CNG kit, tax-free savings bonds?
6. Was the 2025 return filed by 2 November 2026?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act, Chap. 75:01 (IRD 2024 consolidation): read for ss. 5(2), 8(1)(k), 17, 18 and the Third Schedule Parts I and II | https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.01-Income-Tax-Act--2024.pdf | 2026-11-14 |
| IRD, self-employed and sole traders page: read for obligations, rates, business levy, health surcharge, quarterly dates, deductions and tax credits | https://www.ird.gov.tt/self-employed-sole-trader | 2026-11-14 |
| IRD, deductions and required supporting documents: read for the personal allowance by year and the tertiary education cap | https://www.ird.gov.tt/individual/deductions-and-required-supporting-documents | 2026-11-14 |
| IRD, first-time employee page: read for the TD1, the 30 April assessment and 20% interest from 1 May | https://www.ird.gov.tt/first-time-employee | 2026-11-14 |
| IRD, public notice on the 2025 filing deadline: read in full for 2 November 2026 and the late filing penalties | https://www.ird.gov.tt/news/public-notice-self-employed-sole-traders-and-companies | 2026-11-14 |
| IRD, small business person page: read for wear and tear, the 25% non-emolument instalment test and the worked example | https://www.ird.gov.tt/small-business-person | 2026-11-14 |
| IRD, withholding tax page: read for the 30-day payment rule | https://www.ird.gov.tt/withholding-tax | 2026-11-14 |
| Ministry of Finance, Budget Statement FY2026 (13 October 2025): read for revenue measures; no change to the personal allowance found | https://www.finance.gov.tt/wp-content/uploads/2025/10/Budget-Statement-FY-2026-2.pdf | 2026-11-14 |

Not yet confirmed: any Finance Act 2025 change for the 2026 year of income (the 2024 consolidation of the Act was the latest text read); the 183-day residence test the earlier version gave; the combined TT$60,000 cap on pension, annuity and NIS deductions; the first-time home owner allowance (earlier version: TT$30,000 a year for five years from 1 January 2023); the TT$360,000 business levy exemption for individuals (confirmed for companies in the Corporation Tax Act); the business levy exemption period for individuals (IRD says three years; the Corporation Tax Act says twelve months for companies).
