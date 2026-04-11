---
name: au-medicare-levy
description: >
  Use this skill whenever asked about the Australian Medicare Levy, Medicare Levy Surcharge (MLS), low-income reduction thresholds, family thresholds, surcharge tiers, private health insurance (PHI) rebate interaction, or Medicare levy exemptions. Trigger on phrases like "Medicare levy", "Medicare surcharge", "MLS", "do I pay Medicare levy", "low income Medicare", "Medicare levy reduction", "Medicare levy exemption", "private health insurance rebate", "PHI rebate", "M1", "M2", or any question about Medicare-related levies on an Australian tax return. ALWAYS read this skill before touching any Medicare levy work.
---

# Australia Medicare Levy & Medicare Levy Surcharge -- Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Australia |
| Jurisdiction Code | AU |
| Primary Legislation | Medicare Levy Act 1986 (MLA 1986); A New Tax System (Medicare Levy Surcharge -- Fringe Benefits) Act 1999 |
| Supporting Legislation | ITAA 1997 Div 61 (Medicare levy); ITAA 1997 s 8C-8G (MLS); Health Insurance Act 1973; Private Health Insurance Act 2007 |
| Tax Authority | Australian Taxation Office (ATO) |
| Tax Year | 2024-25 (1 July 2024 -- 30 June 2025) |
| Return Items | Item M1 (Medicare levy reduction or exemption); Item M2 (Medicare levy surcharge) |
| Contributor | Open Accountants |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: standard levy calculation, low-income reduction, surcharge tiers, family thresholds. Tier 2: half-year exemptions, part-year residents, PHI rebate tier selection. Tier 3: Norfolk Island transitional, diplomatic exemptions, prescribed overseas forces. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any Medicare levy figure, you MUST know:

1. **Residency status for tax purposes** [T1] -- Australian resident, foreign resident, or temporary resident
2. **Taxable income for the year** [T1] -- Medicare levy is calculated on taxable income
3. **Marital/family status** [T1] -- single, married/de facto, with or without dependent children
4. **Number of dependent children** [T1] -- affects family threshold
5. **Spouse's taxable income** [T1] -- affects family threshold eligibility and MLS
6. **Private health insurance status** [T1] -- does the client (and family) hold appropriate private patient hospital cover for the full year?
7. **Any days of exemption?** [T2] -- foreign resident days, specific medical condition categories
8. **Entitlement to SAPTO?** [T1] -- seniors and pensioners get higher Medicare levy reduction thresholds

---

## Step 1: Standard Medicare Levy [T1]

**Legislation:** Medicare Levy Act 1986 s 6

| Item | Value |
|------|-------|
| Medicare levy rate | 2% of taxable income |
| Who pays | All Australian residents for tax purposes (with limited exemptions) |

### Formula

```
Medicare levy = taxable income x 2%
```

The Medicare levy is calculated on **taxable income** (not gross income, not adjusted taxable income). It is applied automatically by the ATO when the tax return is assessed.

---

## Step 2: Low-Income Reduction -- Singles [T1]

**Legislation:** Medicare Levy Act 1986 s 7

### Thresholds for 2024-25

| Category | Lower Threshold (no levy) | Upper Threshold (full levy) | Shade-in Rate |
|----------|--------------------------|---------------------------|--------------|
| Single (general) | $27,222 | $34,027 | 10 cents per $1 |
| Single (senior/pensioner entitled to SAPTO) | $43,020 | $53,775 | 10 cents per $1 |

### How the reduction works

- **Taxable income at or below the lower threshold:** No Medicare levy payable.
- **Taxable income between lower and upper threshold:** Reduced levy applies (shade-in).
- **Taxable income above the upper threshold:** Full 2% Medicare levy applies.

### Shade-in Formula

```
If taxable_income <= $27,222:
  Medicare levy = $0

If $27,222 < taxable_income <= $34,027:
  Medicare levy = (taxable_income - $27,222) x 10%

If taxable_income > $34,027:
  Medicare levy = taxable_income x 2%
```

**The shade-in rate of 10% means the levy increases by 10 cents for every dollar earned above the lower threshold,** until the reduced levy equals the standard 2% levy (which occurs at the upper threshold). The formula is designed so that at $34,027 the shade-in amount equals $34,027 x 2% = $680.54.

---

## Step 3: Low-Income Reduction -- Families [T1]

**Legislation:** Medicare Levy Act 1986 s 8

### Thresholds for 2024-25

| Category | Family Lower Threshold | Increase Per Dependent Child |
|----------|----------------------|----------------------------|
| Family (general) | $45,907 | + $4,216 per dependent child |
| Family (senior/pensioner entitled to SAPTO) | $63,486 | + $4,216 per dependent child |

### How the family reduction works

- **Family income at or below the family threshold:** No Medicare levy payable for either spouse.
- **Family income above the family threshold:** Each spouse pays their individual share of the family levy, subject to individual reduction rules.

### Family Threshold Calculation

```
Family threshold = $45,907 + ($4,216 x number_of_dependent_children)
```

**Example:** Family with 2 dependent children:
Family threshold = $45,907 + ($4,216 x 2) = $54,339

**"Family income"** for Medicare levy purposes = combined taxable income of both spouses + any exempt foreign employment income + any net financial investment loss + reportable super contributions.

### Individual Threshold for Family Members

If you had a spouse or dependent children for the full year and your individual taxable income was $34,027 or less ($53,775 for SAPTO), you are also entitled to the individual low-income reduction regardless of family income.

---

## Step 4: Medicare Levy Surcharge (MLS) [T1]

**Legislation:** ITAA 1997 s 8C-8G; A New Tax System (Medicare Levy Surcharge -- Fringe Benefits) Act 1999

The MLS is a separate levy on top of the standard 2% Medicare levy. It applies to taxpayers who do **NOT** hold appropriate private patient hospital cover and whose income exceeds the MLS threshold.

### MLS Income Definition

```
Income for MLS purposes = taxable income
  + reportable fringe benefits total
  + total net investment loss (including net financial investment loss and net rental property loss)
  + super lump sum (taxed element, untaxed element)
  -- less child support paid
```

### MLS Thresholds and Rates -- Singles (2024-25) [T1]

| Tier | Income for MLS Purposes | MLS Rate |
|------|------------------------|----------|
| Base | $97,000 or less | 0.0% |
| Tier 1 | $97,001 -- $113,000 | 1.0% |
| Tier 2 | $113,001 -- $151,000 | 1.25% |
| Tier 3 | $151,001 or more | 1.5% |

### MLS Thresholds and Rates -- Families (2024-25) [T1]

| Tier | Family Income for MLS Purposes | MLS Rate |
|------|-------------------------------|----------|
| Base | $194,000 or less | 0.0% |
| Tier 1 | $194,001 -- $226,000 | 1.0% |
| Tier 2 | $226,001 -- $302,000 | 1.25% |
| Tier 3 | $302,001 or more | 1.5% |

**The family income threshold increases by $1,500 for each MLS dependent child after the first child.**

### Key MLS Rules

1. **The MLS applies for each day you (and/or your dependants) do not have appropriate private hospital cover.** If cover was held for part of the year only, MLS is pro-rated for uncovered days.
2. **"Appropriate" cover** means private patient hospital cover with an excess (front-end deductible) of no more than $750 for singles or $1,500 for families/couples.
3. **MLS is calculated on taxable income for MLS purposes, not standard taxable income.** The MLS income definition includes reportable fringe benefits and net investment losses.
4. **If married/de facto, the family threshold applies** regardless of whether the spouse earns income.

---

## Step 5: Private Health Insurance (PHI) Rebate Interaction [T1]

**Legislation:** Private Health Insurance Act 2007 Part 2-2; ITAA 1997 Div 61

The PHI rebate and the MLS use the same income tiers but serve opposite purposes:
- **PHI rebate** = government subsidy for holding private health insurance (reduces with higher income)
- **MLS** = penalty for NOT holding private health insurance (increases with higher income)

### PHI Rebate Tiers -- 2024-25

| Tier | Singles Income | Families Income | Rebate (under 65) | Rebate (65-69) | Rebate (70+) |
|------|---------------|----------------|-------------------|----------------|--------------|
| Base | $97,000 or less | $194,000 or less | 24.608% | 28.710% | 32.812% |
| Tier 1 | $97,001 -- $113,000 | $194,001 -- $226,000 | 16.405% | 20.507% | 24.608% |
| Tier 2 | $113,001 -- $151,000 | $226,001 -- $302,000 | 8.202% | 12.303% | 16.405% |
| Tier 3 | $151,001+ | $302,001+ | 0.000% | 0.000% | 0.000% |

**Planning note:** For clients in Tier 1 or Tier 2 MLS, holding private hospital cover eliminates the MLS AND provides the PHI rebate. The cost of private cover is often less than the MLS, making it financially beneficial.

---

## Step 6: Medicare Levy Exemptions [T1 / T2]

**Legislation:** Medicare Levy Act 1986 s 8; Health Insurance Act 1973

### Full Exemption Categories [T1]

| Category | Exemption |
|----------|-----------|
| Foreign residents (for the full year) | Full exemption from Medicare levy for the entire year |
| Temporary residents not eligible for Medicare | Full exemption (must hold valid visa and not be enrolled in Medicare) |

### Half or Partial Exemption Categories [T2]

| Category | Exemption |
|----------|-----------|
| Part-year residents | Pro-rata exemption for non-resident days. [T2] flag for reviewer. |
| Specific medical conditions (Category 1) | Blind persons -- full exemption. Complete Medicare Levy Exemption Statement. |
| Specific medical conditions (Category 2) | Persons in specified care -- partial or full exemption depending on circumstances. [T2] flag for reviewer. |

### Reciprocal Health Care Agreements [T2]

Australia has reciprocal health care agreements with several countries (UK, Ireland, New Zealand, Sweden, Netherlands, Belgium, Finland, Italy, Norway, Slovenia, Malta). Residents of these countries visiting Australia may be entitled to Medicare and therefore NOT exempt from the levy. [T2] flag for reviewer to confirm coverage.

**Foreign residents who are NOT covered by a reciprocal agreement and NOT enrolled in Medicare are exempt from the Medicare levy.** They must complete item M1 on the tax return.

---

## Step 7: Completing the Tax Return [T1]

### Item M1 -- Medicare Levy Reduction or Exemption

Complete M1 if:
- Taxable income is within the low-income shade-in range
- You are claiming a full or half exemption
- You had a spouse during the year

### Item M2 -- Medicare Levy Surcharge

Complete M2 if:
- You (or your spouse/dependants) did not have appropriate private hospital cover for any day during the year
- Your income for MLS purposes exceeds the relevant threshold ($97,000 singles / $194,000 families)

**If the client held appropriate cover for the full year, M2 does not need to be completed** (no MLS is payable).

---

## Step 8: Edge Case Registry

### EC1 -- Part-year resident [T2]
**Situation:** Client was a foreign resident for 3 months then became an Australian resident for the remaining 9 months.
**Resolution:** Medicare levy is calculated on the full year's taxable income, but a pro-rata exemption applies for the non-resident period. The exemption is calculated as: (exempt days / total days in year) x total Medicare levy. [T2] flag for reviewer -- residency determination is complex.

### EC2 -- Couple where one spouse has PHI and the other does not [T2]
**Situation:** Client has private hospital cover but their spouse does not.
**Resolution:** The MLS applies to BOTH spouses unless ALL family members (including dependants) hold appropriate cover. If the spouse is not covered, MLS is payable by both on their respective taxable incomes. [T2] flag for reviewer.

### EC3 -- Client earns just above the low-income threshold [T1]
**Situation:** Single client with taxable income of $28,000.
**Resolution:** Shade-in applies. Medicare levy = ($28,000 - $27,222) x 10% = $77.80. This is less than the full 2% levy of $560.00.

### EC4 -- Client has net investment losses inflating MLS income [T2]
**Situation:** Client's taxable income is $90,000 but has a net rental property loss of $15,000 (deducted from taxable income). Income for MLS purposes = $90,000 + $15,000 = $105,000.
**Resolution:** Even though taxable income is below $97,000, income for MLS purposes exceeds $97,000 and MLS applies at 1.0% if no private hospital cover is held. [T2] flag for reviewer -- confirm MLS income calculation.

### EC5 -- SAPTO-entitled pensioner with low income [T1]
**Situation:** Pensioner aged 68, taxable income $45,000, entitled to SAPTO.
**Resolution:** SAPTO singles threshold is $43,020 (lower) and $53,775 (upper). At $45,000, the shade-in applies: ($45,000 - $43,020) x 10% = $198.00. Full 2% levy would be $900.00. The reduced amount of $198.00 applies.

### EC6 -- Family with 4 dependent children [T1]
**Situation:** Family with 4 dependent children, combined family income $55,000.
**Resolution:** Family threshold = $45,907 + ($4,216 x 4) = $62,771. Family income of $55,000 is below the threshold. No Medicare levy payable.

### EC7 -- MLS with private hospital cover held for part of year [T2]
**Situation:** Client held appropriate PHI for 200 days of the year, no cover for 165 days. Single, income for MLS purposes $120,000.
**Resolution:** MLS is pro-rated for the 165 uncovered days. MLS = $120,000 x 1.25% x (165/365) = $678.08 (approximately). [T2] flag for reviewer -- confirm exact uncovered days.

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

### Test 1 -- Standard Medicare levy, no reduction
**Input:** Single, Australian resident, taxable income $80,000. Has PHI.
**Expected output:** Medicare levy = $80,000 x 2% = $1,600.00. No MLS (has PHI).

### Test 2 -- Low-income reduction (single)
**Input:** Single, taxable income $30,000. No spouse.
**Expected output:** Shade-in applies. Levy = ($30,000 - $27,222) x 10% = $277.80.

### Test 3 -- Below low-income threshold
**Input:** Single, taxable income $25,000.
**Expected output:** Medicare levy = $0. Below $27,222 lower threshold.

### Test 4 -- MLS Tier 1 (single, no PHI)
**Input:** Single, income for MLS purposes $105,000. No private hospital cover.
**Expected output:** Medicare levy = $105,000 x 2% = $2,100.00. MLS = $105,000 x 1.0% = $1,050.00. Total Medicare-related charges = $3,150.00.

### Test 5 -- MLS Tier 3 (single, no PHI)
**Input:** Single, income for MLS purposes $200,000. No private hospital cover.
**Expected output:** Medicare levy = $200,000 x 2% = $4,000.00. MLS = $200,000 x 1.5% = $3,000.00. Total = $7,000.00.

### Test 6 -- Family below family threshold
**Input:** Family, 2 dependent children, combined family income $50,000.
**Expected output:** Family threshold = $45,907 + ($4,216 x 2) = $54,339. Family income $50,000 < $54,339. No Medicare levy payable.

### Test 7 -- Foreign resident full exemption
**Input:** Foreign resident for the full year. Taxable income $60,000 (Australian-sourced).
**Expected output:** Full Medicare levy exemption. Levy = $0. Must complete item M1.

### Test 8 -- MLS family threshold with children
**Input:** Family, 3 children, combined income for MLS purposes $200,000. No PHI.
**Expected output:** Family MLS threshold = $194,000 + ($1,500 x 2 children after the first) = $197,000. Income $200,000 > $197,000. MLS Tier 1 = 1.0% applies.

---

## PROHIBITIONS

- NEVER apply the Medicare levy to a confirmed full-year foreign resident who is not enrolled in Medicare
- NEVER ignore the MLS income definition -- it is NOT the same as taxable income (includes reportable fringe benefits and net investment losses)
- NEVER tell a client they avoid MLS simply because their taxable income is below $97,000 -- check income for MLS purposes
- NEVER apply the general low-income threshold ($27,222) to a SAPTO-entitled senior -- use the SAPTO thresholds ($43,020 / $53,775)
- NEVER assume PHI eliminates MLS unless the cover is "appropriate" (private patient hospital cover with excess no more than $750 singles / $1,500 families)
- NEVER present Medicare levy figures as definitive -- always label as estimated and direct client to their ATO assessment for confirmation
- NEVER advise on diplomatic or prescribed overseas forces exemptions -- [T3] escalate
- NEVER confuse the Medicare levy (2% on taxable income) with the Medicare Levy Surcharge (1%-1.5% on MLS income for those without PHI) -- they are separate charges

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax agent, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
