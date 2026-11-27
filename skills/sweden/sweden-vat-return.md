---
name: sweden-vat-return
description: >
  Use this skill whenever asked to prepare, review, or classify transactions for
  a Swedish VAT return (momsdeklaration) for a self-employed individual or small
  business in Sweden. Trigger on phrases like "prepare VAT return", "do the
  Swedish VAT", "momsdeklaration", "moms", "skattedeklaration", or any request
  involving Swedish VAT filing. Also trigger when classifying transactions for
  VAT purposes from bank statements, invoices, or other source data. Covers the
  25%, 12% and 6% rates for 2026, including food at 6% from 1 April 2026 and 12%
  from 1 January 2028, ruta 05 to 62, periods, deadlines, skattetillägg and the
  Lämna momsdeklaration e-service. Load alongside vat-workflow-base and
  eu-vat-directive. ALWAYS read this skill before touching any Swedish VAT work.
  This Tier 2 draft supports source checking and reviewer questions; it does not
  authorise filing, payment or a tax position.
version: 2.5
jurisdiction: SE
tax_year: 2026
tax_year_notes: "Calendar 2026 VAT periods. Rate changes follow the tax point: food 12% through 31 March, 6% from 1 April 2026; enacted 12% restoration 1 January 2028. Dance admission 6% from 1 July 2026. Future-effective provisions are not applied early."
last_updated: 2026-11-27
job: vat-return
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: vat-gst
type: filing-howto
---

# Sweden VAT Return v2.5
> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Self-employed individuals and small businesses registered for VAT in Sweden under Mervärdesskattelag (2023:200) ('ML') and Skatteförfarandelag (2011:1244) ('SFL'), and the reviewers working with them. Skatteverket (Swedish Tax Agency) administers the tax. The return is the momsdeklaration, in SEK only. Legacy text also calls it the skattedeklaration, which is SFL's term.

Calendar 2026 VAT periods; operative provisions checked on 27 November 2026. Use the text effective at the tax point, including the transitional rules of SFS 2026:118, 2026:119 and 2026:841. The current ML consolidation also prints provisions taking effect in 2027; those do not apply early.

Load alongside `vat-workflow-base` and `eu-vat-directive`. This Guide supplies the Swedish return rules. Do not invent a refusal code or treat a missing companion section as a tax-law rule.

### Refusals and boundaries

The ordinary registered-business matrix below remains usable. For each following specialist situation, hold the specified calculation or filing outcome; do not insert a guessed amount. Say: **Check this point with one of our partner accountants.**

- R-SE-1: a VAT-group consolidated return.
- R-SE-2: a non-resident registration using a fiscal representative, including the representative's obligations.
- R-SE-3: a mixed taxable/exempt shared-cost allocation whose reasonable basis has not been established. The deduction rule and the statutory full-deduction exceptions are below.
- R-SE-4: any claimed agricultural/forestry flat-rate scheme; this Guide does not establish that a domestic scheme exists.
- R-SE-5: entering/leaving voluntary property taxation or a property capital-goods transfer requiring adjustment/takeover.
- R-SE-6: travel-agent or second-hand/art margin computation; the return still identifies ruta 07.
- R-SE-7: income-tax/ROT/RUT entitlement rather than the VAT base; use the income-tax Guide.

Other narrow holds: a cinema admission rate; a claimed exempt medical-aid category beyond the proved prescription-medicine rule; the historical SEK 500 staff-gift VAT cap; the historical SEK 33 representation shortcut for 6% takeaway food; disputed cross-transition credits without the original invoice/tax-point evidence. These specific outcomes are non-usable here. **Check this point with one of our partner accountants.**

### Working limits

Covered: a business registered for VAT that reports under the normal rules. Not covered: the rules for a business that is not registered. An enterprise under the small business exemption files no momsdeklaration, but it reports VAT it charged in error on form SKV 4702 (Skatteverket), and buying construction services under reverse charge can require it to register. Say so and stop, rather than prepare a return.

### Required inputs

| Level | Items | Policy |
| --- | --- | --- |
| Minimum | Bank statement for the whole period, as CSV, PDF or pasted text, from any bank: Handelsbanken, SEB, Swedbank, Nordea SE, Danske Bank SE, Länsförsäkringar, Revolut Business, Wise Business or any other. | No bank statement: stop. |
| Recommended | Sales invoices, especially EU sales and exports; purchase invoices for every input VAT claim; organisationsnummer and momsregistreringsnummer. | Bank statement only: proceed, but every ruta 48 amount is Needs Input until the document is seen. Record in the reviewer brief: 'This momsdeklaration was produced from bank statement alone. The reviewer must verify that each input VAT claim is supported by a document ML 13 kap. 31 to 36 §§ accepts and that reverse charge classifications match.' |
| Ideal | Complete invoice register, prior period momsdeklaration, skattekonto statement. | Use for reconciliation. |

The legacy SEK 2,000 review level stays only as a red flag setting. ML sets no such floor on the evidence rule.

## Rates, bands and thresholds

| Item | Amount or rule | Position for calendar 2026 | Source and limit |
| --- | --- | --- | --- |
| Standard rate | 25% | Enacted, in force. Applies unless ML 9 kap. 4 to 19 §§ give a lower rate. From 1 January 2028 the cross-reference reads 3 to 18 §§ (Lag 2026:119). | ML 9 kap. 2 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Hotel room letting and camping | 12% | Enacted, in force | ML 9 kap. 4 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Restaurant and catering services | 12%, excluding the part for spirits, wine and starköl | Enacted, in force | ML 9 kap. 5 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Art | 12% on delivery and EU acquisition of art under 20 kap. 7 § not under the margin scheme, and on import of art, collectibles and antiques under 20 kap. 7 to 9 §§ | Enacted, in force | ML 9 kap. 6 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Minor repairs | 12% on repairs of bicycles, shoes, leather goods, clothes and household linen | Enacted, in force | ML 9 kap. 7 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Passenger transport | 6%, except transport where the travel element is of subordinate importance | Enacted, in force | ML 9 kap. 8 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Books, newspapers and similar | 6% under ML 9 kap. 9 to 13 §§: books and similar, subject to 10 kap. 20 and 21 §§ and not wholly or mainly advertising; programmes and catalogues; radio and cassette newspapers; accessible goods; electronic equivalents not wholly or mainly advertising, moving image or audible music | Enacted, in force | ML 9 kap. 9 to 13 §§, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Culture and nature | 6% on admission to concerts, circus, theatre, opera, ballet or other similar performances; admission to dance events; admission to and showing of zoos; showing of nature areas outside tätort, national parks, nature reserves, national city parks and Natura 2000 areas | Enacted, in force from 1 July 2026 (Lag 2026:841). Older rules for an earlier tax point; Skatteverket says dance events were 25% to 30 June 2026. Cinema admission is a separate narrow hold above. | ML 9 kap. 14 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Libraries and museums | 6% where not exempt under 10 kap. 30 § items 2 and 4 | Enacted, in force | ML 9 kap. 15 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Copyright | 6% on the rights in 9 kap. 16 and 17 §§. 9 kap. 16 § second paragraph excludes photographs, advertising, computer programs, and film or video with information, which stay at 25%. | Enacted, in force | ML 9 kap. 16 and 17 §§, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Sport | 6% on sport under 10 kap. 28 § not exempt under 10 kap. 29 §. Exempt where supplied by the state, a municipality or a non-economic association under 4 kap. 6 §. | Enacted, in force | ML 9 kap. 18 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Food from 1 April 2026 | 6% on food under Article 2 of the EU Food Regulation, except (1) water under Article 6 of the drinking water directive and (2) spirits, wine and starköl. Water bottled or in containers for sale is 6%. | Enacted, in force from 1 April 2026 (Lag 2026:118). Older rules, 12% on Skatteverket's statement, for a tax point before that date. | ML 9 kap. 19 § and transitional note 2026:118, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Food from 2028 | 12% on the same food with the same exceptions, moved to ML 9 kap. 3 § | Enacted, not yet in force: applies from 1 January 2028 (Lag 2026:119). Older rules for an earlier tax point. | ML 9 kap. 3 § marked I:2028-01-01, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Exempt with right to deduct | No output VAT, input VAT deductible: the list in ML 13 kap. 10 §, including medicines under 10 kap. 13 §, EU supplies and exports. ML has no 'zero rate'. | Enacted, in force | ML 13 kap. 10 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Small business exemption | Turnover not above SEK 120,000 in the calendar year and not above it in either of the 2 preceding years | Enacted, in force (Lag 2024:942). Skatteverket says the seat must be in Sweden. | ML 18 kap. 4 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| EU small business scheme | EU turnover at most EUR 100,000 in the current and preceding calendar year, plus the Swedish current/prior-two-year test and home-state identification | Enacted, in force. A seat outside the EU cannot use it. | ML 18 kap. 5 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Artist's own art | Exempt only while the bases are strictly below SEK 300,000 and (1) the author or estate makes the supply, (2) the author or estate owns the work at supply and (3) the bases for the tax year are together below SEK 300,000. On request, Skatteverket decides that the supplies are taxable whatever the bases, to the end of the second year after the decision year. At SEK 300,000 exactly the statutory exemption is already unavailable; the ordinary art rate is 12% outside the margin scheme. | Enacted, in force | ML 10 kap. 31 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| EU distance sales limit | SEK 99,680 | Enacted, in force. Conditions under 'Cross-border points'. | ML 6 kap. 62 to 64 §§, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Period bands | SEK 40 million and SEK 1 million of estimated tax base for the tax year, excluding EU acquisitions and imports | Enacted, in force | SFL 26 kap. 10 to 13 §§, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Cash method | Annual turnover normally at most SEK 3 million | Enacted, in force | ML 7 kap. 16 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Listed electronics | Buyer pays on mobile phones (apparatus made or adapted for use in an authorised network on specified frequencies, whether or not it has other uses), integrated circuits not built into end products, consoles, tablets and laptops where both parties are taxable persons who are or must be registered here, the base for these goods in an invoice is together above SEK 100,000, and the buyer's registration duty is not merely a consequence of the purchase | Enacted, in force | ML 16 kap. 16 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Capital goods | Input tax of at least SEK 50,000 (machines, inventory and the like) or at least SEK 100,000 (property). The test is input tax, not cost. | Enacted, in force | ML 15 kap. 4 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Representation, statutory cap | Tax on at most SEK 300 per person and occasion, excluding VAT | Enacted, in force | ML 13 kap. 25 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Representation, administered amounts | SEK 36 (12%); SEK 46 flat with the conditions below; SEK 180 peripheral costs; SEK 300 gifts | Skatteverket practice. SEK 18 is arithmetic (6% of 300), not a published figure. | https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/avdragformomsvidrepresentation.4.15532c7b1442f256baec84b.html |
| Hired cars | Half of the VAT on hire, where use in deductible activity is more than trivial. Skatteverket reads this as more than 100 mil a year, prorated. | 50% enacted; 100 mil is Skatteverket practice | ML 13 kap. 22 §; https://www.skatteverket.se/foretag/moms/sarskildamomsregler/bilarochmoms.4.58d555751259e4d6616800010628.html |
| Mixed use, 95% rule | Full deduction if the purchase is more than 95% for deductible transactions, or if the tax is at most SEK 1,000 and deductible consideration is more than 95% | Enacted, in force | ML 13 kap. 30 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Late filing fees | SEK 625; SEK 1,250 after a föreläggande; periodisk sammanställning SEK 1,250 | Enacted, in force | SFL 48 kap. 1, 5 and 6 §§, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Skattetillägg | 20%; 2% or 5% for period errors | Enacted, in force | SFL 49 kap. 11 and 13 §§, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Interest | Basränta 2.5%; low 2.5%; high 17.5%; income 1.125% | Method enacted; figures are Skatteverket's published amounts, with basränta 2.5% from 1 December 2024 | SFL 65 kap. 3, 4 and 13 §§; https://www.skatteverket.se/privat/skatter/skattekontobetalaochfatillbaka/rantapaskattekontot.4.18e1b10334ebe8bc80002582.html |

Register before starting where SFL 7 kap. 1–2 §§ require it. The Swedish-seat SME exemption is automatic for an unregistered business only while Swedish annual turnover is at most SEK 120,000 in the current year and each of the preceding two years. A registered business needs a decision to use the exemption (ML 18 kap. 8–9 §§). Count turnover under 18 kap. 19–23 §§, including specified exempt/export/financial/property transactions unless merely incidental; exclude fixed-asset disposals. A taxable election is possible under 15 §. The exemption ends from the supply crossing the threshold (11 §); do not charge VAT on exempt invoices and state the exemption (41 §; Skatteverket). There is no ordinary input deduction on these exempt sales (14 §).

For an establishment in another EU country, the Swedish current/prior-two-year limit still applies, plus EU turnover at most EUR 100,000 in both the current and preceding year and identification by the home authority (5 §). A non-EU establishment cannot use this exemption. The exclusions in 6–7 §§ include taxable own-art supplies, voluntarily taxed property/investment-gold supplies, new means of transport and specified own-use transfers. Low turnover does not remove a separate obligation to register for foreign reverse-charge services, qualifying EU service sales, EU goods acquisitions or construction reverse charge. For persons making only non-credit/non-refund supplies and non-taxable legal persons, the ordinary-EU-goods acquisition threshold is SEK 90,000, subject to the current/prior-year acquisition test and exclusions for new transport/excise goods (ML 3 kap. 6–9 §§); confirm that screen before preparing an exempt-business return.

From 1 July 2026 SFL 7 kap. 10–12 §§ permit refusal/deregistration where registration is used wholly or almost wholly for VAT evasion or the specified clear risk exists, and showing a VAT number invalid where the specified evasion risk exists. This follows enacted SFS 2026:707, not a bill.

## The base

### Momsdeklaration boxes

Skatteverket's page calls these fält; the file guide calls them Ruta. Legacy text used ruta, kept here.

| Ruta | Meaning |
| --- | --- |
| 05 | Taxable sales not in 06 to 08, including sale of inventory with deduction and EU buyers that do not qualify |
| 06 | Taxable uttag (own use) and revaluation |
| 07 | Margin base, 0 if negative |
| 08 | Rent under voluntary taxation |
| 10, 11, 12 | Output VAT at 25%, 12% and 6% on 05 to 08, including prepayments |
| 20 | Goods from another EU country, except a middleman's purchase, which goes in 37 |
| 21 | Services from another EU country, main rule |
| 22 | Main-rule services from outside the EU for which the buyer is liable |
| 23 | Goods bought in Sweden where the buyer is liable |
| 24 | Other services bought in Sweden where the buyer is liable |
| 30, 31, 32 | Output VAT at 25%, 12% and 6% on 20 to 24 |
| 35 | Goods sold to another EU country |
| 36 | Goods sold outside the EU, including prepayments when received |
| 37 | Middleman purchase in a triangular trade |
| 38 | Middleman sale in a triangular trade |
| 39 | Services to a taxable person in another EU country, main rule |
| 40 | Other services sold abroad, including to non-EU buyers and non-main-rule services |
| 41 | Sales where the buyer is liable in Sweden |
| 42 | Other sales not in another field: qualifying exempt sales, assembly deliveries, exempt rent, qualifying asset sales without deduction, prescription medicines; insurance compensation/grants not consideration for supplies |
| 48 | Deductible input VAT. Reduce earlier deductions for a credit note; if total input is negative, report the repayment with the required sign. |
| 49 | Sum of 10, 11, 12, 30, 31, 32, 60, 61 and 62, less 48. Always filled, 0 if nil. |
| 50 | Import base: customs value in SEK, duty and charges, and ancillary costs to the destination |
| 60, 61, 62 | Output VAT on imports at 25%, 12% and 6% |

Legacy text used 06 to 08 for sales by rate, 22 and 23 for non-EU goods and services, 36 for EU services and 37 for exports. Those mappings are wrong and are replaced above. A positive ruta 49 is payable and a negative one refundable.

### Output VAT

Sales at every rate go in ruta 05 unless they belong in 06 to 08, with output VAT in 10, 11 or 12 by rate.

**Food or restaurant service.** Skatteverket assesses the whole sale, from what the customer actually gets.

- Food without support services is 6%, including takeaway, food truck sales and ready food in shops.
- Food or drink with services that let the customer eat straight away, such as serving, table setting, dishwashing or premises with tables and chairs, is a restaurant service at 12%. Catering with those support services at the customer's premises is 12%.
- One purchase can carry both: bread taken away at 6%, coffee in the café at 12%.
- Spirits, wine, beer stronger than folköl, drinks containing spirits and tap water are 25%. Split mixed sales.
- Delivery by a separate firm is a separate service at 25%. The seller's own packaging and transport take the food's rate. Optional disposables are 25%.
- A single-purpose lunch voucher takes its rate by use; a multi-purpose voucher takes the rate on redemption.
- Conference packages with meals are 25%; hotel breakfast is 12%. Breakfast, parking, phone, sauna and laundry inside a room price are 12%, otherwise take their own rate. Parking is 25% unless subordinate. Goods transport is 25%. Recharged travel costs take the rate of the main supply.

**Exempt sales.** These go in ruta 42. They are not left off the return, as legacy text said. ML 10 kap.: post (4 and 5 §§); health care (6 to 13 §§, with 10 § listing taxable items such as glasses, pharmacist goods and animal care); social care (14 §); education (15 to 18 §§); groups (19 §); sport (28 and 29 §§); culture (30 and 31 §§); insurance (32 §, Skatteverket: car hire with compulsory insurance is taxable at 25%); banking and finance (33 §, excluding notary, debt collection, factoring administration and safe deposit); property (35 and 36 §§, with 12 taxable limbs). This category list is navigation, not proof that a particular sale is exempt. Record the precise statutory exemption and its conditions from the invoice and service facts; a healthcare label, a financial-advice label or an authority name is insufficient. Where an exemption condition is unresolved, hold that transaction and say: Check this point with one of our partner accountants. Test R-SE-3 for shared costs only after determining the actual taxable/exempt activities.

**Uttag.** A car's private use is an uttag where its value is more than trivial and either (1) input VAT on acquisition was deductible in whole or part or (2) on hire the whole input VAT on rent was deductible (ML 5 kap. 31 §). A half deduction on hire therefore gives no uttag. The base is under 8 kap. 7 §.

### Input VAT

Deduct input VAT for the taxable business (ML 13 kap. 6 §), in ruta 48, subject to the following.

**Evidence.** Deduction must be substantiated (13 kap. 31 §) by an invoice (32 §). No invoice is needed under 33 § only if all 3 conditions are met: (1) there are special reasons, (2) other documentation can substantiate the deduction and (3) the tax relates to an EU acquisition or to reverse charge under 16 kap. 6 § or 8 to 16 §§. Import needs the import document and evidence of the importer (35 §). With no accepted document, there is no deduction. This default is fixed by the law: disclose it.

**Representation (ML 13 kap. 24 and 25 §§ with IL 16 kap. 2 §).** ML 13 kap. 25 § allows input VAT on meals if (1) the cost has an immediate connection to the business, such as starting or keeping business relations, (2) it is reasonable, and (3) the deduction is at most the tax on SEK 300 per person and occasion, excluding VAT. Legacy 'alcohol never deductible' is the income tax result; Skatteverket counts alcohol for VAT.

- Food and non-alcoholic drink at 12%: up to SEK 36 per person. At 6%: up to SEK 18 by arithmetic.
- Food and alcohol above SEK 300: split the capped base by actual net cost, apply the food rate to the food share and 25% to the alcohol share.
- Or the flat amount: SEK 46 per person if cost is above SEK 300 net per person and VAT is at least SEK 46 per person; the unproved SEK 33 shortcut for 6% food is held above; use the supported proportionate cap instead.
- Staff party: food cap SEK 300. Peripheral costs, theatre and green fees: SEK 180 net per person. Representation gifts: SEK 300 net per person.
- Record attendees and purpose. The SEK 60 simple refreshment amount is income tax, not VAT.

**Cars (ML 13 kap. 20 to 23 §§ with 2 kap. 17 §).** Personbil includes a van-body truck or a bus of at most 3,500 kg total weight, unless the truck's cab is a separate body unit (2 kap. 17 §, first paragraph). For ML 5 kap. 31 §, 7 kap. 25 §, 8 kap. 7 § and 13 kap. 20 to 23 §§ it excludes a personbil klass II above 3,500 kg, or at most 3,500 kg with a separate cab (second paragraph). Skatteverket also counts a car with at most 8 seats beside the driver's, mainly built for carrying people. It says a motorhome above 3,500 kg or with a separate cab, or a flatbed truck with a separate cab, is not one.

- Purchase: no deduction, except resale, hire-out, taxi under Lag (2012:211), transport of the deceased and driver training.
- Hire: no deduction, except full deduction for hire-out, taxi, the deceased and driver training; half the VAT where the car is hired for other purposes and used more than trivially in deductible activity, regardless of the share of use (13 kap. 22 §).
- Short hire is also 50%; hire for car dealing is 50%. A finance lease clearly showing a sale is treated as a purchase (Skatteverket).
- Running costs: fuel, service, repair and inspection are deductible if the car is in inventory or hired, with no apportionment for part use (13 kap. 23 §; Skatteverket). Otherwise only costs of deductible driving.
- Extra equipment, such as winter tyres, a towbar or a roof box, is deductible. Motorcycles are treated similarly; mopeds and snowmobiles are not covered (Skatteverket).
- A staff car with salary deduction: output is 20% of the deduction at 25% (Skatteverket).

Legacy 'exclusive business use gives full deduction' is wrong and is removed.

**Other limits.** Private use: no deduction (Skatteverket). Permanent housing: no deduction (13 kap. 26 §), except tax relating to (1) inputs for services under 5 kap. 32 to 34 §§ taxed as uttag and (2) a jordbruksarrende, including its dwelling part (27 §). Home office: Skatteverket says purchases connected with the home normally give no deduction, but a workplace wholly separated from the home and specially adapted to the business does. Mixed property: 13 kap. 13 to 15 §§. Private and business use of one asset: Skatteverket gives 3 options (full deduction with uttag, private portion excluded, or proportional). Pre-start purchases can be deductible where bought with the intention of use only in the taxable business, with accepted evidence; a later change from a private purpose does not qualify. Foreign VAT is never in ruta 48: claim a refund from that country. Staff gifts: the historical SEK 500 VAT cap is a narrow non-usable hold above.

**Apportionment.** ML 13 kap. 29 § requires deduction only for the part that is deductible, or by reasonable division if the part cannot be fixed. Skatteverket accepts division by turnover, time or area, documented. 13 kap. 30 § is in the rates table. See R-SE-3.

### Reverse charge in Sweden (ML 16 kap.)

| Rule | Who pays | Boxes |
| --- | --- | --- |
| Goods, or services connected to property in Sweden, where the buyer is registered here and the supplier is a taxable person not established here (6 §). Not property services under 13 § or 12 kap. The supplier may ask to be liable instead, for all such supplies (7 §). | Buyer | 23 or 24, 30 to 32, 48 |
| Electricity, gas, heating or cooling under 6 kap. 21 to 28 §§, where the buyer is registered here and the supplier is a taxable person not established here (8 §) | Buyer | 23, 30, 48 |
| Services under 6 kap. 33 § from a taxable person not established in Sweden (9 §). Buyer is (1) a taxable person, (2) a non-taxable legal person registered here, or (3) a legal person that would be taxable but for 4 kap. 6 § | Buyer | 21 or 22, 30 to 32, 48 |
| Subsequent supply in Sweden under 10 kap. 51 §, where (1) the recipient is another taxable person or a non-taxable legal person, (2) the recipient is registered here and (3) the supplier issued an invoice under Articles 219a to 237 of the VAT directive (10 §) | Recipient | 23, 30 to 32, 48 where deductible; 37 and 38 are a middleman's boxes. |
| Investment gold where the supplier chose voluntary taxation under 21 kap. 7 or 8 § and both parties are taxable persons who are or must be registered here (11 §) | Buyer | 23, 30, 48 |
| Gold as raw material or semi-finished products of at least 325 thousandths fineness, where both parties are taxable persons who are or must be registered here (12 §) | Buyer | 23, 30, 48 |
| Services concerning property within ground and foundation work, building and civil engineering work, building installation, finishing of buildings or hire of construction machinery with an operator; byggstädning; or supply of staff for those activities (13 §). Buyer is (1) a taxable person supplying such services other than merely occasionally, or (2) another taxable person supplying such services to a person under (1). Not if 9 § applies. | Buyer | 24, 30, 48; seller 41 |
| Waste and scrap of iron, steel, copper, nickel, aluminium, lead, zinc, tin and other base metals; remelting ingots of iron and steel; waste and scrap of cells, batteries and accumulators, where both parties are taxable persons who are or must be registered here (14 §) | Buyer | 23, 30, 48 |
| Emission allowances and other units under 15 §, where both parties are taxable persons who are or must be registered here and 9 § does not apply | Buyer | 24, 30, 48 |
| Mobile phones (apparatus made or adapted for use in an authorised network on specified frequencies, whether or not it has other uses), integrated circuits not built into end products, consoles, tablets and laptops, where both parties are taxable persons who are or must be registered here, the base for these goods in an invoice is together above SEK 100,000 and the buyer's registration duty is not merely a consequence of the purchase (16 §) | Buyer | 23, 30, 48; seller 41 |
| EU acquisition (17 §) | Buyer | 20, 30 to 32, 48 |
| Wrongly charged VAT (23 §) | The person who charged it | See the invoice |

If the conditions of a row under 6 to 16 §§ are not met, the taxable person making the supply is liable (5 §) and charges VAT where the supply is taxable. A sale in Sweden goes in the seller's ruta 41 only where the buyer is liable under one of those rows (Skatteverket); otherwise a domestic taxable sale ordinarily goes in ruta 05. This does not apply to the 17 § and 23 § rows.

**Construction.** Skatteverket applies 2 conditions. (1) The service is a specified construction service, byggstädning, or labour hire for them, in Sweden. (2) The buyer is a taxable person not merely occasionally selling such services, or an occasional seller selling on to such a person. The buyer need not resell. Material included counts as construction; mere goods with insignificant fitting do not. SNI code is irrelevant. The state counts, and municipalities only exceptionally. The seller writes 'omvänd betalningsskyldighet' and the buyer's VAT number on the invoice. Legacy 'both parties are in construction' is corrected: the seller's main business is irrelevant.

The output rate on reverse charge is the rate for that supply, usually 25%. Deduct to the extent the purchase qualifies. Ruta 21 excludes property services, passenger transport, event admission, restaurant and catering, and short-term transport hire; property services go in 24.

### Timing, credits and currency

- Invoice method: ML 7 kap. 14 and 15 §§. Cash method: 7 kap. 16 §, for annual turnover normally at most SEK 3 million, not businesses under the annual accounts laws for credit institutions, securities companies or insurers, or financial holding companies that must prepare group accounts under those laws; unpaid receivables at year-end go in the last period; also covers reverse charge under 16 kap. 6 and 8 to 16 §§. Change: 7 kap. 17 §.
- Prepayments: output when received, input when paid (7 kap. 7 §; Skatteverket). The output rule applies only if the supply is taxable when the payment is received, and not to a supply or transfer of goods exempt under 10 kap. 42 and 46 §§. Apply the rate at that tax point: a qualifying food advance received before 1 April 2026 retains the old 12% rule, even if delivery is later. Construction: 7 kap. 8 §. EU acquisitions: 7 kap. 26 §. Import: 7 kap. 27 §. Input timing: 7 kap. 31 to 34 §§.
- Discounts: 8 kap. 14 §. Retaken goods: 8 kap. 15 §, whose printed text changes on 20 November 2026 under Lag 2026:1025. Bad debts reduce the base: 8 kap. 16 §. Revaluation: 8 kap. 17 §.
- Currency: use the latest average rate on the most representative Swedish market at the tax point, or the latest ECB rate (8 kap. 21 §); cross via euro (22 §); euro accounts (23 §). Legacy 'transaction date, Riksbank' is corrected. OSS uses the ECB rate for the last day of the period.
- There is no carry-forward box. Skatteverket pays a refund automatically if a payout account is registered and no repayment obstacle exists; offsets, outstanding declarations or a statutory hold can prevent payment. Without an account it stays on the skattekonto. Legacy 'credit brought forward' is a skattekonto balance question.

### Capital goods (ML 15 kap.)

Adjustment applies to (1) machines, inventory and the like of declining value with input tax on acquisition of at least SEK 50,000; (2) property new build, extension or rebuilding with input tax on that work of at least SEK 100,000; (3) property and leased or co-operative flats with uttag under 5 kap. 32 § where a deduction under 13 kap. 8 § item 4 or 5 is at least SEK 100,000; (4) rebuilding of a bostadsrätt or hyresrätt with input tax of at least SEK 100,000 (15 kap. 4 §). Cases are in 15 kap. 7 §; aggregation in 6 §. No adjustment if the change leads to own-use taxation or the deductible-share change is less than 5 percentage points (9 §). The period is 10 years for limbs 2, 3 and 4 and 5 years for other capital goods (10 §). On changed use, adjust yearly at 1/10 or 1/5 for the rest of the period (12 and 16 §§). On moving to 18 kap., adjust once for the rest of the period unless the person opposes it, and despite opposition for special reasons (12 §). On a transfer, and on the bankruptcy of a property owner, bostadsrätt holder or tenant under 7 § 6, adjust once for the rest of the period (13 §). The 25% cap applies only to 7 § 3, a taxable sale of a capital good other than property whose input tax was only partly deductible: the adjustment is at most 25% of the price (18 §). Legacy 'cost excl. VAT at least SEK 200,000' is wrong, as the test is input tax and the movable limit is SEK 50,000. Below the limits 15 kap. makes no adjustment; ruta 48 still follows the ordinary rules and limits in 13 kap.

### Conservative defaults

| Ambiguity | Position |
| --- | --- |
| Unknown rate on a sale | Needs Input. Rates are never inferred; a sale is not 25% until its charge is verified. |
| Unknown VAT status of a purchase | No deduction claimed until a document is seen (ML 13 kap. 31 to 36 §§). Disclose. |
| Unknown counterparty country | Needs Input |
| Unknown B2B or B2C status of an EU customer | Needs Input. If evidence stays missing after asking, Skatteverket treats the buyer as non-taxable; the place rule for that service then decides whether Swedish VAT applies, and the rate is verified before any entry. |
| Unknown business use (vehicle, phone, home office) | No deduction claimed until use is documented. Disclose. |
| Unknown SaaS billing entity | Needs Input: entity decides 21, 22 or Swedish VAT. |
| Unknown representation facts or personal use | No deduction until evidence is seen. Disclose. |
| Unknown whether a transaction is in scope | Needs Input |

### Red flag thresholds

Workflow settings, not law. 5 rows are the legacy table. The input VAT row moves the legacy SEK 2,000 document level here. The SEK 0 row is new: `vat-workflow-base` leaves the question threshold to the country and defaults only for the eurozone.

| Threshold | Value |
| --- | --- |
| HIGH single transaction size | SEK 30,000 |
| HIGH tax delta on a single conservative default | SEK 2,000 |
| HIGH input VAT claim without a document seen | SEK 2,000 |
| MEDIUM counterparty concentration | More than 40% of output or input |
| MEDIUM conservative default count | More than 4 across the return |
| LOW absolute net VAT position | SEK 50,000 |
| Tier 2 question threshold | SEK 0: no row is filtered on amount, as no Swedish floor was set |

### Supplier discovery library

Discovery only. Match by case-insensitive substring to find a candidate. Rate, VAT and box come from the document, and no line below is a classification by itself. No billing entity was verified, so none is shown. If nothing matches, use 'Transaction questions and defaults'.

| Pattern | Candidate treatment | Check first |
| --- | --- | --- |
| HANDELSBANKEN, SHB; SEB, SKANDINAVISKA ENSKILDA; SWEDBANK, SPARBANKEN; NORDEA, NORDEA SE; DANSKE BANK SE, LÄNSFÖRSÄKRINGAR BANK | Fee is exempt finance, no ruta 48 (ML 10 kap. 33 §) | Excludes notary, debt collection, factoring administration, safe deposit |
| REVOLUT, WISE, N26 (fee lines) | As above | Separate taxable subscription invoices |
| RÄNTA, INTEREST | No input VAT merely from the bank description | Identify interest income versus expense and its business character; an unresolved income-field outcome is non-usable: Check this point with one of our partner accountants. |
| LÅN, LOAN, AMORTERING | Principal, outside the return | Document shows a loan |
| SKATTEVERKET, MOMS (payment) | Exclude: a tax payment is not a supply for consideration (ML 3 kap. 1 §) | Payment, not a fee |
| TULLVERKET | Exclude duty | Import VAT from the customs bill: ruta 50, 60 to 62 |
| BOLAGSVERKET, FÖRSÄKRINGSKASSAN, KRONOFOGDEMYNDIGHETEN | Identify the actual payment, not a blanket exemption by body | No input VAT without accepted evidence; any unresolved public-authority-fee classification is non-usable: Check this point with one of our partner accountants. |
| ARBETSGIVARAVGIFTER, SOCIALA AVGIFTER, PRELIMINÄRSKATT, F-SKATT | Exclude: tax payments | Payment, not a fee |
| LÖN, SALARY, WAGES (outgoing) | Exclude (ML 4 kap. 2 §) | Employee, not a contractor |
| A-KASSA, FACKFÖRBUND | Identify membership fee versus a separate service | No input VAT without accepted evidence; any unresolved fee classification is non-usable: Check this point with one of our partner accountants. |
| VATTENFALL; ELLEVIO, EON, FORTUM; TELIA, TELIA COMPANY; TELENOR SE, TRE (3), COMVIQ; COMHEM, BREDBAND2 | Candidate domestic 25%, ruta 48 | Invoice, and business use |
| TRYGG-HANSA, IF, FOLKSAM; LÄNSFÖRSÄKRINGAR (insurance); FÖRSÄKRING, INSURANCE | Exempt insurance, no ruta 48 (ML 10 kap. 32 §) | Taxable items invoiced with it |
| POSTNORD, POSTEN | Standard postage possibly exempt (ML 10 kap. 4 and 5 §§) | Invoice shows whether VAT was charged |
| POSTNORD (parcel, courier); DHL, DB SCHENKER, BRING | Candidate domestic 25%, ruta 48 | Goods transport rule; foreign supplier |
| SJ, SJ AB; SL, SKÅNETRAFIKEN, VÄSTTRAFIK; TAXI, TAXI STOCKHOLM, TAXI KURIR; SAS, NORWEGIAN (domestic) | Candidate 6%, ruta 48 if business travel (ML 9 kap. 8 §) | Ticket or receipt |
| SAS, NORWEGIAN, RYANAIR (international) | No Swedish VAT expected: transport with any part abroad is not supplied in Sweden (ML 6 kap. 39 §) | Not '0%'. Foreign VAT is not in ruta 48. |
| ICA, ICA MAXI, ICA KVANTUM; COOP, COOP FORUM, STORA COOP; HEMKÖP, WILLYS, LIDL SE | No deduction until business use is shown | Resale, representation, private |
| RESTAURANTS, CAFES, BARS | No deduction until representation facts are shown | Persons, purpose, split |
| OKQ8, CIRCLE K, PREEM, SHELL SE, INGO | No deduction until the vehicle is known | Item 6.1 below |
| Hotels (Sweden) | Candidate 12%, ruta 48 | Extras outside the room price |
| Office supplies | Candidate domestic 25%, ruta 48 | Invoice |
| Coworking | Candidate domestic 25%, ruta 48 | Rent or service; invoice |
| ADVOKAT, ADVOKATBYRÅ; REVISOR, REVISIONSBOLAG, AUKTORISERAD | Candidate domestic 25%, ruta 48 | Business purpose; private matters give no deduction |
| GOOGLE (Ads, Workspace, Cloud); MICROSOFT (365, Azure); ADOBE; META, FACEBOOK ADS; LINKEDIN (paid); DROPBOX; SLACK; ZOOM; ATLASSIAN (Jira, Confluence); AWS (standard); STRIPE (subscription fees) | If the invoice names an EU entity not established in Sweden: 21, 30, 48 | Entity on the invoice |
| NOTION; ANTHROPIC, CLAUDE; OPENAI, CHATGPT; GITHUB (standard plans); FIGMA; CANVA; HUBSPOT; TWILIO; APPLE | If the invoice names a non-EU entity not established in Sweden: 22, 30, 48 | Entity on the invoice; 21 if EU; Swedish VAT if charged |
| SPOTIFY TECHNOLOGY | If the invoice shows Swedish VAT: domestic, ruta 48, not reverse charge | Legacy says this needs verifying each time |
| STRIPE, PAYPAL (transaction fees) | Candidate exempt finance | ML 10 kap. 33 § limits; fee invoice |
| KLARNA, SWISH (merchant fees) | Needs Input | Exempt fee or taxable platform fee |
| HYRA, LOKALHYRA | Needs Input | Item 6.11 below |
| BOSTADSRÄTT | Identify the actual property/payment and business use | Apply the housing restriction below; an unresolved co-operative-property fee outcome is non-usable: Check this point with one of our partner accountants. |
| ÖVERFÖRING, INTERN, EGET KONTO | Exclude | Own account shown |
| UTDELNING, DIVIDEND | Exclude, ordinary share dividend | Document |
| UTTAG, BANKOMAT, ATM | Exclude until explained | Item 6.10 below |

### Transaction questions and defaults

| Item | What is missing | Default | Question |
| --- | --- | --- | --- |
| 6.1 Fuel and vehicle costs (OKQ8, Circle K, Preem, Shell SE, Ingo) | Vehicle type; owned or hired; use | No deduction until known; then ML 13 kap. 23 § | 'Is this vehicle in the business inventory or hired, and is it a passenger car?' |
| 6.2 Restaurants and entertainment | Purpose, persons, split | No deduction until shown | 'Was this business representation with a documented purpose and attendees? How many persons, and what was food and what was alcohol, excluding VAT?' |
| 6.3 Ambiguous SaaS billing entity | Entity and country | Needs Input | 'Could you check the invoice for the legal entity name and country?' |
| 6.4 Round-number transfers from owner-named counterparties | Nature | Needs Input; excluded only once shown | 'Is this a customer payment, capital injection or loan?' |
| 6.5 Incoming transfers from individuals | Sale or not; country | Needs Input | 'Was this a sale? What was sold, and which country?' |
| 6.6 Incoming transfers from foreign counterparties | Buyer status, supply, country | Needs Input | 'Was this to a business with a VAT number or a consumer, goods or services, and which country?' |
| 6.7 Large one-off purchases | Input tax and asset type | Test input tax against SEK 50,000 or SEK 100,000 | 'What is the VAT on this purchase, and what is the asset?' |
| 6.8 Mixed-use phone, internet, home office | Business share; for a home office, whether the workplace is separated | No deduction until documented | 'Is this a dedicated business line or mixed use? What is the business share, and how is it measured? For a home office, is the workplace wholly separated from the home and specially adapted to the business?' |
| 6.9 Outgoing transfers to individuals | Nature | Needs Input; excluded only once shown | 'Is this a contractor with an invoice, wages, a refund or personal?' |
| 6.10 Cash withdrawals | What the cash paid for | Exclude; no deduction without a document | 'What was the cash used for, and do you hold a document?' |
| 6.11 Rent | Premises; VAT charged | Needs Input. Rent with VAT needs voluntary taxation (ML 12 kap.); no VAT shown means no ruta 48. | 'Is this commercial property? Does the invoice show moms?' |
| 6.12 Foreign hotel | Country; charge | Nothing in ruta 48: foreign VAT is not deductible here. | 'Was this a business trip, and do you hold the invoice for a refund claim there?' |
| 6.13 Construction received (byggtjänster, snickare, målare, VVS) | Service; buyer status; invoice wording | Needs Input. Swedish VAT or reverse charge depends on the 2 conditions. | 'What was done, is it for resale or own use, do you sell such services other than occasionally, and does the invoice say omvänd betalningsskyldighet?' |
| 6.14 ROT and RUT on invoices | Whole invoice | ROT and RUT are income tax reductions. IL 67 kap. 11 a § treats the labour charge as including VAT, so VAT is read from the whole invoice. Rate from the invoice. | 'What is the total invoice amount including VAT, before the ROT or RUT reduction?' |

### Sweden bank statement guide

Read the actual export header and delimiter; never assume a bank layout. The historical Handelsbanken/Swedbank semicolon and SEB tab descriptions are not import specifications.

Hyra is rent, lön salary, ränta interest, överföring transfer, uttag withdrawal and insättning deposit. Own-account transfers ('överföring', 'eget konto', 'intern') are excluded. Sole trader transfers to a personal account are drawings: exclude. A proved credit note reverses the original classification in the legally required period; do not treat every bank refund as a VAT credit. Reduce the recipient's prior input deduction where required.

IBAN prefix: SE is Sweden. DK and FI are EU. NO is outside the EU, corrected from legacy text. IE, DE and FR are EU. US, GB and CH are non-EU. An IBAN shows where the account is, not where the supplier is established.

### Excel working paper

**Working paper only.** The reviewer must check every figure before filing.

The base's Sheet 'Transactions' applies. Column H holds base box, output box and input box, separated by slashes, as one text value: '05/10', '21/30/48', '50/60/48', '48' or '39'. Sweden adds column Q, 'Deductible input VAT'. Enter the deductible amount there. Columns E, F and Q hold positive amounts, whatever the bank sign; a refund or credit note is negative. A limit on deduction is explained in column I, as base Check 10 requires.

Sheet 'Box Summary':

```
| 05 | =SUMIFS(Transactions!E:E, Transactions!H:H, "05/*") |
| 06 | =SUMIFS(Transactions!E:E, Transactions!H:H, "06/*") |
| 07 | Not used: R-SE-6 refuses margin schemes |
| 08 | =SUMIFS(Transactions!E:E, Transactions!H:H, "08/*") |
| 10 | =SUMIFS(Transactions!F:F, Transactions!H:H, "*/10") |
| 11 | =SUMIFS(Transactions!F:F, Transactions!H:H, "*/11") |
| 12 | =SUMIFS(Transactions!F:F, Transactions!H:H, "*/12") |
| 20 to 24 | =SUMIFS(Transactions!E:E, Transactions!H:H, "20/*"), and the same for 21 to 24 |
| 30 | =SUMIFS(Transactions!F:F, Transactions!H:H, "*/30*") |
| 31 | =SUMIFS(Transactions!F:F, Transactions!H:H, "*/31*") |
| 32 | =SUMIFS(Transactions!F:F, Transactions!H:H, "*/32*") |
| 35 to 42 | =SUMIFS(Transactions!E:E, Transactions!H:H, "35"), and the same for 36 to 42 |
| 48 | =SUMIFS(Transactions!Q:Q, Transactions!H:H, "*48") |
| 50 | =SUMIFS(Transactions!E:E, Transactions!H:H, "50/*") |
| 60 | =SUMIFS(Transactions!F:F, Transactions!H:H, "*/60*") |
| 61 | =SUMIFS(Transactions!F:F, Transactions!H:H, "*/61*") |
| 62 | =SUMIFS(Transactions!F:F, Transactions!H:H, "*/62*") |
| 49 | =C10+C11+C12+C30+C31+C32+C60+C61+C62-C48 |
```

In the ruta 49 line, C followed by a box number means that box's row. Output VAT is the sum of each row's VAT, not a box multiplied by one rate, because ruta 05 holds all rates. Legacy formulas are replaced. Sheet 'Return Form': positive ruta 49 is payable to Skatteverket, negative is a refund. Run the recalculation step that `vat-workflow-base` specifies on `sweden-vat-<period>-working-paper.xlsx`.

### Key legislation

ML, SFL and IL are in Sources. Corrected legacy citations: 12% is ML 9 kap. 4 to 7 §§ and 6% is 9 kap. 8 to 19 §§, not 9 kap. 3 and 4 §§; insurance is 10 kap. 32 §, not 35 §; reverse charge is 16 kap. 9 § with place in 6 kap. 33 and 34 §§; construction is 16 kap. 13 §, as 6 kap. 34 a § does not exist; representation is ML 13 kap. 24 and 25 §§ with IL 16 kap. 2 §, not IL alone.

### Known gaps

The supplier library does not cover every Swedish business. Construction services are listed by Skatteverket and not reproduced here. Check capital goods limits and representation amounts for each period. Spotify treatment depends on the invoice.

### Completion checks

```
[ ] Every ruta 48 amount has a document ML 13 kap. 31 to 36 §§ accepts?
[ ] Every Needs Input row is listed for the reviewer?
[ ] Every refusal fired stopped the work, with the exact message?
[ ] Ruta 35, 38 and the ruta 39 sales with a buyer VAT number reconciled to the periodisk sammanställning?
[ ] Rate tested against the tax point, with 1 April and 1 July 2026 checked?
[ ] Ruta 49 equals the sum of 10, 11, 12, 30, 31, 32, 60, 61 and 62, less 48?
[ ] Exempt sales in ruta 42, and R-SE-3 tested?
[ ] No 'Validated' or reviewer statement added?
```

## Deadlines and filing

**Periods (SFL 26 kap. 10 to 13 §§).** The legacy file read these as free choices. The rule is:

| Estimated base for the tax year, excluding EU acquisitions and imports | Period set by law | Shorter period |
| --- | --- | --- |
| Above SEK 40 million | Calendar month (10 §) | None |
| At most SEK 40 million | Calendar quarter (11 §) | Month, by Skatteverket's decision on request or for special reasons (13 §) |
| At most SEK 1 million | Tax year (11 §) | Month or quarter, likewise (13 §) |

A decision on request runs at least 24 months unless special reasons oppose it.

**File every period (SFL 26 kap. 2 and 5 §§), with payment booked by the same day (62 kap. 2 and 3 §§).**

| Period | Deadline | Source |
| --- | --- | --- |
| Quarter | October to December: 12 February. January to March: 12 May. April to June: 17 August. July to September: 12 November. | SFL 26 kap. 26 § |
| Month, base at most SEK 40 million | 12th of the second month after the period; 17th in January and August | SFL 26 kap. 27 § |
| Month, on request | 26th of the following month; 27 December for November; at least 12 periods unless special reasons oppose it | SFL 26 kap. 28 and 30 §§ |
| Month, above SEK 40 million | 26th of the following month; 27 December for November | SFL 26 kap. 30 § |
| Tax year, natural persons/estates filing an income return, without the cross-border transactions defined below | 12 May | SFL 26 kap. 33 a § |
| Tax year, legal persons except estates and HB, filing an income return, without the cross-border transactions under 33 a § second paragraph | Year ending 31 December: 12 July. 30 April: 12 November. 30 June: 27 December. 31 August: 12 March. Electronic filing may be made in the following month: by the 17th in January and August, and the 12th in April and December. Skatteverket groups year-ends. January to April: 12 November (digital 12 December). May to June: 27 December (17 January). July to August: 12 March (12 April). September to December: 12 July (17 August). | SFL 26 kap. 33 b §; Skatteverket |
| Tax year, others including the defined cross-border transactions, HB, KB, VAT groups, enkla bolag representatives and partrederier | 26th of the second month after the year; 27 December. Skatteverket: 26 February for a sole trader with EU trade. | SFL 26 kap. 33 § |

The annual-return exception in SFL 26 kap. 33 a § covers (1) goods delivered/acquired/transferred between EU countries and (2) Article 196 services supplied or acquired for which the buyer pays VAT in Sweden or another EU country. A US SaaS purchase with Swedish Article 196 reverse charge can therefore require the 26 February deadline; "no EU supplier/customer" alone is insufficient.

A deadline on a Saturday, Sunday, public holiday, Midsummer Eve, Christmas Eve or New Year's Eve moves to the next weekday (Lag (1930:173) 2 §). For calendar-2026 quarters: 12 May 2026, 17 August 2026, 12 November 2026 and 12 February 2027. For calendar-2026 annual sole-trader returns: 12 May 2027 if 33 a § applies; otherwise 26 February 2027. Check the registration decision and any actual extension before filing.

**Extensions.** Anstånd for special reasons: SFL 36 kap. 5 §, with a 12 June limit for 33 a filers unless synnerliga skäl, and synnerliga skäl for 33 b filers. Byråanstånd to 26 June: 36 kap. 6 §, for 33 a filers using professional help, and it may be refused. Apply by the deadline. A filing extension is not a payment extension: Skatteverket charges interest from the day after 12 May despite byråanstånd.

**Portal and filing.** File in Skatteverket's e-service **Lämna momsdeklaration**, by XML upload or manual entry; from an accounting system by API with signing in **Mina sidor**; or on paper form SKV 4700, ordered through Beställ blanketter. For a nil return, enter 0 in ruta 49. Tax amounts are whole SEK with öre discarded (SFF 22 kap. 1–2 §§), also for manual and paper reporting. Retain öre in the working paper; XML accepts integers only. Identify yourself with e-legitimation and be authorised to represent the business. Upload prepares a declaration; review, sign and submit separately, and retain the receipt.

**Payment.** To the skattekonto: bankgiro 5050-1055 with OCR. Skatteverket gives an international number for a foreign account. Paid means booked on the account by the deadline.

**Refund.** Skatteverket may withhold excess input VAT where it has opened a check of the return, there is a risk of tax evasion and the excess is a significant amount. It must be repealed or reduced when the underlying circumstances change or special reasons exist; on a reassessment reducing the declared excess, the hold continues until the resulting tax due date. The decision covers at most the excess within the check, for up to 2 years, extendable by 6 months at a time where the check cannot be finished in that time and special reasons exist (SFL 63 a kap. 1 to 5 §§, printed as Lag 2026:707; interest 65 kap. 7 a §). Prop. 2025/26:128, which the Riksdag adopted on 6 May 2026 (SkU22), gives 1 July 2026 with no transitional rules. SFS 2026:707 expressly takes effect on 1 July 2026.

**Corrections.** Redo the return in the accounting system, in 'Se och rätta inlämnade momsdeklarationer', or with a new paper return or letter. Request by the 6th year after the calendar year in which the tax year ended (SFL 66 kap. 7 §); within 2 months of notice for the 18 kinds of decision that section lists, including registration, föreläggande and payment or refund of tax.

**Related filing.** Periodisk sammanställning: SFL 35 kap. 2 to 4 and 9 §§. Due the 25th in the month after the period if electronic, otherwise the 20th in that month. See 'Cross-border points'.

## Penalties and interest

**Late filing (förseningsavgift).** SEK 625 for a skattedeklaration, SEK 1,250 after a föreläggande, and SEK 1,250 for a periodisk sammanställning (SFL 48 kap. 1, 5 and 6 §§).

**Skattetillägg.**

- Grounds: oriktig uppgift for own tax (SFL 49 kap. 4 §), meaning data clearly (1) incorrect, (2) omitted or (3) on a transaction that was a step in VAT evasion, where the person knew or should have known, but not where the data together suffice for a correct decision or are obviously unusable (5 §; SFS 2026:110 takes effect on 1 April 2026); skönsbeskattning (6 §).
- Rate: 20% of the tax not determined or wrongly credited (11 §, the 'annan skatt' rate, as VAT is not in the 56 kap. 3 § list). Period errors: 2% where the period is at most 3 months and the shift is within 4 months, otherwise 5% (13 §). Skönsbeskattning: 20% (15 §).
- A skattetillägg on skönsbeskattning for a missing return is withdrawn where the return is filed within 2 months from the end of the decision month, or from the day the person learnt of it if they show it is likely they did not know before that month ended (7 §).
- No skattetillägg if data for matching were available to Skatteverket within 1 year from the end of the tax year, on own-initiative correction (not if general control informed, the correction is connected to it and made after 2 months), or for a trivial amount (10 §).
- Relief, full or partial, where unreasonable: age, health, misjudgment, disproportion or delay (51 kap. 1 §).

**Interest.** Daily on the skattekonto (SFL 65 kap. 2 to 4 §§). Basränta is 125% of the 6-month treasury bill rate, with a 1.25% floor (3 §). Cost at basränta; income at 45% of it, or 0 where basränta is set at that floor (4 §). Late: basränta plus 15 percentage points until registration with Kronofogden (13 §, Förordning 2026:146). Relief needs synnerliga skäl (15 §). Skatteverket's page gives the amounts in the rates table. Skatteverket's brochure SKV 408 repeats the method and points to the site for current rates.

## Cross-border points

**Goods sold to the EU (ML 10 kap. 42 and 43 §§).** Exempt with deduction, ruta 35, if (1) the buyer is a taxable person or a non-taxable legal person acting as such in another EU country, (2) the buyer has a VAT number there and has given it, and (3) the seller filed a correct periodisk sammanställning or satisfactorily explains why not. The goods must be sent or transported by the seller or buyer, or on either's behalf, from Sweden to another EU country (42 §). For a buyer without deduction/refund rights, or a flat-rate agricultural buyer, 47 § additionally requires its acquisitions to exceed its destination-state threshold or an election to tax them there; that extra test does not apply to excise goods/new means of transport. Check the VAT number on VIES and keep evidence of the transport; evidence must actually establish movement to the other EU country. A VIES result alone proves no transport. Where the Article 45a evidential presumption is used, check its independent-document and buyer-statement conditions in the EU companion. A failed VIES check is not by itself a rate: Needs Input, then test each condition, place and rate. The directive file's local-rate result is applied only after that.

**Services sold to the EU.** Under 6 kap. 33 to 36 §§, a service to a taxable person is taxed where the buyer has its business. Ruta 39, with no Swedish VAT. Skatteverket: a valid VAT number given by the buyer normally suffices, and the sale then goes in the periodisk sammanställning. Without the number, other evidence can show status, such as a tax authority certificate; the sale then goes in ruta 39 and is not listed. If the seller cannot show status, the buyer is treated as non-taxable and the rules for those buyers apply. Other services abroad and services to non-EU buyers: ruta 40.

**Exports (ML 10 kap. 64 to 68 §§).** Exempt with deduction (13 kap. 10 §). Goods under 64 to 66 §§ go in ruta 36. Services under 67 and 68 §§ are not goods, and Skatteverket says services exempt in Sweden go in ruta 42. A service supplied abroad under 6 kap. is assessed separately for ruta 39 or 40. The conditions of those sections apply; check them on each sale.

**EU acquisitions.** Ruta 20, output in 30 to 32, input in 48 (ML 16 kap. 17 §). The seller must be VAT registered in another EU country, the goods must move between EU countries and the buyer must give a valid VAT number (Skatteverket). The ordinary acquisition treatment assumes a qualifying taxable seller; private sellers, new means of transport and margin-scheme goods require their own test, not a universal no-VAT rule.

**Imports.** A registered importer reports to Skatteverket, not Tullverket: ruta 50, output in 60 to 62, input in 48 where deductible (ML 16 kap. 18 to 22 §§). Normally report in the period the tullräkning or tullkvitto was issued, whichever accounting method is used; ML 7 kap. 27 § instead uses the import tax point in the centralised-clearance cases in 16 kap. 21–22 §§. A business not registered at import pays Tullverket. `eu-vat-directive` 4.5 says import VAT is paid at Customs, which is this unregistered case.

**Triangular trade.** Ruta 37 and 38 apply only where a seller in one EU country sells to a middleman in another, the goods go directly to a customer in a third EU country, and all 3 parties are VAT registered in their own countries. The middleman pays no VAT on that purchase, and ruta 38 also goes in the periodisk sammanställning (Skatteverket). Other qualifying EU acquisitions of goods go in ruta 20, not ruta 37. Separately, where the goods go directly to Sweden, ML 10 kap. 51 § exempts the foreign middleman's acquisition and 16 kap. 10 § makes the recipient in Sweden liable if its conditions are met. The Swedish recipient uses ruta 23 and output in 30–32, with input in 48 only where deductible; this is not the middleman's 37/38 route.

**EU distance sales and OSS.** For a seller established in Sweden and not in another EU country, or with no establishment but resident or staying here and not in another EU country, supplying 6 kap. 56 § services or 6 kap. 8 § goods to non-taxable buyers in another EU country, Swedish VAT applies while the combined value excluding VAT is not above SEK 99,680 in the current and previous year (6 kap. 62 §). From the supply exceeding it, the supply is abroad (63 §), and the seller may opt earlier (64 §). This replaces legacy €10,000, which is the directive figure, and covers both goods and services. Above the limit, from the crossing supply, or following the option: use destination-country VAT. Determine whether Union OSS is elected/available or local registration is required; use `eu-oss-digital` for the separate return. Do not enter OSS-covered sales again in the ordinary return. OSS is a separate return in EUR, due the last day of the month after the quarter (import scheme monthly), with no input deduction, ECB rate conversion and required nil returns, and it is not reported in the momsdeklaration (Skatteverket). Payment details come from Skatteverket's OSS page.

**Periodisk sammanställning.** Filed in the e-service Periodisk sammanställning or Filöverföring, or on SKV 5740, only when there are sales. Goods: monthly. Services: quarterly. Both goods and services: monthly (SFL 35 kap. 3 §). A seller moving from quarterly to monthly stays monthly to the fourth calendar quarter after the change. Goods quarterly on request (form SKV 4853), only if goods are at most SEK 500,000 excluding VAT in the quarter of the application and each of the 4 quarters before it, with no other reason for monthly listing. The decision lapses when the limit is exceeded (SFL 35 kap. 4 §; Skatteverket). Call-off stock: SKV 5739. Whole kronor. Ruta 35 and 38 tie to it. Services are listed only where taxable in the buyer's country, so ruta 39 may differ.

**Passenger transport.** Supplied in Sweden only if no part takes place abroad (ML 6 kap. 39 §). An international flight is therefore outside Sweden for its whole length, not '0%'.

**Norway.** Norway is outside the EU, so goods sold there are exports and goods bought from there are imports. A delivery in Sweden to a natural person resident in Norway or on Åland is exempt only if (1) it is goods or a group forming a whole, at SEK 1,000 or more after VAT, and (2) the seller can show the buyer took them there soon after delivery and paid the equivalent tax under a customs bill or similar document (ML 10 kap. 65 §).

## Two worked examples that recompute

These hypothetical inputs and dates are preserved. They assume a registered, fully deductible business, correct invoice tax, a proved Swedish receiving business establishment and the stated supply classification. Exact öre are working-paper calculations; statutory tax fields discard öre at filing, under SFF 22 kap. 1 §. Example 7 is a working-paper roll-up, not a decimal XML return. For its filing reconciliation, the displayed tax components become 10:25,000;12:1,200;30:2,416;48:3,221; their sum gives49:25,395. Preserve the exact-öre working balance25,394.80 separately.

### Example 1: Non-EU SaaS reverse charge (Notion)

`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; SEK 166.88`

If the invoice names the US entity, no Swedish VAT and a service under the main rule: ruta 22 SEK 166.88, ruta 30 SEK 41.72, ruta 48 SEK 41.72. Net effect 0. If the invoice names an EU entity, test ruta 21; Swedish VAT permits ordinary input treatment only if correctly charged, not merely because it appears on an invoice. Convert under ML 8 kap. 21 §: the bank's SEK figure is not automatically that rate.

```oa-check
name: Notion reverse charge
inputs:
  net: 166.88
steps:
  - output: round(pct(net, 25), 2)
  - input: output
  - net_effect: output - input
expected:
  output: 41.72
  input: 41.72
  net_effect: 0
```

### Example 2: EU service, reverse charge (Google Ads)

`10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April ; -9,500.00 ; SEK`

If the invoice names the Irish entity and shows no VAT: ruta 21 SEK 9,500, ruta 30 SEK 2,375, ruta 48 SEK 2,375.

```oa-check
name: Google Ads reverse charge
inputs:
  net: 9500
steps:
  - output: round(pct(net, 25), 2)
  - input: output
  - net_effect: output - input
expected:
  output: 2375
  input: 2375
  net_effect: 0
```

### Example 3: Representation, food and alcohol

`15.04.2026 ; RESTAURANG OPERAKÄLLAREN ; DEBIT ; Client dinner 4 persons ; -4,800.00 ; SEK`

The bank line alone gives no deduction. Ask item 6.2. The receipt then decides.

- Receipt A, all food and non-alcoholic drink at 12%: capped base SEK 1,200, deduction SEK 144. Take-away food at 6%: SEK 72.
- Receipt B, food SEK 3,000 net at 12% and alcohol SEK 1,152 net at 25%: VAT SEK 360 plus SEK 288, SEK 648 in all, gross SEK 4,800. Proportional deduction SEK 187.28. The flat amount is SEK 184, and its conditions are met: cost is above SEK 300 net per person and VAT is SEK 162 per person. Skatteverket lets the client choose either, and SEK 187.28 is the higher.

```oa-check
name: Representation with alcohol
inputs:
  persons: 4
  cap: 300
  food_net: 3000
  alcohol_net: 1152
steps:
  - base: persons * cap
  - total_net: food_net + alcohol_net
  - gross: total_net + pct(food_net, 12) + pct(alcohol_net, 25)
  - food_base: base * food_net / total_net
  - alcohol_base: base * alcohol_net / total_net
  - proportional: round(pct(food_base, 12) + pct(alcohol_base, 25), 2)
  - flat: 46 * persons
  - best: max(proportional, flat)
  - all_food_12: pct(base, 12)
  - takeaway_6: pct(base, 6)
expected:
  base: 1200
  gross: 4800
  proportional: 187.28
  flat: 184
  best: 187.28
  all_food_12: 144
  takeaway_6: 72
```

### Example 4: Passenger rail at 6%

`18.04.2026 ; SJ AB ; DEBIT ; Stockholm–Gothenburg return ; -1,200.00 ; SEK`

Domestic rail with no part abroad, ML 9 kap. 8 §. Ruta 48 if this is business travel and the ticket shows the VAT.

```oa-check
name: Rail ticket
inputs:
  gross: 1200
steps:
  - net: round(gross / 1.06, 2)
  - vat: round(gross - net, 2)
expected:
  net: 1132.08
  vat: 67.92
```

### Example 5: EU B2B service sale

`22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice SE-2026-018 IT consultancy March ; +35,000.00 ; SEK`

The bank receipt date does not establish the reporting period: inspect the invoice and the accounting method. March consultancy paid22April can belong to an earlier period; never duplicate an invoice already reported. If the buyer gave a valid German VAT number: ruta39 SEK35,000 in the proper period, no Swedish VAT, and a line in the periodisk sammanställning if taxable in Germany. Check the number on VIES. If there is no number but other evidence shows a taxable person buying for its business: ruta 39 SEK 35,000, no Swedish VAT and no listing. If status is unproved, this is Needs Input, not 25%: the buyer then counts as non-taxable, and the place rule for that service decides whether Swedish VAT applies. All 3 cases are given to the reviewer. Buyer status, business use and the receiving establishment must be evidenced; a company name alone is insufficient.

```oa-check
name: EU service sale
inputs:
  sale: 35000
steps:
  - ruta_39: sale
  - output_if_status_shown: 0
expected:
  ruta_39: 35000
  output_if_status_shown: 0
```

### Example 6: Mixed-use passenger car

`28.04.2026 ; VOLVO FINANS ; DEBIT ; Car lease May ; -5,500.00 ; SEK`

The bank line does not show hire or finance, the rate or any insurance. Needs Input until the contract and invoice are seen. If it is hire of a personbil at 25% with SEK 5,500 gross, and use in deductible activity is more than trivial: half the VAT, whatever the share of private use, and no uttag. If it is hire-out, taxi, the deceased or driver training: all the VAT. If the agreement clearly shows a sale, it is a purchase: no deduction.

```oa-check
name: Hired car
inputs:
  gross: 5500
steps:
  - net: round(gross / 1.25, 2)
  - vat: round(gross - net, 2)
  - half_deduction: round(vat / 2, 2)
  - full_deduction: vat
  - purchase_deduction: 0
expected:
  net: 4400
  vat: 1100
  half_deduction: 550
  full_deduction: 1100
  purchase_deduction: 0
```

### Example 7: Return roll-up

Add illustrative sales of SEK 100,000 at 25% and SEK 20,000 of e-books at 6%, both in ruta 05. Use Receipt B and the half deduction. Ruta 39 stays out of ruta 49.

```oa-check
name: Ruta 49 roll-up
inputs:
  ruta_05_at_25: 100000
  ruta_05_at_6: 20000
  ruta_21: 9500
  ruta_22: 166.88
  rep: 187.28
  rail: 67.92
  car: 550
steps:
  - ruta_05: ruta_05_at_25 + ruta_05_at_6
  - ruta_10: pct(ruta_05_at_25, 25)
  - ruta_12: pct(ruta_05_at_6, 6)
  - ruta_30: round(pct(ruta_21 + ruta_22, 25), 2)
  - ruta_48: round(ruta_30 + rep + rail + car, 2)
  - ruta_49: round(ruta_10 + ruta_12 + ruta_30 - ruta_48, 2)
expected:
  ruta_05: 120000
  ruta_10: 25000
  ruta_12: 1200
  ruta_30: 2416.72
  ruta_48: 3221.92
  ruta_49: 25394.80
```

## Ask the client first

Intake only. Ask before any output, under `vat-workflow-base` Step 6.5 before Step 7. What stays unanswered is Needs Input, and no working paper is produced with pending entries first.

1. **Entity and registration:** enskild firma, AB, HB or other? Is the business momsregistrerad? What are the organisationsnummer and momsregistreringsnummer (SE, 10 digits, 01)?
2. **Period and method:** month, quarter or tax year, and which period? Invoice or cash method? Is there a decision from Skatteverket on the period?
3. **Business and people:** what does the business do, and does it have employees?
4. **Exempt sales:** does the business make VAT-exempt sales? If so, R-SE-3 may fire.
5. **Cross-border and balance:** any customers or suppliers outside Sweden, EU or non-EU, business or consumer? Is there a skattekonto balance or excess credit from an earlier period?
6. **Vehicles:** is a vehicle used for business? Passenger car or other, owned or hired, private use, and how far driven each year?

## Preserved earlier cases

The earlier cases retain their original inputs and 2026 dates. The same evidence, deduction and filing conditions above apply. Figures labelled estimates are not tax-account assessments.

### Historical case 1: Consultancy on quarterly returns, Q3 2026

An aktiebolag consultancy with a taxable base of about SEK 1.6 million a year files quarterly (SFL 26 kap. 11 §). In July to September 2026 it invoices Swedish clients SEK 400,000 excluding VAT at 25%. Swedish purchase invoices for its taxable work carry SEK 22,000 of VAT. It buys a software service from an Irish business for SEK 30,000 without VAT. It takes three clients to lunch with one staff member: food and soft drinks SEK 2,000 excluding VAT, VAT SEK 240 at 12%, with attendees and purpose recorded.

- Output VAT: 25% of 400,000 = SEK 100,000 (field 05: 400,000; field 10: 100,000).
- Irish service: field 21: 30,000; VAT 25% = SEK 7,500 in field 30, deductible in field 48.
- Lunch: the capped base is SEK 300 x 4 = 1,200, so the deduction is 12% of 1,200 = SEK 144, not the SEK 240 charged (ML 13 kap. 25 §).
- Field 48: 22,000 + 7,500 + 144 = SEK 29,644.
- Field 49: 100,000 + 7,500 - 29,644 = SEK 77,856, filed and on the tax account by 12 November 2026.

```oa-check
name: Sweden Q3 2026 quarterly return, consultancy with an EU service and a capped representation lunch
inputs:
  sales: 400000
  domestic_input_vat: 22000
  eu_service: 30000
  lunch_cost: 2000
  attendees: 4
steps:
  - output_vat: sales * 0.25
  - eu_service_vat: eu_service * 0.25
  - lunch_base: min(lunch_cost, 300 * attendees)
  - lunch_ded: lunch_base * 0.12
  - field_48: domestic_input_vat + eu_service_vat + lunch_ded
  - field_49: output_vat + eu_service_vat - field_48
expected:
  output_vat: 100000
  eu_service_vat: 7500
  lunch_base: 1200
  lunch_ded: 144
  field_48: 29644
  field_49: 77856
```

### Historical case 2: Café with takeaway, Q2 2026, filed and paid late

A café run as a company files quarterly. In April to June 2026, after the food rate fell, it sells:

- takeaway food and soft drinks, SEK 200,000 excluding VAT: food at 6% (ML 9 kap. 19 §) = SEK 12,000;
- meals eaten in the café, SEK 300,000: restaurant service at 12% (ML 9 kap. 5 §) = SEK 36,000;
- wine served with meals, SEK 50,000: excluded from the 12% rate, so 25% = SEK 12,500.

Output VAT is SEK 60,500. It buys food from wholesalers for SEK 150,000 at 6% (input VAT SEK 9,000) and other supplies with SEK 10,000 of VAT. It hires a passenger car used well over 100 Swedish miles a year in the business; the quarter's hire VAT is SEK 3,000, of which 50% (SEK 1,500) is deductible (ML 13 kap. 22 §). Field 48 is SEK 20,500 and field 49 is SEK 40,000.

The return and payment were due on 17 August 2026. The café files and pays 10 days late, on 27 August. Assuming no relief applies, it owes the SEK 625 förseningsavgift (SFL 48 kap. 6 §). Interest runs from 18 August at the base rate plus 15 points, 17.5% a year (SFL 65 kap. 13 §). The check below uses simple daily interest on a 365-day year as an estimate; the tax account shows the exact figure.

```oa-check
name: Sweden Q2 2026 café, 6% food, 12% restaurant, 25% wine, car hire, late return and interest
inputs:
  takeaway: 200000
  dine_in: 300000
  wine: 50000
  food_purchases: 150000
  other_input_vat: 10000
  car_hire_vat: 3000
  late_fee: 625
  days_late: 10
  base_rate_pct: 2.5
steps:
  - output_vat: takeaway * 0.06 + dine_in * 0.12 + wine * 0.25
  - field_48: food_purchases * 0.06 + other_input_vat + car_hire_vat * 0.5
  - field_49: output_vat - field_48
  - interest: round(field_49 * (base_rate_pct + 15) / 100 * days_late / 365, 2)
  - total_due: field_49 + late_fee + interest
expected:
  output_vat: 60500
  field_48: 20500
  field_49: 40000
  interest: 191.78
  total_due: 40816.78
```

### Historical case 3: Ordinary sale, food either side of 1 April, EU goods, import and a correction

All amounts are assumptions. An ordinary 25% sale of SEK 100,000: field 05 100,000, field 10 25,000. Food delivered on 31 March 2026 for SEK 100,000 carries 12,000 of VAT; the same on 1 April carries 6,000. Eaten on the seller's premises, the April sale would be 12%. EU goods for SEK 20,000 at 25%: field 20 20,000, field 30 5,000, field 48 5,000 if deductible. An import base of SEK 40,000 from customs evidence (customs value, duty, transport and insurance to the destination): field 50 40,000, field 60 10,000. A filed return that omitted a SEK 10,000 sale at 25% understated VAT by 2,500: file a complete new return for that period, never one showing only the 2,500.

### Historical case 4: Representation dinner with food and alcohol (Skatteverket's own example)

Dinner for three, attendees and purpose recorded: food SEK 900 and strong beer SEK 600 excluding VAT, VAT SEK 258. The capped base is SEK 900. Food is 60% of cost, so SEK 540 of the base is food and SEK 360 beer. Deductible VAT is SEK 154.80 in field 48. The flat alternative gives SEK 138.

```oa-check
name: Sweden representation dinner for three, Skatteverket example
inputs:
  food: 900
  beer: 600
  people: 3
steps:
  - capped_base: min(food + beer, 300 * people)
  - food_share: capped_base * food / (food + beer)
  - beer_share: capped_base - food_share
  - deduction: food_share * 0.12 + beer_share * 0.25
  - flat: 46 * people
expected:
  capped_base: 900
  food_share: 540
  beer_share: 360
  deduction: 154.80
  flat: 138
```

### Historical case 5: Hired versus bought passenger car

A business hires a car for a full year at SEK 5,500 a month excluding VAT and drives it more than 100 Swedish miles in taxable activity. Monthly hire VAT is SEK 1,375, and SEK 687.50 goes in field 48. At only 50 Swedish miles over a full-year hire, no hire VAT is deductible. Had it bought the car, no purchase VAT would be deductible, while fuel and repair VAT stay fully deductible.

```oa-check
name: Sweden hired passenger car, monthly hire VAT
inputs:
  monthly_hire: 5500
steps:
  - hire_vat: monthly_hire * 25 / 100
  - deductible: hire_vat * 50 / 100
expected:
  hire_vat: 1375
  deductible: 687.50
```


### Original test cases retained with corrected outcomes

All figures below are original hypothetical inputs, not official amounts. Swedish business use, accepted evidence and a proved supply category are required for every deduction.

| Original test | Original inputs | Usable VAT result or bounded hold |
|---|---|---|
| 1 Domestic office purchase | Gross SEK 2,500; net 2,000; VAT 500 | Ruta 48: 500 if fully deductible; no purchase base in 05–12 or 20–32. |
| 2 US AWS service | SEK 1,000/month, no VAT | General-rule service: 22: 1,000; 30/48: 250 each if fully deductible. |
| 3 German goods | EUR 5,000, illustrative SEK 57,500 | Confirm the legal FX base; if 57,500 and 25% qualifying acquisition: 20:57,500;30/48:14,375. |
| 4 Danish goods sale | SEK 30,000, Sweden–Denmark, VAT-registered buyer | 35:30,000/no output only with all movement, communicated VAT-ID and listing conditions above. |
| 5 Unregistered SME | Annual turnover SEK 80,000; supplies 5,000 + VAT 1,250 | If the full current/prior-year/seat/exclusion tests are met: no ordinary return or credit, total gross cost6,250. SEK80,000 is the case input, not the 2026 exemption threshold. |
| 6 Hired personbil | SEK5,000 + VAT1,250, mixed use | If qualifying hire and more-than-trivial business use:48:625;625 unrecovered. |
| 7 French hotel | Gross SEK3,000 including French TVA | No Swedish input VAT. A foreign refund is a separate eligibility claim; do not call the tax universally irrecoverable. |
| 8 Representation | Food SEK2,400 + stated VAT600 at25%;4guests;600net/person | Preserve this inconsistent food-rate invoice input. No computed filing deduction is usable until the supplier corrects/explains the rate and the facts are proved. Check this point with one of our partner accountants. The former blanket VAT block and income-tax deduction conclusion are withdrawn. |
| 9 Construction | Renovation SEK200,000; both registered construction businesses; reverse-charge invoice | If the statutory service/buyer tests apply:24:200,000;30/48:50,000 if fully deductible. |
| 10 ROT | Net100,000 = labour60,000 + materials40,000; VAT25,000; historical30% ×60,000=18,000 reduction | VAT base05:100,000/output10:25,000 unchanged by customer payment split. The historical ROT amount is an input, not a proved 2026 entitlement or rate: Check this point with one of our partner accountants. |
| 11 Restaurant meals | Net SEK50,000 at12% | Restaurant service:05:50,000;11:6,000; takeaway must instead follow the tax-point food rate. |
| 12 Books | Net SEK20,000 at6% | Qualifying non-advertising books:05:20,000;12:1,200. |
| 13 Finance | Advisory receipts SEK500,000, originally described as exempt | Financial advice is not exempt merely by name. If a proved ML10.33 exempt service:42:500,000, no related input credit; otherwise test ordinary25%. Unresolved nature: Check this point with one of our partner accountants. |
| 14 China import | Original customs value including duty SEK100,000; standard goods | First add any required ancillary costs missing from that input. Only if the complete import base is100,000:50:100,000;60:25,000;48:25,000 if deductible. Never30. |
| 15 Partial exemption | Taxable800,000;exempt200,000;inputVAT50,000 | 80% ×50,000=40,000 is illustrative arithmetic only; it is not an approved allocation. Attribute direct costs first and establish a reasonable basis for shared costs. Unresolved method: Check this point with one of our partner accountants. |

### Other earlier topic boundaries

The historical electric/hybrid-car benefit and F-skatt/direct-tax topics do not establish income-tax amounts here. The ordinary VAT car rules above still apply to an electric passenger car. Property transition, group and margin outcomes remain the precise R-SE holds above. Intrastat is a separate statistical filing: the original table labelled2025 used dispatchesSEK4,500,000/arrivalsSEK9,000,000 and a10th deadline; none is a usable2026 threshold/deadline here. Check this point with one of our partner accountants. EU hotel, US SaaS, construction, car hire, representation, EU goods, Norway, credits, property rent, ROT/RUT, agriculture, electric cars, groups, margin schemes, imports and OSS all retain the destinations stated above.

## Sources

Read27 November2026 for the operative passages used here; future-effective text is kept separate from2026 rules. Skatteverket guidance is administrative practice; the Acts control. Hypothetical case values are inputs/computed results, not authority figures.

| Source | URL | Read on |
|---|---|---|
| ML2023:200, operative cited chapters; current consolidation includes2026:1918 and future text; read in part for the specific operative sections cited above | https://data.riksdagen.se/dokument/sfs-2023-200.text | 2026-11-27 |
| SFL2011:1244, cited registration/filing/penalty/refund/interest/reconsideration chapters; read in part for the specific operative sections cited above | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-11-27 |
| SFF2011:1261,22kap.1–2 §§, whole SEK and discarded öre; read in part for the specific operative sections cited above | https://data.riksdagen.se/dokument/sfs-2011-1261.text | 2026-11-27 |
| IL1999:1229,16kap.2 § and67kap.11a § only; read in part for the specific operative sections cited above | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-11-27 |
| Statutory time calculation1930:173,2 §; read in part for the specific operative sections cited above | https://data.riksdagen.se/dokument/sfs-1930-173.text | 2026-11-27 |
| SFS2026:707, enacted registration/refund provisions and1July commencement; read in part for the enacted provision and commencement sentence | https://svenskforfattningssamling.se/sites/default/files/sfs/2026-05/SFS2026-707.pdf | 2026-11-27 |
| SFS2026:1025, repossession amendment effective20November; read in part for the enacted provision and commencement sentence | https://svenskforfattningssamling.se/sites/default/files/sfs/2026-06/SFS2026-1025.pdf | 2026-11-27 |
| SFS2026:110, enacted surcharge provision and1April commencement; read in part for the enacted provision and commencement sentence | https://svenskforfattningssamling.se/sites/default/files/sfs/2026-02/SFS2026-110.pdf | 2026-11-27 |
| Skatteverket, Fylla i momsdeklarationen; read in part for the ruta05–62 definitions | https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html | 2026-11-27 |
| Skatteverket, Lämna momsdeklaration via fil; read in part for the XML integers, representation authority and sign/receipt boundary | https://www.skatteverket.se/foretag/moms/deklareramoms/lamnamomsdeklarationviafilietjansten.4.2fb39afe18dabf1e4d223cc.html | 2026-11-27 |
| Skatteverket, Deklarera moms; read in part for the operative procedure or conditions stated in this Guide | https://www.skatteverket.se/foretag/moms/deklareramoms.4.7459477810df5bccdd480006935.html | 2026-11-27 |
| Skatteverket, När ska jag deklarera moms; read in part for the periods, annual dates and extension interest | https://www.skatteverket.se/foretag/moms/deklareramoms/narskajagdeklareramoms.4.6d02084411db6e252fe80008988.html | 2026-11-27 |
| Skatteverket, Momssatser; read in part for the food/restaurant/vouchers/hotel/transport conditions | https://www.skatteverket.se/foretagochorganisationer/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html | 2026-11-27 |
| Skatteverket, Avdrag för moms vid representation; read in part for the meal cap, proportion and flat alternative | https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/avdragformomsvidrepresentation.4.15532c7b1442f256baec84b.html | 2026-11-27 |
| Skatteverket, Köpa varor eller tjänster till företaget; read in part for the operative procedure or conditions stated in this Guide | https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/kopavarorellertjanstertillforetaget.4.7459477810df5bccdd480005156.html | 2026-11-27 |
| Skatteverket, Bilar och moms; read in part for the purchase/hire, body definitions and private-use conditions | https://www.skatteverket.se/foretag/moms/sarskildamomsregler/bilarochmoms.4.58d555751259e4d6616800010628.html | 2026-11-27 |
| Skatteverket, Omvänd betalningsskyldighet inom byggsektorn; read in part for the operative procedure or conditions stated in this Guide | https://www.skatteverket.se/foretag/moms/sarskildamomsregler/byggverksamhet/omvandbetalningsskyldighetinombyggsektorn.4.47eb30f51122b1aaad28000545.html | 2026-11-27 |
| Skatteverket, I vissa fall behöver du inte registrera; read in part for the operative procedure or conditions stated in this Guide | https://www.skatteverket.se/foretag/moms/momsregistrering/ivissafallbehoverduinteregistreradittforetagformoms.4.3152d9ac158968eb8fd1efe.html | 2026-11-27 |
| Skatteverket, Betala och få tillbaka moms; read in part for the operative procedure or conditions stated in this Guide | https://www.skatteverket.se/foretag/moms/betalaochfatillbakamoms.4.58d555751259e4d66168000354.html | 2026-11-27 |
| Skatteverket, Rätta en momsdeklaration; read in part for the operative procedure or conditions stated in this Guide | https://www.skatteverket.se/foretag/moms/deklareramoms/rattaenmomsdeklaration.4.3684199413c956649b552c4.html | 2026-11-27 |
| Skatteverket, Periodisk sammanställning; read in part for the operative procedure or conditions stated in this Guide | https://www.skatteverket.se/foretag/moms/deklareramoms/periodisksammanstallningforvarorochtjanster.4.58d555751259e4d661680001093.html | 2026-11-27 |
| Skatteverket, Deklarera och betala moms i OSS; read in part for the operative procedure or conditions stated in this Guide | https://www.skatteverket.se/foretag/moms/deklareramoms/ansokomattredovisadistansforsaljningionestopshoposs/deklareraochbetalamomsionestopshop.4.40cab8f8197edf03e644dee.html | 2026-11-27 |
| Skatteverket, Sälja tjänster till andra EU-länder; read in part for the operative procedure or conditions stated in this Guide | https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/forsaljningtillandraeulander/saljatjanstertillandraeulander.4.76a43be412206334b89800010696.html | 2026-11-27 |
| Skatteverket, Ränta på skattekontot; read in part for the base/cost/income rates and applicable dates | https://www.skatteverket.se/privat/skatter/skattekontobetalaochfatillbaka/rantapaskattekontot.4.18e1b10334ebe8bc80002582.html | 2026-11-27 |

Not yet confirmed: only the specific non-usable outcomes listed under Refusals and boundaries, supplier questions and the preserved historical tests. No unconfirmed outcome is available for filing or computation; each has the partner-accountant referral.
