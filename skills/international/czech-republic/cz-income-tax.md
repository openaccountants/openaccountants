---
name: cz-income-tax
description: >
  Use this skill whenever asked about Czech income tax for self-employed individuals (OSVČ). Trigger on phrases like "how much tax do I pay", "DPFO", "daňové přiznání", "income tax return", "výdajové paušály", "expense lump-sums", "paušální daň", "flat-rate tax", "sleva na dani", "tax credits", "self-employed tax Czech", or any question about filing or computing income tax for a self-employed or freelance client in the Czech Republic. This skill covers the 15%/23% rate structure, expense lump-sum percentages (výdajové paušály), paušální daň (lump-sum tax), tax credits (slevy na dani), interaction with health and social insurance, filing deadlines, and penalties. ALWAYS read this skill before touching any Czech income tax work.
version: 1.0
jurisdiction: CZ
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Czech Republic Income Tax (DPFO) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Czech Republic |
| Jurisdiction Code | CZ |
| Primary Legislation | Zákon č. 586/1992 Sb., o daních z příjmů (Income Tax Act) |
| Supporting Legislation | Zákon č. 589/1992 Sb. (social insurance); Zákon č. 592/1992 Sb. (health insurance); Zákon č. 540/2020 Sb. (paušální daň) |
| Tax Authority | Finanční správa (Financial Administration) |
| Filing Portal | Elektronický portál (EPO) / Daňový portál |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires Czech daňový poradce sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate table application, expense lump-sum percentages, paušální daň eligibility, basic tax credit, filing deadlines. Tier 2: mixed-use expense apportionment, spouse credit eligibility, child credit claims, choosing between real expenses and lump-sums. Tier 3: international income, tax treaty application, group structures, crypto taxation. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified tax advisor (daňový poradce) must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Type of self-employment activity** [T1] -- agriculture/craft, trade (živnost), professional services, or rental. Determines lump-sum percentage.
2. **Gross revenue (příjmy)** [T1] -- total received in the year from self-employment.
3. **Expense method chosen** [T1] -- real expenses (skutečné výdaje) or lump-sum expenses (výdajové paušály) or paušální daň.
4. **If real expenses:** total documented business expenses [T1/T2].
5. **VAT registration status** [T1] -- VAT payer or non-payer. Paušální daň requires non-VAT-payer status.
6. **Marital/family status** [T1] -- for spouse and child tax credits.
7. **Other income** [T1] -- employment income (§6), capital income (§8), rental (§9), other (§10).
8. **Social and health insurance paid** [T1] -- amounts paid during the tax year.
9. **Whether using paušální daň** [T1] -- if yes, no DPFO return is filed.

**If expense method is unknown, STOP. You must determine the method before computing.**

---

## Step 1: Determine Tax Rate [T1]

**Legislation:** Zákon č. 586/1992 Sb., § 16

### Income Tax Rates (2025)

| Taxable Income (CZK) | Rate |
|----------------------|------|
| 0 -- 1,676,052 | 15% |
| 1,676,053+ | 23% |

**Note:** The 23% threshold equals 48x the average monthly wage. For 2025, the average wage is CZK 43,967/month, giving 48 x 43,967 = CZK 2,110,416 as the gross income threshold before application of the assessment base (the threshold applies to the tax base, i.e., after deductions, at CZK 1,676,052).

**There is no tax-free band in Czech income tax. The 0% threshold is achieved through the basic tax credit (sleva na poplatníka) applied after tax computation.**

---

## Step 2: Choose Expense Method [T1/T2]

**Legislation:** Zákon č. 586/1992 Sb., § 7

### Option A: Real Expenses (Skutečné výdaje)

Deduct actual documented business expenses against gross revenue. Requires full bookkeeping or tax records (daňová evidence).

### Option B: Expense Lump-Sums (Výdajové paušály) [T1]

**Legislation:** § 7 odst. 7

| Activity Type | Lump-Sum % | Maximum Cap (CZK) |
|--------------|-----------|-------------------|
| Agriculture, forestry, craft trades (řemeslné živnosti) | 80% | 1,600,000 |
| Other trades (živnostenské podnikání) | 60% | 1,200,000 |
| Professional services, other self-employment (§ 7/1c, 7/2) | 40% | 800,000 |
| Rental of business property (§ 9) | 30% | 600,000 |

**Rules:**
- Taxpayer may NOT claim lump-sum expenses AND real expenses simultaneously for the same activity
- If using lump-sums, the taxpayer cannot claim the spouse tax credit (sleva na manžela/manželku) -- verify: this restriction was modified; as of 2025 it applies if lump-sum expenses exceed CZK 50,000
- Lump-sum users are NOT required to keep expense receipts but MUST keep income records

### Option C: Paušální daň (Lump-Sum Tax) [T1]

**Legislation:** Zákon č. 540/2020 Sb., effective from 2021

Single monthly payment covering income tax + social insurance + health insurance.

**Eligibility (all must be met):**
- Annual revenue up to CZK 2,000,000
- NOT a VAT payer (or voluntarily registered)
- NOT an employer
- NOT a partner in a partnership (v.o.s. or k.s.)
- OSVČ as main activity
- No other income exceeding CZK 50,000 (employment excluded if tax withheld)

**2025 Monthly Payments:**

| Band | Revenue Limit (CZK) | Monthly Payment (CZK) | Components |
|------|---------------------|----------------------|------------|
| 1 | up to 1,000,000 | 7,498 | Income tax + social + health |
| 2 | up to 1,500,000 | 16,745 | Income tax + social + health |
| 3 | up to 2,000,000 | 27,139 | Income tax + social + health |

**Registration deadline:** 10 January of the relevant tax year (strict).

**If paušální daň applies, NO tax return (DPFO) is filed. NO annual insurance reconciliation is filed. The skill stops here.**

---

## Step 3: Compute Tax Base [T1]

**Legislation:** § 5, § 7

### Computation Steps

| Step | Description | Formula |
|------|-------------|---------|
| 1 | Gross revenue from self-employment (§ 7) | A |
| 2 | Less: Expenses (real or lump-sum) | B |
| 3 | Partial tax base from self-employment (dílčí základ daně § 7) | A - B = C |
| 4 | Add: Other partial tax bases (§ 6, § 8, § 9, § 10) | D |
| 5 | Total tax base (základ daně) | C + D = E |
| 6 | Less: Non-taxable deductions (§ 15) | F |
| 7 | Adjusted tax base (rounded down to nearest CZK 100) | E - F = G |
| 8 | Tax at 15% / 23% | H |
| 9 | Less: Tax credits (slevy na dani, § 35ba) | I |
| 10 | Tax after credits | H - I = J |
| 11 | Less: Child tax credit (daňové zvýhodnění, § 35c) | K |
| 12 | Final tax liability (may be negative = tax bonus) | J - K = L |

---

## Step 4: Non-Taxable Deductions (Nezdanitelné části, § 15) [T1]

| Deduction | Maximum (CZK) | Conditions |
|-----------|--------------|------------|
| Gifts to charity | 15% of tax base | Minimum CZK 1,000 or 2% of tax base |
| Mortgage interest (úroky z úvěru) | 150,000 | Own housing needs only |
| Private pension contributions (penzijní připojištění) | 24,000 | Contributions above CZK 1,000/month |
| Life insurance (životní pojištění) | 24,000 | Contract conditions must be met |
| Trade union dues | 1.5% of § 6 income | Max CZK 3,000 |

---

## Step 5: Tax Credits (Slevy na dani, § 35ba) [T1]

**Legislation:** § 35ba

| Credit | Annual Amount (CZK) | Conditions |
|--------|---------------------|------------|
| Basic taxpayer credit (na poplatníka) | 30,840 | Every taxpayer, no conditions |
| Spouse credit (na manžela/manželku) | 24,840 | Spouse income < CZK 68,000/year; from 2025 only if caring for child under 3 |
| Spouse with ZTP/P disability | 49,680 | As above + disability certificate |
| Disability credit (invalidita I/II) | 2,520 | |
| Disability credit (invalidita III) | 5,040 | |
| ZTP/P holder | 16,140 | |
| Student credit | 4,020 | Student under 26 (doctoral under 28) |

### Child Tax Credit (Daňové zvýhodnění, § 35c) [T1]

| Child | Annual Amount (CZK) | With ZTP/P (CZK) |
|-------|---------------------|-------------------|
| 1st child | 15,204 | 30,408 |
| 2nd child | 22,320 | 44,640 |
| 3rd and each subsequent | 27,840 | 55,680 |

**The child credit can generate a tax bonus (negative tax = refund) up to CZK 60,300/year. The basic taxpayer credit cannot generate a bonus.**

---

## Step 6: Social and Health Insurance Interaction [T1]

**Legislation:** Zákon č. 589/1992 Sb. (social); Zákon č. 592/1992 Sb. (health)

### Assessment Base

For both social and health insurance, the assessment base is **50% of the partial tax base from self-employment (§ 7)**.

### Rates

| Insurance | Rate | Minimum Monthly (2025, main activity) |
|-----------|------|--------------------------------------|
| Social insurance (ČSSZ) | 29.2% of assessment base | CZK 4,759 |
| Health insurance (VZP etc.) | 13.5% of assessment base | CZK 3,143 |

### Key Rules [T1]

- Social and health insurance are NOT deductible from the income tax base
- Advances are paid monthly; annual reconciliation (Přehled) filed by the DPFO deadline
- If using paušální daň, insurance is included in the monthly payment -- no separate filing
- Self-employed with concurrent employment: social insurance may be secondary (vedlejší činnost) with lower minimums

---

## Step 7: Filing Deadlines [T1]

**Legislation:** § 136 Daňový řád (Tax Procedure Code)

| Filing / Payment | Deadline |
|-----------------|----------|
| DPFO (paper filing) | 1 April of following year |
| DPFO (electronic filing via EPO) | 1 May of following year |
| DPFO (filed by daňový poradce) | 1 July of following year |
| Tax payment | Same as filing deadline |
| Přehled ČSSZ (social insurance reconciliation) | 1 month after DPFO deadline |
| Přehled VZP (health insurance reconciliation) | 1 month after DPFO deadline |
| Paušální daň registration | 10 January |

---

## Step 8: Penalties [T1]

**Legislation:** § 250, § 251, § 252 Daňový řád

| Offence | Penalty |
|---------|---------|
| Late filing (over 5 working days) | 0.05% of tax per day, max 5% of tax (min CZK 500, max CZK 300,000) |
| Late payment interest | Repo rate + 8 percentage points, per annum |
| Incorrect return (additional assessment) | 20% of additionally assessed tax |
| Fraud / tax evasion | Criminal penalties under Trestní zákoník |

---

## Step 9: Edge Case Registry

### EC1 -- Lump-sum expenses exceed cap [T1]
**Situation:** Freelance IT consultant (40% lump-sum) earns CZK 2,500,000.
**Resolution:** 40% of CZK 2,500,000 = CZK 1,000,000, but cap is CZK 800,000. Deductible expenses = CZK 800,000 only. Tax base = CZK 1,700,000. Consider whether real expenses would be more favourable.

### EC2 -- Paušální daň taxpayer exceeds revenue limit mid-year [T1]
**Situation:** OSVČ on paušální daň Band 1 earns CZK 1,200,000 by October.
**Resolution:** If annual revenue exceeds CZK 1,000,000 but stays under CZK 1,500,000, taxpayer moves to Band 2 at year-end reconciliation. If revenue exceeds CZK 2,000,000, paušální daň is lost entirely -- taxpayer must file a standard DPFO for the entire year.

### EC3 -- VAT registration forces exit from paušální daň [T1]
**Situation:** OSVČ on paušální daň is required to register for VAT (exceeds CZK 2,000,000 threshold or voluntarily registers).
**Resolution:** Paušální daň is immediately terminated. Taxpayer must file standard DPFO for the entire year. Cannot re-enter paušální daň until VAT registration is cancelled.

### EC4 -- Combining employment and self-employment income [T1]
**Situation:** Employee earns CZK 600,000 from employment and CZK 300,000 from freelance work.
**Resolution:** Employment income (§ 6) is the super-gross base (employer calculates). Freelance income (§ 7) uses chosen expense method. Both partial tax bases combine for total tax base. Basic credit applies once. Social insurance from self-employment may be secondary activity (vedlejší) if employment is the main activity.

### EC5 -- Student using student credit + child credit for parent [T1/T2]
**Situation:** 24-year-old student freelancer earns CZK 150,000. Parent wants to claim the child credit.
**Resolution:** Student can claim the student credit (CZK 4,020) on their own return. Parent can claim the child credit (CZK 15,204) if the student lives in the household. These are separate credits -- both can be claimed. [T2] Verify the student qualifies as "preparing for future profession" (studying).

### EC6 -- Switching from lump-sum to real expenses [T2]
**Situation:** Freelancer used lump-sum expenses in 2024 but wants real expenses in 2025.
**Resolution:** Taxpayer must adjust the tax base for the transition year. Receivables and payables at year-end of the lump-sum year must be included in the transition adjustment. This is a common source of errors. [T2] Flag for reviewer to compute the transition adjustment correctly.

### EC7 -- OSVČ with losses carried forward [T1]
**Situation:** Freelancer had a loss of CZK 200,000 in 2023. Profit of CZK 500,000 in 2025.
**Resolution:** Tax losses can be carried forward for 5 years (§ 34). The CZK 200,000 loss from 2023 can offset 2025 income. Tax base = CZK 300,000. Loss carry-forward is only available with real expenses, NOT lump-sum expenses.

### EC8 -- Health insurance minimum not met [T1]
**Situation:** OSVČ earns CZK 80,000. 50% assessment base = CZK 40,000. 13.5% = CZK 5,400 annual health insurance.
**Resolution:** Monthly minimum is CZK 3,143 (annual CZK 37,716). Actual calculation (CZK 5,400) is below the minimum. Taxpayer must pay the minimum of CZK 37,716 for the year.

### EC9 -- Spouse credit restriction with lump-sum expenses [T2]
**Situation:** Freelancer uses 60% lump-sum and wants to claim spouse credit.
**Resolution:** Since 2025, the spouse credit is available only when caring for a child under 3, regardless of expense method. Additionally, if lump-sum expenses exceed CZK 50,000, further restrictions may apply. [T2] Flag for reviewer to verify current eligibility rules.

### EC10 -- Crypto income classification [T3]
**Situation:** OSVČ has significant cryptocurrency trading income alongside freelance work.
**Resolution:** [T3] Escalate. Crypto income classification (§ 7 vs § 10) depends on frequency, volume, and whether it constitutes a business activity. Complex area with evolving guidance. Refer to daňový poradce.

---

## Step 10: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified daňový poradce must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to daňový poradce. Document gap.
```

---

## Step 11: Test Suite

### Test 1 -- Standard freelancer, lump-sum expenses, mid-range income
**Input:** IT consultant, single, gross revenue CZK 1,200,000, using 40% lump-sum (professional services), no other income.
**Expected output:** Lump-sum expenses = CZK 480,000. Tax base = CZK 720,000. Tax at 15% = CZK 108,000. Less basic credit CZK 30,840. Final tax = CZK 77,160.

### Test 2 -- Craftsman with 80% lump-sum near cap
**Input:** Carpenter (řemeslná živnost), gross revenue CZK 2,200,000, using 80% lump-sum, single, no children.
**Expected output:** 80% of CZK 2,200,000 = CZK 1,760,000, but cap = CZK 1,600,000. Tax base = CZK 600,000. Tax at 15% = CZK 90,000. Less basic credit CZK 30,840. Final tax = CZK 59,160.

### Test 3 -- High earner hitting 23% band
**Input:** Freelance architect, single, gross revenue CZK 4,000,000, real expenses CZK 1,500,000.
**Expected output:** Tax base = CZK 2,500,000. Tax = 15% on CZK 1,676,052 = CZK 251,408 + 23% on CZK 823,948 = CZK 189,508. Total = CZK 440,916. Less basic credit CZK 30,840. Final tax = CZK 410,076.

### Test 4 -- Paušální daň eligibility check
**Input:** Freelancer, revenue CZK 900,000, not VAT registered, no employees, no partnership.
**Expected output:** Eligible for paušální daň Band 1. Monthly payment CZK 7,498. Annual total CZK 89,976. No DPFO filing required. No insurance reconciliation required.

### Test 5 -- Parent with children, tax bonus
**Input:** Single parent freelancer, revenue CZK 400,000, 40% lump-sum, 3 children (none disabled).
**Expected output:** Tax base = CZK 240,000. Tax at 15% = CZK 36,000. Less basic credit CZK 30,840 = CZK 5,160. Less child credits: CZK 15,204 + CZK 22,320 + CZK 27,840 = CZK 65,364. Tax after credits = CZK 5,160 - CZK 65,364 = -CZK 60,204. Tax bonus (refund) = CZK 60,204 (capped at CZK 60,300).

### Test 6 -- Employment + side freelance income
**Input:** Employee earning CZK 500,000 (tax withheld by employer), side freelance income CZK 180,000, 60% trade lump-sum, single.
**Expected output:** Freelance tax base = CZK 72,000. Combined with employment § 6 base. Lump-sum expense = CZK 108,000. Total tax base = CZK 500,000 + CZK 72,000 = CZK 572,000. Tax = CZK 85,800. Less basic credit CZK 30,840. Tax = CZK 54,960. Less tax withheld from employment. Social insurance on freelance = secondary activity.

### Test 7 -- Lump-sum cap hit, compare with real expenses
**Input:** IT freelancer, revenue CZK 2,500,000, real expenses CZK 1,100,000, 40% lump-sum available.
**Expected output:** Lump-sum: 40% of CZK 2,500,000 = CZK 1,000,000, capped at CZK 800,000. Tax base = CZK 1,700,000. Real expenses: CZK 1,100,000 deducted. Tax base = CZK 1,400,000. Real expenses save CZK 300,000 in tax base. Recommend real expenses.

---

## PROHIBITIONS

- NEVER compute tax without first determining the expense method (real, lump-sum, or paušální daň)
- NEVER allow lump-sum expenses above the statutory cap for the activity type
- NEVER file a DPFO for a paušální daň taxpayer -- if paušální daň is valid, no return is due
- NEVER apply the basic taxpayer credit more than once per taxpayer
- NEVER allow both parents to claim the child credit for the same child
- NEVER treat social and health insurance as deductible from the income tax base -- they are NOT
- NEVER use lump-sum expenses if the taxpayer wants to carry forward a loss -- losses require real expenses
- NEVER advise on crypto, international structures, or tax treaty matters -- escalate to T3
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their daňový poradce for confirmation
- NEVER skip the transition adjustment when switching between lump-sum and real expenses

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a daňový poradce or equivalent licensed practitioner in the Czech Republic) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
