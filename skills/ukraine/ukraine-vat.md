---
name: ukraine-vat
description: "Ukrainian value added tax (podatok na dodanu vartist, PDV) for tax year 2026 under section V of the Tax Code of Ukraine as amended to September 2026. Covers who must register (UAH 1,000,000 in 12 months; single-tax groups 1 to 3 excluded), the 20%, 14%, 7% and 0% rates and what sits at each, exempt and out-of-scope supplies, place of supply, the tax point, input VAT and the 365-day claim window, the pro-rata rule, the electronic administration system (SEA) registration limit, tax invoice registration deadlines and the martial-law penalty scale, invoice blocking, refunds, the reverse charge on services from non-residents, non-resident e-services, the monthly return by the 20th and payment 10 days later, and the martial-law rules. Trigger on: Ukraine VAT, PDV return, register for VAT in Ukraine, tax invoice registration, SEA VAT limit. Out of scope: invoice mechanics in detail (ua-einvoice), single tax (ua-single-tax), corporate income tax (ua-corporate-income-tax), country summary (ua-tax-overview)."
version: 0.1
jurisdiction: UA
category: international
tax_year: 2026
last_updated: 2026-10-30
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ukraine VAT

Ukraine charges value added tax (podatok na dodanu vartist, PDV) under section V of the Tax Code of Ukraine (TCU), Law No. 2755-VI of 2 December 2010, articles 180 to 211, and under the VAT points of the transitional provisions (section XX, subsection 2). This skill uses the consolidated text that includes amendments up to Law No. 4967-IX of 3 September 2026. The State Tax Service (DPS) runs VAT through the taxpayer's electronic cabinet, the Unified Register of Tax Invoices (YERPN) and the electronic administration system (SEA PDV).

Ukraine has been under martial law since 24 February 2022 (Presidential Decree No. 64/2022, approved by Law No. 2102-IX). Several VAT rules below apply only while martial law lasts, and some for six months after it ends. Each one is marked "martial law".

## Who this applies to

**Mandatory registration.** A person must register as a VAT payer when the total of its taxable supplies of goods and services in the last 12 calendar months, including supplies made through a local or global computer network, exceeds UAH 1,000,000 excluding VAT. A payer of the single tax in groups 1 to 3 is excluded from this rule (TCU art. 181.1). The registration application is due no later than the 10th of the month after the month in which the threshold is first reached (art. 183.2). The DPS enters the registration within three working days if there is no ground to refuse (art. 183.9).

**Voluntary registration.** A person below the threshold may register by application (art. 182.1). The application is filed no later than 10 calendar days before the start of the tax period from which the person becomes a payer (art. 183.3).

**Other VAT payers** (art. 180.1) include an importer of goods in taxable volumes, the person keeping the books of a joint-activity agreement, a property manager keeping separate VAT records, and a non-resident supplying e-services to individuals (art. 14.1.139 (d)).

**Importers who are not registered** pay VAT at customs clearance without registering (art. 181.2).

**Reverse-charge recipients.** When a non-resident not registered for VAT supplies services whose place of supply is in Ukraine, the recipient is the person liable to charge and pay the VAT, except for e-services under art. 208-1 (art. 180.2). This applies even to a resident business that is not VAT-registered (art. 208.1, 208.4).

**Counterparty location.** Ukraine is not an EU member state. There are no intra-community supply or acquisition rules. Goods leaving Ukraine are exports and goods entering are imports (art. 185.1). Transactions with temporarily occupied territories and with the aggressor state carry their own rules and are out of scope here; refer them to an adviser.

**Not on the return at all:** wages, pensions, grants and subsidies paid in cash (art. 196.1.6); issue and sale of securities and corporate rights (art. 196.1.1); insurance (art. 196.1.3); currency transactions, lotteries and gambling stakes (art. 196.1.4); reorganisations of legal entities (art. 196.1.7).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Standard rate (TCU art. 193.1 (a), 194.1.1) | 20% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Zero rate: exports, international transport, listed supplies (art. 193.1 (b), 195) | 0% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Reduced rate: medicines and medical devices, cultural performances, museum and zoo visits, hotel accommodation (KVED 55.10), tickets to national and international sports events (art. 193.1 (v)) | 7% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Reduced rate: agricultural products under UKT ZED codes 1001, 1003, 1005, 1201, 1205, 1206 00 (art. 193.1 (h)) | 14% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Mandatory registration threshold, taxable supplies in last 12 months, excl. VAT (art. 181.1) | UAH 1,000,000 | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Registration application, mandatory (art. 183.2) | by the 10th of the next month | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Voluntary registration application (art. 183.3) | 10 calendar days before the period starts | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Tax period (art. 202.1) | calendar month | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Return due (art. 49.18.1, 203.1) | 20 calendar days after month end | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Payment due (art. 57.1, 203.2) | 10 calendar days after the return deadline | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Tax invoice registration, permanent rule (art. 201.10): invoices dated 1st to 15th / 16th to month end | last day of same month / 15th of next month | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Tax invoice registration, martial law (sec. XX, subsec. 2, point 89): invoices dated 1st to 15th / 16th to month end | 5th of next month / 18th of next month | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Window to claim input VAT from a registered invoice (art. 198.6) | 365 calendar days from invoice date | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Non-resident e-services return, quarterly (art. 208-1.4, 208-1.8) | within 40 calendar days after the quarter | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Late registration of a tax invoice, permanent scale (art. 120-1.1) | 10% / 20% / 30% / 40% / 50% of the VAT | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Late registration of a tax invoice, martial law scale (point 90) | 2% / 5% / 10% / 15% / 25% of the VAT | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Late or missing return (art. 120.1) | UAH 340; UAH 1,020 if repeated within a year | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Late payment of an agreed liability (art. 124.1) | 5% up to 30 days; 10% over 30 days | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Penalty interest (penia) (art. 129.4) | 120% of the NBU discount rate a year, per day | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Self-correction of an understatement (art. 50.1); waived with penia from 1 August 2023 until martial law ends (sec. XX, subsec. 10, point 69.38) | 3% of the shortfall (5% route in a later return); 0% during martial law | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Desk audit of a refund return (art. 76.3, 200.10) | 30 calendar days after the filing deadline | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Treasury pays an agreed refund (art. 200.13) | within 5 operating days | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Interest on late refunds (art. 200.23) | 120% of the NBU discount rate | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Record retention, primary documents of CIT payers and simplified-system legal entities (art. 44.3.2) | 1,825 days | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |
| Record retention, other documents (art. 44.3.3) | 1,095 days | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 |

**What sits at 7% (art. 193.1 (v)).** Supply and import of medicines registered in the State Register of Medicines and medical devices registered or conforming to the technical regulations; medicines and devices for authorised clinical trials; import of unregistered medicines under access programmes; theatre, opera, ballet, concert, circus and similar performances and film premieres; showing museum collections, exhibitions and guided tours in museums, zoos and reserves; distribution and showing of films adapted for people with sight or hearing impairments; temporary accommodation in hotels and similar establishments (KVED class 55.10); tickets to sports events of national and international level. Periodicals are not on the 7% list: domestic printed periodicals are exempt (art. 197.1.25).

**What sits at 14% (art. 193.1 (h)).** Supply in Ukraine and import of agricultural products under UKT ZED codes 1001 (wheat), 1003 (barley), 1005 (maize), 1201 (soya beans), 1205 (rape seed) and 1206 00 (sunflower seed). The product names are the headings of the Harmonised System that UKT ZED follows; the law lists only the codes. Everything else, including live cattle, pigs, raw milk, sugar beet, flax and processed food, is at 20%. Point 54-1 of subsection 2 still lists the wider 2021 codes (0102, 0103, 0401 raw milk, 1002, 1004, 1204 00, 1207, 1212 91) but only to fix which rate applies to prepayments, returns and price changes that straddle the date the 14% rate started. It does not put those goods at 14% today.

**What sits at 0% (art. 195).** Export of goods under the export, re-export (processed goods), duty-free and free-zone customs regimes, confirmed by the customs declaration (art. 195.1.1); fuel and supplies for ships and aircraft on international voyages and for spacecraft, and sales by duty-free shops (art. 195.1.2); international carriage of passengers, baggage and cargo under a single international transport document (art. 195.1.3 (a)); work on movable goods imported for that work and re-exported (art. 195.1.3 (b)); servicing aircraft on international flights (art. 195.1.3 (v)). A zero-rated supplier keeps its input VAT.

**Exempt supplies (art. 197).** Exemption means no output VAT and no input VAT on the related costs (art. 198.5 (b)). The main groups:

| Exempt supply | TCU article |
|---|---|
| Baby food and infant goods on the Cabinet list | 197.1.1 |
| Higher, secondary, vocational and pre-school education by licensed institutions | 197.1.2 |
| Rehabilitation aids and special-purpose goods for people with disabilities | 197.1.3 |
| Delivery of pensions, insurance payments and cash aid to the public | 197.1.4 |
| Medical services by licensed healthcare institutions | 197.1.5 |
| Childcare, rehabilitation stays, social services, school and hospital meals | 197.1.7 |
| Urban public transport (not taxis) at regulated fares | 197.1.8 |
| Religious services and religious items supplied by religious organisations | 197.1.9 |
| Funeral services and goods of state and municipal services | 197.1.10 |
| Supply of housing, except the first supply | 197.1.14 |
| Charitable aid, including free supplies to registered charities | 197.1.15 |
| Land plots and land shares, except land under buildings | 197.1.21 |
| Domestic printed periodicals and their distribution | 197.1.25 |
| Supplies to the National Bank of Ukraine (listed items) | 197.19 |
| Import of renewable-energy and energy-saving equipment and materials | 197.16 |

A tax invoice for an exempt supply carries the note "Bez PDV" with the article that grants the exemption (art. 201.3).

## The taxable base

**What is taxed (art. 185.1).** Supplies of goods and services whose place of supply is in Ukraine, including free transfers; imports and exports of goods; and international transport services.

**Tax point (art. 187.1).** The earlier of (a) the date money from the customer reaches the supplier's bank or payment account, and (b) the date goods are shipped (for exports, the date of the customs declaration) or, for services, the date of the document confirming the service. A prepayment therefore creates the liability when it arrives, and a tax invoice is issued on every full or partial supply and on every prepayment received (art. 201.7). For imports the tax point is the date the customs declaration is lodged (art. 187.8).

**Base (art. 188.1, 190.1).** The contract value including state taxes and duties, excluding VAT itself. For imports, the contract value but not less than the customs value, plus duty and excise. For services from non-residents, the base under art. 190.2.

**Place of supply of goods (art. 186.1).** Where the goods are when supplied; if transported, where transport starts; if installed by or for the seller, where they are installed.

**Place of supply of services (art. 186).**

| Service | Place of supply | TCU article |
|---|---|---|
| General rule | where the supplier is registered | 186.4 |
| Services on movable property: loading and warehousing, appraisal, transport-related services, repairs and processing | where actually performed | 186.2.1 |
| Services connected with real estate, including estate agents and construction | where the property is | 186.2.2 |
| Culture, art, education, science, sport, entertainment, fairs and conferences | where actually performed | 186.2.3 |
| IP rights and licences, advertising, consulting, engineering, legal, accounting, audit, software development and testing, data processing, IT advice, staff supply, leasing of movables (not vehicles), telecoms, broadcasting, freight forwarding, film and graphics production | where the recipient is registered as a business, or else lives | 186.3 |
| E-services | where the recipient is located (registration for a business; SIM country, fixed line or other evidence for an individual) | 186.3-1 |

**Input VAT (art. 198).** VAT charged on goods, services, fixed assets and imports goes into the tax credit of the period (art. 198.1, 198.3). The credit is allowed even if the asset is not yet used in taxable supplies in that period (art. 198.3). The credit must be supported by a tax invoice registered in YERPN or by the customs declaration; without them there is no credit (art. 198.6). Registration by the seller is the buyer's only evidence; the buyer needs no other confirmation (art. 201.10). If the buyer does not claim a registered invoice in its period, it may claim it within 365 calendar days of the invoice date (art. 198.6). An invoice the seller registered late is claimed in the period of registration, but no later than 365 days after the invoice date (art. 198.6). The 365-day count stops while the invoice is blocked under art. 201.16 (art. 198.6).

**When input VAT is clawed back (art. 198.5).** If goods, services or fixed assets bought with VAT are used in supplies outside the scope of VAT or supplied outside Ukraine, in exempt supplies, for non-business use or transfers within the balance sheet, or in activity that is not the payer's business, the payer must charge output VAT on them. It does so on a consolidated tax invoice dated no later than the last day of the period and registered in YERPN.

**No special block for cars or entertainment.** Article 198 sets the business-use test above and contains no separate restriction for passenger cars, fuel or entertainment. Input VAT on a car or a client event follows the same test: if it is used in taxable business supplies the credit stands; if it is used privately or outside the business, art. 198.5 claws it back.

**Partly taxable businesses (art. 199).** If purchases are used partly in taxable and partly in non-taxable supplies, the payer takes the full credit and then charges output VAT on a consolidated invoice for the non-taxable share (art. 199.1). The taxable share is taxable supplies of the previous calendar year divided by all supplies (taxable and non-taxable) of that year, both excluding VAT, and it applies for the whole current year (art. 199.2). A new payer, or one that starts non-taxable supplies this year, uses actual figures (art. 199.3). At year end the share is recalculated on the year's actual supplies (art. 199.4) and the adjustment goes in the return for the last period of the year (art. 199.5). There is no de minimis threshold in art. 199.

**Adjustments (art. 192.1).** A later price change, a return of goods or a refunded prepayment adjusts both the seller's liability and the buyer's credit through an adjustment calculation (rozrakhunok koryhuvannia), drawn up like a tax invoice and registered in YERPN. A downward adjustment to an invoice issued to a VAT-registered buyer is registered by the buyer, within 15 calendar days of receiving it (art. 201.10), or 18 days under martial law (point 89).

**Payable or refundable (art. 200.1 to 200.4).** VAT payable is output VAT less input VAT for the period. If positive, it is paid by the deadline (art. 200.2). If negative, the payer may (a) offset it against earlier VAT debt, (b) claim a cash refund of VAT actually paid to suppliers or the budget, or (c) carry it to the next period's credit (art. 200.4). Options (a) and (b) are capped at the SEA registration limit at the time the return is received (art. 200.4). A payer under sanctions under the Law "On Sanctions" gets no refund while the sanctions last (art. 200.4-1).

**Refund process (art. 200.7 to 200.13).** The payer files the return with a refund application and a refund calculation (art. 200.7, 200.8). The DPS runs a desk audit within 30 calendar days after the filing deadline, or after actual filing if late (art. 76.3, 200.10), and may run a documentary audit within 40 calendar days after the filing deadline (art. 200.11). The refund becomes "agreed" in the Register of Refund Applications on the day after the audit term ends with no findings, or automatically where the DPS records nothing by the deadline (art. 200.12). Any tax debt is netted off first (art. 200.12). The Treasury pays an agreed refund within five operating days (art. 200.13). Refunds not paid in time become budget debt that carries interest at 120% of the NBU discount rate (art. 200.23).

**Electronic administration system, SEA PDV (art. 200-1).** Each payer has an SEA account opened automatically (art. 200-1.2). A payer may register tax invoices and adjustments only up to its registration limit (art. 200-1.3, 201.10):

Limit = invoices received and registered (including reverse-charge invoices under art. 208.2) + VAT paid on imports + top-ups from the payer's bank account + "overdraft" - invoices issued and registered - refunds claimed - the excess of declared liabilities over registered invoices.

The "overdraft" is the monthly average of VAT the payer declared as payable and paid (or had deferred) over the last 12 months, recalculated each quarter (art. 200-1.3). If the limit is too low to register an invoice, the payer must transfer the shortfall from its bank account to its SEA account (art. 201.10). The figures run from 1 July 2015 (art. 200-1.3).

**Tax invoice (podatkova nakladna) (art. 201).** An electronic document with a qualified electronic signature, drawn up on the tax point and registered in YERPN within the deadline (art. 201.1). Mandatory fields: sequential number; date; names of seller and buyer; tax numbers of both, and the branch number if a branch supplies; description and quantity; price excluding VAT; rate and VAT amount; total including VAT; UKT ZED code for goods or the State Classifier code for services (at least the first four digits, in full for excisable and imported goods); individual tax number; and, for exports, the customs declaration and contract date and number (art. 201.1). Invoices that are not given to the buyer, and invoices for exempt supplies, must still be registered (art. 201.10). A receipt confirming acceptance is sent within the operating day; if none is sent, the invoice counts as registered (art. 201.10). Errors in mandatory fields (other than the UKT ZED code) that do not prevent identifying the transaction are not grounds to reject the invoice (art. 201.10). If the seller fails to register or makes errors, the buyer may attach a complaint against the seller to its return, and the DPS must audit the seller within 90 calendar days (art. 201.10). Detailed invoice and register mechanics are in `ua-einvoice`.

**Invoice blocking (art. 201.16).** Registration of a tax invoice or adjustment can be suspended in the order and on the grounds set by the Cabinet of Ministers. The suspension receipt goes to both seller and buyer on the same day (art. 201.10). While registration is suspended, the late-registration penalty does not run (art. 120-1.1) and the buyer's 365-day window is interrupted (art. 198.6). Martial law: a separate list of payers with a high level of voluntary compliance is kept; one condition for entry is that no risk decision under art. 201.16 has been taken about the payer (sec. XX, subsec. 10, point 69.41.1 (d)).

**Agriculture.** The special VAT regime for agricultural producers (art. 209) lost force on 1 January 2017. Agricultural producers now use the general rules for output and input VAT, with the 14% rate only for the six codes listed above.

**Martial-law rules on the base.**

- Goods bought in taxable supplies and destroyed or lost through force majeure during martial law, and goods handed to state or municipal ownership or provided for the defence of Ukraine, are not treated as used outside taxable supplies. Art. 198.5 does not apply to them, so no input VAT is clawed back (sec. XX, subsec. 2, point 32-1).
- A free transfer of goods or services to the Armed Forces, National Guard, Security Service, Foreign Intelligence Service, State Border Guard, Ministry of Internal Affairs, State Emergency Service, State Guard, State Special Communications Service, territorial defence volunteer units, other military formations, the civil-protection authority, or state and municipal healthcare institutions, for defence needs, is not a supply of goods or services. This does not apply where the supply would be zero-rated (point 32-1).
- Imports of goods belonging to the state through the Ministry of Defence, the Armed Forces and other military formations are exempt while martial law lasts (point 94).
- Supply in Ukraine of ground unmanned systems in UKT ZED groups 84, 85, 87, 90 and 93 and of listed weapons and ammunition is exempt while martial law lasts (point 99-1).
- Imports of goods listed in point 9-36 of the Customs Code transitional provisions are exempt while martial law lasts, but no later than 1 January 2029 (point 87-1). Imports of goods on a Cabinet list financed through the Energy Community Secretariat are exempt on the same terms (point 88-1).
- Imports of goods listed in point 9-24 of the Customs Code transitional provisions are exempt while martial law lasts, but no later than 1 January 2027 (point 92).

**Changes for 2026.**

- The exemption for supply and import of vehicles with only electric motors (UKT ZED 8701 24 tractor units, 8703 80 10 10, 8703 80 90 10, 8704 60 00 00) ran "until 1 January 2026" (former point 64). Law No. 4698-IX of 3 December 2025 deleted point 64. From 1 January 2026 these vehicles are taxed at 20%.
- The exemption for new vehicles running only on compressed or liquefied methane or biogas also ran until 1 January 2026 (point 64-1). From 2026 they are at 20%.
- The import exemption under point 87-1 was amended by Law No. 4698-IX and now runs to the end of martial law but no later than 1 January 2029.
- No change to the rates or to the UAH 1,000,000 threshold has been enacted for 2026 or 2027 in the text read.

## Deadlines and filing

**Return.** The VAT return is filed for each calendar month within 20 calendar days after the month ends (art. 49.18.1, 203.1). A payer that registers mid-month has a first period running from registration to the end of the first full calendar month (art. 202.1 (a)). The form is set by the Ministry of Finance (art. 201.15 with art. 46). It is filed electronically through the electronic cabinet.

**Payment.** The liability declared is paid within 10 calendar days after the last day for filing the return (art. 57.1, 203.2). The return is due on the 20th of the month after the reporting month, so payment falls on the 30th of that month; for January returns, due 20 February, it falls on 2 March (1 March in a leap year).

**Tax invoices.** Registration deadlines in YERPN:

| Invoice or adjustment | Permanent rule (art. 201.10) | Martial law and six months after (point 89) |
|---|---|---|
| Dated 1st to 15th of the month | by the last day of the same month | by the 5th of the next month |
| Dated 16th to the end of the month | by the 15th of the next month | by the 18th of the next month |
| Consolidated invoices under art. 198.5 and 199.1 | within 20 calendar days after the month end | not changed by point 89 |
| Downward adjustment registered by the buyer | within 15 days of receipt | within 18 days of receipt |

**Corrections.** A payer that finds an error in an earlier return files a correcting calculation (utochniuiuchyi rozrakhunok), or may show the corrected figures in any later return (art. 50.1). An understatement is paid with a 3% fine before the correction is filed, or with a 5% fine if corrected in a later return (art. 50.1). Martial law: from 1 August 2023 until martial law ends, a payer that self-corrects an understatement under art. 50 pays no art. 50.1 fine and no penia, whatever period the error is in (sec. XX, subsec. 10, point 69.38; point 69.1 gives the same relief for periods that fall in martial law). VAT payers may not file corrections reducing liabilities or claiming refunds for periods before February 2022 until martial law ends (sec. XX, subsec. 10, point 69.1).

**Non-resident e-services.** A non-resident registered under art. 208-1 files a simplified quarterly return through the special portal within 40 calendar days after the quarter, even for a quarter with no supplies (art. 208-1.4, 208-1.8). Its tax point is the last day of the quarter in which it was paid (art. 208-1.5). It claims no input VAT and issues no tax invoices (art. 208-1.7).

**Records.** Primary documents, registers and other tax documents of companies paying corporate income tax, and of legal entities on the simplified system, are kept for at least 1,825 days; other documents for at least 1,095 days; documents for transfer pricing and controlled foreign companies (arts. 39, 39-2) for 2,555 days (art. 44.3).

## Penalties and interest

**Late or missing return (art. 120.1).** UAH 340 for each return not filed or filed late; UAH 1,020 for each one if the payer was already fined for the same breach within the year. There is no warning-only first offence in the text.

**Late tax invoice registration (art. 120-1.1).** A percentage of the VAT on the invoice, by days late. The permanent scale and the martial-law scale (point 90, which applies during martial law and for six months after the month in which it ends, to the point 89 deadlines):

| Days late | Permanent rule (art. 120-1.1) | Martial law (point 90) |
|---|---|---|
| up to 15 | 10% | 2% |
| 16 to 30 | 20% | 5% |
| 31 to 60 | 30% | 10% |
| 61 to 365 | 40% | 15% |
| 366 or more | 50% | 25% |

No late-registration fine applies to invoices for exempt or zero-rated supplies, consolidated invoices under art. 198.5 (a) to (h) and art. 199, or while registration is suspended under art. 201.16 (art. 120-1.1).

**No registration at all (art. 120-1.2).** If the invoice is still not registered 10 calendar days after the payer receives a tax notice-decision, the fine is 50% of the VAT on it. Registering within those 10 days avoids this fine and the art. 120-1.1 fine.

**Errors in invoice fields (art. 120-1.3).** UAH 170 when the DPS finds errors on a buyer's complaint, with an order to fix them. If not fixed within 10 days of the order, the fine rises from 10% (up to 15 days) through 20%, 30%, 40%, 50%, 60% and 70% to 100% of the VAT after 181 days.

**Late payment (art. 124).** A fine on the agreed liability paid late: 5% of the debt repaid if up to 30 days late, 10% if more than 30 days late (art. 124.1). Intentional non-payment: 25% (art. 124.2); repeated within 1,095 days or more than 90 days late: 50% (art. 124.3).

**Penalty interest, penia (art. 129).** 120% a year of the NBU discount rate in force on each day, charged for every calendar day late including the day of payment (art. 129.4). On a liability the payer declared itself, including a self-correction under art. 50, penia starts only after 90 calendar days past the payment deadline (art. 129.1.3), and while martial law lasts a self-correction carries no penia at all (point 69.38). On an underpayment found by audit it runs from the first working day after the original deadline (art. 129.1.2).

**Martial-law relief.**

- A payer that cannot meet a deadline (payment, return, invoice registration) during martial law is released from liability if it meets the obligation within six months after martial law ends (sec. XX, subsec. 10, point 69.1).
- A payer that missed deadlines because of its direct participation in hostilities is released if it complies within one month after those consequences end (point 69.3).
- VAT payers must register within those terms the invoices whose deadlines fell in the relief periods and bring their declared credit into line with YERPN data (point 69.1-1).

## Cross-border points

**Imports of goods.** VAT on imports is assessed and collected by customs on the customs declaration (art. 187.8, 190.1). The payer does not self-assess goods imports on the return. Import VAT on the customs declaration supports the input credit (art. 198.6) and raises the SEA registration limit (art. 200-1.3). A non-registered importer pays at customs without registering (art. 181.2).

**Services from non-residents (art. 208).** When a non-resident not registered for VAT supplies services whose place of supply is in Ukraine (for example consulting, software, advertising or licences under art. 186.3), the Ukrainian business recipient charges VAT at 20%, or at 7% for the cultural services in art. 193.1 (v), on the art. 190.2 base (art. 208.2). A VAT-registered recipient draws up a tax invoice for the VAT it charged, registers it in YERPN, includes the VAT in its output for the period (art. 208.3) and, if the service is used in taxable business, claims the same amount as input VAT (art. 198.1 (v), 208.2). The net effect is nil for a fully taxable business. A recipient that is not VAT-registered issues no invoice and pays on a separate calculation form (art. 208.4).

**Non-resident e-services to individuals (art. 208-1).** A non-resident without a permanent establishment that supplies e-services to individuals, including sole proprietors not registered for VAT, registers under art. 208-1.2, charges 20% and files quarterly as above. A Ukrainian VAT-registered business that buys e-services from a non-resident applies the reverse charge under art. 208. Where the contract does not show the customer is a business, the service is treated as supplied to an individual (art. 186.3-1).

**Services supplied abroad.** A service whose place of supply is outside Ukraine under art. 186.3 (for example software development for a US company) is outside Ukrainian VAT. Input VAT on costs used for it is charged back under art. 198.5 (a), which covers supplies whose place of supply is outside Ukraine.

**Exports of goods.** Zero-rated with customs proof (art. 195.1.1); the tax point is the date of the export customs declaration (art. 187.1 (b)). Prepayments for exports and imports do not change the VAT position (art. 187.11). The payer may claim a refund of any negative amount (art. 200.4).

**Worked notes on the old edge cases.**

- Cloud software bought from a US provider (B2B): reverse charge at 20% under art. 208, self-invoice registered in YERPN, same amount claimed as credit.
- Export of grain to Germany: 0% under art. 195.1.1 with the export declaration; input VAT kept.
- Medicines sold to a pharmacy, net UAH 500,000: 7% under art. 193.1 (v), VAT UAH 35,000.
- Sedan bought for management, net UAH 1,000,000, VAT UAH 200,000: credit allowed if used in taxable business; clawed back under art. 198.5 for private or non-business use.
- Sunflower seed sold to a crusher, net UAH 2,000,000: 14% under art. 193.1 (h) (code 1206 00), VAT UAH 280,000. Wheat (1001) is also 14%.
- Invoice blocked under art. 201.16: the buyer cannot claim until it is registered; the seller's late fine and the buyer's 365-day window are paused during the suspension.
- Warehouse goods destroyed by shelling during martial law: no input VAT claw-back (point 32-1).
- Electronics imported from China, customs value UAH 3,000,000, import VAT UAH 600,000: paid at customs, claimed as credit on the customs declaration, and added to the SEA limit.
- Free supply of food to the Armed Forces for defence needs: not a supply (point 32-1); no claw-back of the input VAT.
- Credit note for a price cut: adjustment calculation registered in YERPN, registered by the buyer where it reduces the price paid.
- Residential housing sold after its first supply: exempt (art. 197.1.14).
- SEA limit UAH 300,000 against an invoice with VAT UAH 500,000: transfer UAH 200,000 to the SEA account before registering (art. 201.10).

## Worked examples

**Example 1. Monthly return of a Kyiv LLC, March 2026.** A VAT-registered LLC makes these supplies in March 2026: UAH 1,000,000 of IT services to Ukrainian clients at 20%, UAH 500,000 of sunflower seed (code 1206 00) at 14% and UAH 300,000 of registered medicines at 7%. It buys goods and services for its business from Ukrainian suppliers for UAH 600,000 net at 20%, all on registered tax invoices. It also buys UAH 100,000 of consulting from a Polish firm not registered in Ukraine; the place of supply is Ukraine under art. 186.3, so it charges itself 20% under art. 208.2. Output VAT is UAH 200,000 + UAH 70,000 + UAH 21,000 + UAH 20,000 = UAH 311,000. Input VAT is UAH 120,000 on domestic purchases plus UAH 20,000 on the reverse charge, UAH 140,000. VAT payable is UAH 171,000. The return is due by 20 April 2026 (art. 203.1) and the payment by 30 April 2026 (art. 203.2).

```oa-check
name: Ukrainian LLC, March 2026 return with 20%, 14%, 7% and reverse charge
inputs:
  sales_20: 1000000
  sales_14: 500000
  sales_7: 300000
  purchases_20: 600000
  nonresident_services: 100000
steps:
  - output_20: sales_20 * 0.20
  - output_14: sales_14 * 0.14
  - output_7: sales_7 * 0.07
  - output_rc: nonresident_services * 0.20
  - output_total: output_20 + output_14 + output_7 + output_rc
  - input_domestic: purchases_20 * 0.20
  - input_rc: nonresident_services * 0.20
  - input_total: input_domestic + input_rc
  - payable: output_total - input_total
expected:
  output_total: 311000
  input_total: 140000
  payable: 171000
```

**Example 2. Late invoice under martial law, and a pro-rata charge.** A VAT payer issues a tax invoice dated 20 February 2026 with VAT of UAH 50,000. Under the martial-law deadline it had to be registered by 18 March 2026 (point 89). It is registered on 7 April 2026, which is 20 days late. The martial-law fine is 5% of the VAT, UAH 2,500 (point 90). Under the permanent art. 120-1.1 scale the same delay would cost 20%, UAH 10,000. The same payer also makes exempt supplies. In 2025 its taxable supplies were UAH 8,000,000 out of UAH 10,000,000 in total, both excluding VAT, so its taxable share for 2026 is 80% (art. 199.2). In March 2026 it claims UAH 30,000 of input VAT on shared overheads. It must charge output VAT on the 20% non-taxable share, UAH 6,000, on a consolidated invoice registered in YERPN (art. 199.1). The share is recalculated on actual 2026 figures in the December 2026 return (art. 199.4, 199.5).

```oa-check
name: Martial-law late-registration fine and art. 199 pro-rata charge
inputs:
  invoice_vat: 50000
  days_late: 20
  taxable_2025: 8000000
  total_2025: 10000000
  shared_input_vat: 30000
steps:
  - fine_martial: invoice_vat * 0.05
  - fine_permanent: invoice_vat * 0.20
  - taxable_share: taxable_2025 / total_2025
  - prorata_liability: shared_input_vat * (1 - taxable_share)
expected:
  fine_martial: 2500
  fine_permanent: 10000
  taxable_share: 0.8
  prorata_liability: 6000
```

## Ask the client first

1. Is the business VAT-registered, and from what date? If not, what were its taxable supplies in each of the last 12 months, and is it a single-tax payer in group 1, 2 or 3?
2. What does it sell? Check each line against the 7% list, the six 14% codes, the zero-rated list and the art. 197 exemptions.
3. Does it buy services or e-services from non-residents, import goods, or export goods or services? Each changes the return and the SEA limit.
4. What is its current SEA registration limit, and are any of its own or its suppliers' tax invoices blocked under art. 201.16?
5. Does it make exempt or out-of-scope supplies alongside taxable ones, and what were its 2025 taxable and total supplies?
6. Has it lost goods to hostilities, donated to the defence forces, or missed deadlines it could not meet because of the war? Keep the supporting documents.

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Ukraine, Law No. 2755-VI of 2 December 2010, consolidated with amendments to Law No. 4967-IX of 3 September 2026: arts. 14.1.139, 44.3, 49.18, 50.1, 57.1, 76.3, 120, 120-1, 124, 129, 180 to 183, 185 to 188, 190, 192 to 203, 208, 208-1, 209; section XX subsection 2 points 32-1, 54-1, 64-1, 87-1, 88-1, 89, 90, 92, 94, 99-1; subsection 10 points 69.1, 69.1-1, 69.3, 69.38, 69.41 | https://zakon.rada.gov.ua/laws/show/2755-17 | 2026-10-30 (official text via web.archive.org capture of 12 Oct 2026, https://web.archive.org/web/20261012050950/https://zakon.rada.gov.ua/laws/show/2755-17/print; zakon.rada.gov.ua timed out from our network, and again by curl and a browser tab at review on 30 Oct 2026) |
| Tax Code of Ukraine, consolidated text as of May 2025: former section XX subsection 2 point 64 (electric vehicles) | https://zakon.rada.gov.ua/laws/show/2755-17 | 2026-10-30 (official text via web.archive.org capture of 28 May 2025, https://web.archive.org/web/20250528171622/https://zakon.rada.gov.ua/laws/show/2755-17/print) |
| State Tax Service of Ukraine | https://tax.gov.ua | 2026-10-30 (refused automated access; not read) |

Not yet confirmed: the VAT return form, its line numbers and its annexes (the Ministry of Finance order was not read; the old skill's line numbers and annex names D1 to D7 are left out); the Cabinet of Ministers procedure for suspending invoice registration (Resolution No. 1165), including the risk criteria and the time the regional commission takes to decide; the content of the goods lists in Customs Code transitional points 9-24 and 9-36 (the old skill called them energy equipment and wind turbines); whether residential letting is exempt (the old skill cited art. 197.1.14, which covers sale of housing, not rent); whether a universal postal service exemption exists (not found in art. 197.1); whether input VAT on goods destroyed by hostilities can be refunded in cash or only offset (point 32-1 says nothing on this); the benefits that come with the high-compliance list in point 69.41; the current martial-law extension decree and its end date; a wartime simplified VAT registration (no provision found); the old automatic-refund criteria such as 24 months of registration (not in the current art. 200); the term for appealing a refused refund; DPS guidance on any of the above.

> Contributed by Michael Cutajar.

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
