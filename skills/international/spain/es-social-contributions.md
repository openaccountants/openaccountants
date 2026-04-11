---
name: es-social-contributions
description: >
  Use this skill whenever asked about Spanish self-employed social contributions (cuota de autonomos / RETA). Trigger on phrases like "cuota autonomos", "RETA", "social contributions Spain", "autónomo contributions", "how much do I pay as autonomo", "tarifa plana", "cese de actividad", "regularizacion cuotas", "base de cotización", or any question about Spanish self-employed social security obligations. This skill covers the 2023+ income-based contribution system, 2025 contribution tables by income tranche, tarifa plana for new autonomos, contribution rate breakdown, annual regularisation, payment schedule, IT coverage, and tax deductibility. ALWAYS read this skill before touching any Spanish social contributions work.
version: 1.0
jurisdiction: ES
tax_year: 2025
category: international
depends_on:
  - social-contributions-workflow-base
---

# Spain Social Contributions (RETA) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Spain |
| Jurisdiction Code | ES |
| Primary Legislation | Ley General de la Seguridad Social (LGSS), Real Decreto-ley 13/2022 de 26 de julio (new income-based system) |
| Supporting Legislation | Orden PJC/178/2025 de 25 de febrero (2025 contribution rates and bases); Ley 20/2007 del Estatuto del Trabajo Autonomo; Ley 35/2006 del IRPF (tax deductibility) |
| Tax Authority | Tesoreria General de la Seguridad Social (TGSS) |
| Rate Publisher | TGSS / Ministerio de Inclusion, Seguridad Social y Migraciones |
| Contributor | Open Accountants |
| Validated By | Pending -- requires sign-off by a qualified Spanish asesor fiscal or gestor administrativo |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: tranche table application, contribution rate breakdown, tarifa plana eligibility, payment schedule, regularisation mechanics. Tier 2: pluriactividad (dual employed + autonomo), mid-year starts, societario vs persona fisica edge cases. Tier 3: disability regimes, Mutuas MATEPSS specifics, cross-border posted workers. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified asesor fiscal must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any RETA contribution figure, you MUST know:

1. **Type of autonomo** [T1] -- persona fisica (individual freelancer/sole trader) or autonomo societario (company director). Rates and minimum bases differ.
2. **Estimated monthly net income (rendimientos netos)** [T1] -- determines the applicable tranche. Net income = gross income minus deductible expenses minus 7% generic deduction (3% for societarios).
3. **Is this the first time registering as autonomo?** [T1] -- determines tarifa plana eligibility.
4. **Date of alta (registration) in RETA** [T1] -- determines pro-rata and tarifa plana start.
5. **Any simultaneous employment (pluriactividad)?** [T2] -- may reduce contribution base. Flag for reviewer.
6. **Age** [T2] -- workers aged 47+ have special base election restrictions in transitional provisions.

**If estimated net income is unknown, the autonomo must still choose a provisional base within their estimated tranche. STOP and ask for an income estimate before proceeding.**

---

## Step 1: The Income-Based System (2023 Onwards) [T1]

**Legislation:** Real Decreto-ley 13/2022 de 26 de julio

Since 1 January 2023, Spain operates a contribution system based on actual income (rendimientos netos) for all RETA workers. The previous system of freely choosing any base above the minimum was abolished.

### How It Works

1. The autonomo estimates their annual net income (rendimientos netos) at the start of the year.
2. Net income is calculated as: gross income minus deductible business expenses minus a 7% flat deduction for generic expenses (3% for autonomos societarios).
3. The monthly net income determines which of 15 tranches the autonomo falls into.
4. Each tranche has a minimum and maximum contribution base.
5. The autonomo must choose a base within their tranche range.
6. The monthly contribution (cuota) = chosen base x total contribution rate (31.40% for 2025).
7. After the IRPF tax return is filed, TGSS regularises contributions based on actual income vs the provisional base chosen.

---

## Step 2: 2025 Contribution Table -- 15 Tranches [T1]

**Legislation:** Orden PJC/178/2025 de 25 de febrero; RDL 13/2022 Disposicion transitoria primera

### Tabla Reducida (Tranches 1--3: income below general minimum base)

| Tranche | Monthly Net Income (EUR) | Min. Base (EUR) | Cuota Minima (EUR/month) |
|---------|--------------------------|-----------------|--------------------------|
| 1 | <= 670 | 653.59 | ~200 |
| 2 | 670.01 -- 900.00 | 718.95 | ~220 |
| 3 | 900.01 -- 1,125.90 | 849.67 | ~260 |

### Tabla General (Tranches 4--15)

| Tranche | Monthly Net Income (EUR) | Min. Base (EUR) | Cuota Minima (EUR/month) |
|---------|--------------------------|-----------------|--------------------------|
| 4 | 1,125.91 -- 1,300.00 | 950.98 | ~291 |
| 5 | 1,300.01 -- 1,500.00 | 960.78 | ~294 |
| 6 | 1,500.01 -- 1,700.00 | 960.78 | ~294 |
| 7 | 1,700.01 -- 1,850.00 | 1,143.79 | ~350 |
| 8 | 1,850.01 -- 2,030.00 | 1,209.15 | ~370 |
| 9 | 2,030.01 -- 2,330.00 | 1,274.51 | ~390 |
| 10 | 2,330.01 -- 2,760.00 | 1,356.21 | ~415 |
| 11 | 2,760.01 -- 3,190.00 | 1,437.91 | ~440 |
| 12 | 3,190.01 -- 3,620.00 | 1,519.61 | ~465 |
| 13 | 3,620.01 -- 4,050.00 | 1,601.31 | ~490 |
| 14 | 4,050.01 -- 6,000.00 | 1,732.03 | ~530 |
| 15 | > 6,000.00 | 1,928.10 | ~590 |

**Notes:**
- Cuota minima figures are approximate (base minima x 31.40%). Exact cuota depends on the base chosen within the tranche range.
- The maximum base for all tranches in 2025 is EUR 4,909.50/month (general RETA maximum).
- Autonomos societarios: minimum base is EUR 1,000.00/month regardless of tranche, resulting in a minimum cuota of approximately EUR 314/month.
- The autonomo may choose any base between the minimum and maximum of their tranche. Most choose the minimum.

---

## Step 3: Contribution Rate Breakdown [T1]

**Legislation:** Orden PJC/178/2025; LGSS

The total contribution rate applied to the chosen base in 2025 is **31.40%**, broken down as follows:

| Concept | Rate | Notes |
|---------|------|-------|
| Contingencias comunes (CC) | 28.30% | Covers retirement pension, permanent disability, death and survivorship |
| Contingencias profesionales (CP) | 1.30% | Covers workplace accidents and occupational illness (0.66% IT + 0.64% IPS/MS) |
| Cese de actividad | 0.90% | Covers cessation of activity benefit (equivalent of unemployment for autonomos) |
| Formacion profesional (FP) | 0.10% | Professional training levy |
| Mecanismo de Equidad Intergeneracional (MEI) | 0.80% | Intergenerational equity mechanism (pension sustainability fund) |
| **Total** | **31.40%** | Applied to chosen base within tranche |

### Formula

```
Cuota mensual = Base de cotizacion elegida x 31.40%
```

### Example

Autonomo with monthly net income of EUR 2,500. Falls in Tranche 10 (EUR 2,330.01 -- 2,760.00). Minimum base = EUR 1,356.21.

```
Cuota minima = EUR 1,356.21 x 31.40% = EUR 425.85/month
```

---

## Step 4: Tarifa Plana -- Flat Rate for New Autonomos [T1]

**Legislation:** LGSS Article 38 ter (as amended by RDL 13/2022)

### 2025 Rules

| Feature | Detail |
|---------|--------|
| Amount | EUR 80/month flat rate |
| Duration | First 12 months from alta in RETA |
| Extension | Additional 12 months (months 13--24) if net income in first year is below the Salario Minimo Interprofesional (SMI) |
| Total possible duration | Up to 24 months |
| Eligibility | New autonomos who have NOT been registered in RETA in the prior 2 years (3 years if previously received tarifa plana) |
| Exclusions | Autonomos colaboradores (family members); autonomos with outstanding debts to Seguridad Social or Hacienda |
| Application | At the moment of alta (registration). Cannot be applied retroactively. |
| Coverage | Covers all contingencies (CC, CP, cese, FP, MEI) -- no gaps in coverage |

### Important

- The EUR 80 tarifa plana replaces the normal tranche-based cuota entirely for the eligible period.
- During the tarifa plana period, the contribution base for benefit calculation purposes is the minimum base of Tranche 1 (EUR 653.59 in 2025).
- After the tarifa plana ends, the autonomo must choose a base within their tranche based on estimated income.

---

## Step 5: Incapacidad Temporal (IT) Coverage [T1]

**Legislation:** LGSS; RD 1273/2003

| Feature | Detail |
|---------|--------|
| Waiting period | Day 4 of illness (days 1--3 are not covered) |
| Days 4--20 | 60% of the regulatory base (base reguladora) |
| Day 21 onwards | 75% of the regulatory base |
| Who pays days 4--15 | The autonomo absorbs this (no employer to cover it) |
| Who pays day 16 onwards | The Mutua (mutual insurance company) or INSS |
| Regulatory base | The contribution base of the month prior to the baja (sick leave) |
| Maximum duration | 12 months, extendable by 6 months if recovery expected |

**The IT benefit is directly linked to the chosen contribution base. A higher base = higher daily benefit. This is one reason some autonomos choose a base above their tranche minimum.**

---

## Step 6: Payment Schedule [T1]

**Legislation:** LGSS Article 16; TGSS regulations

| Feature | Detail |
|---------|--------|
| Payment frequency | Monthly |
| Due date | Last business day of each month |
| Payment month | Current month (i.e., January cuota is due on the last business day of January) |
| Payment method | Domiciliacion bancaria (direct debit) -- mandatory since 2018 for most autonomos |
| Late payment surcharge | 10% if paid within the first month after due date; 20% thereafter |
| Interest on arrears | Legal interest rate applies in addition to surcharges |

### Base Change Windows

The autonomo may change their provisional base up to 6 times per year, effective from:

| Request submitted by | Effective from |
|---------------------|----------------|
| Last day of February | 1 March |
| Last day of April | 1 May |
| Last day of June | 1 July |
| Last day of August | 1 September |
| Last day of October | 1 November |
| Last day of December | 1 January (following year) |

---

## Step 7: Regularizacion Anual (Annual Reconciliation) [T1]

**Legislation:** RDL 13/2022 Article 308.1.c LGSS

### How It Works

1. During the year, the autonomo pays cuotas based on a **provisional** base chosen according to estimated income.
2. After the IRPF tax return is filed (typically April--June of the following year), the Agencia Tributaria communicates the definitive net income (rendimientos netos) to the TGSS.
3. The TGSS compares the definitive income against the provisional base used throughout the year.
4. The TGSS determines the tranche that corresponds to the actual income.
5. The TGSS issues a resolution:
   - **If the autonomo underpaid** (actual income higher than estimated, should have been in a higher tranche): TGSS demands additional cuotas. Payment deadline is the last day of the month following notification.
   - **If the autonomo overpaid** (actual income lower than estimated, was in a higher tranche than necessary): TGSS refunds the excess. Refund is made automatically by transfer.
6. This process is **automatic**. The autonomo does not need to request it.

### IRPF Treatment of Regularisation

- Additional cuotas demanded by TGSS: deductible as gasto deducible in the IRPF year they are paid, NOT by amending the prior year return.
- Refunds received from TGSS: taxable as income in the IRPF year they are received.

---

## Step 8: Tax Deductibility of Contributions [T1]

**Legislation:** Ley 35/2006 del IRPF, Article 28 (rendimientos de actividades economicas)

| Question | Answer |
|----------|--------|
| Are RETA contributions deductible? | YES -- 100% deductible as gasto deducible (deductible business expense) |
| In which tax? | IRPF (personal income tax) |
| Which year? | The year in which the cuotas are actually paid (cash basis) |
| Where on the tax return? | As a deductible expense within rendimientos de actividades economicas |
| Does it reduce the base imponible? | Yes -- reduces net taxable income from self-employment |
| Are tarifa plana cuotas also deductible? | Yes -- the EUR 80/month is deductible |
| Are regularisation surcharges deductible? | The additional cuotas are deductible. Late payment surcharges and penalties are NOT deductible. |

---

## Step 9: Net Income Calculation for Tranche Determination [T1]

**Legislation:** RDL 13/2022; LGSS Article 308.1

### Formula

```
Rendimientos netos = Ingresos computables - Gastos deducibles
Rendimientos netos a efectos RETA = Rendimientos netos - 7% deduccion generica
Monthly net = Rendimientos netos a efectos RETA / 12
```

- **Ingresos computables:** All income from the economic activity (invoiced revenue, in-kind income).
- **Gastos deducibles:** All expenses deductible under IRPF rules (supplies, rent, professional services, amortisation, RETA cuotas themselves, etc.).
- **7% generic deduction:** Applied automatically to cover difficult-to-justify expenses. For autonomos societarios, the deduction is 3%.

### Example

| Item | Amount (EUR) |
|------|-------------|
| Gross annual revenue | 48,000 |
| Deductible business expenses | 12,000 |
| Net income before generic deduction | 36,000 |
| 7% generic deduction | 2,520 |
| Net income for RETA purposes | 33,480 |
| Monthly net income | 2,790 |
| Applicable tranche | 11 (EUR 2,760.01 -- 3,190.00) |
| Minimum base | EUR 1,437.91 |
| Minimum cuota | ~EUR 451/month |

---

## Step 10: Cese de Actividad (Cessation of Activity Benefit) [T1]

**Legislation:** Ley 32/2010; LGSS Title V

| Feature | Detail |
|---------|--------|
| What is it | The autonomo equivalent of unemployment benefit |
| Contribution rate | 0.90% (included in the 31.40% total) |
| Minimum contribution period | 12 months continuous in the 24 months prior to cessation |
| Benefit amount | 70% of the average contribution base of the last 12 months |
| Duration | 4 to 24 months depending on contribution period |
| Qualifying events | Involuntary loss of clients (60%+ revenue drop), judicial/administrative closure, force majeure, divorce (for collaborating spouse) |
| Voluntary cessation | Does NOT qualify. Voluntary cessation of activity is NOT covered. |
| Application | Within 30 calendar days of cessation |

---

## Step 11: Edge Case Registry

### EC1 -- Autonomo societario minimum base [T1]
**Situation:** Company director registered as autonomo societario with personal net income below Tranche 4.
**Resolution:** Autonomos societarios have a minimum base of EUR 1,000.00/month regardless of income tranche. The tranche minimum does NOT apply if it is below EUR 1,000. Minimum cuota = approximately EUR 314/month.

### EC2 -- Mid-year alta (registration) [T1]
**Situation:** Autonomo registers on 15 April 2025.
**Resolution:** First month's cuota is pro-rated from the date of alta to end of month. Subsequent months are full cuotas. Tarifa plana (if eligible) starts from the date of alta. The 12-month tarifa plana period runs from the exact date of alta, not from the first of the month.

### EC3 -- Pluriactividad (simultaneous employment and self-employment) [T2]
**Situation:** Client works as an employee (Regimen General) and also has a freelance activity (RETA).
**Resolution:** The client must pay into BOTH regimes. However, a reduction in RETA base may apply if the combined contributions exceed certain thresholds. [T2] Flag for reviewer -- the exact reduction depends on the employment base and requires case-by-case calculation. The client may be entitled to a refund of up to 50% of excess contributions.

### EC4 -- Income drops mid-year [T1]
**Situation:** Autonomo estimated EUR 3,000/month but actual income has dropped to EUR 1,500/month.
**Resolution:** Use one of the 6 annual base change windows (Step 6) to reduce the provisional base to match the lower tranche. The regularisation at year-end will reconcile anyway, but changing the base mid-year avoids cash flow strain.

### EC5 -- First year with no income [T1]
**Situation:** New autonomo registers but earns nothing in the first months.
**Resolution:** If eligible for tarifa plana, the cuota is EUR 80/month regardless of income. If not eligible, the autonomo must still pay at least the Tranche 1 minimum (EUR ~200/month). At year-end regularisation, if actual annual income places them in Tranche 1, the minimum base applies and no further adjustment is needed.

### EC6 -- Autonomo over age 47 [T2]
**Situation:** Autonomo aged 48 wants to choose a high contribution base.
**Resolution:** Transitional provisions from the pre-2023 system may still restrict base choice for workers aged 47+ who were already registered before 2023. [T2] Flag for reviewer to confirm whether the pre-2023 base election restrictions still apply in the specific case.

### EC7 -- Tarifa plana second period rejected [T1]
**Situation:** Autonomo applies for the 12-month extension of tarifa plana but first-year income exceeded the SMI.
**Resolution:** Extension is denied. From month 13, the autonomo must pay the full tranche-based cuota according to their estimated income. No appeal -- the SMI threshold is a hard requirement.

### EC8 -- Regularisation results in large demand [T2]
**Situation:** Autonomo estimated Tranche 5 income but actual income places them in Tranche 14. TGSS demands significant additional cuotas.
**Resolution:** The demand is legally valid. Payment is due by the last day of the month following notification. If the autonomo cannot pay, they may request an aplazamiento (instalment plan) from TGSS. [T2] Flag for reviewer to advise on aplazamiento terms and whether the underlying income estimate was reasonable.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified asesor fiscal must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified asesor fiscal. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard autonomo, Tranche 9
**Input:** Persona fisica, monthly net income EUR 2,100, not first year, no pluriactividad.
**Expected output:** Tranche 9 (EUR 2,030.01 -- 2,330.00). Minimum base = EUR 1,274.51. Minimum cuota = EUR 1,274.51 x 31.40% = EUR 400.20/month. Annual = EUR 4,802.36.

### Test 2 -- New autonomo with tarifa plana
**Input:** First-time registration in RETA, no prior alta in last 2 years, no debts.
**Expected output:** Tarifa plana applies. Cuota = EUR 80/month for first 12 months. If first-year income is below SMI, extendable for 12 more months at EUR 80/month.

### Test 3 -- Autonomo societario, low income
**Input:** Company director registered as autonomo societario, monthly net income EUR 800.
**Expected output:** Autonomo societario minimum base = EUR 1,000.00 (overrides Tranche 2 minimum of EUR 718.95). Cuota = EUR 1,000.00 x 31.40% = EUR 314.00/month.

### Test 4 -- High earner, Tranche 15
**Input:** Persona fisica, monthly net income EUR 8,000, not first year.
**Expected output:** Tranche 15 (> EUR 6,000). Minimum base = EUR 1,928.10. Minimum cuota = EUR 1,928.10 x 31.40% = EUR 605.42/month. Annual = EUR 7,265.09.

### Test 5 -- Regularisation: underpaid
**Input:** Autonomo chose Tranche 5 provisional base (EUR 960.78/month). Actual annual net income = EUR 42,000 (monthly EUR 3,500). Actual tranche = 13 (EUR 3,620.01 -- 4,050.00). Minimum base should have been EUR 1,601.31.
**Expected output:** TGSS regularisation demands additional cuotas. Difference per month = (EUR 1,601.31 - EUR 960.78) x 31.40% = EUR 201.13/month. Annual demand = EUR 2,413.54 (12 months).

### Test 6 -- Regularisation: overpaid
**Input:** Autonomo chose Tranche 10 provisional base (EUR 1,356.21/month). Actual annual net income = EUR 12,000 (monthly EUR 1,000). Actual tranche = 3 (EUR 900.01 -- 1,125.90). Minimum base should have been EUR 849.67.
**Expected output:** TGSS refunds excess. Difference per month = (EUR 1,356.21 - EUR 849.67) x 31.40% = EUR 158.95/month. Annual refund = EUR 1,907.45.

### Test 7 -- Net income calculation with 7% deduction
**Input:** Gross annual revenue EUR 60,000, deductible expenses EUR 15,000.
**Expected output:** Net income = EUR 45,000. After 7% deduction = EUR 45,000 - EUR 3,150 = EUR 41,850. Monthly = EUR 3,487.50. Tranche 12 (EUR 3,190.01 -- 3,620.00). Min. base = EUR 1,519.61. Min. cuota = EUR 477.16/month.

### Test 8 -- Tax deductibility
**Input:** Autonomo paid EUR 4,800 in RETA cuotas during 2025. Preparing 2025 IRPF.
**Expected output:** EUR 4,800 is 100% deductible as gasto deducible within rendimientos de actividades economicas. Reduces taxable self-employment income by EUR 4,800.

---

## PROHIBITIONS

- NEVER compute contributions without knowing whether the client is persona fisica or autonomo societario -- minimum base rules differ
- NEVER use gross income to determine the tranche -- always apply the 7% generic deduction (3% for societarios) first
- NEVER tell a client they can avoid RETA contributions by earning below a threshold -- once registered, contributions are mandatory
- NEVER present tarifa plana as automatic -- the autonomo must apply at the time of alta and meet all eligibility conditions
- NEVER ignore the regularisation process -- all cuotas paid during the year are provisional until TGSS reconciles against actual IRPF income
- NEVER advise on pluriactividad reductions without reviewer confirmation -- the calculation is case-specific
- NEVER present cuota figures as exact to the cent without specifying the base chosen -- the tranche table gives minimum bases; the autonomo may choose higher
- NEVER confuse the payment date (last business day of current month) with a quarterly system
- NEVER advise that late payment surcharges or penalties are tax-deductible -- only the cuotas themselves are deductible
- NEVER compute IT (sick leave) benefits without knowing the actual contribution base of the month prior to baja

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in Spain) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
