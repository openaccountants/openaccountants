---
name: sweden-vat-return
description: "Use this skill whenever asked to prepare, review, or classify transactions for a Swedish VAT return (momsdeklaration) for a self-employed individual or small business in Sweden. Trigger on phrases like \"prepare VAT return\", \"do the Swedish VAT\", \"momsdeklaration\", \"moms\", \"skattedeklaration\", or any request involving Swedish VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. Covers the 25%, 12% and 6% rates for 2026, including food at 6% from 1 April 2026 and 12% from 1 January 2028, ruta 05 to 62, periods, deadlines, skattetillägg and the Lämna momsdeklaration e-service. Load alongside vat-workflow-base and eu-vat-directive. ALWAYS read this skill before touching any Swedish VAT work. This Tier 2 draft supports source checking and reviewer questions; it does not authorise filing, payment or a tax position."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sweden-vat-return"
  jurisdiction: "SE"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Sweden VAT Return v2.4
> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Self-employed individuals and small businesses registered for VAT in Sweden under Mervärdesskattelag (2023:200) ('ML') and Skatteförfarandelag (2011:1244) ('SFL'), and the reviewers working with them. Skatteverket (Swedish Tax Agency) administers the tax. The return is the momsdeklaration, in SEK only. Legacy text also calls it the skattedeklaration, which is SFL's term.

Swedish VAT reporting periods in calendar 2026, read at 5 November 2026. ML was read to SFS 2026:1025 and SFL to SFS 2026:1305. Food at 6% from 1 April 2026 and 12% from 1 January 2028 are enacted. Older rules stay for a tax point before each change date.

### What this file is

This is the Swedish country file for `vat-workflow-base` and it sits beside `eu-vat-directive`. Those files own the workflow, output specification, question form, self-checks and EU layer, and this file adds Swedish content. It declares no `depends_on` key because the legacy file declared none; both companions must still be loaded. A national rule here prevails on a Swedish point, such as import reporting or the SEK distance sales limit. Its status is Tier 2, pending review.

### How to read the amounts

'Enacted' means read in the Act as consolidated by Riksdagen. 'Skatteverket practice' means stated by Skatteverket without a figure in the Act: it shows how the authority applies the law but does not bind a court. 'Held' means not proved, and the item appears on the 'Not yet confirmed' line. A workflow setting, such as a red flag threshold, is not law.

### Refusals and boundaries

These sit beside the refusals in `vat-workflow-base`. Each is a full stop: give the exact message, and classify nothing further.

- **R-SE-1, VAT group.** Trigger: the client is a member of a mervärdesskattegrupp (ML 4 kap. 7 to 14 §§). Message: 'VAT groups require consolidation across all group members. This skill does not cover them. Please refer the return to a qualified practitioner.'
- **R-SE-2, Fiscal representative.** Trigger: a non-resident supplier with a fiscal representative in Sweden. Message: 'Non-resident registrations with fiscal representatives have obligations beyond this skill. Please refer the return to a qualified practitioner.' The legal basis of the term in this setting is held.
- **R-SE-3, Partial exemption.** Trigger: the client makes both sales that give a right to deduct and sales that do not, and a purchase falls under ML 13 kap. 29 § and is not wholly deductible under 13 kap. 30 §. Message: 'You make both taxable and exempt supplies. Input VAT must be apportioned under ML 13 kap. 29 and 30 §§. Please ask an auktoriserad revisor to confirm the apportionment.'
- **R-SE-4, Flat-rate scheme.** Trigger: the client says it uses a flat-rate deduction scheme, for example in forestry or agriculture. Message: 'Flat-rate schemes require sector-specific calculations beyond this skill. Please refer the return to a qualified practitioner.' The word search of ML found 'schablon' only for flat-rate farmers abroad, so whether a Swedish scheme of this kind exists is held.
- **R-SE-5, Voluntary taxation of property.** Trigger: a property owner moving into or out of frivillig beskattning under ML 12 kap. (legacy term: frivillig skattskyldighet). Message: 'Moving into or out of frivillig beskattning can require capital goods adjustments beyond this skill. Please ask an auktoriserad revisor.'
- **R-SE-6, Margin schemes.** Trigger: the client sells under the travel agent scheme (ML 19 kap.) or the second-hand goods, art, collectibles and antiques scheme (ML 20 kap.). Message: 'Margin scheme transactions require transaction-level margin computation. This skill does not cover them. Please refer the return to a qualified practitioner.'
- **R-SE-7, Income tax.** Trigger: the user asks about an income tax return, not the momsdeklaration. Message: 'This skill handles the momsdeklaration only. For Swedish income tax, use the appropriate income tax skill.'

**Missing contract.** The legacy file pointed to `eu-vat-directive` Section 13 and R-EU-5. The directive file read at 5 November 2026 has no refusal catalogue, no Section 13 and no R-EU-5, and `vat-workflow-base` forbids inventing a code. Any row that legacy text sent to R-EU-5 is Needs Input, naming that missing contract. R-EU-12 stays as the base defines it.

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

| Item | Amount or rule | Position at 5 November 2026 | Source and limit |
| --- | --- | --- | --- |
| Standard rate | 25% | Enacted, in force. Applies unless ML 9 kap. 4 to 19 §§ give a lower rate. From 1 January 2028 the cross-reference reads 3 to 18 §§ (Lag 2026:119). | ML 9 kap. 2 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Hotel room letting and camping | 12% | Enacted, in force | ML 9 kap. 4 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Restaurant and catering services | 12%, excluding the part for spirits, wine and starköl | Enacted, in force | ML 9 kap. 5 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Art | 12% on delivery and EU acquisition of art under 20 kap. 7 § not under the margin scheme, and on import of art, collectibles and antiques under 20 kap. 7 to 9 §§ | Enacted, in force | ML 9 kap. 6 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Minor repairs | 12% on repairs of bicycles, shoes, leather goods, clothes and household linen | Enacted, in force | ML 9 kap. 7 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Passenger transport | 6%, except transport where the travel element is of subordinate importance | Enacted, in force | ML 9 kap. 8 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Books, newspapers and similar | 6% under ML 9 kap. 9 to 13 §§: books and similar, subject to 10 kap. 20 and 21 §§ and not wholly or mainly advertising; programmes and catalogues; radio and cassette newspapers; accessible goods; electronic equivalents not wholly or mainly advertising, moving image or audible music | Enacted, in force | ML 9 kap. 9 to 13 §§, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Culture and nature | 6% on admission to concerts, circus, theatre, opera, ballet or other similar performances; admission to dance events; admission to and showing of zoos; showing of nature areas outside tätort, national parks, nature reserves, national city parks and Natura 2000 areas | Enacted, in force from 1 July 2026 (Lag 2026:841). Older rules for an earlier tax point; Skatteverket says dance events were 25% to 30 June 2026. Cinema is not named: held. | ML 9 kap. 14 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Libraries and museums | 6% where not exempt under 10 kap. 30 § items 2 and 4 | Enacted, in force | ML 9 kap. 15 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Copyright | 6% on the rights in 9 kap. 16 and 17 §§. 9 kap. 16 § second paragraph excludes photographs, advertising, computer programs, and film or video with information, which stay at 25%. | Enacted, in force | ML 9 kap. 16 and 17 §§, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Sport | 6% on sport under 10 kap. 28 § not exempt under 10 kap. 29 §. Exempt where supplied by the state, a municipality or a non-economic association under 4 kap. 6 §. | Enacted, in force | ML 9 kap. 18 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Food from 1 April 2026 | 6% on food under Article 2 of the EU Food Regulation, except (1) water under Article 6 of the drinking water directive and (2) spirits, wine and starköl. Water bottled or in containers for sale is 6%. | Enacted, in force from 1 April 2026 (Lag 2026:118). Older rules, 12% on Skatteverket's statement, for a tax point before that date. | ML 9 kap. 19 § and transitional note 2026:118, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Food from 2028 | 12% on the same food with the same exceptions, moved to ML 9 kap. 3 § | Enacted, not yet in force: applies from 1 January 2028 (Lag 2026:119). Older rules for an earlier tax point. | ML 9 kap. 3 § marked I:2028-01-01, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Exempt with right to deduct | No output VAT, input VAT deductible: the list in ML 13 kap. 10 §, including medicines under 10 kap. 13 §, EU supplies and exports. ML has no 'zero rate'. | Enacted, in force | ML 13 kap. 10 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Small business exemption | Turnover not above SEK 120,000 in the calendar year and not above it in either of the 2 preceding years | Enacted, in force (Lag 2024:942). Skatteverket says the seat must be in Sweden. | ML 18 kap. 4 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| EU small business scheme | EUR 100,000, with identification from the home state | Enacted, in force. A seat outside the EU cannot use it. | ML 18 kap. 5 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Artist's own art | Exempt where (1) the author or estate makes the supply, (2) the author or estate owns the work at supply and (3) the bases for the tax year are together below SEK 300,000. On request, Skatteverket decides that the supplies are taxable whatever the bases, to the end of the second year after the decision year. Skatteverket says an artist selling for more than SEK 300,000 in a tax year pays 12% from the first krona. | Enacted, in force | ML 10 kap. 31 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| EU distance sales limit | SEK 99,680 | Enacted, in force. Conditions under 'Cross-border points'. | ML 6 kap. 62 to 64 §§, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Period bands | SEK 40 million and SEK 1 million of estimated tax base for the tax year, excluding EU acquisitions and imports | Enacted, in force | SFL 26 kap. 10 to 13 §§, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Cash method | Annual turnover normally at most SEK 3 million | Enacted, in force | ML 7 kap. 16 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Listed electronics | Buyer pays on mobile phones (apparatus made or adapted for use in an authorised network on specified frequencies, whether or not it has other uses), integrated circuits not built into end products, consoles, tablets and laptops where both parties are taxable persons who are or must be registered here, the base for these goods in an invoice is together above SEK 100,000, and the buyer's registration duty is not merely a consequence of the purchase | Enacted, in force | ML 16 kap. 16 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Capital goods | Input tax of at least SEK 50,000 (machines, inventory and the like) or at least SEK 100,000 (property). The test is input tax, not cost. | Enacted, in force | ML 15 kap. 4 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Representation, statutory cap | Tax on at most SEK 300 per person and occasion, excluding VAT | Enacted, in force | ML 13 kap. 25 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Representation, administered amounts | SEK 36 (12%); SEK 46 flat, or SEK 33 flat where food is 6%; SEK 180 peripheral costs; SEK 300 gifts | Skatteverket practice. SEK 18 is arithmetic (6% of 300), not a published figure. | https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/avdragformomsvidrepresentation.4.15532c7b1442f256baec84b.html |
| Hired cars | Half of the VAT on hire, where use in deductible activity is more than trivial. Skatteverket reads this as more than 100 mil a year, prorated. | 50% enacted; 100 mil is Skatteverket practice | ML 13 kap. 22 §; https://www.skatteverket.se/foretag/moms/sarskildamomsregler/bilarochmoms.4.58d555751259e4d6616800010628.html |
| Mixed use, 95% rule | Full deduction if the purchase is more than 95% for deductible transactions, or if the tax is at most SEK 1,000 and deductible consideration is more than 95% | Enacted, in force | ML 13 kap. 30 §, https://data.riksdagen.se/dokument/sfs-2023-200.text |
| Late filing fees | SEK 625; SEK 1,250 after a föreläggande; periodisk sammanställning SEK 1,250 | Enacted, in force | SFL 48 kap. 1, 5 and 6 §§, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Skattetillägg | 20%; 2% or 5% for period errors | Enacted, in force | SFL 49 kap. 11 and 13 §§, https://data.riksdagen.se/dokument/sfs-2011-1244.text |
| Interest | Basränta 2.5%; low 2.5%; high 17.5%; income 1.125% | Method enacted; figures are Skatteverket's published amounts, with basränta 2.5% from 1 December 2024 | SFL 65 kap. 3, 4 and 13 §§; https://www.skatteverket.se/privat/skatter/skattekontobetalaochfatillbaka/rantapaskattekontot.4.18e1b10334ebe8bc80002582.html |

Registration has no separate threshold. A person liable to VAT must register under SFL 7 kap. 1 §, and must notify Skatteverket before starting (7 kap. 2 §). The small business exemption above is what takes low turnover out, and it is automatic for an unregistered business (ML 18 kap. 8 §). Exceeding the limit ends it from that point (18 kap. 11 §): Skatteverket says to charge VAT from the sale that exceeded it and register. A business may elect taxation instead (18 kap. 15 §). The exemption gives no deduction (18 kap. 14 §). Turnover excludes VAT and fixed assets (18 kap. 19 to 23 §§). The invoice shows no VAT (18 kap. 41 §), and Skatteverket says it must state that the sale is exempt. Skatteverket may refuse registration where there is a clear risk (påtaglig risk) of its use wholly or almost wholly as a step in VAT evasion, deregister where it is so used or that risk exists, and show a VAT number as invalid where there is a clear risk of its use for VAT evasion (SFL 7 kap. 10 to 12 §§, printed as Lag 2026:707). Prop. 2025/26:128, which the Riksdag adopted on 6 May 2026 (SkU22), gives 1 July 2026 with no transitional rules, and Skatteverket also says from 1 July. The SFS text of Lag 2026:707 was not read.

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
| 22 | Services from outside the EU |
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
| 42 | Other sales: exempt sales, assembly, exempt rent, assets sold without deduction, prescription medicines and grants |
| 48 | Deductible input VAT. The e-service has a further field for earlier deducted VAT to pay back. |
| 49 | Sum of 10, 11, 12, 30, 31, 32, 60, 61 and 62, less 48. Always filled, 0 if nil. |
| 50 | Import base: customs value in SEK, duty and charges, and ancillary costs to the destination |
| 60, 61, 62 | Output VAT on imports at 25%, 12% and 6% |

Legacy text used 06 to 08 for sales by rate, 22 and 23 for non-EU goods and services, 36 for EU services and 37 for exports. Those mappings are wrong and are replaced above. A positive ruta 49 is payable and a negative one refundable.

### Output VAT

Sales at every rate go in ruta 05 unless they belong in 06 to 08, with output VAT in 10, 11 or 12 by rate.

**Food or restaurant service.** Skatteverket assesses the whole sale, from what the customer actually gets.

- Food without support services is 6%, including takeaway, food truck sales and ready food in shops.
- Food or drink with services that let the customer eat straight away, such as serving, table setting, dishwashing or premises with tables and chairs, is a restaurant service at 12%. Catering at the customer's premises is 12%.
- One purchase can carry both: bread taken away at 6%, coffee in the café at 12%.
- Spirits, wine, beer stronger than folköl, drinks containing spirits and tap water are 25%. Split mixed sales.
- Delivery by a separate firm is a separate service at 25%. The seller's own packaging and transport take the food's rate. Optional disposables are 25%.
- A single-purpose lunch voucher takes its rate by use; a multi-purpose voucher takes the rate on redemption.
- Conference packages with meals are 25%; hotel breakfast is 12%. Breakfast, parking, phone, sauna and laundry inside a room price are 12%, otherwise take their own rate. Parking is 25% unless subordinate. Goods transport is 25%. Recharged travel costs take the rate of the main supply.

**Exempt sales.** These go in ruta 42. They are not left off the return, as legacy text said. ML 10 kap.: post (4 and 5 §§); health care (6 to 13 §§, with 10 § listing taxable items such as glasses, pharmacist goods and animal care); social care (14 §); education (15 to 18 §§); groups (19 §); sport (28 and 29 §§); culture (30 and 31 §§); insurance (32 §, Skatteverket: car hire with compulsory insurance is taxable at 25%); banking and finance (33 §, excluding notary, debt collection, factoring administration and safe deposit); property (35 and 36 §§, with 12 taxable limbs). This list names the groups only and omits the limbs in each section. Any such sale raises R-SE-3 for shared costs.

**Uttag.** A car's private use is an uttag where its value is more than trivial and either (1) input VAT on acquisition was deductible in whole or part or (2) on hire the whole input VAT on rent was deductible (ML 5 kap. 31 §). A half deduction on hire therefore gives no uttag. The base is under 8 kap. 7 §.

### Input VAT

Deduct input VAT for the taxable business (ML 13 kap. 6 §), in ruta 48, subject to the following.

**Evidence.** Deduction must be substantiated (13 kap. 31 §) by an invoice (32 §). No invoice is needed under 33 § only if all 3 conditions are met: (1) there are special reasons, (2) other documentation can substantiate the deduction and (3) the tax relates to an EU acquisition or to reverse charge under 16 kap. 6 § or 8 to 16 §§. Import needs the import document and evidence of the importer (35 §). With no accepted document, there is no deduction. This default is fixed by the law: disclose it.

**Representation (ML 13 kap. 24 and 25 §§ with IL 16 kap. 2 §).** ML 13 kap. 25 § allows input VAT on meals if (1) the cost has an immediate connection to the business, such as starting or keeping business relations, (2) it is reasonable, and (3) the deduction is at most the tax on SEK 300 per person and occasion, excluding VAT. Legacy 'alcohol never deductible' is the income tax result; Skatteverket counts alcohol for VAT.

- Food and non-alcoholic drink at 12%: up to SEK 36 per person. At 6%: up to SEK 18 by arithmetic.
- Food and alcohol above SEK 300: split the capped base by actual net cost, apply the food rate to the food share and 25% to the alcohol share.
- Or the flat amount: SEK 46 per person if cost is above SEK 300 net per person and VAT is at least SEK 46 per person; SEK 33 if food is at 6% and VAT is at least SEK 33 per person.
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

**Other limits.** Private use: no deduction (Skatteverket). Permanent housing: no deduction (13 kap. 26 §), except tax relating to (1) inputs for services under 5 kap. 32 to 34 §§ taxed as uttag and (2) a jordbruksarrende, including its dwelling part (27 §). Home office: Skatteverket says purchases connected with the home normally give no deduction, but a workplace wholly separated from the home and specially adapted to the business does. Mixed property: 13 kap. 13 to 15 §§. Private and business use of one asset: Skatteverket gives 3 options (full deduction with uttag, private portion excluded, or proportional). Pre-start purchases are deductible if meant for taxable activity. Foreign VAT is never in ruta 48: claim a refund from that country. Staff gifts: IL 11 kap. 14 § on gifts of lesser value is income tax, and no VAT limit was found, so the position is held.

**Apportionment.** ML 13 kap. 29 § requires deduction only for the part that is deductible, or by reasonable division if the part cannot be fixed. Skatteverket accepts division by turnover, time or area, documented. 13 kap. 30 § is in the rates table. See R-SE-3.

### Reverse charge in Sweden (ML 16 kap.)

| Rule | Who pays | Boxes |
| --- | --- | --- |
| Goods, or services connected to property in Sweden, where the buyer is registered here and the supplier is a taxable person not established here (6 §). Not property services under 13 § or 12 kap. The supplier may ask to be liable instead, for all such supplies (7 §). | Buyer | 23 or 24, 30 to 32, 48 |
| Electricity, gas, heating or cooling under 6 kap. 21 to 28 §§, where the buyer is registered here and the supplier is a taxable person not established here (8 §) | Buyer | 23, 30, 48 |
| Services under 6 kap. 33 § from a taxable person not established in Sweden (9 §). Buyer is (1) a taxable person, (2) a non-taxable legal person registered here, or (3) a legal person that would be taxable but for 4 kap. 6 § | Buyer | 21 or 22, 30 to 32, 48 |
| Subsequent supply in Sweden under 10 kap. 51 §, where (1) the recipient is another taxable person or a non-taxable legal person, (2) the recipient is registered here and (3) the supplier issued an invoice under Articles 219a to 237 of the VAT directive (10 §) | Recipient | Held for the recipient. 37 and 38 are a middleman's boxes. |
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
- Prepayments: output when received, input when paid (7 kap. 7 §; Skatteverket). The output rule applies only if the supply is taxable when the payment is received, and not to a supply or transfer of goods exempt under 10 kap. 42 and 46 §§. Construction: 7 kap. 8 §. EU acquisitions: 7 kap. 26 §. Import: 7 kap. 27 §. Input timing: 7 kap. 31 to 34 §§.
- Discounts: 8 kap. 14 §. Retaken goods: 8 kap. 15 §, whose printed text changes on 20 November 2026 under Lag 2026:1025. Bad debts reduce the base: 8 kap. 16 §. Revaluation: 8 kap. 17 §.
- Currency: use the latest average rate on the most representative Swedish market at the tax point, or the latest ECB rate (8 kap. 21 §); cross via euro (22 §); euro accounts (23 §). Legacy 'transaction date, Riksbank' is corrected. OSS uses the ECB rate for the last day of the period.
- There is no carry-forward box. Skatteverket pays a refund automatically if a payout account is registered, otherwise it stays on the skattekonto. Legacy 'credit brought forward' is a skattekonto balance question.

### Capital goods (ML 15 kap.)

Adjustment applies to (1) machines, inventory and the like of declining value with input tax on acquisition of at least SEK 50,000; (2) property new build, extension or rebuilding with input tax on that work of at least SEK 100,000; (3) property and leased or co-operative flats with uttag under 5 kap. 32 § where a deduction under 13 kap. 8 § item 4 or 5 is at least SEK 100,000; (4) rebuilding of a bostadsrätt or hyresrätt with input tax of at least SEK 100,000 (15 kap. 4 §). Cases are in 15 kap. 7 §; aggregation in 6 §. No adjustment under 5 percentage points (9 §). The period is 10 years for limbs 2, 3 and 4 and 5 years for other capital goods (10 §). On changed use, adjust yearly at 1/10 or 1/5 for the rest of the period (12 and 16 §§). On moving to 18 kap., adjust once for the rest of the period unless the person opposes it, and despite opposition for special reasons (12 §). On a transfer, and on the bankruptcy of a property owner, bostadsrätt holder or tenant under 7 § 6, adjust once for the rest of the period (13 §). The 25% cap applies only to 7 § 3, a taxable sale of a capital good other than property whose input tax was only partly deductible: the adjustment is at most 25% of the price (18 §). Legacy 'cost excl. VAT at least SEK 200,000' is wrong, as the test is input tax and the movable limit is SEK 50,000. Below the limits 15 kap. makes no adjustment; ruta 48 still follows the ordinary rules and limits in 13 kap.

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
| RÄNTA, INTEREST | Not a purchase with VAT | Interest income in ruta 42 is held |
| LÅN, LOAN, AMORTERING | Principal, outside the return | Document shows a loan |
| SKATTEVERKET, MOMS (payment) | Exclude: a tax payment is not a supply for consideration (ML 3 kap. 1 §) | Payment, not a fee |
| TULLVERKET | Exclude duty | Import VAT from the customs bill: ruta 50, 60 to 62 |
| BOLAGSVERKET, FÖRSÄKRINGSKASSAN, KRONOFOGDEMYNDIGHETEN | Exclude if no VAT is shown | ML 4 kap. 4 § public authority rule; authority for each body is held |
| ARBETSGIVARAVGIFTER, SOCIALA AVGIFTER, PRELIMINÄRSKATT, F-SKATT | Exclude: tax payments | Payment, not a fee |
| LÖN, SALARY, WAGES (outgoing) | Exclude (ML 4 kap. 2 §) | Employee, not a contractor |
| A-KASSA, FACKFÖRBUND | Exclude if no VAT is shown | Authority held |
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
| BOSTADSRÄTT | Exclude if no VAT is shown | Authority held; private or business |
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

The legacy file says Handelsbanken uses semicolons with YYYY-MM-DD, SEB tabs and Swedbank semicolons, with Datum, Text, Belopp and Saldo. These layouts are not verified: read the header of each file.

Hyra is rent, lön salary, ränta interest, överföring transfer, uttag withdrawal and insättning deposit. Own-account transfers ('överföring', 'eget konto', 'intern') are excluded. Sole trader transfers to a personal account are drawings: exclude. Refunds ('återbetalning', 'kreditnota', 'retur') are negative in the same ruta.

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
| Tax year, natural persons and estates filing an income return, no EU trade | 12 May | SFL 26 kap. 33 a § |
| Tax year, legal persons except estates and HB, filing an income return, with no EU trade under 33 a § second paragraph | Year ending 31 December: 12 July. 30 April: 12 November. 30 June: 27 December. 31 August: 12 March. Electronic filing may be made in the following month: by the 17th in January and August, and the 12th in April and December. Skatteverket groups year-ends. January to April: 12 November (digital 12 December). May to June: 27 December (17 January). July to August: 12 March (12 April). September to December: 12 July (17 August). | SFL 26 kap. 33 b §; Skatteverket |
| Tax year, others including EU trade, HB, KB, VAT groups, enkla bolag representatives and partrederier | 26th of the second month after the year; 27 December. Skatteverket: 26 February for a sole trader with EU trade. | SFL 26 kap. 33 § |

A deadline on a Saturday, Sunday, public holiday, Midsummer Eve, Christmas Eve or New Year's Eve moves to the next weekday (Lag (1930:173) 2 §).

**Extensions.** Anstånd for special reasons: SFL 36 kap. 5 §, with a 12 June limit for 33 a filers unless synnerliga skäl, and synnerliga skäl for 33 b filers. Byråanstånd to 26 June: 36 kap. 6 §, for 33 a filers using professional help, and it may be refused. Apply by the deadline. A filing extension is not a payment extension: Skatteverket charges interest from the day after 12 May despite byråanstånd.

**Portal and filing.** File in Skatteverket's e-service **Lämna momsdeklaration**, by XML upload or manual entry; from an accounting system by API with signing in **Mina sidor**; or on paper form SKV 4700, ordered through Beställ blanketter. For a nil return, press Deklarera noll in the e-service, or write 0 in ruta 49 on paper. XML upload rejects decimals: amounts must be whole numbers. The rounding method, and the position on manual entry and paper, are held.

**Payment.** To the skattekonto: bankgiro 5050-1055 with OCR. Skatteverket gives an international number for a foreign account. Paid means booked on the account by the deadline.

**Refund.** Skatteverket may withhold excess input VAT where it has opened a check of the return, there is a risk of tax evasion and the excess is a significant amount. The decision covers at most the excess within the check, for up to 2 years, extendable by 6 months at a time where the check cannot be finished in that time and special reasons exist (SFL 63 a kap. 1 to 3 §§, printed as Lag 2026:707; interest 65 kap. 7 a §). Prop. 2025/26:128, which the Riksdag adopted on 6 May 2026 (SkU22), gives 1 July 2026 with no transitional rules. The SFS text of Lag 2026:707 was not read.

**Corrections.** Redo the return in the accounting system, in 'Se och rätta inlämnade momsdeklarationer', or with a new paper return or letter. Request by the 6th year after the calendar year in which the tax year ended (SFL 66 kap. 7 §); within 2 months of notice for the 18 kinds of decision that section lists, including registration, föreläggande and payment or refund of tax.

**Related filing.** Periodisk sammanställning: SFL 35 kap. 2 to 4 and 9 §§. Due the 25th in the month after the period if electronic, otherwise the 20th in that month. See 'Cross-border points'.

## Penalties and interest

**Late filing (förseningsavgift).** SEK 625 for a skattedeklaration, SEK 1,250 after a föreläggande, and SEK 1,250 for a periodisk sammanställning (SFL 48 kap. 1, 5 and 6 §§).

**Skattetillägg.**

- Grounds: oriktig uppgift for own tax (SFL 49 kap. 4 §), meaning data clearly (1) incorrect, (2) omitted or (3) on a transaction that was a step in VAT evasion, where the person knew or should have known, but not where the data together suffice for a correct decision or are obviously unusable (5 §, printed as Lag 2026:110; SkU6, which the Riksdag adopted on 25 February 2026, gives 1 April 2026 and records no need for transitional rules; the SFS text was not read); skönsbeskattning (6 §).
- Rate: 20% of the tax not determined or wrongly credited (11 §, the 'annan skatt' rate, as VAT is not in the 56 kap. 3 § list). Period errors: 2% where the period is at most 3 months and the shift is within 4 months, otherwise 5% (13 §). Skönsbeskattning: 20% (15 §).
- A skattetillägg on skönsbeskattning for a missing return is withdrawn where the return is filed within 2 months from the end of the decision month, or from the day the person learnt of it if they show it is likely they did not know before that month ended (7 §).
- No skattetillägg if data for matching were available to Skatteverket within 1 year from the end of the tax year, on own-initiative correction (not if general control informed, the correction is connected to it and made after 2 months), or for a trivial amount (10 §).
- Relief, full or partial, where unreasonable: age, health, misjudgment, disproportion or delay (51 kap. 1 §).

**Interest.** Daily on the skattekonto (SFL 65 kap. 2 to 4 §§). Basränta is 125% of the 6-month treasury bill rate, with a 1.25% floor (3 §). Cost at basränta; income at 45% of it, or 0 where basränta is set at that floor (4 §). Late: basränta plus 15 percentage points until registration with Kronofogden (13 §, Förordning 2026:146). Relief needs synnerliga skäl (15 §). Skatteverket's page gives the amounts in the rates table. Skatteverket's brochure SKV 408 repeats the method and points to the site for current rates.

## Cross-border points

**Goods sold to the EU (ML 10 kap. 42 and 43 §§, subject to 47 §).** Exempt with deduction, ruta 35, if (1) the buyer is a taxable person or a non-taxable legal person acting as such in another EU country, (2) the buyer has a VAT number there and has given it, and (3) the seller filed a correct periodisk sammanställning or satisfactorily explains why not. The goods must be sent or transported by the seller or buyer, or on either's behalf, from Sweden to another EU country (42 §). Check the VAT number on VIES and keep evidence of the transport; the proof rule is held. A failed VIES check is not by itself a rate: Needs Input, then test each condition, place and rate. The directive file's local-rate result is applied only after that.

**Services sold to the EU.** Under 6 kap. 33 to 36 §§, a service to a taxable person is taxed where the buyer has its business. Ruta 39, with no Swedish VAT. Skatteverket: a valid VAT number given by the buyer normally suffices, and the sale then goes in the periodisk sammanställning. Without the number, other evidence can show status, such as a tax authority certificate; the sale then goes in ruta 39 and is not listed. If the seller cannot show status, the buyer is treated as non-taxable and the rules for those buyers apply. Other services abroad and services to non-EU buyers: ruta 40.

**Exports (ML 10 kap. 64 to 68 §§).** Exempt with deduction (13 kap. 10 §). Goods under 64 to 66 §§ go in ruta 36. Services under 67 and 68 §§ are not goods, and Skatteverket says services exempt in Sweden go in ruta 42. A service supplied abroad under 6 kap. is assessed separately for ruta 39 or 40. The conditions of those sections apply; check them on each sale.

**EU acquisitions.** Ruta 20, output in 30 to 32, input in 48 (ML 16 kap. 17 §). The seller must be VAT registered in another EU country, the goods must move between EU countries and the buyer must give a valid VAT number (Skatteverket). No Swedish VAT is computed on a purchase from an unregistered seller, such as a private person.

**Imports.** A registered importer reports to Skatteverket, not Tullverket: ruta 50, output in 60 to 62, input in 48 where deductible (ML 16 kap. 18 to 22 §§). Report in the period the tullräkning or tullkvitto was issued, whichever accounting method is used (Skatteverket). A business not registered at import pays Tullverket. `eu-vat-directive` 4.5 says import VAT is paid at Customs, which is this unregistered case.

**Triangular trade.** Ruta 37 and 38 apply only where a seller in one EU country sells to a middleman in another, the goods go directly to a customer in a third EU country, and all 3 parties are VAT registered in their own countries. The middleman pays no VAT on that purchase, and ruta 38 also goes in the periodisk sammanställning (Skatteverket). Other qualifying EU acquisitions of goods go in ruta 20, not ruta 37. Separately, where the goods go directly to Sweden, ML 10 kap. 51 § exempts the foreign middleman's acquisition and 16 kap. 10 § makes the recipient in Sweden liable if its conditions are met. The recipient's box is held.

**EU distance sales and OSS.** For a seller established in Sweden and not in another EU country, or with no establishment but resident or staying here and not in another EU country, supplying 6 kap. 56 § services or 6 kap. 8 § goods to non-taxable buyers in another EU country, Swedish VAT applies while the combined value excluding VAT is not above SEK 99,680 in the current and previous year (6 kap. 62 §). From the supply exceeding it, the supply is abroad (63 §), and the seller may opt earlier (64 §). This replaces legacy €10,000, which is the directive figure, and covers both goods and services. Above the limit or on option: Needs Input, because the legacy R-EU-5 contract is missing. OSS is a separate return in EUR, due the last day of the month after the quarter (import scheme monthly), with no input deduction, ECB rate conversion and required nil returns, and it is not reported in the momsdeklaration (Skatteverket). Payment details come from Skatteverket's OSS page.

**Periodisk sammanställning.** Filed in the e-service Periodisk sammanställning or Filöverföring, or on SKV 5740, only when there are sales. Goods: monthly. Services: quarterly. Both goods and services: monthly (SFL 35 kap. 3 §). A seller moving from quarterly to monthly stays monthly to the fourth calendar quarter after the change. Goods quarterly on request (form SKV 4853), only if goods are at most SEK 500,000 excluding VAT in the quarter of the application and each of the 4 quarters before it, with no other reason for monthly listing. The decision lapses when the limit is exceeded (SFL 35 kap. 4 §; Skatteverket). Call-off stock: SKV 5739. Whole kronor. Ruta 35 and 38 tie to it. Services are listed only where taxable in the buyer's country, so ruta 39 may differ.

**Passenger transport.** Supplied in Sweden only if no part takes place abroad (ML 6 kap. 39 §). An international flight is therefore outside Sweden for its whole length, not '0%'.

**Norway.** Norway is outside the EU, so goods sold there are exports and goods bought from there are imports. A delivery in Sweden to a natural person resident in Norway or on Åland is exempt only if (1) it is goods or a group forming a whole, at SEK 1,000 or more after VAT, and (2) the seller can show the buyer took them there soon after delivery and paid the equivalent tax under a customs bill or similar document (ML 10 kap. 65 §).

## Two worked examples that recompute

These are from a hypothetical Swedish self-employed IT consultant registered for VAT, on quarterly periods. Example 7 rolls them up. Each assumes the document is held. The rounding method is held, so exact öre are shown.

### Example 1: Non-EU SaaS reverse charge (Notion)

`03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; SEK 166.88`

If the invoice names the US entity, no Swedish VAT and a service under the main rule: ruta 22 SEK 166.88, ruta 30 SEK 41.72, ruta 48 SEK 41.72. Net effect 0. If the invoice names an EU entity, use ruta 21; if it shows Swedish VAT, it is an ordinary purchase. Convert under ML 8 kap. 21 §: the bank's SEK figure is not automatically that rate.

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

If the buyer gave a valid German VAT number: ruta 39 SEK 35,000, no Swedish VAT, and a line in the periodisk sammanställning. Check the number on VIES. If there is no number but other evidence shows a taxable person buying for its business: ruta 39 SEK 35,000, no Swedish VAT and no listing. If status is unproved, this is Needs Input, not 25%: the buyer then counts as non-taxable, and the place rule for that service decides whether Swedish VAT applies. All 3 cases are given to the reviewer.

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

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Mervärdesskattelag (2023:200), Riksdagen consolidation to SFS 2026:1025, read in part, for the sections in the read log: chapters 2 to 10, 12 (5 and 6 §§ only), 13, 15, 16, 18 and transitional notes. 10 kap. 44 to 48 §§ and 7 kap. 26, 27 and 31 to 34 §§ by heading or position only; 19 and 20 kap. headings only; 4 kap. 7 to 14 §§ scanned | https://data.riksdagen.se/dokument/sfs-2023-200.text | 2026-11-05 |
| Skatteförfarandelag (2011:1244), consolidation to SFS 2026:1305, read in part, for the sections in the read log: chapters 7, 26, 35, 36, 48, 49, 51, 56, 62, 63 a, 65, 66; 5 kap. representative sections only partly | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-11-05 |
| Inkomstskattelag (1999:1229), read in part: 11 kap. 14 §, 16 kap. 2 §, 67 kap. 11 a § | https://data.riksdagen.se/dokument/sfs-1999-1229.text | 2026-11-05 |
| Lag (1930:173), read in full | https://data.riksdagen.se/dokument/sfs-1930-173.text | 2026-11-05 |
| Skatteverket, Fylla i momsdeklarationen, read in part for boxes | https://www.skatteverket.se/foretag/moms/deklareramoms/fyllaimomsdeklarationen.4.3a2a542410ab40a421c80004214.html | 2026-11-05 |
| Skatteverket, Lämna momsdeklaration via fil, read in part for file fields | https://www.skatteverket.se/foretag/moms/deklareramoms/lamnamomsdeklarationviafilietjansten.4.2fb39afe18dabf1e4d223cc.html | 2026-11-05 |
| Skatteverket, Deklarera moms, read in part for portal | https://www.skatteverket.se/foretag/moms/deklareramoms.4.7459477810df5bccdd480006935.html | 2026-11-05 |
| Skatteverket, När ska jag deklarera moms, read in part for periods and dates | https://www.skatteverket.se/foretag/moms/deklareramoms/narskajagdeklareramoms.4.6d02084411db6e252fe80008988.html | 2026-11-05 |
| Skatteverket, Momssatser, read in part for rates and the food test | https://www.skatteverket.se/foretagochorganisationer/moms/saljavarorochtjanster/momssatspavarorochtjanster.4.58d555751259e4d66168000409.html | 2026-11-05 |
| Skatteverket, Livsmedelsmomsen sänks till 6 procent, read in part for the food change | https://www.skatteverket.se/omoss/pressochmedia/nyheter/2026/nyheter/livsmedelsmomsensankstill6procent.5.70685bee19c85dd5dd0a3f.html | 2026-11-05 |
| Skatteverket, Avdrag för moms vid representation, read in part for amounts | https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/avdragformomsvidrepresentation.4.15532c7b1442f256baec84b.html | 2026-11-05 |
| Skatteverket, Köpa varor eller tjänster till företaget, read in part for input VAT | https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/kopavarorellertjanstertillforetaget.4.7459477810df5bccdd480005156.html | 2026-11-05 |
| Skatteverket, Bilar och moms, read in part for cars | https://www.skatteverket.se/foretag/moms/sarskildamomsregler/bilarochmoms.4.58d555751259e4d6616800010628.html | 2026-11-05 |
| Skatteverket, Omvänd betalningsskyldighet inom byggsektorn, read in part for construction | https://www.skatteverket.se/foretag/moms/sarskildamomsregler/byggverksamhet/omvandbetalningsskyldighetinombyggsektorn.4.47eb30f51122b1aaad28000545.html | 2026-11-05 |
| Skatteverket, Omvänd betalningsskyldighet, read in part for reverse charge | https://www.skatteverket.se/foretag/moms/sarskildamomsregler/omvandbetalningsskyldighet.4.47eb30f51122b1aaad28000258292.html | 2026-11-05 |
| Skatteverket, I vissa fall behöver du inte registrera, read in part for the exemption | https://www.skatteverket.se/foretag/moms/momsregistrering/ivissafallbehoverduinteregistreradittforetagformoms.4.3152d9ac158968eb8fd1efe.html | 2026-11-05 |
| Skatteverket, Betala och få tillbaka moms, read in part for payment and refund | https://www.skatteverket.se/foretag/moms/betalaochfatillbakamoms.4.58d555751259e4d66168000354.html | 2026-11-05 |
| Skatteverket, Rätta en momsdeklaration, read in part for corrections | https://www.skatteverket.se/foretag/moms/deklareramoms/rattaenmomsdeklaration.4.3684199413c956649b552c4.html | 2026-11-05 |
| Skatteverket, Periodisk sammanställning, read in part for the listing | https://www.skatteverket.se/foretag/moms/deklareramoms/periodisksammanstallningforvarorochtjanster.4.58d555751259e4d661680001093.html | 2026-11-05 |
| Skatteverket, Deklarera och betala moms i OSS, read in part for OSS | https://www.skatteverket.se/foretag/moms/deklareramoms/ansokomattredovisadistansforsaljningionestopshoposs/deklareraochbetalamomsionestopshop.4.40cab8f8197edf03e644dee.html | 2026-11-05 |
| Skatteverket, Sälja tjänster till andra EU-länder, read in part for buyer status | https://www.skatteverket.se/foretag/moms/saljavarorochtjanster/forsaljningtillandraeulander/saljatjanstertillandraeulander.4.76a43be412206334b89800010696.html | 2026-11-05 |
| Skatteverket, Köpa varor från andra EU-länder, read in part for acquisitions | https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/inkopfranandraeulander/kopavarorfranandraeulander.4.3a7aab801183dd6bfd380005738.html | 2026-11-05 |
| Skatteverket, Köpa tjänster från andra EU-länder, read in part for ruta 21 | https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/inkopfranandraeulander/kopatjansterfranandraeulander.4.361dc8c15312eff6fd1d011.html | 2026-11-05 |
| Skatteverket, Köpa varor från länder utanför EU, read in part for import | https://www.skatteverket.se/foretag/moms/kopavarorochtjanster/inkopfranlanderutanforeu/kopavarorfranlanderutanforeuimport.4.361dc8c15312eff6fd37208.html | 2026-11-05 |
| Skatteverket, Uthyrning av fastighet och frivillig beskattning, read in part for rent | https://www.skatteverket.se/foretag/moms/sarskildamomsregler/fastighetsverksamhet/uthyrningavfastighetochfrivilligbeskattning.4.18e1b10334ebe8bc80005741.html | 2026-11-05 |
| Skatteverket, Ränta på skattekontot, read in part for interest | https://www.skatteverket.se/privat/skatter/skattekontobetalaochfatillbaka/rantapaskattekontot.4.18e1b10334ebe8bc80002582.html | 2026-11-05 |
| Skatteverket, Skattekontobroschyren SKV 408 edition 13, read in part for interest | https://www.skatteverket.se/download/18.70685bee19c85dd5dd0325b/1774273676580/Skattekontobroschyren-skv408-utgava13.pdf | 2026-11-05 |
| Skatteverket, Nya lagar från halvårsskiftet 2026, read in part for the 1 July change | https://www.skatteverket.se/omoss/pressochmedia/nyheter/2026/nyheter/nyalagarfranhalvarsskiftet2026.5.650b4a9d19ebd1653db1700.html | 2026-11-05 |
| Proposition 2025/26:128, read in part for commencement and transitional rules; a bill, not enacted text | https://data.riksdagen.se/dokument/HD03128.text | 2026-11-05 |
| Betänkande 2025/26:SkU22, read in part for the decision and commencement; a committee report, not enacted text | https://data.riksdagen.se/dokument/HD01SkU22.text | 2026-11-05 |
| Betänkande 2025/26:SkU6, read in part for the decision and commencement; a committee report, not enacted text | https://data.riksdagen.se/dokument/HD01SkU6.text | 2026-11-05 |

Not yet confirmed: ML and SFL amendments made after the consolidations named in Sources; the SFS text of the amending Acts behind SFL 7 kap. 10 to 12 §§, 49 kap. 5 § and 63 a kap., and so the link between those Act numbers and the bill dates, which rests on matching subject and sections; the rate for cinema, which ML 9 kap. 14 § does not name; 'certain medical aids' with a right to deduct, which legacy text claimed and the search of ML did not support; the SEK 500 staff gift limit for VAT; the earlier SEK 80,000 limit; the rounding method for whole kronor, and the position on manual entry and paper; the proof rule for transport of goods to another EU country; the box for a recipient in Sweden under ML 16 kap. 10 §; the basis of 'fiscal representative' here; whether a Swedish flat-rate scheme exists under R-SE-4; R-EU-5 and `eu-vat-directive` Section 13, which do not exist in the file read; every supplier billing entity, including those the legacy file named and Spotify; bank export layouts; the current basränta beyond Skatteverket's page; interest income in ruta 42; authority for excluding government fees, union fees and bostadsrätt fees; the date for the second version of Lag (1930:173) 2 §, which changes only brottsbalken references.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.2 | 2026-11-05 | Converted to the upstream template from primary text. Boxes, periods, capital goods limits, car and representation rules, citations and defaults corrected. Not reviewed by an accountant. |
| 2.1 | November 2026 | Filing deadlines by turnover band; SEK 120,000 exemption threshold. |
| 2.0 | April 2026 | Full rewrite to three-tier OpenAccountants architecture. |
| 1.0 | April 2026 | Initial draft. Standalone monolithic document. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an auktoriserad revisor, godkänd revisor or equivalent licensed practitioner in Sweden) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sweden-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sweden-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
