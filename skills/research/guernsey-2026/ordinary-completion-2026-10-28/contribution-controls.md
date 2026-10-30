# Ordinary contribution method controls, 2026

These supplementary working papers test the new statutory methods without adding to the main Guide's two blocks. They are writer checks awaiting independent review. Every classification, relevant-income inclusion, certificate and period gate in the [payroll Guide](../../../international/guernsey/gg-payroll-social-insurance.md#current-statutory-class-2-and-class-3-method) must be established first. Amounts were selected so the weekly results have no fractional penny; no new rounding convention is assumed.

Sources read 28 October 2026: [Contributions Regulations rr10–11,37–38](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=268646), [Classification Regulations r2(1)(d)](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=270319), [Social Insurance Law ss6,8](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=253497), [Rates Ordinance 2025 ss1–6,13](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=262506), and [Income Tax Law ss148,209](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=253819).

## Current-year ordinary Class 2 base

Assume ordinary self-employed status throughout 52 contribution weeks, an accepted income-related certificate, no authority substitute-income determination, no other earned income, and no mixed-class or low-profit-floor adjustment. Revenue £100,000 less £45,000 deductible cash costs and £8,000 book depreciation gives £47,000 book profit. Add back that depreciation and deduct £9,000 statutory capital allowances, established under the income Guide's method, to obtain £46,000 tax-assessed business income. An additional £6,000 past-service pension included in assessable earned income brings regulation 10 relevant income to £52,000. It is not automatically business profit alone. No personal income-tax allowance is deducted. The accepted weekly formula gives £124, or £6,448 over 52 weeks.

```oa-check
name: Guernsey Class 2 current-year relevant-income bridge 2026
inputs:
  revenue: 100000
  deductible_cash_costs: 45000
  book_depreciation: 8000
  allowed_capital_allowances: 9000
  assessable_past_service_pension: 6000
  rate: 0.124
  contribution_weeks: 52
steps:
  - book_profit: revenue - deductible_cash_costs - book_depreciation
  - tax_business_income: book_profit + book_depreciation - allowed_capital_allowances
  - relevant_income: tax_business_income + assessable_past_service_pension
  - weekly_contribution: relevant_income * rate / 52
  - period_contribution: weekly_contribution * contribution_weeks
expected:
  book_profit: 47000
  tax_business_income: 46000
  relevant_income: 52000
  weekly_contribution: 124
  period_contribution: 6448
```

## Simultaneous Class 1 and Class 2 annual ceiling

Assume the same-week and annual gates of classification regulation 2(1)(d) hold, employment earnings are £144,560 and regulation 10 relevant self-employed earnings are £60,000 for the full year. Employment earnings are below £196,560; self-employed earnings exceed £9,984. Class 2 uses the £52,000 remaining annual headroom, giving £6,448. Class 1 payroll and any annual refund remain separate; employer contributions do not reduce this base. Regulation 37 makes the Class 2 assessment annual in arrears, payable on receipt of the account.

```oa-check
name: Guernsey simultaneous employment and self-employment cap 2026
inputs:
  employment_earnings: 144560
  relevant_self_employed_earnings: 60000
  annual_upper_limit: 196560
  class_2_rate: 0.124
steps:
  - remaining_headroom: max(0, annual_upper_limit - employment_earnings)
  - class_2_base: min(relevant_self_employed_earnings, remaining_headroom)
  - class_2_liability: class_2_base * class_2_rate
  - excluded_from_class_2_base: relevant_self_employed_earnings - class_2_base
expected:
  remaining_headroom: 52000
  class_2_base: 52000
  class_2_liability: 6448
  excluded_from_class_2_base: 8000
```

## Class 3 source bridge, exception screen and age rates

Assume established Class 3 status, an accepted income-related certificate, current-year assessable occupational pension £10,000, bank interest £5,000 and taxable rental income £22,122. There is no contribution-paid employment income to exclude and no regulation 38(6) disregard. Relevant income is £37,122 before the separate £11,122 contribution allowance. The £12,162 excess over the lower income limit exceeds the £3,068 annual contribution calculated at the under-age rate, so this example does not meet regulation 38(7)'s small-excess condition. The weekly result is £59 below pension age or £19 at pensionable age. The over-age annual contribution is £988 and also below the £12,162 excess. These are alternative full-year age assumptions, not a mid-year pension-age transition.

```oa-check
name: Guernsey Class 3 actual source bridge and alternative age rates 2026
inputs:
  assessable_occupational_pension: 10000
  assessable_interest: 5000
  assessable_rental_income: 22122
  allowance: 11122
  lower_income_limit: 24960
  under_age_rate: 0.118
  pension_age_rate: 0.038
  weeks: 52
steps:
  - relevant_income: assessable_occupational_pension + assessable_interest + assessable_rental_income
  - post_allowance_base: relevant_income - allowance
  - lower_limit_excess: relevant_income - lower_income_limit
  - under_age_weekly: post_allowance_base * under_age_rate / 52
  - under_age_period: under_age_weekly * weeks
  - pension_age_weekly: post_allowance_base * pension_age_rate / 52
  - pension_age_period: pension_age_weekly * weeks
  - under_age_excess_over_potential_contribution: lower_limit_excess - under_age_period
expected:
  relevant_income: 37122
  post_allowance_base: 26000
  lower_limit_excess: 12162
  under_age_weekly: 59
  under_age_period: 3068
  pension_age_weekly: 19
  pension_age_period: 988
  under_age_excess_over_potential_contribution: 9094
```

## Approved partial period and separate full-year reassessment

For an already accepted Class 3 certificate of £59 per contribution week covering 26 weeks, the period amount is £1,534. This does not annualise a new entrant's actual six-month income or decide a regulation 11(1)(b) direction. Separately, assume a full-year Class 2 reassessment within both statutory time tests, from £52,000 to £78,000 relevant income, with 52 weeks at the same class and no additional direction. The weekly amount changes £124 to £186 and the additional contribution is £3,224, exceeding the £5 de minimis. The partial Class 3 and full-year Class 2 cases are different taxpayers.

```oa-check
name: Guernsey certified contribution periods and Class 2 reassessment difference 2026
inputs:
  accepted_class_3_weekly: 59
  accepted_class_3_weeks: 26
  class_2_old_relevant_income: 52000
  class_2_new_relevant_income: 78000
  class_2_rate: 0.124
  class_2_covered_weeks: 52
steps:
  - class_3_period: accepted_class_3_weekly * accepted_class_3_weeks
  - class_2_old_weekly: class_2_old_relevant_income * class_2_rate / 52
  - class_2_new_weekly: class_2_new_relevant_income * class_2_rate / 52
  - class_2_additional: (class_2_new_weekly - class_2_old_weekly) * class_2_covered_weeks
expected:
  class_3_period: 1534
  class_2_old_weekly: 124
  class_2_new_weekly: 186
  class_2_additional: 3224
```
