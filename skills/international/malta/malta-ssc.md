---
name: malta-ssc
description: Use this skill whenever asked about Malta Social Security Contributions (SSC) for self-employed or self-occupied individuals. Trigger on phrases like "how much SSC do I pay", "Class 2 contributions", "social security self-employed", "SSC calculation", "SSC arrears", "do I need to pay SSC", "SSC and income tax", or any question about Malta SSC obligations for a self-employed client. Also trigger when preparing a TA24 income tax return where SSC deductibility (Box 20) is relevant. This skill covers Class 2 rates, min/max caps, payment schedule, registration, penalties, interaction with income tax, TA22 part-time regime, and edge cases. ALWAYS read this skill before touching any SSC-related work.
---

# Malta Social Security Contributions (SSC) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Malta |
| Jurisdiction Code | MT |
| Primary Legislation | Social Security Act, Chapter 318 |
| Supporting Legislation | Income Tax Act Article 14 (SSC deductibility); Income Tax Act Article 4C (TA22 regime) |
| Tax Authority | Department of Social Security (DSS), Malta |
| Rate Publisher | MTCA (publishes annual rate tables) |
| Contributor | Michael Cutajar, CPA (Warrant No. 125122), ACCA |
| Validated By | Michael Cutajar |
| Validation Date | March 2026 |
| Skill Version | 1.0 |
| Accora Integration | `ssc_rates` table, `calculate_ssc_class2()` RPC, `ssc-service.ts`, `tax-return-service.ts` Box 20 |
| Confidence Coverage | Tier 1: rate calculation, min/max caps, payment schedule, TA22 rule. Tier 2: dual status edge cases, mid-year switches, pro-rata exemptions. Tier 3: disability exemptions, group pension arrangements. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Warranted accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any SSC figure, you MUST know:

1. **Birth year** [T1] -- determines SC maximum cap (pre/post 1 January 1962)
2. **Employment status** [T1] -- self-occupied, self-employed, or dual (employed + side income)
3. **Is this the first year of self-employment?** [T1] -- SA minimum applies legislatively
4. **Prior year net self-employment income** [T1] -- SSC is always based on prior year, not current
5. **Has a TA24 been filed for the prior year?** [T1] -- if not, SA minimum applies until assessment
6. **Any full-time employment with Class 1 contributions?** [T1] -- if yes, no Class 2 due

**If birth year is unknown, STOP. Do not compute SSC. Birth year is mandatory.**

---

## Step 1: Determine Class [T1]

**Legislation:** Social Security Act, Chapter 318

| Class | Who | Rate |
|-------|-----|------|
| Class 1 | Employees | 10% employee + 10% employer |
| Class 1A | Employers (maternity fund) | 0.3% of gross salary |
| Class 2 | Self-employed / Self-occupied | 15% of net income (clamped to min/max) |

**Self-occupied vs Self-employed (same rates, different benefits):**
- Self-occupied: trades, businesses, professions (accountant, plumber, shop owner). Entitled to pension + short-term benefits (sickness, injury, maternity).
- Self-employed: income from rents, investments, capital gains. Entitled to pension only.

**If client is both fully employed (Class 1) and has side income:** Class 1 covers everything. NO Class 2 due. See Step 5.

---

## Step 2: Class 2 Rate Calculation [T1]

**Legislation:** Social Security Act, Chapter 318; MTCA Class 2 Rate Table 2026

### Formula
```
SSC = clamp(prior_year_net_income × 15%, minimum, maximum)
```

Where minimum and maximum are:

| Category | Condition | Weekly | Annual |
|----------|-----------|--------|--------|
| SA (minimum) | Net income <= EUR 12,543.72 OR first year | EUR 36.18 | EUR 1,881.36 |
| SB (15% rate) | EUR 12,543.73 to cap threshold | 15% of net | 15% of net |
| SC (maximum, pre-1962) | Born before 1 Jan 1962, income above EUR 25,499.99 | EUR 73.56 | EUR 3,825.12 |
| SC (maximum, post-1962) | Born on/after 1 Jan 1962, income above EUR 29,083.35 | EUR 83.89 | EUR 4,362.28 |

**Birth year affects ONLY the SC maximum. It does NOT affect SA minimum or the 15% SB rate.**

**Born exactly on 1 January 1962 = post-1962 (on or after).**

### Calculation Examples (2026)

| Prior Year Net Income | Birth Year | Category | Annual SSC |
|----------------------|-----------|----------|-----------|
| EUR 8,000 | 1990 | SA | EUR 1,881.36 |
| EUR 0 | 1990 | SA | EUR 1,881.36 |
| EUR 20,000 | 1990 | SB | EUR 3,000.00 |
| EUR 20,000 | 1955 | SB | EUR 3,000.00 |
| EUR 50,000 | 1990 | SC (post-1962) | EUR 4,362.28 |
| EUR 50,000 | 1955 | SC (pre-1962) | EUR 3,825.12 |

---

## Step 3: Key Rules [T1]

**Legislation:** Social Security Act, Chapter 318

1. **SSC is based on PRIOR year net income.** 2026 SSC = based on 2025 net income from filed TA24. Not current year estimates.
2. **First year of self-employment = SA minimum.** This is a legislative provision, not just a default.
3. **No prior year TA24 filed = SA minimum** until DSS assessment is made.
4. **Minimum always applies.** Even at zero income, the SA minimum is due once registered.
5. **Net income = gross income minus allowable deductions** -- same deductions as income tax.

---

## Step 4: Payment Schedule [T1]

**Legislation:** Social Security Act, Chapter 318; DSS Malta annual schedule

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | Jan -- Mar | 30 April |
| Q2 | Apr -- Jun | 31 July |
| Q3 | Jul -- Sep | 31 October |
| Q4 | Oct -- Dec | 31 January (following year) |

- Payment method: Direct Debit or bank transfer to DSS
- Exact dates are set annually by DSS; dates above are standard

---

## Step 5: TA22 Part-Time Self-Employment Rule [T1]

**Legislation:** Income Tax Act, Article 4C; Social Security Act, Chapter 318

| Scenario | SSC Treatment |
|----------|--------------|
| Full-time employed + part-time self-employed | Class 1 covers everything. NO Class 2. |
| Part-time self-employed only (TA22 regime) | Class 2 applies. SA minimum in first year. |

**"Fully employed" is defined by the employment contract and hours, not by income level.**

If there is any doubt about whether the client's employment qualifies as full-time, [T2] flag for reviewer.

---

## Step 6: Maternity Fund (Class 1A) [T1]

**Legislation:** Social Security Act, Chapter 318

- Rate: 0.3% of gross salary
- Who pays: Employer only
- Self-employed / self-occupied: NOT applicable. Do not include in Class 2 calculation.
- Self-occupied persons are entitled to maternity benefits from Class 2 contributions but pay no separate maternity fund.

---

## Step 7: Registration [T1]

| Requirement | Detail |
|-------------|--------|
| When | Within 2 weeks of starting self-employment |
| With whom | Department of Social Security (DSS) |
| Income threshold | EUR 910/year from self-employment triggers obligation |
| Below EUR 910 | May be exempt but should still register |
| Form | SSC registration form (from DSS) |
| Required documents | ID card, VAT certificate (if registered), TA4 (if applicable) |

---

## Step 8: Interaction with Income Tax [T1]

**Legislation:** Income Tax Act, Article 14

| Question | Answer |
|----------|--------|
| Is SSC deductible? | YES -- deducted in Box 20 of the TA24 |
| Which year's SSC? | SSC paid in Year X is deducted in Year X's TA24 |
| Does it reduce taxable income? | Yes -- SSC is subtracted before tax rates are applied |

**Accora implementation:** `tax-return-service.ts` includes SSC in Box 20. `calculate_ssc_class2()` RPC is called during tax return preparation.

---

## Step 9: Penalties [T1]

**Legislation:** Social Security Act, Article 116

| Penalty | Rate |
|---------|------|
| Late payment | 1% per month on outstanding amount |
| Non-registration | All unpaid contributions + penalties |
| Arrears lookback | DSS can claim up to 5 years of unpaid SSC |
| Arrears rate (post-1962) | Calculated at CURRENT rates, not rates when originally due |

**WARNING:** Unlike VAT penalties (capped at EUR 250), SSC penalties are uncapped. 1% per month compounds indefinitely. Arrears situations must be escalated to warranted accountant immediately.

---

## Step 10: Exemptions and Reduced Rates [T2]

The following categories may qualify for exemptions or reduced rates. These are all [T2] -- do not apply without reviewer confirmation.

| Category | Treatment |
|----------|-----------|
| Students (18-24, in full-time education) | Credited contributions (government pays) |
| Pensioners (receiving pension, still working) | Pro-rata reduced rate -- confirm with DSS |
| Certain female categories | Pro-rata reduced rate provisions exist |
| Disabled persons | May qualify for exemption -- confirm with DSS |

**Flag for reviewer whenever any of these categories applies.**

---

## Step 11: Edge Case Registry

### EC1 -- Mid-year switch from employment to self-employment [T1]
**Situation:** Client was employed (Class 1) until June, then became self-employed from July.
**Resolution:** Class 1 stops when employment ends. Class 2 starts when self-employment begins. First-year SA minimum applies for the self-employment period. Quarterly SSC payments due from Q3 onward in year of switch.

### EC2 -- Born exactly 1 January 1962 [T1]
**Situation:** Client's date of birth is 1 January 1962.
**Resolution:** Classified as post-1962. SC maximum = EUR 4,362.28 annually.

### EC3 -- Zero or negative net income [T1]
**Situation:** Client had a loss year. Net income is negative.
**Resolution:** SA minimum still applies (EUR 1,881.36 for 2026). There is no zero-SSC outcome once registered.

### EC4 -- Dual status ambiguity (employed but also director) [T2]
**Situation:** Client is a full-time employee but also a director of their own company drawing a director's fee.
**Resolution:** Director fees from a company where the client is NOT a full-time employee may trigger Class 2. If the client is a full-time employee of the same or another company with Class 1 already paid, Class 2 is not due. [T2] flag for reviewer -- confirm employment contract status and hours before advising.

### EC5 -- Returning self-employed (was self-employed before, stopped, now restarting) [T1]
**Situation:** Client was self-employed 5 years ago, stopped, and is now restarting.
**Resolution:** SA minimum does NOT automatically apply. SA applies only to genuine first-timers. Returning self-employed are assessed on prior year income. If no prior year TA24 for self-employment, SA applies until assessment. [T2] flag for reviewer to confirm with DSS.

### EC6 -- SSC arrears from prior years [T2]
**Situation:** Client has unpaid SSC from previous years.
**Resolution:** DSS can recover up to 5 years. Arrears are calculated at current rates (not historical rates) for post-1962 clients. 1% per month penalty accrues from each missed payment. Do not attempt to quantify arrears without a DSS statement. [T2] escalate to warranted accountant immediately. Do not present an estimate as definitive.

### EC7 -- TA22 client with multiple part-time income sources [T2]
**Situation:** Client has two part-time self-employment activities, neither with full-time employment.
**Resolution:** TA22 requires that the client has NO full-time employment. If both activities are part-time and no full-time employment exists, Class 2 applies. [T2] flag for reviewer -- confirm whether TA22 applies to all activities or whether one tips into full-time equivalence.

### EC8 -- First year, no income yet [T1]
**Situation:** Client registered as self-employed in 2026 but has not yet earned any income.
**Resolution:** SA minimum applies from date of registration. EUR 1,881.36 for 2026, paid quarterly. Minimum is due regardless of income level.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Warranted accountant must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to warranted accountant. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard post-1962, mid-range income
**Input:** Born 1985, prior year net income EUR 20,000, not first year.
**Expected output:** Category SB. Annual SSC = EUR 3,000.00 (15% x EUR 20,000). Quarterly = EUR 750.00.

### Test 2 -- Pre-1962, capped at SC maximum
**Input:** Born 1958, prior year net income EUR 60,000, not first year.
**Expected output:** Category SC (pre-1962). Annual SSC = EUR 3,825.12. Quarterly = EUR 956.28.

### Test 3 -- Post-1962, capped at SC maximum
**Input:** Born 1975, prior year net income EUR 60,000, not first year.
**Expected output:** Category SC (post-1962). Annual SSC = EUR 4,362.28. Quarterly = EUR 1,090.57.

### Test 4 -- Below minimum threshold
**Input:** Born 1990, prior year net income EUR 5,000, not first year.
**Expected output:** Category SA. Annual SSC = EUR 1,881.36 (minimum applies). Quarterly = EUR 470.34.

### Test 5 -- First year, no prior income
**Input:** Born 1988, first year of self-employment, no prior TA24.
**Expected output:** Category SA (first year legislative provision). Annual SSC = EUR 1,881.36. Quarterly = EUR 470.34.

### Test 6 -- Full-time employed + side income
**Input:** Client is a full-time employee paying Class 1. Also earns EUR 8,000 from freelance work.
**Expected output:** NO Class 2 due. Class 1 covers all SSC obligations. TA22 regime may apply for income tax on side income.

### Test 7 -- Zero income, still registered
**Input:** Born 1992, registered self-employed, net income EUR 0 in prior year.
**Expected output:** Category SA. Annual SSC = EUR 1,881.36. Minimum always applies.

### Test 8 -- SSC deductibility on TA24
**Input:** Client paid EUR 3,000 SSC in 2025. Preparing 2025 TA24.
**Expected output:** EUR 3,000 entered in Box 20 of TA24 as deduction from income before tax calculation.

---

## PROHIBITIONS

- NEVER compute SSC without knowing the client's birth year
- NEVER use current year income -- SSC is always based on PRIOR year net income
- NEVER tell a client they owe zero SSC because their income is low -- minimum always applies once registered
- NEVER apply SA minimum to a returning self-employed without reviewer confirmation
- NEVER advise on SSC arrears without a DSS statement -- do not estimate
- NEVER conflate Class 1 and Class 2 -- they are entirely separate obligations
- NEVER include maternity fund (Class 1A) in Class 2 calculations
- NEVER present SSC figures as definitive -- always label as estimated and direct client to their DSS statement for confirmation
- NEVER compute SSC penalties without escalating to a warranted accountant

---

## Contribution Notes (For Non-Malta Jurisdictions)

If adapting this skill for another country:

1. Replace Chapter 318 references with the equivalent national social security legislation.
2. Replace the Class 1 / Class 2 distinction with your jurisdiction's equivalent employee / self-employed contribution classes.
3. Replace rate percentages (15%), minimum (EUR 1,881.36), and maximum caps with your jurisdiction's current year figures.
4. Replace the birth year cutoff (1 January 1962) with any equivalent generational threshold in your jurisdiction, or remove if none exists.
5. Replace payment schedule (quarterly) with your jurisdiction's equivalent.
6. Replace the TA22 part-time regime with your jurisdiction's equivalent treatment for dual employment/self-employment status.
7. Replace income tax deductibility rules (Box 20 of TA24) with your jurisdiction's equivalent.
8. Have a licensed practitioner in your jurisdiction validate every T1 rule before publishing.
9. Add jurisdiction-specific edge cases to the Edge Case Registry.

**A skill may not be published without sign-off from a warranted practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
