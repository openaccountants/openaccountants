# Retained original individual-income controls

All5 predecessor blocks are byte-identical. Independent legal review remains pending.

```oa-check
name: Liechtenstein assumed full-year single minimum-income screen
inputs:
  statutory_monthly_gross_minimum: 2100
  months_in_full_year: 12
  established_total_article_14_income: 24000
steps:
  annual_gross_minimum: statutory_monthly_gross_minimum * months_in_full_year
  income_below_minimum: annual_gross_minimum - established_total_article_14_income
expected:
  annual_gross_minimum: 25200
  income_below_minimum: 1200
```

```oa-check
name: Liechtenstein assumed ordinary tax with deemed wealth yield
inputs:
  established_other_taxable_income: 80000
  established_taxable_net_wealth: 500000
  statutory_yield: 0.04
  selected_state_rate: 0.05
  selected_fixed_subtraction: 1744
  assumed_verified_municipality_surcharge: 1.50
steps:
  deemed_wealth_income: established_taxable_net_wealth * statutory_yield
  combined_taxable_income: established_other_taxable_income + deemed_wealth_income
  state_tax: combined_taxable_income * selected_state_rate - selected_fixed_subtraction
  municipality_tax: state_tax * assumed_verified_municipality_surcharge
  combined_tax_before_credits: state_tax + municipality_tax
expected:
  deemed_wealth_income: 20000
  combined_taxable_income: 100000
  state_tax: 3256
  municipality_tax: 4884
  combined_tax_before_credits: 8140
```

```oa-check
name: Liechtenstein assumed joint state formula and municipality tax
inputs:
  established_joint_taxable_income: 200000
  selected_state_rate: 0.05
  selected_fixed_subtraction: 3488
  assumed_verified_municipality_surcharge: 1.80
steps:
  state_tax: established_joint_taxable_income * selected_state_rate - selected_fixed_subtraction
  municipality_tax: state_tax * assumed_verified_municipality_surcharge
  combined_tax_before_credits: state_tax + municipality_tax
expected:
  state_tax: 6512
  municipality_tax: 11721.60
  combined_tax_before_credits: 18233.60
```

```oa-check
name: Liechtenstein assumed qualifying single parent formula
inputs:
  established_taxable_income: 150000
  selected_state_rate: 0.05
  selected_fixed_subtraction: 2616
  assumed_verified_municipality_surcharge: 2
steps:
  state_tax: established_taxable_income * selected_state_rate - selected_fixed_subtraction
  municipality_tax: state_tax * assumed_verified_municipality_surcharge
  combined_tax_before_credits: state_tax + municipality_tax
expected:
  state_tax: 4884
  municipality_tax: 9768
  combined_tax_before_credits: 14652
```

```oa-check
name: Liechtenstein assumed ordinary individual business loss cap
inputs:
  established_relevant_positive_income: 100000
  established_opening_unused_losses: 90000
  statutory_use_fraction: 0.70
steps:
  ordinary_loss_limit: established_relevant_positive_income * statutory_use_fraction
  losses_used: min(established_opening_unused_losses, ordinary_loss_limit)
  relevant_income_after_loss: established_relevant_positive_income - losses_used
  losses_remaining: established_opening_unused_losses - losses_used
expected:
  ordinary_loss_limit: 70000
  losses_used: 70000
  relevant_income_after_loss: 30000
  losses_remaining: 20000
```
