---
name: mx-imss
description: Use this skill whenever asked about Mexican IMSS social security for self-employed individuals. Trigger on phrases like "IMSS", "seguro social Mexico", "regimen voluntario", "incorporacion voluntaria", "IMSS freelancer", "aseguramiento voluntario", "Modalidad 40", or any question about voluntary IMSS enrollment, contribution calculation, or benefits for self-employed persons in Mexico. Covers voluntary inscription (Modalidad 40, regimen voluntario), contribution bases, health/maternity/retirement/disability benefits, and tax deductibility. ALWAYS read this skill before touching any Mexican IMSS work.
version: 2.1
jurisdiction: MX
tax_year: 2026
last_updated: 2026-11-02
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MX Imss

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Mexico |
| Tax/Contribution | IMSS Social Security (voluntary self-employed) |
| Currency | MXN only |
| Primary legislation | Ley del Seguro Social (LSS) |
| Supporting legislation | Reglamento de la LSS en materia de Afiliacion; Ley del INFONAVIT; Ley del ISR Arts. 25 fr. VI, 28 |
| Authority | Instituto Mexicano del Seguro Social (IMSS) |
| Portal | IMSS Digital (imss.gob.mx) |
| Filing deadline | Monthly contributions; enrolment at any time |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Mexican contador publico or social security specialist |
| Skill version | 2.1 |

### UMA Reference Values (2026, INEGI)

**UMA Reference Values**

| Item | Value |
| --- | --- |
| Daily UMA | MXN 117.31 |
| Monthly UMA | MXN 3,566.22 |
| Annual UMA | MXN 42,794.64 |

### IMSS Five Branches of Insurance

**IMSS Five Branches of Insurance**

| Branch | Coverage |
| --- | --- |
| Enfermedades y Maternidad | Medical care, prescriptions, maternity leave |
| Invalidez y Vida | Disability pension, death benefits |
| Retiro, Cesantia y Vejez | Old-age pension, unemployment in advanced age |
| Riesgos de Trabajo | Work accidents and occupational diseases |
| Guarderias y Prestaciones Sociales | Daycare, social services |

### Voluntary Enrolment Options

**Voluntary Enrolment Options**

| Option | Who | Coverage | Key Detail |
| --- | --- | --- | --- |
| IVRO (Art. 13) | Self-employed, freelancers | All 5 branches | Total approx. 25-30% of chosen base, varying with the base (the illness/maternity in-kind quota is a fixed daily employer cuota per insured, not a percentage of the base) |
| Seguro de Salud para la Familia (Art. 240) | Any non-covered person | Health only | Fixed annual fee in pesos by age bracket; NO pension |
| Modalidad 40 (Art. 218) | Former employees with 52+ prior weeks | Pension only (Invalidez y Vida + Retiro) | Total 10.075% only when the base is 1 salario minimo; approx. 18.8% at bases of 4.01 UMA or more; max 25 UMA |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Employment status unknown | STOP -- do not proceed |
| Prior contribution weeks unknown | Assume ineligible for Modalidad 40 until confirmed |
| Desired salary base unknown | IVRO base floor is the minimum wage of the geographic area (peso amount not yet confirmed); for Modalidad 40 estimates at 4.01 UMA or more use the 18.8% top-band total |
| UMA value unconfirmed | Direct client to INEGI for current value |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** -- Confirmation of self-employed status, CURP, RFC, and whether currently enrolled in any IMSS regime.
- **Recommended inputs** -- Prior IMSS contribution history (semanas cotizadas), desired salary base for contributions, family members to cover.
- **Ideal inputs** -- Full contribution statement from IMSS, prior year ISR return, INFONAVIT status.

### Refusal Catalogue

- **R-MX-1 -- Salaried employees** -- If the client is a salaried employee, the EMPLOYER handles IMSS. This skill covers self-employed/voluntary enrolment only. Stop.  _(R-MX-1)_
- **R-MX-2 -- Employer-employee IMSS disputes** -- Disputes between employers and IMSS regarding contributions or registrations are outside this skill scope. Escalate to a specialist.  _(R-MX-2)_
- **R-MX-3 -- Disability claims** -- IMSS disability benefit claims require medical and legal evaluation. Escalate.  _(R-MX-3)_
- **R-MX-4 -- INFONAVIT complex cases** -- INFONAVIT credit interaction with voluntary IMSS is outside this skill scope. Escalate.  _(R-MX-4)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier for bank statement lines related to IMSS.

### 3.1 IMSS Payment Patterns (Debits)

**IMSS Payment Patterns (Debits)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| IMSS CUOTA OBRERO PATRONAL / IMSS PAGO | IMSS contribution | EXCLUDE from business expenses | Employer-share IMSS cuotas are deductible under LISR Art. 25 fr. VI; Art. 151 personal deductions do not list IMSS cuotas |
| IMSS REGIMEN VOLUNTARIO / IMSS IVRO | IVRO contribution | EXCLUDE from business expenses | Employer-share portion deductible under LISR Art. 25 fr. VI (business-income context) |
| IMSS MODALIDAD 40 / IMSS MOD 40 | Modalidad 40 payment | EXCLUDE from business expenses | Same LISR Art. 25 fr. VI basis for the employer-share portion |
| IMSS SEGURO SALUD FAMILIA / IMSS SSF | Family health insurance | EXCLUDE from business expenses | Art. 151 fr. I medical-expense treatment not confirmed (see Sources) |
| INFONAVIT / INFONAVIT PAGO | Housing contribution | EXCLUDE | Not IMSS; separate programme |

### 3.2 IMSS Benefit Patterns (Credits)

**IMSS Benefit Patterns (Credits)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| IMSS PENSION / PENSION IMSS | Pension income | Taxable income | Report as pension income on ISR return |
| IMSS INCAPACIDAD / SUBSIDIO IMSS | Disability/sickness benefit | Verify tax treatment | May be exempt up to certain amounts |
| IMSS REEMBOLSO | IMSS refund | EXCLUDE | Not income |

## Section 4 -- Worked Examples

### Worked example 1: IVRO at a 10 UMA base

**Input:** Self-employed designer, no prior IMSS coverage, wants coverage for self and family. Chosen base: 10 UMA daily.

**Reasoning:**
The IVRO base floor is the minimum wage of the geographic area and the ceiling is 25 UMA (IMSS procedure 9210-003-612). 10 UMA daily = MXN 1,173.10 (2026 UMA MXN 117.31); monthly base = 1,173.10 x 30.4 = MXN 35,662.24. The self-employed person pays both shares of the percentage-based financing premiums: illness/maternity cash 1% (Art. 107) + Invalidez y Vida 2.375% (Art. 147) + Retiro 2% (Art. 168 fr. I) + Cesantia y Vejez 13% (11.875% patronal top band + 1.125% obrera, Art. 168 fr. II, base at or above 4.01 UMA) + Guarderias 1% (Art. 211) + Riesgos de Trabajo prima media clase I 0.54355% (Art. 73) = 19.91855% of base = MXN 7,103.40/month. On top of that come the fixed illness/maternity in-kind employer cuota per insured per day (Art. 106 fr. I) and the excess cuotas on SBC above three times the minimum wage (Art. 106 fr. II); their peso amounts are not computable from the archived sources (see Sources).

```oa-check
name: IVRO percentage cuotas at 10 UMA base 2026
inputs:
  uma_d: 117.31
steps:
  - sbc_d: uma_d * 10
  - sbc_m: sbc_d * 30.4
  - pct: 0.01 + 0.02375 + 0.02 + 0.13 + 0.01 + 0.0054355
  - cuotas_pct_based: sbc_m * pct
expected:
  sbc_m: 35662.24
  cuotas_pct_based: 7103.40
```

**Classification:** IVRO percentage-based cuotas approx. MXN 7,103.40/month plus the fixed in-kind employer cuota per insured. Deductibility basis is LISR Art. 25 fr. VI for the employer-share portion, not Art. 151.

### Worked example 2: Modalidad 40 at a 10 UMA base

**Input:** Former employee with 200 weeks prior contributions. Left employment 2 years ago. Chose base of 10 UMA daily.

**Reasoning:**
Eligible for Modalidad 40 (has 52+ weeks, within 5-year window). Daily base: MXN 1,173.10; monthly base: MXN 35,662.24. Total rate at 4.01 UMA or more: 18.8% (Invalidez y Vida 2.375% + Retiro 2% + Cesantia y Vejez 11.875% patronal + 1.125% obrera + the Art. 25 second-paragraph quota 1.425%). Monthly cost: MXN 6,704.50. Covers pension only -- NO health coverage.

```oa-check
name: Modalidad 40 at 10 UMA base 2026
inputs:
  sbc_m: 35662.24
steps:
  - pct: 0.02375 + 0.02 + 0.11875 + 0.01125 + 0.01425
  - cuota: sbc_m * pct
expected:
  pct: 0.188
  cuota: 6704.50
```

**Classification:** Modalidad 40 contribution MXN 6,704.50/month. Client needs separate health coverage.

### Worked example 3: Seguro de Salud para la Familia

**Input:** Family of 4: 2 adults (age 35, 33), 2 children (age 8, 5). No current IMSS coverage.

**Reasoning:**
Annual fee per person is a fixed peso amount by age bracket (IMSS fee schedule effective 1 March 2025). Adults 35 and 33 fall in the 30-39 bracket: MXN 11,850 each. Children under 19: MXN 8,900 each. Total annual: MXN 41,500. Health coverage only; no pension.

```oa-check
name: Seguro de Salud para la Familia family of four
inputs:
  adulto_30_39: 11850
  menor_19: 8900
steps:
  - total_anual: 2 * adulto_30_39 + 2 * menor_19
expected:
  total_anual: 41500
```

**Classification:** Annual family health premium MXN 41,500. Whether the premium qualifies as an Art. 151 fr. I medical expense is not confirmed (see Sources).

### Worked example 4: Modalidad 40 at Maximum Base

**Input:** High earner wanting maximum pension. 500 weeks prior contributions. Chose 25 UMA daily.

**Reasoning:**
Maximum Modalidad 40 base: 25 UMA daily = MXN 2,932.75/day; monthly base = MXN 89,155.60. Total rate 18.8% (base far above 4.01 UMA). Monthly cost: MXN 16,761.25. Maximum pension accumulation strategy.

```oa-check
name: Modalidad 40 at 25 UMA ceiling 2026
inputs:
  uma_d: 117.31
steps:
  - sbc_d: uma_d * 25
  - sbc_m: sbc_d * 30.4
  - pct: 0.02375 + 0.02 + 0.11875 + 0.01125 + 0.01425
  - cuota: sbc_m * pct
expected:
  sbc_m: 89155.60
  cuota: 16761.25
```

**Classification:** Modalidad 40 contribution MXN 16,761.25/month. Maximum pension strategy. Flag for reviewer to assess long-term pension impact.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 IVRO Contribution Rates (Art. 13, 106, 107, 147, 168, 211)

- **IVRO both shares** -- For IVRO, the self-employed person pays BOTH employer and employee portions.  _(LSS Art. 13, 106, 107, 147, 168, 211)_
- **IVRO base range** -- Base floor is the minimum wage of the geographic area; ceiling is 25 times the UMA.  _(IMSS procedure 9210-003-612, sec. 5.2.17)_

**IVRO Contribution Rates**  _(LSS Art. 13, 106, 107, 147, 168, 211)_

| Branch | Rate |
| --- | --- |
| Enfermedades y Maternidad (in kind) | Fixed employer cuota diaria per insured (Art. 106 fr. I reads 13.9% of one general daily minimum wage in the consolidated text; current value on the Not yet confirmed line) PLUS additional 6% patronal and 2% obrera on SBC above three times the minimum wage (Art. 106 fr. II) |
| Enfermedades y Maternidad (cash) | 1% of SBC (Art. 107: 70% patronal, 25% obrera, 5% federal) |
| Invalidez y Vida | 1.75% patronal + 0.625% obrera = 2.375% (Art. 147) |
| Retiro | 2.00% (Art. 168 fr. I) |
| Cesantia en Edad Avanzada y Vejez | Patronal 3.150%-11.875% of SBC by wage band (Art. 168 fr. II a table; 11.875% at 4.01 UMA and above) + obrera 1.125% (Art. 168 fr. II b) |
| Guarderias | 1.00% (Art. 211) |
| Riesgos de Trabajo | Prima media clase I 0.54355% (Art. 73; office/low-risk default) |
| **Approximate total** | **approx. 25-30% of base, varying with the base** |

### 5.2 Modalidad 40 Contribution Rates (Art. 218)

**Modalidad 40 Contribution Rates**  _(LSS Art. 218, 147, 168, 25 para. 2)_

| Component | Rate |
| --- | --- |
| Invalidez y Vida | 2.375% (1.75% + 0.625%) |
| Retiro | 2.00% (the full quota) |
| Cesantia y Vejez | Patronal 3.150%-11.875% by wage band + obrera 1.125% |
| Art. 25 second-paragraph quota | 1.425% (1.05% + 0.375%) |
| **Total** | **10.075% only when the base is 1 salario minimo; approx. 18.8% at bases of 4.01 UMA or more** |

- **Modalidad 40 maximum base** -- 25 UMA daily  _(LSS Art. 218; IMSS procedure 9210-003-209)_

### 5.3 Seguro de Salud para la Familia (Art. 240-245)

**Seguro de Salud para la Familia Annual Fee by Age**  _(LSS Art. 240-245; IMSS fee schedule effective 1 March 2025)_

| Age Group | Annual Fee (MXN) |
| --- | --- |
| 0-19 | 8,900 |
| 20-29 | 11,100 |
| 30-39 | 11,850 |
| 40-49 | 13,800 |
| 50-59 | 14,250 |
| 60-69 | 19,800 |
| 70-79 | 20,650 |
| 80 and over | 21,300 |

- **Payment schedule** -- Payment: annual, upfront.  _(LSS Art. 240-245)_

### 5.4 Tax Deductibility (LISR Arts. 25 fr. VI, 28)

**Tax Deductibility**  _(Ley del ISR Art. 25 fr. VI, Art. 28 fr. I)_

| Contribution Type | Deductible? |
| --- | --- |
| IVRO cuotas | Employer-share IMSS cuotas are authorized deductions under LISR Art. 25 fr. VI (business-income context); Art. 151 personal deductions list no IMSS item |
| Modalidad 40 | Same LISR Art. 25 fr. VI basis for the employer-share portion; amounts that originally correspond to third parties are non-deductible under Art. 28 fr. I |
| Seguro de Salud para la Familia | Not confirmed -- Art. 151 fr. I medical-expense treatment unverified (see Sources) |

### 5.5 Eligibility Rules

**Eligibility Rules**

| Rule | Detail |
| --- | --- |
| IVRO eligibility | Self-employed workers, freelancers, independent professionals |
| Modalidad 40 eligibility | Minimum 52 weeks prior contributions; must enrol within 5 years of last employer contribution |
| Seguro de Salud eligibility | Any person not otherwise covered by IMSS |

### 5.6 2020 Reform Impact

- **2020 pension reform impact** -- The DOF 16-12-2020 reform rewrote LSS Art. 168 fr. II: the employer Cesantia en Edad Avanzada y Vejez quota is a wage-band table effective immediately, 3.150% at 1.00 salario minimo rising to 11.875% at SBC of 4.01 UMA and above. The consolidated text contains no annual-increase schedule through 2030; 11.875% is the current top rate. Whether the decree's transitional articles set lower 2023-2030 transitional rates is on the Not yet confirmed line.  _(Reforma LSS DOF 16-12-2020)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Choosing Between IVRO and Seguro de Salud

Freelancer wants health coverage only, no pension. Seguro de Salud is lower cost but accumulates no pension credits. If long-term retirement planning matters, IVRO is required. Flag for reviewer to assess retirement impact.

### 6.2 Choosing Salary Base for IVRO

Higher base = higher cost but higher pension and maternity/disability benefits. Common strategy: choose a base reflecting actual income for adequate coverage. Flag for reviewer to balance cost vs coverage.

### 6.3 Modalidad 40 as Pension Strategy

Modalidad 40 allows choosing up to 25 UMA base to maximize future pension. This is a common strategy for persons approaching retirement age. Flag for reviewer -- qualified advisor must assess pension projection.

### 6.4 Gap in Contributions

If client had employer IMSS, left more than 5 years ago with no contributions since, the Modalidad 40 right has lapsed. IVRO is the only voluntary option.

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
  E2. Estimated ISR benefit                       ___________

REVIEWER FLAGS:
  [ ] Employment status confirmed (self-employed only)?
  [ ] Prior weeks verified for Modalidad 40 eligibility?
  [ ] 5-year window checked for Modalidad 40?
  [ ] UMA values verified with INEGI?
  [ ] Art. 168 fr. II wage-band table applied (no annual escalator)?
```

## Section 8 -- Bank Statement Reading Guide

### Mexican Bank Statement Formats

**Mexican Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| BBVA Mexico (Bancomer) | CSV / PDF | Fecha, Descripcion, Cargo, Abono, Saldo |
| Banorte | CSV | Fecha, Concepto, Retiro, Deposito, Saldo |
| Citibanamex | CSV / PDF | Fecha, Descripcion, Cargos, Abonos, Saldo |
| Santander Mexico | CSV | Fecha, Concepto, Cargo, Abono, Saldo |
| HSBC Mexico | CSV | Fecha, Descripcion, Debito, Credito, Saldo |
| Scotiabank Mexico | CSV | Fecha, Descripcion, Retiro, Deposito, Saldo |

### Key IMSS-Related Narrations

**Key IMSS-Related Narrations**

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| IMSS CUOTA / PAGO IMSS | IMSS contribution | Social security -- LISR Art. 25 fr. VI basis for the employer share |
| IMSS MOD 40 / MODALIDAD 40 | Modalidad 40 payment | Pension contribution -- LISR Art. 25 fr. VI basis |
| IMSS SSF / SEGURO SALUD | Family health insurance | Medical-expense treatment not confirmed |
| INFONAVIT / PAGO INFONAVIT | Housing fund payment | Separate from IMSS |
| PENSION IMSS / RETIRO IMSS | Pension receipt | Taxable pension income |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Identify all IMSS-related debits (contributions paid)
2. Classify as personal social-security payments (NOT business expenses); deductibility basis for the employer share is LISR Art. 25 fr. VI
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

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| IMSS coverage branches | LSS Art. 6, 11 |
| IVRO voluntary enrolment | LSS Art. 13 |
| Modalidad 40 | LSS Art. 218 |
| Seguro de Salud para la Familia | LSS Art. 240-245 |
| Contribution rates | LSS Art. 106, 107, 147, 168, 211 |
| ISR deductibility | Ley del ISR Art. 25 fr. VI, 28 |
| UMA usage | Decreto DOF 27/01/2016 |
| 2020 pension reform | Reforma LSS DOF 16-12-2020 (Art. 168 fr. II quota table) |

### Known Gaps / Out of Scope

- Employer-employee IMSS obligations
- IMSS disability claims processing
- INFONAVIT credit interaction
- ISSSTE (public sector social security)
- Pension calculation projections (require actuarial analysis)

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 2.1 | 2026-11-02 | Deep-review corrections: IVRO/Modalidad 40 rates (Art. 106 fixed cuota, Art. 168 fr. II wage-band table, Art. 25 para. 2 quota), Seguro de Salud fixed peso fees, LISR Art. 25 fr. VI deductibility basis, 2026 UMA, worked examples recomputed |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; bank statement patterns; worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Employment status confirmed as self-employed?
- [ ] Prior IMSS weeks verified before Modalidad 40 recommendation?
- [ ] 5-year Modalidad 40 window checked?
- [ ] UMA values verified with INEGI for current year?
- [ ] Art. 168 fr. II wage-band table applied (no annual escalator)?
- [ ] Deductibility cited to LISR Art. 25 fr. VI (not Art. 151)?

## PROHIBITIONS

- NEVER enrol in Modalidad 40 without verifying at least 52 weeks of prior contributions
- NEVER assume Seguro de Salud para la Familia provides pension or disability coverage -- it is health only
- NEVER use salario minimo for UMA-based IMSS calculations -- UMA governs since 2017; the exceptions are the IVRO base floor and the illness/maternity in-kind fixed cuota, which remain salario-minimo based
- NEVER ignore the 5-year window for Modalidad 40 enrolment after leaving employment
- NEVER apply one flat Cesantia y Vejez rate -- the employer quota is the LSS Art. 168 fr. II wage-band table (3.150% at 1.00 salario minimo to 11.875% at 4.01 UMA and above)
- NEVER apply an illness/maternity in-kind percentage to the whole chosen base -- Art. 106 finances it with a fixed employer cuota diaria per insured plus excess cuotas only on SBC above three times the minimum wage
- NEVER present IMSS calculations as exact -- use the IMSS calculator at imss.gob.mx for precise amounts
- NEVER advise on Modalidad 40 as a pension strategy without flagging for a qualified advisor
- NEVER cite ISR Art. 151 as the IMSS deductibility basis -- Art. 151 lists no IMSS cuotas; the employer share is deductible under LISR Art. 25 fr. VI
- NEVER present calculations as definitive -- always label as estimated and direct client to IMSS or a qualified Mexican contador publico

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Ley del Seguro Social, consolidated text (Cámara de Diputados), last reform DOF 15-01-2026 -- Arts. 13, 25, 28, 73, 106, 107, 147, 168, 211, 218 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf | 2026-10-28 |
| Ley del Impuesto Sobre la Renta, consolidated text (Cámara de Diputados), last reform DOF 01-04-2024 -- Arts. 25 fr. VI, 28, 151 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-28 |
| INEGI, Unidad de Medida y Actualización, valores por año (2026: MXN 117.31 daily) | https://www.inegi.org.mx/temas/uma/ | 2026-11-02 |
| IMSS, Seguro de Salud para la Familia, cuotas vigentes a partir del 1 de marzo de 2025 | https://www.imss.gob.mx/derechoH/segurosalud-familia | 2026-11-02 |
| IMSS, Procedimiento 9210-003-612, aseguramiento de personas trabajadoras independientes o por cuenta propia (IVRO) | https://reposipot.imss.gob.mx/normatividad/DNMR/Procedimiento/9210-003-612.pdf | 2026-11-02 |
| IMSS, Procedimiento 9210-003-209, Continuación Voluntaria Régimen Obligatorio Modalidad 40 | https://www.imss.gob.mx/sites/all/statics/pdf/procedimientos/9210-003-209.pdf | 2026-11-02 |

Not yet confirmed: the current illness/maternity in-kind fixed employer cuota (the consolidated LSS text read shows the original 13.9% of one general daily minimum wage in Art. 106 fr. I; the 1995 law's transitional articles raised it, and the current figure is reported as 20.40% of one UMA per insured per day, but the transitorio text is not in the archived copy); the current illness/maternity excess cuotas (the text read shows 6% patronal / 2% obrera on SBC above three times the minimum wage; 1.10% / 0.40% above 3 UMA are reported but not in the archived text); whether the DOF 16-12-2020 decree's transitional articles set lower 2023-2030 transitional employer cesantía y vejez rates than the final Art. 168 fr. II table read in the consolidated text; the 2025 and 2026 general minimum wage peso amounts (the IVRO base floor and the Art. 106 thresholds; no archived DOF wage decree); Seguro de Salud para la Familia fees effective from 1 March 2026 (the page read shows the 1 March 2025 schedule); whether the Seguro de Salud para la Familia annual premium qualifies as an Art. 151 fr. I medical expense.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico, social security specialist, or equivalent licensed practitioner in Mexico) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
