# Preserved individual controls

All five published controls are retained byte-exact here. Main Guide retains the ordinary withdrawal control and adds a rental-base/2026-transition computation. Accompanying substantive cap, penalty and protected-pension explanations remain in the main Guide.

```oa-check
name: Guernsey 2026 qualifying cap comparison
inputs:
  qualifying: 1000000
  other_included: 100000
  property: 20000
steps:
  - ordinary: (qualifying + other_included + property) * 0.20
  - qualifying_route: min(qualifying * 0.20, 160000) + (other_included + property) * 0.20
  - combined_route: min((qualifying + other_included) * 0.20, 320000) + property * 0.20
expected:
  ordinary: 224000
  qualifying_route: 184000
  combined_route: 224000
```

```oa-check
name: Guernsey 2026 combined cap leaves property tax outside
inputs:
  qualifying: 1000000
  other_included: 1000000
  property: 20000
steps:
  - ordinary: (qualifying + other_included + property) * 0.20
  - qualifying_route: min(qualifying * 0.20, 160000) + (other_included + property) * 0.20
  - combined_route: min((qualifying + other_included) * 0.20, 320000) + property * 0.20
expected:
  ordinary: 404000
  qualifying_route: 364000
  combined_route: 324000
```

```oa-check
name: Guernsey individual late return outside daily penalty grace
inputs:
  initial_penalty: 200
  daily_rate: 10
  confirmed_chargeable_days: 40
steps:
  - daily_penalty: confirmed_chargeable_days * daily_rate
  - unreduced_total: initial_penalty + daily_penalty
expected:
  daily_penalty: 400
  unreduced_total: 600
```

```oa-check
name: Guernsey 2026 personal allowance withdrawal
inputs:
  income: 100000
  threshold: 85000
  personal_allowance: 15200
steps:
  - withdrawal: max(0, (income - threshold) / 5)
  - retained_allowance: max(0, personal_allowance - withdrawal)
  - tax: max(0, income - retained_allowance) * 0.20
expected:
  withdrawal: 3000
  retained_allowance: 12200
  tax: 17560
```

```oa-check
name: Guernsey 2026 ordered relief withdrawal protects eligible pension portion
inputs:
  income: 200000
  threshold: 85000
  personal_allowance: 15200
  eligible_mortgage: 3500
  eligible_pension: 5000
  protected_pension_limit: 2500
steps:
  - withdrawal: max(0, (income - threshold) / 5)
  - personal_removed: min(personal_allowance, withdrawal)
  - remaining_withdrawal: withdrawal - personal_removed
  - mortgage_removed: min(eligible_mortgage, remaining_withdrawal)
  - pension_withdrawable: max(0, eligible_pension - protected_pension_limit)
  - pension_removed: min(pension_withdrawable, remaining_withdrawal - mortgage_removed)
  - retained_pension: eligible_pension - pension_removed
  - unused_withdrawal: remaining_withdrawal - mortgage_removed - pension_removed
  - tax: (income - retained_pension) * 0.20
expected:
  withdrawal: 23000
  personal_removed: 15200
  mortgage_removed: 3500
  pension_removed: 2500
  retained_pension: 2500
  unused_withdrawal: 1800
  tax: 39500
```
