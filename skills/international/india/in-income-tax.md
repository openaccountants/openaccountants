---
name: in-income-tax
description: >
  Use this skill whenever asked about Indian income tax for self-employed professionals, freelancers, or sole proprietors. Trigger on phrases like "how much tax do I pay in India", "ITR-4", "ITR-3", "Sugam", "Section 44ADA", "Section 44AD", "presumptive taxation", "new tax regime", "old tax regime", "advance tax India", "TDS credit", "PAN", "80C", "80D", "income tax return India", "surcharge", "health and education cess", or any question about filing or computing income tax for a self-employed individual in India. This skill covers new regime vs old regime rate tables, presumptive taxation (44ADA for professionals, 44AD for business), regular computation (ITR-3), surcharge, cess, standard deduction, Section 80C/80D deductions, advance tax schedule, TDS credits, PAN requirements, and ITR-4 (Sugam) structure. ALWAYS read this skill before touching any Indian income tax work.
version: 1.0
jurisdiction: IN
tax_year: 2025-26
category: international
depends_on:
  - income-tax-workflow-base
---

# India Income Tax -- Self-Employed Professionals & Sole Proprietors Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | India |
| Jurisdiction Code | IN |
| Primary Legislation | Income Tax Act, 1961 (as amended by Finance Act, 2025) |
| Supporting Legislation | Finance Act 2025; CBDT Circulars; Income-tax Rules, 1962 |
| Tax Authority | Central Board of Direct Taxes (CBDT) / Income Tax Department |
| Filing Portal | https://www.incometax.gov.in |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Chartered Accountant (India) |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year | FY 2025-26 (AY 2026-27) |
| Confidence Coverage | Tier 1: rate table application, presumptive profit percentages, cess calculation, advance tax schedule, PAN rules. Tier 2: regime selection optimisation, mixed digital/cash receipt classification, old regime deduction eligibility. Tier 3: NRI taxation, capital gains, partnership firms, transfer pricing, DTAA. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Chartered Accountant must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Residency status** [T1] -- Resident, Resident but Not Ordinarily Resident (RNOR), or Non-Resident. This skill covers Resident individuals only. RNOR/NRI = [T3] escalate.
2. **Age** [T1] -- Below 60, 60-79 (senior citizen), 80+ (super senior citizen). Affects old regime thresholds.
3. **Nature of income** [T1] -- Professional (Section 44ADA eligible) or Business (Section 44AD eligible) or Regular computation (ITR-3).
4. **Gross receipts / turnover** [T1] -- Total receipts in the financial year.
5. **Percentage of digital receipts** [T1] -- What proportion of total receipts was received through banking channels (account payee cheque, bank draft, ECS, UPI, NEFT, RTGS, online transfers)? Determines 44ADA/44AD threshold eligibility.
6. **Tax regime choice** [T1] -- New regime (default from FY 2023-24) or Old regime (must opt in). If not stated, assume new regime.
7. **Employment income, if any** [T1] -- Salary/pension received alongside self-employment income.
8. **TDS credits** [T1] -- TDS deducted by clients (as per Form 26AS / AIS).
9. **Advance tax already paid** [T1] -- Challans paid during the year.
10. **PAN** [T1] -- Confirm PAN is available. Without PAN, TDS is deducted at 20% (Section 206AA).
11. **Deductions claimed (old regime only)** [T2] -- 80C, 80D, 80E, 80G, etc.

**If residency status is unknown or the person is NRI/RNOR, STOP. This skill does not cover non-resident taxation. Escalate to [T3].**

---

## Step 1: Determine Tax Regime [T1/T2]

**Legislation:** Income Tax Act, Section 115BAC (as amended by Finance Act, 2023 and 2025)

### Default Regime

From FY 2023-24 onwards, the **new tax regime is the default**. A taxpayer must explicitly opt out to use the old regime.

- **Self-employed persons (business/profession income):** Must file Form 10-IEA before the due date of the return to opt for the old regime. Once opted out, they can switch back to the new regime only once.
- **Salaried persons (no business income):** Can switch between regimes each year.

### When to Consider Old Regime [T2]

The old regime is beneficial only if the taxpayer has significant deductions (80C, 80D, HRA, home loan interest, etc.) that exceed the benefit of the wider new-regime slabs. Flag for reviewer to confirm regime choice is optimal.

---

## Step 2: New Tax Regime Rate Table -- FY 2025-26 (AY 2026-27) [T1]

**Legislation:** Section 115BAC, as amended by Finance Act, 2025

| Total Income (INR) | Rate | Cumulative Tax at Top of Band |
|---------------------|------|-------------------------------|
| 0 -- 4,00,000 | 0% | 0 |
| 4,00,001 -- 8,00,000 | 5% | 20,000 |
| 8,00,001 -- 12,00,000 | 10% | 60,000 |
| 12,00,001 -- 16,00,000 | 15% | 1,20,000 |
| 16,00,001 -- 20,00,000 | 20% | 2,00,000 |
| 20,00,001 -- 24,00,000 | 25% | 3,00,000 |
| Above 24,00,000 | 30% | -- |

### Section 87A Rebate (New Regime) [T1]

- If total taxable income does not exceed Rs. 12,00,000, the tax payable is reduced by a rebate of up to Rs. 60,000.
- Effective result: individuals with taxable income up to Rs. 12,00,000 pay zero tax.
- For salaried individuals, adding the Rs. 75,000 standard deduction, this means income up to Rs. 12,75,000 is effectively tax-free.

### Standard Deduction (New Regime) [T1]

- Rs. 75,000 standard deduction available from FY 2024-25 onwards (raised from Rs. 50,000).
- Available to salaried employees and pensioners only under the new regime.
- Self-employed professionals with only business/profession income do NOT get the standard deduction.
- If a professional also has salary income, the standard deduction applies to the salary component only.

### Deductions NOT Available Under New Regime [T1]

The following deductions are NOT available if the taxpayer opts for the new regime:

- Section 80C (PPF, ELSS, LIC, etc.)
- Section 80D (health insurance premium)
- Section 80E (education loan interest)
- Section 80G (donations)
- Section 80TTA/80TTB (savings account interest)
- HRA exemption
- LTA exemption
- Home loan interest deduction (Section 24)
- Professional tax deduction

**Only the standard deduction (Rs. 75,000 for salaried) and employer NPS contribution (Section 80CCD(2), up to 14% of salary) are available under the new regime.**

---

## Step 3: Old Tax Regime Rate Table -- FY 2025-26 [T1]

**Legislation:** Income Tax Act, Section 2(9), First Schedule

### Individual Below 60 Years

| Total Income (INR) | Rate | Cumulative Tax at Top of Band |
|---------------------|------|-------------------------------|
| 0 -- 2,50,000 | 0% | 0 |
| 2,50,001 -- 5,00,000 | 5% | 12,500 |
| 5,00,001 -- 10,00,000 | 20% | 1,12,500 |
| Above 10,00,000 | 30% | -- |

### Senior Citizen (60-79 Years)

| Total Income (INR) | Rate | Cumulative Tax at Top of Band |
|---------------------|------|-------------------------------|
| 0 -- 3,00,000 | 0% | 0 |
| 3,00,001 -- 5,00,000 | 5% | 10,000 |
| 5,00,001 -- 10,00,000 | 20% | 1,10,000 |
| Above 10,00,000 | 30% | -- |

### Super Senior Citizen (80+ Years)

| Total Income (INR) | Rate | Cumulative Tax at Top of Band |
|---------------------|------|-------------------------------|
| 0 -- 5,00,000 | 0% | 0 |
| 5,00,001 -- 10,00,000 | 20% | 1,00,000 |
| Above 10,00,000 | 30% | -- |

### Section 87A Rebate (Old Regime) [T1]

- If total taxable income does not exceed Rs. 5,00,000, the tax payable is reduced by a rebate of up to Rs. 12,500.
- Effective result: individuals with taxable income up to Rs. 5,00,000 pay zero tax under the old regime.

### Key Deductions Available Under Old Regime [T1/T2]

| Section | Deduction | Maximum (INR) |
|---------|-----------|---------------|
| 80C | PPF, ELSS, LIC, tuition fees, home loan principal | 1,50,000 |
| 80CCD(1B) | Additional NPS contribution | 50,000 |
| 80D | Health insurance premium (self) | 25,000 (50,000 for senior citizens) |
| 80D | Health insurance premium (parents) | 25,000 (50,000 if parents are senior citizens) |
| 80E | Education loan interest | No limit (full interest for up to 8 years) |
| 80G | Donations to approved funds/charities | 50% or 100% of donation, subject to limits |
| 80TTA | Savings account interest | 10,000 |
| 24(b) | Home loan interest (self-occupied) | 2,00,000 |
| Standard deduction | Salaried employees and pensioners | 50,000 |

[T2] Flag for reviewer: confirm each deduction claimed has supporting documentation and meets eligibility criteria.

---

## Step 4: Presumptive Taxation -- Section 44ADA (Professionals) [T1]

**Legislation:** Income Tax Act, Section 44ADA

### Eligibility [T1]

| Condition | Requirement |
|-----------|-------------|
| Person | Resident individual or partnership firm (NOT LLP) |
| Profession | Must be a profession referred to in Section 44AA(1): legal, medical, engineering, architecture, accountancy, technical consultancy, interior decoration, or other notified professions |
| Gross receipts threshold | Up to Rs. 50,00,000 in the financial year |
| Enhanced threshold | Up to Rs. 75,00,000 if cash receipts do not exceed 5% of total gross receipts (i.e., 95%+ digital receipts) |
| ITR form | ITR-4 (Sugam) |

### Deemed Profit Computation [T1]

- Taxable income is presumed at **50% of gross receipts** -- no need to maintain books of accounts or get audit.
- The taxpayer may declare income higher than 50% but NOT lower. If the taxpayer wants to declare income lower than 50%, they must opt out and file ITR-3 with full books and audit (if turnover exceeds Rs. 50L/75L).

### Example [T1]

| Item | Amount (INR) |
|------|--------------|
| Gross professional receipts | 40,00,000 |
| Deemed profit (50%) | 20,00,000 |
| Less: Deductions (old regime, e.g., 80C: 1,50,000) | 1,50,000 |
| Taxable income | 18,50,000 |

Under new regime (no 80C deduction): taxable income = Rs. 20,00,000.

### Lock-in Rule [T1]

If a taxpayer opts out of presumptive taxation under Section 44ADA, they cannot opt back in for the **next 5 assessment years** following the year they opted out.

---

## Step 5: Presumptive Taxation -- Section 44AD (Business) [T1]

**Legislation:** Income Tax Act, Section 44AD

### Eligibility [T1]

| Condition | Requirement |
|-----------|-------------|
| Person | Resident individual, HUF, or partnership firm (NOT LLP) |
| Business | Any eligible business (NOT profession under 44AA(1)) |
| Turnover threshold | Up to Rs. 2,00,00,000 (Rs. 2 crore) |
| Enhanced threshold | Up to Rs. 3,00,00,000 (Rs. 3 crore) if cash receipts do not exceed 5% of total receipts |
| ITR form | ITR-4 (Sugam) |

### Deemed Profit Rates [T1]

| Receipt Mode | Deemed Profit Rate |
|--------------|-------------------|
| Digital receipts (banking channels: account payee cheque, bank draft, ECS, UPI, NEFT, RTGS) | **6%** of turnover |
| Cash receipts and other modes | **8%** of turnover |

If a business has mixed receipts, apply 6% to the digital portion and 8% to the cash portion.

### Example [T1]

| Item | Amount (INR) |
|------|--------------|
| Total turnover | 1,50,00,000 |
| Digital receipts (90%) | 1,35,00,000 |
| Cash receipts (10%) | 15,00,000 |
| Deemed profit: digital (6%) | 8,10,000 |
| Deemed profit: cash (8%) | 1,20,000 |
| **Total deemed profit** | **9,30,000** |

### Lock-in Rule [T1]

Same as 44ADA: if a taxpayer opts out, they cannot re-enter presumptive taxation for the next **5 assessment years**.

---

## Step 6: Regular Computation -- ITR-3 [T1/T2]

**Legislation:** Income Tax Act, Sections 28-44

### When ITR-3 Applies [T1]

- Taxpayer has business or professional income AND does not opt for presumptive taxation (44AD/44ADA).
- Taxpayer opted out of presumptive taxation.
- Gross receipts exceed the 44AD/44ADA thresholds.
- Taxpayer wants to declare profit below the deemed percentage.

### Computation Steps [T1]

1. **Gross receipts/turnover** -- total business/professional income.
2. **Less: Allowable business expenses** -- expenses incurred wholly and exclusively for the purpose of business/profession (Section 37).
3. **Less: Depreciation** -- per Income Tax Act rates (Section 32).
4. **= Net profit from business/profession.**
5. **Add: Other income** -- salary, house property, capital gains, other sources.
6. **= Gross total income.**
7. **Less: Chapter VI-A deductions** (old regime only) -- 80C, 80D, etc.
8. **= Total taxable income.**
9. **Apply rate table** (new or old regime).
10. **Add: Surcharge** (if applicable).
11. **Add: Health & Education Cess** (4%).
12. **Less: TDS credits, advance tax paid, self-assessment tax paid.**
13. **= Tax payable / refund.**

### Tax Audit Requirement [T1]

| Situation | Audit Required? |
|-----------|----------------|
| Business turnover > Rs. 1 crore (Rs. 10 crore if 95%+ digital transactions) | Yes -- Section 44AB |
| Professional receipts > Rs. 50 lakh | Yes -- Section 44AB |
| Opted out of 44AD/44ADA and income is below deemed percentage | Yes -- Section 44AB |
| Presumptive taxation opted in and within thresholds | No |

[T2] Flag for reviewer: if audit is required, ensure the taxpayer engages a Chartered Accountant and files Form 3CD before the due date (30 September of the assessment year for audit cases).

---

## Step 7: Surcharge [T1]

**Legislation:** Finance Act, 2025

### New Tax Regime Surcharge Rates

| Total Income (INR) | Surcharge Rate |
|---------------------|---------------|
| Up to 50,00,000 | Nil |
| 50,00,001 -- 1,00,00,000 | 10% |
| 1,00,00,001 -- 2,00,00,000 | 15% |
| Above 2,00,00,000 | 25% |

**Maximum surcharge under new regime is capped at 25%.** The 37% rate does NOT apply under the new regime.

### Old Tax Regime Surcharge Rates

| Total Income (INR) | Surcharge Rate |
|---------------------|---------------|
| Up to 50,00,000 | Nil |
| 50,00,001 -- 1,00,00,000 | 10% |
| 1,00,00,001 -- 2,00,00,000 | 15% |
| 2,00,00,001 -- 5,00,00,000 | 25% |
| Above 5,00,00,000 | 37% |

### Marginal Relief [T1]

Surcharge is subject to marginal relief: the total tax (including surcharge) on income exceeding the threshold cannot exceed the tax on income at the threshold plus the amount of income exceeding the threshold.

### Surcharge on Capital Gains [T1]

Surcharge on income chargeable to tax under Sections 111A (short-term capital gains) and 112A (long-term capital gains) is capped at 15% regardless of income level.

---

## Step 8: Health & Education Cess [T1]

**Legislation:** Finance Act, 2018

- **Rate:** 4% on (income tax + surcharge).
- Applies to ALL taxpayers regardless of income level or regime chosen.
- There is no threshold -- cess is payable even on small tax amounts.

### Total Tax Formula [T1]

```
Total Tax = (Income Tax + Surcharge) x 1.04
```

---

## Step 9: Advance Tax Schedule [T1]

**Legislation:** Income Tax Act, Sections 208-211

### Instalment Schedule (Non-Presumptive / Regular)

| Instalment | Due Date | Cumulative % of Tax Liability |
|-----------|----------|-------------------------------|
| 1st | 15 June | 15% |
| 2nd | 15 September | 45% |
| 3rd | 15 December | 75% |
| 4th | 15 March | 100% |

### Presumptive Taxation (44AD / 44ADA) [T1]

Taxpayers under presumptive taxation must pay **100% of advance tax in a single instalment by 15 March**. The quarterly schedule does not apply.

### Exemption from Advance Tax [T1]

- Resident senior citizens (60+) with NO income from business or profession are exempt from advance tax.
- If total tax liability after TDS credits is less than Rs. 10,000, no advance tax is required (Section 208).

### Interest on Default [T1]

| Section | Trigger | Interest Rate |
|---------|---------|--------------|
| 234B | Failure to pay advance tax (paid < 90% of assessed tax) | 1% per month (simple) on shortfall, from April to date of assessment |
| 234C | Deferment of advance tax instalments | 1% per month (simple) on shortfall for 3 months per instalment |

---

## Step 10: TDS Credits [T1]

**Legislation:** Income Tax Act, Sections 190-206

### Common TDS Rates for Professionals/Businesses

| Section | Nature of Payment | TDS Rate |
|---------|------------------|----------|
| 194J | Professional/technical fees | 10% |
| 194C | Contractor payments (individuals/HUF) | 1% |
| 194C | Contractor payments (others) | 2% |
| 194H | Commission/brokerage | 5% |
| 194A | Interest (other than bank) | 10% |
| 194N | Cash withdrawal > Rs. 1 crore | 2% |

### Claiming TDS Credits [T1]

1. Verify TDS deducted matches **Form 26AS** and **Annual Information Statement (AIS)** on the income tax portal.
2. TDS credit is claimed in the ITR against total tax liability.
3. If TDS exceeds tax liability, the excess is refundable.
4. Mismatch between Form 26AS and ITR will result in processing notice under Section 143(1).

### No PAN / Invalid PAN [T1]

If the payee does not furnish PAN, TDS is deducted at the **higher of**:
- Rate specified in the relevant section, or
- 20% (Section 206AA).

---

## Step 11: PAN Requirements [T1]

**Legislation:** Income Tax Act, Section 139A

| Requirement | Detail |
|-------------|--------|
| Mandatory for | Every person whose total income exceeds the basic exemption limit |
| Application form | Form 49A (Indian citizens) / Form 49AA (foreign nationals) |
| Linkage | PAN must be linked to Aadhaar (Section 139AA). Failure to link renders PAN inoperative. |
| Quoting PAN | Mandatory on all ITRs, TDS certificates, challans, and correspondence with the IT Department |
| Penalty for non-compliance | Rs. 10,000 under Section 272B for not obtaining or quoting PAN |

---

## Step 12: ITR-4 (Sugam) Structure [T1]

**Legislation:** Income Tax Rules, 1962; CBDT notification for AY 2026-27

ITR-4 is the simplified return for individuals, HUFs, and firms (not LLP) opting for presumptive taxation.

### Key Schedules in ITR-4

| Schedule | Description | How to Populate |
|----------|-------------|-----------------|
| Part A -- General | Personal details, PAN, Aadhaar, filing status | From client records |
| Part B -- Gross Total Income | Income under all heads | Business income from presumptive schedule + other income |
| Schedule BP | Business/Profession presumptive income | Gross receipts, deemed profit (50%/6%/8%), nature of business code |
| Schedule IT | Advance tax and self-assessment tax | From challans (BSR code, date, amount) |
| Schedule TDS1 | TDS from salary | From Form 16 |
| Schedule TDS2 | TDS on non-salary income | From Form 16A / Form 26AS |
| Part B-TI | Total income computation | Gross total income less Chapter VI-A deductions |
| Part B-TTI | Tax computation | Tax on total income + surcharge + cess - rebate - TDS - advance tax |
| Schedule VI-A | Deductions under Chapter VI-A | 80C, 80D, etc. (old regime only) |
| Verification | Declaration and digital signature | Taxpayer or authorized signatory |

---

## Step 13: Filing Deadlines [T1]

**Legislation:** Income Tax Act, Section 139(1)

| Filing / Payment | Deadline |
|-----------------|----------|
| ITR-4 (Sugam) -- non-audit cases | 31 July of the assessment year |
| ITR-3 -- non-audit cases | 31 July of the assessment year |
| ITR-3 -- audit cases (Section 44AB) | 31 October of the assessment year |
| Tax audit report (Form 3CD) | 30 September of the assessment year |
| Belated return (Section 139(4)) | 31 December of the assessment year |
| Revised return (Section 139(5)) | 31 December of the assessment year |
| Advance tax -- 1st instalment | 15 June |
| Advance tax -- 2nd instalment | 15 September |
| Advance tax -- 3rd instalment | 15 December |
| Advance tax -- 4th instalment | 15 March |
| Advance tax -- presumptive (single instalment) | 15 March |

### Late Filing Fee [T1]

| Situation | Fee (Section 234F) |
|-----------|-------------------|
| Total income > Rs. 5,00,000, filed after due date | Rs. 5,000 |
| Total income <= Rs. 5,00,000, filed after due date | Rs. 1,000 |

---

## Step 14: Edge Case Registry

### EC1 -- Professional receipts partly in cash, partly digital [T1]

**Situation:** A chartered accountant receives Rs. 60,00,000 in gross receipts. Rs. 58,00,000 is through bank transfers, Rs. 2,00,000 in cash. Cash is 3.33% of total (below 5%).
**Resolution:** Enhanced threshold of Rs. 75,00,000 applies. Eligible for Section 44ADA presumptive taxation. Deemed profit = Rs. 30,00,000 (50% of Rs. 60,00,000). File ITR-4.

### EC2 -- Cash receipts exceed 5% threshold [T1]

**Situation:** A doctor receives Rs. 55,00,000 gross receipts. Rs. 48,00,000 is digital, Rs. 7,00,000 is cash. Cash is 12.7% of total (exceeds 5%).
**Resolution:** Enhanced threshold does NOT apply. Standard threshold of Rs. 50,00,000 applies. Since receipts exceed Rs. 50,00,000, the doctor cannot use Section 44ADA. Must file ITR-3 with regular books of accounts. Tax audit required if receipts exceed Rs. 50,00,000.

### EC3 -- Declaring profit below 50% under 44ADA [T1]

**Situation:** A freelance consultant with Rs. 30,00,000 receipts has actual expenses of Rs. 20,00,000 (profit only Rs. 10,00,000 vs deemed Rs. 15,00,000).
**Resolution:** Cannot declare below 50% under 44ADA. Options: (a) accept Rs. 15,00,000 deemed profit and stay on presumptive, or (b) opt out of 44ADA, file ITR-3 with full books, get tax audit, and declare actual Rs. 10,00,000 profit. But opting out triggers 5-year lock-out from presumptive. [T2] Flag for reviewer to advise.

### EC4 -- Section 87A rebate with marginal income [T1]

**Situation:** A professional under the new regime has taxable income of Rs. 12,10,000.
**Resolution:** Since taxable income exceeds Rs. 12,00,000, the Section 87A rebate does NOT apply. Full tax is computed on Rs. 12,10,000. Tax = Rs. 60,000 + (10,000 x 15%) = Rs. 61,500. Note the cliff effect: Rs. 12,00,000 income = zero tax; Rs. 12,10,000 income = Rs. 61,500 tax. [T2] Flag for reviewer: advise client on maximising deductions or contributions to bring income to Rs. 12,00,000 or below.

### EC5 -- Mixed business and professional income [T2]

**Situation:** A person runs a consulting practice (profession, 44ADA eligible) and also has a retail business (business, 44AD eligible).
**Resolution:** Both presumptive sections can apply simultaneously if each stream independently meets its threshold. Professional income: 50% deemed profit. Business income: 6%/8% deemed profit. Both reported in ITR-4 under separate Schedule BP entries. [T2] Flag for reviewer to confirm both activities qualify independently.

### EC6 -- Old regime chosen but deductions are minimal [T2]

**Situation:** A taxpayer with Rs. 15,00,000 income opts for old regime but only has Rs. 80,000 in 80C deductions.
**Resolution:** New regime is almost certainly more beneficial. Under old regime: taxable income = Rs. 14,20,000, tax = Rs. 12,500 + Rs. 1,00,000 + Rs. 1,26,000 = Rs. 2,38,500. Under new regime: taxable income = Rs. 15,00,000, tax = Rs. 20,000 + Rs. 40,000 + Rs. 45,000 = Rs. 1,05,000. New regime saves Rs. 1,33,500 before cess. [T2] Flag for reviewer to confirm regime switch.

### EC7 -- Advance tax not paid by presumptive taxpayer [T1]

**Situation:** A 44ADA professional with Rs. 25,00,000 receipts did not pay advance tax by 15 March.
**Resolution:** Interest under Section 234C applies at 1% per month on the shortfall for one month (since presumptive taxpayers have a single 15 March deadline). Interest under 234B also applies from April until assessment. Both must be computed and paid as self-assessment tax before filing.

### EC8 -- TDS mismatch with Form 26AS [T1]

**Situation:** Client's books show Rs. 3,50,000 TDS deducted, but Form 26AS shows only Rs. 2,80,000.
**Resolution:** Only claim TDS credit per Form 26AS (Rs. 2,80,000). For the missing Rs. 70,000, the client must follow up with the deductor to file/correct their TDS return. Claiming excess TDS will result in a demand notice under Section 143(1).

### EC9 -- PAN not linked to Aadhaar [T1]

**Situation:** Client has a valid PAN but has not linked it to Aadhaar.
**Resolution:** PAN becomes inoperative. Consequences: (a) cannot file ITR, (b) TDS deducted at higher rate (Section 206AA), (c) pending refunds will not be processed. Client must link PAN-Aadhaar immediately (with late fee of Rs. 1,000 under Section 234H).

### EC10 -- Salary income alongside professional income under new regime [T1]

**Situation:** A software developer earns Rs. 8,00,000 salary and Rs. 20,00,000 professional receipts. Opts for new regime.
**Resolution:** Salary: Rs. 8,00,000 less Rs. 75,000 standard deduction = Rs. 7,25,000. Professional income (44ADA): Rs. 10,00,000 (50% of Rs. 20,00,000). Total income = Rs. 17,25,000. Apply new regime slabs. Standard deduction applies only to salary portion. No 80C/80D deductions under new regime.

---

## Step 15: Full Computation Walkthrough Template [T1]

```
INCOME TAX COMPUTATION -- FY 2025-26 (AY 2026-27)
Regime: [New / Old]

A. Income from Business/Profession
   Gross Receipts:                          ___________
   Deemed Profit (44ADA: 50% / 44AD: 6%/8%): ___________
   OR Net Profit (ITR-3, if regular):        ___________

B. Income from Salary (if any)
   Gross Salary:                             ___________
   Less: Standard Deduction:                 (___________) [75,000 new / 50,000 old]
   Net Salary:                               ___________

C. Income from Other Sources
   Interest / Dividends / Other:             ___________

D. Gross Total Income (A + B + C):           ___________

E. Less: Chapter VI-A Deductions (Old Regime Only)
   Section 80C:                              (___________) [max 1,50,000]
   Section 80D:                              (___________) [max 25,000/50,000]
   Section 80CCD(1B):                        (___________) [max 50,000]
   Other:                                    (___________)
   Total Deductions:                         (___________)

F. Total Taxable Income (D - E):             ___________

G. Income Tax (per slab):                    ___________
H. Less: Section 87A Rebate:                 (___________)
I. Tax after Rebate:                         ___________
J. Add: Surcharge:                           ___________
K. Tax + Surcharge:                          ___________
L. Add: Health & Education Cess (4%):        ___________
M. Total Tax Liability (K + L):             ___________

N. Less: Advance Tax Paid:                   (___________)
O. Less: TDS Credits (per Form 26AS):        (___________)
P. Less: Self-Assessment Tax Paid:           (___________)

Q. Tax Payable / (Refund) (M - N - O - P):  ___________
```

---

## Step 16: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Chartered Accountant must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Chartered Accountant. Document gap.
```

---

## Step 17: Test Suite

### Test 1 -- Professional, new regime, presumptive (44ADA), mid-range income

**Input:** Resident individual, age 35, freelance software consultant (44ADA eligible), gross receipts Rs. 40,00,000 (100% digital), new regime, no salary, TDS per 26AS Rs. 4,00,000 (194J @ 10%), no advance tax paid, no other income.
**Expected output:**
- Deemed profit = Rs. 20,00,000 (50%)
- No deductions (new regime)
- Taxable income = Rs. 20,00,000
- Tax: 0 + 20,000 + 40,000 + 60,000 + 80,000 = Rs. 2,00,000
- 87A rebate: Nil (income > 12L)
- Surcharge: Nil (income <= 50L)
- Cess: Rs. 2,00,000 x 4% = Rs. 8,000
- Total tax: Rs. 2,08,000
- Less TDS: Rs. 4,00,000
- **Refund: Rs. 1,92,000**

### Test 2 -- Professional, old regime, presumptive (44ADA), with deductions

**Input:** Resident individual, age 42, architect, gross receipts Rs. 30,00,000 (100% digital), old regime elected, 80C: Rs. 1,50,000, 80D: Rs. 25,000, no salary, TDS Rs. 3,00,000, advance tax Rs. 0.
**Expected output:**
- Deemed profit = Rs. 15,00,000 (50%)
- Less 80C: Rs. 1,50,000, Less 80D: Rs. 25,000
- Taxable income = Rs. 13,25,000
- Tax (old regime, below 60): 0 + 12,500 + 1,00,000 + (3,25,000 x 30%) = Rs. 12,500 + Rs. 1,00,000 + Rs. 97,500 = Rs. 2,10,000
- 87A rebate: Nil (income > 5L)
- Surcharge: Nil
- Cess: Rs. 2,10,000 x 4% = Rs. 8,400
- Total tax: Rs. 2,18,400
- Less TDS: Rs. 3,00,000
- **Refund: Rs. 81,600**

### Test 3 -- Business, presumptive (44AD), mixed digital/cash receipts

**Input:** Resident individual, age 50, retail trader, turnover Rs. 1,00,00,000. Digital receipts Rs. 85,00,000, cash receipts Rs. 15,00,000. New regime. No TDS. Advance tax paid Rs. 1,00,000.
**Expected output:**
- Deemed profit: (85,00,000 x 6%) + (15,00,000 x 8%) = Rs. 5,10,000 + Rs. 1,20,000 = Rs. 6,30,000
- Taxable income = Rs. 6,30,000
- Tax (new regime): 0 + 20,000 + (2,30,000 x 10%) = Rs. 20,000 + Rs. 23,000 = Rs. 43,000
- 87A rebate: Nil (income > 12L? No, 6.3L < 12L, rebate applies) -- Tax = 0 after rebate (wait: 6,30,000 < 12,00,000 so rebate up to Rs. 60,000 applies; tax Rs. 43,000 fully offset)
- Tax after rebate: Rs. 0
- Cess: Rs. 0
- Total tax: Rs. 0
- Less advance tax: Rs. 1,00,000
- **Refund: Rs. 1,00,000**

### Test 4 -- High-income professional with surcharge, new regime

**Input:** Resident individual, age 45, management consultant, gross receipts Rs. 1,20,00,000 (100% digital), 44ADA eligible (under Rs. 75L? No -- Rs. 1.2 crore exceeds Rs. 75L). Must file ITR-3 with regular computation. Actual net profit Rs. 80,00,000. New regime. TDS Rs. 12,00,000. No advance tax.
**Expected output:**
- Cannot use 44ADA (receipts exceed Rs. 75,00,000)
- Net profit from ITR-3: Rs. 80,00,000
- Tax (new regime): 0 + 20,000 + 40,000 + 60,000 + 80,000 + 1,00,000 + (56,00,000 x 30%) = Rs. 3,00,000 + Rs. 16,80,000 = Rs. 19,80,000
- Surcharge: 10% (income between 50L-1Cr) = Rs. 1,98,000
- Tax + surcharge: Rs. 21,78,000
- Cess: Rs. 21,78,000 x 4% = Rs. 87,120
- Total tax: Rs. 22,65,120
- Less TDS: Rs. 12,00,000
- **Tax payable: Rs. 10,65,120**
- Interest under 234B/234C will also apply for non-payment of advance tax.

### Test 5 -- Section 87A cliff effect, new regime

**Input:** Resident individual, age 30, freelance graphic designer (44ADA), gross receipts Rs. 24,50,000 (100% digital), new regime. No TDS. No advance tax.
**Expected output:**
- Deemed profit = Rs. 12,25,000 (50%)
- Taxable income = Rs. 12,25,000
- Income exceeds Rs. 12,00,000, so 87A rebate does NOT apply
- Tax: 0 + 20,000 + 40,000 + (25,000 x 15%) = Rs. 60,000 + Rs. 3,750 = Rs. 63,750
- Cess: Rs. 63,750 x 4% = Rs. 2,550
- Total tax: Rs. 66,300
- **Tax payable: Rs. 66,300**
- Flag: advise client that reducing receipts by Rs. 50,000 (or increasing business expenditure under ITR-3) would result in zero tax.

### Test 6 -- Senior citizen, old regime, below threshold

**Input:** Resident senior citizen (age 65), retired doctor with consulting income Rs. 5,50,000, old regime, 80C: Rs. 1,50,000, 80D: Rs. 50,000 (senior citizen limit).
**Expected output:**
- Deemed profit (44ADA): Rs. 2,75,000 (50%)
- Less 80C: Rs. 1,50,000, Less 80D: Rs. 50,000
- Taxable income = Rs. 75,000
- Old regime senior citizen: 0% up to Rs. 3,00,000
- Rs. 75,000 is below Rs. 3,00,000 threshold
- **Tax payable: Rs. 0**

### Test 7 -- Advance tax interest calculation (presumptive taxpayer)

**Input:** 44ADA professional, total tax liability Rs. 3,00,000. Advance tax of Rs. 3,00,000 should have been paid by 15 March but was paid on 15 May (2 months late).
**Expected output:**
- Section 234C interest: 1% x Rs. 3,00,000 x 1 month = Rs. 3,000 (for missing the March 15 deadline).
- Section 234B interest: 1% x Rs. 3,00,000 x 2 months (April, May) = Rs. 6,000.
- Total interest: Rs. 9,000.
- Must be paid as self-assessment tax before filing.

---

## PROHIBITIONS

- NEVER compute tax without confirming the tax regime (new or old). If not stated, apply the new regime as the default.
- NEVER apply old regime deductions (80C, 80D, etc.) under the new regime.
- NEVER allow a 44ADA professional to declare profit below 50% of gross receipts without opting out to ITR-3.
- NEVER allow a 44AD business to declare profit below 6%/8% of turnover without opting out to ITR-3.
- NEVER apply the Rs. 75,00,000 enhanced threshold for 44ADA if cash receipts exceed 5% of total receipts -- the limit drops to Rs. 50,00,000.
- NEVER apply the Rs. 3,00,00,000 enhanced threshold for 44AD if cash receipts exceed 5% of total receipts -- the limit drops to Rs. 2,00,00,000.
- NEVER apply the Section 87A rebate if taxable income exceeds Rs. 12,00,000 (new regime) or Rs. 5,00,000 (old regime).
- NEVER apply the 37% surcharge rate under the new regime -- maximum surcharge is 25%.
- NEVER forget Health & Education Cess (4%) -- it applies on top of income tax plus surcharge in all cases.
- NEVER claim TDS credit exceeding the amount shown in Form 26AS / AIS.
- NEVER advise a taxpayer to opt out of presumptive taxation without warning about the 5-year lock-out.
- NEVER present tax calculations as definitive -- always label as estimated and direct the client to their Chartered Accountant for confirmation.
- NEVER advise on NRI taxation, capital gains, partnership firms, or transfer pricing under this skill -- escalate to [T3].

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a Chartered Accountant, tax attorney, or equivalent licensed practitioner in India) before filing or acting upon.

Tax laws in India are subject to frequent amendment by Finance Acts and CBDT notifications. Users must verify all rates, thresholds, and rules against the latest applicable Finance Act and official CBDT circulars for the relevant assessment year.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
