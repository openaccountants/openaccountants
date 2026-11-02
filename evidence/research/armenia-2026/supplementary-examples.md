# Preserved Armenia supplementary calculations

## Offshore management cap and registration-year branch

Assume documented actual management services from a provider within Code 118, no exception, annual gross income AMD 50 million and management cost AMD 3 million. The ordinary 2% limit is 1 million, so disallow 2 million. In the statutory registration year, max(2% of gross, 2 million) permits 2 million and disallows 1 million. This does not prove a service is management rather than excluded management consultancy, or settle transfer pricing/withholding. [Tax Code 118](https://www.arlis.am/hy/acts/215611/latest), read 26 October 2026.

```oa-check
name: Armenia offshore management cap ordinary and registration year
inputs:
  annual_gross_income: 50000000
  qualifying_management_cost: 3000000
steps:
  - ordinary_deduction: min(qualifying_management_cost, annual_gross_income * 0.02)
  - ordinary_disallowance: qualifying_management_cost - ordinary_deduction
  - registration_deduction: min(qualifying_management_cost, max(annual_gross_income * 0.02, 2000000))
  - registration_disallowance: qualifying_management_cost - registration_deduction
expected:
  ordinary_deduction: 1000000
  ordinary_disallowance: 2000000
  registration_deduction: 2000000
  registration_disallowance: 1000000
```

## Social expense caps, earlier tax refunds and offset before cash

Assume all service, person, signed-declaration, noncash and invoice conditions are established; eligible insurance expense AMD 100,000 and education expense 120,000. Health caps at 50,000, education at 100,000 and their combined cap at 100,000. Annual tax is 120,000, comprising 100,000 monthly tax and 20,000 independently declared tax; earlier qualifying refunds consumed 50,000. Available tax permits 70,000 reimbursement: offset 20,000 annual tax first, then 50,000 cash, within the remaining monthly tax. An expense cap is not an unconditional bank refund. [1067-N 8–9](https://www.arlis.am/hy/acts/206432/latest); [956-N 3–7](https://www.arlis.am/hy/acts/231590/latest), read 26 October 2026.

```oa-check
name: Armenia social expense reimbursement offset before cash
inputs:
  eligible_health_cost: 100000
  eligible_education_cost: 120000
  annual_tax: 120000
  monthly_tax: 100000
  independently_declared_tax: 20000
  earlier_refunds: 50000
steps:
  - health_limit: min(eligible_health_cost, 50000)
  - education_limit: min(eligible_education_cost, 100000)
  - expense_limit: min(health_limit + education_limit, 100000)
  - available_tax: max(annual_tax - earlier_refunds, 0)
  - reimbursement: min(expense_limit, available_tax)
  - annual_offset: min(independently_declared_tax, reimbursement)
  - annual_tax_to_pay: max(independently_declared_tax - annual_offset, 0)
  - cash_reimbursement: min(max(reimbursement - annual_offset, 0), max(monthly_tax - earlier_refunds, 0))
expected:
  expense_limit: 100000
  reimbursement: 70000
  annual_offset: 20000
  annual_tax_to_pay: 0
  cash_reimbursement: 50000
```

## Calendar-day sickness split under the current reform

Assume an eligible ordinary employee's case starts in 2026, ten certified calendar days, statutory average AMD 380,000 and nonbinding statutory caps/floor. Monthly sickness base is 80% × 380,000 = 304,000, daily 304,000/30.4 = 10,000. The employer's first seven calendar days cost 70,000, the state's remaining three 30,000. This is not the old five-working-day model or a benefit entitlement inferred from salary alone. [Benefits Law 6/8/22](https://www.arlis.am/hy/acts/205733/latest); [HO-73-N 11](https://www.arlis.am/hy/acts/205729/latest); [1024-N current Annex 5](https://www.arlis.am/hy/acts/196905/latest), read 26 October 2026.

```oa-check
name: Armenia current sickness calendar day payer split
inputs:
  statutory_average: 380000
  eligible_calendar_days: 10
steps:
  - sickness_monthly_base: statutory_average * 0.80
  - sickness_daily_base: sickness_monthly_base / 30.4
  - employer_days: min(eligible_calendar_days, 7)
  - state_days: max(eligible_calendar_days - 7, 0)
  - employer_benefit: sickness_daily_base * employer_days
  - state_benefit: sickness_daily_base * state_days
  - total_benefit: employer_benefit + state_benefit
expected:
  sickness_daily_base: 10000
  employer_benefit: 70000
  state_benefit: 30000
  total_benefit: 100000
```

## Leave pay and distinct termination grounds

Assume the fully established Labour 195 monthly average is AMD 420,000, a five-day week, ten granted working leave days and seventeen established unused days at termination. Daily average 420,000/21 = 20,000 gives leave pay 200,000 and unused-leave compensation 340,000. The stated redundancy branch gives one monthly average, 420,000; the different qualifying three-year-service scale branch gives 25 daily averages, 500,000. These are alternative legal grounds, not two cumulative severance payments. [Labour Code 129/159/169/170/195](https://www.arlis.am/hy/acts/51/latest), read 26 October 2026.

```oa-check
name: Armenia leave and alternative severance grounds
inputs:
  statutory_monthly_average: 420000
  granted_working_days: 10
  unused_working_days: 17
steps:
  - daily_average: statutory_monthly_average / 21
  - leave_pay: daily_average * granted_working_days
  - unused_leave_compensation: daily_average * unused_working_days
  - redundancy_severance: statutory_monthly_average
  - alternative_three_year_ground_severance: daily_average * 25
expected:
  daily_average: 20000
  leave_pay: 200000
  unused_leave_compensation: 340000
  redundancy_severance: 420000
  alternative_three_year_ground_severance: 500000
```

## Reinvested dividend refund is capped investment, not another 5 percent

Assume the same resident paying organisation, receipt-year qualifying capital investment AMD 3,000, tax actually paid on its dividend AMD 5,000, required capital/register evidence and no statutory refusal ground. Refund is min(3,000, 5,000) = 3,000, not 5% × 3,000 = 150. If the qualifying investment is 8,000, the refund is capped at the 5,000 tax actually paid. [Code 159(4)](https://www.arlis.am/hy/acts/215611/latest); [1371-N 1–5](https://www.arlis.am/hy/acts/200942/latest), read 26 October 2026.

```oa-check
name: Armenia dividend reinvestment refund cap
inputs:
  qualifying_small_investment: 3000
  qualifying_larger_investment: 8000
  dividend_tax_actually_paid: 5000
steps:
  - small_investment_refund: min(qualifying_small_investment, dividend_tax_actually_paid)
  - larger_investment_refund: min(qualifying_larger_investment, dividend_tax_actually_paid)
expected:
  small_investment_refund: 3000
  larger_investment_refund: 5000
```

## Turnover reduction carry through two quarters

Assume a qualifying ordinary trader, no special catering/border relief, documented eligible costs and the same activity in each quarter. First-quarter base AMD 10 million, eligible costs AMD 9.8 million and opening **tax-reduction** carry AMD 30,000: current reduction 931,000 plus opening 30,000; the 1% tax floor leaves payable tax 100,000 and unused reduction 61,000. Second-quarter base AMD 2 million and eligible costs AMD 1 million produce current reduction 95,000; with the 61,000 opening carry, payable tax is 44,000, above the 20,000 floor, leaving no carry. The cost balance is not carried again. [Tax Code 258(2)/(6)/(7), 260](https://www.arlis.am/hy/acts/215611/latest); [299-N instructions 12–17](https://www.arlis.am/hy/acts/201377/latest), read 26 October 2026.

```oa-check
name: Armenia turnover tax reduction two quarter carry
inputs:
  q1_base: 10000000
  q1_cost: 9800000
  q1_opening_reduction: 30000
  q2_base: 2000000
  q2_cost: 1000000
steps:
  - q1_gross: q1_base * 0.10
  - q1_floor: q1_base * 0.01
  - q1_reduction: q1_cost * 0.095 + q1_opening_reduction
  - q1_payable: max(q1_gross - q1_reduction, q1_floor)
  - q1_carry: max(q1_reduction - (q1_gross - q1_floor), 0)
  - q2_gross: q2_base * 0.10
  - q2_floor: q2_base * 0.01
  - q2_reduction: q2_cost * 0.095 + q1_carry
  - q2_payable: max(q2_gross - q2_reduction, q2_floor)
  - q2_carry: max(q2_reduction - (q2_gross - q2_floor), 0)
expected:
  q1_payable: 100000
  q1_carry: 61000
  q2_payable: 44000
  q2_carry: 0
```

## Turnover exit conversion is not an ordinary micro carry

Assume established turnover-to-ordinary exit, unused **tax-reduction** carries of AMD 6,000 trade, 2,000 production, 3,000 catering and 4,000 other activity, and AMD 2 million of ordinary taxable profit before this adjustment. Article 264(4)'s separate 10×/20×/10×/15× multipliers create AMD 190,000 of gross-income deductions, leaving 1,810,000 and company profit tax 325,800 at 18%. These multipliers do not apply to a direct micro exit, do not create input VAT and do not establish actual taxpayer eligibility. [Tax Code 125(1), 264(4), 272](https://www.arlis.am/hy/acts/215611/latest), read 26 October 2026.

```oa-check
name: Armenia turnover exit activity reduction conversion
inputs:
  trade_reduction_carry: 6000
  production_reduction_carry: 2000
  catering_reduction_carry: 3000
  other_reduction_carry: 4000
  ordinary_profit_before_conversion: 2000000
steps:
  - exit_deduction: trade_reduction_carry * 10 + production_reduction_carry * 20 + catering_reduction_carry * 10 + other_reduction_carry * 15
  - ordinary_profit_after_conversion: ordinary_profit_before_conversion - exit_deduction
  - company_tax: max(ordinary_profit_after_conversion, 0) * 0.18
expected:
  exit_deduction: 190000
  ordinary_profit_after_conversion: 1810000
  company_tax: 325800
```

These thirty-seven controls are retained from initial candidate df7247a4. They are research evidence, not extra Guides or proof that an actual taxpayer qualifies. Fourteen selected examples remain in the seven tax Guides. The original full text and all51 blocks remain in original-candidate.json. Legal applicability and later source corrections are controlled by the current Guides and review record.

## am-corporate-income-tax.md / Armenia representation ordinary and registration year

### 2. Representation: ordinary versus registration year

Annual gross income 200 million; established representation cost 1.8 million. Ordinary percentage cap is 1 million, below absolute cap 5 million: deduct 1 million, disallow 800,000. If instead the statutory registration-year exception is established, the 5-million absolute cap permits this 1.8-million cost. No special taxpayer facts are inferred. [116][code]

```oa-check
name: Armenia representation ordinary and registration year
inputs:
  gross_income: 200000000
  qualifying_cost: 1800000
steps:
  - ordinary_deduction: min(qualifying_cost, gross_income * 0.005, 5000000)
  - ordinary_disallowance: qualifying_cost - ordinary_deduction
  - registration_year_deduction: min(qualifying_cost, 5000000)
expected:
  ordinary_deduction: 1000000
  ordinary_disallowance: 800000
  registration_year_deduction: 1800000
```


## am-corporate-income-tax.md / Armenia production asset months and small asset

### 3. Production equipment and small asset

Qualifying production equipment original cost 30 million, lawful five-year term, six complete depreciation months in 2026: annual 6 million, current 3 million. Separate qualifying small depreciable asset cost 50,000 inclusive is fully deducted in acquisition year, no second ordinary depreciation. No incomplete month, improvement or special acceleration. [121(1)(3)/(6), (2)(1)][code]

```oa-check
name: Armenia production asset months and small asset
inputs:
  equipment_cost: 30000000
  selected_years: 5
  complete_months: 6
  qualifying_small_asset_cost: 50000
steps:
  - annual_equipment_depreciation: equipment_cost / selected_years
  - current_equipment_depreciation: annual_equipment_depreciation * complete_months / 12
  - small_asset_deduction: qualifying_small_asset_cost
expected:
  annual_equipment_depreciation: 6000000
  current_equipment_depreciation: 3000000
  small_asset_deduction: 50000
```


## am-corporate-income-tax.md / Armenia quarterly advance lower of statutory limbs

### 5. Quarterly advance uses the lower amount

Established Article 135 adjusted prior-year tax 10 million; defined prior-quarter income 60 million, no exception and correct return timing. Tax limb 2 million, income limb 1.2 million: advance 1.2 million. This is not 2 million or one-quarter of last year's tax. [135][code]

```oa-check
name: Armenia quarterly advance lower of statutory limbs
inputs:
  adjusted_prior_year_tax: 10000000
  defined_prior_quarter_income: 60000000
steps:
  - tax_limb: adjusted_prior_year_tax * 0.20
  - income_limb: defined_prior_quarter_income * 0.02
  - advance_due: min(tax_limb, income_limb)
expected:
  tax_limb: 2000000
  income_limb: 1200000
  advance_due: 1200000
```


## am-corporate-income-tax.md / Armenia conditional interest rate and equity amount limits

### 6. Two interest limits without duplicate add-back

Hypothetical full-year single nonbank borrowing 100 million, interest 20 million, closing positive tax equity 3 million. Assume an **illustrative established year-end CBA settlement rate of 6%**, not a certified December 2026 rate. Rate cap permits 12 million, separate interest/equity limit 6 million: permitted amount 6 million and total disallowance 14 million, not 22 million by adding overlapping restrictions. No capitalisation, onward lending, exception, TP difference or part-year issue. [114][code]

```oa-check
name: Armenia conditional interest rate and equity amount limits
inputs:
  full_year_principal: 100000000
  actual_interest: 20000000
  hypothetical_closing_settlement_rate: 0.06
  closing_tax_equity: 3000000
steps:
  - rate_limit: full_year_principal * hypothetical_closing_settlement_rate * 2
  - equity_interest_limit: closing_tax_equity * 2
  - permitted_interest: min(actual_interest, rate_limit, equity_interest_limit)
  - total_disallowance: actual_interest - permitted_interest
expected:
  rate_limit: 12000000
  equity_interest_limit: 6000000
  permitted_interest: 6000000
  total_disallowance: 14000000
```


## am-corporate-income-tax.md / Armenia general donation gross income cap

### 7. General qualifying donation cap

Annual gross income 200 million, qualifying ordinary Article 123(1)(5) donation 800,000, no special recipient category. Cap 500,000 and disallowed excess 300,000. Retain actual recipient/value evidence; this is not the separate 2.5% special-category deduction. [123(1)(5)–(5.1)][code]

```oa-check
name: Armenia general donation gross income cap
inputs:
  gross_income: 200000000
  established_general_donation: 800000
steps:
  - cap: gross_income * 0.0025
  - deductible_donation: min(established_general_donation, cap)
  - excess: established_general_donation - deductible_donation
expected:
  cap: 500000
  deductible_donation: 500000
  excess: 300000
```


## am-cross-border.md / Armenia conditional consultancy net guarantee

### 2. Offshore consultancy with a net guarantee

October 2026 offshore consultancy for an Armenian resident organisation, nonresident corporate supplier/no attributable PE. Source and 20% other-income category established; no relief. Contract guarantees 4 million net and payer bears the single withholding tax: taxable gross 5 million, tax 1 million. Merely multiplying the net by 20% would understate the assumed gross-base tax. Actual contractual/tax-on-tax classification and payer deductibility need separate review. [107(4), 125(4)(5), 132][code]; [HO-234-N 20][july-amend]

```oa-check
name: Armenia conditional consultancy net guarantee
inputs:
  guaranteed_net: 4000000
  established_rate: 0.20
steps:
  - taxable_gross: guaranteed_net / (1 - established_rate)
  - withholding: taxable_gross * established_rate
  - net_check: taxable_gross - withholding
expected:
  taxable_gross: 5000000
  withholding: 1000000
  net_check: 4000000
```


## am-cross-border.md / Armenia established dividend decision tax event

### 3. Qualifying dividend decision before cash transfer

October 2026 qualifying Article 109(3)(5) decision distributing 2 million gross from reporting-year profits to a nonresident company, no relief. Article 132(2)(7) treats the decision as a payment event: 5% withholding 100,000 and residual entitlement 1.9 million, even if cash is transferred later. This does not apply the future bank-dividend changes or settle interim/nonstandard distributions. [109, 125(4)(3.1), 132][code]; [HO-385-N 14][dividend-amend]

```oa-check
name: Armenia established dividend decision tax event
inputs:
  established_gross_dividend: 2000000
steps:
  - withholding: established_gross_dividend * 0.05
  - residual_entitlement: established_gross_dividend - withholding
expected:
  withholding: 100000
  residual_entitlement: 1900000
```


## am-cross-border.md / Armenia eligible foreign credit annual liability carryforward

### 5. Eligible credit exceeds the annual liability

Assume after all legal base and corresponding-tax tests, Article 20(3) eligible credit is 5.4 million, while the year's established corresponding tax liability is only 4 million because of other results. With no competing credits/prepayments, use 4 million this year, carry 1.4 million under Article 20(4), current residual zero. This is a different limit from example 4; neither example resolves multi-country ordering or the actual future return. [20(3)–(4)][code]

```oa-check
name: Armenia eligible foreign credit annual liability carryforward
inputs:
  established_eligible_credit: 5400000
  established_annual_liability: 4000000
steps:
  - current_use: min(established_eligible_credit, established_annual_liability)
  - eligible_carryforward: max(established_eligible_credit - current_use, 0)
  - current_residual: max(established_annual_liability - current_use, 0)
expected:
  current_use: 4000000
  eligible_carryforward: 1400000
  current_residual: 0
```


## am-cross-border.md / Armenia PE and non attributed income separation

### 6. PE profit and non-attributed service receipt

Ordinary registered corporate PE has 50 million documented attributable revenue and 35 million already-established allowable deductions: profit 15 million, tax 2.7 million. The same nonresident separately receives 5 million Armenian-source service income not attributed to the PE, under an established 20% no-relief category: tax 1 million. Separate computed amounts total 3.7 million before actual credits/prepayments and return reconciliation. Do not deduct PE costs again from the 5-million gross non-attributed receipt. [105, 125(1)/(5), 130, 132–133][code]

```oa-check
name: Armenia PE and non attributed income separation
inputs:
  attributable_revenue: 50000000
  established_allowable_pe_costs: 35000000
  non_attributed_service_gross: 5000000
steps:
  - pe_taxable_profit: max(attributable_revenue - established_allowable_pe_costs, 0)
  - pe_computed_tax: pe_taxable_profit * 0.18
  - non_attributed_computed_tax: non_attributed_service_gross * 0.20
  - combined_computed_tax_before_credits: pe_computed_tax + non_attributed_computed_tax
expected:
  pe_taxable_profit: 15000000
  pe_computed_tax: 2700000
  non_attributed_computed_tax: 1000000
  combined_computed_tax_before_credits: 3700000
```


## am-transfer-pricing.md / Armenia separate TP application and notification populations

### 1. Separate the two aggregation populations

Hypothetical established values, exclusive of the three excluded taxes: ordinary controlled transactions AMD 190 million plus Article 363(4) PE/head-office dealings AMD 20 million. General annual aggregate 210 million exceeds 200 million; notification population 190 million does not. This tests the different populations, not how a real loan/PE entry must be valued. [363(6), 375(1)][code]

```oa-check
name: Armenia separate TP application and notification populations
inputs:
  ordinary_controlled: 190000000
  pe_head_office: 20000000
  threshold: 200000000
steps:
  - regulation_population: ordinary_controlled + pe_head_office
  - notification_population: ordinary_controlled
  - regulation_excess: max(regulation_population - threshold, 0)
  - notification_excess: max(notification_population - threshold, 0)
expected:
  regulation_population: 210000000
  notification_population: 190000000
  regulation_excess: 10000000
  notification_excess: 0
```


## am-transfer-pricing.md / Armenia cost plus remuneration

### 3. Cost markup denominator

Established comparable cost pool 80 million and hypothetical supported gross markup 10%; remuneration 88 million. Charged 84 million implies 5%, giving a 4-million remuneration difference. Do not use 10% of sales instead. Scope/annual gate and tax bridge are separately established. [368][code]; [556-N cost-plus provisions][methods]

```oa-check
name: Armenia cost plus remuneration
inputs:
  cost_pool: 80000000
  benchmark_markup: 0.10
  charged_revenue: 84000000
steps:
  - benchmark_profit: cost_pool * benchmark_markup
  - benchmark_revenue: cost_pool + benchmark_profit
  - actual_markup: (charged_revenue - cost_pool) / cost_pool
  - remuneration_difference: benchmark_revenue - charged_revenue
expected:
  benchmark_revenue: 88000000
  actual_markup: 0.05
  remuneration_difference: 4000000
```


## am-transfer-pricing.md / Armenia resale gross sales margin

### 4. Resale sales margin

Established resale facts: net sales 150 million, controlled purchase 130 million, supported gross sales margin 20%. Implied purchase amount 120 million and purchase difference 10 million. No material added value or inconsistent cost classification; no universal deemed margin. [368][code]; [556-N 26–30][methods]

```oa-check
name: Armenia resale gross sales margin
inputs:
  net_sales: 150000000
  charged_purchase: 130000000
  supported_margin: 0.20
steps:
  - required_gross_profit: net_sales * supported_margin
  - implied_purchase: net_sales - required_gross_profit
  - purchase_difference: max(charged_purchase - implied_purchase, 0)
expected:
  required_gross_profit: 30000000
  implied_purchase: 120000000
  purchase_difference: 10000000
```


## am-transfer-pricing.md / Armenia conditional full year loan interest comparison

### 6. Financing comparison is not a safe harbour

Hypothetical full-year simple loan: 100 million principal, charged interest 10%, supported comparable interest 7%. Interest difference 3 million. Comparability assumes currency, term, credit, security and other conditions established; no claim that 7% is a prescribed Armenian rate or that the loan principal is the notification amount. [365(2)(1)(c), 368][code]

```oa-check
name: Armenia conditional full year loan interest comparison
inputs:
  principal: 100000000
  charged_rate: 0.10
  supported_rate: 0.07
steps:
  - charged_interest: principal * charged_rate
  - supported_interest: principal * supported_rate
  - interest_difference: max(charged_interest - supported_interest, 0)
expected:
  charged_interest: 10000000
  supported_interest: 7000000
  interest_difference: 3000000
```


## am-transfer-pricing.md / Armenia documentation sanction base

### 7. Missing documentation has a transaction-value base

Assume Article 402.2 applies to one documentation-subject transaction valued at 50 million: initial fine 5 million. If the post-fine 30-day condition is met and exactly five days are legally established as overdue, additional charge 100,000. This arithmetic does not decide service, liability, relief or the first overdue date. [402.2][code]

```oa-check
name: Armenia documentation sanction base
inputs:
  established_transaction_value: 50000000
  established_post_grace_overdue_days: 5
steps:
  - initial_fine: established_transaction_value * 0.10
  - further_charge: established_transaction_value * 0.0004 * established_post_grace_overdue_days
expected:
  initial_fine: 5000000
  further_charge: 100000
```


## armenia-income-tax.md / Armenia personal interest category rates

### 2. Bank-deposit versus ordinary private-loan interest

Two separate established taxable receipts of 1 million: bank-deposit interest at 10% gives 100,000; ordinary nonbank loan interest under the general 20% rate gives 200,000. Neither has an Article 149 exemption or delayed-payment issue. Do not classify every interest payment at the bank rate. [149, 150(5)/(5.1)][code]

```oa-check
name: Armenia personal interest category rates
inputs:
  taxable_bank_interest: 1000000
  taxable_private_interest: 1000000
steps:
  - bank_pit: taxable_bank_interest * 0.10
  - private_pit: taxable_private_interest * 0.20
expected:
  bank_pit: 100000
  private_pit: 200000
```


## armenia-income-tax.md / Armenia royalty and dividend categories

### 4. Royalty and ordinary dividend remain separate

Taxable received royalty 2 million at 10% and ordinary taxable received dividend 2 million at 5%: 200,000 plus 100,000 = 300,000. No listing, reinvestment or treaty relief; no corporate declaration-before-cash assumption. [142, 149, 150(6)/(8)][code]

```oa-check
name: Armenia royalty and dividend categories
inputs:
  taxable_royalty: 2000000
  taxable_dividend: 2000000
steps:
  - royalty_pit: taxable_royalty * 0.10
  - dividend_pit: taxable_dividend * 0.05
  - total_pit: royalty_pit + dividend_pit
expected:
  royalty_pit: 200000
  dividend_pit: 100000
  total_pit: 300000
```


## armenia-income-tax.md / Armenia established ordinary taxable property income

### 5. Established ordinary taxable property sale

Assume a documented ordinary personal movable-property sale to a tax agent has established taxable total income 5 million, no land/private-person sale exemption, developer/crypto/security category or missing-document rule. Article 150(9)'s 10% produces 500,000, rather than a guessed net capital-gain base after personal acquisition cost. Actual asset/status exemption tests are prerequisites. [147, 150(9)/(13)][code]

```oa-check
name: Armenia established ordinary taxable property income
inputs:
  established_taxable_total_sale_income: 5000000
steps:
  - pit: established_taxable_total_sale_income * 0.10
expected:
  pit: 500000
```


## armenia-income-tax.md / Armenia foreign personal income tax object cap

### 6. Foreign personal-income credit cap

Resident has established taxable foreign salary 12 million at 20%, no exemption/treaty change. Armenian object tax 2.4 million; corresponding foreign tax collected 3 million. Eligible credit 2.4 million, current residual zero. The 600,000 above the foreign-object cap is not an Article 20(4) carryforward. Other stamp/social liabilities are not decided. [20, 150(1)][code]

```oa-check
name: Armenia foreign personal income tax object cap
inputs:
  established_foreign_taxable_salary: 12000000
  corresponding_foreign_tax_collected: 3000000
steps:
  - armenian_object_tax: established_foreign_taxable_salary * 0.20
  - eligible_credit: min(corresponding_foreign_tax_collected, armenian_object_tax)
  - residual_pit: max(armenian_object_tax - eligible_credit, 0)
  - foreign_tax_above_object_cap: corresponding_foreign_tax_collected - eligible_credit
expected:
  armenian_object_tax: 2400000
  eligible_credit: 2400000
  residual_pit: 0
  foreign_tax_above_object_cap: 600000
```


## armenia-income-tax.md / Armenia eligible PIT credit annual liability carry

### 7. Eligible credit carried because annual liability is lower

Separate hypothetical: after statutory category/object tests, eligible personal credit 400,000 and established corresponding annual liability 300,000, no competing relief/prepayment. Use 300,000; carry eligible 100,000 under Article 20(4). The inputs are already legally established; this does not authorise salary business-expense deductions or cross-category aggregation. [20(3)–(4)][code]

```oa-check
name: Armenia eligible PIT credit annual liability carry
inputs:
  established_eligible_credit: 400000
  established_corresponding_annual_liability: 300000
steps:
  - current_use: min(established_eligible_credit, established_corresponding_annual_liability)
  - eligible_carry: max(established_eligible_credit - current_use, 0)
  - residual: max(established_corresponding_annual_liability - current_use, 0)
expected:
  current_use: 300000
  eligible_carry: 100000
  residual: 0
```


## armenia-payroll.md / Armenia ordinary salary upper pension health limbs

### 2. Upper pension and health limbs

Salary 600,000, established mandatory pre-retirement participant/payer: PIT 120,000, pension 35,000, stamp 1,000, health 10,800; net due 433,200. [Same statutory branches above][pension] [Health][health] [Stamp][stamp] [PIT][code]

```oa-check
name: Armenia ordinary salary upper pension health limbs
inputs:
  gross_salary: 600000
steps:
  - pit: gross_salary * 0.20
  - pension: gross_salary * 0.10 - 25000
  - stamp: 1000
  - health: 10800
  - net_due: gross_salary - pit - pension - stamp - health
expected:
  pit: 120000
  pension: 35000
  net_due: 433200
```


## armenia-payroll.md / Armenia salary cap and high stamp

### 3. Pension cap and high stamp

Salary 1.2 million, no cap waiver/other source: PIT 240,000, pension 87,500, stamp 15,000, health 10,800; net 846,700. [Pension 6][pension] [Stamp 12][stamp] [Health 46][health] [PIT 150][code]

```oa-check
name: Armenia salary cap and high stamp
inputs:
  gross_salary: 1200000
steps:
  - pit: gross_salary * 0.20
  - pension_base: min(gross_salary, 75000 * 15)
  - pension: pension_base * 0.10 - 25000
  - stamp: 15000
  - health: 10800
  - net_due: gross_salary - pit - pension - stamp - health
expected:
  pit: 240000
  pension: 87500
  net_due: 846700
```


## armenia-payroll.md / Armenia established nonparticipant pension branch

### 4. Pre-1974 worker with no pension election

Documented nonparticipant, ordinary health/stamp payer, salary 300,000: pension zero, net 234,200. The no-election fact matters; an elected pre-1974 participant cannot use this control. [Pension 5][pension] [Stamp][stamp] [Health][health] [PIT][code]

```oa-check
name: Armenia established nonparticipant pension branch
inputs:
  gross_salary: 300000
steps:
  - pit: gross_salary * 0.20
  - pension: 0
  - net_due: gross_salary - pit - pension - 1000 - 4800
expected:
  pit: 60000
  net_due: 234200
```


## armenia-payroll.md / Armenia accrued salary and unpaid net reconciliation

### 6. Accrued salary and unpaid bank balance

Ordinary 300,000 salary accrued, no salary cash paid yet, established statutory deductions total 80,800. PIT remains 60,000 and net payable 219,200; zero bank salary payment is not zero accrued base or zero authority obligation. Actual withholding/recovery and health payment follow their own rules. [Tax Code 142/154][code], [Pension][pension], [Stamp][stamp], [Health][health]

```oa-check
name: Armenia accrued salary and unpaid net reconciliation
inputs:
  accrued_salary: 300000
  salary_cash_paid: 0
  established_other_employee_deductions: 20800
steps:
  - accrued_pit: accrued_salary * 0.20
  - net_salary_due: accrued_salary - accrued_pit - established_other_employee_deductions
  - closing_net_payable: net_salary_due - salary_cash_paid
expected:
  accrued_pit: 60000
  closing_net_payable: 219200
```


## armenia-payroll.md / Armenia voluntary pension published form inverse base limit

### 7. Qualifying voluntary-pension deduction, not a gross five-percent shortcut

Published-form included total S = 315,000, actual eligible voluntary contribution 20,000, no other exclusions: cap 15,000, PIT base 300,000, PIT 60,000. This only checks the PIT/base method, not the employee's complete net pay or the voluntary plan's eligibility. [Tax Code 147(1)(3)][code], [Annex 1 instruction 5][form]

```oa-check
name: Armenia voluntary pension published form inverse base limit
inputs:
  included_income_total: 315000
  qualifying_voluntary_contribution: 20000
steps:
  - deduction_limit: included_income_total - included_income_total / 1.05
  - permitted_deduction: min(qualifying_voluntary_contribution, deduction_limit)
  - pit_base: included_income_total - permitted_deduction
  - pit: pit_base * 0.20
expected:
  deduction_limit: 15000
  permitted_deduction: 15000
  pit_base: 300000
  pit: 60000
```


## armenia-social-contributions.md / Armenia ordinary monthly pension cap

### 2. Monthly ordinary cap

Mandatory participant, single source, base 2 million, no waiver: capped base 1,125,000, contribution 87,500. [6(6)–(7)][pension], [1][wage]

```oa-check
name: Armenia ordinary monthly pension cap
inputs:
  eligible_base: 2000000
  statutory_minimum_wage: 75000
steps:
  - capped_base: min(eligible_base, statutory_minimum_wage * 15)
  - contribution: capped_base * 0.10 - 25000
expected:
  capped_base: 1125000
  contribution: 87500
```


## armenia-social-contributions.md / Armenia elected pension participant five percent branch

### 3. Established pre-1974 elected participant

The Article 6(3) branch, effective election and 600,000 salary: 30,000, not zero and not the mandatory young-worker 35,000. [5–6][pension]

```oa-check
name: Armenia elected pension participant five percent branch
inputs:
  eligible_salary: 600000
steps:
  - contribution: eligible_salary * 0.05
expected:
  contribution: 30000
```


## armenia-social-contributions.md / Armenia business pension distinct actual and turnover cases

### 4. Actual-income business versus separate turnover-regime case

Mandatory pre-retirement entrepreneur with established annual Article 2(27) income 10 million, no other source/waiver: 700,000. A **different** eligible turnover-regime case for twelve liable months: 60,000. Do not tax turnover as profit or add both cases to the same facts without lawful mixed-regime reconciliation. [6(2)/(5)][pension]

```oa-check
name: Armenia business pension distinct actual and turnover cases
inputs:
  annual_business_income: 10000000
  separate_turnover_case_months: 12
steps:
  - actual_income_contribution: annual_business_income * 0.10 - 300000
  - separate_turnover_contribution: separate_turnover_case_months * 5000
expected:
  actual_income_contribution: 700000
  separate_turnover_contribution: 60000
```


## armenia-social-contributions.md / Armenia employer funded childcare pension

### 5. Employer-funded childcare obligation

Six established liable months under Article 6(10), no employee withholding: employer funds 18,000. This does not determine health status or every leave benefit. [6(10)][pension]

```oa-check
name: Armenia employer funded childcare pension
inputs:
  established_liable_months: 6
steps:
  - employer_payment: established_liable_months * 3000
  - employee_withholding_for_this_obligation: 0
expected:
  employer_payment: 18000
  employee_withholding_for_this_obligation: 0
```


## armenia-social-contributions.md / Armenia monthly stamp threshold discontinuity

### 6. Stamp discontinuity

Established monthly payer/base, no exemption: 1 million has stamp 1,000; 1,000,001 has 15,000. [12][stamp]

```oa-check
name: Armenia monthly stamp threshold discontinuity
inputs:
  lower_branch_stamp: 1000
  upper_branch_stamp: 15000
steps:
  - increase_at_threshold: upper_branch_stamp - lower_branch_stamp
expected:
  increase_at_threshold: 14000
```


## armenia-social-contributions.md / Armenia social package health funding separate self payment

### 8. Social-package lower-paid health beneficiary

Established 2026 payer and beneficiary, salary through 500,000: 4,800 agent amount plus 6,000 self-payment; no assumed 6,000 state subsidy under paragraph 17. [46(9)/(17)/(18)][health]

```oa-check
name: Armenia social package health funding separate self payment
inputs:
  agent_amount: 4800
  self_payment: 6000
steps:
  - total_funding: agent_amount + self_payment
  - state_subsidy_under_paragraph_17: 0
expected:
  total_funding: 10800
  state_subsidy_under_paragraph_17: 0
```


## armenia-social-contributions.md / Armenia ordinary annual business pension cap

### 9. Annual ordinary pension cap

Mandatory actual-business case with established 20 million annual eligible income, no other source, waiver or special exclusion: capped 13.5 million, contribution 1.05 million. [6(6)–(7)][pension], [1][wage]

```oa-check
name: Armenia ordinary annual business pension cap
inputs:
  annual_eligible_income: 20000000
  january_minimum_wage: 75000
steps:
  - capped_base: min(annual_eligible_income, january_minimum_wage * 180)
  - contribution: capped_base * 0.10 - 300000
expected:
  capped_base: 13500000
  contribution: 1050000
```


## armenia-vat.md / Armenia statutory inclusive receipt calculation

### 2. Statutory cash-receipt-only inclusive branch

Ordinary taxable supply, only a cash-register receipt, VAT-inclusive compensation AMD 120,000: use 16.67%, not an unrounded 20/120. [63(2)(4)][code]

```oa-check
name: Armenia statutory inclusive receipt calculation
inputs:
  inclusive_compensation: 120000
steps:
  - vat: inclusive_compensation * 0.1667
  - amount_excluding_calculated_vat: inclusive_compensation - vat
expected:
  vat: 20004
  amount_excluding_calculated_vat: 99996
```


## armenia-vat.md / Armenia late invoice confirmation separates recovery period

### 3. Domestic invoice confirmed after the deadline

September acquisition, otherwise eligible input AMD 200,000. Confirmation on 21 October is after the September return deadline; recovery is October, not September. The output below is a hypothetical ordinary September amount and ignores unrelated inputs. [71(1)(1)][code]

```oa-check
name: Armenia late invoice confirmation separates recovery period
inputs:
  september_output: 500000
  eligible_invoice_vat: 200000
steps:
  - september_input_from_this_invoice: 0
  - september_payable: september_output - september_input_from_this_invoice
  - october_input_from_this_invoice: eligible_invoice_vat
expected:
  september_input_from_this_invoice: 0
  september_payable: 500000
  october_input_from_this_invoice: 200000
```


## armenia-vat.md / Armenia EAEU filing payment and recovery month

### 5. EAEU border month is not automatically recovery month

Ordinary EAEU-status goods enter in September; import declaration submitted and VAT paid on 15 October. AMD 2 million acquisition base, no excise. AMD 400,000 import VAT; recovery in October if otherwise eligible, despite payment before the following-month deadline. [61(3), 71(1)(3)][code]

```oa-check
name: Armenia EAEU filing payment and recovery month
inputs:
  acquisition_base: 2000000
steps:
  - import_vat: acquisition_base * 0.20
  - september_recovery: 0
  - october_recovery: import_vat
expected:
  import_vat: 400000
  september_recovery: 0
  october_recovery: 400000
```


## armenia-vat.md / Armenia subsequent mixed use reversal

### 6. Previously credited common input later used in mixed transactions

Non-fixed services previously credited AMD 200,000, subsequently used for mixed transactions with no direct attribution possible. Established relevant period's total transaction bases AMD 10 million include AMD 3 million non-taxable: reverse AMD 60,000. No other adjustment or special exclusion. This is the subsequent-use paragraph, not an assumed first-year annual ratio. [73(2)(1)(b)][code]

```oa-check
name: Armenia subsequent mixed use reversal
inputs:
  previously_credited_input: 200000
  relevant_non_taxable_base: 3000000
  relevant_total_base: 10000000
steps:
  - non_taxable_share: relevant_non_taxable_base / relevant_total_base
  - reversal: previously_credited_input * non_taxable_share
  - unreversed_input: previously_credited_input - reversal
expected:
  non_taxable_share: 0.3
  reversal: 60000
  unreversed_input: 140000
```


## armenia-vat.md / Armenia fixed asset subsequent non taxable period

### 7. Fixed asset later used exclusively for non-taxable transactions

Previously credited asset, current period Article 121 tax depreciation established at AMD 100,000, exclusively non-taxable use and no statutory exception: reverse AMD 20,000. Do not reverse the full original input solely because one month's use changed. [73(2)(2)(a)][code]

```oa-check
name: Armenia fixed asset subsequent non taxable period
inputs:
  established_period_tax_depreciation: 100000
steps:
  - period_reversal: established_period_tax_depreciation * 0.20
expected:
  period_reversal: 20000
```


## armenia-vat.md / Armenia foreign service agent output and timing branches

### 8. Recipient-agent output does not prove immediate input

Established Armenian-place ordinary consulting from a no-PE foreign organisation to an Armenian VAT payer, statutory net base AMD 1 million. Output AMD 200,000. Compare a fully eligible, timely recipient-issued tax invoice against one issued only after the return deadline: latter case has no current-period input from this transaction. Contract pricing, PE and liability are assumed resolved; no blanket gross-up is implied. [39(1)(4), 70(2), 71(1)(4)][code]

```oa-check
name: Armenia foreign service agent output and timing branches
inputs:
  established_service_base: 1000000
steps:
  - agent_output: established_service_base * 0.20
  - eligible_timely_input: agent_output
  - timely_branch_net: agent_output - eligible_timely_input
  - late_invoice_current_input: 0
  - late_branch_current_net: agent_output - late_invoice_current_input
expected:
  agent_output: 200000
  eligible_timely_input: 200000
  timely_branch_net: 0
  late_invoice_current_input: 0
  late_branch_current_net: 200000
```


## Added current TP calculation controls, 25 October 2026

These ordinary-company controls assume established 18% status, filed before-values, supported upward adjustments and no other relief or deduction changes. They exercise Code105/125/364 and current1032-N fields5–17. They do not prove taxpayer eligibility or authorise ordinary historic CIT/advance amendments.

### Income addition and deduction reduction

```oa-check
name: Armenia separate TP form income and deduction bridge
inputs:
  filed_income: 100000000
  filed_deductions: 80000000
  income_addition: 4000000
  deduction_reduction: 2000000
  original_tax: 3600000
steps:
  - adjusted_income: filed_income + income_addition
  - adjusted_deductions: filed_deductions - deduction_reduction
  - base_adjustment: income_addition + deduction_reduction
  - adjusted_profit: max(0, adjusted_income - adjusted_deductions)
  - adjusted_tax: adjusted_profit * 0.18
  - additional_tax: adjusted_tax - original_tax
expected:
  adjusted_income: 104000000
  adjusted_deductions: 78000000
  base_adjustment: 6000000
  adjusted_profit: 26000000
  adjusted_tax: 4680000
  additional_tax: 1080000
```

### Upward adjustment reduces a loss without cash tax

```oa-check
name: Armenia TP adjustment within a tax loss
inputs:
  filed_income: 100000000
  filed_deductions: 120000000
  income_addition: 15000000
steps:
  - adjusted_balance: filed_income + income_addition - filed_deductions
  - remaining_loss: max(0, -adjusted_balance)
  - taxable_profit: max(0, adjusted_balance)
  - tax: taxable_profit * 0.18
expected:
  adjusted_balance: -5000000
  remaining_loss: 5000000
  taxable_profit: 0
  tax: 0
```

### Only the positive remainder is taxable

```oa-check
name: Armenia TP adjustment crosses from loss to positive profit
inputs:
  filed_income: 100000000
  filed_deductions: 120000000
  income_addition: 25000000
steps:
  - adjusted_balance: filed_income + income_addition - filed_deductions
  - taxable_profit: max(0, adjusted_balance)
  - tax: taxable_profit * 0.18
expected:
  adjusted_balance: 5000000
  taxable_profit: 5000000
  tax: 900000
```


## Entrepreneur and declaration reporting controls, 25 October

Primary scope and assumptions: see entrepreneur-reporting-research.md. Each business deduction, activity, monthly liability and advance exemption is assumed independently established. Threshold cases concern otherwise non-taxable Annex2 receipts from non-family natural persons, not taxable salary or a general annual allowance.

```oa-check
name: Armenia registered entrepreneur ordinary business profit
inputs:
  business_gross_income: 20000000
  permitted_deductions: 12000000
steps:
  - taxable_profit: max(business_gross_income - permitted_deductions, 0)
  - profit_tax: taxable_profit * 0.23
expected:
  taxable_profit: 8000000
  profit_tax: 1840000
```

```oa-check
name: Armenia registered entrepreneur business loss has no negative current tax
inputs:
  business_gross_income: 20000000
  permitted_deductions: 24000000
steps:
  - business_result: business_gross_income - permitted_deductions
  - taxable_profit: max(business_result, 0)
  - current_tax: taxable_profit * 0.23
expected:
  business_result: -4000000
  taxable_profit: 0
  current_tax: 0
```

```oa-check
name: Armenia turnover entrepreneur fixed profit tax excludes only established full suspension months
inputs:
  year_months: 12
  qualifying_full_suspension_months: 3
steps:
  - liable_months: year_months - qualifying_full_suspension_months
  - fixed_profit_tax: liable_months * 5000
expected:
  liable_months: 9
  fixed_profit_tax: 45000
```

```oa-check
name: Armenia registered entrepreneur ordinary lower of quarterly advance
inputs:
  adjusted_prior_year_tax: 3750000
  defined_prior_quarter_income: 20000000
steps:
  - prior_tax_limb: adjusted_prior_year_tax * 0.20
  - prior_income_limb: defined_prior_quarter_income * 0.02
  - advance: min(prior_tax_limb, prior_income_limb)
expected:
  prior_tax_limb: 750000
  prior_income_limb: 400000
  advance: 400000
```

```oa-check
name: Armenia nonfamily nontaxable gift at inclusive omission threshold
inputs:
  one_off_receipt: 1000000
  omission_threshold: 1000000
steps:
  - over_threshold: min(ceil(max(one_off_receipt - omission_threshold, 0)), 1)
  - mandatory_reportable_receipt: one_off_receipt * over_threshold
expected:
  over_threshold: 0
  mandatory_reportable_receipt: 0
```

```oa-check
name: Armenia nonfamily nontaxable gift above threshold reports whole receipt
inputs:
  one_off_receipt: 1200000
  omission_threshold: 1000000
steps:
  - over_threshold: min(ceil(max(one_off_receipt - omission_threshold, 0)), 1)
  - mandatory_reportable_receipt: one_off_receipt * over_threshold
expected:
  over_threshold: 1
  mandatory_reportable_receipt: 1200000
```

## Ordinary corporate deduction controls, 25 October

These assume the actual category, source documents, date gates and any other restrictions have already been established. Travel expenses are assumed to satisfy the separately applicable daily limits. They do not supply an unknown destination rate, legacy-debt legal event or an accepted refund.

```oa-check
name: Armenia ordinary foreign business trip percentage limit
inputs:
  gross_income: 40000000
  eligible_trip_cost: 3000000
steps:
  - ceiling: gross_income * 0.05
  - allowed: min(eligible_trip_cost, ceiling)
  - disallowed: eligible_trip_cost - allowed
expected:
  ceiling: 2000000
  allowed: 2000000
  disallowed: 1000000
```

```oa-check
name: Armenia documented overseas work separate turnover branch
inputs:
  separately_identified_overseas_turnover: 10000000
  eligible_trip_cost: 9000000
steps:
  - ceiling: separately_identified_overseas_turnover * 0.80
  - allowed: min(eligible_trip_cost, ceiling)
  - disallowed: eligible_trip_cost - allowed
expected:
  ceiling: 8000000
  allowed: 8000000
  disallowed: 1000000
```

```oa-check
name: Armenia employer voluntary pension deduction cap
inputs:
  employee_salary_and_equivalents: 12000000
  qualifying_voluntary_pension: 1000000
steps:
  - ceiling: employee_salary_and_equivalents * 0.075
  - allowed: min(qualifying_voluntary_pension, ceiling)
  - disallowed: qualifying_voluntary_pension - allowed
expected:
  ceiling: 900000
  allowed: 900000
  disallowed: 100000
```

```oa-check
name: Armenia staff social cost ordinary and zero gross income branches
inputs:
  ordinary_gross_income: 100000000
  qualifying_social_cost: 400000
  zero_income_case_salary: 20000000
steps:
  - ordinary_ceiling: ordinary_gross_income * 0.0025
  - ordinary_allowed: min(qualifying_social_cost, ordinary_ceiling)
  - zero_income_ceiling: zero_income_case_salary * 0.01
  - zero_income_allowed: min(qualifying_social_cost, zero_income_ceiling)
expected:
  ordinary_ceiling: 250000
  ordinary_allowed: 250000
  zero_income_ceiling: 200000
  zero_income_allowed: 200000
```

```oa-check
name: Armenia single improvement over five percent capitalises the whole item
inputs:
  original_cost: 10000000
  single_improvement: 600000
steps:
  - five_percent: original_cost * 0.05
  - amount_over_test: single_improvement - five_percent
  - whole_capital_item: single_improvement
expected:
  five_percent: 500000
  amount_over_test: 100000
  whole_capital_item: 600000
```

```oa-check
name: Armenia small improvement pool capitalises only excess over fifteen percent
inputs:
  original_cost: 10000000
  qualifying_small_expense: 400000
  number_of_separate_expenses: 4
steps:
  - small_expense_pool: qualifying_small_expense * number_of_separate_expenses
  - cumulative_current_limit: original_cost * 0.15
  - capital_excess: max(small_expense_pool - cumulative_current_limit, 0)
  - current_cost: small_expense_pool - capital_excess
expected:
  small_expense_pool: 1600000
  cumulative_current_limit: 1500000
  capital_excess: 100000
  current_cost: 1500000
```

```oa-check
name: Armenia capital spending over opening carrying amount extends shorter remaining term
inputs:
  january_opening_carrying_amount: 300000
  january_qualifying_capital_spending: 600000
  remaining_years: 2
  asset_minimum_years_under_eight: 5
steps:
  - revised_carrying_amount: january_opening_carrying_amount + january_qualifying_capital_spending
  - revised_years: max(remaining_years, asset_minimum_years_under_eight)
  - annual_depreciation: revised_carrying_amount / revised_years
expected:
  revised_carrying_amount: 900000
  revised_years: 5
  annual_depreciation: 180000
```

```oa-check
name: Armenia eligible sales receivable reserve annual increase
inputs:
  eligible_unpaid_receivable_days_181_to_270: 800000
  opening_tax_reserve: 100000
steps:
  - closing_reserve: eligible_unpaid_receivable_days_181_to_270 * 0.50
  - current_other_deduction: max(closing_reserve - opening_tax_reserve, 0)
expected:
  closing_reserve: 400000
  current_other_deduction: 300000
```

```oa-check
name: Armenia day366 debt not hopeless reverses earlier reserve without a new writeoff
inputs:
  earlier_eligible_receivable: 800000
  earlier_reserve_rate: 0.75
  allowable_closing_reserve_after_day366: 0
steps:
  - opening_reserve: earlier_eligible_receivable * earlier_reserve_rate
  - gross_income_restoration: opening_reserve - allowable_closing_reserve_after_day366
expected:
  opening_reserve: 600000
  gross_income_restoration: 600000
```

```oa-check
name: Armenia ordinary corporate signed excess advances separate from refund approval
inputs:
  annual_tax: 4410000
  calculated_advances_as_positive_workpaper: 5000000
steps:
  - signed_advances_field101: -calculated_advances_as_positive_workpaper
  - signed_balance: annual_tax + signed_advances_field101
  - positive_payment: max(signed_balance, 0)
  - signed_reimbursable_field106: min(signed_balance, 0)
  - positive_workpaper_excess: -signed_reimbursable_field106
expected:
  signed_advances_field101: -5000000
  signed_balance: -590000
  positive_payment: 0
  signed_reimbursable_field106: -590000
  positive_workpaper_excess: 590000
```

## VAT transition controls, 25 October

Assume the statutory stock/asset values, prior input treatment, use, period and documentary entitlement are established. These controls do not establish regime eligibility or a filing acknowledgement.

```oa-check
name: Armenia VAT exit to special system reverses eligible retained stock and assets
inputs:
  retained_qualifying_stock_value: 3000000
  qualifying_asset_carrying_value: 5000000
steps:
  - stock_reversal: retained_qualifying_stock_value * 0.20
  - asset_reversal: qualifying_asset_carrying_value * 0.20
  - total_reduction_of_input: stock_reversal + asset_reversal
expected:
  stock_reversal: 600000
  asset_reversal: 1000000
  total_reduction_of_input: 1600000
```

```oa-check
name: Armenia restored unallocable input uses native taxable share
inputs:
  qualifying_previously_unoffset_vat: 300000
  taxable_transaction_base: 6000000
  all_transaction_base: 10000000
steps:
  - taxable_share: taxable_transaction_base / all_transaction_base
  - restored_input: qualifying_previously_unoffset_vat * taxable_share
expected:
  taxable_share: 0.6
  restored_input: 180000
```

```oa-check
name: Armenia blocked fixed asset mixed taxable use statutory restoration
inputs:
  statutory_period_depreciation: 120000
  taxable_transaction_base: 6000000
  all_transaction_base: 10000000
steps:
  - statutory_restoration_before_share: statutory_period_depreciation * 0.1667
  - taxable_share: taxable_transaction_base / all_transaction_base
  - restored_input: statutory_restoration_before_share * taxable_share
expected:
  statutory_restoration_before_share: 20004
  taxable_share: 0.6
  restored_input: 12002.4
```

## Multiple-source pension: monthly refund and annual non-duplication

Assume an ordinary mandatory participant, two fully paid employer contributions each month, no cap waiver, no business or voluntary self-employed amounts, no status change and all twelve monthly refunds already recorded before the annual reconciliation. The example is not an employer election to under-withhold.

```oa-check
name: Armenia multiple employer pension refund is not repeated annually
inputs:
  salary_per_employer: 1000000
  employers: 2
  minimum_wage: 75000
  year_months: 12
steps:
  - contribution_per_employer: salary_per_employer * 0.10 - 25000
  - total_monthly_paid: contribution_per_employer * employers
  - capped_aggregate_monthly_base: min(salary_per_employer * employers, minimum_wage * 15)
  - monthly_maximum: capped_aggregate_monthly_base * 0.10 - 25000
  - monthly_refund: max(total_monthly_paid - monthly_maximum, 0)
  - original_annual_paid: total_monthly_paid * year_months
  - already_refunded: monthly_refund * year_months
  - recorded_annual_paid_after_refunds: original_annual_paid - already_refunded
  - annual_maximum: minimum_wage * 180 * 0.10 - 300000
  - additional_annual_refund: max(recorded_annual_paid_after_refunds - annual_maximum, 0)
expected:
  contribution_per_employer: 75000
  total_monthly_paid: 150000
  monthly_maximum: 87500
  monthly_refund: 62500
  original_annual_paid: 1800000
  already_refunded: 750000
  recorded_annual_paid_after_refunds: 1050000
  annual_maximum: 1050000
  additional_annual_refund: 0
```


## Ordinary benefit classification and health participant excess

Read26October2026. Hypothetical AMD amounts; legal classification, participant status, settlement and register entry are assumed established. These do not compute benefit entitlement or promise a refund.

Salary300,000 accrued and statutory incapacity benefit50,000 paid in the period: ordinary PIT base350,000 gives70,000. Under the actual pension salary list, the specified statutory benefit is excluded, so the ordinary mandatory pension remains15,000 on300,000, not17,500. No stamp/health/net-pay result is implied. [Tax Code142/147/150](https://www.arlis.am/hy/acts/215611/latest), [joint salary list1(1)(e)](https://www.arlis.am/hy/acts/126230/latest).

```oa-check
name: Armenia salary and statutory benefit separate PIT pension bases
inputs:
  accrued_salary: 300000
  paid_statutory_incapacity_benefit: 50000
steps:
  - pit_base: accrued_salary + paid_statutory_incapacity_benefit
  - ordinary_pit: pit_base * 0.20
  - pension: accrued_salary * 0.05
expected:
  pit_base: 350000
  ordinary_pit: 70000
  pension: 15000
```

Two employers each validly settle the full10,800health premium for the same person/month, each under an established above500,000salary branch. Total21,600less the10,800statutory monthly rate leaves10,800participant excess. The one-time application, full-settlement/register conditions and relevant clocks still govern; neither employer reduces the next payment in anticipation. [Health14(7)–(8)/46(9)](https://www.arlis.am/hy/acts/230432/latest) and actual boardAnnex6recorded in payroll-health-research.md.

```oa-check
name: Armenia two full health premiums participant excess
inputs:
  employer_one_paid: 10800
  employer_two_paid: 10800
  statutory_monthly_rate: 10800
steps:
  - settled_total: employer_one_paid + employer_two_paid
  - participant_excess: settled_total - statutory_monthly_rate
expected:
  settled_total: 21600
  participant_excess: 10800
```


## Resident foreign-credit use and signed return defect

Read26October2026. Ordinary resident company, no competing relief/credits; current foreign amounts below have already passed Code20(3)'s object cap. Article20(4) permits only annual-liability use with the eligible excess carried. The printed749-Nfield95signed comparison is not substituted for the statute. No electronic field behaviour is asserted.

Eligible opening carry4million plus current eligible credit8million, annual liability5million: use5million, carry7million, remaining current taxzero. With signed93=-4million/94=-8million, blind printed95would select-12million because-12million<positive5million. That would consume the carry wrongly. The legal workpaper maps95to-5million,96to-7million and98tozero. [Code20/130](https://www.arlis.am/hy/acts/215611/latest), [actual749-Nfields92–98](https://www.arlis.am/hy/acts/226558/latest).

```oa-check
name: Armenia foreign credit statutory cap preserves carry despite printed sign formula
inputs:
  eligible_opening: 4000000
  eligible_current: 8000000
  annual_liability: 5000000
steps:
  - available: eligible_opening + eligible_current
  - used: min(available, annual_liability)
  - unused_carry: available - used
  - remaining_tax: annual_liability - used
  - signed_field_95: 0 - used
  - signed_field_96: 0 - unused_carry
expected:
  available: 12000000
  used: 5000000
  unused_carry: 7000000
  remaining_tax: 0
  signed_field_95: -5000000
  signed_field_96: -7000000
```


## Loss classification, annual quality cap and natural quantity norm

Read26October2026. Hypothetical AMD, actual loss/quantity/ordinary taxpayer status and all required1261-Ndocumentation assumed established. No dairy special branch or supplier compensation. These do not prove a taxpayer's stock write-off or recoverable input.

Ordinary documented quality loss300,000 and annual gross income20million:1%cap200,000, deductible loss200,000, nondeductible100,000. With60,000related20%input VAT and all other entitlement established,40,000corresponds to deductible loss and20,000is blocked. Reconcile that annual result with credits actually taken earlier; the annual difference belongs to the year's last VATperiod under73(6). [Code122(3)/73(6)](https://www.arlis.am/hy/acts/215611/latest), [1261-N](https://www.arlis.am/hy/acts/171651/latest).

```oa-check
name: Armenia ordinary quality loss annual cap and related VAT
inputs:
  annual_gross_income: 20000000
  documented_quality_loss: 300000
  related_input_vat: 60000
steps:
  - annual_cap: annual_gross_income * 0.01
  - deductible_loss: min(documented_quality_loss, annual_cap)
  - nondeductible_loss: documented_quality_loss - deductible_loss
  - eligible_related_input: related_input_vat * deductible_loss / documented_quality_loss
  - blocked_related_input: related_input_vat - eligible_related_input
expected:
  annual_cap: 200000
  deductible_loss: 200000
  nondeductible_loss: 100000
  eligible_related_input: 40000
  blocked_related_input: 20000
```

Actual recorded cement-storage quantity1,000tonnes, actual shortage3tonnes: current1467-NAnnex2row1storage norm0.2%gives2tonnes, not an automatic allowance above actual loss. With an already established eligible unit tax-cost100,000, allowed natural loss value200,000; excess1tonne/100,000is not deductible under this natural-loss limb. Transport/storage conditions and custody must be correct. [1467-NAnnex2,1–4/row1](https://www.arlis.am/hy/acts/127175/latest), [Code122(2)](https://www.arlis.am/hy/acts/215611/latest).

```oa-check
name: Armenia cement natural storage quantity norm bounded by actual shortage
inputs:
  recorded_tonnes: 1000
  actual_shortage_tonnes: 3
  storage_norm_percent: 0.2
  established_unit_tax_cost: 100000
steps:
  - norm_tonnes: recorded_tonnes * storage_norm_percent / 100
  - allowed_tonnes: min(actual_shortage_tonnes, norm_tonnes)
  - excess_tonnes: actual_shortage_tonnes - allowed_tonnes
  - deductible_natural_loss: allowed_tonnes * established_unit_tax_cost
  - excess_loss_value: excess_tonnes * established_unit_tax_cost
expected:
  norm_tonnes: 2
  allowed_tonnes: 2
  excess_tonnes: 1
  deductible_natural_loss: 200000
  excess_loss_value: 100000
```


## Fresh whole-pack review regression controls, 26 October 2026

The loan date chooses the legal route before the arithmetic. Hypothetical qualifying employee loans with eligible interest 1.8 million and settled wage PIT 2 million: the continuing 2016 loan uses old 8.2 with no modern quarterly cap; the established eligible 2020 loan uses the 1.5 million combined ceiling, assuming no other co-borrower/request has consumed it. This is not a test of actual loan qualification. [Code 160/445(1)(5)](https://www.arlis.am/hy/acts/215611/latest), [continuing old 8.2](https://www.arlis.am/hy/acts/158682/latest), [205-N](https://www.arlis.am/hy/acts/96164/latest).

```oa-check
name: Armenia continuing mortgage cohort differs from modern quarterly cap
inputs:
  paid_eligible_quarter_interest: 1800000
  settled_qualifying_wage_pit: 2000000
  modern_combined_ceiling_available: 1500000
steps:
  - qualifying_2016_loan_refund: min(paid_eligible_quarter_interest, settled_qualifying_wage_pit)
  - qualifying_2020_loan_refund: min(paid_eligible_quarter_interest, settled_qualifying_wage_pit, modern_combined_ceiling_available)
  - difference: qualifying_2016_loan_refund - qualifying_2020_loan_refund
expected:
  qualifying_2016_loan_refund: 1800000
  qualifying_2020_loan_refund: 1500000
  difference: 300000
```

Benefits Law22(1)'s tax-inclusive minimum is derived with Minimum Wage Law1/4's tax-exclusive75,000 and ordinary PIT150(1)'s20%: M−20%M=75,000. The control reconciles the result back to75,000, then checks the employee average-floor branch and ordinary maternity minimum before statutory payment rounding/PIT. A=40,000 is below0.5M; A=50,000 is above it and its80%base is40,000. Independent review of this explicit statutory derivation is required before treating it as cleared. [Benefits Law22](https://www.arlis.am/hy/acts/205733/latest), [Minimum Wage Law1/4](https://www.arlis.am/hy/acts/172160/latest), [PIT150](https://www.arlis.am/hy/acts/215611/latest), [1024-N Annex5(20)](https://www.arlis.am/hy/acts/196905/latest).

```oa-check
name: Armenia tax inclusive benefit minimum and average floor ordering
inputs:
  tax_exclusive_minimum: 75000
  ordinary_pit_rate: 0.20
  above_floor_average: 50000
  below_floor_average: 40000
steps:
  - benefit_minimum_M: tax_exclusive_minimum / (1 - ordinary_pit_rate)
  - included_income_tax: benefit_minimum_M * ordinary_pit_rate
  - reconciled_exclusive_minimum: benefit_minimum_M - included_income_tax
  - average_floor_threshold: benefit_minimum_M * 0.50
  - below_floor_monthly_base: average_floor_threshold
  - above_floor_sickness_base: min(above_floor_average * 0.80, benefit_minimum_M * 10)
  - ordinary_maternity_minimum_before_rounding: average_floor_threshold / 30.4 * 140
expected:
  benefit_minimum_M: 93750
  included_income_tax: 18750
  reconciled_exclusive_minimum: 75000
  average_floor_threshold: 46875
  below_floor_monthly_base: 46875
  above_floor_sickness_base: 40000
  ordinary_maternity_minimum_before_rounding: 215871.7105263158
```
