---
name: nicaragua-iva
description: Use this skill whenever asked to prepare, review, or create a Nicaragua IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "Nicaragua VAT", or any request involving Nicaragua value added tax filing. ALWAYS read this skill before touching any Nicaragua IVA-related work.
---

# Nicaragua IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Nicaragua |
| Jurisdiction Code | NI |
| Primary Legislation | Ley de Concertacion Tributaria (LCT), Ley 822 (as amended by Ley 987) |
| Supporting Legislation | Reglamento de la LCT (Decreto 01-2013); Codigo Tributario |
| Tax Authority | Direccion General de Ingresos (DGI) |
| Filing Portal | https://www.dgi.gob.ni (Ventanilla Electronica Tributaria - VET) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return form, input recovery, calculations. Tier 2: partial exemption, free zone, cooperative treatments. Tier 3: complex structures, rulings. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and RUC (Registro Unico del Contribuyente)** [T1]
2. **Tax regime** [T1] -- Regimen General or Cuota Fija (fixed-fee small taxpayer)
3. **Filing period** [T1] -- monthly (standard)
4. **Industry/sector** [T2]
5. **Does the business make exempt supplies?** [T2]
6. **Does the business import goods?** [T1]
7. **Is the business in a free trade zone?** [T2]
8. **Credit balance brought forward** [T1]

**If items 1-3 are unknown, STOP.**

---

## Step 1: IVA Rate Structure [T1]

**Legislation:** LCT (Ley 822), Articles 107, 109, 114, 115, 127.

### Standard Rate

| Rate | Application |
|------|-------------|
| 15% | Standard rate on all taxable transfers of goods and services [T1] |

### Cuota Fija (Small Taxpayer Regime) [T1]

| Feature | Detail |
|---------|--------|
| Eligibility | Monthly income up to NIO 100,000 and inventory up to NIO 500,000 |
| Tax | Fixed monthly fee (cuota fija) determined by DGI based on income level |
| IVA | Cuota Fija taxpayers do NOT charge IVA, do NOT claim input credits |

### Exempt Goods [T1]

**Legislation:** LCT, Articles 114-115.

- Basic food basket (canasta basica): rice, beans, corn, sugar, cooking oil, eggs, milk, fresh meats, fresh fish, fresh fruits and vegetables, bread, salt, coffee, tortillas
- Medicines and pharmaceutical products
- Agricultural inputs (fertilizers, insecticides, seeds, tools)
- Books, newspapers, school supplies
- Fuel and petroleum derivatives (subject to Impuesto Especifico al Consumo -- IEC)
- Machinery for agricultural production
- Raw materials for artisanal production

### Exempt Services [T1]

- Health/medical services
- Educational services (authorized institutions)
- Financial services (interest, insurance premiums)
- Residential rental
- Public transportation
- Water (domestic supply)
- Electricity (domestic, up to 300 kWh/month)

### Exports (0% -- Full Input Credit) [T1]
- Export of goods: zero-rated with full input credit recovery
- Export of services: services consumed outside Nicaragua [T2]

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (IVA trasladado -- output) or Purchase (IVA acreditable -- input)
- Salaries, INSS (social security), IR (income tax), INATEC (training levy), loans = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (Nicaragua)
- Central American (Guatemala, El Salvador, Honduras, Costa Rica)
- International

### 2c. Determine IVA Rate [T1]
- 0% (export), 15% (standard), or exempt

---

## Step 3: IVA Return Form Structure [T1]

**Filed monthly via VET.**

### IVA Trasladado (Output)

| Line | Description |
|------|-------------|
| 1 | Ingresos gravados (Taxable revenue) |
| 2 | IVA trasladado (Line 1 x 15%) |
| 3 | Exportaciones (Exports at 0%) |
| 4 | Ingresos exentos (Exempt revenue) |
| 5 | Total ingresos |
| 6 | IVA en importaciones auto-declarado |
| 7 | Total IVA trasladado (Line 2 + Line 6) |

### IVA Acreditable (Input)

| Line | Description |
|------|-------------|
| 8 | IVA en compras locales |
| 9 | IVA en importaciones |
| 10 | Total IVA acreditable |
| 11 | Ajustes (blocked/apportioned) |
| 12 | IVA acreditable neto |

### Liquidacion

| Line | Description |
|------|-------------|
| 13 | IVA a pagar (Line 7 - Line 12) |
| 14 | Saldo a favor anterior |
| 15 | Retenciones de IVA |
| 16 | Total a pagar / saldo a favor |

---

## Step 4: IVA Retention [T1]

**Legislation:** LCT, Articles 122-123.

### Retention Agents [T1]

| Agent Type | Retention Rate |
|------------|---------------|
| Large taxpayers (Grandes Contribuyentes) | 2% of purchase value (as IVA advance) [T1] |
| Government entities | 2% of purchase value [T1] |
| Purchasers of agricultural products from small producers | Varies [T2] |

### Self-Retention (Auto-retencion) [T1]
- Large taxpayers may be required to self-retain IVA on certain transactions
- Flag for reviewer: confirm self-retention obligations

---

## Step 5: Reverse Charge on Imported Services [T1]

**Legislation:** LCT, Article 110.

When a Nicaragua registered person receives services from a non-resident:

1. Self-assess IVA at 15% [T1]
2. Report as output IVA [T1]
3. Claim as input if for taxable operations [T1]
4. Net = zero for fully taxable businesses [T1]

---

## Step 6: Deductibility Check

### Blocked Input IVA (No Recovery) [T1]

**Legislation:** LCT, Article 117.

- **Entertainment** -- meals, recreation (unless hospitality) [T1]
- **Motor vehicles** -- passenger vehicles (exception: rental, taxi, transport) [T1]
- **Personal use** [T1]
- **Exempt operations** [T1]
- **Purchases without valid factura** [T1]

### Invoice Requirement [T1]
- Valid factura authorized by DGI required for input credit
- Factura must contain: RUC, description, IVA breakdown, sequential number
- Electronic invoicing being phased in [T2]

### Partial Exemption [T2]
- Direct attribution + proportional method
- `Recovery % = (Taxable Revenue / Total Revenue) * 100`
- Flag for reviewer

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory IVA registration | All persons making taxable sales above Cuota Fija thresholds |
| Cuota Fija eligibility | Monthly income up to NIO 100,000, inventory up to NIO 500,000 |
| Large taxpayer | Designated by DGI resolution |

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Codigo Tributario; LCT.

### Filing Deadlines

| Period | Deadline |
|--------|----------|
| Monthly IVA return | 15th of the month following the period [T1] |
| Monthly IVA retention | 5th of the following month [T1] |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | NIO 750 to NIO 1,500 per return [T1] |
| Late payment | 2.5% per month on unpaid tax (recargo moratorio) [T1] |
| Failure to register | Fines + back-assessment [T1] |
| Failure to issue factura | Closure of business (temporary) + fines [T1] |
| Fraud | Criminal penalties [T1] |

---

## Step 9: Classification Matrix [T1]

### Domestic Purchases

| Category | IVA Rate | Input Credit | Notes |
|----------|---------|--------------|-------|
| Office supplies | 15% | Yes | |
| Commercial rent | 15% | Yes | |
| Residential rent | Exempt | No | |
| Electricity (commercial) | 15% | Yes | |
| Telephone/internet | 15% | Yes | |
| Motor car | 15% | BLOCKED | |
| Entertainment | 15% | BLOCKED | |
| Professional services | 15% | Yes | |
| Insurance (general) | 15% | Yes | |
| Basic food (canasta basica) | Exempt | No | |
| Medicines | Exempt | No | |
| Fuel | Exempt (IEC applies) | No | |

### Sales

| Category | IVA | Return Line |
|----------|-----|-------------|
| Domestic sale (standard) | 15% | Line 1, Line 2 |
| Export | 0% | Line 3 |
| Exempt | Exempt | Line 4 |

---

## Step 10: Free Trade Zone Rules [T2]

**Legislation:** Ley de Zonas Francas Industriales de Exportacion (Decreto 46-91).

- Free zone companies: exempt from IVA on imports and local purchases for export production
- Sales to domestic market: subject to IVA
- Free zone operators must comply with export ratio requirements
- Flag for reviewer: free zone benefits require valid authorization from CNZF

---

## Step 10a: Tax Invoice Requirements [T1]

**Legislation:** LCT; Codigo Tributario; DGI Resoluciones.

A valid factura must contain:

1. Name or razon social of the issuer
2. RUC number of the issuer
3. Sequential pre-printed number authorized by DGI
4. Date of issuance
5. Name and RUC of the buyer (for B2B above threshold)
6. Description of goods or services
7. Quantity and unit price
8. Subtotal (base imponible)
9. IVA amount (15%)
10. Total amount
11. Authorization number from DGI
12. Expiry date of the authorization (fecha de vencimiento)

**Simplified receipts:** For small transactions to final consumers, a simplified receipt may be used (no buyer details required).

**Key rule:** Input IVA is ONLY claimable with a factura that contains all required elements and is within its validity period [T1].

---

## Step 10b: Sector-Specific Rules [T2]

### Agriculture and Livestock

- Unprocessed agricultural products are exempt from IVA [T1]
- Processed food products are taxable at 15% [T1]
- Agricultural cooperatives: may have special IVA exemptions under cooperative legislation [T2]
- Inputs for agricultural production (fertilizers, seeds, insecticides): exempt [T1]
- Veterinary services: taxable at 15% [T1]
- Flag for reviewer: agricultural sector has overlapping legislation. Confirm product classification.

### Tourism and Hospitality

- Hotel accommodation: taxable at 15% [T1]
- Restaurant services: taxable at 15% [T1]
- Tour operator services: taxable at 15% [T1]
- Hotels under INTUR (Instituto Nicaraguense de Turismo) incentives may have IVA exemptions [T2]
- Flag for reviewer: confirm INTUR incentive applicability

### Financial Services

- Interest on loans: exempt [T1]
- Banking commissions and fees: taxable at 15% [T1]
- Insurance premiums (life/health): exempt [T1]
- Insurance premiums (general/property): taxable at 15% [T1]
- Flag for reviewer: distinguish between exempt financial intermediation and taxable fees

### Construction

- Construction services: taxable at 15% [T1]
- Sale of new real estate: taxable at 15% [T1]
- Sale of used real estate: exempt [T2]
- Construction materials: taxable at 15% [T1]
- Flag for reviewer: real estate transactions require careful classification

---

## Step 10c: IVA on Digital Services [T2]

**Legislation:** LCT amendments.

- Digital services provided by non-residents to Nicaraguan consumers are increasingly subject to IVA
- Streaming services, digital advertising, cloud computing: may require reverse charge or registration
- Flag for reviewer: digital services taxation is evolving. Confirm current rules with DGI.

---

## Step 10d: Libro de Compras y Ventas [T1]

All IVA taxpayers must maintain:

- **Libro de Compras** (Purchase ledger): all purchases with factura number, RUC of supplier, date, base amount, IVA, total
- **Libro de Ventas** (Sales ledger): all sales with factura number, RUC of customer (B2B), date, base amount, IVA, total
- Ledgers must be kept in chronological order
- Available for DGI inspection at any time
- Summary totals reconcile to the IVA return
- Retention: minimum 4 years from the end of the fiscal year

---

## PROHIBITIONS [T1]

- NEVER let AI guess IVA classification
- NEVER allow input credit on blocked categories
- NEVER allow input credit without valid factura
- NEVER allow Cuota Fija taxpayers to charge or claim IVA
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse zero-rated exports with exempt supplies
- NEVER compute any number -- all arithmetic is handled by the deterministic engine

---

## Step 11: Edge Case Registry

### EC1 -- Cuota Fija taxpayer selling to general regime buyer [T1]
**Situation:** Cuota Fija taxpayer sells goods. Buyer wants input credit.
**Resolution:** Cuota Fija taxpayer does NOT charge IVA. Buyer CANNOT claim input credit. No IVA is on the invoice.

### EC2 -- Imported software [T1]
**Situation:** Nicaragua company subscribes to US cloud service. No IVA.
**Resolution:** Self-assess IVA at 15%. Output and input. Net = zero.

### EC3 -- Cooperative transactions [T2]
**Situation:** Agricultural cooperative sells processed goods.
**Resolution:** Cooperatives have special tax treatments under LCT. Some cooperative transactions may be exempt. Flag for reviewer: confirm cooperative's tax status.

### EC4 -- Credit notes [T1]
**Situation:** Client issues credit note.
**Resolution:** Reduce output IVA. Report net. Proper nota de credito required.

### EC5 -- Export of services [T2]
**Situation:** IT company provides software development to US client.
**Resolution:** May qualify as export of services (zero-rated) if consumed outside Nicaragua. Flag for reviewer: confirm place of consumption.

### EC6 -- Electricity above domestic threshold [T1]
**Situation:** Business consuming more than 300 kWh/month.
**Resolution:** Commercial electricity above 300 kWh threshold is subject to IVA at 15%. Input credit available.

### EC7 -- Government retention [T1]
**Situation:** Company provides services to government entity.
**Resolution:** Government retains 2% of purchase value. Full IVA charged. Retention credit on Line 15.

### EC8 -- Purchase from informal sector [T2]
**Situation:** Business purchases goods from unregistered street vendor.
**Resolution:** No factura = no input credit. IVA cannot be claimed without valid fiscal documentation.

---

## Step 12: Test Suite

### Test 1 -- Standard local purchase, 15%
**Input:** NI supplier, office supplies, gross NIO 11,500, IVA NIO 1,500, net NIO 10,000. Valid factura.
**Expected output:** Line 8 = NIO 1,500 input IVA. Full recovery.

### Test 2 -- Export, zero-rated
**Input:** Exporter ships beef to US, net NIO 500,000.
**Expected output:** Line 3 = NIO 500,000. No output IVA. Input IVA fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase sedan NIO 600,000, IVA NIO 90,000.
**Expected output:** IVA NIO 90,000 BLOCKED. No input credit.

### Test 4 -- Imported services, reverse charge
**Input:** US consultant, USD 2,000 (~ NIO 73,000). No IVA.
**Expected output:** Self-assess output IVA = NIO 10,950 (15%). Input = NIO 10,950. Net = zero.

### Test 5 -- Cuota Fija taxpayer
**Input:** Small shop, monthly income NIO 50,000. Cuota Fija regime.
**Expected output:** No IVA return filed. Fixed monthly fee paid. No input credit claimed.

### Test 6 -- Exempt supply (medical)
**Input:** Clinic earns NIO 200,000 from patient fees.
**Expected output:** Line 4 = NIO 200,000. No output IVA. Input IVA NOT recoverable.

### Test 7 -- Government retention
**Input:** Services to government NIO 100,000 + IVA NIO 15,000. Government retains 2% of NIO 100,000 = NIO 2,000.
**Expected output:** Output IVA = NIO 15,000. Retention credit (Line 15) = NIO 2,000.

### Test 8 -- Entertainment, blocked
**Input:** Client dinner NIO 1,150 inclusive of IVA NIO 150.
**Expected output:** IVA NIO 150 BLOCKED. No input credit.

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

## Step 14: Additional Rules [T1]

### Place of Supply [T2]

- Services generally taxable where the supplier is domiciled [T1]
- Services related to real estate: taxable where property is located [T1]
- Export of services: services consumed outside Nicaragua by non-residents may be zero-rated [T2]
- Digital services from abroad: subject to IVA at 15% via reverse charge [T2]
- Flag for reviewer: cross-border service classification requires analysis

### Self-Supply (Autoconsumo) [T1]

**Legislation:** LCT, Article 108.

- Withdrawal of goods for personal use: taxable event [T1]
- IVA at 15% on fair market value [T1]
- Report as output IVA [T1]

### Barter Transactions [T1]

- Barter treated as two sales [T1]
- Each party reports IVA on fair market value [T1]

### Installment Sales [T1]

- IVA due at time of delivery [T1]

### Record Retention [T1]

- All fiscal documents, accounting records, and IVA returns must be retained for minimum 4 years from end of fiscal year
- DGI may audit any period within the statute of limitations
- Electronic records must be maintained in accessible format

### IEC (Impuesto Especifico al Consumo) Interaction [T1]

**Legislation:** LCT, Titulo III.

- IEC is a selective consumption tax on specific goods (alcohol, tobacco, vehicles, soft drinks)
- IEC is separate from IVA and NOT reported on the IVA return
- However, IVA is calculated on the price INCLUSIVE of IEC
- This means the IVA base includes the IEC amount [T1]
- Example: Product price NIO 100 + IEC 30 = 130. IVA = 130 x 15% = 19.50 [T1]

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
