---
name: ng-income-tax
description: Use this skill whenever asked about Nigerian personal income tax for self-employed individuals (sole proprietors / freelancers). Trigger on phrases like "Nigeria income tax", "PITA", "NRS", "FIRS", "self-assessment Nigeria", "progressive tax Nigeria", "minimum tax Nigeria", "consolidated relief", "CRA Nigeria", "TIN Nigeria", "WHT Nigeria", "income tax Lagos", "income tax Abuja", "state IRS", or any question about computing or filing income tax for a self-employed person in Nigeria. This skill covers for 2026 the Nigeria Tax Act 2025 bands (0-25%) and rent relief, and for earlier years the old progressive rates (7-24%), minimum tax and consolidated relief allowance, capital allowances, withholding tax credits, self-assessment filing, and FIRS/state IRS requirements. ALWAYS read this skill before touching any Nigerian income tax work.
version: 2.1
jurisdiction: NG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NG Income Tax

Tax year 2026. Unofficial-source warning: see Status columns and "Not yet confirmed".

## Who this applies to

Self-employed individuals, sole proprietors and partners in Nigeria for 2026 and later years of assessment. All NTA figures below are read from an unofficial copy and stay marked unverified until confirmed in an official document. "NTA" means the Nigeria Tax Act 2025, in force 1 January 2026 (commencement line of the Act).

A resident individual is one who, in the year, is domiciled in Nigeria, has a permanent place available for domestic use, has a habitual abode, has substantial economic and immediate family ties, stays at least 183 days in a 12-month period, or serves as a Nigerian diplomat abroad (NTA, definition of resident individual). Any one limb is enough. An individual earning the national minimum wage is outside the rate table (NTA s.58). For 2025 and earlier see the pre-2026 section.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Law | Status and link |
|---|---|---|---|---|
| Band 1, first NGN 800,000 | 0% | 2026 | NTA s.58, Fourth Schedule (a) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 2, next NGN 2,200,000 | 15% | 2026 | Fourth Schedule (b) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 3, next NGN 9,000,000 | 18% | 2026 | Fourth Schedule (c) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 4, next NGN 13,000,000 | 21% | 2026 | Fourth Schedule (d) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 5, next NGN 25,000,000 | 23% | 2026 | Fourth Schedule (e) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 6, above NGN 50,000,000 | 25% | 2026 | Fourth Schedule (f) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Rent relief, on declared actual rent | 20% of annual rent, maximum NGN 500,000 | 2026 | NTA s.30(2)(a)(vi) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |

## The base

Chargeable income is total income under NTA s.28 less eligible deductions (s.30(1)). Total income includes chargeable gains (s.28(2)(a)(v)) and is after capital allowances (s.28(2)(b)(ii)). Eligible deductions (s.30(2)(a)): National Housing Fund, National Health Insurance Scheme and Pension Reform Act contributions, interest on loans for an owner-occupied house, life insurance or deferred annuity premiums paid in the preceding year, and rent relief. A deduction must be claimed in writing (s.31).

The consolidated relief allowance and the 1% minimum tax of the old Personal Income Tax Act are not in the NTA provisions read for individuals; that Act is repealed (s.195). Do not apply them to 2026.

Losses from a trade carry forward against the same trade profits until recouped; digital asset losses only offset digital asset gains (s.28(3)). If records cannot support an assessment, a presumptive regime applies on regulation terms (s.29).

## Deadlines and filing

Dates and forms sit in the Nigeria Tax Administration Act 2025, which we did not open. Do not state a 2026 date from this skill. Ask which state revenue service the client files with, and check its current notice.

## Penalties and interest

Set by the Nigeria Tax Administration Act 2025, not read. See "Not yet confirmed".

## Cross-border points

Foreign employment rules sit in a schedule to the NTA that was not read in full for this update. Refer non-residents and foreign employment cases to a reviewer.

## Two worked examples that recompute

Simple: profit after expenses NGN 5,000,000, rent paid NGN 2,000,000, no other deductions. Rent relief NGN 400,000. Chargeable income NGN 4,600,000. Tax NGN 618,000.

```oa-check
name: Freelancer, profit NGN 5,000,000, rent NGN 2,000,000
inputs:
  profit: 5000000
  rent: 2000000
steps:
  - relief: min(rent * 0.2, 500000)
  - t: profit - relief
  - b2: (min(t, 3000000) - 800000) * 0.15
  - b3: max(min(t, 12000000) - 3000000, 0) * 0.18
  - b4: max(min(t, 25000000) - 12000000, 0) * 0.21
  - b5: max(min(t, 50000000) - 25000000, 0) * 0.23
  - tax: b2 + b3 + b4 + b5
expected:
  tax: 618000.00
```

Decision, should a sole trader with NGN 60,000,000 profit claim rent relief at the cap? Rent NGN 3,000,000 gives relief of NGN 500,000 (20% would be NGN 600,000, so the cap bites). At that level the top band is 25%, so the relief saves NGN 125,000. Tax without it is NGN 12,930,000; with it, NGN 12,805,000.

```oa-check
name: Rent relief at the cap, income above NGN 50,000,000
inputs:
  income: 60000000
  rent: 3000000
steps:
  - relief: min(rent * 0.2, 500000)
  - t: income - relief
  - b2: (min(t, 3000000) - 800000) * 0.15
  - b3: max(min(t, 12000000) - 3000000, 0) * 0.18
  - b4: max(min(t, 25000000) - 12000000, 0) * 0.21
  - b5: max(min(t, 50000000) - 25000000, 0) * 0.23
  - tax: b2 + b3 + b4 + b5
  - tax6: tax + (t - 50000000) * 0.25
expected:
  tax6: 12805000.00
```

## Ask the client first

1. Which year of assessment is this? 2025 or earlier uses the pre-2026 section.
2. Resident in Nigeria under any limb, and in which state?
3. Business profit, and other income?
4. Rent actually paid, and can it be declared?
5. Pension, housing fund, health and life contributions?
6. Any digital asset losses or foreign employment?

## Pre-2026 law (years of assessment to 2025)

This section keeps the earlier text so nothing is lost. It applies to years of assessment up to 2025, under the Acts repealed by NTA s.195 from 1 January 2026 (Personal Income Tax Act, Companies Income Tax Act, Capital Gains Tax Act, Value Added Tax Act and others). It was not re-read against those Acts in this update. Do not use it for 2026. Where it differs from the sections above, the sections above govern 2026 and later.



#### Nigerian Personal Income Tax: Self-Employed / Sole Proprietor (PITA) v2.0

#### Section 1: Quick Reference

##### Progressive Tax Rates (PITA, Sixth Schedule)

**Progressive Tax Rates (PITA, Sixth Schedule)**

| Taxable Income (NGN) | Rate | Status |
| --- | --- | --- |
| First 300,000 | 7% | unverified, earlier text not re-read |
| Next 300,000 (300,001 -- 600,000) | 11% | unverified, earlier text not re-read |
| Next 500,000 (600,001 -- 1,100,000) | 15% | unverified, earlier text not re-read |
| Next 500,000 (1,100,001 -- 1,600,000) | 19% | unverified, earlier text not re-read |
| Next 1,600,000 (1,600,001 -- 3,200,000) | 21% | unverified, earlier text not re-read |
| Above 3,200,000 | 24% | unverified, earlier text not re-read |

##### Consolidated Relief Allowance (CRA)

- **CRA formula**: CRA = max(NGN 200,000, 1% x Gross Income) + 20% x Gross Income

The CRA replaced the previous personal allowance / children's allowance system from 2020.

##### Minimum Tax

**Minimum Tax**

| Rule | Detail | Status |
| --- | --- | --- |
| Rate | 1% of gross income | unverified, earlier text not re-read |
| When it applies | When computed tax (per progressive rates) is LESS than minimum tax | unverified, earlier text not re-read |
| Effect | Taxpayer pays the HIGHER of computed tax or minimum tax | unverified, earlier text not re-read |

##### Capital Allowances (PITA, Fifth Schedule)

**Capital Allowances (PITA, Fifth Schedule)**

| Asset | Initial Allowance | Annual Allowance | Status |
| --- | --- | --- | --- |
| Building (industrial) | 15% | 10% | unverified, earlier text not re-read |
| Motor vehicles | 50% | 25% | unverified, earlier text not re-read |
| Plant and machinery | 50% | 25% | unverified, earlier text not re-read |
| Furniture and fittings | 25% | 20% | unverified, earlier text not re-read |
| Computer equipment | 50% | 25% | unverified, earlier text not re-read |

##### Computation Structure

**Computation Structure**

| Step | Description | Status |
| --- | --- | --- |
| A | Gross income from business | unverified, earlier text not re-read |
| B | Less: Allowable business deductions | unverified, earlier text not re-read |
| C | Assessable income (A minus B) | unverified, earlier text not re-read |
| D | Add: Other income (investment, rental, etc.) | unverified, earlier text not re-read |
| E | Gross total income (C plus D) | unverified, earlier text not re-read |
| F | Less: Consolidated Relief Allowance | unverified, earlier text not re-read |
| G | Less: Other reliefs (pension, NHF, life insurance) | unverified, earlier text not re-read |
| H | Taxable income (E minus F minus G) | unverified, earlier text not re-read |
| I | Tax per progressive rate table | unverified, earlier text not re-read |
| J | Compare with minimum tax (1% of gross) | unverified, earlier text not re-read |
| K | Tax payable (higher of I and J) | unverified, earlier text not re-read |
| L | Less: WHT credits | unverified, earlier text not re-read |
| M | Tax due / (refund) | unverified, earlier text not re-read |

##### Other Reliefs (PITA, s 33)

**Other Reliefs (PITA, s 33)**  _(PITA, s 33)_

| Relief | Amount / Rule | Status |
| --- | --- | --- |
| Pension contribution | Actual contribution to approved scheme (min 8% of basic + housing + transport) | unverified, earlier text not re-read |
| National Housing Fund | 2.5% of basic salary (voluntary for self-employed) | unverified, earlier text not re-read |
| Life insurance premium | Actual premium paid | unverified, earlier text not re-read |
| National Health Insurance | Actual premium paid | unverified, earlier text not re-read |

##### Conservative Defaults

**Conservative Defaults**

| Situation | Default Assumption | Status |
| --- | --- | --- |
| Residency unknown | STOP: non-residents taxed differently | unverified, earlier text not re-read |
| State of residence unknown | STOP: determines filing authority | unverified, earlier text not re-read |
| CRA computed on net income | WRONG: CRA is on GROSS income | unverified, earlier text not re-read |
| Capital expenditure directly deducted | WRONG: use capital allowances | unverified, earlier text not re-read |
| WHT certificate missing | Do NOT credit without certificate | unverified, earlier text not re-read |
| Minimum tax not checked | ALWAYS compare computed tax vs 1% of gross | unverified, earlier text not re-read |
| Filing authority unclear | FIRS for FCT (Abuja); state IRS for all others | unverified, earlier text not re-read |

##### Red Flag Thresholds

**Red Flag Thresholds**

| Flag | Threshold | Status |
| --- | --- | --- |
| Computed tax = 0 but minimum tax > 0 | Minimum tax applies | unverified, earlier text not re-read |
| No WHT certificates from clients | Cannot credit without certificates | unverified, earlier text not re-read |
| Expenses close to income (high ratio) | Minimum tax likely applies | unverified, earlier text not re-read |
| Multiple state operations | Verify correct filing authority | unverified, earlier text not re-read |
| Capital expenditure directly expensed | Must use capital allowance schedule | unverified, earlier text not re-read |

#### Section 2: Required Inputs + Refusal Catalogue

##### Required Inputs

1. **Residency status**: resident vs non-resident
2. **State of residence**: determines FIRS (FCT) or state IRS
3. **Gross income from self-employment**: total business receipts
4. **Business expenses**: nature, amount, and documentation
5. **Other income**: employment, investment, rental
6. **Life insurance and pension contributions**: for relief computation
7. **National Housing Fund contributions**: if applicable
8. **TIN**: Tax Identification Number
9. **WHT certificates**: from clients who withheld tax
10. **Bank statements**: 12 months (calendar year)
11. **Capital assets purchased**: for capital allowance computation

##### Refusal Catalogue

- **R-NG-1**: Non-resident earning Nigeria-source income  _(Stop: WHT as final tax (10% on professional services); different rules)_
- **R-NG-2**: Residency unknown  _(Stop: different treatment)_
- **R-NG-3**: State of residence unknown  _(Stop: determines filing authority)_
- **R-NG-4**: Capital expenditure claimed as expense  _(Reject: must use capital allowance schedule)_
- **R-NG-5**: Old personal allowance / children's allowance system  _(Stop: replaced by CRA from 2020)_
- **R-NG-6**: Petroleum profits tax  _(Escalate: separate regime)_

#### Section 3: Transaction Pattern Library

##### 3.1 Income Patterns

**3.1 Income Patterns**

| # | Narration Pattern | Tax Line | Notes | Status |
| --- | --- | --- | --- | --- |
| I-01 | `TRANSFER FROM [client]` / `NIP CR [client]` | Gross income: PITA taxable | Standard NIP (NIBSS Instant Payment) transfer from client | unverified, earlier text not re-read |
| I-02 | `USSD CREDIT` / `*737 CREDIT` | Gross income: PITA taxable | USSD banking credit from client | unverified, earlier text not re-read |
| I-03 | `POS SETTLEMENT` / `CARD COLLECTION` | Gross income: gross-up | POS terminal settlement | unverified, earlier text not re-read |
| I-04 | `PAYSTACK PAYOUT` / `PAYSTACK SETTLEMENT` | Gross income: gross-up | Paystack (Nigerian payment processor) payout | unverified, earlier text not re-read |
| I-05 | `FLUTTERWAVE PAYOUT` / `FLUTTERWAVE SETTLEMENT` | Gross income: gross-up | Flutterwave settlement | unverified, earlier text not re-read |
| I-06 | `STRIPE PAYOUT NGN` | Gross income: gross-up or foreign | Stripe payout; classify by payer country | unverified, earlier text not re-read |
| I-07 | `PAYPAL TRANSFER` / `PAYPAL WITHDRAWAL` | Gross income: foreign source likely | PayPal; flag for FX conversion | unverified, earlier text not re-read |
| I-08 | `PAYONEER DEPOSIT` | Gross income: foreign source | Payoneer settlement | unverified, earlier text not re-read |
| I-09 | `OPAY RECEIVED` / `PALMPAY RECEIVED` | Gross income: PITA taxable | Mobile money / fintech receipt | unverified, earlier text not re-read |
| I-10 | `TAX REFUND FIRS` / `REFUND SIRS` | NOT income: tax refund | Refund from tax authority | unverified, earlier text not re-read |
| I-11 | `INTEREST EARNED` / `SAVINGS INTEREST` | Investment income | Add to gross total income | unverified, earlier text not re-read |
| I-12 | `RENTAL INCOME` / `RENT RECEIVED` | Rental income | Add to gross total income | unverified, earlier text not re-read |
| I-13 | `WHT DEDUCTED` (annotation on payment) | WHT credit: not income reduction | Credit against final tax; require certificate | unverified, earlier text not re-read |

##### 3.2 Expense Patterns

**3.2 Expense Patterns**

| # | Narration Pattern | Tax Line | Notes | Status |
| --- | --- | --- | --- | --- |
| E-01 | `OFFICE RENT` / `RENT PAYMENT [landlord]` | Rent: fully deductible | Require receipt/invoice | unverified, earlier text not re-read |
| E-02 | `EKEDC` / `IKEDC` / `AEDC` / `BEDC` / `PHED` / `KAEDCO` | Electricity: deductible (business proportion) | Distribution company payment | unverified, earlier text not re-read |
| E-03 | `MTN` / `AIRTEL` / `GLO` / `9MOBILE` | Phone/internet: deductible (business %) | Telecom provider | unverified, earlier text not re-read |
| E-04 | `SPECTRANET` / `SMILE` / `IPNX` / `SWIFT NETWORK` | Internet: deductible (business %) | ISP provider | unverified, earlier text not re-read |
| E-05 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software: fully deductible | Professional tools | unverified, earlier text not re-read |
| E-06 | `ACCOUNTANT` / `AUDIT FEE` / `TAX CONSULTANT` | Professional fees: fully deductible |  | unverified, earlier text not re-read |
| E-07 | `ARIK AIR` / `AIR PEACE` / `DANA AIR` / `IBOM AIR` | Air travel: deductible (business purpose) | Document purpose | unverified, earlier text not re-read |
| E-08 | `HOTEL` / `BOOKING.COM` / `AIRBNB` | Accommodation: deductible (business travel) | Business purpose | unverified, earlier text not re-read |
| E-09 | `PENSION CONTRIBUTION` / `RSA [fund name]` | Pension: relief deduction | Approved pension scheme contribution | unverified, earlier text not re-read |
| E-10 | `NHF` / `NATIONAL HOUSING FUND` | NHF: relief deduction | If applicable | unverified, earlier text not re-read |
| E-11 | `LIFE INSURANCE` / `PREMIUM PAYMENT` | Life insurance: relief deduction | Own life insurance | unverified, earlier text not re-read |
| E-12 | `NHIS` / `HEALTH INSURANCE` | Health insurance: relief deduction | National/private health | unverified, earlier text not re-read |
| E-13 | `TAX PAYMENT FIRS` / `SIRS PAYMENT` | Tax payment: NOT deductible | Payment of tax liability | unverified, earlier text not re-read |
| E-14 | `FUEL` / `PETROL` / `DIESEL` / `TOTAL` / `OANDO` / `CONOIL` | Fuel: deductible (business proportion) | Document business use | unverified, earlier text not re-read |
| E-15 | `OFFICE SUPPLIES` / `STATIONERY` | Supplies: fully deductible |  | unverified, earlier text not re-read |
| E-16 | `MARKETING` / `GOOGLE ADS` / `META ADS` / `ADVERTISING` | Marketing: fully deductible |  | unverified, earlier text not re-read |
| E-17 | `STAFF SALARY` / `PAYROLL` | Staff costs: fully deductible | Include PAYE obligations for staff | unverified, earlier text not re-read |
| E-18 | `TRAINING` / `COURSE` / `CERTIFICATION` | Training: fully deductible | Professional development | unverified, earlier text not re-read |
| E-19 | `GENERATOR FUEL` / `DIESEL GEN` | Generator fuel: deductible (business %) | Common in Nigeria due to power supply | unverified, earlier text not re-read |

##### 3.3 Nigerian Bank Fees (Deductible)

**3.3 Nigerian Bank Fees (Deductible)**

| Pattern | Treatment | Notes | Status |
| --- | --- | --- | --- |
| GTBANK, GUARANTY TRUST | Deductible for business account fees | Now GTCo | unverified, earlier text not re-read |
| ACCESS BANK | Deductible for business account fees | Merged with Diamond Bank | unverified, earlier text not re-read |
| ZENITH BANK | Deductible for business account fees |  | unverified, earlier text not re-read |
| UBA, UNITED BANK FOR AFRICA | Deductible for business account fees |  | unverified, earlier text not re-read |
| FIRST BANK, FBN | Deductible for business account fees |  | unverified, earlier text not re-read |
| STANBIC IBTC | Deductible for business account fees |  | unverified, earlier text not re-read |
| FCMB, FIRST CITY MONUMENT | Deductible for business account fees |  | unverified, earlier text not re-read |
| FIDELITY BANK | Deductible for business account fees |  | unverified, earlier text not re-read |
| STERLING BANK | Deductible for business account fees |  | unverified, earlier text not re-read |
| WEMA BANK / ALAT | Deductible for business account fees |  | unverified, earlier text not re-read |
| KUDA BANK, OPAY, PALMPAY, MONIEPOINT | Deductible for business account fees | Fintech/digital banks | unverified, earlier text not re-read |
| ACCOUNT MAINTENANCE FEE, COT | Deductible | Commission on turnover / maintenance | unverified, earlier text not re-read |
| SMS ALERT FEE, NOTIFICATION FEE | Deductible | Banking notification charges | unverified, earlier text not re-read |
| TRANSFER FEE, NIP FEE | Deductible | Inter-bank transfer fees | unverified, earlier text not re-read |
| STAMP DUTY | EXCLUDE | Government levy on transactions | unverified, earlier text not re-read |

##### 3.4 Government and Statutory (Exclude)

**3.4 Government and Statutory (Exclude)**

| Pattern | Treatment | Notes | Status |
| --- | --- | --- | --- |
| FIRS, FEDERAL INLAND REVENUE | EXCLUDE | Federal tax authority payment | unverified, earlier text not re-read |
| LIRS, LAGOS STATE IRS | EXCLUDE | State tax authority | unverified, earlier text not re-read |
| CAC, CORPORATE AFFAIRS COMMISSION | Deductible | Business registration fee | unverified, earlier text not re-read |
| STAMP DUTY CHARGE | EXCLUDE | Government levy | unverified, earlier text not re-read |

##### 3.5 Internal Transfers and Exclusions

**3.5 Internal Transfers and Exclusions**

| Pattern | Treatment | Notes | Status |
| --- | --- | --- | --- |
| OWN ACCOUNT TRANSFER, SELF TRANSFER | EXCLUDE | Internal movement | unverified, earlier text not re-read |
| ATM WITHDRAWAL | TIER 2: ask | Default exclude; determine purpose | unverified, earlier text not re-read |
| LOAN DISBURSEMENT | EXCLUDE | Loan proceeds, not income | unverified, earlier text not re-read |
| LOAN REPAYMENT | EXCLUDE | Loan principal, out of scope | unverified, earlier text not re-read |

#### Section 4: Worked Examples

##### Example 1: GTBank (Lagos, IT Consultant)

**Bank:** GTBank (Guaranty Trust) statement
**Client:** Chidi Okafor, IT consultant, Lagos

```
Date;Description;Debit;Credit;Balance
05/01/2025;NIP CR FROM TECH CORP LTD;;2,500,000;
15/01/2025;ACCOUNT MAINTENANCE FEE;1,500;;
10/02/2025;NIP CR FROM STARTUP DIGITAL;;1,800,000;
28/02/2025;PENSION RSA CONTRIBUTION;120,000;;
15/03/2025;PAYSTACK SETTLEMENT;;980,000;
01/04/2025;MTN AIRTIME/DATA;25,000;;
20/04/2025;NIP CR FROM GAMMA SOLUTIONS;;3,200,000;
10/07/2025;ACCOUNTANT FEES;150,000;;
10/10/2025;AIR PEACE LAGOS-ABUJA;85,000;;
15/11/2025;WHT DEDUCTED BY TECH CORP;250,000;;
```

**Step 1: Income**

Annualised gross: NGN 8,000,000. WHT deducted by PJ clients: NGN 500,000.

**Step 2: Expenses**

Accounting: NGN 150,000; travel: NGN 85,000; telecom: NGN 300,000; software: NGN 240,000; marketing: NGN 180,000; office rent: NGN 1,200,000; generator fuel: NGN 360,000; other: NGN 485,000. Total: NGN 3,000,000.

**Step 3: Computation**

```
Gross income:             NGN  8,000,000
Less expenses:            NGN  3,000,000
Assessable income:        NGN  5,000,000
Add other income:         NGN          0
Gross total income:       NGN  8,000,000 (for CRA calculation)

CRA: max(200,000, 80,000) + 20% x 8,000,000 = 200,000 + 1,600,000 = NGN 1,800,000
Pension relief:           NGN    120,000

Taxable income: 8,000,000 - 3,000,000 - 1,800,000 - 120,000 = NGN 3,080,000

Tax:
  300,000 x 7%  =   21,000
  300,000 x 11% =   33,000
  500,000 x 15% =   75,000
  500,000 x 19% =   95,000
1,480,000 x 21% =  310,800
Total:              NGN 534,800

Minimum tax: 1% x 8,000,000 = NGN 80,000
Computed tax > minimum → pay NGN 534,800

Less WHT credit: NGN 500,000
Tax due: NGN 34,800
```

##### Example 2: Access Bank (Abuja, Consultant: WHT Heavy)

**Bank:** Access Bank
**Client:** Amina Bello, management consultant, Abuja (FCT: file with FIRS)

Gross: NGN 12,000,000. All from corporate clients with 10% WHT.
WHT suffered: NGN 1,200,000.
After CRA and expenses: tax per rates = NGN 950,000.
Less WHT: NGN 1,200,000.
Result: **refund of NGN 250,000** (WHT > tax). File with FIRS for refund.

##### Example 3: Zenith Bank (Port Harcourt, Physician)

**Bank:** Zenith Bank
**Client:** Dr. Emeka Nwosu, physician, Port Harcourt, Rivers State

Gross: NGN 20,000,000 (hospital fees + private patients).
Expenses: NGN 5,000,000.
CRA: 200,000 + 4,000,000 = NGN 4,200,000.
Pension: NGN 800,000.
Taxable: 20,000,000 - 5,000,000 - 4,200,000 - 800,000 = NGN 10,000,000.

Tax: 21,000 + 33,000 + 75,000 + 95,000 + 336,000 + (10,000,000 - 3,200,000) x 24% = 560,000 + 1,632,000 = **NGN 2,192,000**

File with Rivers State IRS (not FIRS).

##### Example 4: Kuda Bank (Lagos, Freelance Designer: Low Income)

**Bank:** Kuda Bank (digital)
**Client:** Ngozi Eze, freelance designer, Lagos

Gross: NGN 600,000. Expenses: NGN 100,000.
CRA: 200,000 + 120,000 = NGN 320,000.
Taxable: 600,000 - 100,000 - 320,000 = NGN 180,000.
Tax: 7% x 180,000 = NGN 12,600.
Minimum tax: 1% x 600,000 = NGN 6,000.
Pay NGN 12,600 (higher).

##### Example 5: UBA (Lagos, Minimum Tax Scenario)

**Bank:** UBA
**Client:** Tunde Adeyemi, consultant, Lagos

Gross: NGN 10,000,000. Expenses: NGN 9,000,000.
CRA: 200,000 + 2,000,000 = NGN 2,200,000. Pension: NGN 500,000.
Taxable: 10,000,000 - 9,000,000 - 2,200,000 - 500,000 = max(0, -1,700,000) = NGN 0.
Computed tax: NGN 0.
Minimum tax: 1% x 10,000,000 = **NGN 100,000**.
Tax payable: NGN 100,000 (minimum tax applies).

##### Example 6: First Bank (Kano, Multiple Income Sources)

**Bank:** First Bank
**Client:** Ibrahim Musa, accountant, Kano, also earns rental income

Self-employment: NGN 6,000,000. Rental income: NGN 2,400,000.
Total gross: NGN 8,400,000.
CRA on total gross: 200,000 + 1,680,000 = NGN 1,880,000.
All income aggregates. Apply expenses per source. Progressive rates on combined taxable income.
File with Kano State IRS.

#### Section 5: Tier 1 Rules (Apply Directly)

- **T1-NG-1: CRA is computed on GROSS income, not net**: The Consolidated Relief Allowance formula uses gross total income (before expenses), not assessable or taxable income. This is a common error. Always apply CRA to gross.  _(T1-NG-1)_
- **T1-NG-2: Minimum tax is a floor**: Always compare computed tax per progressive rates with 1% of gross income. The taxpayer pays whichever is HIGHER. Minimum tax cannot be avoided by high expenses.  _(T1-NG-2)_
- **T1-NG-3: Capital expenditure must use capital allowances**: Never deduct capital expenditure directly as a business expense. Use the Fifth Schedule rates (initial allowance in year of first use, annual allowance thereafter).  _(T1-NG-3)_
- **T1-NG-4: WHT is a credit, not income reduction**: Withholding tax (10% on professional fees, 5% on contracts) deducted by clients is a credit against final tax. It does not reduce gross income. Must have WHT certificate to claim credit.  _(T1-NG-4)_
- **T1-NG-5: Filing authority depends on state of residence**: FCT (Abuja) residents file with FIRS. All other states file with the State Internal Revenue Service (SIRS). This is not optional.  _(T1-NG-5)_
- **T1-NG-6: Old personal allowance system is abolished**: The pre-2020 system of personal allowance + children's allowance + dependent relative allowance was replaced by CRA. Never apply the old deductions.  _(T1-NG-6)_

#### Section 6: Tier 2 Catalogue (Reviewer Judgement Required)

**Section 6: Tier 2 Catalogue (Reviewer Judgement Required)**

| Code | Situation | Escalation Reason | Suggested Treatment | Status |
| --- | --- | --- | --- | --- |
| T2-NG-1 | Mixed-use vehicle | Business proportion must be documented | Flag: reviewer determines reasonable business-use % | unverified, earlier text not re-read |
| T2-NG-2 | Home office expenses | Proportional deduction for dedicated space | Flag: document proportion and exclusivity | unverified, earlier text not re-read |
| T2-NG-3 | Capital allowance computation for complex assets | Initial vs annual allowance; residual value tracking | Flag: verify asset register and allowance schedule | unverified, earlier text not re-read |
| T2-NG-4 | Multiple state operations | Dual filing obligation possible | Flag: verify correct filing authority for each income source | unverified, earlier text not re-read |
| T2-NG-5 | Foreign income for Nigerian resident | Worldwide income taxable; treaty credits may apply | Escalate: treaty analysis required | unverified, earlier text not re-read |
| T2-NG-6 | Voluntary NHF / NHIS contributions | Relief amounts depend on actual contribution vs statutory basis | Verify contribution receipts and applicable relief limits | unverified, earlier text not re-read |

#### Section 7: Excel Working Paper Template

```
NIGERIAN PITA WORKING PAPER (SELF-EMPLOYED / SOLE PROPRIETOR)
Taxpayer: _______________  TIN: _______________  FY: 2025 (Calendar Year)
State: _______________  Filing Authority: [ ] FIRS (FCT)  [ ] State IRS

SECTION A: GROSS INCOME
                                        NGN
Business receipts:                     ___________
Platform payouts (grossed up):         ___________
Other business income:                 ___________
TOTAL BUSINESS GROSS                   ___________

SECTION B: ALLOWABLE BUSINESS DEDUCTIONS
Office rent:                           ___________
Utilities (business %):                ___________
Telecom (business %):                  ___________
Software:                              ___________
Professional fees:                     ___________
Travel (business purpose):             ___________
Marketing:                             ___________
Staff salaries:                        ___________
Office supplies:                       ___________
Generator fuel (business %):           ___________
Capital allowances:                    ___________
Other deductible:                      ___________
TOTAL DEDUCTIONS                       ___________

SECTION C: ASSESSABLE INCOME
Gross business - deductions            ___________

SECTION D: OTHER INCOME
Investment income:                     ___________
Rental income:                         ___________
Employment income:                     ___________
GROSS TOTAL INCOME                     ___________

SECTION E: RELIEFS
CRA: max(200,000, 1% x Gross) + 20% x Gross  ___________
Pension contribution:                  ___________
NHF:                                   ___________
Life insurance:                        ___________
NHIS:                                  ___________
TOTAL RELIEFS                          ___________

SECTION F: TAXABLE INCOME
Gross total - deductions - reliefs     ___________

SECTION G: TAX COMPUTATION
Tax per progressive rates:             ___________
Minimum tax (1% x gross):             ___________
TAX PAYABLE (higher):                 ___________

SECTION H: CREDITS
WHT suffered (with certificates):      (___________)
TAX DUE / (REFUND)                    ___________

SECTION I: REVIEWER FLAGS
[ ] Residency confirmed (resident)?
[ ] Filing authority confirmed (FIRS or state IRS)?
[ ] CRA computed on GROSS income (not net)?
[ ] Minimum tax compared with computed tax?
[ ] Capital expenditure using capital allowances (not direct deduction)?
[ ] WHT certificates collected for all credits?
[ ] Old personal allowance system NOT applied?
[ ] Generator/fuel expenses documented for business proportion?
[ ] Multiple income sources properly aggregated?
```

#### Section 8: Bank Statement Reading Guide

##### GTBank (Guaranty Trust / GTCo)

- Export: CSV/PDF from GTBank Internet Banking / GTWorld app
- Columns: `Date;Description;Debit;Credit;Balance`
- Amount format: comma thousands, period decimal (e.g., `2,500,000.00`)
- Date: DD/MM/YYYY or DD-MMM-YYYY
- Credits: `NIP CR FROM [sender]`, `MOBILE TRANSFER FROM [sender]`

##### Access Bank

- Export: CSV/Excel from Access More app / Internet Banking
- Columns: `Date;Narration;Debit;Credit;Balance`
- Credits: `NIP CREDIT FROM [sender]`, `TRANSFER FROM [sender]`

##### Zenith Bank

- Export: CSV from Zenith Internet Banking / ZMobile
- Columns: `Trans Date;Value Date;Description;Debit;Credit;Balance`
- Credits: `NIP CR [sender]`, `INWARD TRF FROM [sender]`

##### UBA (United Bank for Africa)

- Export: CSV/PDF from UBA Internet Banking / UBA Mobile
- Standard Nigerian bank format

##### First Bank of Nigeria (FBN)

- Export: CSV from FirstBank Online / FirstMobile
- Columns: `Date;Description;Debit;Credit;Balance`

##### Stanbic IBTC

- Export: CSV from Stanbic IBTC Internet Banking
- Standard format

##### Kuda Bank / OPay / PalmPay / Moniepoint (Digital)

- Export: CSV/PDF from app
- Simple format; credit/debit columns or single column
- Narrations: `Transfer from [name]`, `Received from [name]`
- OPay: `OPay Transfer from [name]`
- PalmPay: `PalmPay Transfer from [name]`
- Moniepoint: `Moniepoint Transfer from [name]`

##### Paystack / Flutterwave Settlements

- Appear in primary bank statement as `PAYSTACK SETTLEMENT` or `FLUTTERWAVE PAYOUT`
- Gross-up required: platform deducts fees before settlement
- Cross-reference with Paystack/Flutterwave merchant dashboard for gross amounts

##### Key Nigerian Banking Notes

- All amounts in NGN (Nigerian naira); comma thousands, period decimal
- NIP (NIBSS Instant Payment) is the standard inter-bank transfer system
- USSD banking (*737 for GTBank, *901 for Access, *966 for Zenith, etc.) common for mobile transfers
- POS (Point of Sale) settlements may be delayed 1-3 days
- Stamp duty charges (NGN 50 on transactions above NGN 10,000) are not deductible business expenses
- Multiple accounts across banks is common: consolidate all statements

#### Section 9: Onboarding Fallback

**Filing authority:**
> "Nigerian personal income tax is administered by the Federal Inland Revenue Service (FIRS) for residents of the Federal Capital Territory (Abuja) and by the State Internal Revenue Service (SIRS) for residents of all other states. Where do you reside? This determines where you file your self-assessment return."

**WHT certificates:**
> "If your clients deducted withholding tax (10% on professional fees, 5% on contracts) from your payments, you need the WHT certificates (credit notes) to claim these as credits against your annual tax. Contact each client to obtain their WHT certificates. Without them, the credit cannot be claimed."

**CRA explanation:**
> "Under the Consolidated Relief Allowance (introduced by Finance Act 2020), you receive an automatic deduction of the higher of NGN 200,000 or 1% of your gross income, plus an additional 20% of your gross income. This replaces the old personal allowance, children's allowance, and dependent relative allowance. No documentation is needed for CRA: it is computed automatically."

**Minimum tax:**
> "Even if your computed tax per the progressive rates is very low or zero (due to high expenses), you are still required to pay a minimum tax of 1% of your gross income. The minimum tax acts as a floor: you pay whichever is higher between computed tax and minimum tax."

#### Section 10: Reference Material

##### Key Legislation

- **Personal Income Tax Act (PITA)**: Cap P8 LFN 2004, as amended by Finance Act 2020, 2021, 2023  _(Personal Income Tax Act (PITA))_
- **FIRS Establishment Act**: Federal Inland Revenue Service  _(FIRS Establishment Act)_
- **Pension Reform Act 2014**: Pension contribution requirements  _(Pension Reform Act 2014)_
- **Finance Act 2020**: Introduced CRA and simplified minimum tax  _(Finance Act 2020)_

##### Filing Calendar

**Filing Calendar**  _(PITA s 41-44)_

| Deadline | Event | Status |
| --- | --- | --- |
| 31 March | Self-assessment return (PITA s 41-44) | unverified, earlier text not re-read |
| 31 March | Payment of tax due | unverified, earlier text not re-read |
| Monthly | WHT remittance (if agente de retención) | unverified, earlier text not re-read |

##### Penalties

**Penalties**

| Offence | Penalty | Status |
| --- | --- | --- |
| Late filing | NGN 50,000 first month + NGN 25,000/subsequent month | unverified, earlier text not re-read |
| Late payment | 10% of tax due + interest at CBN MPR + spread | unverified, earlier text not re-read |
| Failure to keep records | NGN 50,000 fine | unverified, earlier text not re-read |
| Incorrect return (without fraud) | Twice the difference | unverified, earlier text not re-read |
| Tax evasion | NGN 20,000 fine or 3 years imprisonment or both | unverified, earlier text not re-read |

##### Record Keeping

- Minimum retention: 6 years
- Business records, invoices, receipts, bank statements, contracts
- WHT certificates: retain permanently for audit

##### Useful References

- FIRS: www.firs.gov.ng
- TaxPro Max: taxpromax.firs.gov.ng
- State IRS portals: vary by state (LIRS: lirs.gov.ng, etc.)
- Joint Tax Board (JTB): www.jtb.gov.ng



## Sources

| Source | URL | Read on |
|---|---|---|
| Nigeria Tax Act 2025, Act No. 7, Official Gazette No. 117, 26 June 2025. UNOFFICIAL COPY hosted by Premium Times, not an official host. Sections read: ss.28 to 31, 56 to 59, 195, Fourth Schedule, definitions | https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf | 2026-11-01 |
| NRS notice of 20 July 2026 on e-invoicing (read by an earlier pass; official) | https://www.nrs.gov.ng/ | 2026-11-01 |

NRS guides at https://www.nrs.gov.ng/taxpayer-services/tax-guides-and-manuals could not be read: a page shell loaded, then other NRS pages showed a CAPTCHA, so no cross-check was done.

Not yet confirmed: every NTA figure in this skill. Each comes from an unofficial press-hosted copy and was not confirmed in an official document, because nrs.gov.ng showed a CAPTCHA on 2026-11-01 and it was not touched. Also unconfirmed: all filing dates, forms, portals and penalties under the Nigeria Tax Administration Act 2025, whose text we did not open; the VAT registration threshold (no figure appears in the NTA text read); capital allowance rates for ordinary trades; and all earlier text in the pre-2026 section. Lost content restored: 0, nothing removed.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
