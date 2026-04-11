---
name: nl-income-tax
description: Use this skill whenever asked about Netherlands income tax for self-employed individuals (zzp'ers). Trigger on phrases like "how much tax do I pay in the Netherlands", "aangifte inkomstenbelasting", "income tax return Netherlands", "zelfstandigenaftrek", "startersaftrek", "MKB-winstvrijstelling", "urencriterium", "Box 1 income", "Box 3 wealth tax", "heffingskortingen", "arbeidskorting", "KIA investment deduction", "self-employed tax Netherlands", or any question about filing or computing income tax for a Dutch zzp'er or eenmanszaak. Also trigger when preparing or reviewing an aangifte IB, computing deductible expenses, or advising on estimated tax payments. This skill covers Box 1 progressive rates, entrepreneur deductions, capital allowances, tax credits, Box 3 savings/investment income, filing deadlines, and penalties. ALWAYS read this skill before touching any Dutch income tax work.
---

# Netherlands Income Tax -- Self-Employed (ZZP) Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Netherlands |
| Jurisdiction Code | NL |
| Primary Legislation | Wet inkomstenbelasting 2001 (Wet IB 2001) |
| Supporting Legislation | Algemene wet inzake rijksbelastingen (AWR); Wet op de loonbelasting 1964; Invorderingswet 1990 |
| Tax Authority | Belastingdienst (Netherlands Tax Administration) |
| Filing Portal | Mijn Belastingdienst (mijn.belastingdienst.nl) |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Dutch-licensed belastingadviseur or AA/RA accountant |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, entrepreneur deduction amounts, MKB-winstvrijstelling percentage, capital allowance rates, filing deadlines, penalty rates. Tier 2: mixed-use expense apportionment, home office deductions, urencriterium documentation, KIA qualifying asset determination. Tier 3: international income, 30% ruling interaction, emigration/immigration year, Box 2 substantial interest, complex Box 3 situations. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Licensed practitioner must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Business structure** [T1] -- eenmanszaak (sole proprietorship), VOF partner, or maatschap partner. This skill covers eenmanszaak only.
2. **Fiscal partner status** [T1] -- single or with fiscal partner (fiscaal partner). Determines allocation of Box 3 assets and certain deductions.
3. **Age / AOW status** [T1] -- whether the taxpayer has reached AOW (state pension) age. Affects the first-bracket rate.
4. **Gross business revenue (omzet)** [T1] -- total invoiced/received in the year.
5. **Business expenses (zakelijke kosten)** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items).
6. **Hours worked in the business** [T1] -- for urencriterium (1,225-hour threshold).
7. **Years in business** [T1] -- for startersaftrek eligibility (first 3 of the past 5 years).
8. **Business investments in the year** [T1] -- type, cost, date of each capital asset acquired.
9. **Other income** [T1] -- employment income (loon), Box 2 income, Box 3 assets.
10. **BTW registration type** [T1] -- regular BTW or kleineondernemersregeling (KOR, small business VAT exemption).

**If AOW status is unknown, assume pre-AOW age (higher first-bracket rate). Flag for confirmation.**

---

## Step 1: Determine Applicable Rate Table -- Box 1 [T1]

**Legislation:** Wet IB 2001, Article 2.10

### Box 1 Rates 2025 (Pre-AOW Age)

| Taxable Income (EUR) | Rate | Composition |
|---------------------|------|-------------|
| 0 -- 38,441 | 35.82% | ~8.17% income tax + 27.65% national insurance premiums (AOW/Anw/Wlz) |
| 38,442 -- 76,817 | 37.48% | Income tax only |
| 76,818+ | 49.50% | Income tax only |

### Box 1 Rates 2025 (AOW Age Reached)

| Taxable Income (EUR) | Rate | Notes |
|---------------------|------|-------|
| 0 -- 38,441 | 17.92% | No AOW premium component |
| 38,442 -- 76,817 | 37.48% | Same as pre-AOW |
| 76,818+ | 49.50% | Same as pre-AOW |

**The Netherlands does not have a 0% band. Tax applies from the first euro of taxable income. Relief comes through heffingskortingen (tax credits) in Step 7.**

**The national insurance premiums (27.65%) in the first bracket consist of: AOW 17.90%, Anw 0.10%, Wlz 9.65%.**

---

## Step 2: Computation Structure -- Aangifte Inkomstenbelasting [T1]

**Legislation:** Wet IB 2001

| Step | Description | How to Populate |
|------|-------------|-----------------|
| A | Gross business revenue (omzet) | Total invoiced/received in the year |
| B | Less: Allowable business expenses | Expenses passing the zakelijkheidstoets (business purpose test) |
| C | Gross profit (brutowinst) | A minus B |
| D | Less: Zelfstandigenaftrek | EUR 2,470 (2025) if urencriterium met |
| E | Less: Startersaftrek | EUR 2,123 if eligible (first 3 of past 5 years) |
| F | Profit after entrepreneur deductions | C minus D minus E |
| G | Less: MKB-winstvrijstelling | 12.7% of Step F |
| H | Net business profit (winst uit onderneming) | F minus G |
| I | Plus: Other Box 1 income | Employment income, eigen woning forfait, etc. |
| J | Less: Persoonsgebonden aftrek | Personal deductions (alimentatie, specific healthcare costs, etc.) |
| K | Taxable income Box 1 (belastbaar inkomen) | H plus I minus J |
| L | Gross tax (Box 1) | Apply rate table from Step 1 to K |
| M | Less: Heffingskortingen | Tax credits (algemene heffingskorting, arbeidskorting, etc.) |
| N | Net tax payable Box 1 | L minus M (minimum EUR 0) |

**NEVER compute Step L tax figures directly -- pass taxable income to the deterministic engine to apply the rate table.**

---

## Step 3: Entrepreneur Deductions (Ondernemersaftrek) [T1]

**Legislation:** Wet IB 2001, Articles 3.74 -- 3.79

### 3a. Urencriterium (Hours Criterion) [T1/T2]

| Requirement | Detail |
|-------------|--------|
| Minimum hours | 1,225 hours per calendar year |
| What counts | Time spent on business activities: client work, administration, acquisition, travel for business |
| What does NOT count | General training not specific to the business, personal activities |
| Documentation | Must be able to demonstrate hours if audited -- time registration recommended |
| [T2] | Flag for reviewer: confirm hours documentation exists and is credible |

**The urencriterium is a gateway requirement. Without it, no zelfstandigenaftrek, no startersaftrek.**

### 3b. Zelfstandigenaftrek (Self-Employed Deduction) [T1]

| Year | Amount |
|------|--------|
| 2024 | EUR 3,750 |
| **2025** | **EUR 2,470** |
| 2026 | EUR 1,200 |
| 2027 | EUR 900 |

- Deducted from gross profit before MKB-winstvrijstelling
- Can create or increase a loss (verrekenbaar verlies)
- Requires urencriterium to be met

### 3c. Startersaftrek (Starter Deduction) [T1]

| Item | Detail |
|------|--------|
| Amount | EUR 2,123 (2025) |
| Eligibility | In at least 1 of the 5 preceding calendar years you were NOT an entrepreneur for income tax purposes |
| Maximum claims | 3 times in total within a 5-year period |
| Requires | Urencriterium met |

- Applied on top of the zelfstandigenaftrek
- Combined deduction for a qualifying starter in 2025: EUR 2,470 + EUR 2,123 = EUR 4,593

### 3d. MKB-Winstvrijstelling (SME Profit Exemption) [T1]

| Year | Percentage |
|------|-----------|
| 2024 | 13.31% |
| **2025** | **12.7%** |
| 2026 | 12.7% |

- Applied to profit AFTER subtracting zelfstandigenaftrek and startersaftrek
- Available to ALL entrepreneurs (ondernemers) -- no urencriterium required
- Also applies to losses (reduces the deductible loss by 12.7%)

---

## Step 4: Fiscale Oudedagsreserve (FOR) [T1]

**Legislation:** Wet IB 2001, Article 3.67 (repealed)

**The FOR was abolished as of 1 January 2023.** No new additions to the FOR can be made from 2023 onwards.

| Rule | Detail |
|------|--------|
| New additions | NOT permitted from 2023 onward |
| Existing FOR balance | Remains on the balance sheet until settled |
| Settlement | Taxed as Box 1 income when converted to an annuity or upon cessation of business |
| [T2] | If client has an existing FOR balance, flag for reviewer to advise on settlement strategy |

---

## Step 5: Kleinschaligheidsinvesteringsaftrek (KIA) [T1]

**Legislation:** Wet IB 2001, Article 3.41

### KIA Table 2025

| Total Investment (EUR) | Deduction |
|----------------------|-----------|
| 0 -- 2,900 | No KIA |
| 2,901 -- 70,602 | 28% of total investment amount |
| 70,603 -- 130,744 | EUR 19,769 (fixed) |
| 130,745 -- 392,230 | EUR 19,769 minus 7.56% of amount above EUR 130,744 |
| 392,231+ | No KIA |

### KIA Rules [T1]

- Only business assets (bedrijfsmiddelen) with an individual purchase price of at least EUR 450 (excl. BTW) qualify
- Land, residential property, passenger cars, and certain other assets are excluded
- The KIA is a separate deduction from capital allowances (afschrijving) -- you claim both
- Total investment amount = sum of all qualifying investments in the calendar year
- [T2] Flag for reviewer if asset classification is unclear (e.g., is it a business asset or personal?)

---

## Step 6: Capital Allowances (Afschrijving) [T1]

**Legislation:** Wet IB 2001, Article 3.30

### Standard Depreciation

| Asset Type | Minimum Useful Life | Maximum Annual Rate |
|-----------|---------------------|---------------------|
| Computer hardware | Typically 3 years | 33.3% |
| Computer software | Typically 3 years | 33.3% |
| Office equipment | Typically 5 years | 20% |
| Furniture and fittings | Typically 5 years | 20% |
| Motor vehicles | Typically 5 years | 20% |
| Machinery | Typically 5--10 years | 10--20% |

### Residual Value Rule [T1]

- Movable assets: depreciate to a residual value of at least EUR 1 (in practice, often to the expected resale value)
- Buildings: depreciate to no lower than 50% of WOZ value (for own-use business buildings)

### Willekeurige Afschrijving (Accelerated Depreciation) [T2]

- Available for starters meeting the urencriterium and startersaftrek conditions
- Allows depreciation at any chosen rate (including 100% in year 1)
- [T2] Flag for reviewer: confirm starter status and whether accelerated depreciation is beneficial given the client's income profile

---

## Step 7: Heffingskortingen (Tax Credits) [T1]

**Legislation:** Wet IB 2001, Articles 8.10 -- 8.17

### 7a. Algemene Heffingskorting (General Tax Credit) 2025

| Taxable Income (EUR) | Credit |
|---------------------|--------|
| 0 -- 28,406 | EUR 3,068 (maximum) |
| 28,407 -- 76,817 | EUR 3,068 minus 6.337% of income above EUR 28,406 |
| 76,818+ | EUR 0 |

### 7b. Arbeidskorting (Labour Tax Credit) 2025

| Taxable Income (EUR) | Credit |
|---------------------|--------|
| 0 -- 11,491 | 8.231% of income |
| 11,492 -- 26,288 | EUR 946 + 29.861% of income above EUR 11,491 |
| 26,289 -- 43,071 | EUR 5,599 (maximum) |
| 43,072 -- 124,935 | EUR 5,599 minus 6.51% of income above EUR 43,071 |
| 124,936+ | EUR 0 |

- The arbeidskorting is available to zzp'ers -- business profit counts as arbeidsinkomen
- Both credits are applied against the gross Box 1 tax calculated in Step 2, Line L
- Credits cannot reduce tax below EUR 0

### 7c. Other Heffingskortingen [T2]

| Credit | Amount (2025) | Notes |
|--------|---------------|-------|
| Inkomensafhankelijke combinatiekorting (IACK) | Max EUR 2,950 | For working parents with children under 12. Being phased out. |
| Jonggehandicaptenkorting | EUR 898 | For recipients of Wajong benefit |
| Ouderenkorting | Max EUR 2,010 | For those who reached AOW age; income-dependent |
| Alleenstaande ouderenkorting | EUR 524 | Single persons with AOW |

---

## Step 8: Allowable Deductions -- Business Purpose Test [T1/T2]

**Legislation:** Wet IB 2001, Article 3.8 and further

### The Test [T1]

An expense is deductible if it is incurred for the purpose of acquiring, collecting, or maintaining business profit. Mixed-use expenses must be apportioned on a reasonable basis.

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated workspace) | T1 | Fully deductible |
| Professional liability insurance | T1 | Fully deductible |
| Accountancy / belastingadviseur fees | T1 | Fully deductible |
| Office supplies / stationery | T1 | Fully deductible |
| Software subscriptions | T1 | Fully deductible (if not capitalised) |
| Marketing / advertising | T1 | Fully deductible |
| Bank charges (business account) | T1 | Fully deductible |
| Training / courses related to business | T1 | Fully deductible |
| Professional association memberships | T1 | Fully deductible |
| Travel expenses (business purpose) | T1 | Fully deductible |
| Phone / internet | T2 | Business-use portion only |
| Home office (werkruimte) | T2 | See home office rules below |
| Motor vehicle expenses | T2 | See motor vehicle rules below |
| Business meals with clients | T1 | 80% deductible (20% non-deductible under aftrekbeperking) |
| Business gifts | T1 | Deductible up to EUR 27.23 per gift (excl. BTW) if given in a business context |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Personal living expenses | Not business-related |
| Fines and penalties (boeten) | Public policy -- Article 3.14 |
| Income tax itself | Tax on income cannot be deducted |
| 20% of business entertainment/meals | Aftrekbeperking -- Article 3.15 |
| Private portion of mixed-use expenses | Must be apportioned out |
| Clothing (unless protective/uniform) | Considered personal |

### Home Office Rules (Werkruimte) [T2]

**Legislation:** Wet IB 2001, Article 3.16

| Scenario | Treatment |
|----------|-----------|
| Independent workspace (own entrance, own toilet) and you work >70% of your time there AND have no other workspace | Costs deductible on proportional basis |
| Independent workspace but you work <70% there or you have another workspace | Generally NOT deductible |
| Non-independent workspace (room within your home) | NOT deductible |

- [T2] Flag for reviewer: confirm workspace arrangement meets the strict Dutch requirements

### Motor Vehicle Rules [T2]

| Scenario | Treatment |
|----------|-----------|
| Business car on the balance sheet | All costs deductible; private use is added back as bijtelling (typically 22% of catalogue value) |
| Private car used for business | EUR 0.23/km for business kilometres (2025) |
| [T2] | Flag for reviewer: confirm km administration is maintained |

---

## Step 9: Box 3 -- Savings and Investments [T1/T2]

**Legislation:** Wet IB 2001, Articles 5.1 -- 5.3

### Box 3 Overview 2025

| Item | Detail |
|------|--------|
| Tax-free allowance (heffingsvrij vermogen) | EUR 57,684 per person (EUR 115,368 for fiscal partners) |
| Tax rate | 36% on deemed return |
| Reference date | 1 January 2025 |

### Deemed Return Rates 2025

| Asset Category | Deemed Return |
|---------------|--------------|
| Bank savings (banktegoeden) | 1.37% |
| Other investments and assets (overige bezittingen) | 5.88% |
| Debts (schulden) | 2.70% (subtracted) |

### How It Works [T1]

1. Calculate total Box 3 assets minus debts minus heffingsvrij vermogen = grondslag sparen en beleggen
2. Apply weighted deemed return based on asset composition
3. Multiply deemed return by 36% = Box 3 tax

### Transitional System [T2]

For 2025, the Belastingdienst calculates tax using both the fictional return method and (where applicable) the actual return method. The most favourable outcome applies. A new system based on actual returns is planned for 2028.

- [T2] Flag for reviewer if client has significant Box 3 assets -- verify which method is more favourable

---

## Step 10: Filing Deadlines [T1]

**Legislation:** AWR; Wet IB 2001

| Filing / Payment | Deadline |
|-----------------|----------|
| Aangifte inkomstenbelasting (income tax return) | 1 May of the following year (for 2025: 1 May 2026) |
| Filing opens | 1 March of the following year |
| Extension (uitstel) -- standard | Until 1 September (request via belastingadviseur or Mijn Belastingdienst) |
| Extension via belastingadviseur (beconregeling) | Until 1 May of the year after (i.e., 1 May 2027 for 2025 return) |
| Voorlopige aanslag (estimated assessment) | Issued by Belastingdienst; payment due per terms on the assessment |
| BTW returns | Quarterly (or monthly if applicable) |

### Estimated Tax Payments [T1]

- The Belastingdienst issues a voorlopige aanslag (provisional/estimated assessment) based on prior year or your request
- You can request a voorlopige aanslag to spread payments monthly
- Underpayment results in interest (belastingrente) at the current statutory rate

---

## Step 11: Penalties [T1]

**Legislation:** AWR Articles 67a -- 67f; Besluit Bestuurlijke Boeten Belastingdienst

| Offence | Penalty |
|---------|---------|
| Late filing (verzuimboete) | EUR 394 (2025); increases for repeated offences up to EUR 6,709 |
| Failure to file after reminder | Up to EUR 5,514 |
| Incorrect return (vergrijpboete -- negligence) | 25% -- 50% of underpaid tax |
| Incorrect return (vergrijpboete -- intent/fraud) | 50% -- 100% of underpaid tax |
| Late payment interest (belastingrente) | Statutory rate (currently ~7.5% per annum for income tax) |
| Repeated non-filing (3+ years) | Up to EUR 6,709 per offence |

**WARNING:** Belastingrente accrues from 1 July of the year following the tax year. File and pay on time to avoid compounding interest charges.

---

## Step 12: Record Keeping [T1]

**Legislation:** AWR, Article 52

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 7 years (10 years for immovable property) |
| What to keep | All sales invoices, purchase invoices, bank statements, contracts, hour registrations, asset register, BTW returns |
| Format | Paper or digital (Belastingdienst accepts digital) |
| Hour registration | Required to substantiate urencriterium -- date, hours, activity description |
| Asset register | Date acquired, cost, depreciation claimed each year, book value |

---

## Step 13: Edge Case Registry

### EC1 -- BTW included in revenue [T1]
**Situation:** ZZP'er invoices EUR 12,100 (EUR 10,000 net + EUR 2,100 BTW at 21%). Client reports EUR 12,100 as gross revenue.
**Resolution:** Gross revenue must be EUR 10,000 only. BTW collected is a liability to Belastingdienst, not income. For KOR (small business exemption) clients who do not charge BTW, the full amount received IS revenue.

### EC2 -- Urencriterium not met [T1]
**Situation:** ZZP'er worked 1,100 hours in the business. Claims zelfstandigenaftrek.
**Resolution:** NOT eligible. Urencriterium requires minimum 1,225 hours. No zelfstandigenaftrek (EUR 2,470), no startersaftrek (EUR 2,123). MKB-winstvrijstelling (12.7%) still applies -- it does not require urencriterium.

### EC3 -- Starter in year 4 [T1]
**Situation:** ZZP'er started in 2022. Claims startersaftrek for 2025 (4th year).
**Resolution:** Check: was the client an entrepreneur in ALL of the 5 preceding years (2020--2024)? Startersaftrek requires that in at least 1 of the 5 preceding years, the client was NOT an entrepreneur. If the client was an entrepreneur continuously from 2022, they have used 3 years (2022, 2023, 2024) -- no startersaftrek in 2025 (maximum 3 claims).

### EC4 -- Business meal deduction [T1]
**Situation:** ZZP'er takes a client to dinner for EUR 150 and claims full deduction.
**Resolution:** Only 80% deductible. EUR 150 x 80% = EUR 120 deductible. EUR 30 is non-deductible (aftrekbeperking under Article 3.15). This is different from Malta where entertainment is fully blocked.

### EC5 -- KIA and capital allowance combined [T1]
**Situation:** ZZP'er buys a laptop for EUR 1,500 and office furniture for EUR 2,000. Total investment = EUR 3,500. Client only claims depreciation.
**Resolution:** Client should claim BOTH: (1) KIA: EUR 3,500 x 28% = EUR 980 deduction, AND (2) annual depreciation on each asset. These are separate deductions. The KIA is a one-time investment deduction; depreciation spreads the cost over the useful life.

### EC6 -- FOR balance on old balance sheet [T2]
**Situation:** Client has EUR 15,000 FOR balance from pre-2023. Asks what to do.
**Resolution:** FOR was abolished from 2023. No new additions allowed. Existing balance remains until settled. Settlement options: convert to qualifying annuity (lijfrente) or add to taxable income upon cessation. [T2] Flag for reviewer to advise on timing and tax impact of settlement.

### EC7 -- Car on balance sheet, private use [T2]
**Situation:** ZZP'er has a car on the business balance sheet. Uses it 30% privately.
**Resolution:** All car costs are deductible. Add back bijtelling: 22% of catalogue value (list price when new) as taxable income. If the client can prove private use is less than 500 km/year, no bijtelling applies -- but a complete km administration is mandatory. [T2] Flag for reviewer to confirm km log and bijtelling percentage.

### EC8 -- Home office does not qualify [T2]
**Situation:** ZZP'er works from a spare bedroom (no separate entrance, no own toilet).
**Resolution:** NOT a qualifying independent workspace under Dutch rules. No home office deduction for rent/mortgage interest, utilities, or maintenance. The workspace rules in the Netherlands are much stricter than in many other jurisdictions. [T2] Flag for reviewer.

### EC9 -- KOR client revenue treatment [T1]
**Situation:** ZZP'er is on the KOR (kleineondernemersregeling, small business BTW exemption, turnover under EUR 20,000). Client invoices EUR 18,000. No BTW is charged.
**Resolution:** Full EUR 18,000 is gross revenue. No BTW to exclude because none was charged. All input BTW paid on purchases is a cost (cannot be reclaimed under KOR). Gross purchase prices are the deductible expense amounts.

### EC10 -- Fiscal partner allocation [T2]
**Situation:** Married ZZP'er and spouse. Spouse has no income. How to allocate Box 3 assets?
**Resolution:** Fiscal partners can allocate Box 3 assets and liabilities between them in any proportion they choose (as long as the total equals 100%). Optimize by allocating to the partner with lower Box 1 income to maximize algemene heffingskorting. [T2] Flag for reviewer to run both allocation scenarios.

### EC11 -- Loss from business in first years [T1]
**Situation:** ZZP'er starter has a loss of EUR 5,000 in their first year after all deductions.
**Resolution:** The loss can be carried back 3 years or carried forward 9 years against Box 1 income (for losses arising from 2022 onwards, forward carry is limited to EUR 1 million + 50% of income above EUR 1 million, but this is rarely relevant for zzp'ers). Note: MKB-winstvrijstelling reduces the loss by 12.7% (loss becomes EUR 5,000 x 87.3% = EUR 4,365 deductible loss).

---

## Step 14: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Licensed belastingadviseur or AA/RA accountant must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to licensed practitioner. Document gap.
```

---

## Step 15: Test Suite

### Test 1 -- Standard ZZP'er, mid-range income, urencriterium met
**Input:** Single, pre-AOW, gross revenue EUR 60,000, allowable expenses EUR 15,000, urencriterium met (1,400 hours), not a starter, no other income, no Box 3 assets, no investments qualifying for KIA.
**Expected output:** Gross profit = EUR 45,000. Less zelfstandigenaftrek EUR 2,470 = EUR 42,530. MKB-winstvrijstelling: EUR 42,530 x 12.7% = EUR 5,401. Net business profit = EUR 37,129. Taxable income Box 1 = EUR 37,129. Gross tax: EUR 37,129 x 35.82% = EUR 13,299. Less algemene heffingskorting: EUR 3,068 minus 6.337% x (EUR 37,129 - EUR 28,406) = EUR 3,068 - EUR 553 = EUR 2,515. Less arbeidskorting: EUR 5,599 (maximum, income in EUR 26,289 -- 43,071 band). Net tax payable = EUR 13,299 - EUR 2,515 - EUR 5,599 = EUR 5,185.

### Test 2 -- Starter ZZP'er, lower income
**Input:** Single, pre-AOW, first year of business, gross revenue EUR 30,000, allowable expenses EUR 8,000, urencriterium met (1,300 hours), qualifies as starter.
**Expected output:** Gross profit = EUR 22,000. Less zelfstandigenaftrek EUR 2,470 + startersaftrek EUR 2,123 = EUR 4,593. Profit after deductions = EUR 17,407. MKB-winstvrijstelling: EUR 17,407 x 12.7% = EUR 2,211. Net business profit = EUR 15,196. Gross tax: EUR 15,196 x 35.82% = EUR 5,443. Less algemene heffingskorting: EUR 3,068 (maximum -- income under EUR 28,406). Less arbeidskorting: EUR 946 + 29.861% x (EUR 15,196 - EUR 11,491) = EUR 946 + EUR 1,107 = EUR 2,053. Net tax payable = EUR 5,443 - EUR 3,068 - EUR 2,053 = EUR 322.

### Test 3 -- High income ZZP'er, top bracket
**Input:** Single, pre-AOW, gross revenue EUR 140,000, allowable expenses EUR 30,000, urencriterium met, not a starter, no other income.
**Expected output:** Gross profit = EUR 110,000. Less zelfstandigenaftrek EUR 2,470 = EUR 107,530. MKB-winstvrijstelling: EUR 107,530 x 12.7% = EUR 13,656. Net business profit = EUR 93,874. Gross tax: EUR 38,441 x 35.82% + (EUR 76,817 - EUR 38,441) x 37.48% + (EUR 93,874 - EUR 76,817) x 49.50% = EUR 13,770 + EUR 14,381 + EUR 8,443 = EUR 36,594. Less algemene heffingskorting: EUR 0 (income above EUR 76,818). Less arbeidskorting: EUR 0 (income above EUR 124,936). Net tax payable = EUR 36,594.

### Test 4 -- Urencriterium NOT met
**Input:** Part-time ZZP'er, 900 hours, gross revenue EUR 25,000, expenses EUR 5,000.
**Expected output:** Gross profit = EUR 20,000. No zelfstandigenaftrek (urencriterium not met). No startersaftrek. MKB-winstvrijstelling still applies: EUR 20,000 x 12.7% = EUR 2,540. Net business profit = EUR 17,460. Tax calculated on EUR 17,460 at 35.82% minus applicable heffingskortingen.

### Test 5 -- KIA investment deduction
**Input:** ZZP'er invests EUR 5,000 in a new laptop (EUR 2,000) and office furniture (EUR 3,000). Both above EUR 450 threshold.
**Expected output:** Total qualifying investment = EUR 5,000. KIA = EUR 5,000 x 28% = EUR 1,400 one-time deduction. PLUS annual depreciation on each asset separately. KIA and depreciation are both claimed.

### Test 6 -- Business meal, 80% rule
**Input:** ZZP'er claims EUR 500 in business meals with clients.
**Expected output:** Deductible: EUR 500 x 80% = EUR 400. Non-deductible portion: EUR 100 (aftrekbeperking).

### Test 7 -- BTW excluded from revenue
**Input:** Regular BTW-registered ZZP'er. Total receipts from clients EUR 72,600 (all inclusive of 21% BTW).
**Expected output:** Gross revenue = EUR 72,600 / 1.21 = EUR 60,000. EUR 12,600 BTW is excluded from revenue -- it is a liability to Belastingdienst.

### Test 8 -- Box 3 calculation
**Input:** ZZP'er has EUR 100,000 in bank savings, EUR 50,000 in investments, no debts. Single (no fiscal partner).
**Expected output:** Total assets = EUR 150,000. Heffingsvrij vermogen = EUR 57,684. Grondslag = EUR 92,316. Deemed return: bank portion (EUR 100,000/EUR 150,000 x EUR 92,316 = EUR 61,544) x 1.37% = EUR 843 + investment portion (EUR 50,000/EUR 150,000 x EUR 92,316 = EUR 30,772) x 5.88% = EUR 1,809. Total deemed return = EUR 2,652. Box 3 tax = EUR 2,652 x 36% = EUR 955.

---

## PROHIBITIONS

- NEVER apply Box 1 rates without knowing whether the client has reached AOW age
- NEVER compute gross tax figures directly -- pass taxable income to the deterministic engine
- NEVER grant zelfstandigenaftrek or startersaftrek without confirming urencriterium is met
- NEVER apply zelfstandigenaftrek without confirming the client qualifies as an entrepreneur (ondernemer) for income tax purposes
- NEVER allow fines or penalties as a business deduction
- NEVER allow income tax itself as a deduction
- NEVER include BTW collected on sales in gross revenue for regular BTW-registered clients
- NEVER allow home office deductions without confirming the workspace meets the strict independent workspace requirements
- NEVER allow new FOR additions -- the FOR was abolished from 2023
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their belastingadviseur for confirmation
- NEVER advise on Box 2 (aanmerkelijk belang), 30% ruling, or international income situations -- escalate to T3

---

## Contribution Notes (For Other Jurisdictions)

If adapting this skill for another country:

1. Replace Wet IB 2001 references with the equivalent national income tax legislation.
2. Replace the Box 1 rate tables with your jurisdiction's equivalent brackets and rates.
3. Replace the entrepreneur deductions (zelfstandigenaftrek, startersaftrek, MKB-winstvrijstelling) with your jurisdiction's equivalent, if any.
4. Replace the KIA table with your jurisdiction's investment deduction scheme.
5. Replace heffingskortingen with your jurisdiction's tax credit system.
6. Replace filing deadlines and penalty rates with your jurisdiction's current figures.
7. Replace the home office and motor vehicle rules with your jurisdiction's rules.
8. Have a licensed practitioner in your jurisdiction validate every T1 rule before publishing.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a belastingadviseur, AA/RA accountant, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
