---
name: uruguay-iva
description: "Uruguay value added tax (IVA, Impuesto al Valor Agregado) for 2026 under Título 10 of the Texto Ordenado 2023 and Decreto 220/998. Covers who is a taxpayer, the 22% basic rate (tasa básica) and the 10% minimum rate (tasa mínima) and what it covers, the main exemptions (property leases and sales, financial interest, newspapers and books), exports of goods and the listed exports of services, imports and the 50% uplift for third-party imports, input credit rules (necessary costs, vehicles, pro-rata, carried-forward credit, independent professionals), the 2-point reduction for debit-card sales to final consumers, the IVA mínimo for small businesses (literal E, UYU 5,910 a month in 2026, capped at 3.3% of sales), annual versus monthly liquidation (CEDE), filing on form 1050, and DGI penalties. Trigger on: IVA Uruguay 2026, tasa básica, tasa mínima, IVA mínimo, literal E, exportación de servicios, crédito fiscal IVA, Uruguay VAT."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uruguay-iva"
  jurisdiction: "UY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Uruguay: IVA (value added tax) for 2026 v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill computes a Uruguayan IVA liability for a period in 2026 and says how it is declared and paid. Related skills:

- [uy-corporate-income-tax](uy-corporate-income-tax.md): IRAE, whose taxpayer categories decide who pays IVA, and the UI 305,000 small-business limit (literal E).
- [uruguay-income-tax](uruguay-income-tax.md): IRPF; independent professionals who pay IRPF also pay IVA on their fees.

**Which text of the law.** Título 10 (IVA) of the Texto Ordenado 2023 approved by Decreto 101/024, as consolidated by IMPO with Ley 20.446 of 16 December 2025. The regulation is Decreto 220/998, whose references still use the 1996 numbering. The 2026 IVA mínimo amount is set by Decreto 310/025.

**Quick reference, 2026**

| Item | Figure |
|---|---|
| Basic rate (tasa básica) | 22% (T10 art. 34 A) |
| Minimum rate (tasa mínima) | 10% (T10 art. 34 B), on the goods and services in art. 36 |
| Exports of goods | Not taxed, with input credit refunded (arts. 5, 14) |
| Liquidation period | Annual, except CEDE taxpayers, who liquidate monthly (Decreto 220/998 art. 120) |
| Small businesses (literal E) | Fixed monthly IVA of UYU 5,910 in 2026, at most 3.3% of the month's sales if all are e-invoiced; no IVA charged |

## Who this applies to

- **Taxpayers** (T10 art. 6): anyone carrying out taxed acts in activities that are business income under IRAE (T4 art. 12), except farmers who chose IMEBA; IRPF taxpayers who opted into IRAE; independent workers (servicios personales fuera de la relación de dependencia) paying IRPF; non-residents paying IRNR (with exceptions); State commercial entities; importers not otherwise covered; trusts, closed credit funds and savings-and-credit cooperatives; and the owners of construction works under the administration mode.
- **What is taxed** (art. 1): the internal supply of goods, services inside Uruguay, imports and the value added by construction on real estate. A supply of goods includes the private use of business goods by owners or partners (art. 2 A). Services include leases of things, financing and intermediation (art. 2 B).
- **Territory** (art. 5): supplies made in Uruguay are taxed whatever the parties' residence. Exports of goods are not taxed; exports of services are not taxed only when the Executive lists them. Services through the internet or platforms that are consumed or used in Uruguay are treated as performed wholly in Uruguay, as is digital intermediation where both parties are in Uruguay.
- **Tax point** (art. 3): when the goods are delivered or the service is performed; presumed to be the invoice date. Continuous services (such as insurance) arise monthly.
- **Not covered here.** Monotributo and Monotributo Social MIDES (exempt from IVA under art. 40 C), free-zone users, IMEBA farmers, gasoil and fuel regimes, the IVA en suspenso regimes for farm produce and scrap, and investment-promotion refunds.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Basic rate | 22% | 2026 | https://www.impo.com.uy/bases/todgi-2023/10-2024 (T10 art. 34 A) |
| Minimum rate | 10% | 2026 | same, art. 34 B |
| Minimum rate: white bread and galleta de campaña, fish, beef and offal (fresh, chilled, frozen), edible oils, rice, flour, pasta, household salt, sugar, yerba, coffee, tea, common soap, edible fats, milk transport | 10% | 2026 | same, art. 36 A |
| Minimum rate: medicines and pharmaceutical products, their active ingredients, implants | 10% | 2026 | same, art. 36 B |
| Minimum rate: hotel accommodation services | 10% | 2026 | same, art. 36 C |
| Minimum rate: independent human-health services and ambulance transport | 10% | 2026 | same, art. 36 D |
| Minimum rate: local tour packages, street-lighting electricity, gasoil, land passenger transport | 10% | 2026 | same, art. 36 E to H |
| Minimum rate: first sale of real estate by a business (including after significant refurbishment) | 10% | 2026 | same, art. 36 I |
| Minimum rate: fruit, flowers and vegetables in natural state sold to final consumers (not by small farmers without full accounts); poultry, pork and rabbit meat and offal | 10% | 2026 | same, art. 36 K, L |
| Exempt: foreign currency, precious metals, securities, assignments of receivables | Exempt | 2026 | same, art. 38 1) A, C |
| Exempt: sales of real estate other than the first sale by a business; bare land always | Exempt | 2026 | same, art. 38 1) B |
| Exempt: petroleum fuels except fuel oil and gasoil; pasteurised and powdered milk (not flavoured or UHT); farm inputs on the official list | Exempt | 2026 | same, art. 38 1) E, F, G |
| Exempt: newspapers, magazines, books and educational material; music and film on physical or digital media; solar panels | Exempt | 2026 | same, art. 38 1) H, P, R |
| Exempt: interest on securities and bank deposits; bank operations of banks and savings cooperatives (but interest on loans to individuals who do not pay IRAE or IMEBA is taxed, and credit-card and purchase-order interest is always taxed) | Exempt, with the stated exceptions | 2026 | same, art. 38 2) A, E |
| Exempt: leases of real estate (arrendamientos de inmuebles) | Exempt | 2026 | same, art. 38 2) C |
| Exempt: cultural activities of resident artists (independent fees); AFAP and CJPPU commissions; construction services on property not used for IVA or IRAE activity where AUC is paid | Exempt | 2026 | same, art. 38 2) H, N, T, U |
| Imports by a third party in its own name for another, or by non-taxpayers | Base = customs value plus duty, increased by 50% | 2026 | same, art. 13 B |
| International postal parcels (from 1 January 2026) | IVA on the invoice or declared value, never less than USD 20 unless all goods are exempt | 2026 | same, art. 13 B (Ley 20.446 art. 660) |
| Sales to final consumers paid by debit card or e-money | Rate reduced by 2 percentage points | 2026 | same, art. 94 |
| IVA mínimo, literal E taxpayers (income up to UI 305,000 a year) | UYU 5,910 a month in 2026 | 2026 | https://www.impo.com.uy/bases/decretos/310-2025 (art. 1) |
| IVA mínimo cap when all operations are documented by electronic invoices (CFE) | Not more than 3.3% of the month's income | 2026 | https://www.impo.com.uy/bases/decretos/220-1998 (Decreto 220/998 art. 106) |
| IVA mínimo for businesses started from 2021 | 25% of the amount for the first 12 months, 50% for the next 12, then 100% | 2026 | same, art. 106; T10 art. 22 |
| Late filing of a return | UYU 910 per return | 2026 | https://www.impo.com.uy/bases/resoluciones-dgi/97-2026 |
| Late payment fine (mora) | 5% within 5 working days; 10% up to 90 days; 20% after; plus a monthly surcharge | 2026 | https://www.impo.com.uy/bases/codigo-tributario/14306-1974/94 |

## The base

- **Taxable amount** (T10 arts. 12, 13): the consideration, including other taxes on the operation; IVA is shown separately on the invoice unless the DGI allows it to be included in the price. On imports, customs value plus duty.
- **Computation** (art. 14): IVA invoiced on sales, less IVA on returns, discounts and bad debts (art. 3), less:
  1. IVA invoiced by suppliers on documented purchases, and IVA paid on imports, but only for goods and services that form part, directly or indirectly, of the cost of taxed operations;
  2. for mixed taxed and exempt activity, common inputs in the proportion of taxed operations (art. 14; the annual proportion of art. 92 even if liquidated monthly);
  3. for vehicles, only IVA on utility vehicles (trucks and pick-ups) and on other vehicles the regulation treats as necessary for the business, with price, make, type, model and use reported to the DGI;
  4. independent workers who do not pay IRAE cannot deduct IVA on vehicles, furniture or personal expenses;
  5. IVA charged by literal E (IVA mínimo) sellers is not deductible by the buyer.
- **Exports** (art. 14): IVA on inputs to exported goods (and listed exported services) can be refunded or set against other taxes and social contributions, as the Executive sets.
- **Excess credit** (art. 15): an excess of input IVA over output IVA is not refunded; it is carried to the next return. At year-end, an excess that comes only from rate differences (buying at 22%, selling at 10%) becomes cost of sales, except for the 10% sales of property, fruit and vegetables, health and transport.
- **Sale of fixed assets** (art. 14): taxed only if IVA was deducted when they were bought.
- **Exports of services** (Decreto 220/998 art. 34): only the listed services. Examples are international freight, services in customs areas and free zones, and advisory services to persons abroad on activities, assets or rights outside Uruguay (numeral 11 a). The numeral 11 group also covers custom software, software licences and software rights, but only if used exclusively abroad. Anything not on the list is taxed even if the client is abroad.
- **Card-payment reductions** (arts. 94, 102, 103): the seller invoices at the full rate and takes a credit equal to the reduction on the net amount. Excess reduction credit becomes cost of sales.

## Deadlines and filing

| Step | What and where | Source |
|---|---|---|
| Period | Annual liquidation; CEDE taxpayers (and others the DGI designates) liquidate monthly | [Decreto 220/998 art. 120](https://www.impo.com.uy/bases/decretos/220-1998) |
| Annual return | Form 1050 (IVA, IRAE, Impuesto al Patrimonio, ICOSA) for CEDE and NO CEDE taxpayers in the PADI application, filed even without activity, within the fourth month after the year-end; IVA mínimo sole traders and Monotributo do not file it | [DGI, form 1050](https://www.gub.uy/direccion-general-impositiva/sites/direccion-general-impositiva/files/documentos/publicaciones/Charla%20externa%20formulario%201050.pdf) |
| Monthly payments | Advances during the year on the basis the Executive sets (T10 art. 92), on the general deadline table | [T10 art. 92](https://www.impo.com.uy/bases/todgi-2023/10-2024) |
| Independent workers (IRPF) | Form 1302 (IVA servicios personales), due with the IRPF return: 29 June to 31 August 2026 for 2025 | [DGI, calendario 2026](https://www.gub.uy/direccion-general-impositiva/comunicacion/noticias/calendario-campana-2026-irpf) |
| IVA mínimo | Fixed monthly payment; the business issues invoices without IVA | Decreto 220/998 art. 106 |
| Payment | Boleto 2908 through Servicios en Línea, at Abitab, Red Pagos or online banking | [DGI, vencimientos](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/vencimientos-pagos-cuenta-saldos-declaraciones-juradas) |
| Invoices | Numbered invoices showing the taxpayer's registration, goods or services, date, amount and IVA (T10 art. 88); deduction needs a purchase invoice documented that way (art. 14 A) | T10 art. 88 |

## Penalties and interest

- **Late payment** (Código Tributario art. 94): fine of 5%, 10% or 20% of the tax paid late depending on the delay, plus a monthly surcharge calculated day by day at the rate the Executive sets.
- **Late filing:** UYU 910 per return in 2026 (Res. DGI 97/026).
- **Invoicing failures:** not documenting taxed operations as art. 88 requires is presumed fraud (defraudación), unless proven otherwise (art. 88).
- **Card-reduction abuse:** a border-shop reduction claimed without meeting the conditions is defraudación under Código Tributario art. 96, plus the credit and mora (art. 102 bis).

## Cross-border points

- **Imports** by taxpayers are taxed on customs value plus duty and the IVA is deductible; by non-taxpayers the IVA is final, with the 50% uplift (arts. 4, 13).
- **Services from abroad**: a service performed outside Uruguay is outside the territorial scope (art. 5), except digital services used in Uruguay, which are taxed as performed in Uruguay. Non-residents paying IRNR are IVA taxpayers (art. 6 D). No general reverse charge for the Uruguayan customer appears in Título 10.
- **Exports of services**: only those on the Decreto 220/998 art. 34 list are outside IVA, and many require use exclusively abroad.
- **Hotels and tourists**: accommodation is at 10%; the Executive may treat hotel services to non-residents as exports (art. 5).

## Two worked examples that recompute

### Example 1: CEDE company with exempt rent and a passenger car

Andes SA is in the CEDE register and liquidates monthly. In March 2026 it sells goods at 22% for UYU 1,000,000 net and medicines at 10% for UYU 200,000 net. It also lets a warehouse for UYU 300,000 (exempt). Its purchases: IVA of UYU 120,000 on stock and services used only for taxed sales, UYU 30,000 of IVA on common overheads, and UYU 50,000 of IVA on a sedan for a director that the regulation does not treat as necessary.

Output IVA: 22% of 1,000,000 = 220,000 plus 10% of 200,000 = 20,000, total UYU 240,000. Input: the UYU 120,000 is deductible in full. Common overheads go by the taxed share of operations: 1,200,000 / 1,500,000 = 80%, so UYU 24,000. The sedan's IVA is not deductible. IVA payable: 240,000 - 144,000 = UYU 96,000.

```oa-check
name: UY IVA 2026, CEDE month with exempt rent, pro-rata and blocked car
inputs:
  sales_22: 1000000
  sales_10: 200000
  exempt_rent: 300000
  direct_input_iva: 120000
  common_input_iva: 30000
  car_iva: 50000
steps:
  - output_iva: sales_22 * 0.22 + sales_10 * 0.10
  - taxed_share: (sales_22 + sales_10) / (sales_22 + sales_10 + exempt_rent)
  - common_deductible: common_input_iva * taxed_share
  - input_iva: direct_input_iva + common_deductible
  - payable: output_iva - input_iva
expected:
  output_iva: 240000
  taxed_share: 0.80
  common_deductible: 24000
  input_iva: 144000
  payable: 96000
```

### Example 2: should a small shop stay in IVA mínimo or move to the general regime?

A sole trader runs a shop whose yearly income stays within the UI 305,000 limit (checked at the UI quotation at the start of the year). In a typical 2026 month she sells UYU 150,000, all documented by e-tickets, and buys stock for UYU 100,000 net plus UYU 22,000 of IVA. She has been in business for more than two years.

IVA mínimo: the fixed payment is UYU 5,910, but with all sales on CFE it cannot exceed 3.3% of the month's income, 0.033 x 150,000 = UYU 4,950. She pays UYU 4,950 and charges no IVA.

General regime: if her UYU 150,000 of sales were net prices, output IVA at 22% would be UYU 33,000 and her input IVA UYU 22,000, so she would pay UYU 11,000 a month, and she would have to charge IVA on top of her prices.

The decision: she stays in IVA mínimo, saving UYU 6,050 a month. The general regime pays only if her business customers need deductible IVA (they cannot deduct anything from a literal E seller, T10 art. 14) or her margin is thin enough that output minus input IVA falls below the minimum payment. Leaving by option binds her to the general regime for at least three years (Decreto 220/998 art. 106).

```oa-check
name: UY IVA 2026, IVA mínimo vs general regime for a small shop
inputs:
  monthly_sales: 150000
  fixed_payment: 5910
  input_iva: 22000
steps:
  - cap: monthly_sales * 0.033
  - iva_minimo: min(fixed_payment, cap)
  - general_output: monthly_sales * 0.22
  - general_payable: general_output - input_iva
  - monthly_saving: general_payable - iva_minimo
expected:
  cap: 4950
  iva_minimo: 4950
  general_output: 33000
  general_payable: 11000
  monthly_saving: 6050
```

## Ask the client first

1. Taxpayer type: company, sole trader, independent professional in IRPF, literal E (IVA mínimo), Monotributo, CEDE or NO CEDE group, and the fiscal year-end.
2. What is sold, and for each line whether it is at 22%, 10%, exempt or an export (and, for services to clients abroad, which numeral of Decreto 220/998 art. 34 it fits).
3. Exempt income (property leases, financial interest, property sales) that triggers pro-rata of common inputs.
4. Purchases with valid invoices, vehicles bought and whether they are utility or necessary vehicles reported to the DGI, and imports.
5. Credit carried forward from the previous return and any export credit to recover.
6. For small businesses: yearly income in UI, date business started (25% / 50% scale), and whether all sales are on CFE.

## Sources

| Source | URL | Read on |
|---|---|---|
| Texto Ordenado 2023, Título 10 IVA, IMPO consolidated text with Ley 20.446: arts. 1 to 41, 88 to 107 read | https://www.impo.com.uy/bases/todgi-2023/10-2024 | 2026-11-11 |
| Decreto 220/998 (IVA regulation), arts. 34, 106, 120, 142 read | https://www.impo.com.uy/bases/decretos/220-1998 | 2026-11-11 |
| Decreto 310/025, art. 1: 2026 IVA mínimo monthly payment | https://www.impo.com.uy/bases/decretos/310-2025 | 2026-11-11 |
| Decreto 150/007, art. 122: literal E limit of UI 305,000 | https://www.impo.com.uy/bases/decretos/150-2007 | 2026-11-11 |
| DGI, form 1050 presentation, read for who files and the deadline | https://www.gub.uy/direccion-general-impositiva/sites/direccion-general-impositiva/files/documentos/publicaciones/Charla%20externa%20formulario%201050.pdf | 2026-11-11 |
| DGI, vencimientos guide and PDF, read for the fourth-month rule and payment by boleto 2908 | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/vencimientos-pagos-cuenta-saldos-declaraciones-juradas | 2026-11-11 |
| DGI, 2026 IRPF campaign calendar, read for the form 1302 window | https://www.gub.uy/direccion-general-impositiva/comunicacion/noticias/calendario-campana-2026-irpf | 2026-11-11 |
| Código Tributario, art. 94 (mora) | https://www.impo.com.uy/bases/codigo-tributario/14306-1974/94 | 2026-11-11 |
| Resolución DGI 97/026, numeral 1 read for the late-return fine | https://www.impo.com.uy/bases/resoluciones-dgi/97-2026 | 2026-11-11 |

Not yet confirmed: the CEDE monthly return form number and its box layout (the old file's forms 2176 / 2178 and lines 1 to 18 were not found in the sources read); the 2026 monthly due dates by RUT ending; the IVA withholding regimes for State bodies and designated large taxpayers (the old file's 100% on services and 60% on goods); the CFE document codes (e-Factura 111, e-Ticket 101 and others); whether the Executive has used its powers to cut the 2-point card reduction further for sales under UI 4,000 (art. 95) or to treat hotel services to non-residents as exports; the regulatory list of "necessary" vehicles; any withholding or reverse-charge mechanism in decrees for services bought from abroad; the 2026 monthly recargo rate; the UI quotation for 2026.

> Contributed by OpenAccountants.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uruguay-iva` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uruguay-iva. If neither is available, confirm every figure against the official source pages cited above before relying on it.
