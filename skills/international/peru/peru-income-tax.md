---
name: peru-income-tax
description: Use this skill whenever asked about Peru income tax (Impuesto a la Renta) for individuals — especially rentas de trabajo (4ta categoría independent services and 5ta categoría employment). Trigger on phrases like "how much income tax do I pay in Peru", "Impuesto a la Renta", "Formulario Virtual 709", "renta anual", "recibos por honorarios", "cuarta categoría", "quinta categoría", "rentas de trabajo", "deducción 7 UIT", "deducción adicional 3 UIT", "suspensión de retenciones 4ta", "SUNAT income tax", "UIT", "tramos del impuesto", "renta neta", or any question about filing or computing Peruvian individual income tax. Also trigger when preparing or reviewing a Formulario Virtual N° 709, computing the 7-UIT and 20% deductions, or advising on monthly withholding and suspension. This skill covers the UIT-indexed progressive scale (8/14/17/20/30%), the 7-UIT and additional 3-UIT deductions, the 20% cap for 4ta categoría, withholding, suspension thresholds, FV 709 filing and the cronograma de vencimientos. ALWAYS read this skill before touching any Peru income tax work.
version: 0.1
jurisdiction: PE
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Maria Clemencia Valverde Rios
review_status: current
depends_on:
  - income-tax-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Peru Income Tax (Impuesto a la Renta — Rentas de Trabajo)

## Peru Income Tax (Impuesto a la Renta — Rentas de Trabajo) Skill v0.1

> **DISAMBIGUATION.** This skill is for **PERU** (the Andean republic, capital **Lima**). Currency is the **sol (S/ / PEN)** — **NOT** the Panamanian balboa. The tax authority is **SUNAT** (Superintendencia Nacional de Aduanas y de Administración Tributaria). The tax is **Impuesto a la Renta**. If you find content referencing Panama, the balboa, or a flat-rate Panamanian scale, it is wrong — discard it and use this file.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Maria Clemencia Valverde Rios** on 2026-06-29.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### peru-income-tax

- **UIT 2025 (Unidad Impositiva Tributaria)** — S/ 5,350
- **UIT 2026 (Unidad Impositiva Tributaria)** — S/ 5,500  _(DS N° 301-2025-EF)_
- **Tax year** — Calendar year (1 January — 31 December)
- **Annual return form** — Formulario Virtual N° 709 — Renta Anual — Persona Natural
- **TY2025 filing deadline (staggered by last RUC digit)** — 27 May 2026 — 10 June 2026  _(Res. Sup. N° 386-2025/SUNAT)_
- **Progressive scale tramo 1 — up to 5 UIT (renta neta de trabajo)** — Up to S/ 26,750 — 8%  _(SUNAT Orientación — Tasas del impuesto rentas de trabajo)_
- **Progressive scale tramo 2 — over 5 to 20 UIT** — S/ 26 751 — S/ 107 000 — 14%  _(TUO LIR Art. 53)_
- **Progressive scale tramo 3 — over 20 to 35 UIT** — S/ 107 001 — S/ 187 250 — 17%  _(TUO LIR Art. 53)_
- **Progressive scale tramo 4 — over 35 to 45 UIT** — S/ 187,251 — S/ 240,750 — 20%  _(TUO LIR Art. 53)_
- **Progressive scale tramo 5 — over 45 UIT** — Over S/ 240,750 — 30%  _(SUNAT Orientación — Tasas del impuesto rentas de trabajo)_
- **Cumulative tax at 5 UIT boundary (UIT 2025)** — S/ 2,140.00 at S/ 26,750
- **Cumulative tax at 20 UIT boundary (UIT 2025)** — S/ 13,375.00 at S/ 107,000  _(TUO LIR Art. 53)_
- **Cumulative tax at 35 UIT boundary (UIT 2025)** — S/ 27,017.50 at S/ 187,250  _(TUO LIR Art. 53)_
- **Cumulative tax at 45 UIT boundary (UIT 2025)** — S/ 37,717.50 at S/ 240,750  _(TUO LIR Art. 53)_
- **Non-domiciled (non-resident) individuals — flat rate on gross Peruvian-source income** — flat 30% on gross Peruvian-source income — NO 7-UIT allowance, NO additional deductions  _(R-PE-3)_
- **4ta categoría deduction (20% of gross independent income)** — 20% of gross, capped at 24 UIT (S/ 128,400 at UIT 2025)
- **Fixed 7 UIT deduction (standard exemption for combined 4ta + 5ta)** — 7 UIT = S/ 37,450 at UIT 2025
- **Additional deduction (up to 3 UIT) for eligible sustained expenses** — up to 3 UIT = S/ 16,050 at UIT 2025  _(SUNAT — Deducción adicional para rentas de trabajo)_
- **Additional deduction — residential rent inclusion rate** — 30% of rent paid
- **Additional deduction — domestic-worker social security inclusion rate** — 100% of contributions
- **Additional deduction — qualifying professional services inclusion rate** — 30% of amount paid
- **4ta monthly pago a cuenta rate** — An 8% fourth-category withholding tax applies to fee receipts exceeding S/ 1,500, unless a SUNAT Withholding Tax Suspension Certificate is presented or provided.  _(D.S 215-2006  Art. 2)_
- **4ta monthly pago a cuenta rate** — An 8% fourth-category withholding tax applies to fee receipts exceeding S/ 1,500, unless a SUNAT Withholding Tax Suspension Certificate is presented or provided.  _(D.S 215-2006  Art. 2)_
- **Suspension of 4ta retentions form** — Formulario Virtual N° 1609
- **2025 suspension/obligation threshold — general (4ta, or 4ta + 5ta)** — Monthly obligation if income exceeds S/ 3,901; annual suspension available if projected income ≤ S/ 46,813  _(SUNAT Nota de Prensa N° 100, Dec 2024)_
- **2025 suspension/obligation threshold — directors/trustees/representatives (inc. b) + other 4ta/5ta** — Monthly obligation if income exceeds S/ 3,121; annual suspension available if projected income ≤ S/ 37,450  _(SUNAT Nota de Prensa N° 100, Dec 2024)_
- **2026 suspension/obligation threshold — general** — S/ 48,125/yr (S/ 4,010/mo)  _(Res. de Superintendencia N° 000390-2025/SUNAT)_
- **2026 suspension/obligation threshold — directors** — S/ 38,500/yr (S/ 3,208/mo)  _(Res. de Superintendencia N° 000390-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 0** — 27/05/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 1** — 28/05/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 2** — 29/05/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 3** — 01/06/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 4** — 02/06/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 5** — 03/06/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 6** — 04/06/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 7** — 05/06/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 8** — 08/06/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — last RUC digit 9** — 09/06/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **TY2025 deadline — Buenos contribuyentes & those not required to register in RUC** — 10/06/2026  _(Res. de Superintendencia N° 386-2025/SUNAT)_
- **Capital income (1ra rental / 2da dividends, interest, royalties, gains) effective rate** — Fixed effective rate of 5% on capital income (1st category: rentals / 2nd category: interests, royalties, capital gains) whereas in the case of dividends a nominal rate of 5% is paid  _(TUO LIR Art.36,73 A)_
- **Cap on the 20% deduction (4ta categoría)** — 24 UIT = S/ 128,400 at UIT 2025 which does not apply to earnings of corporate directors, statutory auditors, attorneys-in-fact, business managers, executors, or city councilors, regional board members  _(TUO LIR Art. 45)_
- **Annual return not required when income is solely 5ta** — Taxpayers earning exclusively fifth-category income are exempt from filing an annual return, provided that monthly withholdings covered the annual tax and there is no balance due or tax refund to be claimed for excess withholding.  _(LIR art 79)_

## Section 1 — Quick Reference

**Section 1 — Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Peru (República del Perú), capital Lima |
| Tax | Impuesto a la Renta — individuals ("personas naturales"); resident = "domiciliado" |
| Currency | Sol — S/ (ISO: PEN) only |
| Tax year | Calendar year (1 January — 31 December) |
| Indexing unit | UIT (Unidad Impositiva Tributaria). **UIT 2025 = S/ 5,350** (used for TY2025 return). **UIT 2026 = S/ 5,500** (DS N° 301-2025-EF) |
| Scope of this skill | Rentas de trabajo: **4ta categoría** (independent services — recibos por honorarios) + **5ta categoría** (employment) + foreign-source labour income |
| Out of scope | 1ra categoría (rental), 2da categoría (capital — dividends/interest/gains), 3ra categoría (business/corporate). Each uses a different rate — see Section 6 |
| Tax authority | SUNAT |
| Filing portal | SUNAT Operaciones en Línea (SOL) — https://www.sunat.gob.pe — and the SUNAT Personas APP |
| Annual return form | **Formulario Virtual N° 709 — Renta Anual — Persona Natural** |
| Filing deadline | TY2025: staggered by last RUC digit, **27 May 2026 — 10 June 2026** (Res. Sup. N° 386-2025/SUNAT) — see Section 5.6 |
| Validated by | Verified by Maria Clemencia Valverde Rios (CPA) on 2026-06-29 |
| Validation date | Verified by Maria Clemencia Valverde Rios (CPA) on 2026-06-29 |
| Skill version | 0.1 |

### Progressive Scale — Rentas de Trabajo (4ta + 5ta + foreign-source)

**Progressive scale table**

| Tramo (on renta neta, in UIT) | Tramo in soles (UIT 2025 = S/ 5,350) | Rate |
| --- | --- | --- |
| Up to 5 UIT | Up to S/ 26,750 | **8%** |
| Over 5 to 20 UIT | S/ 26,750 — S/ 107,000 | **14%** |
| Over 20 to 35 UIT | S/ 107,000 — S/ 187,250 | **17%** |
| Over 35 to 45 UIT | S/ 187,250 — S/ 240,750 | **20%** |
| Over 45 UIT | Over S/ 240,750 | **30%** |

- **7-UIT exemption note** — **The 7-UIT exemption (S/ 37,450 at UIT 2025) is a SEPARATE prior deduction — NOT a bracket boundary.** The bracket boundaries are 5 / 20 / 35 / 45 UIT measured on net income after the 7-UIT (and, for 4ta, the 20%) deduction. Source: SUNAT Orientación — Tasas del impuesto rentas de trabajo; SUNAT Orientación — Cálculo del impuesto.  _(SUNAT Orientación — Tasas del impuesto rentas de trabajo; SUNAT Orientación — Cálculo del impuesto)_

**Cumulative tax at each top boundary (UIT 2025)**

| Net income reaches | Cumulative tax |
| --- | --- |
| S/ 26,750 (5 UIT) | S/ 2,140.00 |
| S/ 107,000 (20 UIT) | S/ 13,375.00 |
| S/ 187,250 (35 UIT) | S/ 27,017.50 |
| S/ 240,750 (45 UIT) | S/ 37,717.50 |

(Derivation: 8% × 26,750 = 2,140.00; +14% × 80,250 = 11,235.00 → 13,375.00; +17% × 80,250 = 13,642.50 → 27,017.50; +20% × 53,500 = 10,700.00 → 37,717.50; thereafter 30% on the excess over 240,750.)

- **Non-domiciled (non-resident) individuals** — flat **30%** on gross Peruvian-source income — NO 7-UIT allowance, NO additional deductions. Out of scope for this skill — see R-PE-3.  _(R-PE-3)_

### Order of Computation (rentas de trabajo)

**Order of computation table**

| Step | Operation |
| --- | --- |
| 1 | **4ta categoría:** deduct **20% of gross** independent income, capped at **24 UIT** (S/ 128,400 at UIT 2025). (No 20% for director/trustee-type 4ta income under inc. b.) |
| 2 | Add **5ta categoría** (gross employment income) + foreign-source labour income |
| 3 | Deduct the fixed **7 UIT** (S/ 37,450 at UIT 2025) — standard exemption for combined 4ta + 5ta |
| 4 | Deduct the **additional up to 3 UIT** (S/ 16,050 at UIT 2025) for eligible sustained expenses (Section 5.4) |
| 5 | Result = **renta neta de trabajo** → apply the progressive scale above |
| 6 | Subtract withholdings and pagos a cuenta → balance to pay / refund |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown residency (domiciliado vs no domiciliado) | STOP — do not compute. The scale and deductions only apply to domiciliados (R-PE-3) |
| Unknown UIT year | Use **UIT 2025 (S/ 5,350)** for the TY2025 return; flag if computing 2026 withholding |
| Unknown category of an income receipt | Classify by document: recibo por honorarios → 4ta; payroll/boleta → 5ta. If neither, STOP |
| Unknown whether 4ta income is director/trustee (inc. b) | Treat as inc. b → NO 20% deduction (conservative) |
| Unknown eligibility of an additional-deduction expense | Exclude from the 3-UIT additional deduction |
| Unknown whether expense has valid electronic payment + comprobante | Exclude (additional deduction requires bancarización + electronic comprobante) |
| Unknown whether income is solely 5ta | Assume an annual return MAY be required; do not assert "no filing needed" without confirming income is solely 5ta |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — confirmation of **residency** (domiciliado / no domiciliado); the categories of income earned (4ta and/or 5ta); annual totals of gross 4ta income (sum of recibos por honorarios) and gross 5ta income; and the **UIT year** applicable (TY2025 → S/ 5,350).
- **Recommended** — all recibos por honorarios issued, the certificado de rentas y retenciones (5ta) from the employer, monthly 8% withholding totals on 4ta, any suspensión de retenciones approval (FV 1609), prior-year FV 709 or SUNAT account statement, and the last RUC digit (for the deadline).
- **Ideal** — full ledger of additional-deduction expenses with electronic comprobantes and proof of bancarización (residential rent, domestic-worker social security, qualifying professional / hotel-restaurant services), foreign-source labour income details, and monthly pagos a cuenta records.
- **Refusal if minimum is missing — SOFT WARN** — No residency confirmation = hard stop (R-PE-3). Income totals without supporting documents = proceed with reviewer warning: "This computation was produced from declared totals only. The reviewer must verify each recibo por honorarios, the 5ta certificado de rentas, and that every additional-deduction expense meets the electronic-payment and comprobante requirements."

### Refusal Catalogue

- **R-PE-1** — UIT year ambiguous. "Every bracket and deduction is denominated in UIT. The TY2025 annual return uses UIT 2025 = S/ 5,350; 2026 withholding uses UIT 2026 = S/ 5,500. Confirm the tax year before computing."  _(R-PE-1)_
- **R-PE-2** — Business income (3ra categoría) / RUS / RER / Régimen MYPE. "This skill covers rentas de trabajo (4ta + 5ta) only. Business income (3ra categoría) and the Nuevo RUS / RER / Régimen MYPE Tributario regimes use the corporate/business rules. Escalate to a Peru-licensed CPC."  _(R-PE-2)_
- **R-PE-3** — Non-domiciled / non-resident. "Non-domiciled individuals are taxed at a flat 30% on gross Peruvian-source income with no 7-UIT and no deductions; dual-residency and the 183-day test require specialised analysis. Out of scope. Escalate to a Peru-licensed CPC."  _(R-PE-3)_
- **R-PE-4** — Capital income (1ra / 2da categoría). "Rental income (1ra), and dividends / interest / royalties / securities and property capital gains (2da) use a flat ~5% effective rate, not the progressive scale. Out of scope for this rentas-de-trabajo skill — see Section 6 and escalate if a full return combining categories is needed."  _(R-PE-4)_
- **R-PE-5** — Arrears / fraccionamiento / enforcement. "Client has outstanding SUNAT debt, a fraccionamiento, or is subject to cobranza coactiva. Interest and enforcement are material. Do not advise — escalate to a Peru-licensed CPC immediately."  _(R-PE-5)_
- **R-PE-6** — IGV return requested. "This skill covers income tax (Impuesto a la Renta) only. For Peru VAT, use the peru-igv skill."  _(R-PE-6)_

## Section 3 — Transaction / Document Pattern Library

This is the deterministic pre-classifier. When a document or bank line matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5. Match by case-insensitive substring on the description / counterparty.

### 3.1 Income Patterns

**Income Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RECIBO POR HONORARIOS, RXH, HONORARIOS | 4ta categoría | Gross independent income (before 20%) | Apply 20% deduction (cap 24 UIT) unless director/trustee (inc. b) |
| SERVICIOS PROFESIONALES, CONSULTORÍA, ASESORÍA | 4ta categoría | Gross independent income | Confirm billed via recibo por honorarios |
| DIETA DIRECTORIO, DIRECTOR, MANDATARIO, ALBACEA, SÍNDICO, GESTOR DE NEGOCIOS | 4ta categoría (inc. b) | Gross — **NO 20% deduction** | Director/trustee-type 4ta |
| PLANILLA, REMUNERACIÓN, SUELDO, SALARIO, BOLETA DE PAGO | 5ta categoría | Gross employment income | Employer withholds monthly; goes after 20% step |
| GRATIFICACIÓN, CTS-RELATED REMUNERATION, BONO | 5ta categoría | Per certificado de rentas | CTS itself is generally not taxable income — confirm |
| RENTA DE FUENTE EXTRANJERA (TRABAJO) | Foreign-source labour | Add with 4ta+5ta net | Foreign labour income added to renta neta de trabajo |
| ALQUILER COBRADO, ARRENDAMIENTO | 1ra categoría | OUT OF SCOPE | Flat ~5% effective — see R-PE-4 |
| DIVIDENDOS, INTERESES, REGALÍAS, GANANCIA DE CAPITAL, VENTA DE ACCIONES | 2da categoría | OUT OF SCOPE | Flat ~5% effective — see R-PE-4 |
| DEVOLUCIÓN SUNAT, SALDO A FAVOR | EXCLUDE | Not income | Refund of prior-year tax |

### 3.2 Withholding & Payment Patterns

**Withholding & Payment Patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RETENCIÓN 4TA, RETENCIÓN 8% RXH | Withholding credit (4ta) | 8% retained by agent when recibo > S/ 1,500. Credit against annual tax |
| RETENCIÓN 5TA, RETENCIÓN PLANILLA | Withholding credit (5ta) | Employer monthly withholding (proyección anual ÷ 12). Often final if income solely 5ta |
| PAGO A CUENTA 4TA, PAGO 8% MENSUAL | Payment on account (4ta) | 8% monthly pago a cuenta unless suspended (FV 1609) |
| SUSPENSIÓN DE RETENCIONES, FV 1609, FORMULARIO 1609 | No 4ta withholding/pago a cuenta | Valid only if SUNAT approved and within thresholds (Section 5.5) |
| PAGO RENTA ANUAL, REGULARIZACIÓN FV 709 | Final payment of annual balance | Settles balance after credits |

### 3.3 Additional-Deduction (up to 3 UIT) Eligible Expense Patterns

These feed Step 4 (the additional up to 3 UIT). **All require electronic payment (bancarización) and a valid electronic comprobante.** Many qualifying expenses count at **30%** of the amount paid.

**Additional-Deduction Eligible Expense Patterns table**

| Pattern | Category | Inclusion rate | Notes |
| --- | --- | --- | --- |
| ALQUILER VIVIENDA, ARRENDAMIENTO CASA-HABITACIÓN | Residential rent paid by the taxpayer | 30% of rent paid | Landlord must be properly documented; electronic payment required |
| ESSALUD TRABAJADOR DEL HOGAR, APORTE EMPLEADA DEL HOGAR | Domestic-worker social security | 100% of contributions | Contributions for housekeepers / domestic workers |
| HONORARIOS MÉDICO, ODONTÓLOGO, SERVICIOS PROFESIONALES (4ta of provider) | Qualifying professional services | 30% of amount paid | Provider must issue electronic recibo por honorarios |
| HOTEL, RESTAURANTE, BAR, ALOJAMIENTO | Hotel / restaurant services | Per current SUNAT % | Subject to the annually-set list and percentage [RESEARCH GAP: confirm current-year inclusion % for hotel/restaurant] |

- **Total additional deduction cap** — capped at 3 UIT (S/ 16,050 at UIT 2025) regardless of expenses

### 3.4 Exclusions (neither income nor deduction here)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, ENTRE CUENTAS PROPIAS | EXCLUDE | Own-account transfer |
| PRÉSTAMO, DESEMBOLSO, AMORTIZACIÓN PRÉSTAMO | EXCLUDE | Loan principal movement |
| PAGO IGV, SUNAT IGV | EXCLUDE | VAT — use peru-igv skill |
| CTS (deposit) | EXCLUDE / not taxable | Compensación por Tiempo de Servicios — generally not taxable income; confirm |

## Section 4 — Worked Examples

> All figures use **UIT 2025 = S/ 5,350** and reconcile to the cent. Brackets are applied to **renta neta de trabajo** (after the 7-UIT and 20% deductions).

### Example 1 — Independent only (4ta categoría), below threshold

**Input:** Domiciliado. Gross 4ta income (sum of recibos por honorarios) = S/ 60,000. No 5ta income. No additional-deduction expenses.

**Reasoning:**
- 20% deduction = 0.20 × 60,000 = S/ 12,000 (well under the 24-UIT cap of S/ 128,400). Net after 20% = 48,000.
- Less 7 UIT = S/ 37,450. Renta neta de trabajo = 48,000 − 37,450 = **S/ 10,550**.
- 10,550 is within the first tramo (≤ 5 UIT = 26,750), all at 8%.
- Tax = 8% × 10,550 = **S/ 844.00**.

**Result:** Renta neta = S/ 10,550. Annual tax = **S/ 844.00** (before withholding credits).

### Example 2 — Employment only (5ta categoría)

**Input:** Domiciliado. Gross 5ta employment income = S/ 90,000. No 4ta income. No additional-deduction expenses.

**Reasoning:**
- No 20% deduction (that is a 4ta-only step).
- Less 7 UIT = S/ 37,450. Renta neta = 90,000 − 37,450 = **S/ 52,550**.
- Brackets: first 26,750 at 8% = 2,140.00; remainder 52,550 − 26,750 = 25,800 at 14% = 3,612.00.
- Tax = 2,140.00 + 3,612.00 = **S/ 5,752.00**.

**Result:** Renta neta = S/ 52,550. Annual tax = **S/ 5,752.00**. If income were solely 5ta and the employer's monthly withholding equalled this, no annual return is required (Section 5.5).

### Example 3 — Combined 4ta + 5ta, mid-range

**Input:** Domiciliado. Gross 4ta = S/ 50,000; gross 5ta = S/ 120,000. No additional-deduction expenses.

**Reasoning:**
- 4ta 20% deduction = 0.20 × 50,000 = S/ 10,000 (under cap). 4ta net = 40,000.
- Add 5ta gross 120,000 → 40,000 + 120,000 = S/ 160,000.
- Less 7 UIT = S/ 37,450. Renta neta = 160,000 − 37,450 = **S/ 122,550**.
- Brackets:
  - 26,750 × 8% = 2,140.00
  - (107,000 − 26,750) = 80,250 × 14% = 11,235.00
  - (122,550 − 107,000) = 15,550 × 17% = 2,643.50
- Tax = 2,140.00 + 11,235.00 + 2,643.50 = **S/ 16,018.50**.

**Result:** Renta neta = S/ 122,550. Annual tax = **S/ 16,018.50** (before crediting 8% retentions on 4ta and 5ta withholding).

### Example 4 — High income spanning all brackets

**Input:** Domiciliado. Gross 5ta = S/ 300,000. No 4ta income. No additional deductions.

**Reasoning:**
- Less 7 UIT = S/ 37,450. Renta neta = 300,000 − 37,450 = **S/ 262,550**.
- Brackets:
  - 26,750 × 8% = 2,140.00
  - 80,250 × 14% = 11,235.00
  - 80,250 × 17% = 13,642.50
  - 53,500 × 20% = 10,700.00
  - (262,550 − 240,750) = 21,800 × 30% = 6,540.00
- Tax = 2,140.00 + 11,235.00 + 13,642.50 + 10,700.00 + 6,540.00 = **S/ 44,257.50**.

**Result:** Renta neta = S/ 262,550. Annual tax = **S/ 44,257.50**. (Cross-check: cumulative to 45 UIT = S/ 37,717.50, plus 6,540.00 = 44,257.50.)

### Example 5 — Additional 3-UIT deduction applied

**Input:** Domiciliado. Gross 5ta = S/ 90,000. Residential rent paid (electronically, valid comprobante) = S/ 30,000/year. No other eligible expenses.

**Reasoning:**
- Less 7 UIT = S/ 37,450.
- Additional deduction: residential rent counts at 30% → 0.30 × 30,000 = S/ 9,000. This is under the 3-UIT cap (S/ 16,050), so the full S/ 9,000 is allowed.
- Renta neta = 90,000 − 37,450 − 9,000 = **S/ 43,550**.
- Brackets: 26,750 × 8% = 2,140.00; (43,550 − 26,750) = 16,800 × 14% = 2,352.00.
- Tax = 2,140.00 + 2,352.00 = **S/ 4,492.00**.

**Result:** Renta neta = S/ 43,550. Annual tax = **S/ 4,492.00** (vs S/ 5,752.00 in Example 2 — the additional deduction saved S/ 1,260.00).

### Example 6 — 4ta income with director's fees (inc. b — no 20%)

**Input:** Domiciliado. Independent professional 4ta = S/ 40,000; director's fees (dieta de directorio, inc. b) = S/ 20,000. No 5ta income.

**Reasoning:**
- 20% deduction applies ONLY to the professional 4ta: 0.20 × 40,000 = S/ 8,000. Professional net = 32,000.
- Director's fees (inc. b): NO 20% deduction → full S/ 20,000.
- Subtotal = 32,000 + 20,000 = S/ 52,000.
- Less 7 UIT = S/ 37,450. Renta neta = 52,000 − 37,450 = **S/ 14,550**.
- All within first tramo (≤ 26,750) at 8%: tax = 8% × 14,550 = **S/ 1,164.00**.

**Result:** Renta neta = S/ 14,550. Annual tax = **S/ 1,164.00**.

## Section 5 — Tier 1 Rules (When Data Is Clear)

### 5.1 Scope — Rentas de Trabajo Only

- **Scope** — This skill computes tax on **4ta + 5ta categoría + foreign-source labour income**. Capital income (1ra, 2da) and business income (3ra) are out of scope (R-PE-2, R-PE-4). The progressive scale never applies to capital income.

### 5.2 The 20% Deduction (4ta categoría)

- **20% deduction rules** — - Deduct **20% of gross** independent (4ta) income, **capped at 24 UIT** (S/ 128,400 at UIT 2025). - **Does NOT apply** to inc. b income: director's fees (dietas de directorio), trustees (mandatarios), executors (albaceas), síndicos, and gestores de negocios. - This deduction is taken BEFORE adding 5ta income and BEFORE the 7-UIT deduction.

### 5.3 The 7-UIT Deduction

- **7-UIT deduction rules** — - A fixed **7 UIT** (S/ 37,450 at UIT 2025) is deducted from combined 4ta (post-20%) + 5ta + foreign-source labour income. - It is a standalone exemption, **not** a bracket boundary. Apply it before the progressive scale.

### 5.4 The Additional Deduction (up to 3 UIT)

- **Additional deduction rules** — - Up to **3 UIT** (S/ 16,050 at UIT 2025) for sustained eligible expenses. - Eligible categories: residential rent paid by the taxpayer (counted at 30%), social-security contributions for domestic workers (housekeepers), and certain professional-services and hotel/restaurant expenses. - **Hard requirements:** electronic payment (bancarización) AND a valid electronic comprobante de pago. Cash-paid or undocumented expenses do not qualify. - Many qualifying expenses are included at **30%** of the amount paid. The total is capped at 3 UIT regardless. - Source: SUNAT — Deducción adicional para rentas de trabajo.  _(SUNAT — Deducción adicional para rentas de trabajo)_

### 5.5 Withholding & Monthly Obligations

**Withholding & Monthly Obligations table**

| Item | Rule |
| --- | --- |
| 5ta (employees) | Employer withholds monthly on account (proyección anual ÷ 12). If income is **solely 5ta**, employer withholding is final and **no annual return is required** |
| 4ta withholding | Withholding agent retains **8%** of each recibo por honorarios when the receipt **exceeds S/ 1,500** |
| 4ta pago a cuenta | Independents make monthly pagos a cuenta at **8%** unless suspension is granted |
| Suspensión (FV N° 1609) | Available if projected annual income is within the thresholds below; filed via Formulario Virtual N° 1609 and approved by SUNAT |

**2025 suspension / obligation thresholds**  _(SUNAT Nota de Prensa N° 100, Dec 2024)_

| Profile | Monthly obligation if income exceeds | Annual suspension available if projected income ≤ |
| --- | --- | --- |
| General (4ta, or 4ta + 5ta) | S/ 3,901 | S/ 46,813 |
| Directors/trustees/representatives (inc. b) + other 4ta/5ta | S/ 3,121 | S/ 37,450 |

- **2026 threshold update** — For **2026** these were raised by **Res. de Superintendencia N° 000390-2025/SUNAT** to **S/ 48,125**/yr (S/ 4,010/mo) general and **S/ 38,500**/yr (S/ 3,208/mo) directors — apply those only to a 2026 computation.  _(Res. de Superintendencia N° 000390-2025/SUNAT)_

### 5.6 Annual Return — Form, Filing & Deadlines (TY2025)

- **Form and portal** — **Form: Formulario Virtual N° 709 — Renta Anual — Persona Natural**, filed via SUNAT SOL (www.sunat.gob.pe) and the SUNAT Personas APP. Covers 1ra, 2da, rentas de trabajo, and foreign-source income.
- **Who must file** — persons with a balance to pay on 1ra / 2da / work / foreign income, or claiming a refund / saldo a favor. **Not required** if income is solely 5ta-category employment.

**TY2025 cronograma de vencimientos**  _(Res. de Superintendencia N° 386-2025/SUNAT)_

| Last RUC digit | Due date |
| --- | --- |
| 0 | 27/05/2026 |
| 1 | 28/05/2026 |
| 2 | 29/05/2026 |
| 3 | 01/06/2026 |
| 4 | 02/06/2026 |
| 5 | 03/06/2026 |
| 6 | 04/06/2026 |
| 7 | 05/06/2026 |
| 8 | 08/06/2026 |
| 9 | 09/06/2026 |
| Buenos contribuyentes & those not required to register in RUC | 10/06/2026 |

### 5.7 Crediting Withholdings Against Annual Tax

- **Crediting rules** — - 8% retentions on 4ta and employer 5ta withholdings are credits against the annual tax. - Pagos a cuenta already made are also credited. - A positive remainder = balance to pay (regularización via FV 709); a negative remainder = saldo a favor / refund.

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Additional 3-UIT Deduction — Eligibility & Documentation

- **Eligibility & documentation rules** — - Confirm each expense has electronic payment (bancarización) and a valid electronic comprobante. - Confirm the correct inclusion percentage (e.g. 30% for residential rent and many professional services) and that the annual list still includes the category for the tax year. - **Conservative default:** exclude any expense whose documentation or category cannot be confirmed. - **Flag for reviewer:** total claimed vs the 3-UIT cap; current-year hotel/restaurant inclusion percentage.

### 6.2 4ta inc. b Classification (no 20% deduction)

- **inc. b classification rules** — - Director's fees, trustees, executors, síndicos, gestores de negocios get NO 20% deduction. - **Conservative default:** if uncertain whether 4ta income is inc. a (professional) or inc. b, treat as inc. b (no 20%). - **Flag for reviewer:** confirm the nature of each 4ta income stream.

### 6.3 Foreign-Source Labour Income

- **Foreign-source labour income rules** — - Foreign-source labour income of a domiciliado is added to renta neta de trabajo; foreign tax credits may apply. - **Conservative default:** include foreign labour income; do not assume a foreign tax credit without documentation. - **Flag for reviewer:** confirm source, conversion to soles, and any treaty / foreign tax credit.

### 6.4 Residency Determination

- **Residency determination rules** — - Domiciliado status (and the 183-day rule, loss/recovery of residency) determines whether the scale applies at all. - **Conservative default:** STOP if residency is unclear (R-PE-3). - **Flag for reviewer:** confirm domiciliado status for the full tax year.

### 6.5 Solely-5ta "No Filing Required" Determination

- **Solely-5ta determination rules** — - Only valid if the taxpayer has exclusively 5ta income and withholding was correctly applied. - **Conservative default:** do not assert "no filing required" unless income is confirmed solely 5ta with no balance and no refund claim. - **Flag for reviewer:** confirm no 4ta, 1ra, 2da, or foreign income exists.

### 6.6 UIT Year Selection for Cross-Year Work

- **UIT year selection rules** — - TY2025 return → UIT 2025 (S/ 5,350); 2026 monthly withholding → UIT 2026 (S/ 5,500). - **Flag for reviewer:** confirm which UIT applies to the period being computed.

## Section 7 — Working Paper Template

PERU IMPUESTO A LA RENTA — RENTAS DE TRABAJO — WORKING PAPER
Tax Year: 2025        UIT 2025 = S/ 5,350
Client: ___________________________   RUC: __________   Last RUC digit: ___
Residency: Domiciliado / No domiciliado   (STOP if No domiciliado)

A. 4TA CATEGORÍA (INDEPENDENT)
  A1. Gross 4ta — inc. a (professional, recibos honorarios)  ___________
  A2. Less 20% deduction (cap 24 UIT = S/ 128,400)           (__________)
  A3. 4ta inc. a net (A1 - A2)                               ___________
  A4. Gross 4ta — inc. b (director/trustee — NO 20%)         ___________
  A5. Total 4ta net (A3 + A4)                                ___________

B. 5TA CATEGORÍA (EMPLOYMENT)
  B1. Gross 5ta employment income                            ___________

C. FOREIGN-SOURCE LABOUR INCOME
  C1. Foreign labour income (in soles)                       ___________

D. SUBTOTAL (A5 + B1 + C1)                                   ___________

E. DEDUCTIONS
  E1. Less 7 UIT (S/ 37,450)                                 (__________)
  E2. Less additional deduction (up to 3 UIT = S/ 16,050)    (__________)

F. RENTA NETA DE TRABAJO (D - E1 - E2)                       ___________

G. TAX COMPUTATION (pass to deterministic engine)
  Tramo 1: up to 26,750 @ 8%                                 ___________
  Tramo 2: 26,750–107,000 @ 14%                              ___________
  Tramo 3: 107,000–187,250 @ 17%                             ___________
  Tramo 4: 187,250–240,750 @ 20%                             ___________
  Tramo 5: over 240,750 @ 30%                                ___________
  G1. Total annual tax                                       ___________

H. CREDITS
  H1. 8% retentions on 4ta                                   (__________)
  H2. 5ta employer withholding                               (__________)
  H3. Pagos a cuenta                                         (__________)
  H4. Balance to pay / (saldo a favor) (G1 - H1 - H2 - H3)   ___________

REVIEWER FLAGS:
  [ ] Residency (domiciliado) confirmed for full year?
  [ ] Correct UIT year applied?
  [ ] 4ta inc. a vs inc. b correctly split (20% only on inc. a)?
  [ ] 20% cap (24 UIT) respected?
  [ ] Additional-deduction expenses have bancarización + electronic comprobante?
  [ ] Additional deduction within 3-UIT cap?
  [ ] Foreign-source labour income included / FTC documented?
  [ ] If "no filing", confirmed income is solely 5ta?
  [ ] All bracket totals reconcile to the cent?

## Section 8 — Document Reading Guide

### Peruvian Income Documents

**Peruvian Income Documents**

**Peruvian Income Documents**  _(Section 8 — Document Reading Guide)_

| Document | Income type | Key fields | Notes |
| --- | --- | --- | --- |
| Recibo por honorarios electrónico (RHE) | 4ta categoría | Monto bruto, retención 8%, monto neto | Sum the brutos for gross 4ta. 8% retained when > S/ 1,500 |
| Boleta de pago / planilla | 5ta categoría | Remuneración, descuentos, retención | Employer payroll; monthly withholding shown |
| Certificado de rentas y retenciones | 5ta (and 4ta) | Total renta, total retenciones | Annual summary issued by withholding agent — primary source for 5ta |
| Formulario Virtual N° 1609 | Suspension approval | Vigencia, importe proyectado | Confirms suspension of 4ta withholding |
| Reporte de retenciones SUNAT | Credits | Retenciones acumuladas | Cross-check withholding credits |

### Key Peruvian Tax Terms

**Key Peruvian Tax Terms**  _(Section 8 — Document Reading Guide)_

| Term | English | Classification hint |
| --- | --- | --- |
| Renta bruta | Gross income | Before deductions |
| Renta neta | Net income | After deductions — the bracket base |
| Retención | Withholding | Credit against annual tax |
| Pago a cuenta | Payment on account | Credit against annual tax |
| Recibo por honorarios | Independent-service receipt | 4ta categoría income |
| Planilla / remuneración | Payroll / salary | 5ta categoría income |
| Domiciliado | Resident | Scale applies; no domiciliado = flat 30% |
| UIT | Tax unit | Indexing unit for all thresholds |
| Bancarización | Electronic payment | Required for additional deduction |
| Comprobante de pago | Tax receipt/invoice | Required for additional deduction |

## Section 9 — Onboarding Fallback

If the client provides documents but cannot answer onboarding questions immediately:

1. Classify all income/documents using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1) — including STOP on unknown residency.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

ONBOARDING QUESTIONS — PERU IMPUESTO A LA RENTA (RENTAS DE TRABAJO)
1. Residency: are you domiciliado in Peru for the full tax year?
2. Which income did you earn: 4ta (independent/recibos), 5ta (employment), or both?
3. For 4ta: was any of it director's fees, trustee, executor, or síndico (inc. b)?
4. Total gross 4ta income (sum of recibos por honorarios)?
5. Total gross 5ta employment income (per certificado de rentas)?
6. Any foreign-source labour income?
7. Did you pay residential rent, domestic-worker social security, or qualifying
   professional/hotel-restaurant expenses electronically with valid comprobantes?
8. Total 8% retentions on 4ta and 5ta employer withholding for the year?
9. Any pagos a cuenta made? Any suspension of retentions (FV 1609) approved?
10. What is the last digit of your RUC (for the filing deadline)?

## Section 10 — Reference Material

### Key Legal / Source References

**Key Legal / Source References**  _(Section 10 — Reference Material)_

| Topic | Reference |
| --- | --- |
| Progressive scale (8/14/17/20/30%) | SUNAT Orientación — Tasas del impuesto rentas de trabajo: https://orientacion.sunat.gob.pe/7076-05-tasas-del-impuesto-rentas-de-trabajo |
| Tax computation method | SUNAT Orientación — Cálculo del impuesto: https://orientacion.sunat.gob.pe/3071-02-calculo-del-impuesto |
| Categories, 20% & 7-UIT, non-resident 30% | PwC Worldwide Tax Summaries — Peru Individual: https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income (and /deductions, /tax-administration, /income-determination) |
| Additional 3-UIT deduction | SUNAT — Deducción adicional para rentas de trabajo: https://renta.sunat.gob.pe/personas/deduccion-adicional-para-rentas-de-trabajo |
| FV 709 cronograma (TY2025) | SUNAT — Cronograma Renta Anual 2025 FV 709: https://renta.sunat.gob.pe/personas/cronograma-de-declaracion-renta-anual-2025-formulario-ndeg-709 (Res. Sup. N° 386-2025/SUNAT) |
| Suspension of 4ta withholding | SUNAT — Suspensión de retenciones: https://personas.sunat.gob.pe/trabajador-independiente/suspension-retenciones |
| 2026 suspension amounts | Res. de Superintendencia N° 000390-2025/SUNAT (via LP Derecho) |
| UIT 2025 / 2026 | SUNAT Renta 2025: https://renta.sunat.gob.pe/ ; DS N° 301-2025-EF (UIT 2026 = S/ 5,500); EY Perú — Nuevo valor UIT 2026 |
| Peru VAT (separate) | peru-igv skill |

### UIT Reference

**UIT Reference**  _(Section 10 — Reference Material)_

| Year | UIT value | Use |
| --- | --- | --- |
| 2025 | S/ 5,350 | TY2025 annual return (FV 709, filed 2026) |
| 2026 | S/ 5,500 | 2026 monthly withholding / 2026 computations (DS N° 301-2025-EF, eff. 1 Jan 2026) |

### Bracket Reconciliation (UIT 2025)

**Bracket Reconciliation (UIT 2025)**  _(Section 10 — Reference Material)_

| Boundary | Soles | Width | Rate | Tax in band | Cumulative |
| --- | --- | --- | --- | --- | --- |
| 5 UIT | 26,750 | 26,750 | 8% | 2,140.00 | 2,140.00 |
| 20 UIT | 107,000 | 80,250 | 14% | 11,235.00 | 13,375.00 |
| 35 UIT | 187,250 | 80,250 | 17% | 13,642.50 | 27,017.50 |
| 45 UIT | 240,750 | 53,500 | 20% | 10,700.00 | 37,717.50 |
| > 45 UIT | — | excess | 30% | excess × 30% | 37,717.50 + excess×30% |

### Test Suite

**Test 1 — Independent only, low income.**
Input: Domiciliado, gross 4ta S/ 60,000, no 5ta, no additional deductions.
Expected: 20% = 12,000 → net 48,000; less 7 UIT 37,450 → renta neta 10,550; tax 8% × 10,550 = **S/ 844.00**.

**Test 2 — Employment only.**
Input: Domiciliado, gross 5ta S/ 90,000, no additional deductions.
Expected: less 7 UIT → 52,550; tax = 2,140.00 + (25,800 × 14% = 3,612.00) = **S/ 5,752.00**.

**Test 3 — Combined 4ta + 5ta.**
Input: Domiciliado, gross 4ta 50,000, gross 5ta 120,000.
Expected: 4ta net 40,000; +120,000 = 160,000; less 7 UIT → 122,550; tax = 2,140 + 11,235 + (15,550 × 17% = 2,643.50) = **S/ 16,018.50**.

**Test 4 — All brackets.**
Input: Domiciliado, gross 5ta 300,000.
Expected: renta neta 262,550; tax = 37,717.50 + (21,800 × 30% = 6,540) = **S/ 44,257.50**.

**Test 5 — Additional 3-UIT deduction.**
Input: Domiciliado, gross 5ta 90,000, residential rent paid 30,000 (electronic, valid comprobante).
Expected: additional deduction = 30% × 30,000 = 9,000 (under 3-UIT cap); renta neta = 90,000 − 37,450 − 9,000 = 43,550; tax = 2,140 + (16,800 × 14% = 2,352) = **S/ 4,492.00**.

**Test 6 — Director's fees (inc. b, no 20%).**
Input: Domiciliado, professional 4ta 40,000, director's fees 20,000.
Expected: 20% only on professional → net 32,000; +20,000 director = 52,000; less 7 UIT → 14,550; tax 8% × 14,550 = **S/ 1,164.00**.

**Test 7 — Non-domiciled (refusal).**
Input: No domiciliado, Peruvian-source salary.
Expected: STOP (R-PE-3). Flat 30% on gross with no deductions — out of scope.

## PROHIBITIONS

- **R-PE-3** — Non-domiciled individuals pay a flat 30% on gross Peruvian-source income with no deductions — the progressive scale must never be applied to a non-domiciled individual.  _(PROHIBITIONS section)_
- **Jurisdiction and currency** — NEVER use Panama, the balboa, or any Panamanian scale — this is PERU, currency sol (S/ / PEN), authority SUNAT.  _(PROHIBITIONS section)_
- **7-UIT exemption is not a bracket boundary** — NEVER treat the 7-UIT exemption as a bracket boundary — the boundaries are 5/20/35/45 UIT on net income.  _(PROHIBITIONS section)_
- **20% deduction scope** — NEVER apply the 20% deduction to 5ta income or to 4ta inc. b (director/trustee) income.  _(PROHIBITIONS section)_
- **Deduction caps** — NEVER exceed the 24-UIT cap on the 20% deduction or the 3-UIT cap on the additional deduction.  _(PROHIBITIONS section)_
- **Additional deduction requirements** — NEVER allow an additional-deduction expense without electronic payment (bancarización) and a valid electronic comprobante.  _(PROHIBITIONS section)_
- **Capital income rate** — NEVER apply the progressive scale to 1ra or 2da categoría (capital) income — that is a flat ~5% effective rate.  _(PROHIBITIONS section)_
- **UIT year consistency** — NEVER mix UIT years — TY2025 uses S/ 5,350; 2026 uses S/ 5,500.  _(PROHIBITIONS section)_
- **No-filing assertion** — NEVER assert "no annual return required" unless income is confirmed solely 5ta.  _(PROHIBITIONS section)_
- **Deterministic engine required** — NEVER compute final tax figures directly as definitive — pass renta neta to the deterministic engine and label outputs as estimated.  _(PROHIBITIONS section)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Peru-licensed Contador Público Colegiado, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

### Key Peruvian Tax Terms

- **Renta bruta** — Gross income (Before deductions)
- **Renta neta** — Net income (After deductions — the bracket base)
- **Retención** — Withholding (Credit against annual tax)
- **Pago a cuenta** — Payment on account (Credit against annual tax)
- **Recibo por honorarios** — Independent-service receipt (4ta categoría income)
- **Planilla / remuneración** — Payroll / salary (5ta categoría income)
- **Domiciliado** — Resident (Scale applies; no domiciliado = flat 30%)
- **UIT** — Tax unit (Indexing unit for all thresholds)
- **Bancarización** — Electronic payment (Required for additional deduction)
- **Comprobante de pago** — Tax receipt/invoice (Required for additional deduction)

### UIT Reference

- **UIT 2025** — S/ 5,350  _(TY2025 annual return (FV 709, filed 2026))_
- **UIT 2026** — S/ 5,500  _(2026 monthly withholding / 2026 computations (DS N° 301-2025-EF, eff. 1 Jan 2026))_

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
