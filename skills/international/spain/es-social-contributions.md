---
name: es-social-contributions
description: >
  Use this skill whenever asked about Spanish self-employed social contributions (cuota de autonomos / RETA). Trigger on phrases like "cuota autonomos", "RETA", "social contributions Spain", "autónomo contributions", "how much do I pay as autonomo", "tarifa plana", "cese de actividad", "regularizacion cuotas", "base de cotización", "TGSS direct debit", "cuota mensual", or any question about Spanish self-employed social security. Also trigger when classifying bank statement transactions showing TGSS direct debits, cuota autonomos debits, or Seguridad Social payments. ALWAYS read this skill before touching any Spanish social contributions work.
version: 2.0
jurisdiction: ES
tax_year: 2025
category: international
depends_on:
  - social-contributions-workflow-base
---

# Spain Social Contributions (RETA) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

| Field | Value |
|---|---|
| Country | Spain |
| Primary Legislation | LGSS; Real Decreto-ley 13/2022 (income-based system) |
| Supporting Legislation | Orden PJC/178/2025 (2025 rates); Ley 20/2007 (Estatuto Trabajo Autonomo); Ley 35/2006 IRPF |
| Tax Authority | Tesoreria General de la Seguridad Social (TGSS) |
| Currency | EUR only |
| Total contribution rate (2025) | 31.40% |
| Tarifa plana (new autonomos) | EUR 80/month (first 12 months) |
| Payment frequency | Monthly (last business day of current month) |
| Payment method | Domiciliacion bancaria (direct debit) -- mandatory |
| 15 income tranches | Tranche 1 (<=EUR 670/mo) to Tranche 15 (>EUR 6,000/mo) |
| Maximum base (2025) | EUR 4,909.50/month |
| Autonomo societario minimum | EUR 1,000.00/month |
| Base change windows | 6 per year (Feb, Apr, Jun, Aug, Oct, Dec) |
| Regularisation | Automatic after IRPF filing |
| Contributor | Open Accountants |
| Validated by | Pending -- requires sign-off by qualified asesor fiscal |
| Validation date | Pending |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown persona fisica vs societario | Ask -- minimum base rules differ |
| Unknown net income estimate | STOP -- income estimate required for tranche |
| Unknown whether first-time autonomo | Ask -- tarifa plana eligibility |
| Unknown 7% vs 3% deduction | Apply 7% (persona fisica default); 3% for societarios |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- type (persona fisica or societario), estimated monthly net income (rendimientos netos), and whether first registration.

**Recommended** -- bank statements showing TGSS debits, date of alta, prior RETA registration history, IRPF declaration.

**Ideal** -- complete IRPF data, TGSS Informe de Bases de Cotizacion, alta/baja history.

### Refusal catalogue

**R-ES-SC-1 -- Disability regimes.** *Trigger:* client has disability affecting contribution rates. *Message:* "Disability contribution regimes require case-specific TGSS assessment. Escalate."

**R-ES-SC-2 -- Cross-border posted workers.** *Trigger:* client posted from another EU country. *Message:* "EU social security coordination applies. Escalate."

**R-ES-SC-3 -- Mutuas MATEPSS specifics.** *Trigger:* client asks about specific Mutua benefits or coverage details. *Message:* "Mutua-specific benefit calculations are out of scope. Contact the relevant Mutua."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to RETA contributions.

### 3.1 TGSS direct debits (monthly cuota)

| Pattern | Treatment | Notes |
|---|---|---|
| TGSS, TESORERIA GENERAL | EXCLUDE -- RETA cuota | Monthly autonomo contribution |
| SEGURIDAD SOCIAL, SS | EXCLUDE -- RETA cuota | Alternative description |
| CUOTA AUTONOMOS | EXCLUDE -- RETA cuota | Explicit cuota reference |
| RETA, REG ESP TRAB AUTONOMOS | EXCLUDE -- RETA cuota | Regime name reference |
| DOMICILIACION TGSS | EXCLUDE -- RETA cuota | Direct debit description |

### 3.2 Regularisation payments (TGSS demands additional cuotas)

| Pattern | Treatment | Notes |
|---|---|---|
| TGSS REGULARIZACION | EXCLUDE -- RETA regularisation | Additional cuotas demanded after IRPF filing |
| TGSS COMPLEMENTO | EXCLUDE -- RETA adjustment | Adjustment to provisional base |

### 3.3 TGSS refunds (overpayment)

| Pattern | Treatment | Notes |
|---|---|---|
| TGSS DEVOLUCION | EXCLUDE -- RETA refund | Refund of excess cuotas |
| TGSS REINTEGRO | EXCLUDE -- RETA refund | Same |

### 3.4 Tarifa plana payments

| Pattern | Treatment | Notes |
|---|---|---|
| TGSS (amount ~EUR 80) | EXCLUDE -- tarifa plana cuota | Consistent EUR 80/month = tarifa plana |

### 3.5 Tax authority (NOT RETA)

| Pattern | Treatment | Notes |
|---|---|---|
| AEAT, AGENCIA TRIBUTARIA | EXCLUDE -- income tax/VAT | Not social contributions |
| HACIENDA | EXCLUDE -- tax | Not RETA |
| IVA, IRPF (tax reference) | EXCLUDE -- tax | Not RETA |

### 3.6 Employee social security (employer obligations)

| Pattern | Treatment | Notes |
|---|---|---|
| TGSS REGIMEN GENERAL | EXCLUDE -- employee SS | Employer's obligation for employees, not the autonomo's own RETA |
| TC1, TC2 (payroll references) | EXCLUDE -- payroll SS | Employer obligations |

---

## Section 4 -- Worked examples

Six bank statement classifications for a hypothetical Spanish self-employed web developer.

### Example 1 -- Standard monthly RETA cuota (TGSS direct debit)

**Input line:**
`30.04.2025 ; TGSS TESORERIA GENERAL ; ADEUDO ; CUOTA AUTONOMOS ABR 2025 ; -425.85 ; EUR`

**Reasoning:**
Matches "TGSS" + "CUOTA AUTONOMOS" (pattern 3.1). Amount EUR 425.85 = Tranche 10 minimum base (EUR 1,356.21) x 31.40%. Monthly RETA cuota for April 2025, debited on last business day of April. Exclude from VAT.

**Classification:** EXCLUDE -- RETA cuota. 100% deductible as gasto deducible in IRPF.

### Example 2 -- Tarifa plana cuota (new autonomo)

**Input line:**
`31.03.2025 ; TGSS ; ADEUDO ; CUOTA TARIFA PLANA MAR ; -80.00 ; EUR`

**Reasoning:**
Matches "TGSS" (pattern 3.1). Amount EUR 80.00 = tarifa plana flat rate. New autonomo in first 12 months. Covers all contingencies.

**Classification:** EXCLUDE -- tarifa plana RETA cuota. Deductible (EUR 80 x 12 = EUR 960/year).

### Example 3 -- Regularisation demand from TGSS

**Input line:**
`25.09.2025 ; TGSS REGULARIZACION ; ADEUDO ; COMPLEMENTO CUOTAS 2024 ; -2,413.54 ; EUR`

**Reasoning:**
Matches "TGSS REGULARIZACION" (pattern 3.2). After 2024 IRPF filing, TGSS determined actual income placed the autonomo in a higher tranche than the provisional base used. This is the additional cuotas demanded. Due by last day of month following notification.

**Classification:** EXCLUDE -- RETA regularisation demand. Deductible in 2025 (year paid, not 2024).

### Example 4 -- TGSS refund (overpaid cuotas)

**Input line:**
`15.10.2025 ; TGSS DEVOLUCION ; ABONO ; DEVOLUCION CUOTAS 2024 ; +1,907.45 ; EUR`

**Reasoning:**
Matches "TGSS DEVOLUCION" (pattern 3.3). TGSS refunding excess cuotas because actual income was in a lower tranche. This is a CREDIT. Taxable as income in the IRPF year received (2025).

**Classification:** EXCLUDE from VAT. Taxable income in 2025 IRPF (refund of previously deducted cuotas).

### Example 5 -- AEAT tax payment (NOT RETA)

**Input line:**
`20.04.2025 ; AGENCIA TRIBUTARIA ; ADEUDO ; PAGO FRACCIONADO IRPF ; -1,500.00 ; EUR`

**Reasoning:**
Matches "AGENCIA TRIBUTARIA" (pattern 3.5). This is a quarterly IRPF instalment (pago fraccionado), NOT a social contribution. Do not classify as RETA.

**Classification:** EXCLUDE -- income tax. NOT RETA.

### Example 6 -- Employer TGSS payment (not autonomo's own RETA)

**Input line:**
`30.04.2025 ; TGSS REGIMEN GENERAL ; ADEUDO ; SS EMPLEADOS ABR ; -2,800.00 ; EUR`

**Reasoning:**
Matches "TGSS REGIMEN GENERAL" (pattern 3.6). This is the employer's social security obligation for their employees under the General Regime. It is NOT the autonomo's own RETA cuota.

**Classification:** EXCLUDE -- employer SS for employees. Not the autonomo's personal RETA contribution.

---

## Section 5 -- Tier 1 rules

### Rule 1 -- Net income formula for tranche determination

```
Rendimientos netos = Ingresos computables - Gastos deducibles
Rendimientos netos RETA = Rendimientos netos - 7% deduccion generica (3% for societarios)
Monthly net = Rendimientos netos RETA / 12
```

### Rule 2 -- 2025 tranche table (15 tranches)

**Tabla Reducida (Tranches 1-3):**

| Tranche | Monthly Net (EUR) | Min. Base (EUR) | Approx. Min. Cuota (EUR/month) |
|---|---|---|---|
| 1 | <= 670 | 653.59 | ~200 |
| 2 | 670.01-900.00 | 718.95 | ~220 |
| 3 | 900.01-1,125.90 | 849.67 | ~260 |

**Tabla General (Tranches 4-15):**

| Tranche | Monthly Net (EUR) | Min. Base (EUR) | Approx. Min. Cuota (EUR/month) |
|---|---|---|---|
| 4 | 1,125.91-1,300.00 | 950.98 | ~291 |
| 5 | 1,300.01-1,500.00 | 960.78 | ~294 |
| 6 | 1,500.01-1,700.00 | 960.78 | ~294 |
| 7 | 1,700.01-1,850.00 | 1,143.79 | ~350 |
| 8 | 1,850.01-2,030.00 | 1,209.15 | ~370 |
| 9 | 2,030.01-2,330.00 | 1,274.51 | ~390 |
| 10 | 2,330.01-2,760.00 | 1,356.21 | ~415 |
| 11 | 2,760.01-3,190.00 | 1,437.91 | ~440 |
| 12 | 3,190.01-3,620.00 | 1,519.61 | ~465 |
| 13 | 3,620.01-4,050.00 | 1,601.31 | ~490 |
| 14 | 4,050.01-6,000.00 | 1,732.03 | ~530 |
| 15 | > 6,000.00 | 1,928.10 | ~590 |

Maximum base for all tranches: EUR 4,909.50/month.

### Rule 3 -- Contribution rate breakdown (2025)

| Concept | Rate |
|---|---|
| Contingencias comunes | 28.30% |
| Contingencias profesionales | 1.30% |
| Cese de actividad | 0.90% |
| Formacion profesional | 0.10% |
| MEI | 0.80% |
| **Total** | **31.40%** |

### Rule 4 -- Cuota formula

```
Cuota mensual = Base de cotizacion elegida x 31.40%
```

### Rule 5 -- Tarifa plana

EUR 80/month for first 12 months. Extendable 12 more months if first-year income < SMI. Eligibility: no RETA registration in prior 2 years (3 years if previously received tarifa plana). Must apply at time of alta.

### Rule 6 -- Autonomo societario minimum

EUR 1,000/month regardless of tranche. Min cuota: ~EUR 314/month.

### Rule 7 -- Payment schedule

Monthly. Due: last business day of current month. Mandatory domiciliacion bancaria. Late surcharge: 10% first month, 20% thereafter.

### Rule 8 -- Base change windows (6 per year)

Submit by: end Feb (effective 1 Mar), end Apr (1 May), end Jun (1 Jul), end Aug (1 Sep), end Oct (1 Nov), end Dec (1 Jan).

### Rule 9 -- Annual regularisation (automatic)

After IRPF filed, TGSS compares actual vs provisional. Underpayment: TGSS demands additional cuotas. Overpayment: TGSS refunds automatically. Additional cuotas deductible in year paid. Refunds taxable in year received.

### Rule 10 -- Tax deductibility

RETA cuotas: 100% deductible as gasto deducible in IRPF. Tarifa plana cuotas: also deductible. Late surcharges and penalties: NOT deductible.

---

## Section 6 -- Tier 2 catalogue

### T2-1 -- Pluriactividad (simultaneous employment + RETA)

**Trigger:** Client works as employee (Regimen General) and self-employed (RETA) simultaneously.
**Issue:** Must pay into both regimes. Reduction in RETA base may apply if combined contributions exceed thresholds. Potential 50% refund of excess.
**Action:** Flag for reviewer -- case-specific calculation required.

### T2-2 -- Autonomo over age 47

**Trigger:** Client aged 47+ wants specific base election.
**Issue:** Transitional provisions from pre-2023 system may restrict base choice.
**Action:** Flag for reviewer.

### T2-3 -- Large regularisation demand

**Trigger:** TGSS demands significant additional cuotas (estimated tranche far below actual).
**Issue:** Payment due by last day of month following notification. Aplazamiento possible.
**Action:** Flag for reviewer to advise on aplazamiento and whether income estimate was reasonable.

### T2-4 -- Mid-year alta (pro-rata)

**Trigger:** Client registers mid-month.
**Issue:** First month cuota pro-rated from date of alta. Tarifa plana runs from exact alta date, not first of month.
**Action:** Confirm exact alta date.

### T2-5 -- Tarifa plana extension rejected

**Trigger:** First-year income exceeded SMI.
**Issue:** Extension denied. From month 13, full tranche-based cuota applies.
**Action:** Confirm income level and transition to full cuota.

---

## Section 7 -- Excel working paper template

```
SPAIN RETA CONTRIBUTIONS -- WORKING PAPER
Client: [name]
Tax Year: [year]
Prepared: [date]

INPUT DATA
  Type:                          [Persona fisica / Autonomo societario]
  Gross annual revenue:          EUR [____]
  Deductible expenses:           EUR [____]
  Net income before deduction:   EUR [____]
  Generic deduction (7%/3%):     EUR [____]
  Net income for RETA:           EUR [____]
  Monthly net:                   EUR [____]
  Applicable tranche:            [____]
  Tarifa plana eligible:         [YES/NO]
  Date of alta:                  [____]

CUOTA COMPUTATION
  Chosen base (min of tranche):  EUR [____]
  Rate:                          31.40%
  Monthly cuota:                 EUR [____]
  Annual cuota (12 months):      EUR [____]

OR TARIFA PLANA
  Monthly cuota:                 EUR 80.00
  Annual (12 months):            EUR 960.00

REGULARISATION ESTIMATE
  Actual tranche (post-IRPF):    [____]
  Actual min base:               EUR [____]
  Difference per month:          EUR [____]
  Annual adjustment:             EUR [____]
  Direction: [DEMAND / REFUND]

IRPF DEDUCTIBILITY
  Total cuotas paid:             EUR [____]
  Deductible as gasto deducible: EUR [____]

REVIEWER FLAGS
  [List any Tier 2 flags]
```

---

## Section 8 -- Bank statement reading guide

### How RETA payments appear on Spanish bank statements

**TGSS direct debits:**
- Description: "TGSS", "TESORERIA GENERAL", "SEGURIDAD SOCIAL", "CUOTA AUTONOMOS"
- Timing: Last business day of each month (current month payment)
- Amount: Consistent monthly amount (unless base changed)
- Tarifa plana: exactly EUR 80.00

**Regularisation payments:**
- Description: "TGSS REGULARIZACION", "COMPLEMENTO CUOTAS"
- Timing: After IRPF filing (typically Sep-Dec)
- Amount: Can be large if tranche mismatch

**Refunds:**
- Description: "TGSS DEVOLUCION", "TGSS REINTEGRO"
- Direction: CREDIT (incoming)
- Amount: Varies

**Key identification tips:**
1. RETA is MONTHLY, not quarterly -- look for consistent end-of-month debits
2. EUR 80 monthly = tarifa plana (new autonomo)
3. Amounts around EUR 200-600 = standard tranche cuotas
4. AEAT debits are tax, not social security
5. "REGIMEN GENERAL" debits are employer SS for employees, not the autonomo's RETA

---

## Section 9 -- Onboarding fallback

If the client provides only a bank statement:

1. **Scan for TGSS debits** -- identify monthly pattern and amount
2. **Identify tarifa plana** -- consistent EUR 80/month indicates new autonomo
3. **Estimate tranche from cuota amount:**
   - ~EUR 200 = Tranche 1
   - ~EUR 300 = Tranche 4-6
   - ~EUR 400-415 = Tranche 9-10
   - ~EUR 530 = Tranche 14
   - ~EUR 590 = Tranche 15
4. **Look for regularisation** -- large TGSS debit or credit mid-year
5. **Flag:** "RETA tranche estimated from cuota amount on bank statement. Actual income and chosen base have not been independently verified. Reviewer must confirm before IRPF filing."

---

## Section 10 -- Reference material

### Net income example

| Item | EUR |
|---|---|
| Gross annual revenue | 48,000 |
| Deductible expenses | 12,000 |
| Net before deduction | 36,000 |
| 7% generic deduction | 2,520 |
| Net for RETA | 33,480 |
| Monthly | 2,790 |
| Tranche | 11 (EUR 2,760.01-3,190.00) |
| Min base | EUR 1,437.91 |
| Min cuota | ~EUR 451/month |

### Cese de actividad (cessation benefit)

70% of average contribution base of last 12 months. 4-24 months duration. Must have 12 months continuous contribution in prior 24. Voluntary cessation does NOT qualify.

### IT (sick leave) coverage

Days 4-20: 60% of regulatory base. Day 21+: 75%. Days 1-3 not covered. Higher chosen base = higher daily benefit.

### Test suite

**Test 1:** Persona fisica, monthly net EUR 2,100. -> Tranche 9. Min base EUR 1,274.51. Cuota: EUR 400.20/month.

**Test 2:** New autonomo, tarifa plana. -> EUR 80/month for 12 months.

**Test 3:** Societario, monthly net EUR 800. -> Societario minimum EUR 1,000. Cuota: EUR 314/month.

**Test 4:** High earner, monthly net EUR 8,000. -> Tranche 15. Min base EUR 1,928.10. Cuota: EUR 605.42/month.

**Test 5:** Regularisation underpaid: chose Tranche 5 (EUR 960.78), actual Tranche 13 (EUR 1,601.31). -> Additional EUR 201.13/month = EUR 2,413.54/year.

**Test 6:** Regularisation overpaid: chose Tranche 10 (EUR 1,356.21), actual Tranche 3 (EUR 849.67). -> Refund EUR 158.95/month = EUR 1,907.45/year.

**Test 7:** Net income calc: EUR 60,000 gross, EUR 15,000 expenses. -> EUR 41,850 after 7%. Monthly EUR 3,487.50. Tranche 12. Min cuota EUR 477.16.

**Test 8:** Deductibility: paid EUR 4,800 cuotas. -> 100% deductible in IRPF.

### Prohibitions

- NEVER compute without knowing persona fisica vs societario
- NEVER use gross income for tranche -- always apply 7%/3% deduction first
- NEVER tell client they can avoid RETA once registered
- NEVER present tarifa plana as automatic -- must apply at alta
- NEVER ignore regularisation
- NEVER advise on pluriactividad without reviewer
- NEVER present cuotas as exact without specifying chosen base
- NEVER confuse monthly payment with quarterly
- NEVER advise late surcharges are deductible
- NEVER compute IT benefits without knowing actual base of month prior to baja

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal, gestor administrativo, or equivalent licensed practitioner in Spain) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
