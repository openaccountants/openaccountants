---
name: estonia-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Estonian VAT return (KMD form) for any client. Trigger on phrases like "prepare VAT return", "do the KMD", "fill in KMD", "Estonian VAT", "kaibemaks", or any request involving Estonia VAT filing. This skill covers Estonia only and standard KM registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Estonian VAT work.
version: 2.1
jurisdiction: EE
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: filing-howto
domain: vat-gst
---

# Estonia VAT return (KMD and KMD INF)

## Scope

This skill covers the monthly Estonian VAT return, form KMD, and its annex, form KMD INF, for a person registered as liable to VAT in Estonia (a company such as an OÜ or AS, or a sole proprietor, FIE). It covers the rates in force for 2026 periods, the registration threshold, the monthly deadline and payment, domestic and cross-border reverse charge, the report on intra-Community supply (form VD), the OSS and IOSS special schemes at a summary level, corrections, bad-debt relief, and interest on late payment.

The primary year is 2026. This skill applies the ordinary calendar-month period. Ask whether EMTA has approved a longer period; if so, use the actual approval and refer its period-specific requirements rather than applying the monthly defaults. A short dated section near the end covers 2025 periods, which straddle the 1 July 2025 rate change.

All figures come from the Estonian Tax and Customs Board (Maksu- ja Tolliamet, ETCB) at emta.ee. The ETCB publishes English translations of the forms "for your information only"; the Estonian original is the form that is filed ([KMD forms page](https://www.emta.ee/en/business-client/taxes-and-payment/tax-returns-exchange-information/vat-return-forms-vd-and-vdp)).

Out of scope: VAT groups beyond a mention, the margin schemes for second-hand goods and travel services, partial exemption calculations, import VAT deferment authorisations, and the special-case VAT return for unregistered persons.

## Ask the client first

- **Are you registered as liable to VAT in Estonia, and from what date?** Get the VAT number. Registration takes effect from the day the threshold was exceeded, not the day the ETCB decides.
- **Are you a full taxable person, or a taxable person with limited liability?** Limited-liability persons file KMD but do not file the KMD INF annex.
- **Which month is being filed, and has EMTA approved a longer taxation period?** Obtain any approval before applying these ordinary monthly instructions. The rate depends on the time of supply, so the period matters.
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
2. **Fix the taxable period.** Use one calendar month for an ordinary monthly filer; an approved longer period must follow its actual ruling. Put each supply in the month in which it arose (time of supply), which also fixes the rate.
3. **Sort every sale by rate and box.** Standard rate to line 1, the 13% rate to line 2², the 9% rate to line 2, zero-rated supply to line 3 and its sub-lines, exempt supply to line 8, and supply under the special arrangements of § 41¹ of the VAT Act to line 9.
4. **Self-assess reverse-charge purchases.** Services from foreign suppliers not registered in Estonia, and intra-Community acquisitions of goods, go into line 1 (or line 2 or 2² at a reduced rate) so that output VAT is calculated in line 4. Also show them in the information lines 6, 6.1, 7 and 7.1.
5. **Compute output VAT in line 4.** The form's formula is 24% of line 1 + 20% of line 1¹ + 22% of line 1² + 9% of line 2 + 5% of line 2¹ + 13% of line 2².
6. **Collect deductible input VAT in line 5.** Include reverse-charge VAT you are entitled to deduct. Show import VAT (5.1), fixed assets (5.2) and passenger cars (5.3 or 5.4) as sub-lines of line 5.
7. **Apply restrictions.** Passenger cars: usually half. Mixed taxable and exempt activity: partial deduction. Private use: none.
8. **Adjustments.** Year-end recalculation of partial deduction, fixed-asset adjustments and car-use changes go in line 10 (increase) or line 11 (decrease), never both.
9. **Read the result.** Line 12 is VAT payable and line 13 is overpaid VAT. A refund needs a separate application for a refund from the prepayment account.
10. **Build the KMD INF annex.** Part A lists sales invoices and Part B purchase invoices, where the relevant total per transaction partner without VAT is at least EUR 1,000 in the period. Test issued and received invoices separately, and test ordinary invoices and credit invoices separately. If either ordinary-invoice or credit-invoice total reaches the limit, include all reportable invoices for that partner in that direction, including the credit notes. Apply the form's exceptions for private customers, non-residents without an Estonian register code, professional secrecy, travel-scheme-only invoices and non-deductible purchases.
11. **File the VD report** for reportable intra-Community goods or general-rule services to businesses in other EU countries. Exclude services exempt in the recipient state, including the small-business scheme; apply the specific line 3.1/VD exceptions below.
12. **File and pay by the 20th** of the following month through e-MTA or X-tee.

## Figures with years

### Rates for 2026 periods

| Rate ([ETCB rates](https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate)) | Applies to | In force | KMD line | Official source |
| --- | --- | --- | --- |---|
| 24% | Standard rate: everything without a specific reduced rate or exemption | From 1 July 2025 (22% from 1 January 2024 to 30 June 2025) | 1 | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate |
| 13% | Accommodation, and accommodation with breakfast; not other services sold with it | From 1 January 2025 (previously 9%) | 2² | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-13-vat-rate |
| 9% | Books and educational literature (printed or electronic); listed medicines, contraceptives and medical devices for personal use of disabled persons; press publications (printed or electronic, not mainly advertising, erotic, or video or music content) | Press publications back at 9% from 1 January 2025 (5% from 1 August 2022 to 31 December 2024) | 2 | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-9-vat-rate |
| 0% | Exports; intra-Community supply of goods to a buyer with a valid EU VAT number, shown on the VD report; listed transport and ship/aircraft supplies | Standing | 3, 3.1, 3.1.1, 3.2, 3.2.1 | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-0-vat-rate-goods |
| 5% | Only for cash-accounting users: press publications invoiced and supplied before 1 January 2025, where supply arises later; allowed until 31 December 2026 | Transitional | 2¹ | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-9-vat-rate |
| 9% on accommodation | Only for cash-accounting users: accommodation invoiced and provided before 1 January 2025; allowed until 31 December 2026 (a right, not an obligation) | Transitional | 2 | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-13-vat-rate |
| 22% and 20% | Only for credit notes on invoices originally taxed at those rates | Historic | 1² (22%), 1¹ (20%) | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |

Sources: [standard rate](https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate); [rates handbook](https://www.emta.ee/en/node/336/main_chapter/83171/pdf); [VAT Act changes](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax); [KMD form from 01.07.2025](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf).

The ETCB says the correct rate "must be chosen on the basis of the time of supply". Software, games and web publications that are mainly advertising stay at 24%.

### Thresholds and dates

| Item | Figure | Source | Official source |
| --- | --- | --- |---|
| Registration threshold | Supply with place of supply in Estonia exceeding EUR 40,000 from the start of the calendar year | [Registration handbook](https://www.emta.ee/en/node/333/handbook/4/pdf) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer |
| Time to apply after crossing it | Three working days; the ETCB then has five working days to decide | Registration handbook | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer |
| Limited-liability registration | Intra-Community acquisitions of goods exceeding EUR 10,000 from the start of the year | [Registration page](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer |
| EU small-business scheme (foreign small enterprises) | Voluntary; EU-wide annual turnover must not exceed EUR 100,000 in either the current or previous calendar year. Exactly EUR 100,000 does not itself breach the EU-wide ceiling. National eligibility, prior notification and activated EX identification remain separate conditions; this headline alone does not establish eligibility | Directive Articles 284(2)-(5), 288a(2), 14 April 2025 consolidation; dedicated SME chapter | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-vat-provisions/special-scheme-small-businesses |
| OSS distance-sales and digital-services threshold | EUR 10,000 across all other Member States together | [Special schemes page](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services |
| KMD INF annex | Invoices totalling at least EUR 1,000 without VAT per transaction partner in the period | [Filing page](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| KMD, KMD INF and VD deadline | 20th day of the month after the period; VAT is also payable by then | Filing page; KMD form | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| OSS return | Quarterly, by the last day of the month after the quarter | Special schemes page | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services |
| IOSS return | Monthly, by the last day of the following month | Special schemes page | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services |
| Interest on late tax | 0.06% a day (21.9% a year) | [Payment of interests](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests) | https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests |
| Passenger-car input VAT | Usually 50% deductible | [Passenger cars and VAT](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting |
| Bad-debt relief with more than EUR 30,000 of VAT in the claim | Claim must be confirmed by a court judgment in force | [VAT Act changes](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/reduction-tax-liability-case-irrecoverable-arrears |

### What counts toward the EUR 40,000 (from 1 January 2025)

- Taxable supply of goods and services, including zero-rated supply, but not transfers of fixed assets.
- Real-estate transactions (sales, leases, rentals) under § 16(2) clauses 2, 3 and 6, except fixed-asset transfers and occasional transactions.
- Insurance and financial services, except occasional services.
- Only supply whose place of supply is Estonia. If all of a person's supply is exempt or zero-rated (and none is an intra-Community supply of goods), there is no registration obligation however large it is.
- Under a margin scheme, the full amount received counts, not the margin.

A foreign business with no permanent establishment in Estonia ordinarily has no registration threshold for Estonian taxable supply not reverse-charged to an Estonian taxable person. First check whether an eligible EU-established small enterprise has validly activated the cross-border SME exemption: obtain its prior-notification/EX identification and activation confirmation, and refer the complete scheme eligibility check rather than directing a qualifying exempt supplier to register. Without a valid applicable exemption, registration arises from the first such taxable supply. The EU-wide EUR 100,000 ceiling does not replace the separate Estonian threshold or scheme conditions.

### KMD line map (form valid from 1 July 2025, used for 2026)

The form numbers some lines with a superscript: 1¹ is "line 1 superscript 1", and likewise 1², 2¹, 2² and 4¹. These are sub-lines of lines 1, 2 and 4. They are not the same as lines 11, 12 and 13 (adjustment, VAT payable, overpaid). English PDF text copies often print them flattened, as "11" or "41", so read them from the form layout.

| Line ([KMD form](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf)) | What goes in it | Official source |
| --- | --- |---|
| 1 | Taxable value at 24%. Includes intra-Community acquisitions of goods, services received from foreign businesses not registered in Estonia, self-supply, and credit notes on 24% supplies | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 1¹ | Credit notes and § 29¹ changes on transactions taxed at 20% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 1² | Credit notes and § 29¹ changes on transactions taxed at 22% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 2 | Taxable value at 9% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 2¹ | Taxable value at 5% (cash-accounting transition for press publications), plus credit notes and § 29¹ changes on transactions taxed at 5% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 2² | Taxable value at 13% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 3 | Zero-rated supply under VAT Act § 15(3)-(4), except intra-Community supply performed by a customs agency for another person under § 17(2^1), which that agency reports on VD only | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 3.1 | Of which: intra-Community supply of goods, and general-rule services to taxable persons in other Member States, except recipient-state zero-rated services and services exempt under the small-business scheme | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 3.1.1 | Of which: intra-Community supply of goods | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 3.2 | Of which: exports of goods | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 3.2.1 | Of which: tax-free sales to travellers | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 4 | Total output VAT, calculated by the formula above | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 4¹ | Import VAT, only for persons the ETCB has authorised to declare import VAT on the KMD | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 5 | Total deductible input VAT | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 5.1 | Of which: import VAT | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 5.2 | Of which: VAT on fixed assets | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 5.3 | Number of cars, and input VAT, for cars meeting the § 30(4) 3) to 5) conditions (full deduction). Cars bought to resell or to rent out are not shown here, though their VAT is deductible in line 5 | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 5.4 | Number of cars, and input VAT, for cars used partly for business (at most 50% of input VAT) | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 6 | Information: intra-Community acquisitions of goods and services from taxable persons of other Member States | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 6.1 | Information: of which intra-Community acquisitions of goods | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 7 | Information: other acquisitions on which you calculate VAT (non-EU suppliers not registered in Estonia, triangular acquisitions, goods to be installed, § 41¹ goods) | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 7.1 | Information: of which § 41¹ acquisitions (immovables, scrap metal, precious metal and metal products) | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 8 | Exempt supply | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 9 | Supply under the § 41¹ special arrangements, and goods to be installed or assembled in another Member State | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 10 / 11 | Adjustments up (10) or down (11); only one of the two is completed | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 12 | VAT payable: line 4 + line 4¹ − line 5 + line 10 − line 11 | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |
| 13 | Overpaid VAT, by the same formula | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf |

Source: [KMD form and instructions, valid from 01.07.2025](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf). Amounts are entered to the cent, in euro.

### Reverse charge on the KMD, in one place

- **Services from an EU business** (general-rule B2B services): taxable value in line 1 (or 2 or 2²), VAT in line 4; also line 6. Deduct in line 5 if the service is used for taxable supply.
- **Goods acquired from another Member State**: line 1 (or 2 or 2²) and line 6 and 6.1; deduct in line 5.
- **Services or goods from a non-EU business not registered in Estonia** on which you must calculate VAT: line 1 and line 7; deduct in line 5.
- **Domestic reverse charge under § 41¹** (immovables sold under the option to tax, scrap metal, precious metal and metal products): the buyer declares the acquisition in line 1 and lines 7 and 7.1; the seller declares the supply in line 9, not line 1. In the KMD INF annex the seller's invoice carries special code 02 in Part A and the buyer's carries special code 12 in Part B.
- **Triangular transactions**: an Estonian acquirer (C) declares in line 1 or 2 and lines 4 and 7; an Estonian middle reseller (B) declares only in column 4 of form VD, not on the KMD; an Estonian first seller (A) declares an intra-Community supply in lines 3, 3.1 and 3.1.1 and on the VD.

### Passenger cars

The restriction applies to category M1 (including M1G) vehicles with a gross weight not exceeding 3,500 kilograms and no more than eight seats besides the driver's. For those cars, and for fuel, repairs, parking and other goods and services bought for them, usually half of the input VAT is deductible, however much the car is used privately. Advertising placed on a car, and buying or renting a trailer, are not car costs.

Full deduction is allowed only in the § 30(4) exceptions: a car bought for resale or for renting out (and not used by the buyer itself); a car mainly used for paid passenger transport or driving lessons, with the required licences; or a car used exclusively for business, where private use is precluded and the business can show it (for example a logbook or GPS records, and parking at the premises outside working hours). Commuting by employees can fall outside private use if the Income Tax Act conditions are met. Under the exclusive-business exception, if the car is used privately even once, including with the employee reimbursing the cost, it is not exclusive business use. The separate qualifying passenger-transport and driving-school exceptions can allow full deduction with private use taxed as self-supply; do not apply the exclusive-business test indiscriminately to those exceptions. On the KMD, cars bought to resell or to rent out are deducted in full in line 5 but are not counted in line 5.3; line 5.3 is for the passenger-transport, driving-lesson and exclusive-business cars.

If a car bought as exclusively business-use with full acquisition VAT deducted first becomes privately used within two years of acquisition, amend the acquisition-period return to reduce the acquisition deduction: it is treated as partly business-use throughout those first two years. Running-cost VAT is not retrospectively reduced by that acquisition rule. From the month private use first starts, the running-cost deduction is capped at 50% for the following 12 months even if private trips stop sooner; exempt or non-business activity can reduce it further. Lease payments are running costs. For a qualifying taxi/driving-school car that leaves its exception within that period, account for self-supply VAT already paid when making the adjustment. Do not import the authority page's historical divisor of 1.2 into a 2026 self-supply calculation; its current 24% treatment requires the applicable law/rate and is held below. [EMTA passenger-car chapter, acquisition and running-cost adjustments](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting).

Where the business also makes exempt supply, the car percentage is applied on top of the partial-deduction proportion ([ETCB, Passenger cars and VAT accounting](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting)).

## Boundaries and exceptions

| Situation | Treatment ([ETCB filing guidance](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports)) | Watch for | Official source |
| --- | --- | --- |---|
| Sale of goods to a business in another Member State | 0%, lines 3, 3.1 and 3.1.1, and on form VD | Only if the buyer has the required valid VAT number from another Member State, transport evidence is held and the supply is correctly reported on VD. If the exemption conditions fail, classify the transaction under the applicable place-of-supply and destination rules; do not automatically assume Estonian VAT | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports/when-declare https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-0-vat-rate-goods |
| B2B general-rule service to a business in another Member State | Outside Estonian VAT; line 3 and 3.1, and column 5 of form VD | Services tied to immovable property, services zero-rated in the customer's state (such as export transport), and services exempt under the small-business scheme are excluded from line 3.1 and VD; determine the applicable line 3 treatment from the actual supply and scheme | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports/when-declare |
| Sale to a consumer in another Member State (goods shipped, or digital services) | For eligible intra-Community distance sales dispatched from Estonia and telecommunications, broadcasting or electronic services, origin-country VAT applies only if the seller is established only in Estonia and the combined qualifying EU-wide value excluding VAT does not exceed EUR 10,000 in either the current or preceding calendar year, unless a destination-place option or active OSS applies. The destination-place option binds for at least two calendar years; active OSS does not reset to origin VAT at the start of a year. When the threshold is exceeded, destination treatment starts immediately; OSS is one reporting route | OSS supplies go on the OSS return, not on the KMD. Other consumer services do not automatically qualify for this EUR 10,000 derogation | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 |
| Export of goods outside the EU | 0%, lines 3 and 3.2 | Keep export evidence | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-0-vat-rate-goods |
| Tax-free sale to a traveller | 0%, lines 3, 3.2 and 3.2.1 | | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-0-vat-rate-goods |
| Exempt supply (for example insurance, most financial services, certain property transactions) | Line 8; related input VAT is not deductible | The option to tax some exempt supplies needs written notice to the ETCB before the supply | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| Wages, social tax, income tax, loans, dividends, own transfers, tax payments | Not supply: leave off the KMD | | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| Supply to or from a VAT group member | The group files one KMD; each member files its own KMD INF annex | | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| Mistakenly charged VAT on an invoice by an unregistered person | The VAT shown is payable; the person files a KMD | | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| Goods moved to another Member State as call-off stock | Not on the KMD; declared on form VD in the call-off block, and on VDP if returned or the acquirer changes within 12 months | | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports/when-declare |
| Invoice with mixed rates, zero-rated or exempt lines | KMD INF special code 03 | | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_inf_2025_07_eng.pdf |
| Supply under the § 41 or § 42 margin schemes | KMD INF special code 01 | Margin schemes are out of scope here | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_inf_2025_07_eng.pdf |

Sources: [Filing VAT returns and reports](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports); [KMD INF form from 01.07.2025](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_inf_2025_07_eng.pdf); [rates handbook](https://www.emta.ee/en/node/336/main_chapter/83171/pdf); [VAT rates and exempt supply](https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate).

### Classifying a bank statement

When working from a bank export, classify by what the invoice shows, not by the brand name on the statement:

- **Look at the billing entity and its country on the invoice.** A foreign brand may bill from an EU subsidiary (EU reverse charge, line 6) or from outside the EU (line 7). If there is no invoice, ask for it before claiming any input VAT.
- **Bank fees, interest, loan principal and insurance premiums** are exempt or outside VAT: no input VAT.
- **Salaries, social tax, income tax and payments to the ETCB** are not purchases: leave them out.
- **Owner transfers, dividends and transfers between own accounts** are out of scope.
- **Cash withdrawals**: ask what they paid for; exclude until supported by an invoice.
- **Guest entertainment, employee meals and employee accommodation**: input VAT is blocked by VAT Act § 30(1)-(2), except employee accommodation on a business trip. A business purpose alone does not remove the block. Where goods were bought for taxable business use and later diverted to staff or guests, apply the self-supply treatment described by EMTA. Separate ordinary restaurant trading purchases from guest or employee consumption.
- **Domestic purchases at 24% with a valid Estonian invoice**: deductible in line 5 if used for taxable supply.

When facts are missing, stop the affected classification: establish the place of supply, customer status and any reduced rate or exemption before choosing a rate. For ordinary services, a missing customer VAT number does not by itself conclusively establish consumer status. Council Implementing Regulation (EU) 282/2011 Articles 17-20 distinguish business status, private-use capacity and location. Article 18(1)(b) permits the pending-number case with proof of application, other business evidence and reasonable commercial checks. The ordinary no-number presumption in Article 18(2) is qualified by contrary information; its second paragraph has a separate rule for the listed telecommunications, broadcasting, electronic and virtual-event services. Under Article 19, exclusively private use is non-business even for a taxable customer, while a mixed private/business service follows Article 44 absent abuse. Verify the actual applicable service/place rule rather than assigning a VAT rate from a number alone. For ordinary intra-Community goods, do not claim 0% without the required VAT-number and transport/reporting evidence. New means of transport and excise goods have separate exceptions: refer those cases rather than apply the ordinary VAT-number test indiscriminately. A purchase with no compliant invoice is not deductible. For a car, confirm taxable business use before applying the usual 50% restriction; a wholly private car has no deductible business input VAT.

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

- The application is due within three working days: by Wednesday the 7th, assuming the intervening weekdays are working days and no public holiday changes the count.
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

### Recomputing checks for Cases 1 and 2

```oa-check
name: Estonia KMD domestic sale and US software 2026, existing Case 1
inputs:
  sale: 1000
  software: 100
  vat_rate: 0.24
steps:
  - line1: sale + software
  - line4: line1 * vat_rate
  - line7: software
  - line5: software * vat_rate
  - line12: line4 - line5
expected:
  line1: 1100
  line4: 264
  line7: 100
  line5: 24
  line12: 240
```

```oa-check
name: Estonia car mixed taxable activity 2026, existing Case 2
inputs:
  input_vat: 12
  taxable_share: 0.60
steps:
  - mixed_use_deduction: input_vat * 0.50 * taxable_share
  - exclusive_business_deduction: input_vat * taxable_share
expected:
  mixed_use_deduction: 3.60
  exclusive_business_deduction: 7.20
```

## When to refuse or refer

- **E-resident company with no staff, office or permanent establishment in Estonia.** Whether its services are supplied from Estonia, and whether it is an Estonian taxable person for a given transaction, depends on where it really does business. Refer to a specialist before filing.
- **Partial exemption.** A business with both taxable and exempt supply must deduct input VAT proportionally and recalculate in the last period of the year (§ 32). Refer the year-end recalculation.
- **Margin schemes** (second-hand goods, art, antiques, travel services): out of scope.
- **§ 41¹ special arrangements** for immovables and metals where the client is unsure whether the arrangement applies.
- **VAT groups**: joint return, separate annexes, joint liability.
- **Import VAT on the KMD (line 4¹)**: only with an ETCB authorisation.
- **Bad-debt relief where the claim includes more than EUR 30,000 of VAT**: needs a court judgment in force.
- **OSS or IOSS returns**: this skill covers only when they apply and their deadlines.
- **Any period before 2025** other than the credit-note lines: check the form version valid for that period.

## Filing and payment

**Deadline.** The KMD and the KMD INF annex are filed, and the VAT is payable, by the 20th day of the month after the taxable period. The VD report has the same deadline. If no reportable intra-Community supply was made, no VD is filed.

**How.** In e-MTA choose Taxes, then Value added tax, then Submit and view KMD, and Add a new tax return (Lisa uus deklaratsioon). Enter the data manually, or use Add data from file for UTF-8 XML/CSV. Uploading alone does not submit the return: after processing, click Submit a VAT return, then check Submitted and the Errors column. Correct errors and resubmit. In e-MTA (manual entry, or XML or CSV upload; a re-upload overwrites all earlier data in every part), or by machine-to-machine interface over X-tee from accounting software. Paper filing at a service bureau is allowed only if the person has been registered for less than 12 months, or the annex has fewer than five invoices. A return shows "Submitted" once accepted; "Not submitted" means errors to fix.

**Payment.** Pay to the ETCB prepayment account. Interest runs at 0.06% a day from the day after the due date until payment. Instalment schedules can be applied for in e-MTA.

**Refunds.** An overpayment (line 13) stays on the prepayment account unless you apply for a refund, or for a transfer to another person's prepayment account.

**Corrections.**
- KMD and KMD INF: amend the return for the original period in e-MTA, by re-uploading a corrected file or editing online. Remember that an uploaded file replaces all previous data for that part.
- Credit notes: declare in the period the credit note is issued, at the rate of the original invoice (so a credit note on a 22% invoice goes to line 1², and one on a 20% invoice to line 1¹). Show them in the VD for that period too, if the original was on a VD.
- VD: corrections and late call-off stock entries go on form VDP.
- OSS and IOSS: correct a previous return in a later return, not by amending the original.
- Mismatches between your KMD INF and your trading partners' annexes can affect your tax behaviour rating and send your return for review; resolve them with the partner first.

**Bad-debt relief (§ 29¹).** A seller can reduce output VAT on an unpaid invoice if all conditions are met: a compliant invoice was issued and its VAT declared in the right period; the claim was not assigned; at least 12 months and no more than three years have passed since the payment due date (the ETCB notes an exception, "except in case described in clause 6"; check § 29¹ of the Act if it may apply); the claim is written off in the accounts after all feasible collection efforts (or collection would cost more than the claim); a court judgment in force if the claim includes more than EUR 30,000 of VAT; the buyer is not an associated person; and the buyer is told in writing in the month of write-off. The reduction goes in the line for the original invoice's rate, which reduces line 4: line 1 for 24%, 1² for 22%, 1¹ for 20%, 2 for 9%, 2² for 13%, 2¹ for 5%. For the ordinary 12-month rule, determine the original invoice's actual rate and due date. A 2026 write-off may concern either a 22% or a 24% invoice; do not infer the rate from the write-off year. The timing exception for a court-certified claim is on the Not yet confirmed line; the buyer reduces its input VAT in line 5; both show the invoice again with minus figures in KMD INF only where it is reportable in that period. Treat each unpaid invoice as a separate claim for the EUR 30,000 court test unless invoices have already been taken to court together as one claim. Do not waive the written buyer notification because the buyer is being liquidated or is difficult to contact. If the debt is later paid, VAT is declared again in the period of payment, to the extent paid. Do not issue a credit note solely because a debt is written off. The seller's VAT reduction is in the write-off period; the buyer reduces input VAT in the period it receives the written notification.

**Penalties.** The KMD carries a declaration that incorrect or inaccurate information is punishable under the Taxation Act. Late payment always attracts interest. The ETCB's English pages checked for this skill do not give a fine schedule for late filing; check the Taxation Act before quoting a figure.

**From 2027.** The ETCB announced that businesses will be able to submit the source data for the VAT calculation in a standardised xbrl_GL format over X-tee instead of the form-based return; other methods remain.

## Returns for 2025 periods (late filings and amendments)

- **January to June 2025**: standard rate 22%, on the KMD form valid from 1 January 2025 to 30 June 2025. Accommodation was already 13% and press publications 9% from 1 January 2025.
- **July to December 2025**: standard rate 24%, on the form valid from 1 July 2025.
- **Straddling supplies.** The rate follows the time of supply. The ETCB's examples: a June 2025 prepayment, paid in June, for goods delivered in July is taxed at 22%; a partial June advance is at 22% and the rest, delivered and paid in August, at 24%; a service from 1 June to 31 July 2025 invoiced in one amount with no prepayment is supplied in July and taxed wholly at 24%; separate monthly invoices split 22% and 24%; goods sold at 22% in May and returned in July are credited at 22%; an invoice issued in June alone creates no supply, so delivery and payment in July means 24% and the invoice must show 24%.
- **Old 20% contracts.** A written contract concluded before 1 May 2023 with a fixed 20% rate and no right to raise the price could keep 20% only until 30 June 2025 (shortened from 31 December 2025).

Source: [ETCB, Changes in the Estonian Value Added Tax Act](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax).

## Completion checklist

- [ ] VAT registration and effective date confirmed; limited-liability status checked.
- [ ] Ordinary calendar-month period confirmed, or an approved longer period referred with its actual ruling; every supply dated by time of supply.
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

## Sources

| Source and scope actually read | Official URL | Read on |
|---|---|---|
| Read for current standard rate and time-of-supply instruction: EMTA VAT standard rate | https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate | 2026-11-16 |
| Read for accommodation rate and cash-accounting transition: EMTA 13% rate | https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-13-vat-rate | 2026-11-16 |
| Read for eligible books, educational literature, listed medical goods and press exclusions: EMTA 9% rate | https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-9-vat-rate | 2026-11-16 |
| Read for return filers, VAT-group/limited-liability distinction, monthly deadline and annex threshold: EMTA filing VAT returns | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports | 2026-11-16 |
| Read for EUR 40,000 and EUR 10,000 thresholds, taxpayer definitions and e-MTA registration: EMTA registration | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer | 2026-11-16 |
| Read for official current form version and English/Estonian form distinction: EMTA VAT forms index | https://www.emta.ee/en/business-client/taxes-and-payment/tax-returns-exchange-information/vat-return-forms-vd-and-vdp | 2026-11-16 |
| Read for all KMD fields, formula, credit-note rate lines, reverse-charge information fields, adjustments and refund application: current official form and instructions, pages 1-5 | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07_eng.pdf | 2026-11-16 |
| Read for KMD INF fields, per-partner debit/credit thresholds, invoice exceptions and non-resident register codes: official instructions, pages 1-10, including the special-code columns | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_inf_2025_07_eng.pdf | 2026-11-16 |
| Read for 50% restriction, qualifying cars, full-deduction exceptions and business/private-use distinction: EMTA passenger cars | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting | 2026-11-16 |
| Read for guest/employee consumption block and employee business-trip accommodation exception: EMTA restrictions | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/restrictions-deduction-input-vat | 2026-11-16 |
| Read for all eight bad-debt conditions, court-claim exception, seller/buyer periods, no credit note and later payment: EMTA irrecoverable arrears | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/reduction-tax-liability-case-irrecoverable-arrears | 2026-11-16 |

| Read for customer status/capacity/location, especially pending VAT numbers and qualified presumptions: Regulation 282/2011 Articles 17-20, official 14 April 2025 consolidation; no claim of checking later amendments | https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 | 2026-11-16 |
| Read for 0% goods conditions, valid-number exceptions and reporting: EMTA zero-rated goods | https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-0-vat-rate-goods | 2026-11-16 |
| Read for full 2025-onward threshold composition, real-estate/insurance/financial and fixed-asset/occasional exceptions: EMTA threshold calculation | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer/threshold-calculation-1-january-2025 | 2026-11-16 |
| Read for threshold crossing, effective registration, review/notification, invoice correction and deregistration restart: EMTA obligation to register | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer/obligation-register-taxable-person | 2026-11-16 |
| Read for daily interest, claim minimum and whole-euro rounding: EMTA payment of interests | https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests | 2026-11-16 |

| Read for complete electronic submission, upload/submit distinction, status/errors, overwrite and UTF-8 instructions: EMTA e-MTA filing | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports/filing-e-mta | 2026-11-16 |
| Read for paper-filing alternatives, under 12 months OR fewer than five annex invoices: EMTA service offices | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports/filing-our-customer-service-offices | 2026-11-16 |
| Read for intra-Community reporting time, service column, immovable/export-service exceptions, call-off stock and VDP: EMTA when to declare | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports/when-declare | 2026-11-16 |
| Read for the dated July 2025 transition, all seven related examples, cash-accounting reduced-rate transitions and announced 2027 method: EMTA VAT changes | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax | 2026-11-16 |
| Read for OSS scope, EUR 10,000 threshold and exclusions, quarterly deadline, voluntary application and IOSS monthly deadline: EMTA special schemes, scoped sections only, not the full handbook | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services | 2026-11-16 |

| Read for the ordinary monthly period and EMTA approval of a longer period: State Portal VAT, declaring and paying section | https://www.eesti.ee/en/artikkel/doing-business/taxes/valueadded-tax | 2026-11-16 |
| Read for the voluntary SME scheme and current/previous calendar-year EU threshold, with the loose registration summary resolved against Directive Articles 284 and 288a: EMTA dedicated SME chapter | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-vat-provisions/special-scheme-small-businesses | 2026-11-16 |

| Read for inclusive EU-wide SME ceiling, prior notification, EX identification/activation and preceding/current-year cessation, and the full distance/digital supply threshold and destination option: VAT Directive Articles 59c, 284 and 288a, official 14 April 2025 consolidation | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 | 2026-11-16 |

Not yet confirmed: later amendments to the dated 14 April 2025 EU Directive and Implementing Regulation consolidations; the actual SME eligibility/activation workflow remains referred. The exact timing exception under VAT Act § 29^1(1)(6) for court-certified claims; current operative VAT Act text could not be reopened on Riigi Teataja. later amendments to the dated EU customer-status consolidation and the current self-supply calculation divisor for qualifying privately used taxi/driving-school vehicles could not be confirmed. Do not calculate that self-supply from the historical 1.2 divisor printed by the car page. Full OSS/IOSS registration, intermediary and correction workflows, detailed penalty amounts and other jobs expressly referred above remain outside this filing skill. Do not treat these held review gaps as newly verified; all six existing worked cases and original referrals are retained.
