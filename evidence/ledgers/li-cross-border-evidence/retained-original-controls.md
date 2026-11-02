# Retained original cross-border controls

All three24October2026 predecessor blocks and their case assumptions remain exact here. This does not extend the historical independent review to the30October writer changes.

### Assumed eligible nonbusiness foreign-credit ceiling

Assume a resident individual with all article 18a eligibility gates, no excluded/special category, exhausted source relief, CHF 1,600 qualifying foreign tax and a separately established CHF 1,200 domestic limit under article 18b. Credit is CHF 1,200. The CHF 400 excess is not treated as an automatic carryforward or refund.

```oa-check
name: Liechtenstein assumed eligible foreign tax credit ceiling
inputs:
  established_qualifying_foreign_tax: 1600
  established_domestic_credit_limit: 1200
steps:
  available_credit: min(established_qualifying_foreign_tax, established_domestic_credit_limit)
  uncredited_foreign_tax: established_qualifying_foreign_tax - available_credit
expected:
  available_credit: 1200
  uncredited_foreign_tax: 400
```

### Specified nonresident individual board payment

Assume a CHF 10,000 gross payment within article 24(2)(b), no treaty reduction/authority exemption and no other issue. Article 25(3)'s 12% gives CHF 1,200 withheld and CHF 8,800 paid before any separately applicable deductions. An ordinary employment wage does not inherit this rate.

```oa-check
name: Liechtenstein assumed specified nonresident board withholding
inputs:
  established_gross_board_payment: 10000
  established_statutory_rate: 0.12
steps:
  source_tax: established_gross_board_payment * established_statutory_rate
  cash_after_source_tax_only: established_gross_board_payment - source_tax
expected:
  source_tax: 1200
  cash_after_source_tax_only: 8800
```

### Corporate asset exit workpaper

Assume article 51 applies to one asset with CHF 100,000 established arm's-length value and CHF 60,000 tax carrying value. The assumed taxable uplift is CHF 40,000; at 12.5%, the isolated tax effect is CHF 5,000 before equity/loss/other interactions. Whether/when it is paid or deferred must be decided separately from the valuation arithmetic.

```oa-check
name: Liechtenstein assumed corporate asset exit uplift
inputs:
  established_arm_length_value: 100000
  established_tax_carrying_value: 60000
  ordinary_corporate_rate: 0.125
steps:
  assumed_taxable_uplift: established_arm_length_value - established_tax_carrying_value
  isolated_tax_before_other_rules: assumed_taxable_uplift * ordinary_corporate_rate
expected:
  assumed_taxable_uplift: 40000
  isolated_tax_before_other_rules: 5000
```
