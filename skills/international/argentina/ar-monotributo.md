---
name: ar-monotributo
description: >
  Use this skill whenever asked about the Argentine Monotributo simplified tax regime. Trigger on phrases like "monotributo", "regimen simplificado", "AFIP", "DAS monotributo", "categorias monotributo", "impuesto integrado", "monotributista", or any question about the unified monthly payment, category thresholds, or obligations for small self-employed individuals in Argentina. Covers the unified monthly payment (impuesto integrado + aportes jubilatorios + obra social), revenue-based categories (A through K), and exclusion rules. ALWAYS read this skill before touching any Argentine Monotributo work.
version: 2.0
jurisdiction: AR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Argentina Monotributo -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Argentina |
| Tax | Monotributo unified payment (impuesto integrado + SIPA pension + obra social) |
| Currency | ARS only |
| Tax year | Calendar year |
| Primary legislation | Ley 24.977 (Monotributo, Regimen Simplificado para Pequenos Contribuyentes), as amended |
| Supporting legislation | RG AFIP; Decreto reglamentario |
| Tax authority | Administracion Federal de Ingresos Publicos (AFIP) / ARCA |
| Filing portal | Monotributo portal via AFIP web (afip.gob.ar) |
| Filing deadline | Monthly DAS by the 20th; recategorization January 20 and July 20 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by an Argentine contador publico |
| Skill version | 2.0 |

### Services Categories (2025 approximate)

| Cat. | Max Annual Revenue (ARS) | Impuesto Integrado (ARS/month) | Aportes Jubilatorios (ARS/month) | Obra Social (ARS/month) | Total Monthly (ARS) |
|---|---|---|---|---|---|
| A | ~2,108,288 | ~1,047 | ~5,540 | ~7,402 | ~13,989 |
| B | ~3,133,941 | ~2,014 | ~6,094 | ~7,402 | ~15,510 |
| C | ~4,387,518 | ~3,441 | ~6,703 | ~7,402 | ~17,546 |
| D | ~5,449,094 | ~5,658 | ~7,374 | ~7,402 | ~20,434 |
| E | ~6,416,528 | ~8,904 | ~8,186 | ~7,402 | ~24,492 |
| F | ~8,020,660 | ~12,776 | ~8,837 | ~7,402 | ~29,015 |
| G | ~9,624,792 | ~17,029 | ~9,520 | ~7,402 | ~33,951 |
| H | ~11,916,410 | ~30,454 | ~10,510 | ~7,402 | ~48,366 |

### Goods Categories (higher thresholds, additional physical parameters)

| Cat. | Max Annual Revenue (ARS) |
|---|---|
| I | ~13,337,213 |
| J | ~15,285,088 |
| K | ~16,957,968 |

All amounts are approximate. AFIP updates these semi-annually. Verify at afip.gob.ar.

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown activity type | Services (lower revenue ceilings -- most conservative) |
| Unknown category | Highest category that fits revenue (highest payment) |
| Unknown obra social election | Enrolled |
| Unknown unit price limit | Assume limit applies |
| Unknown employee count | Zero |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- gross revenue for the last 12 months, activity type (services vs goods), and current Monotributo category.

**Recommended** -- commercial premises area, electricity consumption, annual rent paid, unit price of goods, number of employees, obra social enrollment status, prior recategorization history.

**Ideal** -- AFIP portal data export, complete electronic invoice register (Factura C), bank statements for the 12-month rolling period.

### Refusal Catalogue

**R-AR-1 -- Regimen General.** "Revenue exceeds the maximum Monotributo threshold. Client must be in the Regimen General (IVA + Ganancias). This skill does not cover the general regime."

**R-AR-2 -- Sociedades.** "Companies (SRL, SA, SAS) file under different regimes. This skill covers individual Monotributistas only."

**R-AR-3 -- Exclusion transition planning.** "Transition from Monotributo to Regimen General involves retroactive effects and complex planning. Escalate to contador publico."

**R-AR-4 -- Foreign income with CEPO.** "Foreign exchange regulations (CEPO) affecting receipt of foreign-source income require specialist analysis. Escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | Tax Label | Treatment | Notes |
|---|---|---|---|
| CLIENT PAYMENT, TRANSFERENCIA | Monotributo revenue | Include in 12-month rolling revenue | Core income |
| MERCADO PAGO, MP COBRO | Monotributo revenue | Include | Platform receipts |
| FACTURA C COBRO | Monotributo revenue | Include | Invoice collection |
| EXPORTACION SERVICIOS, FACTURA E | Monotributo revenue (export) | Include in revenue threshold | Must issue Factura E |
| TRANSFERENCIA PROPIA, AHORRO | EXCLUDE | Internal transfer | Between own accounts |
| DEVOLUCION, REINTEGRO | Check | May reduce revenue | Refund -- verify if net or gross |
| SUBSIDIO, PLAN SOCIAL | EXCLUDE | Government transfer | Not Monotributo revenue |
| INTERESES, PLAZO FIJO | EXCLUDE | Financial income | Not Monotributo activity income |

### 3.2 Expense Patterns (Debits on Bank Statement)

Monotributo does NOT require expense tracking (no deductions). However, these patterns help identify the DAS payment and operational context:

| Pattern | Treatment | Notes |
|---|---|---|
| AFIP DAS, MONOTRIBUTO, VEP | Monthly unified payment | Impuesto integrado + SIPA + obra social |
| PAGO FACIL, RAPIPAGO (AFIP) | DAS payment via payment network | Same |
| DEBITO AUTOMATICO AFIP | Automatic DAS deduction | Same |
| INGRESOS BRUTOS, IIBB | Provincial gross receipts tax | Separate obligation -- not covered |
| PERSONAL, SUPERMERCADO, ALQUILER | EXCLUDE | Personal expense |

### 3.3 Platform-Specific Patterns

| Pattern | Treatment | Notes |
|---|---|---|
| MERCADO LIBRE, ML VENTA | Revenue | Goods sale via marketplace |
| PEDIDOS YA, RAPPI | Revenue | Delivery platform income |
| PAYPAL, WISE, PAYONEER | Revenue (foreign) | Must issue Factura E; verify CEPO compliance |
| STRIPE PAYOUT | Revenue (foreign) | Same |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Services Freelancer, Category D

**Input:** Freelance consultant, annual revenue ARS 5,000,000, services only.

**Computation:**
- Category D (revenue <= ~5,449,094)
- Monthly payment: ~ARS 20,434 (impuesto integrado ~5,658 + aportes ~7,374 + obra social ~7,402)
- Annual cost: ~ARS 245,208

### Example 2 -- Low-Income Category A

**Input:** Freelance tutor, annual revenue ARS 1,500,000.

**Computation:**
- Category A (revenue <= ~2,108,288)
- Monthly payment: ~ARS 13,989
- Annual cost: ~ARS 167,868

### Example 3 -- Goods Seller, Category I

**Input:** Online retailer, annual revenue ARS 12,000,000, premises 80 m2, unit price ARS 50,000.

**Computation:**
- Category I (goods, revenue <= ~13,337,213)
- Must verify premises area, electricity, rent are within limits
- Monthly payment per Category I table

### Example 4 -- Exclusion Trigger

**Input:** Services freelancer, 12-month revenue ARS 13,000,000.

**Classification:**
- Exceeds Category H ceiling (~11,916,410) for services
- EXCLUDED from Monotributo
- Must register for Regimen General (IVA + Ganancias)
- ESCALATE to contador publico

### Example 5 -- Recategorization Needed

**Input:** Currently Category B. Trailing 12-month revenue = ARS 4,000,000.

**Computation:**
- Exceeds Category B (~3,133,941) but within Category C (~4,387,518)
- Must recategorize to C at next semi-annual window
- New monthly payment: ~ARS 17,546

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Monotributo Structure

**Legislation:** Ley 24.977, Art. 6-11

The Monotributo is a unified monthly payment replacing income tax (Ganancias), VAT (IVA), pension contributions (SIPA), and health coverage (obra social) with a single fixed monthly amount determined by category.

### 5.2 Category Determination

**Legislation:** Ley 24.977, Art. 8

Category is determined by the highest of: (a) gross revenue in the last 12 months, (b) commercial premises area, (c) electricity consumption, (d) rent paid. For services, only revenue applies. For goods, all parameters apply.

### 5.3 Recategorization

**Legislation:** Ley 24.977, Art. 9

Semi-annual recategorization (January and July). Based on revenue and parameters over the preceding 12 months. Deadline: January 20 and July 20. AFIP may recategorize automatically based on electronic invoice data.

### 5.4 Factura C Requirements

Monotributo invoices must be Factura C (no IVA discrimination). Must include: CUIT of issuer, current category letter, description of service/goods, total amount, and CAE from AFIP's online invoicing system. For exports: Factura E.

### 5.5 Physical Parameter Limits (Goods)

**Legislation:** Ley 24.977, Art. 8

Premises area: from 30 m2 (Cat A) to 200 m2 (Cat K). Electricity consumed: from 3,330 kW to 20,000 kW. Rent paid: increasing ceilings per category. Unit price: max ~ARS 180,589 per unit. Services categories do NOT have physical parameters.

### 5.6 Payment and Compliance

Payment deadline: 20th of each month. Methods: VEP, debito automatico, Pago Facil/Rapipago. Electronic invoicing is mandatory (Factura C). Annual informativa required for some categories.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Revenue Approaching Category Ceiling

Freelancer in Category D with 11 months of revenue at ARS 5,200,000. If 12-month rolling revenue exceeds Category D ceiling, must recategorize to E at next semi-annual window. If exceeds all ceilings, exclusion applies. Flag for reviewer to monitor and advise.

### 6.2 Mixed Services and Goods

AFIP considers the primary activity. If goods sales are incidental, services categories apply. If both are significant, the higher threshold (goods) categories may apply, but all physical parameters must also be met. Flag for reviewer.

### 6.3 Client Receives Income from Abroad

Foreign-source income IS included in Monotributo revenue thresholds. Client must issue Factura E (exportacion de servicios). Currency conversion at official rate. Flag for reviewer -- foreign exchange regulations (CEPO) may affect receipt of funds.

### 6.4 Voluntary Departure from Monotributo

Can voluntarily renounce Monotributo and register for IVA + Ganancias. Effective from the first day of the month following renunciation. Cannot return to Monotributo for 3 years.

---

## Section 7 -- Excel Working Paper Template

```
ARGENTINA MONOTRIBUTO -- Working Paper
Period: [12-month rolling period]

A. REVENUE DETERMINATION
  A1. Gross revenue (last 12 months)              ___________
  A2. Activity type (services / goods / mixed)     ___________
  A3. Premises area (m2) -- goods only             ___________
  A4. Electricity consumption (kW) -- goods only   ___________
  A5. Annual rent paid (ARS) -- goods only         ___________
  A6. Max unit price of goods (ARS)                ___________

B. CATEGORY DETERMINATION
  B1. Revenue-based category                       ___________
  B2. Premises-based category (goods only)         ___________
  B3. Final category (highest of B1, B2)           ___________

C. MONTHLY PAYMENT
  C1. Impuesto integrado                           ___________
  C2. Aportes jubilatorios                         ___________
  C3. Obra social                                  ___________
  C4. TOTAL MONTHLY DAS                            ___________

D. ANNUAL COST
  D1. C4 x 12                                     ___________

REVIEWER FLAGS:
  [ ] Revenue verified against AFIP invoicing data?
  [ ] Recategorization window approaching?
  [ ] Physical parameters within limits (goods)?
  [ ] Foreign income included in revenue?
  [ ] Approaching exclusion threshold?
```

---

## Section 8 -- Bank Statement Reading Guide

### Argentine Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| Banco Nacion, Banco Provincia | PDF, CSV | Fecha, Descripcion, Debito, Credito, Saldo |
| Galicia, BBVA, Santander | CSV, PDF | Fecha, Concepto, Importe, Saldo |
| Brubank, Uala, Naranja X | CSV | Fecha, Descripcion, Monto |
| Mercado Pago | CSV, PDF | Fecha, Detalle, Monto |
| Wise, Payoneer | CSV | Date, Description, Amount, Currency |

### Key Argentine Banking Terms

| Term | Classification Hint |
|---|---|
| TRANSFERENCIA RECIBIDA | Incoming payment -- likely revenue |
| DEBITO AUTOMATICO | Regular outgoing -- check if DAS |
| COMPRA CON DEBITO | Point-of-sale purchase |
| EXTRACCION ATM | Cash withdrawal |
| PLAZO FIJO | Term deposit interest |
| MERCADO PAGO | Could be income or expense |
| VEP AFIP | Tax payment |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- ARGENTINA MONOTRIBUTO
1. What is your CUIT?
2. Are you currently registered as Monotributista?
3. What is your current category?
4. Activity type: services, goods, or both?
5. Gross revenue in the last 12 months?
6. Do you have commercial premises? Area in m2?
7. Do you have employees?
8. Are you enrolled in obra social?
9. Do you invoice foreign clients (Factura E)?
10. Date of last recategorization?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Monotributo structure | Ley 24.977, Art. 6-11 |
| Category table | Ley 24.977, Art. 8 |
| Physical parameters | Ley 24.977, Art. 8 |
| Recategorization | Ley 24.977, Art. 9 |
| Exclusion rules | Ley 24.977, Art. 20-21 |
| Payment deadlines | Ley 24.977, Art. 31 |
| Factura C requirements | RG AFIP facturacion electronica |
| Factura E (exports) | RG AFIP exportacion de servicios |

### Monotributo Social

Monotributo Social is a reduced-cost version for vulnerable populations, cooperatives, and social economy workers. Different eligibility criteria. Reduced or zero impuesto integrado. Verify eligibility with AFIP or social services.

### Late Payment Consequences

Interest accrues on unpaid amounts. After prolonged non-payment, AFIP may suspend the CUIT and the client loses obra social coverage. Must regularize through AFIP's payment plan system (Mis Facilidades).

---

## PROHIBITIONS

- NEVER allow Monotributo for revenue exceeding the maximum category threshold -- client must be in Regimen General
- NEVER issue Factura A or B from a Monotributo taxpayer -- Monotributo uses Factura C (or E for exports)
- NEVER discriminate IVA on a Monotributo invoice -- IVA is embedded in the unified payment
- NEVER ignore physical parameters for goods sellers -- revenue alone is insufficient
- NEVER treat Monotributo amounts as fixed forever -- they are updated semi-annually by AFIP
- NEVER allow a client excluded from Monotributo to continue making Monotributo payments
- NEVER ignore the 3-year lockout when voluntarily leaving Monotributo
- NEVER present calculations as definitive -- always label as estimated and direct client to a contador publico

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico or equivalent licensed practitioner in Argentina) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
