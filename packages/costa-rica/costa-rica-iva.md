---
name: costa-rica-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Costa Rica IVA (Impuesto al Valor Agregado) return or advise on Costa Rican VAT registration, filing, and Hacienda compliance. Trigger on phrases like "prepare IVA return Costa Rica", "Costa Rica VAT", "IVA Costa Rica", "Hacienda", "CÉDULA jurídica", or any Costa Rica IVA request. ALWAYS read this skill before touching any Costa Rica IVA work.
version: 2.0
jurisdiction: CR
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Costa Rica IVA (Impuesto sobre el Valor Agregado)

## Scope

This Guide covers Costa Rica's value added tax (IVA) for the 2026 calendar year: who must register, which rate applies, how input credit (crédito fiscal) works, the monthly return, electronic invoicing, the special regimes, and the administrative penalties. The legal base is Ley N.º 6826, Ley del Impuesto sobre el Valor Agregado, as rewritten in full by Title I of Ley N.º 9635 (Fortalecimiento de las Finanzas Públicas), with its Reglamento (Decreto 41779-H). Title I took effect on 1 July 2019. The penalties come from the Código de Normas y Procedimientos Tributarios (Ley 4755).

Out of scope: customs valuation on imports, selective consumption tax, the single fuel tax (fuel sales are outside IVA; see below), income tax, and free zone (zona franca) incentive contracts.

**Source note.** The Procuraduría's SCIJ full-text pages for the current consolidated law are served through a script-driven viewer that could not be read for this Guide. The law quotes below come from the text of Ley 9635 as published (a SCIJ copy marked as a superseded version, because later laws have amended some articles). They are cross-checked against Hacienda guidance published since, including 2025-2026 TRIBU-CR material. Where a point rests only on older guidance, the Guide says so. Before relying on a rate for an unusual item, check the current article on SCIJ or ask the Dirección General de Tributación (DGT).

Law as published: [Ley 9635, Título I (SCIJ)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML).

## Ask the client first

- **Registration.** Is the business registered with the DGT, and under which regime: general, Régimen de Tributación Simplificada, Régimen Especial Agropecuario, or the used-goods regime?
- **What exactly is sold.** For each product or service line, is it at the general rate, at a reduced rate, exempt (and if so, with or without the right to full credit), or not subject (no sujeto)?
- **Customers.** Are there exports, sales to free zone companies, or sales to exempt bodies that hold an exoneration authorised in EXONET?
- **Purchases.** Does every purchase have an electronic receipt (comprobante electrónico) authorised by Hacienda, or a customs declaration for imports?
- **Mixed activity.** Does the business make both taxable sales and sales without a right to credit? If so, the proportionality rule (prorrata) applies.
- **Foreign services.** Does the business buy services or intangibles from suppliers not domiciled in Costa Rica, including digital services paid by card?
- **Rent.** For any property let or rented: is it housing, what is the monthly rent, and is the tenant a micro or small business registered with MEIC or MAG?
- **Past compliance.** Are any monthly returns missing or late, and has Hacienda contacted the business? This decides which penalty reduction is still available.

## The method, step by step

1. **Confirm the taxpayer.** Anyone who habitually organises production factors on their own account to produce, distribute, sell or provide goods or services is a taxpayer. So are importers, exporters, and those in the simplified regime. Ley 6826 art. 4: "Son contribuyentes de este impuesto las personas físicas, jurídicas, las entidades públicas o privadas que realicen actividades que impliquen la ordenación por cuenta propia de factores de producción".
2. **Register before starting.** Art. 5: "Al iniciar sus actividades gravadas, las personas o las entidades a las que se refiere el artículo anterior deben inscribirse en el registro de contribuyentes". The law sets no turnover threshold for registration. A business that does not register is registered by Hacienda on its own motion and can still be fined.
3. **Classify each sale.** Start from the general rate. Move a line to a reduced rate, exemption or non-subject treatment only when a specific provision (art. 8, 9 or 11, or a special law) and any required authorisation cover it.
4. **Issue an electronic receipt** for every sale, at the time of sale. Show each rate separately.
5. **Compute the output tax (débito fiscal)** by rate.
6. **Compute the input tax (crédito fiscal)** only for documented purchases used in taxable or credit-bearing operations. Apply the restrictions and the prorrata where they apply.
7. **File and pay** the monthly return in TRIBU-CR. It is due by the fifteenth calendar day of the following month. File it even when nothing is due or the result is a credit balance.
8. **Carry forward or apply** any credit balance, and keep the records.

## Rates and figures for 2026

| Item | Figure | Year / status | Source |
| --- | --- | --- | --- |
| General rate | 13% | In force since 1 July 2019; unchanged for 2026 | [Ley 6826 art. 10](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML); [Hacienda rent guidance](https://www.hacienda.go.cr/docs/ArrendamientoBienesMueblesInmuebles.pdf) |
| Private health services by authorised centres or professionals who belong to their professional college | 4% | In force for 2026 | [art. 11(1)(b)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML); [Hacienda health-services note](https://www.hacienda.go.cr/docs/ServiciosSaludHumanaPrivada.pdf) |
| Air tickets with origin or destination in Costa Rica | 4%; on international air transport, the tax is charged on 10% of the ticket value | Law as published | [art. 11(1)(a)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML); [DGT deck, July 2021](https://www.hacienda.go.cr/docs/PresentacionIVACRTEx.pdf) |
| Medicines, and the raw materials, inputs, machinery, equipment and reagents needed to produce them, as authorised by Hacienda | 2% | Law as published; DGT deck of July 2021 | [art. 11(2)(a)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML) |
| Private education services | 2% | Law as published. The 2021 DGT deck limits this to private education not regulated by MEP or CONESUP; private education regulated by MEP or CONESUP is exempt under art. 8(31) (check which applies) | [art. 11(2)(b)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML) |
| Personal insurance premiums | 2% | Law as published | [art. 11(2)(c)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML) |
| Purchases and sales by state higher-education institutions, their foundations, CONARE and SINAES, when needed for their purposes | 2% | Law as published | [art. 11(2)(d)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML) |
| Goods in the Canasta Básica Tributaria, plus the machinery, equipment, services and inputs needed to produce them | 1% | The list is set by executive decree. The Hacienda-hosted list is Decreto 43790-H-MEIC-S (La Gaceta, 11 November 2022), made under Ley 9914. Check that no newer decree applies | [art. 11(3)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML); [Decreto 43790-H-MEIC-S](https://www.hacienda.go.cr/docs/CanastaBasica2023Ley-decreto-43790.pdf) |
| Farm and livestock goods in the basket, including live animals, and the inputs across the production chain | 1% | Law as published. The 2021 DGT deck adds veterinary products and farm and non-sport fishing inputs, for producers registered with MAG and/or INCOPESCA | [art. 11(3)(a)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML) |
| Other reduced-rate columns on the monthly return | 0.5% and 3% | The 2025 draft IVA form resolution shows columns for these rates. This Guide has not sourced which items they cover: check before using them | [Draft Hacienda form resolution, 2025](https://www.hacienda.go.cr/docs/ProyResUsoformularios_IVAyREA.pdf) |
| Salario base (salary unit used for rent and fines) | CRC 462,200 | Applies 1 January to 31 December 2026 (Circular 246-2025) | [Hacienda salario base table](https://www.hacienda.go.cr/docs/SalariosBaseActualEHistorico.pdf) |
| Exempt housing rent ceiling (1.5 salarios base) | CRC 693,300 per month | 2026, derived: 1.5 × CRC 462,200 | [art. 8(9)](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML); [salario base table](https://www.hacienda.go.cr/docs/SalariosBaseActualEHistorico.pdf) |

**Services by engineers, architects, topographers and civil construction, and tourism services registered with ICT.** These had phased-in rates after 2019. They reached the general rate from 1 September 2023 (construction services on projects registered with CFIA) and from 1 July 2023 (ICT-registered tourism services). For 2026, apply 13% unless a later law says otherwise. Source: [DGT deck of July 2021](https://www.hacienda.go.cr/docs/PresentacionIVACRTEx.pdf), which states "A partir del 1/09/2023 13%" and "Del 1 de julio 2023 en adelante. 13%".

**Exports.** Exports of goods and services are exempt with the right to full credit. This includes services used outside Costa Rica, and sales to and between free zone beneficiaries (art. 8(1) and 8(2)). The monthly return reports them as exempt sales with the right to full credit. It is not a separate zero rate.

## Exemptions, non-subject operations and boundaries

| Situation | Treatment | Condition or trap |
| --- | --- | --- |
| Rent of property used exclusively as housing ("destinados exclusivamente a viviendas"), including garages, annexes and furniture let together | Exempt if the monthly rent is equal to or less than 1.5 salarios base (CRC 693,300 in 2026) | A mixed-use let (for example a home that also serves as an office or shop) is not used exclusively as housing, so it does not qualify under this heading: treat it at 13% unless another exemption applies, and refer if unsure. If the rent exceeds the ceiling, 13% applies to the **whole** rent, not only the excess: "el impuesto se aplicará al total de la renta" (art. 8(9)) ([Ley 6826 art. 8](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML)) |
| Rent paid by micro and small businesses registered with MEIC, or micro and small farm businesses registered with MAG | Exempt up to the same 1.5 salarios base ceiling | Needs the authorisation issued through EXONET (Hacienda rent guidance) |
| Rent of premises used for worship by religious organisations | Exempt | art. 8(9) |
| Interest and commissions on loans and credit; invoice discounting; financial and operating leases that work as financing; transfers through SUGEF-supervised entities; deposit-taking from the public; cash withdrawals by any means; paying bills and taxes through a financial entity; buying, selling or exchanging foreign currency and similar FX services; card commissions; bank guarantees; pension-fund commissions | Exempt | art. 8(3)-(7), law as published. This is a list, not a blanket "financial services" exemption. A bank fee for a service that none of these items covers is not exempt under this row: check it against the current art. 8 before charging 13% ([Ley 6826 art. 8](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML)) |
| Life insurance with life annuities; work-risk, farm and social-housing insurance | Exempt | art. 8(8) and the 2021 DGT deck. Other **personal** insurance is 2%, not exempt (law as published and 2021 DGT deck; confirm current art. 11) ([DGT deck](https://www.hacienda.go.cr/docs/PresentacionIVACRTEx.pdf)) |
| Residential electricity; residential water | Exempt if monthly consumption is 280 kWh or less (electricity) or 30 cubic metres or less (water) | Law as published, art. 8(11) and 8(12). If consumption exceeds either limit, the tax applies to the **whole** consumption, not only the excess. Bottled water is never exempt ("No gozará de esta exención el agua envasada"). Commercial supplies are at 13% ([Ley 6826 art. 8](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML)) |
| Land passenger transport and passenger cabotage | Exempt | Law as published, art. 8(24): only with a permit or concession from the State and a fare regulated by ARESEP ([Ley 6826 art. 8](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML)) |
| Sales to or purchases by CCSS and the municipalities | Not subject (no sujeto) under art. 9 | Not the same as exempt. Art. 30 of the Reglamento gives some of these sales a right to credit |
| Transfers of real estate and movable property subject to other taxes; sales of fuel | Not subject | Covered by other taxes (2021 DGT deck, art. 9) |
| Private education at pre-school, primary, secondary, university, para-university and technical levels; books in any format | Exempt | Law as published, art. 8(31) (education) and 8(25) (books). Per the 2021 DGT deck, the education exemption covers private education regulated by MEP or CONESUP, and private education outside that scope is at 2% (law as published and 2021 DGT deck; confirm current art. 11). The book exemption does not cover e-readers or other electronic devices for reading books ("no será aplicable a los medios electrónicos que permiten el acceso y la lectura de libros") ([Ley 6826 art. 8](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML); [DGT deck](https://www.hacienda.go.cr/docs/PresentacionIVACRTEx.pdf)) |
| Wheelchairs, orthopaedic equipment, prostheses, hearing and rehabilitation equipment | Exempt | Through EXONET (2021 DGT deck) |
| Private health service that also sells restaurant, lodging or internet services | Health part at 4%; the other services at 13% | The receipt must show the services separately (Hacienda health-services note) ([Hacienda note](https://www.hacienda.go.cr/docs/ServiciosSaludHumanaPrivada.pdf)) |

## Input credit (crédito fiscal)

- **Who can claim.** Only a registered taxpayer can claim, and only for purchases used in operations that are subject and not exempt, or in operations that carry a right to credit such as exports (arts. 17 and 21).
- **Documents.** The credit must be documented, and the document must be in the taxpayer's hands. That means the original receipt authorised by Hacienda, or the customs document for imports showing the tax paid (arts. 17 and 20; 2021 DGT deck). No authorised electronic receipt means no credit.
- **Excluded purchases.** No credit is allowed for an amount above what the law allows, or for tax charged before the chargeable event. Purchases listed in arts. 19 and 28 are also excluded. The 2021 DGT deck gives examples: jewellery and precious stones, food, shows, travel and lodging, and vehicles not classed as special vehicles. Check the current art. 19 wording before disallowing a whole category.
- **Reduced-rate sales.** A business selling at a reduced rate recovers input tax only up to that reduced rate on the purchases used for those sales. Art. 26: "el crédito fiscal será el que resulte de aplicar el tipo reducido a la base imponible". The rest is a cost for income tax purposes ("gasto para utilidades" on the return).
- **Mixed businesses (prorrata).** If purchases serve both operations with a right to credit and operations without one, credit follows the proportion rules in arts. 22 to 24. Hacienda publishes a manual and calculation tools for this. Capital goods whose value exceeds fifteen salarios base need an adjustment on the return (2025 draft form resolution).
- **Pre-operating stage.** The 2021 DGT deck allows credit for tax paid in the pre-operating stage, limited to four years. Check this against the current Reglamento before using it.
- **Credit balances.** A credit balance carries to the following months (art. 28). If the taxpayer expects that the next three months will not produce enough output tax to absorb it, the balance can be used through the compensation or refund procedures in arts. 45 and 47 of the Código. A credit can be claimed in the return for the period in which it arises or in a later one, within the limitation period.

## Foreign suppliers and digital services

- **Business buyer of foreign services (reverse charge).** When the supplier of a service or intangible is not domiciled in Costa Rica, the recipient is the taxpayer, provided the recipient is itself an IVA taxpayer (art. 4, second paragraph). The recipient accounts for the tax on its own return.
- **Consumers buying digital services.** Hacienda can require suppliers and intermediaries of internet or platform services consumed in Costa Rica to collect the tax. Card issuers must act as collection agents (agentes de percepción) when cardholders buy such services (art. 30). The general 13% rate applies (2021 DGT deck). ([Ley 6826 art. 30](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML))
- **TRIBU-CR returns for these regimes** (Hacienda 2025 code table): "IVA06" for collection on international service purchases by card (daily); "IVA07" for collection by intermediaries of cross-border digital services registered with the DGT (monthly); "IVA09" for cross-border digital service suppliers registered with the DGT (monthly).

## Special regimes

- **Régimen de Tributación Simplificada (arts. 35 to 41).** Available only to activities that Hacienda has studied and authorised, within limits on capital, purchases and other elements set by decree. Entry and exit are voluntary, and the regime affects both IVA and income tax. The tax is computed by applying the published factor for the activity to purchases. A return is filed each quarter, within the first fifteen calendar days of October, January, April and July (art. 38). In TRIBU-CR this is return "IVA04", quarterly, which replaced the old D-105 form. Participants do not have to issue invoices except where Hacienda requires it or the buyer asks, but they must ask their suppliers for invoices (art. 40). They do not claim ordinary input credit (art. 41). Refer to a professional before moving a client into or out of this regime.
- **Régimen Especial Agropecuario (REA).** Voluntary, and it affects IVA only. Growers of sugar cane and coffee and honey producers file once a year; other farm activities file every four months (2021 DGT deck). TRIBU-CR returns: "IVA02" (four-monthly) and "IVA03" (annual).
- **Used goods (arts. 31 and 32).** A voluntary regime for resellers of used goods, with a minimum stay of two years (2021 DGT deck). Modalities (b) and (c) file TRIBU-CR return "IVA08", monthly.

## Worked cases

All amounts are hypothetical and are in colones before tax unless stated otherwise.

**Case 1: consulting fee at the general rate.** A San José consultancy invoices a local company CRC 1,000,000 plus tax in March 2026. Output tax: 13% × CRC 1,000,000 = CRC 130,000, reported on the March return. That return is due by the fifteenth of April 2026. ([rate: Ley 6826 art. 10](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML))

**Case 2: housing rent above the ceiling.** A landlord lets a furnished flat for CRC 800,000 a month in 2026. The ceiling is CRC 693,300 (1.5 × CRC 462,200). The rent exceeds it, so tax applies to the whole rent: 13% × CRC 800,000 = CRC 104,000 a month. It is not charged only on the excess. At a rent of CRC 693,300 or less, the rent would be exempt. ([Hacienda rent guidance](https://www.hacienda.go.cr/docs/ArrendamientoBienesMueblesInmuebles.pdf))

**Case 3: private clinic.** An authorised private clinic charges CRC 500,000 for a consultation and tests. Tax: 4% × CRC 500,000 = CRC 20,000. If the clinic also bills a companion's lodging, that lodging is at 13% and goes on a separate line. When the patient pays by credit or debit card, the provider refunds the tax to the patient on the spot and claims it as a payment on account (pago a cuenta) in its monthly return (Hacienda health-services note). ([Hacienda health-services note](https://www.hacienda.go.cr/docs/ServiciosSaludHumanaPrivada.pdf))

**Case 4: international air ticket.** A Costa Rican travel seller sells a San José–Madrid ticket for CRC 600,000. The tax base is 10% of the ticket value, CRC 60,000, and the rate is 4%. Tax: CRC 60,000 × 4% = CRC 2,400. The 4% air rate and the 10% base rest on the law as published and the 2021 DGT deck: confirm the current art. 11 before relying on them. ([Ley 6826 art. 11](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML))

**Case 5: late payment and late filing.** A taxpayer files and pays the March 2026 return, with tax due of CRC 1,000,000, three months late. Late-payment penalty (art. 80): 1% per month or part of a month, so 3 × 1% × CRC 1,000,000 = CRC 30,000. This is capped at 20% of the unpaid tax and has no reduction. Late-filing fine (art. 79): half a salario base, CRC 231,100. If the taxpayer files, self-assesses and pays the fine voluntarily before any action by Hacienda, the fine drops by 80%, to CRC 46,220. Late-payment interest under the Código may also apply. It is not computed here: check it with Hacienda. ([Hacienda penalties table](https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf))

## When to refuse or refer

Refer to a Costa Rican Contador Público Autorizado or tax lawyer, rather than answering from this Guide, when:
- the business makes both credit-bearing and non-credit-bearing operations and the prorrata has to be computed or adjusted;
- the question involves free zone status, EXONET exonerations, or exempt institutions buying under special laws;
- real estate transfers, construction projects or tourism services registered with ICT are involved in a period before the phase-in ended;
- the client wants to enter or leave the simplified regime or the REA, or the used-goods regime;
- the item might fall under the 0.5% or 3% columns on the monthly return, or under a basket decree newer than 43790-H-MEIC-S; ([draft form resolution](https://www.hacienda.go.cr/docs/ProyResUsoformularios_IVAyREA.pdf))
- Hacienda has already started an action, audit or sanction proceeding;
- the client asks for a refund of a credit balance.

Refuse to guess a rate. If the classification of an item is not clear from the sources above, say so and point to the DGT or a professional.

## Filing and payment

- **System.** Returns are filed in TRIBU-CR, Hacienda's tax system that replaced ATV ("el nuevo sistema TRIBU-CR"). Authorisations that were set up in ATV carried over automatically to TRIBU-CR (Hacienda TRIBU-CR FAQ, question 56). The online office is the OVi.
- **Monthly return.** The general IVA return is TRIBU-CR code 150 ("IVA01", monthly). It replaced the old D-104 form. Hacienda's rent and health-services guidance refers to it as "formulario D-150 a través del sistema de TRIBU-CR". The draft 2025 resolution shows the form layout: sales and tax by rate, exempt sales with and without a right to credit, and purchases with the credit or the cost-for-income-tax split.
- **Deadline.** Art. 27: taxpayers "deben liquidar el impuesto a más tardar el decimoquinto día natural de cada mes, mediante declaración jurada de las ventas de bienes o prestación de servicios correspondientes al mes anterior". The tax is paid when the return is filed.
- **Nil and credit returns.** "La obligación de presentar la declaración subsiste aun cuando no se pague el impuesto o cuando la diferencia entre el débito fiscal y el crédito fiscal represente un saldo en favor del contribuyente" (art. 27). The duty continues until the taxpayer deregisters.
- **Quarterly and other returns.** Simplified regime: quarterly, within the first fifteen calendar days of October, January, April and July. REA: every four months or annually. Used goods and digital-service collectors: monthly (see the special regimes section).
- **Electronic receipts.** Every sale needs a Hacienda-authorised electronic receipt, issued and delivered at the time of sale. Failing to issue or deliver one is fined two salarios base, CRC 924,400 in 2026, with no reduction (Código art. 85). A repeat offence after a final ruling can close the business for five calendar days (art. 86). Refusing card or other electronic payment is fined one salario base, CRC 462,200 (art. 85 bis). This Guide has not sourced the current technical version of the electronic receipt: take it from Hacienda's comprobantes electrónicos pages. Working note (check, not sourced here): each electronic receipt carries a numeric key (clave numérica), which the earlier version of this Guide gave as fifty digits. Match it to the purchase before claiming a credit. Receipts issued in US dollars still have to be reported in colones on the return, at the exchange rate the rules require. ([Hacienda penalties table](https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf))

### Penalties (Código de Normas y Procedimientos Tributarios; amounts for 2026)

Penalties are self-assessed on form D-176 in TRIBU-CR.

| Breach | Penalty 2026 | Reduction (art. 88) |
| --- | --- | --- |
| Failing to register, update or deregister (art. 78) | Half a salario base (CRC 231,100) per month or part of a month, up to 3 salarios base (CRC 1,386,600) | 75% if corrected voluntarily before any Hacienda action; 80% if the fine is also self-assessed and paid at the same time. Not available when Hacienda registers the taxpayer on its own motion ([source](https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf)) |
| Late filing of a self-assessed return (art. 79) | Half a salario base, CRC 231,100 | Same scale: 75% or 80% voluntarily; 50% or 55% after Hacienda acts but before the sanction ruling; 25% or 30% after the ruling, within the appeal period ([source](https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf)) |
| Late payment (arts. 80 and 80 bis) | 1% of the unpaid tax per month or part of a month, capped at 20% | None ([source](https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf)) |
| Not issuing or delivering authorised receipts (art. 85) | 2 salarios base, CRC 924,400 | None ([source](https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf)) |
| Not keeping accounting records (art. 84) | 1 salario base, CRC 462,200 | Check whether art. 88 applies ([source](https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf)) |

Source: [Hacienda, "Infracciones y Sanciones Administrativas más relevantes", updated January 2026](https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf).

## Completion checklist

- [ ] Taxpayer registered in TRIBU-CR under the right regime and activities.
- [ ] Each sales line classified: 13%, reduced (4%, 2% or 1%), exempt with or without credit, or not subject, with the legal basis noted. ([Ley 6826 arts. 10-11](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML))
- [ ] Housing and small-business rents tested against CRC 693,300 (2026), and tax applied to the full rent if above it. ([salario base table](https://www.hacienda.go.cr/docs/SalariosBaseActualEHistorico.pdf))
- [ ] Exports and zona franca sales supported, and EXONET authorisations on file.
- [ ] Every input credit supported by an authorised electronic receipt or customs document; excluded items removed.
- [ ] Reduced-rate limit on credit (art. 26) and prorrata (arts. 22 to 24) applied.
- [ ] Foreign services: reverse charge booked by business recipients, and any card-issuer collection reconciled.
- [ ] Return code 150 filed by the fifteenth calendar day of the following month, even if nil or in credit; tax paid at filing.
- [ ] Credit balance carried forward or claimed under arts. 45 and 47 of the Código.
- [ ] Any late filing or payment penalty self-assessed on D-176, with the art. 88 reduction claimed where it is still available.

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
