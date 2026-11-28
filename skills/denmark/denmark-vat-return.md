---
name: denmark-vat-return
description: "Danish VAT (moms) and the VAT return (momsangivelse) for 2026, for a business registered or registering in Denmark. Covers the single 25% rate and the zero-rated supplies (exports, intra-EU goods, newspapers, passenger air transport), the DKK 50,000 registration threshold and the EU SME scheme (EUR 100,000 EU turnover, EX number), half-yearly, quarterly and monthly periods by turnover with the 2026 deadlines, input VAT and its limits (cars, restaurants 25%, hotels, gifts, entertainment, partial deduction), domestic reverse charge, the boxes A, B and C, the EU sales list, invoices, digital bookkeeping from 2026, corrections, and the DKK 1,400 fee and interest for late returns. Trigger phrases: prepare VAT return, do the VAT, classify transactions for VAT from bank statements or invoices, moms, momsangivelse, Danish VAT return, momsfrister, EU-salg uden moms, momsfradrag, TastSelv Erhverv. Out of scope: income tax (dk-income-tax), company tax (dk-corporate-tax), payroll and lønsumsafgift (dk-payroll), cross-border income tax (dk-cross-border); OSS returns, margin schemes and property VAT are referred."
version: 2.4
jurisdiction: DK
tax_year: 2026
last_updated: 2026-11-28
depends_on:
  - vat-workflow-base
  - eu-vat-directive
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Denmark: VAT (moms) and the VAT return (2026)

> **Source-cited draft: not reviewed by an accountant.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any business's facts. Do not rely on it to file or pay without review by a qualified professional in Denmark.

“ML” below means Momsloven, read with the amendments identified in Sources; “MB” means Momsbekendtgørelsen. The operative provisions and authority instructions below were read on 28 November 2026. Use the business’s assigned period and documented transaction facts. The dependency Guides provide a preparation method and EU context; the Danish conditions below control this return.

## Who this applies to

- **Any taxable person who supplies goods or services in Denmark** must register (ML § 47, stk. 1), unless one of the exceptions below applies. A taxable person is anyone who independently carries on an economic activity, whatever the legal form: sole traders (enkeltmandsvirksomhed), partnerships, ApS and A/S companies.
- **Small business exemption.** A business established in Denmark is exempt from registration and from charging VAT while its Danish annual turnover under ML § 71 j does not exceed DKK 50,000 (ML § 71 e, stk. 1, in force from 1 January 2025; it replaced the old § 48). It cannot use the exemption in a year if it exceeded the threshold in the previous year, and the exemption ends from the moment the threshold is passed during the year (ML § 71 k, stk. 1). The turnover test is not simply all receipts or only standard-rated sales: include the zero-rated and non-incidental property/financial/insurance transactions specified in § 71 j and exclude disposals of investment assets. The artist’s DKK 350,000 exemption includes other supplies up to DKK 50,000 within that threshold; only one sector exemption can be used at a time (§ 71 e, stk. 2-3). A business under the threshold may still register voluntarily, for at least 2 calendar years (ML § 49).
- **Exempt activity only.** A business whose supplies are all exempt under ML § 13 (for example qualifying healthcare, education, insurance, financial services and letting of property) does not register for those supplies (ML § 47, stk. 1, nr. 1). It may still have to register for acquisitions or reverse-charge purchases, including foreign general-rule B2B services (ML §§ 50 and 50 b; see Cross-border points).
- **Foreign businesses.** A business established abroad that makes taxable supplies in Denmark must register unless the Danish customer is made liable under reverse charge (ML § 47, stk. 2, 3. pkt.). A business established outside the EU, in a country without a mutual-assistance agreement with Denmark, must register through a Danish representative (ML § 47, stk. 2). An EU business can use the Danish small business exemption only through the EU SME scheme (ML § 71 e, stk. 4). OSS-only registration treatment and every actual foreign registration are outside the usable filing route here. Check this point with one of our partner accountants.
- **Out of scope here:** OSS and IOSS returns, the margin schemes for second-hand goods, art and travel, VAT on buildings and land, VAT groups (fællesregistrering, ML § 47, stk. 4), lønsumsafgift (payroll tax on VAT-exempt businesses, see dk-payroll), and businesses that let cars or run a driving school (special car rules in ML § 42, stk. 6). These outputs are not usable from this Guide. Check this point with one of our partner accountants.
- **Also refer:** missing registration, invoice, customs, buyer VAT number or EU transport evidence (keep the records and name the unresolved route); an unclear exemption or place of supply; a food, hospitality, gift or vehicle cost that does not fit the rules below, or whose purpose or attendees are undocumented (do not claim it); and a negative or authority-corrected return outside the self-service route. Keep the amount unresolved, not silently zero. Check this point with one of our partner accountants.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate (the only positive rate) | 25% of the taxable amount | 2026 | ML § 33; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Zero rate (exempt with right to deduct): goods sent to a VAT-registered buyer in another EU country, exports outside the EU, newspapers published at least monthly (also electronic), passenger air transport | 0% | 2026 | ML § 34, stk. 1, nr. 1, 5, 18 and 22 (nr. 22 added by lov nr. 1693/2024 from 1 Jan 2025); https://www.retsinformation.dk/eli/lta/2024/1693/pdf |
| Prepayment received before delivery or invoice: taxable amount | 80% of the amount received (so VAT is 20% of the gross payment) | 2026 | ML § 27, stk. 1, 2. pkt.; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Registration threshold, business established in Denmark | Annual Danish turnover under ML § 71 j above DKK 50,000 | 2026 | ML § 71 e, stk. 1 (lov nr. 1693/2024); https://www.retsinformation.dk/eli/lta/2024/1693/pdf |
| Threshold for an artist's first sale of own works | DKK 350,000 a year | 2026 | ML § 71 e, stk. 2; https://www.retsinformation.dk/eli/lta/2024/1693/pdf |
| EU SME scheme: EU-wide turnover ceiling to use another country's exemption (or Denmark's, for an EU business) | EUR 100,000 in the previous or current year | 2026 | ML § 71 k, stk. 2 and 3; https://www.retsinformation.dk/eli/lta/2024/1693/pdf |
| Unregistered business: EU goods purchases before registration is needed | DKK 80,000 a year (current and previous year), no excise goods | 2026 | ML § 50; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Half-yearly period | Taxable supplies not above DKK 5 million a year | 2026 | ML § 57, stk. 4; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Quarterly period | Above DKK 5 million and up to DKK 50 million a year; also a new registration unless expected supplies exceed DKK 55 million | 2026 | ML § 57, stk. 3 and § 47, stk. 6; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Monthly period | Above DKK 50 million a year; a new registration expecting more than DKK 55 million | 2026 | ML § 57, stk. 2 and § 47, stk. 6; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Restaurant meals of a strictly business nature | 25% of the VAT is deductible | 2026 | ML § 42, stk. 2; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Long-term (over 6 months) lease of a passenger car | Deduct VAT on the rent up to 25% of a base of 2% a month of the registration tax (first 3 years), 1% after; at least 10% VAT-liable driving | 2026 | ML § 42, stk. 4 and 5; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Vans and trucks up to 3 tonnes used partly privately | All VAT on running costs; one third of rent VAT if hired, where supplies exceed DKK 50,000 (ML § 41, stk. 5) | 2026 | ML § 41, stk. 2 and 3; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Telephones placed at employees’ homes | 50% of VAT on bills addressed to and paid by the business, capped at VAT it actually bears | 2026 | ML § 40, stk. 2; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Capital goods adjustment applies to machinery, software and rights | Cost above DKK 100,000 excluding VAT | 2026 | ML § 43, stk. 2; https://www.retsinformation.dk/eli/lta/2024/209/pdf |
| Simplified invoice, subject to the full-invoice exceptions below | Supply of DKK 3,000 or less | 2026 | MB § 66, stk. 1; https://www.retsinformation.dk/eli/lta/2023/1435/pdf |
| Application for quarterly EU goods listing | Not on monthly VAT; EU goods sales not above DKK 400,000 in the quarter and each of the 4 previous quarters; separate service-only permission below | 2026 | MB § 99, stk. 4; https://www.retsinformation.dk/eli/lta/2023/1435/pdf |
| Fee for a provisional assessment when a return is late | DKK 1,400 per period | 2026 | Opkrævningsloven § 4, stk. 2 as amended by lov nr. 16/2025, § 1 (for assessments from 1 Feb 2025); https://www.retsinformation.dk/eli/lta/2025/16/pdf |
| Late-payment interest | Base rate 0.1% plus 0.85 points = 0.95% a month, charged per day as 0.95% x 12 / 365 of the unpaid amount (366 in a leap year) | 2026 | Opkrævningsloven § 7, stk. 1 and 2, and § 16 c, stk. 1; SKM2025.720.SKTST, https://info.skat.dk/data.aspx?oid=2459995; L 80 (2024-25) remarks, https://www.ft.dk/ripdf/samling/20241/lovforslag/l80/20241_l80_som_fremsat.pdf |
| Reminder fee (payment reminder; EU sales list reminder) | DKK 160 (was DKK 65 before 14 Sep 2026) | 2026 | Opkrævningsloven § 6 and ML § 54, stk. 3, as amended by lov nr. 763/2026; https://www.retsinformation.dk/eli/lta/2026/763/pdf |
| Digital bookkeeping duty, personally owned business | Net turnover above DKK 300,000 in 2 consecutive income years | 2026 | Bogføringsloven § 16, stk. 1; BEK nr. 297/2025; https://www.retsinformation.dk/eli/lta/2025/297/pdf |

The ordinary positive Danish rate is 25%. Distinguish ML § 34 exemptions with deduction from ordinary ML § 13 exemptions and the SME exemption. Deduction is not automatic for every exempt or foreign supply: ML § 37 contains exceptions and the input limits still apply.

## The taxable base

**Output VAT.** Output VAT is 25% of the consideration excluding VAT, including directly linked subsidies (ML § 27, stk. 1). The base includes other duties and taxes, incidental costs charged to the customer (commission, packing, shipping, insurance), connection fees and agent's commission (ML § 27, stk. 2). Each period's output VAT covers supplies, intra-EU acquisitions, imports and reverse-charge purchases for which VAT became due in the period (ML § 56, stk. 2).

**When VAT is due.** VAT is due on delivery (ML § 23, stk. 1). If an invoice is issued before or soon after delivery, the invoice date counts (stk. 2). A payment received before delivery or invoice makes VAT due on the payment date (stk. 3); the taxable amount is then 80% of what was received (ML § 27, stk. 1, 2. pkt.).

**Exempt supplies.** Ordinary ML § 13 supplies carry no output VAT and related input VAT is normally excluded. Special deduction rules in ML § 37, stk. 7-8 (certain foreign financial/insurance supplies and international passenger transport) need separate examination; an actual claim under them is not usable here. Check this point with one of our partner accountants.

 The following are ML § 13, stk. 1 categories, each subject to its statutory limits rather than automatic sector classification: hospital and medical care including physiotherapy and dentistry (nr. 1), social care (nr. 2), education (nr. 3), sport by non-profit bodies (nr. 5), cultural activities (nr. 6), authors' and artists' services (nr. 7), letting of property (nr. 8), supply of property other than new buildings and building land (nr. 9), insurance (nr. 10), financial services (nr. 11), lotteries (nr. 12) and qualifying passenger transport (nr. 15; commercial non-route bus transport is excluded and passenger air has the separate zero-rate rule). Exempt letting does not extend to hotel accommodation, short letting of rooms, camping, parking, advertising space or storage boxes; the property-sale exemption excludes new buildings and building land. Exemption eligibility must be established, not inferred from an industry label (ML § 13). Two changes matter now:
- From 1 January 2026 the education exemption covers "education of children and young people under 30, school teaching and teaching at higher education institutions, vocational training"; the wider wording "other teaching of a school-like or vocational nature" was removed (lov nr. 1783/2025, § 1, nr. 1). A course provider must test the actual course, age and statutory conditions; commercial courses primarily aimed at businesses/institutions remain excluded from the exemption. An unresolved education claim is not usable. Check this point with one of our partner accountants.
- From 1 July 2025 a licence to use an author's or artist's copyright is taxable when supplied by anyone other than the author or artist (ML § 4 d and § 13, stk. 1, nr. 7, by lov nr. 1695/2024). The author/artist exemption does not cover outright transfer of copyright, patents, trademarks and similar rights, or the listed patent/trademark licences; do not treat every intellectual-property sale as exempt.

**Input VAT: the main rule.** A registered business deducts VAT on purchases used only for its taxable supplies, including supplies made abroad (ML § 37, stk. 1). Deductible VAT includes VAT on domestic purchases, VAT on intra-EU acquisitions, import VAT and self-assessed reverse-charge VAT (ML § 37, stk. 2). The claim needs an invoice or customs document (MB § 83), For a domestic VAT invoice the supplier must be entitled to charge that VAT; reverse-charge and import deductions use their own documentation. A business purpose alone does not prove taxable use or remove a statutory block.

**When input VAT is booked.** Input VAT belongs to the period in which the purchase was delivered or cleared through customs (MB § 81, stk. 1). From 1 July 2025 a business may instead book input VAT when it books the expense in its accounts: as a rule in the period right after delivery, and at the latest in the period that falls 6 months after delivery (MB § 81, stk. 3, added by BEK nr. 518/2025). Payment-basis booking with adjustment for supplier balances is also allowed (MB § 81, stk. 2). One method must be used for all purchases in a period (MB § 81, stk. 4).

**Partial deduction.** For costs used for both taxable and exempt activity, the deductible share is the taxable turnover as a share of total turnover (ML § 38, stk. 1). Exclude disposals of used capital goods, incidental property transactions, passive capital investment, including the listed isolated intra-group loans and interest on own sales credit from the denominator as ML § 38, stk. 1 requires. During the year use one provisional percentage, rounded up to the next whole number: the final percentage for the previous financial year if it has been worked out by the time the first return of the year is filed, otherwise the final percentage for the year before that. A start-up uses the period’s turnover provisionally. Settle the final percentage for goods/services delivered in the prior financial year in the period that includes the 6th month after that year ends (MB § 17 as amended by BEK nr. 518/2025). Costs used partly for private purposes are deducted on an estimate of the business share (ML § 38, stk. 2). Once a year the return asks whether the business has exempt activity (ML § 38 a).

**No deduction or limited deduction (ML §§ 41-42).** These limits apply even where the cost is wholly business:
- **Food, housing and staff benefits:** no deduction for meals for the owner and staff, housing for them, benefits in kind, or holiday homes and childcare for staff (ML § 42, stk. 1, nr. 1-4). Skattestyrelsen allows a deduction for food on unannounced overtime only if it was not planned, was announced immediately before normal hours ended and is not usual, and 100% for food and drinks at meetings in the business's own premises (meetings with business contacts, board meetings, internal meetings with professional content, internal courses) (skat.dk, food and hotel).
- **Entertainment, representation and gifts:** no deduction (ML § 42, stk. 1, nr. 5). Product samples and ordinary advertising items are not gifts in this sense (Den juridiske vejledning D.A.11.5.7.4). Gifts to staff are also gifts for this rule (same section).
- **Restaurant meals:** 25% of the VAT is deductible where the cost is strictly business (ML § 42, stk. 2). A genuinely mixed private/business restaurant event cannot be split to claim a business share; participation of spouses in an otherwise qualifying staff party does not itself remove the deduction (Den juridiske vejledning D.A.11.5.7.2). For spending disproportionate to the business purpose, the eligible amount is reduced to usual restaurant costs at the current price level (same guidance). A Christmas lunch or staff party held at a restaurant gets 25%; food at a staff party in the business's own or rented premises gets nothing (skat.dk, food and hotel).
- **Hotels:** for wholly taxable business use the room is fully deductible and restaurant items such as breakfast get 25%, provided the hotel invoice shows them separately. A social element in the stay is estimated and excluded (skat.dk, food and hotel). ML § 42 sets no percentage limit on hotel rooms; mixed taxable/exempt use still follows the partial-deduction rules.
- **Passenger cars (up to 9 persons, white plates) and motorbikes:** no deduction on purchase or running costs such as petrol or repairs (ML § 42, stk. 1, nr. 6; skat.dk, vehicles), and none under the long-lease exception on rent or lease of 6 months or less (skat.dk, vehicles). So a white-plate car bought with DKK 60,000 of VAT on the invoice gives no input VAT. A lease of more than 6 months gives a limited deduction set out in the table above, shown on the lessor’s invoice (ML § 42, stk. 4 and 5; MB § 58, stk. 5). It cannot exceed actual rent VAT. The first 3 years run from first registration (manufacture if earlier use/registration date is unknown); if registration tax is unknown the statutory substitute is 55% of the lessor’s VAT-inclusive acquisition price. Obtain the lessor’s calculation before claiming. The Øresund bridge toll is deductible to the extent allowed for business taxable use (ML § 42, stk. 7). A business that sells cars, lets cars or runs a driving school deducts normally (ML § 42, stk. 6).
- **Vans and trucks up to 3 tonnes (yellow or "parrot" plates):** VAT on purchase is deductible only if the vehicle is used solely for taxable activity (ML § 41, stk. 1). Running costs are fully deductible even with part private use, and one third of the VAT on rent of a hired one (ML § 41, stk. 2 and 3), but only if the business's supplies exceed the DKK 50,000 threshold (ML § 41, stk. 5). Insurance and fines carry no deductible VAT (skat.dk, vehicles).
- **Telephones at employees’ homes:** 50% of VAT where bills are addressed to and paid by the business; never more than the VAT it actually bears (ML § 40, stk. 2). Other mixed-use phone, internet and home-office costs need the actual use and any special rules; do not default to 50%.

**Capital goods.** Depreciating machinery/equipment and capital-like software/rights costing strictly more than DKK 100,000 excluding VAT are capital goods; property has no such general threshold, while property repair/maintenance is covered above DKK 100,000 in a year (ML § 43). The adjustment periods are 5 years for the listed movable goods/rights and property repairs, 10 years for property, including the acquisition/use year. Annual adjustment is normally one fifth or one tenth of acquisition VAT for the changed deduction share; a change below 10 percentage points is excepted (ML § 44). Disposal, cessation, succession and the actual adjustment require separate facts; no actual adjustment output is usable here. Check this point with one of our partner accountants.

**Domestic reverse charge.** The Danish buyer, not the seller, pays the VAT when a taxable person in Denmark buys from a business established in Denmark (ML § 46, stk. 1):
- CO2 allowances and credits, and gas and electricity certificates (nr. 6);
- scrap metal (nr. 7);
- mobile phones (nr. 8), integrated circuits before they are built into end products (nr. 9), and game consoles, tablets and laptops (nr. 10). These three do not apply where the seller sells only or mainly to private consumers (ML § 46, stk. 2);
- gas and electricity to a reseller, unless delivered to the reseller's own meter point (nr. 11);
- telecom services bought by a taxable person whose principal activity with those purchases is resale and whose own consumption is insignificant (nr. 12);
- taxable investment gold under the option in ML § 51 a, and gold materials/semi-manufactured products of 325 thousandths or more, where the buyer is registered (nr. 4).

The seller invoices without VAT. The buyer enters the VAT as output VAT and, if the purchase is for taxable use, deducts the same amount.

**Invoices.** Subject to ML § 52 a, stk. 2’s exemption/OSS exceptions, every taxable person must issue an invoice for each supply, and a separate invoice for a prepayment (ML § 52 a, stk. 1). A full invoice shows the date, a sequential number, the seller's VAT number, both parties' names and addresses, what was supplied, the delivery date if different, the taxable amount and unit price, the rate and the VAT (MB § 58). For a supply of DKK 3,000 or less a simplified invoice is allowed subject to MB § 66’s exceptions: a business customer requesting a full invoice, the specified household services and private-customer services of DKK 5,000 or more, EU goods/new transport supplies, and EU distance sales outside the relevant OSS invoicing exception. Include the supplier identity/registration number, date, sequential number, quantity/nature, total consideration and VAT amount or data to calculate it. Retain the original invoice; issue a credit note for a return or later price reduction (ML § 52 a, stk. 5), and reduce input VAT for supplier credits (MB § 82). A compulsory composition that reduces/cancels liabilities requires an input-deduction adjustment (ML § 37, stk. 10, added by lov nr. 1783/2025); Hold its actual calculation pending the debt records. Check this point with one of our partner accountants. A business that is not registered must not show VAT on an invoice; VAT shown in error must be paid over unless corrected with the customer (ML § 52 a, stk. 6 and 7; ML § 46, stk. 6, which was stk. 7 before lov nr. 332/2024 renumbered § 46).

**Digital bookkeeping from 2026.** Under the Bookkeeping Act (Bogføringsloven, lov nr. 700 of 24 May 2022), a business that must file an annual report under the statutory annual-report obligation or a personally owned business with net turnover above DKK 300,000 in 2 consecutive income years must record its transactions and keep its vouchers in a digital bookkeeping system (§ 16, stk. 1). The system must be registered with the Danish Business Authority or meet the § 15 requirements, which include the ability to send and receive e-invoices automatically (§ 15, stk. 1, nr. 3; § 16, stk. 2). For companies this applied from financial years starting on or after 1 July 2024 (registered standard system) or 1 January 2025 (other systems) (BEK nr. 1342/2023, § 1). For personally owned businesses over the DKK 300,000 limit it applies from the first financial year starting on or after 1 January 2026 (BEK nr. 297/2025, § 1). This is a duty to use a compliant digital system; its e-invoice capability does not establish a universal duty to issue every invoice electronically. The special group-system exception in BEK nr. 1342/2023, § 1, stk. 3 was brought into the 2026 commencement by BEK nr. 297/2025. An actual special group-system or outsourced-bookkeeping compliance opinion is outside this filing method. Check this point with one of our partner accountants.

## Deadlines and filing

**Registering.** Register through virk.dk at least 8 days before taxable activity starts (ML § 47, stk. 6). A new registration starts on quarterly returns, or monthly if expected taxable supplies exceed DKK 55 million. Changes are notified within 8 days, and so is closing down (ML § 47, stk. 6 and 7).

**Periods.** Half-yearly up to DKK 5 million, quarterly above DKK 5 million and up to DKK 50 million, monthly above DKK 50 million (ML § 57, stk. 2-4). The period changes from 1 January, based on taxable supplies in the 12 months from 1 July to 30 June before it; a period can only be lengthened if every return and payment in those 12 months was on time (ML § 57, stk. 6). A business may ask for a shorter period from 1 January or 1 July, at least 1 month ahead, and then stays on it for 2 years (ML § 57, stk. 7 and 8). Skattestyrelsen can impose a shorter period under the criteria and procedure in ML § 62, as amended by lov nr. 1473/2024, § 4; do not infer a changed period merely from one late payment. Use the actual notice. An unresolved imposed-period case is not usable here. Check this point with one of our partner accountants.

**Return and payment deadlines.** The return and the payment have the same deadline (skat.dk, VAT deadlines):
- Half-yearly and quarterly: the 1st day of the 3rd month after the period ends (ML § 57, stk. 3 and 4).
- Monthly: the 25th of the following month; June is due 1 month and 17 days after the period (ML § 57, stk. 2).

| Period (2026) | Due |
|---|---|
| 2nd half 2025 / Q4 2025 | 2 March 2026 |
| Q1 2026 | 1 June 2026 |
| 1st half 2026 / Q2 2026 | 1 September 2026 |
| Q3 2026 | 1 December 2026 |
| 2nd half 2026 / Q4 2026 | 1 March 2027 |

Monthly filers, 2026: December 2025 by 26 January; January by 25 February; February by 25 March; March by 27 April; April by 26 May; May by 25 June; June by 17 August; July by 25 August; August by 25 September; September by 26 October; October by 25 November; November by 28 December 2026; December 2026 by 25 January 2027. These dates apply ML § 57 and Opkrævningsloven § 2, stk. 3’s next-bank-day rule; the live authority table now displays mainly later periods. Danish bank holidays matter, including 25 May and 24–26 December in 2026. Confirm any imposed special period separately.

**Filing.** File in TastSelv Erhverv. A registered business files every period, including a nil return when there was no activity (skat.dk, registration). A nil return is not a classification of zero-rated sales. Amounts are in whole kroner (ML § 57, stk. 1). The return fields are: output VAT (salgsmoms), VAT on goods bought abroad (EU and non-EU, including import VAT), VAT on services bought abroad under reverse charge, input VAT (købsmoms), and the value boxes A goods, A services, B goods (EU sales list), B goods (not on the list), B services and C (MB § 79; skat.dk, foreign trade).
- **A goods:** value of goods acquired from other EU countries, plus the EU-origin installation/assembly and distance-sale goods described in MB § 79, stk. 2. **A services:** value of services bought from other EU countries under the general B2B rule. Non-EU purchases do not go in box A.
- **B goods (EU sales list):** zero-rated goods to VAT-registered buyers in other EU countries. **B goods (not on the list):** new means of transport to non-registered buyers, installation and assembly in other EU countries, distance sales. **B services:** services to EU businesses under the general B2B rule.
- **C:** other supplies without Danish VAT, such as exports outside the EU, and services to EU businesses that are taxed where the property, transport, restaurant service or short-term hire takes place (skat.dk, foreign trade).

Net VAT is output VAT plus VAT on foreign purchases, less deductible input VAT (ML § 56, stk. 1; MB § 78). The digital receipt states whether VAT is payable or refundable (skat.dk, pay VAT). A negative result is refunded no later than 3 weeks after a return filed on time is received (Opkrævningsloven § 12, stk. 2), subject to tax-account settlement, the payout limit and set-offs, and is paid to the business's NemKonto (§ 12, stk. 5; § 16 c, stk. 5); Skattestyrelsen gives this as normally 21 days after filing (skat.dk, pay VAT). Skattestyrelsen can suspend the deadline where the business prevents checks, or hold the refund while earlier returns/information are missing (§ 12, stk. 3 and 4). Automatic payout normally requires at least DKK 200 unless a smaller amount is requested, and a business may choose a higher retained-credit limit, up to DKK 200,000 (§ 16 c, stk. 5). A negative VAT result alone is not a guaranteed cash refund by a particular date. Skattestyrelsen recommends paying no earlier than 5 working days before the deadline, because an earlier payment may be set against other public debt (skat.dk, pay VAT).

**EU sales list (EU-salg uden moms).** A business that sells zero-rated goods to EU-registered buyers, or services to EU businesses under the general B2B rule, reports each buyer's VAT number and the total value by the 25th of the month after the period, whatever its VAT return period (MB §§ 99 and 100). The default listing period is the month. Goods listing can be quarterly on permission if the business is not on monthly VAT and EU goods sales do not exceed DKK 400,000 in the quarter and each of the 4 previous quarters; crossing the limit requires listing the elapsed months of that quarter. A separate quarterly permission exists for businesses listing only services (MB § 99, stk. 4-6). Services exempt in the destination country are excluded from the list (MB § 99, stk. 1). Apply for quarterly listing in TastSelv Erhverv; the 2026 quarterly dates are 25 January (Q4 2025), 25 April, 25 July and 25 October, and 25 January 2027 for Q4 2026 (skat.dk, VAT deadlines). There is no nil listing (skat.dk, foreign trade). The values in box B and on the list must agree (MB § 85, stk. 4 and 5). The zero rate for intra-EU goods is lost if the list is missing or wrong, unless the failure is properly explained (ML § 34, stk. 2).

**Corrections.** Correct the period the error belongs to in TastSelv Erhverv. A return can be corrected the same day before 4 pm through the filing screen, and after that through the correction route (skat.dk, correct a return). A business that wants its VAT changed must put forward the facts or legal grounds within 3 years of the return deadline (Skatteforvaltningsloven § 31, stk. 2); Skattestyrelsen has the same 3 years to give notice of a change (§ 31, stk. 1). After that, a change is possible only in the cases in § 32, stk. 1: earlier practice finally overturned, a change that follows directly from another VAT change, intent or gross negligence, special circumstances accepted by Skattestyrelsen, or a change in the private-law or public-law basis of the VAT. The request must be made within 6 months of learning of the ground (§ 32, stk. 2). Skattestyrelsen states that a forgotten deduction, a misunderstanding of the rules or a wrong entry is not enough, and that it rarely allows a change after 3 years. Apply in writing in TastSelv Erhverv (Contact, Write to us, then VAT, Change of VAT return, 3 years or older), stating the reason, the documentation, which VAT to change and the correct amount (skat.dk, correct a return). Enter corrections only in the period the error belongs to, never in an unrelated period, and keep the acknowledgement.

**Build the schedule before the return.** Determine output tax points and use one legally permitted input-period method under MB § 81; a bank date alone does not establish either. For each item record the invoice date, legal counterparty, VAT number, goods or services, origin and destination, VAT-exclusive base, VAT shown, rate or route, business purpose, customs evidence and document ID. Reconcile output VAT to sales, input VAT to invoices after the limits above, foreign-purchase VAT to the box A, import and service schedules, boxes B and C to cross-border evidence, and the net result to the VAT control account. Keep the return receipt, the reconciliation and the invoice and customs schedule together. If an input deduction fails, change the input total; never delete the matching acquisition or import VAT to make the return balance. Do not take the VAT base from a bank debit. Prepare the return in DKK; for a foreign-currency invoice keep the actual conversion basis. This Guide has not proved the rate/date rule: an output requiring a new currency conversion is not usable. Check this point with one of our partner accountants.

**Records.** VAT records must support each period's figures (ML § 55). Invoices must be kept (ML § 52 c); a digital bookkeeping system must keep records and vouchers for 5 years (Bogføringsloven § 15, stk. 1, nr. 1).

## Penalties and interest

- **Late return.** If no return arrives by the deadline, Skattestyrelsen sets the VAT provisionally (foreløbig fastsættelse) and charges DKK 1,400 for each period (Opkrævningsloven § 4, stk. 1 and 2, as amended by lov nr. 16/2025). The fee is due even if the return is filed afterwards (skat.dk, provisional assessments). After 4 consecutive provisional assessments for the same registration, Skattestyrelsen can cancel it only after the statutory notice and opportunity to submit the missing returns within 14 days (Opkrævningsloven § 4, stk. 3, communication amended by lov nr. 1694/2024).
- **Late payment.** Interest accrues for each day after the last on-time payment day up to and including the day of payment, at the base rate plus 0.85 percentage points a month (Opkrævningsloven § 7, stk. 1). The 2026 base rate is 0.1% (SKM2025.720.SKTST), so the rate is 0.95% a month. The monthly rate is spread evenly over the calendar year: daily interest = unpaid amount x 0.95% x 12 / 365 (366 in a leap year), rounded to 2 decimals (remarks to L 80 of 2024-25, which became lov nr. 1694/2024; Den juridiske vejledning, A.B.4.7.2). The interest is not deductible for income tax. VAT sits on the tax account (skattekonto), where a debit balance carries the same rate (Opkrævningsloven § 16 c, stk. 1); from 1 January 2026 interest is charged only on the part of the debit comprising principal and fees, not on interest or fines (lov nr. 1783/2025, § 2, nr. 5-6, commenced by BEK nr. 1793/2025). That act repealed the earlier uncommenced amendment in lov nr. 1694/2024, § 1, nr. 15. Account allocation, changes in principal and separately interest-bearing fees must be included in an actual settlement.
- **Reminders.** A reminder letter costs DKK 160 from 14 September 2026 (DKK 65 before) (Opkrævningsloven § 6; lov nr. 763/2026). A reminder about a missing EU sales list costs the same (ML § 54, stk. 3). A debit balance above DKK 5,000 on the tax account is payable at once and triggers a reminder; ceased businesses, the specified estates and businesses with debt already in collection also have the amended rule for balances above DKK 200 (Opkrævningsloven § 16 c, stk. 4; lov nr. 763/2026).
- **Under-declaration.** VAT paid too little is payable with the normal payment deadline, so interest runs from that date (Opkrævningsloven § 5, stk. 1).
- **Fines and prison.** Wrong or misleading information, failure to register, and breaches of the invoicing and record rules, done deliberately or with gross negligence, are punished by fines (ML § 81, stk. 1). With intent to evade VAT the penalty is a fine or up to 1 year and 6 months in prison, or more under the Criminal Code § 289 (ML § 81, stk. 3). Issuing false invoices is a separate offence (ML § 81, stk. 4). Companies can be fined (ML § 81, stk. 6). Skattestyrelsen can also issue an order with daily fines to enforce registration duties (ML § 47, stk. 8).
- **Buyer's joint liability.** A registered buyer who pays a Danish supplier in a way that does not identify payer and payee through a bank or payment institution can be jointly liable for VAT the supplier evades, unless the payment is DKK 8,000 or less including VAT. Connected split payments and recurring payments under one contract in the year are aggregated. Liability is for the supplier’s evaded VAT on the supply; where bank/payment-institution payment was not possible, the statutory escape by reporting the purchase within 14 days after payment, at latest 1 month after receipt of the invoice, also matters (ML § 46, stk. 11-13, renumbered by lov nr. 332/2024). An actual liability conclusion needs all these facts. Check this point with one of our partner accountants.

## Cross-border points

- **Goods sold to EU businesses.** Zero-rated when the goods leave Denmark for another EU country and the buyer is registered there and has given its VAT number (ML § 34, stk. 1, nr. 1). Obtain and verify the buyer's number, keep proof of the check, and keep transport evidence such as carrier documents (skat.dk, EU documentation). Invoice by the 15th of the month after delivery (ML § 52 b), and the supply is treated as made on that 15th unless invoiced earlier (ML § 24). Report in box B goods and on the EU sales list.
- **Services sold to EU businesses.** Under the general B2B rule the place of supply is the customer's country and the customer pays the VAT there. Invoice by the 15th of the following month (ML § 52 b, stk. 2), report in box B services and on the EU sales list. Property services, passenger transport, restaurant and catering services and short-term hire of transport located in another EU country go in box C, not B services (skat.dk, foreign trade).
- **Buying from the EU.** For ordinary taxable EU acquisitions and foreign general-rule B2B services with Danish place of supply, a registered business self-assesses Danish VAT: enter the VAT in "VAT on goods bought abroad" or "VAT on services bought abroad", deduct it as input VAT if the use is taxable, and report the value in box A goods or A services. If the EU seller charged its own VAT in error, still self-assess 25% Danish VAT, do not claim the foreign VAT as input VAT, and ask the seller to refund it. The DKK 80,000 acquisition exception requires eligible exempt/small-business/non-taxable legal-person status, purchases not above that amount in both current and previous years, and no excise goods; new means of transport have a separate taxable-acquisition rule (ML §§ 11 and 50). Foreign general-rule B2B services can trigger registration and reverse charge irrespective of these thresholds (ML § 50 b). Apply the special place rules to property/hotels, passenger transport, physical event admission, restaurants/catering and short-term hire; a foreign invoice alone does not prove there is no Danish VAT. ML § 16, stk. 2’s actual-use exception can also affect the specified rights, advertising, consultancy, non-competition, financial/insurance, labour, movable-hire and energy-network services used outside the EU. Actual special-place/use disputes are non-usable holds, with the invoice, location, receiving establishment and actual use preserved. Check this point with one of our partner accountants.

- **Buying from foreign suppliers in Denmark.** When a foreign business without a fixed establishment in Denmark installs or assembles goods here, or supplies general B2B services, the Danish business buyer pays the VAT (ML § 46, stk. 1, nr. 2 and 3). This applies even if the foreign supplier has a Danish VAT number (ML § 46 a, stk. 1).
- **Imports from outside the EU.** Import VAT is 25% of the customs value plus customs duty and other import charges (not the VAT itself), plus incidental costs to the first destination in Denmark and another known EU destination at import (ML § 32, stk. 1). Special art/collectors’ items/antiques and processed reimports have different bases under ML § 32; those outputs are not usable here. Check this point with one of our partner accountants. A registered importer enters import VAT in "VAT on goods bought abroad" and deducts it as input VAT to the extent of taxable use (ML § 37, stk. 2, nr. 3). Keep the customs import specification (MB § 80, stk. 2) and do not count costs already in the customs value twice. Non-EU goods do not go in box A; non-EU services bought under reverse charge go in "VAT on services bought abroad" but not in box A services (MB § 79, stk. 3).
- **Exports.** Goods sent outside the EU are zero-rated (ML § 34, stk. 1, nr. 5). Report the value in box C.
- **Sales to private customers in other EU countries.** A Danish supplier established only in Denmark, with the cross-border customer/destination conditions in ML § 21 e, whose distance sales of goods and electronic, telecom and broadcasting services to private customers in other EU countries do not exceed EUR 10,000 in the current calendar year and did not in the previous one charges Danish VAT (ML § 21 e, stk. 1, nr. 3); it may opt out for at least 2 years (§ 21 e, stk. 2). Above that, VAT is due in each customer's country, usually through the One Stop Shop, whose return and payment are due by the end of the month after the period (ML § 66 g). OSS returns are out of scope; refer.
- **EU SME scheme.** A Danish business can use another EU country's small business exemption if its EU-wide turnover did not exceed EUR 100,000 in the previous or current year. It notifies Skattestyrelsen in advance, receives a number with the suffix "EX", and reports its turnover per country for each calendar quarter within 1 month after the quarter ends. It must report within 15 working days if it passes EUR 100,000 (ML § 71 e, stk. 5; §§ 71 f-71 g; § 71 k, stk. 3). It must also satisfy the host country’s exemption conditions, including its national threshold. An EU business can use the Danish DKK 50,000 exemption through its home authority and EX identification, with the Danish preceding-year condition (ML § 71 e, stk. 4). A business using a small business exemption cannot zero-rate intra-EU goods (ML § 34 c), and there is no deduction for input VAT on supplies made exempt under another country's SME exemption (ML § 37, stk. 9).
- **Non-EU businesses** in countries without the specified mutual-assistance agreement, which must register in Denmark, do so through a Danish representative, who is jointly liable (ML § 47, stk. 2; § 46, stk. 7, stk. 8 before the 2024 renumbering). Income tax for non-residents is in dk-cross-border.

## Worked examples

### Example 1: Consultancy on quarterly returns, Q3 2026

An ApS consultancy registered in 2026 is assigned quarterly returns and does not expect supplies above DKK 55 million (ML § 47, stk. 6). In Q3 2026 (July to September) it invoices Danish clients DKK 200,000 excluding VAT. Domestic purchase invoices for its taxable work carry DKK 18,000 of VAT. It buys a software service from a German supplier for DKK 20,000 without VAT. It takes clients to a restaurant (invoice VAT DKK 1,000) and pays for a hotel night on a work trip where the invoice shows room VAT DKK 600 and breakfast VAT DKK 100 separately.

- Output VAT: 25% of DKK 200,000 = DKK 50,000 (ML § 33).
- Reverse charge on the German service: 25% of DKK 20,000 = DKK 5,000, entered in "VAT on services bought abroad", with DKK 20,000 in box A services. It is deductible because the use is taxable (ML § 37, stk. 2).
- Restaurant: 25% of DKK 1,000 = DKK 250 (ML § 42, stk. 2).
- Hotel: the room VAT DKK 600 in full, plus 25% of the DKK 100 breakfast VAT = DKK 625.
- Input VAT: DKK 18,000 + 250 + 625 + 5,000 = DKK 23,875.
- Net VAT: DKK 50,000 + 5,000 - 23,875 = DKK 31,125, filed and paid by 1 December 2026.

```oa-check
name: Denmark Q3 2026 quarterly return, consultancy with an EU service, restaurant and hotel
inputs:
  sales: 200000
  domestic_input_vat: 18000
  eu_service: 20000
  restaurant_vat: 1000
  hotel_room_vat: 600
  hotel_breakfast_vat: 100
steps:
  - output_vat: sales * 0.25
  - eu_service_vat: eu_service * 0.25
  - restaurant_ded: restaurant_vat * 0.25
  - hotel_ded: hotel_room_vat + hotel_breakfast_vat * 0.25
  - input_vat: domestic_input_vat + restaurant_ded + hotel_ded + eu_service_vat
  - net_vat: output_vat + eu_service_vat - input_vat
expected:
  output_vat: 50000
  eu_service_vat: 5000
  restaurant_ded: 250
  hotel_ded: 625
  input_vat: 23875
  net_vat: 31125
```

### Example 2: Physiotherapy clinic with taxable product sales, first half of 2026, filed late

A physiotherapy clinic run as a sole trader makes exempt treatments (ML § 13, stk. 1, nr. 1) and taxable sales of training equipment and fitness classes (assume adult non-qualifying recreational classes, not exempt education), so it is registered for its taxable part and files half-yearly. In its 2025 financial year (the calendar year) taxable turnover was DKK 583,000 and exempt turnover DKK 317,000. Its final 2025 deduction percentage was known when the first 2026 return was filed; neither turnover figure contains a denominator exclusion.

For the first half of 2026:
- Taxable sales DKK 300,000 excluding VAT, so output VAT DKK 75,000.
- VAT on equipment bought for resale (used only for taxable sales): DKK 20,000, fully deductible.
- VAT on shared costs used for both activities (cleaning, IT, a treatment couch under DKK 100,000): DKK 8,000. The provisional deduction percentage is 583,000 / 900,000 = 64.78%, rounded up to 65% (MB § 17, stk. 1), so DKK 5,200 is deductible.
- VAT on supplies used only for treatments: DKK 3,000, not deductible.
- A restaurant lunch with an equipment supplier about the product range, strictly business, invoice VAT DKK 400: 25% = DKK 100.
- Input VAT: DKK 20,000 + 5,200 + 100 = DKK 25,300. Net VAT payable: DKK 49,700.

The return and payment were due on 1 September 2026. The owner files nothing by then, so Skattestyrelsen makes a provisional assessment and charges DKK 1,400 (Opkrævningsloven § 4, stk. 2). The fee is a separate charge, not VAT. The owner then files the correct return and pays the DKK 49,700 on 1 October 2026. Interest accrues on the unpaid VAT for each day from 2 September to 1 October 2026, which is 30 days: DKK 49,700 x 0.95% x 12 / 365 x 30 = DKK 465.68 (Opkrævningsloven § 7, stk. 1, and § 16 c, stk. 1; 2026 has 365 days). This is a principal-only arithmetic illustration, not the tax-account payoff: interest on the fee and every other account movement are left out. DKK 51,565.68 below therefore means VAT plus the stated fee plus this principal-only interest illustration. The actual payment balance remains unresolved until the account statement is reconciled. Check this point with one of our partner accountants. The final 2026 percentage is settled with the return for the period that includes June 2027, the 6th month after the year end (MB § 17, stk. 2).

```oa-check
name: Denmark H1 2026 half-yearly return, mixed clinic with pro-rata rounding, a late-filing fee and 30 days' interest
inputs:
  taxable_prior: 583000
  exempt_prior: 317000
  sales: 300000
  resale_input_vat: 20000
  shared_input_vat: 8000
  restaurant_vat: 400
  late_fee: 1400
  monthly_rate_pct: 0.95
  days_late: 30
steps:
  - pro_rata_pct: ceil(taxable_prior / (taxable_prior + exempt_prior) * 100)
  - output_vat: sales * 0.25
  - shared_ded: shared_input_vat * pro_rata_pct / 100
  - restaurant_ded: restaurant_vat * 0.25
  - input_vat: resale_input_vat + shared_ded + restaurant_ded
  - net_vat: output_vat - input_vat
  - total_due_excl_interest: net_vat + late_fee
  - interest: round(net_vat * monthly_rate_pct / 100 * 12 / 365 * days_late, 2)
  - total_due: total_due_excl_interest + interest
expected:
  pro_rata_pct: 65
  output_vat: 75000
  shared_ded: 5200
  restaurant_ded: 100
  input_vat: 25300
  net_vat: 49700
  total_due_excl_interest: 51100
  interest: 465.68
  total_due: 51565.68
```

### Example 3: Ordinary return with an EU service and a non-EU import, plus a later correction

A wholly taxable registered business has a domestic sale of DKK 100,000 excluding VAT, a domestic purchase with DKK 10,000 of VAT on a valid invoice, an EU service of DKK 20,000, and a non-EU import whose customs statement shows DKK 2,500 of import VAT. There are no EU goods purchases, so box A goods is zero; box A services is DKK 20,000 (MB § 79). Later it finds it left out a DKK 10,000 domestic sale from that period, so it corrects that period for DKK 2,500 more output VAT.

- Output VAT: DKK 25,000. VAT on goods bought abroad: DKK 2,500. VAT on services bought abroad: DKK 5,000.
- Input VAT: DKK 10,000 + 5,000 + 2,500 = DKK 17,500.
- Net VAT: DKK 25,000 + 2,500 + 5,000 - 17,500 = DKK 15,000; after the correction, DKK 17,500.

```oa-check
name: Denmark ordinary return with EU service, non-EU import and an omitted sale corrected
inputs:
  sales: 100000
  domestic_input_vat: 10000
  eu_service: 20000
  import_vat: 2500
  omitted_sale: 10000
steps:
  - output_vat: sales * 0.25
  - eu_service_vat: eu_service * 0.25
  - input_vat: domestic_input_vat + eu_service_vat + import_vat
  - net_vat: output_vat + import_vat + eu_service_vat - input_vat
  - correction_vat: omitted_sale * 0.25
  - corrected_net_vat: net_vat + correction_vat
expected:
  output_vat: 25000
  eu_service_vat: 5000
  input_vat: 17500
  net_vat: 15000
  correction_vat: 2500
  corrected_net_vat: 17500
```

### Earlier cases retained with their original inputs

These cases keep their original years, amounts and descriptions. Amounts are DKK unless another currency is stated. Apply the documentation, taxable-use, timing and deduction conditions above. A **Hold** is a non-usable output, not a nil deduction or an assumption of compliance. For every Hold below: **Check this point with one of our partner accountants.**

The six April 2026 bank lines are retained verbatim; supplier names identify the original records, not proof of the supplier’s country, VAT status or service:

| Original input | Conditional answer / hold |
|---|---|
| `03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; DKK 109.52` | If the documented legal supplier is non-EU and this is a general-rule B2B service for wholly taxable Danish use, foreign-services VAT is 27.38 and the same VAT is deductible; no A services. The given 109.52 is an original DKK input, not a newly proved conversion of USD 16.00. Hold any new currency conversion. |
| `10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -6,350.00 ; DKK` | If the invoice verifies an EU general-rule B2B advertising service for taxable Danish use: foreign-services VAT and deductible input VAT are each 1,587.50; A services 6,350. This purchase is not an EU sales-list entry. |
| `15.04.2026 ; RESTAURANT MARCHAL ; DEBIT ; Client dinner ; -1,800.00 ; DKK` | If a valid standard-rated VAT-inclusive invoice and strictly business event are established: base 1,440, VAT 360, deductible 90. Hold the actual claim while purpose/attendees or invoice are missing; “client dinner” alone is insufficient. |
| `18.04.2026 ; DUSTIN A/S ; DEBIT ; Invoice DK2026-441 Dell XPS 15 ; -12,495.00 ; DKK` | If this is a valid ordinary 25% domestic invoice for wholly taxable use: base 9,996, input VAT 2,499. The amount is below, not above, the ML § 43 capital-goods threshold. Verify the invoice and domestic electronics reverse-charge exception before using this route. |
| `22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice DK-2026-018 IT consultancy March ; +26,250.00 ; DKK` | If the customer’s German business/receiving establishment and general-rule service are proved: no Danish VAT, B services and EU sales list 26,250. This is a foreign place of supply, not a domestic zero rate. Hold the period until the invoice/supply tax point is known: the description says March, while receipt was 22 April. |
| `28.04.2026 ; JYSK BILCENTER ; DEBIT ; Car lease payment April ; -4,500.00 ; DKK` | Hold the actual deduction: plate/class, weight, lease duration, taxable use and lessor’s statutory base are missing. If 4,500 is a documented VAT-inclusive 25% charge, its VAT is 900; a qualifying partly private hired van up to 3 tonnes could give 300 under § 41, whereas an eligible passenger-car long lease uses § 42’s capped base, not a universal one-third rule. |

| Historical case / unchanged inputs | Answer or explicit destination |
|---|---|
| Older domestic sale 100,000; supported purchase VAT 10,000; EU service 20,000; omitted sale 10,000 | Example 3 keeps all four inputs and gives output 25,000, service VAT 5,000 and correction 2,500. The older EU goods-sale case with buyer VAT number and transport evidence maps to B goods and EU sales list, subject to the Cross-border conditions. |
| Older restaurant VAT 400; hotel room VAT 300 and separate breakfast VAT 40; passenger-car purchase VAT 60,000 | Restaurant deduction 100; qualifying business hotel deduction 310; ordinary passenger-car purchase deduction zero. |
| EC1: food, children’s clothing, books, hairdressing | The ordinary rate is 25%; test any actual exemption rather than infer a foreign reduced rate. |
| EC2/EC13: goods/services to Greenland or Faroe Islands; Faroese seafood import | ML § 2 excludes both territories from the Danish VAT area. Goods leaving Denmark for them follow the documented non-EU export route; Faroese goods entering Denmark follow import rules. A service is not automatically an export merely because the customer is there: apply the service place-of-supply rule. No assertion about either territory’s own tax rates is made. |
| EC3 and Test 10: plumbing subcontractor, building-site installation, invoice 80,000 without VAT | There is no blanket domestic construction reverse charge. With an ordinary Danish-established taxable supplier this is a domestic 25% supply: VAT 20,000 must be invoiced; correct the unsupported reverse-charge invoice. A foreign supplier or special place-of-supply dispute is a Hold, tested under ML §§ 18 and 46. |
| EC4: passenger car 400,000 + VAT 100,000; Test 4: passenger car 300,000 + VAT 75,000 | Ordinary business purchase deduction zero; gross costs 500,000 and 375,000 respectively. Employee income-tax benefits and special dealer/lessor/driving-school cases remain outside this return. |
| EC5: yellow-plate van, max 4 tons, 200,000 + VAT 50,000, 80% business/20% private | Hold: “max 4 tons” does not establish whether the up-to-3-ton rule applies. Do not claim full 50,000 and invent a fixed deemed-output charge. Establish weight/use and the applicable rule. |
| Test 11: yellow-plate van 250,000 + VAT 62,500, 70% business/30% private | If up to 3 tonnes, mixed private use prevents purchase-VAT deduction under ML § 41, stk. 1; no automatic full 62,500 recovery. Hold if weight or any special regime is unknown. |
| EC6: business dinner 3,000 + VAT 750; Test 5: 2,000 + VAT 500 | Strictly business restaurant deductions 187.50 and 125; non-deductible VAT 562.50 and 375 respectively. |
| EC7: business hotel room 1,500 + VAT 375; Test 6: 1,200 + VAT 300 | Qualifying room VAT is deductible in full: 375 and 300, not blocked. Separate restaurant items and private/social use. |
| EC8: exempt financial company; historic payroll-tax methods 1–4 | Actual exemption/registration follows Who this applies to. Lønsumsafgift is a separate filing: Hold its liability, method and rates. Historical 3.54%, 15.3%, 6.37% and “90% of profit” are not usable tax outputs here. |
| EC9: US SaaS USD 500/month; Test 2: US SaaS 2,000 net | For a proved general-rule B2B service used in Denmark, self-assess 25%; input deduction depends on taxable use. Test 2 gives VAT 500 and, if wholly taxable, deduction 500; no A services. EC9’s DKK result is a Hold until conversion is established. |
| EC10: input VAT 80,000/output VAT 30,000; Test 9: output 40,000/input 65,000 | Negative VAT results 50,000 and 25,000 respectively. Apply the refund/account-credit conditions above; no unconditional promise of cash within 3 weeks of the filing deadline. |
| EC11: new apartment-building sale, historical “5 years”; EC14: 3 commercial and 2 residential units | Hold actual property taxation, the historical five-year test, voluntary unit registration and allocation. New-building/building-land exceptions exist, but these outcomes need the property rules and transaction facts. No property tax result is usable here. |
| EC12: management consultancy to Swedish VAT-registered business; Test 8: Swedish consultancy 50,000 | On proved general-rule B2B facts, B services and EU sales list; Test 8 value 50,000, no Danish output VAT. Replace the old C-2 label with the actual field name. |
| EC15: EU consumer digital sales exceeding EUR 10,000 | The threshold and single-establishment conditions below select the place-of-supply route. Hold the actual destination registration/OSS filing; use a separate return when applicable. |
| Test 1: office supplies 10,000 net + VAT 2,500 | Valid ordinary domestic invoice and wholly taxable use: input VAT 2,500. |
| Test 3: German raw materials EUR 10,000, original approximate DKK 75,000, DE VAT number | If 75,000 is the established DKK base, acquisition VAT 18,750 and taxable-use input VAT 18,750; A goods 75,000. The approximate conversion is not a rate rule; Hold any actual conversion still needed. |
| Test 7: documented goods export to US, 200,000; Test 12: machinery sale to Greenland, 150,000 | With the export conditions proved: C values 200,000 and 150,000 respectively, no output VAT. |
| Test 13: Italian hotel EUR 200 including Italian VAT EUR 20 (original 10% input) | Accommodation is located with the property; do not self-assess Danish service VAT or deduct Italian VAT in the Danish return. Hold Italian rate validation and any foreign-VAT refund entitlement; do not declare the foreign VAT permanently irrecoverable. |
| Test 14: 60% taxable/40% exempt financial supplies; shared net expense 10,000 + VAT 2,500 | If 60% is the valid provisional/final share under the denominator and timing rules, input deduction 1,500; non-deductible VAT 1,000. Do not infer the percentage merely from an industry label. |

### Classification matrix and unresolved historical routes

Use named return fields, not the old invented numbered rubrik 1–9 or A-moms/B-moms/C-1/C-2 mappings. Classify domestic sales/purchases, EU acquisitions, foreign services, imports, EU goods/services sales and exports using the filing and Cross-border sections above. Credit notes reduce the original VAT/input accounts; an acquisition/import output liability survives a failed input deduction.

A bank statement, currency, foreign-looking name or supplier-pattern list never establishes VAT jurisdiction or entitlement. This includes the former bank/government/utilities/insurance/post/logistics/transport/food/SaaS/payment-processor/professional/payroll/rent/internal-transfer lists. Obtain the actual contract/invoice and establish whether the payment is consideration for a supply. Salary, loan principal, dividends, share capital, tax, fines, genuine non-supply insurance settlements and internal transfers are not classified as taxable purchases merely because cash moved. A bank or processor may supply both taxable and exempt services; a government payee is not an exemption rule.

Unclear owner/individual receipts, outgoing individual payments, cash withdrawals, fuel/vehicle costs, mixed-use home-office/internet costs, rent, large purchases, platform/marketplace sales, foreign accommodation, missing transport evidence and foreign-currency conversion are **non-usable holds** until their missing facts and operative rules are established. The historical supplier-default confidence tiers, spreadsheet formulas, colour rules and bank-specific parsing formats do not establish tax law or an official return schema. Keep transaction identifiers, signed bank amounts and separate sales/purchase/VAT/foreign-value schedules, reconcile the control account and preserve the filing receipt. No new spreadsheet or automatic bank classifier is supplied. **Check this point with one of our partner accountants.**

Historic specialised maritime/aircraft/tourist exemptions (including the old “5 tonnes” vessel condition), art/margin schemes, VAT grouping, property, foreign VAT recovery and lønsumsafgift retain their scope as **non-usable holds**, not blanket exemptions. The old advertising-gift “DKK 100 per item/recipient/year” test is also not established by this Guide. **Check this point with one of our partner accountants.**

## Ask the client first

1. Is the business established in Denmark, and what are its CVR or SE number, registration date and assigned VAT period? Send the sales and purchase ledgers and invoices for the period; a bank payee alone is not enough to classify a transaction. (Decides registration, the threshold and the deadline.)
2. What was taxable turnover in the last calendar year and so far this year, and does any of it come from exempt activity (healthcare, education, letting, finance)? (Decides the DKK 50,000 test, the period, and partial deduction.)
3. Does the business buy from or sell to other EU countries or outside the EU, and does it hold the customers' VAT numbers and transport evidence? Send the customs records for imports. (Decides boxes A, B and C, the EU sales list and the zero rate.)
4. Which costs are meals, hotels, gifts, staff events or vehicles, and for vehicles: plate colour, weight, bought or leased, and how long? Send the invoice, the business purpose and who attended or received it. (These carry the ML §§ 41-42 limits.)
5. Has any return been filed late, assessed provisionally or corrected, and is there a debit on the tax account? (Fees, interest and the correction route.)
6. For a personally owned business: was net turnover above DKK 300,000 in each of the last 2 income years? (Digital bookkeeping duty from the 2026 financial year.)

## Sources

| Source | URL | Read on |
|---|---|---|
| ML, LBK nr. 209/2024: read §§ 2–4, 11–13, 16, 18, 21–24, 27, 32–34, 37–44, 46–47, 49–50, 52–57, 62, 66 and 81 for the operative subjects below, with amendments | https://www.retsinformation.dk/eli/lta/2024/209/pdf | 2026-11-28 |
| Amendment applicability: ML1473 § 4 (62), ML1489 § 12 (29 a), ML1703 § 16 (13); MB1075 §§ 43/46/55/133, MB1158 § 65, MB850 § 64; read the changed clauses, not unrelated Acts | https://www.retsinformation.dk/eli/lta/2024/1473/pdf ; https://www.retsinformation.dk/eli/lta/2024/1489/pdf ; https://www.retsinformation.dk/eli/lta/2024/1703/pdf ; https://www.retsinformation.dk/eli/lta/2024/1075/pdf ; https://www.retsinformation.dk/eli/lta/2024/1158/pdf ; https://www.retsinformation.dk/eli/lta/2025/850/pdf | 2026-11-28 |
| Lov nr. 332/2024, § 1: read the changes to events §§ 16/20 a/21, SME restrictions § 34 c/37(9), § 41 threshold and § 46 renumbering | https://www.retsinformation.dk/eli/lta/2024/332/pdf | 2026-11-28 |
| Lov nr. 1693/2024, § 1: read §§ 71 b–71 k (SME thresholds, turnover, EX, reporting/loss), § 34(1)(22) air transport and § 56 input timing | https://www.retsinformation.dk/eli/lta/2024/1693/pdf | 2026-11-28 |
| Lov nr. 1695/2024, §§ 1–2: read ML § 4 d and § 13(1)(7) licensing/transfer scope and 1 July 2025 application | https://www.retsinformation.dk/eli/lta/2024/1695/pdf | 2026-11-28 |
| Lov nr. 1783/2025: read § 1 education/ships/composition/SME, § 2(5–6) interest, § 5 repeal and § 6 commencement; BEK1793 §§ 1–3 start 1 January 2026 | https://www.retsinformation.dk/eli/lta/2025/1783/pdf ; https://www.retsinformation.dk/eli/lta/2025/1793/pdf | 2026-11-28 |
| Lov nr. 763/2026, §§ 1–3: read payment/account reminder and ML § 54 fees, amount and 14 September commencement | https://www.retsinformation.dk/eli/lta/2026/763/pdf | 2026-11-28 |
| MB, BEK nr. 1435/2023: read §§ 17, 58, 66, 78–86, 99–100; BEK nr. 518/2025 §§ 1–2 input timing/pro-rata changes and commencement | https://www.retsinformation.dk/eli/lta/2023/1435/pdf ; https://www.retsinformation.dk/eli/lta/2025/518/pdf | 2026-11-28 |
| Opkrævningsloven LBK nr. 1040/2024: read §§ 2, 4–7, 12, 16 c; nr. 1694/2024 § 1 daily/rate/account amendments and nr. 16/2025 § 1 fee | https://www.retsinformation.dk/eli/lta/2024/1040/pdf ; https://www.retsinformation.dk/eli/lta/2024/1694/pdf ; https://www.retsinformation.dk/eli/lta/2025/16/pdf | 2026-11-28 |
| 2026 base interest, SKM2025.720.SKTST | https://info.skat.dk/data.aspx?oid=2459995 | 2026-11-28 |
| L 80 (2024–25), remarks pp. 40–41: actual-day conversion of the monthly interest rate; interpretive explanation, not the enacted rate | https://www.ft.dk/ripdf/samling/20241/lovforslag/l80/20241_l80_som_fremsat.pdf | 2026-11-28 |
| Skatteforvaltningsloven LBK nr. 1228/2025, §§ 31–32 | https://www.retsinformation.dk/eli/lta/2025/1228/pdf | 2026-11-28 |
| Bogføringsloven nr. 700/2022, §§ 15–16 and 18; commencement orders nr. 1342/2023 and nr. 297/2025 | https://www.retsinformation.dk/eli/lta/2022/700/pdf ; https://www.retsinformation.dk/eli/lta/2023/1342/pdf ; https://www.retsinformation.dk/eli/lta/2025/297/pdf | 2026-11-28 |
| Skattestyrelsen: food/hotel; restaurants; gifts | https://skat.dk/erhverv/moms/fradrag-for-moms/udgifter-du-kan-faa-momsfradrag-for/momsfradrag-for-forplejning-og-hotel ; https://info.skat.dk/data.aspx?oid=2085707 ; https://info.skat.dk/data.aspx?oid=2085709 | 2026-11-28 |
| Skattestyrelsen: vehicle deductions (motorbike/car purchase and running rules) | https://skat.dk/en-us/businesses/vat/vat-deductions/vat-deductible-expenses/vat-deductions-for-vehicle-expenses | 2026-11-28 |
| Skattestyrelsen: VAT deadlines (page now mainly later periods), payment and corrections | https://skat.dk/erhverv/moms/frister-indberet-og-betal-moms ; https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-pay-vat ; https://skat.dk/en-us/businesses/vat/vat-what-to-do/how-to-change-your-vat-return-or-vat-payment | 2026-11-28 |
| Danmarks Nationalbank: Danish bank-closure calendar, 2026 | https://www.nationalbanken.dk/da/vores-arbejde/stabile-priser-pengepolitik-og-dansk-oekonomi/banklukkedage | 2026-11-28 |

**Not yet confirmed:** Actual foreign-currency conversions, special foreign/OSS/property/margin/group/vehicle cases and every Hold identified above are not usable filing outputs from this Guide. Preserve their original facts and obtain the missing rule/facts before filing. Check this point with one of our partner accountants.
