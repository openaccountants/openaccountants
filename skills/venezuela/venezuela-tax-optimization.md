---
name: venezuela-tax-optimization
description: Use this skill whenever asked about reducing tax in Venezuela, tax planning, saving tax, optimizing tax, allowances, deductions the client might be missing, or any question about legal strategies to minimize income tax liability for individuals or companies in Venezuela. Trigger on phrases like "reduce tax", "tax planning", "save tax", "optimize", "allowances", "deductions I'm missing", "pay less tax", "tax-efficient", "tax minimization", "how to lower my tax bill", "ISLR planning", "IVA optimization", "SENIAT", "unidad tributaria". ALWAYS read this skill before advising on any Venezuela tax optimization strategy.
jurisdiction: VE
tax_year: 2025
last_updated: 2026-07-13
authored_by: Jose Padilla, CPA
reviewed_by: Jose Padilla
review_status: current
trust_label: Checked by Jose Padilla
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Venezuela Tax Optimization

## Venezuela Tax Optimization Skill v0.1

> HYPERINFLATIONARY JURISDICTION — CRITICAL PROTOCOL
>
> All monetary thresholds and bracket boundaries in Venezuelan law are expressed
> in Tax Units (Unidades Tributarias / UT). Before quoting ANY bolivar (Bs./VES)
> figure to a client, confirm the current UT value with SENIAT. The value as of
> June 2, 2025 is **Bs. 43.00** (SNAT/2025/000048, Gaceta Oficial No. 43,140).
> This value was raised 377.8% from the previous Bs. 9.00 set in May 2023, and
> may change again at any time. All bolivar amounts in this skill use the 2025
> UT of Bs. 43.00 as a reference only.
>
> Penalties under the Código Orgánico Tributario (COT) 2020 reform are expressed
> in **USD at the BCV official rate**, NOT in UT. Confirm the BCV rate on the
> day of the computation.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Jose Padilla** on 2026-06-21.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### venezuela-tax-optimization

- **Valor de la Unidad Tributaria (UT) — 2025** — Bs. 43.00  _(SNAT/2025/000048, Gaceta Oficial No. 43,140)_
- **Valor de la Unidad Tributaria (UT) — anterior (mayo 2023)** — Bs. 9.00  _(SNAT/2025/000048)_
- **UT value increase from 2023 to 2025** — 377.8%  _(SNAT/2025/000048)_
- **Fecha límite para la declaración anual del ISLR de personas naturales** — 31 de marzo del año siguiente
- **Umbral de declaración del ISLR para personas naturales** — Renta neta anual ≥ 1,000 UT (= Bs. 43,000 a la UT de 2025)
- **Fecha límite para la declaración del IVA** — Día 15 del mes siguiente (mensual)
- **Ejercicio fiscal venezolano** — Año calendario: 1 Jan – 31 Dec  _(PwC — Venezuela individual)_
- **Desgravamen único (standard personal deduction)** — 774 UT per year (= Bs. 33,282 at 2025 UT)  _(ISLR Law Art. 60 and 61)_
- **Desgravamen detallado — educación (contribuyente + dependientes menores de 26 años)** — Sin límite  _(ISLR Law Art. 60 and 61)_
- **Desgravamen detallado — primas de seguros de vida/cirugía/hospitalización/maternidad** — Sin límite  _(ISLR Law Art. 60 and 61)_
- **Desgravamen detallado — gastos médicos/odontológicos/de hospitalización** — Sin límite  _(ISLR Law Art. 60 and 61)_
- **Desgravamen detallado — intereses hipotecarios sobre vivienda principal (límite anual)** — 1,000 UT = Bs. 43,000 a la UT de 2025  _(ISLR Law Art. 60 and 61)_
- **Desgravamen detallado — alquiler de vivienda principal (límite anual)** — 800 UT = Bs. 34,400 a la UT de 2025  _(ISLR Law Art. 60 and 61)_
- **Período de arrastre de pérdidas comerciales/operativas** — Máximo 3 años  _(ISLR Law)_
- **Límite anual de aplicación del arrastre de pérdidas** — 25% de la renta gravable de ese año  _(ISLR Law)_
- **Arrastre retroactivo de pérdidas** — No permitido  _(ISLR Law)_
- **Regla de compensación de pérdidas de fuente extranjera** — Solo puede compensarse con rentas de fuente extranjera  _(Ley del ISLR)_
- **Pérdidas por corrección monetaria (ajuste por inflación) — arrastre** — No pueden arrastrarse en absoluto; expiran en el ejercicio en que se generan  _(Ley del ISLR)_
- **Banda 1: 0–1,000 UT** — 6%; Fixed deduction: 0 UT / Bs. 0  _(Ley del ISLR)_
- **Banda 2: 1,000–1,500 UT** — 9%; Fixed deduction: 30 UT / Bs. 1,290  _(Ley del ISLR)_
- **Banda 3: 1,500–2,000 UT** — 12%; Fixed deduction: 75 UT / Bs. 3,225  _(Ley del ISLR)_
- **Banda 4: 2,000–2,500 UT** — 16%; Fixed deduction: 155 UT / Bs. 6,665  _(Ley del ISLR)_
- **Banda 5: 2,500–3,000 UT** — 20%; Fixed deduction: 255 UT / Bs. 10,965  _(Ley del ISLR)_
- **Banda 6: 3,000–4,000 UT** — 24%; Fixed deduction: 375 UT / Bs. 16,125  _(Ley del ISLR)_
- **Banda 7: 4,000–6,000 UT** — 29%; Deducción fija: 575 UT / Bs. 24,725  _(Ley del ISLR)_
- **Banda 8: Más de 6,000 UT** — 34%; Deducción fija: 875 UT / Bs. 37,625  _(Ley del ISLR)_
- **Fórmula del impuesto** — Impuesto = (Renta × Tasa%) − Deducción Fija (en Bs.)  _(Ley del ISLR)_
- **Banda 1: 0–2,000 UT (corporate)** — 15%; Deducción fija: 0 UT / Bs. 0  _(Ley del ISLR)_
- **Banda 2: 2,000–3,000 UT (corporate)** — 22%; Deducción fija: 140 UT / Bs. 6,020  _(Ley del ISLR)_
- **Banda 3: Más de 3,000 UT (corporate)** — 34%; Deducción fija: 500 UT / Bs. 21,500  _(Ley del ISLR)_
- **Tasa fija especial: explotación petrolera** — 50%  _(PwC — Venezuela, Corporate, Taxes on corporate income)_
- **Tasa fija especial: bancos / entidades financieras / seguros** — 40%  _(PwC — Venezuela, Corporate, Taxes on corporate income)_
- **Tasa de retención en la fuente sobre dividendos domésticos** — 34% fijo  _(Ley del ISLR)_
- **España — tasa de retención en la fuente sobre dividendos según convenio** — 0% para accionistas corporativos calificados; 10% para los demás
- **Estados Unidos — tasa de retención en la fuente sobre dividendos según convenio** — 5% para participaciones ≥10%; 15% en los demás casos
- **México — tasa de retención en la fuente sobre dividendos según convenio** — 5%
- **Francia — tasa de retención en la fuente sobre dividendos según convenio** — 0% bajo ciertas condiciones; 15% en los demás casos
- **Canadá — tasa de retención en la fuente sobre dividendos según convenio** — 10% para participaciones ≥25%; 15% en los demás casos
- **Brasil — tasa de retención en la fuente sobre dividendos según convenio** — 10% para participaciones sustanciales; 15% en los demás casos
- **Número total de convenios tributarios vigentes (a enero de 2026)** — ~40 convenios  _(PwC Worldwide Tax Summaries — Venezuela Withholding Taxes (January 2026))_
- **Límite de la razón deuda-capital para subcapitalización** — 1:1 (la deuda con partes relacionadas no debe exceder el patrimonio)  _(ISLR Law Art. 38)_
- **Consecuencia de exceder el límite 1:1** — Los intereses sobre el exceso de deuda no son deducibles para el ISLR  _(ISLR Law Art. 38)_
- **Tasa LOCTI — bingos, casinos, alcohol, tabaco** — 2% de los ingresos brutos mensuales  _(LOCTI (Ley Orgánica de Ciencia, Tecnología e Innovación, April 2022))_
- **Tasa LOCTI — hidrocarburos o minería** — 1% de los ingresos brutos mensuales  _(LOCTI (April 2022))_
- **Tasa LOCTI — todas las demás actividades** — 0.5% de los ingresos brutos mensuales  _(LOCTI (April 2022))_
- **Tasa LOCTI — empresas de actividad múltiple** — La tasa más alta aplicable calculada sobre el total de ingresos brutos  _(LOCTI (April 2022))_
- **Exención LOCTI — sector petrolero (a partir de la Reforma de la Ley de Hidrocarburos de enero de 2026)** — Exento  _(Hydrocarbons Law Reform, January 29, 2026)_
- **Umbral de activación por ingresos brutos mensuales de la LOCTI** — Ingresos brutos mensuales que superen 150,000 veces la divisa extranjera de mayor valor publicada por el BCV  _(LOCTI (April 2022))_
- **Frecuencia de pago y sistema de la LOCTI** — Mensual a través del sistema SIDCAI  _(Administrative Ruling No. 015-004-2024, February 2024)_
- **Rango de tarifas del ISAE** — 1% al 6.5% de los ingresos brutos (varía según el municipio y la actividad)  _(Ley Orgánica del Poder Público Municipal)_
- **Base imponible mínima del ISAE** — 20 UT (= Bs. 860 a la UT 2025)  _(Ley Orgánica del Poder Público Municipal)_
- **Tasa estándar del IVA** — 16%  _(Ley de IVA)_
- **Tasa reducida del IVA** — 8% (caprinos, ovinos y otros menores; carnes refrigeradas; manteca vegetal; servicios profesionales a entes públicos; transporte aéreo nacional de pasajeros; ciertas construcciones)  _(Ley de IVA)_
- **Tasa del recargo por artículos de lujo** — +15% (efectivo total ~31%) sobre vehículos ≥ USD 40,000; motocicletas ≥ USD 20,000; joyas ≥ USD 300; servicios de restaurante/bar; máquinas de juego  _(Ley de IVA)_
- **Umbral del recargo por lujo — vehículos** — ≥ USD 40,000  _(Ley de IVA)_
- **Umbral del recargo por lujo — motocicletas** — ≥ USD 20,000  _(Ley de IVA)_
- **Umbral del recargo por lujo — joyas** — ≥ USD 300  _(Ley de IVA)_
- **IVA tasa cero** — Los servicios prestados en Venezuela para personas en el exterior se consideran prestados en Venezuela y por ende se les aplica el iva de 16%  _(Ley de IVA)_
- **Rango de la tasa del recargo por divisas / criptoactivos** — 5–25% sobre transacciones pagadas en moneda extranjera, criptomonedas o criptoactivos no venezolanos  _(Ley de IVA / IGTF)_
- **Exención del IVA sobre importaciones de alimentos básicos, medicamentos, fertilizantes, equipos médicos, libros y ciertos combustibles — estatus** — Suspendida a partir del 5 de julio de 2025  _(Presidential Decree No. 5,145, June 30, 2025)_
- **Exención del IVA para importaciones realizadas por organismos de la Administración Pública Nacional y entidades privadas designadas** — Exención por un año hasta el 30 de junio de 2026  _(Presidential Decree No. 5,146, June 30, 2025)_
- **IVSS (Social Security) — employer contribution rate (by risk class)** — 9% / 10% / 11%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **IVSS (Social Security) — employee contribution rate** — 4%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **Tope de la base salarial del IVSS** — 5 salarios mínimos
- **Fecha límite de pago del IVSS** — Antes del día 16 de cada mes
- **FAOV (Housing) — employer contribution rate** — 2%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **FAOV (Housing / Ley de Vivienda y Hábitat) — employee contribution rate** — 1%  _(PwC Worldwide Tax Summaries, reviewed 12 Jan 2026)_
- **Fecha límite de pago del FAOV** — Dentro de los primeros 5 días hábiles de cada mes
- **FAV (Vivienda — secundaria / LPH) tasa de contribución patronal** — 2% (base salarial tope: 10 salarios mínimos)
- **FAV (Vivienda — secundaria / LPH) tasa de contribución del trabajador** — 0.5% (base salarial tope: 10 salarios mínimos)
- **INCES — tasa de contribución patronal** — 2% del total de salarios  _(PwC Worldwide Tax Summaries, revisado el 12 Jan 2026)_
- **INCES (Capacitación laboral) — tasa de contribución del empleado** — 0.5% (sobre las utilidades de fin de año)  _(PwC Worldwide Tax Summaries, revisado el 12 Jan 2026)_
- **Fecha límite de pago del INCES** — Dentro de los primeros 5 días hábiles después del cierre de cada trimestre
- **Desempleo (Régimen Prestacional de Empleo) — tasa de contribución patronal** — 2%  _(PwC Worldwide Tax Summaries, revisado el 12 Jan 2026)_
- **Desempleo (Régimen Prestacional de Empleo) — tasa de contribución del empleado** — 0.5%  _(PwC Worldwide Tax Summaries, revisado el 12 Jan 2026)_
- **LOPCYMAT (Riesgo laboral) — tasa de contribución patronal** — 0  _(la lopcymat no pide pagos regulares solo establece sanciones por incumplimientos (multas))_
- **Contribución Especial de Pensión — tasa patronal (a partir de mayo de 2024)** — 9% (solo patronal)
- **ZEE Estado La Guaira — reintegro del ISLR** — Hasta el 100% durante los primeros 4 ejercicios fiscales  _(Decretos Presidenciales 4,838–4,841 (August 2023))_
- **ZEE Militar de Aragua — reintegro del ISLR** — Hasta el 100% durante los primeros 4 ejercicios fiscales  _(Decretos Presidenciales 4,838–4,841 (August 2023))_
- **ZEE Península de Paraguaná — reintegro del ISLR** — Hasta el 100% durante los primeros 4 ejercicios fiscales  _(Decretos Presidenciales 4,838–4,841 (August 2023))_
- **ZEE Isla Tortuga — reintegro del ISLR** — Hasta el 100% durante los primeros 20 ejercicios fiscales  _(Decretos Presidenciales 4,838–4,841 (August 2023))_
- **Requisito de exportación en ZEE (a partir del año 7)** — ≥ 60% de la producción exportada  _(Decretos Presidenciales 4,838–4,841 (August 2023))_
- **Reembolso de aranceles aduaneros en ZEE sobre insumos, materias primas y maquinaria importados** — 100%  _(Decretos Presidenciales 4,838–4,841 (August 2023))_
- **Fecha límite de publicación del tope de incentivos en ZEE** — Dentro de los 15 días hábiles siguientes al período de declaración del ISLR  _(Resolution 015-25)_
- **Certificación de elegibilidad en ZEE** — Se debe obtener la certificación conforme a la Resolution 015-25 (May 9, 2025)  _(Resolution 015-25)_
- **Denominación de sanciones del COT 2020** — USD al tipo de cambio oficial del BCV (NO en UT)  _(Código Orgánico Tributario (COT) reforma 2020, Art. 91)_
- **Prescripción del COT / período de conservación de documentos** — 5 años  _(Código Orgánico Tributario (COT))_
- **Fecha límite de pago de la cuota 1 del ISLR** — 31 March (junto con la declaración anual)
- **Fecha límite de pago de la cuota 2 del ISLR** — 20 días después de la fecha límite del March 31 (es decir, ~20 April)
- **Fecha límite de pago de la cuota 3 del ISLR** — 40 días después de la fecha límite del March 31 (es decir, ~10 May)
- **Doctrina de sustancia económica / base legal de precios de transferencia** — Art. 112–118 ISLR  _(Ley de ISLR (Decreto No. 1.435, Dec 2014))_
- **Umbral de ratio deuda-capital por defecto para subcapitalización** — 1:1 (cualquier deuda con partes relacionadas que supere este límite se trata como no deducible)  _(ISLR Law Art. 38)_
- **Ampliación de las obligaciones de retención del IVA — fecha de entrada en vigor de la resolución** — August 1, 2025  _(SNAT/2025/000054)_

## Section 1 — Quick Reference

**Section 1 — Quick Reference**

| Field | Value |
| --- | --- |
| Country | Bolivarian Republic of Venezuela |
| Key tax authority | SENIAT (Servicio Nacional Integrado de Administración Aduanera y Tributaria) |
| Key optimization legislation | Ley de ISLR (Decreto No. 1.435, Dec 2014) + Reglamento; COT 2020; Ley de IVA; LOCTI (Apr 2022) |
| Tax authority attitude to planning | SENIAT accepts legitimate planning within the ISLR Law. No codified general anti-avoidance rule (GAAR) in domestic law, but economic substance doctrine applied in transfer pricing (Art. 112–118 ISLR). Aggressive structures lacking commercial purpose are challenged. |
| Currency | Bolívar digital (Bs. / VES) |
| Unit of account for tax law | Tax Unit (UT) — value set annually by SENIAT administrative ruling. 2025 value: Bs. 43.00 |
| Tax year | Calendar year (1 Jan – 31 Dec) for most taxpayers |
| ISLR individual filing deadline | 31 March of the following year |
| ISLR individual filing threshold | Annual net income ≥ 1,000 UT (= Bs. 43,000 at 2025 UT) |
| VAT return deadline | 15th of the following month (monthly) |

## Section 2 — When to Use This Skill

Use this skill when the client:

- Is a Venezuelan-resident individual or company subject to ISLR
- Has Venezuelan-source income regardless of where they reside (territorial rules apply for non-residents)
- Is planning a dividend distribution from a Venezuelan entity
- Is structuring an inbound or outbound payment subject to Venezuelan withholding
- Asks about LOCTI, ISAE (municipal business tax), IVA structuring, or SEZ incentives
- Is in the hydrocarbons, banking, or insurance sector (special ISLR rates apply)
- Holds cryptocurrency with Venezuelan tax obligations
- Is planning to establish or relocate operations to a Venezuelan Special Economic Zone (SEZ)

Do NOT use this skill if the client's primary tax nexus is in another jurisdiction; in that case, use the relevant jurisdiction skill alongside this one for cross-border analysis.

## Section 3 — Conservative Defaults

When facts are uncertain, this skill defaults to the most conservative (highest-tax) reading unless the client explicitly provides documentation supporting a more favorable position:

1. **UT value**: Use the published SNAT/2025/000048 value of Bs. 43.00 but flag that the agent must verify the current value from SENIAT before quoting bolivar figures.
2. **Desgravamen**: Default to the standard 774 UT deduction unless the client can document itemized amounts exceed 774 UT.
3. **Dividend rate**: Default to 34% domestic rate unless a tax treaty is confirmed to apply and the holding structure qualifies under treaty anti-abuse provisions.
4. **Thin capitalization**: Default to treating any related-party debt exceeding a 1:1 debt-to-equity ratio as non-deductible.
5. **IGTF**: Default to assuming the tax applies at applicable rates until the client produces an Official Gazette decree confirming full elimination or their SENIAT-confirmed "special taxpayer" exemption.
6. **SEZ incentives**: Treat incentives as unavailable until the client produces Resolution 015-25 certification from the Ministry of Finance.
7. **Export drawback**: Per PwC (January 2026), the customs duty drawback program is "not currently being applied in practice." Do not rely on it in a planning scenario without current confirmation.

## Section 4 — Refusal Catalogue

**Refusal Catalogue**

| Scenario | Reason |
| --- | --- |
| Petroleum sector ISLR structuring (post-January 2026 Hydrocarbons Law Reform) | 180-day transition period ongoing; regime highly fact-specific; requires engagement with Ministry of Hydrocarbons |
| Transfer pricing documentation preparation | Requires functional analysis, benchmark study, and TP specialist sign-off |
| APAs (unilateral or bilateral) | Require SENIAT negotiation; outside automated skill scope |
| Suspected ISLR evasion or undeclared prior years | Regularization requires specialist; criminal exposure under COT Art. 119 |
| Cryptocurrency income with no booking records | Cannot compute ISLR without market-value records at receipt date; instruct client to reconstruct records first |
| Special taxpayer (sujeto pasivo especial) calendar compliance | Filing windows are taxpayer-specific under SNAT/2025/000091; do not compute deadlines without the client's specific calendar from SENIAT |
| Anti-drug, sports, or high-net-wealth (IMPAE) contribution calculations | These require verified accounting profit figures; do not estimate without audited financials |
| Mixed-company or PSA petroleum contracts | Highly negotiated; outside skill scope |

- **Petroleum sector ISLR structuring (post-January 2026 Hydrocarbons Law Reform)** — 180-day transition period ongoing; regime highly fact-specific; requires engagement with Ministry of Hydrocarbons
- **Transfer pricing documentation preparation** — Requires functional analysis, benchmark study, and TP specialist sign-off
- **APAs (unilateral or bilateral)** — Require SENIAT negotiation; outside automated skill scope
- **Suspected ISLR evasion or undeclared prior years** — Regularization requires specialist; criminal exposure under COT Art. 119
- **Cryptocurrency income with no booking records** — Cannot compute ISLR without market-value records at receipt date; instruct client to reconstruct records first
- **Special taxpayer (sujeto pasivo especial) calendar compliance** — Filing windows are taxpayer-specific under SNAT/2025/000091; do not compute deadlines without the client's specific calendar from SENIAT
- **Anti-drug, sports, or high-net-wealth (IMPAE) contribution calculations** — These require verified accounting profit figures; do not estimate without audited financials
- **Mixed-company or PSA petroleum contracts** — Highly negotiated; outside skill scope

## Section 5 — Major Optimization Lever 1: Desgravamen Único vs. Itemized Deductions

### Mechanism

- **Desgravamen único vs. itemized** — Venezuelan ISLR Law (Art. 60 and 61) allows individuals to deduct one of two mutually exclusive sets of personal deductions before applying Tarifa No. 1: - **Desgravamen único (standard):** 774 UT per year. No documentation required. - **Desgravamen detallado (itemized):** Sum of qualifying expenses actually paid to Venezuelan-domiciled entities.  _(ISLR Law Art. 60 and 61)_

### Itemized Deduction Categories and Limits

**Itemized Deduction Categories and Limits**

| Category | Annual Limit | Notes |
| --- | --- | --- |
| Education (taxpayer + dependents under 26) | No cap | All levels; must be paid to registered Venezuelan institutions |
| Life, surgery, hospitalization, maternity insurance premiums | No cap | Policy must be with Venezuelan-domiciled insurer |
| Medical, dental, and hospitalization expenses | No cap | Must be medically necessary; receipts required |
| Mortgage interest — primary residence | 1,000 UT = Bs. 43,000 | Only principal dwelling; Venezuelan lender |
| Rent — primary residence | 800 UT = Bs. 34,400 | Only principal dwelling; Venezuelan lessor |

### Eligibility

- **Eligibility for desgravamen** — Any individual resident filing under Tarifa No. 1. Non-residents are generally not entitled to these deductions.

### Quantified Savings

At the margin, each additional UT of deduction beyond the standard 774 UT saves tax at the marginal rate applicable to the individual's bracket.

Example: An individual in the 24% bracket (income 3,000–4,000 UT range) who itemizes Bs. 50,000 in qualifying expenses vs. using the 774 UT standard (= Bs. 33,282) gains an extra deduction of Bs. 16,718 (= ~389 UT), saving:

389 UT × 24% × Bs. 43 = approximately **Bs. 4,012 in ISLR savings** — but confirm exact UT value first.

### Decision Rule

- **Decision rule for itemizing** — Sum all qualifying itemized expenses. If the total exceeds Bs. 33,282 (774 UT × Bs. 43), itemize. Otherwise, use the standard deduction. This calculation must be performed fresh each year because the UT value changes.

### Source

PwC Worldwide Tax Summaries — Venezuela Individual, Deductions (reviewed January 2026). Lstributos.com (2025 brackets). Naymaconsultores (2025 filing guidance).

## Section 6 — Major Optimization Lever 2: Loss Carryforward Planning

### Mechanism

- **Loss carryforward mechanism** — ISLR Law permits carrying forward trade/business losses for up to **3 years**. In any single carryforward year, losses applied may not exceed **25% of that year's taxable income**. No carryback is permitted.

### Eligibility

- **Loss carryforward eligibility** — - Individuals and companies subject to Tarifa No. 1 or Tarifa No. 2 respectively. - Losses must arise from legitimate commercial activity. - Foreign-source losses may only offset foreign-source income. - **Monetary correction (inflation adjustment) losses cannot be carried forward at all.**

### Quantified Savings

**Loss carryforward quantified savings**

| Year | Taxable Income before Loss | Loss Applied (max 25%) | Taxable Income after Loss | Tax at 34% | Tax Saving (vs. no loss) |
| --- | --- | --- | --- | --- | --- |
| Y2 | Bs. 172,000 (4,000 UT) | Bs. 43,000 (1,000 UT) | Bs. 129,000 (3,000 UT) | Bs. 43,860 | Bs. 14,620 |
| Y3 | Bs. 172,000 (4,000 UT) | Bs. 43,000 (1,000 UT) | Bs. 129,000 (3,000 UT) | Bs. 43,860 | Bs. 14,620 |
| Y4 | Bs. 172,000 (4,000 UT) | Bs. 43,000 (1,000 UT) | Bs. 129,000 (3,000 UT) | Bs. 43,860 | Bs. 14,620 |
| Remaining unabsorbed | Bs. 43,000 (1,000 UT) | Expired — 3-year limit reached | — | — | Lost |

### Planning Implication

- **Loss carryforward planning implication** — Plan income recognition so that profitable years fall within 3 years of the loss year. Do not generate losses in Year N if profitability is not expected until Year N+4 — the loss will expire.

### Source

PwC Worldwide Tax Summaries — Venezuela Corporate, Deductions (January 2026).

## Section 7 — Major Optimization Lever 3: Individual vs. Corporate Rate Arbitrage

### Tarifa No. 1 — Individual Rates (2025)

**Tarifa No. 1 — Individual Rates (2025)**

| Taxable Income (UT) | Taxable Income (Bs., at UT=43) | Rate | Fixed Deduction (UT) | Fixed Deduction (Bs.) |
| --- | --- | --- | --- | --- |
| 0 – 1,000 | 0 – 43,000 | 6% | 0 | 0 |
| 1,000 – 1,500 | 43,000 – 64,500 | 9% | 30 | 1,290 |
| 1,500 – 2,000 | 64,500 – 86,000 | 12% | 75 | 3,225 |
| 2,000 – 2,500 | 86,000 – 107,500 | 16% | 155 | 6,665 |
| 2,500 – 3,000 | 107,500 – 129,000 | 20% | 255 | 10,965 |
| 3,000 – 4,000 | 129,000 – 172,000 | 24% | 375 | 16,125 |
| 4,000 – 6,000 | 172,000 – 258,000 | 29% | 575 | 24,725 |
| Over 6,000 | Over 258,000 | 34% | 875 | 37,625 |

### Tarifa No. 2 — Corporate Rates (2025)

**Tarifa No. 2 — Corporate Rates (2025)**

| Taxable Income (UT) | Taxable Income (Bs., at UT=43) | Rate | Fixed Deduction (UT) | Fixed Deduction (Bs.) |
| --- | --- | --- | --- | --- |
| 0 – 2,000 | 0 – 86,000 | 15% | 0 | 0 |
| 2,000 – 3,000 | 86,000 – 129,000 | 22% | 140 | 6,020 |
| Over 3,000 | Over 129,000 | 34% | 500 | 21,500 |

### Special Sector Flat Rates

**Special Sector Flat Rates**

| Sector | Flat Rate |
| --- | --- |
| Petroleum exploitation, refining, transport, export of hydrocarbons | 50% |
| Banking and insurance | 40% |

### Optimization Logic

- **Individual vs corporate rate arbitrage logic** — For income levels below ~2,000 UT (Bs. 86,000), the individual progressive rate (6%–12%) is lower than the corporate minimum rate of 15%. Sole-trader structures are more efficient at low income. Once income exceeds ~4,000 UT (Bs. 172,000), individual and corporate rates converge at 34%, and corporate structuring offers no rate advantage at the entity level — but dividend distribution then triggers an additional 34% dividend WHT, creating economic double taxation unless a treaty applies. **Key rule of thumb:** Corporate structuring is only tax-efficient in Venezuela if profits can be retained in the company (avoiding dividend tax) or if a treaty holding structure reduces the dividend WHT to 0–10%.

### Source

PwC Worldwide Tax Summaries — Venezuela Corporate and Individual (January 2026). icalculator.com/ve income-tax-rates.

## Section 8 — Major Optimization Lever 4: Special Economic Zone (SEZ) Incentives

### Mechanism

**Mechanism**

| SEZ | ISLR Refund | Duration | Export Requirement from Year 7 |
| --- | --- | --- | --- |
| La Guaira State SEZ | Up to 100% | First 4 fiscal years | ≥ 60% of production exported |
| Aragua Military SEZ | Up to 100% | First 4 fiscal years | ≥ 60% of production exported |
| Paraguaná Peninsula SEZ | Up to 100% | First 4 fiscal years | ≥ 60% of production exported |
| Tortuga Island SEZ | Up to 100% | First 20 fiscal years | ≥ 60% of production exported |

### Eligibility

- **SEZ eligibility** — Company must physically operate within the designated SEZ and obtain certification under Resolution 015-25 (May 9, 2025). Maximum total incentives are capped annually by the Ministry of Finance (cap published within 15 business days after the ISLR filing period).

### Quantified Savings

A manufacturing company earning 5,000 UT (Bs. 215,000) of taxable income per year would ordinarily pay:

Tarifa No. 2: (Bs. 215,000 × 34%) − Bs. 21,500 = Bs. 73,100 − Bs. 21,500 = **Bs. 51,600 in ISLR annually**.

Under a 100% SEZ refund: ISLR paid = Bs. 51,600; ISLR refunded = Bs. 51,600; **Net ISLR cost = Bs. 0** for the qualifying period.

Over 4 years: **Bs. 206,400 in cumulative ISLR savings** (at 2025 UT; amounts will change as UT adjusts).

Note: These are structured as reimbursements/drawbacks, not direct exemptions. The company must file ISLR, pay the tax, then apply for the refund. Cash-flow implications must be planned.

### Source

VATupdate — SEZs tax incentives (September 2023). Lexology — SEZ implementing rules (Resolution 015-25, May 2025). PwC — Tax Credits and Incentives (January 2026). PwC explicitly notes export drawback is "not currently being applied in practice" — SEZ refunds are a distinct mechanism; confirm status with SENIAT before relying on them.

## Section 9 — Major Optimization Lever 5: Treaty Withholding Rate Reduction on Dividends

### Mechanism

- **Domestic dividend withholding rate** — 34% flat  _(ISLR Law)_

### Treaty Rates (Dividends) — Selected

**Treaty Rates (Dividends) — Selected**

| Treaty Partner | Reduced WHT Rate | Notes |
| --- | --- | --- |
| Spain | 0–10% | 0% for qualifying corporate shareholders; 10% for others |
| United States | 5–15% | 5% for ≥10% shareholding; 15% otherwise |
| Mexico | 5% | Beneficial for intra-LatAm structures |
| France | 0–15% | 0% in certain conditions; treaty contains anti-abuse provisions |
| Canada | 10–15% | 10% for ≥25% shareholding; 15% otherwise |
| Brazil | 10–15% | 10% for substantial holdings |

### Eligibility

- **Treaty WHT eligibility conditions** — To access treaty WHT rates: 1. A qualifying holding company must be established in the treaty country. 2. The holding company must have genuine substance (management, employees, offices) to satisfy treaty anti-abuse provisions. 3. The payment must constitute "dividends" within the treaty definition. 4. Beneficial ownership must rest with a treaty-country resident (conduit structures disqualified).

### Quantified Savings

**Dividend treaty savings example**

| Scenario | WHT Rate | WHT Amount | Net to Parent |
| --- | --- | --- | --- |
| No treaty (domestic) | 34% | Bs. 146,200 | Bs. 283,800 |
| Via Spain holding co. | 10% | Bs. 43,000 | Bs. 387,000 |
| Via Spain (0% tier) | 0% | Bs. 0 | Bs. 430,000 |
| **Saving (Spain 0% vs. no treaty)** |  | **Bs. 146,200** |  |

### Source

PwC Worldwide Tax Summaries — Venezuela Withholding Taxes (January 2026).

## Section 10 — Major Optimization Lever 6: Thin Capitalization Management

### Mechanism

- **Thin capitalization mechanism** — Venezuela has one of the world's most restrictive thin-capitalization rules. ISLR Law (Art. 38): if the **average total related-party debt** of an entity during the fiscal year exceeds its **average equity**, the excess debt is recharacterized as equity and the corresponding interest is **non-deductible** for ISLR. Ratio: **1:1 debt-to-equity** (compared to Canada 1.5:1, Germany 30%-of-EBITDA, OECD best practice).  _(ISLR Law Art. 38)_

### Eligibility Scope

- **Thin cap eligibility scope** — Applies to related-party debt. Third-party arm's-length debt is not explicitly subject to the thin-cap rule. However, SENIAT has challenged back-to-back loan arrangements that route third-party debt through a related party.

### Quantified Savings

A company with Bs. 200,000 (4,651 UT) in equity that borrows Bs. 300,000 (6,977 UT) from a related party at 12% annual interest:

- Related-party debt: Bs. 300,000
- Equity: Bs. 200,000
- Excess debt: Bs. 100,000 (debt minus equity)
- Non-deductible interest: Bs. 100,000 × 12% = **Bs. 12,000 of non-deductible interest**
- Additional ISLR cost at 34%: Bs. 12,000 × 34% = **Bs. 4,080**

If the company restructures to equity = debt = Bs. 250,000 (capitalizing Bs. 50,000 of the loan):
- Remaining related-party debt: Bs. 250,000 = equity — within the 1:1 ratio
- All interest now deductible
- **Annual saving: Bs. 4,080 in ISLR**

### Planning Actions

- **Thin cap planning actions** — 1. Monitor the debt-to-equity ratio at the start of each fiscal year (rule applies to the annual average). 2. Capitalize related-party loans above the 1:1 threshold before year-end. 3. Replace excess related-party debt with third-party bank debt where commercially viable. 4. Do not use back-to-back loan structures where the economic lender is a related party.

### Source

PwC Worldwide Tax Summaries — Venezuela Group Taxation (January 2026).

## Section 11 — Major Optimization Lever 7: LOCTI Contribution — Sector Classification

### Mechanism

- **LOCTI mechanism** — LOCTI (Ley Orgánica de Ciencia, Tecnología e Innovación, April 2022) imposes a monthly contribution on gross income. Rate depends on the company's activity classification.

### Rate Table

**LOCTI Rate Table**

| Sector | LOCTI Rate | Base |
| --- | --- | --- |
| Bingos, casinos, alcohol, tobacco | 2% | Monthly gross income |
| Hydrocarbons or mining | 1% | Monthly gross income |
| All other activities | 0.5% | Monthly gross income |
| Multi-activity companies | Highest applicable rate | Assessed on total gross income |

### Quantified Savings

**LOCTI misclassification savings example**

| Classification | Rate | Annual LOCTI | Overpayment if misclassified |
| --- | --- | --- | --- |
| Incorrect: gambling | 2% | Bs. 200,000 | — |
| Correct: other | 0.5% | Bs. 50,000 | **Bs. 150,000/year saved** |

### Administration

- **LOCTI administration** — LOCTI is paid monthly via the SIDCAI system administered by SENIAT (Administrative Ruling No. 015-004-2024, February 2024). This is a contribution, not an ISLR credit.  _(Administrative Ruling No. 015-004-2024, February 2024)_

### Source

PwC Worldwide Tax Summaries — Venezuela Corporate Other Taxes (January 2026). IBA Tax Country Report — Venezuela 2025. Baker McKenzie LOCTI bulletin (2024).

## Section 12 — Major Optimization Lever 8: ISAE (Municipal Business Tax) Deductibility

### Mechanism

- **ISAE mechanism** — The Impuesto sobre Actividades Económicas (ISAE), also called Patente de Industria y Comercio, is levied by each Venezuelan municipality on gross income from economic activities within their jurisdiction. Legal basis: Ley Orgánica del Poder Público Municipal. Key features: - Rates vary by municipality and activity: general range **1% to 6.5%** of gross income. - Minimum taxable base: 20 UT (= Bs. 860 at 2025 UT). - Rates are set by each municipality's Ordenanza — there is no national cap. **ISLR interaction:** ISAE paid to municipalities is **deductible as an operating expense** against ISLR taxable income. This makes proper ISAE documentation and allocation critical for ISLR planning.  _(Ley Orgánica del Poder Público Municipal)_

### Quantified Savings

A company paying Bs. 300,000 in ISAE across multiple municipalities, operating in the 34% ISLR bracket:

ISLR reduction: Bs. 300,000 × 34% = **Bs. 102,000 in annual ISLR savings** from properly deducting ISAE.

If ISAE is not claimed: Bs. 102,000 of avoidable ISLR is paid unnecessarily.

### Planning Actions

- **ISAE planning actions** — 1. Maintain separate records of ISAE paid by municipality and period. 2. Ensure all ISAE payments are supported by official receipts (comprobantes municipales). 3. Review the activity classification in each municipality's tariff schedule annually — misclassification can result in overpayment (ISAE computed on gross income, not net, so errors are magnified). 4. Note that ISAE computed on gross income is a significant burden for low-margin businesses; negotiate favorable tariff classification during municipal business license renewal.

### Source

PwC Worldwide Tax Summaries — Venezuela Corporate Other Taxes (January 2026). Acceso a la Justicia — ISAE explainer.

## Section 13 — Major Optimization Lever 9: VAT Rate Structuring

### Rate Structure

**VAT Rate Structure**

| Category | Rate | Examples |
| --- | --- | --- |
| Standard | 16% | Most goods and services |
| Reduced | 8% | Goats, sheep, minor livestock; refrigerated meats; shortening; professional services to government bodies; domestic air passenger transport; certain construction |
| Luxury surcharge | +15% (total effective ~31%) | Vehicles ≥ USD 40,000; motorcycles ≥ USD 20,000; jewelry ≥ USD 300; restaurant/bar services; gaming machines |
| Zero-rated | 0% | Exports of goods and services |
| Foreign currency / crypto surcharge | 5–25% | Transactions paid in foreign currency, crypto, or non-Venezuelan crypto-assets (rate set by Executive) |

### Key 2025 Change — Import Exemption Suspension

- **Import exemption suspension and replacement exemption** — Presidential Decree No. 5,145 (June 30, 2025; effective July 5, 2025) **suspended** the VAT exemption on imports of basic foods, medicines, fertilizers, medical equipment, books, and certain fuels. Simultaneously, Decree No. 5,146 granted a **one-year VAT exemption until June 30, 2026** for imports by National Public Administration bodies and designated private entities (Appendix I). Companies relying on these exemptions must re-verify their status annually.  _(Presidential Decree No. 5,145, June 30, 2025; Presidential Decree No. 5,146, June 30, 2025)_

### Optimization Actions

- **VAT optimization actions** — 1. **Export structuring:** If services can legitimately be rendered for the benefit of foreign recipients, qualifying as an export of services yields 0% output VAT while input VAT remains recoverable. 2. **Activity classification:** Verify that the reduced 8% rate is claimed for qualifying activities (e.g., government professional services contracts). Overcharging at 16% creates administrative burden; undercharging creates a compliance liability. 3. **Foreign currency transaction planning:** The 5–25% surcharge on transactions paid in foreign currency or crypto is significant. Where contractually possible, structure payment terms to use bolivar settlement. 4. **Special taxpayer withholding (from August 1, 2025):** Ruling SNAT/2025/000054 expanded VAT withholding obligations. Verify whether the client is a designated withholding agent and whether their counterparties are, to correctly account for VAT flows.

### Source

Avalara — Venezuelan VAT Compliance (2025). KPMG — Venezuela VAT changes 2025 (August 2025). PwC — Corporate Other Taxes (January 2026). VATupdate — Exemption until June 2026 (July 2025).

### Rate Table

**Social Security / Payroll Contribution Rate Table**  _(Section 14 — Major Optimization Lever 10)_

| Fund | Employer Rate | Employee Rate | Salary Base Cap | Notes |
| --- | --- | --- | --- | --- |
| IVSS (Mandatory Social Security) | 9–11% | 4% | 5 minimum salaries | Employer rate varies by enterprise risk classification |
| FAOV (Housing Savings — primary) | 2% | 1% | No cap | Based on integral salary |
| FAV (Housing — secondary / LPH) | 2% | 0.5% | 10 minimum salaries | Employment Benefit Regime |
| INCES (Training) | 2% (quarterly wages) | 0.5% (profit-sharing/utilidades) | No cap | Employer quarterly; employee on utilidades only |
| Paro Forzoso (Unemployment) | 2% | 0.5% | No cap | — |
| LOPCYMAT (Workplace safety) | 0% | — | No cap | Employer only; rate set by INPSASEL risk assessment |
| Special Pension Contribution (from May 2024) | 9% | — | — | Employer only |

### Payment Deadlines

**Payment Deadlines**  _(Section 14 — Major Optimization Lever 10)_

| Fund | Deadline |
| --- | --- |
| IVSS | By the 16th of each month |
| FAOV | Within first 5 business days of each month |
| INCES | Within first 5 business days after each quarter closes |

### Optimization Actions

- **IVSS risk tier** — The employer IVSS rate (9–11%) is determined by INPSASEL (the workplace safety authority) based on industry risk classification. Investing in documented workplace safety improvements and obtaining a favorable INPSASEL risk rating can reduce the employer contribution by up to 2 percentage points.  _(Section 14 — Optimization Actions)_
- **LOPCYMAT rate** — This is 0% per the applicable rate, set by INPSASEL risk assessment.  _(Section 14 — Optimization Actions)_
- **Integral salary calculation** — Ensure the FAOV base (integral salary) is correctly computed. Overstating the integral salary base (e.g., incorrectly including non-salary benefits) overstates contributions.  _(Section 14 — Optimization Actions)_

### Quantified Example

**IVSS Cost Scenario Table**  _(Section 14 — Quantified Example)_

| Scenario | Annual IVSS Cost | Difference |
| --- | --- | --- |
| 11% (high-risk) | Bs. 550,000 | — |
| 9% (low-risk, after safety investment) | Bs. 450,000 | **Bs. 100,000/year saved** |

**LOPCYMAT Scenario Table**  _(Section 14 — Quantified Example)_

| Scenario | Annual LOPCYMAT | Difference |
| --- | --- | --- |
| 0% | Bs. 0 | — |

A company with Bs. 5,000,000 annual payroll at the 11% IVSS rate vs. 9%:

LOPCYMAT: Rate is 0%; no LOPCYMAT cost applies.

**Combined potential payroll saving: Bs. 200,000/year** from safety investment — before considering the ISLR deductibility of the safety investment itself.

### Source

PwC — Venezuela Individual Other Taxes (January 2026). Playroll Venezuela payroll guide. Moore Global — Venezuela Tax Guide.

### Pattern 1: Should an individual use desgravamen único or itemized?

START: Individual ISLR filer, Venezuela resident

Step 1: Sum qualifying itemized expenses:
  - Education expenses (no cap)
  - Insurance premiums (life/surgery/hospitalization/maternity) (no cap)
  - Medical/dental/hospital expenses (no cap)
  - Mortgage interest on primary residence (cap: 1,000 UT = Bs. 43,000 at 2025 UT)
  - Rent on primary residence (cap: 800 UT = Bs. 34,400 at 2025 UT)

Step 2: Compare sum to standard desgravamen único: 774 UT (= Bs. 33,282 at 2025 UT)

Step 3:
  If sum > 774 UT → USE ITEMIZED (desgravamen detallado)
  If sum ≤ 774 UT → USE STANDARD (desgravamen único)

Step 4: Confirm all itemized expenses were paid to Venezuelan-domiciled entities.
  If any expense was paid to a foreign entity → EXCLUDE that item from itemized total.
  Re-run comparison.

Note: Must choose ONE method. Cannot combine. Decision is made per fiscal year.

### Pattern 2: Is a corporate structure beneficial vs. sole trader?

START: Venezuelan entrepreneur considering structuring

Step 1: Estimate annual net income (UT)
  < 2,000 UT (Bs. 86,000)? → SOLE TRADER likely more efficient
    Reason: Individual rates 6–12% vs. corporate minimum 15%

  2,000–3,000 UT (Bs. 86,000–129,000)? → DEPENDS on profit retention
    If profits can be retained in company: Corp rate 22% vs. individual up to 16–20%
    If profits must be distributed: Add 34% dividend WHT → economic double tax
    Sole trader likely better unless treaty holding structure available

  > 3,000 UT (Bs. 129,000)? → Both corporate and individual converge at 34%
    Corporate beneficial ONLY if:
    (a) Profits retained long-term, AND
    (b) Treaty holding structure reduces dividend WHT to ≤10%
    Otherwise: equivalent effective rate, with corporate adding compliance cost

Step 2: Check sector:
  Banking or insurance? → FLAT 40% corporate rate (worse than individual at most levels)
  Petroleum? → FLAT 50% (unambiguously the highest; avoid direct ownership if possible)

Step 3: Assess treaty availability:
  Is there a treaty-country holding company option? (Spain 0–10%, US 5–15%, Mexico 5%)
  Does the holding company have genuine commercial substance?
  If YES to both → Corporate structure with treaty holding reduces effective total rate
  If NO → Avoid corporate structure at income > 2,000 UT

Conclusion: Venezuela's high dividend WHT means sole-trader structures are competitive
at most income levels unless a qualifying treaty holding structure is in place.

### Pattern 3: Thin capitalization compliance check

START: Venezuelan company with related-party loans

Step 1: Compute average equity for the fiscal year (average of opening and closing equity)
Step 2: Compute average total related-party debt for the fiscal year
Step 3: Compare:
  Related-party debt ≤ equity? → COMPLIANT; all interest deductible
  Related-party debt > equity? → NON-COMPLIANT
    Excess = related-party debt − equity
    Interest on excess = excess × interest rate = NON-DEDUCTIBLE
    Additional ISLR cost = non-deductible interest × applicable Tarifa No. 2 rate

Step 4: Remediation options:
  Option A: Capitalize part of the loan (convert to equity) before fiscal year-end
  Option B: Accelerate loan repayment to bring below 1:1 ratio
  Option C: Replace related-party loan with third-party bank debt
  Option D: None viable → Accept non-deductible interest and document

Step 5: Document the average equity and debt calculation in the tax working paper.

### Pattern 4: Which LOCTI rate applies?

START: Company receiving LOCTI assessment

Step 1: Identify primary activity:
  Bingo, casino, alcohol production/sale, or tobacco? → 2%
  Hydrocarbons extraction or mining (and NOT exempt under Jan 2026 reform)? → 1%
  Petroleum company qualifying under 2026 Hydrocarbons Law Reform? → EXEMPT
  All other activities? → 0.5%

Step 2: Multi-activity company?
  Yes → Apply HIGHEST rate to ALL gross income
  No → Apply single applicable rate

Step 3: Is monthly gross income above 150,000× BCV highest foreign currency rate?
  Below threshold → NOT SUBJECT to LOCTI this month
  Above threshold → LOCTI applies at the rate from Step 1

Step 4: Pay via SIDCAI by monthly deadline.

### Pattern 5: Loss carryforward — can it be used this year?

START: Company with a prior-year loss carryforward

Step 1: What year was the loss incurred?
  More than 3 tax years ago? → EXPIRED; cannot use
  Within 3 years? → PROCEED

Step 2: Is the current year taxable income positive?
  No (current-year loss) → Cannot use carryforward; carries forward again (if within 3-year limit)
  Yes → PROCEED

Step 3: Compute 25% of current-year taxable income (before loss application)
  Amount = current-year taxable income × 25%
  Loss applied this year = MINIMUM of (remaining carryforward balance, 25% of taxable income)

Step 4: Apply the loss. Remaining balance carries forward if within 3-year window.

Step 5: Is the loss from inflation/monetary correction?
  Yes → CANNOT be carried forward at all. If not used in the year generated, it expires.
  No → Standard 3-year carryforward applies.

## Section 16 — Worked Examples

> All examples use UT = Bs. 43.00 (SNAT/2025/000048, June 2, 2025).
> CONFIRM CURRENT UT VALUE FROM SENIAT BEFORE QUOTING BS. FIGURES TO CLIENTS.

### Worked Example 1: Individual — Desgravamen Comparison (High Medical Spend)

**Facts:** María is a Venezuelan-resident architect. FY 2025. Annual professional income: Bs. 180,000 (approximately 4,186 UT). She paid during 2025:
- Surgery and hospitalization (Venezuelan clinic): Bs. 22,000
- Life insurance premium (Venezuelan insurer): Bs. 8,000
- Daughter's university fees (Venezuelan university): Bs. 14,000
- Mortgage interest on her Caracas apartment: Bs. 40,000 (but cap is 1,000 UT = Bs. 43,000 so full amount within cap)

**Step 1: Determine gross income in UT**
Bs. 180,000 ÷ Bs. 43 = 4,186 UT (approximately)

**Step 2: Calculate desgravamen único**
Standard deduction: 774 UT × Bs. 43 = Bs. 33,282

**Step 3: Itemized deductions table**  _(Worked Example 1)_

| Item | Amount | Within Cap? |
| --- | --- | --- |
| Surgery/hospitalization | Bs. 22,000 | No cap — fully included |
| Life insurance premium | Bs. 8,000 | No cap — fully included |
| University fees | Bs. 14,000 | No cap — fully included |
| Mortgage interest | Bs. 40,000 | Cap = Bs. 43,000 — fully included |
| **Total itemized** | **Bs. 84,000** |  |

Bs. 84,000 ÷ Bs. 43 = 1,953 UT

**Step 4: Compare table**  _(Worked Example 1)_

| Method | Deduction (Bs.) | Deduction (UT) |
| --- | --- | --- |
| Desgravamen único | Bs. 33,282 | 774 UT |
| Itemized | Bs. 84,000 | 1,953 UT |
| **Advantage of itemized** | **Bs. 50,718 more** | **1,179 UT more** |

**Step 5: Taxable income table**  _(Worked Example 1)_

| Method | Gross Income | Less Desgravamen | Taxable Income |
| --- | --- | --- | --- |
| Standard | Bs. 180,000 | Bs. 33,282 | Bs. 146,718 (= ~3,412 UT) |
| Itemized | Bs. 180,000 | Bs. 84,000 | Bs. 96,000 (= ~2,233 UT) |

- **Step 6: Apply Tarifa No. 1** — _Standard desgravamen (taxable income Bs. 146,718 → ~3,412 UT — in the 3,000–4,000 UT bracket at 24%):_ Tax = (Bs. 146,718 × 24%) − Bs. 16,125 Tax = Bs. 35,212 − Bs. 16,125 = **Bs. 19,087** _Itemized (taxable income Bs. 96,000 → ~2,233 UT — in the 2,000–2,500 UT bracket at 16%):_ Tax = (Bs. 96,000 × 16%) − Bs. 6,665 Tax = Bs. 15,360 − Bs. 6,665 = **Bs. 8,695**  _(Worked Example 1)_

**Reconciliation table**  _(Worked Example 1)_

| Scenario | ISLR Due | Saving |
| --- | --- | --- |
| Standard desgravamen | Bs. 19,087 | — |
| Itemized desgravamen | Bs. 8,695 | — |
| **Saving from itemizing** |  | **Bs. 10,392** |

Recommendation: María should use itemized deductions. Annual ISLR saving of **Bs. 10,392** (at 2025 UT). All payments must be to Venezuelan-domiciled entities with valid tax receipts (facturas con RIF).

### Worked Example 2: Company — Loss Carryforward Absorption

**Facts:** TechVe C.A. (non-financial company). Results over 4 years:

**Results over 4 years table**  _(Worked Example 2)_

| Year | Net Taxable Income / (Loss) before Carryforward | Notes |
| --- | --- | --- |
| FY2023 | (Bs. 120,000) = ~(2,791 UT) | Operating loss |
| FY2024 | Bs. 50,000 = ~1,163 UT | Recovery year |
| FY2025 | Bs. 200,000 = ~4,651 UT | Strong year (at 2025 UT) |
| FY2026 | Bs. 250,000 = ~5,814 UT | Strong year (assumed 2025 UT for illustration) |

- **Carryforward mechanics FY2024-FY2026** — **Carryforward mechanics (annual loss application cap: 25% of taxable income):** **FY2024:** - Current-year taxable income: Bs. 50,000 - 25% cap on loss use: Bs. 12,500 - Loss applied: Bs. 12,500 - Taxable income after loss: Bs. 37,500 (= 872 UT) - Tax at 15% (≤ 2,000 UT bracket): Bs. 5,625 - Without loss: Bs. 50,000 × 15% = Bs. 7,500; Saving Year 2: **Bs. 1,875** - Remaining carryforward: Bs. 107,500 **FY2025:** - Current-year taxable income: Bs. 200,000 - 25% cap: Bs. 50,000 - Loss applied: Bs. 50,000 - Taxable income after loss: Bs. 150,000 (= 3,488 UT — 22% bracket then 34% bracket; use blended calculation) - First 2,000 UT (Bs. 86,000) at 15% = Bs. 12,900 - Next 1,000 UT (Bs. 43,000) at 22% = Bs. 9,460 - Remaining Bs. 21,000 (488 UT) at 34% = Bs. 7,140 - Total ISLR: Bs. 29,500 - Without loss applied (Bs. 200,000): - First 2,000 UT (Bs. 86,000) × 15% = Bs. 12,900 - Next 1,000 UT (Bs. 43,000) × 22% = Bs. 9,460 - Remaining Bs. 71,000 (1,651 UT) × 34% = Bs. 24,140 - Total ISLR: Bs. 46,500 - Saving Year 3: Bs. 46,500 − Bs. 29,500 = **Bs. 17,000** - Remaining carryforward: Bs. 57,500 **FY2026 (Year 4 — beyond 3-year limit from FY2023):** - Loss incurred FY2023; FY2026 is the 4th year → **LOSS EXPIRED**. Remaining Bs. 57,500 cannot be used.  _(Worked Example 2)_

**Reconciliation table**  _(Worked Example 2)_

| Year | Loss Applied | ISLR Saving |
| --- | --- | --- |
| FY2024 | Bs. 12,500 | Bs. 1,875 |
| FY2025 | Bs. 50,000 | Bs. 17,000 |
| FY2026 | Bs. 0 (expired) | Bs. 0 |
| **Total** | **Bs. 62,500** | **Bs. 18,875** |
| Unused loss (expired) | Bs. 57,500 | Bs. 0 |

**Key lesson:** TechVe's profitability recovery was too slow. Had it generated Bs. 240,000 in FY2025 (allowing Bs. 60,000 carryforward = 25% × Bs. 240,000), it would have absorbed more of the loss. Tax planning to accelerate profitability recognition into Year 2/3 windows maximizes loss absorption.

### Worked Example 3: Corporate Dividend Extraction — Treaty vs. No Treaty

**Facts:** InverVE S.A., a Venezuelan operating company with 100% foreign ownership. Annual after-tax profit: Bs. 430,000 (10,000 UT at 2025 UT). The parent intends to distribute all profits.

**Scenario A: No treaty table**  _(Worked Example 3)_

| Step | Amount |
| --- | --- |
| Venezuelan ISLR (assume income > 3,000 UT; 34% bracket) | Bs. 430,000 × 34% − Bs. 21,500 = Bs. 124,700 |
| After-ISLR profit | Bs. 305,300 |
| Dividend WHT (34% on distributed amount) | Bs. 305,300 × 34% = Bs. 103,802 |
| Net distributed to foreign parent | Bs. 305,300 − Bs. 103,802 = **Bs. 201,498** |
| Effective combined rate | (Bs. 430,000 − Bs. 201,498) ÷ Bs. 430,000 = **53.1%** |

**Scenario B: Spanish holding company (10%) table**  _(Worked Example 3)_

| Step | Amount |
| --- | --- |
| Venezuelan ISLR (same) | Bs. 124,700 |
| After-ISLR profit | Bs. 305,300 |
| Dividend WHT (10% treaty rate, Spain) | Bs. 305,300 × 10% = Bs. 30,530 |
| Net distributed to Spanish holdco | Bs. 305,300 − Bs. 30,530 = **Bs. 274,770** |
| Effective combined rate | (Bs. 430,000 − Bs. 274,770) ÷ Bs. 430,000 = **36.1%** |

**Scenario C: Spanish holding company (0%) table**  _(Worked Example 3)_

| Step | Amount |
| --- | --- |
| Venezuelan ISLR (same) | Bs. 124,700 |
| After-ISLR profit | Bs. 305,300 |
| Dividend WHT (0% treaty rate) | Bs. 0 |
| Net distributed to Spanish holdco | **Bs. 305,300** |
| Effective combined rate | (Bs. 430,000 − Bs. 305,300) ÷ Bs. 430,000 = **29.0%** |

**Reconciliation table**  _(Worked Example 3)_

| Scenario | Net to Parent (Bs.) | Effective Rate | Saving vs. No Treaty |
| --- | --- | --- | --- |
| No treaty | Bs. 201,498 | 53.1% | — |
| Spain (10%) | Bs. 274,770 | 36.1% | **Bs. 73,272** |
| Spain (0%) | Bs. 305,300 | 29.0% | **Bs. 103,802** |

Note: ISLR computed as a simplified illustration. The dividend tax base is the positive difference between book income and fiscal income (LIFO method) — this may differ from the full after-tax profit. Engage a Venezuelan CPA to compute the exact dividend tax base before distribution.

Note on Spain treaty 0% rate: the 10% general dividend rate is confirmed by PwC/Deloitte. The specific shareholding threshold qualifying for the 0% tier is cited in treaty commentary but **must be verified against the treaty text** before client use — do not rely on the 0% rate without confirming the threshold with a tax adviser.

## Section 17 — Tier 1 Prompts (Basic Optimization)

Use these prompts for straightforward individual or small-business clients:

1. "Using Venezuela's ISLR Tarifa No. 1, compute the annual ISLR for an individual with gross income of [X] UT, using the standard 774 UT desgravamen único. Show the bracket calculation."

2. "My client has the following itemized expenses: [list]. Is the desgravamen detallado or the desgravamen único more favorable? Show the comparison."

3. "Calculate the ISLR for a Venezuelan C.A. with taxable income of [X] UT using Tarifa No. 2. Show the bracket computation."

4. "A Venezuelan company paid [X] Bs. in ISAE (municipal business tax) this year. How much does this reduce its ISLR liability, assuming the 34% bracket?"

5. "A Venezuelan company's related-party debt averages [X] Bs. and its equity averages [Y] Bs. Is it within the thin-capitalization limit? How much interest is non-deductible?"

## Section 18 — Tier 2 Prompts (Complex / Multi-Lever Optimization)

Use these prompts for corporate clients, cross-border structures, or multi-year planning:

1. "A Venezuelan company incurred a Bs. [X] operating loss in FY[year]. Project the maximum ISLR savings from carrying this forward, assuming the following income in subsequent years: [Y1, Y2, Y3]. Show the 25%-of-taxable-income cap applied each year and flag the expiry."

2. "Structure a dividend extraction plan for a Venezuelan company with after-tax profits of Bs. [X], owned by a holding company in [country]. Compute the effective combined rate under domestic law and under the treaty, showing the WHT comparison."

3. "A company in [city], Venezuela operates across three municipalities with the following gross income per municipality: [list]. Calculate total ISAE across all municipalities and the ISLR deduction value of that ISAE, assuming the 34% bracket."

4. "Evaluate whether a Special Economic Zone structure (Tortuga Island SEZ) is viable for a manufacturing company projecting annual ISLR of Bs. [X] over 20 years. Show the cumulative ISLR saving against setup and compliance costs (placeholder for client-specific costs)."

5. "A Venezuelan company has related-party loans of Bs. [X] at [Y]% interest and equity of Bs. [Z]. Calculate the thin-capitalization non-deductible interest and the additional ISLR cost. Propose the minimum equity injection or loan repayment to achieve compliance."

6. "A client has cryptocurrency trading profits in FY2025. They received [X] BTC at various dates; provide a framework for computing ISLR in bolivars, identifying the market-value-at-receipt principle, the applicable Tarifa, and the record-keeping required for SENIAT."

## Section 19 — Working Paper Template

Use this template to document Venezuela ISLR computations for individual or corporate clients. Retain all supporting documents for 5 years (COT statute of limitations).

```
VENEZUELA ISLR WORKING PAPER
Client: ___________________________
RIF: ______________________________
Fiscal Year: _______________________
UT value used: Bs. _____ (SENIAT Ruling No. _______, G.O. No. ________, Date: _________)
UT value confirmation: [ ] Confirmed from SENIAT website on __________ / [ ] Using SNAT/2025/000048 (Bs. 43.00)

SECTION A — GROSS INCOME
1. Employment / professional fees:              Bs. _____________ = _______ UT
2. Business/commercial income:                  Bs. _____________ = _______ UT
3. Rental income:                               Bs. _____________ = _______ UT
4. Dividends received (if applicable):          Bs. _____________ = _______ UT
5. Cryptocurrency income (market value at receipt): Bs. _________ = _______ UT
6. Other income:                                Bs. _____________ = _______ UT
   TOTAL GROSS INCOME:                          Bs. _____________ = _______ UT

SECTION B — DEDUCTIONS / DESGRAVAMEN
Method selected: [ ] Desgravamen único (774 UT = Bs. _____) | [ ] Desgravamen detallado
If itemized:
  Education expenses:                           Bs. _____________
  Insurance premiums:                           Bs. _____________
  Medical/dental/hospital:                      Bs. _____________
  Mortgage interest (cap 1,000 UT = Bs. _____): Bs. _____________
  Rent (cap 800 UT = Bs. _____):                Bs. _____________
  TOTAL ITEMIZED:                               Bs. _____________ = _______ UT
Desgravamen applied:                            Bs. _____________ = _______ UT

SECTION C — LOSS CARRYFORWARD
Prior-year loss balance:                        Bs. _____________ = _______ UT (incurred FY ____)
25% of current taxable income:                  Bs. _____________
Loss applied this year (lesser of above two):   Bs. _____________
Remaining carryforward:                         Bs. _____________ (expires FY ____)

SECTION D — TAXABLE INCOME
= Gross income − Desgravamen − Loss applied
Taxable income:                                 Bs. _____________ = _______ UT

SECTION E — TARIFA COMPUTATION
For individuals (Tarifa No. 1):
Applicable bracket: _______ UT to _______ UT at _______ %
Tax = Bs. _____________ × ____% − Bs. _____________ (fixed deduction)
     = Bs. _____________

For companies (Tarifa No. 2):
Layer 1: [0–2,000 UT] Bs. ______ × 15% = Bs. ______
Layer 2: [2,000–3,000 UT] Bs. ______ × 22% = Bs. ______
Layer 3: [>3,000 UT] Bs. ______ × 34% = Bs. ______
TOTAL ISLR:                                     Bs. _____________

SECTION F — MUNICIPAL TAXES (ISAE)
ISAE paid (Municipality 1 — ____________):      Bs. _____________
ISAE paid (Municipality 2 — ____________):      Bs. _____________
TOTAL ISAE (ISLR-deductible):                   Bs. _____________
ISLR reduction from ISAE deductibility:         Bs. _____________ × ____% = Bs. _____________

SECTION G — SOCIAL SECURITY / LOCTI
IVSS employer rate: ____% (risk tier confirmed: Y/N)
LOPCYMAT rate: 0% (INPSASEL assessment date: ________)
LOCTI rate: ____% (activity: ______________________)
LOCTI amount: Bs. _____________

SECTION H — WITHHOLDING TAXES ON DIVIDENDS
Dividend declared: Bs. _____________
Tax base (book income minus fiscal income per LIFO): Bs. _____________
Applicable WHT rate: ____% ([ ] Domestic 34% | [ ] Treaty — Country: ____________, Rate: ___%)
Treaty qualification confirmed: [ ] Yes [ ] No
WHT amount: Bs. _____________

SECTION I — PENALTY / INTEREST RISK ASSESSMENT
Filing deadline: ________________
Estimated filing date: ____________
Late filing risk: [ ] None | [ ] Possible — days late: ____
Late payment interest (COT): ____% per annum from ____________
Penalty currency: USD at BCV rate of Bs. ______/USD (COT Art. 91, 2020 reform)

SECTION J — SIGN-OFF
Prepared by: _________________________  Date: ____________
Reviewed by: _________________________ Date: ____________
CPA/EA signature required before filing: [ ] Pending [ ] Obtained
```

## Section 20 — Test Suite

> All tests use UT = Bs. 43.00. Answers are verifiable against the Tarifa schedules above.

### Test 1 — Individual Tarifa No. 1, Basic Bracket Calculation

- **computation** — **Facts:** Individual gross income = 3,500 UT (= Bs. 150,500). Uses desgravamen único (774 UT = Bs. 33,282). No loss carryforward. **Taxable income:** Bs. 150,500 − Bs. 33,282 = Bs. 117,218 (= approximately 2,726 UT) Bracket: 2,500–3,000 UT at 20%, fixed deduction Bs. 10,965. **Expected ISLR:** Bs. 117,218 × 20% − Bs. 10,965 = Bs. 23,444 − Bs. 10,965 = **Bs. 12,479**  _(Test 1)_

### Test 2 — Corporate Tarifa No. 2, Multi-Bracket

- **computation** — **Facts:** Company taxable income = 4,500 UT = Bs. 193,500. No carryforward. Layer 1: 2,000 UT × Bs. 43 = Bs. 86,000 × 15% = Bs. 12,900 Layer 2: 1,000 UT × Bs. 43 = Bs. 43,000 × 22% = Bs. 9,460 Layer 3: 1,500 UT × Bs. 43 = Bs. 64,500 × 34% = Bs. 21,930 **Expected ISLR:** Bs. 12,900 + Bs. 9,460 + Bs. 21,930 = **Bs. 44,290**  _(Test 2)_

### Test 3 — Thin Capitalization Interest Disallowance

- **computation** — **Facts:** Company average equity = Bs. 80,000 (1,860 UT). Average related-party debt = Bs. 120,000 (2,791 UT). Interest rate on related-party debt = 10% per annum. Permitted debt (1:1 ratio) = Bs. 80,000 Excess debt = Bs. 120,000 − Bs. 80,000 = Bs. 40,000 Non-deductible interest = Bs. 40,000 × 10% = Bs. 4,000 Additional ISLR (assuming 34% bracket): Bs. 4,000 × 34% = **Bs. 1,360** **Expected additional ISLR cost: Bs. 1,360**  _(Test 3)_

### Test 4 — Loss Carryforward, 25% Cap Application

- **computation** — **Facts:** Company incurred Bs. 200,000 loss in FY2022. Current year (FY2025) is the last year within the 3-year carryforward window. FY2025 taxable income before loss = Bs. 600,000 (13,953 UT). Company is in the 34% bracket throughout. 25% of Bs. 600,000 = Bs. 150,000 (maximum loss use) Remaining carryforward = Bs. 200,000 > Bs. 150,000 → apply Bs. 150,000 Remaining Bs. 50,000 → EXPIRES (FY2026 would be Year 4, beyond 3-year limit) ISLR without loss: (Bs. 600,000 × 34%) − Bs. 16,125 Wait — use bracket layering: Layer 1: Bs. 86,000 × 15% = Bs. 12,900 Layer 2: Bs. 43,000 × 22% = Bs. 9,460 Layer 3: (Bs. 600,000 − Bs. 129,000) × 34% = Bs. 471,000 × 34% = Bs. 160,140 Total without loss: Bs. 12,900 + Bs. 9,460 + Bs. 160,140 = Bs. 182,500 ISLR with loss (taxable income Bs. 450,000): Layer 1: Bs. 86,000 × 15% = Bs. 12,900 Layer 2: Bs. 43,000 × 22% = Bs. 9,460 Layer 3: (Bs. 450,000 − Bs. 129,000) × 34% = Bs. 321,000 × 34% = Bs. 109,140 Total with loss: Bs. 12,900 + Bs. 9,460 + Bs. 109,140 = Bs. 131,500 **Expected ISLR saving from loss carryforward: Bs. 182,500 − Bs. 131,500 = Bs. 51,000** **Expired loss: Bs. 50,000 (wasted)**  _(Test 4)_

### Test 5 — Dividend Withholding: Domestic vs. Treaty

- **computation** — **Facts:** Venezuelan C.A. distributes Bs. 86,000 (2,000 UT) to a Spanish corporate parent qualifying for the 0% treaty rate on dividends. Domestic rate: 34% → WHT = Bs. 86,000 × 34% = Bs. 29,240 Treaty rate (Spain, 0%): WHT = Bs. 0 **Expected saving from treaty: Bs. 29,240** **Net received by Spanish parent: Bs. 86,000 (vs. Bs. 56,760 without treaty)**  _(Test 5)_

### Test 6 — Desgravamen Comparison

- **computation** — **Facts:** Individual with gross income = 5,000 UT (Bs. 215,000). Qualifying itemized expenses: - Medical expenses: Bs. 20,000 - Insurance premiums: Bs. 5,000 - Mortgage interest: Bs. 43,000 (at the 1,000 UT cap exactly) - Education: Bs. 0 - Rent: N/A (owns home) Total itemized: Bs. 68,000 (= 1,581 UT) Standard desgravamen: 774 UT = Bs. 33,282 Itemized exceeds standard by Bs. 34,718 (807 UT) → **use itemized** Taxable income (itemized): Bs. 215,000 − Bs. 68,000 = Bs. 147,000 (= 3,419 UT) Bracket: 3,000–4,000 UT at 24%, fixed deduction Bs. 16,125 ISLR = Bs. 147,000 × 24% − Bs. 16,125 = Bs. 35,280 − Bs. 16,125 = Bs. 19,155 Taxable income (standard): Bs. 215,000 − Bs. 33,282 = Bs. 181,718 (= 4,226 UT) Bracket: 4,000–6,000 UT at 29%, fixed deduction Bs. 24,725 ISLR = Bs. 181,718 × 29% − Bs. 24,725 = Bs. 52,698 − Bs. 24,725 = Bs. 27,973 **Expected saving from itemizing: Bs. 27,973 − Bs. 19,155 = Bs. 8,818**  _(Test 6)_

## Section 21 — Prohibitions

**Prohibitions Table**  _(Section 21)_

| Prohibited Action | Reason |
| --- | --- |
| Advising clients to structure transactions solely to create artificial ISLR losses | Economic substance doctrine; SENIAT challenge risk; potential evasion charges under COT |
| Using UT-denominated figures without confirming the current UT value from SENIAT | Hyperinflationary environment makes stale bolivar figures materially misleading |
| Recommending treaty holding structures without confirming genuine commercial substance | Anti-abuse provisions in Venezuelan treaties and SENIAT enforcement; principal purpose test applied |
| Claiming desgravamen detallado for expenses paid to foreign-domiciled entities | ISLR Law requires payment to Venezuelan-domiciled entities for itemized deductions |
| Carrying forward inflation/monetary correction losses | ISLR Law explicitly prohibits this; such losses expire in the year generated |
| Applying the thin-cap exception to what is economically a related-party loan routed through a third-party bank | SENIAT has challenged back-to-back arrangements; substance-over-form principle applies |
| Computing penalties in UT | COT 2020 reform (Art. 91) denominates penalties in USD at the BCV official rate; using UT gives the wrong answer |
| Recommending SEZ incentives without current Ministry of Finance certification | Incentives require annual Resolution 015-25 certification; uncertified companies receive no refund |
| Advising reliance on the export drawback program | PwC (January 2026) states this is "not currently being applied in practice" |
| Providing definitive advice on the January 2026 Hydrocarbons Law Reform for existing petroleum contracts | 180-day transition period ongoing; requires specialist and engagement with Ministry of Hydrocarbons |

## Section 22 — Annual Tax Planning Calendar

**Annual Tax Planning Calendar Table**  _(Section 22)_

| Month | Action |
| --- | --- |
| January | Confirm new UT value if SENIAT has issued an adjustment ruling. Check for Special Taxpayer calendar (SNAT/2025/000091 for FY2026). Begin assembling FY prior-year income and expense records. |
| February | Review desgravamen único vs. itemized comparison using FY prior-year receipts. Confirm BCV rate for penalty risk assessment. |
| March | **31 March: ISLR annual declaration due for individuals.** File on time; late filing triggers USD-denominated penalties under COT Art. 91 2020 reform. Pay 1st instalment if applicable. |
| April | 2nd instalment of ISLR (due 20 days after the March 31 deadline). Review IVSS risk classification with INPSASEL; initiate reclassification if safety improvements made. |
| May | 3rd instalment of ISLR (due 40 days after the March 31 deadline). Mid-year income projection for thin-capitalization monitoring (average debt-to-equity check). |
| June | Verify current UT value (SENIAT ruling often issued mid-year). Check Decree 5,146 VAT import exemption expiry (June 30, 2026 for qualifying importers). |
| July | VAT exemption suspension (Decree 5,145) operational since July 5, 2025 — confirm import VAT status for basic goods. Expanded VAT withholding rules (SNAT/2025/000054) operational since August 2025; verify withholding agent status. |
| August | Review LOCTI payments year-to-date. Confirm BCV-based threshold test monthly. Payroll audit: verify IVSS, FAOV, INCES filings. |
| September | Assess loss carryforward position: is FY[3 years ago] loss at risk of expiry? Accelerate profitability recognition if needed to absorb expiring loss within 25% annual cap. |
| October | Year-end planning: assess whether itemized deductions will exceed 774 UT. Schedule any remaining qualifying expenditure (insurance renewals, medical procedures) before December 31. |
| November | Thin-capitalization final check: year-end equity vs. related-party debt average. Capitalize excess related-party loans if needed before December 31. |
| December | **December 31:** Close fiscal year. Confirm ISAE receipts from all municipalities for ISLR deduction documentation. Review cryptocurrency positions: market values at December 31 needed for ISLR computation. Confirm SEZ certification status if applicable. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Venezuela's tax environment is subject to rapid change due to hyperinflation, frequent legislative reforms, and administrative rulings. All monetary figures expressed in bolivars (Bs./VES) are derived from the 2025 Tax Unit value of Bs. 43.00 (SNAT/2025/000048) and will become inaccurate when the UT value is next adjusted by SENIAT.

Penalty amounts under COT 2020 are denominated in USD at the BCV official rate, not UT. Confirm the BCV rate at the time of any penalty computation.

Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Venezuelan professional (contador público colegiado or abogado tributarista registered with SENIAT) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
