---
name: colombia-iva
description: Use this skill whenever asked to prepare, review, or create a Colombia IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "declaracion de IVA", "Colombia VAT", "DIAN filing", "factura electronica", or any request involving Colombian IVA filing. Also trigger when classifying transactions for IVA purposes from bank statements, invoices, or other source data. This skill contains the complete Colombia IVA classification rules, form mappings, deductibility rules, withholding treatment (retencion en la fuente de IVA), Impuesto Nacional al Consumo (INC), electronic invoicing requirements, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any IVA-related work for Colombia.
---

# Colombia IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Colombia |
| Jurisdiction Code | CO |
| Primary Legislation | Estatuto Tributario (E.T.), Libro Tercero -- Impuesto sobre las Ventas (Articles 420--513) |
| Supporting Legislation | Decreto 1625 de 2016 (Decreto Unico Reglamentario en materia tributaria); Ley 2277 de 2022 (Reforma Tributaria); Resolucion DIAN 000165 de 2023 (facturacion electronica); Decreto Legislativo 1474 de 2025 (emergency fiscal measures for 2026 budget) |
| Tax Authority | DIAN -- Direccion de Impuestos y Aduanas Nacionales |
| Filing Portal | https://muisca.dian.gov.co |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, form mapping, filing periods, electronic invoicing triggers. Tier 2: INC classification, partial exemption, withholding agent obligations. Tier 3: complex transfer pricing, special economic zones (ZF), multi-entity groups. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed Contador Publico must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed Contador Publico and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and NIT (Numero de Identificacion Tributaria)** [T1] -- 9-digit NIT + verification digit
2. **Taxpayer classification** [T1] -- Responsable de IVA (standard) or No Responsable de IVA (simplified, formerly Regimen Simplificado)
3. **Filing period** [T1] -- Bi-monthly (large taxpayers / grandes contribuyentes) or Quarterly (cuatrimestral for other responsables)
4. **Gran Contribuyente status** [T1] -- designated by DIAN resolution; affects filing frequency and withholding obligations
5. **Industry/sector** [T2] -- impacts INC applicability (restaurants, bars, vehicles, telecoms)
6. **Does the business make exempt supplies?** [T2] -- If yes, proportional IVA recovery required (pro-rata); reviewer must confirm
7. **Is the client a withholding agent (agente de retencion de IVA)?** [T1] -- Grandes contribuyentes and designated entities must withhold 15% of IVA from suppliers
8. **Does the client have electronic invoicing (facturacion electronica) enabled?** [T1] -- mandatory for all IVA responsables
9. **Does the client import goods or services?** [T2] -- customs IVA and reverse charge on services from abroad

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until taxpayer status and period are confirmed.**

---

## Step 1: IVA Rate Classification Rules

### 1a. Standard Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 19% | General rate on taxable goods and services | E.T. Art. 468 |

**Legislation:** Estatuto Tributario, Article 468. The general tariff of IVA is 19%.

### 1b. Reduced Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 5% | Certain processed foods (coffee, chocolate, pasta, sausages) | E.T. Art. 468-1 |
| 5% | Cotton, fiber, yarn | E.T. Art. 468-1 |
| 5% | Agricultural insurance | E.T. Art. 468-1 |
| 5% | Storage services for agricultural products | E.T. Art. 468-1 |
| 5% | Bicycles and electric bicycles valued under 50 UVT | E.T. Art. 468-1 |
| 5% | First sale of used vehicles | E.T. Art. 468-1 |
| 5% | Sanitary towels, tampons | E.T. Art. 468-1 |

### 1c. Zero-Rated (Exento con derecho a devolucion) [T1]

| Category | Legislation |
|----------|-------------|
| Exports of goods | E.T. Art. 479 |
| Exports of services | E.T. Art. 481 |
| Services provided from Colombia and used exclusively abroad | E.T. Art. 481(c) |
| Sale of gold to Banco de la Republica | E.T. Art. 481(b) |
| Raw materials for production of exported goods (Plan Vallejo) | E.T. Art. 481(a) |

**Key distinction:** Zero-rated (exento) suppliers CAN recover input IVA. This is different from excluded goods/services where no IVA recovery is permitted.

### 1d. Excluded Goods and Services (Excluido -- No IVA) [T1]

| Category | Legislation |
|----------|-------------|
| Basic food (rice, corn, wheat, potatoes, vegetables, fruits, eggs, milk, bread, salt) | E.T. Art. 424 |
| Live animals and unprocessed meat | E.T. Art. 424 |
| Medicines and pharmaceutical products | E.T. Art. 424 |
| Agricultural inputs (fertilizers, pesticides, seeds) | E.T. Art. 424 |
| Education services | E.T. Art. 476, numeral 6 |
| Health/medical services | E.T. Art. 476, numeral 1 |
| Public transport (urban and metropolitan) | E.T. Art. 476, numeral 2 |
| Financial services (interest, commissions on loans) | E.T. Art. 476, numeral 3 |
| Residential public utilities (first consumption tiers -- estratos 1 and 2) | E.T. Art. 476, numeral 4 |
| Internet services (estratos 1, 2, and 3) | E.T. Art. 476, numeral 7 |
| Residential rent | E.T. Art. 476, numeral 5 |
| Insurance for agricultural activities | E.T. Art. 476 |

**Key distinction:** Excluded (excluido) suppliers CANNOT recover input IVA. IVA paid on purchases becomes a cost.

### 1e. Impuesto Nacional al Consumo (INC) [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 8% | Restaurant and bar services (food and beverages consumed on premises) | E.T. Art. 512-1 |
| 8% | Mobile telephony services | E.T. Art. 512-1 |
| 8% | Sale of certain vehicles (value > 30,000 UVT) | E.T. Art. 512-3 |
| 16% | Sale of luxury vehicles (value > 30,000 UVT, certain categories) | E.T. Art. 512-3 |
| 4% | Sale of used vehicles by dealers | E.T. Art. 512-5 |

**INC is NOT IVA.** INC is a separate consumption tax. INC paid CANNOT be deducted as input tax credit. INC is filed on Form 310.

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]

- Sale (IVA generado / output IVA) or Purchase (IVA descontable / input IVA)
- Salaries, social security contributions (aportes parafiscales), tax payments, loan repayments, dividends = OUT OF SCOPE (never on IVA return)
- **Legislation:** E.T. Art. 420 (definition of taxable events: sale of goods, provision of services, import of goods)

### 2b. Determine Counterparty Location [T1]

- Colombia (domestic): supplier/customer country is CO
- Andean Community (CAN): Bolivia, Ecuador, Peru -- special treatment under Decision 599
- Other international: all other countries

### 2c. Determine IVA Rate from Invoice [T1]

- Calculate from amounts: `rate = iva_amount / base_amount * 100`
- Normalize to nearest standard rate: 0%, 5%, 19%
- If rate does not match any standard rate, flag for review [T2]

### 2d. Determine Expense Category [T1]

- Capital goods (activos fijos): goods with useful life > 1 year and used in business operations
- Goods for resale (mercancias): goods purchased to resell in ordinary course of business
- Operating expenses (gastos operacionales): overheads, services, supplies consumed
- **Legislation:** E.T. Art. 491 (IVA on capital goods -- deductible against income tax, not IVA, unless specific exceptions apply)

---

## Step 3: IVA Return Form Mapping (Form 300) [T1]

**Legislation:** DIAN Resolution, Form 300 -- Declaracion del Impuesto sobre las Ventas.

### Output IVA (IVA Generado)

| Line | Description | Rate |
|------|-------------|------|
| Line 27 | Taxable income at general rate (19%) | 19% |
| Line 28 | Taxable income at reduced rate (5%) | 5% |
| Line 29 | IVA generated at 19% | calculated |
| Line 30 | IVA generated at 5% | calculated |
| Line 31 | Total IVA generated on sales | sum |
| Line 32 | Exports (zero-rated -- exentos Art. 481) | 0% |
| Line 33 | Excluded income (excluidos) | N/A |

### Input IVA (IVA Descontable)

| Line | Description |
|------|-------------|
| Line 35 | IVA paid on imports |
| Line 36 | IVA paid on purchases of goods (not capital assets) |
| Line 37 | IVA paid on services |
| Line 38 | IVA descontable on capital goods (if applicable under Art. 258-1) |
| Line 39 | Total IVA descontable |

### Withholdings and Balance

| Line | Description |
|------|-------------|
| Line 40 | IVA withheld by third parties (retenciones de IVA que le practicaron) |
| Line 41 | Balance: IVA generado minus IVA descontable minus retenciones |
| Line 42 | Tax payable or credit balance carried forward |

---

## Step 4: IVA on Capital Goods (Activos Fijos) [T2]

**Legislation:** E.T. Art. 491; E.T. Art. 258-1.

### General Rule [T1]
IVA paid on acquisition of capital goods (activos fijos) is generally NOT deductible as input IVA (IVA descontable). Instead, it forms part of the cost of the asset.

### Exception -- Income Tax Discount (Art. 258-1) [T2]
IVA paid on capital goods may be taken as a discount (descuento) against income tax (not IVA). This applies to:
- Productive real capital goods (activos fijos reales productivos)
- The discount is taken on the income tax return, NOT the IVA return

**Flag for reviewer:** If client purchases capital goods with significant IVA, confirm whether income tax discount under Art. 258-1 applies. This requires analysis of asset classification and productive use.

### Exception -- Exporters [T1]
Exporters (zero-rated suppliers) CAN recover IVA on capital goods used exclusively in export activity, via refund mechanism (devolucion de saldos a favor).

---

## Step 5: Withholding of IVA (Retencion en la Fuente de IVA) [T1]

**Legislation:** E.T. Art. 437-1; E.T. Art. 437-2.

### Who Must Withhold [T1]

| Agent Type | Withholding Rate | Legislation |
|------------|-----------------|-------------|
| Grandes Contribuyentes | 15% of IVA charged by supplier | E.T. Art. 437-2(1) |
| Government entities (entidades estatales) | 50% of IVA charged | E.T. Art. 437-2(2) |
| Designated withholding agents (by DIAN resolution) | 15% of IVA charged | E.T. Art. 437-2 |
| Credit/debit card acquirers (on card payments) | 15% of IVA charged | E.T. Art. 437-2 |

### Mechanics [T1]

1. Buyer (withholding agent) pays supplier the net amount minus withheld IVA
2. Buyer remits withheld IVA to DIAN via Form 350 (Declaracion de Retenciones)
3. Supplier reports the withholding as a credit on their own IVA return (Line 40)
4. The withheld amount reduces the supplier's IVA payable

### Example [T1]

| Item | Amount |
|------|--------|
| Service fee (base) | COP 1,000,000 |
| IVA at 19% | COP 190,000 |
| Retencion de IVA (15% of IVA) | COP 28,500 |
| Amount paid to supplier | COP 1,161,500 |
| Amount remitted to DIAN by buyer | COP 28,500 |

---

## Step 6: Electronic Invoicing (Facturacion Electronica) [T1]

**Legislation:** E.T. Art. 616-1; Resolucion DIAN 000042 de 2020; Resolucion DIAN 000165 de 2023.

### Mandatory Requirements [T1]

| Requirement | Detail |
|-------------|--------|
| Who must issue | ALL IVA responsables must issue electronic invoices |
| Format | UBL 2.1 XML standard (Colombian adaptation) |
| Validation | Real-time validation by DIAN before delivery to buyer |
| CUFE | Each invoice has a unique electronic invoice code (Codigo Unico de Factura Electronica) |
| Consecutive numbering | Authorization range from DIAN required |
| Delivery | Must be delivered electronically to buyer; buyer must acknowledge receipt (acuse de recibo) |
| Storage | Minimum 5 years (E.T. Art. 632) |
| Contingency | If electronic system fails, paper contingency invoice allowed; must be transmitted within 48 hours |

### Document Types [T1]

| Document | Code | Usage |
|----------|------|-------|
| Factura Electronica de Venta | 01 | Standard sales invoice |
| Nota Credito | 91 | Credit note (adjustment, return) |
| Nota Debito | 92 | Debit note (additional charges) |
| Documento Soporte | 05 | Purchases from non-IVA-responsable suppliers |

### Documento Soporte [T1]

**Legislation:** Resolucion DIAN 000167 de 2021.

When purchasing from a No Responsable de IVA supplier (formerly regimen simplificado), the buyer must issue a "Documento Soporte en adquisiciones efectuadas a sujetos no obligados a expedir factura" to support the expense deduction and any applicable withholdings. This document must be transmitted electronically to DIAN.

---

## Step 7: IVA on Imports [T1]

**Legislation:** E.T. Art. 459; E.T. Art. 420(c).

### Import of Goods [T1]

| Element | Detail |
|---------|--------|
| Taxable event | Import of goods into Colombian customs territory |
| Tax base | CIF value + customs duties + other import charges |
| Rate | 19% (general) or 5% (if goods qualify for reduced rate) |
| Collection | IVA collected by DIAN at customs (Declaracion de Importacion) |
| Deductibility | Deductible as input IVA on Form 300, Line 35 |

### Import of Services [T2]

| Element | Detail |
|---------|--------|
| Taxable event | Services provided from abroad and used/consumed in Colombia |
| Tax base | Total amount paid for the service |
| Rate | 19% |
| Mechanism | Buyer self-assesses IVA (reverse charge) and includes in output IVA |
| Deductibility | Self-assessed IVA is simultaneously deductible as input IVA (net effect zero for fully taxable businesses) |
| Withholding | Buyer must withhold 100% of IVA on services from non-residents (E.T. Art. 437-2, numeral 3) |

**Legislation:** E.T. Art. 420, paragrafo 3; E.T. Art. 437-2, numeral 3.

---

## Step 8: Filing Periods and Deadlines [T1]

**Legislation:** E.T. Art. 600; E.T. Art. 601; Decreto 2229 de annual tax calendar.

### Filing Frequency [T1]

| Taxpayer Type | Period | Months Covered |
|---------------|--------|----------------|
| Grandes Contribuyentes | Bi-monthly | Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct, Nov-Dec |
| Other Responsables de IVA (income >= 92,000 UVT) | Bi-monthly | Same as above |
| Other Responsables de IVA (income < 92,000 UVT) | Quarterly (cuatrimestral) | Jan-Apr, May-Aug, Sep-Dec |

### Deadlines [T1]

Deadlines are set annually by decree (Decreto de plazos). Generally:

| Period | Approximate Deadline |
|--------|---------------------|
| Bi-monthly | Between 8th and 22nd of the month following the end of the bi-month, depending on last digit of NIT |
| Quarterly | Between 8th and 22nd of the month following the end of the quarter, depending on last digit of NIT |

**The exact date depends on the last digit of the NIT. Consult the annual tax calendar decree (Decreto de plazos) for the specific year.**

### Late Filing Penalties [T1]

| Penalty | Calculation | Legislation |
|---------|-------------|-------------|
| Penalty for late filing (extemporaneidad) | 5% of tax payable per month or fraction of month, up to 100% | E.T. Art. 641 |
| Penalty for late payment | Interest at the daily effective rate set by government (tasa de interes moratorio) | E.T. Art. 634 |
| Minimum penalty | 10 UVT | E.T. Art. 639 |

---

## Step 9: No Responsable de IVA (Simplified Regime) [T1]

**Legislation:** E.T. Art. 437, paragrafo 3; E.T. Art. 506.

### Threshold Conditions (ALL must be met to qualify) [T1]

| Condition | Threshold |
|-----------|-----------|
| Gross income in prior year | < 3,500 UVT |
| Maximum one commercial establishment | 1 |
| No customs activities (imports/exports) | None |
| No franchise, concession, or exploitation of intangibles | None |
| Not a user of free trade zone | N/A |
| Bank deposits and investments | < 3,500 UVT |
| Total consumption via credit/debit cards | < 3,500 UVT |
| Total value of purchases and consumption | < 3,500 UVT |
| Total cumulative value of bank consignments | < 3,500 UVT |

### Obligations of No Responsable [T1]

| Obligation | Requirement |
|------------|-------------|
| Charge IVA | NO -- cannot charge IVA on sales |
| File IVA returns | NO -- exempt from IVA filing |
| Issue electronic invoices | NO -- but must comply with POS system or equivalent |
| Recover input IVA | NO -- IVA on purchases is a cost |
| Register with DIAN (RUT) | YES -- must update RUT to reflect No Responsable status |
| Inscription visible | YES -- must display "No Responsable de IVA" at establishment |

---

## Step 10: Proportionality Rule (Prorrata) [T2]

**Legislation:** E.T. Art. 490.

### When It Applies [T2]
When a taxpayer makes both taxable supplies (gravadas) and excluded/exempt supplies (excluidas/exentas), input IVA must be apportioned.

### Calculation [T2]

```
Recovery % = (Taxable Income / Total Income) * 100
Deductible IVA = Total Input IVA * Recovery %
```

| Income Type | Included in Numerator | Included in Denominator |
|-------------|----------------------|------------------------|
| Taxable at 19% | Yes | Yes |
| Taxable at 5% | Yes | Yes |
| Zero-rated (exento Art. 481) | Yes | Yes |
| Excluded (excluido) | No | Yes |

**Flag for reviewer: pro-rata calculation must be confirmed by Contador Publico before applying. Annual adjustment may be required.**

---

## Step 11: Non-Deductible Input IVA [T1]

**Legislation:** E.T. Art. 488; E.T. Art. 490; E.T. Art. 491.

### Categories Where IVA is NOT Deductible [T1]

| Category | Legislation | Notes |
|----------|-------------|-------|
| Capital goods (activos fijos) -- general rule | E.T. Art. 491 | Exception: income tax discount under Art. 258-1 |
| Goods and services not related to taxable activity | E.T. Art. 488 | Must have direct/indirect nexus to taxable income |
| Personal consumption items | E.T. Art. 488 | Not related to business activity |
| Entertainment and representation (above limits) | E.T. Art. 107 (income tax deductibility limits apply) | Proportional limitation |
| Purchases from No Responsable suppliers (no Documento Soporte) | Resolucion DIAN 000167 | Must have valid Documento Soporte |
| Purchases without valid electronic invoice | E.T. Art. 771-2 | Invoice must meet all legal requirements |

### Deductibility Hierarchy [T1]

1. **Check: Is the supplier IVA responsable?** If No Responsable, no IVA is charged; ensure Documento Soporte is issued.
2. **Check: Is the purchase related to taxable business activity?** If no nexus, IVA is not deductible.
3. **Check: Is the purchase a capital good?** If yes, IVA goes to asset cost (not deductible on IVA return).
4. **Check: Does proportionality (prorrata) apply?** If business makes both taxable and excluded supplies, apply pro-rata.
5. **Check: Is the invoice valid?** Electronic invoice with CUFE required.

---

## Step 12: Key Thresholds and UVT Values [T1]

**Legislation:** E.T. Art. 868 (UVT definition).

| Threshold | Value | Notes |
|-----------|-------|-------|
| UVT (Unidad de Valor Tributario) 2025 | COP 49,799 | DIAN Resolution 000193 (Dec 2024) |
| UVT 2026 | COP 52,374 | DIAN Resolution 000238 (Dec 15, 2025); 5.17% IPC adjustment |
| No Responsable income threshold | 3,500 UVT | ~COP 183,309,000 (2026); ~COP 174,296,500 (2025) |
| Bi-monthly vs quarterly filing threshold | 92,000 UVT | Income in prior year |
| INC vehicle threshold (8% rate) | 30,000 UVT | Vehicle value |
| Minimum penalty | 10 UVT | ~COP 497,990 (2025) |

---

## Step 13: Andean Community (CAN) Special Rules [T2]

**Legislation:** Decision 599 of the Andean Community (CAN); E.T. Art. 420.

### Member Countries [T1]
Bolivia, Colombia, Ecuador, Peru.

### VAT Treatment for Intra-CAN Trade [T2]

| Transaction | Treatment |
|-------------|-----------|
| Export of goods to CAN member | Zero-rated (exento) in Colombia; importing country charges its own VAT |
| Import of goods from CAN member | IVA charged at Colombian rate on import |
| Services between CAN members | Place-of-supply rules under Decision 599 apply |

**Flag for reviewer:** CAN rules can be complex. Confirm specific treatment with Contador Publico for cross-border service transactions.

---

## Step 14: Free Trade Zones (Zonas Francas) [T2]

**Legislation:** E.T. Art. 420, paragrafo; Ley 1004 de 2005.

### General Rules [T2]

| Transaction | IVA Treatment |
|-------------|---------------|
| Sales from Colombia to Free Trade Zone (ZF) | Treated as export -- zero-rated (exento) |
| Sales from ZF to Colombia | Treated as import -- IVA at 19% |
| Sales within ZF (ZF to ZF) | Excluded from IVA |
| Imports into ZF from abroad | Excluded from IVA (no customs IVA) |

**Flag for reviewer:** Free Trade Zone transactions require careful documentation. Verify user type (industrial, commercial, or services) and applicable DIAN rulings.

---

## Step 15: IVA Refunds (Devolucion de Saldos a Favor) [T2]

**Legislation:** E.T. Art. 815; E.T. Art. 850; E.T. Art. 855.

### Who Can Request Refunds [T1]

| Category | Right to Refund |
|----------|----------------|
| Exporters (exentos Art. 481) | Yes -- automatic right |
| Taxpayers with persistent credit balances (saldos a favor) | Yes -- after 2 consecutive periods |
| Producers of excluded goods with input IVA | Yes -- under specific conditions (E.T. Art. 477) |

### Refund Process [T2]

| Step | Detail |
|------|--------|
| 1 | File IVA return showing credit balance (saldo a favor) |
| 2 | Submit refund request to DIAN (solicitud de devolucion) |
| 3 | DIAN has 50 business days to process (30 days for exporters) |
| 4 | DIAN may audit before approving (verificacion previa) |
| 5 | Refund issued via bank transfer or TIDIS (tax credit certificates) |

**Flag for reviewer:** Refund requests are frequently audited by DIAN. Ensure all supporting documentation (electronic invoices, customs declarations, bank statements) is complete and consistent.

---

## Step 16: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Contador Publico must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Contador Publico. Document gap.
```

---

## Step 17: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions. Each is tagged with its confidence tier.

### EC1 -- Restaurant meal expense (INC vs IVA) [T1]
**Situation:** Client pays for a business meal at a restaurant. Invoice shows 8% charge.
**Resolution:** The 8% is INC (Impuesto Nacional al Consumo), NOT IVA. INC is not deductible as input IVA. Report as operating expense; the 8% INC is a non-recoverable cost embedded in the expense.
**Legislation:** E.T. Art. 512-1; E.T. Art. 512-13.

### EC2 -- Purchase from No Responsable supplier [T1]
**Situation:** Client purchases goods from a small supplier who is No Responsable de IVA. No IVA is charged.
**Resolution:** No IVA entry on the return. Buyer must issue Documento Soporte (electronically transmitted to DIAN) to support the expense deduction. If applicable, buyer must apply retencion en la fuente (income tax withholding) on the payment.
**Legislation:** Resolucion DIAN 000167 de 2021.

### EC3 -- Software subscription from US provider (e.g., AWS, Google) [T1]
**Situation:** Monthly subscription from a US company, no IVA on invoice.
**Resolution:** Reverse charge applies. Buyer self-assesses 19% IVA on the service value. Report as output IVA (Line 29 contribution) and simultaneously claim as input IVA (Line 37). Net effect zero for fully taxable businesses. Buyer must also withhold 100% of the self-assessed IVA and remit to DIAN.
**Legislation:** E.T. Art. 420, paragrafo 3; E.T. Art. 437-2, numeral 3.

### EC4 -- Mixed business: taxable sales + restaurant (INC) [T2]
**Situation:** Client operates both a consulting firm (IVA at 19%) and a restaurant (INC at 8%). How to handle input IVA on shared expenses?
**Resolution:** Input IVA on expenses exclusively attributable to IVA-taxable activity is fully deductible. Input IVA on expenses exclusively attributable to INC activity (restaurant) is NOT deductible. Shared expenses must be apportioned using prorrata. Flag for reviewer: confirm apportionment methodology with Contador Publico.
**Legislation:** E.T. Art. 490.

### EC5 -- Credit note received [T1]
**Situation:** Client receives a credit note (nota credito) from a supplier.
**Resolution:** Reduce the original input IVA entry by the IVA amount on the credit note. The credit note must be an electronic document (Nota Credito Electronica, code 91) validated by DIAN.
**Legislation:** E.T. Art. 484; Resolucion DIAN 000042.

### EC6 -- Export of services [T1]
**Situation:** Colombian company provides consulting services to a foreign client. Service is used exclusively outside Colombia.
**Resolution:** Zero-rated (exento) under Art. 481(c). No IVA charged. Report on Line 32 of Form 300. Input IVA on costs related to this activity IS recoverable. Client may request IVA refund (devolucion).
**Legislation:** E.T. Art. 481(c).

### EC7 -- Sale of used capital goods [T2]
**Situation:** Client sells a computer that was previously used as a capital good.
**Resolution:** Sale of used capital goods is generally excluded from IVA (excluido) under E.T. Art. 424, provided the goods were used by the seller. However, if the seller is in the business of selling used goods, IVA applies. Flag for reviewer.
**Legislation:** E.T. Art. 424; E.T. Art. 420.

### EC8 -- Digital services from foreign providers to Colombian consumers [T2]
**Situation:** Foreign digital platform (Netflix, Spotify, etc.) charges Colombian consumers.
**Resolution:** Foreign providers of digital services must register for IVA in Colombia and charge 19% IVA. If the provider has NOT registered, the payment platform or financial intermediary must withhold the IVA. This does not affect the end consumer's IVA return. Flag for reviewer if client is a business subscriber.
**Legislation:** E.T. Art. 437-2, numeral 8; Resolucion DIAN 000051 de 2018.

### EC9 -- Goods donated to non-profit [T2]
**Situation:** Client donates inventory to a registered non-profit organization.
**Resolution:** Donations of goods are generally subject to IVA (treated as deemed sale). However, donations to entities listed in E.T. Art. 22 (non-profit entities of the special tax regime) may be excluded. Flag for reviewer: confirm the recipient's tax status and applicable exclusion.
**Legislation:** E.T. Art. 421(b); E.T. Art. 480.

### EC10 -- Retefuente vs RetIVA confusion [T1]
**Situation:** Client confuses income tax withholding (retencion en la fuente por renta) with IVA withholding (retencion de IVA).
**Resolution:** These are separate obligations filed on separate forms. Retencion en la fuente (income tax) is filed on Form 350 sections related to income tax. Retencion de IVA is also on Form 350 but in the IVA section. They have different rates and different bases. On the IVA return (Form 300), only IVA withholdings appear (Line 40).
**Legislation:** E.T. Art. 437-1 (RetIVA); E.T. Art. 365 et seq. (Retefuente renta).

---

## Step 18: INC Return (Form 310) -- Summary [T1]

**Legislation:** E.T. Art. 512-1 through 512-22.

| Field | Detail |
|-------|--------|
| Form | 310 -- Declaracion Impuesto Nacional al Consumo |
| Filing period | Bi-monthly (same periods as IVA for grandes contribuyentes) |
| Rate: Restaurants/bars | 8% on total consumption (food + beverages) |
| Rate: Telephony | 8% on service value |
| Rate: Vehicles | 8% or 16% depending on value and type |
| Deductibility | INC paid is NOT deductible as input IVA |
| Relationship to IVA | Separate tax; INC replaces IVA for covered activities |

### Restaurant Regime [T1]

| Rule | Detail |
|------|--------|
| Restaurants charging INC 8% | Do NOT charge IVA 19% on food/beverage sales |
| INC base | Total value of food and beverages consumed on premises |
| Tips (propinas) | NOT included in INC base |
| Takeout/delivery | Subject to INC if the establishment is primarily a restaurant |
| Franchise restaurants | Subject to INC |

---

## Step 19: Penalties and Interest Summary [T1]

**Legislation:** E.T. Art. 634--672.

| Infraction | Penalty | Legislation |
|------------|---------|-------------|
| Late filing (extemporaneidad) | 5% of tax per month or fraction, up to 100% | E.T. Art. 641 |
| Failure to file | 10% of tax per month or fraction, up to 200% | E.T. Art. 642 |
| Arithmetic errors | 30% of the difference in tax | E.T. Art. 646 |
| Failure to invoice | Closure of establishment for 3 days (first offense); 30 days (repeat) | E.T. Art. 657 |
| Failure to transmit electronic invoice | Penalty of 1% of invoices not transmitted, up to 15,000 UVT | E.T. Art. 651 |
| Late payment interest | Daily effective interest rate (tasa de usura certificada by Superfinanciera) | E.T. Art. 634 |

---

## Step 20: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard local sale, 19% IVA
**Input:** Colombian client sells consulting services to local customer, base COP 10,000,000, IVA COP 1,900,000.
**Expected output:** Form 300, Line 27 = COP 10,000,000, Line 29 = COP 1,900,000.

### Test 2 -- Purchase from local supplier, 19% IVA, operating expense
**Input:** Colombian client buys office supplies from local IVA-responsable supplier, base COP 500,000, IVA COP 95,000. Valid electronic invoice with CUFE.
**Expected output:** Form 300, Line 36 += COP 95,000. Input IVA deductible.

### Test 3 -- Restaurant meal (INC, not IVA)
**Input:** Client pays COP 200,000 for business lunch. Invoice shows INC 8% = COP 16,000.
**Expected output:** NO entry on Form 300 (IVA return). INC is not deductible as input IVA. Total expense = COP 216,000.

### Test 4 -- Export of services
**Input:** Colombian company invoices US client USD 5,000 for software development. Service used exclusively outside Colombia.
**Expected output:** Form 300, Line 32 (exports/exentos). No IVA charged. Input IVA on related costs IS recoverable.

### Test 5 -- Import of services (reverse charge)
**Input:** Colombian company pays US$1,000 (COP 4,200,000) for AWS cloud services. No IVA on invoice.
**Expected output:** Self-assess IVA: COP 4,200,000 * 19% = COP 798,000 output IVA. Simultaneously claim COP 798,000 as input IVA (Line 37). Net effect zero. Withhold 100% of IVA and remit to DIAN via Form 350.

### Test 6 -- Purchase of capital good
**Input:** Client purchases machinery for COP 50,000,000, IVA COP 9,500,000. Asset is productive capital.
**Expected output:** IVA of COP 9,500,000 is NOT deductible on Form 300 (IVA return). IVA forms part of asset cost. May be eligible for income tax discount under E.T. Art. 258-1 on income tax return. Flag for reviewer.

### Test 7 -- Sale at reduced rate (5%)
**Input:** Client sells processed food (coffee) at 5% rate, base COP 2,000,000, IVA COP 100,000.
**Expected output:** Form 300, Line 28 = COP 2,000,000, Line 30 = COP 100,000.

### Test 8 -- Withholding of IVA by Gran Contribuyente buyer
**Input:** Gran Contribuyente client purchases services from local supplier, base COP 3,000,000, IVA COP 570,000. Client is withholding agent.
**Expected output:** Client withholds 15% of IVA = COP 85,500. Pays supplier COP 3,484,500 (3,000,000 + 570,000 - 85,500). Remits COP 85,500 to DIAN on Form 350. Reports IVA descontable COP 570,000 on Form 300.

---

## PROHIBITIONS [T1]

- NEVER confuse IVA (19%/5%) with INC (8%/16%) -- they are separate taxes on separate returns
- NEVER allow INC to be deducted as input IVA
- NEVER classify capital goods IVA as deductible input IVA on Form 300 (general rule)
- NEVER file an IVA return for a No Responsable de IVA client
- NEVER omit Documento Soporte when purchasing from No Responsable suppliers
- NEVER omit reverse charge on services imported from abroad
- NEVER ignore the NIT-based deadline schedule -- exact date depends on last digit of NIT
- NEVER accept an invoice without valid CUFE as support for input IVA deduction
- NEVER confuse retencion en la fuente (income tax) with retencion de IVA
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 21: Reporting Obligations Summary [T1]

**Legislation:** E.T. Art. 574; RG DIAN (annual resolution on information reporting -- Resolucion de Medios Magneticos).

| Form | Description | Frequency | Deadline |
|------|-------------|-----------|----------|
| Form 300 | Declaracion de IVA | Bi-monthly or quarterly | Per NIT calendar |
| Form 310 | Declaracion de INC | Bi-monthly | Per NIT calendar |
| Form 350 | Declaracion de Retenciones en la Fuente | Monthly | Per NIT calendar |
| Medios Magneticos | Exogena (third-party information reporting) | Annual | Per DIAN resolution |
| Facturacion Electronica | Real-time electronic invoicing | Continuous | Each transaction |
| Documento Soporte | Purchases from No Responsable suppliers | Per transaction | Before expense deduction |

### Annual Information Reporting (Informacion Exogena) [T2]

| Element | Detail |
|---------|--------|
| What | Detailed annual report of all transactions with third parties |
| Who | All IVA responsables above DIAN-set thresholds |
| Content | Purchases, sales, retenciones practicadas, retenciones sufridas, IVA descontable, IVA generado, payroll |
| Format | XML per DIAN specifications |
| Penalty for non-compliance | Up to 15,000 UVT |

**Flag for reviewer:** Exogena reporting requirements change annually. Verify current year resolution and applicable thresholds with Contador Publico.

---

## Contribution Notes (For Adaptation to Other Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all form line numbers with the equivalent lines on your jurisdiction's VAT/IVA return form.
3. Replace IVA rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace the UVT values and thresholds with your jurisdiction's equivalent.
5. Replace the No Responsable thresholds with your jurisdiction's simplified regime equivalent.
6. Replace the electronic invoicing requirements with your jurisdiction's e-invoicing rules.
7. Replace the withholding regime with your jurisdiction's equivalent.
8. Have a licensed accountant in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
