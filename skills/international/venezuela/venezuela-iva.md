---
name: venezuela-iva
description: Use this skill whenever asked to prepare, review, or create a Venezuela IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "Venezuela VAT", or any request involving Venezuela value added tax filing. ALWAYS read this skill before touching any Venezuela IVA-related work. NOTE -- Venezuela's economic instability means rates and thresholds change frequently. ALWAYS verify current rates before filing. [T2]
---

# Venezuela IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Venezuela (Republica Bolivariana de Venezuela) |
| Jurisdiction Code | VE |
| Primary Legislation | Ley de Impuesto al Valor Agregado (Gaceta Oficial, multiple reforms) |
| Supporting Legislation | Reglamento de la Ley del IVA; Providencias SENIAT |
| Tax Authority | Servicio Nacional Integrado de Administracion Aduanera y Tributaria (SENIAT) |
| Filing Portal | http://www.seniat.gob.ve (Portal Fiscal SENIAT) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires sign-off by a licensed Venezuela CPA (Contador Publico Colegiado) |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Last Verified | April 2026 -- rates, thresholds, forms, and deadlines verified against current sources |
| Confidence Coverage | Tier 1: return form structure, basic classification rules. Tier 2: rate verification (rates change frequently), withholding, exchange rate issues. Tier 3: complex structures, currency controls, rulings. |

---

## CRITICAL WARNING [T2]

**Venezuela's economic and regulatory environment is highly volatile.** The following aspects change frequently and MUST be verified before every filing:

1. **IVA rate** -- has changed multiple times (12%, 16%, other rates have been enacted). The rate stated in this skill (16%) reflects the most recently confirmed standard rate but MAY have changed.
2. **Additional luxury/selective rate** -- an adicional rate of up to 15% has been applied to luxury goods at various times.
3. **Currency** -- Venezuela has undergone multiple currency reconversions (Bolivar Fuerte to Bolivar Soberano to Bolivar Digital). All amounts must use the current currency denomination.
4. **Exchange rates** -- official and parallel exchange rates diverge significantly. Tax obligations are generally based on official BCV (Banco Central de Venezuela) rates.
5. **Filing systems** -- SENIAT's online portals experience frequent downtime.

**Flag for reviewer on EVERY filing: confirm current IVA rate, currency denomination, and SENIAT system availability.**

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options. Given Venezuela's instability, more items are T2 than in other jurisdictions.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and RIF (Registro de Informacion Fiscal)** [T1] -- format: J-12345678-9 (juridica) or V-12345678-9 (natural)
2. **IVA registration status** [T1] -- Contribuyente Ordinario or Contribuyente Formal
3. **Filing period** [T1] -- monthly (Contribuyente Ordinario), quarterly (Contribuyente Formal, subject to conditions)
4. **Industry/sector** [T2]
5. **Does the business make exempt supplies?** [T2]
6. **Does the business import goods?** [T1]
7. **Is the business a designated Contribuyente Especial?** [T2] -- special withholding obligations
8. **Credit balance brought forward** [T1]
9. **Current applicable IVA rate** [T2] -- MUST verify before classifying

**If items 1-3 are unknown, STOP.**

---

## Step 1: IVA Rate Structure [T2]

**Legislation:** Ley del IVA, Articles 27, 61, 62.

### Standard Rate [T2]

| Rate | Application |
|------|-------------|
| 16% | Standard rate (alicuota general). NOTE: this rate has changed multiple times. Verify with SENIAT before filing. [T2] |

### Reduced Rate [T2]

| Rate | Application |
|------|-------------|
| 8% | Certain food products and essential goods (when enacted by Executive Decree) [T2] |

### Additional Rate (Luxury) [T2]

| Rate | Application |
|------|-------------|
| Up to 15% additional | Luxury goods and non-essential items (Alicuota Adicional). Applied on top of standard rate when enacted. [T2] |

**WARNING:** The Executive has authority to modify rates within ranges established by law (8% to 16.5% standard; 0% to 15% additional). Verify current gazette.

### Exempt Goods [T1]

**Legislation:** Ley del IVA, Article 18.

- Basic food: rice, corn flour (harina de maiz precocida), bread, pasta, fresh meats, fresh fish, eggs, milk, sugar, salt, fresh fruits and vegetables, cooking oil, margarine, sardines, tuna (canned, basic)
- Medicines and pharmaceutical products
- Agricultural inputs (fertilizers, seeds, insecticides, animal feed)
- Books, newspapers, school supplies
- Fuel and petroleum derivatives (regulated prices)
- Machinery for agricultural production
- Equipment for public health
- Wheelchairs and medical equipment for disabled persons

### Exempt Services [T1]

**Legislation:** Ley del IVA, Article 19.

- Health/medical services (public and private)
- Educational services (authorized institutions)
- Residential rental
- Public transportation (urban)
- Water (domestic supply)
- Electricity (domestic, up to threshold)
- Telephone (residential, basic plan)
- Financial services: interest on savings, certain insurance
- Government services

### Exports (0% -- Full Input Credit) [T1]
- Export of goods: zero-rated with full input credit recovery
- Export of services: services consumed outside Venezuela [T2]

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (debito fiscal -- output) or Purchase (credito fiscal -- input)
- Salaries, IVSS (social security), FAOV (housing), INCE (training), BANAVIH, loans = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (Venezuela)
- International
- Note: Venezuela is NOT a current active member of MERCOSUR (suspended 2017) or CAN (withdrew 2006). Treat all foreign counterparties as international.

### 2c. Determine IVA Rate [T2]
- 0% (export), current standard rate, reduced rate, or exempt
- ALWAYS verify rate before classifying

---

## Step 3: IVA Return Form Structure (Forma 30) [T1]

**Filed monthly for Contribuyentes Ordinarios.**

### Debito Fiscal (Output)

| Line | Description |
|------|-------------|
| 1 | Ventas internas gravadas (Domestic taxable sales) |
| 2 | Debito fiscal en ventas internas |
| 3 | Ventas de exportacion (Exports) |
| 4 | Ventas internas no gravadas / exentas |
| 5 | Total ventas |
| 6 | Total debito fiscal |

### Credito Fiscal (Input)

| Line | Description |
|------|-------------|
| 7 | Compras internas gravadas |
| 8 | Credito fiscal en compras internas |
| 9 | Importaciones gravadas |
| 10 | Credito fiscal en importaciones |
| 11 | Total credito fiscal |
| 12 | Ajustes (blocked/proportional) |
| 13 | Credito fiscal neto |

### Liquidacion

| Line | Description |
|------|-------------|
| 14 | Diferencia (Line 6 - Line 13) |
| 15 | Excedente credito fiscal anterior |
| 16 | Retenciones de IVA (Contribuyentes Especiales) |
| 17 | Total a pagar / excedente |

---

## Step 4: IVA Withholding by Contribuyentes Especiales [T1]

**Legislation:** Providencia Administrativa SNAT 2005-0056 (as amended).

Venezuela's IVA withholding regime for Contribuyentes Especiales is one of the most impactful:

### Withholding Rates [T1]

| Scenario | Rate |
|----------|------|
| Contribuyente Especial purchasing from ordinary taxpayer with fiscal domicile | 75% of IVA [T1] |
| Contribuyente Especial purchasing from supplier without fiscal domicile address | 100% of IVA [T1] |
| Contribuyente Especial purchasing from non-registered/informal | 100% of IVA [T2] |
| Government entities (Entes Publicos) | 75% or 100% of IVA [T1] |

### Treatment [T1]
- Withholding agent (Contribuyente Especial) withholds IVA from payment
- Supplier claims withheld amount on Line 16 of their Forma 30
- Withholding agent files IVA withholding return (bi-weekly) via SENIAT portal
- Comprobante de retencion must be issued

### Bi-Weekly Withholding Filing [T1]
- Contribuyentes Especiales file IVA withholding returns twice per month:
  - First 15 days: filed by 20th
  - Last 15 days (or remainder): filed by 5th of following month
- Calendar published annually by SENIAT

---

## Step 5: Reverse Charge on Imported Services [T1]

When a Venezuela registered person receives services from a non-resident:

1. Self-assess IVA at standard rate [T2]
2. Report as debito fiscal [T1]
3. Claim as credito fiscal if for taxable operations [T1]
4. Net = zero for fully taxable businesses [T1]

---

## Step 6: Deductibility Check

### Blocked Input IVA [T1]

**Legislation:** Ley del IVA, Article 33.

- **Motor vehicles** -- passenger vehicles (exception: rental, taxi, transport) [T1]
- **Entertainment/recreation** -- meals, hospitality (unless hospitality business) [T1]
- **Personal use** [T1]
- **Exempt operations** [T1]
- **Purchases without valid factura (fiscal invoice)** [T1]

### Fiscal Invoice Requirement [T1]

**Legislation:** Ley del IVA, Article 54; Providencias SENIAT on facturacion.

- All invoices must comply with SENIAT requirements
- Must include: RIF, date, description, base imponible, IVA amount, total
- Fiscal machines (impresoras fiscales) required for certain taxpayers
- Electronic invoicing being implemented through IGTF (Impuesto a Grandes Transacciones Financieras) related reforms [T2]

### Partial Exemption [T2]
- Direct attribution + proportional (prorrata)
- `Recovery % = (Taxable Sales / Total Sales) * 100`
- Flag for reviewer

---

## Step 7: Libro de Compras y Ventas (Purchase and Sales Ledgers) [T1]

**Legislation:** Ley del IVA, Article 56.

All IVA taxpayers must maintain:

- **Libro de Compras** -- purchase ledger with all purchases, RIF of supplier, base, IVA, total
- **Libro de Ventas** -- sales ledger with all sales, RIF of customer (B2B), base, IVA, total
- These ledgers must be available for SENIAT inspection
- Summary totals flow to the Forma 30
- Chronological order required

---

## Step 8: Key Thresholds [T2]

| Threshold | Value |
|-----------|-------|
| Contribuyente Ordinario | All persons making habitual taxable sales above threshold |
| Contribuyente Formal | Small taxpayers -- simplified obligations (not required to charge IVA if below threshold) [T2] |
| Contribuyente Especial | Designated by SENIAT based on revenue/importance -- special withholding agent |
| Note | Thresholds are expressed in Unidades Tributarias (UT), which are adjusted periodically. Verify current UT value. [T2] |

---

## Step 9: Filing Deadlines and Penalties [T1]

### Filing Deadlines [T1]

| Taxpayer Type | Period | Deadline |
|---------------|--------|----------|
| Contribuyente Ordinario | Monthly | Calendar published by SENIAT based on last digit of RIF [T1] |
| Contribuyente Formal | Quarterly | 15th of month following quarter end [T2] |
| Contribuyente Especial (withholding) | Bi-weekly | Calendar published by SENIAT [T1] |

### Penalties [T1]

| Violation | Penalty |
|-----------|---------|
| Late filing | 5 UT to 50 UT per return [T1] |
| Late payment | 1% per month on unpaid tax + monetary correction [T1] |
| Failure to withhold | 100% to 300% of amount not withheld [T1] |
| Failure to keep Libros | 50 UT to 200 UT [T1] |
| Fraud (defraudacion) | 100% to 300% of tax evaded + criminal prosecution [T1] |
| Failure to issue factura | Closure of business (1-5 days) [T1] |

---

## Step 10: Classification Matrix [T1]

### Domestic Purchases

| Category | IVA Rate | Input Credit | Notes |
|----------|---------|--------------|-------|
| Office supplies | 16% [T2] | Yes | Verify rate |
| Commercial rent | 16% [T2] | Yes | |
| Residential rent | Exempt | No | |
| Electricity (commercial) | 16% [T2] | Yes | |
| Telephone/internet | 16% [T2] | Yes | |
| Motor car | 16% [T2] | BLOCKED | |
| Entertainment | 16% [T2] | BLOCKED | |
| Professional services | 16% [T2] | Yes | |
| Insurance (general) | 16% [T2] | Yes | |
| Basic food | Exempt | No | |
| Medicines | Exempt | No | |
| Fuel | Exempt | No | Regulated |

### Sales

| Category | IVA | Return Line |
|----------|-----|-------------|
| Domestic taxable | 16% [T2] | Line 1, Line 2 |
| Export | 0% | Line 3 |
| Exempt | Exempt | Line 4 |
| Luxury (additional rate) | 16% + additional [T2] | Line 1, Line 2 (combined) |

---

## Step 11: Currency and Exchange Rate Issues [T2]

**Critical for Venezuela:**

- All tax returns are filed in Bolivares (Bs.) at the current denomination
- Currency reconversions: Bolivar Fuerte (2008) -> Bolivar Soberano (2018, 5 zeros removed) -> Bolivar Digital (2021, 6 zeros removed)
- Exchange rate for foreign-currency transactions: use official BCV rate on date of transaction
- IGTF (Impuesto a las Grandes Transacciones Financieras): additional tax on transactions in foreign currency -- separate from IVA but often confused [T2]
- Flag for reviewer: ALWAYS confirm current currency denomination and conversion factors

---

## PROHIBITIONS [T1]

- NEVER let AI guess IVA classification
- NEVER assume IVA rate without verification -- rates change frequently in Venezuela [T2]
- NEVER allow input credit on blocked categories
- NEVER allow input credit without valid factura
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse IVA with IGTF (separate taxes)
- NEVER use outdated currency denominations
- NEVER ignore Contribuyente Especial withholding obligations
- NEVER compute any number -- all arithmetic is handled by the deterministic engine

---

## Step 12: Edge Case Registry

### EC1 -- Rate change mid-period [T2]
**Situation:** IVA rate changes during a filing period.
**Resolution:** Apply the rate in effect at the time of the taxable event (date of sale or service). A single period may have transactions at different rates. Flag for reviewer: confirm transition rules from the specific gazette.

### EC2 -- Imported software [T1]
**Situation:** Venezuela company subscribes to US cloud service. No IVA.
**Resolution:** Self-assess IVA at current standard rate. Output and input. Net = zero.

### EC3 -- Contribuyente Especial withholding at 75% [T1]
**Situation:** Contribuyente Especial purchases services from ordinary taxpayer. Invoice: Bs. 10,000 + IVA Bs. 1,600.
**Resolution:** Withhold 75% of IVA = Bs. 1,200. Pay supplier Bs. 10,400 (10,000 + 400 remaining IVA). File bi-weekly withholding return. Issue comprobante de retencion. Supplier claims Bs. 1,200 on Line 16.

### EC4 -- Credit notes [T1]
**Situation:** Client issues nota de credito.
**Resolution:** Reduce debito fiscal. Record in Libro de Ventas. Report net.

### EC5 -- Transaction in USD [T2]
**Situation:** Sale denominated in US dollars.
**Resolution:** Convert to Bolivares at BCV official rate on date of transaction. IVA calculated on Bolivar equivalent. IGTF may also apply on the foreign currency portion. Flag for reviewer.

### EC6 -- Luxury goods additional rate [T2]
**Situation:** Company sells imported perfumes.
**Resolution:** May be subject to standard rate + additional luxury rate. Total rate could be 16% + up to 15% = 31%. Verify current gazette for applicable additional rate and product list. Flag for reviewer.

### EC7 -- SENIAT portal downtime [T2]
**Situation:** SENIAT portal is unavailable on filing deadline.
**Resolution:** Document the system unavailability (screenshots, printouts). File as soon as system is available. Penalties may be contested based on force majeure. Flag for reviewer.

### EC8 -- Hyperinflation accounting [T3]
**Situation:** IVA amounts affected by hyperinflation between transaction and payment dates.
**Resolution:** Escalate to specialist. Hyperinflation adjustments and their interaction with IVA are complex. IAS 29 may apply for financial reporting but tax obligations follow nominal Bolivar amounts.

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
Action Required: Licensed CPA must confirm before filing. In Venezuela, ALSO verify current rate and currency denomination.
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

## Step 14: Test Suite

### Test 1 -- Standard local purchase, 16%
**Input:** VE supplier, office supplies, gross Bs. 11,600, IVA Bs. 1,600, net Bs. 10,000. Valid factura.
**Expected output:** Line 8 = Bs. 1,600 credito fiscal. Full recovery. (Verify rate at time of transaction.)

### Test 2 -- Export, zero-rated
**Input:** Exporter ships goods, net Bs. 500,000.
**Expected output:** Line 3 = Bs. 500,000. No debito fiscal. Credito fiscal fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase sedan Bs. 200,000, IVA Bs. 32,000.
**Expected output:** IVA Bs. 32,000 BLOCKED. No credito fiscal.

### Test 4 -- Contribuyente Especial withholding
**Input:** CE purchases from ordinary taxpayer. Invoice Bs. 50,000 + IVA Bs. 8,000. Withhold 75%.
**Expected output:** Withholding = Bs. 6,000 (75% of 8,000). Supplier claims Bs. 6,000 on Line 16.

### Test 5 -- Imported services, reverse charge
**Input:** US consulting, USD 1,000 at BCV rate 36.60 = Bs. 36,600. No IVA.
**Expected output:** Self-assess debito fiscal = Bs. 5,856 (16%). Credito fiscal = Bs. 5,856. Net = zero.

### Test 6 -- Exempt supply (medical)
**Input:** Clinic earns Bs. 100,000 from patient fees.
**Expected output:** Line 4 = Bs. 100,000. No debito fiscal. Credito fiscal NOT recoverable.

### Test 7 -- Mixed operations
**Input:** 70% taxable, 30% exempt. Common IVA = Bs. 10,000.
**Expected output:** Flag T2. Input = Bs. 7,000 (70%). Blocked = Bs. 3,000 (30%).

### Test 8 -- Entertainment, blocked
**Input:** Client dinner Bs. 5,800 inclusive of IVA Bs. 800.
**Expected output:** IVA Bs. 800 BLOCKED. No credito fiscal.

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**

**SPECIAL NOTE FOR VENEZUELA:** Given the extreme volatility of the Venezuelan tax and economic environment, this skill requires more frequent updates than skills for stable jurisdictions. The reviewer must verify ALL rates, thresholds, and currency values at the time of each filing. Consider this skill as a structural framework rather than a definitive rate reference.

---

## Appendix A: Sector-Specific Rules [T2]

### Oil and Gas (Hydrocarbons)

- **PDVSA and state-owned enterprises**: subject to IVA on domestic operations [T1]
- **Oil exports**: zero-rated [T1]
- **Services to oil sector**: taxable at standard rate [T1]
- **Joint ventures (empresas mixtas)**: IVA on service fees and supplies [T2]
- **ISLR (Income Tax) interaction**: separate from IVA [T3]
- Flag for reviewer: oil sector transactions require specialist knowledge

### Mining

- **Gold mining**: special tax regime. IVA on domestic sales of gold may apply [T2]
- **Other minerals**: IVA at standard rate on domestic sales [T1]
- **Exports**: zero-rated [T1]

### Agriculture

- **Unprocessed agricultural products**: exempt (basic food) [T1]
- **Processed food**: taxable at standard rate (unless on exempt list) [T1]
- **Agricultural inputs**: exempt [T1]

### Financial Services

- **Interest on savings**: exempt [T1]
- **Banking commissions**: taxable at standard rate [T1]
- **Insurance premiums (life)**: exempt [T1]
- **Insurance premiums (general)**: taxable [T1]
- **IGTF on foreign currency transactions**: separate from IVA [T2]

### Telecommunications

- **All telecom services**: taxable at standard rate [T1]
- **Internet services**: taxable at standard rate [T1]

### Construction and Real Estate

- **Construction services**: taxable at standard rate [T1]
- **Sale of real estate**: exempt from IVA (subject to registration tax) [T1]
- **Commercial rental**: taxable at standard rate [T1]
- **Residential rental**: exempt [T1]

---

## Appendix B: IGTF (Impuesto a las Grandes Transacciones Financieras) [T2]

**Legislation:** Ley de IGTF (Gaceta Oficial).

This is NOT IVA but is frequently confused with it:

- IGTF is a financial transactions tax
- Applies to payments in foreign currency (USD, EUR, crypto) at rate of 2-3%
- Also applies to large Bolivar transactions through the banking system
- IGTF is NOT reported on the IVA return -- it has its own return
- IGTF does NOT affect IVA calculations
- However, IGTF must be accounted for separately in the business records
- Flag for reviewer: clearly separate IGTF from IVA in all reporting

---

## Appendix C: Additional Rules [T1]

### Self-Supply (Autoconsumo) [T1]

- Withdrawal of goods for personal use: taxable event [T1]
- IVA at standard rate on fair market value [T1]
- Report as debito fiscal [T1]

### Barter [T1]

- Treated as two sales [T1]
- IVA on fair market value for each leg [T1]

### Installment Sales [T1]

- IVA due at time of delivery [T1]

### Record Retention [T1]

- All fiscal documents and IVA returns: minimum 4 years (prescripcion ordinaria)
- In cases of fraud: no prescription limit
- SENIAT may audit any period within statute of limitations


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
