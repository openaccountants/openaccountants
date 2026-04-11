---
name: jp-income-tax
description: >
  Use this skill whenever asked about Japanese income tax for self-employed individuals filing a final tax return (確定申告 Kakutei Shinkoku). Trigger on phrases like "how much tax do I pay in Japan", "kakutei shinkoku", "確定申告", "blue return", "青色申告", "white return", "白色申告", "business income Japan", "事業所得", "necessary expenses", "必要経費", "basic deduction", "基礎控除", "reconstruction tax", "resident tax", "住民税", "self-employed tax Japan", "e-Tax", or any question about filing or computing income tax for a self-employed individual in Japan. This skill covers progressive brackets (5%-45%), blue vs white return, special deductions, reconstruction surtax, resident tax, necessary expenses, social insurance, and filing deadlines. ALWAYS read this skill before touching any Japan income tax work.
version: 1.0
jurisdiction: JP
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Japan Income Tax (確定申告) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Japan |
| Jurisdiction Code | JP |
| Primary Legislation | Income Tax Act (所得税法 Shotokuzei-ho) |
| Supporting Legislation | Special Taxation Measures Act (租税特別措置法); Local Tax Act (地方税法); Act on Special Measures for Securing Financial Resources Necessary for Reconstruction (復興財源確保法) |
| Tax Authority | National Tax Agency (国税庁 NTA / Kokuzei-cho) |
| Filing Portal | e-Tax (国税電子申告・納税システム) |
| Contributor | Open Accountants community |
| Validated By | Pending -- requires sign-off by a Japanese Certified Public Tax Accountant (税理士 Zeirishi) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, blue return special deduction amounts, basic deduction, filing deadlines, reconstruction surtax calculation. Tier 2: home office apportionment, vehicle business %, medical expense deduction thresholds, spouse deduction eligibility, mixed-use expense allocation. Tier 3: foreign tax credits, capital gains on real estate, cryptocurrency taxation, non-resident taxation, corporate restructuring. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Licensed tax accountant (税理士) must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Tax residency status** [T1] -- resident (居住者), non-permanent resident (非永住者), or non-resident (非居住者). Non-residents have different rules. If non-resident, escalate [T3].
2. **Return type** [T1] -- blue return (青色申告) or white return (白色申告). Determines available deductions.
3. **Gross business income (事業収入)** [T1] -- total business revenue received in the calendar year (January 1 -- December 31).
4. **Bookkeeping method** [T1] -- double-entry bookkeeping (複式簿記) or simplified bookkeeping (簡易簿記). Affects blue return deduction amount.
5. **e-Tax filing or paper filing** [T1] -- e-Tax filing is required for the maximum blue return deduction.
6. **Necessary expenses (必要経費)** [T1/T2] -- nature and amount of each business expense.
7. **Social insurance premiums paid** [T1] -- national health insurance (国民健康保険), national pension (国民年金), and any other social insurance.
8. **Marital status and dependents** [T2] -- for spouse deduction (配偶者控除) and dependent deduction (扶養控除).
9. **Other income** [T1] -- employment income (給与所得), interest, dividends, rental, miscellaneous income.
10. **Prior year carried-forward losses** [T1] -- blue return filers can carry forward losses for 3 years.

**If tax residency is unknown, STOP. Do not compute. Tax residency status is mandatory.**

---

## Step 1: Determine Applicable National Income Tax Rates [T1]

**Legislation:** Income Tax Act (所得税法), Article 89

### Progressive Tax Rates (2025 tax year)

| Taxable Income (JPY) | Rate | Deduction Amount (控除額) | Cumulative Reference |
|----------------------|------|--------------------------|---------------------|
| 0 -- 1,950,000 | 5% | 0 | Max tax: 97,500 |
| 1,950,001 -- 3,300,000 | 10% | 97,500 | Max tax: 232,500 |
| 3,300,001 -- 6,950,000 | 20% | 427,500 | Max tax: 962,500 |
| 6,950,001 -- 9,000,000 | 23% | 636,000 | Max tax: 1,434,000 |
| 9,000,001 -- 18,000,000 | 33% | 1,536,000 | Max tax: 4,404,000 |
| 18,000,001 -- 40,000,000 | 40% | 2,796,000 | Max tax: 13,204,000 |
| 40,000,001+ | 45% | 4,796,000 | -- |

**Shortcut formula:** Tax = (Taxable Income x Rate) - Deduction Amount. For example: taxable income of 5,000,000 => (5,000,000 x 20%) - 427,500 = 572,500.

**These rates have been stable since 2015 and remain unchanged for tax year 2025.**

---

## Step 2: Reconstruction Special Income Tax (復興特別所得税) [T1]

**Legislation:** Act on Special Measures for Securing Financial Resources Necessary for Reconstruction

- **Rate:** 2.1% of the calculated national income tax amount
- **Period:** 2013 through 2037 (25 years)
- **Calculation:** Reconstruction tax = National income tax x 2.1%
- **Total effective rate:** National income tax x 102.1%

Example: If national income tax is 500,000, reconstruction tax = 500,000 x 2.1% = 10,500. Total national tax = 510,500.

---

## Step 3: Resident Tax (住民税) [T1]

**Legislation:** Local Tax Act (地方税法)

### Structure [T1]

| Component | Rate | Notes |
|-----------|------|-------|
| Prefectural income tax (都道府県民税) | 4% | Of taxable income |
| Municipal income tax (市区町村民税) | 6% | Of taxable income |
| **Total income-based** | **10%** | Flat combined rate |
| Per-capita levy (均等割) | Approx. 5,000 | Fixed annual amount (varies slightly by municipality) |
| Forest environment tax (森林環境税) | 1,000 | From 2024 onward |

### Key Rules [T1]

- Resident tax is calculated and assessed **by the municipality** based on the prior year's national tax return.
- Resident tax is **not filed separately** -- the municipality computes it from the final return (確定申告) data.
- Payment: quarterly instalments (June, August, October, January) or monthly withholding for employees.
- Resident tax uses a slightly different deduction structure than national tax (e.g., basic deduction for resident tax is 430,000, not 580,000).
- Self-employed persons pay resident tax by quarterly payment slips (普通徴収).

---

## Step 4: Blue Return vs White Return [T1]

**Legislation:** Income Tax Act, Articles 143-148 (blue return provisions)

### Comparison [T1]

| Feature | Blue Return (青色申告) | White Return (白色申告) |
|---------|----------------------|----------------------|
| Application required | Yes -- must file Form 144 (青色申告承認申請書) in advance | No -- default method |
| Application deadline | By 15 March of the year you want to start (or within 2 months of starting business) | N/A |
| Bookkeeping requirement | Double-entry bookkeeping (for max deduction) or simplified bookkeeping | Basic record-keeping |
| Special deduction | Up to 650,000 (double-entry + e-Tax) or 550,000 (double-entry, paper filing) or 100,000 (simplified bookkeeping) | None |
| Loss carry-forward | 3 years | Not available |
| Family employee salary deduction | Fully deductible if pre-registered (専従者給与) | Limited to 500,000 (spouse) or 860,000 (other family) |
| Depreciation special provisions | Available (increased initial depreciation, etc.) | Not available |

### Blue Return Special Deduction Amounts (2025) [T1]

| Condition | Deduction (JPY) |
|-----------|----------------|
| Double-entry bookkeeping + e-Tax filing (or approved digital record-keeping) | 650,000 |
| Double-entry bookkeeping + paper filing | 550,000 |
| Simplified bookkeeping (either filing method) | 100,000 |

**Note:** Starting from tax year 2026 (to be filed in 2027), the blue return special deduction is expected to increase to 750,000 for those maintaining "excellent electronic books" (優良な電子帳簿). This does NOT apply to tax year 2025.

---

## Step 5: Business Income Computation (事業所得) [T1/T2]

**Legislation:** Income Tax Act, Articles 27, 37

### Computation Structure [T1]

```
  Gross business revenue (事業収入/売上)
- Necessary expenses (必要経費)
= Business income before blue return deduction (事業所得 -- 青色申告特別控除前)
- Blue return special deduction (青色申告特別控除)
= Business income (事業所得)
```

### Necessary Expenses (必要経費) -- Deductible [T1/T2]

| Expense (Japanese term) | Tier | Treatment |
|--------------------------|------|-----------|
| Rent for business premises (地代家賃) | T1 | Fully deductible |
| Utilities for business premises (水道光熱費) | T1/T2 | Fully deductible if dedicated; apportion if home office |
| Communication costs (通信費) -- phone, internet | T2 | Business use portion only |
| Travel and transportation (旅費交通費) | T1 | Fully deductible if business purpose |
| Advertising and promotion (広告宣伝費) | T1 | Fully deductible |
| Office supplies and consumables (消耗品費) | T1 | Fully deductible. Items under 100,000 can be expensed immediately. |
| Depreciation (減価償却費) | T1 | Per NTA depreciation tables (see Step 6) |
| Insurance premiums, business (損害保険料) | T1 | Fully deductible |
| Repair and maintenance (修繕費) | T1 | Deductible if maintaining existing condition (not improvement) |
| Outsourcing and subcontracting (外注工賃) | T1 | Fully deductible |
| Books and reference materials (図書研究費/新聞図書費) | T1 | Fully deductible if business-related |
| Entertainment and hospitality (接待交際費) | T2 | Deductible if business purpose; no statutory limit for sole proprietors (unlike corporations). Flag for reviewer if excessive. |
| Tax accountant fees (税理士報酬) | T1 | Fully deductible |
| Bad debts (貸倒金) | T2 | Flag for reviewer -- confirm irrecoverability |
| Interest on business loans (利子割引料) | T1 | Fully deductible |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Income tax and resident tax (所得税・住民税) | Tax on income cannot be deducted |
| Personal living expenses (家事費) | Private expense |
| Fines and penalties (罰金・科料) | Public policy |
| National pension and health insurance premiums | NOT a business expense -- deducted as social insurance deduction (所得控除), not as a necessary expense |
| Personal portion of mixed-use expenses | Must be apportioned; personal portion is non-deductible |

### Home Office Rules (家事按分) [T2]

- Calculate the proportion of home used for business: floor area ratio or time-based ratio
- Apply that percentage to: rent, electricity, internet, water
- NTA generally accepts a reasonable apportionment (no requirement for a dedicated room, unlike Malta)
- Common accepted ratios: 30-50% for freelancers working primarily from home
- Must be documented and consistent
- [T2] Flag for reviewer: confirm apportionment method is reasonable and documented

---

## Step 6: Depreciation (減価償却) [T1]

**Legislation:** Income Tax Act, Article 49; NTA Depreciation Tables (耐用年数表)

### Common Depreciation Rates (Declining Balance / 定率法 is default for most assets)

| Asset Type | Useful Life | Declining Balance Rate | Straight-Line Rate |
|-----------|-------------|----------------------|-------------------|
| Personal computers | 4 years | 0.500 | 0.250 |
| Servers | 5 years | 0.400 | 0.200 |
| Office furniture (metal) | 15 years | 0.133 | 0.067 |
| Office furniture (wood) | 8 years | 0.250 | 0.125 |
| Motor vehicles (ordinary) | 6 years | 0.333 | 0.167 |
| Motor vehicles (light) | 4 years | 0.500 | 0.250 |
| Buildings (residential, wood) | 22 years | N/A (SL only) | 0.046 |
| Buildings (residential, RC) | 47 years | N/A (SL only) | 0.022 |
| Software (purchased) | 3-5 years | varies | 0.200-0.333 |

### Rules [T1]

- **Default method:** Declining balance (定率法) for most assets. Buildings must use straight-line (定額法) since 2016.
- **Election:** Taxpayer can elect straight-line for any asset by filing Form 16 (減価償却資産の償却方法の届出書).
- **Items under 100,000:** Can be expensed immediately (少額減価償却資産).
- **Items 100,001 to 199,999:** Can be depreciated over 3 years uniformly (一括償却資産) regardless of type.
- **Blue return filers: items under 300,000:** Can be expensed immediately (少額減価償却資産の特例), subject to an annual aggregate limit of 3,000,000. This is a blue return privilege.
- Pro-rata for months of use in the acquisition year.

---

## Step 7: Income Deductions (所得控除) [T1/T2]

**Legislation:** Income Tax Act, Articles 72-86

These deductions are subtracted from total income (after business income computation) to arrive at taxable income.

### Key Deductions [T1]

| Deduction (Japanese) | Amount (2025) | Notes |
|----------------------|---------------|-------|
| Basic deduction (基礎控除) | 580,000 (income up to 23.5M); phases down above; 0 above 25M | Increased from 480,000 for 2025 tax year |
| Social insurance deduction (社会保険料控除) | Actual amount paid | National pension, national health insurance, etc. Unlimited. |
| Small enterprise mutual aid deduction (小規模企業共済等掛金控除) | Actual amount paid | iDeCo contributions included here |
| Life insurance deduction (生命保険料控除) | Up to 120,000 total | Combined limit for general, medical, pension insurance |
| Earthquake insurance deduction (地震保険料控除) | Up to 50,000 | Actual premiums paid |
| Spouse deduction (配偶者控除) | Up to 380,000 | If spouse's income is 480,000 or less; phases out if taxpayer income > 9M |
| Special spouse deduction (配偶者特別控除) | Up to 380,000 (sliding scale) | If spouse's income is between 480,001 and 1,330,000 |
| Dependent deduction (扶養控除) | 380,000 -- 630,000 per dependent | Amount varies by age of dependent |
| Medical expense deduction (医療費控除) | Amount exceeding 100,000 (or 5% of income if lower) | Cap of 2,000,000 |
| Donation deduction (寄附金控除) | Amount minus 2,000 | For qualifying donations (furusato nozei, etc.) |
| Disability deduction (障害者控除) | 270,000 -- 750,000 | Per qualifying person |

### Basic Deduction Detail (2025 Reform) [T1]

| Total Income (合計所得金額) | Basic Deduction (2025) |
|----------------------------|----------------------|
| Up to 1,320,000 | 950,000 (temporary special enhancement for 2025-2026) |
| 1,320,001 -- 2,695,000 | 880,000 (temporary special enhancement for 2025-2026) |
| 2,695,001 -- 6,550,000 | 680,000 (temporary special enhancement for 2025-2026) |
| 6,550,001 -- 23,500,000 | 580,000 |
| 23,500,001 -- 24,000,000 | 480,000 |
| 24,000,001 -- 24,500,000 | 320,000 |
| 24,500,001 -- 25,000,000 | 160,000 |
| Above 25,000,000 | 0 |

**Note:** For 2025-2026 only, a temporary special enhancement (特定親族特別控除 / 特別基礎控除上乗せ) applies for incomes up to 6,550,000, providing an additional basic deduction above the standard 580,000. Confirm details with the NTA for the exact applicable amounts.

---

## Step 8: Tax Computation Walkthrough [T1]

### Full Computation Flow

```
1. Gross business revenue (事業収入)
2. Minus: Necessary expenses (必要経費)
3. = Business income before blue deduction
4. Minus: Blue return special deduction (青色申告特別控除)
5. = Business income (事業所得)
6. Plus: Other income (給与所得, 雑所得, etc.)
7. = Total income (合計所得金額)
8. Minus: Income deductions (所得控除) -- basic, social insurance, spouse, dependents, etc.
9. = Taxable income (課税所得金額) -- round down to nearest 1,000
10. Apply progressive rate table (Step 1)
11. = Calculated income tax (算出税額)
12. Minus: Tax credits (税額控除) -- dividend credit, housing loan credit, etc.
13. = National income tax before reconstruction tax
14. Plus: Reconstruction special income tax (2.1% of line 13)
15. = Total national tax payable (申告納税額) -- round down to nearest 100
16. Minus: Withholding tax already paid (源泉徴収税額)
17. = Tax due / refund (第3期分の税額 / 還付)
```

**Taxable income is rounded down to the nearest 1,000 yen before applying the rate table.**
**Final tax payable is rounded down to the nearest 100 yen.**

---

## Step 9: Filing Deadlines [T1]

**Legislation:** Income Tax Act; Tax Administration Act

| Filing / Payment | Deadline |
|-----------------|----------|
| Final return (確定申告) | March 15 of the following year (e.g., 2025 income due by March 15, 2026) |
| Payment of national income tax | March 15 (same as filing deadline) |
| Deferred payment (延納) | Up to half the tax can be deferred until May 31 (with interest) |
| Resident tax payment | Quarterly: June, August, October, January (municipality sends payment slips after processing the final return) |
| Consumption tax return (if applicable) | March 31 of the following year |

**Filing period:** February 16 to March 15. The NTA opens the filing window on February 16 each year.

**Extension:** No general extension available for individuals. If the deadline falls on a weekend or holiday, it moves to the next business day.

---

## Step 10: Penalties [T1]

**Legislation:** National Tax Penalties Act (国税通則法)

| Offence | Penalty |
|---------|---------|
| Late filing (期限後申告) -- within 1 month, voluntary | 5% of the additional tax due (無申告加算税) |
| Late filing -- beyond 1 month or after notice | 15% on first 500,000 + 20% on excess (無申告加算税) |
| Under-reporting (過少申告加算税) | 10% of additional tax due (15% on portion exceeding 500,000 or 10% of original tax, whichever is greater) |
| Fraud or concealment (重加算税) | 35% (with return filed) or 40% (no return filed) |
| Late payment interest (延滞税) | Approx. 2.4% for first 2 months, then approx. 8.7% (rates adjusted annually based on market rates) |

---

## Step 11: Record Keeping [T1]

**Legislation:** Income Tax Act; Blue Return provisions

| Requirement | Blue Return | White Return |
|-------------|------------|--------------|
| Retention period | 7 years for accounting books; 5 years for receipts and other documents | 5 years for receipts; 7 years for accounting books (if income > 3M) |
| What to keep | General journal, general ledger, all invoices, receipts, bank statements, contracts | Simple income/expense records, receipts |
| Format | Paper or digital (electronic record-keeping rules apply under the Electronic Books Preservation Act / 電子帳簿保存法) | Paper or digital |
| Invoice requirements | From Oct 2023: Qualified Invoice (適格請求書) for consumption tax input credits | Basic receipts |

---

## Step 12: Edge Case Registry

### EC1 -- Blue return filed without advance application [T1]
**Situation:** Client started freelancing in April 2025 and wants to file a blue return for 2025, but never submitted Form 144.
**Resolution:** Blue return application must be filed within 2 months of starting a business, or by March 15 of the first year the blue return is desired (for existing businesses). If the deadline was missed, the client must file a white return for 2025 and apply for blue return from 2026. No retroactive approval.

### EC2 -- White return filer tries to carry forward losses [T1]
**Situation:** White return filer had a business loss of 2,000,000 in 2024 and wants to offset it against 2025 income.
**Resolution:** NOT allowed. Loss carry-forward is a blue return privilege only. The 2024 loss is forfeited for white return filers.

### EC3 -- Home office expense without apportionment [T2]
**Situation:** Client works from home and deducts 100% of rent (120,000/month = 1,440,000/year) as a business expense.
**Resolution:** Must apportion between business and personal use. NTA expects a reasonable ratio (e.g., floor area or time). If client works from a dedicated room that is 30% of the apartment, deduct 30% = 432,000. [T2] Flag for reviewer to confirm apportionment.

### EC4 -- National pension deducted as necessary expense [T1]
**Situation:** Client includes national pension payments (199,080/year) in the necessary expenses section of the return.
**Resolution:** INCORRECT. National pension is a social insurance deduction (所得控除), NOT a necessary expense (必要経費). Move to the social insurance deduction section. It reduces income after business income computation, not business income itself.

### EC5 -- Blue return: simplified bookkeeping claiming 650,000 deduction [T1]
**Situation:** Blue return filer uses simplified bookkeeping (簡易簿記) but claims the 650,000 special deduction.
**Resolution:** INCORRECT. Simplified bookkeeping only qualifies for the 100,000 deduction. The 650,000 deduction requires double-entry bookkeeping AND e-Tax filing (or approved electronic record-keeping). Reduce to 100,000.

### EC6 -- Reconstruction tax omitted [T1]
**Situation:** Client computes national income tax as 500,000 but does not add the reconstruction special income tax.
**Resolution:** INCORRECT. Must add 2.1%: 500,000 x 2.1% = 10,500. Total national tax = 510,500. The reconstruction surtax applies to all individual income tax through 2037.

### EC7 -- Entertainment expenses for sole proprietor [T2]
**Situation:** Sole proprietor deducts 800,000 in entertainment/hospitality expenses (接待交際費).
**Resolution:** Unlike corporations (which have statutory limits), sole proprietors have NO statutory cap on entertainment deductions. However, the expenses must be genuinely business-related and reasonable. An unusually high amount will attract NTA scrutiny. [T2] Flag for reviewer to assess reasonableness.

### EC8 -- Asset under 100,000 yen capitalised [T1]
**Situation:** Client buys a 80,000 yen desk and adds it to the depreciation schedule.
**Resolution:** Assets costing under 100,000 yen are treated as consumables (少額減価償却資産) and can be expensed immediately. Remove from depreciation schedule and deduct fully in current year.

### EC9 -- Spouse deduction claimed when spouse income is too high [T1]
**Situation:** Client claims spouse deduction (配偶者控除) of 380,000, but spouse has part-time income of 1,500,000.
**Resolution:** INCORRECT. Spouse deduction requires spouse's total income to be 480,000 or less (approximately 1,030,000 in gross salary after the employment income deduction). At 1,500,000 gross salary, the spouse's income exceeds the limit. Check if special spouse deduction (配偶者特別控除) applies at a reduced amount based on a sliding scale.

### EC10 -- Withholding tax on freelance payments not claimed as credit [T1]
**Situation:** Freelance designer received 1,000,000 in payments from clients, with 102,100 withheld at source (10.21%). Client reports net receipts of 897,900 as income.
**Resolution:** INCORRECT. Gross income is 1,000,000 (pre-withholding). The 102,100 is a tax credit (源泉徴収税額), not a reduction of income. Report 1,000,000 as gross business revenue and claim 102,100 as a credit against the final tax liability.

---

## Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Licensed tax accountant (税理士) must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed tax accountant (税理士). Document gap.
```

---

## Step 14: Test Suite

### Test 1 -- Standard blue return filer, mid-range income
**Input:** Resident, blue return (double-entry + e-Tax), gross business revenue 8,000,000, necessary expenses 2,500,000, national pension 199,080, national health insurance 450,000, basic deduction applies. No other deductions.
**Expected output:** Business income before blue deduction = 5,500,000. Blue deduction = 650,000. Business income = 4,850,000. Total income = 4,850,000. Social insurance deduction = 199,080 + 450,000 = 649,080. Basic deduction = 680,000 (temporary enhanced for income up to 6.55M). Taxable income = 4,850,000 - 649,080 - 680,000 = 3,520,920, rounded down to 3,520,000. Tax = (3,520,000 x 20%) - 427,500 = 276,500. Reconstruction tax = 276,500 x 2.1% = 5,806 (rounded down to 5,806). Total national tax = 282,306, rounded down to 282,300.

### Test 2 -- White return filer, low income
**Input:** Resident, white return, gross business revenue 3,000,000, necessary expenses 1,200,000, national pension 199,080, national health insurance 200,000. No dependents.
**Expected output:** Business income = 1,800,000 (no blue deduction). Social insurance = 399,080. Basic deduction = 880,000 (temporary enhanced for income up to 2.695M). Taxable income = 1,800,000 - 399,080 - 880,000 = 520,920, rounded down to 520,000. Tax = 520,000 x 5% = 26,000. Reconstruction tax = 26,000 x 2.1% = 546. Total = 26,546, rounded down to 26,500.

### Test 3 -- Blue return with simplified bookkeeping
**Input:** Resident, blue return with simplified bookkeeping (簡易簿記), paper filing. Gross revenue 5,000,000, expenses 1,500,000.
**Expected output:** Blue deduction = 100,000 (not 650,000 -- simplified bookkeeping). Business income = 5,000,000 - 1,500,000 - 100,000 = 3,400,000.

### Test 4 -- Withholding tax credit
**Input:** Freelance writer, blue return (e-Tax, double-entry). Gross revenue 6,000,000 (before withholding). Withholding tax deducted by clients: 612,600 (10.21%). Expenses: 1,000,000.
**Expected output:** Business income = 6,000,000 - 1,000,000 - 650,000 = 4,350,000. After income deductions (assume 1,200,000 total), taxable income = 3,150,000. Tax = (3,150,000 x 10%) - 97,500 = 217,500. Reconstruction = 217,500 x 2.1% = 4,567. Total = 222,067, rounded to 222,000. Less withholding 612,600. Refund of approximately 390,600.

### Test 5 -- Loss carry-forward (blue return only)
**Input:** Blue return filer. 2024 loss of 1,500,000 carried forward. 2025 business income = 4,000,000.
**Expected output:** 2025 business income after loss offset = 4,000,000 - 1,500,000 = 2,500,000. The loss carry-forward is applied before income deductions.

### Test 6 -- National pension incorrectly deducted as necessary expense
**Input:** Client includes 199,080 national pension in necessary expenses (必要経費).
**Expected output:** Remove from necessary expenses. Move to social insurance deduction (社会保険料控除). Business income increases by 199,080; but taxable income remains the same since it is deducted as an income deduction instead.

### Test 7 -- Reconstruction tax verification
**Input:** National income tax calculated as 1,000,000.
**Expected output:** Reconstruction tax = 1,000,000 x 2.1% = 21,000. Total national tax = 1,021,000.

---

## PROHIBITIONS

- NEVER compute income tax without confirming tax residency status
- NEVER apply the 650,000 blue return deduction without verifying double-entry bookkeeping AND e-Tax filing (or approved digital record-keeping)
- NEVER allow blue return privileges (loss carry-forward, full family salary deduction, 650,000 deduction) for white return filers
- NEVER omit the reconstruction special income tax (2.1%)
- NEVER deduct national pension or health insurance as a necessary expense -- they are income deductions
- NEVER allow income tax or resident tax as a deduction
- NEVER allow fines or penalties as a deduction
- NEVER skip rounding down taxable income to the nearest 1,000 yen before applying rates
- NEVER skip rounding down final tax payable to the nearest 100 yen
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their tax accountant (税理士) for confirmation
- NEVER advise on non-resident taxation, cryptocurrency gains, or real estate capital gains without escalating [T3]

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Certified Public Tax Accountant / 税理士 or equivalent licensed practitioner in Japan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
