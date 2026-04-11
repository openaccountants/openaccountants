---
name: co-vat-return
description: >
  Colombian VAT return (IVA -- Impuesto sobre las Ventas) for self-employed individuals under the regimen comun/responsable. Covers the standard 19% rate, reduced 5%, excluded goods/services, bimonthly/quarterly filing, electronic invoicing, and Regimen Simple de Tributacion (SIMPLE). Primary source: Estatuto Tributario (E.T.) Libro Tercero; Ley 1819/2016; Ley 2277/2022.
version: 1.0
jurisdiction: CO
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
validated: April 2026
---

# Colombia VAT Return (IVA) v1.0

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Complete

This is a Tier 2 content skill for preparing the Colombian IVA return (Formulario 300) for self-employed individuals classified as responsables de IVA (formerly regimen comun). Colombia uses a two-rate IVA system (19% and 5%) with an extensive list of excluded (excluido) and exempt (exento) goods and services.

---

## Section 1 -- Scope statement

**In scope:**

- Formulario 300 (IVA return -- Declaracion del Impuesto sobre las Ventas)
- Responsables de IVA (general regime taxpayers)
- Two IVA rates: 19% (general) and 5% (reduced)
- Excluded and exempt classifications
- Bimonthly filing (default) and quarterly filing (for small responsables)
- Electronic invoicing (facturacion electronica)
- IVA descontable (deductible input IVA)
- Withholding IVA (retencion en la fuente por IVA)

**Out of scope (refused):**

- Regimen Simple de Tributacion (SIMPLE) -- separate integrated regime
- No responsables de IVA (formerly regimen simplificado) -- not required to file IVA returns
- Corporate IVA
- IVA on imports (customs)
- National consumption tax (Impuesto Nacional al Consumo -- INC)
- Transfer pricing

---

## Section 2 -- Filing requirements

### Who must file

Personas naturales (natural persons) are responsables de IVA if they meet ANY of the following in the prior year:

1. Gross income from taxable activities exceeds 3,500 UVT (approximately COP 165,000,000 for 2025), OR
2. They have more than one commercial establishment, OR
3. They are users of a free trade zone, OR
4. They sell through franchises or concessions.

If none of these apply, the person is a no responsable and does NOT file IVA returns. **Source:** E.T. Art. 437, as modified by Ley 2010/2019.

### Filing frequency

| Taxpayer category | Filing frequency | Periods | Source |
|-------------------|------------------|---------|--------|
| Grandes Contribuyentes | Bimonthly (Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct, Nov-Dec) | 6 returns/year | E.T. Art. 600 |
| Other responsables (default) | Bimonthly | 6 returns/year | E.T. Art. 600 |
| Small responsables (income < 92,000 UVT) | Quarterly (Jan-Mar, Apr-Jun, Jul-Sep, Oct-Dec) | 4 returns/year | E.T. Art. 600, Par. 1 |

### Due dates

Due dates are set by the DIAN calendar, typically based on the last two digits of the NIT. Generally between the 8th and 22nd of the month following the period end.

---

## Section 3 -- Rates and thresholds

### IVA rates

| Rate | Applies to | Source |
|------|-----------|--------|
| 19% (general) | Most goods and services | E.T. Art. 468 |
| 5% (reduced) | Certain foodstuffs (rice, sugar, coffee, chocolate), agricultural inputs, certain insurance, some medical devices | E.T. Art. 468-1 |
| 0% (exempt / exento) | Goods in E.T. Art. 477 (meat, eggs, milk, fish for domestic consumption, certain exports). Seller charges 0% but recovers input IVA. | E.T. Art. 477 |
| Excluded (excluido) | Goods in E.T. Art. 424 and services in E.T. Art. 476 (education, health, public transport, financial services). No IVA charged, no input IVA recovery. | E.T. Art. 424, 476 |

### Key thresholds (2025)

| Item | UVT | Approximate COP | Source |
|------|-----|------------------|--------|
| UVT value (2025) | 1 UVT | COP 47,065 (subject to annual update by DIAN) | E.T. Art. 868 |
| Responsable threshold | 3,500 UVT | ~COP 164,727,500 | E.T. Art. 437, Par. 3 |
| Quarterly filing threshold | < 92,000 UVT | ~COP 4,329,980,000 | E.T. Art. 600 |

---

## Section 4 -- Computation rules (Step format)

### Step 1: Classify all sales and services

For each transaction:
1. **Gravado 19% (taxable at 19%):** Default for most goods and services.
2. **Gravado 5% (taxable at 5%):** Check E.T. Art. 468-1 list.
3. **Exento (exempt, 0%):** Check E.T. Art. 477. Seller recovers input IVA.
4. **Excluido (excluded):** Check E.T. Art. 424/476. No IVA charged, no input IVA recovery.

### Step 2: Compute IVA generado (output IVA)

Sum of IVA charged on all taxable sales:
- Sales at 19% x 19%
- Sales at 5% x 5%
- Exempt sales: no IVA charged, but input IVA is recoverable.

### Step 3: Compute IVA descontable (deductible input IVA)

For each purchase with IVA:
1. Verify the supplier's electronic invoice is valid.
2. Verify the purchase relates to taxable or exempt (not excluded) activities.
3. Sum the IVA on valid purchase invoices.

Input IVA is NOT recoverable if:
- The purchase relates to excluded activities (E.T. Art. 488).
- The invoice is not a valid electronic invoice.
- The purchase is for personal consumption.

### Step 4: Apply proportional rule if mixed activities

If the taxpayer has both taxable/exempt AND excluded activities:
- Only input IVA attributable to taxable/exempt sales is deductible.
- Proportion = (taxable + exempt sales) / (taxable + exempt + excluded sales).

**Source:** E.T. Art. 490.

### Step 5: Compute net IVA

IVA generado - IVA descontable = net IVA.

- If positive: tax to pay.
- If negative: saldo a favor (credit balance). Can be carried forward or requested as refund (for exporters and exempt-goods producers).

### Step 6: Apply withholding IVA credits

Deduct retencion en la fuente por IVA suffered during the period (15% of IVA on purchases above 4 UVT, withheld by designated agents).

Net amount due = net IVA - IVA withholdings suffered.

### Step 7: File via DIAN portal

- File Formulario 300 electronically via the DIAN Muisca platform (muisca.dian.gov.co).
- Pay via authorized banks.

---

## Section 5 -- Edge cases and special rules

### E-1: Excluded vs. exempt -- critical distinction

- **Excluded (excluido):** No IVA charged. No input IVA recovery. The taxpayer who sells excluded items absorbs any IVA paid on inputs as a cost.
- **Exempt (exento):** No IVA charged (0% rate). BUT the seller CAN recover input IVA. This creates a refund position for producers/exporters of exempt goods.

This distinction is the most common source of errors. Misclassifying excluded as exempt (or vice versa) changes the input IVA recovery calculation entirely.

### E-2: Electronic invoicing (facturacion electronica)

Since 2019, all responsables de IVA must issue electronic invoices via the DIAN system. Input IVA is only deductible if supported by a valid electronic invoice. **Source:** E.T. Art. 616-1; Resolucion DIAN 000042/2020.

### E-3: Withholding IVA (retencion en la fuente por IVA)

Designated withholding agents (grandes contribuyentes, state entities, others) must withhold 15% of the IVA amount on purchases exceeding 4 UVT per transaction. This withholding is an advance on the supplier's IVA liability. **Source:** E.T. Art. 437-1.

### E-4: Regimen Simple de Tributacion (SIMPLE)

The SIMPLE regime is an optional simplified integrated regime that replaces income tax, IVA, ICA (municipal industry and commerce tax), and other taxes with a single progressive payment. Taxpayers in SIMPLE do not file separate IVA returns. This skill does NOT cover SIMPLE.

### E-5: Services consumed in Colombia

Services provided from abroad and consumed in Colombia are subject to 19% IVA. The Colombian buyer must self-assess (autorretencion) and report on the IVA return. **Source:** E.T. Art. 420, Par. 3.

### E-6: Saldo a favor and refund requests

Exporters and producers of exempt goods with persistent saldos a favor may request refunds from DIAN. The refund process requires filing a solicitud de devolucion and typically involves an audit. Processing time: 50 business days (or 30 with a bank guarantee).

---

## Section 6 -- Test suite

### Test 1: Standard bimonthly return

- **Input:** Sales at 19%: COP 50,000,000. Purchases at 19%: COP 30,000,000.
- **Expected:** IVA generado: COP 9,500,000. IVA descontable: COP 5,700,000. Net: COP 3,800,000.

### Test 2: Mixed rates

- **Input:** Sales at 19%: COP 40,000,000. Sales at 5%: COP 10,000,000. Purchases at 19%: COP 25,000,000.
- **Expected:** IVA generado: (40M x 19%) + (10M x 5%) = 7,600,000 + 500,000 = COP 8,100,000. IVA descontable: COP 4,750,000. Net: COP 3,350,000.

### Test 3: Excluded activity (no recovery)

- **Input:** All sales are excluded (education). Purchases with IVA: COP 5,000,000 (IVA: COP 950,000).
- **Expected:** No IVA generado. No IVA descontable (excluded activity). IVA on purchases is a cost.

### Test 4: Export (exempt with recovery)

- **Input:** Export sales: COP 100,000,000 (exempt, 0%). Purchases at 19%: COP 30,000,000 (IVA: COP 5,700,000).
- **Expected:** IVA generado: COP 0. IVA descontable: COP 5,700,000. Saldo a favor: COP 5,700,000. May request refund.

### Test 5: Withholding IVA credit

- **Input:** Net IVA: COP 3,800,000. IVA withheld by clients: COP 1,200,000.
- **Expected:** Amount due: COP 2,600,000.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT confuse excluded with exempt. They have opposite input IVA recovery rules.
- **P-2:** Do NOT claim IVA descontable on purchases related to excluded activities.
- **P-3:** Do NOT accept non-electronic invoices as support for input IVA deductions.
- **P-4:** Do NOT file IVA returns for no responsables (they are not required to file).
- **P-5:** Do NOT ignore the withholding IVA mechanism when clients are designated agents.
- **P-6:** Do NOT prepare SIMPLE regime returns using this skill.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Taxpayer confirmed as responsable de IVA (not no responsable, not SIMPLE)
- [ ] All transactions classified: gravado 19%, gravado 5%, exento, or excluido
- [ ] Excluded vs. exempt distinction correctly applied
- [ ] Input IVA only claimed for taxable/exempt activities (not excluded)
- [ ] Electronic invoices verified for all input IVA claims
- [ ] Withholding IVA credits applied
- [ ] Filing frequency correct (bimonthly or quarterly based on income)
- [ ] Due date checked against DIAN calendar for NIT ending digits

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
