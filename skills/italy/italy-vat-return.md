---
name: italy-vat-return
description: >
  Use this skill whenever asked to prepare, review, or classify transactions for
  an Italian VAT return (Liquidazione IVA Periodica / LIPE) for a self-employed
  individual or small business under the regime ordinario in Italy. Trigger on
  phrases like "prepare LIPE", "Italian VAT return", "Liquidazione IVA", "IVA
  italiana", "classify transactions for Italian VAT", or any request involving
  Italy VAT filing. Covers Italy only, regime ordinario, monthly or quarterly
  settlement, for 2026 periods under DPR 633/1972; the Testo unico IVA applies
  from 1 January 2027 and is not mapped here. Regime forfettario, regime dei
  minimi, split payment, margin schemes and VAT groups are refused. MUST be
  loaded alongside BOTH vat-workflow-base AND eu-vat-directive. ALWAYS read this
  skill before touching any Italian VAT work. This Tier 2 draft supports source
  checking and reviewer questions; it does not authorise filing, payment or a
  tax position.
version: 2.3
jurisdiction: IT
category: international
tax_year: 2026
tax_year_notes: "IVA periods in calendar 2026, read at 5 November 2026, under DPR 633/1972. The Testo unico IVA (D.Lgs. 10/2026), the sanctions Testo unico (D.Lgs. 173/2024) and the Testo unico on compliance and assessment (D.Lgs. 141/2026) apply from 1 January 2027 and are not mapped. Filings made in 2027 for 2026 periods are held on that point."
last_updated: 2026-11-05
tier: 2
depends_on:
  - vat-workflow-base
  - eu-vat-directive
job: vat-return
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: vat-gst
---

# Italy VAT Return v2.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

<!-- einvoice-xref -->
> **This pack has a separate e-invoicing guide: `italy-einvoice`.** This guide does not
> cover it. Where a jurisdiction operates a mandatory electronic-invoicing or
> real-time-reporting regime, the obligations and any consequences for input-tax
> recovery sit in that guide - read it alongside this one before filing or advising.
> **No claim about that jurisdiction's regime is made here**; this is a pointer only.

## Who this applies to

This section is in the child skill `italy-vat-return-reference`, moved there word for word so this file stays under the size limit. Load it with this skill.

## Rates, bands and thresholds

Rates are for 2026 periods. Each row leads with the official text. 'Administered' means an Agenzia statement where the statute reads differently.

| Item | Amount or rule | Position at 5 November 2026 | Official source |
| --- | --- | --- | --- |
| Standard rate | 22% | In force, art 16(1) | [DPR 633 art 16](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art16!vig=) |
| Reduced rate, Tabella A Part II | 4% | In force, art 16(2), subject to art 34. Tabella A headings print 2% and 9%: the rates are those in art 16. | [DPR 633 art 16](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art16!vig=) and [Tabella A in the act](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633!vig=) |
| Reduced rate, Tabella A Part II-bis | 5% | In force, art 16(2) | same |
| Reduced rate, Tabella A Part III | 10% | In force, art 16(2) | same |
| Non imponibile | No IVA charged, right of deduction kept. The legacy '0% rate' label is replaced: arts 8, 8-bis and 9 and art 41 use 'non imponibile'. | In force | [DPR 633 art 8](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art8!vig=); [D.L. 331 art 41](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art41!vig=) |
| Esente | No IVA charged, no deduction on related costs (art 19(2)) | Art 10, in force | [DPR 633 art 10](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art10!vig=) |
| Quarterly option limit, services and professions | Volume d'affari of the prior calendar year not above EUR 500,000 | Administered. DPR 542/1999 art 7(1) still prints lire 600 million. The amending act was not found. | [Agenzia, Come pagare l'IVA](https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva-imprese); [DPR 542 art 7](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1999-12-14;542~art7!vig=) |
| Quarterly option limit, other activities | Not above EUR 800,000. Without separate records of mixed activities, this limit applies to all of them (art 7(2)). | Administered. Art 7(1) prints lire 1 billion. | same |
| Quarterly interest | 1% on amounts to pay under the option | In force, art 7(3). Not on the acconto. Not for the special quarterlies. | [DPR 542 art 7](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1999-12-14;542~art7!vig=); [Agenzia, F24 IVA periodica](https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24ivap10/come-e-quando-si-versa) |
| Small periodic amount | Not paid if not above EUR 100; carried to the next period and in any case paid by 16 December (monthly) or 16 November (quarterly) | In force | [DPR 100/1998 art 1](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-03-23;100~art1!vig=); [DPR 542 art 7](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1999-12-14;542~art7!vig=) |
| Annual balance | Paid if above EUR 10.33 | Annual return instructions for 2025 | [Instructions, IVA 2026](https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711) |
| Acconto | 88% of the prior year's December, Q4 or annual payment, or of the current one if lower; analytic alternative. Not due below EUR 103.29. | L. 405/1990 art 6 prints 200,000 lire and older percentages. 88% comes from D.L. 155/1993 art 15(1), read only in the note to art 6. The VP13 instructions give EUR 103.29. | [L. 405/1990 art 6](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-12-29;405~art6!vig=); [LIPE instructions](https://www.agenziaentrate.gov.it/portale/documents/20143/5986193/IVA+period_2024.pdf/04990f53-edc9-048a-c953-49592ebea05f?t=1742281742832) |
| Refund minimum | In art 30(2) and art 34(9) cases the annual credit must be above EUR 2,582.28, but the refund may be requested for a lower amount. No minimum on cessation, or on the route through the 2 prior years' credits. | Art 30 prints lire 5 million; the annual instructions give the euro amount and these limbs, and number the cases as art 30(2) | [DPR 633 art 30](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art30!vig=); [Instructions, IVA 2026](https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711) |
| Refund above EUR 30,000 | Visto di conformita or alternative signature with a declaration, or guarantee in the art 38-bis(4) cases | In force, art 38-bis(3) and (4) | [DPR 633 art 38-bis](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art38bis!vig=) |
| Credit used in F24 | Above EUR 5,000 a year: only from the 10th day after filing the return or application showing it | In force, D.Lgs. 241/1997 art 17(1) | [D.Lgs. 241 art 17](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art17!vig=) |
| Annual offset limit | EUR 2,000,000 | Read only in the annual instructions, citing L. 388/2000 art 34(1) | [Instructions, IVA 2026](https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711) |
| Simplified invoice | Total not above EUR 100; not for art 41 intra-EU supplies or art 21(6-bis)(a) operations, where the customer is the debtor in another Member State (art 21-bis(2)) | In force | [DPR 633 art 21-bis](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art21bis!vig=) |
| Road motor vehicle, not exclusively business use | 40% deduction, art 19-bis.1(c), for road motor vehicles other than those in Tabella B letter (f). Vehicle: not above 3,500 kg and not above 8 seats excluding the driver. | In force; Tabella B not read | [DPR 633 art 19-bis.1](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19bis.1!vig=) |
| Representation goods | Deductible only for goods of unit cost not above EUR 50, art 19-bis.1(h) | In force | same |
| Depreciable goods test for IVA adjustments | Not depreciable if unit cost is not above 1 million lire, or if the income tax coefficient is above 25%, art 19-bis.2(5). EUR 516.46 is the income tax figure in TUIR art 102(5). | In force. The art 19-bis.2 text prints lire; the euro amount is read from TUIR. | [DPR 633 art 19-bis.2](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19bis.2!vig=); [TUIR art 102](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art102!vig=) |
| Intra-EU acquisitions by exempt persons | EUR 10,000 a year, D.L. 331/1993 art 38(5)(c) | In force | [D.L. 331 art 38](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art38!vig=) |
| Consumer sales within Italian IVA | EUR 10,000 a year, D.L. 331/1993 art 41(1)(b), on the conditions under Sales to EU consumers | In force | [D.L. 331 art 41](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art41!vig=) |
| Export periods | 90 days, art 8(1)(b); 180 days, art 8(1)(b-bis) | In force | [DPR 633 art 8](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art8!vig=) |

**What the 22% covers.** Every taxable supply not in Tabella A or another rule. The art 16(3) rule gives contracts d'opera and appalto, and finance lease and noleggio, the rate of the goods concerned.

**What the reduced rates cover.** These are the items the legacy file touched, with those near them, by Tabella A number. It is not the full Tabella: items left out here stay in it. Each item has its own wording and exclusions, so match the wording. A supplier's invoice settles what a buyer sees, not the law.

| Rate | Tabella A items | Official source |
| --- | --- | --- |
| 4% (Part II) | Milk (3); butter, cheese (4); vegetables and fruit (5 to 8); cereals and flours (9 to 11); olive and vegetable oils (13); margarine (14); pasta, crackers and bread (15); tomatoes (16); newspapers, books and periodicals, excluding pornographic items and catalogues (18); fertilisers (19); feed (20); houses other than A1, A8 and A9 on the prima casa conditions (21); rural buildings (21-bis); goods for building the listed houses (24); appalto for the same buildings (39); orthopaedic items, prostheses and invalid vehicles (30 to 33, 41-quater); canteens (37); barrier removal (41-ter) | [Tabella A in the act](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633!vig=) |
| 5% (Part II-bis) | Art 10 nn 18, 19, 20, 21 and 27-ter services by social cooperatives and their consortia and by imprese sociali to the n. 27-ter persons (1); fresh basil, rosemary and sage, oregano and the listed plants (1-bis); urban transport by sea, lake, river and lagoon (1-ter); the listed medical devices (1-ter.1); fresh or chilled truffles (1-quater); winter sports and alpine courses by registered instructors, where not exempt (1-septies); live horses not for food, sold by 31 December of the year after birth (1-octies); art, antiques and collectables in letters a, b and c of the D.L. 41/1995 table, where art 36 does not apply (1-novies) | [Tabella A in the act](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633!vig=) |
| 10% (Part III) | Meat (3 to 10); fish (10-bis); yoghurt (11); eggs (14); honey (16); spices (25); sugar (59, 60); chocolate (64); fine bakery (68); water and mineral waters (81); beer (82); electricity for domestic use, electricity and gas for extractive, agricultural and manufacturing businesses including printing and publishing, electricity for land reclamation consortia's irrigation and drainage plant, electricity to wholesale customers, and gas fed into distribution networks or to electricity producers (103); medicines (114); sanitary products (114.1); baby nappies (114.2); accommodation for guests of art 6 L. 217/1983 structures, with the other limbs of item 120; food and drink service, including vending, and appalto for it (121); theatre, concerts, circus and the other shows in item 123; methane for civil use up to 480 cubic metres a year, and LPG by network for cooking and hot water or in 10 to 20 kg cylinders (127-bis); passenger transport, excluding 1-ter and art 10 n. 14 (127-novies); extraordinary maintenance of public residential buildings (127-duodecies); goods for recovery works other than art 31(a) and (b) L. 457/1978 (127-terdecies); appalto for them (127-quaterdecies); the recovered buildings sold by the works firm (127-quinquiesdecies); waste and sewerage services (127-sexiesdecies); residential leases by builders and social housing (127-duodevicies); art 10 services by social cooperatives under contract (127-undevicies) | [Tabella A in the act](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633!vig=) |

Corrections to the legacy lists: spices are 10%, not 5%; the 5% food items are the named herbs, plants and truffles; item 127-septiesdecies is repealed (D.L. 95/2025).

**Renovation.** 10% on services for works under art 31(1)(a) to (d) L. 457/1978 on buildings mainly used as private housing (L. 488/1999 art 7(1)(b)), with 'significant goods' limited by decree. The date in that text is 2003; L. 191/2009 art 2(11) extends the rule by amending L. 244/2007 art 1(18), which was not read. Items 127-terdecies and 127-quaterdecies above are separate limbs.

## The base

IVA applies to supplies of goods and services made in Italy in the exercise of a business, art or profession, and to imports (art 1). The tax point follows art 6 and the base art 13. Art 15 leaves out of the base moratory interest and penalties for the customer's delay; goods given as a discount or premium under the original terms, unless at a higher rate; documented reimbursements of advances made in the customer's name and for its account; packaging with an agreed refund on return; and the IVA itself.

**Tax point, art 6.** Goods: movables on delivery or shipment, immovables on the contract. Services: on payment. An earlier invoice, or an earlier payment in whole or in part, fixes the point to that extent (art 6(4)), so a deposit is caught. A suspensive effect moves the point to when it occurs, and for movables within a year. For supplies to the listed public bodies, tax falls due on payment (art 6(5)). Cross-border B2B services fall when completed, on periodic accrual or on part payment (art 6(6)).

**Invoices, arts 21 and 22.** Issue within 12 days of the operation. Deferred invoice for the month's goods with a transport document, by the 15th of the next month. EU B2B services by the 15th of the next month (art 21(4)(c)), with non-EU ones under (d). Exempt or non imponibile invoices carry the art 21(6) annotation. Retail and the other businesses under art 22 issue an invoice only if asked no later than the time of the operation. E-invoice rules are in `italy-einvoice`.

**Deduction, art 19.** The right arises when the tax falls due. Since 12 August 2026 art 19(1) reads that it is exercised at the latest with the return for the second year after the year the right arose, and art 25 requires registration by the return for the second year after receipt of the invoice (D.Lgs. 148/2026 art 12). The articles of that decree read show no separate transition rule: treatment of rights that arose earlier is held. Not deductible: tax on exempt or non-taxed operations (art 19(2)), with the art 19(3) exceptions. Mixed private use is split by objective criteria (art 19(4)). Pro rata is R-IT-4.

**Monthly cut-off.** Invoices received and registered by the 15th of the following month count for the month, except purchases of the prior year (DPR 100/1998 art 1(1)). Quarterly filers may register sales invoices by the end of the month after the quarter (DPR 542/1999 art 7(3-bis)).

**Split payment.** Art 17-ter covers supplies to: (1) the public administrations in L. 196/2009 art 1(2); (1-bis) (0a) national, regional and local enti pubblici economici, including aziende speciali and ASP; (0b) foundations with at least 70% of the fondo di dotazione from public administrations; (a) companies controlled under art 2359(1) n. 2 c.c. directly by the Presidenza del Consiglio and Ministries; (b) companies controlled under art 2359(1) n. 1 directly or indirectly by public administrations or the persons in (0a), (0b), (a) or (c); (c) companies with at least 70% of capital held by public administrations or the persons in (0a), (0b), (a) or (b). Listed companies are out for invoices from 1 July 2025 (D.L. 84/2025 art 10). Art 17-ter(1-quater) lets a customer's attestation bind the supplier. Art 17-ter(1-quinquies) excludes enti gestori of demanio collettivo for uso civico, and (1-sexies) excludes services whose fees are subject to withholding. The rule runs under an EU derogation (1-ter). The MEF states that Decision (EU) 2026/1728 continues it to 30 June 2029; the Official Journal text was not obtained. R-IT-3 applies.

### Conservative defaults

These apply the Tier 2 rule in `vat-workflow-base`. A default stands only where the law read fixes the result of the missing fact. Otherwise the item is Needs Input, nothing is entered, and the question goes on the form.

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | Needs Input. The legacy '22%' is replaced: a receipt can be taxable at another rate, exempt, non imponibile, outside IVA or no sale. |
| Unknown VAT status of a purchase | Needs Input. No VP5 entry without a document registered under art 25. |
| Unknown counterparty country | Needs Input. The legacy 'Domestic Italy' is replaced. |
| Unknown B2B vs B2C status for EU customer | Needs Input. The legacy 'B2C, charge 22%' is replaced: `eu-vat-directive` says not to zero-rate if VIES fails, which does not fix the Italian charge. |
| Road motor vehicle, not the object of the activity, client not an agent or commercial representative, exclusive business use not shown | 40% (art 19-bis.1(c)). Disclose it, the fuller deduction if exclusive use is proved, and the IVA at stake. Any of those facts unknown: Needs Input. |
| Unknown business-use share of phone, internet, home office or other mixed item | Needs Input. Art 19(4) requires objective criteria, so the law fixes neither 0% nor 100%. |
| Unknown SaaS billing entity | Needs Input. The route and related filings follow the supplier's establishment and the invoice. |
| Unknown blocked-input status (entertainment, personal use) | Needs Input. No VP5 entry until answered. |
| Unknown whether a transaction is in scope | Needs Input |
| Period, filing frequency or regime unknown | Needs Input. A regime that fires a refusal stops the workflow. |

### Red flag thresholds

Working review settings for the reviewer brief, not legal amounts.

| Flag | Value |
| --- | --- |
| HIGH single transaction | EUR 5,000 |
| HIGH tax delta on a single default | EUR 400 |
| MEDIUM counterparty concentration | More than 40% of output or input |
| MEDIUM conservative default count | More than 4 across the return |
| LOW absolute net IVA position | EUR 10,000 |
| Tier 2 question threshold | EUR 0: no row is filtered on amount, as no Italian floor is supported |

### LIPE fields (VP section)

The legacy VP table was wrong from VP2 to VP12 and is replaced from the model and instructions the Agenzia links on its form page, file edition 2024. Amounts are in euro and cents, with the third decimal rounded up at 5 or more. Check the edition on the page before filing.

| Line | Meaning |
| --- | --- |
| VP1 | Period: month (col 1) or quarter (col 2), with boxes for subforniture, exceptional events and extraordinary operations. Quarter 5 is for the Q4 of art 7 DPR 542 quarterlies. |
| VP2 | Total sales, net of IVA, made in the period: taxable, non imponibile, exempt, deferred, those where the customer owes the tax, and art 21(6-bis) non-territorial operations. Leaves out exempt sales under the art 36-bis dispensa, except art 10 nn 11, 18, 19 and third paragraph. |
| VP3 | Total purchases, net of IVA: domestic, intra-EU and imports, from invoices and customs bills registered in the period, including deferred ones and those with non-deductible IVA |
| VP4 | IVA esigibile. Includes reverse-charge tax and art 17-ter tax that entered the settlement. |
| VP5 | IVA detratta. Includes the deductible part of reverse-charge tax. |
| VP6 | Col 1, IVA dovuta: VP4 - VP5 if positive. Col 2, credit: the absolute amount otherwise. |
| VP7 | Debt from the prior period not above EUR 100 |
| VP8 | Credit from the prior period, net of any part claimed by quarterly refund or offset application |
| VP9 | Credit from the prior year's annual return used in the settlement. A credit offset in F24 does not go here, except as a negative entry removing a credit already shown in VP9 and not yet used, so it can be offset. A refund claimed in earlier years and refused for the part used in a settlement also goes here. |
| VP10 | Payments by F24 'elementi identificativi' for first domestic vehicle sales (D.L. 262/2006) |
| VP11 | Particular tax credits used in the settlement, other than those offset in F24 |
| VP12 | 1% interest on amounts to pay under art 7 DPR 542, for quarterlies. Not for Q4. |
| VP13 | Acconto: col 1 method (1 historic, 2 forecast, 3 analytic, 4 telecoms, water, energy and waste operators), col 2 amount, even if unpaid. Below EUR 103.29, not paid and not shown. |
| VP14 | Col 1 IVA to pay, even if not paid because not above EUR 100. Col 2 credit. |

The form's formulas, with the floors:

- VP14 col 1 = max((VP6 col 1 + VP7 + VP12) - (VP6 col 2 + VP8 + VP9 + VP10 + VP11 + VP13 col 2), 0)
- VP14 col 2 = max((VP6 col 2 + VP8 + VP9 + VP10 + VP11 + VP13 col 2) - (VP6 col 1 + VP7 + VP12), 0)

The VP12 base is 'importi da versare'. This file reads that as the amount to pay before the interest, net of credits, which matches how VL36 works in the annual return. That reading is held, so VP12, VP14 and any amount built on them, including Example 1, are conditional on it. The Q4 of art 7 quarterlies leaves VP11, VP12 and VP14 blank and settles in the annual return, where VL36 takes the 1%. Differed esigibilita: the taxable amount goes in VP2 for the period of the operation and the tax in VP4 when it falls due. Payments under ravvedimento are not shown in VP lines. If there are no data to report, no LIPE is due unless a credit is carried.

### VAT registers

| Register | Purpose |
| --- | --- |
| Registro delle fatture emesse (art 23) | Sales invoices issued |
| Registro degli acquisti (art 25) | Purchase invoices received and customs bills |
| Registro dei corrispettivi (art 24) | Daily receipts (retail and hospitality). Electronic storage and transmission of daily data replaces this register under D.Lgs. 127/2015 art 2(1). |

### Classification rules

Valid codes for column H of the working paper are below. Each row carries one code, as Check 5 of the base requires, and the Box Summary sheet maps each code to VP lines. The legacy slash entry is replaced.

| Code | Use | Goes to |
| --- | --- | --- |
| OUT-T | Sale with Italian IVA | VP2 net, VP4 tax |
| OUT-N | Sale without Italian IVA: non imponibile, exempt, non-territorial with art 21(6-bis) invoice, or customer-debtor | VP2 net |
| IN-D | Purchase with deductible IVA on a registered document | VP3 net, VP5 deductible tax |
| IN-N | Registered purchase with no deductible IVA | VP3 net. Any non-deductible tax goes in neither VP4 nor VP5. |
| IN-RC | Reverse-charge purchase: customer accounts for the tax | VP3 net, VP4 tax, VP5 deductible part |

Check 10 of the base: IN-RC nets to zero only where the tax is fully deductible.

- **Standard rate.** 22%, art 16(1). Sales OUT-T, purchases IN-D.
- **Reduced rates.** See the rate lists. Sales OUT-T, purchases IN-D, subject to the blocks below.
- **Non imponibile.** Exports (art 8, with export evidence), and intra-EU B2B goods (D.L. 331/1993 art 41, with the art 41(2-ter) conditions). OUT-N. The legacy 'Intra-EU B2B services, non imponibile' is corrected: under art 7-ter they are outside Italian IVA, with an art 21(6-bis)(a) invoice.
- **Exempt.** Art 10, including medical services (n. 18), education (n. 20), insurance (n. 2), financial services (n. 1), residential rent where n. 8 applies, and the universal postal service (n. 16). OUT-N, no deduction on related costs. R-IT-4 where its trigger fires.
- **Domestic purchases.** Input IVA on a compliant invoice from an Italian supplier is deductible for purchases used in taxable business activity, subject to the blocks. IN-D.
- **Reverse charge, EU supplier.** Art 17(2): the customer fulfils the supplier's duties, integrating and registering the invoice under D.L. 331/1993 arts 46 and 47, by the 15th of the month after receipt, referring to the prior month. IN-RC. The legacy 'VP3/VP10' is wrong: VP10 is not an intra-EU line.
- **Reverse charge, non-EU supplier.** Art 17(2), with the self-invoice (autofattura) under art 21(5). IN-RC. The legacy 'VP11/VP12' is wrong: those lines are tax credits and quarterly interest.
- **EU goods received.** Intra-EU acquisition, D.L. 331/1993 art 38, at the rate of the goods (art 46(1)). IN-RC.
- **Imports.** Customs assesses, settles and collects the tax for each operation (art 70). The customs bill registered under art 25 supports IN-D. The legacy statement that import IVA can be deferred to the LIPE since 2022 was not supported by any text read and is held. No gold or silver case is worked here.
- **Sales.** Charge 22%, 10%, 5% or 4% as applicable, via fattura elettronica through SDI where `italy-einvoice` says so. OUT-T.
- **Sales to EU consumers.** Goods to EU consumers stay under Italian IVA only if all these hold (D.L. 331/1993 art 41(1)(b)): the seller is established in Italy and not also in another member state; art 7-octies(3)(b) consumer services plus intra-EU distance sales did not exceed EUR 10,000 in the prior calendar year and have not in the current year; and the seller has not opted for tax in the other state. Otherwise R-IT-9.

### Input IVA blocked or limited

Art 19-bis.1 DPR 633. The legacy section is corrected on each point marked.

- **Road motor vehicles, (c).** 40% for road motor vehicles other than those in Tabella B letter (f), which was not read, if not used exclusively in the business, art or profession. The rule does not apply where vehicles are the object of the activity, or to agents and commercial representatives. A vehicle here is one other than farm or forestry tractors, normally for road transport of persons or goods, of maximum authorised mass not above 3,500 kg and not above 8 seats excluding the driver. The vehicle's components and spares follow the same limit. The legacy 'legal presumption' and '100% for taxis, driving schools, car rental' are replaced by these tests. The art 19-bis.1(c) limit rests on an EU derogation whose current decision was not read.
- **Fuel, lease and running costs, (d).** Fuel and lubricants, art 16(3) services (hire and leasing), custody, maintenance, repair and use, including road transit, are deductible in the same measure as the vehicle. The letter's last sentence requires proof of the operation by payment by credit, debit or prepaid card, or other means the Agenzia sets. Its words follow the whole letter. The Agenzia applies it to fuel and lubricants (provvedimento 73203 of 4 April 2018; circ. 8/E 2018), and accepts cheques, bankers' and postal drafts, and electronic means including direct debit, bank or postal transfer, postal bill and cards. Cash is not listed. No text read extends the sentence to the other costs in (d) or expressly excludes them, so that reach is held, and such a cost paid in cash is Needs Input. Motorway tolls follow the vehicle. A vehicle at 40% gives 40%.
- **Aircraft, (a), and Tabella B and pleasure craft, (b).** Blocked on the conditions there, with (b) open only where the activity is their object and not for professionals. Needs Input.
- **Passenger transport, (e).** Not deductible unless it is the object of the activity. This reaches rail, flights, taxis and ride hire. The legacy VP5 rows on those suppliers are corrected.
- **Food and drink, (f).** Not deductible on purchase or import, except where they are the object of the activity, or served in school, company or inter-company canteens or by vending machines in the premises.
- **Restaurants and hotels.** The former block in (e) was removed for operations from 1 September 2008 (D.L. 112/2008 art 83(28-ter)). A business meal or hotel stay is deductible only on an invoice registered under art 25, for a purchase inherent to the taxable activity, and not where it is a representation cost under (h). A scontrino alone does not support it (arts 22 and 25). The reach of (f) over restaurant service, as against food purchases, is not stated in the text read and is held.
- **Representation, (h).** Not deductible, as defined for income tax, except goods of unit cost not above EUR 50. The legacy 'deductible if proper fattura obtained' is wrong. The definition is in a decree not read, so whether an item is representation is Needs Input.
- **Residential buildings, (i).** Tax on buying residential buildings, or on their lease, maintenance, recovery or management, is not deductible, except for firms whose exclusive or main object is building them. The block does not apply to those whose art 10 n. 8 exempt operations reduce the percentage under art 19(5) and art 19-bis.
- **Telephony.** The legacy '50% deductible (Art. 19-bis1 lett. d)' is wrong. The former letter (g) was repealed by L. 244/2007, and (d) is about vehicles. Telephony follows art 19(1) and (4).
- **Personal use.** Not deductible (art 19(1) and (4)).

### Capital goods

Assets above EUR 516.46 go through income tax depreciation (TUIR art 102(5) for a business; for a professional see `it-income-tax`). The legacy line that the threshold matters for income tax and not IVA is corrected: art 19-bis.2(5) uses the 1 million lire and 25% test to say which goods are depreciable for IVA adjustments. Input deduction itself follows the same rules as other purchases, in VP5, and the LIPE has no separate line. The annual return records depreciable purchases separately.

Art 19-bis.2: depreciable goods adjust over the year of entry into use and the 4 following years, buildings over 10; the percentage adjustment under art 19-bis.2(4) applies where the deduction percentage varies by more than 10 points. Art 19-bis.2(3) was repealed by D.Lgs. 186/2025. Flag each such purchase for the registro dei beni ammortizzabili.

### Supplier discovery library

This is a matching aid. It does not override the law, and the legacy 'deterministic pre-classifier' wording is withdrawn. A name does not establish a billing entity, a rate or what an invoice shows, and no supplier's status was read for this conversion. Billing entities below are from the legacy file and are unverified. Match by case-insensitive substring on the counterparty name; use the most specific pattern; if none matches, use the classification rules.

'Claim' below means: IN-D, for the IVA the document shows, only with an invoice or customs bill registered under art 25, for taxable use. 'No IVA' means: no VP5. Where a registered invoice is held it is IN-N; where none is held it is outside the VP lines, flagged. An exempt purchase is an IN-N row, not a legal exclusion: VP3 has no exempt carve-out.

**Banks.** Art 10(1)(1) covers financing, deposits, current accounts, payments and transfers; custody and administration of securities is taxable; debt collection is excluded.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| UNICREDIT, UNICREDIT SPA | No IVA for bank charges and fees | Check the document: a taxable service charged with IVA is Claim |
| INTESA SANPAOLO, INTESA SP | same | same |
| BANCO BPM, BPM | same | same |
| MONTE DEI PASCHI, MPS | same | same |
| BPER BANCA | same | same |
| POSTE ITALIANE, BANCOPOSTA | same | same |
| CREDITO EMILIANO, CREDEM | same | same |
| REVOLUT, WISE, N26 (fee lines) | same | Check for separate taxable subscription invoices |
| INTERESSI, INTERESSE | No IVA | Paid or received interest on financing is exempt (art 10(1)(1)), not out of scope as the legacy said. Moratory interest is left out of the base (art 15). |
| MUTUO, PRESTITO, FINANZIAMENTO | Exclude | Loan principal movement, outside IVA. Any interest within it: as above. |

**Government, regulators and statutory bodies.** Tax payments are no supply. Fees depend on the document.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| AGENZIA ENTRATE, AGENZIA DELLE ENTRATE | Exclude | Tax payment, not a supply |
| F24, MODELLO F24, PAGAMENTO F24 | Exclude | Tax payment (IVA, IRPEF, INPS, IRAP) via F24 |
| INPS | Exclude | Social security contributions (contributi previdenziali) |
| INAIL | Exclude | Workplace insurance contributions |
| CAMERA DI COMMERCIO, CCIAA, REGISTRO IMPRESE | Exclude | Chamber and company registry fees, no IVA shown. If a document shows IVA: Claim. |
| COMUNE DI, MUNICIPIO | Exclude | Municipal fees and taxes. If a document shows IVA: Claim. |
| REGIONE, PROVINCIA | Exclude | same |
| EQUITALIA, AGENZIA RISCOSSIONE | Exclude | Tax collection agency. Equitalia is the legacy name. |
| DOGANA, AGENZIA DOGANE | Exclude the duty | Check for import IVA on the customs bill: Claim on that bill |

**Utilities and telecoms.** Mixed use: Needs Input.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| ENEL, ENEL ENERGIA, ENEL SERVIZIO | Claim | Electricity: use the rate on the invoice. Item 103 gives 10% to domestic use and to extractive, agricultural and manufacturing businesses. |
| ENI, ENI PLENITUDE | Claim | Gas: use the rate on the invoice. Item 127-bis gives 10% to civil use up to 480 cubic metres a year. |
| EDISON, A2A, IREN, HERA | Claim | Use the rate on the invoice |
| ACEA | Claim | Water may be 10% (item 81), electricity as above |
| TIM, TELECOM ITALIA | Claim | Business share under art 19(4) |
| VODAFONE IT, VODAFONE ITALIA | Claim | same |
| WIND TRE, WINDTRE | Claim | same |
| FASTWEB | Claim | same |
| ILIAD | Claim | same |

**Insurance.** Art 10(1)(2).

| Pattern | Treatment | Condition |
| --- | --- | --- |
| GENERALI, ASSICURAZIONI GENERALI | No IVA | Insurance, exempt |
| ALLIANZ, ALLIANZ ITALIA | No IVA | same |
| UNIPOL, UNIPOLSAI | No IVA | same |
| AXA ITALIA | No IVA | same |
| CATTOLICA ASSICURAZIONI, ZURICH | No IVA | same |
| ASSICURAZIONE, POLIZZA | No IVA | Check any document showing IVA |

**Post and logistics.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| POSTE ITALIANE (standard mail) | No IVA for universal service postage | Art 10(1)(16). Individually negotiated terms are excluded from the exemption. |
| POSTE ITALIANE (parcels, Poste Delivery) | Claim | Non-universal services are taxable |
| SDA EXPRESS, BRT, BARTOLINI | Claim | Express courier |
| DHL EXPRESS ITALIA | Claim | same |
| GLS ITALY, TNT ITALIA | Claim | same |

**Transport and travel.** The sale side rates are in the rate lists. The buyer side is blocked by art 19-bis.1(e) unless passenger transport is the client's activity.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| TRENITALIA, ITALO, NTV | No VP5, blocked | Rail, 10% on the supplier's side (item 127-novies). IN-N with an invoice. |
| ATAC, ATM MILANO, GTT, ANM | No VP5, blocked | Urban transport, 10% on the supplier's side. Tickets fall under art 74(1)(e). |
| UBER IT, UBER ITALY | No VP5, blocked | Read the document for the service and supplier. Any service other than passenger transport shown on it: Needs Input. |
| TAXI, RADIOTAXI | No VP5 | Urban transport by veicoli da piazza within a commune or between communes not over 50 km apart is exempt (art 10(1)(14)). The legacy 10% is wrong for that case. Otherwise 10%, blocked. |
| ALITALIA, ITA AIRWAYS (domestic) | No VP5, blocked | Domestic flights 10% (item 127-novies). Alitalia is the legacy name. |
| ITA AIRWAYS, RYANAIR, EASYJET (international) | No VP5, blocked | Partly in Italy and partly abroad under one contract: non imponibile (art 9(1)(1)) on the supplier's side. The legacy 'exempt' is corrected. |
| AUTOSTRADE, TELEPASS | Follows the vehicle | Road transit under art 19-bis.1(d). Check the rate on the invoice. |

**Food, restaurants and hotels.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| ESSELUNGA | No VP5 | Food and drink, art 19-bis.1(f), unless they are the object of the activity or a listed canteen or vending case |
| CONAD, COOP, EUROSPIN, LIDL | No VP5 | same |
| CARREFOUR ITALIA, PENNY, MD | No VP5 | same |
| PAM, DESPAR, IPER | No VP5 | same |
| RISTORANTE, TRATTORIA, PIZZERIA, BAR | Needs Input | Restaurants and hotels rule above. Representation: blocked. |
| HOTEL, ALBERGO, BOOKING | Needs Input | Italian hotel: same rule. Foreign hotel: foreign tax, no VP5. |

**Fuel.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| ENI, Q8, IP, ESSO, SHELL (fuel) | Vehicle share | Art 19-bis.1(d). Needs an invoice and card or other traceable payment. |

**SaaS and platforms, invoice from an EU entity.** IN-RC if the invoice shows no Italian IVA. If it shows Italian IVA from an Italian-registered supplier: Claim.

| Pattern | Legacy billing entity, unverified | Treatment |
| --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Ireland Ltd (IE) | IN-RC after checking the invoice |
| MICROSOFT (365, Azure) | Microsoft Ireland Operations Ltd (IE) | same |
| ADOBE | Adobe Systems Software Ireland Ltd (IE) | same |
| META, FACEBOOK ADS | Meta Platforms Ireland Ltd (IE) | same |
| LINKEDIN (paid) | LinkedIn Ireland Unlimited (IE) | same |
| SPOTIFY TECHNOLOGY | Spotify AB (SE) | same |
| DROPBOX | Dropbox International Unlimited (IE) | same |
| SLACK | Slack Technologies Ireland Ltd (IE) | same |
| ATLASSIAN (Jira, Confluence) | Atlassian Network Services BV (NL) | same |
| ZOOM | Zoom Video Communications Ireland Ltd (IE) | same |
| STRIPE (subscription fees) | Stripe Technology Europe Ltd (IE) | same |
| AWS (standard), AWS EMEA SARL | AWS EMEA SARL (LU), check | same. If the invoice shows Italian IVA, Claim. |

**SaaS and platforms, invoice from a non-EU entity.** IN-RC with autofattura if the invoice shows no Italian IVA.

| Pattern | Legacy billing entity, unverified | Treatment |
| --- | --- | --- |
| NOTION | Notion Labs Inc (US) | IN-RC after checking the invoice |
| ANTHROPIC, CLAUDE | Anthropic PBC (US) | same |
| OPENAI, CHATGPT | OpenAI Inc (US) | same |
| GITHUB (standard plans) | GitHub Inc (US), check if billed by an IE entity | same |
| FIGMA | Figma Inc (US) | same |
| CANVA | Canva Pty Ltd (AU) | same |
| HUBSPOT | HubSpot Inc (US) or HubSpot Ireland Ltd (IE), check | same, on the entity shown |
| TWILIO | Twilio Inc (US) | same |
| APPLE | Not in the legacy file | Needs Input: read the invoice |

**Payment processors.** The legacy 'exempt financial services' is replaced: art 10(1)(1) turns on the service, so a processor's fee is not exempt by name.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| STRIPE (transaction fees), PAYPAL (transaction fees) | Needs Input | Read the fee invoice for the supplier, the service and the art 10 reference. |
| STRIPE (monthly subscription) | IN-RC after checking the invoice | Legacy billing entity is IE, unverified |
| SUMUP, SQUARE, ZETTLE | Check invoice | Italian entity with IVA: Claim. EU entity, no IVA: IN-RC. |
| NEXI, SATISPAY | Check invoice | Italian payment processor: fees may be exempt or taxable |

**Professional services.** Claim, subject to the purchase being for the business. The legacy 'Always deductible' is replaced: art 19 has no such category.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| COMMERCIALISTA, STUDIO COMMERCIALE | Claim | Business purpose |
| AVVOCATO, STUDIO LEGALE | Claim | Business legal matter |
| NOTAIO, STUDIO NOTARILE | Claim | Notarial fees on business transactions. Taxes recharged in the customer's name are outside the base (art 15). |
| CONSULENTE DEL LAVORO | Claim | Payroll consultant |
| ARCHITETTO, INGEGNERE, GEOMETRA | Claim | Check art 19-bis.1(i) for residential work |

**Office and workspace.** Not in the legacy file; generic rows required by the base.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| CANCELLERIA, CARTOLERIA, OFFICE SUPPLIES, AMAZON BUSINESS | Claim | Business purchase with an invoice. A scontrino does not support it. |
| COWORKING, UFFICIO CONDIVISO | Check invoice | Claim where the invoice shows IVA |

**Payroll and social security.** Exclude entirely.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| INPS, CONTRIBUTI INPS | Exclude | Social security contributions |
| INAIL, PREMIO INAIL | Exclude | Workplace insurance |
| STIPENDIO, SALARIO, BUSTA PAGA | Exclude | Wages, outside IVA |
| TFR, TRATTAMENTO FINE RAPPORTO | Exclude | Severance fund, outside IVA |
| CASSA PREVIDENZA, ENPAM, CNPADC | Exclude | Professional pension fund |

**Property and rent.** Art 10(1)(8): leases of buildings are exempt, except where the law taxes them or the landlord opts. See the rent row under Transaction questions and defaults.

| Pattern | Treatment | Condition |
| --- | --- | --- |
| AFFITTO COMMERCIALE, LOCAZIONE COMMERCIALE | Check invoice | Claim where the landlord charged IVA |
| AFFITTO, LOCAZIONE (residential, no IVA) | No VP5 | Art 19-bis.1(i) blocks any tax on residential leases for most clients |
| IMU, TASI | Exclude | Property tax, not a supply |
| CONDOMINIO | Check invoice | Exclude if no IVA is shown; Claim if a document shows IVA |

**Internal transfers and exclusions.**

| Pattern | Treatment | Condition |
| --- | --- | --- |
| GIROCONTO, BONIFICO INTERNO | Exclude | Internal movement |
| TRASFERIMENTO TRA CONTI | Exclude | Own-account transfer |
| DIVIDENDO | Exclude | Dividend payment, outside IVA |
| RATA MUTUO, RIMBORSO PRESTITO | Exclude | Loan repayment, outside IVA |
| PRELIEVO BANCOMAT, PRELIEVO CONTANTI | Tier 2, ask | Needs Input: what was the cash spent on? |
| APPORTO PERSONALE, VERSAMENTO SOCIO | Exclude | Owner injection |

### Bank statement reading guide

Follow the universal exclusion rules in `vat-workflow-base` Step 6, plus these patterns.

- **CSV format.** Italian banks typically export CSV or Excel with DD/MM/YYYY dates. Common columns: Data, Descrizione/Causale, Dare (debit), Avere (credit), Saldo. These are from the legacy file, and no bank's documents were read. Confirm against the file supplied.
- **Italian terms.** Affitto (rent), stipendio (salary), interessi (interest), bonifico (transfer), contributi (contributions), fattura (invoice), rimborso (refund), versamento (deposit), prelievo (withdrawal).
- **ABI causale codes.** The legacy list is 27 bonifico, 48 credit card, 05 direct debit (RID/SDD), 26 cheque, said to appear in UniCredit and Intesa exports. No source was read. Treat them as hints only.
- **Internal transfers.** Giroconto is an internal transfer. Exclude.
- **F24 payments.** Tax payments appear as 'PAGAMENTO F24' or with tax codes: 6001 to 6012 monthly IVA, 6031 to 6033 quarterly IVA, 6034 Q4 for the special quarterlies, 6013 and 6035 acconto, per the annual instructions. Always exclude.
- **Fattura elettronica (SDI).** Electronic invoices go through SDI under D.Lgs. 127/2015 art 1(3). Who is covered and from when are in `italy-einvoice`. An SDI extract is the most reliable data source: prefer it over the bank statement for invoice details.
- **Foreign currency.** Art 13(4): the exchange rate of the day of the operation or, if that is not on the invoice, the day of issue; failing that, the nearest earlier quotation. The art 13(4) annual ECB option is in the text. The legacy 'bank statement rate' is not the statutory rate.
- **IBAN prefix.** IT is Italy. IE, LU, NL, FR and DE are EU. US, GB, AU and CH are non-EU. A prefix is a hint for the question form and does not prove where the party is established.

### Transaction questions and defaults

Tier 2 catalogue for the structured form in `vat-workflow-base`. 'Needs Input' means nothing is entered until answered.

| Item | Pattern | Default | Question |
| --- | --- | --- | --- |
| Fuel and vehicle costs | ENI, Q8, IP, ESSO, SHELL, fuel receipts | Conservative defaults row. Fuel or lubricants with no proof of card or traceable payment: no VP5. Another art 19-bis.1(d) cost paid in cash: Needs Input. | 'Is this a core business vehicle (taxi/rental) or a standard company car? Is it used only for the business? Are you an agent or commercial representative? How was the cost paid?' |
| Restaurants and entertainment | Any named ristorante, trattoria, pizzeria, bar | Needs Input | 'Do you have a fattura elettronica (not just a scontrino) for this meal? Was it a business expense? Was it to entertain clients or for your own or staff business travel?' |
| Ambiguous SaaS billing entities | Google, Microsoft, Adobe, Meta and the other names in the SaaS tables | Needs Input. The legacy non-EU default is replaced. | 'Could you check the invoice? I need the legal entity name and country.' |
| Owner-named round-number receipts | Round-number incoming transfers from owner-named counterparties | Needs Input. The legacy 'exclude as owner injection' is replaced. | 'The EUR X transfer from [name]: customer payment, own money, or loan?' |
| Receipts from individuals, not the owner | Incoming transfers from individual names | Needs Input. The legacy 'domestic B2C sale at 22%' is replaced. | 'Was it a sale? Business or consumer?' |
| Foreign receipts | Incoming transfers from foreign counterparties | Needs Input. The legacy 'domestic 22%' is replaced. | 'B2B with a VAT number, B2C, goods or services, which country?' |
| Large one-off purchases | Near EUR 516.46 | Needs Input on the capital flag; the IVA follows the ordinary rules | 'Confirm the total invoice amount and what the item is.' |
| Mixed-use phone, internet | TIM, Vodafone, WindTre personal lines | Needs Input. The legacy 50% is removed. | 'Is this a dedicated business line or mixed-use? If mixed, on what objective basis is the business share set?' |
| Outgoing transfers to individuals | Bonifico to a person | Needs Input. The legacy 'exclude as drawings' is replaced. | 'Contractor payment, wages, refund, or personal?' |
| Cash withdrawals | Prelievo bancomat, prelievo contanti | Needs Input. The legacy 'exclude' is replaced by the same rule. | 'What was the cash used for?' |
| Rent payments | Affitto, locazione, canone | Needs Input. The legacy 'no IVA' default is replaced. | 'Commercial or residential? Does the landlord charge IVA?' |
| Foreign hotel and accommodation | Foreign hotel | Foreign tax is not Italian input IVA: no VP5 (art 7-quater places the service where the building is) | 'Business trip?' Income tax deduction is possible; see `it-income-tax`. |
| Airbnb income | Airbnb credits | Needs Input | 'Short-term tourist rental? Duration? Cedolare secca applied?' |
| Domestic reverse charge | Payments to subcontractors in construction, cleaning and energy | Needs Input | 'Is this a domestic reverse charge sector? What does the invoice say about art 17(6)?' |
| Platform sales | Marketplace payouts | Needs Input. R-IT-9 for cross-border consumer sales. Platform fees: check invoice. | 'Do you sell to buyers outside Italy?' |

**Domestic reverse charge, art 17(6).** Customer accounts for the tax on: (a) construction sector services other than those in (a-ter), including labour supply, by subcontractors to businesses that build or renovate buildings, to the main contractor or to another subcontractor, but not to a contraente generale given all the works; (a-bis) building sales taxed by option; (a-ter) cleaning, demolition, installation and completion on buildings; (a-quater) and (a-quinquies), which depend on EU authorisation; (b) mobile phones; (c) consoles, tablets, laptops and integrated circuits before installation; (d-bis), (d-ter) and (d-quater), the gas and electricity certificate and reseller cases. The text limits (b), (c), (d-bis), (d-ter) and (d-quater) to operations carried out until 31 December 2026. Art 17(5) adds gold. On art 17(5) and (6) reverse charge the customer's tax goes in VP4 and VP5, and the supplier's taxable amount in VP2. Logistics under (a-quinquies): L. 207/2024 art 1(58) makes it subject to an art 395 authorisation. Meanwhile art 1(59) to (63) gives a 3-year option, also open between contractor and subcontractors, which is not reverse charge: the supplier invoices under art 21, and the customer pays the IVA in the supplier's name and on its behalf by F24, with no offset, by the art 18 date for the month after the invoice date. The supplier stays jointly liable. The annual return has line VJ30 for these purchases. The LIPE treatment of the option was not read and is held.

### Onboarding fallback

This is intake only. Ask these only where inference fails, and before any output (Step 6.5 of the base comes before Step 7). What stays unanswered is Needs Input.

| Fact | Inference | Question |
| --- | --- | --- |
| Entity type | SRL, SPA, SAS: company; ditta individuale: sole trader; libero professionista: freelance professional | 'Ditta individuale, SRL, or libero professionista?' |
| VAT regime | A LIPE filing points to regime ordinario but does not prove it | 'Are you under regime ordinario or regime forfettario?' |
| Partita IVA | IT-format P.IVA on invoices | 'What is your Partita IVA? (IT + 11 digits)' |
| Filing period and frequency | Date range on statement | 'Which period? Monthly or quarterly filer?' |
| Industry and sector | Counterparty mix | 'What does the business do?' |
| Employees | INPS outgoing | 'Do you have employees?' |
| Exempt supplies | Medical, financial or educational income | 'Do you make any exempt sales?' If yes, test R-IT-4. |
| Credit carried forward | Not inferable; always ask | 'Do you have IVA credit from the prior period (VP8) or the prior year (VP9)?' |
| Cross-border customers | Foreign IBANs | 'Customers outside Italy? EU or non-EU? B2B or B2C?' |
| Public bodies | Payments from public-sounding entities | 'Do you supply Italian public administration or the other art 17-ter bodies?' If yes, test R-IT-3. |

### Excel working paper

Working paper only. The specification is in `vat-workflow-base` Section 3, including its columns A to P. Column H takes the codes under Classification rules. Sheet 'Box Summary' carries one row per VP line, and Sheet 'Return Form' follows the VP layout.

| Line | Label | Source |
| --- | --- | --- |
| VP2 | Total sales | =SUMIFS(Transactions!E:E, H, "OUT-T") + SUMIFS(E:E, H, "OUT-N") |
| VP3 | Total purchases | =SUMIFS on IN-D, IN-N and IN-RC |
| VP4 | IVA esigibile | Tax on OUT-T and IN-RC rows |
| VP5 | IVA detratta | Deductible tax on IN-D and IN-RC rows |
| VP6 | Dovuta or credit | col 1 =MAX(VP4-VP5,0); col 2 =MAX(VP5-VP4,0) |
| VP7, VP8, VP9, VP10, VP11, VP13 | Prior debt, credits, payments, acconto | Manual entry from the prior LIPE, annual return and F24 records |
| VP12 | Quarterly interest | =ROUND(1% x amount to pay before interest, 2), quarterly only, not Q4 |
| VP14 | To pay or credit | The 2 formulas under LIPE fields |

Mandatory recalculation before delivery:

```bash
python /mnt/skills/public/xlsx/scripts/recalc.py /mnt/user-data/outputs/italy-vat-<period>-working-paper.xlsx
```

**Related filings for Check 11.** A row in these cases triggers another filing:

| Row | Filing |
| --- | --- |
| OUT-N for intra-EU goods, or an EU B2B service; IN-RC for EU goods or services | Intrastat lists (D.L. 331/1993 art 50(6)), subject to the art 50(6-bis) decree and the art 50(6) provvedimento, not read, which can reduce who files and may exclude a row |
| OUT-N or IN-RC with a party not established in Italy | Cross-border data via SDI (D.Lgs. 127/2015 art 1(3-bis)), unless a customs bill or SDI e-invoice covers the operation, or it is a purchase of up to EUR 5,000 per operation not territorial in Italy under arts 7 to 7-octies |
| Any period | Annual Dichiarazione IVA, where the client is obliged |

### Key legislation

| Topic | Source |
| --- | --- |
| Scope, place, tax point | DPR 633 arts 1, 6, 7 to 7-septies |
| Exports and exempt supplies | DPR 633 arts 8, 8-bis, 9, 10 |
| Base and rates | DPR 633 arts 13, 15, 16, Tabella A |
| Reverse charge and split payment | DPR 633 arts 17, 17-ter |
| Deduction and adjustment | DPR 633 arts 19, 19-bis, 19-bis.1, 19-bis.2 |
| Invoices and registers | DPR 633 arts 21 to 25; D.Lgs. 127/2015 |
| Credit and refund | DPR 633 arts 30, 38-bis |
| Registration | DPR 633 arts 35, 35-ter |
| Intra-EU operations | D.L. 331/1993 arts 38 to 50 |
| LIPE | D.L. 78/2010 art 21-bis |
| Settlement and payment | DPR 100/1998 art 1; DPR 542/1999 arts 6, 7; D.Lgs. 241/1997 arts 17 to 19 |
| Annual return | DPR 322/1998 art 8 |
| Acconto | L. 405/1990 art 6 |
| Penalties | D.Lgs. 471/1997; D.Lgs. 472/1997 art 13; D.Lgs. 87/2024 |
| EU directive | Council Directive 2006/112/EC and Council Implementing Regulation 282/2011, via `eu-vat-directive` |

### Known gaps

- The supplier library does not cover every Italian SME.
- Split payment: R-IT-3 refuses.
- Domestic reverse charge is Tier 2 only.
- Restaurant deductibility needs an invoice, and this workflow cannot verify the document type from a bank line.
- The 40% vehicle limit and the EUR 516.46 figure rest on the texts read at 5 November 2026. Check them each year.
- The VP12 base is this file's reading of the words, so a reviewer checks the calculation.
- The 2027 Testo unico mapping is not done.

## Deadlines and filing

This section is in the child skill `italy-vat-return-reference`, moved there word for word so this file stays under the size limit. Load it with this skill.

## Penalties and interest

This section is in the child skill `italy-vat-return-reference`, moved there word for word so this file stays under the size limit. Load it with this skill.

## Cross-border points

This section is in the child skill `italy-vat-return-reference`, moved there word for word so this file stays under the size limit. Load it with this skill.

## Two worked examples that recompute

All examples are hypothetical, from a Rome-based self-employed IT consultant in regime ordinario, quarterly, with volume d'affari within EUR 500,000 and no refusal fired. Each `oa-check` is checked by CI. Examples 1 and 2 are the 2 required; Example 2 is the decision. Each rests on the documents shown being held.

### Example 1: quarterly LIPE, Q2 2026

**Input.** Domestic sales EUR 12,000 at 22%. EU B2B service sale EUR 3,500 to a German company with a valid VIES number, completed in the quarter. Laptop EUR 1,307.38 plus IVA EUR 287.62, invoice registered. Google Ireland EUR 850, invoice with no Italian IVA. Notion Labs Inc EUR 14.68, no Italian IVA. Car lease EUR 450 gross at 22%, paid by direct debit, mixed use, client not an agent, vehicle not the object of the activity. VP8 credit from Q1 EUR 300.

```oa-check
name: Italy Q2 2026 LIPE with reverse charge, 40% vehicle and credit
inputs:
  sales_22: 12000
  eu_service_sale: 3500
  laptop_net: 1307.38
  laptop_iva: 287.62
  google_net: 850
  notion_net: 14.68
  lease_gross: 450
  vehicle_share: 40
  vp8: 300
  rate: 22
steps:
  - lease_net: round(lease_gross * 100 / (100 + rate), 2)
  - lease_iva: lease_gross - lease_net
  - lease_deductible: round(pct(lease_iva, vehicle_share), 2)
  - output_sales: pct(sales_22, rate)
  - rc_google: round(pct(google_net, rate), 2)
  - rc_notion: round(pct(notion_net, rate), 2)
  - vp2: sales_22 + eu_service_sale
  - vp3: laptop_net + google_net + notion_net + lease_net
  - vp4: output_sales + rc_google + rc_notion
  - vp5: laptop_iva + rc_google + rc_notion + lease_deductible
  - vp6_col1: max(vp4 - vp5, 0)
  - vp6_col2: max(vp5 - vp4, 0)
  - to_pay_before_interest: max(vp6_col1 - vp6_col2 - vp8, 0)
  - vp12: round(pct(to_pay_before_interest, 1), 2)
  - vp14_col1: max((vp6_col1 + vp12) - (vp6_col2 + vp8), 0)
  - vp14_col2: max((vp6_col2 + vp8) - (vp6_col1 + vp12), 0)
expected:
  lease_net: 368.85
  lease_iva: 81.15
  lease_deductible: 32.46
  vp2: 15500
  vp3: 2540.91
  vp4: 2830.23
  vp5: 510.31
  vp6_col1: 2319.92
  vp6_col2: 0
  to_pay_before_interest: 2019.92
  vp12: 20.20
  vp14_col1: 2040.12
  vp14_col2: 0
```

**Result.** Conditional on this file's held reading of the VP12 base, VP14 col 1 is EUR 2,040.12, payable by F24 by 20 August 2026, with the LIPE by 30 September 2026. The non-deductible EUR 48.69 of the lease is a cost. The EU sale and the Google Ireland purchase fall under Intrastat lists subject to the hold under Related filings, so whether either is listed is held. The 2 foreign purchases need cross-border data unless an art 1(3-bis) exception applies. Another base changes the amount: for scale only, 1% before the VP8 credit gives VP12 of EUR 23.20 and VP14 col 1 of EUR 2,043.12. Confirm the base before relying on either. On this file's reading, had the VP8 credit exceeded the debt, nothing would be payable, VP12 would be nil and col 2 would carry the credit.

### Example 2: monthly or quarterly

**Input.** The consultant's IVA to pay before interest is EUR 6,000, 5,000 and 7,000 for Q1 to Q3, and EUR 4,000 for the Q4 balance in the annual return. Volume d'affari is EUR 300,000 in services. IVA arises evenly across each quarter's months.

```oa-check
name: Italy monthly or quarterly settlement, cost of the option
inputs:
  q1: 6000
  q2: 5000
  q3: 7000
  q4: 4000
  volume: 300000
  services_limit: 500000
steps:
  - headroom: services_limit - volume
  - int_q1: pct(q1, 1)
  - int_q2: pct(q2, 1)
  - int_q3: pct(q3, 1)
  - int_q4: pct(q4, 1)
  - cost_q1_to_q3: int_q1 + int_q2 + int_q3
  - quarterly_cost: cost_q1_to_q3 + int_q4
  - monthly_cost: 0
  - extra_cost_of_quarterly: quarterly_cost - monthly_cost
  - average_months_deferred: (3 + 2 + 1) / 3
  - break_even_percent_a_year: 1 * 12 / average_months_deferred
expected:
  headroom: 200000
  cost_q1_to_q3: 180
  int_q4: 40
  quarterly_cost: 220
  extra_cost_of_quarterly: 220
  average_months_deferred: 2
  break_even_percent_a_year: 6
```

**Result.** Quarterly costs EUR 220 a year more than monthly: EUR 180 on Q1 to Q3 plus EUR 40 on Q4. On Q1 to Q3, 1% buys a payment on average 2 months later. On interest alone, choose monthly if the client's own cost of money is below about 6% a year simple, and quarterly if above it. Any bookkeeping saving is a separate judgement. The month counts are 3, 2 and 1 for the 3 months of a quarter and move slightly with the August date. Q4 is left out of the break-even because the acconto changes its timing. Monthly has no option step. Quarterly is open only because EUR 300,000 is within EUR 500,000; above that it closes. The option is communicated in the first annual return after the choice, takes effect from the year chosen and lasts until revoked unless the limit is exceeded.

### Example 3: amount not above EUR 100

**Input.** A monthly filer has VP14 col 1 of EUR 85 for January 2026 and VP6 col 1 of EUR 1,000 for February, with no credits.

```oa-check
name: Italy EUR 100 carry in a monthly settlement
inputs:
  january_vp14: 85
  february_vp6: 1000
  limit: 100
steps:
  - over_limit: min(ceil(max(january_vp14 - limit, 0)), 1)
  - january_paid: january_vp14 * over_limit
  - february_vp7: january_vp14 - january_paid
  - february_vp14: february_vp6 + february_vp7
expected:
  over_limit: 0
  january_paid: 0
  february_vp7: 85
  february_vp14: 1085
```

**Result.** Nothing is paid by 16 February. February's VP7 is EUR 85 and EUR 1,085 is paid by 16 March 2026. A carry still open at the end must be paid by 16 December 2026. The carry itself needs the amount to be EUR 100 or less: at EUR 100.01 the whole amount is paid.

### Example 4: vehicle costs

**Input.** Lease IVA EUR 81.15 and fuel IVA EUR 22 paid by card, on a car in the business. Cases: mixed use; exclusive business use proved, or the client is an agent; fuel paid in cash.

```oa-check
name: Italy art 19-bis.1 vehicle and fuel deduction cases
inputs:
  lease_iva: 81.15
  fuel_iva: 22
  share_mixed: 40
  share_full: 100
steps:
  - mixed_lease: round(pct(lease_iva, share_mixed), 2)
  - mixed_fuel: round(pct(fuel_iva, share_mixed), 2)
  - mixed_total: mixed_lease + mixed_fuel
  - full_total: pct(lease_iva, share_full) + pct(fuel_iva, share_full)
  - difference: full_total - mixed_total
  - cash_fuel_case: mixed_lease + 0
expected:
  mixed_lease: 32.46
  mixed_fuel: 8.80
  mixed_total: 41.26
  full_total: 103.15
  difference: 61.89
  cash_fuel_case: 32.46
```

**Result.** Mixed use: EUR 41.26 in VP5. Exclusive use proved, or an agent or commercial representative: EUR 103.15. What decides it is the art 19-bis.1(c) test, not the legacy list of taxi, driving school and rental. The EUR 61.89 is the IVA at stake to disclose. Fuel in cash: no fuel deduction, EUR 32.46 only. The legacy said an IT consultant has 40%, which still holds on these facts.

### Transaction patterns

From the same hypothetical account, Q2 2026. Each tests both cases.

**Non-EU SaaS.** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; EUR 14.68`. Invoice from a US entity with no IVA: autofattura under art 17(2) and art 21(5). IN-RC: VP3 EUR 14.68, VP4 and VP5 EUR 3.23. Net zero for a fully taxable client. The legacy 'VP4 (via VP12)' is wrong. Use the art 13(4) exchange rate, not the bank's, if they differ.

**EU service.** `10.04.2026 ; GOOGLE IRELAND LIMITED ; DEBIT ; Google Ads April 2026 ; -850.00 ; EUR`. Invoice from an IE entity with no IVA: integrate and register under art 17(2) and D.L. 331/1993 arts 46 and 47. IN-RC: VP3 EUR 850, VP4 and VP5 EUR 187. Both sides appear. Invoice showing Italian IVA: IN-D for the tax shown.

**Restaurant.** `15.04.2026 ; RISTORANTE DA MARIO ROMA ; DEBIT ; Business dinner ; -220.00 ; EUR`. Needs Input, with the restaurant question. Client dinner that is representation: blocked under (h), IN-N. Staff or own business travel with a fattura elettronica registered under art 25: IN-D at the 10% rate shown (item 121): EUR 220 x 10/110 = EUR 20 in VP5, net EUR 200 in VP3, subject to the hold on (f). A scontrino only: no VP5. The legacy Q1 question is kept.

**Capital goods.** `18.04.2026 ; DELL ITALIA SRL ; DEBIT ; Invoice DEL2026-0041 Laptop XPS 15 ; -1,595.00 ; EUR`. EUR 1,595 / 1.22 = EUR 1,307.38 net, above EUR 516.46. Registered invoice: IN-D, VP3 EUR 1,307.38, VP5 EUR 287.62. Flag for the registro dei beni ammortizzabili and for art 19-bis.2.

**EU B2B service sale.** `22.04.2026 ; STUDIO KREBS GMBH ; CREDIT ; Invoice IT-2026-018 IT consultancy March ; +3,500.00 ; EUR`. German customer's USt-IdNr valid on VIES, invoice with 'inversione contabile': OUT-N, VP2 EUR 3,500, no IVA, Intrastat list subject to the hold under Related filings. The narrative says March: art 6(6) places the sale when the work is completed, or on earlier payment, so this pattern treats it as completed in April, in the Q2 VP2. If it was completed in March, it belongs in the Q1 VP2. Confirm the date. Number not verified: Needs Input (HIGH). The legacy 'non imponibile' field note is replaced.

**Motor vehicle.** `28.04.2026 ; LEASYS SPA ; DEBIT ; Lease payment Fiat 500X ; -450.00 ; EUR`. EUR 368.85 net and EUR 81.15 IVA. Default in Conservative defaults once the facts there are known: 40%, EUR 32.46 in VP5, VP3 EUR 368.85. The block on lease is art 19-bis.1(d), by reference to (c). The question stays: 'Vehicle: 40% IVA deductible unless used only for the business. Is that so, is the vehicle the object of your activity, or are you an agent?'

**Taxi.** `05.05.2026 ; RADIOTAXI ROMA ; DEBIT ; Corsa ; -18.00 ; EUR`. Urban: exempt under art 10(1)(14), no IVA. Otherwise blocked under (e). No VP5 either way.

**Fuel.** `12.05.2026 ; Q8 ; DEBIT ; Carburante ; -122.00 ; EUR`. Invoice and card payment, 40% vehicle: EUR 100 net, EUR 22 IVA, EUR 8.80 in VP5. Bank line alone: Needs Input.

## Ask the client first

This section is in the child skill `italy-vat-return-reference`, moved there word for word so this file stays under the size limit. Load it with this skill.

## Sources

Read on means the date read for this conversion. Limits follow each source. Normattiva is the official Italian law database. Articles were read in the text in force at retrieval; those marked 'retained' were read from an earlier phase's copy.

| Source | URL | Read on |
| --- | --- | --- |
| DPR 633 art 1, scope. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art1!vig= | 2026-11-05 |
| DPR 633 art 2, supplies of goods. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art2!vig= | 2026-11-05 |
| DPR 633 art 3, supplies of services. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art3!vig= | 2026-11-05 |
| DPR 633 art 4, business activity. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art4!vig= | 2026-11-05 |
| DPR 633 art 5, arts and professions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art5!vig= | 2026-11-05 |
| DPR 633 art 6, tax point. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art6!vig= | 2026-11-05 |
| DPR 633 art 7, definitions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7!vig= | 2026-11-05 |
| DPR 633 art 7-bis, place of goods. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7bis!vig= | 2026-11-05 |
| DPR 633 art 7-ter, place of services. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7ter!vig= | 2026-11-05 |
| DPR 633 art 7-quater, service exceptions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7quater!vig= | 2026-11-05 |
| DPR 633 art 7-quinquies, culture and sport. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7quinquies!vig= | 2026-11-05 |
| DPR 633 art 7-sexies, B2C exceptions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7sexies!vig= | 2026-11-05 |
| DPR 633 art 7-septies, non-EU consumers. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art7septies!vig= | 2026-11-05 |
| DPR 633 art 8, exports. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art8!vig= | 2026-11-05 |
| DPR 633 art 8-bis, operations treated as exports. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art8bis!vig= | 2026-11-05 |
| DPR 633 art 9, international services. Read in part: the paragraphs this file cites. Limbs 1 to 5 read. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art9!vig= | 2026-11-05 |
| DPR 633 art 10, exemptions. Read in part: the paragraphs this file cites. Numbers 1, 2, 8, 8-bis, 8-ter, 14, 15, 16, 18, 19, 20, 21 and 27-ter. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art10!vig= | 2026-11-05 |
| DPR 633 art 13, base. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art13!vig= | 2026-11-05 |
| DPR 633 art 15, exclusions from the base. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art15!vig= | 2026-11-05 |
| DPR 633 art 16, rates. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art16!vig= | 2026-11-05 |
| DPR 633 art 17, debtor and reverse charge. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art17!vig= | 2026-11-05 |
| DPR 633 art 17-ter, split payment. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art17ter!vig= | 2026-11-05 |
| DPR 633 art 18, rivalsa. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art18!vig= | 2026-11-05 |
| DPR 633 art 19, deduction. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19!vig= | 2026-11-05 |
| DPR 633 art 19-bis, deduction percentage. Read in full. The URN returned art 19-bis.1, so this was opened from the act page; the URL is the act. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633!vig= | 2026-11-05 |
| DPR 633 art 19-bis.1, limits on deduction. Read in part: the paragraphs this file cites. Letters (a) to (i) and their notes. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19bis.1!vig= | 2026-11-05 |
| DPR 633 art 19-bis.2, adjustment. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art19bis.2!vig= | 2026-11-05 |
| DPR 633 art 21, invoices. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art21!vig= | 2026-11-05 |
| DPR 633 art 21-bis, simplified invoice. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art21bis!vig= | 2026-11-05 |
| DPR 633 art 22, invoice on request. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art22!vig= | 2026-11-05 |
| DPR 633 art 23, sales register. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art23!vig= | 2026-11-05 |
| DPR 633 art 24, receipts register. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art24!vig= | 2026-11-05 |
| DPR 633 art 25, purchase register. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art25!vig= | 2026-11-05 |
| DPR 633 art 26, variations. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art26!vig= | 2026-11-05 |
| DPR 633 art 27, monthly settlement. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art27!vig= | 2026-11-05 |
| DPR 633 art 30, year-end credit. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art30!vig= | 2026-11-05 |
| DPR 633 art 33. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art33!vig= | 2026-11-05 |
| DPR 633 art 34, farming. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art34!vig= | 2026-11-05 |
| DPR 633 art 35, registration. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art35!vig= | 2026-11-05 |
| DPR 633 art 35-ter, direct identification. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art35ter!vig= | 2026-11-05 |
| DPR 633 art 36, separate activities. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art36!vig= | 2026-11-05 |
| DPR 633 art 38-bis, refunds. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art38bis!vig= | 2026-11-05 |
| DPR 633 art 67, imports. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art67!vig= | 2026-11-05 |
| DPR 633 art 70, import tax. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art70!vig= | 2026-11-05 |
| DPR 633 art 70-bis, VAT group. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art70bis!vig= | 2026-11-05 |
| DPR 633 art 70-terdecies, EU franchise. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art70terdecies!vig= | 2026-11-05 |
| DPR 633 art 70-quaterdecies, EU franchise conditions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art70quaterdecies!vig= | 2026-11-05 |
| DPR 633 art 74, special sectors. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art74!vig= | 2026-11-05 |
| DPR 633 art 74-sexies, special scheme. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633~art74sexies!vig= | 2026-11-05 |
| DPR 633 Tabella A. Read in part: the paragraphs this file cites. Parts II, II-bis and III, for the items named; opened from the act page, so the URL is the act. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1972-10-26;633!vig= | 2026-11-05 |
| D.L. 331/1993 art 38, intra-EU acquisitions. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art38!vig= | 2026-11-05 |
| D.L. 331/1993 art 40, place. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art40!vig= | 2026-11-05 |
| D.L. 331/1993 art 41, intra-EU supplies. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art41!vig= | 2026-11-05 |
| D.L. 331/1993 art 46, invoices. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art46!vig= | 2026-11-05 |
| D.L. 331/1993 art 47, registration. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art47!vig= | 2026-11-05 |
| D.L. 331/1993 art 50, lists. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1993-08-30;331~art50!vig= | 2026-11-05 |
| D.L. 41/1995 art 36, margin scheme. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1995-02-23;41~art36!vig= | 2026-11-05 |
| D.L. 78/2010 art 21-bis, LIPE. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2010-05-31;78~art21bis!vig= | 2026-11-05 |
| D.L. 98/2011 art 27, regime di vantaggio. Read in part: the paragraphs this file cites. Repeal note. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-07-06;98~art27!vig= | 2026-11-05 |
| D.L. 16/2012 art 3-quater, August date. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2012-03-02;16~art3quater!vig= | 2026-11-05 |
| D.Lgs. 127/2015 art 1, e-invoices and cross-border data. Read in part: the paragraphs this file cites. Commi 3, 3-bis and 6. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art1!vig= | 2026-11-05 |
| D.Lgs. 127/2015 art 2, daily receipts. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-08-05;127~art2!vig= | 2026-11-05 |
| DPR 100/1998 art 1, monthly settlement. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-03-23;100~art1!vig= | 2026-11-05 |
| DPR 542/1999 art 6, annual balance. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1999-12-14;542~art6!vig= | 2026-11-05 |
| DPR 542/1999 art 7, quarterly option. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1999-12-14;542~art7!vig= | 2026-11-05 |
| DPR 322/1998 art 8, annual return. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art8!vig= | 2026-11-05 |
| DPR 600/1973 art 18, simplified accounts. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art18!vig= | 2026-11-05 |
| L. 405/1990 art 6, acconto. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-12-29;405~art6!vig= | 2026-11-05 |
| L. 488/1999 art 7, renovation. Read in part: the paragraphs this file cites. Comma 1(b). | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1999-12-23;488~art7!vig= | 2026-11-05 |
| L. 191/2009 art 2, comma 11. Read in part: the paragraphs this file cites. Comma 11 only. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2009-12-23;191~art2!vig= | 2026-11-05 |
| TUIR art 102, depreciation. Read in part: the paragraphs this file cites. Comma 5. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art102!vig= | 2026-11-05 |
| D.Lgs. 241/1997 art 17, offset. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art17!vig= | 2026-11-05 |
| D.Lgs. 241/1997 art 18, due dates. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art18!vig= | 2026-11-05 |
| D.Lgs. 241/1997 art 19, payment. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art19!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 7, export penalties. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art7!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 8, return content. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art8!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 9, records. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art9!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 11, other violations. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art11!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 12, accessory sanctions. Read in part: the paragraphs this file cites. Commi 1, 1-bis and 2. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art12!vig= | 2026-11-05 |
| D.Lgs. 472/1997 art 12, combined violations. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art12!vig= | 2026-11-05 |
| D.Lgs. 148/2026, act page. Read in part: the paragraphs this file cites. Header and in-force date. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 12, deduction limit. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art12!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 33. Read in full. Other articles of the decree not read. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art33!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 34. Read in part: the paragraphs this file cites. Searched for an application clause. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art34!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 35. Read in part: the paragraphs this file cites. Searched for an application clause. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art35!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 36. Read in part: the paragraphs this file cites. Searched for an application clause. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art36!vig= | 2026-11-05 |
| D.Lgs. 148/2026 art 37. Read in part: the paragraphs this file cites. Searched for an application clause. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;148~art37!vig= | 2026-11-05 |
| D.Lgs. 10/2026, Testo unico IVA, decree page. Read in part: the paragraphs this file cites. Header and in-force date. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10!vig= | 2026-11-05 |
| Testo unico IVA art 1. Read in part: the paragraphs this file cites. Read to confirm the text; the Testo unico is not mapped. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art1!vig= | 2026-11-05 |
| Testo unico IVA art 169. Read in part: the paragraphs this file cites. Read to confirm the text; the Testo unico is not mapped. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art169!vig= | 2026-11-05 |
| Testo unico IVA art 170, repeals. Read in full. Not mapped article by article to 2026 provisions. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art170!vig= | 2026-11-05 |
| Testo unico IVA art 171, application. Read in full. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-01-19;10:1~art171!vig= | 2026-11-05 |
| D.Lgs. 173/2024 Allegato art 102, application. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-11-05;173:1~art102!vig= | 2026-11-05 |
| D.Lgs. 141/2026, decree page. Read in part: the paragraphs this file cites. Header and in-force date. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-05;141!vig= | 2026-11-05 |
| D.Lgs. 141/2026 Allegato art 367, repeals. Read in part: the paragraphs this file cites. Comma 1(d). | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-05;141:1~art367!vig= | 2026-11-05 |
| D.Lgs. 141/2026 Allegato art 368, application. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-05;141:1~art368!vig= | 2026-11-05 |
| Agenzia, Come pagare l'IVA. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/come-pagare-l-iva-imprese | 2026-11-05 |
| Agenzia, F24 IVA periodica. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/f24ivap10/come-e-quando-si-versa | 2026-11-05 |
| Agenzia, Norme generali e aliquote. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/iva-regole-generali-aliquote-esenzioni-pagamento/norme-generali-e-aliquote-imprese | 2026-11-05 |
| Agenzia, LIPE: che cos'e. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/infogen_comunicaz_liquidaz_per_iva | 2026-11-05 |
| Agenzia, LIPE FAQ. Read in part: the paragraphs this file cites. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/faq-liquidaz-iva | 2026-11-05 |
| Agenzia, LIPE model and instructions page. Read in full. Links to the file edition used. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/modello-e-istruzioni-_comunicaz-liquidaz-per-iva | 2026-11-05 |
| Agenzia, LIPE norms page. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/normativa-e-prassi-comunicazione-delle-liquidazioni-periodiche-iva | 2026-11-05 |
| Agenzia, LIPE transmission page. Read in full. Administrative statement. | https://www.agenziaentrate.gov.it/portale/schede/comunicazioni/liquidazioni-periodiche-iva/modalita_trasmissione_liquidaz_per_iva | 2026-11-05 |
| Agenzia, LIPE model and instructions, file edition 2024. Read in part: the paragraphs this file cites. General instructions and lines VP1 to VP14; local text extract. The form page links this edition. | https://www.agenziaentrate.gov.it/portale/documents/20143/5986193/IVA+period_2024.pdf/04990f53-edc9-048a-c953-49592ebea05f?t=1742281742832 | 2026-11-05 |
| Agenzia, LIPE model and instructions, file edition 2023. Read in part: the paragraphs this file cites. Compared with the 2024 edition; local text extract. | https://www.agenziaentrate.gov.it/portale/documents/20143/289118/IVA+periodica_2023.pdf/8828af2c-ef09-69e9-d259-6ac3d189ddc6 | 2026-11-05 |
| Agenzia provvedimento 73203 of 4 April 2018, payment means for fuel and lubricants. Read in full. Administrative statement; local text extract. | https://www.agenziaentrate.gov.it/portale/documents/20143/296703/Provvedimento+04042018+mezzi+pagamento_PROVVEDIMENTO+N_73203+DEL+04-04-2018.pdf/e0e18c4f-b1e5-dfd9-8196-2cac72e65717 | 2026-11-05 |
| Agenzia circ. 8/E of 30 April 2018, fuel sales and payment. Read in part: the paragraphs this file cites. Introduction and the passages on payment means; searched for other art 19-bis.1(d) costs, none named; local text extract. | https://www.agenziaentrate.gov.it/portale/documents/20143/297557/Circolare+n+8+del+30+04+2018_Circolare_N_8_30042018.pdf/7972d001-311b-31f0-f4a0-f7cb1f75090c | 2026-11-05 |
| Agenzia, Dichiarazione IVA 2026 instructions. Read in part: the paragraphs this file cites. Sections on filing, payment, VL, VE, VJ and VX lines and refunds; local text extract. | https://www.agenziaentrate.gov.it/portale/documents/20143/9602686/IVA_ANNUALE_2026_istr.pdf/2a42fb92-1b76-229a-d0f5-06069d79b514?t=1768504755711 | 2026-11-05 |
| MEF note on the split payment extension. Read in full. Press note, reporting a decision whose Official Journal text was not obtained. | https://www.finanze.gov.it/it/archivi/notizie/dettaglio-notizie/Pubblicata-la-decisione-di-proroga-dello-Split-Payment-00001 | 2026-11-05 |
| D.Lgs. 471/1997 art 5, return penalties. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art5!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 6, documents and deduction. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art6!vig= | 2026-11-05 |
| D.Lgs. 471/1997 art 13, payment. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig= | 2026-11-05 |
| D.Lgs. 472/1997 art 13, ravvedimento. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig= | 2026-11-05 |
| D.Lgs. 87/2024 art 5, application. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-06-14;87~art5!vig= | 2026-11-05 |
| DPR 322/1998 art 2, comma 7. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig= | 2026-11-05 |
| L. 207/2024 art 1, commi 57 to 63. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig= | 2026-11-05 |
| L. 190/2014 art 1, regime forfettario. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1!vig= | 2026-11-05 |
| DPR 435/2001 art 17, payment dates. Retained. Read in part: the paragraphs this file cites. | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2001-12-07;435~art17!vig= | 2026-11-05 |

Cited only as they appear in a text above, and not read on their own: DPR 633 art 73(1)(e), in art 74; c.c. art 2359, L. 196/2009 and D.L. 84/2025, in art 17-ter and its notes; D.L. 95/2025 and D.Lgs. 186/2025, in the DPR 633 amendment notes; L. 217/1983 and L. 457/1978, in Tabella A; D.L. 112/2008 and L. 244/2007, in the art 19-bis.1 notes; L. 205/2017 art 1(922) and (923), in the 2018 provvedimento and circ. 8/E 2018; D.L. 155/1993, in the note to L. 405/1990 art 6; D.L. 223/2006, in D.L. 16/2012 art 3-quater; D.Lgs. 74/2000 art 1, in D.Lgs. 471/1997 art 13; D.L. 262/2006, circ. 195/1999 and ris. 104/E 2017, in the LIPE instructions; L. 388/2000 art 34 and ris. 73/E 2017, in the annual instructions; the provvedimento of 21 March 2018, on the Agenzia LIPE pages.

Not yet confirmed: which text governs the Q4 2026 LIPE, Q4 payment, December 2026 monthly payment, annual return and acconto rules for filings made in 2027, and the Testo unico numbering for 2027 periods, including the replacement for D.L. 78/2010 art 21-bis; the transition for deduction rights that arose before D.Lgs. 148/2026 art 12 took effect, and any application clause in articles of that decree not read; the amending act that puts EUR 500,000 and EUR 800,000 into DPR 542/1999 art 7, which prints lire, and the same for the euro amounts of lire 5 million in art 30 and 1 million lire in art 19-bis.2(5); the conflict between L. 190/2014 art 1(58)(e-bis) and (60) on payment dates; the Official Journal text of Decision (EU) 2026/1728, where EUR-Lex returned a bot challenge and the MEF note was used instead, and the 2015 ministerial decree on split payment mechanics; the current EU derogation for the 40% vehicle limit; whether the art 19-bis.1(d) payment sentence reaches costs other than fuel and lubricants; Tabella B letter (f), which takes some vehicles outside the 40% rule; the 2008 ministerial decree defining representation costs; the reach of art 19-bis.1(f) over restaurant service; the legacy statement that import IVA can be deferred to the LIPE since 2022, which no text read supports; L. 244/2007 art 1(18) on renovation; the legal interest rate; the VP12 base and any interest on a carried quarterly amount; the F24 code 6099 in a sibling guide, where the Agenzia code page returned 404; the Intrastat periodicity decree and the art 50(6) provvedimento, including whether a service purchase is listed; the D.L. 746/1983 dichiarazione d'intento rules; the LIPE treatment of the L. 207/2024 art 1(59) logistics option; the reach of D.Lgs. 74/2000 art 1(1)(g-quater)(2); the volume d'affari definition in art 20, which was not read, with line VE50 used; the R-EU-1 to R-EU-11 catalogue; every legacy billing entity, the ABI causale codes and the bank column layouts; the format of the Partita IVA as 'IT + 11 digits'; and the penalty text before the D.Lgs. 87/2024 amendments, for older violations.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.3 | 2026-11-05 | Converted to the upstream template. Tax year moved to 2026 with the 2027 Testo unico boundary stated. Replaced the VP table and field mappings; corrected the Q2 LIPE date, VP14 formula, 0% label, EU services label, spices rate, taxi, flights, telephony, representation, vehicle tests, EUR 516.46 role and processor fees. Added penalties, registration, refunds, split payment persons, the forfettario conflict, D.Lgs. 148/2026 deduction limit, R-IT-9 and Needs Input defaults. Moved onboarding to intake only. |
| 2.2 | November 2026 | Legacy: quarterly limit for services corrected to EUR 500,000. |
| 2.1 | April 2026 | Legacy: full rewrite to the Malta v2.1 structure, 10 sections, country-specific supplier pattern library. |
| 1.0 | | Legacy: initial skill. |

This skill is incomplete without BOTH companion files loaded alongside it: `vat-workflow-base` and `eu-vat-directive`.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista, revisore legale, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
