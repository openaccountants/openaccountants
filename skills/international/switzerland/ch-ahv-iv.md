---
name: ch-ahv-iv
description: Use this skill whenever asked about Swiss AHV/IV (Alters- und Hinterlassenenversicherung / Invalidenversicherung) social contributions for self-employed individuals. Trigger on phrases like "AHV contributions", "Swiss social security self-employed", "AHV/IV/EO", "Beitragsverfügung", "sliding scale AHV", "Swiss self-employed insurance", or any question about social insurance obligations for a self-employed client in Switzerland. Covers the 5.371-10% sliding scale, EO, minimum contribution, and BVG voluntary pillar 2. ALWAYS read this skill before touching any Switzerland social contributions work.
---

# Switzerland AHV/IV Contributions -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Switzerland |
| Jurisdiction Code | CH |
| Primary Legislation | AHVG (Bundesgesetz über die Alters- und Hinterlassenenversicherung) |
| Supporting Legislation | IVG; EOG; AHVV (Verordnung); BVG (Berufliche Vorsorge) |
| Tax Authority | Ausgleichskasse (Compensation Office -- cantonal or professional) |
| Rate Publisher | BSV (Bundesamt für Sozialversicherungen) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Swiss Treuhänder or Wirtschaftsprüfer |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: sliding scale, minimum/maximum, EO, payment. Tier 2: voluntary BVG, international coordination. Tier 3: AG/AI cantonal supplements, military service credits. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified professional must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any AHV/IV figure, you MUST know:

1. **Self-employment status** [T1] -- is the client recognized as selbständig erwerbend by the Ausgleichskasse?
2. **Net earned income from self-employment** [T1] -- Reineinkommen from all self-employed activities
3. **Which Ausgleichskasse?** [T1] -- cantonal or professional (e.g., Medisuisse for doctors)
4. **Age** [T1] -- contributions start at 18 (20 for employed), end at reference age (65M/65F from 2028)
5. **Any concurrent employment?** [T1] -- employer already pays AHV on wages
6. **Interest in voluntary BVG (Pillar 2)?** [T2] -- optional for self-employed

**If self-employment status is not confirmed by the Ausgleichskasse, STOP. The Ausgleichskasse determines status, not the client.**

---

## Step 1: AHV/IV/EO Rate Structure (2025) [T1]

**Legislation:** AHVG art. 8; AHVV art. 21

### Components

| Component | Full Rate (on income >= CHF 58,800) | Legislation |
|-----------|--------------------------------------|-------------|
| AHV (old-age and survivors) | 8.10% | AHVG art. 8 |
| IV (disability) | 1.40% | IVG art. 3 |
| EO (income replacement / maternity) | 0.50% | EOG art. 27 |
| **Total** | **10.00%** | |

### Sliding Scale (Sinkende Beitragsskala)

For income between CHF 9,800 and CHF 58,800, a reduced sliding scale applies:

| Annual Net Income | AHV/IV/EO Rate |
|-------------------|----------------|
| Up to CHF 9,800 | Minimum contribution (CHF 514/year) |
| CHF 9,800 | 5.371% |
| CHF 17,400 | 5.509% |
| CHF 21,400 | 5.666% |
| CHF 25,200 | 5.859% |
| CHF 28,900 | 6.101% |
| CHF 32,600 | 6.405% |
| CHF 36,100 | 6.783% |
| CHF 39,600 | 7.226% |
| CHF 42,900 | 7.726% |
| CHF 46,200 | 8.271% |
| CHF 49,200 | 8.849% |
| CHF 52,200 | 9.444% |
| CHF 55,400 | 9.953% |
| CHF 58,800 and above | 10.000% |

**The Ausgleichskasse publishes the exact table with interpolation. The rates above are reference points.**

### Minimum and Maximum Contributions

| Parameter | Amount (2025) |
|-----------|---------------|
| Minimum annual contribution (AHV/IV/EO) | CHF 514 |
| Minimum income for minimum contribution | CHF 9,800 |
| Income where full 10% rate kicks in | CHF 58,800 |
| No upper cap on income | No maximum |

**There is no upper cap. AHV/IV/EO applies at 10% on all income above CHF 58,800 without limit.**

---

## Step 2: Contribution Base [T1]

**Legislation:** AHVG art. 9; AHVV art. 17-22

```
contribution_base = net_self_employment_income
                  = gross_revenue - business_expenses - depreciation
                  + capital_gains_on_business_assets (if applicable)
```

### Key Rules for the Base

1. The base is the **Reineinkommen** (net income) from self-employment as determined by the tax assessment
2. Personal AHV/IV/EO contributions paid are added back (50% gross-up rule): the actual base = Reineinkommen + 50% of contributions due (to approximate the employer half)
3. Interest on business capital is deducted from the base
4. The Ausgleichskasse uses the definitive tax assessment from the cantonal tax authority

---

## Step 3: Computation Steps [T1]

### Step 3.1 -- Determine net income and apply gross-up

```
raw_income = net_self_employment_income_per_tax_assessment
adjusted_income = raw_income + (AHV_contributions_paid × 50%)  # approximation
# In practice, the Ausgleichskasse computes this via published tables
```

### Step 3.2 -- Apply sliding scale or full rate

```
IF adjusted_income <= 9,800:
    annual_contribution = 514  # minimum
ELIF adjusted_income < 58,800:
    annual_contribution = adjusted_income × sliding_scale_rate  # from table
ELSE:
    annual_contribution = adjusted_income × 10.00%
```

### Step 3.3 -- Add FAK (Family Allowance Fund) if applicable

Some cantons require self-employed to pay FAK contributions (Familienausgleichskasse). Rates vary by canton (typically 1-3%).

```
IF canton_requires_FAK:
    FAK = adjusted_income × cantonal_FAK_rate
    total = annual_contribution + FAK
```

### Step 3.4 -- Administration costs

The Ausgleichskasse charges administration costs (Verwaltungskosten), typically 1-5% of contributions.

---

## Step 4: Payment Schedule [T1]

**Legislation:** AHVV art. 34-36

- Self-employed pay **quarterly advance payments** (Akontobeiträge)
- Advances are based on prior-year income or estimated current-year income
- Final settlement occurs after the definitive tax assessment is available (often 1-2 years later)

| Payment | Due |
|---------|-----|
| Advance Q1 | Per Ausgleichskasse schedule (varies) |
| Advance Q2 | Per Ausgleichskasse schedule |
| Advance Q3 | Per Ausgleichskasse schedule |
| Advance Q4 | Per Ausgleichskasse schedule |
| Final settlement | Upon definitive tax assessment |

- Late payment: Verzugszinsen at 5% per annum (AHVV art. 41bis)
- Advances can be adjusted up or down upon request with justification

---

## Step 5: Tax Deductibility [T1]

**Legislation:** DBG art. 33(1)(d)

| Question | Answer |
|----------|--------|
| Are AHV/IV/EO contributions deductible? | YES -- from income for federal and cantonal tax |
| Classification | Personal deduction (Versicherungsabzug), not business expense |
| When deductible? | In the year they relate to (accrual basis for contributions) |

---

## Step 6: Voluntary BVG (Pillar 2) [T2]

**Legislation:** BVG art. 4, 44, 46

Self-employed persons are NOT obligatorily insured under BVG (Pillar 2) but may join voluntarily:

| Option | Detail |
|--------|--------|
| Join a BVG Stiftung | Self-employed can join the Stiftung of their professional association or the Auffangeinrichtung |
| Contribution basis | Insured salary = net self-employment income (subject to BVG minimum/maximum) |
| BVG minimum insured salary (2025) | CHF 22,050 |
| BVG maximum insured salary (2025) | CHF 88,200 |
| Contribution rates | Age-dependent: 7% (25-34), 10% (35-44), 15% (45-54), 18% (55-65) |
| Tax treatment | Contributions fully deductible from income |

**[T2] -- BVG plan design varies. Confirm specific fund rules with the Stiftung.**

### Pillar 3a (Säule 3a)

| Parameter | Amount (2025) |
|-----------|---------------|
| With BVG (Pillar 2) | Max CHF 7,056 |
| Without BVG (Pillar 2) | Max 20% of net income, up to CHF 35,280 |

---

## Step 7: Edge Case Registry

### EC1 -- Income below minimum threshold [T1]
**Situation:** Client's net self-employment income is CHF 5,000.
**Resolution:** Minimum contribution of CHF 514/year applies. Client cannot pay less than the minimum regardless of income level.

### EC2 -- Concurrent employment and self-employment [T1]
**Situation:** Client is employed (AHV paid by employer on salary) and also self-employed.
**Resolution:** AHV is due separately on self-employment income. No offset between employment and self-employment contributions. However, if total employment income already exceeds the full-rate threshold, self-employment contributions are still calculated independently on self-employment income alone.

### EC3 -- Non-cash income / benefits in kind [T1]
**Situation:** Client receives part of business income in kind.
**Resolution:** All income including benefits in kind must be included in the AHV contribution base at fair market value.

### EC4 -- Business cessation mid-year [T1]
**Situation:** Client stops self-employment in June.
**Resolution:** Contributions are pro-rated for the period of activity. Minimum contribution is also pro-rated (1/12 per month of activity). Final settlement based on actual income for the partial year.

### EC5 -- Person approaching reference age [T1]
**Situation:** Client turns 65 in the contribution year.
**Resolution:** Contributions are due until the end of the month in which the client reaches reference age. After reference age, a Freibetrag of CHF 16,800/year applies -- no contributions on income below this. Above the Freibetrag, standard rates apply but only AHV/EO (no IV).

### EC6 -- Persons without gainful employment [T2]
**Situation:** Client has no income but is resident in Switzerland.
**Resolution:** Non-employed persons pay AHV/IV/EO based on wealth and pension income. Minimum CHF 514/year. [T2] -- calculation based on Rentnertabelle, confirm with Ausgleichskasse.

### EC7 -- International coordination (EU/EFTA) [T2]
**Situation:** Client works in Switzerland and an EU/EFTA country.
**Resolution:** Under the Agreement on Free Movement of Persons, social insurance is generally payable in one country only. Determination depends on where substantial activity occurs. [T2] -- A1 certificate required.

### EC8 -- Capital gains on business assets [T1]
**Situation:** Client sells a business asset at a gain.
**Resolution:** Capital gains on business assets (Kapitalgewinne auf Geschäftsvermögen) are subject to AHV/IV/EO contributions as part of the self-employment income base.

---

## Step 8: Reviewer Escalation Protocol

When Claude identifies a [T2] situation:

```
REVIEWER FLAG
Tier: T2
Client: [name]
Situation: [description]
Issue: [what is ambiguous]
Options: [possible treatments]
Recommended: [most likely correct treatment and why]
Action Required: Qualified Treuhänder must confirm before advising client.
```

---

## Step 9: Test Suite

### Test 1 -- Income at full rate
**Input:** Net self-employment income CHF 100,000, age 40.
**Expected output:** AHV/IV/EO = CHF 100,000 x 10.00% = CHF 10,000. Plus administration costs.

### Test 2 -- Income in sliding scale range
**Input:** Net self-employment income CHF 40,000, age 35.
**Expected output:** Approximately CHF 40,000 x ~7.2% = ~CHF 2,880 (exact rate from Ausgleichskasse table). Plus administration costs.

### Test 3 -- Minimum contribution
**Input:** Net self-employment income CHF 5,000, age 30.
**Expected output:** Minimum contribution CHF 514/year.

### Test 4 -- Very high income (no cap)
**Input:** Net self-employment income CHF 500,000, age 50.
**Expected output:** AHV/IV/EO = CHF 500,000 x 10.00% = CHF 50,000. No upper cap.

### Test 5 -- Post-reference-age with Freibetrag
**Input:** Net self-employment income CHF 25,000, age 67.
**Expected output:** Freibetrag = CHF 16,800. Contributory income = CHF 25,000 - CHF 16,800 = CHF 8,200. Below minimum threshold of CHF 9,800, so minimum of CHF 514 would normally apply. But since CHF 8,200 < CHF 9,800 and the Freibetrag has been applied, contribution = CHF 514 minimum (AHV/EO only, no IV).

### Test 6 -- Concurrent employment + self-employment
**Input:** Employment salary CHF 80,000 (AHV paid by employer), self-employment income CHF 30,000, age 38.
**Expected output:** Self-employment AHV/IV/EO on CHF 30,000 at sliding scale rate (~6.4%) = ~CHF 1,920. Employment AHV handled separately by employer.

### Test 7 -- Pillar 3a without BVG
**Input:** Self-employed, no BVG, net income CHF 120,000, age 42.
**Expected output:** Maximum Pillar 3a = 20% x CHF 120,000 = CHF 24,000, capped at CHF 35,280. Deductible: CHF 24,000.

---

## PROHIBITIONS

- NEVER determine self-employment status yourself -- only the Ausgleichskasse can confirm this
- NEVER apply the full 10% rate to incomes below CHF 58,800 -- the sliding scale must be used
- NEVER state there is a maximum cap on AHV/IV contributions -- there is no upper cap in Switzerland
- NEVER ignore the CHF 514 minimum contribution -- it always applies regardless of income level
- NEVER confuse the self-employed contribution (full rate) with the employee half-rate (5.00%)
- NEVER forget the Freibetrag (CHF 16,800) for persons past reference age
- NEVER advise on voluntary BVG without flagging for reviewer -- plan specifics vary
- NEVER present AHV figures without noting that final settlement depends on the definitive tax assessment
- NEVER ignore FAK cantonal obligations -- rates and rules vary by canton

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
