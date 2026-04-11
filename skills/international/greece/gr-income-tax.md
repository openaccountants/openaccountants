---
name: gr-income-tax
description: >
  Use this skill whenever asked about Greek income tax for self-employed individuals (ελεύθερος επαγγελματίας). Trigger on phrases like "how much tax do I pay", "φορολογική δήλωση", "E1", "E3", "income tax return Greece", "τεκμήρια", "EFKA", "MyDATA", "self-employed tax Greece", or any question about filing or computing income tax for a self-employed or freelance client in Greece. This skill covers the progressive 9%-44% rate brackets, τεκμήρια (deemed income/presumptive rules), EFKA social insurance, τέλος επιτηδεύματος (abolished 2025), εισφορά αλληλεγγύης (abolished 2023), depreciation, MyDATA e-books, filing deadlines, and penalties. ALWAYS read this skill before touching any Greek income tax work.
version: 1.0
jurisdiction: GR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Greece Income Tax (Φόρος Εισοδήματος) -- Self-Employed Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Greece |
| Jurisdiction Code | GR |
| Primary Legislation | Κώδικας Φορολογίας Εισοδήματος (ΚΦΕ), N.4172/2013 |
| Supporting Legislation | N.4387/2016 (EFKA); N.4308/2014 (Greek Accounting Standards / ΕΛΠ); N.5073/2023 (presumptive income); N.5246/2025 (2026 reform) |
| Tax Authority | Ανεξάρτητη Αρχή Δημοσίων Εσόδων (ΑΑΔΕ -- Independent Authority for Public Revenue) |
| Filing Portal | TAXISnet (taxisnet.gr) / myAADE |
| Contributor | Open Accountants Community |
| Validated By | Pending -- requires Greek λογιστής-φοροτεχνικός sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate brackets, filing deadlines, τέλος επιτηδεύματος status, EFKA category structure. Tier 2: τεκμήρια calculations, expense apportionment, EFKA category selection, MyDATA compliance. Tier 3: international income, tax treaties, shipping income, crypto. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags and presents options. Qualified λογιστής-φοροτεχνικός must confirm.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate and document.

---

## Step 0: Client Onboarding Questions

Before computing any income tax figure, you MUST know:

1. **Self-employment type** [T1] -- ελεύθερος επαγγελματίας (freelancer/professional), ατομική επιχείρηση (sole proprietorship), or other.
2. **KAD activity code(s)** [T1] -- determines presumptive income calculation and VAT treatment.
3. **Gross revenue (ακαθάριστα έσοδα)** [T1] -- total invoiced in the year.
4. **Business expenses (δαπάνες)** [T1/T2] -- documented deductible expenses.
5. **Number of employees** [T1] -- affects presumptive income calculation.
6. **Years in business** [T1] -- new professionals (<5 years) get reduced EFKA contributions.
7. **EFKA category chosen** [T1] -- which of the 6 insurance categories was elected.
8. **Other income** [T1] -- employment (μισθωτές υπηρεσίες), rental, dividends, interest.
9. **Population of municipality** [T2] -- affects presumptive income reduction (50% for municipalities <1,500 inhabitants).

**If activity type and gross revenue are unknown, STOP. Do not compute.**

---

## Step 1: Determine Tax Rate Brackets [T1]

**Legislation:** ΚΦΕ, Art. 29

### Self-Employment Income Tax Rates (2025)

| Taxable Income (EUR) | Rate | Cumulative Tax at Top (EUR) |
|---------------------|------|-----------------------------|
| 0 -- 10,000 | 9% | 900 |
| 10,001 -- 20,000 | 22% | 3,100 |
| 20,001 -- 30,000 | 28% | 5,900 |
| 30,001 -- 40,000 | 36% | 9,500 |
| 40,001+ | 44% | -- |

**Important distinctions from employment/pension income:**
- Self-employed income does NOT benefit from the tax reduction (μείωση φόρου) of up to EUR 777 that applies to employment/pension income
- Self-employed under 25: 0% rate on first two bands (up to EUR 20,000)
- Self-employed aged 26-30: 9% rate on first two bands (up to EUR 20,000)

---

## Step 2: Prepayment of Tax (Προκαταβολή φόρου) [T1]

**Legislation:** ΚΦΕ, Art. 69

| Item | Detail |
|------|--------|
| Rate | 55% of current year's tax liability |
| Due | With the annual return |
| Credit | Offset against next year's final tax |
| First year | Reduced to 50% in the first 3 years of activity |

**The prepayment is calculated on the current year's tax and credited against the following year. This means a new self-employed person faces a double payment burden in year 1 (full tax + 55% prepayment).**

---

## Step 3: Abolished Levies -- Status Confirmation [T1]

### Τέλος Επιτηδεύματος (Professional Tax / Business Levy) [T1]

| Year | Status |
|------|--------|
| Up to 2023 | EUR 650/year for individuals |
| 2024 | Reduced to EUR 325 (50% reduction) |
| 2025 onwards | **ABOLISHED** -- no longer payable |

### Εισφορά Αλληλεγγύης (Solidarity Surcharge) [T1]

| Year | Status |
|------|--------|
| Up to 2022 | Progressive 2.2% -- 10% surcharge on income above EUR 12,000 |
| 2023 onwards | **ABOLISHED** for all private-sector income |

**Do NOT include τέλος επιτηδεύματος or εισφορά αλληλεγγύης in any 2025 tax computation.**

---

## Step 4: Τεκμήρια -- Presumptive / Deemed Income (Minimum Taxable Income) [T1/T2]

**Legislation:** ΚΦΕ, Art. 28A-28Γ (as amended by N.5073/2023)

### How It Works [T1]

Greece imposes a minimum presumed net business income for self-employed persons. Even if actual profit is lower, the taxpayer may be taxed on the higher deemed amount.

### Calculation Components [T2]

The minimum presumed income is the HIGHEST of:

1. **Employee-equivalent income:** The taxpayer is presumed to earn at least what a full-time employee would earn at the minimum wage (EUR 830/month gross in 2025 = approximately EUR 9,960/year), OR at least what their highest-paid employee earns

2. **Plus: 10% of annual labour costs up to EUR 15,000**

3. **Plus: 5% of revenue exceeding the average revenue for the taxpayer's KAD activity code**

**The deemed income cap is EUR 50,000** -- the presumptive system cannot impute more than this.

### Exemptions / Reductions [T1]

| Condition | Reduction |
|-----------|----------|
| Municipality with population < 1,500 | 50% reduction in minimum presumed income |
| First 3 years of activity | Exemption from presumptive rules |
| Disability (67%+) | Exemption |
| Reservist military service period | Proportional reduction |

### Interaction with Actual Income [T2]

- If actual net income > deemed minimum: tax based on actual income (no adjustment)
- If actual net income < deemed minimum: taxpayer must justify the difference or be taxed on the deemed amount
- Taxpayer can rebut the presumption with evidence (bank statements, contracts, etc.)
- [T2] Flag for reviewer whenever deemed income exceeds actual income

---

## Step 5: Deductible Expenses [T1/T2]

**Legislation:** ΚΦΕ, Art. 22-23; ΕΛΠ (Greek Accounting Standards)

### Deductible [T1]

| Expense | Treatment |
|---------|-----------|
| Rent (business premises) | Fully deductible |
| EFKA contributions | Fully deductible |
| Professional insurance | Fully deductible |
| Accountancy / legal fees | Fully deductible |
| Office supplies | Fully deductible |
| Software subscriptions | Fully deductible |
| Marketing / advertising | Fully deductible |
| Telecommunications (business) | Fully deductible or proportional |
| Travel (business purpose, documented) | Fully deductible |
| Training / conferences (related to activity) | Fully deductible |
| Bank charges (business account) | Fully deductible |

### NOT Deductible [T1]

| Expense | Reason |
|---------|--------|
| Personal expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax | Cannot deduct tax on income |
| Entertainment (>50% personal element) | Blocked |
| Expenses without proper documentation | Art. 23 -- must have legal receipt/invoice |
| Expenses paid in cash above EUR 500 | Must use electronic payment (bank transfer, card) |

### Cash Payment Limit [T1]

**All business expenses above EUR 500 must be paid electronically (bank transfer, credit/debit card, cheque).** Cash payments above EUR 500 are non-deductible even if properly documented.

---

## Step 6: Depreciation (Αποσβέσεις) [T1]

**Legislation:** ΚΦΕ, Art. 24; ΕΛΠ

### Depreciation Rates (Straight-Line)

| Asset Type | Annual Rate |
|-----------|-------------|
| Buildings (commercial/industrial) | 4% |
| Mechanical/electrical equipment | 10% |
| Transport vehicles | 16% |
| Computer hardware | 20% |
| Computer software | 20% |
| Office equipment / furniture | 10% |
| Tools and instruments | 33% |
| Patents, licences | 10% |
| Goodwill (from acquisition) | 10% |

### Rules [T1]

- Depreciation starts in the year the asset is first used in the business
- Straight-line method on cost price (residual value can be set to zero)
- Low-value assets under EUR 1,500: may be fully expensed in the year of acquisition
- Motor vehicles: only the business-use proportion is deductible [T2]

---

## Step 7: EFKA Social Insurance Contributions [T1/T2]

**Legislation:** N.4387/2016, as amended

### Contribution Structure

Self-employed persons choose one of 6 insurance categories annually (by 31 January). If no choice is made, Category 1 applies.

### 2025 Monthly Contribution Amounts (approximate)

| Category | Monthly Amount (EUR) | Annual Amount (EUR) |
|----------|---------------------|---------------------|
| 1 (minimum) | ~255 | ~3,060 |
| 2 | ~315 | ~3,780 |
| 3 | ~375 | ~4,500 |
| 4 | ~440 | ~5,280 |
| 5 | ~530 | ~6,360 |
| 6 (maximum) | ~650 | ~7,800 |
| Special (new, <5 years) | ~156 | ~1,877 |

**Components:** Pension (primary), health insurance, and supplementary pension contributions are bundled into the category amount.

### Key Rules [T1]

- EFKA contributions are fully deductible from taxable income
- Category choice locks in for the full calendar year
- New self-employed (<5 years experience): special reduced category available
- If also employed: employer pays EFKA from employment; self-employment EFKA is reduced (parallel insurance rules apply)
- EFKA is mandatory -- there is no opt-out

---

## Step 8: MyDATA E-Books and Invoicing [T1]

**Legislation:** N.4308/2014 (ΕΛΠ); ΑΑΔΕ Decision A.1138/2020

### Requirements (2025)

| Requirement | Detail |
|-------------|--------|
| Data transmission to myDATA | All income and expense documents must be transmitted to the ΑΑΔΕ myDATA platform |
| Timing | Real-time or daily preferred; no later than VAT return deadline |
| Required data | Issuer TIN, recipient TIN, invoice number, date, amounts, VAT, classification codes |
| Tools | Private EDIP provider or free government tools (timologio.minfin.gr, myDATAapp) |
| Income classification | Revenue must be classified by income type (services, goods, etc.) |
| Expense classification | Expenses must be classified for deductibility |

### B2B E-Invoicing Mandate (2026)

| Turnover (2023) | Mandatory From |
|-----------------|---------------|
| Above EUR 1,000,000 | 2 March 2026 |
| All remaining taxpayers | 1 October 2026 |

**For tax year 2025, myDATA e-book transmission is mandatory but structured e-invoicing (B2B) is not yet required.**

---

## Step 9: Filing Deadlines [T1]

**Legislation:** ΚΦΕ; Κώδικας Φορολογικής Διαδικασίας

| Filing / Payment | Deadline |
|-----------------|----------|
| E1 (annual income tax return) + E3 (business income schedule) | 30 June of following year |
| Prepayment of tax (προκαταβολή) | With E1, by 30 June |
| Tax payment | In up to 8 equal monthly instalments starting 31 July |
| VAT return | Monthly by 26th, or quarterly |
| myDATA e-book data transmission | Ongoing / at least by VAT return deadline |
| EFKA category selection | 31 January |

---

## Step 10: Penalties [T1]

**Legislation:** Κώδικας Φορολογικής Διαδικασίας, Art. 54-59

| Offence | Penalty |
|---------|---------|
| Late filing of E1 | EUR 100 (within 30 days), or higher for extended delay |
| Inaccurate return | 10% of additional tax if self-corrected; higher if audited |
| Late payment interest | 0.73% per month (8.76% per annum) |
| Failure to issue invoices | EUR 500 -- EUR 5,000 per instance |
| Failure to transmit myDATA data | EUR 250 -- EUR 10,000 depending on severity |
| Tax evasion (above EUR 100,000) | Criminal penalties under N.4174/2013 |

---

## Step 11: Edge Case Registry

### EC1 -- Presumptive income exceeds actual profit [T2]
**Situation:** Freelance graphic designer earns EUR 8,000 net profit but deemed minimum income is EUR 12,000.
**Resolution:** Taxpayer is taxed on EUR 12,000 (the higher amount) unless they can rebut with evidence. Tax = 9% x EUR 10,000 + 22% x EUR 2,000 = EUR 900 + EUR 440 = EUR 1,340. [T2] Flag for reviewer: assist client in gathering evidence to rebut presumption if actual income is genuinely lower.

### EC2 -- New self-employed, first-year double tax burden [T1]
**Situation:** New freelancer in year 1, net profit EUR 25,000. No prior prepayment credit.
**Resolution:** Tax = EUR 900 + EUR 2,200 + EUR 1,400 = EUR 4,500. Prepayment = 50% x EUR 4,500 = EUR 2,250 (reduced rate for first 3 years). Total year-1 payment = EUR 6,750. Warn client about the front-loaded burden.

### EC3 -- Expense paid in cash above EUR 500 [T1]
**Situation:** Freelancer pays EUR 800 cash for equipment.
**Resolution:** NOT deductible. Payment must be electronic (bank transfer, card) for amounts above EUR 500. The expense is lost for tax purposes even if a proper invoice exists.

### EC4 -- Young freelancer under 25 [T1]
**Situation:** 23-year-old software developer, net profit EUR 18,000.
**Resolution:** Under-25 exemption: 0% rate on first two bands (up to EUR 20,000). Tax = EUR 0. Prepayment = EUR 0. Only EFKA contributions are due.

### EC5 -- Municipality with <1,500 inhabitants [T2]
**Situation:** Freelancer based in a small village (population 800), deemed income would be EUR 15,000.
**Resolution:** 50% reduction in presumptive income: EUR 7,500. Tax on EUR 7,500 = 9% x EUR 7,500 = EUR 675. [T2] Verify municipality population and that the taxpayer's registered address qualifies.

### EC6 -- EFKA category selection impact on total burden [T2]
**Situation:** Freelancer earning EUR 30,000 net is deciding between EFKA Category 1 (EUR 3,060/year) and Category 3 (EUR 4,500/year).
**Resolution:** Category 1: taxable after EFKA = EUR 26,940. Tax = EUR 900 + EUR 2,200 + EUR 1,943 = EUR 5,043. Category 3: taxable after EFKA = EUR 25,500. Tax = EUR 900 + EUR 2,200 + EUR 1,540 = EUR 4,640. Higher EFKA = lower tax, but total out-of-pocket differs. [T2] Present full comparison to client.

### EC7 -- Dual activity: employment + freelance [T1/T2]
**Situation:** Employee earning EUR 20,000 also freelances earning EUR 15,000 net.
**Resolution:** Employment income taxed separately (employer withholds). Freelance income taxed at progressive rates (starting from 9% on first EUR 10,000). But total income determines the final tax band. Income is combined on E1. EFKA from employment covers pension; freelance EFKA may be reduced. [T2] Flag for reviewer to verify parallel insurance treatment.

### EC8 -- Depreciation of low-value asset [T1]
**Situation:** Freelancer buys a printer for EUR 400.
**Resolution:** Below EUR 1,500 threshold. May expense fully in the year of acquisition rather than depreciating. EUR 400 goes directly to expenses.

### EC9 -- Τέλος επιτηδεύματος included in computation [T1]
**Situation:** Accountant's software automatically adds EUR 650 business levy to the tax computation.
**Resolution:** INCORRECT for 2025. The τέλος επιτηδεύματος was abolished from 2025 onwards. Remove from computation. The EUR 325 reduced rate applied only in 2024.

### EC10 -- Client claims solidarity surcharge [T1]
**Situation:** Tax return includes εισφορά αλληλεγγύης calculation.
**Resolution:** INCORRECT for 2025. The solidarity surcharge was abolished for all private-sector income from 2023 onwards. Remove from computation.

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
Action Required: Qualified λογιστής-φοροτεχνικός must confirm before filing.
```

When Claude identifies a [T3] situation:

```
ESCALATION REQUIRED
Tier: T3
Client: [name]
Situation: [description]
Issue: [outside skill scope]
Action Required: Do not advise. Refer to λογιστής-φοροτεχνικός. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard freelancer, mid-range income
**Input:** Freelance consultant, aged 35, net profit EUR 35,000 after expenses, EFKA Category 1 (EUR 3,060 deducted).
**Expected output:** Taxable = EUR 35,000 - EUR 3,060 = EUR 31,940. Tax = EUR 900 + EUR 2,200 + EUR 2,800 + EUR 698 = EUR 6,598. Prepayment = 55% x EUR 6,598 = EUR 3,629. Total = EUR 10,227. Plus EFKA EUR 3,060.

### Test 2 -- High-income freelancer, top bracket
**Input:** Freelance architect, net profit EUR 80,000, EFKA Category 3 (EUR 4,500).
**Expected output:** Taxable = EUR 75,500. Tax = EUR 900 + EUR 2,200 + EUR 2,800 + EUR 3,600 + EUR 15,620 = EUR 25,120. Prepayment = 55% x EUR 25,120 = EUR 13,816. Total = EUR 38,936. Plus EFKA EUR 4,500.

### Test 3 -- Young freelancer under 25
**Input:** 24-year-old developer, net profit EUR 22,000, EFKA Special Category (EUR 1,877).
**Expected output:** Taxable = EUR 20,123. Under-25 rule: 0% on first EUR 20,000. Tax = 28% x EUR 123 = EUR 34. Prepayment = 50% x EUR 34 = EUR 17. Total = EUR 51. Plus EFKA EUR 1,877.

### Test 4 -- New freelancer, year-1 double burden
**Input:** New freelancer (year 1), net profit EUR 20,000, EFKA Category 1 (EUR 3,060), aged 40.
**Expected output:** Taxable = EUR 16,940. Tax = EUR 900 + EUR 1,527 = EUR 2,427. Prepayment = 50% x EUR 2,427 = EUR 1,214 (first 3 years = 50%). Total payment = EUR 3,641. Plus EFKA EUR 3,060.

### Test 5 -- Presumptive income exceeds actual
**Input:** Freelancer in Athens, net profit EUR 6,000, no employees, minimum wage EUR 9,960.
**Expected output:** Deemed minimum income = EUR 9,960 (employee-equivalent). Since EUR 9,960 > EUR 6,000, taxed on EUR 9,960. Tax = 9% x EUR 9,960 = EUR 896. Unless rebutted with evidence.

### Test 6 -- Cash payment disallowed
**Input:** Freelancer claims EUR 2,000 equipment expense paid in cash.
**Expected output:** EUR 2,000 is NOT deductible (above EUR 500 cash limit). Remove from expenses. Advise client to use electronic payment for future purchases.

### Test 7 -- Abolished levies check
**Input:** Tax computation includes EUR 650 τέλος επιτηδεύματος and EUR 500 εισφορά αλληλεγγύης.
**Expected output:** Remove both. Τέλος επιτηδεύματος abolished from 2025. Εισφορά αλληλεγγύης abolished from 2023. Total reduction = EUR 1,150.

---

## PROHIBITIONS

- NEVER apply the employment/pension tax reduction (EUR 777) to self-employment income -- it does not apply
- NEVER include τέλος επιτηδεύματος in any 2025 or later computation -- it is abolished
- NEVER include εισφορά αλληλεγγύης in any 2023 or later computation -- it is abolished
- NEVER allow expenses paid in cash above EUR 500 as deductible -- electronic payment is mandatory
- NEVER ignore the τεκμήρια (presumptive income) -- always check whether deemed income exceeds actual
- NEVER allow depreciation on assets below EUR 1,500 that could be expensed immediately
- NEVER present the 55% prepayment as optional -- it is mandatory
- NEVER allow a client to change EFKA category mid-year -- the choice locks in for 12 months
- NEVER advise on shipping income, international structures, or tax treaties -- escalate to T3
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their λογιστής-φοροτεχνικός for confirmation
- NEVER apply 2026 reformed rates to 2025 income -- the N.5246/2025 changes take effect 1 January 2026

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a λογιστής-φοροτεχνικός or equivalent licensed practitioner in Greece) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
