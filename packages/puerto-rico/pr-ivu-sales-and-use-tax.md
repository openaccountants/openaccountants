---
name: pr-ivu-sales-and-use-tax
description: >
  Compute Puerto Rico sales and use tax (IVU) for 2026. The state portion is 6
  percent under section 4020.01 plus the 4.5 percent surtax under section 4210.01,
  which is 10.5 percent, and the municipal portion is 1 percent under section
  6080.14, for 11.5 percent on a taxable sale of tangible personal property. Covers
  the food exemption, the 4 percent rate on services to other merchants and
  designated professional services, the USD 200,000 prior-year volume test, merchant
  registration, and the monthly return (Modelo SC 2915) on SURI, including the July
  2026 municipal integration for the 73 participating municipalities. Trigger on
  "IVU", "Puerto Rico sales tax", "impuesto sobre ventas y uso", "SURI", "10.5
  percent", "11.5 percent", "Modelo SC 2915", "municipal IVU".
jurisdiction: PR
category: international
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
version: "1.0"
---

# Puerto Rico sales and use tax (IVU), 2026

> **Source-cited draft.** Built from the Puerto Rico Internal Revenue Code of 2011, legislative-library revision of 28 May 2026, the Hacienda monthly IVU page, and Carta Circular de Rentas Internas Num. 26-13, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** On a taxable sale of tangible personal property the state IVU is **10.5 percent** (6 percent under section 4020.01 plus 4.5 percent under section 4210.01) and the municipal IVU is **1 percent** under section 6080.14. The combined charge is **11.5 percent**. Food and food ingredients are exempt from the state tax and are subject to the municipal 1 percent. Services to other merchants, and designated professional services, are not in the 11.5 percent base. They are taxed at **4 percent**, and the municipal 1 percent does not apply, unless a designated-professional exception in section 4010.01(ll)(12) removes the 4 percent. The monthly return is Modelo SC 2915, filed only on SURI by the **20th** of the following month.

## Scope and who this is for

In scope: the sales and use tax a merchant collects, reports and pays in Puerto Rico in 2026. That is the state sales tax, the state use tax, the 4.5 percent surtax, and the municipal 1 percent, including how the July 2026 SURI integration changes the municipal filing for participating municipalities.

A merchant is a person who wants to carry on business in Puerto Rico as a merchant. Registration is required before operations begin, for each business location. [Section 4060.01](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

Out of scope:

| Topic | Where it goes |
| --- | --- |
| Individual income tax | `pr-individual-income-tax` |
| Corporate income tax | `pr-company-income-tax` |
| The reseller-credit percentage in section 4050.04 | not yet confirmed; do not invent it |
| Municipal license tax (patente municipal) | not this tax |
| Alcoholic-beverage excise under Subtitle E | not this tax |

## Ask the client first

1. **What was sold:** tangible personal property, food or food ingredients, prepared food, a service to another merchant, or a designated professional service.
2. **Where the sale is sourced:** the delivery rules in section 4020.03, and the municipality of the location. Bayamon, Carolina, Guaynabo, Mayaguez and San Juan are not in the July 2026 SURI municipal integration.
3. **The merchant's status:** registered or not, withholding agent or not, and whether a reseller certificate applies.
4. **For a designated professional:** prior-year business volume, and whether the service is court representation, legal consulting or notarial work excluded by section 4010.01(ll)(12)(B).
5. **For a restaurant:** whether it holds the Secretary's certification for the prepared-food surtax exemption.
6. **The period:** a month before July 2026, or July 2026 or later. The municipal payment path changes on the July 2026 return.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Who it applies to | Source |
| --- | --- | --- | --- |
| State sales tax | 6 percent of the sales price | Taxable items, from 1 February 2014. Taxable items include tangible personal property, taxable services and admission rights | [Section 4020.01(b)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| State use tax | 6 percent | Use, storage or consumption of a taxable item in Puerto Rico that was not already subject to the sales tax, from 1 February 2014 | [Section 4020.02(d)(2)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| State surtax on sales | 4.5 percent of the sales price | Taxable-item sales after 30 June 2015, in addition to the 6 percent. Chapter 3 exemptions of Subtitle D apply | [Section 4210.01(a) and (b)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| State surtax on use | 4.5 percent | Use after 30 June 2015 that was not already taxed under sections 4020.01 and 4210.01 | [Section 4210.02(b)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| State total on taxable tangible property | 10.5 percent | 6 percent plus 4.5 percent. This is the state IVU | [Sections 4020.01(b) and 4210.01(b)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Municipal sales and use tax | 1 percent | Every municipality, from 1 February 2014, on the Subtitle D base and exemptions, with the exceptions in section 6080.14. Collected by the municipalities or their fiduciary | [Section 6080.14(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Combined rate on taxable tangible property | 11.5 percent | State 10.5 percent plus municipal 1 percent | [Sections 4020.01(b), 4210.01(b) and 6080.14(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Food and food ingredients, state | 0 percent | Exempt from the sales tax. The surtax follows the Subtitle D Chapter 3 exemptions. Prepared food, sweets, carbonated drinks, alcoholic drinks, tobacco and dietary supplements are not in this exemption | [Sections 4030.11(a) and 4010.01(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Food and food ingredients, municipal | 1 percent | Municipalities impose this from 1 July 2014 | [Section 6080.14(a)(1)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Prepared food at a certified restaurant, surtax | 0 percent of the 4.5 percent surtax | Transactions after 1 October 2019 of prepared food, carbonated beverages, bakery products and sweets, by a restaurant the Secretary has certified. The 6 percent sales tax is not removed by this paragraph | [Section 4210.01(a)(1)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Services to other merchants, and designated professional services | 4 percent | Rendered after 30 September 2015. These services are excluded from "taxable services", so the 6 percent and the 4.5 percent do not apply. The municipal 1 percent does not apply | [Sections 4010.01(nn)(3), 4210.01(c) and 6080.14(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Designated professional services below the volume line | 4 percent does not apply | From 1 March 2019, when prior-year business volume does not exceed USD 200,000. Volume is the aggregate of the controlled group, and for an individual it includes every business. Court representation, legal consulting and notarial fees of an admitted lawyer are also outside the 4 percent | [Section 4010.01(ll)(12)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Monthly return due date | The 20th day of the following month | Modelo SC 2915. Electronic returns must be received by that day. A Saturday, Sunday or federal or state holiday moves a mailed return to the next business day | [Section 4041.02(c) and (d)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf) |
| Participating municipalities in the SURI municipal integration | 73 | July 2026 period onward. The five that are not participating are Bayamon, Carolina, Guaynabo, Mayaguez and San Juan | [CC RI 26-13](https://hacienda.pr.gov/publicaciones/carta-circular-de-rentas-internas-num-26-13-cc-ri-26-13) |

Taxable services, for events after 30 September 2015, still include the services listed in section 4010.01(nn)(1): storage of tangible property (other than motor vehicles and food), certain leases, computer programming, installation, and repair. Those remain in the 11.5 percent computation unless another exemption applies. Services to other merchants and designated professional services are pulled out of that definition and fall under the 4 percent rule instead. [Section 4010.01(nn)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

### How to compute one sale

1. Decide whether the item is tangible personal property, food or a food ingredient, a taxable service, a service to another merchant, or a designated professional service.
2. For taxable tangible property and for a taxable service that was not removed from the definition, charge 6 percent plus 4.5 percent plus 1 percent.
3. For food and food ingredients, charge the municipal 1 percent only.
4. For a service to another merchant, charge 4 percent and do not add the municipal 1 percent.
5. For a designated professional service, charge 4 percent only when the section 4010.01(ll)(12) exceptions do not apply. If prior-year volume does not exceed USD 200,000, or the legal-services exclusion applies, do not charge the 4 percent and do not charge the municipal 1 percent.
6. For prepared food, carbonated drinks, bakery products or sweets sold by a certified restaurant after 1 October 2019, drop the 4.5 percent surtax. Keep the 6 percent. Keep the municipal 1 percent, because that exemption is not a Subtitle D exemption.

The sales price includes delivery, installation billed to complete the sale, and tips the merchant adds to the price. It does not include a discount the buyer actually takes, separately stated financing charges, or a tax imposed by law on the consumer that is stated separately. [Section 4010.01, Precio de venta](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

Use tax follows the same rates when the item was not already taxed on the sale. An item imported from outside Puerto Rico is reported on the import declaration, which includes the municipal use tax the Secretary collects, so a second municipal import return is not filed. [Sections 4020.02 and 4041.02(a)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

## Boundary and exception table

| Situation | What changes |
| --- | --- |
| Food or a food ingredient | State tax is zero. Municipal tax is 1 percent |
| Prepared food is not a food ingredient | It stays taxable unless a specific exemption applies |
| Certified restaurant, prepared food, after 1 October 2019 | Drop the 4.5 percent only |
| Service to another merchant | 4 percent, no municipal 1 percent |
| Designated professional, prior-year volume not over USD 200,000 | The 4 percent does not apply |
| Lawyer's court representation, legal consulting or notarial fees | The 4 percent does not apply, even above the volume line |
| Sale sourced to Bayamon, Carolina, Guaynabo, Mayaguez or San Juan, July 2026 or later | State IVU is still on the SURI return. Municipal IVU for that location is not calculated in the consolidated SURI municipal balance. File it with that municipality |
| Merchant's certificate says the merchant is not an IVU collector | No monthly return is required to report exempt sales, unless the merchant sells a taxable item |
| Reseller buying for resale with a reseller certificate | May buy tangible property for resale free of the municipal 1 percent. The municipal credit rules are not the state credit rules |

## Worked cases

**Case 1. Taxable goods.** A registered merchant sells taxable tangible personal property, not food, for USD 1,000. The state sales tax is USD 60. The surtax is USD 45. The state total is USD 105. The municipal tax is USD 10. The customer is charged USD 115.

```oa-check
name: Taxable goods, sales price 1000 (2026)
inputs:
  price: 1000
steps:
  - state_sales: price * 0.06
  - surtax: price * 0.045
  - state_total: state_sales + surtax
  - municipal: price * 0.01
  - charged: state_total + municipal
expected:
  state_sales: 60.00
  surtax: 45.00
  state_total: 105.00
  municipal: 10.00
  charged: 115.00
```

**Case 2, a decision: designated professional service or a sale of goods.** A CPA whose prior-year business volume was USD 250,000 bills USD 2,000 for accounting services. Accounting is a designated professional service. Volume exceeds USD 200,000, and the bill is not court representation or a notarial fee, so the 4 percent applies: USD 80. The municipal 1 percent does not apply. If the same USD 2,000 were a sale of taxable goods, the charge would be USD 230. The classification changes the tax by USD 150.

If that CPA's prior-year volume had been USD 180,000, it would not exceed USD 200,000, and section 4010.01(ll)(12)(A) would remove the 4 percent. The tax on the fee would be zero. Do not use the goods rate on the fee in either volume case.

```oa-check
name: Designated professional fee against a sale of goods (2026)
inputs:
  amount: 2000
steps:
  - service_tax: amount * 0.04
  - goods_state: amount * 0.06 + amount * 0.045
  - goods_municipal: amount * 0.01
  - goods_total: goods_state + goods_municipal
  - difference: goods_total - service_tax
expected:
  service_tax: 80.00
  goods_state: 210.00
  goods_municipal: 20.00
  goods_total: 230.00
  difference: 150.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-IVU-CLASS | The file does not show whether the charge is goods, food, a taxable service, a service to a merchant, or a designated profession | Do not pick 11.5, 1, 4 or 0 percent |
| R-IVU-VOLUME | Designated professional service and prior-year volume is missing | Do not charge 4 percent |
| R-IVU-RESELLER | A reseller credit is the question | Stop. The percentage in section 4050.04 is not confirmed in this skill |
| R-IVU-MUNI | The location is one of the five non-participating municipalities and the question is that municipality's own form | The state return is still Modelo SC 2915 on SURI. The municipal form is that municipality's, and this skill does not reproduce it |
| R-IVU-INCOME | The question is income tax on the profit | Use `pr-individual-income-tax` or `pr-company-income-tax` |

## Filing and payment

Register before the business starts. File a Solicitud de Certificado de Registro de Comerciantes with the Secretary for each location, naming the persons with an interest, their residences, the main office and every place sales are made. The certificate states whether the merchant is a withholding agent. It must be displayed where the public can see it. A change, a theft of the certificate, or a full or partial close of operations is reported within 30 days. [Sections 4060.01 and 4060.02](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

Each month, file Modelo SC 2915, Planilla Mensual de Impuesto sobre Ventas y Uso. It is due no later than the 20th day of the following month. Hacienda's page says the return and the payment can be filed only electronically through SURI. The informative form for July 2026 and after is linked from that page. SURI is at the address the page gives: [https://suri.hacienda.pr.gov/_/](https://suri.hacienda.pr.gov/_/). [Hacienda, Planilla Mensual de IVU](https://hacienda.pr.gov/ivu/planilla-mensual-de-ivu). The return reports taxable sales and exempt sales, use tax the merchant paid on purchases in Puerto Rico, and the reseller credit when section 4050.04 allows it. A merchant whose certificate says the merchant is not an IVU collector does not file to report exempt sales, but must file if any taxable item is sold. [Section 4041.02(c)](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf).

From the July 2026 period, whose due date is 20 August 2026, municipal IVU of the 73 participating municipalities is filed and paid only as part of this SURI return. The return and the payments are available from 1 August 2026. On 1 July 2026 SURI splits the account into Ventas y Uso - Estatal and Ventas y Uso - Municipal. File and amend the return, and pay the state IVU, from Ventas y Uso - Estatal. Pay the municipal balance, line 14(e), from Ventas y Uso - Municipal, as one payment for every participating municipality on the return. Filing the return is not the payment. Pay electronically on SURI, no later than the statutory due date. A partial municipal payment is spread across the participating municipalities. It does not clear one municipality. The five non-participating municipalities are Bayamon, Carolina, Guaynabo, Mayaguez and San Juan. Their locations are still reported on the SURI return for the state tax. Their municipal IVU is filed with each of those municipalities on that municipality's form. Periods before July 2026 stay on the earlier municipal process, with COFIM or the municipality. [CC RI 26-13](https://hacienda.pr.gov/publicaciones/carta-circular-de-rentas-internas-num-26-13-cc-ri-26-13).

Interest on unpaid tax is 10 percent a year from the due date. A delay of 30 days or less has no surcharge. More than 30 days and not more than 60 days adds 5 percent of the unpaid amount. More than 60 days adds 10 percent. [Section 6030.02](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf). Failure to file adds 5 percent if the failure is not more than 30 days, plus 10 percent for each further 30 days or fraction, and not more than 25 percent. [Section 6030.11](https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf). CC RI 26-13 states that an unpaid municipal balance on the SURI municipal account accrues the interest, surcharges and penalties of the Code, and that the debt appears on the debt certification, Modelo SC 6096.

## Completion checklist

- The item is classified before a rate is applied.
- Food is at municipal 1 percent only. Prepared food is not treated as that exemption.
- A designated professional fee is tested against prior-year volume and against the legal-services exclusion.
- The municipality is checked against the five non-participating names before the municipal payment is put on SURI.
- For July 2026 and later, the return is filed from Ventas y Uso - Estatal and the municipal payment is a separate payment from Ventas y Uso - Municipal.
- The 20th is applied to the following month, with the weekend and holiday rule.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Internal Revenue Code of 2011, revision of 28 May 2026. Read for sections 4020.01(b), 4020.02(d), 4210.01(a) through (c) and 4210.02(b): 6 percent, 4.5 percent and the 4 percent service rate. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Same code, same revision. Read for section 4010.01(a), (ll) and (nn): food, prepared food, designated professions, the USD 200,000 volume line, and the post-30 September 2015 exclusions. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Same code, same revision. Read for sections 4030.11, 4030.12, 4041.02, 4060.01 and 4060.02: the food exemption, the 20th-day return, and merchant registration. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Same code, same revision. Read for section 6080.14(a): the municipal 1 percent, the food rule, and the exclusion of services to merchants and designated professional services. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Same code, same revision. Read for sections 6030.02 and 6030.11: 10 percent interest, the 5 and 10 percent surcharges, and the filing addition capped at 25 percent. | https://bvirtualogp.pr.gov/ogp/Bvirtual/leyesreferencia/PDF/C%C3%B3digos/1-2011/1-2011.pdf | 2026-11-13 |
| Hacienda, Planilla Mensual de IVU. Read for Modelo SC 2915, the 20th of each month, electronic filing only on SURI, and the link https://suri.hacienda.pr.gov/_/. | https://hacienda.pr.gov/ivu/planilla-mensual-de-ivu | 2026-11-13 |
| Carta Circular de Rentas Internas Num. 26-13. Read for the July 2026 integration, 73 participating municipalities, the five non-participants, line 14(e), and the separate state and municipal payments. | https://hacienda.pr.gov/publicaciones/carta-circular-de-rentas-internas-num-26-13-cc-ri-26-13 | 2026-11-13 |

Not yet confirmed: the reseller-credit percentage and the other limits in section 4050.04. The municipal forms and due dates of Bayamon, Carolina, Guaynabo, Mayaguez and San Juan. Whether every service listed in section 4010.01(nn)(1) is taxed at 11.5 percent after the later exemptions in that definition are applied one by one. The combined rate on prepared food at a certified restaurant is stated as 6 percent plus the municipal 1 percent. A Hacienda worked example of that 7 percent was not on the pages read.
