---
name: mx-vat-return
description: >
  Mexican VAT return (IVA -- Impuesto al Valor Agregado, Declaracion Mensual) for self-employed individuals. Covers the standard 16% rate, zero rate (tasa 0%), exempt activities, monthly filing via SAT portal, DIOT informative declaration, CFDI electronic invoicing, and IVA acreditable computation. Primary source: Ley del IVA (LIVA).
version: 1.0
jurisdiction: MX
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
validated: April 2026
---

# Mexico VAT Return (IVA -- Declaracion Mensual) v1.0

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Complete

This is a Tier 2 content skill for preparing the Mexican IVA monthly return for self-employed individuals (personas fisicas con actividad empresarial or regimen de servicios profesionales). Mexico has a single standard rate (16%) plus a zero rate for essential goods and exports, with monthly filing.

---

## Section 1 -- Scope statement

**In scope:**

- Monthly IVA return (Declaracion Mensual via SAT portal)
- Standard 16% IVA rate
- Zero rate (tasa 0%) for food, medicine, exports, agricultural inputs
- Exempt activities
- IVA trasladado (output IVA) and IVA acreditable (input IVA)
- IVA retenido (IVA withheld by clients)
- DIOT (Declaracion Informativa de Operaciones con Terceros)
- CFDI (Comprobante Fiscal Digital por Internet) electronic invoicing

**Out of scope (refused):**

- Resico (Regimen Simplificado de Confianza) -- simplified regime with different IVA filing
- Corporate IVA returns
- IVA on imports (customs)
- IEPS (Impuesto Especial sobre Produccion y Servicios)
- ISAN (automotive tax)
- Transfer pricing
- Tax treaty applications

---

## Section 2 -- Filing requirements

### Who must file

Every persona fisica conducting taxable activities must file monthly IVA returns. This includes:
- Actividad empresarial (business activity)
- Servicios profesionales (professional services / freelancing)
- Arrendamiento (rental income)

Registration is via the SAT (Servicio de Administracion Tributaria) portal. **Source:** LIVA, Art. 5-D.

### Filing schedule

| Item | Detail | Source |
|------|--------|--------|
| Filing period | Monthly | LIVA, Art. 5-D |
| Due date | 17th of the following month | CFF Art. 31; LIVA Art. 5-D |
| Filing method | Electronic via SAT declaraciones portal | LIVA; SAT Resolucion Miscelanea |
| CFDI requirement | Mandatory for all taxpayers | CFF Art. 29 |

### DIOT filing

The DIOT must be filed monthly (by the 17th of the following month) listing all transactions with third parties above MXN 50,000 in the month. **Source:** LIVA, Art. 32, Frac. VIII.

---

## Section 3 -- Rates and thresholds

### IVA rates

| Rate | Applies to | Source |
|------|-----------|--------|
| 16% (general) | Most goods and services throughout Mexico | LIVA, Art. 1 |
| 0% (tasa cero) | Basic food (unprocessed), prescription medicine, agricultural/livestock/fishing inputs, exports of goods, certain agricultural services | LIVA, Art. 2-A |
| Exempt | Medical services, education, residential rent, sale of residential property, author's rights, insurance on agricultural/fishing property | LIVA, Art. 15 |

**Note:** The former 11% border zone rate was eliminated. The standard rate of 16% applies nationwide since 2014.

### Key distinction: zero rate vs. exempt

| Feature | Zero rate (tasa 0%) | Exempt |
|---------|---------------------|--------|
| IVA charged to customer | 0% | No IVA |
| Input IVA (IVA acreditable) | Fully recoverable | NOT recoverable |
| Net effect for seller | Refund position likely | IVA on inputs is a cost |

---

## Section 4 -- Computation rules (Step format)

### Step 1: Classify all activities

For each sale/service:
1. **Gravado 16%:** Default rate for most goods and services.
2. **Tasa 0%:** Check LIVA Art. 2-A list (food, medicine, exports, agricultural inputs).
3. **Exento:** Check LIVA Art. 15 list (medical, education, residential rent).

### Step 2: Compute IVA trasladado (output IVA)

- Sum of IVA charged on all 16% sales: sales amount x 16%.
- Zero-rate sales contribute $0 to IVA trasladado but remain reportable.
- Exempt sales: no IVA charged.

**Cash basis rule:** Mexico uses a cash-flow basis for IVA. IVA trasladado is recognized when payment is RECEIVED, not when the invoice is issued. **Source:** LIVA, Art. 1-B.

### Step 3: Compute IVA acreditable (deductible input IVA)

For each purchase with IVA:
1. Verify the CFDI (electronic invoice) is valid and properly issued.
2. Verify the purchase is strictly indispensable for the taxable activity.
3. IVA must have been effectively paid (cash basis).
4. Sum the IVA on valid, paid purchase CFDIs.

**Cash basis rule:** IVA acreditable is recognized when payment is MADE, not when the invoice is received.

### Step 4: Apply proportional rule if mixed activities

If the taxpayer has both taxable/zero-rate AND exempt activities:

IVA acreditable proportion = (taxable + zero-rate sales) / (taxable + zero-rate + exempt sales)

Apply this proportion to total input IVA. Only the proportional amount is deductible.

**Source:** LIVA, Art. 5, Frac. V.

### Step 5: Compute net IVA

IVA trasladado - IVA acreditable = net IVA.

- If positive: tax to pay.
- If negative: saldo a favor. Can be offset against future IVA or requested as refund.

### Step 6: Apply IVA retenido (withheld IVA)

Certain payers are required to withhold IVA from payments to service providers:

| Scenario | Withholding rate | Source |
|----------|-----------------|--------|
| Legal entities paying personas fisicas for services | 2/3 of IVA (10.6667% of the fee) | LIVA, Art. 1-A, Frac. II |
| Outsourcing/subcontracting | 6% of service value | LIVA, Art. 1-A, Frac. IV |

Net IVA due = IVA trasladado - IVA acreditable - IVA retenido (credited).

### Step 7: File DIOT

List all transactions with each third party exceeding MXN 50,000. Include:
- RFC (tax ID) of each counterpart
- Total value of transactions
- IVA charged/paid
- Whether taxable, zero-rate, or exempt

### Step 8: File and pay

- Submit declaration via SAT portal (declaraciones.sat.gob.mx).
- Pay via bank transfer or at authorized bank branches.

---

## Section 5 -- Edge cases and special rules

### E-1: Cash-flow basis (flujo de efectivo)

Mexico's IVA operates on a cash-flow basis, NOT an accrual basis. IVA is recognized when cash is received (output) or paid (input). This means:
- An invoice issued in March but paid in April: IVA trasladado recognized in April.
- A purchase invoice received in March but paid in May: IVA acreditable recognized in May.

This is the single most important rule in Mexican IVA and the most common source of errors.

### E-2: CFDI requirements

All transactions must be supported by a valid CFDI (Comprobante Fiscal Digital por Internet) stamped by an authorized PAC (Proveedor Autorizado de Certificacion). Input IVA without a valid CFDI is NOT deductible. **Source:** CFF Art. 29.

### E-3: Saldo a favor and refund

Saldos a favor can be:
- Offset against future monthly IVA liabilities (compensacion universal was eliminated in 2019; now only IVA saldo a favor can offset IVA).
- Requested as refund via SAT portal (Formato Electronico de Devoluciones). Refunds are subject to SAT review and may take 40 business days.

### E-4: IVA on professional services (honorarios)

Personas fisicas providing professional services (lawyers, accountants, consultants, developers) charge 16% IVA. When the client is a persona moral (legal entity), the client withholds 2/3 of the IVA (effectively 10.6667% of the pre-tax fee). The professional credits this withholding against their IVA liability.

### E-5: Border zone stimulus (Decreto)

Certain businesses in the northern and southern border zones may apply a reduced IVA effective rate via a fiscal stimulus decree. This stimulus (which reduces the effective rate) may be available for border-zone businesses. Flag for reviewer if the taxpayer operates in a border municipality.

### E-6: Invoicing to foreigners

Services provided to foreign clients consumed abroad are zero-rated (export of services). Requirements: payment must be received from abroad, and the service must be consumed entirely outside Mexico. **Source:** LIVA, Art. 29, Frac. IV.

---

## Section 6 -- Test suite

### Test 1: Standard monthly return (cash basis)

- **Input:** Sales invoiced: MXN 500,000 (16% IVA). Payments received: MXN 400,000. Purchases paid: MXN 200,000 (16% IVA).
- **Expected:** IVA trasladado: MXN 400,000 x 16% = MXN 64,000 (cash received only). IVA acreditable: MXN 200,000 x 16% = MXN 32,000. Net: MXN 32,000.

### Test 2: Professional with IVA retention

- **Input:** Professional services to legal entity: MXN 100,000 + IVA MXN 16,000. Client withholds 2/3 of IVA: MXN 10,667.
- **Expected:** IVA trasladado: MXN 16,000. IVA retenido credit: MXN 10,667. Net before input IVA: MXN 5,333.

### Test 3: Zero-rate exporter

- **Input:** Export sales: MXN 300,000 (tasa 0%). Purchases paid: MXN 150,000 (IVA: MXN 24,000).
- **Expected:** IVA trasladado: MXN 0. IVA acreditable: MXN 24,000. Saldo a favor: MXN 24,000.

### Test 4: Mixed taxable and exempt

- **Input:** Taxable sales: MXN 800,000. Exempt sales: MXN 200,000. Total IVA on purchases: MXN 50,000.
- **Expected:** Proportion: 80%. IVA acreditable: MXN 40,000.

### Test 5: Accrual vs. cash trap

- **Input:** Invoice issued for MXN 100,000 + IVA. Payment NOT received.
- **Expected:** IVA trasladado: MXN 0 (cash basis -- not yet received). Common error: reporting IVA on accrual.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT use accrual basis for IVA. Mexico uses cash-flow basis.
- **P-2:** Do NOT claim IVA acreditable without a valid stamped CFDI.
- **P-3:** Do NOT claim IVA acreditable on exempt-activity purchases.
- **P-4:** Do NOT ignore the DIOT filing obligation. It is separate from the IVA return but equally mandatory.
- **P-5:** Do NOT confuse zero rate with exempt. Zero rate allows input IVA recovery; exempt does not.
- **P-6:** Do NOT offset IVA saldo a favor against other taxes (compensacion universal was eliminated in 2019).

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Cash-flow basis applied (IVA recognized when paid/received, NOT invoiced)
- [ ] All transactions supported by valid stamped CFDIs
- [ ] Correct rate applied (16%, 0%, exempt)
- [ ] IVA retenido correctly credited
- [ ] Proportional rule applied if mixed taxable/exempt activities
- [ ] DIOT prepared for all third-party transactions > MXN 50,000
- [ ] Saldo a favor correctly computed and NOT offset against non-IVA taxes
- [ ] Filing due date: 17th of following month

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
