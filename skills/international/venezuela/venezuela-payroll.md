---
name: venezuela-payroll
description: Use this skill whenever asked about Venezuela payroll processing for employed persons. Trigger on phrases like "Venezuela payroll", "ISLR Venezuela", "Impuesto Sobre la Renta withholding", "retención ISLR", "Unidad Tributaria", "valor de la UT", "IVSS deduction", "Seguro Social Venezuela", "FAOV", "Ley de Vivienda y Hábitat", "INCES", "Paro Forzoso", "Régimen Prestacional de Empleo", "LOPCYMAT", "AR-I", "AR-C", "ARC", "comprobante de retención", "salario mínimo Venezuela", "Ingreso Mínimo Integral", "bono de guerra económica", "cestaticket", "desgravamen único", "rebaja personal", "net salary Venezuela", "salario neto Venezuela", "gross to net Venezuela", "IGTF", "bolívares payroll", or any question about computing employee pay, income-tax withholding, or social-security/parafiscal contributions for Venezuela-based employees. This skill covers ISLR (income tax) withholding by the employer, IVSS social security, Paro Forzoso (employment benefit), FAOV (housing), INCES (training), LOPCYMAT (workplace safety), the frozen legal minimum wage vs the USD-indexed non-salary bonuses (Ingreso Mínimo Integral), the AR-I / AR-C withholding mechanism, and filing obligations to SENIAT. ALWAYS read this skill before processing any Venezuela payroll.
version: 0.1
jurisdiction: VE
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Jose Padilla
review_status: current
depends_on:
  - payroll-workflow-base
category: payroll
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Venezuela Payroll

## Venezuela Payroll Skill v0.1

> **Tier 2 (research-verified) — NOT yet accountant-verified.** Several figures carry `[RESEARCH GAP — reviewer to confirm]` markers. A licensed Venezuelan contador público colegiado must reconcile those before any output is presented as final.

> **Hyperinflation / UT context (READ FIRST).** Almost every statutory figure in Venezuelan tax law is expressed in **Tax Units (Unidad Tributaria — UT)**, not bolívares. The current value is **VES 43.00 per UT**, effective **2 June 2025** (Providencia Administrativa SNAT/2025/0048, Gaceta Oficial No. 43,140). Using the wrong UT value invalidates every ISLR computation. Separately, the **legal minimum wage is frozen at VES 130/month** (since March 2022); the bulk of worker compensation is paid as **explicitly non-salary USD-indexed bonuses** that do NOT enter the contribution or ISLR base. Both distortions are statutory and must be modelled as written below, not "corrected."

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Jose Padilla** on 2026-06-21.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### venezuela-payroll

- **Tax Unit (UT) value** — VES 43.00  _(Providencia Administrativa SNAT/2025/0048, Gaceta Oficial No. 43,140)_
- **Tax year** — Calendar year (1 January – 31 December)  _(PwC — Venezuela individual)_
- **Salario mínimo legal (salario mínimo)** — VES 130/mes (congelado desde marzo de 2022)  _(PwC (other taxes, 'VES 130 as of 15 March 2022'); WageIndicator)_
- **Ingreso Mínimo Integral (IMI)** — El 30 de abril 2026 por anuncio presidencial se ajusta a 240 USD al mes y se hace obligatorio para la empresa privada  _(Guacamaya)_
- **Bono de Guerra Económica (bono no salarial)** — El 30 de abril 2026 por anuncio presidencial se ajusta a 200 USD al mes y se hace obligatorio para la empresa privada  _(Guacamaya)_
- **Cestaticket (bono de alimentación no salarial)** — US$40/mes  _(Guacamaya)_
- **ISLR — alícuota del tramo 1 (0–1,000 UT)** — 6%; sustraendo 0 UT  _(Art. 50 LISR; PwC Worldwide Tax Summaries — Venezuela (last reviewed 12 Jan 2026))_
- **ISLR — alícuota del tramo 2 (1,000–1,500 UT)** — 9%; sustraendo 30 UT  _(Art. 50 LISR; PwC Worldwide Tax Summaries — Venezuela (last reviewed 12 Jan 2026))_
- **ISLR impuesto sobre la renta — tarifa del tramo 3 (1,500–2,000 UT)** — 12%; sustraendo 75 UT  _(Art. 50 LISR; PwC Worldwide Tax Summaries — Venezuela (última revisión 12 Jan 2026))_
- **ISLR impuesto sobre la renta — tarifa del tramo 4 (2,000–2,500 UT)** — 16%; sustraendo 155 UT  _(Art. 50 LISR; PwC Worldwide Tax Summaries — Venezuela (última revisión 12 Jan 2026))_
- **ISLR impuesto sobre la renta — tarifa del tramo 5 (2,500–3,000 UT)** — 20%; sustraendo 255 UT  _(Art. 50 LISR; PwC Worldwide Tax Summaries — Venezuela (última revisión 12 Jan 2026))_
- **ISLR impuesto sobre la renta — tarifa del tramo 6 (3,000–4,000 UT)** — 24%; sustraendo 375 UT  _(Art. 50 LISR; PwC Worldwide Tax Summaries — Venezuela (última revisión 12 Jan 2026))_
- **ISLR impuesto sobre la renta — tarifa del tramo 7 (4,000–6,000 UT)** — 29%; sustraendo 575 UT  _(Art. 50 LISR; PwC Worldwide Tax Summaries — Venezuela (última revisión 12 Jan 2026))_
- **ISLR impuesto sobre la renta — tarifa del tramo 8 (más de 6,000 UT)** — 34%; sustraendo 875 UT  _(Art. 50 LISR; PwC Worldwide Tax Summaries — Venezuela (última revisión 12 Jan 2026))_
- **Fórmula de cálculo de la tarifa del ISLR** — impuesto = (renta gravable en UT × tasa del tramo) − sustraendo del tramo, luego × VES 43  _(Art. 50 LISR; PwC)_
- **Desgravamen único (deducción personal estándar)** — 774 UT por año (= Bs. 33,282 a la UT de 2025)  _(ISLR Law Art. 60 and 61)_
- **Crédito fiscal personal (rebaja personal) — por contribuyente** — 10 UT (= VES 430 at VES 43/UT)  _(PwC; Nayma Consultores)_
- **Crédito fiscal personal (rebaja personal) — por carga (hijos/padres)** — 10 UT per registered dependent  _(PwC; Nayma Consultores)_
- **Tasa de retención para no residentes (tasa única)** — 34% withheld at source on Venezuelan-source income  _(PwC — Venezuela individual)_
- **Base de retención para no residentes — servicios profesionales** — 34% applied to 90% of gross payments  _(PwC — Venezuela individual)_
- **Umbral de retención del ISLR (obligación patronal activada)** — Estimated net annual enrichment ≥ 1,000 UT (= VES 43,000 at VES 43/UT)  _(PwC; Nayma Consultores)_
- **IVSS (Social Security) — employee contribution rate** — 4%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **IVSS — tasa de contribución patronal (clase de riesgo mínimo/bajo)** — 9%  _(PwC; CloudPay; Rivermate)_
- **IVSS — tasa de contribución patronal (clase de riesgo medio)** — 10%  _(PwC; CloudPay; Rivermate)_
- **IVSS — tasa de contribución patronal (máxima / clase de alto riesgo)** — 11%  _(PwC; CloudPay; Rivermate)_
- **Techo contributivo del IVSS** — Hasta 5 salarios mínimos urbanos (≈ VES 650/mes al salario mínimo congelado de VES 130)  _(PwC)_
- **Desempleo (Régimen Prestacional de Empleo) — tasa de contribución del empleado** — 0.5%  _(PwC Worldwide Tax Summaries, revisado el 12 Jan 2026)_
- **Desempleo (Régimen Prestacional de Empleo) — tasa de contribución patronal** — 2%  _(PwC Worldwide Tax Summaries, revisado el 12 Jan 2026)_
- **Techo contributivo del Paro Forzoso** — Hasta 10 salarios mínimos urbanos (≈ VES 1,300/mes al salario mínimo congelado de VES 130)  _(PwC)_
- **FAOV (Housing / Ley de Vivienda y Hábitat) — employee contribution rate** — 1%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **FAOV (Housing) — employer contribution rate** — 2%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **FAOV — tope de cotización** — Maximo 10 salarios minimos  _(El artículo 172 de la Ley de Régimen Prestacional de Vivienda y Hábitat,)_
- **INCES — employee contribution rate (base: utilidades/profit-sharing)** — 0.5% on annual utilidades  _(PwC)_
- **INCES — employer contribution rate (base: total wages/salaries paid)** — 2% on total payroll  _(PwC)_
- **LOPCYMAT — employer contribution rate (workplace health & safety)** — 0  _(la lopcymat no pide pagos regulares solo establece sanciones por incumplimientos (multas))_
- **Tasa total de contribución del empleado sobre el salario (IVSS + Paro + FAOV)** — 5.5%  _(PwC)_
- **Tasa total mínima de contribución patronal sobre el salario (IVSS mín + Paro + FAOV)** — 13.0%  _(PwC)_
- **Tasa total máxima de contribución patronal sobre el salario (IVSS máx + Paro + FAOV)** — 15.0%  _(PwC)_
- **Carga parafiscal patronal combinada incluyendo INCES (excluido LOPCYMAT)** — 15.0%–17.0% de la base salarial  _(PwC)_
- **Tasa del IGTF (Impuesto a las Grandes Transacciones Financieras)** — 3% sobre los pagos realizados en divisas o criptomonedas a través del sistema financiero  _(PwC Worldwide Tax Summaries — Venezuela (other taxes, last reviewed 12 Jan 2026))_
- **Tasa del Impuesto al Patrimonio Neto** — 0.25%/año  _(PwC Worldwide Tax Summaries — Venezuela (otros impuestos, última revisión 12 Jan 2026))_
- **Impuesto al Patrimonio Neto — umbral mínimo de patrimonio neto** — 150,000,000 UT  _(PwC Worldwide Tax Summaries — Venezuela (otros impuestos, última revisión 12 Jan 2026))_
- **Fecha límite para la declaración anual del ISLR (impuesto sobre la renta de personas naturales)** — 31 de marzo del año siguiente al ejercicio fiscal (no prorrogable)  _(PwC Tax administration)_
- **Opción de pago fraccionado del ISLR — cuota 1** — 31 March  _(Efecto Cocuyo; El Diario)_
- **Opción de pago fraccionado del ISLR — cuota 2** — 21 April  _(Efecto Cocuyo; El Diario)_
- **Opción de pago fraccionado del ISLR — cuota 3** — 12 May  _(Efecto Cocuyo; El Diario)_
- **Obligados a declarar el ISLR — umbral de enriquecimiento neto** — Enriquecimiento neto > 1,000 UT  _(Efecto Cocuyo)_
- **Obligados a declarar el ISLR — umbral de ingresos brutos** — Ingresos brutos > 1,500 UT  _(Efecto Cocuyo)_
- **Formulario AR-I — momento de presentación** — Presentado por el empleado al empleador antes del primer pago del año; actualizar si cambian las circunstancias  _(Nayma Consultores; Efecto Cocuyo)_
- **Sanción por ingresos omitidos / pago insuficiente** — 100% al 300% del impuesto omitido  _(Grant Thornton Venezuela COT table; Galac; MPPEF; COT 2020 reform)_
- **Omisión de presentar declaración — sanción de cierre** — Cierre del establecimiento por 10 días  _(Grant Thornton; COT 2020 reform)_
- **Omisión de presentar declaración — multa monetaria** — Multa de 150× la tasa de cambio oficial más alta del BCV  _(Grant Thornton; COT 2020 reform)_
- **Declaración incompleta o presentada con retraso (≤ 1 año)** — Multa de 100× la tasa de cambio oficial más alta del BCV  _(Grant Thornton; COT 2020 reform)_
- **Pago tardío (enteramiento tardío) — tasa diaria dentro del primer año** — 0.28% del monto adeudado por día de mora, con tope del 100%  _(Grant Thornton; Galac; COT 2020 reform)_
- **Pago tardío — recargo adicional después de 1 año** — 50% adicional del monto adeudado  _(Grant Thornton; COT 2020 reform)_
- **Pago tardío — recargo adicional después de 2 años** — 150% adicional del monto adeudado  _(Grant Thornton; COT 2020 reform)_
- **Multiplicador de sanción para contribuyentes especiales (COT Art. 108)** — Sanciones incrementadas en un 200%  _(COT Art. 108; Grant Thornton Venezuela)_

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Venezuela (República Bolivariana de Venezuela) |
| Currency | Bolívar (VES / Bs.) — wages legally denominated in bolívares; USD bonuses are non-salary |
| Standard pay frequency | Bi-weekly (quincenal) or monthly; minimum wage stated monthly |
| Tax year | Calendar year (1 January -- 31 December) (PwC — Venezuela individual) |
| Income tax | YES — ISLR (Impuesto Sobre la Renta), progressive 6%–34% in UT, employer-withheld |
| Tax Unit (UT) value | **VES 43.00**, effective 2 Jun 2025 (SNAT/2025/0048, Gaceta 43,140) |
| Tax authority | SENIAT (Servicio Nacional Integrado de Administración Aduanera y Tributaria) |
| Social security authority | IVSS (Instituto Venezolano de los Seguros Sociales) |
| Housing fund | FAOV / BANAVIH (Ley de Régimen Prestacional de Vivienda y Hábitat) |
| Training levy | INCES (Instituto Nacional de Capacitación y Educación Socialista) |
| Workplace safety | LOPCYMAT / INPSASEL |
| Employee withholding form | **AR-I** (employee → employer, sets withholding %) |
| Employer certificate form | **AR-C / ARC** (employer → employee, comprobante de retención) |
| Annual ISLR return deadline | **31 March** (natural persons; PwC; Efecto Cocuyo) |
| Key legislation | Ley de Impuesto Sobre la Renta (Art. 50, Art. 31); Código Orgánico Tributario (COT); Ley del Seguro Social; Ley del Régimen Prestacional de Empleo; Ley del Régimen Prestacional de Vivienda y Hábitat; Ley del INCES; LOPCYMAT |
| Filing portal | SENIAT en línea (`declaraciones.seniat.gob.ve`) |
| Validated by | Verified by Jose Padilla (CPA) on 2026-06-21 |
| Skill version | 0.1 |

## Section 2 -- Income Tax Withholding (ISLR — Impuesto Sobre la Renta)

Venezuela **does** levy personal income tax on employees. The employer is a **withholding agent (agente de retención)** and applies a withholding percentage derived from the employee's **Form AR-I** declaration (PwC — Venezuela individual; Nayma Consultores). Residents are taxed on worldwide income; the progressive tariff (Art. 50 LISR) is expressed in **UT**.

### ISLR Progressive Tariff (Art. 50 LISR) — Tax Year 2025

**ISLR Progressive Tariff (Art. 50 LISR) — Tax Year 2025**  _(Source: PwC Worldwide Tax Summaries — Venezuela (taxes on personal income, last reviewed 12 Jan 2026). Method: `tax = (taxable income in UT × bracket rate) − bracket subtraction`, then `× VES 43`.)_

| Taxable income (UT) | Rate | Subtraction (UT) |
| --- | --- | --- |
| 0 – 1,000 | 6% | 0 |
| 1,000 – 1,500 | 9% | 30 |
| 1,500 – 2,000 | 12% | 75 |
| 2,000 – 2,500 | 16% | 155 |
| 2,500 – 3,000 | 20% | 255 |
| 3,000 – 4,000 | 24% | 375 |
| 4,000 – 6,000 | 29% | 575 |
| Over 6,000 | 34% | 875 |

**Continuity check (cumulative ISLR in UT at each bracket edge)**

| Edge (UT) | Lower band tax | Upper band tax | Tie? |
| --- | --- | --- | --- |
| 1,000 | 1,000×0.06−0 = **60** | 1,000×0.09−30 = **60** | ✓ |
| 1,500 | 1,500×0.09−30 = **105** | 1,500×0.12−75 = **105** | ✓ |
| 2,000 | 2,000×0.12−75 = **165** | 2,000×0.16−155 = **165** | ✓ |
| 2,500 | 2,500×0.16−155 = **245** | 2,500×0.20−255 = **245** | ✓ |
| 3,000 | 3,000×0.20−255 = **345** | 3,000×0.24−375 = **345** | ✓ |
| 4,000 | 4,000×0.24−375 = **585** | 4,000×0.29−575 = **585** | ✓ |
| 6,000 | 6,000×0.29−575 = **1,165** | 6,000×0.34−875 = **1,165** | ✓ |

All subtraction constants tie out exactly.

### Deductions and credits (PwC — Venezuela individual)

**Deductions and credits table**

| Item | Amount | Notes | Source |
| --- | --- | --- | --- |
| Standard deduction (desgravamen único) | **774 UT** (= VES 33,282 at VES 43) | Alternative to itemizing; subtracted from gross before applying the tariff | PwC; Nayma Consultores; Guacamaya |
| Personal tax credit (rebaja personal) | **10 UT per taxpayer** | Plus per dependent (children/parents registered in the SENIAT profile) | PwC; Nayma Consultores |

774 UT × VES 43 = **VES 33,282**. 10 UT × VES 43 = **VES 430** credit per taxpayer.

### Non-residents

- **Non-resident withholding** — Flat **34%** withheld at source on Venezuelan-source income; for professional services the 34% applies to **90%** of gross payments  _(PwC — Venezuela individual)_

## Section 3 -- ISLR Payroll Withholding Mechanism (employer obligation)

**ISLR Payroll Withholding Mechanism table**

| Item | Detail | Source |
| --- | --- | --- |
| Withholding threshold | Employer withholds ISLR from salary only when estimated **net annual enrichment ≥ 1,000 UT** (= **VES 43,000** at VES 43). Below this, no withholding. | PwC; Nayma Consultores |
| Form AR-I | Filed by the **employee → employer**. The worker estimates annual income, desgravámenes and dependents to derive the withholding **percentage** the employer applies each pay period. Submit before the first payment of the year; update if circumstances change. | Nayma Consultores; Efecto Cocuyo |
| Form AR-C (ARC) | Issued by the **employer → employee** — comprobante de retención summarizing prior-year income and ISLR withheld; needed by the employee to file the annual return. | Nayma Consultores |

> **Practical reality:** because the minimum wage is frozen at VES 130/month (Section 6) and most compensation is paid as **non-salary bonuses** excluded from the ISLR salary base, the typical formally-paid worker's net annual enrichment falls **below 1,000 UT (VES 43,000)**, so **no ISLR is withheld in practice**. The mechanics above must still be authored and applied correctly for any worker whose salary base does cross the threshold.

## Section 4 -- Social Security & Parafiscal Contributions

Primary source: **PwC Worldwide Tax Summaries — Venezuela (other taxes, last reviewed 12 Jan 2026)**, which gives the exact splits, ceilings and minimum-wage-denominated caps. Secondary corroboration of the IVSS 4%/9–11% and FAOV 1%/2% splits: CloudPay and Rivermate (EOR guides).

### Contribution table (2025)

**Contribution table (2025)**

| Regime | Employee | Employer | Base / ceiling | Source |
| --- | --- | --- | --- | --- |
| **IVSS** (Seguro Social) | **4%** | **9% / 10% / 11%** by company risk class (min/medium/max) | Up to **5 minimum urban salaries** | PwC; CloudPay; Rivermate |
| **Paro Forzoso** (Régimen Prestacional de Empleo — forced unemployment) | **0.5%** | **2%** | Up to **10 minimum urban salaries** | PwC |
| **FAOV** (Régimen Prestacional de Vivienda y Hábitat — housing) | **1%** | **2%** | Up to **10 minimum salaries** | PwC; CloudPay |
| **INCES** (training) | **0.5%** (on utilidades / profit-sharing bonus) | **2%** (on total wages/salaries paid) | Employer base = total payroll; employee base = annual utilidades | PwC |
| **LOPCYMAT** (workplace health & safety) | — (employer only) | **0%** | Confirmed 0 — `[RESEARCH GAP — reviewer to confirm]` | PwC (noted "disputed") |

### Column totals — salary-based regimes (IVSS + Paro Forzoso + FAOV)

**Column totals table**

| Side | IVSS | Paro Forzoso | FAOV | **Salary total** |
| --- | --- | --- | --- | --- |
| Employee | 4.0% | 0.5% | 1.0% | **5.5%** |
| Employer (min risk class, IVSS 9%) | 9.0% | 2.0% | 2.0% | **13.0%** |
| Employer (max risk class, IVSS 11%) | 11.0% | 2.0% | 2.0% | **15.0%** |

> INCES employee 0.5% is excluded from the salary total because its base is the **annual utilidades bonus**, not the monthly salary. LOPCYMAT is excluded because its rate is risk-dependent and disputed.

*Check:* employee 4.0 + 0.5 + 1.0 = **5.5%**. Employer (min) 9.0 + 2.0 + 2.0 = **13.0%**; (max) 11.0 + 2.0 + 2.0 = **15.0%**. Add employer INCES **2.0%** (on total payroll) for a combined employer parafiscal load of **15.0%–17.0%** before LOPCYMAT. Tie out.

> **Ceiling distortion (flag).** The IVSS (5 min salaries) and Paro Forzoso (10 min salaries) ceilings are denominated in **minimum salaries**. Because the legal minimum wage is frozen at **VES 130/month**, these caps are economically trivial: IVSS ceiling ≈ 5 × 130 = **VES 650/mo**, Paro ceiling ≈ 10 × 130 = **VES 1,300/mo**. This is a known statutory distortion — apply the caps as written and FLAG.

> **IVSS "restructured Feb 2025" framing is unconfirmed.** Secondary EOR sources (CloudPay, Rivermate, Playroll) assert a Feb-2025 IVSS restructuring, but the **rate values** (4% employee / 9–11% employer) are confirmed by PwC. `[RESEARCH GAP — reviewer to confirm]` the primary IVSS Providencia behind any 2025 change; the rate values themselves are sound.

## Section 5 -- Minimum Wage & the "Ingreso Mínimo Integral" reality

**Minimum Wage & IMI table**

| Item | Amount | Notes | Source |
| --- | --- | --- | --- |
| Legal minimum wage (salario mínimo) | **VES 130/month**, frozen since **March 2022** | ≈ US$0.50–1/month at the official BCV rate in 2025; this is the figure feeding the IVSS/Paro ceilings | PwC (other taxes, "VES 130 as of 15 March 2022"); WageIndicator — `[RESEARCH GAP — reviewer to confirm 2025 BCV/Gaceta minimum wage]` |
| Ingreso Mínimo Integral (IMI) | **US$240/month** (30 April 2026, presidential announcement) | Comprehensive minimum income — mandatory for private sector | Guacamaya |
| — Bono de Guerra Económica | **US$200** (up from US$120) | **Non-salary** bonus — mandatory for private sector | Guacamaya |
| — Cestaticket (food voucher) | **US$40** | **Non-salary** bonus | Guacamaya |

> **Critical payroll point.** The Bono de Guerra Económica and Cestaticket are explicitly **"bonos de carácter no salarial"** — they do **NOT** count toward pensions, prestaciones sociales (severance), social-security contributions, vacation pay, or the ISLR salary base. Therefore IVSS/Paro/FAOV contributions **and** ISLR withholding are computed on the tiny **VES 130** base salary (or contractual base), NOT on the USD bonuses (Guacamaya).

## Section 6 -- Conservative Defaults

When an input is missing or ambiguous, apply the **conservative** assumption (the one that does NOT understate withholding/contributions) and FLAG it for the reviewer.

**Conservative defaults table**

| Unknown | Conservative default | Why |
| --- | --- | --- |
| UT value to apply | **VES 43.00** (SNAT/2025/0048, eff. 2 Jun 2025) | Current; any earlier value invalidates ISLR |
| Company IVSS risk class | Use **9% employer** (min class) for cost, but FLAG range to 11% | Avoids over-stating employer cost while flagging |
| Whether a payment is salary or bonus | Treat USD Bono de Guerra / Cestaticket as **non-salary** (excluded from base) | Statutory characterization |
| Whether ISLR withholding applies | Withhold only if estimated net annual enrichment **≥ 1,000 UT (VES 43,000)** | PwC threshold |
| Desgravamen | Apply **774 UT** standard deduction unless itemizing is substantiated | Simpler, statutory default |
| Dependents / rebaja | Apply **10 UT** taxpayer credit only; add dependents only if registered in SENIAT | Credit requires registration |
| LOPCYMAT rate | **0%** | Confirmed 0 per accountant review |
| Tax year | Default to **2025** unless the period is clearly another year | Skill tax_year is 2025 |
| Currency | Bolívar (VES) for the salary base; USD only for non-salary bonuses | Wages denominated in VES |

## Section 7 -- Required Inputs + Refusal Catalogue

### Required inputs before computing payroll

- **Required inputs list** — 1. Base monthly salary in bolívares (VES) — the contractual salary, separate from USD bonuses. 2. Any non-salary USD bonuses paid (Bono de Guerra Económica, Cestaticket) — for disclosure only. 3. Company IVSS risk class (min/medium/max → 9% / 10% / 11% employer). 4. Form AR-I withholding percentage (or the data to estimate it: annual income, desgravamen, dependents). 5. Tax/fiscal year and the UT value in force (VES 43.00 for 2025 from 2 Jun 2025). 6. Whether any payment is settled in foreign currency / crypto (IGTF 3% relevance — Section 14). 7. LOPCYMAT/INPSASEL risk registration (for employer safety contribution), where available.

### Refusal catalogue — DO NOT compute, refuse and request input

**Refusal catalogue table**

| Situation | Action |
| --- | --- |
| No base salary in VES provided | REFUSE — request the bolívar base salary |
| Only a USD total given, with no split between salary and non-salary bonuses | REFUSE — request the salary/non-salary split; bases differ |
| UT value unknown or a stale UT (e.g. VES 9) supplied for a 2025 computation | REFUSE — confirm VES 43.00 (SNAT/2025/0048) before any ISLR figure |
| Request to treat the USD Bono de Guerra / Cestaticket as salary to inflate the base | REFUSE — they are statutorily non-salary; flag |
| Request to omit IVSS/FAOV/ISLR "to save money" | REFUSE — these are statutory; escalate to accountant |
| Self-employed / fees / rental / professional-services income mixed in | REFUSE payroll path — route to a Venezuela income-tax skill |
| Definitive "this is your exact tax" assertion requested | REFUSE — outputs are estimates pending accountant sign-off |

## Section 8 -- Transaction / Payment Pattern Library (deterministic)

Classify bank-statement lines deterministically. Match case-insensitively; longest/most-specific pattern wins. Venezuelan statements mix Spanish payroll terms with USD-bonus references.

### Salary / bonus credits (money arriving in an employee account)

**Salary/bonus credit patterns table**

| Pattern (case-insensitive) | Classification |
| --- | --- |
| `SALARIO`, `SUELDO`, `NOMINA`, `PAGO QUINCENA`, `PAGO NOMINA` | Net salary payment (salary base) |
| `ABONO SALARIO`, `TRANSF.* [empresa]` | Net salary payment |
| `BONO GUERRA`, `BONO DE GUERRA`, `GUERRA ECONOMICA` | Bono de Guerra Económica (NON-salary, USD-indexed) |
| `CESTATICKET`, `CESTA TICKET`, `ALIMENTACION` | Cestaticket food voucher (NON-salary) |
| `UTILIDADES`, `AGUINALDO`, `BONO FIN DE AÑO` | Profit-sharing / year-end bonus (INCES employee base) |
| `REINTEGRO IVSS`, `DEVOLUCION IVSS` | IVSS refund/adjustment — not income |

### Employer debits (money leaving the employer account)

**Employer debits patterns table**

| Pattern | Classification |
| --- | --- |
| `SENIAT`, `RETENCION ISLR`, `ISLR NOMINA`, `PLANILLA ISLR` | ISLR withholding remitted to SENIAT (liability settlement) |
| `IVSS`, `SEGURO SOCIAL`, `TIUNA` | IVSS contribution (employer + employee portions) |
| `PARO FORZOSO`, `REGIMEN PRESTACIONAL EMPLEO`, `RPE` | Paro Forzoso / employment-benefit contribution |
| `FAOV`, `BANAVIH`, `VIVIENDA Y HABITAT` | FAOV housing fund |
| `INCES` | INCES 2% training levy |
| `LOPCYMAT`, `INPSASEL` | Workplace-safety contribution |
| `IGTF`, `IMPUESTO GRANDES TRANSACCIONES` | 3% tax on foreign-currency/crypto payments (Section 14) |
| `PAGO NOMINA`, `DISPERSION NOMINA` | Net wages disbursed to employees |

## Section 9 -- Worked Examples

> All figures use the **2025** ISLR tariff and **UT = VES 43.00**. The desgravamen único (774 UT = VES 33,282) and 10 UT (VES 430) personal credit are applied where ISLR arises. Social-security contributions are computed on the **salary base only** (USD non-salary bonuses excluded). Amounts rounded to the cent. These are illustrative bolívar salary bases chosen to exercise the mechanics; real frozen-minimum-wage workers fall below the ISLR threshold.

### Example 1 — Frozen minimum-wage worker (typical real case)

**Inputs:** Salary base VES 130/month → annual base VES 1,560. Plus US$200 Bono de Guerra and US$40 Cestaticket (non-salary). IVSS min risk class.

- Annual salary base VES 1,560 → in UT = 1,560 ÷ 43 = **36.3 UT** ≪ 1,000 UT threshold → **ISLR = VES 0.00**.
- IVSS employee 4% × 130 = **VES 5.20**; Paro 0.5% × 130 = **VES 0.65**; FAOV 1% × 130 = **VES 1.30**.
- **Employee deductions** = 5.20 + 0.65 + 1.30 = **VES 7.15**.
- **Net salary (VES)** = 130.00 − 7.15 = **VES 122.85**, plus US$240 non-salary bonuses paid separately.

*Bank lines:* `PAGO NOMINA` credit **VES 122.85**; `BONO DE GUERRA` credit **US$200**; `CESTATICKET` credit **US$40**.

### Example 2 — Salary base below the ISLR threshold but above min wage

**Inputs:** Salary base VES 3,000/month → annual base VES 36,000. IVSS min risk class.

- Annual base VES 36,000 → in UT = 36,000 ÷ 43 = **837.2 UT** < 1,000 UT (VES 43,000) → **ISLR = VES 0.00** (no withholding).
- IVSS 4% × 3,000 = **VES 120.00**; Paro 0.5% × 3,000 = **VES 15.00**; FAOV 1% × 3,000 = **VES 30.00**.
- **Employee deductions** = 120.00 + 15.00 + 30.00 = **VES 165.00**.
- **Net salary** = 3,000.00 − 165.00 = **VES 2,835.00**.

> Note: the IVSS ceiling (≈5 × 130 = VES 650/mo) is below this salary, so strictly IVSS/Paro would be capped at the ceiling base. This example applies the rate to full salary for mechanical clarity; in production apply `min(salary, ceiling)` and FLAG the distortion (Section 4).

### Example 3 — Salary base crossing the ISLR threshold (6% band)

**Inputs:** Salary base VES 6,000/month → annual base VES 72,000. Standard desgravamen 774 UT.

- Annual base VES 72,000 → in UT = 72,000 ÷ 43 = **1,674.42 UT**.
- Less desgravamen único 774 UT → taxable enrichment = 1,674.42 − 774 = **900.42 UT** < 1,000 UT → falls in the **6% band**.
- Gross tariff tax = 900.42 × 0.06 − 0 = **54.025 UT**.
- Less personal credit (rebaja) 10 UT → 54.025 − 10 = **44.025 UT**.
- ISLR (VES) = 44.025 × 43 = **VES 1,893.08/year** → monthly ≈ 1,893.08 ÷ 12 = **VES 157.76**.
- IVSS 4% × 6,000 = 240.00; Paro 0.5% × 6,000 = 30.00; FAOV 1% × 6,000 = 60.00 → social = **VES 330.00**.
- **Employee deductions/month** = 157.76 + 330.00 = **VES 487.76**.
- **Net salary** = 6,000.00 − 487.76 = **VES 5,512.24**.

### Example 4 — Higher salary base (9% band, dependents)

**Inputs:** Salary base VES 9,000/month → annual base VES 108,000. Desgravamen 774 UT. One dependent (+10 UT credit, total rebaja 20 UT).

- Annual base VES 108,000 → in UT = 108,000 ÷ 43 = **2,511.63 UT**.
- Less desgravamen 774 UT → taxable = 2,511.63 − 774 = **1,737.63 UT** (falls in the **12% band**, 1,500–2,000, subtract 75).
- Gross tariff tax = 1,737.63 × 0.12 − 75 = 208.5153 − 75 = **133.5153 UT**.
- Less rebaja 20 UT (taxpayer 10 + dependent 10) → 133.5153 − 20 = **113.5153 UT**.
- ISLR (VES) = 113.5153 × 43 = **VES 4,881.16/year** → monthly ≈ 4,881.16 ÷ 12 = **VES 406.76**.
- IVSS 4% × 9,000 = 360.00; Paro 0.5% × 9,000 = 45.00; FAOV 1% × 9,000 = 90.00 → social = **VES 495.00**.
- **Employee deductions/month** = 406.76 + 495.00 = **VES 901.76**.
- **Net salary** = 9,000.00 − 901.76 = **VES 8,098.24**.

### Example 5 — Employer total cost of the Example 3 worker (salary base VES 6,000/month)

**Employer total cost table**

| Employer cost item | Computation | Amount (VES) |
| --- | --- | --- |
| Salary base | — | 6,000.00 |
| IVSS employer 9% | 9% × 6,000 | 540.00 |
| Paro Forzoso employer 2% | 2% × 6,000 | 120.00 |
| FAOV employer 2% | 2% × 6,000 | 120.00 |
| INCES employer 2% | 2% × 6,000 | 120.00 |
| **Total employer cost (ex-LOPCYMAT)** | sum | **6,900.00** |

IVSS minimum risk class (9% employer). LOPCYMAT excluded (risk-dependent, see flag).

*Check:* 6,000 + 540 + 120 + 120 + 120 = **6,900.00**. Employer-on-top burden = VES 900.00 = **15.0%** of base (IVSS 9% + Paro 2% + FAOV 2% + INCES 2%). Tie out. LOPCYMAT confirmed 0% — no additional amount.

### Example 6 — Non-resident professional-services payment

**Inputs:** Non-resident paid VES 50,000 for professional services.

- Withholding base = 90% × 50,000 = **VES 45,000**.
- ISLR withheld = 34% × 45,000 = **VES 15,300** (PwC — flat 34% on 90% of gross for non-resident professional services).
- **Net to non-resident** = 50,000.00 − 15,300.00 = **VES 34,700.00**.

## Section 10 -- Tier 1 Rules (hard, non-negotiable)

- **Tier 1 hard rules** — 1. Use **UT = VES 43.00** (SNAT/2025/0048) for all 2025 ISLR computations; never a stale UT. 2. Compute ISLR on the **salary base in UT**, apply the Art. 50 tariff via the subtraction method, then convert at VES 43. 3. Withhold ISLR only when estimated **net annual enrichment ≥ 1,000 UT (VES 43,000)** (PwC). 4. The USD **Bono de Guerra Económica and Cestaticket are non-salary** — exclude them from the ISLR and contribution bases (Guacamaya). 5. IVSS employee **4%**, FAOV employee **1%**, Paro employee **0.5%**; employer IVSS **9%/10%/11%** by risk class, Paro **2%**, FAOV **2%**, INCES **2%** (PwC). 6. Apply the IVSS (5 min salaries) and Paro (10 min salaries) ceilings as written, using the **VES 130** frozen minimum wage, and FLAG the distortion. 7. Form **AR-I** (employee→employer) sets the withholding %; Form **AR-C/ARC** (employer→employee) is the year-end retention certificate. 8. The annual ISLR return for natural persons is due **31 March** (installments 31 Mar / 21 Apr / 12 May) (Efecto Cocuyo). 9. Every output is an **estimate** pending licensed-accountant sign-off.

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue table**

| Question | Why it needs a reviewer |
| --- | --- |
| IVSS Feb-2025 "restructuring" | Asserted by EOR secondary sources only; primary Providencia not located |
| LOPCYMAT rate | Confirmed 0% per accountant review |
| 2025 official minimum wage confirmation | PwC date is 15 Mar 2022; primary BCV/Gaceta 2025 confirmation not retrieved |
| Exact monthly withholding remittance calendar | Depends on the SENIAT withholding Providencia and special-taxpayer calendar |
| Deductibility/ordering of IVSS/FAOV against the ISLR base | Not cleanly confirmed against LISR |
| INCES employee 0.5% base (utilidades) timing | Annual bonus base vs monthly — confirm period |
| Net wealth tax / IGTF interaction with USD payroll settlement | Confirm IGTF applies to specific salary-settlement flows |

## Section 12 -- Excel Working Paper Template

**Excel Working Paper Template columns**  _(input)_

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | Salary base (VES/month) | input (excludes USD bonuses) |
| C | Annual salary base | `=B*12` |
| D | Annual base in UT | `=C/$UT` |
| E | Desgravamen (UT) | `774` (or itemized if substantiated) |
| F | Taxable enrichment (UT) | `=MAX(0, D-E)` |
| G | Gross tariff tax (UT) | nested IF on F using Art. 50 subtraction constants |
| H | Rebaja (UT) | `=10 + 10*dependents` |
| I | ISLR annual (UT) | `=MAX(0, G-H)` |
| J | ISLR annual (VES) | `=I*$UT` |
| K | ISLR monthly (VES) | `=IF(D>=1000, J/12, 0)` |
| L | IVSS employee | `=B*4%` |
| M | Paro employee | `=B*0.5%` |
| N | FAOV employee | `=B*1%` |
| O | Employee deductions | `=K+L+M+N` |
| P | Net salary | `=B-O` |
| Q | Employer IVSS (risk class) | `=B*risk%` (9/10/11%) |
| R | Employer Paro+FAOV+INCES | `=B*(2%+2%+2%)` |
| S | Total employer cost (ex-LOPCYMAT) | `=B+Q+R` |

- **ISLR formula for column G (UT, Art. 50 2025)** — =IF(F<=1000,F*0.06, IF(F<=1500,F*0.09-30, IF(F<=2000,F*0.12-75, IF(F<=2500,F*0.16-155, IF(F<=3000,F*0.20-255, IF(F<=4000,F*0.24-375, IF(F<=6000,F*0.29-575, F*0.34-875)))))))  _(Art. 50 2025)_

Apply IVSS/Paro caps (`min(B, ceiling)`) in production; omitted above for clarity and FLAGGED.

## Section 13 -- Bank Statement / Terminology Reading Guide

**Bank Statement / Terminology Reading Guide**

| Spanish term | English / meaning |
| --- | --- |
| Nómina | Payroll / payroll run |
| Salario / Sueldo | Salary / wage |
| Quincena | Bi-weekly (fortnightly) pay period |
| Retención ISLR | Income-tax withholding |
| Unidad Tributaria (UT) | Tax Unit (VES 43.00 in 2025) |
| Desgravamen único | Standard deduction (774 UT) |
| Rebaja personal | Personal tax credit (10 UT) |
| Enriquecimiento neto | Net enrichment (taxable income) |
| Bono de Guerra Económica | Economic War Bonus (US$200, non-salary) |
| Cestaticket | Food voucher (US$40, non-salary) |
| Utilidades / Aguinaldo | Profit-sharing / year-end bonus |
| IVSS | Venezuelan Social Security Institute |
| Paro Forzoso | Forced-unemployment (employment-benefit) regime |
| FAOV / BANAVIH | Housing savings fund / housing bank |
| INCES | Vocational-training levy |
| LOPCYMAT / INPSASEL | Workplace health & safety law / institute |
| Comprobante de retención (AR-C/ARC) | Withholding certificate |
| IGTF | Tax on Large Financial Transactions (3% on FX/crypto) |
| Salario mínimo | Minimum wage (VES 130/month) |

## Section 14 -- Other Taxes Touching Payroll / Individuals

**Other Taxes Touching Payroll / Individuals**  _(Source: PwC Worldwide Tax Summaries — Venezuela (other taxes, last reviewed 12 Jan 2026).)_

| Tax | Detail |
| --- | --- |
| Tax on Large Financial Transactions (IGTF) | **3%** on payments made in **foreign currency or crypto** through the financial system — relevant where employers pay/settle salaries or bonuses in USD |
| Net Wealth Tax | **0.25%/year** on net worth **≥ 150,000,000 UT** |

## Section 15 -- Onboarding Fallback

If the engagement lacks key data:

1. **No prior nómina available** → request the last 3 months of payroll registers plus IVSS/FAOV/SENIAT receipts to back-solve the rates and bases actually applied.
2. **UT value uncertain** → confirm VES 43.00 against SNAT/2025/0048 (Gaceta 43,140) before any ISLR figure; treat any VES 9 reference as stale (pre-2 Jun 2025).
3. **Salary vs bonus split unknown** → request the contract; default the USD Bono de Guerra / Cestaticket to **non-salary** (excluded from base), FLAG.
4. **IVSS risk class unknown** → default employer 9% (min class), FLAG range to 11%.
5. **LOPCYMAT registration unknown** → do not quantify; FLAG the 0.75%–10% band pending INPSASEL data.
6. **Year ambiguity** → default to the 2025 UT and tariff.

## Section 16 -- Filing, Forms & Deadlines

**Filing, Forms & Deadlines**  _(PwC; Efecto Cocuyo; El Diario; Forvis Mazars / Moore; Nayma Consultores)_

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year ending 31 Dec | PwC |
| Annual ISLR return (natural persons) | Due **31 March**; installment option 3 payments — **31 Mar / 21 Apr / 12 May** | Efecto Cocuyo; El Diario |
| Who must file | Net enrichment **> 1,000 UT** OR gross income **> 1,500 UT**; requires active **RIF** + SENIAT portal registration | Efecto Cocuyo |
| Employer monthly ISLR remittance | Per the SENIAT withholding Providencia / special-taxpayer calendar | Forvis Mazars / Moore retention tables — `[RESEARCH GAP — reviewer to confirm exact monthly dates]` |
| Form AR-I | Employee files to employer before the first payment of the year | Nayma Consultores |
| Form AR-C (ARC) | Employer issues to employee for the prior year | Nayma Consultores |

## Section 17 -- Penalties (Código Orgánico Tributario — COT)

The **2020 COT reform** re-denominated many penalties from UT to the **official BCV exchange rate (highest published)** rather than UT. Source: Grant Thornton Venezuela COT table; Galac; MPPEF.

**Penalties (COT)**  _(Grant Thornton)_

| Item | Detail | Source |
| --- | --- | --- |
| Omitted income / underpayment | Fine **100% to 300%** of the omitted tax | Grant Thornton |
| Failure to file a return | **10-day closure** of the establishment **+ fine of 150× the highest official BCV rate** | Grant Thornton |
| Incomplete return / late by ≤ 1 year | Fine **100× the highest BCV rate** | Grant Thornton |
| Late payment (enteramiento tardío) within 1 year | **0.28% of amount owed per day of delay, capped at 100%** | Grant Thornton; Galac |
| Late payment after 1 year | Additional **50%** of amount owed | Grant Thornton |
| Late payment after 2 years | Additional **150%** of amount owed | Grant Thornton |
| Special taxpayers (contribuyentes especiales) | Formal-duty penalties increased by **200%** | Grant Thornton |

## Section 18 -- Summary Employer/Employee Burden (2025, salary-based regimes)

**Summary Employer/Employee Burden (2025, salary-based regimes)**

| Contribution | Employee | Employer | Base/cap |
| --- | --- | --- | --- |
| ISLR | 6–34% progressive (in UT) | (withholding agent) | net enrichment, threshold 1,000 UT |
| IVSS | 4% | 9% / 10% / 11% (risk class) | up to 5 min salaries (≈VES 650/mo) |
| Paro Forzoso | 0.5% | 2% | up to 10 min salaries (≈VES 1,300/mo) |
| FAOV | 1% | 2% | up to 10 min salaries |
| INCES | 0.5% (on utilidades) | 2% (on total payroll) | bonus base (ee) / total wages (er) |
| LOPCYMAT | — | 0% | confirmed 0 |
| **Salary-based total (ee 5.5% / er 13–15%)** | **5.5%** | **13.0%–15.0%** | excludes INCES & LOPCYMAT |

*Check:* employee 4 + 0.5 + 1 = **5.5%**; employer min 9 + 2 + 2 = **13.0%**, max 11 + 2 + 2 = **15.0%**. Tie out.

## Section 19 -- Reference Material

**Reference Material**

| Topic | Figure | Source |
| --- | --- | --- |
| UT value 2025 | VES 43.00 (eff. 2 Jun 2025) | SNAT/2025/0048, Gaceta 43,140; Moore retention table |
| ISLR tariff | 6%–34%, Art. 50 LISR | PwC |
| Desgravamen único | 774 UT (VES 33,282) | PwC; Nayma Consultores |
| Personal credit (rebaja) | 10 UT | PwC |
| Withholding threshold | 1,000 UT (VES 43,000) | PwC; Nayma Consultores |
| Non-resident WHT | 34% on 90% of gross (professional services) | PwC |
| IVSS | 4% ee / 9–11% er | PwC; CloudPay; Rivermate |
| Paro Forzoso | 0.5% ee / 2% er | PwC |
| FAOV | 1% ee / 2% er | PwC; CloudPay |
| INCES | 0.5% ee (utilidades) / 2% er (payroll) | PwC |
| LOPCYMAT | 0% er | PwC |
| Minimum wage | VES 130/month (frozen Mar 2022) | PwC; WageIndicator |
| Ingreso Mínimo Integral | US$240 (US$200 bono + US$40 cestaticket), non-salary | Guacamaya |
| Annual ISLR deadline | 31 March (installments 31 Mar / 21 Apr / 12 May) | Efecto Cocuyo; El Diario |
| IGTF | 3% on FX/crypto payments | PwC |
| Net wealth tax | 0.25% on net worth ≥ 150,000,000 UT | PwC |
| COT penalties | 100–300% omission; BCV-rate-denominated | Grant Thornton |

Key authorities: SENIAT (`seniat.gob.ve`), IVSS, BANAVIH/FAOV, INCES, INPSASEL, BCV. Big-4/secondary: PwC Worldwide Tax Summaries, Grant Thornton Venezuela, Moore/Forvis Mazars (retention tables), Efecto Cocuyo, El Diario, Nayma Consultores, Guacamaya, CloudPay, Rivermate, lega.law.

## Section 20 -- Test Suite

Each test recomputes end-to-end. Expected values use the 2025 Art. 50 tariff and UT = VES 43.00.

1. **Frozen min-wage worker.** Salary base VES 130/mo. Annual base 1,560 → 36.3 UT < 1,000 UT → ISLR **VES 0.00**; employee social = 4%+0.5%+1% × 130 = **VES 7.15**; net **VES 122.85**.
2. **Below threshold.** Salary base VES 3,000/mo. Annual base 36,000 → 837.2 UT < 1,000 UT → ISLR **VES 0.00**; employee social **VES 165.00**; net **VES 2,835.00**.
3. **6% band.** Salary base VES 6,000/mo, desgravamen 774 UT, rebaja 10 UT. Taxable **900.42 UT**; ISLR annual **VES 1,893.08**, monthly **VES 157.76**; net **VES 5,512.24**.
4. **12% band, 1 dependent.** Salary base VES 9,000/mo, desgravamen 774, rebaja 20 UT. Taxable **1,737.63 UT**; ISLR annual **VES 4,881.16**, monthly **VES 406.76**; net **VES 8,098.24**.
5. **Employer cost.** Salary base VES 6,000/mo, IVSS 9% class. Total employer cost (ex-LOPCYMAT) **VES 6,900.00** (burden 15.0% of base).
6. **Non-resident services.** VES 50,000 fee → 34% × (90% × 50,000) = **VES 15,300** withheld; net **VES 34,700.00**.
7. **Bracket continuity.** Cumulative ISLR at 1,000 UT = 60; at 2,000 UT = 165; at 4,000 UT = 585; at 6,000 UT = 1,165 (subtraction constants tie out — Section 2).
8. **Non-salary exclusion.** US$200 Bono de Guerra + US$40 Cestaticket → excluded from ISLR and contribution bases; contribution base stays at the VES salary only.
9. **Stale-UT refusal.** ISLR requested with UT = VES 9 for a 2025 period → REFUSE; require VES 43.00.
10. **Currency split refusal.** Only a USD total provided with no salary/non-salary split → REFUSE and request the split.

## PROHIBITIONS

- **Stale UT prohibition** — NEVER use a stale Unidad Tributaria — 2025 ISLR uses VES 43.00 (SNAT/2025/0048), not VES 9.  _(SNAT/2025/0048)_
- **Non-salary bonus treatment** — NEVER treat the USD Bono de Guerra Económica or Cestaticket as salary — they are statutorily non-salary.
- **Non-salary bonuses excluded from bases** — NEVER include the USD non-salary bonuses in the IVSS/Paro/FAOV/ISLR base.
- **Below-threshold withholding** — NEVER withhold ISLR where estimated net annual enrichment is below 1,000 UT (VES 43,000).
- **Statutory contributions completeness** — NEVER omit the statutory contributions: IVSS, Paro Forzoso, FAOV, INCES.
- **LOPCYMAT employer rate** — LOPCYMAT employer rate is confirmed at 0%.
- **IVSS restructuring framing** — NEVER present the IVSS "Feb-2025 restructuring" framing as confirmed — only the rate values are sourced.
- **Monthly ISLR remittance date** — NEVER state an exact monthly ISLR remittance date without the SENIAT withholding calendar — it is a research gap.
- **IGTF applicability** — NEVER ignore the 3% IGTF where salaries or bonuses are settled in foreign currency or crypto.
- **Definitive computations prohibition** — NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Venezuelan contador público.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed contador público colegiado in Venezuela) before implementation.

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
