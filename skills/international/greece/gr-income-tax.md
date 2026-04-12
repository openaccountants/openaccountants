---
name: gr-income-tax
description: >
  Use this skill whenever asked about Greek income tax for self-employed individuals (ελεύθερος επαγγελματίας). Trigger on phrases like "how much tax do I pay", "φορολογική δήλωση", "E1", "E3", "income tax return Greece", "τεκμήρια", "EFKA", "MyDATA", "self-employed tax Greece", or any question about filing or computing income tax for a self-employed or freelance client in Greece. ALWAYS read this skill before touching any Greek income tax work.
version: 2.0
jurisdiction: GR
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Greece Income Tax (Φόρος Εισοδήματος) -- Self-Employed Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Greece (Ελληνική Δημοκρατία) |
| Tax type | Φόρος εισοδήματος (income tax on business activity) |
| Primary legislation | ΚΦΕ, N.4172/2013 |
| Supporting legislation | N.4387/2016 (EFKA); N.4308/2014 (ΕΛΠ); N.5073/2023 (presumptive income); N.5246/2025 (2026 reform) |
| Tax authority | ΑΑΔΕ (Ανεξάρτητη Αρχή Δημοσίων Εσόδων) |
| Filing portal | TAXISnet / myAADE |
| Currency | EUR only |
| Return forms | E1 (income tax) + E3 (business income schedule) |
| Filing deadline | 30 June of the following year |
| Tax payment | Up to 8 monthly instalments from 31 July |
| Prepayment (προκαταβολή) | 55% of current tax (50% first 3 years) |
| EFKA contributions | 6 categories, EUR 3,060--7,800/year |
| Τέλος επιτηδεύματος | ABOLISHED from 2025 |
| Εισφορά αλληλεγγύης | ABOLISHED from 2023 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Greek λογιστής-φοροτεχνικός sign-off |
| Validation date | Pending |

**Progressive tax brackets (self-employment, 2025):**

| Taxable income (EUR) | Rate | Cumulative at top |
|---|---|---|
| 0--10,000 | 9% | EUR 900 |
| 10,001--20,000 | 22% | EUR 3,100 |
| 20,001--30,000 | 28% | EUR 5,900 |
| 30,001--40,000 | 36% | EUR 9,500 |
| 40,001+ | 44% | -- |

**Age-based reductions:**

| Age | Benefit |
|---|---|
| Under 25 | 0% on first EUR 20,000 |
| 26--30 | 9% on first EUR 20,000 |
| 31+ | Standard rates above |

**EFKA contribution categories (2025):**

| Category | Monthly EUR | Annual EUR |
|---|---|---|
| 1 (minimum) | ~255 | ~3,060 |
| 2 | ~315 | ~3,780 |
| 3 | ~375 | ~4,500 |
| 4 | ~440 | ~5,280 |
| 5 | ~530 | ~6,360 |
| 6 (maximum) | ~650 | ~7,800 |
| Special (new, <5 years) | ~156 | ~1,877 |

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown expense category | Not deductible |
| Unknown business-use proportion | 0% |
| Cash payment above EUR 500 | NOT deductible (mandatory electronic) |
| Unknown EFKA category | Category 1 (minimum) |
| Τεκμήρια vs actual | Use higher of deemed or actual income |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement for the tax year. Acceptable from: National Bank of Greece (Εθνική), Alpha Bank, Piraeus Bank (Τράπεζα Πειραιώς), Eurobank, Optima Bank, or fintech (Revolut, Wise).

**Recommended** -- invoices (transmitted via myDATA), EFKA contribution statements, KAD code, prior year E1/E3.

**Ideal** -- complete accounting records per ΕΛΠ, myDATA reconciliation, EFKA category confirmation.

### Refusal catalogue

**R-GR-1 -- Legal entity (OE, EE, AE, EPE, IKE).** *Trigger:* client is a company. *Message:* "This skill covers freelancers/sole proprietors only. Companies file corporate income tax. Please use a separate skill."

**R-GR-2 -- International income / shipping.** *Trigger:* foreign income or shipping activity. *Message:* "International income and shipping are outside scope. Consult a λογιστής-φοροτεχνικός."

**R-GR-3 -- 2026 reformed rates applied to 2025.** *Trigger:* client asks about N.5246/2025 changes. *Message:* "The 2026 reform takes effect 1 January 2026. For tax year 2025, use the current rates in Section 1."

---

## Section 3 -- Transaction pattern library (the lookup table)

### 3.1 Greek banks (fees and interest)

| Pattern | Treatment | Notes |
|---|---|---|
| ΕΘΝΙΚΗ ΤΡΑΠΕΖΑ, NATIONAL BANK OF GREECE, NBG | Bank charges: deductible | Monthly fees |
| ALPHA BANK, ΑΛΦΑ ΤΡΑΠΕΖΑ | Bank charges: deductible | Same |
| ΤΡΑΠΕΖΑ ΠΕΙΡΑΙΩΣ, PIRAEUS BANK | Bank charges: deductible | Same |
| EUROBANK, EUROBANK ERGASIAS | Bank charges: deductible | Same |
| OPTIMA BANK | Bank charges: deductible | Same |
| REVOLUT, WISE (fees) | Deductible | Fintech fees |
| ΤΟΚΟΙ, INTEREST (credit) | EXCLUDE from business income | Capital income |
| ΤΟΚΟΙ, INTEREST (debit) | Deductible if business loan | Personal: EXCLUDE |
| ΔΑΝΕΙΟ (loan principal) | EXCLUDE | Principal movement |

### 3.2 Greek government and statutory bodies

| Pattern | Treatment | Notes |
|---|---|---|
| ΑΑΔΕ, ΕΦΟΡΙΑ, ΔΟΥ | EXCLUDE | Tax payment |
| ΕΦΚΑ, EFKA | Deductible from taxable income | EFKA contributions are fully deductible |
| ΦΟΡΟΣ ΕΙΣΟΔΗΜΑΤΟΣ | EXCLUDE | Income tax payment |
| ΓΕΜΗ (General Commercial Registry) | Deductible | Registration fee |
| ΕΠΙΜΕΛΗΤΗΡΙΟ (Chamber of Commerce) | Deductible | Membership fee |

### 3.3 Greek utilities and telecoms

| Pattern | Treatment | Notes |
|---|---|---|
| ΔΕΗ (Public Power Corporation) | Deductible if business premises | Electricity; apportion if home |
| ΦΥΣΙΚΟ ΑΕΡΙΟ, ΔΕΠΑ | Deductible if business premises | Gas |
| COSMOTE, VODAFONE GR, WIND, NOVA | Deductible: business phone/internet | Mixed: apportion |
| FORTHNET, HOL | Deductible: business internet | Mixed: apportion |
| ΕΥΔΑΠ (water -- Athens) | Deductible if business premises | Water |

### 3.4 SaaS and software -- international

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, ADOBE, META | Deductible expense | EU reverse charge ΦΠΑ |
| GITHUB, OPENAI, ANTHROPIC | Deductible expense | Non-EU |
| SLACK, ZOOM, ATLASSIAN | Deductible expense | Check entity |

### 3.5 Professional services (Greece)

| Pattern | Treatment | Notes |
|---|---|---|
| ΛΟΓΙΣΤΗΣ, ΛΟΓΙΣΤΙΚΟ ΓΡΑΦΕΙΟ | Deductible | Accounting fees |
| ΔΙΚΗΓΟΡΟΣ, ΔΙΚΗΓΟΡΙΚΟ ΓΡΑΦΕΙΟ | Deductible if business | Legal fees |
| ΣΥΜΒΟΛΑΙΟΓΡΑΦΟΣ | Deductible if business | Notary fees |
| ΦΟΡΟΤΕΧΝΙΚΟΣ | Deductible | Tax advisory |

### 3.6 Transport and travel

| Pattern | Treatment | Notes |
|---|---|---|
| ΟΣΕ, TRAINOSE, HELLENIC TRAIN | Deductible if business | Train |
| ΑΕΡΟΠΟΡΙΑ, AEGEAN, OLYMPIC AIR | Deductible if business travel | Flights |
| ΚΤΕΛ | Deductible if business | Intercity bus |
| OASA, METRO, STASY (Athens transport) | Deductible if business | Public transport |
| SHELL GR, BP GR, AVIN, EKO | Deductible: business vehicle portion | Fuel |
| UBER, BEAT, BOLT | Deductible if business | Ride services |

### 3.7 Office and supplies

| Pattern | Treatment | Notes |
|---|---|---|
| PUBLIC, PLAISIO, KOTSOVOLOS | Capital if > EUR 1,500; else expense | IT/electronics |
| ΙΚΕΑ, IKEA GR | Capital or expense depending on value | Office items |
| ΕΛΤΑ (Hellenic Post) | Deductible | Postage |

### 3.8 Food and entertainment

| Pattern | Treatment | Notes |
|---|---|---|
| ΑΒ ΒΑΣΙΛΟΠΟΥΛΟΣ, ΣΚΛΑΒΕΝΙΤΗΣ, LIDL GR, ΜΑΣΟΥΤΗΣ | Default: NOT deductible | Personal provisioning |
| ΕΣΤΙΑΤΟΡΙΟ, RESTAURANT | Deductible if documented business purpose | But >50% personal element = blocked |

### 3.9 Cash payment limit (critical)

| Rule | Detail |
|---|---|
| All business expenses above EUR 500 | MUST be paid electronically (bank transfer, card) |
| Cash payments above EUR 500 | NOT deductible regardless of documentation |

### 3.10 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| ΜΕΤΑΦΟΡΑ, OWN TRANSFER | EXCLUDE | Internal |
| ΑΝΑΛΗΨΗ, ATM | EXCLUDE (default: drawings) | Ask client |
| ΚΑΤΑΘΕΣΗ | EXCLUDE | Owner deposit |

---

## Section 4 -- Worked examples

### Example 1 -- Standard freelancer, mid-range

**Input:** Consultant, age 35, net profit EUR 35,000 after expenses, EFKA Cat 1 (EUR 3,060).
**Computation:** Taxable = EUR 31,940. Tax = EUR 900 + EUR 2,200 + EUR 2,800 + EUR 698 = EUR 6,598. Prepayment = 55% x EUR 6,598 = EUR 3,629. Year-1 total = EUR 10,227 + EFKA EUR 3,060.

### Example 2 -- Young freelancer under 25

**Input:** Age 24, developer, net profit EUR 22,000, EFKA Special (EUR 1,877).
**Computation:** Taxable = EUR 20,123. Under-25: 0% on first EUR 20,000. Tax = 28% x EUR 123 = EUR 34. Prepayment = 50% x EUR 34 = EUR 17. Total = EUR 51 + EFKA EUR 1,877.

### Example 3 -- Presumptive income exceeds actual

**Input:** Athens freelancer, net profit EUR 6,000, no employees, min wage EUR 9,960.
**Computation:** Deemed = EUR 9,960. Since EUR 9,960 > EUR 6,000, taxed on EUR 9,960 unless rebutted. Tax = 9% x EUR 9,960 = EUR 896.

### Example 4 -- Cash expense disallowed

**Input:** Freelancer pays EUR 800 cash for equipment.
**Result:** NOT deductible. Above EUR 500 cash limit. Must use electronic payment.

---

## Section 5 -- Tier 1 rules (deterministic)

### 5.1 Tax rate brackets
Progressive 9%/22%/28%/36%/44%. Self-employed do NOT get the EUR 777 employment/pension tax reduction. Under-25: 0% on first EUR 20,000. Ages 26-30: 9% on first EUR 20,000. **Legislation:** ΚΦΕ Art. 29.

### 5.2 Prepayment (προκαταβολή)
55% of current year's tax. First 3 years: 50%. Offset against next year. Creates double burden in year 1. **Legislation:** Art. 69.

### 5.3 Abolished levies
Τέλος επιτηδεύματος: abolished from 2025. Εισφορά αλληλεγγύης: abolished from 2023. Do NOT include in any 2025 computation. **Legislation:** Various amendment acts.

### 5.4 Τεκμήρια (presumptive income)
Minimum = highest of: employee-equivalent (EUR 9,960), plus 10% of labour costs up to EUR 15,000, plus 5% of revenue above KAD average. Cap EUR 50,000. First 3 years: exempt. Municipality < 1,500: 50% reduction. Disability 67%+: exempt. **Legislation:** Art. 28A-28Γ.

### 5.5 Cash payment limit
EUR 500 maximum for deductible cash payments. Above: must be electronic. Non-compliance = non-deductible. **Legislation:** ΚΦΕ Art. 23.

### 5.6 Depreciation
Buildings: 4%. Equipment: 10%. Transport: 16%. Computers: 20%. Software: 20%. Tools: 33%. Assets under EUR 1,500: expense immediately. **Legislation:** Art. 24.

### 5.7 EFKA
6 categories. Category choice locks in for calendar year. Selection by 31 January. New self-employed (<5 years): special reduced category. Fully deductible from taxable income. **Legislation:** N.4387/2016.

### 5.8 MyDATA
All income/expense documents must be transmitted to myDATA. Real-time or by VAT deadline. B2B e-invoicing mandatory from 2026 (phased). **Legislation:** N.4308/2014.

---

## Section 6 -- Tier 2 catalogue

### 6.1 Τεκμήρια rebuttal
*Why:* Deemed income may exceed actual. *Default:* Tax on higher amount. *Question:* "Can you provide evidence (bank statements, contracts) showing actual income is lower than deemed?"

### 6.2 EFKA category optimization
*Why:* Higher category = higher deduction but higher outlay. *Default:* Category 1 (minimum). *Question:* "Which EFKA category did you choose?"

### 6.3 Dual activity (employment + freelance)
*Why:* Income combined. EFKA parallel rules. *Default:* Flag for reviewer. *Question:* "Do you have employment income? Employer pays EFKA from that?"

### 6.4 Motor vehicle business proportion
*Why:* Only business portion deductible. *Default:* 0%. *Question:* "What proportion of vehicle use is business?"

### 6.5 Municipality population
*Why:* <1,500 inhabitants = 50% presumptive reduction. *Default:* Standard (no reduction). *Question:* "What is the population of your registered municipality?"

---

## Section 7 -- Excel working paper template

### Sheet "Transactions"
Columns: Date, Counterparty, Description, Amount (EUR), Category (Revenue/Expense/Depreciation/EFKA/EXCLUDE), Deductible amount, Payment method (Electronic/Cash), Default?, Question, Notes.

### Sheet "Tax Computation"
Progressive bracket calculation. Τεκμήρια comparison. Prepayment. EFKA deduction.

---

## Section 8 -- Bank statement reading guide

**CSV formats.** National Bank of Greece uses semicolons with DD/MM/YYYY. Alpha Bank uses CSV with various formats. Piraeus Bank uses semicolons. Common columns: Ημερομηνία (Date), Περιγραφή (Description), Ποσό (Amount), Υπόλοιπο (Balance).

**Greek language variants.** Common: μεταφορά (transfer), κατάθεση (deposit), ανάληψη (withdrawal), προμήθεια (commission), τόκοι (interest), τιμολόγιο (invoice), πληρωμή (payment), ενοίκιο (rent).

**EFKA payments.** Monthly to EFKA. Fully deductible from income.

**Payment method tracking.** Critical for EUR 500 cash rule. Card/transfer = deductible. Cash > EUR 500 = non-deductible.

---

## Section 9 -- Onboarding fallback

### 9.1 Activity type
*Inference:* From counterparty mix. *Fallback:* "Freelancer or sole proprietorship? What is your KAD code?"

### 9.2 Years in business
*Inference:* Not inferable. *Fallback:* "How many years have you been self-employed? (Affects presumptive exemption and prepayment rate.)"

### 9.3 EFKA category
*Inference:* From EFKA payment amounts. *Fallback:* "Which EFKA category are you in?"

### 9.4 Age
*Inference:* Not inferable. *Fallback:* "What is your age? (Under 25 and 26-30 get reduced rates.)"

### 9.5 Municipality
*Inference:* From address. *Fallback:* "Where is your registered address? Population < 1,500?"

### 9.6 Employees
*Inference:* Salary outflows. *Fallback:* "Do you have employees? (Affects τεκμήρια.)"

---

## Section 10 -- Reference material

### Test suite

**Test 1 -- Mid-range freelancer.** EUR 35,000 profit, EFKA Cat 1. Tax EUR 6,598 + prepayment EUR 3,629 = EUR 10,227 + EFKA EUR 3,060.
**Test 2 -- High earner.** EUR 80,000 profit, EFKA Cat 3. Tax EUR 25,120 + prepayment EUR 13,816.
**Test 3 -- Under 25.** EUR 22,000, 0% on first EUR 20,000. Tax EUR 34.
**Test 4 -- New freelancer year 1.** EUR 20,000, prepayment at 50%. Total EUR 3,641.
**Test 5 -- Presumptive > actual.** EUR 6,000 actual, EUR 9,960 deemed. Tax on EUR 9,960.
**Test 6 -- Cash disallowed.** EUR 2,000 cash purchase. Non-deductible.
**Test 7 -- Abolished levies.** Remove τέλος (EUR 650) and solidarity surcharge.

### Edge case registry

**EC1 -- Presumptive exceeds actual.** Tax on deemed unless rebutted.
**EC2 -- Year-1 double burden.** Full tax + prepayment.
**EC3 -- Cash > EUR 500.** Non-deductible.
**EC4 -- Under 25 exemption.** 0% on first EUR 20,000.
**EC5 -- Small municipality.** 50% presumptive reduction.
**EC6 -- EFKA category impact.** Higher category = lower tax but higher outlay.
**EC7 -- Employment + freelance.** Combined brackets. Parallel EFKA.
**EC8 -- Low-value assets.** Under EUR 1,500 = expense immediately.
**EC9 -- Τέλος included.** REMOVE -- abolished 2025.
**EC10 -- Solidarity surcharge.** REMOVE -- abolished 2023.

### Prohibitions

- NEVER apply employment/pension tax reduction (EUR 777) to self-employment
- NEVER include τέλος επιτηδεύματος in 2025+ computation
- NEVER include εισφορά αλληλεγγύης in 2023+ computation
- NEVER allow cash expenses above EUR 500 as deductible
- NEVER ignore τεκμήρια presumptive income check
- NEVER allow depreciation on assets under EUR 1,500
- NEVER present 55% prepayment as optional
- NEVER allow EFKA category change mid-year
- NEVER apply 2026 reformed rates to 2025 income
- NEVER present calculations as definitive

### Sources

1. ΚΦΕ N.4172/2013
2. N.4387/2016 (EFKA)
3. N.4308/2014 (ΕΛΠ)
4. N.5073/2023 (presumptive income)
5. ΑΑΔΕ -- https://www.aade.gr

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a λογιστής-φοροτεχνικός or equivalent licensed practitioner in Greece) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
