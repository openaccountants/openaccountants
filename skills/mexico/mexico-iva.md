---
name: mexico-iva
description: Prepare, review and classify Mexican IVA transactions for 2026 from bank statements, CFDI XMLs and import/foreign receipts. Covers rates, border stimulus, cash timing, credit, withholding, monthly returns, original cases and specialist refusal boundaries.
version: 2.3
jurisdiction: MX
tax_year: 2026
last_updated: 2026-11-27
type: situation-rules
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mexico IVA

## Who this applies to

For Mexican personas físicas and personas morales preparing the ordinary monthly IVA working paper for **2026**, then mapping to SAT Declaraciones y Pagos. Establish actual supplies, settlement, credit and withholding from documents; a bank statement alone establishes neither rate nor credit. Read Required inputs and the specialist refusal boundaries.

## Rates, bands and thresholds

| Item | 2026 rule and conditions | Official source |
|---|---|---|
| Ordinary taxable acts | 16%, on the value excluding IVA; establish Mexican territorial scope first | [LIVA 1, 10, 16, 21](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf) |
| Listed zero-rated acts | 0%; eligible inputs remain subject to the credit conditions | [LIVA 2-A](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf) |
| Exempt acts | No output IVA; directly attributable inputs are not creditable | [LIVA 5 V, 9, 15, 20, 25](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf) |
| Border stimulus | Derived effective 8% = 16% × (1 − 50%); only eligible operations and taxpayers, not a general regional rate | [North XI–XIII](https://sidof.segob.gob.mx/notas/docFuente/5547485); [South X–XII](https://sidof.segob.gob.mx/notas/docFuente/5609182) |
| Border duration | Through 31 December 2026 for both decrees | [DOF extension, Articles One–Two](https://dof.gob.mx/nota_detalle.php?codigo=5777697&fecha=31/12/2025) |
| Ordinary personal-service/commission/rental withholding | Two thirds of IVA actually paid by a persona moral to a persona física, for the listed operations | [RLIVA 3 I](https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf) |
| Goods road freight withholding | 4% of consideration effectively paid by a persona moral, supplier may be individual or company | [RLIVA 3 II](https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf); [LIVA 1-A II c](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf) |
| Automobile investment deduction limits | MXN 175,000 ordinary; MXN 250,000 rechargeable electric, qualifying hybrid or hydrogen; IVA follows deductible proportion | [LISR 36 II; LIVA 5 I](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf) |
| Ordinary monthly payment | Day 17 of following month; ascertain any applicable calendar/decree extension before setting the actual date | [LIVA 5-D](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf) |

## The taxable base

**Classify the act, not the bank label.** LIVA 1 covers sales of goods, independent services, temporary use and imports. Goods territory follows Article 10; ordinary resident services carried out wholly or partly in Mexico follow Article 16; use of tangible goods follows Article 21. A foreign customer alone does not establish an export. Subordinated employment and ISR-assimilated remuneration are outside independent services (Article 14). Reconcile documented own-account transfers, loan principal, capital contributions, dividends, tax payments and personal drawings separately; do not infer them from a round amount, a government name or an ATM withdrawal. An advance for a taxable supply is not an excluded loan. [LIVA 1, 1-B, 14, 16, 18, 21][liva].

**Cash settlement.** Ordinary sales/services/rent are recognised when effectively collected, including advances, payment in kind and other extinction of the obligation. Cheques normally count when cashed, or transferred other than for collection. Credit entitlement requires effective payment in the relevant month as well as the other conditions. PUE is not proof that payment happened on the invoice date. The special interest accrual rule in Article 18-A is outside this ordinary workflow. [LIVA 1-B, 5 III, 11, 17, 22][liva].

### Zero-rated and exempt classification

- **Food and medicines:** Article 2-A I a covers non-industrialised animals/vegetables, excluding rubber and household pets. I b covers patent medicines and human/animal food, not just unprocessed or prescription items. Its exclusions include non-milk beverages (including juice), specified drink concentrates, caviar/smoked salmon/elvers, flavourings/microencapsulates/additives, chewing gum and processed household-pet food. Prepared food is ordinarily standard-rated, including takeaway/home delivery and premises with no eating facilities. Plain non-carbonated, non-compound water excludes containers below ten litres. Domestic-use water supply is zero-rated under II h, not municipal-name exempt. [LIVA 2-A][liva]; [RLIVA 6–7][rliva].
- **Agriculture:** zero rate only for the listed complete machinery/equipment in I e, fertilisers/pesticides/herbicides/fungicides destined for agriculture/livestock in I f, and hydroponic greenhouses/integrated equipment/irrigation in I g. III covers temporary use of the I e/g machinery, not farmland. II a covers the enumerated services directly to farmers/livestock producers for agricultural purposes; II b–h includes maize/wheat milling, milk pasteurisation, hydroponic-greenhouse services, cotton ginning, livestock/poultry slaughter, reinsurance and domestic water. Agricultural insurance is tested under the exemption, not assumed zero-rated. [LIVA 2-A][liva].
- **Publications/menstrual goods:** publications edited by the taxpayer qualify under I i; other sales of books/newspapers/magazines are exempt under Article 9 III. I j covers pads, tampons and cups for menstrual management; LIF 2026 Article 25 XIII also covers menstrual underwear and discs, reusable/disposable. [LIVA 2-A, 9][liva]; [LIF 25 XIII][lif].
- **Land/housing/used goods:** land and the residential part of construction are exempt, excluding hotels. Used movable goods are exempt except those sold by businesses. Residential rent requires actual housing use; the furnished/hotel/lodging exclusion applies. Allocate genuine mixed residential/commercial use. Commercial construction/rent generally follows the ordinary rate; do not tax the land portion. [LIVA 9 I–IV, 20 II][liva].
- **Services:** education requires the public-provider, authorisation/RVOE or preschool conditions of Article 15 IV. Urban/suburban/metropolitan public land passenger transport is exempt; private-vehicle rides booked through digital intermediary platforms are excluded from that exemption. Medical services requiring a medical title qualify when supplied by individuals alone, through civil societies, or authorised private assistance/beneficence institutions under XIV; public decentralised medical/hospital/radiology/laboratory services follow XV. A commercial hospital or veterinary label alone is insufficient. [LIVA 15 IV–V, XIV–XV][liva].
- **Insurance/finance:** test the policy against Article 15 IX: agricultural risks; qualifying housing-credit default and financial guarantees used for housing finance; life insurance/pensions and agent commissions on those policies. Test interest against the actual financing/provider/borrower/use conditions in X, including the restrictions for individuals and the credit-card exclusion. Ordinary account fees, card annuities and payment-processing commissions have no blanket exemption. [LIVA 15 IX–X, 18-A][liva].

### Border stimulus: north and south

Verify the actual establishment/local premises and municipality under each decree, actual delivery/performance in the region, timely IVA aviso under RMF 11.9.2 / procedure 3/DEC-5, and all exclusions. North Article I includes its 2022 municipality amendment; do not use the old incomplete list or postcode ranges as eligibility evidence. [2022 decree][north2022]. Under procedure 3/DEC-5, file within the month following RFC registration or the branch/establishment opening notice in the region; for resumption or obligation updates, by day 17 of the following month. Keep the notice receipt. [Anexo 2, 3/DEC-5][annex2]. The old general eighteen-month and payroll tests must not be applied as IVA prerequisites: Article VII's eighteen-month test concerns the ISR benefit; IVA has its separate XI–XIII north / X–XII south conditions. Both decrees remain effective through the end of 2026. [North][north]; [2020 amendment][northAmend]; [South][south]; [extension][expiry].

Do not apply the stimulus to real-estate sales, intangible sales/temporary use or the respective digital-content/service exclusions. Check CFF 69/69-B/69-B Bis listings, shareholders and affected transactions; limited correction/penalty-remission exceptions under RMF 11.9.12–13 and 20–21 require their own evidence, not a clean-RFC assumption. Transport must start and finish inside the region without outside stops. Imports are not covered by the domestic stimulus. South also excludes individuals electing LIVA 18-M. For uncertain eligibility/remediation, hold that transaction: Check this point with one of our partner accountants. [North XIII as amended][northAmend]; [North original exclusions][north]; [South XII][south]; [RMF 11.9][rmf].

Once 72 hours have passed after the aviso, use the CFDI option “IVA Crédito aplicado del 50%” and the permitted product/service catalogue entry. Generic 01010101 is excluded except qualifying public-in-general operations; excluded catalogue items cannot use the benefit. Retention uses the rate after the stimulus. Buyer input is the IVA actually transferred and qualifying for credit. [RMF 11.9.3][rmf].

### CFDI and input credit

Use the actual valid CFDI 4.0 XML, not just a bank description or PDF. Check issuer/recipient RFC and registered identity, recipient fiscal postcode/regime/use, issuer regime, place/date, currency/exchange rate where required, actual payment method/form, transaction details, separately stated IVA, fiscal UUID and seals. Confirm current SAT status and material transaction evidence; a stamp does not prove a real supply. Income, credit-note, goods-transfer, payment and payroll types are I/E/T/P/N; do not demand every ordinary payment field on a P or T document. CFF 29-A IX requires real existing transactions. [CFF 29, 29-A][cff]; [Anexo 20][technical].

For ordinary fully paid invoices use PUE and the actual form; for deferred/instalment invoices use PPD/99 (99 means payment form not yet defined). REP links actual payment to the original UUID; one per payment or monthly grouping for the same recipient is permitted. It is due by the fifth **natural** day of the following month, not five business days after each payment. Resolve a missing/late REP before treating the working paper as filing-ready; do not move the actual tax point to the REP issuance month or assume an unpaid PUE is paid. Correction/cancellation must preserve the real transaction and payment dates; see the existing mx-cfdi Guide for the current deadline and acceptance matrix. [SAT CFDI][satcfdi]; [RMF 2.7.1.32][rmf]; [LIVA 5 III][liva].

Apply all LIVA 5 conditions: indispensable business expenditure deductible for ISR; separate IVA on the qualifying fiscal receipt; actual payment; import pedimento in the taxpayer's name with IVA paid. Partially deductible costs allow only the corresponding IVA proportion. Personal/representation expenses and costs exclusively for exempt/non-object activities do not create recoverable IVA. Foreign digital receipts have the specific exception below. Gifts and employee benefits need their actual deductibility analysis; no generic gift threshold establishes a credit. [LIVA 4–5][liva].

**Attribution before proportion.** Non-investment inputs exclusively for taxable/zero-rated activities qualify in full, subject to all other credit conditions; those exclusively for exempt/non-object activities do not. Common inputs use eligible taxable/zero-rated activity value divided by total relevant activity value for that month, including Article 4-A non-object activity. Apply Article 5-C exclusions and its financial-sector exception; ordinary imports, qualifying fixed-asset disposals, dividends (subject to its predominantly-dividend exception), specified securities/currency transactions, interest/FX and the other listed excluded values do not simply go into an all-bank-receipts denominator. Investments, changes of use, preoperating costs and an existing Article 5-B election have different adjustment rules. Do not replace them with a universal annual true-up: Check this point with one of our partner accountants. [LIVA 5 V, 5-A–C][liva].

**Withheld input IVA:** the portion retained by the buyer must first be remitted; it is creditable in the monthly declaration following the declaration in which it was remitted. Track it separately from the non-retained portion and do not credit it in the purchase month. [LIVA 5 IV][liva].

**Restaurants:** representation expenses and bars do not qualify. An otherwise indispensable ordinary restaurant meal is not automatically representation: LISR 28 XX disallows 91.5%, leaving a derived 8.5% deductible portion, with the specified card/authorised-wallet payment condition. Qualifying travel meals have a separate rule and limits; hold those specific limits pending case review. [LISR 28 IV, V, XX; LIVA 5 I][lisr].

**Vehicles/fuel:** ordinary automobile investment credit follows the deductible fraction, capped by the amounts in the rate table; the higher limit has the stated propulsion conditions. The exclusive automobile-rental business exception is subject also to LISR 36 III's related-party restriction. Do not infer unlimited credit for taxis, cargo vehicles or motorcycles without establishing the legal vehicle classification and use: Check this point with one of our partner accountants. Automobile operating costs also follow the deductible-investment proportion under LISR 28 II. Fuel needs the prescribed non-cash payment even at or below MXN 2,000 and the supplier's current permit information on the receipt, as well as business use and IVA documentation. [LISR 27 III, 28 II, 36 II–III; LIVA 5 I][lisr].

## Cross-border points

Persona moral payments to individuals for independent personal services, commissions and temporary use of goods attract two-thirds IVA withholding; not every purchase from an individual is such a service. Goods road-freight withholding is in the rate table. LIVA 1-A also covers credit institutions acquiring assets by adjudication/payment in kind; companies acquiring scrap for industrial inputs/resale; and persons acquiring or temporarily using tangible goods supplied by non-residents without a Mexican permanent establishment. Those unreduced categories retain the IVA transferred, subject to the import-only taxpayer exception. This is not a universal withholding on foreign services. The former subcontracting 6% rule is repealed; specialised-service documentation under LIVA 5 II must still be checked. Do not revive it to match an old example. [LIVA 1-A, 5 II][liva]; [RLIVA 3][rliva].

Retain when effectively paying and remit separately, ordinarily by the following month's day 17. Input credit, prior favourable balances and other reductions cannot offset the retained tax remittance. A seller reduces its own IVA by tax withheld from it under the applicable rules; this differs from the buyer's later credit timing. [LIVA 1, 1-A, 5 IV][liva].

**Platforms in 2026:** where an intermediary collects both price and IVA on behalf of the supplier, LIVA 18-J II a requires retention of half the collected IVA for individuals furnishing RFC, all of it without RFC. Mexican-resident intermediaries have corresponding duties under 1-A BIS. LIF 2026 Article 25 IX extends the Article 18-J retention to companies and requires all collected IVA retained for foreign suppliers without a Mexican establishment selling goods in Mexico, and for proceeds deposited in foreign bank/deposit accounts. The airline non-retention facility in RMF 9.1.24 has its own treaty/IATA and RFC/foreign-ID conditions; hold that specific outcome for review. [First RMF modification][mod1]. Platforms remit by day 17 of the following month and provide the retention CFDI within the following month's first five days, under 18-J II b–c. Reconcile gross sale, platform commission, IVA, each retention and net bank settlement separately. The rider buying transport does not itself retain half of the fare's IVA merely because a platform is involved. A definitive platform-payment election has different credit consequences and is outside this ordinary return: Check this point with one of our partner accountants. [LIVA 1-A BIS, 18-J–M][liva]; [LIF 25 IX][lif].

**Foreign digital subscriptions:** Chapter III Bis covers only the enumerated paid, fundamentally automated digital services in Article 18-B: listed digital content (with electronic books/newspapers/magazines excluded from I), intermediation, online clubs/dating, and distance teaching/tests/exercises. Determine Mexican recipient location using Article 18-C, the actual supplier and SAT registration; SaaS/cloud storage or advertising is not automatically one category. A qualifying registered foreign provider charges ordinary IVA and its Article 18-D V receipt can support credit under 18-F without a Mexican CFDI, provided separate tax, required receipt particulars and other credit conditions are met. There is no blanket B2B self-withholding on these purchases. If the provider is not on the Article 18-D list, 18-I directs the recipient to the appropriate import rule. [LIVA 16, 18-B–F, 18-I][liva].

**Other imports:** goods import IVA follows the customs transaction and pedimento; the Article 27 base includes customs value plus import duty and other import contributions/charges, not IVA itself. Check Article 25 exemptions and temporary-import exceptions; do not assume all imports are taxable or all temporary imports exempt. Ordinary foreign services used in Mexico fall under 24 V (excluding international transport), become taxable when effectively paid under 26 IV and use the relevant Article 27/18 base. RLIVA 50 permits qualifying intangible/service import credit in the same monthly declaration. Record **both import IVA payable and eligible import IVA credit**; posting input B3 alone omits the liability. [LIVA 24–28][liva]; [RLIVA 48–50][rliva].

**Exports:** definite goods export needs completed customs formalities. Services must satisfy the applicable Article 29 export category and foreign-use requirements, not simply be billed in USD or to a foreign name. For IT development/integration/maintenance under IV i: infrastructure, human and material resources entirely in Mexico; provider device/ISP IPs in Mexico and recipient device/ISP IPs abroad; foreign customer's tax ID on the receipt; electronic payment from a foreign financial account to the provider's Mexican credit-institution account; no VPN provision and no application to goods situated in Mexico. Keep the accounting evidence required by RMF 4.6.6, including the foreign tax ID in the CFDI Leyendas Fiscales complement with “TIN del residente en el extranjero:”. Other qualifying service categories require their own conditions under Article 29/RLIVA 58–61. [LIVA 29][liva]; [RLIVA 57–61][rliva]; [RMF 4.6][rmf].

### Supplier pattern library

Route documents by these original patterns, then apply the operative rules. Names do not establish issuer, SAT status, item, rate, business use or credit.

| Original pattern group | Documentary treatment |
|---|---|
| BBVA/BANCOMER, BANORTE/BANCO MERCANTIL DEL NORTE, SANTANDER, CITIBANAMEX/BANAMEX, HSBC, SCOTIABANK, BANCO AZTECA, BANREGIO/BANBAJIO/BANCO DEL BAJIO; INTERESES/INTERES/RDTO; COMISION BANCARIA/ANUALIDAD TARJETA | Separate loan principal, interest and ordinary account/card charges. Test the actual financing exemption; do not exclude all fees. |
| SAT/SERVICIO DE ADMINISTRACION TRIBUTARIA, DECLARACION/PAGO DE IMPUESTOS, IMSS/SEGURO SOCIAL, INFONAVIT, AFORE/PENSIONES, GOBIERNO/SECRETARIA/AYUNTAMIENTO, MUNICIPIO/PREDIAL/TENENCIA, TRAMITE/LICENCIA GOBIERNO | Match actual tax/contribution/right payment. Government commercial supplies are not automatically outside IVA. |
| CFE/COMISION FEDERAL DE ELECTRICIDAD, TELMEX/TELEFONOS DE MEXICO, TELCEL/AT&T MEXICO/MOVISTAR, IZZI/TOTALPLAY/MEGACABLE, GAS NATURAL/NATURGY/GAS LP | Ordinary taxable route; verify actual item, agricultural electricity exception and business attribution. |
| AGUA/SAPAS/SIAPA/SACMEX | Distinguish zero-rated domestic water service from other supplies and charges. |
| PEMEX/GASOLINERA/ESTACION DE SERVICIO, GASOLINA/DIESEL/COMBUSTIBLE; CASETA/PEAJE/CAPUFE | Verify fuel or toll receipt, business use and the applicable credit conditions; do not invent a simplified-document exemption. |
| GNP/GRUPO NACIONAL PROVINCIAL, AXA/MAPFRE, METLIFE/SEGUROS MONTERREY, QUALITAS/HDI, SEGUROS/POLIZA/PRIMA | Read the policy; only the actual exempt categories qualify. |
| WALMART/WALMEX/BODEGA AURRERA, COSTCO, AMAZON MX, MERCADO LIBRE, OFFICE DEPOT/STAPLES, HOME DEPOT, LIVERPOOL/PALACIO DE HIERRO, SORIANA/CHEDRAUI/LA COMER | Split mixed-rate items; verify issuer and business purpose. |
| UBER/DIDI/BEAT/CABIFY; ADO/PRIMERA PLUS/ETN; METROBUS/METRO/TRANSPORTE PUBLICO | Distinguish private platform rides, intercity transport and qualifying urban public transport; separate rider's credit from platform's seller withholding. |
| VOLARIS/AEROMEXICO/VIVA AEROBUS | Domestic flights follow ordinary treatment. International passenger flights are not wholly zero-rated: Article 16 treats a quarter as Mexican service, and Article 29 VI zero-rates the qualifying foreign portion supplied by Mexican residents. Reconcile actual ticket components. |
| GOOGLE/GGLE (Ads/Workspace/Cloud), MICROSOFT/MSFT (365/Azure), ADOBE, META/FACEBOOK/FCBK, AMAZON WEB SERVICES/AWS, ZOOM, SLACK/ATLASSIAN/NOTION, SPOTIFY/NETFLIX/APPLE | Establish Mexican issuer, registered foreign digital provider or other import; apply the corresponding rules. |
| STRIPE, PAYPAL, MERCADOPAGO, CONEKTA/OPENPAY/SR PAGO, CLIP/IZETTLE | Separate principal, service fees, financing and refunds; no blanket fee exemption. |
| NOTARIO/NOTARIA/FE PUBLICA, CONTADOR/CONTABILIDAD/DESPACHO CONTABLE, ABOGADO/BUFETE/DESPACHO JURIDICO, CONSULTORIA/ASESORIA | Verify actual service, deductibility, entity and withholding. |
| NOMINA/SUELDO/SALARIO, PTU/REPARTO DE UTILIDADES, AGUINALDO/VACACIONES, SAR/AFORE; TRASPASO/TRANSFERENCIA PROPIA/MOVIMIENTO ENTRE CUENTAS; RETIRO/CAJERO/ATM; DIVIDENDO/PRESTAMO PERSONAL/DISPOSICION | Reconcile underlying payment and evidence; no tax classification based only on the pattern. Cash withdrawal itself does not prove personal expenditure. |

Legal classification sources for this matrix: [LIVA 1–3, 5, 14–16, 18, 18-B–J, 24–29][liva].

## Deadlines and filing

Ordinary IVA is calculated for each calendar month and paid through SAT Declaraciones y Pagos by the statutory date in the rate table. Monthly is not universal: LIVA 5-F/33 and special regimes need separate handling. Do not infer the period from the first/last bank entry; confirm complete monthly coverage and obligations. Any RFC-based extension or unusual holiday/portal deadline must be established for the actual taxpayer/date; otherwise use the statutory due date in the draft. [LIVA 5-D–F, 33][liva].

DIOT is separate from the payment return. RMF 4.5.1 allows the supplier information during the following month for individuals and companies, subject to applicable relief. Reconcile supplier RFC/foreign identification, transaction kind, paid bases/rates, creditable and non-creditable IVA and withholdings; follow the actual SAT form, not the old fifteen-percent field. RESICO individuals and companies within RMF 3.13.17 are relieved; RMF 2.8.1.17 also relieves the specified individual business/professional/platform/rental chapters where prior-year total income did not exceed MXN 4,000,000, or qualifying new starters estimate no more than that. Do not infer relief from merely using a software tool. [RMF 4.5.1, 3.13.17, 2.8.1.17][rmf].

A current saldo a favor may be credited against own IVA in following months until exhausted, or requested as a refund of the full balance; an amount requested for refund cannot also be carried forward. Do not use prior favourable balances to pay supplier-retention liabilities. Distinguish unused old balance from a newly generated current-period balance. [LIVA 6, 1-A][liva].

Refunds/discounts/returned advances require documented restitution of IVA identifying the original invoice. The seller reduces the taxable values in the following declaration(s) as Article 7 allows; the buyer reduces credit in the month of the specified event, and pays any excess over available credit. A credit note's issue/receipt alone is not proof of restitution. If retention was already remitted, Article 7 instead requires complementary declarations to reverse the operation. [LIVA 7][liva].

## Penalties and interest

Late/incorrect payment, filing, withholding, false CFDIs and blocked seals require case-specific correction and accessory calculations. The former approximate monthly surcharge and penalty ranges are not usable for 2026. No automatic penalty-free cure is promised. For the precise amounts, limitation/refund deadline, CFF 49 Bis/69-B procedure, response period or criminal consequences: Check this point with one of our partner accountants. [CFF][cff].

## Worked examples

Amounts are MXN unless stated. Original inputs are retained; results are conditional on documentary proof. [LIVA 1, 1-A, 5, 24–29][liva]; [RLIVA 3, 50][rliva]; [LISR 28, 36, 106][lisr].

### Example 1 -- Standard domestic sale with CFDI

Original input: 05.04.2026; EMPRESA TECH SA DE CV; CREDIT; Factura FE-2026-041 Consultoria abril; MXN 116,000.00. Original invoice base 100,000 and IVA 16,000 give gross 116,000. If the individual consultant's supply is an independent personal professional service to this company, IVA retention is 10,666.67 and ordinary Article 106 ISR retention is 10,000; expected cash is 95,333.33. Difference: 20,666.67. Reconcile contract/CFDI/retention records before accepting settlement; retain full base/output IVA for an actually settled invoice.

```oa-check
name: Original Example 1 invoice and professional-service cash reconciliation
inputs:
  net: 100000
  observed: 116000
steps:
  - iva: net * 0.16
  - gross: net + iva
  - retained_iva: round(iva * 2 / 3, 2)
  - retained_isr: net * 0.10
  - expected_cash: gross - retained_iva - retained_isr
  - difference: round(observed - expected_cash, 2)
expected:
  iva: 16000
  gross: 116000
  retained_iva: 10666.67
  retained_isr: 10000
  expected_cash: 95333.33
  difference: 20666.67
```

### Example 2 -- Corporate client withholds IVA

Original input: 10.04.2026; CORPORATIVO DELTA SA DE CV; CREDIT; Pago factura consultoria; MXN 105,333.33. Preserve the original fee 100,000 and gross 116,000. Both retentions matter: IVA 10,666.67 and ordinary professional-service ISR 10,000 leave cash 95,333.33, not 105,333.33. Difference: 10,000. Hold the invoice match; preserve the observed deposit and fee. On established settlement report full output IVA and actual IVA withheld; ISR is not an IVA credit.

```oa-check
name: Original Example 2 includes both IVA and ISR withheld
inputs:
  fee: 100000
  bank: 105333.33
steps:
  - iva: fee * 0.16
  - retenido: round(iva * 2 / 3, 2)
  - isr: fee * 0.10
  - net_cash: fee + iva - retenido - isr
  - difference: round(bank - net_cash, 2)
expected:
  iva: 16000
  retenido: 10666.67
  isr: 10000
  net_cash: 95333.33
  difference: 10000
```

### Example 3 -- Foreign digital service

Original input: 15.04.2026; NOTION LABS INC; DEBIT; Monthly subscription; USD 15.00; MXN 270.00. The implied rate 18 is not verified fiscal FX; supplier registration/category remain unestablished. If 270 is the confirmed pre-IVA Article 24/27 import base, output import IVA is 43.20 and fully eligible same-month import credit is 43.20: net zero, with **both sides** recorded. If the actual Chapter III Bis provider charged IVA and supplied a qualifying receipt, apply 18-F instead and do not self-assess again. Until those facts are established, the entry has no usable final IVA classification: Check this point with one of our partner accountants.

```oa-check
name: Original Example 3 conditional import has liability and credit
inputs:
  usd: 15
  mxn_value: 270
steps:
  - implied_fx: mxn_value / usd
  - iva_import: round(mxn_value * 0.16, 2)
  - eligible_credit: iva_import
  - net_iva: iva_import - eligible_credit
expected:
  implied_fx: 18
  iva_import: 43.20
  eligible_credit: 43.20
  net_iva: 0
```

### Example 4 -- Client restaurant meal

Original input: 18.04.2026; RESTAURANTE LA HACIENDA; DEBIT; Comida con cliente; MXN 2,500.00. Assuming the receipt is entirely ordinary IVA-inclusive restaurant consideration, base is 2,155.17 and IVA is 344.83. An indispensable ordinary restaurant meal satisfying the specified electronic payment/documentation conditions permits the derived 8.5% portion, 29.31; representation/bar treatment permits zero. The description alone establishes neither. Draft credit stays zero until the actual meal/business/payment facts are documented; do not call every business lunch non-deductible representation.

```oa-check
name: Original Example 4 conditional ordinary restaurant credit
inputs:
  gross: 2500
steps:
  - base: round(gross / 1.16, 2)
  - iva: round(gross - base, 2)
  - credit: round(iva * 0.085, 2)
expected:
  base: 2155.17
  iva: 344.83
  credit: 29.31
```

### Example 5 -- Software service for foreign customer

Original input: 22.04.2026; ACME CORP (US); CREDIT; Invoice MX-2026-012 Software development; USD 5,000.00; MXN 90,000.00. Preserve both currencies; the implied rate is 18, not established fiscal FX. If this is qualifying IT development exported under Article 29 IV i and every infrastructure/IP/tax-ID/payment/no-VPN/Mexican-goods condition above is documented, the 90,000 confirmed MXN base is zero-rated, output IVA zero; qualifying attributable inputs retain credit eligibility. Foreign client and overseas benefit alone do not close the conditions. Otherwise hold the zero-rating outcome: Check this point with one of our partner accountants.

```oa-check
name: Original Example 5 conditional qualifying software export
inputs:
  usd: 5000
  mxn_base: 90000
steps:
  - implied_fx: mxn_base / usd
  - output_iva: mxn_base * 0
expected:
  implied_fx: 18
  output_iva: 0
```

### Example 6 -- Fuel and vehicle proportion

Original input: 28.04.2026; GASOLINERA PEMEX EST 1234; DEBIT; Carga gasolina; MXN 1,200.00. Base 1,034.48/IVA 165.52 is a mathematical extraction **only if** gross contains solely consideration plus ordinary IVA. Fuel receipts may contain non-IVA-base components: use actual receipt IVA. Credit remains zero in the draft until business use, vehicle classification/value, prescribed non-cash payment (even below 2,000), current permit and valid receipt are established. Apply the deductible vehicle proportion to operating costs; neither automatic full credit nor an invented vehicle price is allowed.

```oa-check
name: Original Example 6 gross-only mathematical illustration
inputs:
  gross: 1200
steps:
  - net: round(gross / 1.16, 2)
  - iva: round(gross - net, 2)
expected:
  net: 1034.48
  iva: 165.52
```

### Original historical tests -- same inputs, corrected conditions

These 2026 cases assume genuine settled transactions, valid documents and exclusively taxable business use unless stated otherwise; internal line codes follow below.

| Original case | Preserved inputs and usable result |
|---|---|
| T1 | Company consulting sale 100,000 net: A1 100,000, A2 16,000. Do not import individual-service retentions into a company supplier. |
| T2 | Company supplies purchase 5,000 net + 800 IVA, valid CFDI, bank transfer: 800 eligible input; DIOT only if not relieved. |
| T3 | Agricultural company sells unprocessed vegetables 200,000: A5 200,000, A6 zero; eligible related inputs may be credited. |
| T4 | Individual residential rent 12,000/month: exempt only if actual housing conditions and furnished/hotel exclusion are satisfied; directly attributable input credit zero. |
| T5 | Company pays individual accountant 50,000 + 8,000 IVA: retained IVA 5,333.33, ordinary professional-service ISR 5,000, net cash 47,666.67. Non-retained IVA 2,666.67 may qualify now; retained 5,333.33 only in the declaration after remittance. The former 52,666.67 cash figure omitted ISR. |
| T6 | Chinese computer import, customs value 300,000, pedimento IVA paid 48,000: retain both input figures; 48,000 credit only if valid. It reconciles to 16% of 300,000 only assuming no extra customs-base additions; otherwise the pedimento/base needs correction. |
| T7 | Verified-eligible Tijuana goods sale 80,000 net: border output 6,400; eligibility and CFDI restrictions must actually be met. |
| T8 | Ordinary business sedan 350,000 + 56,000 IVA: deductible proportion 175,000/350,000 = half; eligible credit 28,000, blocked 28,000. |
| T9 | SAT-registered foreign Netflix corporate subscription 15,000/month: no blanket buyer withholding. If 15,000 is the pre-IVA price of a qualifying Chapter III Bis supply, provider IVA 2,400 and gross 17,400; if IVA-inclusive, base 12,931.03/IVA 2,068.97. Verify business indispensability and receipt before any credit. |
| T10 | Unpaid PPD 100,000 + 16,000 IVA/no REP: current credit zero. Later payment/receipt evidence must be reconciled; REP date does not replace statutory payment timing. |
| T11 | Supplier credit note 10,000 + 1,600 IVA/original UUID: reduce credit 1,600 on the actual Article 7 event; confirm restitution. If retention was remitted use the complementary-return rule. |
| T12 | Monthly taxable sales 800,000, exempt 200,000 and common input IVA 32,000: assuming these are all relevant values, no Article 5-C exclusion and no alternative election, factor 0.80, credit 25,600, blocked 6,400. No universal annual adjustment. |

```oa-check
name: Historical T5 T7 T8 T9 T12 exact reconciliation
inputs:
  professional_fee: 50000
  border_base: 80000
  car_base: 350000
  car_iva: 56000
  car_cap: 175000
  netflix: 15000
  taxable: 800000
  exempt: 200000
  common_iva: 32000
steps:
  - fee_iva: professional_fee * 0.16
  - fee_retention: round(fee_iva * 2 / 3, 2)
  - fee_isr: professional_fee * 0.10
  - fee_cash: professional_fee + fee_iva - fee_retention - fee_isr
  - fee_current_credit: round(fee_iva - fee_retention, 2)
  - border_iva: border_base * 0.08
  - car_credit: car_iva * car_cap / car_base
  - car_blocked: car_iva - car_credit
  - netflix_exclusive_iva: netflix * 0.16
  - netflix_exclusive_gross: netflix + netflix_exclusive_iva
  - netflix_inclusive_base: round(netflix / 1.16, 2)
  - netflix_inclusive_iva: round(netflix - netflix_inclusive_base, 2)
  - factor: taxable / (taxable + exempt)
  - common_credit: common_iva * factor
  - common_blocked: common_iva - common_credit
expected:
  fee_iva: 8000
  fee_retention: 5333.33
  fee_isr: 5000
  fee_cash: 47666.67
  fee_current_credit: 2666.67
  border_iva: 6400
  car_credit: 28000
  car_blocked: 28000
  netflix_exclusive_iva: 2400
  netflix_exclusive_gross: 17400
  netflix_inclusive_base: 12931.03
  netflix_inclusive_iva: 2068.97
  factor: 0.8
  common_credit: 25600
  common_blocked: 6400
```

## Working paper and required inputs

**Inputs before classification:** legal name/RFC, actual entity/regime, complete monthly statements; issued/received XMLs and SAT status; REP/payment evidence; foreign receipts/pedimentos; contracts/business purpose; mixed/exempt/non-object activity; prior returns/balances/refund requests; retentions; exports/border evidence. RFC length/regime code does not establish eligibility. Search records first. With neither statements nor documents, stop; statement-only work remains an **unfileable draft** with unsupported credits and classifications held.

**Uncertainty policy:** remove automatic assumptions of domestic/B2C/no withholding, excluded owner injection/personal ATM use or standard-rate treatment of unidentified transactions. Hold the affected classification and credit pending evidence. For an established ordinary taxable domestic sale without proven stimulus, use the ordinary rate; this does not settle an unidentified transaction. Preserve the original internal review triggers as workflow policy only: transaction 50,000; tax delta 5,000; counterparty concentration above 40%; more than four unresolved defaults; absolute net IVA 100,000. They are not legal thresholds or permission to file unresolved entries.

**Transaction sheet:** Date, Counterparty/RFC, CFDI UUID or permitted foreign/customs document ID, Gross MXN, Net MXN, output/input/import IVA separately, IVA retained by customer, IVA retained from supplier, rate/category, internal line code, evidence/default flag, missing facts and notes. Match DD/MM/YYYY or DD-MMM-YYYY dates and Cargo/Abono/Saldo to actual statements; resolve comma/pipe delimiters, SPEI references/CLABE, domiciliaciones, card abbreviations and cash use before classification. Do not mix supplier invoices with net platform/customer settlement or double-count own-bank transfers. Use blue source inputs, black formulas, green cross-sheet references, yellow unresolved rows and red attempted unsupported credit as internal formatting conventions.

Foreign-currency tax conversion uses the actual acquisition rate, or absent acquisition the Banxico DOF rate published on the day before tax accrual; absent that publication use the latest prior rate. Invoice TipoCambio, payment-date data and tax conversion are distinct. Preserve original currency, value, date and rounding reconciliation. Calculate with fractions of a peso; final tax-payment rounding follows CFF 20 (up to fifty cents down, fifty-one to ninety-nine up). [CFF 20][cff].

**Return Summary:** A/B/C/D are internal workbook labels, never official SAT casillas. Use positive tax-control amounts and a separate debit/credit sign; an entry can have multiple tags, so do not SUMIFS one exclusive line-code cell to collect both sale base and withholding.

- A1/A2 = ordinary taxable base/output; A3/A4 = qualifying border base/output; A5/A6 = zero-rated base/zero output; A7 = exempt base. A8 = A1+A3+A5+A7, a classified domestic-activity subtotal, **not** automatically the credit-factor denominator. A9 = A2+A4.
- B1/B2 = qualifying domestic input at the actual invoiced ordinary/border rate; B3 = qualifying import IVA credit. B4 is the input candidate total. Keep direct taxable, direct exempt/non-object, common and capital inputs separate; B5 applies only to the relevant common pool; B6 = eligible directly attributable credit + common-pool credit + separately eligible investment/import/previously retained credit, without duplicates.
- Add a separate import-IVA liability control to A9 when computing own tax. C1 = IVA actually withheld by customers; C2 = supplier IVA retained, remitted separately with its own later-credit tracking. D1 = own output/import liability minus B6; D2 = D1−C1. If D2 is positive, D3 may use only available old own-IVA balance, up to D2. D4 = remaining payable; D5 = newly generated balance only where D2 is negative. Carry unused old balance separately; do not turn it into a new refund claim. [LIVA 1, 5, 5-D, 6][liva].

### Refusal boundaries and historical edge cases

- **R-MX-1:** IMMEX/maquiladora, virtual/temporary imports, certification/guarantees; **R-MX-2:** proposed consolidated/group filing; **R-MX-3:** transfer-pricing adjustments to the IVA base. Do not classify these as ordinary transactions: Check this point with one of our partner accountants.
- **R-MX-4:** CFF 69-B/false-CFDI listing or materiality concern. Hold the affected documents and distinguish preliminary presumption, final finding and actual remedial evidence; do not claim all documents of every listed party are conclusively false. Procedural deadlines and case response: Check this point with one of our partner accountants.
- **R-MX-5:** annual ISR return; **R-MX-6:** payroll, nómina CFDIs, IMSS/INFONAVIT processing. Route to the corresponding existing work; do not prepare these through the IVA working paper.
- **EC1–EC10:** client lunch, business platform ride, foreign programmer/designer, incorrect-recipient RFC, supplier credit note, fuel, taxable construction advance, shop/apartment mixed rent, employee/independent-service boundary and commercial real estate remain covered by the operative rules above. Incorrect RFC requires a valid correction; no unsupported credit. Foreign freelancer is an import analysis, not automatic all-IVA withholding. Mixed-use allocation needs factual evidence; employment/contractor uncertainty is a hold: Check this point with one of our partner accountants.
- **EC11:** crypto payment/trading remains a specialist hold; **EC12:** donated goods require the Article 8 business/non-deductible-donation exception; **EC13:** parent/subsidiary management service remains subject to actual service/base/credit rules, with price adjustments under R-MX-3; **EC14:** goods return follows Article 7, not a credit-note-date shortcut. For the unestablished crypto/donation outcome: Check this point with one of our partner accountants.
- **Historic special categories, held pending transaction-specific proof:** gold/jewellery/bullion (old “10K” shortcut is unusable); shares/credit instruments/currency; artist/copyright and public-entertainment exemptions; international maritime service; furnished housing; diplomatic/charity/art imports and temporary-to-definitive imports; cargo/taxi/motorcycle/lease classification; gifts/employee benefits; preoperating and capital adjustments. No generic exemption, no-cap or full-credit outcome is offered: Check this point with one of our partner accountants.
- **Historic procedures/figures, archival only and not usable outcomes:** CFF authenticity/49 Bis five-business-day response, seal suspension/publication/criminal consequences; platform ISR table (2.5%/20%), online information access from 1 April 2026, platform-specific receipt implementation; five-year refund limit; DIOT platform/54-field/40,000-record and 1 August 2025 change claims; old penalties 1,810–22,400 and 17,020–97,330, approximately 1.47% monthly surcharge, full-unwithheld-amount and 55–75% credit-penalty shortcuts; RESICO 3,500,000 eligibility shortcut. Do not apply any of these from this Guide: Check this point with one of our partner accountants.

## Ask the client first

Use the Required inputs checklist; ask only for facts absent from the records. Keep each mismatch visible in the reviewer brief: transaction, missing evidence, conditional options/calculation and hold. This is not professional approval of the Guide.

## Sources

Each listed passage was read or its unchanged, already-proven quote reused on **2026-11-27**. URLs alone were not treated as reads. The operative rules control over older Guide versions; all cases retain their original inputs. Specialist holds above supply no usable tax outcome.

| Source and scope read | Official URL | Read on |
|---|---|---|
| LIVA: taxable acts/territory/settlement; zero/exempt; input credit, proportion, retention, balances; digital services; imports/exports | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf | 2026-11-27 |
| RLIVA: retention, agricultural/medicine definitions, service imports and foreign-use conditions | https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf | 2026-11-27 |
| LISR: business documentation/fuel; representation/restaurants, automobile costs/caps; professional-service ISR used only in examples | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-11-27 |
| LIF 2026: Article 25 IX platform IVA, XIII menstrual products, commencement | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIF_2026.pdf | 2026-11-27 |
| CFF current official copy: Article 20 FX/rounding; 29/29-A invoicing/materiality. Specialist procedure/penalty amounts not offered | https://dgesui.ses.sep.gob.mx/sites/default/files/2026-05/CFF.pdf | 2026-11-27 |
| North decree: IVA XI–XIII, separate ISR VII; original Article I geographical rule | https://sidof.segob.gob.mx/notas/docFuente/5547485 | 2026-11-27 |
| North amendment: intangible-use exclusion/transport and separate ISR notice provisions | https://dof.gob.mx/nota_detalle.php?codigo=5609181&fecha=30/12/2020 | 2026-11-27 |
| South decree: III and X–XII; region and IVA exclusions | https://sidof.segob.gob.mx/notas/docFuente/5609182 | 2026-11-27 |
| Border extension: Articles One–Two and commencement | https://dof.gob.mx/nota_detalle.php?codigo=5777697&fecha=31/12/2025 | 2026-11-27 |
| RMF 2026: 11.9 border, 4.5.1 DIOT, 3.13.17/2.8.1.17 relief, 4.6.6 IT evidence; unchanged 2.7.1.32 payment quotes reused from proven mx-cfdi | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf | 2026-11-27 |
| SAT CFDI and Anexo 20 4.0: common field/payment definitions, unchanged proven mx-cfdi quotes reused for the same scope | https://wwwmat.sat.gob.mx/consultas/35025/formato-de-factura-electronica-%28anexo-20%29; https://dof.gob.mx/2022/SHCP/SHCP_130122.pdf | 2026-11-27 |

Not yet confirmed: The specialist outcomes explicitly held above are not usable guidance. No open ordinary-return claim is offered for filing. Check this point with one of our partner accountants.

The first through fourth published RMF modifications and the 26 November advance were checked for applicability; the ordinary rules cited remain operative. The first modification updates border rule 11.9.13 and adds the specific airline facility; do not apply their exceptions without the required evidence.

| Additional operative source read | Official URL | Read on |
|---|---|---|
| north2022 -- municipality/notice or amending-clause applicability, as relevant | https://sidof.segob.gob.mx/notas/docFuente/5669251 | 2026-11-27 |
| annex2 -- municipality/notice or amending-clause applicability, as relevant | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-2-RMF-2026_DOF-28122025.pdf | 2026-11-27 |
| mod1 -- municipality/notice or amending-clause applicability, as relevant | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/1aRM_RMF2026.pdf | 2026-11-27 |
| mod2 -- municipality/notice or amending-clause applicability, as relevant | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/2aRM_RMF2026_01102026.pdf | 2026-11-27 |
| mod3 -- municipality/notice or amending-clause applicability, as relevant | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/3aRM_RMF2026_DOF_02102026.pdf | 2026-11-27 |
| mod4 -- municipality/notice or amending-clause applicability, as relevant | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/4aRM_RMF2026_DOF-30102026.pdf | 2026-11-27 |
| advance5 -- municipality/notice or amending-clause applicability, as relevant | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anticipadas/5aRM_RMF2026_Cuartaversion_anticipada_26112026.pdf | 2026-11-27 |

[north2022]: https://sidof.segob.gob.mx/notas/docFuente/5669251
[annex2]: https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-2-RMF-2026_DOF-28122025.pdf
[mod1]: https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/1aRM_RMF2026.pdf
[mod2]: https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/2aRM_RMF2026_01102026.pdf
[mod3]: https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/3aRM_RMF2026_DOF_02102026.pdf
[mod4]: https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/4aRM_RMF2026_DOF-30102026.pdf
[advance5]: https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anticipadas/5aRM_RMF2026_Cuartaversion_anticipada_26112026.pdf

[liva]: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf
[lisr]: https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf
[rliva]: https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf
[rmf]: https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf
[cff]: https://dgesui.ses.sep.gob.mx/sites/default/files/2026-05/CFF.pdf
[north]: https://sidof.segob.gob.mx/notas/docFuente/5547485
[northAmend]: https://dof.gob.mx/nota_detalle.php?codigo=5609181&fecha=30/12/2020
[south]: https://sidof.segob.gob.mx/notas/docFuente/5609182
[expiry]: https://dof.gob.mx/nota_detalle.php?codigo=5777697&fecha=31/12/2025
[lif]: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIF_2026.pdf
[technical]: https://dof.gob.mx/2022/SHCP/SHCP_130122.pdf
[satcfdi]: https://wwwmat.sat.gob.mx/consultas/35025/formato-de-factura-electronica-%28anexo-20%29

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained in the OpenAccountants skills registry.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
