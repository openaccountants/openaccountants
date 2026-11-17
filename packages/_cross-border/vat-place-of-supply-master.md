---
name: vat-place-of-supply-master
description: "The definitive place-of-supply reference for cross-border VAT on services and goods. Use when the user asks about: place of supply, where is VAT due, which country's VAT, Art 44, Art 45, B2B place of supply, B2C place of supply, immovable property VAT, transport VAT, electronically supplied services place of supply, distance selling, chain transactions, triangulation, OSS decision tree, IOSS, intra-EU supply, import VAT, Art 47, Art 48, Art 53, Art 55, Art 56, Art 58, Art 31, Art 32, Art 33, Art 36a, US sales tax nexus, Australian GST on imports, India OIDAR, Japan consumption tax, freelancer cross-border VAT, \"where do I charge VAT\", or any question about determining the correct country for VAT/GST on a cross-border transaction."
version: 1.1
jurisdiction: INTL
tax_year: 2026
last_updated: 2026-11-14
source_checked: 2026-11-14
type: situation-rules
category: cross-border
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: cross-border
---

# VAT Place Of Supply Master

## Scope

Determine the country of a cross-border supply of goods or services, then separately determine exemption, rate, the person liable and the reporting route. This is the EU 2026 framework with bounded US, Australian, Indian and Japanese comparisons. It covers freelancers, taxable and non-taxable recipients, goods sellers, electronic platforms and relevant fixed establishments. It does not prepare a national return, resolve every state's US sales tax or decide a disputed establishment without evidence.

The primary legislation is Council Directive 2006/112/EC, especially Articles 31–61, with Council Implementing Regulation 282/2011. Contributor: OpenAccountants. Skill version 1.1; source review 14 November 2026. Working tags [T1], [T2] and [T3] identify known-fact rules, fact-sensitive issues and referral boundaries; they do not constitute professional approval.

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

#### Article 44  -  B2B General Rule [T1]

A taxable person acting as such includes a business whose status is established under Regulation Articles 17–19; it is not limited to someone already holding a VAT number. Article 43 also treats a VAT-identified non-taxable legal person as taxable for these place rules. A service acquired exclusively for private use follows the non-taxable-person rule. VIES is an important EU evidence route; a pending number can be supported by other proof and reasonable verification under Article 18. For a non-EU customer obtain the prescribed certificate, registration or other business evidence and verify it.

Place is the customer's business establishment, unless the service is supplied to a fixed establishment elsewhere; failing those, permanent address/usual residence. For an ordinary taxable Article 44 service, Article 196 shifts liability to the taxable recipient or VAT-identified non-taxable legal person when the supplier is not established in that member state for the supply, including the Article 192a intervening-establishment test. It can include a non-EU supplier. Domestic or exempt supplies need their own treatment. Invoice without supplier VAT only after establishing liability: this is not universal zero-rating. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; Regulation Articles 10–13a, 17–24: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### Article 45  -  B2C General Rule [T1]

For a non-taxable recipient, place is the supplier's business establishment or fixed establishment from which the service is supplied, then permanent address/usual residence. If taxable and supplier-liable, apply that country's VAT, subject to national registration and exemptions. A private individual is an example, not the complete class of non-taxable recipients. First check Section 2. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### Quick Reference

| Scenario | Place of Supply | Who Accounts for VAT | Official source |
|---|---|---|---|
| B2B general service | Receiving establishment under Article 44 | Customer under Article 196 only when its conditions apply; otherwise establish liability separately | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2C general service | Supplying establishment under Article 45 | Normally supplier, subject to exemption and specific liable-person rules | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

### Section 2: Special Rules for Services

These override Articles 44/45 where their conditions apply. A place conclusion alone does not determine registration, exemption or who pays.

#### 2.1 Immovable Property  -  Article 47 [T1]

Place is the property location for sufficiently directly connected services: valuation, estate agency, specified property legal work, construction, accommodation, property management and architectural plans for a particular plot. General legal advice or plans not tied to a plot do not qualify merely because property is mentioned. Regulation Article 31a supplies inclusions and exclusions. A German architect designing a specified Portuguese building for an Irish customer has Portuguese place; check Portuguese exemption/liability and national Article 194 reverse charge before demanding supplier registration or supplier-charged VAT. Remote work does not itself displace Article 47. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### 2.2 Passenger Transport  -  Article 48 [T1]

B2B and B2C place follows the actual route in proportion to distances. For a bus from Belgium through Luxembourg to Germany, allocate the service to those territories by distance; then apply each relevant national exemption and rate. Do not infer VAT is necessarily charged in all three. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 2.3 Goods Transport (B2C only)  -  Articles 49–51 [T2]

Ordinary B2B goods transport follows Article 44. B2C transport other than intra-Community transport follows the actual route proportionately under Article 49. B2C intra-Community transport starts at the departure place under Article 50; Article 51 requires departure and arrival in different member states. The former destination-country instruction was wrong. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 2.4 Cultural, Artistic, Sporting, Scientific, Educational, Entertainment Events  -  Articles 53–54 [T2]

| Scenario | Article | Place of Supply | Official source |
|---|---|---|---|
| B2B physical admission and ancillary admission services | 53 | Where the event takes place | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2B virtual attendance | 44 | Receiving business establishment; Article 53 expressly excludes virtual attendance | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2C physical activities and ancillary services, including organisers | 54 | Where actually carried out | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2C activities streamed or otherwise virtually available | 54 | Customer establishment, permanent address or usual residence | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| B2B organising, production or sponsorship rather than admission | 44, subject to other applicable special rules | Receiving establishment | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |

Admission concerns the right to attend, including qualifying seminars; advance registration, payment and active participation do not themselves turn it into an Article 44 service. ECJ case C-647/17 (*Srf konsulterna*), paragraphs 23–36 and ruling, held the professional five-day course fell within Article 53. The old statement had reversed that result. Judgment: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62017CJ0647; Regulation Articles 32–33: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### 2.5 Restaurant and Catering Services  -  Articles 55/57 [T1]

B2B and B2C ordinary restaurant/catering place is where physically carried out under Article 55. On board a ship, aircraft or train during the passenger-transport section effected within the Community, Article 57 instead uses that section's departure point; apply its defined departure/arrival and separate return-journey rules. It is not every service aboard any transport. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 2.6 Short-Term Hire of Transport  -  Article 56 [T1]

Short-term continuous possession/use means no more than 30 days, or 90 days for vessels (in words on the page); place is where actually put at the customer's disposal. Longer B2B hire normally follows Article 44. Longer B2C hire follows customer establishment/address/residence under Article 56(2), correcting the former supplier rule. For B2C pleasure boats, the disposal place applies if the supplier supplies from its business/fixed establishment there; otherwise the customer rule applies. Check actual contracts, extensions and successive hire under Regulation Articles 38–40. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

#### 2.7 Electronically Supplied Services, Telecoms, Broadcasting (B2C)  -  Articles 58/59c [T1]

Article 58 uses the consumer's establishment/address/residence for TBE. Automated SaaS, downloads, streaming, e-books, pre-recorded automated courses and hosting can be electronic services under Regulation Article 7/Annex I; internet delivery alone is insufficient. Human-led virtual education may instead be Article 54. B2B ordinarily follows Article 44, with a separate liability test. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1.

The EUR 10,000 exception is VAT-exclusive combined qualifying TBE and intra-EU distance goods, not a separate allowance for each. The supplier must be established/addressed/resident in only one member state; services go to non-taxable persons in other member states and qualifying goods dispatch from that sole state to another. Total must not exceed EUR 10,000 in the current **and preceding** calendar year. Equality qualifies; the full supply that crosses the threshold uses destination, not only its excess. A voluntary destination option lasts at least 2 calendar years (in words on the page). Non-EU and multi-member-state established suppliers cannot use this exception. These are place rules, not a blanket exemption or OSS registration trigger. Article 59c: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

Use eligible OSS optionally, or required local registrations, for taxable destination supplies. Also check the cross-border SME exemption where available; destination does not mean every supply must bear VAT. See `eu-oss-digital.md`. Sources: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en.

#### 2.8 "Listed Services" to Non-EU Consumers (B2C)  -  Article 59 [T1]

For a non-taxable person established/addressed/resident outside the EU, Article 59 locates these at the customer: intellectual-property/copyright licensing; advertising; consulting, legal, accounting, engineering and similar services; data processing/information; obligations to refrain from relevant activities/rights; banking, financial and insurance transactions except safe-deposit hire; staff supply; movable tangible-property hire except transport; and gas/electricity/heating/cooling-network access, transmission/distribution and directly linked services. TBE uses Article 58, not the former erroneous Article 59 list. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

A non-listed personal service does not automatically default to Article 45: first test property, activities, transport, catering and other special rules. Cleaning identified property can be Article 47; physical yoga instruction can be Article 54. Article 59a permits national effective-use-and-enjoyment adjustments for specified services to avoid double/non-taxation or distortion; check actual national implementation before the final result. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

### Section 3: Rules for Goods

#### 3.1 Domestic Supply  -  No Transport (Article 31) [T1]

Place is where goods are located when supplied. A German shop's walk-in sale of goods located there has German place; apply the actual product/exemption/registration rules. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 3.2 Goods Dispatched or Transported (Article 32) [T1]

Ordinary place is where dispatch/transport to the customer begins: a German warehouse dispatching to a German customer has German place. Distance sales, installation and other specific rules can override this. When dispatch begins outside the EU, Article 32's second paragraph places the designated importer's supply and subsequent supplies in the import member state. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 3.3 Intra-EU Distance Selling (Articles 14(4)/33) [T1]

Qualifying supplier-dispatched/facilitated goods to the specified non-taxable or acquisition-exempt recipients in another member state are normally located where transport ends. Mere absence of a VAT number is not the statutory recipient test. Exclude new means of transport and supplier-installed/assembled goods; check Article 35 margin-scheme exclusions and electronic-interface deemed supplies under Articles 14a/36b. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

Apply the fully conditioned net combined EUR 10,000 exception in Section 2.7; otherwise destination applies from the crossing supply. Union OSS is an optional report route, with local registration an alternative. The former national EUR 35,000/EUR 100,000 distance-sales thresholds were replaced from 1 July 2021; they are historical, not alternatives to Article 59c. Directive Articles 33/59c and Commission overview: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en.

#### 3.4 Imports from Outside the EU (Articles 30/60–61) [T1]

Ordinary import place is the member state of entry under Article 60. For the specified suspensive customs arrangements Article 61 instead uses the state where the arrangement ceases. Member states designate the liable importer/person under Article 201. Article 211 permits qualifying postponed return accounting: payment to customs at entry is not universal. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

For eligible distance sales of imported goods in consignments of intrinsic value no more than EUR 150, excluding excise products, optional IOSS collects destination VAT on the sale when payment is accepted; a valid IOSS import is exempt from import VAT under Article 143(1)(ca). It is not merely an import with VAT paid at the border. Non-EU suppliers normally need an EU intermediary, subject to the Article 369m mutual-assistance condition. Customs duty remains separate. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1, Articles 14(4), 33, 143(1)(ca), 369l–369n.

#### 3.5 Installation or Assembly (Article 36) [T1]

Place is where goods are installed/assembled by or for the supplier, with or without a trial run. German machinery shipped and installed in a French factory has French place; then check French liability/registration and rate. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

#### 3.6 Chain Transactions (Article 36a) [T1]

Directive (EU) 2018/1910 introduced this chain-transaction rule; the current consolidated Directive identifies it as insertion M21 immediately above Article 36a. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

For successive supplies A → B → C of the same goods with direct transport from the first supplier to the final customer across member states, attribute transport to the supply **to** the intermediary operator B, where B (not the first supplier) transports or arranges transport. If B communicates the dispatch member state's VAT number to A, attribute it to B's onward supply instead. Article 36a excludes Article 14a deemed-interface transactions. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

Only the attributed moving supply can qualify as the intra-Community exempt supply under Article 138; attribution itself grants no exemption. Test transport, recipient VAT identification outside dispatch state, recap conditions and evidence. Other chain supplies require their own location/treatment; avoid assuming every residual supply is simply taxable domestic. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1, Articles 36a/138–139.

**Simplified triangulation (Article 141):** retain A (MS1) → B (MS2) → C (MS3), but three countries alone do not suffice. B must not be established in MS3 and must be identified in another state; its acquisition is for a subsequent MS3 supply; goods travel directly from a state other than B's identification state to C; C is identified in MS3 and designated liable under Article 197. Check invoice/recap and Article 42 conditions. The qualifying invoice carries "Reverse charge" and C accounts for tax. Source: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1, Articles 42, 141, 197, 226(11a), 265.

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

An item can comprise goods sharing tariff classification, description and origin where the declaration requires origin; EUR 3 is neither universally per physical article nor per parcel. Declaration lines and dataset matter. IOSS remains optional VAT collection, not a customs-duty exemption. When the seller recovers duty from the customer it forms part of the sale consideration/VAT base; the valid IOSS import is VAT-exempt. For special-arrangement/standard imports, customs duty enters the import VAT base. Source: Regulation 2026/1022 Article 1(1)(b) https://publications.europa.eu/resource/cellar/3b9f822b-74e8-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1; Commission revised VAT addendum, 6 October 2026, pages 1–4 https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=VAT+treatment+of+the+EUR+3+customs+duty+and+of+the+EUR+2+Customs+Union+handling+fee+%E2%80%93+Revised+version+06+October+2026.pdf.

### Section 5: Non-EU Rules Comparison

#### 5.1 US Sales Tax Nexus

| Aspect | US Rule | Official source |
|---|---|---|
| Tax type / sourcing | State and local sales/use taxes; establish nexus, product taxability, sourcing, exemption and marketplace responsibility separately. There is no single EU-style national VAT registration | https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates; https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm |
| Physical nexus | Actual state connections matter. South Dakota's examples include property, sales staff and deliveries in company vehicles; this is not an exhaustive all-state test | https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates |
| Economic nexus (*South Dakota v. Wayfair*, 2018) | Do not reuse a universal USD 100,000/200-transactions rule. South Dakota removed its 200-transaction limb from 1 July 2023; its current remote-seller rule is **more than** USD 100,000 gross sales in the current or preceding calendar year. Other states have their own tests | https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates |
| Digital services / CA | California electronic-only data/software/downloads generally are not taxable; a tangible backup/printed copy can change the entire sale's treatment | https://cdtfa.ca.gov/formspubs/pub109/nontaxable-sales.htm |
| Digital services / GA | Georgia Rule 560-12-2-.118(5)(c) excludes SaaS. Distinguish taxable specified digital goods and permanent-use rights from excluded subscriptions | https://rules.sos.ga.gov/gac/560-12-2 |
| Digital services / MO | Missouri 12 CSR 10-109.050(3)(I) excludes SaaS; provider-owned tangible property can still bear tax | https://www.sos.mo.gov/cmsimages/adrules/csr/current/12csr/12c10-109.pdf |
| Buyer accounting | Purchaser use-tax self-assessment exists. California requires qualifying taxable purchases without seller collection to be reported; this is not the EU credit-invoice reverse-charge mechanism | https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm |
| Key difference from EU | Build the actual state-by-state nexus/taxability/sourcing register. Tax automation such as Stripe Tax, TaxJar or Avalara does not establish the legal result or replace official state rules | https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates; https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm |

The original nationwide SaaS/state counts are retained as unconfirmed under Sources; they are not a 2026 compliance rule.

#### 5.2 Australian GST on Imports

| Aspect | Australian Rule | Official source |
|---|---|---|
| Threshold | AUD 75,000 or more relevant annual GST turnover for ordinary businesses; test relevant current/projected GST turnover under Division 188, applying its statutory exclusions (including the special non-resident rules). Not a global revenue shortcut | https://softwaredevelopers.ato.gov.au/GSTintangibles; https://business.gov.au/registrations/register-for-taxes/register-for-goods-and-services-tax-gst; https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html |
| Digital services B2C | Qualifying offshore consumer sales require supplier/platform analysis and registration when required; standard GST is 10% of value under section 9-70, not an automatic charge on every offshore supply | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html; https://softwaredevelopers.ato.gov.au/GSTintangibles |
| Low-value goods | Customs value ≤AUD 1,000, excluding tobacco/tobacco products/alcohol. Consumer point-of-sale collection began 1 July 2018; test supplier/platform responsibility, registration and taxable-importation exceptions | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html; https://www.abf.gov.au/help-and-support-subsite/customsnotices/2018-13.pdf |
| B2B | Division 84 is conditional: for ordinary offshore intangibles not connected with Australia, consideration, registered/required recipient, enterprise purpose and **not solely creditable purpose** are key. Fully creditable ordinary offshore purchases generally do not trigger section 84-5. Special deemed-consumer cases and agreed Division 83 reverse charge need separate analysis | https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |

Sections 84-10/84-12 make the recipient liable for a qualifying Division 84 supply at 10% of its price. This price rule differs from ordinary section 9-70's value rule; check input-credit entitlement separately. Source: https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html.

#### 5.3 India OIDAR (Online Information and Database Access or Retrieval)

| Aspect | Indian Rule | Official source |
|---|---|---|
| Applies to | Foreign OIDAR to a non-taxable online recipient: now **any unregistered person**, including a person registered solely for TDS under CGST section 24(vi), not merely a private consumer | IGST sections 2(16)/14: https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |
| Definition | Delivery mediated by IT over an electronic network whose nature makes supply impossible without IT. The old substantially automated/minimal-human requirement was omitted from 1 October 2023; do not import the EU ESS test | IGST section 2(17) and amendment footnote: https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |
| Place and liability | Section 13(12) uses recipient location, with its specified non-contradictory evidence test; section 14 places liability on the overseas supplier, subject to its intermediary deemed-supplier conditions | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |
| Rate | Classify the actual service and current notification before computing. This comparison does not establish a universal OIDAR rate; the former blanket figure is reserved under Sources | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |
| Registration | Mandatory foreign-OIDAR registration is not subject to the ordinary turnover threshold. Use the single simplified route, FORM GST REG-10, rather than generic NRTP REG-09; GST portal Services → Registration → New Registration, relevant non-resident online-provider category | IGST section 14: https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf; CBIC Circular 257/03/2026 sections 3.1–3.2 and Annex I Q3–5: https://ifsca.gov.in/CommonDirect/ViewFile?fileName=Circular_No_257_03_2026__1__20261104_1149.pdf&id=850da50e42b9c192894a42a7d2ca34ff |
| B2B | For a registered Indian recipient, test import/place, exemption and Notification 10/2017-Integrated Tax (Rate), serial 1; the notified recipient reverse-charges a qualifying taxable service from non-taxable territory | https://cbic-gst.gov.in/hindi/pdf/integrated-tax-rate/Notification10-IGST.pdf; https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf |
| Equalization Levy | Historical 2% e-commerce levy ceased for consideration on/after 1 August 2024; remaining equalisation-levy provisions ceased from 1 April 2025. The old 2% category had a relevant-consideration Rs. 2 crore threshold, not a global-revenue test. It is not a current GST surcharge | https://www.incometaxindia.gov.in/equalisation-levy3 |

For Indian software-development exports, the foreign-customer fact alone is insufficient: IGST section 2(6) requires supplier in India, recipient and place outside India, permitted foreign exchange/INR receipt and no merely same-person establishments. Apply section 13's actual rule/exceptions and section 16. Eligible registered exporters can use the bond/LUT route without IGST subject to the current export/receipt conditions; FORM GST RFD-11 is the CBIC route. This skill does not settle a missing condition or refund entitlement. Sources: https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf, sections 2(6), 13, 16; CBIC circular, paragraph 2 https://cbic-gst.gov.in/pdf/circularno-2-gst.pdf. Current national procedures must accompany filing. CGST Rule 96A(1)(b), as substituted by Notification 12/2024 rule 20, expressly accommodates the later of the specified year and permitted FEMA/RBI receipt period, plus applicable Commissioner extension; do not apply a stale fixed receipt deadline. Official amendment: https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf.

The scanned section 13(8)(b) intermediary-location clause is historical: Finance Act 2026 section 157 omitted it from 30 March 2026. Apply section 13(2) and remaining applicable exceptions to current facts, rather than repeating the pre-amendment supplier-location rule. Official Act sections 1/157: https://egazette.gov.in/WriteReadData/2026/271439.pdf.

#### 5.4 Japan Consumption Tax on Digital Services

| Aspect | Japanese Rule | Official source |
|---|---|---|
| Rate | Standard combined consumption tax 10%; reduced 8% applies to qualifying food/drink excluding alcohol/dining out and specified subscription newspapers, not electronic services merely because they are content | https://www.nta.go.jp/english/taxes/consumption_tax/01.htm |
| Foreign B2C electronic services | Japanese recipient location and service classification matter; supplier normally accounts unless an applicable exemption or specified-platform rule changes the result | https://www.nta.go.jp/english/taxes/consumption_tax/0024006-219.pdf; https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6635.htm; https://www.nta.go.jp/english/taxes/consumption_tax/05.htm |
| B2B | Nature/contract terms must normally limit the electronic service to business recipients; a business buyer alone does not prove B2B classification. Qualifying specified taxable purchases use recipient reverse charge, with general-taxation taxable-sales ratio ≥95%, simplified-taxation and applicable transitional-period exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6118.htm |
| Threshold | Normally exempt where base-period taxable sales are ≤JPY 10 million, subject to specified-period, new-company/capital, foreign-business and QIS-registration exceptions. Do not state nil de minimis or unconditional liability regardless of revenue | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6635.htm; https://www.nta.go.jp/english/taxes/consumption_tax/0024006-219.pdf |
| Platform | Since 1 April 2025, qualifying foreign B2C electronic services with consideration through a specified platform are deemed supplied by that platform | https://www.nta.go.jp/english/taxes/consumption_tax/05.htm |
| Invoice system | QIS began 1 October 2023. Books/qualified-invoice requirements have statutory exceptions and transitional partial-credit rules; absence of a registered invoice is not an unconditional total denial | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm |

#### Comparison Summary

| Feature | EU | US | Australia | India | Japan | Official sources |
|---|---|---|---|---|---|---|
| Tax type | VAT | State/local sales and use | GST | GST; EL now historical | JCT | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm; https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html; https://www.incometaxindia.gov.in/equalisation-levy3; https://www.nta.go.jp/english/taxes/consumption_tax/01.htm |
| B2B mechanism | Article 196 when conditions apply | Seller collection / purchaser use tax as applicable | Conditional Divisions 83/84 | Notified qualifying import reverse charge | Specified purchases with exceptions | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm; https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html; https://cbic-gst.gov.in/hindi/pdf/integrated-tax-rate/Notification10-IGST.pdf; https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6118.htm |
| B2C digital | Customer place, conditioned exceptions | Nexus **and** sourcing/taxability | Connected consumer supply | Recipient place / OIDAR status | Recipient place and classification | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates; https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html; https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf; https://www.nta.go.jp/english/taxes/consumption_tax/0024006-219.pdf |
| Registration | Optional eligible OSS or local routes | Per state obligations | ATO standard/simplified route | Foreign OIDAR single simplified registration | NTA supplier or specified-platform obligations | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en; https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates; https://softwaredevelopers.ato.gov.au/GSTintangibles; https://ifsca.gov.in/CommonDirect/ViewFile?fileName=Circular_No_257_03_2026__1__20261104_1149.pdf&id=850da50e42b9c192894a42a7d2ca34ff; https://www.nta.go.jp/english/taxes/consumption_tax/05.htm |
| Threshold | Conditioned net combined EUR 10,000 place exception | State-specific; no national threshold | Ordinary AUD 75,000 GST-turnover test | No ordinary turnover threshold for liable foreign OIDAR | Normally JPY 10 million base-period exemption, with exceptions | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates; https://softwaredevelopers.ato.gov.au/GSTintangibles; https://business.gov.au/registrations/register-for-taxes/register-for-goods-and-services-tax-gst; https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html; https://ifsca.gov.in/CommonDirect/ViewFile?fileName=Circular_No_257_03_2026__1__20261104_1149.pdf&id=850da50e42b9c192894a42a7d2ca34ff; https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6635.htm |

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
| Germany | France | Web development (B2B) | Ordinary business service to French establishment, German supplier not established there: Article 44/196, no German VAT; standard taxable French recipient self-assesses at 20%, with deduction separate | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Germany | France | Web development (B2C) | Bespoke human work, no special-rule facts: Article 45 Germany, standard taxable supplier charges 19%; do not classify by internet delivery alone | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Germany | France | SaaS subscription (B2C) | Article 58 France at standard 20% for this taxable SaaS, **unless** fully conditioned Article 59c origin exception applies; optional OSS/local route | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |
| Malta | US | Consulting (B2B) | Ordinary service to US business establishment: Article 44 US place, no Malta VAT. Check US/state treatment separately | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates |
| Malta | US | Pre-recorded online course (B2C) | Automated ESS: Article 58 customer place outside EU, not Article 59; check actual location/use-enjoyment and US nexus/taxability | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates |
| UK | Germany | Design services (B2B) | Ordinary general-rule service to German business, no property/other exception: outside UK VAT; Article 44/196 German recipient liability if UK supplier non-established there, rate/exemption checked locally | https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 |
| India | Australia | Software dev (B2B) | Zero-rated export only with IGST section 2(6)/13/16 facts; eligible bond/LUT route does not cure missing export conditions. Australian Division 84 charge only if its conditions apply, generally absent for an ordinary wholly creditable offshore purchase | https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf; https://cbic-gst.gov.in/pdf/circularno-2-gst.pdf; https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html |
| US | EU consumers | SaaS product (B2C) | Taxable automated service: Article 58 destination, no Article 59c benefit; optional non-Union OSS or local registration, platform/exemption analysis first | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en |
| France | Switzerland | Architecture for property in France | Specified French property, Article 47 France; standard taxable architecture 20% if supplier-liable, regardless of Swiss customer address. Check actual supplier establishment/national liability | https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm |

## Boundary and exception table

### EC1  -  Bespoke software vs. SaaS (ESS classification) [T2]

**Situation:** A developer builds custom software for a specific B2C client. **Resolution:** Significant human development is not automatically an electronic service; apply Regulation Article 7's automation/minimal-human test to the actual supply. Ordinary bespoke services follow Article 45 B2C/Article 44 B2B absent another exception; automated SaaS normally Article 58 B2C. Escalate uncertain customisation. Sources: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

### EC2  -  Remote worker creating PE risk [T2]

**Situation:** A UK freelancer works from Spain for 8 months serving UK clients. **Resolution:** That duration is an illustrative fact, not a VAT establishment threshold. Regulation Articles 10–13 test central administration, actual permanence/resources, address and residence. Determine whether a Spanish supplying establishment affects Article 45; Article 44 still tests the customer's receiving establishment, while supplier establishment can change liability. Assess residence/permanent-establishment tax risks separately; VAT fixed establishment and income-tax PE are not interchangeable. Sources: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1.

### EC3  -  Mixed digital and live service bundle [T2]

**Situation:** Pre-recorded videos plus live weekly coaching calls to an EU consumer. **Resolution:** Determine independent supplies, a principal/ancillary supply, or an inseparable economic whole from the contract and substance; a single price is not decisive. Automated videos may be Article 58; live educational activities made virtually available may be Article 54 customer place, although excluded from ESS. Ordinary individual consultancy can be Article 45. Do not automatically assign live coaching to supplier place or force principal-element analysis onto every inseparable bundle. Sources: https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1; https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; C-41/04 paragraphs 17–30 https://publications.europa.eu/resource/cellar/0ae577bc-f9ea-49a0-bca7-ea5362c31dd4.0002.02/DOC_1 .

### EC4  -  Chain transaction with unknown intermediary role [T3]

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

Sources for EU prohibitions: https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1; https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1. National boundaries: Section 5's primary sources. Refer uncertain composites, establishment, triangulation, exemption, customs preferences or national filing details to the relevant qualified reviewer; preserve conditional results and missing facts.

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

Read on 14 November 2026 means the actual operative sections below, including neighboring conditions, were read. Generic legal-index redirects and blocked pages were not treated as source text. The EU consolidation is dated 14 April 2025; current 2026 scheme guidance and the separate 2026 customs amendments supply the stated later changes. India’s scanned Act includes amendments through 2024; Finance Act 2026 section 157 and the current registration circular are read overlays, and the Rule 96A amendment is sourced separately.

| Official source | Actual read scope | Read date |
|---|---|---|
| VAT Directive https://publications.europa.eu/resource/cellar/03c42d77-512a-11f0-a9d0-01aa75ed71a1.0007.02/DOC_1 | Read for Articles 14/14a, 30–61, 138–143, 168–169, 192a–197, 201, 211, 226, 262–265, 358a–369x; place, exemption, liability and schemes| 2026-11-14 |
| VAT Implementing Regulation https://publications.europa.eu/resource/cellar/5bc93f0b-2a93-11f0-8a44-01aa75ed71a1.0006.02/DOC_1 | Read for Articles 7/Annex I, 9a–13b, 17–24f, 31a–40; automation, establishment, recipient evidence, property/events/hire| 2026-11-14 |
| C-647/17 https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:62017CJ0647 | Read for Whole judgment and ruling; especially paragraphs 23–36; former reversed result corrected| 2026-11-14 |
| C-41/04 https://publications.europa.eu/resource/cellar/0ae577bc-f9ea-49a0-bca7-ea5362c31dd4.0002.02/DOC_1 | Read for Judgment paragraphs 17–30 and neighboring single-supply reasoning| 2026-11-14 |
| Commission OSS https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en ; https://vat-one-stop-shop.ec.europa.eu/one-stop-shop/declare-and-pay-oss_en | Read for Eligibility, scheme coverage, return/payment and national portal responsibilities; optional registration| 2026-11-14 |
| EU customs https://publications.europa.eu/resource/cellar/2ae65d0b-0c6b-11f1-8870-01aa75ed71a1.0006.03/DOC_1 ; https://publications.europa.eu/resource/cellar/3b9f822b-74e8-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1 | Read for Regulation 2026/382 Articles 1–4 and neighboring recitals; 2026/1022 Articles 1–2 and Annex, including postal/item definitions| 2026-11-14 |
| Commission VAT/customs addendum https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=VAT+treatment+of+the+EUR+3+customs+duty+and+of+the+EUR+2+Customs+Union+handling+fee+%E2%80%93+Revised+version+06+October+2026.pdf | Read for All 4 pages, revised 6 October 2026: customs duty versus VAT base and import exemption; fee expectation not enactment| 2026-11-14 |
| EU current rate card https://europa.eu/youreurope/business/finance-and-tax/vat/vat-rules-rates/index_en.htm | Read for All 27 member-state standard rates; examples use only standard taxable scenarios and no territorial derogations| 2026-11-14 |
| South Dakota DOR https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates | Read for SB30 effective change and remote-seller FAQ incl physical presence/current-prior gross sales; no national threshold inference| 2026-11-14 |
| California CDTFA https://cdtfa.ca.gov/formspubs/pub109/nontaxable-sales.htm ; https://cdtfa.ca.gov/taxes-and-fees/use-tax/business-use.htm | Read for Electronic-only versus tangible data/software; purchaser use-tax conditions and reporting| 2026-11-14 |
| Georgia Secretary of State https://rules.sos.ga.gov/gac/560-12-2 | Read for Rule 560-12-2-.118 definitions, imposition, sourcing and exemptions/exclusions, especially (5)(c)| 2026-11-14 |
| Missouri Secretary of State https://www.sos.mo.gov/cmsimages/adrules/csr/current/12csr/12c10-109.pdf | Read for 12 CSR 10-109.050 definitions/rules/examples, particularly (3)(I) SaaS| 2026-11-14 |
| Australian GST Act https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_1/document_1.html | Read for 2026 compilation, sections 9-5/25/26/70, 23-5/15, 83-5–35, 84-5–13 and 84-75–85: liability, consumer scope and exclusions| 2026-11-14 |
| ATO https://softwaredevelopers.ato.gov.au/GSTintangibles ; https://business.gov.au/registrations/register-for-taxes/register-for-goods-and-services-tax-gst | Read for Imported services/digital consumer summary; GST rate and registration/turnover; historical developer page supplemented with 2026 Act| 2026-11-14 |
| Australian Border Force https://www.abf.gov.au/help-and-support-subsite/customsnotices/2018-13.pdf | Read for Notice 2018/13 both pages: historical commencement, consumer/supplier roles and goods exclusions; current thresholds checked against 2026 Act| 2026-11-14 |
| Indian IGST Act https://thc.nic.in/Central%20Governmental%20Acts/Integrated%20Goods%20and%20Services%20Tax%20Act%2C%202017..pdf | Read for Scanned pages 2–4, 16–22: sections 2(6)/(14)–(17), 13, 14/14A, 16 and amendment notes; visually read operative pages| 2026-11-14 |
| CBIC registration circular https://ifsca.gov.in/CommonDirect/ViewFile?fileName=Circular_No_257_03_2026__1__20261104_1149.pdf&id=850da50e42b9c192894a42a7d2ca34ff | Read for Circular 257/03/2026, pages 1–3 and Annex I Q3–5: current category, compulsory registration, REG-10 and portal menu| 2026-11-14 |
| CBIC import service notification https://cbic-gst.gov.in/hindi/pdf/integrated-tax-rate/Notification10-IGST.pdf | Read for Notification 10/2017-Integrated Tax (Rate), preamble, serial 1, explanation and commencement; not a rate notification| 2026-11-14 |
| CBIC export circular https://cbic-gst.gov.in/pdf/circularno-2-gst.pdf | Read for Paragraphs 1–3: bond/LUT and FORM GST RFD-11; historical procedural text, no current receipt deadline asserted| 2026-11-14 |
| Indian Income Tax Department https://www.incometaxindia.gov.in/equalisation-levy3 | Read for Current sunset note, historic e-commerce period and Rs. 2 crore relevant-consideration exclusion| 2026-11-14 |
| Japan NTA https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6635.htm ; https://www.nta.go.jp/english/taxes/consumption_tax/0024006-219.pdf | Read for 2026 No.6635 all operative paragraphs/notes; July 2024 electronic-services brochure all 5 pages including QIS exception| 2026-11-14 |
| Japan NTA https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6118.htm ; https://www.nta.go.jp/english/taxes/consumption_tax/05.htm | Read for 2026 No.6118 definition, reverse-charge transition/exceptions and invoice paragraphs; platform scope/effective date| 2026-11-14 |
| Japan NTA https://www.nta.go.jp/english/taxes/consumption_tax/01.htm ; https://www.nta.go.jp/taxes/shiraberu/taxanswer/shohi/6498.htm | Read for Basic knowledge sections 6–11 and rate table; current 2026 No.6498 invoice exceptions/transition, without asserting an old credit percentage| 2026-11-14 |
| UK HMRC https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | Read for Notice 741A sections 1.4, 2, 3–4 and 6.1–6.4; general service place and outside-UK result| 2026-11-14 |

| Finance Act 2026 https://egazette.gov.in/WriteReadData/2026/271439.pdf | Read for pages 1 and 77–78, sections 1/157, commencement and sole IGST amendment; operative pages visually inspected | 2026-11-14 |
| CBIC Notification 12/2024 https://gstcouncil.gov.in/sites/default/files/2024-09/central-tax-12-2024-11072024.pdf | Read for rule 1 commencement and rule 20, pages 7–8: Rule 96A receipt-period substitution and GSTR-1A | 2026-11-14 |

| Australian GST Act volume 2 https://www.legislation.gov.au/C2004A00446/2026-01-01/2026-01-01/text/original/epub/OEBPS/document_2/document_2.html | Read for Division 188, sections 188-10 through 188-40: current/projected turnover, inclusions and exclusions; not limited simply to taxable supplies | 2026-11-14 |

**Not yet confirmed:** The original US counts "SaaS taxable in ~25 states" and "45+ states" have not been established from a complete 2026 official state-by-state inventory; do not use them. The former universal Indian OIDAR 18% figure has not been confirmed across classifications and current rate notifications; do not compute it from this skill. The Commission's 6 October addendum expected a separate EUR 2 handling fee from 1 November 2026, but that expectation alone does not prove adoption/current application; no operative fee instruction is given. Current Greek Article 194 conditions, every national return box and any transaction-specific exemption/rate not established here require the relevant national overlay. These are preserved evidence gaps outside the usable method, not alternative conclusions.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. VAT rates, thresholds, and place-of-supply rules are subject to change. Always verify current rules with official sources and a qualified indirect tax advisor.

*Data reflects 2025–2026 rules. OpenAccountants  -  open-source accounting skills for AI  -  info@openaccountants.com*
