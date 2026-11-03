# Supplementary controls: fo-cross-border-payments

Derived case amounts from the cited rules. Original main Guide examples remain unchanged.

### 3. Ordinary company credit capped at tax on foreign income

Assume a fully Faroese-taxable standalone company qualifying for Assessment Act §5(2)'s 18% rate. Its established net ordinary profit is DKK 400,000 domestic plus DKK 100,000 from one country without a Faroese double-tax treaty, after all relevant expense allocation. Eligible foreign income tax actually paid on that DKK 100,000 is DKK 25,000. Assume no separate capital income, losses, special regime, other credits, withholding adjustments or later foreign refund. Faroese tax before relief is DKK 90,000; the foreign-income cap is DKK 18,000. Current credit is DKK 18,000 and Faroese tax after relief DKK 72,000. The remaining DKK 7,000 foreign tax is not credited in this calculation; no carryforward right is assumed. If the otherwise identical foreign tax were DKK 10,000, credit would instead be DKK 10,000 and Faroese tax DKK 80,000. [Tax Act §154][tax]; [Assessment Act §5(2)][rate]; [TAKS VLS O.1.1, O.1.4][relief]

```oa-check
name: Faroese ordinary company foreign credit lower of paid tax and domestic limit
inputs:
  domestic_net_profit: 400000
  foreign_net_profit: 100000
  rate: 0.18
  foreign_paid_high: 25000
  foreign_paid_low: 10000
steps:
  worldwide_base: domestic_net_profit + foreign_net_profit
  tax_before_relief: worldwide_base * rate
  foreign_limit: tax_before_relief * foreign_net_profit / worldwide_base
  credit_high: min(foreign_paid_high, foreign_limit)
  tax_after_high: tax_before_relief - credit_high
  foreign_uncredited_high: foreign_paid_high - credit_high
  credit_low: min(foreign_paid_low, foreign_limit)
  tax_after_low: tax_before_relief - credit_low
expected:
  worldwide_base: 500000
  tax_before_relief: 90000
  foreign_limit: 18000
  credit_high: 18000
  tax_after_high: 72000
  foreign_uncredited_high: 7000
  credit_low: 10000
  tax_after_low: 80000
```


## Ordinary branch-profit bridge

Derived from Tax Act §2(2),TAKS VLS C.2 independent-enterprise attribution and Assessment Act §5(2). Inputs are hypothetical proved allocations, not a legal fixed expense ratio. No foreign treaty exception, intangible or finance attribution is assumed.

```oa-check
name: Faroese ordinary corporate branch profit bridge
inputs:
  attributable_receipts: 1000000
  deductible_direct_cost: 600000
  proved_head_office_cost: 100000
  rate: 0.18
steps:
  profit: attributable_receipts - deductible_direct_cost - proved_head_office_cost
  tax: profit * rate
expected:
  profit: 300000
  tax: 54000
```

## Later exit-deferral disposal below departure value, above original basis

Capital Income Act §2c(2)–(3). Derived only for one security,original basis100000,departure150000,sale140000,no foreign tax or foreign loss deduction,no other balance adjustments. Actual-basis loss,foreign loss deductions and rising values require their separate rules.

```oa-check
name: Faroese later exit-deferral gain and value-fall reduction
inputs:
  original_basis: 100000
  departure_value: 150000
  sale_value: 140000
  rate: 0.35
steps:
  original_balance: (departure_value - original_basis) * rate
  actual_gain: sale_value - original_basis
  tax_paid: actual_gain * rate
  balance_after_payment: original_balance - tax_paid
  value_fall: departure_value - sale_value
  further_reduction: value_fall * rate
  final_balance: balance_after_payment - further_reduction
expected:
  original_balance: 17500
  actual_gain: 40000
  tax_paid: 14000
  balance_after_payment: 3500
  value_fall: 10000
  further_reduction: 3500
  final_balance: 0
```
