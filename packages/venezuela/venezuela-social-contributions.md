---
name: venezuela-social-contributions
description: "Use this skill whenever asked about Venezuela social security and payroll contributions (IVSS, Paro Forzoso, FAOV, INCES, LOPCYMAT) for employers or employees. Trigger on phrases like \"how much social security do I pay in Venezuela\", \"IVSS contribution\", \"Seguro Social Obligatorio\", \"Paro Forzoso\", \"régimen prestacional de empleo\", \"FAOV housing contribution\", \"INCES training levy\", \"LOPCYMAT\", \"aporte patronal\", \"deducción IVSS\", \"salario mínimo VES 130\", \"cestaticket\", \"bono de guerra\", \"ISLR withholding on salary\", \"Venezuela payroll tax\", or any question about Venezuelan employer/employee statutory contributions. Also trigger when classifying bank statement transactions that relate to IVSS, FAOV/BANAVIH, INCES, or SENIAT debits from Banco de Venezuela, Banesco, Mercantil, or other Venezuelan banks. CRITICAL: Venezuela's legal minimum wage has been frozen at VES 130 since March 2022 and real pay is delivered through NON-salary bonuses (Cestaticket, Bono de Guerra) that are EXCLUDED from the contribution base — never apply contribution rates to total pay. This skill covers contribution rates and splits, the salary vs. non-salary base distinction, contributory ceilings expressed in minimum salaries, the ISLR personal income tax brackets, the Tax Unit (UT) value, filing deadlines, penalties, bank statement classification, and edge cases. ALWAYS read this skill before touching any Venezuelan payroll/social-contribution work."
version: 0.1
jurisdiction: VE
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Jose Padilla
review_status: current
depends_on: - social-contributions-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Venezuela Social Security & Payroll Contributions

## Venezuela Social Security & Payroll Contributions Skill v0.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Jose Padilla** on 2026-06-21.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### venezuela-social-contributions

- **Salario mínimo mensual legal (salario mínimo)** — VES 130  _(PwC; CloudPay)_
- **Valor de la Unidad Tributaria (UT/TU) 2025** — VES 43  _(Administrative Ruling SNAT/2025/000048, Official Gazette 2 June 2025 (Orbitax))_
- **Annual ISLR (personal income tax) return deadline** — 31 March following the tax year (cannot be extended)  _(PwC Tax administration)_
- **IVSS (Social Security) — employer contribution rate (by risk class)** — 9% / 10% / 11%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **IVSS (Social Security) — employee contribution rate** — 4%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **Techo contributivo del IVSS (trabajadores urbanos)** — 5 salarios mínimos = VES 650/mes (5 × VES 130)  _(PwC; CloudPay)_
- **Desempleo (Régimen Prestacional de Empleo) — tasa de contribución patronal** — 2%  _(PwC Worldwide Tax Summaries, revisado el 12 Jan 2026)_
- **Desempleo (Régimen Prestacional de Empleo) — tasa de contribución del empleado** — 0.5%  _(PwC Worldwide Tax Summaries, revisado el 12 Jan 2026)_
- **Techo contributivo del Paro Forzoso (trabajadores urbanos)** — 10 salarios mínimos = VES 1,300/mes (10 × VES 130)  _(PwC)_
- **FAOV (Housing) — employer contribution rate** — 2%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **FAOV (Housing / Ley de Vivienda y Hábitat) — employee contribution rate** — 1%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **FAOV — tope de cotización** — Maximo 10 salarios minimos  _(El artículo 172 de la Ley de Régimen Prestacional de Vivienda y Hábitat,)_
- **INCES employer rate (on total salaries paid)** — 2%  _(PwC Worldwide Tax Summaries — Venezuela)_
- **INCES employee rate (on annual utilidades profit-share bonus)** — 0.5%  _(PwC Worldwide Tax Summaries — Venezuela)_
- **Tasa patronal de LOPCYMAT (según nivel de riesgo; solo a cargo del patrono)** — 0.75% – 10%  _(PwC Worldwide Tax Summaries — Venezuela)_
- **Tasa del trabajador de LOPCYMAT** — 0  _(la lopcymat no pide pagos regulares solo establece sanciones por incumplimientos (multas))_
- **Tope absoluto del IVSS (VES, salario mínimo congelado)** — VES 650/month (5 × VES 130)  _(PwC; CloudPay)_
- **Tope absoluto del Paro Forzoso (VES, salario mínimo congelado)** — VES 1,300/month (10 × VES 130)  _(PwC)_
- **Tramo del ISLR: 0 – 1,000 UT** — 6%; subtraction 0 TU  _(PwC — Venezuela, Individual, Taxes on personal income)_
- **Tramo del ISLR: 1,000 – 1,500 UT** — 9%; subtraction 30 TU  _(PwC — Venezuela, Individual, Taxes on personal income)_
- **Tramo del ISLR: 1,500 – 2,000 UT** — 12%; subtraction 75 TU  _(PwC — Venezuela, Individual, Taxes on personal income)_
- **Tramo del ISLR: 2,000 – 2,500 UT** — 16%; subtraction 155 TU  _(PwC — Venezuela, Individual, Taxes on personal income)_
- **Tramo del ISLR: 2,500 – 3,000 UT** — 20%; subtraction 255 TU  _(PwC — Venezuela, Individual, Taxes on personal income)_
- **Tramo del ISLR: 3,000 – 4,000 UT** — 24%; subtraction 375 TU  _(PwC — Venezuela, Individual, Taxes on personal income)_
- **Tramo del ISLR: 4,000 – 6,000 UT** — 29%; sustraendo 575 UT  _(PwC — Venezuela, Individual, Taxes on personal income)_
- **Tramo del ISLR: más de 6,000 UT** — 34%; sustraendo 875 UT  _(PwC — Venezuela, Individual, Taxes on personal income)_
- **No residente — actividades profesionales no empresariales — tasa legal** — 34% sobre el 90% del ingreso bruto  _(PwC Worldwide Tax Summaries, revisado el 12 Jan 2026)_
- **Impuesto corporativo (Tarifa 2): 0 – 2,000 UT** — 15%  _(PwC — Venezuela, Corporate, Taxes on corporate income)_
- **Impuesto corporativo (Tarifa 2): 2,000 – 3,000 UT** — 22%  _(PwC — Venezuela, Corporate, Taxes on corporate income)_
- **Impuesto corporativo (Tarifa 2): más de 3,000 UT** — 34%  _(PwC — Venezuela, Corporate, Taxes on corporate income)_
- **Tasa fija especial: explotación petrolera** — 50%  _(PwC — Venezuela, Corporate, Taxes on corporate income)_
- **Tasa fija especial: bancos / entidades financieras / seguros** — 40%  _(PwC — Venezuela, Corporate, Taxes on corporate income)_
- **Tasa plana especial: corporaciones en consorcio (joint-venture)** — 50%  _(PwC — Venezuela, Corporate, Taxes on corporate income)_
- **Umbral para la declaración de impuesto estimado (ingresos calificados del año anterior)** — > 1,500 TU (= VES 64,500 a la UT 43 para 2025)  _(PwC, Tax administration)_
- **Fórmula del impuesto estimado** — 75% del impuesto calculado sobre el 80% de los ingresos netos del ejercicio anterior; pagadero en una sola cuota o en 6 cuotas iguales, salvo para sujeto pasivo contribuyente especial que sustituye este proceso por el regimen especial de anticipos que es el 1% de las ventas brutas de cada quincena y pagadero en cada quincena  _(PwC, Tax administration)_
- **Formulario de ISLR para personas naturales (2025, sin confirmar)** — la forma se llama DPN-99025 y actualmente es electronica, tambien llamada forma 25 entre los contadores pero actualmente al ser electronica no se le conoce como forma  _(PwC (no menciona el código para 2025))_
- **Regla de declaración para cónyuges** — Los cónyuges declaran conjuntamente como un solo contribuyente; la declaración separada solo procede con acuerdo escrito de separación de bienes Y cuando los ingresos se limiten a sueldos/honorarios  _(PwC, Tax administration)_
- **Sanción: omisión de ingresos / subdeclaración del ISLR** — Multa del 100% – 300% del impuesto omitido  _(Grant Thornton Venezuela penalty schedule; Justia COT)_
- **Sanción: omisión de presentar una declaración** — Cierre del establecimiento por 10 días más multa de 150× la tasa de la divisa de mayor valor del BCV  _(Grant Thornton Venezuela penalty schedule; Justia COT)_
- **Sanción: declaración incompleta o presentada con retraso de hasta un año** — Multa de 100× la tasa de la divisa de mayor valor del BCV  _(Grant Thornton Venezuela penalty schedule; Justia COT)_
- **Special taxpayer penalty multiplier (COT Art. 108)** — Penalties increased by 200%  _(COT Art. 108; Grant Thornton Venezuela)_
- **Base de indexación de sanciones** — Las sanciones pecuniarias se indexan a la tasa oficial del BCV de la divisa extranjera de mayor valor (indexadas al tipo de cambio, no a la UT)  _(COT 2020 reform)_
- **Fórmula del tope del IVSS** — 5 × salario mínimo mensual  _(PwC)_
- **Fórmula del tope del Paro Forzoso** — 10 × salario mínimo mensual  _(PwC)_
- **Umbral del anticipo de impuesto en VES (2025)** — VES 64,500 (1,500 TU × VES 43)  _(PwC, Tax administration)_
- **INCES employee contribution base** — Annual utilidades (profit-share) bonus — NOT monthly salary; no cap  _(PwC)_
- **Base de la contribución al FAOV** — Maximo 10 salarios minimos  _(El artículo 172 de la Ley de Régimen Prestacional de Vivienda y Hábitat,)_
- **Partidas no salariales excluidas de todas las bases de contribución** — Además la ley establece que no se debe incluir el bono de transporte pero en toda la legislación de Venezuela hay varias caracteristicas que pueden hacer que un bono no tenga caracter salarial y para ello es necesario evaluarlo uno a uno el caso  _(PwC; government non-salary classification)_
- **Rango de tarifas del ISLR para residentes** — 6% – 34% (progresivo, sobre ingresos mundiales)  _(PwC, Taxes on personal income)_

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Venezuela (Bolivarian Republic of Venezuela) |
| Currency | Venezuelan bolívar (VES, "bolívar digital") |
| Social security authority | IVSS — Instituto Venezolano de los Seguros Sociales |
| Tax authority | SENIAT — Servicio Nacional Integrado de Administración Aduanera y Tributaria |
| Housing fund authority | BANAVIH (administers FAOV — Fondo de Ahorro Obligatorio para la Vivienda) |
| Training authority | INCES — Instituto Nacional de Capacitación y Educación Socialista |
| Primary legislation | Ley del Seguro Social; Ley del Régimen Prestacional de Empleo; Ley del Régimen Prestacional de Vivienda y Hábitat; Ley del INCES; LOPCYMAT |
| Tax year | Calendar year |
| Legal minimum monthly wage (salario mínimo) | **VES 130** since 15 March 2022 — unchanged through 2025 (PwC; CloudPay) |
| Tax Unit (UT/TU) value 2025 | **VES 43** per Administrative Ruling SNAT/2025/000048, Official Gazette 2 June 2025 (Orbitax) |
| Annual ISLR (personal income tax) return deadline | **31 March** following the tax year — cannot be extended (PwC Tax administration) |
| Validated by | Verified by Jose Padilla (CPA) on 2026-06-21 |
| Validation date | Verified by Jose Padilla (CPA) on 2026-06-21 |

### CRITICAL Venezuela-specific caveat — read FIRST

The **legal monthly minimum wage (salario mínimo) has been frozen at VES 130 since 15 March 2022** (PwC; CloudPay). Almost all social-security and payroll contributions are legally computed on the **salary** base, which in practice is tiny. Real worker compensation is delivered through **non-salary bonuses** — the *Bono contra la Guerra Económica* ("Bono de Guerra") and the *Cestaticket Socialista* — which the government explicitly classifies as **non-salary** so they are **EXCLUDED** from the contribution base. As of 30 April 2025 the indexed minimum income totalled ~US$160/month (Cestaticket ~$40 + Bono de Guerra ~$120, paid in VES at the BCV rate), while the underlying VES 130 minimum wage is worth only ~US$2.50.

**You MUST account for the salary vs. non-salary distinction. Mechanically applying rates to "total pay" will be wrong.** See Section 5, Rule 1.

### Contribution overview (2025)

Source: PwC Worldwide Tax Summaries — Venezuela, Individual, Other taxes (taxsummaries.pwc.com/venezuela/individual/other-taxes), corroborated by CloudPay (cloudpay.com/payroll-guide/venezuela-payroll-and-benefits-guide).

**Contribution overview table**

| Regime | Employer | Employee | Base / Ceiling |
| --- | --- | --- | --- |
| **IVSS** — Seguro Social Obligatorio (mandatory social security) | 9% / 10% / 11% (by occupational-risk class) | 4% | Capped at **5 minimum salaries** (urban workers) |
| **Paro Forzoso** — Régimen Prestacional de Empleo (unemployment) | 2% | 0.5% | Capped at **10 minimum salaries** (urban workers) |
| **FAOV** — Régimen Prestacional de Vivienda y Hábitat (housing) | 2% | 1% | Total monthly **integral salary, capped at 10 minimum salaries** |
| **INCES** — training levy | 2% (on total salaries paid) | 0.5% (on annual *utilidades* profit-share bonus) | No cap |
| **LOPCYMAT** — workplace prevention/safety | 0.75% – 10% (risk-dependent) | 0% | Total salaries paid; cap interpretation disputed |

- The **IVSS** and **Paro Forzoso** ceilings are expressed in *minimum salaries*. With the frozen VES 130 minimum wage, the contributory ceilings are extremely low in absolute terms (IVSS cap = 5 × VES 130 = VES 650/month; Paro Forzoso cap = 10 × VES 130 = VES 1,300/month).
- **FAOV** uses the *integral salary* (salario integral) capped at **10 minimum salaries** — integral salary includes commissions, gratifications, profit sharing, bonuses, vacation bonus, and shift premiums (PwC).
- IVSS announced contribution-rate administration changes in Feb 2025 (secondary EOR sources, e.g. Rivermate). PwC still reports the classic 4% employee / 9–11% employer split for 2025 — **treat 4% / 9–11% as authoritative**. [RESEARCH GAP — reviewer to confirm whether the Feb-2025 IVSS administrative change altered the split, against ivss.gob.ve.]

### Conservative defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown occupational-risk class (IVSS) | Use the **lowest** employer rate 9% for estimates; flag for reviewer to confirm class |
| Unknown LOPCYMAT risk rate | STOP — do not estimate; range is 0.75%–10% and is too wide to default safely. Flag for reviewer |
| Pay described only as "total pay" or "total income" | STOP — split into salary vs. non-salary (Cestaticket / Bono de Guerra) before applying ANY rate |
| Unknown whether bonus is salary or non-salary | Treat Cestaticket and Bono de Guerra as **non-salary (EXCLUDED)**; flag everything else for reviewer |
| Unknown whether worker is "urban" | Assume urban-worker ceilings (5 / 10 minimum salaries); flag for reviewer |
| Unknown UT for a year other than 2025 | STOP — UT changes by Administrative Ruling; do not assume |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — the worker's **salary** base (the legally-classified *salario*, NOT total compensation) and whether the payment items are salary or non-salary. Without the salary/non-salary split, STOP.

**Recommended** — occupational-risk class (for IVSS 9/10/11%), LOPCYMAT risk rate, integral-salary components (for FAOV), and the annual *utilidades* profit-share figure (for the INCES employee 0.5%).

**Ideal** — the IVSS/BANAVIH/INCES registration records, the payroll register showing salary vs. non-salary line items, and bank statements showing the monthly statutory debits.

### Refusal catalogue

- **R-VE-SC-1 — Salary vs. non-salary split unknown** — Trigger: only "total pay" is provided, with no breakdown of salary vs. Cestaticket / Bono de Guerra. Message: "Venezuelan contributions are computed on the *salary* base only. The Cestaticket Socialista and Bono contra la Guerra Económica are legally non-salary and are excluded. Applying rates to total pay overstates contributions massively. Provide the salary component before I can compute anything."
- **R-VE-SC-2 — LOPCYMAT risk rate unknown** — Trigger: LOPCYMAT computation requested without the assigned risk percentage. Message: "LOPCYMAT employer contributions range 0.75%–10% depending on the assigned occupational-risk rate (INPSASEL classification). I cannot default across a 13× range. Provide the assigned rate or escalate to a licensed accountant."
- **R-VE-SC-3 — IVSS Feb-2025 rate-change query** — Trigger: client asks whether IVSS rates changed in 2025. Message: "Secondary EOR sources reference a Feb-2025 IVSS administrative change, but PwC still reports the 4% employee / 9–11% employer split for 2025. [RESEARCH GAP] This must be confirmed directly against ivss.gob.ve before relying on it. Escalate to a licensed accountant."
- **R-VE-SC-4 — Penalty / arrears quantification** — Trigger: client asks to quantify contribution arrears or COT penalties. Message: "COT penalties are FX-indexed to the BCV highest-value-currency rate and special-taxpayer penalties increase by 200%. Do not estimate arrears or penalties without authority statements. Escalate to a licensed accountant immediately."
- **R-VE-SC-5 — Exact SENIAT/IVSS form code as load-bearing** — Trigger: output depends on naming the exact 2025 ISLR individual form code. Message: "The individual ISLR form is DPN-99025, an electronic form also known informally as 'Forma 25' among accountants. If the exact form code is load-bearing, confirm directly against seniat.gob.ve."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Venezuelan statutory contributions and taxes. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Statutory contributions and tax payments always EXCLUDE from any revenue/expense VAT (IVA) classification — they are statutory obligations, not business supplies. Amounts are in VES.

### 3.1 IVSS / social-security debits

**IVSS / social-security debits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IVSS, SEGURO SOCIAL, SEGURO SOCIAL OBLIGATORIO | EXCLUDE — IVSS contribution | Monthly employer + employee IVSS |
| INSTITUTO VENEZOLANO DE LOS SEGUROS SOCIALES | EXCLUDE — IVSS contribution | Full authority name |
| TIUNA, SISTEMA TIUNA | EXCLUDE — IVSS contribution | IVSS online payment system reference |

### 3.2 Other statutory regimes

**Other statutory regimes table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PARO FORZOSO, REGIMEN PRESTACIONAL DE EMPLEO, RPE | EXCLUDE — unemployment (Paro Forzoso) | Employer 2% / employee 0.5% |
| FAOV, BANAVIH, VIVIENDA Y HABITAT, AHORRO HABITACIONAL | EXCLUDE — housing (FAOV) | Employer 2% / employee 1%, integral salary, cap 10 minimum salaries |
| INCES, INCE | EXCLUDE — training levy | Employer 2% / employee 0.5% on utilidades |
| LOPCYMAT, INPSASEL | EXCLUDE — workplace-safety (LOPCYMAT) | Employer-only 0.75%–10% |

### 3.3 SENIAT / tax payments (NOT social contributions — do not confuse)

**SENIAT / tax payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SENIAT | EXCLUDE — tax payment, not a contribution | ISLR, IVA or other SENIAT tax |
| ISLR, IMPUESTO SOBRE LA RENTA | EXCLUDE — income tax | Not a social contribution |
| IVA, IMPUESTO AL VALOR AGREGADO | EXCLUDE — VAT | Not a social contribution |
| RETENCION, RETENCION ISLR | EXCLUDE — withholding tax | Salary/professional-fee withholding |

### 3.4 Salary and non-salary payroll (exclude from contribution classification)

**Salary and non-salary payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NOMINA, SUELDO, SALARIO (outgoing) | EXCLUDE — payroll (salary) | Salary base; contributions computed separately |
| CESTATICKET, CESTA TICKET, CESTATICKET SOCIALISTA | EXCLUDE — **non-salary** benefit | NOT in the contribution base |
| BONO DE GUERRA, BONO CONTRA LA GUERRA ECONOMICA | EXCLUDE — **non-salary** benefit | NOT in the contribution base |
| UTILIDADES (outgoing) | EXCLUDE — profit-share bonus | INCES employee 0.5% applies to this figure |

### 3.5 Benefit payments received (not contributions paid)

**Benefit payments received table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IVSS PENSION, PENSION DE VEJEZ | EXCLUDE — pension income received | Not a contribution payment |
| PARO FORZOSO PAGO, PRESTACION DESEMPLEO | EXCLUDE — unemployment benefit received | Not a contribution payment |

## Section 4 -- Worked examples

Six bank statement classifications for a hypothetical small employer in Caracas. All amounts in VES. Because the minimum wage is frozen at VES 130, salary-base contributions are tiny in absolute terms; FAOV (no cap, integral salary) is usually the largest line.

> Throughout: the **salary base** used for IVSS/Paro Forzoso is the legally-classified *salario*, which for a minimum-wage worker is VES 130/month, subject to the minimum-salary ceilings. Cestaticket and Bono de Guerra are **excluded**.

### Example 1 — IVSS monthly contribution, single minimum-wage worker

**Input line:**
`05.02.2025 ; IVSS SEGURO SOCIAL OBLIGATORIO ; DEBITO ; ENERO 2025 ; -16,90 ; VES`

**Reasoning:**
Matches "IVSS / SEGURO SOCIAL OBLIGATORIO" (pattern 3.1). Salary base = VES 130 (minimum wage, below the 5-minimum-salary IVSS ceiling of VES 650). Employer 9% (lowest risk class default) + employee 4% = 13% of VES 130 = **VES 16.90**. Excludes from IVA.

Check: 130 × 0.09 = 11.70 (employer); 130 × 0.04 = 5.20 (employee); 11.70 + 5.20 = **16.90**. ✓

**Classification:** EXCLUDE — IVSS contribution (employer VES 11.70 + employee VES 5.20).

### Example 2 — FAOV housing contribution (integral salary, no cap)

**Input line:**
`07.02.2025 ; BANAVIH FAOV AHORRO HABITACIONAL ; DEBITO ; ENERO 2025 ; -3,90 ; VES`

**Reasoning:**
Matches "BANAVIH / FAOV" (pattern 3.2). FAOV uses the **integral salary** with **no ceiling**: employer 2% + employee 1% = 3%. On a VES 130 integral salary (no other integral components present), 3% × 130 = **VES 3.90**. If integral-salary components (commissions, bonuses classified as salary) existed, the base would be higher.

Check: 130 × 0.02 = 2.60 (employer); 130 × 0.01 = 1.30 (employee); 2.60 + 1.30 = **3.90**. ✓

**Classification:** EXCLUDE — FAOV housing contribution (employer VES 2.60 + employee VES 1.30).

### Example 3 — Paro Forzoso (unemployment)

**Input line:**
`07.02.2025 ; PARO FORZOSO REGIMEN PRESTACIONAL EMPLEO ; DEBITO ; ENERO 2025 ; -3,25 ; VES`

**Reasoning:**
Matches "PARO FORZOSO / RPE" (pattern 3.2). Salary base VES 130 (below the 10-minimum-salary ceiling of VES 1,300). Employer 2% + employee 0.5% = 2.5% × 130 = **VES 3.25**.

Check: 130 × 0.02 = 2.60 (employer); 130 × 0.005 = 0.65 (employee); 2.60 + 0.65 = **3.25**. ✓

**Classification:** EXCLUDE — Paro Forzoso (employer VES 2.60 + employee VES 0.65).

### Example 4 — Cestaticket paid (non-salary, NOT a contribution and NOT in the base)

**Input line:**
`10.02.2025 ; CESTATICKET SOCIALISTA ; DEBITO ; FEBRERO 2025 ; -2.080,00 ; VES`

**Reasoning:**
Matches "CESTATICKET" (pattern 3.4). This is a **non-salary** benefit paid to the worker. It is the dominant part of real take-home pay (here ~VES 2,080, far above the VES 130 salary), but it is **EXCLUDED from every contribution base**. Do NOT add it to the salary base when computing IVSS/Paro Forzoso/FAOV. It is also not itself a statutory contribution debit.

**Classification:** EXCLUDE — non-salary benefit. NOT in any contribution base.

### Example 5 — SENIAT ISLR payment (tax, NOT a social contribution)

**Input line:**
`28.03.2025 ; SENIAT ISLR DECLARACION ANUAL ; DEBITO ; EJERCICIO 2024 ; -45.000,00 ; VES`

**Reasoning:**
Matches "SENIAT / ISLR" (pattern 3.3). This is an annual income-tax (ISLR) payment, due by **31 March** following the tax year (PwC Tax administration). It is NOT a social-security contribution — do not classify it as IVSS/FAOV/etc.

**Classification:** EXCLUDE — ISLR income tax payment. NOT a social contribution.

### Example 6 — Ambiguous IVSS lump sum (possible arrears/penalty)

**Input line:**
`15.06.2025 ; IVSS ; DEBITO ; AJUSTE/RECARGO ; -1.250,00 ; VES`

**Reasoning:**
Matches "IVSS" (pattern 3.1) but the amount is irregular and the reference says "AJUSTE/RECARGO" (adjustment/surcharge). This may include arrears plus COT-indexed penalties (FX-indexed to the BCV highest-value-currency rate; +200% for special taxpayers). Principal cannot be separated from penalty without an IVSS statement.

**Classification:** EXCLUDE from IVA. Flag for reviewer — request the IVSS breakdown to split contribution principal from penalty.

## Section 5 -- Tier 1 rules

These rules apply when payroll data is clear and the salary/non-salary split is available. Apply exactly as written. Source for all rates: PwC Worldwide Tax Summaries — Venezuela (Individual, Other taxes & Tax administration) unless noted.

### Rule 1 — Contributions are computed on the SALARY base, NOT total pay

- **Rule 1** — The Cestaticket Socialista and Bono contra la Guerra Económica are non-salary and are EXCLUDED from every contribution base. Always strip these out before applying any rate. This is the single most important rule for Venezuela.  _(PwC; the government's explicit non-salary classification)_

### Rule 2 — IVSS (Seguro Social Obligatorio)

- **Rule 2** — Employer 9% / 10% / 11% by occupational-risk class; employee 4%. Base capped at 5 minimum salaries (urban workers) = 5 × VES 130 = VES 650/month.  _(PwC; CloudPay)_

### Rule 3 — Paro Forzoso (Régimen Prestacional de Empleo)

- **Rule 3** — Employer 2%; employee 0.5%. Base capped at 10 minimum salaries (urban workers) = 10 × VES 130 = VES 1,300/month.  _(PwC)_

### Rule 4 — FAOV (housing) uses integral salary capped at 10 minimum salaries

- **Rule 4** — Employer 2%; employee 1%. Base = total monthly integral salary (commissions, gratifications, profit sharing, bonuses, vacation bonus, shift premiums) — capped at 10 minimum salaries. This is usually the largest contribution line for anyone earning above the salary minimum.  _(PwC)_

### Rule 5 — INCES (training levy)

- **Rule 5** — Employer 2% on total salaries paid; employee 0.5% applied to the annual utilidades (profit-share) bonus — no cap. The employee component is NOT a monthly salary deduction; it attaches to the utilidades payment.  _(PwC)_

### Rule 6 — LOPCYMAT (workplace prevention) is employer-only

- **Rule 6** — Employer 0.75%–10% depending on assigned occupational-risk rate; no employee contribution. Do not default the rate — see R-VE-SC-2.  _(PwC)_

### Rule 7 — Ceilings are expressed in minimum salaries

- **Rule 7** — IVSS = 5 minimum salaries; Paro Forzoso = 10 minimum salaries. With the frozen VES 130 minimum wage, recompute the absolute cap as (multiple × VES 130) whenever the minimum wage figure is current. If the minimum wage changes, the absolute ceilings move with it.

### Rule 8 — ISLR (personal income tax) is separate from contributions

- **Rule 8** — ISLR is progressive 6%–34% on a Tax-Unit (TU) basis for residents (worldwide income); non-residents pay flat 34% on 90% of gross for non-business professional income. The UT value for 2025 is VES 43 (SNAT/2025/000048, Gazette 2 June 2025). See Section 10 for the bracket table.  _(PwC, Taxes on personal income)_

### Rule 9 — ISLR filing deadline is 31 March and cannot be extended

- **Rule 9** — The annual ISLR return is due 31 March following the calendar tax year; late filing triggers penalties plus interest. Major/"special" taxpayers file on SENIAT-set dates.  _(PwC, Tax administration)_

### Rule 10 — Estimated-tax return threshold

- **Rule 10** — An estimated-tax (declaración estimada) return is required if prior-year income from commercial, credit, independent-professional, leasing, or partnership activities exceeded 1,500 TU. Estimated tax = 75% of the tax computed on 80% of estimated income; payable as a single payment or six equal instalments. For 2025, 1,500 TU = 1,500 × VES 43 = VES 64,500.  _(PwC, Tax administration)_

## Section 6 -- Tier 2 catalogue

When data is ambiguous or client circumstances are unclear, flag these situations for reviewer confirmation.

### T2-1 — Occupational-risk class for IVSS (9% vs 10% vs 11%)

**Trigger:** employer IVSS rate must be applied but the risk class is not documented.
**Issue:** the employer rate is 9%, 10%, or 11% depending on the IVSS-assigned occupational-risk class.
**Action:** flag for reviewer. Use 9% only as a provisional estimate and label it as such.

### T2-2 — LOPCYMAT risk rate (0.75%–10%)

**Trigger:** LOPCYMAT contribution must be computed.
**Issue:** the rate spans a 13× range and is assigned per the INPSASEL classification; the cap interpretation is disputed.
**Action:** flag for reviewer. Do not estimate without the assigned rate.

### T2-3 — Integral-salary composition for FAOV

**Trigger:** worker has commissions, bonuses, or shift premiums that may be salary or non-salary.
**Issue:** FAOV uses the integral salary (no cap), so misclassifying a component changes the base directly. Cestaticket and Bono de Guerra are non-salary; other items require judgement.
**Action:** flag for reviewer to confirm which components are integral salary.

### T2-4 — IVSS Feb-2025 administrative change

**Trigger:** client relies on a 2025 IVSS rate.
**Issue:** secondary EOR sources cite a Feb-2025 IVSS administrative change; PwC still shows 4%/9–11%. [RESEARCH GAP]
**Action:** flag for reviewer to confirm against ivss.gob.ve before filing.

### T2-5 — Special-taxpayer (contribuyente especial) status

**Trigger:** client is or may be a SENIAT-designated special taxpayer.
**Issue:** special taxpayers file ISLR on SENIAT-set dates, may make bi-weekly advance payments, and face penalties increased by 200% (COT Art. 108).
**Action:** flag for reviewer to confirm special-taxpayer designation and the applicable calendar.

### T2-6 — Contribution arrears and FX-indexed penalties

**Trigger:** unpaid contributions or COT penalties.
**Issue:** COT-2020 penalties are FX-indexed to the BCV highest-value-currency rate, not UT-indexed; quantification requires authority statements.
**Action:** do not estimate; escalate to a licensed accountant (see R-VE-SC-4).

## Section 7 -- Excel working paper template

When producing a Venezuelan contribution computation, structure the working paper as follows:

```
VENEZUELA SOCIAL CONTRIBUTIONS -- WORKING PAPER
Employer / Client: [name]
Tax Year: [year]            Month: [____]
Prepared: [date]

INPUT DATA
  Salary base (salario, VES):          [____]
  Integral salary (FAOV base, VES):    [____]
  Non-salary excluded items:
     Cestaticket (VES):                [____]  (EXCLUDED)
     Bono de Guerra (VES):             [____]  (EXCLUDED)
  Occupational-risk class (IVSS):      [9% / 10% / 11%]
  LOPCYMAT assigned rate:              [0.75%–10% — confirm]
  Annual utilidades (VES):             [____]  (INCES employee base)
  Minimum wage in force (VES):         130  (since 15 Mar 2022)

CEILINGS (recompute from minimum wage)
  IVSS cap (5 x min wage, VES):        650
  Paro Forzoso cap (10 x min wage):    1,300
  FAOV cap:                            10 minimum salaries (10 × VES 130 = VES 1,300)

CONTRIBUTIONS                           Employer        Employee
  IVSS    (9–11% / 4%):                 [____]          [____]
  Paro Forzoso (2% / 0.5%):            [____]          [____]
  FAOV    (2% / 1%, integral):         [____]          [____]
  INCES   (2% salaries / 0.5% util.):  [____]          [____]
  LOPCYMAT (0.75–10% / nil):           [____]            nil
  ------------------------------------------------------------
  TOTAL:                               [____]          [____]

ISLR (if computing income tax)
  Taxable income (TU = VES / 43):      [____] TU
  Bracket rate:                        [____]%
  Subtraction (TU):                    [____]
  Tax (TU):                            [____]
  Tax (VES = TU x 43):                 [____]

REVIEWER FLAGS
  [List any Tier 2 / RESEARCH GAP flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How statutory debits appear on Venezuelan bank statements

**Banco de Venezuela:**
- Description: "IVSS", "SEGURO SOCIAL OBLIGATORIO", "BANAVIH FAOV", "INCES", "SENIAT"
- Timing: monthly (contributions); ISLR annually around March
- Amount: small in VES for salary-base contributions (minimum wage frozen at VES 130)

**Banesco:**
- Description: "IVSS SEGURO SOCIAL", "FAOV AHORRO HABITACIONAL", "PARO FORZOSO", "RETENCION ISLR"
- Timing: same monthly cycle

**Mercantil / BBVA Provincial / Banco Mercantil:**
- Description: "INSTITUTO VENEZOLANO DE LOS SEGUROS SOCIALES", "BANAVIH", "INCES", "SENIAT"
- Timing: same monthly cycle

**Key identification tips:**
1. Statutory contributions are always outgoing (DEBITO), never credits.
2. Salary-base contributions (IVSS, Paro Forzoso) are tiny in VES because the salary minimum is frozen at VES 130 — do not assume a small debit is an error.
3. FAOV (integral salary, capped at 10 minimum salaries) is usually the largest contribution line for higher earners.
4. **Cestaticket** and **Bono de Guerra** debits are large non-salary payments — they are NOT contributions and NOT in the contribution base.
5. Do not confuse SENIAT (ISLR/IVA tax) debits with IVSS/FAOV/INCES (social contribution) debits.
6. Irregular IVSS/SENIAT lump sums with "RECARGO", "AJUSTE", or "MULTA" may include FX-indexed penalties — flag for reviewer.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for statutory debits** — identify all outgoing payments matching Section 3 patterns (IVSS, FAOV/BANAVIH, Paro Forzoso, INCES, LOPCYMAT, SENIAT).
2. **Separate contributions from tax** — IVSS/FAOV/INCES/Paro Forzoso/LOPCYMAT are social contributions; SENIAT/ISLR/IVA are taxes.
3. **Identify the salary base** — look for NOMINA/SUELDO/SALARIO outgoing lines. Treat CESTATICKET and BONO DE GUERRA as non-salary (excluded from the base).
4. **Reverse-check IVSS:** if you can see the salary base, employer+employee IVSS ≈ 13% (9% + 4%) of the capped salary base. A monthly IVSS debit far above 13% of (5 × minimum wage) suggests arrears or a non-default risk class.
5. **Flag for reviewer:** "Contribution classification derived from bank statement amounts only. Salary vs. non-salary split, occupational-risk class, LOPCYMAT rate, and special-taxpayer status have not been independently verified. Reviewer must confirm before filing."

## Section 10 -- Reference material

### ISLR personal income tax brackets — residents (2025)

**ISLR personal income tax brackets — residents (2025)**  _(PwC — Venezuela, Individual, Taxes on personal income)_

| Taxable income (TU) | Rate | Subtraction (TU) |
| --- | --- | --- |
| 0 – 1,000 | 6% | 0 |
| 1,000 – 1,500 | 9% | 30 |
| 1,500 – 2,000 | 12% | 75 |
| 2,000 – 2,500 | 16% | 155 |
| 2,500 – 3,000 | 20% | 255 |
| 3,000 – 4,000 | 24% | 375 |
| 4,000 – 6,000 | 29% | 575 |
| Over 6,000 | 34% | 875 |

- **Non-residents ISLR rate** — flat 34% on 90% of gross for non-business professional income  _(PwC)_

### Corporate income tax (context)

**Corporate income tax (context)**  _(PwC — Venezuela, Corporate, Taxes on corporate income)_

| Bracket | Rate |
| --- | --- |
| 0–2,000 TU | 15% |
| 2,000–3,000 TU | 22% |
| over 3,000 TU | 34% |

### Filing & registration thresholds

**Filing & registration thresholds table**

| Item | Value | Source |
| --- | --- | --- |
| Annual ISLR return deadline | 31 March (no extension) | PwC, Tax administration |
| Estimated-tax return threshold | prior-year income > 1,500 TU (= VES 64,500 at UT 43) | PwC, Tax administration |
| Estimated tax formula | 75% of tax on 80% of prior-year net income; lump or 6 instalments (special taxpayers: 1% of gross biweekly sales per fortnight) | PwC, Tax administration |
| Individual ISLR form (2025) | DPN-99025 (electronic form, also historically called "Forma 25" among accountants; as an electronic form it is not commonly referred to by a form name) | PwC (does not name 2025 code) |
| Spouses | file jointly as one taxpayer; separate only with written property-separation agreement + salary/fees only | PwC, Tax administration |

### Penalties (Código Orgánico Tributario / COT, 2020 reform)

**Penalties table**  _(Grant Thornton Venezuela penalty schedule; Justia COT)_

| Penalty | Rate / basis |
| --- | --- |
| Omitting income / underpaying ISLR | fine 100%–300% of the omitted tax |
| Failure to file a declaration | 10-day closure of the establishment **plus** fine 150× the BCV highest-value-currency rate |
| Incomplete declaration or delay up to one year | fine 100× the BCV highest-value-currency rate |
| Special taxpayers (COT Art. 108) | penalties increased by **200%** |
| Indexation | pecuniary sanctions indexed to the **BCV official rate of the highest-value foreign currency** (FX-indexed, not UT-indexed) |

### Worked ISLR bracket check (for the test suite)

For taxable income of 5,000 TU (falls in the 4,000–6,000 band): tax = 5,000 × 29% − 575 = 1,450 − 575 = **875 TU**. In VES at UT 43: 875 × 43 = **VES 37,625**.

### Test suite

**Test 1 — IVSS, minimum-wage worker.** Salary base VES 130, risk class lowest (9%). Employer = 130 × 9% = VES 11.70; employee = 130 × 4% = VES 5.20; total = **VES 16.90**.

**Test 2 — FAOV, integral salary VES 130.** Employer = 130 × 2% = VES 2.60; employee = 130 × 1% = VES 1.30; total = **VES 3.90**.

**Test 3 — Paro Forzoso, salary base VES 130.** Employer = 130 × 2% = VES 2.60; employee = 130 × 0.5% = VES 0.65; total = **VES 3.25**.

**Test 4 — IVSS ceiling.** Salary base = VES 2,000 (above the 5-minimum-salary cap). Capped base = 5 × 130 = VES 650. Employer (9%) = VES 58.50; employee (4%) = VES 26.00; total = **VES 84.50** (NOT computed on the uncapped VES 2,000).

**Test 5 — Cestaticket exclusion.** Worker receives salary VES 130 + Cestaticket VES 2,080. Contribution base = **VES 130 only**; Cestaticket VES 2,080 is excluded. IVSS total (per Test 1) = VES 16.90.

**Test 6 — INCES employee on utilidades.** Annual utilidades VES 4,000. Employee INCES = 4,000 × 0.5% = **VES 20.00** (attaches to the utilidades payment, not the monthly salary).

**Test 7 — ISLR resident, taxable income 5,000 TU (2025).** Tax = 5,000 × 29% − 575 = **875 TU** = 875 × VES 43 = **VES 37,625**.

**Test 8 — ISLR resident, taxable income 1,000 TU.** Falls at the top of the 6% band: 1,000 × 6% − 0 = **60 TU** = 60 × VES 43 = **VES 2,580**.

**Test 9 — Estimated-tax threshold (2025).** Prior-year qualifying income of VES 70,000 = 70,000 / 43 = 1,627.9 TU > 1,500 TU → estimated-tax return **required**.

**Test 10 — Non-resident professional fee.** Gross VES 100,000 non-business professional income: tax = 34% × (90% × 100,000) = 34% × 90,000 = **VES 30,600** withheld.

### Prohibitions

- NEVER apply contribution rates to total pay — strip out Cestaticket and Bono de Guerra (non-salary) first.
- NEVER assume the minimum wage has changed — it has been frozen at VES 130 since 15 March 2022; confirm before relying on a different figure.
- NEVER default the LOPCYMAT rate — it spans 0.75%–10%; flag for reviewer.
- NEVER apply IVSS/Paro Forzoso rates to an uncapped base — the ceilings are 5 and 10 minimum salaries respectively.
- NEVER use a UT value other than VES 43 for 2025 without an Administrative Ruling reference.
- NEVER conflate SENIAT (ISLR/IVA tax) debits with IVSS/FAOV/INCES (social contribution) debits.
- NEVER quantify arrears or COT penalties without authority statements — they are FX-indexed and special-taxpayer penalties rise 200%.
- NEVER rely on the IVSS Feb-2025 rate-change claim without confirming against ivss.gob.ve [RESEARCH GAP].
- NEVER cite an exact 2025 ISLR form code as definitive without confirming against seniat.gob.ve [RESEARCH GAP].
- NEVER present contribution or tax figures as definitive — always label as estimated and direct the client to their IVSS/SENIAT statements.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
