---
name: tj-corporate-income-tax
description: "Compute ordinary 2026 Tajikistan corporate income tax, current payments and annual settlement; distinguish manufacturing transition, financial/mobile companies, non-resident withholding and treaty-document conditions. Special regimes and live declaration fields require separate review."
jurisdiction: TJ
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: international
type: computation
version: 0.1
---

# Tajikistan corporate income tax v0.1

> **General reference only.** This skill prepares a working paper for review by a qualified Tajikistan professional. Confirm the facts, source version and filing procedure before filing, paying or taking a tax position.

**Built from the law. Not yet approved.** Tax year 2026; checked on 2026-11-15.


## Scope

For ordinary corporate income-tax payers, including resident legal entities and non-residents operating through a Tajik permanent establishment. A resident company has worldwide-income exposure; a non-resident permanent establishment computes on connected Tajik-source income and permitted deductions. Non-PE gross withholding is a separate computation. [Arts. 180-182](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


## Ask the client first

- Incorporation and management location, residence certificates and any permanent establishment.
- Activities and separate income streams, including manufacturing, extraction, finance or mobile telecommunications.
- Tax regime, investment agreement, exemption approval and any tax-holiday history.
- Accounts, tax adjustments, documented deductions, asset schedules and loss vintages.
- Prior-year tax, current monthly gross income, first-quarter comparison, advances and withholding credits.
- Cross-border recipient, beneficial owner, payment type, treaty application and residence evidence.


## The method, step by step


### Determine the current rate

| Activity and period | Rate | Official provision |
|---|---|---|
| Ordinary manufacturing/production of goods, from 1 January 2026 | 18%. The printed 13% in art. 183(4) applied only through 31 December 2025 under the transition | [Arts. 183(4), 397(13)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Extraction/processing of natural resources and ordinary other activities | 18%, subject to a separately established exemption or special regime | [Art. 183(4)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Financial credit organisations and mobile companies | 20%, subject to a separately established exemption or special regime | [Art. 183(4)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |

A company is resident if established under Tajik law or if its principal management body is in Tajikistan. A foreign legal form alone does not decide the tax residence. Establish the permanent-establishment question before treating every payment to a foreign business as gross withholding. [Arts. 14(8), 182(2)-(3)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Reconcile accounting profit to taxable profit

Compute taxable income as gross income less deductions permitted by the Code. Document actual income-related expenditure; accounting expense is not automatically a tax deduction. Exclude exempt income and its related treatment only after confirming the applicable statutory exemption. [Arts. 182, 189-190](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Apply art. 192 disallowances and relevant limitations before applying the rate. In particular, private/non-business expenses, corporate income tax and budget fines/penalties cannot simply remain in the deductible expense total. Capital expenditure needs its statutory asset/depreciation treatment. [Arts. 190, 192](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

An ordinary business loss may be carried forward for up to 3 years; non-business property-disposal losses are restricted to the corresponding property-disposal income and have their own carryforward. Tax-holiday losses require separate consideration, rather than automatic carryforward. Keep year-by-year evidence. [Arts. 189(4), 197](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


### Current payments and annual settlement

| Obligation | Timing or computation | Official provision |
|---|---|---|
| Ordinary monthly current payment | Due by the 15th after the reporting month; in the 12-month cycle beginning each 15 April, at least the greater of prior-year tax ÷ 12 and 1% of reporting-month gross income (the fraction is in words on the page) | [Art. 242(1)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Annual corporate return and annual accounting statements, including balance sheet | By 1 April after the reporting year | [Art. 241(4), (8)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Final annual computation and payment | By 10 April after the reporting calendar year; credit current payments against annual liability | [Arts. 242(3), 243(6)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |

Art. 242(2) permits a different current-payment calculation where current first-quarter gross income is less than 50% of the corresponding prior-year quarter: with quarterly reports, use previous-quarter tax divided by 3, still at least 1% of reporting-month gross income. Confirm eligibility and the relevant quarter before changing the ordinary method. Excess current payments are credited against other liabilities or refunded under art. 242(3); late current payments carry interest under art. 242(4). [Art. 242(2)-(4)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Prepare separate schedules for gross income, deductible costs, disallowances, capital allowances, exempt income, allowable losses, tax by activity, credits and balance due. Reconcile advances to tax-account evidence. Obtain the current corporate declaration and attachments from the Tax Committee [personal cabinet](https://www.andoz.tj/) or competent office, map the schedules to its current fields and retain the receipt/payment reconciliation. Current fields and penalty calculations are a handoff boundary, not verified in this skill.


### Payments to non-residents without a connected permanent establishment

| Payment with Tajik source, subject to treaty and statutory exceptions | Domestic withholding rate | Official provision |
|---|---|---|
| Dividends paid by a resident company | 12%; taxed dividends are excluded from the recipient's further gross income under art. 237(2) | [Arts. 237, 239(8)(1)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Interest paid by a resident or non-resident permanent establishment | 12% ordinarily; statutory exempt recipients and the controlled-foreign-company rule must be tested | [Art. 238(1)-(5)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Interest paid by a resident enterprise, other than a financial credit organisation, to a controlled foreign company | 18%, overriding the ordinary interest rate | [Art. 238(5)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |
| Royalties falling within other non-resident Tajik-source income, unconnected to a permanent establishment | 15% of gross income, without expense deductions, subject to art. 239's VAT adjustment and treaty rules | [Art. 239(1), (3), (8)(7)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) |

Do not call every interest payment final: art. 238(3) gives individual-recipient finality, while art. 238(4) requires a taxable resident legal-entity recipient to include gross interest and credit evidenced withholding. The art. 238(2) exclusions include resident financial credit organisations, finance authorities, the central bank and resident finance-leasing companies. Other non-resident payment classes can have different rules and are outside this limited table. [Arts. 238-239](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

Treaty reduction is not automatic. For dividends, interest and royalties, obtain the non-resident application, residence document, evidence that the recipient is the final/beneficial recipient, and treaty eligibility; disclose the payment, rate and treaty in the withholding computation. No country treaty rate is confirmed here. Withhold/payment timing and certificates follow art. 236, including its wage-bank-payment rule and otherwise the 10-working-day rule after month end. [Arts. 174, 236(4)-(6)](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


## Worked cases


### Ordinary company: profit, current payments and annual balance

Illustrative ordinary company: taxable gross TJS 1,000,000; permitted expenses TJS 700,000; no exemption, loss or other adjustment. Profit is TJS 300,000; corporate tax is TJS 54,000. Evidenced current payments of TJS 48,000 leave TJS 6,000 payable at annual settlement.

```oa-check
name: Ordinary corporate annual settlement
inputs:
  gross_income: 1000000
  permitted_expenses: 700000
  current_payments: 48000
steps:
  taxable_profit: gross_income - permitted_expenses
  annual_tax: taxable_profit * 0.18
  balance: annual_tax - current_payments
expected:
  taxable_profit: 300000
  annual_tax: 54000
  balance: 6000
```


### Current-payment floor determines the amount

Illustrative ordinary art. 242(1) method, in the cycle beginning 15 April: prior-year tax TJS 54,000 gives a TJS 4,500 monthly benchmark. At monthly gross income TJS 300,000 the turnover floor is TJS 3,000, so pay TJS 4,500. At TJS 600,000 the floor is TJS 6,000, so pay TJS 6,000. This is a current payment, not final tax on profit.

```oa-check
name: Decide the binding current-payment benchmark
inputs:
  prior_year_tax: 54000
  lower_month_gross: 300000
  higher_month_gross: 600000
steps:
  prior_benchmark: prior_year_tax / 12
  lower_floor: lower_month_gross * 0.01
  higher_floor: higher_month_gross * 0.01
  lower_payment: max(prior_benchmark, lower_floor)
  higher_payment: max(prior_benchmark, higher_floor)
expected:
  prior_benchmark: 4500
  lower_floor: 3000
  higher_floor: 6000
  lower_payment: 4500
  higher_payment: 6000
```


## When to refuse or refer

Refer special/simplified regimes, incentives, exempt or mixed activities, related-party pricing, foreign credits, permanent-establishment allocation, financial/mobile classification and treaty entitlement. Do not use the expired manufacturing rate, net an unsupported expense into profit, or submit without the official declaration and a reconciled tax account.


## Sources

| Official source | Read for | Date read |
|---|---|---|
| [Tax Committee, current consolidated Tax Code](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) | Read for arts. 14(8), 180-183, 189-192, 197, 174, 236-243 and 397(13), including adjacent exceptions. | 2026-11-15 |

Not yet confirmed: Live corporate/withholding declaration fields and payment references; client-specific incentive, depreciation, foreign-credit and treaty computations; penalty amounts. No treaty rate table is supplied. The old manufacturing 13% rate is retained only as an expired historical rule.

