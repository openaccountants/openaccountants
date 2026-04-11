---
name: no-social-contributions
description: Use this skill whenever asked about Norwegian social contributions (trygdeavgift) for self-employed individuals operating as enkeltpersonforetak (sole proprietorship). Trigger on phrases like "trygdeavgift", "Norwegian social security", "self-employed contributions Norway", "NAV contributions", "national insurance Norway", "how much trygdeavgift do I pay", or any question about social contribution obligations for a self-employed client in Norway. This skill covers the 10.9% rate on business income, minimum thresholds, payment schedule, interaction with trinnskatt and income tax, exemptions, and edge cases. ALWAYS read this skill before touching any Norway social contributions work.
---

# Norway Social Contributions (Trygdeavgift) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Norway |
| Jurisdiction Code | NO |
| Primary Legislation | Folketrygdloven (National Insurance Act) |
| Supporting Legislation | Skatteloven (Tax Act); Skatteforvaltningsloven (Tax Administration Act) |
| Tax Authority | Skatteetaten (Norwegian Tax Administration) |
| Rate Publisher | Skatteetaten (publishes annual rate tables) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Norwegian statsautorisert revisor or registered accountant |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate calculation, thresholds, payment schedule. Tier 2: voluntary additional coverage, cross-border EEA situations, partial-year residency. Tier 3: disability benefits interaction, seafarer/fisherman regimes, Svalbard rules. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any trygdeavgift figure, you MUST know:

1. **Tax residency status** [T1] -- is the client tax-resident in Norway for the full year?
2. **Income type** [T1] -- business income (næringsinntekt) vs wage income (lønnsinntekt) vs pension income
3. **Total personal income (personinntekt) from self-employment** [T1] -- this is the base for trygdeavgift
4. **Is the client registered as enkeltpersonforetak?** [T1] -- confirms self-employed status
5. **Any concurrent employment?** [T1] -- employer already pays arbeidsgiveravgift on wages
6. **Age** [T1] -- reduced rate applies to persons under 17 or over 69

**If income type is unknown, STOP. Do not compute trygdeavgift. Income type determines the rate.**

---

## Step 1: Determine Rate Category [T1]

**Legislation:** Folketrygdloven; Stortingets vedtak om trygdeavgift

| Income Type | Rate (2025) | Who |
|-------------|-------------|-----|
| Wage income (lønnsinntekt) | 7.7% | Employees |
| Business income (næringsinntekt) | 10.9% | Self-employed (enkeltpersonforetak) |
| Fishing / hunting / childminding | 7.6% | Special categories |
| Pension income | 5.1% | Pensioners |

**Self-employed persons pay 10.9% on personinntekt from business activity.**

The higher rate for self-employed (10.9% vs 7.7%) compensates for the fact that self-employed do not have an employer paying arbeidsgiveravgift (employer's social contribution of 14.1%).

---

## Step 2: Trygdeavgift Calculation [T1]

**Legislation:** Folketrygdloven; Stortingets vedtak om trygdeavgift 2025

### Formula
```
trygdeavgift = personinntekt_from_business × 10.9%
```

### Minimum Threshold (Nedre grense)

| Parameter | Amount (2025) |
|-----------|---------------|
| Nedre grense (lower threshold) | NOK 69,650 |
| 25% phase-in range | NOK 69,650 to full rate |

**If personinntekt <= NOK 69,650:** No trygdeavgift is due.

**If personinntekt is just above NOK 69,650:** A 25% phase-in rule applies. The trygdeavgift cannot exceed 25% of the income above the threshold. This prevents a cliff effect at the threshold.

```
phase_in_cap = (personinntekt - 69,650) × 25%
trygdeavgift = min(personinntekt × 10.9%, phase_in_cap)
```

### Frikort (Exemption Card)

If total income does not exceed NOK 100,000 in 2025, the client can apply for a frikort (tax exemption card). No tax is withheld up to this limit, but trygdeavgift still applies if personinntekt exceeds NOK 69,650.

### Calculation Examples (2025)

| Personinntekt | Rate | Trygdeavgift | Notes |
|---------------|------|-------------|-------|
| NOK 50,000 | 10.9% | NOK 0 | Below threshold |
| NOK 75,000 | 10.9% | NOK 1,337.50 | Phase-in: min(8,175, (75,000-69,650)x25% = 1,337.50) |
| NOK 200,000 | 10.9% | NOK 21,800 | Full rate applies |
| NOK 500,000 | 10.9% | NOK 54,500 | Full rate applies |
| NOK 1,000,000 | 10.9% | NOK 109,000 | No upper cap |

**There is no upper cap on trygdeavgift. It applies to the full personinntekt without limit.**

---

## Step 3: Key Rules [T1]

**Legislation:** Folketrygdloven

1. **Trygdeavgift is based on personinntekt, not gross revenue.** Personinntekt = business income after allowable deductions but before personal allowances.
2. **No upper cap.** Unlike many EU countries, Norway has no ceiling on trygdeavgift.
3. **Trygdeavgift is NOT deductible** from income for income tax purposes.
4. **Trygdeavgift is calculated and assessed by Skatteetaten** as part of the annual tax assessment (skatteoppgjør).
5. **Trygdeavgift covers:** pension (alderspensjon), sickness (sykepenger), maternity/paternity (foreldrepenger), disability (uføretrygd), work assessment allowance, unemployment benefits.
6. **Self-employed sickness benefits:** Self-employed receive 80% coverage from day 17 (not day 1 like employees). Optional additional coverage available.

---

## Step 4: Payment Schedule [T1]

**Legislation:** Skattebetalingsloven (Tax Payment Act)

Self-employed pay trygdeavgift as part of forskuddsskatt (advance tax), which is paid in quarterly instalments:

| Instalment | Due Date |
|------------|----------|
| 1st | 15 March |
| 2nd | 15 June |
| 3rd | 15 September |
| 4th | 15 December |

- Forskuddsskatt covers both income tax and trygdeavgift combined
- Amount is based on expected income for the current year
- Final settlement occurs after the annual tax return (skattemelding) is filed
- Skattemelding deadline: 30 April (following year) for wage earners; 31 May for self-employed

---

## Step 5: Interaction with Income Tax [T1]

**Legislation:** Skatteloven; Folketrygdloven

| Question | Answer |
|----------|--------|
| Is trygdeavgift deductible from taxable income? | NO -- trygdeavgift is not deductible |
| Is it reported on the skattemelding? | YES -- calculated automatically by Skatteetaten based on reported income |
| Does it reduce the tax base? | NO -- it is an additional charge on top of income tax |
| How does it interact with trinnskatt? | Trinnskatt and trygdeavgift are both calculated on personinntekt but are separate charges |

### Total Marginal Rates for Self-Employed (2025)

| Income Bracket | Income Tax (22%) | Trinnskatt | Trygdeavgift (10.9%) | Combined |
|----------------|------------------|------------|----------------------|----------|
| NOK 0 -- 208,050 | 22% | 0% | 10.9% | 32.9% |
| NOK 208,051 -- 292,850 | 22% | 1.7% | 10.9% | 34.6% |
| NOK 292,851 -- 670,000 | 22% | 4.0% | 10.9% | 36.9% |
| NOK 670,001 -- 937,900 | 22% | 13.6% | 10.9% | 46.5% |
| NOK 937,901 -- 1,350,000 | 22% | 16.6% | 10.9% | 49.5% |
| Over NOK 1,350,000 | 22% | 17.6% | 10.9% | 50.5% |

---

## Step 6: Optional Additional Sickness Coverage [T2]

**Legislation:** Folketrygdloven § 8-36 to § 8-39

Self-employed can voluntarily pay for enhanced sickness benefit coverage:

| Coverage Option | Extra Premium | Benefit |
|----------------|---------------|---------|
| Standard (no extra) | 0% | 80% of income from day 17 |
| 80% from day 1 | ~2.0% of personinntekt | 80% coverage from day 1 of illness |
| 100% from day 17 | ~1.1% of personinntekt | 100% coverage from day 17 |
| 100% from day 1 | ~3.1% of personinntekt | 100% coverage from day 1 |

**[T2] -- Confirm current premium rates with NAV before advising. Rates are set annually.**

---

## Step 7: Registration [T1]

| Requirement | Detail |
|-------------|--------|
| When | Before starting business activity |
| With whom | Brønnøysundregistrene (Register of Business Enterprises) |
| Registration | Enhetsregisteret (Entity Register) and Foretaksregisteret (Business Register) |
| Tax registration | Automatic via Skatteetaten once registered |
| Threshold for VAT registration | NOK 50,000 in turnover (separate from trygdeavgift) |
| Required | Norwegian national ID number (fødselsnummer) or D-number |

---

## Step 8: Edge Case Registry

### EC1 -- Part-year self-employment [T1]
**Situation:** Client started self-employment in July, was employed January--June.
**Resolution:** Trygdeavgift at 10.9% applies only to personinntekt from self-employment. Wage income is subject to 7.7% rate. Both rates apply to their respective income portions in the same tax year. Forskuddsskatt should be adjusted from the quarter self-employment begins.

### EC2 -- Concurrent employment and self-employment [T1]
**Situation:** Client is employed full-time and runs a side business as enkeltpersonforetak.
**Resolution:** Wage income taxed at 7.7% trygdeavgift (deducted by employer). Business income taxed at 10.9% trygdeavgift. Both apply simultaneously. No offset between them.

### EC3 -- Income below threshold (phase-in) [T1]
**Situation:** Client has personinntekt of NOK 72,000 from self-employment.
**Resolution:** Phase-in rule applies. Trygdeavgift = min(72,000 x 10.9% = 7,848, (72,000 - 69,650) x 25% = 587.50) = NOK 587.50.

### EC4 -- Self-employed aged 70+ [T1]
**Situation:** Client is 72 years old and still running an enkeltpersonforetak.
**Resolution:** Reduced trygdeavgift rate of 5.1% applies to personinntekt from business activity for persons aged 70 and over (in the income year). Standard 10.9% does NOT apply.

### EC5 -- Cross-border EEA worker [T2]
**Situation:** Client lives in Norway but performs some work in Sweden.
**Resolution:** Under EU/EEA social security coordination (Regulation 883/2004), the client generally pays social contributions in only one country. If the client works substantially (25%+) in Sweden, Swedish rules may apply. [T2] flag for reviewer -- requires A1 certificate determination.

### EC6 -- Negative personinntekt (business loss) [T1]
**Situation:** Client's enkeltpersonforetak made a loss in the tax year.
**Resolution:** Trygdeavgift = NOK 0. There is no minimum trygdeavgift in Norway. Losses can be carried forward against future income for income tax purposes but do not create negative trygdeavgift.

### EC7 -- Fisherman or hunter [T1]
**Situation:** Client is a self-employed fisherman.
**Resolution:** Reduced rate of 7.6% applies instead of 10.9%. This is a specific legislative carve-out for fishing, hunting, and childminding in own home.

### EC8 -- Client on frikort with business income [T1]
**Situation:** Client has a frikort (exemption card) for total income under NOK 100,000, but business income is NOK 80,000.
**Resolution:** Frikort exempts from tax withholding, NOT from trygdeavgift. If personinntekt exceeds NOK 69,650, trygdeavgift is still assessed at final tax settlement. Client should be warned they will owe trygdeavgift at settlement.

### EC9 -- Non-resident performing work in Norway [T2]
**Situation:** Client is not tax-resident in Norway but earns business income from Norwegian sources.
**Resolution:** Non-residents may still be subject to Norwegian trygdeavgift if they are members of the Norwegian National Insurance scheme (folketrygden). Membership depends on duration and nature of stay. [T2] flag for reviewer -- requires assessment of social security membership.

### EC10 -- Voluntary higher pension accrual [T2]
**Situation:** Client wants to know if paying more trygdeavgift increases pension.
**Resolution:** Trygdeavgift is a fixed-rate charge; you cannot voluntarily pay more. Pension accrual is based on pensjongivende inntekt (pension-qualifying income), which is the same as personinntekt. Higher income = higher pension accrual, up to 7.1G cap (approx NOK 848,000 in 2025). [T2] if client asks about supplementary pension options.

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
Action Required: Qualified accountant must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified accountant. Document gap.
```

---

## Step 10: Test Suite

### Test 1 -- Standard self-employed, mid-range income
**Input:** Personinntekt NOK 500,000 from enkeltpersonforetak, age 40.
**Expected output:** Trygdeavgift = NOK 54,500 (10.9% x 500,000). Quarterly forskuddsskatt includes this amount.

### Test 2 -- Below threshold
**Input:** Personinntekt NOK 50,000 from side business, age 35.
**Expected output:** Trygdeavgift = NOK 0. Below NOK 69,650 threshold.

### Test 3 -- Phase-in range
**Input:** Personinntekt NOK 75,000, age 28.
**Expected output:** Phase-in applies. Trygdeavgift = min(8,175, 1,337.50) = NOK 1,337.50.

### Test 4 -- High income, no cap
**Input:** Personinntekt NOK 2,000,000, age 45.
**Expected output:** Trygdeavgift = NOK 218,000 (10.9% x 2,000,000). No upper cap.

### Test 5 -- Aged 70+
**Input:** Personinntekt NOK 300,000, age 72.
**Expected output:** Trygdeavgift = NOK 15,300 (5.1% x 300,000). Reduced rate for 70+.

### Test 6 -- Business loss
**Input:** Personinntekt NOK -50,000 (loss), age 38.
**Expected output:** Trygdeavgift = NOK 0. No minimum applies.

### Test 7 -- Concurrent employment + self-employment
**Input:** Wage income NOK 400,000 (7.7% paid by employer), business income NOK 200,000, age 35.
**Expected output:** Trygdeavgift on business income = NOK 21,800 (10.9% x 200,000). Wage trygdeavgift handled separately.

---

## PROHIBITIONS

- NEVER compute trygdeavgift without confirming the income type (business vs wage vs pension)
- NEVER apply the 7.7% wage rate to self-employment income -- the correct rate is 10.9%
- NEVER tell a client there is a maximum cap on trygdeavgift -- there is no upper cap in Norway
- NEVER state that trygdeavgift is tax-deductible -- it is NOT deductible from taxable income
- NEVER ignore the NOK 69,650 threshold and phase-in rule for low-income clients
- NEVER apply the 10.9% rate to clients aged 70+ -- the reduced 5.1% rate applies
- NEVER advise on cross-border social security without flagging for reviewer (EU/EEA Regulation 883/2004)
- NEVER present trygdeavgift figures as definitive -- always label as estimated and direct client to their skatteoppgjør for confirmation
- NEVER conflate trygdeavgift (employee/self-employed) with arbeidsgiveravgift (employer contribution of 14.1%)

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
