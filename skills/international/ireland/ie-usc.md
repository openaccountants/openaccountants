---
name: ie-usc
description: Use this skill whenever asked about Ireland's Universal Social Charge (USC) for self-employed individuals or any taxpayer. Trigger on phrases like "USC calculation", "universal social charge", "USC rates Ireland", "USC bands", "USC surcharge", "USC self-employed", "USC medical card", "USC exemption", or any question about USC obligations. This skill covers standard rates and bands, the self-employed surcharge, exemptions, reduced rates for medical card holders and over-70s, and edge cases. ALWAYS read this skill before touching any Irish USC work.
---

# Ireland Universal Social Charge (USC) -- Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Ireland |
| Jurisdiction Code | IE |
| Primary Legislation | Finance Act 2011 (as amended annually); Taxes Consolidation Act 1997, Part 18D |
| Supporting Legislation | Finance Act 2024; Finance Act 2025 (Budget 2026 changes) |
| Tax Authority | Revenue Commissioners |
| Rate Publisher | Revenue Commissioners / Department of Finance |
| Contributor | Open Accountants |
| Validated By | Pending -- licensed Irish practitioner sign-off required |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: standard bands and rates, exemption threshold, surcharge. Tier 2: medical card reduced rates, interaction with DIRT, dual income sources. Tier 3: cross-border USC treatment, Department of Social Protection income. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any USC figure, you MUST know:

1. **Tax year** [T1] -- bands change annually
2. **Total income** [T1] -- USC is charged on gross income before pension contributions or other reliefs
3. **Is total income above or below the exemption threshold?** [T1] -- EUR 13,000 for 2025/2026
4. **Does the client hold a full medical card?** [T2] -- reduced rates may apply
5. **Is the client aged 70 or over?** [T2] -- reduced rates may apply
6. **Does the client have non-PAYE income exceeding EUR 100,000?** [T1] -- 3% surcharge applies
7. **Is there any Department of Social Protection (DSP) income?** [T1] -- exempt from USC

**If tax year is unknown, STOP. Do not compute USC. Bands shift annually.**

---

## Step 1: Exemption Test [T1]

**Legislation:** Taxes Consolidation Act 1997, s 531AN

| Total Income | USC Liability |
|-------------|--------------|
| <= EUR 13,000 (2025/2026) | Fully exempt -- no USC payable |
| > EUR 13,000 | USC on ENTIRE income (not just the excess) |

**The exemption is an all-or-nothing threshold. If income is EUR 13,001, USC applies to the full EUR 13,001.**

**DSP payments (e.g., Jobseeker's Benefit, State Pension) are exempt from USC but are included in the income total for the exemption test.**

---

## Step 2: Standard USC Bands and Rates [T1]

**Legislation:** Taxes Consolidation Act 1997, s 531AN; Finance Act 2025

### 2025 Bands

| Band | Income Range | Rate |
|------|-------------|------|
| 1 | First EUR 12,012 | 0.5% |
| 2 | EUR 12,012.01 to EUR 27,382 | 2.0% |
| 3 | EUR 27,382.01 to EUR 70,044 | 3.0% |
| 4 | Above EUR 70,044 | 8.0% |

### 2026 Bands

| Band | Income Range | Rate |
|------|-------------|------|
| 1 | First EUR 12,012 | 0.5% |
| 2 | EUR 12,012.01 to EUR 28,700 | 2.0% |
| 3 | EUR 28,700.01 to EUR 70,044 | 3.0% |
| 4 | Above EUR 70,044 | 8.0% |

**The only change from 2025 to 2026 is the Band 2 ceiling rising from EUR 27,382 to EUR 28,700.**

---

## Step 3: Self-Employed Surcharge [T1]

**Legislation:** Taxes Consolidation Act 1997, s 531AN(3)

| Condition | Surcharge |
|-----------|-----------|
| Non-PAYE income > EUR 100,000 | Additional 3% on non-PAYE income above EUR 100,000 |
| Non-PAYE income <= EUR 100,000 | No surcharge |

**Effective USC rate on non-PAYE income above EUR 100,000 = 8% + 3% = 11%.**

**"Non-PAYE income" includes self-employment income, rental income, investment income, and any income not subject to PAYE.**

### Formula (2026)

```
USC = (EUR 12,012 x 0.5%)
    + ((EUR 28,700 - EUR 12,012) x 2.0%)
    + ((EUR 70,044 - EUR 28,700) x 3.0%)
    + ((min(total_income, EUR 100,000) - EUR 70,044) x 8.0%)     [if income > 70,044]
    + ((total_income - EUR 100,000) x 11.0%)                      [if non-PAYE income > 100,000]
```

### Calculation Example (2026) -- Self-employed, EUR 150,000 income

| Band | Income Slice | Rate | USC |
|------|-------------|------|-----|
| 1 | EUR 12,012 | 0.5% | EUR 60.06 |
| 2 | EUR 16,688 (28,700 - 12,012) | 2.0% | EUR 333.76 |
| 3 | EUR 41,344 (70,044 - 28,700) | 3.0% | EUR 1,240.32 |
| 4 | EUR 29,956 (100,000 - 70,044) | 8.0% | EUR 2,396.48 |
| Surcharge | EUR 50,000 (150,000 - 100,000) | 11.0% | EUR 5,500.00 |
| **Total** | | | **EUR 9,530.62** |

---

## Step 4: Reduced Rates [T2]

**Legislation:** Taxes Consolidation Act 1997, s 531AN; Finance Act 2025

### Medical Card Holders / Aged 70+

| Condition | Reduced Rate Cap | Income Limit |
|-----------|-----------------|-------------|
| Full medical card holder AND aggregate income <= EUR 60,000 | Max 2.0% on all income | EUR 60,000 |
| Aged 70+ AND aggregate income <= EUR 60,000 | Max 2.0% on all income | EUR 60,000 |
| Either condition AND income > EUR 60,000 | Standard rates apply on income above EUR 60,000 | N/A |

**Reduced rate bands (2025/2026):**

| Band | Income Range | Rate |
|------|-------------|------|
| 1 | First EUR 12,012 | 0.5% |
| 2 | Above EUR 12,012 (up to EUR 60,000) | 2.0% |

**This relief is extended through 31 December 2027.**

**[T2] flag for reviewer if medical card status is uncertain or if income is near the EUR 60,000 boundary.**

---

## Step 5: USC and Income Tax Interaction [T1]

| Question | Answer |
|----------|--------|
| Is USC deductible for income tax? | NO |
| Is USC part of PRSI? | NO -- they are entirely separate charges |
| Is USC applied before or after tax credits? | USC is applied to gross income; income tax credits do not reduce USC |
| Does USC apply to DSP payments? | NO -- DSP payments are exempt from USC |
| Does USC apply to DIRT income? | NO -- deposit interest subject to DIRT is exempt from USC (already taxed at source) |

---

## Step 6: Payment Schedule [T1]

| Payment Method | Detail |
|---------------|--------|
| PAYE employees | Deducted at source by employer through payroll |
| Self-assessed (self-employed) | Included in preliminary tax (31 Oct / mid-Nov ROS) and balance on Form 11 |

---

## Step 7: Edge Case Registry

### EC1 -- Income exactly EUR 13,000 [T1]
**Situation:** Client's total income is exactly EUR 13,000.
**Resolution:** Exempt from USC. The threshold is "not exceeding EUR 13,000", so EUR 13,000 exactly is exempt.

### EC2 -- Income EUR 13,001 [T1]
**Situation:** Client's total income is EUR 13,001.
**Resolution:** USC applies to the FULL EUR 13,001. Band 1: EUR 12,012 x 0.5% = EUR 60.06. Band 2: EUR 989 x 2.0% = EUR 19.78. Total = EUR 79.84.

### EC3 -- Medical card holder with income EUR 61,000 [T2]
**Situation:** Client holds a full medical card but income is EUR 61,000.
**Resolution:** Income exceeds EUR 60,000 limit. Standard USC rates apply, not reduced rates. [T2] flag for reviewer to confirm medical card status and income figure.

### EC4 -- Mixed PAYE and non-PAYE income, surcharge test [T1]
**Situation:** Client earns EUR 80,000 PAYE and EUR 40,000 self-employment. Total = EUR 120,000.
**Resolution:** Non-PAYE income is EUR 40,000, which is below EUR 100,000. No surcharge applies. Standard rates on full EUR 120,000.

### EC5 -- Non-PAYE income exactly EUR 100,000 [T1]
**Situation:** Client has EUR 100,000 non-PAYE self-employment income and no PAYE income.
**Resolution:** No surcharge. Surcharge applies only to non-PAYE income EXCEEDING EUR 100,000. Standard 8% rate applies up to EUR 100,000.

### EC6 -- DSP income included in exemption test [T1]
**Situation:** Client has EUR 10,000 self-employment income and EUR 4,000 Jobseeker's Benefit.
**Resolution:** Total income for exemption test = EUR 14,000 (exceeds EUR 13,000). USC applies. But USC is charged only on the EUR 10,000 non-DSP income. DSP payments are exempt from USC itself.

### EC7 -- Client turning 70 mid-year [T2]
**Situation:** Client turns 70 in June 2026.
**Resolution:** [T2] flag for reviewer. Reduced rate applies for the full year if the client is aged 70 at any point during the year and income <= EUR 60,000. Confirm with Revenue guidance.

### EC8 -- Rental income only, no trade [T1]
**Situation:** Client has EUR 50,000 rental income, no employment.
**Resolution:** Rental income is non-PAYE income. Standard USC bands apply. If rental income were > EUR 100,000, the 3% surcharge would also apply on the excess.

### EC9 -- DIRT-subject deposit interest [T1]
**Situation:** Client has EUR 5,000 deposit interest already subject to DIRT.
**Resolution:** DIRT income is exempt from USC. Exclude from USC calculation. However, include in total income for the exemption threshold test.

---

## Step 8: Reviewer Escalation Protocol

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

## Step 9: Test Suite

### Test 1 -- Standard self-employed, mid-range income (2026)
**Input:** Self-employed, total income EUR 50,000, age 45, no medical card.
**Expected output:** Band 1: EUR 12,012 x 0.5% = EUR 60.06. Band 2: EUR 16,688 x 2.0% = EUR 333.76. Band 3: EUR 21,300 x 3.0% = EUR 639.00. Total USC = EUR 1,032.82.

### Test 2 -- Exempt (below threshold)
**Input:** Total income EUR 12,500, age 35.
**Expected output:** USC = EUR 0. Income below EUR 13,000 exemption threshold.

### Test 3 -- Surcharge applies (2026)
**Input:** Self-employed, non-PAYE income EUR 150,000, age 50.
**Expected output:** Bands 1-4 on first EUR 100,000 = EUR 4,030.62. Surcharge: EUR 50,000 x 11% = EUR 5,500.00. Total = EUR 9,530.62.

### Test 4 -- Medical card holder, reduced rates
**Input:** Full medical card, total income EUR 40,000, age 72.
**Expected output:** Band 1: EUR 12,012 x 0.5% = EUR 60.06. Band 2: EUR 27,988 x 2.0% = EUR 559.76. Total = EUR 619.82.

### Test 5 -- Just above exemption
**Input:** Total income EUR 13,001, age 30.
**Expected output:** Band 1: EUR 12,012 x 0.5% = EUR 60.06. Band 2: EUR 989 x 2.0% = EUR 19.78. Total = EUR 79.84.

### Test 6 -- DSP income in exemption test
**Input:** Self-employment income EUR 10,000, DSP income EUR 4,000, age 40.
**Expected output:** Total for exemption test = EUR 14,000 (exceeds EUR 13,000). USC charged on EUR 10,000 only (DSP exempt). Band 1: EUR 10,000 x 0.5% = EUR 50.00. Total = EUR 50.00.

---

## PROHIBITIONS

- NEVER compute USC without confirming the tax year -- bands change annually
- NEVER apply USC to income at or below the EUR 13,000 exemption threshold
- NEVER forget that the exemption test uses TOTAL income but DSP payments are exempt from the charge itself
- NEVER apply reduced rates without confirming both medical card status AND income <= EUR 60,000
- NEVER omit the 3% surcharge on non-PAYE income exceeding EUR 100,000
- NEVER conflate USC with PRSI or income tax -- they are three separate charges
- NEVER state that USC is deductible for income tax purposes -- it is NOT
- NEVER apply income tax credits against USC -- credits do not reduce USC
- NEVER present USC figures as definitive -- always label as estimated and direct client to Revenue for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CTA, AITI, or equivalent licensed practitioner in Ireland) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
