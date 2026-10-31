# Preserved original corporate controls

The three original blocks below are unchanged; two other original controls remain in the Guide.

```oa-check
name: Andorra ordinary advance and annual balance
inputs:
  prior_liability: 18000
  advance_rate: 0.50
  current_liability: 22000
steps:
  advance: prior_liability * advance_rate
  final_balance: current_liability - advance
expected:
  advance: 9000
  final_balance: 13000
```

```oa-check
name: Andorra advance excess reconciliation
inputs:
  prior_liability: 20000
  advance_rate: 0.50
  current_liability: 6000
steps:
  paid_advance: prior_liability * advance_rate
  final_balance: current_liability - paid_advance
  excess: paid_advance - current_liability
expected:
  paid_advance: 10000
  final_balance: -4000
  excess: 4000
```

```oa-check
name: Andorra eligible intangible partial expenditure ratio
inputs:
  net_income: 100000
  qualifying_costs: 60000
  total_costs: 100000
  uplift: 1.30
  reduction_rate: 0.80
  general_rate: 0.10
steps:
  adjusted_numerator: min(qualifying_costs * uplift, total_costs)
  ratio: adjusted_numerator / total_costs
  reduction: net_income * reduction_rate * ratio
  remaining_base: net_income - reduction
  tax_before_other_adjustments: remaining_base * general_rate
expected:
  adjusted_numerator: 78000
  ratio: 0.78
  reduction: 62400
  remaining_base: 37600
  tax_before_other_adjustments: 3760
```
