---
name: ar-vat-return
description: >
  Argentine VAT return (IVA -- Impuesto al Valor Agregado) for self-employed individuals under the regimen general. Covers the standard 21% rate, reduced 10.5%, increased 27%, monthly filing via AFIP SIAP/web, debito/credito fiscal computation, and withholding/perception regimes. Primary source: Ley 23.349 (Ley de IVA) and its regulatory decree (Decreto 692/98).
version: 1.0
jurisdiction: AR
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
validated: April 2026
---

# Argentina VAT Return (IVA) v1.0

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Complete

This is a Tier 2 content skill for preparing the Argentine IVA (Impuesto al Valor Agregado) monthly return for self-employed individuals (autonomos/monotributistas graduating to regimen general). Argentina has a three-rate VAT system with extensive withholding and perception regimes.

---

## Section 1 -- Scope statement

**In scope:**

- Monthly IVA return (DDJJ IVA -- F.2002)
- Responsable Inscripto (registered taxpayer under the general regime)
- Three VAT rates: 21%, 10.5%, 27%
- Debito fiscal (output VAT) and credito fiscal (input VAT)
- Withholdings (retenciones) and perceptions (percepciones) suffered
- Filing via AFIP web services or SIAP
- Electronic invoicing (factura electronica) requirements

**Out of scope (refused):**

- Monotributo (simplified small taxpayer regime)
- Corporate IVA returns
- IVA on imports (customs VAT) beyond basic classification
- Transfer pricing implications
- Percepciones as agent (acting as withholding/perception agent)
- Provincial gross income tax (Ingresos Brutos)

---

## Section 2 -- Filing requirements

### Who must file

Every Responsable Inscripto must file a monthly IVA return, even if there is no activity (zero return). Registration is mandatory once annual revenue exceeds the Monotributo thresholds. **Source:** Ley 23.349, Art. 4.

### Filing schedule

| Item | Detail | Source |
|------|--------|--------|
| Filing period | Monthly | Ley 23.349, Art. 27 |
| Due date | Determined by CUIT ending digit (AFIP calendar, typically between the 18th and 22nd of the following month) | RG AFIP 3382/2012 |
| Filing method | Electronic via AFIP web (F.2002 online) | RG AFIP 3711/2015 |
| Electronic invoicing | Mandatory for all Responsables Inscriptos | RG AFIP 4291/2018 |

---

## Section 3 -- Rates and thresholds

### VAT rates

| Rate | Applies to | Source |
|------|-----------|--------|
| 21% (standard) | Most goods and services | Ley 23.349, Art. 28 |
| 10.5% (reduced) | Capital goods, certain food products, medical services, newspapers, residential construction, certain transport | Ley 23.349, Art. 28, inc. a) |
| 27% (increased) | Telecommunications, gas, electricity, water for non-residential use | Ley 23.349, Art. 28, inc. b) |
| 0% (exempt) | Specified exempt supplies (education, health under certain conditions, financial services, books, bread/milk) | Ley 23.349, Art. 7 |

### Key thresholds

| Item | Amount | Source |
|------|--------|--------|
| Monotributo graduation threshold (services, 2025) | ARS ~11,916,410/year (updated periodically) | Ley 24.977, Annex |
| Credito fiscal carry-forward | Unlimited (no expiry) | Ley 23.349, Art. 24 |

---

## Section 4 -- Computation rules (Step format)

### Step 1: Compute debito fiscal (output VAT)

For each sale/service during the month:
1. Classify the transaction: standard (21%), reduced (10.5%), increased (27%), or exempt.
2. Verify the electronic invoice (factura electronica) was issued via AFIP.
3. Debito fiscal = sum of IVA charged on all invoices issued.

### Step 2: Compute credito fiscal (input VAT)

For each purchase/expense during the month:
1. Verify the supplier's invoice is a valid factura electronica.
2. Classify the IVA rate charged.
3. Verify the expense is related to taxable activity (credito fiscal is only recoverable on purchases related to taxable sales).
4. Credito fiscal = sum of IVA on valid purchase invoices.

### Step 3: Apply pro-rata rule if mixed activities

If the taxpayer makes both taxable and exempt sales:
- Credito fiscal must be apportioned between taxable and exempt activities.
- Only the portion attributable to taxable activities is recoverable.
- Pro-rata = taxable sales / (taxable sales + exempt sales).
- Recoverable credito fiscal = total credito fiscal x pro-rata.

**Source:** Ley 23.349, Art. 13.

### Step 4: Compute net IVA position

Debito fiscal - credito fiscal = net IVA.

- If positive: tax to pay.
- If negative: carry forward as saldo a favor tecnico (technical credit balance).

### Step 5: Apply withholdings and perceptions suffered

Deduct IVA withholdings (retenciones) and perceptions (percepciones) suffered during the month from the net IVA:

- Withholdings: amounts withheld by customers who are designated withholding agents.
- Perceptions: additional IVA charged by suppliers who are designated perception agents.

Net amount due = net IVA - withholdings - perceptions.

If negative: the balance becomes saldo de libre disponibilidad (freely available balance) that can be applied to other AFIP obligations.

### Step 6: File and pay

- File F.2002 via AFIP web portal.
- Pay via VEP (Volante Electronico de Pago) through authorized banks.

---

## Section 5 -- Edge cases and special rules

### E-1: Factura electronica requirement

All invoices (ventas and compras) must be electronic invoices authorized by AFIP. Paper invoices are no longer valid for credito fiscal. Types:
- Factura A: between Responsables Inscriptos
- Factura B: from Responsable Inscripto to final consumer or exempt subject
- Factura C: from Monotributista

Only Factura A and certain import documents generate credito fiscal.

### E-2: Saldo a favor tecnico vs. libre disponibilidad

- **Saldo a favor tecnico:** arises when credito fiscal exceeds debito fiscal. Can only be carried forward against future debito fiscal.
- **Saldo de libre disponibilidad:** arises from excess withholdings/perceptions. Can be used against any AFIP tax obligation (IVA, Ganancias, etc.) or requested as refund.

### E-3: Non-computable credito fiscal

Credito fiscal is NOT recoverable for:
- Personal consumption items (food, clothing for personal use)
- Automobiles exceeding a threshold value
- Invoices from Monotributistas (Factura C has no IVA discrimination)
- Purchases from non-registered suppliers

### E-4: Services exported

Services exported (performed for foreign clients, consumed abroad) are treated as zero-rated with credit recovery. The taxpayer can claim a refund of the related credito fiscal. **Source:** Ley 23.349, Art. 43.

### E-5: Inflation and currency

All amounts are in Argentine Pesos (ARS). Given high inflation, the real value of credito fiscal carry-forwards erodes over time. There is no inflation adjustment mechanism for VAT credits.

### E-6: Withholding regimes (regimenes de retencion)

Large buyers (designated by AFIP) must withhold a percentage of IVA from payments to suppliers. Common rates: 50% or 100% of the IVA. The withheld amount is credited against the supplier's IVA liability. **Source:** RG AFIP 2854/2010.

---

## Section 6 -- Test suite

### Test 1: Standard monthly return

- **Input:** Sales at 21%: ARS 1,000,000. Purchases at 21%: ARS 600,000.
- **Expected:** Debito: ARS 210,000. Credito: ARS 126,000. Net IVA: ARS 84,000.

### Test 2: Mixed rates

- **Input:** Sales at 21%: ARS 500,000. Sales at 10.5%: ARS 200,000. Purchases at 21%: ARS 400,000.
- **Expected:** Debito: (500,000 x 21%) + (200,000 x 10.5%) = 105,000 + 21,000 = 126,000. Credito: 84,000. Net: ARS 42,000.

### Test 3: Withholdings reduce payment

- **Input:** Net IVA: ARS 84,000. Withholdings suffered: ARS 30,000. Perceptions suffered: ARS 10,000.
- **Expected:** Amount due: 84,000 - 30,000 - 10,000 = ARS 44,000.

### Test 4: Saldo a favor

- **Input:** Debito: ARS 50,000. Credito: ARS 80,000.
- **Expected:** Saldo a favor tecnico: ARS 30,000. Carry forward to next month. No payment due.

### Test 5: Pro-rata for mixed activities

- **Input:** Taxable sales: ARS 800,000. Exempt sales: ARS 200,000. Total credito fiscal: ARS 100,000.
- **Expected:** Pro-rata: 800,000 / 1,000,000 = 80%. Recoverable credito: ARS 80,000.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT claim credito fiscal from Factura C (Monotributista invoices). They do not discriminate IVA.
- **P-2:** Do NOT claim credito fiscal on personal consumption items.
- **P-3:** Do NOT ignore the pro-rata rule when both taxable and exempt sales exist.
- **P-4:** Do NOT confuse saldo a favor tecnico with saldo de libre disponibilidad. They have different uses.
- **P-5:** Do NOT file without verifying all invoices are properly authorized electronic invoices.
- **P-6:** Do NOT advise on Monotributo eligibility or transition. That is a separate analysis.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] All sales invoices are authorized electronic invoices (factura electronica)
- [ ] Correct VAT rate applied per transaction (21%, 10.5%, 27%, exempt)
- [ ] Credito fiscal only claimed from valid Factura A or import documents
- [ ] Pro-rata applied if mixed taxable/exempt activities
- [ ] Withholdings and perceptions correctly deducted
- [ ] Saldo a favor correctly classified (tecnico vs. libre disponibilidad)
- [ ] Filing due date verified against AFIP calendar for CUIT ending digit
- [ ] Zero return filed if no activity

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
