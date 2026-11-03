# Supplementary Part V controls: local unreviewed writer candidate

These arithmetic controls use the explicit scope and independently established group-floor assumptions in the Guide. They do not prove scope, group allocation, currency conversion, exemption eligibility or a final tax liability.

```oa-check
name: Gibraltar Part V floor exceeds EBITDA limb
inputs:
  exceeding_costs: 4000000
  tax_ebitda: 6000000
  established_applicable_group_floor: 3000000
steps:
  - ebitda_limb: tax_ebitda * 0.30
  - ordinary_limit: max(ebitda_limb, established_applicable_group_floor)
  - deductible_under_part_v: min(exceeding_costs, ordinary_limit)
  - disallowed_costs_carried: exceeding_costs - deductible_under_part_v
expected:
  ebitda_limb: 1800000
  ordinary_limit: 3000000
  deductible_under_part_v: 3000000
  disallowed_costs_carried: 1000000
```

```oa-check
name: Gibraltar Part V equal EBITDA and floor boundary
inputs:
  exceeding_costs: 3000000
  tax_ebitda: 10000000
  established_applicable_group_floor: 3000000
steps:
  - ebitda_limb: tax_ebitda * 0.30
  - ordinary_limit: max(ebitda_limb, established_applicable_group_floor)
  - deductible_under_part_v: min(exceeding_costs, ordinary_limit)
  - disallowed_costs: exceeding_costs - deductible_under_part_v
expected:
  ebitda_limb: 3000000
  ordinary_limit: 3000000
  deductible_under_part_v: 3000000
  disallowed_costs: 0
```
