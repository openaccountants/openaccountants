---
name: dominican-republic-payroll
description: Use this skill whenever asked about Dominican Republic payroll processing for employed persons. Trigger on phrases like "Dominican Republic payroll", "nómina República Dominicana", "TSS", "retención ISR nómina", "descuentos de ley RD", "sueldo neto Dominican Republic", "net salary Dominican Republic", "AFP SFS descuento", "regalía pascual", "salario de navidad", "INFOTEP", "salario mínimo RD", "gross to net Dominican Republic", "employer cost Dominican Republic", or any question about computing employee pay, income-tax withholding (retención de ISR), or social-security (TSS) contributions for Dominican Republic-based employees. This skill covers ISR monthly withholding (DGII escala salarial), TSS contributions (AFP, SFS, SRL, INFOTEP), the regalía pascual (13th salary), minimum wage, payslip and monthly filing obligations. ALWAYS read this skill before processing any Dominican Republic payroll.
version: 0.1
jurisdiction: DO
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Miguel Lantigua
review_status: current
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Dominican Republic Payroll

## Dominican Republic Payroll Skill v0.1

Tier 2 — research-verified. Figures sourced from the DGII (escala salarial FY2025), the Tesorería de la Seguridad Social (TSS), PwC Worldwide Tax Summaries (updated 5 Dec 2025), and Dominican payroll references. NOT yet signed off by a licensed Dominican contador. Treat every computation as an estimate pending professional review.

## Section 1 -- Quick Reference

**Quick Reference**

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Dominican Republic |
| Currency | DOP (Dominican peso, RD$) only |
| Standard pay frequency | Monthly (some sectors quincenal) |
| Tax year | Calendar year (1 January -- 31 December) |
| Income-tax withholding | Retención de ISR — annualise the monthly ISR base, apply the annual scale, ÷ 12 |
| Income-tax authority | Dirección General de Impuestos Internos (DGII) |
| Social security | Tesorería de la Seguridad Social (TSS): AFP, SFS, SRL, INFOTEP |
| Validated by | Pending -- requires sign-off by a licensed Dominican contador |
| Skill version | 0.1 |

### The single most important DR payroll fact

- **ISR retención base and annualisation method** — The ISR retención base = gross salary − employee AFP (2.87%) − employee SFS (3.04%). TSS employee contributions are deducted before the income-tax scale is applied. Withholding is computed on the annualised base (× 12), the annual scale applied, then ÷ 12.

## Section 2 -- Social Security Deductions (TSS)

See `dominican-republic-social-contributions.md` for full detail. Payroll summary:

**Social Security Deductions (TSS)**

| Contribution | Employee | Employer | Base ceiling |
| --- | --- | --- | --- |
| AFP — pension | 2.87% | 7.10% | 20× min cotizable wage |
| SFS — health | 3.04% | 7.09% | 10× min cotizable wage |
| SRL — occupational risk | — | ~1.20% | 4× min cotizable wage |
| INFOTEP — training | 0.50% (bonuses only) | 1.00% (payroll) | — |

- **Employee payroll deduction total and minimum cotizable wage** — Employee payroll deduction = 5.91% (AFP + SFS) of salario cotizable, each capped at its own ceiling. Minimum cotizable wage: RD$21,674.80/mo (1 Apr 2025 – 31 Jan 2026) → RD$23,223/mo from 1 Feb 2026.  _(TSS Res. 01-2025)_

## Section 3 -- Income Tax Withholding (Retención de ISR)

- **ISR base calculation method** — Base = gross − employee AFP − employee SFS. Annualise (× 12), apply the scale, divide by 12.

### Annual ISR scale (DGII, FY2025)

**Annual ISR scale (DGII, FY2025)**  _(PwC (updated 5 Dec 2025); DGII escala salarial FY2025)_

| Annual taxable income (RD$) | Tax on lower limit | Rate on excess |
| --- | --- | --- |
| 0 -- 416,220.00 | 0 | 0% (exempt) |
| 416,220.01 -- 624,329.00 | 0 | 15% over 416,220.00 |
| 624,329.01 -- 867,123.00 | RD$31,216 | 20% over 624,329.00 |
| 867,123.01 and above | RD$79,776 | 25% over 867,123.00 |

Source: PwC (updated 5 Dec 2025); DGII escala salarial FY2025. The exempt threshold is inflation-indexed annually (FY2024 was RD$399,923). Withholding begins at ~RD$34,685/month of ISR base (416,220 ÷ 12). [RESEARCH GAP — reviewer to confirm the FY2026 scale before using it for 2026 payrolls.]

## Section 4 -- Worked Examples (gross-to-net, monthly; Apr-2025 ceilings)

### Example 1 — Below the ISR threshold (gross RD$25,000)

AFP employee 2.87% × 25,000 = 717.50; SFS employee 3.04% × 25,000 = 760.00 → TSS = 1,477.50
ISR base = 25,000 − 1,477.50 = 23,522.50 → annualised 282,270 < 416,220 → RD$0 ISR
Net pay = 25,000 − 1,477.50 = RD$23,522.50

### Example 2 — Mid salary (gross RD$50,000)

AFP employee 1,435.00 + SFS employee 1,520.00 = TSS 2,955.00
ISR base = 50,000 − 2,955.00 = 47,045.00 → annualised 564,540 → 15% × (564,540 − 416,220) = 15% × 148,320 = 22,248 annual → ÷ 12 = RD$1,854.00/month
Net pay = 50,000 − 2,955.00 − 1,854.00 = RD$45,191.00
Employer on-cost: AFP 3,550.00 + SFS 3,545.00 + SRL 600.00 + INFOTEP 500.00 = RD$8,195.00 → total cost RD$58,195.00

### Example 3 — High earner (gross RD$300,000)

AFP employee 2.87% × 300,000 = 8,610.00; SFS employee capped at 216,748 → 3.04% × 216,748 = 6,589.14 → TSS = 15,199.14
ISR base = 300,000 − 15,199.14 = 284,800.86 → annualised 3,417,610 → top band: 79,776 + 25% × (3,417,610 − 867,123) = 79,776 + 637,621.75 = 717,397.75 annual → ÷ 12 = RD$59,783.15/month
Net pay = 300,000 − 15,199.14 − 59,783.15 = RD$224,017.71

## Section 5 -- Regalía Pascual (13th salary) & Minimum Wage

### Regalía Pascual (salario de navidad) — mandatory

- **Regalía pascual calculation and treatment** — = 1/12 of the ordinary salary earned in the calendar year, paid by 20 December. Exempt from ISR and from AFP/SFS; INFOTEP employee 0.5% applies to it.  _(Código de Trabajo art. 219)_

### Minimum Wage

Set by sector and employer size by the Comité Nacional de Salarios (CNS) — non-sectorised private wages depend on the company's size band. [RESEARCH GAP — reviewer to confirm the current CNS minimum-wage schedule by sector/size.]

## Section 6 -- Payslip & Filing Obligations

**Payslip & Filing Obligations**

| Obligation | Channel | Deadline |
| --- | --- | --- |
| TSS contributions (AFP+SFS+SRL+INFOTEP) | TSS platform (SUIR+) | First working days of the following month |
| ISR retención on salaries | DGII — **IR-3** (monthly withholding declaration) | By the 10th of the following month |
| Annual reconciliation of withholdings | DGII — **IR-13** / annual report | Per DGII calendar |

The payslip (volante de pago) must show gross salary, AFP and SFS employee deductions, ISR retención, other authorised deductions, and net pay. [RESEARCH GAP — reviewer to confirm current form numbers/deadlines against DGII.]

## Section 7 -- Common Payroll Patterns

**Common Payroll Patterns**

| Pattern | Classification |
| --- | --- |
| NÓMINA, PAGO SUELDO, ABONO NÓMINA | Net salary disbursement |
| TSS, AFP, SFS, ARS, INFOTEP | TSS social-security remittance |
| DGII, ISR, IR-3, RETENCIÓN | ISR withholding to DGII |
| REGALÍA, SALARIO NAVIDAD | 13th salary (Dec, ISR-exempt) |

## Section 8 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill |
| --- | --- |
| Employee payroll (this skill) | **dominican-republic-payroll.md** |
| Self-employed / individual income tax (IR-1) | dominican-republic-income-tax.md |
| TSS contribution rates & ceilings detail | dominican-republic-social-contributions.md |
| Dominican ITBIS (18% VAT) | dominican-republic-itbis (consumption tax) |

## PROHIBITIONS

- **Never apply ISR scale to gross** — NEVER apply the ISR scale to gross — the base is gross − employee AFP − employee SFS.
- **Never compute monthly ISR by monthly bracket lookup** — NEVER compute monthly ISR by a monthly bracket lookup — annualise the base, apply the annual scale, then ÷ 12.
- **Never apply one ceiling to all TSS funds** — NEVER apply one ceiling to all TSS funds — AFP (20×), SFS (10×), SRL (4×) each cap separately.
- **Never withhold ISR on regalía pascual** — NEVER withhold ISR on the regalía pascual — it is exempt.
- **Never charge employees SRL** — NEVER charge employees SRL — it is employer-only.
- **Never present computations as definitive** — NEVER present payroll computations as definitive — label as estimated and direct to a licensed Dominican contador.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed contador in the Dominican Republic) before filing or acting upon.

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
