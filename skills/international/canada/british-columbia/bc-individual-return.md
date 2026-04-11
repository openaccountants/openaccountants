---
name: bc-individual-return
description: >
  Use this skill whenever asked about British Columbia provincial income tax for a self-employed sole proprietor. Trigger on phrases like "BC tax", "BC428", "British Columbia income tax", "BC tax brackets", "BC tax reduction", "BC climate action tax credit", "provincial tax BC", or any question about computing BC provincial tax for a self-employed individual. Covers BC tax brackets, BC personal tax credits, BC tax reduction, climate action tax credit, and BC-specific rules. ALWAYS read this skill before touching any BC provincial tax work.
version: 1.0
jurisdiction: CA-BC
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
  - ca-fed-t1-return
---

# British Columbia Provincial Income Tax -- Self-Employed Sole Proprietor Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Canada -- British Columbia |
| Jurisdiction Code | CA-BC |
| Primary Legislation | BC Income Tax Act, RSBC 2002, c. 27 |
| Supporting Legislation | Income Tax Act (Canada) (ITA); BC Budget 2025 measures |
| Tax Authority | Canada Revenue Agency (CRA) on behalf of BC |
| Filing Portal | CRA My Account / NETFILE / EFILE |
| Form | BC428 -- British Columbia Tax |
| Supporting Schedules | BC(S12) -- BC Tax Reduction |
| Contributor | Open Accountants Community |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: bracket application, personal credits, BC tax reduction, filing deadlines. Tier 2: medical expenses, charitable donations, political contributions, disability credit. Tier 3: interprovincial moves, part-year resident, trusts. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. CPA/CA must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any BC provincial tax figure, you MUST know:

1. **Province of residence on December 31** [T1] -- must be BC; if not, this skill does not apply
2. **Federal taxable income** [T1] -- from T1 line 26000 (drives BC tax brackets)
3. **Federal net income** [T1] -- from T1 line 23600 (drives BC tax reduction, credit clawbacks)
4. **Net self-employment income** [T1] -- from T2125
5. **Marital status and spouse/partner net income** [T1] -- affects spousal credit, BC tax reduction
6. **Number of dependants** [T1/T2] -- affects BC tax reduction calculation
7. **Medical expenses claimed federally** [T2] -- if claiming BC medical expense credit
8. **Charitable donations claimed federally** [T2] -- if claiming BC donation credit
9. **Disability certificate (T2201)** [T2] -- if claiming BC disability credit
10. **BC political contributions** [T2] -- if claiming BC political contribution credit

**If province of residence is NOT BC on December 31, STOP. This skill does not apply.**

---

## Step 1: BC Tax Brackets -- 2025 [T1]

**Legislation:** BC ITA, s. 4.1; 2025 indexed amounts

### 2025 British Columbia Provincial Tax Rates

| Taxable Income (CAD) | Marginal Rate | Cumulative Tax at Top of Bracket |
|----------------------|---------------|----------------------------------|
| $0 -- $47,937 | 5.06% | $2,426 |
| $47,938 -- $95,875 | 7.70% | $2,426 + $3,691 = $6,117 |
| $95,876 -- $110,076 | 10.50% | $6,117 + $1,491 = $7,608 |
| $110,077 -- $133,664 | 12.29% | $7,608 + $2,900 = $10,508 |
| $133,665 -- $181,232 | 14.70% | $10,508 + $6,992 = $17,500 |
| $181,233 -- $252,752 | 16.80% | $17,500 + $12,015 = $29,515 |
| $252,753 + | 20.50% | $29,515 + ... |

**Note:** These brackets are indexed annually for BC CPI. The 2025 indexation factor is approximately 1.028. Confirm exact indexed thresholds against CRA/BC published tables for the filing year.

### How to Apply [T1]

1. Start with **taxable income** from T1 line 26000
2. Apply each BC marginal rate to the portion of income within each bracket
3. Sum to get **gross BC tax** (BC428, line 40)
4. Subtract BC non-refundable credits (Step 2) to get **BC basic tax**
5. Apply BC tax reduction (Step 3) if applicable
6. Result is **net BC tax payable**

---

## Step 2: BC Non-Refundable Tax Credits -- 2025 [T1]

**Legislation:** BC ITA, s. 4.3 et seq.

All BC non-refundable credits are converted to tax savings at the **lowest BC marginal rate of 5.06%**.

### Personal Credit Amounts [T1]

| Credit | Amount (2025) | Tax Value (x 5.06%) |
|--------|---------------|---------------------|
| Basic personal amount | $12,580 | $636 |
| Spousal / common-law partner amount | $12,580 minus partner's net income (min $0) | up to $636 |
| Age amount (65+) | $5,870 (reduced at net income > $40,495; eliminated at ~$86,179) | up to $297 |
| CPP/CPP2 contributions (employer-equivalent portion) | actual amount (half of self-employed CPP/CPP2) | varies |
| EI premiums (if opted in) | actual amount | varies |

### Computation [T1]

1. Sum all applicable BC personal credit amounts
2. Multiply total by 5.06%
3. This is the **BC non-refundable credit** that reduces gross BC tax
4. BC tax cannot go below zero from non-refundable credits

---

## Step 3: BC Tax Reduction -- 2025 [T1]

**Legislation:** BC ITA, s. 4.62; BC(S12)

The BC tax reduction provides additional relief for low-income individuals.

### Calculation [T1]

1. **Maximum reduction** = $521 (2025 indexed)
2. **Plus** $152 for each dependant (2025 indexed)
3. **Credit percentage** = 3.56% of net income
4. **Reduction = Maximum reduction - credit percentage of net income**
5. If result < 0, no reduction applies

### Thresholds [T1]

| Situation | Reduction Eliminated At (approx.) |
|-----------|-----------------------------------|
| Single, no dependants | net income ~ $14,635 |
| With 1 dependant | net income ~ $18,905 |

### Application [T1]

1. Compute BC basic tax (after non-refundable credits)
2. Compute BC tax reduction per formula above
3. Subtract reduction from BC basic tax
4. Result cannot go below zero

---

## Step 4: BC Dividend Tax Credits [T2]

**Legislation:** BC ITA, s. 4.69

| Dividend Type | Federal Gross-Up | BC DTC Rate | BC DTC |
|---------------|------------------|-------------|--------|
| Eligible dividends | 38% | 12.0% of grossed-up amount | reduces BC tax |
| Non-eligible dividends | 15% | 1.96% of grossed-up amount | reduces BC tax |

**Self-employed relevance:** Only applicable if the sole proprietor also receives dividend income from investments. Flag for reviewer if present.

---

## Step 5: BC Political Contribution Credit [T2]

**Legislation:** BC ITA, s. 4.73

| Contribution Amount | Credit |
|---------------------|--------|
| First $100 | 75% |
| $100.01 -- $550 | $75 + 50% of amount over $100 |
| $550.01 -- $1,150 | $300 + 33.33% of amount over $550 |
| Maximum credit | **$500** |

Must be a contribution to a registered BC political party or candidate.

---

## Step 6: Climate Action Tax Credit (CATC) [T1]

**Legislation:** BC ITA, s. 8.1; BC Climate Action Tax Credit Regulation

This is a **refundable** credit paid quarterly by CRA. Not calculated on BC428, but relevant for cash-flow planning.

### 2025 Amounts (estimated, subject to indexation) [T1]

| Recipient | Amount (annual) |
|-----------|-----------------|
| Individual | $504 |
| Spouse/common-law partner | $252 |
| Each child under 19 | $126 |

### Clawback [T1]

- Reduced by 2% of adjusted family net income above $41,071 (2025 estimate)
- Fully eliminated when family income exceeds threshold (varies by family size)

**Note:** CRA calculates and pays CATC automatically. This skill documents amounts for client advisory only.

---

## Step 7: BC428 Assembly [T1]

### Line-by-Line Summary

| BC428 Line | Description | Source |
|------------|-------------|--------|
| Line 1 | Taxable income | T1 line 26000 |
| Line 40 | Gross BC tax | Step 1 computation |
| Line 47 | BC non-refundable credits | Step 2 |
| Line 48 | BC basic tax (line 40 - line 47, min 0) | |
| Line 52 | BC tax reduction | Step 3 |
| Line 56 | Net BC tax (line 48 - line 52, min 0) | |
| Line 60 | BC dividend tax credits | Step 4 |
| Line 62 | BC political contribution credit | Step 5 |
| Line 70 | BC tax payable | Final provincial tax |

---

## Step 8: Edge Cases and Special Rules

### 8a. Part-Year BC Resident [T3]

If the individual moved into or out of BC during the year:
- Provincial tax is based on province of residence on **December 31**
- If resident of BC on Dec 31: full BC tax applies on worldwide income
- If NOT resident of BC on Dec 31: this skill does not apply
- **ESCALATE** part-year situations to reviewer

### 8b. Multiple Provinces of Self-Employment [T2]

If business income was earned in multiple provinces:
- Federal tax is allocated among provinces using T2203 (Provincial and Territorial Taxes for Multiple Jurisdictions)
- This skill assumes all income is taxable in BC
- If multi-province allocation required, **FLAG for reviewer** and load T2203 rules

### 8c. First Nations Tax Exemption [T3]

- Section 87 of the Indian Act exempts certain income earned by Status Indians on-reserve
- If client is a Status Indian with on-reserve business income, **ESCALATE**
- Do NOT attempt to compute exemption without reviewer guidance

### 8d. BC Training Tax Credit (Expired) [T1]

- The BC training tax credit for apprentices expired after 2014
- Do NOT claim this credit for 2025 returns
- If client asks about training credits, advise that the federal Canada Training Credit (CTC) may apply (computed on the federal return)

### 8e. BC Home Renovation Tax Credit for Seniors [T2]

- Available to individuals 65+ or living with a family member 65+
- 10% of eligible renovation expenses (max $10,000 in expenses = $1,000 credit)
- Only available for principal residence in BC
- **FLAG for reviewer** if client is 65+ and has renovation receipts

### 8f. BC Renter's Tax Credit (2025+) [T2]

- BC introduced a renter's tax credit starting 2024
- Up to $400 per year for tenants with adjusted income under threshold
- **FLAG for reviewer** if client rents their residence
- Note: a sole proprietor who uses home office may claim either the renter credit or home office deduction (T2125) for the rental portion, but not both for the same space

---

## Step 9: Prohibitions

1. **DO NOT** file or sign any return. This skill produces working papers only.
2. **DO NOT** apply this skill if province of residence on December 31 is not BC.
3. **DO NOT** compute tax for corporations, partnerships, or trusts.
4. **DO NOT** guess at First Nations exemption amounts.
5. **DO NOT** use prior-year bracket amounts -- always confirm 2025 indexed thresholds.
6. **DO NOT** combine this skill with another provincial skill for the same return year.
7. **DO NOT** provide legal advice on residency disputes.
8. **DO NOT** claim expired credits (training tax credit, etc.).

---

## Step 10: Test Suite

### Test 1 -- Low Income, Single [T1]

| Input | Value |
|-------|-------|
| Taxable income | $25,000 |
| Net income | $25,000 |
| Status | Single, no dependants |

**Expected:**
- Gross BC tax: $25,000 x 5.06% = $1,265.00
- BC basic personal credit: $12,580 x 5.06% = $636.55
- BC basic tax: $1,265.00 - $636.55 = $628.45
- BC tax reduction: $521 - (3.56% x $25,000) = $521 - $890 = $0 (reduction eliminated)
- Net BC tax: **$628.45**

### Test 2 -- Mid-Range Income [T1]

| Input | Value |
|-------|-------|
| Taxable income | $80,000 |
| Net income | $80,000 |
| Status | Single, no dependants |

**Expected:**
- First $47,937 at 5.06% = $2,425.61
- $80,000 - $47,937 = $32,063 at 7.70% = $2,468.85
- Gross BC tax: $2,425.61 + $2,468.85 = $4,894.46
- BC basic personal credit: $636.55
- BC basic tax: $4,894.46 - $636.55 = $4,257.91
- BC tax reduction: eliminated (net income >> $14,635)
- Net BC tax: **$4,257.91**

### Test 3 -- High Income, Top Bracket [T1]

| Input | Value |
|-------|-------|
| Taxable income | $300,000 |
| Net income | $300,000 |
| Status | Married, spouse net income $0 |

**Expected:**
- Tax through $252,752 = $29,515 (from bracket table)
- $300,000 - $252,752 = $47,248 at 20.50% = $9,685.84
- Gross BC tax: $29,515 + $9,685.84 = $39,200.84
- BC basic personal credit: $636.55
- BC spousal credit: $12,580 x 5.06% = $636.55
- Total credits: $1,273.10
- BC basic tax: $39,200.84 - $1,273.10 = $37,927.74
- Net BC tax: **$37,927.74**

### Test 4 -- Below Basic Personal Amount [T1]

| Input | Value |
|-------|-------|
| Taxable income | $10,000 |
| Net income | $10,000 |
| Status | Single, no dependants |

**Expected:**
- Gross BC tax: $10,000 x 5.06% = $506.00
- BC basic personal credit: $636.55
- BC basic tax: $506.00 - $636.55 = $0 (cannot go below zero)
- Net BC tax: **$0**

### Test 5 -- BC Tax Reduction Applies [T1]

| Input | Value |
|-------|-------|
| Taxable income | $13,000 |
| Net income | $13,000 |
| Status | Single, no dependants |

**Expected:**
- Gross BC tax: $13,000 x 5.06% = $657.80
- BC basic personal credit: $636.55
- BC basic tax: $657.80 - $636.55 = $21.25
- BC tax reduction: $521 - (3.56% x $13,000) = $521 - $462.80 = $58.20
- Reduction exceeds basic tax, so reduction capped at $21.25
- Net BC tax: **$0**

---

## Step 11: Self-Checks

Before delivering output, verify:

- [ ] Province of residence on December 31 is confirmed as BC
- [ ] Taxable income matches T1 line 26000
- [ ] All 7 BC bracket rates applied correctly with 2025 indexed thresholds
- [ ] Basic personal amount uses 2025 indexed figure ($12,580)
- [ ] BC tax reduction computed using correct formula and 2025 amounts
- [ ] Non-refundable credits multiplied at 5.06% (lowest BC rate)
- [ ] BC tax payable is zero or positive (never negative)
- [ ] No expired credits claimed
- [ ] Part-year / multi-province situations flagged for reviewer
- [ ] Output traces to source documents

---

## Section 12 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
