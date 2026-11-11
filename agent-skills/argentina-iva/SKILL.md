---
name: argentina-iva
description: "Compute and classify Argentina IVA transactions for 2026. Use for debito fiscal, credito fiscal, the ordinary 21%, 10.5% and 27% treatments, domestic exemptions, mixed activity, imports of services, foreign digital services, exports, invoices and technical versus freely available balances. Covers individuals and companies in the general regime. Work from legal supply, taxpayer status, tax point and evidence, never a bank or supplier brand. Produces a monthly computation and reconciliation for professional review; ar-vat-return owns F.2051 filing. Specialist agents, customs valuation, export-refund claims, construction and agricultural elections are routed."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/argentina-iva"
  jurisdiction: "AR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Argentina: IVA computation and classification 2026 v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Responsables Inscriptos (RI), individuals or legal persons, computing ordinary national IVA under Ley 23.349, ordered text approved by Decreto 280/1997 (IVA Law). Arts. 1/4 cover domestic goods/services, definitive goods imports, qualifying imported services and foreign digital-service recipients. A universal turnover threshold does not determine RI status; test the actual taxable activity and any [Monotributo](ar-monotributo.md) eligibility/exit separately. CUIT is the 11-digit taxpayer identifier. Currency is ARS.

**Quick answer:** classify the actual supply and tax point, apply its lawful rate/base, allow only evidenced eligible credit, allocate direct/common/private costs, then keep technical credit and suffered-tax/direct-payment balances separate. Missing facts remain pending; “unknown” is not permission to tax every bank credit or manufacture input credit. Establish taxpayer/month, supplier/buyer status, contracts/invoices, use and prior balances first.

This Guide is **Not yet approved**. It loads the VAT workflow base, produces the transaction ledger and tax bridge, and hands the result to [ar-vat-return](ar-vat-return.md) for current F.2051 filing. The ordinary computation is shared by individuals and companies; corporate form does not itself require an obsolete form.

Out of scope: acting as withholding/perception agent, detailed customs values, export-refund applications, complex financial instruments, construction/developer computations, agricultural annual-payment elections, promotion/territorial regimes, intercompany valuation and litigation over inflation/limitations. Ordinary bank fees, medical/insurance/transport classifications, mixed credits and imported services remain covered below. Provincial AGIP/ARBA/IIBB collections are separate taxes.

## Rates, bands and thresholds

These are the ordinary treatments covered, not a claim that all special publishing/media or promoted rates are reproduced. Read current art. 28, not an embedded historical table. The old supposed 2.5% agricultural category is unsupported and is not used.

| Treatment | Conditions | Official source |
|---|---|---|
| General 21% | Taxable domestic goods/services unless a specific exemption/reduction/increase applies | IVA Law art. 28; https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Increased 27% | Specified gas/electricity/metered-water sales and art. 3(e)(4)-(6) services, outside premises exclusively dwelling/recreation/vacation or vacant land, **and** RI or Monotributo purchaser/user; decree exceptions below | Art. 28 paragraph 2; https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Reduced 10.5% foods | Live poultry/rabbits and cattle/sheep/pigs/camels/goats; their fresh/chilled/frozen uncooked/unprepared meats; fresh/chilled/frozen unprepared fruit/vegetables; bulk honey; cereals/oilseeds excluding rice; dried beans/peas/lentils; wheat flour NCM11.01 | Art. 28(a)(1)-(6); https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Reduced 10.5% bakery | Bread/bakery/biscuits exclusively from wheat flour, not prepacked for sale, under Food Code arts.726,727,755,757,760; not every bread/cake | Art. 28(a)(7); https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Reduced 10.5% passenger transport | Domestic land/water/air transport except qualifying exempt taxi/remis below | Art. 28(h); https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Reduced 10.5% qualifying healthcare | Nonexempt medical services supplied/contracted by co-ops, mutuals or prepaid systems; not all private fees | Art. 28(i); https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Reduced 10.5% qualifying bank loans | Interest/commissions on Ley 21.526 loans to RI borrowers; qualifying foreign-bank loan requires Basel-supervision condition | Art. 28(d); https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Reduced 10.5% irrigation electricity | Agroindustrial irrigation systems/equipment from 1 April 2026; separate from general commercial electricity | Art. 28(m), Ley 27.802 arts. 189/217; https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 ; https://biblioteca.arca.gob.ar/dcp/LEY_C_027802_2026_02_27 |
| Exempt short taxi/remis | Taxi/remis with driver, route no more than 100 km; not a blanket short bus/train exemption | Art. 7(h)(12); https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Exports | Qualifying goods exports, services effectively used abroad and international transport have art. 43 treatment; distinguish territorial/exempt classification from ordinary exempt no-credit sales | Arts. 1(b), 7(h)(13), 8(d), 43; https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Passenger-car input-credit limit | Credit corresponding to ARS 20,000 net value, not ARS 20,000 credit; stock/main taxable car-business exceptions apply | Art. 12(a)(1); https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |

### Ordinary exemptions and rate switches

Under arts. 7/28 and Decreto 692 arts. 29-31/66:

- Books, qualifying pamphlets/works, newspapers and periodicals, including digital subscriptions, are exempt across the commercial chain regardless of medium. Separately priced taxable extras do not inherit exemption; digital book access/download has its express exemption. The old blanket reduced rate for books/newspapers is incorrect.
- Natural ordinary water and plain whole/skimmed fluid/powder milk are exempt only for the named buyers, including final consumers, specified public bodies, school/university canteens, obras sociales and listed nonprofits. Qualifying fortified/enriched milk within the Food Code definitions remains included under decree art.29; other additives/product definitions and buyer status matter. Mineral/gaseous water is excluded. Public piped water is a service, not that goods exemption. An RI business purchase is not private final consumption just because the product is milk.
- Human medicinal specialties resold by authorised pharmacies/drugstores/similar establishments are exempt where the first domestic manufacturer/importer/contract-manufacturer sale was taxed. Prescription versus OTC is not the statutory distinction. First taxable supply is generally at the general rate absent a specific rule; pharmacy toiletries and other merchandise follow their own classification.
- Medical/paramedical exemption is limited to payments by statutory obras sociales, qualifying professional councils/colleges/pension funds, and the prescribed beneficiary copay/lack-of-service payments. Decree art.31 covers obligatory family and legally elected free-choice affiliates, excluding voluntary prepaid-style adhesion; qualifying ART medical payments receive the corresponding treatment. Preserve the original provider's evidence and the prescribed payer, copay or lack-of-service proof. An obra-social service channelled through prepaga/co-op/mutual can qualify with evidence. Direct private treatment is not “exempt up to a limit”; nonexempt co-op/mutual/prepaga services have the stated reduction, ordinary direct private fees the general treatment. Medical equipment/capital goods require actual NCM-annex classification, not a blanket medical-device rate.
- Recognised official-plan education, qualifying official-curriculum private classes and nurseries have the statutory exemption. Ordinary corporate training/consultancy is not automatically exempt.
- Exclusive tenant/family dwelling rent and the named rural/public-lessee cases are exempt. Other leases require their own statutory/regulatory test; the low-rent exception's current amount is not supplied. Construction/developer and complex lease computations are referred.
- Bank deposits/interbank, specified housing loans and other enumerated financial cases have conditional exemptions. Bank account/transfer fees are not blanket-exempt. Qualifying bank-loan interest/commission reduction does not reduce every bank fee.
- Insurance is ordinarily taxable. Private retirement, life insurance of any type, ART affiliation contracts and their reinsurance/retrocession have the express exclusion. Property/motor/general business policies are not exempt merely because issued by an insurer.

For 27%, Decreto 692 art. 66 excludes independent resellers/co-providers, gas used to generate electricity and value-added telecom services. Establish the supplied component, customer status and premises; an internet/utility billing label alone proves none of those tests. Mixed residential/business use is not exclusively dwelling. LPG/propane/butane, qualifying agricultural chemical fertilizers and listed agricultural services have their own art. 28 entries; do not apply a general “all agriculture” rate.

## The base

### 1. Establish the tax point and net price

Use IVA Law arts. 5-6 and 10-11. Ordinary goods normally trigger at the earliest delivery, invoice or equivalent. Ordinary services normally trigger at completion or partial/full payment, whichever first. Price-freezing advances trigger on receipt for that amount. Work on goods, judicial/professional-fund collections and construction certificates have express exceptions; do not use bank receipt or invoice date universally.

Metered gas/electricity/water generally trigger at due date or payment, earlier; qualifying residential final-consumer water has cash timing. Fixed-tariff water/sewer/drainage and tariff/unit-based telecom have their stated due/payment rules. Insurance triggers on policy issuance or contract subscription; nonproportional reinsurance also on later premium adjustments, proportional reinsurance on each reported cession (art.5(b)(6)). Its art.10 base is total policy premium net of financial surcharges; do not apply the generic financing-inclusion sentence to that exception. Financial returns and property rent have their own due/payment rules. Refer complex construction or disputed multi-event contracts before selecting a convenient period.

Net price follows invoice/equivalent and customary discounts; include ancillary freight, packing, insurance, installation and specified financing/rights components where art. 10 requires, even separately billed. IVA itself is excluded. Use debit/credit notes at the original applicable rate, correct period and proportion of input credit originally taken; do not deduct a bank refund without the underlying transaction.

Foreign currency without its own duly authorised rate uses Banco Nación seller rate at the close of the day before the tax point (Decreto 692 art. 49). Foreign digital intermediary perceptions and export invoicing have their own timing below. A later bank conversion is not necessarily the IVA conversion.

### 2. Calculate output and valid input credit

Sum output by lawful rate/base and adjustments. Input under art. 12 is the actual invoiced/import tax up to the lawful rate on the proper net/customs base, only for taxable-linked activity, with the supplier's tax point perfected and the required valid invoice/equivalent/data. Authorisation alone does not prove business use. Import customs evidence is distinct from the foreign supplier invoice.

Factura A/authorised equivalent with correct counterparty/IVA data supports an eligible RI's claim; C documents supply no supplier IVA credit. Current art. 39 requires IVA discrimination also on invoices to final/exempt/Monotributo recipients. Therefore B is not defined by absence of a breakdown, and an IVA line does not create a consumer's right to credit. Validate issuer status, document modality/authority, expiry and transaction, not only a bank descriptor or XML existence.

Current RG 4290 as amended permits normal electronic/controller modalities and prescribed contingencies/equivalents. Not every valid document has CAE: authorised CAI/manual contingency can be valid where permitted, including the stated Comprobantes en Línea fallback; web-service users have restricted alternatives, not unrestricted paper use. RG 5893 takes effect 1 November 2026 with its specified non-IVA-subject electronic-only requirement deferred to 1 March 2027; do not use an old blanket social-Monotributo exception. The applicable invoicing rule must fit the taxpayer and period.

### 3. Apply restrictions before apportionment

Art. 12(a)(1)'s car limit is IVA on ARS 20,000 net value, e.g. 4,200 at the general rate before further use restrictions. It is not a standard deductible percentage or complete denial whenever the car costs more. Stock and the specified main taxable rental/taxi/remis/commercial-traveller/similar-business exception need actual facts; Decreto 692 art. 51 defines the vehicle and the narrow similar-business test, excluding ambulances from the car definition.

Private consumption gives no business credit. Art. 12(a)(3)-(4) also restricts named restaurant/hotel/hourly lodging/bath/massage/gym/hairdressing/parking services and ordinary clothing even if a business invoice exists. Decree art. 52 allows the same-service resale or directly relevant conference/congress/convention/event exception and exclusive work-clothing/stock cases. Ordinary dual-use clothing does not qualify merely from a logo assertion. Do not revive the repealed old vehicle running-cost ban in art. 12(a)(2).

Under decree art. 57, an RI tenant carrying on taxable activity can credit qualifying premises utilities/telecom in the owner's/previous tenant's name where the tenant's payment duty is express in the current lease or a jointly signed note, subject to all normal restrictions. Do not reject this explicit exception solely because the invoice names the landlord.

### 4. Direct allocation, common costs and annual adjustment

First assign directly identifiable taxable-linked credit, exclude exempt/non-taxed-only and private portions. Only genuinely inseparable common credit uses the estimated proportion of relevant taxable net operations to total taxable + exempt + non-taxed operations (art. 13; decree arts. 53-55). Reduced-rate sales remain taxable. Exports with art. 43 recovery treatment require their own allocation; do not classify their inputs as ordinary exempt-only disallowed costs.

Adjust estimated common and private-use amounts in the last month of the commercial year, or calendar year where no commercial accounts, using actual full-year operations/use. Special operation bases can change the denominator under decree art. 54. If later evidence permits direct attribution, make the prescribed adjustment; software's global-prorata option does not override the legal allocation order.

### 5. Reconcile two different balances

After current eligible input and prior technical credit, a positive technical position is available for eligible direct payments/suffered IVA withholdings/perceptions; a negative position remains **saldo técnico** against future IVA debits under art. 24, subject to separate statutory recovery regimes. Direct-payment excess is separately **saldo de libre disponibilidad**, with authorised compensation/accreditation/refund/transfer procedures and restrictions. Do not combine both as freely available or promise offset against every ARCA obligation.

Use actual certificates and period rules, not every “AFIP/ARCA tax” bank debit. Current suffered-retention/perception timing and F.2051 administration are in the filing Guide. Do not publish a universal 50%/100% customer-withholding rate without its actual current regime/invoice status. Acting as agent is a separate job.

Keep nominal ARS balances. The law retains historical indexation language, but Ley 24.073 art. 39 limits the ordinary index system to March 1992; do not automatically revalue a normal monthly credit by current CPI. Art. 24 does not by itself establish an unlimited, dispute-free, prescription-free credit life. Special refunds and judicial remedies need their own analysis.

### Supplier and bank recognition: preserve evidence, correct assumptions

The prior brand library is retained as a recognition aid, never a legal rate source:

| Transaction family / old examples | What to inspect and classify |
|---|---|
| BNA, Galicia, Santander, BBVA, Macro | Account/transfer service versus qualifying loan/deposit; no brand-wide exemption |
| Mercado Pago, Prisma, Fiserv/First Data, Naranja X, Ualá | Separate processing fee, settlement principal and suffered taxes; normal fee versus exempt financial transaction |
| Edenor, Edesur, Metrogas, ECOGAS, AySA | Actual energy/gas/water service, metering, premises/customer and resale/irrigation exceptions |
| Telecom/Personal/Fibertel, Claro, Movistar, DirecTV, Arnet | Telecom versus value-added/internet/TV and bundle allocation; evidence controls rate, not brand |
| Aerolíneas, LATAM, Flybondi, JetSMART, trains/buses/subte, Uber/Cabify | Actual domestic/international passenger route, taxi/remis legal class and distance; separate platform commission; no claim that every named carrier operates a current route |
| OCA, Andreani, Correo, DHL, FedEx | Domestic courier/freight versus qualifying international transport and separate storage/agency fees |
| Carrefour, Disco/Vea, Rappi, MercadoLibre, office suppliers, Farmacity | Product-by-product food/medicine/book/general merchandise and separate platform services, plus actual taxable-business use |
| Tango, Bejerman, Colppy, Nubox, Microsoft, Google, Zoom, AWS | Actual invoicing entity and service performance/use; local subsidiary invoice is not automatically foreign reverse charge |
| Accountants, lawyers, advertising, consultants, notaries | General-regime domestic taxable professional service, any actual exemption/Monotributo status and special tax-point rules |
| San Cristóbal, Galicia Seguros, Experta ART, Sancor, MAPFRE | Actual policy: property/motor/business versus named life/retirement/ART exclusion |
| Obra social, clinic, pharmacy, device supplier | Payer/beneficiary/provider conditions, authorised medicinal resale or NCM goods classification; no prescription/OTC shortcut |

Galicia/Nación-style **FC A, RECIBO C, HONORARIOS, DÉBITO ARCA, PAGO EXTERIOR/SWIFT** are clues to retrieve documents. `$14.520.000,00` means ARS 14,520,000.00. A tax debit can be another tax; SWIFT can be a loan, import, export or internal transfer. Trace own transfers, withheld amounts, processor fees, refunds and cancelled invoices before matching tax totals.

If a genuine single-rate IVA-inclusive domestic amount is established, net = gross / (1 + rate), IVA = gross - net. Divisors are 1.21, 1.105 or 1.27 for the stated ordinary rates. Do not apply that arithmetic to a foreign net invoice, mixed basket, loan or unidentified deposit. Request missing evidence and leave credit unclaimed pending proof; do not fabricate a “conservative” taxable sale or final legal disallowance from incomplete records. The old ARS materiality/concentration/default-count flags were internal suggestions, not statutory thresholds; set review materiality separately, without making it tax law.

## Deadlines and filing

Ordinary IVA is monthly under art. 27. [ar-vat-return](ar-vat-return.md) owns the actual F.2051 **Portal IVA** sequence, CUIT calendar, no-movement return, suffered-tax timing and post-submission payment reconciliation. RG 5705 makes that route mandatory from November 2025 originals/amendments. The old F.2002/SIAP instruction is historical, not the 2026 route.

Agricultural-exclusive annual-payment elections and qualifying MiPyME payment deferrals require their own status/procedure; they do not permit omission of ordinary monthly records/returns. Imported-service payments below have a separate deadline from the monthly return. Save filed F.2051, acknowledgement and independent payment proof; one does not establish the other.

## Penalties and interest

Current 2026 penalties/interest and a taxpayer-specific limitation dispute are unconfirmed; compute none from old figures. Missing invoices, wrong tax point, unsupported credits, late filing and unpaid balance are distinct failures. Preserve source documents, adjustments and notices; refer disputed imported-service, exemption or recovery treatment before finalising a return. Bank reconciliation does not cure invalid documentation.

## Cross-border points

### Foreign services used in Argentina

An RI receiving services performed abroad and effectively first used/disposed of in Argentina falls under art. 1(d)/RG 549, including digital services. Non-RI foreign digital recipients instead fall under art. 1(e)/RG 4240. Supplier identity/domicile and effective use control; a global brand's Argentine entity is not automatically a service import.

For ordinary B2B art. 1(d), tax point is earlier completion or partial/full payment under art. 5(h), subject to the financial exception. Base is the foreign invoice's **net price** under the article after 26, not a price presumed to include Argentine IVA. Mixed taxable/exempt use follows the decree's special allocation/annual correction rule. Apply the actual rate and FX; pay within **ten administrative business days** after tax point under RG 549 art. 1. Financial institutions can collect under arts. 4-5; reconcile proof to avoid paying twice. Their special financial cases have separate treatment.

Paid eligible import IVA is creditable in the **following fiscal period after the tax point**, under art. 12/RG 549 art. 7; it is not same-month output/input cancellation. Current generic RG 549 VEP codes/screens have not been confirmed, so do not borrow the B2C code or describe legacy paper bank forms as current UI. Stop the payment instruction until the actual authorised route is established.

For non-RI RG 4240 digital services, credit-card perception is at first statement payment, full even if only part is paid; debit/prepaid at debit and aggregators at fund collection. Without a liable intermediary, recipient pays by the last day of the foreign-provider-payment month (arts. 3-4, 7-8). Intermediary conversion uses Banco Nación seller at the previous business-day close before its statement/liquidation/document; self-payment uses the decree's general rule. This is not the B2B ten-day timetable. No ordinary RI credit is created by treating a B2C charge as a business invoice.

### Exports

Definitive goods exports and international transport have the statutory exemption/art. 43 treatment. Domestic-performed services qualify only with effective use/first disposition abroad under art. 1(b), not merely a foreign customer or foreign-currency payment. Keep contracts, use/deliverable evidence and E invoices/credit/debit notes; a service export does not universally require a goods customs declaration. Official E-invoice guidance uses its own seller-divisa prior exchange-business-day conversion rule; do not use a hypothetical example rate as a market quote.

Art. 43 allows previously unused export-linked input credit against own domestic taxable debit; residual recovery/accreditation/refund/transfer requires registration, returns, statutory limits and the applicable procedure. This Guide does not promise automatic cash refund. Income-tax source/treaties/withholding and TP remain separate analyses in [argentina-cross-border](argentina-cross-border.md) and [argentina-transfer-pricing](argentina-transfer-pricing.md).

## Two worked examples that recompute

### 1. Direct allocation or blanket prorata?

Assume net operations 800,000 taxable and 200,000 exempt, direct taxable input IVA 40,000, direct exempt input IVA 20,000 and inseparable common input IVA 40,000, with all other credit conditions met. Common proportion is 80%; credit = 40,000 + 40,000 × 80% = 72,000. A blanket 80% of all 100,000 would give 80,000 and overclaim 8,000. Annual actual-operation adjustment remains required. If instead all 100,000 were genuinely common, 80,000 would be correct.

```oa-check
name: Direct allocation before common credit
inputs:
  taxable_operations: 800000
  exempt_operations: 200000
  direct_taxable_credit: 40000
  direct_exempt_credit: 20000
  common_credit: 40000
steps:
  - common_ratio: taxable_operations / (taxable_operations + exempt_operations)
  - eligible_credit: direct_taxable_credit + common_credit * common_ratio
  - wrong_blanket_credit: (direct_taxable_credit + direct_exempt_credit + common_credit) * common_ratio
  - overclaim: wrong_blanket_credit - eligible_credit
expected:
  common_ratio: 0.8
  eligible_credit: 72000
  wrong_blanket_credit: 80000
  overclaim: 8000
```

### 2. Imported cloud service versus local IVA-inclusive invoice

Assume an RI's wholly taxable-use foreign cloud service has April 2026 tax point and net foreign invoice translated lawfully to ARS 5,040,000, ordinary rate. Import IVA = 5,040,000 × 21% = 1,058,400, paid under RG 549 and creditable in May subject to payment/evidence. Do not divide the foreign net price by 1.21. A genuinely IVA-inclusive local invoice of the same gross amount would instead contain net 4,165,289.26 and IVA 874,710.74. Different facts change both base and timing.

```oa-check
name: Foreign net price versus local IVA-inclusive amount
inputs:
  foreign_net_price: 5040000
  local_gross_price: 5040000
steps:
  - import_iva: foreign_net_price * 0.21
  - local_net: round(local_gross_price / 1.21, 2)
  - local_iva: local_gross_price - local_net
expected:
  import_iva: 1058400
  local_net: 4165289.26
  local_iva: 874710.74
```

The six earlier practical cases are retained with corrected assumptions: domestic RI consulting net12m gives IVA2.52m/gross14.52m; qualifying office electricity net5m at27% gives1.35m/gross6.35m; a proved foreign-use SaaS export USD60,000 at a purely hypothetical1040 conversion gives ARS62.4m and no output IVA, with actual FX/evidence still required; imported cloud is corrected above; a valid domestic C supplier document1.2m gives no supplier input IVA; a month with taxable net100m at21% and20m at10.5%, plus valid purchases50m at21% and10m at27%, gives output23.1m-input13.2m=9.9m before balances/suffered taxes. Export30m in that last case needs art43 allocation, not automatic no-credit treatment. One C invoice does not prove its issuer's annual exclusion from Monotributo.

## Ask the client first

1. CUIT/status, month, fiscal close, all activities, prior returns and separate technical/free balances.
2. Issued/received invoices and equivalents, authorisation/modality, contracts, credit/debit notes, tax-point events and supplier/buyer status.
3. Product/process/NCM, premises/customer/use, medical payer/beneficiary, transport legal class/route and actual policy type.
4. Taxable/exempt/non-taxed operations, direct/common/private use, assets/cars and evidence for exceptions.
5. All ARS/foreign-currency banks/processors, suffered IVA certificates, imports/customs records and foreign-service payment/FX evidence.
6. Export contracts/E invoices/effective-use evidence, collection history and actual notices/unresolved classifications.

Working paper columns: tax-point/document dates, supplier/customer/CUIT, document/type/CAE-or-CAI/controller reference, net/FX/rate/IVA, in/out/import/export/exempt status, eligible credit/direct-common-private allocation, suffered-tax certificate/period, prior balances and pending issue. Retain **Output_Sales**, **Input_Purchases**, **Foreign_Service_IVA**, **IVA_Summary** and **Pending_Items** tabs or equivalent schedules. Keep current payment and next-period foreign-service credit separate. Reconcile documents to banks and return, and keep the unresolved issue, source needed and reviewer decision, not an invented default.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| Read for scope/taxpoint/rates/exemptions/base/credit/balances/exports: IVA Law current arts.1,3-5,7-8,10-13,24,26-28,37-43; quotations: "VEINTE MIL PESOS", "período fiscal inmediato siguiente" | https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 | 2026-11-11 |
| Read for ordinary conditions,FX,car/service restrictions,allocation,tenantcredit,utilityexceptions: Decreto692 arts.29-31,41,49-57,unnumberedafter65,66; quotation: "prestaciones de servicio de valor agregado en telecomunicaciones" | https://biblioteca.arca.gob.ar/search/query/dcp/DEC_C_000692_1998_06_11 | 2026-11-11 |
| Read for irrigation-electricity effective date: Ley27802 arts.189,217; quotation: "primer día del mes inmediato siguiente" | https://biblioteca.arca.gob.ar/dcp/LEY_C_027802_2026_02_27 | 2026-11-11 |
| Read for B2Bforeign-service tax/payment/credit: RG549 wholecurrentrule; quotations: "DIEZ (10) días hábiles administrativos", "período fiscal inmediato siguiente" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:549%7Co:3%7Ca:1999%7Cf:09/04/1999 | 2026-11-11 |
| Read for non-RIdigital collection/payment/FX: RG4240 arts.3-8; quotation: "hasta el último día del mes" | https://biblioteca.afip.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:4240%7Co:3%7Ca:2018%7Cf:11/05/2018 | 2026-11-11 |
| Read for normal/contingency invoice modes: currentRG4290arts.1,5-9,14-18; quotation: "Comprobantes en Línea" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:4290%7Co:3%7Ca:2018%7Cf:02/08/2018 | 2026-11-11 |
| Read for2026invoicing scope/effective dates: RG5893arts.2,5; quotation: "1 de marzo de 2027" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5893%7Co:9%7Ca:2026%7Cf:27/08/2026 | 2026-11-11 |
| Read for current monthlyF2051 transition: RG5705whole; quotation: "período fiscal noviembre 2025 y siguientes" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5705%7Co%3A9%7Ca%3A2025%7Cf%3A30%2F05%2F2025 | 2026-11-11 |
| Read for export E-invoice/evidence andconversion: ARCAexportinvoicespage; quotation: "facturas de exportación clase" | https://www.arca.gob.ar/derechos-de-exportacion-de-servicios/comprobantes-y-facturacion/comprobantes.asp | 2026-11-11 |
| Read for ordinary index ceiling: Ley24073art.39; quotation: "mes de marzo de 1992, inclusive" | https://www.argentina.gob.ar/normativa/nacional/ley-24073-472/actualizacion | 2026-11-11 |

Not yet confirmed: actual CUIT/month extension dates, generic RG549 current VEPcodes/UI, current penalties/interest, low-rent exception amount, specific product/NCM/telecom-bundle facts and any disputed limitation or exceptional inflation claim. Old blanket2.5%agriculture, bank/insurance/medicine/transport shortcuts, all-electronic-only credit and same-month foreign-service cancellation are replaced by verified conditional law. Specialist refund/agent/customs/construction/agricultural-election procedures remain out of scope, not ordinary exemptions.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `argentina-iva` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/argentina-iva. If neither is available, confirm every figure against the official source pages cited above before relying on it.
