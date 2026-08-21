---
name: peru-payroll
description: Use this skill whenever asked about Peru payroll processing for employed persons. Trigger on phrases like "Peru payroll", "nómina Perú", "planilla Perú", "renta de quinta categoría", "retención de quinta", "impuesto a la renta quinta", "PLAME", "Formulario 601", "EsSalud", "aporte EsSalud 9%", "ONP", "SNP 13%", "AFP", "aporte AFP", "comisión AFP", "prima de seguro AFP", "SBS AFP", "T-Registro", "UIT Perú", "RMV", "salario mínimo Perú", "sueldo mínimo Perú", "net salary Peru", "sueldo neto", "PAYE Peru", "tax withholding Peru", "employer contributions Peru", "SUNAT planilla", "gross to net Peru", "PEN payroll", "sol salary", or any question about computing employee pay, withholding fifth-category income tax, or mandatory social contributions (EsSalud, ONP, AFP) for Peru-based employees. This skill covers fifth-category income-tax withholding (7-UIT exemption + 8%–30% progressive schedule), EsSalud (employer), the ONP/AFP pension choice (employee-borne), the RMV minimum wage, non-domiciled flat withholding, T-Registro registration, and PLAME/SUNAT filing obligations. ALWAYS read this skill before processing any Peru payroll.
version: 0.1
jurisdiction: PE
tax_year: 2026
last_updated: 2026-07-13
reviewed_by: Maria Clemencia Valverde Rios
review_status: current
depends_on:
  - payroll-workflow-base
category: payroll
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Peru Payroll

## Peru Payroll Skill v0.1

Tier 2 — research-verified. Figures below are sourced from the Peruvian tax authority (Superintendencia Nacional de Aduanas y de Administración Tributaria, SUNAT), the pension/AFP supervisor (Superintendencia de Banca, Seguros y AFP, SBS), the social-health insurer (EsSalud), the public pension office (ONP), the Presidencia/MTPE (minimum wage Supreme Decree 006-2024-TR), Garrigues, and PwC Worldwide Tax Summaries. NOT yet signed off by a licensed Peruvian accountant (Contador Público Colegiado) or tax adviser. Treat every computation as an estimate pending professional review.

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Maria Clemencia Valverde Rios** on 2026-06-29.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### peru-payroll

- **Currency** — Peruvian Sol (PEN / S/) only
- **Standard pay frequency** — Monthly
- **Tax year** — Calendar year (1 January -- 31 December)
- **UIT (Unidad Impositiva Tributaria) 2026** — S/ 5,500
- **UIT (Unidad Impositiva Tributaria) 2025** — S/ 5,350
- **Filing portal** — SUNAT — SOL / PLAME (Formulario Virtual N° 601)
- **Standard fixed deduction (7 UIT exemption)** — 7 UIT = 7 × 5,500 = S/ 38,500 (2026)  _(TUO LIR Art. 46)_
- **Additional deduction (qualifying expenses)** — Up to 3 UIT = up to S/ 16,500 (2026) for specific documented personal expenses—such as hotels, restaurants, leases, and EsSalud contributions for domestic workers  _(TUO LIR Art. 46)_
- **Additional 3 UIT deduction at withholding stage default** — S/ 0 at source unless documented  _(TUO LIR Art. 46)_
- **5th-cat income tax Band 1 — Up to 5 UIT (0 – 27,500)** — 8%  _(TUO LIR Art. 53)_
- **5th-cat income tax Band 2 — Over 5 to 20 UIT (27,500 – 110,000)** — 14%  _(TUO LIR Art. 53)_
- **5th-cat income tax Band 3 — Over 20 to 35 UIT (110,000 – 192,500)** — 17%  _(TUO LIR Art. 53)_
- **5th-cat income tax Band 4 — Over 35 to 45 UIT (192,500 – 247,500)** — 20%  _(TUO LIR Art. 53)_
- **5th-cat income tax Band 5 — Over 45 UIT (Over 247,500)** — 30%  _(TUO LIR Art. 53)_
- **Cumulative tax at top of Band 1 (5 UIT)** — S/ 2,200.00  _(TUO LIR Art. 53)_
- **Cumulative tax at top of Band 2 (20 UIT)** — S/ 13,750.00  _(TUO LIR Art. 53)_
- **Cumulative tax at top of Band 3 (35 UIT)** — S/ 27,775.00  _(TUO LIR Art. 53)_
- **Cumulative tax at top of Band 4 (45 UIT)** — S/ 38,775.00  _(TUO LIR Art. 53)_
- **Non-domiciled employment income withholding** — 30% flat on gross Peruvian-source income, no deductions, no 7 UIT exemption  _(TUO LIR)_
- **ONP / SNP pension contribution (employee-borne)** — 13%
- **ONP / SNP base/cap** — Monthly remuneration; no cap
- **AFP mandatory contribution (all AFPs)** — 10.00% of gross salary; no cap
- **AFP insurance prima (prima de seguro, uniform)** — Established by SBS Resolution No. 03399-2024. The 1.37% flat rate is valid until Dec 31, 2026. The RMA cap updates quarterly  _(SBS Resolution No. 03399-2024.)_
- **Maximum insurable remuneration (RMA), Q2 2026** — S/ 12,598.91
- **AFP HABITAT commission on flow (mixed)** — 1.47%  _(SBS — Comisiones y Prima del SPP, devengue 2026-06)_
- **AFP HABITAT annual commission on balance** — 1.25%  _(SBS — Comisiones y Prima del SPP, devengue 2026-06)_
- **AFP INTEGRA commission on flow (mixed)** — 1.55%  _(SBS — Comisiones y Prima del SPP, devengue 2026-06)_
- **AFP INTEGRA annual commission on balance** — 0.78%  _(SBS — Comisiones y Prima del SPP, devengue 2026-06)_
- **AFP PRIMA commission on flow (mixed)** — 1.60%  _(SBS — Comisiones y Prima del SPP, devengue 2026-06)_
- **AFP HABITAT annual commission on balance** — 1.25%  _(SBS — Comisiones y Prima del SPP, devengue 2026-06)_
- **AFP PROFUTURO commission on flow (mixed)** — 1.69%  _(SBS — Comisiones y Prima del SPP, devengue 2026-06)_
- **AFP PROFUTURO annual commission on balance** — 0.68%  _(SBS — Comisiones y Prima del SPP, devengue 2026-06)_
- **Total AFP withholding range** — ≈ 12.84%–13.06% (lowest 12.84% HABITAT flow, highest 13.06% PROFUTURO flow)
- **EsSalud (health) employer contribution** — 9%
- **EsSalud base/cap** — Monthly remuneration; no upper cap; minimum base = 1 RMV
- **EPS credit against EsSalud** — UP to 25% of EsSalud payment (provided that it does not exceed the amount paid to the EPS and 10% of the UIT per worker)  _(Art. 16 Ley N° 26790)_
- **RMV (Remuneración Mínima Vital)** — S/ 1,130 / month (up from S/ 1,025)  _(Supreme Decree 006-2024-TR)_
- **RMV hourly equivalent (48-hour week)** — ((RMV/30) * 7)  / 48
- **T-Registro registration of new worker** — late T-Registro enrollment constitutes a grave infraction subject to a variable fine based on the number of affected employees; for fiscal year 2026 (UIT = S/ 5,500.00), this penalty scales from 1.57 UIT (S/ 8,635.00) for 1–10 workers up to a maximum legal cap of 26.12 UIT (S/ 143,660.00) for 1,000+ workers, superseding any previous historical thresholds.  _(Art. 24.2 D.S. 019-2006-TR)_
- **Late T-Registro SUNAFIL fine** — late T-Registro enrollment constitutes a grave infraction subject to a variable fine based on the number of affected employees; for fiscal year 2026 (UIT = S/ 5,500.00), this penalty scales from 1.57 UIT (S/ 8,635.00) for 1–10 workers up to a maximum legal cap of 26.12 UIT (S/ 143,660.00) for 1,000+ workers, superseding any previous historical thresholds  _(Arts. 24.2 y 48.1 del D.S. N° 019-2006-TR)_
- **PLAME (Formulario Virtual N° 601) monthly deadline** — Monthly, by date matching last digit of employer's RUC per SUNAT annual cronograma;  _(Art 4° b DS N° 018-2007-TR)_
- **AFP remittance (via AFPnet) deadline** — Within the first 5 business days of the following month
- **Employee annual income-tax return form** — Formulario Virtual N° 709 — per last RUC/DNI digit in SUNAT annual cronograma; pure single-employer wage earners generally need not file
- **Failure to file PLAME on time (General / MYPE Tax Regime)** — Base fine 1 UIT (S/ 5,500)  _(Código Tributario Art. 176, num. 1)_
- **Failure to file PLAME on time (RER)** — 50% UIT (S/ 2,750)  _(Código Tributario Art. 176, num. 1)_
- **Failure to file PLAME on time (Nuevo RUS)** — 0.6% of monthly net income  _(Código Tributario Art. 176, num. 1)_
- **Régimen de Gradualidad fine reduction** — Up to 100% (or up to 95% with payment)  _(Régimen de Gradualidad (SUNAT))_
- **Prior-year net revenues < 19 UIT and induced rectification within the 7th business day** — Up to 98% (or up to 99% with payment).  _(Codigo Tributario Art. 176, num. 1)_
- **Prior-year net revenues < 150 UIT and induced rectification within the 7th business day** — Up to 90% (or up to 95% with payment).  _(Codigo Tributario Art. 176, num. 1)_
- **Prior-year net revenues > 150 UIT and induced rectification within the 7th business day** — Up to 80% (or up to 90% with payment).  _(Codigo Tributario Art. 176, num. 1)_

## Section 1 -- Quick Reference

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Peru (Republic of Peru / República del Perú) |
| Currency | Peruvian Sol (PEN / S/) only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) (PwC) |
| Income tax withholding system | Monthly withholding by the employer on projected annual fifth-category income, less 7 UIT, divided across the year; annual adjustment (PwC; Decreto Supremo 179-2004-EF, TUO LIR) |
| Income tax authority | Superintendencia Nacional de Aduanas y de Administración Tributaria (SUNAT) |
| Health insurance authority | EsSalud (Seguro Social de Salud) |
| Public pension authority | Oficina de Normalización Previsional (ONP / Sistema Nacional de Pensiones, SNP) |
| Private pension supervisor | Superintendencia de Banca, Seguros y AFP (SBS); pensions run by the four AFPs |
| Reference unit | UIT (Unidad Impositiva Tributaria) = **S/ 5,500** for 2026 (PwC) |
| Filing portal | SUNAT — SOL / PLAME (Formulario Virtual N° 601) |
| Validated by | Verified by Maria Clemencia Valverde Rios (CPA) on 2026-06-29 |
| Skill version | 0.1 |

Read this whole section before computing anything. The shared payroll runbook lives in `payroll-workflow-base` — follow that runbook with this skill supplying the Peru-specific content.

### The single most important Peru facts

> **Peru DOES have a personal income tax on employment income** ("renta de quinta categoría"), withheld at source monthly by the employer. The first **7 UIT (S/ 38,500 for 2026)** of annual employment income are exempt; the excess is taxed on a progressive **8% / 14% / 17% / 20% / 30%** schedule. (PwC; TUO LIR)

> **The pension is employee-borne and the employee chooses ONE system**: public **ONP/SNP at 13%**, or a private **AFP** (≈12.5%–13% total: 10% mandatory + 1.37% insurance prima + a per-AFP commission). The employer **withholds** the pension; the employer's only contribution on top of salary is **EsSalud at 9%** (health). (PwC; SBS; ONP)

## Section 2 -- Income Tax Withholding (Renta de Quinta Categoría)

The employer projects the employee's annual fifth-category remuneration, subtracts the 7 UIT exemption, applies the progressive schedule, and withholds the result in monthly installments declared through PLAME. (PwC; TUO LIR Art. 40–46)

### Reference unit — UIT (Unidad Impositiva Tributaria)

**UIT by tax year**

| Tax year | UIT | Source |
| --- | --- | --- |
| 2026 | **S/ 5,500** | PwC (confirmed) |
| 2025 | S/ 5,350 | secondary summaries **[RESEARCH GAP — confirm against the SUNAT/MEF Supreme Decree]** |

The brackets are defined in UIT, so the UIT value is load-bearing.

All worked examples below use the confirmed **UIT 2026 = S/ 5,500**. (PwC)

### Standard and additional deductions

**Deductions table**

| Deduction | Amount | Notes / source |
| --- | --- | --- |
| Standard fixed deduction | **7 UIT** = 7 × 5,500 = **S/ 38,500** (2026) | First 7 UIT of annual employment income exempt (PwC; TUO LIR Art. 46) |
| Additional deduction (qualifying expenses) | **Up to 3 UIT** = up to S/ 16,500 (2026) | Property lease, independent professional services, hotels, restaurants, etc., subject to requirements (PwC; TUO LIR Art. 46) |

> The additional **3 UIT** deduction requires documentary support and qualifying expense categories; the employer does not apply it at source by default — it is reconciled by the taxpayer. Default it to **S/ 0** at the withholding stage unless the employee has filed the qualifying support (see Conservative Defaults).

### Progressive Brackets — Domiciled Employment Income (2026)

**Progressive brackets table**  _(PwC — taxes on personal income; TUO LIR Art. 53)_

| Band | Net taxable income (UIT) | Net taxable income (S/, 2026) | Marginal rate | Cumulative tax at the top of the band (S/) |
| --- | --- | --- | --- | --- |
| 1 | Up to 5 UIT | 0 – 27,500 | 8% | 2,200.00 |
| 2 | Over 5 to 20 UIT | 27,500 – 110,000 | 14% | 13,750.00 |
| 3 | Over 20 to 35 UIT | 110,000 – 192,500 | 17% | 27,775.00 |
| 4 | Over 35 to 45 UIT | 192,500 – 247,500 | 20% | 38,775.00 |
| 5 | Over 45 UIT | Over 247,500 | 30% | — |

Cumulative-tax check (recomputed):
- Band 1 top: 27,500 × 8% = **2,200.00** ✓
- Band 2 top: 2,200 + (110,000 − 27,500) × 14% = 2,200 + 82,500 × 14% = 2,200 + 11,550 = **13,750.00** ✓
- Band 3 top: 13,750 + (192,500 − 110,000) × 17% = 13,750 + 82,500 × 17% = 13,750 + 14,025 = **27,775.00** ✓
- Band 4 top: 27,775 + (247,500 − 192,500) × 20% = 27,775 + 55,000 × 20% = 27,775 + 11,000 = **38,775.00** ✓

### Non-Domiciled Employment Income

**Non-domiciled withholding table**

| Income type | Withholding | Basis | Source |
| --- | --- | --- | --- |
| Salaries/wages to non-domiciled employees | **30% flat** | Gross Peruvian-source income, **no deductions**, no 7 UIT exemption | PwC — TUO LIR |

### Monthly Withholding Method (domiciled)

- **Deterministic withholding order** — 1. Start with **projected annual remuneration** (ordinary monthly salary across the year; in practice Peru also pays **two gratificaciones** — see the note below — which are taxable fifth-category income). 2. Subtract the **7 UIT** standard exemption (S/ 38,500 for 2026). 3. Subtract any **confirmed additional deduction** (up to 3 UIT; default S/ 0 at source). 4. The result is the **net annual taxable income**. 5. Apply the progressive schedule → **annual income tax**. 6. Distribute the annual tax across the remaining periods per SUNAT's installment method → **monthly withholding**, with a year-end adjustment.  _(PwC; TUO LIR; SUNAT)_

> **Gratificaciones note.** Peruvian law grants two statutory gratificaciones per year (July and December), each ≈ one month's salary, which **are** taxable fifth-category income — so a real annual projection commonly uses ~14 months, not 12. To keep the arithmetic transparent and within the researched dataset, the worked examples below project on **12 months only** and flag this; a reviewer should add the gratificaciones (and the related 9% bonificación extraordinaria paid in lieu of EsSalud on gratificaciones) to the projection. **[RESEARCH GAP — confirm the exact gratificación projection mechanics and timing.]**

## Section 3 -- Contributions: Employee Deductions (Pension — ONP or AFP)

The employee pays a **pension contribution, withheld from salary**, into exactly **one** system. The employer contributes **nothing** to the pension on top — pensions are entirely employee-borne. (PwC; SBS; ONP)

### Option A — ONP / SNP (public, defined-benefit)

**ONP/SNP table**

| Contribution | Rate | Payer | Authority | Base / cap | Source |
| --- | --- | --- | --- | --- | --- |
| ONP / SNP | **13%** | Employee (withheld) | ONP | Monthly remuneration; **no cap** | PwC; ONP |

### Option B — AFP (private, individual accounts)

**AFP rates table**  _(SBS — Comisiones y Prima del SPP, devengue 2026-06)_

| AFP | Mandatory contribution | Insurance prima | Commission on flow (mixed) | Annual commission on balance |
| --- | --- | --- | --- | --- |
| HABITAT | 10.00% | 1.37% | 1.47% | 1.25% |
| INTEGRA | 10.00% | 1.37% | 1.55% | 0.78% |
| PRIMA | 10.00% | 1.37% | 1.60% | 1.25% |
| PROFUTURO | 10.00% | 1.37% | 1.69% | 0.68% |

- **Mandatory contribution** — 10.00% of gross salary, to the worker's individual account (uniform across AFPs; no cap).  _(SBS)_
- **Insurance prima cap** — 1.37% (uniform), capped on the maximum insurable remuneration (RMA) = S/ 12,598.91 for the Apr–Jun 2026 quarter; the RMA is reset quarterly by SBS. **[RESEARCH GAP — pull the live RMA at publication time.]**  _(SBS)_
- **Commission variance** — Commission varies by AFP (and by scheme — flow vs. mixed); the table shows the "comisión sobre flujo (mixta)" leg. Total AFP withholding ≈ 12.5%–13%.

> **AFP-total range check (recomputed):** lowest = 10.00% + 1.37% + 1.47% (HABITAT flow) = **12.84%**; highest = 10.00% + 1.37% + 1.69% (PROFUTURO flow) = **13.06%**. The ≈12.5%–13% range in the research holds when the prima is RMA-capped on higher salaries (the prima leg falls below 1.37% of gross above the RMA). (SBS)

> **No employee EsSalud contribution.** Health (EsSalud) is **employer-borne** — see Section 4. The employee's only payroll deduction besides income tax is the pension.

## Section 4 -- Contributions: Employer Contributions (EsSalud)

The employer's only payroll contribution on top of salary is **EsSalud (health)**. (PwC; EsSalud)

**EsSalud table**

| Contribution | Rate | Authority | Base / cap | Source |
| --- | --- | --- | --- | --- |
| EsSalud (health) | **9%** | EsSalud | Monthly remuneration; **no upper cap**; **minimum base = 1 RMV** | PwC; EsSalud |

- **EsSalud borne entirely by employer** — Borne entirely by the **employer** — never deducted from the employee.  _(PwC)_
- **No upper ceiling** — No upper ceiling.  _(PwC)_
- **Minimum base** — The EsSalud base may not be less than the minimum wage (RMV); EsSalud is computed on at least 1 RMV even where a part-time worker earns less. **[RESEARCH GAP — the RMV-floor rule is a general labour rule; confirm the exact regulatory cite.]**
- **EPS credit** — Up to 25% of EPS (private health-plan) payments may be credited against EsSalud.  _(PwC)_
- **Filing channel** — Declared/paid via PLAME (Formulario Virtual N° 601).  _(SUNAT)_

### Employer-side wedge summary

**Wedge summary table**

| Component | Employee | Employer | Source |
| --- | --- | --- | --- |
| EsSalud (health) | — | 9% | PwC; EsSalud |
| Pension (ONP 13% **or** AFP ≈12.84%–13.06%) | withheld from employee | — | PwC; SBS; ONP |
| Income tax (5th cat.) | withheld from employee | — | PwC |
| **Net employer-borne add-on over salary** | — | **≈ 9% (EsSalud)** | (pension + income tax are employee withholdings) |

> **Tax treatment / scope:** beyond EsSalud, employers also owe statutory benefits **not covered by this withholding/contribution skill** — CTS (compensación por tiempo de servicios), two gratificaciones per year, and vacation. These are flagged **out of scope** here and must be provisioned separately. **[RESEARCH GAP — CTS/gratificación/vacation accrual mechanics not in this dataset.]**

## Section 5 -- Minimum Wage (RMV) and Working Hours

**RMV table**

| Item | Value | Source |
| --- | --- | --- |
| RMV (Remuneración Mínima Vital) | **S/ 1,130 / month**, effective **1 January 2025** (up from S/ 1,025) | Supreme Decree 006-2024-TR (Presidencia; Garrigues) |
| Hourly equivalent | ≈ S/ 5.17 (48-hour week) | Garrigues **[RESEARCH GAP — confirm exact statutory hourly derivation]** |

- **RMV floors** — The RMV floors the EsSalud base and many statutory benefit computations.  _(Presidencia; Garrigues)_

### Working Hours and Overtime

> **[RESEARCH GAP — reviewer to confirm]** Statutory overtime multipliers, the maximum daily/weekly hours, and night/Sunday/holiday premiums under Peruvian labour law were not part of this research dataset. A reviewer should populate these before relying on overtime figures.

## Section 6 -- Conservative Defaults

- **Section rule** — When an input is unknown, the skill MUST apply the conservative default below and flag the assumption in its output rather than guessing a more favourable figure.

**Conservative defaults table**

| Field | Default | Rationale |
| --- | --- | --- |
| Additional deduction (up to 3 UIT) | **S/ 0 at source** | Requires qualifying-expense documentation; not applied by the employer at withholding stage. (PwC; TUO LIR) |
| Domicile status | **Domiciled** (progressive 8%–30% with 7 UIT exemption) | Apply the 30% non-domiciled flat rate only when non-domicile is confirmed. |
| Pension system | **Confirm with the employee** — do NOT assume ONP vs AFP; if unknown, flag and request it | ONP (13%) and AFP (≈12.84%–13.06%) differ; the choice is the employee's and must be on record. |
| AFP commission scheme | **Use the per-AFP "comisión sobre flujo (mixta)" from the SBS table for the current devengue** | Commission varies by AFP; default to the live SBS figure, not an average. |
| AFP prima base | **min(remuneration, RMA)** | The prima is capped at the RMA (S/ 12,598.91, Q2 2026); never apply 1.37% to remuneration above the RMA. |
| UIT | **S/ 5,500 (2026)** | Confirmed; for 2025 runs confirm UIT against the SUNAT/MEF Supreme Decree. **[RESEARCH GAP]** |
| EsSalud base | **max(remuneration, 1 RMV)** | EsSalud floored at the minimum wage. **[RESEARCH GAP — confirm cite]** |
| Gratificaciones in the projection | **Project on 12 months and flag** | The 14-month reality (2 gratificaciones) is out of the clean dataset; reviewer to add. **[RESEARCH GAP]** |
| Employer cost estimate | **Salary × 1.09 (add 9% EsSalud)** plus separately-provisioned CTS / gratificaciones / vacation | EsSalud is the only on-top payroll contribution; other benefits are out of scope. |

### Required inputs before any computation

- **Required inputs list** — 1. **Monthly base salary** (remuneración) in PEN. 2. **Domicile status** — domiciled (progressive) vs non-domiciled (30% flat on gross). 3. **Pension system** — ONP/SNP (13%) **or** AFP (which of HABITAT / INTEGRA / PRIMA / PROFUTURO, and flow vs. mixed scheme). 4. **Pay period (month and year)** — to pick the correct UIT, RMV, and SBS AFP devengue. 5. **Additional 3 UIT deduction** — whether qualifying expenses are documented (default S/ 0 at source). 6. Whether **gratificaciones** fall in the period — to include them in the projection (currently flagged out of scope).

### Refusal Catalogue — DO NOT attempt; route to a licensed accountant

**Refusal catalogue table**

| Scenario | Why it is out of scope |
| --- | --- |
| Cross-border / posted workers / totalization (social-security coordination) | Requires treaty / EsSalud/ONP determination — see `cross-border-payroll-coordination`. |
| Double-tax-treaty relief, expat tax-equalisation, tie-breaker domicile | Beyond a domestic payroll run; route to a reviewer. |
| CTS, gratificaciones, and vacation accrual / payout computation | Statutory benefits out of scope for this withholding/contribution skill. **[RESEARCH GAP]** |
| Benefits in kind / company cars / stock-option valuation | Peruvian BIK valuation rules were not in this research dataset. **[RESEARCH GAP]** |
| Severance / indemnización por despido taxation | Not in scope; route to a reviewer. |
| Self-employed / fourth-category (renta de cuarta) regimes | Different regime (independent professional services) — out of scope for employer payroll. |
| The 3 UIT additional deduction reconciliation | Taxpayer-level, documentation-dependent; not applied by the employer at source. |
| Overtime / night / Sunday / holiday premiums and maximum hours | Not in this research dataset. **[RESEARCH GAP]** |

## Section 8 -- Transaction / Payment Pattern Library

Deterministic classification of Peruvian bank-statement lines for payroll. Match on the uppercased description fragment.

### Salary credits (what lands in the employee's account)

**Salary credits table**

| Bank statement text (ES / EN) | Classification |
| --- | --- |
| `SUELDO`, `REMUNERACION`, `PLANILLA`, `PAGO PLANILLA` | Net salary payment |
| `NOMINA`, `PAYROLL`, `SALARY`, `HABERES` | Net salary payment (variant) |
| `ADELANTO`, `ADELANTO DE SUELDO` | Salary advance (not final pay) |
| `GRATIFICACION`, `GRATI` | Statutory gratificación (July / December) |
| `CTS`, `DEPOSITO CTS` | CTS deposit (out of scope here) |
| `DEVOLUCION RENTA`, `REINTEGRO SUNAT` | Income-tax refund — NOT income |

### Employer debits (what leaves the employer's account)

**Employer debits table**

| Bank statement text (ES / EN) | Classification |
| --- | --- |
| `SUNAT`, `PLAME`, `FORM 601`, `RENTA QUINTA`, `RETENCION RENTA` | Income-tax (5th cat.) + EsSalud/ONP remittance to SUNAT via PLAME |
| `ESSALUD`, `APORTE ESSALUD` | EsSalud 9% employer contribution (via PLAME) |
| `ONP`, `SNP`, `APORTE ONP` | ONP 13% (withheld employee pension) remittance |
| `AFP`, `INTEGRA`, `PRIMA AFP`, `PROFUTURO`, `HABITAT`, `AFPNET` | AFP contribution/commission/prima remittance (withheld) |
| `PAGO PLANILLA`, `NOMINA`, `PAYROLL RUN` | Net wages disbursed to employees |

> Income tax (5th cat.), EsSalud (9%), and ONP (13%) are declared together through **PLAME (Formulario 601)** to SUNAT; AFP amounts are reported in PLAME and paid to the AFP (commonly via AFPnet) within the first **5 business days** of the following month. (SUNAT; SBS)

## Section 9 -- Worked Examples

All examples use **2026** figures (UIT S/ 5,500; 7 UIT exemption S/ 38,500), domiciled status, the **additional 3 UIT deduction defaulted to S/ 0**, and a **12-month projection** (gratificaciones excluded — flagged). Income tax uses the 8%–30% schedule from Section 2. Every line below was recomputed end-to-end.

### Example 1 — Low earner, S/ 3,000/month, ONP affiliate

Bank statement context: `PLANILLA … S/ 2,610.00` credited to the employee; `APORTE ONP … S/ 390.00`, `APORTE ESSALUD … S/ 270.00` debited from the employer.

**Example 1 computation table**

| Step | Computation | S/ |
| --- | --- | --- |
| Annual remuneration (12 months) | 3,000 × 12 | 36,000.00 |
| Less 7 UIT exemption | — | 38,500.00 |
| Net annual taxable income | max(36,000 − 38,500, 0) | 0.00 |
| Annual income tax | base is 0 | 0.00 |
| Monthly income tax | — | 0.00 |
| ONP pension (13% × 3,000) | monthly, withheld | 390.00 |
| **Net monthly salary** | 3,000 − 390 − 0 | **2,610.00** |
| EsSalud (employer, 9% × 3,000) | on top — not deducted | 270.00 |

> The 7 UIT exemption alone wipes out the income-tax base at S/ 36,000/year. The employer separately pays EsSalud S/ 270.

### Example 2 — Mid earner, S/ 8,000/month, ONP affiliate

**Example 2 computation table**

| Step | Computation | S/ |
| --- | --- | --- |
| Annual remuneration (12 months) | 8,000 × 12 | 96,000.00 |
| Less 7 UIT exemption | — | 38,500.00 |
| Net annual taxable income | 96,000 − 38,500 | 57,500.00 |
| Band placement | 57,500 / 5,500 = 10.45 UIT → Band 2 (5–20 UIT) | — |
| Income tax — Band 1 (5 UIT × 8%) | 27,500 × 8% | 2,200.00 |
| Income tax — Band 2 (14% × excess over 27,500) | (57,500 − 27,500) × 14% | 4,200.00 |
| Annual income tax | 2,200 + 4,200 | 6,400.00 |
| Monthly income tax | 6,400 ÷ 12 | 533.33 |
| ONP pension (13% × 8,000) | monthly, withheld | 1,040.00 |
| **Net monthly salary** | 8,000 − 1,040 − 533.33 | **6,426.67** |
| EsSalud (employer, 9% × 8,000) | on top | 720.00 |

### Example 3 — Mid earner, S/ 8,000/month, AFP INTEGRA (mixed/flow scheme)

Same income tax as Example 2 (S/ 533.33/month). Pension switches to AFP. Salary S/ 8,000 < RMA S/ 12,598.91, so the prima applies to the full salary.

**Example 3 computation table**

| Step | Computation | S/ |
| --- | --- | --- |
| AFP mandatory (10% × 8,000) | individual account | 800.00 |
| AFP insurance prima (1.37% × min(8,000, 12,598.91)) | 1.37% × 8,000 | 109.60 |
| AFP commission — INTEGRA flow (1.55% × 8,000) | 1.55% × 8,000 | 124.00 |
| Total AFP withholding | 800 + 109.60 + 124.00 | 1,033.60 |
| Monthly income tax | (from Example 2) | 533.33 |
| **Net monthly salary** | 8,000 − 1,033.60 − 533.33 | **6,433.07** |
| EsSalud (employer, 9% × 8,000) | on top | 720.00 |

> AFP total = 12.92% of S/ 8,000 = S/ 1,033.60 (verify: 0.10 + 0.0137 + 0.0155 = 0.1292; 0.1292 × 8,000 = 1,033.60 ✓). Net is S/ 6.40 higher than the ONP equivalent (Example 2) here purely because INTEGRA's effective AFP rate (12.92%) is just below ONP's flat 13%.

### Example 4 — High earner, S/ 20,000/month, AFP PROFUTURO (flow scheme)

Salary S/ 20,000 > RMA S/ 12,598.91, so the **prima is capped** at the RMA; the commission is charged on full remuneration.

**Example 4 computation table**

| Step | Computation | S/ |
| --- | --- | --- |
| Annual remuneration (12 months) | 20,000 × 12 | 240,000.00 |
| Less 7 UIT exemption | — | 38,500.00 |
| Net annual taxable income | 240,000 − 38,500 | 201,500.00 |
| Band placement | 201,500 / 5,500 = 36.6 UIT → Band 4 (35–45 UIT) | — |
| Income tax — cumulative at 35 UIT (S/ 192,500) | (from Section 2 table) | 27,775.00 |
| Income tax — Band 4 (20% × (201,500 − 192,500)) | 9,000 × 20% | 1,800.00 |
| Annual income tax | 27,775 + 1,800 | 29,575.00 |
| Monthly income tax | 29,575 ÷ 12 | 2,464.58 |
| AFP mandatory (10% × 20,000) | individual account (no cap) | 2,000.00 |
| AFP insurance prima (1.37% × RMA 12,598.91) | capped | 172.61 |
| AFP commission — PROFUTURO flow (1.69% × 20,000) | on full remuneration | 338.00 |
| Total AFP withholding | 2,000 + 172.61 + 338.00 | 2,510.61 |
| **Net monthly salary** | 20,000 − 2,510.61 − 2,464.58 | **15,024.81** |
| EsSalud (employer, 9% × 20,000) | on top | 1,800.00 |

> Prima cap check: 1.37% × 12,598.91 = 172.6051 → S/ 172.61 ✓ (not 1.37% × 20,000 = S/ 274.00). The mandatory 10% and the commission are NOT RMA-capped — only the prima is.

### Example 5 — Non-domiciled employee, S/ 15,000 gross

**Example 5 computation table**

| Step | Computation | S/ |
| --- | --- | --- |
| Gross Peruvian-source remuneration | — | 15,000.00 |
| Income tax (30% flat, no deductions, no 7 UIT) | 15,000 × 30% | 4,500.00 |
| **Net to non-domiciled employee** | 15,000 − 4,500 | **10,500.00** |

> Non-domiciled employment income is taxed at a **30% flat rate on gross** (TUO LIR) — no 7 UIT exemption, no progressive schedule. (PwC) EsSalud/pension treatment for a non-domiciled assignment must be confirmed per the specific arrangement **[RESEARCH GAP]**.

### Example 6 — Employer cost for an S/ 8,000/month employee

**Example 6 computation table**

| Step | Computation | S/ |
| --- | --- | --- |
| Monthly base salary | — | 8,000.00 |
| EsSalud (employer, 9% × 8,000) | on top | 720.00 |
| **Total monthly employer payroll-contribution cost** | 8,000 + 720 | **8,720.00** |
| Memo: pension (ONP/AFP) and income tax | withheld from the employee — NOT an employer cost | — |
| Memo: CTS / gratificaciones / vacation | **out of scope — provision separately** | **[RESEARCH GAP]** |

> The only payroll contribution the employer pays on top of salary is the **9% EsSalud** (S/ 720). Pension and income tax are employee-borne withholdings. CTS, two gratificaciones, and vacation are statutory employer costs but are out of scope for this skill and must be provisioned separately.

## Section 10 -- Tier 1 Rules (deterministic — the skill applies these directly)

- **UIT 2026 and 7 UIT exemption** — UIT 2026 = S/ 5,500; the 7 UIT standard exemption = S/ 38,500 for 2026.  _(PwC; TUO LIR)_

**Domiciled 5th-category progressive income tax bands**  _(PwC; TUO LIR Art. 53)_

| Band | Rate |
| --- | --- |
| ≤5 UIT | 8% |
| 5–20 UIT | 14% |
| 20–35 UIT | 17% |
| 35–45 UIT | 20% |
| >45 UIT | 30% |

- **Additional up to 3 UIT deduction** — The additional up to 3 UIT deduction is not applied by the employer at source by default — default S/ 0 and reconcile at taxpayer level.  _(PwC; TUO LIR Art. 46)_
- **Non-domiciled employment income tax rate** — 30% flat on gross, no deductions, no 7 UIT exemption  _(PwC; TUO LIR)_
- **Pension is employee-borne** — The pension is employee-borne and withheld, into exactly one system: ONP/SNP 13% (no cap) or AFP (10% mandatory + 1.37% prima + per-AFP commission). The employer contributes nothing to the pension.  _(PwC; SBS; ONP)_
- **AFP prima cap** — AFP prima (1.37%) is capped at the RMA (S/ 12,598.91, Q2 2026); the 10% mandatory and the commission are charged on full remuneration.  _(SBS)_
- **EsSalud rate** — 9%, employer-borne, no upper cap, base floored at 1 RMV; up to 25% of EPS payments creditable.  _(PwC; EsSalud)_
- **Employer's only on-top payroll contribution** — The employer's only on-top payroll contribution is 9% EsSalud; pension and income tax are employee withholdings.  _(PwC)_
- **RMV (minimum wage)** — S/ 1,130/month since 1 January 2025 (DS 006-2024-TR)  _(Presidencia; Garrigues)_
- **Filing mechanics for income tax, EsSalud, ONP, AFP** — Income tax (5th cat.), EsSalud, and ONP are declared monthly via PLAME (Formulario Virtual N° 601) to SUNAT; AFP amounts are paid within the first 5 business days of the following month.  _(SUNAT; SBS)_
- **T-Registro registration deadline** — New workers must be registered in T-Registro within 24 hours of start date.  _(SUNAT)_
- **Currency and tax year** — Currency is PEN (Sol) only; the tax year is the calendar year.  _(PwC)_

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

These items depend on facts or sources not fully resolved in this research. The skill must surface them and recommend professional review rather than asserting a single answer.

**Tier 2 Catalogue**

| Ref | Issue | What the reviewer must resolve |
| --- | --- | --- |
| **[T2-1]** | UIT 2025 (S/ 5,350) | Confirm against the SUNAT/MEF Supreme Decree if the run targets 2025. **[RESEARCH GAP]** |
| **[T2-2]** | AFP commission rates and the RMA prima cap | Both reset periodically (commission monthly devengue; RMA quarterly). Pull the live SBS figure at publication time. **[RESEARCH GAP]** |
| **[T2-3]** | EsSalud 9% rate and RMV-floor cite | The SUNAT EsSalud page did not itself state the 9% or the RMV minimum base in the fetched content; 9% is via PwC and the RMV floor is a general labour rule — confirm the exact regulatory cite. |
| **[T2-4]** | Gratificaciones in the income-tax projection | Confirm the 14-month projection mechanics, timing, and the 9% bonificación extraordinaria paid in lieu of EsSalud on gratificaciones. **[RESEARCH GAP]** |
| **[T2-5]** | Additional 3 UIT deduction | Confirm the qualifying-expense categories, documentation, and whether/when the employer reflects it. |
| **[T2-6]** | EPS credit (25%) mechanics | Confirm how the EPS credit against EsSalud is computed and filed. |
| **[T2-7]** | Overtime / night / Sunday / holiday premiums and maximum hours | Not researched here — confirm from Peruvian labour law and any convenio colectivo. |
| **[T2-8]** | CTS, gratificaciones, vacation accruals; severance; BIK | Not in this research dataset — reviewer to populate. |
| **[T2-9]** | Exact PLAME monthly deadline | Tied to the last digit of the employer's RUC per SUNAT's annual cronograma — confirm the specific date for the period. |
| **[T2-10]** | EsSalud/pension treatment for non-domiciled assignments | Confirm whether EsSalud and pension apply alongside the 30% income-tax withholding for a given assignment. |

## Section 12 -- Filing Obligations

### Registration

**Registration filing**  _(SUNAT)_

| Filing | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| **T-Registro** (registro de empleadores y trabajadores) | Register each new worker (and the employer) | Within **24 hours** of start date | SUNAT |

Late T-Registro can draw a SUNAFIL fine of up to S/ 123,750. (SUNAT) **[T2 — confirm the current SUNAFIL fine schedule.]**

### Monthly — PLAME

**Monthly PLAME and AFP filing**  _(SUNAT; SBS)_

| Form / system | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| **PLAME (Planilla Mensual de Pagos) — Formulario Virtual N° 601** | Single monthly electronic declaration consolidating 5th-category income-tax withholding, EsSalud (9%), ONP (13%), AFP data, SCTR, and per-worker remuneration | Monthly, by the date matching the **last digit of the employer's RUC** per SUNAT's annual cronograma; rolls to the next business day if the due date is non-business; window opens the first business day of the following month | SUNAT |
| AFP remittance (via AFPnet) | Pay AFP mandatory / prima / commission | Within the first **5 business days** of the following month | SBS |

### Annual — employees

**Annual employee filing**  _(SUNAT (personas))_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| **Formulario Virtual N° 709** | Employee annual income-tax return — only where the employee has additional income/deductions; pure single-employer wage earners generally need not file | Per the last RUC/DNI digit in SUNAT's annual cronograma | SUNAT (personas) **[T2-9 — confirm the specific date]** |

## Section 13 -- Penalties

Figures below come from SUNAT guidance and the Tax Code (Código Tributario, TUO DS 133-2013-EF); confirm exact article wording and current amounts. **[T2]**

**Penalties table**  _(Código Tributario Art. 176, num. 1 (SUNAT); Régimen de Gradualidad (SUNAT); SUNAFIL)_

| Infraction | Penalty | Reference |
| --- | --- | --- |
| **Failure to file PLAME on time** | Base fine **1 UIT** (S/ 5,500, General / MYPE Tax Regime); **50% UIT** (S/ 2,750) for RER; **0.6%** of monthly net income for Nuevo RUS | Código Tributario Art. 176, num. 1 (SUNAT) |
| **Régimen de Gradualidad** (voluntary filing before SUNAT notice) | Fine reduction up to **100%** (or up to 95% with payment) | Régimen de Gradualidad (SUNAT) |
| **Late T-Registro** | Up to **S/ 123,750** | SUNAFIL **[T2 — confirm current schedule]** |

Default interest and additional sanctions may apply. Record-retention requirements were not part of this research dataset. **[RESEARCH GAP — confirm record-retention period.]**

## Section 14 -- Excel Working Paper Template

A reviewer-ready annual working paper should contain the following columns (one row per employee). Inputs are entered; computed cells follow the Section 2 withholding order exactly.

**Excel working paper column table**  _(—)_

| Col | Heading | Type | Formula / source |
| --- | --- | --- | --- |
| A | Employee name | Input | — |
| B | RUC / DNI | Input | SUNAT identifier |
| C | Domicile | Input | domiciled / non-domiciled |
| D | Pension system | Input | ONP / AFP-{HABITAT,INTEGRA,PRIMA,PROFUTURO} |
| E | Monthly base salary (S/) | Input | remuneración |
| F | UIT (year) | Input | `5500` (2026) |
| G | Annual remuneration (S/) | Computed | `E * 12` (add gratificaciones if in scope) |
| H | 7 UIT exemption | Computed | `F * 7` |
| I | Additional deduction (≤3 UIT) | Input | `0` unless documented, capped at `F*3` |
| J | Net annual taxable income | Computed | `MAX(G - H - I, 0)` |
| K | Annual income tax | Computed | progressive 8/14/17/20/30% on J (Section 2 cumulative table) |
| L | Monthly income tax | Computed | `K / 12` |
| M | Monthly pension (ONP 13%) | Computed | `IF(D="ONP", E*13%, "")` |
| N | AFP mandatory (10%) | Computed | `IF(left(D,3)="AFP", E*10%, "")` |
| O | AFP prima (1.37%, RMA cap) | Computed | `IF(left(D,3)="AFP", MIN(E,12598.91)*1.37%, "")` |
| P | AFP commission (per-AFP %) | Computed | `IF(left(D,3)="AFP", E*comm%, "")` |
| Q | Total pension withheld | Computed | `IF(D="ONP", M, N+O+P)` |
| R | Net monthly salary | Computed | `E - Q - L` |
| S | EsSalud (employer, 9%) | Computed | `MAX(E, RMV) * 9%` |
| T | Total monthly employer cost | Computed | `E + S` (CTS/gratificación/vacation provisioned separately) |

For a non-domiciled employee (col C = non-domiciled), income tax = `E * 30%` on gross with no deductions; columns H–Q do not apply. Footer checks: sum of column L + EsSalud + ONP ties to the PLAME (Form 601) remittance; sum of N+O+P ties to the AFP remittance; sum of R ties to total net wages disbursed.

## Section 15 -- Peruvian Bank Statement & Terminology Reading Guide

**Terminology reading guide**  _(—)_

| Spanish term | English | Relevance |
| --- | --- | --- |
| Remuneración / sueldo | Salary / wage | Starting figure for all computations |
| Sueldo neto | Net salary | What the employee receives |
| Renta de quinta categoría | Fifth-category (employment) income | The category this skill covers |
| Renta neta imponible | Net taxable income | After the 7 UIT exemption, before income tax |
| Retención de quinta | Fifth-category withholding | The monthly withholding mechanism |
| UIT | Tax reference unit | S/ 5,500 (2026); defines the brackets |
| EsSalud | Social-health insurance | 9%, employer-borne |
| ONP / SNP | Public pension | 13%, withheld from the employee |
| AFP | Private pension fund | 10% + prima + commission, withheld |
| Prima de seguro | Insurance premium (AFP) | 1.37%, RMA-capped |
| Comisión (sobre flujo / mixta) | AFP commission | Varies by AFP |
| RMA | Maximum insurable remuneration | S/ 12,598.91 (Q2 2026), caps the AFP prima |
| RMV | Minimum wage | S/ 1,130/month |
| Gratificación | Statutory bonus | July / December (out of scope here) |
| CTS | Service-time compensation | Statutory benefit (out of scope here) |
| PLAME | Monthly payroll declaration | Formulario Virtual N° 601 to SUNAT |
| T-Registro | Employer/worker registry | Register new workers within 24h |
| SUNAT | Tax administration | Receives income tax, EsSalud, ONP via PLAME |
| SBS | Banking/insurance/AFP supervisor | Sets AFP commission/prima tables |
| RUC | Taxpayer ID | Determines PLAME due date by last digit |
| Sol (S/ / PEN) | Currency | All figures in Soles |

## Section 16 -- Onboarding Fallback

When key facts are missing, ask the user these questions before computing. If a question is unanswered, apply the Section 6 conservative default and clearly flag the assumption.

1. What is the employee's monthly base salary in PEN?
2. Is the employee domiciled or non-domiciled in Peru? (Non-domiciled → 30% flat on gross.)
3. Which pension system — ONP/SNP (13%) or AFP? If AFP, which (HABITAT / INTEGRA / PRIMA / PROFUTURO) and flow or mixed scheme?
4. Which month and year is this pay run for? (Determines the UIT, RMV, and SBS AFP devengue.)
5. Does the employee have a documented additional 3 UIT deduction? (If unproven → S/ 0 at source.)
6. Do gratificaciones fall in this period? (Currently flagged out of scope — reviewer to add.)

## Section 17 -- Interaction with Other Skills

**Interaction with other skills table**  _(—)_

| Scenario | Skill to use |
| --- | --- |
| Employee payroll (5th-cat. income tax + EsSalud + ONP/AFP) | **This skill (peru-payroll.md)** |
| Peru IGV (VAT) returns | peru-igv.md |
| Peru personal income tax (annual / other categories) | peru-income-tax.md |
| Peru social-security mechanics (detailed EsSalud/ONP/AFP) | peru-social-security.md |
| Cross-border / posted workers / totalization | cross-border-payroll-coordination.md |
| Shared workflow runbook | payroll-workflow-base.md |

### Key handoff points

- Payroll → Bookkeeping: Gross wages and the 9% employer EsSalud are expenses; withheld income tax, ONP, and AFP amounts are liabilities until remitted via PLAME/AFPnet.
- Payroll → Income tax: Most single-employer wage earners are settled through withholding; some file Formulario Virtual N° 709 where they have additional income/deductions.
- Payroll → Social security: ONP/AFP contributions build the employee's pension entitlement; EsSalud funds health coverage. CTS, gratificaciones, and vacation are separate statutory benefits (out of scope here).

## Section 18 -- Reference Material

**Reference material table**  _(—)_

| # | Source | Publisher | URL |
| --- | --- | --- | --- |
| 1 | Peru — Individual — Taxes on personal income (UIT 5,500; 7 UIT; 8%–30% schedule; 30% non-domiciled) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income |
| 2 | Peru — Individual — Other taxes (EsSalud 9%; ONP 13%) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/peru/individual/other-taxes |
| 3 | Declaración y pago de los aportes EsSalud | SUNAT (orientación) | https://orientacion.sunat.gob.pe/08-declaracion-y-pago-de-los-aportes-essalud |
| 4 | Declaración y pago de aportes al Sistema Nacional de Pensiones (ONP) | SUNAT (orientación) | https://orientacion.sunat.gob.pe/declaracion-y-pago-de-aportes-al-sistema-nacional-de-pensiones-onp |
| 5 | Comisiones y prima del SPP (AFP table, devengue 2026-06; RMA cap) | SBS | https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx |
| 6 | RMV S/ 1,130 (anuncio Presidencia) | Presidencia del Perú (gob.pe) | https://www.gob.pe/institucion/presidencia/noticias/1082104-presidenta-boluarte-anuncia-aumento-de-la-remuneracion-minima-vital-a-1130-soles |
| 7 | Perú aumenta a S/ 1,130 la RMV 2025 (DS 006-2024-TR) | Garrigues | https://www.garrigues.com/es_ES/noticia/peru-aumenta-105-soles-remuneracion-minima-vital-2025-trabajadores-sujetos-regimen-laboral |
| 8 | Obligaciones del empleador — T-Registro (24h; SUNAFIL fine) | SUNAT (orientación) | https://orientacion.sunat.gob.pe/03-obligaciones-del-empleador-t-registro |
| 9 | Formulario Virtual 601 — PLAME web | SUNAT (orientación) | https://orientacion.sunat.gob.pe/formulario-virtual-601-plame-web |
| 10 | Declaración y pago — trabajador dependiente (Formulario 709) | SUNAT (personas) | https://personas.sunat.gob.pe/trabajador-dependiente/declaracion-pago-0 |
| 11 | Régimen de gradualidad — multa Art. 176 num. 1 | SUNAT (gob.pe) | https://www.gob.pe/institucion/sunat/informes-publicaciones/6369903-regimen-de-gradualidad-aplicable-a-la-multa-por-no-presentar-las-declaraciones-en-la-fecha-de-vencimiento-articulo-176-numeral-1-del-codigo-tributario |
| 12 | Régimen de gradualidad (facultad sancionadora) | SUNAT (emprender) | https://emprender.sunat.gob.pe/acciones-sunat/facultad-sancionadora/regimen-gradualidad |

Primary authorities: SUNAT (https://www.sunat.gob.pe; orientacion.sunat.gob.pe; personas.sunat.gob.pe); SBS (https://www.sbs.gob.pe); EsSalud (https://www.essalud.gob.pe); ONP (https://www.onp.gob.pe); Presidencia/MTPE (https://www.gob.pe).

### Test Suite

Run these to validate any implementation of this skill. Expected results use 2026 figures (UIT S/ 5,500), domiciled status, the additional 3 UIT deduction at S/ 0, and a 12-month projection unless stated otherwise.

1. Low earner, ONP. S/ 3,000/month, ONP. Expect: net annual taxable S/ 0.00, annual income tax S/ 0.00, ONP S/ 390.00/month, net salary S/ 2,610.00, employer EsSalud S/ 270.00.
2. Mid earner, ONP. S/ 8,000/month, ONP. Expect: net annual taxable S/ 57,500.00, annual income tax S/ 6,400.00 (S/ 2,200 + S/ 4,200), monthly income tax S/ 533.33, ONP S/ 1,040.00, net salary S/ 6,426.67, employer EsSalud S/ 720.00.
3. Mid earner, AFP INTEGRA. S/ 8,000/month, AFP INTEGRA flow. Expect: AFP S/ 1,033.60 (800 + 109.60 + 124.00 = 12.92%), monthly income tax S/ 533.33, net salary S/ 6,433.07, employer EsSalud S/ 720.00.
4. High earner, AFP PROFUTURO, prima capped. S/ 20,000/month, AFP PROFUTURO flow. Expect: net annual taxable S/ 201,500.00, annual income tax S/ 29,575.00 (S/ 27,775 + 20% × S/ 9,000), monthly income tax S/ 2,464.58, AFP S/ 2,510.61 (2,000 + prima 172.61 capped at RMA + commission 338.00), net salary S/ 15,024.81, employer EsSalud S/ 1,800.00.
5. Non-domiciled flat rate. S/ 15,000 gross to a non-domiciled employee. Expect: income tax S/ 4,500.00 (30% on gross, no deductions), net S/ 10,500.00.
6. Employer cost. S/ 8,000/month employee. Expect: employer payroll-contribution cost = salary S/ 8,000 + EsSalud S/ 720 = S/ 8,720.00 (pension and income tax are employee withholdings; CTS/gratificación/vacation out of scope).
7. Bracket cumulative check. Confirm cumulative tax at band tops: 5 UIT → S/ 2,200; 20 UIT → S/ 13,750; 35 UIT → S/ 27,775; 45 UIT → S/ 38,775.
8. Prima cap check. Confirm the AFP prima for an S/ 20,000 salary is 1.37% × S/ 12,598.91 = S/ 172.61 (capped), NOT 1.37% × S/ 20,000 = S/ 274.00.
9. 7 UIT exemption. Confirm an S/ 36,000/year (S/ 3,000/month) earner has a S/ 0 income-tax base after the 7 UIT (S/ 38,500) exemption.
10. Pension is employee-borne. Confirm ONP/AFP are withheld from the employee and the employer adds only 9% EsSalud on top.
11. Additional-deduction default. Additional 3 UIT deduction unconfirmed — confirm the skill applies S/ 0 (not S/ 16,500) and flags the assumption.
12. Domicile guard. Confirm the skill applies the 30% flat (no deductions) only when non-domicile is confirmed, and the progressive 8%–30% schedule otherwise.

## PROHIBITIONS

- NEVER claim Peru has no income tax — fifth-category income tax applies to employment income at 8%–30% above the 7 UIT exemption (TUO LIR).
- NEVER apply the additional 3 UIT deduction at source without documented qualifying expenses — default to S/ 0 and flag it.
- NEVER treat the pension (ONP 13% / AFP ≈12.84%–13.06%) as an employer cost — it is withheld from the employee.
- NEVER assume ONP vs AFP — the system is the employee's choice and must be confirmed before computing the pension.
- NEVER apply the AFP prima (1.37%) above the RMA (S/ 12,598.91, Q2 2026) — the prima is RMA-capped; the 10% mandatory and the commission are not.
- NEVER use a single "average" AFP commission — use the per-AFP figure from the live SBS table for the correct devengue.
- NEVER deduct EsSalud (9%) from the employee's pay — it is an employer contribution on top of salary.
- NEVER apply the progressive schedule to a non-domiciled employee — non-domiciled pay a 30% definitive flat rate on gross.
- NEVER run a full-time employee below the RMV (S/ 1,130/month).
- NEVER omit T-Registro within 24 hours of a new worker's start date — SUNAFIL fines apply.
- NEVER quote a penalty figure as definitive — the Código Tributario / SUNAFIL amounts here are pending reviewer confirmation.
- NEVER present payroll computations as definitive — always label them as estimated and direct the user to a licensed Peruvian Contador Público Colegiado.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed Contador Público Colegiado or tax adviser in Peru) before implementation.

The most up-to-date, verified version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
