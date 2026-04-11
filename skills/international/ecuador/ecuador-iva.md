---
name: ecuador-iva
description: Use this skill whenever asked to prepare, review, or create an Ecuador IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "Ecuador VAT", or any request involving Ecuador value added tax filing. ALWAYS read this skill before touching any Ecuador IVA-related work.
---

# Ecuador IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Ecuador |
| Jurisdiction Code | EC |
| Primary Legislation | Ley de Regimen Tributario Interno (LRTI), as amended |
| Supporting Legislation | Reglamento para la Aplicacion de la LRTI; Codigo Tributario; Ley Organica de Simplicidad y Progresividad Tributaria |
| Tax Authority | Servicio de Rentas Internas (SRI) |
| Filing Portal | https://www.sri.gob.ec (SRI en Linea) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return form, input recovery, calculations. Tier 2: partial exemption, ZEDE/free zone, oil sector, rate changes. Tier 3: complex structures, rulings, transfer pricing. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and RUC (Registro Unico de Contribuyentes)** [T1] -- 13-digit RUC
2. **Tax regime** [T1] -- Regimen General, RIMPE (Regimen Simplificado para Emprendedores y Negocios Populares), or Sociedad
3. **Filing period** [T1] -- monthly (standard) or semi-annual (RIMPE)
4. **Industry/sector** [T2] -- oil sector, agriculture, ZEDE, tourism
5. **Does the business make exempt (tarifa 0%) supplies?** [T2]
6. **Does the business import goods?** [T1]
7. **Is the business in a ZEDE or special economic zone?** [T2]
8. **Credit balance brought forward** [T1]

**If items 1-3 are unknown, STOP.**

---

## Step 1: IVA Rate Structure [T1]

**Legislation:** LRTI, Articles 55, 56, 65.

### IMPORTANT: Rate Increase Effective April 1, 2024 [T1]

Ecuador increased the standard IVA rate from 12% to 15% effective April 1, 2024, under the Organic Law to Confront the Internal Armed Conflict and the Social and Economic Crisis (enacted March 12, 2024) and Executive Decree No. 198 (March 15, 2024). The 15% rate has been confirmed for 2025 (Executive Decree 470, December 10, 2024) and for 2026 (SRI circular, December 26, 2025). The LRTI establishes a range of 13%-15% for the IVA rate, modifiable by presidential decree. The 151 products in the canasta basica remain at tarifa 0%. Construction materials were subject to a transitional 5% reduced rate.

### Standard Rate

| Rate | Application |
|------|-------------|
| 15% | Standard rate on all taxable transfers of goods and services (from April 1, 2024; confirmed through 2026) [T1] |
| 12% | Previous standard rate (applicable to periods before April 1, 2024) [T1] |

### Zero-Rated Goods (Tarifa 0%) [T1]

**Legislation:** LRTI, Article 55.

- Unprocessed agricultural products: fresh fruits, vegetables, grains, meats, fish, eggs, milk
- Basic food basket items (canasta basica)
- Medicines and pharmaceutical products (registered with ARCSA)
- Agricultural inputs (fertilizers, seeds, insecticides)
- Animal feed
- Tractors and agricultural machinery
- Books, newspapers, educational materials
- Paper and materials for printing
- Infant formula and baby food
- Feminine hygiene products
- Seeds and plants for cultivation

### Zero-Rated Services (Tarifa 0%) [T1]

**Legislation:** LRTI, Article 56.

- Health/medical services
- Educational services (authorized institutions)
- Public transportation (urban and interprovincial)
- Residential rental
- Financial services (interest, commissions on credit operations)
- Insurance premiums (life, health, personal accident)
- Electricity and water (domestic, up to thresholds)
- Funerals
- Internet services (residential, up to threshold)
- Tourism packages for incoming foreign tourists [T2]

**Note:** Ecuador uses "tarifa 0%" (zero rate) for what many countries call "exempt." The key distinction is that some tarifa 0% goods/services DO allow input credit recovery (e.g., exports), while others do NOT (e.g., medical services). This depends on the specific article. [T2]

### Exports (0% -- Full Input Credit) [T1]
- Export of goods: zero-rated with FULL input credit recovery
- Export of services: certain services to non-residents [T2]

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (IVA cobrado -- output) or Purchase (IVA pagado -- input)
- Salaries, IESS (social security), IR (income tax), loans, dividends = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (Ecuador)
- CAN (Comunidad Andina): Colombia, Peru, Bolivia
- International

### 2c. Determine IVA Rate [T1]
- 0% (tarifa 0%), 15% (standard, post-April 2024), or 12% (pre-April 2024)

### 2d. Factor Proporcionalidad (Proportionality Factor) [T2]
- If the business makes both tarifa 15% and tarifa 0% supplies, input IVA recovery must be apportioned
- The Factor de Proporcionalidad determines the recoverable percentage
- `Factor = (Sales at 15% + Exports) / Total Sales`

---

## Step 3: IVA Return Form Structure (Formulario 104) [T1]

**Filed monthly via SRI en Linea.**

### Ventas (Output)

| Line | Description |
|------|-------------|
| 401 | Ventas gravadas con tarifa diferente de 0% (excluye activos fijos) |
| 402 | Ventas de activos fijos gravadas |
| 403 | Ventas locales tarifa 0% (que no dan derecho a credito tributario) |
| 404 | Ventas locales tarifa 0% (que dan derecho a credito tributario) |
| 405 | Exportaciones de bienes |
| 406 | Exportaciones de servicios |
| 409 | Total ventas |
| 411 | IVA generado en ventas (output IVA) |

### Compras (Input)

| Line | Description |
|------|-------------|
| 500 | Adquisiciones gravadas (excluye activos fijos) |
| 501 | Adquisiciones de activos fijos gravados |
| 502 | Adquisiciones no gravadas |
| 503 | Importaciones gravadas |
| 504 | Importaciones de activos fijos gravados |
| 505 | Importaciones no gravadas |
| 510 | IVA en adquisiciones |
| 511 | IVA en importaciones |

### Liquidacion

| Line | Description |
|------|-------------|
| 601 | IVA causado (output) |
| 602 | Credito tributario aplicable (input credit) |
| 605 | Factor de proporcionalidad |
| 699 | Impuesto a pagar / saldo a favor |
| 721 | Retenciones de IVA recibidas |
| 902 | Total a pagar |

---

## Step 4: IVA Withholding (Retencion) [T1]

**Legislation:** LRTI, Article 63; Resoluciones SRI.

Ecuador has an extensive IVA withholding system -- one of the most complex in Latin America.

### Withholding Rates [T1]

| Scenario | Rate |
|----------|------|
| Purchase of goods from general taxpayer | 30% of IVA [T1] |
| Purchase of services from general taxpayer | 70% of IVA [T1] |
| Professional services from individuals | 100% of IVA [T1] |
| Purchases with liquidacion de compra (informal sector) | 100% of IVA [T1] |
| Government entities (all purchases) | 100% of IVA [T1] |
| Exporters (all local purchases) | 100% of IVA [T1] |
| Designated special taxpayers | Varies (30%/70%/100%) [T2] |

### Treatment on the Return [T1]
- Supplier reports full output IVA
- IVA withheld is reported by supplier on Line 721 as credit
- Withholding agent files Formulario 104 Anexo (ATS) monthly with details

### Withholding Certificate [T1]
- A comprobante de retencion must be issued within 5 days of payment
- Must include: RUC of both parties, base amount, IVA withheld, percentage applied

---

## Step 5: Deductibility Check

### Blocked/Non-Creditable Input IVA [T1]

**Legislation:** LRTI, Article 66.

- **Personal use** -- goods/services not for business [T1]
- **Tarifa 0% operations** -- input IVA on costs attributable to tarifa 0% sales (except exports) is NOT recoverable [T1]
- **Purchases without valid comprobante de venta** -- no credit without proper fiscal document [T1]
- **Entertainment** -- generally blocked unless hospitality industry [T1]
- **Motor vehicles** -- passenger vehicles (exception: rental, taxi, transport) [T1]

### Factor de Proporcionalidad [T2]

**Legislation:** LRTI, Article 66; Reglamento, Article 193.

If mixed taxable (15%) and non-creditable tarifa 0% operations:
- `Factor = (Ventas gravadas + Exportaciones) / Total Ventas`
- Apply factor to common input IVA
- Directly attributable input IVA: allocate fully
- Flag for reviewer: confirm factor calculation

---

## Step 6: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory IVA registration | All persons/companies registered with RUC making taxable transfers |
| RIMPE (simplified regime) | Gross income up to USD 300,000 (emprendedores) or USD 20,000 (negocios populares) |
| Electronic invoicing | Mandatory for all taxpayers |

---

## Step 7: Filing Deadlines and Penalties [T1]

**Legislation:** LRTI; Codigo Tributario; Ley de Regimen Tributario Interno.

### Filing Deadlines [T1]

Filing date depends on the 9th digit of the RUC:

| 9th Digit of RUC | Due Date (of following month) |
|-------------------|-------------------------------|
| 1 | 10th |
| 2 | 12th |
| 3 | 14th |
| 4 | 16th |
| 5 | 18th |
| 6 | 20th |
| 7 | 22nd |
| 8 | 24th |
| 9 | 26th |
| 0 | 28th |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | 3% per month on tax due (max 100%) [T1] |
| Late payment | Interest at rate set by Central Bank (approximately 0.9-1% per month) [T1] |
| Failure to register | Fines + back-assessment [T1] |
| Failure to issue comprobante | Closure of business (7 days) + fines [T1] |
| Failure to withhold IVA | 100% of amount that should have been withheld + interest + penalties [T1] |
| Fraud | Criminal penalties [T1] |

---

## Step 8: Electronic Invoicing [T1]

**Legislation:** SRI Resoluciones.

Ecuador has mandatory electronic invoicing for all taxpayers:

- All invoices (facturas), credit notes (notas de credito), debit notes (notas de debito), and retention vouchers (comprobantes de retencion) must be issued electronically
- XML format authorized by SRI
- Real-time or batch authorization via SRI web services
- Input IVA ONLY deductible with SRI-authorized electronic documents

---

## Step 9: Classification Matrix [T1]

### Domestic Purchases

| Category | IVA Rate | Input Credit | Notes |
|----------|---------|--------------|-------|
| Office supplies | 15% | Yes (with comprobante) | |
| Commercial rent | 15% | Yes | |
| Residential rent | 0% | No | Tarifa 0% |
| Electricity (commercial) | 15% | Yes | |
| Telephone/internet | 15% | Yes | |
| Motor car | 15% | BLOCKED | |
| Entertainment | 15% | BLOCKED | |
| Professional services | 15% | Yes | Withhold 70% or 100% IVA |
| Insurance (general) | 15% | Yes | |
| Insurance (life) | 0% | No | Tarifa 0% |
| Basic food | 0% | No | |
| Medicines | 0% | No | |
| Fuel | 15% | Yes (if business) | |

### Sales

| Category | IVA | Return Line |
|----------|-----|-------------|
| Domestic taxable sale | 15% | Line 401, Line 411 |
| Export of goods | 0% (credit allowed) | Line 405 |
| Export of services | 0% (credit allowed) | Line 406 |
| Tarifa 0% (no credit) | 0% | Line 403 |
| Tarifa 0% (credit allowed) | 0% | Line 404 |

---

## Step 10: ATS (Anexo Transaccional Simplificado) [T1]

**Legislation:** SRI Resoluciones.

In addition to Formulario 104, all taxpayers must file the ATS monthly:

- Details all purchase and sale transactions with RUC, amounts, IVA, withholdings
- Cross-matched by SRI electronically
- Discrepancies trigger automatic notifications and potential audits
- Filing deadline: same as IVA return

---

## Step 10a: Sector-Specific Rules [T2]

### Oil and Mining

- Oil sector: IVA at standard rate on domestic transactions [T1]
- Exports of crude oil: zero-rated [T1]
- Service contracts with the state (EPPETROECUADOR): complex IVA treatment [T3]
- Mining exports: zero-rated [T1]
- Flag for reviewer: oil/mining sector has specialized regulations. Escalate to specialist.

### Agriculture

- Unprocessed agricultural products: tarifa 0% [T1]
- Processed food: standard rate [T1]
- Agricultural inputs (fertilizers, seeds): tarifa 0% [T1]
- Flowers for export: zero-rated with full input credit (major export sector) [T1]
- Banana and shrimp exports: zero-rated [T1]

### Tourism

- Hotel accommodation: standard rate [T1]
- Tourism packages for incoming foreign tourists: tarifa 0% [T2]
- Restaurant services: standard rate [T1]
- Artisan services (registered artisans): tarifa 0% [T1]
- Flag for reviewer: artisan registration must be valid with JNDA

### Financial Services

- Interest on loans: tarifa 0% [T1]
- Banking fees and commissions: standard rate [T1]
- Insurance premiums (life/health): tarifa 0% [T1]
- Insurance premiums (general): standard rate [T1]

### Construction and Real Estate

- Construction services: standard rate [T1]
- First transfer of new real estate: standard rate [T1]
- Subsequent transfers: exempt [T2]
- Residential rental: tarifa 0% [T1]
- Commercial rental: standard rate [T1]

### Artisan Sector [T1]

**Legislation:** LRTI, Article 56.

- Services provided by qualified artisans (registered with JNDA -- Junta Nacional de Defensa del Artesano): tarifa 0%
- Goods produced by qualified artisans: tarifa 0%
- Artisan registration must be current and valid
- If artisan loses qualification, standard rate applies immediately

---

## Step 10b: Libro de Compras y Ventas [T1]

All IVA taxpayers must maintain purchase and sales records:

- **Purchases**: all transactions with comprobante details, RUC of supplier, date, base, IVA, withholding applied
- **Sales**: all transactions with comprobante details, RUC of customer (B2B), date, base, IVA, withholding received
- Electronic submission via ATS format
- Summary totals reconcile to Formulario 104
- Retention: minimum 7 years

---

## PROHIBITIONS [T1]

- NEVER let AI guess IVA classification
- NEVER allow input credit without valid SRI-authorized electronic document
- NEVER allow input credit on tarifa 0% costs (except for exporters)
- NEVER allow input credit on blocked categories (entertainment, motor vehicles, personal)
- NEVER apply pre-April 2024 rate (12%) to post-April 2024 periods (15% confirmed through 2026)
- NEVER ignore the Factor de Proporcionalidad for mixed operations
- NEVER fail to apply IVA withholding rules when the client is a withholding agent
- NEVER compute any number -- all arithmetic is handled by the deterministic engine

---

## Step 11: Edge Case Registry

### EC1 -- Rate change transition (12% to 15%) [T1]
**Situation:** Invoice issued straddling the April 1, 2024 rate change.
**Resolution:** Rate applicable is based on the date of the taxable event (transfer of goods or provision of service), not invoice date. Pre-April 1, 2024 events = 12%. Post-April 1, 2024 = 15%. The 15% rate is confirmed through 2026. This transition is now historical; all current-period transactions use 15%.

### EC2 -- Exporter IVA recovery [T1]
**Situation:** Exporter has no domestic taxable sales. All exports are tarifa 0%.
**Resolution:** Exporters are entitled to FULL input IVA recovery on all costs attributable to exports. File for IVA refund (devolucion de IVA) via SRI.
**Legislation:** LRTI, Article 72.

### EC3 -- Purchase with liquidacion de compra [T1]
**Situation:** Company purchases goods from informal sector (no RUC).
**Resolution:** Issue liquidacion de compra (purchase settlement voucher). Withhold 100% IVA. The IVA withheld is the supplier's IVA; buyer can claim input credit.

### EC4 -- Credit notes [T1]
**Situation:** Client issues electronic credit note.
**Resolution:** Reduce output IVA. Must be SRI-authorized electronic document. Report net.

### EC5 -- Services from CAN (Comunidad Andina) country [T2]
**Situation:** Ecuador company receives services from Colombian firm.
**Resolution:** CAN Decision 599 may affect withholding tax treatment but does not change IVA treatment. Self-assess IVA at 15%. Flag for reviewer: confirm CAN implications.

### EC6 -- Oil sector transactions [T3]
**Situation:** Oil company with service contracts.
**Resolution:** Oil sector has complex IVA treatments under specific regulations. Escalate to specialist. Do not classify.

### EC7 -- RIMPE taxpayer [T1]
**Situation:** RIMPE Negocio Popular taxpayer (income under USD 20,000).
**Resolution:** RIMPE Negocios Populares pay a fixed annual quota. They do NOT charge IVA separately. Buyers cannot claim input IVA credit on purchases from these taxpayers.

### EC8 -- IVA withholding by special taxpayer [T1]
**Situation:** Special taxpayer (contribuyente especial) purchases services for USD 5,000 + IVA USD 750.
**Resolution:** Withhold 70% of IVA = USD 525. Issue comprobante de retencion within 5 days. Supplier claims USD 525 on Line 721.

---

## Step 12: Test Suite

### Test 1 -- Standard local purchase, 15%
**Input:** EC supplier, office supplies, gross USD 1,150, IVA USD 150, net USD 1,000. Valid electronic factura.
**Expected output:** Line 510 = USD 150 input IVA. Full recovery (if only taxable operations).

### Test 2 -- Export, zero-rated with credit
**Input:** Exporter ships bananas, net USD 100,000.
**Expected output:** Line 405 = USD 100,000. No output IVA. Input IVA FULLY recoverable. Apply for devolucion.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase sedan USD 25,000, IVA USD 3,750.
**Expected output:** IVA USD 3,750 BLOCKED. No input credit.

### Test 4 -- Imported services, reverse charge
**Input:** US software company, USD 5,000. No IVA.
**Expected output:** Self-assess output IVA = USD 750 (15%). Input = USD 750. Net = zero.

### Test 5 -- Mixed operations (Factor de Proporcionalidad)
**Input:** Sales: USD 80,000 at 15% + USD 20,000 at tarifa 0% (no credit). Common input IVA = USD 3,000.
**Expected output:** Flag T2. Factor = 80,000/100,000 = 80%. Input credit = USD 2,400. Blocked = USD 600.

### Test 6 -- Professional services withholding
**Input:** Individual accountant provides services USD 2,000 + IVA USD 300. Client is general taxpayer.
**Expected output:** Withhold 100% IVA = USD 300. Issue comprobante de retencion. Full USD 300 input credit for buyer.

### Test 7 -- Exempt supply (medical)
**Input:** Clinic earns USD 50,000 from patient fees.
**Expected output:** Line 403 = USD 50,000 (tarifa 0%, no credit). No output IVA. Input IVA NOT recoverable.

### Test 8 -- Entertainment, blocked
**Input:** Client dinner USD 115 inclusive of IVA USD 15.
**Expected output:** IVA USD 15 BLOCKED. No input credit.

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
Action Required: Licensed CPA must confirm before filing. Verify current IVA rate.
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
- Export of services: services consumed outside Ecuador [T2]
- Digital services from abroad: buyer self-assesses IVA [T2]
- Flag for reviewer: place of supply analysis required for cross-border services

### Self-Supply (Autoconsumo) [T1]

**Legislation:** LRTI, Article 53.

- Withdrawal of goods for personal use or employee consumption: taxable event [T1]
- IVA at standard rate on fair market value [T1]
- Report as output IVA [T1]

### Devolucion de IVA (IVA Refund) [T2]

**Legislation:** LRTI, Articles 72-73.

Special IVA refund provisions for:
- Exporters: full refund of input IVA on export-related costs [T1]
- Persons with disabilities: IVA refund on personal consumption [T1]
- Elderly persons (over 65): IVA refund on personal consumption [T1]
- International organizations: IVA refund per agreements [T2]
- Flag for reviewer: refund process requires SRI application and documentation

### ICE (Impuesto a los Consumos Especiales) Interaction [T1]

**Legislation:** LRTI, Articles 75-89.

- ICE is Ecuador's selective consumption tax (alcohol, tobacco, vehicles, soft drinks, etc.)
- ICE is separate from IVA and NOT reported on the IVA return
- IVA is calculated on the price INCLUSIVE of ICE [T1]
- Example: Product USD 100 + ICE USD 30 = USD 130. IVA = USD 130 x 15% = USD 19.50 [T1]

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
