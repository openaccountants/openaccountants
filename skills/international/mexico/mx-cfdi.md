---
name: mx-cfdi
description: Use this skill whenever asked about Mexican CFDI electronic invoicing. Trigger on phrases like "CFDI", "factura electronica", "PAC", "complemento de pago", "comprobante fiscal", "SAT factura", "CFDI 4.0", "timbrado", "cancelacion CFDI", or any question about issuing, receiving, or managing electronic invoices in Mexico. Covers CFDI 4.0 structure, PAC certification, complemento de pago, uso de CFDI, cancellation rules, and SAT obligations. ALWAYS read this skill before touching any Mexican CFDI work.
---

# Mexico CFDI Electronic Invoicing -- Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Mexico |
| Jurisdiction Code | MX |
| Primary Legislation | Codigo Fiscal de la Federacion (CFF), Art. 29, 29-A |
| Supporting Legislation | Resolucion Miscelanea Fiscal (RMF) 2025; Anexo 20 (CFDI technical standard) |
| Tax Authority | Servicio de Administracion Tributaria (SAT) |
| Portal | Portal SAT (sat.gob.mx) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Mexican contador publico |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: CFDI 4.0 mandatory fields, PAC timbrado, uso de CFDI codes, cancellation rules. Tier 2: complemento de pago timing, foreign currency CFDIs, regime-specific codes. Tier 3: CFDI for payroll (nomina), foreign trade complement, audits. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before advising on any CFDI matter, you MUST know:

1. **RFC (Registro Federal de Contribuyentes)** [T1] -- tax ID
2. **Tax regime (regimen fiscal)** [T1] -- determines regime code on CFDI
3. **e.firma (FIEL) and CSD (Certificado de Sello Digital)** [T1] -- required for issuing CFDIs
4. **PAC provider** [T1] -- which authorized certification provider is used
5. **Type of transaction** [T1] -- sale, service, payment receipt, credit note
6. **Client's RFC and tax regime** [T1] -- required on CFDI 4.0 for the recipient
7. **Uso de CFDI** [T1] -- the purpose code the recipient needs

**If the client does not have a CSD, STOP. They cannot issue CFDIs without it. Must apply at SAT first.**

---

## Step 1: CFDI 4.0 Overview [T1]

**Legislation:** CFF Art. 29, 29-A; Anexo 20 v4.0

CFDI 4.0 has been mandatory since April 1, 2023. All previous versions are obsolete.

### Key Changes from CFDI 3.3 to 4.0 [T1]

| Change | Detail |
|--------|--------|
| Recipient name validation | Must match exactly with SAT's Constancia de Situacion Fiscal |
| Recipient RFC validation | SAT validates recipient RFC in real time |
| Recipient tax regime | Now mandatory (was optional) |
| Recipient postal code | Now mandatory (fiscal domicile of recipient) |
| Export field | New mandatory field (even if "01" = no export) |

---

## Step 2: CFDI 4.0 Mandatory Fields [T1]

**Legislation:** Anexo 20, Seccion II

| Field | Description | Example |
|-------|-------------|---------|
| Version | Always "4.0" | 4.0 |
| Serie | Invoice series (optional but recommended) | A |
| Folio | Sequential number (optional but recommended) | 1001 |
| Fecha | Date and time of issuance (ISO 8601) | 2025-06-15T10:30:00 |
| FormaPago | Payment method code (catalogo c_FormaPago) | 03 (transfer), 01 (cash), 99 (por definir) |
| SubTotal | Amount before tax | 10000.00 |
| Moneda | Currency code (ISO 4217) | MXN, USD |
| TipoCambio | Exchange rate (required if not MXN) | 17.50 |
| Total | Total including tax | 11600.00 |
| TipoDeComprobante | I (ingreso), E (egreso), T (traslado), P (pago), N (nomina) | I |
| Exportacion | Export code: 01 (no), 02 (definitive), 03 (temporary) | 01 |
| MetodoPago | PUE (una sola exhibicion) or PPD (parcialidades/diferido) | PUE |
| LugarExpedicion | Issuer's postal code | 06600 |
| **Emisor (Issuer)** | | |
| Rfc | Issuer RFC | XAXX010101000 |
| Nombre | Issuer legal name (must match SAT records) | Juan Perez Lopez |
| RegimenFiscal | Issuer regime code (catalogo c_RegimenFiscal) | 612 (personas fisicas) |
| **Receptor (Recipient)** | | |
| Rfc | Recipient RFC | XEXX010101000 |
| Nombre | Recipient legal name (must match SAT records exactly) | Empresa SA de CV |
| DomicilioFiscalReceptor | Recipient postal code | 01000 |
| RegimenFiscalReceptor | Recipient regime code | 601 |
| UsoCFDI | Purpose of CFDI for recipient (catalogo c_UsoCFDI) | G03 (gastos en general) |

---

## Step 3: Common Uso de CFDI Codes [T1]

| Code | Description | Typical Use |
|------|-------------|-------------|
| G01 | Adquisicion de mercancias | Purchase of goods |
| G03 | Gastos en general | General expenses (most common for services) |
| I01 | Construcciones | Construction |
| D01 | Honorarios medicos | Medical fees |
| D04 | Donativos | Donations |
| S01 | Sin efectos fiscales | No tax effect (informational) |
| CP01 | Pagos | For complemento de pago |

---

## Step 4: Common Regimen Fiscal Codes [T1]

| Code | Regime |
|------|--------|
| 601 | General de Ley Personas Morales |
| 603 | Personas Morales con Fines no Lucrativos |
| 605 | Sueldos y Salarios |
| 606 | Arrendamiento |
| 607 | Regimen de Enajenacion o Adquisicion de Bienes |
| 608 | Demas ingresos |
| 610 | Residentes en el Extranjero sin EP |
| 612 | Personas Fisicas con Actividades Empresariales y Profesionales |
| 616 | Sin obligaciones fiscales |
| 621 | Incorporacion Fiscal (historical) |
| 625 | Regimen Simplificado de Confianza (RESICO) |
| 626 | RESICO Personas Morales |

---

## Step 5: PAC (Proveedor Autorizado de Certificacion) [T1]

**Legislation:** CFF Art. 29, fraccion IV

| Detail | Value |
|--------|-------|
| Purpose | PACs validate and digitally stamp (timbrar) CFDIs |
| Requirement | Every CFDI must be certified by an authorized PAC |
| Timing | Within 72 hours of the transaction (or at time of issuance) |
| UUID | The PAC assigns a unique identifier (UUID / folio fiscal) |
| Cost | PACs charge per CFDI stamped (some free tiers for low volume) |

### Timbrado Process [T1]

1. Taxpayer generates CFDI XML with their CSD
2. Sends to PAC for validation
3. PAC validates against SAT catalogs and recipient data
4. PAC stamps (timbra) the CFDI, adding Timbre Fiscal Digital
5. Returns the stamped XML and optional PDF representation
6. SAT receives a copy from the PAC

---

## Step 6: Complemento de Pago (Payment Complement) [T1]

**Legislation:** RMF 2025, Regla 2.7.1.32

### When Required [T1]

| Scenario | Required? |
|----------|----------|
| Full payment at time of invoice (PUE) | No -- full CFDI with FormaPago is sufficient |
| Partial payments or deferred payment (PPD) | Yes -- must issue complemento de pago for each payment received |

### Complemento de Pago Structure [T1]

| Field | Detail |
|-------|--------|
| TipoDeComprobante | "P" (pago) |
| Subtotal/Total | 0 (payment complements have zero amounts in the main body) |
| Complemento contains | Payment date, payment method, amount, currency, related CFDI UUID(s), amount applied per CFDI |

### Timing Rules [T1]

| Rule | Deadline |
|------|----------|
| Issue complemento de pago | By the 5th day of the month following the month payment was received |
| Late issuance | May trigger SAT queries or penalties |

---

## Step 7: Cancellation Rules [T1]

**Legislation:** CFF Art. 29-A, penultimo parrafo; RMF 2025

### Cancellation Process [T1]

| Rule | Detail |
|------|--------|
| Cancellation must state reason | Mandatory reason code (catalogo c_Motivocancelacion) |
| Reason 01 | Comprobante emitido con errores con relacion (replacement CFDI issued) |
| Reason 02 | Comprobante emitido con errores sin relacion (no replacement) |
| Reason 03 | No se llevo a cabo la operacion (transaction did not occur) |
| Reason 04 | Operacion nominativa relacionada en la factura global |
| Recipient acceptance | Required for CFDIs with total > MXN 1,000 (recipient has 72 hours to accept/reject via Buzon Tributario) |
| Cancellation deadline | Must cancel within the same fiscal year of issuance, or by the deadline for the annual return |

### Cancellation Without Recipient Acceptance [T1]

No acceptance needed when:
- CFDI total <= MXN 1,000
- CFDI is to general public (RFC generico XAXX010101000)
- Payroll CFDIs (nomina)
- Export CFDIs
- Traspasos between own accounts

---

## Step 8: Edge Case Registry

### EC1 -- Recipient name does not match SAT records [T1]
**Situation:** Client tries to issue CFDI but PAC rejects because recipient name doesn't match.
**Resolution:** CFDI 4.0 validates recipient name against SAT's database. Recipient must provide their exact legal name as shown on their Constancia de Situacion Fiscal. Even accent marks and abbreviations matter.

### EC2 -- Payment received in USD [T2]
**Situation:** Freelancer receives payment in USD for services.
**Resolution:** CFDI can be issued in USD (Moneda: USD). Must include TipoCambio (exchange rate). Use the exchange rate published by Banco de Mexico for the date. For tax purposes, income is converted to MXN. [T2] Flag for reviewer on exchange rate date selection.

### EC3 -- Forgot to issue complemento de pago [T1]
**Situation:** Client issued PPD CFDI 4 months ago, received payment, never issued complemento de pago.
**Resolution:** Issue the complemento de pago immediately. Late issuance may trigger SAT automated queries. The original CFDI with PPD method remains open until the complemento is issued.

### EC4 -- Client wants to cancel a CFDI from 6 months ago [T1]
**Situation:** CFDI issued in January, client wants to cancel in July.
**Resolution:** Cancellation is allowed within the same fiscal year (or before annual return deadline). If total > MXN 1,000, recipient must accept cancellation within 72 hours. If recipient rejects, cancellation fails.

### EC5 -- RESICO freelancer issuing CFDI [T1]
**Situation:** Client is under RESICO (Regimen Simplificado de Confianza).
**Resolution:** Use RegimenFiscal code 625. CFDIs are issued normally through PAC. RESICO does not exempt from CFDI obligations. IVA is still charged on the CFDI (RESICO replaces ISR, not IVA).

### EC6 -- CFDI to foreign client (non-resident) [T1]
**Situation:** Freelancer invoices a US company.
**Resolution:** Use recipient RFC generico for foreign residents: XEXX010101000. Recipient name as the foreign entity's legal name. RegimenFiscalReceptor: 616. UsoCFDI: S01. Exportacion field: 02 (definitive export of services) or 01 if service consumed in Mexico.

---

## Step 9: Test Suite

### Test 1 -- Standard services CFDI (PUE)
**Input:** Freelancer (RFC: GOPE850101AB1, Regime 612) invoicing Mexican company for MXN 10,000 consulting. Full payment at time of service. Recipient in regime 601.
**Expected output:**
- TipoDeComprobante: I
- MetodoPago: PUE
- SubTotal: 10,000.00
- IVA Trasladado: 1,600.00 (16%)
- Total: 11,600.00
- FormaPago: 03 (transferencia)
- Exportacion: 01

### Test 2 -- CFDI with partial payments (PPD)
**Input:** Invoice for MXN 50,000. Client will pay in 2 instalments.
**Expected output:**
- Initial CFDI: MetodoPago PPD, FormaPago 99 (por definir), Total 58,000 (incl. IVA)
- After 1st payment of MXN 29,000: issue complemento de pago (Tipo P) referencing original UUID, amount applied 29,000
- After 2nd payment: second complemento de pago for remaining 29,000

### Test 3 -- CFDI to foreign client
**Input:** US company, services MXN 20,000 equivalent (billed in USD 1,142.86 at rate 17.50).
**Expected output:**
- Receptor RFC: XEXX010101000
- Moneda: USD
- TipoCambio: 17.50
- SubTotal: 1,142.86 (USD)
- IVA: 0% if export of services (verify applicable exemption) OR 16% if consumed in Mexico
- Exportacion: 02 (if definitive export)

### Test 4 -- Cancellation with replacement
**Input:** CFDI with error in amount. Must cancel and reissue.
**Expected output:**
- Issue new (correct) CFDI first
- Cancel original with Motivo 01 (con relacion) referencing the new CFDI's UUID
- If original total > MXN 1,000: wait for recipient acceptance (72 hours max)

---

## PROHIBITIONS

- NEVER issue a CFDI without a valid CSD -- it will be rejected
- NEVER use CFDI version 3.3 -- only 4.0 is valid from April 2023
- NEVER omit the recipient's RFC, name, regime, or postal code -- all are mandatory in 4.0
- NEVER issue a PPD CFDI without following up with complemento de pago when payment is received
- NEVER cancel a CFDI without specifying a valid motivo de cancelacion code
- NEVER assume cancellation is automatic -- CFDIs over MXN 1,000 require recipient acceptance
- NEVER use FormaPago 99 with MetodoPago PUE -- 99 is only for PPD
- NEVER ignore the complemento de pago deadline (5th of the following month)
- NEVER present guidance as definitive -- always label as estimated and direct client to a Mexican contador publico

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico or equivalent licensed practitioner in Mexico) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
