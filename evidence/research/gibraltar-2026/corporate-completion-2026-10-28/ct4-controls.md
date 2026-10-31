# Gibraltar CT4 forecast controls

Writer-only arithmetic on assumed established liabilities, not a deemed approval or surcharge assessment. Both controls preserve the Commissioner decision and period-allocation boundary.

```oa-check
name: CT4 each-payment amount is half the forecast not half the reduction
inputs:
  verified_original_basis_liability: 24000
  reasonable_period_forecast: 10000
  assumed_final_liability: 14000
steps:
  - original_each: verified_original_basis_liability * 0.5
  - requested_each: reasonable_period_forecast * 0.5
  - proposed_total: requested_each * 2
  - proposed_total_reduction: verified_original_basis_liability - proposed_total
  - remaining_before_surcharge_reconciliation: assumed_final_liability - proposed_total
expected:
  original_each: 12000
  requested_each: 5000
  proposed_total: 10000
  proposed_total_reduction: 14000
  remaining_before_surcharge_reconciliation: 4000
```

```oa-check
name: CT4 zero forecast is a request for discharge
inputs:
  reasonable_period_forecast: 0
steps:
  - requested_each: reasonable_period_forecast * 0.5
expected:
  requested_each: 0
```
