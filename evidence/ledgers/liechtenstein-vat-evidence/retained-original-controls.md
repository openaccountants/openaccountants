# Retained original Liechtenstein VAT controls

All four24October2026 predecessor calculation blocks and assumptions are preserved byte-for-byte. The30October writer methods still await independent whole-pack review.

Amounts are hypothetical unless expressly identified otherwise. A passing calculation establishes neither classification nor permission to file.

### VAT-inclusive ordinary domestic invoice

Assume an established domestic standard-rate taxable supply for CHF 10,810 gross. The customer country/name alone is not that evidence.

```oa-check
name: Liechtenstein assumed standard VAT inclusive invoice
inputs:
  established_gross_price: 10810
  established_rate: 0.081
steps:
  net_price: established_gross_price / (1 + established_rate)
  output_vat: established_gross_price - net_price
expected:
  net_price: 10000
  output_vat: 810
```

### Qualifying reduced goods and accommodation

Assume separately classified domestic supplies: CHF 1,000 net qualifying reduced-rate goods and CHF 200 net qualifying accommodation. A restaurant meal is not included in the reduced goods assumption.

```oa-check
name: Liechtenstein assumed reduced goods and accommodation rates
inputs:
  established_reduced_net: 1000
  reduced_rate: 0.026
  established_accommodation_net: 200
  accommodation_rate: 0.038
steps:
  reduced_vat: established_reduced_net * reduced_rate
  accommodation_vat: established_accommodation_net * accommodation_rate
  combined_output_vat: reduced_vat + accommodation_vat
expected:
  reduced_vat: 26
  accommodation_vat: 7.60
  combined_output_vat: 33.60
```

### Acquisition tax with supported partial input entitlement

Assume an article-10 registered recipient, an established domestic article 8(1) service from a qualifying unregistered foreign supplier, no article 45a exclusion, a CHF 1,000 net base and documented 70% input entitlement under the effective method. Assess CHF 81 acquisition tax, with CHF 56.70 deductible and CHF 24.30 remaining. The supplier brand does not establish these gates.

```oa-check
name: Liechtenstein assumed acquisition tax with partial input entitlement
inputs:
  established_service_base: 1000
  established_rate: 0.081
  established_deductible_fraction: 0.70
steps:
  acquisition_tax: established_service_base * established_rate
  deductible_input: acquisition_tax * established_deductible_fraction
  net_tax_effect: acquisition_tax - deductible_input
expected:
  acquisition_tax: 81
  deductible_input: 56.70
  net_tax_effect: 24.30
```

### Invoice food versus restaurant classification

The same CHF 500 net food value gives CHF 13 at 2.6% only on established qualifying goods/takeaway facts, versus CHF 40.50 for a normal-rate restaurant service. The CHF 27.50 difference is a classification control, not an election for the cheaper result.

```oa-check
name: Liechtenstein assumed food supply classification comparison
inputs:
  established_net_price: 500
  qualifying_reduced_rate: 0.026
  restaurant_rate: 0.081
steps:
  qualifying_goods_vat: established_net_price * qualifying_reduced_rate
  restaurant_vat: established_net_price * restaurant_rate
  difference: restaurant_vat - qualifying_goods_vat
expected:
  qualifying_goods_vat: 13
  restaurant_vat: 40.50
  difference: 27.50
```
