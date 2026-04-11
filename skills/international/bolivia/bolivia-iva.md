---
name: bolivia-iva
description: Use this skill whenever asked to prepare, review, or create a Bolivia IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "Bolivia VAT", or any request involving Bolivia value added tax filing. ALWAYS read this skill before touching any Bolivia IVA-related work.
---

# Bolivia IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Bolivia (Estado Plurinacional de Bolivia) |
| Jurisdiction Code | BO |
| Primary Legislation | Ley 843 (Ley de Reforma Tributaria), Titulo I -- IVA |
| Supporting Legislation | Decreto Supremo 21530 (Reglamento IVA); Resoluciones Normativas de Directorio (RND) del SIN |
| Tax Authority | Servicio de Impuestos Nacionales (SIN) |
| Filing Portal | https://www.impuestos.gob.bo (Oficina Virtual SIN) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires sign-off by a licensed Bolivia CPA (Auditor Financiero) |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Last Verified | April 2026 -- rates, thresholds, forms, and deadlines verified against current sources |
| Confidence Coverage | Tier 1: rate classification, return form, input recovery. Tier 2: partial exemption, hydrocarbons sector, mining, cooperative treatments. Tier 3: complex structures, rulings. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and NIT (Numero de Identificacion Tributaria)** [T1]
2. **Tax regime** [T1] -- Regimen General, Regimen Simplificado (RSI), Regimen Agropecuario Unificado (RAU), or STI
3. **Filing period** [T1] -- monthly (standard)
4. **Industry/sector** [T2] -- mining, hydrocarbons, agriculture, services
5. **Does the business make exempt supplies?** [T2]
6. **Does the business import goods?** [T1]
7. **Credit balance brought forward** [T1]

**If items 1-3 are unknown, STOP.**

---

## Step 1: IVA Rate Structure [T1]

**Legislation:** Ley 843, Article 15.

### Standard Rate

| Rate | Application |
|------|-------------|
| 13% | Single rate on all taxable sales of goods, works, services, and imports [T1] |

**Important note on the 13% rate:** Bolivia's IVA is unique in that the 13% is applied as a "tax-inclusive" rate. The stated price is considered to INCLUDE IVA. This means the effective tax on the net amount is approximately 14.94% (13/87). However, for return reporting purposes, the IVA is calculated as 13% of the gross/inclusive price. [T1]

### No Reduced Rates [T1]
Bolivia does NOT have reduced IVA rates. The single rate of 13% applies to all taxable transactions.

### Exempt Supplies [T1]

**Legislation:** Ley 843, Article 2; Decreto Supremo 21530.

**Exempt goods:**
- Agricultural products in their natural state (sold by original producer under RAU)
- Books, newspapers, magazines (national production)
- Precious metals (gold -- specific transactions with Central Bank)

**Exempt services:**
- Financial intermediation services (interest on deposits, certain banking operations)
- Educational services (public and authorized private)
- Health services (public health system)
- Diplomatic and consular services
- International transport (covered by international agreements)

**Note:** Bolivia has a relatively narrow list of exemptions compared to other Latin American countries. Most goods and services are taxable at 13%.

### Exports (0% -- Full Input Credit) [T1]
- Export of goods: zero-rated with full input credit recovery
- Export of services: certain services consumed outside Bolivia [T2]

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (debito fiscal -- output) or Purchase (credito fiscal -- input)
- Salaries, AFP contributions (pension), health insurance contributions, loans, dividends = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (Bolivia)
- CAN (Comunidad Andina): Colombia, Ecuador, Peru
- MERCOSUR associate
- International

### 2c. Determine IVA Rate [T1]
- 0% (export) or 13% (standard, inclusive), or exempt
- No intermediate rates

### 2d. IVA Calculation Method [T1]
- **IVA = Gross price x 13%** (tax-inclusive method)
- Net amount = Gross price x 87%
- This is different from most countries where IVA = Net x rate

---

## Step 3: IVA Return Form Structure (Formulario 200/210) [T1]

**Filed monthly via Oficina Virtual SIN.**

### Debito Fiscal (Output)

| Line | Description |
|------|-------------|
| 1 | Ventas gravadas del periodo (Taxable sales, gross amounts) |
| 2 | Debito fiscal (Line 1 x 13%) |
| 3 | Exportaciones (Exports at 0%) |
| 4 | Ventas no gravadas / exentas |
| 5 | Total ventas |

### Credito Fiscal (Input)

| Line | Description |
|------|-------------|
| 6 | Compras gravadas del periodo (Taxable purchases, gross amounts) |
| 7 | Credito fiscal (Line 6 x 13%) |
| 8 | Compras no gravadas |
| 9 | Importaciones gravadas |
| 10 | Credito fiscal por importaciones |
| 11 | Total credito fiscal (Line 7 + Line 10) |

### Liquidacion

| Line | Description |
|------|-------------|
| 12 | Diferencia (Line 2 - Line 11) |
| 13 | Saldo a favor del periodo anterior |
| 14 | Actualizacion de saldo a favor (UFV adjustment) |
| 15 | Total saldo a favor |
| 16 | Impuesto a pagar / saldo a favor |

---

## Step 4: IT (Impuesto a las Transacciones) Interaction [T1]

**Legislation:** Ley 843, Titulo VI.

Bolivia also has the IT (Impuesto a las Transacciones) at 3% on gross revenue. Key interaction:

- IVA (debito fiscal) can be used as credit against IT
- IT is a separate return (Formulario 400) but IVA debito fiscal is creditable
- This is a unique feature of the Bolivian tax system
- The IVA paid (debito fiscal) reduces the effective IT burden

**This interaction is OUT OF SCOPE of this IVA skill but critical to understand. [T3]**

---

## Step 5: Reverse Charge on Imported Services [T1]

**Legislation:** Ley 843, Article 1; Decreto Supremo 21530.

When a Bolivia registered person receives services from a non-resident:

1. Self-assess IVA at 13% on the gross value [T1]
2. Report as debito fiscal [T1]
3. Claim as credito fiscal if for taxable operations [T1]
4. Net = zero for fully taxable businesses [T1]

---

## Step 6: Deductibility Check

### Blocked Input IVA (No Recovery) [T1]

**Legislation:** Ley 843, Article 8; Decreto Supremo 21530, Article 8.

- **Motor vehicles** -- passenger vehicles not used directly in the business activity [T1]
- **Entertainment** -- meals, recreation not directly related to business [T1]
- **Personal use** -- any goods/services for personal consumption [T1]
- **Exempt operations** -- costs attributable to exempt revenues [T1]
- **Purchases without valid factura (nota fiscal)** -- critically important in Bolivia [T1]

### Nota Fiscal (Fiscal Invoice) Requirement [T1]

**Legislation:** RND 10-0021-16; Ley 843.

Bolivia has a unique system for fiscal invoices:

- All invoices must be authorized by SIN (dosificacion)
- Invoices must contain: NIT, razon social, NIT of buyer, numero de autorizacion, fecha limite de emision
- **Facturas must include the buyer's NIT and name** -- invoices without buyer NIT are NOT valid for credito fiscal [T1]
- Expired facturas (past fecha limite de emision) are NOT valid for credito fiscal [T1]
- Electronic invoicing (Facturacion Electronica en Linea -- FEL) is being implemented
- EVERY factura has a dosificacion number and must be verifiable on the SIN website

### Nota Fiscal Validation Rules [T1]
- Check NIT of supplier is valid and active
- Check numero de autorizacion against SIN database
- Check fecha limite de emision has not passed
- Check buyer NIT is correctly printed
- If ANY of these fail: credito fiscal is LOST

### Partial Exemption [T2]
- Direct attribution + proportional
- Flag for reviewer

---

## Step 7: UFV Adjustment [T1]

**Legislation:** Ley 843; Codigo Tributario.

Bolivia uses the UFV (Unidad de Fomento de la Vivienda) for inflation adjustment:

- Tax credits carried forward are adjusted by UFV variation
- UFV is published daily by the Central Bank
- The adjustment (maintenance of value) applies to credit balances
- This is unique to Bolivia and ensures credits maintain real value

---

## Step 8: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Regimen General | All businesses above simplified thresholds |
| Regimen Simplificado (RSI) | Artisans, small traders with limited capital (below BOB 60,000 annual capital) |
| RAU (Agricultural) | Agricultural producers -- pay a fixed annual amount instead of IVA + IT + IUE |

**Legislation:** Ley 843; DS 24484 (RSI); DS 24463 (RAU).

---

## Step 9: Filing Deadlines and Penalties [T1]

**Legislation:** Codigo Tributario, Ley 2492.

### Filing Deadlines [T1]

Filing date depends on the last digit of the NIT:

| Last Digit of NIT | Due Date (of following month) |
|-------------------|-------------------------------|
| 0 | 13th |
| 1 | 14th |
| 2 | 15th |
| 3 | 16th |
| 4 | 17th |
| 5 | 18th |
| 6 | 19th |
| 7 | 20th |
| 8 | 21st |
| 9 | 22nd |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | 100 UFV per month (late filing fine) [T1] |
| Late payment | Interest at rate published by Central Bank + maintenance of value (UFV) [T1] |
| Failure to register | Fines + back-assessment + potential criminal [T1] |
| Failure to issue nota fiscal | 6,000 UFV fine per instance + potential closure [T1] |
| Fraud (defraudacion) | Criminal: 3-6 years imprisonment + fines [T1] |
| Omission (omision de pago) | 100% of tax omitted + interest [T1] |

---

## Step 10: Classification Matrix [T1]

### Domestic Purchases

| Category | IVA | Input Credit | Notes |
|----------|-----|--------------|-------|
| Office supplies | 13% (inclusive) | Yes (with nota fiscal) | |
| Commercial rent | 13% (inclusive) | Yes | |
| Residential rent | Exempt | No | |
| Electricity (commercial) | 13% (inclusive) | Yes | |
| Telephone/internet | 13% (inclusive) | Yes | |
| Motor car | 13% (inclusive) | BLOCKED | |
| Entertainment | 13% (inclusive) | BLOCKED | |
| Professional services | 13% (inclusive) | Yes | |
| Insurance | 13% (inclusive) | Yes | |
| Books (national) | Exempt | No | |

### Sales

| Category | IVA | Return Line |
|----------|-----|-------------|
| Domestic sale | 13% (inclusive) | Line 1, Line 2 |
| Export | 0% | Line 3 |
| Exempt | Exempt | Line 4 |

---

## Step 11: Mining and Hydrocarbons [T2]

**Legislation:** Ley 3787 (Mining); Ley 3058 (Hydrocarbons).

- Mining companies: IVA applies to domestic sales. Exports zero-rated. Input IVA on mining inputs recoverable.
- Hydrocarbons: IVA at 13% applies. YPFB and licensed operators have specific compliance requirements.
- Both sectors have additional sector-specific taxes outside IVA scope.
- Flag for reviewer: mining/hydrocarbons transactions require specialist review [T3]

---

## Step 11a: Nota Fiscal System Details [T1]

### Types of Notas Fiscales

| Document | Use | Supports Credito Fiscal |
|----------|-----|------------------------|
| Factura | Standard sales | YES (with buyer NIT) [T1] |
| Nota Fiscal de Compra-Venta | Simplified sale | YES (with buyer NIT) [T1] |
| Recibo de Alquiler | Rental receipts | YES [T1] |
| Nota de Credito-Debito | Adjustments | YES (reduces/increases IVA) [T1] |
| Factura Comercial de Exportacion | Export sales | N/A (zero-rated) [T1] |
| Factura de Zona Franca | Free zone operations | Varies [T2] |

### Dosificacion System [T1]

Bolivia's unique dosificacion system:
1. Each nota fiscal series must be authorized by SIN (dosificacion)
2. The dosificacion provides: NIT, numero de autorizacion, fecha limite de emision
3. Every factura has a codigo de control (verification code) generated by SIN algorithm
4. Verification: buyers can verify any nota fiscal on the SIN website
5. Notas fiscales past their fecha limite de emision are INVALID

### FEL (Facturacion Electronica en Linea) [T2]

Bolivia is implementing electronic invoicing:
- Phased rollout based on taxpayer classification
- Real-time authorization by SIN system
- Replaces paper dosificacion system
- Digital signature required
- Flag for reviewer: confirm client's FEL obligation status

---

## Step 11b: Sector-Specific Rules [T2]

### Mining

- Domestic sales of minerals: IVA at 13% [T1]
- Exports of minerals: zero-rated with full credito fiscal recovery [T1]
- Mining inputs (explosives, machinery, chemicals): IVA at 13%, credito fiscal available [T1]
- Cooperatives mineras: may have special IVA treatment [T2]
- ICM (Impuesto Complementario a la Mineria): separate from IVA [T3]

### Agriculture

- Agricultural producers under RAU: do NOT charge IVA [T1]
- Agricultural products sold by non-RAU taxpayers: IVA at 13% [T1]
- Agricultural inputs: IVA at 13% (credito fiscal available for general regime taxpayers) [T1]
- Exports of agricultural products: zero-rated [T1]
- Quinoa, soy, coffee exports: zero-rated [T1]

### Construction and Real Estate

- Construction services: IVA at 13% [T1]
- Sale of new real estate: IVA at 13% on the construction value (land excluded) [T2]
- Rental of real estate: IVA at 13% [T1]
- Residential rental (low value): may be exempt under certain conditions [T2]

### Financial Services

- Interest on deposits: exempt [T1]
- Banking commissions and fees: IVA at 13% [T1]
- Insurance premiums: IVA at 13% [T1]
- Leasing: IVA at 13% on each payment [T1]

### Telecommunications

- All telecom services: IVA at 13% [T1]
- Internet services: IVA at 13% [T1]

### Gas and Hydrocarbons

- Domestic sale of natural gas: IVA at 13% [T1]
- Export of natural gas: zero-rated [T1]
- YPFB operations: complex, multiple taxes apply [T3]

---

## Step 11c: IT-IVA Credit Mechanism Details [T2]

**Legislation:** Ley 843, Titulo VI.

The interaction between IVA and IT (Impuesto a las Transacciones) is unique to Bolivia:

1. IT = 3% on gross revenue (all transactions)
2. IVA debito fiscal paid in a period can be used as credit against IT of the same period
3. If IVA debito > IT liability: excess IVA credit is lost (cannot be carried forward for IT purposes)
4. If IVA debito < IT liability: IT is reduced by the IVA debito amount

**Example:** Company has IVA debito of BOB 13,000 and IT liability of BOB 9,000.
- IT payable = BOB 9,000 - BOB 9,000 (IVA credit, limited to IT amount) = BOB 0
- Excess IVA debito of BOB 4,000 not usable for IT (but still functions normally for IVA purposes)

**Flag for reviewer: this interaction should be reviewed by a licensed CPA to ensure proper application.**

---

## Step 11d: Libro de Compras y Ventas IVA [T1]

**Legislation:** DS 21530; RND SIN.

All IVA taxpayers must maintain:

- **Libro de Compras IVA**: purchases with nota fiscal number, NIT of supplier, autorizacion number, date, monto (total inclusive amount), credito fiscal (13%)
- **Libro de Ventas IVA**: sales with nota fiscal number, NIT of buyer (or "Sin Nombre" for B2C), autorizacion, date, monto, debito fiscal
- Monthly format submitted electronically to SIN (via portal or FACILITO software)
- Summary totals reconcile to Formulario 200
- Retention: minimum 8 years (prescripcion tributaria)
- SIN cross-matches purchase/sales ledgers between taxpayers

---

## PROHIBITIONS [T1]

- NEVER let AI guess IVA classification
- NEVER allow input credit without valid nota fiscal (with buyer NIT, valid autorizacion, unexpired fecha limite)
- NEVER allow input credit on blocked categories
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse the tax-inclusive 13% method with the standard exclusive method used in other countries
- NEVER forget the UFV adjustment on carried-forward credits
- NEVER allow RSI or RAU taxpayers to claim/charge IVA (they are in substitute regimes)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine

---

## Step 12: Edge Case Registry

### EC1 -- Nota fiscal without buyer NIT [T1]
**Situation:** Supplier issues factura but omits the buyer's NIT.
**Resolution:** Credito fiscal LOST. The factura is NOT valid for IVA credit purposes. Must request corrected factura with NIT included.
**Legislation:** DS 21530, Article 8.

### EC2 -- Expired nota fiscal [T1]
**Situation:** Supplier issues factura past the fecha limite de emision.
**Resolution:** Credito fiscal LOST. Expired facturas cannot be used for IVA credit.

### EC3 -- Imported software [T1]
**Situation:** Bolivia company subscribes to US cloud service. No IVA.
**Resolution:** Self-assess IVA at 13% (inclusive basis). Output and input. Net = zero.

### EC4 -- Credit notes [T1]
**Situation:** Client issues nota de credito-debito.
**Resolution:** Reduce debito fiscal. Valid nota fiscal required. Report net.

### EC5 -- IVA-IT credit interaction [T2]
**Situation:** Company has IVA debito fiscal of BOB 10,000. IT liability of BOB 3,000.
**Resolution:** IVA debito fiscal can be credited against IT. This reduces IT payable. However, this is an IT return calculation, not an IVA return item. Flag for reviewer: ensure proper IT credit application.

### EC6 -- RAU taxpayer selling products [T1]
**Situation:** Agricultural producer under RAU sells wheat.
**Resolution:** RAU taxpayers do NOT charge IVA. They pay a flat annual tax instead. Buyers cannot claim IVA credit on RAU purchases.

### EC7 -- UFV adjustment on credit balance [T1]
**Situation:** Company carries forward IVA credit of BOB 5,000 from prior period.
**Resolution:** Adjust by UFV variation between filing dates. Report adjusted amount on Line 14.

### EC8 -- Donation of goods [T1]
**Situation:** Company donates goods to charity.
**Resolution:** Donation is treated as a taxable transfer for IVA purposes. Debito fiscal applies on the fair market value. No credito fiscal recovery reversal required if IVA was originally claimed on the goods.
**Legislation:** Ley 843, Article 2.

---

## Step 13: Test Suite

### Test 1 -- Standard local purchase, 13% (inclusive)
**Input:** BO supplier, office supplies, gross BOB 1,000. IVA = BOB 130 (13% of 1,000). Valid nota fiscal with buyer NIT.
**Expected output:** Line 7 = BOB 130 credito fiscal. Full recovery.

### Test 2 -- Export, zero-rated
**Input:** Exporter ships tin to US, FOB USD 50,000 (~ BOB 345,000).
**Expected output:** Line 3 = BOB 345,000. No debito fiscal. Credito fiscal fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase sedan BOB 120,000. IVA = BOB 15,600.
**Expected output:** IVA BOB 15,600 BLOCKED. No credito fiscal.

### Test 4 -- Imported services, reverse charge
**Input:** US consulting, USD 2,000 (~ BOB 13,800). No IVA.
**Expected output:** Self-assess debito fiscal = BOB 1,794 (13%). Credito fiscal = BOB 1,794. Net = zero.

### Test 5 -- Nota fiscal without buyer NIT
**Input:** Purchase BOB 5,000. Nota fiscal missing buyer NIT. IVA = BOB 650.
**Expected output:** IVA BOB 650 NOT creditable. Invalid nota fiscal.

### Test 6 -- Exempt supply (education)
**Input:** School earns BOB 100,000 from tuition.
**Expected output:** Line 4 = BOB 100,000. No debito fiscal. Credito fiscal NOT recoverable.

### Test 7 -- UFV credit adjustment
**Input:** Credit carried forward BOB 5,000. UFV variation = 0.5% for the period.
**Expected output:** Adjusted credit = BOB 5,025. Report on Line 14.

### Test 8 -- Entertainment, blocked
**Input:** Client dinner BOB 500 inclusive of IVA BOB 65.
**Expected output:** IVA BOB 65 BLOCKED. No credito fiscal.

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
