---
name: ro-income-tax
description: >
  Use this skill whenever asked about Romanian income tax for self-employed individuals (PFA). Trigger on phrases like "how much tax do I pay", "Declarația Unică", "PFA tax", "norma de venit", "impozit pe venit", "CAS", "CASS", "self-employed tax Romania", or any question about filing or computing income tax for a self-employed or freelance client in Romania. This skill covers the flat 10% income tax, real income system (sistem real), norma de venit (deemed income), micro-enterprise regime, CAS (25% pension), CASS (10% health), filing deadlines, and penalties. ALWAYS read this skill before touching any Romanian income tax work.
version: 1.0
jurisdiction: RO
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Romania Income Tax (Declarația Unică) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Romania |
| Jurisdiction Code | RO |
| Primary Legislation | Codul Fiscal (Legea 227/2015), Titlul IV (income from independent activities) |
| Supporting Legislation | Codul de Procedură Fiscală (Legea 207/2015); OUG 168/2022 (fiscal consolidation measures); Legea 239/2025 (fiscal package 2) |
| Tax Authority | Agenția Națională de Administrare Fiscală (ANAF) |
| Filing Portal | SPV (Spațiul Privat Virtual) / declaratii.anaf.ro |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires Romanian expert contabil or consultant fiscal sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: income tax rate, CAS/CASS thresholds, norma de venit identification, filing deadlines. Tier 2: choosing between sistem real and norma de venit, CAS/CASS optimisation, micro-enterprise vs PFA decision. Tier 3: international income, tax treaties, crypto, transfer pricing. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified consultant fiscal must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Entity type** [T1] -- PFA (Persoană Fizică Autorizată), II (Întreprindere Individuală), IF (Întreprindere Familială), or SRL (micro-enterprise).
2. **Income determination method** [T1] -- sistem real (actual income/expenses) or norma de venit (deemed income).
3. **CAEN activity code(s)** [T1] -- determines norma de venit availability and amount.
4. **County (județ)** [T1] -- norma de venit varies by county.
5. **Gross revenue** [T1] -- total received in the year.
6. **Business expenses** [T1/T2] -- if using sistem real.
7. **Other income** [T1] -- employment, rental, dividends, interest, crypto.
8. **Minimum wage basis** [T1] -- RON 4,050/month for 2025.

**If entity type and income determination method are unknown, STOP. Must determine before computing.**

---

## Step 1: Income Tax Rate [T1]

**Legislation:** Codul Fiscal, Art. 68, Art. 69

### PFA / II / IF Income Tax

| Rate | Applies To |
|------|-----------|
| 10% flat | Net income from independent activities |

**Romania uses a flat 10% income tax on net income from self-employment. There are no progressive bands.**

---

## Step 2: Income Determination Methods [T1/T2]

### Option A: Sistem Real (Real Income System) [T1]

**Legislation:** Codul Fiscal, Art. 68

Net income = Gross revenue - Deductible expenses

**Deductible expenses** must be:
- Incurred for the purpose of earning income
- Documented with invoices/receipts
- Not on the non-deductible list (Art. 68 para. 5)

**Key deductible expenses:**
| Expense | Treatment |
|---------|-----------|
| Materials and supplies | Fully deductible |
| Rent (business premises) | Fully deductible |
| Utilities (business) | Fully deductible; proportional if home office |
| Professional services | Fully deductible |
| Insurance (business) | Fully deductible |
| Depreciation | Per Codul Fiscal rates |
| CAS and CASS contributions | Deductible from gross income |
| Travel (business purpose) | Deductible with documentation |
| Training/education (related to activity) | Fully deductible |

**NOT deductible:**
| Expense | Reason |
|---------|--------|
| Personal expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself | Cannot deduct tax on income |
| Entertainment (protocol) expenses | Limited to 2% of adjusted gross income |
| Sponsorship | Separate regime -- tax credit, not deduction |

### Option B: Norma de Venit (Deemed Income) [T1]

**Legislation:** Codul Fiscal, Art. 69

- ANAF publishes annual deemed income amounts by CAEN code and county (județ)
- If the taxpayer's CAEN code has an established norma, they may elect to use it
- Income tax = 10% x norma de venit amount (fixed, regardless of actual revenue or expenses)
- No bookkeeping required (only revenue records for VAT if applicable)
- Norma is set by the territorial fiscal authority and published by 15 February each year

**Norma de venit is attractive when actual profit exceeds the deemed amount.** If actual profit is lower, sistem real is preferable.

**Limitation:** Norma de venit is available only for specific CAEN codes (typically services, trades, small retail). Not all activities qualify.

---

## Step 3: Micro-Enterprise Regime (SRL only) [T1]

**Legislation:** Codul Fiscal, Art. 47-56^3

**This section applies to SRL (limited liability company), NOT PFA. Included for comparison since many freelancers consider SRL vs PFA.**

| Condition | 2025 Requirement |
|-----------|-----------------|
| Revenue threshold | Up to EUR 250,000 (reduced from EUR 500,000 as of 1 Jan 2025) |
| Employees | At least 1 employee required |
| Share capital | Not held >25% by state entities |
| Activity | Not in excluded CAEN codes (banking, insurance, gambling, consulting under specific codes) |

| Tax Rate | Condition |
|----------|-----------|
| 1% on revenue | At least 1 employee |
| 3% on revenue | Certain CAEN codes (including custom software development from 2025) or no employee |

**From 2026:** Threshold further reduced to EUR 100,000.

**Key difference from PFA:** Micro-enterprise tax is on REVENUE (turnover), not profit. No expense deductions.

---

## Step 4: Social Contributions (CAS and CASS) [T1]

**Legislation:** Codul Fiscal, Art. 148-154 (CAS), Art. 170-174 (CASS)

### CAS -- Contribuția de Asigurări Sociale (Pension) [T1]

| Item | 2025 Value |
|------|-----------|
| Rate | 25% |
| Minimum threshold | 12 x minimum wage = 12 x RON 4,050 = RON 48,600/year |
| Upper threshold | 24 x minimum wage = 24 x RON 4,050 = RON 97,200/year |

**Rules:**
- If net income < RON 48,600: CAS is optional (but no pension rights accrue if not paid)
- If net income >= RON 48,600 and < RON 97,200: CAS = 25% x RON 48,600 = RON 12,150
- If net income >= RON 97,200: CAS = 25% x RON 97,200 = RON 24,300
- CAS is paid as a fixed amount based on the threshold tier, NOT as a percentage of actual income

### CASS -- Contribuția de Asigurări Sociale de Sănătate (Health) [T1]

| Item | 2025 Value |
|------|-----------|
| Rate | 10% |
| Minimum threshold | 6 x minimum wage = 6 x RON 4,050 = RON 24,300/year |
| Upper threshold | 12 x minimum wage = 12 x RON 4,050 = RON 48,600/year |
| Maximum cap | 24 x minimum wage = 24 x RON 4,050 = RON 97,200/year (for very high earners) |

**Rules:**
- If net income < RON 24,300: CASS is STILL mandatory at minimum = 10% x RON 24,300 = RON 2,430/year (ensures basic health coverage)
- If net income >= RON 24,300 and < RON 48,600: CASS = 10% x RON 24,300 = RON 2,430
- If net income >= RON 48,600: CASS = 10% x RON 48,600 = RON 4,860
- If net income >= RON 97,200: CASS = 10% x RON 97,200 = RON 9,720

### Combined Maximum Burden (2025) [T1]

| Component | Maximum Annual Amount (RON) |
|-----------|----------------------------|
| Income tax (10%) | Varies with income |
| CAS (25%) | 24,300 |
| CASS (10%) | 9,720 |

---

## Step 5: Computation Walkthrough [T1]

### Sistem Real Computation

| Step | Description | Formula |
|------|-------------|---------|
| 1 | Gross revenue | A |
| 2 | Less: Deductible expenses (including CAS/CASS paid) | B |
| 3 | Net income (venit net) | A - B = C |
| 4 | Income tax = 10% x C | D |
| 5 | Determine CAS tier based on C | E |
| 6 | Determine CASS tier based on C | F |
| 7 | Total tax + contributions | D + E + F |

### Norma de Venit Computation

| Step | Description | Formula |
|------|-------------|---------|
| 1 | Look up norma de venit for CAEN code + county | N |
| 2 | Income tax = 10% x N | D |
| 3 | Determine CAS tier based on N | E |
| 4 | Determine CASS tier based on N | F |
| 5 | Total tax + contributions | D + E + F |

**Under norma de venit, actual revenue and expenses are irrelevant to the tax computation.**

---

## Step 6: Filing Deadlines [T1]

**Legislation:** Codul de Procedură Fiscală

| Filing / Payment | Deadline |
|-----------------|----------|
| Declarația Unică (Form 212) -- annual declaration | 25 May of following year |
| Advance payments (if applicable) | Based on prior year amounts, due with Declarația Unică |
| VAT return (if VAT registered) | Monthly by 25th, or quarterly/semester |
| Norma de venit election | At registration or by 31 January for existing PFA |

**Note (2025 change):** Starting from income year 2024 filed in 2025, the Declarația Unică includes ONLY prior year actual income -- estimated current-year income is no longer required in the same form.

---

## Step 7: Penalties [T1]

**Legislation:** Codul de Procedură Fiscală, Art. 181-186

| Offence | Penalty |
|---------|---------|
| Late filing of Declarația Unică | RON 500 -- RON 5,500 for individuals |
| Late payment interest | 0.02% per day of delay |
| Late payment penalties | 0.01% per day of delay (cumulative with interest) |
| Failure to declare income | Up to RON 27,500 + potential criminal liability |
| Tax evasion | Criminal penalties under Legea 241/2005 |

---

## Step 8: Edge Case Registry

### EC1 -- PFA net income falls between CAS thresholds [T1]
**Situation:** PFA earns RON 60,000 net income (above 12x but below 24x minimum wage).
**Resolution:** CAS = 25% x RON 48,600 = RON 12,150 (fixed at the 12x tier). CASS = 10% x RON 48,600 = RON 4,860 (at the 12x tier). Income tax = 10% x RON 60,000 = RON 6,000. Total = RON 23,010.

### EC2 -- PFA with very low income, CASS still mandatory [T1]
**Situation:** PFA earns RON 15,000 net income (below 6x minimum wage).
**Resolution:** CAS is optional (below RON 48,600 threshold). CASS is mandatory at minimum = RON 2,430. Income tax = 10% x RON 15,000 = RON 1,500. Total minimum = RON 3,930 (assuming CAS not elected).

### EC3 -- Norma de venit vs sistem real comparison [T2]
**Situation:** PFA taxi driver in Bucharest. Norma de venit = RON 30,000. Actual profit = RON 55,000.
**Resolution:** Under norma: tax = RON 3,000 + CAS on RON 30,000 basis. Under sistem real: tax = RON 5,500 + CAS on RON 55,000 basis. Norma is significantly cheaper. [T2] Flag for reviewer to verify current norma amount for CAEN code and county.

### EC4 -- SRL micro vs PFA comparison [T2]
**Situation:** IT developer earning RON 300,000/year considering PFA vs SRL micro.
**Resolution:** PFA: 10% income tax on net profit + CAS (max RON 24,300) + CASS (max RON 9,720). SRL micro (1%): RON 3,000 on revenue + employee salary taxes. But SRL threshold drops to EUR 100,000 in 2026 and software CAEN codes face 3% rate from 2025. [T2] Flag: requires full comparison of PFA vs SRL total cost including dividend extraction.

### EC5 -- Multiple CAEN codes, one has norma [T2]
**Situation:** PFA registered for CAEN 4711 (retail, norma available) and CAEN 6201 (software, no norma).
**Resolution:** Norma de venit can be applied only to the activity for which a norma exists. The other activity must use sistem real. [T2] This creates complexity -- flag for reviewer to ensure proper income separation.

### EC6 -- CAS/CASS deductibility timing [T1]
**Situation:** PFA pays CAS/CASS in March 2025 for tax year 2024 income.
**Resolution:** CAS/CASS are deductible in the year they are paid, not the year they relate to. The March 2025 payment is deductible from 2025 income (if using sistem real). In the Declarația Unică, the contributions are declared for the income year to which they apply.

### EC7 -- Exceeding micro-enterprise threshold mid-year [T1]
**Situation:** SRL micro earns EUR 260,000 in first 9 months, exceeding EUR 250,000 threshold.
**Resolution:** SRL exits micro-enterprise regime and must pay standard 16% corporate income tax (impozit pe profit) from the quarter in which the threshold was exceeded. Cannot re-enter micro regime until revenue falls below threshold for a full year.

### EC8 -- Part-year PFA registration [T1]
**Situation:** PFA registered in July 2025 (6 months of activity).
**Resolution:** Income tax applies to actual income earned. CAS threshold is prorated: 6/12 x RON 48,600 = RON 24,300. CASS threshold is prorated: 6/12 x RON 24,300 = RON 12,150. If net income exceeds prorated thresholds, contributions are due.

### EC9 -- PFA with employment income [T1]
**Situation:** Employee earns RON 80,000 from employment. PFA earns RON 40,000 net from freelance work.
**Resolution:** Employment income: CAS/CASS withheld by employer. PFA income: separate CAS/CASS calculation based on PFA net income only. Income tax on PFA = 10% x RON 40,000 = RON 4,000. CAS may not be required if PFA income < RON 48,600 (optional). CASS = minimum RON 2,430 (mandatory regardless).

### EC10 -- Minimum wage increase mid-year impact [T2]
**Situation:** Minimum wage increases from RON 4,050 to a new amount mid-year.
**Resolution:** CAS/CASS thresholds are generally set based on the minimum wage in force at the time the Declarația Unică is filed. [T2] Flag for reviewer: if minimum wage changes during the tax year, verify which rate applies for threshold calculations.

---

## Step 9: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified consultant fiscal must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to consultant fiscal. Document gap.
```

---

## Step 10: Test Suite

### Test 1 -- Standard PFA, sistem real, mid-range income
**Input:** PFA, sistem real, CAEN 6201 (software), gross revenue RON 200,000, deductible expenses RON 70,000 (including CAS/CASS from prior year).
**Expected output:** Net income = RON 130,000. Income tax = 10% x RON 130,000 = RON 13,000. CAS = 25% x RON 97,200 = RON 24,300 (above 24x threshold). CASS = 10% x RON 48,600 = RON 4,860. Total = RON 42,160.

### Test 2 -- PFA using norma de venit
**Input:** PFA taxi driver, Bucharest, norma de venit = RON 32,000.
**Expected output:** Income tax = 10% x RON 32,000 = RON 3,200. CAS = optional (RON 32,000 < RON 48,600). CASS = 10% x RON 24,300 = RON 2,430 (minimum mandatory). Total (no CAS) = RON 5,630.

### Test 3 -- Low-income PFA, mandatory CASS
**Input:** PFA, sistem real, net income RON 18,000.
**Expected output:** Income tax = RON 1,800. CAS = optional (below RON 48,600). CASS = RON 2,430 (mandatory minimum at 6x tier). Total (no CAS) = RON 4,230.

### Test 4 -- High-income PFA, all caps hit
**Input:** PFA, sistem real, net income RON 500,000.
**Expected output:** Income tax = RON 50,000. CAS = RON 24,300 (capped at 24x). CASS = RON 9,720 (capped at 24x). Total = RON 84,020. Effective rate = 16.8%.

### Test 5 -- SRL micro-enterprise vs PFA comparison
**Input:** Revenue RON 240,000, expenses RON 100,000, 1 employee.
**Expected output:** PFA sistem real: net = RON 140,000. Tax = RON 14,000. CAS = RON 24,300. CASS = RON 4,860. PFA total = RON 43,160. SRL micro (1%): tax = RON 2,400. Plus employee salary costs and 8% dividend tax on extraction. Flag: SRL micro appears cheaper but must account for dividend extraction tax and employee costs.

### Test 6 -- Part-year PFA registration
**Input:** PFA registered 1 July 2025. Net income for 6 months = RON 30,000.
**Expected output:** Income tax = RON 3,000. CAS threshold prorated: 6/12 x RON 48,600 = RON 24,300. Net income RON 30,000 > RON 24,300, so CAS = 25% x RON 24,300 = RON 6,075. CASS threshold prorated: 6/12 x RON 24,300 = RON 12,150. Net income > RON 12,150, so CASS = 10% x RON 12,150 = RON 1,215. Total = RON 10,290.

---

## PROHIBITIONS

- NEVER apply progressive tax rates -- Romania uses a flat 10% income tax for PFA
- NEVER ignore the mandatory CASS minimum -- CASS is due even if income is zero or very low
- NEVER confuse CAS thresholds with actual income percentages -- CAS is a fixed amount based on tier brackets, not a percentage of actual income
- NEVER apply norma de venit to a CAEN code or county for which no norma has been published
- NEVER use micro-enterprise rules for a PFA -- micro-enterprise is for SRL only
- NEVER advise SRL micro-enterprise for CAEN codes that face the 3% rate without disclosing the rate difference
- NEVER forget to prorate CAS/CASS thresholds for part-year registrations
- NEVER advise on crypto, international income, or transfer pricing -- escalate to T3
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their consultant fiscal for confirmation
- NEVER assume the micro-enterprise EUR 250,000 threshold is stable -- it drops to EUR 100,000 in 2026

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an expert contabil or consultant fiscal in Romania) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
