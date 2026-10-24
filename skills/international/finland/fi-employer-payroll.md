---
name: fi-employer-payroll
description: >
  Prepare Finnish employer payroll reporting for 2026: distinguish earnings
  payment reports, the employer's separate report and tax payment; calculate
  the employer health-insurance contribution for eligible wages. Pension,
  unemployment, accident coverage and full withholding review remain open.
jurisdiction: FI
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.7
---

# Finland employer payroll reporting v0.7

## Who this applies to

This draft addresses the ordinary business-employer electronic reporting cycle. Household, paper-filing, non-cash-only, international and other exceptional cases require separate rules. It does not replace the worker-status, tax-card, wage-base or insurance assessment before payroll.

Reporting deadlines are linked to when the worker can use the payment, rather than when the work was performed. A different employer tax period does not extend the earnings-report deadline. [Incomes Register deadlines][deadlines]

## Rates, bands and thresholds

Vero publishes a **1.91% employer health-insurance contribution for 2026**, compared with 1.87% for 2025. Its guidance covers employees aged 16–67 who are insured in Finland under the relevant health-insurance rules. Determine the applicable wage base and coverage before multiplying. [Social insurance contributions][insurance]

The employer contribution can apply even when withholding is zero or remuneration consists of benefits. The employee's insured-person health contribution is included in the withholding rate; do not deduct it again as a separate item. Vero distinguishes trade income from wages for this contribution. [Social insurance contributions][insurance]

The same official page lists pension, unemployment, occupational accident/disease and group life contributions separately. Their inclusion depends on the applicable coverage and other conditions. This Guide supplies no universal all-in employer percentage. [Social insurance contributions][insurance]

## Employee pension insurance: TyEL eligibility and shares

Ilmarinen's Finnish eligibility page specifies employment, monthly wages of at least **EUR 71.72 in 2026**, and the age conditions. Insurance begins from the month after turning 17 and ends at the end of the month of reaching the upper age: 68 for birth years through 1957, 69 for 1958–1961, and 70 for 1962 onwards. Its English eligibility page contains an inconsistent final birth-year phrase; the Finnish text and contribution page agree on 1962 onwards. [Finnish TyEL eligibility][tyel-eligibility]; [Contribution page][tyel-contributions]

Confirm the actual scheme, employment, insured earnings, birthday month, international coverage and any owner/entrepreneur classification. The existence of a YEL Guide does not settle employee TyEL status.

For covered employees in 2026, the published employee share is **7.30%**. Deduct that share from pay and remit the full insurer contribution as employer. The published average total of 24.40% and average employer share of 17.10% are not every employer's invoice rate: administration, employer characteristics and bonuses can affect the actual charge. Obtain the current insurer-specific rate and reconcile it separately. [Ilmarinen contribution calculation][tyel-calculation]

## Unemployment insurance: classify before calculating

The Employment Fund's liability guidance identifies employees aged 18 to under 65 and employer annual wages exceeding EUR 1,500, subject to exclusions. It excludes the specified self-employed/agricultural categories and flags ownership, entity type and international circumstances for assessment. The EUR 1,500 threshold concerns payment to the Fund, not whether to deduct a liable employee's contribution. Deduct the employee share even if annual payroll does not exceed EUR 1,500; in that case the employer keeps the deducted amount. Report the wages and deduction to the Incomes Register. [Employment Fund payment guidance][unemployment-payment] Birthday-month transitions and international coverage still need detailed checks. [Employment Fund liability][unemployment-liability]

Its 2026 payment guidance states:

| Contribution | 2026 rate |
|---|---|
| Ordinary employer: eligible annual payroll up to EUR 2,509,500 | 0.31% |
| Ordinary employer: excess over that band | 1.23% |
| Ordinary employee | 0.89% |
| Part-owner employee | 0.39% |
| Employer on part-owner wages | 0.31% |

Part-owner wages are excluded from the ordinary employer band calculation. The employee share is deducted from pay; the employer remits both shares on the Fund's invoices. Universities and state enterprises have separate upper rates. [Employment Fund payment guidance][unemployment-payment]

Reconcile eligible wages and ownership status before calculating. This draft does not determine whether a shareholder meets the statutory part-owner definition. Keep the insurer/Fund decisions and payroll reports consistent; tax withholding and the employer health contribution are separate amounts.

## Withholding instructions and income ceilings

For ordinary wage withholding, obtain the current tax-card data electronically or from the employee. The card gives a basic rate, additional rate and income ceiling. Apply the additional rate to the part exceeding the applicable ceiling unless a valid revised card changes the instruction. Vero's wage-card guidance states **60% withholding when no wage tax card is available**; distinguish missing paper from valid data already received electronically. [Wage tax-card guidance][card]

Each employer monitors the wages it has paid against the annual ceiling; employees with multiple employers must monitor their overall position and obtain revised cards where needed. Asking for a higher withholding rate does not increase the ceiling. A lower rate requires a revised card based on updated income/deduction information. [Rate and ceiling guidance][ceiling]

Retain the card's effective dates, source, rates, ceiling and the employer's cumulative payroll values. Confirm how a revised card applies to its validity period before changing the payroll calculation. These records are a preparation control; this draft does not prescribe every revised-card or cumulative-withholding algorithm. Cross-border tax-at-source cards and special remuneration require separate classification.

## Statutory wage classification and cash limit

Prepayment Act section 13 includes employment remuneration, fringe benefits and specified personal fees in wages. Section 9 sets the payer's withholding obligation subject to exceptions; section 11 ties withholding to payment/crediting and limits it to the amount paid in cash. Benefits therefore affect the established base without automatically providing cash from which to withhold. Benefit-only withholding has separate decree rules. Resolve classification and available cash before completing the payslip; do not infer that missing cash removes reporting or employer-health obligations. [Prepayment Act, sections 9, 11 and 13][prepayment-law]

## Reports and deadlines

| Obligation | Ordinary electronic-reporting rule |
|---|---|
| Earnings payment report | Within five calendar days following payment availability |
| Employer's separate report | By the fifth of the following calendar month |
| Registered regular employer with no wages | Monthly separate report with the appropriate no-wages information |
| Casual business employer | Separate report for the relevant wage-payment months |

[Incomes Register deadlines][deadlines]. Weekends and holidays count within the five-day period; when the final reporting day falls on a weekend or holiday, the guidance permits the following business day. Verify the particular calendar and exception before fixing the due date.

The separate report carries the employer health contribution and relevant adjustments; it does not replace each worker's earnings details. Preserve both submission confirmations and reconcile their periods to payroll. [Employer reporting guidance][reporting]

## Payment is a separate step

For an ordinary monthly tax period, Vero's instructions direct payment of withholding and employer health contributions to the Tax Administration by the twelfth of the following month. Longer authorised tax periods affect payment timing; determine the employer's actual period rather than assuming one. Filing the earnings report is not itself evidence of payment. [Reporting/payment guidance][reporting]

Confirm the applicable business-day treatment, tax references and MyTax balance before delivery. Other insurers' contribution invoices have separate payment routes. This draft has not tested a live payroll submission, account or bank payment.

## Preparation workpaper

Use this practical checklist alongside the verified payroll rules for the actual employee:

1. Establish worker classification, residence, insurance status and payment date.
2. Reconcile cash wages, benefits, expenses and the bases used for each deduction/contribution.
3. Apply the valid withholding instruction and separately supported employee deductions.
4. Prepare each worker's earnings report and the employer's monthly separate report.
5. Reconcile submissions, payslips, net cash, tax liabilities and insurer invoices.
6. Retain acceptance confirmations, payment evidence and correction records.

This checklist is preparation practice, not a complete statutory payroll specification. Wage and benefit valuation, tax cards, pensions, unemployment coverage, collective agreements and termination payments still need substantive checks.

## Worked example

Assume EUR 20,000 is the correctly established eligible employer-health contribution base for 2026, with no adjustments. At 1.91%, the contribution is EUR 382. The example excludes other employer costs and does not determine whether a worker is insured.

```oa-check
name: Finland 2026 employer health contribution
inputs:
  eligible_contribution_base: 20000
  employer_health_rate: 0.0191
steps:
  employer_health_contribution: eligible_contribution_base * employer_health_rate
expected:
  employer_health_contribution: 382
```

### 2. A payment crosses the applicable ceiling

Assume ordinary wage withholding, a valid card with a EUR 30,000 ceiling, EUR 28,000 previously paid by this employer within the relevant card calculation, a EUR 4,000 current payment, and card rates of 20% basic and 40% additional. EUR 2,000 remains at the basic rate and EUR 2,000 falls above the ceiling: withholding totals EUR 1,200. Rates are invented card assumptions. Employee insurance deductions and the final cash payment require separate calculations.

```oa-check
name: Finland assumed tax card ceiling crossing
inputs:
  card_ceiling: 30000
  previous_employer_payments: 28000
  current_wages: 4000
  assumed_basic_rate: 0.20
  assumed_additional_rate: 0.40
steps:
  remaining_ceiling: card_ceiling - previous_employer_payments
  basic_rate_wages: min(current_wages, max(0, remaining_ceiling))
  additional_rate_wages: current_wages - basic_rate_wages
  withheld_tax: basic_rate_wages * assumed_basic_rate + additional_rate_wages * assumed_additional_rate
expected:
  remaining_ceiling: 2000
  basic_rate_wages: 2000
  additional_rate_wages: 2000
  withheld_tax: 1200
```

### 3. No available wage-card instruction

Assume an ordinary EUR 2,000 wage payment to which Vero's missing-card rule applies and no valid electronic withholding data. Withholding at 60% is EUR 1,200. The EUR 800 remainder is before separate employee insurance and other valid deductions, not a final payslip net amount.

```oa-check
name: Finland assumed missing wage card withholding
inputs:
  ordinary_wages: 2000
  missing_card_rate: 0.60
steps:
  withheld_tax: ordinary_wages * missing_card_rate
  remainder_before_other_deductions: ordinary_wages - withheld_tax
expected:
  withheld_tax: 1200
  remainder_before_other_deductions: 800
```

### 4. Ordinary employer unemployment bands

Assume EUR 3,000,000 of fully eligible ordinary annual payroll, excluding part-owner wages and special employer categories. Applying the published bands gives EUR 7,779.45 plus EUR 6,033.15, totalling EUR 13,812.60. This estimates the employer share only; reconcile actual invoicing and rounding separately.

```oa-check
name: Finland 2026 ordinary employer unemployment bands
inputs:
  eligible_ordinary_payroll: 3000000
  lower_band_limit: 2509500
  lower_rate: 0.0031
  upper_rate: 0.0123
steps:
  lower_band_wages: min(eligible_ordinary_payroll, lower_band_limit)
  upper_band_wages: max(0, eligible_ordinary_payroll - lower_band_limit)
  lower_contribution: round(lower_band_wages * lower_rate, 2)
  upper_contribution: round(upper_band_wages * upper_rate, 2)
  employer_total: lower_contribution + upper_contribution
expected:
  lower_band_wages: 2509500
  upper_band_wages: 490500
  lower_contribution: 7779.45
  upper_contribution: 6033.15
  employer_total: 13812.60
```

### 5. Employee deductions versus employer contribution

Assume ordinary cash wages of EUR 3,000, valid assumed tax-card withholding of 20%, full TyEL eligibility at 7.30%, ordinary employee unemployment eligibility at 0.89%, and no other deductions. Cash pay is EUR 2,154.30 after EUR 600 tax, EUR 219 pension and EUR 26.70 unemployment. If the same EUR 3,000 is the employer-health base, its EUR 57.30 contribution is an additional employer liability, not another employee deduction. The example does not establish eligibility or total employer cost.

```oa-check
name: Finland assumed employee payroll deduction reconciliation
inputs:
  cash_wages: 3000
  assumed_card_rate: 0.20
  employee_pension_rate: 0.073
  employee_unemployment_rate: 0.0089
  employer_health_rate: 0.0191
steps:
  tax_withheld: cash_wages * assumed_card_rate
  employee_pension: cash_wages * employee_pension_rate
  employee_unemployment: cash_wages * employee_unemployment_rate
  employee_cash: cash_wages - tax_withheld - employee_pension - employee_unemployment
  employer_health_separately: cash_wages * employer_health_rate
expected:
  tax_withheld: 600
  employee_pension: 219
  employee_unemployment: 26.7
  employee_cash: 2154.3
  employer_health_separately: 57.3
```

### 6. Withholding cannot exceed cash pay

Assume EUR 500 gross cash wages, EUR 1,500 properly valued taxable benefits, and a valid invented 40% ordinary withholding instruction with no ceiling issue. The uncapped calculation is EUR 800, but statutory withholding is limited to the EUR 500 cash amount. The EUR 300 difference is a reconciliation flag, not a conclusion about a separate tax debt or recovery right. Insurance deductions, later payments, benefits-only rules and the final payslip require separate checks.

```oa-check
name: Finland assumed cash limit on wage withholding
inputs:
  gross_cash_wages: 500
  established_taxable_benefits: 1500
  assumed_card_rate: 0.40
steps:
  taxable_wage_base: gross_cash_wages + established_taxable_benefits
  uncapped_withholding: taxable_wage_base * assumed_card_rate
  cash_limited_withholding: min(uncapped_withholding, gross_cash_wages)
  difference_from_uncapped_amount: uncapped_withholding - cash_limited_withholding
expected:
  taxable_wage_base: 2000
  uncapped_withholding: 800
  cash_limited_withholding: 500
  difference_from_uncapped_amount: 300
```

## Ask the client first

- Who is paid, for what work, where, and on which payment dates?
- What are the worker's insurance status and valid withholding instructions?
- Which amounts are wages, benefits, expenses or trade income?
- Is the employer registered as regular, and what is its payment tax period?
- Which reports, corrections, insurer invoices and payments already exist?

## Sources and review limits

Official text retrieved through the search index on 23 October 2026:

- [Prepayment Act][prepayment-law], sections 9, 11 and 13, read directly from the official page's embedded Finnish statutory text on 23 October 2026. Full decree, contribution-law and exceptional-case reconciliation remains open.

- [Vero social insurance contributions][insurance], 2026 table and scope.
- [TyEL eligibility in Finnish][tyel-eligibility], [contribution page][tyel-contributions] and [contribution calculation][tyel-calculation], retrieved in indexed insurer text on 23 October 2026.
- [Employment Fund liability][unemployment-liability] and [payment/rate guidance][unemployment-payment], retrieved as indexed official text on 23 October 2026.
- [Incomes Register deadlines][deadlines].
- [Vero wage reporting and employer contributions][reporting].
- [Wage tax-card guidance][card], updated 14 April 2026; [rate and ceiling guidance][ceiling], updated 1 January 2026, retrieved as indexed official text.

Not yet confirmed: complete current statutory chain, employee withholding and benefit valuation, full pension statutory/coverage review, accident/group-life rules and rates, complete unemployment eligibility and special-category rules, cross-border insurance, exceptional reporting, sanctions and live correction/payment procedures. Independent source-review scope is recorded in the [country README](README.md#evidence-and-next-action); named Finnish accountant review remains outstanding. Payroll and social-contribution coverage remain partial.

[insurance]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/social-insurance-contributions/
[prepayment-law]: https://www.finlex.fi/fi/lainsaadanto/1996/1118
[deadlines]: https://www.vero.fi/en/incomes-register/companies-and-organisations/deadlines-for-reporting/
[reporting]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/how-to-report-wages-and-employers-contributions/

[card]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/tax_card/wage-earners/
[ceiling]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/tax_card/tax-rate-and-income-ceiling/

[unemployment-liability]: https://www.tyollisyysrahasto.fi/en/Unemploymentinsurancecontribution/payment-liability-for-unemployment-insurance-contributions/
[unemployment-payment]: https://www.tyollisyysrahasto.fi/en/Unemploymentinsurancecontribution/paying-unemployment-insurance-contributions/

[tyel-eligibility]: https://www.ilmarinen.fi/tyonantaja/tyel-vakuutus/
[tyel-contributions]: https://www.ilmarinen.fi/en/employer/tyel-contributions/
[tyel-calculation]: https://www.ilmarinen.fi/en/employer/managing-tyel-insurance/determining-the-tyel-contribution/
