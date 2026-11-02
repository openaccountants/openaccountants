# Supplementary boundary controls, 2026

These exercise distinct statutory methods beyond the exactly two examples in each Guide. Documentary eligibility, actual valuations and notices remain inputs.

## Combined corporate loss and credit floor

Positive pre-loss base100000; eligible losses90000; elect to use50000. Grossafterloss5000, prelossfloor3000. Of an assumed independently eligible4000credit, use2000 andcarry2000, retaining40000losses within their original expiry. This does not establish the credit's own eligibility.

```oa-check
name: Andorra combined loss and credit settlement floor
inputs:
  pre_loss_base: 100000
  eligible_losses: 90000
  chosen_loss_use: 50000
  tax_rate: 0.10
  floor_fraction: 0.30
  eligible_credit: 4000
steps:
  floor: pre_loss_base * tax_rate * floor_fraction
  post_loss_base: pre_loss_base - chosen_loss_use
  gross_after_losses: post_loss_base * tax_rate
  usable_credit: min(eligible_credit, max(0, gross_after_losses - floor))
  settlement: gross_after_losses - usable_credit
  credit_remaining: eligible_credit - usable_credit
  loss_remaining: eligible_losses - chosen_loss_use
expected:
  floor: 3000
  post_loss_base: 50000
  gross_after_losses: 5000
  usable_credit: 2000
  settlement: 3000
  credit_remaining: 2000
  loss_remaining: 40000
```

## PE cessation value

An assigned fixed asset had market value120000on entering use inAndorra, verified deductible depreciation30000and noothercorrection. At cessation actual marketvalue150000. Article17(2)b/17(3)differenceis60000. Assume ordinary pre-exit taxableprofit40000,nootheradjustments/loss/creditsand paidadvance7000: totalbase100000,tax10000,balance3000. This is not an individual residence-loss charge or temporary-import re-export.

```oa-check
name: Andorra PE cessation gain and annual balance
inputs:
  entry_market_value: 120000
  deductible_depreciation: 30000
  exit_market_value: 150000
  ordinary_taxable_profit: 40000
  tax_rate: 0.10
  paid_advance: 7000
steps:
  remaining_basis: entry_market_value - deductible_depreciation
  exit_gain: exit_market_value - remaining_basis
  taxable_base: ordinary_taxable_profit + exit_gain
  tax: taxable_base * tax_rate
  balance: tax - paid_advance
expected:
  remaining_basis: 90000
  exit_gain: 60000
  taxable_base: 100000
  tax: 10000
  balance: 3000
```

## Ordinary25% health complement, full months

Approved ordinary25%base,nootherdirecthealthcoverage,noretiredgeneral-onlyexception,noincapacityorpartmonth. FebruaryCASSsheetprovidesJanmethod;Julyamountusesdatednewminimumandthesameformula.

```oa-check
name: Andorra ordinary 25 percent health complement across July
inputs:
  reference: 2672.52
  base_fraction: 0.25
  january_minimum: 1525.33
  july_minimum: 1568.67
  full_rate: 0.22
  complement_rate: 0.10
steps:
  base: reference * base_fraction
  ordinary_quota: round(base * full_rate, 2)
  january_complement: round((january_minimum - base) * complement_rate, 2)
  july_complement: round((july_minimum - base) * complement_rate, 2)
  january_total: ordinary_quota + january_complement
  july_total: ordinary_quota + july_complement
expected:
  base: 668.13
  ordinary_quota: 146.99
  january_complement: 85.72
  july_complement: 90.05
  january_total: 232.71
  july_total: 237.04
```

## Company migration: no participation exemption assumed

Actual ordinary outbound-company factswithinIS17a,noincomingentryexception,noassetsretainedAndorraPE,noloss/credits. Subsidiarysharesmarket500000,taxbasis200000. FollowingCV0366-2026's materiallyequivalentcase,do not exemptthedeemedgainunder20: gain300000,10%tax30000beforeactualadvances. Not a ruling on every reorganisation or inbound-historycase.

```oa-check
name: Andorra company migration deemed share gain
inputs:
  market_value: 500000
  tax_basis: 200000
  tax_rate: 0.10
steps:
  deemed_gain: market_value - tax_basis
  tax: deemed_gain * tax_rate
expected:
  deemed_gain: 300000
  tax: 30000
```
