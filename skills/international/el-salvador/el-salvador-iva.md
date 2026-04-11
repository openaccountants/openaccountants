---
name: el-salvador-iva
description: Use this skill whenever asked to prepare, review, or create an El Salvador IVA (Impuesto a la Transferencia de Bienes Muebles y a la Prestacion de Servicios) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "El Salvador VAT", or any request involving El Salvador value added tax filing. ALWAYS read this skill before touching any El Salvador IVA-related work.
---

# El Salvador IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | El Salvador |
| Jurisdiction Code | SV |
| Primary Legislation | Ley del Impuesto a la Transferencia de Bienes Muebles y a la Prestacion de Servicios (Ley del IVA), Decreto Legislativo 296 |
| Supporting Legislation | Reglamento de la Ley del IVA; Codigo Tributario |
| Tax Authority | Ministerio de Hacienda (MH) / Direccion General de Impuestos Internos (DGII) |
| Filing Portal | https://portaldgii.mh.gob.sv (Portal DGII) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return form assignment, input tax recovery, derived calculations. Tier 2: partial exemption, free zone, maquila treatments. Tier 3: complex structures, rulings. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and NIT (Numero de Identificacion Tributaria)** [T1] -- 14-digit NIT
2. **NRC (Numero de Registro de Contribuyente)** [T1] -- IVA registration number
3. **Filing period** [T1] -- monthly (standard for all IVA filers)
4. **Industry/sector** [T2] -- impacts classification (maquila, free zone, agriculture)
5. **Does the business make exempt supplies?** [T2]
6. **Does the business import goods?** [T1]
7. **Is the business in a free trade zone (Zona Franca)?** [T2]
8. **Credit balance brought forward** [T1]

**If items 1-3 are unknown, STOP.**

---

## Step 1: IVA Rate Structure [T1]

**Legislation:** Ley del IVA, Article 54.

### Standard Rate

| Rate | Application |
|------|-------------|
| 13% | Standard rate on all taxable transfers of goods and provision of services [T1] |

### Exempt Supplies [T1]

**Legislation:** Ley del IVA, Articles 44, 45, 46.

**Exempt goods (Article 44):**
- Unprocessed agricultural products: grains, fresh fruits, vegetables, fresh meats, eggs, milk
- Live animals for production
- Medicines and pharmaceutical products
- Agricultural inputs (fertilizers, insecticides, seeds)
- Books, newspapers, school supplies
- Fuel and petroleum derivatives (subject to specific fuel contribution instead)
- Machinery for agricultural use

**Exempt services (Article 46):**
- Health/medical services
- Educational services (authorized institutions)
- Financial services (interest, insurance premiums)
- Residential rental
- Public transportation
- Water (piped, domestic)
- Electricity (domestic, first tier consumption)

### Exports (0% -- Full Input Credit) [T1]
- Export of goods: zero-rated with full input credit [T1]
- Export of services: services consumed outside El Salvador by non-residents [T2]

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (debito fiscal -- output) or Purchase (credito fiscal -- input)
- Salaries, ISSS (social security), AFP (pension), ISR (income tax), loans, dividends = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (El Salvador)
- Central American (Guatemala, Honduras, Nicaragua, Costa Rica)
- International

### 2c. Determine IVA Rate [T1]
- 0% (export), 13% (standard), or exempt

---

## Step 3: IVA Return Form Structure (F-07) [T1]

**Filed monthly via Portal DGII.**

### Debito Fiscal (Output)

| Line | Description |
|------|-------------|
| 1 | Ventas internas gravadas (Domestic taxable sales) |
| 2 | Ventas a contribuyentes (B2B taxable sales) |
| 3 | Ventas a consumidor final (B2C taxable sales) |
| 4 | Exportaciones (Exports at 0%) |
| 5 | Ventas exentas (Exempt sales) |
| 6 | Total ventas |
| 7 | Debito fiscal (IVA on taxable sales at 13%) |

### Credito Fiscal (Input)

| Line | Description |
|------|-------------|
| 8 | Compras internas gravadas (Domestic taxable purchases) |
| 9 | Importaciones gravadas (Taxable imports) |
| 10 | Credito fiscal por compras (Input IVA -- local) |
| 11 | Credito fiscal por importaciones (Input IVA -- imports) |
| 12 | Total credito fiscal |
| 13 | Ajustes al credito fiscal (blocked/apportioned) |
| 14 | Credito fiscal neto |

### Liquidacion

| Line | Description |
|------|-------------|
| 15 | Impuesto determinado (Line 7 - Line 14) |
| 16 | Remanente credito fiscal anterior (prior credit) |
| 17 | Retenciones y percepciones |
| 18 | Total a pagar / remanente |

---

## Step 4: IVA Retention and Perception [T1]

**Legislation:** Ley del IVA, Articles 162-162-B; Codigo Tributario, Article 162.

El Salvador has an extensive retention/perception system:

### Retention (Retencion) [T1]

| Agent Type | Retention Rate |
|------------|---------------|
| Large taxpayer purchasing from small/medium taxpayers | 1% of taxable purchase price (not of IVA) [T1] |
| Government entities | 1% of purchase price [T1] |

### Perception (Percepcion) [T1]

| Agent Type | Perception Rate |
|------------|----------------|
| Large taxpayer selling to small/medium taxpayers | 1% of taxable sale price [T1] |

### Treatment on the Return [T1]
- Retentions/perceptions credited on Line 17
- Certificates must be obtained and retained
- Large taxpayers designated by MH resolution

---

## Step 5: Reverse Charge on Imported Services [T1]

**Legislation:** Ley del IVA, Article 14-A.

When an El Salvador registered person receives services from a non-resident:

1. Self-assess IVA at 13% [T1]
2. Report as output IVA (debito fiscal) [T1]
3. Claim as input IVA (credito fiscal) if for taxable operations [T1]
4. Net effect: zero for fully taxable businesses [T1]

---

## Step 6: Deductibility Check

### Blocked Input IVA (No Recovery) [T1]

**Legislation:** Ley del IVA, Articles 65, 65-A.

- **Entertainment** -- meals, recreation (unless hospitality business) [T1]
- **Motor vehicles** -- passenger vehicles (exception: rental, taxi, transport businesses) [T1]
- **Personal use** [T1]
- **Exempt operations** -- costs attributable to exempt supplies [T1]
- **Purchases without valid Comprobante de Credito Fiscal (CCF)** [T1]

### Invoice Requirement [T1]
- B2B: Comprobante de Credito Fiscal (CCF) -- supports input IVA credit
- B2C: Factura de Consumidor Final -- does NOT support input credit for the buyer
- Input IVA only deductible with valid CCF or equivalent electronic document (DTE)

### Partial Exemption [T2]
- Direct attribution + proportional method for common costs
- `Recovery % = (Taxable Sales / Total Sales) * 100`
- Flag for reviewer

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory IVA registration | Annual taxable sales exceeding USD 5,714.29 (El Salvador uses USD) [T1] |
| Large taxpayer designation | Designated by MH resolution (typically annual revenue > USD 1,000,000) [T2] |
| Electronic invoicing (DTE) | Mandatory phased rollout [T2] |

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Codigo Tributario, Articles 238, 246, 249.

### Filing Deadlines

| Period | Deadline |
|--------|----------|
| Monthly IVA return (F-07) | 10th business day of the month following the period [T1] |
| IVA retention/perception return | 10th business day of following month [T1] |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | USD 8 per day (individuals) / USD 11 per day (companies), max 20 minimum wages [T1] |
| Late payment | 2% per month on unpaid tax (max 60%) [T1] |
| Failure to register | Fines + back-assessment [T1] |
| Failure to issue CCF/factura | Closure of business (temporary, 5-10 days) [T1] |
| Fraud | Criminal penalties; imprisonment 4-6 years [T1] |

---

## Step 9: Classification Matrix [T1]

### Domestic Purchases

| Category | IVA Rate | Input Credit | Document |
|----------|---------|--------------|----------|
| Office supplies | 13% | Yes (with CCF) | CCF |
| Commercial rent | 13% | Yes | CCF |
| Residential rent | Exempt | No | Factura |
| Electricity (commercial) | 13% | Yes | CCF |
| Telephone/internet | 13% | Yes | CCF |
| Motor car | 13% | BLOCKED | CCF |
| Entertainment | 13% | BLOCKED | CCF |
| Professional services | 13% | Yes | CCF |
| Insurance | 13% | Yes | CCF |
| Basic food | Exempt | No | N/A |
| Medicines | Exempt | No | N/A |
| Fuel | Exempt (specific tax) | No IVA | Factura |

### Sales

| Category | IVA | Return Line |
|----------|-----|-------------|
| B2B domestic (standard) | 13% | Line 2, Line 7 |
| B2C domestic | 13% | Line 3, Line 7 |
| Export | 0% | Line 4 |
| Exempt | Exempt | Line 5 |

---

## Step 10: Free Trade Zone (Zona Franca) Rules [T2]

**Legislation:** Ley de Zonas Francas Industriales y de Comercializacion.

- Free zone companies: exempt from IVA on imports for export processing
- Sales to domestic market from free zone: subject to IVA as imports
- Maquila operations: special regime, generally exempt from IVA on inputs
- Flag for reviewer: free zone benefits require valid DPA (Decreto de Promocion de Actividades) authorization

---

## Step 10a: Tax Invoice Requirements [T1]

**Legislation:** Ley del IVA; Codigo Tributario, Article 107.

### Types of Tax Documents

| Document | Code | Use | Supports IVA Credit |
|----------|------|-----|-------------------|
| Comprobante de Credito Fiscal (CCF) | - | B2B transactions | YES [T1] |
| Factura de Consumidor Final | - | B2C transactions | NO [T1] |
| Nota de Credito | - | Returns, corrections | YES (reduces IVA) [T1] |
| Nota de Debito | - | Additional charges | YES [T1] |
| Factura de Exportacion | - | Export sales | N/A (zero-rated) [T1] |
| Documento Tributario Electronico (DTE) | - | Electronic equivalent of above | Same as underlying type [T1] |

### Required Contents of CCF [T1]

1. Pre-printed text "COMPROBANTE DE CREDITO FISCAL"
2. Name, trade name, NIT, and NRC of issuer
3. Pre-printed sequential number authorized by MH
4. Date of issuance
5. Name, NIT, and NRC of buyer
6. Description of goods or services
7. Quantity and unit price
8. Taxable base (base imponible)
9. IVA amount (13%)
10. Total amount
11. Printed terms of payment (credit/cash)
12. Authorization resolution number from MH

### DTE (Electronic Invoicing) [T2]

El Salvador is implementing mandatory electronic invoicing (DTE):
- Large taxpayers: already mandatory
- Medium and small taxpayers: phased rollout
- DTE replaces paper CCF and facturas
- Must be authorized by MH digital system
- Input IVA credit valid with authorized DTE

---

## Step 10b: Sector-Specific Rules [T2]

### Agriculture

- First sale of unprocessed agricultural products by the producer: exempt [T2]
- Subsequent sales: taxable at 13% [T1]
- Agricultural inputs (seeds, fertilizers): exempt [T1]
- Veterinary services and supplies: exempt [T1]
- Processing services for agricultural products: taxable at 13% [T1]
- Flag for reviewer: "first sale by producer" exemption requires careful verification

### Manufacturing and Maquila

- Maquila operations: special regime under Ley de Servicios Internacionales
- Raw materials imported for maquila: IVA exempt [T2]
- Finished goods re-exported: zero-rated [T1]
- Domestic sales by maquila: standard 13% IVA [T1]
- Flag for reviewer: maquila license must be current and valid

### Construction and Real Estate

- Construction services: taxable at 13% [T1]
- First transfer of new real estate: taxable at 13% [T1]
- Subsequent transfers of used real estate: exempt [T2]
- Construction materials: taxable at 13% [T1]
- Architectural and engineering services: taxable at 13% [T1]

### Financial Services

- Interest on loans: exempt [T1]
- Banking fees and commissions: taxable at 13% [T1]
- Insurance premiums (life/health): exempt [T1]
- Insurance premiums (property/casualty): taxable at 13% [T1]
- Credit card fees: taxable at 13% [T1]

### Digital Economy

- Digital services from non-residents: subject to IVA at 13% via reverse charge [T2]
- Streaming, cloud computing, digital advertising: buyer self-assesses [T2]
- Flag for reviewer: digital services taxation rules may be evolving

---

## Step 10c: Libro de Compras y Ventas [T1]

**Legislation:** Codigo Tributario, Article 141.

All IVA taxpayers must maintain:

- **Libro de Ventas a Contribuyentes** -- sales to registered taxpayers (CCF)
- **Libro de Ventas a Consumidor Final** -- sales to final consumers (facturas)
- **Libro de Compras** -- all purchases with CCF details
- All books must be legalized by a public accountant (Contador Publico)
- Available for MH/DGII inspection
- Retention period: minimum 5 years
- Summary totals reconcile to F-07 return

---

## PROHIBITIONS [T1]

- NEVER let AI guess IVA classification
- NEVER allow input credit on blocked categories
- NEVER allow input credit without valid CCF or DTE
- NEVER allow input credit on Factura de Consumidor Final for B2B purchases
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse zero-rated exports with exempt supplies
- NEVER compute any number -- all arithmetic is handled by the deterministic engine

---

## Step 11: Edge Case Registry

### EC1 -- Purchase documented with Factura (not CCF) [T1]
**Situation:** Supplier issues Factura de Consumidor Final instead of CCF to a registered taxpayer.
**Resolution:** Input IVA NOT deductible. Factura does not support credito fiscal. Request CCF from supplier.

### EC2 -- Imported software from US [T1]
**Situation:** El Salvador company subscribes to US cloud service. No IVA.
**Resolution:** Self-assess IVA at 13%. Output = debito fiscal. Input = credito fiscal (if taxable operations). Net = zero.

### EC3 -- Retention by large taxpayer [T1]
**Situation:** Large taxpayer client retains 1% from small supplier's invoice.
**Resolution:** Client reports input IVA in full. Retained 1% remitted to MH. Supplier claims retention credit on Line 17.

### EC4 -- Credit notes (Nota de Credito) [T1]
**Situation:** Client issues credit note for returns.
**Resolution:** Reduce debito fiscal. Issue proper Nota de Credito. Report net.

### EC5 -- Cross-border services to Honduras [T2]
**Situation:** El Salvador company provides IT services to Honduras company.
**Resolution:** May qualify as export (zero-rated) if consumed outside El Salvador. Flag for reviewer.

### EC6 -- Real estate sale [T2]
**Situation:** Company sells commercial property.
**Resolution:** Transfer of real estate is subject to IVA at 13% (first transfer of new construction). Subsequent transfers may be exempt. Flag for reviewer.

### EC7 -- Bitcoin (digital currency) transactions [T2]
**Situation:** Client receives Bitcoin as payment for goods/services.
**Resolution:** El Salvador recognizes Bitcoin as legal tender. IVA still applies on the underlying supply of goods/services at 13%. The payment method does not affect IVA treatment. Value in USD at time of transaction. Flag for reviewer: Bitcoin accounting is evolving [T2].

### EC8 -- Agricultural first sale [T2]
**Situation:** Farmer sells unprocessed corn to wholesaler.
**Resolution:** First sale of unprocessed agricultural products may be exempt. Confirm the product qualifies and this is indeed the first sale. Flag for reviewer.

---

## Step 12: Test Suite

### Test 1 -- Standard local purchase, 13%
**Input:** SV supplier, office supplies, gross USD 1,130, IVA USD 130, net USD 1,000. Valid CCF.
**Expected output:** Line 10 = USD 130 input IVA. Full recovery.

### Test 2 -- Export, zero-rated
**Input:** Exporter ships textiles to US, net USD 50,000.
**Expected output:** Line 4 = USD 50,000. No output IVA. Input IVA fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase sedan USD 20,000, IVA USD 2,600.
**Expected output:** IVA USD 2,600 BLOCKED. No input credit.

### Test 4 -- Imported services, reverse charge
**Input:** US consultant, USD 3,000. No IVA.
**Expected output:** Self-assess output IVA = USD 390 (13%). Input = USD 390. Net = zero.

### Test 5 -- Purchase with Factura (no credit)
**Input:** Supplies purchased with Factura de Consumidor Final. IVA USD 65.
**Expected output:** IVA USD 65 NOT deductible. No CCF.

### Test 6 -- Exempt supply (medical)
**Input:** Medical clinic earns USD 10,000.
**Expected output:** Line 5 = USD 10,000. No output IVA. Input IVA on clinic costs NOT recoverable.

### Test 7 -- Large taxpayer retention
**Input:** Large taxpayer purchases USD 10,000 goods from small supplier. Retains 1% = USD 100.
**Expected output:** Input IVA = USD 1,300 (full). USD 100 retention remitted to MH separately.

### Test 8 -- Entertainment, blocked
**Input:** Client dinner USD 565 inclusive of IVA USD 65.
**Expected output:** IVA USD 65 BLOCKED. No input credit.

---

## Step 13: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed CPA must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed CPA. Document gap.
```

---

## Step 14: Additional Classification Rules [T1]

### Place of Supply Rules for Services [T2]

**Legislation:** Ley del IVA, Articles 16-17.

- Services are generally taxable where the provider is domiciled [T1]
- Exception: services related to real estate are taxable where the property is located [T1]
- Exception: services consumed abroad by non-residents may qualify as export [T2]
- Digital services: place of consumption increasingly relevant [T2]
- Flag for reviewer: place of supply for cross-border services requires analysis

### Self-Supply (Autoconsumo) [T1]

**Legislation:** Ley del IVA, Article 4.

- When a business withdraws goods for personal use or provides free services, this constitutes a taxable event [T1]
- IVA must be self-assessed on the fair market value [T1]
- Report as output IVA (debito fiscal) on the return [T1]

### Barter and Non-Monetary Transactions [T1]

- Barter (permuta) is treated as two simultaneous sales [T1]
- Each party reports the fair market value as a taxable sale [T1]
- IVA applies at 13% on each leg of the transaction [T1]

### Installment Sales [T1]

- IVA is fully due at the time of delivery, not at each payment [T1]
- The full IVA is reported as debito fiscal in the period of the sale [T1]
- Buyer can claim full credito fiscal immediately (with CCF) [T1]

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
