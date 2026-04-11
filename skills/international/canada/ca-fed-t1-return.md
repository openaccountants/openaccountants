---
name: ca-fed-t1-return
description: >
  Use this skill whenever asked about a Canadian federal T1 General individual income tax return for a self-employed sole proprietor. Trigger on phrases like "T1 return", "personal tax Canada", "federal tax brackets", "basic personal amount", "CPP self-employed", "CPP2", "self-employment tax Canada", "net income", "taxable income", "federal tax calculation", "non-refundable credits", "instalment payments", or any question about computing federal tax owing for a self-employed individual in Canada. Covers federal tax brackets, BPA, CPP/CPP2 at double rate, optional EI, net income and taxable income computation, non-refundable credits, and balance owing/refund. ALWAYS read this skill before touching any T1 return work for self-employed clients.
version: 1.0
jurisdiction: CA-FED
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
  - ca-fed-t2125
---

# Canada T1 General Individual Return -- Self-Employed Sole Proprietor Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Canada -- Federal |
| Jurisdiction Code | CA-FED |
| Primary Legislation | Income Tax Act (ITA), R.S.C. 1985, c. 1 (5th Supp.) |
| Supporting Legislation | Canada Pension Plan (CPP) Act; Employment Insurance Act; Income Tax Regulations (ITR) |
| Tax Authority | Canada Revenue Agency (CRA) |
| Filing Portal | CRA My Account / NETFILE / EFILE |
| Form | T1 General -- Income Tax and Benefit Return |
| Supporting Schedules | Schedule 1 (Federal Tax), Schedule 8 (CPP contributions on self-employment), Schedule 13 (EI premiums on self-employment), T2125 |
| Contributor | Open Accountants Community |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: bracket application, BPA, CPP/CPP2 computation, filing deadlines, basic non-refundable credits. Tier 2: income from multiple sources, pension splitting, medical expenses, charitable donations. Tier 3: non-resident returns, part-year resident, bankruptcy, deceased returns, trust income. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. CPA/CA must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any federal tax figure, you MUST know:

1. **Full legal name and SIN** [T1] -- Social Insurance Number required for filing
2. **Date of birth** [T1] -- affects age-based credits (age amount, pension income splitting)
3. **Marital status as of December 31** [T1] -- single, married, common-law, widowed, divorced, separated
4. **Province/territory of residence on December 31** [T1] -- determines provincial tax (out of scope for this skill but required on T1)
5. **Net self-employment income** [T1] -- from T2125 (ca-fed-t2125 skill)
6. **Other income sources** [T1/T2] -- employment (T4), investment, rental, pensions, EI benefits, etc.
7. **Deductions claimed** [T1/T2] -- RRSP, professional dues, childcare, moving expenses, etc.
8. **Non-refundable credits** [T1/T2] -- medical, charitable, tuition, disability, etc.
9. **Tax instalments paid during the year** [T1] -- quarterly amounts remitted
10. **Tax withheld at source** [T1] -- from T4 slips, T4A, T3, etc.
11. **CPP/EI elections** [T1] -- has the self-employed individual opted into EI special benefits?
12. **Prior year tax data** [T1] -- for instalment calculations and carryforward amounts

**If province of residence is unknown, STOP. Province determines provincial tax and surtaxes.**

---

## Step 1: Federal Tax Brackets -- 2025 [T1]

**Legislation:** ITA s. 117(2)

### 2025 Federal Income Tax Rates

| Taxable Income (CAD) | Marginal Rate | Cumulative Tax at Top of Bracket |
|----------------------|---------------|----------------------------------|
| $0 -- $57,375 | 14.5%* | $8,319 |
| $57,376 -- $114,750 | 20.5% | $8,319 + $11,762 = $20,081 |
| $114,751 -- $177,882 | 26% | $20,081 + $16,414 = $36,495 |
| $177,883 -- $253,414 | 29% | $36,495 + $21,904 = $58,399 |
| $253,415 + | 33% | $58,399 + ... |

*The 14.5% rate for 2025 is a blended rate. The federal government reduced the lowest bracket rate from 15% to 14% effective July 1, 2025. For the full calendar year 2025, the effective rate on the first bracket is 14.5% (15% x 6/12 + 14% x 6/12).

**Note:** These brackets are indexed annually for inflation using the CPI adjustment factor.

### How to Apply [T1]

1. Start with **taxable income** (line 26000 of the T1)
2. Apply each marginal rate to the portion of income within each bracket
3. Sum to get **basic federal tax** (Schedule 1, line 31)
4. Subtract non-refundable credits (converted to 14.5% for 2025) to get **net federal tax**

---

## Step 2: Basic Personal Amount (BPA) -- 2025 [T1]

**Legislation:** ITA s. 118(1)(c); ITA s. 117.1

| Net Income Level | BPA Claimable |
|------------------|---------------|
| $177,882 or less | $16,129 (maximum) |
| Between $177,882 and $253,414 | Graduated reduction from $16,129 down to $14,538 |
| $253,414 or more | $14,538 (base amount) |

### BPA Calculation for Income Between $177,882 and $253,414 [T1]

BPA = $16,129 - ($16,129 - $14,538) x (Net income - $177,882) / ($253,414 - $177,882)

BPA = $16,129 - $1,591 x (Net income - $177,882) / $75,532

### Tax Credit Value [T1]

The BPA is a **non-refundable tax credit** at the lowest marginal rate:

BPA credit = BPA x 14.5% = up to $16,129 x 14.5% = **$2,339** (maximum for 2025)

---

## Step 3: CPP Contributions -- Self-Employed (Schedule 8) [T1]

**Legislation:** Canada Pension Plan Act, s. 10; CPP Regulations

### CPP Base Contributions (2025) [T1]

| Item | Amount |
|------|--------|
| Year's Maximum Pensionable Earnings (YMPE) | $71,300 |
| Year's Basic Exemption | $3,500 |
| Maximum contributory earnings (YMPE - exemption) | $67,800 |
| Employee rate | 5.95% |
| Self-employed rate (double -- employee + employer) | **11.90%** |
| Maximum self-employed CPP contribution | $67,800 x 11.90% = **$8,068.20** |

### CPP2 -- Second Additional CPP (2025) [T1]

| Item | Amount |
|------|--------|
| Year's Additional Maximum Pensionable Earnings (YAMPE) | $81,200 |
| CPP2 earnings range | $71,300 to $81,200 = $9,900 |
| Employee CPP2 rate | 4.00% |
| Self-employed CPP2 rate (double) | **8.00%** |
| Maximum self-employed CPP2 contribution | $9,900 x 8.00% = **$792.00** |

### CPP Computation for Self-Employed [T1]

1. **Pensionable self-employment earnings** = net self-employment income from T2125 (line 13500 or 13700)
2. If earnings < $3,500: no CPP required
3. If earnings >= $3,500 and <= $71,300: CPP = (earnings - $3,500) x 11.90%
4. If earnings > $71,300: CPP = $67,800 x 11.90% = $8,068.20 (maximum)
5. **CPP2:** if earnings > $71,300 and <= $81,200: CPP2 = (earnings - $71,300) x 8.00%
6. If earnings > $81,200: CPP2 = $9,900 x 8.00% = $792.00 (maximum)
7. **Total CPP + CPP2** = up to $8,068.20 + $792.00 = **$8,860.20**

### Tax Treatment of Self-Employed CPP [T1]

| Portion | Treatment | Where on T1 |
|---------|-----------|-------------|
| 50% of CPP/CPP2 (the "employee" half) | Non-refundable tax credit at 14.5% | Schedule 1, line 30800 / 30900 |
| 50% of CPP/CPP2 (the "employer" half) | Deduction from net income | T1 line 22200 |

This means the self-employed person gets:
- A **deduction** for half (reduces net income and therefore taxable income)
- A **credit** for the other half (reduces tax payable at the lowest rate)

### Schedule 8 [T1]

Self-employed CPP contributions are computed on **Schedule 8** (CPP Contributions on Self-Employment and Other Earnings) and flow to:
- T1 line 22200 (deduction for employer-equivalent portion)
- Schedule 1 line 30800 (credit for employee-equivalent portion)

---

## Step 4: Employment Insurance -- Self-Employed (Optional) [T1]

**Legislation:** Employment Insurance Act, Part VII.1

### Key Rules [T1]

| Item | Detail |
|------|--------|
| Mandatory? | **NO.** EI is voluntary for self-employed individuals. |
| What it covers | Special benefits only: maternity, parental, sickness, compassionate care, family caregiver |
| What it does NOT cover | Regular EI benefits (you cannot collect regular EI as self-employed) |
| Premium rate (2025, outside Quebec) | $1.64 per $100 of self-employment earnings |
| Maximum insurable earnings (2025) | $65,700 |
| Maximum annual premium (2025) | **$1,077.48** |
| Quebec rate (2025) | $1.30 per $100 (lower because QPIP covers parental) |
| When premiums are paid | Annually with the T1 return (Schedule 13) |
| Waiting period | 12 months after registering before eligible for benefits |
| Opt-out | Once you have collected benefits, you cannot opt out. If you have never collected, you can stop at any time. |

### Tax Treatment [T1]

EI premiums paid by self-employed individuals are a **non-refundable tax credit** at the lowest rate (14.5% for 2025) on Schedule 1.

**Self-employed do NOT pay the employer portion of EI** (unlike CPP where they pay double).

---

## Step 5: T1 Income Computation -- Total Income to Taxable Income [T1]

**Legislation:** ITA s. 3 (income computation); ITA s. 2(1) (taxable income)

### Line-by-Line Structure

| T1 Line | Description | Source |
|---------|-------------|--------|
| **Total Income** | | |
| 10100 | Employment income | T4 slips |
| 10400 | Other employment income | T4A, tips, etc. |
| 11500 | Old Age Security pension | T4A(OAS) |
| 11300 | Pension income | T4A |
| 12000 | Taxable dividends | T5, T3 |
| 12100 | Interest income | T5, T3 |
| 12700 | Taxable capital gains (50% inclusion) | Schedule 3 |
| 13000 | Other income | Various |
| 13500 | **Self-employment business income** | **T2125** |
| 13700 | Professional income | T2125 |
| 13900 | Commission income | T2125 |
| 14100 | Farming income | T2042 |
| 14300 | Fishing income | T2121 |
| 14700 | Workers' compensation | T5007 |
| 14500 | Social assistance | |
| 15000 | **Total income** | Sum of all above |

| T1 Line | Description | |
|---------|-------------|---|
| **Net Income** | | |
| 20700 | RPP deduction | |
| 20800 | RRSP deduction | |
| 21000 | Deduction for elected split-pension | |
| 21200 | Annual union, professional, or like dues | |
| 21400 | Child care expenses | |
| 21500 | Disability supports deduction | |
| 21700 | Business investment loss | |
| 21900 | Moving expenses | |
| 22000 | Support payments made | |
| 22100 | Carrying charges and interest expenses | |
| 22200 | **CPP/CPP2 on self-employment (employer half)** | **Schedule 8** |
| 22215 | CPP2 contributions on self-employment | Schedule 8 |
| 22900 | Other employment expenses | T777 |
| 23100 | Clergy residence deduction | |
| 23200 | Other deductions | |
| 23400 | Net business income (if loss, may create negative net income) | |
| 23500 | Social benefits repayment | |
| 23600 | **Net income** | Total income minus deductions |

| T1 Line | Description | |
|---------|-------------|---|
| **Taxable Income** | | |
| 24400 | Canadian Armed Forces personnel deductions | |
| 24900 | Security options deductions | |
| 25000 | Other payments deduction | |
| 25100 | Limited partnership losses of other years | |
| 25200 | Non-capital losses of other years | |
| 25300 | Net capital losses of other years | |
| 25400 | Capital gains deduction | |
| 25500 | Northern residents deductions | |
| 25600 | Additional deductions | |
| 26000 | **Taxable income** | Net income minus line 24400-25600 |

---

## Step 6: Federal Tax Computation (Schedule 1) [T1]

**Legislation:** ITA s. 117(2), s. 118-118.95 (credits)

### Computation Steps

| Step | Description | Schedule 1 Line |
|------|-------------|-----------------|
| 1 | Apply tax brackets to taxable income (line 26000) | Line 31 |
| 2 | Subtract non-refundable credits (see Step 7) | Lines 33500-35000 |
| 3 | = Basic federal tax | Line 35000 |
| 4 | Add: federal dividend tax credit recovery (if applicable) | |
| 5 | Subtract: federal dividend tax credit | Line 40425 |
| 6 | Subtract: federal foreign tax credit | |
| 7 | Subtract: federal political contribution tax credit | |
| 8 | Subtract: investment tax credit | |
| 9 | Subtract: labour-sponsored fund tax credit | |
| 10 | = **Net federal tax** | Line 42000 |

---

## Step 7: Non-Refundable Credits (Schedule 1) [T1]

**Legislation:** ITA s. 118-118.95

All non-refundable credits are converted to a credit at the **lowest marginal rate (14.5% for 2025)** unless otherwise specified.

### Common Non-Refundable Credits for Self-Employed

| Credit | 2025 Amount/Limit | T1/Schedule 1 Line | Notes |
|--------|-------------------|---------------------|-------|
| Basic personal amount | Up to $16,129 | 30000 | See Step 2 for income-based reduction |
| CPP contributions (employee portion) | Up to $4,034.10 | 30800 | Half of self-employed CPP |
| CPP2 contributions (employee portion) | Up to $396.00 | 30900 | Half of self-employed CPP2 |
| EI premiums (self-employed, if opted in) | Up to $1,077.48 | 31200 | Voluntary |
| Canada employment amount | $1,368 | 31260 | NOT available to self-employed (employment income only) |
| Age amount (65+) | $8,790 (reduced if income > $44,325) | 30100 | |
| Spouse/common-law partner amount | Up to $16,129 minus spouse's net income | 30300 | |
| Eligible dependant amount | Up to $16,129 minus dependant's net income | 30400 | |
| Canada caregiver amount | Up to $8,375 | 30425-30500 | |
| Disability amount (for self) | $9,872 | 31600 | Requires T2201 certification |
| Tuition (Schedule 11) | Actual tuition paid | 32300 | |
| Medical expenses | Amounts > lesser of 3% of net income or $2,759 | 33099 | |
| Charitable donations | 15% on first $200 + 29%/33% on excess | 34900 | 33% rate on income above $253,414 |
| Home accessibility tax credit | 15% on up to $20,000 of eligible expenses | | For qualifying individuals |

### Credits NOT Available to Self-Employed [T1]

| Credit | Reason |
|--------|--------|
| Canada employment amount ($1,368) | Only for employment income (T4), not self-employment income |
| EI premiums (unless opted in) | Self-employed EI is voluntary |

---

## Step 8: Net Income, Taxable Income, and Federal Tax -- Full Computation [T1]

### Worked Example Framework

```
TOTAL INCOME
  Self-employment income (T2125 line 13500)     $XX,XXX
  + Other income (employment, investment, etc.)  $XX,XXX
  = Total income (line 15000)                    $XX,XXX

NET INCOME
  - RRSP deduction                               ($X,XXX)
  - CPP employer-half deduction (line 22200)     ($X,XXX)
  - CPP2 employer-half deduction (line 22215)    ($XXX)
  - Other deductions                             ($X,XXX)
  = Net income (line 23600)                      $XX,XXX

TAXABLE INCOME
  - Loss carryovers, capital gains deduction     ($X,XXX)
  = Taxable income (line 26000)                  $XX,XXX

FEDERAL TAX (Schedule 1)
  Tax on taxable income per brackets             $XX,XXX
  - Non-refundable credits x 14.5%              ($X,XXX)
  = Basic federal tax                            $XX,XXX
  - Dividend tax credit, foreign tax credit      ($XXX)
  = Net federal tax (line 42000)                 $XX,XXX

AMOUNTS OWING / REFUND
  Net federal tax                                $XX,XXX
  + Provincial tax (separate calculation)        $XX,XXX
  + CPP payable on self-employment (Schedule 8)  $XX,XXX
  + CPP2 payable on self-employment              $XXX
  + EI payable on self-employment (if opted in)  $X,XXX
  + Social benefits repayment (if applicable)    $XXX
  = Total payable                                $XX,XXX
  - Tax deducted at source (T4 slips)           ($X,XXX)
  - Instalments paid                            ($X,XXX)
  - Provincial credits                          ($XXX)
  - Other credits (GST/HST credit, CCB, etc.)   ($XXX)
  = Balance owing / (refund)                     $XX,XXX
```

---

## Step 9: Instalment Requirements [T1]

**Legislation:** ITA s. 156(1); ITA s. 156.1(2)

### When Instalments Are Required [T1]

| Condition | Instalments Required? |
|-----------|-----------------------|
| Net tax owing > $3,000 in current year AND in either of the two prior years | YES |
| Net tax owing <= $3,000 in current year OR in both prior years | NO |
| Quebec residents | Threshold is $1,800 for federal (different for provincial) |

"Net tax owing" = total tax payable minus tax withheld at source. For self-employed individuals with no employer withholding, this almost always exceeds $3,000.

### Instalment Due Dates [T1]

| Instalment | Due Date |
|------------|----------|
| 1st quarter | March 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | December 15 |

### Instalment Calculation Methods [T1]

| Method | How It Works |
|--------|--------------|
| No-calculation option | CRA sends instalment reminders based on prior year(s) |
| Prior-year method | Each instalment = 1/4 of prior year's net tax owing |
| Current-year method | Each instalment = 1/4 of estimated current year net tax owing |

### Instalment Interest [T1]

CRA charges instalment interest on late or insufficient instalments at the prescribed rate (compounded daily). Interest is offset if later instalments are overpaid.

---

## Step 10: Filing Deadlines [T1]

**Legislation:** ITA s. 150(1)(d); ITA s. 156.1

| Item | Deadline |
|------|----------|
| T1 filing deadline (self-employed or spouse/partner of self-employed) | **June 15** of the following year |
| Payment deadline (balance owing) | **April 30** of the following year |
| Penalty for late filing | 5% of balance owing + 1% per complete month late (max 12 months) |
| Repeated late filing (2nd+ in 3 years) | 10% of balance owing + 2% per complete month late (max 20 months) |
| Interest on unpaid balance | Prescribed rate, compounded daily, starting **May 1** |

**CRITICAL:** Self-employed filers have until June 15 to file, but any balance owing accrues interest from **April 30**. Pay by April 30 to avoid interest even if the return is filed later.

---

## Step 11: Edge Case Registry

### EC1 -- CPP on multiple income sources [T1]
**Situation:** Self-employed person also has T4 employment income. Employer already deducted CPP on $50,000 of employment earnings.
**Resolution:** Total CPP contributions cannot exceed the annual maximum. Schedule 8 computes the remaining CPP owing on self-employment earnings after accounting for CPP already paid through employment. The combined pensionable earnings are capped at YMPE ($71,300).

### EC2 -- Self-employed person under 18 or over 70 [T1]
**Situation:** Self-employed individual is 72 years old.
**Resolution:** CPP contributions are optional for individuals aged 65-70 (election on Schedule 8). After age 70, no CPP contributions are required or permitted. CPP2 follows the same age rules.

### EC3 -- BPA reduction for high earners [T1]
**Situation:** Self-employed person has net income of $210,000.
**Resolution:** BPA = $16,129 - $1,591 x ($210,000 - $177,882) / $75,532 = $16,129 - $1,591 x 0.4249 = $16,129 - $676 = $15,453. Credit = $15,453 x 14.5% = $2,241.

### EC4 -- Business loss offsets other income [T1]
**Situation:** Self-employment loss of ($15,000). Employment income of $60,000.
**Resolution:** Business loss offsets employment income. Net income = $60,000 - $15,000 = $45,000. CPP on self-employment = $0 (no positive self-employment earnings). The loss may also be carried back 3 years or forward 20 years if there is no other income to offset.

### EC5 -- Instalment interest charged [T1]
**Situation:** Self-employed person paid no instalments during the year. Prior year tax owing was $12,000. Current year balance owing is $15,000.
**Resolution:** CRA will charge instalment interest on four missed payments of approximately $3,000 each (prior-year method). Interest runs from each missed instalment date to April 30 of the following year at the prescribed rate.

### EC6 -- EI opt-in timing [T1]
**Situation:** Self-employed person wants to opt into EI and immediately claim sickness benefits.
**Resolution:** NOT allowed. There is a 12-month waiting period after registering for EI special benefits before any claim can be made. Premiums paid during the waiting period are non-refundable if benefits are never claimed.

### EC7 -- Quick Method GST/HST and the T1 [T1]
**Situation:** Self-employed person uses Quick Method. The Quick Method benefit (difference between GST collected and amount remitted) was $1,200.
**Resolution:** The $1,200 Quick Method benefit is included in business income on T2125 (line 8290) and flows to T1 line 13500. It is fully taxable.

### EC8 -- RRSP deduction room for self-employed [T1]
**Situation:** Self-employed person wants to know maximum RRSP contribution.
**Resolution:** RRSP deduction limit = 18% of prior year's earned income, up to the annual RRSP dollar limit ($32,490 for 2025, based on 2024 earned income). Earned income includes net self-employment income (T2125) minus the CPP employer-half deduction. Unused room carries forward.

### EC9 -- CPP2 on self-employment earnings between YMPE and YAMPE [T1]
**Situation:** Self-employed net income is $78,000.
**Resolution:** Base CPP = ($71,300 - $3,500) x 11.90% = $8,068.20. CPP2 = ($78,000 - $71,300) x 8.00% = $6,700 x 8.00% = $536.00. Total CPP + CPP2 = $8,604.20. Half deducted from net income ($4,302.10), half as non-refundable credit.

### EC10 -- Late filing penalty with no balance owing [T1]
**Situation:** Self-employed person files on September 30 (late) but is owed a refund.
**Resolution:** No late-filing penalty applies because the penalty is calculated on balance owing, which is $0 or negative. However, the refund is delayed. Interest on refunds begins 30 days after the later of the filing deadline or the date the return is filed.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: CPA/CA must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to CPA/CA. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard self-employed, single income source
**Input:** Sole proprietor, net business income (from T2125) = $85,000. No other income. RRSP deduction = $10,000. No dependants. Province: Ontario (provincial tax out of scope). No EI opt-in.
**Expected:**
- Total income = $85,000
- CPP (base): ($71,300 - $3,500) x 11.90% = $8,068.20
- CPP2: ($81,200 - $71,300) x 8.00% = but earnings $85,000 > YAMPE, so CPP2 = $9,900 x 8.00% = $792.00
- Wait: earnings $85,000 > $81,200, so CPP2 = $792.00 max
- CPP employer-half deduction: ($8,068.20 + $792.00) / 2 = $4,430.10
- Net income = $85,000 - $10,000 (RRSP) - $4,430.10 = $70,569.90
- Taxable income = $70,569.90
- Federal tax: $57,375 x 14.5% = $8,319.38 + ($70,569.90 - $57,375) x 20.5% = $8,319.38 + $2,704.95 = $11,024.33
- BPA credit: $16,129 x 14.5% = $2,338.71
- CPP employee-half credit: $4,430.10 x 14.5% = $642.36
- Total credits = $2,338.71 + $642.36 = $2,981.07
- Basic federal tax = $11,024.33 - $2,981.07 = $8,043.26
- CPP payable (Schedule 8) = $8,860.20 (added to T1 as payable, not as tax)
- Balance: federal tax $8,043.26 + CPP $8,860.20 = $16,903.46 (before provincial tax and instalments)

### Test 2 -- Low-income self-employed, below BPA
**Input:** Sole proprietor, net business income = $14,000. No other income. No RRSP.
**Expected:**
- Total income = $14,000
- CPP: ($14,000 - $3,500) x 11.90% = $1,249.50
- CPP2: $0 (earnings below YMPE)
- CPP employer-half deduction: $624.75
- Net income = $14,000 - $624.75 = $13,375.25
- Taxable income = $13,375.25
- Federal tax: $13,375.25 x 14.5% = $1,939.41
- BPA credit: $16,129 x 14.5% = $2,338.71
- CPP employee-half credit: $624.75 x 14.5% = $90.59
- Total credits = $2,429.30
- Basic federal tax = $1,939.41 - $2,429.30 = **negative** = $0 (credits exceed tax; no refund of non-refundable credits)
- CPP payable = $1,249.50
- Balance: $0 federal tax + $1,249.50 CPP = $1,249.50

### Test 3 -- High-income self-employed, top bracket
**Input:** Sole proprietor, net business income = $300,000. RRSP = $32,490 (max). No other income.
**Expected:**
- Total income = $300,000
- CPP: $8,068.20 (max). CPP2: $792.00 (max). Total = $8,860.20
- CPP employer-half deduction: $4,430.10
- Net income = $300,000 - $32,490 - $4,430.10 = $263,079.90
- Taxable income = $263,079.90
- Federal tax: $8,319 + $11,762 + $16,414 + $21,904 + ($263,079.90 - $253,414) x 33% = $58,399 + $3,189.75 = $61,588.75
- BPA: net income $263,079.90 > $253,414, so BPA = $14,538. Credit = $14,538 x 14.5% = $2,108.01
- CPP employee-half credit: $4,430.10 x 14.5% = $642.36
- Total credits = $2,750.37
- Basic federal tax = $61,588.75 - $2,750.37 = $58,838.38
- Charitable: 33% rate applies on donations to extent income > $253,414

### Test 4 -- Self-employed with employment income and CPP overlap
**Input:** Employment income $55,000 (CPP deducted by employer: $55,000 - $3,500 = $51,500 x 5.95% = $3,064.25 employee portion). Self-employment income $30,000.
**Expected:**
- Remaining pensionable earnings for CPP: $71,300 - $55,000 = $16,300
- Self-employed CPP on remaining: $16,300 x 11.90% = $1,939.70
- CPP2: ($81,200 - $71,300) = $9,900, but total earnings = $85,000 > $81,200, so CPP2 = $9,900 x 8.00% = $792.00 -- but must check if any CPP2 was paid through employment. If employer deducted CPP2 on $55,000 (no -- CPP2 only applies above YMPE $71,300, and employment was $55,000 < YMPE), so full CPP2 = $792.00 on self-employment.
- Schedule 8 handles the integration automatically.

### Test 5 -- Late filing penalty
**Input:** Self-employed, balance owing $8,000, filed 3 months late (September 30 instead of June 15).
**Expected:** Penalty = 5% x $8,000 + 1% x $8,000 x 3 months = $400 + $240 = $640. Plus interest on $8,000 from May 1 at prescribed rate.

---

## PROHIBITIONS

- NEVER apply tax brackets without first computing net income and taxable income through all deduction steps
- NEVER forget the CPP employer-half deduction from net income (line 22200) -- it reduces taxable income
- NEVER apply the Canada employment amount ($1,368) credit to self-employment income -- it is for T4 employment income only
- NEVER treat EI as mandatory for self-employed -- it is optional
- NEVER compute provincial tax in this skill -- provincial tax is separate and depends on province of residence
- NEVER assume the BPA is always $16,129 -- it reduces for high-income earners above $177,882
- NEVER allow home office expenses from T2125 to create a business loss
- NEVER present tax calculations as final -- always label as estimated and direct client to their CPA/CA for sign-off
- NEVER omit CPP2 for self-employment earnings above YMPE ($71,300) -- CPP2 is mandatory as of 2024
- NEVER forget that the payment deadline is April 30 even though the filing deadline is June 15
- NEVER skip checking instalment requirements -- most self-employed individuals owe instalments

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
