---
name: gr-efka
description: Use this skill whenever asked about Greek EFKA (e-EFKA / Ενιαίος Φορέας Κοινωνικής Ασφάλισης) social insurance contributions for self-employed individuals. Trigger on phrases like "EFKA contributions", "Greek social insurance", "ελεύθερος επαγγελματίας ασφάλιση", "EFKA categories", "self-employed Greece insurance", or any question about social insurance obligations for a self-employed client in Greece. Covers the 6-category system for main pension, healthcare, and supplementary pension. ALWAYS read this skill before touching any Greece social contributions work.
---

# Greece EFKA Contributions -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Greece |
| Jurisdiction Code | GR |
| Primary Legislation | N.4670/2020 (EFKA reform); N.4387/2016 (Ασφαλιστικό) |
| Supporting Legislation | N.4756/2020; Ministerial decisions on contribution categories |
| Tax Authority | AADE (for tax); e-EFKA (for social insurance) |
| Contributor | Open Accountants |
| Validated By | Pending -- requires validation by Greek λογιστής or ορκωτός ελεγκτής |
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

1. **Professional category** [T1] -- freelancer (ελεύθερος επαγγελματίας), sole proprietor (ατομική επιχείρηση), or liberal profession (ελεύθερο επάγγελμα)?
2. **Years of activity** [T1] -- determines which contribution category (1-6) applies by default
3. **Chosen category** [T1] -- new entrants start at category 1; established professionals may choose to move up
4. **Is the client also employed?** [T1] -- parallel insurance rules apply
5. **Registered with which professional body?** [T2] -- engineers (TEE), lawyers (bar), doctors, etc. have specific rules

**If professional category is unknown, STOP.**

---

## Step 1: The 6-Category System [T1]

**Legislation:** N.4670/2020, art. 35-39

Since June 2020, Greece replaced income-based contributions with a **6-category system** of fixed monthly amounts. Self-employed choose their category (with minimums based on years of activity).

### Monthly Contribution Amounts per Category (2025)

| Category | Main Pension (Κύρια σύνταξη) | Health (Υγειονομική) | Supplementary Pension (Επικουρική) | Total Monthly |
|----------|------------------------------|----------------------|-----------------------------------|---------------|
| 1 | EUR 210 | EUR 55 | EUR 42 | EUR 307 |
| 2 | EUR 252 | EUR 66 | EUR 51 | EUR 369 |
| 3 | EUR 315 | EUR 83 | EUR 63 | EUR 461 |
| 4 | EUR 378 | EUR 100 | EUR 76 | EUR 554 |
| 5 | EUR 473 | EUR 125 | EUR 95 | EUR 693 |
| 6 | EUR 567 | EUR 150 | EUR 113 | EUR 830 |

### Mandatory Minimum Category by Years of Activity

| Years Since Registration | Minimum Category |
|-------------------------|-----------------|
| 0-5 years | Category 1 |
| 6-10 years (from year 6) | Category 2 |
| 11-15 years (from year 11) | Category 3 |
| 16-20 years (from year 16) | Category 4 |
| 21-25 years (from year 21) | Category 5 |
| 26+ years (from year 26) | Category 6 |

**A professional can always choose a HIGHER category than their minimum, but never a lower one.**

---

## Step 2: Additional Contributions [T1]

### OAED (Unemployment) Contribution

| Who | Monthly Amount |
|-----|---------------|
| Self-employed (non-employer) | EUR 10/month |

### ETEAEP (Lump-sum benefit fund) -- for specific professions

Some professions (lawyers, engineers, doctors) have additional professional-body contributions. These are separate from EFKA.

---

## Step 3: Computation Steps [T1]

### Step 3.1 -- Determine minimum category

```
years_active = current_year - year_of_registration

IF years_active <= 5: min_category = 1
ELIF years_active <= 10: min_category = 2
ELIF years_active <= 15: min_category = 3
ELIF years_active <= 20: min_category = 4
ELIF years_active <= 25: min_category = 5
ELSE: min_category = 6
```

### Step 3.2 -- Determine chosen category

```
chosen_category = max(client_choice, min_category)
```

### Step 3.3 -- Calculate monthly and annual contributions

```
monthly_total = pension[chosen_category] + health[chosen_category] + supplementary[chosen_category] + OAED
annual_total = monthly_total × 12
```

### Step 3.4 -- New entrants discount (first 5 years)

New professionals in their first 5 years who remain in Category 1 benefit from the lowest rates. There is no additional discount beyond the category 1 rates.

---

## Step 4: Payment Schedule [T1]

**Legislation:** N.4670/2020

| Obligation | Due Date |
|------------|----------|
| Monthly EFKA contribution | Last business day of each month (for that month) |
| Payment method | Electronic via e-EFKA portal or direct debit |

- Late payment: 3% surcharge per month (capped at 100% of principal)
- Non-payment: e-EFKA can certify debt and pursue collection via KEAO (Centre for Debt Collection of Social Security)

---

## Step 5: Tax Deductibility [T1]

| Question | Answer |
|----------|--------|
| Are EFKA contributions deductible? | YES -- deductible from gross income for income tax purposes |
| Classification | Personal deduction (not business expense) |
| Which components? | All: pension, health, supplementary, OAED |

---

## Step 6: Category Selection Strategy [T2]

**Legislation:** N.4670/2020, art. 39

- Category choice is made annually (by February for the current year)
- Higher category = higher pension entitlement in retirement
- Higher category = higher current cost
- The choice is irreversible for the year once made

**[T2] -- Advising on optimal category choice requires modelling retirement benefits vs current cash flow. Flag for reviewer.**

---

## Step 7: Edge Case Registry

### EC1 -- New professional, first year [T1]
**Situation:** Client registered as freelancer in October 2025.
**Resolution:** Category 1 applies (minimum for years 0-5). Monthly: EUR 307 + EUR 10 OAED = EUR 317. Pro-rated from registration month.

### EC2 -- Professional with 12 years of activity [T1]
**Situation:** Client has been registered since 2013 (12 years).
**Resolution:** Minimum category = 3. Monthly: EUR 461 + EUR 10 = EUR 471. Client may choose categories 4, 5, or 6 for higher pension accrual.

### EC3 -- Concurrent employment and self-employment [T1]
**Situation:** Client is employed (EFKA paid by employer) and also has a freelance practice.
**Resolution:** Parallel insurance applies. Client pays EFKA contributions on BOTH activities. Employment contributions deducted from salary. Self-employment contributions paid at chosen category. No offset.

### EC4 -- Suspension of activity [T1]
**Situation:** Client temporarily suspends freelance activity.
**Resolution:** Client must formally notify e-EFKA. During suspension, no contributions are due. Health coverage continues for up to 12 months after last contribution. Beyond that, coverage lapses.

### EC5 -- Engineer/lawyer with professional body contributions [T2]
**Situation:** Client is a lawyer paying both EFKA and bar association contributions.
**Resolution:** Bar/TEE/medical association contributions are separate from EFKA. Client pays both. [T2] -- confirm professional body rates as they vary by chamber and are set independently.

### EC6 -- Farmer transitioning to freelance [T2]
**Situation:** Client was insured under OGA (agricultural) and starts freelance work.
**Resolution:** Must switch to EFKA self-employed regime. Previous OGA contributions count toward pension entitlement. [T2] -- confirm transitional rules with e-EFKA.

### EC7 -- Non-resident EU freelancer working in Greece [T2]
**Situation:** EU citizen providing services in Greece.
**Resolution:** Under EU Regulation 883/2004, social insurance is payable in one country. [T2] -- A1 certificate determination required.

### EC8 -- Very low income professional [T1]
**Situation:** Client earns only EUR 3,000/year from freelance work.
**Resolution:** Income level does NOT affect the contribution amount. Category 1 minimum applies regardless. Monthly EUR 317 is due. The flat-category system is NOT income-related.

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
Action Required: Qualified λογιστής must confirm before advising client.
```

---

## Step 9: Test Suite

### Test 1 -- New freelancer, Category 1
**Input:** First year of activity, no prior registration, age 28.
**Expected output:** Category 1. Monthly: EUR 307 + EUR 10 OAED = EUR 317. Annual: EUR 3,804.

### Test 2 -- Established professional, 8 years, stays at minimum
**Input:** Registered 8 years ago, chooses minimum category.
**Expected output:** Minimum category = 2. Monthly: EUR 369 + EUR 10 = EUR 379. Annual: EUR 4,548.

### Test 3 -- Senior professional, 22 years, minimum category
**Input:** Registered 22 years ago, stays at minimum.
**Expected output:** Minimum category = 5. Monthly: EUR 693 + EUR 10 = EUR 703. Annual: EUR 8,436.

### Test 4 -- Professional choosing higher category
**Input:** Registered 3 years ago (min cat 1), chooses Category 4.
**Expected output:** Category 4 (above minimum). Monthly: EUR 554 + EUR 10 = EUR 564. Annual: EUR 6,768.

### Test 5 -- 30-year veteran, Category 6
**Input:** Registered 30 years ago, minimum applies.
**Expected output:** Category 6 mandatory. Monthly: EUR 830 + EUR 10 = EUR 840. Annual: EUR 10,080.

### Test 6 -- Concurrent employment + self-employment
**Input:** Employed (EFKA from salary), also freelancing, 5 years self-employed.
**Expected output:** Self-employed EFKA: Category 1 minimum. EUR 317/month in addition to employment EFKA. Employment EFKA handled separately.

---

## PROHIBITIONS

- NEVER compute EFKA based on income -- the category system uses FIXED monthly amounts regardless of income
- NEVER allow a client to choose a category below their minimum based on years of activity
- NEVER ignore the OAED (EUR 10/month) -- it applies to all self-employed
- NEVER confuse EFKA contributions with professional-body contributions (bar, TEE, etc.)
- NEVER state that parallel insurance (employment + self-employment) allows an offset -- contributions are additive
- NEVER advise on category optimization without flagging for reviewer -- retirement benefit modelling required
- NEVER present contributions as income-dependent -- they are fixed per category
- NEVER forget late payment surcharges -- 3% per month is severe

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
