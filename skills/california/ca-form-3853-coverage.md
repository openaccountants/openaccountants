---
name: ca-form-3853-coverage
description: Tier 2 California content skill for Form 3853 (Health Coverage Exemptions and Individual Shared Responsibility Penalty) for California residents under the state individual mandate enacted by SB 78 (2019) and codified at R&TC section 61000 et seq. Covers tax year 2025 including the penalty computation (greater of flat dollar amount or percentage of income), Minimum Essential Coverage (MEC) requirements using the federal ACA definition, month-by-month coverage analysis, exemption categories (affordability, short gap, religious conscience, hardship, and others), Covered California interaction, and reporting forms (1095-A, 1095-B, 1095-C). Defers income tax computation to ca-540-individual-return and estimated tax to ca-estimated-tax-540es. MUST be loaded alongside us-tax-workflow-base v0.1 or later. California residents only.
version: 0.2
---

# CA Form 3853 Coverage Skill v0.2

## What this file is, and what it is not

**This file is a content skill that loads on top of `us-tax-workflow-base` v0.1.** It provides the California individual mandate rules and Form 3853 preparation for tax year 2025. California reinstated the individual health coverage mandate effective January 1, 2020 under SB 78 (2019), codified in R&TC sections 61000-61130. This skill determines whether the taxpayer had qualifying coverage, whether an exemption applies, and if not, computes the Individual Shared Responsibility Penalty (ISRP).

**This skill does NOT compute the taxpayer's California income tax** (handled by `ca-540-individual-return`). It produces a Form 3853 worksheet and penalty amount that flows to Form 540.

---

## Section 1 -- Scope statement

This skill covers California Form 3853 for tax year 2025 for taxpayers who are:

- Full-year California residents (or part-year residents for months of CA residency)
- All filing statuses

For the following kinds of work:

- Determining whether the taxpayer (and all household members) had Minimum Essential Coverage (MEC) for each month of 2025
- Identifying applicable exemptions from the mandate
- Computing the Individual Shared Responsibility Penalty (ISRP) for months without coverage or exemption
- Preparing Form 3853 (Health Coverage Exemptions and Individual Shared Responsibility Penalty)
- Reconciling 1095-A, 1095-B, and 1095-C forms with actual coverage

This skill does NOT cover:

- Premium Tax Credit / APTC reconciliation (Form 3849 / federal Form 8962)
- Covered California enrollment assistance
- Health insurance plan selection
- Employer mandate (large employer reporting under ACA section 6056)

---

## Section 2 -- Year coverage and currency

**Tax year covered:** 2025.

**Currency date:** April 2026.

**Legislation reflected:**
- SB 78 (2019) -- California individual mandate
- R&TC sections 61000-61130
- Health and Safety Code section 100705 (Covered California)
- 42 USC 18091 (federal ACA MEC definition, incorporated by reference)
- FTB Form 3853 Instructions (2025)
- Covered California / FTB joint guidance on exemptions

---

## Section 3 -- Year-specific figures table for tax year 2025

### Penalty amounts (verify 2025)

| Figure | Value | Source |
|---|---|---|
| Flat dollar: per adult (age 18+) | $950 | R&TC section 61015; indexed for inflation |
| Flat dollar: per child (under 18) | $475 (half of adult amount) | R&TC section 61015 |
| Flat dollar: family cap | $2,850 (3x adult amount) | R&TC section 61015 |
| Percentage of income method | 2.5% of household income above the CA filing threshold | R&TC section 61015 |
| Penalty = GREATER of flat dollar or percentage method | Per R&TC section 61015 | |
| Maximum penalty cap | Cannot exceed the statewide average premium for a bronze-level plan (verify 2025 amount) | R&TC section 61015 |

### Filing thresholds for penalty computation (verify 2025)

| Filing status | Filing threshold (CA) |
|---|---|
| Single, under 65 | $21,135 (verify 2025) |
| Single, 65+ | $27,385 (verify 2025) |
| HOH, under 65 | $34,025 (verify 2025) |
| MFJ, both under 65 | $42,270 (verify 2025) |

### Affordability threshold (verify 2025)

| Figure | Value |
|---|---|
| Coverage is unaffordable if lowest-cost bronze plan exceeds | 8.27% of household income (verify 2025 -- this percentage is indexed) |

---

## Section 4 -- Primary source library

| Source | Use |
|---|---|
| R&TC section 61000 | Definitions |
| R&TC section 61005 | Requirement to maintain MEC |
| R&TC section 61010 | Minimum Essential Coverage definition (references federal ACA) |
| R&TC section 61015 | Penalty computation |
| R&TC section 61020 | Exemptions from the mandate |
| R&TC section 61025 | Hardship exemptions |
| R&TC section 61030 | Religious conscience exemption |
| R&TC section 61100 | Reporting requirements |
| R&TC section 61105 | Penalty assessment and collection |
| 42 USC 18022 | Federal essential health benefits (bronze-level definition) |
| 26 USC 5000A(f) | Federal MEC definition (incorporated by CA reference) |
| FTB Form 3853 Instructions (2025) | Line-by-line preparation |
| FTB Publication 3895B | Health Coverage Exemptions |

---

## Section 5 -- Minimum Essential Coverage (MEC)

### 5.1 -- What qualifies as MEC

California uses the federal ACA definition of Minimum Essential Coverage (26 USC 5000A(f)). Qualifying coverage includes:

| Coverage type | Qualifies as MEC? |
|---|---|
| Employer-sponsored group health plan (including COBRA) | Yes |
| Individual market plan (including Covered California) | Yes |
| Medicare Part A | Yes |
| Medicaid (Medi-Cal in California) | Yes |
| CHIP | Yes |
| TRICARE | Yes |
| VA health care | Yes |
| Peace Corps volunteer coverage | Yes |
| Self-funded student health plan | Yes (if meets MEC standards) |
| Short-term limited duration insurance (STLDI) | No -- does NOT qualify as MEC |
| Health care sharing ministry | No -- does NOT qualify as MEC in California |
| Health savings account (HSA) alone | No -- not coverage |
| Dental/vision only plans | No |

### 5.2 -- Month-by-month analysis

The mandate is assessed on a MONTHLY basis. For each month of 2025, for each household member:

1. Did the individual have MEC for that month? (Coverage for at least one day of the month counts as coverage for the full month.)
2. If no coverage, does an exemption apply for that month?
3. If no coverage and no exemption, a penalty is assessed for that month.

The annual penalty is 1/12 of the annual amount, multiplied by the number of uncovered months (without exemption).

---

## Section 6 -- Exemptions from the mandate

### 6.1 -- Exemption categories

| Exemption | Description | How to claim |
|---|---|---|
| **Affordability** | Lowest-cost bronze plan through Covered California exceeds 8.27% of household income (verify 2025 percentage) | Form 3853 Part III, or apply through Covered California for ECN |
| **Short coverage gap** | Gap of less than 3 consecutive months during the year | Form 3853 Part III -- automatic if gap < 3 months. Only one short gap per year. |
| **Income below filing threshold** | Gross income below CA filing threshold (so no CA return is filed) | No Form 3853 needed if no return is filed |
| **Religious conscience** | Member of a recognized religious sect with objection to insurance | Must obtain Exemption Certificate Number (ECN) from Covered California |
| **Incarceration** | Individual was incarcerated (not pending disposition of charges) | Form 3853 Part III |
| **Not lawfully present** | Individual is not a U.S. citizen or lawfully present | Form 3853 Part III |
| **Hardship** | Various hardship circumstances (homelessness, eviction, domestic violence, etc.) | Form 3853 Part III, or apply through Covered California for ECN |
| **Members of Indian tribes** | Enrolled member or eligible for IHS services | Form 3853 Part III |
| **Certain noncitizens** | Not required to file a tax return because of foreign-earned income exclusion | Form 3853 Part III |
| **Coverage considered unaffordable** | Employer coverage is unaffordable (employee share > 8.27% of income) | Form 3853 Part III |

### 6.2 -- Short coverage gap rules

- A "short coverage gap" is a continuous period of less than 3 months without MEC.
- Only ONE short gap exemption is allowed per calendar year.
- If the gap is 3 months or longer, no short-gap exemption applies, and the penalty is assessed for ALL months in the gap.
- A gap that spans two calendar years: count the months in each year separately.

### 6.3 -- Affordability exemption details

- Compare the annual premium for the lowest-cost bronze-level plan available through Covered California (for the taxpayer's household size and zip code) against 8.27% of household income (verify 2025 percentage).
- If the premium exceeds 8.27%, the taxpayer qualifies for the affordability exemption.
- Household income = MAGI (modified adjusted gross income) for all members of the tax household.
- The taxpayer can either self-certify on Form 3853 or obtain an ECN from Covered California.

---

## Section 7 -- Penalty computation

### 7.1 -- Method A: Flat dollar amount

For each month without coverage and without exemption:

1. Count the number of unexempt individuals in the household.
2. Adults (18+): $950 per person per year (1/12 per month).
3. Children (under 18): $475 per person per year (1/12 per month).
4. Family cap: maximum flat dollar penalty = $2,850 per year (or 1/12 per month).

### 7.2 -- Method B: Percentage of income

1. Household income = CA AGI (or MAGI if different).
2. Filing threshold = CA filing threshold for the taxpayer's filing status.
3. Excess income = Household income - Filing threshold.
4. Percentage penalty = 2.5% x Excess income.
5. Prorate by the number of months without coverage (x months / 12).

### 7.3 -- Final penalty

1. Penalty = GREATER of Method A or Method B.
2. Cap: the penalty cannot exceed the statewide average annual premium for a bronze-level plan available through Covered California for the taxpayer's household size (verify 2025 cap amount).
3. Prorate for partial-year exposure (months without coverage / 12).

### 7.4 -- Reporting on Form 540

- The Form 3853 penalty amount flows to Form 540 Line 92 (verify 2025 line reference).
- The penalty is assessed as additional tax on the CA return.
- The penalty is NOT deductible on any return.

---

## Section 8 -- Reporting forms interaction

### 8.1 -- Form 1095-A (Health Insurance Marketplace Statement)

- Issued by Covered California to individuals who purchased marketplace coverage.
- Shows monthly enrollment, monthly premium, monthly SLCSP (second lowest cost silver plan), and monthly APTC.
- Used to reconcile Premium Tax Credit on federal Form 8962 (not this skill's scope).
- Used on Form 3853 to verify coverage months.

### 8.2 -- Form 1095-B (Health Coverage)

- Issued by health insurers and government programs (Medi-Cal, etc.).
- Shows which individuals were covered and for which months.
- Used on Form 3853 to verify coverage months.

### 8.3 -- Form 1095-C (Employer-Provided Health Insurance Offer and Coverage)

- Issued by Applicable Large Employers (ALEs, 50+ FTEs).
- Shows whether coverage was offered to the employee and dependents.
- Line 14 codes indicate the type of offer; Line 16 codes indicate coverage.
- Used on Form 3853 to verify coverage months.
- Also used for affordability exemption analysis (was affordable coverage offered?).

### 8.4 -- Missing 1095 forms

- If the taxpayer does not receive a 1095-B or 1095-C, they should still report coverage based on their own records.
- Contact the insurer or employer if forms are missing.
- Do NOT delay filing solely because a 1095 form is late (the mandate still applies based on actual coverage status).

---

## Section 9 -- PROHIBITIONS

**P-3853-1.** NEVER assume health care sharing ministries qualify as MEC in California. They do NOT. The federal exemption for health care sharing ministries under 26 USC 5000A(d)(2)(B) was relevant when the federal mandate had a penalty, but California's mandate does not recognize sharing ministries as MEC.

**P-3853-2.** NEVER assume short-term limited duration insurance (STLDI) qualifies as MEC. It does NOT under federal or California definitions.

**P-3853-3.** NEVER allow more than one short coverage gap exemption per calendar year. Only one gap of less than 3 consecutive months is exempt.

**P-3853-4.** NEVER compute the penalty using federal filing thresholds. Use CALIFORNIA filing thresholds for the percentage-of-income method.

**P-3853-5.** NEVER skip Form 3853 when the taxpayer had coverage all year. If coverage was maintained for all 12 months for all household members, Form 3853 is not required (but the taxpayer should still check the full-year coverage box on Form 540).

**P-3853-6.** NEVER advise that the penalty is deductible. The ISRP is a penalty, not a tax or expense, and is not deductible on any federal or state return.

**P-3853-7.** NEVER confuse the California mandate with the federal mandate. The federal individual mandate penalty was reduced to $0 effective 2019 by TCJA. California's mandate is separate and independently enforced with real penalties.

**P-3853-8.** NEVER assume all household members have the same coverage status. Analyze each individual in the tax household separately, month by month.

---

## Section 10 -- Edge Cases

### EC-3853-1 -- Taxpayer with health care sharing ministry only

**Situation:** Taxpayer was a member of a health care sharing ministry for all of 2025. No other coverage.

**Resolution:**
- Health care sharing ministries do NOT qualify as MEC in California.
- Taxpayer is uninsured for all 12 months under the CA mandate.
- No exemption applies (sharing ministry is not an exemption category).
- Compute the full-year penalty using the greater of flat dollar or percentage method.
- **Flag for reviewer:** Taxpayer may qualify for a hardship or affordability exemption if they can demonstrate that marketplace coverage was unaffordable.

### EC-3853-2 -- Short coverage gap of exactly 3 months

**Situation:** Taxpayer had no coverage for January, February, and March 2025 (3 months). Coverage started April 1.

**Resolution:**
- A short coverage gap exemption applies ONLY if the gap is LESS than 3 consecutive months.
- 3 months = NOT less than 3. The short gap exemption does NOT apply.
- Penalty is assessed for all 3 months (January, February, March).
- **Flag for reviewer:** If the gap were only 2 months (e.g., February-March), the short gap exemption would apply.

### EC-3853-3 -- Two separate gaps in the same year

**Situation:** Taxpayer had no coverage in February (1 month gap) and again in September-October (2 month gap).

**Resolution:**
- The short gap exemption can only be used ONCE per year.
- Apply the exemption to the LONGER gap (September-October, 2 months) -- this is more favorable.
- February has no exemption; penalty assessed for 1 month.
- Total penalty months: 1 (February only).
- **Flag for reviewer:** The taxpayer should apply the exemption strategically to minimize penalty.

### EC-3853-4 -- High-income taxpayer with no coverage

**Situation:** Single filer, CA AGI $300,000, no coverage for all 12 months, no exemptions.

**Resolution:**
- Method A (flat dollar): $950 (1 adult, no children).
- Method B (percentage): 2.5% x ($300,000 - $21,135) = 2.5% x $278,865 = $6,972 (verify filing threshold).
- Penalty = greater of $950 or $6,972 = $6,972.
- Cap: cannot exceed the statewide average annual bronze plan premium (verify 2025 cap). If $6,972 is below the cap, the penalty is $6,972.
- **Flag for reviewer:** Verify filing threshold and bronze plan cap for 2025.

### EC-3853-5 -- Family with mixed coverage status

**Situation:** MFJ couple with two children. Spouse 1 had employer coverage all year. Spouse 2 and children had no coverage for 4 months (May-August) due to job transition.

**Resolution:**
- Spouse 1: covered all year, no penalty.
- Spouse 2 + 2 children: no coverage for 4 months. Not a short gap (4 months > 3).
- Monthly flat dollar for uninsured: $950/12 (Spouse 2) + $475/12 (child 1) + $475/12 (child 2) = $158.33/month.
- 4 months: $158.33 x 4 = $633.33.
- Also compute percentage method on household income for 4/12 of the year.
- Penalty = greater of the two methods, prorated.
- **Flag for reviewer:** Check if COBRA was available during the gap (COBRA = MEC if elected).

### EC-3853-6 -- Taxpayer with Medi-Cal for part of the year

**Situation:** Taxpayer had Medi-Cal from January through June 2025, then lost eligibility due to income increase. Enrolled in Covered California plan starting September 2025. No coverage July-August.

**Resolution:**
- January-June: Medi-Cal = MEC. Covered.
- July-August: 2-month gap. Less than 3 months. Short gap exemption applies (if no other gap in the year).
- September-December: Covered California = MEC. Covered.
- No penalty. Form 3853 should document the gap and claim the short gap exemption.

### EC-3853-7 -- ITIN filer subject to mandate

**Situation:** ITIN filer (undocumented immigrant) who files a CA tax return. Had no health coverage.

**Resolution:**
- If the individual is "not lawfully present," they are exempt from the mandate under R&TC section 61020.
- Claim the exemption on Form 3853 Part III.
- No penalty.
- However: if the individual IS lawfully present (e.g., DACA recipient with ITIN), the mandate applies and the penalty would be assessed for uncovered months.
- **Flag for reviewer:** Determine the individual's immigration status carefully. "ITIN filer" does not automatically mean "not lawfully present."

### EC-3853-8 -- Affordability exemption borderline

**Situation:** Single filer, household income $45,000. Lowest-cost bronze plan on Covered California = $3,800/year. Affordability threshold = 8.27%.

**Resolution:**
- 8.27% of $45,000 = $3,721.50.
- $3,800 > $3,721.50. Coverage is UNAFFORDABLE.
- Affordability exemption applies for all 12 months.
- No penalty.
- If income were slightly higher ($46,100), then 8.27% x $46,100 = $3,812.47, and coverage would be affordable ($3,800 < $3,812.47). Penalty would apply.
- **Flag for reviewer:** Verify the exact premium for the taxpayer's zip code, age, and household size.

---

## Section 11 -- Test Suite

### Test 3853-1 -- Full-year coverage, no Form 3853 needed

**Input:** Single filer, employer coverage all 12 months. 1095-B confirms.
**Expected:** Check "full-year coverage" box on Form 540. No Form 3853 required. No penalty.

### Test 3853-2 -- No coverage, single filer, moderate income

**Input:** Single, CA AGI $60,000, no coverage all 12 months, no exemptions. Filing threshold $21,135 (verify).
**Expected:** Method A: $950. Method B: 2.5% x ($60,000 - $21,135) = $971.63. Penalty = greater = $971.63. Cap: verify against bronze plan average. File Form 3853.

### Test 3853-3 -- Short coverage gap (2 months)

**Input:** Single, CA AGI $80,000, no coverage for June-July (2-month gap). Covered all other months.
**Expected:** Short gap exemption applies (less than 3 consecutive months, first gap of the year). No penalty. File Form 3853 claiming short gap exemption.

### Test 3853-4 -- Family, partial year uncovered

**Input:** MFJ, 2 adults, 1 child (age 10). CA AGI $100,000. One adult uncovered for 6 months (July-December). Others covered all year.
**Expected:** Method A (for uncovered months): $950/12 x 6 = $475. Method B: 2.5% x ($100,000 - $42,270) x (6/12) = 2.5% x $57,730 x 0.5 = $721.63. Penalty = greater = $721.63. Verify against cap.

### Test 3853-5 -- Health care sharing ministry (no MEC)

**Input:** Single, CA AGI $75,000, member of health sharing ministry all year. No other coverage.
**Expected:** Sharing ministry does not qualify as MEC. No exemption applies. Method A: $950. Method B: 2.5% x ($75,000 - $21,135) = $1,346.63. Penalty = $1,346.63. Verify against cap. File Form 3853.

### Test 3853-6 -- Affordability exemption

**Input:** Single, household income $40,000. Lowest bronze plan = $3,500/year. 8.27% x $40,000 = $3,308.
**Expected:** $3,500 > $3,308. Coverage is unaffordable. Affordability exemption applies. No penalty. File Form 3853 claiming affordability exemption.

---

## Section 12 -- Self-checks

**Check 240 -- Coverage status determined for every household member.** Verify that each individual in the tax household has a month-by-month coverage determination.

**Check 241 -- 1095 forms reconciled.** Verify 1095-A, 1095-B, and/or 1095-C match the reported coverage months.

**Check 242 -- Exemptions properly claimed.** If an exemption is claimed, verify it is a recognized CA exemption and properly documented.

**Check 243 -- Short gap exemption used at most once.** If a short gap exemption is claimed, verify no other gap exemption is used in the same year.

**Check 244 -- Penalty uses the greater of flat dollar or percentage.** Verify both methods are computed and the larger is used.

**Check 245 -- Penalty does not exceed the bronze plan cap.** Verify the penalty is capped at the statewide average annual bronze plan premium.

**Check 246 -- Penalty flows to Form 540.** Verify the Form 3853 penalty amount appears on Form 540 Line 92 (verify line reference).

**Check 247 -- Sharing ministries flagged.** If taxpayer reports a health sharing ministry, verify it is NOT treated as MEC and penalty is computed.

**Check 248 -- STLDI flagged.** If taxpayer has short-term limited duration insurance, verify it is NOT treated as MEC.

---

## Section 13 -- Cross-skill references

**Inputs from:**
- `ca-540-individual-return` -- CA AGI, filing status, household composition
- `us-federal-return-assembly` -- federal MAGI if needed for exemption computations

**Outputs to:**
- `ca-540-individual-return` -- Form 3853 penalty amount for Form 540 Line 92
- `us-ca-return-assembly` -- Form 3853 worksheet for final package

---

## Section 14 -- Known gaps

1. Covered California premium amounts by zip code and household size are not embedded in this skill; they must be looked up at filing time.
2. The statewide average bronze plan premium cap for 2025 must be verified against FTB/Covered California publications.
3. Part-year residents require pro-rata analysis; this skill covers full-year residents primarily.
4. The affordability percentage (8.27%) is indexed and must be verified for 2025.
5. Hardship exemption determinations require case-by-case analysis beyond this skill's scope.

### Change log
- **v0.1 (April 2026):** Stub.
- **v0.2 (April 2026):** Full content skill with MEC definitions, exemptions, penalty computation, edge cases, and test suite.

## End of skill


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
