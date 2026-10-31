# Original Guernsey regression controls

All 32 published a23757a2 oa-check blocks, retained byte-exact. These supplement the two main controls in each current computational Guide. All original explanatory prose is also preserved in original/*.txt and retained or specifically reconciled in the main Guides.

## gg-company-accounts-and-reporting.txt, control 1

```oa-check
name: Guernsey September 2026 multiple late changes are separate breaches
inputs:
  director_changes: 2
  director_penalty: 90
  resident_agent_changes: 1
  resident_agent_penalty: 250
steps:
  - total_penalty: director_changes * director_penalty + resident_agent_changes * resident_agent_penalty
expected:
  total_penalty: 430
```

## gg-corporate-tax-substance.txt, control 1

```oa-check
name: Guernsey established corporate income streams
inputs:
  standard_income: 100000
  intermediate_income: 30000
  rental_income: 20000
steps:
  - standard_tax: standard_income * 0
  - intermediate_tax: intermediate_income * 0.10
  - rental_tax: rental_income * 0.20
  - total_tax: standard_tax + intermediate_tax + rental_tax
expected:
  standard_tax: 0
  intermediate_tax: 3000
  rental_tax: 4000
  total_tax: 7000
```

## gg-corporate-tax-substance.txt, control 2

```oa-check
name: Guernsey corporate daily penalty after concession period
inputs:
  initial_penalty: 300
  daily_rate: 50
  established_chargeable_days: 35
steps:
  - daily_penalty: daily_rate * established_chargeable_days
  - total_penalty: initial_penalty + daily_penalty
expected:
  daily_penalty: 1750
  total_penalty: 2050
```

## gg-gst-transition.txt, control 1

```oa-check
name: Guernsey planned GST exclusive-price scenario, not current liability
inputs:
  net_price: 1000
  assumed_rate: 0.03
steps:
  - hypothetical_gst: net_price * assumed_rate
  - gross_price: net_price + hypothetical_gst
expected:
  hypothetical_gst: 30
  gross_price: 1030
```

## gg-gst-transition.txt, control 2

```oa-check
name: Guernsey planned GST fixed-inclusive-price scenario
inputs:
  fixed_total: 1000
  assumed_rate: 0.03
steps:
  - net_price: round(fixed_total / (1 + assumed_rate), 2)
  - hypothetical_gst: fixed_total - net_price
expected:
  net_price: 970.87
  hypothetical_gst: 29.13
```

## gg-individual-income-tax.txt, control 1

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

## gg-individual-income-tax.txt, control 2

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

## gg-individual-income-tax.txt, control 3

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

## gg-individual-income-tax.txt, control 4

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

## gg-individual-income-tax.txt, control 5

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

## gg-payroll-social-insurance.txt, control 1

```oa-check
name: Guernsey Class 3 allowance applies after exemption test
inputs:
  established_income: 24960
  lower_limit: 24960
  non_employed_allowance: 11122
  rate: 0.118
steps:
  - margin_above_lower: established_income - lower_limit
  - assessment_base: established_income - non_employed_allowance
  - annual_rate_arithmetic: assessment_base * rate
expected:
  margin_above_lower: 0
  assessment_base: 13838
  annual_rate_arithmetic: 1632.884
```

## gg-payroll-social-insurance.txt, control 2

```oa-check
name: Guernsey ordinary monthly Class 1 contributions 2026
inputs:
  gross: 3000
  cap: 16380
  employee_rate: 0.075
  employer_rate: 0.071
steps:
  - base: min(gross, cap)
  - employee_si: round(base * employee_rate, 2)
  - employer_si: round(base * employer_rate, 2)
  - employer_cost: gross + employer_si
expected:
  employee_si: 225
  employer_si: 213
  employer_cost: 3213
```

## gg-payroll-social-insurance.txt, control 3

```oa-check
name: Guernsey monthly Class 1 upper cap 2026
inputs:
  gross: 20000
  cap: 16380
  employee_rate: 0.075
  employer_rate: 0.071
steps:
  - base: min(gross, cap)
  - employee_si: round(base * employee_rate, 2)
  - employer_si: round(base * employer_rate, 2)
expected:
  base: 16380
  employee_si: 1228.50
  employer_si: 1162.98
```

## gg-payroll-social-insurance.txt, control 4

```oa-check
name: Guernsey eligible recurring benefit with annual exemption
inputs:
  monthly_cost: 100
  annual_exemption: 900
  months: 12
steps:
  - monthly_exemption: annual_exemption / months
  - monthly_taxable_benefit: max(0, monthly_cost - monthly_exemption)
  - annual_taxable_benefit: monthly_taxable_benefit * months
expected:
  monthly_exemption: 75
  monthly_taxable_benefit: 25
  annual_taxable_benefit: 300
```

## gg-payroll-social-insurance.txt, control 5

```oa-check
name: Guernsey employer-paid income tax on benefit
inputs:
  taxable_benefit: 5000
  tax_rate: 0.20
steps:
  - grossed_income: taxable_benefit / (1 - tax_rate)
  - tax_reimbursement: grossed_income - taxable_benefit
  - total_tax: grossed_income * tax_rate
  - after_tax_value: grossed_income - total_tax
expected:
  grossed_income: 6250
  tax_reimbursement: 1250
  total_tax: 1250
  after_tax_value: 5000
```

## gg-payroll-social-insurance.txt, control 6

```oa-check
name: Guernsey ordinary car benefit cost includes trade-in value
inputs:
  gross_car_cost: 30000
  extras: 3000
  employee_extras_payment: 2000
  benefit_rate: 0.20
steps:
  - benefit_cost: gross_car_cost + extras - employee_extras_payment
  - annual_benefit: benefit_cost * benefit_rate
expected:
  benefit_cost: 31000
  annual_benefit: 6200
```

## gg-payroll-social-insurance.txt, control 7

```oa-check
name: Guernsey car business-use strict percentage boundary
inputs:
  total_miles: 10000
  boundary_business_miles: 7500
  above_business_miles: 7510
  gross_cost: 30000
steps:
  - boundary_percent: boundary_business_miles / total_miles * 100
  - above_percent: above_business_miles / total_miles * 100
  - ordinary_benefit: gross_cost * 0.20
expected:
  boundary_percent: 75
  above_percent: 75.1
  ordinary_benefit: 6000
```

## gg-payroll-social-insurance.txt, control 8

```oa-check
name: Guernsey furnished accommodation with valid rental-value election
inputs:
  established_emoluments: 40000
  furnished_rate: 0.175
  verified_rental_value: 6000
steps:
  - percentage_benefit: established_emoluments * furnished_rate
  - benefit_with_valid_election: min(percentage_benefit, verified_rental_value)
expected:
  percentage_benefit: 7000
  benefit_with_valid_election: 6000
```

## gg-property-document-duty.txt, control 1

```oa-check
name: Guernsey 600000 realty ordinary and qualified downsizing
inputs:
  realty: 600000
steps:
  - first_slice: 300000 * 0.0225
  - second_slice: 200000 * 0.035
  - third_slice: (realty - 500000) * 0.04
  - ordinary_duty: first_slice + second_slice + third_slice
  - qualified_relief: first_slice + second_slice
  - qualified_net_duty: ordinary_duty - qualified_relief
expected:
  ordinary_duty: 17750
  qualified_relief: 13750
  qualified_net_duty: 4000
```

## gg-property-document-duty.txt, control 2

```oa-check
name: Guernsey six million realty official cross-check
inputs:
  realty: 6000000
steps:
  - band1: 300000 * 0.0225
  - band2: 200000 * 0.035
  - band3: 450000 * 0.04
  - band4: 300000 * 0.0425
  - band5: 1250000 * 0.045
  - band6: 2500000 * 0.055
  - band7: (realty - 5000000) * 0.07
  - duty: band1 + band2 + band3 + band4 + band5 + band6 + band7
expected:
  duty: 308250
```

## gg-property-document-duty.txt, control 3

```oa-check
name: Guernsey document duty 500000 boundary
inputs:
  additional_value: 100
steps:
  - boundary_duty: 300000 * 0.0225 + 200000 * 0.035
  - additional_duty: additional_value * 0.04
  - above_boundary_duty: boundary_duty + additional_duty
expected:
  boundary_duty: 13750
  additional_duty: 4
  above_boundary_duty: 13754
```

## gg-secondary-pensions.txt, control 1

```oa-check
name: Guernsey 2026 minimum secondary pension ordinary month
inputs:
  qualifying_earnings: 3000
  monthly_cap: 16380
  employer_rate: 0.01
  employee_rate: 0.015
steps:
  - base: min(qualifying_earnings, monthly_cap)
  - employer_pension: round(base * employer_rate, 2)
  - employee_pension: round(base * employee_rate, 2)
  - combined_pension: employer_pension + employee_pension
expected:
  employer_pension: 30
  employee_pension: 45
  combined_pension: 75
```

## gg-secondary-pensions.txt, control 2

```oa-check
name: Guernsey 2026 secondary pension monthly cap
inputs:
  qualifying_earnings: 20000
  monthly_cap: 16380
  employer_rate: 0.01
  employee_rate: 0.015
steps:
  - base: min(qualifying_earnings, monthly_cap)
  - employer_pension: round(base * employer_rate, 2)
  - employee_pension: round(base * employee_rate, 2)
  - combined_pension: employer_pension + employee_pension
expected:
  base: 16380
  employer_pension: 163.80
  employee_pension: 245.70
  combined_pension: 409.50
```

## gg-uk-treaty-employment-and-relief.txt, control 1

```oa-check
name: PE anti-fragmentation ownership boundary
inputs:
  total_equal_interests: 100
  at_boundary: 50
  above_boundary: 51
steps:
  - boundary_percentage: at_boundary / total_equal_interests * 100
  - above_percentage: above_boundary / total_equal_interests * 100
expected:
  boundary_percentage: 50
  above_percentage: 51
```

## gg-uk-treaty-employment-and-relief.txt, control 2

```oa-check
name: Supported PE profit bridge before domestic tax
inputs:
  attributed_revenue: 200000
  established_allowable_costs: 130000
  supported_profit_adjustment: 10000
steps:
  - initial_profit: attributed_revenue - established_allowable_costs
  - revised_profit: initial_profit + supported_profit_adjustment
expected:
  initial_profit: 70000
  revised_profit: 80000
```

## gg-uk-treaty-employment-and-relief.txt, control 3

```oa-check
name: Property-income dividend treaty ceiling is not a minimum tax
inputs:
  gross_dividend: 10000
  ceiling_rate: 0.15
  higher_domestic_tax: 2000
  lower_domestic_tax: 1000
steps:
  - ceiling: gross_dividend * ceiling_rate
  - higher_case_tax: min(higher_domestic_tax, ceiling)
  - lower_case_tax: min(lower_domestic_tax, ceiling)
expected:
  ceiling: 1500
  higher_case_tax: 1500
  lower_case_tax: 1000
```

## gg-uk-treaty-employment-and-relief.txt, control 4

```oa-check
name: Non-resident ownership strict less-than boundary
inputs:
  total_equal_shares: 100
  below_boundary_shares: 24
  boundary_shares: 25
steps:
  - below_percentage: below_boundary_shares / total_equal_shares * 100
  - boundary_percentage: boundary_shares / total_equal_shares * 100
expected:
  below_percentage: 24
  boundary_percentage: 25
```

## gg-uk-treaty-employment-and-relief.txt, control 5

```oa-check
name: Associated-enterprise profit adjustment and excess interest
inputs:
  supported_service_price: 120000
  actual_service_price: 90000
  actual_interest: 50000
  supported_independent_interest: 40000
steps:
  - profit_adjustment: supported_service_price - actual_service_price
  - excess_interest: actual_interest - supported_independent_interest
expected:
  profit_adjustment: 30000
  excess_interest: 10000
```

## gg-uk-treaty-employment-and-relief.txt, control 6

```oa-check
name: Guernsey UK property-rich interest value boundary
inputs:
  total_value: 1000000
  boundary_property_value: 500000
  higher_property_value: 510000
steps:
  - boundary_percent: boundary_property_value / total_value * 100
  - higher_percent: higher_property_value / total_value * 100
expected:
  boundary_percent: 50
  higher_percent: 51
```

## gg-uk-treaty-employment-and-relief.txt, control 7

```oa-check
name: Guernsey UK offshore associated activity overlap
inputs:
  enterprise_days: 22
  associated_days: 14
  simultaneous_days: 6
steps:
  - aggregated_days: enterprise_days + associated_days - simultaneous_days
  - additional_nonoverlapping_day: aggregated_days + 1
expected:
  aggregated_days: 30
  additional_nonoverlapping_day: 31
```

## gg-uk-treaty-employment-and-relief.txt, control 8

```oa-check
name: Employment presence boundary in one tested rolling window
inputs:
  first_visit_days: 90
  second_visit_days: 93
  additional_day: 1
steps:
  - at_boundary: first_visit_days + second_visit_days
  - over_boundary: at_boundary + additional_day
expected:
  at_boundary: 183
  over_boundary: 184
```

## gg-uk-treaty-employment-and-relief.txt, control 9

```oa-check
name: Guernsey treaty credit below and above the same-income ceiling
inputs:
  guernsey_precredit_tax: 4000
  lower_eligible_uk_tax: 3000
  higher_eligible_uk_tax: 5000
steps:
  - lower_credit: min(guernsey_precredit_tax, lower_eligible_uk_tax)
  - lower_residual: guernsey_precredit_tax - lower_credit
  - higher_credit: min(guernsey_precredit_tax, higher_eligible_uk_tax)
  - higher_residual: guernsey_precredit_tax - higher_credit
  - excess_over_ceiling: higher_eligible_uk_tax - higher_credit
expected:
  lower_credit: 3000
  lower_residual: 1000
  higher_credit: 4000
  higher_residual: 0
  excess_over_ceiling: 1000
```
