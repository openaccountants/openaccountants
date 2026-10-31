# Basque foreign-assignment closeout controls

These fictional controls test the labelled literal own-art11 annual-day method in es-foral-income-tax. They do not claim a binding part-year ruling, return-box rounding or software parity. Full original-language article contexts are in source-contexts.json. The taxpayer cap, qualifying foreign work and specific pay conditions remain those of the linked Guide. Retain unrounded terms until aggregation and the cap.

## Short relationship

```oa-check
name: Basque literal annual-day part-year foreign assignment
inputs:
  nonspecific: 18400
  specific: 3000
  qualifying_days: 46
  annual_days: 365
  gross: 21400
steps:
  eligible: specific + nonspecific * qualifying_days / annual_days
  residual: gross - eligible
expected:
  eligible: 5318.904109589041
  residual: 16081.09589041096
```

## Successive employers

```oa-check
name: Basque literal annual-day successive-payer allocation
inputs:
  first_pay: 27300
  first_days: 39
  second_pay: 18400
  second_days: 36
  annual_days: 365
steps:
  first_eligible: first_pay * first_days / annual_days
  second_eligible: second_pay * second_days / annual_days
  total_eligible: first_eligible + second_eligible
expected:
  first_eligible: 2916.986301369863
  second_eligible: 1814.794520547945
  total_eligible: 4731.780821917808
```

## One cap and specific pay

```oa-check
name: Basque single taxpayer foreign-assignment cap
inputs:
  eligible_first: 40000
  eligible_second: 40000
  annual_cap: 60100
steps:
  total_eligible: eligible_first + eligible_second
  exempt: min(total_eligible, annual_cap)
  residual: total_eligible - exempt
expected:
  total_eligible: 80000
  exempt: 60100
  residual: 19900
```

```oa-check
name: Basque specific foreign-service pay is not prorated twice
inputs:
  nonspecific: 18400
  specific: 3000
  qualifying_days: 46
  annual_days: 365
steps:
  eligible_nonspecific: nonspecific * qualifying_days / annual_days
  eligible_specific: specific
  total_eligible: eligible_nonspecific + eligible_specific
expected:
  eligible_nonspecific: 2318.904109589041
  eligible_specific: 3000
  total_eligible: 5318.904109589041
```

## Domestic-only separate payer

```oa-check
name: Unrelated domestic-only payer adds no foreign exemption
inputs:
  domestic_only_pay: 50000
  qualifying_days: 0
  annual_days: 365
steps:
  exempt_increment: domestic_only_pay * qualifying_days / annual_days
expected:
  exempt_increment: 0
```
