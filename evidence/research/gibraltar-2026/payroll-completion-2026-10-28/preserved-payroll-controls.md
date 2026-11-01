# Preserved payroll calculation controls

Six original v0.14 supplementary blocks, retained byte-exact. Their full original prose/conditions remain in the Guide; the original ER and monthly-PAYE controls are the two main examples.

## Original supplementary control 1

```oa-check
name: Gibraltar daily code24 current-linked table example
inputs:
  gross_pay: 105
  confirmed_days: 3
  verified_daily_table_tax: 0.96
steps:
  - daily_equivalent: gross_pay / confirmed_days
  - paye: verified_daily_table_tax * confirmed_days
expected:
  daily_equivalent: 35
  paye: 2.88
```

## Original supplementary control 2

```oa-check
name: Gibraltar confirmed monthly MW PN and T2 classes
inputs:
  earnings: 1000
steps:
  - mw_employee: 69.12
  - mw_employer: min(173.98, max(78.65, earnings * 0.20))
  - pn_employee: 0
  - pn_employer: min(243.65, max(138.55, earnings * 0.18))
  - t2_employee: min(16.99, earnings * 0.10)
  - t2_employer: 0
expected:
  mw_employee: 69.12
  mw_employer: 173.98
  pn_employee: 0
  pn_employer: 180
  t2_employee: 16.99
  t2_employer: 0
```

## Original supplementary control 3

```oa-check
name: Gibraltar confirmed partial-month weekly limits
inputs:
  low_earnings: 100
  low_weeks: 2
  high_earnings: 1800
  high_weeks: 3
steps:
  - low_employee: min(low_weeks * 40.79, max(low_weeks * 14.34, low_earnings * 0.10))
  - low_employer: min(low_weeks * 56.22, max(low_weeks * 31.98, low_earnings * 0.18))
  - high_employee: min(high_weeks * 40.79, max(high_weeks * 14.34, high_earnings * 0.10))
  - high_employer: min(high_weeks * 56.22, max(high_weeks * 31.98, high_earnings * 0.18))
expected:
  low_employee: 28.68
  low_employer: 63.96
  high_employee: 122.37
  high_employer: 168.66
```

## Original supplementary control 4

```oa-check
name: Gibraltar shared final contribution week two paydays
inputs:
  first_pay: 300
  second_pay: 300
steps:
  - first_employee: min(40.79, max(14.34, first_pay * 0.10))
  - first_employer: min(56.22, max(31.98, first_pay * 0.18))
  - combined_earnings: first_pay + second_pay
  - total_employee: min(40.79, max(14.34, combined_earnings * 0.10))
  - total_employer: min(56.22, max(31.98, combined_earnings * 0.18))
  - second_employee: total_employee - first_employee
  - second_employer: total_employer - first_employer
expected:
  first_employee: 30
  first_employer: 54
  total_employee: 40.79
  total_employer: 56.22
  second_employee: 10.79
  second_employer: 2.22
```

## Original supplementary control 5

```oa-check
name: Gibraltar P8 separate PAYE and combined SI reconciliation
inputs:
  paye_deducted: 4800
  employee_si: 2000
  employer_si: 2800
  paye_paid: 4500
  si_paid: 4600
steps:
  - total_si: employee_si + employer_si
  - paye_outstanding: paye_deducted - paye_paid
  - si_outstanding: total_si - si_paid
expected:
  total_si: 4800
  paye_outstanding: 300
  si_outstanding: 200
```

## Original supplementary control 6

```oa-check
name: Gibraltar two established compound PAYE increments
inputs:
  principal: 1000
steps:
  - after_first_increment: principal * 1.02
  - after_second_increment: after_first_increment * 1.02
  - increase: after_second_increment - principal
expected:
  after_first_increment: 1020
  after_second_increment: 1040.40
  increase: 40.40
```
