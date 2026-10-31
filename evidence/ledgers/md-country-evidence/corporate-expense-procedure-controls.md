# Moldova corporate expense procedure controls

Writer controls only, read2026-10-30. Sources: [Government693/2018 annex1 points34–41,51–55](https://www.legis.md/cautare/getResults?doc_id=154927&lang=ro), [Code33(1)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), and the [official17400 forecast input](https://cnas.gov.md/sites/default/files/2026-10/Particularitati2026.pdf). Actual legal eligibility, business purpose, status, gross-income base and records are hypothetical assumptions. These are not independent review or taxpayer-specific conclusions.

The representation control assumes one properly documented delegation and statutory gross income containing no excluded-income/base ambiguity. Apply the gift sublimit before the combined representation ceiling; the final add-back must not count the same expenditure twice.

```oa-check
name: Moldova representation overall ceiling and delegate gift sublimit
inputs:
  statutory_gross_income: 2000000
  representation_expense: 20000
  gift_one: 500
  gift_two: 700
  standard_annual_personal_exemption: 29700
steps:
  gift_limit_per_delegate: standard_annual_personal_exemption * 0.02
  gifts_within_sublimit: min(gift_one, gift_limit_per_delegate) + min(gift_two, gift_limit_per_delegate)
  gift_sublimit_excess: gift_one + gift_two - gifts_within_sublimit
  eligible_before_overall_cap: representation_expense - gift_sublimit_excess
  overall_representation_cap: statutory_gross_income * 0.0075
  allowed_representation: min(eligible_before_overall_cap, overall_representation_cap)
  total_representation_add_back: representation_expense - allowed_representation
expected:
  gift_limit_per_delegate: 594
  gifts_within_sublimit: 1094
  gift_sublimit_excess: 106
  eligible_before_overall_cap: 19894
  overall_representation_cap: 15000
  allowed_representation: 15000
  total_representation_add_back: 5000
```

For the organised employee food/transport control, assume20average employees and the same20actual recipients for22actual days, with all policy/consent/route/attendance and cost evidence. The positive wage gap supports the stipulated ordinary meal gate. Above-cap benefit amounts are not labelled permanent CIT disallowances: the taxed-payment deduction is a separate legal test.

```oa-check
name: Moldova organised employee meal gate and food transport caps
inputs:
  monthly_payroll: 300000
  average_employees: 20
  forecast_monthly_average: 17400
  actual_recipients: 20
  actual_work_transport_days: 22
  monthly_food_cost_ex_vat: 35000
  monthly_transport_cost_ex_vat: 40000
steps:
  employer_average_gross_pay: monthly_payroll / average_employees
  ordinary_food_wage_threshold: forecast_monthly_average * 0.75
  wage_above_threshold: employer_average_gross_pay - ordinary_food_wage_threshold
  person_days: actual_recipients * actual_work_transport_days
  standard_food_cap: person_days * 70
  food_above_standard_cap: max(monthly_food_cost_ex_vat - standard_food_cap, 0)
  standard_transport_cap: person_days * 75
  transport_above_standard_cap: max(monthly_transport_cost_ex_vat - standard_transport_cap, 0)
expected:
  employer_average_gross_pay: 15000
  ordinary_food_wage_threshold: 13050
  wage_above_threshold: 1950
  person_days: 440
  standard_food_cap: 30800
  food_above_standard_cap: 4200
  standard_transport_cap: 33000
  transport_above_standard_cap: 7000
```

The insurance control assumes qualifying paid business policies:80000within the combined55(2)(h)–(l)classes and20000in the separately identified motor-property class55(2)(c), with no subsidy/employee/private-use issue. It does not apply3%to every insurance class or repeat3%per policy.

```oa-check
name: Moldova insurance combined listed-class cap
inputs:
  statutory_gross_income_all_sources: 2000000
  listed_h_to_l_premiums_paid: 80000
  separate_motor_premium_paid: 20000
steps:
  listed_class_combined_cap: statutory_gross_income_all_sources * 0.03
  allowed_listed_class_premiums: min(listed_h_to_l_premiums_paid, listed_class_combined_cap)
  listed_class_excess: listed_h_to_l_premiums_paid - allowed_listed_class_premiums
  total_qualifying_insurance_deduction: allowed_listed_class_premiums + separate_motor_premium_paid
expected:
  listed_class_combined_cap: 60000
  allowed_listed_class_premiums: 60000
  listed_class_excess: 20000
  total_qualifying_insurance_deduction: 80000
```


## Resident company disposal: repair the subsequently merged example's scope

Writer control, independent legal review pending. Reuse only the hypothetical inputs in PR #1008's first example: an ordinary resident SRL with accounting profit 900,000 including an 80,000 share-disposal gain and a 15,000 statutory fine, no other adjustments/losses/credits, and 96,000 evidenced instalments. Assume the booked disposal gain already equals the ordinary tax result. Current Code arts. 14(1)(a), 18(a)/(o), 24, 30 and 37–40 do not give this SRL the nonbusiness individual's 50% exclusion. Add back the fine; retain the full booked gain. The counterfactual excluded-half result below is labelled wrong and retained solely to quantify the published example's error, not as an available company election.

Primary source read 30 October 2026: https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro (arts. 14, 18, 24, 30, 37–40, 83–84 and 87). Exact scope observations and the full incoming example are retained in the source ledger and predecessor reconciliation.

```oa-check
name: Moldova resident company capital gain scope and fine addback
inputs:
  accounting_profit_including_full_gain: 900000
  statutory_fine: 15000
  gain_already_in_profit: 80000
  prior_year_tax: 96000
  evidenced_instalments: 96000
steps:
  taxable_income: accounting_profit_including_full_gain + statutory_fine
  ordinary_company_tax: taxable_income * 0.12
  balance_due: ordinary_company_tax - evidenced_instalments
  counterfactual_wrong_excluded_half: gain_already_in_profit * 0.50
  counterfactual_wrong_company_tax: (taxable_income - counterfactual_wrong_excluded_half) * 0.12
  understated_tax_from_wrong_scope: ordinary_company_tax - counterfactual_wrong_company_tax
  instalment_comparison: min(prior_year_tax, ordinary_company_tax * 0.80)
  instalment_shortfall: max(0, instalment_comparison - evidenced_instalments)
expected:
  taxable_income: 915000
  ordinary_company_tax: 109800
  balance_due: 13800
  counterfactual_wrong_excluded_half: 40000
  counterfactual_wrong_company_tax: 105000
  understated_tax_from_wrong_scope: 4800
  instalment_comparison: 87840
  instalment_shortfall: 0
```
