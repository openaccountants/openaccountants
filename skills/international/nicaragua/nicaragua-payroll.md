---
name: nicaragua-payroll
description: Use this skill whenever asked about Nicaragua payroll processing for employed persons. Trigger on phrases like "Nicaragua payroll", "nomina Nicaragua", "INSS deduction", "INSS laboral", "INSS patronal", "IR rentas del trabajo", "retencion IR Nicaragua", "INATEC 2%", "Form IR-122", "Form IR-106", "planilla INSS", "salario neto Nicaragua", "net salary Nicaragua", "cordoba payroll", "employer social security Nicaragua", "salario minimo Nicaragua", "minimum wage Nicaragua", "gross to net Nicaragua", or any question about computing employee pay, income-tax withholding, or social-security contributions for Nicaragua-based employees. This skill covers IR (rentas del trabajo) progressive withholding, INSS employee/employer contributions (Regimen Integral), the INATEC training levy, sector minimum wages, payroll filing obligations (IR-122, IR-106, INSS planilla), and penalties. The reporting currency is the Nicaraguan cordoba (NIO / C$). ALWAYS read this skill before processing any Nicaragua payroll.
version: 0.1
jurisdiction: NI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nicaragua Payroll Skill v0.1 (Tier 2 — research-verified, pending accountant sign-off)

## Nicaragua Payroll Skill v0.1 (Tier 2 — research-verified, pending accountant sign-off)

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Nicaragua (Republic of Nicaragua) |
| Currency | Nicaraguan cordoba (NIO / C$) only |
| Standard pay frequency | Monthly (most common); biweekly (quincenal) permitted |
| Tax year | Calendar year (1 January -- 31 December); alternative 12-month periods may be authorized [PwC, Ley 822] |
| Income-tax system | IR -- Rentas del Trabajo (PAYE-style monthly withholding by employer) |
| Tax authority | Direccion General de Ingresos (DGI) -- dgi.gob.ni |
| Social-security authority | Instituto Nicaraguense de Seguridad Social (INSS) -- inss.gob.ni |
| Training levy | INATEC -- 2% of gross payroll, collected via the INSS invoice |
| Key legislation | Ley de Concertacion Tributaria (Ley 822, rentas del trabajo Art. 23); Ley de Seguridad Social + 2019 reform (Decreto Presidencial); Codigo del Trabajo (Ley 185); INATEC levy decree |
| Filing portal | DGI Ventanilla Electronica Tributaria (VET); INSS SIE (Sistema Integrado de aplicaciones Especificas) |
| Validated by | Pending -- requires sign-off by a licensed Nicaraguan accountant (Contador Publico Autorizado) |
| Skill version | 0.1 (Tier 2 -- research-verified) |

This is a **Tier-2 research-verified** skill. Several figures are flagged **[RESEARCH GAP — reviewer to confirm]** where a fully authoritative source could not be isolated. Do not treat any computation as final until a licensed Nicaraguan accountant signs off.

## Section 2 -- Income Tax Withholding (IR -- Rentas del Trabajo)

- **IR withholding method overview** — The employer withholds income tax monthly on employment income (rentas del trabajo) and remits it to the DGI. The tax is computed by annualizing the employee's monthly taxable income, applying the progressive table, then dividing the annual liability by 12 (or by the number of pay periods).
- **Taxable base** — Taxable base = gross salary minus the employee's INSS contribution. The 7% employee INSS deduction is taken before the IR table is applied.  _([PwC Worldwide Tax Summaries — Nicaragua, last reviewed 12 Jan 2026])_

### IR Progressive Annual Brackets — residents (NIO)

**IR Progressive Annual Brackets — residents (NIO)**  _([Source: PwC Worldwide Tax Summaries — Nicaragua / Ley de Concertacion Tributaria (Ley 822), Art. 23. https://taxsummaries.pwc.com/nicaragua/individual/taxes-on-personal-income])_

| Annual taxable income (NIO) | Base tax (NIO) | Marginal rate on excess over lower bound |
| --- | --- | --- |
| 0 -- 100,000.00 | 0 | 0% (exempt) |
| 100,000.01 -- 200,000.00 | 0 | 15% |
| 200,000.01 -- 350,000.00 | 15,000 | 20% |
| 350,000.01 -- 500,000.00 | 45,000 | 25% |
| 500,000.01 and over | 82,500 | 30% |

**Cumulative-base self-check** (recomputed):
- At C$200,000: 0 + 15% x (200,000 − 100,000) = **15,000** -> matches base of next band ✓
- At C$350,000: 15,000 + 20% x (350,000 − 200,000) = 15,000 + 30,000 = **45,000** ✓
- At C$500,000: 45,000 + 25% x (500,000 − 350,000) = 45,000 + 37,500 = **82,500** ✓

### Key rules

- **IR exemption** — The first C$100,000 of annual net employment income is exempt (the 0% band is the tax-free allowance — there is no separate personal allowance).  _([PwC / Ley 822])_
- **Non-residents flat rate** — Non-residents: flat 20% definitive withholding on Nicaraguan-source income (no bracket table, no annualization).  _([PwC — Nicaragua, taxes on personal income])_
- **Tax year** — Tax year = calendar year.  _([PwC])_

### Monthly withholding method (deterministic)

- **Monthly withholding method** — 1. monthly_inss_employee   = gross_monthly x 0.07 2. monthly_taxable         = gross_monthly − monthly_inss_employee 3. annual_taxable          = monthly_taxable x 12          (annualize) 4. annual_IR               = base_tax(band) + rate(band) x (annual_taxable − band_floor) 5. monthly_IR_withholding  = annual_IR / 12 6. net_pay                 = gross_monthly − monthly_inss_employee − monthly_IR_withholding

If pay is irregular (bonuses, 13th-month aguinaldo), reconcile via the annual IR-106 return rather than the simple /12 method — flag to reviewer.

## Section 3 -- Social Security -- INSS Employee Deductions (Regimen Integral)

- **Employee INSS overview** — Employee INSS is computed on gross salary/wages at a total of 7.00%. Rates per the 2019 INSS reform (effective 1 Feb 2019, current for 2025).  _([Latin Alliance reform summary; PwC — Nicaragua, other taxes])_

### INSS Employee Contribution Components (2025)

**INSS Employee Contribution Components (2025)**

| Component | Rate |
| --- | --- |
| IVM (Invalidez, Vejez y Muerte — pensions) | 4.75% |
| Enfermedad y Maternidad (health) | 2.25% |
| **Total employee** | **7.00%** |

**Component self-check:** 4.75% + 2.25% = **7.00%** ✓

### Contribution ceiling (techo de cotizacion)

- **No statutory ceiling** — The 2019 reform eliminated the salary cap ("se elimina el limite maximo para la remuneracion objeto de cotizacion"). Treat as no statutory ceiling.  _([Latin Alliance — 2019 reform])_
- **Disputed ceiling figure** — **[RESEARCH GAP — reviewer to confirm]** A secondary calculator source (calculorapido.com) cites a 2025 ceiling of C$130,362.60/month. This conflicts with the authoritative "no ceiling" position from the 2019 reform and could not be confirmed against an INSS/official source. Default to "no ceiling" unless INSS publishes otherwise; have the reviewer verify before finalizing high-earner payroll.

For biweekly (quincenal) pay, contributions are computed on the period's gross and totalled monthly on the planilla.

## Section 4 -- Social Security -- INSS Employer Contributions + INATEC

- **Employer INSS overview** — Employer INSS is computed on gross salary/wages. The total rate depends on headcount (the 50-employee line changes only the IVM portion).  _([Latin Alliance — 2019 reform; PwC])_

### INSS Employer Contribution Components (2025)

**INSS Employer Contribution Components (2025)**

| Component | < 50 employees | >= 50 employees |
| --- | --- | --- |
| IVM (pensions) | 12.5% | 13.5% |
| Enfermedad y Maternidad (health) | 6.0% | 6.0% |
| Riesgos Profesionales (occupational risk) | 1.5% | 1.5% |
| Victimas de Guerra (war victims) | 1.5% | 1.5% |
| **Total employer INSS** | **21.5%** | **22.5%** |

**Component self-check:**
- < 50: 12.5 + 6.0 + 1.5 + 1.5 = **21.5%** ✓
- >= 50: 13.5 + 6.0 + 1.5 + 1.5 = **22.5%** ✓

### INATEC training levy

**INATEC training levy**  _([Source: serviciocontablenicaragua.com — gestion de nomina; INATEC levy decree https://ni.vlex.com/vid/reglamento-recaudo-aporte-mensual-36219852])_

| Levy | Rate | Base | Paid by | Collected via |
| --- | --- | --- | --- | --- |
| INATEC | 2.0% | Total gross monthly payroll | Employer (NOT deducted from employees) | Same monthly INSS invoice (INSS is collection agent) |

### Total employer payroll burden

**Total employer payroll burden**

| Headcount | INSS employer | INATEC | **Total employer burden** |
| --- | --- | --- | --- |
| < 50 employees | 21.5% | 2.0% | **23.5%** |
| >= 50 employees | 22.5% | 2.0% | **24.5%** |

**Self-check:** 21.5 + 2.0 = **23.5%** ✓ ; 22.5 + 2.0 = **24.5%** ✓

## Section 5 -- Minimum Wage (effective 1 March 2025 -- 28 February 2026)

- **4% increase context** — A 4% increase was agreed by the Comision Nacional de Salario Minimo, effective 1 March 2025. Monthly minimums by sector (NIO/month).  _([Bloomberg Linea, 28 Feb 2025; CNZF confirmation of 4% rise])_

**Minimum wage by sector**  _([Sources: https://www.bloomberglinea.com/2025/02/28/salario-minimo-de-nicaragua-2025-los-montos-por-sector-a-partir-del-1-de-marzo/ ; https://cnzf.gob.ni/salario-minimo-en-nicaragua-subira-4-a-partir-del-1-de-marzo/])_

| Sector | Monthly minimum (C$) |
| --- | --- |
| Agropecuario (agriculture) | 5,950.02 |
| Micro/pequena industria artesanal y turistica | 6,268.43 |
| Gobierno Central y Municipal | 7,419.90 |
| Minas, canteras e industria manufacturera | 8,046.00 |
| Pesca (fishing) | 9,047.20 |
| Electricidad/gas/agua, comercio, restaurantes, hoteles, transporte, comunicaciones | 10,913.54 |
| Construccion, establecimientos financieros y seguros | 13,315.61 |
| Industria sujeta a regimen fiscal (zonas francas / maquila) | **[RESEARCH GAP — reviewer to confirm]** — set separately; not isolated in sources. Verify with MITRAB. |

## Section 6 -- Conservative Defaults

- **Missing input policy** — When an input is missing, apply the most conservative defensible assumption, label the output ESTIMATED, and surface the assumption for reviewer confirmation.

**Conservative defaults table**

| Unknown | Conservative default | Rationale |
| --- | --- | --- |
| Residence status | Treat as **resident** (use bracket table) ONLY if local employment is confirmed; otherwise flag. Apply 20% non-resident withholding only when non-residence is documented. | Resident brackets give a tax-free band; choosing wrongly under-withholds. Flag either way. |
| Employer headcount (for INSS rate) | Use **22.5%** (>= 50 employees rate) unless headcount < 50 is confirmed | Higher employer rate avoids under-accruing the employer liability. |
| INSS ceiling | **No ceiling** (per 2019 reform) | Authoritative position; computes the full 7% / 21.5--22.5%. Reviewer to confirm the disputed C$130,362.60 figure. |
| Sector minimum wage | Use the **highest plausible applicable** sector rate when sector is ambiguous | Prevents paying below the statutory floor. |
| Pay frequency | Monthly | Most common in Nicaragua. |
| Aguinaldo (13th month) | Assume payable (mandatory under Codigo del Trabajo) and flag for separate treatment | 13th-month is a statutory entitlement; omitting it understates cost. |

- **Default disclosure requirement** — Never silently fill a gap — every default must appear in the output with a "(assumed)" tag.

## Section 7 -- Required Inputs & Refusal Catalogue

### Minimum required inputs to compute a payslip

- **Minimum required inputs** — 1. Gross monthly salary (C$) 2. Pay frequency (monthly / quincenal) 3. Employee residence status (resident / non-resident) 4. Employer headcount band (< 50 or >= 50 employees) — for the employer INSS rate 5. Sector (to validate against minimum wage)

### Refusal Catalogue — STOP and request input; do NOT guess

**Refusal Catalogue table**

| Missing / ambiguous input | Action |
| --- | --- |
| Gross salary not provided | REFUSE to compute; request the gross figure |
| Currency stated as anything other than NIO/C$ | REFUSE; confirm the cordoba amount (do not FX-convert silently) |
| Residence status unknown AND salary is high | REFUSE to finalize; resident vs 20% non-resident materially changes tax |
| Headcount band unknown | Compute with the 22.5% default, label ESTIMATED, request confirmation |
| Request to compute net pay below the sector minimum wage | REFUSE; warn that the gross breaches the statutory minimum |
| Request to omit INSS or INATEC to "lower cost" | REFUSE; these are mandatory statutory charges |
| Request for definitive/final figures without accountant review | REFUSE to label as final; output is ESTIMATED only |

## Section 8 -- Transaction / Payment Pattern Library

Deterministic mapping of common Nicaraguan bank-statement narrations to payroll classifications. Match case-insensitively; Spanish and English variants both occur.

### Salary credits (employee side)

**Salary credits table**

| Narration pattern (es/en) | Classification |
| --- | --- |
| PAGO NOMINA, NOMINA, SALARIO, PAGO SALARIO | Net salary payment |
| ABONO SALARIO, DEPOSITO NOMINA, PLANILLA | Net salary payment |
| QUINCENA, PAGO QUINCENAL | Net salary (biweekly) |
| AGUINALDO, 13ER MES, TRECEAVO MES | 13th-month bonus (aguinaldo) — statutory |
| VACACIONES, PAGO VACACIONES | Vacation pay |
| LIQUIDACION, INDEMNIZACION | Severance / final settlement |

### Employer debit patterns

**Employer debit patterns table**

| Narration pattern (es/en) | Classification |
| --- | --- |
| INSS, PAGO INSS, FACTURA INSS, SIE INSS | INSS contribution remittance (employee + employer + INATEC bundled) |
| INATEC, APORTE INATEC | INATEC 2% levy (usually inside the INSS invoice) |
| DGI, IR-122, RETENCION IR, PAGO IR | IR (rentas del trabajo) withholding remitted to DGI |
| VET DGI, DECLARACION IR | DGI tax filing payment |
| PLANILLA, PAGO PLANILLA, NOMINA RUN | Payroll disbursement to employees |

### Posting template (double-entry shorthand)

```
On payroll accrual (per employee, monthly):
  Dr  Salary expense (gross)                  gross
  Dr  Employer INSS expense                   gross x 21.5% or 22.5%
  Dr  INATEC expense                          gross x 2.0%
      Cr  Net pay payable                      net
      Cr  INSS payable (employee 7%)           gross x 7%
      Cr  INSS payable (employer)              gross x 21.5% / 22.5%
      Cr  INATEC payable                       gross x 2.0%
      Cr  IR withholding payable (DGI)         monthly IR

On INSS/INATEC remittance (combined invoice, by ~10th business day):
  Dr  INSS payable + INATEC payable
      Cr  Bank

On DGI IR remittance (IR-122):
  Dr  IR withholding payable
      Cr  Bank
```

## Section 9 -- Worked Examples

All figures in NIO (C$). INSS employee = 7%. Resident IR uses the Section 2 bracket table on the annualized base. Each example is recomputed end-to-end below.

### Example A — Mid earner, small firm (< 50 employees)

Gross monthly: C$30,000. Resident. Sector: commerce. Headcount < 50.

**Example A table**

| Step | Computation | Result (C$) |
| --- | --- | --- |
| Employee INSS (monthly) | 30,000 x 7% | 2,100.00 |
| Monthly taxable | 30,000 − 2,100 | 27,900.00 |
| Annualized taxable | 27,900 x 12 | 334,800.00 |
| Band | 200,000.01 -- 350,000 (base 15,000, 20%) | — |
| Annual IR | 15,000 + 20% x (334,800 − 200,000) = 15,000 + 26,960 | 41,960.00 |
| Monthly IR | 41,960 / 12 | 3,496.67 |
| **Net pay (monthly)** | 30,000 − 2,100 − 3,496.67 | **24,403.33** |
| Employer INSS | 30,000 x 21.5% | 6,450.00 |
| INATEC | 30,000 x 2% | 600.00 |
| **Total employer cost** | 30,000 + 6,450 + 600 | **37,050.00** |

### Example B — Commerce minimum wage

Gross monthly: C$10,913.54 (commerce sector minimum). Resident. Headcount < 50.

**Example B table**

| Step | Computation | Result (C$) |
| --- | --- | --- |
| Employee INSS | 10,913.54 x 7% | 763.95 |
| Monthly taxable | 10,913.54 − 763.95 | 10,149.59 |
| Annualized taxable | 10,149.59 x 12 | 121,795.08 |
| Band | 100,000.01 -- 200,000 (15%) | — |
| Annual IR | 15% x (121,795.08 − 100,000) = 15% x 21,795.08 | 3,269.26 |
| Monthly IR | 3,269.26 / 12 | 272.44 |
| **Net pay (monthly)** | 10,913.54 − 763.95 − 272.44 | **9,877.15** |
| Employer INSS | 10,913.54 x 21.5% | 2,346.41 |
| INATEC | 10,913.54 x 2% | 218.27 |
| **Total employer cost** | 10,913.54 + 2,346.41 + 218.27 | **13,478.22** |

### Example C — Exempt low earner (manufacturing minimum)

Gross monthly: C$8,046.00 (minas/manufactura minimum). Resident. Headcount < 50.

**Example C table**

| Step | Computation | Result (C$) |
| --- | --- | --- |
| Employee INSS | 8,046 x 7% | 563.22 |
| Monthly taxable | 8,046 − 563.22 | 7,482.78 |
| Annualized taxable | 7,482.78 x 12 | 89,793.36 |
| Band | 0 -- 100,000 (0% exempt) | — |
| Annual IR | 0 (below C$100,000 exemption) | 0.00 |
| Monthly IR | — | 0.00 |
| **Net pay (monthly)** | 8,046 − 563.22 − 0 | **7,482.78** |
| Employer INSS | 8,046 x 21.5% | 1,729.89 |
| INATEC | 8,046 x 2% | 160.92 |
| **Total employer cost** | 8,046 + 1,729.89 + 160.92 | **9,936.81** |

### Example D — High earner, large firm (>= 50 employees)

Gross monthly: C$60,000. Resident. Headcount >= 50.

**Example D table**

| Step | Computation | Result (C$) |
| --- | --- | --- |
| Employee INSS | 60,000 x 7% | 4,200.00 |
| Monthly taxable | 60,000 − 4,200 | 55,800.00 |
| Annualized taxable | 55,800 x 12 | 669,600.00 |
| Band | 500,000.01+ (base 82,500, 30%) | — |
| Annual IR | 82,500 + 30% x (669,600 − 500,000) = 82,500 + 50,880 | 133,380.00 |
| Monthly IR | 133,380 / 12 | 11,115.00 |
| **Net pay (monthly)** | 60,000 − 4,200 − 11,115 | **44,685.00** |
| Employer INSS | 60,000 x 22.5% | 13,500.00 |
| INATEC | 60,000 x 2% | 1,200.00 |
| **Total employer cost** | 60,000 + 13,500 + 1,200 | **74,700.00** |

### Example E — Non-resident employee

Gross monthly: C$50,000. Non-resident (flat 20% definitive withholding, no bracket table, no exemption). [PwC]

**Example E table**

| Step | Computation | Result (C$) |
| --- | --- | --- |
| IR (definitive) | 50,000 x 20% | 10,000.00 |
| Income net of IR | 50,000 − 10,000 | 40,000.00 |
| Employee INSS (if locally employed) | 50,000 x 7% | 3,500.00 — **[RESEARCH GAP — reviewer to confirm INSS applicability to this non-resident's contract]** |
| **Net pay (if INSS applies)** | 50,000 − 10,000 − 3,500 | **36,500.00** |
| Employer INSS (>= 50) | 50,000 x 22.5% | 11,250.00 |
| INATEC | 50,000 x 2% | 1,000.00 |

Whether INSS applies to a non-resident depends on the employment relationship; confirm with the reviewer before finalizing.

## Section 10 -- Tier 1 Rules (deterministic — apply automatically)

- **Rule 1** — Employee INSS = 7.00% of gross, deducted before IR.  _([2019 reform])_
- **Rule 2** — IR taxable base = gross − employee INSS.  _([PwC / Ley 822])_
- **Rule 3** — Annualize monthly taxable income before applying the IR table; divide the resulting annual IR by 12 for the monthly withholding.
- **Rule 4** — First C$100,000 annual net is exempt (0% band).  _([Ley 822 Art. 23])_
- **Rule 5** — Non-residents: flat 20% definitive withholding, no brackets, no exemption.  _([PwC])_
- **Rule 6** — Employer INSS = 21.5% (< 50 staff) or 22.5% (>= 50 staff) of gross.  _([2019 reform])_
- **Rule 7** — INATEC = 2.0% of gross payroll, employer-paid, via the INSS invoice.  _([INATEC decree])_
- **Rule 8** — Gross must not be below the applicable sector minimum wage.  _([CNSM / Bloomberg Linea])_
- **Rule 9** — INSS and IR are remitted separately: INSS+INATEC on the combined INSS invoice; IR via DGI Form IR-122.
- **Rule 10** — Treat INSS as having no contribution ceiling unless the reviewer confirms otherwise.

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

These require a licensed Nicaraguan accountant's judgement — surface them, do not auto-resolve.

**Tier 2 catalogue table**

| Topic | Why it needs judgement |
| --- | --- |
| INSS contribution ceiling | Conflicting sources (no cap vs C$130,362.60/month). **[RESEARCH GAP]** |
| Aguinaldo (13th month) taxation | Interaction of the statutory 13th-month payment with the annual IR reconciliation. |
| Bonuses / variable pay | Irregular pay distorts the simple /12 annualization; reconcile on IR-106. |
| Non-resident INSS applicability | Depends on contract type and local-employment status. **[RESEARCH GAP]** |
| Zona franca / maquila minimum wage | Set separately by sector agreement. **[RESEARCH GAP]** |
| Expat / dual-coverage cases | Totalization, foreign social security, treaty positions. |
| Severance (liquidacion / indemnizacion) | Tax and INSS treatment of termination payments. |
| Exact DGI penalty percentages | Codigo Tributario figures not confirmed. **[RESEARCH GAP]** |
| Employees with 2+ employers | Aggregate-income filing obligation (> C$100,000/yr). |

## Section 12 -- Excel Working Paper Template

Recommended columns for a monthly payroll working paper (one row per employee).

**Excel working paper template table**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | RUC / cedula | input |
| C | Sector | input |
| D | Residence (R/NR) | input |
| E | Gross monthly (C$) | input |
| F | Sector minimum (C$) | lookup (Section 5) — flag if E < F |
| G | Employee INSS 7% | =E*0.07 |
| H | Monthly taxable | =E-G |
| I | Annualized taxable | =H*12 |
| J | Annual IR | bracket formula on I (Section 2) |
| K | Monthly IR | =J/12 (resident) or =E*0.20 (non-resident definitive) |
| L | Net pay | =E-G-K |
| M | Employer INSS % | 0.215 (<50) or 0.225 (>=50) |
| N | Employer INSS (C$) | =E*M |
| O | INATEC 2% | =E*0.02 |
| P | Total employer cost | =E+N+O |

Footer checks (must hold):
- `SUM(G) + SUM(K)` = total deductions remitted (INSS employee + IR)
- `SUM(N) + SUM(G) + SUM(O)` = total on the INSS/INATEC invoice + (note IR is separate to DGI)
- `SUM(L) + SUM(G) + SUM(K)` = `SUM(E)` (net + deductions = gross) for each resident row

## Section 13 -- Bank Statement / Terminology Reading Guide

Common Nicaraguan payroll and statement terms (Spanish -> meaning):

**Terminology reading guide table**

| Term | Meaning |
| --- | --- |
| Nomina / planilla | Payroll |
| Salario bruto | Gross salary |
| Salario neto | Net salary |
| Quincena / quincenal | Biweekly pay period |
| INSS laboral | Employee social-security deduction (7%) |
| INSS patronal | Employer social-security contribution (21.5% / 22.5%) |
| IVM | Invalidez, Vejez y Muerte (pension portion of INSS) |
| Retencion IR | Income-tax withholding (rentas del trabajo) |
| Aguinaldo / treceavo mes | 13th-month statutory bonus |
| Liquidacion | Final settlement on termination |
| Indemnizacion | Severance pay |
| RUC | Registro Unico del Contribuyente (taxpayer ID) |
| Cedula | National ID number |
| VET | Ventanilla Electronica Tributaria (DGI e-filing portal) |
| SIE | INSS electronic planilla system |

When reading a statement: a single combined "INSS" debit usually bundles employee 7% + employer 21.5/22.5% + INATEC 2%. The "DGI" / "IR-122" debit is the income-tax remittance and is always separate.

## Section 14 -- Onboarding Fallback

If the client cannot supply structured payroll data, gather the minimum manually:

1. **List each employee** with gross monthly salary and sector.
2. **Confirm headcount band** (< 50 or >= 50) once for the whole employer.
3. **Confirm residence** for any foreign staff.
4. **Confirm registrations exist**: INSS employer registration + DGI withholding-agent (RUC) registration. If either is missing, STOP and escalate — payroll cannot be legally run without them.
5. If no prior planillas exist, reconstruct the last 3 months from bank debits tagged "INSS" and "DGI/IR" using the Section 8 pattern library, and flag for reviewer.
6. Default any remaining gap per Section 6 and label all output ESTIMATED.

### Registration thresholds

**Registration thresholds table**

| Obligation | Trigger | Authority |
| --- | --- | --- |
| Register as employer + enrol worker (Regimen Integral) | **At least one employee** (no headcount minimum) | INSS |
| Register as withholding agent (RUC) for PAYE | Operating IR-122 withholding | DGI |
| 50-employee line | Changes only the **employer INSS rate** (21.5% -> 22.5%), not the obligation to register | INSS |

A precise statutory registration deadline window could not be isolated from an official page — **[RESEARCH GAP — reviewer to confirm]**.

### Income tax (DGI) filing

**Income tax filing table**

| Form | Purpose | Deadline |
| --- | --- | --- |
| IR-122 | Monthly IR withholding remittance | Within the first days of the following month — commonly stated as the **first 5 working days**, but the exact day was **not** confirmed from an official DGI source. **[RESEARCH GAP — reviewer to confirm]** [PwC tax administration] |
| IR-106 | Annual IR return | Within **90 days after year-end** (~31 March). For TY2025, DGI announced Form 106 with deadline **28 February 2026**. [EY Nicaragua DGI annual-declaration alert] |

- **Filing exemption / aggregate income rule** — Employees with a single employer and no education/health/professional-service deductions are exempt from filing. Employees with two or more employers whose aggregate income exceeds C$100,000/year must file annually.  _([PwC tax administration])_

### Social security (INSS) filing

**INSS filing table**

| Item | Deadline |
| --- | --- |
| Monthly contributions + planilla (SIE) | Within the **first 10 business days** of the month following accrual. [INSS / Reglamento General de la Ley de Seguridad Social] |

### Penalties

**Penalties table**

| Charge | Amount | Source |
| --- | --- | --- |
| INSS late payment (recargo por mora) | **2% monthly interest** on amount owed, capitalizing from due date | INSS Reglamento General; worki360 |
| INSS late/failed planilla submission | **2% surcharge** | INSS Reglamento General |
| INSS administrative fines | Additional fixed/proportional fines may apply | INSS |
| DGI late filing/payment (IR) | Codigo Tributario generally imposes a monthly surcharge (recargo por mora) plus interest (mantenimiento de valor); **exact current percentages NOT confirmed from an authoritative DGI source.** **[RESEARCH GAP — reviewer to confirm against Codigo Tributario / Ley 562]** | — |

## Section 16 -- Interaction with Other Skills

**Interaction with other skills table**

| Scenario | Skill to use |
| --- | --- |
| Employee payroll (IR + INSS + INATEC) | **This skill (nicaragua-payroll.md)** |
| Self-employed / independent income tax | nicaragua-income-tax.md (if available) |
| Nicaragua IVA (VAT) returns | nicaragua-vat-return.md (if available) |
| Nicaragua bookkeeping | nicaragua-bookkeeping.md (if available) |
| Employer corporate income tax (IR Anual) | nicaragua-corporate-tax.md (if available) |

### Key handoff points

- **Payroll -> Bookkeeping:** Gross wages, employer INSS, and INATEC are expenses; employee INSS and IR withholding are liabilities until remitted.
- **Payroll -> Income Tax:** Annual employment income feeds the employee's IR-106 where a return is required.
- **Payroll -> Social Security:** INSS Regimen Integral contributions count toward pension (IVM) entitlement.

### Reference figures (with provenance)

**Reference figures table**

| Item | Value | Source |
| --- | --- | --- |
| IR exemption (annual) | C$100,000 | Ley 822 Art. 23 / PwC |
| IR top marginal rate | 30% over C$500,000 | Ley 822 / PwC |
| Non-resident IR | 20% definitive | PwC |
| Employee INSS | 7.00% (4.75 IVM + 2.25 health) | 2019 reform / PwC |
| Employer INSS < 50 | 21.5% | 2019 reform / Latin Alliance |
| Employer INSS >= 50 | 22.5% | 2019 reform / Latin Alliance |
| INATEC | 2.0% | INATEC decree |
| INSS ceiling | None (disputed) | 2019 reform — **[RESEARCH GAP]** |
| INSS payment deadline | First 10 business days of following month | INSS Reglamento General |
| IR-106 annual deadline | 90 days after year-end (~31 Mar); TY2025 = 28 Feb 2026 | EY / PwC |
| INSS mora | 2% monthly | INSS Reglamento General |

### Numbered Test Suite (recompute to confirm before relying on this skill)

1. **Bracket boundary @ C$200,000 annual taxable** -> IR = 0 + 15% x 100,000 = **C$15,000**. ✓
2. **Bracket boundary @ C$350,000** -> 15,000 + 20% x 150,000 = **C$45,000**. ✓
3. **Bracket boundary @ C$500,000** -> 45,000 + 25% x 150,000 = **C$82,500**. ✓
4. **Example A net pay** (gross 30,000) -> 30,000 − 2,100 − 3,496.67 = **C$24,403.33**. ✓
5. **Example B net pay** (commerce min 10,913.54) -> 10,913.54 − 763.95 − 272.44 = **C$9,877.15**. ✓
6. **Example C exempt** (8,046) -> annualized taxable 89,793.36 < 100,000 -> IR = **0**; net = **C$7,482.78**. ✓
7. **Example D net pay** (60,000, >=50) -> 60,000 − 4,200 − 11,115 = **C$44,685.00**. ✓
8. **Employer total cost, Example A** -> 30,000 + 6,450 + 600 = **C$37,050.00**. ✓
9. **Employer total cost, Example D** -> 60,000 + 13,500 + 1,200 = **C$74,700.00**. ✓
10. **Employee INSS components** -> 4.75% + 2.25% = **7.00%**. ✓
11. **Employer INSS >= 50 components** -> 13.5 + 6.0 + 1.5 + 1.5 = **22.5%**. ✓
12. **Employer burden < 50** -> 21.5% + 2.0% INATEC = **23.5%**. ✓
13. **Non-resident IR** (Example E, 50,000) -> 50,000 x 20% = **C$10,000**. ✓
14. **Net + deductions = gross** (Example A) -> 24,403.33 + 2,100 + 3,496.67 = **30,000.00**. ✓

## PROHIBITIONS

- NEVER apply the IR table to gross salary — the base is gross minus the 7% employee INSS.
- NEVER skip annualizing monthly taxable income before applying the IR brackets.
- NEVER apply resident brackets to a confirmed non-resident — use the flat 20% definitive withholding.
- NEVER omit the INATEC 2% employer levy.
- NEVER use the same employer INSS rate for all clients — confirm the < 50 vs >= 50 headcount band.
- NEVER deduct INATEC from the employee — it is an employer-only charge.
- NEVER pay a gross below the applicable sector minimum wage.
- NEVER assume a current INSS contribution ceiling — the 2019 reform removed it; the C$130,362.60 figure is unconfirmed.
- NEVER run payroll without confirming the employer's INSS and DGI (RUC) withholding-agent registrations.
- NEVER FX-convert a non-cordoba figure silently — all computation is in NIO/C$.
- NEVER present any computation as definitive — label as ESTIMATED and direct to a licensed Nicaraguan accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed Nicaraguan accountant / Contador Publico Autorizado) before implementation. This is a Tier-2 research-verified skill containing items explicitly flagged **[RESEARCH GAP — reviewer to confirm]**; these must be resolved before the skill is relied upon.

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
