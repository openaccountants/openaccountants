# Liechtenstein ordinary unquoted-share valuation controls

Hypothetical full-year CHF accounts. These controls implement SteV 7a and Annex 1 A–C, consolidation 1 July 2026, read 31 October 2026: https://www.gesetze.li/konso/pdf/2010437000 . The company is operating and has representative results unless the case states otherwise. Actual classifications, reserves and article 54 asset determinations are established assumptions. No independent-transfer override applies. Figures are not real client data. Helper rounding is separately labelled; no final tax-rounding rule is inferred.

## Ordinary valuation and separate voting-right boundaries

Established after-appropriation equity CHF450,000, participation hidden reserves CHF30,000 and taxed hidden reserves CHF20,000 produce S=CHF500,000. Current adjusted annual earnings CHF120,000 and preceding earnings CHF90,000 give weighted earnings CHF110,000, a risk-adjusted CHF93,500, E=CHF623,333.333333, U=CHF582,222.222222 above the CHF300,000 minimum. The helper rounds the company to CHF582,200. For the same 10% economic interest, voting rights below20%, exactly20%, or exactly50% give holder amounts CHF46,576 / CHF52,398 / CHF58,220 respectively. This deliberately separates capital and votes; it does not copy F70 into both facts.

```oa-check
name: LI ordinary share valuation and voting-right boundaries
inputs:
  equity_after_appropriation: 450000
  participation_hidden_reserves: 30000
  taxed_hidden_reserves: 20000
  current_adjusted_annual_earnings: 120000
  prior_adjusted_annual_earnings: 90000
  risk_factor: 0.85
  ordinary_capitalisation_rate: 0.15
  minimum_substance_factor: 0.6
  economic_interest: 0.1
  discount_below_20_votes: 0.2
  discount_at_20_votes: 0.1
  discount_at_50_votes: 0
steps:
  substance: equity_after_appropriation + participation_hidden_reserves + taxed_hidden_reserves
  weighted_earnings: (2 * current_adjusted_annual_earnings + prior_adjusted_annual_earnings) / 3
  risk_adjusted_earnings: max(0, weighted_earnings * risk_factor)
  earnings_value: risk_adjusted_earnings / ordinary_capitalisation_rate
  weighted_company: (2 * earnings_value + substance) / 3
  minimum_company: minimum_substance_factor * substance
  statutory_company: max(weighted_company, minimum_company)
  helper_rounded_company: floor(statutory_company / 100) * 100
  holder_below_20_votes: helper_rounded_company * economic_interest * (1 - discount_below_20_votes)
  holder_at_20_votes: helper_rounded_company * economic_interest * (1 - discount_at_20_votes)
  holder_at_50_votes: helper_rounded_company * economic_interest * (1 - discount_at_50_votes)
expected:
  substance: 500000
  weighted_earnings: 110000
  risk_adjusted_earnings: 93500
  earnings_value: 623333.333333
  weighted_company: 582222.222222
  minimum_company: 300000
  statutory_company: 582222.222222
  helper_rounded_company: 582200
  holder_below_20_votes: 46576
  holder_at_20_votes: 52398
  holder_at_50_votes: 58220
```

## Negative earnings and the substance floor

The negative weighted result produces E=0, not a negative earnings value. The weighted company value of CHF166,666.666667 is increased to the CHF300,000 minimum.

```oa-check
name: LI negative earnings value and minimum substance
inputs:
  current_adjusted_earnings: -12000
  prior_adjusted_earnings: -9000
  substance: 500000
  risk_factor: 0.85
  capitalisation_rate: 0.15
  minimum_substance_factor: 0.6
steps:
  weighted_earnings: (2 * current_adjusted_earnings + prior_adjusted_earnings) / 3
  earnings_value: max(0, weighted_earnings * risk_factor / capitalisation_rate)
  weighted_company: (2 * earnings_value + substance) / 3
  minimum_company: substance * minimum_substance_factor
  statutory_company: max(weighted_company, minimum_company)
expected:
  weighted_earnings: -11000
  earnings_value: 0
  weighted_company: 166666.666667
  minimum_company: 300000
  statutory_company: 300000
```

## Non-operating assets and related net earnings

Assume CHF150,000 is correctly established as the shareholder/non-operating asset pool under SteG54, within total S of CHF500,000. Current/prior related net earnings CHF1,000 each are inside the given CHF121,000/CHF91,000 results. Remove both those results and the asset pool from the operating weighting, then add the asset pool back once. The statutory floor is 60%×CHF350,000+CHF150,000=CHF360,000. The weighted total is CHF682,222.222222. Actual article54 classification, tax adjustments and asset values are not proved by this conservation control.

```oa-check
name: LI non-operating assets removed and restored once
inputs:
  total_substance: 500000
  established_nonoperating_assets: 150000
  current_total_earnings: 121000
  prior_total_earnings: 91000
  current_nonoperating_net_earnings: 1000
  prior_nonoperating_net_earnings: 1000
  risk_factor: 0.85
  capitalisation_rate: 0.15
  minimum_operating_substance_factor: 0.6
steps:
  operating_substance: total_substance - established_nonoperating_assets
  current_operating_earnings: current_total_earnings - current_nonoperating_net_earnings
  prior_operating_earnings: prior_total_earnings - prior_nonoperating_net_earnings
  operating_earnings_value: max(0, (2 * current_operating_earnings + prior_operating_earnings) * risk_factor / (3 * capitalisation_rate))
  operating_weighted_company: (2 * operating_earnings_value + operating_substance) / 3
  total_weighted_company: operating_weighted_company + established_nonoperating_assets
  minimum_company: operating_substance * minimum_operating_substance_factor + established_nonoperating_assets
  statutory_company: max(total_weighted_company, minimum_company)
expected:
  operating_substance: 350000
  current_operating_earnings: 120000
  prior_operating_earnings: 90000
  operating_earnings_value: 623333.333333
  operating_weighted_company: 532222.222222
  total_weighted_company: 682222.222222
  minimum_company: 360000
  statutory_company: 682222.222222
```

## FMA rate versus substance-method classifications

Assume a regulated operating financial institution within Annex1A uses K=20%, producing E=CHF467,500 and U=CHF478,333.333333. A holding/property/inactive/liquidating company within B instead uses established S of CHF500,000. A new company without representative results uses S under A(2). A bank/insurer is not classified as a B finance company merely because it is financial. This control does not extend C's minority deduction from A to B.

```oa-check
name: LI FMA earnings capitalisation versus substance-only methods
inputs:
  current_adjusted_earnings: 120000
  prior_adjusted_earnings: 90000
  risk_factor: 0.85
  fma_capitalisation_rate: 0.2
  substance: 500000
  minimum_substance_factor: 0.6
steps:
  fma_earnings_value: max(0, (2 * current_adjusted_earnings + prior_adjusted_earnings) * risk_factor / (3 * fma_capitalisation_rate))
  fma_weighted_company: (2 * fma_earnings_value + substance) / 3
  fma_company: max(fma_weighted_company, minimum_substance_factor * substance)
  qualifying_annex_b_company: substance
  new_company_without_representative_results: substance
expected:
  fma_earnings_value: 467500
  fma_weighted_company: 478333.333333
  fma_company: 478333.333333
  qualifying_annex_b_company: 500000
  new_company_without_representative_results: 500000
```
