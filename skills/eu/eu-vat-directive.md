---
name: eu-vat-directive
description: "Load this skill as a shared reference whenever working on VAT for any EU member state in tax year 2026. Sets out, article by article, the common rules of Council Directive 2006/112/EC (consolidated to 14 April 2025) and Implementing Regulation 282/2011 that apply across all 27 EU member states -- the member state list, the rate framework after Directive 2022/542 and the 2026 rate table, intra-community acquisitions, reverse charge mechanics, place of supply exceptions, the EUR 10,000 distance selling threshold, OSS, EC Sales Lists, local consumption, imports and IOSS, VAT number checks, blocked input VAT, invoicing, the SME scheme (EUR 85,000 national cap, EUR 100,000 Union cap) and the ViDA timetable. Always load the country-specific VAT skill alongside this one. Do NOT use this skill alone -- it must be combined with the relevant country skill (e.g. ie-vat-return, germany-vat-return) which overrides anything country-specific. Step-by-step companion with test cases: eu-vat-base."
jurisdiction: EU
tax_year: 2026
last_updated: 2026-10-31
version: 1.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# eu-vat-directive

## EU VAT Directive: Common Rules (Directive 2006/112/EC)

## Scope

- **Scope**: All 27 EU Member States
- **Primary Legislation**: Council Directive 2006/112/EC of 28 November 2006 (consolidated version of 14 April 2025, the latest consolidation; no later amendment applies before 2027)
- **Supporting Legislation**: Directive (EU) 2022/542 (reduced rates reform); Directive (EU) 2020/285 (SME scheme, from 1 January 2025); Implementing Regulation 282/2011 (consolidated 14 April 2025); ViDA package: Directive (EU) 2025/516, Regulation (EU) 2025/517, Implementing Regulation (EU) 2025/518; Directive (EU) 2025/1539; Directive 2008/9/EC (refunds)
- **Source**: EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414
- **Contributor**: Open Accounting Skills Registry
- **Version**: 1.2
- **Rates Current As Of**: 30 October 2026 (TEDB, with 2026 mid-year changes dated)
- **Status**: awaiting-validation
- **Note**: This skill contains ONLY rules common to all EU member states. Country-specific rules (form boxes, national rates, filing deadlines, small business thresholds) are in the country skill. The country skill overrides this one where there is any conflict.

## Ask the client first

- Which member state is the supplier established in, and which is the customer in?
- Is the customer a business with a valid VAT number or a consumer?
- Is the supply goods or services, and where do the goods start and end their journey?
- What was the turnover in the member state, and across the Union, in the current and last calendar year?

## The method, step by step

Load the country skill first; it overrides this skill where they conflict. Then work through the steps below in order.

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Derived directly from the Directive. Applies in all member states unless the country skill specifies otherwise.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Rule exists in the Directive but national implementation varies. Check the country skill.
- **[T3] Tier 3 -- Out of Scope.** Not covered by this skill. Refer to country skill or warranted practitioner.

## Section 1: EU Member State List [T1]

- **EU Member State List**: AT Austria | BE Belgium | BG Bulgaria | HR Croatia | CY Cyprus | CZ Czech Republic | DK Denmark | EE Estonia | FI Finland | FR France | DE Germany | GR Greece (EL in VAT numbers) | HU Hungary | IE Ireland | IT Italy | LV Latvia | LT Lithuania | LU Luxembourg | MT Malta | NL Netherlands | PL Poland | PT Portugal | RO Romania | SK Slovakia | SI Slovenia | ES Spain | SE Sweden  _(Directive 2006/112/EC, Articles 1 and 5)_
- **NOT EU (treat as non-EU / third country)**: UK (EU VAT law stopped applying to it at the end of the transition period on 31 December 2020, Withdrawal Agreement, Article 126; but the EU VAT rules on goods still apply in Northern Ireland under Article 8 of the Protocol on Ireland/Northern Ireland, so goods moving between Northern Ireland and a member state follow Section 3; for services Northern Ireland is part of the UK, a third country); Norway, Switzerland, Iceland (EEA or EFTA but not EU); USA, Canada, Australia, UAE, and all other non-EU countries
- **Parts of member states outside the EU VAT area**: Mount Athos, the Canary Islands, the French territories in Articles 349 and 355(1) TFEU, the Aland Islands, the Channel Islands, Campione d'Italia, the Italian waters of Lake Lugano, Heligoland, Busingen, Ceuta, Melilla and Livigno. Treat supplies to and from them like third-country trade.  _(Directive 2006/112/EC, Article 6)_

## Section 2: VAT Rate Framework [T1]

Legislation: Directive 2006/112/EC, Articles 93-105b and Annex III, as amended by Directive (EU) 2022/542

### Rate Structure Rules (apply in all member states)

**Rate Structure Rules**  _(Directive 2006/112/EC, Articles 94-98 and 105a, as amended by Directive (EU) 2022/542)_

| Rule | Rate or limit | Official source |
| --- | --- | --- |
| Standard rate minimum | Cannot be lower than 15% (Article 97); one standard rate for goods and services (Article 96) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 |
| Reduced rates | Maximum two reduced rates, neither below 5%, only for Annex III items, in at most 24 Annex III points (Article 98(1)) | same |
| Super-reduced rate | Below 5% -- one such rate, plus one zero rate, for at most seven Annex III points, chosen from points (1) to (6) and (10c) or items covered by Article 105a(1) (Article 98(2)) | same |
| Zero rate | Exemption with deduction of input VAT. Allowed under Article 98(2) as above, and under acquired rights for items a member state zero-rated on 1 January 2021 (Article 105a(1), (2)) | same |
| Parking rate | Minimum 12% -- reduced rates of at least 12% applied on 1 January 2021 to items outside Annex III may continue (Article 105a(3)) | same |
| Sunset | Reduced and zero rates on fossil fuels, peat and firewood end by 1 January 2030; on chemical pesticides and fertilisers by 1 January 2032 (Article 105a(4)) | same |
| Electronically supplied services | No reduced rate except Annex III points (6), (7), (8) and (13) (Article 98(3)) | same |
| Acquisitions and imports | Same rate as a domestic supply of like goods (Article 94) | same |

### 2026 Rate Table -- All EU Member States

**2026 Rate Table -- All EU Member States**  _(European Commission TEDB web service, situation on 30 October 2026; mainland main rates)_

| Country | Code | Standard | Reduced 1 | Reduced 2 | Super-Reduced | Parking | Official source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Austria | AT | 20% | 10% | 13% | 4.9% (foodstuffs, from 1 July 2026) | -- | https://ec.europa.eu/taxation_customs/tedb/ |
| Belgium | BE | 21% | 6% | 12% | -- | 12% | same |
| Bulgaria | BG | 20% | 9% | -- | -- | -- | same |
| Croatia | HR | 25% | 5% | 13% | -- | -- | same |
| Cyprus | CY | 19% | 5% | 9% | 3% | -- | same |
| Czech Republic | CZ | 21% | 12% | -- | -- | -- | same |
| Denmark | DK | 25% | -- | -- | -- | -- | same |
| Estonia | EE | 24% | 9% | 13% | -- | -- | same |
| Finland | FI | 25.5% | 10% | 13.5% | -- | -- | same |
| France | FR | 20% | 5.5% | 10% | 2.1% | -- | same |
| Germany | DE | 19% | 7% | -- | -- | -- | same |
| Greece | GR | 24% | 6% | 13% | 4% (narrow) | 13% | same |
| Hungary | HU | 27% | 5% | 18% | -- | -- | same |
| Ireland | IE | 23% | 9% | 13.5% | 4.8% (livestock) | -- | same |
| Italy | IT | 22% | 5% | 10% | 4% | -- | same |
| Latvia | LV | 21% | 5% | 12% | -- | -- | same |
| Lithuania | LT | 21% | 5% | 12% | -- | -- | same |
| Luxembourg | LU | 17% | 8% | -- | 3% | 14% | same |
| Malta | MT | 18% | 5% | 7% | -- | 12% | same |
| Netherlands | NL | 21% | 9% | -- | -- | -- | same |
| Poland | PL | 23% | 5% | 8% | -- | -- | same |
| Portugal | PT | 23% | 6% | 13% | -- | 13% | same |
| Romania | RO | 21% | 11% | -- | -- | -- | same |
| Slovakia | SK | 23% | 5% | 19% | -- | -- | same |
| Slovenia | SI | 22% | 5% | 9.5% | -- | -- | same |
| Spain | ES | 21% | 10% | -- | 4% | -- | same |
| Sweden | SE | 25% | 6% | 12% | -- | -- | same |

Rates as on 30 October 2026. Always verify current rates against the European Commission's TEDB (Taxes in Europe Database) and the country skill before filing.

- **2026 changes within the year (TEDB)**: Belgium hotel accommodation 6% to 12% from 1 March 2026; Sweden foodstuffs 12% to 6% from 1 April 2026; Austria 4.9% on listed foodstuffs from 1 July 2026; Ireland restaurant and catering services and hairdressing 13.5% to 9% from 1 July 2026.
- **Changes from 1 January 2026 (TEDB)**: Finland 14% rate becomes 13.5%; Lithuania 9% rate becomes 12%.
- **Corrections to the 2025 version of this table**: Estonia now has 9% and 13% reduced rates; Finland 10% and 13.5%; Latvia 5% and 12%; Luxembourg 17% standard (16% applied only until 31 December 2023); Romania 21% standard and 11% reduced (from 1 August 2025); Ireland 4.8% livestock rate (Revenue).
- **Zero rates**: every member state exempts intra-community supplies of goods (Article 138) and exports (Article 146) with the right to deduct. Domestic zero rates are national: check the country skill.
- **Regional rates (not in the table)**: Austria 19% (Jungholz and Mittelberg); Greece 17% on Leros, Lesvos, Kos, Samos and Chios; Portugal 16% (Azores) and 22% (Madeira); Corsica rates in France.

## Section 3: Intra-Community Acquisitions (ICA) [T1]

Legislation: Directive 2006/112/EC, Articles 2(1)(b), 20, 40-42, 67, 69, 94, 138; Implementing Regulation 282/2011, Article 45a

### Definition

- **Intra-Community Acquisition (ICA)**: An ICA occurs when physical goods are dispatched or transported from one EU member state to another and acquired by a taxable person or a non-taxable legal person (in practice, B2B between VAT-registered businesses).  _(Directive 2006/112/EC, Articles 2(1)(b), 20)_

### Rules

- **Place of ICA**: The place of ICA is where transport ends  _(Article 40)_. If the buyer uses a VAT number of a different member state, that member state also taxes the acquisition until the buyer proves it was taxed where transport ended  _(Article 41)_.
- **Acquiring business liability**: The acquiring business is liable for VAT on the acquisition (self-assessment, commonly called reverse charge)  _(Article 2(1)(b))_
- **Supplier invoicing**: The supplier invoices at 0% (exempt intra-community supply)  _(Article 138(1))_
- **Acquirer self-assessment**: The acquirer self-assesses output VAT at the rate for a domestic supply of the same goods in its member state (usually the standard rate) AND claims the same amount as input VAT  _(Articles 94(1), 168(c))_
- **Net cash effect**: Net cash effect = zero for a fully taxable business
- **When VAT is due**: On issue of the invoice, or on the 15th day of the month after the supply if no invoice has been issued by then  _(Articles 67, 69, 222)_
- **VAT number on invoice**: The supplier must quote the customer's VAT number on the invoice  _(Article 226(4))_
- **EC Sales List reporting**: The supplier must report the sale on an EC Sales List (ESL) / Recapitulative Statement. Without a correct statement, the exemption is lost unless the supplier justifies the error  _(Article 138(1a))_
- **Proof of transport**: Presumed when the supplier holds two non-contradictory transport documents from two independent parties, or one transport document plus one other item (insurance, bank payment for transport, notary or warehouse document). If the customer transports, the customer's written statement is also needed, by the 10th day of the following month  _(Implementing Regulation 282/2011, Article 45a)_

### Invoice Reference

- **Supplier invoice wording**: a reference to the exemption, e.g. VAT exempt intra-Community supply -- Article 138(1) Directive 2006/112/EC  _(Article 226(11))_
- **Invoice deadline**: no later than the 15th day of the month after the month of supply  _(Article 222)_

## Section 4: Reverse Charge -- Cross-Border Services (B2B) [T1]

Legislation: Directive 2006/112/EC, Articles 44, 194, 196, 199a

### The General B2B Rule (Article 44)

- **General B2B place of supply**: For services supplied to a taxable person acting as such, the place of supply is where the customer is established (or its fixed establishment that receives the service). Consequence: where the supplier is not established in that member state, the supplier charges 0% VAT and the customer pays the VAT (Article 196). The customer self-assesses output VAT at their local rate and claims the same as input VAT. Net effect = zero for a fully taxable business.  _(Articles 44, 196)_

### Mandatory for

- **Mandatory application scenarios**: All B2B cross-border services where Article 44 applies and the supplier is not established in the customer's member state; Services supplied by a non-EU supplier to an EU VAT-registered customer; also a non-taxable legal person identified for VAT  _(Directive 2006/112/EC, Article 196)_

### Invoice Reference

- **Supplier invoice wording**: the mention "Reverse charge" (Article 226(11a)); often with "Articles 44 and 196 Directive 2006/112/EC". Due by the 15th day of the following month (Article 222).  _(Articles 44, 196, 222, 226)_

### Exceptions to Article 44 (place where service is physically performed) [T2]

These services are taxed where performed, not where the customer is established:

**Exceptions to Article 44**  _(Directive 2006/112/EC, Articles 47-58)_

| Service Type | Place of Supply | Directive Article | Official source |
| --- | --- | --- | --- |
| Services related to immovable property (including hotel accommodation) | Where property is located | Article 47 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 |
| Passenger transport | Where transport takes place, by distance covered | Article 48 | same |
| Restaurant / catering services | Where physically carried out (on board in the EU: point of departure, Article 57) | Article 55 | same |
| Short-term hire of transport (up to 30 days; vessels 90 days) | Where vehicle put at disposal | Article 56 | same |
| Admission to cultural / sports / educational events and fairs (B2B) | Where event takes place; NOT for virtual attendance, which follows Article 44 (from 1 January 2025) | Article 53 | same |

- **B2C points to note**: B2C cultural, sports, educational and similar activities are taxed where they take place, but if streamed or made available virtually, where the customer lives (Article 54(1), from 1 January 2025); B2C telecoms, broadcasting and electronically supplied services are taxed where the customer lives (Article 58).
- **Reviewer flag**: [T2] For any of these exception categories, flag for reviewer to confirm correct place of supply treatment.

### Domestic reverse charges [T2]

- **Article 194**: a member state may make the customer liable on domestic supplies by non-established suppliers. Optional in 2026; mandatory from 1 July 2028 where the customer is already VAT-identified there (Directive (EU) 2025/516, Article 3).
- **Article 199a**: the optional domestic reverse charge for listed fraud-prone supplies (such as mobile phones, integrated circuits, gas and electricity to dealers, emission allowances) runs until 31 December 2026. Check the country skill.

## Section 5: Reverse Charge -- Non-EU Supplier to EU Business [T1]

Legislation: Directive 2006/112/EC, Articles 44, 196

- **Non-EU supplier to EU business rules**: When a non-EU supplier (US, UK, CH, AU etc.) provides services to an EU VAT-registered business: Supplier invoices at 0% (no EU VAT charged); EU customer self-assesses output VAT at local rate; EU customer claims same amount as input VAT (if fully taxable); Net effect = zero for fully taxable business; This applies to: software subscriptions, cloud hosting, consulting services, digital services, IP licences  _(Directive 2006/112/EC, Articles 44, 196)_

Common examples: AWS, Google Workspace, Microsoft 365, Notion, Slack, Stripe fees, LinkedIn ads -- all trigger reverse charge when purchased by an EU VAT-registered business. [T2] Check the contracting entity on the invoice: where the provider invoices from an entity in the customer's own member state, local VAT is charged instead.

## Section 6: Distance Selling -- B2C Cross-Border [T1]

Legislation: Directive 2006/112/EC, Articles 33, 58, 59c, 358-369zb

### The EUR 10,000 Threshold

- **EUR 10,000 distance selling threshold**: 10000 EUR per calendar year, total intra-community B2C distance sales of goods plus B2C telecoms, broadcasting and electronically supplied services to customers in ALL other EU countries combined, excluding VAT. Available only to a supplier established in one member state only. The threshold is passed if the total exceeds EUR 10,000 in the current year or did so in the previous year.  _(Directive 2006/112/EC, Article 59c(1))_
- **Above threshold rule**: If exceeded during the year, the customer's country rate applies from that point (destination principle). Must either register in each destination country OR use the OSS (One Stop Shop).  _(Articles 33(a), 58, 59c(2))_
- **Below threshold rule**: Below EUR 10,000: apply VAT at the supplier's own country rate. The supplier may opt for destination taxation; the option binds for at least two calendar years.  _(Article 59c(1), (3))_
- **Not covered by the threshold**: other B2C services (they follow Article 45 or the specific rules in Section 4) and distance sales of imported goods (Article 33(b), (c)).

### One Stop Shop (OSS)

- **OSS**: Allows a supplier to register in one EU member state and declare and pay VAT for all EU B2C distance sales of goods and B2C services in member states where it is not established, through that single registration (Union scheme, Articles 369a-369k). Non-EU businesses selling B2C services use the non-Union scheme (Articles 358-369). Eliminates the need to register separately in every customer's country.  _(Articles 358-369k)_
- **OSS returns**: quarterly, by the end of the month after the quarter, even if nothing was sold  _(Articles 364, 369f)_
- **IOSS**: imported goods in consignments up to EUR 150 (no excise goods); the import is exempt and VAT is charged at checkout; monthly returns by the end of the following month  _(Articles 143(1)(ca), 369l, 369s)_
- **No deduction in OSS**: input VAT is reclaimed under Directive 2008/9/EC or a local return, not in the OSS return  _(Article 369j)_
- **Reviewer flag**: [T2] If client makes significant B2C sales across EU: flag for reviewer to assess OSS registration requirement.

## Section 7: EC Sales List / Recapitulative Statement [T1]

- **EC Sales List filing requirement**: Every VAT-registered business that makes exempt intra-community supplies of goods, B2B services under Article 44 where the customer pays the VAT (Article 196), or call-off stock transfers must file an EC Sales List (called Recapitulative Statement in the Directive) reporting: Customer VAT numbers; Total value supplied to each customer; Period covered.  _(Directive 2006/112/EC, Articles 262-264)_
- **Timing**: monthly, within one month (Article 263(1)). A member state may allow quarterly statements, within one month of the quarter end, while intra-community supplies of goods stay at or below EUR 50,000 in the quarter and in each of the previous four quarters; once they pass EUR 50,000 in a quarter, monthly statements start from the end of that month (Article 263(1a)); for services, quarterly without a cap (Article 263(1c)). Filing frequency and format varies by country -- check country skill.
- **Triangulation**: an intermediary using the simplification for an ABC triangle reports it on its statement; without that, the Article 41 double charge applies  _(Articles 42, 141, 197, 265)_

## Section 8: Local Consumption Exception [T1]

- **Local consumption VAT treatment**: When a business pays for services consumed locally in another EU country (hotel, restaurant, taxi, conference admission), the VAT is charged locally by the supplier at their national rate. This is NOT reverse charge.  _(Directive 2006/112/EC, Articles 47 (hotels), 48 (passenger transport), 53 (admission to events), 55 (restaurants))_

Examples:
- Employee stays in a Paris hotel -- French VAT charged, not reverse charge
- Delegate attends a Berlin conference in person -- German VAT charged, not reverse charge (online attendance: reverse charge under Article 44)
- Business lunch in Amsterdam -- Dutch VAT charged, not reverse charge

- **Foreign VAT recovery**: The foreign VAT paid is an expense unless the business files a cross-border VAT refund claim under Directive 2008/9/EC. The claim goes through the business's own member state and must be filed by 30 September of the year after the refund period.  _(Directive 2008/9/EC, Article 15(1))_
- **Reviewer flag**: [T2] Cross-border VAT refund claims: possible for EU businesses but requires separate process; items blocked in the member state of refund stay blocked. Flag for reviewer if amounts are material.

## Section 9: Import of Physical Goods from Non-EU [T2]

- **Import VAT treatment**: When physical goods are imported from outside the EU: Import VAT is charged at the border by Customs, not via reverse charge on the VAT return; Import VAT is paid to Customs at the point of entry, at the rate for a domestic supply of like goods; The business recovers import VAT as input tax via the VAT return (using the Customs entry document); Reverse charge on the VAT return is NOT used for physical goods imports, unless the member state lets import VAT be entered in the VAT return instead of paid at the border (postponed accounting)  _(Directive 2006/112/EC, Articles 30, 60, 70-71, 94(2), 168(e), 211; national customs legislation)_
- **Low-value imports**: see IOSS in Section 6. From 1 July 2028, for distance sales of imported goods up to EUR 150 not declared under IOSS, the supplier or deemed supplier, not the customer, is liable for the import VAT  _(new Article 201(2), Directive (EU) 2025/1539)_
- **Reviewer flag**: [T2] Process and documentation varies by country. Flag for reviewer to confirm: (a) client has the customs entry document, (b) import VAT amount is correct, (c) recovery is allowable.

## Section 10: VAT Number Validation [T1]

- **VAT number validation requirement**: Before applying zero rate (ICA or B2B services): Verify the customer's VAT number is valid using the EU VIES system: https://ec.europa.eu/taxation_customs/vies/; A valid VAT number is a prerequisite for zero-rating goods (Article 138(1)(b)); For services, the supplier may treat the customer as a business when it has the customer's VAT number and has confirmed its validity and the linked name and address through VIES (Implementing Regulation 282/2011, Article 18(1)(a)); If VIES validation fails, do not zero-rate -- apply local VAT rate  _(Directive 2006/112/EC, Article 138; Implementing Regulation 282/2011, Article 18; Regulation 904/2010, Article 31)_

## Section 11: Blocked Categories -- Common EU Rules [T1/T2]

- **Blocked categories background**: Article 176 says VAT is never deductible on expenditure that is not strictly business expenditure, such as luxuries, amusements or entertainment, and lets member states keep the exclusions in their national law on 1 January 1979 (or on accession) (standstill clause). As a result, blocked categories vary significantly by country.  _(Directive 2006/112/EC, Articles 176-177)_
- **Common categories blocked in most EU member states [T1]**: Entertainment expenses (client meals, hospitality); Personal use items  _(Directive 2006/112/EC, Article 176)_
- **Categories blocked in some but not all member states [T2]**: Motor vehicles (blocked in some, partially allowed in others); Fuel (varies by country and vehicle type); Accommodation (varies)  _(Directive 2006/112/EC, Articles 176-177)_
- **Deduction needs an invoice**: Article 178(a)

Always check the country skill for the specific blocked categories for that jurisdiction.

## Section 12: Invoicing Requirements [T1]

- **Mandatory invoice elements**: Date of issue; Sequential invoice number; Supplier VAT number; Customer VAT number (for B2B intra-community supplies and reverse-charge supplies); Full name and address of supplier and customer; Description of goods or services; Date of supply (if different from invoice date); Taxable amount per VAT rate; VAT rate applied; VAT amount payable; For exempt intra-community supplies: reference to the exemption (Article 226(11)); For reverse charge: the mention "Reverse charge" (Article 226(11a)); "Self-billing" (Article 226(10a)); "Cash accounting" (Article 226(7a))  _(Directive 2006/112/EC, Article 226)_
- **Invoice deadline**: 15th day of the following month for exempt intra-community supplies and Article 196 services; national deadlines for other supplies  _(Article 222)_
- **E-invoicing in 2026**: [T2] Since 14 April 2025 a member state may require domestic e-invoices without EU authorisation and without the buyer's consent (Articles 218 and 232 as amended by Directive (EU) 2025/516, Article 1). National mandates and start dates vary: check country skill. EU-wide e-invoicing for intra-EU B2B starts 1 July 2030 (Section 14).

## Section 13: SME Scheme (from 1 January 2025) [T1/T2]

Legislation: Directive 2006/112/EC, Articles 281-294 as replaced by Directive (EU) 2020/285 (applies from 1 January 2025)

- **National threshold cap**: a member state's SME exemption threshold may not exceed EUR 85,000 of annual turnover in that member state; sector thresholds also may not exceed EUR 85,000  _(Article 284(1))_
- **Cross-border exemption**: a business established in another member state can use the host state's exemption if its Union annual turnover does not exceed EUR 100,000 and its turnover in the host state is within the host threshold  _(Article 284(2))_
- **Procedure**: prior notification to the member state of establishment and an identification number with the suffix "EX"; the exemption starts when the number is given, at the latest 35 working days after notification  _(Article 284(3), (5))_
- **Exceeding the threshold**: no exemption in the year after a year above the threshold. In the year itself, up to 10% over the threshold keeps the exemption; more than 10% ends it at once. Member states may set a 25% ceiling or no ceiling instead (never so that more than EUR 100,000 stays exempt), or end the exemption as soon as the threshold is passed. The cross-border exemption ends as soon as Union turnover passes EUR 100,000  _(Article 288a)_
- **Turnover**: sales of capital assets are excluded  _(Article 288(2))_
- [T2] Each member state's threshold and options: check the country skill.

## Section 14: ViDA (VAT in the Digital Age) timetable [T1]

Legislation: Directive (EU) 2025/516, Article 6; Regulation (EU) 2025/517, Article 6; Implementing Regulation (EU) 2025/518, Article 3; Directive (EU) 2025/1539, Article 2

| Applies from | What changes | Official source |
| --- | --- | --- |
| 14 April 2025 | Optional domestic e-invoicing mandates without derogation; no buyer consent needed (Directive 2025/516, Article 1(2), (3)) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 |
| 1 January 2027 | Cash accounting reworded (Article 66); Article 59c threshold counts only goods sent from the supplier's own member state; non-Union OSS usable by non-EU suppliers also VAT-registered in a member state; OSS covers B2C energy supplies by non-established suppliers until 30 June 2028 (Directive 2025/516, Article 2) | same |
| 1 July 2028 | Platforms deemed suppliers of short-term accommodation (up to 30 nights) and road passenger transport (member states may delay to 1 January 2030); mandatory reverse charge for non-established suppliers to VAT-identified customers (Article 194); wider OSS and a transfer-of-own-goods OSS; no new call-off stock movements after 30 June 2028 (Directive 2025/516, Article 3, call-off stock Article 2; Implementing Regulation 2025/518); import VAT on distance sales of imported goods not declared under IOSS payable by the supplier or deemed supplier, with a tax representative for a third-country supplier without a mutual-assistance agreement (Directive 2025/1539, new Article 201) | same |
| 1 July 2029 | Call-off stock register and call-off statement removed; Article 17a ends 30 June 2029 (Directive 2025/516, Articles 2 and 4) | same |
| 1 July 2030 | E-invoices in the European standard by default; intra-EU B2B invoices within 10 days; transaction-by-transaction digital reporting replaces the recapitulative statement (supplier at invoice issue, buyer within 5 days of receipt) (Directive 2025/516, Article 5) | same |
| 1 July 2032 | Last stage of administrative cooperation changes (Regulation 2025/517, Article 6) | same |
| 1 January 2035 | Member states with a domestic real-time reporting system before 1 January 2024 must align it (Directive 2025/516, Article 6(5)) | same |

## Worked cases

### Case 1: Intra-community acquisition

A German business buys goods of EUR 10,000 from a French supplier, with a valid VAT number and transport to Germany. The supplier invoices at 0% under Article 138. The buyer self-assesses at the German 19% rate and deducts the same amount if the goods serve taxed supplies.

```oa-check
name: Acquisition of EUR 10,000 at 19%, full deduction
inputs:
  net: 10000
steps:
  - output_vat: net * 0.19
  - input_vat: output_vat
  - net_payable: output_vat - input_vat
expected:
  output_vat: 1900.00
  net_payable: 0.00
```

### Case 2: Should the seller charge home or destination VAT

An Irish seller, established only in Ireland, makes EUR 12,000 of B2C distance sales of goods into Germany. That exceeds EUR 10,000 (Article 59c), so sales from the crossing onwards bear German 19%, not Irish 23%, declared through OSS or a German registration. On a further EUR 1,000 sale the VAT changes as below.

```oa-check
name: VAT on a further EUR 1,000 sale, home against destination rate
inputs:
  sale: 1000
  total: 12000
steps:
  - over_threshold: max(total - 10000, 0)
  - home_vat: sale * 0.23
  - destination_vat: sale * 0.19
  - difference: home_vat - destination_vat
expected:
  over_threshold: 2000.00
  destination_vat: 190.00
  difference: 40.00
```

## When to refuse or refer

- **Prohibition list**: NEVER zero-rate an intra-community supply without a valid customer VAT number verified on VIES and a correct EC Sales List entry; NEVER zero-rate goods without proof of transport; NEVER apply reverse charge to services consumed locally in another EU country (hotel, restaurant, taxi); NEVER apply reverse charge to physical goods imports -- import VAT is handled via Customs; NEVER use this skill alone -- always load the country skill alongside it; NEVER override the country skill with this base skill -- the country skill takes precedence on all national specifics; NEVER present EU-wide rules as applying without exception -- national derogations exist and are significant; NEVER apply ViDA rules that start after 2026 to 2026 transactions

## Gap Report

**Gap Report**

| Area | Status | Official source |
| --- | --- | --- |
| Core Directive rules | T1 -- sourced from the EUR-Lex consolidated text of 14 April 2025 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 |
| 2026 rate table | T1 -- read from the European Commission TEDB web service on 30 October 2026 (situations on 1 January and 30 October 2026); Ireland 4.8% from Revenue | same |
| OSS / IOSS detail | T2 -- return periods and scope covered; detailed country implementation in country skills | same |
| SME scheme | T1 for the EU caps; T2 for national thresholds | same |
| ViDA timetable | T1 -- from the ViDA acts' application articles | same |
| Intrastat thresholds | T3 -- not covered; varies by country; add to country skills | same |
| SAF-T / e-invoicing mandates | T3 -- national mandates not covered; varies significantly by country | same |
| VAT groups | T3 -- not covered; varies by country (Article 11 option) | same |
| Capital goods adjustment period | T3 -- varies by country; covered in country skills | same |

Practitioner review required for: rate table accuracy (verify against EC TEDB and the country skill), any T2 rules before advising clients.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Council Directive 2006/112/EC, consolidated text of 14 April 2025 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 | 2026-10-30 |
| Council Implementing Regulation (EU) No 282/2011, consolidated text of 14 April 2025 (Articles 18, 45a) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02011R0282-20250414 | 2026-10-30 |
| Council Directive (EU) 2025/516 (ViDA) | https://eur-lex.europa.eu/eli/dir/2025/516/oj/eng | 2026-10-30 |
| Council Regulation (EU) 2025/517 | https://eur-lex.europa.eu/eli/reg/2025/517/oj/eng | 2026-10-30 |
| Council Implementing Regulation (EU) 2025/518 | https://eur-lex.europa.eu/eli/reg_impl/2025/518/oj/eng | 2026-10-30 |
| Council Directive (EU) 2025/1539 | https://eur-lex.europa.eu/eli/dir/2025/1539/oj/eng | 2026-10-30 |
| Council Directive (EU) 2020/285 (SME scheme) | https://eur-lex.europa.eu/eli/dir/2020/285/oj/eng | 2026-10-30 |
| Council Directive (EU) 2022/542 (VAT rates) | https://eur-lex.europa.eu/eli/dir/2022/542/oj/eng | 2026-10-30 |
| Agreement on the withdrawal of the United Kingdom from the EU (OJ L 29, 31.1.2020), Article 126 and Protocol on Ireland/Northern Ireland, Article 8 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12020W/TXT | 2026-10-30 |
| Council Directive 2008/9/EC (refunds), Article 15 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32008L0009 | 2026-10-30 |
| European Commission TEDB VAT rates web service (situations on 31 December 2023 to 30 October 2026) | https://ec.europa.eu/taxation_customs/tedb/ | 2026-10-30 |
| European Commission, VAT rates (secondary guidance) | https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/vat-rates_en | 2026-10-30 |
| Irish Revenue, Current VAT rates | https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx | 2026-10-30 |

Not yet confirmed: each country's domestic zero rates (the old table showed "Yes" for every country; replaced by the parking-rate column and a note); whether any member state's Article 199a reverse charge continues after 31 December 2026 (an extension proposal was not read in the Official Journal); national e-invoicing and SAF-T start dates; Intrastat thresholds.

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
