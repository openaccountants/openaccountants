---
name: iceland-payroll
description: Use this skill whenever asked about Iceland payroll processing for employed persons. Trigger on phrases like "Iceland payroll", "Icelandic payroll", "staðgreiðsla", "PAYE Iceland", "withholding Iceland", "tryggingagjald", "social security contribution Iceland", "persónuafsláttur", "personal tax credit Iceland", "lífeyrissjóður", "mandatory pension Iceland", "séreignarsparnaður", "supplementary pension", "launagreiðendaskrá", "employer registry Iceland", "RSK 5.02", "launamiði", "skilagreining", "net salary Iceland", "tax withholding Iceland", "employer social cost Iceland", "kjarasamningur", "minimum wage Iceland", "municipal income tax Iceland", "gross to net Iceland", "salary calculation Iceland", or any question about computing employee pay, withholding income tax (state + municipal), or social contributions for Iceland-based employees. This skill covers PAYE (staðgreiðsla) income tax withholding, the personal tax credit, employer social security contribution (tryggingagjald), mandatory occupational pension (employee 4% + employer 11.5%), supplementary private pension, no statutory minimum wage (collective-agreement minimums), and filing obligations to Skatturinn. ALWAYS read this skill before processing any Iceland payroll.
version: 0.1
jurisdiction: IS
tax_year: 2026
last_updated: 2026-09-24
authored_by: OpenAccountants team
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland payroll: employer method for 2026

Figures are for tax year 2026. [Dated official rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/)

## Ask the client first

- Use this method for ordinary Icelandic employed-person payroll in 2026. Establish employer and employee identity, residence and work location, pay date and period, contract and collective agreement, cash wages, benefits, pension arrangements, other deductions, and the employee's tax-credit and bracket instruction. Keep source documents and pay-run approval. Unknown tax residence, posted-worker coverage, contractor status, director fees, child wages, equity, benefit valuation or sector-specific charges require the applicable separate rule before calculation.

The employer must be on the withholding register and have the required electronic identity or withholding web key. The electronic service supports returns, detailed wage information, bank payment claims, corrections and statements. [Skatturinn electronic filing](https://www.skatturinn.is/atvinnurekstur/rafraen-skil/stadgreidsla/)

## The method, step by step

1. Establish wage components, pension arrangements and the employee instruction.
2. Calculate taxable income, withholding and cash net separately.
3. Add employer pension and payroll tax, then file, pay and reconcile.

### Withholding bands and employee instruction

For monthly taxable income in 2026, apply each rate only to its band:

| Monthly taxable income, ISK | Rate |
| --- | ---: |
| Up to 498,122 | 31.49% |
| Above 498,122 through 1,398,450 | 37.99% |
| Above 1,398,450 | 46.29% |
| Evidence | [Official rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) |

The monthly personal tax credit is ISK 72,492. These are withholding figures, not a promise of the employee's final annual tax. [Official rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/)

Obtain instructions on the bracket, whether credit is used, starting month and supported accumulated credit. Multiple employers must use the employee's allocation; they cannot see each other's credit use. Unused credit can accumulate within the year, but cannot cross into another year. People moving to/from Iceland or temporarily working there need the day-limited entitlement checked; a displayed cumulative balance can overstate their entitlement. Obtain the employee's statement when changing employers. Never turn a credit into extra cash after withholding reaches zero. [Personal tax credit](https://www.skatturinn.is/english/individuals/personal-tax-credit/)

The default calculation uses each month's wages separately, including bonuses and overtime. Do not casually average high and low months or give every employer the lowest band; special averaging and multi-employer instructions require their own facts. [Withholding method](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

## Pension and gross-to-net calculation

The current employer instructions use 4% employee pension and an adjustable 11.5% employer default. They exclude ages 15 and younger and 70 or older. Confirm actual contributions, fund, collective agreement, base, remittance schedule and supplementary arrangements. [Employer instructions](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

Employee mandatory contributions can be deducted from income up to 4% of the contribution base. Qualifying additional pension contributions have a separate deduction up to 4%; regular payment and an eligible recipient are conditions. A tax deduction limit does not itself establish a worker's contractual pension entitlement. [Pension deduction conditions](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/)

Keep cash and noncash components distinct:

```text
withholding base = taxable cash remuneration + taxable noncash benefits
                   − eligible employee pension deduction − other supported deductions
income tax withheld = maximum of zero and
                      (progressive band tax − authorised available credit)
bank net pay = cash remuneration + supported cash reimbursements
               − employee pension withheld − income tax withheld
               − other authorised cash deductions
```

A noncash benefit can increase taxable income without adding money to the bank payment. Confirm valuation and pension treatment separately. Do not deduct employer pension or employer payroll tax from employee pay. These formulas are accounting controls; a benefit or reimbursement must have its own legal classification before use.

## Employer pension and payroll tax

Calculate employer pension separately from the employee deduction. General 2026 payroll tax (`tryggingagjald`) is 6.35%. Its base includes taxable benefits as well as wages; special-worker exemptions/rates require supporting evidence. Do not reduce this employer base by the employee's pension deduction. [Payroll tax](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald)

Employer pension contributions also enter the payroll-tax base. The wage-return guidance expressly includes the general employer pension contribution among reportable payroll-tax amounts. Use that base rule with the dated current-year rate; the annual-return page's assessment-year label is not a new wage-year rate. [Payroll-tax base reporting](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/)

```text
employer payroll tax = confirmed total payroll-tax base × applicable employer rate
ordinary cash-wage employer cost = cash wages + employer pension + payroll tax
                                  + other applicable employer obligations
```

For benefits, separately reconcile actual employer benefit cost and the tax valuation; they need not be equal. The ordinary cost formula below assumes no benefits or additional employer charges.

## File, pay and correct

Use the employer service: `Vefskil → Staðgreiðsla → Skila skýrslu`, or supported payroll software. Submission and payment deadline is normally the fifteenth of the following month, shifted to the next working day for weekends/holidays. Confirm the tax calendar and the generated payment claim. Registered legal entities submit a nil return even when no wages were paid. [Filing and corrections](https://www.skatturinn.is/einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum/) [Dated reporting rule](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

### Map the calculation to the return

The official employer instructions map the monthly return as follows:

| Field | Enter or check |
| --- | --- |
| Kennitala | Employee identifier. |
| Laun og hlunnindi | Wages, car benefits, taxable vehicle allowance and taxable daily allowances. |
| Lífeyrissjóður | Paid deductible employee pension, including eligible supplementary savings. |
| Persónuafsláttur / Persónuafsláttur maka | Authorised credit; spouse credit entered separately. |
| Þrepaskipti / Þar af í þrepi 2 | Allocate taxable income between applicable bands. |
| Mótframlag | Actual employer pension; correct the default when needed. |
| Tryggingagjald / Reikna | Calculate employer payroll tax and reconcile the displayed amount. |
| Source | [Official return instructions](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) |

Do not submit the prose calculation as a return. Match each employee row, totals and the payment claim; save the accepted submission and payment evidence.

For an incorrect submitted return, Skatturinn instructs employers to submit the correct return first and then reverse the wrong return using `Vefskil → Staðgreiðsla → Bakfæra skýrslu`; correction login requires the withholding web key. Preserve both references and acknowledgements. Reconcile the resulting liability and actual payments; a return correction is not proof of a cash refund or offset. [Correction sequence](https://www.skatturinn.is/einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum/)

For every run, reconcile wages and benefits, employee deductions, employer pension, tax bases, withholding, payroll tax, the pension-fund payment, bank net pay and ledger. Give the employee the itemised result. At year end reconcile the payroll records to wage statements and employer annual reporting for the actual wage year; use the relevant year's filing instructions before submission. Payroll-tax annual assessment follows the employer wage return. [Annual payroll-tax reporting](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald)

## Worked checks

These hypothetical monthly cases assume an ordinary adult employee, full authorised monthly credit, eligible employee pension at 4%, employer pension at 11.5%, no additional savings, no benefits and no other charges unless expressly stated. Figures use exact arithmetic and show two decimal places with final rounding; actual reporting must follow the service's currency/rounding requirements. They are not authority-approved payroll outputs. [Rates and pension inputs](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) The official case below is the filing reference for identical inputs; the decimal table is secondary arithmetic validation. Do not infer a universal rounding rule from one official example.

### Official monthly example and reconciled payment

For cash wages 600,000, employee pension 24,000, taxable income 576,000, credit 72,492 and employer pension 69,000, the authority displays withholding **113,953** and payroll tax **42,482**. The taxable allocation is 498,122 in the first band and 77,878 in the second. [Official example](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

Using those displayed results, bank pay is **462,047** and employer cost is **711,482**. Reconcile bank pay plus employee pension plus withholding to cash wages; reconcile wages plus employer pension plus payroll tax to cost. These are derived controls for the official example. Actual employer/employee facts and the accepted service output still control filing. [Source illustration](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

### Decimal validation examples

Displayed band subtotals are individually rounded for readability; total tax is calculated from unrounded components, so the displayed subtotals can differ from the rounded total.

| Case | Employee result | Employer result |
| --- | --- | --- |
| A: cash wages 400,000 | Employee pension 16,000; taxable base 384,000; band tax 120,921.60; withholding 48,429.60; bank net 335,570.40. | Employer pension 46,000; payroll-tax base 446,000; payroll tax 28,321; combined cost 474,321. |
| B: cash wages 600,000 | Employee pension 24,000; base 576,000. First-band tax 156,858.62; remaining base 77,878 gives second-band tax 29,585.85. Total band tax 186,444.47; withholding 113,952.47; bank net 462,047.53. | Employer pension 69,000; payroll-tax base 669,000; payroll tax 42,481.50; combined cost 711,481.50. |
| C: cash wages 200,000 | Employee pension 8,000; base 192,000; band tax 60,460.80; withholding zero; bank net 192,000. Unused monthly credit 12,031.20 needs supporting same-year records before later use. | Employer pension 23,000; payroll-tax base 223,000; payroll tax 14,160.50; combined cost 237,160.50. |
| K: cash wages 1,800,000 | Employee pension 72,000; taxable base 1,728,000. First-band tax 156,858.62; second-band tax 342,034.61; third-band excess 329,550 gives tax 152,548.70. Total band tax 651,441.92; withholding 578,949.92; bank net 1,149,050.08. | Employer pension 207,000; payroll-tax base 2,007,000; payroll tax 127,444.50; combined cost 2,134,444.50. |
| Evidence | [Rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) and [pension](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) | [Payroll tax](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald) |
| D: illustrative noncash control only | Cash 400,000, already-established taxable noncash benefit 20,000, documented deductible pension 16,000: base 404,000; band tax 127,219.60; withholding 54,727.60; bank net 329,272.40. | Confirm benefit valuation, pensionability, employer contributions and employer tax base separately; no total-cost conclusion. |

Additional decision checks: exactly at the first band ceiling, no amount enters the next band; above the upper ceiling, only the excess enters the highest band. A second employer without current bracket/credit instructions must obtain them before a final calculation. A prior-year unused credit cannot reduce this year's tax. An erroneous filed return follows the correct-then-reverse sequence. A registered legal entity with no wages still files the nil return.

## When to refuse or refer

- Return the period, employee scope, evidence gaps, each cash/noncash component, pension fund and bases, employee and employer contributions, band calculation and credit usage, withholding, bank net, employer costs, filing deadline and references, and reconciliation result. Do not label an unresolved input as confirmed. Recheck before the next wage year, when an official rate/rule changes, or when worker status, pension terms, residence or benefit arrangements change. Refer cross-border, special-worker and disputed classification questions for a specific supported method; do not substitute this ordinary calculation.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
