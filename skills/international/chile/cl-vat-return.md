---
name: cl-vat-return
description: >
  Chilean VAT return (IVA -- Impuesto al Valor Agregado, Formulario 29) for self-employed individuals. Covers the standard 19% rate, monthly filing via SII portal, debito/credito fiscal, electronic invoicing (DTE/SII), remanente de credito fiscal, and withholding on services. Primary source: DL 825 (Ley de IVA), Ley 20.780 (Tax Reform 2014).
version: 1.0
jurisdiction: CL
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
validated: April 2026
---

# Chile VAT Return (IVA -- Formulario 29) v1.0

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Complete

This is a Tier 2 content skill for preparing the Chilean IVA monthly return (Formulario 29) for self-employed individuals (contribuyentes de primera categoria and trabajadores independientes con inicio de actividades).

---

## Section 1 -- Scope statement

**In scope:**

- Formulario 29 (monthly VAT and withholding return)
- Standard 19% IVA rate
- Debito fiscal (output VAT) and credito fiscal (input VAT)
- Electronic invoicing via SII (Servicio de Impuestos Internos) -- DTE (Documento Tributario Electronico)
- Remanente de credito fiscal (carried-forward input VAT)
- PPM (Pagos Provisionales Mensuales -- monthly provisional income tax payments reported on same form)
- Withholding on fees (retencion de honorarios)

**Out of scope (refused):**

- Annual income tax return (Formulario 22 / Operacion Renta)
- Corporate VAT returns (Sociedades)
- IVA on imports (beyond basic classification)
- IVA on real estate transactions (habitual sellers)
- Special regimes (free trade zones, ZOFRI)
- Transfer pricing

---

## Section 2 -- Filing requirements

### Who must file

Every taxpayer with inicio de actividades (business registration) who conducts taxable activity must file Formulario 29 monthly. This includes self-employed professionals who sell goods or provide taxable services. **Source:** DL 825, Art. 64.

### Filing schedule

| Item | Detail | Source |
|------|--------|--------|
| Filing period | Monthly | DL 825, Art. 64 |
| Due date | 12th of the following month (may vary; check SII calendar) | SII Resolucion Exenta |
| Filing method | Electronic via SII portal (sii.cl) | DL 825; SII instructions |
| Electronic invoicing | Mandatory for all taxpayers since 2018 | Ley 20.727 |

---

## Section 3 -- Rates and thresholds

| Item | Rate | Source |
|------|------|--------|
| Standard IVA rate | 19% | DL 825, Art. 14 |
| Exempt sales | Listed in DL 825, Art. 12 and Art. 13 | DL 825 |
| Exports | Zero-rated (0%) with input VAT recovery | DL 825, Art. 36 |
| PPM rate (first category, general) | Variable (typically 1% of gross income, or actual prior-year effective rate) | Ley de Renta, Art. 84 |
| Retencion de honorarios (withholding on fees to individuals) | 13.75% (2025, increasing annually toward 17% by 2028) | Ley 21.133; Ley de Renta Art. 74 |

### Key exemptions (DL 825, Art. 12-13)

- Education services
- Hospital/health services (public)
- Passenger transport
- Insurance premiums
- Interest on financial operations
- Exported services (zero-rated with credit recovery)

---

## Section 4 -- Computation rules (Step format)

### Step 1: Compute debito fiscal (output VAT)

For each sale/service during the month:
1. Identify if the transaction is taxable (19%), exempt, or zero-rated (export).
2. Verify the DTE (electronic tax document) was issued via SII.
3. Sum the IVA charged on all issued documents.

Document types:
- Factura electronica (33): to other businesses
- Boleta electronica (39): to final consumers
- Nota de credito electronica (61): for adjustments/returns
- Nota de debito electronica (56): for price increases

### Step 2: Compute credito fiscal (input VAT)

For each purchase/expense:
1. Verify the supplier's document is a valid DTE.
2. Verify the expense relates to the taxpayer's taxable activity.
3. Sum the IVA on valid purchase documents received.

Credito fiscal is recoverable only if:
- The purchase is related to taxable (not exempt) activities.
- The DTE is valid and properly issued.
- The document is received within the same month or the following two months.

**Source:** DL 825, Art. 23.

### Step 3: Apply proportional rule if mixed activities

If the taxpayer makes both taxable and exempt sales, credito fiscal must be proportionally allocated. Only the portion attributable to taxable sales is recoverable.

Proportion = taxable sales / (taxable + exempt sales) over the last 12 months.

**Source:** DL 825, Art. 23, No. 3.

### Step 4: Compute net IVA

Debito fiscal - credito fiscal = net IVA.

- If positive: tax to pay.
- If negative: remanente de credito fiscal (carry forward to next month). This balance is adjusted for inflation (UTM-based) and carries forward indefinitely.

### Step 5: Report PPM (Pagos Provisionales Mensuales)

On the same Formulario 29, report the monthly provisional income tax payment:
- PPM = gross income x PPM rate (1% default or prior-year effective rate).
- This is an advance payment of annual income tax, not VAT, but is filed on the same form.

### Step 6: Report withholdings

If the taxpayer received fees subject to retencion de honorarios (13.75% in 2025), report the withheld amount as a credit.

### Step 7: File and pay

- Submit Formulario 29 via SII portal.
- Pay via authorized banks or online (TGR -- Tesoreria General de la Republica).

---

## Section 5 -- Edge cases and special rules

### E-1: Remanente de credito fiscal

Input VAT credits that exceed output VAT carry forward indefinitely. The balance is adjusted monthly for inflation using the UTM (Unidad Tributaria Mensual). This protects the real value of the credit, unlike Argentina where credits erode. **Source:** DL 825, Art. 26.

After six consecutive months of remanente, the taxpayer may request a refund if the credits arise from acquisition of fixed assets.

### E-2: Exports and zero rating

Exports of goods and qualifying services are zero-rated. The exporter can recover all related input VAT. Claims are made via Formulario 29 and may require additional documentation (DUS -- Documento Unico de Salida). **Source:** DL 825, Art. 36.

### E-3: Professional services and IVA

Professional services were historically exempt from IVA in Chile. Since the 2023 reform (effective 2025), certain professional services provided by personas naturales remain exempt from IVA but are subject to the boleta de honorarios withholding regime. Services provided by a business entity (empresa individual) are generally subject to 19% IVA.

### E-4: Construction and real estate

IVA applies to the sale of new real estate by habitual sellers (constructoras). The IVA is 19% on the sale price. A special deduction for construction (credito especial empresas constructoras, CEEC) has been reduced and is being phased out. Flag for reviewer if applicable.

### E-5: Late filing penalties

| Penalty | Amount | Source |
|---------|--------|--------|
| Late filing | 1 UTM per month of delay | Codigo Tributario, Art. 97 No. 2 |
| Late payment | Interest at 1.5% per month | Codigo Tributario, Art. 53 |
| Reajuste (inflation adjustment) | IPC-based adjustment on unpaid tax | Codigo Tributario, Art. 53 |

### E-6: Boleta de honorarios

Self-employed professionals issuing boletas de honorarios are subject to withholding of 13.75% (2025) by the payer. This withholding is an advance on income tax, not IVA. It is reported on Formulario 29 as a credit.

---

## Section 6 -- Test suite

### Test 1: Standard monthly return

- **Input:** Sales at 19%: CLP 10,000,000. Purchases at 19%: CLP 6,000,000.
- **Expected:** Debito: CLP 1,900,000. Credito: CLP 1,140,000. Net IVA: CLP 760,000.

### Test 2: Remanente (credit carry-forward)

- **Input:** Debito: CLP 500,000. Credito: CLP 800,000. Prior remanente: CLP 100,000 (adjusted).
- **Expected:** Total credito: CLP 900,000. Net IVA: -CLP 400,000. New remanente: CLP 400,000.

### Test 3: Mixed taxable and exempt

- **Input:** Taxable sales: CLP 8,000,000. Exempt sales: CLP 2,000,000. Total credito fiscal: CLP 1,200,000.
- **Expected:** Proportion: 80%. Recoverable credito: CLP 960,000.

### Test 4: Export with credit recovery

- **Input:** Export sales: CLP 5,000,000. Related input VAT: CLP 400,000. No domestic taxable sales.
- **Expected:** Debito: CLP 0. Credito: CLP 400,000. Remanente: CLP 400,000. After 6 months, may request refund.

### Test 5: PPM computation

- **Input:** Gross income: CLP 10,000,000. PPM rate: 1%.
- **Expected:** PPM: CLP 100,000. Reported on Formulario 29 alongside IVA.

---

## Section 7 -- Prohibitions

- **P-1:** Do NOT claim credito fiscal from documents that are not valid DTEs.
- **P-2:** Do NOT claim credito fiscal on purchases unrelated to taxable activity.
- **P-3:** Do NOT ignore the proportional rule when both taxable and exempt sales exist.
- **P-4:** Do NOT confuse IVA withholding with income tax withholding (retencion de honorarios).
- **P-5:** Do NOT omit the PPM from Formulario 29. Both IVA and PPM are reported on the same form.
- **P-6:** Do NOT assume all professional services are IVA-exempt. Check the entity type and reform status.

---

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] All sales documents are valid DTEs authorized by SII
- [ ] Correct IVA rate (19%) applied
- [ ] Credito fiscal only from valid purchase DTEs
- [ ] Proportional rule applied if mixed taxable/exempt activities
- [ ] Remanente de credito fiscal adjusted for inflation (UTM)
- [ ] PPM computed and reported on same form
- [ ] Filing due date checked against SII calendar
- [ ] Withholdings on honorarios correctly reported

---

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
