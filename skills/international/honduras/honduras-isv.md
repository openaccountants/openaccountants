---
name: honduras-isv
description: Use this skill whenever asked to prepare, review, or create a Honduras ISV (Impuesto Sobre Ventas) return for any client. Trigger on phrases like "prepare ISV return", "do the ISV", "Honduras sales tax", "Honduras VAT", or any request involving Honduras consumption tax filing. ALWAYS read this skill before touching any Honduras ISV-related work.
---

# Honduras ISV Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Honduras |
| Jurisdiction Code | HN |
| Primary Legislation | Ley del Impuesto Sobre Ventas (ISV), Decreto 24-63 (as amended by Decreto 17-2010, Decreto 278-2013) |
| Supporting Legislation | Reglamento de la Ley del ISV; Codigo Tributario |
| Tax Authority | Servicio de Administracion de Rentas (SAR) |
| Filing Portal | https://www.sar.gob.hn (Portal SAR) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return form assignment, input tax recovery. Tier 2: partial exemption, free zone, maquila, tourism. Tier 3: complex structures, rulings. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and RTN (Registro Tributario Nacional)** [T1] -- 14-digit RTN
2. **ISV registration status** [T1]
3. **Filing period** [T1] -- monthly (standard)
4. **Industry/sector** [T2] -- impacts classification (maquila, free zone, tourism, agriculture)
5. **Does the business make exempt supplies?** [T2]
6. **Does the business import goods?** [T1]
7. **Is the business in a free trade zone (ZOLI/ZIP)?** [T2]
8. **Credit balance brought forward** [T1]

**If items 1-3 are unknown, STOP.**

---

## Step 1: ISV Rate Structure [T1]

**Legislation:** Ley del ISV, Article 5 (as amended).

### Standard Rate

| Rate | Application |
|------|-------------|
| 15% | Standard rate on all taxable sales of goods and services [T1] |

### Higher Rate

| Rate | Application |
|------|-------------|
| 18% | Alcoholic beverages, tobacco products, and luxury goods (specified in regulations) [T1] |

**Luxury goods subject to 18%** include [T1]:
- Alcoholic beverages of all kinds
- Tobacco and tobacco products
- Perfumes and cosmetics (imported, above threshold)
- Jewelry and precious stones
- Firearms and ammunition (non-military)
- Fireworks
- Jet skis, yachts, and pleasure boats

### Exempt Goods and Services [T1]

**Legislation:** Ley del ISV, Article 6.

**Exempt goods:**
- Unprocessed agricultural products (grains, fresh fruits, vegetables, fresh meats, eggs, milk)
- Basic food basket (canasta basica) -- 30+ items specified by regulation
- Medicines and pharmaceutical products (prescription)
- Agricultural inputs (fertilizers, insecticides, seeds, agricultural tools)
- Books, newspapers, educational materials
- Fuel and petroleum derivatives (subject to specific tax)
- Machinery for agricultural or industrial production

**Exempt services:**
- Health/medical services
- Educational services (authorized institutions)
- Financial services (interest, insurance premiums on life/health)
- Residential rental
- Public transportation
- Water and electricity (domestic, first tier)
- Legal services rendered in judicial proceedings [T2]

### Exports (0% -- Full Input Credit) [T1]
- Export of goods: zero-rated with full input credit recovery
- Export of services: may qualify if consumed outside Honduras [T2]

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (ISV cobrado -- output) or Purchase (ISV pagado -- input)
- Salaries, IHSS (social security), RAP (pension), ISR (income tax), loans = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (Honduras)
- Central American (Guatemala, El Salvador, Nicaragua, Costa Rica)
- International

### 2c. Determine ISV Rate [T1]
- 0% (export), 15% (standard), 18% (alcohol/tobacco/luxury), or exempt

---

## Step 3: ISV Return Form Structure (DEI-345 / SAR Form) [T1]

**Filed monthly via Portal SAR.**

### ISV Cobrado (Output)

| Line | Description |
|------|-------------|
| 1 | Ventas gravadas al 15% (Standard-rate taxable sales) |
| 2 | ISV cobrado al 15% |
| 3 | Ventas gravadas al 18% (Higher-rate sales) |
| 4 | ISV cobrado al 18% |
| 5 | Exportaciones (Exports at 0%) |
| 6 | Ventas exentas (Exempt sales) |
| 7 | Total ventas |
| 8 | Total ISV cobrado (Line 2 + Line 4) |

### ISV Pagado / Credito Fiscal (Input)

| Line | Description |
|------|-------------|
| 9 | ISV pagado en compras locales (ISV on local purchases) |
| 10 | ISV pagado en importaciones (ISV on imports) |
| 11 | Total ISV pagado |
| 12 | Ajustes (blocked/apportioned) |
| 13 | ISV pagado deducible (Net input) |

### Liquidacion

| Line | Description |
|------|-------------|
| 14 | ISV a pagar (Line 8 - Line 13) |
| 15 | Credito fiscal anterior |
| 16 | Retenciones |
| 17 | Total a pagar / saldo a favor |

---

## Step 4: ISV Retention [T1]

**Legislation:** Ley del ISV; SAR resolutions.

### Retention Agents [T1]

| Agent Type | Retention Rate |
|------------|---------------|
| Large taxpayers designated by SAR | 1% of purchase value [T1] |
| Government entities | 1% of purchase value [T1] |

### Treatment [T1]
- Supplier reports full output ISV
- Retained amount credited on Line 16
- Retention certificates required

---

## Step 5: Reverse Charge on Imported Services [T1]

**Legislation:** Ley del ISV, Article 3.

When a Honduras registered person receives taxable services from a non-resident:

1. Self-assess ISV at 15% (or 18% for applicable services) [T1]
2. Report as output ISV [T1]
3. Claim as input ISV if for taxable operations [T1]
4. Net effect: zero for fully taxable businesses [T1]

---

## Step 6: Deductibility Check

### Blocked Input ISV (No Recovery) [T1]

**Legislation:** Ley del ISV, Article 10.

- **Entertainment** -- meals, recreation (unless hospitality trade) [T1]
- **Motor vehicles** -- passenger vehicles (exception: rental, taxi, transport) [T1]
- **Personal use** [T1]
- **Exempt operations** [T1]
- **Purchases without valid factura fiscal** [T1]

### Invoice Requirement [T1]
- Factura fiscal authorized by SAR is required for input ISV credit
- CAI (Codigo de Autorizacion de Impresion) must be valid and not expired
- Electronic invoicing system being implemented [T2]

### Partial Exemption [T2]
- Direct attribution + proportional for common costs
- Flag for reviewer

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory ISV registration | All persons/entities making taxable sales must register [T1] |
| Large taxpayer designation | Designated by SAR resolution [T2] |

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Codigo Tributario; Ley del ISV, Article 12.

### Filing Deadlines

| Period | Deadline |
|--------|----------|
| Monthly ISV return | 10th of the month following the period [T1] |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | HNL 200 per day (maximum varies) [T1] |
| Late payment | 3% per month on unpaid tax (max 36%) [T1] |
| Failure to register | Fines + back-assessment [T1] |
| Failure to issue factura fiscal | Closure of business (temporary) + fines [T1] |
| Fraud | Criminal penalties + imprisonment [T1] |

---

## Step 9: Classification Matrix [T1]

### Domestic Purchases

| Category | ISV Rate | Input Credit | Notes |
|----------|---------|--------------|-------|
| Office supplies | 15% | Yes | |
| Commercial rent | 15% | Yes | |
| Residential rent | Exempt | No | |
| Electricity (commercial) | 15% | Yes | |
| Telephone/internet | 15% | Yes | |
| Motor car | 15% | BLOCKED | |
| Entertainment | 15% | BLOCKED | |
| Alcoholic beverages (purchase) | 18% | BLOCKED (entertainment) | |
| Professional services | 15% | Yes | |
| Insurance (general) | 15% | Yes | |
| Basic food items | Exempt | No | |
| Medicines | Exempt | No | |
| Agricultural machinery | Exempt | No | |

### Sales

| Category | ISV | Return Line |
|----------|-----|-------------|
| Domestic sale (standard) | 15% | Line 1, Line 2 |
| Alcohol/tobacco sales | 18% | Line 3, Line 4 |
| Export | 0% | Line 5 |
| Exempt supply | Exempt | Line 6 |

---

## Step 10: Free Trade Zone and Maquila Rules [T2]

**Legislation:** Ley de Zonas Libres (ZOLI); Ley de Zonas Industriales de Procesamiento (ZIP).

- ZOLI/ZIP companies: exempt from ISV on imports for export manufacturing
- Sales to domestic market from ZOLI/ZIP: subject to ISV as imports
- Maquila operations: special regime, inputs for export production exempt
- Flag for reviewer: free zone benefits require valid authorization

---

## Step 10a: Tax Invoice Requirements [T1]

**Legislation:** Ley del ISV; SAR regulations on facturacion.

### Required Invoice Contents [T1]

1. Name or razon social of the issuer
2. RTN of the issuer
3. CAI (Codigo de Autorizacion de Impresion) -- unique authorization code
4. Sequential number (pre-printed or electronic)
5. Date of issuance
6. Name and RTN of buyer (B2B transactions)
7. Description of goods or services
8. Quantity and unit price
9. Subtotal (base gravable)
10. ISV amount (15% or 18%)
11. Total amount
12. Fecha limite de emision (expiry date of CAI)

### CAI Validation Rules [T1]

- Every fiscal document must have a valid CAI
- CAI has an expiry date (fecha limite de emision) -- typically 12 months
- Expired CAI = INVALID invoice = NO input ISV credit [T1]
- CAI must be verified on SAR portal
- Businesses must request new CAI before expiry

### Electronic Invoicing [T2]

Honduras is implementing electronic invoicing:
- Designated taxpayers are migrating to Documento Tributario Electronico (DTE)
- DTE replaces paper facturas with CAI
- Electronic authorization by SAR system
- DTE rollout continues through 2025-2026 with phased mandatory adoption
- Flag for reviewer: confirm client's electronic invoicing obligations and DTE migration status

### Tax Amnesty -- Decreto No. 7-2026 [T2]

In early 2026, Honduras enacted Decreto No. 7-2026 establishing a four-month general tax amnesty for the regularization of material or formal tax obligations not complied with as of December 31, 2025. Taxes covered include ISV, ISR, Net Asset Tax, and withholding obligations. Financial penalties are waived under the amnesty. Flag for reviewer: confirm if client has outstanding ISV obligations that may benefit from this amnesty.

---

## Step 10b: Sector-Specific Rules [T2]

### Agriculture and Livestock

- Unprocessed agricultural products (canasta basica): exempt [T1]
- Processed food products: taxable at 15% [T1]
- Agricultural machinery: exempt [T1]
- Veterinary services: exempt [T1]
- Agrochemicals and fertilizers: exempt [T1]
- Coffee (green/unprocessed): exempt [T1]
- Coffee (roasted/processed): taxable at 15% [T1]

### Tourism

- Hotel accommodation: taxable at 15% [T1]
- Hotels under tourism incentive decree: may have ISV exemptions [T2]
- Restaurant services: taxable at 15% [T1]
- Tour operator services: taxable at 15% [T1]
- Flag for reviewer: confirm tourism incentive applicability with IHTT

### Construction and Real Estate

- Construction services: taxable at 15% [T1]
- Construction materials: taxable at 15% [T1]
- Sale of new real estate: taxable at 15% [T1]
- Sale of used real estate: exempt [T2]
- Residential rental: exempt [T1]
- Commercial rental: taxable at 15% [T1]

### Financial Services

- Interest on loans: exempt [T1]
- Banking commissions: taxable at 15% [T1]
- Insurance premiums (life/health): exempt [T1]
- Insurance premiums (property): taxable at 15% [T1]

### Telecommunications

- Mobile and fixed-line services: taxable at 15% [T1]
- Internet services: taxable at 15% [T1]
- Cable/satellite TV: taxable at 15% [T1]
- Prepaid phone cards: ISV included in sale price [T1]

---

## Step 10c: Libro de Compras y Ventas [T1]

All ISV taxpayers must maintain:

- **Libro de Compras**: all purchases with factura details, RTN of supplier, date, base, ISV, total
- **Libro de Ventas**: all sales with factura details, RTN of customer (B2B), date, base, ISV (by rate: 15% and 18%), total
- Chronological order required
- Available for SAR inspection
- Retention: minimum 5 years from end of fiscal year
- Summary totals must reconcile to the ISV return

---

## PROHIBITIONS [T1]

- NEVER let AI guess ISV classification
- NEVER allow input credit on blocked categories
- NEVER allow input credit without valid factura fiscal with valid CAI
- NEVER confuse 15% rate with 18% rate -- check product category
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse zero-rated exports with exempt supplies
- NEVER compute any number -- all arithmetic is handled by the deterministic engine

---

## Step 11: Edge Case Registry

### EC1 -- Alcohol purchase for resale (liquor store) [T1]
**Situation:** Liquor store purchases alcoholic beverages for resale.
**Resolution:** ISV at 18% applies. Input ISV IS recoverable because the purchase is for taxable resale (not entertainment/personal consumption). Entertainment block does not apply to inventory for resale.

### EC2 -- Imported software from US [T1]
**Situation:** Honduras company subscribes to US cloud software. No ISV.
**Resolution:** Self-assess ISV at 15%. Output and input. Net = zero if for taxable operations.

### EC3 -- Mixed-rate invoice (restaurant selling food and alcohol) [T1]
**Situation:** Restaurant invoice includes food (15%) and alcohol (18%).
**Resolution:** Split by line item. Food at 15%. Alcohol at 18%. If not split, apply 18% to alcohol portion and 15% to food.

### EC4 -- Credit notes [T1]
**Situation:** Client issues credit note.
**Resolution:** Reduce output ISV. Report net figures. Proper credit note with CAI required.

### EC5 -- Tourism sector hotel [T2]
**Situation:** Hotel registered under Tourism Incentives Law.
**Resolution:** Hotels may have ISV exemptions under tourism incentive legislation. Flag for reviewer: confirm specific incentive decree and applicable benefits.

### EC6 -- Agricultural first sale [T2]
**Situation:** Farmer sells corn directly.
**Resolution:** Unprocessed agricultural products are exempt at first sale. Confirm product is on exempt list. Flag for reviewer.

### EC7 -- Import of luxury goods [T1]
**Situation:** Company imports perfumes from France.
**Resolution:** ISV at 18% applies (luxury goods category). Paid at customs. Input credit available if for taxable resale.

### EC8 -- Government contract [T1]
**Situation:** Company provides services to government entity.
**Resolution:** Government retains 1% of invoice value. Full ISV charged. Retention credit claimed on Line 16.

---

## Step 12: Test Suite

### Test 1 -- Standard local purchase, 15%
**Input:** HN supplier, office supplies, gross HNL 11,500, ISV HNL 1,500, net HNL 10,000. Valid factura.
**Expected output:** Line 9 = HNL 1,500 input ISV. Full recovery.

### Test 2 -- Export, zero-rated
**Input:** Exporter ships coffee to US, net HNL 500,000.
**Expected output:** Line 5 = HNL 500,000. No output ISV. Input ISV fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase sedan HNL 400,000, ISV HNL 60,000.
**Expected output:** ISV HNL 60,000 BLOCKED. No input credit.

### Test 4 -- Alcohol sale at 18%
**Input:** Liquor store sells rum HNL 5,900 (HNL 5,000 + HNL 900 ISV at 18%).
**Expected output:** Line 3 = HNL 5,000. Line 4 = HNL 900.

### Test 5 -- Imported services, reverse charge
**Input:** US consulting firm, USD 2,000 (~ HNL 49,400). No ISV.
**Expected output:** Self-assess output ISV = HNL 7,410 (15%). Input = HNL 7,410. Net = zero.

### Test 6 -- Exempt supply (medical)
**Input:** Clinic earns HNL 100,000 from patient fees.
**Expected output:** Line 6 = HNL 100,000. No output ISV. Input ISV NOT recoverable.

### Test 7 -- Mixed food/alcohol restaurant sale
**Input:** Restaurant bill: food HNL 1,000 (15% ISV = HNL 150) + alcohol HNL 500 (18% ISV = HNL 90).
**Expected output:** Line 2 = HNL 150. Line 4 = HNL 90. Total ISV = HNL 240.

### Test 8 -- Purchase without valid CAI
**Input:** Supplier provides invoice with expired CAI. ISV HNL 750.
**Expected output:** ISV HNL 750 NOT deductible. Invalid fiscal document.

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

- Services generally taxable where the supplier is located [T1]
- Services related to real estate: taxable where property is located [T1]
- Services consumed outside Honduras by non-residents: may be zero-rated [T2]
- Flag for reviewer: cross-border service classification

### Self-Supply (Autoconsumo) [T1]

- Withdrawal of goods for personal use or free provision of services: taxable event [T1]
- ISV at applicable rate (15% or 18%) on fair market value [T1]
- Report as output ISV [T1]

### Barter Transactions [T1]

- Barter treated as two sales -- each party reports ISV on fair market value [T1]

### Installment Sales [T1]

- ISV due at time of delivery, not at each payment installment [T1]

### Credit Card / Digital Payment Processing [T1]

- All sales made via credit/debit card must be reported with the card processor details
- Card processors may be designated as ISV withholding agents [T2]

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
