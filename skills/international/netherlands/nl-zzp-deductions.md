---
name: nl-zzp-deductions
description: >
  Use this skill whenever asked about Dutch self-employed (zzp) tax deductions. Trigger on phrases like "zelfstandigenaftrek", "startersaftrek", "MKB-winstvrijstelling", "urencriterium", "1225 hours", "KIA", "kleinschaligheidsinvesteringsaftrek", "FOR", "fiscale oudedagsreserve", "meewerkaftrek", "willekeurige afschrijving", "zzp deductions", "Dutch freelancer deductions", "Netherlands self-employed tax benefits", or any question about tax deductions available to Dutch sole proprietors (eenmanszaak) and freelancers (zzp'ers). This skill covers all major ondernemersaftrek components, the MKB-winstvrijstelling, investment deductions, the hours criterion, and their interaction with Box 1 computation. ALWAYS read this skill before touching any Dutch self-employed deduction work.
version: 1.0
jurisdiction: NL
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Netherlands ZZP Deductions -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Netherlands |
| Jurisdiction Code | NL |
| Primary Legislation | Wet inkomstenbelasting 2001 (Wet IB 2001), Articles 3.74--3.79a (ondernemersaftrek), Article 3.79a (MKB-winstvrijstelling), Articles 3.40--3.48 (investeringsaftrek) |
| Supporting Legislation | Uitvoeringsregeling inkomstenbelasting 2001; Belastingplan 2023 (FOR abolition); Belastingplan 2025 |
| Tax Authority | Belastingdienst (Dutch Tax and Customs Administration) |
| Filing Portal | Mijn Belastingdienst / Aangifte inkomstenbelasting |
| Contributor | Open Accountants |
| Validated By | Pending -- requires sign-off by a qualified Dutch belastingadviseur or registeraccountant |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: zelfstandigenaftrek amount, startersaftrek amount, MKB-winstvrijstelling rate, urencriterium threshold, KIA table, FOR abolition, computation order. Tier 2: urencriterium documentation disputes, mixed business/hobby activities, meewerkaftrek valuation, BV vs eenmanszaak transition. Tier 3: international structures, fiscal unity, complex partnership allocations. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified belastingadviseur must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any ZZP deduction, you MUST know:

1. **Business structure** [T1] -- eenmanszaak (sole proprietorship), maatschap/VOF (partnership), or BV. This skill covers eenmanszaak and partnership participants only. BV is out of scope.
2. **Does the client meet the urencriterium (1,225 hours)?** [T1/T2] -- required for zelfstandigenaftrek, startersaftrek, and willekeurige afschrijving. See Step 2.
3. **Is this a starter?** [T1] -- determines startersaftrek and willekeurige afschrijving eligibility. See Step 3.
4. **Gross profit from the enterprise (winst uit onderneming)** [T1] -- needed to compute deduction order and MKB-winstvrijstelling.
5. **Total business investments in the year** [T1] -- needed for KIA calculation.
6. **Does the fiscal partner work in the business without pay or for less than EUR 5,000?** [T2] -- determines meewerkaftrek eligibility.
7. **Does the client have an existing FOR balance from pre-2023?** [T1] -- determines whether FOR release rules apply.

**If the urencriterium status is unknown, STOP. Many deductions depend on it. Clarify hours before computing deductions.**

---

## Step 1: Zelfstandigenaftrek (Self-Employed Deduction) [T1]

**Legislation:** Wet IB 2001 Article 3.76

### 2025 Amount

| Category | Amount (EUR) |
|----------|-------------|
| Standard (below AOW age at start of year) | 2,470 |
| AOW age reached at start of year | 1,235 (50% of standard) |

### Declining Schedule

| Year | Amount (EUR) |
|------|-------------|
| 2024 | 3,750 |
| 2025 | 2,470 |
| 2026 | 1,200 |
| 2027 | 900 |

The zelfstandigenaftrek is being phased down as part of the government's policy to reduce the tax gap between employees and self-employed.

### Requirements [T1]

1. The client must qualify as an ondernemer (entrepreneur) for income tax purposes.
2. The client must meet the **urencriterium** (1,225 hours -- see Step 2).
3. The client must NOT have reached AOW age at the start of the calendar year (or they receive half).

### Limitation Rule [T1]

The zelfstandigenaftrek cannot exceed the amount of profit from the enterprise (winst) BEFORE the ondernemersaftrek is applied. If profit is lower than the zelfstandigenaftrek, only the profit amount is deductible.

**Exception:** If the client also qualifies for the startersaftrek, this limitation does NOT apply -- the full zelfstandigenaftrek is deductible even if it exceeds profit, creating a negative income from enterprise that can offset other Box 1 income.

---

## Step 2: Urencriterium (Hours Criterion) [T1/T2]

**Legislation:** Wet IB 2001 Article 3.6

### Threshold

The entrepreneur must spend at least **1,225 hours per calendar year** on activities for the enterprise.

### What Counts [T1]

| Activity | Counts? |
|----------|---------|
| Direct client work (billable hours) | Yes |
| Administration and bookkeeping | Yes |
| Acquisition of new clients (sales, marketing) | Yes |
| Professional development related to the business | Yes |
| Preparing quotes and proposals | Yes |
| Business meetings | Yes |
| Purchasing supplies for the business | Yes |
| Strategic planning for the business | Yes |

### What Does NOT Count [T1]

| Activity | Counts? |
|----------|---------|
| Travel time to and from clients | No |
| Commuting | No |
| Time spent on personal development unrelated to the business | No |
| Sick leave | No |
| Vacation | No |

### Documentation [T2]

The Belastingdienst may request proof of the hours claimed. There is no mandatory format, but the client should maintain a contemporaneous time log (urenregistratie). A retroactively constructed estimate is weak evidence.

**[T2] Flag for reviewer if hours are close to the 1,225 threshold (e.g., between 1,200 and 1,300). The Belastingdienst scrutinises borderline cases.**

### Part-Year [T1]

If the enterprise starts or ends mid-year, the 1,225 hours threshold is NOT pro-rated. The full 1,225 hours must still be met in the calendar year. This makes it very difficult for mid-year starters to qualify in their first year unless they started early in the year.

---

## Step 3: Startersaftrek (Starter's Deduction) [T1]

**Legislation:** Wet IB 2001 Article 3.76 lid 3

### 2025 Amount

**EUR 2,123** -- on top of the zelfstandigenaftrek.

### Requirements [T1]

1. The client qualifies for the zelfstandigenaftrek (meets urencriterium).
2. In the preceding 5 years, the client applied the zelfstandigenaftrek in at most 2 of those years.
3. In practice, this means the startersaftrek is available in the first 3 years of a 5-year window.

### Effect [T1]

Total deduction for a qualifying starter in 2025:

```
Zelfstandigenaftrek: EUR 2,470
Startersaftrek:      EUR 2,123
Total:               EUR 4,593
```

### Special Rule -- No Profit Limitation [T1]

Unlike the zelfstandigenaftrek alone, when the startersaftrek applies, the combined deduction (zelfstandigenaftrek + startersaftrek) is NOT limited to the profit. It can create a negative result from enterprise, which offsets other Box 1 income (employment income, pension, etc.).

---

## Step 4: MKB-Winstvrijstelling (SME Profit Exemption) [T1]

**Legislation:** Wet IB 2001 Article 3.79a

### 2025 Rate

**12.7%** of the qualifying profit.

### Calculation [T1]

The MKB-winstvrijstelling is calculated on the profit AFTER deducting the ondernemersaftrek (zelfstandigenaftrek + startersaftrek + any other ondernemersaftrek components).

```
Qualifying profit = Winst uit onderneming - Ondernemersaftrek
MKB-winstvrijstelling = Qualifying profit x 12.7%
Taxable profit = Qualifying profit - MKB-winstvrijstelling
```

### Requirements [T1]

- The client must qualify as an ondernemer for income tax purposes.
- The urencriterium is NOT required for the MKB-winstvrijstelling. All ondernemers qualify regardless of hours.
- This is the key difference from the zelfstandigenaftrek: MKB-winstvrijstelling is available to every ondernemer, even those who do not meet 1,225 hours.

### Example

| Item | Amount (EUR) |
|------|-------------|
| Winst uit onderneming (profit) | 50,000 |
| Zelfstandigenaftrek | -2,470 |
| Qualifying profit | 47,530 |
| MKB-winstvrijstelling (12.7%) | -6,036 |
| Taxable profit (added to Box 1) | 41,494 |

### Important Note

If the qualifying profit is negative (loss), the MKB-winstvrijstelling reduces the loss by 12.7%. A loss of EUR 10,000 becomes a loss of EUR 8,730 after applying the 12.7% exemption. This works against the taxpayer in loss years.

---

## Step 5: Fiscale Oudedagsreserve (FOR) -- Abolished [T1]

**Legislation:** Wet IB 2001 Article 3.67 (repealed effective 1 January 2023 by Belastingplan 2023)

### Status

The FOR has been **abolished as of 1 January 2023**. No new additions to the FOR are permitted from 2023 onwards.

### Existing Balances [T1]

| Situation | Treatment |
|-----------|-----------|
| FOR balance on 31 December 2022 | Remains on the balance sheet. Not immediately taxed. |
| Conversion to lijfrente (annuity) | The FOR balance can be converted into a qualifying annuity product (lijfrente) at any time. The premium paid is deductible within the annual jaarruimte/reserveringsruimte limits. |
| Release without lijfrente | If the FOR balance is released without purchasing a qualifying annuity (e.g., upon business cessation), the released amount is added to Box 1 taxable income and taxed at progressive rates. |
| Business cessation (staking) | At cessation, the FOR must be released. If converted to a lijfrente within 6 months after cessation, the stakingsaftrek (max EUR 3,630 in 2025) may apply. |

### What Replaced It

Entrepreneurs who want tax-advantaged retirement savings must now use the jaarruimte (annual room) to make actual lijfrente contributions. The jaarruimte is calculated based on the entrepreneur's profit and any pension accrual.

**NEVER compute a new FOR addition for 2023 or later years. The FOR is abolished.**

---

## Step 6: Kleinschaligheidsinvesteringsaftrek (KIA) [T1]

**Legislation:** Wet IB 2001 Article 3.41

### 2025 Table

| Total Investment (EUR) | Deduction |
|-----------------------|-----------|
| 0 -- 2,900 | No deduction |
| 2,901 -- 70,602 | 28% of total investment amount |
| 70,603 -- 130,744 | EUR 19,769 (fixed amount) |
| 130,745 -- 392,230 | EUR 19,769 minus 7.56% of the amount exceeding EUR 130,744 |
| > 392,230 | No deduction |

### Requirements [T1]

1. Each individual asset must cost at least **EUR 450** (excluding deductible VAT).
2. The total qualifying investment in the year must be at least **EUR 2,901**.
3. The investment must be in business assets (bedrijfsmiddelen) used in the enterprise.
4. The urencriterium is NOT required for KIA.

### Excluded Assets [T1]

- Land
- Residential buildings (woonhuizen)
- Personal cars with a catalogue value above EUR 12,000 (unless >10% of the investment relates to business modifications)
- Assets intended for lease to third parties
- Animals in agriculture (vee)
- Goodwill
- Assets acquired from a connected person (verbonden persoon) unless they are new to the connected person too

### Desinvesteringsbijtelling (Disinvestment Addition) [T1]

If a business asset for which KIA was claimed is sold within 5 years of acquisition, and the proceeds exceed the book value, a desinvesteringsbijtelling (disinvestment addition) applies. The addition is proportional to the original KIA percentage.

### Example

| Item | Amount (EUR) |
|------|-------------|
| Laptop purchased | 1,800 |
| Office desk | 900 |
| Printer | 650 |
| Total qualifying investment | 3,350 |
| KIA deduction (28% of EUR 3,350) | 938 |

---

## Step 7: Willekeurige Afschrijving voor Starters (WAS -- Random Depreciation for Starters) [T1]

**Legislation:** Wet IB 2001 Article 3.34

### What It Is

Qualifying starters may depreciate business assets at any pace they choose, instead of following the standard straight-line depreciation rules. This allows front-loading depreciation to reduce taxable profit in early years.

### Requirements [T1]

1. The client qualifies for the startersaftrek (i.e., meets the urencriterium AND is in the first 3-of-5-year window).
2. The asset must be a qualifying business asset (bedrijfsmiddel) costing at least EUR 450.
3. The total amount of assets eligible for willekeurige afschrijving in the year must not exceed EUR 392,230.
4. The asset must be new or acquired in the setup year (aanloopjaar) before the business formally started.

### How It Works [T1]

- The entrepreneur decides in which year(s) to claim the depreciation.
- Up to 100% of the cost can be depreciated in the first year.
- The residual value (restwaarde) floor still applies -- you cannot depreciate below estimated residual value.
- For buildings: willekeurige afschrijving is limited to the WOZ value.

### Example

A qualifying starter purchases a laptop for EUR 2,000 in January. Normal depreciation would be EUR 400/year over 5 years. With willekeurige afschrijving, the full EUR 2,000 (minus any residual value) can be depreciated in year 1.

---

## Step 8: Meewerkaftrek (Spouse Working Deduction) [T2]

**Legislation:** Wet IB 2001 Article 3.78

### What It Is

If the entrepreneur's fiscal partner works in the business without being paid, or for a payment of less than EUR 5,000/year, the entrepreneur can claim the meewerkaftrek.

### 2025 Table

| Hours worked by partner per year | Deduction (% of profit) |
|----------------------------------|------------------------|
| 525 -- 874 | 1.25% |
| 875 -- 1,224 | 2.00% |
| 1,225 -- 1,749 | 3.00% |
| 1,750+ | 4.00% |

### Requirements [T2]

1. The fiscal partner must work at least 525 hours per year in the enterprise.
2. The partner must receive no payment, or a payment of less than EUR 5,000.
3. The entrepreneur must qualify as ondernemer.
4. The urencriterium (1,225 hours) for the entrepreneur is NOT required for meewerkaftrek.

### Important [T2]

- [T2] Flag for reviewer: the hours worked by the partner must be documented and verifiable. The Belastingdienst may challenge the claim.
- The meewerkaftrek is being phased out -- it will be reduced and abolished from 2027.
- In most cases, it is more advantageous to pay the partner a normal salary (which is deductible from profit and taxed at the partner's own lower marginal rate). The meewerkaftrek is only beneficial in specific situations. [T2] Flag for reviewer to confirm which approach is more tax-efficient.

---

## Step 9: Interaction with Box 1 Computation [T1]

**Legislation:** Wet IB 2001 Article 3.2 et seq.

### Computation Order

The deductions must be applied in this specific order:

```
1. Winst uit onderneming (profit from enterprise)
     = Revenue - Costs - Depreciation - KIA
2. Minus: Ondernemersaftrek
     = Zelfstandigenaftrek + Startersaftrek + Meewerkaftrek + Stakingsaftrek
3. = Profit after ondernemersaftrek
4. Minus: MKB-winstvrijstelling (12.7% of line 3)
5. = Taxable profit from enterprise
6. Add: Other Box 1 income (employment, pension, periodic payments)
7. Minus: Personal deductions (hypotheekrenteaftrek, lijfrente, etc.)
8. = Belastbaar inkomen Box 1
9. Apply progressive Box 1 rates
```

### Box 1 Rates 2025

| Taxable Income (EUR) | Rate |
|----------------------|------|
| 0 -- 38,441 | 35.82% |
| 38,442 -- 76,817 | 37.48% |
| 76,818+ | 49.50% |

### Key Interaction Points [T1]

- The zelfstandigenaftrek and startersaftrek reduce profit BEFORE the MKB-winstvrijstelling is calculated. This means they have a multiplied effect: EUR 2,470 zelfstandigenaftrek reduces taxable income by EUR 2,470 + (12.7% x EUR 2,470) = EUR 2,784.
- KIA reduces profit at step 1 (as part of costs/depreciation), not at step 2. It is therefore also included in the base for MKB-winstvrijstelling.
- The heffingskortingen (tax credits, especially the arbeidskorting) are applied after computing the gross tax on Box 1 income. Self-employed income qualifies for the arbeidskorting.

---

## Step 10: Edge Case Registry

### EC1 -- Hours just below 1,225 [T2]
**Situation:** Client claims 1,210 hours. Wants to include 20 hours of travel time to meet the criterion.
**Resolution:** Travel time does NOT count toward the urencriterium. Client does not qualify for zelfstandigenaftrek or startersaftrek. Client DOES still qualify for MKB-winstvrijstelling (no hours requirement) and KIA (no hours requirement). [T2] Flag for reviewer if hours are borderline.

### EC2 -- Loss year with startersaftrek [T1]
**Situation:** Starter has a profit of EUR 1,000 but qualifies for zelfstandigenaftrek (EUR 2,470) + startersaftrek (EUR 2,123) = EUR 4,593 total deduction.
**Resolution:** Because the startersaftrek applies, the profit limitation rule does NOT apply. The full EUR 4,593 is deducted, resulting in a loss of EUR 3,593 from enterprise. This loss offsets other Box 1 income (e.g., employment income). The MKB-winstvrijstelling then applies to the negative result, reducing the loss by 12.7% (loss becomes EUR 3,137).

### EC3 -- Loss year without startersaftrek [T1]
**Situation:** Non-starter has a profit of EUR 1,500 and qualifies for zelfstandigenaftrek of EUR 2,470.
**Resolution:** The zelfstandigenaftrek is limited to the profit: EUR 1,500. The remaining EUR 970 is lost (cannot be carried forward). MKB-winstvrijstelling: 12.7% of (EUR 1,500 - EUR 1,500) = EUR 0.

### EC4 -- FOR balance from pre-2023, business continues [T1]
**Situation:** Client has a FOR balance of EUR 15,000 from 2022. Business is still active in 2025.
**Resolution:** The FOR balance remains on the balance sheet. No new additions. No forced release as long as the business continues. The client may voluntarily convert (part of) the balance to a lijfrente product at any time, deducting the premium within jaarruimte limits.

### EC5 -- KIA on personal car above EUR 12,000 [T1]
**Situation:** Client purchases a car with catalogue value EUR 25,000, used 70% for business.
**Resolution:** Cars with a catalogue value above EUR 12,000 are excluded from KIA. No KIA deduction, regardless of business use percentage. Normal depreciation (based on business use %) does apply.

### EC6 -- Desinvesteringsbijtelling triggered [T1]
**Situation:** Client purchased a machine for EUR 5,000 in 2023 and claimed KIA of EUR 1,400 (28%). Client sells the machine in 2025 for EUR 3,000.
**Resolution:** Disinvestment addition applies: EUR 3,000 x 28% = EUR 840 is added to profit in 2025. (The 28% rate used is the KIA percentage that applied at the time of investment.)

### EC7 -- Partner paid EUR 6,000 -- meewerkaftrek not available [T1]
**Situation:** Fiscal partner works 900 hours in the business and receives EUR 6,000 payment.
**Resolution:** Meewerkaftrek requires that the partner receives less than EUR 5,000. Since EUR 6,000 exceeds the threshold, meewerkaftrek does NOT apply. The EUR 6,000 is a deductible business expense for the entrepreneur and taxable income for the partner.

### EC8 -- Mid-year starter, urencriterium not met [T1]
**Situation:** Client starts their business on 1 September 2025 and works 800 hours by 31 December.
**Resolution:** The 1,225 hours threshold is NOT pro-rated. Client does not qualify for zelfstandigenaftrek or startersaftrek in 2025. Client DOES qualify for MKB-winstvrijstelling and KIA. The startersaftrek "year 1 of 3" is not used up -- it starts counting from the first year the client actually qualifies.

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified belastingadviseur must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified belastingadviseur. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Standard zzp'er, meets urencriterium, not a starter
**Input:** Eenmanszaak, winst EUR 50,000, meets 1,225 hours, not a starter, total investments EUR 2,000, no partner working in business.
**Expected output:** Zelfstandigenaftrek = EUR 2,470. No startersaftrek. No meewerkaftrek. KIA = EUR 0 (below EUR 2,901 threshold). MKB-winstvrijstelling = (EUR 50,000 - EUR 2,470) x 12.7% = EUR 6,036. Taxable profit = EUR 50,000 - EUR 2,470 - EUR 6,036 = EUR 41,494.

### Test 2 -- Starter with low profit
**Input:** Eenmanszaak, first year, winst EUR 2,000, meets 1,225 hours, total investments EUR 4,000.
**Expected output:** Zelfstandigenaftrek = EUR 2,470 (not limited to profit because startersaftrek applies). Startersaftrek = EUR 2,123. Total ondernemersaftrek = EUR 4,593. KIA = EUR 4,000 x 28% = EUR 1,120. Profit after KIA = EUR 2,000 - EUR 1,120 = EUR 880. Profit after ondernemersaftrek = EUR 880 - EUR 4,593 = -EUR 3,713. MKB-winstvrijstelling = -EUR 3,713 x 12.7% = -EUR 472 (reduces loss). Taxable result = -EUR 3,713 + EUR 472 = -EUR 3,241. This loss offsets other Box 1 income.

### Test 3 -- Does not meet urencriterium
**Input:** Eenmanszaak, winst EUR 30,000, only 900 hours worked, total investments EUR 8,000.
**Expected output:** No zelfstandigenaftrek (hours not met). No startersaftrek. KIA = EUR 8,000 x 28% = EUR 2,240. Profit after KIA = EUR 30,000 - EUR 2,240 = EUR 27,760. No ondernemersaftrek. MKB-winstvrijstelling = EUR 27,760 x 12.7% = EUR 3,526. Taxable profit = EUR 27,760 - EUR 3,526 = EUR 24,234.

### Test 4 -- Large investment, KIA fixed amount
**Input:** Eenmanszaak, total investments EUR 90,000 (all qualifying assets above EUR 450 each).
**Expected output:** Investment falls in EUR 70,603 -- 130,744 bracket. KIA = EUR 19,769 (fixed amount).

### Test 5 -- Very large investment, KIA phase-out
**Input:** Eenmanszaak, total investments EUR 200,000.
**Expected output:** Investment falls in EUR 130,745 -- 392,230 bracket. Excess = EUR 200,000 - EUR 130,744 = EUR 69,256. KIA = EUR 19,769 - (7.56% x EUR 69,256) = EUR 19,769 - EUR 5,236 = EUR 14,533.

### Test 6 -- FOR balance, ongoing business
**Input:** Client has FOR balance EUR 20,000 from 2022. Business still active in 2025.
**Expected output:** No new FOR addition (abolished from 2023). Balance stays on balance sheet. No forced release. Client may convert to lijfrente voluntarily within jaarruimte limits.

### Test 7 -- Meewerkaftrek
**Input:** Eenmanszaak, winst EUR 60,000, fiscal partner works 1,300 hours unpaid.
**Expected output:** Partner hours in 1,225--1,749 bracket. Meewerkaftrek = 3% x EUR 60,000 = EUR 1,800. Total ondernemersaftrek = EUR 2,470 (zelfstandigenaftrek) + EUR 1,800 (meewerkaftrek) = EUR 4,270. MKB-winstvrijstelling = (EUR 60,000 - EUR 4,270) x 12.7% = EUR 7,078. Taxable profit = EUR 60,000 - EUR 4,270 - EUR 7,078 = EUR 48,652.

### Test 8 -- AOW-age entrepreneur
**Input:** Entrepreneur reached AOW age on 1 January 2025. Winst EUR 25,000. Meets urencriterium.
**Expected output:** Zelfstandigenaftrek = EUR 1,235 (50% of EUR 2,470). MKB-winstvrijstelling = (EUR 25,000 - EUR 1,235) x 12.7% = EUR 3,018. Taxable profit = EUR 25,000 - EUR 1,235 - EUR 3,018 = EUR 20,747.

---

## PROHIBITIONS

- NEVER apply the zelfstandigenaftrek without confirming the urencriterium is met -- 1,225 hours is a hard threshold
- NEVER pro-rate the urencriterium for part-year businesses -- the full 1,225 hours must be met in the calendar year
- NEVER include travel time in the urencriterium count -- it is explicitly excluded
- NEVER compute a new FOR addition for 2023 or later -- the FOR has been abolished; only existing balances are managed
- NEVER apply the startersaftrek beyond the first 3 qualifying years in a 5-year window
- NEVER forget that the MKB-winstvrijstelling is calculated AFTER the ondernemersaftrek -- the order matters
- NEVER apply the profit limitation to the zelfstandigenaftrek when the startersaftrek also applies -- the limitation is lifted for starters
- NEVER claim KIA on cars with a catalogue value above EUR 12,000 -- they are excluded
- NEVER claim KIA on individual assets costing less than EUR 450 -- they do not qualify
- NEVER ignore the desinvesteringsbijtelling when a KIA-claimed asset is sold within 5 years
- NEVER present computed deductions as definitive -- always label as estimated and direct client to their belastingadviseur for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a belastingadviseur, registeraccountant, or equivalent licensed practitioner in the Netherlands) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
