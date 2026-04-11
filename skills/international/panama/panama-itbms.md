---
name: panama-itbms
description: Use this skill whenever asked to prepare, review, or create a Panama ITBMS (Impuesto de Transferencia de Bienes Muebles y Servicios) return for any client. Trigger on phrases like "prepare ITBMS return", "do the ITBMS", "Panama VAT", "Panama tax", or any request involving Panama consumption tax filing. Also trigger when classifying transactions for ITBMS purposes. This skill contains the complete Panama ITBMS classification rules, return form mappings, deductibility rules, and filing deadlines. ALWAYS read this skill before touching any ITBMS-related work.
---

# Panama ITBMS Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Panama |
| Jurisdiction Code | PA |
| Primary Legislation | Codigo Fiscal de Panama (Fiscal Code), Title IX -- ITBMS (as amended by Ley 8 de 2010, Ley 49 de 2009) |
| Supporting Legislation | Decreto Ejecutivo 84 de 2005 (Reglamento ITBMS); Resoluciones DGI |
| Tax Authority | Direccion General de Ingresos (DGI) |
| Filing Portal | https://dgi.mef.gob.pa (E-Tax 2.0) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return form assignment, input tax recovery, derived calculations. Tier 2: partial exemption, SEM/free zone, Colon Free Zone treatments, territorial tax interaction. Tier 3: complex group structures, advance rulings, multinational structuring. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and RUC (Registro Unico de Contribuyente)** [T1]
2. **ITBMS registration status** [T1] -- registered or not
3. **Filing period** [T1] -- monthly (standard)
4. **Industry/sector** [T2] -- impacts classification (Colon Free Zone, SEM, banking, tourism)
5. **Does the business make exempt supplies?** [T2] -- partial attribution
6. **Does the business import goods?** [T1]
7. **Is the business in a special economic zone (SEM, Colon Free Zone, Ciudad del Saber)?** [T2]
8. **Credit balance brought forward** [T1]
9. **Does the business earn foreign-source income?** [T2] -- Panama has territorial taxation

**If items 1-3 are unknown, STOP.**

---

## Step 1: ITBMS Rate Structure [T1]

**Legislation:** Fiscal Code, Article 1057-V.

### Standard Rate

| Rate | Application |
|------|-------------|
| 7% | Standard rate on taxable transfers of movable goods and services [T1] |

### Special Rates

| Rate | Application |
|------|-------------|
| 10% | Alcoholic beverages and hotel/short-term accommodation services [T1] |
| 15% | Tobacco and tobacco-derived products [T1] |

### Exempt Goods and Services (No ITBMS) [T1]

**Legislation:** Fiscal Code, Articles 1057-V(5), 1057-V(6).

**Exempt goods:**
- Unprocessed food (rice, beans, corn, fresh fruits, vegetables, fresh meats, fresh fish, eggs, milk)
- Basic food basket (canasta basica familiar)
- Medicines and pharmaceutical products (prescribed)
- Agricultural inputs (fertilizers, seeds, pesticides)
- Books, newspapers, educational materials
- Fuel and petroleum derivatives (subject to specific fuel tax)
- Machinery and equipment for agricultural use

**Exempt services:**
- Financial services (interest, insurance premiums on life policies)
- Medical and health services
- Educational services (approved institutions)
- Residential rental
- Public transportation
- Electricity (domestic, up to threshold)
- Water (domestic supply)
- Professional services of regulated professions (lawyers, doctors, engineers, architects, CPAs) -- NOTE: this is a significant difference from most countries [T1]

### Exports (0% -- Full Input Credit) [T1]
- Export of goods: zero-rated with full input credit recovery
- Export of services: services consumed outside Panama may qualify [T2]

---

## Step 2: Territorial Tax System -- Key Interaction [T2]

**Panama does NOT tax foreign-source income.** This has ITBMS implications:

- Services rendered entirely outside Panama to non-resident clients: NOT subject to ITBMS [T1]
- Goods exported: zero-rated (input credit allowed) [T1]
- Services rendered in Panama but paid from abroad: subject to ITBMS if consumed in Panama [T2]
- Re-invoicing / intermediation services: complex -- flag for reviewer [T3]
- Input ITBMS on costs related to non-taxable foreign operations: NOT recoverable unless attributable to taxable domestic operations [T2]

**Flag for reviewer: the interaction between territorial taxation and ITBMS recovery requires careful analysis of the source and place of consumption of each service.**

---

## Step 3: Transaction Classification Rules

### 3a. Determine Transaction Type [T1]
- Sale/transfer (ITBMS causado -- output) or Purchase (ITBMS soportado -- input)
- Salaries, CSS (social security), income tax, loan repayments, dividends = OUT OF SCOPE

### 3b. Determine Counterparty Location [T1]
- Domestic (Panama)
- Colon Free Zone / SEM / Special zones
- International

### 3c. Determine ITBMS Rate [T1]
- 0% (export), 7% (standard), 10% (alcohol/accommodation), 15% (tobacco), or exempt

### 3d. Determine Expense Category [T1]
- Capital goods: equipment, machinery, vehicles
- Inventory: goods for resale
- Operating expenses: everything else

---

## Step 4: ITBMS Return Form Structure (Formulario 430) [T1]

**Filed monthly via E-Tax 2.0.**

### Section I -- ITBMS Causado (Output)

| Line | Description |
|------|-------------|
| 1 | Ventas gravadas al 7% (Taxable sales at 7%) |
| 2 | ITBMS causado al 7% |
| 3 | Ventas gravadas al 10% (Alcohol/accommodation) |
| 4 | ITBMS causado al 10% |
| 5 | Ventas gravadas al 15% (Tobacco) |
| 6 | ITBMS causado al 15% |
| 7 | Exportaciones (Exports -- 0%) |
| 8 | Operaciones exentas (Exempt operations) |
| 9 | ITBMS en importaciones (ITBMS on imports, self-assessed) |
| 10 | Total ITBMS causado |

### Section II -- ITBMS Soportado (Input/Credit)

| Line | Description |
|------|-------------|
| 11 | ITBMS pagado en compras locales |
| 12 | ITBMS pagado en importaciones |
| 13 | Total ITBMS soportado |
| 14 | Ajustes (blocked/apportioned) |
| 15 | ITBMS soportado deducible |

### Section III -- Liquidacion

| Line | Description |
|------|-------------|
| 16 | ITBMS neto (Line 10 - Line 15) |
| 17 | Saldo a favor anterior |
| 18 | Retenciones |
| 19 | Total a pagar / saldo a favor |

---

## Step 5: Reverse Charge on Imported Services [T1]

**Legislation:** Fiscal Code, Article 1057-V(2).

When a Panama registered person receives taxable services from a non-resident:

1. Self-assess ITBMS at 7% [T1]
2. Report as output ITBMS (Line 9) [T1]
3. Claim as input ITBMS (Line 13) if used for taxable operations [T1]
4. Net effect: zero for fully taxable businesses [T1]

### Important Exception -- Professional Services [T1]
- If the imported service falls within the regulated professions exemption (legal, medical, engineering, architecture, accounting), it is EXEMPT from ITBMS even when imported
- Flag for reviewer: confirm whether the service type would be exempt domestically [T2]

---

## Step 6: Deductibility Check

### Blocked Input ITBMS (No Recovery) [T1]

**Legislation:** Fiscal Code, Article 1057-V(10).

- **Entertainment** -- meals, drinks, recreation (unless hospitality trade) [T1]
- **Motor vehicles** -- passenger vehicles (exception: rental, taxi businesses) [T1]
- **Personal use** -- not for business purposes [T1]
- **Exempt operations** -- no input credit on costs for exempt supplies [T1]
- **Non-taxable foreign operations** -- input ITBMS on costs attributable to foreign-source (non-ITBMS) operations is NOT recoverable [T2]

### Partial Exemption [T2]
- Direct attribution first
- Common costs: `Recovery % = (Taxable Revenue / Total Revenue) * 100`
- Flag for reviewer: the territorial system adds complexity -- foreign-source revenue is neither taxable nor exempt for ITBMS purposes

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory ITBMS registration | Annual taxable operations exceeding USD 36,000 [T1] |
| Voluntary registration | Below USD 36,000 (may register voluntarily) |
| Note: Panama uses USD as currency | No exchange rate issues for US-denominated transactions |

**Legislation:** Fiscal Code, Article 1057-V(3).

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Fiscal Code, Articles 1057-V(15), 710, 752.

### Filing Deadlines

| Period | Deadline |
|--------|----------|
| Monthly ITBMS return | 15th of the month following the period [T1] |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | USD 100 to USD 5,000 depending on classification [T1] |
| Late payment | Surcharge of 10% on unpaid tax + interest at market rate [T1] |
| Failure to register | Back-assessment + penalties [T1] |
| Fraudulent return | Criminal penalties; fines + imprisonment [T1] |
| Failure to issue fiscal receipt | USD 1,000 to USD 5,000 per occurrence [T1] |

---

## Step 9: Fiscal Receipt / Electronic Invoicing [T1]

**Legislation:** Fiscal Code; DGI electronic invoicing regulations.

Panama has implemented electronic invoicing (Factura Electronica):

1. Equipment Fiscal (EF) machines were previously required -- now transitioning to electronic system
2. All invoices must include: RUC, date, description, net amount, ITBMS, total
3. Invoices must be authorized by DGI (pre-numbered or electronic)
4. Input ITBMS is only deductible with valid fiscal receipts

---

## Step 10: Classification Matrix [T1]

### Domestic Purchases

| Category | ITBMS Rate | Input Credit | Notes |
|----------|-----------|--------------|-------|
| Office supplies | 7% | Yes | |
| Commercial rent | 7% | Yes | |
| Residential rent | Exempt | No | |
| Electricity (commercial) | 7% | Yes | |
| Telephone/internet | 7% | Yes | |
| Motor car | 7% | BLOCKED | |
| Entertainment | 7% | BLOCKED | |
| Legal services | Exempt | No | Regulated profession |
| Accounting/CPA services | Exempt | No | Regulated profession |
| Architecture/engineering | Exempt | No | Regulated profession |
| Insurance (general) | 7% | Yes | |
| Insurance (life) | Exempt | No | |
| Alcoholic beverages | 10% | BLOCKED (entertainment) | |
| Hotel accommodation | 10% | Yes (if business travel) | |
| Basic food items | Exempt | No | |
| Medicines | Exempt | No | |

### Sales

| Category | ITBMS | Return Line |
|----------|-------|-------------|
| Domestic sale (standard) | 7% | Line 1, Line 2 |
| Alcoholic beverage sales | 10% | Line 3, Line 4 |
| Hotel accommodation sales | 10% | Line 3, Line 4 |
| Tobacco sales | 15% | Line 5, Line 6 |
| Export of goods | 0% | Line 7 |
| Exempt supply | Exempt | Line 8 |

---

## Step 11: Special Economic Zones [T2]

### Colon Free Zone (Zona Libre de Colon) [T2]

**Legislation:** Decreto Ley 18 de 1948 (as amended).

- Largest free trade zone in the Western Hemisphere
- Goods entering CFZ for re-export: exempt from ITBMS and customs duties
- Goods sold from CFZ to Panama domestic market: subject to ITBMS at 7% as imports
- Services within CFZ: generally subject to ITBMS unless specifically exempted
- Flag for reviewer: CFZ transactions require careful documentation

### Special Economic Areas (SEM) [T2]

**Legislation:** Ley 32 de 2011 (SEM Law).

- Manufacturing, logistics, and service companies in SEMs may qualify for ITBMS exemptions
- Exports from SEM: zero-rated
- Purchases for SEM operations: may be exempt
- Flag for reviewer: confirm SEM license and applicable benefits

### Ciudad del Saber (City of Knowledge) [T2]
- Technology and innovation hub with special tax benefits
- ITBMS treatment depends on specific agreement with government
- Flag for reviewer

---

## PROHIBITIONS [T1]

- NEVER let AI guess ITBMS classification -- it is deterministic from facts
- NEVER allow input credit on blocked categories (entertainment, motor vehicles, personal use)
- NEVER apply ITBMS to exempt regulated professional services (legal, medical, engineering, architecture, CPA)
- NEVER allow input credit on costs attributable to non-taxable foreign operations without reviewer confirmation
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse zero-rated exports (input credit allowed) with exempt (NO input credit)
- NEVER ignore the USD 36,000 registration threshold
- NEVER treat Colon Free Zone re-export transactions as domestic sales
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Step 12: Edge Case Registry

### EC1 -- Professional services from non-resident [T2]
**Situation:** Panama company hires a US law firm for legal advice.
**Resolution:** Legal services are exempt from ITBMS (regulated profession). Even when imported, the exemption applies. No self-assessment required. However, flag for reviewer: confirm the service genuinely falls within the regulated profession exemption.

### EC2 -- Hotel accommodation for business travel [T1]
**Situation:** Employee stays at a Panama hotel. Invoice shows 10% ITBMS.
**Resolution:** ITBMS at 10% on accommodation is recoverable input tax if used for business purposes. Report on Line 13.

### EC3 -- Colon Free Zone sale to local market [T2]
**Situation:** CFZ company sells electronics to a Panama City retailer.
**Resolution:** Treated as an import. ITBMS at 7% applies on CIF value + duties. Buyer pays at customs. Flag for reviewer: confirm customs entry documentation.

### EC4 -- Credit notes [T1]
**Situation:** Client issues credit note for returned goods.
**Resolution:** Reduce output ITBMS. Report net figures. Issue proper fiscal credit note.

### EC5 -- Software subscription from US (non-professional service) [T1]
**Situation:** Panama business subscribes to US cloud software (not a regulated profession service).
**Resolution:** Reverse charge at 7%. Self-assess output ITBMS. Claim input if for taxable operations. Net = zero.

### EC6 -- Mixed domestic and foreign operations [T2]
**Situation:** Company provides consulting to both Panama clients (taxable) and Colombia clients (not subject to ITBMS, territorial principle).
**Resolution:** Apportion input ITBMS. Only input ITBMS attributable to taxable domestic operations is recoverable. Flag for reviewer: determine apportionment basis.

### EC7 -- Alcohol sold by restaurant [T1]
**Situation:** Restaurant sells alcoholic beverages.
**Resolution:** Alcoholic beverages are subject to 10% ITBMS (not 7%). Report separately on Line 3/Line 4. Food served by the restaurant is at 7%. Tobacco products are at 15% (Line 5/Line 6).

### EC8 -- Real estate sale (commercial) [T2]
**Situation:** Company sells a commercial property.
**Resolution:** Sale of new commercial real estate may be subject to ITBMS at 7%. Sale of used property may be exempt. Land component is generally exempt. Flag for reviewer: ITBMS on real estate is complex.
**Legislation:** Fiscal Code, Article 1057-V.

### EC9 -- International business headquarters (SEM/MHQ) [T2]
**Situation:** Multinational headquarters in Panama provides management services to affiliates.
**Resolution:** Services to foreign affiliates may fall outside ITBMS scope (territorial principle -- services consumed abroad). Services to domestic affiliates: ITBMS at 7%. Flag for reviewer: confirm place of consumption and SEM/MHQ license.

### EC10 -- Construction on government contract [T2]
**Situation:** Construction company works on government infrastructure project.
**Resolution:** Construction services are taxable at 7%. Government entities may have specific ITBMS withholding obligations. Flag for reviewer: confirm government procurement ITBMS treatment.

---

## Step 12a: Sector-Specific Guidance [T2]

### Banking and Financial Services (Detailed)

**Legislation:** Fiscal Code; Banking Law.

Panama is a major international financial center:
- **Interest on loans**: exempt [T1]
- **Banking commissions and fees**: taxable at 7% [T1]
- **Trust administration fees**: taxable at 7% [T1]
- **Insurance premiums (life)**: exempt [T1]
- **Insurance premiums (general)**: taxable at 7% [T1]
- **Securities brokerage**: taxable at 7% [T1]
- **International banking operations**: services consumed outside Panama are NOT subject to ITBMS (territorial principle) [T2]
- Flag for reviewer: distinguish domestic vs. international financial services

### Maritime Sector

- **Ship registration fees**: exempt from ITBMS (government fee) [T1]
- **Maritime services (domestic)**: taxable at 7% [T1]
- **Canal-related services**: specific regime [T3]
- **International shipping services**: NOT subject to ITBMS (consumed outside Panama) [T1]
- **Ship repair and maintenance**: taxable at 7% if performed in Panama [T1]

### Tourism and Hospitality

- **Hotel accommodation**: taxable at 10% (special rate) [T1]
- **Restaurant services**: taxable at 7% [T1]
- **Tour operator services**: taxable at 7% [T1]
- **Tourism incentive law**: approved tourism projects may have ITBMS exemptions on construction [T2]
- Flag for reviewer: confirm tourism incentive applicability

### Construction and Real Estate

- **Construction services**: taxable at 7% [T1]
- **Sale of new commercial real estate**: taxable at 7% on improvements [T2]
- **Sale of residential real estate**: may be exempt (certain conditions) [T2]
- **Land (bare)**: exempt [T1]
- **Commercial rental**: taxable at 7% [T1]
- **Residential rental**: exempt [T1]

### Professional Services (Regulated Professions) -- CRITICAL [T1]

**This is unique to Panama.** The following regulated professional services are EXEMPT from ITBMS:

| Profession | Exempt? |
|-----------|---------|
| Lawyers (Abogados) | YES -- exempt [T1] |
| Doctors (Medicos) | YES -- exempt [T1] |
| Engineers (Ingenieros) | YES -- exempt [T1] |
| Architects (Arquitectos) | YES -- exempt [T1] |
| Certified Public Accountants (CPA) | YES -- exempt [T1] |
| Dentists (Odontologos) | YES -- exempt [T1] |
| Psychologists | YES -- exempt [T1] |
| Veterinarians | YES -- exempt [T1] |

**Non-regulated consulting services** (e.g., management consulting, IT consulting, marketing): taxable at 7% [T1].

This distinction is critical for input ITBMS recovery: costs attributable to providing exempt professional services do NOT generate recoverable input ITBMS.

---

## Step 12b: Books and Records [T1]

**Legislation:** Fiscal Code; Codigo de Comercio.

All ITBMS-registered persons must maintain:

- **Sales records**: invoices/receipts, fiscal machine records, export documentation
- **Purchase records**: purchase invoices with ITBMS breakdowns
- **Import records**: customs entries showing ITBMS paid
- **ITBMS account**: summary ledger of output/input ITBMS
- **Bank statements**: reconciled to business records
- Records must be retained for a minimum of **5 years**
- Records available for DGI inspection at the fiscal domicile

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

## Step 14: Test Suite

### Test 1 -- Standard local purchase, 7%
**Input:** Panama supplier, office equipment, gross USD 1,070, ITBMS USD 70, net USD 1,000. Valid fiscal receipt.
**Expected output:** Line 11 = USD 70 input ITBMS. Full recovery.

### Test 2 -- Export, zero-rated
**Input:** Registered exporter ships goods to Colombia, net USD 50,000.
**Expected output:** Line 7 = USD 50,000. No output ITBMS. Input ITBMS fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase of sedan USD 30,000, ITBMS USD 2,100.
**Expected output:** ITBMS USD 2,100 BLOCKED. No input credit.

### Test 4 -- Legal services (exempt regulated profession)
**Input:** Panama law firm provides legal advice USD 5,000. No ITBMS charged.
**Expected output:** No ITBMS. Exempt regulated profession. No input/output entries.

### Test 5 -- Hotel accommodation sale at 10%
**Input:** Hotel charges guest USD 2,200 (USD 2,000 + USD 200 ITBMS at 10%).
**Expected output:** Line 3 = USD 2,000. Line 4 = USD 200.

### Test 6 -- Imported services (non-professional), reverse charge
**Input:** US marketing firm provides services USD 10,000. No ITBMS.
**Expected output:** Self-assess output ITBMS = USD 700 (7%). Input ITBMS = USD 700. Net = zero.

### Test 7 -- Alcohol sales at 10%
**Input:** Liquor store sells beverages USD 5,500 (USD 5,000 + USD 500 ITBMS at 10%).
**Expected output:** Line 3 = USD 5,000. Line 4 = USD 500.

### Test 8 -- Entertainment, blocked
**Input:** Client dinner USD 535 inclusive of ITBMS USD 35.
**Expected output:** ITBMS USD 35 BLOCKED. No input credit.

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
