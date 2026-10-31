# Payroll and formation supplementary controls

Writer arithmetic checks, not independent review. Actual source rules and exact original-language quotations are in the two figure/rule ledgers. The two main payroll blocks are unchanged; formation remains a non-tax companion with zero main blocks. All amounts below other than statutory rates/limits are assumed facts or derived outputs.

```oa-check
name: Faroese pension A contribution strict DKK30 boundary throughout2026
inputs:
  lower_wage: 249
  boundary_wage: 250
  rate: 0.12
steps:
  lower_contribution: lower_wage * rate
  boundary_contribution: boundary_wage * rate
expected:
  lower_contribution: 29.88
  boundary_contribution: 30
```

The own old rule excludes below30 for A/B; new law retains below30 A and excludes below500 B. These comparisons concern the computed contribution, not a universal monthly B-income threshold. Pre-amendment assessment/settlement transition is reserved.

```oa-check
name: B-income partyear explicit statutory365 denominator
inputs:
  eligible_annual_b_income: 100000
  days_without_duty: 73
  year_denominator: 365
  pension_rate: 0.12
steps:
  unreduced_contribution: eligible_annual_b_income * pension_rate
  reduction: unreduced_contribution * days_without_duty / year_denominator
  contribution: unreduced_contribution - reduction
expected:
  unreduced_contribution: 12000
  reduction: 2400
  contribution: 9600
```

```oa-check
name: Employee payment actual asset benefit offset with zero floor
inputs:
  annual_value: 56800
  proved_payment: 5000
  excess_payment: 60000
steps:
  ordinary_benefit: max(annual_value - proved_payment, 0)
  overpaid_benefit: max(annual_value - excess_payment, 0)
expected:
  ordinary_benefit: 51800
  overpaid_benefit: 0
```

```oa-check
name: Documented actual private mileage partyear car without employee payment
inputs:
  annual_value: 56800
  private_km: 4000
  annual_standard_private_km: 10000
  calendar_months_only: 6
steps:
  actual_mileage_value: annual_value * private_km / annual_standard_private_km
  unsupported_calendar_result: annual_value * calendar_months_only / 12
  separator: unsupported_calendar_result - actual_mileage_value
expected:
  actual_mileage_value: 22720
  unsupported_calendar_result: 28400
  separator: 5680
```

```oa-check
name: Foreign plan isolated single income post February combined funding
inputs:
  sole_eligible_income: 30000
  actual_foreign_funding: 2700
  rate: 0.12
steps:
  combined_target: sole_eligible_income * rate
  needed_faroese_funding: max(combined_target - actual_foreign_funding, 0)
  combined_actual: actual_foreign_funding + needed_faroese_funding
expected:
  combined_target: 3600
  needed_faroese_funding: 900
  combined_actual: 3600
```

The January illustration is a separate claimant with actual TAKS acceptance under the then own law and original Regulation52/2023, including75% continuing payouts. It is not an inferred unconditional exemption or retroactive approval. The March illustration applies the February statutory floor, rather than delaying it until the August regulation.

```oa-check
name: Whole contribution final pension tax at235000 income endpoint
inputs:
  gross_contribution: 12000
  provisional_rate: 0.40
  final_rate: 0.30
steps:
  provisional_tax: gross_contribution * provisional_rate
  final_tax: gross_contribution * final_rate
  account_refund: provisional_tax - final_tax
expected:
  provisional_tax: 4800
  final_tax: 3600
  account_refund: 1200
```

```oa-check
name: SpF premium selected specific section33 incorporation and literal alternative
inputs:
  capital: 200000
  premium: 100000
  capital_fraction: 0.25
  capital_cash_floor: 50000
steps:
  capital_paid: max(capital * capital_fraction, capital_cash_floor)
  actual_paid_fraction: capital_paid / capital
  selected_premium_paid: premium * actual_paid_fraction
  selected_total: capital_paid + selected_premium_paid
  isolated_full_premium_alternative: capital_paid + premium
expected:
  capital_paid: 50000
  actual_paid_fraction: 0.25
  selected_premium_paid: 25000
  selected_total: 75000
  isolated_full_premium_alternative: 150000
```

```oa-check
name: SpF minimum capital and full proportion premium
inputs:
  capital: 50000
  premium: 20000
  fraction: 0.25
  cash_floor: 50000
steps:
  capital_paid: max(capital * fraction, cash_floor)
  actual_fraction: capital_paid / capital
  premium_paid: premium * actual_fraction
  total_paid: capital_paid + premium_paid
expected:
  actual_fraction: 1
  premium_paid: 20000
  total_paid: 70000
```

```oa-check
name: PF full cash premium and separate noncash full payment
inputs:
  pf_capital: 500000
  pf_premium: 100000
  fraction: 0.25
  noncash_capital: 200000
  noncash_premium: 100000
steps:
  pf_capital_paid: pf_capital * fraction
  pf_total_paid: pf_capital_paid + pf_premium
  noncash_total_paid: noncash_capital + noncash_premium
expected:
  pf_capital_paid: 125000
  pf_total_paid: 225000
  noncash_total_paid: 300000
```
