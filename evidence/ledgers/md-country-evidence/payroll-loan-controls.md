# Moldova ordinary MDL employer-loan benefit controls

Writer controls only; independent whole-country review pending. Read30October2026. Sources: [current Code19(d)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Government697point8(4)](https://www.legis.md/cautare/getResults?doc_id=152473&lang=ro), [visually inspected formula image](https://www.legis.md/UserFiles/images/RO/2020/mo165-176md/formula_543.png), and [BNMDPMC8 configured forNovember2025](https://bnm.md/bdi/pages/reports/dpmc/DPMC8.xhtml?id=0&lang=ro). The exact returned report text/query settings are retained in sources/fiscal-code-article-BNM-NOV2025-LOANS.json. Its domestic-currency new-individual-total over-five-year rate is8.32%. This is not the all-bank/all-term total, the individual-entrepreneur rate or the monetary-policy base.

The numeric balances, contract rates and established days are assumed facts, not statutory thresholds. Both scenarios assume a genuine employer/employee loan outside the bank/non-bank general-customer exception. They determine the PIT benefit value only, without deciding contribution bases, actual collection, cumulative relief, no-cash remittance or final monetary rounding. The Guides retain exactly two examples each; these are separate controls.

## Interest-free ordinary MDL loan, full30-day month

Assume36500MDL outstanding throughout30established days of use inApril2026, with no principal change, no employee interest and no exception. The image's365-day denominator gives249.60benefit. Do not round8.32% up to9%, substitute the6% policy rate, or divide the annual benefit by12 regardless of days.

```oa-check
name: Moldova 2026 ordinary MDL interest free employer loan
inputs:
  sourced_november2025_individual_mdl_rate_percent: 8.32
  actual_employee_rate_percent: 0
  assumed_loan_balance_mdl: 36500
  established_use_days_in_month: 30
steps:
  positive_rate_gap_percent: max(0, sourced_november2025_individual_mdl_rate_percent - actual_employee_rate_percent)
  monthly_benefit_mdl: assumed_loan_balance_mdl * established_use_days_in_month / 365 * positive_rate_gap_percent / 100
expected:
  positive_rate_gap_percent: 8.32
  monthly_benefit_mdl: 249.60
tolerance: 0.00000001
```

## Principal repayment and no positive benefit at a higher contract rate

Assume an ordinary MDL loan at3%contract interest. Records establish36500principal for the first10days and29200for the following20days of a30-day month, after7300has been correctly allocated to principal. The two benefit segments are53.20and85.12,total138.32. Using the unchanged original balance for all30days would give159.60and overstate the benefit by21.28. The10/20-day segmentation is an established scenario fact; this does not settle real transaction-day conventions. In a separate alternative with9%contract interest and the same8.32%benchmark, there is no positive rate gap and the interest benefit is zero. This does not make actual loan interest or debt forgiveness tax-free under every other provision.

```oa-check
name: Moldova 2026 employer loan repayment and positive difference
inputs:
  sourced_november2025_individual_mdl_rate_percent: 8.32
  actual_employee_rate_percent: 3
  first_balance_mdl: 36500
  accepted_principal_repayment_mdl: 7300
  first_segment_use_days: 10
  second_segment_use_days: 20
  alternative_higher_contract_rate_percent: 9
steps:
  positive_rate_gap_percent: max(0, sourced_november2025_individual_mdl_rate_percent - actual_employee_rate_percent)
  second_balance_mdl: first_balance_mdl - accepted_principal_repayment_mdl
  first_segment_benefit_mdl: first_balance_mdl * first_segment_use_days / 365 * positive_rate_gap_percent / 100
  second_segment_benefit_mdl: second_balance_mdl * second_segment_use_days / 365 * positive_rate_gap_percent / 100
  actual_monthly_benefit_mdl: first_segment_benefit_mdl + second_segment_benefit_mdl
  unchanged_balance_benefit_mdl: first_balance_mdl * (first_segment_use_days + second_segment_use_days) / 365 * positive_rate_gap_percent / 100
  unchanged_balance_overstatement_mdl: unchanged_balance_benefit_mdl - actual_monthly_benefit_mdl
  alternative_positive_rate_gap_percent: max(0, sourced_november2025_individual_mdl_rate_percent - alternative_higher_contract_rate_percent)
  alternative_interest_benefit_mdl: first_balance_mdl * (first_segment_use_days + second_segment_use_days) / 365 * alternative_positive_rate_gap_percent / 100
expected:
  positive_rate_gap_percent: 5.32
  second_balance_mdl: 29200
  first_segment_benefit_mdl: 53.20
  second_segment_benefit_mdl: 85.12
  actual_monthly_benefit_mdl: 138.32
  unchanged_balance_benefit_mdl: 159.60
  unchanged_balance_overstatement_mdl: 21.28
  alternative_positive_rate_gap_percent: 0
  alternative_interest_benefit_mdl: 0
tolerance: 0.00000001
```
