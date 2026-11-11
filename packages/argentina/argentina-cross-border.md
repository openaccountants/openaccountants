---
name: argentina-cross-border
description: >
  Use this Guide for Argentina cross-border income tax in fiscal year 2026:
  beneficiarios del exterior, retenciones al exterior, residencia fiscal,
  convenios de doble imposicion, establecimiento permanente, tax residence,
  foreign tax credits and SIRE F.997. It covers resident worldwide versus
  non-resident Argentine-source taxation, ordinary outbound payment
  presumptions, withholding and gross-up, residence changes, permanent
  establishments, treaty documentation under RG 5855/2026 and foreign tax
  credit limitations. It prepares a documented tax-classification working
  paper for professional review. It does not give country-specific treaty
  rates, foreign exchange permissions, securities exemptions, indirect
  transfer computations, customs or a complete imported-service VAT return.
version: 0.2
jurisdiction: AR
category: cross-border
domain: tax
type: situation-rules
tax_year: 2026
last_updated: 2026-11-11
tier: 2
---

# Argentina: cross-border tax 2026 v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Argentine residents receiving foreign-source income and Argentine payers of Argentine-source income to foreign beneficiaries. It also screens inbound businesses for a permanent establishment (PE). This Guide is **Not yet approved**. Use it to classify a payment and document the domestic baseline, not to authorise a remittance or filing. Currency is ARS unless a transaction's original currency is expressly stated; examples assume no conversion difference.

**Quick answer:** establish residence, source, income category, PE and treaty entitlement before choosing a withholding rate. Ordinary foreign-beneficiary tax is 35% of the statutory presumed net income, not automatically 35% of the invoice. A treaty can change the result only if the actual treaty, protocol, effective date and relief conditions support it. For treaty-documentation payments from the RG 5855 application date in June 2026, a current foreign residence certificate and the new declaration are separate requirements.

Required initial facts: payment/accrual dates, supplier's legal form and residence, where the services/property are used or performed, the contract's tax-borne clause, ownership/PE facts, and any treaty certificate/declaration. Corporate net-income taxation is in [ar-corporate-income-tax](ar-corporate-income-tax.md), employee withholding in [argentina-payroll](argentina-payroll.md), self-employed income in [argentina-income-tax](argentina-income-tax.md) and related-party pricing in [argentina-transfer-pricing](argentina-transfer-pricing.md).

**Out of scope:** treaty-by-treaty rates and MLI matching, securities and digital-asset exemptions, indirect share transfers, shipping/aviation, foreign audiovisual/streaming exploitation and insurance special presumptions, CFC/look-through computations, foreign-exchange controls, customs, wealth tax and imported-service VAT computation. These are referrals, not an assumption of exemption. Do not conclude that emigrating erases an existing tax liability.

## Rates, bands and thresholds

### Domestic foreign-beneficiary baseline for 2026

Apply these only after determining that the receipt is Argentine-source, no separate statutory rule overrides it, and no proven treaty relief applies. LIG art. 104 presumptions generally do not permit contrary evidence, except the express actual-net option for its (g)/(h) categories. The effective rates below are arithmetic products, not additional statutory rates.

| Payment category | Presumed net share | Tax on presumed net | Effective share of gross | Conditions and official source |
|---|---|---|---|---|
| Qualifying technical assistance, engineering or consulting | 60% | 35% | 21% | LIG art. 104(a)(1): duly compliant technology-transfer contract, registered, actually performed, and service not obtainable locally in competent authority's judgment; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Other qualifying patent/right licences under technology-transfer contracts | 80% | 35% | 28% | Art. 104(a)(2), statutory technology-transfer compliance required; if a single contract mixes categories, use the higher presumption; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Qualifying copyright exploitation | 35% | 35% | 12.25% | Art. 104(b), national copyright registration and art. 26(j) conditions required: tax falls directly on author/heir; qualifying publication/performance/reproduction income; no commissioned work or work/service contract origin. The resident copyright exemption does not extend to foreign beneficiaries. It also covers the specified public/exempt-body foreign-artist contracts up to two months in the fiscal year; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Qualifying foreign credit/loan interest | 43% | 35% | 15.05% | Art. 104(c)(1): borrower governed by Ley 21.526 or supplier financing of imported depreciable movable goods excluding cars. For other art. 53 borrowers/individuals/estates, the foreign bank/finance lender must be central-bank/equivalent supervised and in a jurisdiction not low/no-tax, or one with a qualifying information-exchange agreement and no banking/securities/other secrecy defence. Specified bonds placed in investment-protection-reciprocity countries require Ley 23.576 registration within two years of issue; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Other foreign credit/loan interest within art. 104(c)(2) | 100% | 35% | 35% | Relevant art. 53 borrower/individual/estate where the lender fails the stated qualifying test; do not infer 15.05% from the label interest; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Temporary personal activity in Argentina | 70% | 35% | 24.5% | Art. 104(e), specified intellectual/technical/professional/artistic/sporting or other personal activity; stay not more than six months in fiscal year; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Lease of movable property by foreign resident | 40% | 35% | 14% | Art. 104(f), Argentine-source rental; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Rent of Argentine real property | 60% | 35% | 21% | Art. 104(g), excluding the 2026 qualifying individual/estate housing-rent exemption in art. 26(n) and Decreto 862 art. 83. It covers rent accruing from 1 January 2026, including qualifying furniture/accessories/services, only where the tenant exclusively uses the property as their unique family permanent home. Corporate lessors do not qualify for that individual/estate exemption. Actual-net option with admitted local expenses/deductions also exists; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Transfer of Argentine-situated/economically-used property by foreign enterprise | 50% | 35% | 17.5% | Art. 104(h), subject to special regimes for particular gains; actual-net option also exists; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Other Argentine-source gains not in preceding categories | 90% | 35% | 31.5% | Art. 104(i), residual category only; do not automatically classify every software/service contract here; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Dividends to foreign beneficiary | Separate gross dividend basis | 7% | 7% | Art. 97 as amended by Ley 27.630; profit-year/transitional provisions and any treaty need checking separately; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |

The 43% presumption for specified Argentine bank deposits is separately in LIG art. 104(d), but test the instrument's current exemption provisions before applying it. This Guide does not compute financial-instrument exemptions.

### Residence, PE and treaty-documentation time tests

| Rule | Time test | Qualification and official source |
|---|---|---|
| Foreign individual becoming resident without permanent immigration residence | Twelve months' authorised temporary presence | LIG art. 116(b), with permitted temporary absences and exception where facts show no intention of habitual permanence; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Resident loss through absence, where permanent foreign residence was not acquired sooner | Twelve continuous months abroad | Art. 117, temporary-presence and habitual-intent exceptions apply; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Temporary absences/presences in residence tests | No more than 90 days, consecutive or not, in each twelve-month period | Decreto 862 arts. 281 and 283; https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06 |
| Domestic-law construction PE | More than six months | LIG art. 22; linked subcontractor and identical/similar linked activities aggregate as prescribed; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Domestic-law service PE | More than six months in any twelve months | Art. 22, services in Argentina through own/contracted personnel and linked identical/similar activities aggregate; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Foreign tax credit carryforward | Five following fiscal years | LIG art. 175, only against tax on foreign-source net income, then expires; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Treaty residence certificate with no stated validity period | Twelve months after issue | RG 5855 art. 2; a stated validity period governs if supplied; https://biblioteca.arca.gob.ar/dcp/REAG01005855_2026_06_02 |
| New treaty documentary procedure | Payments from fifteen calendar days after publication on 3 June 2026 | RG 5855 art. 13; old declarations retain effect for their validity period if facts unchanged, art. 12; https://biblioteca.arca.gob.ar/dcp/REAG01005855_2026_06_02 |

## The base

### 1. Residence and source

[LIG art. 1](https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05) taxes residents on worldwide income and permits the limited foreign tax credit; non-residents are taxed on Argentine-source income. Art. 5 generally looks to property situated/placed/economically used in Argentina, activities carried on there, and events there. The parties' nationality, residence or place of contracting does not displace that source test. Under art. 9, an ordinary foreign seller's gain from a simple import into Argentina is foreign-source; do not subject every imported-goods invoice to residual service withholding. Art. 13 specifically treats foreign-performed technical/financial/other advice and remuneration of directors of Argentine entities acting abroad as Argentine-source. Do not equate foreign invoice address with foreign source.

Individuals of Argentine nationality generally are resident unless they lost residence under art. 117. Current art. 116, amended by Ley 27.802 art. 194, excepts citizenship obtained through qualifying investment naturalisation: that naturalisation alone does not create tax residence, and the foreign-individual rules remain applicable. Existing permanent residents remain residents. Foreign individuals can acquire residence through permanent immigration status or the temporary-presence route. Under art. 116, the latter foreign-individual acquisition takes effect from the start of the month immediately following the qualifying month. Under art. 117, loss takes effect on the first day of the month immediately following acquisition of permanent residence abroad or completion of the qualifying absence. Test art. 118 official-service exception, art. 122 dual-residence facts, and art. 123 special categories. In particular, art. 123(c) excludes foreign individuals whose duly substantiated employment assignment requires a stay no longer than five years, and accompanying family members who were not already resident; their Argentine-source income nevertheless follows the rules applicable to residents under art. 123's final paragraph. Do not subject such workers automatically to the temporary-visitor gross presumption. Decreto 862 art. 281 requires a claim of no habitual-intent under the temporary-presence acquisition test at least thirty days before completing the twelve months; that claim can be exercised only once. For temporary absence, count from the day after exit through re-entry inclusive (Decreto 862 art. 281); temporary presence counts from the day after entry through exit inclusive (art. 283). Dual-residence time comparison uses the calendar year (art. 284). These are domestic rules; a treaty residence tie-breaker must be read separately.

Art. 122 tests a continuing Argentine permanent home, then centre of vital interests where both homes exist, habitual abode, and nationality in the specified fallback case. A residence card alone is insufficient where facts show continuing domestic residence. Under arts. 119-121 keep the evidence of foreign residence/absence, settle the relevant resident-period income, and communicate the change to withholding agents. Foreign-beneficiary treatment starts when loss becomes effective. If earlier withholding was omitted before notification, art. 120 calls for recovery from future payments or notification of inability to recover.

### 2. Screen for a PE

[LIG art. 22](https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05) covers a fixed business place and examples such as a branch, office, factory, workshop or extraction site. The construction and service time tests above are additional routes, not exemptions for a fixed place that already qualifies. Listed storage/display/purchasing/information or other activities are excluded only if auxiliary or preparatory, including the combined activity.

A dependent person can create a PE through habitual contracting/significant contract-closing role. Art. 22 also lists alternatives: keeping stock for regular delivery, assuming the foreign principal's risks, detailed instructions/general control, activities economically belonging to that principal, or remuneration irrespective of activity outcome. Contract-signing authority is not indispensable to all these routes. An ordinary independent intermediary exception requires real independence and normal arm's length dealings; working exclusively/principally for one foreign enterprise or its related enterprises defeats that exception as specified. If a PE exists, calculate attributable business profits under the corporate rules; do not treat all PE receipts as final gross withholding merely because the owner is abroad. Treaties may change the PE definition and profit-allocation result.

### 3. Classify and compute outbound withholding

Under [LIG arts. 102-104](https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05), identify a payment to a foreign beneficiary, including payment through a representative or an in-country receipt without proof of stable residence. Apply the category's presumed net share, then 35%, unless a special rule such as dividends applies. Payment has the extended art. 24 meaning, so a relevant credit/disposal can trigger the rule before a bank transfer. Keep an explicit source/category memo and test treaty relief separately.

Decreto 862 arts. 263-267 require the technology-transfer authority certificate and INPI registration. Local unavailability is assessed at registration, and the services must actually have been performed by payment; a denied certificate routes the payment to art. 104(i). The artist two-month test aggregates the qualifying contracts in the year (art. 268). A temporary personal activity lasting more than six months instead uses actual net income under LIG art. 23 and an annual return under Decreto 862 art. 270, not the residual presumption. Qualifying financial leases have special conditions under art. 269 and need separate review.

For art. 104(g)/(h), compare the presumed-net route with actual net income only if the necessary local expenses and deductions have been expressly admitted by ARCA. Do not substitute an unsupported spreadsheet of costs. Other art. 104 presumptions cannot simply be replaced by actual profit.

Where a third party bears the tax, [Decreto 862 art. 227](https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06) adds that tax to the gain. For a flat effective gross withholding fraction r and promised net amount N, gross = N/(1-r), tax = gross-N. This formula presupposes a single applicable category and no statutory gross-up exception. Art. 227 excludes gross-up for foreign financing interest destined for industry, extractive operations and primary production; examine the use of funds before grossing up any loan interest.

### 4. Foreign tax credit

[LIG arts. 165-176](https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05) permit qualifying analogous national foreign income taxes actually paid, supported by receipts. The tax must satisfy art. 166's analogous-tax test; a foreign turnover tax or VAT is not automatically creditable. The credit is limited to Argentine tax attributable to foreign-source gains; excess cannot offset domestic-source tax. Under art. 167, except an express different rule, convert foreign tax at BNA buyer exchange rate at the close of its actual payment day and credit it in that payment fiscal year. Under art. 171, where the foreign return assesses global net income, allocate its tax by foreign-country gross gains taxable in Argentina divided by total gross gains in that foreign return. Exclude foreign tax compensated by its own foreign-credit relief; separately assess the underlying third-country tax. Keep source allocation, conversion, returns, receipts, refunds and carryforward schedules. Art. 175 allows excess for five following fiscal years. Additional foreign tax on earlier years enters the payment fiscal year under art. 172. A foreign-recognised refund/reduction of earlier credits reduces credit in the recognition year using the original conversion rate (art. 173); any application of that recognised amount to foreign tax is separately considered. Foreign tax recoveries also reduce credit under art. 176. Indirect corporate/PE credits, transparent entities and CFC attribution require separate review of arts. 168-174, not an automatic credit for every tax paid anywhere in the group.

## Deadlines and filing

### Treaty relief at payment

Use [RG 5855 arts. 1-8 and 12-13](https://biblioteca.arca.gob.ar/dcp/REAG01005855_2026_06_02) for payments from 18 June 2026 (fifteen calendar days after publication on 3 June), including treaty outcomes with no withholding. Earlier payments remain under RG 3497/2228 and need the historic procedure, rather than retroactive application of the new checklist:

1. Read the actual treaty/protocol and effective application dates from the [ARCA official treaty inventory](https://www.arca.gob.ar/convenios-internacionales/materia/convenios-para-evitar-la-doble-imposicion.asp). Establish beneficiary status, residence, income article, PE connection and anti-abuse conditions before asserting relief. Signature or parliamentary approval alone is not proof the relief applies to this payment.
2. Obtain the beneficiary's valid fiscal-residence certificate issued by the foreign competent authority for the relevant period **before payment/withholding**, or before the first of periodic payments under the same instrument. If it has no validity term, the twelve-month rule applies. Apostille or Argentine consular legalisation is required unless authenticity can be corroborated through the authority's official electronic verification system.
3. Obtain the separate signed [RG 5855 Annex declaration](https://biblioteca.afip.gob.ar/search/query/adjunto.aspx?p=t%3ARAG%7Cn%3A5855%7Co%3A9%7Ca%3A2026%7Cd%3Aanexo_7669897_1.pdf). Complete fields (a)-(h): beneficiary name, foreign tax number, fiscal address, local representative identification if any, contract/transaction description, service/operation start and term, income type, and the exact treaty article/paragraph. The declarant confirms all treaty eligibility conditions.
4. Retain certificate, declaration, contract/invoices and the relief working paper. If payer and withholding agent differ, give the latter the required copies before withholding/payment; it retains them too. Supply legalised public-translator Spanish translations on ARCA request where documents are in another language.
5. Renew the certificate before the first payment after expiry or changed certificate facts; obtain a new declaration when its facts change. Without the current certificate, apply domestic withholding under art. 7, not the unsubstantiated treaty rate. Old-regime declarations continue only for their validity period and unchanged facts under art. 12.
6. For excess withholding after late documentation, art. 8 permits SIRE cancellation/modification only after the agent checks requirements and refunds the excess to the beneficiary. Where refund is not feasible, the specified representative or payer who contractually bore tax and suffered loss can pursue the Ley 11.683 recovery route. Do not quietly net an unapproved refund from another supplier's payment.

### SIRE certificate, monthly return and payment

ARCA's [SIRE F.997 manual](https://www.arca.gob.ar/ClaveFiscal/manuales/documentos/dit.mis_aplicaciones_web.CF_MU_MAW_F997-1.0.0.pdf), section 3, identifies foreign-beneficiary income tax as **tax 218**, certificates **F.2003**, and monthly return **F.997**. The manual is a legacy operational manual dated 2016 still published by ARCA, so its screenshots are not evidence of a live 2026 UI. Current applicability is corroborated by RG 5855 art. 8's SIRE requirement.

Enter the certificate's beneficiary, country, category, payment/base and withholding details in SIRE; deliver the certificate and reconcile the monthly set to the ledger. In **Mis Aplicaciones Web**, the manual uses **Buscar**, then **Editar**, to open the automatically generated period/sequence. Check **Determinación del Saldo** and **Totales por Quincena por Régimen**. **Grabar** saves; **Presentar** submits and produces **Acuse de Recibo** and **Tiquet de la Presentación**. Retain them and the VEP payment receipt. A draft saved with Grabar is not a filed return. Rectifications have separate selections in that manual. ARCA's current applications page requires a monthly **SIN MOVIMIENTO** return when there are no reportable operations, without first issuing a certificate: https://www.arca.gob.ar/sire/liquidacion/aplicaciones-web.asp .

ARCA's current SIRE payment page specifies foreign-beneficiary balance VEP codes 218 / 19 / 19 and payment-on-account codes 218 / 27 / 27 (tax / concept / subconcept): https://www.arca.gob.ar/sire/liquidacion/pagos.asp . The applicable current CUIT due-date grid and live portal field layout have not been confirmed here. Obtain the official calendar and payment instructions before remitting or paying; do not reuse payroll SICORE or F.931 codes for foreign-beneficiary SIRE.

## Penalties and interest

RG 5855 art. 10 refers documentary non-compliance to Ley 11.683. Missing a valid certificate also denies treaty treatment at source under art. 7, independently of penalties. Filing default, failure to withhold, late deposit and an unsupported refund are distinct issues. This Guide has not confirmed the current penalty amounts, interest periods or rates and gives none. A source/treaty uncertainty must be resolved or treated under the domestic rules before payment, not covered with an invented rate.

## Cross-border points

Foreign exchange permission and the tax result are separate: a permitted currency payment does not establish treaty exemption, and a withholding obligation does not establish exchange-control permission. Imported services can also produce IVA obligations; use the relevant [Argentina IVA Guide](argentina-iva.md) and identify taxable use in Argentina before treating the income-tax withholding as the complete tax cost.

Group dealings also need the [Argentina transfer pricing Guide](argentina-transfer-pricing.md). A treaty rate does not validate the contract price or establish deductibility. Related-party financial-interest limitation and technical-advice deduction caps belong in the corporate computation. Treaty-country rate matrices and MLI matching are deliberately outside this Guide: the actual article and effective instruments must be examined for the counterparty and payment date.

## Two worked examples that recompute

### 1. Qualifying technical assistance or residual service?

Assume ARS 1,000,000 gross Argentine-source payment to a foreign provider, no PE, no treaty relief and no payer-borne tax. If art. 104(a)(1)'s registration, technology-transfer, unavailable-locally and actual-service conditions are all proven, presumed net is 600,000 and tax 210,000. If that category fails and the properly classified receipt falls in residual art. 104(i), presumed net is 900,000 and tax 315,000. The difference is 105,000. Failure of a condition does not automatically establish the residual category; review all categories before selecting it. The 21% result is not a universal consultancy rate.

```oa-check
name: Technical-assistance classification decision
inputs:
  gross_payment: 1000000
steps:
  - qualifying_net: gross_payment * 0.60
  - qualifying_tax: qualifying_net * 0.35
  - residual_net: gross_payment * 0.90
  - residual_tax: residual_net * 0.35
  - tax_difference: residual_tax - qualifying_tax
expected:
  qualifying_net: 600000
  qualifying_tax: 210000
  residual_net: 900000
  residual_tax: 315000
  tax_difference: 105000
```

### 2. Payer promises net rent for movable property

Assume a foreign lessor's ordinary Argentine-source movable-property rent, domestic art. 104(f) applies, no treaty, and payer promises the lessor ARS 1,000,000 net. The effective gross withholding fraction is 40% × 35% = 14%. Gross-up under Decreto 862 art. 227 gives gross 1,162,790.70 and tax 162,790.70. Withholding 14% of the promised net would pay only 140,000 and understate the gross-up. This is a lease, not financing interest within the gross-up exception.

```oa-check
name: Payer-borne tax on movable-property rent
inputs:
  promised_net: 1000000
steps:
  - effective_rate: 0.40 * 0.35
  - gross_payment: promised_net / (1 - effective_rate)
  - withholding: gross_payment * effective_rate
  - received_net: gross_payment - withholding
expected:
  gross_payment: 1162790.70
  withholding: 162790.70
  received_net: 1000000
```

## Ask the client first

1. Residence evidence, nationality/legal form, immigration changes, days and homes in each country, effective residence-loss dates.
2. Contract, invoice, service/property location, actual work/usage, income type, payment/credit dates and tax-borne clause.
3. PE facts: premises, people, service/construction duration, related subcontractors, contracting authority and agents.
4. Treaty/protocol claimed, beneficiary eligibility, valid certificate, verification/legalisation, declaration and changes in facts.
5. Technology-transfer/copyright registrations and special-category evidence; financing lender status and use of funds.
6. Foreign tax assessments/receipts/refunds, credit carryforwards, SIRE certificates, prior returns and payment acknowledgements.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| Read for scope/source and withholding: LIG arts. 1, 5-9, 13-14, 22, 26(j)/(n), 97, 102-104; quotation: "el TREINTA Y CINCO POR CIENTO (35 %) de tales beneficios" | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for residence and foreign credits: LIG arts. 116-124, 165-176; quotations: "DOCE (12) meses", "CINCO (5) años fiscales inmediatos siguientes" | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for gross-up and temporary visits: Decreto 862 arts. 83, 227, 263-271, 281, 283-284; quotation: "la ganancia se acrecentará en el importe abonado" | https://biblioteca.arca.gob.ar/dcp/DEC_C_000862_2019_12_06 | 2026-11-11 |
| Read for 2026 treaty relief process: RG 5855 arts. 1-14; quotations: "certificado de residencia fiscal vigente", "QUINCE (15) días corridos" | https://biblioteca.arca.gob.ar/dcp/REAG01005855_2026_06_02 | 2026-11-11 |
| Read for required fields: RG 5855 Annex, Spanish declaration fields (a)-(h) and signature; quotation: "Encuadre de la renta en el artículo" | https://biblioteca.afip.gob.ar/search/query/adjunto.aspx?p=t%3ARAG%7Cn%3A5855%7Co%3A9%7Ca%3A2026%7Cd%3Aanexo_7669897_1.pdf | 2026-11-11 |
| Read for official treaty-document routing: ARCA agreement table and protocol links; no country rate derived from this inventory | https://www.arca.gob.ar/convenios-internacionales/materia/convenios-para-evitar-la-doble-imposicion.asp | 2026-11-11 |
| Read for no-movement obligation: ARCA Mis Aplicaciones Web SIRE page; quotation: "SIN MOVIMIENTO" | https://www.arca.gob.ar/sire/liquidacion/aplicaciones-web.asp | 2026-11-11 |
| Read for payment codes: ARCA SIRE foreign-beneficiary tax table, balance and payment-on-account rows; quotation: "Saldo de la declaración jurada" | https://www.arca.gob.ar/sire/liquidacion/pagos.asp | 2026-11-11 |
| Read for filing fields: ARCA F.997 manual v1.0.0, section 3 and subsections 3.1-3.3; legacy document dated 24 February 2016; quotation: "Impuesto 218 - Impuesto a las Ganancias - Beneficiarios del Exterior" | https://www.arca.gob.ar/ClaveFiscal/manuales/documentos/dit.mis_aplicaciones_web.CF_MU_MAW_F997-1.0.0.pdf | 2026-11-11 |

Not yet confirmed: current SIRE CUIT calendar and live UI fields; 2026 penalties and interest; country-specific treaty/protocol/MLI rates/effective dates; security/indirect-transfer exemptions and computations; operational ARCA residence-deregistration filing steps; full pre-18-June treaty-documentation workflow under RG 3497/2228. Those omissions are not exemptions. Special financial/transport/insurance regimes, CFC/indirect credits, exchange controls and imported-service IVA computation are out of scope.
