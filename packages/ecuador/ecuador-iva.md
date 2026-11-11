---
name: ecuador-iva
description: "Ecuador value added tax (Impuesto al Valor Agregado, IVA) for 2026 under the Ley de Régimen Tributario Interno (LRTI) arts. 52 to 74 and its Reglamento. Covers what is taxed and not taxed, the statutory 13% rate raised to 15% by Executive Decree from 1 April 2024 and still in force for 2026 (SRI Circular NAC-DGECCGC25-00000006), the 0% goods and services lists, 5% on construction materials, the 8% holiday tourism rate set by decree, the base, when IVA falls due, imported services and digital services, IVA withholding by agents (30%, 70%, 100%, 10%, 20%), input credit and the proportionality factor, credit balances and exporter refunds, the monthly or six-monthly Formulario 104 return by ninth digit of the RUC, RIMPE, penalties and interest. Trigger on: IVA Ecuador 2026, tarifa IVA 15%, tarifa 0%, formulario 104, declaración de IVA, retención de IVA 70% 100%, crédito tributario IVA, factor de proporcionalidad, servicios digitales IVA, IVA importación de servicios, Ecuador VAT return."
version: 2.1
jurisdiction: EC
tax_year: 2026
last_updated: 2026-11-11
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Ecuador: IVA (value added tax), 2026 v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers Ecuador's IVA for 2026: what is taxed, the rates, the base, withholding, input credit and the monthly or six-monthly return (Formulario 104) in SRI en línea. Income tax is in [ecuador-income-tax](ecuador-income-tax.md) and [ec-corporate-income-tax](ec-corporate-income-tax.md). The special consumption tax (ICE) is not covered.

**Which text of the law.** The LRTI codification published by the SRI's Dirección Nacional Jurídica with last reform 1 April 2026 (arts. 52 to 74), and the Reglamento (RLRTI), SRI codification with last reform 18 November 2025 (arts. 140 to 159). **The rate.** LRTI art. 65 sets 13% and lets the President set the general rate between 13% and 15% by decree. Executive Decree 198 (RO Supl. 520, 18 March 2024) set 15% from 1 April 2024, and Executive Decree 470 (RO Supl. 700, 10 December 2024) kept 15% for 2025. No decree changed it for 2026. RLRTI art. 141 says that without a new decree the last rate set stays in force, and SRI Circular NAC-DGECCGC25-00000006 (26 December 2025) confirms 15% is in force until the President changes it.

**Quick reference (2026).** General rate: 15%. Reduced: 5% on local sales of listed construction materials; 8% on tourism services on holiday dates set by decree. Zero rate: the goods and services in LRTI arts. 55 and 56. Return: Formulario 104, monthly by the ninth digit of the RUC (10th to 28th of the next month); six-monthly for 0%-only sellers. Currency: US dollar.

## Who this applies to

- **Who charges IVA** (agentes de percepción, LRTI art. 63(a.1)):
  - individuals and companies that habitually sell taxed goods or provide taxed services;
  - non-resident providers of digital services that register with the SRI. Registration does not create a permanent establishment (RLRTI art. 147.2).
- **Importers** of taxed goods pay IVA as contribuyentes in the customs declaration, before clearance (arts. 63(a), 70).
- **Importers of services**, and buyers of digital services from unregistered non-residents, are contribuyentes. They self-assess and withhold 100% (art. 70; RLRTI arts. 146, 146.1).
- **Withholding agents** (agentes de retención, art. 63(b); RLRTI art. 147):
  - taxpayers the SRI names as agents and special taxpayers;
  - card issuers, and insurers;
  - public bodies, which withhold 100%;
  - anyone who imports services or issues a purchase settlement (liquidación de compra).
- **RIMPE.**
  - Negocios Populares: their sales are at 0% and they file no IVA return (art. 97.9).
  - RIMPE Emprendedores: they charge IVA and file six-monthly (RLRTI art. 236).
- **Taxable transactions** (arts. 52, 53, 56): transfers of movable tangible goods (including free transfers, consignment sales, leasing with a purchase option, and own use of goods produced or sold), copyrights and industrial property rights, services of any kind provided without an employment relationship, digital services, and imports.
- **Not subject to IVA** (art. 54):
  - contributions in kind to companies;
  - allocations on inheritance or on liquidation of a company or marital partnership;
  - transfers of businesses under the Código de Comercio;
  - mergers, spin-offs and transformations;
  - gifts to public bodies and to non-profits;
  - transfers of shares and other securities;
  - condominium and common-expense fees.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Statutory general rate | 13%; the President may set it between 13% and 15% by decree | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 65) |
| General rate in force in 2026 | 15% (Decree 198 from 1 Apr 2024; Decree 470 for 2025; it stays without a new decree) | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=236482f4-6125-42fd-b073-62c99d08233d&nombre=NAC-DGECCGC25-00000006.pdf (SRI Circular NAC-DGECCGC25-00000006); RLRTI art. 141 |
| Rate before 1 April 2024 | 12% | 2026 | https://www.sri.gob.ec/impuesto-al-valor-agregado-iva (SRI table of decrees) |
| Local sales of construction materials on the SRI list | 5%, from 1 Apr 2024; input IVA that cannot be offset may be expensed for income tax in the year paid | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (unnumbered articles after arts. 55 and 66); RLRTI art. 140.2 |
| Tourism services (Ley de Turismo art. 5) on national or local holidays and the weekend days next to them | may be cut to 8% by executive decree, only for the dates the decree names, only for establishments on the Ministry of Tourism register | 2026 | same (unnumbered article after art. 65) |
| Zero-rated goods | the list in art. 55, summarised under The base | 2026 | same (art. 55) |
| Zero-rated services | the list in art. 56, summarised under The base | 2026 | same (art. 56) |
| Chambers and unions: member fees up to USD 1,500 a year | 0%; fees above USD 1,500 are taxed (the article still says "12%") | 2026 | same (art. 56(23)) |
| Postal and courier imports for personal use, up to 4 kg and customs value up to 5% of the fracción básica (5% × USD 12,208 = USD 610.40) | 0% | 2026 | same (art. 55(15)); RLRTI art. 143; fracción básica from https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf |
| Digital services sold through a platform that delivers goods, card payment with no split of the commission | IVA withheld on 10% of the total paid | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 147.1) |
| Refund of IVA to persons with disabilities and older adults on basic personal goods and services | monthly base up to 2 salarios básicos unificados (2 × USD 482 = USD 964) | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (art. 74 and next article); SBU from https://www.trabajo.gob.ec/wp-content/uploads/downloads/2026/01/ACUERDO-MINISTERIAL-MDT-2025-195.pdf |

**IVA withholding percentages (SRI Resolution NAC-DGERCGC20-00000061 and reforms).** The agent withholds a share of the IVA on the invoice when it pays or credits, whichever is first (RLRTI art. 148).

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Agent buying taxed goods from a supplier that is not a special taxpayer | 30% of the IVA | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/185c7087-f119-4f0d-8dcd-702c30ebd793/NAC-DGERCGC20-00000061.pdf (art. 4(a)) |
| Agent buying services, rights, intermediation commissions or consultancy from a non-special taxpayer | 70% | 2026 | same (art. 4(b)) |
| Professional services of individuals with a higher-education degree (not consultancy contracts); rent of real estate from individuals not keeping accounts; purchase settlements; directors' fees | 100% | 2026 | same (art. 4(c)) |
| Special taxpayer buying goods from another special taxpayer | 10% | 2026 | same (art. 5(a)) |
| Special taxpayer buying services from another special taxpayer | 20% | 2026 | same (art. 5(b)) |
| Construction contracts | 30% | 2026 | same (art. 7) |
| Imported services; imported digital services (by the card issuer or, with no intermediary, the buyer) | 100% | 2026 | same (arts. 8, 9); LRTI art. 70 |
| Habitual exporters named as agents or special taxpayers, on all purchases | 100% | 2026 | same (art. 11) |
| Public sector bodies as agents | 100% | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 63, last paragraph) |
| Not withheld | special taxpayers (except the cases above), state institutions, public companies, airlines, travel agents on air tickets, fuel distributors on fuel, banks on financial services | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/185c7087-f119-4f0d-8dcd-702c30ebd793/NAC-DGERCGC20-00000061.pdf (art. 3); RLRTI art. 148 |

## The base

**Taxable amount (LRTI arts. 58 to 60).**

- **Base** is the full price of the goods or services, including taxes (so ICE is inside the base), service charges and other charges legally part of the price.
- **Deducted from it**: normal discounts and bonuses shown on the invoice, goods and packaging returned, and interest and insurance premiums in instalment sales.
- **Imports**: customs value plus taxes, duties, fees and other charges on the import declaration.
- **Barter, own use and gifts**: market value.
- **Restaurants and hotels**: the legal 10% tip is outside the base (RLRTI art. 145).
- **Reimbursed expenses**: invoice them separately from the fee, with the supporting receipts. IVA applies to the fee only (RLRTI art. 144).

**When IVA falls due (art. 61).**

- **Goods**: on delivery, or on payment or credit to account, whichever is first.
- **Services**: when provided, or on payment or credit, at the taxpayer's choice. The choice must follow a habitual pattern, and the rate applied is the rate on the date of that event (RLRTI art. 141).
- **Work certified by stages**: on each certificate.
- **Own use**: on withdrawal of the goods.
- **Imports**: on customs clearance.
- **Successive supplies**: each period.
- **Imported digital services**: on payment by the resident.

**Zero-rated goods (art. 55), main items.**

- Unprocessed farm, poultry, livestock, bee, rabbit, aquatic, forestry and fish products in their natural state. Cold storage, husking, crushing, mechanical oil extraction, slaughtering, cutting and packing are not processing.
- Natural, pasteurised and powdered domestic milk; cheese and yoghurt; infant formula.
- Bread, sugar, panela, salt, lard, margarine, oats, cornflour, pasta, flour, domestic canned tuna, mackerel, sardine and trout, and edible oils other than olive oil.
- Certified seeds, plants and flowers; animal feed; fertilisers and pesticides; farm inputs; tractors up to 300 hp and farm machinery on the decree lists.
- Human medicines on the annual decree list and their inputs; glucometers, insulin pumps, pacemakers, masks, oximeters, and antibacterial alcohol and gel above 70%.
- Bond paper, newsprint and books.
- Exports.
- Imports by diplomats, passengers within their allowance, gifts to the public sector, temporary admission and transit, and free-zone users.
- Electricity.
- Commercial aircraft.
- Fully electric vehicles, and batteries and chargers for hybrid and electric vehicles.
- Personal postal imports within the limit above.
- Gold bought by the Central Bank or by licensed miners and traders.
- Boats and equipment for artisanal fishing; new fishing vessels.
- Solar photovoltaic equipment and wastewater plants.
- Sanitary towels, tampons, menstrual cups and popular nappies.
- Fuel imports by licensed importers.

**Zero-rated services (art. 56), main items.**

- Domestic land and water passenger and cargo transport; international cargo transport; air cargo to, from and in Galápagos.
- Health services and the manufacture of medicines.
- Rent of property used only as a home.
- Public electricity, drinking water, sewerage, rubbish collection, irrigation and drainage.
- Education at every level; nurseries and old people's homes; religious services; funeral services.
- Artistic and cultural services on the decree list.
- Administrative services of the State for a fee; stock-exchange services.
- **Exported services**, if all four hold: the exporter is resident; the client is not; use takes place entirely abroad; and no one doing business in Ecuador books the payment as a cost.
- Inbound tourism packages sold to non-residents.
- Tolls; the lotteries of Junta de Beneficencia and Fe y Alegría; crop-dusting.
- Services of qualified artisans, and the goods they make and sell, while under the bookkeeping thresholds.
- Cold storage of export perishables; slaughtering and similar.
- Credit life insurance, prepaid medicine, health and life insurance, personal accident insurance, compulsory traffic insurance and farm insurance.
- Member fees up to USD 1,500 a year.
- Construction of social-interest housing in qualified projects.
- Rent of farmland.
- Charging of fully electric vehicles.
- Lodging for foreign tourists (in Ecuador under 90 days, no residence) at registered establishments.

**Financial services** set as such by the regulator are taxed. Other services in a bank's ordinary business that are not set as financial services are not (RLRTI, unnumbered article after art. 141).

**Input credit (art. 66).**

- **What gives credit.** IVA paid on local purchases and imports of fixed assets, goods, raw materials, inputs and services gives credit only if they are used for making taxed sales. The IVA must be shown separately on the sales receipt, import document or withholding receipt. The credit can be used for up to **5 years** from when the return was due.
- **Full credit**: sellers of goods or services at a rate other than 0%; inbound tourism packages; 0% sales direct to exporters; exports.
- **Mixed sellers** (some sales at 0% without credit): credit = the proportion of taxed sales + exports + inbound tourism + 0% sales to exporters over total sales, applied to the IVA on common purchases. Where the accounts can tie a purchase to taxed sales, all its IVA is credited. Where they tie it to 0% sales, none of it is. On the return this is box 563 (factor) and box 564 (credit). The IVA not credited (box 565) can be deducted for income tax.
- **No credit**: businesses whose sales are all at 0%, and State bodies.

The law has no fixed list of blocked purchases. The test is use for taxed sales. Personal spending, and spending tied to 0% or exempt sales, gives no credit.

**Credit balances and refunds (arts. 69, 72).**

- **Carry-forward.** A credit balance carries to the next month (boxes 615 and 617, brought back in boxes 605 and 606).
- **Withholding credits.** If credits from withholdings cannot be used within 6 months, the taxpayer may ask for a refund or offset, within 5 years of payment, without interest.
- **Exporters.** Exporters registered with the SRI get the IVA on exported goods and their inputs refunded without interest within 90 days, with interest after that. Service exporters get the same within the limits of the Comité de Política Tributaria. Crude oil and other non-renewable resources are excluded, except mining exports from 2018.
- **Other refunds.** Separate refund rules cover real-estate projects, social housing, zero-emission vehicle leasing, persons with disabilities, older adults, and audiovisual production (arts. 72 to 74 and the articles that follow them).

## Deadlines and filing

| Item | Deadline | Source URL |
|---|---|---|
| Monthly return and payment (anyone with sales at a rate other than 0%, or who withholds IVA) | by ninth digit of the RUC: 1 = 10th, 2 = 12th, 3 = 14th, 4 = 16th, 5 = 18th, 6 = 20th, 7 = 22nd, 8 = 24th, 9 = 26th, 0 = 28th of the following month | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 158); LRTI art. 67 |
| Six-monthly return (only 0% or untaxed sales, or all IVA withheld at 100%, and not a withholding agent) | January to June: same digit days in July; July to December: same digit days in January | same (RLRTI art. 158); https://www.sri.gob.ec/impuesto-al-valor-agregado-iva |
| RIMPE Emprendedor | six-monthly and cumulative, by ninth digit | https://www.sri.gob.ec/impuesto-al-valor-agregado-iva; RLRTI art. 236 |
| Sales on credit of a month or more | IVA on the credit part may be declared the month after next | LRTI art. 67 |
| State bodies and public companies; Galápagos | up to the 20th of the next month; Galápagos up to the 28th | RLRTI art. 158 |
| Due date on a holiday or rest day | moves to the next business day, unless that falls in the next month; then it moves back to the last business day of the month | same |
| Imports of goods | IVA in the import declaration, paid before clearance | LRTI art. 70; RLRTI art. 158 |
| Zero or nil periods | the return is still due, except for individuals not keeping accounts who only import services | RLRTI art. 158 |

**How to file Formulario 104, step by step** (SRI guide to the IVA return).

1. Log in to SRI en línea with the RUC and password. Go to Declaraciones, then Declaración de Impuestos, then Elaboración y envío de declaraciones, and choose the IVA form and period.
2. **Sales.** Taxed local sales go in boxes 401 and 402 (gross), with net in 411 and 412 and IVA in 421 and 422. Tourism establishments on a decree date pick the reduced rate in box 203 and use boxes 410 and 420. 0% sales without credit go in 403 and 404; 0% sales with credit in 405 and 406. Exports of goods go in 407 and services in 408. Untaxed or exempt transfers go in 431. Total sales: 419; total IVA generated: 429.
3. **Sales on credit.** Boxes 480 to 485 split this month's cash and credit sales. 484 is the IVA due this month; 485 carries the rest to 483 next month.
4. **Purchases.** Taxed purchases with credit go in boxes 500 and 501. Compute the factor in box 563 as (411 + 412 + 420 + 415 + 416 + 417 + 418) / 419, and the credit in box 564. The IVA not credited goes in box 565 (deductible for income tax).
5. **Tax summary.** Box 601 holds the IVA due, or box 602 the credit (never both). Bring the prior credit forward into 605 and 606. This must be no more than last period's 615 and 617. Enter withholdings suffered in 609 and carry forward any balance into 615 and 617.
6. **As a withholding agent**, enter the IVA withheld: 10% and 20% in boxes 721 and 723; 30%, 50%, 70% and 100% in boxes 725, 727, 729 and 731. Imported services go in 731.
7. Submit. The system shows the total to pay (box 902). Pay by the ninth-digit date. An amended return records earlier payments in box 890.

## Penalties and interest

| Item | Rule | Source URL |
|---|---|---|
| Late return with IVA to pay | 3% per month or part of a month, on the IVA to pay after credit, cap 100% of it | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 100) |
| Late return with no IVA to pay | 0.1% of the period's sales per month or part of a month, cap 5% of those sales | same |
| Fine not self-assessed and paid | collected by the SRI increased by 20% | same |
| Late payment or declaration of IVA withheld | same deadlines, fines and surcharges as the return; withholding agents carry the income tax withholding agents' obligations and penalties | RLRTI art. 158; LRTI art. 63 |
| Interest | Banco Central del Ecuador 90-day active reference rate, per month (part month counts as a full month); 1.3 times that rate on tax assessed by the SRI | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf (CT art. 21) |
| Surcharge on IVA assessed by the SRI | 20% of the principal | same (CT art. 90) |
| False information in an exporter refund claim | fine of twice the amount sought | LRTI art. 72 |
| Undue IVA refund to a disabled or older person for non-basic or non-personal purchases | refund plus a 100% fine | LRTI art. 74 |

## Cross-border points

- **Exports of goods** are 0% with full credit and an IVA refund (arts. 55(8), 57, 66, 72).
- **Exports of services** are 0% only if all four conditions in art. 56(14) are met. Otherwise charge 15%.
- **Imported services**: the Ecuadorian buyer issues a liquidación de compra, self-assesses the IVA, withholds 100%, declares it in its monthly return (box 731), and takes the same IVA as input credit if the service is used for taxed sales (art. 70; RLRTI arts. 146, 147).
- **Imported digital services** (the RLRTI art. 140.1 list: SaaS, streaming, cloud, online advertising, platforms and similar):
  - If the non-resident provider is registered with the SRI, it charges and declares the IVA.
  - If it is not registered and the buyer pays by card, the card issuer withholds 100%; the card statement is the withholding receipt.
  - If it is not registered and there is no intermediary, the buyer self-assesses and withholds 100%.
  - For delivery platforms, the IVA is on the commission. Where it is not split out, the base is 10% of the total.
  - The SRI publishes a list of unregistered providers every quarter (RLRTI arts. 140.1, 146.1, 147.1, 148.1).
- **Imports of goods**: IVA on customs value plus duties, paid before clearance (arts. 59, 70).

## Two worked examples that recompute

### Example 1: monthly return for a consultancy, with withholdings and an imported service

Servicios Andinos Cía. Ltda. provides consulting (15%). It is a withholding agent but not a special taxpayer. In March 2026 it invoices USD 20,000 plus IVA to clients who are all withholding agents. Its taxed local purchases are USD 8,000 plus IVA. It also pays USD 500 to a non-resident for a consulting service used in Ecuador. It has no credit brought forward.

- Output IVA: 20,000 × 15% = **USD 3,000** (box 401 and 411; IVA 421).
- Imported service: the company issues a liquidación de compra and self-assesses 500 × 15% = **USD 75**. It withholds 100% of it (box 731) and pays that USD 75 with the return.
- Input credit: 8,000 × 15% = 1,200, plus the USD 75 on the imported service = **USD 1,275**.
- IVA due: 3,000 − 1,275 = **USD 1,725** (box 601).
- Withholdings suffered: the clients withheld 70% of the IVA on services, 3,000 × 70% = **USD 2,100** (box 609). That is more than the IVA due, so nothing is due on its own sales. **USD 375** of withholding credit carries forward (box 617).
- To pay with the April return date (by ninth digit): only the **USD 75** withheld on the imported service.

```oa-check
name: EC IVA March 2026, consultancy, 70% withholdings suffered, imported service
inputs:
  sales: 20000
  purchases: 8000
  imported_service: 500
  rate: 0.15
  withholding_share: 0.70
steps:
  - output_iva: sales * rate
  - import_iva: imported_service * rate
  - input_credit: purchases * rate + import_iva
  - iva_due: output_iva - input_credit
  - withheld_by_clients: output_iva * withholding_share
  - carry_forward: max(0, withheld_by_clients - iva_due)
  - own_iva_payable: max(0, iva_due - withheld_by_clients)
  - total_to_pay: own_iva_payable + import_iva
expected:
  output_iva: 3000
  import_iva: 75
  input_credit: 1275
  iva_due: 1725
  withheld_by_clients: 2100
  carry_forward: 375
  own_iva_payable: 0
  total_to_pay: 75
```

### Example 2: mixed seller, proportionality factor or direct attribution? (a decision worked both ways)

A clinic that also runs a café has, in a month, USD 60,000 of café sales at 15% and USD 40,000 of health services at 0% without credit. Its purchases carry USD 3,000 of IVA, all of it on shared costs (rent, utilities, cleaning). Output IVA is 60,000 × 15% = USD 9,000.

- **Proportionality factor** (art. 66(2); box 563): 60,000 / 100,000 = 0.60. Credit = 3,000 × 0.60 = **USD 1,800**. IVA to pay = 9,000 − 1,800 = **USD 7,200**. The USD 1,200 not credited goes to box 565 and is deductible for income tax.
- **Direct attribution**, if its accounts separate costs without doubt: say USD 2,500 of the IVA ties to the café and USD 500 to the clinic. Credit = **USD 2,500**. IVA to pay = **USD 6,500**. The USD 500 tied to 0% sales gives no credit and is deductible for income tax.
- **The figure that decides** is the share of input IVA the accounts can tie to taxed sales. Here it is 2,500 / 3,000 = 83%, above the 60% factor, so direct attribution saves USD 700 a month. Below 60%, the factor is better. Direct attribution needs accounting that separates the costs without doubt.

```oa-check
name: EC IVA 2026, mixed seller, factor against direct attribution
inputs:
  taxed_sales: 60000
  zero_sales: 40000
  input_iva: 3000
  attributed_to_taxed: 2500
  rate: 0.15
steps:
  - output_iva: taxed_sales * rate
  - factor: taxed_sales / (taxed_sales + zero_sales)
  - credit_factor: input_iva * factor
  - pay_factor: output_iva - credit_factor
  - not_credited_factor: input_iva - credit_factor
  - pay_direct: output_iva - attributed_to_taxed
  - saving: pay_factor - pay_direct
  - share_attributed: round(attributed_to_taxed / input_iva, 4)
expected:
  output_iva: 9000
  factor: 0.60
  credit_factor: 1800
  pay_factor: 7200
  not_credited_factor: 1200
  pay_direct: 6500
  saving: 700
  share_attributed: 0.8333
```

## Ask the client first

1. What does the RUC show: general regime, RIMPE Emprendedor or Negocio Popular, special taxpayer, withholding agent, habitual exporter? This sets the return frequency and which withholding percentages apply both ways.
2. What does it sell, and at which rate (15%, 5% construction materials, 0% list, exports, tourism on decree dates)? Does it have any 0% sales without credit?
3. Do its purchases tie to taxed or 0% sales, and do its accounts separate them?
4. Does it import goods, services or digital services, and how does it pay non-residents (card, transfer, platform)?
5. Withholdings suffered and made this period, and any credit balance brought forward (boxes 615 and 617 of the last return).
6. The ninth digit of the RUC, the period, and any sales on credit of a month or more.

## Sources

| Source | URL | Read on |
|---|---|---|
| LRTI, SRI codification, last reform 2026-04-01: arts. 52-74 with the unnumbered articles after 55, 63, 65, 66 and 72, art. 97.9 and art. 100 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| RLRTI, SRI codification, last reform 2025-11-18: arts. 140-151 (including 140.1, 140.2, 146.1, 147.1, 147.2, 148.1) and 158 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| SRI Circular NAC-DGECCGC25-00000006 (26 Dec 2025): the 15% rate stays in force until a new decree | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=236482f4-6125-42fd-b073-62c99d08233d&nombre=NAC-DGECCGC25-00000006.pdf | 2026-11-11 |
| SRI, IVA page: who files, monthly and six-monthly deadlines, RIMPE Emprendedor, table of rate decrees (198, 190, 644) and the 5% construction rate | https://www.sri.gob.ec/impuesto-al-valor-agregado-iva | 2026-11-11 |
| SRI Resolution NAC-DGERCGC20-00000061 (RO Ed. Esp. 1100, 30 Sep 2020): IVA withholding percentages, arts. 3-5, 7-9, 11 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/185c7087-f119-4f0d-8dcd-702c30ebd793/NAC-DGERCGC20-00000061.pdf | 2026-11-11 |
| SRI guide: Elaboración y envío de la declaración del IVA (box-by-box Formulario 104) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/e084fae5-9677-450c-8161-21e7c3a9f65b/Gu%C3%ADa%20para%20el%20llenado%20del%20Formulario%20Impuesto%20al%20Valor%20Agregado%20IVA.PDF | 2026-11-11 |
| SRI Resolution NAC-DGERCGC25-00000043: 2026 fracción básica USD 12,208 (postal import limit) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf | 2026-11-11 |
| Código Tributario, SRI codification, last modification RO 372 of 10 Aug 2023: arts. 21 and 90 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf | 2026-11-11 |
| Ministerio del Trabajo, Acuerdo Ministerial MDT-2025-195: SBU USD 482 from 1 Jan 2026 | https://www.trabajo.gob.ec/wp-content/uploads/downloads/2026/01/ACUERDO-MINISTERIAL-MDT-2025-195.pdf | 2026-11-11 |

Not yet confirmed:
- the 2026 decrees and dates for the 8% tourism rate (none was read from an official text);
- the current list of construction materials at 5%;
- whether NAC-DGERCGC20-00000061 has later reforms changing the 30%, 70% and 100% rates (the SRI form guide still cites it);
- the time limit for issuing an IVA withholding receipt;
- whether electronic invoices are a condition of input credit beyond showing the IVA separately;
- how bank interest is treated as against bank fees;
- the RIMPE Emprendedor six-monthly calendar for 2026;
- Andean Community Decision 599 on services between member states;
- the ZEDE regime beyond the free-zone rule in art. 55(9)(e);
- the art. 56(23) reference to a "12%" rate, which predates the current rate.
