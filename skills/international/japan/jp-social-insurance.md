---
name: jp-social-insurance
description: >
  Use this skill whenever asked about Japanese National Health Insurance (NHI) or National Pension for self-employed individuals. Trigger on phrases like "NHI", "kokumin kenko hoken", "kokumin nenkin", "national pension Japan", "health insurance freelancer Japan", "social insurance self-employed Japan", or any question about NHI premiums, pension contributions, or social insurance obligations for sole proprietors in Japan. Covers NHI income-based calculation, National Pension fixed monthly amount, payment schedules, and reduction/exemption rules. ALWAYS read this skill before touching any Japanese social insurance work.
version: 2.0
jurisdiction: JP
tax_year: 2025
category: international
---

# Japan NHI + National Pension -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

Read this whole section before computing anything.

| Field | Value |
|---|---|
| Country | Japan |
| Jurisdiction Code | JP |
| Primary Legislation | National Health Insurance Act; National Pension Act |
| Supporting Legislation | Long-Term Care Insurance Act; Local Tax Act |
| Tax Authority | Municipal governments (NHI); Japan Pension Service (National Pension) |
| Tax Year | FY 2025 (April 2025 -- March 2026) |
| Currency | JPY only |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Japanese tax accountant or social insurance labour consultant |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: National Pension fixed amount, NHI component structure, payment schedules, caps. Tier 2: NHI municipal rate variations, reduction eligibility, partial-year calculations. Tier 3: disability pension, survivors pension, voluntary additional pension. |

**National Pension (FY 2025):**

| Item | Amount |
|---|---|
| Monthly premium | JPY 17,510 |
| Annual total | JPY 210,120 |
| Category 1 insured | Self-employed, freelancers, students, unemployed aged 20-59 |
| Tax treatment | Fully deductible as social insurance premium deduction |

**NHI component structure:**

| Component | Purpose | Applies To |
|---|---|---|
| Medical | Basic health insurance | All NHI enrollees |
| Support | Elderly health system support | All NHI enrollees |
| Long-term care | Long-term care insurance | Ages 40-64 only |

**NHI annual caps (FY 2025):**

| Component | Annual Cap |
|---|---|
| Medical | JPY 650,000 |
| Support | JPY 240,000 |
| Long-term care | JPY 170,000 |
| Total maximum | JPY 1,060,000 |

**NHI sub-elements per component:**

| Sub-Element | Basis | Typical Range |
|---|---|---|
| Income-based | Prior-year income minus JPY 430,000 base deduction | 5-12% (varies by municipality) |
| Per-capita | Fixed amount per enrolled person | JPY 20,000-60,000/year |
| Per-household | Fixed amount per household | JPY 0-30,000/year (some omit) |
| Asset-based | Fixed-asset tax | Being phased out |

**Low-income reductions (NHI per-capita/per-household only):**

| Reduction | Household Income Threshold (2025) |
|---|---|
| 70% reduction | JPY 430,000 + (JPY 100,000 x earners beyond 1) |
| 50% reduction | JPY 430,000 + JPY 295,000 x insured + (JPY 100,000 x earners beyond 1) |
| 20% reduction | JPY 430,000 + JPY 545,000 x insured + (JPY 100,000 x earners beyond 1) |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown municipality | Flag for reviewer -- cannot compute NHI without municipal rates |
| Unknown prior-year income | Use JPY 0 (minimum NHI, possible pension exemption) |
| Unknown age | Assume under 40 (no long-term care component) |
| Unknown shakai hoken status | Assume NOT enrolled (NHI applies) |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing any social insurance figure, you MUST know:

1. Residency status -- resident in Japan (non-residents not covered)
2. Age -- determines pension category (20-59) and long-term care (40-64)
3. Municipality of residence -- NHI rates vary by municipality
4. Prior-year income -- NHI premiums based on prior calendar year
5. Number of NHI-enrolled household members -- per-capita component per person
6. Whether enrolled in any employer health insurance -- employees on shakai hoken excluded from NHI
7. Whether any pension exemption or deferral has been granted

If the client is enrolled in employer-based health insurance, STOP. This skill covers NHI only.

### Refusal catalogue

**R-JP-SI-1 -- Disability pension.** Trigger: client asks about disability pension eligibility or computation. Message: "Disability pension eligibility and computation under the National Pension Act require case-specific assessment. Please escalate to a social insurance labour consultant."

**R-JP-SI-2 -- Survivors pension.** Trigger: client asks about survivors pension. Message: "Survivors pension claims are outside this skill's scope. Please escalate to a social insurance labour consultant."

**R-JP-SI-3 -- Voluntary additional pension (Kokumin Nenkin Kikin).** Trigger: client asks about additional pension schemes. Message: "Voluntary additional pension schemes require separate analysis. Please escalate to a qualified professional."

---

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement entries related to social insurance. Match by case-insensitive substring.

### 3.1 National Pension debits

| Pattern | Treatment | Notes |
|---|---|---|
| NENKIN, PENSION, 年金, 国民年金 | NATIONAL PENSION PAYMENT | Monthly premium -- due by end of following month |
| JAPAN PENSION SERVICE, 日本年金機構 | NATIONAL PENSION PAYMENT | Same |
| 年金前納, ADVANCE PENSION | ADVANCE PENSION PAYMENT | 6-month, 1-year, or 2-year advance payment (discounted) |

### 3.2 NHI premium debits

| Pattern | Treatment | Notes |
|---|---|---|
| NHI, 国民健康保険, 国保, KOKUMIN KENKO | NHI PREMIUM PAYMENT | Municipal billing -- typically June to March (10 instalments) |
| 市区町村, CITY OFFICE, WARD OFFICE | POSSIBLE NHI PAYMENT | Verify -- municipalities bill NHI directly |
| 口座振替 (bank debit) + municipal name | NHI AUTO-DEBIT | Auto-debit for NHI premium |

### 3.3 Long-term care (embedded in NHI for ages 40-64)

| Pattern | Treatment | Notes |
|---|---|---|
| 介護保険, LONG-TERM CARE | LTCI COMPONENT | Included in NHI billing for ages 40-64; separate billing for 65+ |

### 3.4 Employer health insurance (exclusion trigger)

| Pattern | Treatment | Notes |
|---|---|---|
| 健康保険, KENPO, 協会けんぽ | EMPLOYER HEALTH INSURANCE | Client is on shakai hoken -- STOP, NHI skill does not apply |
| 厚生年金, KOSEI NENKIN | EMPLOYEES PENSION | Client is on shakai hoken -- STOP |

---

## Section 4 -- National Pension rules

### 4.1 Category 1 insured (Tier 1)

Legislation: National Pension Act, Art. 87

Self-employed individuals, freelancers, students, and unemployed aged 20-59 are Category 1 insured. Monthly premium for FY 2025: JPY 17,510. Annual total: JPY 210,120.

### 4.2 Payment methods and discounts (Tier 1)

| Method | Discount |
|---|---|
| Monthly | None |
| 6-month advance | ~1% |
| 1-year advance | ~2% |
| 2-year advance | ~4% |
| Bank transfer (early debit) | Slight additional discount |

### 4.3 Tax deductibility (Tier 1)

National Pension premiums are fully deductible as social insurance premium deduction on the income tax return. No cap.

### 4.4 Exemptions and deferrals (Tier 1 / Tier 2)

Legislation: National Pension Act, Art. 90

| Exemption Type | Income Threshold (single, approx) | Payment |
|---|---|---|
| Full exemption | Prior-year income <= JPY 670,000 | JPY 0 |
| 3/4 exemption | Income <= ~JPY 930,000 | 1/4 of standard |
| 1/2 exemption | Income <= ~JPY 1,410,000 | 1/2 of standard |
| 1/4 exemption | Income <= ~JPY 1,890,000 | 3/4 of standard |
| Payment deferral (under 50) | Income <= JPY 670,000 | Deferred |

Exemption/deferral reduces future pension benefits. Flag for reviewer if client qualifies.

---

## Section 5 -- NHI computation

### 5.1 NHI computation template (Tier 2)

Because rates vary by municipality, this is a template. Actual rates must be obtained from the client's municipal office.

| Step | Action |
|---|---|
| 5.1 | Obtain prior calendar year total income |
| 5.2 | Subtract base deduction: JPY 430,000 to get NHI taxable income |
| 5.3 | For each component (Medical, Support, Long-term care): multiply by municipal income-based rate |
| 5.4 | Add per-capita amount x number of NHI-enrolled household members |
| 5.5 | Add per-household flat amount (if municipality charges it) |
| 5.6 | Cap each component at statutory maximum |
| 5.7 | Sum all three components = annual NHI premium |
| 5.8 | Divide by number of instalments (typically 10) |

### 5.2 Illustrative rates -- Tokyo 23 Wards (Tier 2)

| Component | Income Rate | Per-Capita | Per-Household |
|---|---|---|---|
| Medical | ~7.17% | ~JPY 42,100 | JPY 0 |
| Support | ~2.42% | ~JPY 14,400 | JPY 0 |
| Long-term care | ~2.14% | ~JPY 15,600 | JPY 0 |

These rates are illustrative. Always verify with the specific municipality.

### 5.3 Low-income reduction (Tier 1)

Reductions apply only to per-capita and per-household portions, NOT to income-based portion. The 70%/50%/20% reductions are applied automatically based on household income reported to the municipality.

---

## Section 6 -- Payment schedules

### 6.1 NHI (Tier 1)

| Detail | Value |
|---|---|
| Payment period | Typically June to March (10 instalments) |
| Due date | End of each month (varies by municipality) |
| Methods | Bank transfer, convenience store, credit card, bank debit |

### 6.2 National Pension (Tier 1)

| Detail | Value |
|---|---|
| Payment period | Monthly, April to March |
| Due date | End of the following month |
| Methods | Bank transfer, convenience store, credit card, Pay-easy, bank debit |

---

## Section 7 -- Edge case registry

### EC1 -- Mid-year arrival in Japan (Tier 2)
Situation: Client registers as resident in September.
Resolution: NHI prorated from month of registration. Pension owed from month of gaining Category 1 status. Prior-year income may be zero, resulting in low NHI and possible pension exemption. Flag for reviewer.

### EC2 -- Dual income: self-employment + part-time employment (Tier 1)
Situation: Client works part-time (under shakai hoken threshold) and freelances.
Resolution: If part-time does not provide shakai hoken, client remains on NHI. Both employment and self-employment income included in NHI calculation. Pension remains Category 1.

### EC3 -- Client turns 40 during year (Tier 1)
Situation: Client turns 40 in October.
Resolution: Long-term care component starts from the month the client turns 40. NHI premium recalculated mid-year.

### EC4 -- Client turns 60 during year (Tier 1)
Situation: Client turns 60 in March.
Resolution: Category 1 obligation ends the month before turning 60. May optionally continue as voluntary insured. Escalate for advice on voluntary continuation.

### EC5 -- Client has high income but few assets (Tier 1)
Situation: Freelancer earns JPY 10,000,000.
Resolution: Income-based portion will be high, but each component is capped. Total NHI cannot exceed JPY 1,060,000.

### EC6 -- Non-payment consequences (Tier 1)
Situation: Client has not paid NHI for 12 months.
Resolution: Municipality may issue short-validity insurance card or qualification certificate requiring 100% upfront payment. Pension non-payment reduces future benefits and may affect disability pension eligibility.

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
Action Required: Qualified professional must confirm before advising client.
```

When a Tier 3 situation is identified:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified professional. Document gap.
```

---

## Section 9 -- Test suite

### Test 1 -- Standard freelancer, mid-range income (Tokyo 23 Wards illustrative)
Input: Age 35, single, prior-year income JPY 5,000,000, no other household NHI members.
Expected output: NHI taxable income = 5,000,000 - 430,000 = JPY 4,570,000. Medical: ~JPY 369,769. Support: ~JPY 124,994. Long-term care: N/A (under 40). Total NHI: ~JPY 494,763. Pension: JPY 210,120. Total: ~JPY 704,883.

### Test 2 -- Low-income freelancer qualifying for 70% reduction
Input: Age 28, single, prior-year income JPY 300,000.
Expected output: NHI taxable income = JPY 0. Income-based = JPY 0. 70% reduction on per-capita. Medical per-capita: JPY 12,630. Support: JPY 4,320. Total NHI: ~JPY 16,950. Pension: full exemption likely.

### Test 3 -- High earner hitting caps
Input: Age 45, single, prior-year income JPY 20,000,000.
Expected output: Medical capped at JPY 650,000. Support capped at JPY 240,000. Long-term care capped at JPY 170,000. Total NHI: JPY 1,060,000. Pension: JPY 210,120. Total: JPY 1,270,120.

### Test 4 -- Mid-year registration
Input: Age 30, registers residency in July (9 months).
Expected output: NHI prorated x 9/12. Pension: JPY 17,510 x 9 = JPY 157,590.

---

## Section 10 -- Prohibitions and disclaimer

### Prohibitions

- NEVER assume NHI rates are uniform across Japan -- they vary by municipality and MUST be verified
- NEVER omit the long-term care component for clients aged 40-64
- NEVER include clients enrolled in employer shakai hoken in NHI calculations
- NEVER treat National Pension as optional for Category 1 insured persons aged 20-59 -- it is legally mandatory
- NEVER forget that NHI premiums are based on PRIOR-year income, not current-year income
- NEVER apply the low-income reduction to the income-based portion -- it applies only to per-capita and per-household portions
- NEVER present calculations as definitive -- always label as estimated and direct client to their municipal office or a qualified professional

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a tax accountant, social insurance labour consultant, or equivalent licensed practitioner in Japan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
