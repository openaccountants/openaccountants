---
name: dominican-republic-itbis
description: Prepare and review ordinary Dominican Republic ITBIS for 2025, with the original April 2026 examples retained under their stated conditions. Covers rates, input credits, NCF, monthly IT-1, information reports and explicit holds for unproven special-regime outcomes. Read alongside vat-workflow-base.
version: 2.1
jurisdiction: DO
tax_year: 2025
last_updated: 2026-11-28
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Miguel Lantigua"
reviewed_on: 2026-11-03
tier: 1
domain: vat-gst
---

# Dominican Republic ITBIS

## Scope

This Guide covers ordinary 2025 ITBIS. The three original April 2026 bank examples remain dated April 2026; the ordinary rates and conditions used in those examples also apply to those transactions. This is not a general update to every later-2026 regime, penalty or collection rule. Read alongside [VAT workflow base](../global/methods/vat-workflow-base.md) and [workflow base](../global/methods/workflow-base.md).

## Ask the client first

A bank statement can start reconciliation; it cannot establish a completed ITBIS return. Obtain the RNC and actual registration/regime, filing month, industry and activities, sales and purchase invoices, NCF/e-NCF authorisations/status, credit notes, customs declarations and proof of payment, export evidence, withholding certificates, prior credit and earlier returns. Identify exempt/taxable activities, free-zone status, foreign services, fixed assets, inventory and operating expenses. Verify the RNC against DGII rather than inferring registration from a supposed identity-number length.

Keep Spanish bank descriptions, signs, original currency and any supported DOP conversion. Banreservas/Popular CSV exports and statements from Banco Popular Dominicano, Scotiabank DR, BHD Leon, Banco Santa Cruz or another bank are acceptable inputs. Reconcile cash, card and bank sales to invoices; cash is not automatically excluded. Unknown rate, location or credit eligibility is an unresolved fact, not an automatic 18%, domestic-location or permanent no-credit classification.

## Rates, bands and thresholds

Industrialised-goods transfers/imports and provision or letting of taxable services are within Article 335. Determine the actual supply, taxpayer, territory and exemption before applying a rate. See [Código Tributario, Title III, Articles 335–345](https://dgii.gov.do/legislacion/codigoTributario/Cdigo%20Tributario/Titulo3.pdf) and [DGII ITBIS guidance](https://dgii.gov.do/cicloContribuyente/obligacionesTributarias/principalesImpuestos/Paginas/Itbis.aspx), read 28 November 2026.

| Rate / treatment | Conditions and source |
| --- | --- |
| Standard 18% | Ordinary taxable supplies. Do not apply the printed conditional 16% general reduction in isolation: Article 345 conditions it on the revenue target; DGII confirms continuing 18% application from 2016. [DGII](https://dgii.gov.do/cicloContribuyente/obligacionesTributarias/principalesImpuestos/Paginas/Itbis.aspx) |
| Reduced 16% | Only the tariff descriptions in Article 345 II, including specified yogurt, butter, coffee, edible fats/oils, sugar and cocoa/chocolate products. Coffee exclusions and exact tariff classification matter. Not every processed food, and not a transition that automatically ended at 18%. [Article 345](https://dgii.gov.do/legislacion/codigoTributario/Cdigo%20Tributario/Titulo3.pdf) |
| Zero-rated exported goods | Goods actually exported under Article 342, supported by shipping/customs evidence. A foreign payer is insufficient. Related input relief and any refund require their own conditions and procedure. [Article 342](https://dgii.gov.do/legislacion/codigoTributario/Cdigo%20Tributario/Titulo3.pdf) |
| Exempt goods | Article 343's descriptions and tariff boundaries control. Preserve separate checks for basic/unprocessed foods, medicines, educational books, agricultural inputs and fuels: neither every product in these families nor every item within a mixed tariff subheading is exempt. Basic-basket exemption is not zero-rating. [Article 343](https://dgii.gov.do/legislacion/codigoTributario/Cdigo%20Tributario/Titulo3.pdf) |
| Exempt services | Article 344 includes financial services including insurance, pensions, land passenger/freight transport, electricity/water/rubbish collection, housing rental, health, educational/cultural, funeral and beauty-salon services. Apply the actual service definition, not every sale by an institution in that industry. [Article 344](https://dgii.gov.do/legislacion/codigoTributario/Cdigo%20Tributario/Titulo3.pdf) |

[Decreto 293-11, Articles 14–15](https://dgii.gov.do/legislacion/decretos/Documents/2011/decreto293-11.pdf) supplies the service conditions. Financial services include deposits, loans, credit-card services, credit lines/letters and foreign exchange; an unrelated service or brokerage commission is not exempt merely because its name says commission. Electricity/water supply is exempt without an invented domestic-consumption threshold; installation, repair and the relevant equipment/materials are excluded from that exemption. Exempt providers do not thereby acquire all their inputs exempt. Do not extend an export-goods conclusion to exported services without proving the separate service conditions.

## The method, step by step

1. Build the invoice-level sales and purchase registers. Distinguish taxable, exempt, zero-rated and non-supply movements; domestic, international and DR-CAFTA labels do not themselves establish a rate. Reconcile payroll/TSS/ISR, loans, dividends and own-account transfers to their underlying records rather than creating input/output ITBIS from a bank description. Employment in a relationship of dependence is not a service for Article 335 purposes (Decreto 293-11, Article 3).
2. Use Article 338's tax points rather than bank dates alone: goods invoice or, absent it, delivery/withdrawal; imports when available to the importer under customs law; services at the first invoice, completion or partial/full payment. For letting, the earlier contract signature or delivery applies; long-term letting or combined movable/immovable letting uses the earlier instalment due date or receipt, subject to the regulation. Reconcile payment dates without replacing the supply period.
3. Use Article 339's base. Domestic goods include ancillary charges and applicable selective-consumption tax, less discounts. Imports use the customs tariff value plus **all import taxes**, not an unsupported universal “18% of CIF plus duty” shortcut. Service consideration excludes the mandatory legal tip. Taxable/exempt status and any special base must be established before calculating tax. Customs ITBIS is paid with customs taxes under Article 354.
4. Deduct input ITBIS only when **all** Decreto 293-11 Article 18 conditions are met: claimant is an ITBIS taxpayer; use is for taxable activities subject to the stated exempt-producer/exporter exceptions; expenditure is ISR-deductible; ITBIS was expressly passed to that claimant; credited ITBIS is not also taken as ISR cost/expense; it is not from assets in Category I; and tax is separately shown in a compliant fiscal document. Local and service purchases need the applicable fiscal/supporting evidence; imports require DGA documents showing tax paid (Articles 17–18). A B01 alone does not prove recoverability.
5. Allocate directly attributable inputs first. For common inputs that cannot be distinguished between taxable and exempt operations, Article 349 uses taxable operations divided by total operations for the period. Preserve the statutory exceptions; “exempt” is neither universal full recovery nor universal denial. Article 350 excess eligible credit carries forward; no automatic cash refund or exemption from filing follows.
6. Record withholding suffered separately from output tax and input deductions. Preserve gross taxable sales/output; apply only actual supported payments on account in the correct period. The supplier's credit and a withholding agent's own duties are separate. Do not impose universal government 100%, corporate 30%, card 2% of gross or nonresident 18% rules. The old Norma 08-04 was repealed: [Aviso 24-23](https://dgii.gov.do/publicacionesOficiales/avisosInformativos/Documents/2023/24-23.pdf). Its appearance in an older form legend does not restore it.

Sources: [Title III, Articles 338–350, 354–355](https://dgii.gov.do/legislacion/codigoTributario/Cdigo%20Tributario/Titulo3.pdf), [Decreto 293-11](https://dgii.gov.do/legislacion/decretos/Documents/2011/decreto293-11.pdf), [DGII Guide 7](https://dgii.gov.do/publicacionesOficiales/bibliotecaVirtual/contribuyentes/itbis/Documents/1-Guia%207%20-%20(ITBIS).pdf), read 28 November 2026. Guide 7's later-2026 penalty/collection material is not applied retroactively here.

## Fiscal documents and monthly filing

Article 355 requires documents supporting taxable **and exempt** transactions and separately stated tax. Verify the actual issuer, RNC, invoice type, authorisation/status, applicable expiry, supply and supporting evidence. Do not require a Dominican NCF on every foreign invoice or assume any document alone confers a credit.

| Paper / electronic type | Function, subject to the underlying legal conditions |
| --- | --- |
| B01 / E31 | Fiscal-credit invoice; eligible credits remain subject to all credit conditions. |
| B02 / E32 | Consumer invoice; does not support buyer ITBIS credit. |
| B03 / E33; B04 / E34 | Debit note; credit note. Trace to the original transaction and adjustment conditions. |
| B11 / E41 | Purchases from persons not registered as taxpayers, using the prescribed purchaser-issued document. |
| B12 | Authorised Registro Único de Ingresos; not a general receipt for all small sales. DGII's January 2025 guidance retains traditional series B during the voluntary period and requires E32 afterward. Establish the taxpayer's actual period. |
| B13 / E43 | Minor work-related expenses under the prescribed category. |
| B14 / E44 | Authorised special-regime transactions; not automatic exemption for any free-zone-labelled supplier/customer. |
| B15 / E45 | Government transactions. |
| B16 / E46 | Goods exports. |

An authorised, digitally signed e-CF has the same legal validity/effects as paper. These are specific codes, not every number between E31 and E46. Do not invent E12. The taxpayer's mandatory e-CF phase, certification/authorisation, actual expiry, transmission protocol and paper-replacement date remain a non-usable hold until established. **Check this point with one of our partner accountants.**

Sources: [DGII document types](https://dgii.gov.do/cicloContribuyente/facturacion/comprobantesFiscales/Paginas/tiposComprobantes.aspx), [Guide 5](https://dgii.gov.do/publicacionesOficiales/bibliotecaVirtual/contribuyentes/facturacion/Documents/Comprobantes%20Fiscales/1-Guia%205-Comprobantes%20Fiscales.pdf), [DGII B12 guidance dated 13 January 2025](https://ayuda.dgii.gov.do/conversations/facturacin-electrnica/ca4914-cmo-deben-facturar-electrnicamente-los-contribuyentes-que-se-encuentran-autorizados-a-emitir-comprobantes-de-registro-nico-de-ingreso-b12/678542666d8c84701c43e5b6), read 28 November 2026.

The ordinary ITBIS period is a calendar month. File IT-1 and pay within the first **20 days** of the following month, including a return when no tax is payable (Article 353); use DGII Oficina Virtual or the applicable DGII filing channel. Confirm registration and actual regime; an unverified RST threshold is not permission to omit ordinary filings.

Applicable information reports have a different ordinary deadline: Norma 07-2018 Article 8 requires the first **15 days** after the invoicing month. 606 covers costs/expenses, input credits and relevant retentions/perceptions; 607 sales and third-party retentions with prescribed detail/summary requirements; 608 cancelled fiscal documents and reasons; 609 foreign-service payments. No-operation 606/607/608 are informative reports under that rule. Establish any actual fiscal-solution/e-CF substitution rather than duplicating or omitting reports by assumption. Validate corresponding reports before the tax return. Sources: [Norma 07-2018, Articles 3–10](https://dgii.gov.do/legislacion/normasGenerales/Documents/NG%20sobre%20Comprobantes%20Fiscales/Norma07-18.pdf), [Article 353](https://dgii.gov.do/legislacion/codigoTributario/Cdigo%20Tributario/Titulo3.pdf), read 28 November 2026.

### Return mapping

The cited [DGII IT-1 2020 instructivo](https://dgii.gov.do/publicacionesOficiales/bibliotecaVirtual/contribuyentes/itbis/Documents/Instructivo%20LLENADO%20IT-1%202020.pdf), pages 17–21 and Annex A, supplies this versioned map, not an invented annual 2026 form. Match the actual period's form before filing; special-rate/construction/agent sections require their own conditions.

| Item | Main IT-1 field in that instructivo |
| --- | --- |
| Total operations; goods exports; local exempt sales | 1; 2; 4 respectively. Other exempt/non-subject categories have distinct fields; do not collapse them. |
| Taxable bases at 18% / 16% | 11 / 12. Output at those rates: 16 / 17; total output: 21. |
| Eligible local purchases / deductible services / imports | 22 / 23 / 24, using the corresponding Annex A field 56; total deductible: 25. |
| Current output less deductible input | Positive result 26; negative result 27. |
| Prior credit | 29, from previous return's new credit field 34. |
| Supported payments computable for retentions | 30, from Annex A field 33. Do not replace this with the historical invented “line 13”. |
| Adjusted payable / new credit | 33 / 34, after applicable supported credits/payments and adjustments. |

The agent's retention/perception section is separate from tax on the supplier's sales. Some actual agent procedures involve related IR-17 reporting; this Guide establishes no blanket “all ITBIS goes on IR-17” rule, no universal nonresident self-assessment and no universal tenth-day ITBIS deadline.

## Bank patterns and working paper

These are search candidates, not automatic tax decisions. Retain the underlying expense or receipt even when it produces no input/output ITBIS.

| Original pattern | Evidence-based treatment |
| --- | --- |
| BANRESERVAS, BANCO DE RESERVAS; POPULAR, BANCO POPULAR; BHD LEON, SCOTIABANK DR | Confirm financial-service nature; qualifying financial services are exempt. A bank name alone does not classify every transaction. |
| DGII; TSS, SOCIAL SECURITY | Reconcile genuine tax/social-security payments, not new purchases. Keep amounts in the ledger. |
| DGA, ADUANAS | Separate customs charges, duties and paid import ITBIS; eligible DGA-supported input tax must not be discarded with the payment. |
| EDENORTE, EDESUR, EDEESTE; CAASD, INAPA | Electricity/water supply exemption; separately examine installation, repair and materials. |
| CLARO DR, ALTICE, WIND TELECOM | Actual telecom supply/invoice; ordinary taxable service, not a rate inferred solely from provider. |
| GOOGLE, MICROSOFT, META, AWS | Foreign-service investigation; do not automatically self-assess 18% or create matching credit. See hold below. |
| SALARIO, WAGES; TRANSFERENCIA PROPIA | Confirm dependent employment or an actual own-account transfer; no supply inferred solely from the description. |

The working paper should retain source/invoice reference, date and tax point, counterparty/RNC, NCF/e-NCF, original currency/conversion, signed gross, net, tax, rate/classification, eligible/ineligible/unresolved input, allocation, withholding certificate/period, return field and open evidence. Summarise output at 18% and 16%, zero-rated exports, exempt operations, eligible input, prior credit, supported payments on account and net payable/credit separately. Preserve Spanish CSV text, compare invoices to bank/card/cash totals and reconcile customs, notes, reports and the prior return. A summary without the invoice-level audit trail is insufficient.

## Worked cases

These preserve the original inputs. Conditional results are usable only if the stated facts are established. Amounts in an explicit hold are not filing instructions.

### Original current examples

**Example 1 – domestic sale**

**Input:** `05.04.2026 ; CLIENTE DOMINICANO SRL ; CREDIT ; Factura DO-041 ; DOP 118,000`

If this is an ordinary domestic taxable sale whose DOP 118,000 is inclusive of 18% ITBIS, net is DOP 100,000 and output DOP 18,000. Map the base/output to fields 11/16 in the cited form. The bank entry alone does not establish rate, tax inclusion or tax point.

```oa-check
name: Original April 2026 domestic sale, conditional 18 percent inclusive
inputs:
  gross: 118000
  rate: 0.18
steps:
  net: gross / (1 + rate)
  output: gross - net
expected:
  net: 100000
  output: 18000
```

**Example 2 – goods export, if established**

**Input:** `15.04.2026 ; US BUYER ; CREDIT ; Export ; DOP 500,000`

If evidence establishes an actual goods export within Article 342, net is DOP 500,000, output DOP 0 and the class is zero-rated, mapped to field 2. The label “US BUYER” or “Export” does not establish those facts. Exported services require separate conditions; hold that outcome if the supply is a service or export evidence is missing. **Check this point with one of our partner accountants.**

**Example 3 – bank commission, if financial service**

**Input:** `30.04.2026 ; BANRESERVAS ; DEBIT ; Comision ; DOP -200`

If this is a qualifying financial-service commission, record the DOP -200 expense as exempt, with no input ITBIS. Keep the expense in the accounts. If it is a different service, obtain the actual invoice and classify it; do not discard it solely because BANRESERVAS appears.

### Preserved historical numerical tests

The original historical tests did not specify an individual transaction year; none is invented here. Apply their stated facts to the actual period and establish every operative condition.

| Test and original inputs | Corrected usable result or explicit hold |
| --- | --- |
| 1. Dominican supplier, office supplies, gross DOP 11,800, ITBIS DOP 1,800, net DOP 10,000; valid B01 | The split is correct. Deduct DOP 1,800 only if every Article 18 condition is met, ordinarily local-purchase field 22 through Annex A field 56. B01 validity alone is insufficient. |
| 2. Registered exporter ships goods to the US, net DOP 500,000 | Article 342 goods-export proof supports DOP 0 output. Related eligible inputs remain subject to the export/input rules; no automatic universal refund. |
| 3. Sedan DOP 2,000,000, ITBIS DOP 360,000, valid B01 | Preserve the stated price and tax; do not reinterpret whether the price includes tax. A sedan is not automatically denied credit merely by its label. Actual use, ISR deductibility and all credit conditions are needed; no final DOP 360,000 credit or blanket block is established. **Check this point with one of our partner accountants.** |
| 4. US firm provides consulting, USD 3,000 (approximately DOP 180,000), no ITBIS invoice | Preserve the original approximate conversion as a case assumption, not an official FX quote. DOP 180,000 × 18% = DOP 32,400 is only the historical hypothetical arithmetic. No automatic DOP 32,400 self-assessment plus equal credit/net zero is established. Territoriality, actual service, taxpayer/agent and documentation require resolution. **Check this point with one of our partner accountants.** |
| 5. Retail supplies, B02, ITBIS DOP 900 | B02 does not support buyer ITBIS credit. Do not claim DOP 900 from that document; seek compliant correction. |
| 6. Government services, DOP 100,000 plus ITBIS DOP 18,000, stipulated actual 100% ITBIS withholding | If the sale is ordinary taxable and the DOP 18,000 retention is actually certified/computable in this period, retain DOP 18,000 output and DOP 18,000 payment on account: transaction-only net DOP 0 before other return items. This does not establish a universal government withholding rate. Use the supported Annex A/main-field path, not invented line 13. |
| 7. Credit-card payments DOP 500,000, stipulated actual 2% / DOP 10,000 withheld | Arithmetic is DOP 500,000 × 2% = DOP 10,000. The rate is original case data, not a current universal levy on gross card payments. Verify the certificate, legal base, period and computable amount before using DOP 10,000 as payment on account; no fabricated sales-tax split. |
| 8. Client dinner DOP 5,900 inclusive of ITBIS DOP 900 | The stated split gives net DOP 5,000. Business purpose, ISR deductibility, compliant document and the remaining credit conditions control; neither automatic DOP 900 recovery nor a blanket entertainment ban is proved. **Check this point with one of our partner accountants.** |

```oa-check
name: Original office supplies tax split, credit still conditional
inputs:
  gross: 11800
  stated_tax: 1800
steps:
  net: gross - stated_tax
expected:
  net: 10000
```

## Preserved edge cases and sector boundaries

| Original edge case | Outcome and missing conditions |
| --- | --- |
| EC1 – purchase without NCF | Identify the required evidence/document and seek correction. No credit from an unsupported domestic purchase merely because it was paid; do not automatically call the whole gross amount an ISR-deductible cost. |
| EC2 – card processor retaining 2% | Keep the actual certificate/amount and original stipulated rate separate from law. Norma 08-04 is repealed; verify the operative base/rate/period. Historical test 7's arithmetic remains above. |
| EC3 – free-zone local sale | A free-zone company sells finished goods to a Dominican company. R-DO-1 below. Article 357's export treatment for otherwise taxable goods moving from national territory to an industrial free zone, and import treatment in the reverse direction, does not prove every individual exemption, local-service treatment or B14 entitlement. |
| EC4 – returned goods / B04 | Article 338 permits nullification within 30 days counted from the supporting document or delivery, with party agreement, goods returned and consideration refunded; partial refunds leave tax on the unrefunded amount. Trace the original invoice and actual conditions; a credit-note label alone is insufficient. |
| EC5 – US consultant USD 5,000 | A Dominican company pays the US consultant USD 5,000 for services. This is separate from historical test 4's USD 3,000. No invented DOP conversion, universal reverse charge, matching input credit or IR-17 result. The foreign-service hold below applies. **Check this point with one of our partner accountants.** |
| EC6 – pharmacy exempt goods plus taxable general-store supplies | A company operates both businesses. Classify the actual goods, directly allocate attributable inputs, then apply Article 349 to common inputs that cannot be distinguished. Do not infer every pharmacy sale is exempt. |
| EC7 – government retaining 100% ITBIS | Preserve the stipulated retention fact, subject to actual certification/computability. Keep gross output and the payment on account distinct, as in historical test 6; no universal government rate is asserted. |
| EC8 – foreign digital B2C provider | A foreign e-commerce company sells digital services to Dominican consumers. Individual registration, collection, territorial and effective-date treatment is not established by the SaaS label. Non-usable hold. **Check this point with one of our partner accountants.** |
| EC9 – new commercial building | A company sells a newly constructed commercial building. Do not charge 18% on the entire real-estate price or assume a universal “improvements only” base. Distinguish property transfer, materials, construction/professional services and any special base. Non-usable individual outcome. **Check this point with one of our partner accountants.** |
| EC10 – inventory donated to charity | A company donates inventory to a charity. Article 336 includes onerous or gratuitous transfers/withdrawals; that does not establish this charity's exemption, valuation or a universal fair-market-value tax charge. Non-usable individual outcome. **Check this point with one of our partner accountants.** |

Retain these original sector enquiries:

- **Tourism:** ordinary taxable hotel/restaurant services use the ordinary rate, but do not assume the full all-inclusive package is a universal base. CONFOTUR and other specific incentives require their own evidence. Article 339 excludes the mandatory legal tip; Aviso 24-23 identifies that tip as 10% of the invoiced amount under Labour Code Article 228. Special-package/incentive outcome remains held. **Check this point with one of our partner accountants.**
- **Financial sector:** qualifying banking, credit-card and insurance services are exempt under Article 344/Decreto Article 14(d); no blanket 18% on all bank commissions/general insurance. Classify an independent commission or other service separately.
- **Agriculture:** preserve the raw foods, medicines, agricultural-input and raw-tobacco enquiries. Article 343's actual tariff/product/use boundaries govern; no all-agricultural-inputs exemption. Processed cigars actually exported as goods follow Article 342 if proved; raw-tobacco classification without its actual product/tariff evidence stays unresolved. **Check this point with one of our partner accountants.**
- **Manufacturing/free zones:** otherwise taxable national-to-industrial-free-zone goods and reverse movements have the Article 357 boundary; imports, inter-zone supplies, local services and individual authorisations stay under R-DO-1.
- **Construction/property:** distinguish materials, contractor/professional services, actual special bases and property transfers. Category I acquisitions are excluded by the stated input-credit condition; do not generalise that rule to every vehicle or every construction invoice. The unproved building outcome remains held.
- **Ordinary expense matrix:** office supplies, commercial rent, professional fees and telecoms need actual taxable supply/rate and full credit conditions; housing rental, qualifying financial/insurance, electricity and water follow their actual exemptions. Food/medicines need product classification; cars and dinners need evidence, not blanket credit bans.

## When to refuse or refer

**R-DO-1 – free-zone/special regime.** Keep entity, authorisation, goods/import/inter-zone/local-service facts and special NCF claim. No general FTZ exemption or bespoke return is established here. **Check this point with one of our partner accountants.**

**R-DO-2 – withholding agent.** Preserve certificates, supplier/customer type, actual service and payment dates. Agent liability, rate/base, declarations and any related IR-17 process require the operative rule for that transaction; no blanket corporate 30%, individual-service 100%, government 100% or card 2%-of-gross instruction. **Check this point with one of our partner accountants.**

**Foreign services / SaaS / service exports.** Preserve provider residence, place/performance/use of the actual service, registration, treaty/territorial facts, invoice and any agent rules. GOOGLE, MICROSOFT, META or AWS does not establish automatic 18% self-assessment, matching credit or a net-zero transaction. No general foreign B2C collection/registration outcome or exported-service exemption is established. **Check this point with one of our partner accountants.**

**Historical unproved parameters.** The old RST threshold **DOP 8,698,516** is preserved solely as an unverified historical parameter, not an operative threshold or current admission rule. The old penalties **DOP 4,945 each month**, **10% first month plus 4% later months**, **1.73% interest**, **twice the tax**, and **2–6 years' imprisonment** are also non-usable historical assertions: the actual period, conduct, transition and authority were not established. Do not use them to calculate liability or substitute later-2026 website figures for a 2025/April 2026 event. The former blanket ITBIS/IR-17 tenth-day instruction is not usable either. **Check this point with one of our partner accountants.**

For any unresolved classification, keep the amount, evidence gap and affected return fields visible; do not manufacture a filing-ready figure. Official Spanish law controls over summaries. The sources above were read on 28 November 2026; Decreto 293-11's scanned pages and the large IT-1 instructivo were read visually. Form legends and modern summaries can contain older or later-period rules, so the operative law, actual period and documented taxpayer conditions control.

## Sources

- [Código Tributario, Title III](https://dgii.gov.do/legislacion/codigoTributario/Cdigo%20Tributario/Titulo3.pdf) – read 2026-11-28: Articles 335–355 and 357; scope, tax points, tariff/rate conditions, exemptions, credits, monthly filing and goods/free-zone boundary. Article 345 and DGII's continuing-rate guidance control the conditional rate footnote.
- [DGII ITBIS guidance](https://dgii.gov.do/cicloContribuyente/obligacionesTributarias/principalesImpuestos/Paginas/Itbis.aspx) – read 2026-11-28: continuing ordinary rate from 2016; its later-period penalty figures are not used for the original periods.
- [Decreto 293-11](https://dgii.gov.do/legislacion/decretos/Documents/2011/decreto293-11.pdf) – read 2026-11-28: scanned pages 4, 15–16, 18 and 20–21 visually, covering dependent employment, exempt-service conditions and all Article 18 input-credit requirements.
- [Norma 07-2018](https://dgii.gov.do/legislacion/normasGenerales/Documents/NG%20sobre%20Comprobantes%20Fiscales/Norma07-18.pdf) – read 2026-11-28: Articles 3–10, information-report scope, ordinary reporting deadline and pre-return validation.
- [DGII IT-1 instructivo](https://dgii.gov.do/publicacionesOficiales/bibliotecaVirtual/contribuyentes/itbis/Documents/Instructivo%20LLENADO%20IT-1%202020.pdf) – read 2026-11-28: actual form/Annex A box mapping visually on pages 10–12, 17–21 and 23; the 2020 title and repealed card-retention legend are expressly distinguished from operative law.
- [DGII Guide 5](https://dgii.gov.do/publicacionesOficiales/bibliotecaVirtual/contribuyentes/facturacion/Documents/Comprobantes%20Fiscales/1-Guia%205-Comprobantes%20Fiscales.pdf) – read 2026-11-28: specific paper/electronic fiscal-document roles and electronic validity; no individual mandate date inferred.
- [Aviso 24-23](https://dgii.gov.do/publicacionesOficiales/avisosInformativos/Documents/2023/24-23.pdf) – read 2026-11-28: repeal of Norma 08-04, distinction between invoiced base and taxes/tip, and mandatory-tip description.

Not yet confirmed: the individual e-CF mandate, FTZ/withholding, foreign/digital-service, special-package/incentive, RST, penalty, property/donation and sedan/dinner outcomes remain the explicit non-usable holds above; no later-2026 general update is asserted. Check this point with one of our partner accountants.

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. Latest version at [openaccountants.com](https://www.openaccountants.com).
