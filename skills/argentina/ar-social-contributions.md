---
name: ar-social-contributions
description: Use this skill whenever asked about Argentine self-employed social contributions (aportes autónomos). Trigger on phrases like "aportes autónomos", "categoría autónomos", "jubilación autónomos", "PAMI autónomos", "cuánto pago de autónomo", "contribuciones SIPA", or any question about Argentine social security obligations for self-employed individuals. Covers Categories I-V, retirement (SIPA), PAMI (INSSJP), and obra social contributions, monthly fixed amounts, VEP payment, and edge cases. ALWAYS read this skill before touching any Argentine social contribution work.
version: 2.0
jurisdiction: AR
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: A licensed accountant (name withheld at their request)
review_status: current
trust_label: Checked by a licensed accountant (name withheld at their request)
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AR Social Contributions

## Argentina Social Contributions (Aportes Autónomos) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
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

CRITICAL: Amounts change EVERY MONTH due to movilidad previsional. Always verify current amounts on ARCA website.

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

- **R-AR-SOC-1 -- Moratoria (debt regularization)** — Trigger: client has years of unpaid contributions. Message: "Moratoria terms are set by specific ARCA resolutions. Escalate to qualified contador."
- **R-AR-SOC-2 -- Differential regime** — Trigger: hazardous/arduous activity. Message: "Primed categories (I'-V') apply. Verify activity qualification with ARCA. Flag for reviewer."

### Prohibitions

- **Prohibitions list** — NEVER use amounts from a prior month without verifying current movilidad-adjusted values; NEVER assign Category I to a professional with university degree; NEVER tell a registered autónomo they owe nothing because of zero income -- amounts are fixed; NEVER confuse Monotributo with Autónomo -- entirely separate regimes; NEVER advise on moratoria without escalating; NEVER present amounts as definitive beyond the current month; NEVER assume dual-status clients are exempt from autónomo contributions; NEVER assign an employer below their employee-count floor

## Section 3 -- Category determination

**Category determination table**  _(Ley 24.241)_

| Category | Who |
| --- | --- |
| I | Lowest income, no employees, no university degree |
| II | Mid-range or professionals (university degree) without employees |
| III | Professionals with up to 3 employees or higher income |
| IV | Employers with 4-6 employees or high income |
| V | Employers with 7+ employees or highest income |

- **Key rules** — Professionals with university degree: minimum Category II. Employers: Category III (1-3), IV (4-6), V (7+) as floor.  _(Ley 24.241)_

### Reference amounts (September 2025)

**Reference amounts (September 2025)**

| Category | Monthly total (ARS) |
| --- | --- |
| I | ~57,530 |
| II | ~80,541 |
| III | ~115,059 |
| IV | ~184,094 |
| V | ~253,129 |

### Components

**Components table**

| Component | Destination |
| --- | --- |
| Aporte jubilatorio | SIPA (retirement pension) |
| Aporte PAMI | INSSJP (retiree health) |
| Aporte obra social | Obra Social (current health) |

### Movilidad (indexation)

- **Movilidad adjustment rule** — Amounts adjusted monthly per Ley 27.609 movilidad formula (CPI + RIPTE). ARCA publishes updated tables each month.  _(Ley 27.609)_

### VEP generation

1. Access ARCA portal
2. Select "Autónomos" > "Generar VEP"
3. Confirm period and category
4. Pay through linked bank account

### Registration

- **Registration requirements** — Registration must be completed in the same month in which the event that places the person within the régimen occurs (Formulario 885). At most, and not preferably, it may be completed retroactively up to the following month’s due date, since the régimen is paid in arrears, so the payment is still made on time. Must have CUIT. Cannot be both Monotributista and Autónomo for the same activity.

### Tax deductibility

**Tax deductibility table**

| Question | Answer |
| --- | --- |
| Are aportes deductible? | YES -- for income tax (Ganancias) |
| Where reported? | Annual return deductions |
| Which year? | Year of payment |

### Penalties

**Penalties table**

| Penalty | Detail |
| --- | --- |
| Late payment | Daily interest (tasa resolutoria) |
| Non-registration | Fines + retroactive contributions |
| Non-payment | Periods do not count for retirement |
| ARCA can pursue | Ejecución fiscal (judicial collection) |

### Voluntary higher category

- **Voluntary higher category rule** — Client may opt for a higher category than minimum. Increases future retirement benefits. File recategorización through ARCA.

### Dual status (employed + self-employed)

- **Dual status rule** — Must pay BOTH employee contributions (withheld) AND autónomo contributions. No exemption. Obra social may be unified.

### Jubilado continuing to work

- **Jubilado continuing to work rule** — Must still pay autónomo contributions. PAMI component may differ. Flag for reviewer.

### EC1 -- Professional choosing Category I

Situation: Lawyer tries to register Category I.
Resolution: REJECT. Minimum Category II for university-degree professionals.

### EC2 -- Zero income month

Situation: No revenue, still registered.
Resolution: Full monthly contribution due. Fixed amounts regardless of income.

### EC3 -- Monotributo confusion

Situation: Client asks about aportes but is Monotributista.
Resolution: This skill does not apply. Direct to Monotributo skill.

### EC4 -- Employer drops below threshold

Situation: Category IV (5 employees) terminates 2, now has 3.
Resolution: May request recategorización to Category III. Not automatic. Flag for reviewer.

### EC5 -- Switch from Monotributo mid-year

Situation: Monotributista until June, Autónomo from July.
Resolution: Autónomo contributions start July. Category based on projected income. Flag for reviewer.

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

### Test 1 -- Standard Category I

Input: Freelance designer, no degree, no employees, Sep 2025.
Expected output: Category I. ~ARS 57,530. VEP by end of October.

### Test 2 -- Professional minimum

Input: Self-employed accountant, no employees, Sep 2025.
Expected output: Category II. ~ARS 80,541.

### Test 3 -- Employer with 5 employees

Input: Small business, 5 employees, Sep 2025.
Expected output: Category IV. ~ARS 184,094.

### Test 4 -- Dual status

Input: Employed full-time AND freelance.
Expected output: Must pay autónomo separately.

### Test 5 -- Zero income month

Input: Category I, zero revenue August 2025.
Expected output: Full contribution due.

### Test 6 -- Professional attempting Category I

Input: Lawyer tries Category I.
Expected output: REJECT. Minimum Category II.

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
