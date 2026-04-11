---
name: ro-cas-cass
description: Use this skill whenever asked about Romanian self-employed social and health contributions (CAS/CASS). Trigger on phrases like "CAS Romania", "CASS Romania", "contribuții sociale PFA", "Declarația Unică", "pensie PFA", "Romanian social contributions", or any question about social/health insurance obligations for a self-employed client in Romania. Covers CAS 25% and CASS 10% on fixed tier bases tied to minimum gross wage multiples. ALWAYS read this skill before touching any Romania social contributions work.
---

# Romania CAS/CASS -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Romania |
| Jurisdiction Code | RO |
| Primary Legislation | Codul Fiscal (Legea nr. 227/2015), Titlul V (CAS) and Titlul VI (CASS) |
| Supporting Legislation | OUG nr. 168/2022; annual minimum wage ordinances |
| Tax Authority | ANAF (Agenția Națională de Administrare Fiscală) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Romanian consultant fiscal |
| Validation Date | Pending |
| Skill Version | 1.0 |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

Before computing, you MUST know:

1. **Entity type** [T1] -- PFA (Persoană Fizică Autorizată), II (Întreprindere Individuală), or liberal profession?
2. **Estimated annual net income** [T1] -- this determines which tier applies
3. **Income type** [T1] -- independent activities (activități independente), intellectual property, rental income, agricultural?
4. **Is the client also employed?** [T1] -- CAS may not be required if already paying through employment
5. **Year of activity** [T1] -- first year or ongoing?

**If net income estimate is unknown, STOP. The tier-based system requires knowing anticipated income.**

---

## Step 1: CAS (Pension) System [T1]

**Legislation:** Codul Fiscal, art. 148-150

### Rate

CAS (Contribuția de Asigurări Sociale) = **25%**

### Contribution Base -- Fixed Tiers

CAS uses a **fixed base** system -- the contribution base is NOT the actual income but a fixed multiple of the minimum gross wage:

| Estimated Annual Net Income | CAS Due? | Contribution Base | Annual CAS (25%) |
|----------------------------|----------|-------------------|------------------|
| Below 12 x minimum gross wage (< RON 43,080) | NO -- voluntary only | N/A | RON 0 (unless opt-in) |
| RON 43,080 -- RON 86,160 (12-24 x min wage) | YES -- mandatory | 12 x minimum gross wage = RON 43,080 | RON 10,770 |
| Above RON 86,160 (> 24 x min wage) | YES -- mandatory | 24 x minimum gross wage = RON 86,160 | RON 21,540 |

**Minimum gross wage (2025): RON 3,590/month**

### Key Rules

- CAS is based on the **estimated** net income declared in the Declarația Unică at the start of the year
- The actual base is fixed at the tier level, NOT at actual income
- If actual income at year-end differs from the estimate, the tier may change -- reconciliation occurs via the annual Declarația Unică

---

## Step 2: CASS (Health Insurance) System [T1]

**Legislation:** Codul Fiscal, art. 170-174

### Rate

CASS (Contribuția de Asigurări Sociale de Sănătate) = **10%**

### Contribution Base -- Fixed Tiers

| Estimated Annual Net Income | CASS Due? | Contribution Base | Annual CASS (10%) |
|----------------------------|-----------|-------------------|-------------------|
| Below 6 x minimum gross wage (< RON 21,540) | NO -- but no health insurance coverage | N/A | RON 0 |
| RON 21,540 -- RON 43,080 (6-12 x min wage) | YES | 6 x minimum gross wage = RON 21,540 | RON 2,154 |
| RON 43,080 -- RON 86,160 (12-24 x min wage) | YES | 12 x minimum gross wage = RON 43,080 | RON 4,308 |
| Above RON 86,160 (> 24 x min wage) | YES | 24 x minimum gross wage = RON 86,160 | RON 8,616 |

### CASS for Non-Income Earners

Persons with no income who want health coverage must pay CASS on a base of 6 x minimum gross wage = RON 2,154/year.

---

## Step 3: Computation Steps [T1]

### Step 3.1 -- Estimate annual net income

```
net_income = gross_revenue - deductible_expenses
# OR if using norma de venit (income norm): net_income = prescribed_norm
```

### Step 3.2 -- Determine CAS tier

```
min_wage_annual = 3,590 × 12 = 43,080

IF net_income < 43,080:
    CAS = 0  (voluntary opt-in available at RON 10,770)
ELIF net_income <= 86,160:
    CAS = 43,080 × 25% = 10,770
ELSE:
    CAS = 86,160 × 25% = 21,540
```

### Step 3.3 -- Determine CASS tier

```
IF net_income < 21,540:
    CASS = 0  (no health coverage unless voluntary)
ELIF net_income < 43,080:
    CASS = 21,540 × 10% = 2,154
ELIF net_income <= 86,160:
    CASS = 43,080 × 10% = 4,308
ELSE:
    CASS = 86,160 × 10% = 8,616
```

### Step 3.4 -- Total annual social contributions

```
total = CAS + CASS
```

---

## Step 4: Declarația Unică and Payment [T1]

**Legislation:** Codul Fiscal, art. 120-122

### Filing

| Obligation | Detail |
|------------|--------|
| Form | Declarația Unică (Formular 212) |
| Initial filing | By 25 May of the current year (estimated income for current year + reconciliation of prior year) |
| Reconciliation | Actual income reported in next year's Declarația Unică |

### Payment Schedule

| Payment | Due Date |
|---------|----------|
| Full annual CAS + CASS | By 25 May of the following year |
| Optional advance payments | Any time during the year (recommended to avoid cash flow shock) |

- No mandatory quarterly advance payments -- the full amount is due annually
- Late payment triggers interest (0.01%/day) and penalties (0.01%/day)

---

## Step 5: Tax Deductibility [T1]

| Question | Answer |
|----------|--------|
| Is CAS deductible from income tax base? | YES -- CAS is deductible from the net income for income tax purposes |
| Is CASS deductible? | YES -- CASS is also deductible |
| When deductible? | In the year the contributions relate to (accrual basis) |
| Effect | Reduces the 10% income tax base |

---

## Step 6: Interaction with Employment [T1]

**Legislation:** Codul Fiscal, art. 148(3), 170(3)

| Scenario | CAS Obligation | CASS Obligation |
|----------|---------------|-----------------|
| Employed AND self-employed (income < 12 x min wage from SE) | No additional CAS (already paying through employment) | CASS may be additional if combined income reaches higher tier |
| Employed AND self-employed (income >= 12 x min wage from SE) | CAS due on self-employment at applicable tier | CASS at applicable tier on self-employment income |

Key: CAS from employment does NOT exempt from CAS on self-employment income if self-employment income crosses the 12x threshold.

---

## Step 7: Edge Case Registry

### EC1 -- Income below all thresholds [T1]
**Situation:** PFA with net income of RON 15,000/year.
**Resolution:** Below 6x minimum wage. CAS = RON 0 (voluntary). CASS = RON 0 (but NO health insurance coverage). Flag: client has no state health insurance -- recommend voluntary CASS payment of RON 2,154.

### EC2 -- Income just above 12x threshold [T1]
**Situation:** PFA with net income of RON 44,000.
**Resolution:** CAS tier: 12-24x range. CAS = RON 10,770. CASS tier: 12-24x range. CASS = RON 4,308. Total: RON 15,078.

### EC3 -- Norma de venit (income norm) taxpayer [T1]
**Situation:** Client uses prescribed income norms rather than actual income/expenses.
**Resolution:** CAS/CASS thresholds are applied to the norma de venit amount, not actual income. The norm IS the net income for contribution purposes.

### EC4 -- Multiple income sources [T2]
**Situation:** Client has PFA income AND intellectual property income AND rental income.
**Resolution:** All categories of income are aggregated to determine the threshold tier. CAS and CASS bases are determined by total net income across all categories. [T2] -- confirm aggregation rules with consultant fiscal.

### EC5 -- Concurrent employment, high self-employment income [T1]
**Situation:** Client earns RON 60,000/year from employment and RON 100,000/year from PFA.
**Resolution:** CAS already paid on employment income. Self-employment CAS: tier is >24x, so CAS = RON 21,540. CASS: additional CASS at highest tier = RON 8,616. Employment CASS handled separately by employer.

### EC6 -- Voluntary CAS opt-in [T1]
**Situation:** Client with income below RON 43,080 wants pension credits.
**Resolution:** Client can voluntarily opt in to CAS by declaring in Declarația Unică. Base = 12x minimum wage. Annual CAS = RON 10,770. This provides pension insurance credit for the year.

### EC7 -- First year of activity [T1]
**Situation:** PFA registered in September 2025.
**Resolution:** Estimated income is for the remaining months only. Thresholds are NOT pro-rated -- they remain annual. If annualized estimated income would cross a threshold, apply that tier.

### EC8 -- Micro-enterprise (SRL) owner also working as PFA [T2]
**Situation:** Client owns an SRL (micro-enterprise) and also operates a PFA.
**Resolution:** SRL dividends are subject to CASS separately. PFA income triggers its own CAS/CASS obligations. [T2] -- complex interaction, confirm with consultant fiscal.

---

## Step 8: Test Suite

### Test 1 -- Low income, below all thresholds
**Input:** PFA net income RON 18,000/year, no employment.
**Expected output:** CAS: RON 0 (below 12x threshold). CASS: RON 0 (below 6x threshold). Flag: no health coverage.

### Test 2 -- Mid-range, 12-24x tier
**Input:** PFA net income RON 60,000/year, no employment.
**Expected output:** CAS: RON 10,770 (base = RON 43,080 x 25%). CASS: RON 4,308 (base = RON 43,080 x 10%). Total: RON 15,078.

### Test 3 -- High income, above 24x
**Input:** PFA net income RON 150,000/year, no employment.
**Expected output:** CAS: RON 21,540 (base = RON 86,160 x 25%). CASS: RON 8,616 (base = RON 86,160 x 10%). Total: RON 30,156.

### Test 4 -- Between 6x and 12x (CASS but no CAS)
**Input:** PFA net income RON 30,000/year, no employment.
**Expected output:** CAS: RON 0 (below 12x). CASS: RON 2,154 (base = RON 21,540 x 10%). Total: RON 2,154.

### Test 5 -- Employed plus self-employed
**Input:** Employment income RON 50,000/year, PFA net income RON 50,000/year.
**Expected output:** Self-employment CAS: RON 10,770 (PFA income in 12-24x tier). Self-employment CASS: RON 4,308. Employment CAS/CASS handled separately. Total additional from PFA: RON 15,078.

### Test 6 -- Voluntary CAS opt-in
**Input:** PFA net income RON 20,000, client opts in to CAS.
**Expected output:** Voluntary CAS: RON 10,770. CASS: RON 2,154 (6-12x tier). Total: RON 12,924.

---

## PROHIBITIONS

- NEVER compute CAS/CASS on actual income -- the contribution base is a FIXED tier multiple of minimum wage
- NEVER forget that below the 6x threshold, the client has NO health insurance coverage
- NEVER confuse annual thresholds with monthly amounts -- thresholds are annual
- NEVER ignore that CAS and CASS are both deductible from income tax
- NEVER tell a client below the CAS threshold that they have pension coverage -- they do not (unless voluntary opt-in)
- NEVER present a single rate (e.g., "25% of income") -- CAS is 25% of the FIXED BASE, not of actual income
- NEVER advise on multiple income source aggregation without flagging for reviewer
- NEVER assume employment CAS exempts from self-employment CAS -- it does not if self-employment income crosses the threshold

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
