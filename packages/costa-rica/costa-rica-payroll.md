---
name: costa-rica-payroll
description: Use this skill whenever asked about Costa Rica payroll processing for employed persons (planilla). Trigger on phrases like "Costa Rica payroll", "planilla CCSS", "cuotas obrero-patronales", "impuesto al salario", "retención salario Costa Rica", "cargas sociales", "CCSS contribution", "IVM", "SEM", "FODESAF", "aguinaldo", "cesantía", "salario mínimo Costa Rica", "TRIBU-CR retenciones", "form 137", "D-103 replacement", "net salary Costa Rica", "gross to net colones", "SICERE", "INS riesgos del trabajo", "base mínima contributiva", or any question about computing employee pay, salary withholding tax, or social-security contributions for Costa Rica-based employees. This skill covers impuesto al salario (monthly income-tax withholding), CCSS cuotas obrero-patronales (employee and employer), the separate INS work-risk policy, family tax credits, statutory aguinaldo, cesantía, minimum wage, and filing obligations via TRIBU-CR and SICERE. ALWAYS read this skill before processing any Costa Rica payroll.
version: 0.1
jurisdiction: CR
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Costa Rica Payroll Skill v0.1 (Tier 2 — research-verified, pending accountant sign-off)

## Costa Rica Payroll Skill v0.1 (Tier 2 — research-verified, pending accountant sign-off)

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Costa Rica (national, code CR) |
| Currency | CRC -- Costa Rican colón (₡/¢) only |
| Standard pay frequency | Monthly or quincenal (bi-monthly, 15th + month-end); weekly permitted for jornaleros |
| Tax year | Calendar / fiscal year (1 January -- 31 December) |
| Income-tax withholding system | Impuesto único sobre las rentas del trabajo dependiente (impuesto al salario) -- monthly employer withholding, 5-band schedule |
| Income-tax authority | Dirección General de Tributación (DGT), Ministerio de Hacienda -- via TRIBU-CR portal (replaced ATV / D-103 on 6 Oct 2025) |
| Social-security authority | Caja Costarricense de Seguro Social (CCSS) -- via SICERE / Oficina Virtual |
| Work-risk insurer | Instituto Nacional de Seguros (INS) -- riesgos del trabajo policy |
| Minimum-wage authority | Ministerio de Trabajo y Seguridad Social (MTSS) |
| Key legislation | Ley del Impuesto sobre la Renta No. 7092, Título II; Decreto Ejecutivo No. 44772-H (2025 brackets); Ley Constitutiva de la CCSS No. 17; Ley de Protección al Trabajador No. 7983; Código de Trabajo; Código de Normas y Procedimientos Tributarios (CNPT) Ley No. 4755; Decreto No. 44756-MTSS (2025 minimum wages) |
| Filing portals | TRIBU-CR (income-tax withholding); SICERE / Oficina Virtual (CCSS planilla) |
| Validated by | Pending -- requires sign-off by a Costa Rican Contador Público Autorizado (CPA) |
| Skill version | 0.1 |

> **Tier-2 note.** All figures below are research-verified against official decrees and Big-4 / legal-firm sources but have **not** yet been reviewed section-by-section by a warranted Costa Rican accountant. Where a figure rests on a single secondary source or the official table could not be machine-read, it is flagged inline as `[RESEARCH GAP — reviewer to confirm]`.

## Section 2 -- Income Tax Withholding (Impuesto al Salario)

The employer withholds **impuesto al salario** monthly on each employee's gross monthly remuneration, using the 5-band schedule in Decreto Ejecutivo No. 44772-H (La Gaceta No. 227, 03 Dec 2024, effective 01 Jan 2025). For an employee with a single employer this withholding is the employee's **final** tax on that employment income (*impuesto único sobre el trabajo dependiente*) — no annual return is required unless the employee has multiple employers or other income sources.

### Impuesto al Salario Brackets (2025, monthly, CRC)

**Impuesto al Salario Brackets (2025, monthly, CRC)**  _(Decreto 44772-H, confirmed against the official UCR Oficina de Recursos Humanos "Tabla del Impuesto al Salario 2025")_

| Monthly gross remuneration band (₡) | Marginal rate | Tax on full band (₡) | Cumulative tax at top of band (₡) |
| --- | --- | --- | --- |
| 0 to 922,000 | 0% (exento) | 0 | 0 |
| over 922,000 to 1,352,000 | 10% | 43,000 | 43,000 |
| over 1,352,000 to 2,373,000 | 15% | 153,150 | 196,150 |
| over 2,373,000 to 4,745,000 | 20% | 474,400 | 670,550 |
| over 4,745,000 | 25% | (open) | (open) |

- **Cumulative-tax check** — 0 + 43,000 + 153,150 + 474,400 = 670,550 at ₡4,745,000 (top of the 20% band). Tax above that point = 670,550 + 25% × (gross − 4,745,000).  _(Decreto 44772-H)_

### Computation Method

- **Withholding computation steps** — 1. Take gross monthly remuneration (salario bruto) — the income-tax base. Per authoritative TRIBU-CR guidance, the employee's CCSS contribution (10.67%) is NOT deducted before applying the brackets; the base is gross. [RESEARCH GAP — reviewer to confirm: at least one EOR summary implied a net-of-CCSS base; conservative default below uses GROSS.] 2. Apply the marginal-band schedule above to obtain gross income tax. 3. Subtract any family tax credits (créditos familiares) the employee qualifies for (Section 2.1). 4. The result is the monthly impuesto al salario to withhold. It cannot go below zero.  _(TRIBU-CR guidance)_

### Section 2.1 -- Family Tax Credits (Créditos Familiares, 2025, monthly)

**Family Tax Credits (Créditos Familiares, 2025, monthly)**  _(Decreto 44772-H / UCR table)_

| Credit | Monthly amount (₡) | Condition |
| --- | --- | --- |
| Per qualifying child (hijo) | 1,720 | Minor, or studying up to age 25, or lifelong if disabled |
| Per spouse (cónyuge) | 2,600 | One spouse only if both are taxpayers |

- **Credit eligibility rules** — Credits are not available to legal entities. If both spouses are taxpayers, the spouse credit is claimed by only one of them.  _(Decreto 44772-H / UCR table)_

## Section 3 -- Social Security -- Employee Deductions (CCSS, 2025)

Employee cuotas obrero-patronales are withheld from gross salary and remitted to CCSS via SICERE. Source: CCSS / Hacienda guidance, itemised in Officium Legal table cross-checked with EY/BDO alerts.

**Employee CCSS deductions table**  _(CCSS / Hacienda guidance, itemised in Officium Legal table cross-checked with EY/BDO alerts)_

| Fund | Employee rate (2025) |
| --- | --- |
| SEM -- Seguro de Enfermedad y Maternidad (health/maternity) | 5.50% |
| IVM -- Invalidez, Vejez y Muerte (pension) | 4.17% |
| Banco Popular y de Desarrollo Comunal | 1.00% |
| **TOTAL employee CCSS** | **10.67%** |

- **Sum check** — 5.50 + 4.17 + 1.00 = 10.67%. ✔
- **Employee CCSS from 01 Jan 2026** — 10.83% (5.50 + 4.33 + 1.00), IVM rises from 4.17% to 4.33%  _(BDO Costa Rica / Globalex CR / CCSS board decision)_

## Section 4 -- Social Security -- Employer Contributions (CCSS, 2025)

Employer cuotas obrero-patronales fund CCSS plus several public institutions and the Ley de Protección al Trabajador funds. Source: Officium Legal itemised table cross-checked with secondary EOR/Big-4 guides.

**Employer CCSS contributions table**  _(Officium Legal itemised table cross-checked with secondary EOR/Big-4 guides)_

| Fund | Employer rate (2025) |
| --- | --- |
| SEM -- Seguro de Enfermedad y Maternidad | 9.25% |
| IVM -- Invalidez, Vejez y Muerte | 5.42% |
| Asignaciones Familiares (FODESAF) | 5.00% |
| INA -- Instituto Nacional de Aprendizaje | 1.50% |
| FCL -- Fondo de Capitalización Laboral (Ley 7983) | 1.50% |
| ROP / pension complementaria + Banco Popular aporte patronal (grouped) | 2.00% |
| Banco Popular patronal | 0.50% |
| IMAS -- Instituto Mixto de Ayuda Social | 0.50% |
| **TOTAL employer CCSS** | **26.67%** |

- **Research gap note on employer total** — [RESEARCH GAP — reviewer to confirm: the authoritative employer total is 26.67% (confirmed across CCSS/Hacienda/Big-4 sources), but the line-item breakdown above sums arithmetically to 25.67%. The internal allocation of the ~2.00% "ROP/pension + Banco Popular" tranche and the separate 0.50% Banco Popular patronal line is itemised differently by source, and the official CCSS rate table could not be machine-read. Use the CONFIRMED 26.67% total for cost computations; treat the per-fund split as indicative pending a Costa Rican accountant's confirmation of the exact 1.00% reconciling line.]
- **Employer CCSS from 01 Jan 2026** — 26.83% (only the IVM line changes, from 5.42% to 5.58%). The State contribution to IVM also rises from 1.57% to 1.75%. Schedule valid through 31 Dec 2028, with a further increase from 01 Jan 2029.  _(BDO Costa Rica / Globalex CR / CCSS 2019 board decision)_

### Section 4.1 -- INS Riesgos del Trabajo (Work-Risk Insurance) -- SEPARATE

- **Overview** — Every employer must also hold a riesgos del trabajo (workers' compensation) policy with INS. This is a mandatory employer cost on top of the 26.67% CCSS total, and is NOT included in it in standard breakdowns.

**INS Riesgos del Trabajo table**

| Item | Employer cost |
| --- | --- |
| INS riesgos del trabajo | ~1.0% of payroll, risk-rated (typically ~1%–2% range) `[RESEARCH GAP — reviewer to confirm: rate is set per the company's occupational risk class; ~1% is illustrative only]` |

## Section 5 -- Total Social-Charge Cost Summary

**Total Social-Charge Cost Summary**

| Party | 2025 | From 01 Jan 2026 |
| --- | --- | --- |
| Employee CCSS (withheld from gross) | 10.67% | 10.83% |
| Employer CCSS | 26.67% | 26.83% |
| Employer INS work-risk (separate) | ~1.0% (risk-rated) | ~1.0% (risk-rated) |
| **Approx. total employer on-cost** | **~27.67%** (26.67% + ~1% INS) | **~27.83%** (26.83% + ~1% INS) |

- **Rate switch rule** — Only the IVM line changes between 2025 and 2026 (employer +0.16, employee +0.16). Use 2025 rates for pay periods up to 31 Dec 2025; switch to 2026 rates for pay periods on/after 01 Jan 2026.

## Section 6 -- Thresholds and Contribution Bases

**Thresholds and Contribution Bases**

| Item | Value (2025) | Source |
| --- | --- | --- |
| Income-tax-free monthly amount (employment) | ₡922,000/month | Decreto 44772-H |
| Base Mínima Contributiva (BMC) -- IVM | ₡287,360/month | EY Centroamérica / CCSS |
| Base Mínima Contributiva (BMC) -- SEM | ₡307,013/month | EY Centroamérica / CCSS |
| Reduced BMC for salaried workers (from 01 Jan 2025) | 50% of the full BMC, applies to all wage-earners regardless of age; contributions are still **reported on actual salary earned** | EY / BDS / CCSS |
| Salario base (penalty calculations) | ₡462,200 | CNPT Ley 4755 / CMFLca |

## Section 7 -- Minimum Wage (2025)

- **Occupation-based minimum wage rule** — Costa Rica has no single national minimum wage — minimum wages are set by occupation in Decreto No. 44756-MTSS (La Gaceta No. 232, 10 Dec 2024), with a +2.37% adjustment effective 01 Jan 2025. Use the MTSS category matching the role.  _(Decreto No. 44756-MTSS)_

**Minimum Wage (2025) table**  _(Decreto 44756-MTSS, reported by La Nación and MTSS official table)_

| Occupational category (private sector) | Monthly minimum (₡) |
| --- | --- |
| Trabajador No Calificado (generic unskilled) | 367,108 |
| Semicalificado (semi-skilled) | 399,203 |
| Calificado (skilled) | 413,023 |
| Técnicos, bachiller universitario, licenciado universitario | Higher tiers per the MTSS decree `[RESEARCH GAP — reviewer to confirm specific técnico/universitario figures from the MTSS table]` |

## Section 8 -- Statutory Pay Items

### Section 8.1 -- Aguinaldo (13th-Month Salary) -- Mandatory

**Aguinaldo rules table**  _(Código de Trabajo / AG Legal)_

| Rule | Detail |
| --- | --- |
| Calculation | Sum of all ordinary + extraordinary salaries earned **01 Dec – 30 Nov**, divided by 12 |
| Payment deadline | By **20 December** |
| Tax / CCSS treatment | **Exempt** from income tax and CCSS contributions |
| Permitted deductions | Only court-ordered child support (pensión alimentaria) |

### Section 8.2 -- Cesantía (Severance) -- on Unjustified Dismissal / Employer Cause

**Cesantía entitlement table**  _(Código de Trabajo)_

| Service | Entitlement |
| --- | --- |
| First year | ~19.5 days of wages |
| Subsequent years | up to ~22 days per year |
| Cap | 8 years of service |

## Section 9 -- Conservative Defaults

- **CCSS rates by pay period** — Use 2025 totals (employer 26.67% / employee 10.67%) for periods up to 31 Dec 2025; switch to 26.83% / 10.83% only for pay periods on/after 01 Jan 2026. Only the IVM line changes.  _(BDO / CCSS board)_
- **Income-tax base is GROSS** — Apply impuesto al salario brackets to gross monthly remuneration; do not pre-deduct employee CCSS from the income-tax base.  _(TRIBU-CR guidance — one EOR source disagreed; flag for confirmation)_
- **INS is a SEPARATE employer cost** — Treat riesgos del trabajo (~1%, risk-rated) as additional to the 26.67% CCSS total, not inside it.  _(Standard breakdowns exclude INS)_
- **Minimum wage is occupation-specific** — Use the MTSS decree category matching the role; never assume a single national floor.  _(Decreto 44756-MTSS)_
- **Use the CONFIRMED 26.67% total** — Not the per-fund sum (which reconciles to 25.67% from secondary sources) when computing employer cost.  _(See Section 4 RESEARCH GAP)_
- **Aguinaldo is exempt** — Aguinaldo is exempt from income tax and CCSS — never withhold on it (except court-ordered pensión alimentaria).  _(Código de Trabajo)_

## Section 10 -- Required Inputs + Refusal Catalogue

### Required Inputs

**Required Inputs table**

| Input | Why needed |
| --- | --- |
| Employee gross monthly remuneration (₡) | Base for both impuesto al salario and CCSS |
| Pay period date | Determines 2025 vs 2026 CCSS rates |
| Number of qualifying children + spouse-taxpayer status | Family tax credits (₡1,720/child, ₡2,600/spouse) |
| Whether employee has a single or multiple employers | Determines if monthly withholding is final |
| Occupational category | Minimum-wage compliance check |
| Company occupational risk class | INS riesgos del trabajo rate |
| Employer CCSS registration (inscripción patronal) status | Compliance / filing obligation |

### Refusal Catalogue — DO NOT proceed (refuse and request the missing item) if:

- **Refusal conditions** — - Gross monthly remuneration is not provided or is below the applicable occupational minimum wage (flag a minimum-wage breach). - The pay period straddles 31 Dec 2025 / 01 Jan 2026 without clarification of which rate set applies. - The employer is not registered with CCSS (inscripción patronal) — payroll cannot be lawfully run. - Family-credit claims are asserted without child/spouse documentation. - A net-pay target is given and you are asked to "gross up" without confirming the income-tax base treatment (gross vs net) — flag the RESEARCH GAP. - Aguinaldo is requested with income tax or CCSS withheld on it — refuse; it is exempt.

## Section 11 -- Transaction / Payment Pattern Library

Deterministic classification of common Costa Rican bank-statement lines (Spanish terms first, then English/EOR variants).

### Salary Credits (employee receiving)

**Salary Credits table**

| Pattern | Classification |
| --- | --- |
| SALARIO, PLANILLA, PAGO QUINCENA, DEPOSITO SALARIO | Net salary payment |
| AGUINALDO | 13th-month salary (exempt; paid by 20 Dec) |
| LIQUIDACION, CESANTIA, PREAVISO | Severance / termination payment |
| VACACIONES PAGADAS | Paid leave |

### Employer Debits (employer paying)

**Employer Debits table**

| Pattern | Classification |
| --- | --- |
| CCSS PLANILLA, SICERE, CAJA COSTARRICENSE | CCSS cuotas obrero-patronales remittance |
| FACTURA CCSS, RECIBO SICERE | CCSS auto-generated invoice (if planilla not filed) |
| HACIENDA, TRIBU-CR, RETENCION SALARIO, IMPUESTO AL SALARIO | Impuesto al salario withholding remittance to DGT |
| INS, RIESGOS DEL TRABAJO, POLIZA INS | INS work-risk policy premium |
| FODESAF, INA, IMAS, BANCO POPULAR APORTE | Component charges within CCSS planilla |
| PLANILLA SALARIOS, PAGO EMPLEADOS, TRANSFERENCIA NOMINA | Net wages disbursement to employees |
| PENSION ALIMENTARIA, EMBARGO JUDICIAL | Court-ordered child-support deduction |

## Section 12 -- Worked Examples

All examples use 2025 rates, gross income-tax base, employee CCSS 10.67%, employer CCSS 26.67%. Figures recomputed end-to-end.

### Example A -- Below tax threshold, 1 child

- Gross monthly: ₡800,000. Single employer. 1 qualifying child.
- Bank line: `DEPOSITO SALARIO ABC SA ₡715,360`
- Income tax: gross ₡800,000 ≤ ₡922,000 → **₡0** (child credit cannot create a refund).
- Employee CCSS: 800,000 × 10.67% = **₡85,360**.
- **Net pay = 800,000 − 0 − 85,360 = ₡714,640.**
- Employer CCSS cost: 800,000 × 26.67% = ₡213,360 (+ ~₡8,000 INS at ~1%).

### Example B -- Mid-band, 1 child credit

- Gross monthly: ₡1,000,000. Single employer. 1 qualifying child.
- Income tax (gross base): 10% × (1,000,000 − 922,000) = 10% × 78,000 = ₡7,800.
- Less child credit ₡1,720 → income tax withheld = **₡6,080**.
- Employee CCSS: 1,000,000 × 10.67% = ₡106,700.
- **Net pay = 1,000,000 − 106,700 − 6,080 = ₡887,220.**
- Employer CCSS: 1,000,000 × 26.67% = ₡266,700 (+ ~₡10,000 INS).

### Example C -- Skilled employee, single, no credits

- Gross monthly: ₡1,500,000. Single employer. No dependants.
- Income tax: 10% × (1,352,000 − 922,000) + 15% × (1,500,000 − 1,352,000)
  = 10% × 430,000 + 15% × 148,000 = 43,000 + 22,200 = **₡65,200**.
- Employee CCSS: 1,500,000 × 10.67% = ₡160,050.
- **Net pay = 1,500,000 − 160,050 − 65,200 = ₡1,274,750.**
- Employer CCSS: 1,500,000 × 26.67% = ₡400,050.

### Example D -- Manager with spouse + 2 children

- Gross monthly: ₡3,000,000. Single employer. Spouse (claimed) + 2 qualifying children.
- Income tax: cumulative at ₡2,373,000 = ₡196,150; plus 20% × (3,000,000 − 2,373,000) = 20% × 627,000 = 125,400 → ₡321,550 before credits.
- Credits: 2,600 (spouse) + 2 × 1,720 (children) = ₡6,040 → income tax withheld = **₡315,510**.
- Employee CCSS: 3,000,000 × 10.67% = ₡320,100.
- **Net pay = 3,000,000 − 320,100 − 315,510 = ₡2,364,390.**
- Employer CCSS: 3,000,000 × 26.67% = ₡800,100.

### Example E -- High earner, top band, single

- Gross monthly: ₡5,000,000. Single employer. No dependants.
- Income tax: cumulative at ₡4,745,000 = ₡670,550; plus 25% × (5,000,000 − 4,745,000) = 25% × 255,000 = 63,750 → **₡734,300**.
- Employee CCSS: 5,000,000 × 10.67% = ₡533,500.
- **Net pay = 5,000,000 − 533,500 − 734,300 = ₡3,732,200.**
- Employer CCSS: 5,000,000 × 26.67% = ₡1,333,500.

### Example F -- Aguinaldo (13th-month)

- Employee earned ₡1,000,000/month, 12 full months 01 Dec 2024 – 30 Nov 2025.
- Aguinaldo = (sum of salaries Dec–Nov) ÷ 12 = ₡12,000,000 ÷ 12 = **₡1,000,000**.
- Tax / CCSS: **exempt**. No withholding (unless a court-ordered pensión alimentaria applies).
- Must be paid by 20 December 2025. Bank line: `AGUINALDO ₡1,000,000`.

## Section 13 -- Tier 1 Rules (deterministic — apply automatically)

- **Tier 1 rules list** — 1. Apply the 2025 impuesto al salario schedule (0% / 10% / 15% / 20% / 25%) to gross monthly remuneration; band edges ₡922,000 / ₡1,352,000 / ₡2,373,000 / ₡4,745,000 (Decreto 44772-H). 2. Subtract family credits AFTER computing gross tax: ₡1,720/child, ₡2,600/spouse (one spouse only). Tax cannot go below ₡0. 3. Income tax withheld monthly is the employee's final tax if there is a single employer/source. 4. Withhold employee CCSS at 10.67% of gross (2025) / 10.83% (from 01 Jan 2026). 5. Compute employer CCSS at 26.67% of gross (2025) / 26.83% (from 01 Jan 2026). 6. Add the separate INS riesgos del trabajo employer cost (~1%, risk-rated) — never fold it into the CCSS total. 7. Aguinaldo = (salaries 01 Dec–30 Nov) ÷ 12; pay by 20 Dec; exempt from income tax and CCSS. 8. File impuesto al salario withholding via TRIBU-CR (form 137 + 207; D-138 for legal entities) within the first 15 calendar days of the following month. 9. File the CCSS planilla via SICERE within the reporting window (≈26th of the month to the 4th business day of the next); if not filed, CCSS auto-invoices on the 5th business day with a 2% surcharge on SEM and IVM. 10. Register the employer (inscripción patronal) and each new hire with CCSS within the first 8 business days of starting activity / hiring.  _(Decreto 44772-H)_

## Section 14 -- Tier 2 Catalogue (reviewer judgement required)

These items require a Costa Rican accountant's judgement and are flagged rather than auto-computed:

1. **Income-tax base (gross vs net of CCSS).** Conservative default is gross; one EOR source implied net. `[RESEARCH GAP — reviewer to confirm]`
2. **Exact employer fund split.** The per-fund breakdown reconciles to 25.67% from secondary sources but the confirmed total is 26.67%; the reconciling ~1% line needs confirmation. `[RESEARCH GAP — reviewer to confirm]`
3. **INS riesgos del trabajo rate.** Risk-rated per company occupational class (~1%–2%); the company-specific rate must be obtained from INS. `[RESEARCH GAP — reviewer to confirm]`
4. **Base Mínima Contributiva application.** Whether the 50% reduced BMC (from 01 Jan 2025) affects a specific low-wage or part-time worker's contributory floor — contributions are still reported on actual salary earned.
5. **Multi-employer reconciliation.** If the employee has more than one employer/source, an annual reconciliation may be required — outside monthly withholding.
6. **Specialised minimum-wage tiers** (técnico / universitario) and sector-specific arrangements.
7. **Cesantía exact day-count** within the ~19.5–22 days/year sliding scale and the 8-year cap for a specific tenure.
8. **Self-employed (actividad lucrativa) annual brackets** — out of scope for employer payroll; the live PwC page now renders 2026 figures and 2025 self-employed figures were not separately confirmed. `[RESEARCH GAP — out of scope]`

## Section 15 -- Excel Working Paper Template

Suggested columns for a monthly planilla working paper (one row per employee):

**Excel Working Paper Template table**

| Col | Header | Formula / Source |
| --- | --- | --- |
| A | Employee name | input |
| B | Cédula / ID | input |
| C | Occupational category | input (minimum-wage check) |
| D | Gross monthly remuneration ₡ | input |
| E | Minimum wage for category ₡ | lookup (MTSS) |
| F | Min-wage OK? | `=IF(D>=E,"OK","BREACH")` |
| G | Qualifying children | input |
| H | Spouse credit claimed? | input (0/1) |
| I | Gross income tax ₡ | bracket formula on D (Section 2) |
| J | Family credits ₡ | `=G*1720 + H*2600` |
| K | Income tax withheld ₡ | `=MAX(I-J,0)` |
| L | Employee CCSS ₡ | `=D*0.1067` (2025) / `=D*0.1083` (2026) |
| M | Net pay ₡ | `=D-K-L` |
| N | Employer CCSS ₡ | `=D*0.2667` (2025) / `=D*0.2683` (2026) |
| O | Employer INS work-risk ₡ | `=D*<company risk rate>` (≈1%) |
| P | Total employer cost ₡ | `=D+N+O` |

- **Bracket formula for column I** — =IF(D<=922000,0, IF(D<=1352000,(D-922000)*0.10, IF(D<=2373000,43000+(D-1352000)*0.15, IF(D<=4745000,196150+(D-2373000)*0.20, 670550+(D-4745000)*0.25))))

Totals row: column L, M, N, K must each sum independently; reconcile column P to the bank disbursement plus remittances.

## Section 16 -- Costa Rican Bank Statement / Terminology Reading Guide

**Terminology Reading Guide table**

| Spanish term | Meaning |
| --- | --- |
| Salario bruto | Gross salary |
| Salario neto | Net salary (take-home) |
| Planilla | Payroll / contribution filing |
| Cuotas obrero-patronales | Combined employee + employer CCSS contributions |
| Impuesto al salario / impuesto único | Monthly employment income-tax withholding |
| Retención | Withholding |
| Aguinaldo | 13th-month mandatory salary (paid by 20 Dec) |
| Cesantía | Severance pay |
| Preaviso | Notice-period pay |
| Cargas sociales | Social charges (CCSS + ancillary) |
| SEM | Health & maternity fund |
| IVM | Disability, old-age & death pension fund |
| FODESAF / Asignaciones Familiares | Family-allowances social fund |
| FCL / ROP | Labour-capitalisation fund / complementary pension (Ley 7983) |
| Riesgos del trabajo | Work-risk (workers' comp) INS policy |
| Base Mínima Contributiva (BMC) | Minimum contributory base |
| Salario base | Statutory base amount for penalty calculations (₡462,200, 2025) |
| Pensión alimentaria | Court-ordered child/family support |
| Quincena | Fortnight (bi-monthly pay period) |

## Section 17 -- Onboarding Fallback

If you cannot identify the correct figures for a specific employee or period:

1. Confirm the pay-period date to select 2025 vs 2026 CCSS rates.
2. Confirm single vs multiple employers to decide if monthly withholding is final.
3. If the employer's CCSS registration status is unknown, treat the engagement as blocked until inscripción patronal is confirmed.
4. If the INS risk class is unknown, use ~1% as an illustrative placeholder and flag it as `[RESEARCH GAP — reviewer to confirm]`.
5. If the income-tax base treatment is contested, default to gross and flag for the Costa Rican accountant.
6. Always present output as estimated and route to a Contador Público Autorizado for sign-off.

## Section 18 -- Filing Obligations

### Income Tax Withholding (TRIBU-CR)

**Income Tax Withholding table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| Form 137 (Declaración autoliquidativa) + Form 207 (Informative) | Report and pay impuesto al salario withheld from salaries (replaced legacy D-103 when TRIBU-CR launched 06 Oct 2025) | First **15 calendar days** of the month following payment |
| D-138 (legal entities) | Withholding declaration for juridical persons | First **15 calendar days** of the following month |

### Social Security (CCSS)

**Social Security (CCSS) table**  _(Siempre al Día (TRIBU-CR retenciones); CCSS Patronos)_

| Filing | Purpose | Deadline |
| --- | --- | --- |
| CCSS Planilla (SICERE / Oficina Virtual) | Monthly social-security contribution filing & payment | Reporting window ≈26th of the month to the 4th business day of the next; if not filed, CCSS auto-invoices on the **5th business day** with a **2% surcharge** on SEM and IVM |
| Inscripción Patronal + employee registration | Employer registration with CCSS and registration of each new hire | Within the first **8 business days** of starting activity / hiring |

### Penalties (CNPT Ley 4755; 2025 salario base = ₡462,200)

**Penalties table**  _(CNPT Ley 4755)_

| Penalty | Detail |
| --- | --- |
| Late CCSS planilla | Auto-invoice on 5th business day + **2%** surcharge on SEM & IVM; interest + collection follow |
| Late / omitted registration | **50% of a salario base** per month or fraction (₡231,100/month), capped at 3 salarios base (max ₡1,386,600) |
| Late filing of self-assessed/withholding declaration | Fine of **0.5 salario base** (₡231,100) |
| Late payment of tax (mora) | **1% per month** or fraction from due date, no reduction, capped at **20%** of the unpaid tax, plus statutory interest (CNPT art. 80 bis) |
| Aguinaldo non-payment | Labor sanctions of **1 to 23 salarios base** plus administrative proceedings (Código de Trabajo) |
| Reductions | Tax-infraction fines (excluding interest) reducible **25%–80%** for voluntary correction depending on timing |

## Section 19 -- Reference Material + Test Suite

### Reference Figures (all 2025 unless noted)

**Reference Figures table**

| Item | Value | Source |
| --- | --- | --- |
| Income-tax-free monthly amount | ₡922,000 | Decreto 44772-H |
| Bracket edges (monthly) | 922,000 / 1,352,000 / 2,373,000 / 4,745,000 | Decreto 44772-H |
| Marginal rates | 0 / 10 / 15 / 20 / 25% | Decreto 44772-H |
| Child credit / spouse credit | ₡1,720 / ₡2,600 per month | Decreto 44772-H |
| Employee CCSS total | 10.67% (2025) → 10.83% (2026) | CCSS / BDO |
| Employer CCSS total | 26.67% (2025) → 26.83% (2026) | CCSS / BDO |
| INS work-risk | ~1% risk-rated | INS `[RESEARCH GAP]` |
| BMC IVM / SEM | ₡287,360 / ₡307,013 | EY / CCSS |
| Salario base | ₡462,200 | CNPT / CMFLca |
| Minimum wage (unskilled / semi / skilled) | ₡367,108 / ₡399,203 / ₡413,023 | Decreto 44756-MTSS |

### Test Suite (recompute and assert — figures verified end-to-end)

1. Gross ₡800,000, single, 1 child → income tax ₡0; employee CCSS ₡85,360; net ₡714,640.
2. Gross ₡1,000,000, single, 1 child → gross tax ₡7,800; credit ₡1,720; tax ₡6,080; CCSS ₡106,700; net ₡887,220.
3. Gross ₡1,500,000, single, no dependants → tax ₡65,200; CCSS ₡160,050; net ₡1,274,750.
4. Gross ₡3,000,000, spouse + 2 children → gross tax ₡321,550; credits ₡6,040; tax ₡315,510; CCSS ₡320,100; net ₡2,364,390.
5. Gross ₡5,000,000, single → tax ₡734,300; CCSS ₡533,500; net ₡3,732,200.
6. Cumulative-tax assertion: tax at ₡4,745,000 = ₡670,550 (= 43,000 + 153,150 + 474,400).
7. Employer-cost assertion: gross ₡1,000,000 → employer CCSS 26.67% = ₡266,700; +1% INS ≈ ₡10,000.
8. Aguinaldo assertion: ₡1,000,000/month × 12 ÷ 12 = ₡1,000,000; exempt; paid by 20 Dec.
9. 2026 rate switch assertion: employee CCSS 10.83%, employer CCSS 26.83% for periods on/after 01 Jan 2026 (only IVM line changes).
10. Late-payment cap assertion: mora is 1%/month capped at 20% of unpaid tax.

## Section 20 -- Interaction with Other Skills

**Interaction with Other Skills table**

| Scenario | Skill to use |
| --- | --- |
| Employee payroll (impuesto al salario + CCSS) | **This skill (costa-rica-payroll.md)** |
| Corporate income tax | costa-rica-corporate-tax.md (if available) |
| VAT (IVA) returns | costa-rica-vat-return.md (if available) |
| Bookkeeping | costa-rica-bookkeeping.md (if available) |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages, employer CCSS, and INS work-risk are expenses; employee CCSS and impuesto al salario withheld are liabilities until remitted to CCSS/Hacienda.
- **Payroll → Income Tax:** Single-employer monthly withholding is final; multi-source employees need annual reconciliation.

## PROHIBITIONS

- **Prohibitions list** — - NEVER run payroll for an employer that is not registered with CCSS (inscripción patronal). - NEVER fold the INS riesgos del trabajo cost into the 26.67% CCSS total — it is a separate employer policy. - NEVER pre-deduct employee CCSS from the income-tax base without flagging (conservative default = GROSS base). - NEVER withhold income tax or CCSS on aguinaldo — it is exempt (only court-ordered pensión alimentaria may be deducted). - NEVER use 2026 CCSS rates (26.83% / 10.83%) for pay periods before 01 Jan 2026, or 2025 rates after. - NEVER assume a single national minimum wage — use the MTSS occupation-specific figure. - NEVER let family credits create a negative income-tax (refund) — floor the withholding at ₡0. - NEVER miss the TRIBU-CR 15-calendar-day or CCSS planilla deadlines — surcharges and penalties apply. - NEVER present the per-fund employer breakdown as exact — the confirmed total is 26.67%; the line split is a `[RESEARCH GAP]`. - NEVER present payroll computations as definitive — always label as estimated and direct to a Costa Rican Contador Público Autorizado.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Público Autorizado in Costa Rica) before implementation.

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
