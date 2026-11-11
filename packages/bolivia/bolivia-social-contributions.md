---
name: bolivia-social-contributions
description: "Bolivia social-security contributions for employees and employers in 2026: the long-term pension system (Sistema Integral de Pensiones, Ley 065 de Pensiones as amended by Ley 1582) collected by the Gestora Pública, and the short-term health insurance paid to the Caja Nacional de Salud or another health fund. Covers the employee's 12.71% (10% monthly contribution, 1.71% common-risk premium, 0.5% solidarity contribution, 0.5% commission), the Aporte Nacional Solidario of 1.15%, 5.74% and 11.48% above Bs 13,000, Bs 25,000 and Bs 35,000, the employer's 10% health contribution, 1.71% professional-risk premium, 2% housing contribution and 3.5% employer solidarity contribution, the 2.3% mining solidarity contribution, the total ganado base, the 2026 minimum wage of Bs 3,300, the Gestora payment deadline, foreign employees, late-payment rules and bank-statement patterns. Trigger on: aportes Gestora, aporte laboral 12.71%, aporte patronal, Aporte Nacional Solidario, ANS, Caja Nacional de Salud 10%, CNS, pro vivienda, riesgo profesional, total ganado, Bolivia social security. Out of scope: RC-IVA withholding (bolivia-income-tax), the monthly payroll run and labour benefits (bolivia-payroll)."
version: 0.2
jurisdiction: BO
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - social-contributions-workflow-base
category: international
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
---

# Bolivia social-security contributions for 2026: Gestora pensions, health fund, housing and solidarity v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The law is Ley N° 065 de Pensiones of 10 December 2010 (the Sistema Integral de Pensiones, SIP), as amended by Ley N° 1582 of 1 October 2024, with its contributions regulation (DS 0778 of 26 January 2011, its attachment replaced by DS 5280 of 20 November 2024). Short-term health insurance is financed under DS 21637 of 25 June 1987. The 2026 minimum wage is in DS 5516. All texts were read in the Gaceta Oficial de Bolivia. The pension contributions are collected by the Gestora Pública de la Seguridad Social de Largo Plazo (the Gestora) and supervised by the APS; health contributions go to the employer's health fund (Caja Nacional de Salud, CNS, or another caja). All amounts are in bolivianos (Bs). Tax year 2026, contributions monthly.

This skill owns the contribution rates. The employee's RC-IVA withholding, which deducts these contributions, is in [bolivia-income-tax](bolivia-income-tax.md). The monthly payroll run, the aguinaldo, severance and other labour items are in [bolivia-payroll](bolivia-payroll.md).

## Who this applies to

- **Dependent employees (asegurados dependientes)** in the private and public sectors, and their employers. The employer registers with the Gestora and the health fund, deducts the employee's share from the total ganado and pays both shares (Ley 065 arts. 83 and 94).
- **Foreign employees** with an employment relationship in Bolivia must contribute to the SIP like nationals (Ley 065 art. 104 I a). A foreign insured person who leaves Bolivia for good without a pension can have the balance in their account transferred to the pension body of their country or another one they name (art. 105).
- **Mining and metallurgical employers** pay an extra 2.3% for their productive-area workers (Ley 065 art. 87 d, text of Ley 1582).
- **Out of scope:** independent workers and consultants contributing on their own (asegurados independientes, Ley 065 art. 101, with a common-risk and a labour-risk premium on their contribution income); mining cooperatives; voluntary contributors; pensioners who keep working. Refer these.

**When to refer.** Refer for: very high earners where a contribution ceiling may apply (not confirmed here); people with several employers (the Aporte Nacional Solidario is then declared on the combined total through a Declaración Jurada Previsional, Ley 065 art. 95); arrears and the Gestora's interest for late payment; mining cooperatives; workers aged 65 or over (the risk premiums stop at 65, Ley 065 art. 83).

## Rates, bands and thresholds

Quick answer: the **employee pays 12.71%** of total ganado, plus the Aporte Nacional Solidario (ANS) on the slices above Bs 13,000. The **employer pays 17.21%** (10% health, 1.71% professional risk, 2% housing, 3.5% solidarity), or 19.51% for mining productive-area workers.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Employee: monthly contribution (cotización mensual) to the personal pension account (Ley 065 art. 88) | 10% of total ganado | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/138860 |
| Employee: common-risk premium (prima por riesgo común), deducted from total ganado (Ley 065 art. 83 b), paid until age 65 | 1.71% of total ganado | 2026 | https://gestora.bo/pdf/folletos/3/4.jpg |
| Employee: solidarity contribution (aporte solidario del asegurado) (Ley 065 art. 87 b) | 0.5% of total ganado | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/138860 |
| Employee: Gestora commission (comisión) (Ley 065 art. 151 a), reviewable every three years | 0.5% of total ganado | 2026 | same |
| Employee total (aportes laborales) | 12.71% of total ganado | 2026 | https://gestora.bo/pdf/folletos/3/3.jpg |
| Employee: Aporte Nacional Solidario, slice of total ganado above Bs 13,000 (Ley 065 art. 87 f iii, text of Ley 1582) | 1.15% | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/280468 |
| ANS, slice above Bs 25,000 (art. 87 f ii) | a further 5.74% (6.89% in all on that slice) | 2026 | same |
| ANS, slice above Bs 35,000 (art. 87 f i) | a further 11.48% (18.37% in all on that slice) | 2026 | same |
| Employer: health contribution to the health fund (DS 21637 art. 8) | 10% of all pay of insured workers | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/18031 |
| Employer: professional-risk premium (prima por riesgo profesional) (Ley 065 art. 83 a), paid until the worker is 65 | 1.71% of total ganado | 2026 | https://gestora.bo/pdf/folletos/3/4.jpg |
| Employer: housing contribution (aporte patronal para vivienda), collected by the Gestora (DS 4942 art. 1) | 2% of total ganado | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/169107 |
| Employer: employer solidarity contribution (aporte patronal solidario) (Ley 065 art. 87 c, text of Ley 1582, from gestión 2024) | 3.5% of total ganado | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/280468 |
| Employer, mining and metallurgical sector, productive-area workers only: aporte solidario minero (art. 87 d, text of Ley 1582; DS 0778 art. 15, text of DS 5280) | 2.3% of total ganado | 2026 | same |
| Employer total, general (sum of the four rows above it) | 17.21% of total ganado | 2026 | same |
| Employer total, mining productive-area workers | 19.51% of total ganado | 2026 | same |
| National minimum wage (SMN), public and private sectors, retroactive to 1 January 2026 (DS 5516 art. 23) | Bs 3,300 a month | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281033 |
| Payment deadline to the Gestora (DS 0778 art. 6 I, cited in DS 5280; Gestora leaflet) | Last working day of the month after the month the pay was earned | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/280548 |
| Declaración Jurada Previsional for ANS contributors (Ley 065 art. 95) | Required when total solidario is Bs 13,000 or more | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/138860 |

The two 1.71% premiums come from the Gestora's own employer leaflet, an image on gestora.bo. The same leaflet shows the employer solidarity contribution at 3%, the figure before Ley 1582; the law (3.5%) governs. Ley 1582 lets the Executive update the ANS thresholds every five years.

## The base

**Total ganado.** Every contribution is a percentage of the worker's total ganado, the gross pay for the month (Ley 065 arts. 83, 87, 88 and 94). Take the gross from the payroll (salary plus the other pay items the payroll includes). The health contribution is on "la totalidad de las remuneraciones" of insured workers (DS 21637 art. 8).

**Employee share, step by step:**

1. Monthly contribution 10%, common-risk premium 1.71%, solidarity contribution 0.5% and commission 0.5%: 12.71% of total ganado. The employer deducts it from pay as withholding agent (Ley 065 art. 94).
2. Aporte Nacional Solidario. If total ganado is above Bs 13,000, add 1.15% of the excess over Bs 13,000; if above Bs 25,000, add 5.74% of the excess over Bs 25,000; if above Bs 35,000, add 11.48% of the excess over Bs 35,000 (art. 87 f). Each percentage applies to the difference over its threshold "cuando la diferencia sea positiva", so they stack on the top slices. A dependent pays it through the employer on their total ganado (art. 94 a).
3. The employee's contributions are deducted from the RC-IVA base in the employer's monthly RC-IVA computation ([bolivia-income-tax](bolivia-income-tax.md)).

**Employer share, step by step:**

1. Health 10%, to the CNS or the health fund the employer is registered with.
2. Professional-risk premium 1.71%, housing 2% and employer solidarity 3.5%, to the Gestora.
3. Mining and metallurgical employers add 2.3% for productive-area workers.
4. These are the employer's own cost, never deducted from the worker. Unpaid contributions and interest can never be charged to the worker later (Ley 065 art. 107).

**Where the money goes.** The 10% goes to the worker's personal pension account (art. 88). The solidarity contributions and the ANS finance the Solidarity Fund (art. 87). The risk premiums finance disability and death benefits (art. 83). The commission pays the Gestora (art. 151).

## Deadlines and filing

**Steps, in the order the employer meets them:**

1. **Register as an employer with the Gestora** through the electronic employer registration form on gestora.bo or at its offices, with the legal representative's ID, power of attorney, the employer's identification documents and a location sketch (Gestora employer leaflet).
2. **Register each worker** with the SIP on the electronic registration form (same leaflet).
3. **Register as an employer with the health fund.** For the CNS: forms AVC-01, AVC-02 and RCI-1A, the NIT certificate, an opening balance sheet signed by the departmental college of accountants, the company deed if a company, the payroll (one original and five copies signed by the workers), a list of staff with dates of birth, a location sketch and a pre-employment medical receipt of Bs 100 per worker (CNS employer page). Report each worker who leaves on the "Aviso de Baja de Asegurado" form within 30 calendar days (Decreto Ley 13214 art. 8, text of Ley 890).
4. **Each month,** compute both shares on the month's total ganado and deduct the employee's 12.71% and any ANS from pay.
5. **Declare and pay the Gestora** through the Formulario de Pago de Contribuciones (FPC), online in the Gestora's virtual office or at a bank, by the **last working day of the month after the pay month**. July 2026 pay is due by Monday 31 August 2026 (DS 0778 art. 6 I; Gestora employer leaflet).
6. **Pay the health fund** its 10% under its own planilla.
7. From the day after the deadline the employer is in arrears (mora) and owes interest for late payment and an incremental interest, under the regulation (Ley 065 art. 107).

## Penalties and interest

- **Late payment to the Gestora:** the employer is in arrears from the day after the deadline and owes the contributions, the interés por mora, the interés incremental and surcharges (Ley 065 arts. 106 and 107). The Gestora collects through an administrative procedure, a coercive social-security procedure (its debit note is an enforceable title) and, where it applies, criminal proceedings (arts. 106, 109 and 110). The interest rates are set by regulation and were not read here.
- **ANS contributors in arrears** owe the same interest (art. 108).
- **No charge to the worker:** contributions and interest the employer failed to pay can never be collected from the insured worker (art. 107).

## Cross-border points

- **Foreign employees** working for an employer in Bolivia contribute in full (Ley 065 art. 104 I a). On leaving Bolivia for good without a pension they may transfer their account balance abroad (art. 105).
- **Bolivians employed by foreign embassies and international organisations accredited in Bolivia** also contribute; the employer acts as withholding agent (art. 104 I b).
- **No social-security agreement** was read for this skill. Posted workers and totalisation of periods with other countries: refer.
- Tax on pay for work in Bolivia by non-domiciled individuals: [bolivia-income-tax](bolivia-income-tax.md). Payments for services from abroad: [bolivia-cross-border](bolivia-cross-border.md).

## Two worked examples that recompute

### Example 1: employee on Bs 8,000 a month, general employer

July 2026. Total ganado Bs 8,000, below the ANS threshold.

- Employee: 10% Bs 800.00; 1.71% Bs 136.80; 0.5% Bs 40.00; 0.5% Bs 40.00; total Bs 1,016.80 (12.71%). ANS: none.
- Employer: health 10% Bs 800.00; professional risk 1.71% Bs 136.80; housing 2% Bs 160.00; solidarity 3.5% Bs 280.00; total Bs 1,376.80 (17.21%).
- Pay before RC-IVA: Bs 6,983.20. Employer cost: Bs 9,376.80.
- The Gestora FPC for July (Bs 1,016.80 employee plus Bs 576.80 employer, Bs 1,593.60) is due by Monday 31 August 2026; the Bs 800 goes to the health fund.

```oa-check
name: Employee Bs 8,000, July 2026, general employer
inputs:
  total_ganado: 8000
steps:
  - pension_10: total_ganado * 0.10
  - riesgo_comun: total_ganado * 0.0171
  - solidario_asegurado: total_ganado * 0.005
  - comision: total_ganado * 0.005
  - employee_total: pension_10 + riesgo_comun + solidario_asegurado + comision
  - health: total_ganado * 0.10
  - riesgo_profesional: total_ganado * 0.0171
  - vivienda: total_ganado * 0.02
  - patronal_solidario: total_ganado * 0.035
  - employer_total: health + riesgo_profesional + vivienda + patronal_solidario
  - to_gestora: employee_total + riesgo_profesional + vivienda + patronal_solidario
  - pay_before_rc_iva: total_ganado - employee_total
  - employer_cost: total_ganado + employer_total
expected:
  employee_total: 1016.80
  employer_total: 1376.80
  to_gestora: 1593.60
  pay_before_rc_iva: 6983.20
  employer_cost: 9376.80
```

### Example 2: high earner on Bs 40,000 a month, general and mining employer

Total ganado Bs 40,000. All three ANS slices apply.

- Employee 12.71%: Bs 5,084.00.
- ANS: (40,000 - 13,000) x 1.15% = Bs 310.50; (40,000 - 25,000) x 5.74% = Bs 861.00; (40,000 - 35,000) x 11.48% = Bs 574.00. ANS Bs 1,745.50.
- Employee deductions: Bs 6,829.50. Pay before RC-IVA: Bs 33,170.50.
- Employer, general: 17.21% = Bs 6,884.00. The edge: a mining employer, for a productive-area worker, adds 2.3% (Bs 920.00): Bs 7,804.00 (19.51%).

```oa-check
name: Employee Bs 40,000, ANS three slices, general and mining employer (2026)
inputs:
  total_ganado: 40000
steps:
  - employee_base: total_ganado * 0.1271
  - ans_1: max(total_ganado - 13000, 0) * 0.0115
  - ans_2: max(total_ganado - 25000, 0) * 0.0574
  - ans_3: max(total_ganado - 35000, 0) * 0.1148
  - ans: ans_1 + ans_2 + ans_3
  - employee_deductions: employee_base + ans
  - pay_before_rc_iva: total_ganado - employee_deductions
  - employer_general: total_ganado * 0.1721
  - employer_mining: employer_general + total_ganado * 0.023
expected:
  employee_base: 5084.00
  ans_1: 310.50
  ans_2: 861.00
  ans_3: 574.00
  ans: 1745.50
  employee_deductions: 6829.50
  pay_before_rc_iva: 33170.50
  employer_general: 6884.00
  employer_mining: 7804.00
```

### Bank-statement patterns

| Pattern in the narrative | What it is |
|---|---|
| GESTORA, GESTORA PUBLICA, FPC, APORTES, PLANILLA APORTES, COMISION GESTORA | Monthly payment to the Gestora: employee 12.71%, ANS, professional risk, housing, employer solidarity |
| APORTE NACIONAL SOLIDARIO, ANS, APORTE SOLIDARIO | Solidarity contributions, inside the Gestora payment |
| CNS, CAJA NACIONAL DE SALUD, CAJA DE SALUD, SEGURO CORTO PLAZO | Employer health contribution, 10% |
| PRO VIVIENDA, PROVIVIENDA, VIVIENDA | Housing 2%, collected by the Gestora |
| RIESGO PROFESIONAL, RIESGO COMUN | Risk premiums, inside the Gestora payment |
| SIN, IMPUESTOS NACIONALES, SIAT, FORM 608, RC-IVA | RC-IVA withheld from pay ([bolivia-income-tax](bolivia-income-tax.md)), not a contribution |
| IVA, FORM 200, IT, FORM 400, IUE, FORM 500 | Tax payments ([bolivia-iva](bolivia-iva.md), [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md)), not contributions |
| SUELDO, SALARIO, HABERES, PLANILLA SUELDOS, AGUINALDO, INDEMNIZACION, DESAHUCIO | Pay to workers ([bolivia-payroll](bolivia-payroll.md)), not contributions |

Bolivian bank exports (Banco Unión, BNB, Banco Mercantil Santa Cruz, Banco BISA, BCP) usually show dates as DD/MM/YYYY and amounts with a comma for decimals and a point for thousands (1.016,80).

## Ask the client first

1. Monthly total ganado of each worker, and whether anyone has a second employer (ANS on the combined total, Declaración Jurada Previsional).
2. The employer's sector: mining and metallurgical (2.3% extra for productive-area workers) or not.
3. Which health fund the employer is registered with (CNS or another caja).
4. Each worker's age (the risk premiums stop at 65) and whether anyone already draws a pension.
5. Whether any worker is foreign, posted from abroad, or works for an embassy or international organisation.
6. Any months not yet paid to the Gestora or the health fund.

## Sources

| Source | URL | Read on |
|---|---|---|
| Gaceta Oficial, Ley N° 065 de Pensiones of 10 December 2010 (HTML text): read arts. 83, 87, 88, 94, 95, 101, 104 to 110 and 151 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/138860 | 2026-11-11 |
| Gaceta Oficial, Ley N° 1582 of 1 October 2024 (HTML text): read art. 2 II (new art. 87 c, d and f) and Disposición Final Segunda (applies from gestión 2024) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/280468 | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 5280 of 20 November 2024 (HTML text): read the recitals (DS 0778 art. 6 I deadline) and art. 2 (new DS 0778 art. 15, 2.3% mining); the attachment it replaces is not in the HTML | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/280548 | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 21637 of 25 June 1987 (HTML text): read art. 8 (10% employer health contribution) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/18031 | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 4942 of 17 May 2023 (HTML text): read art. 1 (Gestora collects the 2% employer housing contribution) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/169107 | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 5516 (HTML text): read art. 23 (SMN Bs 3,300 from 1 January 2026) and art. 21 (salary negotiation) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281033 | 2026-11-11 |
| Gaceta Oficial, Ley N° 890 of 26 January 2017 (HTML text): read the new art. 8 of Decreto Ley 13214 (30-day leaver notice) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/154386 | 2026-11-11 |
| Gestora, employer leaflet, page 3 (image): who is an employer, registration, the 12.71% employee total | https://gestora.bo/pdf/folletos/3/3.jpg | 2026-11-11 |
| Gestora, employer leaflet, page 4 (image): employee and employer percentage tables, FPC, last working day of the following month | https://gestora.bo/pdf/folletos/3/4.jpg | 2026-11-11 |
| Caja Nacional de Salud, employer page: documents to register an employer and report changes | https://www.cns.gob.bo/Site/empleador | 2026-11-11 |

Not yet confirmed: the regulation that sets the 1.71% common-risk and professional-risk premiums (the DS 0778 attachment as replaced by DS 5280 is not in the Gaceta HTML; the figures come from the Gestora's leaflet); whether a contribution ceiling (tope) applies to total ganado, and at what amount, for 2026; the definitions of total ganado and total solidario in Ley 065's glossary; the health fund's payment deadline and its late-payment surcharges; the Gestora's interest rates for late payment; the treatment of the aguinaldo and severance in the contribution base; any social-security agreement with another country; whether the Executive has updated the ANS thresholds since Ley 1582.
