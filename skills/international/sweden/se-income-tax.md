---
name: se-income-tax
description: Use this skill whenever asked about Swedish income tax for self-employed individuals (enskild firma / enskild näringsidkare). Trigger on phrases like "Swedish tax", "kommunalskatt", "statlig inkomstskatt", "jobbskatteavdrag", "grundavdrag", "NE-bilaga", "F-skatt", "expansionsfond", "räntefördelning", "Inkomstdeklaration 1", "self-employed tax Sweden", or any question about filing or computing income tax for a Swedish self-employed client. Covers kommunalskatt, statlig inkomstskatt, jobbskatteavdrag, grundavdrag, egenavgifter, F-skatt, expansionsfond, räntefördelning, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Swedish income tax work.
---

# Sweden Income Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Sweden |
| Jurisdiction Code | SE |
| Primary Legislation | Inkomstskattelagen (IL, 1999:1229); Skatteförfarandelagen (SFL, 2011:1244) |
| Supporting Legislation | Socialavgiftslagen (SAL, 2000:980); Bokföringslagen (BFL, 1999:1078) |
| Tax Authority | Skatteverket (Swedish Tax Agency) |
| Filing Portal | skatteverket.se / Mina sidor |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Swedish auktoriserad or godkänd revisor |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: kommunalskatt, statlig skatt threshold, grundavdrag, filing deadlines. Tier 2: jobbskatteavdrag computation, expansionsfond/räntefördelning choice, mixed-use expense apportionment. Tier 3: international income, 3:12 rules (fåmansbolag), complex restructuring. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified revisor must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Business form** [T1] -- enskild firma (sole proprietorship), freelancer, or other
2. **Municipality of residence** [T1] -- determines kommunalskatt rate
3. **Gross business revenue** [T1] -- total invoiced/received in the year
4. **Business expenses** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items)
5. **Age at start of income year** [T1] -- affects grundavdrag and jobbskatteavdrag amounts
6. **Other income** [T1] -- employment income, capital income (inkomst av kapital)
7. **Net business assets** [T1] -- for räntefördelning and expansionsfond calculations
8. **F-skatt registration** [T1] -- required for self-employed status
9. **Prior year losses** [T1] -- carried forward underskudd

**If municipality is unknown, use the national average kommunalskatt of 32.41% (2025). Flag as estimated.**

---

## Step 1: Income Tax Rates (2025) [T1]

**Legislation:** Inkomstskattelagen (IL) kap. 65

### Kommunalskatt (Municipal + Regional Tax)

| Item | Rate (2025) |
|------|-------------|
| Average kommunalskatt | 32.41% |
| Range | 28.98% (Österåker) to 35.30% (Degerfors) |
| Applied to | Taxable earned income (beskattningsbar förvärvsinkomst) |

### Statlig Inkomstskatt (State Income Tax)

| Item | Amount / Rate (2025) |
|------|----------------------|
| Brytpunkt (threshold) -- under age 66 | SEK 625,800 taxable earned income |
| Brytpunkt (threshold) -- age 66+ | SEK 733,200 taxable earned income |
| Rate above brytpunkt | 20% |
| Below brytpunkt | 0% state tax |

**Note:** The brytpunkt of SEK 625,800 refers to taxable earned income (after grundavdrag). The corresponding gross income level is approximately SEK 643,100 (before grundavdrag for a typical earner under 66).

### Grundavdrag (Basic Deduction) [T1]

| Item | Amount (2025) |
|------|---------------|
| Minimum grundavdrag (born 1959 or later) | SEK 17,300 |
| Maximum grundavdrag (born 1959 or later) | SEK 45,300 |
| Maximum grundavdrag (age 66+ at start of year) | SEK 86,500 |

Grundavdrag is income-dependent and computed automatically by Skatteverket based on total earned income. It reduces taxable earned income before both kommunalskatt and statlig skatt are applied.

---

## Step 2: Egenavgifter (Self-Employment Contributions) [T1]

**Legislation:** Socialavgiftslagen (SAL)

| Item | Rate (2025) |
|------|-------------|
| Full egenavgifter | 28.97% |
| Reduced rate (born 1959 or earlier, age 66+) | 10.21% |
| Applied to | Överskudd av näringsverksamhet (net business profit) |
| Deductibility | Egenavgifter are deductible against business income |

### Schablonavdrag (Standard Deduction for Egenavgifter) [T1]

Since egenavgifter are calculated on the same profit they reduce, a standard deduction (schablonavdrag) of 25% of net business income is allowed as a preliminary reduction. The actual egenavgifter are computed on the return and reconciled.

**Computation:**
1. Net business profit before egenavgifter = X
2. Schablonavdrag = X x 25% = Y
3. Taxable business income = X - Y
4. Actual egenavgifter computed on final taxable business income

---

## Step 3: Jobbskatteavdrag (Earned Income Tax Credit) [T2]

**Legislation:** IL kap. 67

| Item | Detail (2025) |
|------|---------------|
| Nature | Tax credit reducing kommunalskatt (not statlig skatt) |
| Maximum reduction | Approximately SEK 44,000--46,000/year for average earners |
| Eligibility | All earned income (both employment and business income) |
| Computation | Complex formula based on earned income, kommunalskatt rate, and age |

The jobbskatteavdrag is computed automatically by Skatteverket. It is a non-refundable credit that reduces kommunalskatt payable. Self-employed persons are eligible for jobbskatteavdrag on their business income.

**[T2] The exact jobbskatteavdrag amount depends on a complex formula. Flag for reviewer if precise amount is critical to advice.**

---

## Step 4: NE-bilaga (Business Income Attachment) [T1]

**Legislation:** SFL; Skatteverkets föreskrifter

The NE-bilaga is the attachment to Inkomstdeklaration 1 where self-employed individuals report their business income and expenses.

### Key NE-bilaga Fields

| Field | Description |
|-------|-------------|
| R1 | Gross revenue (intäkter) |
| R2 | Cost of goods sold |
| R3--R6 | Operating expenses (by category) |
| R7 | Depreciation (avskrivningar) |
| R8 | Other expenses |
| R9 | Net business result (överskudd/underskudd) |
| R14 | Sjukpenninggrundande inkomst (SGI -- sickness benefit base) |
| R24 | Räntefördelning (interest allocation) |
| R33--R35 | Expansionsfond (expansion fund) |

---

## Step 5: Allowable Deductions [T1/T2]

**Legislation:** IL kap. 16 (näringsverksamhet deductions)

### The General Deduction Rule [T1]

An expense is deductible if it is incurred for the purpose of acquiring and maintaining income in the business (IL 16:1). Mixed-use expenses must be apportioned.

### Deductible Expenses

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent (dedicated) | T1 | Fully deductible |
| Professional insurance | T1 | Fully deductible |
| Accountancy / revisor fees | T1 | Fully deductible |
| Office supplies | T1 | Fully deductible |
| Software subscriptions (business use) | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Business bank charges | T1 | Fully deductible |
| Professional development | T1 | Fully deductible if related to current business |
| Travel (business purpose) | T1 | Fully deductible; traktamente (per diem) rates apply |
| Phone / internet | T2 | Business use portion only |
| Motor vehicle expenses | T2 | Business use portion or standard rate per km |
| Home office | T2 | Proportional or standard deduction |
| Representation (limited) | T1 | Internal: SEK 300/person/event; external: no food deduction (only simpler refreshments) |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Private living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Not deductible |
| Capital expenditure | Depreciated, not expensed (unless under SEK 5,000 half-price base) |
| Personal drawings (egna uttag) | Not an expense |

### Home Office Rules [T2]

- Dedicated room exclusively for business: deduct proportional share of housing costs
- Standard deduction: SEK 2,000/year for home office (without documentation requirements)
- If actual costs exceed standard: document with floor area calculation
- [T2] Flag for reviewer to confirm workspace qualifies

### Motor Vehicle Rules [T2]

- Standard rate: SEK 25.00/mil (2025) for business travel using private car
- Alternative: actual costs with logbook apportionment
- [T2] Flag for reviewer to confirm business km documentation

---

## Step 6: Depreciation (Avskrivningar) [T1]

**Legislation:** IL kap. 18, 19, 20

### Methods and Rates

| Asset Type | Method | Rate |
|-----------|--------|------|
| Inventarier (machinery, equipment) -- main rule | Declining balance (pool) | 30% (räkenskapsenlig avskrivning) |
| Inventarier -- supplementary rule | Straight-line | 20% per year |
| Buildings (business) | Straight-line | 2--5% depending on building type |
| Goodwill | Declining balance (pool) | 30% (pooled with inventarier) |
| Markanläggning (land improvements) | Straight-line | 5% or 10% |

### Rules [T1]

- Inventarier pooled together; 30% declining balance on pool value
- Low-value assets under approximately SEK 5,000 (half a prisbasbelopp): may be expensed immediately (direktavdrag)
- Assets with expected useful life under 3 years: expensed immediately regardless of cost
- Supplementary rule guarantees full deduction over 5 years even if declining balance is slower

---

## Step 7: Expansionsfond (Expansion Fund) [T2]

**Legislation:** IL kap. 34

| Item | Detail (2025) |
|------|---------------|
| Tax rate on allocation | 20.6% (same as bolagsskatt) |
| Maximum allocation | Limited by net business assets (kapitalunderlag) |
| Effect | Defers taxation -- profit set aside taxed at 20.6% now; taxed as personal income when reversed |
| Reversal | Taxed as business income in the year of reversal |
| Mandatory reversal | On cessation of business |

**When advantageous:** Business income is high and expected to be lower in future years; or when retaining capital for expansion. Effectively lets a sole proprietor pay "company tax" on retained earnings.

**[T2] Expansionsfond allocation requires accurate calculation of kapitalunderlag using SKV 2196. Flag for reviewer.**

---

## Step 8: Räntefördelning (Interest Allocation) [T2]

**Legislation:** IL kap. 33

| Item | Detail (2025) |
|------|---------------|
| Positiv räntefördelning rate | 2.96% (statslåneräntan + 6 percentage points) |
| Negativ räntefördelning threshold | Capital deficit exceeding SEK 500,000 change during year |
| Effect of positive | Portion of business income reclassified as capital income (taxed at 30% instead of marginal rate) |
| Effect of negative | Portion of capital income reclassified as business income (taxed at marginal rate) |

### Positive Räntefördelning [T2]

- If net business assets at start of year are positive and exceed SEK 50,000
- Räntefördelningsbelopp = net positive assets x 2.96%
- This amount is moved from business income to capital income (inkomst av kapital, taxed at 30%)
- Beneficial when marginal tax rate on business income exceeds 30%

**[T2] Requires accurate balance sheet. Flag for reviewer to confirm asset valuation.**

---

## Step 9: F-skatt (Preliminary Tax) [T1]

**Legislation:** SFL kap. 55

| Item | Detail |
|------|--------|
| Requirement | All self-employed must register for F-skatt |
| Payment | Monthly instalments based on estimated income |
| Adjustment | Can be adjusted via skatteverket.se during the year |
| Debiterad preliminärskatt | Set by Skatteverket or self-assessed via preliminary income declaration |

### F-skatt vs FA-skatt [T1]

| Type | Who |
|------|-----|
| F-skatt | Solely self-employed |
| FA-skatt | Self-employed AND employed (combined) |
| A-skatt | Employed only (employer withholds) |

Self-employed persons without F-skatt registration will have difficulty invoicing clients, as the client becomes responsible for employer contributions on payments to non-F-skatt holders.

---

## Step 10: Filing Deadlines [T1]

**Legislation:** SFL

| Filing / Payment | Deadline |
|-----------------|----------|
| Inkomstdeklaration 1 (digital filing) | 2 May of the following year |
| Inkomstdeklaration 1 (paper filing) | Earlier deadline -- typically mid-March (verify annually) |
| Extension (via revisor / ombud) | 16 June |
| F-skatt monthly instalments | 12th of each month |
| Slutskattebesked (final tax assessment) | Typically August--December |

---

## Step 11: Penalties [T1]

**Legislation:** SFL kap. 48, 49

| Offence | Penalty |
|---------|---------|
| Late filing of Inkomstdeklaration | Förseningsavgift: SEK 6,250 (first offence); SEK 12,500 (second); SEK 18,750 (third within 5 years) |
| Incorrect return (negligence) | Skattetillägg: 40% of the tax on understated income |
| Incorrect return (periodic taxation) | Skattetillägg: 10% on periodic returns |
| Voluntary correction | Reduced or no skattetillägg |
| Late payment of F-skatt | Interest (kostnadsränta) at statutory rate |

---

## Step 12: Interaction with Moms (VAT) [T1]

**Legislation:** Mervärdesskattelagen (ML)

| Scenario | Income Tax Treatment |
|----------|---------------------|
| Moms collected on sales (momsregistrerad) | NOT income -- liability to Skatteverket. Exclude from R1 revenue. |
| Input moms recovered | NOT an expense -- reclaimable. Exclude from costs. |
| Non-deductible moms (e.g., representation) | IS an expense -- adds to cost |
| Not momsregistrerad (under SEK 80,000 turnover, 2025) | No moms charged; no input moms reclaimed; gross = net |

---

## Step 13: Record Keeping [T1]

**Legislation:** Bokföringslagen (BFL)

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 7 years from end of calendar year |
| What to keep | Verifikationer (vouchers), bokföring (accounts), annual accounts, contracts |
| Format | Digital or paper (BFL allows digital; original must be verifiable) |
| Standard | Must follow god redovisningssed (generally accepted accounting principles) |

---

## Step 14: Edge Case Registry

### EC1 -- Statlig skatt applied below brytpunkt [T1]
**Situation:** Client applies 20% statlig inkomstskatt on income below SEK 625,800.
**Resolution:** INCORRECT. Statlig skatt only applies to taxable earned income ABOVE SEK 625,800 (under age 66). Remove statlig skatt from income below this threshold.

### EC2 -- Egenavgifter not deducted [T1]
**Situation:** Client computes tax on full business profit without deducting egenavgifter.
**Resolution:** INCORRECT. Egenavgifter are deductible against business income. Apply 25% schablonavdrag on net profit as preliminary deduction. Reconcile with actual egenavgifter on the return.

### EC3 -- Capital expenditure expensed directly [T1]
**Situation:** Client buys equipment for SEK 15,000 and deducts full amount as expense.
**Resolution:** Above half prisbasbelopp (approximately SEK 5,000 in 2025) and useful life over 3 years. Must enter inventarier pool. Depreciation year 1 = 30% of SEK 15,000 = SEK 4,500. Remove from expenses; add to depreciation.

### EC4 -- Moms included in revenue [T1]
**Situation:** Momsregistrerad client reports SEK 500,000 including 25% moms.
**Resolution:** Revenue for income tax (NE R1) = SEK 400,000. The SEK 100,000 moms is a liability, not income.

### EC5 -- Expansionsfond reversed without taxation [T1]
**Situation:** Client closes business and does not report reversal of SEK 200,000 expansionsfond.
**Resolution:** INCORRECT. Expansionsfond must be reversed and taxed as business income upon cessation. The 20.6% tax previously paid is credited. Remaining amount taxed at marginal rate.

### EC6 -- Negative räntefördelning ignored [T2]
**Situation:** Client has large negative capital in business (deficit exceeding SEK 500,000 change) but does not apply negative räntefördelning.
**Resolution:** Mandatory negative räntefördelning may apply, reclassifying capital income as business income. [T2] Flag for reviewer to confirm threshold and computation.

### EC7 -- Jobbskatteavdrag claimed on capital income [T1]
**Situation:** Client applies jobbskatteavdrag to reduce tax on rental or investment income.
**Resolution:** INCORRECT. Jobbskatteavdrag applies only to earned income (förvärvsinkomst), not capital income (inkomst av kapital).

### EC8 -- F-skatt not registered [T1]
**Situation:** Client operates as enskild firma but has not registered for F-skatt.
**Resolution:** Must register for F-skatt immediately. Without F-skatt, clients paying the individual are treated as employers and must pay arbetsgivaravgifter on the payments.

### EC9 -- Home office standard deduction combined with actual costs [T2]
**Situation:** Client claims both SEK 2,000 standard deduction and actual home office costs.
**Resolution:** INCORRECT. Must choose one method -- either standard deduction OR actual costs. Cannot combine. [T2] Flag for reviewer.

### EC10 -- Representation food costs deducted [T1]
**Situation:** Client deducts SEK 5,000 for restaurant meals with external business contacts.
**Resolution:** External representation food costs are NOT deductible for income tax (even though limited moms deduction may apply). Only simpler refreshments (enklare förtäring) up to SEK 300/person are deductible for internal events.

---

## Step 15: Reviewer Escalation Protocol

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

## Step 16: Test Suite

### Test 1 -- Standard self-employed, mid-range income
**Input:** Enskild firma, Stockholm (kommunalskatt 30.44%), born 1985, gross revenue SEK 800,000, allowable expenses SEK 200,000, no expansionsfond or räntefördelning.
**Expected output:** Net business profit = SEK 600,000. Schablonavdrag for egenavgifter = SEK 600,000 x 25% = SEK 150,000. Taxable business income = SEK 450,000. Grundavdrag approximately SEK 17,300. Beskattningsbar förvärvsinkomst = SEK 432,700. Below brytpunkt (SEK 625,800): no statlig skatt. Kommunalskatt = SEK 432,700 x 30.44% = approx SEK 131,714. Less jobbskatteavdrag. Plus egenavgifter (28.97% on adjusted base).

### Test 2 -- High income, statlig skatt applies
**Input:** Enskild firma, kommunalskatt 32.41%, born 1980, net business income SEK 900,000.
**Expected output:** After schablonavdrag and grundavdrag, taxable earned income exceeds SEK 625,800. Statlig skatt at 20% applies to the excess.

### Test 3 -- Expansionsfond allocation
**Input:** Net business income SEK 500,000, client allocates SEK 200,000 to expansionsfond.
**Expected output:** Expansionsfondsskatt = SEK 200,000 x 20.6% = SEK 41,200. Taxable business income reduced to SEK 300,000 (before egenavgifter schablonavdrag).

### Test 4 -- Capital item expensed
**Input:** Client buys office furniture for SEK 20,000, deducts full amount.
**Expected output:** Above half prisbasbelopp, useful life over 3 years. Enter inventarier pool. Depreciation = SEK 20,000 x 30% = SEK 6,000 year 1. Remove SEK 20,000 from expenses; add SEK 6,000.

### Test 5 -- Moms included in revenue
**Input:** Momsregistrerad client reports SEK 1,250,000 gross receipts including 25% moms.
**Expected output:** NE R1 revenue = SEK 1,000,000. Moms of SEK 250,000 excluded.

### Test 6 -- F-skatt instalment
**Input:** Client expects total F-skatt of SEK 120,000 for the year.
**Expected output:** 12 monthly instalments of SEK 10,000 each, due 12th of each month.

### Test 7 -- Räntefördelning applied
**Input:** Net business assets at start of year SEK 500,000. Business income SEK 400,000.
**Expected output:** Räntefördelningsbelopp = SEK 500,000 x 2.96% = SEK 14,800. This amount reclassified from business income (marginal rate) to capital income (30%). Taxable business income reduced to SEK 385,200.

---

## PROHIBITIONS

- NEVER apply statlig inkomstskatt to income below the brytpunkt (SEK 625,800 taxable earned income, under age 66)
- NEVER forget to deduct egenavgifter (or schablonavdrag) from business income before computing tax
- NEVER include moms collected in NE-bilaga revenue for momsregistrerade clients
- NEVER allow capital expenditure above half prisbasbelopp (with life over 3 years) to be expensed directly
- NEVER allow food costs for external representation as a deduction
- NEVER combine standard home office deduction with actual cost deduction
- NEVER ignore mandatory negative räntefördelning when thresholds are exceeded
- NEVER apply jobbskatteavdrag to capital income
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their revisor
- NEVER advise on international income, 3:12 rules (fåmansbolag), or complex restructuring -- escalate to T3

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an auktoriserad revisor, godkänd revisor, or equivalent licensed practitioner in Sweden) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
