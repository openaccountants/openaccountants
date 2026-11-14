---
name: co-vat-return
description: >
  Colombian VAT (IVA, impuesto sobre las ventas) for 2026: who must register as responsable de IVA (the
  3,500 UVT tests in ET art. 437 par. 3, 4,000 UVT for State contractors), what is taxed (art. 420), the
  19% general rate (art. 468), the 5% goods and services (arts. 468-1, 468-3), excluded goods and services
  with no credit (arts. 424, 476: health, education, public transport and freight, utilities, residential
  rent, interest, hosting and cloud) and exempt supplies with credit and refund (arts. 477, 478, 481:
  fresh meat, milk, eggs, rice, exports of goods and services), the base and tax point, input IVA and its
  limits (arts. 485, 488, 490, 491, 496), IVA withholding at 15% (arts. 437-1, 437-2), bimonthly or
  four-monthly periods at 92,000 UVT (art. 600), Form 300 boxes, 2026 deadlines by NIT and penalties.
  UVT 2026 COP 52,374. Trigger on: IVA Colombia, declaración de IVA formulario 300, responsable de IVA,
  no responsable 3.500 UVT, IVA bimestral cuatrimestral, IVA descontable, reteIVA, exportación de
  servicios IVA, Colombian VAT return.
version: 1.2
jurisdiction: CO
category: international
tax_year: 2026
last_updated: 2026-11-14
type: computation
depends_on:
  - vat-workflow-base
tier: 2
domain: vat-gst
---

# Colombia: IVA (VAT) return, 2026 v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Tax year.** Calendar 2026: the bimonthly periods January-February to November-December 2026, or the four-monthly periods January-April to September-December 2026. One UVT is **COP 52,374** for 2026 (DIAN Resolución 000238 of 15 December 2025).

**Which text of the law.** The Estatuto Tributario (ET) Libro III as consolidated on the Senate's official site, updated there to 15 October 2026. Changes in 2026: Ley 2615 de 2026 rewrote art. 478 (books, magazines and music), and Decreto Legislativo 240 de 2026 moved online gambling out of IVA into a separate 16% tax for 2026 (arts. 420(e), 512-22). Deadlines: Decreto Único Reglamentario 1625 de 2016 (DUR), arts. 1.6.1.13.2.30 and 1.6.1.13.2.31, substituted by Decreto 2229 de 2023.

Related skills: [colombia-income-tax](colombia-income-tax.md) (an IVA responsable individual must file income tax), [co-corporate-income-tax](co-corporate-income-tax.md), and the approved [formalizing-small-informal-businesses-in-colombia](formalizing-small-informal-businesses-in-colombia.md) (RUT and Régimen Simple sign-up, not repeated). `colombia-iva.md` in this folder is an older duplicate of this skill.

## Who this applies to

- **Responsables de IVA** (art. 437): merchants and anyone habitually selling goods, anyone providing services, importers, and buyers who must self-assess (see Cross-border points).
- **No responsables** (art. 437 par. 3): individual retailers and artisans, small farmers and stockbreeders, and individuals providing services, but only if they meet **all** of these: gross income from the activity under 3,500 UVT (COP 183,309,000) in 2025 and in 2026; one business premises at most; no franchise, concession or royalty arrangement there; not a customs user; no single taxed contract of 3,500 UVT or more in 2025 or 2026; and bank deposits and investments from taxed activity not over 3,500 UVT. The limit is 4,000 UVT (COP 209,496,000) for individuals whose income comes from contracts with the State (par. 5). A no responsable may not add IVA to its prices; if it does, it takes on all the obligations of a responsable (par. 1). Before signing a taxed contract of more than 3,500 UVT, it must register as responsable.
- **Companies**: the art. 437 par. 3 exception names individual retailers and artisans, small farmers and stockbreeders and service providers; treat a company making taxed supplies as a responsable unless a source confirms otherwise (see Not yet confirmed).
- **Régimen Simple members** are not responsables if they only run small shops, minimarkets or hairdressers (art. 908(1)), or are individuals with gross income under 3,500 UVT (art. 437 par. 4).
- **Out of scope**: the municipal industry and commerce tax (ICA), which is not IVA; the national consumption tax (impuesto nacional al consumo) on restaurants and bars, the special IVA rules for construction (AIU) and gambling, free-zone and international marketing company details, and the IVA refund procedure.

## Rates, bands and thresholds

| Item | Rate or figure | Year | Source URL |
|---|---|---|---|
| UVT for 2026 | COP 52,374 (DIAN Resolución 000238 of 15 Dec 2025) | 2026 | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0238_2025.htm |
| General rate | 19% | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr019.html (art. 468) |
| Reduced rate, goods listed by tariff heading (for example coffee, wheat, industrial maize and rice, flours, sugar, table chocolate, dry pasta, animal feed, raw vegetable oils, farm machinery and tools, natural-gas vehicle kits) | 5% | 2026 | same (art. 468-1) |
| Reduced rate, services (storage of farm products in bonded warehouses, farm insurance, prepaid medicine and complementary health plans, health insurance policies, certain cleaning and security services by solidarity entities employing people with disabilities) | 5% | 2026 | same (art. 468-3) |
| Domestic passenger air tickets | 19%: the 5% rate in art. 468-3(5) ran only to 31 December 2022; routes with no organised land transport and listed tourist routes are excluded (art. 476(10)) | 2026 | same (arts. 468-3(5), 476(10)) |
| Excluded services, no IVA and no credit (art. 476): medical, dental, hospital and lab services; recognised education; public land, river and sea passenger transport, and all cargo transport; public energy, water, sewerage, refuse and household gas; residential rent; interest and leasing; web pages, hosting and cloud computing; cinema, sport and cultural tickets; funeral services; internet for stratum 3 homes | 0%, no IVA | 2026 | same (art. 476) |
| Excluded goods (art. 424), for example fresh potatoes, paddy rice, most medicines, personal computers worth up to 50 UVT (COP 2,618,700, computed at the 2026 UVT of COP 52,374) | 0%, no IVA | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr017.html (art. 424) |
| Exempt goods with right to credit and refund (art. 477), for example fresh or frozen beef, pork, chicken and fish, milk, fresh cheese, fresh eggs, rice for human consumption, infant formula | 0% with credit | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr019.html (art. 477) |
| Books and magazines of scientific and cultural character, and musical works | exempt; instruments and inputs for luthiers excluded (Ley 2615 de 2026) | 2026 | same (art. 478) |
| Exports of goods, sales to international marketing companies for export, services used exclusively abroad by non-residents with no business in Colombia, tourist services to non-residents | exempt with bimonthly refund | 2026 | same (art. 481) |
| No responsable threshold (individuals) | 3,500 UVT (COP 183,309,000); 4,000 UVT (COP 209,496,000) for State contractors; COP amounts computed at the 2026 UVT of COP 52,374 | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr017.html (art. 437 par. 3, 5) |
| IVA withholding (reteIVA), general | 15% of the IVA, unless a decree sets another rate up to 50% | 2026 | same (art. 437-1) |
| IVA withholding on services from non-residents (art. 437-2(3) and (8)) | 100% of the IVA, by the Colombian buyer | 2026 | same (art. 437-1 par. 1) |
| Bimonthly filing | grandes contribuyentes, those with gross income of 92,000 UVT (COP 4,818,408,000, computed at the 2026 UVT of COP 52,374) or more at 31 Dec 2025, and art. 477 and 481 exporters | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr025.html (art. 600(1)) |
| Four-monthly filing | everyone else: gross income under 92,000 UVT | 2026 | same (art. 600(2)) |
| Input IVA timing | in the period of the tax point or the next 3 bimonthly periods (bimonthly filers) or the next 1 four-monthly period | 2026 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr020.html (art. 496) |

## The base

**What is taxed (art. 420).** The sale of movable and immovable goods unless excluded; the sale of industrial-property intangibles; services provided in Colombia **or from abroad** unless excluded; imports of goods unless excluded. The sale of fixed assets is not taxed, except residential property, vehicles and assets habitually sold for third parties, and aircraft (par. 1).

**Tax point (art. 429).** Goods: the date of the invoice, or delivery if there is none. Services: the earliest of the invoice date, the end of the service, or payment. Imports: at customs clearance, paid with the customs duties.

**Base (arts. 447, 459).** The full value of the transaction, including financing charges, transport, installation, insurance, commissions and other extras, even if invoiced separately. Interest on financing the IVA itself is not in the base. Imports: the customs value plus customs duty.

**Excluded and exempt are different.** An **excluded** supply (arts. 424, 476) carries no IVA and the input IVA on it is not creditable: it becomes a cost. An **exempt** supply (arts. 477, 478, 481) is at 0% and its input IVA is creditable and refundable.

**Input IVA (impuestos descontables).**

1. Creditable: IVA invoiced on goods and services bought, and IVA paid on imports (art. 485).
2. Only if the purchase is a cost or expense for income tax and is used for taxed operations (art. 488), and backed by an invoice meeting arts. 617 and 618 (art. 771-2).
3. IVA on fixed assets is **not** creditable in IVA (art. 491); a responsable can instead take it as a discount against income tax in the year paid or later (art. 258-1).
4. Common inputs used for both taxed or exempt and excluded operations, that cannot be traced, are credited in proportion to the period's taxed and exempt operations over all operations (art. 490, prorrata). See Example 2.
5. Book it in the period of the tax point or the next three bimonthly periods (one four-monthly period) and claim it in the return of the period it was booked (art. 496).
6. Purchases from a no responsable carry no IVA and give no credit.

**Withholding (reteIVA).** State entities, grandes contribuyentes, entities DIAN designates, card issuers and responsables buying services from non-residents withhold IVA on payment or crediting, whichever is first (arts. 437-1, 437-2). The general rate is 15% of the IVA. The supplier claims the IVA withheld in box 85 in the period or the next three periods, if booked in the period.

**Classifying common bank-statement lines.** The Estatuto decides, not the supplier's name (art. 476 numbers as read on 14 Nov 2026):

- **Banks and cards.** Interest and financial yields on credit operations and financial leasing are excluded (art. 476(16)); so are foreign-exchange operations (476(27)) and commissions for the use of credit and debit cards (476(28)). Other bank fees are not on the list: treat them as taxed at 19% unless an exclusion is shown.
- **Utilities.** Public energy services (476(11)), water, sewerage and refuse services (476(12)) and household gas (476(13)) are excluded, whoever the customer is. Internet connection is excluded only for residential users in stratum 3 (476(7)); local telephone service is excluded only for the first 325 minutes a month billed to strata 1, 2 and 3 and for public telephones (476(8)). Business mobile and internet: 19%.
- **Transport.** Public land, river and sea passenger transport in Colombia (476(9)) is excluded. Domestic air tickets are 19% since the 5% rate of art. 468-3(5) ended on 31 December 2022, except routes with no organised land transport and the listed tourist routes, which are excluded (476(10)).
- **Rent and cloud.** Residential rent is excluded (476(15)); commercial rent is 19%. Web pages, hosting and cloud computing are excluded (476(21)).
- **Insurance.** Prepaid medicine, complementary health plans and health insurance policies are 5% (art. 468-3); compulsory health plans of the social security system are excluded (476(3)). No general exclusion for other insurance was found in art. 476: confirm before treating a premium as excluded.
- **Food and medicines.** Rice for human consumption, fresh eggs, milk and fresh meat are exempt with credit (art. 477); most medicines and paddy rice are excluded (art. 424). The difference matters to the seller (credit and refund), not to the buyer: neither carries IVA to credit.

**Conservative defaults when facts are missing.** Treat a sale as taxed at 19% until a 5%, excluded or exempt rule is shown (arts. 468, 468-1, 468-3, 424, 476, 477); treat an export as domestic until the export proof is in hand (art. 481); give no credit without a valid invoice to the buyer (art. 771-2), on a purchase from a no responsable, on a fixed asset (art. 491), or on a business-use share that is not documented (art. 488).

**When only bank totals are available.** Treat each total as IVA-inclusive: at 19%, net = total x 100 / 119 and IVA = total x 19 / 119; at 5%, net = total x 100 / 105. Give no credit on any payment without a valid electronic invoice, list the missing invoices and ask for them. Colombian bank statements write pesos with a full stop for thousands and no decimals: $119.000.000 is COP 119,000,000.

**E-invoicing.** Invoices and equivalent documents form the invoicing system that DIAN regulates, including electronic documents (art. 616-1). Costs and input IVA need a valid invoice (art. 771-2).

## Deadlines and filing

| Period | Due date for 2026 periods | Rule |
|---|---|---|
| Bimonthly: Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct 2026, Nov-Dec 2026 | March, May, July, September, November 2026 and January 2027: 7th business day (NIT ending 1) to 16th business day (ending 0), by the last digit of the NIT, ignoring the check digit | DUR art. 1.6.1.13.2.30 |
| Four-monthly: Jan-Apr, May-Aug, Sep-Dec 2026 | May 2026, September 2026, January 2027: same day pattern | DUR art. 1.6.1.13.2.31 |
| No operations in a period | no return is due for a period with no taxed operations and nothing creditable or adjustable | ET art. 601; DUR art. 1.6.1.13.2.31 par. 1 |

**Form 300, step by step.** File online through DIAN's filing service; box 980 (total paid) is always zero on the return, and payment is made separately by the due date. Box 24 is the periodicity (bimonthly 01 to 06, four-monthly 01 to 03).

| Step | Form 300 boxes |
|---|---|
| Income by type | 27 taxed at 5%, 28 taxed at 19%, 29 AIU base, 30 exports of goods (FOB), 31 exports of services, 32 sales to international marketing companies, 33 sales to free zones, 35 exempt, 39 excluded, 40 not taxed; 41 gross; 42 returns; 43 net |
| Purchases | 44 to 49 imports, 50 to 54 domestic purchases by rate; 55 gross; 56 returns; 57 net |
| IVA generated | 58 at 5%, 59 at 19%, 60 AIU, 65 own use and gifts, 66 IVA recovered on purchase returns; 67 total |
| IVA creditable | 68 to 70 imports, 71 to 75 purchases by rate; 77 total; 78 IVA withheld on non-resident services; 79 IVA on sales returns; 80 adjustments; 81 total creditable |
| Result | 82 balance due for the period (67 minus 81) or 83 credit (81 minus 67); 84 last period's credit; 85 IVA withheld from you; 86 balance due on tax; 87 penalties (at least 10 UVT); 88 total to pay or 89 total credit; 90 to 93 credit balance control |

## Penalties and interest

- **Late filing (art. 641):** 5% of the tax per month or part month, up to 100%.
- **Not filing after a summons (art. 643(2)):** 10% of the higher of the bank deposits or gross income found by DIAN, or gross income in the last IVA return.
- **Own correction (art. 644):** 10% of the extra tax before a DIAN summons, 20% after.
- **Inaccuracy (art. 648):** 100% of the difference found by DIAN.
- **Minimum penalty (art. 639):** 10 UVT (COP 523,740).
- **Late payment interest (arts. 634, 635):** daily, at the consumer-credit usury rate minus 2 points.

## Cross-border points

- **Services from abroad** used in Colombia are taxed (art. 420(c)). When a responsable buys a taxed service from a non-resident, it withholds 100% of the IVA (arts. 437-1 par. 1, 437-2(3)), declares it, and may credit it in box 78. Foreign providers of digital services to non-responsables register and declare under the DIAN procedure, and need not issue invoices (art. 437 par. 2).
- **Imports**: IVA on the customs value plus duty, paid with the customs declaration (arts. 429(d), 459), credited in boxes 68 to 70.
- **Exports**: goods and services used exclusively abroad by non-residents with no business in Colombia are exempt with refund (art. 481); keep the documents that prove the export. Exporters file bimonthly (art. 600(1)).

## Two worked examples that recompute

### Example 1: consulting company, bimonthly, with exports and reteIVA

Andes Consultores SAS (gross income over 92,000 UVT, so bimonthly) has, in March-April 2026: domestic consulting of COP 100,000,000 at 19%; consulting for a US client with no business in Colombia of COP 80,000,000 (exempt export, art. 481(c)); purchases of taxed services of COP 40,000,000 plus 19% IVA, all used in the business. Its domestic client is a gran contribuyente and withheld 15% of the IVA.

- IVA generated (boxes 59, 67): 19% x 100,000,000 = COP 19,000,000. The export goes in box 31 with no IVA.
- IVA creditable (boxes 75, 81): 19% x 40,000,000 = COP 7,600,000. The export is exempt, not excluded, so no proration is needed.
- Box 82: 19,000,000 minus 7,600,000 = COP 11,400,000.
- IVA withheld (box 85): 15% x 19,000,000 = COP 2,850,000.
- To pay (box 88): **COP 8,550,000**, in May 2026 on the business day for its NIT's last digit.

```oa-check
name: CO IVA 2026, bimonthly consulting with export and reteIVA
inputs:
  domestic_sales: 100000000
  export_sales: 80000000
  taxed_purchases: 40000000
steps:
  - iva_generated: domestic_sales * 0.19
  - iva_export: export_sales * 0
  - iva_creditable: taxed_purchases * 0.19
  - box_82: iva_generated - iva_creditable
  - reteiva: iva_generated * 0.15
  - to_pay: box_82 - reteiva
expected:
  iva_generated: 19000000
  iva_export: 0
  iva_creditable: 7600000
  box_82: 11400000
  reteiva: 2850000
  to_pay: 8550000
```

### Example 2: individual landlord, registration and proration

Marta, an individual, rents a shop for COP 16,000,000 a month and a flat for COP 5,000,000 a month throughout 2026. She files four-monthly (income under 92,000 UVT).

- **Must she register?** Her taxed income (commercial rent) is 12 x 16,000,000 = COP 192,000,000, above 3,500 UVT (COP 183,309,000), so she is a responsable de IVA (art. 437 par. 3). The residential rent is excluded and does not count as taxed activity. At COP 15,000,000 a month (COP 180,000,000 a year) she would stay a no responsable if she also met the other five conditions.
- **January-April 2026:** IVA on commercial rent 19% x 64,000,000 = COP 12,160,000. Residential rent 20,000,000 goes in box 39 (excluded).
- **Common costs:** building maintenance for both properties with IVA of COP 1,900,000 cannot be traced to either. Credit 1,900,000 x 64,000,000 / 84,000,000 = COP 1,447,619 (art. 490); the other COP 452,381 is a cost for income tax.
- **To pay:** 12,160,000 minus 1,447,619 = COP 10,712,381 (COP 10,712,000 on the form), in May 2026.

```oa-check
name: CO IVA 2026, landlord threshold and art. 490 proration
inputs:
  uvt: 52374
  commercial_rent_month: 16000000
  residential_rent_month: 5000000
  common_iva: 1900000
steps:
  - threshold: 3500 * uvt
  - taxed_income_year: commercial_rent_month * 12
  - over_threshold: taxed_income_year - threshold
  - commercial_period: commercial_rent_month * 4
  - residential_period: residential_rent_month * 4
  - iva_generated: commercial_period * 0.19
  - creditable: common_iva * commercial_period / (commercial_period + residential_period)
  - not_creditable: common_iva - creditable
  - to_pay: iva_generated - creditable
expected:
  threshold: 183309000
  taxed_income_year: 192000000
  over_threshold: 8691000
  iva_generated: 12160000
  creditable: 1447619.05
  not_creditable: 452380.95
  to_pay: 10712380.95
```

## Ask the client first

1. Individual or company? For an individual: gross income from taxed activity in 2025 and 2026, number of premises, franchises, customs status, largest single contract, and bank deposits from taxed activity (the six art. 437 par. 3 tests).
2. Gross income at 31 December 2025 (bimonthly at 92,000 UVT or more) and whether DIAN has made it a gran contribuyente.
3. What it sells: the goods by tariff heading or the services, to classify each at 19%, 5%, excluded or exempt; any exports, with the proof.
4. Purchases and imports with valid invoices, which are fixed assets, and which inputs serve both taxed and excluded operations.
5. IVA withheld by customers (certificates), services bought from non-residents, last period's credit balance.
6. The last digit of the NIT, for the due date.

## Sources

| Source | URL | Read on |
|---|---|---|
| DIAN Resolución 000238 of 15 Dec 2025: UVT 2026 = COP 52,374 | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0238_2025.htm | 2026-11-11 |
| ET arts. 420, 424, 429, 437 (par. 1 to 5), 437-1, 437-2 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr017.html | 2026-11-11 |
| ET arts. 447, 459 (base) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr018.html | 2026-11-11 |
| ET arts. 468, 468-1, 468-3, 476, 477, 478 (as amended by Ley 2615 de 2026), 481, 485, 488 | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr019.html | 2026-11-11 |
| ET arts. 476 (numbers 3, 7 to 13, 15, 16, 21, 27, 28) and 488, reopened: read for the classification notes in The base | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr019.html | 2026-11-14 |
| ET arts. 490, 491, 496 (proration, fixed assets, timing) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr020.html | 2026-11-11 |
| ET arts. 512-22 (online gambling, Decreto Legislativo 240 de 2026) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr021.html | 2026-11-11 |
| ET arts. 600, 601, 616-1 (periods, who files, invoicing) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr025.html | 2026-11-11 |
| ET art. 258-1 (IVA on fixed assets as income tax discount) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr010.html | 2026-11-11 |
| ET arts. 634, 635, 639, 641, 643, 644, 648 (interest and penalties) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr026.html | 2026-11-11 |
| ET art. 771-2 (invoices) | http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr031.html | 2026-11-11 |
| DUR 1625 de 2016, arts. 1.6.1.13.2.30 and 1.6.1.13.2.31 (IVA deadlines), DIAN normograma | https://normograma.dian.gov.co/dian/compilacion/docs/decreto_1625_2016.htm | 2026-11-11 |
| DIAN, Form 300 and instructions (boxes 24 to 102, 980) | https://www.dian.gov.co/atencionciudadano/formulariosinstructivos/Formularios/2025/Formulario_300_2025.pdf | 2026-11-11 |

Not yet confirmed: the decree rates of IVA withholding other than the 15% default (up to 50% allowed); the calendar dates of the 2026 and January 2027 deadlines (only the business-day rule was read); the full tariff lists of arts. 424, 468-1 and 477 (only examples are given here, check the heading); whether an individual below the thresholds may register voluntarily; whether a company providing services can use the art. 437 par. 3 exception; the refund procedure and its timing for exporters; the payment form for Form 300 balances; the IVA treatment of insurance premiums other than the health policies of art. 468-3 (no exclusion found in art. 476 as read on 14 Nov 2026).
