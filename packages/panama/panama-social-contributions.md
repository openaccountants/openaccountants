---
name: panama-social-contributions
description: Use this skill whenever asked about Panama social security and payroll contributions (Caja de Seguro Social / CSS) for employees, employers, or self-employed independent professionals. Trigger on phrases like "Panama CSS contributions", "Caja de Seguro Social", "cuota obrero-patronal", "seguro educativo", "how much social security do I pay in Panama", "Panama payroll taxes", "Law 462 / Ley 462 CSS reform", "Panama employer contribution rate", "self-employed CSS Panama", "IVM contribution", "Panama planilla", or any question about Panama CSS, educational insurance tax, or payroll obligations. Also trigger when classifying bank-statement transactions that relate to CSS debits, seguro educativo, planilla payments, or DGI tax payments from Banco General, Banistmo, BAC, or other Panamanian banks. Also trigger when Panama personal income tax (Impuesto sobre la Renta) withholding or the territorial-income rules are relevant. This skill covers employee/employer CSS rates, the Law 462 staggered employer-rate increase, educational insurance tax, self-employed IVM/health rates, the (lack of) contribution ceiling, late-payment surcharges, interaction with territorial income tax, the 13th month, minimum wage context, bank-statement classification patterns, and edge cases. ALWAYS read this skill before touching any Panama CSS or payroll work.
version: 0.1
jurisdiction: PA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Panama Social Security Contributions (CSS) -- Payroll & Self-Employed

## Section 1 -- Quick reference

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Panama (Republic of Panama) |
| Currency | US Dollar (USD); local unit "Balboa" (B/.) pegged 1:1 to USD — figures interchangeable |
| Primary Legislation | Ley 51 (CSS organic law); **Ley 462 of 18 Mar 2025** (CSS reform) |
| Supporting Legislation | Educational Insurance Tax (Seguro Educativo); Código Fiscal (Impuesto sobre la Renta) |
| Social-insurance authority | Caja de Seguro Social (CSS) |
| Tax authority | Dirección General de Ingresos (DGI), Ministerio de Economía y Finanzas (MEF) |
| Minimum-wage authority | Ministerio de Trabajo y Desarrollo Laboral (MITRADEL) |
| Employee CSS rate | **9.75%** of gross (unchanged by Ley 462) [PwC; Ley 462] |
| Employee educational insurance | **1.25%** of gross [PwC] |
| Employer CSS rate (1 Apr 2025) | **13.25%** of gross [Ley 462; MEF] |
| Employer educational insurance | **1.50%** of gross [PwC] |
| Contribution ceiling | **None** — no maximum taxable amount for CSS or educational insurance [PwC] |
| Self-employed IVM (mandatory) | **9.36%** of declared income [Ley 462; Morgan & Morgan] |
| Personal income tax | Territorial — Panama-source income only; 0% / 15% / 25% bands [PwC] |
| 13th month (Décimo) | Mandatory; paid 15 Apr, 15 Aug, 15 Dec [Código de Trabajo] |
| Validated by | Pending — requires sign-off by a Panamanian-qualified accountant (Contador Público Autorizado) |
| Validation date | Pending |

**Cuota obrero-patronal overview (current period, from 1 Apr 2025)**

| Component | Employee | Employer |
| --- | --- | --- |
| CSS social security (Seguro Social) | 9.75% | 13.25% [Ley 462; MEF] |
| Educational Insurance Tax (Seguro Educativo) | 1.25% | 1.50% [PwC] |
| **Total** | **11.00%** | **14.75%** |

*Arithmetic check: employee 9.75 + 1.25 = 11.00%. Employer 13.25 + 1.50 = 14.75%. Combined obrero-patronal load = 11.00 + 14.75 = 25.75% of gross, with no ceiling.*

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown payroll period (which Ley 462 employer rate applies) | Use the rate in force for the actual payroll month; for current work use 13.25% employer CSS |
| Unknown worker status (employee vs independent) | Ask — do NOT assume; employee and self-employed regimes differ entirely |
| Unknown whether self-employed opted into health coverage | Apply mandatory IVM 9.36% only; flag health 8.5% as optional |
| Décimo (13th month) CSS treatment | STOP — do not compute CSS on the décimo without confirmation [RESEARCH GAP — reviewer to confirm] |
| Income source unclear (Panama-source vs foreign) | Treat as foreign-source EXEMPT only with evidence; otherwise flag for reviewer |
| Late-payment surcharge schedule | Flag for reviewer — verify live CSS Reglamento; relief periods may suspend surcharges |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- worker status (employee vs self-employed independent) and gross monthly remuneration. Without worker status, STOP. The employee and self-employed CSS regimes are entirely different.

**Recommended** -- the payroll month/period (because the employer CSS rate changes under Ley 462 over time), and whether a self-employed worker has opted into voluntary health coverage.

**Ideal** -- the CSS planilla (payroll filing), bank statements showing CSS and seguro educativo debits, and (for income tax) the RUC registration and source classification of income (Panama-source vs foreign-source).

### Refusal catalogue

- **R-PA-CSS-1 -- Worker status unknown** — Trigger: not stated whether the person is an employee or a self-employed independent. Message: "Worker status is mandatory. Employees pay 9.75% CSS + 1.25% educational insurance with a matching employer contribution; self-employed independents pay 9.36% IVM (mandatory) with optional 8.5% health. Cannot proceed without confirming status."
- **R-PA-CSS-2 -- Décimo Tercer Mes (13th month) CSS treatment** — Trigger: request to compute CSS on the 13th-month payment. Message: "The CSS/withholding treatment of the décimo differs from ordinary wages and was not confirmed from a single authoritative source in research [RESEARCH GAP — reviewer to confirm]. Do not compute CSS on the décimo. Escalate to a Panamanian accountant."
- **R-PA-CSS-3 -- Late-payment surcharges / mora** — Trigger: delinquent employer contributions, recargos, or mora quantification. Message: "CSS surcharge escalation (2/5/10/15%) and 1%/month interest under Ley 51 come from secondary summaries; relief periods have at times suspended surcharges. Do not quantify mora without the live CSS Reglamento General de Ingresos and a CSS statement. Non-payment can be a criminal offense. Escalate immediately."
- **R-PA-CSS-4 -- Income-tax penalties / return form** — Trigger: request for the exact income-tax return form number or late-filing/late-payment income-tax penalties. Message: "The specific Declaración Jurada de Rentas form number and income-tax penalty percentages were not confirmed from DGI in research [RESEARCH GAP — reviewer to confirm]. Source these from dgi.mef.gob.pa before advising."
- **R-PA-CSS-5 -- Future-dated employer rates** — Trigger: a computation for a payroll period on/after 1 Mar 2027 or 1 Mar 2029. Message: "Employer CSS rates of 14.25% (from 1 Mar 2027) and 15.25% (from 1 Mar 2029) are scheduled future rates under Ley 462. Confirm no further legislative change before applying. Flag for reviewer."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank-statement transactions related to Panama social insurance and payroll tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. CSS and educational-insurance payments EXCLUDE from any ITBMS (VAT) return — they are statutory payroll/personal obligations, not taxable supplies.

### 3.1 CSS contribution debits (cuota obrero-patronal)

**CSS contribution debits table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CSS, CAJA DE SEGURO SOCIAL | EXCLUDE -- CSS payment | Monthly obrero-patronal contribution |
| SEGURO SOCIAL, SEG SOCIAL | EXCLUDE -- CSS payment | Same |
| CUOTA OBRERO PATRONAL, OBRERO-PATRONAL | EXCLUDE -- CSS payment | Combined employee+employer remittance |
| PLANILLA CSS, PLANILLA | EXCLUDE -- CSS payroll filing payment | Monthly payroll remittance |
| IVM | EXCLUDE -- CSS (self-employed IVM) | Independent-worker mandatory contribution |

### 3.2 Educational insurance tax (Seguro Educativo)

**Educational insurance tax table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SEGURO EDUCATIVO, SEG EDUCATIVO | EXCLUDE -- educational insurance tax | 1.25% employee / 1.50% employer |
| EDUCATIVO | EXCLUDE -- educational insurance tax | Abbreviated reference |

### 3.3 DGI / income-tax payments (NOT CSS -- do not confuse)

**DGI / income-tax payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DGI, DIRECCION GENERAL DE INGRESOS | EXCLUDE -- income tax, not CSS | DGI tax remittance |
| IMPUESTO SOBRE LA RENTA, ISR | EXCLUDE -- income tax | Not social security |
| ITBMS | EXCLUDE -- VAT (ITBMS), not CSS | Indirect tax, separate return |
| RETENCION, RETENCIÓN | EXCLUDE -- withholding (likely income tax) | Confirm — not CSS |

### 3.4 Salary and payroll (exclude from CSS classification)

**Salary and payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SALARIO, SUELDO, PLANILLA NETA (outgoing) | EXCLUDE -- payroll expense | Net wage, not a CSS payment |
| DECIMO, DÉCIMO, DECIMO TERCER MES | EXCLUDE -- 13th-month payment | Statutory; CSS treatment flagged separately |
| SALARIO, SUELDO (incoming) | EXCLUDE -- employment income received | Not a CSS payment |

### 3.5 Pension payments (received -- not CSS contributions)

**Pension payments table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION CSS, JUBILACION | EXCLUDE -- pension income received | Not a contribution payment |
| PENSION VEJEZ, IVM PENSION | EXCLUDE -- pension income | Not a contribution |

## Section 4 -- Worked examples

Six bank-statement classifications and payroll computations for a hypothetical Panama City employer and a self-employed consultant. All figures in USD/Balboa (1:1).

### Example 1 -- Standard employee CSS + educational insurance (employer remittance)

**Scenario:** Employee gross salary B/.1,500.00/month, payroll period May 2025 (employer rate 13.25%).

**Computation:**
- Employee CSS 9.75% × 1,500 = **146.25**
- Employee educational 1.25% × 1,500 = **18.75**
- Employee total withheld = 146.25 + 18.75 = **165.00**
- Employer CSS 13.25% × 1,500 = **198.75**
- Employer educational 1.50% × 1,500 = **22.50**
- Employer total = 198.75 + 22.50 = **221.25**
- Total remitted to CSS/DGI for this employee = 165.00 + 221.25 = **386.25**

**Input line:**
`31.05.2025 ; CAJA DE SEGURO SOCIAL ; DEBITO ; PLANILLA MAYO ; -386.25 ; USD`

**Classification:** EXCLUDE -- CSS + educational insurance remittance. No ceiling applies.

### Example 2 -- Higher-salary employee (no ceiling)

**Scenario:** Employee gross salary B/.2,000.00/month, payroll period 2025.

**Computation:**
- Employee CSS 9.75% × 2,000 = **195.00**; educational 1.25% × 2,000 = **25.00**; employee total = **220.00**
- Employer CSS 13.25% × 2,000 = **265.00**; educational 1.50% × 2,000 = **30.00**; employer total = **295.00**

Because Panama has **no contribution ceiling** [PwC], the same percentages apply no matter how high the salary rises — there is no cap on the taxable base.

**Classification:** EXCLUDE -- CSS payroll. Note the absence of a ceiling distinguishes Panama from capped systems.

### Example 3 -- Self-employed independent, mandatory IVM only

**Scenario:** Independent consultant declares B/.3,000.00/month, opts NOT to take voluntary health coverage. Affiliation mandatory under Ley 462.

**Computation:**
- IVM 9.36% × 3,000 = **280.80/month** (mandatory) [Ley 462; Morgan & Morgan]
- Health & maternity 8.5% — NOT elected (voluntary; requires min declared income B/.800)

**Input line:**
`30.06.2025 ; CAJA DE SEGURO SOCIAL ; DEBITO ; IVM INDEPENDIENTE ; -280.80 ; USD`

**Classification:** EXCLUDE -- self-employed CSS (IVM). Health 8.5% not applied (voluntary, not elected).

### Example 4 -- Self-employed independent, with voluntary health coverage

**Scenario:** Same consultant, declares B/.3,000.00/month, ELECTS voluntary health & maternity coverage.

**Computation:**
- IVM 9.36% × 3,000 = **280.80**
- Health & maternity 8.5% × 3,000 = **255.00**
- Total self-employed CSS = 280.80 + 255.00 = **535.80/month**

**Classification:** EXCLUDE -- self-employed CSS (IVM + voluntary health). Confirm the declared-income base on which the worker elected to contribute.

### Example 5 -- DGI income-tax payment (NOT CSS)

**Scenario:** Self-employed taxpayer pays estimated income tax (3 installments: 30 Jun, 30 Sep, 31 Dec). Panama-source net income B/.30,000/year.

**Computation (annual PIT, 2025 bands):**
- Band 0–11,000: 0
- Band 11,000–50,000 at 15%: (30,000 − 11,000) × 15% = 19,000 × 15% = **2,850.00** [PwC]
- One estimated installment ≈ 2,850 / 3 = **950.00**

**Input line:**
`30.06.2025 ; DIRECCION GENERAL DE INGRESOS ; DEBITO ; ISR ESTIMADO ; -950.00 ; USD`

**Classification:** EXCLUDE -- income tax (DGI), NOT CSS. Income tax is territorial and separate from social insurance.

### Example 6 -- Ambiguous CSS debit (possible mora / surcharge)

**Input line:**
`15.09.2025 ; CAJA DE SEGURO SOCIAL ; DEBITO ; CONVENIO DE PAGO ; -1,250.00 ; USD`

**Reasoning:**
Matches "CAJA DE SEGURO SOCIAL" (3.1) but reference says "CONVENIO DE PAGO" (payment agreement for delinquent contributions). The amount may include surcharges (2/5/10/15%) and 1%/month interest under Ley 51 [La Estrella; CSS Reglamento — RESEARCH GAP, verify schedule]. Cannot separate principal from surcharge without a CSS statement.

**Classification:** EXCLUDE from ITBMS. Flag for reviewer -- request CSS breakdown to split contribution principal from surcharge/interest. Non-payment can be a criminal offense under Ley 51.

## Section 5 -- Tier 1 rules

Apply these when data is clear and all required inputs are available.

### Rule 1 -- Employee contribution formula

- **Employee withholding formula** — Employee withholding = gross × (9.75% CSS + 1.25% educational) = gross × 11.00%. No ceiling on the base.  _([PwC; Ley 462])_

### Rule 2 -- Employer contribution formula (Ley 462 staggered)

- **Employer load formula** — Employer load = gross × (CSS rate for the period + 1.50% educational)

**Employer CSS staggered schedule**

| Period | Employer CSS | + Educational | = Employer total |
| --- | --- | --- | --- |
| 1 Apr 2025 – 28 Feb 2027 | 13.25% | 1.50% | **14.75%** [Ley 462; MEF] |
| 1 Mar 2027 – 28 Feb 2029 | 14.25% | 1.50% | **15.75%** (future-dated) [Ley 462] |
| From 1 Mar 2029 | 15.25% | 1.50% | **16.75%** (future-dated) [Ley 462] |

*The employer CSS rate was 12.25% before Ley 462; the reform raises it by 3 points in three steps. Employee rate unchanged at 9.75%.*

### Rule 3 -- No contribution ceiling

- **No contribution ceiling** — There is no maximum taxable amount for either CSS or the educational insurance tax. The percentage applies to the full gross, however high.  _([PwC])_

### Rule 4 -- Self-employed independents (Ley 462)

- **Self-employed affiliation and rates** — Affiliation is mandatory for independent workers and professional-service providers. IVM (Invalidez, Vejez y Muerte) = 9.36% of declared income (mandatory). Health & maternity = 8.5% (voluntary; minimum declared monthly income B/.800 to opt in).  _([Ley 462; Morgan & Morgan; Pension Policy International])_

### Rule 5 -- Educational insurance is separate from CSS

- **Educational insurance separate levy** — Seguro Educativo (1.25% employee / 1.50% employer) is a distinct payroll levy from the CSS social-security contribution but is remitted on the same gross base with no ceiling.  _([PwC])_

### Rule 6 -- Personal income tax is territorial

- **Territorial income tax** — Only Panama-source income is taxed. Foreign-source income is exempt for residents and non-residents alike. There are no local/municipal income taxes.  _([PwC])_

### Rule 7 -- Income-tax bands (2025)

**Income-tax bands table (Rule 7)**  _([PwC])_

| Taxable income (USD) | Cumulative tax at top of band | Rate on excess |
| --- | --- | --- |
| 0 – 11,000 | 0 | 0% |
| 11,000 – 50,000 | 5,850 | 15% (on amount over 11,000) |
| Over 50,000 | — | 25% |

*Cumulative check: at 50,000 → (50,000 − 11,000) × 15% = 39,000 × 15% = 5,850. ✓* [PwC]

### Rule 8 -- Who must file income tax

- **Filing requirement** — All taxpayers EXCEPT employees with a single source of wage income whose tax is fully withheld monthly by the employer. Self-employed/independent professionals must file. Filing via DGI eTax 2; taxpayers hold a RUC (Registro Único de Contribuyente).  _([PwC])_

### Rule 9 -- Income-tax deadlines

**Income-tax deadlines table**

| Item | Date |
| --- | --- |
| Tax year | Calendar year (1 Jan – 31 Dec) [PwC] |
| Return due | **15 March** following year; 2-month extension to **15 May** generally available [PwC] |
| Estimated tax (filers) | 3 equal installments: **30 Jun, 30 Sep, 31 Dec** [PwC] |

### Rule 10 -- 13th month (Décimo Tercer Mes)

- **13th month payment schedule and CSS treatment** — Mandatory under the Código de Trabajo, paid in three installments: 15 April, 15 August, 15 December. The décimo is subject to its own CSS/withholding rules that differ from ordinary wages. The exact CSS rate on the décimo is [RESEARCH GAP — reviewer to confirm]; do not compute it here.  _([Código de Trabajo])_

### Rule 11 -- CSS late-payment surcharges (mora)

**CSS late-payment surcharge schedule**  _([CSS Reglamento; La Estrella — verify, RESEARCH GAP])_

| Delinquency period | Surcharge |
| --- | --- |
| First 10 calendar days | 2% |
| Days 11–20 | 5% |
| After 30 days | 10% |
| Day 31 | 15% |

Non-payment can become a criminal offense under Ley 51; convenios de pago are available. Do not quantify without the live CSS Reglamento and a CSS statement.

## Section 6 -- Tier 2 catalogue

Flag these for reviewer confirmation when data is ambiguous or circumstances are unclear.

### T2-1 -- Payroll spanning a Ley 462 rate-change boundary

- **T2-1** — Trigger: Payroll period straddles 1 Mar 2027 or 1 Mar 2029. Issue: Employer CSS rate steps from 13.25% → 14.25% → 15.25%. Future rates are scheduled, not yet in force. Action: Flag for reviewer; confirm the rate in force for the exact payroll month and that no further legislative change has occurred.

### T2-2 -- Self-employed health-coverage election

- **T2-2** — Trigger: Independent worker unclear on whether they opted into voluntary 8.5% health coverage. Issue: IVM 9.36% is mandatory; health 8.5% is voluntary and needs minimum declared income B/.800. Action: Flag for reviewer; apply mandatory IVM only until election is confirmed.

### T2-3 -- Declared-income base for independents

- **T2-3** — Trigger: Independent worker voluntarily declares the income on which they contribute. Issue: The declared base (within CSS rules) drives the contribution; it may differ from actual earnings. Action: Flag for reviewer to confirm the declared base used.

### T2-4 -- Income source classification (Panama-source vs foreign)

- **T2-4** — Trigger: Income may be foreign-source (exempt) or Panama-source (taxable). Issue: Panama's territorial system exempts foreign-source income; misclassification mis-states income tax. Action: Flag for reviewer. Do not treat income as exempt without evidence of foreign source.

### T2-5 -- CSS arrears / convenio de pago

- **T2-5** — Trigger: Delinquent contributions, surcharges, or a payment agreement appear. Issue: Surcharge schedule and 1%/month interest require the live CSS Reglamento; relief periods may suspend surcharges; non-payment can be criminal. Action: Do not quantify. Escalate to a Panamanian accountant immediately.

### T2-6 -- Décimo Tercer Mes CSS treatment

- **T2-6** — Trigger: 13th-month payment in scope for CSS. Issue: Décimo CSS/withholding differs from ordinary wages; exact rate unconfirmed [RESEARCH GAP]. Action: Flag for reviewer; source from CSS / Código de Trabajo before computing.

## Section 7 -- Excel working paper template

```
PANAMA CSS / PAYROLL COMPUTATION -- WORKING PAPER
Client: [name]                    RUC: [____]
Period: [month/year]              Prepared: [date]

INPUT DATA
  Worker status:                 [Employee / Self-employed independent]
  Gross monthly remuneration:    USD [____]
  Payroll month (Ley 462 rate):  [____]   Employer CSS rate: [13.25 / 14.25 / 15.25]%
  Self-employed health elected:  [YES / NO / N/A]
  Declared base (if independent): USD [____]

EMPLOYEE COMPUTATION (if employee)
  CSS 9.75% × gross:             USD [____]
  Educational 1.25% × gross:     USD [____]
  Employee total (11.00%):       USD [____]

EMPLOYER COMPUTATION (if employee)
  CSS [rate]% × gross:           USD [____]
  Educational 1.50% × gross:     USD [____]
  Employer total:                USD [____]

SELF-EMPLOYED COMPUTATION (if independent)
  IVM 9.36% × declared base:     USD [____]   (mandatory)
  Health 8.5% × declared base:   USD [____]   (voluntary, if elected)
  Self-employed total:           USD [____]

CEILING CHECK
  Contribution ceiling:          NONE — full gross taxed

INCOME TAX (territorial; if applicable)
  Panama-source taxable income:  USD [____]
  PIT (0% / 15% / 25% bands):    USD [____]

REVIEWER FLAGS
  [List any Tier 2 flags here — décimo, arrears, source, future rates]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their impact]
```

## Section 8 -- Bank statement reading guide

### How CSS / payroll debits appear on Panamanian bank statements

**Banco General:**
- Description: "CSS", "CAJA DE SEGURO SOCIAL", "SEGURO SOCIAL", "PLANILLA CSS"
- Timing: Monthly (planilla remittance)
- Amount: Combined obrero-patronal for all employees, OR per-employee figure

**Banistmo:**
- Description: "CAJA DE SEGURO SOCIAL", "SEG SOCIAL", "SEGURO EDUCATIVO"
- Timing: Monthly
- Amount: CSS and/or educational insurance

**BAC Credomatic:**
- Description: "CSS", "IVM" (for independents), "DGI" (income tax — NOT CSS)
- Timing: Monthly (CSS); quarterly estimated installments (DGI income tax)

**Key identification tips:**
1. CSS debits are outgoing (DEBITO), recurring monthly.
2. "SEGURO EDUCATIVO" is the educational insurance tax — exclude alongside CSS, but it is a distinct levy.
3. "IVM" on an independent's statement is the mandatory self-employed contribution.
4. Do NOT confuse CSS with "DGI" / "ISR" (income tax) or "ITBMS" (VAT) debits.
5. "DECIMO" / "DÉCIMO" debits are 13th-month wage payments, not CSS.
6. "CONVENIO DE PAGO" indicates delinquent-contribution arrangements — flag for reviewer.

### Currency note

Statements may show "B/." (Balboa) or "USD". They are the same value (1:1 peg). Treat interchangeably.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Confirm worker status** -- employer payroll (CSS planilla, employee+employer) vs independent (IVM). If unclear, STOP and ask.
2. **Scan for CSS debits** -- identify outgoing payments matching Section 3 patterns (CSS, SEGURO SOCIAL, SEGURO EDUCATIVO, IVM, PLANILLA).
3. **Separate the levies** -- CSS social security vs educational insurance vs income tax (DGI) vs VAT (ITBMS).
4. **Reverse-check employee figures** -- employee withholding should be ~11.00% of gross; employer ~14.75% (from 1 Apr 2025). If amounts imply a ceiling, flag — Panama has none.
5. **Flag for reviewer:** "CSS classification derived from bank-statement amounts only. Worker status, payroll period (Ley 462 rate), declared base, and income source have not been independently verified. Reviewer must confirm before filing."

## Section 10 -- Reference material

### Contribution rate summary

**Contribution rate summary table**

| Regime | Component | Rate | Source |
| --- | --- | --- | --- |
| Employee | CSS social security | 9.75% | PwC; Ley 462 |
| Employee | Educational insurance | 1.25% | PwC |
| Employee | **Total** | **11.00%** | (9.75 + 1.25) |
| Employer (1 Apr 2025) | CSS social security | 13.25% | Ley 462; MEF |
| Employer | Educational insurance | 1.50% | PwC |
| Employer | **Total (current)** | **14.75%** | (13.25 + 1.50) |
| Employer (from 1 Mar 2027) | **Total** | **15.75%** (future) | Ley 462 |
| Employer (from 1 Mar 2029) | **Total** | **16.75%** (future) | Ley 462 |
| Self-employed | IVM (mandatory) | 9.36% | Ley 462; Morgan & Morgan |
| Self-employed | Health & maternity (voluntary) | 8.5% | Ley 462; min declared B/.800 |

### Income tax bands (2025)

**Income tax bands (2025) reference table**

| Taxable income (USD) | Cumulative tax | Rate on excess | Source |
| --- | --- | --- | --- |
| 0 – 11,000 | 0 | 0% | PwC |
| 11,000 – 50,000 | 5,850 | 15% | PwC |
| Over 50,000 | — | 25% | PwC |

### Pension & retirement context

**Pension & retirement context table**

| Item | Value | Source |
| --- | --- | --- |
| Retirement age — women | 57 | Ley 462 (unchanged) |
| Retirement age — men | 62 | Ley 462 (unchanged) |
| Minimum (solidarity) pension | B/.144.00 | Morgan & Morgan |

### Minimum wage context (MITRADEL)

- Decree: Executive Decree No. 13 of 31 Dec 2025 (Gaceta Oficial 30438), effective **16 Jan 2026**, 2-year term [EY; MITRADEL].
- **No single national figure** — 59 differentiated rates across 74 economic activities, split by Region 1 (major urban districts) and Region 2 (remaining districts).
- Simple average ≈ **USD 636.80/month** [La Prensa].
- Example hourly rates (2026) [La Prensa; MITRADEL]: Construction $3.51 (R1) / $3.30 (R2); large-firm manufacturing up to $3.13 (R1) / $2.58 (R2); large wholesale/retail $3.02 (R1) / $2.48 (R2); banana agriculture $2.58 nationally.
- Domestic workers (monthly): B/.350 (R1), B/.320 (R2) [La Prensa; MITRADEL].

### Test suite

**Test 1:** Employee gross B/.1,500, May 2025. → Employee 11.00% = **165.00** (CSS 146.25 + educ 18.75). Employer 14.75% = **221.25** (CSS 198.75 + educ 22.50).

**Test 2:** Employee gross B/.2,000, 2025. → Employee = **220.00**. Employer = **295.00**. No ceiling applied.

**Test 3:** Self-employed declares B/.3,000, no health. → IVM 9.36% = **280.80**. Health not applied.

**Test 4:** Self-employed declares B/.3,000, with health. → IVM 280.80 + health 8.5% (255.00) = **535.80**.

**Test 5:** Panama-source taxable income B/.30,000. → PIT = (30,000 − 11,000) × 15% = **2,850.00**.

**Test 6:** Panama-source taxable income B/.80,000. → PIT = 5,850 + (80,000 − 50,000) × 25% = 5,850 + 7,500 = **13,350.00**.

**Test 7:** Employee with single wage source, tax fully withheld monthly. → No income-tax return filing required [PwC].

**Test 8:** Foreign-source income only, Panama resident. → Income-tax = **0** (territorial; foreign-source exempt). CSS still applies to any Panama employment.

**Test 9:** Payroll month March 2027. → Employer CSS 14.25% + educ 1.50% = **15.75%** (future-dated; confirm no change). Flag for reviewer.

### Prohibitions

- NEVER compute CSS without confirming worker status (employee vs self-employed independent).
- NEVER apply a contribution ceiling — Panama has none on CSS or educational insurance.
- NEVER apply the employee rate as if it changed under Ley 462 — only the employer rate increases.
- NEVER apply the 14.25% or 15.25% employer rate to a current (pre-1 Mar 2027) payroll — those are scheduled future rates.
- NEVER apply voluntary 8.5% health to a self-employed worker without confirming election.
- NEVER compute CSS on the 13th-month (décimo) — its treatment is unconfirmed [RESEARCH GAP]; escalate.
- NEVER quantify CSS arrears/surcharges without the live CSS Reglamento and a CSS statement.
- NEVER treat foreign-source income as taxable, nor Panama-source income as exempt, without evidence.
- NEVER confuse CSS / SEGURO EDUCATIVO with DGI income tax or ITBMS (VAT).
- NEVER present figures as definitive — label as estimated and direct the client to CSS/DGI records.
- NEVER quote an income-tax return form number or penalty percentage not confirmed from DGI [RESEARCH GAP].

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
