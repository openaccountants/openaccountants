---
name: ar-social-contributions
description: Use this skill whenever asked about Argentine self-employed social contributions (aportes autónomos). Trigger on phrases like "aportes autónomos", "categoría autónomos", "jubilación autónomos", "PAMI autónomos", "cuánto pago de autónomo", "contribuciones SIPA", or any question about Argentine social security obligations for self-employed individuals. Covers Categories I-V, retirement (SIPA), PAMI (INSSJP), and obra social contributions, monthly fixed amounts, VEP payment, and edge cases. ALWAYS read this skill before touching any Argentine social contribution work.
version: 2.0
---

# Argentina Social Contributions (Aportes Autónomos) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Argentina |
| Authority | ARCA (formerly AFIP) |
| Primary legislation | Ley 24.241 (SIPA), Ley 19.032 (INSSJP/PAMI) |
| Supporting legislation | Ley 23.660 (Obras Sociales); ARCA monthly resolutions |
| System | 5-category fixed monthly amounts |
| Components | Aporte jubilatorio (SIPA) + PAMI + Obra social |
| Category I (Sep 2025) | ~ARS 57,530/month |
| Category V (Sep 2025) | ~ARS 253,129/month |
| Professionals minimum | Category II |
| Employers minimum | Category III (1-3 emp), IV (4-6), V (7+) |
| Payment method | VEP via ARCA portal |
| Due date | Last business day of following month |
| Currency | ARS only (amounts change monthly due to movilidad) |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Argentine contador |
| Validation date | Pending |

**CRITICAL: Amounts change EVERY MONTH due to movilidad previsional. Always verify current amounts on ARCA website.**

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Activity type** -- profesional (university degree) vs other self-employed?
2. **Annual gross income** -- determines category
3. **Number of employees** -- affects category floor
4. **Concurrent employment (relación de dependencia)?** -- dual status rules
5. **Current month/period** -- amounts change monthly
6. **Monotributista or Autónomo?** -- this skill covers Autónomos only

**If activity type is unknown, STOP.**

### Refusal catalogue

**R-AR-SOC-1 -- Moratoria (debt regularization).** Trigger: client has years of unpaid contributions. Message: "Moratoria terms are set by specific ARCA resolutions. Escalate to qualified contador."

**R-AR-SOC-2 -- Differential regime.** Trigger: hazardous/arduous activity. Message: "Primed categories (I'-V') apply. Verify activity qualification with ARCA. Flag for reviewer."

### Prohibitions

- NEVER use amounts from a prior month without verifying current movilidad-adjusted values
- NEVER assign Category I to a professional with university degree
- NEVER tell a registered autónomo they owe nothing because of zero income -- amounts are fixed
- NEVER confuse Monotributo with Autónomo -- entirely separate regimes
- NEVER advise on moratoria without escalating
- NEVER present amounts as definitive beyond the current month
- NEVER assume dual-status clients are exempt from autónomo contributions
- NEVER assign an employer below their employee-count floor

---

## Section 3 -- Category determination

**Legislation:** Ley 24.241

| Category | Who |
|---|---|
| I | Lowest income, no employees, no university degree |
| II | Mid-range or professionals (university degree) without employees |
| III | Professionals with up to 3 employees or higher income |
| IV | Employers with 4-6 employees or high income |
| V | Employers with 7+ employees or highest income |

Key rules:
- Professionals with university degree: minimum Category II
- Employers: Category III (1-3), IV (4-6), V (7+) as floor

---

## Section 4 -- Monthly amounts and components

### Reference amounts (September 2025)

| Category | Monthly total (ARS) |
|---|---|
| I | ~57,530 |
| II | ~80,541 |
| III | ~115,059 |
| IV | ~184,094 |
| V | ~253,129 |

### Components

| Component | Destination |
|---|---|
| Aporte jubilatorio | SIPA (retirement pension) |
| Aporte PAMI | INSSJP (retiree health) |
| Aporte obra social | Obra Social (current health) |

### Movilidad (indexation)

Amounts adjusted monthly per Ley 27.609 movilidad formula (CPI + RIPTE). ARCA publishes updated tables each month.

---

## Section 5 -- Payment and registration

### VEP generation

1. Access ARCA portal
2. Select "Autónomos" > "Generar VEP"
3. Confirm period and category
4. Pay through linked bank account

### Registration

Register within 30 days via Formulario 885. Must have CUIT. Cannot be both Monotributista and Autónomo for same activity.

---

## Section 6 -- Tax deductibility and penalties

### Tax deductibility

| Question | Answer |
|---|---|
| Are aportes deductible? | YES -- for income tax (Ganancias) |
| Where reported? | Annual return deductions |
| Which year? | Year of payment |

### Penalties

| Penalty | Detail |
|---|---|
| Late payment | Daily interest (tasa resolutoria) |
| Non-registration | Fines + retroactive contributions |
| Non-payment | Periods do not count for retirement |
| ARCA can pursue | Ejecución fiscal (judicial collection) |

---

## Section 7 -- Voluntary higher category and dual status

### Voluntary higher category

Client may opt for a higher category than minimum. Increases future retirement benefits. File recategorización through ARCA.

### Dual status (employed + self-employed)

Must pay BOTH employee contributions (withheld) AND autónomo contributions. No exemption. Obra social may be unified.

### Jubilado continuing to work

Must still pay autónomo contributions. PAMI component may differ. Flag for reviewer.

---

## Section 8 -- Edge case registry

### EC1 -- Professional choosing Category I
**Situation:** Lawyer tries to register Category I.
**Resolution:** REJECT. Minimum Category II for university-degree professionals.

### EC2 -- Zero income month
**Situation:** No revenue, still registered.
**Resolution:** Full monthly contribution due. Fixed amounts regardless of income.

### EC3 -- Monotributo confusion
**Situation:** Client asks about aportes but is Monotributista.
**Resolution:** This skill does not apply. Direct to Monotributo skill.

### EC4 -- Employer drops below threshold
**Situation:** Category IV (5 employees) terminates 2, now has 3.
**Resolution:** May request recategorización to Category III. Not automatic. Flag for reviewer.

### EC5 -- Switch from Monotributo mid-year
**Situation:** Monotributista until June, Autónomo from July.
**Resolution:** Autónomo contributions start July. Category based on projected income. Flag for reviewer.

---

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

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

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified contador. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard Category I
**Input:** Freelance designer, no degree, no employees, Sep 2025.
**Expected output:** Category I. ~ARS 57,530. VEP by end of October.

### Test 2 -- Professional minimum
**Input:** Self-employed accountant, no employees, Sep 2025.
**Expected output:** Category II. ~ARS 80,541.

### Test 3 -- Employer with 5 employees
**Input:** Small business, 5 employees, Sep 2025.
**Expected output:** Category IV. ~ARS 184,094.

### Test 4 -- Dual status
**Input:** Employed full-time AND freelance.
**Expected output:** Must pay autónomo separately.

### Test 5 -- Zero income month
**Input:** Category I, zero revenue August 2025.
**Expected output:** Full contribution due.

### Test 6 -- Professional attempting Category I
**Input:** Lawyer tries Category I.
**Expected output:** REJECT. Minimum Category II.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
