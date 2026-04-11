---
name: dominican-republic-itbis
description: Use this skill whenever asked to prepare, review, or create a Dominican Republic ITBIS (Impuesto sobre Transferencias de Bienes Industrializados y Servicios) return for any client. Trigger on phrases like "prepare ITBIS return", "do the ITBIS", "Dominican Republic VAT", "DR tax return", or any request involving Dominican Republic consumption tax filing. Also trigger when classifying transactions for ITBIS purposes from bank statements, invoices, or other source data. ALWAYS read this skill before touching any ITBIS-related work.
---

# Dominican Republic ITBIS Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Dominican Republic |
| Jurisdiction Code | DO |
| Primary Legislation | Codigo Tributario (Tax Code), Ley 11-92, as amended by Ley 253-12 |
| Supporting Legislation | Reglamento de Aplicacion del ITBIS (Decreto 293-11); Normas Generales DGII |
| Tax Authority | Direccion General de Impuestos Internos (DGII) |
| Filing Portal | https://dgii.gov.do (Oficina Virtual DGII) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return form assignment, input tax recovery, derived calculations. Tier 2: partial exemption, free-zone treatments, withholding ITBIS. Tier 3: complex group structures, advance rulings, transfer pricing. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed CPA must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to licensed CPA.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts:

1. **Entity name and RNC (Registro Nacional del Contribuyente)** [T1] -- 9-digit for companies, 11-digit cedula for individuals
2. **ITBIS registration status** [T1] -- all persons making taxable supplies must register
3. **Filing period** [T1] -- monthly (standard for all ITBIS filers)
4. **Industry/sector** [T2] -- impacts classification (free zones, tourism, agriculture)
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required
6. **Does the business import goods?** [T1] -- impacts customs ITBIS
7. **Is the business in a free trade zone?** [T2] -- Ley 8-90 regime
8. **Credit balance brought forward** [T1]

**If items 1-3 are unknown, STOP.**

---

## Step 1: ITBIS Rate Structure [T1]

**Legislation:** Tax Code 11-92, Article 341 (as amended by Ley 253-12).

### Standard Rate

| Rate | Application |
|------|-------------|
| 18% | Standard rate on taxable transfers of industrialized goods and services [T1] |

### Reduced Rates

| Rate | Application |
|------|-------------|
| 16% | Certain goods (yogurt, butter, coffee, fats and oils -- transitional rates applied in reform) [T2] |

Note: The 2012 tax reform (Ley 253-12) introduced a phased schedule to bring previously exempt items to 18%. Some items remain at transitional reduced rates. Flag for reviewer to confirm current applicable rate [T2].

### Zero-Rated / Exempt Supplies [T1]

**Legislation:** Tax Code, Articles 343, 344.

**Exempt goods (no ITBIS, no input credit):**
- Unprocessed agricultural products (rice, beans, vegetables, fruits, fresh meat, fresh fish, eggs, milk)
- Basic food basket items (canasta basica)
- Medicines and pharmaceutical products
- Fuel and derivatives (subject to Impuesto Selectivo al Consumo instead)
- Educational materials, books, newspapers
- Agricultural inputs (fertilizers, pesticides, seeds)

**Exempt services:**
- Educational services (approved institutions)
- Health/medical services
- Financial services (interest, insurance premiums)
- Residential rental
- Electricity (domestic, up to threshold)
- Water (domestic supply)
- Public transportation
- Cultural and sporting events (government-sponsored)

**Exports (0% -- input credit allowed):**
- Export of goods: zero-rated with full input credit recovery [T1]
- Export of services: certain services consumed abroad may qualify [T2]

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale/transfer (ITBIS cobrado -- output) or Purchase (ITBIS pagado -- input)
- Salaries, TSS (social security), ISR withholding, loan repayments, dividends = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (Dominican Republic)
- DR-CAFTA countries: USA, Central America
- International: all other

### 2c. Determine ITBIS Rate [T1]
- Calculate: `rate = itbis_amount / net_amount * 100`
- Normalize: 0% (exempt/export), 16% (reduced), 18% (standard)

### 2d. Determine Expense Category [T1]
- Capital goods (activos fijos): equipment, machinery, vehicles, furniture
- Inventory (inventario): goods for resale
- Operating expenses (gastos): everything else

---

## Step 3: ITBIS Return Form Structure (IT-1) [T1]

**The ITBIS return (Formulario IT-1) is filed monthly.**

### Section I -- ITBIS Cobrado (Output Tax)

| Line | Description |
|------|-------------|
| 1 | Ingresos por operaciones gravadas (Revenue from taxable operations) |
| 2 | ITBIS cobrado (18% or applicable rate) |
| 3 | Exportaciones de bienes (Exports of goods) |
| 4 | Ingresos por operaciones exentas (Exempt revenue) |
| 5 | ITBIS cobrado en servicios prestados (ITBIS on services rendered) |
| 6 | Total ITBIS cobrado |

### Section II -- ITBIS Pagado (Input Tax)

| Line | Description |
|------|-------------|
| 7 | ITBIS pagado en compras locales (ITBIS on local purchases) |
| 8 | ITBIS pagado en importaciones (ITBIS on imports) |
| 9 | ITBIS pagado en gastos (ITBIS on expenses) |
| 10 | Total ITBIS pagado deducible (Total deductible input ITBIS) |

### Section III -- Liquidacion (Settlement)

| Line | Description |
|------|-------------|
| 11 | ITBIS neto (Line 6 - Line 10) |
| 12 | Saldo a favor anterior (Prior credit balance) |
| 13 | Retenciones de ITBIS (ITBIS withheld by third parties) |
| 14 | Otros creditos autorizados |
| 15 | Total a pagar o saldo a favor |

---

## Step 4: Reverse Charge on Imported Services [T1]

**Legislation:** Tax Code, Article 346.

When a Dominican registered person receives services from a non-resident:

1. Self-assess ITBIS at 18% on the value [T1]
2. Report as output ITBIS [T1]
3. Claim as input ITBIS if used for taxable operations [T1]
4. Net effect: zero for fully taxable businesses [T1]

### Exceptions [T1]
- Out-of-scope categories: NEVER self-assess
- Exempt services: self-assess but NO input credit
- Services consumed outside DR: NOT subject to ITBIS

---

## Step 5: ITBIS Withholding (Retenciones) [T1]

**Legislation:** Norma General 07-2007; 02-2005.

The DGII has established a withholding system for ITBIS:

### Designated Withholding Agents (Agentes de Retencion) [T1]

| Agent Type | Withholding Rate |
|------------|-----------------|
| Government entities (Estado) | 100% of ITBIS invoiced [T1] |
| Companies designated by DGII | 30% of ITBIS invoiced on goods, 100% on services from individuals [T1] |
| Credit/debit card processors | 2% of total transaction value (as proxy for ITBIS) [T1] |

### Treatment on the Return [T1]
- The supplier reports full output ITBIS on their IT-1
- ITBIS withheld is reported on Line 13 as a credit
- Net effect: reduces amount payable

### ITBIS Withheld on Payments to Non-Residents [T1]
- When paying a non-resident for services, the payer must withhold and remit 18% ITBIS
- This is reported on Form IR-17 (withholding return)
- The payer may claim input credit on their IT-1

---

## Step 6: Deductibility Check

### Blocked Input ITBIS (No Recovery) [T1]

**Legislation:** Tax Code, Article 349.

- **Entertainment** -- meals, drinks, recreation (unless hospitality business) [T1]
- **Motor vehicles** -- passenger vehicles (exception: rental, taxi, driving school businesses) [T1]
- **Personal use items** -- not for business purposes [T1]
- **Goods/services for exempt operations** -- no input credit [T1]
- **Purchases without valid fiscal receipt (NCF)** -- ITBIS on purchases without a valid Numero de Comprobante Fiscal is NOT deductible [T1]

### Critical: NCF Requirement [T1]

**Legislation:** Tax Code, Article 50; Norma General 06-2018.

- ALL purchases must be supported by a valid NCF (Numero de Comprobante Fiscal) to claim input ITBIS
- The NCF must be verified on the DGII portal (https://dgii.gov.do/NCF)
- Invalid, expired, or missing NCFs = NO input credit
- This is strictly enforced through electronic cross-matching (DGII e-CF system)

### Partial Exemption [T2]

If both taxable and exempt operations:
- Direct attribution first
- Common costs: `Recovery % = (Taxable Revenue / Total Revenue) * 100`
- Flag for reviewer

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| ITBIS registration | All persons making taxable transfers must register (no minimum threshold) [T1] |
| Simplified regime (RST) | Gross income up to DOP 8,698,516 annually (adjusted periodically) [T2] |
| NCF electronic invoicing (e-CF) | Mandatory for large taxpayers; phased rollout [T2] |

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Tax Code, Articles 252, 253, 257.

### Filing Deadlines

| Period | Deadline |
|--------|----------|
| Monthly IT-1 | 20th of the month following the period [T1] |
| ITBIS withholding (IR-17) | 10th of the following month [T1] |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | DOP 4,945 for first month + DOP 4,945 per additional month (adjusted annually) [T1] |
| Late payment | Surcharge of 10% first month + 4% per additional month (recargo) [T1] |
| Interest on late payment | 1.73% per month (tasa de interes indemnizatorio -- adjusted periodically) [T1] |
| Fraud | Criminal prosecution; fines up to 2x tax evaded + imprisonment 2-6 years [T1] |
| Missing NCF | Loss of input ITBIS credit + penalties [T1] |

---

## Step 9: Fiscal Receipt (NCF) Requirements [T1]

**Legislation:** Tax Code, Article 50; Decreto 254-06; Norma General 06-2018.

### Types of NCF (Comprobantes Fiscales)

| Type | Code | Use |
|------|------|-----|
| Credito Fiscal | B01 | B2B transactions (allows buyer input credit) |
| Consumidor Final | B02 | B2C transactions (no input credit for buyer) |
| Nota de Debito | B03 | Price increases, additional charges |
| Nota de Credito | B04 | Returns, discounts, corrections |
| Comprobante de Compras | B11 | Purchases from informal sector |
| Registro Unico de Ingresos | B12 | Summary of minor transactions |
| Gastos Menores | B13 | Minor expenses |
| Gubernamental | B15 | Government entities |
| Regimenes Especiales | B14 | Free zones, special regimes |
| e-CF (electronic) | E31-E46 | Electronic fiscal receipts (mandatory rollout) |

### Key Rules [T1]
- Input ITBIS is ONLY deductible with a valid B01 (Credito Fiscal) or equivalent e-CF
- B02 (Consumidor Final) does NOT support input ITBIS deduction
- All NCFs must be reported in the purchase/sales formats (Formatos 606/607) filed monthly with DGII

---

## Step 10: Classification Matrix [T1]

### Domestic Purchases

| Category | ITBIS Treatment | Input Credit | NCF Required |
|----------|----------------|--------------|--------------|
| Office supplies | 18% | Yes (with B01) | Yes |
| Commercial rent | 18% | Yes (with B01) | Yes |
| Residential rent | Exempt | No | Yes |
| Electricity (commercial) | 18% | Yes | Yes |
| Telephone/internet | 18% | Yes | Yes |
| Motor car | 18% | BLOCKED | Yes |
| Entertainment | 18% | BLOCKED | Yes |
| Professional fees | 18% | Yes (with B01) | Yes |
| Insurance (general) | 18% | Yes | Yes |
| Insurance (life) | Exempt | No | Yes |
| Basic food items | Exempt | No | N/A |
| Medicines | Exempt | No | N/A |

### Sales

| Category | ITBIS | Return Line |
|----------|-------|-------------|
| Domestic taxable sale | 18% | Line 1, Line 2 |
| Export of goods | 0% | Line 3 |
| Exempt supply | Exempt | Line 4 |

---

## Step 11: Free Trade Zone (Zona Franca) Rules [T2]

**Legislation:** Ley 8-90 (Free Trade Zone Law).

- Companies operating in free trade zones are exempt from ITBIS on goods purchased for export processing
- Sales from free zones to local market are subject to ITBIS at 18% as imports
- Transfers between free-zone companies: exempt
- Free-zone companies must use NCF type B14 (Regimenes Especiales)
- Flag for reviewer: free-zone compliance requires careful documentation

---

## Step 12: Monthly Reporting Requirements (Formatos) [T1]

**Legislation:** Norma General 01-2007.

In addition to the IT-1 return, taxpayers must file:

| Format | Description | Deadline |
|--------|-------------|----------|
| Formato 606 | Purchase report (all purchases with NCFs) | 20th of following month |
| Formato 607 | Sales report (all sales with NCFs) | 20th of following month |
| Formato 608 | Cancelled NCFs report | 20th of following month |
| Formato 609 | Payments to non-residents | 20th of following month |

These formats are cross-matched by DGII. Discrepancies trigger audits.

---

## PROHIBITIONS [T1]

- NEVER let AI guess ITBIS classification -- it is deterministic from facts
- NEVER allow input ITBIS without a valid NCF (B01 or e-CF equivalent)
- NEVER allow input credit on B02 (Consumidor Final) receipts
- NEVER allow input credit on blocked categories (entertainment, motor vehicles, personal use)
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse zero-rated exports (input credit allowed) with exempt (NO input credit)
- NEVER file IT-1 without filing matching Formatos 606/607
- NEVER ignore NCF validation -- all NCFs must be verified on DGII portal
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Step 13: Edge Case Registry

### EC1 -- Purchase without NCF [T1]
**Situation:** Supplier provides a receipt but no valid NCF.
**Resolution:** ITBIS is NOT deductible. The full amount including ITBIS becomes a cost. Advise client to request proper B01 NCF from supplier.
**Legislation:** Tax Code, Article 50.

### EC2 -- ITBIS withholding by credit card processor [T1]
**Situation:** Client receives credit card payments. Processor withholds 2% of total.
**Resolution:** The 2% withholding is an advance on ITBIS. Report on Line 13 of IT-1 as a credit. Ensure the withholding certificate is obtained from the processor.

### EC3 -- Free-zone company selling to local market [T2]
**Situation:** Free-zone company sells finished goods to a Dominican company.
**Resolution:** The goods are treated as imports. ITBIS at 18% applies on the CIF value plus customs duties. The buyer pays ITBIS at customs and claims input credit. Flag for reviewer.

### EC4 -- Credit note (Nota de Credito B04) [T1]
**Situation:** Client issues a credit note for returned goods.
**Resolution:** Issue B04 NCF. Reduce output ITBIS on IT-1. Reduce sales in Formato 607. Customer must reduce their input ITBIS.

### EC5 -- Services from non-resident, ITBIS withholding [T1]
**Situation:** Dominican company pays US consultant USD 5,000 for services.
**Resolution:** Withhold 18% ITBIS (DOP equivalent). Report on IR-17 withholding return. Claim as input ITBIS on IT-1 (Line 9 or equivalent). Also consider ISR (income tax) withholding obligations.

### EC6 -- Mixed exempt and taxable operations [T2]
**Situation:** Company operates both a pharmacy (exempt medicines) and a general store (taxable goods).
**Resolution:** Apportion input ITBIS. Direct costs: allocate. Common costs: pro-rata based on revenue. Flag for reviewer.

### EC7 -- Government contract payment [T1]
**Situation:** Client provides services to a government entity. Government withholds 100% ITBIS.
**Resolution:** Report full output ITBIS on IT-1. Report 100% withholding on Line 13. Net ITBIS payable reduced accordingly. Ensure B15 NCF is used.

### EC8 -- E-commerce sales to Dominican consumers [T2]
**Situation:** Foreign e-commerce company sells digital services to DR consumers.
**Resolution:** Under recent rules, non-resident digital service providers may be required to register and charge ITBIS. Flag for reviewer: confirm current status of digital services taxation rules.

### EC9 -- Construction and real estate [T2]
**Situation:** Company sells a newly constructed commercial building.
**Resolution:** Transfer of real estate is subject to ITBIS at 18% on the construction/improvements value. Land component may be excluded. Flag for reviewer: confirm ITBIS treatment on real estate.

### EC10 -- Donations of goods [T1]
**Situation:** Company donates inventory to a charity.
**Resolution:** Donations of goods are treated as taxable transfers for ITBIS purposes. ITBIS must be self-assessed on the fair market value. However, certain donations to approved non-profit organizations may be exempt under specific DGII rulings. Flag for reviewer.

---

## Step 12a: Sector-Specific Guidance [T2]

### Tourism Sector

- **Hotel accommodation**: ITBIS at 18% [T1]
- **CONFOTUR (Ley 158-01) incentives**: approved tourism projects may have ITBIS exemptions on construction and equipment [T2]
- **Restaurant services**: ITBIS at 18% [T1]
- **All-inclusive resorts**: ITBIS on full package price [T1]
- **Propina legal (10% service charge)**: NOT subject to ITBIS (it is a labor charge, not a service) [T1]
- Flag for reviewer: CONFOTUR benefits require valid resolution from DGII

### Financial Services

- **Interest on loans**: exempt [T1]
- **Banking commissions and fees**: taxable at 18% [T1]
- **Insurance premiums (life/health)**: exempt [T1]
- **Insurance premiums (general)**: taxable at 18% [T1]
- **Credit card fees**: taxable at 18% [T1]

### Agriculture

- **Unprocessed agricultural products**: exempt [T1]
- **Processed food products**: taxable at 18% (unless on exempt list) [T1]
- **Agricultural inputs**: exempt [T1]
- **Tobacco (raw)**: exempt [T1]
- **Tobacco (processed/cigars for export)**: zero-rated [T1]

### Manufacturing and Free Zones (Detailed)

- **Free zone (Zona Franca) companies**: Ley 8-90 regime
- **Imports for free zone processing**: ITBIS exempt [T1]
- **Sales from free zone to local market**: treated as imports, ITBIS at 18% [T1]
- **Inter-zone transfers**: ITBIS exempt [T1]
- **Free zone companies selling services to local market**: ITBIS at 18% [T2]
- **NCF type B14**: required for free zone transactions [T1]
- Flag for reviewer: free zone compliance is strict

### Construction

- **Construction services**: ITBIS at 18% [T1]
- **Construction materials**: ITBIS at 18% [T1]
- **Architectural/engineering services**: ITBIS at 18% [T1]

---

## Step 12b: e-CF (Electronic Fiscal Receipt) System [T2]

**Legislation:** Norma General 06-2018; DGII Resoluciones.

The Dominican Republic is transitioning to mandatory electronic invoicing (e-CF):

### e-CF Document Types

| Type | Code | Use |
|------|------|-----|
| e-Factura de Credito Fiscal | E31 | B2B (input credit allowed) |
| e-Factura de Consumo | E32 | B2C (no input credit) |
| e-Nota de Debito | E33 | Additional charges |
| e-Nota de Credito | E34 | Returns, corrections |
| e-Compras | E41 | Purchases from informal sector |
| e-Gastos Menores | E43 | Minor expenses |
| e-Regimenes Especiales | E44 | Free zone, special regime |
| e-Gubernamental | E45 | Government entities |
| e-Exportacion | E46 | Export transactions |

### Key Rules [T1]

- e-CF phased rollout: large taxpayers first, then medium, then small
- Electronic signature and DGII authorization required
- Real-time or batch authorization
- e-CF replaces paper NCF for obligated taxpayers
- Input ITBIS credit rules same as paper NCF (E31 = input credit; E32 = no credit)

---

## Step 14: Test Suite

### Test 1 -- Standard local purchase, 18%
**Input:** Dominican supplier, office supplies, gross DOP 11,800, ITBIS DOP 1,800, net DOP 10,000. Valid B01 NCF.
**Expected output:** Line 7 = DOP 1,800 input ITBIS. Full recovery.

### Test 2 -- Export, zero-rated
**Input:** Registered exporter ships goods to US, net DOP 500,000.
**Expected output:** Line 3 = DOP 500,000. No output ITBIS. Input ITBIS fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase of sedan DOP 2,000,000, ITBIS DOP 360,000. Valid B01.
**Expected output:** ITBIS DOP 360,000 BLOCKED. No input credit.

### Test 4 -- Imported services, reverse charge
**Input:** US firm provides consulting, USD 3,000 (~ DOP 180,000). No ITBIS on invoice.
**Expected output:** Self-assess output ITBIS = DOP 32,400 (18%). Input ITBIS = DOP 32,400. Net = zero.

### Test 5 -- Purchase with B02 receipt (no credit)
**Input:** Client purchases supplies from retailer with B02 (Consumidor Final) receipt. ITBIS DOP 900.
**Expected output:** ITBIS DOP 900 NOT deductible. B02 does not support input credit.

### Test 6 -- Government withholding at 100%
**Input:** Services to government entity DOP 100,000 + ITBIS DOP 18,000. Government withholds 100% ITBIS.
**Expected output:** Output ITBIS = DOP 18,000. Withholding credit (Line 13) = DOP 18,000. Net payable = zero on this transaction.

### Test 7 -- Credit card withholding
**Input:** Client receives credit card payments totaling DOP 500,000. Processor withholds 2% = DOP 10,000.
**Expected output:** Report DOP 10,000 on Line 13 as ITBIS advance credit.

### Test 8 -- Entertainment, blocked
**Input:** Client dinner DOP 5,900 inclusive of ITBIS DOP 900.
**Expected output:** ITBIS DOP 900 BLOCKED. No input credit.

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
