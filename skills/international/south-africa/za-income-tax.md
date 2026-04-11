---
name: za-income-tax
description: Use this skill whenever asked about South African income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay", "ITR12", "income tax return", "SARS", "tax brackets", "provisional tax", "IRP6", "rebates", "medical credits", "retirement deduction", "turnover tax", "eFiling", or any question about filing or computing income tax for a self-employed or sole proprietor client in South Africa. This skill covers progressive rates (18-45%), rebates (primary/secondary/tertiary), medical tax credits, retirement fund deductions, provisional tax (IRP6), turnover tax for micro businesses, penalties, and interaction with VAT. ALWAYS read this skill before touching any South African income tax work.
---

# South Africa Income Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | South Africa |
| Jurisdiction Code | ZA |
| Primary Legislation | Income Tax Act 58 of 1962 |
| Supporting Legislation | Tax Administration Act 28 of 2011; Sixth Schedule (Turnover Tax); Fourth Schedule (Provisional Tax) |
| Tax Authority | South African Revenue Service (SARS) |
| Filing Portal | SARS eFiling (www.sarsefiling.co.za) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a South African registered tax practitioner |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, rebate amounts, medical credit rates, provisional tax schedule, turnover tax eligibility. Tier 2: retirement fund deduction optimisation, mixed-use expense apportionment, home office claims, travel allowance. Tier 3: foreign income exemption (s10(1)(o)(ii)), capital gains tax, trusts, emigration. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified tax practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Age at end of tax year (28 Feb)** [T1] -- determines which rebate(s) apply (primary, secondary 65+, tertiary 75+)
2. **Residency status** [T1] -- resident vs non-resident; this skill covers residents only
3. **Gross self-employment income** [T1] -- total turnover from trade
4. **Business expenses** [T1/T2] -- nature and amount (T2 for mixed-use items like vehicle, home office)
5. **Retirement fund contributions** [T1] -- RA or pension contributions paid during the year
6. **Medical scheme contributions** [T1] -- monthly medical aid contributions and number of dependants
7. **Out-of-pocket medical expenses** [T2] -- qualifying additional medical expenses (for over-65 or disability)
8. **Provisional tax payments** [T1] -- IRP6 amounts paid during the year
9. **Other income** [T1] -- employment, rental, interest, dividends, capital gains
10. **Turnover tax election** [T1] -- whether the client has elected turnover tax under the Sixth Schedule

**If age is unknown, STOP. Age determines rebates and tax threshold. Age is mandatory.**

---

## Step 1: Determine Applicable Rate Table [T1]

**Legislation:** Income Tax Act 58 of 1962, rates schedule (2025/2026 year of assessment: 1 March 2025 -- 28 February 2026)

### Progressive Tax Table (All Individuals)

| Taxable Income (ZAR) | Rate | Cumulative Tax at Top |
|----------------------|------|-----------------------|
| 1 -- 237,100 | 18% | R42,678 |
| 237,101 -- 370,500 | R42,678 + 26% above R237,100 | R77,362 |
| 370,501 -- 512,800 | R77,362 + 31% above R370,500 | R121,475 |
| 512,801 -- 673,000 | R121,475 + 36% above R512,800 | R179,147 |
| 673,001 -- 857,900 | R179,147 + 39% above R673,000 | R251,258 |
| 857,901 -- 1,817,000 | R251,258 + 41% above R857,900 | R644,489 |
| 1,817,001+ | R644,489 + 45% above R1,817,000 | -- |

**South Africa uses one rate table for all individuals regardless of marital status.**

### Tax Rebates [T1]

| Rebate | Amount (2025/2026) | Eligibility |
|--------|-------------------|-------------|
| Primary | R17,235 | All natural persons |
| Secondary | R9,444 | Age 65 and older at end of year of assessment |
| Tertiary | R3,145 | Age 75 and older at end of year of assessment |

### Tax Thresholds (Below These = No Tax) [T1]

| Age Group | Threshold |
|-----------|-----------|
| Below 65 | R95,750 |
| 65 to below 75 | R148,217 |
| 75 and above | R165,689 |

---

## Step 2: ITR12 Computation Structure [T1]

**Legislation:** Income Tax Act; Tax Administration Act

| Step | Description | How to Populate |
|------|-------------|-----------------|
| A | Gross income from trade | Total self-employment revenue (Code 3606 on ITR12) |
| B | Less: Allowable business deductions | Expenses passing the "in the production of income" test (s11(a)) |
| C | Net profit from trade | A minus B |
| D | Add: Other income | Employment, rental, interest, foreign income |
| E | Gross income | C plus D |
| F | Less: Exempt income | Interest exemption (R23,800 under 65; R34,500 65+) |
| G | Less: Retirement fund deduction | s11F deduction (see Step 4) |
| H | Taxable income | E minus F minus G |
| I | Normal tax per table | Apply rate table to H |
| J | Less: Rebates | Primary + Secondary (if 65+) + Tertiary (if 75+) |
| K | Less: Medical tax credits | s6A + s6B credits (see Step 5) |
| L | Less: Provisional tax paid | IRP6 payments (1st + 2nd + 3rd voluntary) |
| M | Tax due / (refund) | I minus J minus K minus L |

---

## Step 3: Allowable Deductions [T1/T2]

**Legislation:** Income Tax Act, s11(a) -- "in the production of income"

### The Test [T1]
An expense is deductible if it is incurred in the production of income, is not of a capital nature, and is laid out or expended for the purposes of trade. SARS applies the "trade" and "production of income" requirements strictly.

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated business premises) | T1 | Fully deductible |
| Professional indemnity insurance | T1 | Fully deductible |
| Accounting and audit fees | T1 | Fully deductible |
| Office supplies / stationery | T1 | Fully deductible |
| Software subscriptions (business) | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Professional body subscriptions | T1 | Fully deductible |
| Travel (business purpose, flights/hotels) | T1 | Fully deductible if wholly for business |
| Bad debts (previously included in income) | T2 | Flag for reviewer -- confirm debt is truly irrecoverable |
| Home office expenses | T2 | Only if dedicated room used regularly and exclusively for trade (s11(a) + IN 28) |
| Motor vehicle expenses | T2 | Business portion only -- logbook required |
| Phone / internet | T2 | Business use portion only |
| Wear-and-tear allowance (s11(e)) | T1 | Based on SARS Interpretation Note 47 useful life tables |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Entertainment (client meals) | s23(m) -- expressly disallowed for sole proprietors |
| Personal living expenses | Not in the production of income |
| Fines and penalties | Public policy; s23(o) |
| Income tax itself | Tax on income is not deductible |
| Capital expenditure | Through wear-and-tear / depreciation, not direct deduction |
| Drawings / personal withdrawals | Not an expense |
| Donations (claimed as deduction) | s18A -- only to approved PBOs, capped at 10% of taxable income |

### Home Office Rules [T2]

**Legislation:** s11(a) read with IN 28

- The room must be used **regularly and exclusively** for trade purposes
- For self-employed: a dedicated room in the dwelling qualifies
- Calculate proportion: room area / total home area (or room count method)
- Apply proportion to: rent/bond interest, electricity, cleaning, rates, insurance
- SARS IN 28 is strict -- dual-use rooms do not qualify
- [T2] Flag for reviewer to confirm room layout and exclusivity

### Motor Vehicle Rules [T2]

- Option 1: Actual costs x business % (requires detailed logbook per s8(1)(b))
- Option 2: SARS fixed cost table (Interpretation Note 14) -- simplified but may be less favourable
- Logbook must record each trip: date, destination, km, purpose
- [T2] Flag for reviewer to confirm business km percentage

---

## Step 4: Retirement Fund Deduction [T1]

**Legislation:** s11F of the Income Tax Act

| Rule | Detail |
|------|--------|
| Deduction rate | 27.5% of the greater of remuneration or taxable income (before s11F deduction) |
| Annual cap | R350,000 |
| Qualifying funds | Pension fund, provident fund, retirement annuity (RA) fund |
| Excess contributions | Carried forward to future years; or added to tax-free lump sum (R550,000) at retirement |

**For self-employed individuals, an RA is typically the vehicle used. Contributions to an RA are deductible up to 27.5% of taxable income, capped at R350,000 per year.**

---

## Step 5: Medical Tax Credits [T1]

**Legislation:** s6A (Medical Scheme Fees Tax Credit) and s6B (Additional Medical Expenses Tax Credit)

### s6A -- Medical Scheme Fees Tax Credit (2025/2026) [T1]

| Member | Monthly Credit |
|--------|---------------|
| Main member (taxpayer) | R364 |
| First dependant | R364 |
| Each additional dependant | R246 |

Annual credit = monthly credit x 12.

### s6B -- Additional Medical Expenses Tax Credit [T2]

- Available to taxpayers aged 65+, or taxpayers/dependants with a disability
- For under-65 without disability: excess medical expenses above 7.5% of taxable income x 25%
- [T2] Flag for reviewer -- s6B calculations are complex and depend on disability status

---

## Step 6: Provisional Tax (IRP6) [T1]

**Legislation:** Fourth Schedule to the Income Tax Act

### Instalment Schedule

| Instalment | Deadline | Amount |
|-----------|----------|--------|
| 1st (IRP6) | 31 August | 50% of estimated total tax for the year |
| 2nd (IRP6) | Last day of February (28/29 Feb) | Remaining estimated tax (top-up to 100%) |
| 3rd (voluntary) | 30 September (7 months after year-end) | Top-up payment to reduce interest; optional |

### Rules [T1]

- Based on **estimated** taxable income for the current year (unlike Malta which uses prior year)
- First provisional payment: estimate must be reasonable; SARS may impose penalties for under-estimation
- Second provisional payment: estimate must be within 90% of actual (for taxable income under R1M) or 80% (over R1M)
- Penalty for under-estimation: 20% of the difference between actual tax and estimated tax
- Interest on late/short payment: prescribed rate (currently around 10.75% per annum -- verify with SARS)
- Self-employed individuals who earn income not subject to PAYE must register as provisional taxpayers

---

## Step 7: Turnover Tax Option [T1]

**Legislation:** Sixth Schedule to the Income Tax Act

### Eligibility [T1]

| Condition | Requirement |
|-----------|-------------|
| Annual turnover | Not exceeding R1,000,000 |
| Entity type | Sole proprietor, partnership, company, close corporation, co-operative |
| Exclusions | Professional services (as defined), personal service providers, certain investment income |

### Turnover Tax Table (2025/2026) [T1]

| Turnover (ZAR) | Rate |
|----------------|------|
| 0 -- 335,000 | 0% |
| 335,001 -- 500,000 | 1% of amount above R335,000 |
| 500,001 -- 750,000 | R1,650 + 2% above R500,000 |
| 750,001 -- 1,000,000 | R6,650 + 3% above R750,000 |

### Key Points [T1]

- Replaces income tax, capital gains tax, dividends tax, and VAT (if turnover under R1M)
- Two interim payments + top-up with annual return (TT03)
- Cannot claim normal business deductions -- turnover tax replaces the income tax computation
- [T2] Flag for reviewer: confirm whether turnover tax is more favourable than normal tax after deductions

---

## Step 8: Filing and Deadlines [T1]

**Legislation:** Tax Administration Act 28 of 2011

| Filing / Payment | Deadline |
|-----------------|----------|
| ITR12 (non-provisional taxpayers, eFiling) | Late October (SARS announces exact dates annually) |
| ITR12 (provisional taxpayers, eFiling) | Late January of following year (SARS announces) |
| IRP6 1st provisional | 31 August |
| IRP6 2nd provisional | Last day of February |
| IRP6 3rd voluntary | 30 September |
| Turnover tax interim payments | August and February |
| Turnover tax annual (TT03) | Within 6 months of year-end |

### Filing Window [T1]

SARS opens the filing season annually, typically:
- Non-provisional: July to October/November
- Provisional: July to January
- All filing via eFiling (online) or SARS branch (by appointment)

---

## Step 9: Penalties [T1]

**Legislation:** Tax Administration Act, Chapter 15

| Offence | Penalty |
|---------|---------|
| Late filing (Admin Non-Compliance Penalty) | R250 -- R16,000/month depending on taxable income band |
| Under-estimation of provisional tax | 20% of difference between actual and estimated tax |
| Late payment interest | Prescribed rate (approx. 10.75% p.a. -- SARS publishes quarterly) |
| Understatement penalty | 10% (substantial understatement) to 200% (intentional evasion) |
| Failure to register as provisional taxpayer | R250 -- R16,000/month |

### Admin Non-Compliance Penalty Scale [T1]

| Assessed Loss / Taxable Income | Monthly Penalty |
|-------------------------------|-----------------|
| Assessed loss | R250 |
| R0 -- R250,000 | R250 |
| R250,001 -- R500,000 | R500 |
| R500,001 -- R1,000,000 | R1,000 |
| R1,000,001 -- R5,000,000 | R2,000 |
| R5,000,001 -- R10,000,000 | R4,000 |
| R10,000,001 -- R50,000,000 | R8,000 |
| R50,000,001+ | R16,000 |

Maximum: 35 months of penalties.

---

## Step 10: Record Keeping [T1]

**Legislation:** Tax Administration Act, s29-s32

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 5 years from date of submission of return (prescribed in s29) |
| What to keep | All invoices, receipts, bank statements, contracts, logbooks, asset register |
| Format | Paper or electronic (SARS accepts both) |
| Logbook | Must be maintained for motor vehicle claims (date, destination, km, purpose) |

---

## Step 11: Edge Case Registry

### EC1 -- Interest exemption applied incorrectly [T1]
**Situation:** Self-employed client aged 40 earns R30,000 interest from a savings account. Client excludes all interest from taxable income.
**Resolution:** Only R23,800 is exempt (under 65). The remaining R6,200 must be included in taxable income. If client were 65+, exemption would be R34,500.

### EC2 -- Turnover tax elected but client earns professional service income [T1]
**Situation:** Client is a freelance accountant who elects turnover tax.
**Resolution:** NOT eligible. Professional services (accounting, legal, medical, etc.) are excluded from turnover tax under the Sixth Schedule. Must use normal tax system.

### EC3 -- Retirement contribution exceeds cap [T1]
**Situation:** Self-employed client contributes R400,000 to RA in a single year. Taxable income is R900,000.
**Resolution:** Deduction = lesser of 27.5% x R900,000 = R247,500 or R350,000. Deduction is R247,500. Excess R152,500 carries forward. Do not deduct more than R247,500.

### EC4 -- Home office in shared room [T2]
**Situation:** Client works from a dining room table that is also used for family meals.
**Resolution:** NOT deductible. IN 28 requires the room to be used regularly and exclusively for trade. A dual-use room does not qualify. No home office deduction.

### EC5 -- Provisional tax under-estimated [T1]
**Situation:** Client estimated taxable income at R300,000 on both IRP6 returns. Actual taxable income is R500,000.
**Resolution:** Penalty applies. 20% x (tax on R500,000 minus tax on R300,000) = penalty. SARS may also impose interest. Flag to client immediately.

### EC6 -- Medical credits for sole proprietor with 4 dependants [T1]
**Situation:** Main member + spouse + 3 children on medical aid. Monthly contribution R5,000.
**Resolution:** Credit = (R364 x 2 for first two members) + (R246 x 3 for additional dependants) = R728 + R738 = R1,466/month = R17,592/year. This is a credit against tax, not a deduction from income.

### EC7 -- Foreign income for resident [T3]
**Situation:** SA-resident freelancer earns income from clients in the UK and wants to know about the foreign employment income exemption.
**Resolution:** ESCALATE. The s10(1)(o)(ii) exemption applies only to employment income, not self-employment income. Foreign self-employment income is fully taxable (subject to foreign tax credits under s6quat). This is T3 -- refer to a tax practitioner for proper double taxation agreement analysis.

### EC8 -- Switching from turnover tax to normal tax mid-year [T2]
**Situation:** Client was on turnover tax but turnover exceeded R1M in September.
**Resolution:** Client must exit turnover tax. The transition rules under the Sixth Schedule require the client to register for normal tax. [T2] Flag for reviewer -- transitional calculations and potential VAT registration implications must be assessed.

### EC9 -- Entertainment expenses claimed [T1]
**Situation:** Client includes R15,000 for client entertainment dinners as a business expense.
**Resolution:** NOT deductible for sole proprietors. s23(m) denies entertainment deductions for individuals deriving income mainly from trade. Remove from deductions.

### EC10 -- Assessed loss carried forward [T2]
**Situation:** Client's business expenses exceed income, creating an assessed loss of R80,000.
**Resolution:** The assessed loss can be carried forward to the next year under s20. However, SARS may query the loss and require evidence that the trade is being carried on with a reasonable prospect of profit. [T2] Flag for reviewer.

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
Action Required: Registered tax practitioner must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to registered tax practitioner. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard self-employed, mid-range income
**Input:** Age 35, gross revenue R600,000, allowable expenses R180,000, RA contribution R80,000, medical aid R3,500/month (main + 1 dependant), provisional tax paid R40,000.
**Expected output:** Net profit R420,000. s11F deduction = 27.5% x R420,000 = R115,500 (below cap). Taxable income = R304,500. Tax = R42,678 + 26% x (R304,500 - R237,100) = R42,678 + R17,524 = R60,202. Rebate R17,235. Medical credit = R364 x 2 x 12 = R8,736. Net tax = R60,202 - R17,235 - R8,736 = R34,231. Less provisional R40,000 = refund R5,769.

### Test 2 -- Senior citizen with enhanced rebates
**Input:** Age 68, gross revenue R200,000, expenses R50,000, RA R30,000, no medical aid, no provisional tax.
**Expected output:** Net profit R150,000. s11F = 27.5% x R150,000 = R41,250. Taxable income = R108,750. Tax = 18% x R108,750 = R19,575. Less primary R17,235 less secondary R9,444 = -R7,104. Tax = R0 (below threshold R148,217). No tax payable.

### Test 3 -- Turnover tax election
**Input:** Sole proprietor, non-professional service, turnover R650,000. Elected turnover tax.
**Expected output:** Turnover tax = R1,650 + 2% x (R650,000 - R500,000) = R1,650 + R3,000 = R4,650 total tax for the year.

### Test 4 -- Retirement deduction hits cap
**Input:** Taxable income (before s11F) R2,000,000. RA contribution R600,000.
**Expected output:** 27.5% x R2,000,000 = R550,000 but cap is R350,000. Deduction = R350,000. Excess R250,000 carries forward.

### Test 5 -- Medical credits with large family
**Input:** Main member + spouse + 4 children = 6 members. Monthly contribution R8,000.
**Expected output:** Credit = (R364 x 2) + (R246 x 4) = R728 + R984 = R1,712/month = R20,544/year credit against tax.

### Test 6 -- Under-estimation penalty
**Input:** Client estimated R200,000 taxable income on both IRP6s. Actual taxable income R450,000.
**Expected output:** Tax on actual R450,000 = R42,678 + 26% x (R450,000 - R237,100) = R42,678 + R55,354 = R98,032 - R17,235 rebate = R80,797. Tax on estimated R200,000 = R36,000 - R17,235 = R18,765. Under-estimation penalty = 20% x (R80,797 - R18,765) = R12,406.

---

## PROHIBITIONS

- NEVER compute tax without knowing the client's age (determines rebates and threshold)
- NEVER apply tax to income below the tax threshold for the relevant age group
- NEVER allow entertainment expenses as a deduction for sole proprietors
- NEVER deduct retirement contributions above the R350,000 annual cap
- NEVER allow turnover tax for professional service providers (accountants, lawyers, doctors, etc.)
- NEVER use prior year income for provisional tax -- South Africa uses estimated current year income
- NEVER treat medical tax credits as a deduction from income -- they are credits against tax
- NEVER allow home office deduction for a non-dedicated, dual-use room
- NEVER allow income tax itself as a deduction
- NEVER present tax calculations as definitive -- always label as estimated and direct client to a registered tax practitioner for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a registered tax practitioner, CA(SA), or equivalent licensed practitioner in South Africa) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
