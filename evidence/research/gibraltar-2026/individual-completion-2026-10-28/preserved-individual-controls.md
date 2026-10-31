# Preserved individual calculation controls

Original v0.9 controls, retained byte-exact. They support the matching full prose and assumptions retained in the Guide; they do not establish final assessments.

## Original supplementary control 1

```oa-check
name: Health insurance deduction cap and non-resident month reduction
inputs:
  eligible_abs_premiums: 6000
  abs_cap: 5395
  otherwise_eligible_gibs_deduction: 3000
  smaller_eligible_deduction: 2400
  complete_nonresident_months: 3
steps:
  - full_year_abs: min(eligible_abs_premiums, abs_cap)
  - part_year_gibs: otherwise_eligible_gibs_deduction * (12 - complete_nonresident_months) / 12
  - part_year_smaller_deduction: smaller_eligible_deduction * (12 - complete_nonresident_months) / 12
expected:
  full_year_abs: 5395
  part_year_gibs: 2250
  part_year_smaller_deduction: 1800
```

## Original supplementary control 2

```oa-check
name: Low-income taper inside range and at upper endpoint
inputs:
  income: 17601
  upper_endpoint: 17822
  lower_reference: 17501
  full_relief: 64.40
steps:
  - relief: full_relief - 0.2 * (income - lower_reference)
  - endpoint_relief: full_relief - 0.2 * (upper_endpoint - lower_reference)
expected:
  relief: 44.40
  endpoint_relief: 0.20
```

## Original supplementary control 3

```oa-check
name: Individual payments on account and final reconciliation
inputs:
  preceding_relevant_liability: 6000
  higher_final_liability: 7500
  lower_final_liability: 5000
steps:
  - each_instalment: preceding_relevant_liability * 0.5
  - paid: each_instalment * 2
  - balance_due: max(0, higher_final_liability - paid)
  - overpayment: max(0, paid - lower_final_liability)
expected:
  each_instalment: 3000
  balance_due: 1500
  overpayment: 1000
```

## Original supplementary control 4

```oa-check
name: Gibraltar approved versus imported pension component
inputs:
  established_taxable_pension_component: 20000
steps:
  - section_14a_component_tax: established_taxable_pension_component * 0.025
  - qualifying_rule_3a_component_tax: established_taxable_pension_component * 0
expected:
  section_14a_component_tax: 500
  qualifying_rule_3a_component_tax: 0
```

## Original supplementary control 5

```oa-check
name: Gibraltar specified deduction reduction after death
inputs:
  otherwise_allowable_annual_deduction: 6000
  complete_months_october_case: 8
  complete_months_june_case: 0
steps:
  - october_reduction: otherwise_allowable_annual_deduction * complete_months_october_case / 12
  - october_remaining: otherwise_allowable_annual_deduction - october_reduction
  - june_reduction: otherwise_allowable_annual_deduction * complete_months_june_case / 12
expected:
  october_reduction: 4000
  october_remaining: 2000
  june_reduction: 0
```

## Original supplementary control 6

```oa-check
name: Non-resident pensioner worldwide-income relief floor
inputs:
  worldwide_income: 50000
  chargeable_income: 20000
  hypothetical_worldwide_tax: 10000
  liability_below_floor: 3000
  liability_above_floor: 5000
steps:
  - floor: hypothetical_worldwide_tax * chargeable_income / worldwide_income
  - restriction_below: max(0, floor - liability_below_floor)
  - restricted_liability: liability_below_floor + restriction_below
  - restriction_above: max(0, floor - liability_above_floor)
expected:
  floor: 4000
  restriction_below: 1000
  restricted_liability: 4000
  restriction_above: 0
```
