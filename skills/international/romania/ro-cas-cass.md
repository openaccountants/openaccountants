---
name: ro-cas-cass
description: Use this skill whenever asked about Romanian self-employed social and health contributions (CAS/CASS). Trigger on phrases like "CAS Romania", "CASS Romania", "contribuții sociale PFA", "Declarația Unică", "pensie PFA", "Romanian social contributions", or any question about social/health insurance obligations for a self-employed client in Romania. Covers CAS 25% and CASS 10% on fixed tier bases tied to minimum gross wage multiples. ALWAYS read this skill before touching any Romania social contributions work.
version: 2.0
---

# Romania CAS/CASS -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Romania |
| Authority | ANAF (Agenția Națională de Administrare Fiscală) |
| Primary legislation | Codul Fiscal (Legea nr. 227/2015), Titlul V (CAS) and Titlul VI (CASS) |
| Supporting legislation | OUG nr. 168/2022; annual minimum wage ordinances |
| CAS rate | 25% on fixed tier base |
| CASS rate | 10% on fixed tier base |
| Minimum gross wage (2025) | RON 3,590/month |
| CAS threshold | 12x min wage = RON 43,080 (below: voluntary) |
| CAS upper tier | 24x min wage = RON 86,160 |
| CASS lowest tier | 6x min wage = RON 21,540 |
| Filing form | Declarația Unică (Formular 212) |
| Payment deadline | 25 May of following year |
| Currency | RON only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Romanian consultant fiscal |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Entity type** -- PFA, II, or liberal profession?
2. **Estimated annual net income** -- determines which tier applies
3. **Income type** -- independent activities, intellectual property, rental, agricultural?
4. **Is the client also employed?** -- CAS may not be required if already paying through employment
5. **Year of activity** -- first year or ongoing?

**If net income estimate is unknown, STOP. The tier-based system requires knowing anticipated income.**

### Refusal catalogue

**R-RO-SOC-1 -- Multiple income source aggregation.** Trigger: client has PFA + IP + rental income and asks how they interact. Message: "Aggregation rules for multiple income categories require confirmation with consultant fiscal. Flag for reviewer."

### Prohibitions

- NEVER compute CAS/CASS on actual income -- the contribution base is a FIXED tier multiple of minimum wage
- NEVER forget that below the 6x threshold, the client has NO health insurance coverage
- NEVER confuse annual thresholds with monthly amounts
- NEVER ignore that CAS and CASS are both deductible from income tax
- NEVER tell a client below the CAS threshold that they have pension coverage (unless voluntary opt-in)
- NEVER present a single rate (e.g., "25% of income") -- CAS is 25% of the FIXED BASE
- NEVER assume employment CAS exempts from self-employment CAS if self-employment income crosses the threshold

---

## Section 3 -- CAS (pension) tier system

**Legislation:** Codul Fiscal, art. 148-150

| Estimated annual net income | CAS due? | Contribution base | Annual CAS (25%) |
|---|---|---|---|
| Below RON 43,080 (< 12x min wage) | Voluntary only | N/A | RON 0 (unless opt-in at RON 10,770) |
| RON 43,080 -- RON 86,160 | Mandatory | RON 43,080 | RON 10,770 |
| Above RON 86,160 (> 24x min wage) | Mandatory | RON 86,160 | RON 21,540 |

CAS is based on ESTIMATED net income declared in the Declarația Unică. The base is fixed at tier level, NOT at actual income.

---

## Section 4 -- CASS (health insurance) tier system

**Legislation:** Codul Fiscal, art. 170-174

| Estimated annual net income | CASS due? | Contribution base | Annual CASS (10%) |
|---|---|---|---|
| Below RON 21,540 (< 6x min wage) | No (but no health coverage) | N/A | RON 0 |
| RON 21,540 -- RON 43,080 | Yes | RON 21,540 | RON 2,154 |
| RON 43,080 -- RON 86,160 | Yes | RON 43,080 | RON 4,308 |
| Above RON 86,160 | Yes | RON 86,160 | RON 8,616 |

---

## Section 5 -- Computation steps

### Step 5.1 -- Estimate annual net income

```
net_income = gross_revenue - deductible_expenses
```

### Step 5.2 -- Determine CAS tier

```
IF net_income < 43,080:
    CAS = 0  (voluntary opt-in at RON 10,770)
ELIF net_income <= 86,160:
    CAS = 43,080 x 25% = 10,770
ELSE:
    CAS = 86,160 x 25% = 21,540
```

### Step 5.3 -- Determine CASS tier

```
IF net_income < 21,540:
    CASS = 0  (no health coverage)
ELIF net_income < 43,080:
    CASS = 21,540 x 10% = 2,154
ELIF net_income <= 86,160:
    CASS = 43,080 x 10% = 4,308
ELSE:
    CASS = 86,160 x 10% = 8,616
```

### Step 5.4 -- Total

```
total = CAS + CASS
```

---

## Section 6 -- Filing, payment, and tax deductibility

### Declarația Unică

| Obligation | Detail |
|---|---|
| Form | Declarația Unică (Formular 212) |
| Initial filing | By 25 May of current year (estimate + prior-year reconciliation) |
| Reconciliation | Actual income in next year's filing |

### Payment schedule

| Payment | Due date |
|---|---|
| Full annual CAS + CASS | By 25 May of following year |
| Optional advances | Any time (recommended) |

Late payment: interest (0.01%/day) and penalties (0.01%/day).

### Tax deductibility

| Question | Answer |
|---|---|
| Is CAS deductible? | YES -- from net income for income tax |
| Is CASS deductible? | YES |
| When deductible? | Year contributions relate to (accrual) |
| Effect | Reduces 10% income tax base |

---

## Section 7 -- Interaction with employment and special situations

### Employed AND self-employed

| Scenario | CAS obligation | CASS obligation |
|---|---|---|
| SE income < 12x min wage | No additional CAS | CASS at applicable tier on SE income |
| SE income >= 12x min wage | CAS at applicable tier | CASS at applicable tier |

Employment CAS does NOT exempt from self-employment CAS if SE income crosses threshold.

### Norma de venit (income norm)

CAS/CASS thresholds apply to the norma de venit amount, not actual income.

### First year of activity

Estimated income for remaining months only. Thresholds are NOT pro-rated -- they remain annual.

---

## Section 8 -- Edge case registry

### EC1 -- Below all thresholds
**Situation:** PFA net income RON 15,000/year.
**Resolution:** CAS RON 0. CASS RON 0. Flag: no health coverage. Recommend voluntary CASS (RON 2,154).

### EC2 -- Just above 12x threshold
**Situation:** PFA net income RON 44,000.
**Resolution:** CAS RON 10,770. CASS RON 4,308. Total RON 15,078.

### EC3 -- Voluntary CAS opt-in
**Situation:** Income below RON 43,080, client wants pension credits.
**Resolution:** Voluntary CAS at RON 10,770. Provides pension credit for the year.

### EC4 -- Multiple income sources
**Situation:** PFA + IP + rental income.
**Resolution:** All categories aggregated to determine tier. Flag for reviewer to confirm rules.

### EC5 -- Concurrent employment, high SE income
**Situation:** Employment RON 60,000, PFA RON 100,000.
**Resolution:** SE CAS: RON 21,540 (>24x tier). SE CASS: RON 8,616. Employment handled separately.

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
Action Required: Qualified consultant fiscal must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified consultant fiscal. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Low income, below all thresholds
**Input:** PFA net income RON 18,000, no employment.
**Expected output:** CAS RON 0. CASS RON 0. Flag: no health coverage.

### Test 2 -- Mid-range, 12-24x tier
**Input:** PFA net income RON 60,000, no employment.
**Expected output:** CAS RON 10,770. CASS RON 4,308. Total RON 15,078.

### Test 3 -- High income, above 24x
**Input:** PFA net income RON 150,000.
**Expected output:** CAS RON 21,540. CASS RON 8,616. Total RON 30,156.

### Test 4 -- Between 6x and 12x
**Input:** PFA net income RON 30,000.
**Expected output:** CAS RON 0. CASS RON 2,154. Total RON 2,154.

### Test 5 -- Employed plus self-employed
**Input:** Employment RON 50,000, PFA RON 50,000.
**Expected output:** SE CAS RON 10,770. SE CASS RON 4,308. Total additional RON 15,078.

### Test 6 -- Voluntary CAS opt-in
**Input:** PFA net income RON 20,000, opts in.
**Expected output:** Voluntary CAS RON 10,770. CASS RON 2,154. Total RON 12,924.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
