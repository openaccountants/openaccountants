---
name: azerbaijan-vat
description: 'Use this skill for 2026 Azerbaijan VAT working papers for ordinary domestic VAT taxpayers, importers, exporters and recipients of non-resident services. It covers compulsory and voluntary registration, the rolling and single-contract thresholds, 2026 POS turnover weighting, tax points, input credit and mixed-use allocation, monthly returns, reverse charge, cancellation and retained inventory. Trigger on Azerbaijan VAT, EDV, VAT deposit account, non-resident services, input VAT, mixed taxable and exempt supplies and VAT registration. It covers the separate registration and filing process for foreign B2C electronic sellers. Specialist agricultural margin, leasing and other special schemes need separate source checks. Checked against the law (tier 2); no accountant has signed it off.'
version: 2.1
jurisdiction: AZ
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
---

# Azerbaijan Value Added Tax v2.1

> **Checked against the law.** Tax year 2026. Figures independently re-checked against the official sources on 31 October 2026. General reference for working papers; a qualified professional must review the facts and filing position. No accountant has signed this skill off.

## Who this applies to

Persons registered or required to register for Azerbaijan VAT (ƏDV), importers and recipients acting as tax agents for non-resident services under [Tax Code art. 153–155, 169](https://e-qanun.az/frameworks/46/f_46948.html). Ordinary domestic businesses, imports, exports and mixed taxable/exempt activities are covered. A simplified-tax business is not exempt from all reverse-charge obligations merely because it is outside ordinary VAT registration.

Rolling turnover is not the only registration trigger. Excise/mandatory-marked goods producers and building-construction businesses are mandatory VAT taxpayers under art. 154.6. Non-resident internet sellers to unregistered Azerbaijan customers have a separate registration rule under art. 33.8-1, not the domestic rolling threshold. The foreign-seller registration and filing process below follows Cabinet Decision 387, as consolidated for the 2026 statutory threshold.

## Rates, bands and thresholds

| Item | Amount / treatment | Tax year / period | Official source |
|---|---|---|---|
| Standard VAT | 18% of VAT-exclusive consideration/base | 2026 | [Tax Code art. 173.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Exports of goods and listed art. 168.1.5 services | 0%, subject to classification/evidence | 2026 | [Tax Code art. 165.1.3](https://e-qanun.az/frameworks/46/f_46948.html) |
| International/transit transport and listed related services | 0%, with the postal exception | 2026 | [Tax Code art. 165.1.4](https://e-qanun.az/frameworks/46/f_46948.html) |
| Domestic compulsory registration | Taxable operations above 200,000 over rolling 12 months | 2026 | [Tax Code art. 155.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Single contract/transaction trigger | Total above 200,000; register before transaction | 2026 | [Tax Code art. 155.1, 157.3.1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Qualifying public retail/service POS threshold weighting | 0.5 × qualifying turnover for threshold only | Operations from 1 Jan 2026 | [Tax Code art. 155.1-1](https://e-qanun.az/frameworks/46/f_46948.html); Law 297-VIIQD transitional art. 18.1 |
| Voluntary deregistration threshold | Prior full 12 months at most 100,000 after art. 158.2-1 POS weighting; at least 1 year after last registration, subject to exceptions | 2026 | [Tax Code arts. 158.2–158.2-1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Non-resident B2C electronic seller trigger | Calendar-year turnover above USD 10,000 equivalent; register within 30 days | Current 2026 text | [Tax Code art. 33.8-1](https://e-qanun.az/frameworks/46/f_46948.html) |
| Catering public integrated-POS turnover deduction | 50% of qualifying POS turnover | 1 Jan 2026–31 Dec 2028 | [Tax Code art. 174.5](https://e-qanun.az/frameworks/46/f_46948.html) |
| Medical/public private-practice integrated-POS turnover deduction | 50% of qualifying POS turnover | 1 Jan 2024–31 Dec 2026 | [Tax Code art. 174.5](https://e-qanun.az/frameworks/46/f_46948.html) |

## The base

Determine supply, place, time, VAT base and rate before aggregating a return. Art. 161 uses consideration excluding VAT, including the specified other duties/taxes/charges. For a VAT-inclusive price at the standard rate, VAT equals gross × 18/118 and net equals gross/1.18. Do not use the invoice amount as VAT-exclusive without checking the contract.

Under art. 166, the ordinary tax point is payment. Advance receipts are taxable when paid; instalments are separate transactions to their extent. Set-off, barter, gratuitous supplies, expired debt and other statutory cases have their own tax points. Cash-register operations follow the receipt rule in art. 166.1.1-1. Do not replace this system with a universal invoice-date or delivery-date rule. Apply art. 163 adjustments when price, cancellation or return facts change.

Separate standard-rate, zero-rate, exempt and outside-scope supplies. Zero-rated transactions remain taxable and permit eligible input credit (art. 175.7); exempt transactions do not generally permit input credit (art. 175.6). Art. 164 gives specific exemptions; for example qualifying producers' own agricultural product sales are exempt from 1 January 2014 for thirteen years (art. 164.1.18). Financial services for this purpose include insurance and reinsurance and the related agent and broker services (art. 13.2.14.7). Other art. 164 exemptions include paid education services (art. 164.1.13) and metro passenger transport (art. 164.1.12). Goods and services for the official use of accredited international organisations and foreign diplomatic and consular missions, and for the personal use of their non-citizen diplomatic and administrative staff and families, are zero-rated (art. 165.1.1). Test a financial-service exemption under art. 164.1.2 against its current definition; this skill does not extend it to every bank or leasing invoice. Law 413-VIIQD of 26 May 2026 changes the leasing exemptions from 25 December 2026, the date the Tax Code's commencement notes give for it (it enters into force with the Law on Financial Lease, 412-VIIQ). From that date "leasing" (lizinq) becomes "financial lease" (maliyyə icarəsi) in arts. 164.1.2, 164.1.2-1 and 164.1.25; art. 164.1.34-1 loses its "without transfer of ownership" condition and covers renting farm machinery to agricultural producers; and art. 164.1.50 drops "or leasing" from the exemption for aircraft and engines rented from non-residents without an Azerbaijan PE (Law 413-VIIQD arts. 2.8.1-2.8.4, 26). Use the current wording for operations up to 24 December 2026 and the amended wording from 25 December 2026.

For domestic input credit, obtain a valid electronic invoice and evidence that the VAT-exclusive value was paid from the purchaser's bank/payment account to the supplier's account and VAT was paid to the VAT deposit account, subject to art. 175's express exceptions. Credit the corresponding paid part of instalments. Cash-register receipts alone, non-compliant invoices and sham-transaction documents do not establish credit (arts. 175.9, 175.11). The VAT-deposit payment is due within one working day of paying the net consideration under art. 175.1.3, with the art. 177.5 exception. Import documents evidencing paid import VAT support credit under art. 175.10.

Directly attribute input VAT to taxable and exempt transactions where separately evidenced. For common mixed-use input, restrict credit to the statutory taxable-use proportion; exclude private/non-business use. Art. 175.4 provides the taxable-turnover share for mixed taxable/exempt transactions and permits full credit for separately accounted taxable inputs. A PIT or corporate deduction is not proof of VAT recoverability. Check the additional restrictions for state-funded and specified social expenditure in arts. 175.3 and 175.6.

Compute payable VAT as output VAT plus adjustments/reverse-charge liability less allowable input credit under art. 174.1. Record excess credit distinctly. For taxpayers with at least 50% zero-rated turnover, art. 179.1 provides repayment within 20 days of application; others use the four-month limit in art. 179.2. Risky-taxpayer claims are subject to the commencement qualification in art. 179.4. Do not promise a refund without a valid application and those checks.

For the 2026 catering relief, only services to the public paid through POS terminals integrated with the cash register qualify. Subtract 50% of that qualifying turnover from total taxable turnover, then apply 18%. Other bank transfers are not automatically qualifying POS receipts. The same art. 174.5 relief for medical institutions/private medical practice has its own 2024–2026 period. Keep qualifying and other receipts separate. Do not confuse this deduction with the 0.5 registration-threshold weighting or the separate 6% catering simplified tax.

The agricultural trade-margin regime under arts. 153.3, 159.1 and 174.4 applies for the stated five-year period from 1 January 2022, subject to purchase/sales records. From 2026 the definition includes qualifying farmed fish, excluding the specified processing and foreign-origin fish treatment. Imported agricultural products have an election under art. 175.13. These are specialist schemes outside the ordinary return examples.

## Deadlines and filing

For rolling turnover, compulsory registration takes effect on the first day of the month after crossing the threshold; apply within ten days of that date. For a single contract above 200,000, apply before the transaction. Mandatory-category businesses apply with initial registration or before starting the relevant later activity. Voluntary registration ordinarily takes effect on the first day of the following reporting period ([Tax Code art. 155.1, 156–157](https://e-qanun.az/frameworks/46/f_46948.html)). Apply the POS weighting only to operations from 1 January 2026, not earlier receipts within the same rolling window.

Ordinary domestic VAT reporting periods are calendar months (art. 178). File and pay by the following month's 20th under art. 177.1–177.2 via the State Tax Service electronic system. The registered foreign electronic seller has the distinct payment deadline below. Imported goods VAT is assessed/collected by customs under art. 177.4. For a non-VAT-registered tax agent buying in-scope non-resident services, pay reverse-charge VAT within seven days after paying the supplier and file by the following month's 20th (art. 169.5). A VAT-registered agent pays with the monthly VAT return and claims credit only when art. 169.4 and art. 175 conditions are met.

For a foreign B2C electronic seller without an Azerbaijan PE, [Cabinet Decision 387, paragraphs 1.3, 2 and 3-1](https://frameworks.e-qanun.az/55/f_55514.html) requires registration through the electronic-commerce tax administration platform within 30 days after the calendar-year USD 10,000-equivalent threshold is exceeded. VAT registration takes effect from tax registration. Supply the entity/home-country registration and tax information, addresses, activities, payment currency, intended start date, at least two responsible persons and the prescribed electronic supporting documents. The authority checks the submission within 20 working days under paragraph 2.2. Document authentication and translation follow section 7. Changes in the paragraph 2.7 information require notification within 20 working days (paragraph 4.1.2).

The registered seller calculates its own Azerbaijan VAT and submits monthly returns through that platform by the following month's 20th under Tax Code arts. 177.2 and 178; the special art. 177.1.4 payment deadline is the last day of the following month. Pay in the selected AZN, USD, EUR or GBP currency under Decision 387 paragraphs 2.7.9 and 3-1.4, converting foreign-currency payment to AZN at the Central Bank's official rate on the payment day. Paragraphs 1.5.1–1.5.4 identify customer-location evidence, including local payment provider, customer location, device IP and mobile country code. Under paragraph 1.7, the registered seller's in-scope B2C supplies are not also collected through the art. 169 payment-agent route; paragraph 1.7-1 retains that route for unregistered sellers. Screen this status before applying payment-agent collection, so the same receipt is not charged twice. A seller deregistered under section 3 returns to the applicable art. 169.3 treatment; previous liabilities remain due.

If taxable business ceases, apply for deregistration under art. 158.1. For voluntary low-turnover deregistration, art. 158.2-1 also weights qualifying retail/public-service POS turnover by 0.5 when applying the 100,000 test in art. 158.2. This rule took effect on 1 January 2026 under Law 297-VIIQD art. 19.6. The restriction to operations after 1 January 2026 in art. 18.1 expressly names arts. 155.1-1 and 218.1-1, not art. 158.2-1; do not transplant that receipt-date restriction into the deregistration test. Inventory retained at cancellation is treated as supplied immediately before cancellation under arts. 159.6, 161.3 and 166.3, subject to the overriding art. 159.7 credit-entitlement rule. If the goods were acquired in a VAT-taxed transaction but the purchaser had no art. 175 entitlement to input credit, their supply is not taxable under that provision; if entitlement was partly denied, reduce the taxable amount by the denied proportion. Establish entitlement from the acquisition/use records, not simply whether credit was claimed. A final return on liquidation/individual cessation is required within 30 days, without extending the normal return deadline (art. 177.2). Small turnover alone does not cancel registration.

## Penalties and interest

Under [Tax Code art. 57.1](https://e-qanun.az/frameworks/46/f_46948.html), failure without grounds to submit a required return for a period with taxable or exempt operations or tax objects attracts AZN 40. Under [Tax Code art. 58.1](https://e-qanun.az/frameworks/46/f_46948.html), an understated or evaded tax amount attracts a 50% financial sanction, excluding additional tax assessed by a desk audit; the horizontal-monitoring case in art. 58.1-1 uses 25%. Under [Tax Code art. 59.1–59.2](https://e-qanun.az/frameworks/46/f_46948.html), late tax or advance payments bear 0.1% per overdue day, for at most one year. For additional tax identified by field audit or horizontal monitoring, interest starts on the assessment date under art. 59.2. Apply the facts and procedural exceptions before assessing a sanction.

Operating without compulsory VAT registration attracts 50% of the VAT payable for the unregistered period under art. 58.4. Failure to make the specified timely VAT-deposit payment attracts 50% of the unpaid VAT under art. 58.6, subject to its exception. These are separate conduct tests; do not automatically add every sanction to the same error.

## Cross-border points

Goods are supplied where delivered, with dispatch/installation exceptions in art. 167. Services use art. 168's ordered tests: immovable property, movable-property work, cultural/education/sport activity, transport, listed recipient-location services, then the supplier-place fallback. The earliest applicable paragraph controls. Legal/accounting/consulting, intellectual property, specified electronic services and other listed services use the recipient-location test under art. 168.1.5. Do not infer export zero-rating from payment in foreign currency.

Imported taxable goods use customs value plus applicable duties/taxes excluding VAT and road tax (art. 162). For in-country services of an unregistered non-resident, assess reverse charge under art. 169 independently of income-tax withholding. Art. 33.8-1 expressly excludes certain remotely delivered professional services, real-time education/training and event-ticket booking from its electronic-commerce definition; that does not erase other VAT source/agent obligations. Apply the registered foreign B2C procedure and its separate payment timing above, with the customer-location and exclusion tests in Cabinet Decision 387.

## Two worked examples that recompute

### Ordinary monthly return

Assume 50,000 VAT-exclusive paid taxable sales and 20,000 VAT-exclusive purchases, with all input conditions met and no adjustments. Output VAT is 9,000; input VAT is 3,600; payable is 5,400.

```oa-check
name: AZ ordinary VAT 2026
inputs:
  sales_net: 50000
  purchases_net: 20000
steps:
  - output_vat: sales_net*0.18
  - input_vat: purchases_net*0.18
  - payable: output_vat-input_vat
expected:
  output_vat: 9000
  input_vat: 3600
  payable: 5400
```

### Mixed taxable and exempt use

Assume 80,000 standard-rate VAT-exclusive turnover and 20,000 exempt turnover. Common inputs have 9,000 VAT and cannot be directly attributed; all payment/invoice conditions are met. The taxable share is 80%, giving 7,200 input credit. Output VAT of 14,400 less credit gives 7,200 payable. No art. 174.5 relief applies in this example.

```oa-check
name: AZ mixed VAT input credit 2026
inputs:
  taxable_sales: 80000
  exempt_sales: 20000
  common_input_vat: 9000
steps:
  - share: taxable_sales/(taxable_sales+exempt_sales)
  - credit: common_input_vat*share
  - output_vat: taxable_sales*0.18
  - payable: output_vat-credit
expected:
  share: 0.8
  credit: 7200
  payable: 7200
```

## Ask the client first

- What are registration status, rolling turnover, single-contract values and mandatory-category activities?
- Which receipts occurred from 1 January 2026 and which POS payments qualify for threshold weighting or catering/medical relief?
- What is the actual supply, customer location, payment/tax point and VAT-inclusive or exclusive price?
- Are there exempt sales, private use, valid electronic invoices, deposit-account payments and import documents?
- Are there non-resident suppliers, B2C electronic sales, customs entries or export evidence?
- Is this a specialist margin/election case or a cessation with retained assets?

## Sources

| Source and provisions read | Official URL | Read on |
|---|---|---|
| Tax Code, arts. 33.8-1, 57–59, 153–179 and commencement annotations | https://e-qanun.az/frameworks/46/f_46948.html | 2026-10-31 |
| Cabinet Decision 387, current consolidated electronic-seller procedure, paras. 1–7 | https://frameworks.e-qanun.az/55/f_55514.html | 2026-10-31 |
| Law 297-VIIQD, arts. 18.1 and 19.6, commencement and POS transition | https://frameworks.e-qanun.az/61/f_61117.html | 2026-10-31 |
| Law 413-VIIQD of 26 May 2026, arts. 2.8.1-2.8.4 and 26 (leasing exemptions from 25 December 2026) | https://frameworks.e-qanun.az/62/f_62107.html | 2026-10-31 |
| STS 2026 amendment FAQ, POS transitional provision art. 18.1 | https://www.taxes.gov.az/uploads/2026/faq/FAQ2026.pdf | 2026-10-31 |

Not yet confirmed: a general block on input VAT for passenger cars or entertainment (the old version of this skill stated one from a secondary source; it was not found in art. 175); which contracts the Law on Financial Lease (412-VIIQ) treats as a financial lease, which decides what falls within the amended exemptions from 25 December 2026. Specialist agricultural margin/election calculations are outside scope.

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
