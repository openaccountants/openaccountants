---
name: mx-cfdi
version: 2.3
description: Use this skill whenever asked about Mexican CFDI electronic invoicing. Trigger on phrases like "CFDI", "factura electronica", "PAC", "complemento de pago", "comprobante fiscal", "SAT factura", "CFDI 4.0", "timbrado", "cancelacion CFDI", or any question about issuing, receiving, or managing electronic invoices in Mexico. Covers CFDI 4.0 structure, PAC certification, complemento de pago, uso de CFDI, cancellation rules, and SAT obligations. ALWAYS read this skill before touching any Mexican CFDI work.
jurisdiction: MX
tax_year: 2026
last_updated: 2026-11-27
type: filing-howto
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mexico — CFDI electronic invoicing (2026)

## Who this applies to

For Mexican issuers preparing ordinary CFDI invoices, payment complements and cancellations. Use CFDI 4.0: SAT identifies it as the only valid version since 1 April 2023. [SAT format page](https://wwwmat.sat.gob.mx/consultas/35025/formato-de-factura-electronica-%28anexo-20%29).

**Required inputs:** issuer and recipient RFC, registered name, fiscal regime and postal code; transaction and tax treatment; actual payment dates, amounts, currency and method; issuing channel and certificate; and, for cancellation, original UUID, related documents, reason and replacement UUID. Obtain the data from the records already available before asking for anything missing. Do not make delivery of a Constancia de Situación Fiscal a condition of issuing an invoice (CFF art. 83 IX).

## Rates, bands and thresholds

| Item | Applicable rule | Official source |
| --- | --- | --- |
| Payment complement | Issue by the fifth natural day of the month immediately following receipt; one per payment or one covering the month's payments from the same recipient | [RMF 2026, 2.7.1.32](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf) |
| Cancellation up to MXN 1,000 | No acceptance under this amount exception, except payment-complement CFDIs and the fuel cases identified in rule 2.7.1.34, third paragraph; other exceptions must be assessed separately | [RMF 2026, 2.7.1.35 I](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf) |
| Acceptance response | Three business days following receipt of the request; silence normally accepts, subject to the express fuel exclusions below | [RMF 2026, 2.7.1.34](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf), [CFF art. 12](https://dgesui.ses.sep.gob.mx/sites/default/files/2026-05/CFF.pdf) |
| Certification interval | PAC validates that generation-to-certification does not exceed 72 hours, using LugarExpedicion's time zone; this is not a general extension of the transaction's issuance deadline | [RMF 2026, 2.7.2.9 I and final paragraphs](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf) |

## The taxable base

### Ordinary invoice fields

Use the [Anexo 20, I.A and I.F technical standard](https://dof.gob.mx/2022/SHCP/SHCP_130122.pdf), together with [Anexo 29 for 2026, VI.1](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo_29_RMF2026-09012026.pdf). The table is a field checklist, not a complete XML schema: certificate, signature, concepts, taxes and applicable complements must also validate.

| Field | Entry or condition |
| --- | --- |
| Version | 4.0 |
| Serie / Folio | Optional internal identifiers; original syntax illustrations A / 1001 |
| Fecha | Actual local issuance date and time; the original 2025-06-15T10:30:00 is a syntax illustration, not a date to put on a current invoice |
| FormaPago / MetodoPago | For ordinary income invoices: full payment received at or before invoicing means PUE and the actual payment form; unpaid or instalment/deferred payment means PPD and FormaPago 99. The original transfer illustration is 03; the old 01 cash illustration is unconfirmed and non-usable pending the catalogue check below |
| SubTotal | Sum of concept amounts before discounts and tax; original illustration 10000.00 |
| Moneda / TipoCambio | Currency code, such as MXN or USD; exchange rate required when currency is neither MXN nor XXX. For MXN it may be omitted, or must be 1 if included; for XXX omit it. The foreign-currency rate expresses pesos per currency unit |
| Total | SubTotal minus discounts plus transferred taxes and other applicable contributions, minus retained taxes; not simply SubTotal plus IVA |
| TipoDeComprobante | I (income), E (credit/egreso), T (transfer/traslado), P (payment), N (payroll). P requires the payment complement; N requires the payroll complement. Do not apply ordinary-invoice payment fields to T or P |
| Exportacion | Required current catalogue value. 01 means No aplica. Do not infer 02 from a foreign customer's address: its technical validation requires the foreign-trade complement; Anexo 29 also recognises 04, with or without that complement. Selection for service exports, and the old 02/03 definitive/temporary mapping, remain on hold below |
| LugarExpedicion | Postal code of the issuing establishment; original illustration 06600 |
| Emisor | Actual issuer RFC, registered name and applicable RegimenFiscal; XAXX010101000 is a generic recipient code, not an ordinary issuer identity |
| Receptor | RFC, registered name, DomicilioFiscalReceptor, RegimenFiscalReceptor and UsoCFDI. Original domestic illustrations: postal code 01000, regime 601 and use G03; do not copy illustrative data into a real invoice |
| Conceptos / taxes | Record the goods/services, product and unit keys, quantity, description, unit value, amount, ObjetoImp and applicable taxes and complements under the standard |

For registered parties, match the name to SAT's registered data in uppercase, respecting numbers, spaces and punctuation; EC1 (PAC rejects the recipient's name) requires correcting the data against the registration record, not inventing accent or abbreviation rules. [SAT name instructions](https://www.sat.gob.mx/minisitio/Factura/documentos/Infografia_FacturaElectronica_NombreReceptor.pdf).

### UsoCFDI codes

The selected use must fit both the recipient's person type and fiscal regime under Anexo 20 I.F. A description alone does not establish deductibility.

| Code | Description / disposition | Official source |
| --- | --- | --- |
| G01 | Original merchandise-purchase lookup: non-usable pending current catalogue confirmation. Check this point with one of our partner accountants. | [SAT technical entry point](https://wwwmat.sat.gob.mx/consultas/35025/formato-de-factura-electronica-%28anexo-20%29) |
| G03 | Gastos en general; select only where compatible with the recipient's regime | [SAT CFDI guide, UsoCFDI](https://www.sat.gob.mx/minisitio/Factura/documentos/Guia_llenadoCFDI_DPA.pdf) |
| I01 | Original construction lookup: non-usable pending current catalogue confirmation. Check this point with one of our partner accountants. | [SAT technical entry point](https://wwwmat.sat.gob.mx/consultas/35025/formato-de-factura-electronica-%28anexo-20%29) |
| D01 | Honorarios médicos, dentales y gastos hospitalarios; no automatic deduction conclusion | [SAT personal deductions](https://www.sat.gob.mx/minisitio/DeduccionesPersonales/gastos_medicos.html) |
| D04 | Donativos; the donor's person type and current catalogue matter; SAT's donation FAQ distinguishes individual D04 from corporate G03 | [SAT donation CFDI FAQ](https://www.sat.gob.mx/minisitio/DonatariasAutorizadas/documentos/preguntasfrecuentes/CFDI.pdf) |
| S01 | Sin efectos fiscales; used for the foreign generic RFC in SAT's guide | [SAT CFDI guide, UsoCFDI](https://www.sat.gob.mx/minisitio/Factura/documentos/Guia_llenadoCFDI_DPA.pdf) |
| CP01 | Payment-complement use | [SAT Pagos 2.0 standard, section 4](https://wwwmat.sat.gob.mx/cs/Satellite?blobcol=urldata&blobkey=id&blobtable=MungoBlobs&blobwhere=1461175070885&ssbinary=true) |

### Fiscal-regime code lookup

These are descriptions, not a test of regime eligibility. Use the regime actually applicable to the transaction and validate person type/current catalogue as required by Anexo 20 I.F. Source for every description: [SAT fiscal-regime table](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen).

| Code | Description | Official source |
| --- | --- | --- |
| 601 | General de Ley Personas Morales | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 603 | Personas Morales con Fines no Lucrativos | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 605 | Sueldos y Salarios e Ingresos Asimilados a Salarios | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 606 | Arrendamiento | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 607 | Enajenación o Adquisición de Bienes | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 608 | Demás ingresos | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 610 | Residentes en el Extranjero sin Establecimiento Permanente en México | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 612 | Personas Físicas con Actividades Empresariales y Profesionales | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 616 | Sin obligaciones fiscales | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 621 | Incorporación Fiscal; listing the code does not establish current eligibility | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 625 | Actividades Empresariales con Ingresos a través de Plataformas Tecnológicas; not RESICO | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |
| 626 | Régimen Simplificado de Confianza; not a code reserved to companies | [SAT](https://www.cloudb.sat.gob.mx/datos_fiscales/regimen) |

EC5 (RESICO freelancer): use the actual RESICO code above; do not assume RESICO removes invoicing duties or determines IVA treatment. Verify the transaction's tax treatment separately. [CFF art. 29](https://dgesui.ses.sep.gob.mx/sites/default/files/2026-05/CFF.pdf).

## Deadlines and filing

### Issue and certify

1. Choose SAT's issuing tools or an authorised certification provider (PAC/PCCFDI). A paid PAC is not mandatory for every issuer. Generally obtain a valid e.firma and CSD under CFF art. 29 I–II. Individuals may substitute their e.firma for CSD only through “Genera tu factura” and “Portal de factura electrónica” under RMF 2.2.8; certificate restrictions still apply.
2. Enter the actual transaction and party data above; generate/sign the XML, then obtain certification under RMF 2.7.2.9. A successful certification returns the fiscal folio, certification date/time and digital seals. A rejected XML is not a certified invoice.
3. Deliver or make available the certified XML; supply the printed representation when requested. Keep the XML and certification/rejection records. [CFF arts. 29 IV–VI, 29 Bis](https://dgesui.ses.sep.gob.mx/sites/default/files/2026-05/CFF.pdf), [RMF 2026, 2.2.8 and 2.7.2.9](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

### Receive payment

Under RMF 2.7.1.32, issue the invoice for the full operation, then record partial/deferred payments with the payment complement. Monthly grouping is permitted only for the same recipient. Record the actual payment date, form, amount and currency, related UUID, instalment number, prior balance, amount applied and remaining balance, plus the required tax details. [RMF 2026](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf), [SAT Pagos 2.0, sections 1 and 4](https://wwwmat.sat.gob.mx/cs/Satellite?blobcol=urldata&blobkey=id&blobtable=MungoBlobs&blobwhere=1461175070885&ssbinary=true).

For an ordinary payment CFDI: TipoDeComprobante P, SubTotal and Total zero, Moneda XXX, Exportacion 01 and UsoCFDI CP01; omit the main-body FormaPago, MetodoPago and TipoCambio. The payment currency, amount and payment form belong in the complement. Zero in the main body does not mean a zero payment. Follow the full Pagos 2.0 schema, including its concept and tax validations.

EC3 (PPD invoice issued 4 months ago, paid, complement missing): issue the missing complement using the actual payment date, preserve the late-issuance evidence and obtain advice on the breach. Do not claim the invoice automatically remains “open” in SAT or that late issuance removes penalties. Check this point with one of our partner accountants.

### Cancel or replace

Use the [SAT cancellation portal or provider](https://www.sat.gob.mx/minisitio/Factura/cancela_procesocancelacion.htm). Identify the original UUID and reason; income cancellations must have documentary justification. Under current CFF art. 29-A, cancel no later than the month in which the annual ISR return for the issuance year is due, subject to the acceptance rules. Before relying on that outer limit for a special-regime or global invoice, check its specific rule. [CFF art. 29-A](https://dgesui.ses.sep.gob.mx/sites/default/files/2026-05/CFF.pdf).

| Reason | SAT description |
| --- | --- |
| 01 | Comprobantes emitidos con errores con relación; state the replacement's fiscal folio |
| 02 | Comprobantes emitidos con errores sin relación |
| 03 | No se llevó a cabo la operación |
| 04 | Operación nominativa relacionada en una factura global |

All reason descriptions: [SAT cancellation process](https://www.sat.gob.mx/minisitio/Factura/cancela_procesocancelacion.htm). If other CFDIs relate to the original, resolve their prior cancellation as required by RMF 2.7.1.34; do not cancel the wrong UUID or leave payments unaccounted for. If the operation continues, the replacement must be related to the cancelled invoice.

Where acceptance is required, the recipient responds within three business days following receipt; silence ordinarily counts as acceptance. RMF 2.7.1.34 excludes its specified hydrocarbon/petroleum concept-complement CFDIs and specified fuel Carta Porte income CFDIs from acceptance by silence. A rejected request is not a cancellation. Preserve and check the final status rather than equating “request received” with “cancelled”. [RMF 2026, 2.7.1.34](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf), [Anexo 29, November revision, VI.3](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/SegundaModificacion_Anexo29_DOF-06112026.pdf).

**No-acceptance matrix — RMF 2.7.1.35.** Apply its conditions, not a blanket amount test. The final paragraph excludes hydrocarbon/petroleum income operations under rule 2.6.1.1 from the facility except the public-in-general and foreign-resident cases (VII/VIII).

| Case | Condition / limitation |
| --- | --- |
| Small amount | Total up to MXN 1,000, excluding REP/payment complements and the rule 2.7.1.34 third-paragraph cases |
| Payroll / egreso / traslado | Payroll qualifies; egreso excludes the rule 2.7.1.34 third-paragraph cases; traslado excludes the specified fuel Carta Porte cases under 2.7.7.1.6 |
| RIF / withholding-information CFDI | Income CFDIs to continuing RIF taxpayers under the cited transitional rules; CFDIs for retentions and payment information are a distinct category from REP |
| General public / foreign resident | Must meet rule 2.7.1.21 / 2.7.1.23 respectively; “export” alone is not the exception |
| Prompt cancellation | Within the business day following issuance |
| Acquirer / primary sector | Only the specified section 2.7.3 / rule 2.7.4.1 transactions using the stated PCECFDI or PCGCFDISP route; not transfers between one's own accounts generally |
| Financial system / government | Members of the financial system; the Federation for derechos, productos y aprovechamientos, not all public agencies' invoices |

Source for every matrix row: [RMF 2026, 2.7.1.35 I–XII and final paragraphs](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf). Special fuel or primary-sector implementation: Check this point with one of our partner accountants.

## Penalties and interest

Failure to issue/deliver valid CFDIs or make them available when required is covered by CFF art. 83 VII; art. 83 IX also prohibits conditioning issuance on production of the fiscal certificate. For art. 83 VII, art. 84 IV(a) has the general fine, IV(b) the specified individual-regime fine and IV(c) the authorised-donee fine; do not apply the old archived 2025 range as a universal current penalty. [CFF arts. 83–84](https://dgesui.ses.sep.gob.mx/sites/default/files/2026-05/CFF.pdf).

Non-usable hold: select the exact sanction, any reduction, and any updating/late-payment charge only after identifying the breach, period and taxpayer. The original citations to arts. 38/39 for custody penalties and arts. 22/146 for interest are not usable authority for those conclusions. Check this point with one of our partner accountants.

## Cross-border points

For a foreign resident not registered in the RFC, RMF 2.7.1.23 provides XEXX010101000. For a generic recipient RFC, Anexo 20 I.F requires the recipient postal code to equal LugarExpedicion and regime 616; the SAT guide specifies S01 for the foreign generic RFC. The domestic generic RFC is XAXX010101000, under its own conditions. [RMF 2026, 2.7.1.23](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf), [Anexo 20 I.F](https://dof.gob.mx/2022/SHCP/SHCP_130122.pdf), [SAT guide](https://www.sat.gob.mx/minisitio/Factura/documentos/Guia_llenadoCFDI_DPA.pdf).

EC2 (freelancer paid in USD): distinguish the invoice's TipoCambio and the payment complement's TipoCambioP from the tax-conversion rule. For contributions, CFF art. 20 uses the acquisition exchange rate; without acquisition, the Banco de México DOF rate published the day before accrual, or the last prior publication if none was published that day. Do not simply choose the invoice-date rate. [CFF art. 20](https://dgesui.ses.sep.gob.mx/sites/default/files/2026-05/CFF.pdf), [SAT payment standard, TipoCambioP](https://wwwmat.sat.gob.mx/cs/Satellite?blobcol=urldata&blobkey=id&blobtable=MungoBlobs&blobwhere=1461175070885&ssbinary=true).

EC6 (freelancer invoices a US company): the foreign-customer facts alone do not settle IVA or Exportacion. Zero-rating must satisfy LIVA art. 29 and the applicable service-specific conditions; it is not an exemption. Non-usable hold for the original unspecified services/export classification: Check this point with one of our partner accountants. [LIVA art. 29](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf).

## Worked examples

### Deadline checks (original inputs retained)

These compute the nominal fifth-calendar-day cutoff, not a dated holiday-adjusted filing calendar. Apply CFF art. 12 to the actual date where relevant.

```oa-check
name: Complemento de pago deadline
inputs:
  payment_day_of_month: 27
  days_in_month: 30
steps:
  - deadline_day: 5
  - days_allowed: days_in_month - payment_day_of_month + deadline_day
expected:
  deadline_day: 5
  days_allowed: 8
```

```oa-check
name: Early-month payment still due 5th of next month
inputs:
  payment_day_of_month: 3
  deadline_day: 5
  days_in_month: 30
steps:
  - days_allowed: days_in_month - payment_day_of_month + deadline_day
expected:
  deadline_day: 5
  days_allowed: 32
```

Authority: [RMF 2026, 2.7.1.32](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf). The early-month case now uses an explicitly assumed 30-day month; the old output 5 was the next month's day number, not days available after payment.

### Worked example 1: Standard services CFDI (PUE)

Original input: freelancer RFC GOPE850101AB1, regime 612; Mexican corporate customer in regime 601; MXN 10,000 consulting, fully paid at service. Keep I, PUE, transfer form 03 and Exportacion 01 for the assumed domestic service. At the general IVA rate, transferred IVA is MXN 1,600 and gross consideration MXN 11,600. If this is a personal professional service, the company withholds ISR of MXN 1,000 and two-thirds of IVA, rounded to MXN 1,066.67; invoice Total/net payment is MXN 9,533.33. The original MXN 11,600 was not a safe unconditional Total. If the service is instead a business activity, establish its withholding treatment before finalising. [LIVA arts. 1 and 1-A II(a)](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf), [LISR art. 106](https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf), [RLIVA art. 3 I(a)](https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf).

```oa-check
name: Original consulting case with professional-service withholding
inputs:
  fee: 10000
  iva_rate: 0.16
  isr_rate: 0.10
steps:
  - iva: fee * iva_rate
  - gross: fee + iva
  - isr_withheld: fee * isr_rate
  - iva_withheld: round(iva * 2 / 3, 2)
  - net: gross - isr_withheld - iva_withheld
expected:
  iva: 1600
  gross: 11600
  isr_withheld: 1000
  iva_withheld: 1066.67
  net: 9533.33
```

### Worked example 2: CFDI with partial payments (PPD)

Original input: MXN 50,000 invoice, two instalments, first payment MXN 29,000 and remaining payment MXN 29,000. For the original general-rate illustration, explicitly assume the MXN 50,000 is before IVA, no discount and no withholding. IVA is MXN 8,000; Total is MXN 58,000. Initial invoice PPD/FormaPago 99; each payment complement references the original UUID and its applied MXN 29,000. Remaining balance after the first is MXN 29,000, after the second zero. Separate complements are valid; a single monthly complement is also permitted if both payments fall in the same month for the same recipient. [LIVA art. 1](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf), [RMF 2026, 2.7.1.29 and 2.7.1.32](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

```oa-check
name: Original two-instalment case
inputs:
  base: 50000
  iva_rate: 0.16
  first_payment: 29000
  second_payment: 29000
steps:
  - iva: base * iva_rate
  - total: base + iva
  - after_first: total - first_payment
  - after_second: after_first - second_payment
expected:
  iva: 8000
  total: 58000
  after_first: 29000
  after_second: 0
```

### Worked example 3: CFDI to foreign client

Original input: US company; services described as MXN 20,000 equivalent, billed USD 1,142.86 at rate 17.50. Preserve USD SubTotal 1,142.86 and the supplied rate: their product is MXN 20,000.05, a MXN 0.05 rounding difference from 20,000. The rate is a hypothetical input, not a verified rate for an actual date. If the customer is not RFC-registered, the foreign generic rules above apply. IVA rate, taxable territory, Exportacion and foreign-trade-complement selection remain non-usable until the service and use/payment facts are established; neither 0% nor 16% follows automatically from this input. Check this point with one of our partner accountants.

```oa-check
name: Original foreign-currency inputs without changing the invoice amount
inputs:
  usd: 1142.86
  rate: 17.50
  stated_mxn: 20000
steps:
  - converted_mxn: usd * rate
  - difference: converted_mxn - stated_mxn
expected:
  converted_mxn: 20000.05
  difference: 0.05
```

### Worked example 4: Cancellation with replacement

Original input: invoice amount is wrong; correct and replace it. Obtain the replacement's UUID, use reason 01 and identify that UUID in the cancellation request; resolve any related-payment cancellation first. Apply the deadline and full exception matrix, then verify final cancellation status. Do not promise automatic cancellation merely because an amount is small. [SAT process](https://www.sat.gob.mx/minisitio/Factura/cancela_procesocancelacion.htm), [RMF 2026, 2.7.1.34–35](https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf).

EC4 retains its original timing: invoice in January, cancellation sought in July, six months later. For an ordinary same-year invoice this is within the statutory annual-return-month limit; it still requires a supported reason, the applicable acceptance process and final status confirmation. A recipient's rejection does not cancel the invoice.

## Ask the client first

Use the required inputs above. Do not request private signing keys or passwords in chat. Before treating an invoice as ready, resolve missing party data, taxable treatment, any withholding, certification, payment evidence and cancellation dependencies. Do not use a pending status, an illustrative rate or a referred conclusion as a filing instruction.

## Sources

| Source and passages actually read | Official URL | Read on |
| --- | --- | --- |
| CFF, current 09-04-2026 text, arts. 12, 20, 29, 29 Bis, 29-A and 83–84; official government-hosted copy used after the legislature URL timed out | https://dgesui.ses.sep.gob.mx/sites/default/files/2026-05/CFF.pdf | 2026-11-27 |
| RMF 2026, rules 2.2.8, 2.7.1.23, 2.7.1.29, 2.7.1.32–35 and 2.7.2.9, including all acceptance exceptions and certificate conditions | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf | 2026-11-27 |
| SAT 2026 amendment index and amending clauses through the fourth published resolution / latest advance fifth version: applicability check; the cited ordinary-invoice/payment/cancellation rules remain operative | https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/normatividad_rmf_rgce2026.html | 2026-11-27 |
| Anexo 20, CFDI 4.0, I.A / I.F field definitions and validations; 2022 publication remains the technical base, applied with 2026 Anexo 29 | https://dof.gob.mx/2022/SHCP/SHCP_130122.pdf | 2026-11-27 |
| Anexo 29 for 2026, II and VI.1 technical qualifications, with July addition requiring P/N complements and November VI.3 cancellation-response update | https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo_29_RMF2026-09012026.pdf ; https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Primera-Modificacion-Anexo-29-DOF-17072026.pdf ; https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/SegundaModificacion_Anexo29_DOF-06112026.pdf | 2026-11-27 |
| SAT format page: version and PUE/PPD FAQ; recipient-name instructions: uppercase and registered-data punctuation | https://wwwmat.sat.gob.mx/consultas/35025/formato-de-factura-electronica-%28anexo-20%29 ; https://www.sat.gob.mx/minisitio/Factura/documentos/Infografia_FacturaElectronica_NombreReceptor.pdf | 2026-11-27 |
| SAT fiscal-regime table, descriptions for all retained codes; table read from the site's public bundle because its HTML is an application shell | https://www.cloudb.sat.gob.mx/datos_fiscales/regimen | 2026-11-27 |
| SAT CFDI DPA guide, common field definitions, generic-foreign RFC / regime / use and G03; public-entity-specific tax treatment not generalised | https://www.sat.gob.mx/minisitio/Factura/documentos/Guia_llenadoCFDI_DPA.pdf | 2026-11-27 |
| SAT payment-complement 2.0 standard, payment/document attributes and section 4 base-CFDI validations | https://wwwmat.sat.gob.mx/cs/Satellite?blobcol=urldata&blobkey=id&blobtable=MungoBlobs&blobwhere=1461175070885&ssbinary=true | 2026-11-27 |
| SAT cancellation process, reason codes and replacement folio; statutory/RMF qualifications prevail over the summary | https://www.sat.gob.mx/minisitio/Factura/cancela_procesocancelacion.htm | 2026-11-27 |
| SAT medical-deduction page D01 description and donation FAQ D04/G03 distinctions; only code descriptions used | https://www.sat.gob.mx/minisitio/DeduccionesPersonales/gastos_medicos.html ; https://www.sat.gob.mx/minisitio/DonatariasAutorizadas/documentos/preguntasfrecuentes/CFDI.pdf | 2026-11-27 |
| LIVA arts. 1, 1-A II(a), 29; LISR art. 106; RLIVA art. 3 I(a), including professional-service withholding conditions | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf ; https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf ; https://www.ordenjuridico.gob.mx/Documentos/Federal/pdf/wo88442.pdf | 2026-11-27 |

Not yet confirmed: non-usable holds are G01/I01 catalogue descriptions and selection, the original cash-code illustration, the old Exportacion 02/03 mapping and service-export coding, transaction-specific export IVA for the US-company case, and exact sanctions/remediation for late or missing CFDIs. The linked general CFDI filling guide and catalogue entry point timed out on direct and browser access; no failed fetch is counted as a source read. Payroll calculations, foreign-trade-complement preparation, fuel/primary-sector implementation and audit outcomes require their own facts and professional review. Check this point with one of our partner accountants.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network - accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
