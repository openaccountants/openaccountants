# Moldova 2026 social-insurance writer calculation controls

These are writer arithmetic controls tied to the retained CNAS instructions. They do not establish statutory applicability, health/PIT calculations, a reviewed Guide or comprehensive country coverage. Whole-country review is pending. Each case gives its classification assumptions.

Source: [CNAS 2026 instructions](https://cnas.gov.md/sites/default/files/2026-10/Particularitati2026.pdf), read 30 October 2026.

## 1. Private employer ordinary social base
CNAS point 9.2. Employer and every payment are documented as ordinary private-sector/in-scope; this is social insurance only, not net pay.

```oa-check
name: Moldova 2026 Private employer ordinary social base
inputs:
  accrued_in_scope_pay: 10000
steps:
  employer_social: accrued_in_scope_pay * 0.24
  salary_plus_social: accrued_in_scope_pay + employer_social
expected:
  employer_social: 2400
  salary_plus_social: 12400
```

## 2. Public institution ordinary social base
CNAS point 9.1. Institution meets the actual public category and is not a higher-education or medical exception.

```oa-check
name: Moldova 2026 Public institution ordinary social base
inputs:
  accrued_in_scope_pay: 10000
steps:
  employer_social: accrued_in_scope_pay * 0.29
expected:
  employer_social: 2900
```

## 3. Civil aviation listed private role
CNAS point 10.2. Actual private civil-aviation role is on the statutory special-condition list; ordinary hazardous work alone does not establish this tariff.

```oa-check
name: Moldova 2026 Civil aviation listed private role
inputs:
  accrued_in_scope_pay: 20000
steps:
  employer_social: accrued_in_scope_pay * 0.32
expected:
  employer_social: 6400
```

## 4. Civil aviation listed public role
CNAS point 10.1. Actual public civil-aviation role is within the specified list.

```oa-check
name: Moldova 2026 Civil aviation listed public role
inputs:
  accrued_in_scope_pay: 20000
steps:
  employer_social: accrued_in_scope_pay * 0.39
expected:
  employer_social: 7800
```

## 5. Agricultural employer and state shares
CNAS point 13–13.4. Documented qualifying agricultural activity and annual/policy gates satisfied; no automatic grant from a bank label.

```oa-check
name: Moldova 2026 Agricultural employer and state shares
inputs:
  accrued_in_scope_pay: 10000
  qualifying_activity_income: 800000
  operating_income: 1000000
steps:
  activity_ratio: qualifying_activity_income / operating_income
  total_social: accrued_in_scope_pay * 0.24
  employer_share: accrued_in_scope_pay * 0.18
  state_compensation: accrued_in_scope_pay * 0.06
  share_check: employer_share + state_compensation
expected:
  activity_ratio: 0.8
  total_social: 2400
  employer_share: 1800
  state_compensation: 600
  share_check: 2400
```

## 6. Fixed founder full calendar year
CNAS point 15.1–15.2. Registered throughout 2026; no pension/disability/insured-employment/suspension or sickness exception.

```oa-check
name: Moldova 2026 Fixed founder full calendar year
inputs:
  active_months: 12
  monthly_social: 1906.5
steps:
  annual_social: active_months * monthly_social
expected:
  annual_social: 22878
```

## 7. Justice professional full calendar year
CNAS point 16.2. Qualifying justice profession; no exemption, suspension or sickness period.

```oa-check
name: Moldova 2026 Justice professional full calendar year
inputs:
  active_months: 12
  monthly_social: 2580.5
steps:
  annual_social: active_months * monthly_social
expected:
  annual_social: 30966
```

## 8. Patent two touched calendar months
CNAS point 17.3. A 2026 patent touches two calendar months, even if each is partial; no exemption.

```oa-check
name: Moldova 2026 Patent two touched calendar months
inputs:
  touched_months: 2
  monthly_social: 1906.5
steps:
  social_due: touched_months * monthly_social
expected:
  social_due: 3813
```

## 9. Taxi June hiring remaining days
CNAS point 18.1. A June 2026 qualifying taxi-driver hiring covers ten remaining calendar days out of thirty; no claim to the July ordinary regime.

```oa-check
name: Moldova 2026 Taxi June hiring remaining days
inputs:
  monthly_social: 1906.5
  remaining_days: 10
  calendar_days_in_month: 30
steps:
  social_due: monthly_social * remaining_days / calendar_days_in_month
expected:
  social_due: 635.5
```

## 10. Day worker contribution arithmetic
CNAS point 19.1. Day worker covered by the statutory category, no competing-insurance exemption; pay is above the stated full-day minimum. This is not ordinary employee SSC.

```oa-check
name: Moldova 2026 Day worker contribution arithmetic
inputs:
  documented_daily_pay: 500
steps:
  social_due: documented_daily_pay * 0.06
expected:
  social_due: 30
```

## 11. IT park insured income and budget allocation
CNAS point 12.1–12.3. Qualifying employment at one IT-park employer; single-tax paid is an evidenced assumption, not computed here. Civil contracts require their separate treatment.

```oa-check
name: Moldova 2026 IT park insured income and budget allocation
inputs:
  forecast_monthly_salary: 17400
  assumed_single_tax_paid: 100000
steps:
  insured_monthly_income: forecast_monthly_salary * 0.68
  social_budget_allocation: assumed_single_tax_paid * 0.547
expected:
  insured_monthly_income: 11832
  social_budget_allocation: 54700
```

## 12. Independent services annual band arithmetic
CNAS point 2.1/20.2. Documented new independent service-entrepreneur category for a full 2026 year. Cumulative annual reconciliation only; monthly notices and any health top-up are separate.

```oa-check
name: Moldova 2026 Independent services annual band arithmetic
inputs:
  annual_in_scope_receipts: 1300000
  ordinary_band: 1200000
steps:
  ordinary_tax: min(annual_in_scope_receipts, ordinary_band) * 0.15
  excess_tax: max(0, annual_in_scope_receipts - ordinary_band) * 0.35
  single_tax: ordinary_tax + excess_tax
  social_allocation: single_tax * 0.533
expected:
  ordinary_tax: 180000
  excess_tax: 35000
  single_tax: 215000
  social_allocation: 114595
```

## 13. Voluntary agriculture final-month adjustment
CNAS point 22–22.1. Individual unregistered agricultural landholder/tenant voluntarily insured for full year under the actual category; preserve CNAS published monthly adjustment.

```oa-check
name: Moldova 2026 Voluntary agriculture final-month adjustment
inputs:
  jan_to_nov_months: 11
  jan_to_nov_amount: 485.59
  december_amount: 485.51
steps:
  year_total: jan_to_nov_months * jan_to_nov_amount + december_amount
expected:
  year_total: 5827
```

## 14. Social arrears simple daily charge
CNAS point 34–36. Constant actual social principal debt and ten chargeable days, ordinary category; no agricultural deferral, debt movements or statutory exception. CNAS actual account governs application.

```oa-check
name: Moldova 2026 Social arrears simple daily charge
inputs:
  unchanged_principal_debt: 10000
  late_days_including_payment_day: 10
steps:
  late_charge: unchanged_principal_debt * 0.001 * late_days_including_payment_day
expected:
  late_charge: 100
```
