---
name: se-social-contributions
description: Use this skill whenever asked about Swedish self-employed social contributions (egenavgifter). Trigger on phrases like "egenavgifter", "Swedish self-employed contributions", "F-skatt", "Swedish social insurance", "Skatteverket egenavgifter", "enskild firma avgifter", or any question about social contribution obligations for a self-employed client in Sweden. Covers the ~28.97% combined rate, component breakdown, age-based reductions, and deductibility. ALWAYS read this skill before touching any Sweden social contributions work.
version: 2.0
---

# Sweden Social Contributions (Egenavgifter) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Sweden (Kingdom of Sweden) |
| Authority | Skatteverket (Swedish Tax Agency) |
| Primary legislation | Socialavgiftslagen (2000:980) -- SAL |
| Supporting legislation | Inkomstskattelagen (1999:1229); Skatteförfarandelagen (2011:1244) |
| Total egenavgifter rate | 28.97% |
| Effective rate after deduction | ~22.47% |
| Age 67+ rate (born 1938-1957) | 10.21% (ålderspensionsavgift only) |
| Age 88+ (born before 1938) | 0% |
| First 5 years reduction | ~21.47% (on first SEK 200,000) |
| Upper cap | None |
| F-skatt payment | Monthly (12th of each month) |
| Annual declaration | By 2 May |
| Currency | SEK only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Swedish auktoriserad revisor |
| Validation date | Pending |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Business form** -- enskild firma, handelsbolag partner, or kommanditbolag?
2. **F-skatt registration** -- confirmed?
3. **Överskott av näringsverksamhet** -- net business income
4. **Age/birth year** -- reduced rates for 67+
5. **Any concurrent employment?** -- separate egenavgifter
6. **Business year** -- first 5 years? (reduction available)

**If F-skatt status is unknown, STOP.**

### Refusal catalogue

**R-SE-SOC-1 -- Cross-border worker.** Trigger: client works in Sweden and Denmark/other EU state. Message: "EU Regulation 883/2004 applies. A1 certificate required. Escalate."

### Prohibitions

- NEVER forget the circular deduction (effective rate ~22.47%, not 28.97%)
- NEVER apply full rate to persons born 1938-1957 -- only 10.21%
- NEVER state there is a cap -- there is no upper limit
- NEVER apply egenavgifter to capital income -- only näringsverksamhet
- NEVER ignore the first-5-years reduction
- NEVER confuse egenavgifter (28.97%) with arbetsgivaravgifter (31.42%)
- NEVER present F-skatt as only income tax -- it includes egenavgifter

---

## Section 3 -- Rate components (2025)

**Legislation:** SAL 3 kap.

| Component | Rate |
|---|---|
| Ålderspensionsavgift (old-age pension) | 10.21% |
| Efterlevandepensionsavgift (survivors) | 0.60% |
| Sjukförsäkringsavgift (sickness) | 3.64% |
| Föräldraförsäkringsavgift (parental) | 2.60% |
| Arbetsmarknadsavgift (labour market) | 0.10% |
| Arbetsskadeavgift (work injury) | 0.20% |
| Allmän löneavgift (general payroll tax) | 11.62% |
| **Total** | **28.97%** |

---

## Section 4 -- Age reductions and first-5-years

### Age-based reductions

| Age category | Effective rate |
|---|---|
| Born 1958 or later (under ~67) | 28.97% |
| Born 1938-1957 (67-86) | 10.21% (only ålderspensionsavgift) |
| Born before 1938 (88+) | 0% |

### First 5 years reduction

**Legislation:** SAL 3 kap. 18 Section

Sjukförsäkringsavgift reduced by up to 7.5 percentage points on first SEK 200,000 of net business income. Effective rate ~21.47% for qualifying new businesses. Available only once per person.

---

## Section 5 -- Computation steps

### Step 5.1 -- Contribution base and circular deduction

```
contribution_base = net_business_income (överskott av näringsverksamhet)
```

Egenavgifter are deductible from income, creating a circular calculation:

```
egenavgifter = net_business_income x rate / (1 + rate)
```

For full rate: effective = 28.97% / 128.97% = ~22.47%.

### Step 5.2 -- Apply age reduction

```
IF born_1938_to_1957: rate = 10.21%
ELIF born_before_1938: rate = 0%
ELSE: rate = 28.97%
```

### Step 5.3 -- Calculate

```
egenavgifter = net_business_income x rate / (1 + rate)
```

### Step 5.4 -- F-skatt monthly payments

```
monthly_F_skatt = (estimated_income_tax + estimated_egenavgifter) / 12
```

---

## Section 6 -- Payment schedule and tax deductibility

### Payment schedule

| Payment | Due date |
|---|---|
| Monthly F-skatt | 12th of each month (17th for Feb/Aug) |
| Annual reconciliation | Inkomstdeklaration by 2 May |

Client can request jämkning if income changes significantly.

### Tax deductibility

| Question | Answer |
|---|---|
| Are egenavgifter deductible? | YES -- reduce net business income for income tax |
| When deductible? | In the income year they relate to |
| Effect | Reduces base for both kommunalskatt and statlig skatt |

---

## Section 7 -- Marginal burden context

| Income level | Kommunalskatt (~32%) | Statlig skatt | Egenavgifter (~22.47%) | Combined |
|---|---|---|---|---|
| Below ~SEK 614,000 | ~32% | 0% | ~22.47% | ~47% |
| Above ~SEK 614,000 | ~32% | 20% | ~22.47% | ~55% |

Kommunalskatt varies by municipality (average ~32%).

---

## Section 8 -- Edge case registry

### EC1 -- Aged 68 (born 1957)
**Situation:** Still running enskild firma.
**Resolution:** Only ålderspensionsavgift (10.21%). Effective ~9.27%.

### EC2 -- First year, low income
**Situation:** Started enskild firma in June, net SEK 80,000.
**Resolution:** First-5-years reduction. Effective ~21.47%.

### EC3 -- Handelsbolag partner
**Situation:** Partner in handelsbolag.
**Resolution:** Same rules as sole proprietor on their share of profit.

### EC4 -- Concurrent employment + self-employment
**Situation:** Employed and runs side enskild firma.
**Resolution:** Full egenavgifter on self-employment income. No offset with employer charges.

### EC5 -- Business loss
**Situation:** Net income SEK -30,000.
**Resolution:** Egenavgifter = SEK 0. Loss carried forward per IL rules.

### EC6 -- Passive business income
**Situation:** Kapitalinkomst from business activity.
**Resolution:** Egenavgifter only on active näringsverksamhet income. Flag for reviewer.

---

## Section 9 -- Reviewer escalation protocol

When a situation requires reviewer judgement:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified auktoriserad revisor must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified revisor. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- Standard sole proprietor
**Input:** Net income SEK 500,000, age 40, established.
**Expected output:** Egenavgifter = SEK 500,000 x 28.97% / 1.2897 = SEK 112,315.

### Test 2 -- Low income
**Input:** Net income SEK 100,000, age 35.
**Expected output:** SEK 22,463.

### Test 3 -- New business, first year
**Input:** Net income SEK 150,000, age 30, year 1.
**Expected output:** Reduced ~21.47%. SEK 26,505.

### Test 4 -- Aged 68
**Input:** Net income SEK 300,000, age 68.
**Expected output:** Rate 10.21%. SEK 27,792.

### Test 5 -- High income
**Input:** Net income SEK 2,000,000, age 45.
**Expected output:** SEK 449,256. No cap.

### Test 6 -- Business loss
**Input:** Net income SEK -50,000, age 38.
**Expected output:** SEK 0.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
