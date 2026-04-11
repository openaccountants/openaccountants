---
name: se-social-contributions
description: Use this skill whenever asked about Swedish self-employed social contributions (egenavgifter). Trigger on phrases like "egenavgifter", "Swedish self-employed contributions", "F-skatt", "Swedish social insurance", "Skatteverket egenavgifter", "enskild firma avgifter", or any question about social contribution obligations for a self-employed client in Sweden. Covers the ~28.97% combined rate, component breakdown, age-based reductions, and deductibility. ALWAYS read this skill before touching any Sweden social contributions work.
---

# Sweden Social Contributions (Egenavgifter) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Sweden |
| Jurisdiction Code | SE |
| Primary Legislation | Socialavgiftslagen (2000:980) -- SAL |
| Supporting Legislation | Inkomstskattelagen (1999:1229); Skatteförfarandelagen (2011:1244) |
| Tax Authority | Skatteverket (Swedish Tax Agency) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Swedish auktoriserad revisor |
| Validation Date | Pending |
| Skill Version | 1.0 |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

Before computing, you MUST know:

1. **Business form** [T1] -- enskild firma (sole proprietorship), handelsbolag partner (partnership), or kommanditbolag?
2. **F-skatt registration** [T1] -- is the client registered for F-skatt (preliminary self-employment tax)?
3. **Överskott av näringsverksamhet** [T1] -- net business income (surplus of business activity)
4. **Age** [T1] -- reduced rates apply for persons born 1938-1958 (age 67+) and those born 1957 or earlier
5. **Any concurrent employment?** [T1] -- employment and self-employment egenavgifter are separate
6. **Business year** [T1] -- first five years? (schablonavdrag available)

**If F-skatt status is unknown, STOP. F-skatt registration determines the tax framework.**

---

## Step 1: Egenavgifter Rate Components (2025) [T1]

**Legislation:** SAL 3 kap.

| Component | Rate (2025) |
|-----------|-------------|
| Ålderspensionsavgift (old-age pension) | 10.21% |
| Efterlevandepensionsavgift (survivors' pension) | 0.60% |
| Sjukförsäkringsavgift (sickness insurance) | 3.64% |
| Föräldraförsäkringsavgift (parental insurance) | 2.60% |
| Arbetsmarknadsavgift (labour market / unemployment) | 0.10% |
| Arbetsskadeavgift (work injury) | 0.20% |
| Allmän löneavgift (general payroll tax) | 11.62% |
| **Total egenavgifter** | **28.97%** |

---

## Step 2: Age-Based Reductions [T1]

**Legislation:** SAL 3 kap. 15-18 §§

| Age Category | Reduction | Effective Rate |
|-------------|-----------|----------------|
| Born 1958 or later (under ~67) | Full rate | 28.97% |
| Born 1938-1957 (age 67-86) | Only ålderspensionsavgift applies | 10.21% |
| Born 1937 or earlier (age 88+) | No egenavgifter | 0% |

**The age-based reduction removes ALL components except the old-age pension contribution for persons aged 67+.**

---

## Step 3: Contribution Base [T1]

**Legislation:** SAL 3 kap. 12-13 §§; IL 16 kap.

```
contribution_base = överskott_av_näringsverksamhet (net business income)
```

### Schablonavdrag (Standard Deduction)

Before applying egenavgifter, the net business income is reduced by a schablonavdrag of **25%** (representing the egenavgifter themselves, as they are deductible):

```
adjusted_base = net_business_income × (1 - 0.25)
# Simplified: adjusted_base = net_business_income × 0.75
```

This ensures egenavgifter are effectively calculated on income net of themselves.

Wait -- this is the simplified version. The actual mechanism:

```
egenavgifter = adjusted_income × 28.97%
adjusted_income = net_business_income - egenavgifter
# Circular, resolved by: adjusted_income = net_business_income / (1 + 0.2897) approximately
# Skatteverket provides tables, or: egenavgifter ≈ net_income × 28.97% / 128.97% ≈ net_income × 22.47%
```

**In practice, Skatteverket handles the circular calculation. For estimation:**
```
estimated_egenavgifter = net_business_income × 28.97% / (1 + 28.97%)
                       = net_business_income × 22.47%
```

---

## Step 4: Computation Steps [T1]

### Step 4.1 -- Determine net business income

```
net_business_income = gross_revenue - deductible_business_expenses
```

### Step 4.2 -- Apply age reduction if applicable

```
IF born_1938_to_1957:
    rate = 10.21%
ELIF born_before_1938:
    rate = 0%
ELSE:
    rate = 28.97%
```

### Step 4.3 -- Calculate egenavgifter

```
egenavgifter = net_business_income × rate / (1 + rate)
```

### Step 4.4 -- Annual amount

```
annual_egenavgifter = egenavgifter (as computed)
```

### Step 4.5 -- Preliminary tax (F-skatt)

F-skatt payments cover both income tax and egenavgifter combined, paid monthly:

```
monthly_F_skatt = (estimated_income_tax + estimated_egenavgifter) / 12
```

---

## Step 5: Payment Schedule [T1]

**Legislation:** Skatteförfarandelagen kap. 62

F-skatt is paid monthly:

| Payment | Due Date |
|---------|----------|
| Monthly F-skatt | 12th of each month (or 17th for February and August) |
| Annual reconciliation | Via inkomstdeklaration, filed by 2 May (sole proprietors) |

- F-skatt amount is based on preliminary income estimate
- Client can request adjustment (jämkning) if income changes significantly
- Final settlement at annual tax assessment

---

## Step 6: First 5 Years Reduction [T1]

**Legislation:** SAL 3 kap. 18 §

For the first 5 years of business activity, a **nedsättning** (reduction) of egenavgifter is available:

| Component Reduced | Reduction |
|-------------------|-----------|
| Sjukförsäkringsavgift | Reduced by up to 7.5 percentage points |

This effectively lowers the total from 28.97% to approximately **21.47%** for qualifying new businesses in the first five calendar years.

### Conditions

- Applies to the first SEK 200,000 of net business income
- The reduction is calculated automatically by Skatteverket
- Available only once per person (cannot restart by closing and reopening a business)

---

## Step 7: Tax Deductibility [T1]

| Question | Answer |
|----------|--------|
| Are egenavgifter deductible? | YES -- they reduce net business income for income tax purposes |
| When deductible? | In the income year they relate to (accrual) |
| Mechanism | Built into the schablonavdrag / circular calculation |
| Effect on income tax | Reduces the base for both kommunalskatt and statlig skatt |

---

## Step 8: Interaction with Income Tax [T1]

### Total Marginal Burden for Self-Employed (2025)

| Income Level | Kommunalskatt (~32%) | Statlig skatt | Egenavgifter (effective ~22.47%) | Combined Effective |
|--------------|---------------------|---------------|----------------------------------|--------------------|
| Below SEK 614,000 (approx.) | ~32% | 0% | ~22.47% | ~47% |
| Above SEK 614,000 | ~32% | 20% | ~22.47% | ~55% |

Note: kommunalskatt varies by municipality (average ~32%).

---

## Step 9: Edge Case Registry

### EC1 -- Sole proprietor aged 68 [T1]
**Situation:** Client born 1957, age 68, still running enskild firma.
**Resolution:** Only ålderspensionsavgift (10.21%) applies. All other components are waived. Effective egenavgifter = net_income x 10.21% / 1.1021 = ~9.27% of net income.

### EC2 -- First year of business, low income [T1]
**Situation:** Client started enskild firma in June, net income SEK 80,000 for partial year.
**Resolution:** First-5-years reduction applies. On SEK 80,000, sjukförsäkringsavgift reduced. Effective rate ~21.47%. Egenavgifter = SEK 80,000 x 21.47% / 1.2147 = ~SEK 14,137.

### EC3 -- Handelsbolag partner [T1]
**Situation:** Client is a partner in a handelsbolag (trading partnership).
**Resolution:** Each partner pays egenavgifter on their share of partnership profit, exactly as if they were a sole proprietor. Same rates, same rules.

### EC4 -- Concurrent employment and self-employment [T1]
**Situation:** Client is employed (arbetsgivaravgifter paid by employer) and runs a side enskild firma.
**Resolution:** Egenavgifter apply at full rate on net self-employment income, regardless of employment. No offset between employer social charges and egenavgifter.

### EC5 -- Negative business income (loss) [T1]
**Situation:** Client's enskild firma made a loss of SEK -30,000.
**Resolution:** Egenavgifter = SEK 0. No egenavgifter on negative income. Loss can be carried forward or offset against other income per IL rules.

### EC6 -- Passive business income [T2]
**Situation:** Client has passive (kapitalinkomst) income from a business activity.
**Resolution:** Egenavgifter only apply to active business income (näringsverksamhet). Capital income is not subject to egenavgifter. [T2] -- confirm classification with Skatteverket.

### EC7 -- Cross-border worker (EU/EEA) [T2]
**Situation:** Client is self-employed in Sweden and performs work in Denmark.
**Resolution:** Under EU Regulation 883/2004, social insurance payable in one country. [T2] -- A1 certificate required.

### EC8 -- ISK or kapitalförsäkring income [T1]
**Situation:** Client has investment income via ISK (Investeringssparkonto).
**Resolution:** ISK income is taxed via schablonintäkt and is NOT subject to egenavgifter. Only näringsverksamhet income triggers egenavgifter.

---

## Step 10: Test Suite

### Test 1 -- Standard sole proprietor
**Input:** Net business income SEK 500,000, age 40, established business.
**Expected output:** Egenavgifter = SEK 500,000 x 28.97% / 1.2897 = SEK 112,315. Monthly F-skatt covers this plus income tax.

### Test 2 -- Low income
**Input:** Net business income SEK 100,000, age 35, established business.
**Expected output:** Egenavgifter = SEK 100,000 x 28.97% / 1.2897 = SEK 22,463.

### Test 3 -- New business, first year (under SEK 200,000)
**Input:** Net business income SEK 150,000, age 30, year 1.
**Expected output:** Reduced rate ~21.47%. Egenavgifter = SEK 150,000 x 21.47% / 1.2147 = SEK 26,505. Saving vs full rate: ~SEK 7,190.

### Test 4 -- Aged 68 (born 1957)
**Input:** Net business income SEK 300,000, age 68.
**Expected output:** Rate = 10.21%. Egenavgifter = SEK 300,000 x 10.21% / 1.1021 = SEK 27,792.

### Test 5 -- High income
**Input:** Net business income SEK 2,000,000, age 45.
**Expected output:** Egenavgifter = SEK 2,000,000 x 28.97% / 1.2897 = SEK 449,256. No upper cap.

### Test 6 -- Business loss
**Input:** Net business income SEK -50,000, age 38.
**Expected output:** Egenavgifter = SEK 0.

---

## PROHIBITIONS

- NEVER forget the circular deduction (egenavgifter are deductible from income, so effective rate is ~22.47%, not 28.97%)
- NEVER apply full rate to persons born 1938-1957 -- only ålderspensionsavgift (10.21%) applies
- NEVER state there is a cap on egenavgifter -- there is no upper limit
- NEVER apply egenavgifter to capital income -- only näringsverksamhet income is subject
- NEVER ignore the first-5-years reduction -- it provides material savings to new businesses
- NEVER confuse egenavgifter (self-employed) with arbetsgivaravgifter (employer contributions, 31.42%)
- NEVER present F-skatt payments as only income tax -- they include egenavgifter
- NEVER advise on cross-border situations without flagging for reviewer (EU Regulation 883/2004)

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
