---
name: bolivia-payroll
description: Use this skill whenever asked about Bolivia payroll processing for employed (dependent) persons. Trigger on phrases like "Bolivia payroll", "planilla Bolivia", "RC-IVA", "Regimen Complementario al IVA", "retencion RC-IVA", "Form 608", "Formulario 608", "Form 110", "Formulario 110", "Form 610", "aporte laboral", "aporte patronal", "Gestora Publica", "AFP Bolivia", "Caja Nacional de Salud", "CNS", "riesgo comun", "riesgo profesional", "aporte solidario", "Aporte Nacional Solidario", "ANS", "aguinaldo", "segundo aguinaldo", "indemnizacion", "desahucio", "salario minimo nacional", "SMN Bolivia", "total ganado", "descuentos planilla Bolivia", "net salary Bolivia", "gross to net Bolivia", "withholding Bolivia", or any question about computing employee pay, RC-IVA withholding, or social/pension contributions for Bolivia-based employees. This skill covers RC-IVA (13%) wage withholding via the employer as agente de retencion, employee pension-side contributions (Aporte Laboral 12.71%), the Aporte Nacional Solidario, employer social charges (Aporte Patronal 17.21% general / 19.51% mining), the minimum wage (SMN), statutory bonuses (aguinaldo), severance, and filing obligations. ALWAYS read this skill before processing any Bolivia payroll.
version: 0.1
jurisdiction: BO
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bolivia Payroll

## Bolivia Payroll Skill v0.1

**Tier 2 (research-verified).** The RC-IVA 13% flat rate, the employee Aporte Laboral (12.71%: 10% vejez + 1.71% riesgo comun + 0.50% comision Gestora + 0.50% aporte solidario), the 60-SMN pension cap, the Aporte Nacional Solidario brackets (1.15% / 5.74% / 11.48% above Bs 13,000 / Bs 25,000 / Bs 35,000) and the employer Aporte Patronal (17.21% general / 19.51% mining) are taken from PwC Worldwide Tax Summaries (Bolivia) and corroborated by Bolivian payroll/advisory guides (Planifica, Bolivia Impuestos, TopTrabajos). The flat 13% RC-IVA and the agente-de-retencion mechanism rest on Ley N° 843 (Arts. 19-36) and DS 21531; the ANS brackets and the 3.5% Aporte Patronal Solidario rest on Ley N° 1582 (1 Oct 2024). The 2025 SMN (Bs 2,750) is from DS 5383 (1 May 2025); the 2026 SMN (Bs 3,300) is from DS 5516 (Jan 2026). **Several official SIN/SIAT and MEFP pages repeatedly failed TLS verification or returned 403 in the research environment, so secondary (Big-4 / Bolivian advisory) sources were relied upon and must be re-verified against the authority before publication.** Figures carry **[RESEARCH GAP — reviewer to confirm]** markers where the primary authority figure could not be pinned to a single fixed published value (notably the exact DS 5383 presumed-VAT-credit change, the aguinaldo RC-IVA treatment, and whether the ANS is deductible from the RC-IVA base). Confidence: **medium**.

## Section 1 -- Quick Reference

**Section 1 Quick Reference fields**

| Field | Value |
| --- | --- |
| Country | Bolivia (Estado Plurinacional de Bolivia) |
| Currency | BOB (boliviano, Bs) only |
| Standard pay frequency | Monthly (mensual) |
| Tax year | Calendar year (1 January -- 31 December); RC-IVA withholding is monthly |
| Personal income tax | **YES** — RC-IVA (Regimen Complementario al IVA), a flat 13% on individuals' income including salaried/dependent workers (Ley N° 843, Arts. 19+). For dependent employees the employer withholds it monthly. |
| Tax authority | Servicio de Impuestos Nacionales (SIN) — impuestos.gob.bo; RC-IVA filed via the SIAT portal (siatinfo.impuestos.gob.bo) |
| Social security / pension authority | Gestora Publica de la Seguridad Social de Largo Plazo (gestora.bo) — long-term (pension) contributions; Caja Nacional de Salud (CNS) — short-term health |
| Labor / minimum wage authority | Ministerio de Trabajo, Empleo y Prevision Social (mintrabajo.gob.bo) |
| Key legislation | Ley N° 843 (Texto Ordenado), Arts. 19-36 — RC-IVA; DS 21531 (reglamento RC-IVA); DS 5383 of 1 May 2025 (SMN Bs 2,750); Ley N° 065 (Ley de Pensiones); Ley N° 1582 of 1 Oct 2024 (ANS brackets + 3.5% Aporte Patronal Solidario); DS 5516 of Jan 2026 (SMN Bs 3,300); Ley N° 2492 (Codigo Tributario) — penalties |
| Filing portal | SIAT (siatinfo.impuestos.gob.bo) — RC-IVA Forms 608 / 610; "Mis Facturas" app — Form 110. Gestora Publica / CNS planillas — respective portals |
| RC-IVA non-taxable minimum (2025) | 2 SMN = Bs 5,500/month (2 x Bs 2,750) (Ley 843; DS 5383) |
| RC-IVA non-taxable minimum (2026) | 2 SMN = Bs 6,600/month (2 x Bs 3,300) (DS 5516) |
| Validated by | Pending -- requires sign-off by a Bolivian reviewer (contador / auditor) |
| Skill version | 0.1 |

**Headline rates (2025)**  _(PwC Worldwide Tax Summaries (Bolivia); Ley 843; Ley 1582)_

| Item | Employee | Employer |
| --- | --- | --- |
| RC-IVA (personal income tax, withheld) | 13% flat on net taxable base (see Section 2) | -- (employer is only the agente de retencion) |
| Old-age pension (Aporte de Vejez) | 10.00% | -- |
| Riesgo Comun / Riesgo Profesional | 1.71% | 1.71% |
| Comision de administracion (Gestora) | 0.50% | -- |
| Aporte Solidario del Asegurado | 0.50% | -- |
| Caja Nacional de Salud (health) | -- | 10.00% |
| Aporte Patronal Pro-Vivienda (housing) | -- | 2.00% |
| Aporte Patronal Solidario (APS) | -- | 3.50% |
| **Total employee social (Aporte Laboral)** | **12.71%** | -- |
| **Total employer social (Aporte Patronal), general** | -- | **17.21%** |
| **Total employer social (Aporte Patronal), mining** | -- | **19.51%** |
| Aporte Nacional Solidario (ANS, employee) | marginal 1.15% / 5.74% / 11.48% above Bs 13,000 / 25,000 / 35,000 | -- |

- **Pension cap and RC-IVA base note** — Employee pension contributions (Aporte Laboral 12.71%) and old-age/riesgo-comun branches are capped at 60 SMN/month (Bs 165,000 in 2025 = 60 x Bs 2,750; Bs 198,000 in 2026 = 60 x Bs 3,300). The RC-IVA base is computed on total ganado less the deductible employee pension contributions less 2 SMN less VAT credits.  _(PwC; Ley 065)_

## Section 2 -- Personal Income Tax Withholding (RC-IVA, the agente-de-retencion mechanism)

Bolivia **does** have a personal income tax for salaried workers: the **Regimen Complementario al IVA (RC-IVA)**, a **flat 13%** levied on individuals' income (Ley N° 843, Arts. 19-36). For **dependent employees** the employer is the **agente de retencion** — it computes and withholds RC-IVA monthly, files a consolidated planilla tributaria, and remits via **Form 608**. There is **no joint filing**; married couples file separately. (Sources: Ley 843; DS 21531; PwC Worldwide Tax Summaries.)

### RC-IVA Computation Method (dependent employees, monthly)

- **RC-IVA computation steps** — 1. Start from total ganado (gross monthly earnings). 2. Subtract the deductible employee pension contributions (Aporte Laboral, 12.71%) — Section 3. 3. Subtract the non-taxable minimum = 2 SMN/month (Bs 5,500 in 2025; Bs 6,600 in 2026). 4. Apply 13% to the remaining base → gross RC-IVA. 5. Offset against the gross RC-IVA the employee's VAT credit: (a) the presumed VAT-credit allowance, plus (b) 13% of the VAT on invoices (facturas) the employee submits via Form 110. 6. The net of step 5 (if positive) is the RC-IVA withheld; if the credit exceeds the gross RC-IVA, no RC-IVA is withheld and the surplus credit carries forward as a saldo a favor del dependiente.  _(Ley 843; DS 21531; PwC)_
- **Non-taxable minimum (paso 3)** — 2 SMN/month = Bs 5,500 in 2025 (2 x Bs 2,750) and Bs 6,600 in 2026 (2 x Bs 3,300)  _(Ley 843; DS 5383; DS 5516)_
- **Presumed VAT credit (paso 5a)** — Historically the presumed credit equalled 13% of 2 SMN, which together with the 2-SMN minimum made the effective RC-IVA exemption roughly 4 SMN of gross salary. DS 5383 (1 May 2025) reportedly reduced the presumed-credit reference from 2 SMN to 1 SMN, lowering the threshold so workers earning above ~Bs 9,400/month may owe RC-IVA unless they submit enough invoices. [RESEARCH GAP — reviewer to confirm the exact wording of DS 5383 on the presumed VAT-credit allowance against the decree itself; multiple advisory sources report the 2-SMN→1-SMN reduction but it was not confirmed from the Gaceta Oficial.]  _(advisory summaries — Rigoberto Paredes; Bolivia Impuestos)_

> Conservative default: until DS 5383 is confirmed, use the higher RC-IVA liability (presumed credit = 13% of 1 SMN) for affected mid-earners and flag for the reviewer.

### Flat rate

**RC-IVA flat rate table**  _(Ley 843, Arts. 19-36)_

| Tax | Type | Rate | Base |
| --- | --- | --- | --- |
| RC-IVA (personal income tax) | Flat | **13%** | Total ganado − employee pension contributions (12.71%) − 2 SMN minimum − VAT credits (presumed + submitted facturas). (Ley 843, Arts. 19-36.) |

- **No progressive scale** — There is no progressive scale: RC-IVA is a single 13% rate. The exemption is delivered through the 2-SMN minimum and the VAT-credit offset, not a 0% band, so for most low/mid earners the effective RC-IVA is nil once the minimum and presumed credit are applied.  _(PwC; Ley 843)_

### Direct / independent RC-IVA taxpayers

- **Contribuyentes directos routing** — Non-dependent persons (e.g. directors' fees, rental income, salaried individuals paid by a foreign employer) are contribuyentes directos and self-declare RC-IVA on Form 610 rather than being withheld through payroll. Route these out of the dependent-payroll flow (R-BO-P-2).  _(SIAT; SIN)_

## Section 3 -- Social Security -- Employee Deductions (Aporte Laboral)

The employee bears the pension-side contributions (collected by the Gestora Publica) plus, for higher earners, the Aporte Nacional Solidario. Health (CNS) is employer-only (Section 4). All are computed on total ganado (gross). (Sources: PwC Worldwide Tax Summaries; Planifica; TopTrabajos; Ley 065; Ley 1582.)

### Employee Contribution Rates (2025)

**Employee Contribution Rates (2025)**  _(PwC Worldwide Tax Summaries; Ley 065; Planifica)_

| Contribution (Spanish) | Rate | Base | Destination / Source |
| --- | --- | --- | --- |
| Aporte de Vejez (old-age pension) | 10.00% | Total ganado (capped at 60 SMN) | Individual pension account — Gestora Publica (PwC; Ley 065) |
| Prima de Riesgo Comun (disability/death) | 1.71% | Total ganado (capped at 60 SMN) | Gestora Publica (PwC) |
| Comision de administracion (Gestora) | 0.50% | Total ganado | Gestora Publica admin fee (PwC; Planifica) |
| Aporte Solidario del Asegurado | 0.50% | Total ganado | Fondo Solidario / Pension Solidaria de Vejez (PwC; Planifica) |
| **TOTAL employee pension-side (Aporte Laboral)** | **12.71%** | Total ganado | = 10.00 + 1.71 + 0.50 + 0.50; **deductible from the RC-IVA base** (PwC) |

Arithmetic check: 10.00 + 1.71 + 0.50 + 0.50 = 12.71%. ✓

### Aporte Nacional Solidario (ANS) -- employee, post-Ley 1582 (effective 1 Oct 2024)

- **ANS applicability and history** — The ANS applies only to total ganado above Bs 13,000/month, with cumulative marginal rates (the rates stack on each successive slice). Pre-Ley 1582 the rates were 1% / 5% / 10%; Ley 1582 raised them.  _(Ley N° 1582; MEFP; Bolivia Impuestos)_

**ANS marginal bracket table**  _(Ley 1582; MEFP)_

| Slice of total ganado | Marginal rate applied to the slice | Source |
| --- | --- | --- |
| Portion from Bs 13,000.01 to Bs 25,000 | **1.15%** | Ley 1582; MEFP |
| Portion from Bs 25,000.01 to Bs 35,000 | **1.15% + 5.74% = 6.89%** | Ley 1582; MEFP |
| Portion above Bs 35,000 | **1.15% + 5.74% + 11.48% = 18.37%** | Ley 1582; MEFP |

> Computation: the three rates are additive on each band (the standard Bolivian ANS method). Example for Bs 30,000: (25,000 − 13,000) x 1.15% + (30,000 − 25,000) x 6.89% = 138.00 + 344.50 = Bs 482.50. [RESEARCH GAP — reviewer to confirm the precise marginal-vs-stacked computation with a worked example against the MEFP/SIN; the data describes the rates as cumulative marginal across Bs 13,000 / 25,000 / 35,000.]

> [RESEARCH GAP — reviewer to confirm whether the ANS is deductible from the RC-IVA base.] The 12.71% Aporte Laboral is confirmed deductible (PwC); the worked examples below treat the ANS as a further deductible employee social contribution but flag it for the reviewer.

### Pension contribution ceiling (tope)

- **Pension contribution ceiling** — Pension (vejez and riesgo comun) contributions are levied up to a cap of 60 SMN per month = Bs 165,000 in 2025 (60 x Bs 2,750) and Bs 198,000 in 2026 (60 x Bs 3,300). PwC cites the cap as ~USD 28,450. [RESEARCH GAP — reviewer to confirm whether the 0.50% comision, the 0.50% aporte solidario and the ANS are also subject to the 60-SMN cap or computed on uncapped total ganado.]  _(PwC; Ley 065)_

## Section 4 -- Social Security -- Employer Contributions (Aporte Patronal)

The employer pays the short-term health contribution (CNS), the work-accident branch, the housing fund and the Aporte Patronal Solidario — all employer-only, all on total ganado. The employer does not pay RC-IVA (it only withholds it) and does not pay the employee pension branches. (Sources: PwC Worldwide Tax Summaries — Corporate, Other taxes; Planifica; Ley 1582.)

### Employer Contribution Rates (2025)

**Employer Contribution Rates (2025)**  _(PwC; Planifica; Ley 1582)_

| Contribution (Spanish) | Rate | Base | Destination / Notes |
| --- | --- | --- | --- |
| Caja Nacional de Salud (CNS) — short-term health | 10.00% | Total ganado | CNS (or chosen Caja) (PwC; Planifica) |
| Riesgo Profesional (work-accident) | 1.71% | Total ganado | Gestora Publica (PwC) |
| Aporte Patronal Pro-Vivienda (FONVIS / housing) | 2.00% | Total ganado | Housing fund (PwC; Planifica) |
| Aporte Patronal Solidario (APS) | 3.50% | Total ganado | Raised from 3.00% to 3.50% by Ley 1582 (eff. 1 Oct 2024) (Ley 1582; PwC) |
| **TOTAL employer social (Aporte Patronal) — general** | **17.21%** | Total ganado | = 10.00 + 1.71 + 2.00 + 3.50 (PwC) |
| **TOTAL employer social (Aporte Patronal) — mining** | **19.51%** | Total ganado | General 17.21% + ~2.30% mining (PwC) |

Arithmetic check (general): 10.00 + 1.71 + 2.00 + 3.50 = 17.21%. ✓ Mining: 17.21 + 2.30 = 19.51%. ✓

> The employer total moved from 16.71% (3.00% APS) to 17.21% (3.50% APS) under Ley 1582. [RESEARCH GAP — reviewer to confirm the exact effective date for payroll application of the 3.5% APS; some Bolivian payroll guides still quote 16.71%. 17.21% reflects the current 3.5% APS and is the figure used here.]

## Section 5 -- Minimum Wage (SMN), Statutory Bonuses and Reference Items

### Salario Minimo Nacional (SMN) -- full-time monthly

**SMN by year**  _(DS 5383; DS 5516)_

| Year | SMN/month | Source |
| --- | --- | --- |
| 2025 | **Bs 2,750** | DS 5383 (1 May 2025; +10% vs Bs 2,500; basic-salary haber increase 5%, retroactive to 1 Jan 2025) (DS 5383 / Lexivox) |
| 2026 | **Bs 3,300** | DS 5516 (published 13 Jan 2026; +20%, retroactive to 1 Jan 2026) (DS 5516; secondary sources) |

The SMN drives both the RC-IVA non-taxable minimum (2 SMN) and the pension cap (60 SMN), so figures must be updated annually with each salary decree. [RESEARCH GAP — reviewer to confirm the 2026 SMN Bs 3,300 against the Gaceta Oficial; it is reported consistently by multiple secondary sources.]

### Statutory Bonuses and Benefits

**Statutory Bonuses and Benefits table**  _(PwC; Deel; Ministerio de Trabajo; DS 21531; DS 1802)_

| Item (Spanish) | Detail | RC-IVA treatment |
| --- | --- | --- |
| Aguinaldo (Christmas bonus) | Mandatory 13th-month salary (1 monthly salary), payable by ~20 December (Ministerio de Trabajo) | **[RESEARCH GAP — conflicting sources.]** PwC: all bonuses **except** the Christmas bonus are taxed (implying the aguinaldo de Navidad is RC-IVA-exempt per DS 21531); some Bolivian sources list the aguinaldo as taxable. **Reconcile before finalizing.** |
| Segundo Aguinaldo ("Esfuerzo por Bolivia", DS 1802) | Second 13th-month payment, **only** mandatory if national GDP growth exceeds **4.5%** | Not RC-IVA taxed (DS 1802) |
| Indemnizacion (severance) | 1 month salary per year of service (pro-rata after 3 months) | **RC-IVA-exempt** (DS 21531) |
| Desahucio (unjustified-dismissal compensation) | 3 months salary | **RC-IVA-exempt** (DS 21531) |
| Prima anual | 1 month salary when the company has profits; employees with 3+ months service | **Taxable** for RC-IVA (Deel; advisory) |
| Vacaciones (annual leave) | 15 working days (1-5 yrs service), 20 (5-10 yrs), 30 (10+ yrs), paid 100% | Paid leave (Deel; Ministerio de Trabajo) |
| Working hours / overtime | Max 8h/day, 48h/week (daytime); overtime surcharge **100%**; max 2 extra hours/day | Labor rule (Ley General del Trabajo; Deel) |

## Section 6 -- Conservative Defaults

When an input is ambiguous, apply the conservative default and flag for the reviewer rather than guessing.

**Conservative Defaults table**

| Ambiguity | Conservative Default |
| --- | --- |
| RC-IVA base | Treat RC-IVA as **13%** of (total ganado − 12.71% employee pension contributions − 2 SMN minimum − VAT credits). If invoice (factura) data is unavailable, assume **no VAT credit beyond the presumed allowance**, which maximizes the withholding. |
| DS 5383 presumed-credit change | Until the exact DS 5383 text is confirmed, conservatively assume the **higher** RC-IVA liability (presumed credit reduced to **1 SMN**, i.e. 13% x 1 SMN) for affected earners and flag for accountant review. Trigger R-BO-P-7. |
| Employer social cost | Use **17.21%** of total ganado for general employers (**19.51%** for mining). Add aguinaldo, an indemnizacion provision, and pro-vivienda when budgeting fully-loaded cost. |
| Aporte Nacional Solidario | Apply **only** if monthly total ganado exceeds **Bs 13,000**; compute **cumulatively** across the 1.15% / 6.89% / 18.37% effective bands (additive 1.15% + 5.74% + 11.48%). |
| ANS deductibility | Treat the ANS as a deductible employee social contribution for the RC-IVA base, but **flag** — confirm with the reviewer (R-BO-P-8). |
| Pension cap | Apply the **60-SMN** cap (Bs 165,000/month in 2025; Bs 198,000 in 2026) to vejez and riesgo comun; flag whether comision/aporte solidario/ANS are also capped. |
| SMN / year | Use **Bs 2,750** for 2025 pay periods and **Bs 3,300** for 2026 pay periods; never mix. The SMN drives the 2-SMN minimum and the 60-SMN cap. |
| Aguinaldo RC-IVA | Treat the **Christmas aguinaldo** as RC-IVA-exempt (PwC view) but **flag** the conflicting Bolivian-source view; treat indemnizacion and desahucio as RC-IVA-exempt (DS 21531). |
| Currency | All amounts in **BOB (Bs)**. Do not convert to USD in computations. |

## Section 7 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — For each employee: total ganado (gross monthly earnings), pay period, the employer's NIT (Numero de Identificacion Tributaria), and the year (for the SMN). Whether the worker is a dependent employee (vs contribuyente directo).
- **Recommended** — The employee's Form 110 invoice (factura) total for the month (to compute the VAT credit), the last digit of the employer's NIT (for the Form 608 due date), whether the employer is mining (19.51% vs 17.21%), date of hire (for aguinaldo/indemnizacion pro-rata), and any bonuses/prima.
- **Ideal** — The full planilla tributaria and planilla de aportes (Gestora/CNS), prior Form 608 filings, prior-month cumulative RC-IVA saldos a favor del dependiente, and the employee's pension/CNS registration.

### Bolivia-Specific Refusal Catalogue

- **R-BO-P-1 — No total ganado** — Trigger: gross monthly earnings are not provided. Message: "RC-IVA withholding and social contributions are computed on total ganado (gross). Provide the gross monthly earnings before running payroll."
- **R-BO-P-2 — Contribuyente directo / non-dependent** — Trigger: the person is independent, a director on fees, a landlord, or salaried by a foreign employer. Message: "Non-dependent persons self-declare RC-IVA on Form 610 (contribuyente directo) rather than through employer withholding. Use the direct-RC-IVA / income-tax flow, not this dependent-payroll skill."
- **R-BO-P-3 — Cross-border / expat / treaty** — Trigger: a posted worker, treaty question, or split-residence employee. Message: "Cross-border social security and RC-IVA treatment require specialist advice; route through a Bolivian reviewer."
- **R-BO-P-4 — Benefits in kind / equity** — Trigger: company car, housing, stock options or other non-cash benefits. Message: "Benefit-in-kind treatment for RC-IVA and contributions is not detailed here; route through a Bolivian reviewer."
- **R-BO-P-5 — Termination / severance** — Trigger: indemnizacion, desahucio, or a final-settlement (finiquito) calculation. Message: "Severance (indemnizacion 1 month/year), desahucio (3 months) and the finiquito have specific labor and RC-IVA-exempt treatment (DS 21531); do not run through standard monthly withholding — flag for the reviewer."
- **R-BO-P-6 — Aguinaldo / segundo aguinaldo** — Trigger: a 13th-month or second-aguinaldo computation. Message: "The aguinaldo (by ~20 December) and the segundo aguinaldo (only if GDP growth > 4.5%) have specific timing and RC-IVA treatment; flag for the reviewer (R-BO-P-6)."
- **R-BO-P-7 — DS 5383 presumed-credit uncertainty** — Trigger: a mid-earner (above ~Bs 9,400/month) where the presumed VAT credit determines whether RC-IVA is due. Message: "The exact DS 5383 presumed-VAT-credit reference (2 SMN vs 1 SMN) is unconfirmed; the conservative (1-SMN) figure is used. Confirm DS 5383 before relying on the result."
- **R-BO-P-8 — ANS deductibility / computation** — Trigger: total ganado above Bs 13,000 where the ANS affects the RC-IVA base. Message: "Whether the Aporte Nacional Solidario is deductible from the RC-IVA base, and the exact marginal computation, require reviewer confirmation."

## Section 8 -- Transaction / Payment Pattern Library

Match by case-insensitive substring. Spanish variants treated as their English equivalent. Most specific match wins. Amounts in BOB (Bs).

### 8.1 Salary credits (to the employee's account)

**Salary credit patterns**

| Pattern | Classification |
| --- | --- |
| SUELDO, SALARIO, HABER, PAGO PLANILLA, REMUNERACION | Net salary payment |
| EMPLEADOR [name] TRANSFERENCIA, ABONO SUELDO | Net salary payment |
| AGUINALDO, AGUINALDO NAVIDAD | Aguinaldo (13th month, ~20 December) |
| SEGUNDO AGUINALDO, ESFUERZO POR BOLIVIA | Segundo aguinaldo (only if GDP growth > 4.5%) |
| PRIMA, PRIMA ANUAL | Prima (taxable for RC-IVA) |
| INDEMNIZACION, DESAHUCIO, FINIQUITO | Termination payment — flag R-BO-P-5 (RC-IVA-exempt under DS 21531) |
| HORAS EXTRAS, RECARGO | Overtime pay |

### 8.2 Employer statutory debits (to the authorities)

**Employer statutory debit patterns**

| Pattern | Classification |
| --- | --- |
| RC-IVA, FORM 608, FORMULARIO 608, IMPUESTOS NACIONALES, SIN, SIAT, RETENCION | RC-IVA withholding remittance to the SIN (Form 608) |
| GESTORA, GESTORA PUBLICA, APORTE LABORAL, APORTE PATRONAL, AFP | Pension / Gestora Publica contributions (employee + employer) |
| CNS, CAJA NACIONAL DE SALUD, CAJA SALUD, SEGURO SALUD | Health contribution (employer 10%, CNS) |
| RIESGO PROFESIONAL, RIESGO COMUN | Riesgo branches (within Gestora planilla) |
| PRO-VIVIENDA, FONVIS, VIVIENDA | Aporte Patronal Pro-Vivienda (housing 2%) |
| APORTE SOLIDARIO, APORTE NACIONAL SOLIDARIO, ANS, APS | Solidario contributions (employee aporte solidario / ANS; employer APS) |

### 8.3 Net wage disbursement (employer's bank)

**Net wage disbursement patterns**

| Pattern | Classification |
| --- | --- |
| PLANILLA SUELDOS, PAGO DE HABERES, NOMINA, PAYROLL | Salary disbursement to employees |
| PLANILLA TRIBUTARIA | Consolidated RC-IVA / contributions run |

### 8.4 Exclusions / not payroll

**Exclusion patterns**

| Pattern | Classification |
| --- | --- |
| TRANSFERENCIA INTERNA, TRASPASO PROPIO | Internal movement — exclude |
| DIVIDENDO, DIVIDENDOS | Out of scope — exclude |
| PRESTAMO, ANTICIPO | Loan / advance principal — exclude (not salary) |
| INTERESES | Interest — exclude |

## Section 9 -- Worked Examples

All figures use the **2025** parameter set unless stated: **SMN Bs 2,750**; 2-SMN RC-IVA minimum **Bs 5,500**; 60-SMN pension cap **Bs 165,000/month**; presumed VAT credit conservatively **13% x 1 SMN = Bs 357.50** (DS 5383 conservative default). RC-IVA shown assumes the employee submits **no facturas** via Form 110 (the conservative, maximum-withholding case). Employer on-cost uses **17.21%** (general). All amounts in BOB (Bs). Withholding is **illustrative** — a Bolivian reviewer must confirm the DS 5383 presumed-credit and the aguinaldo/ANS treatment.

### Example 1 — Minimum-wage employee (Bs 2,750/month, 2025)

**Bank statement line (employer debit):**
`30/06/2025 ; PLANILLA SUELDOS - J. MAMANI ; DEBITO ; Sueldo junio ; -2.400,47 ; Bs`

**Reasoning:**
Total ganado Bs 2,750. Employee pension (Aporte Laboral) 12.71% x 2,750 = **Bs 349.53**. RC-IVA base = 2,750 − 349.53 − 5,500 (2 SMN) = **negative** → RC-IVA = **Bs 0**. ANS: 2,750 < 13,000 → **Bs 0**. Net = 2,750 − 349.53 = **Bs 2,400.47**.

**Example 1 table**

| Item | Base | Rate | Amount (Bs) |
| --- | --- | --- | --- |
| Total ganado | -- | -- | 2,750.00 |
| Employee Aporte Laboral | 2,750.00 | 12.71% | 349.53 |
| RC-IVA (base ≤ 0) | -- | 13% | 0.00 |
| ANS (below Bs 13,000) | -- | -- | 0.00 |
| **Net pay** | -- | -- | **2,400.47** |
| Employer Aporte Patronal | 2,750.00 | 17.21% | 473.28 |

### Example 2 — Low earner, RC-IVA still nil (Bs 8,000/month, 2025, no facturas)

**Bank statement line (employee credit):**
`30/06/2025 ; EMPLEADOR SRL TRANSFERENCIA ; CREDITO ; Sueldo junio ; +6.983,20 ; Bs`

**Reasoning:**
Total ganado Bs 8,000. Aporte Laboral 12.71% x 8,000 = **Bs 1,016.80**. RC-IVA base = 8,000 − 1,016.80 − 5,500 = **Bs 1,483.20**; gross RC-IVA = 13% x 1,483.20 = **Bs 192.82**. Presumed VAT credit (Bs 357.50) **exceeds** the gross RC-IVA → RC-IVA withheld = **Bs 0**; surplus credit Bs 164.68 carries forward. ANS: 8,000 < 13,000 → Bs 0. Net = 8,000 − 1,016.80 = **Bs 6,983.20**.

**Example 2 table**

| Item | Base | Rate | Amount (Bs) |
| --- | --- | --- | --- |
| Total ganado | -- | -- | 8,000.00 |
| Employee Aporte Laboral | 8,000.00 | 12.71% | 1,016.80 |
| RC-IVA base | -- | -- | 1,483.20 |
| Gross RC-IVA | 1,483.20 | 13% | 192.82 |
| Less presumed VAT credit | -- | -- | (357.50) |
| RC-IVA withheld (floored at 0) | -- | -- | 0.00 |
| **Net pay** | -- | -- | **6,983.20** |

### Example 3 — Mid earner, RC-IVA now due (Bs 12,000/month, 2025, no facturas)

**Bank statement line (employer debit, RC-IVA remittance):**
`16/07/2025 ; IMPUESTOS NACIONALES RC-IVA F608 ; DEBITO ; Retencion junio ; -289,22 ; Bs`

**Reasoning:**
Total ganado Bs 12,000. Aporte Laboral 12.71% x 12,000 = **Bs 1,525.20**. RC-IVA base = 12,000 − 1,525.20 − 5,500 = **Bs 4,974.80**; gross RC-IVA = 13% x 4,974.80 = **Bs 646.72**. Presumed VAT credit Bs 357.50 → RC-IVA withheld = 646.72 − 357.50 = **Bs 289.22** (employee submits no facturas; submitting facturas worth ≥ Bs 2,224 of VAT-inclusive purchases would extinguish it). ANS: 12,000 < 13,000 → Bs 0. Net = 12,000 − 1,525.20 − 289.22 = **Bs 10,185.58**.

**Example 3 table**

| Item | Base | Rate | Amount (Bs) |
| --- | --- | --- | --- |
| Total ganado | -- | -- | 12,000.00 |
| Employee Aporte Laboral | 12,000.00 | 12.71% | 1,525.20 |
| RC-IVA base | -- | -- | 4,974.80 |
| Gross RC-IVA | 4,974.80 | 13% | 646.72 |
| Less presumed VAT credit | -- | -- | (357.50) |
| RC-IVA withheld | -- | -- | 289.22 |
| **Net pay** | -- | -- | **10,185.58** |
| Employer Aporte Patronal | 12,000.00 | 17.21% | 2,065.20 |

> Under the **historical** presumed credit (13% x 2 SMN = Bs 715.00) the gross RC-IVA Bs 646.72 would have been fully covered → Bs 0 withheld. This example shows why the DS 5383 change (R-BO-P-7) matters for mid-earners.

### Example 4 — High earner, ANS applies (Bs 30,000/month, 2025, no facturas)

**Bank statement line (employer debit, Gestora):**
`05/07/2025 ; GESTORA PUBLICA APORTE LABORAL ; DEBITO ; Aportes junio ; -4.295,50 ; Bs`

**Reasoning:**
Total ganado Bs 30,000 (below the 60-SMN cap Bs 165,000, so no cap effect). Aporte Laboral 12.71% x 30,000 = **Bs 3,813.00**. ANS (cumulative marginal): slice 13,000–25,000 = 12,000 x 1.15% = **138.00**; slice 25,000–30,000 = 5,000 x 6.89% = **344.50**; ANS = **Bs 482.50**. Total employee social = 3,813.00 + 482.50 = **Bs 4,295.50**. RC-IVA base = 30,000 − 4,295.50 − 5,500 = **Bs 20,204.50**; gross RC-IVA = 13% x 20,204.50 = **Bs 2,626.59**; less presumed credit Bs 357.50 → RC-IVA withheld = **Bs 2,269.09**. Net = 30,000 − 4,295.50 − 2,269.09 = **Bs 23,435.41**.

**Example 4 table**

| Item | Base | Rate | Amount (Bs) |
| --- | --- | --- | --- |
| Total ganado | -- | -- | 30,000.00 |
| Employee Aporte Laboral | 30,000.00 | 12.71% | 3,813.00 |
| ANS (13k–25k @ 1.15% + 25k–30k @ 6.89%) | -- | marginal | 482.50 |
| RC-IVA base (after social + 2 SMN) | -- | -- | 20,204.50 |
| Gross RC-IVA | 20,204.50 | 13% | 2,626.59 |
| Less presumed VAT credit | -- | -- | (357.50) |
| RC-IVA withheld | -- | -- | 2,269.09 |
| **Net pay** | -- | -- | **23,435.41** |
| Employer Aporte Patronal | 30,000.00 | 17.21% | 5,163.00 |

> **[RESEARCH GAP]** This example treats the ANS as deductible from the RC-IVA base (R-BO-P-8). If the ANS is **not** deductible, the RC-IVA base would be 30,000 − 3,813.00 − 5,500 = 20,687.00 and gross RC-IVA = Bs 2,689.31 (withheld 2,331.81). Reviewer to confirm.

### Example 5 — Pension cap binds (Bs 200,000/month, 2025)

Total ganado Bs 200,000 exceeds the 60-SMN pension cap **Bs 165,000** (60 x Bs 2,750). The capped pension branches (vejez 10% + riesgo comun 1.71% = 11.71%) apply to **Bs 165,000**, not Bs 200,000. The comision (0.50%), aporte solidario (0.50%) and ANS may be on uncapped total ganado **[RESEARCH GAP — confirm which branches the 60-SMN cap covers, R-BO-P-8]**.

**Example 5 table**

| Item | Base | Rate | Amount (Bs) |
| --- | --- | --- | --- |
| Vejez + riesgo comun (capped) | 165,000.00 | 11.71% | 19,321.50 |
| Comision + aporte solidario (cap status to confirm) | 200,000.00 | 1.00% | 2,000.00 |
| **Pension-side subtotal (illustrative)** | -- | -- | **21,321.50** |

### Example 6 — Employer Aporte Patronal remittance (Bs 12,000 employee, general)

**Bank statement line (employer debit):**
`05/07/2025 ; GESTORA + CNS APORTE PATRONAL ; DEBITO ; Aportes junio ; -2.065,20 ; Bs`

**Reasoning:**
Employer Aporte Patronal = 17.21% x total ganado. For Example 3 (Bs 12,000): CNS 10% = Bs 1,200.00; riesgo profesional 1.71% = Bs 205.20; pro-vivienda 2% = Bs 240.00; APS 3.5% = Bs 420.00. Total = 1,200.00 + 205.20 + 240.00 + 420.00 = **Bs 2,065.20** (= 17.21% x 12,000). This is an **employer expense**, separate from the employee Aporte Laboral and the RC-IVA withheld. (A **mining** employer would pay 19.51% = Bs 2,341.20.)

**Example 6 table**

| Component | Base | Rate | Amount (Bs) |
| --- | --- | --- | --- |
| CNS (health) | 12,000.00 | 10.00% | 1,200.00 |
| Riesgo profesional | 12,000.00 | 1.71% | 205.20 |
| Pro-vivienda (housing) | 12,000.00 | 2.00% | 240.00 |
| Aporte Patronal Solidario | 12,000.00 | 3.50% | 420.00 |
| **Total employer (general)** | -- | **17.21%** | **2,065.20** |

## Section 10 -- Tier 1 Rules (deterministic)

- **RC-IVA is flat 13% personal income tax** — RC-IVA is Bolivia's personal income tax, levied at a flat 13% on individuals' income including salaried/dependent workers. There is no progressive scale.  _(Ley N° 843, Arts. 19+)_
- **Employer as agente de retencion** — For dependent employees the employer is the agente de retencion: it deducts the employee pension contributions (12.71%), subtracts a non-taxable minimum of 2 SMN, applies 13%, then offsets the presumed VAT credit plus 13% of the VAT on submitted facturas (Form 110).  _(Ley 843; DS 21531; PwC)_
- **Non-taxable minimum (2 SMN)** — Bs 5,500 in 2025 and Bs 6,600 in 2026; historically the presumed VAT credit (13% of 2 SMN) made the effective exemption ~4 SMN of gross salary.  _(Ley 843; DS 5383; DS 5516)_
- **DS 5383 presumed-VAT-credit reduction** — DS 5383 (1 May 2025) reportedly reduced the presumed-VAT-credit reference from 2 SMN to 1 SMN, raising RC-IVA liability for mid-earners (above ~Bs 9,400/month) unless they submit invoices. [RESEARCH GAP — verify exact wording.]  _(Advisory: Rigoberto Paredes; Bolivia Impuestos)_
- **Employee pension-side contribution (Aporte Laboral)** — 12.71% of total ganado: 10% vejez + 1.71% riesgo comun + 0.50% comision Gestora + 0.50% aporte solidario; capped at 60 SMN and deductible from the RC-IVA base.  _(PwC; Ley 065; Planifica)_
- **Employer social charges (Aporte Patronal)** — 17.21% of total ganado for general employers (19.51% mining): 10% CNS health + 1.71% riesgo profesional + 2% pro-vivienda + 3.5% Aporte Patronal Solidario.  _(PwC; Ley 1582)_
- **Aporte Patronal Solidario increase** — The Aporte Patronal Solidario rose from 3.0% to 3.5% under Ley 1582 (eff. 1 Oct 2024); the employer total moved from 16.71% to 17.21%.  _(Ley 1582; PwC)_
- **Aporte Nacional Solidario (ANS)** — Applies only to total ganado above Bs 13,000/month, cumulative marginal: 1.15% (over Bs 13,000) + 5.74% (over Bs 25,000) + 11.48% (over Bs 35,000); pre-Ley 1582 the rates were 1% / 5% / 10%.  _(Ley 1582; MEFP)_
- **Pension cap** — 60 SMN/month = Bs 165,000 in 2025 (Bs 198,000 in 2026) on vejez and riesgo comun.  _(PwC; Ley 065)_
- **SMN (National Minimum Wage)** — Bs 2,750/month for 2025 (DS 5383, +10%); Bs 3,300/month for 2026 (DS 5516, +20%, retroactive to 1 Jan 2026). The SMN drives both the 2-SMN minimum and the 60-SMN cap.  _(DS 5383; DS 5516)_
- **RC-IVA monthly remittance deadline** — Employers file Form 608 v.4 by the due date set by the last digit of the NIT (NIT ending 0 → day 13, 1 → 14, … 9 → day 22 of the following month); weekend/holiday deadlines roll to the next business day.  _(SIN Calendario Tributario 2025)_
- **Form 110 and Form 610 usage** — Employees claim VAT credits via Form 110 (now through the "Mis Facturas" app under RND 102000000025 / RND 1020-25), submitted monthly to the employer; direct/independent RC-IVA taxpayers use Form 610.  _(SIAT)_
- **Aguinaldo, segundo aguinaldo, indemnizacion, desahucio** — Christmas aguinaldo (1 month salary, payable by ~20 December) is mandatory; the segundo aguinaldo (DS 1802) is only mandatory when GDP growth > 4.5%. Indemnizacion (1 month/year) and desahucio (3 months) are RC-IVA-exempt (DS 21531); the aguinaldo's RC-IVA treatment is unsettled across sources. [RESEARCH GAP.]  _(PwC; DS 21531; DS 1802; Deel)_
- **Penalty for omision de pago** — Penalty for omision de pago is 60% of the unpaid tax (in UFV), reducible to 80% off (pay within 20 days of the Vista de Cargo) or 60% off (before appealing the Resolucion Determinativa); tax debt is indexed to UFV plus interest from the due date.  _(Ley 2492; RND 102200000016)_
- **Contribution base and currency** — Pension/health contributions are computed on total ganado (gross); all amounts are in bolivianos (BOB).

## Section 11 -- Tier 2 Catalogue (reviewer judgement)

Items requiring professional judgement; apply the default and flag the question.

### 11.1 RC-IVA presumed VAT credit (DS 5383)

- **Default and question** — Default: conservative — presumed credit = 13% x 1 SMN (higher liability). Question: "Does DS 5383 (1 May 2025) reduce the presumed VAT-credit reference from 2 SMN to 1 SMN?" — R-BO-P-7. [RESEARCH GAP.]  _(R-BO-P-7)_

### 11.2 Submitted facturas (Form 110)

- **Default and question** — Default: assume no facturas (maximum withholding). Question: "What is the employee's monthly Form 110 invoice total? 13% of it offsets the RC-IVA."

### 11.3 Aguinaldo RC-IVA treatment

- **Default and question** — Default: treat the Christmas aguinaldo as RC-IVA-exempt (PwC) but flag. Question: "Is the aguinaldo de Navidad RC-IVA-exempt (PwC/DS 21531) or taxable (some Bolivian sources)?" — R-BO-P-6. [RESEARCH GAP.]  _(R-BO-P-6)_

### 11.4 ANS deductibility and computation

- **Default and question** — Default: treat the ANS as deductible from the RC-IVA base; compute cumulatively. Question: "Is the ANS deductible from the RC-IVA base, and is the marginal computation stacked (1.15% / 6.89% / 18.37%)?" — R-BO-P-8. [RESEARCH GAP.]  _(R-BO-P-8)_

### 11.5 Pension cap scope

- **Default and question** — Default: apply the 60-SMN cap to vejez and riesgo comun. Question: "Do the 0.50% comision, 0.50% aporte solidario and the ANS also sit under the 60-SMN cap, or on uncapped total ganado?" [RESEARCH GAP.]

### 11.6 Mining vs general employer

- **Default and question** — Default: general 17.21%. Question: "Is the employer in the mining sector? If so, employer charges are 19.51%."  _(PwC)_

### 11.7 APS effective rate

- **Default and question** — Default: 3.5% APS (17.21% total). Question: "Confirm the 3.5% Aporte Patronal Solidario applies to this pay period (Ley 1582, eff. Oct 2024); some guides still quote 3.0%/16.71%." [RESEARCH GAP.]  _(Ley 1582)_

### 11.8 Termination / finiquito

- **Default and question** — Default: flag — indemnizacion and desahucio are RC-IVA-exempt (DS 21531). Question: "Is this a termination/finiquito (indemnizacion 1 month/year, desahucio 3 months)?" — R-BO-P-5.  _(R-BO-P-5; DS 21531)_

### 11.9 Worker type

- **Default and question** — Default: dependent employee. Question: "Is the person a dependent employee or a contribuyente directo (Form 610)?" — R-BO-P-2.  _(R-BO-P-2)_

### 11.10 Penalty / interest on late remittance

- **Default and question** — Default: flag exposure. Question: "Were the Form 608 filing, the Gestora/CNS planilla, or the aguinaldo payment late?" See Section 15.

## Section 12 -- Excel Working Paper Template

Per `payroll-workflow-base`. One row per employee per pay period. Suggested columns (amounts in Bs):

**Working paper columns**

| Col | Header | Notes |
| --- | --- | --- |
| A | Employee name | -- |
| B | CI / matricula (Gestora) | National ID / pension registration |
| C | Pay period | e.g. 2025-06 |
| D | Total ganado | Period gross |
| E | Pension-capped base | min(total ganado, 60 SMN = Bs 165,000/month in 2025) |
| F | Aporte Laboral 12.71% | E x 12.71% (vejez 10% + riesgo comun 1.71% + comision 0.50% + solidario 0.50%) — see Tier 2 11.5 on cap scope |
| G | ANS | cumulative marginal on D above Bs 13,000 (1.15% / 6.89% / 18.37% bands); 0 if D ≤ 13,000 |
| H | RC-IVA base | D − F − G − (2 SMN = Bs 5,500 in 2025) − VAT credits; floored at 0 |
| I | Gross RC-IVA | max(H,0) x 13% |
| J | Presumed VAT credit | 13% x 1 SMN = Bs 357.50 (DS 5383 conservative); or 13% x 2 SMN = Bs 715.00 historical |
| K | Form 110 factura credit | 13% x submitted invoice total |
| L | RC-IVA withheld | max(I − J − K, 0); surplus carries forward |
| M | Net pay | D − F − G − L |
| N | Employer CNS 10% | D x 10.00% |
| O | Employer riesgo profesional 1.71% | D x 1.71% |
| P | Employer pro-vivienda 2% | D x 2.00% |
| Q | Employer APS 3.5% | D x 3.50% |
| R | Total employer (Aporte Patronal) | N+O+P+Q = D x 17.21% (general) or x 19.51% (mining) |
| S | Total employer cost | D + R |

**Summary sheet** rolls up: total RC-IVA withheld (→ SIN via Form 608), total Aporte Laboral + ANS (→ Gestora), total CNS (→ Caja), total employer Aporte Patronal, and total employer cost. Flag rows where the DS 5383 presumed-credit (J), the aguinaldo treatment, or the ANS deductibility (G/H) is reviewer-dependent.

## Section 13 -- Bolivia Bank Statement / Terminology Reading Guide

**CSV conventions.** Bolivian banks (Banco Mercantil Santa Cruz, Banco Nacional de Bolivia / BNB, Banco Union, Banco BISA, Banco de Credito BCP) typically use semicolon or comma delimiters and DD/MM/YYYY dates. **BOB (Bs)** only; amounts often use the **comma as decimal separator and period as thousands separator** (e.g. `2.400,47`). Narratives are in Spanish.

**Language variants**

| Spanish | English |
| --- | --- |
| Sueldo / Salario / Haber / Remuneracion | Salary |
| Total ganado | Gross earnings (the contribution/RC-IVA base) |
| Planilla de sueldos / Nomina | Payroll run |
| Planilla tributaria | Consolidated tax/contribution declaration |
| RC-IVA / Regimen Complementario al IVA | Personal income tax (withholding) |
| Retencion | Withholding |
| Aporte Laboral | Employee pension-side contribution (12.71%) |
| Aporte Patronal | Employer social charges (17.21% / 19.51%) |
| Gestora Publica / AFP | Long-term (pension) collector |
| Caja Nacional de Salud / CNS | Short-term health collector |
| Riesgo comun / Riesgo profesional | Common-risk / work-accident branch |
| Aporte Solidario / Aporte Nacional Solidario | Solidarity contribution(s) |
| Aguinaldo / Segundo aguinaldo | Christmas / second 13th-month bonus |
| Indemnizacion / Desahucio / Finiquito | Severance / dismissal compensation / final settlement |
| Factura | Tax invoice (claimed via Form 110) |
| Horas extras | Overtime |

- **Authority counterparties** — "SIN" / "Impuestos Nacionales" / "SIAT" = the tax authority (RC-IVA, Forms 608/610/110). "Gestora" / "Gestora Publica" / "AFP" = the long-term pension collector (vejez, riesgo comun, comision, solidario, ANS, riesgo profesional). "CNS" / "Caja Nacional de Salud" = the short-term health collector (employer 10%).
- **NIT** — "NIT" (Numero de Identificacion Tributaria) — the employer's tax ID; its last digit sets the Form 608 monthly due date.

## Section 14 -- Onboarding Fallback

### 14.1 Worker type

- **Inference and fallback** — Inference: employment contract = dependent employee. Fallback: "Is this a dependent employee on payroll or a contribuyente directo (Form 610)?" If direct → R-BO-P-2.  _(R-BO-P-2)_

### 14.2 Total ganado

- **Fallback** — Fallback: "What is the monthly total ganado (gross), and any bonuses / prima / aguinaldo this period?" If missing → R-BO-P-1.  _(R-BO-P-1)_

### 14.3 Year / SMN

- **Inference and fallback** — Inference: current calendar year. Fallback: "Which year's pay period? SMN = Bs 2,750 (2025) or Bs 3,300 (2026); it drives the 2-SMN RC-IVA minimum and the 60-SMN cap."

### 14.4 Form 110 facturas

- **Fallback** — Fallback: "Has the employee submitted Form 110 invoices (facturas) this month? 13% of the invoice VAT offsets the RC-IVA; if none, the conservative (maximum) withholding applies."

### 14.5 Employer sector and NIT

- **Fallback** — Fallback: "Is the employer in the mining sector (19.51%) or general (17.21%)? What is the last digit of the NIT (it sets the Form 608 due date)?"

### 14.6 Termination / aguinaldo

- **Fallback** — Fallback: "Is this a termination (indemnizacion/desahucio/finiquito) or an aguinaldo computation? These have special RC-IVA treatment." → R-BO-P-5 / R-BO-P-6.  _(R-BO-P-5; R-BO-P-6)_

### 14.7 DS 5383 / ANS

- **Fallback** — Fallback: "For mid/high earners, confirm the DS 5383 presumed-credit basis (R-BO-P-7) and whether the ANS applies (total ganado > Bs 13,000) and is deductible (R-BO-P-8)."  _(R-BO-P-7; R-BO-P-8)_

## Section 15 -- Filing Obligations and Penalties

### Forms and Deadlines

**Forms and Deadlines**

| Form | Purpose | Deadline |
| --- | --- | --- |
| **Form 608 (RC-IVA Agentes de Retencion) v.4** | Employer's monthly consolidated RC-IVA withholding declaration; filed only when there is tax withheld and/or balances in favor of dependents | **Monthly**, by the due date per **last digit of the employer's NIT** (NIT ending 0 → day 13, 1 → 14, … 9 → day 22 of the following month) (SIN Calendario Tributario 2025) |
| **Form 110 (RC-IVA dependientes)** | Employee's submission of invoices/facturas to claim the 13% VAT credit; generated via the "Mis Facturas" app in SIAT (RND 102000000025 / RND 1020-25) | Submitted **monthly to the employer** (agente de retencion) per current regulation (SIAT) |
| **Form 610 (RC-IVA Contribuyente Directo) v.4** | RC-IVA declaration for direct/independent taxpayers (directors' fees, rental income, foreign-employer salaried individuals) | Quarterly / monthly per regulation, by NIT last-digit calendar (SIAT) — **[RESEARCH GAP — reviewer to confirm exact frequency]** |
| **Planilla de Aportes (Gestora Publica)** | Monthly pension/social contribution declaration and payment to the Gestora Publica | **Monthly** (typically by the last day of the following month) — **[RESEARCH GAP — reviewer to confirm the current Gestora calendar]** |
| **CNS planilla** | Monthly health contribution declaration and payment to the Caja Nacional de Salud (or chosen Caja) | **Monthly** — **[RESEARCH GAP — reviewer to confirm the current CNS deadline]** |

### Penalties and Interest

**Penalties and Interest**

| Item | Detail |
| --- | --- |
| **Omision de pago** | Fine of **60% of the unpaid tax (omitido)**, maintained in UFV value. Reducible: **80% reduction** if paid within 20 days of the Vista de Cargo; **60% reduction** if paid before appealing the Resolucion Determinativa. (Ley 2492; RND 102200000016.) |
| **Mantenimiento de valor + intereses** | Tax debt is updated to **UFV** (inflation-indexed) **plus interest** from the original due date until payment. (Ley 2492.) |
| **Incumplimiento de deberes formales (IDF)** | Fixed fines (in UFV) for late/missing declarations and formal-duty breaches per RND 10-0012-04 (and successors); amounts differ for individuals vs companies. **[RESEARCH GAP — IDF fixed-fine amounts vary by RND and taxpayer type and were not enumerated.]** (RND 10-0012-04; SIN sanciones table.) |
| **Aguinaldo non-payment** | **Labor (not tax) penalty:** failure to pay the aguinaldo by the deadline obliges the employer to pay **double (doble aguinaldo)**. (Ministerio de Trabajo instructivo.) |

## Section 16 -- Interaction with Other Skills

**Interaction table**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (RC-IVA withholding + social contributions) | **This skill (bolivia-payroll.md)** |
| Direct/independent RC-IVA (Form 610) | Bolivia direct-RC-IVA / income-tax skill |
| Bolivia VAT (IVA) | bolivia-iva.md |
| Employer corporate tax (IUE) | Bolivia corporate-tax skill |
| Cross-border / expat / treaty | cross-border skill |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages and the employer Aporte Patronal (CNS, riesgo profesional, pro-vivienda, APS) are **expenses**; the RC-IVA withheld and the employee Aporte Laboral / ANS are **liabilities** until remitted to the SIN / Gestora / CNS.
- **Payroll → RC-IVA (direct):** Non-dependent income (directors' fees, rentals, foreign-paid salary) is self-declared on Form 610, not withheld through payroll.
- **Payroll → VAT (IVA):** The employee's Form 110 facturas feed the 13% RC-IVA VAT credit; this is the personal mirror of the company's IVA system.

## Section 17 -- Reference Material and Test Suite

### Sources

1. PwC Worldwide Tax Summaries — Bolivia, Individual, Taxes on personal income (RC-IVA 13%): https://taxsummaries.pwc.com/bolivia/individual/taxes-on-personal-income
2. PwC Worldwide Tax Summaries — Bolivia, Individual, Other taxes (employee 12.71% AFP, ANS scale 1.15%-11.48%, 60-SMN cap, Bs 13,000 threshold): https://taxsummaries.pwc.com/bolivia/individual/other-taxes
3. PwC Worldwide Tax Summaries — Bolivia, Corporate, Other taxes (employer social charges 17.21% general / 19.51% mining): https://taxsummaries.pwc.com/bolivia/corporate/other-taxes
4. PwC Worldwide Tax Summaries — Bolivia, Individual, Tax administration (employer monthly RC-IVA consolidated return): https://taxsummaries.pwc.com/bolivia/individual/tax-administration
5. Servicio de Impuestos Nacionales (SIN) — RC-IVA (SIAT Info): https://siatinfo.impuestos.gob.bo/index.php/impuesto-asunto/rc-iva
6. SIN / SIAT — 610 Regimen Complementario del IVA - Contribuyente Directo (Forms 608/610/110): https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/regimen-complementario-al-iva/610-regimen-complementario-del-iva-contribuyente-directo
7. SIN — Texto Formularios 110 y 610 (julio 2025): https://www.impuestos.gob.bo/wp-content/uploads/2025/10/TEXTO-FORMULARIOS-110-610.pdf
8. SIN — Calendario Tributario 2025 (NIT last-digit due dates): https://www.impuestos.gob.bo/wp-content/uploads/2025/09/calendario-tributario-2025.pdf
9. MEFP — Ley N° 1582 (1 Oct 2024), Aporte Nacional Solidario & Pension Solidaria: https://www.economiayfinanzas.gob.bo/sites/default/files/2024-10/L15821807NCPP.pdf
10. MEFP — Ley 1582 brackets 1.15% / 5.74% / 11.48%: https://www.economiayfinanzas.gob.bo/node/11448
11. Gaceta Oficial / Lexivox — Decreto Supremo N° 5383, 1 de mayo de 2025 (SMN Bs 2,750): https://www.lexivox.org/norms/BO-DS-N5383.html
12. Planifica Consultores — Aportes a la Gestora Publica y Caja de Salud (guia empleado y empleador): https://www.planifica.com.bo/aportes-afp-caja-salud-bolivia-guia-empleado-empleador/
13. Bolivia Impuestos — Cambios en el Aporte Nacional Solidario - Ley 1582: https://boliviaimpuestos.com/cambios-en-aporte-nacional-solidario-ley-1582/
14. TopTrabajos — Descuentos de planilla en Bolivia: AFP y RC-IVA: https://www.toptrabajos.com/bo/blog/descuentos-planilla-bolivia/
15. Rigoberto Paredes & Asociados — Bolivia 2025 Salary Increase: Impact on RC-IVA (DS 5383 presumed-credit change): https://www.rigobertoparedes.com/en/bolivia-2025-salary-increase/
16. Deel — Tabla de beneficios sociales en Bolivia (aguinaldo, indemnizacion, vacaciones): https://www.deel.com/es/blog/tabla-beneficios-sociales-bolivia/
17. Bolivia Impuestos — Multas de Impuestos Nacionales / omision de pago 60% (Ley 2492): https://boliviaimpuestos.com/multas-impuestos-nacionales/

### Known Gaps

1. **DS 5383 presumed VAT credit:** multiple advisory sources say it reduced the presumed-credit reference from 2 SMN to 1 SMN, increasing liability, but this was **not confirmed from the decree itself**. The conservative (1-SMN) figure is used. (R-BO-P-7.)
2. **Employer total 17.21% (PwC) vs 16.71% (some Bolivian guides):** the difference is the Aporte Patronal Solidario at 3.5% (post-Ley 1582) vs 3.0% (pre-1582). 17.21% (3.5% APS) is used; confirm the effective date for payroll application.
3. **Aguinaldo RC-IVA treatment:** PwC states all bonuses except the Christmas bonus are taxable, while some Bolivian sources list the aguinaldo as taxable and only indemnizacion/desahucio/quinquenio as exempt (DS 21531). Reconcile before finalizing. (R-BO-P-6.)
4. **Pension cap scope:** PwC cites 60 SMN (~USD 28,450); whether the 0.50% comision, 0.50% aporte solidario and the ANS sit under the cap or on uncapped total ganado is unconfirmed. The Gestora monthly payment deadline was not confirmed from the Gestora Publica site.
5. **ANS computation:** the brackets are applied cumulatively/marginally across Bs 13,000 / 25,000 / 35,000 per the MEFP description; the precise marginal-vs-stacked computation and **ANS deductibility from the RC-IVA base** need a worked example confirmed with the authority. (R-BO-P-8.)
6. **2026 SMN Bs 3,300 (DS 5516):** reported by multiple secondary sources and consistent, but confirm against the Gaceta Oficial.
7. **IDF fixed-fine amounts** vary by RND and taxpayer type and were not enumerated in detail.
8. **Official-source access:** several SIN/SIAT and MEFP pages repeatedly failed TLS certificate verification or returned 403 in the research environment; many figures rest on secondary (Big-4 / Bolivian advisory) sources and should be re-verified directly against the authority before publication. Data primarily reflects **tax year 2025** with the **2026 SMN** noted.

### Test Suite

A correct implementation should pass each of these checks (2025 parameter set: SMN Bs 2,750; 2-SMN minimum Bs 5,500; 60-SMN cap Bs 165,000; presumed credit conservatively 13% x 1 SMN = Bs 357.50; no facturas unless stated):

1. **RC-IVA flat rate:** RC-IVA is a single **13%** flat rate (no progressive brackets).
2. **Employee Aporte Laboral:** 10.00 + 1.71 + 0.50 + 0.50 = **12.71%** of total ganado; deductible from the RC-IVA base.
3. **Employer Aporte Patronal (general):** 10.00 + 1.71 + 2.00 + 3.50 = **17.21%**; mining = **19.51%**.
4. **APS step-up:** the Aporte Patronal Solidario is **3.5%** (post-Ley 1582), making the employer total 17.21% (was 16.71% at 3.0%).
5. **Minimum-wage nil RC-IVA (Ex.1):** total ganado Bs 2,750 → Aporte Laboral Bs 349.53; RC-IVA base 2,750 − 349.53 − 5,500 < 0 → RC-IVA **Bs 0**; net **Bs 2,400.47**.
6. **Low earner nil RC-IVA (Ex.2):** Bs 8,000 → base 1,483.20 → gross RC-IVA Bs 192.82 < presumed credit Bs 357.50 → RC-IVA **Bs 0**; net **Bs 6,983.20**.
7. **Mid earner RC-IVA due (Ex.3):** Bs 12,000 → base 4,974.80 → gross RC-IVA Bs 646.72 − Bs 357.50 = **Bs 289.22** withheld; net **Bs 10,185.58**.
8. **ANS threshold:** total ganado ≤ Bs 13,000 → ANS **Bs 0**.
9. **ANS cumulative (Ex.4):** Bs 30,000 → (25,000−13,000) x 1.15% + (30,000−25,000) x 6.89% = 138.00 + 344.50 = **Bs 482.50**.
10. **High earner net (Ex.4):** Bs 30,000 → employee social 4,295.50, RC-IVA withheld 2,269.09 → net **Bs 23,435.41** (ANS treated as deductible — flag R-BO-P-8).
11. **Pension cap (Ex.5):** Bs 200,000 → vejez + riesgo comun (11.71%) on capped Bs 165,000 = **Bs 19,321.50**, not on Bs 200,000.
12. **Employer remittance (Ex.6):** Bs 12,000 → 17.21% = CNS 1,200.00 + riesgo 205.20 + vivienda 240.00 + APS 420.00 = **Bs 2,065.20**.
13. **Form 608 due date:** filed monthly by the **last digit of the NIT** (0 → day 13 … 9 → day 22 of the following month).
14. **Form 110 / 610:** employees claim VAT credits via Form 110 ("Mis Facturas"); contribuyentes directos use Form 610.
15. **Exempt termination:** indemnizacion (1 month/year) and desahucio (3 months) are **RC-IVA-exempt** (DS 21531) — flag R-BO-P-5, do not run through monthly withholding.
16. **Omision de pago penalty:** **60%** of the unpaid tax (in UFV), reducible to 80% off (within 20 days of the Vista de Cargo) or 60% off (before appealing).
17. **DS 5383 sensitivity:** under the historical 2-SMN presumed credit (Bs 715.00), Example 3's Bs 646.72 gross RC-IVA would be fully covered → Bs 0; under the conservative 1-SMN credit it is Bs 289.22. Flag R-BO-P-7.

## PROHIBITIONS

- NEVER treat Bolivia as having **no personal income tax** — RC-IVA is a flat 13% personal income tax withheld from salaries (Ley 843); the exemption is delivered through the 2-SMN minimum and VAT credits, not a 0% band.
- NEVER compute RC-IVA without first deducting the employee Aporte Laboral (**12.71%**) and the **2-SMN** non-taxable minimum (Bs 5,500 in 2025; Bs 6,600 in 2026) from total ganado.
- NEVER omit the **presumed VAT credit** and the Form 110 factura credit when computing RC-IVA withheld — for most low/mid earners these reduce RC-IVA to nil.
- NEVER use the historical 2-SMN presumed credit for mid-earners without confirming DS 5383 — use the conservative 1-SMN figure and flag R-BO-P-7. **[RESEARCH GAP.]**
- NEVER apply the **Aporte Nacional Solidario** below Bs 13,000/month, and never apply it as a flat rate — it is cumulative marginal (1.15% / 6.89% / 18.37% effective bands).
- NEVER charge the employer RC-IVA — the employer is only the **agente de retencion**; RC-IVA is the employee's tax.
- NEVER charge the **employer** the employee pension branches (vejez, comision, aporte solidario, ANS) — these are employee-only.
- NEVER use **16.71%** for general employer charges — the current total is **17.21%** (3.5% APS, post-Ley 1582); mining is 19.51%.
- NEVER compute capped pension branches above the **60-SMN** cap (Bs 165,000/month in 2025; Bs 198,000 in 2026).
- NEVER mix SMN years — use **Bs 2,750** for 2025 and **Bs 3,300** for 2026; the SMN drives both the 2-SMN minimum and the 60-SMN cap.
- NEVER run a termination (indemnizacion / desahucio / finiquito) through standard monthly RC-IVA withholding — these are RC-IVA-exempt (DS 21531); flag R-BO-P-5.
- NEVER run a contribuyente directo (Form 610) through dependent payroll — flag R-BO-P-2.
- NEVER miss the **Form 608** deadline (per NIT last digit, days 13-22 of the following month) — omision de pago carries a 60% (UFV-indexed) penalty plus interest.
- NEVER fail to pay the aguinaldo by its deadline — the labor penalty is **double aguinaldo**.
- NEVER present payroll computations as definitive — always label as estimated and direct to a Bolivian reviewer (contador / auditor).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador or auditor in Bolivia) before implementation.

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
