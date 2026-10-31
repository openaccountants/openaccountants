# Montenegro PIT: additional source and form controls

Read with the Guide and figure ledger. These are workpaper controls, not representations that unresolved live IRMS fields have been confirmed. Pausal source: [Rulebook art. 5](https://wapi.gov.me/download/13de63a3-660e-4cb4-bb77-b0b59e456834?version=1.0). Form source: [103/2025 art. 3 and attachments](https://www.sluzbenilist.me/propisi/385024/download). PIT bands, deductions and foreign-credit cap: [PIT Law arts. 10, 20, 37p, 42 and 44](https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0). Contribution rate/base: [Contributions Law arts. 9, 11, 15 and 18](https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0). All read 2026-10-31.

```oa-check
name: Montenegro pausal group I, turnover ceiling 7500
inputs:
  turnover_ceiling: 7500
  cost_percent: 50
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 3750
  pit: 0
  combined: 412.5
```

```oa-check
name: Montenegro pausal group I, turnover ceiling 15000
inputs:
  turnover_ceiling: 15000
  cost_percent: 50
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 7500
  pit: 0
  combined: 825
```

```oa-check
name: Montenegro pausal group I, turnover ceiling 22500
inputs:
  turnover_ceiling: 22500
  cost_percent: 50
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 11250
  pit: 256.5
  combined: 1494
```

```oa-check
name: Montenegro pausal group I, turnover ceiling 30000
inputs:
  turnover_ceiling: 30000
  cost_percent: 50
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 15000
  pit: 774
  combined: 2424
```

```oa-check
name: Montenegro pausal group II, turnover ceiling 7500
inputs:
  turnover_ceiling: 7500
  cost_percent: 40
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 4500
  pit: 0
  combined: 495
```

```oa-check
name: Montenegro pausal group II, turnover ceiling 15000
inputs:
  turnover_ceiling: 15000
  cost_percent: 40
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 9000
  pit: 54
  combined: 1044
```

```oa-check
name: Montenegro pausal group II, turnover ceiling 22500
inputs:
  turnover_ceiling: 22500
  cost_percent: 40
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 13500
  pit: 549
  combined: 2034
```

```oa-check
name: Montenegro pausal group II, turnover ceiling 30000
inputs:
  turnover_ceiling: 30000
  cost_percent: 40
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 18000
  pit: 1224
  combined: 3204
```

```oa-check
name: Montenegro pausal group III, turnover ceiling 7500
inputs:
  turnover_ceiling: 7500
  cost_percent: 35
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 4875
  pit: 0
  combined: 536.25
```

```oa-check
name: Montenegro pausal group III, turnover ceiling 15000
inputs:
  turnover_ceiling: 15000
  cost_percent: 35
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 9750
  pit: 121.5
  combined: 1194
```

```oa-check
name: Montenegro pausal group III, turnover ceiling 22500
inputs:
  turnover_ceiling: 22500
  cost_percent: 35
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 14625
  pit: 717.75
  combined: 2326.5
```

```oa-check
name: Montenegro pausal group III, turnover ceiling 30000
inputs:
  turnover_ceiling: 30000
  cost_percent: 35
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 19500
  pit: 1449
  combined: 3594
```

```oa-check
name: Montenegro pausal group IV, turnover ceiling 7500
inputs:
  turnover_ceiling: 7500
  cost_percent: 30
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 5250
  pit: 0
  combined: 577.5
```

```oa-check
name: Montenegro pausal group IV, turnover ceiling 15000
inputs:
  turnover_ceiling: 15000
  cost_percent: 30
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 10500
  pit: 189
  combined: 1344
```

```oa-check
name: Montenegro pausal group IV, turnover ceiling 22500
inputs:
  turnover_ceiling: 22500
  cost_percent: 30
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 15750
  pit: 886.5
  combined: 2619
```

```oa-check
name: Montenegro pausal group IV, turnover ceiling 30000
inputs:
  turnover_ceiling: 30000
  cost_percent: 30
steps:
  - base: turnover_ceiling * (1 - cost_percent / 100)
  - pit: max(min(base, 12000) - 8400, 0) * 0.09 + max(base - 12000, 0) * 0.15
  - combined: base * 0.11 + pit
expected:
  base: 21000
  pit: 1674
  combined: 3984
```

## Full-year assessed split, not PIT twice

Assume a full-year group-II third-subgroup decision, ordinary insurance and a municipal decision setting 13% surtax. The table already includes contributions; the surtax applies to PIT, not the combined amount. No unknown rounding is needed for this row.

```oa-check
name: Montenegro pausal monthly split and separate assumed municipal surtax
inputs:
  annual_pit: 549
  base: 13500
  assumed_surtax_rate: 0.13
steps:
  - pio: base * 0.10
  - unemployment: base * 0.01
  - combined: annual_pit + pio + unemployment
  - monthly_pit: annual_pit / 12
  - monthly_contributions: (pio + unemployment) / 12
  - monthly_combined: combined / 12
  - annual_surtax: annual_pit * assumed_surtax_rate
  - all_in: combined + annual_surtax
expected:
  pio: 1350
  unemployment: 135
  combined: 2034
  monthly_pit: 45.75
  monthly_contributions: 123.75
  monthly_combined: 169.5
  annual_surtax: 71.37
  all_in: 2105.37
```

## H: mutually exclusive cost routes and no income duplication

Assume domestic nonwithheld occasional receipts 2,000 with no documented costs; residual internet receipts 10,000; nonsalary gaming receipts 5,000 with documented costs 1,200. Gaming uses actual costs rather than also deducting the 20% standard allowance. This yields H12 and main3.6.

```oa-check
name: Montenegro H independent category bases
inputs:
  occasional_receipts: 2000
  internet_receipts: 10000
  gaming_receipts: 5000
  documented_gaming_costs: 1200
steps:
  - h5: occasional_receipts * (1 - 0.30)
  - h8: internet_receipts * (1 - 0.15)
  - h11: gaming_receipts - documented_gaming_costs
  - h12: h5 + h8 + h11
  - pit: h12 * 0.15
expected:
  h5: 1400
  h8: 8500
  h11: 3800
  h12: 13700
  pit: 2055
```

## Mixed ordinary full-year return: main due and refund

Assume principal taxable business base 24,840; domestic rent base B4=14,000, sport D6=500, copyright E6=2,000; H12=13,700. Foreign dividend 10,000 and occasional net income 1,400 are each included only in F, not duplicated in B/D/E/H. Foreign paid taxes are dividend 2,000 and occasional 70; the eligible credit is capped separately at 1,500 and 210 respectively. Thus 1,570 is eligible, not the 1,710 pooled domestic tax on those foreign categories. No foreign salary, supplementary activity, gambling, relief or municipal surtax is assumed. Business PIT advances are 1,800; B/D/E advances 2,100/75/300.

```oa-check
name: Montenegro main ordinary full-year due with isolated foreign credit cap
inputs:
  principal_base: 24840
  b4: 14000
  d6: 500
  e6: 2000
  f_dividend: 10000
  f_occasional_net: 1400
  h12: 13700
  foreign_dividend_tax: 2000
  foreign_occasional_tax: 70
  business_advances: 1800
  b5: 2100
  d7: 75
  e7: 300
steps:
  - main12: max(min(principal_base, 12000) - 8400, 0) * 0.09 + max(principal_base - 12000, 0) * 0.15
  - f15: min(foreign_dividend_tax, f_dividend * 0.15) + min(foreign_occasional_tax, f_occasional_net * 0.15)
  - main35: f_dividend + f_occasional_net
  - main37: b4 + d6 + e6 + main35 + h12
  - main39: main37 * 0.15
  - main41: main12 + main39
  - main58: business_advances + b5 + d7 + e7 + f15
  - main61: max(main41 - main58, 0)
  - main62: max(main58 - main41, 0)
expected:
  main12: 2250
  f15: 1570
  main35: 11400
  main37: 41600
  main39: 6240
  main41: 8490
  main58: 5845
  main61: 2645
  main62: 0
```

```oa-check
name: Montenegro main overpayment split without a double refund
inputs:
  main41: 8490
  main58: 9000
  refund_requested: 300
steps:
  - overpaid: max(main58 - main41, 0)
  - next_period_credit: overpaid - refund_requested
  - claimed_total: refund_requested + next_period_credit
expected:
  overpaid: 510
  next_period_credit: 210
  claimed_total: 510
```

## A1 component arithmetic despite the printed total conflict

Assume a separately established annual contribution base 12,000, ordinary principal-entrepreneur rates 10% PIO and 1% unemployment, no exemptions, advances of PIO 1,300 and unemployment100. PIO has an overpayment and unemployment a debt. Keep those components separate. This does not certify how the live portal resolves A1 total2.

```oa-check
name: Montenegro A1 component balances remain separate
inputs:
  base: 12000
  pio_advance: 1300
  unemployment_advance: 100
steps:
  - pio_charge: base * 0.10
  - unemployment_charge: base * 0.01
  - pio_overpaid: max(pio_advance - pio_charge, 0)
  - pio_due: max(pio_charge - pio_advance, 0)
  - unemployment_overpaid: max(unemployment_advance - unemployment_charge, 0)
  - unemployment_due: max(unemployment_charge - unemployment_advance, 0)
expected:
  pio_charge: 1200
  unemployment_charge: 120
  pio_overpaid: 100
  pio_due: 0
  unemployment_overpaid: 0
  unemployment_due: 20
```

## KPP and ZPO receipt reconciliation

Two illustrative transactions: product120/service80 and product30/service70. KPP total300 reconciles to product150 + service150; prior/planned application totals use the same separation. The authority decision and actual period are independent inputs.

```oa-check
name: Montenegro KPP products and services conservation
inputs:
  first_products: 120
  first_services: 80
  second_products: 30
  second_services: 70
steps:
  - products: first_products + second_products
  - services: first_services + second_services
  - turnover: products + services
expected:
  products: 150
  services: 150
  turnover: 300
```

## Printed partial-year discrepancy, retained as a gap

This reproduces the two arithmetic routes to prove why no accepted proration/rounding method is claimed. The printed example uses 302 days and a rounded daily amount23.01. The statute and source do not settle the live2026 acceptance method.

```oa-check
name: Montenegro A printed early rounding versus full precision
inputs:
  annual_amount: 8400
  days_in_year: 365
  active_days: 302
steps:
  - printed_daily: round(annual_amount / days_in_year, 2)
  - printed_result: printed_daily * active_days
  - full_precision_result: round(annual_amount * active_days / days_in_year, 2)
  - difference: full_precision_result - printed_result
expected:
  printed_daily: 23.01
  printed_result: 6949.02
  full_precision_result: 6950.14
  difference: 1.12
```
