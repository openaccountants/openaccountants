---
name: mexico-einvoice
description: Use this skill whenever asked about Mexico e-invoicing, CFDI (Comprobante Fiscal Digital por Internet), SAT (Servicio de Administración Tributaria), PAC (Proveedor Autorizado de Certificación), timbrado (digital stamping), Anexo 20, CFDI version 4.0, XML schema for Mexican invoices, UUID/folio fiscal, RFC validation, complemento de pago, carta porte, nomina, cancelación de CFDI, or any question about generating, validating, certifying, or troubleshooting Mexican electronic invoices. Also trigger when advising on SAT compliance, PAC selection, XML structure, fiscal regime codes, product catalog codes (c_ClaveProdServ), or CFDI workflow. ALWAYS read this skill before touching any Mexico e-invoice work.
version: 1.2
jurisdiction: MX
tax_year: 2026
last_updated: 2026-11-14
type: filing-howto
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - einvoice-workflow-base
category: invoicing
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mexico Einvoice

## Who this applies to

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | United Mexican States (Mexico) |
| Currency | MXN (Mexican Peso); multi-currency supported with exchange rate |
| E-Invoicing System | CFDI (Comprobante Fiscal Digital por Internet) |
| Governing Body | SAT (Servicio de Administración Tributaria) |
| Key Legislation | Código Fiscal de la Federación (CFF) Art. 29, 29-A; Resolución Miscelánea Fiscal (RMF) |
| Technical Standard | Anexo 20 Version 4.0 |
| Schema Format | XML (W3C compliant) |
| Current Version | CFDI 4.0 (mandatory since 1 January 2023) |
| Certification Model | Three-party clearance: Taxpayer → PAC → SAT |
| Implementation Status | Most mature e-invoicing system in the Americas; mandatory for all taxpayers since 2014 |
| Taxpayer ID | RFC (Registro Federal de Contribuyentes) |

### Key Dates

**Key Dates**

| Event | Date |
| --- | --- |
| CFDI inception | 2004 (CFD); 2011 (CFDI mandatory for large) |
| Universal mandate | 1 April 2014 (all taxpayers) |
| CFDI 3.3 | 1 July 2017 |
| CFDI 4.0 published | 1 January 2022 |
| CFDI 4.0 sole valid version | 1 January 2023 |
| Platform real-time access mandate | 1 April 2026 (Art. 30-B CFF, added DOF 07-11-2025; transitorio: "entrará en vigor el 1 de abril de 2026") |

## Rates, bands and thresholds

### IVA (Value Added Tax)

**IVA (Value Added Tax)**

| Rate | Application | Source |
| --- | --- | --- |
| 16% | General rate (most goods and services) | [LIVA Art. 1 (SAT)](https://wwwmatnp.sat.gob.mx/articulo/19848/articulo-1) |
| 0% | Basic foodstuffs, medicines, exports | [LIVA Art. 2-A (SAT)](https://wwwmatnp.sat.gob.mx/articulo/06071/articulo-2-a) |
| Exempt | Education (Art. 15 Fr. IV), residential rent (Art. 20 Fr. II), medical services by individuals (Art. 15 Fr. XIV) | [LIVA Art. 15 (SAT)](https://wwwmatnp.sat.gob.mx/articulo/67548/articulo-15); [LIVA Art. 20 (SAT)](https://wwwmatnp.sat.gob.mx/articulo/39877/articulo-20) |

### IEPS (Special Production and Services Tax)

- **IEPS applicability** - Applied on specific goods: alcohol, tobacco, fuel, sugary drinks, pesticides. Rates vary by product category.

### Tax Retention

**Tax Retention**

| Tax | Rate | When | Source |
| --- | --- | --- | --- |
| ISR retention | 10% (general regime payees; LISR Art. 106, penultimate paragraph, in force) | Professional services paid by personas morales to personas físicas | [LISR Art. 106, DOF 11-12-2013](https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013) |
| ISR retention - RESICO | 1.25% (LISR Art. 113-J) | Business/professional services or rent from RESICO personas físicas to personas morales | [LISR Art. 113-J, DOF 12-11-2021](https://dof.gob.mx/nota_detalle.php?codigo=5635286&fecha=12/11/2021) |
| IVA retention | Two thirds of the IVA trasladado and effectively paid: 2/3 x 16% = 10.6667% of the invoice (RLIVA Art. 3 fr. I: "las dos terceras partes del impuesto que se les traslade y que haya sido efectivamente pagado"; retention duty: LIVA Art. 1o.-A fr. II a) and c)) | Independent personal services, commission services, and temporary use of goods (leases) from personas físicas to personas morales | [RLIVA Art. 3 fr. I, DOF 04-12-2006](https://dof.gob.mx/nota_detalle.php?codigo=4939297&fecha=04/12/2006) |
| IVA retention - autotransporte | 4% of the consideration effectively paid (RLIVA Art. 3 fr. II) | Land freight autotransporte terrestre de bienes services received by personas morales | [RLIVA Art. 3 fr. II, DOF 04-12-2006](https://dof.gob.mx/nota_detalle.php?codigo=4939297&fecha=04/12/2006) |

### Calculation Rules

- **Calculation Rules** - Tax base per line = Cantidad × ValorUnitario (before tax); Tax per line = Base × TasaOCuota; Round to 2 decimal places at line level (6 decimal places for TasaOCuota); Document SubTotal = sum of all line Importe values; Document Total = SubTotal + TotalImpuestosTrasladados - TotalImpuestosRetenidos; For PPD (deferred payment): taxes recorded in Complemento de Pago at time of actual payment

### Multi-Currency

- **Multi-Currency rules** - If Moneda ≠ MXN, must include TipoCambio (exchange rate). All amounts in the CFDI are in the stated Moneda. SAT computes MXN equivalent using the stated TipoCambio.

## The taxable base

### Who Must Comply

- **Mandate applicability** - ALL taxpayers in Mexico (personas físicas and personas morales) who carry out economic activities. No threshold - every transaction requiring a tax receipt must produce a CFDI. Applies to: sales of goods, services, leases, payroll, donations, exports, imports.

### Document Types (TipoDeComprobante)

**Document Types (TipoDeComprobante)**

| Code | Type | Description |
| --- | --- | --- |
| I | Ingreso | Income invoice (standard sales/services) |
| E | Egreso | Credit note / refund |
| T | Traslado | Transfer of goods (no payment) |
| N | Nómina | Payroll voucher |
| P | Pago | Payment receipt (Complemento de Pago) |

### Complementos (Supplements)

**Complementos (Supplements)**

| Complemento | Use Case |
| --- | --- |
| Pagos 2.0 | Payment receipts for deferred/partial payments |
| Carta Porte 3.1 | Bill of lading for goods transport |
| Nómina 1.2 | Payroll details |
| Comercio Exterior 2.0 | Export invoices |
| INE | Political party donations |
| Hidrocarburos | Oil & gas sector |

### B2C Treatment

- **B2C rules** - B2C sales use RFC genérico: XAXX010101000 (domestic) or XEXX010101000 (foreign). Still requires full CFDI generation and PAC certification. Simplified "factura global" available for aggregating small B2C transactions (daily/weekly/monthly).

## Deadlines and filing

### PAC Certification (Mandatory)

**PAC Certification (Mandatory)**

| Aspect | Detail |
| --- | --- |
| Role | PACs validate, stamp, and transmit CFDIs to SAT |
| Number of Active PACs | ~70+ authorized by SAT |
| Connection | SOAP or REST web services (varies by PAC) |
| Validation Steps | Structure, catalogs, RFC validation, tax math, CSD validity |
| Stamping Time | Usually < 3 seconds |
| Fallback | SAT free portal (portal.sat.gob.mx) for manual low-volume issuance |

### Communication Flow

- **Communication Flow** - 1. Taxpayer system generates CFDI XML (signed with CSD) 2. Submit to PAC via web service 3. PAC validates structure + data against SAT catalogs 4. PAC validates receiver RFC/name/postal code against SAT database 5. PAC generates UUID (folio fiscal) 6. PAC applies TimbreFiscalDigital complement (SAT stamp) 7. PAC returns stamped CFDI to taxpayer 8. PAC transmits a copy to SAT 9. Taxpayer delivers stamped CFDI to receiver

### SAT Free Issuance Portal

- **SAT Free Issuance Portal** - Available at portalcfdi.facturaelectronica.sat.gob.mx. Limited to low-volume issuance. Requires e.firma (FIEL) login. Not suitable for automated/high-volume scenarios.

### Cancellation

**Cancellation**

| Rule | Detail |
| --- | --- |
| Method | Submit cancellation request via PAC |
| Receiver acceptance | Required for invoices > MXN 1,000; receiver must respond within 3 days of the request (RMF 2025 rule 2.7.1.34: "a más tardar dentro de los tres días siguientes") |
| Motivo (reason) | 01=CFDI with errors (related doc exists), 02=CFDI with errors (no replacement), 03=Transaction did not occur, 04=Related to global invoice |
| Time limit | Same fiscal year or month following issuance |
| FolioSustitucion | UUID of replacement CFDI (if motivo=01) |

## Section 3 -- Technical Format

### XML Schema

**XML Schema**

| Aspect | Detail |
| --- | --- |
| Format | XML |
| Version Attribute | Version="4.0" |
| Root Element | `<cfdi:Comprobante>` |
| Primary Namespace | http://www.sat.gob.mx/cfd/4 |
| XSD Schema | cfdv40.xsd |
| Timbre Fiscal Schema | TimbreFiscalDigitalv11.xsd |
| XSLT (cadena original) | cadenaoriginal_4_0.xslt |
| Catalogs XSD | catCFDI.xsd |
| Encoding | UTF-8 |

### CFDI Lifecycle

Taxpayer ERP/System → Generate XML → Sign with CSD (e.firma) →
Submit to PAC → PAC validates → PAC stamps (timbrado) →
PAC returns UUID + TimbreFiscalDigital → Invoice valid →
PAC transmits copy to SAT

### Digital Certificates

**Digital Certificates**

| Certificate | Purpose |
| --- | --- |
| e.firma (FIEL) | General identity certificate (not for signing CFDI directly) |
| CSD (Certificado de Sello Digital) | Specifically for signing CFDI; obtained from SAT portal |
| PAC Certificate | PAC's own certificate for the timbrado (fiscal stamp) |

### Cadena Original

- **Cadena Original** - The "cadena original" is a pipe-delimited string of all significant invoice fields, generated via XSLT transformation. The taxpayer's digital seal (sello) is a SHA-256 + RSA signature of this cadena original.

## Section 4 -- Mandatory Fields

### Comprobante (Root) Attributes

**Comprobante (Root) Attributes**

| Attribute | Description | Format/Values |
| --- | --- | --- |
| Version | Schema version | "4.0" |
| Serie | Series identifier | 1-25 alphanumeric |
| Folio | Sequential number | 1-40 alphanumeric |
| Fecha | Issue date/time | AAAA-MM-DDThh:mm:ss |
| FormaPago | Payment form code | c_FormaPago catalog (01=Cash, 03=Transfer, 99=Por definir) |
| SubTotal | Subtotal before tax | Decimal |
| Moneda | Currency code | c_Moneda catalog (MXN, USD, EUR, etc.) |
| TipoCambio | Exchange rate (if not MXN) | Decimal |
| Total | Total amount | Decimal |
| TipoDeComprobante | Document type | I, E, T, N, P |
| Exportacion | Export indicator | 01=No export, 02=Definitive, 03=Temporary |
| MetodoPago | Payment method | PUE (single payment) or PPD (deferred/partial) |
| LugarExpedicion | Issuing postal code | 5-digit Mexican postal code |
| Sello | Digital seal (signature) | Base64-encoded RSA signature |
| NoCertificado | CSD certificate number | 20-digit string |
| Certificado | CSD public certificate | Base64-encoded X.509 |

### Emisor (Issuer)

**Emisor (Issuer)**

| Element/Attribute | Description |
| --- | --- |
| Rfc | Issuer RFC (12 or 13 chars) |
| Nombre | Legal name (must match SAT records exactly) |
| RegimenFiscal | Fiscal regime code (c_RegimenFiscal catalog) |

### Receptor (Receiver)

**Receptor (Receiver)**

| Element/Attribute | Description |
| --- | --- |
| Rfc | Receiver RFC (or XAXX010101000 for generic B2C) |
| Nombre | Receiver legal name (must match SAT records) |
| DomicilioFiscalReceptor | Receiver's fiscal postal code (must match SAT records) |
| RegimenFiscalReceptor | Receiver's fiscal regime code |
| UsoCFDI | Purpose of CFDI (c_UsoCFDI: G01=Acquisition, G03=Expenses, etc.) |

### Conceptos (Line Items)

**Conceptos (Line Items)**

| Attribute | Description |
| --- | --- |
| ClaveProdServ | SAT product/service catalog code (8 digits) |
| NoIdentificacion | Internal product identifier |
| Cantidad | Quantity |
| ClaveUnidad | Unit of measure code (c_ClaveUnidad) |
| Unidad | Unit description |
| Descripcion | Item description |
| ValorUnitario | Unit price |
| Importe | Line amount (Cantidad × ValorUnitario) |
| ObjetoImp | Tax object (01=No tax object, 02=Yes taxed, 03=Yes not taxed, 04=Yes partially) |

### Impuestos (Taxes)

**Impuestos (Taxes)**

| Path | Description |
| --- | --- |
| Concepto/Impuestos/Traslados/Traslado | Tax transfer per line |
| @Base | Taxable base |
| @Impuesto | Tax code (002=IVA, 003=IEPS) |
| @TipoFactor | Tasa (rate), Cuota (fixed), Exento (exempt) |
| @TasaOCuota | Rate value (0.160000 for 16% IVA) |
| @Importe | Tax amount |
| Impuestos/TotalImpuestosTrasladados | Document-level total transferred taxes |
| Impuestos/TotalImpuestosRetenidos | Document-level total retained taxes |

### Timbre Fiscal Digital (Added by PAC)

**Timbre Fiscal Digital (Added by PAC)**

| Attribute | Description |
| --- | --- |
| Version | "1.1" |
| UUID | Folio fiscal (36-char UUID) - the unique invoice identifier |
| FechaTimbrado | PAC stamping timestamp |
| RfcProvCertif | PAC's RFC |
| SelloCFD | Taxpayer's seal (repeated) |
| NoCertificadoSAT | SAT certificate number used by PAC |
| SelloSAT | PAC/SAT digital seal |

## Section 6 -- Validation Rules

### PAC Validation Sequence

- **PAC Validation Sequence** - 1. Structural - XML well-formed, conforms to cfdv40.xsd 2. Catalog codes - All coded fields must exist in SAT catalogs (c_FormaPago, c_Moneda, c_ClaveProdServ, c_ClaveUnidad, c_UsoCFDI, c_RegimenFiscal, etc.) 3. RFC validation - Receiver RFC must exist in SAT's valid RFC list (LRFC) 4. Name matching - Receiver Nombre must match SAT records exactly (including accents/capitalization) 5. Postal code - DomicilioFiscalReceptor must match SAT's registered address for that RFC 6. Fiscal regime - RegimenFiscalReceptor must match SAT's records 7. Mathematical - SubTotal = sum of Concepto.Importe; Total = SubTotal + taxes - retentions 8. CSD validity - Certificate not expired, not revoked, belongs to issuer RFC 9. Seal verification - Sello matches cadena original using CSD public key

### Common Rejection Reasons

**Common Rejection Reasons**

| Error | Description | Fix |
| --- | --- | --- |
| 301 | XML structure invalid | Validate against cfdv40.xsd |
| 302 | CSD expired or revoked | Renew CSD at SAT portal |
| 303 | Invalid seal | Recompute cadena original and resign |
| 305 | Receiver RFC not in LRFC | Verify RFC exists in SAT database |
| 306 | Receiver name mismatch | Use exact name from SAT's constancia |
| 307 | Receiver postal code mismatch | Use fiscal domicile postal code |
| 402 | Invalid ClaveProdServ | Look up correct 8-digit code in SAT catalog |

## Section 8 -- Archiving Requirements

**Archiving Requirements**

| Requirement | Detail |
| --- | --- |
| Retention Period | 5 years from date the tax return was filed (CFF Art. 30); effectively 6-7 years |
| Format | Original signed XML (with TimbreFiscalDigital) |
| Accessibility | Must be available for SAT audit; queryable from SAT portal |
| Storage | Electronic; taxpayer's own systems + copy maintained by SAT |
| PDF Representation | Optional; XML is the legal document; PDF/printed version is courtesy copy |
| Complementos | Must retain all associated complementos (pagos, carta porte, etc.) |
| Cancellation Records | Retain cancelled CFDIs with cancellation acknowledgment |
| Platform Data (from 1 April 2026) | Platforms must provide SAT permanent online access; data archived 5+ years |

## Penalties and interest

**Penalties for Non-Compliance**

| Violation | Penalty |
| --- | --- |
| Not issuing CFDI | MXN 19,700.00 - MXN 112,650.00 per event for tax year 2025 (RMF 2025 Anexo 5); MXN 22,300.00 - MXN 127,530.00 for 2026 (CFF Art. 84 fr. IV a), updated DOF 28-12-2025). Infraction: CFF Art. 83 fr. VII |
| Issuing CFDI without fiscal requirements | Same range as above (CFF Art. 83 fr. VII: "expedirlos sin que cumplan los requisitos") |
| Not delivering CFDI to client upon request | Same range as above (CFF Art. 83 fr. VII: "no entregar o no poner a disposición de los clientes") |
| CSD cancellation by SAT | SAT may cancel CSD for repeated violations (prevents all future CFDI issuance) |
| Simulated operations (EFOS) | 2-9 years imprisonment + fines (CFF Art. 113 Bis) |
| Acquiring/using CFDI from EFOS | Tax deductions/credits disallowed + penalty |
| Late cancellation | Administrative fines; SAT may reject cancellation |

### Receiver Consequences

- **Receiver Consequences** - Receiver who deducts/credits a CFDI that does not meet requirements risks deduction disallowance. ISR deductions and IVA credits require a valid CFDI with correct receiver data.

## Cross-border points

### Monthly VAT Return (Declaración Mensual IVA)

- **Monthly VAT Return** - IVA trasladado (output VAT) derived from type "I" CFDIs issued. IVA acreditable (input VAT) derived from type "I" CFDIs received. IVA retenido from retention CFDIs. SAT pre-fills monthly return proposals based on CFDI data.

### Annual ISR Return

- **Annual ISR Return** - Income declared must match sum of type "I" CFDIs issued in the fiscal year. Deductions must be backed by valid received CFDIs. SAT cross-references reported income vs. CFDI issuance records.

### Payroll (Nómina)

- **Payroll (Nómina) interactions** - Payroll CFDIs (type "N" with Nómina complemento) feed into: Employee's annual tax return (pre-filled income); Employer's ISR withholding obligations; Social security (IMSS) cross-validation.

### Complemento de Pago

- **Complemento de Pago rules** - For PPD method invoices, actual VAT is recognized only when payment CFDI is issued. Cashflow-based IVA timing: VAT liability/credit arises on payment date, not invoice date. Monthly IVA return uses payment CFDIs for deferred-payment transactions.

### SAT Audit Crossmatching

- **SAT Audit Crossmatching** - SAT automatically cross-references buyer-seller CFDI pairs. Discrepancies flagged in taxpayer's "Buzón Tributario" (tax mailbox). Invitation letters ("carta invitación") issued for unexplained income vs. CFDI mismatches.

## Worked examples

### Worked example 1: Services CFDI with ISR retention

**Input:** Professional services CFDI under the general regime: subtotal $10,000.00; IVA transferred at 16%; the payer retains ISR at 10% (LISR Art. 106).

**Computation:**
```
Subtotal:             $10,000.00
IVA trasladado 16%:    $1,600.00
Total:                $11,600.00
ISR retenido 10%:      $1,000.00
Net cash to issuer:   $11,600.00 - $1,000.00 = $10,600.00
```

```oa-check
name: Services CFDI with 10 percent ISR retention (Art. 106)
inputs:
  subtotal: 10000
steps:
  - iva: round(subtotal * 0.16, 2)
  - total: subtotal + iva
  - isr: round(subtotal * 0.10, 2)
  - net: total - isr
expected:
  iva: 1600.00
  total: 11600.00
  isr: 1000.00
  net: 10600.00
```

## Ask the client first

- Which CFDI types and monthly volumes; which PAC do they use?
- Do they issue CFDIs to digital platforms or receive platform CFDIs (CFF Art. 30-B, platform access from 1 April 2026)?
- General regime (10% ISR retention, LISR Art. 106) or RESICO (1.25%, LISR Art. 113-J)?
- Who monitors acceptance and rejection of cancellation requests in the SAT portal?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| SAT article portal, LIVA Arts. 1, 2-A, 15 and 20, read for 16%, the 0% list, exempt education (Art. 15 Fr. IV), medical services (Art. 15 Fr. XIV) and residential rent (Art. 20 Fr. II) | https://wwwmatnp.sat.gob.mx/ordenamiento/37585/ley-del-impuesto-al-valor-agregado | 2026-11-14 |
| DOF 11-12-2013, decree issuing the LISR, read for Art. 106 (10% retention) | https://dof.gob.mx/nota_detalle.php?codigo=5325373&fecha=11/12/2013 | 2026-11-14 |
| DOF 12-11-2021, RESICO reform, read for LISR Art. 113-J (1.25%) | https://dof.gob.mx/nota_detalle.php?codigo=5635286&fecha=12/11/2021 | 2026-11-14 |
| DOF 04-12-2006, Reglamento de la Ley del IVA, read for Art. 3 fr. I (two thirds) and fr. II (4% on land freight) | https://dof.gob.mx/nota_detalle.php?codigo=4939297&fecha=04/12/2006 | 2026-11-14 |
| Codigo Fiscal de la Federacion, texto vigente (ultima reforma DOF 09-04-2026; multas actualizadas DOF 28-12-2025) | https://www.diputados.gob.mx/LeyesBiblio/pdf/CFF.pdf | 2026-10-31 |
| Ley del Impuesto sobre la Renta, texto vigente (DOF 01-04-2024) | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-28 |
| Ley del Impuesto al Valor Agregado, texto vigente 2026 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf | 2026-11-02 |
| Reglamento de la Ley del IVA, texto vigente (Cámara de Diputados, DOF 04-12-2006, ultima reforma DOF 25-09-2014), Art. 3 frs. I y II | https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LIVA_250914.pdf | 2026-11-02 |
| Resolucion Miscelanea Fiscal 2025 (reglas 2.7.1.34, 2.7.1.35) | http://omawww.sat.gob.mx/normatividad_RMF_RGCE/Paginas/documentos2025/rmf/rmf/RMF_2025-30122024.pdf | 2026-11-02 |
| RMF 2025 Anexo 5 (multas actualizadas) | http://omawww.sat.gob.mx/normatividad_RMF_RGCE/Paginas/documentos2025/rmf/anexos/Anexo5_RMF2025-30122024.pdf | 2026-11-02 |

Not yet confirmed: number of active PACs; PAC-to-SAT copy transmission window; error-code table (301-402) is PAC-vendor convention, not statute text.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Público, CPA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
