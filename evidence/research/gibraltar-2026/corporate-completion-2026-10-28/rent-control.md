# Conditional rented-premises control

Assumes the relevant rent was paid, income-producing amounts were independently supported, paragraph2(1)(a) applies, and no greater-sum exception is relied on. No business-use percentage or tax outcome is inferred.

```oa-check
name: Rented domestic premises business amount and two-thirds cap
inputs:
  relevant_bona_fide_rent: 18000
  established_income_producing_rent: 9000
  higher_established_income_producing_rent: 14400
steps:
  - ordinary_rent_cap: relevant_bona_fide_rent * 2 / 3
  - first_amount_within_tests: min(established_income_producing_rent, ordinary_rent_cap)
  - higher_amount_within_tests: min(higher_established_income_producing_rent, ordinary_rent_cap)
expected:
  ordinary_rent_cap: 12000
  first_amount_within_tests: 9000
  higher_amount_within_tests: 12000
```
