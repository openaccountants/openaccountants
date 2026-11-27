---
name: estonia-vat-return
description: Use this Guide whenever asked to prepare, review, or classify transactions for an Estonian VAT return (KMD form) for any client. Trigger on phrases like "prepare VAT return", "do the KMD", "fill in KMD", "Estonian VAT", "kaibemaks", or any request involving Estonia VAT filing. This Guide covers Estonia only and standard KM registration. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this Guide before touching any Estonian VAT work.
version: 2.2
jurisdiction: EE
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: filing-howto
domain: vat-gst
---

# Estonia VAT return (KMD and KMD INF)

## Scope

This Guide covers the monthly Estonian VAT return, form KMD, and its annex, form KMD INF, for a person registered as liable to VAT in Estonia (a company such as an OÜ or AS, or a sole proprietor, FIE). It covers the rates in force for 2026 periods, the registration threshold, the monthly deadline and payment, domestic and cross-border reverse charge, the report on intra-Community supply (form VD), the OSS and IOSS special schemes at a summary level, corrections, bad-debt relief, and interest on late payment.

The primary year is 2026. This Guide applies the ordinary calendar-month period. Ask whether EMTA has approved a longer period; if so, use the actual approval and refer its period-specific requirements rather than applying the monthly defaults. A short dated section near the end covers 2025 periods, which straddle the 1 July 2025 rate change.

Use the Estonian VAT Act (KMS) and the Estonian Tax and Customs Board (Maksu- ja Tolliamet, EMTA/ETCB) forms. The [operative Act](https://www.riigiteataja.ee/akt/130062026129) was read in Estonian for the provisions cited below; its current consolidation applies from 1 October to 31 December 2026. Use the dated rules below for earlier supplies. Load vat-workflow-base and eu-vat-directive alongside this Guide.

Out of scope: VAT groups beyond a mention, the margin schemes for second-hand goods and travel services, partial exemption calculations, import VAT deferment authorisations, and the special-case VAT return for unregistered persons.

## Ask the client first

- **Are you registered as liable to VAT in Estonia, and from what date?** Get the VAT number. Registration takes effect from the day the threshold was exceeded, not the day the ETCB decides.
- **Are you a full taxable person, or a taxable person with limited liability?** Limited-liability persons file KMD only for periods with transactions under KMS § 3(5), without KMD INF; they have no input-VAT deduction.
- **Which month is being filed, and has EMTA approved a longer taxation period?** Obtain any approval before applying these ordinary monthly instructions. The rate depends on the time of supply, so the period matters.
- **Do you use cash accounting for VAT?** It changes when supply arises and keeps some transitional rates open until 31 December 2026.
- **What did you sell?** Standard-rated, accommodation, books, medicines and medical devices, press publications, exports, sales of goods or services to EU businesses, exempt supplies (financial, insurance, some property), and sales to consumers in other EU countries.
- **For every EU business customer: do you hold a valid VAT number from their Member State?** Ordinary intra-Community goods need the required valid number; new-vehicle/excise exceptions are held below.
- **What did you buy from abroad?** Services from EU or non-EU suppliers, goods from other EU countries, imports, and whether the foreign supplier charged its own VAT.
- **Do you own, lease or run any passenger cars (category M1)?** Is any car used only for business, with records that preclude private use?
- **Do you make any exempt supplies?** If yes, input VAT may need partial deduction and a year-end recalculation.
- **Did any customer fail to pay an invoice, or were credit notes issued?**
- **Are you in the OSS or IOSS scheme?** Those supplies go on a separate special-scheme return, not on KMD.
- **Is the company run by e-residents with no staff, office or permanent establishment in Estonia?** See "When to refuse or refer".

## The method, step by step

1. **Confirm who must file.** A full VAT registrant files KMD and KMD INF, including a nil return/annex indication when applicable. A limited-liability registrant files KMD only for periods with KMS § 3(5) transactions, without the annex or input deduction. An unregistered person who shows VAT on an invoice must declare and pay that VAT; do not refuse solely because turnover is below the registration threshold (KMS §§ 27(2), 29(12), 38).
2. **Fix the taxable period.** Use a calendar month unless EMTA approved a longer period. A first registration period with fewer than 15 calendar days may be combined with the next period (KMS § 27). For ordinary domestic supplies/services, the earlier of supply or payment fixes the tax point; advances count to the extent paid. Intra-Community goods normally use the following month’s 15th or an earlier invoice date (KMS § 11); do not apply the cash-accounting shortcut to cross-border transactions excluded by § 44(11).
3. **Sort every sale by rate and box.** Standard rate to line 1, the 13% rate to line 2², the 9% rate to line 2, zero-rated supply to line 3 and its sub-lines, exempt supply to line 8, and supply under the special arrangements of § 41¹ of the VAT Act to line 9.
4. **Self-assess reverse-charge purchases.** First establish an Estonian taxable purchase under KMS § 3(4), with no supplying Estonian establishment. A supplier validly using Estonia’s cross-border SME exemption with an EX number is excluded by § 3(7). Report taxable purchases in the rate base and line 4, plus the information lines below. Do not reverse-charge merely because a bank description is foreign, or assume foreign VAT removes an otherwise applicable liability.
5. **Compute output VAT in line 4.** The form's formula is 24% of line 1 + 20% of line 1¹ + 22% of line 1² + 9% of line 2 + 5% of line 2¹ + 13% of line 2².
6. **Collect deductible input VAT in line 5.** Include reverse-charge VAT you are entitled to deduct. Show import VAT (5.1), fixed assets (5.2) and passenger cars (5.3 or 5.4) as sub-lines of line 5.
7. **Apply restrictions.** Passenger cars: normally half, subject to the exceptions and further restrictions below. Mixed taxable/exempt activity needs attribution; wholly private expenditure gives no deduction.
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
| 13% | Accommodation, and accommodation with breakfast; not separately accompanying goods/services | From 1 January 2025 (previously 9%) | 2² | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-13-vat-rate |
| 9% | Books and educational literature (printed or electronic, except exempt learning materials under § 16(1)(6)); medicines, contraceptives, sanitary/hygiene goods and disability medical devices/aids (including qualifying aid hire) on the ministerial list; press publications (printed or electronic, not mainly advertisements/private advertisements, erotic/pornographic, video or music content) | Press publications back at 9% from 1 January 2025 (5% from 1 August 2022 to 31 December 2024) | 2 | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-9-vat-rate |
| 0% | Qualifying exports and intra-Community goods; apply the transport, customer-number and VD conditions below. Special transport, ship/aircraft and diplomatic supplies require a separate eligibility check | Standing | 3, 3.1, 3.1.1, 3.2, 3.2.1 | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-0-vat-rate-goods |
| 5% | Only for cash-accounting users: press publications invoiced and supplied before 1 January 2025, where supply arises later; allowed until 31 December 2026 | Transitional | 2¹ | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-9-vat-rate |
| 9% on accommodation | Only for cash-accounting users: accommodation invoiced and provided before 1 January 2025; allowed until 31 December 2026 (a right, not an obligation) | Transitional | 2 | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-13-vat-rate |
| 22% and 20% | Credit notes and § 29¹ adjustments on transactions originally taxed at those rates | Historic | 1² (22%), 1¹ (20%) | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |

Sources: [standard rate](https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate); [rates handbook](https://www.emta.ee/en/node/336/main_chapter/83171/pdf); [VAT Act changes](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax); [KMD form from 01.07.2025](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf).

The ETCB says the correct rate "must be chosen on the basis of the time of supply". Do not extend a publication’s reduced rate to ordinary software/games or excluded advertising publications.

### Thresholds and dates

| Item | Figure | Source | Official source |
| --- | --- | --- |---|
| Registration threshold | Estonian-place annual turnover under KMS § 19¹(3) exceeding EUR 40,000; composition and exceptions below | [Registration handbook](https://www.emta.ee/en/node/333/handbook/4/pdf) | https://www.riigiteataja.ee/akt/130062026129 |
| Time to apply after crossing it | Apply within three working days; registration normally within five working days of receipt, or of additional business evidence under KMS § 20(4¹) | Registration handbook | https://www.riigiteataja.ee/akt/130062026129 |
| Limited-liability registration | For an Estonian person/Estonian establishment outside full VAT registration: counted intra-Community goods above EUR 10,000 from year start; excise/new vehicles are separate; valid EX-exempt purchases excluded. Foreign services under § 21(1) can trigger registration from the first receipt, without a monetary threshold; private non-business individuals are excluded | [Registration page](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/registration-vat-payer) | https://www.riigiteataja.ee/akt/130062026129 |
| EU small-business scheme (foreign small enterprises) | Voluntary; EU-wide annual turnover must not exceed EUR 100,000 in either the current or previous calendar year. Exactly EUR 100,000 does not itself breach the EU-wide ceiling. National eligibility, prior notification and activated EX identification remain separate conditions; this headline alone does not establish eligibility | Directive Articles 284(2)-(5), 288a(2), 14 April 2025 consolidation; dedicated SME chapter | https://www.riigiteataja.ee/akt/130062026129 |
| OSS distance-sales and digital-services threshold | EUR 10,000 across all other Member States together | [Special schemes page](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services |
| KMD INF annex | Invoices totalling at least EUR 1,000 without VAT per transaction partner in the period | [Filing page](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| KMD, KMD INF and VD deadline | 20th day of the month after the period; VAT is also payable by then | Filing page; KMD form | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| OSS return | Quarterly, by the last day of the month after the quarter | Special schemes page | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services |
| IOSS return | Monthly, by the last day of the following month | Special schemes page | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services |
| Interest on late tax | 0.06% a day (21.9% a year) | [Payment of interests](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests) | https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests |
| Passenger-car input VAT | Normally 50%, subject to taxable business use | [Passenger cars and VAT](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting |
| Bad-debt relief with more than EUR 30,000 of VAT in the claim | Claim must be confirmed by a court judgment in force | [VAT Act changes](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax) | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/reduction-tax-liability-case-irrecoverable-arrears |

### What counts toward the EUR 40,000 (from 1 January 2025)

- Taxable supply of goods and services, including zero-rated supply, but not transfers of fixed assets.
- Real-estate transactions (sales, leases, rentals) under § 16(2) clauses 2, 3 and 6, except fixed-asset transfers and occasional transactions.
- Insurance and financial services, except occasional services.
- Only supply whose place of supply is Estonia. If all of a person's supply is exempt or zero-rated (and none is an intra-Community supply of goods), the ordinary § 19(1) obligation does not arise; its deemed-supplier marketplace rule is a separate exception.
- Margin-scheme turnover calculation is held with the other margin-scheme work below; do not use the margin as a registration shortcut.

A foreign business without an Estonian establishment normally registers from its first Estonian taxable supply that the recipient does not reverse-charge. First check the exceptions in KMS § 19(3): the qualifying EX small-business exemption, all-zero-rated supplies (subject to its intra-Community/deemed-supplier exclusions), and supplies covered by an OSS registration in another Member State. The SME exemption under § 19(1¹) requires EU turnover not exceeding EUR 100,000 in both the current and previous calendar years, the separate Estonian threshold conditions, and home-authority EX registration/confirmation for Estonia. If those conditions or the foreign supplier’s liability cannot be established, hold that transaction: Check this point with one of our partner accountants.

### KMD line map (form valid from 1 July 2025, used for 2026)

The form numbers some lines with a superscript: 1¹ is "line 1 superscript 1", and likewise 1², 2¹, 2² and 4¹. These are sub-lines of lines 1, 2 and 4. They are not the same as lines 11, 12 and 13 (adjustment, VAT payable, overpaid). English PDF text copies often print them flattened, as "11" or "41", so read them from the form layout.

| Line ([KMD form](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf)) | What goes in it | Official source |
| --- | --- |---|
| 1 | Taxable value at 24%. Includes intra-Community acquisitions of goods, services received from foreign businesses not registered in Estonia, self-supply, and credit notes on 24% supplies | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 1¹ | Credit notes and § 29¹ changes on transactions taxed at 20% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 1² | Credit notes and § 29¹ changes on transactions taxed at 22% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 2 | Taxable value at 9% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 2¹ | Taxable value at 5% (cash-accounting transition for press publications), plus credit notes and § 29¹ changes on transactions taxed at 5% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 2² | Taxable value at 13% | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 3 | Zero-rated supply under VAT Act § 15(3)-(4), except intra-Community supply performed by a customs agency for another person under § 17(2^1), which that agency reports on VD only | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 3.1 | Of which: intra-Community supply of goods, and general-rule services to taxable persons in other Member States, except recipient-state zero-rated services and services exempt under the small-business scheme | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 3.1.1 | Of which: intra-Community supply of goods | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 3.2 | Of which: exports of goods | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 3.2.1 | Of which: tax-free sales to travellers | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 4 | Total output VAT, calculated by the formula above | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 4¹ | Import VAT, only for persons the ETCB has authorised to declare import VAT on the KMD | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 5 | Total deductible input VAT | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 5.1 | Of which: import VAT | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 5.2 | Of which: VAT on fixed assets | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 5.3 | Number of cars, and input VAT, for cars meeting the § 30(4) 3) to 5) conditions (full deduction). Cars bought to resell or to rent out are not shown here, though their VAT is deductible in line 5 | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 5.4 | Number of cars, and input VAT, for cars used partly for business (at most 50% of input VAT) | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 6 | Information: intra-Community acquisitions of goods and services from taxable persons of other Member States | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 6.1 | Information: of which intra-Community acquisitions of goods | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 7 | Information: other acquisitions on which you calculate VAT (non-EU suppliers not registered in Estonia, triangular acquisitions, goods to be installed, § 41¹ goods) | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 7.1 | Information: of which § 41¹ acquisitions (immovables, scrap metal, precious metal and metal products) | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 8 | Exempt supply | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 9 | Supply under the § 41¹ special arrangements, and goods to be installed or assembled in another Member State | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 10 / 11 | Adjustments up (10) or down (11); only one of the two is completed | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 12 | VAT payable: line 4 + line 4¹ − line 5 + line 10 − line 11 | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |
| 13 | Overpaid VAT, by the same formula | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf |

Source: [KMD form and instructions, valid from 01.07.2025](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf). Amounts are entered to the cent, in euro.

### Reverse charge on the KMD, in one place

- **Services from an EU business** (general-rule B2B services): taxable value in line 1 (or 2 or 2²), VAT in line 4; also line 6. Deduct in line 5 if the service is used for taxable supply.
- **Goods acquired from another Member State**: line 1 (or 2 or 2²) and line 6 and 6.1; deduct in line 5.
- **Services or goods from a non-EU business not registered in Estonia** on which you must calculate VAT: line 1 and line 7; deduct in line 5.
- **Domestic reverse charge under § 41¹** (immovables sold under the option to tax, scrap metal, precious metal and metal products): the buyer declares the acquisition in line 1 and lines 7 and 7.1; the seller declares the supply in line 9, not line 1. In the KMD INF annex the seller's invoice carries special code 02 in Part A and the buyer's carries special code 12 in Part B.
- **Triangular transactions**: an Estonian acquirer (C) declares in line 1 or 2 and lines 4 and 7; an Estonian middle reseller (B) declares only in column 4 of form VD, not on the KMD; an Estonian first seller (A) declares an intra-Community supply in lines 3, 3.1 and 3.1.1 and on the VD.

### Passenger cars

The restriction applies to category M1 (including M1G) vehicles with a gross weight not exceeding 3,500 kilograms and no more than eight seats besides the driver's. For those cars, and for fuel, repairs, parking and other goods and services bought for them, the ordinary business car restriction is 50%; for a FIE/non-business allocation deduct only the business-use share, capped at 50%, then apply the taxable-supply proportion. Advertising/trailer allocation is held: Check this point with one of our partner accountants.

Full deduction is allowed only in the § 30(4) exceptions: a car bought for resale or for renting out (and not used by the buyer itself); a car mainly used for paid passenger transport or driving lessons, with the required licences; or a car used exclusively for business, where private use is precluded and the business can show it (for example a logbook or GPS records, and parking at the premises outside working hours). Employee commuting needs the separate § 30(4¹)/Income Tax Act conditions: Check this point with one of our partner accountants. Under the exclusive-business exception, if the car is used privately even once, including with the employee reimbursing the cost, it is not exclusive business use. The separate qualifying passenger-transport and driving-school exceptions can allow full deduction with private use taxed as self-supply; do not apply the exclusive-business test indiscriminately to those exceptions. Their private-use self-supply calculation is held: Check this point with one of our partner accountants. On the KMD, cars bought to resell or to rent out are deducted in full in line 5 but are not counted in line 5.3; line 5.3 is for the passenger-transport, driving-lesson and exclusive-business cars.

If a car bought as exclusively business-use with full acquisition VAT deducted first becomes privately used within two years of acquisition, amend the acquisition-period return to reduce the acquisition deduction: it is treated as partly business-use throughout those first two years. Running-cost VAT is not retrospectively reduced by that acquisition rule. From the month private use first starts, the running-cost deduction is capped at 50% for the following 12 months even if private trips stop sooner; exempt or non-business activity can reduce it further. Lease payments are running costs. For a qualifying taxi/driving-school car that leaves its exception within that period, account for self-supply VAT already paid when making the adjustment. Do not import the authority page's historical divisor of 1.2 into a 2026 self-supply calculation; its current 24% treatment requires the applicable law/rate and is held below. [EMTA passenger-car chapter, acquisition and running-cost adjustments](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting).

Where the business also makes exempt supply, the car percentage is applied on top of the partial-deduction proportion ([ETCB, Passenger cars and VAT accounting](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting)).

## Boundaries and exceptions

| Situation | Treatment ([ETCB filing guidance](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports)) | Watch for | Official source |
| --- | --- | --- |---|
| Sale of goods to a business in another Member State | 0%, lines 3, 3.1 and 3.1.1, and on form VD | Only if the buyer has the required valid VAT number from another Member State, transport evidence is held and the supply is correctly reported on VD. If the exemption conditions fail, classify the transaction under the applicable place-of-supply and destination rules; do not automatically assume Estonian VAT | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports/when-declare https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-0-vat-rate-goods |
| B2B general-rule service to a business in another Member State | General-rule service under the Estonian registration: no Estonian output VAT; line 3 and 3.1, VD column 5 | Using a foreign VAT registration or another special place rule requires separate classification; services tied to immovable property, services zero-rated in the customer's state (such as export transport), and services exempt under the small-business scheme are excluded from line 3.1 and VD; determine the applicable line 3 treatment from the actual supply and scheme | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports/when-declare |
| Sale to a consumer in another Member State (goods shipped, or digital services) | For eligible intra-Community distance sales dispatched from Estonia and telecommunications, broadcasting or electronic services, origin-country VAT applies only if the seller is established only in Estonia and the combined qualifying EU-wide value excluding VAT does not exceed EUR 10,000 in either the current or preceding calendar year, unless a destination-place option or active OSS applies. The destination-place option binds for at least two calendar years; active OSS does not reset to origin VAT at the start of a year. When the threshold is exceeded, destination treatment starts immediately; OSS is one reporting route | OSS supplies go on the OSS return, not on the KMD. Other consumer services do not automatically qualify for this EUR 10,000 derogation | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/special-schemes-e-commerce-and-services https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 |
| Export of goods outside the EU | 0%, lines 3 and 3.2 | Keep export evidence | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-0-vat-rate-goods |
| Tax-free sale to a traveller | Qualifying export: lines 3, 3.2 and 3.2.1 | KMS § 5(2): non-EU residence, same-day same-shop sale over EUR 38 including VAT, unopened goods removed by the third following month-end, and customs/police confirmation; otherwise hold | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/supply-taxable-0-vat-rate-goods |
| Exempt supply (for example insurance, most financial services, certain property transactions) | Line 8; related input VAT is normally not deductible (the eligible non-EU insurance/financial-service exception in KMS § 29(1) remains) | The option to tax some exempt supplies needs written notice to the ETCB before the supply | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| Wages, social tax, income tax, loan principal, dividends, own transfers, tax payments | Not supply: leave off the KMD | | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| Supply to or from a VAT group member | The group files one KMD; each member files its own KMD INF annex | | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| Mistakenly charged VAT on an invoice by an unregistered person | The VAT shown is payable; the person files a KMD | | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports |
| Goods moved to another Member State as call-off stock | Not on the KMD; declared on form VD in the call-off block, and on VDP if returned or the acquirer changes within 12 months | | https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports/when-declare |
| Invoice with mixed rates, zero-rated or exempt lines | KMD INF special code 03 | | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_inf_2025_07.pdf |
| Supply under the § 41 or § 42 margin schemes | KMD INF special code 01 | Margin schemes are out of scope here | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_inf_2025_07.pdf |

Sources: [Filing VAT returns and reports](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports); [KMD INF form from 01.07.2025](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_inf_2025_07.pdf); [rates handbook](https://www.emta.ee/en/node/336/main_chapter/83171/pdf); [VAT rates and exempt supply](https://emta.ee/en/business-client/taxes-and-payment/value-added-tax/vat-rates-and-supply-exempt-tax/standard-vat-rate).

### Classifying a bank statement

When working from a bank export, classify by what the invoice shows, not by the brand name on the statement:

- **Look at the billing entity and its country on the invoice.** A foreign brand may bill from an EU subsidiary (EU reverse charge, line 6) or from outside the EU (line 7). Obtain the invoice and actual transaction evidence; the statutory other-evidence exceptions for reverse charge remain available.
- **Loan principal, genuine interest and exempt financial/insurance services** give no Estonian input VAT. Inspect bank/payment-processor subscriptions and fees individually; their name alone does not establish exemption.
- **Salaries, social tax, income tax and payments to the ETCB** are not purchases: leave them out.
- **Owner transfers, dividends and transfers between own accounts** are out of scope.
- **Cash withdrawals**: ask what they paid for; exclude until supported by an invoice.
- **Guest entertainment, employee meals and employee accommodation**: input VAT is blocked by VAT Act § 30(1)-(2), except employee accommodation on a business trip. A business purpose alone does not remove the block. Where goods were bought for taxable business use and later diverted to staff or guests, apply the self-supply treatment described by EMTA. Separate ordinary restaurant trading purchases from guest or employee consumption.
- **Domestic purchases at 24% with a valid Estonian invoice**: deductible in line 5 if used for taxable supply.

When facts are missing, hold the affected classification. Establish customer business status/capacity, actual supply, country and rate; do not infer B2C or Estonian VAT merely from a missing VAT number. Pending-number evidence and special/private-use services require the companion EU rules; if unresolved: Check this point with one of our partner accountants. Ordinary intra-Community goods still need the required number, transport and VD evidence. New vehicles and excise exceptions are held. Domestic input VAT requires a compliant invoice; reverse-charge goods/foreign services may use other evidence under KMS § 31(2)–(3). A wholly private car gives no business deduction.

## Worked cases

### Case 1: domestic sale and a US software subscription, March 2026 ([KMD form](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf))

An Estonian OÜ, fully taxable, sells consulting in Estonia for EUR 1,000 net and buys a EUR 100 software subscription from a US company not registered in Estonia.

- Line 1: EUR 1,000 + EUR 100 = EUR 1,100.
- Line 4: 24% of EUR 1,100 = EUR 264 (EUR 240 on the sale and EUR 24 self-assessed on the subscription).
- Line 7: EUR 100 (information).
- Line 5: EUR 24 deductible, because the software is used for taxable supply.
- Line 12: EUR 264 − EUR 24 = EUR 240 payable by 20 April 2026.
- KMD INF: the sale goes in Part A if that customer's invoices in March total at least EUR 1,000 without VAT, which they do. Assume the US supplier has no supplying Estonian establishment. The US supplier has no Estonian register code, and the KMD INF instructions say invoices of non-resident partners without one are not declared, so it is not listed in Part B.

### Case 2: company car fuel ([ETCB example](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting))

Fuel costs EUR 50 plus EUR 12 VAT. The company's supply is 60% taxable and 40% exempt.

- Car also used privately: deductible input VAT = EUR 12 × 50% × 60% = EUR 3.6, shown in line 5 and line 5.4.
- Car used exclusively for business (private use precluded and recorded): EUR 12 × 60% = EUR 7.2, shown in line 5 and line 5.3.

Source: [ETCB, Passenger cars and VAT accounting](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/calculation-and-refund-vat/passenger-cars-and-vat-accounting).

### Case 3: crossing the registration threshold ([ETCB handbook](https://www.emta.ee/en/node/333/handbook/4/pdf))

A sole trader's Estonian supply since 1 January passes EUR 40,000 on Friday the 2nd of a month.

- The application is due within three working days: by Wednesday the 7th, assuming the intervening weekdays are working days and no public holiday changes the count.
- The ETCB registers the person from the 2nd. The ordinary five-working-day decision period runs from receipt of the application, or receipt of additional business evidence if required by § 20(4¹).
- VAT is due from the effective registration date, including the threshold-crossing taxable supply. For ordinary domestic supplies, issue the compliant invoice within seven calendar days of supply/payment under § 37; do not count seven days from receipt of the VAT number. Correct a previously non-compliant invoice.

Source: [ETCB registration handbook](https://www.emta.ee/en/node/333/handbook/4/pdf).

### Case 4: KMD INF annex, several small invoices ([ETCB filing guidance](https://www.emta.ee/en/business-client/taxes-and-payment/value-added-tax/filing-vat-returns-and-reports))

In May 2026 a company issues two invoices at 24% to the same Estonian business customer: EUR 600 and EUR 500 without VAT.

- Total per partner = EUR 1,100, which is at least EUR 1,000, so both invoices go in Part A.
- A different customer with a single EUR 900 invoice is below the limit and need not be listed (the Act allows listing invoices below the limit).
- Invoices to private individuals acting outside a sole-trader business are not declared.

### Case 5: late payment interest ([ETCB interest](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests))

EUR 5,000 of VAT for June 2026, due 20 July 2026, is paid 10 days late.

- Interest = EUR 5,000 × 10 × 0.06% = EUR 30.
- Interest claims are rounded to whole euros; no interest demand is issued below EUR 10, which is not a general exemption from accruing/paying interest. This case assumes no statutory suspension or reduction.

Source: [ETCB, Payment of interests](https://www.emta.ee/en/business-client/taxes-and-payment/payment-arrears/payment-interests).

### Case 6: EU B2B service and an Irish advertising invoice ([KMD form](https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf))

A company invoices EUR 3,500 of consulting to a German business with a valid German VAT number, and receives an invoice for EUR 850 of advertising from an Irish company.

- Sale: line 3 and 3.1 with EUR 3,500; also column 5 of form VD, both due by the 20th of the following month.
- Purchase: line 1 and line 6 with EUR 850; line 4 includes 24% of it, EUR 204; line 5 deducts EUR 204 if used for taxable supply. Assume a normal taxable Irish supplier without an Estonian registration/establishment or applicable EX exemption, and taxable business use. The Irish supplier has no Estonian register code, so its invoice is not declared in KMD INF Part B.

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

## Original cases retained from earlier versions

These are the original inputs, not extra current invoices. The common law/evidence conditions above apply. **A historical 22% invoice with no verified supply date is not a usable 2026 deduction or tax computation.** Keep its stated amount; obtain the tax point and compliant evidence rather than changing the input or silently redating it. Where indicated, the result is held: Check this point with one of our partner accountants.

### April bank examples (original 2026 dates)

| Original example and input | Corrected conditional result or hold |
|---|---|
| Example 1: `03.04.2026 ; NOTION LABS INC ; -14.68 EUR` (original net input) | If evidence confirms a EUR 14.68 net general-rule foreign business service with no supplying Estonian establishment: 24% = EUR 3.52, rate base line 1, output line 4, information line 7; equal line 5 deduction only to the eligible extent. A merchant name alone proves none of those facts. |
| Example 2: `10.04.2026 ; GOOGLE IRELAND LIMITED ; -850.00 EUR` | If EUR 850 is net taxable advertising from the Irish entity with no Estonian registration/establishment or EX exemption: EUR 204 output, lines 1/4/6 and eligible line 5. If net/gross or supplier status is unproved, hold. |
| Example 3: `15.04.2026 ; RESTORAN TCHAIKOVSKY ; -220.00 EUR` | Purpose remains unknown. Guest entertainment/staff meals are blocked; restaurant trading inputs are different. No automatic deduction from the bank name. Hold pending facts. |
| Example 4: `28.04.2026 ; CIRCLE K EESTI ; Fuel ; -60.00 EUR` | Car use/evidence remain unknown. If invoice proves EUR 60 gross at 24%, VAT is EUR 11.61 and the ordinary 50% deduction EUR 5.81 before further business/exempt restrictions (lines 5/5.4). Do not use the old derived net EUR 50.85 or VAT deduction EUR 5.59, which used 22%. Hold until use and invoice are established. |
| Example 5: `22.04.2026 ; STUDIO KREBS GMBH ; +3,500.00 EUR` | Apply current Case 6’s EUR 3,500 service treatment only after its German business/customer, general-rule and establishment conditions are met; lines 3/3.1, VD column 5. |
| Example 6: `18.04.2026 ; EURONICS EESTI ; Laptop ; -1,595.00 EUR` | If the invoice confirms EUR 1,595 gross at 24% and eligible taxable use: EUR 308.71 input VAT in line 5, also 5.2 if a fixed asset. The bank debit alone does not establish gross/net, invoice validity or asset classification. Hold those unresolved inputs. |

### Original edge cases EC1–EC18

| Case | Original facts and destination |
|---|---|
| EC1 | Finnish hotel invoice showing 14% foreign VAT; no Estonian input VAT/reverse charge for Finnish accommodation. Foreign-rate validity and foreign refund: Check this point with one of our partner accountants. Do not call foreign VAT automatically irrecoverable. |
| EC2 | Monthly US software, no VAT shown: use the foreign-service matrix after checking actual place/supplier/evidence; eligible deduction can neutralise output. |
| EC3 | Car EUR 20,000 + EUR 4,400 VAT (22%), mixed private/business use. Keep that invoice input; no verified tax point. The old EUR 2,200 deduction is held for 2026. If a legitimate historic invoice is established, apply its actual VAT and restrictions; current mixed-car sub-line is 5.4. |
| EC4 | Claimed exclusively business car with stated EUR 4,400 VAT and notification. Exclusive use must be substantiated; line 5.3, not the old 5.4. The 22% tax point remains held as in EC3; notification alone does not prove entitlement. |
| EC5 | Goods sold to US customer: only qualifying export with removal/sale evidence gets lines 3/3.2 and zero rate. |
| EC6 | Goods sold to Latvian company with a valid VAT number: add transport and VD evidence; lines 3/3.1/3.1.1. |
| EC7 | Domestic returned-goods credit note: reverse eligible input VAT in line 5 in the credit-note period, at original invoice rate. |
| EC8 | Estonian e-resident IT consultant serving EU/non-EU businesses and consumers: no blanket “foreign customer = outside VAT”. Check this point with one of our partner accountants. |
| EC9 | German machinery invoice at 0%, valid VAT number: ordinary taxable acquisition enters the rate base/4/6/6.1 and eligible 5, also 5.2 if a fixed asset. |
| EC10 | EUR 1,200 excluding VAT with one partner: apply reportable-invoice conditions and direction separately; then INF A or B as appropriate. |
| EC11 | Commercial-property sale and proposed option to tax: newly taxable buildings/land and election conditions need classification first. Check this point with one of our partner accountants. |
| EC12 | Investment gold from Estonian dealer: do not assume automatic domestic reverse charge or no deduction. Check this point with one of our partner accountants. |
| EC13 | Service spanning 1 January 2024 (20% to 22%), invoice after change: retain that year; use tax points, not invoice date alone. Complete historical transition conditions: Check this point with one of our partner accountants. |
| EC14 | Sales invoice unpaid for more than 12 months: non-payment/bankruptcy alone is insufficient; ordinary relief requires all § 29¹ conditions above. |
| EC15 | Fuel EUR 500 + EUR 110 VAT (22%), mixed car: preserve invoice figures; old EUR 55 deduction held without verified historic tax point/use. For a legitimate historic invoice use line 5/5.4 with its actual eligible amount. |
| EC16 | German A → Estonian B → Latvian C, goods direct Germany–Latvia: keep roles; use the triangle declaration matrix only after simplification eligibility is confirmed. Check this point with one of our partner accountants. |
| EC17 | Related entities forming VAT group: Check this point with one of our partner accountants. Existing registered-group filing is described above. |
| EC18 | Used-car dealer buys/resells cars under possible margin scheme: Check this point with one of our partner accountants. No automatic margin eligibility or ordinary line-8 mapping. |

### Original Tests 1–15

| Test | Original inputs retained; corrected result or non-usable hold |
|---|---|
| 1 | Domestic office supplies EUR 244 gross / 200 net / 44 VAT at 22%: arithmetic consistent, tax point unverified; no automatic 2026 EUR 44 deduction. Hold. |
| 2 | Finnish consulting EUR 1,000 net, no VAT: for a taxable 2026 general-rule service, EUR 240 output and eligible input, lines 1/4/6/5; old EUR 220 expectation is superseded. |
| 3 | Mixed car EUR 20,000 + EUR 4,400 VAT, not notified business-only: same tax-point hold as EC3; do not silently replace EUR 4,400. |
| 4 | Latvia goods EUR 5,000, 0%, verified customer number: transport/VD/ordinary supply conditions required; lines 3/3.1/3.1.1, no output VAT. |
| 5 | Unregistered business below EUR 40,000 buys supplies: no ordinary registrant’s input deduction. Do not conclude “cannot ever file KMD”; first consider limited registration, foreign services and VAT improperly invoiced. |
| 6 | US supplier (Google Workspace), EUR 50/month, no VAT: if evidenced net taxable foreign service in 2026, EUR 12 output/eligible input; lines 1/4/7/5. Retain the stipulated US supplier; brand does not change it to Ireland. Old EUR 11 expectation is superseded. |
| 7 | Hotel sale EUR 113 gross / 100 net / 13 VAT: qualifying accommodation, line 2² EUR 100 and line 4 EUR 13; extras separately classified. |
| 8 | Guest dinner EUR 300 gross / 251 net / 49 VAT, stated 22%: block entertainment input (zero). The supplied net/VAT breakdown is itself inconsistent; do not repair it by silently changing the inputs. |
| 9 | Scrap metal EUR 5,000, supplier invoice labelled 0% domestic reverse charge: verify § 41¹ eligibility and correct invoice (reverse charge is not a zero-rated sale); taxable 2026 base yields EUR 1,200 output, lines 1/4/7/7.1, eligible 5. Old EUR 1,100 expectation is superseded. |
| 10 | China electronics customs value EUR 10,000; assessed import VAT EUR 2,200 (22%), customs document: preserve actual assessment; tax point and assessment basis unverified. Do not compute a new assessment from customs value alone or claim this as current 2026 VAT. Hold; ordinary eligible import input uses 5/5.1. |
| 11 | German machinery EUR 15,000 net, 0% supplier invoice: taxable 2026 acquisition gives EUR 3,600 output/eligible input, lines 1/4/6/6.1/5, plus 5.2 if fixed asset. Old EUR 3,300 expectation is superseded. |
| 12 | German hotel EUR 500 including stated EUR 35 German VAT (7%): preserve input, no Estonian reverse charge/input; rate/arithmetic and possible foreign refund remain held. Check this point with one of our partner accountants. |
| 13 | Mixed-car fuel EUR 500 + EUR 110 VAT (22%): same historic tax-point hold as EC15, including old EUR 55 expectation. |
| 14 | Branded pens EUR 8 each, total EUR 400 + EUR 88 VAT: preserve original inputs; do not assume a EUR 10 input-deduction safe harbour. Gifts/self-supply and historic rate: Check this point with one of our partner accountants. |
| 15 | Wine gifts EUR 25 each, total EUR 500 + EUR 110 VAT: preserve original inputs; do not apply an invented over-EUR-10 purchase deduction block. Gifts/self-supply and historic rate: Check this point with one of our partner accountants. |

## When to refuse or refer

The ordinary KMD workflow above remains usable. Hold only the affected specialised transaction below; do not apply an unproved outcome.

- E-resident company without clear Estonian business substance; foreign tax refunds; complex supplier/customer status or foreign VAT charged in error: Check this point with one of our partner accountants.
- Partial-exemption method/year-end computation beyond the simple car example, claimed de minimis relief, fixed-asset adjustment calculations and car private-use self-supply: Check this point with one of our partner accountants.
- Margin/travel/auction schemes and their registration turnover; diplomatic, ship/aircraft or special transport zero rates; healthcare/education/universal-post/gambling exemption eligibility, property eligibility/option to tax, investment gold, mobile phones/circuits and other uncertain domestic reverse-charge classifications: Check this point with one of our partner accountants.
- VAT-group formation (the registered group files one KMD and member annexes), call-off-stock eligibility/12-month conditions, complex triangulation eligibility, import-deferment authorisation and court-certified bad debts: Check this point with one of our partner accountants.
- OSS/IOSS registration, intermediaries and correction workflows; Intrastat thresholds/deadlines, fiscal representation, deregistration and pre-2025 form versions: Check this point with one of our partner accountants.
- Detailed penalty figures, refund processing timelines, gifts/alcohol/tobacco outcomes beyond the express entertainment block, foreign VAT recovery, unsupported bank-format assumptions and the announced 2027 workflow: Check this point with one of our partner accountants.

## Filing and payment

**Deadline.** The KMD and the KMD INF annex are filed, and the VAT is payable, by the 20th day of the month after the taxable period. The VD report has the same deadline. If that due date is a public holiday or other non-working day, it moves to the next working day. If no reportable intra-Community supply was made, no VD is filed.

**How.** In [e-MTA](https://maasikas.emta.ee), choose “Maksud” → “Käibemaks” → “KMD esitamine ja vaatamine” → “Lisa uus deklaratsioon”. Enter KMD and KMD INF manually or upload XML/CSV; then click “Esita deklaratsioon”. Check the status is “Esitatud”; “Esitamata” and the “Vead” column mean errors to correct before resubmitting. Re-uploading overwrites the data of the included part(s), not necessarily every part. X-tee submission from accounting software is another route. Under KMS § 27(1¹), electronic filing is mandatory once registered for at least 12 months **or** the annex contains more than five invoices; paper otherwise, or with EMTA permission on a reasoned request. Do not use the former “under 12 months OR fewer than five” paper test.

**Payment.** Pay to the ETCB prepayment account. Interest runs at 0.06% a day from the day after the due date until payment. Instalment schedules can be applied for in e-MTA.

**Refunds.** An overpayment (line 13) stays on the prepayment account unless you apply for a refund, or for a transfer to another person's prepayment account.

**Corrections.**
- KMD and KMD INF: amend the return for the original period in e-MTA, by re-uploading a corrected file or editing online. Remember that an uploaded file replaces all previous data for that part.
- Credit notes: declare in the period the credit note is issued, at the rate of the original invoice (so a credit note on a 22% invoice goes to line 1², and one on a 20% invoice to line 1¹). Show them in the VD for that period too, if the original was on a VD.
- VD: corrections and late call-off stock entries go on form VDP.
- OSS and IOSS: correct a previous return in a later return, not by amending the original.
- Mismatches between your KMD INF and your trading partners' annexes can affect your tax behaviour rating and send your return for review; resolve them with the partner first.

**Bad-debt relief (§ 29¹).** For ordinary claims, reduce VAT only on the unpaid portion when all conditions are met: a § 37 invoice and original VAT declaration; no assignment of the claim; 12 months to three years since payment was due; accounting write-off after all reasonable collection efforts or disproportionate collection cost; no associated buyer; and written notice to the buyer in the write-off month stating the VAT. A claim containing more than EUR 30,000 VAT requires a final court judgment; the statute expressly excepts that case from its ordinary time-window condition. Court-certified claims, aggregating invoices and disputed notification are held: Check this point with one of our partner accountants.

The seller adjusts in the write-off month at the original invoice rate (including 22% or 24% for a 2026 write-off); the buyer reverses the corresponding previously deducted input VAT in the month it receives notice. Use negative invoice figures in KMD INF only when reportable. Later recovery is taxable to the extent paid in the payment month. Do not issue a price-reduction credit note merely for non-payment (KMS §§ 29(7), 29¹ and the KMD INF instructions).

**Penalties.** The KMD carries a declaration that incorrect or inaccurate information is punishable under the Taxation Act. Ordinary late payment accrues interest, subject to statutory suspension/reduction grounds. The ETCB's English pages checked for this Guide do not give a fine schedule for late filing; check the Taxation Act before quoting a figure.

**From 2027.** EMTA now announces data-based filing from April 2027, with changed formats and combined VD data. Do not reuse this 2026 form map for that workflow: Check this point with one of our partner accountants.

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
- [ ] Input VAT in line 5 only with the evidence required by KMS § 31 and an eligible taxable-business use; sub-lines 5.1, 5.2, 5.3 and 5.4 filled.
- [ ] Cars: 50% unless an exception is documented; car count entered in 5.3 or 5.4.
- [ ] Partial deduction applied if any exempt supply; year-end recalculation in line 10 or 11.
- [ ] Credit notes at the original rate (lines 1¹ and 1² for old 20% and 22% invoices; line 2¹ for 5%).
- [ ] KMD INF Parts A and B complete for every partner at or above EUR 1,000; special codes used (Part A: 01 for §§ 41–42, 02 for § 41¹, 03 for mixed-rate/exempt/outside-scope invoices; Part B: 11 for partial deduction under § 29(4), § 30 or § 32, 12 for § 41¹ acquisitions); partner registry codes entered.
- [ ] OSS or IOSS supplies kept off the KMD.
- [ ] Line 12 or 13 reconciled to the ledger; refund application made if wanted.
- [ ] Filed and paid by the 20th of the following month.

## Sources

| Source and provisions actually read | Official URL | Read on |
|---|---|---|
| Estonian KMS, operative 1 October–31 December 2026: §§ 1–3, 5, 7–11, 15–16, 19–21, 26–33, 37–38, 41¹, 43–44 and 46; rates, registration, SME exception, tax points, returns, evidence, restrictions, ordinary bad debt and scheme deadlines. Read rendered law in browser; direct reader exposed only a JavaScript shell. | https://www.riigiteataja.ee/akt/130062026129 | 2026-11-27 |
| Estonian KMD, both pages: superscript fields, output formula, reverse-charge information, input sub-lines, adjustments, payable/overpaid result and refund request. | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_2025_07.pdf | 2026-11-27 |
| Estonian KMD INF, pages 5–7 instructions: debit/credit thresholds, exceptions, partner codes, invoice timing, special codes including § 30 partial deduction and corrections. | https://www.emta.ee/sites/default/files/documents/2025-07/vorm_kmd_inf_2025_07.pdf | 2026-11-27 |
| Estonian EMTA e-MTA instructions: menu, submit/status/errors and overwrite of included parts; filing overview for X-tee. | https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaibedeklaratsiooni-ja-aruannete-esitamine/e-mtas | 2026-11-27 |
| Estonian car chapter: business/non-business cap, exemptions, original fuel examples, acquisition amendment and running-cost period. | https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaibemaksu-arvutamine-ja-tagastamine/soiduautodega-seotud-kaibemaksuarvestus | 2026-11-27 |
| Estonian interest chapter: accrual, rate, claim threshold/rounding and suspension grounds. | https://www.emta.ee/eraklient/maksud-ja-tasumine/tasumine-volad/intresside-tasumine | 2026-11-27 |
| Estonian EMTA VAT changes: original 2025 tax-point examples and dated rate changes; older 20% end-date summary is superseded by KMS § 46/current July subsection. | https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks | 2026-11-27 |
| Estonian intra-Community declaration chapter: VD services and column 5, call-off/VDP directions; triangle role table read separately. | https://www.emta.ee/node/337/chapter/10406/pdf ; https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaupade-maksustamine/kolmnurktehingu-deklareerimise-pohimotted | 2026-11-27 |
| Estonian EMTA new-registrant memo: holiday/non-working-day deadline shift (calendar section). | https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaibedeklaratsiooni-ja-aruannete-esitamine/kassapohise-kaibemaksukohustuslase-meelespea | 2026-11-27 |
| Estonian EMTA 2027 announcement: April start and changing workflow only, not an operative 2026 filing instruction. | https://www.emta.ee/ariklient/maksud-ja-tasumine/kaibemaks/kaibedeklaratsiooni-ja-aruannete-esitamine/kaibedeklaratsiooni-esitamine-muutub-2027-aastal-andmepohiseks | 2026-11-27 |

Not yet confirmed: every specialised outcome expressly held above, including unverified historical 22% invoice tax points and foreign tax figures, remains non-usable. Check this point with one of our partner accountants. Historical cases marked “hold” use that same non-usable referral. No source availability or earlier “verified” label is treated as proof. No accountant approval is claimed.
