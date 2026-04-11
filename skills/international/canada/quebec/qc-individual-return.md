---
name: qc-individual-return
description: >
  Use this skill whenever asked about Quebec provincial income tax (TP-1) for a self-employed sole proprietor. Trigger on phrases like "Quebec tax", "TP-1", "Quebec income tax", "Quebec brackets", "QPP", "QPIP", "Revenu Quebec", "QHSF", "health services fund", "solidarity tax credit", "Quebec abatement", or any question about computing Quebec provincial tax for a self-employed individual. Covers Quebec's separate tax brackets, QPP contributions, QHSF, Quebec abatement, and Quebec-specific credits. ALWAYS read this skill before touching any Quebec provincial tax work.
version: 1.0
jurisdiction: CA-QC
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
  - ca-fed-t1-return
---

# Quebec TP-1 Provincial Income Tax -- Self-Employed Sole Proprietor Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Canada -- Quebec |
| Jurisdiction Code | CA-QC |
| Primary Legislation | Taxation Act (Quebec), CQLR c. I-3 |
| Supporting Legislation | Act respecting the Quebec Pension Plan (QPP); Act respecting parental insurance (QPIP); ITA (Canada) |
| Tax Authority | Revenu Quebec (provincial); CRA (federal) |
| Filing Portal | Revenu Quebec My Account (ImpotNet) / CRA My Account (federal return only) |
| Form | TP-1 -- Quebec Income Tax Return (filed SEPARATELY from federal T1) |
| Supporting Schedules | Schedule E (QPP), Schedule F (QPIP), Schedule B (tax credits), TP-80 (self-employment income) |
| Contributor | Open Accountants Community |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: bracket application, personal credits, QPP, QPIP, QHSF, Quebec abatement, filing deadlines. Tier 2: solidarity credit, medical expenses, charitable donations, work premium. Tier 3: interprovincial moves, part-year resident, trusts, corporate integration. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. CPA/CA must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## CRITICAL: Quebec Files a Separate Provincial Return

Unlike all other Canadian provinces (where CRA administers provincial tax via the T1), Quebec administers its own income tax system. Quebec residents must file:

1. **Federal T1** with CRA (with the 16.5% Quebec abatement reducing federal tax)
2. **TP-1** with Revenu Quebec (completely separate return with separate brackets, credits, and rules)

This skill covers the **TP-1 (Quebec provincial return)** only.

---

## Step 0: Client Onboarding Questions

Before computing any Quebec provincial tax figure, you MUST know:

1. **Province of residence on December 31** [T1] -- must be Quebec; if not, this skill does not apply
2. **Total income** [T1] -- Quebec computes its own total income (may differ from federal)
3. **Net self-employment income** [T1] -- from TP-80 (Quebec equivalent of T2125)
4. **Marital status and spouse/partner net income** [T1] -- affects credits
5. **Number of dependant children** [T1/T2] -- affects family-related credits
6. **QPP contributions from employment** [T1] -- if any T4/RL-1 employment income
7. **QPIP premiums from employment** [T1] -- from RL-1
8. **Rent paid or property tax paid** [T2] -- for solidarity tax credit
9. **Municipal address** [T2] -- solidarity credit varies by region
10. **Medical expenses, charitable donations, disability status** [T2] -- Quebec credits

**If province of residence is NOT Quebec on December 31, STOP. This skill does not apply.**

---

## Step 1: Quebec Tax Brackets -- 2025 [T1]

**Legislation:** Taxation Act (Quebec), s. 750; 2025 indexed amounts

### 2025 Quebec Provincial Tax Rates

| Taxable Income (CAD) | Marginal Rate |
|----------------------|---------------|
| $0 -- $53,255 | 14% |
| $53,256 -- $106,495 | 19% |
| $106,496 -- $129,590 | 24% |
| $129,591 + | 25.75% |

**Note:** Quebec brackets are indexed annually using the Quebec CPI (excluding alcohol and tobacco). Confirm exact indexed thresholds against Revenu Quebec published tables.

### How to Apply [T1]

1. Start with **Quebec taxable income** (TP-1 line 299)
2. Apply each Quebec marginal rate to the portion of income within each bracket
3. Sum to get **gross Quebec tax** (TP-1 line 401)
4. Subtract Quebec non-refundable credits (Step 2) to get **Quebec net tax**
5. Subtract additional refundable credits (Step 6)

---

## Step 2: Quebec Non-Refundable Tax Credits -- 2025 [T1]

**Legislation:** Taxation Act (Quebec), s. 752 et seq.

Quebec non-refundable credits are converted at **14%** (the lowest Quebec rate) unless otherwise specified.

### Personal Credit Amounts [T1]

| Credit | Amount (2025) | Tax Value (x 14%) |
|--------|---------------|---------------------|
| Basic personal amount (amount for a person living alone) | $18,056 | $2,528 |
| Person living alone supplement | $2,200 (if applicable) | $308 |
| Spouse/partner amount | varies (transfer of unused credits) | varies |
| Age amount (65+) | $3,640 | $510 |
| Retirement income amount | up to $3,017 | up to $422 |

**Note:** Quebec's basic personal amount is significantly higher than other provinces because Quebec has higher marginal rates.

### Computation [T1]

1. Sum all applicable Quebec personal credit amounts
2. Multiply total by 14% (or applicable rate for specific credits)
3. This is the **Quebec non-refundable credit** that reduces gross Quebec tax
4. Quebec tax cannot go below zero from non-refundable credits

---

## Step 3: Quebec Pension Plan (QPP) -- Self-Employed -- 2025 [T1]

**Legislation:** Act respecting the Quebec Pension Plan, s. 50 et seq.

Quebec residents contribute to QPP instead of CPP.

### QPP Base Contributions (2025) [T1]

| Item | Amount |
|------|--------|
| Maximum Pensionable Earnings (MPE) | $71,300 |
| Basic exemption | $3,500 |
| Maximum contributory earnings | $67,800 |
| Employee rate | 6.40% |
| Self-employed rate (double) | **12.80%** |
| Maximum self-employed QPP contribution | $67,800 x 12.80% = **$8,678.40** |

### QPP2 -- Second Additional QPP (2025) [T1]

| Item | Amount |
|------|--------|
| Year's Additional Maximum Pensionable Earnings (YAMPE) | $81,200 |
| QPP2 earnings range | $71,300 to $81,200 = $9,900 |
| Employee QPP2 rate | 4.00% |
| Self-employed QPP2 rate (double) | **8.00%** |
| Maximum self-employed QPP2 contribution | $9,900 x 8.00% = **$792.00** |

### QPP Computation for Self-Employed [T1]

1. **Pensionable self-employment earnings** = net self-employment income from TP-80
2. If earnings < $3,500: no QPP required
3. If earnings >= $3,500 and <= $71,300: QPP = (earnings - $3,500) x 12.80%
4. If earnings > $71,300: QPP = maximum $8,678.40
5. **QPP2:** same logic as CPP2 but using QPP2 rates
6. Half of self-employed QPP/QPP2 is deductible from income (employer portion); other half is a non-refundable credit

**Note:** QPP rates are slightly higher than CPP rates. Do NOT use CPP rates for Quebec residents.

---

## Step 4: Quebec Parental Insurance Plan (QPIP) -- 2025 [T1]

**Legislation:** Act respecting parental insurance; QPIP Regulation

Quebec residents pay QPIP premiums instead of being covered by federal EI for parental/maternity benefits.

### Self-Employed QPIP (2025) [T1]

| Item | Amount |
|------|--------|
| Maximum insurable earnings | $98,000 |
| Self-employed premium rate | 0.878% |
| Maximum self-employed QPIP premium | $98,000 x 0.878% = **$860.44** |

### Computation [T1]

1. QPIP applies to net self-employment income
2. If self-employment income <= $2,000: no QPIP payable
3. If self-employment income > $2,000: QPIP = min(income, $98,000) x 0.878%
4. QPIP premiums are fully deductible from Quebec income

---

## Step 5: Quebec Health Services Fund (QHSF) -- Self-Employed -- 2025 [T1]

**Legislation:** Act respecting the Regie de l'assurance maladie du Quebec (RAMQ), s. 34

Self-employed individuals pay the QHSF contribution directly on their TP-1.

### QHSF Rates for Self-Employed (2025) [T1]

| Net Income | QHSF Rate |
|------------|-----------|
| $0 -- $16,780 | 0% |
| $16,781 -- $59,885 | Graduated from 0% to 1% |
| $59,886+ | 1% of total net income |

### Graduated Calculation [T1]

For income between $16,780 and $59,885:

QHSF = (net income - $16,780) x (net income x 1%) / ($59,885 - $16,780)

For income above $59,885:

QHSF = net income x 1%

**Maximum QHSF** is not capped (1% of total net income at higher incomes).

---

## Step 6: Quebec Refundable Credits [T2]

### 6a. Solidarity Tax Credit [T2]

**Legislation:** Taxation Act (Quebec), s. 1029.8.116.12 et seq.

Paid monthly by Revenu Quebec. Claimed on Schedule D.

| Component | Maximum (2025 est.) |
|-----------|---------------------|
| QST component | $360 per adult |
| Housing component | $756 (if property tax/rent paid) |
| Northern village component | $2,005 (Inuit/Cree communities) |

- Reduced by 3% of family net income above $40,060 (estimated 2025)

### 6b. Work Premium [T2]

| Category | Maximum (2025 est.) |
|----------|---------------------|
| Single, no children | $1,117 |
| Couple, no children | $1,737 |
| Single, with children | $2,629 |
| Couple, with children | $3,570 |

- Based on work income exceeding $2,400 (single) or $3,600 (couple)
- Reduced above income thresholds

### 6c. Medical Expenses Credit [T2]

- Quebec allows 25% of medical expenses exceeding 3% of family income
- This is a refundable credit (unlike federal non-refundable medical credit)
- **FLAG for reviewer** if client has significant medical expenses

---

## Step 7: Quebec Abatement on Federal Return [T1]

**Legislation:** ITA (Canada), s. 120(2)

Because Quebec collects its own income tax, Quebec residents receive a **16.5% abatement** on federal basic tax.

### Computation [T1]

1. Compute federal basic tax (from T1 Schedule 1)
2. Quebec abatement = federal basic tax x 16.5%
3. Abatement reduces federal tax payable (T1 line 44000)

**This abatement is computed on the federal T1, not the TP-1. But it is essential context for total tax planning.**

---

## Step 8: TP-1 Assembly [T1]

### Key Line Summary

| TP-1 Line | Description | Source |
|-----------|-------------|--------|
| Line 199 | Total income | Quebec calculation (similar to federal line 15000) |
| Line 275 | Net income | After deductions |
| Line 299 | Taxable income | After additional deductions |
| Line 401 | Gross Quebec tax | Step 1 computation |
| Line 413 | Quebec non-refundable credits | Step 2 |
| Line 430 | Net Quebec tax | Line 401 - line 413, min 0 |
| Schedule E | QPP contributions | Step 3 |
| Schedule F | QPIP premiums | Step 4 |
| Line 448 | QHSF contribution | Step 5 |
| Line 450 | Quebec tax payable | Final amount |

---

## Step 9: Edge Cases and Special Rules

### 9a. Quebec vs. Federal Income Differences [T1]

Quebec taxable income may differ from federal taxable income because:
- Quebec has different deduction rules (e.g., stock option deductions, capital gains inclusion)
- The TP-80 (self-employment) may produce different results than T2125 due to Quebec-specific rules
- **Always compute Quebec income independently** -- do not simply copy federal amounts

### 9b. Part-Year Quebec Resident [T3]

- If moved into or out of Quebec during the year, **ESCALATE**
- Part-year Quebec residents may need to file returns in both provinces
- Quebec has specific rules for income allocation on move

### 9c. Interprovincial Self-Employment [T2]

- If business has a permanent establishment in another province, Quebec tax may be allocated
- **FLAG for reviewer** if client has out-of-province business operations

### 9d. Quebec Stock Savings Plan (QSSP) Deduction [T3]

- Rarely used; **ESCALATE** if client asks

### 9e. QPP vs. CPP Interaction [T1]

- Quebec residents ALWAYS contribute to QPP, never to CPP
- If client has employment income from outside Quebec (with CPP deductions on T4), adjustments are needed
- **FLAG for reviewer** if client has both QPP and CPP contributions in the same year

### 9f. EI Premiums for Quebec Residents [T1]

- Quebec residents pay **reduced EI premiums** (no maternity/parental component, covered by QPIP)
- 2025 Quebec EI rate: 1.31% (vs. 1.64% outside Quebec) on employment income
- Self-employed Quebec residents who opt into EI special benefits pay the employee rate only

---

## Step 10: Prohibitions

1. **DO NOT** file or sign any return. This skill produces working papers only.
2. **DO NOT** apply this skill if province of residence on December 31 is not Quebec.
3. **DO NOT** compute tax for corporations, partnerships, or trusts.
4. **DO NOT** use CPP rates for Quebec residents -- always use QPP rates.
5. **DO NOT** copy federal taxable income to Quebec taxable income without verification.
6. **DO NOT** forget the QHSF contribution -- it is a significant additional cost.
7. **DO NOT** forget the Quebec abatement on the federal return.
8. **DO NOT** combine this skill with another provincial skill for the same return year.
9. **DO NOT** provide legal advice on residency disputes.
10. **DO NOT** use prior-year bracket amounts -- always confirm 2025 indexed thresholds.

---

## Step 11: Test Suite

### Test 1 -- Low Income, Single [T1]

| Input | Value |
|-------|-------|
| Quebec taxable income | $30,000 |
| Net self-employment income | $30,000 |
| Status | Single |

**Expected:**
- Gross Quebec tax: $30,000 x 14% = $4,200.00
- Quebec basic personal credit: $18,056 x 14% = $2,527.84
- Net Quebec tax: $4,200.00 - $2,527.84 = $1,672.16
- QPP: ($30,000 - $3,500) x 12.80% = $26,500 x 12.80% = $3,392.00
- QPIP: $30,000 x 0.878% = $263.40
- QHSF: graduated rate (income between $16,780 and $59,885)
  - QHSF = ($30,000 - $16,780) x ($30,000 x 1%) / ($59,885 - $16,780)
  - QHSF = $13,220 x $300 / $43,105 = **$92.02** (approx.)
- Total Quebec taxes and contributions: $1,672.16 + $3,392.00 + $263.40 + $92.02 = **$5,419.58**

### Test 2 -- Mid-Range Income [T1]

| Input | Value |
|-------|-------|
| Quebec taxable income | $80,000 |
| Net self-employment income | $80,000 |
| Status | Single |

**Expected:**
- First $53,255 at 14% = $7,455.70
- $80,000 - $53,255 = $26,745 at 19% = $5,081.55
- Gross Quebec tax: $7,455.70 + $5,081.55 = $12,537.25
- Quebec basic personal credit: $2,527.84
- Net Quebec tax: $12,537.25 - $2,527.84 = $10,009.41
- QPP: max = $8,678.40 (income > $71,300)
- QPP2: ($80,000 - $71,300) x 8.00% = $8,700 x 8.00% = $696.00
- QPIP: $80,000 x 0.878% = $702.40
- QHSF: $80,000 x 1% = $800.00
- Total: $10,009.41 + $8,678.40 + $696.00 + $702.40 + $800.00 = **$20,886.21**

### Test 3 -- High Income, Top Bracket [T1]

| Input | Value |
|-------|-------|
| Quebec taxable income | $200,000 |
| Net self-employment income | $200,000 |
| Status | Single |

**Expected:**
- First $53,255 at 14% = $7,455.70
- $53,256 -- $106,495: $53,240 at 19% = $10,115.60
- $106,496 -- $129,590: $23,095 at 24% = $5,542.80
- $129,591 -- $200,000: $70,410 at 25.75% = $18,130.58
- Gross Quebec tax: $7,455.70 + $10,115.60 + $5,542.80 + $18,130.58 = $41,244.68
- Quebec basic personal credit: $2,527.84
- Net Quebec tax: $41,244.68 - $2,527.84 = $38,716.84
- QPP: max = $8,678.40
- QPP2: max = $792.00
- QPIP: max = $860.44
- QHSF: $200,000 x 1% = $2,000.00
- Total: $38,716.84 + $8,678.40 + $792.00 + $860.44 + $2,000.00 = **$51,047.68**

### Test 4 -- Below Basic Personal Amount [T1]

| Input | Value |
|-------|-------|
| Quebec taxable income | $15,000 |
| Net self-employment income | $15,000 |
| Status | Single |

**Expected:**
- Gross Quebec tax: $15,000 x 14% = $2,100.00
- Quebec basic personal credit: $2,527.84
- Net Quebec tax: $0 (cannot go below zero)
- QPP: ($15,000 - $3,500) x 12.80% = $1,472.00
- QPIP: $15,000 x 0.878% = $131.70
- QHSF: $0 (income < $16,780)
- Total: $0 + $1,472.00 + $131.70 + $0 = **$1,603.70** (QPP/QPIP still owing)

---

## Step 12: Self-Checks

Before delivering output, verify:

- [ ] Province of residence on December 31 is confirmed as Quebec
- [ ] Quebec taxable income computed independently from federal (not simply copied)
- [ ] All 4 Quebec bracket rates applied correctly with 2025 indexed thresholds
- [ ] Basic personal amount uses 2025 indexed figure ($18,056)
- [ ] QPP rates used (NOT CPP rates)
- [ ] QPIP premium computed at 0.878% self-employed rate
- [ ] QHSF contribution computed using graduated formula
- [ ] Quebec abatement noted on federal return (16.5%)
- [ ] Non-refundable credits multiplied at 14% (lowest Quebec rate)
- [ ] Quebec tax payable is zero or positive
- [ ] Part-year / multi-province situations flagged for reviewer
- [ ] Output traces to source documents

---

## Section 13 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
