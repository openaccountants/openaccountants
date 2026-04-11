---
name: ie-prsi-class-s
description: Use this skill whenever asked about Irish PRSI Class S contributions for self-employed individuals. Trigger on phrases like "PRSI self-employed", "Class S contributions", "how much PRSI do I pay", "PRSI calculation Ireland", "self-employed social insurance Ireland", "PRSI threshold", or any question about PRSI obligations for a self-employed client in Ireland. This skill covers Class S rates, minimum contribution, income threshold, payment schedule, interaction with income tax, and edge cases. ALWAYS read this skill before touching any Irish PRSI Class S work.
---

# Ireland PRSI Class S -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Ireland |
| Jurisdiction Code | IE |
| Primary Legislation | Social Welfare Consolidation Act 2005 (as amended) |
| Supporting Legislation | Finance Act (annual); Social Welfare Acts (annual amendments) |
| Tax Authority | Department of Social Protection (DSP); Revenue Commissioners (collection) |
| Rate Publisher | Department of Social Protection / Revenue |
| Contributor | Open Accountants |
| Validated By | Pending -- licensed Irish practitioner sign-off required |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate calculation, minimum contribution, income threshold, payment schedule. Tier 2: blended rate transitions, dual PRSI class situations, voluntary contributions. Tier 3: cross-border workers, EU coordination of social security. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any PRSI Class S figure, you MUST know:

1. **Tax year** [T1] -- determines applicable rate (rates change mid-year on 1 October)
2. **Total income from all sources** [T1] -- PRSI Class S is levied on aggregate income, not just self-employment income
3. **Is income from all sources below EUR 5,000?** [T1] -- if yes, no PRSI liability
4. **Does the client have any PAYE employment?** [T1] -- if yes, may already pay Class A; Class S may not apply
5. **Age** [T1] -- PRSI is not payable once the client reaches age 66 (State Pension age)
6. **Is the client a proprietary director?** [T2] -- proprietary directors with 15%+ shareholding pay Class S

**If tax year is unknown, STOP. Do not compute PRSI. The rate changes annually and mid-year.**

---

## Step 1: Determine Liability [T1]

**Legislation:** Social Welfare Consolidation Act 2005, Part II

| Condition | PRSI Liability |
|-----------|---------------|
| Total income from all sources >= EUR 5,000 | Class S applies |
| Total income from all sources < EUR 5,000 | No PRSI liability |
| Client aged 66 or over | No PRSI liability |
| Client already paying Class A as PAYE employee | See Step 4 for dual status |

**"Total income from all sources" includes self-employment income, rental income, investment income, and any other assessable income.**

---

## Step 2: Class S Rate Calculation [T1]

**Legislation:** Social Welfare Consolidation Act 2005; Social Welfare Act 2024 (rate increases)

### 2025 Rates (Blended)

From 1 January 2025 to 30 September 2025: **4.1%**
From 1 October 2025 to 31 December 2025: **4.2%**

Blended annual rate for 2025 self-assessment: **4.125%** (9/12 x 4.1% + 3/12 x 4.2%)

### 2026 Rates (Blended)

From 1 January 2026 to 30 September 2026: **4.2%**
From 1 October 2026 to 31 December 2026: **4.35%**

Blended annual rate for 2026 self-assessment: **4.2375%** (9/12 x 4.2% + 3/12 x 4.35%)

### Formula

```
PRSI = max(total_income x blended_rate, minimum_contribution)
```

### Minimum Contribution

| Tax Year | Minimum |
|----------|---------|
| 2025 | EUR 650 |
| 2026 | EUR 650 |

**The minimum applies when the calculated PRSI (income x rate) is less than EUR 650, provided income >= EUR 5,000.**

### Calculation Examples (2025)

| Total Income | Rate | Calculated PRSI | Minimum Applies? | PRSI Due |
|-------------|------|----------------|-------------------|----------|
| EUR 4,000 | N/A | N/A | N/A | EUR 0 (below threshold) |
| EUR 5,000 | 4.125% | EUR 206.25 | Yes | EUR 650.00 |
| EUR 20,000 | 4.125% | EUR 825.00 | No | EUR 825.00 |
| EUR 100,000 | 4.125% | EUR 4,125.00 | No | EUR 4,125.00 |

---

## Step 3: Key Rules [T1]

**Legislation:** Social Welfare Consolidation Act 2005

1. **PRSI Class S is based on CURRENT year income.** Unlike Malta SSC, Irish PRSI is assessed on the same year's income via self-assessment.
2. **No upper earnings limit.** PRSI Class S applies to ALL income above the EUR 5,000 threshold with no cap.
3. **The EUR 5,000 threshold is an all-or-nothing test.** If income is EUR 5,001, PRSI applies to the FULL EUR 5,001, not just EUR 1.
4. **Minimum contribution of EUR 650 applies** whenever income >= EUR 5,000 but calculated PRSI < EUR 650.
5. **PRSI is NOT deductible for income tax purposes.** It is a separate charge.
6. **Class S covers pension, widow/widower's pension, guardian's payment, maternity/paternity/parent's benefit, and treatment benefit** (from 2025 onwards, treatment benefit extended to Class S contributors).

---

## Step 4: Dual Status -- PAYE Employment + Self-Employment [T2]

**Legislation:** Social Welfare Consolidation Act 2005, Schedule 1

| Scenario | PRSI Treatment |
|----------|---------------|
| PAYE employee (Class A) + self-employment income >= EUR 5,000 | Class A on employment income + Class S on self-employment and other non-PAYE income |
| PAYE employee (Class A) + self-employment income < EUR 5,000 | Class A only; no Class S |
| Proprietary director (15%+ shareholding) | Class S on all income (not Class A), even if receiving a salary |

**Class A and Class S can both apply simultaneously to the same individual on different income streams.**

---

## Step 5: Payment Schedule [T1]

**Legislation:** Taxes Consolidation Act 1997, Part 41A (self-assessment); Social Welfare Consolidation Act 2005

| Event | Deadline |
|-------|----------|
| Preliminary tax (including PRSI) | 31 October of the tax year (extended to mid-November for ROS e-filers) |
| Final return and balance | 31 October of the following year (extended to mid-November for ROS e-filers) |

- PRSI Class S is collected by Revenue through the self-assessment system (Form 11)
- It is NOT paid separately to the Department of Social Protection
- Preliminary tax must include estimated PRSI

---

## Step 6: Voluntary Contributions [T2]

**Legislation:** Social Welfare Consolidation Act 2005, Part II, Chapter 5

| Requirement | Detail |
|-------------|--------|
| Who | Former Class S contributors who have ceased self-employment |
| Rate | EUR 500 per year (flat rate, 2025/2026) |
| Purpose | Maintains pension entitlement record |
| Application | Must apply within 60 months of last compulsory contribution |

**Flag for reviewer if client is considering voluntary contributions -- confirm contribution record with DSP.**

---

## Step 7: Registration [T1]

| Requirement | Detail |
|-------------|--------|
| When | Within 30 days of commencing self-employment |
| With whom | Revenue Commissioners (Form TR1 for individuals, TR2 for companies) |
| Income threshold | EUR 5,000 annual income from all sources |
| Below EUR 5,000 | No PRSI liability, but should still register for income tax |

---

## Step 8: Edge Case Registry

### EC1 -- Income exactly EUR 5,000 [T1]
**Situation:** Client's total income from all sources is exactly EUR 5,000.
**Resolution:** PRSI Class S applies. Calculated PRSI = EUR 5,000 x 4.125% = EUR 206.25 (2025). Minimum of EUR 650 applies. Client pays EUR 650.

### EC2 -- Income EUR 4,999 [T1]
**Situation:** Client's total income is EUR 4,999.
**Resolution:** No PRSI liability. The EUR 5,000 threshold is not met. PRSI = EUR 0.

### EC3 -- Mid-year commencement of self-employment [T1]
**Situation:** Client started self-employment in July 2025.
**Resolution:** PRSI is based on total income for the full tax year (January to December), not pro-rated. If total income from all sources >= EUR 5,000 for the year, Class S applies on full income.

### EC4 -- Proprietary director receiving only a salary [T2]
**Situation:** Client is a proprietary director (15%+ shareholding) receiving a PAYE salary but no dividends.
**Resolution:** Proprietary directors pay Class S, not Class A, regardless of how they draw income. The employer does NOT deduct Class A PRSI. [T2] flag for reviewer -- confirm shareholding percentage and employment contract.

### EC5 -- Client turning 66 mid-year [T1]
**Situation:** Client reaches age 66 in August 2025.
**Resolution:** PRSI ceases from the contribution week in which the client turns 66. Income earned after that date is not subject to PRSI. Income before that date is. [T2] flag for reviewer to confirm exact contribution week calculation.

### EC6 -- Rental income only, no trade [T1]
**Situation:** Client has EUR 30,000 rental income but no trade or profession.
**Resolution:** Class S applies to rental income if total income from all sources >= EUR 5,000. Rental income is assessable for PRSI Class S.

### EC7 -- EU/EEA cross-border worker [T3]
**Situation:** Client is self-employed in Ireland but resident in another EU/EEA state, or vice versa.
**Resolution:** EU Regulation 883/2004 governs which state collects social insurance. [T3] escalate -- do not advise without specialist cross-border guidance.

### EC8 -- Client with both Class A and Class S in same year [T2]
**Situation:** Client is a PAYE employee (Class A) and also has self-employment income above EUR 5,000.
**Resolution:** Both classes apply. Class A is deducted at source from employment. Class S is self-assessed on the non-PAYE income via Form 11. The two do not offset. [T2] flag for reviewer to confirm that the PAYE employment is genuine (not a proprietary director situation).

### EC9 -- Rate transition year (October rate change) [T1]
**Situation:** Client asks which rate applies for 2025.
**Resolution:** The blended rate of 4.125% applies for the 2025 annual self-assessment. Revenue applies the blended rate automatically. Do not apply 4.1% or 4.2% separately on an annual return.

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
Action Required: Qualified practitioner must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified practitioner. Document gap.
```

---

## Step 10: Test Suite

### Test 1 -- Standard self-employed, mid-range income (2025)
**Input:** Self-employed, total income EUR 50,000, age 45, no PAYE employment.
**Expected output:** PRSI = EUR 50,000 x 4.125% = EUR 2,062.50. No minimum applies.

### Test 2 -- Below threshold
**Input:** Self-employed, total income EUR 4,500, age 35.
**Expected output:** PRSI = EUR 0. Income below EUR 5,000 threshold.

### Test 3 -- Minimum contribution applies
**Input:** Self-employed, total income EUR 10,000, age 40.
**Expected output:** Calculated PRSI = EUR 10,000 x 4.125% = EUR 412.50. Below minimum. PRSI = EUR 650.

### Test 4 -- Aged 66+
**Input:** Self-employed, total income EUR 80,000, age 67.
**Expected output:** PRSI = EUR 0. No PRSI liability at age 66+.

### Test 5 -- Dual Class A and Class S
**Input:** PAYE employee earning EUR 60,000 (Class A deducted at source) + self-employment income EUR 25,000, age 50.
**Expected output:** Class S on non-PAYE income: EUR 25,000 x 4.125% = EUR 1,031.25 via self-assessment. Class A handled separately at source.

### Test 6 -- Exactly at threshold
**Input:** Total income EUR 5,000, age 30.
**Expected output:** PRSI = EUR 650 (minimum applies; calculated = EUR 206.25).

### Test 7 -- 2026 rate
**Input:** Self-employed, total income EUR 80,000, age 42, tax year 2026.
**Expected output:** PRSI = EUR 80,000 x 4.2375% = EUR 3,390.00.

---

## PROHIBITIONS

- NEVER compute PRSI without confirming the tax year -- rates change annually and mid-year
- NEVER tell a client they owe no PRSI without checking the EUR 5,000 threshold from ALL sources
- NEVER apply a single rate (4.1% or 4.2%) to an annual return -- use the blended rate for the tax year
- NEVER treat a proprietary director as Class A -- they are Class S regardless of salary arrangements
- NEVER state that PRSI is deductible for income tax -- it is NOT
- NEVER advise on EU cross-border social insurance without specialist input
- NEVER pro-rate the EUR 5,000 threshold for partial years -- it is an annual threshold
- NEVER conflate USC and PRSI -- they are separate charges with separate rules
- NEVER present PRSI figures as definitive -- always label as estimated and direct client to Revenue for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CTA, AITI, or equivalent licensed practitioner in Ireland) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
