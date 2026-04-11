---
name: on-individual-return
description: >
  Use this skill whenever asked about Ontario provincial income tax for a self-employed sole proprietor. Trigger on phrases like "Ontario tax", "ON428", "Ontario income tax", "Ontario surtax", "Ontario Health Premium", "OHP", "OEPTC", "Ontario trillium", "provincial tax Ontario", or any question about computing Ontario provincial tax for a self-employed individual. Covers Ontario tax brackets, surtax, Ontario Health Premium, Ontario trillium benefit, and Ontario-specific credits. ALWAYS read this skill before touching any Ontario provincial tax work.
version: 1.0
jurisdiction: CA-ON
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
  - ca-fed-t1-return
---

# Ontario Provincial Income Tax -- Self-Employed Sole Proprietor Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Canada -- Ontario |
| Jurisdiction Code | CA-ON |
| Primary Legislation | Ontario Income Tax Act, 2000 (part of Taxation Act, 2007, S.O. 2007, c. 11, Sch. A) |
| Supporting Legislation | Income Tax Act (Canada) (ITA); Ontario Budget 2025 measures |
| Tax Authority | Canada Revenue Agency (CRA) on behalf of Ontario |
| Filing Portal | CRA My Account / NETFILE / EFILE |
| Form | ON428 -- Ontario Tax |
| Supporting Schedules | ON479 (Ontario Credits), ON-BEN (Ontario Trillium Benefit) |
| Contributor | Open Accountants Community |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: bracket application, surtax, OHP, personal credits, filing deadlines. Tier 2: OEPTC, OSTC, NOEC, medical expenses, charitable donations. Tier 3: interprovincial moves, part-year resident, trusts. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. CPA/CA must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any Ontario provincial tax figure, you MUST know:

1. **Province of residence on December 31** [T1] -- must be Ontario; if not, this skill does not apply
2. **Federal taxable income** [T1] -- from T1 line 26000 (drives Ontario tax brackets)
3. **Federal net income** [T1] -- from T1 line 23600 (drives OHP, credit clawbacks)
4. **Net self-employment income** [T1] -- from T2125
5. **Marital status and spouse/partner net income** [T1] -- affects spousal credit, OEPTC
6. **Number of children** [T1/T2] -- affects OSTC
7. **Property tax or rent paid** [T2] -- for OEPTC calculation
8. **Home energy costs** [T2] -- for NOEC (Northern Ontario Energy Credit) if applicable
9. **Municipality of residence** [T2] -- Northern Ontario vs. Southern Ontario (NOEC eligibility)
10. **Medical expenses, charitable donations, disability status** [T2] -- Ontario credits

**If province of residence is NOT Ontario on December 31, STOP. This skill does not apply.**

---

## Step 1: Ontario Tax Brackets -- 2025 [T1]

**Legislation:** Taxation Act, 2007, s. 3; 2025 indexed amounts

### 2025 Ontario Provincial Tax Rates

| Taxable Income (CAD) | Marginal Rate | Cumulative Tax at Top of Bracket |
|----------------------|---------------|----------------------------------|
| $0 -- $52,886 | 5.05% | $2,671 |
| $52,887 -- $105,775 | 9.15% | $2,671 + $4,839 = $7,510 |
| $105,776 -- $150,000 | 11.16% | $7,510 + $4,937 = $12,447 |
| $150,001 -- $220,000 | 12.16% | $12,447 + $8,512 = $20,959 |
| $220,001 + | 13.16% | $20,959 + ... |

**Note:** These brackets are indexed annually for Ontario CPI. Confirm exact indexed thresholds against CRA/Ontario published tables for the filing year.

### How to Apply [T1]

1. Start with **taxable income** from T1 line 26000
2. Apply each Ontario marginal rate to the portion of income within each bracket
3. Sum to get **gross Ontario tax** (ON428, line 12)
4. Subtract Ontario non-refundable credits (Step 2) to get **Ontario basic tax** (line 23)
5. Apply Ontario surtax (Step 3)
6. Add Ontario Health Premium (Step 4)
7. Subtract Ontario credits (Step 6) for final payable

---

## Step 2: Ontario Non-Refundable Tax Credits -- 2025 [T1]

**Legislation:** Taxation Act, 2007, s. 8 et seq.

All Ontario non-refundable credits are converted to tax savings at the **lowest Ontario marginal rate of 5.05%**.

### Personal Credit Amounts [T1]

| Credit | Amount (2025) | Tax Value (x 5.05%) |
|--------|---------------|---------------------|
| Basic personal amount | $11,865 | $599 |
| Spousal / common-law partner amount | $11,865 minus partner's net income (min $0) | up to $599 |
| Age amount (65+) | $5,590 (reduced at net income > $42,335) | up to $282 |
| CPP/CPP2 contributions (employer-equivalent portion) | actual amount | varies |
| EI premiums (if opted in) | actual amount | varies |

### Computation [T1]

1. Sum all applicable Ontario personal credit amounts
2. Multiply total by 5.05%
3. This is the **Ontario non-refundable credit** that reduces gross Ontario tax
4. Ontario tax cannot go below zero from non-refundable credits

---

## Step 3: Ontario Surtax -- 2025 [T1]

**Legislation:** Taxation Act, 2007, s. 3(2)

The Ontario surtax is an **additional tax on top of Ontario basic tax** for higher-income earners.

### Surtax Computation [T1]

| Component | Rate | Threshold |
|-----------|------|-----------|
| Surtax 1 | 20% | on Ontario basic tax exceeding $5,315 |
| Surtax 2 | 36% | on Ontario basic tax exceeding $6,802 |

### Formula [T1]

```
Ontario surtax = 20% x max(0, basic_tax - $5,315) + 36% x max(0, basic_tax - $6,802)
```

### How It Works [T1]

1. Compute Ontario basic tax (gross tax minus non-refundable credits)
2. If basic tax <= $5,315: no surtax
3. If basic tax > $5,315 but <= $6,802: surtax = 20% x (basic_tax - $5,315)
4. If basic tax > $6,802: surtax = 20% x (basic_tax - $5,315) + 36% x (basic_tax - $6,802)
5. Add surtax to basic tax to get **Ontario tax before OHP**

**Note:** The surtax thresholds are NOT indexed for inflation. They have been frozen at these levels for many years, capturing an increasing number of taxpayers annually.

---

## Step 4: Ontario Health Premium (OHP) -- 2025 [T1]

**Legislation:** Taxation Act, 2007, s. 3(5); Ontario Health Premium Amounts Regulation

The OHP is a progressive premium based on **taxable income**. It is NOT a tax credit reduction -- it is an additional amount added to Ontario tax.

### OHP Schedule [T1]

| Taxable Income (CAD) | OHP |
|----------------------|-----|
| $0 -- $20,000 | $0 |
| $20,001 -- $25,000 | 6% of income over $20,000 (max $300) |
| $25,001 -- $36,000 | $300 |
| $36,001 -- $38,500 | $300 + 6% of income over $36,000 (max $450) |
| $38,501 -- $48,000 | $450 |
| $48,001 -- $48,600 | $450 + 25% of income over $48,000 (max $600) |
| $48,601 -- $72,000 | $600 |
| $72,001 -- $72,600 | $600 + 25% of income over $72,000 (max $750) |
| $72,601 -- $200,000 | $750 |
| $200,001 -- $200,600 | $750 + 25% of income over $200,000 (max $900) |
| $200,601+ | $900 |

### Key Points [T1]

- Maximum OHP is **$900** per year
- OHP is based on **taxable income** (T1 line 26000), NOT net income
- OHP appears on ON428 line 61
- OHP amounts are NOT indexed for inflation

---

## Step 5: Ontario Dividend Tax Credits [T2]

**Legislation:** Taxation Act, 2007, s. 19

| Dividend Type | Federal Gross-Up | Ontario DTC Rate | Ontario DTC |
|---------------|------------------|------------------|-------------|
| Eligible dividends | 38% | 10.0% of grossed-up amount | reduces Ontario tax |
| Non-eligible dividends | 15% | 2.9863% of grossed-up amount | reduces Ontario tax |

**Self-employed relevance:** Only applicable if the sole proprietor also receives dividend income. Flag for reviewer if present.

---

## Step 6: Ontario Trillium Benefit (OTB) [T2]

**Legislation:** Taxation Act, 2007, Part IV

The OTB combines three credits paid monthly by CRA. Claimed on ON-BEN form, not ON428.

### Components [T2]

#### 6a. Ontario Energy and Property Tax Credit (OEPTC) [T2]

| Category | Maximum (2025 est.) |
|----------|---------------------|
| Non-senior (18-64) | $1,194 |
| Senior (65+) | $1,360 |

- Based on occupancy cost: property tax paid OR 20% of rent paid
- Reduced by 2% of adjusted family net income above $26,535 (estimated 2025)

#### 6b. Ontario Sales Tax Credit (OSTC) [T2]

| Recipient | Maximum (2025 est.) |
|-----------|---------------------|
| Individual | $360 |
| Spouse/partner | $360 |
| Per child under 19 | $360 |

- Reduced by 4% of adjusted family net income above $26,535 (estimated 2025)

#### 6c. Northern Ontario Energy Credit (NOEC) [T2]

| Category | Maximum (2025 est.) |
|----------|---------------------|
| Single | $180 |
| Family | $218 |

- Only available to residents of Northern Ontario districts
- Reduced by 2% of adjusted family net income above $26,535 (estimated 2025)

**Note:** CRA calculates and pays OTB automatically based on the ON-BEN form. This skill documents amounts for client advisory only.

---

## Step 7: ON428 Assembly [T1]

### Line-by-Line Summary

| ON428 Line | Description | Source |
|------------|-------------|--------|
| Line 1 | Taxable income | T1 line 26000 |
| Line 12 | Gross Ontario tax | Step 1 computation |
| Line 22 | Ontario non-refundable credits | Step 2 |
| Line 23 | Ontario basic tax (line 12 - line 22, min 0) | |
| Line 33 | Ontario surtax | Step 3 |
| Line 38 | Ontario tax before credits (line 23 + line 33) | |
| Line 45 | Ontario dividend tax credits | Step 5 |
| Line 49 | Ontario additional tax (foreign tax credit recovery) | |
| Line 56 | Net Ontario tax | |
| Line 61 | Ontario Health Premium | Step 4 |
| Line 62 | Ontario tax payable (line 56 + line 61) | Final amount |

---

## Step 8: Edge Cases and Special Rules

### 8a. Part-Year Ontario Resident [T3]

- Provincial tax is based on province of residence on **December 31**
- If resident of Ontario on Dec 31: full Ontario tax applies
- If NOT resident of Ontario on Dec 31: this skill does not apply
- **ESCALATE** part-year situations to reviewer

### 8b. Multiple Provinces of Self-Employment [T2]

- If business income was earned in multiple provinces, T2203 may be required
- This skill assumes all income is taxable in Ontario
- If multi-province allocation required, **FLAG for reviewer**

### 8c. Ontario Surtax Interaction with Credits [T1]

- The surtax is calculated on Ontario basic tax AFTER non-refundable credits
- Ontario tax credits (ON479) reduce tax AFTER surtax is added
- The ordering matters: credits -> basic tax -> surtax -> additional credits

### 8d. OHP Not Reducible by Credits [T1]

- The Ontario Health Premium is a separate charge
- It is NOT reduced by Ontario non-refundable credits or surtax credits
- OHP is added to net Ontario tax as a final step

### 8e. First Nations Tax Exemption [T3]

- Section 87 Indian Act exemptions may apply
- **ESCALATE** to reviewer -- do not compute

### 8f. Ontario Childcare Access and Relief from Expenses (CARE) Credit [T2]

- Refundable credit for childcare expenses
- Percentage depends on family income (75% at lowest income, declining to 0%)
- Only relevant if client has childcare expenses
- **FLAG for reviewer** if applicable

---

## Step 9: Prohibitions

1. **DO NOT** file or sign any return. This skill produces working papers only.
2. **DO NOT** apply this skill if province of residence on December 31 is not Ontario.
3. **DO NOT** compute tax for corporations, partnerships, or trusts.
4. **DO NOT** guess at First Nations exemption amounts.
5. **DO NOT** use prior-year bracket amounts -- always confirm 2025 indexed thresholds.
6. **DO NOT** combine this skill with another provincial skill for the same return year.
7. **DO NOT** reduce the Ontario Health Premium by tax credits.
8. **DO NOT** forget the surtax -- it dramatically increases effective rates above ~$90,000 taxable income.
9. **DO NOT** provide legal advice on residency disputes.

---

## Step 10: Test Suite

### Test 1 -- Low Income, Below OHP Threshold [T1]

| Input | Value |
|-------|-------|
| Taxable income | $18,000 |
| Net income | $18,000 |
| Status | Single, no dependants |

**Expected:**
- Gross Ontario tax: $18,000 x 5.05% = $909.00
- Ontario basic personal credit: $11,865 x 5.05% = $599.18
- Ontario basic tax: $909.00 - $599.18 = $309.82
- Ontario surtax: $0 (basic tax < $5,315)
- OHP: $0 (taxable income <= $20,000)
- Ontario tax payable: **$309.82**

### Test 2 -- Mid-Range Income, No Surtax [T1]

| Input | Value |
|-------|-------|
| Taxable income | $75,000 |
| Net income | $75,000 |
| Status | Single |

**Expected:**
- First $52,886 at 5.05% = $2,670.74
- $75,000 - $52,886 = $22,114 at 9.15% = $2,023.43
- Gross Ontario tax: $2,670.74 + $2,023.43 = $4,694.17
- Ontario basic personal credit: $599.18
- Ontario basic tax: $4,694.17 - $599.18 = $4,094.99
- Ontario surtax: $0 (basic tax < $5,315)
- OHP: $600 (income in $48,601-$72,000... wait, $75,000 is in $72,001-$72,600 range)
- Actually $75,000 > $72,600 so OHP = $750
- Ontario tax payable: $4,094.99 + $750 = **$4,844.99**

### Test 3 -- High Income, Surtax Applies [T1]

| Input | Value |
|-------|-------|
| Taxable income | $200,000 |
| Net income | $200,000 |
| Status | Single |

**Expected:**
- First $52,886 at 5.05% = $2,670.74
- $52,887 -- $105,775: $52,889 at 9.15% = $4,839.34
- $105,776 -- $150,000: $44,225 at 11.16% = $4,935.51
- $150,001 -- $200,000: $50,000 at 12.16% = $6,080.00
- Gross Ontario tax: $2,670.74 + $4,839.34 + $4,935.51 + $6,080.00 = $18,525.59
- Ontario basic personal credit: $599.18
- Ontario basic tax: $18,525.59 - $599.18 = $17,926.41
- Surtax 1: 20% x ($17,926.41 - $5,315) = 20% x $12,611.41 = $2,522.28
- Surtax 2: 36% x ($17,926.41 - $6,802) = 36% x $11,124.41 = $4,004.79
- Total surtax: $2,522.28 + $4,004.79 = $6,527.07
- OHP: $750 (taxable income in $72,601-$200,000 range)
- Ontario tax payable: $17,926.41 + $6,527.07 + $750 = **$25,203.48**

### Test 4 -- Below Basic Personal Amount [T1]

| Input | Value |
|-------|-------|
| Taxable income | $8,000 |
| Net income | $8,000 |
| Status | Single |

**Expected:**
- Gross Ontario tax: $8,000 x 5.05% = $404.00
- Ontario basic personal credit: $599.18
- Ontario basic tax: $0 (cannot go below zero)
- Ontario surtax: $0
- OHP: $0 (taxable income <= $20,000)
- Ontario tax payable: **$0**

### Test 5 -- Maximum OHP [T1]

| Input | Value |
|-------|-------|
| Taxable income | $250,000 |

**Expected:**
- OHP: **$900** (taxable income > $200,600)

---

## Step 11: Self-Checks

Before delivering output, verify:

- [ ] Province of residence on December 31 is confirmed as Ontario
- [ ] Taxable income matches T1 line 26000
- [ ] All 5 Ontario bracket rates applied correctly with 2025 indexed thresholds
- [ ] Basic personal amount uses 2025 indexed figure ($11,865)
- [ ] Ontario surtax computed on basic tax (AFTER non-refundable credits)
- [ ] Ontario Health Premium computed on taxable income using correct schedule
- [ ] OHP is NOT reduced by tax credits
- [ ] Non-refundable credits multiplied at 5.05% (lowest Ontario rate)
- [ ] Ontario tax payable is zero or positive (never negative before OHP)
- [ ] Part-year / multi-province situations flagged for reviewer
- [ ] Output traces to source documents

---

## Section 12 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
