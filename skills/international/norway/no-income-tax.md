---
name: no-income-tax
description: Use this skill whenever asked about Norwegian income tax for self-employed individuals (enkeltpersonforetak). Trigger on phrases like "Norwegian tax", "trinnskatt", "alminnelig inntekt", "personfradrag", "skattemelding", "RF-1175", "næringsoppgave", "enkeltpersonforetak", "self-employed tax Norway", or any question about filing or computing income tax for a Norwegian self-employed client. Covers alminnelig inntekt (22%), trinnskatt (5 brackets), personfradrag, næringsinntekt computation, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Norwegian income tax work.
---

# Norway Income Tax -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Norway |
| Jurisdiction Code | NO |
| Primary Legislation | Skatteloven (Tax Act); Skatteforvaltningsloven (Tax Administration Act) |
| Supporting Legislation | Folketrygdloven (National Insurance Act); Bokforingsloven (Bookkeeping Act) |
| Tax Authority | Skatteetaten (Norwegian Tax Administration) |
| Filing Portal | skatteetaten.no / Altinn |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Norwegian statsautorisert or registrert revisor |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: alminnelig inntekt rate, trinnskatt brackets, personfradrag, filing deadlines. Tier 2: næringsinntekt adjustments, mixed-use expense apportionment, home office. Tier 3: international income, permanent establishment, complex restructuring. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified revisor must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Business form** [T1] -- enkeltpersonforetak (sole proprietorship), freelancer, or other
2. **Gross business revenue** [T1] -- total invoiced/received in the year
3. **Business expenses** [T1/T2] -- nature and amount of each expense (T2 for mixed-use items)
4. **Municipality of residence** [T1] -- all municipalities use same rates for alminnelig inntekt; relevant for trygdeavgift
5. **Other income** [T1] -- employment income, capital income, rental income
6. **Trygdeavgift class** [T1] -- næringsinntekt uses a higher trygdeavgift rate (11.0%) than employment income
7. **Assets in business** [T1] -- for depreciation schedule (saldogrupper)
8. **Prior year losses** [T1] -- carried forward underskudd (losses)

**If business form is unknown, STOP. The trygdeavgift rate depends on whether income is næringsinntekt or lønnsinntekt.**

---

## Step 1: Alminnelig Inntekt (General Income Tax) [T1]

**Legislation:** Skatteloven ss 15-2

| Item | Rate / Amount (2025) |
|------|----------------------|
| Alminnelig inntekt rate | 22% flat |
| Applied to | Net income after all deductions |
| Personfradrag (personal allowance) | NOK 108,550 (class 1) |

Alminnelig inntekt is a flat 22% tax on net income (all income sources minus all deductions minus personfradrag). It applies to both personal and capital income.

---

## Step 2: Trinnskatt (Bracket Surtax) [T1]

**Legislation:** Stortingsvedtak om skatt av inntekt og formue

### Trinnskatt Rates (2025)

| Bracket (Trinn) | Income Range (NOK) | Rate |
|-----------------|-------------------|------|
| Trinn 1 | 217,401 -- 306,050 | 1.7% |
| Trinn 2 | 306,051 -- 697,150 | 4.0% |
| Trinn 3 | 697,151 -- 942,400 | 13.7% |
| Trinn 4 | 942,401 -- 1,410,750 | 16.7% |
| Trinn 5 | Above 1,410,750 | 17.7% |

Trinnskatt applies to gross personal income (personinntekt) -- NOT to alminnelig inntekt. For self-employed, personinntekt is computed from næringsinntekt after certain adjustments (skjermingsfradrag).

**Trinnskatt is cumulative.** Each bracket's rate applies only to the income within that bracket.

---

## Step 3: Trygdeavgift (National Insurance Contribution) [T1]

**Legislation:** Folketrygdloven ss 23-3

| Income Type | Rate (2025) |
|-------------|-------------|
| Næringsinntekt (self-employment income) | 11.0% |
| Lønnsinntekt (employment income) | 7.9% |
| Pensjonsinntekt (pension income) | 5.1% |

For self-employed individuals, trygdeavgift at 11.0% is applied to personinntekt from business activities. There is a lower threshold below which no trygdeavgift is due (approximately NOK 69,650 in 2025).

---

## Step 4: Næringsinntekt Computation (RF-1175) [T1/T2]

**Legislation:** Skatteloven kap. 5, 6; RF-1175 form guidance

### Computation Steps [T1]

1. **Gross business revenue** -- all invoiced/received income from business activity
2. **Less: Cost of goods sold** -- direct costs of products/services
3. **Less: Operating expenses** -- see Step 5 for deductible expenses
4. **Less: Depreciation** -- saldoavskrivninger per Step 6
5. **= Net business income (næringsinntekt)**
6. **Less: Skjermingsfradrag** -- shields a portion of business return from high marginal rates [T2]

### RF-1175 Næringsoppgave 1 [T1]

| Requirement | Detail |
|-------------|--------|
| Who must file | All enkeltpersonforetak with gross revenue above NOK 50,000 |
| Exemption | Gross revenue NOK 50,000 or below: exempt from filing næringsoppgave |
| Attachment | Filed as attachment to skattemelding via Altinn |

### Skjermingsfradrag (Shielding Deduction) [T2]

- Shields a risk-free return on business capital from trinnskatt and trygdeavgift
- Computed as: net positive business assets x skjermingsrente (set annually by Ministry of Finance)
- Reduces personinntekt (not alminnelig inntekt)
- [T2] Flag for reviewer: computation requires accurate balance sheet valuation

---

## Step 5: Allowable Deductions [T1/T2]

**Legislation:** Skatteloven ss 6-1 (general deduction rule)

### The General Deduction Rule [T1]

An expense is deductible if it has a sufficient connection to taxable income (tilknytningskravet). The expense must be incurred to acquire, secure, or maintain taxable income.

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
| Professional development / courses | T1 | Fully deductible if related to current business |
| Travel (business purpose) | T1 | Fully deductible; standard rates or actual costs |
| Phone / internet | T2 | Business use portion only |
| Motor vehicle expenses | T2 | Business use portion or standard rate per km |
| Home office | T2 | Proportional -- see home office rules |
| Representation (business entertaining) | T1 | Deductible up to NOK 559/person per event (2025) |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Private living expenses | Not connected to income |
| Fines and penalties | Public policy |
| Income tax and trygdeavgift | Not deductible against income |
| Capital expenditure | Depreciated via saldogrupper, not expensed |
| Personal drawings | Not an expense |
| Costs of acquiring education for a new profession | Education for current profession OK; new profession blocked |

### Home Office Rules [T2]

- Dedicated room used exclusively for business: deduct proportional share of housing costs
- Standard deduction: NOK 2,050/year (2025) for home office as alternative to actual costs
- Room must be exclusively used for business -- dual-use rooms do not qualify
- [T2] Flag for reviewer to confirm workspace arrangement

### Motor Vehicle Rules [T2]

- Standard rate for business km: NOK 3.50/km (2025, verify annually)
- Alternative: actual costs apportioned by business-use percentage with logbook
- [T2] Flag for reviewer to confirm business km documentation

### Minstefradrag -- NOT for Self-Employed [T1]

**Minstefradrag (minimum standard deduction) does NOT apply to næringsinntekt.** It only applies to employment income (lønnsinntekt). Self-employed persons must deduct actual documented expenses.

---

## Step 6: Depreciation (Saldoavskrivninger) [T1]

**Legislation:** Skatteloven ss 14-40 to 14-48

### Saldogrupper (Depreciation Groups)

| Group | Asset Type | Max Rate |
|-------|-----------|----------|
| a | Office machines, equipment | 30% |
| b | Acquired goodwill | 20% |
| c | Trucks, buses, vans | 24% |
| d | Passenger cars, machinery, fixtures | 20% |
| e | Ships, boats | 14% |
| f | Aircraft | 12% |
| g | Technical installations in buildings | 10% |
| h | Commercial buildings (hotels, car parks) | 4% |
| i | Office/business buildings | 2% |
| j | Technical installations in buildings (electrically operated) | 10% |

### Rules [T1]

- Declining balance method on each group's pool
- Assets pooled by group; depreciation applied to the group's opening balance + additions - disposals
- Low-value assets under NOK 15,000: may be expensed immediately
- Assets with expected useful life under 3 years: may be expensed immediately regardless of cost

---

## Step 7: Filing Deadlines [T1]

**Legislation:** Skatteforvaltningsloven

| Filing / Payment | Deadline |
|-----------------|----------|
| Skattemelding (tax return) | 30 April of the following year |
| RF-1175 Næringsoppgave | Filed with skattemelding (30 April) |
| Forskuddsskatt (preliminary tax) instalments | 15 March, 15 June, 15 September, 15 December |
| Extension | Not normally available; late filing attracts penalties |

### Forskuddsskatt (Preliminary Tax) [T1]

- Self-employed must pay forskuddsskatt in 4 quarterly instalments
- Based on expected income for the current year
- Can be adjusted via skatteetaten.no during the year
- Underpayment attracts restskatt (additional tax) with interest

---

## Step 8: Penalties [T1]

**Legislation:** Skatteforvaltningsloven kap. 14

| Offence | Penalty |
|---------|---------|
| Late filing of skattemelding | Tvangsmulkt: NOK 641/day, capped at approximately NOK 64,100 |
| Failure to file næringsoppgave | Skjønnsligning (estimated assessment) by Skatteetaten |
| Incorrect return (negligence) | Tilleggsskatt: 20% of the tax on understated income |
| Incorrect return (gross negligence) | Tilleggsskatt: 40% of the tax on understated income |
| Fraud | Tilleggsskatt: 60% + criminal prosecution |
| Late payment of restskatt | Interest at statutory rate |

---

## Step 9: Interaction with MVA (Merverdiavgift / VAT) [T1]

**Legislation:** Merverdiavgiftsloven

| Scenario | Income Tax Treatment |
|----------|---------------------|
| MVA collected on sales (MVA-registered) | NOT income -- liability to Skatteetaten. Exclude from revenue. |
| Input MVA recovered | NOT an expense -- reclaimable. Exclude from expenses. |
| Non-deductible MVA (e.g., representation) | IS an expense -- adds to cost |
| Not MVA-registered (under NOK 50,000 turnover) | No MVA charged; no input MVA reclaimed; gross = net |

---

## Step 10: Record Keeping [T1]

**Legislation:** Bokforingsloven

| Requirement | Detail |
|-------------|--------|
| Minimum retention period | 5 years from end of financial year |
| What to keep | All sales documentation, purchase documentation, bank statements, contracts, asset register |
| Format | Digital storage required (bokforingsloven 2023 requirements) |
| Standard | Must follow Norwegian bookkeeping standards (god bokforingsskikk) |

---

## Step 11: Edge Case Registry

### EC1 -- Minstefradrag claimed on næringsinntekt [T1]
**Situation:** Self-employed client claims minstefradrag on business income.
**Resolution:** INCORRECT. Minstefradrag applies only to employment income (lønnsinntekt). Self-employed must deduct actual documented expenses. Remove minstefradrag from næringsinntekt computation.

### EC2 -- Trygdeavgift at employment rate [T1]
**Situation:** Client applies 7.9% trygdeavgift to næringsinntekt.
**Resolution:** INCORRECT. Næringsinntekt trygdeavgift is 11.0%, not 7.9%. The 7.9% rate is for lønnsinntekt only.

### EC3 -- Trinnskatt applied to alminnelig inntekt [T1]
**Situation:** Client computes trinnskatt on net taxable income (alminnelig inntekt).
**Resolution:** INCORRECT. Trinnskatt applies to personinntekt (gross personal income less skjermingsfradrag), NOT alminnelig inntekt. Recalculate on correct base.

### EC4 -- Capital expenditure expensed directly [T1]
**Situation:** Client buys equipment for NOK 30,000 and deducts full amount as an expense.
**Resolution:** Above NOK 15,000 and expected life over 3 years. Must enter appropriate saldogruppe. Add to depreciation schedule at applicable group rate.

### EC5 -- MVA included in revenue [T1]
**Situation:** MVA-registered client reports NOK 500,000 gross receipts including 25% MVA.
**Resolution:** Revenue for income tax = NOK 400,000. The NOK 100,000 MVA collected is a liability, not income. Exclude from revenue.

### EC6 -- Home office in dual-use room [T2]
**Situation:** Client works from living room and claims 30% of housing costs.
**Resolution:** Dual-use room does NOT qualify for actual cost apportionment. Client may claim the standard deduction of NOK 2,050/year. [T2] Flag for reviewer.

### EC7 -- Forskuddsskatt not paid [T1]
**Situation:** Client did not pay forskuddsskatt instalments during the year.
**Resolution:** All tax becomes restskatt due on assessment. Interest will be charged. The full tax liability plus interest is due. Advise client to set up forskuddsskatt immediately for the current year.

### EC8 -- Losses carried forward [T1]
**Situation:** Client had NOK 100,000 loss in prior year, now has NOK 200,000 profit.
**Resolution:** Prior year losses (underskudd) carry forward and reduce alminnelig inntekt. Taxable alminnelig inntekt = NOK 200,000 - NOK 100,000 = NOK 100,000. Loss carry-forward has no time limit in Norway.

### EC9 -- RF-1175 exemption misapplied [T1]
**Situation:** Client with NOK 80,000 gross revenue believes they are exempt from filing næringsoppgave.
**Resolution:** INCORRECT. Exemption applies only if gross revenue is NOK 50,000 or below. At NOK 80,000, RF-1175 must be filed with the skattemelding.

### EC10 -- Education deduction for new profession [T1]
**Situation:** Self-employed consultant pays NOK 50,000 for a law degree, claiming it as a business expense.
**Resolution:** NOT deductible. Education for a new profession is not deductible. Only courses maintaining or updating skills in the current profession qualify.

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
**Input:** Enkeltpersonforetak, gross revenue NOK 800,000, allowable expenses NOK 200,000, no other income, no prior losses.
**Expected output:** Næringsinntekt = NOK 600,000. Alminnelig inntekt = NOK 600,000 - NOK 108,550 (personfradrag) = NOK 491,450 x 22% = NOK 108,119. Trinnskatt: Trinn 1 (NOK 217,401--306,050) = NOK 88,649 x 1.7% = NOK 1,507. Trinn 2 (NOK 306,051--600,000) = NOK 293,949 x 4.0% = NOK 11,758. Trygdeavgift = NOK 600,000 x 11.0% = NOK 66,000. Total tax approximately NOK 187,384.

### Test 2 -- High income, upper trinnskatt brackets
**Input:** Enkeltpersonforetak, næringsinntekt NOK 1,200,000, no skjermingsfradrag.
**Expected output:** Trinnskatt spans Trinn 1 through Trinn 4. Trinn 4 portion: NOK 1,200,000 - NOK 942,400 = NOK 257,600 x 16.7% = NOK 43,019.

### Test 3 -- Low income, below trinnskatt threshold
**Input:** Enkeltpersonforetak, næringsinntekt NOK 200,000.
**Expected output:** Below Trinn 1 threshold (NOK 217,400). No trinnskatt due. Only alminnelig inntekt (22% on NOK 200,000 - NOK 108,550) and trygdeavgift (11.0% on NOK 200,000).

### Test 4 -- Minstefradrag incorrectly claimed
**Input:** Client claims minstefradrag of NOK 104,450 on næringsinntekt of NOK 500,000.
**Expected output:** Reject minstefradrag. Only actual documented expenses are deductible against næringsinntekt. Recalculate using actual expense receipts.

### Test 5 -- Capital item expensed
**Input:** Client buys laptop for NOK 25,000, deducts full amount as operating expense.
**Expected output:** Above NOK 15,000 and useful life over 3 years. Add to saldogruppe a (office machines). Depreciation year 1 = NOK 25,000 x 30% = NOK 7,500. Remove NOK 25,000 from expenses; add NOK 7,500 depreciation.

### Test 6 -- Forskuddsskatt schedule
**Input:** Client expects total tax of NOK 200,000 for the year.
**Expected output:** 4 instalments of NOK 50,000 each: 15 March, 15 June, 15 September, 15 December.

### Test 7 -- Loss carry-forward
**Input:** Prior year loss NOK 150,000. Current year næringsinntekt NOK 400,000.
**Expected output:** Alminnelig inntekt base = NOK 400,000 - NOK 150,000 = NOK 250,000. Loss fully absorbed. Trinnskatt and trygdeavgift based on personinntekt of NOK 400,000 (loss carry-forward does not reduce personinntekt).

---

## PROHIBITIONS

- NEVER apply minstefradrag to næringsinntekt -- it is for employment income only
- NEVER apply trinnskatt to alminnelig inntekt -- trinnskatt applies to personinntekt
- NEVER use the 7.9% trygdeavgift rate for næringsinntekt -- the correct rate is 11.0%
- NEVER include MVA collected in taxable revenue for MVA-registered clients
- NEVER allow capital expenditure above NOK 15,000 (with life over 3 years) to be expensed directly
- NEVER deduct income tax or trygdeavgift as a business expense
- NEVER allow education costs for a new profession as a deduction
- NEVER ignore the personfradrag -- it reduces alminnelig inntekt by NOK 108,550
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their revisor
- NEVER advise on international income, permanent establishment, or dual residency -- escalate to T3

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a statsautorisert revisor, registrert revisor, or equivalent licensed practitioner in Norway) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
