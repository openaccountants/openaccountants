---
name: kr-social-insurance
description: >
  Use this skill whenever asked about South Korean social insurance contributions for self-employed persons. Trigger on phrases like "National Pension Korea", "NPS self-employed", "Korean health insurance", "NHIS self-employed", "long-term care insurance Korea", "Korean social insurance", "4 major insurances Korea", or any question about social insurance obligations for a self-employed client in South Korea. This skill covers National Pension (NPS), National Health Insurance (NHIS), Long-Term Care Insurance, Employment Insurance, and Industrial Accident Insurance as they apply to self-employed individuals. ALWAYS read this skill before touching any Korean social insurance-related work.
version: 2.0
jurisdiction: KR
tax_year: 2025
category: international
---

# South Korea Social Insurance Contributions -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

Read this whole section before computing anything.

| Field | Value |
|---|---|
| Country | South Korea |
| Jurisdiction Code | KR |
| Primary Legislation | National Pension Act; National Health Insurance Act; Long-Term Care Insurance Act; Employment Insurance Act; Industrial Accident Compensation Insurance Act |
| Supporting Legislation | Income Tax Act -- deductibility of NPS and NHIS contributions |
| Tax Authority | National Pension Service (NPS); National Health Insurance Service (NHIS); Ministry of Employment and Labor |
| Tax Year | 2025 |
| Currency | KRW only |
| Contributor | Open Accountants |
| Validated By | Pending -- licensed Korean practitioner sign-off required |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: NPS rate/ceiling, NHIS rate, LTCI rate, payment schedule, tax deductibility. Tier 2: NHIS property-based assessment, income reclassification, voluntary employment insurance. Tier 3: disability exemptions, international social security agreements, arrears disputes. |

**NPS key figures (2025):**

| Item | Value |
|---|---|
| Total contribution rate | 9.0% of monthly income |
| Self-employed share | 9.0% (full amount, no employer) |
| Monthly income floor (Jan-Jun 2025) | KRW 390,000 |
| Monthly income ceiling (Jan-Jun 2025) | KRW 6,170,000 |
| Monthly income floor (Jul 2025-Jun 2026) | KRW 400,000 |
| Monthly income ceiling (Jul 2025-Jun 2026) | KRW 6,370,000 |
| From 2026 | Rate increases to 9.5%, rising 0.5%/year to 13.0% by 2033 |

**Four major social insurances overview:**

| Insurance | Applies to Self-Employed? | Self-Employed Pays |
|---|---|---|
| National Pension (NPS) | YES -- mandatory ages 18-59 | Full 9% |
| National Health Insurance (NHIS) | YES -- mandatory for all residents | Full contribution (income + property based) |
| Long-Term Care Insurance (LTCI) | YES -- add-on to NHIS | 12.95% of NHIS premium |
| Employment Insurance | NO (voluntary opt-in available) | N/A unless enrolled |
| Industrial Accident Insurance | NO for most self-employed | N/A (some high-risk occupations may opt in) |

**NHIS key figures (2025):**

| Item | Value |
|---|---|
| NHIS premium rate (nominal) | 7.09% |
| Point value per score (community insured) | KRW 211.5 |
| Monthly minimum premium | ~KRW 19,780 |
| LTCI rate (as % of NHIS premium) | 12.95% |
| LTCI rate from 2026 | 13.14% |

**Tax treatment:**

| Contribution | Tax Benefit |
|---|---|
| NPS | Income deduction -- reduces taxable income directly |
| NHIS + LTCI | Tax credit -- 12% of premiums paid credited against tax |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown monthly income | Use NPS floor (KRW 400,000 from Jul 2025) |
| Unknown NHIS property/vehicle data | Flag for reviewer -- cannot compute without data |
| Unknown employment status | Treat as self-employed (community insured) |
| Unknown age for NPS | Assume mandatory (age 18-59) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any social insurance figure, you MUST know:

1. Age -- NPS is mandatory for persons aged 18 to 59
2. Employment status -- self-employed, freelancer, or dual (employed + side self-employment)
3. Monthly reported income -- basis for NPS contributions
4. Property and vehicle ownership -- affects NHIS calculation for community insured
5. Number of household members on NHIS -- NHIS for self-employed is household-based
6. Is there any employment income? -- if fully employed, employer handles all 4 insurances

If monthly income is unknown, STOP. Do not compute NPS. Income is mandatory for NPS calculation.

### Refusal catalogue

**R-KR-SI-1 -- Disability exemption.** Trigger: client asks about NPS exemption due to disability. Message: "NPS disability exemptions require verification of disability status with NPS. This is outside this skill's scope. Please escalate to a licensed Korean practitioner."

**R-KR-SI-2 -- International social security agreement.** Trigger: client is a foreign national asking about NPS obligations under a bilateral agreement. Message: "NPS obligations for foreign nationals depend on the specific bilateral social security agreement between South Korea and the client's home country. Please escalate to a licensed Korean practitioner."

**R-KR-SI-3 -- Arrears disputes.** Trigger: client disputes accumulated NPS or NHIS arrears. Message: "Arrears disputes require direct engagement with NPS or NHIS. This skill cannot advise on dispute resolution. Please escalate to a licensed Korean practitioner."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement entries related to social insurance. Match by case-insensitive substring on the counterparty name or transaction description.

### 3.1 National Pension (NPS) debits

| Pattern | Treatment | Notes |
|---|---|---|
| NPS, NATIONAL PENSION, 국민연금 | NPS CONTRIBUTION | Monthly contribution -- due by 10th of following month |
| 국민연금공단, PENSION SERVICE | NPS CONTRIBUTION | Same |
| NPS REFUND, 연금환급 | NPS REFUND | Overpayment refund or exemption-related |

### 3.2 National Health Insurance (NHIS) debits

| Pattern | Treatment | Notes |
|---|---|---|
| NHIS, 국민건강보험, 건강보험공단 | NHIS + LTCI PREMIUM | Monthly premium -- due by 25th of month (community insured) |
| HEALTH INSURANCE, 건강보험료 | NHIS PREMIUM | Same |
| 장기요양, LONG-TERM CARE | LTCI COMPONENT | Automatically included in NHIS billing |

### 3.3 Employment Insurance (voluntary -- rare for self-employed)

| Pattern | Treatment | Notes |
|---|---|---|
| 고용보험, EMPLOYMENT INSURANCE | VOLUNTARY EI PREMIUM | Only if self-employed person has voluntarily enrolled |
| 근로복지공단 | EI or INDUSTRIAL ACCIDENT | Verify which insurance -- could be either |

### 3.4 Tax authority (income reporting triggers)

| Pattern | Treatment | Notes |
|---|---|---|
| NTS, 국세청, NATIONAL TAX SERVICE | TAX PAYMENT | Income tax payment; NPS/NHIS adjust based on NTS data |
| HOMETAX, 홈택스 | TAX FILING | Filing portal -- triggers income data cross-reference |

---

## Section 4 -- NPS computation rules

### 4.1 NPS eligibility (Tier 1)

Legislation: National Pension Act

Self-employed pay the full 9%. There is no employer to share the burden. Income is self-reported to NPS. NPS may adjust based on tax return data.

Ages 18 to 59 are mandatory. Persons aged 60-64 may voluntarily continue. Exemptions (for no income, students, military) must be applied for -- they are not automatic.

### 4.2 NPS computation (Tier 1)

```
Monthly NPS = clamp(reported_monthly_income, floor, ceiling) x 9%
```

| Example Monthly Income | Period | NPS Base | Monthly NPS |
|---|---|---|---|
| KRW 3,000,000 | Jul 2025+ | KRW 3,000,000 | KRW 270,000 |
| KRW 8,000,000 | Jul 2025+ | KRW 6,370,000 (capped) | KRW 573,300 |
| KRW 300,000 | Jul 2025+ | KRW 400,000 (floor) | KRW 36,000 |

### 4.3 NHIS computation -- community insured (Tier 2)

Legislation: National Health Insurance Act

For self-employed (community insured), NHIS is NOT a simple percentage of income:

```
Monthly NHIS Premium = (Income Score + Property Score + Vehicle Score) x Point Value per Score
```

Point value per score (2025): KRW 211.5

Since September 2022, income is weighted more heavily (property-based portion reduced). However, property and vehicles still factor in. The exact NHIS premium cannot be computed without knowing income, property, and vehicle details. Flag for reviewer or direct client to the NHIS premium calculator.

### 4.4 LTCI computation (Tier 1)

```
Monthly LTCI = NHIS Premium x 12.95%
```

LTCI is automatically calculated as a percentage of the NHIS premium. Not a separate enrolment.

---

## Section 5 -- Payment schedule and income reporting

### 5.1 Payment schedule (Tier 1)

NPS: Monthly, due by 10th of following month. Bank transfer, auto-debit, or at designated banks/post offices.

NHIS + LTCI: Monthly, due by 25th of each month (community insured). Bank transfer, auto-debit, credit card, or at designated locations.

If the due date falls on a weekend or public holiday, payment is due by the next business day.

### 5.2 Income reporting and adjustment (Tier 1)

NPS: Self-employed report monthly income when first registering. NPS adjusts every July based on prior year tax return. Voluntary adjustment requests accepted at any time.

NHIS: Adjusted annually based on income and property data from NTS and local government. Effective date typically November. Appeals within 90 days.

---

## Section 6 -- Tax deductibility and employment/accident insurance

### 6.1 Tax deductibility (Tier 1)

Legislation: Income Tax Act

NPS: income deduction -- the full amount paid is deducted from gross income before tax calculation. More valuable for higher-income earners.

NHIS + LTCI: itemized deduction (tax credit) -- 12% of premiums paid is credited against tax liability. Benefits all income levels equally.

### 6.2 Employment Insurance (Tier 1)

Not mandatory for self-employed. Voluntary enrolment available for self-employed with at least 1 employee or certain solo categories. Benefits include unemployment payments if business closes. Rate varies by selected insured income grade (7 grades).

### 6.3 Industrial Accident Insurance (Tier 1)

Not mandatory for most self-employed. Voluntary enrolment for certain high-risk occupations (construction, transportation, delivery, insurance sales).

---

## Section 7 -- Edge case registry

### EC1 -- Dual status: employed and self-employed (Tier 2)
Situation: Client is employed full-time and also has self-employment income.
Resolution: NPS: No additional NPS on self-employment income if already paying as workplace insured. NHIS: Additional NHIS premium may be assessed on self-employment income exceeding KRW 20 million/year. Flag for reviewer.

### EC2 -- Self-employed with zero or very low income (Tier 1)
Situation: Client registered as self-employed but has no income or income below the NPS floor.
Resolution: NPS: May apply for contribution exemption due to no income. Not automatic -- must be applied for. NHIS: Minimum premium of approximately KRW 19,780/month still applies.

### EC3 -- Turning 60 during the year (Tier 1)
Situation: Client turns 60.
Resolution: NPS contributions cease from the month after turning 60. Client may opt for voluntary continued enrolment until age 65. NHIS and LTCI continue -- no age limit.

### EC4 -- Newly registered self-employed (Tier 1)
Situation: Client just registered with no prior tax return.
Resolution: NPS: Client self-reports expected monthly income. NPS may accept declared amount until first tax return. NHIS: Initial premium assessed on available data; adjusted after first tax filing.

### EC5 -- Foreign national self-employed in Korea (Tier 2)
Situation: Client is a foreign national operating as self-employed.
Resolution: NPS: Mandatory for nationals from countries with reciprocal agreements. Others may be exempt or contribute without benefits. NHIS: Mandatory for all foreign residents staying 6+ months. Flag for reviewer -- check bilateral agreement.

### EC6 -- Self-employed with employees (Tier 1)
Situation: Client employs staff.
Resolution: The client's own contributions follow self-employed rules (this skill). For employees, the client must register as a workplace and pay employer shares -- separate obligation outside this skill.

### EC7 -- NPS ceiling adjustment mid-year (July) (Tier 1)
Situation: Client's income exceeds NPS ceiling, and ceiling changes in July.
Resolution: January-June uses pre-July ceiling. From July, new ceiling applies. NPS adjusts automatically.

### EC8 -- NHIS premium dispute (Tier 2)
Situation: Client believes NHIS premium is too high.
Resolution: May request adjustment by submitting updated income documentation to NHIS. Appeals within 90 days of premium notice. Flag for reviewer.

---

## Section 8 -- Reviewer escalation protocol

When a Tier 2 situation is identified:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Licensed Korean practitioner must confirm before advising client.
```

When a Tier 3 situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed Korean practitioner. Document gap.
```

---

## Section 9 -- Test suite

### Test 1 -- Standard self-employed, income KRW 3,000,000/month
Input: Age 35, monthly income KRW 3,000,000, period Jul 2025+.
Expected output: NPS = KRW 3,000,000 x 9% = KRW 270,000/month. NHIS = requires property/vehicle data (flag Tier 2). LTCI = NHIS premium x 12.95%.

### Test 2 -- Income above NPS ceiling
Input: Age 40, monthly income KRW 8,000,000, period Jul 2025+.
Expected output: NPS base capped at KRW 6,370,000. NPS = KRW 573,300/month.

### Test 3 -- Income below NPS floor
Input: Age 25, monthly income KRW 300,000, period Jul 2025+.
Expected output: NPS base raised to floor KRW 400,000. NPS = KRW 36,000/month. Client may apply for exemption.

### Test 4 -- Age 60, NPS cessation
Input: Age 60 (turned 60 in March 2025), monthly income KRW 4,000,000.
Expected output: NPS contributions cease from April 2025. Voluntary continued enrolment available. NHIS and LTCI continue.

### Test 5 -- Tax deductibility calculation
Input: Annual NPS paid = KRW 3,240,000. Annual NHIS + LTCI paid = KRW 2,400,000.
Expected output: NPS: income deduction of KRW 3,240,000. NHIS + LTCI: tax credit of KRW 288,000 (= KRW 2,400,000 x 12%).

### Test 6 -- Employment insurance voluntary enrolment
Input: Self-employed with 3 employees wants unemployment coverage.
Expected output: Eligible for voluntary employment insurance. Not mandatory. Benefits include unemployment payments if business closes.

### Test 7 -- NPS ceiling transition (Jan-Jun vs Jul-Dec)
Input: Age 45, monthly income KRW 6,300,000, full year 2025.
Expected output: Jan-Jun: NPS base = KRW 6,170,000 (capped). NPS = KRW 555,300/month. Jul-Dec: NPS base = KRW 6,300,000 (below new ceiling). NPS = KRW 567,000/month.

### Test 8 -- LTCI computation
Input: NHIS monthly premium = KRW 350,000.
Expected output: LTCI = KRW 350,000 x 12.95% = KRW 45,325/month. Total health insurance = KRW 395,325/month.

---

## Section 10 -- Prohibitions and disclaimer

### Prohibitions

- NEVER compute NPS without knowing the client's monthly reported income
- NEVER apply the employee NPS rate (4.5%) to a self-employed person -- self-employed pay the full 9%
- NEVER compute NHIS for a self-employed person using only the 7.09% rate -- the community insured calculation requires income, property, and vehicle data
- NEVER tell a client that employment insurance or industrial accident insurance is mandatory for self-employed -- it is voluntary (with limited exceptions)
- NEVER ignore the NPS ceiling change that occurs every July
- NEVER conflate NPS income deduction with NHIS/LTCI tax credit -- they are different mechanisms
- NEVER assume NPS contribution exemption is automatic -- it must be applied for
- NEVER advise on bilateral social security agreements without reviewer confirmation
- NEVER present social insurance figures as definitive -- always label as estimated and direct client to NPS/NHIS notices
- NEVER compute arrears or penalties without escalating to a licensed practitioner

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
