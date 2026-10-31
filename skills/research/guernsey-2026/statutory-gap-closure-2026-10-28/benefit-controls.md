# Statutory benefit gap controls

Sources read28October2026: [Valuation Regulations2010reg5](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=267239), [authentic2010reg5](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=267223), [2025amendmentrr2–4,7](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=265330); [ExemptionOrdinance2(1)(v)](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=263414), [2022No3ss12,14](https://www.guernseylegalresources.gg/CHttpHandler.ashx?fileid=263409). Writer controls pending independent whole-pack review. All main Guide controls remain byte-exact. Assumes171actual availabledays in2026, unrestrictedcar, actual30kcost; no discretionary valuation reduction or employee payment. Benefits in the second control are independently established eligible values after all specific exclusions.

```oa-check
name: Statutory annual car valuation and remaining booked benefit reconciliation
inputs:
  actual_car_cost: 30000
  annual_rate: 0.2
  available_days: 171
  statutory_denominator: 365
  prior_months: 5
  monthly_booked_amount: 500
steps:
  - annual_benefit: actual_car_cost * annual_rate
  - statutory_period_benefit: round(annual_benefit * available_days / statutory_denominator, 2)
  - already_booked: prior_months * monthly_booked_amount
  - remaining_annual_reconciliation: statutory_period_benefit - already_booked
  - guide_monthly_june: round(20 * monthly_booked_amount / 30, 2)
  - guide_booked_total: already_booked + guide_monthly_june
  - excess_over_statutory_total: guide_booked_total - statutory_period_benefit
expected:
  annual_benefit: 6000
  statutory_period_benefit: 2810.96
  remaining_annual_reconciliation: 310.96
  guide_booked_total: 2833.33
  excess_over_statutory_total: 22.37
```

```oa-check
name: Employee annual aggregate eligible benefits and duplicate payroll exemption reconciliation
inputs:
  employer_a_eligible_benefits: 1200
  employer_b_eligible_benefits: 600
  annual_exemption: 900
  exemption_used_by_a: 900
  exemption_used_by_b: 600
steps:
  - aggregate_eligible_benefits: employer_a_eligible_benefits + employer_b_eligible_benefits
  - single_annual_exemption: min(aggregate_eligible_benefits, annual_exemption)
  - correct_annual_taxable_benefit: aggregate_eligible_benefits - single_annual_exemption
  - exemption_already_used: exemption_used_by_a + exemption_used_by_b
  - payroll_taxable_benefits: aggregate_eligible_benefits - exemption_already_used
  - taxable_benefit_reconciliation: correct_annual_taxable_benefit - payroll_taxable_benefits
expected:
  aggregate_eligible_benefits: 1800
  single_annual_exemption: 900
  correct_annual_taxable_benefit: 900
  payroll_taxable_benefits: 300
  taxable_benefit_reconciliation: 600
```

These are benefit-base computations, not final tax/refund instructions or an employer-specific allocation direction.
