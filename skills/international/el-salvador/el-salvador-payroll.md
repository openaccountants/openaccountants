---
name: el-salvador-payroll
description: Use this skill whenever asked about El Salvador payroll processing for employed persons. Trigger on phrases like "El Salvador payroll", "planilla El Salvador", "ISSS", "AFP Crecer", "AFP Confía", "retención de renta", "ISR planilla", "descuentos de ley", "sueldo neto El Salvador", "net salary El Salvador", "aguinaldo", "INSAFORP", "salario mínimo El Salvador", "gross to net El Salvador", "employer cost El Salvador", "cotización ISSS AFP", or any question about computing employee pay, income-tax withholding (retención), or social-security/pension contributions for El Salvador-based employees. This skill covers ISR monthly withholding (Decreto Ejecutivo 10, in force 8 May 2025), ISSS health contributions (employee + employer, $1,000 base cap), AFP pension contributions, the INSAFORP training levy, minimum wage, the mandatory aguinaldo (Christmas bonus), vacation, payslip and monthly filing obligations. ALWAYS read this skill before processing any El Salvador payroll.
version: 0.1
jurisdiction: SV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# El Salvador Payroll

## El Salvador Payroll Skill v0.1

**Tier 2 — research-verified. Figures sourced from the Ministerio de Hacienda (Decreto Ejecutivo 10, 2025), ISSS, the Superintendencia del Sistema Financiero (AFP), PwC Worldwide Tax Summaries, and Salvadoran payroll references. NOT yet signed off by a licensed Salvadoran contador. Treat every computation as an estimate pending professional review.**

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Republic of El Salvador |
| Currency | USD only (US dollar is legal tender; the colón is retired) |
| Standard pay frequency | Monthly (quincenal — twice-monthly — is also common) |
| Tax year | Calendar year (1 January -- 31 December) |
| Income-tax withholding | Retención de ISR — monthly table, applied to salary **net of AFP and ISSS** |
| Income-tax authority | Ministerio de Hacienda — Dirección General de Impuestos Internos (DGII) |
| Health / maternity social security | Instituto Salvadoreño del Seguro Social (ISSS) |
| Pension | AFP (private — AFP Crecer, AFP Confía), overseen by the Superintendencia del Sistema Financiero (SSF) |
| Training levy | INSAFORP (Instituto Salvadoreño de Formación Profesional) — employer 1% |
| Key legislation | Ley de Impuesto sobre la Renta; Decreto Ejecutivo 10 (2025) retención tables; Ley del Seguro Social; Ley del Sistema de Ahorro para Pensiones (SAP); Código de Trabajo |
| Validated by | Pending -- requires sign-off by a licensed Salvadoran contador / abogado laboral |
| Skill version | 0.1 |

### The single most important El Salvador payroll fact

- **ISR base calculation rule** — The ISR retención table is applied to the salary AFTER deducting the employee's ISSS and AFP contributions (those are renta no gravada). Base = gross − ISSS(employee) − AFP(employee). Applying the table to gross over-withholds.  _(Ministerio de Hacienda; SalarioSV; HazConta)_

## Section 2 -- Income Tax Withholding (Retención de ISR)

- **ISR withholding base rule** — The employer withholds ISR monthly. Base = gross salary − employee ISSS − employee AFP. Apply the monthly table below to that base.

### Monthly retención table (Decreto Ejecutivo 10, in force 8 May 2025)

**Monthly retención table**  _(Ministerio de Hacienda, Decreto Ejecutivo No. 10 (30 Apr 2025), in force 8 May 2025)_

| Tramo | Monthly base (gross − AFP − ISSS), USD | Withholding |
| --- | --- | --- |
| I | 0.01 -- 550.00 | Nil (exempt) |
| II | 550.01 -- 895.24 | USD 17.67 + 10% on excess over 550.00 |
| III | 895.25 -- 2,038.10 | USD 60.00 + 20% on excess over 895.24 |
| IV | 2,038.11 and over | USD 288.57 + 30% on excess over 2,038.10 |

Source: Ministerio de Hacienda, Decreto Ejecutivo No. 10 (30 Apr 2025), in force 8 May 2025; the reform raised the monthly exempt amount from USD 472 (unchanged since 2011) to USD 550. (Diario El Mundo; Contaportable)

> Note. The cuotas fijas (17.67 / 60.00 / 288.57) mirror the annual Art. 37 table ÷ 12 (annual 212.12 / 720.00 / 3,462.86). There is a small step at the $895.24 boundary (the 10% progression reaches 52.19 vs the $60.00 band-3 base). This is the official table, not an error.

## Section 3 -- Social Security — ISSS (Health & Maternity)

ISSS covers health, maternity, and work-risk benefits. Contributions are computed on a salary base capped at USD 1,000/month.

**ISSS contributions table**  _(ISSS; PwC)_

| Contribution | Rate | Capped base | Maximum / month |
| --- | --- | --- | --- |
| ISSS — employee | 3% | USD 1,000 | USD 30.00 |
| ISSS — employer | 7.5% | USD 1,000 | USD 75.00 |

- **ISSS cap rule** — Salary above USD 1,000 does NOT increase the ISSS contribution — both sides are frozen at USD 30 / USD 75.  _(ISSS; PwC)_

## Section 4 -- Pension — AFP (Sistema de Ahorro para Pensiones)

Pension contributions go to the employee's chosen AFP (Crecer or Confía). The contributory-base salary cap was eliminated from January 2023 — AFP applies to the full salary with no maximum.

**AFP contributions table**  _(SSF; Ley SAP; PwC)_

| Contribution | Rate | Cap |
| --- | --- | --- |
| AFP — employee | 7.25% | None (cap removed Jan 2023) |
| AFP — employer | 8.75% | None |
| **Total AFP** | **16.00%** | None |

- **AFP employee rate composition** — The 7.25% employee rate already includes the AFP commission and disability/survivor insurance premium.  _(SSF; Ley SAP; PwC)_

## Section 5 -- Employer On-Costs (full picture)

**Employer on-costs table**

| Employer contribution | Rate | Base / cap | On gross USD 1,000 |
| --- | --- | --- | --- |
| ISSS (employer) | 7.5% | capped at USD 1,000 | USD 75.00 |
| AFP (employer) | 8.75% | uncapped | USD 87.50 |
| INSAFORP (training levy) | 1% | total payroll (employers with ≥ 1 worker subject; small-employer thresholds apply) | USD 10.00 |
| **Total employer on-cost** | **~17.25%** (at/below the ISSS cap) |  | **USD 172.50** |

**Total employer cost** of a USD 1,000 employee ≈ USD 1,172.50/month (before aguinaldo and vacation accruals). [INSAFORP threshold — **RESEARCH GAP — reviewer to confirm the current small-employer exemption.**]

### Minimum Wage (2025)

**Minimum wage table**  _(Ministerio de Trabajo)_

| Sector | Monthly (USD) |
| --- | --- |
| Commerce & services | 408.80 |
| Industry / manufacturing | 408.80 |
| Textile / apparel (maquila) | 359.16 |
| Agriculture | 272.66 |

Minimum wages are set by sector by the Consejo Nacional del Salario Mínimo. **[RESEARCH GAP — reviewer to confirm the current sector schedule and any 2026 revision.]** (Ministerio de Trabajo)

### Aguinaldo (Christmas Bonus) — mandatory

- **Aguinaldo payment window** — Paid between 12 and 20 December, scaled by completed years of service.  _(Código de Trabajo arts. 196–202)_

**Aguinaldo scale table**  _(Código de Trabajo arts. 196–202)_

| Service | Aguinaldo |
| --- | --- |
| 1 -- < 3 years | 15 days' salary |
| 3 -- < 10 years | 19 days' salary |
| 10+ years | 21 days' salary |

- **Aguinaldo ISR exemption** — Aguinaldo is exempt from ISR up to a statutory limit (two minimum monthly wages of the commerce sector); the excess is taxable. **[RESEARCH GAP — reviewer to confirm the current exempt limit.]**  _(Código de Trabajo arts. 196–202)_

### Vacation

- **Vacation entitlement** — 15 days after each completed year of service, plus a 30% vacation premium (prima vacacional) on the corresponding salary.  _(Código de Trabajo art. 177)_

### Example 1 — Minimum-wage employee (gross USD 408.80)

- ISSS employee: 3% × 408.80 = **USD 12.26**
- AFP employee: 7.25% × 408.80 = **USD 29.64**
- ISR base = 408.80 − 12.26 − 29.64 = **366.90** ≤ 550 → **USD 0.00 retención**
- **Net pay = 408.80 − 12.26 − 29.64 = USD 366.90**

### Example 2 — Mid salary (gross USD 1,000)

- ISSS employee: 3% × min(1,000, 1,000 cap) = **USD 30.00**
- AFP employee: 7.25% × 1,000 = **USD 72.50**
- ISR base = 1,000 − 30.00 − 72.50 = **897.50** → Tramo III: 60.00 + 20% × (897.50 − 895.24) = 60.00 + 0.45 = **USD 60.45**
- **Net pay = 1,000 − 30.00 − 72.50 − 60.45 = USD 837.05**
- Employer on-cost: ISSS 75.00 + AFP 87.50 + INSAFORP 10.00 = **USD 172.50** → total cost **USD 1,172.50**

### Example 3 — High earner (gross USD 2,500)

- ISSS employee: capped → **USD 30.00** (base frozen at USD 1,000)
- AFP employee: 7.25% × 2,500 = **USD 181.25** (no cap)
- ISR base = 2,500 − 30.00 − 181.25 = **2,288.75** → Tramo IV: 288.57 + 30% × (2,288.75 − 2,038.10) = 288.57 + 75.20 = **USD 363.77**
- **Net pay = 2,500 − 30.00 − 181.25 − 363.77 = USD 1,924.98**

## Section 8 -- Payslip Requirements

- **Payslip requirements** — The employer must issue a payslip (boleta de pago / comprobante) showing: gross salary, ISSS employee deduction, AFP employee deduction, ISR retención, any other authorised deductions, and net pay. Records are retained for inspection by the Ministerio de Trabajo and DGII.

## Section 9 -- Filing & Payment Obligations

**Filing & payment obligations table**

| Obligation | Form / channel | Deadline |
| --- | --- | --- |
| ISR retención (monthly) | DGII — declaración mensual de pago a cuenta e impuesto retenido (**F-14**) | Within 10 working days of month-end |
| Annual statement of withholdings | DGII — informe anual de retenciones (**F-910**) | 31 January (following year) |
| ISSS planilla (monthly) | ISSS portal (SEPS) | Per ISSS calendar (monthly) |
| AFP planilla (monthly) | AFP / SSF electronic planilla | Monthly |

**[RESEARCH GAP — reviewer to confirm the exact current form numbers and deadlines against the DGII and ISSS portals.]**

## Section 10 -- Common Payroll Patterns (bank statement / accounting)

**Common payroll patterns table**

| Pattern | Classification |
| --- | --- |
| PLANILLA, NÓMINA, PAGO SALARIO, ABONO NÓMINA | Net salary disbursement |
| ISSS, SEGURO SOCIAL | ISSS remittance (employer + employee health) |
| AFP CRECER, AFP CONFÍA, PENSIÓN | AFP pension remittance |
| DGII, HACIENDA, PAGO A CUENTA, RETENCIÓN | ISR retención / pago a cuenta to Hacienda |
| INSAFORP | Training levy (employer 1%) |
| AGUINALDO | Mandatory Christmas bonus (Dec) |

## Section 11 -- Interaction with Other Skills

**Interaction with other skills table**

| Scenario | Skill |
| --- | --- |
| Employee payroll (this skill) | **el-salvador-payroll.md** |
| Self-employed / individual income tax (F-11, Art. 37 annual table) | el-salvador-income-tax.md |
| Employer & self-insured social/pension rates, annual PIT table | el-salvador-social-contributions.md |
| El Salvador IVA (13%) | el-salvador-vat (consumption tax) |

**Handoff:** the employee FS-equivalent annual figures (gross, ISR withheld, ISSS, AFP) feed the individual's annual ISR settlement on Form F-11 if the employee has other income or claims a refund.

## PROHIBITIONS

- **Prohibition 1** — NEVER apply the ISR retención table to gross salary — the base is gross − ISSS − AFP (employee).
- **Prohibition 2** — NEVER compute ISSS on salary above USD 1,000 — both employee (USD 30) and employer (USD 75) are capped at the USD 1,000 base.
- **Prohibition 3** — NEVER cap AFP — the contributory-base ceiling was removed in January 2023; AFP applies to the full salary.
- **Prohibition 4** — NEVER omit the employer INSAFORP 1% training levy from the true employer cost.
- **Prohibition 5** — NEVER omit the mandatory aguinaldo (Dec) or the 30% vacation premium from annual labour cost.
- **Prohibition 6** — NEVER treat the USD 550 monthly exemption as USD 472 — that pre-2025 figure was superseded by Decreto Ejecutivo 10.
- **Prohibition 7** — NEVER present payroll computations as definitive — always label as estimated and direct to a licensed Salvadoran contador.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed contador or abogado in El Salvador) before filing or acting upon.

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
