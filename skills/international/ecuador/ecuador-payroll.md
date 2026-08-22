---
name: ecuador-payroll
description: Use this skill whenever asked about Ecuador payroll processing for employed persons (relación de dependencia). Trigger on phrases like "Ecuador payroll", "rol de pagos", "aporte IESS", "aporte personal 9.45%", "aporte patronal 11.15%", "retención impuesto a la renta en relación de dependencia", "proyección anual", "décimo tercero", "décimo cuarto", "fondos de reserva", "sueldo neto Ecuador", "net salary Ecuador", "salario básico unificado", "SBU", "gross to net Ecuador", "employer cost Ecuador", or any question about computing employee pay, income-tax withholding, IESS contributions, or mandatory bonuses for Ecuador-based employees. This skill covers IESS personal and patronal contributions, the annual income-tax projection-and-withholding method, the personal-expense rebate, the 13th and 14th salaries, fondos de reserva, the SBU, payslip and filing obligations. ALWAYS read this skill before processing any Ecuador payroll.
version: 0.1
jurisdiction: EC
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ecuador Payroll

## Ecuador Payroll Skill v0.1

Tier 2 — research-verified. Figures sourced from the SRI (Servicio de Rentas Internas), IESS, the Código del Trabajo, PwC Worldwide Tax Summaries, and Ecuadorian payroll references. NOT yet signed off by a licensed Ecuadorian contador. Treat every computation as an estimate pending professional review.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Ecuador |
| Currency | USD only (US dollar is legal tender since 2000) |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Income-tax withholding | Retención en relación de dependencia — annual projection method (project, apply table, ÷ 12) |
| Income-tax authority | Servicio de Rentas Internas (SRI) |
| Social security | Instituto Ecuatoriano de Seguridad Social (IESS) |
| Key legislation | Ley de Régimen Tributario Interno (LRTI); Código del Trabajo; Ley de Seguridad Social |
| SBU (salario básico unificado), 2025 | USD 470/month (2026: USD 482) |
| Validated by | Pending -- requires sign-off by a licensed Ecuadorian contador |
| Skill version | 0.1 |

### Two facts that govern Ecuador payroll

1. **IESS personal contribution (9.45%) is deducted before computing income-tax withholding**, and income tax uses an **annual projection** (not a monthly bracket lookup).
2. **Décimo tercero, décimo cuarto and fondos de reserva are EXEMPT** from both IESS contributions and income tax — never include them in the IESS base or the IR projection.

## Section 2 -- Social Security (IESS)

- **IESS contribution base** — IESS contributions are computed on the materia gravada (salary + habitual remuneration: commissions, overtime, etc.). Floor = 1 SBU. No upper ceiling.  _(IESS Tasas de Aportación (as reported by EcuadorLegalOnline; misalario.ec))_

**IESS contribution rates**  _(IESS Tasas de Aportación (as reported by EcuadorLegalOnline; misalario.ec))_

| Contribution | Rate (private sector) |
| --- | --- |
| Aporte personal (employee) | 9.45% |
| Aporte patronal (employer) | 11.15% |
| Combined reference | 20.60% |

[RESEARCH GAP — the IESS official rate PDF was not machine-readable; the 9.45% / 11.15% rates and the fund-by-fund split (IVM / salud / riesgos / cesantía) rely on secondary sources — reviewer to confirm against the IESS document.]

## Section 3 -- Income Tax Withholding (Retención en relación de dependencia)

- **Annual projection withholding method** — 1. Project annual taxable income = (monthly salary × 12) + projected taxable extras − annual IESS personal (9.45%). Exclude décimos and fondos de reserva (exempt). 2. Subtract allowable items and apply the rebaja por gastos personales (personal-expense tax credit, based on family burdens / cargas familiares). 3. Apply the annual IR table below to get annual tax. 4. Monthly withholding = annual tax ÷ 12 (re-projected if pay changes).  _(LRTI art. 36)_

### Annual IR table — 2025 (LRTI art. 36; indexed annually to urban CPI)

**Annual IR table — 2025**  _(LRTI art. 36; indexed annually to urban CPI)_

| Taxable income from (USD) | up to (USD) | Tax on base | % on excess |
| --- | --- | --- | --- |
| 0 | 12,081 | 0 | 0% |
| 12,081 | 15,387 | 0 | 5% |
| 15,387 | 19,978 | 165 | 10% |
| 19,978 | 26,422 | 624 | 12% |
| 26,422 | 34,770 | 1,398 | 15% |
| 34,770 | 46,089 | 2,650 | 20% |
| 46,089 | 61,359 | 4,914 | 25% |
| 61,359 | 81,817 | 8,731 | 30% |
| 81,817 | 108,810 | 14,869 | 35% |
| 108,810 | + | 24,316 | 37% |

- **2026 update and non-resident rate** — 2026: exempt base rises to USD 12,208 (SRI Resolution NAC-DGERCGC25-00000043). Use the 2026 table from ecuador-income-tax.md for 2026 payrolls. Non-residents: flat 25%, no brackets, no allowance.  _(SRI Resolution NAC-DGERCGC25-00000043)_

The personal-expense rebate (rebaja) reduces the computed tax and is reported by the employee on Form SRI-GP. The worked examples below show tax before the rebate; the rebate lowers the withholding. [RESEARCH GAP — reviewer to apply the current gastos-personales rebate cap by number of cargas familiares.]

## Section 4 -- Mandatory Bonuses & Reserve Fund

**Mandatory bonuses & reserve fund**  _(Código del Trabajo; IESS)_

| Benefit | Amount | Timing | IESS / IR? |
| --- | --- | --- | --- |
| Décimo tercero (13th salary) | 1/12 of remuneration earned 1 Dec–30 Nov | Paid by 24 December (or monthly if elected) | Exempt from both |
| Décimo cuarto (14th salary) | 1 SBU (USD 470 in 2025) | Sierra/Amazonía by 15 Aug; Costa/Insular by 15 Mar | Exempt from both |
| Fondos de reserva | 8.33% of remuneration | From the 13th month of employment; paid monthly to IESS or accrued | Exempt from both |

- **Exclusion from IESS base and IR projection** — Do NOT add these to the IESS base or to the IR projection.  _(Código del Trabajo; IESS)_

### Example 1 — SBU earner (gross USD 470)

IESS personal: 9.45% × 470 = USD 44.42
IR projection: (470 × 12) − (44.42 × 12) = 5,640 − 533 = 5,107 < 12,081 → 0% → USD 0.00/month
Net pay = 470 − 44.42 = USD 425.58 (plus décimo tercero, décimo cuarto and fondos de reserva accruing separately)

### Example 2 — Mid salary (gross USD 1,000)

IESS personal: 9.45% × 1,000 = USD 94.50
IR projection: (1,000 × 12) − (94.50 × 12) = 12,000 − 1,134 = 10,866 < 12,081 → 0% → USD 0.00/month
Net pay = 1,000 − 94.50 = USD 905.50

### Example 3 — Higher earner (gross USD 2,500)

IESS personal: 9.45% × 2,500 = USD 236.25
IR projection: (2,500 × 12) − (236.25 × 12) = 30,000 − 2,835 = 27,165; falls in the 26,422–34,770 band → annual tax = 1,398 + 15% × (27,165 − 26,422) = 1,398 + 111.45 = USD 1,509.45 (before the gastos-personales rebate)
Monthly withholding = 1,509.45 ÷ 12 = USD 125.79 (before rebate; the rebate lowers it)
Net pay (before rebate) = 2,500 − 236.25 − 125.79 = USD 2,137.96
Employer cost: IESS patronal 11.15% × 2,500 = USD 278.75 (plus accruals for décimos and fondos de reserva)

## Section 6 -- Payslip (Rol de Pagos)

The rol de pagos must show: gross salary and habitual remuneration, IESS aporte personal (9.45%), IR retención, any other authorised deductions, net pay, and the employer-side IESS aporte patronal and benefit accruals. Employees access contribution history via the IESS portal.

## Section 7 -- Filing & Payment Obligations

**Filing & payment obligations**

| Obligation | Channel | Deadline |
| --- | --- | --- |
| IESS planilla (aportes) | IESS online system | Within 15 days of month-end |
| IR retención en relación de dependencia | SRI — monthly Formulario 103 | Per the 9th-digit (noveno dígito) calendar |
| Annual employee withholding certificate | SRI Form 107 to each employee | By end of January (following year) |
| Décimo tercero / décimo cuarto reports | Ministerio del Trabajo (SUT) | After each payment deadline |

[RESEARCH GAP — reviewer to confirm current form numbers and the noveno-dígito due dates.]

## Section 8 -- Common Payroll Patterns

**Common payroll patterns**

| Pattern | Classification |
| --- | --- |
| ROL DE PAGOS, SUELDO, NÓMINA, ABONO SUELDO | Net salary disbursement |
| IESS, APORTE IESS, PLANILLA IESS | IESS remittance (personal + patronal) |
| SRI, RETENCIÓN RENTA, FORM 103 | IR withholding to the SRI |
| DÉCIMO TERCERO, DÉCIMO CUARTO | Mandatory 13th / 14th salaries (exempt) |
| FONDOS DE RESERVA | 8.33% reserve fund (exempt) |

## Section 9 -- Interaction with Other Skills

**Interaction with other skills**

| Scenario | Skill |
| --- | --- |
| Employee payroll (this skill) | **ecuador-payroll.md** |
| Self-employed / individual income tax (Formulario 102/102A, RIMPE, gastos personales) | ecuador-income-tax.md |
| Employer & self-employed IESS rates | ecuador-social-contributions.md |
| Ecuador IVA (15%) | ecuador-iva (consumption tax) |

Handoff: the SRI Form 107 (annual withholding certificate) feeds the employee's personal income-tax return (Form 102A) where they have other income or claim the gastos-personales rebate.

## PROHIBITIONS

- NEVER use a monthly IR bracket lookup — Ecuador withholds by ANNUAL projection (project, apply the annual table, divide by 12).
- NEVER include décimo tercero, décimo cuarto, or fondos de reserva in the IESS base or the IR projection — all three are exempt.
- NEVER cap IESS — there is no upper salary ceiling (floor is 1 SBU).
- NEVER ignore the gastos-personales rebate — it reduces the employee's withholding.
- NEVER apply IESS at less than 1 SBU for a full-time worker.
- NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Ecuadorian contador.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed contador in Ecuador) before filing or acting upon.

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
