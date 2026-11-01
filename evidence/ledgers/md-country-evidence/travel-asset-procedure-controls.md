# Moldova travel and asset procedure controls

Writer arithmetic controls, read 30 October 2026. These do not constitute independent review or an actual taxpayer computation. Sources: [HG10/2012 current regulation points19^1,21–25](https://www.legis.md/cautare/getResults?doc_id=145854&lang=ro), [HG704/2019 points12–14,24–28,32–36](https://www.legis.md/cautare/getResults?doc_id=146665&lang=ro), and [Code26^1](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro). Guide examples remain exactly two per Guide; these extra controls are separate writer evidence.

## Distinct daily-allowance and lodging branches

Assume an annex daily norm of **100** and lodging ceiling of **200** in a hypothetical currency. Neither number is claimed as a statutory destination rate. The traveller's category, ordinary authorised trip, records and host-funding tests are assumed satisfied. A chosen private-sector70% allowance is70 per eligible day. This is a separate scenario from the full-norm65-day foreign-trip decision reducing days61–65 to50%. A one-day domestic trip has no allowance; a one-day foreign trip uses the full norm in that scenario. Two actual documented lodging nights of250 and150 average200; the no-document50% route is a different one-night scenario, assuming no free or host-funded lodging. Do not add those alternative scenarios together or multiply70% by50%.

```oa-check
name: Moldova distinct travel daily allowance and lodging branches
inputs:
  assumed_annex_daily_norm: 100
  assumed_lodging_ceiling: 200
  eligible_days_private_choice: 3
  foreign_days_full_norm: 60
  foreign_additional_days_manager_half_choice: 5
  documented_night_one: 250
  documented_night_two: 150
steps:
  private_daily_choice: assumed_annex_daily_norm * 0.70
  private_three_day_allowance: private_daily_choice * eligible_days_private_choice
  same_day_domestic_allowance: assumed_annex_daily_norm * 0
  same_day_foreign_full_norm: assumed_annex_daily_norm
  foreign_sixty_five_day_separate_scenario: foreign_days_full_norm * assumed_annex_daily_norm + foreign_additional_days_manager_half_choice * assumed_annex_daily_norm * 0.50
  average_documented_lodging: (documented_night_one + documented_night_two) / 2
  no_document_one_night_separate_scenario: assumed_lodging_ceiling * 0.50
expected:
  private_daily_choice: 70
  private_three_day_allowance: 210
  same_day_domestic_allowance: 0
  same_day_foreign_full_norm: 100
  foreign_sixty_five_day_separate_scenario: 6250
  average_documented_lodging: 200
  no_document_one_night_separate_scenario: 100
```

## Ordinary depreciation and alternative disposal outcomes

Assume an ordinary qualifying asset with verified cost120000 and lawful five-year life, commissioned in February2026, no subsequent costs, grants or special method. It is sold in November: ordinary depreciation covers March through November inclusive, nine months. A sale at110000 gives8000 tax gain after18000 tax depreciation. The lower-market-value donation and taxable insurance-compensation routes below are **alternative** disposals of an identical asset with the same tax balance, not successive deductions. The donated asset's assumed market value is95000; the positive donation result is zero. A forced-loss case has20000 qualifying taxable insurance compensation and can deduct at most20000 of the102000 remaining tax value. This does not authorise a second depreciation or full forced-loss write-off.

```oa-check
name: Moldova ordinary asset depreciation through disposal month
inputs:
  verified_tax_entry_cost: 120000
  verified_useful_life_years: 5
  eligible_months_march_through_november: 9
  assumed_sale_proceeds: 110000
  assumed_donation_market_value: 95000
  assumed_qualifying_taxable_insurance: 20000
steps:
  annual_straight_line: verified_tax_entry_cost / verified_useful_life_years
  depreciation_through_disposal_month: annual_straight_line / 12 * eligible_months_march_through_november
  tax_undepreciated_value: verified_tax_entry_cost - depreciation_through_disposal_month
  sale_tax_result: assumed_sale_proceeds - tax_undepreciated_value
  alternative_donation_tax_result: max(0, assumed_donation_market_value - tax_undepreciated_value)
  alternative_forced_loss_deduction: min(tax_undepreciated_value, assumed_qualifying_taxable_insurance)
expected:
  annual_straight_line: 24000
  depreciation_through_disposal_month: 18000
  tax_undepreciated_value: 102000
  sale_tax_result: 8000
  alternative_donation_tax_result: 0
  alternative_forced_loss_deduction: 20000
```

## Qualifying leased-asset repair excess

Assume an ordinary qualifying operating-lease contract originally longer than12 months, with repair costs borne by the user,200000 accrued annual lease charges and50000 qualifying repair costs. No aircraft, owned taxi or short-contract exception applies. Current repair deduction is30000;20000 becomes a separate investment asset when the repair completes in March. The remaining contract term is30 months and the underlying asset's verified useful life is48 months. The entity chooses the ordinary shorter30-month life, without electing a longer one. April–December gives nine depreciation months and6000 tax depreciation, separate from the current30000 repair deduction. Actual eligibility, lawful life and approved annex/register records are assumed, not established by this arithmetic.

```oa-check
name: Moldova ordinary leased asset repair cap and excess asset
inputs:
  annual_accrued_lease_charges: 200000
  qualifying_repairs: 50000
  remaining_contract_months: 30
  underlying_lawful_life_months: 48
  months_after_march_completion: 9
steps:
  ordinary_repair_cap: annual_accrued_lease_charges * 0.15
  current_repair_deduction: min(qualifying_repairs, ordinary_repair_cap)
  separate_investment_basis: max(0, qualifying_repairs - current_repair_deduction)
  chosen_ordinary_life_months: min(remaining_contract_months, underlying_lawful_life_months)
  current_year_investment_depreciation: separate_investment_basis / chosen_ordinary_life_months * months_after_march_completion
  combined_current_deductions: current_repair_deduction + current_year_investment_depreciation
expected:
  ordinary_repair_cap: 30000
  current_repair_deduction: 30000
  separate_investment_basis: 20000
  chosen_ordinary_life_months: 30
  current_year_investment_depreciation: 6000
  combined_current_deductions: 36000
```
