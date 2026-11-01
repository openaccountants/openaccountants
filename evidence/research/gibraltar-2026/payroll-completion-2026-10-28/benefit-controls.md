# Separate ordinary benefit valuation controls

All examples assume independently established charging scope, period, non-exemption and evidence. They are separate scenarios, not one employee's combined benefits, tax or SI base. No £250 subtraction or threshold-boundary conclusion is assumed.

## Expense, voucher, employer-owned car and comparable loan

The expense paid away satisfies paragraph6's employment-expense test. The non-cash voucher meets paragraph8 conditions and timing. The car is available for private use for a full first year, is employer-owned, and has no pool/shared-use exception. The separate fuel case meets paragraph28’s actual chargeability conditions; its original paragraph23 reference is retained. The loan is outstanding for a full employment year, has no paragraph32/33 exception and uses an independently evidenced assumed5% unconnected bank/building-society comparator on similar non-interest terms. That5% is not a statutory rate.

```oa-check
name: Separate expense voucher owned-car and comparable-loan values
inputs:
  expense_payment: 2000
  qualifying_expenses_paid_away: 1500
  noncash_voucher_cost: 600
  voucher_made_good: 100
  owned_car_cost: 40000
  car_made_good: 2000
  qualifying_employer_fuel_cost: 2000
  fuel_made_good: 300
  full_year_loan: 50000
  evidenced_comparable_rate: 0.05
  loan_interest_paid: 1000
steps:
  - expense_earnings: expense_payment - qualifying_expenses_paid_away
  - voucher_value: noncash_voucher_cost - voucher_made_good
  - car_value: owned_car_cost * 0.25 - car_made_good
  - fuel_value: qualifying_employer_fuel_cost * 0.9 - fuel_made_good
  - loan_value: full_year_loan * evidenced_comparable_rate - loan_interest_paid
expected:
  expense_earnings: 500
  voucher_value: 500
  car_value: 8000
  fuel_value: 1500
  loan_value: 1500
```

## Accommodation and residual non-car asset

Accommodation is provided for a full taxable year, without paragraph13 exception; higher actual provider rent applies. The separate residual asset is neither a car nor another specially covered/excluded benefit. Its market value is established at the statutory initial-use time, and additional expense excludes acquisition/rent amounts already accounted for. No shared allocation or unverified part-year convention is used.

```oa-check
name: Separate full-year accommodation and residual non-car asset values
inputs:
  accommodation_annual_value: 18000
  provider_annual_rent: 24000
  accommodation_made_good: 6000
  residual_asset_initial_market_value: 10000
  asset_annual_hire: 2500
  asset_additional_expense: 300
  asset_made_good: 100
steps:
  - accommodation_value: max(accommodation_annual_value, provider_annual_rent) - accommodation_made_good
  - asset_use_value: residual_asset_initial_market_value * 0.2
  - asset_value: max(asset_use_value, asset_annual_hire) + asset_additional_expense - asset_made_good
expected:
  accommodation_value: 18000
  asset_use_value: 2000
  asset_value: 2700
```

## Separate employer-paid benefit tax cases

Paragraph74 election and the otherwise taxable value have already been independently established for each separate case. These values are after any properly established scope/exclusion treatment; this check does not decide paragraph73's aggregate threshold, the exactly£250 boundary or subtract£250 from a larger package. The statutory higher rate is applied to its whole established base; no employee wage deduction or extra tax gross-up is assumed.

```oa-check
name: Separate established employer-paid benefit tax bases
inputs:
  established_lower_case_base: 1000
  established_higher_case_base: 20000
steps:
  - lower_case_tax: established_lower_case_base * 0.2
  - higher_case_tax: established_higher_case_base * 0.29
expected:
  lower_case_tax: 200
  higher_case_tax: 5800
```
