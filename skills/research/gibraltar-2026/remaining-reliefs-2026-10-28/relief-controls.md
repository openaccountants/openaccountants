# Assumed certified relief calculations, unreviewed additions

These scenarios assume the stated statutory eligibility, recognised expenditure, actual certification and claim period. Amounts are deductions from income, not tax refunds. The source ledger records scope/conditions; GIBS interaction remains outside these computations.

```oa-check
name: Solar installation aggregate cap and two-year joint allocation
inputs:
  qualifying_cost: 8000
  aggregate_cap: 6000
  assessment_years: 2
  first_share: 0.60
  second_share: 0.40
steps:
  - total_deduction: min(qualifying_cost, aggregate_cap)
  - each_year: total_deduction / assessment_years
  - first_claimant_each_year: each_year * first_share
  - second_claimant_each_year: each_year * second_share
expected:
  total_deduction: 6000
  each_year: 3000
  first_claimant_each_year: 1800
  second_claimant_each_year: 1200
```

```oa-check
name: Performance improvement to rating D including EPC cost
inputs:
  qualifying_work: 10000
  EPC_cost: 200
  achieved_D_rate: 0.30
steps:
  - evidenced_total: qualifying_work + EPC_cost
  - income_deduction: evidenced_total * achieved_D_rate
expected:
  evidenced_total: 10200
  income_deduction: 3060
```

```oa-check
name: EV charger aggregate cap and agreed allocation
inputs:
  qualifying_cost: 2800
  aggregate_cap: 2000
  first_share: 0.75
  second_share: 0.25
steps:
  - deduction: min(qualifying_cost, aggregate_cap)
  - first_claimant: deduction * first_share
  - second_claimant: deduction * second_share
expected:
  deduction: 2000
  first_claimant: 1500
  second_claimant: 500
```

```oa-check
name: Disabled business access cost cap, eligibility assumed
inputs:
  qualifying_cost: 18000
  aggregate_cap: 15000
steps:
  - income_deduction: min(qualifying_cost, aggregate_cap)
expected:
  income_deduction: 15000
```
