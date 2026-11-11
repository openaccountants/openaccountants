---
name: ar-vat-return
description: "Prepare and reconcile the Argentina monthly IVA return for 2026 through IVA Simple, Portal IVA and F.2051. Use for Responsable Inscripto filing, Libro ventas/compras, registration adjustments, retenciones/percepciones, technical/free balances, no-movement returns and payment evidence. The ordinary process applies to registered individuals and companies; specialist corporate transactions are routed. argentina-iva owns supply classification, rates, credit restrictions and imported-service computation. Produce a return-to-working-paper reconciliation for professional review, without inventing numbered boxes, current VEP codes or CUIT extensions."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ar-vat-return"
  jurisdiction: "AR"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Argentina: monthly IVA return 2026 v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Ordinary Responsables Inscriptos preparing monthly IVA under IVA Law art. 27 and RG 5705. The earlier Guide focused on self-employed general-regime individuals, including a lawful Monotributo transition; this workflow remains applicable to them and to ordinary companies. A company's form does not make F.2051 unavailable. Complex corporate transactions require their specialist analysis before filing.

**Quick answer:** for 2026 originals and amendments use **Portal IVA → F.2051**, Clave Fiscal level 3+, completing electronic registration and then determination. Validate prefilled data, reconcile the two distinct credit balances, preview and confirm the actual return, then separately pay/reconcile. Ending the registration module is not final return submission. Get CUIT/status, period, invoices, tax-point ledger, prior balances and suffered-tax certificates first.

This Guide is **Not yet approved**. It loads the VAT workflow base and returns a filing checklist, reconciliation, acknowledgement/payment evidence and unresolved items. [argentina-iva](argentina-iva.md) owns the computation and classification. [ar-monotributo](ar-monotributo.md) owns simplified-regime eligibility/exit; there is no old approximate service ceiling repeated as an IVA registration threshold.

Out of scope: agency withholding/perception computation, customs valuation, export-refund applications, construction/developer and agricultural elections, special financial instruments, complex transition-benefit calculations and provincial IIBB returns. Suffered national IVA retentions/perceptions are included. AGIP/ARBA collection is not national IVA merely because it appears on a bank statement.

## Rates, bands and thresholds

Load [IVA computation](argentina-iva.md) for the general/reduced/increased rate conditions, domestic exemptions and export treatment. Do not copy an old 2025 table into the return. The computation distinguishes books, food/medicinal resale, medical payer/provider, utilities/customer/premises, transport/distance, bank/insurance and goods/NCM conditions; no bank or supplier brand fixes a rate.

| Filing parameter | Rule and condition | Official source |
|---|---|---|
| Ordinary tax period | Monthly calendar period; specific annual-payment/deferral cases are separate elections, not permission to omit monthly records | IVA Law art. 27; https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 |
| Current return | F.2051 in Portal IVA, Clave Fiscal level 3 or above | RG 5705 art. 2; https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5705%7Co%3A9%7Ca%3A2025%7Cf%3A30%2F05%2F2025 |
| Mandatory periods | November 2025 onward, originals and amendments | RG 5705 art. 8; https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5705%7Co%3A9%7Ca%3A2025%7Cf%3A30%2F05%2F2025 |
| Suffered IVA perception timing | Applicable amended regimes permit the perception period or one of the next five periods; confirm particular regime/exception | RG 5750 and ARCA current guidance; https://www.arca.gob.ar/iva/iva-simple/retenciones-percepciones.asp |

## The base

### Build the legal working paper before using prefilled figures

Reconcile sales/purchases, credit/debit notes, advances, imports/exports and exemptions to the legally correct tax point. Output is not simply every deposit; input is not simply every amount labelled IVA. Use the computation Guide's art. 5 timing, arts. 10-12 base and credit checks, car/service/clothing restrictions, direct/common/private allocation and annual adjustment. Reduced-rate taxable sales remain taxable for allocation. Foreign B2B service IVA can need separate payment and next-period credit; do not place a same-month offset into ordinary output/input just to make it zero.

Document valid invoice/equivalent, issuer/buyer status and authority modality: electronic, authorised controller or permitted contingency/equivalent. A missing CAE is not conclusive if another lawful modality applies; unauthorised paper is not validated merely by appearance. C invoices do not create supplier IVA credit. Current invoice transparency means an IVA breakdown on a B/final-consumer invoice does not itself establish credit entitlement. The old “all paper invalid/all input Factura A” absolutes are replaced by the legal evidence and eligibility tests.

Direct taxable credit is allocated first, direct exempt/non-taxed and private costs excluded, and only inseparable common costs prorated. Keep the annual last-month adjustment. Personal costs are not deductible because the platform accepts a number. The car ceiling, restricted services and tenant utility-in-owner-name exception are in the owning computation Guide; do not replace them with a guessed business-use percentage.

### Keep technical and freely available balances separate

IVA Law art. 24 distinguishes credit generated by the tax computation from excess direct payments. Excess eligible input over output becomes technical credit against future IVA debit, subject to separately authorised recovery regimes. Eligible suffered IVA retentions/perceptions and direct-payment excess have their own freely available balance, subject to actual compensation/refund/transfer rules. Do not automatically offset that balance against any ARCA obligation or describe all negative IVA as cash refundable.

A positive technical determination is reduced by eligible suffered IVA amounts and actual admitted payments/balances, avoiding double use. Negative technical credit remains separately identified while direct-payment excess stays in its own account. Reconcile opening, changes and closing balances to the prior filed return and actual tax account. Nominal ARS controls do not imply automatic CPI revaluation or an unconditional no-expiry guarantee; the computation Guide explains the statutory index limitation.

### Suffered IVA amounts and timing

ARCA's current [retentions/perceptions instructions](https://www.arca.gob.ar/iva/iva-simple/retenciones-percepciones.asp), read with RG 5750, distinguish:

- Retentions generally belong to the period in which practiced. The prescribed exception permits inclusion in the first return whose due date follows the retention where the underlying tax point arose earlier. Match certificate, transaction and period before using it.
- Perceptions under the amended regimes may be used in their period or one of the five immediately following periods. The RG 1603 art. 8 previous-period exception requires the underlying operation to belong to that previous period and the perception to be practiced by that previous return's filing deadline. This is not permission to put every late certificate in any old year.
- Portal IVA displays SIRE/SICORE information. Validate it against real certificates; add/correct/import lawful omissions and prevent duplication. The portal is not proof the buyer applied the correct regime/rate.

Do not use the old universal 50%/100% withholding shortcut. The customer may be a designated agent, but current regime, invoice status and transaction determine the actual withheld amount. Acting as that agent is outside this recipient's return Guide. Bank IIBB, Ganancias or other levy entries must not be relabelled IVA.

## Deadlines and filing

### Select the legal period and current route

RG 5705 arts. 7-8 mandates F.2051 for November 2025 and later. June–October 2025 has the prescribed transitional options; May 2025 and earlier stays with the taxpayer's applicable historical procedure. F.731/F.810/F.2002 and SIAP are not the ordinary 2026 route. An amendment follows its actual period's rules, not automatically today's newest screen.

Ordinary schedule is the following month by CUIT ending: 0/1 day 18, 2/3 day 19, 4/5 day 20, 6/7 day 21, 8/9 day 22 (RG 4172 current annex V(a), imported by RG 5705 art. 5). Nonbusiness days/holidays move the affected and successive dates correlatively to following business days under RG 4172 art. 2. Check the actual month's calendar and any applicable extension before stating a calendar date. The old fixed “18th–23rd” range is not the controlling rule. A qualifying MiPyME payment deferral has its own eligibility/timing; do not infer that filing is deferred too.

### Follow the official current F.2051 sequence

The [official 14-step tutorial, Guide 518](https://serviciosweb.afip.gob.ar/genericos/guiasPasoPaso/VerGuia.aspx?id=518), was read through every public step and its displayed screenshots. It supports the field/card labels below; no live authenticated filing or numbered-box test was performed.

1. Sign in with CUIT/Clave Fiscal, open **Portal IVA**. Under **Nueva declaración jurada**, choose **Ingresar**, fiscal period, **Continuar**. Confirm taxpayer and original/amendment context before changing records.
2. Indicate actual movements and specific operations. If truly no operations, use **Sin movimientos → Registrar sin movimientos** for registration. Continue reviewing determination and opening balances; no activity does not establish that a prior balance or other adjustment vanishes.
3. Open **Libro ventas**. Review documents including cancellations; import missing records from ARCA, own file or **Agregar comprobante**. For ARCA import, choose carefully whether existing records are retained or replaced. Reconcile net sales, rates/output, exempt/non-taxed/export entries and credit notes. Then **Continuar a Libro compras**.
4. Review **Libro compras**, add permitted missing documents and import/customs records. Reconcile total and computable IVA to the working paper, including direct/common/private allocation and restricted credits. Software's **Asignación Directa / Prorrateo Global / CF Computable Global** options do not change art. 13. Then **Continuar a Ajustes**.
5. Under **Ajustes al Crédito Fiscal**, enter only supported applicable adjustments, including qualifying social-security credit/other concepts. Use **Guardar** and **Volver**. Under **Ajustes al Débito Fiscal**, review tax-point adjustments and the applicable debit/restitution cards. Do not enter a generic balancing plug.
6. Complete compulsory **Apertura de otros conceptos**, using **Editar/Guardar** for **Operaciones que generan Crédito Fiscal**, **Restitución de Crédito Fiscal**, **Débito Fiscal** and **Restitución de Débito Fiscal** as applicable. Reconcile every adjustment to evidence.
7. Choose **Vista previa** for registration. If correct, **Finalizar presentación y continuar**. This finalises registration and moves to the tax-determination module; it is not by itself submission of the completed F.2051.
8. Confirm the month's characteristics, including exports, special regimes, prior balances and prepayments. The choices enable the relevant determination cards. **Continuar**.
9. Reconcile these actual cards: **Débito y crédito fiscal**; **Exportaciones, operaciones exentas y regímenes especiales**; **Retenciones y percepciones**; **Pagos a cuenta**; **Administración de saldos**; **Determinación del impuesto**. Prefilled output/input comes from registration; prefilled technical/free balances come from the prior period. Check both separately. Correct/import suffered-tax data with attention to replacement options and legal timing.
10. Preview the actual F.2051, reconcile determination and payment/carry balances, then confirm **PRESENTAR**. Save the filed declaration, acknowledgement and actual confirmation/reference. If validation rejects a record, resolve it from the source evidence rather than altering the tax to silence the screen.
11. Arrange payment through the current authorised mechanism, including VEP where available, by the applicable due date. Retain bank/payment reference and reconcile settlement in the tax account. Filing receipt is not proof of payment. Generic live VEP numeric codes/current payment screens have not been independently confirmed here and must not be invented.
12. Carry technical/free balances independently into the next period; retain amendments, adjustment explanation and replaced-file history. Reconcile consecutive periods, not only the current month's bank movement.

The linked older Libro IVA Digital PDF describes historical Libro IVA/IVA Listo interfaces and was not used to invent current F.2051 buttons. The current specifications require taxable/exempt/non-taxed transactions, imports/exports and credit/debit notes; a foreign goods supplier invoice does not replace a customs despacho. Exact taxpayer-specific special flags/file layouts must be checked before bulk import.

## Penalties and interest

Current 2026 penalty amounts and interest percentages are unconfirmed; no nominal historic fine or guessed daily rate is provided. No-movement filing, payment, adjustment and certificate evidence remain separate obligations. Missing prefilled data does not excuse an incorrect return. Record the actual notice, tax/period, principal, source and payment; refer disputed input-credit, export-recovery or imported-service assessments before finalising an amendment.

## Cross-border points

The [IVA computation Guide](argentina-iva.md) owns imported-service base/timing, non-RI digital collection and export eligibility. Do not treat foreign-client service receipts as exports without effective foreign use, or foreign brand names as imports when a local entity supplied the service. Export input recovery under art. 43 is a separate claim procedure; the monthly return does not automatically trigger a refund.

Keep foreign-currency invoice, conversion date/rate evidence, bank proof, customs or E-invoice records as appropriate. Income-tax withholding/treaties/TP are separate and route to [cross-border](argentina-cross-border.md) and [TP](argentina-transfer-pricing.md). A service export does not automatically need a goods customs declaration.

## Two worked examples that recompute

### 1. File the ordinary determination and suffered amounts

Assume valid domestic taxable sales net1,000,000 and eligible purchases net600,000 at the general21% rate, correct period, no prior technical/free balance. Output210,000, input126,000, technical payable84,000. Valid correctly timed suffered IVA retention30,000 and perception10,000 reduce payment to44,000. Reconcile those figures through the output/input, suffered-tax and determination cards; save return acknowledgement and separate44,000 payment proof.

```oa-check
name: Monthly IVA determination and suffered taxes
inputs:
  net_sales: 1000000
  net_purchases: 600000
  retention: 30000
  perception: 10000
steps:
  - output_iva: net_sales * 0.21
  - input_iva: net_purchases * 0.21
  - technical_payable: output_iva - input_iva
  - balance_to_pay: technical_payable - retention - perception
expected:
  output_iva: 210000
  input_iva: 126000
  technical_payable: 84000
  balance_to_pay: 44000
```

### 2. Negative computation is not all freely available

Assume output100,000, eligible input120,000 and valid current suffered IVA retention8,000, no other amounts. Technical carryforward is20,000; direct-payment/free balance is8,000. No payment is due, but **Administración de saldos** must not show28,000 freely available. Both balances need separate next-period controls.

```oa-check
name: Separate technical and freely available balances
inputs:
  output_iva: 100000
  input_iva: 120000
  suffered_retention: 8000
steps:
  - technical_credit: max(0, input_iva - output_iva)
  - technical_payable: max(0, output_iva - input_iva)
  - free_balance: max(0, suffered_retention - technical_payable)
  - amount_to_pay: max(0, technical_payable - suffered_retention)
expected:
  technical_credit: 20000
  technical_payable: 0
  free_balance: 8000
  amount_to_pay: 0
```

The other old tests remain valid only with their stated legal assumptions: taxable sales500,000 at21% plus200,000 at10.5% give output126,000; eligible purchases400,000 at21% give84,000 and technical payable42,000. Output50,000/input80,000 leaves30,000 technical credit. For taxable800,000/exempt200,000,100,000 wholly inseparable common IVA permits estimated80,000; directly identifiable amounts must instead be allocated first, and annual actual-operation adjustment still applies. Do not make a reduced-rate sale exempt for this test.

## Ask the client first

1. CUIT/status, month, original/amended return, fiscal close, activity and actual due-date/election evidence.
2. Issued/received invoices/equivalents and authorisations, tax-point ledger, imports/exports and credit/debit notes.
3. Taxable/exempt/non-taxed operations, private/common/direct allocation, restricted assets/services and supporting exceptions.
4. Prior filed F.2051 and tax account, separately reconciled technical/free balances, paid amounts and adjustments.
5. Actual IVA retention/perception certificates with regime/date, all ARS/foreign-currency bank/processors and missing documents.
6. Current portal access/filing reference, notices, special flags and evidence for any deferred payment or specialist transaction.

Completion checklist: all required periods registered; source records validated; legal rates/taxpoints/credits established; direct allocation and annual adjustment checked; suffered taxes timed and not duplicated; technical/free balances separate; actual CUIT deadline checked; final F.2051 acknowledged; payment independently reconciled; next-period schedules saved. An unresolved eligibility/taxpoint/credit gap stops that component, not a request to guess a filing figure.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| Read for monthly period,credit/base/balances and documentary eligibility: IVA Law arts.5,10-13,24,27-28,37,39,41,43; quotation: "sólo deberá aplicarse a los débitos fiscales" | https://biblioteca.arca.gob.ar/search/query/dcp/TOR_C_020631_1997_03_26 | 2026-11-11 |
| Read for current F.2051 route,modules,validation,effective dates and calendar/payment: RG5705whole; quotation: "deberán ser validados por los contribuyentes" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5705%7Co%3A9%7Ca%3A2025%7Cf%3A30%2F05%2F2025 | 2026-11-11 |
| Read for ordinarycalendarannexV(a)-(b)andholidayruleart.2: RG4172andcurrentannex; quotation: "días hábiles inmediatos siguientes" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:4172%7Co:3%7Ca:2017%7Cf:22/12/2017 | 2026-11-11 |
| Read for IVA due-daygrid/currentannexsectionV: quotation: "0 y 1" | https://biblioteca.arca.gob.ar/search/query/adjunto.aspx?p=t:RAG%7Cn:4172%7Co:3%7Ca:2017%7Cd:RG4172_efecto4354.pdf | 2026-11-11 |
| Read for everycurrentF.2051tutorialstep1-14 anddisplayedscreens: Guide518; quotation: "Finalizar presentación y continuar";publicstepresponsesread,notjustshellpage | https://serviciosweb.afip.gob.ar/genericos/guiasPasoPaso/VerGuia.aspx?id=518 | 2026-11-11 |
| Read for registration specifications/recordscope andallocationoptions: ARCAIVA Simple; quotation: "SIN MOVIMIENTO" | https://www.arca.gob.ar/iva/iva-simple/especificaciones-especiales.asp | 2026-11-11 |
| Read for sufferingperiod/certificates/SIRE-SICORE: ARCAretentions/perceptions; quotation: "alguno de los 5 períodos fiscales inmediatos siguientes" | https://www.arca.gob.ar/iva/iva-simple/retenciones-percepciones.asp | 2026-11-11 |
| Read for current amendedregime perceptiontiming: RG 5750 operative articles and art.10: applies to original/amended returns presented from 1 September 2025; quotation: "que se presenten a partir del 1 de septiembre de 2025, inclusive" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5750%7Co:9%7Ca:2025%7Cf:26/08/2025 | 2026-11-11 |
| Read for prefilleddatavalidation andtwo modules: ARCAconfectionpage; quotation: "Todos los comprobantes, certificados o datos" | https://www.arca.gob.ar/iva/iva-simple/confeccion-declaracion.asp | 2026-11-11 |

Not yet confirmed: taxpayer-specific current-month dates/extensions and elections; live generic VEP numericcodes/payment screens; numberedboxes not shown by currenttutorial; currentpenalties/interest; detailedbulkimport/specialflags beyondordinarysequence. Old approximate Monotributothreshold, universal50%/100%agent rates, all-electronic/A-only credit, unlimited-credit-life and any-ARCA-tax offset claims are replaced by the owning Guide's verified conditional rules or explicit specialist/unconfirmed route, not repeated as facts.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ar-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ar-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
