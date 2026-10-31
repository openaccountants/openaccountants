# Retained original corporate controls

All four predecessor blocks are byte-identical. Writer preservation only; applicability and independent review remain pending.

```oa-check
name: Liechtenstein assumed corporate equity and loss bridge
inputs:
  book_profit_before_tax: 100000
  established_addbacks: 5000
  established_modified_equity: 500000
  equity_reference_rate: 0.04
  assessed_opening_losses: 60000
  ordinary_loss_fraction: 0.70
  tax_rate: 0.125
  applicable_minimum: 1800
steps:
  profit_before_equity: book_profit_before_tax + established_addbacks
  equity_deduction: min(profit_before_equity, established_modified_equity * equity_reference_rate)
  profit_before_losses: profit_before_equity - equity_deduction
  losses_used: min(assessed_opening_losses, profit_before_losses * ordinary_loss_fraction)
  taxable_profit: profit_before_losses - losses_used
  ordinary_tax: taxable_profit * tax_rate
  income_tax_with_minimum: max(ordinary_tax, applicable_minimum)
  closing_loss_balance: assessed_opening_losses - losses_used
expected:
  profit_before_equity: 105000
  equity_deduction: 20000
  profit_before_losses: 85000
  losses_used: 59500
  taxable_profit: 25500
  ordinary_tax: 3187.50
  income_tax_with_minimum: 3187.50
  closing_loss_balance: 500
```

```oa-check
name: Liechtenstein assumed applicable minimum tax comparison
inputs:
  established_taxable_profit: 10000
  tax_rate: 0.125
  applicable_minimum: 1800
steps:
  ordinary_tax: established_taxable_profit * tax_rate
  resulting_income_tax: max(ordinary_tax, applicable_minimum)
  increase_due_to_minimum: resulting_income_tax - ordinary_tax
expected:
  ordinary_tax: 1250
  resulting_income_tax: 1800
  increase_due_to_minimum: 550
```

```oa-check
name: Liechtenstein assumed equity deduction no new loss
inputs:
  established_profit_before_equity: 10000
  established_modified_equity: 500000
  reference_rate: 0.04
steps:
  raw_equity_amount: established_modified_equity * reference_rate
  allowed_equity_deduction: min(established_profit_before_equity, raw_equity_amount)
  profit_after_equity: established_profit_before_equity - allowed_equity_deduction
expected:
  raw_equity_amount: 20000
  allowed_equity_deduction: 10000
  profit_after_equity: 0
```

```oa-check
name: Liechtenstein assumed three year minimum tax balance screen
inputs:
  first_balance: 400000
  second_balance: 500000
  third_balance: 600000
  years: 3
  statutory_limit: 500000
steps:
  three_year_average: (first_balance + second_balance + third_balance) / years
  remaining_limit: statutory_limit - three_year_average
expected:
  three_year_average: 500000
  remaining_limit: 0
```
