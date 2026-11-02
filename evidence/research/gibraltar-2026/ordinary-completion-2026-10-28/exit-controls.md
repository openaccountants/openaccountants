# Supplementary residence-exit retained-PE boundary

Explicit assumptions: established paragraph18A(1)(c)corporate residence transfer; the first asset is chargeable under18A(2); the second remains effectively connected with a GibraltarPEand is excluded from this event. Values/classifications are assumed supported evidence, not determined by this control. No final tax or later-disposal exemption is calculated.

```oa-check
name: Gibraltar residence exit excludes retained PE asset
inputs:
  chargeable_market_value: 1000000
  chargeable_tax_value: 600000
  retained_pe_market_value: 300000
  retained_pe_tax_value: 150000
steps:
  - chargeable_exit_base: chargeable_market_value - chargeable_tax_value
  - retained_pe_difference_not_in_this_charge: retained_pe_market_value - retained_pe_tax_value
  - included_retained_pe_base: 0
  - total_event_base: chargeable_exit_base + included_retained_pe_base
expected:
  chargeable_exit_base: 400000
  retained_pe_difference_not_in_this_charge: 150000
  included_retained_pe_base: 0
  total_event_base: 400000
```
