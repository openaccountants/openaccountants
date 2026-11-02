---
name: sm-vat-gst
description: >
  San Marino indirect tax for 2026. San Marino has no VAT; it charges a single-stage import tax (imposta monofase) on goods and connected services brought into the Republic, under Law 40/1972. Covers who pays, the taxable base, the ordinary 17% rate, the Decree 108/1997 reduced and increased tables (2%, 6%, 10% and 21%) and the 5% energy-saving Table E, the network-utility exemption, the separate special import tax on fuels, the services tax on private customers (imposta complementare sui servizi), the 1% capital-goods rate and its vehicle, rental and retention rules, used goods, export refunds, the Italy-San Marino electronic invoicing exchange through SDI under the Italian decree of 21 June 2021, and the domestic e-invoicing transition under Delegated Decree 133/2026 (optional from 1 October 2026, required from 1 January 2027, penalties from 2028). Use for San Marino VAT, monofase rate, import tax, trading with Italy, San Marino e-invoice and capital-goods questions.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.4
---

# San Marino monofase import tax and the VAT interface with Italy v0.4

Tax year: calendar year 2026. Currency EUR. Authority: UO Ufficio Tributario (Tax Office). San Marino has no value added tax. The Finance department lists the single-stage import tax (monofase) and related levies as the domestic indirect-tax system ([Finance department][finance]). The `vat-gst` file name is kept for compatibility.

## 1. Who this applies to

- **Taxable event.** Import tax is charged on goods and connected services imported into San Marino ([Law 40/1972, arts 1-4][l40]).
- **Who pays.** The importer. Those on whose behalf the goods are imported and those who physically bring them in are jointly liable ([Law 40/1972, art 5][l40]).
- **Not taxable.** Money and money claims, securities and stamps, imports by State bodies, contractual discounts in kind and returnable packaging ([Decree 108/1997, art 2][d108]).
- **Domestic sales** between San Marino operators carry no import tax; from 2027 they need an electronic invoice (section 4).
- **Trade with Italy** follows the Italian decree of 21 June 2021: Italian VAT rules apply on the Italian side, monofase on the San Marino side.

## 2. Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Ordinary import tax rate | 17% of the taxable base, for operations from 1 January 2012 | 2026 | [DD 183/2011, arts 1-2][dd183] |
| Table A goods (listed basic foods and other items) | 2% | 2026 | [Decree 108/1997, art 1 and Table A][d108] |
| Table A item 23-ter added: feminine hygiene pads, tampons and cups | 2%, on imports from 1 August 2026 (Table B item 95-bis repealed) | 2026 | [DD 98/2026, arts 1-2][dd98] |
| Table B goods (listed foods and other items) | 6% | 2026 | [Decree 108/1997, art 1 and Table B][d108] |
| Table C petroleum products, lower band (agricultural fuel, domestic LPG 10-20 kg, industrial heating oil) | 10% | 2026 | [Decree 108/1997, Table C][d108] |
| Table C petroleum products, upper band (road and heating diesel, automotive LPG, petrol, lubricants and all other petroleum products) | 21% (raised from 20%) | 2026 | [DD 183/2011, art 1][dd183] |
| Table E goods (listed energy-saving and renewable-energy goods, such as photovoltaic panels and inverters, solar thermal panels, condensing boilers) | 5% from 1 July 2009 (9% when the table was created in 2008) | 2026 | [DD 133/2007, art 1 and Table E][dd133e]; [DD 87/2009, art 3][dd87] |
| Natural gas, electricity and drinking water supplied through the public network | Exempt from import tax from 1 January 2012 | 2026 | [Decree-Law 124/2011, art 2, as ratified by Decree-Law 149/2011][dl149] |
| Fixed tax per document (commissions, free samples, newspapers and books, collector coins, listed scrap metal bought in the EU) | 4,000 lire per document (euro amount not stated in the text read) | 2026 | [Decree 108/1997, art 3][d108] |
| Used goods, art and antiques bought in the EU by a business | Tax on 50% of the base | 2026 | [Decree 108/1997, art 4][d108] |
| Used vehicles taken from private persons, when registered in San Marino; collector items and coins | Tax on 10% of the base | 2026 | [Decree 108/1997, art 4][d108] |
| Capital goods directly used in business by licensed operators | 1%, if unit value over 250, or homogeneous purchases with a base over 500 | 2026 | [Decree 135/2003, arts 1-3][d135] |
| Business cars for mixed use | 7%, one car per licence (plus one per co-holder and per 5 permanent staff, up to 20); not open cars over 2,000 cc or closed cars over 2,000 cc with fewer than 5 seats | 2026 | [Decree 135/2003, art 4][d135] |
| Goods for rental without driver | 9% motor vehicles, 2% aircraft, 6% boats | 2026 | [Decree 135/2003, art 5][d135] |
| Building works and installations for new hotel and restaurant projects | 6% (other property is excluded from the capital-goods rates) | 2026 | [Decree 135/2003, art 6][d135] |
| Capital-goods retention period | 12 months from delivery or registration; 2 years for mixed-use cars | 2026 | [Decree 135/2003, art 7][d135] |
| Domestic e-invoicing exclusion | Operators with prior-year declared revenue below 100,000 (they can opt in) | 2027 | [DD 133/2026, art 2(2)][dd133] |
| Domestic e-invoicing penalty | 100 per violation, from 1 January 2028 | 2028 | [DD 133/2026, arts 6, 11(4)][dd133] |
| Italian supplier's invoice not validated by the San Marino Tax Office | Italian supplier issues a credit note within 30 days after 4 months from issue | 2026 | [Italian DM 21 June 2021, art 3(3)][italy] |

## 3. The base

**Starting point.** The base is the total consideration due to the supplier ([Law 40/1972, art 3][l40]), plus exigible excise duties, levies and equivalent charges. Decree 50/1993 has separate exchange-rate and customs-value rules for imports from outside the EU customs territory and for purchases within it; where the price is missing or not the only consideration, use normal value ([Decree 50/1993, art 3][d50]).

**Rate.** Apply 17% unless the goods are listed in Table A, B or C, or a special decree applies ([DD 183/2011, art 1][dd183]; [Decree 108/1997, art 1][d108]). Classify by the exact table entry; the item lists have been amended many times since 1997 (for example DD 98/2026).

**Capital goods (1%).** Available to licensed economic operators, recognised agricultural cooperatives and registered professionals for material and intangible goods directly used in their activity ([Decree 135/2003, arts 1-3][d135]). Replacement parts qualify if over 5% of the asset's historical cost. Property and installations are excluded, except the 6% hotel and restaurant works ([Decree 135/2003, arts 1, 6][d135]). If the asset is sold before the retention period ends, the seller pays the difference between full import tax and tax already paid within 30 days, unless the buyer is itself entitled to the relief and keeps it for the remaining period, or the Finance secretariat authorises the sale ([Decree 135/2003, art 8][d135]). Mixed-use cars worth 10,000 or less can be sold freely, but no new relieved car for 6 months; rental firms can sell after nine months with notice ([Decree 135/2003, art 7][d135]). Non-profit volunteer associations pay 7% on cars and 1% on other goods with authorisation ([Decree 135/2003, art 9][d135]).

**Energy products.** Petrol, diesel, LPG, kerosene, fuel oils, lubricants and natural gas also carry a per-unit special import tax (imposta speciale sulle importazioni) under Law 42/1975, at amounts per litre or kg set by Delegated Decree 195/2011 and changed by later decrees; the latest read, DD 84/2025, cut petrol by 0.015 and raised road diesel by 0.015 per litre from 16 June 2025 ([DD 195/2011, art 1][dd195]; [DD 84/2025, arts 1-2][dd84]). This is separate from the Table C monofase rate.

**Services to private customers (imposta complementare sui servizi).** Listed services supplied by a San Marino economic operator to a private customer who is not an economic operator carry the imposta complementare sui servizi under Law 194/2010 article 48. The customer owes it; the supplier charges and pays it over as withholding agent. Covered services include legal, notarial, accounting, tax and engineering advice, translation and private teaching, maintenance and repair, installation and transport connected with a sale, building and installation work (on the price net of materials), cleaning and gardening, and property and commercial intermediation ([DD 50/2011, arts 2-11][dd50]). Private health services are outside it from 1 January 2012 ([Decree-Law 149/2011, art 3][dl149]). Business-to-business services do not carry it.

**Export refunds.** Monofase is single-stage, so there is no input-tax credit. A San Marino business that exports previously imported goods (to Italy or elsewhere) can claim a refund of the import tax paid, under criteria set by separate administrative measure ([Law 40/1972, arts 9, 14][l40]). Keep the import tax receipt, the link between imported and exported goods (including transformation records), the export invoice and the customs or validation evidence.

## 4. Deadlines and filing

### Italy to San Marino (purchases from Italy)

Since 1 October 2021 the Italian decree of 21 June 2021 governs the exchange; since 1 July 2022 invoices for goods traded between Italy and San Marino must be electronic, except for operators not required to e-invoice in Italy ([Italian DM, arts 2, 22][italy]). The Italian supplier sends the e-invoice through SDI with the San Marino buyer's identification; the San Marino Tax Office checks that import tax has been paid and confirms validation, which the Italian supplier sees online ([Italian DM, art 3][italy]). If not validated within four months of issue, the Italian supplier issues a credit note within the following 30 days, without penalties ([Italian DM, art 3(3)][italy]). Paper invoices (where allowed) are issued in three copies and stamped by the Tax Office ([Italian DM, arts 4-5][italy]).

### San Marino to Italy (sales to Italy)

The San Marino seller's e-invoice goes through the San Marino Tax Office to SDI ([Italian DM, art 6][italy]). An invoice can carry Italian VAT, collected and paid through the specific route, or be issued without VAT, in which case the Italian business buyer self-accounts for VAT under reverse charge ([Italian DM, arts 7-8][italy]). Sales to private buyers, new means of transport, distance sales, non-commercial bodies and services have their own articles ([Italian DM, arts 13-16, 20][italy]).

### Domestic invoices between San Marino operators (DD 133/2026)

| Period | Rule | Source |
|---|---|---|
| 1 October to 31 December 2026 | Covered operators can choose to transmit domestic business invoices and credit notes electronically instead of on paper | [DD 133/2026, art 11(1)][dd133] |
| From 1 January 2027 | Electronic invoices required between economic operators (COE to COE), unless revenue in the prior calendar year was below 100,000; paper-invoice rules also start | [DD 133/2026, arts 2, 11(2)-(3)][dd133] |
| From 1 January 2028 | The article 6 and 7 penalties apply | [DD 133/2026, art 11(4)][dd133] |
| State, public administration and public bodies | When the implementing regulation enters into force | [DD 133/2026, art 11][dd133] |

An operator that exceeded 100,000 or opted in must keep using e-invoices in later years ([DD 133/2026, art 2(3)][dd133]). The invoice is prepared and transmitted by the second month after delivery or shipment (goods), completion (services) or payment (advances), with special rules for continuous supplies ([DD 133/2026, art 3][dd133]). An invoice rejected by HUB SM is treated as not issued ([DD 133/2026, art 4(3)][dd133]). The 100,000 test is an invoice-format rule, not a registration or tax threshold.

### Import documents

Decree 50/1993 articles 4 and 5 set the import document and control routes for purchases from outside and inside the EU ([Decree 50/1993, arts 4-5][d50]). Import tax is not filed on a periodic return.

## 5. Penalties and interest

- **E-invoicing:** 100 per violation for the article 6 failures, and the article 7 recipient self-documentation duty, both from 1 January 2028 ([DD 133/2026, arts 6-7, 11(4)][dd133]).
- **Early sale of relieved capital goods:** the full-rate tax difference is due within 30 days of the sale ([Decree 135/2003, art 8][d135]).
- **Italian side:** the Italian supplier's credit note after four months without validation carries no Italian penalties or interest ([Italian DM, art 3(3)][italy]).

## 6. Cross-border points

- Italy is San Marino's customs-union partner for goods traffic; the electronic exchange in section 4 replaces the 1993 paper procedure.
- Imports from other EU States and from outside the EU follow the Decree 50/1993 base and document rules ([Decree 50/1993, arts 3-5][d50]).
- Re-exports of imported goods give a refund of monofase under Law 40/1972 articles 9 and 14, not a credit.
- Services bought from abroad: classify first; only services connected with imported goods are within Law 40/1972 ([Law 40/1972, arts 1-5][l40]). Income-tax withholding on payments abroad is in `sm-cross-border`.

## 7. Two worked examples that recompute

### Example 1: ordinary import plus a Table A item

A shop imports goods with an ordinary taxable base of 10,000 and Table A goods with a base of 2,000. Ordinary tax 1,700; Table A tax 40; total 1,740.

```oa-check
name: San Marino 2026 ordinary and Table A import tax
inputs:
  ordinary_base: 10000
  table_a_base: 2000
  ordinary_rate: 0.17
  table_a_rate: 0.02
steps:
  ordinary_tax: ordinary_base * ordinary_rate
  table_a_tax: table_a_base * table_a_rate
  total_import_tax: ordinary_tax + table_a_tax
expected:
  ordinary_tax: 1700
  table_a_tax: 40
  total_import_tax: 1740
```

A single ordinary import with a base of 12,000 gives 2,040 of tax (14,040 with tax).

### Example 2: capital good sold early (edge case)

A licensed manufacturer imports a machine with a base of 50,000 at the 1% capital-goods rate: tax 500. It sells the machine after eight months to a private buyer, inside the 12-month retention period. Within 30 days it must pay the ordinary-rate tax less tax already paid: 8,500 - 500 = 8,000.

```oa-check
name: San Marino 2026 capital-goods import and early-sale top-up
inputs:
  asset_base: 50000
  capital_goods_rate: 0.01
  ordinary_rate: 0.17
steps:
  relieved_tax: asset_base * capital_goods_rate
  full_rate_tax: asset_base * ordinary_rate
  top_up_on_early_sale: full_rate_tax - relieved_tax
expected:
  relieved_tax: 500
  full_rate_tax: 8500
  top_up_on_early_sale: 8000
```

## 8. Ask the client first

1. What exactly is imported, from which country, and the tariff description of each item.
2. Who is the importer, and whether it holds a licence or professional registration (for the 1% route).
3. Invoice value, freight, duties and other charges, and the currency.
4. Whether the goods are kept, used in the business, sold on, or re-exported, and when.
5. For Italian trade: the counterparty's VAT number, whether invoices carry Italian VAT, and the validation status.
6. Prior-year revenue (for the 2027 e-invoicing obligation) and whether the operator opted in during 2026.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 40/1972 (import tax), arts 1-5, 9-17 | https://www.consigliograndeegenerale.sm/contents/instance18/files/document/19029leggi_2560.pdf | 2026-10-30 |
| Decree 50/1993, arts 3-5 (base, import documents) | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17021434.html | 2026-10-30 |
| Decree 108/1997, arts 1-4 and Tables A-D | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17022004.html | 2026-10-30 |
| Delegated Decree 183/2011, arts 1-2 (17% rate, Table C 21%) | https://www.consigliograndeegenerale.sm/on-line/home/documento17046854.html | 2026-10-30 |
| Decree 135/2003, arts 1-11 (capital goods) | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17022916.html | 2026-10-30 |
| Delegated Decree 98/2026 of 27 July 2026 (Table A 23-ter) | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=e54431a0e32f941616323ba3300c13a32828e853 | 2026-10-30 |
| Delegated Decree 133/2026 (domestic e-invoicing), arts 2-11 | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=4d7f1ffcf645b166ffc567d328d888e43fcdd538 | 2026-10-30 |
| Italy, Ministerial Decree 21 June 2021 (Gazzetta Ufficiale 168 of 15 July 2021), arts 1-8, 13-16, 20-22 | https://www.gazzettaufficiale.it/eli/gu/2021/07/15/168/sg/pdf | 2026-10-30 |
| Delegated Decree 133/2007 (Table E, energy-saving goods) | https://faolex.fao.org/docs/pdf/smr76724.pdf | 2026-10-30 |
| Delegated Decree 87/2009, art 3 (Table E rate 5%) | https://faolex.fao.org/docs/pdf/smr89742.pdf | 2026-10-30 |
| Decree-Law 149/2011 (ratifying Decree-Law 124/2011), arts 2-3 | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17045584.html | 2026-10-30 |
| Delegated Decree 50/2011 (imposta complementare sui servizi), arts 2-11 | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17027521.html | 2026-10-30 |
| Delegated Decree 195/2011 (special import tax on energy products), art 1 | https://www.consigliograndeegenerale.sm/on-line/home/documento17047292.html | 2026-10-30 |
| Delegated Decree 84/2025 (petrol and diesel special import tax), arts 1-2 | https://www.consigliograndeegenerale.sm/on-line/home/documento17152660.html | 2026-10-30 |
| Delegated Decrees 6/2023 and 118/2023 (Table A items 13-bis and 23-bis, Table B item 58) | https://www.consigliograndeegenerale.sm/on-line/home/documento17137375.html | 2026-10-30 |
| San Marino Finance department, national taxation page | https://www.finanze.sm/pub2/FinanzeSM/FISCALITA-NAZIONALE.html | 2026-10-24 |

Not yet confirmed: whether Decree 108/1997 Table A and B rates, the Table E rate and Decree 135/2003 rates were changed by decrees not found in this review (DD 6/2023, DD 118/2023 and DD 98/2026 only moved items between tables); the current per-litre and per-kg amounts of the special import tax on energy products; the rate and current list of services for the imposta complementare sui servizi (a Finance department report on a postal-services decree, after 2015, gives 3%), and DD 152/2025 changes to its exemptions; the euro amount of the fixed per-document tax; the 3.5% used-vehicle rate in the earlier version of this skill; the export-refund rates, forms and time limits; import-tax payment due dates; the registration an importer needs before clearing goods (economic-operator code); Regulation 28/2026 technical rules for HUB SM.

[l40]: https://www.consigliograndeegenerale.sm/contents/instance18/files/document/19029leggi_2560.pdf
[d50]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17021434.html
[d108]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17022004.html
[dd183]: https://www.consigliograndeegenerale.sm/on-line/home/documento17046854.html
[d135]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17022916.html
[dd98]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=e54431a0e32f941616323ba3300c13a32828e853
[dd133]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=4d7f1ffcf645b166ffc567d328d888e43fcdd538
[italy]: https://www.gazzettaufficiale.it/eli/gu/2021/07/15/168/sg/pdf
[finance]: https://www.finanze.sm/pub2/FinanzeSM/FISCALITA-NAZIONALE.html
[dd133e]: https://faolex.fao.org/docs/pdf/smr76724.pdf
[dd87]: https://faolex.fao.org/docs/pdf/smr89742.pdf
[dl149]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17045584.html
[dd50]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17027521.html
[dd195]: https://www.consigliograndeegenerale.sm/on-line/home/documento17047292.html
[dd84]: https://www.consigliograndeegenerale.sm/on-line/home/documento17152660.html

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
