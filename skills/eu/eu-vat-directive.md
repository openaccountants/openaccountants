---
name: eu-vat-directive
description: "Shared EU VAT reference for 2026: territorial scope, the Directive rate framework, intra-Community acquisitions, B2B services, place-of-supply exceptions, distance sales, OSS/IOSS, recapitulative statements, imports, input deductions, invoices and SME exemptions. Load the relevant country Guide for national options, rates, forms and deadlines. Future ViDA implementation and unproven national rate details are explicitly held for specialist review. Companion workflow: eu-vat-base."
jurisdiction: EU
tax_year: 2026
last_updated: 2026-11-27
version: 1.4
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# eu-vat-directive

## Scope

EU VAT common rules for **2026**, read against Directive 2006/112/EC consolidated to 14 April 2025. Use the relevant country Guide alongside this reference; national options and derogations need their national implementation. Resolve any conflict with the operative law. Contributor: Open Accounting Skills Registry.

## Ask the client first

Establish supplier and customer locations and fixed establishments, customer status and business use, goods versus services, actual dispatch/destination, transaction date, deduction entitlement, and current/preceding-year domestic and Union turnover. Read the available records before asking for missing facts.

## The method, step by step

### Territory

- The 27 Member States are Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain and Sweden ([EU country list](https://european-union.europa.eu/principles-countries-history/eu-countries_en)). EU membership alone does not establish VAT territory.
- The UK is outside the EU; Northern Ireland remains within the EU VAT regime for goods, but not services. Preserve that distinction for goods movements ([Revenue, postponed accounting](https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part07-provisions-relating-to-imports-exports/postponed-accounting.pdf)). Norway, Switzerland, Iceland, USA, Canada, Australia and UAE are not Member States.
- Article 6 excludes Mount Athos, Canary Islands, the specified French territories under TFEU Articles 349/355(1), Åland Islands, Channel Islands, Campione d'Italia, Italian waters of Lake Lugano, Heligoland, Büsingen, Ceuta, Melilla and Livigno. Apply the third-territory rules rather than assuming an intra-EU transaction ([Articles 5–6](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng)).

### Rate framework

These are permissions and limits, not a national rate card. The former country rate table and regional/mid-year detail are held under Sources.

| Rule | Rate or limit and conditions | Official source |
|---|---|---|
| Standard | One standard rate for goods and services; at least 15% (Articles 96–97). | https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng |
| Reduced | Member States may apply two reduced rates, at least 5%, to Annex III supplies in at most 24 points (Article 98(1)). | same |
| Below-minimum and zero | In addition, one rate below 5% and an exemption with input deduction, for at most seven Annex III points from (1)–(6), (10c), or the Article 105a(1) options. Article 98(2) allows existing coverage over seven points until 1 January 2032 or earlier definitive arrangements. | same |
| Acquired rights | Article 105a(1) preserves qualifying treatment applied on 1 January 2021 within its conditions. Article 105a(2) continuation outside Annex III ends on 1 January 2032 or earlier definitive arrangements. | same |
| Parking | Article 105a(3) preserves qualifying rates of at least 12% outside Annex III applied on 1 January 2021; other Member States may adopt under the same conditions and Article 105a(5) procedure. | same |
| Environmental sunset | Under Article 105a(4), the specified reduced/zero treatment ends by 1 January 2030 for fossil fuels, peat and firewood, and by 1 January 2032 for chemical pesticides/fertilisers. | same |
| Electronic services | Article 98(3) excludes reduced rates/exemptions except Annex III points (6), (7), (8), (13). | same |
| Acquisition/import rate | Like domestic goods under Article 94(1)–(2); Article 94(3) permits a reduced import rate for specified art, collectors' items and antiques despite a domestic standard rate. | same |

### Intra-Community goods

- An acquisition is obtaining the right to dispose as owner of movable tangible goods transported between Member States (Article 20). For ordinary goods, test Article 2(1)(b)(i): purchaser acting as a taxable person or non-taxable legal person; taxable vendor outside the SME exemption and Articles 33/36. Article 3 exclusions and Article 4 margin-scheme exclusions prevent an automatic charge merely because goods cross a border. New means of transport and excise goods have separate Article 2 rules. [Articles 2–4, 20](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Acquisition place is where transport ends. Using another Member State's VAT number can also trigger Article 41 taxation there until destination taxation is established; the Article 42 triangulation exception has separate conditions. The person making a taxable acquisition is liable under Article 200. [Articles 40–42, 200](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Supplier exemption requires actual transport to another Member State, a qualifying customer acting there, and its VAT identification in a different Member State from dispatch communicated to the supplier. A missing/incorrect recapitulative statement defeats exemption unless duly justified to the authority. Check Article 139's SME, acquisition-exclusion and margin-scheme exceptions. [Articles 138–139](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Self-assess at the applicable rate; deduction is separate and limited to deductible use, exclusions and formalities. For an acquisition, Article 178(c) requires the return information and invoice. Equal output/input VAT and a zero net amount arise only with full deduction. [Articles 94, 168(c), 173, 176, 178](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Acquisition VAT becomes chargeable on invoice issue or expiry of the Article 222 deadline if no invoice was issued; the qualifying supply invoice is due by the fifteenth day of the following month. [Articles 67, 69, 222](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Article 45a's rebuttable transport presumption needs two non-contradictory transport items, or one transport item plus a qualifying insurance/bank, official-arrival or destination-warehouse item. Issuers must be independent of each other, vendor and acquirer. Where the acquirer arranges transport, also obtain its statement with all Article 45a(1)(b)(i) particulars by the tenth day of the following month. The authority may rebut the presumption; failure of the presumption is not automatically proof that transport did not occur. [Regulation 282/2011, Article 45a](https://eur-lex.europa.eu/eli/reg_impl/2011/282/2025-04-14/eng).

### Services and reverse charge

- Article 44 ordinarily locates a service to a taxable person acting as such at its business establishment, or the receiving fixed establishment, with permanent address/usual residence as fallback. Article 196 makes the qualifying customer liable when the supplier is not established in that Member State. This includes non-EU suppliers and VAT-identified non-taxable legal persons; it is not supplier zero-rating. Deduction still depends on entitlement and Article 178(f) formalities. [Articles 44, 168, 178, 196](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Software, cloud hosting, consulting, digital services, IP licences and advertising require the actual supply and contracting entity to be checked. The old AWS, Google Workspace, Microsoft 365, Notion, Slack, Stripe and LinkedIn examples are not automatic tax classifications: payment/financial services may be exempt. A supplier's local fixed establishment counts only if it intervenes in the supply; a local VAT number alone is not an establishment. [Articles 135, 192a–196](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng); [Regulation 282/2011, Article 11(3)](https://eur-lex.europa.eu/eli/reg_impl/2011/282/2025-04-14/eng).
- In 2026, Article 194 permits Member States to shift liability for taxable supplies by a non-established supplier to the customer. Article 199a separately permits specified fraud-prone supplies through 31 December 2026, with national conditions. Neither is a universal domestic reverse charge. [Articles 194, 199a](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).

### Distance sales and special schemes

- Article 59c's EUR 10,000 total, excluding VAT, combines qualifying intra-Community distance sales of goods and cross-border B2C telecoms/broadcasting/electronic services. The supplier must be established/resident only in one Member State; customers/destinations must satisfy Article 59c(1)(b), and the total must not exceed the limit in either the current or preceding calendar year. Other B2C services and imported-goods distance sales do not use this threshold. [Articles 33, 58, 59c](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Once exceeded, destination taxation applies from that time. A qualifying supplier may instead elect destination treatment for at least two calendar years. At or below the threshold is not automatically exempt: apply the otherwise applicable origin rule and national treatment unless the option is used. [Article 59c](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Union OSS covers intra-Community distance sales, specified deemed-supplier domestic goods and B2C services where the supplier is not established in the Member State of consumption. It is optional and applies to all supplies within its scope; it does not remove registration obligations for activities outside it. [Articles 369b, 369j](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Non-Union OSS covers qualifying B2C services by suppliers with no EU business/fixed establishment. [Articles 358a, 359](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Union and non-Union OSS returns are quarterly, including nil returns, due by the end of the following month. [Articles 364, 369f](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- IOSS covers imported distance-sale consignments of intrinsic value not exceeding EUR 150, excluding excise goods. Check Article 369m eligibility/intermediary requirements. VAT becomes chargeable on acceptance of payment; import exemption requires the valid IOSS number at customs by declaration. Returns, including nil returns, are monthly and due by the end of the following month. [Articles 143(1)(ca), 369l–369n, 369s](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Input VAT is not deducted in an OSS/IOSS return. Use the applicable refund mechanism or, where required to register for other activities, the appropriate local return. [Articles 368, 369j, 369w](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).

### EC Sales Lists

- Article 262 covers qualifying exempt goods supplies, triangulation and non-exempt Article 196 services; call-off stock has additional information requirements. Report supplier/customer identifiers and values for the proper chargeable period under Articles 264–265. Exempt services are excluded. [Articles 262–265](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Default: monthly within one month. National quarterly permission for goods requires no more than EUR 50,000 in the quarter and each preceding four quarters. If exceeded, permission ends after that month and a statement for elapsed month(s) is due within one month. Services can have national quarterly permission without that cap, but mixed suppliers may follow the goods timetable. [Article 263](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).

### Deductions, refunds and imports

- Non-business expenditure, such as luxuries/amusements/entertainment, is non-deductible. Article 176 also preserves national exclusions at the standstill date or accession. Do not infer a common EU block for every meal, vehicle, fuel or hotel invoice. Test national exclusions, deductible use, partial exemption and documentation. [Articles 168, 173, 176, 178](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Foreign VAT is not automatically an irrecoverable expense. Directive 2008/9 eligibility requires establishment in another Member State, no refund-state establishment effecting transactions and no local supplies except its specified exceptions; deductible business use and refund-state restrictions apply. Incorrectly invoiced VAT is excluded. [Articles 2–6, 18](https://eur-lex.europa.eu/eli/dir/2008/9/2010-10-01/eng).
- Submit the electronic application through the establishment state's portal by 30 September of the following calendar year, complete with Article 8/9/11 information. [Articles 7, 15](https://eur-lex.europa.eu/eli/dir/2008/9/2010-10-01/eng).
- On import, liability is assigned by the Member State of importation. Article 211 allows national postponed accounting through a VAT return; border payment is not universal. [Articles 201, 211](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Import deduction requires qualifying deductible use and an import document identifying the claimant as consignee/importer and stating the VAT or enabling calculation. [Articles 168(e), 178(e)](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).

### VAT numbers and invoices

- Validate customer VAT identification and linked name/address through VIES. For services, Regulation 282/2011 Article 18 also permits other proof and reasonable checks where a number has been applied for but not received; status and business capacity remain decisive. A failed VIES result does not by itself establish that local VAT is due. Goods exemption still requires the Article 138 conditions. [Article 138](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng); [Regulation, Articles 18–19](https://eur-lex.europa.eu/eli/reg_impl/2011/282/2025-04-14/eng).
- Ordinary Article 226 invoice details include issue date/unique sequential number; supplier identification; customer VAT identification when liable or receiving Article 138 goods; names/addresses; quantity/nature or service extent; relevant supply/payment date; taxable amount per rate/exemption, unit prices/discounts, rate and VAT amount where required. Add exemption reference for exempt goods and “Reverse charge” where the customer is liable. “Self-billing” and “Cash accounting” apply only in their specified circumstances. [Article 226](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Article 222's fifteenth-day deadline covers qualifying Article 138 goods and Article 196 services; other invoice deadlines are national. Since 14 April 2025 Member States may mandate e-invoices for established suppliers' domestic supplies other than Article 262 transactions, and may dispense with acceptance by domestic recipients. This is not a universal EU mandate in 2026. [Articles 218, 222, 232](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng); [Directive 2025/516, Article 6(1)](https://eur-lex.europa.eu/eli/dir/2025/516/oj/eng).

### SME exemption

- National exemption is optional; domestic/sector thresholds may not exceed EUR 85,000. Multiple eligible sector thresholds cannot be combined. [Article 284(1)](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- A qualifying business established in another Member State also needs Union annual turnover no greater than EUR 100,000 and compliance with the host threshold; preceding-year exclusions also apply. [Articles 284(2), 288a](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Cross-border exemption needs prior notification and an EX identification number from the establishment state. It starts on notification of that number, or confirmation for an updated notification, normally within 35 working days; anti-evasion/avoidance checks can require longer. [Article 284(3)–(5)](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Exceeding the national threshold in the preceding year prevents exemption for one year; national law may extend to two. The default current-year tolerance is 10%, but national choices can be 25%, no ceiling subject to the EUR 100,000 domestic maximum, or immediate cessation on crossing the national threshold. Cross-border exemption ceases immediately when Union turnover exceeds EUR 100,000 and is unavailable if that Union limit was exceeded in the preceding year. [Article 288a](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).
- Use Article 288's turnover composition, including specified exempt transactions; capital-asset disposals are excluded. Exempt small enterprises cannot deduct VAT or show VAT on their invoices. [Articles 288–289](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng).

## Boundary and exception table

| Service | Place rule; then determine liability and national exemption | Official source |
|---|---|---|
| Property/hotel | Property location, Article 47. | https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng |
| Passenger transport/taxi | Place of transport proportionate to distances, Article 48. | same |
| Restaurant/catering | Physical performance, Article 55; qualifying intra-EU on-board consumption uses departure under Article 57. | same |
| Short-term transport hire | Where put at disposal; continuous use no more than 30 days, or 90 days for vessels, Article 56. | same |
| B2B event admission | Event location, Article 53; virtual attendance excluded from this special rule and ordinarily follows Article 44. | same |
| B2C cultural/sport/education activities | Activity location; streamed/virtual access instead uses customer establishment/address/residence, Article 54(1). | same |
| B2C telecoms/broadcasting/electronic services | Customer establishment/address/residence, Article 58, subject to Article 59c. | same |

Original local examples retained: a Paris hotel locates the service in France; in-person Berlin conference admission in Germany; an Amsterdam business lunch in the Netherlands. With taxable supplies by local established suppliers, local VAT is ordinarily invoiced. Online B2B Berlin attendance ordinarily follows Article 44 instead. Location alone never decides who pays: check Article 194 and national exemptions rather than asserting “never reverse charge”.

## Worked cases

### Case 1: Intra-community acquisition

Original 2026 scenario: a German business buys EUR 10,000 of goods from a French supplier, with a valid customer VAT number and transport to Germany. Assume ordinary standard-rated goods, both acting as taxable persons, no SME/margin or acquisition exclusion, satisfied Article 138/139 reporting and transport conditions, and full German input deduction with required documents. Supplier exemption and purchaser self-assessment then follow; the German standard rate is 19% ([UStG §12(1)](https://www.gesetze-im-internet.de/ustg_1980/__12.html)).

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
  input_vat: 1900.00
  net_payable: 0.00
```

### Case 2: Should the seller charge home or destination VAT

Original 2026 inputs retained: Irish seller established only in Ireland, EUR 12,000 qualifying distance sales into Germany, and a further EUR 1,000 net sale. Assume standard-rated goods, ordinary taxation without SME exemption, dispatch from Ireland, and no excluded special arrangements. Destination taxation has applied from the crossing transaction, not retroactively to earlier sales. The further sale bears German 19%; the Irish 23% comparison applies only to otherwise home-taxed ordinary goods ([Article 59c](https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng); [German §12](https://www.gesetze-im-internet.de/ustg_1980/__12.html); [Irish §46(1)(a)](https://revisedacts.lawreform.ie/eli/2010/act/31/section/46/revised/en/html)). Use eligible Union OSS or destination registration for these taxable sales.

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
  home_vat: 230.00
  destination_vat: 190.00
  difference: 40.00
```

## When to refuse or refer

Do not treat reverse charge as an exemption or automatic full deduction, guess national options, infer VAT treatment from a brand, or apply future ViDA measures to a 2026 transaction.

For triangulation, detailed national derogations and the held topics under Sources: **Check this point with one of our partner accountants.** Do not use the held material to file or price a transaction.

## Filing and payment

Use the country Guide for national registrations, forms, return boxes, payment procedures and deadlines. OSS/IOSS and recapitulative-statement periods above do not replace a national VAT return. Check separate refund eligibility before recording foreign VAT as an expense.

## Completion checklist

Confirm territory, supply classification, supplier/customer status and establishments, applicable national treatment, chargeability, evidence, deduction entitlement, invoice wording, return/recapitulative reporting and any refund process. Recompute the original examples only with their stated assumptions.

## Sources

| Source and scope read | URL | Read on |
|---|---|---|
| Directive 2006/112/EC, consolidation applicable in 2026; Articles 2–6, 20, 33, 40–59c, 67/69, 94–105a, 135, 138–139, 143, 168–178, 192a–201, 211, 218–232, 262–265, 284–289, 358a–369w | https://eur-lex.europa.eu/eli/dir/2006/112/2025-04-14/eng | 2026-11-27; operative provisions read in browser; fetch challenge not counted |
| Regulation 282/2011, Articles 11, 18–19, 45a | https://eur-lex.europa.eu/eli/reg_impl/2011/282/2025-04-14/eng | 2026-11-27; browser text read |
| Directive 2008/9/EC, consolidated Articles 2–7, 15, 18 | https://eur-lex.europa.eu/eli/dir/2008/9/2010-10-01/eng | 2026-11-27; browser text read |
| Directive 2025/516, Article 6 commencement conditions for current domestic e-invoicing permission | https://eur-lex.europa.eu/eli/dir/2025/516/oj/eng | 2026-11-27; Article 6 read in browser |
| EU Member State list, both pages | https://european-union.europa.eu/principles-countries-history/eu-countries_en | 2026-11-27; both lists read |
| German UStG §12(1), standard rate; completed DEVAT-02 read reused for unchanged case rate | https://www.gesetze-im-internet.de/ustg_1980/__12.html | 2026-11-26; completed read reused |
| Irish VATCA §46(1)(a), ordinary standard rate; completed IEVAT-10 read reused | https://revisedacts.lawreform.ie/eli/2010/act/31/section/46/revised/en/html | 2026-11-26; completed read reused |
| Revenue postponed accounting, NI goods/services distinction; completed IEVAT-35 read reused | https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part07-provisions-relating-to-imports-exports/postponed-accounting.pdf | 2026-11-26; completed read reused |

Not yet confirmed: **non-usable holds**: the former national rate table for all listed Member States (including domestic zero, super-reduced and parking coverage), the Belgium/Sweden/Austria/Ireland mid-year changes, Finland/Lithuania start-year changes, old Estonia/Latvia/Luxembourg/Romania/Irish livestock corrections, and Austria/Greece/Portugal/Corsica regional rates. Detailed post-2026 ViDA cash accounting, distance-sale threshold amendment, non-Union/energy OSS, platform deemed suppliers, Article 194 mandatory reverse charge, own-goods OSS, call-off stock transition, import supplier/tax-representative liability, digital invoices/reporting and administrative cooperation/alignment timetable are also held; this Guide does not supply operative future advice. The former broad export-zero-rate conclusion is also held pending its full exemption/deduction conditions. National VAT-number prefixes, invoice currency/special-invoice exceptions, Intrastat, national SAF-T/e-invoicing dates, VAT groups and capital-goods adjustment periods remain country/specialist matters. Check this point with one of our partner accountants.
