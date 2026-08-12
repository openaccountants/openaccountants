---
name: panama-payroll
description: Use this skill whenever asked about Panama payroll processing for employed persons (planilla). Trigger on phrases like "Panama payroll", "planilla CSS", "Caja de Seguro Social", "cuota obrero-patronal", "seguro educativo", "riesgos profesionales", "ISR Panama", "retención de salario Panama", "impuesto sobre la renta salario", "décimo tercer mes", "décimo Panama", "13th month Panama", "SIPE", "salario mínimo Panama", "Form 03 Panama", "planilla 03", "net salary Panama", "gross to net balboa", "MITRADEL", "DGI retención", or any question about computing employee pay, salary withholding tax, or social-security contributions for Panama-based employees. This skill covers ISR (monthly income-tax withholding on salaries), CSS social-security contributions (employee and employer), educational insurance, professional-risk insurance, the mandatory décimo tercer mes, minimum wage, and filing obligations via SIPE/DGI. ALWAYS read this skill before processing any Panama payroll.
version: 0.1
jurisdiction: PA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Panama Payroll Skill v0.1 (Tier 2 — research-verified, pending accountant sign-off)

## Panama Payroll Skill v0.1 (Tier 2 — research-verified, pending accountant sign-off)

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Republic of Panama (national, code PA) |
| Currency | PAB -- Panamanian Balboa (B/.); pegged 1:1 with USD and USD circulates as legal tender |
| Standard pay frequency | Monthly or quincenal (bi-monthly, 15th + month-end); weekly permitted |
| Tax system | **Territorial** -- only Panamanian-source income is taxed (PwC, *Taxes on personal income*) |
| Tax year | Calendar / fiscal year (1 January -- 31 December) |
| Income-tax withholding system | ISR (Impuesto Sobre la Renta) -- monthly employer withholding on salaries, projected over 13 months (12 + décimo) |
| Income-tax authority | Dirección General de Ingresos (DGI), Ministerio de Economía y Finanzas (MEF) |
| Social-security authority | Caja de Seguro Social (CSS) |
| Labour / minimum-wage authority | Ministerio de Trabajo y Desarrollo Laboral (MITRADEL) |
| Key legislation | Código Fiscal (ISR brackets, confirmed on DGI *Tarifa* page); **Ley No. 462 de 18 marzo 2025** (CSS reform, employer-rate phase-in); Cabinet Decree No. 221 of 18 Nov 1971 (décimo); Executive Decree No. 13 of 31 Dec 2025 (2026 minimum wage) |
| Filing portals | SIPE (Sistema de Ingresos y Prestaciones Económicas -- CSS planilla, consolidates CSS + ISR); DGI e-Tax |
| Validated by | Pending -- requires sign-off by a Panamanian Contador Público Autorizado (CPA) |
| Skill version | 0.1 |

> **Tier-2 note.** Figures below are research-verified. The load-bearing fully-verified figures are: the three ISR brackets (0 / 15 / 25% at B/.11,000 / B/.50,000), confirmed on the DGI *Tarifa* page and PwC; and the post-Law-462 CSS rates (employee 9.75%, employer 13.25% rising to 14.25% / 15.25%, educational 1.25% / 1.50%, **no wage ceiling**), confirmed by PwC and Fabrega Molino. Several specifics could NOT be obtained from a primary CSS/DGI page and are flagged inline as `[RESEARCH GAP — reviewer to confirm]`: the riesgos-profesionales rate-by-class table, the internal health/pension split of the 9.75%, the 7.25% décimo SS rate, exact late-payment penalty formulas, and the full 59-rate minimum-wage annex.

## Section 2 -- Income Tax Withholding (ISR on salaries)

- **ISR withholding computation method** — The employer withholds ISR monthly from wages, salaries, and other remuneration for personal services. Panama taxes only Panamanian-source income (territorial system). Multiply the monthly salary by 13 (12 months + décimo/XIII month) to estimate annual income, apply the bracket table to the annual figure, then deduct proportionally each month (one-twelfth of the annual liability).  _(PwC *Panama — Individual — Tax administration*; method consistency across secondary payroll guides)_

### ISR Brackets (annual net taxable income, B/. = USD)

**ISR Brackets table**  _(DGI *Tarifa* page (https://dgi.mef.gob.pa/DInforme/Tarifa) and PwC *Taxes on personal income* (tax year 2026, last reviewed 18 Jan 2026))_

| Annual net taxable income (B/.) | Marginal rate | Tax on the band (B/.) | Cumulative tax at top of band (B/.) |
| --- | --- | --- | --- |
| 0 to 11,000 | 0% (exento) | 0 | 0 |
| over 11,000 to 50,000 | 15% | 5,850 | 5,850 |
| over 50,000 | 25% | (open) | (open) |

- **Cumulative-tax check** — 15% × (50,000 − 11,000) = 15% × 39,000 = 5,850 at B/.50,000. Tax above that point = 5,850 + 25% × (annual income − 50,000). ✔  _(DGI *Tarifa* / PwC (computed))_
- **No local/municipal income taxes on salaries** — No local / municipal income taxes on salaries.  _(PwC)_
- **Tax-free allowance** — B/.11,000 B/. per year (annual)  _(DGI *Tarifa* / PwC)_

### Computation Method (employer withholding)

- **Employer ISR withholding steps** — 1. Take the employee's monthly gross remuneration and project annual income = monthly × 13 (12 + décimo). 2. Apply the annual ISR bracket schedule to the projected annual figure. 3. Divide the resulting annual ISR by 12 to obtain the monthly amount to withhold. 4. Withheld ISR is remitted to DGI monthly, by the 15th of the following month.  _(PwC / secondary payroll guides)_

Note: the décimo is included in the annualisation factor (×13) for projecting the ISR base, but the décimo payment itself has special SS treatment (Section 8) and its own ISR treatment where the worker's income level is taxable.

### Section 2.1 -- Individual filing (context)

- **Individual filing rules** — Tax year = calendar year. An employee with a single salary source already withheld by the employer is generally exempt from filing. Others file by 15 March of the following year; estimated tax (for filers) is due in 3 installments — 30 June, 30 September, 31 December.  _(PwC *Tax administration*)_
- **Form 03 and planilla 03** — The employer provides each employee an annual Form 03 (Comprobante de Ingresos) and files an annual employer information return (planilla 03) of salaries/withholdings, due 31 March of the following year.  _(PwC *Tax administration*)_

### Section 2.2 -- Key personal deductions (relevant only if the employee files)

**Key personal deductions table**  _(PwC *Panama — Individual — Deductions*)_

| Deduction | Limit (B/.) |
| --- | --- |
| Married-couple personal exemption | 800 |
| Mortgage interest (Panama home) | up to 15,000/yr |
| Retirement contributions | up to 15,000 |
| Education expenses (since Jan 2019) | up to 3,600 per student |
| Charitable donations | up to 50,000/yr |
| Medical expenses (incurred in Panama, documented) | deductible |

These reduce the taxable base on an employee's own return; they are not normally applied in routine employer monthly withholding.

## Section 3 -- Social Security -- Employee Deductions (CSS, from 1 Apr 2025)

**Employee CSS deductions table**  _(PwC *Other taxes*; Fabrega Molino *Panama Social Security Reform 2025*)_

| Contribution | Employee rate | Ceiling |
| --- | --- | --- |
| Social security (Seguro Social, CSS) | 9.75% | **none** |
| Educational insurance (Seguro Educativo) | 1.25% | **none** |
| **TOTAL employee deduction** | **11.00%** | **none** |

- **Sum check** — 9.75 + 1.25 = 11.00%. ✔  _(PwC *Other taxes*)_
- **No wage ceiling** — No wage ceiling / cap on CSS or educational insurance — no maximum limit on the taxable amount.  _(PwC)_

The internal split of the 9.75% between health (Enfermedad y Maternidad) and pension (IVM) was not obtainable from a primary CSS page. `[RESEARCH GAP — reviewer to confirm the health/pension split of the 9.75% employee rate]`

## Section 4 -- Social Security -- Employer Contributions (CSS, from 1 Apr 2025)

**Employer CSS contributions table**  _(PwC *Other taxes*; Fabrega Molino on Law 462)_

| Contribution | Employer rate | Ceiling |
| --- | --- | --- |
| Social security (Seguro Social, CSS) | 13.25% (from 1 Apr 2025) | **none** |
| Educational insurance (Seguro Educativo) | 1.50% | **none** |
| **Subtotal (CSS + educational)** | **14.75%** | **none** |
| Professional risk (Riesgos Profesionales) | 0.33% – 6.25% (by industry risk class) | n/a |

- **Sum check employer subtotal** — 13.25 + 1.50 = 14.75%. ✔ The riesgos-profesionales rate is additional to the 14.75% and varies by occupational risk class.  _(PwC / Fabrega Molino)_

`[RESEARCH GAP — reviewer to confirm: the riesgos-profesionales 0.33%–6.25% band is from a single secondary guide (allaboutpanamacity); the exact rate-by-industry-class table could not be confirmed on an official CSS page. Obtain the company-specific rate from CSS before relying on it.]`

### Section 4.1 -- Employer CSS rate phase-in (Law 462)

**Employer CSS rate phase-in table**  _(Fabrega Molino; MEF reform summary)_

| Period | Employer CSS rate | Employer subtotal (CSS + 1.50% educational) |
| --- | --- | --- |
| 1 Apr 2025 – 28 Feb 2027 | 13.25% | 14.75% |
| from 1 Mar 2027 | 14.25% | 15.75% |
| from 1 Mar 2029 | 15.25% | 16.75% |

- **Retirement ages unchanged** — Retirement ages (unchanged under Law 462): men 62, women 57.  _(Fabrega Molino)_

## Section 5 -- Total Social-Charge Cost Summary

**Total Social-Charge Cost Summary table**

| Party | Current (from 1 Apr 2025) | from 1 Mar 2027 | from 1 Mar 2029 |
| --- | --- | --- | --- |
| Employee CSS (9.75%) + educational (1.25%) | 11.00% | 11.00% | 11.00% |
| Employer CSS | 13.25% | 14.25% | 15.25% |
| Employer educational | 1.50% | 1.50% | 1.50% |
| Employer subtotal (CSS + educational) | 14.75% | 15.75% | 16.75% |
| Employer riesgos profesionales (separate, by class) | 0.33%–6.25% | 0.33%–6.25% | 0.33%–6.25% |

- **Phase-in application rule** — Only the employer CSS line changes across the phase-in. Use the current 13.25% (subtotal 14.75%) for pay periods up to 28 Feb 2027; switch to 14.25% (subtotal 15.75%) from 1 Mar 2027.  _(Law 462 / Fabrega Molino)_

## Section 6 -- Thresholds and Contribution Bases

**Thresholds and Contribution Bases table**

| Item | Value | Source |
| --- | --- | --- |
| Income-tax-free annual amount | B/.11,000/year | DGI *Tarifa* / PwC |
| ISR bracket edges (annual) | 11,000 / 50,000 | DGI *Tarifa* / PwC |
| ISR marginal rates | 0 / 15 / 25% | DGI *Tarifa* / PwC |
| Cumulative ISR at B/.50,000 | B/.5,850 | DGI *Tarifa* / PwC (computed) |
| ISR annualisation factor | × 13 (12 months + décimo) | PwC / secondary payroll guides |
| Employee CSS + educational | 11.00% (9.75% + 1.25%), no ceiling | PwC / Fabrega Molino |
| Employer CSS + educational | 14.75% (13.25% + 1.50%), no ceiling | PwC / Fabrega Molino |
| Employer riesgos profesionales | 0.33%–6.25% by class `[RESEARCH GAP]` | allaboutpanamacity (secondary) |
| Décimo SS rate (reduced) | 7.25% `[RESEARCH GAP]` | allaboutpanamacity / PKF (secondary) |
| Retirement age | men 62 / women 57 | Fabrega Molino |

## Section 7 -- Minimum Wage (2026)

The minimum wage is set by Executive Decree No. 13 of 31 Dec 2025, published 6 Jan 2026 (Gaceta Oficial No. 30438), effective 16 January 2026 (replacing Decree No. 01 of 10 Jan 2024). Rates are set per hour, differentiated by economic activity, occupation, company size, and region — 59 rates across 74 activities. Source: EY *Panamá — salario mínimo 2026*; MITRADEL press release.

**Two regions:**
- **Region 1** — Panama City, San Miguelito, Colón, David, Santiago, Chitré, Penonomé, Aguadulce, La Chorrera, Arraiján, Boquete, Bugaba, Changuinola + listed districts in Herrera, Los Santos, Tierras Altas.
- **Region 2** — all remaining districts.

Representative hourly rates (examples, NOT exhaustive — use the MITRADEL annex for the exact activity/size/region cell):

**Representative minimum wage rates table**  _(EY *Panamá — salario mínimo 2026*; MITRADEL press release)_

| Activity (example) | Region 1 (B/./hr) | Region 2 (B/./hr) |
| --- | --- | --- |
| Manufacturing — small companies | 2.32 | 1.95 |
| Manufacturing — large companies | 3.13 | 2.58 |
| Construction | 3.51 | 3.30 |
| Electricity / gas / water | 3.50 (nationwide) | 3.50 (nationwide) |
| Retail — large companies | 3.02 | 2.48 |
| Domestic workers | 350.00 / month (Region 1) | — |

`[RESEARCH GAP — the full 59-rate per-activity table is an annex PDF to Decree 13 and was not retrieved. Pull the exact cell from the MITRADEL annex when granular rates are needed; the figures above are representative examples only.]`

## Section 8 -- Statutory Pay Items

### Section 8.1 -- Décimo Tercer Mes (13th-Month Bonus) -- Mandatory

**Décimo Tercer Mes rules table**  _(Cabinet Decree No. 221 of 18 Nov 1971, regulated by Decree No. 19 of 7 Sept 1973; allaboutpanamacity; PKF Panamá / Laboremia (secondary))_

| Rule | Detail |
| --- | --- |
| Amount | 1 day's salary per 11 days worked in the preceding 4-month period (≈ one month's salary per year total) |
| Payment schedule | 3 installments: **15 April, 15 August, 15 December** |
| Social-security treatment | SS deducted at a **reduced 7.25%** (vs the regular 9.75%) `[RESEARCH GAP — the 7.25% décimo SS rate is widely cited in secondary sources but could not be pulled from a primary CSS page — reviewer to confirm]` |
| ISR treatment | ISR withholding applies to the décimo where the worker's annual income level is taxable |
| Garnishment | Cannot be garnished |

## Section 9 -- Conservative Defaults

- **ISR base default** — ISR base is GROSS Panamanian-source salary, projected ×13. Project annual income = monthly × 13, apply brackets, divide by 12. Do not pre-deduct CSS from the ISR base unless the reviewer confirms a net-of-CSS treatment.  _(PwC)_
- **Employee deduction default** — Employee deduction = 11.00% (CSS 9.75% + educational 1.25%), no ceiling, on every pay period.  _(PwC / Fabrega Molino)_
- **Employer subtotal default** — Employer subtotal = 14.75% (CSS 13.25% + educational 1.50%) for periods up to 28 Feb 2027; switch to 15.75% from 1 Mar 2027, 16.75% from 1 Mar 2029.  _(Law 462)_
- **Riesgos profesionales default** — Riesgos profesionales is a SEPARATE employer cost (0.33%–6.25% by class) on top of the 14.75% subtotal — never fold it in. Default to the lowest band only as an illustrative placeholder and flag. `[RESEARCH GAP]`
- **Minimum wage default** — Minimum wage is per activity/size/region. Never assume a single national floor — use the MITRADEL Decree 13 annex cell matching the role. `[RESEARCH GAP]`
- **Décimo SS rate default** — Décimo SS at 7.25%, not 9.75%, and ISR on the décimo only where the worker is taxable. `[RESEARCH GAP]`  _(secondary)_
- **USD parity default** — USD = balboa 1:1 — present figures in B/.; USD amounts are numerically identical.

## Section 10 -- Required Inputs + Refusal Catalogue

### Required Inputs

**Required Inputs table**

| Input | Why needed |
| --- | --- |
| Employee gross monthly remuneration (B/.) | Base for both ISR (×13 projection) and CSS |
| Pay-period date | Determines employer CSS rate (13.25% vs 14.25% from 1 Mar 2027) |
| Single vs multiple income sources | Determines whether monthly withholding is final (filing exemption) |
| Whether the remuneration is Panamanian-source | Territorial system — foreign-source salary is not taxed |
| Occupational activity, company size, region | Minimum-wage compliance check |
| Company occupational risk class | Riesgos-profesionales rate (0.33%–6.25%) |
| Employer CSS registration status + new-hire registration | Compliance / SIPE filing obligation |

### Refusal Catalogue — DO NOT proceed (refuse and request the missing item) if:

- **Missing/below minimum-wage remuneration** — Gross monthly remuneration is not provided or is below the applicable minimum-wage cell (flag a minimum-wage breach).
- **Unclear Panamanian-source status** — It is unclear whether the salary is Panamanian-source (territorial system — refuse to tax foreign-source income without confirmation).
- **Employer not registered with CSS** — The employer is not registered with CSS — payroll cannot be lawfully run via SIPE.
- **Gross-up without confirming ISR base** — A net-pay target is given and you are asked to "gross up" without confirming the ISR base (gross vs net of CSS) — flag the RESEARCH GAP.
- **Wrong décimo SS rate requested** — A décimo is requested with the regular 9.75% SS rate instead of the reduced 7.25% — flag for confirmation.
- **Phase-in boundary ambiguity** — The pay period falls on/after a phase-in boundary (1 Mar 2027 / 1 Mar 2029) without clarification of which employer CSS rate applies.

## Section 11 -- Transaction / Payment Pattern Library

Deterministic classification of common Panamanian bank-statement lines (Spanish terms first, then English/EOR variants).

### Salary Credits (employee receiving)

**Salary Credits table**

| Pattern | Classification |
| --- | --- |
| SALARIO, PLANILLA, PAGO QUINCENA, DEPOSITO SALARIO, ABONO SALARIO | Net salary payment |
| DECIMO, DECIMO TERCER MES, XIII MES | Décimo installment (Apr / Aug / Dec; 7.25% SS) |
| LIQUIDACION, PRIMA DE ANTIGUEDAD, INDEMNIZACION | Severance / termination payment |
| VACACIONES | Paid leave |

### Employer Debits (employer paying)

**Employer Debits table**

| Pattern | Classification |
| --- | --- |
| CSS PLANILLA, CAJA DE SEGURO SOCIAL, SIPE | CSS contributions (employee + employer) remittance |
| SEGURO EDUCATIVO | Educational-insurance component within SIPE |
| RIESGOS PROFESIONALES, RIESGO PROFESIONAL | Professional-risk insurance premium (employer) |
| DGI, MEF, RETENCION ISR, IMPUESTO SOBRE LA RENTA | ISR withholding remittance to DGI |
| PLANILLA SALARIOS, PAGO EMPLEADOS, TRANSFERENCIA NOMINA | Net wages disbursement to employees |
| DECIMO TERCER MES, XIII MES | Décimo payment to employees (Apr / Aug / Dec) |

## Section 12 -- Worked Examples

All examples use current rates: ISR brackets 0 / 15 / 25% (edges 11,000 / 50,000); ISR base = monthly × 13 projected annual, ÷ 12 monthly; employee CSS+educational 11.00%; employer subtotal 14.75% (CSS 13.25% + educational 1.50%). Riesgos profesionales shown illustratively at the low end and flagged. Figures recomputed end-to-end (B/. = USD).

### Example A -- Below ISR threshold

- Gross monthly: B/.800. Single Panamanian-source salary.
- Projected annual = 800 × 13 = 10,400 ≤ 11,000 → annual ISR **B/.0** → monthly ISR **B/.0**.
- Employee CSS + educational: 800 × 11.00% = **B/.88.00**.
- **Net pay = 800 − 0 − 88.00 = B/.712.00.**
- Employer cost: 800 × 14.75% = B/.118.00 (+ riesgos profesionales by class, e.g. ~B/.2.64 at 0.33%).
- Bank line: `DEPOSITO SALARIO XYZ SA B/.712.00`.

### Example B -- Mid-band, single source

- Gross monthly: B/.1,500.
- Projected annual = 1,500 × 13 = 19,500. Annual ISR = 15% × (19,500 − 11,000) = 15% × 8,500 = 1,275 → monthly ISR = 1,275 ÷ 12 = **B/.106.25**.
- Employee CSS + educational: 1,500 × 11.00% = **B/.165.00**.
- **Net pay = 1,500 − 106.25 − 165.00 = B/.1,228.75.**
- Employer cost: 1,500 × 14.75% = B/.221.25 (+ riesgos profesionales).

### Example C -- Top of 15% projection band

- Gross monthly: B/.3,000.
- Projected annual = 3,000 × 13 = 39,000. Annual ISR = 15% × (39,000 − 11,000) = 15% × 28,000 = 4,200 → monthly ISR = 4,200 ÷ 12 = **B/.350.00**.
- Employee CSS + educational: 3,000 × 11.00% = **B/.330.00**.
- **Net pay = 3,000 − 350.00 − 330.00 = B/.2,320.00.**
- Employer cost: 3,000 × 14.75% = B/.442.50 (+ riesgos profesionales).

### Example D -- Into the 25% band

- Gross monthly: B/.5,000.
- Projected annual = 5,000 × 13 = 65,000. Annual ISR = 5,850 + 25% × (65,000 − 50,000) = 5,850 + 25% × 15,000 = 5,850 + 3,750 = 9,600 → monthly ISR = 9,600 ÷ 12 = **B/.800.00**.
- Employee CSS + educational: 5,000 × 11.00% = **B/.550.00**.
- **Net pay = 5,000 − 800.00 − 550.00 = B/.3,650.00.**
- Employer cost: 5,000 × 14.75% = B/.737.50 (+ riesgos profesionales).

### Example E -- High earner, top band

- Gross monthly: B/.10,000.
- Projected annual = 10,000 × 13 = 130,000. Annual ISR = 5,850 + 25% × (130,000 − 50,000) = 5,850 + 25% × 80,000 = 5,850 + 20,000 = 25,850 → monthly ISR = 25,850 ÷ 12 = **B/.2,154.17** (rounded).
- Employee CSS + educational: 10,000 × 11.00% = **B/.1,100.00**.
- **Net pay = 10,000 − 2,154.17 − 1,100.00 = B/.6,745.83.**
- Employer cost: 10,000 × 14.75% = B/.1,475.00 (+ riesgos profesionales).

### Example F -- Décimo Tercer Mes installment

- Employee earns B/.3,000/month, full year. Annual décimo ≈ one month's salary = **B/.3,000**, paid in three installments (15 Apr / 15 Aug / 15 Dec).
- SS deducted at the reduced **7.25%**: 3,000 × 7.25% = B/.217.50. `[RESEARCH GAP — 7.25% rate from secondary sources]`
- Net décimo before ISR = 3,000 − 217.50 = **B/.2,782.50** (ISR additionally applies where the worker's income level is taxable).
- Bank line: `DECIMO TERCER MES B/.2,782.50` (split across three installments in practice).

## Section 13 -- Tier 1 Rules (deterministic — apply automatically)

- **Rule 1 ISR projection** — Project ISR base = monthly gross (Panamanian-source) × 13; apply annual brackets 0% / 15% / 25% with edges B/.11,000 / B/.50,000; divide annual ISR by 12 for the monthly amount.  _(DGI *Tarifa* / PwC)_
- **Rule 2 cumulative ISR formula** — Cumulative ISR at B/.50,000 = B/.5,850; above B/.50,000, ISR = 5,850 + 25% × (annual − 50,000).
- **Rule 3 final withholding** — ISR withheld monthly is the employee's final tax if there is a single salary source — no annual return required.
- **Rule 4 employee CSS** — Withhold employee CSS + educational = 11.00% of gross (9.75% + 1.25%); no ceiling.  _(PwC / Fabrega Molino)_
- **Rule 5 employer CSS** — Compute employer CSS + educational = 14.75% of gross (13.25% + 1.50%) for periods up to 28 Feb 2027; 15.75% from 1 Mar 2027; 16.75% from 1 Mar 2029.  _(Law 462)_
- **Rule 6 riesgos profesionales separate** — Add the separate riesgos-profesionales employer cost (0.33%–6.25% by class) — never fold it into the CSS subtotal. `[RESEARCH GAP]`
- **Rule 7 décimo** — Décimo = ≈ one month's salary, paid in 3 installments (15 Apr / 15 Aug / 15 Dec); SS at the reduced 7.25%; ISR where taxable; cannot be garnished. `[RESEARCH GAP on 7.25%]`
- **Rule 8 ISR remittance deadline** — Remit ISR to DGI monthly by the 15th of the following month. `[RESEARCH GAP on date]`
- **Rule 9 SIPE filing and registration** — File the CSS planilla via SIPE before the 21st of the month; pay within the following month; register each new hire with CSS within ~5 working days of hire. `[RESEARCH GAP — SIPE timing from secondary sources]`
- **Rule 10 Form 03 and planilla 03** — Issue each employee Form 03 (Comprobante de Ingresos) and file the annual employer return (planilla 03) by 31 March of the following year.  _(PwC)_

## Section 14 -- Tier 2 Catalogue (reviewer judgement required)

These items require a Panamanian accountant's judgement and are flagged rather than auto-computed:

1. **ISR base (gross vs net of CSS).** Conservative default is gross-Panamanian-source projected ×13; confirm no pre-deduction of CSS applies. `[RESEARCH GAP — reviewer to confirm]`
2. **Riesgos-profesionales rate.** 0.33%–6.25% by occupational class; the exact rate table by industry is from a single secondary source and must be confirmed with CSS. `[RESEARCH GAP]`
3. **Health/pension split of the 9.75% employee rate.** Not obtainable from a primary CSS page. `[RESEARCH GAP]`
4. **Décimo SS rate (7.25%).** Widely cited but not pulled from a primary CSS page. `[RESEARCH GAP]`
5. **Late-payment penalty / surcharge formulas (CSS and DGI).** Exact percentages not found on an authoritative page. `[RESEARCH GAP]`
6. **Minimum-wage cell.** The precise per-activity/size/region rate from the Decree 13 annex (59 rates). `[RESEARCH GAP]`
7. **Territoriality edge cases.** Whether a specific component of remuneration is Panamanian-source (e.g. work partly performed abroad).
8. **Personal-return deductions.** Mortgage / education / retirement / donation deductions affect the employee's own return, not routine employer withholding.

## Section 15 -- Excel Working Paper Template

**Excel Working Paper Template columns**

| Col | Header | Formula / Source |
| --- | --- | --- |
| A | Employee name | input |
| B | Cédula / ID | input |
| C | Activity / size / region | input (minimum-wage check) |
| D | Gross monthly remuneration B/. | input |
| E | Minimum wage for cell B/. | lookup (MITRADEL Decree 13 annex) |
| F | Min-wage OK? | `=IF(D>=E,"OK","BREACH")` |
| G | Projected annual B/. | `=D*13` |
| H | Annual ISR B/. | bracket formula on G (Section 2) |
| I | Monthly ISR B/. | `=H/12` |
| J | Employee CSS + educational B/. | `=D*0.11` |
| K | Net pay B/. | `=D-I-J` |
| L | Employer CSS + educational B/. | `=D*0.1475` (to 28 Feb 2027) / `=D*0.1575` (from 1 Mar 2027) |
| M | Employer riesgos profesionales B/. | `=D*<company risk rate>` (0.33%–6.25%) |
| N | Total employer cost B/. | `=D+L+M` |

- **Annual-ISR bracket nested formula (column H)** — =IF(G<=11000,0, IF(G<=50000,(G-11000)*0.15, 5850+(G-50000)*0.25))

Totals row: columns I, J, K, L must each sum independently; reconcile column N to the bank disbursement plus remittances. Add a separate décimo working paper using the reduced 7.25% SS rate for Apr / Aug / Dec installments.

## Section 16 -- Panamanian Bank Statement / Terminology Reading Guide

**Terminology reading guide table**

| Spanish term | Meaning |
| --- | --- |
| Salario bruto | Gross salary |
| Salario neto | Net salary (take-home) |
| Planilla | Payroll / contribution filing |
| Cuota obrero-patronal | Combined employee + employer CSS contribution |
| Seguro Social / CSS | Social-security fund (Caja de Seguro Social) |
| Seguro Educativo | Educational-insurance contribution |
| Riesgos Profesionales | Professional-risk (workers' comp) insurance |
| Retención | Withholding |
| ISR / Impuesto Sobre la Renta | Income tax |
| Décimo Tercer Mes / XIII Mes | 13th-month mandatory bonus (Apr / Aug / Dec) |
| Prima de antigüedad | Seniority premium (termination) |
| Indemnización | Severance / dismissal compensation |
| Quincena | Fortnight (bi-monthly pay period) |
| SIPE | CSS online declaration/payment system (consolidates CSS + ISR) |
| DGI | Dirección General de Ingresos (tax authority) |
| MITRADEL | Labour ministry (minimum wage / labour law) |
| Comprobante de Ingresos (Form 03) | Annual income certificate to the employee |
| Balboa (B/.) | National currency unit, 1:1 with USD |

## Section 17 -- Onboarding Fallback

If you cannot identify the correct figures for a specific employee or period:

1. Confirm the pay-period date to select the employer CSS rate (13.25% to 28 Feb 2027; 14.25% from 1 Mar 2027).
2. Confirm the salary is Panamanian-source (territorial system) before applying ISR.
3. Confirm single vs multiple income sources to decide if monthly withholding is final.
4. If the employer's CSS registration status is unknown, treat the engagement as blocked until registration is confirmed.
5. If the riesgos-profesionales risk class is unknown, use the 0.33% low band only as an illustrative placeholder and flag it as `[RESEARCH GAP — reviewer to confirm]`.
6. If the ISR base treatment is contested, default to gross-Panamanian-source projected ×13 and flag for the Panamanian accountant.
7. Always present output as estimated and route to a Contador Público Autorizado for sign-off.

## Section 18 -- Filing Obligations

### Income Tax Withholding (DGI)

**Income Tax Withholding filings table**

| Item | Purpose | Deadline |
| --- | --- | --- |
| Monthly ISR remittance | Pay ISR withheld from salaries to DGI | By the **15th** of the following month `[RESEARCH GAP — secondary source]` |
| Form 03 (Comprobante de Ingresos) | Annual income certificate to each employee | Annually |
| Planilla 03 (employer information return) | Annual return of salaries / withholdings | **31 March** of the following year (PwC) |

### Social Security (CSS / SIPE)

**Social Security filings table**  _(PwC *Tax administration* (planilla 03, Form 03); SIPE timing and registration windows from secondary payroll providers (neeyamo, papayaglobal))_

| Filing | Purpose | Deadline |
| --- | --- | --- |
| Monthly CSS planilla (SIPE) | Declare and pay CSS + educational (employee + employer) + ISR | Present **before the 21st** of the month; pay within the following month `[RESEARCH GAP — secondary]` |
| New-hire registration | Register each new employee with CSS (and DGI) | Within ~**5 working days** of hire `[RESEARCH GAP — secondary]` |

### Penalties

**Penalties table**

| Penalty | Detail |
| --- | --- |
| Late CSS payment | Surcharges + interest assessed by CSS `[RESEARCH GAP — exact formula not on a primary page]` |
| Unregistered workers / under-declaration | Retroactive employer + employee contributions, surcharges, MITRADEL fines, and in severe cases suspension of operations `[RESEARCH GAP — exact figures not confirmed]` |
| Late ISR remittance | Surcharges / interest by DGI `[RESEARCH GAP — exact formula not confirmed]` |

> Note: a "12.25%" retroactive employer figure appears in one secondary source but conflicts with the current 13.25% rate — treat as outdated and do NOT use it.

### Reference Figures (current unless noted)

**Reference Figures table**

| Item | Value | Source |
| --- | --- | --- |
| Income-tax-free annual amount | B/.11,000 | DGI *Tarifa* / PwC |
| ISR bracket edges (annual) | 11,000 / 50,000 | DGI *Tarifa* / PwC |
| ISR marginal rates | 0 / 15 / 25% | DGI *Tarifa* / PwC |
| Cumulative ISR at B/.50,000 | B/.5,850 | DGI *Tarifa* / PwC (computed) |
| ISR annualisation factor | × 13 | PwC / secondary |
| Employee CSS + educational | 11.00% (9.75% + 1.25%), no ceiling | PwC / Fabrega Molino |
| Employer CSS + educational | 14.75% (13.25% + 1.50%) → 15.75% (2027) → 16.75% (2029) | PwC / Fabrega Molino / Law 462 |
| Riesgos profesionales | 0.33%–6.25% by class | allaboutpanamacity `[RESEARCH GAP]` |
| Décimo SS rate | 7.25% (reduced) | secondary `[RESEARCH GAP]` |
| Retirement age | men 62 / women 57 | Fabrega Molino |
| Minimum wage | per activity/size/region (Decree 13, eff. 16 Jan 2026) | EY / MITRADEL `[RESEARCH GAP on full annex]` |

### Test Suite (recompute and assert — figures verified end-to-end)

1. **Gross B/.800 →** projected annual 10,400 ≤ 11,000; ISR B/.0; employee CSS B/.88.00; **net B/.712.00**.
2. **Gross B/.1,500 →** projected annual 19,500; annual ISR B/.1,275; monthly ISR B/.106.25; CSS B/.165.00; **net B/.1,228.75**.
3. **Gross B/.3,000 →** projected annual 39,000; annual ISR B/.4,200; monthly ISR B/.350.00; CSS B/.330.00; **net B/.2,320.00**.
4. **Gross B/.5,000 →** projected annual 65,000; annual ISR B/.9,600; monthly ISR B/.800.00; CSS B/.550.00; **net B/.3,650.00**.
5. **Gross B/.10,000 →** projected annual 130,000; annual ISR B/.25,850; monthly ISR B/.2,154.17; CSS B/.1,100.00; **net B/.6,745.83**.
6. **Cumulative-ISR assertion:** annual ISR at B/.50,000 = 15% × (50,000 − 11,000) = **B/.5,850**.
7. **Employee-deduction assertion:** 9.75% + 1.25% = **11.00%**, no ceiling.
8. **Employer-subtotal assertion:** 13.25% + 1.50% = **14.75%** (to 28 Feb 2027); 14.25% + 1.50% = 15.75% (from 1 Mar 2027).
9. **Employer-cost assertion:** gross B/.3,000 → employer CSS+educational 14.75% = **B/.442.50** (+ riesgos profesionales by class).
10. **Décimo assertion:** B/.3,000 décimo → SS 7.25% = B/.217.50; net before ISR = **B/.2,782.50**; paid 15 Apr / 15 Aug / 15 Dec. `[RESEARCH GAP on 7.25%]`

## Section 20 -- Interaction with Other Skills

**Interaction with Other Skills table**

| Scenario | Skill to use |
| --- | --- |
| Employee payroll (ISR + CSS) | **This skill (panama-payroll.md)** |
| ITBMS (VAT) returns | panama-itbms.md |
| Corporate income tax | panama-corporate-tax.md (if available) |
| Bookkeeping | panama-bookkeeping.md (if available) |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages, employer CSS + educational, and riesgos profesionales are expenses; employee CSS + educational and ISR withheld are liabilities until remitted to CSS/DGI.
- **Payroll → Income Tax:** Single-source monthly ISR withholding is final; multi-source employees must file by 15 March of the following year.

## PROHIBITIONS

- **Prohibitions list** — - NEVER run payroll for an employer that is not registered with CSS — SIPE filing requires registration. - NEVER tax foreign-source salary — Panama is territorial; only Panamanian-source income is taxed. - NEVER fold the riesgos-profesionales cost into the 14.75% CSS subtotal — it is a separate employer policy (0.33%–6.25% by class). - NEVER apply a wage ceiling to CSS or educational insurance — there is no maximum contributory base. - NEVER withhold the regular 9.75% SS on the décimo — it uses the reduced 7.25% rate (flag the `[RESEARCH GAP]`). - NEVER omit the ×13 annualisation when projecting the ISR base. - NEVER assume a single national minimum wage — use the MITRADEL Decree 13 cell for activity/size/region. - NEVER use the outdated "12.25%" retroactive employer figure — the current rate is 13.25%. - NEVER use 2027/2029 employer CSS rates for periods before their phase-in dates, or current rates after. - NEVER present payroll computations as definitive — always label as estimated and direct to a Panamanian Contador Público Autorizado.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Contador Público Autorizado in Panama) before implementation.

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
