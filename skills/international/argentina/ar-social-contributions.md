---
name: ar-social-contributions
description: Use this skill whenever asked about Argentine self-employed social contributions (aportes autónomos). Trigger on phrases like "aportes autónomos", "categoría autónomos", "jubilación autónomos", "PAMI autónomos", "cuánto pago de autónomo", "contribuciones SIPA", or any question about Argentine social security obligations for self-employed individuals. Covers Categories I-V, retirement (SIPA), PAMI (INSSJP), and obra social contributions, monthly fixed amounts, VEP payment, and edge cases. ALWAYS read this skill before touching any Argentine social contribution work.
---

# Argentina Social Contributions (Aportes Autónomos) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Argentina |
| Jurisdiction Code | AR |
| Primary Legislation | Ley 24.241 (Sistema Integrado de Jubilaciones y Pensiones -- SIPA), Ley 19.032 (INSSJP/PAMI) |
| Supporting Legislation | Resolución General ARCA/AFIP (monthly rate updates), Ley 23.660 (Obras Sociales) |
| Tax Authority | ARCA (formerly AFIP -- Administración Federal de Ingresos Públicos) |
| Rate Publisher | ARCA (publishes monthly rate tables with movilidad adjustments) |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: category determination, monthly amounts, payment schedule. Tier 2: category changes mid-year, dual status, voluntary higher category. Tier 3: moratoria/regularización, disability exemptions. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified contador must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any aporte figure, you MUST know:

1. **Activity type** [T1] -- profesional (university degree) vs. other self-employed (comerciante, oficio)
2. **Annual gross income from self-employment** [T1] -- determines category (I-V)
3. **Number of employees (if any)** [T1] -- affects category floor for employers
4. **Is client also employed (relación de dependencia)?** [T1] -- dual status rules apply
5. **Current month/period** [T1] -- amounts change monthly due to movilidad
6. **Is client registered as Monotributista or Autónomo?** [T1] -- Monotributo has its own contribution regime; this skill covers Autónomos only

**If activity type is unknown, STOP. Do not assign a category.**

---

## Step 1: Determine Category [T1]

**Legislation:** Ley 24.241, Resolución General ARCA

| Category | Who | Typical Profile |
|----------|-----|-----------------|
| I | Lowest income self-employed, no employees | Freelancers, independent contractors, low-revenue professionals |
| II | Mid-range income or professionals (university degree) without employees | Contadores, abogados, médicos without staff |
| III | Professionals with up to 3 employees or higher income | Professional firms, small businesses |
| IV | Employers with 4-6 employees or high income | Medium businesses |
| V | Employers with 7+ employees or highest income | Larger operations |

**Key rule:** Professionals with university degree (título habilitante) start at minimum Category II, never Category I.

**Employers:** Must be in at least Category III (1-3 employees), IV (4-6), or V (7+). The number of employees sets the floor.

---

## Step 2: Monthly Contribution Amounts [T1]

**Legislation:** Ley 24.241, ARCA monthly publication

### Contribution Components (all categories)

Each monthly payment includes three components:

| Component | Destination | Purpose |
|-----------|------------|---------|
| Aporte jubilatorio | SIPA (Sistema Integrado Previsional Argentino) | Retirement pension |
| Aporte PAMI | INSSJP (Instituto Nacional de Servicios Sociales para Jubilados y Pensionados) | Health coverage for retirees |
| Aporte obra social | Obra Social | Current health insurance |

### Reference Amounts (September 2025)

| Category | Monthly Total (ARS) |
|----------|-------------------|
| I | ~$57,530 |
| II | ~$80,541 |
| III | ~$115,059 |
| IV | ~$184,094 |
| V | ~$253,129 |

**CRITICAL: These amounts change EVERY MONTH** due to movilidad previsional adjustments. Always verify the current month's amounts on the ARCA website before advising.

### Differential Categories (I' to V')

Workers in hazardous or arduous activities (actividades penosas o riesgosas) with differential retirement regimes use primed categories (I', II', III', IV', V') with higher amounts. [T2] -- confirm with reviewer if client's activity qualifies.

---

## Step 3: Payment Method and Schedule [T1]

**Legislation:** Resolución General ARCA

| Item | Detail |
|------|--------|
| Payment instrument | VEP (Volante Electrónico de Pago) generated via ARCA portal |
| Due date | By the last business day of the month following the contribution period |
| Frequency | Monthly |
| Payment channels | Home banking, electronic payment via ARCA |
| CUIT required | Yes -- must have CUIT (Clave Unica de Identificación Tributaria) |

### VEP Generation Steps

1. Access ARCA portal (servicios online)
2. Select "Autónomos" > "Generar VEP"
3. Confirm period and category
4. Generate VEP and pay through linked bank account

---

## Step 4: Registration [T1]

| Requirement | Detail |
|-------------|--------|
| When | Within 30 days of commencing self-employed activity |
| Where | ARCA portal (online) or delegación ARCA |
| Key form | Formulario 885 (alta autónomos) |
| Documents | CUIT, proof of activity, professional title (if applicable) |
| Monotributo vs. Autónomo | Client must choose one regime. Cannot be both simultaneously for same activity. |

---

## Step 5: Movilidad (Indexation) [T1]

**Legislation:** Ley 27.609 (movilidad formula)

- Contribution amounts are adjusted monthly based on the movilidad previsional formula
- The formula considers CPI (IPC) and salary indices (RIPTE)
- ARCA publishes updated tables each month
- **Never use amounts from a prior month without checking for updates**

---

## Step 6: Interaction with Income Tax [T1]

| Question | Answer |
|----------|--------|
| Are aportes autónomos deductible? | YES -- deductible for income tax purposes (Ganancias) |
| Where reported? | Deducted as "cargas de familia y deducciones" in the annual tax return |
| Which year? | Aportes paid in Year X are deducted in Year X's return |

---

## Step 7: Penalties [T1]

**Legislation:** Ley 11.683 (Ley de Procedimientos Fiscales)

| Penalty | Detail |
|---------|--------|
| Late payment interest | Resolutoria tasa applied daily on overdue amounts |
| Non-registration | Fines under Ley 11.683 + retroactive contributions |
| Debt collection | ARCA can initiate ejecución fiscal (judicial collection) |
| Impact on benefits | Periods without payment do not count for retirement |

---

## Step 8: Edge Case Registry

### EC1 -- Professional with no employees choosing Category I [T1]
**Situation:** A lawyer (abogado) tries to register as Category I.
**Resolution:** Professionals with university title MUST be at least Category II. Category I is not available to them. Reject and assign Category II minimum.

### EC2 -- Dual status: employed + self-employed [T1]
**Situation:** Client is both an employee (relación de dependencia) and runs a side business.
**Resolution:** Must pay BOTH employee contributions (withheld by employer) AND autónomo contributions for the self-employed activity. No exemption from autónomo for being employed. Obra social may be unified.

### EC3 -- Client switches from Monotributo to Autónomo mid-year [T2]
**Situation:** Client was Monotributista until June, then switches to Autónomo from July.
**Resolution:** Monotributo contributions cover January-June. Autónomo contributions start from July. Category must be determined based on projected annual income. [T2] flag for reviewer -- confirm transition and category assignment.

### EC4 -- Employer drops below employee threshold [T2]
**Situation:** Category IV employer (5 employees) terminates two employees, now has 3.
**Resolution:** May request recategorización to Category III. However, the change is not automatic -- must file with ARCA. [T2] flag for reviewer to confirm timing and process.

### EC5 -- Zero income month but still registered [T1]
**Situation:** Client had no income in a given month but is still registered as autónomo.
**Resolution:** Monthly contribution is still due. Autónomo contributions are fixed by category, not by income. Not paying creates debt with ARCA.

### EC6 -- Client in moratoria (payment plan for arrears) [T3]
**Situation:** Client has years of unpaid contributions and wants to enter a moratoria.
**Resolution:** [T3] Escalate. Moratoria terms are set by specific ARCA resolutions with eligibility windows. Do not advise on moratoria without a qualified contador reviewing the specific resolution in force.

### EC7 -- Differential regime (actividad riesgosa) [T2]
**Situation:** Client works in mining, aviation, or other hazardous activity.
**Resolution:** Uses primed categories (I' to V') with higher amounts. Must verify the activity qualifies under the differential regime list. [T2] flag for reviewer.

### EC8 -- Voluntary higher category [T1]
**Situation:** Client in Category I wants to pay Category III amounts voluntarily.
**Resolution:** Permitted. A self-employed person may opt for a higher category than the minimum required. This increases future retirement benefits. File recategorización through ARCA portal.

### EC9 -- Jubilado (retiree) continuing to work [T2]
**Situation:** Client receives a retirement pension but continues self-employed activity.
**Resolution:** Must still pay autónomo contributions. PAMI component may differ. [T2] flag for reviewer to confirm applicable reductions.

---

## Step 9: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified contador must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified contador. Document gap.
```

---

## Step 10: Test Suite

### Test 1 -- Standard Category I freelancer
**Input:** Freelance graphic designer, no university degree, no employees, September 2025.
**Expected output:** Category I. Monthly contribution ~ARS 57,530. Paid via VEP by end of October 2025.

### Test 2 -- Professional minimum Category II
**Input:** Self-employed accountant (contador público), no employees, September 2025.
**Expected output:** Category II (minimum for professionals). Monthly ~ARS 80,541.

### Test 3 -- Employer with 5 employees
**Input:** Small business owner, 5 employees, September 2025.
**Expected output:** Category IV (floor for 4-6 employees). Monthly ~ARS 184,094.

### Test 4 -- Dual status employee + autónomo
**Input:** Client is employed full-time AND runs a freelance business on the side.
**Expected output:** Must pay autónomo contributions separately. Employment contributions do not cover self-employed activity.

### Test 5 -- Zero income month
**Input:** Category I autónomo, zero revenue in August 2025.
**Expected output:** Full monthly contribution still due (~ARS 57,530 for September payment). Fixed amount regardless of income.

### Test 6 -- Monotributo confusion
**Input:** Client asks about "aportes autónomos" but is registered as Monotributista.
**Expected output:** This skill does not apply. Monotributo has its own integrated contribution. Direct client to Monotributo skill.

### Test 7 -- Professional attempting Category I
**Input:** Self-employed lawyer (abogado) tries to register in Category I.
**Expected output:** REJECT. Minimum is Category II for professionals with university title.

---

## PROHIBITIONS

- NEVER use amounts from a prior month without verifying current movilidad-adjusted values
- NEVER assign Category I to a professional with a university degree (título habilitante)
- NEVER tell a registered autónomo they owe nothing because they had no income -- contributions are fixed monthly amounts
- NEVER confuse Monotributo contributions with Autónomo contributions -- they are entirely separate regimes
- NEVER advise on moratoria (debt regularization plans) without escalating to a qualified contador
- NEVER present contribution amounts as definitive beyond the current month -- amounts change monthly
- NEVER assume dual-status clients are exempt from autónomo contributions because they are employed
- NEVER compute penalties or interest without escalating to a qualified contador
- NEVER assign an employer to a category below their employee-count floor

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
