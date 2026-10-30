# Ordinary housing and car-period comparison controls

Writer controls awaiting independent review. [2026 Benefits in Kind Guide section 11, examples 4–5, Fact Sheet 2 and E28](https://gov.gg/CHttpHandler.ashx?id=202739&p=0), reread 28 October 2026. The main payroll Guide's two original blocks remain unchanged.

## Actual emoluments and housing periods

Example A assumes the authority's ordinary furnished-housing category, 50 days in Guernsey, accommodation available for all 50 days, £3,000 relevant actual emoluments, no contribution and no rental-value election affecting the result. The percentage benefit is £525; dividing by 365 would be the wrong denominator for this specific method. Example B is a different full-year split-employment case: £30,000 plus £10,000 relevant emoluments, ordinary furnished accommodation, no contribution and no lower-value election. E28 requires both employers' emoluments in the base, so the benefit is £7,000. Neither example allocates the separate £900 miscellaneous-benefit exemption.

```oa-check
name: Guernsey ordinary accommodation arrival period and split employment
inputs:
  example_a_days_available: 50
  example_a_days_in_guernsey: 50
  example_a_relevant_emoluments: 3000
  example_b_other_job_emoluments: 30000
  example_b_provider_emoluments: 10000
  furnished_housing_rate: 0.175
steps:
  - example_a_benefit: example_a_days_available / example_a_days_in_guernsey * example_a_relevant_emoluments * furnished_housing_rate
  - example_b_emoluments: example_b_other_job_emoluments + example_b_provider_emoluments
  - example_b_benefit: example_b_emoluments * furnished_housing_rate
expected:
  example_a_benefit: 525
  example_b_emoluments: 40000
  example_b_benefit: 7000
```

## Preserve the car-period formula discrepancy

Assume the Guide's £30,000 car, giving £6,000 annual benefit at 20%, with 171 available days from 1 January–20 June 2026. Section 11's annual days/365 expression gives £2,810.96. Its separate final-month example retains five £500 entries plus £333.33 for twenty of June's thirty days, giving £2,833.33. This control proves the difference, not authority to select a formula or make a £22.37 correction. A current assessment/reconciliation instruction is still needed for that boundary.

```oa-check
name: Guernsey car benefit annual versus stated final-month method remains unresolved
inputs:
  car_cost: 30000
  car_benefit_rate: 0.20
  available_days: 171
  year_days: 365
  prior_full_months: 5
  final_month_available_days: 20
  final_month_days: 30
steps:
  - annual_benefit: car_cost * car_benefit_rate
  - annual_day_method: round(annual_benefit * available_days / year_days, 2)
  - monthly_amount: annual_benefit / 12
  - prior_month_entries: prior_full_months * monthly_amount
  - final_month_entry: round(final_month_available_days * monthly_amount / final_month_days, 2)
  - monthly_payroll_method: prior_month_entries + final_month_entry
  - unresolved_difference: monthly_payroll_method - annual_day_method
expected:
  annual_benefit: 6000
  annual_day_method: 2810.96
  final_month_entry: 333.33
  monthly_payroll_method: 2833.33
  unresolved_difference: 22.37
```
