---
name: moldova-vat
description: Use this Guide for Moldova VAT (TVA) registration, output tax, input credits, mixed supplies, imports, exported services, tax points and the monthly VAT12 reconciliation for 2026. It covers ordinary registered businesses and explains separate obligations for unregistered service importers, specified property purchasers, energy traders and nonresident electronic-service suppliers. Trigger on Moldova VAT, TVA Moldova, VAT12, imported SaaS, input deduction or SFS VAT filing. Load alongside vat-workflow-base v0.1 or later. Check the dated registration thresholds, actual supply classification and evidence before calculating. Remaining source and implementation gaps are explicit; the country draft has a bounded source-review record linked under Sources.
version: "2.6"
jurisdiction: MD
category: international
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova VAT v2.6

2026 draft, law read 30–31 October 2026. Use alongside `vat-workflow-base` v0.1 or later for document handling. The Moldova law and current return instructions control the tax calculation. The bounded source-review record is linked under Sources; accountant attestation is not provided.

## Who this applies to

This Guide covers ordinary Moldova TVA registration, domestic and imported goods/services, output tax, input credits, mixed activities, adjustments, monthly VAT12 reporting and payment. Classify the taxpayer and the transaction separately: being below the registration threshold does not remove every VAT obligation. Under Fiscal Code art. 94(a)–(f), the taxable persons include registered/required-to-register businesses and permanent establishments, goods importers, service importers irrespective of ordinary registration (subject to the stated social-political-organisation exclusion), certain buyers of insolvent/pledged/mortgaged/seized property, and the separate nonresident electronic-services class. [Code arts. 93–95](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

For an ordinary business, test eligible supplies in **any consecutive 12 months**, excluding supplies exempt without credit and art. 95(2) non-objects. Test again after adding non-exempt imported services under art. 112(4). The threshold is exceeded, rather than merely reached: **MDL 1.5 million for January–February 2026; MDL 1.7 million from 1 March 2026**. Notify/register by the last day of the month of exceedance; ordinary registration takes effect on the first day of the following month. The period previously spent registered is excluded from a subsequent threshold test. The art. 112(1) exclusions include Title II chapter 10^4 independent service entrepreneurs and the specified public bodies/institutions, with the stated public-education exception. A business anticipating taxable supplies can register voluntarily, normally effective from the first day of the month after applying. Eligible network-energy purchasers under art. 110(4) must register before those purchases; reorganisation has its own succession date and five-working-day notification. [January art. 112](https://www.legis.md/cautare/getResults?doc_id=149766&lang=ro), [Law 12/2026 artsI–II](https://www.legis.md/cautare/getResults?doc_id=153159&lang=ro), [current art. 112](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Nonresident automated electronic services to resident nonbusiness individuals follow arts. 94(d),95(1^1),109^1,111(5),112^1,114(1^1),115(1^2),(3), rather than automatically using a business's monthly reverse-charge return. Registration follows assignment of the fiscal code; the period is quarterly, the payment date is the tax point, and the declaration/payment deadline is the 25th after the quarter. MDL, USD or EUR payment is permitted for this class. Ordinary VAT12 amounts are expressed in lei. A card payment to a software brand does not establish whether the customer is a business or the supplier falls in this consumer regime. [Code](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Do not refuse all mixed activity or all dealings across the Nistru. Compute direct attribution/prorata for ordinary mixed activity. Identify the counterparty's actual fiscal relationship and the relevant customs/implementing-law route for cross-Nistru dealings; the specialist procedure remains unconfirmed below. Income-tax calculations belong in the companion income Guides. VAT work here produces evidenced working papers and a return reconciliation, not a bank-statement-only filing conclusion.

### Registration cancellation and final stock/asset calculation

Inform SFS when taxable supplies cease; article 113(1) leaves the cancellation procedure to SFS. SFS can cancel registration itself for failure to furnish the required VAT returns for each tax period, inaccurate headquarters/subdivision address information, or liquidation without a cancellation application before the liquidation tax audit starts. Do not invent a fixed number of missed returns. In liquidation, apply before that audit; otherwise the authority’s 113(2)(d) route applies. [Code 113(1),(2),(6)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); ledger 208–209/213.

**At cancellation**, article 113(3) deems a taxable supply of stock and fixed assets for which acquisition VAT was deducted, and requires payment of the resulting VAT. Use **market value**, or for depreciable assets **the greater of carrying value and market value**. Inventory the qualifying remaining items, original deductions and valuation evidence, then apply their actual VAT classification/rate. The cancellation date under 113(4) is the date of the audit act underlying SFS’s cancellation decision. Formal statutory suspension does not itself cancel registration; if supplies occur during suspension, 113(5) restores VAT rights/obligations from the first day of the month of those supplies. The actual SFS cancellation application and final-return implementation remain unverified. [Code 113(3)–(5)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); ledger 210–212.

## Rates, bands and thresholds

| Item | 2026 treatment | Official source |
|---|---|---|
| Standard rate |20% of the taxable value unless a specific reduced/exempt treatment applies |[Code art. 96(a)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Ordinary registration test |Eligible supplies, and separate combined supplies/imported-services test, **over** MDL 1.5m Jan–Feb; **over** MDL 1.7m from 1 March; rolling 12 months |[January art. 112](https://www.legis.md/cautare/getResults?doc_id=149766&lang=ro), [Law 12 artsI–II](https://www.legis.md/cautare/getResults?doc_id=153159&lang=ro)|
| Listed bread/bakery and milk/dairy |8% on the specified domestic tariff lines; the listed dairy fat condition is maximum 40%; specified baby foods are exempt without credit instead |[Code art. 96(b) first indent; 103(1)(2)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Medicines and medical goods |8% for the statutory authorised/registered medicines, qualifying pharmacy preparations and the listed tariff goods; January–April also included goods registered in the State medical-device register in the second indent. **From 1 May**, that register alone no longer qualifies a device under that indent; check the remaining tariff list or another exemption |[January art. 96](https://www.legis.md/cautare/getResults?doc_id=149766&lang=ro), [May art. 96, Law 41 amendment note](https://www.legis.md/cautare/getResults?doc_id=153671&lang=ro)|
| Pharmaceutical ethyl alcohol |8% for the specified undenatured tariff lines, purposes and annual Government quota; no blanket alcohol reduction |[Code art. 96(b) second indent](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Natural gas/LPG and gas-network services |8% for domestic natural gas, the specified container import/domestic LPG at tariff 2711, and natural-gas transport/distribution; distinguish the network import exemption and energy reverse charge |[Code arts. 96(b),101(1^1)–(1^2),104(b^1),101^7](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Agricultural/food goods |8% for the enumerated natural livestock, crop/horticulture tariff lines, and beet sugar; not every food or agricultural purchase |[Code art. 96(b)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Solid biofuel |8% for the listed electricity/heat/hot-water production purpose, qualifying feedstock/residues, and heat from solid biofuel supplied to public institutions |[Code art. 96(b)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Accommodation and catering |8% for the listed sectionI accommodation and qualifying food/nonalcoholic drinks supplied with related immediate-consumption services; sectionI and art. 93(21) conditions matter |[Code arts. 96(b),93(21)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Specified menstrual products |8% for the stated ex 9619, ex 392490000 and 401490000 goods; match the product description and tariff |[Code art. 96(b)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Exports/international transport |Exempt **with credit**, subject to art. 104(a), export/place rules and evidence; the Code's current category is not a third numeric rate |[Code arts. 93(11),(20),104(a),111](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Residential utilities |Listed electricity/heat/hot water/water/sewerage for residential property, including holiday homes, exempt **with credit**; distinguish ordinary commercial premises |[Code art. 104(b)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Shared-input de minimis |Full shared-input deduction if exempt-without-credit supplies/total relevant supplies is **less than 0.05**; exactly 0.05 does not qualify |[Code art. 102(4)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Business-card cash-register proof |Connected fiscal receipt up to MDL 2,000 inclusive each, no more than MDL 10,000 per period, paid by business card; not a universal invoice waiver |[Code art. 102(10)(d)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|
| Ordinary reporting/payment |Monthly; 25th of the following month, with statutory import/property exceptions |[Code arts. 114–115](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|

The current reduced medical tariff list is 300215000,3005,300610,300630000,300640000,300660000,300670000,370790,380894,382100000,3822,4014,401512000,481890100,900110900,900130000,900140,900150,901831,901832 and 901839000. Use the full art. 96(b) tariff list for agricultural classification, including its express exclusions. A supplier name is not a tariff classification. [Code art. 96(b)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

## The base

### Classify the supply before the payment

For each invoice/contract, identify goods or services, ownership/principal/agent, place, date, taxable person, rate/exemption, taxable value, credit evidence and the reporting box. Goods include buildings; supplies include transfers in kind and specified free transfers. Rent/usufruct/operating lease and use of intellectual property are services. Electricity, heat and gas are goods; ancillary goods/services follow the linkage rules in art. 105. Mandatary transactions in the principal's name belong to the principal under art. 106. Commission and fiduciary chains under art. 107 can contain deemed purchases/resupplies plus a separate service; do not collapse them into a net bank commission. [Code arts. 93,95,105–107](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Under art. 97, start with consideration paid/payable excluding VAT and reduce by the contemporaneous documented discount/rebate/loyalty reduction. Include other taxes/charges except VAT. In-kind consideration uses market value. The taxable value of depreciable assets supplied is the greater of carrying value and market value. Insolvent/secured-property acquisitions have their own purchase-value base. For a proved VAT-inclusive domestic price, separate VAT mathematically as gross×rate/(1+rate); do not divide a stand-alone customs-tax payment by 1.20. Customs import value is customs value plus applicable import taxes/charges excluding VAT under art. 100. [Code arts. 97,100](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Related-party/employee below-market supplies use market value under art. 99(1), with its agricultural cooperative/producer-group exception. Art. 99(2)–(5) distinguishes free employee supplies, personal/family appropriation, free gifts to other persons and remuneration in kind; their bases are not all the same. Use the relevant acquisition-value, production-cost or market-value branch; market value cannot fall below cost of sales under art. 99(6). Art. 95(2)(c) excludes qualifying advertising/promotion gifts within 0.5% of prior-year sales, or for a newly created business 0.5% of preceding-month sales with year-end adjustment. Reorganisation, meal-voucher nominal value and the other art. 95(2) non-objects have their own conditions. [Code arts. 95,99](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

### Exemptions are transaction-specific

Art. 103 exemptions **without credit** include housing/land and their specified rent/rights (not transaction commissions); education directly within the stated education/training categories; authorised state-fee services and professional justice-sector activity; medical services except cosmetic services, the listed medical goods and qualifying care; listed financial operations including insurance/reinsurance/intermediation; postal services; the specified domestic passenger transport and other enumerated supplies. A bank's consultancy, information, rental, cash-handling or custody service can fall outside the financial exemption's wording. Notaries/lawyers cannot be automatically coded 20% solely by their occupation where art. 103(1)(6) applies. A commercial property rent is not the housing/land exemption merely because its bank narrative says “rent”. [Code art. 103(1)(1),(5),(6),(9),(10),(12),(13),(16),(17)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Other express art. 103 exemptions include the listed publications/digital books and associated rights/editing (advertising/erotic exclusions), qualifying agricultural-cooperative services subject to the 75% condition, the listed passenger-vehicle tariffs, certain agricultural machinery, qualifying production/service assets contributed to capital, renewable-generation construction, authorised waste machinery and listed forestry work. Capital-contribution relief under 103(1)(29) requires the Government procedure and has a three-year disposal/use restriction, a clawback and no deduction of that clawback. The exact procedure is not supplied here. Do not confuse an **exempt car purchase** with a universal ban on VAT on every vehicle expense. Customs/re-import/temporary-admission, humanitarian/diplomatic and other specialist art. 103 exemptions require their own evidence. [Code art. 103](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

The following are also exemptions **without credit**, under their actual article 103(1) conditions:

- Point 3 covers State property redeemed in privatisation.
- Point 14 covers the specified gambling-business services and lotteries. Its exception excludes the stated services whose value is included wholly/partly in the stake or admission payment and other services to spectators/participants; it is not an exemption for every service at a gambling venue.
- Point 15 covers the listed human/animal burial and cremation services and related funeral activities, including preparation/embalming, funeral premises and plots, cemetery/grave upkeep, transporting bodies, religious rites, funeral organisation and making/supplying coffins or wreaths.
- Point 16 covers **hostel accommodation** and the listed communal services to the population: residential-space rental, residential-building maintenance, sanitation and lift use. This is distinct from article 104(b)’s listed residential utilities **with credit**.
- Point 27^2 covers anti-hail rockets at tariff 3604. Point 27^3 lists hydraulic turbines up to 1,000 kW at 841011000, generators over 75 kW but not over 375 kW at 850133000, the specified parts at 850300990 and electrical circuit-switching apparatus. Match the actual statutory description and tariff/power limits; a renewable-energy label alone is insufficient.

Sources: [Code 103(1)(3),(14)–(16),(27^2)–(27^3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); existing ledger 110,120–122,131–132. Preserve qualifying invoices and the particular exemption evidence.

Exemption **with credit** under art. 104 includes proved exports and listed international-transport services, the residential utilities, the listed network-energy imports, specified Government-listed assistance projects, defined free-zone/port/airport movements and qualifying light-industry processing. Internal zone supplies can instead be non-objects under art. 95(2)(a). Transport/balancing-energy exclusions and directions of movement matter; neither foreign payment nor a zone address establishes the exemption. Implementing lists/proof for these specialist routes remain unconfirmed below. [Code arts. 95(2),104](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

### Calculate eligible input VAT, not a bank-derived estimate

Under art. 102(1), an ordinary registered payer deducts VAT paid/payable to VAT-registered suppliers on purchases for taxable business supplies. Goods imports require the import tax payment and customs proof; imported-service credit is based on the **calculated** service VAT for the qualifying business use. Keep output and credit separately even when equal. An unregistered service importer does not acquire the registered-payer credit merely by paying reverse charge. [Code arts. 101(1),102(1),(10),115](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

1. Attribute directly: taxable business input is eligible; input exclusively for exempt-without-credit supplies is cost/expense. For shared supplies, apply art. 102(3)–(4), rather than blocking the entire business.
2. Shared-input monthly prorata is relevant taxable supplies excluding VAT/total taxable plus exempt-without-credit supplies, excluding advances from both. Apply the statutory two-decimal rounding and keep the calculation. Use annual figures for the definitive prorata in the final period and adjust the prior deductions. The less-than 0.05 exempt-share rule allows full shared-input deduction; the annual test can recover shared VAT previously expensed. It does not turn exclusively exempt/private inputs into taxable business inputs. The precise fraction-versus-percentage representation for non-exact rounding is left unconfirmed below; both examples use exact ratios. [Art. 102(2)–(4)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).
3. For mixed taxable/exempt building construction, the separate project-estimated taxable-commercial-space cost/total cost coefficient, rounded to two decimals, replaces a sales-ratio shortcut. Recalculate for changed estimates quarterly in the first period after the quarter; changed use has its separate timing. Keep each project separate. [Art. 102(4^1)–(4^3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).
4. Arts. 102(5)–(7) distinguish the named non-objects, a taxable-to-exempt change and the reverse change. Adjust remaining stock by previously deducted/expensed VAT and depreciable assets by the VAT attributable to carrying value, excluding revaluation; use the statutory change/use period, not a blanket five-year adjustment borrowed from another country. [Code](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).
5. Private/nonbusiness purchases, theft, excess waste/perishability and unamortised scrapped assets follow 102(8); documented exceptional destruction follows 102(8^1). Food-donation excess follows 102(8^2). Entertainment unconnected with the business is blocked under 102(9), subject to its 24(19),(19^3) exceptions; direct inputs of an entertainment business qualify under its own rule. Fuel is not taxed at 0% by default. For upkeep/operation/repair of cars used by occupation minor groups 112/121, art. 102(17) permits only one car per such person; check business use and proof as well. [Code art. 102](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).
6. Hold a fiscal invoice, the relevant paid-tax property/customs document, or the narrowly qualifying connected business-card fiscal receipts. Art. 102(14) requires the actual supplier to be the invoice issuer. For the listed services/utilities/petroleum/specified goods, a fiscal invoice issued by the 10th inclusive of the next month permits deduction in the supply month under 102(12). A different invoice received late follows 102(13): deduct in the actual receipt period without amending earlier periods merely for late receipt. Retain actual issue and receipt dates. [Code art. 102(10)–(15)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

### Adjustments, credits and refunds

Documented price changes, returns and later discounts adjust the taxable value under art. 98. Supplier adjustment invoices show minus/plus under 117^1(12). A statutory bad debt permits seller output adjustment beginning in the recognised bad-debt period; later recovery restores taxation. A purchaser's corresponding unpaid bad-debt credit is removed under 116(3). Ordinary overdue status alone is not proof of statutory bad debt. [Code arts. 98,116,117^1](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Ordinary excess input carries forward under 101(2). A cash refund is conditional:101(3) has the listed bread/dairy producer cap, 101(5) the exempt-with-credit supply cap, 101(5^1) the energy simplification cap, 101(6) the leasing cap; 101^1 covers qualifying capital expenditure with exclusions and an in-use production-building route. Art. 101^6 concerns qualifying e-Factura/connected-register transactions from 1 January 2023 and Government limits; 101^8 covers its listed renewable-storage tariffs. The ordinary statutory refund routes generally state 45-days, or 60-days where the taxpayer has filed disagreement with the audit act, but the Government evidence/application rules must also be satisfied. Use a refund decision first against public-budget debt, then permitted future liabilities or the taxpayer's own bank/payment account; do not assign the refund to creditors. An unregistered qualifying 22-plus-passenger vehicle investor has a distinct 101^3 route. Do not fill box 24 merely because a credit exists. The detailed Government procedures and 2026 refund programmes are not confirmed in this draft. [Code arts. 101–101^8](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

## Deadlines and filing

For a refund or tax-offset request, use the [VAT refund application Guide](md-vat-refund.md), which supplies the current HG93 application, route-specific ceilings, paid/unpaid credit allocation, evidence and SFS/Treasury stages. VAT12 submission and the refund application are separate steps.

### Tax points and actual deadlines

The ordinary period is a calendar month. File the official declaration electronically and pay by the 25th of the following month, not month end. Prepare purchase/sales registers by that same 25th. The special nonresident consumer-electronic period is quarterly, as stated above. Formal suspension and cancellation need their statutory treatment; do not assume a silent cessation cancels registration. [Code arts. 114,115,118,113](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Art. 108 starts with delivery/service performance, but applies earlier invoice/payment rules, including advances. Goods transport normally starts the tax point, export uses removal from Moldova, and real-property supply uses registration of ownership. Regular utilities/rent use the earlier contractual delivery or regular payment; leasing uses contractual payment dates or an earlier advance. Successive-payment works/services follow acceptance/certification or contractual acceptance. Special insolvency/secured-property timing must be applied to its own branch. For imports, art. 109 sets customs timing for goods and the earlier service import/payment (including advance) for services. For unregistered service importers, pay by the 25th after that earlier month; specified property-acquisition payment timing is separately in 115(2)(c). [Code arts. 108–109,115(2)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

Issue fiscal invoices at the statutory tax point unless an express exception applies. Art. 117(2) specifies supplier/customer identity, fiscal codes, issue/supply dates, description/quantity, unit price excluding VAT, rate, total and tax, plus “Taxare inversă” where required. Export and specified retail/consumer/digital exceptions do not replace the underlying records. E-factura is mandatory for the statutory SFS-list cases and the specified public contracts, principal petroleum, relevant counterparties without fiscal-budget relations and assistance-project transactions, subject to each exception. Art. 117^1 permits the specified accompanying-note, services/petroleum and business-card e-invoice timing through the 10th of the next month; do not turn that invoice timing into a later output-tax point. [Code arts. 117–117^1](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

### Current VAT12 mapping

Use Order 1164/2012 annex 2, consolidated through Order 529/2025. The latter applies to reporting periods from January 2026. The ordinary declaration has 24 boxes. [Instructions](https://www.legis.md/cautare/getResults?doc_id=151641&lang=ro), [Order 529 point 2](https://www.legis.md/cautare/getResults?doc_id=151607&lang=ro).

| Box | Current content / control | Instruction point |
|---|---|---|
|1 /2|Standard domestic taxable supply base / output VAT, including taxable advances and adjustments|3.2–3.3|
|3 /4|Reduced-rate domestic supply base / output VAT, including taxable advances and adjustments|3.5–3.6|
|5|Supplies exempt with credit, excluding advances|3.7|
|6|Supplies exempt without credit, excluding advances, including relevant value adjustments|3.8|
|7 /8|Imported/procured services and the specified 2026 energy reverse-charge operations / their calculated VAT|3.9–3.10|
|9 /10|The specified insolvent/secured property, capital-relief clawback and specified non-budget-relations utility base / calculated tax|3.10^2–3.10^3|
|11|Output VAT corrections, statutory bad-debt and qualifying promotion adjustments|3.11|
|12|Total supply base =1+3+5+6|3.12|
|13|Total output VAT =2+4+8+11; **does not include 10**|3.13|
|13.1|Included VAT on advances not followed by supply in that same period; not another additive liability|3.14|
|14 /15|Ordinary domestic purchase base / **eligible** VAT;14 can also include purchases without credit, 15 cannot|3.15–3.16|
|16 /17|Imports and the listed procured goods/services, including qualifying energy operations / eligible VAT and customs adjustments|3.17–3.18|
|18|Input corrections including bad debt, definitive annual prorata and construction adjustments|3.19|
|19|Prior box 23 plus prior box 24 not requested/accepted for refund, subject to the actual opening reconciliation|3.20|
|20|Total available deduction =15+17+18+19|3.21|
|21|Positive ordinary liability =13−20; otherwise blank/zero as the form requires|3.22|
|22|Separate budget liability equal to 10; it is not netted away through 13−20|3.23|
|23|Remaining eligible carryforward =20−13−24 when positive|3.24|
|24|VAT actually requested for refund under a supported statutory route|3.25|

All table mappings: [Order 1164 annex 2 points 3.1–3.25](https://www.legis.md/cautare/getResults?doc_id=151641&lang=ro). The energy additions to 7/8/16/17 do not move those operations into the separate 9/10/22 property route merely because both are called reverse charge.

Attach TVA FACT (received fiscal invoices) and TVA LIVR (issued fiscal invoices) under points 4,5,5^1, including relevant compensated-cost refacturing and excluding the specified “Nonlivrare” redirection documents. The 102(12) prior-supply-month invoice can appear in the receipt or deduction-period annex as the instruction permits; retain a reconciliation to avoid double credit. Nonregistered service importers complete 7/8/21 without registered-payer credit; the separate property/clawback cases use 9/10/22 under point 7. [Instructions](https://www.legis.md/cautare/getResults?doc_id=151641&lang=ro).

Point 8 prevents submission for a future/missing period, failure of the 12/13/20 arithmetic checks, missing annex counterparty/date/invoice identity, or invoice numbers not allocated to the issuer. A prepared form is not a filed return: retain successful submission acknowledgement and separate payment evidence. A corrected return follows the original period's valid form and art. 188's six-year limit and audit restrictions; distinguish a later-period statutory adjustment from correction of a mistaken original entry. [Order 1164 annex 2 point 8](https://www.legis.md/cautare/getResults?doc_id=151641&lang=ro), [Code art. 188](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

### Working paper and classification controls

Use these supplier patterns as **search prompts**, not legal defaults: MAIB/Moldova Agroindbank, Victoriabank, MICB/Moldindconbank, Mobiasbanca and Eximbank; SFS/Vama/CNAS/ASP; Moldovagaz/Moldelectrica, Apa-Canal, Moldtelecom/Orange/Moldcell; Moldasig/Grawe/Donaris; Linella/NR1/Metro/restaurants; Google/Microsoft/Adobe/Meta/Slack/Zoom/Notion/AWS/Anthropic/OpenAI; notaries/auditors/accountants/lawyers; salary/dividend/internal/cash movements. Inspect the actual legal supplier and service. “Bank” does not prove a financial exemption, “government” does not prove every fee has identical VAT treatment, “water/electricity” does not determine residential purpose, “restaurant” does not prove private use, and “SaaS” does not establish the customer's status or supplier's location. The governing tests are arts. 93–104,111 and 102, not the narrative pattern.

A bank statement is a discovery/reconciliation input. Obtain fiscal invoices, contracts, registers, prior return/credit/refund decisions, customs declarations/tax proof, supplier/customer IDNO and registration dates before concluding the return. Record original and MDL amounts, conversion source/date, supply/advance/invoice/receipt/customs dates, actual legal rate/exemption article, business-use attribution, input evidence, box and adjustment history. Track withheld bank charges, settlements and internal transfers separately. A loan's principal, an ATM withdrawal or a salary payment is not automatically a taxable invoice. Useful Romanian discovery terms: salariu, dobândă, credit/împrumut, numerar, intern, vamă, asigurare and contabil. [Code arts. 93–95,102,108–111,118](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

The default domestic country, automatic 20%, automatic foreign-receipt exemption, fuel 0%, automatic rent exemption and blanket mixed-activity refusal are replaced by documented classification or an unresolved item. In particular, MDL 288 net imported SaaS yields MDL 57.60 at 20%, rather than an unexplained 58; a proven MDL 450 VAT-inclusive taxable telecom invoice splits 375/75; a proven MDL 1,620 VAT-inclusive 8% gas invoice splits 1,500/120. A payment labelled MDL 12,000 “import TVA” is not evidence of a MDL 10,000 customs base and MDL 2,000 tax. Classify the foreign IT receipt and dinner only after the legal tests above. These are corrections to legacy fixtures, not additional filing examples or verified client facts.

## Penalties and interest

**Calendar-2026 ordinary tax late charge.** Code art. 228(3) and the BNM decision of 6 November 2025, point 1, supply the calculation: the retained **6.00%** short-term policy rate, rounded up to a whole percent, plus **5 percentage points**, divided by **365 days**, gives **0.0301% per delayed day** after rounding the daily percentage to four decimal places. The decimal multiplier is **0.000301**. Apply it to the established outstanding principal for each chargeable day; split changes in principal and calendar year. This calculation concerns debts governed by art. 228 and does not replace a separate statutory regime's rate or establish case-specific relief. [Code art. 228(2)–(3)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); [BNM decision, point 1](https://bnm.md/en/node/69226).

For legal-person/business categories in art. 232(a),(c), art. 260(1) sets reporting-preparation/presentation fines of MDL 500–1,000 per return, capped at MDL 10,000 for all returns; the distinct nonbusiness-individual category has MDL 200–400, capped at MDL 2,000. Failure to issue a required fiscal invoice within arts. 117/117^1 timing is MDL 3,000–3,600 per invoice, capped at MDL 72,000 under 260(4). Late/nonregistration as a VAT payer is 7%–10% of taxable supply volume excluding art. 104 supplies under 256(7); where this fine is applied, 261(5) is not also applied. Do not treat those ranges as a discretionary minimum automatically selected by software. [Code arts. 232,256(7),260](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

False-data understatement is 20%–30% of the understated amount under 261(4); genuine self-correction under 188 is excepted by 261(4^1). Evasion under 261(5) is 80%–100% of undeclared tax, subject to the non-cumulation just described. Late-payment interest under 228 runs from the day after due date through actual payment; its annual formula uses the prior-November BNM base rate rounded up to a whole percent, plus 5 points, divided by days in the year and rounded to four decimals. Additional-liability self-correction interest is capped at the corresponding tax under 228(2^1). Determine the correct case-specific relief/audit treatment; do not substitute the social-contribution 0.1% rate for ordinary VAT late charges. [Code arts. 228,261,188](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

**An excessive refund has its own interest period.** Under article 228(10), the late charge applies to the **amount refunded in excess**, including an excess found after repeated control. It runs from the actual refund to the business’s bank/payment account, or the stated budget-debt extinguishment, through recovery. Do not use the refund-request date or charge the lawfully refunded portion merely because the overall claim was examined. This is separate from the ordinary original-tax due date. [Code 228(10)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro); existing ledger 286.

### Assessment, collection and refund limitation

Use **current Code 264’s statutory start dates**, rather than the actual date a late return/payment was made. Under 264(1)(a), tax and late charges can be determined within **four years from the last statutory filing date**, or the payment due date if no return is prescribed. Tax-specific sanctions use the corresponding statutory filing/payment date under 264(1)(b); sanctions unrelated to a particular tax use the offence date under 264(1)(c). Paragraph 2 is repealed. Under 264(3), SFS can extend the period subject to control, **not beyond six years from the last statutory filing date**, where no return was submitted or the taxpayer seeks an overpayment/statutory refund. These are conditional powers and clocks, not a universal six-year assessment period. [Code 264](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), read 31 October 2026.

**Collection is separate.** For an obligation determined within 264, 265(1) requires the specified enforcement action/court referral within six years after determination. The clock is subject to 265(2)’s suspension circumstances, resumes when the circumstance ends under 265(3), and is interrupted under the Civil Code with a fresh period under 265(4)–(5). The suspension list covers the stated detention/absence, deferral/instalment, court, insolvency, special-record and enforcement circumstances. Do not infer expiry solely by adding six calendar years; the applicable Civil Code interruption grounds and case-specific event dates still require verification. [Code 265](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

**An offset/refund application has its own clock.** Under 266(1), apply within six years from the relevant payment/arising of the amount; filing suspends that period. A late application is invalid unless SFS reinstates/accepts it under 266(2) on evidence that the taxpayer could not comply. Unclaimed amounts are cancelled under the Government procedure in 266(3), whose detailed implementation is not supplied here. This time limit does not itself prove a substantive credit/refund entitlement. Retain statutory due dates, actual filings/refund applications, determination/enforcement dates, suspension/interruption evidence and decisions separately. [Code 266](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

## Cross-border points

Determine place before exemption. Art. 110 distinguishes untransported goods, customer/third-party transport, supplier transport and the special energy-trader/consumption rules. Art. 111 places real-property-related services at the property, transport along the route/distance, the listed cultural/educational/tangible-property/auxiliary activities where actually performed and tangible-property hire where used/possessed. The listed IP, advertising, consultancy/legal/accounting/marketing/information/IT/personnel/agency services follow the recipient's establishment/residence; communications/broadcast/electronic services also follow their specified recipient rule. The residual rule is the supplier's establishment/residence. Do not import an EU-wide general B2B rule into every Moldova service. [Code arts. 110–111](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

A nonresident supply whose place is Moldova is an imported service under 93(9); apply 94(c),109(2),101/102 and 115 rather than relying on the merchant label. Conversely, export of services requires a nonresident recipient and a place outside Moldova under 93(11), then the applicable 104(a) treatment/evidence. A German payer or foreign-currency receipt alone is insufficient. For nonresident automated consumer e-services, 111(5) tests residence, payment-account/provider location, IP or country telephone prefix; one condition suffices. Email consultancy and online ordering followed by offline delivery are expressly outside the automated e-services definition in 95(1^1), although other place rules can still apply. [Code](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro).

FromJanuary 2026, arts. 101(1^1)–(1^2),104(b^1),110(4)–(5),111(1)(g),112(4^1) and 101^7 establish the specified network-energy rules. For domestic electricity/gas supplies between VAT-registered persons, 101^7 requires the buyer's statutory trader status: the relevant licence/operator category, principal resale activity and own use no more than 1%. Supplier invoices say “Taxare inversă” without VAT; the buyer records calculated output and input. A supplier charging tax incorrectly creates a lost input right until corrected under 101^7(5); an ineligible buyer requires cancellation/reissue under(6). The annual January–November own-use declaration has a Ministry-prescribed procedure still unconfirmed here. Purchases from a foreign energy seller under 101(1^1) use the invoice/primary-document date and must not be counted a second time upon subsequent customs import. [Code arts. 101,101^7](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [January commencement notes](https://www.legis.md/cautare/getResults?doc_id=149766&lang=ro), [Order 529](https://www.legis.md/cautare/getResults?doc_id=151607&lang=ro).

DCFTA/customs-origin relief is not by itself an exemption from Moldova import VAT. Use the customs taxable value/rate/exemption and proof for the actual goods. Goods/services involving residents without fiscal relations with Moldova's budget need the applicable implementing-law/customs analysis and e-invoice/return route; blanket “Transnistria out of scope” is insufficient. The ordinary reporting branches are retained above, while the full 2026 transitional regime, DCFTA origin procedure and treaty/project-specific evidence remain unconfirmed below.

## Two worked examples that recompute

### 1. Ordinary registered payer, imported service and customs input

Assume a wholly taxable registered business, in an ordinary 2026 month, with supported standard domestic sales MDL 100,000, qualifying 8% domestic sales MDL 50,000 and documented exempt-with-credit exports MDL 20,000. All amounts exclude VAT unless stated. Eligible domestic purchases are MDL 30,000+6,000 VAT. Customs goods have a confirmed customs VAT base MDL 15,000 and paid tax MDL 3,000, with no additional taxable charges; an imported business software service has MDL 2,000 base and 400 calculated VAT. Every credit meets 102; no 9/10 property transaction, advances, corrections or refund request; reconciled prior credit MDL 1,000. [Code arts. 96,100–102,104,109; Order 1164 points 3.2–3.25](https://www.legis.md/cautare/getResults?doc_id=151641&lang=ro).

```oa-check
name: Moldova VAT12 ordinary return with imports
tolerance: 0.0001
inputs:
  standard_sales: 100000
  reduced_sales: 50000
  exports: 20000
  domestic_base: 30000
  customs_base: 15000
  import_service_base: 2000
  opening_credit: 1000
  box6: 0
  box9: 0
  box10: 0
  box11: 0
  box18: 0
  box24: 0
steps:
  box1: standard_sales
  box2: box1 * 0.20
  box3: reduced_sales
  box4: box3 * 0.08
  box5: exports
  box7: import_service_base
  box8: box7 * 0.20
  box12: box1 + box3 + box5 + box6
  box13: box2 + box4 + box8 + box11
  box14: domestic_base
  box15: domestic_base * 0.20
  box16: customs_base + import_service_base
  box17: customs_base * 0.20 + box8
  box19: opening_credit
  box20: box15 + box17 + box18 + box19
  box21: max(box13 - box20, 0)
  box22: box10
  box23: max(box20 - box13 - box24, 0)
  total_payment: box21 + box22
expected:
  box12: 170000
  box13: 24400
  box16: 17000
  box17: 3400
  box20: 10400
  box21: 14000
  box22: 0
  box23: 0
  total_payment: 14000
```

The service has both 400 output and 400 eligible input; its credit is not a cash remittance for that transaction. The ordinary return reconciles to MDL 14,000 payable, separately from the already-paid MDL 3,000 customs tax.

### 2. Mixed activity and the definitive annual adjustment

Assume standard taxable monthly supplies MDL 80,000 and exempt-without-credit supplies MDL 20,000, no advances. Supported direct taxable input VAT is MDL 10,000, direct exempt input 2,000, private input 500 and shared input 5,000. Monthly ratio 0.80 is exact, so shared credit 4,000 and current-period credit 14,000; a proved opening credit 2,000 offsets the ordinary 16,000 output. For the annual adjustment, assume this is the year's entire shared-input pool and later sales bring relevant annual taxable/exempt totals to 300,000/100,000. The exact definitive ratio 0.75 allows 3,750 shared credit, requiring a **250 reduction** of prior credit in the final-period box 18; other final-period transactions are not computed here. A 4% exempt share is below the statutory boundary; exactly 5% is not. Those boundary statements do not extend credit to private or exclusively exempt purchases. [Code 102(2)–(4)](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro), [Order 1164 point 3.19](https://www.legis.md/cautare/getResults?doc_id=151641&lang=ro).

```oa-check
name: Moldova mixed-input monthly and definitive annual prorata
tolerance: 0.0001
inputs:
  taxable_month: 80000
  exempt_month: 20000
  direct_taxable_vat: 10000
  direct_exempt_vat: 2000
  private_vat: 500
  shared_vat: 5000
  opening_credit: 2000
  annual_taxable: 300000
  annual_exempt: 100000
steps:
  monthly_ratio: taxable_month / (taxable_month + exempt_month)
  exempt_share: exempt_month / (taxable_month + exempt_month)
  shared_credit: shared_vat * monthly_ratio
  eligible_current: direct_taxable_vat + shared_credit
  blocked_current: direct_exempt_vat + private_vat + shared_vat - shared_credit
  output_month: taxable_month * 0.20
  payable_month: max(output_month - eligible_current - opening_credit, 0)
  annual_ratio: annual_taxable / (annual_taxable + annual_exempt)
  annual_shared_credit: shared_vat * annual_ratio
  final_period_input_adjustment: annual_shared_credit - shared_credit
expected:
  monthly_ratio: 0.80
  exempt_share: 0.20
  shared_credit: 4000
  eligible_current: 14000
  blocked_current: 3500
  payable_month: 0
  annual_ratio: 0.75
  annual_shared_credit: 3750
  final_period_input_adjustment: -250
```

## Ask the client first

- What is the legal entity/activity, IDNO, actual VAT registration/effective date, and any cancellation, reorganisation, formal suspension or chapter 10^4 status? Which consecutive 12 month supplies and imported services trigger the relevant dated registration test? Were any obligations already triggered before a threshold change?
- What is supplied, to whom and where? Obtain contracts, tariff/product evidence, actual customer/supplier establishments and property/use locations, not just a merchant narrative. Which supplies are standard/reduced, exempt with credit, exempt without credit or non-objects? What proves the particular education, medical, justice, finance, residential, export or project condition?
- Obtain invoices and actual receipt dates, customs declarations and paid-tax evidence, advances and acceptance records, returns/discounts/bad debts, business-card fiscal receipts and the business/private attribution.
- What is directly taxable/exempt/shared, including construction projects, cars by qualifying user, entertainment, gifts, destruction, changed use and capital-relief disposals?
- What opening credit, prior refund request/decision, arrears and earlier corrections must reconcile? Supply the filed return, annexes, receipt and payment record.
- Are there nonresident consumer electronic services, energy-trader licences/own-use conditions, insolvency/security property, cross-Nistru fiscal-status issues, free-zone movements or a claimed customs/DCFTA relief requiring the separate procedure?

## Sources

**Bounded source review, 31 October 2026.** The [independent review record](../../evidence/ledgers/md-country-evidence/independent-review/FINAL-REVIEW.md) covers the stated source/claim scope. Ordinary gaps below remain unresolved. This Guide remains a source-cited draft, without accountant attestation or comprehensive coverage.

| Primary source actually read | Scope | Read date |
|---|---|---|
| [BNM monetary-policy decision, 6 November 2025, point 1](https://bnm.md/en/node/69226) | Fetched 6.00% short-term base input; calendar-2026 daily percentage derived with Code 228(3), rather than copied from an old rate. | 2026-10-30 |
|[Fiscal Code current consolidation 157050](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro)|Selected arts. 93–118 and contained superscript articles; 232,256,260–261,228,188. Current TVA scope/base/credit/exemption/place/timing/reporting and penalties; not a claim to have audited the entire Code|2026-10-30|
|[January consolidation 149766](https://www.legis.md/cautare/getResults?doc_id=149766&lang=ro)|Arts. 96,104,112 and retained energy commencement notes. Jan–Feb threshold and pre-May medical-device wording|2026-10-30|
|[Law 12/2026](https://www.legis.md/cautare/getResults?doc_id=153159&lang=ro)|ArtsI–II;1 March 2026 registration threshold change|2026-10-30|
|[May consolidation 153671](https://www.legis.md/cautare/getResults?doc_id=153671&lang=ro), [Law 41/2026](https://www.legis.md/cautare/getResults?doc_id=153667&lang=ro)|Art. 96 and the Law 41 medical-device amendment/1 May commencement; remaining tariff-based reduced categories retained|2026-10-30|
|[Order 1164/2012 current consolidation 151641](https://www.legis.md/cautare/getResults?doc_id=151641&lang=ro)|Full annex 2 text: ordinary 24 boxes, annexes, unregistered routes and critical submission errors. Linked annex 1 DOCX not retrieved|2026-10-30|
|[Order 529/2025](https://www.legis.md/cautare/getResults?doc_id=151607&lang=ro)|Energy box 7/8/16/17 amendments, applicability from January 2026 periods|2026-10-30|

| Source | Read scope | Read on |
|---|---|---|
| [Current Code 264–266](https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro) | Full assessment, collection and refund-limitation provisions read; clocks, statutory start dates and conditional extensions separated. Historical/Civil Code/Government implementation gaps remain | 2026-10-31 |

Not yet confirmed: full 2026 amendment-by-amendment commencement reconciliation beyond the dated changes above; actual late-registration assessment period and procedural relief; non-exact prorata rounding representation in SFS practice; Government refund application/proof/limits and 2026 refund-programme amendments; Government capital-contribution, destruction, assistance-project/free-zone/processing and other specialist exemption procedures; full 2026 cross-Nistru transitional law/customs and DCFTA origin procedures; current Ministry energy-trader own-use declaration procedure; current nonresident e-services registration/form/payment implementation; foreign-currency VAT conversion date and supporting BNM rule; case-specific late-charge relief/account allocation; current annex 1 TVA12 DOCX/layout and authenticated portal validation/rounding; counterparty-specific status, bank-export conventions and the legal assumptions of legacy transactions. These gaps remain explicit and this VAT draft does not establish comprehensive country coverage or accountant attestation.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
