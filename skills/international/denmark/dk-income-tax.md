---
name: dk-income-tax
description: Use this skill whenever asked about Danish income tax for self-employed individuals (selvstændig erhvervsdrivende). Trigger on phrases like "Danish tax", "AM-bidrag", "bundskat", "topskat", "kommuneskat", "virksomhedsordningen", "kapitalafkastordningen", "personfradrag", "Årsopgørelse", "Oplysningsskema", "self-employed tax Denmark", or any question about filing or computing income tax for a Danish self-employed client. Covers AM-bidrag (8%), bundskat, topskat, kommuneskat, kirkeskat, virksomhedsordningen, kapitalafkastordningen, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Danish income tax work.
---

# Denmark Income Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Denmark |
| Jurisdiction Code | DK |
| Primary Legislation | Personskatteloven (PSL); Kildeskatteloven (KSL); Virksomhedsskatteloven (VSL); Kapitalafkastordningen (KAO) |
| Supporting Legislation | Ligningsloven (LL); Afskrivningsloven (AL); Statsskatteloven (SL) |
| Tax Authority | Skattestyrelsen (SKAT) |
| Filing Portal | skat.dk / TastSelv |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Danish statsautoriseret or registreret revisor |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: AM-bidrag, bundskat, topskat rates, personfradrag, filing deadlines. Tier 2: virksomhedsordningen vs kapitalafkastordningen choice, mixed-use expense apportionment, home office. Tier 3: international income, transfer pricing, complex VSO exits. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified revisor must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Business form** [T1] -- selvstændig erhvervsdrivende (sole proprietor), freelancer, or other
2. **Tax scheme election** [T2] -- Virksomhedsordningen (VSO), Kapitalafkastordningen (KAO), or no scheme (personskatteloven default)
3. **Gross business revenue** [T1] -- total invoiced/received in the year before any deductions
4. **Business expenses** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items)
5. **Municipality of residence** [T1] -- determines kommuneskat rate
6. **Church membership** [T1] -- member of Folkekirken? Determines if kirkeskat applies
7. **Other income** [T1] -- employment income, capital income, share income
8. **AM-bidrag already withheld** [T1] -- from employment or B-income payments
9. **Prior year tax liability** [T1] -- for B-skat (preliminary tax) calculation

**If municipality is unknown, use the national average kommuneskat of 25.1%. Flag as estimated.**

---

## Step 1: AM-bidrag (Labour Market Contribution) [T1]

**Legislation:** Arbejdsmarkedsbidragsloven

| Item | Rate / Amount |
|------|---------------|
| AM-bidrag rate | 8% |
| Applied to | Gross business income (before any other deductions) |
| Nature | Mandatory for all earned income -- not optional |

AM-bidrag is calculated first and reduces the base for all subsequent income taxes. It is NOT a deduction -- it is a separate tax applied before the income tax computation begins.

**Computation:** AM-bidrag = Gross business income x 8%

The remaining 92% of gross income becomes the base for bundskat, topskat, and kommuneskat calculations.

---

## Step 2: Income Tax Rates (2025) [T1]

**Legislation:** Personskatteloven; Kommuneskatteloven

### State Taxes

| Tax | Rate | Threshold (2025) | Applied To |
|-----|------|-------------------|------------|
| Bundskat | 12.01% | On personal income above personfradrag | Personal income after AM-bidrag |
| Topskat | 15% | Personal income above DKK 611,800 (after AM-bidrag) | Only the excess above DKK 611,800 |

### Local Taxes

| Tax | Rate (2025) | Notes |
|-----|-------------|-------|
| Kommuneskat | Avg 25.1% (range 22--27%) | Varies by municipality; applied to taxable income |
| Kirkeskat | Avg 0.87% (range 0.39--1.20%) | Optional -- only for Folkekirken members |

### Personal Allowance

| Item | Amount (2025) |
|------|---------------|
| Personfradrag (personal allowance) | DKK 51,600 |
| Personfradrag (under 18) | DKK 40,500 |

The personfradrag reduces the tax payable, not the taxable income directly. It provides a tax value equal to personfradrag x (bundskat rate + kommuneskat rate + kirkeskat rate if applicable).

### Tax Ceiling (Skatteloft) [T1]

The combined marginal tax rate on personal income (bundskat + topskat + kommuneskat + kirkeskat) is capped at approximately 52.07% (2025). If the sum of rates exceeds this ceiling, the topskat rate is reduced. Kirkeskat is excluded from the ceiling computation.

---

## Step 3: Virksomhedsordningen (VSO) vs Kapitalafkastordningen (KAO) [T2]

**Legislation:** Virksomhedsskatteloven (VSL); Kapitalafkastordningen

### Virksomhedsordningen (Business Scheme) [T2]

| Feature | Detail |
|---------|--------|
| Interim tax on retained profits | 22% (2025) |
| Interest deductions | Full deduction of business interest against business income |
| Income splitting | Can split income between personal income and capital income |
| Opsparet overskud | Profits retained in VSO taxed at 22% until withdrawn |
| Withdrawal | Taxed as personal income when withdrawn from VSO |
| Requirement | Full separation of business and private finances required |

**When VSO is advantageous:** Business has significant interest expenses; profits can be retained in the business; income is highly variable year to year.

### Kapitalafkastordningen (Capital Yield Scheme) [T2]

| Feature | Detail |
|---------|--------|
| Capital yield rate (2025) | 2% |
| Applied to | Net business assets at start of year |
| Effect | Portion of business income reclassified as capital income (lower tax) |
| Requirement | Less strict separation than VSO |

**When KAO is advantageous:** Business has significant assets but limited interest expenses; simpler administration than VSO.

### No Scheme (Default) [T1]

All business profit is taxed as personal income under personskatteloven. Simplest option but no income-splitting benefits.

**[T2] The choice between VSO, KAO, and no scheme requires modelling all three scenarios. Flag for reviewer to confirm optimal scheme.**

---

## Step 4: Allowable Deductions [T1/T2]

**Legislation:** Statsskatteloven ss 6; Ligningsloven

### The Driftsomkostning Test [T1]

An expense is deductible only if incurred to acquire, secure, or maintain income (SL ss 6, stk. 1, litra a). Mixed-use expenses must be apportioned.

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated business premises) | T1 | Fully deductible |
| Professional insurance | T1 | Fully deductible |
| Accountancy / revisor fees | T1 | Fully deductible |
| Office supplies | T1 | Fully deductible |
| Software subscriptions (business use) | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Business bank charges | T1 | Fully deductible |
| Professional development / courses | T1 | Fully deductible if directly related to business |
| Travel (business purpose) | T1 | Fully deductible; per diem rates apply (rejsefradrag) |
| Phone / internet | T2 | Business use portion only -- client to confirm % |
| Motor vehicle expenses | T2 | Business use portion only or standard rate per km |
| Home office | T2 | Proportional -- see home office rules |
| Representation (limited) | T1 | 25% deductible (DKK limit per person applies) |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Private living expenses | Not business-related (SL ss 6) |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income cannot reduce income |
| Capital expenditure | Depreciated under afskrivningsloven, not expensed |
| Personal drawings | Not an expense |

### Home Office Rules [T2]

- Dedicated room used exclusively for business: deduct proportional share of rent/mortgage interest, utilities, insurance
- Room must be unsuitable for private use (e.g., no bed, not a living room)
- Standard deduction of DKK 2,100/year (2025) available as alternative to actual cost apportionment
- [T2] Flag for reviewer to confirm workspace qualifies

### Motor Vehicle Rules [T2]

- Business km can be claimed at standard rates (Skatteraadets satser) or actual cost apportioned
- Standard rate (2025): DKK 3.79/km for first 20,000 km; DKK 2.23/km thereafter
- Logbook required if claiming actual costs with apportionment
- [T2] Flag for reviewer to confirm method and business percentage

---

## Step 5: Depreciation (Afskrivninger) [T1]

**Legislation:** Afskrivningsloven (AL)

### Depreciation Rates

| Asset Type | Method | Rate |
|-----------|--------|------|
| Machinery, equipment, vehicles (driftsmidler) | Declining balance (pool) | Up to 25% per year |
| Buildings (business use) | Straight-line | 4% per year |
| Software (purchased) | Declining balance (pool) | Up to 25% per year |
| Goodwill | Straight-line | 1/7 per year (~14.3%) |
| Patents, licences | Straight-line | Over useful life |

### Rules [T1]

- Driftsmidler are pooled together; 25% declining balance applied to the pool's written-down value
- Assets under DKK 15,400 (2025, indexed): may be expensed immediately (straksafskrivning)
- Partial-year acquisition: full-year depreciation in year of acquisition
- Building depreciation: only for business-use buildings; residential buildings not depreciable

---

## Step 6: B-skat (Preliminary Tax for Self-Employed) [T1]

**Legislation:** Kildeskatteloven (KSL)

| Feature | Detail |
|---------|--------|
| Payment schedule | 10 monthly instalments (typically Jan--May, Aug--Dec) |
| Basis | Self-assessed expected income for the year |
| Adjustment | Can be adjusted via TastSelv during the year |
| Restskat (underpayment) | Interest charged at ~3.3% on amounts above DKK 22,900 |
| Overpayment | Refunded with interest |

### Rules [T1]

- B-skat covers AM-bidrag + income tax on self-employment income
- Taxpayer estimates income at start of year; SKAT issues B-skat payment slips
- Underpayment above DKK 22,900 attracts a day-to-day interest charge (procenttillaeg)
- It is better to overestimate slightly than to underestimate

---

## Step 7: Filing Deadlines [T1]

**Legislation:** Skattekontrolloven; KSL

| Filing / Payment | Deadline |
|-----------------|----------|
| Oplysningsskema (tax return) -- self-employed | 1 July (extended from 1 May for self-employed) |
| B-skat instalments | Monthly (10 instalments, Jan--May + Aug--Dec) |
| AM-bidrag | Included in B-skat instalments |
| Extension | Possible via revisor -- typically to 1 September |

**Note:** Employed individuals file by 1 May. Self-employed (selvstændig erhvervsdrivende) have an automatic extension to 1 July.

---

## Step 8: Penalties [T1]

**Legislation:** Skattekontrolloven; Skatteforvaltningsloven

| Offence | Penalty |
|---------|---------|
| Late filing | DKK 200/day up to a maximum (typically DKK 5,000) |
| Incorrect return (negligence) | Additional tax up to 20% of the understated amount |
| Incorrect return (gross negligence / fraud) | Additional tax up to 100% + criminal prosecution |
| Late B-skat payment | Interest + enforcement proceedings via Gældsstyrelsen |

---

## Step 9: Interaction with VAT (Moms) [T1]

**Legislation:** Momsloven (VAT Act)

| Scenario | Income Tax Treatment |
|----------|---------------------|
| Moms collected on sales (momsregistreret) | NOT income -- it is a liability to SKAT. Exclude from gross revenue. |
| Input moms recovered | NOT an expense -- it is reclaimable. Exclude from expenses. |
| Non-deductible moms (e.g., entertainment) | IS an expense -- adds to cost of the purchase |
| Non-registered (under DKK 50,000 turnover) | No moms charged; no input moms reclaimed; gross = net |

---

## Step 10: Record Keeping [T1]

**Legislation:** Bogforingsloven (Bookkeeping Act)

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 5 years from end of financial year |
| What to keep | All invoices, receipts, bank statements, contracts, asset register |
| Format | Digital or paper (digital preferred; Bogforingsloven 2022 encourages digital) |
| Bookkeeping standard | Must follow Danish bookkeeping standards (god bogforingsskik) |

---

## Step 11: Edge Case Registry

### EC1 -- AM-bidrag applied after deductions [T1]
**Situation:** Client computes AM-bidrag on net income after deducting expenses.
**Resolution:** INCORRECT. AM-bidrag is 8% on gross personal income before any deductions. Recalculate on gross.

### EC2 -- VSO entry with private debt [T2]
**Situation:** Client enters virksomhedsordningen but has private debt mixed with business assets.
**Resolution:** All assets and liabilities in VSO must be business-related. Private debt cannot enter VSO. [T2] Flag for reviewer to confirm asset/liability separation.

### EC3 -- Topskat computed on total income [T1]
**Situation:** Client applies 15% topskat to entire income above personfradrag.
**Resolution:** INCORRECT. Topskat applies only to the portion of personal income (after AM-bidrag) exceeding DKK 611,800. Below that threshold, only bundskat + kommuneskat apply.

### EC4 -- Kirkeskat charged to non-member [T1]
**Situation:** Client is not a member of Folkekirken but kirkeskat appears in computation.
**Resolution:** Remove kirkeskat. Only members of the Danish National Church pay kirkeskat. Confirm membership status.

### EC5 -- Capital expenditure expensed directly [T1]
**Situation:** Client buys equipment for DKK 25,000 and deducts full amount as an expense.
**Resolution:** If above DKK 15,400 (straksafskrivning limit), must be added to the driftsmiddel pool and depreciated at up to 25% declining balance. Remove from expenses; add to depreciation schedule.

### EC6 -- VSO withdrawal not taxed [T1]
**Situation:** Client withdraws opsparet overskud from VSO but does not report as personal income.
**Resolution:** Withdrawals from VSO opsparet overskud are taxable as personal income in the year of withdrawal. The 22% interim tax paid is credited against the final tax. Must be reported.

### EC7 -- Representation expenses fully deducted [T1]
**Situation:** Client deducts DKK 4,000 in client entertainment (representation) at 100%.
**Resolution:** Only 25% of representation expenses are deductible for tax purposes. Deductible amount = DKK 4,000 x 25% = DKK 1,000.

### EC8 -- Personfradrag doubled for married couple [T2]
**Situation:** Married couple where one spouse has no income; client claims double personfradrag.
**Resolution:** An unused personfradrag can be transferred between spouses for bundskat purposes only (not for topskat). [T2] Flag for reviewer to confirm correct transfer computation.

### EC9 -- First year B-skat estimation [T2]
**Situation:** New self-employed person does not know how much B-skat to pay.
**Resolution:** Must estimate expected income and report to SKAT via TastSelv. If no estimate filed, SKAT sets B-skat at DKK 0. Underpayment interest will apply if actual income is significant. [T2] Advise client to estimate conservatively.

### EC10 -- Moms included in revenue figure [T1]
**Situation:** Momsregistreret client reports DKK 125,000 gross receipts including 25% moms.
**Resolution:** Revenue for income tax = DKK 100,000. The DKK 25,000 moms collected is a liability to SKAT, not income. Exclude from Box 1 / gross revenue.

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
Action Required: Qualified revisor must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified revisor. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard self-employed, mid-range income
**Input:** Self-employed, Copenhagen (kommuneskat 23.8%), not Folkekirken member, gross revenue DKK 600,000, allowable expenses DKK 150,000, no VSO/KAO, no other income.
**Expected output:** AM-bidrag = DKK 600,000 x 8% = DKK 48,000. Personal income after AM = DKK 552,000. Net income = DKK 552,000 - DKK 150,000 = DKK 402,000. Below topskat threshold (DKK 611,800 on personal income after AM). Personfradrag tax value = DKK 51,600 x (12.01% + 23.8%) = DKK 18,477. Bundskat = DKK 402,000 x 12.01% = DKK 48,280. Kommuneskat = DKK 402,000 x 23.8% = DKK 95,676. Total before personfradrag credit = DKK 143,956. Less personfradrag credit = DKK 18,477. Tax on income = DKK 125,479. Plus AM-bidrag = DKK 48,000. Total tax = DKK 173,479.

### Test 2 -- High income, topskat applies
**Input:** Self-employed, Aarhus (kommuneskat 24.6%), Folkekirken member (kirkeskat 0.71%), gross revenue DKK 1,000,000, allowable expenses DKK 200,000, no VSO.
**Expected output:** AM-bidrag = DKK 80,000. Personal income after AM = DKK 920,000. Above topskat threshold: topskat on DKK 920,000 - DKK 611,800 = DKK 308,200 x 15% = DKK 46,230. Plus bundskat, kommuneskat, kirkeskat on taxable income.

### Test 3 -- Virksomhedsordningen retained profit
**Input:** Self-employed using VSO, net business profit DKK 500,000, retains DKK 300,000 in VSO as opsparet overskud.
**Expected output:** DKK 300,000 taxed at 22% interim = DKK 66,000. Remaining DKK 200,000 (after AM-bidrag on full gross) taxed as personal income at progressive rates.

### Test 4 -- Capital item incorrectly expensed
**Input:** Client purchases computer for DKK 20,000, deducts full amount as expense.
**Expected output:** Above DKK 15,400 straksafskrivning threshold. Must enter driftsmiddel pool. Year 1 depreciation: DKK 20,000 x 25% = DKK 5,000. Remove DKK 20,000 from expenses; add DKK 5,000 depreciation.

### Test 5 -- Representation expense overclaimed
**Input:** Client deducts DKK 8,000 representation at 100%.
**Expected output:** Only 25% deductible. Correct deduction = DKK 2,000. Remove DKK 6,000 from deductible expenses.

### Test 6 -- Moms included in income
**Input:** Momsregistreret client reports DKK 750,000 including 25% moms.
**Expected output:** Net revenue = DKK 600,000. Moms of DKK 150,000 excluded from taxable revenue.

### Test 7 -- B-skat instalment schedule
**Input:** Client expects DKK 80,000 total tax for the year.
**Expected output:** 10 monthly instalments of DKK 8,000 each (Jan--May, Aug--Dec).

---

## PROHIBITIONS

- NEVER compute AM-bidrag on net income -- it is always 8% on GROSS personal income
- NEVER apply topskat to income below DKK 611,800 (after AM-bidrag)
- NEVER charge kirkeskat without confirming Folkekirken membership
- NEVER include moms collected in taxable revenue for momsregistrerede clients
- NEVER allow capital expenditure above DKK 15,400 to be expensed directly -- must enter driftsmiddel pool
- NEVER advise on VSO/KAO choice without modelling both scenarios -- flag for reviewer
- NEVER allow 100% deduction of representation expenses -- maximum 25%
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their revisor for confirmation
- NEVER treat VSO opsparet overskud withdrawals as tax-free
- NEVER advise on international income or dual residency -- escalate to T3

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a statsautoriseret revisor, registreret revisor, or equivalent licensed practitioner in Denmark) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
