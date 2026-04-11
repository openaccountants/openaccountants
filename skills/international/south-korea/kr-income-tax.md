---
name: kr-income-tax
description: >
  Use this skill whenever asked about South Korean income tax for self-employed individuals. Trigger on phrases like "comprehensive income tax", "종합소득세", "global income tax Korea", "사업소득", "business income Korea", "간편장부", "simplified bookkeeping", "복식부기", "double-entry Korea", "local income tax surtax", "estimated tax Korea", "Korean income tax return", or any question about filing or computing income tax for a Korean freelancer or self-employed person. Also trigger when preparing or reviewing a comprehensive income tax return, computing deductions, or advising on bookkeeping method thresholds. This skill covers progressive brackets (6-45%), local income tax (10% surtax), bookkeeping methods, standard deduction rates, personal deductions, filing deadlines, estimated tax, and penalties. ALWAYS read this skill before touching any Korean income tax work.
version: 1.0
jurisdiction: KR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# South Korea Income Tax (종합소득세) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | South Korea (Republic of Korea) |
| Jurisdiction Code | KR |
| Primary Legislation | Income Tax Act (소득세법), Art. 55 (tax rates), Art. 70 (filing), Art. 160 (bookkeeping) |
| Supporting Legislation | Local Tax Act (지방세법) Art. 86-92 (local income tax); Enforcement Decree of the Income Tax Act (소득세법 시행령); Tax Procedures Act (국세기본법) |
| Tax Authority | National Tax Service (국세청, NTS) |
| Filing Portal | Hometax (hometax.go.kr) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a qualified Korean 세무사 (tax accountant) or 공인회계사 (CPA) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, bracket calculation, local income tax surtax, bookkeeping thresholds, filing deadlines, estimated tax schedule. Tier 2: standard deduction rate selection, mixed-use expense apportionment, personal deduction eligibility, bookkeeping method optimisation. Tier 3: international income, financial income global taxation, capital gains on real estate, corporate conversion. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified 세무사 or 공인회계사 must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Business type (업종)** [T1] -- service, manufacturing, retail, profession, etc. Determines standard deduction rate and bookkeeping threshold.
2. **Total revenue (총수입금액)** [T1] -- gross business income for the year.
3. **Bookkeeping method** [T1] -- simplified bookkeeping (간편장부), double-entry bookkeeping (복식부기), or standard deduction rate (기준경비율/단순경비율).
4. **Business expenses** [T1/T2] -- nature and amount of each necessary expense (T2 for mixed-use items).
5. **Other income** [T1] -- employment income (근로소득), interest (이자소득), dividends (배당소득), pension (연금소득), other income (기타소득).
6. **Family status** [T1] -- marital status, number of dependants (spouse, children, parents aged 60+).
7. **Insurance/medical/education expenses** [T2] -- amounts paid for eligible deductions.
8. **Estimated tax already paid** [T1] -- November prepayment (중간예납) and withholding taxes (원천징수).
9. **Prior year tax liability** [T1] -- for estimated tax (중간예납) calculation.

**If business type is unknown, STOP. The business type determines the applicable standard deduction rate and bookkeeping threshold.**

---

## Step 1: Progressive Tax Brackets (국세) [T1]

**Legislation:** Income Tax Act (소득세법), Art. 55 -- 2025 Tax Year

| Taxable Income (과세표준) | Rate | Cumulative Tax at Top of Band | Quick Deduction (누진공제) |
|---------------------------|------|-------------------------------|---------------------------|
| Up to KRW 14,000,000 | 6% | KRW 840,000 | -- |
| KRW 14,000,001 -- KRW 50,000,000 | 15% | KRW 6,240,000 | KRW 1,260,000 |
| KRW 50,000,001 -- KRW 88,000,000 | 24% | KRW 15,360,000 | KRW 5,760,000 |
| KRW 88,000,001 -- KRW 150,000,000 | 35% | KRW 37,060,000 | KRW 15,440,000 |
| KRW 150,000,001 -- KRW 300,000,000 | 38% | KRW 94,060,000 | KRW 19,940,000 |
| KRW 300,000,001 -- KRW 500,000,000 | 40% | KRW 174,060,000 | KRW 25,940,000 |
| KRW 500,000,001 -- KRW 1,000,000,000 | 42% | KRW 384,060,000 | KRW 35,940,000 |
| Over KRW 1,000,000,000 | 45% | -- | KRW 65,940,000 |

### Quick Calculation Method [T1]

Tax = (과세표준 x applicable rate) - 누진공제

Example: 과세표준 KRW 60,000,000 -> (60,000,000 x 24%) - 5,760,000 = 14,400,000 - 5,760,000 = KRW 8,640,000

**NEVER compute final tax figures directly in Claude -- pass 과세표준 to the deterministic engine to apply the brackets.**

---

## Step 2: Local Income Tax (지방소득세) [T1]

**Legislation:** Local Tax Act (지방세법), Art. 86-92

| Rule | Detail |
|------|--------|
| Rate | 10% of national income tax liability |
| Filing | Separate return filed with the local government |
| Deadline | Same as national: 31 May (or 30 June with tax agent) |
| Payment | Separate from national tax |

**Effective combined marginal rates:**

| National Rate | + Local (10% surtax) | = Combined Rate |
|---------------|----------------------|-----------------|
| 6% | 0.6% | 6.6% |
| 15% | 1.5% | 16.5% |
| 24% | 2.4% | 26.4% |
| 35% | 3.5% | 38.5% |
| 38% | 3.8% | 41.8% |
| 40% | 4.0% | 44.0% |
| 42% | 4.2% | 46.2% |
| 45% | 4.5% | 49.5% |

---

## Step 3: Bookkeeping Methods and Thresholds [T1/T2]

**Legislation:** Income Tax Act, Art. 160; Enforcement Decree Art. 208

### Bookkeeping Obligation Thresholds by Business Type

| Business Type | Simplified Bookkeeping (간편장부) Threshold | Double-Entry Required Above |
|--------------|-------------------------------------------|-----------------------------|
| Agriculture, forestry, fisheries, mining | Prior year revenue below KRW 300,000,000 | KRW 300,000,000 and above |
| Manufacturing, accommodation, food service, construction | Prior year revenue below KRW 150,000,000 | KRW 150,000,000 and above |
| Wholesale/retail, real estate | Prior year revenue below KRW 150,000,000 | KRW 150,000,000 and above |
| Service industries (professional, technical, etc.) | Prior year revenue below KRW 75,000,000 | KRW 75,000,000 and above |
| New businesses (first year) | Simplified allowed regardless of revenue | -- |

### Three Methods of Determining Income [T1]

| Method | Who Can Use | How It Works |
|--------|-------------|--------------|
| Double-entry bookkeeping (복식부기) | Anyone; mandatory above thresholds | Full accrual accounting. Income = Revenue - Documented expenses |
| Simplified bookkeeping (간편장부) | Below threshold businesses | Cash-basis simplified records. Income = Revenue - Documented expenses (simplified format) |
| Standard deduction rate (추계신고) | Businesses failing to keep books | Income = Revenue - (Revenue x standard deduction rate). Penalties apply for not keeping books. |

### Standard Deduction Rates (경비율) [T1/T2]

Two types of standard deduction rates exist:

| Type | Korean | Who Uses It | Rate Source |
|------|--------|-------------|-------------|
| Simple expense rate | 단순경비율 | Small businesses below certain thresholds (generally new or very small) | Published annually by NTS per business code |
| Standard expense rate | 기준경비율 | Businesses above simple rate threshold but not keeping proper books | Published annually by NTS per business code -- MUCH lower than 단순경비율 |

**The rates vary significantly by ATECO-equivalent business classification code (업종코드).** Common examples (indicative):

| Business Type | 단순경비율 (Simple) | 기준경비율 (Standard) |
|---------------|--------------------|-----------------------|
| Software development (722000) | ~64.1% | ~13.5% |
| Business consulting (715000) | ~51.6% | ~16.0% |
| Design services (730000) | ~57.4% | ~14.0% |
| Translation/interpretation (749907) | ~55.0% | ~18.0% |
| Medical practice (851) | ~46.0% | ~11.0% |

[T2] Flag for reviewer: always confirm the exact 업종코드 and verify the current year's published rate from the NTS database.

### Penalty for Not Keeping Books [T1]

If a taxpayer who is required to keep books fails to do so and files using 추계신고:
- **Bookkeeping non-compliance penalty (무기장가산세):** 20% of the tax attributable to the unrecorded income

---

## Step 4: Computing Taxable Income (과세표준) [T1/T2]

**Legislation:** Income Tax Act, Art. 14, 19-21, 27, 43, 45, 47, 50

### Computation Structure

| Step | Description | How to Populate |
|------|-------------|-----------------|
| A | 총수입금액 (Gross revenue) | Total business receipts for the year |
| B | 필요경비 (Necessary expenses) | Documented business expenses (or standard deduction rate amount) |
| C | 사업소득금액 (Business income) | A minus B |
| D | 종합소득금액 (Comprehensive income) | C + other income types (employment, interest, dividends, pension, other) |
| E | 소득공제 (Income deductions) | Personal deductions, pension deductions, special deductions |
| F | 과세표준 (Taxable income) | D minus E |
| G | 산출세액 (Calculated tax) | Apply rate table from Step 1 to F |
| H | 세액공제 (Tax credits) | Child tax credit, standard tax credit, pension contribution credit, etc. |
| I | 결정세액 (Determined tax) | G minus H |
| J | 기납부세액 (Taxes already paid) | 중간예납 + 원천징수 + prepayments |
| K | 납부할 세액 (Tax payable) | I minus J |

---

## Step 5: Income Deductions (소득공제) [T1/T2]

**Legislation:** Income Tax Act, Art. 50-54

### Personal Deductions (인적공제) [T1]

| Deduction | Amount (KRW) | Conditions |
|-----------|-------------|------------|
| Basic deduction (기본공제) -- taxpayer | 1,500,000 | All taxpayers |
| Basic deduction -- spouse | 1,500,000 | If spouse annual income does not exceed KRW 1,000,000 (or KRW 5,000,000 gross employment income) |
| Basic deduction -- dependant (per person) | 1,500,000 | Children under 20, parents aged 60+, siblings aged under 20 or over 60, with income below KRW 1,000,000 |
| Additional -- aged 70+ (경로우대공제) | 1,000,000 per person | For dependants aged 70 or over |
| Additional -- disabled (장애인공제) | 2,000,000 per person | Registered disabled dependants |
| Additional -- single parent (한부모공제) | 1,000,000 | Unmarried with dependant child (cannot combine with 부녀자공제) |
| Additional -- working woman (부녀자공제) | 500,000 | Married woman or single mother with comprehensive income under KRW 30,000,000 |

### Pension Deductions (연금보험료공제) [T1]

| Type | Deduction |
|------|-----------|
| National Pension (국민연금) contributions | Fully deductible |
| Other public pension contributions | Fully deductible |

### Special Deductions for Self-Employed (특별소득공제 equivalent) [T2]

Self-employed individuals claim these as itemised deductions rather than through the simplified system available to employees:

| Item | Deduction / Limit |
|------|-------------------|
| Health insurance (건강보험) premiums paid | Fully deductible |
| Employment insurance (고용보험) premiums | Fully deductible |
| Private pension savings (개인연금저축) | Deductible up to KRW 7,200,000/year (combined with retirement pension) |
| Housing-related deductions | Various -- interest on housing loans, housing subscription savings |
| Small business mutual aid (소기업소상공인 공제부금) | Deductible up to KRW 5,000,000/year |

---

## Step 6: Tax Credits (세액공제) [T1/T2]

**Legislation:** Income Tax Act, Art. 56-59

| Tax Credit | Amount / Rate | Conditions |
|------------|---------------|------------|
| Child tax credit (자녀세액공제) | KRW 150,000 per child (1-2 children); KRW 300,000 for 3rd+ child | Children aged 8-20 (or all ages if disabled) |
| Standard tax credit (표준세액공제) | KRW 70,000 | For those not claiming itemised deductions |
| Retirement pension contribution credit | 12% (or 15% for total income under KRW 55M) of contributions | Up to KRW 9,000,000 contribution (combined IRP + pension) |
| Medical expenses credit (의료비 세액공제) | 15% of expenses exceeding 3% of 총급여 | Capped; 난임시술 = 30%, 미숙아 = 20% |
| Education expenses credit (교육비 세액공제) | 15% of actual expenses | Preschool/elementary/secondary up to KRW 3,000,000/child; university up to KRW 9,000,000/child |
| Donation credit (기부금 세액공제) | 15% (up to KRW 10M) / 30% (above KRW 10M) | Political donations: 100/KRW; statutory/designated donations at applicable rates |
| Insurance premium credit (보험료 세액공제) | 12% of premiums | Up to KRW 1,000,000 in general insurance; KRW 1,000,000 disabled insurance |

**Note:** Self-employed individuals generally claim the standard tax credit (KRW 70,000) OR itemised deductions/credits, not both. [T2] Flag for reviewer: confirm which option is more favourable.

---

## Step 7: Filing Deadlines [T1]

**Legislation:** Income Tax Act, Art. 70, 76

| Filing / Payment | Deadline |
|-----------------|----------|
| 종합소득세 확정신고 (Final return) | 31 May of the following year |
| Extended deadline (with 세무사 / tax agent) | 30 June of the following year |
| 지방소득세 (Local income tax return) | 31 May (same as national) |
| 중간예납 (Estimated tax prepayment) | 30 November (for the current tax year) |
| 원천징수 (Withholding tax) | Monthly -- 10th of the following month |

### Estimated Tax Prepayment (중간예납) [T1]

| Rule | Detail |
|------|--------|
| Amount | 1/2 of prior year's final national income tax |
| Due date | 30 November |
| Exemption | If prior year tax was below KRW 500,000, no prepayment required |
| Adjustment | Cannot be adjusted based on current year estimates -- strictly prior year based |

---

## Step 8: Withholding Tax (원천징수) [T1]

**Legislation:** Income Tax Act, Art. 127, 129, 144-2

| Type of Income | Withholding Rate |
|----------------|-----------------|
| Freelance / independent contractor income (사업소득 -- 인적용역) | 3.3% (3% national + 0.3% local) |
| Interest income | 14% (+ 1.4% local = 15.4%) |
| Dividend income | 14% (+ 1.4% local = 15.4%) |
| Other income (기타소득) | 22% (20% national + 2% local) of 60% of gross (i.e., 8.8% effective if no expenses) |

**For self-employed professionals:** Clients typically withhold 3.3% on payments. This is credited against the final tax liability at year-end filing (Step 4, line J).

---

## Step 9: Penalties [T1]

**Legislation:** Tax Procedures Act (국세기본법), Art. 47-2 to 47-5; Income Tax Act, Art. 81

| Offence | Penalty |
|---------|---------|
| Late filing (무신고가산세) -- no fraud | 20% of tax due |
| Late filing -- fraud | 40% of tax due |
| Underreporting (과소신고가산세) -- no fraud | 10% of understated tax |
| Underreporting -- fraud | 40% of understated tax |
| Late payment (납부불성실가산세) | 0.022% per day (approximately 8% per year) |
| Non-issuance of tax invoice | 2% of supply value |
| Bookkeeping non-compliance (무기장가산세) | 20% of tax on unreported income |

**WARNING:** The late payment penalty of 0.022% per day accumulates quickly and is uncapped. Any arrears situation must be escalated to a qualified 세무사 immediately.

---

## Step 10: Record Keeping [T1]

**Legislation:** Income Tax Act, Art. 160; Tax Procedures Act, Art. 85-2

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 5 years from the filing deadline |
| What to keep | All tax invoices (세금계산서), cash receipts (현금영수증), bank statements, contracts, income tax returns |
| Electronic tax invoices | Mandatory for businesses above certain thresholds |
| Cash receipt system (현금영수증) | Mandatory issuance for consumer-facing businesses; optional but beneficial for B2B |
| Hometax records | NTS maintains digital records of all electronic invoices and cash receipts -- accessible via Hometax |

---

## Step 11: Edge Case Registry

### EC1 -- Freelancer using 단순경비율 when books should be kept [T1]
**Situation:** Software developer with KRW 80,000,000 revenue uses 단순경비율 (simple expense rate) instead of keeping 간편장부.
**Resolution:** Service industry threshold for 간편장부 is KRW 75,000,000. At KRW 80,000,000, the taxpayer exceeds the threshold and MUST keep at least 간편장부 (or 복식부기). Using 추계신고 incurs a 20% 무기장가산세 on top of regular tax. File correctly with bookkeeping records.

### EC2 -- Local income tax omitted [T1]
**Situation:** Client files national 종합소득세 but forgets to file and pay local income tax.
**Resolution:** Local income tax (10% surtax) is a separate obligation filed with the local government. Failure to file incurs separate penalties. File immediately via Wetax (wetax.go.kr).

### EC3 -- 3.3% withholding not credited against final tax [T1]
**Situation:** Freelance translator had KRW 5,000,000 withheld at source (3.3% on KRW 150,000,000 gross). Client does not claim the credit on the final return.
**Resolution:** The 원천징수 amount must be entered on the return as 기납부세액 (taxes already paid). If omitted, the client double-pays. Verify withholding amounts against the 지급명세서 (payment statement) issued by each payer.

### EC4 -- Financial income exceeding KRW 20,000,000 threshold [T2]
**Situation:** Client has KRW 25,000,000 in interest and dividend income in addition to business income.
**Resolution:** When combined financial income (interest + dividends) exceeds KRW 20,000,000, the excess must be included in comprehensive income (종합소득) and taxed at progressive rates instead of the flat 14% withholding. [T2] Flag for reviewer: confirm the global taxation calculation.

### EC5 -- First year of business, no 중간예납 [T1]
**Situation:** New freelancer started in 2025. NTS sends a 중간예납 notice for November 2025.
**Resolution:** First year of business: no prior year tax exists, so 중간예납 should be KRW 0. If NTS sends a notice based on incorrect data, the taxpayer can file an objection or pay KRW 0 with explanation. Full tax is paid with the final return by 31 May 2026.

### EC6 -- Spouse income exceeding dependant threshold [T1]
**Situation:** Client claims spouse as dependant (KRW 1,500,000 기본공제). Spouse earned KRW 6,000,000 from part-time employment.
**Resolution:** Spouse can be claimed as dependant ONLY if their annual income does not exceed KRW 1,000,000 (or KRW 5,000,000 in gross employment income). KRW 6,000,000 gross employment income exceeds the KRW 5,000,000 threshold. Remove the spouse deduction.

### EC7 -- Wrong 업종코드 applied to standard deduction rate [T2]
**Situation:** IT consultant registered under general consulting code but actually provides software development services. The 단순경비율 differs by 12 percentage points.
**Resolution:** The correct 업종코드 determines the applicable standard deduction rate. An incorrect code can significantly over- or under-state deductible expenses. [T2] Flag for reviewer: verify the 업종코드 against the actual nature of services provided and correct if necessary.

### EC8 -- Self-employed taxpayer eligible for retirement pension credit [T2]
**Situation:** Self-employed client contributes KRW 7,000,000 to an IRP (Individual Retirement Pension) and KRW 3,000,000 to a private pension.
**Resolution:** Combined deductible pension contribution capped at KRW 9,000,000 (for income under KRW 120M). Total contributions KRW 10,000,000 exceed cap. Deductible = KRW 9,000,000. Credit = 15% x KRW 9,000,000 = KRW 1,350,000 (if total income under KRW 55M; 12% if above). [T2] Flag for reviewer: confirm income threshold for the higher credit rate.

### EC9 -- Mixed personal and business use of home office [T2]
**Situation:** Freelancer works from home and claims 40% of rent and utilities as business expenses.
**Resolution:** Home office expenses are deductible only to the extent of actual business use. The proportion must be reasonable and documented (dedicated room or measurable workspace percentage). [T2] Flag for reviewer: confirm the business-use percentage is supportable.

### EC10 -- Tax agent extension not properly claimed [T1]
**Situation:** Client assumes they have until 30 June because they hired a 세무사, but the 세무사 did not file the extension request.
**Resolution:** The 30 June deadline applies only when a 세무사 or 공인회계사 is formally engaged and the extension is properly registered with NTS. Without proper registration, the deadline remains 31 May. Late filing penalties apply from 1 June.

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
Action Required: Qualified 세무사 or 공인회계사 must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to 세무사 or 공인회계사. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard self-employed professional, mid-range income, simplified bookkeeping
**Input:** Software developer, revenue KRW 60,000,000, documented expenses KRW 20,000,000 (간편장부), basic deduction KRW 1,500,000 (self only, unmarried), National Pension paid KRW 4,000,000, health insurance KRW 2,000,000, no other income, no withholding.
**Expected output:** Business income = KRW 40,000,000. Comprehensive income = KRW 40,000,000. Deductions: basic KRW 1,500,000 + pension KRW 4,000,000 + health insurance KRW 2,000,000 = KRW 7,500,000. 과세표준 = KRW 32,500,000. National tax = (KRW 32,500,000 x 15%) - KRW 1,260,000 = KRW 3,615,000. Local tax = KRW 361,500. Total = KRW 3,976,500.

### Test 2 -- Higher income, double-entry bookkeeping required
**Input:** Business consultant, revenue KRW 120,000,000, documented expenses KRW 35,000,000 (복식부기). Married with 2 children (ages 10, 14). National Pension KRW 5,400,000, health insurance KRW 3,600,000. No other income. Withholding (원천징수) = KRW 3,960,000.
**Expected output:** Business income = KRW 85,000,000. Deductions: basic self KRW 1,500,000 + spouse KRW 1,500,000 + 2 children KRW 3,000,000 + pension KRW 5,400,000 + health KRW 3,600,000 = KRW 15,000,000. 과세표준 = KRW 70,000,000. National tax = (KRW 70,000,000 x 24%) - KRW 5,760,000 = KRW 11,040,000. Child credit = KRW 300,000 (2 children). Determined tax = KRW 10,740,000. Less withholding KRW 3,960,000. National tax payable = KRW 6,780,000. Local tax = KRW 1,074,000. Total payable = KRW 7,854,000.

### Test 3 -- Low income, effective zero tax
**Input:** Freelance tutor, revenue KRW 15,000,000, documented expenses KRW 5,000,000. Basic deduction KRW 1,500,000, National Pension KRW 1,500,000. No other income.
**Expected output:** Business income = KRW 10,000,000. Deductions = KRW 3,000,000. 과세표준 = KRW 7,000,000. National tax = KRW 7,000,000 x 6% = KRW 420,000. Standard tax credit = KRW 70,000. Determined tax = KRW 350,000. Local tax = KRW 35,000. Total = KRW 385,000.

### Test 4 -- 중간예납 calculation
**Input:** 2024 final national income tax = KRW 8,000,000.
**Expected output:** 중간예납 for November 2025 = KRW 8,000,000 / 2 = KRW 4,000,000. Due 30 November 2025.

### Test 5 -- Standard deduction rate (추계신고) with penalty
**Input:** IT freelancer, revenue KRW 90,000,000, failed to keep books. Service industry threshold = KRW 75,000,000. 기준경비율 = 13.5% (indicative). 주요경비 (major expenses) documented = KRW 30,000,000.
**Expected output:** Income under 기준경비율 = KRW 90,000,000 - KRW 30,000,000 (주요경비) - (KRW 90,000,000 x 13.5%) = KRW 90,000,000 - KRW 30,000,000 - KRW 12,150,000 = KRW 47,850,000. Apply brackets. Additional 무기장가산세 = 20% of tax on unreported income. [T2] Flag for reviewer: confirm 업종코드 and 기준경비율.

### Test 6 -- Withholding credit correctly applied
**Input:** Translator with 5 clients. Total fees received KRW 50,000,000. Total 3.3% withholding = KRW 1,650,000 (KRW 1,500,000 national + KRW 150,000 local). Final national tax = KRW 2,000,000.
**Expected output:** National tax payable = KRW 2,000,000 - KRW 1,500,000 = KRW 500,000. Local tax = KRW 200,000 - KRW 150,000 = KRW 50,000. Total payable = KRW 550,000.

### Test 7 -- Spouse dependant eligibility check
**Input:** Client claims spouse with KRW 4,500,000 gross employment income.
**Expected output:** Spouse qualifies (under KRW 5,000,000 gross employment threshold). Deduction of KRW 1,500,000 allowed.

---

## PROHIBITIONS

- NEVER compute tax without knowing the business type (업종) and bookkeeping method
- NEVER compute final tax figures directly -- pass 과세표준 to the deterministic engine
- NEVER omit local income tax (10% surtax) -- it is a separate but mandatory obligation
- NEVER allow a dependant deduction for a spouse whose income exceeds the threshold
- NEVER use 단순경비율 for taxpayers above the 단순경비율 revenue threshold
- NEVER ignore the 무기장가산세 penalty for taxpayers required to keep books who fail to do so
- NEVER forget to credit 원천징수 (withholding taxes) against the final tax liability
- NEVER assume the 30 June filing extension applies without confirming 세무사 engagement
- NEVER advise on financial income global taxation (interest + dividends exceeding KRW 20M) -- escalate to T2/T3
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their 세무사 for confirmation
- NEVER use prior year's standard deduction rates for the current year without verifying against the NTS published rates

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a 세무사 (tax accountant), 공인회계사 (CPA), or equivalent licensed practitioner in South Korea) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
