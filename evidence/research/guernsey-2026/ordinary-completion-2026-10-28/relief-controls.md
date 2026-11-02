# Domestic foreign-tax relief controls

Sources read 28 October 2026: [Income Tax Law sections 173 and 176](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=253819), complete operative text. All income/tax inputs are assumed independently established; both illustrations avoid excess foreign-tax deductions and underlying-tax adjustments. No treaty entitlement, actual rate or current claim form is inferred. Pending fresh independent review.

```oa-check
name: Guernsey domestic treaty-credit effective-rate ceiling without excess tax
inputs:
  total_guernsey_income: 100000
  total_precredit_tax: 10000
  eligible_foreign_income: 20000
  eligible_foreign_tax: 1500
steps:
  - effective_rate: total_precredit_tax / total_guernsey_income
  - same_income_ceiling: eligible_foreign_income * effective_rate
  - credit: min(eligible_foreign_tax, same_income_ceiling, total_precredit_tax)
  - total_residual_tax: total_precredit_tax - credit
expected:
  effective_rate: 0.1
  same_income_ceiling: 2000
  credit: 1500
  total_residual_tax: 8500
```

```oa-check
name: Guernsey unilateral relief ordinary no-excess case
inputs:
  total_guernsey_income: 100000
  total_prerelief_tax: 10000
  eligible_foreign_income: 10000
  foreign_effective_rate: 0.05
steps:
  - guernsey_effective_rate: total_prerelief_tax / total_guernsey_income
  - three_quarters_ceiling: guernsey_effective_rate * 0.75
  - relief_rate: min(foreign_effective_rate, three_quarters_ceiling)
  - relief: eligible_foreign_income * relief_rate
expected:
  guernsey_effective_rate: 0.1
  three_quarters_ceiling: 0.075
  relief_rate: 0.05
  relief: 500
```
