# Moldova individual deduction and capital allocation controls

Writer arithmetic only; independent whole-country review remains pending. Read 30 October 2026. Sources: [Code35^2(6),40–42](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [January education rule](https://www.legis.md/cautare/getResults?doc_id=149766&lang=ro), and [Government693/2018 annex2 points35^1,39–44](https://www.legis.md/cautare/getResults?doc_id=154927&lang=ro). These controls do not add examples to the Guide, which retains exactly two.

## Education is one aggregate cap

Assume an eligible resident's own qualifying education costs12000 and qualifying dependent-child education costs9000 and5000, all actually paid in2026 with the applicable evidence. The statutory institution/beneficiary conditions are established; there is no duplicate or employer-funded claim. Assume60000 ordinary taxable income before this deduction, with no other adjustments or exemption. Aggregate26000 produces the statutory20000 deduction, not20000 per beneficiary or the generic form's outdated one-forecast-salary cap. Resulting tax is4800 at12%, a2400 reduction from7200. The scenario assumes evidence and eligibility; arithmetic does not establish them.

```oa-check
name: Moldova 2026 education aggregate cap
inputs:
  eligible_own_education_paid: 12000
  eligible_child_one_education_paid: 9000
  eligible_child_two_education_paid: 5000
  taxable_income_before_education: 60000
steps:
  total_eligible_education_paid: eligible_own_education_paid + eligible_child_one_education_paid + eligible_child_two_education_paid
  education_deduction: min(total_eligible_education_paid, 20000)
  nondeducted_education_excess: max(0, total_eligible_education_paid - education_deduction)
  taxable_income_after_education: max(0, taxable_income_before_education - education_deduction)
  tax_before_education: taxable_income_before_education * 0.12
  tax_after_education: taxable_income_after_education * 0.12
  tax_reduction: tax_before_education - tax_after_education
expected:
  total_eligible_education_paid: 26000
  education_deduction: 20000
  nondeducted_education_excess: 6000
  taxable_income_after_education: 40000
  tax_before_education: 7200
  tax_after_education: 4800
  tax_reduction: 2400
```

## Acquisition, ownership and instalment allocations remain distinct

Assume a single acquisition costs60000 for two capital assets whose established transaction-date market values are40000 and60000. Allocate24000 to assetA and36000 to assetB. AssetA is sold for40000, without a nonrecognition exemption, other capital losses or other tax adjustments. In an alternative2026 joint-owner scenario, the owner's25% share takes both10000 proceeds and6000 cost, leaving4000 gain,2000 taxable inclusion and240 tax at12%.

In a separate instalment scenario for all of assetA, the contract allocates60% of price to2026 and40% to a later tax period. The2026 calculation uses24000 proceeds and14400 cost, giving9600 gain,4800 taxable inclusion and576 tax. The remaining16000 proceeds and9600 cost reconcile the unused basis; the control does not assert a future year's inclusion fraction or tax rate. Neither an ownership fraction nor a payment fraction permits deducting the full original24000 cost repeatedly. Actual transaction dates, lawful cost, contract shares, residence, recognition and current-period rates are assumed established.

```oa-check
name: Moldova 2026 capital acquisition ownership and payment allocations
inputs:
  total_acquisition_price: 60000
  asset_a_market_value_at_acquisition: 40000
  asset_b_market_value_at_acquisition: 60000
  asset_a_sale_proceeds: 40000
  alternative_owner_fraction: 0.25
  first_period_contract_fraction: 0.60
steps:
  combined_market_value: asset_a_market_value_at_acquisition + asset_b_market_value_at_acquisition
  asset_a_allocated_cost: total_acquisition_price * asset_a_market_value_at_acquisition / combined_market_value
  asset_b_allocated_cost: total_acquisition_price * asset_b_market_value_at_acquisition / combined_market_value
  alternative_owner_proceeds: asset_a_sale_proceeds * alternative_owner_fraction
  alternative_owner_cost: asset_a_allocated_cost * alternative_owner_fraction
  alternative_owner_gain: alternative_owner_proceeds - alternative_owner_cost
  alternative_owner_taxable_inclusion: alternative_owner_gain * 0.50
  alternative_owner_tax: alternative_owner_taxable_inclusion * 0.12
  first_period_proceeds: asset_a_sale_proceeds * first_period_contract_fraction
  first_period_cost: asset_a_allocated_cost * first_period_contract_fraction
  first_period_gain: first_period_proceeds - first_period_cost
  first_period_taxable_inclusion: first_period_gain * 0.50
  first_period_tax: first_period_taxable_inclusion * 0.12
  remaining_contract_proceeds: asset_a_sale_proceeds - first_period_proceeds
  remaining_cost_not_reused: asset_a_allocated_cost - first_period_cost
  total_raw_gain_reconciliation: first_period_gain + remaining_contract_proceeds - remaining_cost_not_reused
expected:
  combined_market_value: 100000
  asset_a_allocated_cost: 24000
  asset_b_allocated_cost: 36000
  alternative_owner_proceeds: 10000
  alternative_owner_cost: 6000
  alternative_owner_gain: 4000
  alternative_owner_taxable_inclusion: 2000
  alternative_owner_tax: 240
  first_period_proceeds: 24000
  first_period_cost: 14400
  first_period_gain: 9600
  first_period_taxable_inclusion: 4800
  first_period_tax: 576
  remaining_contract_proceeds: 16000
  remaining_cost_not_reused: 9600
  total_raw_gain_reconciliation: 16000
```
