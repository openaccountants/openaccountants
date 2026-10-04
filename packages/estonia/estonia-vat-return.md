---
name: estonia-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Estonian VAT return (KMD form) for any client. Trigger on phrases like "prepare VAT return", "do the KMD", "fill in KMD", "Estonian VAT", "kaibemaks", or any request involving Estonia VAT filing. This skill covers Estonia only and standard KM registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Estonian VAT work.
version: 2.0
jurisdiction: EE
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia VAT return (KMD and KMD INF)

## Scope

This Guide covers the monthly Estonian VAT return, form KMD, and its annex, form KMD INF, for a person registered as liable to VAT in Estonia (a company such as an OÜ or AS, or a sole proprietor, FIE). It covers the rates in force for 2026 periods, the registration threshold, the monthly deadline and payment, domestic and cross-border reverse charge, the report on intra-Community supply (form VD), the OSS and IOSS special schemes at a summary level, corrections, bad-debt relief, and interest on late payment.

The primary year is 2026. Estonia's taxable period is one calendar month, so every 2026 month is filed under the rules below. A short dated section near the end covers 2025 periods, which straddle the 1 July 2025 rate change.

All figures come from the Estonian Tax and Customs Board (Maksu- ja Tolliamet, ETCB) at emta.ee. The ETCB publishes English translations of the forms "for your information only"; the Estonian original is the form that is filed ([KMD forms page](https://www.emta.ee/en/business-client/taxes-and-payment/tax-returns-exchange-information/vat-return-forms-vd-and-vdp)).

Out of scope: VAT groups beyond a mention, the margin schemes for second-hand goods and travel services, partial exemption calculations, import VAT deferment authorisations, and the special-case VAT return for unregistered persons.

## Ask the client first

- **Are you registered as liable to VAT in Estonia, and from what date?** Get the VAT number. Registration takes effect from the day the threshold was exceeded, not the day the ETCB decides.
- **Are you a full taxable person, or a taxable person with limited liability?** Limited-liability persons file KMD but do not file the KMD INF annex.
- **Which month is being filed?** The rate depends on the time of supply, so the period matters.
- **Do you use cash accounting for VAT?** It changes when supply arises and keeps some transitional rates open until 31 December 2026.
- **What did you sell?** Standard-rated, accommodation, books, medicines and medical devices, press publications, exports, sales of goods or services to EU businesses, exempt supplies (financial, insurance, some property), and sales to consumers in other EU countries.
- **For every EU business customer: do you hold a valid VAT number from their Member State?** No valid number means no 0% on an intra-Community supply of goods.
- **What did you buy from abroad?** Services from EU or non-EU suppliers, goods from other EU countries, imports, and whether the foreign supplier charged its own VAT.
- **Do you own, lease or run any passenger cars (category M1)?** Is any car used only for business, with records that preclude private use?
- **Do you make any exempt supplies?** If yes, input VAT may need partial deduction and a year-end recalculation.
- **Did any customer fail to pay an invoice, or were credit notes issued?**
- **Are you in the OSS or IOSS scheme?** Those supplies go on a separate special-scheme return, not on KMD.
- **Is the company run by e-residents with no staff, office or permanent establishment in Estonia?** See "When to refuse or refer".

## The method, step by step

1. **Confirm who must file.** A KMD and its KMD INF annex are filed by persons registered as VAT payers, and also by persons not registered who have issued an invoice or other sales document showing a VAT amount. A taxable person with limited liability files the KMD but not the annex ([ETCB, Filing VAT returns and reports](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports)).
2. **Fix the taxable period.** It is one calendar month. Put each supply in the month in which it arose (time of supply), which also fixes the rate.
3. **Sort every sale by rate and box.** Standard rate to line 1, the 13% rate to line 2², the 9% rate to line 2, zero-rated supply to line 3 and its sub-lines, exempt supply to line 8, and supply under the special arrangements of § 41¹ of the VAT Act to line 9.
4. **Self-assess reverse-charge purchases.** Services from foreign suppliers not registered in Estonia, and intra-Community acquisitions of goods, go into line 1 (or line 2 or 2² at a reduced rate) so that output VAT is calculated in line 4. Also show them in the information lines 6, 6.1, 7 and 7.1.
5. **Compute output VAT in line 4.** The form's formula is 24% of line 1 + 20% of line 1¹ + 22% of line 1² + 9% of line 2 + 5% of line 2¹ + 13% of line 2².
6. **Collect deductible input VAT in line 5.** Include reverse-charge VAT you are entitled to deduct. Show import VAT (5.1), fixed assets (5.2) and passenger cars (5.3 or 5.4) as sub-lines of line 5.
7. **Apply restrictions.** Passenger cars: usually half. Mixed taxable and exempt activity: partial deduction. Private use: none.
8. **Adjustments.** Year-end recalculation of partial deduction, fixed-asset adjustments and car-use changes go in line 10 (increase) or line 11 (decrease), never both.
9. **Read the result.** Line 12 is VAT payable and line 13 is overpaid VAT. A refund needs a separate application for a refund from the prepayment account.
10. **Build the KMD INF annex.** Part A lists sales invoices and Part B purchase invoices, where the total per transaction partner without VAT is at least EUR 1,000 in the period.
11. **File the VD report** if you made intra-Community supplies of goods or general-rule services to businesses in other EU countries.
12. **File and pay by the 20th** of the following month through e-MTA or X-tee.

## Figures with years

### Rates for 2026 periods

| Rate ([ETCB rates](https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate)) | Applies to | In force | KMD line |
| --- | --- | --- | --- |
| 24% | Standard rate: everything without a specific reduced rate or exemption | From 1 July 2025 (22% from 1 January 2024 to 30 June 2025) | 1 |
| 13% | Accommodation, and accommodation with breakfast; not other services sold with it | From 1 January 2025 (previously 9%) | 2² |
| 9% | Books and educational literature (printed or electronic); listed medicines, contraceptives and medical devices for personal use of disabled persons; press publications (printed or electronic, not mainly advertising, erotic, or video or music content) | Press publications back at 9% from 1 January 2025 (5% from 1 August 2022 to 31 December 2024) | 2 |
| 0% | Exports; intra-Community supply of goods to a buyer with a valid EU VAT number, shown on the VD report; listed transport and ship/aircraft supplies | Standing | 3, 3.1, 3.1.1, 3.2, 3.2.1 |
| 5% | Only for cash-accounting users: press publications invoiced and supplied before 1 January 2025, where supply arises later; allowed until 31 December 2026 | Transitional | 2¹ |
| 9% on accommodation | Only for cash-accounting users: accommodation invoiced and provided before 1 January 2025; allowed until 31 December 2026 (a right, not an obligation) | Transitional | 2 |
| 22% and 20% | Only for credit notes on invoices originally taxed at those rates | Historic | 1² (22%), 1¹ (20%) |

Sources: [standard rate](https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate); [rates handbook](https://www.emta.ee/en/node/336/main_chapter/83171/pdf); [VAT Act changes](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax); [KMD form from 01.07.2025](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf).

The ETCB says the correct rate "must be chosen on the basis of the time of supply". Software, games and web publications that are mainly advertising stay at 24%.

### Thresholds and dates

| Item | Figure | Source |
| --- | --- | --- |
| Registration threshold | Supply with place of supply in Estonia exceeding EUR 40,000 from the start of the calendar year | [Registration handbook](https://www.emta.ee/en/node/333/handbook/4/pdf) |
| Time to apply after crossing it | Three working days; the ETCB then has five working days to decide | Registration handbook |
| Limited-liability registration | Intra-Community acquisitions of goods exceeding EUR 10,000 from the start of the year | [Registration page](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer) |
| EU small-business scheme (foreign small enterprises) | EU-wide supply under EUR 100,000 | Registration handbook |
| OSS distance-sales and digital-services threshold | EUR 10,000 across all other Member States together | [Special schemes page](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services) |
| KMD INF annex | Invoices totalling at least EUR 1,000 without VAT per transaction partner in the period | [Filing page](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports) |
| KMD, KMD INF and VD deadline | 20th day of the month after the period; VAT is also payable by then | Filing page; KMD form |
| OSS return | Quarterly, by the last day of the month after the quarter | Special schemes page |
| IOSS return | Monthly, by the last day of the following month | Special schemes page |
| Interest on late tax | 0.06% a day (21.9% a year) | [Payment of interests](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests) |
| Passenger-car input VAT | Usually 50% deductible | [Passenger cars and VAT](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting) |
| Bad-debt relief with more than EUR 30,000 of VAT in the claim | Claim must be confirmed by a court judgment in force | [VAT Act changes](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax) |

### What counts toward the EUR 40,000 (from 1 January 2025)

- Taxable supply of goods and services, including zero-rated supply, but not transfers of fixed assets.
- Real-estate transactions (sales, leases, rentals) under § 16(2) clauses 2, 3 and 6, except fixed-asset transfers and occasional transactions.
- Insurance and financial services, except occasional services.
- Only supply whose place of supply is Estonia. If all of a person's supply is exempt or zero-rated (and none is an intra-Community supply of goods), there is no registration obligation however large it is.
- Under a margin scheme, the full amount received counts, not the margin.

A foreign business with no permanent establishment in Estonia has no threshold: if it makes supply taxable in Estonia that is not reverse-charged to an Estonian taxable person, it must register from the date that supply arises.

### KMD line map (form valid from 1 July 2025, used for 2026)

The form numbers some lines with a superscript: 1¹ is "line 1 superscript 1", and likewise 1², 2¹, 2² and 4¹. These are sub-lines of lines 1, 2 and 4. They are not the same as lines 11, 12 and 13 (adjustment, VAT payable, overpaid). English PDF text copies often print them flattened, as "11" or "41", so read them from the form layout.

| Line ([KMD form](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf)) | What goes in it |
| --- | --- |
| 1 | Taxable value at 24%. Includes intra-Community acquisitions of goods, services received from foreign businesses not registered in Estonia, self-supply, and credit notes on 24% supplies |
| 1¹ | Credit notes and § 29¹ changes on transactions taxed at 20% |
| 1² | Credit notes and § 29¹ changes on transactions taxed at 22% |
| 2 | Taxable value at 9% |
| 2¹ | Taxable value at 5% (cash-accounting transition for press publications), plus credit notes and § 29¹ changes on transactions taxed at 5% |
| 2² | Taxable value at 13% |
| 3 | All zero-rated supply |
| 3.1 | Of which: intra-Community supply of goods, and general-rule services to taxable persons in other Member States |
| 3.1.1 | Of which: intra-Community supply of goods |
| 3.2 | Of which: exports of goods |
| 3.2.1 | Of which: tax-free sales to travellers |
| 4 | Total output VAT, calculated by the formula above |
| 4¹ | Import VAT, only for persons the ETCB has authorised to declare import VAT on the KMD |
| 5 | Total deductible input VAT |
| 5.1 | Of which: import VAT |
| 5.2 | Of which: VAT on fixed assets |
| 5.3 | Number of cars, and input VAT, for cars meeting the § 30(4) 3) to 5) conditions (full deduction). Cars bought to resell or to rent out are not shown here, though their VAT is deductible in line 5 |
| 5.4 | Number of cars, and input VAT, for cars used partly for business (at most 50% of input VAT) |
| 6 | Information: intra-Community acquisitions of goods and services from taxable persons of other Member States |
| 6.1 | Information: of which intra-Community acquisitions of goods |
| 7 | Information: other acquisitions on which you calculate VAT (non-EU suppliers not registered in Estonia, triangular acquisitions, goods to be installed, § 41¹ goods) |
| 7.1 | Information: of which § 41¹ acquisitions (immovables, scrap metal, precious metal and metal products) |
| 8 | Exempt supply |
| 9 | Supply under the § 41¹ special arrangements, and goods to be installed or assembled in another Member State |
| 10 / 11 | Adjustments up (10) or down (11); only one of the two is completed |
| 12 | VAT payable: line 4 + line 4¹ − line 5 + line 10 − line 11 |
| 13 | Overpaid VAT, by the same formula |

Source: [KMD form and instructions, valid from 01.07.2025](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf). Amounts are entered to the cent, in euro.

### Reverse charge on the KMD, in one place

- **Services from an EU business** (general-rule B2B services): taxable value in line 1 (or 2 or 2²), VAT in line 4; also line 6. Deduct in line 5 if the service is used for taxable supply.
- **Goods acquired from another Member State**: line 1 (or 2 or 2²) and line 6 and 6.1; deduct in line 5.
- **Services or goods from a non-EU business not registered in Estonia** on which you must calculate VAT: line 1 and line 7; deduct in line 5.
- **Domestic reverse charge under § 41¹** (immovables sold under the option to tax, scrap metal, precious metal and metal products): the buyer declares the acquisition in line 1 and lines 7 and 7.1; the seller declares the supply in line 9, not line 1. In the KMD INF annex the seller's invoice carries special code 02 in Part A and the buyer's carries special code 12 in Part B.
- **Triangular transactions**: an Estonian acquirer (C) declares in line 1 or 2 and lines 4 and 7; an Estonian middle reseller (B) declares only in column 4 of form VD, not on the KMD; an Estonian first seller (A) declares an intra-Community supply in lines 3, 3.1 and 3.1.1 and on the VD.

### Passenger cars

The restriction applies to category M1 (including M1G) vehicles with a gross weight not exceeding 3,500 kilograms and no more than eight seats besides the driver's. For those cars, and for fuel, repairs, parking and other goods and services bought for them, usually half of the input VAT is deductible, however much the car is used privately. Advertising placed on a car, and buying or renting a trailer, are not car costs.

Full deduction is allowed only in the § 30(4) exceptions: a car bought for resale or for renting out (and not used by the buyer itself); a car mainly used for paid passenger transport or driving lessons, with the required licences; or a car used exclusively for business, where private use is precluded and the business can show it (for example a logbook or GPS records, and parking at the premises outside working hours). Commuting by employees can fall outside private use if the Income Tax Act conditions are met. If the car is used privately even once, including with the employee reimbursing the cost, it is not exclusive business use. On the KMD, cars bought to resell or to rent out are deducted in full in line 5 but are not counted in line 5.3; line 5.3 is for the passenger-transport, driving-lesson and exclusive-business cars.

Where the business also makes exempt supply, the car percentage is applied on top of the partial-deduction proportion ([ETCB, Passenger cars and VAT accounting](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting)).

## Boundaries and exceptions

| Situation | Treatment ([ETCB filing guidance](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports)) | Watch for |
| --- | --- | --- |
| Sale of goods to a business in another Member State | 0%, lines 3, 3.1 and 3.1.1, and on form VD | Only if the buyer has a valid VAT number from another Member State and the supply is on the VD report. Otherwise charge Estonian VAT |
| B2B general-rule service to a business in another Member State | Outside Estonian VAT; line 3 and 3.1, and column 5 of form VD | Services tied to immovable property, and services zero-rated in the customer's state (such as export transport), go in line 3 only and not on the VD |
| Sale to a consumer in another Member State (goods shipped, or digital services) | Estonian VAT while EU-wide sales stay within the EUR 10,000 threshold and the seller is established only in Estonia; above it, the customer's state rate, usually through OSS | OSS supplies go on the OSS return, not on the KMD |
| Export of goods outside the EU | 0%, lines 3 and 3.2 | Keep export evidence |
| Tax-free sale to a traveller | 0%, lines 3, 3.2 and 3.2.1 | |
| Exempt supply (for example insurance, most financial services, certain property transactions) | Line 8; related input VAT is not deductible | The option to tax some exempt supplies needs written notice to the ETCB before the supply |
| Wages, social tax, income tax, loans, dividends, own transfers, tax payments | Not supply: leave off the KMD | |
| Supply to or from a VAT group member | The group files one KMD; each member files its own KMD INF annex | |
| Mistakenly charged VAT on an invoice by an unregistered person | The VAT shown is payable; the person files a KMD | |
| Goods moved to another Member State as call-off stock | Not on the KMD; declared on form VD in the call-off block, and on VDP if returned or the acquirer changes within 12 months | |
| Invoice with mixed rates, zero-rated or exempt lines | KMD INF special code 03 | |
| Supply under the § 41 or § 42 margin schemes | KMD INF special code 01 | Margin schemes are out of scope here |

Sources: [Filing VAT returns and reports](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports); [KMD INF form from 01.07.2025](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_inf_2025_07_eng.pdf); [rates handbook](https://www.emta.ee/en/node/336/main_chapter/83171/pdf); [VAT rates and exempt supply](https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate).

### Classifying a bank statement

When working from a bank export, classify by what the invoice shows, not by the brand name on the statement:

- **Look at the billing entity and its country on the invoice.** A foreign brand may bill from an EU subsidiary (EU reverse charge, line 6) or from outside the EU (line 7). If there is no invoice, ask for it before claiming any input VAT.
- **Bank fees, interest, loan principal and insurance premiums** are exempt or outside VAT: no input VAT.
- **Salaries, social tax, income tax and payments to the ETCB** are not purchases: leave them out.
- **Owner transfers, dividends and transfers between own accounts** are out of scope.
- **Cash withdrawals**: ask what they paid for; exclude until supported by an invoice.
- **Restaurant and entertainment costs**: the ETCB pages do not list a specific block, but input VAT is deductible only for goods and services used for taxable business supply. Default to no deduction until the business purpose is confirmed.
- **Domestic purchases at 24% with a valid Estonian invoice**: deductible in line 5 if used for taxable supply.

Conservative defaults when facts are missing: an unknown sale rate is 24%; an EU customer with no confirmed valid VAT number is treated as a consumer and charged Estonian VAT; a purchase with no compliant invoice is not deductible; a car of unknown use is at 50%.

## Worked cases

### Case 1: domestic sale and a US software subscription, March 2026 ([KMD form](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf))

An Estonian OÜ, fully taxable, sells consulting in Estonia for EUR 1,000 net and buys a EUR 100 software subscription from a US company not registered in Estonia.

- Line 1: EUR 1,000 + EUR 100 = EUR 1,100.
- Line 4: 24% of EUR 1,100 = EUR 264 (EUR 240 on the sale and EUR 24 self-assessed on the subscription).
- Line 7: EUR 100 (information).
- Line 5: EUR 24 deductible, because the software is used for taxable supply.
- Line 12: EUR 264 − EUR 24 = EUR 240 payable by 20 April 2026.
- KMD INF: the sale goes in Part A if that customer's invoices in March total at least EUR 1,000 without VAT, which they do. The US supplier has no Estonian register code, and the KMD INF instructions say invoices of non-resident partners without one are not declared, so it is not listed in Part B.

### Case 2: company car fuel ([ETCB example](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting))

Fuel costs EUR 50 plus EUR 12 VAT. The company's supply is 60% taxable and 40% exempt.

- Car also used privately: deductible input VAT = EUR 12 × 50% × 60% = EUR 3.6, shown in line 5 and line 5.4.
- Car used exclusively for business (private use precluded and recorded): EUR 12 × 60% = EUR 7.2, shown in line 5 and line 5.3.

Source: [ETCB, Passenger cars and VAT accounting](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting).

### Case 3: crossing the registration threshold ([ETCB handbook](https://www.emta.ee/en/node/333/handbook/4/pdf))

A sole trader's Estonian supply since 1 January passes EUR 40,000 on Friday the 2nd of a month.

- The application is due within three working days: by Wednesday the 7th.
- The ETCB registers the person from the 2nd, the day the threshold was exceeded, and must decide within five working days of the application.
- VAT is due on supply from the 2nd even before the VAT number arrives; compliant invoices are issued later, within 7 days as the ETCB example notes, and non-compliant ones corrected.

Source: [ETCB registration handbook](https://www.emta.ee/en/node/333/handbook/4/pdf).

### Case 4: KMD INF annex, several small invoices ([ETCB filing guidance](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports))

In May 2026 a company issues two invoices at 24% to the same Estonian business customer: EUR 600 and EUR 500 without VAT.

- Total per partner = EUR 1,100, which is at least EUR 1,000, so both invoices go in Part A.
- A third customer with a single EUR 900 invoice is below the limit and need not be listed (the Act allows listing invoices below the limit).
- Invoices to private individuals are not declared.

### Case 5: late payment interest ([ETCB interest](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests))

EUR 5,000 of VAT for June 2026, due 20 July 2026, is paid 10 days late.

- Interest = EUR 5,000 × 10 × 0.06% = EUR 30.
- Interest is rounded to the nearest euro, and the ETCB issues no interest claim below EUR 10.

Source: [ETCB, Payment of interests](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests).

### Case 6: EU B2B service and an Irish advertising invoice ([KMD form](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf))

A company invoices EUR 3,500 of consulting to a German business with a valid German VAT number, and receives an invoice for EUR 850 of advertising from an Irish company.

- Sale: line 3 and 3.1 with EUR 3,500; also column 5 of form VD, both due by the 20th of the following month.
- Purchase: line 1 and line 6 with EUR 850; line 4 includes 24% of it, EUR 204; line 5 deducts EUR 204 if used for taxable supply. The Irish supplier has no Estonian register code, so its invoice is not declared in KMD INF Part B.

## When to refuse or refer

- **E-resident company with no staff, office or permanent establishment in Estonia.** Whether its services are supplied from Estonia, and whether it is an Estonian taxable person for a given transaction, depends on where it really does business. Refer to a specialist before filing.
- **Partial exemption.** A business with both taxable and exempt supply must deduct input VAT proportionally and recalculate in the last period of the year (§ 32). Refer the year-end recalculation.
- **Margin schemes** (second-hand goods, art, antiques, travel services): out of scope.
- **§ 41¹ special arrangements** for immovables and metals where the client is unsure whether the arrangement applies.
- **VAT groups**: joint return, separate annexes, joint liability.
- **Import VAT on the KMD (line 4¹)**: only with an ETCB authorisation.
- **Bad-debt relief where the claim includes more than EUR 30,000 of VAT**: needs a court judgment in force.
- **OSS or IOSS returns**: this Guide covers only when they apply and their deadlines.
- **Any period before 2025** other than the credit-note lines: check the form version valid for that period.

## Filing and payment

**Deadline.** The KMD and the KMD INF annex are filed, and the VAT is payable, by the 20th day of the month after the taxable period. The VD report has the same deadline. If no reportable intra-Community supply was made, no VD is filed.

**How.** In e-MTA (manual entry, or XML or CSV upload; a re-upload overwrites all earlier data in every part), or by machine-to-machine interface over X-tee from accounting software. Paper filing at a service bureau is allowed only if the person has been registered for less than 12 months, or the annex has fewer than five invoices. A return shows "Submitted" once accepted; "Not submitted" means errors to fix.

**Payment.** Pay to the ETCB prepayment account. Interest runs at 0.06% a day from the day after the due date until payment. Instalment schedules can be applied for in e-MTA.

**Refunds.** An overpayment (line 13) stays on the prepayment account unless you apply for a refund, or for a transfer to another person's prepayment account.

**Corrections.**
- KMD and KMD INF: amend the return for the original period in e-MTA, by re-uploading a corrected file or editing online. Remember that an uploaded file replaces all previous data for that part.
- Credit notes: declare in the period the credit note is issued, at the rate of the original invoice (so a credit note on a 22% invoice goes to line 1², and one on a 20% invoice to line 1¹). Show them in the VD for that period too, if the original was on a VD.
- VD: corrections and late call-off stock entries go on form VDP.
- OSS and IOSS: correct a previous return in a later return, not by amending the original.
- Mismatches between your KMD INF and your trading partners' annexes can affect your tax behaviour rating and send your return for review; resolve them with the partner first.

**Bad-debt relief (§ 29¹).** A seller can reduce output VAT on an unpaid invoice if all conditions are met: a compliant invoice was issued and its VAT declared in the right period; the claim was not assigned; at least 12 months and no more than three years have passed since the payment due date (the ETCB notes an exception, "except in case described in clause 6"; check § 29¹ of the Act if it may apply); the claim is written off in the accounts after all feasible collection efforts (or collection would cost more than the claim); a court judgment in force if the claim includes more than EUR 30,000 of VAT; the buyer is not an associated person; and the buyer is told in writing in the month of write-off. The reduction goes in the line for the original invoice's rate, which reduces line 4: line 1 for 24%, 1² for 22%, 1¹ for 20%, 2 for 9%, 2² for 13%, 2¹ for 5%. Relief needs 12 months to pass, so most 2026 claims concern invoices from before July 2025 at 22% and go in line 1²; the buyer reduces its input VAT in line 5; both show the invoice again with minus figures in KMD INF. If the debt is later paid, VAT is declared again.

**Penalties.** The KMD carries a declaration that incorrect or inaccurate information is punishable under the Taxation Act. Late payment always attracts interest. The ETCB's English pages checked for this Guide do not give a fine schedule for late filing; check the Taxation Act before quoting a figure.

**From 2027.** The ETCB announced that businesses will be able to submit the source data for the VAT calculation in a standardised xbrl_GL format over X-tee instead of the form-based return; other methods remain.

## Returns for 2025 periods (late filings and amendments)

- **January to June 2025**: standard rate 22%, on the KMD form valid from 1 January 2025 to 30 June 2025. Accommodation was already 13% and press publications 9% from 1 January 2025.
- **July to December 2025**: standard rate 24%, on the form valid from 1 July 2025.
- **Straddling supplies.** The rate follows the time of supply. The ETCB's examples: a June 2025 prepayment, paid in June, for goods delivered in July is taxed at 22%; a partial June advance is at 22% and the rest, delivered and paid in August, at 24%; a service from 1 June to 31 July 2025 invoiced in one amount with no prepayment is supplied in July and taxed wholly at 24%; separate monthly invoices split 22% and 24%; goods sold at 22% in May and returned in July are credited at 22%; an invoice issued in June alone creates no supply, so delivery and payment in July means 24% and the invoice must show 24%.
- **Old 20% contracts.** A written contract concluded before 1 May 2023 with a fixed 20% rate and no right to raise the price could keep 20% only until 30 June 2025 (shortened from 31 December 2025).

Source: [ETCB, Changes in the Estonian Value Added Tax Act](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax).

## Completion checklist

- [ ] VAT registration and effective date confirmed; limited-liability status checked.
- [ ] Period is the calendar month; every supply dated by time of supply.
- [ ] Sales split into lines 1, 2, 2², 3 (with 3.1, 3.1.1, 3.2, 3.2.1), 8 and 9.
- [ ] EU customer VAT numbers checked before using 0%; VD report prepared.
- [ ] Reverse-charge purchases in line 1 (or 2 or 2²) and information lines 6, 6.1, 7, 7.1.
- [ ] Input VAT in line 5 only with a compliant invoice (or import document) and a taxable-business use; sub-lines 5.1, 5.2, 5.3 and 5.4 filled.
- [ ] Cars: 50% unless an exception is documented; car count entered in 5.3 or 5.4.
- [ ] Partial deduction applied if any exempt supply; year-end recalculation in line 10 or 11.
- [ ] Credit notes at the original rate (lines 1¹ and 1² for old 20% and 22% invoices; line 2¹ for 5%).
- [ ] KMD INF Parts A and B complete for every partner at or above EUR 1,000; special codes used (Part A: 01, 02, 03; Part B: 11 for partial deduction under § 32 or § 29(4), 12 for § 41¹ acquisitions); partner registry codes entered.
- [ ] OSS or IOSS supplies kept off the KMD.
- [ ] Line 12 or 13 reconciled to the ledger; refund application made if wanted.
- [ ] Filed and paid by the 20th of the following month.

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
