---
name: montenegro-vat
description: "Montenegro value added tax (PDV) for 2026 under the VAT Law as amended by Official Gazette 12/26 (in force 6 February 2026, building land taxable from 1 April 2026). Covers who must register (EUR 30,000 in the last 12 months, application by the 20th of the next month), the 21% standard rate, the 7% and 15% reduced lists (bread, flour and sunflower oil at 7%: their 2022 zero rate ended on 31 December 2022), 0% supplies including exports, exemptions, tax point and advances, import VAT, place of supply for services and the recipient's reverse charge, input VAT restrictions and the rounded annual pro rata, the monthly PR PDV-2 return and payment by the 15th through IRMS, refunds in 60 or 30 days, fines and late-payment interest (0.03% a day to 17 July 2026, then 5.4% a year). The July 2026 VAT Law (104/26) applies only from EU accession. Use with vat-workflow-base."
version: 2.1
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
depends_on:
  - vat-workflow-base
---

# Montenegro VAT (PDV), tax year 2026

[law]: https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0
[amend]: https://wapi.gov.me/download/80b15e7e-da28-49b7-9ca6-de1849b9ab61?version=1.0
[future]: https://wapi.gov.me/download/a7c33b8f-aa74-4197-b1fa-317ea466161f?version=1.0
[form]: https://wapi.gov.me/download/e3d2b1f2-341b-487e-8e2a-d77868bbf52e?version=1.0
[irms]: https://www.gov.me/clanak/vazno-obavjestenje-u-vezi-sa-pocetkom-primjene-novog-integrisanog-it-sistema-poreske-uprave-irms
[tal]: https://wapi.gov.me/download/6bf4fd6a-fa32-4c33-9f5a-3a13ae509233?version=1.0
[g4922]: https://www.sluzbenilist.me/propisi/333002/download
[g6522]: https://www.sluzbenilist.me/propisi/338064/download
[g9424]: https://www.sluzbenilist.me/propisi/373704/download

## Who this applies to

A taxable person is anyone who independently carries on a business activity (production, trade, services, farming, professions, or the lasting exploitation of property for income), whatever its purpose or result. A person who occasionally supplies newly built buildings, parts of them, or building land is also a taxable person. Importers are taxable persons for the goods they import. State and local bodies acting in their public functions are outside, unless they make supplies that would be taxable in other hands. [VAT Law arts. 13, 4][law]; [12/26 arts. 1, 4][amend]

Small taxpayers: a person whose supplies in the last 12 months do not exceed, and are not likely to exceed, EUR 30,000 is not a taxable person. They must not show VAT on invoices and have no right to deduct input VAT. They may apply to register voluntarily; the registration then lasts at least three years. The small-taxpayer rule does not apply to taxpayers established outside Montenegro. [VAT Law art. 42][law]

Who pays the tax (the tax debtor): the supplier; the tax representative of a non-established supplier, or, if none is appointed, the recipient; anyone who shows VAT on an invoice when not entitled to; the importer; and, for natural gas, electricity and heating or cooling, the registered energy wholesaler or registered buyer for own use. [VAT Law art. 12][law]

Use this skill with `vat-workflow-base`. Monetary amounts are in euro; Montenegro uses the euro.

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Standard rate | 21% on every supply of goods and services and every import not given a reduced or zero rate | 2026 | [VAT Law art. 24][law] |
| Reduced rate 7% | basic foods (bread, flour, milk and dairy products, infant food, lard, oil including sunflower oil, meat, eggs, sugar); medicines including veterinary, other than those at 0% under art. 25(1)(9); orthotic and prosthetic aids and surgically implanted medical devices, other than those at 0% under art. 25(1)(9); textbooks and teaching aids; drinking water other than bottled; daily and periodical press (not mainly advertising); public passenger transport and luggage; public hygiene services; funeral services and related goods; animal feed, fertiliser, plant protection, seed and planting material, live animals; menstrual products; baby nappies | 2026 | [VAT Law art. 24a(1)][law] as replaced by [94/24 art. 1][g9424] |
| Reduced rate 15% | books and serial publications; accommodation in accommodation establishments defined by the tourism law; preparing and serving food and drink in catering establishments, except alcoholic drinks, sweetened still or sparkling drinks, and coffee; copyright and services in education, literature and art; copyright in science, works of art, collections and antiques; admission tickets to cinema, theatre, concerts, museums, fairs, amusement parks, exhibitions, zoos and similar events (unless exempt); use of sports facilities for non-profit purposes; marina services (15% until EU accession); solar panels; hairdressing | 2026 | [VAT Law arts. 24a(2), 71i][law] |
| Zero rate 0% | exports by the seller or a non-established buyer; services directly linked to exports and imports; international air and sea transport; supplies to diplomatic missions and international organisations; medicines and medical devices on the Health Insurance Fund list; supplies to free zones and customs warehouses; donor-funded and loan-funded supplies where the agreement excludes tax | 2026 | [VAT Law art. 25(1)][law] |
| Registration threshold | supplies above EUR 30,000 in the last 12 months or a shorter period | 2026 | [VAT Law art. 55(1)][law] as replaced by [12/26 art. 13][amend] |
| Small-taxpayer limit | EUR 30,000 in the last 12 months (not likely to exceed); voluntary registration for at least 3 years | 2026 | [VAT Law art. 42][law] |
| Registration application | by the 20th day of the month after the month the threshold was passed; decision within 7 days | from 6 Feb 2026 | [12/26 art. 13][amend] |
| Tax period | calendar month | 2026 | [VAT Law art. 33][law] |
| Return and payment | electronic return and payment by the 15th of the following month; nil return still required | 2026 | [VAT Law arts. 35, 36][law] |
| Tax point with no invoice | 8 days after delivery or performance | 2026 | [VAT Law art. 18(3)][law] |
| Farmer flat-rate compensation | 8% of the purchase value, paid by the registered buyer and deductible as input VAT | 2026 | [VAT Law art. 43][law] |
| Refund of excess input VAT | 60 days from the return; 30 days for mainly-export taxpayers and those with an excess in more than 3 consecutive returns | 2026 | [VAT Law art. 50][law] |
| Capital goods correction period | 5 years (equipment), 10 years (immovable property); no correction for a difference of EUR 30 or less | 2026 | [VAT Law art. 39][law], [12/26 art. 12][amend] |
| Record retention | 5 years after the year concerned; 20 years for property records | 2026 | [VAT Law art. 54][law] |
| Fine, legal person, late or missing return or registration and other art. 58 offences | EUR 3,000 to 10,000; responsible person EUR 800 to 2,000; entrepreneur EUR 1,000 to 4,000 | from 6 Feb 2026 | [12/26 art. 14][amend] |
| Fine, legal person, wrong tax point, base, input VAT, late payment and other art. 59 offences | EUR 6,000 to 20,000; responsible person EUR 1,500 to 2,000; entrepreneur EUR 2,000 to 6,000 | 2026 | [VAT Law art. 59][law] |
| Late-payment interest, 1 January to 17 July 2026 | 0.03% a day from the day after the due date | 2026 | [Tax Administration Law art. 95][tal] |
| Late-payment interest, 18 July to 31 December 2026 | 5.4% a year (ECB main refinancing rate + 3 points, set each half-year) | 2026 | [104/26 Tax Administration Law amendment arts. 20, 26](https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0); [Tax Administration decision, 24 Jul 2026](https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0) |

The 12/26 amendment entered into force on publication, 6 February 2026. It did not change the rates in arts. 24 to 25 (its only art. 25 change adds a reciprocity condition for diplomatic staff and widens the art. 25(2) rulebook reference). The repeal clause of the July 2026 VAT Law lists 12/26 as the last amendment of the current law, so these rates apply for the whole of 2026. [12/26 arts. 8, 16][amend]; [104/26 art. 212][future]

Bread, flour and sunflower oil are 7% in 2026 (rows 12 and 18). The consolidated text still prints art. 25(1)(12d), which zero-rated them, but that point is spent. Official Gazette 49/22 added it for flour and sunflower oil from 6 May 2022, 65/22 added bread from 21 June 2022, and both laws provide that point 12d ceased to be valid on 31 December 2022 (arts. 71e and 71f). No later amendment extended it. Art. 24a(1)(1), as replaced by 94/24 from 1 January 2025, lists bread, flour and oil at 7%, and 94/24 also removed point 12d from the import exemption cross-reference in art. 28. [VAT Law arts. 24a(1)(1), 25(1)(12d), 71e, 71f][law]; [49/22 arts. 2, 4][g4922]; [65/22 arts. 2, 3][g6522]; [94/24 arts. 1, 3, 6][g9424]

Goods are classified under the customs tariff and activities under the activity classification. The Ministry of Finance publishes the detailed lists for the 7% and 15% rates. [VAT Law arts. 24a(3), 61][law]

## The taxable base

### Supplies and what is out of scope

A supply of goods is a transfer of the right to dispose of movable or immovable property. It includes supplies under a public body's order, sales on commission, hire-purchase, sale of newly built buildings and real rights giving ownership or possession, sale of building land by a taxable person (from 1 April 2026), disposal of business assets by a liquidator or receiver, supplies of gas, electricity and heating or cooling, private use of business goods where input VAT was deductible, and barter. Land other than building land is not a supply. Used cars, motorcycles and boats are not a supply where no input VAT was deductible on purchase. [VAT Law art. 4][law] as replaced by [12/26 art. 1][amend]

Building land: art. 4(2)(5) applies from 1 April 2026. Building land is land for which an act approving construction has been issued; land under a new building is part of the supply of that building (art. 4(4) to (5)). Advance payments for new buildings or building land made up to 1 April 2026, where the final invoice is issued later, are taxed under the earlier text, with no correction on the final invoice up to the amount of the advance. [12/26 art. 15, new art. 72b][amend]

Transfer of a going concern: the transfer of all or part of the assets, for consideration or not, or as a contribution, is not a supply if the acquirer is or becomes a taxable person and continues the taxable activity. The acquirer steps into the transferor's shoes and must correct input VAT under art. 39 if the conditions change. [VAT Law art. 7][law] as replaced by [12/26 art. 2][amend]

### Exemptions

Exempt without input credit, public interest (art. 26): public postal services; health services and care under health insurance rules; social insurance services; pre-school, school and adult education and the supplies linked to them; services and goods of schools and student institutions; cultural services by non-profit bodies; sport services by non-profit bodies; public broadcasting (non-commercial); religious services; NGO services where no distortion of competition is likely.

Other exemptions (art. 27): insurance and reinsurance, including brokers and agents; real property, except the first transfer of a newly built building; residential letting for permanent housing of more than 60 days and letting of registered farm land or forest; banking and financial services (credit, guarantees, deposits, accounts, payments, legal tender, shares and securities, investment fund management; debt collection and safe custody of securities are taxable); valid postage and revenue stamps; gold bought by the Central Bank; games of chance. [VAT Law arts. 26, 27][law]

Input VAT linked to exempt supplies is not deductible, except for 0% supplies under art. 25 and specified financial and insurance services supplied to a recipient established outside Montenegro or linked to exported goods. [VAT Law art. 37(3) to (4)][law]

### Tax point

VAT is due when goods are delivered or services performed, which is the date the invoice is issued. With no invoice, VAT is due 8 days after delivery. An advance received before the invoice or the supply is taxed on the day it is received, on the amount received. For continuous supplies with successive invoices or payments, the tax point is the last day of the period the invoice or payment covers. A change in the base is taxed on the date of the document that records it. Where the recipient is the tax debtor, the tax point is the earlier of receipt of the invoice and payment, or the 8th day after supply if no invoice arrives. [VAT Law art. 18][law]

For imports, VAT arises when customs duty and other import charges arise. [VAT Law art. 19][law]

### Taxable amount

The base is everything the supplier receives or will receive for the supply from the buyer or a third party, including subsidies directly linked to the price. Discounts and amounts paid in another's name and for their account are handled under art. 20. Foreign-currency amounts are converted at the Central Bank of Montenegro middle rate on the tax point date (imports use the customs rate). [VAT Law arts. 20, 23][law]

Import base: the customs value plus excise duties, other taxes and charges payable abroad and on import (except VAT), plus incidental costs (commission, packing, transport, insurance) up to the first destination in Montenegro, less discounts not already excluded. [VAT Law art. 22][law]

Bad debts: the supplier may reduce output VAT only on a final court decision closing bankruptcy, halting enforcement or approving a compulsory settlement, provided the claim was sued before the proceedings began, or where the debtor has been struck off the register. VAT is due again on any later receipt. [VAT Law art. 20a][law] as replaced by [12/26 art. 7][amend]

### Input VAT

A taxable person deducts input VAT on purchases, imports and services received that are used for taxable activity, including activity abroad that would carry a deduction in Montenegro. The deduction needs an invoice meeting art. 32 or a customs declaration and is taken in the period the invoice or declaration is received. [VAT Law art. 37(1), (2), (6), (7)][law]

No deduction for: sport and leisure boats, passenger cars and motorcycles, their fuel, lubricants, spare parts and related services (except vehicles held for resale, rental, taxi or passenger and goods transport, or driving instruction); purchase of a newly built residential building; and representation (entertainment) costs. VAT shown by a person not entitled to charge it, and VAT charged above the correct amount, is not deductible even if paid. A recipient liable under art. 12(1)(2) deducts only if it has accounted for the VAT. [VAT Law art. 37(5), (8) to (10)][law]

Mixed supplies (art. 38): only the part linked to taxable supplies is deductible, and the split is made before the return is filed. The annual proportion is taxable turnover (with a right of deduction) over that amount plus turnover without a right of deduction, including subsidies other than price-linked subsidies. Disposals of equipment and occasional financial and property transactions are left out. The percentage is rounded up to a whole number. The provisional rate for the year uses last year's figures (or an estimate approved in writing by the tax authority) and is corrected in the last period of the year. Separate percentages by business line need written approval and separate books. [VAT Law art. 38][law]

Capital goods: input VAT is corrected if, within 5 years from the year equipment was first used (10 years for property), the conditions that decided the deduction change. A change of conditions includes moving to small-taxpayer status, ceasing activity, and selling equipment or property (other than new buildings) inside the period where the sale is not taxed. No correction where the difference is EUR 30 or less. [VAT Law art. 39][law] as amended by [12/26 art. 12][amend]

A newly registered taxpayer gets a proportional deduction for stock held before registration, set by the tax authority, with no refund on that basis. [VAT Law art. 40][law]

Farmers: a registered buyer of farm or forest products from an unregistered farmer adds 8% flat-rate compensation to the purchase value and may deduct it as input VAT; the farmer needs prior approval from the tax authority. [VAT Law art. 43][law]

### Invoices

A B2B invoice shows at least: date and number; supplier name, address and VAT number; customer name and address; date of supply; quantity and description; net amount; rate; VAT; total. A supplier of services whose place of supply is outside Montenegro writes "prenos poreske obaveze" (transfer of tax liability) on the invoice. A supplier of gas, electricity or heating or cooling to a taxable person who is not the final consumer writes the same words. Exempt and 0% invoices state that no VAT is charged and cite the article. [VAT Law art. 32][law] as amended by [12/26 art. 10][amend]

The VAT number is the PIB with the prefix "ME". The tax authority replaces VAT numbers issued before 12/26 with new numbers of its own motion. [VAT Law art. 55(7)][law]; [12/26 art. 15, new art. 72c][amend]

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Registration application | by the 20th of the month after the month supplies exceeded EUR 30,000 (last 12 months or shorter); otherwise registered by the authority of its own motion | [VAT Law art. 55][law] |
| Registration decision | within 7 days of the application; taxable status starts on the date set in the decision | [VAT Law art. 55(3)][law] |
| Start, change or end of activity | notify the tax authority | [VAT Law art. 55(5)][law] |
| Monthly return (PR PDV-2) | electronically by the 15th of the next month, including nil periods | [VAT Law art. 35][law] |
| Payment | by the 15th of the next month; a recipient liable under art. 12 pays in the same time | [VAT Law art. 36][law] |
| Import VAT | assessed and paid like an import duty under customs rules | [VAT Law art. 36(3)][law] |
| Deregistration | on request if supplies in the last 12 months or calendar year are within the art. 42 limit; of the authority's motion on cessation; output VAT due on stock and goods kept for private use before the decision | [VAT Law art. 56][law] |

Portal: since 12 January 2026 returns are filed in the Tax Administration's IRMS portal at https://irms.tax.gov.me/. The old CRPS and TAXIS portals closed on 31 December 2025. December 2025 VAT returns filed by 30 January 2026 counted as on time; that extension did not move the payment date. [Tax Administration IRMS notice, 30 Dec 2025][irms]

If a return is not filed, or records are missing, the tax authority may estimate the liability from a control, from comparable taxpayers or from other business data. [VAT Law art. 35(6)][law]

### Return rows (PR PDV-2)

| Row | Content |
|---|---|
| 1 to 8 | period (with box for an amended return), PIB, name, activity code, address, authorised person, liquidation date, VAT number |
| 9 | no transactions in the period |
| 10, 11, 12 | taxable supplies (net) at 21%, 15%, 7% |
| 13 | supplies at 0% |
| 14 | exempt supplies |
| 15 | gas, electricity, heating or cooling supplied with transfer of liability |
| 16, 17, 18 | output VAT on domestic supplies at 21%, 15%, 7% |
| 19 | input VAT on domestic purchases |
| 20 | VAT paid on imports |
| 21 | VAT on services from foreign persons (recipient liable under art. 12(1)(2)), in both the output and input columns |
| 22 | 8% flat-rate compensation paid to farmers |
| 23 | VAT on energy supplies where the buyer is the tax debtor |
| 24 | total output VAT: 16 + 17 + 18 + 21 |
| 25 | total input VAT: 19 + 20 + 21 + 22 |
| 26 | input VAT with no right of deduction |
| 27 | deductible input VAT: 25 minus 26 |
| 28 | VAT payable: 24 minus 27 |
| 29 | VAT credit: 27 minus 24 |
| 30 | refund requested for row 29: yes or no (no means carried forward) |

[PR PDV-2 form and instructions][form]

The printed totals in rows 24 and 25 do not include row 23.

## Penalties and interest

Art. 58 (as replaced by 12/26), legal person EUR 3,000 to 10,000, responsible person EUR 800 to 2,000, entrepreneur EUR 1,000 to 4,000, for: a foreign supplier of B2C services taxed in Montenegro that does not set up a permanent establishment or appoint a representative; not issuing an invoice; not displaying the invoice notice at each point of sale; a non-established international road passenger carrier not filing its registration; not filing the VAT return, or filing it late; not filing for a special scheme 15 days before the month it starts; not applying for registration by the 20th of the following month; not notifying start, change or end of activity. [12/26 art. 14][amend]

Art. 59, legal person EUR 6,000 to 20,000, responsible person EUR 1,500 to 2,000, entrepreneur EUR 2,000 to 6,000, for (among the listed offences): not charging VAT at the art. 18 tax point; using a wrong base; not issuing or keeping invoices; missing invoice details; wrong output VAT; not paying VAT by the 15th; wrong input VAT under arts. 37 to 40; charging VAT or deducting in breach of art. 42; not correcting input VAT on property; errors in the second-hand, auction and investment-gold schemes; missing records, invoice books or import VAT records; not keeping records for the retention period; not paying VAT on deregistration. [VAT Law art. 59][law]

For a foreign B2C supplier without a representative and for the art. 59 offences in points 5, 7 and 19 (wrong output VAT, wrong input VAT, deregistration VAT), a ban on carrying on the activity for 30 days to one year may be added. [VAT Law art. 60][law]

Interest: unpaid or underpaid tax carries interest at 0.03% a day until 17 July 2026 and, from 18 July 2026, at 5.4% a year (ECB main refinancing rate plus 3 points, set each half-year; 104/26 arts. 20 and 26 and the Tax Administration decision of 24 July 2026), from the day after the due date; no interest is charged on interest. Overpaid tax earns interest at the same rate. Until 17 July 2026 it ran from the day the refund request was received (from the payment date where the assessment was annulled, changed or revoked). From 18 July 2026 art. 96 as replaced by 104/26 art. 21 says interest is calculated within 30 days of receipt of the request (or of the act annulling the assessment). Appeals, enforcement and interest not covered by the VAT Law follow the Tax Administration Law. [Tax Administration Law arts. 95, 96][tal]; [104/26 Tax Administration Law amendment arts. 20, 21, 26](https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0); [VAT Law arts. 57, 62][law]

## Cross-border points

Place of supply of services (arts. 17 to 17j, as replaced by 12/26):

- B2B general rule: where the recipient taxable person has its seat, or the fixed establishment receiving the service. Foreign legal persons count as taxable persons for this rule.
- B2C general rule: where the supplier has its seat or fixed establishment.
- Property services (including estate agents, valuers, architects and site supervision): where the property is.
- Passenger transport, and goods transport to non-taxable persons: proportionally by distance.
- Admission to events: where the event takes place; online events for consumers: where the consumer lives.
- Restaurant and catering: where performed (on ships, aircraft and trains: where the journey starts).
- Short-term hire of means of transport (30 days, boats 90 days): where made available; long-term hire to consumers: where the consumer lives, with a special rule for leisure boats.
- Intermediary services to consumers: where performed (property intermediaries: where the property is). Ancillary transport services and valuations of or work on movable goods for consumers: where performed.
- Telecom, broadcasting and electronic services to consumers: where the consumer has its seat or residence.
- Intellectual property, advertising, consultants, engineers, lawyers, auditors, translators, banking, finance and insurance, staffing, movable goods hire and energy network access to consumers: where the consumer has its seat or residence.
- Use and enjoyment: for the services in arts. 17c(2), 17f(3) to (4), 17g(1) and 17i, the place of supply is where the service is actually used, to avoid double or non-taxation; for telecom, electronic and advertising services to taxable persons the same applies.

[VAT Law arts. 17 to 17j][law] as inserted by [12/26 arts. 5, 6][amend]

Services bought from abroad: where the place of supply is Montenegro and the non-established supplier has no tax representative, the Montenegrin recipient is the tax debtor (row 21). It accounts output VAT and deducts it as input VAT if the purchase is for taxable supplies. [VAT Law arts. 12(1)(2), 37(10)][law]; [form][form]

Foreign B2C suppliers: a supplier of services whose place of supply is in Montenegro because the non-taxable customer is there must set up a permanent establishment or appoint a representative in Montenegro. Art. 42 (the EUR 30,000 small-taxpayer limit) does not apply to taxpayers established abroad. [VAT Law arts. 12(2), 42(4)][law]; [12/26 art. 3][amend]

Services supplied abroad: an invoice for services whose place of supply is outside Montenegro carries "prenos poreske obaveze". Input VAT on costs used for activity abroad is deductible if it would be deductible for the same activity in Montenegro. [VAT Law arts. 32(7), 37(2)][law]

Exports: goods count as exported when they actually leave Montenegro or enter a free zone or customs warehouse for export. A foreign customer or a foreign payment alone does not make a supply 0%. [VAT Law art. 25(3)][law]

International road passenger transport by a non-established carrier: online registration with the tax authority (confirmation within 48 hours) and a VAT return for each period of operation, unless a tax treaty with the carrier's state exempts it. [VAT Law arts. 35a, 35b][law]

Refunds to non-established businesses: a business established abroad may reclaim Montenegrin input VAT on purchases and imports used for its foreign activity, if in the period it made no supplies in Montenegro other than services linked to imports and exports under arts. 22(2)(2), 25 and 30 and services on which the recipient pays the VAT. Detailed conditions, deadlines and minimum amounts are set by the Ministry of Finance. [VAT Law art. 51][law]

Travellers: individuals with no permanent or temporary residence in Montenegro may reclaim VAT on goods they take out of the country, except mineral oils, alcohol and tobacco. [VAT Law art. 52][law]

EU accession law: the new VAT Law (Official Gazette 104/26, 17 July 2026) entered into force on the eighth day after publication but applies only from the day Montenegro joins the EU; on that day it repeals the current law. Nothing in it applies to 2026 transactions. Its implementing acts are due within one year of entry into force. [104/26 arts. 211 to 213][future]

## Worked examples

October 2026, EUR. Classification, tax point and deduction evidence are given as facts of each example.

### 1. Three rates on one return

A registered business has gross supplies of 12,100 at 21%, 11,500 of hotel accommodation at 15% and 1,070 of milk and dairy products at 7%. Domestic input VAT is 900 and import VAT paid is 400; 300 of the domestic input VAT is on a passenger car, which is blocked. No reverse charge, energy or farmer transactions.

Net values: 12,100 / 1.21 = 10,000 (row 10); 11,500 / 1.15 = 10,000 (row 11); 1,070 / 1.07 = 1,000 (row 12). Output VAT 2,100 + 1,500 + 70 = 3,670 (row 24). Gross input 900 + 400 = 1,300 (row 25); blocked 300 (row 26); deductible 1,000 (row 27). Payable 3,670 minus 1,000 = 2,670 (row 28), filed and paid by the 15th of November. [VAT Law arts. 24, 24a, 37(5)][law]; [form][form]

```oa-check
name: Montenegro three rate ordinary VAT return
inputs:
  standard_gross: 12100
  accommodation_gross: 11500
  basic_food_gross: 1070
  domestic_input_vat: 900
  import_vat_paid: 400
  restricted_input: 300
steps:
  - row_10: standard_gross / 1.21
  - row_11: accommodation_gross / 1.15
  - row_12: basic_food_gross / 1.07
  - row_16: standard_gross - row_10
  - row_17: accommodation_gross - row_11
  - row_18: basic_food_gross - row_12
  - row_24: row_16 + row_17 + row_18
  - row_25: domestic_input_vat + import_vat_paid
  - row_27: row_25 - restricted_input
  - payable: row_24 - row_27
expected:
  row_10: 10000
  row_11: 10000
  row_12: 1000
  row_16: 2100
  row_17: 1500
  row_18: 70
  row_24: 3670
  row_25: 1300
  row_27: 1000
  payable: 2670
```

### 2. Advance and final invoice

A contract totals 24,200 gross at 21%. An advance of 6,050 was received in an earlier month and taxed on receipt. The final invoice is issued in October. VAT on the whole contract is 24,200 minus 20,000 = 4,200; VAT already paid on the advance is 6,050 minus 5,000 = 1,050; October output VAT is 3,150. (Not a new building or building land, so the art. 72b transition does not apply.) [VAT Law arts. 18(4), 24][law]

```oa-check
name: Montenegro advance final invoice reconciliation
inputs:
  contract_gross: 24200
  prior_advance_gross: 6050
  rate: 0.21
steps:
  - contract_net: contract_gross / (1 + rate)
  - full_contract_vat: contract_gross - contract_net
  - advance_net: prior_advance_gross / (1 + rate)
  - prior_advance_vat: prior_advance_gross - advance_net
  - final_period_vat: full_contract_vat - prior_advance_vat
expected:
  contract_net: 20000
  full_contract_vat: 4200
  advance_net: 5000
  prior_advance_vat: 1050
  final_period_vat: 3150
```

### 3. Import VAT base

Customs value is 20,000. Customs duty is 1,000 (a figure given for the example, not a tariff rate). Freight and insurance to the first destination in Montenegro, not already in the customs value, are 500. The goods are standard rated. Base 21,500; import VAT 4,515, deductible in row 20 in the period the customs declaration is received, if the goods are for taxable supplies. [VAT Law arts. 22, 24, 37(6) to (7)][law]

```oa-check
name: Montenegro import VAT base and recovery input
inputs:
  customs_value: 20000
  assumed_duty: 1000
  additional_ancillary_costs: 500
  vat_rate: 0.21
steps:
  - import_vat_base: customs_value + assumed_duty + additional_ancillary_costs
  - import_vat_assessed: import_vat_base * vat_rate
  - eligible_paid_import_input: import_vat_assessed
expected:
  import_vat_base: 21500
  import_vat_assessed: 4515
  eligible_paid_import_input: 4515
```

### 4. Reverse charge with partial recovery

A registered Montenegrin business buys a consultancy service for 2,400 from a foreign firm with no representative in Montenegro. Under art. 17(2) the place of supply is Montenegro, so the recipient is liable. Its annual deduction percentage is 60%. Row 21 output 504; row 21 input 504; deductible 302.40; 201.60 goes to row 26. Net VAT cost 201.60. [VAT Law arts. 12(1)(2), 17(2), 18(8), 37(10), 38][law]; [form][form]

```oa-check
name: Montenegro recipient service VAT partial recovery
inputs:
  service_base: 2400
  vat_rate: 0.21
  established_recovery_fraction: 0.60
steps:
  - row_21_output: service_base * vat_rate
  - row_21_gross_input: row_21_output
  - eligible_input: row_21_gross_input * established_recovery_fraction
  - row_26_disallowed_part: row_21_gross_input - eligible_input
  - net_vat_cost: row_21_output - eligible_input
expected:
  row_21_output: 504
  row_21_gross_input: 504
  eligible_input: 302.40
  row_26_disallowed_part: 201.60
  net_vat_cost: 201.60
```

### 5. Annual pro rata, rounded up

After the art. 38 exclusions, annual turnover with a right of deduction is 65,001 and other turnover in the denominator is 34,999. 65,001 / 100,000 = 65.001%, rounded up to 66%. Shared input VAT 1,000 gives 660 deductible; with 200 of directly attributable deductible input, total deductible is 860. Gross input including 100 attributable to exempt supplies and 50 blocked is 1,350, so 490 is not deductible. The blocked and exempt-only inputs are kept out of the pro rata. [VAT Law arts. 37, 38(3) to (5)][law]

```oa-check
name: Montenegro shared input upward rounded annual proportion
inputs:
  credit_bearing_turnover: 65001
  other_denominator_turnover: 34999
  shared_input: 1000
  directly_deductible_input: 200
  directly_exempt_input: 100
  restricted_input: 50
steps:
  - denominator: credit_bearing_turnover + other_denominator_turnover
  - rounded_percent: ceil(credit_bearing_turnover / denominator * 100)
  - shared_deductible: shared_input * rounded_percent / 100
  - total_deductible: directly_deductible_input + shared_deductible
  - gross_input: shared_input + directly_deductible_input + directly_exempt_input + restricted_input
  - total_nondeductible: gross_input - total_deductible
expected:
  denominator: 100000
  rounded_percent: 66
  shared_deductible: 660
  total_deductible: 860
  gross_input: 1350
  total_nondeductible: 490
```

### 6. Credit, offset against other tax debts

Deductible input VAT is 5,000 and output VAT 1,800: credit 3,200 (row 29). The taxpayer has 700 of other taxes past their due date. If it ticks "yes" in row 30, the refund is reduced by that debt, leaving 2,500, paid within 60 days of the return (30 days if it mainly exports or has shown an excess in more than three consecutive returns). [VAT Law art. 50(1) to (3)][law]; [form][form]

```oa-check
name: Montenegro excess input and due other tax offset
inputs:
  eligible_input: 5000
  output_tax: 1800
  confirmed_due_other_taxes: 700
steps:
  - vat_credit: max(0, eligible_input - output_tax)
  - offset: min(vat_credit, confirmed_due_other_taxes)
  - credit_after_offset: vat_credit - offset
expected:
  vat_credit: 3200
  offset: 700
  credit_after_offset: 2500
```

## Ask the client first

1. Is the business registered for VAT, from what date, and what were its supplies month by month for the last 12 months? (Registration duty, art. 42 status, first return.)
2. What exactly does it sell, and to whom? For food, accommodation, catering, medicines and publications the rate depends on the exact product and establishment (0%, 7%, 15% or 21%).
3. Does it buy services from abroad or sell services to foreign customers, and are the customers businesses or consumers? (Place of supply, row 21, foreign-supplier representative duty.)
4. Does it make exempt supplies (letting, financial, insurance, health, education, property)? (Pro rata and the provisional percentage from last year.)
5. Does it buy or sell new buildings, building land, gas or electricity, or buy from unregistered farmers? (Art. 72b transition, energy reverse charge, 8% compensation.)
6. Is there a VAT credit from earlier months, any other tax overdue, and does it want a refund or carry-forward? (Art. 50 and row 30.)

## Sources

| Source | URL | Read on |
|---|---|---|
| Law on Value Added Tax, consolidated text through Official Gazette 12/26, arts. 3 to 4, 7, 12 to 25, 26 to 28, 32 to 40, 42 to 43, 50 to 63 | https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0 | 2026-10-30 |
| Law amending the Law on VAT, Official Gazette 12/26 (6 Feb 2026), arts. 1 to 16 incl. new arts. 72b and 72c | https://wapi.gov.me/download/80b15e7e-da28-49b7-9ca6-de1849b9ab61?version=1.0 | 2026-10-30 |
| Law on Value Added Tax, Official Gazette 104/26 (17 Jul 2026), arts. 211 to 213 (application from EU accession) | https://wapi.gov.me/download/a7c33b8f-aa74-4197-b1fa-317ea466161f?version=1.0 | 2026-10-30 |
| Law amending the Law on VAT, Official Gazette 49/22 (6 May 2022), arts. 2 and 4 (art. 25(1)(12d) and its end on 31 Dec 2022, art. 71e) | https://www.sluzbenilist.me/propisi/333002/download | 2026-10-30 |
| Law amending the Law on VAT, Official Gazette 65/22 (21 June 2022), arts. 2 and 3 (bread added to 12d; art. 71f, end on 31 Dec 2022) | https://www.sluzbenilist.me/propisi/338064/download | 2026-10-30 |
| Law amending the Law on VAT, Official Gazette 94/24, arts. 1 (new art. 24a), 3 (new art. 28), 4 (farmer compensation 8%), 5 (art. 71i) and 6 (applies from 1 Jan 2025) | https://www.sluzbenilist.me/propisi/373704/download | 2026-10-30 |
| Tax Administration, form PR PDV-2 and filling instructions | https://wapi.gov.me/download/e3d2b1f2-341b-487e-8e2a-d77868bbf52e?version=1.0 | 2026-10-30 |
| Tax Administration, notice on the start of IRMS (30 Dec 2025) | https://www.gov.me/clanak/vazno-obavjestenje-u-vezi-sa-pocetkom-primjene-novog-integrisanog-it-sistema-poreske-uprave-irms | 2026-10-30 |
| Law on Tax Administration, consolidated text through Official Gazette 160/25 (before 104/26), arts. 95 to 97 | https://wapi.gov.me/download/6bf4fd6a-fa32-4c33-9f5a-3a13ae509233?version=1.0 | 2026-10-30 |
| Law amending the Tax Administration Law, Official Gazette 104/26 (17 July 2026), arts. 20 (new art. 95 rate: ECB + 3 points), 21 (new art. 96, interest on overpaid tax) and 26 (in force the next day) | https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0 | 2026-10-30 |
| Tax Administration decision on the default interest rate for 18 July to 31 December 2026 (5.4% a year) | https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0 | 2026-10-30 |

Not yet confirmed: the Ministry of Finance lists of goods and services at 7% and 15% (art. 24a(3)) in their current version; whether the 2026 Budget Law used the art. 63 power to change a VAT rate; the current IRMS electronic return layout against the PR PDV-2 form (published December 2024), including how energy row 23 enters the totals; the rulebooks for refunds (art. 50(5)), non-established business refunds (art. 51) and traveller refunds (art. 52), including deadlines and minimum amounts; from when interest on overpaid tax runs under the 30-day wording of art. 96 as replaced by 104/26 art. 21; the computation method for capital goods corrections under art. 39 and the Ministry rulebook on the pro rata (art. 38(8)); the special schemes for travel agents (art. 44), second-hand goods, art and antiques (arts. 45 to 47), auctions (arts. 48 to 49) and investment gold (art. 49a); the procedure and time limit for an amended return; the date of EU accession that starts the 104/26 law.

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
