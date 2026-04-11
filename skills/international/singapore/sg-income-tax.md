---
name: sg-income-tax
description: Use this skill whenever asked about Singapore income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay in Singapore", "Form B", "Form B1", "IRAS income tax", "trade income", "capital allowances Singapore", "personal reliefs", "tax residence 183 days", "Section 10(1)(a)", "CPF self-employed", "self-employed tax Singapore", or any question about filing or computing income tax for a Singapore sole proprietor or freelancer. Also trigger when preparing or reviewing a Form B/B1, computing trade income, or advising on personal reliefs and capital allowances. This skill covers progressive rates (0--24%), trade income computation, capital allowances (Section 19/19A), approved deductions, personal reliefs, tax residence rules, filing deadlines, and penalties. ALWAYS read this skill before touching any Singapore income tax work.
---

# Singapore Income Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Singapore |
| Jurisdiction Code | SG |
| Primary Legislation | Income Tax Act 1947 (ITA) |
| Supporting Legislation | Economic Expansion Incentives (Relief from Income Tax) Act; Income Tax (Approved Donations) Regulations |
| Tax Authority | Inland Revenue Authority of Singapore (IRAS) |
| Filing Portal | myTax Portal (mytax.iras.gov.sg) via Singpass |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Singapore-licensed tax practitioner or Accredited Tax Adviser |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Tax Year Coverage | Year of Assessment (YA) 2025 (income earned in calendar year 2024) and YA 2026 (income earned in 2025) |
| Confidence Coverage | Tier 1: rate table application, personal relief amounts, capital allowance rates, filing deadlines, penalty rates. Tier 2: mixed-use expense apportionment, home office deductions, capital vs revenue distinction, NOR scheme (expired). Tier 3: international income, transfer pricing, partnership allocations, corporate structures, GST interaction for GST-registered persons. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Accredited Tax Adviser must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Tax residence status** [T1] -- Singapore tax resident (citizen/PR residing in Singapore, or physically present/employed for 183+ days in the calendar year) or non-resident. Determines which rate table applies.
2. **Year of Assessment (YA)** [T1] -- Singapore taxes on a preceding year basis. YA 2026 = income earned in calendar year 2025.
3. **Nature of self-employment** [T1] -- sole proprietor, freelancer, partner in a partnership, or commission agent.
4. **Gross trade income** [T1] -- total revenue from trade, business, profession, or vocation (Section 10(1)(a)).
5. **Business expenses** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items).
6. **Capital assets acquired in the year** [T1] -- type, cost, date first used in business.
7. **Other income** [T1] -- employment income, rental income, interest, dividends (note: Singapore dividends are generally exempt under one-tier system).
8. **Personal circumstances** [T1] -- age, marital status, number of children, CPF contributions, dependants.
9. **GST registration status** [T1] -- GST-registered (turnover exceeds SGD 1 million or voluntarily registered) or not.

**If tax residence status is unknown, STOP. Do not apply a rate table. Tax residence status is mandatory.**

---

## Step 1: Determine Tax Residence [T1]

**Legislation:** ITA, Section 2; IRAS guidelines

### Tax Resident Criteria

| Criterion | Detail |
|-----------|--------|
| Singapore citizen or PR | Residing in Singapore (except for temporary absences) |
| Foreigner | Physically present or employed in Singapore for 183 days or more in the calendar year |
| Continuous period straddling two years | If present for a continuous period of at least 183 days straddling two calendar years, resident for both years |
| Foreigner working in Singapore for 3 consecutive years | Tax resident for all 3 years even if less than 183 days in the first/last year |

### Non-Resident Treatment

| Duration | Treatment |
|----------|-----------|
| 0 -- 60 days | Income exempt from tax (unless director, public entertainer, or specific exceptions) |
| 61 -- 182 days | Flat 15% on employment income or resident rates, whichever is higher |
| 183+ days | Tax resident -- progressive rates apply |

**This skill covers TAX RESIDENTS only. Non-resident computations are [T3] -- escalate.**

---

## Step 2: Progressive Tax Rate Table -- Resident Individuals [T1]

**Legislation:** ITA, Section 43(1) and Third Schedule

### YA 2025 and YA 2026 Rates (Income Earned in 2024/2025)

| Chargeable Income (SGD) | Rate | Gross Tax Payable (Cumulative) |
|------------------------|------|-------------------------------|
| First 20,000 | 0% | 0 |
| Next 10,000 (20,001 -- 30,000) | 2% | 200 |
| Next 10,000 (30,001 -- 40,000) | 3.5% | 550 |
| Next 40,000 (40,001 -- 80,000) | 7% | 3,350 |
| Next 40,000 (80,001 -- 120,000) | 11.5% | 7,950 |
| Next 40,000 (120,001 -- 160,000) | 15% | 13,950 |
| Next 40,000 (160,001 -- 200,000) | 18% | 21,150 |
| Next 40,000 (200,001 -- 240,000) | 19% | 28,750 |
| Next 40,000 (240,001 -- 280,000) | 19.5% | 36,550 |
| Next 40,000 (280,001 -- 320,000) | 20% | 44,550 |
| In excess of 320,000 | 22% | -- |

### YA 2025 Personal Income Tax Rebate [T1]

| Item | Detail |
|------|--------|
| Rebate | 60% of tax payable |
| Cap | SGD 200 |
| Applies to | YA 2025 only (income earned in 2024) |

**From YA 2024 onwards, a new top marginal rate of 24% applies to chargeable income above SGD 1,000,000:**

| Chargeable Income (SGD) | Rate |
|------------------------|------|
| 500,001 -- 1,000,000 | 23% |
| Above 1,000,000 | 24% |

**NEVER compute tax figures directly -- pass chargeable income to the deterministic engine to apply the rate table.**

---

## Step 3: Trade Income Computation -- Section 10(1)(a) [T1]

**Legislation:** ITA, Section 10(1)(a), Sections 14--15

### Computation Structure

| Step | Description | How to Populate |
|------|-------------|-----------------|
| A | Gross revenue / turnover | Total invoiced/received from trade, business, profession, or vocation |
| B | Less: Allowable business expenses | Expenses wholly and exclusively incurred in the production of income (Section 14) |
| C | Add: Balancing charges | Proceeds on disposal of assets exceeding tax written-down value |
| D | Less: Capital allowances | Section 19/19A depreciation (Step 4) |
| E | Adjusted trade income | A minus B plus C minus D |
| F | Less: Approved donations | Donations to approved IPCs (250% deduction for cash donations) |
| G | Less: Current year losses | Losses from other trade sources (if any) |
| H | Assessable income | E minus F minus G |
| I | Less: Personal reliefs | Reliefs from Step 5 |
| J | Chargeable income | H minus I |
| K | Gross tax | Apply rate table from Step 2 to J |
| L | Less: Tax rebates | YA 2025: 60% rebate capped at SGD 200 |
| M | Net tax payable | K minus L |

---

## Step 4: Capital Allowances [T1]

**Legislation:** ITA, Sections 19, 19A, 19B

### 4a. Section 19 -- Standard Write-Off [T1]

| Item | Detail |
|------|--------|
| Basis | Cost of plant and machinery used for the purpose of trade |
| Write-off period | Over the prescribed working life of the asset (6, 12, or 16 years) |
| Initial allowance | 20% of cost in the year of acquisition (one-time) |
| Annual allowance | Remaining 80% spread equally over the prescribed working life |

### Prescribed Working Life

| Asset Category | Working Life | Annual Allowance (after IA) |
|---------------|-------------|---------------------------|
| Computers | 6 years | 13.33% of cost per year |
| Motor vehicles | 6 years | 13.33% of cost per year |
| Office equipment | 6 years | 13.33% of cost per year |
| Office furniture | 6 years | 13.33% of cost per year |
| Renovation/refurbishment | 3 years (Section 14Q) | 33.33% per year (capped at SGD 300,000 per 3-year period) |

### 4b. Section 19A -- Accelerated Write-Off [T1]

| Option | Write-Off |
|--------|-----------|
| One-year write-off | 100% in the YA relating to the basis period in which the asset was acquired |
| Three-year write-off | 75% in Year 1, 25% in Year 2 (for YA 2024 expenditure); or 33.33% per year over 3 years |

- Election under Section 19A is irrevocable once made for a particular YA
- Applies to all qualifying assets acquired in that basis period -- cannot cherry-pick

### 4c. Low-Value Assets -- Section 19A(10A) [T1]

| Rule | Detail |
|------|--------|
| Qualifying cost | Below SGD 5,000 per asset |
| Write-off | 100% in the year of acquisition |
| Annual cap | SGD 30,000 total per YA for all low-value assets |
| Excess | Assets exceeding the SGD 30,000 cap are written off under Section 19 or 19A |

### 4d. Balancing Adjustments [T1/T2]

| Scenario | Treatment |
|----------|-----------|
| Sale proceeds > tax written-down value | Balancing charge (taxable -- added back to income) |
| Sale proceeds < tax written-down value | Balancing allowance (deductible) |
| [T2] | Flag for reviewer if disposal is to a related party -- market value rules may apply |

---

## Step 5: Personal Reliefs [T1]

**Legislation:** ITA, Sections 36--40

### Relief Cap [T1]

**Total personal reliefs are capped at SGD 80,000 per YA.**

### Relief Table (YA 2025/2026)

| Relief | Amount (SGD) | Conditions |
|--------|-------------|------------|
| Earned income relief (below age 55) | Lower of actual earned income or 1,000 | Automatically applied |
| Earned income relief (age 55--59) | Lower of actual earned income or 6,000 | Automatically applied |
| Earned income relief (age 60+) | Lower of actual earned income or 8,000 | Automatically applied |
| Spouse/handicapped spouse relief | 2,000 / 5,500 | Spouse income not exceeding SGD 4,000 in the year; married/maintained/lived with taxpayer |
| Qualifying child relief (QCR) | 4,000 per child | Child under 16, or in full-time education; child's income not exceeding SGD 8,000 |
| Handicapped child relief | 7,500 per child | Instead of QCR |
| Working mother's child relief (WMCR) | 15% of earned income for 1st child, 20% for 2nd, 25% for 3rd and subsequent | Only for working mothers; married, divorced, or widowed |
| QCR + WMCR combined cap | 50,000 per child | Cannot exceed SGD 50,000 per child |
| Parent/handicapped parent relief | 9,000 / 14,000 | Parent resident in Singapore, maintained by taxpayer, parent income not exceeding SGD 4,000 |
| Grandparent caregiver relief | 3,000 | For working mothers; grandparent/grandparent-in-law cares for child |
| CPF relief (employee/self-employed) | Mandatory CPF contributions | Up to the CPF contribution cap (SGD 6,300/month or SGD 37,740/year for employees in 2025) |
| CPF cash top-up relief | Up to 8,000 (own) + 8,000 (family) | Cash top-ups to CPF Special/Retirement/MediSave accounts |
| SRS relief (Supplementary Retirement Scheme) | Up to 15,300 (citizens/PRs) or 35,700 (foreigners) | Contributions to SRS account |
| Life insurance relief | Lower of premiums paid or SGD 5,000 | Only if CPF contributions are less than SGD 5,000; rare for self-employed |
| Course fees relief | Up to 5,500 | Fees for approved courses for self, to gain skills relevant to employment/business |
| NSman relief (self) | 3,000 / 1,500 (key appointment / non-key) | For NSmen who performed NS activities |
| Donations to approved IPCs | 250% of donation amount | Approved institutions of public character; deducted from assessable income, not as a personal relief |

### CPF for Self-Employed Persons [T1]

| Item | Detail |
|------|--------|
| Mandatory contribution | MediSave contributions only (based on net trade income) |
| Voluntary contribution | Can make voluntary CPF contributions to Ordinary/Special accounts |
| MediSave contribution rates | Tiered based on age and net trade income -- consult IRAS/CPF tables |
| Tax deduction | Mandatory MediSave contributions are deductible as a personal relief |
| [T2] | Flag if client's MediSave contributions are unclear -- verify with CPF statement |

---

## Step 6: Approved Deductions -- Business Expenses [T1/T2]

**Legislation:** ITA, Sections 14--15

### The Test [T1]

An expense is deductible under Section 14 only if it is wholly and exclusively incurred in the production of income. If an expense is incurred partly for business and partly for private purposes, only the business portion is deductible.

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Rent for business premises | T1 | Fully deductible |
| Professional indemnity insurance | T1 | Fully deductible |
| Accounting / tax agent fees | T1 | Fully deductible |
| Office supplies / stationery | T1 | Fully deductible |
| Software subscriptions | T1 | Fully deductible (if not capitalised) |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Staff costs (salaries, CPF contributions) | T1 | Fully deductible |
| Transport / travel (business purpose) | T1 | Fully deductible |
| Telephone / internet (business portion) | T2 | Apportion if mixed use |
| Business entertainment | T1 | Deductible if incurred for income production; keep records of purpose, persons, amounts |
| Bad debts (trade debts written off) | T2 | Deductible if previously included in income and genuinely irrecoverable |
| Motor vehicle expenses | T2 | See motor vehicle rules below |
| Home office expenses | T2 | See home office rules below |

### NOT Deductible (Section 15) [T1]

| Expense | Reason |
|---------|--------|
| Domestic or private expenses | Section 15(1)(a) |
| Capital expenditure (unless through capital allowances) | Section 15(1)(c) |
| Income tax itself | Section 15(1)(d) |
| Any sum recoverable under insurance or indemnity | Section 15(1)(e) |
| Fines and penalties for law violations | Not incurred in production of income |
| Provisions and reserves (unrealised losses) | Not actually incurred |
| Drawings / personal withdrawals | Not an expense |
| Private motor vehicle depreciation (S-plated cars for individuals) | Private cars are not deductible |

### Home Office Rules [T2]

- IRAS does not have a blanket home office deduction scheme for self-employed
- Expenses such as additional electricity, internet (business portion) may be claimed if the home is used as a place of business
- Must apportion reasonably between business and private use
- [T2] Flag for reviewer: confirm apportionment basis and documentation

### Motor Vehicle Rules [T2]

| Vehicle Type | Treatment |
|-------------|-----------|
| Commercial vehicle (goods vehicle, van) | Running costs deductible; capital allowances claimable |
| Private car (S-plated) | Running costs for business use may be claimed (petrol, parking, ERP); capital allowances NOT claimable for private cars |
| Motor vehicle lease/rental | Deductible if used for business |
| [T2] | Flag for reviewer: confirm business vs private use percentage and vehicle classification |

---

## Step 7: Not Ordinarily Resident (NOR) Scheme [T1]

**Legislation:** ITA; IRAS administrative concession

**The NOR scheme has been abolished.** The scheme was phased out after YA 2020 for new applicants. Existing NOR taxpayers were allowed to retain the status until YA 2024. From YA 2025 onwards, the NOR scheme is no longer available.

| Rule | Detail |
|------|--------|
| New applications | NOT accepted from YA 2021 onwards |
| Existing NOR status | Expired after YA 2024 |
| Employer overseas pension contributions | Fully taxable from YA 2025 (no more partial exemption) |
| Impact | Former NOR taxpayers are now taxed as regular tax residents |

**Do not apply NOR concessions for YA 2025 or later. If a client asks about NOR, confirm it is expired.**

---

## Step 8: Filing Deadlines [T1]

**Legislation:** ITA; IRAS administrative guidelines

| Filing / Payment | Deadline |
|-----------------|----------|
| Form B / Form B1 (individual income tax return) | 18 April of the YA (e.g., 18 April 2025 for YA 2025) |
| Paper filing | 15 April of the YA |
| Filing opens | 1 March of the YA |
| Payment of tax | Within 1 month of Notice of Assessment (NOA) |
| GIRO instalment plan | 12 monthly interest-free instalments if on GIRO; apply by specified date |

### Who Must File [T1]

| Scenario | Must File? |
|----------|-----------|
| Self-employed with net trade income | YES -- File Form B |
| Annual income exceeds SGD 22,000 | YES |
| Annual income SGD 22,000 or below and no other income | May not need to file, but IRAS may still issue a filing requirement |
| Received a letter/SMS/notification from IRAS to file | YES -- must file regardless of income level |
| Non-resident with Singapore-source income | YES -- File Form M |

### Form B vs Form B1 [T1]

| Form | Who Files |
|------|-----------|
| Form B | Self-employed individuals (sole proprietors, partners, commission agents) |
| Form B1 | Employed individuals with no self-employment income |

---

## Step 9: Penalties [T1]

**Legislation:** ITA, Sections 93, 94, 95, 96

| Offence | Penalty |
|---------|---------|
| Late filing | Fine of SGD 200 -- SGD 1,000 per offence |
| Non-filing (estimated assessment issued) | IRAS issues estimated NOA based on available info; 5% penalty on tax owed |
| Failure to file after court summons | Fine up to SGD 1,000; in default, imprisonment up to 6 months |
| Incorrect return (without reasonable excuse) | Penalty up to 200% of tax undercharged |
| Wilful tax evasion (Section 96) | Fine up to SGD 50,000 and/or imprisonment up to 3 years; penalty up to 400% of tax undercharged |
| Late payment of tax | 5% penalty imposed on tax remaining unpaid after 30 days from NOA due date; additional 1% per month thereafter (capped at 12%) |

**WARNING:** IRAS issues estimated assessments (estimated NOAs) for non-filers. These estimates are often higher than actual tax liability. The taxpayer must still file a return to revise the estimate or face paying the estimated amount.

---

## Step 10: Record Keeping [T1]

**Legislation:** ITA, Section 67

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 5 years from the relevant YA |
| What to keep | All sales invoices, purchase invoices, bank statements, receipts, contracts, capital asset register, CPF statements |
| Format | Paper or digital (IRAS accepts digital records) |
| Business records | Revenue records, expense receipts, bank statements, loan agreements, asset purchase records |
| Failure to keep records | Fine up to SGD 1,000 and/or imprisonment up to 6 months |

---

## Step 11: Edge Case Registry

### EC1 -- GST included in revenue [T1]
**Situation:** GST-registered sole proprietor invoices SGD 10,700 (SGD 10,000 + SGD 700 GST at 9%). Client reports SGD 10,700 as gross trade income.
**Resolution:** Gross trade income must be SGD 10,000 only. GST collected is a liability to IRAS, not income. For non-GST-registered persons, the full amount received IS revenue (no GST to exclude).

### EC2 -- Private car expenses [T1]
**Situation:** Self-employed person uses a private S-plated car for business. Claims depreciation and all running costs.
**Resolution:** Capital allowances on private cars are NOT deductible. Running costs (petrol, parking, ERP) for documented business trips are deductible. Insurance and road tax are private expenses unless the car is a commercial vehicle. [T2] Flag for reviewer to confirm usage split.

### EC3 -- Capital vs revenue expenditure [T2]
**Situation:** Self-employed person spends SGD 8,000 renovating office premises. Claims as a revenue expense.
**Resolution:** Renovation costs are capital in nature. However, Section 14Q allows deduction of qualifying renovation/refurbishment costs over 3 years, capped at SGD 300,000 per 3-year period. [T2] Flag for reviewer to confirm the expenditure qualifies under Section 14Q.

### EC4 -- Low-value asset cap exceeded [T1]
**Situation:** Self-employed person buys 10 laptops at SGD 4,000 each = SGD 40,000 total. Claims 100% write-off under Section 19A(10A).
**Resolution:** Each laptop is below SGD 5,000, so each qualifies individually. However, the annual cap is SGD 30,000. First SGD 30,000 (7.5 laptops) is written off immediately. Remaining SGD 10,000 must be written off under Section 19 or 19A over the prescribed working life.

### EC5 -- Non-trade income [T1]
**Situation:** Self-employed person earns SGD 5,000 interest from a bank fixed deposit. Includes it as trade income.
**Resolution:** Interest from bank deposits is NOT trade income. It is taxable under Section 10(1)(d) (interest income) but reported separately. Note: interest from approved banks in Singapore may be exempt from tax for individuals.

### EC6 -- Spouse relief income threshold [T1]
**Situation:** Taxpayer claims spouse relief. Spouse earns SGD 5,000 per year.
**Resolution:** Spouse relief requires spouse's income to be SGD 4,000 or below. Since spouse earns SGD 5,000, no spouse relief is available. The threshold is on the spouse's total income, not just employment income.

### EC7 -- Personal relief cap breached [T1]
**Situation:** Taxpayer claims total personal reliefs of SGD 95,000 (earned income, CPF, spouse, children, donations, course fees).
**Resolution:** Total reliefs capped at SGD 80,000. Note: approved donations (250% deduction) are NOT subject to the SGD 80,000 personal relief cap -- they are deducted from assessable income separately.

### EC8 -- Non-resident, short-term self-employment [T3]
**Situation:** Foreigner performs self-employed work in Singapore for 120 days.
**Resolution:** [T3] Escalate. Non-resident self-employment income is taxed differently from employment income. The 60-day exemption applies to employment income, not self-employment income. Trade income derived from Singapore is generally taxable regardless of duration. Refer to Accredited Tax Adviser.

### EC9 -- Section 19A irrevocable election [T1]
**Situation:** Self-employed person elects Section 19A one-year write-off for YA 2026, then realises they would have preferred 3-year write-off.
**Resolution:** The election is irrevocable once made. It applies to ALL qualifying plant and machinery acquired in that basis period. Cannot reverse or selectively apply. File correctly the first time.

### EC10 -- Donations to approved IPCs [T1]
**Situation:** Self-employed person donates SGD 5,000 cash to an approved IPC and wants to claim the deduction.
**Resolution:** Deduction = SGD 5,000 x 250% = SGD 12,500. This is deducted from assessable income, NOT as a personal relief. It is therefore NOT subject to the SGD 80,000 personal relief cap. Donation must be to an approved Institution of a Public Character and must be supported by receipts.

### EC11 -- CPF MediSave for self-employed [T2]
**Situation:** Self-employed person with net trade income of SGD 60,000 asks how much MediSave to contribute.
**Resolution:** Self-employed persons are required to contribute to MediSave based on their net trade income and age. The contribution rate ranges from 4% to 10.5% depending on age group. For net trade income of SGD 60,000, the contribution is based on tiered rates. [T2] Flag for reviewer to calculate exact contribution using IRAS/CPF MediSave contribution tables for the specific age group.

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
Action Required: Accredited Tax Adviser or licensed practitioner must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to Accredited Tax Adviser. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard self-employed, mid-range income
**Input:** Singapore citizen, age 35, single, net trade income SGD 80,000, no other income, earned income relief SGD 1,000, CPF MediSave contribution SGD 3,600, no other reliefs, YA 2026.
**Expected output:** Assessable income = SGD 80,000. Personal reliefs = SGD 1,000 + SGD 3,600 = SGD 4,600. Chargeable income = SGD 75,400. Tax: SGD 0 (first 20,000) + SGD 200 (next 10,000 at 2%) + SGD 350 (next 10,000 at 3.5%) + SGD 2,478 (next 35,400 at 7%) = SGD 3,028. No YA 2026 rebate assumed. Net tax payable = SGD 3,028.

### Test 2 -- Higher income self-employed
**Input:** Singapore PR, age 45, married, net trade income SGD 200,000, spouse income SGD 3,000, 2 qualifying children, earned income relief SGD 1,000, CPF MediSave SGD 5,000, spouse relief SGD 2,000, QCR SGD 8,000 (2 x SGD 4,000), YA 2026.
**Expected output:** Assessable income = SGD 200,000. Personal reliefs = SGD 1,000 + SGD 5,000 + SGD 2,000 + SGD 8,000 = SGD 16,000. Chargeable income = SGD 184,000. Tax: SGD 0 + SGD 200 + SGD 350 + SGD 2,800 + SGD 4,600 + SGD 6,000 + SGD 4,320 (SGD 24,000 at 18%) = SGD 18,270. Net tax payable = SGD 18,270.

### Test 3 -- Low income, below taxable threshold
**Input:** Singapore citizen, age 28, single, net trade income SGD 18,000, earned income relief SGD 1,000, CPF MediSave SGD 1,000, no other reliefs, YA 2026.
**Expected output:** Assessable income = SGD 18,000. Personal reliefs = SGD 2,000. Chargeable income = SGD 16,000. Tax: SGD 0 (below SGD 20,000 threshold). Net tax payable = SGD 0.

### Test 4 -- Capital allowances, Section 19A one-year write-off
**Input:** Self-employed person buys computer equipment for SGD 12,000. Elects Section 19A one-year write-off.
**Expected output:** Capital allowance in Year 1 = SGD 12,000 (100% write-off). No further allowances in subsequent years. Deducted from trade income.

### Test 5 -- Low-value asset within cap
**Input:** Self-employed person buys 5 items at SGD 4,500 each = SGD 22,500 total. All below SGD 5,000 individually. No other qualifying assets.
**Expected output:** Total SGD 22,500 is below the SGD 30,000 annual cap. All 5 items fully written off under Section 19A(10A) in the year of acquisition.

### Test 6 -- Personal relief cap
**Input:** Taxpayer claims: earned income SGD 8,000, CPF SGD 37,740, SRS SGD 15,300, course fees SGD 5,500, parent relief SGD 18,000, spouse SGD 2,000 = total SGD 86,540.
**Expected output:** Total reliefs capped at SGD 80,000. Excess SGD 6,540 is disallowed. Chargeable income = assessable income minus SGD 80,000.

### Test 7 -- GST excluded from revenue
**Input:** GST-registered sole proprietor. Total receipts from clients SGD 107,000 (inclusive of 9% GST on all sales).
**Expected output:** Gross trade income = SGD 107,000 / 1.09 = SGD 98,165 (rounded). GST collected (SGD 8,835) is excluded -- it is a GST liability, not income.

### Test 8 -- Approved donation deduction
**Input:** Self-employed person with assessable income SGD 60,000. Donates SGD 2,000 cash to approved IPC.
**Expected output:** Donation deduction = SGD 2,000 x 250% = SGD 5,000. Deducted from assessable income (not from personal reliefs). Adjusted assessable income = SGD 55,000. Then apply personal reliefs to get chargeable income.

---

## PROHIBITIONS

- NEVER apply resident tax rates without confirming tax residence status (183-day rule or citizen/PR status)
- NEVER compute tax figures directly -- pass chargeable income to the deterministic engine to apply the rate table
- NEVER allow private car capital allowances for S-plated vehicles
- NEVER allow income tax itself as a deduction
- NEVER allow fines or penalties for law violations as a deduction
- NEVER allow personal or domestic expenses as business deductions
- NEVER include GST collected on sales in gross trade income for GST-registered persons
- NEVER allow personal reliefs to exceed the SGD 80,000 cap
- NEVER apply NOR scheme concessions for YA 2025 or later -- the scheme is expired
- NEVER confuse Year of Assessment with the basis period (YA 2026 = income earned in 2025)
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Accredited Tax Adviser for confirmation
- NEVER advise on non-resident tax computations -- escalate to T3

---

## Contribution Notes (For Other Jurisdictions)

If adapting this skill for another country:

1. Replace ITA references with the equivalent national income tax legislation.
2. Replace the progressive rate table with your jurisdiction's equivalent brackets and rates.
3. Replace Section 10(1)(a) trade income rules with your jurisdiction's equivalent.
4. Replace Section 19/19A capital allowance rules with your jurisdiction's depreciation schedule.
5. Replace personal reliefs with your jurisdiction's equivalent relief/credit system.
6. Replace filing deadlines and penalty rates with your jurisdiction's current figures.
7. Replace CPF references with your jurisdiction's equivalent social security/pension system.
8. Have a licensed practitioner in your jurisdiction validate every T1 rule before publishing.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an Accredited Tax Adviser, Chartered Accountant, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
