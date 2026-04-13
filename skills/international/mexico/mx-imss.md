---
name: mx-imss
description: >
  Use this skill whenever asked about Mexican IMSS social security for self-employed individuals. Trigger on phrases like "IMSS", "seguro social Mexico", "regimen voluntario", "incorporacion voluntaria", "IMSS freelancer", "aseguramiento voluntario", "Modalidad 40", or any question about voluntary IMSS enrollment, contribution calculation, or benefits for self-employed persons in Mexico. Covers voluntary inscription (Modalidad 40, regimen voluntario), contribution bases, health/maternity/retirement/disability benefits, and tax deductibility. ALWAYS read this skill before touching any Mexican IMSS work.
version: 2.0
jurisdiction: MX
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Mexico IMSS Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Mexico |
| Tax/Contribution | IMSS Social Security (voluntary self-employed) |
| Currency | MXN only |
| Primary legislation | Ley del Seguro Social (LSS) |
| Supporting legislation | Reglamento de la LSS en materia de Afiliacion; Ley del INFONAVIT; Ley del ISR Art. 151 |
| Authority | Instituto Mexicano del Seguro Social (IMSS) |
| Portal | IMSS Digital (imss.gob.mx) |
| Filing deadline | Monthly contributions; enrolment at any time |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Mexican contador publico or social security specialist |
| Skill version | 2.0 |

### UMA Reference Values (2025 -- verify with INEGI)

| Item | Approximate Value |
|---|---|
| Daily UMA | MXN 113.14 |
| Monthly UMA | MXN 3,439.46 |
| Annual UMA | MXN 41,273.52 |

### IMSS Five Branches of Insurance

| Branch | Coverage |
|---|---|
| Enfermedades y Maternidad | Medical care, prescriptions, maternity leave |
| Invalidez y Vida | Disability pension, death benefits |
| Retiro, Cesantia y Vejez | Old-age pension, unemployment in advanced age |
| Riesgos de Trabajo | Work accidents and occupational diseases |
| Guarderias y Prestaciones Sociales | Daycare, social services |

### Voluntary Enrolment Options

| Option | Who | Coverage | Key Detail |
|---|---|---|---|
| IVRO (Art. 13) | Self-employed, freelancers | All 5 branches | Total contribution approx. 31-33% of chosen base |
| Seguro de Salud para la Familia (Art. 240) | Any non-covered person | Health only | Fixed annual cost by age bracket; NO pension |
| Modalidad 40 (Art. 218) | Former employees with 52+ prior weeks | Pension only (Invalidez y Vida + Retiro) | Total approx. 10.075% of chosen base; max 25 UMA |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Employment status unknown | STOP -- do not proceed |
| Prior contribution weeks unknown | Assume ineligible for Modalidad 40 until confirmed |
| Desired salary base unknown | Use 1 UMA (minimum) for estimates |
| UMA value unconfirmed | Direct client to INEGI for current value |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Confirmation of self-employed status, CURP, RFC, and whether currently enrolled in any IMSS regime.

**Recommended:** Prior IMSS contribution history (semanas cotizadas), desired salary base for contributions, family members to cover.

**Ideal:** Full contribution statement from IMSS, prior year ISR return, INFONAVIT status.

### Refusal Catalogue

**R-MX-1 -- Salaried employees.** "If the client is a salaried employee, the EMPLOYER handles IMSS. This skill covers self-employed/voluntary enrolment only. Stop."

**R-MX-2 -- Employer-employee IMSS disputes.** "Disputes between employers and IMSS regarding contributions or registrations are outside this skill scope. Escalate to a specialist."

**R-MX-3 -- Disability claims.** "IMSS disability benefit claims require medical and legal evaluation. Escalate."

**R-MX-4 -- INFONAVIT complex cases.** "INFONAVIT credit interaction with voluntary IMSS is outside this skill scope. Escalate."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier for bank statement lines related to IMSS.

### 3.1 IMSS Payment Patterns (Debits)

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| IMSS CUOTA OBRERO PATRONAL / IMSS PAGO | IMSS contribution | EXCLUDE from business expenses | Personal social security -- ISR deduction (Art. 151) |
| IMSS REGIMEN VOLUNTARIO / IMSS IVRO | IVRO contribution | EXCLUDE from business expenses | Personal deduction for ISR |
| IMSS MODALIDAD 40 / IMSS MOD 40 | Modalidad 40 payment | EXCLUDE from business expenses | Personal deduction for ISR |
| IMSS SEGURO SALUD FAMILIA / IMSS SSF | Family health insurance | EXCLUDE from business expenses | Medical expense deduction (limited) |
| INFONAVIT / INFONAVIT PAGO | Housing contribution | EXCLUDE | Not IMSS; separate programme |

### 3.2 IMSS Benefit Patterns (Credits)

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| IMSS PENSION / PENSION IMSS | Pension income | Taxable income | Report as pension income on ISR return |
| IMSS INCAPACIDAD / SUBSIDIO IMSS | Disability/sickness benefit | Verify tax treatment | May be exempt up to certain amounts |
| IMSS REEMBOLSO | IMSS refund | EXCLUDE | Not income |

---

## Section 4 -- Worked Examples

### Example 1 -- IVRO at Minimum Base (1 UMA)

**Input:** Self-employed designer, no prior IMSS coverage, wants minimum coverage for self and family.

**Reasoning:**
IVRO at 1 UMA daily (approx. MXN 113.14/day). Monthly base approx. MXN 3,439.46. Self-employed pays both employer and employee shares. Total rate approx. 31% of base. Monthly cost approx. MXN 1,066. Covers all 5 branches including health for family.

**Classification:** IVRO monthly contribution MXN 1,066. Deductible for ISR purposes under Art. 151.

### Example 2 -- Modalidad 40 at Moderate Base

**Input:** Former employee with 200 weeks prior contributions. Left employment 2 years ago. Chose base of 10 UMA daily.

**Reasoning:**
Eligible for Modalidad 40 (has 52+ weeks, within 5-year window). Daily base: approx. MXN 1,131.40. Monthly base: approx. MXN 34,394.60. Rate: approx. 10.075%. Monthly cost: approx. MXN 3,465. Covers pension only -- NO health coverage.

**Classification:** Modalidad 40 contribution MXN 3,465/month. Deductible for ISR. Client needs separate health coverage.

### Example 3 -- Seguro de Salud para la Familia

**Input:** Family of 4: 2 adults (age 35, 33), 2 children (age 8, 5). No current IMSS coverage.

**Reasoning:**
Annual cost per person based on age brackets. Adults (19-39): approx. 7.5% of annual UMA each. Children (under 19): approx. 5.9% of annual UMA each. Total annual: approx. MXN 11,061. Health coverage only; no pension.

**Classification:** Annual family health premium MXN 11,061. Deductible as medical expense (limited).

### Example 4 -- Modalidad 40 at Maximum Base

**Input:** High earner wanting maximum pension. 500 weeks prior contributions. Chose 25 UMA daily.

**Reasoning:**
Maximum Modalidad 40 base: 25 UMA daily = approx. MXN 2,828.50/day = approx. MXN 85,987/month. Monthly cost: approx. 10.075% = MXN 8,663. Maximum pension accumulation strategy.

**Classification:** Modalidad 40 contribution MXN 8,663/month. Maximum pension strategy. Flag for reviewer to assess long-term pension impact.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 IVRO Contribution Rates (Art. 13, 106, 147, 168, 211)

For IVRO, the self-employed person pays BOTH employer and employee portions:

| Branch | Total Rate (% of base salary) |
|---|---|
| Enfermedades y Maternidad (in kind, fixed) | approx. 20.40% |
| Enfermedades y Maternidad (in kind, excess) | Varies by salary above 3 UMA |
| Enfermedades y Maternidad (cash) | approx. 1.00% |
| Invalidez y Vida | approx. 2.375% |
| Retiro | 2.00% |
| Cesantia en Edad Avanzada y Vejez | approx. 4.375% (increasing under 2020 reform) |
| Guarderias | 1.00% |
| Riesgos de Trabajo | approx. 0.54% (office/low-risk average) |
| **Approximate total** | **approx. 31-33%** |

### 5.2 Modalidad 40 Contribution Rates (Art. 218)

| Component | Rate |
|---|---|
| Invalidez y Vida | approx. 2.375% |
| Retiro | 2.00% |
| Cesantia y Vejez | approx. 4.375% |
| **Total** | **approx. 10.075%** |

Maximum base: 25 UMA daily.

### 5.3 Seguro de Salud para la Familia (Art. 240-245)

Annual cost per family member:

| Age Group | Annual Cost (approx. % of annual UMA) |
|---|---|
| Under 19 | approx. 5.9% |
| 19-39 | approx. 7.5% |
| 40-59 | approx. 9.1% |
| 60+ | approx. 11.9% |

Payment: annual, upfront.

### 5.4 Tax Deductibility (ISR Art. 151)

| Contribution Type | Deductible? |
|---|---|
| IVRO contributions | Yes -- social security contribution deduction |
| Modalidad 40 | Yes -- deductible for ISR |
| Seguro de Salud para la Familia | Yes -- medical expense deduction (limited) |

### 5.5 Eligibility Rules

| Rule | Detail |
|---|---|
| IVRO eligibility | Self-employed workers, freelancers, independent professionals |
| Modalidad 40 eligibility | Minimum 52 weeks prior contributions; must enrol within 5 years of last employer contribution |
| Seguro de Salud eligibility | Any person not otherwise covered by IMSS |

### 5.6 2020 Reform Impact

The 2020 pension reform gradually increases the employer share of Cesantia en Edad Avanzada y Vejez from 3.15% (2023) to 11.875% (2030). For IVRO, the self-employed pays both shares, so total contribution increases annually through 2030.

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Choosing Between IVRO and Seguro de Salud

Freelancer wants health coverage only, no pension. Seguro de Salud is lower cost but accumulates no pension credits. If long-term retirement planning matters, IVRO is required. Flag for reviewer to assess retirement impact.

### 6.2 Choosing Salary Base for IVRO

Higher base = higher cost but higher pension and maternity/disability benefits. Common strategy: choose a base reflecting actual income for adequate coverage. Flag for reviewer to balance cost vs coverage.

### 6.3 Modalidad 40 as Pension Strategy

Modalidad 40 allows choosing up to 25 UMA base to maximize future pension. This is a common strategy for persons approaching retirement age. Flag for reviewer -- qualified advisor must assess pension projection.

### 6.4 Gap in Contributions

If client had employer IMSS, left more than 5 years ago with no contributions since, the Modalidad 40 right has lapsed. IVRO is the only voluntary option.

---

## Section 7 -- Working Paper Template

```
MEXICO IMSS SELF-EMPLOYED WORKING PAPER
Client: _______________  CURP: ___________  RFC: ___________
Date: ___________

A. CURRENT STATUS
  A1. Employment status                          ___________
  A2. Currently enrolled in IMSS?                ___________
  A3. Prior IMSS weeks (semanas cotizadas)       ___________
  A4. Date of last employer contribution         ___________

B. CHOSEN OPTION
  B1. IVRO / Modalidad 40 / Seguro de Salud     ___________

C. CONTRIBUTION CALCULATION
  C1. Chosen base salary (daily UMA multiples)   ___________
  C2. Monthly base                               ___________
  C3. Applicable rate                            ___________
  C4. Monthly contribution                       ___________
  C5. Annual contribution                        ___________

D. COVERAGE
  D1. Health (Enfermedades y Maternidad)         ___________
  D2. Disability (Invalidez y Vida)              ___________
  D3. Pension (Retiro, Cesantia y Vejez)         ___________
  D4. Work Risk (Riesgos de Trabajo)             ___________
  D5. Childcare (Guarderias)                     ___________

E. TAX DEDUCTIBILITY
  E1. ISR deduction type                         ___________
  E2. Estimated ISR benefit                      ___________

REVIEWER FLAGS:
  [ ] Employment status confirmed (self-employed only)?
  [ ] Prior weeks verified for Modalidad 40 eligibility?
  [ ] 5-year window checked for Modalidad 40?
  [ ] UMA values verified with INEGI?
  [ ] 2020 reform rate adjustments applied?
```

---

## Section 8 -- Bank Statement Reading Guide

### Mexican Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| BBVA Mexico (Bancomer) | CSV / PDF | Fecha, Descripcion, Cargo, Abono, Saldo |
| Banorte | CSV | Fecha, Concepto, Retiro, Deposito, Saldo |
| Citibanamex | CSV / PDF | Fecha, Descripcion, Cargos, Abonos, Saldo |
| Santander Mexico | CSV | Fecha, Concepto, Cargo, Abono, Saldo |
| HSBC Mexico | CSV | Fecha, Descripcion, Debito, Credito, Saldo |
| Scotiabank Mexico | CSV | Fecha, Descripcion, Retiro, Deposito, Saldo |

### Key IMSS-Related Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| IMSS CUOTA / PAGO IMSS | IMSS contribution | Social security -- personal deduction |
| IMSS MOD 40 / MODALIDAD 40 | Modalidad 40 payment | Pension contribution -- personal deduction |
| IMSS SSF / SEGURO SALUD | Family health insurance | Medical expense deduction |
| INFONAVIT / PAGO INFONAVIT | Housing fund payment | Separate from IMSS |
| PENSION IMSS / RETIRO IMSS | Pension receipt | Taxable pension income |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Identify all IMSS-related debits (contributions paid)
2. Classify as personal deductions (NOT business expenses)
3. Flag Modalidad 40 payments separately from IVRO
4. Do NOT assume eligibility for any programme without confirmation

Present these questions:

```
ONBOARDING QUESTIONS -- MEXICO IMSS SELF-EMPLOYED
1. Are you purely self-employed, or also employed part-time?
2. Are you currently enrolled in any IMSS regime? If so, which one?
3. What is your CURP and RFC?
4. How many weeks have you contributed to IMSS in total (semanas cotizadas)?
5. If you were previously employed, when was your last employer IMSS contribution?
6. Which family members do you want to cover (spouse, children, parents)?
7. What salary base do you want for your contributions?
8. Are you interested in health coverage, pension coverage, or both?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| IMSS coverage branches | LSS Art. 6, 11 |
| IVRO voluntary enrolment | LSS Art. 13 |
| Modalidad 40 | LSS Art. 218 |
| Seguro de Salud para la Familia | LSS Art. 240-245 |
| Contribution rates | LSS Art. 106, 147, 168, 211 |
| ISR deductibility | Ley del ISR Art. 151 |
| UMA usage | Decreto DOF 27/01/2016 |
| 2020 pension reform | Reforma LSS 2020 (Cesantia rates) |

### Known Gaps / Out of Scope

- Employer-employee IMSS obligations
- IMSS disability claims processing
- INFONAVIT credit interaction
- ISSSTE (public sector social security)
- Pension calculation projections (require actuarial analysis)

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; bank statement patterns; worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Employment status confirmed as self-employed?
- [ ] Prior IMSS weeks verified before Modalidad 40 recommendation?
- [ ] 5-year Modalidad 40 window checked?
- [ ] UMA values verified with INEGI for current year?
- [ ] 2020 reform rate increases applied?
- [ ] Contributions classified as personal deductions (NOT business expenses)?

---

## PROHIBITIONS

- NEVER enrol in Modalidad 40 without verifying at least 52 weeks of prior contributions
- NEVER assume Seguro de Salud para la Familia provides pension or disability coverage -- it is health only
- NEVER use salario minimo for IMSS calculations -- use UMA since 2017
- NEVER ignore the 5-year window for Modalidad 40 enrolment after leaving employment
- NEVER assume IVRO rates are fixed -- the 2020 reform increases Cesantia rates annually through 2030
- NEVER present IMSS calculations as exact -- use the IMSS calculator at imss.gob.mx for precise amounts
- NEVER advise on Modalidad 40 as a pension strategy without flagging for a qualified advisor
- NEVER classify IMSS contributions as business expenses -- they are personal deductions under ISR Art. 151
- NEVER present calculations as definitive -- always label as estimated and direct client to IMSS or a qualified Mexican contador publico

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico, social security specialist, or equivalent licensed practitioner in Mexico) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
