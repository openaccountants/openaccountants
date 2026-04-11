---
name: jp-social-insurance
description: Use this skill whenever asked about Japanese National Health Insurance (NHI / 国民健康保険) or National Pension (国民年金) for self-employed individuals. Trigger on phrases like "NHI", "kokumin kenko hoken", "kokumin nenkin", "national pension Japan", "health insurance freelancer Japan", "social insurance self-employed Japan", or any question about NHI premiums, pension contributions, or social insurance obligations for sole proprietors in Japan. Covers NHI income-based calculation, National Pension fixed monthly amount, payment schedules, and reduction/exemption rules. ALWAYS read this skill before touching any Japanese social insurance work.
---

# Japan NHI + National Pension -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Japan |
| Jurisdiction Code | JP |
| Primary Legislation | National Health Insurance Act (国民健康保険法); National Pension Act (国民年金法) |
| Supporting Legislation | Long-Term Care Insurance Act (介護保険法); Local Tax Act (地方税法) |
| Tax Authority | Municipal governments (NHI); Japan Pension Service / 日本年金機構 (Pension) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Japanese tax accountant (税理士) or social insurance labour consultant (社会保険労務士) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | 2025 |
| Confidence Coverage | Tier 1: National Pension fixed amount, NHI component structure, payment schedules. Tier 2: NHI municipal rate variations, reduction eligibility, partial-year calculations. Tier 3: disability pension, survivors pension, voluntary additional pension. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any social insurance figure, you MUST know:

1. **Residency status** [T1] -- resident (住民票 registered) in Japan; non-residents are not covered
2. **Age** [T1] -- determines pension category (Category 1 insured: age 20-59) and long-term care (age 40-64)
3. **Municipality of residence** [T2] -- NHI rates vary by municipality
4. **Prior-year income** [T1] -- NHI premiums are based on prior calendar year income (所得)
5. **Number of NHI-enrolled household members** [T1] -- per-capita component applies per person
6. **Whether enrolled in any employer health insurance** [T1] -- employees on shakai hoken are excluded from NHI
7. **Whether any pension exemption or deferral has been granted** [T2] -- exemptions reduce or eliminate pension obligation

**If the client is enrolled in employer-based health insurance (健康保険), STOP. This skill covers only NHI (国民健康保険) for self-employed.**

---

## Step 1: National Pension (国民年金) [T1]

**Legislation:** National Pension Act, Art. 87

### Category 1 Insured Persons

Self-employed individuals, freelancers, students, and unemployed persons aged 20-59 are Category 1 insured (第1号被保険者).

### Monthly Contribution [T1]

| Item | Amount (FY 2025) | Source |
|------|-----------------|--------|
| Monthly pension premium | JPY 17,510 | National Pension Act; Japan Pension Service announcement FY 2025 |
| Annual total | JPY 210,120 | 17,510 x 12 |

**Note:** The user-provided figure of JPY 16,980 corresponds to FY 2024. For FY 2025 (April 2025 -- March 2026), the amount is JPY 17,510. Verify with Japan Pension Service (nenkin.go.jp) for the exact current figure.

### Payment Methods [T1]

| Method | Detail |
|--------|--------|
| Monthly | By end of following month |
| 6-month advance | ~1% discount |
| 1-year advance | ~2% discount |
| 2-year advance | ~4% discount |
|口座振替 (bank transfer) | Slight additional discount for early debit |

### Tax Deductibility [T1]

National Pension premiums are fully deductible as social insurance premium deduction (社会保険料控除) on the income tax return. No cap.

---

## Step 2: NHI Premium Structure [T1/T2]

**Legislation:** National Health Insurance Act, Art. 76

NHI premiums consist of three components, each with up to three sub-elements:

### Component Breakdown [T1]

| Component | Purpose | Age Requirement |
|-----------|---------|----------------|
| Medical (医療分) | Basic health insurance | All NHI enrollees |
| Support (後期高齢者支援金分) | Support for elderly health system | All NHI enrollees |
| Long-term care (介護分) | Long-term care insurance | Ages 40-64 only |

### Sub-Elements per Component [T2 -- rates vary by municipality]

| Sub-Element | Basis | Typical Range |
|-------------|-------|---------------|
| Income-based (所得割) | Prior-year income minus JPY 430,000 base deduction | 5-12% (varies by municipality) |
| Per-capita (均等割) | Fixed amount per enrolled person | JPY 20,000-60,000/year per person |
| Per-household (平等割) | Fixed amount per household | JPY 0-30,000/year (some municipalities omit) |
| Asset-based (資産割) | Based on fixed-asset tax | Being phased out; many municipalities have eliminated |

### Annual Caps (FY 2025) [T1]

| Component | Annual Cap |
|-----------|-----------|
| Medical (医療分) | JPY 650,000 |
| Support (後期高齢者支援金分) | JPY 240,000 |
| Long-term care (介護分) | JPY 170,000 |
| **Total maximum** | **JPY 1,060,000** |

---

## Step 3: NHI Computation Steps [T2]

**Because rates vary by municipality, the following is a template. Actual rates must be obtained from the client's municipal office.**

| Step | Action |
|------|--------|
| 3.1 | Obtain prior calendar year total income (総所得金額) |
| 3.2 | Subtract base deduction: JPY 430,000 (2025) to get NHI taxable income |
| 3.3 | For each component (Medical, Support, Long-term care): multiply NHI taxable income by the municipal income-based rate |
| 3.4 | Add per-capita amount x number of NHI-enrolled household members |
| 3.5 | Add per-household flat amount (if municipality charges it) |
| 3.6 | Cap each component at the statutory maximum |
| 3.7 | Sum all three components = annual NHI premium |
| 3.8 | Divide by number of payment instalments (typically 10) |

### Example -- Tokyo 23 Wards (Illustrative, T2) [T2]

| Component | Income Rate | Per-Capita | Per-Household |
|-----------|-----------|-----------|---------------|
| Medical | ~7.17% | ~JPY 42,100 | JPY 0 |
| Support | ~2.42% | ~JPY 14,400 | JPY 0 |
| Long-term care | ~2.14% | ~JPY 15,600 | JPY 0 |

**These rates are illustrative. Always verify with the specific ward/municipality.**

---

## Step 4: NHI Reduction for Low Income [T1]

**Legislation:** National Health Insurance Act, Art. 77; Local Tax Act, Art. 703-5

Households with income below certain thresholds receive automatic reductions on the per-capita and per-household portions:

| Reduction | Household Income Threshold (2025) |
|-----------|----------------------------------|
| 70% reduction (7割軽減) | JPY 430,000 + (JPY 100,000 x number of earners beyond 1) |
| 50% reduction (5割軽減) | JPY 430,000 + JPY 295,000 x number of insured + (JPY 100,000 x earners beyond 1) |
| 20% reduction (2割軽減) | JPY 430,000 + JPY 545,000 x number of insured + (JPY 100,000 x earners beyond 1) |

**The reduction applies only to the per-capita (均等割) and per-household (平等割) portions, NOT to the income-based portion.**

---

## Step 5: National Pension Exemptions and Deferrals [T1/T2]

**Legislation:** National Pension Act, Art. 90

| Exemption Type | Income Threshold (single person, approximate) | Payment |
|---------------|----------------------------------------------|---------|
| Full exemption (全額免除) | Prior-year income <= JPY 670,000 | JPY 0 |
| 3/4 exemption | Income <= ~JPY 930,000 | 1/4 of standard |
| 1/2 exemption | Income <= ~JPY 1,410,000 | 1/2 of standard |
| 1/4 exemption | Income <= ~JPY 1,890,000 | 3/4 of standard |
| Payment deferral (納付猶予) | Under age 50, income <= JPY 670,000 | Deferred |

[T2] Exemption/deferral reduces future pension benefits. Flag for reviewer if client qualifies -- advise on benefit impact.

---

## Step 6: Payment Schedule [T1]

### NHI [T1]

| Detail | Value |
|--------|-------|
| Payment period | Typically June to March (10 instalments) |
| Due date | End of each month (varies by municipality) |
| Methods | Bank transfer, convenience store, credit card, bank debit |

### National Pension [T1]

| Detail | Value |
|--------|-------|
| Payment period | Monthly, April to March |
| Due date | End of the following month |
| Methods | Bank transfer, convenience store, credit card, Pay-easy, bank debit |

---

## Step 7: Edge Case Registry

### EC1 -- Mid-year arrival in Japan [T2]
**Situation:** Client registers as resident in September. How are NHI and pension computed?
**Resolution:** NHI is prorated from the month of registration. Pension is owed from the month of gaining Category 1 status. Prior-year income may be zero (no Japan income), resulting in low NHI and possible pension exemption eligibility. [T2] Flag for reviewer.

### EC2 -- Dual income: self-employment + part-time employment [T1]
**Situation:** Client works part-time (under shakai hoken threshold) and freelances.
**Resolution:** If part-time job does not provide shakai hoken, client remains on NHI. Both employment and self-employment income are included in NHI calculation. Pension remains Category 1.

### EC3 -- Client turns 40 during year [T1]
**Situation:** Client turns 40 in October. Long-term care component starts when?
**Resolution:** Long-term care (介護分) starts from the month the client turns 40. NHI premium is recalculated mid-year.

### EC4 -- Client turns 60 during year [T1]
**Situation:** Client turns 60 in March. National Pension obligation ends when?
**Resolution:** Category 1 insured obligation ends the month before turning 60. Client may optionally continue as voluntary insured (任意加入) to increase pension benefits [T3 -- escalate for advice].

### EC5 -- Client has high income but few assets [T1]
**Situation:** Freelancer earns JPY 10,000,000. NHI premium calculation.
**Resolution:** Income-based portion will be high, but each component is capped. Total NHI cannot exceed JPY 1,060,000 (FY 2025 caps). Verify cap amounts for current year.

### EC6 -- Non-payment consequences [T1]
**Situation:** Client has not paid NHI for 12 months.
**Resolution:** Municipality may issue a short-validity insurance card (短期被保険者証) or a qualification certificate (資格証明書) requiring 100% upfront payment. Pension non-payment results in reduced future benefits and may affect disability pension eligibility.

---

## Step 8: Test Suite

### Test 1 -- Standard freelancer, mid-range income (Tokyo 23 Wards illustrative rates)
**Input:** Age 35, single, prior-year income JPY 5,000,000, no other household NHI members.
**Expected output:**
- NHI taxable income = 5,000,000 - 430,000 = JPY 4,570,000
- Medical: 4,570,000 x 7.17% + 42,100 = 327,669 + 42,100 = JPY 369,769
- Support: 4,570,000 x 2.42% + 14,400 = 110,594 + 14,400 = JPY 124,994
- Long-term care: N/A (under 40)
- Total NHI: ~JPY 494,763
- National Pension: 17,510 x 12 = JPY 210,120
- Total social insurance: ~JPY 704,883

### Test 2 -- Low-income freelancer qualifying for 70% reduction
**Input:** Age 28, single, prior-year income JPY 300,000.
**Expected output:**
- NHI taxable income = max(300,000 - 430,000, 0) = JPY 0
- Income-based portions = JPY 0
- Household income (300,000) <= 430,000 threshold: qualifies for 70% reduction on per-capita
- Medical per-capita: 42,100 x 30% = JPY 12,630
- Support per-capita: 14,400 x 30% = JPY 4,320
- Total NHI: ~JPY 16,950
- National Pension: full exemption likely (income below JPY 670,000 threshold)

### Test 3 -- High earner hitting caps
**Input:** Age 45, single, prior-year income JPY 20,000,000.
**Expected output:**
- Medical: capped at JPY 650,000
- Support: capped at JPY 240,000
- Long-term care (age 45): capped at JPY 170,000
- Total NHI: JPY 1,060,000
- National Pension: JPY 210,120
- Total: JPY 1,270,120

### Test 4 -- Mid-year registration
**Input:** Age 30, registers residency in July (9 months of coverage).
**Expected output:**
- NHI: annual premium prorated x 9/12
- National Pension: 17,510 x 9 = JPY 157,590

---

## PROHIBITIONS

- NEVER assume NHI rates are uniform across Japan -- they vary by municipality and MUST be verified
- NEVER omit the long-term care component for clients aged 40-64
- NEVER include clients enrolled in employer shakai hoken in NHI calculations
- NEVER treat National Pension as optional for Category 1 insured persons aged 20-59 -- it is legally mandatory
- NEVER forget that NHI premiums are based on PRIOR-year income, not current-year income
- NEVER apply the low-income reduction to the income-based portion -- it applies only to per-capita and per-household portions
- NEVER present calculations as definitive -- always label as estimated and direct client to their municipal office or a qualified 税理士/社会保険労務士

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a 税理士, 社会保険労務士, or equivalent licensed practitioner in Japan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
