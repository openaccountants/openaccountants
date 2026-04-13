---
name: no-social-contributions
description: Use this skill whenever asked about Norwegian social contributions (trygdeavgift) for self-employed individuals operating as enkeltpersonforetak (sole proprietorship). Trigger on phrases like "trygdeavgift", "Norwegian social security", "self-employed contributions Norway", "NAV contributions", "national insurance Norway", "how much trygdeavgift do I pay", or any question about social contribution obligations for a self-employed client in Norway. This skill covers the 10.9% rate on business income, minimum thresholds, payment schedule, interaction with trinnskatt and income tax, exemptions, and edge cases. ALWAYS read this skill before touching any Norway social contributions work.
version: 2.0
---

# Norway Social Contributions (Trygdeavgift) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Norway (Kingdom of Norway) |
| Authority | Skatteetaten (Norwegian Tax Administration) |
| Primary legislation | Folketrygdloven (National Insurance Act) |
| Supporting legislation | Skatteloven; Skatteforvaltningsloven; Skattebetalingsloven |
| Self-employed rate | 10.9% on personinntekt from business |
| Wage income rate | 7.7% (for comparison) |
| Pension income rate | 5.1% |
| Age 70+ rate | 5.1% |
| Lower threshold (nedre grense) | NOK 69,650 (2025) |
| Phase-in rule | 25% of income above threshold |
| Upper cap | None |
| Payment method | Forskuddsskatt (quarterly advances) |
| Due dates | 15 Mar, 15 Jun, 15 Sep, 15 Dec |
| Currency | NOK only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Norwegian statsautorisert revisor |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Tax residency status** -- full-year Norwegian tax resident?
2. **Income type** -- business income (næringsinntekt) vs wage vs pension
3. **Total personinntekt from self-employment** -- the trygdeavgift base
4. **Registered as enkeltpersonforetak?** -- confirms self-employed status
5. **Any concurrent employment?** -- employer pays separate trygdeavgift
6. **Age** -- reduced rate for 70+

**If income type is unknown, STOP.**

### Refusal catalogue

**R-NO-SOC-1 -- Non-resident social security membership.** Trigger: non-resident earning business income in Norway. Message: "Membership in folketrygden depends on duration and nature of stay. Escalate to reviewer."

**R-NO-SOC-2 -- Seafarer/fisherman regime.** Trigger: self-employed fisherman or seafarer. Message: "Special rate regimes apply (7.6% for fishing). Confirm activity classification."

### Prohibitions

- NEVER compute trygdeavgift without confirming income type (business vs wage vs pension)
- NEVER apply the 7.7% wage rate to self-employment income -- correct rate is 10.9%
- NEVER tell a client there is a maximum cap -- there is no upper cap
- NEVER state that trygdeavgift is tax-deductible -- it is NOT
- NEVER ignore the NOK 69,650 threshold and phase-in rule
- NEVER apply 10.9% to clients aged 70+ -- reduced 5.1% applies
- NEVER conflate trygdeavgift with arbeidsgiveravgift (employer 14.1%)

---

## Section 3 -- Rate determination

**Legislation:** Folketrygdloven; Stortingets vedtak om trygdeavgift

| Income type | Rate (2025) |
|---|---|
| Wage income (lønnsinntekt) | 7.7% |
| Business income (næringsinntekt) | 10.9% |
| Fishing / hunting / childminding | 7.6% |
| Pension income | 5.1% |

The higher rate for self-employed compensates for the absence of employer arbeidsgiveravgift (14.1%).

---

## Section 4 -- Calculation rules and thresholds

### Formula

```
trygdeavgift = personinntekt_from_business x 10.9%
```

### Threshold and phase-in

| Parameter | Amount (2025) |
|---|---|
| Nedre grense (lower threshold) | NOK 69,650 |
| Phase-in rate | 25% |

If personinntekt <= NOK 69,650: no trygdeavgift.

If just above:

```
phase_in_cap = (personinntekt - 69,650) x 25%
trygdeavgift = min(personinntekt x 10.9%, phase_in_cap)
```

No upper cap. Trygdeavgift applies to full personinntekt without limit.

### Age 70+ reduction

Reduced rate of 5.1% applies. Standard 10.9% does NOT apply.

---

## Section 5 -- Key rules and coverage

1. Trygdeavgift based on personinntekt, not gross revenue
2. No upper cap
3. NOT deductible from income for income tax
4. Calculated by Skatteetaten as part of annual skatteoppgjør
5. Covers: pension, sickness (80% from day 17), maternity/paternity, disability, unemployment
6. Self-employed sickness: 80% from day 17 (not day 1). Optional additional coverage available

### Optional additional sickness coverage

| Option | Extra premium | Benefit |
|---|---|---|
| Standard | 0% | 80% from day 17 |
| 80% from day 1 | ~2.0% | 80% from day 1 |
| 100% from day 17 | ~1.1% | 100% from day 17 |
| 100% from day 1 | ~3.1% | 100% from day 1 |

Confirm current premium rates with NAV before advising.

---

## Section 6 -- Payment schedule and total marginal rates

### Payment schedule

| Instalment | Due date |
|---|---|
| 1st | 15 March |
| 2nd | 15 June |
| 3rd | 15 September |
| 4th | 15 December |

Forskuddsskatt covers both income tax and trygdeavgift. Skattemelding deadline: 31 May for self-employed.

### Total marginal rates (2025)

| Income bracket | Income tax (22%) | Trinnskatt | Trygdeavgift (10.9%) | Combined |
|---|---|---|---|---|
| NOK 0 -- 208,050 | 22% | 0% | 10.9% | 32.9% |
| NOK 208,051 -- 292,850 | 22% | 1.7% | 10.9% | 34.6% |
| NOK 292,851 -- 670,000 | 22% | 4.0% | 10.9% | 36.9% |
| NOK 670,001 -- 937,900 | 22% | 13.6% | 10.9% | 46.5% |
| NOK 937,901 -- 1,350,000 | 22% | 16.6% | 10.9% | 49.5% |
| Over NOK 1,350,000 | 22% | 17.6% | 10.9% | 50.5% |

---

## Section 7 -- Registration and frikort

### Registration

Register with Brønnøysundregistrene before starting activity. Tax registration automatic via Skatteetaten.

### Frikort

Frikort exempts from tax withholding (income under NOK 100,000) but NOT from trygdeavgift. If personinntekt exceeds NOK 69,650, trygdeavgift is still assessed at settlement.

---

## Section 8 -- Edge case registry

### EC1 -- Part-year self-employment
**Situation:** Started in July, employed Jan-Jun.
**Resolution:** 10.9% on business income. 7.7% on wage income. Both apply separately.

### EC2 -- Phase-in range
**Situation:** Personinntekt NOK 72,000.
**Resolution:** Phase-in: min(7,848, 587.50) = NOK 587.50.

### EC3 -- Aged 72
**Situation:** Age 72, still running business.
**Resolution:** Reduced 5.1%. NOK 300,000 income = NOK 15,300.

### EC4 -- Business loss
**Situation:** Net loss.
**Resolution:** Trygdeavgift = NOK 0. No minimum.

### EC5 -- Frikort with business income
**Situation:** Frikort, business income NOK 80,000.
**Resolution:** Frikort does not exempt from trygdeavgift. Will owe at settlement.

### EC6 -- Cross-border EEA
**Situation:** Works in Norway and Sweden.
**Resolution:** EU/EEA Regulation 883/2004. A1 certificate required. Escalate.

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
Action Required: Qualified accountant must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified accountant. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard, mid-range
**Input:** Personinntekt NOK 500,000, age 40.
**Expected output:** NOK 54,500.

### Test 2 -- Below threshold
**Input:** Personinntekt NOK 50,000, age 35.
**Expected output:** NOK 0.

### Test 3 -- Phase-in range
**Input:** Personinntekt NOK 75,000, age 28.
**Expected output:** min(8,175, 1,337.50) = NOK 1,337.50.

### Test 4 -- High income, no cap
**Input:** Personinntekt NOK 2,000,000, age 45.
**Expected output:** NOK 218,000.

### Test 5 -- Aged 70+
**Input:** Personinntekt NOK 300,000, age 72.
**Expected output:** NOK 15,300 (5.1%).

### Test 6 -- Business loss
**Input:** Loss NOK -50,000, age 38.
**Expected output:** NOK 0.

### Test 7 -- Concurrent employment + self-employment
**Input:** Wage NOK 400,000, business NOK 200,000, age 35.
**Expected output:** Business trygdeavgift NOK 21,800. Wage handled separately.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
