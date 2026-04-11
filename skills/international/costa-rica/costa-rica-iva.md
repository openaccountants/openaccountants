---
name: costa-rica-iva
description: Use this skill whenever asked to prepare, review, or create a Costa Rica IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "declaracion de IVA", "Costa Rica VAT", "ATV filing", "Ministerio de Hacienda", "factura electronica", or any request involving Costa Rican IVA filing. Also trigger when classifying transactions for IVA purposes from bank statements, invoices, or other source data. This skill contains the complete Costa Rica IVA classification rules, form D-104 mappings, four-rate structure (13%/4%/2%/1%), deductibility rules, electronic invoicing requirements, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any IVA-related work for Costa Rica.
---

# Costa Rica IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Costa Rica |
| Jurisdiction Code | CR |
| Primary Legislation | Ley de Fortalecimiento de las Finanzas Publicas (Ley 9635, December 2018) -- Title I: Impuesto al Valor Agregado |
| Supporting Legislation | Reglamento a la Ley 9635 (Decreto Ejecutivo 41779-H); Resolucion DGT-R-012-2018 (electronic invoicing); Ley 4755 Codigo de Normas y Procedimientos Tributarios |
| Tax Authority | Ministerio de Hacienda -- Direccion General de Tributacion (DGT) |
| Filing Portal | https://www.hacienda.go.cr (ATV -- Administracion Tributaria Virtual; transitioning to Tribu-CR from late 2025) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, form D-104 mapping, filing periods, electronic invoicing triggers. Tier 2: partial credit (prorrata), transitional rules from sales tax to IVA, sector-specific exemptions. Tier 3: complex international services, special regimes (free trade zones -- ZF), real estate transactions. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed Contador Publico Autorizado must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed Contador Publico Autorizado and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and cedula juridica/fisica** [T1] -- legal entity number (cedula juridica) or individual ID (cedula fisica)
2. **Tax registration number (NIT)** [T1] -- registered with Ministerio de Hacienda
3. **Taxpayer type** [T1] -- Contribuyente (registered taxpayer) or not registered
4. **IVA regime** [T1] -- Regimen Tradicional (standard) or Regimen Simplificado (simplified for small taxpayers)
5. **Filing period** [T1] -- Monthly (standard for all IVA taxpayers)
6. **Industry/sector** [T2] -- impacts applicable rate (health, education, basic goods)
7. **Does the business make exempt supplies?** [T2] -- If yes, proportional credit (prorrata) required
8. **Is the client registered for electronic invoicing?** [T1] -- mandatory for all taxpayers
9. **Does the client export goods or services?** [T1] -- exporters have zero-rated treatment with credit right
10. **Does the client provide services subject to reduced rates?** [T2] -- health (4%), education supplies/pharma (2%), basic basket (1%)

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until registration status is confirmed.**

---

## Step 1: IVA Rate Classification Rules

### 1a. Standard Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 13% | General rate on all taxable goods and services not specifically assigned another rate | Ley 9635, Art. 10 |

**Legislation:** Ley 9635, Article 10. The general IVA rate is 13%.

### 1b. Reduced Rate -- 4% [T1]

| Application | Legislation |
|-------------|-------------|
| Private health services (medical, dental, laboratory, imaging, hospital) | Ley 9635, Art. 11(a) |
| Tickets for cultural, sporting, and recreational events | Ley 9635, Art. 11(a) |
| Private education services (preschool, primary, secondary, university) -- fees and tuition | Ley 9635, Art. 11(a) |

### 1c. Reduced Rate -- 2% [T1]

| Application | Legislation |
|-------------|-------------|
| Essential pharmaceutical products (medicines in the CCSS list -- Caja Costarricense de Seguro Social) | Ley 9635, Art. 11(b) |
| Inputs and raw materials for agricultural production (seeds, fertilizers, agrochemicals) | Ley 9635, Art. 11(b) |
| Veterinary services | Ley 9635, Art. 11(b) |
| Supplies for formal education (school supplies, uniforms) | Ley 9635, Art. 11(b) |
| Primas de seguro personales (personal insurance -- life, medical) | Ley 9635, Art. 11(b) |

### 1d. Reduced Rate -- 1% [T1]

| Application | Legislation |
|-------------|-------------|
| Goods in the Canasta Basica Tributaria (basic basket -- essential food and household items defined by Ministerio de Hacienda) | Ley 9635, Art. 11(c) |

**The Canasta Basica Tributaria is a specific list of goods published by the Ministerio de Hacienda. Only items on this list qualify for the 1% rate. All other food items are at 13% or exempt.**

### 1e. Zero-Rated (Exento con derecho a credito) [T1]

| Category | Legislation |
|----------|-------------|
| Exports of goods | Ley 9635, Art. 8(1)(a) |
| Services provided from Costa Rica and used exclusively abroad | Ley 9635, Art. 8(1)(b) |
| Sales to Free Trade Zones (Zonas Francas) | Ley 9635, Art. 8(1)(c) |
| International transport of goods and passengers | Ley 9635, Art. 8(1)(d) |

**Key distinction:** Zero-rated suppliers CAN recover input IVA (credito fiscal).

### 1f. Exempt Supplies (Exento sin credito) [T1]

| Category | Legislation |
|----------|-------------|
| Residential rent up to 1.5 base salary (salario base) per month | Ley 9635, Art. 8(2)(a) |
| Public education (CCSS, MEP -- public schools, universities) | Ley 9635, Art. 8(2)(b) |
| Health services provided by CCSS (public health system) | Ley 9635, Art. 8(2)(c) |
| Financial services (interest on loans, commissions) | Ley 9635, Art. 8(2)(d) |
| Public transport (buses, trains -- regulated routes) | Ley 9635, Art. 8(2)(e) |
| Sale of goods and services by the State (certain) | Ley 9635, Art. 8(2) |
| Residential electricity and water (first consumption blocks -- subsidized tiers) | Ley 9635, Art. 8(2)(f) |
| Cooperatives (certain agricultural cooperatives) | Ley 9635, Art. 8(2) |
| Basic food items explicitly listed as exempt (distinct from Canasta Basica at 1%) | Ley 9635, Art. 8(2) |
| Wheelchairs, prosthetics, and disability aids | Ley 9635, Art. 8(2) |
| Books and cultural publications | Ley 9635, Art. 8(2) |

### 1g. Not Subject to IVA (No Sujeto) [T1]

| Category | Notes |
|----------|-------|
| Salaries and wages | Employment income |
| Dividends | Capital distribution |
| Loan repayments (principal) | Financial transaction |
| Government taxes and fees (tributos) | Not commercial activity |
| Donations (certain) | Conditions apply |
| Sale of a going concern (traspaso de negocio) | Specific conditions |

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]

- Sale (IVA debito fiscal / output IVA) or Purchase (IVA credito fiscal / input IVA)
- Salaries, cargas sociales (CCSS employer contributions), tax payments, loan repayments = OUT OF SCOPE
- **Legislation:** Ley 9635, Art. 1 (taxable events: sale of goods, rendering of services, import of goods, import of services, cross-border digital services)

### 2b. Determine Counterparty Location [T1]

- Costa Rica (domestic): supplier/customer country is CR
- Central American Common Market (MCCA): Guatemala, El Salvador, Honduras, Nicaragua -- common customs treatment
- International: all other countries

### 2c. Determine IVA Rate [T1]

- Calculate from amounts: `rate = iva_amount / base_amount * 100`
- Normalize to nearest standard rate: 0%, 1%, 2%, 4%, 13%
- If rate does not match, flag for review [T2]

### 2d. Determine Document Type [T1]

| Document | Usage | IVA Credit |
|----------|-------|------------|
| Factura Electronica | B2B and B2C standard invoice | Yes (B2B) |
| Tiquete Electronico | Small B2C transactions | No credito fiscal for buyer |
| Nota de Credito Electronica | Credit note (reversal/adjustment) | Adjusts credito fiscal |
| Nota de Debito Electronica | Debit note (additional charges) | Adjusts credito fiscal |
| Factura Electronica de Compra | Buyer-issued invoice for specific cases | Yes (conditions) |
| Factura Electronica de Exportacion | Export invoice | Zero-rated documentation |

---

## Step 3: Form D-104 Mapping (Declaracion del IVA) [T1]

**Legislation:** Ley 9635; Ministerio de Hacienda ATV portal; Form D-104 instructions.

### Output IVA (Debito Fiscal)

| Section | Description | Rate |
|---------|-------------|------|
| Ventas gravadas al 13% | Taxable sales at standard rate | 13% |
| Ventas gravadas al 4% | Taxable sales at reduced rate (health/education) | 4% |
| Ventas gravadas al 2% | Taxable sales at reduced rate (pharma/agro/education supplies) | 2% |
| Ventas gravadas al 1% | Taxable sales (canasta basica) | 1% |
| Ventas exentas/no sujetas | Exempt and zero-rated sales | 0% |
| Exportaciones | Export sales | 0% (with credit) |
| Total debito fiscal | Sum of all output IVA | calculated |

### Input IVA (Credito Fiscal)

| Section | Description |
|---------|-------------|
| Compras con derecho a credito al 13% | Purchases at 13% for taxable activity |
| Compras con derecho a credito al 4% | Purchases at 4% |
| Compras con derecho a credito al 2% | Purchases at 2% |
| Compras con derecho a credito al 1% | Purchases at 1% |
| Importaciones | IGV on imports |
| Total credito fiscal | Sum of all input IVA |

### Balance and Payment

| Section | Description |
|---------|-------------|
| IVA determinado | Debito fiscal minus credito fiscal |
| Credito de periodos anteriores | Carried forward credit from prior periods |
| IVA a pagar | Tax payable |
| Saldo a favor | Credit balance (carried forward) |

---

## Step 4: Credito Fiscal (Input IVA) Rules [T1]

**Legislation:** Ley 9635, Art. 14-17.

### Requirements for Valid Credito Fiscal [T1]

| Requirement | Detail | Legislation |
|-------------|--------|-------------|
| Valid electronic invoice | Must be a Factura Electronica (not Tiquete Electronico) | Ley 9635, Art. 17 |
| Related to taxable activity | Expense must have direct nexus to IVA-generating activity | Ley 9635, Art. 14 |
| Registered in purchase ledger | Must be recorded in the period | Ley 9635, Art. 17 |
| IVA shown separately | IVA must be discriminated on the invoice | Ley 9635, Art. 17 |
| Supplier registered | Supplier must be a registered taxpayer | Ley 9635, Art. 17 |

### Rate Matching Rule (Tope de Credito Fiscal) [T1]

**Legislation:** Ley 9635, Art. 15.

| Rule | Detail |
|------|--------|
| General principle | Credito fiscal is limited to the IVA rate applicable to the taxpayer's sales |
| Example: Client sells at 4% | Input IVA at 13% is ONLY recoverable up to 4% (the difference is a cost) |
| Example: Client sells at 13% | Input IVA at 13% is fully recoverable |
| Example: Client sells at 1% | Input IVA at 13% is only recoverable up to 1% |
| Exporters (0% with credit) | Input IVA at 13% is fully recoverable (special export treatment) |

### Rate Matching Calculation [T1]

```
IF sale_rate >= purchase_rate THEN
    credito_fiscal = full input IVA
ELSE
    credito_fiscal = base * sale_rate
    non_recoverable = input_IVA - credito_fiscal (becomes cost)
END
```

### Items Where Credito Fiscal is NOT Allowed [T1]

| Category | Legislation | Notes |
|----------|-------------|-------|
| Purchases supported only by Tiquete Electronico | Ley 9635, Art. 17 | Tiquetes do not give right to credito fiscal |
| Purchases not related to taxable activity | Ley 9635, Art. 14 | Personal use, non-business |
| Vehicles for personal transport (sedans, SUVs) | Ley 9635, Art. 14 | Exception: vehicles essential to business (freight, taxis, rental) |
| Entertainment and personal consumption | Ley 9635, Art. 14 | Not business-related |
| Purchases for exempt-only activity | Ley 9635, Art. 14 | No credit on inputs for exempt supplies |
| Purchases exceeding the sale rate (excess) | Ley 9635, Art. 15 | Excess becomes cost |

---

## Step 5: Proportional Credito Fiscal (Prorrata) [T2]

**Legislation:** Ley 9635, Art. 16; Reglamento, Art. 24.

### When It Applies [T2]
When a taxpayer makes both taxable (gravadas) and exempt (exentas) sales, credito fiscal on common expenses must be apportioned.

### Calculation [T2]

```
Proportion % = (Taxable Sales / Total Sales) * 100
Deductible Credito Fiscal (common) = Common Input IVA * Proportion %
```

| Expense Type | Treatment |
|-------------|-----------|
| Exclusively for taxable sales | 100% credito fiscal (subject to rate matching) |
| Exclusively for exempt sales | 0% credito fiscal |
| Common/shared expenses | Proportional (prorrata) then rate matching |

**Flag for reviewer: prorrata calculation must be confirmed by Contador Publico Autorizado before applying.**

---

## Step 6: Electronic Invoicing (Facturacion Electronica) [T1]

**Legislation:** Resolucion DGT-R-012-2018; Ley 9635, Art. 28; Decreto Ejecutivo 41820-H.

### Mandatory Requirements [T1]

| Requirement | Detail |
|-------------|--------|
| Who must issue | ALL registered taxpayers (mandatory since 2019 -- phased rollout completed) |
| Format | XML format per Ministerio de Hacienda specifications (based on UBL) |
| Validation | Real-time validation by Ministerio de Hacienda system (Comprobantes Electronicos) |
| Clave numerica | 50-digit unique key for each document |
| Consecutivo | Consecutive number within authorized range |
| Delivery | Must be sent to buyer electronically (email or platform) |
| Buyer acceptance | Buyer has 8 business days to accept, partially accept, or reject |
| Storage | Minimum 4 years (Codigo de Normas y Procedimientos Tributarios, Art. 109) |

### Document Codes [T1]

| Code | Document | Usage |
|------|----------|-------|
| 01 | Factura Electronica | Standard invoice (B2B and B2C) |
| 02 | Nota de Debito Electronica | Additional charges |
| 03 | Nota de Credito Electronica | Reversals/adjustments |
| 04 | Tiquete Electronico | Small B2C transactions |
| 08 | Factura Electronica de Compra | Buyer-issued for specific cases |
| 09 | Factura Electronica de Exportacion | Export invoice |

### Acceptance Messages [T1]

| Code | Message | Meaning |
|------|---------|---------|
| 1 | Aceptado | Buyer accepts fully |
| 2 | Aceptado Parcialmente | Buyer accepts with conditions |
| 3 | Rechazado | Buyer rejects |

**A Factura Electronica with acceptance code 1 or 2 is valid for credito fiscal. Code 3 (rejected) invalidates the document.**

---

## Step 7: IVA on Imports [T1]

**Legislation:** Ley 9635, Art. 3(c); Art. 12.

### Import of Goods [T1]

| Element | Detail |
|---------|--------|
| Taxable event | Import of goods into Costa Rican territory |
| Tax base | CIF value + customs duties (DAI) + selective consumption tax (if applicable) |
| Rate | 13% (standard) or reduced rate if goods qualify |
| Collection | IVA collected by Servicio Nacional de Aduanas at import |
| Document | DUA (Declaracion Unica Aduanera) |
| Deductibility | IVA on imports deductible as credito fiscal (subject to rate matching) |

### Import of Services [T1]

**Legislation:** Ley 9635, Art. 3(d); Art. 12.

| Element | Detail |
|---------|--------|
| Taxable event | Services provided from abroad and used/consumed in Costa Rica |
| Tax base | Total amount paid for the service |
| Rate | 13% (or applicable reduced rate) |
| Mechanism | Buyer self-assesses IVA (reverse charge -- "IVA por servicios transfronterizos") |
| Filing | Declared and paid via Form D-104 |
| Deductibility | Self-assessed IVA is simultaneously deductible (net zero for fully taxable businesses at 13%) |

### Cross-Border Digital Services [T1]

**Legislation:** Ley 9635, Art. 3(e); Decreto Ejecutivo 43198-H.

| Element | Detail |
|---------|--------|
| What | Digital services provided by non-resident entities to Costa Rican consumers |
| Examples | Streaming (Netflix, Spotify), cloud services, digital advertising, apps |
| Mechanism | Foreign providers must register with Ministerio de Hacienda and charge IVA |
| Rate | 13% |
| Collection | Via credit card intermediaries if provider is not registered |

---

## Step 8: Transitional Rules (Sales Tax to IVA) [T2]

**Legislation:** Ley 9635, Transitorios.

### Background [T1]
Before Ley 9635 (effective July 1, 2019), Costa Rica had a 13% General Sales Tax (Impuesto General sobre las Ventas -- IGV) that applied only to goods and certain services. Ley 9635 replaced this with a broad-based IVA covering goods AND services.

### Key Differences [T2]

| Aspect | Old Sales Tax (IGV) | New IVA (Ley 9635) |
|--------|---------------------|---------------------|
| Scope | Goods + limited services | Goods + ALL services |
| Rate | 13% (single rate) | 13% + 4% + 2% + 1% (multiple rates) |
| Services | Most services exempt | Most services taxable (at various rates) |
| Credito fiscal | Limited | Broader (but with rate matching rule) |
| Financial services | Not taxed | Exempt (no IVA) |
| Health services | Not taxed | 4% (private) or exempt (CCSS public) |

**Flag for reviewer:** Transitional issues may still arise for contracts spanning the July 2019 changeover, inventory in transit, and credit balances from the old sales tax regime.

---

## Step 9: Free Trade Zones (Zonas Francas) [T2]

**Legislation:** Ley 7210 (Ley de Zonas Francas); Ley 9635, Art. 8(1)(c).

### IVA Treatment [T2]

| Transaction | Treatment |
|-------------|-----------|
| Sales from Costa Rica to ZF company | Zero-rated (exento con credito) -- treated as export |
| Purchases by ZF company from Costa Rica | ZF company does not pay IVA (tax-free import) |
| Sales from ZF to Costa Rica (nacionalizacion) | IVA at import (treated as import) |
| Sales between ZF companies | No IVA |
| Exports from ZF abroad | No IVA (already outside customs territory) |

**Flag for reviewer:** Free Trade Zone transactions require specific documentation and customs procedures. Confirm the ZF company's registry status and applicable benefits with Contador Publico Autorizado.

---

## Step 10: Filing Deadlines [T1]

**Legislation:** Ley 9635, Art. 27; Codigo de Normas y Procedimientos Tributarios.

### Standard Filing [T1]

| Period | Filing Deadline | Notes |
|--------|----------------|-------|
| Monthly | 15th of the following month | All registered IVA taxpayers |
| Payment | Same as filing deadline (15th) | Payment concurrent with filing |

**Unlike many Latin American countries, Costa Rica uses a fixed date (15th) rather than a CUIT/RUC-based sliding schedule.**

### Filing Methods [T1]

| Method | Detail |
|--------|--------|
| ATV / Tribu-CR portal | Form D-104 filed electronically via ATV (Administracion Tributaria Virtual) or its replacement Tribu-CR (rollout began October 2025). Electronic Invoice 4.4 mandatory from September 2026. |
| Bank payment | Payment through authorized banking platforms (conectividad bancaria) |

### Late Filing Penalties [T1]

| Penalty | Calculation | Legislation |
|---------|-------------|-------------|
| Late filing surcharge | 1% of tax per month, up to 20% | CNPT, Art. 78 |
| Late payment interest | Monthly interest rate set by Ministerio de Hacienda | CNPT, Art. 57 |
| Failure to file | Sanction of 50% of tax (minimum 3 salarios base) | CNPT, Art. 78 |
| Tax evasion | Criminal penalties possible | CNPT, Art. 92 |
| Failure to issue electronic invoice | Closure of establishment (5 days) | CNPT, Art. 86 |

---

## Step 11: Simplified Regime (Regimen Simplificado) [T2]

**Legislation:** Ley 9635, Art. 26; Reglamento, Art. 30-32.

### Who Qualifies [T2]

| Condition | Threshold |
|-----------|-----------|
| Annual gross income | Below threshold set by Ministerio de Hacienda (varies by activity) |
| Activity type | Retail (venta al detalle), restaurants, bars, bakeries, and certain services |
| Employees | Maximum 5 employees |
| Establishments | Maximum 1 commercial establishment |

### Simplified IVA Treatment [T2]

| Feature | Detail |
|---------|--------|
| IVA rate charged | Standard rates (13%, 4%, 2%, 1%) apply |
| Credito fiscal | NO -- simplified regime taxpayers cannot claim credito fiscal |
| Filing | Simplified quarterly return |
| Payment | Fixed factor applied to gross income (percentage set by regulation) |
| Electronic invoicing | Still mandatory |

### Simplified Regime Factors (Approximate) [T2]

| Activity | Factor Applied to Gross Sales |
|----------|-------------------------------|
| Retail (general) | 2% |
| Restaurants/bars | 4% |
| Bakeries | 2% |
| Services (general) | 4% |

**Flag for reviewer:** Simplified regime factors and thresholds change. Verify current values with Ministerio de Hacienda. Confirm qualification with Contador Publico Autorizado.

---

## Step 12: Residential Rent Exemption [T1]

**Legislation:** Ley 9635, Art. 8(2)(a).

### Rules [T1]

| Rule | Detail |
|------|--------|
| Exempt threshold | Residential rent up to 1.5 salario base per month is exempt from IVA |
| Salario base reference | Salario base de un oficinista 1 del Poder Judicial (set annually) |
| 2025 value (approximate) | ~CRC 462,200 (salario base); threshold = ~CRC 693,300 |
| Above threshold | Rent above 1.5 salario base is subject to IVA at 13% on the ENTIRE amount |
| Commercial rent | Always subject to IVA at 13% (no exemption) |
| Furnished rent | Subject to IVA at 13% (no exemption, considered a service) |

### Critical Distinction [T1]

| Rent Amount | Treatment |
|-------------|-----------|
| <= 1.5 salario base | Exempt (no IVA) |
| > 1.5 salario base | 13% IVA on FULL amount (not just the excess) |
| Commercial/furnished | 13% IVA regardless of amount |

---

## Step 13: Key Thresholds [T1]

| Threshold | Value | Notes |
|-----------|-------|-------|
| Salario base (2025 approx.) | ~CRC 462,200 | Used for rent exemption, penalties |
| Residential rent exemption | 1.5 salario base (~CRC 693,300) | Monthly rent threshold |
| Simplified regime income | Varies by activity | Check current Ministerio de Hacienda resolution |
| Statute of limitations | 4 years (standard); 10 years (fraud) | CNPT, Art. 51 |
| Electronic invoice storage | 4 years minimum | CNPT, Art. 109 |

---

## Step 14: Saldo a Favor (Credit Balances) [T1]

**Legislation:** Ley 9635, Art. 23.

### Rules [T1]

| Rule | Detail |
|------|--------|
| Carryforward | If credito fiscal exceeds debito fiscal, the excess (saldo a favor) carries forward |
| Indexation | No inflation adjustment |
| Expiry | Carried forward for up to 3 years (36 months); if not used, lost |
| Refund | Only for exporters and taxpayers in specific situations (Art. 23) |

### Exporter Refund [T1]

| Element | Detail |
|---------|--------|
| Who qualifies | Exporters (zero-rated under Art. 8(1)) |
| What is recoverable | Credito fiscal attributable to export activity |
| How | Refund request (solicitud de devolucion) to Ministerio de Hacienda |
| Timeline | Ministerio has 30 business days to process |
| Audit risk | Refund requests may trigger audit |

---

## Step 15: Canasta Basica Tributaria (1% Rate List) [T1]

**Legislation:** Ley 9635, Art. 11(c); Decreto Ejecutivo defining the list.

### Key Categories [T1]

| Category | Examples |
|----------|----------|
| Basic grains | Rice, beans, corn, wheat |
| Dairy | Fluid milk, pasteurized |
| Bread | Basic bread products |
| Eggs | Chicken eggs |
| Basic vegetables | Tomatoes, onions, potatoes, carrots |
| Basic fruits | Bananas, plantains |
| Basic proteins | Chicken, certain cuts of beef |
| Cooking oils | Basic vegetable oil |
| Basic hygiene | Toilet paper, basic soap |
| Baby formula | Infant nutrition |

**IMPORTANT:** Not all food is at 1%. Only items specifically listed in the Canasta Basica Tributaria qualify. Processed, premium, or imported food products may be at 13%.

### Distinction from Exempt [T1]

| Category | Rate | Treatment |
|----------|------|-----------|
| Canasta basica (specific list) | 1% | Taxable at 1%; credito fiscal for seller limited to 1% |
| Exempt food (if any remain in Art. 8) | 0% | Exempt; no IVA; no credito fiscal for seller |
| All other food/beverages | 13% | Standard rate |

---

## Step 16: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Contador Publico Autorizado must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Contador Publico Autorizado. Document gap.
```

---

## Step 17: Edge Case Registry

### EC1 -- Health service at 4% [T1]
**Situation:** Client (medical clinic) charges patients for medical consultations.
**Resolution:** Private health services are taxable at 4%. Issue Factura Electronica with 4% IVA. Input IVA on clinic expenses (at 13%) is subject to the rate matching rule -- only recoverable up to 4%. The excess (13% - 4% = 9%) becomes a cost.
**Legislation:** Ley 9635, Art. 11(a); Art. 15.

### EC2 -- Purchase documented with Tiquete Electronico [T1]
**Situation:** Employee purchases office supplies and receives only a Tiquete Electronico.
**Resolution:** No credito fiscal. Tiquetes Electronicos do not give right to credito fiscal. The full amount (including IVA) is the expense. To claim credito fiscal, a Factura Electronica must be requested.
**Legislation:** Ley 9635, Art. 17.

### EC3 -- Software subscription from US provider (e.g., AWS, Netflix) [T1]
**Situation:** Monthly charge from a US company for cloud services. Provider is not registered in Costa Rica.
**Resolution:** Reverse charge applies. Buyer self-assesses IVA at 13% on the service value. Report as debito fiscal and simultaneously claim as credito fiscal on Form D-104. Net zero for fully taxable businesses at 13%. If provider IS registered, IVA should be charged on the invoice.
**Legislation:** Ley 9635, Art. 3(d)(e); Decreto 43198-H.

### EC4 -- Residential rent below threshold [T1]
**Situation:** Landlord rents an unfurnished apartment for CRC 500,000/month (below 1.5 salario base).
**Resolution:** Exempt from IVA. No IVA charged. No credito fiscal on related expenses (exempt activity). Report as ventas exentas on D-104.
**Legislation:** Ley 9635, Art. 8(2)(a).

### EC5 -- Residential rent above threshold [T1]
**Situation:** Landlord rents an unfurnished apartment for CRC 900,000/month (above 1.5 salario base).
**Resolution:** IVA at 13% on the FULL CRC 900,000 (not just the excess). IVA = CRC 117,000. Total = CRC 1,017,000. The exemption is lost entirely when rent exceeds the threshold.
**Legislation:** Ley 9635, Art. 8(2)(a).

### EC6 -- Export of goods [T1]
**Situation:** Costa Rican company exports coffee beans to the US.
**Resolution:** Zero-rated under Art. 8(1)(a). No IVA charged. Issue Factura Electronica de Exportacion. Credito fiscal on all related costs (at any rate) IS fully recoverable. Client may request IVA refund (devolucion).
**Legislation:** Ley 9635, Art. 8(1)(a); Art. 23.

### EC7 -- Sale to Free Trade Zone company [T1]
**Situation:** Costa Rican supplier sells goods to a company in a Zona Franca.
**Resolution:** Treated as export (zero-rated) under Art. 8(1)(c). No IVA charged. Credito fiscal recoverable. Must verify buyer's ZF registration status.
**Legislation:** Ley 9635, Art. 8(1)(c); Ley 7210.

### EC8 -- Restaurant services [T1]
**Situation:** Client operates a restaurant selling prepared food and beverages.
**Resolution:** Restaurant services are taxable at 13% (standard rate). This is different from Colombia (where restaurants pay INC instead of IVA). Issue Factura Electronica at 13%. Full credito fiscal on inputs (subject to normal rules).
**Legislation:** Ley 9635, Art. 10.

### EC9 -- Mixed-rate business (health clinic + pharmacy) [T2]
**Situation:** Client operates a medical clinic (4% on consultations) and sells pharmaceutical products (2% for essential medicines, 13% for others).
**Resolution:** Each sale must be classified at the correct rate. Credito fiscal on inputs must be allocated by activity. For common expenses, apply prorrata AND rate matching. Flag for reviewer: confirm allocation methodology and rate matching application with Contador Publico Autorizado.
**Legislation:** Ley 9635, Art. 15-16.

### EC10 -- Credit note received [T1]
**Situation:** Supplier issues Nota de Credito Electronica for returned goods.
**Resolution:** Reduce credito fiscal by the IVA amount on the credit note. The NC must reference the original Factura and be a valid electronic document accepted by Ministerio de Hacienda.
**Legislation:** Ley 9635, Art. 17; Resolucion DGT-R-012-2018.

---

## Step 18: Penalties and Interest Summary [T1]

**Legislation:** Codigo de Normas y Procedimientos Tributarios (CNPT), Ley 4755.

| Infraction | Penalty | Legislation |
|------------|---------|-------------|
| Late filing | 1% of tax per month, up to 20% (minimum 3 salarios base) | CNPT, Art. 78 |
| Late payment | Monthly interest rate (tasa de interes) set by Ministerio de Hacienda | CNPT, Art. 57 |
| Failure to file | 50% of tax owed (minimum 3 salarios base) | CNPT, Art. 78 |
| Failure to issue electronic invoice | Closure of establishment for 5 natural days (first offense) | CNPT, Art. 86 |
| Tax evasion (fraud) | Criminal penalties: 150-350 salarios base fine | CNPT, Art. 92 |
| Providing false information | 100% of tax difference | CNPT, Art. 81 |
| Not keeping proper records | 2 salarios base per infraction | CNPT, Art. 84 |

---

## Step 19: Comparison with Previous Sales Tax (Pre-2019) [T1]

| Feature | Old Sales Tax (pre-July 2019) | New IVA (Ley 9635) |
|---------|-------------------------------|---------------------|
| Name | Impuesto General sobre las Ventas (IGV) | Impuesto al Valor Agregado (IVA) |
| Rate | 13% (single) | 13%, 4%, 2%, 1% (four rates) |
| Goods | Taxable (most) | Taxable (most) |
| Services | Limited (specific list) | Broad (most services taxable) |
| Health services | Not taxed | 4% (private) / exempt (CCSS) |
| Education | Not taxed | 4% (private) / exempt (public) |
| Financial services | Not taxed | Exempt |
| Credito fiscal | Available | Available (with rate matching rule) |
| Canasta basica | Not specifically categorized | 1% rate |
| Electronic invoicing | Not mandatory | Mandatory |

---

## Step 20: Test Suite

### Test 1 -- Standard local sale at 13%
**Input:** Costa Rican company sells consulting services to local business, base CRC 1,000,000, IVA CRC 130,000. Factura Electronica issued.
**Expected output:** Form D-104, ventas gravadas 13% += CRC 1,000,000, debito fiscal += CRC 130,000.

### Test 2 -- Purchase with valid Factura, operating expense
**Input:** Company buys office supplies from local supplier, base CRC 200,000, IVA CRC 26,000 (13%). Valid Factura Electronica received and accepted.
**Expected output:** Form D-104, compras gravadas 13% += CRC 200,000, credito fiscal += CRC 26,000.

### Test 3 -- Health service sale at 4%
**Input:** Medical clinic charges patient CRC 100,000 for consultation. IVA at 4% = CRC 4,000.
**Expected output:** Form D-104, ventas gravadas 4% += CRC 100,000, debito fiscal += CRC 4,000.

### Test 4 -- Input IVA with rate matching (health clinic buying at 13%)
**Input:** Medical clinic (selling at 4%) buys medical supplies at 13%. Base CRC 500,000, IVA CRC 65,000.
**Expected output:** Credito fiscal limited to 4% of base = CRC 20,000. Non-recoverable = CRC 45,000 (becomes cost). Form D-104, credito fiscal += CRC 20,000.

### Test 5 -- Canasta basica sale at 1%
**Input:** Supermarket sells basic rice (in canasta basica list), base CRC 50,000, IVA CRC 500 (1%).
**Expected output:** Form D-104, ventas gravadas 1% += CRC 50,000, debito fiscal += CRC 500.

### Test 6 -- Export of goods
**Input:** Company exports pineapples, FOB value USD 5,000. Factura de Exportacion issued.
**Expected output:** Form D-104, exportaciones += CRC equivalent. No IVA charged. Credito fiscal on inputs fully recoverable.

### Test 7 -- Residential rent below threshold (exempt)
**Input:** Landlord rents unfurnished apartment for CRC 500,000/month.
**Expected output:** Exempt. No IVA charged. Report as ventas exentas. No credito fiscal on rental-related expenses.

### Test 8 -- Residential rent above threshold (taxable)
**Input:** Landlord rents unfurnished apartment for CRC 900,000/month.
**Expected output:** IVA at 13% on FULL amount. IVA = CRC 117,000. Total = CRC 1,017,000. Report in ventas gravadas 13%.

### Test 9 -- Import of services (reverse charge)
**Input:** Company pays USD 2,000 (CRC 1,060,000) for foreign marketing services. Provider not registered in CR.
**Expected output:** Self-assess IVA: CRC 1,060,000 * 13% = CRC 137,800. Report as debito fiscal AND credito fiscal. Net zero for fully taxable business at 13%.

### Test 10 -- Purchase with Tiquete Electronico only (no credito fiscal)
**Input:** Employee buys cleaning supplies CRC 15,000 total. Only Tiquete Electronico received.
**Expected output:** No credito fiscal. Full CRC 15,000 is operating expense. No IVA entry on D-104 for input.

---

## PROHIBITIONS [T1]

- NEVER allow credito fiscal on Tiquete Electronico purchases
- NEVER ignore the rate matching rule (Art. 15) -- credito fiscal is capped at the seller's applicable output rate
- NEVER apply the 1% rate to food items NOT on the Canasta Basica Tributaria list
- NEVER exempt residential rent above 1.5 salario base -- the FULL amount becomes taxable at 13%
- NEVER confuse the old sales tax (IGV, pre-2019) with the current IVA (Ley 9635)
- NEVER allow credito fiscal for simplified regime (Regimen Simplificado) taxpayers
- NEVER omit reverse charge on services imported from abroad
- NEVER accept an electronic invoice that was rejected (acceptance code 3) as valid for credito fiscal
- NEVER apply the 4% health rate to non-health services or the 2% rate to non-qualifying products
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Contribution Notes (For Adaptation to Other Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all Form D-104 sections with the equivalent sections on your jurisdiction's VAT/IVA return form.
3. Replace IVA rates (13%/4%/2%/1%) with your jurisdiction's standard and reduced rates.
4. Replace the Canasta Basica Tributaria concept with your jurisdiction's equivalent (if any).
5. Replace the residential rent exemption threshold (1.5 salario base) with your jurisdiction's equivalent.
6. Replace the rate matching rule with your jurisdiction's equivalent credito fiscal limitation.
7. Replace the electronic invoicing requirements with your jurisdiction's e-invoicing rules.
8. Have a licensed accountant in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
