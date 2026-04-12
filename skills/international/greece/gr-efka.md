---
name: gr-efka
description: Use this skill whenever asked about Greek EFKA (e-EFKA / Ενιαίος Φορέας Κοινωνικής Ασφάλισης) social insurance contributions for self-employed individuals. Trigger on phrases like "EFKA contributions", "Greek social insurance", "ελεύθερος επαγγελματίας ασφάλιση", "EFKA categories", "self-employed Greece insurance", or any question about social insurance obligations for a self-employed client in Greece. Covers the 6-category system for main pension, healthcare, and supplementary pension. ALWAYS read this skill before touching any Greece social contributions work.
version: 2.0
---

# Greece EFKA Contributions -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Greece (Hellenic Republic) |
| Authority | e-EFKA (Ενιαίος Φορέας Κοινωνικής Ασφάλισης) |
| Primary legislation | N.4670/2020 (EFKA reform); N.4387/2016 |
| Supporting legislation | N.4756/2020; ministerial decisions on categories |
| System | 6-category fixed monthly amounts (NOT income-based) |
| Category 1 monthly total | EUR 307 |
| Category 6 monthly total | EUR 830 |
| OAED (unemployment) | EUR 10/month additional |
| Payment frequency | Monthly |
| Payment deadline | Last business day of each month |
| Currency | EUR only |
| Contributor | Open Accountants |
| Validated by | Pending -- requires validation by Greek λογιστής |
| Validation date | Pending |

**Monthly amounts per category (2025):**

| Cat | Main pension | Health | Supplementary | Total |
|---|---|---|---|---|
| 1 | EUR 210 | EUR 55 | EUR 42 | EUR 307 |
| 2 | EUR 252 | EUR 66 | EUR 51 | EUR 369 |
| 3 | EUR 315 | EUR 83 | EUR 63 | EUR 461 |
| 4 | EUR 378 | EUR 100 | EUR 76 | EUR 554 |
| 5 | EUR 473 | EUR 125 | EUR 95 | EUR 693 |
| 6 | EUR 567 | EUR 150 | EUR 113 | EUR 830 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before computing, you MUST obtain:

1. **Professional category** -- freelancer, sole proprietor, or liberal profession?
2. **Years of activity** -- determines minimum category
3. **Chosen category** -- new entrants start at 1; may choose higher
4. **Is the client also employed?** -- parallel insurance rules
5. **Registered with which professional body?** -- engineers, lawyers, doctors may have additional rules

**If professional category is unknown, STOP.**

### Refusal catalogue

**R-GR-EFKA-1 -- Farmer transition.** Trigger: client transitioning from OGA (agricultural) to freelance. Message: "OGA-to-EFKA transitional rules require specialist review. Escalate."

**R-GR-EFKA-2 -- Professional body contributions.** Trigger: question about bar/TEE/medical chamber rates. Message: "Professional body contributions are separate from EFKA and set independently. Confirm with the relevant chamber."

### Prohibitions

- NEVER compute EFKA based on income -- the category system uses FIXED monthly amounts
- NEVER allow a client to choose a category below their minimum based on years
- NEVER ignore OAED (EUR 10/month) -- applies to all self-employed
- NEVER confuse EFKA contributions with professional-body contributions
- NEVER state parallel insurance allows an offset -- contributions are additive
- NEVER advise on category optimization without flagging for reviewer
- NEVER present contributions as income-dependent -- they are fixed per category
- NEVER forget late payment surcharges -- 3% per month

---

## Section 3 -- The 6-category system

**Legislation:** N.4670/2020, art. 35-39

### Mandatory minimum category by years of activity

| Years since registration | Minimum category |
|---|---|
| 0-5 years | Category 1 |
| 6-10 years | Category 2 |
| 11-15 years | Category 3 |
| 16-20 years | Category 4 |
| 21-25 years | Category 5 |
| 26+ years | Category 6 |

A professional can always choose a HIGHER category than their minimum, but never a lower one. Choice is made annually by February and is irreversible for the year.

---

## Section 4 -- Additional contributions and category selection

### OAED (unemployment)

All self-employed: EUR 10/month in addition to category amounts.

### ETEAEP (lump-sum benefit fund)

Some professions (lawyers, engineers, doctors) have additional professional-body contributions separate from EFKA.

### Category selection strategy

Higher category = higher pension entitlement in retirement but higher current cost. Advising on optimal choice requires retirement benefit modelling. Flag for reviewer.

---

## Section 5 -- Computation steps

### Step 5.1 -- Determine minimum category

```
years_active = current_year - year_of_registration

IF years_active <= 5: min_category = 1
ELIF years_active <= 10: min_category = 2
ELIF years_active <= 15: min_category = 3
ELIF years_active <= 20: min_category = 4
ELIF years_active <= 25: min_category = 5
ELSE: min_category = 6
```

### Step 5.2 -- Determine chosen category

```
chosen_category = max(client_choice, min_category)
```

### Step 5.3 -- Calculate contributions

```
monthly_total = pension[chosen] + health[chosen] + supplementary[chosen] + OAED (10)
annual_total = monthly_total x 12
```

---

## Section 6 -- Payment schedule and tax deductibility

### Payment schedule

| Obligation | Due date |
|---|---|
| Monthly EFKA | Last business day of each month |
| Payment method | e-EFKA portal or direct debit |

Late payment: 3% surcharge per month (capped at 100% of principal). Non-payment: KEAO debt collection.

### Tax deductibility

| Question | Answer |
|---|---|
| Are EFKA contributions deductible? | YES -- from gross income for income tax |
| Classification | Personal deduction |
| Which components? | All: pension, health, supplementary, OAED |

---

## Section 7 -- Parallel insurance and suspension

### Concurrent employment and self-employment

Parallel insurance applies. Client pays EFKA on BOTH activities. No offset.

### Suspension of activity

Must formally notify e-EFKA. No contributions during suspension. Health coverage continues up to 12 months after last contribution, then lapses.

### Very low income

Income level does NOT affect the contribution amount. Category minimums apply regardless.

---

## Section 8 -- Edge case registry

### EC1 -- New professional, first year
**Situation:** Registered in October 2025.
**Resolution:** Category 1. Monthly EUR 317 (EUR 307 + EUR 10 OAED). Pro-rated from registration.

### EC2 -- Professional with 12 years
**Situation:** Registered since 2013.
**Resolution:** Minimum category 3. Monthly EUR 471. May choose 4, 5, or 6.

### EC3 -- Senior professional, 22 years
**Situation:** Registered 22 years ago.
**Resolution:** Minimum category 5. Monthly EUR 703. Annual EUR 8,436.

### EC4 -- Choosing higher category
**Situation:** 3 years registered, chooses Category 4.
**Resolution:** Category 4 (above minimum). Monthly EUR 564. Annual EUR 6,768.

### EC5 -- 30-year veteran
**Situation:** 30 years registered.
**Resolution:** Category 6 mandatory. Monthly EUR 840. Annual EUR 10,080.

### EC6 -- Non-resident EU freelancer
**Situation:** EU citizen providing services in Greece.
**Resolution:** EU Regulation 883/2004. A1 certificate required. Escalate.

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
Action Required: Qualified λογιστής must confirm before advising client.
```

When a situation is outside skill scope:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to qualified λογιστής. Document gap.
```

---

## Section 10 -- Test suite

### Test 1 -- New freelancer, Category 1
**Input:** First year, age 28.
**Expected output:** Category 1. Monthly EUR 317. Annual EUR 3,804.

### Test 2 -- 8 years, minimum category
**Input:** 8 years registered.
**Expected output:** Category 2. Monthly EUR 379. Annual EUR 4,548.

### Test 3 -- 22 years, minimum
**Input:** 22 years registered.
**Expected output:** Category 5. Monthly EUR 703. Annual EUR 8,436.

### Test 4 -- Choosing higher
**Input:** 3 years, chooses Category 4.
**Expected output:** Monthly EUR 564. Annual EUR 6,768.

### Test 5 -- 30-year veteran
**Input:** 30 years.
**Expected output:** Category 6. Monthly EUR 840. Annual EUR 10,080.

### Test 6 -- Concurrent employment
**Input:** Employed + freelancing, 5 years.
**Expected output:** Self-employed EFKA Category 1 EUR 317/month in addition to employment EFKA.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
