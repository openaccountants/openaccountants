---
name: au-individual-return
description: >
  Use this skill whenever asked about Australian individual income tax for sole traders. Trigger on phrases like "how much tax do I pay in Australia", "Australian tax return", "sole trader tax", "ABN tax", "Medicare levy", "LITO", "PAYG", "tax brackets Australia", "BAS", "instant asset write-off", "home office deduction", "HELP repayment", "HECS debt", "small business income tax offset", "motor vehicle deduction", or any question about filing or computing income tax for an Australian sole trader. Covers 2024-25 Stage 3 tax rates, Medicare levy and surcharge, LITO, business income computation, allowable deductions, depreciation, instant asset write-off, small business income tax offset, HELP/HECS repayments, and final tax computation. ALWAYS read this skill before touching any Australian income tax work.
version: 2.0
jurisdiction: AU
tax_year: 2024-25
category: international
depends_on:
  - income-tax-workflow-base
---

# Australia Individual Income Tax -- Sole Trader Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Australia |
| Tax | Income tax + Medicare levy + HELP repayments (if applicable) |
| Currency | AUD only |
| Tax year | 1 July 2024 -- 30 June 2025 |
| Primary legislation | Income Tax Assessment Act 1997 (ITAA 1997); Income Tax Assessment Act 1936 (ITAA 1936) |
| Supporting legislation | Tax Administration Act 1953; Medicare Levy Act 1986; Higher Education Support Act 2003 |
| Tax authority | Australian Taxation Office (ATO) |
| Filing portal | myTax (via myGov) or registered tax agent |
| Filing deadline | 31 October 2025 (self-lodged); May 2026 (tax agent) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- Australian CPA/CA sign-off required |
| Skill version | 2.0 |

### Tax Rates -- Resident Individual (2024-25, Stage 3) [T1]

| Taxable Income (AUD) | Rate | Tax on This Band |
|---|---|---|
| 0 -- 18,200 | 0% | Tax-free threshold |
| 18,201 -- 45,000 | 16% | Max $4,288 |
| 45,001 -- 135,000 | 30% | Max $27,000 |
| 135,001 -- 190,000 | 37% | Max $20,350 |
| 190,001+ | 45% | |

### Medicare Levy [T1]

| Item | Value |
|---|---|
| Rate | 2% of taxable income |
| Low-income threshold (single) | $26,000 (no levy below; phase-in to $32,500) |
| Low-income threshold (family) | $43,846 + $4,027 per dependent child |
| Surcharge (no private hospital cover) | Additional 1%-1.5% if income over $93,000 (single) |

### Low Income Tax Offset (LITO) [T1]

| Taxable Income (AUD) | LITO |
|---|---|
| Up to $45,000 | $700 |
| $45,001 -- $66,667 | Reduces by 5c per $1 over $45,000 |
| $66,668+ | $0 |

### Small Business Income Tax Offset (SBITO) [T1]

| Item | Value |
|---|---|
| Rate | 16% of income tax on business income |
| Cap | $1,000 |
| Eligibility | Aggregated turnover under $5 million (individuals and trusts only) |

### Key Deduction Rates [T1]

| Item | Rate |
|---|---|
| Home office -- fixed rate method | 67 cents per hour |
| Motor vehicle -- cents per km method | 88 cents per km (max 5,000 km) |
| Instant asset write-off (small business) | $20,000 threshold (assets under $20,000 immediately deductible) |
| Superannuation (deductible personal contribution) | Up to $30,000 concessional cap |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Unknown residency status | Australian resident (but STOP if genuinely unclear) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown depreciation effective life | Use ATO's Table of Depreciation |
| Unknown private health insurance status | No cover (Medicare levy surcharge may apply) |
| Unknown aggregated turnover | Over $10 million (no small business concessions) |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full financial year (1 July to 30 June), confirmation of ABN/TFN, and whether the taxpayer is an Australian resident.

**Recommended** -- all tax invoices issued, purchase receipts, PAYG payment summaries or income statements (via myGov), prior year tax return, BAS lodgments.

**Ideal** -- complete bookkeeping records, depreciation schedule, motor vehicle logbook, home office hours log, private health insurance statement, HELP debt balance.

### Refusal Catalogue

**R-AU-1 -- Companies and trusts.** "Companies lodge company tax returns. Trusts lodge trust returns. This skill covers individual sole traders only."

**R-AU-2 -- Non-residents.** "Non-resident tax rates and rules differ significantly. Out of scope."

**R-AU-3 -- Capital gains tax events.** "CGT events require specialised computation (cost base, discounts, exemptions). Out of scope."

**R-AU-4 -- Complex depreciation (effective life disputes).** "Where the ATO effective life is contested or the asset has no published rate, escalate."

**R-AU-5 -- Partnership or PSI (Personal Services Income).** "PSI rules and partnership allocations require separate analysis. Escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | Tax Label | Treatment | Notes |
|---|---|---|---|
| ABN INCOME, CLIENT PAYMENT, [client name] | Business income (Item P8) | Gross business income | Core sole trader income |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Revenue | Match to underlying invoices |
| PAYPAL TRANSFER | Business income | Revenue | Report gross before fees |
| DIRECT CREDIT [client name] | Business income | Revenue | Bank transfer from client |
| INTEREST, SAVINGS INTEREST | Interest income (Item 10) | NOT business income | Report separately as interest |
| DIVIDEND, DISTRIBUTION | Dividend income (Item 11) | NOT business income | Report separately. Include franking credits. |
| FRANKING CREDIT | Gross-up dividend | Add to assessable income | Franking credit is both income and tax offset |
| ATO REFUND, TAX REFUND | EXCLUDE | Not income | Prior year tax refund |
| CENTRELINK, JOBSEEKER, YOUTH ALLOWANCE | Government payment (Item 6) | May be taxable | Check specific payment type |
| SUPERANNUATION (lump sum or pension) | Item 7 or 8 | Check | Depends on age and components |
| OWN TRANSFER, SAVINGS | EXCLUDE | Internal | Between own accounts |
| RENTAL INCOME | Rental income (Item 21) | NOT business income | Separate rental schedule |

### 3.2 Expense Patterns (Debits on Bank Statement)

| Pattern | Deduction Category | Tier | Treatment |
|---|---|---|---|
| RENT, OFFICE RENT, SERVICED OFFICE | Business expense -- occupancy | T1 | Fully deductible if dedicated business premises |
| HOME OFFICE, WORK FROM HOME | Home office deduction (D5) | T2 | Fixed rate 67c/hr OR actual cost method. See Tier 2. |
| PETROL, FUEL, CALTEX, BP, SHELL, AMPOL | Motor vehicle (D1) | T2 | Cents/km (88c, max 5,000 km) OR logbook method |
| CAR INSURANCE, REGO, SERVICE | Motor vehicle | T2 | Only under logbook method (not cents/km) |
| TOLL, CITYLINK, LINKT | Motor vehicle or travel | T1 | Business travel tolls: deductible under either method |
| FLIGHT, QANTAS, VIRGIN, JETSTAR | Travel (D2) | T1 | Fully deductible if business travel |
| ACCOMMODATION, HOTEL | Travel | T1 | Deductible if business travel with overnight stay |
| MEALS (business travel, overnight) | Travel | T1 | Reasonable amount while travelling overnight |
| MEALS (client entertainment) | NOT deductible | T1 | Entertainment: NOT deductible for sole traders |
| INSURANCE, PROFESSIONAL INDEMNITY | Business expense -- insurance | T1 | Fully deductible |
| INCOME PROTECTION INSURANCE | Deduction (D15) | T1 | Fully deductible (personal deduction, not business) |
| ACCOUNTING, TAX AGENT, BAS AGENT | Cost of managing tax affairs (D10) | T1 | Fully deductible |
| OFFICE SUPPLIES, OFFICEWORKS | Business expense | T1 | Fully deductible |
| SOFTWARE, SUBSCRIPTION, XERO, MYOB | Business expense -- IT | T1 | Fully deductible |
| GOOGLE ADS, META ADS, FACEBOOK ADS | Business expense -- advertising | T1 | Fully deductible |
| PHONE, TELSTRA, OPTUS, VODAFONE | Business expense -- telecom | T2 | Business portion only |
| INTERNET, NBN | Business expense -- telecom | T2 | Business portion only (or included in home office 67c rate) |
| TRAINING, COURSE, SELF-EDUCATION | Self-education (D4) | T1 | Deductible if directly related to current income-producing activity. NOT deductible if for new career. |
| COMPUTER, LAPTOP, EQUIPMENT (under $20,000) | Instant asset write-off | T1 | Immediately deductible if small business entity and cost < $20,000 |
| COMPUTER, LAPTOP, EQUIPMENT (over $20,000) | Depreciation (D2 business) | T1 | Depreciate over effective life per ATO table |
| SUPER CONTRIBUTION, SUNSUPER, AUSTRALIAN SUPER | Deduction (Item D12) | T1 | Personal deductible super contribution up to $30,000 concessional cap. Must lodge notice of intent. |
| ATO TAX, INCOME TAX, PAYG INSTALMENT | EXCLUDE | Not deductible | Tax payments are not deductions |
| GST PAYMENT, BAS PAYMENT | EXCLUDE from income tax | T1 | GST is separate. Report net of GST if registered. |
| PRIVATE HEALTH, MEDIBANK, BUPA, NIB, HCF | NOT a deduction (but affects MLS) | T1 | Private health insurance is NOT tax deductible. But having it avoids Medicare Levy Surcharge. PHI rebate claimed separately. |
| PERSONAL, GROCERY, ENTERTAINMENT | EXCLUDE | Not deductible | Personal expenses |
| DONATION, CHARITY, DGR | Tax offset (Item D9) | T1 | Deductible if to a deductible gift recipient (DGR). Must be $2+ and genuinely a gift. |

### 3.3 SaaS Subscriptions

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE | Fully deductible business expense | Operating expense |
| SLACK, ZOOM, NOTION, FIGMA, GITHUB | Fully deductible | Same |
| AWS, HEROKU, DIGITAL OCEAN | Fully deductible | Hosting costs |
| CANVA (AU entity) | Fully deductible | Australian company |
| XERO, MYOB | Fully deductible (cost of managing tax affairs or business expense) | Accounting software |
| SPOTIFY, NETFLIX | NOT deductible | Personal entertainment |

### 3.4 Internal Transfers and Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFER, SAVINGS, TERM DEPOSIT | EXCLUDE | Internal movement |
| MORTGAGE, HOME LOAN | EXCLUDE (or home office %) | Personal. Home office actual costs method only. |
| ATM, CASH | T2 -- ask | Default exclude |
| HECS REPAYMENT, HELP | NOT a deduction | Compulsory repayment is not a tax deduction |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Sole Trader (Graphic Designer)

**Input:** ABN income AUD 92,000. Business expenses: software AUD 3,600, advertising AUD 1,200, accounting AUD 1,100, office supplies AUD 800. Home office 1,200 hours at 67c/hr. Car 4,000 business km at 88c/km. No other income. No HELP debt. Has PHI.

**Computation:**
- Business income: AUD 92,000
- Expenses: 3,600 + 1,200 + 1,100 + 800 = AUD 6,700
- Home office: 1,200 x 0.67 = AUD 804
- Motor vehicle: 4,000 x 0.88 = AUD 3,520
- Total deductions: 6,700 + 804 + 3,520 = AUD 11,024
- Taxable income: 92,000 - 11,024 = AUD 80,976
- Tax: 0 + 4,288 + (80,976 - 45,000) x 30% = 4,288 + 10,793 = AUD 15,081
- Medicare: 80,976 x 2% = AUD 1,620
- LITO: $0 (income > $66,667)
- SBITO: 16% x (tax attributable to business income) -- business is 100% of income, so 16% x 15,081 = 2,413, capped at AUD 1,000
- Final tax: 15,081 + 1,620 - 1,000 = AUD 15,701

### Example 2 -- Instant Asset Write-Off

**Input:** Small business entity (turnover < $10M). Purchases laptop AUD 2,800 and monitor AUD 950. Both under $20,000.

**Classification:** Both items are immediately deductible under the instant asset write-off. Total deduction: AUD 3,750 in the year of purchase. No depreciation schedule needed.

### Example 3 -- Motor Vehicle (Logbook vs Cents/Km)

**Input:** Total km: 20,000. Business km: 12,000 (60%). Car costs: fuel AUD 4,800, insurance AUD 1,600, rego AUD 800, service AUD 1,200, depreciation AUD 4,000. Total AUD 12,400.

**Computation:**
- Cents/km: min(12,000, 5,000) x $0.88 = AUD 4,400 (capped at 5,000 km)
- Logbook: 12,400 x 60% = AUD 7,440
- Logbook method is significantly more beneficial. But requires a valid logbook kept for a continuous 12-week period.
- [T2] Flag: confirm logbook exists and is valid.

### Example 4 -- Home Office (Fixed Rate vs Actual)

**Input:** Works from home 1,600 hours/year. Dedicated office in 3-bedroom house (1/4 area). Electricity AUD 2,400, internet AUD 1,200, phone AUD 960 (80% business), depreciation on furniture AUD 400.

**Computation:**
- Fixed rate: 1,600 x $0.67 = AUD 1,072 (covers electricity, gas, phone, internet, stationery, depreciation of furniture)
- Actual cost: electricity 1/4 x AUD 2,400 = AUD 600. Internet 80% x AUD 1,200 = AUD 960. Phone 80% x AUD 960 = AUD 768. Depreciation AUD 400. Total = AUD 2,728.
- Actual method is significantly better here.
- Under fixed rate: only computer/printer depreciation and occupancy expenses (rent, mortgage interest, rates, insurance) can be claimed additionally. Under actual: each item claimed individually.
- [T2] Flag: confirm method choice and occupancy costs if actual.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Business Income [T1]

**Legislation:** ITAA 1997 Div 6

All amounts derived from carrying on a business. If GST-registered, report net of GST. If not registered, report gross.

### 5.2 General Deduction [T1]

**Legislation:** ITAA 1997 s8-1

A deduction for any loss or outgoing to the extent it is incurred in gaining or producing assessable income, or necessarily incurred in carrying on a business. Must not be private, domestic, or capital in nature.

### 5.3 Depreciation [T1]

**Legislation:** ITAA 1997 Div 40

| Method | Calculation |
|---|---|
| Diminishing value | Base value x (days held / 365) x (200% / effective life) |
| Prime cost (straight line) | Cost x (days held / 365) x (100% / effective life) |

Small business entity (turnover < $10M): can use simplified depreciation -- pool all assets over $20,000 at 15% first year, 30% thereafter.

**Instant asset write-off:** Assets costing less than $20,000 (2024-25) can be immediately deducted by small business entities. This threshold may change each year -- confirm for current year.

### 5.4 Superannuation [T1]

Personal deductible contributions up to $30,000 concessional cap (combined with employer contributions if also employed). Must lodge a valid "Notice of intent to claim" with the super fund AND receive acknowledgment BEFORE lodging the tax return or rolling over.

### 5.5 HELP/HECS Repayment [T1]

| Repayment Income (2024-25) | Rate |
|---|---|
| Below $54,435 | 0% |
| $54,435 -- $62,850 | 1% |
| $62,851 -- $66,620 | 2% |
| $66,621 -- $70,618 | 2.5% |
| ... (progressive to) | ... |
| $151,201+ | 10% |

Repayment income = taxable income + reportable fringe benefits + net investment losses + reportable super. HELP repayments are NOT deductible.

### 5.6 Filing and Penalties [T1]

| Item | Value |
|---|---|
| Self-lodge deadline | 31 October 2025 |
| Tax agent deadline | Varies (typically March-May 2026) |
| Failure to lodge on time | $313 per 28-day period, up to 5 periods ($1,565 max) |
| Shortfall penalty (reasonable care not taken) | 25% of shortfall |
| Shortfall penalty (recklessness) | 50% of shortfall |
| General Interest Charge (GIC) | ~11% annually (varies quarterly) |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office [T2]

**Two methods (from 1 July 2022):**

| Method | What It Covers | Additional Claims |
|---|---|---|
| Fixed rate (67c/hr) | Electricity, gas, phone, internet, stationery, computer/printer ink | Separately claim: technology depreciation (computer, monitor), occupancy costs (if dedicated room), cleaning |
| Actual cost | Each expense claimed individually at actual business % | No fixed rate component |

Under either method: must have records of hours worked from home. Fixed rate: can use any reasonable record. Actual: need receipts and usage records.

Occupancy expenses (rent, mortgage interest, rates, home insurance, land tax) are ONLY deductible if you have a dedicated area set aside exclusively as a place of business. These are separate from running expenses.

**Flag for reviewer:** Confirm method, hours, and whether occupancy expenses apply.

### 6.2 Motor Vehicle [T2]

| Method | How It Works | Records |
|---|---|---|
| Cents per km (88c) | Max 5,000 business km. No receipts needed. | Reasonable estimate of business km |
| Logbook | Business % of actual costs including depreciation | 12-week continuous logbook, valid for 5 years |

Cannot claim both. Parking, tolls, and roadside assistance are separate and deductible under either method for business trips.

**Flag for reviewer:** Confirm method and km/logbook records.

### 6.3 Private Health Insurance (Medicare Levy Surcharge) [T2]

If income over $93,000 (single) and no appropriate private hospital cover, Medicare levy surcharge applies:

| Income | MLS Rate |
|---|---|
| $93,001 -- $108,000 | 1% |
| $108,001 -- $144,000 | 1.25% |
| $144,001+ | 1.5% |

PHI rebate: income-tested offset that reduces PHI premiums. Claimed via reduced premiums or tax offset.

**Flag for reviewer:** Confirm PHI status and income level.

### 6.4 Personal Services Income (PSI) [T2]

If income is mainly a reward for personal efforts/skills and not from conducting a personal services business, PSI rules limit deductions. Cannot claim rent, mortgage interest, certain home office costs against PSI.

**Flag for reviewer:** Confirm whether PSI rules apply (results test, unrelated clients test, employment test, business premises test).

---

## Section 7 -- Excel Working Paper Template

```
AUSTRALIAN INDIVIDUAL TAX RETURN -- Working Paper
Tax Year: 2024-25

A. INCOME
  A1. Business income (ABN income)                 ___________
  A2. Employment income (per income statement)     ___________
  A3. Interest income                              ___________
  A4. Dividend income (grossed up with franking)   ___________
  A5. Rental income (net)                          ___________
  A6. Other income                                 ___________
  A7. TOTAL ASSESSABLE INCOME                      ___________

B. DEDUCTIONS
  B1. Business expenses (direct)                   ___________
  B2. Home office (67c/hr or actual)               ___________
  B3. Motor vehicle (88c/km or logbook)            ___________
  B4. Travel (flights, accommodation)              ___________
  B5. Self-education                               ___________
  B6. Depreciation / instant asset write-off       ___________
  B7. Personal super contributions                 ___________
  B8. Income protection insurance                  ___________
  B9. Cost of managing tax affairs                 ___________
  B10. Donations (DGR)                             ___________
  B11. Other deductions                            ___________
  B12. TOTAL DEDUCTIONS                            ___________

C. TAXABLE INCOME (A7 - B12)                       ___________

D. TAX COMPUTATION
  D1. Tax on taxable income (Stage 3 rates)        ___________
  D2. Medicare levy (2%)                           ___________
  D3. Medicare levy surcharge (if applicable)      ___________
  D4. HELP/HECS repayment (if applicable)          ___________
  D5. Gross tax                                    ___________
  D6. Less: LITO                                   ___________
  D7. Less: SBITO (16%, max $1,000)                ___________
  D8. Less: Franking credits offset                ___________
  D9. Less: PHI rebate offset                      ___________
  D10. Less: PAYG instalments paid                 ___________
  D11. Less: PAYG withholding (employment)         ___________
  D12. TAX DUE / (REFUND)                          ___________

REVIEWER FLAGS:
  [ ] Residency status confirmed?
  [ ] Home office method and hours verified?
  [ ] Motor vehicle method confirmed?
  [ ] Instant asset write-off eligibility (SBE < $10M)?
  [ ] Super contribution notice of intent lodged?
  [ ] PHI status confirmed (MLS)?
  [ ] HELP debt status confirmed?
  [ ] All T2 items flagged?
```

---

## Section 8 -- Bank Statement Reading Guide

### Australian Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| CBA, ANZ, Westpac, NAB | CSV, PDF | Date, Description, Debit, Credit, Balance |
| Macquarie, Suncorp, Bendigo | CSV | Date, Narrative, Amount |
| Up, ING, Ubank | CSV | Date, Description, Amount |
| Wise, Revolut | CSV | Date, Description, Amount, Currency |

### Key Australian Banking Terms

| Term | Classification Hint |
|---|---|
| Direct Credit | Incoming payment -- could be income |
| Direct Debit | Regular outgoing -- likely expense |
| EFTPOS | Point-of-sale purchase |
| BPAY | Bill payment |
| Osko / PayID | Fast payment -- check direction |
| ATM | Cash withdrawal -- ask purpose |
| Interest Paid | Income -- report separately |
| Dividend | Income -- check franking |

---

## Section 9 -- Onboarding Fallback

```
ONBOARDING QUESTIONS -- AUSTRALIA INDIVIDUAL RETURN
1. Are you an Australian resident for tax purposes?
2. Do you have an active ABN and TFN?
3. Are you registered for GST?
4. What is your aggregated turnover? (for small business concessions)
5. Do you work from home? How many hours per year? Method preference (67c or actual)?
6. Do you use a vehicle for business? Method preference (cents/km or logbook)?
7. Any assets purchased this year? Cost?
8. Do you have private health insurance? Full year?
9. Do you have a HELP/HECS debt?
10. Are you also employed (PAYG income)?
11. Any personal super contributions made?
12. Prior year tax return / depreciation schedule available?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Assessable income | ITAA 1997 s6-1, s6-5 |
| General deduction | ITAA 1997 s8-1 |
| Capital vs revenue | ITAA 1997 s8-1(2)(a) |
| Depreciation | ITAA 1997 Div 40 |
| Small business entity | ITAA 1997 Div 328 |
| Instant asset write-off | ITAA 1997 s328-180 |
| Home office | ATO Practical Compliance Guideline PCG 2023/1 |
| Motor vehicle | ITAA 1997 s28-13, s28-15 |
| Superannuation deduction | ITAA 1997 Div 290 |
| Medicare levy | Medicare Levy Act 1986 |
| HELP repayments | Higher Education Support Act 2003 |
| LITO | ITAA 1997 s61-1 |
| SBITO | ITAA 1997 s328-375 |

### Interaction with GST [T1]

| Scenario | Income Tax Treatment |
|---|---|
| GST collected on sales (registered) | NOT income. Report net of GST. |
| GST credits (ITC) recovered | NOT an expense. Report net of GST. |
| Not registered for GST | GST paid on purchases IS part of the cost. Report gross. |
| GST on private portion | Non-claimable GST is part of cost. |

---

## PROHIBITIONS

- NEVER allow private or domestic expenses as business deductions
- NEVER allow entertainment expenses for sole traders (not deductible)
- NEVER claim more than 5,000 km under the cents-per-km method
- NEVER claim occupancy expenses (rent, mortgage interest) for home office unless dedicated area exclusively for business
- NEVER forget to lodge notice of intent for personal super contributions
- NEVER claim HELP repayments as a deduction
- NEVER claim private health insurance premiums as a deduction
- NEVER apply the instant asset write-off without confirming small business entity status
- NEVER include income tax or GST payments as business deductions
- NEVER report GST-inclusive amounts if GST-registered
- NEVER present tax calculations as definitive -- always label as estimated

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, CA, or registered tax agent in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
