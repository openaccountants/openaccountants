---
name: pl-income-tax
description: Use this skill whenever asked about Polish income tax (PIT) for self-employed individuals (działalność gospodarcza / JDG). Trigger on phrases like "Polish tax", "PIT-36", "PIT-36L", "skala podatkowa", "ryczałt", "IP Box", "kwota wolna", "ZUS", "składki", "działalność gospodarcza", "self-employed tax Poland", or any question about filing or computing income tax for a Polish self-employed client. Covers skala podatkowa (12%/32%), flat tax (19%), ryczałt, IP Box (5%), kwota wolna, ZUS contributions, deductible expenses, filing deadlines, and penalties. ALWAYS read this skill before touching any Polish income tax work.
---

# Poland Income Tax (PIT) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Poland |
| Jurisdiction Code | PL |
| Primary Legislation | Ustawa o podatku dochodowym od osob fizycznych (PIT Act, 26 July 1991); Ustawa o zryczaltowanym podatku dochodowym (Ryczałt Act, 20 November 1998) |
| Supporting Legislation | Ustawa o systemie ubezpieczeń społecznych (Social Insurance Act); Ustawa o świadczeniach opieki zdrowotnej (Health Insurance Act); Ordynacja podatkowa (Tax Ordinance) |
| Tax Authority | Krajowa Administracja Skarbowa (KAS -- National Revenue Administration) |
| Filing Portal | e-Urzad Skarbowy (e-US) / podatki.gov.pl |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires sign-off by a Polish doradca podatkowy or biegły rewident |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: skala podatkowa rates, flat tax rate, ryczałt rates, kwota wolna, filing deadlines. Tier 2: ryczałt rate classification by activity (PKD code), IP Box eligibility, ZUS optimization. Tier 3: international income, CFC rules, transfer pricing, complex structures. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified doradca podatkowy must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Business form** [T1] -- jednoosobowa działalność gospodarcza (JDG / sole proprietorship), freelancer, or other
2. **Chosen taxation form** [T1] -- skala podatkowa, podatek liniowy (flat tax), ryczałt, or karta podatkowa
3. **PKD code (activity classification)** [T2] -- determines available taxation forms and ryczałt rate
4. **Gross business revenue** [T1] -- total invoiced/received in the year
5. **Business expenses** [T1/T2] -- nature and amount (not relevant for ryczałt, which taxes revenue)
6. **ZUS contributions paid** [T1] -- social (społeczne) and health (zdrowotne) amounts
7. **ZUS basis** [T1] -- preferential (ulga na start / preferencyjne), standard, or large ZUS
8. **Other income** [T1] -- employment, rental, capital gains
9. **IP income** [T2] -- if claiming IP Box, nature and documentation of qualifying IP

**If taxation form is unknown, STOP. The entire computation depends on which form the client has elected.**

---

## Step 1: Taxation Form Options [T1/T2]

**Legislation:** PIT Act art. 9a, 27, 30c; Ryczałt Act

Polish self-employed individuals must choose one taxation form at the start of the year (or when registering). The choice is binding for the entire tax year.

### Option A: Skala Podatkowa (Progressive Scale) [T1]

| Bracket | Rate (2025) | Threshold |
|---------|-------------|-----------|
| First bracket | 12% | Income up to PLN 120,000 |
| Second bracket | 32% | Income above PLN 120,000 |

| Item | Amount (2025) |
|------|---------------|
| Kwota wolna od podatku (tax-free amount) | PLN 30,000 |
| Kwota zmniejszająca podatek (tax-reducing amount) | PLN 3,600 (= PLN 30,000 x 12%) |
| Monthly tax-reducing amount | PLN 300 |

**Form filed:** PIT-36

**Advantages:** Kwota wolna applies; joint filing with spouse possible; most deductions and credits available (ulgi podatkowe).

### Option B: Podatek Liniowy (Flat Tax) [T1]

| Item | Rate / Amount (2025) |
|------|----------------------|
| Flat rate | 19% on net income |
| Kwota wolna | Does NOT apply |
| Joint filing with spouse | NOT available |

**Form filed:** PIT-36L

**Advantages:** Lower effective rate for high earners (above approximately PLN 120,000 net income). Simpler computation.

**Disadvantages:** No kwota wolna (PLN 30,000 tax-free threshold does not apply). Cannot file jointly. Most personal tax credits (ulgi) are not available.

### Option C: Ryczałt od przychodów ewidencjonowanych (Lump-Sum Tax on Recorded Revenue) [T1/T2]

| Rate | Applies To (examples) |
|------|----------------------|
| 17% | Liberal professions (lawyers, doctors -- individual practice) |
| 15% | Certain consulting, advertising, IT services |
| 14% | Healthcare services |
| 12.5% | Revenue above PLN 100,000 from rental |
| 12% | IT services (many software development activities under certain PKD codes) |
| 10% | Property purchase/sale services |
| 8.5% | Service activities (general); rental income up to PLN 100,000 |
| 5.5% | Construction, manufacturing |
| 3% | Trade (retail/wholesale), gastronomy |
| 2% | Sale of agricultural products |

**Form filed:** PIT-28

**Advantages:** Lowest effective rate for many service activities. Simple -- tax on revenue, no need to track expenses.

**Disadvantages:** Cannot deduct business expenses (tax is on gross revenue, not net income). Kwota wolna does NOT apply. Limited deductions.

**Revenue limit for ryczałt eligibility (2025):** PLN 8,569,200 (EUR 2 million equivalent) in the prior year.

**[T2] The correct ryczałt rate depends on the PKD code and specific nature of services. Flag for reviewer to confirm rate classification.**

### Option D: IP Box [T2]

| Item | Detail |
|------|--------|
| Rate | 5% on qualifying IP income |
| Eligible IP | Patents, copyrights to computer programs, industrial designs, utility models |
| Requirement | R&D activity must be conducted; qualifying costs tracked; nexus ratio computed |
| Documentation | Separate IP income ledger (ewidencja) required |
| Can combine with | Skala podatkowa or podatek liniowy (NOT ryczałt) |

**Form filed:** PIT-36 or PIT-36L with PIT/IP attachment

**[T2] IP Box requires extensive documentation and nexus ratio computation. Always flag for reviewer. Incorrect application carries significant penalty risk.**

---

## Step 2: ZUS Contributions [T1/T2]

**Legislation:** Social Insurance Act; Health Insurance Act

### Social Contributions (Składki społeczne) [T1]

| Contribution | Rate (2025) |
|-------------|-------------|
| Emerytalna (pension) | 19.52% |
| Rentowa (disability) | 8.00% |
| Chorobowa (sickness -- voluntary) | 2.45% |
| Wypadkowa (accident) | 1.67% (standard for JDG) |
| Fundusz Pracy (labour fund) | 2.45% |
| Total (with sickness) | ~34.09% of declared base |

### ZUS Bases (2025)

| Category | Monthly Base | Duration |
|----------|-------------|----------|
| Ulga na start | No social ZUS; health only | First 6 months of activity |
| Preferencyjne ZUS | 30% of minimum wage base | Months 7--30 of activity |
| Standard (duży) ZUS | 60% of forecast average wage | After preferential period |

### Health Contribution (Składka zdrowotna) [T1/T2]

The health contribution depends on the chosen taxation form:

| Taxation Form | Health Contribution Base (2025) |
|--------------|-------------------------------|
| Skala podatkowa | 9% of actual monthly income (minimum PLN 314.96/month) |
| Podatek liniowy | 4.9% of actual monthly income (minimum PLN 314.96/month) |
| Ryczałt | Fixed amounts based on revenue brackets |

### Health Contribution Deductibility [T1]

| Taxation Form | Health Contribution Deductibility |
|--------------|----------------------------------|
| Skala podatkowa | NOT deductible from income or tax |
| Podatek liniowy | Deductible from income up to annual limit |
| Ryczałt | 50% deductible from revenue |

### Social Contribution Deductibility [T1]

Social contributions (społeczne) are fully deductible from income (skala podatkowa / liniowy) or from revenue (ryczałt). This includes pension, disability, sickness (if opted in), accident, and labour fund contributions.

---

## Step 3: Computation -- Skala Podatkowa [T1]

**Step-by-step:**

1. Gross revenue
2. Less: Tax-deductible costs (koszty uzyskania przychodow)
3. = Dochod (income)
4. Less: Social ZUS contributions (if not already deducted in costs)
5. Less: Other deductions (ulgi -- e.g., internet deduction, rehabilitation, donations)
6. = Podstawa opodatkowania (tax base), rounded to full PLN
7. Apply rate: 12% on first PLN 120,000; 32% on excess
8. Less: Kwota zmniejszająca podatek (PLN 3,600)
9. = Tax before credits
10. Less: Health contribution (NOT deductible under skala)
11. Less: Tax credits (ulga prorodzinna -- child credit, etc.)
12. = Tax due (PIT-36)

---

## Step 4: Computation -- Podatek Liniowy [T1]

**Step-by-step:**

1. Gross revenue
2. Less: Tax-deductible costs
3. = Dochod (income)
4. Less: Social ZUS contributions
5. Less: Health contribution (deductible up to annual limit)
6. = Podstawa opodatkowania
7. Apply rate: 19% flat
8. = Tax due (PIT-36L)

**No kwota wolna. No kwota zmniejszająca. No joint filing. No child credit.**

---

## Step 5: Computation -- Ryczałt [T1]

**Step-by-step:**

1. Gross revenue (przychód)
2. Less: Social ZUS contributions
3. Less: 50% of health contribution
4. = Podstawa opodatkowania
5. Apply applicable ryczałt rate (by activity type)
6. = Tax due (PIT-28)

**No business expense deductions. Tax is on revenue, not profit.**

---

## Step 6: Allowable Deductions (Skala / Liniowy Only) [T1/T2]

**Legislation:** PIT Act art. 22, 23

### The Deduction Rule [T1]

An expense is deductible if it was incurred to earn, maintain, or secure taxable revenue (art. 22 ust. 1) and is not on the exclusion list (art. 23).

### Deductible Expenses (Koszty uzyskania przychodow)

| Expense | Tier | Treatment |
|---------|------|-----------|
| Office rent | T1 | Fully deductible |
| Professional insurance | T1 | Fully deductible |
| Accountancy / biuro rachunkowe fees | T1 | Fully deductible |
| Office supplies | T1 | Fully deductible |
| Software subscriptions (business) | T1 | Fully deductible |
| Marketing / advertising | T1 | Fully deductible |
| Business bank charges | T1 | Fully deductible |
| Professional development | T1 | Fully deductible if related to business |
| Business travel (delegacja) | T1 | Per diem rates (dieta) + actual transport/accommodation |
| Phone / internet | T2 | Business use portion; mixed-use apportionment |
| Motor vehicle (in środki trwałe) | T2 | If in business asset register: 100% costs; if private car used for business: 20% of expenses deductible |
| Home office | T2 | Proportional to business-use area |
| Social ZUS contributions | T1 | Fully deductible (from income or as cost) |
| Representation (limited) | T1 | Deductible if documented and business-related |

### NOT Deductible (art. 23) [T1]

| Expense | Reason |
|---------|--------|
| Personal living expenses | Not business-related |
| Fines and penalties (kary, grzywny) | Public policy (art. 23 ust. 1 pkt 15) |
| Income tax (PIT) | Tax on income (art. 23 ust. 1 pkt 12) |
| Capital expenditure | Depreciated via środki trwałe |
| Health contribution (under skala podatkowa) | Explicitly non-deductible |
| 75% of private car expenses used for business | Only 20% deductible if car not in asset register |

### Private Car Used for Business [T2]

- Car NOT in business asset register (środki trwałe): only 20% of total car expenses deductible
- Car IN business asset register: 100% if exclusively business use; 75% if mixed use
- [T2] Flag for reviewer to confirm car use documentation

---

## Step 7: Depreciation (Amortyzacja) [T1]

**Legislation:** PIT Act art. 22a--22o

### Depreciation Rates

| Asset Type | Rate | Method |
|-----------|------|--------|
| Computer hardware | 30% | Straight-line |
| Computer software | 50% | Straight-line |
| Passenger cars | 20% | Straight-line |
| Office furniture | 20% | Straight-line |
| Machinery / equipment | 10--20% | Straight-line |
| Buildings (commercial) | 2.5% | Straight-line |
| Goodwill | Over contract period or 60 months | Straight-line |

### Rules [T1]

- Assets with initial value above PLN 10,000: must be entered in środki trwałe register and depreciated
- Assets with initial value up to PLN 10,000: may be expensed immediately (jednorazowa amortyzacja)
- Passenger car depreciation cap: PLN 150,000 (for combustion cars); PLN 225,000 (for electric/hybrid cars)
- Depreciation starts the month after the asset is placed in service

---

## Step 8: Filing Deadlines [T1]

**Legislation:** PIT Act; Tax Ordinance

| Filing / Payment | Deadline |
|-----------------|----------|
| PIT-36 (skala podatkowa) | 30 April of the following year |
| PIT-36L (flat tax) | 30 April of the following year |
| PIT-28 (ryczałt) | 30 April of the following year |
| Monthly advance payments (zaliczki) | 20th of the following month |
| Quarterly advance payments (if elected) | 20th of the month following the quarter |
| Annual ZUS reconciation (ZUS DRA) | Monthly, by 20th |

---

## Step 9: Penalties [T1]

**Legislation:** Kodeks karny skarbowy (Fiscal Penal Code)

| Offence | Penalty |
|---------|---------|
| Late filing (wykroczenie skarbowe) | Grzywna (fine): PLN 430 to PLN 86,000 (2025, indexed) |
| Late payment of tax | Interest (odsetki) at 14.5% per annum (2025, verify) |
| Incorrect return (negligence) | Fine + corrected assessment + interest |
| Incorrect return (intentional) | Criminal prosecution; fines up to 720 daily rates |
| Failure to keep records | Fine + estimated assessment |
| Czynny żal (voluntary disclosure) | Immunity from penalty if filed before audit commences |

**Czynny żal (active regret):** A taxpayer who voluntarily corrects their return and pays the outstanding tax before the tax authority initiates proceedings is exempt from fiscal penalties. This is a critical safety valve.

---

## Step 10: Interaction with VAT (Podatek VAT) [T1]

**Legislation:** Ustawa o podatku od towarów i usług (VAT Act)

| Scenario | Income Tax Treatment |
|----------|---------------------|
| VAT collected on sales (czynny podatnik VAT) | NOT income -- liability to US. Exclude from revenue. |
| Input VAT recovered | NOT an expense -- reclaimable. Exclude from costs. |
| Non-deductible VAT (e.g., 50% on passenger cars) | IS an expense -- adds to cost |
| VAT-exempt (zwolnienie podmiotowe, under PLN 200,000) | No VAT charged or reclaimed; gross = net |

---

## Step 11: Record Keeping [T1]

**Legislation:** PIT Act; Tax Ordinance; Accounting Act

| Requirement | Detail |
|-------------|--------|
| KPiR (Podatkowa Księga Przychodów i Rozchodów) | Required for skala podatkowa and podatek liniowy |
| Ewidencja przychodów | Required for ryczałt |
| Minimum retention | 5 years from end of calendar year in which tax return was filed |
| What to keep | All invoices (faktury), receipts, bank statements, contracts, asset register (ewidencja środków trwałych) |
| Format | Paper or digital (JPK reporting requirements for digital books) |

---

## Step 12: Edge Case Registry

### EC1 -- Kwota wolna claimed under podatek liniowy [T1]
**Situation:** Client on flat tax (PIT-36L) claims PLN 30,000 tax-free amount.
**Resolution:** INCORRECT. Kwota wolna does NOT apply to podatek liniowy. The full income is taxed at 19%.

### EC2 -- Ryczałt rate misclassified [T2]
**Situation:** Software developer claims 8.5% ryczałt rate on all IT revenue.
**Resolution:** The correct rate depends on the specific PKD code and nature of services. Many IT services qualify for 12%, not 8.5%. Some qualify for 15%. [T2] Flag for reviewer to confirm PKD code and applicable rate based on classification ruling (interpretacja podatkowa).

### EC3 -- Business expenses deducted under ryczałt [T1]
**Situation:** Client on ryczałt deducts PLN 50,000 in business expenses from revenue.
**Resolution:** INCORRECT. Ryczałt is levied on gross revenue. No business expense deductions are allowed (only ZUS social contributions and 50% of health contribution).

### EC4 -- Health contribution deducted under skala podatkowa [T1]
**Situation:** Client on skala podatkowa deducts health contribution from income.
**Resolution:** INCORRECT. Under skala podatkowa, health contribution is NOT deductible from income or tax. It is deductible only under podatek liniowy (from income) and ryczałt (50% from revenue).

### EC5 -- IP Box without R&D documentation [T2]
**Situation:** Client claims 5% IP Box rate but has no R&D cost documentation or separate IP income ledger.
**Resolution:** IP Box REQUIRES: (1) separate IP income ledger, (2) R&D activity documentation, (3) nexus ratio calculation. Without these, IP Box cannot be applied. Revert to the client's base taxation form. [T2] Escalate -- risk of penalties.

### EC6 -- Private car 100% expenses deducted [T1]
**Situation:** Client uses private car (not in środki trwałe) for business and deducts 100% of car expenses.
**Resolution:** INCORRECT. If car is NOT in the business asset register, only 20% of total car expenses are deductible. Reduce deduction to 20%.

### EC7 -- Joint filing claimed with podatek liniowy [T1]
**Situation:** Married client on PIT-36L wants to file jointly with spouse.
**Resolution:** NOT available. Joint filing (wspólne rozliczenie) is only available for skala podatkowa (PIT-36). Client must file PIT-36L individually.

### EC8 -- Czynny żal after audit commenced [T1]
**Situation:** Client wants to file czynny żal after receiving notification of tax audit.
**Resolution:** TOO LATE. Czynny żal is only effective if filed before the tax authority initiates proceedings (kontrola or postępowanie). After notification, czynny żal does not provide immunity.

### EC9 -- Ulga dla klasy średniej claimed [T1]
**Situation:** Client claims ulga dla klasy średniej (middle class relief) on 2025 return.
**Resolution:** This relief was abolished effective 1 July 2022 (replaced by the 12% rate reduction from 17% under Polski Ład 2.0). It does NOT exist for tax year 2025. Remove from computation.

### EC10 -- Car depreciation above cap [T1]
**Situation:** Client depreciates a car with initial value PLN 200,000 at full 20%.
**Resolution:** Depreciation is capped at PLN 150,000 initial value for combustion cars (PLN 225,000 for electric). Only PLN 150,000 x 20% = PLN 30,000/year is deductible. Excess depreciation (on PLN 50,000 x 20% = PLN 10,000) is NOT deductible.

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
Action Required: Qualified doradca podatkowy must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified doradca podatkowy or biegły rewident. Document gap.
```

---

## Step 14: Test Suite

### Test 1 -- Skala podatkowa, mid-range income
**Input:** JDG on skala podatkowa, revenue PLN 300,000, tax-deductible costs PLN 100,000, social ZUS PLN 18,000, no health deduction.
**Expected output:** Dochód = PLN 200,000. Less social ZUS = PLN 182,000. Tax: PLN 120,000 x 12% = PLN 14,400; PLN 62,000 x 32% = PLN 19,840. Total = PLN 34,240. Less kwota zmniejszająca = PLN 3,600. Tax = PLN 30,640.

### Test 2 -- Podatek liniowy, high income
**Input:** JDG on flat tax, dochód PLN 500,000, social ZUS PLN 18,000, health contribution deductible amount PLN 12,000.
**Expected output:** Base = PLN 500,000 - PLN 18,000 - PLN 12,000 = PLN 470,000. Tax = PLN 470,000 x 19% = PLN 89,300. No kwota wolna.

### Test 3 -- Ryczałt, IT services at 12%
**Input:** JDG on ryczałt (12% rate), revenue PLN 400,000, social ZUS PLN 18,000, health contribution 50% deductible = PLN 6,000.
**Expected output:** Base = PLN 400,000 - PLN 18,000 - PLN 6,000 = PLN 376,000. Tax = PLN 376,000 x 12% = PLN 45,120.

### Test 4 -- Kwota wolna incorrectly applied to flat tax
**Input:** Client on PIT-36L claims PLN 30,000 tax-free.
**Expected output:** Reject. Kwota wolna does not apply to podatek liniowy. Full income taxed at 19%.

### Test 5 -- Car depreciation exceeds cap
**Input:** Car PLN 200,000 entered in środki trwałe. Client claims PLN 40,000 depreciation (20%).
**Expected output:** Cap applies: deductible depreciation = PLN 150,000 x 20% = PLN 30,000. Excess PLN 10,000 is non-deductible. Adjust.

### Test 6 -- Ulga dla klasy średniej claimed
**Input:** Client includes ulga dla klasy średniej on 2025 PIT-36.
**Expected output:** Reject. Relief abolished since July 2022. Remove from return.

### Test 7 -- Czynny żal timing
**Input:** Client received audit notification on 15 March. Files czynny żal on 20 March.
**Expected output:** Invalid. Czynny żal must be filed before audit notification. No immunity from penalties.

---

## PROHIBITIONS

- NEVER apply kwota wolna (PLN 30,000) to podatek liniowy or ryczałt -- it applies only to skala podatkowa
- NEVER deduct business expenses under ryczałt -- ryczałt is levied on revenue
- NEVER deduct health contribution under skala podatkowa -- it is non-deductible under this form
- NEVER allow joint filing for podatek liniowy clients
- NEVER apply ulga dla klasy średniej -- it was abolished in 2022
- NEVER apply IP Box without confirming R&D documentation and separate IP income ledger
- NEVER allow 100% car expense deduction for private cars not in the business asset register -- cap at 20%
- NEVER exceed car depreciation caps (PLN 150,000 combustion / PLN 225,000 electric)
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their doradca podatkowy
- NEVER advise on international income, CFC rules, or transfer pricing -- escalate to T3

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a doradca podatkowy, biegły rewident, or equivalent licensed practitioner in Poland) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
