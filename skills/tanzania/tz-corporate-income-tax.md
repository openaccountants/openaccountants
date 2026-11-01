---
name: tz-corporate-income-tax
description: >
  Tanzania corporate income tax for the 2026 year of income: the 30% rate, reduced rates, the 1% turnover tax on perpetual losses, loss limits, interest limits, deemed distributions, instalments and the final return under the Income Tax Act Cap. 332 and the Finance Act 2026. Use for company tax, corporation tax, TRA provisional return, or final return questions for Tanzanian companies and branches.
jurisdiction: TZ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 0.1
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tanzania corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Corporations, trusts, unapproved retirement funds and domestic permanent establishments of non-residents pay tax on total income (First Schedule para 3(1)). TRA lists limited companies, clubs, co-operatives, charities, political parties and branches as liable; partnerships are not taxed, their partners are ([TRA corporation tax](https://www.tra.go.tz/page/corporation-tax)). A corporation is resident if incorporated or formed under Tanzanian law, or if its management and control are exercised in Tanzania at any time in the year (ITA s.86(4)); a resident is taxed on worldwide income, a non-resident only on Tanzanian-source income (s.6(1)). The year of income is the calendar year unless the Commissioner approves another 12-month period ([TRA](https://www.tra.go.tz/page/corporation-tax)).

Out of scope: individuals (see [Income tax](tanzania-income-tax.md)), mining and petroleum ring-fencing beyond the rate, and VAT. The Income Tax Act is a Union law; the Minister may set a separate rate for Zanzibar for individuals (First Schedule para 1(7)), and this skill does not cover any Zanzibar variation.

## Rates, bands and thresholds

| Item | Figure | Condition | Tax year | Source |
|---|---|---|---|---|
| Standard rate | 30% | Total income of a corporation or domestic permanent establishment | 2026 | [ITA First Sch para 3(1)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Mining or petroleum income | 30% | Income from mining or petroleum operations | 2026 | [ITA First Sch para 1(5), (6)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Newly listed company | 25% | Listed on the Dar es Salaam Stock Exchange with at least 25% of equity issued to the public; three consecutive years from listing. The float was 30% before the Finance Act 2025 | 2026 | [FA 2025 s.60(d)(i)](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf) |
| New vehicle, tractor, boat or outboard engine assembly plant | 10% | Newly established plant with a performance agreement; five consecutive years from start of production | 2026 | [ITA First Sch para 3(2)(b)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| New pharmaceutical or leather manufacturer | 20% | Performance agreement; five consecutive years from start of production | 2026 | [ITA First Sch para 3(2)(c)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Turnover tax on perpetual loss | 1% of turnover of the third year | Perpetual unrelieved loss for three consecutive years. Not for agricultural, health or education corporations (tea processing: 1 July 2024 to 30 June 2027 only) | 2026 | [FA 2025 s.60(d)(ii)](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf); [FA 2024 s.34](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf) |
| Repatriated income of a branch | 10% | On top of the 30% | 2026 | [ITA First Sch para 3(4)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Loss relief limit | Income cannot fall below 40% of income before losses | Applies where the company has chargeable income and unrelieved losses for the four previous consecutive years; not agricultural, health or education corporations | 2026 | [ITA s.19(2)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf); [FA 2024 s.36](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf) |
| Interest limit | Debt-to-equity 7 to 3 | Exempt-controlled resident entity: 25% or more of underlying ownership held by non-residents or exempt persons | 2026 | [ITA s.12(2), (3)](https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf) |
| Deemed distribution | 15% of profit | No distribution within 12 months after year end. Was 30% until the Finance Act 2026 (from 1 July 2026) | 2026 | [FA 2026 s.22](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf) |
| Certified return | Gross income above TZS 100,000,000 | Return prepared or certified by a CPA in public practice | 2026 | [FA 2025 s.59](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf) |

## The base

1. Start from business and investment income; a resident includes foreign income (s.6(1)).
2. Deduct expenditure incurred wholly and exclusively in producing income (s.11(2)). It must be supported by a fiscal receipt unless the supplier is a non-resident without a permanent establishment or is excluded from issuing one (s.11(4), [FA 2024 s.35](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf)).
3. Apply the interest limit if the company is exempt-controlled (s.12(2)). Equity includes paid-up capital and, since the Finance Act 2025, positive retained earnings ([FA 2025 s.48](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf)).
4. Deduct losses (s.19). Foreign, investment, agricultural and speculative losses only offset the same class of income (s.19).
5. A change of more than 50% in underlying ownership against any time in the previous three years treats assets as realised and stops pre-change losses (s.56(1), (2)).
6. Deemed distribution: where no distribution is made for the year within 12 months after its end, the Commissioner may treat 15% of profit as distributed, and withholding tax follows. This does not apply to entities covered by s.96(6), companies listed on the DSE, banks and financial institutions, insurers, and mining companies with a Framework Agreement ([FA 2026 s.22](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf)). A later real distribution of that amount carries no further withholding ([FA 2025 s.49](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf)).

## Deadlines and filing

1. **TIN:** apply within 15 days of starting the activity (TAA s.22(1), [FA 2026 s.72](https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf)).
2. **Estimate and instalments:** file the statement of estimated tax payable and pay the first instalment by the end of the third month of the year. Pay the rest at the end of months 6, 9 and 12: 31 March, 30 June, 30 September and 31 December for a calendar year (ITA s.113(2), [TRA](https://www.tra.go.tz/page/corporation-tax)).
3. **Final return:** file within six months after year end (ITA s.117(1)), and pay the balance by the same date ([TRA](https://www.tra.go.tz/page/corporation-tax)). A company audited by the Controller and Auditor General has nine months ([FA 2024 s.44](https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf)). A return is due even with no taxable income ([TRA](https://www.tra.go.tz/page/corporation-tax)).
4. **Portal:** TRA's taxpayer portal, https://taxpayerportal.tra.go.tz/. Not yet confirmed: the current form numbers and boxes of the corporate return; we did not find an official page for that exact task, so do not quote any.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late filing or payment | Per month or part: 2.5% of the unpaid tax, or 15 currency points for a body corporate (TZS 225,000), whichever is higher | [TAA s.89](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf) |
| Currency point | TZS 15,000 | [TAA First Schedule](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf) |
| Late payment interest | Statutory rate, compounded monthly. The statutory rate is the Bank of Tanzania prevailing discount rate; the 2026 figure is unverified | [TAA s.87(1), s.3](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf) |
| Under-estimating instalments | Interest where the estimate is below 80% of the correct amount | [TAA s.86(3)](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf) |
| Failing to keep documents | 10 currency points a month for a body corporate | [TAA s.88(2)](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf) |
| False statement | 50% of the shortfall; 75% if knowing or reckless | [TAA s.90(2)](https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf) |

## Cross-border points

Branch profits, withholding on payments abroad, treaty limits and gains on foreign sales sit in [Cross-border](tz-cross-border.md). Related-party pricing sits in [Transfer pricing](tz-transfer-pricing.md). Foreign tax on foreign income is creditable up to the Tanzanian average rate on that income (ITA s.98).

## Two worked examples that recompute

**Example 1: profit with old losses.** A company has income of TZS 800,000,000 before losses, TZS 600,000,000 of unrelieved losses and losses in each of the four previous years. Income cannot fall below 40%, so it uses TZS 480,000,000 of losses, pays tax on TZS 320,000,000 and carries TZS 120,000,000 forward.

```oa-check
name: Loss limit, income TZS 800m, losses TZS 600m
inputs:
  income: 800000000
  losses: 600000000
steps:
  - floor_income: income * 0.40
  - used: min(losses, income - floor_income)
  - taxable: income - used
  - tax: taxable * 0.30
  - carried: losses - used
expected:
  tax: 96000000
  carried: 120000000
```

**Example 2: distribute, or take the deemed distribution?** A non-listed resident company has profit of TZS 1,000,000,000 and no distribution for 2026. If the Commissioner applies s.33A, TZS 150,000,000 is treated as distributed and 10% withholding applies, so TZS 15,000,000 is due. If the company really distributes TZS 150,000,000 within the 12 months the tax is the same, but the cash reaches the shareholders. If the shareholder is a resident company holding 25% or more of shares and votes, the real dividend carries 5%, so TZS 7,500,000.

```oa-check
name: Deemed distribution at 15 percent, then 10 percent withholding
inputs:
  profit: 1000000000
steps:
  - deemed: profit * 0.15
  - wht_other: deemed * 0.10
  - wht_group: deemed * 0.05
expected:
  wht_other: 15000000
  wht_group: 7500000
```

## Ask the client first

1. Is the entity resident, or a branch of a non-resident?
2. What is the year of income, and has TRA approved a non-calendar year?
3. Are there losses for the four previous years, and in which class of income?
4. What is the sector: agriculture, health, education, mining, petroleum, listed, or performance-agreement manufacturer?
5. Who owns it? Is 25% or more held by non-residents or exempt persons, and has ownership moved by more than 50% in three years?
6. Was a dividend paid for the year, and what is gross income for the CPA test?

## Sources

All read on 2026-11-01. Quotes are saved in the Africa sources file.

| Source | Link | Read |
|---|---|---|
| Income Tax Act Cap. 332 R.E. 2023 | https://www.tra.go.tz/images/uploads/acts/The_Income_Tax_Act.pdf | 2026-11-01, ss.3, 6, 11, 12, 19, 33, 56, 86, 89, 92, 93, 98, 105 to 117, First Sch |
| Finance Act 2026, No. 2, in force 1 July 2026 | https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2026.pdf | 2026-11-01, Parts IX, XXI, XXVI |
| Finance Act 2025, No. 11 | https://www.tra.go.tz/images/uploads/acts/THE_FINANCE_ACT%2C_2025.pdf | 2026-11-01, Income Tax Part, ss.47 to 61 |
| Finance Act 2024, No. 6 | https://www.tra.go.tz/images/uploads/acts/Finance_Act_2024_%281%29.pdf | 2026-11-01, Income Tax Part, ss.33 to 47 |
| Tax Administration Act Cap. 438 R.E. 2023 | https://www.tra.go.tz/images/uploads/acts/Tax_Administration_Act.pdf | 2026-11-01, ss.86 to 90, First Sch |
| TRA, Corporation Tax | https://www.tra.go.tz/page/corporation-tax | 2026-11-01, whole page |

Not yet confirmed: the 2026 statutory interest rate figure; current form numbers and boxes of the corporate return.
