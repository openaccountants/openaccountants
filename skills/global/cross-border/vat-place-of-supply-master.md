---
name: vat-place-of-supply-master
description: "The definitive place-of-supply reference for cross-border VAT on services and goods. Use when the user asks about: place of supply, where is VAT due, which country's VAT, Art 44, Art 45, B2B place of supply, B2C place of supply, immovable property VAT, transport VAT, electronically supplied services place of supply, distance selling, chain transactions, triangulation, OSS decision tree, IOSS, intra-EU supply, import VAT, Art 47, Art 48, Art 53, Art 55, Art 56, Art 58, Art 31, Art 32, Art 33, Art 36a, US sales tax nexus, Australian GST on imports, India OIDAR, Japan consumption tax, freelancer cross-border VAT, \"where do I charge VAT\", or any question about determining the correct country for VAT/GST on a cross-border transaction."
version: 1.2
jurisdiction: INTL
tax_year: 2026
last_updated: 2026-11-27
source_checked: 2026-11-27
type: situation-rules
category: cross-border
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# VAT Place Of Supply Master

## Scope

Determine the country of a cross-border supply of goods or services, then separately determine exemption, rate, the person liable and the reporting route. This is the EU 2026 framework with bounded US, Australian, Indian and Japanese comparisons. It covers freelancers, taxable and non-taxable recipients, goods sellers, electronic platforms and relevant fixed establishments. It does not prepare a national return, resolve every state's US sales tax or decide a disputed establishment without evidence.

The primary legislation is Council Directive 2006/112/EC, especially Articles 31–61, with Implementing Regulation 282/2011. Contributor: OpenAccountants. This is a place-of-supply method, not professional approval.

Use `eu-reverse-charge.md`, `eu-oss-digital.md`, `non-eu-export-services.md` and `cross-border-vat-gst.md` with the relevant national overlay. EU place rules do not automatically establish liability under another country's law.

> **Disclaimer:** This skill provides general guidance on VAT/GST place-of-supply rules. These rules are complex, jurisdiction-specific, and subject to change. Consult a qualified indirect tax advisor before taking positions on VAT obligations.

### Quick reference

| Supply | Place, rate or threshold and conditions | Official source |
|---|---|---|
| Ordinary B2B service | Article 44: receiving business establishment, or receiving fixed establishment; Article 196 customer liability requires a supplier not established there for this supply | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Ordinary B2C service | Article 45 supplier establishment, after checking all special rules | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Consumer TBE / qualifying intra-EU distance goods | Destination, subject to the fully conditioned EUR 10,000 net combined exception in Article 59c | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| OSS / IOSS | Optional reporting schemes, not an obligation to register for a particular scheme merely because destination VAT applies | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en |
| Short-term transport hire | Up to 30 days, or 90 days for vessels (in words on the page): continuous possession/use; actual disposal place, Article 56 | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

## Ask the client first

1. What exactly is supplied: goods, admission, a human service, automated content, transport, property-related work or a bundle? Obtain the contract and invoice.
2. Where are the business and fixed establishments of supplier and recipient, and which actually provide/receive the supply? What are the goods' dispatch, installation and arrival locations?
3. What is the recipient's taxable/registration status and actual business or private use? Gather VIES/registration evidence and permitted alternative evidence; a VAT number is not the entire status test.
4. What are the transaction dates, relevant national exemptions, SME eligibility, elections, platform role and rate classification?
5. For Article 59c, obtain current and preceding calendar-year combined qualifying net turnover, every establishment, dispatch origin and destination, and any destination election.
6. For imports, obtain intrinsic consignment value, excise status, importer/declarant, IOSS use/intermediary, customs classification and any preferential treatment.
7. For non-EU comparisons, obtain the actual state/country rules, registration and exemption facts before concluding that a business buyer reverse-charges.

If an essential fact is unknown, stop the affected conclusion, identify the missing evidence and present conditional outcomes. Do not invent an establishment, exemption, rate or filing instruction.

## The method, step by step

Identify the supply and relevant establishments; test special place rules before the general rule; determine exemption and local rate; identify the liable person; then choose an eligible reporting route and retain the evidence. The following sections retain the original services, goods, OSS/IOSS, comparison and freelancer routes.

### Section 1: General Rules for Services

#### Article 44  -  B2B General Rule

A taxable person acting as such includes a business whose status is established under Regulation Articles 17–19; it is not limited to someone already holding a VAT number. Article 43 also treats a VAT-identified non-taxable legal person as taxable for these place rules. A service acquired exclusively for private use follows the non-taxable-person rule. VIES is an important EU evidence route; a pending number can be supported by other proof and reasonable verification under Article 18. For a non-EU customer obtain the prescribed certificate, registration or other business evidence and verify it.

Place is the customer's business establishment, unless the service is supplied to a fixed establishment elsewhere; failing those, permanent address/usual residence. For an ordinary taxable Article 44 service, Article 196 shifts liability to the taxable recipient or VAT-identified non-taxable legal person when the supplier is not established in that member state for the supply, including the Article 192a intervening-establishment test. It can include a non-EU supplier. Domestic or exempt supplies need their own treatment. Where the supplier’s business is in the tax state, the non-intervention exception cannot be used (Regulation Article 54). For a fixed establishment, assess the actual human/technical resources used in fulfilment; mere administrative support is not intervention, and a local VAT number on the invoice creates a rebuttable intervention presumption (Regulation Article 53). Invoice without supplier VAT only after establishing liability: this is not universal zero-rating. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; Regulation Articles 10–13a, 17–24: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### Article 45  -  B2C General Rule

For a non-taxable recipient, place is the supplier's business establishment or fixed establishment from which the service is supplied, then permanent address/usual residence. If taxable and supplier-liable, apply that country's VAT, subject to national registration and exemptions. A private individual is an example, not the complete class of non-taxable recipients. First check Section 2. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### Quick Reference

| Scenario | Place of Supply | Who Accounts for VAT | Official source |
|---|---|---|---|
| B2B general service | Receiving establishment under Article 44 | Customer under Article 196 only when its conditions apply; otherwise establish liability separately | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2C general service | Supplying establishment under Article 45 | Normally supplier, subject to exemption and specific liable-person rules | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

### Section 2: Special Rules for Services

These override Articles 44/45 where their conditions apply. A place conclusion alone does not determine registration, exemption or who pays.

#### 2.1 Immovable Property  -  Article 47

Place is the property location for sufficiently directly connected services: valuation, estate agency, specified property legal work, construction, accommodation, property management and architectural plans for a particular plot. General legal advice or plans not tied to a plot do not qualify merely because property is mentioned. Regulation Article 31a supplies inclusions and exclusions. A German architect designing a specified Portuguese building for an Irish customer has Portuguese place; check Portuguese exemption/liability and national Article 194 reverse charge before demanding supplier registration or supplier-charged VAT. Remote work does not itself displace Article 47. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### 2.2 Passenger Transport  -  Article 48

B2B and B2C place follows the actual route in proportion to distances. For a bus from Belgium through Luxembourg to Germany, allocate the service to those territories by distance; then apply each relevant national exemption and rate. Do not infer VAT is necessarily charged in all three. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 2.3 Goods Transport (B2C only)  -  Articles 49–51

Ordinary B2B goods transport follows Article 44. B2C transport other than intra-Community transport follows the actual route proportionately under Article 49. B2C intra-Community transport starts at the departure place under Article 50; Article 51 requires departure and arrival in different member states. The former destination-country instruction was wrong. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 2.4 Cultural, Artistic, Sporting, Scientific, Educational, Entertainment Events  -  Articles 53–54

| Scenario | Article | Place of Supply | Official source |
|---|---|---|---|
| B2B physical admission and ancillary admission services | 53 | Where the event takes place | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2B virtual attendance | 44 | Receiving business establishment; Article 53 expressly excludes virtual attendance | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2C physical activities and ancillary services, including organisers | 54 | Where actually carried out | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2C activities streamed or otherwise virtually available | 54 | Customer establishment, permanent address or usual residence | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2B organising, production or sponsorship rather than admission | 44, subject to other applicable special rules | Receiving establishment | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

Admission concerns the right to attend, including qualifying seminars; advance registration and payment do not themselves turn it into an Article 44 service. ECJ case C-647/17 (*Srf konsulterna*), ruling held the professional five-day course fell within Article 53. The old statement had reversed that result. Official judgment ruling: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62017CA0647; Regulation Articles 32–33: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### 2.5 Restaurant and Catering Services  -  Articles 55/57

B2B and B2C ordinary restaurant/catering place is where physically carried out under Article 55. On board a ship, aircraft or train during the passenger-transport section effected within the Community, Article 57 instead uses that section's departure point. The qualifying section has no stopover outside the Community between its first scheduled EU embarkation (after any earlier outside stopover) and last scheduled EU disembarkation for those passengers (before any later outside stopover); treat the return leg separately. It is not every service aboard any transport. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 2.6 Short-Term Hire of Transport  -  Article 56

Short-term continuous possession/use means no more than 30 days, or 90 days for vessels (in words on the page); place is where actually put at the customer's disposal. Longer B2B hire normally follows Article 44. Longer B2C hire follows customer establishment/address/residence under Article 56(2), correcting the former supplier rule. For B2C pleasure boats, the disposal place applies if the supplier supplies from its business/fixed establishment there; otherwise the customer rule applies. Check the actual duration against the contract, extensions and consecutive contracts for the same means of transport; force majeure and the Regulation’s anti-abuse boundaries matter. Actual disposal means physical possession by the customer or its representative (Regulation Articles 38–40). Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### 2.7 Electronically Supplied Services, Telecoms, Broadcasting (B2C)  -  Articles 58/59c

Article 58 uses the consumer's establishment/address/residence for TBE. Automated SaaS, downloads, streaming, e-books, pre-recorded automated courses and hosting can be electronic services under Regulation Article 7/Annex I; internet delivery alone is insufficient. Human-led virtual education may instead be Article 54. B2B ordinarily follows Article 44, with a separate liability test. Before applying a consumer destination result, resolve customer-location evidence under Regulation Articles 24a–24f and any interface/deemed-supplier issue under Article 9a. If these facts are unresolved, the destination/liability outcome is non-usable. Check this point with one of our partner accountants. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

The EUR 10,000 exception is VAT-exclusive combined qualifying TBE and intra-EU distance goods, not a separate allowance for each. The supplier must be established/addressed/resident in only one member state; services go to non-taxable persons in other member states and qualifying goods dispatch from that sole state to another. Total must not exceed EUR 10,000 in the current **and preceding** calendar year. Equality qualifies; the full supply that crosses the threshold uses destination, not only its excess. A voluntary destination option lasts at least 2 calendar years (in words on the page). Non-EU and multi-member-state established suppliers cannot use this exception. These are place rules, not a blanket exemption or OSS registration trigger. Article 59c: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

Use eligible OSS optionally, or required local registrations, for taxable destination supplies. Also check the cross-border SME exemption where available; destination does not mean every supply must bear VAT. See `eu-oss-digital.md`. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en.

#### 2.8 "Listed Services" to Non-EU Consumers (B2C)  -  Article 59

For a non-taxable person established/addressed/resident outside the EU, Article 59 locates these at the customer: intellectual-property/copyright licensing; advertising; consulting, legal, accounting, engineering and similar services; data processing/information; obligations to refrain from relevant activities/rights; banking, financial and insurance transactions except safe-deposit hire; staff supply; movable tangible-property hire except transport; and gas/electricity/heating/cooling-network access, transmission/distribution and directly linked services. TBE uses Article 58, not the former erroneous Article 59 list. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

A non-listed personal service does not automatically default to Article 45: first test property, activities, transport, catering and other special rules. Cleaning identified property can be Article 47; physical yoga instruction can be Article 54. Article 59a permits national effective-use-and-enjoyment adjustments for specified services to avoid double/non-taxation or distortion; check actual national implementation before the final result. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

### Section 3: Rules for Goods

#### 3.1 Domestic Supply  -  No Transport (Article 31)

Place is where goods are located when supplied. A German shop's walk-in sale of goods located there has German place; apply the actual product/exemption/registration rules. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 3.2 Goods Dispatched or Transported (Article 32)

Ordinary place is where dispatch/transport to the customer begins: a German warehouse dispatching to a German customer has German place. Distance sales, installation and other specific rules can override this. When dispatch begins outside the EU, Article 32's second paragraph places the designated importer's supply and subsequent supplies in the import member state. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 3.3 Intra-EU Distance Selling (Articles 14(4)/33)

Qualifying supplier-dispatched/facilitated goods to the specified non-taxable or acquisition-exempt recipients in another member state are normally located where transport ends. Mere absence of a VAT number is not the statutory recipient test. Exclude new means of transport and supplier-installed/assembled goods; check Article 35 margin-scheme exclusions and electronic-interface deemed supplies under Articles 14a/36b. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

Apply the fully conditioned net combined EUR 10,000 exception in Section 2.7; otherwise destination applies from the crossing supply. Union OSS is an optional report route, with local registration an alternative. Directive Articles 33/59c and Commission overview: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en.

#### 3.4 Imports from Outside the EU (Articles 30/60–61)

Ordinary import place is the member state of entry under Article 60. For the specified suspensive customs arrangements Article 61 instead uses the state where the arrangement ceases. Member states designate the liable importer/person under Article 201. Article 211 permits qualifying postponed return accounting: payment to customs at entry is not universal. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

For eligible distance sales of imported goods in consignments of intrinsic value no more than EUR 150, excluding excise products, optional IOSS collects destination VAT on the sale when payment is accepted; the import is VAT-exempt under Article 143(1)(ca) only when the applicable supplier/intermediary IOSS number is provided to the competent customs office by lodging the import declaration at the latest. It is not merely an import with VAT paid at the border. Non-EU suppliers normally need an EU intermediary, subject to the Article 369m mutual-assistance condition. Customs duty remains separate. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1, Articles 14(4), 33, 143(1)(ca), 369l–369n.

#### 3.5 Installation or Assembly (Article 36)

Place is where goods are installed/assembled by or for the supplier, with or without a trial run. German machinery shipped and installed in a French factory has French place; then check French liability/registration and rate. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 3.6 Chain Transactions (Article 36a)

For successive supplies A → B → C of the same goods with direct transport from the first supplier to the final customer across member states, attribute transport to the supply **to** the intermediary operator B, where B (not the first supplier) transports or arranges transport. If B communicates the dispatch member state's VAT number to A, attribute it to B's onward supply instead. Article 36a excludes Article 14a deemed-interface transactions. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

Only the attributed moving supply can qualify as the intra-Community exempt supply under Article 138; attribution itself grants no exemption. Article 139 excludes the relevant SME-exempt suppliers, acquisition-exempt recipients and specified margin/auction arrangements from that general exemption. Test transport, recipient VAT identification outside dispatch state, recap conditions and evidence. Other chain supplies require their own location/treatment; avoid assuming every residual supply is simply taxable domestic. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1, Articles 36a/138–139.

**Simplified triangulation (Article 141):** retain A (MS1) → B (MS2) → C (MS3), but three countries alone do not suffice. B must not be established in MS3 and must be identified in another state; its acquisition is for a subsequent MS3 supply; goods travel directly from a state other than B's identification state to C; C is identified in MS3 and designated liable under Article 197. Check the Article 197 compliant invoice, any national tax-representative derogation, and Article 42/265 recap conditions. The qualifying invoice carries "Reverse charge" and C accounts for tax. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1, Articles 42, 141, 197, 226(11a), 265.

### Section 4: OSS / IOSS Decision Tree

#### When to register for One-Stop Shop

1. Identify actual B2C supplies and their place first. If no eligible cross-border goods or service supply exists, these schemes are not the reporting route. All eligible services may qualify, not only digital ones.
2. For qualifying TBE/intra-EU distance goods, test **all** Article 59c facts in Section 2.7. If the exception applies and no destination election is made, use origin treatment. If it does not apply, destination follows; check exemptions and the liable person.
3. Choose an eligible optional scheme or comply through local registrations. An EU supplier normally uses Union OSS for eligible B2C services in states where it is not established and eligible intra-EU distance goods. A non-EU supplier can use non-Union OSS for eligible EU B2C services, or Union OSS for qualifying intra-EU distance goods. A non-EU supplier has no Article 59c benefit.
4. For eligible imported distance goods, test intrinsic consignment value, excise exclusion, platform role and intermediary. Choose IOSS or the applicable import/local route. A consignment above the IOSS ceiling is outside that scheme, not exempt from VAT.

Sources: Directive Articles 358a–369x https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; Commission scheme overview https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en. Do not apply the guides explicitly for 2027 to a 2026 transaction.

#### OSS Comparison Table

| Scheme | Who | What | Filing | Official source |
|---|---|---|---|---|
| Union OSS | Eligible EU or non-EU sellers; service-establishment restrictions apply | Qualifying intra-EU distance goods; B2C services where not established in consumption state; specified deemed domestic goods | Quarterly; competent identification state | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Non-Union OSS | Supplier with neither business nor fixed establishment in EU | All eligible EU B2C services | Quarterly; chosen identification state | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| IOSS | Eligible EU/non-EU sellers, including required intermediary arrangements | Imported distance goods in intrinsic consignments ≤EUR 150; no excise products | Monthly; return/payment by end of following month (in words on the page), even a nil period | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

For quarterly OSS, return/payment is due by the end of the following month; the competent national portal issues registration and return/payment references. Use the national overlay and `eu-oss-digital.md` for fields, correction and record rules. Source: https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en; Directive Articles 364/367/369f/369i/369s/369v https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### Customs duty from 1 July 2026: separate from IOSS VAT

Regulation 2026/382 removed the EUR 150 customs-duty relief from 1 July 2026. Its temporary EUR 3 per **item**, for qualifying intrinsic consignments ≤EUR 150, applies from 1 July 2026 until 1 July 2028: IOSS import-VAT-exempt goods or goods within the amended postal-consignment definition. Regulation 2026/1022 broadened that definition to eligible distance-sale goods, excluding IOSS goods already in the first limb and goods benefiting from preferential measures, including customs-union agreements. Thus it is not restricted to traditional postal carriers. Non-IOSS preferential treatment must be established under customs law; IOSS goods remain subject to the simplified duty. Sources: Regulation 2026/382 Articles 1–4 https://publications.europa.eu/resource/cellar/2ae65d0b-0c6b-11f1-8870-01aa75ed71a1.0006.03/DOC_1; Regulation 2026/1022 Articles 1(1), 2 https://publications.europa.eu/resource/cellar/3b9f822b-74e8-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1.

An item can comprise goods sharing tariff classification, description and origin where the declaration requires origin; EUR 3 is neither universally per physical article nor per parcel. Declaration lines and dataset matter. IOSS remains optional VAT collection, not a customs-duty exemption. When the seller recovers duty from the customer it forms part of the sale consideration/VAT base; the valid IOSS import is VAT-exempt. For special-arrangement/standard imports, customs duty enters the import VAT base. Sources: Directive Articles 73/78 (sale consideration) and 85/86 (import base), https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; Regulation 2026/1022 Article 1(1)(b) https://publications.europa.eu/resource/cellar/3b9f822b-74e8-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1.

### Section 5: Non-EU Rules Comparison

#### 5.1 US Sales Tax Nexus

| Aspect | US Rule | Official source |
|---|---|---|
| Tax type / sourcing | State and local sales/use taxes; establish nexus, product taxability, sourcing, exemption and marketplace responsibility separately. There is no single EU-style national VAT registration | https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates; https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm |
| Physical nexus | Actual state connections matter. South Dakota's examples include property, sales staff and deliveries in company vehicles; this is not an exhaustive all-state test | https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates |
| Economic nexus (*South Dakota v. Wayfair*, 2018) | Do not reuse a universal USD 100,000/200-transactions rule. South Dakota removed its 200-transaction limb from 1 July 2023; its current remote-seller rule is **more than** USD 100,000 gross sales in the current or preceding calendar year. Section 10-64-2.1 allows registration/remittance to start on the first day of the first month beginning at least thirty days after the criteria are met. Other states have their own tests | https://www.sdlegislature.gov/api/Statutes/10-64.html?all=true; https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates |
| Digital services / CA | California electronic-only data/software/downloads generally are not taxable; a tangible backup/printed copy can change the sale’s treatment; for a nontaxable electronically transferred prewritten program, documentation/manuals supplied without additional charge do not themselves make the program taxable (Regulation 1502(f)(1)(D)) | https://cdtfa.ca.gov/lawguides/vol1/sutr/1502.html; https://cdtfa.ca.gov/formspubs/pub109/nontaxable-sales.htm |
| Digital services / GA | Georgia Rule 560-12-2-.118(5)(c) excludes SaaS. Distinguish SaaS from specified digital goods: a download-and-retain right can be taxable even when continued payment is required; do not treat every subscription as excluded | https://rules.sos.ga.gov/gac/560-12-2-.118 |
| Digital services / MO | Missouri 12 CSR 10-109.050(2)(C)/(3)(I) excludes defined SaaS, which does not give the purchaser use of specifically identified tangible property; the provider pays sales/use tax on tangible property purchased or used in Missouri | https://www.sos.mo.gov/cmsimages/adrules/csr/current/12csr/12c10-109.pdf |
| Buyer accounting | Purchaser use-tax self-assessment exists. California requires qualifying taxable purchases without seller collection to be reported; this is not the EU credit-invoice reverse-charge mechanism | https://cdtfa.ca.gov/lawguides/vol1/sutl/6202.html; https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm |
| Key difference from EU | Build the actual state-by-state nexus/taxability/sourcing register. Tax automation such as Stripe Tax, TaxJar or Avalara does not establish the legal result or replace official state rules | https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates; https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm |

A nationwide SaaS-taxability count and a universal remote-seller threshold are not supplied. Use each relevant state’s current rule.

#### 5.2 Australian GST on Imports - comparison on hold

**Non-usable comparison:** Australian registration/turnover, consumer digital supplies, low-value imports, platform responsibility, rates and Divisions 83/84 reverse charge require the current Australian Guide. This Guide supplies no Australian tax or registration conclusion. Check this point with one of our partner accountants.

#### 5.3 India OIDAR - comparison on hold

**Non-usable comparison:** OIDAR definition and recipient status, place/liability, rate, simplified registration, B2B imports, equalisation levy and software-export/LUT/receipt conditions require the current Indian Guide. The historical and current Indian rules previously printed here are not usable instructions. Check this point with one of our partner accountants.

#### 5.4 Japan Consumption Tax on Digital Services - comparison on hold

**Non-usable comparison:** Electronic-service classification, supplier/recipient liability, exemptions and turnover tests, rates, specified-platform rules and qualified invoices/input credits require the current Japanese Guide. This Guide supplies no Japanese tax or registration conclusion. Check this point with one of our partner accountants.

#### Comparison Summary

| Feature | EU | US | Australia | India | Japan |
|---|---|---|---|---|---|
| Place and liability | Sections 1–3: test place separately from exemption/liability | Section 5.1: actual state nexus, sourcing and product rules | Non-usable; see 5.2 | Non-usable; see 5.3 | Non-usable; see 5.4 |
| Registration and reporting | Section 4: eligible optional OSS/IOSS or local route | State-specific assessment; no national threshold inferred | Check this point with one of our partner accountants. | Check this point with one of our partner accountants. | Check this point with one of our partner accountants. |

### Section 6: Practical Decision Flowchart for Freelancers

"I'm in Country A, my client is in Country B, and I'm providing [service type]. What VAT applies?"

#### Step 1: Classify the Supply

Physical goods go to Goods Flow; services continue. Online ordering does not make a physical good an electronic service. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; Regulation Article 7 https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### Step 2: Identify the Customer

Determine taxable-person/legal-person status and actual use, not only VAT-number possession. Apply Regulation Articles 17–19 evidence, including permitted alternatives for pending IDs and non-EU recipients. Business use proceeds to Step 3; non-taxable/private use to Step 4. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### Step 3: B2B Service  -  Check Exceptions

| Question | If YES | If NO | Official source |
|---|---|---|---|
| Sufficient direct property connection? | Article 47 property place | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| Physical event admission? | Article 53 event place; virtual attendance excluded | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Short-term hire, up to 30 days / vessels 90 days (in words on the page)? | Article 56 actual disposal place | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Restaurant/catering? | Article 55 performed place or qualifying Article 57 onboard departure | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Passenger transport? | Article 48 route allocation | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| No specific rule? | Article 44 receiving-establishment place; then Article 196 or other national liability and exemption | Do not infer another country's reverse charge from EU law | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

#### Step 4: B2C Service  -  Check Exceptions

| Question | If YES | If NO | Official source |
|---|---|---|---|
| TBE/automated electronic service? | Article 58 customer place, with fully conditioned Article 59c exception | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| Sufficient direct property connection? | Article 47 property place | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 |
| Event/activity or ancillary service? | Article 54 physical place; streamed/virtual customer place | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Passenger/goods transport, catering, vehicle hire, intermediary or work on movable goods? | Apply Articles 46, 48–52, 54(2), 55–57 and Section 2 as appropriate; long-term consumer hire uses customer rule | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Consumer outside EU and Article 59 listed service? | Customer place; check national Article 59a adjustments | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| None applies? | Article 45 supplying-establishment place, then taxability and liability | Stop if facts insufficient | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

#### Goods Flow

| Question | If YES | If NO | Official source |
|---|---|---|---|
| Supplier installation/assembly? | Article 36 installation place; not ordinary distance selling | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Qualifying intra-EU consumer distance sale? | Article 33 destination, with fully conditioned Article 59c exception; optional Union OSS | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| Imported distance goods, intrinsic consignment ≤EUR 150 and no excise? | Optional eligible IOSS; otherwise applicable import/local route; customs duty separate | Continue | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/2ae65d0b-0c6b-11f1-8870-01aa75ed71a1.0006.03/DOC_1 |
| Standard domestic or B2B intra-EU goods? | Articles 31/32 and actual acquisition/exemption conditions; Article 138 is not automatic | Test chains, margin scheme, deemed platform and other applicable rules | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

#### Common Freelancer Scenarios

| You are in... | Client is in... | Service | Result and assumptions | Official source |
|---|---|---|---|---|
| Germany | France | Web development (B2B) | Ordinary business service to French establishment, German supplier not established there: Article 44/196, no German VAT; standard taxable French recipient self-assesses at 20%, with deduction separate | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://www.gesetze-im-internet.de/ustg_1980/__12.html; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000026950057/2026-01-21; https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 |
| Germany | France | Web development (B2C) | Bespoke human work, no special-rule facts: Article 45 Germany, standard taxable supplier charges 19%; do not classify by internet delivery alone | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Germany | France | SaaS subscription (B2C) | Article 58 France at standard 20% for this taxable SaaS, **unless** fully conditioned Article 59c origin exception applies; optional OSS/local route | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Malta | US | Consulting (B2B) | Ordinary service to US business establishment: Article 44 US place, no Malta VAT. Check US/state treatment separately | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates |
| Malta | US | Pre-recorded online course (B2C) | Automated ESS: Article 58 customer place outside EU, not Article 59; check actual location/use-enjoyment and US nexus/taxability | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates |
| UK | Germany | Design services (B2B) | Ordinary general-rule service to German business, no property/other exception: outside UK VAT; Article 44/196 German recipient liability if UK supplier non-established there, rate/exemption checked locally | https://www.legislation.gov.uk/ukpga/1994/23/section/7A; https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| India | Australia | Software dev (B2B) | **Non-usable outcome:** original direction and service retained; export status, LUT/receipt conditions and Australian recipient liability await both country Guides. Check this point with one of our partner accountants. | Sections 5.2–5.3; no local-law conclusion |
| US | EU consumers | SaaS product (B2C) | Taxable automated service: Article 58 destination, no Article 59c benefit; optional non-Union OSS or local registration, platform/exemption analysis first | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en |
| France | Switzerland | Architecture for property in France | Specified French property, Article 47 France; standard taxable architecture 20% if supplier-liable, regardless of Swiss customer address. Check actual supplier establishment/national liability | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |

## Boundary and exception table

### EC1  -  Bespoke software vs. SaaS (ESS classification)

**Situation:** A developer builds custom software for a specific B2C client. **Resolution:** Significant human development is not automatically an electronic service; apply Regulation Article 7's automation/minimal-human test to the actual supply. Ordinary bespoke services follow Article 45 B2C/Article 44 B2B absent another exception; automated SaaS normally Article 58 B2C. Escalate uncertain customisation. Sources: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

### EC2  -  Remote worker creating PE risk

**Situation:** A UK freelancer works from Spain for 8 months serving UK clients. **Resolution:** That duration is an illustrative fact, not a VAT establishment threshold. Regulation Articles 10–13 test central administration, actual permanence/resources, address and residence. Determine whether a Spanish supplying establishment affects Article 45; Article 44 still tests the customer's receiving establishment, while supplier establishment can change liability. Assess residence/permanent-establishment tax risks separately; VAT fixed establishment and income-tax PE are not interchangeable. Sources: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

### EC3  -  Mixed digital and live service bundle

**Situation:** Pre-recorded videos plus live weekly coaching calls to an EU consumer. **Resolution:** Automated videos and human-led virtual activities are classified under different rules (Sections 2.4/2.7). **Non-usable outcome:** this Guide does not decide whether the videos and live weekly calls form one supply, or which element determines its treatment. Preserve the contract, pricing and promised deliverables. Check this point with one of our partner accountants. Sources: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1

### EC4  -  Chain transaction with unknown intermediary role

**Situation:** A → B → C, direct Poland-to-Portugal shipment, B's role unknown. **Resolution:** Stop exemption/location conclusions until transport responsibility, contracts, Incoterms and VAT-number communication are established. Article 36a attribution and Article 138 exemption are separate tests; wrong attribution can create competing tax claims. Obtain review before invoicing/filing. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

## Worked cases

### Test 1  -  B2B consulting, Germany to France

**Input:** German consultant invoices a French company with a valid FR VAT number EUR 5,000 net for strategy consulting, received in France; no French supplier establishment or exemption. **Expected:** Articles 44/196 France, no German VAT; French customer accounts, deduction separately. The German supplier includes the qualifying non-exempt Article 262(1)(c) service on the recap statement; use the German return/statement overlay. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

### Test 2  -  B2C yoga class (non-listed service), Malta to US consumer

**Input:** Private in-person yoga session in Malta for a US tourist, EUR 100 **net**; taxable standard-rated activity, no sports/education/other exemption. **Expected:** Physical sporting/educational activity can fall under Article 54 rather than the old assumed Article 45; both locate these stated facts in Malta. At the standard 18%, VAT EUR 18 and gross EUR 118 (derived). If the original EUR 100 were gross, VAT is EUR 15.25 and net EUR 84.75 (derived, rounded). Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm.

### Test 3  -  B2C SaaS, US company to French consumer

**Input:** Taxable automated SaaS subscription EUR 20 **net** per month, French consumer, US supplier with no EU establishment and no deemed platform. **Expected:** Article 58 France; no Article 59c benefit. Non-Union OSS is optional; local compliance is the alternative. Standard French 20% gives VAT EUR 4, gross EUR 24 (derived). If EUR 20 is gross, VAT EUR 3.33 and net EUR 16.67 (derived, rounded). Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm.

```oa-check
name: US SaaS to French consumer, net and gross alternatives
inputs:
  net: 20
  rate: 0.20
  gross_alternative: 20
steps:
  vat: round(net * rate, 2)
  gross: net + vat
  included_vat: round(gross_alternative * rate / (1 + rate), 2)
  alternative_net: gross_alternative - included_vat
expected:
  vat: 4
  gross: 24
  included_vat: 3.33
  alternative_net: 16.67
```

### Test 4  -  Architect, property in another country

**Input:** Italian architect designs an identified Greek villa for a German business client, EUR 15,000 net. **Expected:** Article 47 Greece. Article 196 does not itself decide liability; check Greek Article 194 implementation, recipient qualifications, exemptions and supplier establishment before requiring supplier registration. No Greek rate or return box is asserted here. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

### Test 5  -  Distance selling, below threshold

**Input:** Seller established only in Spain dispatches qualifying handmade goods from Spain to consumers in 5 other EU countries. Current net qualifying distance goods EUR 8,000; prior year EUR 7,000; no other qualifying TBE, destination election or special exclusion. **Expected:** Article 59c condition met in both years: Spain origin treatment permitted, with actual Spanish product/exemption rules. Current headroom EUR 2,000 and prior-year headroom EUR 3,000 (derived). Destination election and optional OSS are alternatives, not a mandatory scheme. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

### Test 6  -  Distance selling, above threshold

**Input:** Same seller now has EUR 15,000 combined qualifying net current-year turnover. **Expected:** Article 59c no longer applies from the supply that crossed EUR 10,000. EUR 5,000 excess is derived turnover arithmetic, **not** a tax base for retroactively taxing every sale. Identify the crossing supply; full crossing and later supplies use destination, then optional Union OSS or local compliance. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

For a concrete crossing within that original scenario, assume EUR 9,800 before a EUR 500 net sale to France, no exemption and standard-rated goods at 20%: total EUR 10,300; the entire EUR 500 sale bears French VAT EUR 100, gross EUR 600 (derived). Earlier qualifying origin supplies remain origin. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm.

```oa-check
name: Spanish distance seller, headroom and full crossing supply
inputs:
  threshold: 10000
  prior_year: 7000
  earlier_total: 8000
  before_crossing: 9800
  sale: 500
  france_rate: 0.20
  later_total: 15000
steps:
  current_headroom: threshold - earlier_total
  prior_headroom: threshold - prior_year
  after_crossing: before_crossing + sale
  excess_at_crossing: max(0, after_crossing - threshold)
  destination_vat: sale * france_rate
  gross_crossing: sale + destination_vat
  later_excess: later_total - threshold
expected:
  current_headroom: 2000
  prior_headroom: 3000
  after_crossing: 10300
  excess_at_crossing: 300
  destination_vat: 100
  gross_crossing: 600
  later_excess: 5000
```

## When to refuse or refer

The original PROHIBITIONS remain, with their legal boundaries:

1. Never default to Article 44/45 without checking special place rules.
2. Never assume foreign B2C means outside EU VAT. Article 58/54 and other exceptions also matter; Article 59 is not the only consumer destination rule.
3. Never ignore Article 47 where the sufficiently direct property test is met; establish liability separately.
4. Never apply Article 59c's EUR 10,000 benefit to a non-EU supplier. Destination still requires taxability, exemption and platform analysis.
5. Never confuse outside scope, zero rate, exemption with deduction and exemption without deduction. EU law calls Article 138 relief an exemption; deduction can survive under Article 169. Do not say every exempt supply loses input recovery.
6. Never skip recipient VAT-ID/transport/recap verification for the relevant intra-EU goods exemption. For services, preserve permitted Article 18 alternative evidence; lack of a VIES hit is not automatic domestic VAT.
7. Never apply EU rules automatically to US, Australia, India or Japan. Use the actual national/state overlay and refuse an unsupported local rate, registration or reverse-charge conclusion.

Sources for EU prohibitions: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1. National boundaries: Section 5's primary sources. For unresolved composite classification, establishment, triangulation conditions, exemptions/SME relief, national use-and-enjoyment adjustments, customs preferences or national filing details, the affected outcome is non-usable. Preserve the inputs. Check this point with one of our partner accountants.

## Filing and payment

This is a place/liability reference, not a substitute national return. Hand off the classified supply, establishments, date, net consideration, rate/exemption evidence, liable person, input-credit restrictions and chosen scheme to the current national skill. For an Article 196 supplier, preserve invoice "Reverse charge" and relevant recap obligations. For OSS/IOSS, use the competent official portal, actual registration/return identifier, consumption-state/rate/taxable-value fields and issued payment reference; retain submission acknowledgment and confirm payment allocation. Do not invent a box number or claim submission without its receipt. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en.

## Completion checklist

- [ ] Supply, customer status/use and relevant establishments evidenced.
- [ ] Special rule tested before general place; rate/exemption and liability decided separately.
- [ ] Thresholds include periods, combined population, exclusions and any elections.
- [ ] Optional scheme distinguished from legal registration obligations.
- [ ] Non-EU/state conclusions supported by the actual overlay; unresolved figures excluded.
- [ ] Original scenario assumptions, gross/net amounts and crossing date recorded.
- [ ] National filing handoff and review evidence saved before action.

## Sources

Operative sections and their conditions were read, or applicable completed exact-source proof was reused, on the dates below. A successful download or a JavaScript challenge page is not a source read. APAC comparisons are explicitly non-usable; no new APAC research is claimed.

| Official source | Actual read scope | Read date |
|---|---|---|
| VAT Directive https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 | Read operative Articles 14/14a, 30–36b, 42–61, 73/78/85/86, 138/139/141/143(1)(ca), 169, 192a/193/194/196/197, 201/211/226/262, 358a/359/364/367/369a/369b/369f/369i/369l/369m/369n/369s/369v: definitions, conditions, exclusions and schemes | 2026-11-27 |
| Implementing Regulation https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 | Read operative Articles 7, 9a–13, 17–22, 24a/24b/24f, 31a–33, 38–40, 53–54: automation, establishment, evidence, property/admission/hire and supplier intervention. Unresolved location/interface facts remain held | 2026-11-27 |
| C-647/17 official ruling https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A62017CA0647 | Completed exact official ruling reused: five-day course, taxable attendees, advance registration/payment and Article 53; no fresh whole-judgment read claimed | 2026-11-27 applicability checked |
| Commission OSS https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en | Read eligibility/optional/all-supplies coverage, threshold dispatch origin, return/payment periods and field/reference guidance; statute controls conditions | 2026-11-27 |
| EU customs https://publications.europa.eu/resource/cellar/2ae65d0b-0c6b-11f1-8870-01aa75ed71a1.0006.03/DOC_1; https://publications.europa.eu/resource/cellar/3b9f822b-74e8-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1 | Read 2026/382 Articles 1–4 and 2026/1022 Article 1 amendments to postal/item definitions and Article 2 commencement; VAT-base support is Directive Articles 73/78/85/86 | 2026-11-27 |
| German rate https://www.gesetze-im-internet.de/ustg_1980/__12.html | Completed exact §12(1) nineteen-per-cent proof reused for ordinary standard-rated services; reduced/exempt cases excluded | 2026-11-26; applicability checked 2026-11-27 |
| French rate https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000026950057/2026-01-21 | Completed exact CGI278 twenty-per-cent proof reused for stipulated metropolitan standard-rated supplies, excluding exemptions/reduced rates | 2026-11-27 reuse applicability checked |
| Maltese rate https://legislation.mt/getpdf/6ac352947b5e681a8405fbf4 | Completed exact Article19(1)–(2) eighteen-per-cent proof reused, subject to Eighth Schedule and exemptions; yoga example expressly stipulates standard-rated taxable activity | 2026-11-26; applicability checked 2026-11-27 |
| South Dakota https://www.sdlegislature.gov/api/Statutes/10-64.html?all=true; https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates | Read §§10-64-2/2.1 and DOR physical-presence/remote-seller FAQ: current/prior gross revenue, transaction-test removal and registration start | 2026-11-27 |
| California https://cdtfa.ca.gov/lawguides/vol1/sutr/1502.html; https://cdtfa.ca.gov/formspubs/pub109/nontaxable-sales.htm; https://cdtfa.ca.gov/lawguides/vol1/sutl/6202.html; https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm | Read Regulation1502(f)(1)(D), Publication109 electronic-transfer/physical-copy text, RTC6202(a) and business use-tax scope; documentation exception retained | 2026-11-27 |
| Georgia https://rules.sos.ga.gov/gac/560-12-2-.118 | Read official browser-rendered Rule560-12-2-.118 definitions, imposition, sourcing, exclusions; SaaS and download/retain boundary. Non-rendered script shell was not evidence | 2026-11-27 |
| Missouri https://www.sos.mo.gov/cmsimages/adrules/csr/current/12csr/12c10-109.pdf | Read 12CSR10-109.050(2)(C)/(3)(I): SaaS definition, identified-property exclusion and provider tax obligation | 2026-11-27 |
| UK https://www.legislation.gov.uk/ukpga/1994/23/section/7A; https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | Read VATA7A(1)–(5), HMRC741A1.4 and 6.1–6.4 for ordinary UK-to-Germany business design case, subject to special rules | 2026-11-27 |

**Not yet confirmed:** Non-usable holds, not calculation inputs: the original nationwide US SaaS/state counts; every Australian/Indian/Japanese comparison topic identified in Sections 5.2–5.4 (including the historical Indian blanket OIDAR rate); mixed video/live-coaching composite classification; disputed establishment, Greek/Portuguese national Article 194 conditions, national exemptions/SME relief and effective-use-and-enjoyment overrides, triangulation invoice/recap facts, customs preferences, every unestablished national return box and rate. The former EUR 2 handling-fee expectation and its proposed start date are not an enacted-fee instruction in this Guide. Preserve the transaction inputs and use the relevant current national Guide before acting. Check this point with one of our partner accountants.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. VAT rates, thresholds, and place-of-supply rules are subject to change. Always verify current rules with official sources and a qualified indirect tax advisor.

*Data reflects 2025–2026 rules. OpenAccountants  -  open-source accounting skills for AI  -  info@openaccountants.com*
