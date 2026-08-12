---
name: spain-payroll
description: Use this skill whenever asked about Spanish payroll processing for employees. Trigger on phrases like "Spanish payroll", "nómina España", "IRPF retención", "retenciones nómina", "Seguridad Social cotización", "contingencias comunes", "base de cotización", "Salario Mínimo Interprofesional", "SMI", "paga extra", "tredicesima España", "Agencia Tributaria retención", "modelo 111", "modelo 190", "Sistema RED", "Siltra", "TC1 TC2", "RLC RNT", "MEI cotización", "cuota solidaridad", "bruto neto España", "despido indemnización", "FOGASA", or any question about computing employee pay, income tax withholding, or social security contributions in Spain. This skill covers IRPF withholding, Seguridad Social contributions (employee and employer), mandatory benefits, nómina (payslip) requirements, filing obligations, and employer cost analysis. ALWAYS read this skill before processing any Spanish employee payroll.
version: 1.0
jurisdiction: ES
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Payroll

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Currency | EUR only |
| Standard pay frequency | Monthly (mensual) -- paid in 12 + 2 pagas extraordinarias (14 payments typical) |
| Tax year | Calendar year (1 January -- 31 December) |
| Income tax withholding | IRPF retención (progressive, computed via AEAT algorithm) |
| Social insurance authority | Tesorería General de la Seguridad Social (TGSS) |
| Tax authority | Agencia Estatal de Administración Tributaria (AEAT) |
| Key legislation | Ley 35/2006 (LIRPF); Real Decreto Legislativo 8/2015 (LGSS); Real Decreto 126/2026 (SMI 2026); Orden PJC/297/2026 (cotización 2026); Estatuto de los Trabajadores (RDL 2/2015) |
| Maximum contribution base (2026) | EUR 5,101.20/month |
| AEAT withholding algorithm | ALGORITMO_2026 (published by Sede AEAT) |
| Validated by | Pending -- requires sign-off by a Spanish asesor fiscal / gestor |
| Skill version | 1.0 |

## Section 2 -- Income Tax Withholding (IRPF Retención)

The employer computes the IRPF withholding rate using the official AEAT algorithm (ALGORITMO_2026). The rate is personalised based on the employee's annual gross remuneration, family situation, and deductions.

### IRPF Tax Brackets (2026 -- State + General Autonomous Community)

**IRPF Tax Brackets (2026 -- State + General Autonomous Community)**

| Taxable Income (EUR, annual) | Combined Rate (State + Regional) |
| --- | --- |
| 0 -- 12,450 | 19% |
| 12,451 -- 20,200 | 24% |
| 20,201 -- 35,200 | 30% |
| 35,201 -- 60,000 | 37% |
| 60,001 -- 300,000 | 45% |
| 300,001+ | 47% |

Rates shown are state + general regional tariff. Autonomous Communities (Comunidades Autónomas) may adjust their half of the rate, creating variations.

### Key IRPF Parameters

**Key IRPF Parameters**

| Parameter | Detail |
| --- | --- |
| Minimum personal allowance (mínimo del contribuyente) | EUR 5,550 per taxpayer |
| Per-child allowance | EUR 2,400 (1st), EUR 2,700 (2nd), EUR 4,000 (3rd), EUR 4,500 (4th+) |
| Reduction for employment income (rendimientos del trabajo) | Progressive reduction for income below ~EUR 19,747 |
| Minimum withholding rate | 2% (general); 0% for SMI-level earnings |
| Special contracts minimum | 6% (relaciones laborales especiales de carácter dependiente) |

### SMI and IRPF Exemption

Employees earning the SMI (EUR 17,094/year gross in 14 payments) are generally exempt from IRPF withholding, as the algorithm produces a 0% rate after applying the reducción por rendimientos del trabajo and personal minimum.

## Section 3 -- Social Security -- Employee Deductions (2026)

### Contribution Rates (Régimen General -- Employee Share)

**Contribution Rates (Régimen General -- Employee Share)**

| Concept | Employee Rate | Base |
| --- | --- | --- |
| Contingencias comunes | 4.70% | Base de cotización (min EUR 1,424.40 -- max EUR 5,101.20/month) |
| Desempleo (unemployment) -- indefinido | 1.55% | Base de cotización |
| Desempleo -- temporal (fixed-term) | 1.60% | Base de cotización |
| Formación profesional | 0.10% | Base de cotización |
| MEI (Mecanismo de Equidad Intergeneracional) | 0.15% | Base de cotización |
| **Total employee (indefinido)** | **6.50%** |  |
| **Total employee (temporal)** | **6.55%** |  |

### Cotización Adicional de Solidaridad (2026)

**Cotización Adicional de Solidaridad (2026)**

| Tier | Excess Range | Total Rate | Employee Share | Employer Share |
| --- | --- | --- | --- | --- |
| 1st | EUR 5,101.21 -- EUR 5,611.32 | 1.15% | 0.19% | 0.96% |
| 2nd | EUR 5,611.33 -- EUR 7,651.80 | 1.25% | 0.21% | 1.04% |
| 3rd | Above EUR 7,651.80 | 1.46% | 0.24% | 1.22% |

For employees earning above the maximum base (EUR 5,101.20/month), a solidarity surcharge applies to the excess:

These rates increase annually until 2045.

### Bases de Cotización (2026)

**Bases de Cotización (2026)**

| Group | Category | Minimum (EUR/month) | Maximum (EUR/month) |
| --- | --- | --- | --- |
| 1 | Ingenieros y Licenciados | 1,989.30 | 5,101.20 |
| 2 | Ingenieros Técnicos, Peritos | 1,649.70 | 5,101.20 |
| 3 | Jefes Administrativos y de Taller | 1,435.20 | 5,101.20 |
| 4--7 | All other categories | 1,424.40 | 5,101.20 |

The minimum base for groups 4--7 equals the SMI + 1/6 (prorrata pagas extras).

## Section 4 -- Social Security -- Employer Contributions (2026)

### Contribution Rates (Régimen General -- Employer Share)

**Contribution Rates (Régimen General -- Employer Share)**

| Concept | Employer Rate | Base |
| --- | --- | --- |
| Contingencias comunes | 23.60% | Base de cotización |
| Desempleo -- indefinido | 5.50% | Base de cotización |
| Desempleo -- temporal | 6.70% | Base de cotización |
| FOGASA (Fondo de Garantía Salarial) | 0.20% | Base de cotización |
| Formación profesional | 0.60% | Base de cotización |
| MEI | 0.75% | Base de cotización |
| Contingencias profesionales (AT/EP) | Variable (0.90% -- 7.15%+) | Base de cotización |
| **Total employer (indefinido, excluding AT/EP)** | **~30.65%** |  |

### Typical Total Employer Cost (including AT/EP)

**Typical Total Employer Cost (including AT/EP)**

| Scenario | Approximate Employer Rate |
| --- | --- |
| Office worker (AT/EP ~1.50%) | ~32.15% |
| Construction worker (AT/EP ~6.70%) | ~37.35% |
| Retail employee (AT/EP ~1.00%) | ~31.65% |

### Solidarity Surcharge -- Employer Share (2026)

See Section 3 above. The employer bears 83.39% of each solidarity tier.

## Section 5 -- Minimum Wage and Overtime

### Salario Mínimo Interprofesional (SMI 2026)

**Salario Mínimo Interprofesional (SMI 2026)**

| Item | Value |
| --- | --- |
| Monthly (14 payments) | EUR 1,221 |
| Monthly (12 payments, prorrateado) | EUR 1,424.50 |
| Daily | EUR 40.70 |
| Annual gross | EUR 17,094 |
| Effective | 1 January -- 31 December 2026 |
| Change vs 2025 | +3.1% (+EUR 37/month) |
| Legal basis | Real Decreto 126/2026, 18 February |

The SMI refers to cash remuneration only -- in-kind benefits cannot reduce it.

### Working Hours and Overtime

**Working Hours and Overtime**

| Rule | Detail |
| --- | --- |
| Maximum annual hours | 1,826.27 hours (40 hours/week equivalent, per Estatuto de los Trabajadores Art. 34) |
| Maximum weekly hours | 40 hours average over annual period |
| Maximum daily hours | 9 hours (unless collective agreement provides otherwise; minimum 12 hours between shifts) |
| Overtime limit | 80 hours per year (Art. 35.2 ET); excludes overtime compensated with rest |
| Overtime surcharge | Minimum: same hourly rate (no mandatory premium unless by collective agreement) |
| Typical collective agreement surcharges | 25%--75% depending on day/time; night: 25%+ |
| Compensatory rest | Employer may compensate overtime with equivalent rest within 4 months instead of payment |

## Section 6 -- Mandatory Benefits

### Pagas Extraordinarias (Extra Payments)

**Pagas Extraordinarias (Extra Payments)**

| Entitlement | Detail |
| --- | --- |
| Number | 2 per year (minimum per Art. 31 ET) |
| Amount | Typically 1 month's base salary each (per CCNL) |
| Timing | Usually June and December; may be prorated into 12 monthly payments by agreement |
| Subject to SS and IRPF | Yes -- included in base de cotización when prorated; separate calculation when paid as lump sum |

### Vacaciones (Annual Leave)

**Vacaciones (Annual Leave)**

| Entitlement | Detail |
| --- | --- |
| Statutory minimum | 30 calendar days per year (Art. 38 ET) = approximately 22 working days |
| Non-substitutable | Cannot be replaced with monetary compensation except on termination |
| Carry-over | Must be taken within the calendar year (limited flexibility) |
| Public holidays | 14 days per year (national + regional + local) |

### Incapacidad Temporal (Sick Leave)

**Incapacidad Temporal (Sick Leave)**

| Period | Who Pays | Rate |
| --- | --- | --- |
| Days 1--3 | Employer (if collective agreement provides; otherwise unpaid) | Per agreement |
| Days 4--15 | Employer | 60% of base reguladora |
| Days 16--20 | INSS (via employer advance) | 60% of base reguladora |
| Day 21 onward | INSS (via employer advance) | 75% of base reguladora |
| Maximum | 365 days + 180-day extension |  |

Many collective agreements improve these percentages (often 100% from day 1).

### Maternidad (Maternity Leave)

**Maternidad (Maternity Leave)**

| Entitlement | Detail |
| --- | --- |
| Duration | 16 weeks (6 mandatory post-birth; remaining flexible) |
| Pay | 100% of base reguladora from INSS |
| Multiple births | +2 weeks per additional child |

### Paternidad (Paternity Leave)

**Paternidad (Paternity Leave)**

| Entitlement | Detail |
| --- | --- |
| Duration | 16 weeks (equal to maternity since 2021) |
| Pay | 100% of base reguladora from INSS |
| Mandatory | First 6 weeks must be taken immediately and full-time |

### Severance (Indemnización por Despido)

**Severance (Indemnización por Despido)**

| Type | Compensation |
| --- | --- |
| Despido improcedente (unfair dismissal) | 33 days per year worked, max 24 months' salary |
| Despido objetivo (objective dismissal) | 20 days per year worked, max 12 months' salary |
| FOGASA | Guarantees payment of unpaid wages and severance if employer is insolvent |

## Section 7 -- Payslip Requirements

The nómina must comply with the official model established by Orden ESS/2098/2014 (updated periodically).

### Mandatory Payslip Fields

**Mandatory Payslip Fields**

| Section | Required Fields |
| --- | --- |
| Header | Employer: name, CIF, domicilio, código de cuenta de cotización (CCC), sector CNAE |
| Employee | Name, NIF/NIE, número de afiliación SS, grupo de cotización, categoría profesional, fecha de antigüedad |
| Period | Month and year, total days worked |
| Devengos (earnings) | Percepciones salariales: salario base, complementos salariales, horas extraordinarias, gratificaciones extraordinarias, salario en especie |
|  | Percepciones no salariales: indemnizaciones, prestaciones SS, dietas/gastos de viaje |
| Deducciones (deductions) | IRPF withholding (amount and rate) |
|  | Contingencias comunes (4.70%) |
|  | Desempleo (1.55% or 1.60%) |
|  | Formación profesional (0.10%) |
|  | MEI (0.15%) |
|  | Other deductions (anticipos, préstamos, etc.) |
| Totals | Total devengado (gross), total a deducir, líquido total a percibir (net pay) |
| Employer cost | Base de cotización contingencias comunes, base de cotización contingencias profesionales, employer contribution breakdown |
| Footer | Date, employer signature (or electronic), employee signature |

### Delivery

- Paper or electronic format
- Employee must receive before or on payment date
- Employer must retain copies for 4 years minimum

## Section 8 -- Filing Obligations

### Monthly

**Monthly**

| Obligation | Deadline | Method |
| --- | --- | --- |
| Cotizaciones SS (RLC -- Recibo de Liquidación de Cotizaciones) | Last day of the following month | Sistema RED / Siltra (TGSS) |
| SS payment | Last day of the following month | Direct debit or electronic payment |
| IRPF withholding payment (Modelo 111) | 20th of following month (quarterly for < 6 employees in certain cases) | AEAT Sede Electrónica |

### Quarterly (Small Employers)

**Quarterly (Small Employers)**

| Obligation | Deadline | Notes |
| --- | --- | --- |
| Modelo 111 (quarterly) | 20th of month after quarter (20 Apr, 20 Jul, 20 Oct, 20 Jan) | For employers with < 6 employees or specific situations |

### Annual

**Annual**

| Obligation | Deadline | Notes |
| --- | --- | --- |
| Modelo 190 (annual withholding summary) | 31 January of following year | Summary of all IRPF withholdings, by employee |
| Certificado de retenciones | Before 31 January | Issued to each employee; feeds into their IRPF return |
| CRA (Certificado de empresa para prestaciones) | Within 10 days of termination | For employee to claim unemployment benefits |

### Employee Obligations

**Employee Obligations**

| Item | Detail |
| --- | --- |
| Declaración de la Renta (IRPF annual return) | April -- June (Campaña de la Renta) |
| Mandatory filing threshold | Generally > EUR 22,000 from single employer; > EUR 15,876 from 2+ employers |

## Section 9 -- Common Payroll Patterns

### Typical Bank Statement Descriptions (Salary Credits)

**Typical Bank Statement Descriptions (Salary Credits)**

| Pattern | Classification |
| --- | --- |
| NOMINA, SALARIO, HABERES | Net salary payment |
| PAGA EXTRA, PAGA EXTRAORDINARIA | Extra payment (June/December) |
| LIQUIDACION, FINIQUITO | Final settlement on termination (includes prorated paga extra, vacation, etc.) |
| INDEMNIZACION DESPIDO | Severance payment |
| PRESTACION INSS, INCAPACIDAD TEMPORAL | Sickness/maternity benefit from INSS |
| DESEMPLEO SEPE | Unemployment benefit |

### Typical Employer Debit Patterns

**Typical Employer Debit Patterns**

| Pattern | Classification |
| --- | --- |
| TGSS COTIZACIONES, SEG SOCIAL | Social security contribution payment |
| AEAT 111, HACIENDA RETENCIONES | IRPF withholding remittance |
| NOMINAS TRANSFERENCIA | Salary disbursement to employees |
| FOGASA | Wage Guarantee Fund contribution |
| MUTUA [NAME] | Occupational risk mutual (AT/EP) |

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (IRPF + SS) | **This skill (spain-payroll.md)** |
| Self-employed (autónomos) tax and SS | spain-autonomos.md |
| IVA (Spanish VAT) | spain-vat-return.md |
| Bookkeeping | spain-bookkeeping.md |
| E-invoicing (TicketBAI, Verifactu, SII) | spain-einvoice.md |

### Key Handoff Points

- **Payroll → Bookkeeping:** Gross wages + employer SS are P&L expenses (cuentas 640 + 642). Employee IRPF is a liability (cuenta 4751) until Modelo 111 payment. Employee/employer SS contributions are liabilities (cuenta 476) until payment to TGSS. Pagas extras should be accrued monthly (1/12 per month).
- **Payroll → Income Tax:** Certificado de retenciones feeds into the employee's Declaración de la Renta. The AEAT algorithm determines withholding rates -- employers do not manually compute brackets.
- **Payroll → SS:** RLC/RNT (formerly TC1/TC2) must reconcile with nómina totals. Sistema RED is the electronic channel for all SS communications.

## PROHIBITIONS

- **Never manually compute IRPF** — NEVER manually compute IRPF withholding rates -- use the official AEAT ALGORITMO_2026
- **Never forget MEI and solidarity surcharge** — NEVER forget the MEI (0.90% total) and solidarity surcharge for high earners -- they are mandatory from 2026
- **Never confuse 12/14 payment structures** — NEVER confuse 12-payment and 14-payment structures -- the base de cotización must correctly prorate pagas extras
- **Never omit pagas extraordinarias** — NEVER omit pagas extraordinarias -- 2 per year are legally required (Art. 31 ET)  _(Art. 31 ET)_
- **Never apply IRPF to SMI without verification** — NEVER apply IRPF to SMI-level salaries without verifying the algorithm produces 0% -- most SMI earners are exempt
- **Never exceed 80 hours annual overtime** — NEVER exceed 80 hours of annual overtime (unless compensated with rest)
- **Never issue incomplete nómina** — NEVER issue a nómina missing any field required by the official model
- **Never miss SS/Modelo 111 deadlines** — NEVER miss the SS payment deadline (last day of following month) or Modelo 111 deadline (20th)
- **Never present computations as definitive** — NEVER present payroll computations as definitive -- direct to an asesor fiscal or gestor for sign-off

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or graduado social in Spain) before implementation.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
