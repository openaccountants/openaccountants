---
name: eu-vat-base
description: "Load this skill as a shared reference whenever working on VAT for any EU member state in tax year 2026. Contains the common rules from Council Directive 2006/112/EC (consolidated to 14 April 2025) and Implementing Regulation 282/2011 that apply across all 27 EU member states -- intra-community supplies and acquisitions, reverse charge mechanics, place of supply rules, the EUR 10,000 distance selling threshold, OSS and IOSS, the SME scheme (EUR 85,000 national cap, EUR 100,000 Union cap), the reduced-rate framework, the 2026 rate table and the ViDA timetable (2025, 2027, 2028, 2029, 2030, 2035). Always load the country-specific VAT skill alongside this one. Do NOT use this skill alone -- it must be combined with the relevant country skill (e.g. ireland-vat-return, germany-vat-return) which overrides anything country-specific. Article-by-article companion: eu-vat-directive."
jurisdiction: EU
tax_year: 2026
last_updated: 2026-10-30
version: 2.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EU VAT Base

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Scope | All 27 EU Member States |
| Primary Legislation | Council Directive 2006/112/EC of 28 November 2006 (consolidated version of 14 April 2025, the latest consolidation; no later amendment applies before 2027) |
| Supporting Legislation | Directive (EU) 2022/542 (reduced rates reform); Directive (EU) 2020/285 (SME scheme, applies from 1 January 2025); Implementing Regulation 282/2011 (consolidated 14 April 2025); ViDA package: Directive (EU) 2025/516, Regulation (EU) 2025/517, Implementing Regulation (EU) 2025/518; Directive (EU) 2025/1539 (import VAT, from 1 July 2028); Directive 2008/9/EC (refunds) |
| Source | EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 |
| Contributor | Open Accounting Skills Registry |
| Version | 2.1 |
| Rates Current As Of | 30 October 2026 (TEDB, with 2026 mid-year changes dated) |
| Status | awaiting-validation |
| Format | Q1 Step Format |
| Note | This skill contains ONLY rules common to all EU member states. Country-specific rules (form boxes, national rates, filing deadlines, small business thresholds) are in the country skill. The country skill overrides this one where there is any conflict. |

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Derived directly from the Directive. Applies in all member states unless the country skill specifies otherwise.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Rule exists in the Directive but national implementation varies. Check the country skill.
- **[T3] Tier 3 -- Out of Scope.** Not covered by this skill. Refer to country skill or warranted practitioner.

## Step 0: Jurisdiction Check [T1]

**Legislation:** Directive 2006/112/EC, Articles 1, 5 and 6

**Purpose:** Confirm which EU member state(s) are involved before proceeding.

### 0.1 Current EU Member States (27)

- **Current EU Member States (27)**: AT Austria | BE Belgium | BG Bulgaria | HR Croatia | CY Cyprus | CZ Czech Republic | DK Denmark | EE Estonia | FI Finland | FR France | DE Germany | GR Greece (EL in VAT numbers) | HU Hungary | IE Ireland | IT Italy | LV Latvia | LT Lithuania | LU Luxembourg | MT Malta | NL Netherlands | PL Poland | PT Portugal | RO Romania | SK Slovakia | SI Slovenia | ES Spain | SE Sweden

### 0.2 NOT EU (treat as non-EU / third country)

- UK: outside the EU. EU VAT law stopped applying to it at the end of the transition period on 31 December 2020 (Withdrawal Agreement, Article 126). Exception: the EU VAT rules on goods still apply in Northern Ireland (Protocol on Ireland/Northern Ireland, Article 8), so goods moving between Northern Ireland and a member state follow the intra-community rules in Step 3. The Protocol covers goods only: for services, Northern Ireland is part of the UK, a third country. [T2] Check the UK skill for the Northern Ireland mechanics.
- Norway, Switzerland, Iceland (EEA or EFTA but not EU)
- USA, Canada, Australia, UAE, and all other non-EU countries
- Parts of member states that are outside the EU VAT area (Article 6): Mount Athos, the Canary Islands, the French territories in Articles 349 and 355(1) TFEU, the Aland Islands, the Channel Islands, Campione d'Italia, the Italian waters of Lake Lugano, Heligoland, Busingen, Ceuta, Melilla and Livigno. Supplies to and from these places are treated like third-country trade.

### 0.3 Jurisdiction Checklist

Before proceeding to Step 1, confirm:
- [ ] Which member state is the supplier established in (business seat or fixed establishment)?
- [ ] Which member state (or non-EU country) is the customer established in?
- [ ] Is the customer VAT-registered? (Check VIES: https://ec.europa.eu/taxation_customs/vies/)
- [ ] Is the transaction B2B or B2C?
- [ ] Goods or services? If goods, where does transport start and end?

## Step 1: EU VAT Fundamentals [T1]

**Legislation:** Directive 2006/112/EC, Articles 1-4, 138, 168, 176, 178, 217-240; Implementing Regulation 282/2011, Article 18

### 1.1 Core Principle

- **Core Principle**: VAT is a consumption tax borne by the final consumer. Businesses act as collection agents -- they charge VAT on sales (output VAT), deduct VAT on purchases (input VAT, Article 168), and remit the difference to the tax authority. To deduct VAT on a purchase, the business must hold a valid invoice (Article 178(a)).

### 1.2 VAT Number Validation

- **VAT Number Validation**: Before applying zero rate (exempt intra-community supply of goods or B2B services): verify the customer's VAT number is valid using the EU VIES system: https://ec.europa.eu/taxation_customs/vies/.
  - Goods: the exemption for an intra-community supply needs a customer identified for VAT in another member state who has given that number to the supplier (Article 138(1)(b)).
  - Services: unless the supplier has information to the contrary, it may treat an EU customer as a taxable person when the customer has given its VAT number and the supplier has confirmed its validity and the linked name and address (Implementing Regulation 282/2011, Article 18(1)(a), through VIES under Regulation 904/2010, Article 31).
  - If VIES validation fails, do not zero-rate -- apply local VAT rate. Keep the VIES confirmation with the invoice.

### 1.3 Invoicing Requirements

- **Invoicing Requirements**: Mandatory invoice elements for all EU member states (Article 226): Date of issue; Sequential invoice number; Supplier VAT number; Customer VAT number (for B2B intra-community supplies and reverse-charge supplies); Full name and address of supplier and customer; Description of goods or services; Date of supply (if different from invoice date); Taxable amount per VAT rate; VAT rate applied; VAT amount payable; For exempt intra-community supplies: reference to the exemption (Article 226(11), e.g. "Article 138 Directive 2006/112/EC"); For reverse charge: the mention "Reverse charge" (Article 226(11a)); for self-billing: "Self-billing" (Article 226(10a)); under cash accounting: "Cash accounting" (Article 226(7a)).
- **Invoice deadline for cross-border B2B**: For an exempt intra-community supply of goods (Article 138) or a B2B service where the customer pays the VAT under Article 196, the invoice must be issued no later than the 15th day of the month after the month of the chargeable event (Article 222). For other supplies the member state sets the deadline.
- **E-invoicing in 2026**: Since 14 April 2025 a member state may require businesses established there to issue electronic invoices for domestic supplies without asking the EU for permission, and may drop the need for the buyer's consent (Articles 218 and 232 as amended by Directive (EU) 2025/516, Article 1). [T2] Whether a domestic e-invoicing mandate applies in 2026, and from what date, is a national rule: check the country skill. EU-wide mandatory e-invoicing for intra-EU B2B starts only on 1 July 2030 (see Step 8).

### 1.4 Blocked Categories -- Common EU Rules

- **Blocked Categories -- Common EU Rules**: Article 176 says VAT is never deductible on expenditure that is not strictly business expenditure, "such as that on luxuries, amusements or entertainment", and lets member states keep the exclusions their national law had on 1 January 1979 (or on their accession date) until the Council adopts common rules (standstill clause). As a result, blocked categories vary significantly by country. Common categories blocked in most EU member states [T1]: - Entertainment expenses (client meals, hospitality) - Personal use items. Categories blocked in some but not all member states [T2]: - Motor vehicles (blocked in some, partially allowed in others) - Fuel (varies by country and vehicle type) - Accommodation (varies). **Always check the country skill for the specific blocked categories for that jurisdiction.**  _(Directive 2006/112/EC, Articles 176-177)_

## Step 2: Rate Framework [T1]

**Legislation:** Directive 2006/112/EC, Articles 93-105b and Annex III, as amended by Directive (EU) 2022/542

### 2.1 Rate Structure Rules (apply in all member states)

**Rate Structure Rules Table**

| Rule | Detail | Article |
| --- | --- | --- |
| Standard rate minimum | Cannot be lower than 15%; the same rate for goods and services | Articles 96, 97 |
| Reduced rates | Maximum two reduced rates, neither below 5%, only for goods and services in Annex III, in a maximum of 24 Annex III points | Article 98(1) |
| Super-reduced rate and zero rate | In addition, one rate below 5% and one exemption with deduction of input VAT ("zero rate"), for a maximum of seven Annex III points, chosen from points (1) to (6) and (10c) (food, water, medicines, medical equipment and aids for health care or disability, passenger transport, books and press, and solar panels on or near homes and public buildings) or from items covered by Article 105a(1) | Article 98(2) |
| Acquired rights below 5% or zero | Rates below 5% and zero rates that a member state applied on 1 January 2021 may continue; rates below 12% (including below 5% and zero) on items outside Annex III may continue until 1 January 2032 at the latest | Article 105a(1), (2) |
| Parking rate | Minimum 12% -- reduced rates of at least 12% that a member state applied on 1 January 2021 to items outside Annex III may continue | Article 105a(3) |
| Fossil fuels and pesticides | Reduced rates and zero rates on fossil fuels, peat and firewood end by 1 January 2030; on chemical pesticides and chemical fertilisers by 1 January 2032 | Article 105a(4) |
| Electronically supplied services | No reduced rate except for items in Annex III points (6), (7), (8) and (13) (e-books and e-press, broadcasting, admission including live-streamed events) | Article 98(3) |
| Rate on acquisitions and imports | Same rate as a domestic supply of like goods in that member state | Article 94 |

### 2.2 2026 Rate Table -- All EU Member States

**2026 Rate Table -- All EU Member States** (main rates for the mainland; source: European Commission Taxes in Europe Database (TEDB) web service, situation on 30 October 2026, compared with 1 January 2026)

| Country | Code | Standard | Reduced 1 | Reduced 2 | Super-Reduced (below 5%) | Parking (12% or more) |
| --- | --- | --- | --- | --- | --- | --- |
| Austria | AT | 20% | 10% | 13% | 4.9% (foodstuffs, from 1 July 2026) | -- |
| Belgium | BE | 21% | 6% | 12% | -- | 12% |
| Bulgaria | BG | 20% | 9% | -- | -- | -- |
| Croatia | HR | 25% | 5% | 13% | -- | -- |
| Cyprus | CY | 19% | 5% | 9% | 3% | -- |
| Czech Republic | CZ | 21% | 12% | -- | -- | -- |
| Denmark | DK | 25% | -- | -- | -- | -- |
| Estonia | EE | 24% | 9% | 13% | -- | -- |
| Finland | FI | 25.5% | 10% | 13.5% | -- | -- |
| France | FR | 20% | 5.5% | 10% | 2.1% | -- |
| Germany | DE | 19% | 7% | -- | -- | -- |
| Greece | GR | 24% | 6% | 13% | 4% (narrow: renovation work for persons with disabilities) | 13% |
| Hungary | HU | 27% | 5% | 18% | -- | -- |
| Ireland | IE | 23% | 9% | 13.5% | 4.8% (livestock) | -- |
| Italy | IT | 22% | 5% | 10% | 4% | -- |
| Latvia | LV | 21% | 5% | 12% | -- | -- |
| Lithuania | LT | 21% | 5% | 12% | -- | -- |
| Luxembourg | LU | 17% | 8% | -- | 3% | 14% |
| Malta | MT | 18% | 5% | 7% | -- | 12% |
| Netherlands | NL | 21% | 9% | -- | -- | -- |
| Poland | PL | 23% | 5% | 8% | -- | -- |
| Portugal | PT | 23% | 6% | 13% | -- | 13% |
| Romania | RO | 21% | 11% | -- | -- | -- |
| Slovakia | SK | 23% | 5% | 19% | -- | -- |
| Slovenia | SI | 22% | 5% | 9.5% | -- | -- |
| Spain | ES | 21% | 10% | -- | 4% | -- |
| Sweden | SE | 25% | 6% | 12% | -- | -- |

**Zero rates.** Every member state exempts intra-community supplies of goods (Article 138) and exports (Article 146) with the right to deduct input VAT, which works like a 0% rate. Domestic zero rates under Article 98(2) and 105a are national and listed in TEDB per product: check the country skill.

**Regional rates (not in the table).** TEDB also lists regional rates: Austria 19% (Jungholz and Mittelberg); Greece 17% on the islands of Leros, Lesvos, Kos, Samos and Chios; Portugal 16% (Azores) and 22% (Madeira) standard rates; separate rates for Corsica in France. The Canary Islands are outside the EU VAT area (Article 6).

**Note:** Always verify current rates against the European Commission's TEDB (Taxes in Europe Database) and the country skill before filing. TEDB data is supplied by the member states themselves.

**Key changes since 2024:**
- Estonia: standard rate increased from 22% to 24% (1 July 2025); accommodation reduced rate raised from 9% to 13% (1 January 2025)
- Finland: standard rate increased from 24% to 25.5% (1 September 2024); the 14% reduced rate is 13.5% from 1 January 2026, alongside the 10% rate
- Ireland: livestock rate 4.8% confirmed (Revenue rate table, 1 January 2026); restaurant and catering services and hairdressing moved from 13.5% to 9% on 1 July 2026 (TEDB)
- Lithuania: reduced rates restructured to 5% and 12% from 1 January 2026 (the 9% rate became 12%). In TEDB the 5% rate covers books, newspapers and periodicals, medicines and medical equipment; the 12% rate covers hotel accommodation, passenger transport and admission to shows and cultural events
- Luxembourg: standard rate returned to 17% on 1 January 2024 (the temporary 16% rate applied until 31 December 2023, not 2024 as an earlier version said); parking rate 14%
- Romania: standard rate increased from 19% to 21% (1 August 2025); reduced rates consolidated from 5%/9% to single 11% rate
- Slovakia: standard rate increased from 20% to 23% (1 January 2025); reduced rates restructured to 5%/19%
- Belgium: hotel accommodation moved from 6% to 12% on 1 March 2026 (TEDB)
- Sweden: foodstuffs moved from 12% to 6% on 1 April 2026 (TEDB)
- Austria: a 4.9% rate applies to the foodstuffs listed in Annex 3 to section 10 of the Austrian VAT Act from 1 July 2026 (TEDB)

## Step 3: Intra-Community Rules [T1]

**Legislation:** Directive 2006/112/EC, Articles 2(1)(b), 17a, 20, 36a, 40-42, 67, 69, 94, 138, 141, 262-265; Implementing Regulation 282/2011, Article 45a

### 3.1 Intra-Community Acquisitions (ICA) -- Definition

- **Intra-Community Acquisitions (ICA) -- Definition**: An ICA occurs when physical goods are dispatched or transported from one EU member state to another, and the buyer is a taxable person or a non-taxable legal person (Articles 2(1)(b) and 20). In practice: B2B goods movements between VAT-registered businesses.

### 3.2 ICA Rules

- **ICA Rules**:
  - The place of ICA is where transport ends (Article 40). If the buyer quotes a VAT number from a different member state, VAT is also due there until the buyer shows it was taxed where transport ended (Article 41).
  - The acquiring business is liable for VAT (self-assessment, often called reverse charge).
  - The supplier invoices at 0% (exempt intra-community supply, Article 138).
  - The acquirer self-assesses output VAT at the rate that applies to a domestic supply of the same goods in the member state of arrival (Article 94(1)) -- usually the standard rate, but a reduced rate where the goods qualify -- AND claims the same amount as input VAT (Article 168(c)).
  - Net cash effect = zero for a fully taxable business.
  - VAT becomes chargeable when the invoice is issued, or on the 15th day of the month after the supply if no invoice has been issued by then (Articles 67 and 69).
  - The supplier must quote the customer's VAT number on the invoice (Article 226(4)).
  - The supplier must report the sale on an EC Sales List (ESL) / Recapitulative Statement.

### 3.3 Conditions for the 0% (exempt) intra-community supply

- **Conditions**: The supplier may apply the exemption only if (Article 138(1) and (1a)):
  1. the goods are dispatched or transported to another member state;
  2. the customer is a taxable person or non-taxable legal person in another member state, identified for VAT there, and has given that VAT number to the supplier;
  3. the supplier files a correct recapitulative statement for the supply (otherwise the exemption is lost unless the supplier can justify the error).
- **Proof of transport**: It is presumed that goods left the member state if the supplier holds two non-contradictory documents from two independent parties (for example a signed CMR and a carrier's invoice), or one transport document plus one other item such as an insurance policy or bank payment for the transport. If the customer arranges transport, the supplier also needs the customer's written statement, which the customer must give by the 10th day of the month after the supply (Implementing Regulation 282/2011, Article 45a). The tax authority can rebut the presumption.

### 3.4 Invoice Reference

- **Invoice Reference**: Supplier invoice must refer to the exemption, e.g. "VAT exempt intra-Community supply -- Article 138(1) Directive 2006/112/EC" (Article 226(11)). Use the national-law reference if the country skill gives one.

### 3.5 EC Sales List / Recapitulative Statement

- **EC Sales List / Recapitulative Statement**: Every VAT-registered business that makes exempt intra-community supplies of goods, B2B services taxed in the customer's member state under Article 44 and paid by the customer under Article 196, or call-off stock transfers must file an EC Sales List (called Recapitulative Statement in the Directive) reporting customer VAT numbers and total value supplied to each customer for the period (Articles 262 and 264).
  - Default: one statement per calendar month, filed within one month (Article 263(1)).
  - A member state may allow a quarterly statement, due within one month of the quarter end, if intra-community supplies of goods do not exceed EUR 50,000 in the quarter or in any of the previous four quarters; once goods exceed EUR 50,000 in a quarter, monthly filing starts from that month (Article 263(1a)).
  - For services only, a member state may allow quarterly filing without a cap (Article 263(1c)).
  - Filing frequency and format varies by country -- check country skill.

### 3.6 Local Consumption Exception

- **Local Consumption Exception**: When a business pays for services consumed locally in another EU country (hotel, restaurant, taxi, conference admission), the VAT is charged locally by the supplier at their national rate. This is NOT reverse charge. The legal reason: hotel accommodation is taxed where the property is (Article 47), restaurant services where they are carried out (Article 55), passenger transport where it takes place (Article 48), and B2B admission to events where the event takes place (Article 53). Examples: - Employee stays in a Paris hotel -- French VAT charged, not reverse charge - Delegate attends a Berlin conference -- German VAT charged, not reverse charge - Business lunch in Amsterdam -- Dutch VAT charged, not reverse charge. The foreign VAT paid is an expense unless the business files a cross-border VAT refund claim under Directive 2008/9/EC. [T2] Cross-border VAT refund claims: possible for EU businesses through the online portal of their own member state; the claim must be filed by 30 September of the year after the refund period (Directive 2008/9/EC, Article 15(1)). Deductibility follows the rules of the member state of refund (blocked items stay blocked). Flag for reviewer if amounts are material.
- **Virtual attendance**: From 1 January 2025, Article 53 does not apply when a business attends an event virtually; the general B2B rule (Article 44, reverse charge) applies instead (Directive (EU) 2022/542).

### 3.7 Chain transactions and call-off stock

- **Chain transactions**: Where goods are sold along a chain (A to B to C) but travel directly from A's member state to C's, only one supply carries the transport and can be the 0% intra-community supply. By default that is the supply TO the intermediary (B) who arranges the transport. If B gives A a VAT number from the member state of departure, the transport is ascribed to B's supply to C instead (Article 36a). The other supply is a domestic supply in the member state of departure or arrival.
- **Call-off stock**: Goods sent to a known customer in another member state, held there and taken by that customer within 12 months, are treated as one exempt supply and one acquisition when the customer takes them, provided the conditions of Article 17a are met (no establishment of the supplier there, customer's VAT number known, register kept, goods listed on the recapitulative statement). [T2] Article 17a is wound down by ViDA: only goods sent on or before 30 June 2028 qualify, and the article stops applying on 30 June 2029 (Directive (EU) 2025/516, Article 2).

## Step 4: Reverse Charge Framework [T1]

**Legislation:** Directive 2006/112/EC, Articles 44, 194, 196, 199a

### 4.1 The General B2B Rule (Article 44)

- **The General B2B Rule (Article 44)**: For services supplied to a taxable person acting as such, the place of supply is where the customer is established (or the fixed establishment receiving the service). Consequence: when the supplier is not established in the customer's member state, the supplier charges 0% VAT and the customer pays the VAT (Article 196): it self-assesses output VAT at its local rate and claims the same as input VAT. Net effect = zero for a fully taxable business.

### 4.2 Mandatory for

- **Mandatory for**: - All B2B cross-border services where Article 44 applies and the supplier is not established in the customer's member state (Article 196) - Services supplied by a non-EU supplier to an EU VAT-registered customer - Also applies to a non-taxable legal person that is identified for VAT (Article 196).

### 4.3 Invoice Reference

- **Invoice Reference**: Supplier invoice must carry the mention "Reverse charge" (Article 226(11a)). Many suppliers add "Articles 44 and 196 Directive 2006/112/EC". The invoice is due by the 15th day of the following month (Article 222).

### 4.4 Non-EU Supplier to EU Business

- **Non-EU Supplier to EU Business**: When a non-EU supplier (US, UK, CH, AU etc.) provides services to an EU VAT-registered business: - Supplier invoices at 0% (no EU VAT charged) - EU customer self-assesses output VAT at local rate - EU customer claims same amount as input VAT (if fully taxable) - Net effect = zero for fully taxable business - This applies to: software subscriptions, cloud hosting, consulting services, digital services, IP licences, advertising. **Common examples:** AWS, Google Workspace, Microsoft 365, Notion, Slack, Stripe fees, LinkedIn ads -- all trigger reverse charge when purchased by an EU VAT-registered business that is the customer under Article 44. [T2] Check who the contracting entity is: some of these providers invoice from an EU entity, which is still a cross-border reverse charge if that entity is in another member state, but a domestic VAT charge if it is in the customer's own member state.  _(Directive 2006/112/EC, Articles 44, 196)_

### 4.5 Domestic reverse charges in 2026 [T2]

- **Supplies by non-established suppliers**: Article 194 lets a member state make the customer liable for VAT on any domestic supply of goods or services by a supplier not established there. In 2026 this is optional and national. From 1 July 2028 it becomes mandatory where the customer is already VAT-identified in that member state (Directive (EU) 2025/516, Article 3).
- **Optional domestic reverse charge for fraud-prone supplies** (e.g. mobile phones, integrated circuits, gas and electricity to dealers, emission allowances): Article 199a allows these until 31 December 2026. Check the country skill for which items apply and whether the national rule continues into 2027.

### 4.6 Import of Physical Goods from Non-EU [T2]

- **Import of Physical Goods from Non-EU**: When physical goods are imported from outside the EU: - Import VAT is charged at the border by Customs, not via reverse charge on the VAT return - Import VAT is paid to Customs at the point of entry, at the rate for a domestic supply of like goods (Article 94(2)) - The business recovers import VAT as input tax via the VAT return (Article 168(e)), using the Customs entry document - Reverse charge on the VAT return is NOT used for physical goods imports, unless the member state has a postponed accounting scheme (Article 211) [T2]. Process and documentation varies by country. Flag for reviewer to confirm: (a) client has the customs entry document, (b) import VAT amount is correct, (c) recovery is allowable.  _(Directive 2006/112/EC, Articles 30, 60, 70-71, 94(2), 168(e), 211; national customs legislation)_
- **Low-value consignments (IOSS)**: B2C distance sales of goods imported in consignments of an intrinsic value up to EUR 150 (excluding excise goods) can be declared through the Import One Stop Shop. The import is then VAT-exempt at the border and the seller charges the customer's member state VAT at checkout (Articles 143(1)(ca) and 369l). A platform that facilitates such sales is deemed to be the supplier (Article 14a(1)). From 1 July 2028, for such sales not declared under IOSS, the supplier or the deemed supplier, not the customer, becomes liable for the import VAT (new Article 201(2), Directive (EU) 2025/1539).

## Step 5: Place of Supply Rules [T1/T2]

**Legislation:** Directive 2006/112/EC, Articles 31-59c

### 5.1 Goods

**Goods**

| Scenario | Place of Supply | Article |
| --- | --- | --- |
| Goods not dispatched/transported | Where goods are located at time of supply | Article 31 |
| Goods dispatched/transported by or for the supplier or customer | Where dispatch/transport begins | Article 32 |
| Intra-community acquisition | Where transport ends | Article 40 |
| Intra-community distance sales (B2C) | Where transport ends (customer's member state), unless the EUR 10,000 rule in Article 59c applies | Articles 33(a), 59c |
| Distance sales of imported goods (B2C) | Where transport ends; or the member state of import if declared under IOSS | Article 33(b), (c) |
| Chain transactions | Transport ascribed to one supply only | Article 36a |

### 5.2 Services -- General Rules

**Services -- General Rules**

| Scenario | Place of Supply | Article |
| --- | --- | --- |
| B2B services (general rule) | Where customer is established | Article 44 |
| B2C services (general rule) | Where supplier is established | Article 45 |

### 5.3 Services -- Exceptions to Articles 44 and 45 [T2]

These services are taxed where performed or where the customer lives, not under the general rule:

**Services -- Exceptions**

| Service Type | Place of Supply | Directive Article |
| --- | --- | --- |
| Services related to immovable property (including hotel accommodation, estate agents, architects) | Where property is located | Article 47 |
| Passenger transport | Where the transport takes place, in proportion to distances covered | Article 48 |
| B2C transport of goods (not intra-community) | Where the transport takes place, by distance | Article 49 |
| B2C intra-community transport of goods | Place of departure | Article 50 |
| Admission to cultural, sports, educational and similar events (B2B) | Where event takes place; not if attendance is virtual | Article 53 |
| Cultural, sports, educational and similar activities (B2C) | Where they take place; if streamed or virtual, where the customer lives (from 1 January 2025) | Article 54(1) |
| B2C ancillary transport services and work on movable goods | Where physically carried out | Article 54(2) |
| Restaurant / catering services | Where physically carried out | Article 55 |
| Catering on board ships, aircraft, trains in the EU | Point of departure | Article 57 |
| Short-term hire of transport (up to 30 days; vessels up to 90 days) | Where vehicle put at disposal | Article 56(1), (3) |
| Long-term hire of transport (B2C) | Where the customer lives | Article 56(2) |
| Telecoms, broadcasting and electronically supplied services (B2C) | Where the customer lives | Article 58 |

[T2] For any of these exception categories, flag for reviewer to confirm correct place of supply treatment.

## Step 6: Common Thresholds [T1]

**Legislation:** Directive 2006/112/EC, Articles 33, 58, 59c, 281-294, 358-369zb; Directive (EU) 2020/285

### 6.1 Distance Selling -- B2C Cross-Border (EUR 10,000 Threshold)

- **Distance Selling -- B2C Cross-Border Threshold**: The EUR 10,000 threshold applies only when ALL of these are true (Article 59c(1)): the supplier is established (or lives) in only one member state; the sales are intra-community distance sales of goods sent from that member state, or telecoms, broadcasting and electronically supplied services (Article 58) to non-taxable customers in other member states; and the total of those sales across ALL other EU countries combined, excluding VAT, did not exceed EUR 10,000 in the current calendar year nor in the previous one.
  - Below EUR 10,000: apply VAT at the supplier's own country rate.
  - Once the total exceeds EUR 10,000 during a year, the customer's member state rate applies from that sale onwards (Article 59c(2)) (destination principle). The supplier must either register in each destination country OR use the OSS (One Stop Shop).
  - A supplier below the threshold may opt for destination taxation; the option binds for at least two calendar years (Article 59c(3)).
  - Other B2C services (e.g. consulting, accountancy) are not covered: they follow Article 45 or the specific rules in Step 5, with no threshold.

### 6.2 One Stop Shop (OSS)

- **One Stop Shop (OSS)**: Allows a supplier to register in one EU member state and declare and pay VAT for all EU B2C distance sales of goods and B2C services in member states where it is not established, through that single registration (Union scheme, Articles 369a-369k; non-Union scheme for non-EU businesses selling services, Articles 358-369). Eliminates the need to register separately in every customer's country.
  - Returns are quarterly, due by the end of the month after the quarter, and must be filed even if nothing was sold (Articles 364 and 369f).
  - Import OSS (IOSS) returns are monthly, due by the end of the following month (Article 369s).
  - Input VAT cannot be deducted in the OSS return; it is reclaimed under Directive 2008/9/EC or through a local VAT return (Article 369j).
  - [T2] If client makes significant B2C sales across EU: flag for reviewer to assess OSS registration requirement.

### 6.3 SME Scheme

- **SME Scheme (Directive 2020/285, applies from 1 January 2025)**: Member states may exempt small enterprises from VAT below a national threshold. Thresholds vary by country. Check the country skill for the specific threshold. The EU rules:
  - The national threshold may not exceed **EUR 85,000** of annual turnover in that member state (Article 284(1)). Sector thresholds are allowed, but none above EUR 85,000.
  - **Cross-border SME exemption**: a small business established in one member state can use the exemption in other member states that have one, if its **Union annual turnover does not exceed EUR 100,000** and its turnover in each host member state is within that state's threshold (Article 284(2)).
  - To use it, the business sends a prior notification to its own member state and receives an identification number with the suffix "EX" (Article 284(3)). The exemption applies from the date the number is given, at the latest 35 working days after the notification (Article 284(5)).
  - Exceeding the threshold: the exemption is lost for the following calendar year. During the year, a business that exceeds the national threshold by not more than 10% keeps the exemption for that year; above 10% it ends at once. Member states may instead set a 25% ceiling or no ceiling, but never so that turnover above EUR 100,000 stays exempt, or may end the exemption as soon as the threshold is passed (Article 288a(1)). A non-established business loses the cross-border exemption as soon as its Union turnover passes EUR 100,000 (Article 288a(2)).
  - Turnover for the test excludes sales of capital assets (Article 288(2)).

## Step 7: Filing Obligations [T1/T2]

**Legislation:** Directive 2006/112/EC, Articles 206, 250-252, 262-265

### 7.1 VAT Return

- **VAT Return**: All VAT-registered businesses must file periodic VAT returns (Article 250). Each member state sets the tax period at one, two or three months, or a different period of up to one year (Article 252(2)). The return deadline may not be more than two months after the end of the period (Article 252(1)). The net VAT is paid when the return is submitted unless the member state sets another date or interim payments (Article 206). Exact frequency and deadlines vary by country -- check country skill.

### 7.2 EC Sales List (Recapitulative Statement)

Required for all exempt intra-community supplies of goods, B2B reverse-charge services under Article 44, and call-off stock transfers. Monthly by default; quarterly options in Article 263. See Step 3.5.

### 7.3 Intrastat

- **Intrastat**: [T2] Businesses exceeding national Intrastat thresholds must file statistical declarations for intra-EU movements of goods. Intrastat is a statistics duty, not a VAT rule. Thresholds and requirements vary by country -- check country skill.

### 7.4 SAF-T / Digital Reporting

- **SAF-T / Digital Reporting**: [T2] Several EU member states require Standard Audit File for Tax (SAF-T), real-time invoice reporting or other digital reporting formats under national law. Requirements vary significantly -- check country skill. The EU-wide digital reporting for intra-EU B2B transactions starts on 1 July 2030 (Step 8).

## Step 8: ViDA (VAT in the Digital Age) timetable [T1]

**Legislation:** Directive (EU) 2025/516 (in force 14 April 2025), Regulation (EU) 2025/517, Implementing Regulation (EU) 2025/518

None of the ViDA changes below, other than the 2025 e-invoicing options, applies in tax year 2026. Use this to plan.

| Applies from | What changes | Source |
| --- | --- | --- |
| 14 April 2025 | Member states may require domestic e-invoices without EU authorisation, and without the buyer's consent | Directive 2025/516, Article 1(2), (3) and Article 6(1) |
| 1 January 2027 | Cash accounting rules reworded (Article 66); the EUR 10,000 Article 59c threshold counts only goods sent from the supplier's own member state; the non-Union OSS can be used by a non-EU supplier of B2C services that is also VAT-registered in a member state; OSS covers B2C supplies of gas, electricity, heat and cooling by non-established suppliers until 30 June 2028 (Article 369aa) | Directive 2025/516, Article 2 and Article 6(2) |
| 1 July 2028 | Platforms deemed suppliers of short-term accommodation rental (up to 30 nights) and road passenger transport (member states may delay to 1 January 2030); mandatory reverse charge for non-established suppliers where the customer is VAT-identified (new Article 194); OSS extended to domestic B2C supplies of goods by non-established suppliers and to energy supplies (new Article 369b), and a new OSS for transfers of own goods; invoice deadline extended to Article 194 supplies; no new call-off stock movements after 30 June 2028 | Directive 2025/516, Article 3 and Article 6(3) (call-off stock: Article 2); Implementing Regulation 2025/518 |
| 1 July 2028 | Supplier or deemed supplier, not the customer, liable for import VAT on distance sales of imported goods up to EUR 150 not declared under IOSS; a supplier established in a third country with no mutual-assistance agreement must appoint a tax representative unless the import is exempt under IOSS | Directive 2025/1539, Articles 1 and 2 (new Article 201) |
| 1 July 2029 | Call-off stock register and call-off recapitulative statement removed (Article 17a ends 30 June 2029) | Directive 2025/516, Article 4 and Article 2 |
| 1 July 2030 | Electronic invoices in the European standard (EN 16931) become the default; intra-EU B2B invoices within 10 days of the chargeable event; digital reporting of each intra-EU B2B transaction replaces the recapitulative statement (supplier reports when the invoice is issued, buyer within 5 days of receipt); recipient's consent no longer needed for standard e-invoices | Directive 2025/516, Article 5 and Article 6(5) |
| 1 July 2032 | Last stage of the administrative cooperation changes | Regulation 2025/517, Article 6 |
| 1 January 2035 | Member states that had a domestic real-time reporting system before 1 January 2024 must align it with the EU standard | Directive 2025/516, Article 6(5), second subparagraph |

## PROHIBITIONS

- **Prohibitions**: - NEVER zero-rate an intra-community supply without a valid customer VAT number verified on VIES and without including it on the recapitulative statement - NEVER zero-rate goods without proof that they left the member state - NEVER apply reverse charge to services consumed locally in another EU country (hotel, restaurant, taxi) - NEVER apply reverse charge to physical goods imports -- import VAT is handled via Customs (unless a national postponed accounting scheme applies) - NEVER use this skill alone -- always load the country skill alongside it - NEVER override the country skill with this base skill -- the country skill takes precedence on all national specifics - NEVER present EU-wide rules as applying without exception -- national derogations exist and are significant - NEVER apply ViDA rules that start after 2026 to 2026 transactions

## Edge Case Registry

**Edge Case Registry**

| # | Scenario | Correct Treatment | Common Mistake |
| --- | --- | --- | --- |
| 1 | EU business buys SaaS from US company | Reverse charge: self-assess output VAT + claim as input VAT | Treating as out-of-scope (no VAT entry) |
| 2 | Employee hotel stay in another EU country | Local VAT charged by hotel; NOT reverse charge | Applying reverse charge on the VAT return |
| 3 | Physical goods imported from China | Import VAT via Customs; recover on VAT return | Applying reverse charge instead of import VAT |
| 4 | B2B sale of goods to EU customer without valid VAT number | Charge local VAT at the domestic rate for those goods; do NOT zero-rate | Zero-rating without VIES validation |
| 5 | B2C distance sales under EUR 10,000, supplier established in one member state | Apply supplier's own country VAT rate | Applying customer's country rate below threshold |
| 6 | B2C distance sales above EUR 10,000 | Apply customer's country VAT rate (OSS or local registration) | Continuing to apply supplier's country rate |
| 7 | Chain transaction (A sells to B, B sells to C, goods go direct A to C) | Only one leg qualifies as intra-community supply (Article 36a: by default the supply to the intermediary who transports); other is domestic | Treating both legs as intra-community |
| 8 | Business attends a conference online, organiser in another member state | General B2B rule (Article 44): reverse charge; Article 53 does not apply to virtual attendance | Paying the organiser's local VAT |
| 9 | Business established in two member states sells online B2C below EUR 10,000 | The threshold is not available (Article 59c(1)(a)); destination VAT from the first sale | Applying the home rate |
| 10 | Small business uses the SME exemption in another member state | Needs Union turnover up to EUR 100,000, prior notification and an "EX" number | Assuming the home exemption covers all of the EU |

## Test Suite

**Test Suite**

| # | Input | Expected Output | Step |
| --- | --- | --- | --- |
| T1 | Irish VAT-registered business buys consulting from German VAT-registered firm | Reverse charge: Irish business self-assesses Irish VAT (23%) as output and input | Step 4.1 |
| T2 | French business buys standard-rated goods from German business, goods shipped DE to FR | ICA in France; French business self-assesses French VAT (20%) as output and input | Step 3.2 |
| T3 | Malta business buys AWS subscription (US supplier) | Reverse charge: Malta business self-assesses 18% output + input VAT | Step 4.4 |
| T4 | Spanish business employee stays in Amsterdam hotel | Dutch VAT charged by hotel at the 9% accommodation rate (TEDB); no reverse charge; expense on books unless reclaimed under Directive 2008/9/EC | Step 3.6 |
| T5 | Polish e-commerce seller, established only in Poland, EUR 15,000 B2C sales of goods shipped to other EU countries in 2026 | Threshold exceeded: destination rates from the sale that crossed EUR 10,000; use OSS or register in each destination country | Step 6.1 |
| T6 | Slovak business supplies standard-rated goods to Czech business, invalid VAT number on VIES | Do NOT zero-rate; charge Slovak standard rate (23%) | Step 1.2 |
| T7 | Romanian business, standard rate question | 21% standard rate (increased from 19% on 1 August 2025) | Step 2.2 |
| T8 | Swedish grocer, sale of food on 15 May 2026 | 6% (food moved from 12% to 6% on 1 April 2026) | Step 2.2 |
| T9 | German business sells goods to a French customer and issues the invoice on 20 November 2026 for goods shipped on 3 October 2026 | Late: the invoice was due by 15 November 2026 (Article 222); VAT on the supply became chargeable on 15 November (Article 67) | Step 1.3 |

## Contribution Notes

**Contribution Notes**

| Area | Status |
| --- | --- |
| Core Directive rules | T1 -- sourced from the EUR-Lex consolidated text of 14 April 2025 |
| 2026 rate table | T1 -- read from the Commission TEDB web service on 30 October 2026 (situation on 1 January and 30 October 2026); Ireland 4.8% from Revenue |
| OSS / IOSS detail | T2 -- core return periods covered; detailed country implementation in country skills |
| ViDA timetable | T1 -- from Directive 2025/516 Article 6 and the amending regulations |
| Intrastat thresholds | T3 -- not covered; varies by country; add to country skills |
| SAF-T / e-invoicing mandates | T3 -- national mandates not covered; varies significantly by country |
| VAT groups | T3 -- not covered; varies by country (Article 11 option) |
| Capital goods adjustment period | T3 -- varies by country; covered in country skills |

**Practitioner review required for:** rate table accuracy (verify against EC TEDB and the country skill), any T2 rules before advising clients.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Council Directive 2006/112/EC, consolidated text of 14 April 2025 (Articles 2, 6, 14a, 17a, 20, 31-59c, 66-69, 94, 96-98, 105a, 138, 143, 168, 176, 178, 194, 196, 199a, 206, 211, 222, 226, 250-252, 262-264, 284, 288, 288a, 358-369zb) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02006L0112-20250414 | 2026-10-30 |
| Council Implementing Regulation (EU) No 282/2011, consolidated text of 14 April 2025 (Articles 18, 45a) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02011R0282-20250414 | 2026-10-30 |
| Council Directive (EU) 2025/516 (ViDA), Articles 1-7 | https://eur-lex.europa.eu/eli/dir/2025/516/oj/eng | 2026-10-30 |
| Council Regulation (EU) 2025/517 (ViDA administrative cooperation), Article 6 | https://eur-lex.europa.eu/eli/reg/2025/517/oj/eng | 2026-10-30 |
| Council Implementing Regulation (EU) 2025/518 (ViDA implementing rules), Article 3 | https://eur-lex.europa.eu/eli/reg_impl/2025/518/oj/eng | 2026-10-30 |
| Council Directive (EU) 2025/1539 (import VAT on distance sales), Articles 1-2 | https://eur-lex.europa.eu/eli/dir/2025/1539/oj/eng | 2026-10-30 |
| Council Directive (EU) 2020/285 (SME scheme), Article 3 | https://eur-lex.europa.eu/eli/dir/2020/285/oj/eng | 2026-10-30 |
| Council Directive (EU) 2022/542 (VAT rates), Article 3 | https://eur-lex.europa.eu/eli/dir/2022/542/oj/eng | 2026-10-30 |
| Agreement on the withdrawal of the United Kingdom from the EU (OJ L 29, 31.1.2020), Article 126 and Protocol on Ireland/Northern Ireland, Article 8 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12020W/TXT | 2026-10-30 |
| Council Directive 2008/9/EC (refunds to EU businesses), Article 15 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32008L0009 | 2026-10-30 |
| European Commission, Taxes in Europe Database (TEDB) VAT rates web service, situation on 1 January 2026 and 30 October 2026 (rate table; dated 2026 changes) | https://ec.europa.eu/taxation_customs/tedb/ | 2026-10-30 |
| European Commission, VAT rates (secondary guidance on the rate framework) | https://taxation-customs.ec.europa.eu/taxation/vat/vat-directive/vat-rates_en | 2026-10-30 |
| Irish Revenue, Current VAT rates (livestock rate 4.8% from 1 January 2026) | https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx | 2026-10-30 |

Not yet confirmed: each country's domestic zero rates (the old table showed "Yes" for every country; TEDB lists them per product, so the column was replaced by the parking-rate column); France's other 2026 changes in TEDB (energy rates); whether any member state extends its Article 199a reverse charge beyond 31 December 2026 (a Commission proposal to extend Article 199a was not read in the Official Journal); national e-invoicing and SAF-T start dates; Intrastat thresholds.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
