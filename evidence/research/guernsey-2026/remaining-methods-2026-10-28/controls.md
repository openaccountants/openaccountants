# Supplementary ordinary PE bridge controls

These controls assume the independently evidenced attribution, deductibility and income-class inputs stated in the Guide; they do not establish a PE or a prescribed profit margin. Source: Income Tax Law ss7,84–86 and Fifth Schedule; UK treaty art7. Original two main Guide controls remain byte-exact.

```oa-check
name: Guernsey ordinary standard-rate PE domestic profit bridge 2026
inputs:
  revenue: 200000
  book_costs: 130000
  book_depreciation: 10000
  capital_allowances: 5000
  rate: 0
steps:
  - accounts_profit: revenue - book_costs
  - taxable_profit: accounts_profit + book_depreciation - capital_allowances
  - company_tax: taxable_profit * rate
expected:
  accounts_profit: 70000
  taxable_profit: 75000
  company_tax: 0
```

```oa-check
name: Guernsey established intermediate-rate PE domestic profit bridge 2026
inputs:
  revenue: 200000
  book_costs: 130000
  book_depreciation: 10000
  capital_allowances: 5000
  rate: 0.10
steps:
  - accounts_profit: revenue - book_costs
  - taxable_profit: accounts_profit + book_depreciation - capital_allowances
  - company_tax: taxable_profit * rate
expected:
  accounts_profit: 70000
  taxable_profit: 75000
  company_tax: 7500
```
