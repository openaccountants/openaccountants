---
name: kr-social-insurance
description: Use this skill whenever asked about South Korean social insurance contributions for self-employed persons. Trigger on phrases like "National Pension Korea", "NPS self-employed", "Korean health insurance", "NHIS self-employed", "long-term care insurance Korea", "Korean social insurance", "4 major insurances Korea", or any question about social insurance obligations for a self-employed client in South Korea. This skill covers National Pension (NPS), National Health Insurance (NHIS), Long-Term Care Insurance, Employment Insurance, and Industrial Accident Insurance as they apply to self-employed individuals. ALWAYS read this skill before touching any Korean social insurance-related work.
---

# South Korea Social Insurance Contributions -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | South Korea |
| Jurisdiction Code | KR |
| Primary Legislation | National Pension Act (국민연금법); National Health Insurance Act (국민건강보험법); Long-Term Care Insurance Act (노인장기요양보험법); Employment Insurance Act (고용보험법); Industrial Accident Compensation Insurance Act (산업재해보상보험법) |
| Supporting Legislation | Income Tax Act (소득세법) -- deductibility of NPS and NHIS contributions |
| Tax Authority | National Pension Service (NPS / 국민연금공단); National Health Insurance Service (NHIS / 국민건강보험공단); Ministry of Employment and Labor |
| Rate Publisher | NPS and NHIS (publish annual rate tables and ceiling adjustments) |
| Contributor | Open Accountants |
| Validated By | Pending -- licensed Korean practitioner (세무사/공인회계사) sign-off required |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: NPS rate/ceiling, NHIS rate, LTCI rate, payment schedule, tax deductibility. Tier 2: NHIS property-based assessment for self-employed, income reclassification, voluntary employment insurance. Tier 3: disability exemptions, international social security agreements, arrears disputes. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Licensed practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any social insurance figure, you MUST know:

1. **Age** [T1] -- NPS is mandatory for persons aged 18 to 59
2. **Employment status** [T1] -- self-employed (개인사업자), freelancer (프리랜서), or dual (employed + side self-employment)
3. **Monthly reported income** [T1] -- basis for NPS contributions
4. **Property and vehicle ownership** [T2] -- affects NHIS calculation for self-employed (지역가입자)
5. **Number of household members on NHIS** [T2] -- NHIS for self-employed is household-based
6. **Is there any employment (근로소득)?** [T1] -- if fully employed, employer handles all 4 insurances; self-employment income may trigger additional NHIS

**If monthly income is unknown, STOP. Do not compute NPS. Income is mandatory for NPS calculation.**

---

## Step 1: Overview of the Four Major Social Insurances [T1]

**South Korea operates a "4 major social insurance" (4대 보험) system:**

| Insurance | Applies to Self-Employed? | Self-Employed Pays |
|-----------|--------------------------|-------------------|
| National Pension (NPS / 국민연금) | YES -- mandatory for ages 18-59 | Full 9% (no employer share) |
| National Health Insurance (NHIS / 국민건강보험) | YES -- mandatory for all residents | Full contribution (income + property based) |
| Long-Term Care Insurance (장기요양보험) | YES -- mandatory (add-on to NHIS) | Percentage of NHIS premium |
| Employment Insurance (고용보험) | NO -- not applicable (voluntary opt-in available) | N/A unless voluntarily enrolled |
| Industrial Accident Insurance (산재보험) | NO -- not applicable for most self-employed | N/A (some high-risk occupations may opt in) |

---

## Step 2: National Pension (NPS) [T1]

**Legislation:** National Pension Act (국민연금법)

### Rate

| Item | 2025 Rate |
|------|-----------|
| Total contribution rate | 9.0% of monthly income |
| Employee share (if employed) | 4.5% |
| Employer share (if employed) | 4.5% |
| **Self-employed share** | **9.0% (full amount, no employer)** |

**From 2026:** The NPS contribution rate will increase to 9.5%, rising by 0.5% per year until reaching 13.0% in 2033 under the pension reform enacted in 2025.

### Income Ceiling and Floor

The NPS contribution base has upper and lower limits, adjusted annually every July:

| Period | Monthly Income Floor | Monthly Income Ceiling |
|--------|---------------------|----------------------|
| Jan 2025 -- Jun 2025 | KRW 390,000 | KRW 6,170,000 |
| Jul 2025 -- Jun 2026 | KRW 400,000 | KRW 6,370,000 |

### Contribution Calculation

```
Monthly NPS = clamp(reported_monthly_income, floor, ceiling) x 9%
```

| Example Monthly Income | Period | NPS Base | Monthly NPS |
|-----------------------|--------|----------|-------------|
| KRW 3,000,000 | Jul 2025 | KRW 3,000,000 | KRW 270,000 |
| KRW 8,000,000 | Jul 2025 | KRW 6,370,000 (capped) | KRW 573,300 |
| KRW 300,000 | Jul 2025 | KRW 400,000 (floor) | KRW 36,000 |

### Key Rules

1. **Self-employed pay the full 9%.** There is no employer to share the burden.
2. **Income is self-reported** to NPS. NPS may adjust based on tax return data.
3. **Ages 18 to 59 are mandatory.** Persons aged 60-64 may voluntarily continue (임의계속가입).
4. **Exemptions:** Persons with no income, students, and military service members may apply for contribution exemption (납부예외). The exemption must be applied for -- it is not automatic.

---

## Step 3: National Health Insurance (NHIS) [T1/T2]

**Legislation:** National Health Insurance Act (국민건강보험법)

### Classification

| Category | Korean Term | Who |
|----------|------------|-----|
| Workplace insured | 직장가입자 | Employees and their dependants |
| Community insured | 지역가입자 | Self-employed, freelancers, and others not covered by workplace insurance |

**Self-employed persons are classified as community insured (지역가입자).** Their NHIS premium is calculated differently from employees.

### NHIS Rate for 2025

| Item | 2025 Rate |
|------|-----------|
| NHIS premium rate (nominal) | 7.09% |
| Employee share (if employed) | 3.545% |
| Employer share (if employed) | 3.545% |

### Self-Employed (Community Insured) Calculation [T2]

For self-employed persons, NHIS contributions are NOT a simple percentage of income. The calculation is based on:

1. **Income score** -- derived from reported income (근로소득, 사업소득, 이자/배당소득, etc.)
2. **Property score** -- derived from property ownership (real estate, vehicles)
3. **Vehicle score** -- derived from vehicle value and age

```
Monthly NHIS Premium = (Income Score + Property Score + Vehicle Score) x Point Value per Score
```

| Item | 2025 Value |
|------|-----------|
| Point value per score (부과점수당 금액) | KRW 211.5 |

**Since September 2022**, the self-employed calculation has been reformed to weight income more heavily (income-based portion increased, property-based portion reduced). However, property and vehicles still factor into the calculation.

**[T2] The exact NHIS premium for a self-employed person cannot be computed without knowing income, property, and vehicle details. Flag for reviewer or direct the client to the NHIS premium calculator.**

### NHIS Floor and Cap

| Item | Amount |
|------|--------|
| Monthly minimum premium | Approximately KRW 19,780 (2025) |
| Monthly maximum premium | Adjusted annually; approximately KRW 4,240,710 (2025, verify with NHIS) |

---

## Step 4: Long-Term Care Insurance [T1]

**Legislation:** Long-Term Care Insurance Act (노인장기요양보험법)

Long-Term Care Insurance (LTCI) is not a separate enrolment -- it is automatically calculated as a percentage of the NHIS premium.

| Item | 2025 Rate |
|------|-----------|
| LTCI rate (as % of NHIS premium) | 12.95% |

### Calculation

```
Monthly LTCI = NHIS Premium x 12.95%
```

### Example

| NHIS Premium | LTCI (12.95%) | Total Health + LTCI |
|-------------|---------------|---------------------|
| KRW 200,000 | KRW 25,900 | KRW 225,900 |
| KRW 500,000 | KRW 64,750 | KRW 564,750 |

**From 2026:** The LTCI rate increases to 13.14% of NHIS premium.

---

## Step 5: Employment Insurance [T1]

**Legislation:** Employment Insurance Act (고용보험법)

| Item | Detail |
|------|--------|
| Mandatory for self-employed? | NO |
| Voluntary enrolment available? | YES -- self-employed persons may opt in (자영업자 고용보험) |
| Eligibility for voluntary enrolment | Self-employed persons with at least 1 employee, or certain solo self-employed categories |
| Voluntary rate | Varies by selected insured income grade (7 grades available) |
| Benefits if enrolled | Unemployment benefits (실업급여) if business closes |

**Default position: self-employed persons are NOT covered by employment insurance unless they voluntarily enrol.**

---

## Step 6: Industrial Accident Insurance [T1]

**Legislation:** Industrial Accident Compensation Insurance Act (산업재해보상보험법)

| Item | Detail |
|------|--------|
| Mandatory for self-employed? | NO (mandatory only for employers with employees) |
| Voluntary enrolment available? | YES -- for certain high-risk self-employed occupations (특수형태근로종사자 or solo operators in designated industries) |
| Common voluntary categories | Construction, transportation, delivery, insurance sales agents |

**Default position: most self-employed persons are NOT covered by industrial accident insurance.**

---

## Step 7: Payment Schedule [T1]

**Legislation:** National Pension Act; National Health Insurance Act

### NPS Payment

| Item | Detail |
|------|--------|
| Frequency | Monthly |
| Due date | **10th of the following month** (e.g., January contribution due by 10 February) |
| Payment method | Bank transfer, auto-debit, or at designated banks/post offices |
| Grace period | None -- contributions are delinquent after the 10th |

### NHIS + LTCI Payment

| Item | Detail |
|------|--------|
| Frequency | Monthly |
| Due date | **25th of each month** (for community insured / self-employed) |
| Payment method | Bank transfer, auto-debit, credit card, or at designated locations |

**If the due date falls on a weekend or public holiday, payment is due by the next business day.**

---

## Step 8: Income Reporting and Adjustment [T1]

### NPS Income Reporting

| Item | Detail |
|------|--------|
| Initial report | Self-employed report their monthly income when first registering with NPS |
| Annual adjustment | NPS adjusts contribution base every July based on reported income from the prior year's tax return |
| Voluntary adjustment | Self-employed may request an income change at any time if circumstances change (income increase or decrease) |
| Verification | NPS cross-references with National Tax Service (NTS / 국세청) data from tax returns |

### NHIS Income Reporting

| Item | Detail |
|------|--------|
| Annual adjustment | NHIS adjusts premiums annually based on income and property data from NTS and local government records |
| Notification | NHIS sends a premium adjustment notice; effective date is typically November of each year |
| Appeal | Self-employed may appeal premium adjustments within 90 days |

---

## Step 9: Tax Deductibility [T1]

**Legislation:** Income Tax Act (소득세법)

| Contribution | Tax Treatment |
|-------------|---------------|
| National Pension (NPS) | **Income deduction (소득공제)** -- deducted from gross income before tax calculation. The full amount of NPS contributions paid is deductible. |
| National Health Insurance (NHIS) | **Itemized deduction (특별세액공제 / 보험료 세액공제)** -- 12% of NHIS + LTCI premiums paid is credited against tax liability (not deducted from income). |
| Long-Term Care Insurance | Combined with NHIS for the 12% tax credit calculation. |
| Employment Insurance (if voluntarily enrolled) | Treated same as NHIS -- 12% tax credit. |

### Key Distinction

- **NPS = income deduction (reduces taxable income directly).** This is more valuable for higher-income earners.
- **NHIS/LTCI = tax credit (reduces tax payable by 12% of premiums paid).** This benefits all income levels equally.

### Example

| Item | Amount | Tax Benefit |
|------|--------|-------------|
| NPS paid | KRW 3,240,000/year | Reduces taxable income by KRW 3,240,000 |
| NHIS + LTCI paid | KRW 2,400,000/year | Tax credit = KRW 2,400,000 x 12% = KRW 288,000 |

---

## Step 10: Edge Case Registry

### EC1 -- Dual status: employed and self-employed [T2]
**Situation:** Client is employed full-time (workplace insured) and also has self-employment income.
**Resolution:** NPS: No additional NPS on self-employment income if already paying NPS as an employee (workplace insured takes precedence). NHIS: Additional NHIS premium may be assessed on self-employment income exceeding KRW 20 million/year. [T2] flag for reviewer to verify NHIS supplementary premium rules.

### EC2 -- Self-employed with zero or very low income [T1]
**Situation:** Client registered as self-employed but has no income or income below the NPS floor.
**Resolution:** NPS: May apply for contribution exemption (납부예외) due to no income. The exemption is not automatic -- must be applied for. NHIS: Minimum premium of approximately KRW 19,780/month still applies.

### EC3 -- Turning 60 during the year [T1]
**Situation:** Client turns 60, which is the NPS mandatory upper age limit.
**Resolution:** NPS contributions cease from the month after turning 60. Client may opt for voluntary continued enrolment (임의계속가입) until age 65. NHIS and LTCI continue -- there is no age limit for health insurance.

### EC4 -- Newly registered self-employed [T1]
**Situation:** Client just registered as a self-employed person and has no prior tax return.
**Resolution:** NPS: Client self-reports expected monthly income. NPS may accept the declared amount until the first tax return is available for verification. NHIS: Initial premium is assessed based on available data; may be adjusted after first tax filing.

### EC5 -- Foreign national self-employed in Korea [T2]
**Situation:** Client is a foreign national operating as self-employed in South Korea.
**Resolution:** NPS: Mandatory for foreign nationals from countries with reciprocal social security agreements. Nationals from countries without agreements may be exempt or may contribute without pension benefits. NHIS: Mandatory for all foreign residents staying 6+ months. [T2] flag for reviewer -- check the specific bilateral agreement.

### EC6 -- Self-employed with employees [T1]
**Situation:** Client is a self-employed person who also employs staff.
**Resolution:** The client's own contributions follow self-employed rules (this skill). For employees, the client must register as a workplace and pay employer shares of all 4 insurances for the employees. This is a separate obligation outside the scope of this skill.

### EC7 -- NPS ceiling adjustment mid-year (July) [T1]
**Situation:** Client's income exceeds the NPS ceiling, and the ceiling changes in July.
**Resolution:** NPS contributions for January-June use the pre-July ceiling. From July onward, the new ceiling applies. The transition is automatic -- NPS adjusts the contribution notice.

### EC8 -- NHIS premium dispute [T2]
**Situation:** Client believes their NHIS premium is too high relative to actual income.
**Resolution:** Self-employed may request a premium adjustment by submitting updated income documentation to NHIS. Appeals must be filed within 90 days of the premium notice. [T2] flag for reviewer.

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Licensed Korean practitioner (세무사/공인회계사) must confirm before advising client.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed Korean practitioner. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Standard self-employed, income KRW 3,000,000/month
**Input:** Age 35, monthly income KRW 3,000,000, period Jul 2025+.
**Expected output:** NPS = KRW 3,000,000 x 9% = KRW 270,000/month. NHIS = computed via point system (requires property/vehicle data -- flag [T2]). LTCI = NHIS premium x 12.95%.

### Test 2 -- Income above NPS ceiling
**Input:** Age 40, monthly income KRW 8,000,000, period Jul 2025+.
**Expected output:** NPS base capped at KRW 6,370,000. NPS = KRW 6,370,000 x 9% = KRW 573,300/month.

### Test 3 -- Income below NPS floor
**Input:** Age 25, monthly income KRW 300,000, period Jul 2025+.
**Expected output:** NPS base raised to floor KRW 400,000. NPS = KRW 400,000 x 9% = KRW 36,000/month. Alternatively, client may apply for contribution exemption if no assessable income.

### Test 4 -- Age 60, NPS cessation
**Input:** Age 60 (turned 60 in March 2025), monthly income KRW 4,000,000.
**Expected output:** NPS contributions cease from April 2025 (month after turning 60). Client may opt for voluntary continued enrolment. NHIS and LTCI continue unchanged.

### Test 5 -- Tax deductibility calculation
**Input:** Annual NPS paid = KRW 3,240,000. Annual NHIS + LTCI paid = KRW 2,400,000.
**Expected output:** NPS: income deduction of KRW 3,240,000 (reduces taxable income). NHIS + LTCI: tax credit of KRW 288,000 (= KRW 2,400,000 x 12%).

### Test 6 -- Employment insurance voluntary enrolment
**Input:** Self-employed person with 3 employees wants to know about unemployment coverage.
**Expected output:** Eligible for voluntary employment insurance. Not mandatory. If enrolled, benefits include unemployment payments if business closes. Contributions based on selected income grade.

### Test 7 -- NPS ceiling transition (Jan-Jun vs Jul-Dec)
**Input:** Age 45, monthly income KRW 6,300,000, full year 2025.
**Expected output:** Jan-Jun: NPS base = KRW 6,170,000 (capped at pre-July ceiling). NPS = KRW 555,300/month. Jul-Dec: NPS base = KRW 6,300,000 (below new ceiling of KRW 6,370,000). NPS = KRW 567,000/month.

### Test 8 -- LTCI computation
**Input:** NHIS monthly premium = KRW 350,000.
**Expected output:** LTCI = KRW 350,000 x 12.95% = KRW 45,325/month. Total health insurance burden = KRW 395,325/month.

---

## PROHIBITIONS

- NEVER compute NPS without knowing the client's monthly reported income
- NEVER apply the employee NPS rate (4.5%) to a self-employed person -- self-employed pay the full 9%
- NEVER compute NHIS for a self-employed person using only the 7.09% rate -- the community insured calculation requires income, property, and vehicle data
- NEVER tell a client that employment insurance or industrial accident insurance is mandatory for self-employed -- it is voluntary (with limited exceptions)
- NEVER ignore the NPS ceiling change that occurs every July
- NEVER conflate NPS income deduction with NHIS/LTCI tax credit -- they are different tax mechanisms
- NEVER assume NPS contribution exemption is automatic -- it must be applied for
- NEVER advise on bilateral social security agreements without [T2] reviewer confirmation
- NEVER present social insurance figures as definitive -- always label as estimated and direct client to their NPS/NHIS notices for confirmation
- NEVER compute arrears or penalties without escalating to a licensed practitioner

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
