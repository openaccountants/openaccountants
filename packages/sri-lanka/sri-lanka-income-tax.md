---
name: sri-lanka-income-tax
description: Use this skill whenever asked about Sri Lanka income tax for individuals, sole proprietors, freelancers, and self-employed people for the year of assessment 2026/27 (1 April 2026 to 31 March 2027). Trigger on phrases like how much income tax do I pay in Sri Lanka, APIT, PAYE, personal relief, Inland Revenue Department, IRD, year of assessment, self-assessment instalments, EPF ETF, TIN registration, Asmt_IIT return, withholding tax interest, freelancer tax LKR, or any question about computing or filing personal income tax for a resident or non-resident individual in Sri Lanka. Gives the Rs. 1,800,000 personal relief, the 6% to 36% slabs, the 15% maximum rate on foreign-currency income remitted through a bank, the 45% rate, the capital gains rate rise to 15% from 3 June 2026, credits, instalments, the return date and penalties, under the Inland Revenue Act No. 24 of 2017 as amended up to Act No. 11 of 2026.
version: "1.0"
jurisdiction: LK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27 (2026-27), 1 April 2026 to 31 March 2027"
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Sri Lanka Income Tax: individual and self-employed, year of assessment 2026/27, v1.0

Built from the law: not yet approved by an accountant. Figures are taken from the Inland Revenue Act No. 24 of 2017 (IRA) as consolidated by the Inland Revenue Department (IRD), the Inland Revenue (Amendment) Act No. 11 of 2026, and IRD pages read on 14 November 2026. Anything not confirmed there sits on the Not yet confirmed line under Sources.

## Scope and who this is for

| Field | Detail |
| --- | --- |
| Country | Democratic Socialist Republic of Sri Lanka |
| Tax | Personal income tax (administered by the IRD) |
| Currency | Sri Lankan Rupee (LKR, Rs.) only |
| Year of assessment (YA) | 1 April to 31 March; this skill: YA 2026/27 |
| Law | IRA No. 24 of 2017, as amended by Acts No. 10 of 2021, 45 of 2022, 4 and 14 of 2023, 2 of 2025 and 11 of 2026 (certified 3 June 2026) |
| Filing portal | IRD e-Services (e-filing) |
| Return deadline | Eight months after the year end: 30 November 2027 for YA 2026/27 (section 93(1)) |

- **Sri Lanka has a progressive personal income tax** on resident individuals and non-resident individuals. The rates in First Schedule paragraph 1(1D) apply "for a year of assessment commencing from April 1, 2025" and were not changed by Act No. 11 of 2026, so they apply to 2026/27.
- **In:** residents, non-resident citizens and non-citizen non-residents with employment, business, investment or other income; sole proprietors and freelancers.
- **Out:** company tax (`sri-lanka-corporate-tax`), partnership returns (only the partnership rate is noted), capital gains tax computation (`sri-lanka-capital-gains-tax`), payroll APIT tables (`sri-lanka-payroll`), withholding by payers (`sri-lanka-withholding-tax`), instalment detail (`sri-lanka-provisional-tax-ait`), VAT (`sri-lanka-vat`), SSCL (`sri-lanka-sscl`).
- **What changed for 2026/27:** capital gains on investment assets of individuals and partnerships rose from 10% to 15% from 3 June 2026, the date Act No. 11 of 2026 became law (its section 36 amending First Schedule paragraphs 1(2)(a) and 2(2)(a)); motor vehicle gains are now listed in section 8(2)(c); instalments moved to a prior-year basis from 1 April 2026; interest of up to Rs. 5,000 for the year no longer needs a return on its own (new section 94(1)(d)); a resident individual with no taxable income may give a self-declaration so that a financial institution does not withhold on interest (new section 84(3)(f)); a return declaring at least 120% of the previous year's tax, paid in full with no refund claim and an affidavit, is accepted as filed (new section 135(7)); senior citizens may file in writing or electronically (section 113(1D)).

## Ask the client first

1. Residence and citizenship: resident, non-resident citizen, or non-citizen non-resident? (The relief is for residents and non-resident citizens only.)
2. Income sources: employment (APIT deducted?), business or self-employment, rent, interest, dividends, foreign income.
3. Any service income for use outside Sri Lanka, or foreign-source income, earned in foreign currency and remitted through a bank to Sri Lanka, with evidence?
4. Any realisation of investment assets or motor vehicles in the year, and the dates (before or from 3 June 2026)?
5. Credits: APIT certificates, withholding certificates, instalments paid.
6. Staff employed (EPF and ETF), home office or vehicle business use.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Personal relief | Rs. 1,800,000 a year | Each year of assessment from 1 April 2025; residents and non-resident citizens; not against investment-asset gains | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Income%20Tax.aspx?menuid=1201 |
| Slab 1: taxable income up to Rs. 1,000,000 | 6% | First Schedule paragraph 1(1D), years from 1 April 2025 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |
| Slab 2: over Rs. 1,000,000 to Rs. 1,500,000 | Rs. 60,000 plus 18% of the excess over Rs. 1,000,000 | Same | same |
| Slab 3: over Rs. 1,500,000 to Rs. 2,000,000 | Rs. 150,000 plus 24% of the excess over Rs. 1,500,000 | Same | same |
| Slab 4: over Rs. 2,000,000 to Rs. 2,500,000 | Rs. 270,000 plus 30% of the excess over Rs. 2,000,000 | Same | same |
| Slab 5: over Rs. 2,500,000 | Rs. 420,000 plus 36% of the excess over Rs. 2,500,000 | Same | same |
| Services for use outside Sri Lanka, paid in foreign currency and remitted through a bank | Maximum rate of 15% | Paragraph 1(6)(a), from 1 April 2025 | same |
| Foreign-source gains and profits in foreign currency remitted through a bank | Maximum rate of 15% | Paragraph 1(6)(b), from 1 April 2025 | same |
| Betting and gaming, manufacture and sale or import and sale of liquor or tobacco | 45% | Paragraph 1(2)(c), from 1 April 2025 | same |
| Gains from the realisation of investment assets, individuals | 15% from 3 June 2026; 10% before | Act No. 11 of 2026 section 36(1), operative on the date the Bill became an Act | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf |
| Partnership: taxable income up to Rs. 1,000,000 | 0%, then 6% on the excess | Partners' shares then exempt at the individual level | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx |
| Partnership investment-asset gains | 15% from 3 June 2026; 10% before | Act No. 11 of 2026 section 36(2) | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf |
| Terminal benefits (commuted pension, retiring gratuity, approved loss-of-office scheme, ETF payment) | 0% on the first Rs. 10,000,000; 6% on the next Rs. 10,000,000; 12% on the balance | Paragraph 1(2)(b)(iii) and (3), from 1 January 2020 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |
| Rent relief, resident individual's investment asset | 25% of rent income | IRD tax chart list of reliefs | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx |
| Solar panel relief, resident individual | Rs. 600,000 a year, up to the expenditure | IRD tax chart list of reliefs | same |
| Late filing penalty | Greater of 5% of tax owing plus 1% a month, or fifty thousand rupees plus ten thousand rupees a month; capped at four hundred thousand rupees | Section 178 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |
| Late payment penalty | 20% of tax due but not paid (10% for an instalment) | Not paid within 14 days of the due date; section 179 | same |
| Late payment interest | one and one-half per cent per month or part month | Sections 157, 159(1) | same |
| Interest income with no return needed on that ground | Not over five thousand rupees for the year | New section 94(1)(d), from 1 April 2025 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf |

### Steps

1. Confirm residence and citizenship (Ask the client first).
2. Build assessable income: employment (per APIT certificate), business profit (income less deductible expenses, capital allowances), investment income (gross up any net-of-WHT receipts), other income. A VAT-registered person excludes the VAT collected.
3. Set aside special-rate income: investment-asset gains (15% from 3 June 2026; relief does not apply), 45% activities, terminal benefits (own scale), and foreign-currency remitted income eligible for the 15% maximum (only with bank evidence).
4. Deduct the Rs. 1,800,000 personal relief (residents and non-resident citizens), and any rent or solar relief that applies.
5. Apply the slabs to the remaining taxable income. For income eligible for the 15% maximum, the slab rate on that income is capped at 15% (reading of "maximum rate of 15%"; confirm with the IRD where material).
6. Deduct APIT, withholding credits and instalments. The balance is due on the return due date (section 145(2)(b)).
7. File the return (Asmt_IIT) on IRD e-Services by 30 November 2027.

### Penalties and interest

| Default | Consequence | Section |
| --- | --- | --- |
| Return late | Greater of 5% of tax owing plus 1% a month, or Rs. 50,000 plus Rs. 10,000 a month; cap Rs. 400,000 | 178 |
| Tax not paid within 14 days | 20% of the unpaid tax | 179(1) |
| Instalment not paid within 14 days | 10% of the unpaid instalment | 179(2) |
| Any late tax | Interest at 1.5% a month or part month from the due date | 157, 159 |
| Negligent or intentional understatement | 25%, or 75% if over Rs. 10,000,000 or 25% of the liability | 180 |
| Failing to register | Up to Rs. 50,000 | 177 |
| Failing to file after a 30-day notice | Fine up to Rs. 400,000, up to six months' imprisonment, or both | New section 185A |

### Transaction Pattern Library

Deterministic pre-classifier. When a bank-statement transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty name or description as it appears on the statement. If multiple match, use the most specific. If none match, fall through to Tier 1 rules in Section 5. Local-language (Sinhala/Tamil transliteration and English) terms are included.

#### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Business income | If VAT-registered, extract net (excl. 18% VAT) |
| FEES, PROFESSIONAL FEES, CONSULTANCY, SERVICE CHARGE | Business income | Typical self-employment fee |
| STRIPE PAYOUT, PAYONEER, WISE, PAYPAL | Business income (often foreign-currency service income) | May qualify for max-15% concession: FLAG, do not auto-apply |
| UPWORK, FIVERR, TOPTAL, FREELANCER | Business income | Freelance platform; net of platform commission; often foreign-currency: FLAG concession |
| SALARY, SALARIES, EMP [name], MAASIKA (monthly pay) | Employment income | Subject to APIT at source: reconcile to APIT certificate |
| RENT RECEIVED, KULIYA (rent) | Rental income | 10% AIT applies if rent > Rs. 100,000/month to resident individual |
| INTEREST, INTERESSI, FD INTEREST, SAVINGS INT | Investment income | 10% WHT/AIT deducted at source |
| DIVIDEND, DIVIDENDS | Investment income | 15% final WHT |
| IRD REFUND, TAX REFUND | EXCLUDE | Refund of prior-year tax, not income |
| GOVERNMENT GRANT, RELIEF GRANT | Check nature | Capital grants EXCLUDE; revenue grants = business income |

#### 3.2 Expense Patterns (Debits): Deductible business expenses

**Deductible business expenses**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT, KULIYA UFFICE, COMMERCIAL RENT | Office rent | Deductible | Dedicated business premises |
| ACCOUNTANT, AUDITOR, BOOKKEEP, CA SRI LANKA | Accountancy fees | Deductible |  |
| LAWYER, LEGAL, NOTARY (business) | Legal fees | Deductible | Must be business-related |
| STATIONERY, OFFICE SUPPLIES | Office supplies | Deductible |  |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Advertising | Deductible |  |
| TRAINING, COURSE, SEMINAR, CPD | Training | Deductible | Must relate to current business |
| BANK CHARGE, COMMISSION, LEDGER FEE | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYONEER FEE, TRANSACTION FEE | Payment processing | Deductible |  |
| DOMAIN, HOSTING, AWS, AZURE, DIGITALOCEAN | IT infrastructure | Deductible | Capitalise if a long-lived asset: see 3.5 |

#### 3.3 Expense Patterns (Debits): SaaS / software subscriptions

**SaaS / software subscriptions**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |

#### 3.4 Expense Patterns (Debits): Utilities (apportion if mixed)

**Utilities**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| CEB, LECO, ELECTRICITY BILL | Electricity | T2 if home office | 100% if dedicated office; proportional if home; default 0% |
| WATER BOARD, NWSDB | Water | T2 if home office | Same apportionment rule |
| DIALOG, MOBITEL, SLT, HUTCH, AIRTEL | Telecoms / broadband | T2 | Business-use portion only; default 0% if mixed |

#### 3.5 Expense Patterns (Debits): Capital / depreciable assets

**Capital / depreciable assets**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | Capital allowance | Do NOT fully expense; see Section 5.4 [RESEARCH GAP: confirm rate] |
| PRINTER, SCANNER, COPIER | Office equipment | Capital allowance | [RESEARCH GAP: confirm rate] |
| FURNITURE, DESK, CHAIR | Furniture/fittings | Capital allowance | [RESEARCH GAP: confirm rate] |
| VEHICLE, CAR (business) | Motor vehicle | Capital allowance, business % only | [RESEARCH GAP: confirm rate] |

#### 3.6 Expense Patterns (Debits): NOT deductible

**NOT deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Private / non-business |
| GROCERIES, SUPERMARKET, KEELLS, CARGILLS, ARPICO | Personal | NOT deductible | Private living costs |
| FINE, PENALTY, SURCHARGE | Fines/penalties | NOT deductible | Public policy |
| INCOME TAX, IRD PAYMENT, SELF-ASSESSMENT TAX | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |

#### 3.7 Exclusions and special routing (neither ordinary income nor expense)

**Exclusions and special routing**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN ACCOUNT, INTERNAL TRANSFER, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN, LOAN REPAYMENT (principal) | EXCLUDE | Capital movement (interest may be deductible if business) |
| EPF, ETF, PROVIDENT FUND | EXCLUDE from income tax expense | Statutory contribution: see Section 6.3 |
| VAT PAYMENT, SSCL PAYMENT | EXCLUDE | Indirect-tax liability, not an income-tax expense |
| SELF-ASSESSMENT INSTALMENT, QUARTERLY TAX | Credit against liability | Not an expense: it is tax paid on account |

#### 3.8 Sri Lankan Banks: Statement Format Reference

**Sri Lankan Banks: Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Bank of Ceylon (BOC) | TRANSFER, SLIP, STANDING ORDER, CHARGES | PDF/CSV; date DD/MM/YYYY |
| People's Bank | DEPOSIT, WITHDRAWAL, DD, CHARGE | PDF; description carries counterparty |
| Commercial Bank (ComBank) | FUND TRANSFER, CEFT, SLIPS, FEE | CSV/PDF; CEFT = electronic transfer |
| Hatton National Bank (HNB) | TRANSFER, SO, DD, COMMISSION | PDF/CSV |
| Sampath Bank | SLIPS, ONLINE TRF, CHARGE | CSV; clean counterparty names |


### Classification examples

#### Example 1: Local client payment (not VAT-registered)

Input line:
`14/06/2025 ; BOC FUND TRANSFER IN ; PERERA TRADING (PVT) LTD ; INV-2025-021 ; +250,000.00 ; LKR`

Reasoning:
Local fee for services. Client is below VAT threshold and not registered, so the full Rs. 250,000 is business income. No VAT to strip out.

Classification: Business income = Rs. 250,000.

#### Example 2: Foreign-currency freelance payout (concession FLAG)

Input line:
`28/06/2025 ; COMBANK CEFT ; PAYONEER INC ; USD SERVICE PAYOUT ; +480,000.00 ; LKR`

Reasoning:
Service income earned in / remitted via foreign currency through a bank may qualify for the max-15% concession (IRD tax chart 2025/2026). This is reviewer judgement: it depends on remittance routing and documentation. Do NOT auto-apply the 15% cap. Default: include Rs. 480,000 as business income at progressive rates and FLAG for the reviewer to assess the concession.

Classification: Business income = Rs. 480,000. FLAG: possible 15% foreign-currency-service concession (R-LK-4).

#### Example 3: Bank interest with 10% WHT deducted

Input line:
`30/09/2025 ; HNB ; FD INTEREST CREDIT ; NET OF WHT ; +90,000.00 ; LKR`

Reasoning:
Interest and discount income carries 10% WHT/AIT at source from 1 Apr 2025 (up from 5%). If the credit is shown net of WHT, gross it up: Rs. 90,000 / 0.90 = Rs. 100,000 gross, with Rs. 10,000 WHT credit. For a resident with total annual income above Rs. 1,800,000, interest is included; the 10% deducted is a credit against the final liability. For a non-resident citizen, the 10% on bank interest is a final tax (not added to the progressive computation).
Source: IRD tax chart (withholding table, from 1 April 2025).

Classification: Investment income gross = Rs. 100,000; WHT credit = Rs. 10,000. (Confirm whether net or gross is shown on the statement.)

#### Example 4: SaaS subscription (deductible)

Input line:
`01/07/2025 ; SAMPATH ONLINE ; ADOBE SYSTEMS ; CREATIVE CLOUD ; -9,500.00 ; LKR`

Reasoning:
Recurring software subscription used in the business. Fully deductible operating expense.

Classification: Deductible expense = Rs. 9,500.

#### Example 5: EPF/ETF remittance by a sole proprietor with staff

Input line:
`31/07/2025 ; BOC STANDING ORDER ; EPF DEPARTMENT ; JUN 2025 CONTRIB ; -160,000.00 ; LKR`

Reasoning:
This is the employer EPF remittance for staff (employee 8% + employer 12%). The employer share is a deductible business cost; the employee share was withheld from staff salaries and is not the proprietor's own expense. EPF must be remitted on or before the last working day of the following month. Do NOT classify as the proprietor's personal income-tax deduction line: it sits in the payroll-cost computation. FLAG to confirm the employer/employee split.
Source: EPF (CBSL) Employer FAQ: https://epf.lk/?page_id=811

Classification: Payroll cost (employer share deductible). FLAG: confirm employer vs employee split.


### Tier 1 rules (when data is clear)

#### 5.1 The wholly-and-exclusively / business-nexus test

- **Business-nexus test**: An expense is deductible only if incurred in producing the business income. Mixed-use expenses must be apportioned on a reasonable, documented basis. Domestic/private expenses are not deductible.  _(Inland Revenue Act No. 24 of 2017 (deductions provisions))_

#### 5.2 Income recognition

- **Income recognition**: All business income goes into assessable income. Where the individual is VAT-registered, report income net of the 18% VAT collected (VAT is a liability to IRD, not income). Employment income subject to APIT is included but reconciled against the APIT certificate (the APIT already deducted is a credit).

#### 5.3 Personal relief

- **Personal relief application detail**: Deduct Rs. 1,800,000/year from assessable income before applying the slabs (residents and non-resident citizens only). Relief does NOT apply against investment-asset gains. Monthly equivalent Rs. 150,000 is used in APIT.  _(IRD PN/IT/2025-01 (26.03.2025))_

#### 5.4 Capital allowances (depreciation)

- **Capital allowances research gap**: Capital assets are not fully expensed in year one; they are written off over time via capital allowances under the Inland Revenue Act No. 24 of 2017. [RESEARCH GAP: reviewer to confirm the current per-class capital-allowance rates and the depreciable-asset classes under IRA No. 24 of 2017 before applying any depreciation figure.] Until confirmed, flag every capital asset for reviewer treatment rather than guessing a rate.  _(Inland Revenue Act No. 24 of 2017)_


#### 5.7 Non-deductible expenses

**Non-deductible expenses table**

| Expense | Reason |
| --- | --- |
| Entertainment / private meals | Not in production of income |
| Personal living expenses, drawings | Private |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Capital expenditure | Recovered via capital allowances, not expensed |


### Tier 2 Catalogue (Reviewer Judgement Required) + Payroll Contributions

#### 6.1 Home office deduction

- **Home office deduction rules**: - Calculate the proportion of the home used wholly for business (dedicated room / floor area). - Apply that percentage to rent, electricity (CEB/LECO), water (NWSDB), broadband. - A dual-use room does not qualify. Conservative default: 0% until reviewer confirms a dedicated workspace and basis. Flag for reviewer: confirm room/floor-area basis and that the space is genuinely dedicated.

#### 6.2 Motor vehicle business use

- **Motor vehicle business use rules**: - Only the business-use percentage of fuel, insurance, maintenance and depreciation is deductible. - Requires a mileage log. Conservative default: 0% business use until a log is provided. Flag for reviewer: confirm business percentage and capital-allowance rate (see Section 5.4 research gap).

#### 6.3 EPF: Employees' Provident Fund

- **EPF rules**: - Employee: 8% of total monthly earnings (withheld from salary). - Employer: 12% of total monthly earnings. - Total: 20%. No statutory salary ceiling/floor on the percentage (applies to "total earnings"). - Remit on or before the last working day of the following month. - Late surcharge (escalating on the contribution): 1-10 days 5%; 11 days-1 month 15%; 1-3 months 20%; 3-6 months 30%; 6-12 months 40%; over 12 months 50%. Plus 2% surcharge for incomplete details.  _(EPF (CBSL) Employer FAQ: https://epf.lk/?page_id=811 ; CBSL: https://www.cbsl.gov.lk/en/employees-provident-fund)_

#### 6.4 ETF: Employees' Trust Fund

- **ETF rules**: - Employer: 3% of total monthly earnings. Employee: nil: the employer may not deduct ETF from the employee. - Remit on or before the last working day of the succeeding month. - Late surcharge: same escalating 5% -> 50% scale; late half-yearly returns add a 1% surcharge per delayed month on face value.  _(ETF Board Employers FAQ: https://etfb.lk/employers-faq/)_

#### 6.5 Gratuity

- **Gratuity rules**: gratuity is payable on termination under the Payment of Gratuity Act No. 12 of 1983. The service and headcount conditions and the formula in the earlier version came from a secondary source and are on the Not yet confirmed line; refer.

#### 6.6 Foreign-currency / foreign-source concession (max 15%)

- **Foreign-currency concession rule**: The max-15% rate on foreign-source income, or service income earned in/remitted via foreign currency through a bank, depends on remittance routing and documentation. Conservative default: apply ordinary progressive rates and FLAG; do not auto-apply 15% (R-LK-4).

#### 6.7 Bad debt write-off

- **Bad debt write-off rule**: Deductible only if the income was previously brought to account, recovery steps were taken, and the debt is genuinely irrecoverable. Flag for reviewer to confirm all three.


## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Non-citizen non-resident | No personal relief; slabs apply to taxable income |
| Investment asset sold before 3 June 2026 | 10% |
| Investment asset sold on or after 3 June 2026 | 15% |
| Gain on a motor vehicle | Now listed as a gain in section 8(2)(c) (Act No. 11 of 2026, from 1 April 2024); refer the computation |
| Foreign-currency fees kept abroad | Normal slabs, no 15% cap |
| Interest only, not over Rs. 5,000 for the year | No return needed on that ground (section 94(1)(d)) |
| Salary arrears received this year | Tax credit under new section 96A (from 1 January 2024); refer the computation |
| Declared tax at least 120% of last year, paid in full, no refund claim, affidavit | Return accepted as filed (section 135(7), from 1 April 2025) |

#### Conservative Defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown residence status | STOP: relief and rates differ for non-citizen non-residents |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether income is foreign-source remitted via bank | Treat as ordinary income (progressive rates), flag for reviewer |
| Unknown whether person is an instalment payer | Assume instalment payer if any business / self-employment income |
| Unknown VAT registration status | Assume not registered; flag if turnover near threshold |
| Unknown gratuity entitlement | Flag: depends on years of service and employer size |


## Worked cases

### Case 1: resident sole proprietor across all five slabs

Resident, net profit Rs. 5,300,000, no other income, no special-rate income. Taxable income after the relief is Rs. 3,500,000.

```oa-check
name: Resident individual, profit Rs. 5,300,000, YA 2026/27
inputs:
  profit: 5300000
  relief: 1800000
steps:
  - taxable: max(profit - relief, 0)
  - b1: min(taxable, 1000000) * 0.06
  - b2: max(min(taxable, 1500000) - 1000000, 0) * 0.18
  - b3: max(min(taxable, 2000000) - 1500000, 0) * 0.24
  - b4: max(min(taxable, 2500000) - 2000000, 0) * 0.30
  - b5: max(taxable - 2500000, 0) * 0.36
  - tax: b1 + b2 + b3 + b4 + b5
expected:
  taxable: 3500000
  tax: 780000
```

### Case 2: decision, bring foreign client fees home through a bank or not

A resident freelance developer earns the same Rs. 5,300,000 profit from overseas clients, paid in US dollars. If the fees are remitted through a Sri Lankan bank, paragraph 1(6)(a) caps the rate at 15%, so every slab above 15% falls to 15%. If the money stays abroad, the normal slabs apply. The developer also sold listed shares held as an investment on 10 July 2026 for a gain of Rs. 2,000,000: after 3 June 2026 the rate is 15%, not 10%, and the relief does not apply to it.

```oa-check
name: Foreign-currency fees remitted against not remitted, plus a 2026 gain
inputs:
  profit: 5300000
  relief: 1800000
  gain: 2000000
steps:
  - taxable: profit - relief
  - normal_tax: min(taxable, 1000000) * 0.06 + max(min(taxable, 1500000) - 1000000, 0) * 0.18 + max(min(taxable, 2000000) - 1500000, 0) * 0.24 + max(min(taxable, 2500000) - 2000000, 0) * 0.30 + max(taxable - 2500000, 0) * 0.36
  - remitted_tax: min(taxable, 1000000) * 0.06 + max(taxable - 1000000, 0) * 0.15
  - saving: normal_tax - remitted_tax
  - gain_tax: gain * 0.15
  - gain_tax_before_june: gain * 0.10
expected:
  normal_tax: 780000
  remitted_tax: 435000
  saving: 345000
  gain_tax: 300000
  gain_tax_before_june: 200000
```

The 15% cap is read here as capping each slab rate; if the IRD applies it differently, recompute. Use it only with bank-remittance evidence.

#### Test Suite

Test 1: Slab boundary, single slab.
Input: Resident, net profit Rs. 2,800,000, no other income.
Expected: relief 1,800,000 -> taxable 1,000,000; tax = 1,000,000 x 6% = Rs. 60,000.

Test 2: Multiple slabs.
Input: Resident, net profit Rs. 5,300,000.
Expected: taxable 3,500,000; tax = 60,000 + 90,000 + 120,000 + 150,000 + (1,000,000 x 36% = 360,000) = Rs. 780,000.

Test 3: Below relief, no tax.
Input: Resident, net profit Rs. 1,500,000.
Expected: 1,500,000 - 1,800,000 < 0 -> taxable Rs. 0; income tax = Rs. 0.

Test 4: Top slab reached exactly.
Input: Resident, net profit Rs. 4,300,000 -> taxable 2,500,000.
Expected: cumulative tax at top of 30% slab = Rs. 420,000; nothing in the 36% band; tax = Rs. 420,000.

Test 5: Interest gross-up with WHT credit.
Input: FD interest credited net Rs. 90,000 (10% WHT withheld).
Expected: gross = 90,000 / 0.90 = Rs. 100,000; WHT credit Rs. 10,000 against liability.

Test 6: EPF/ETF employer on-cost.
Input: Monthly gross payroll Rs. 1,000,000 for staff.
Expected: EPF employer 12% = Rs. 120,000; ETF employer 3% = Rs. 30,000; employer on-cost = Rs. 150,000 (15%). Employee EPF 8% = Rs. 80,000 withheld from staff. Total contributions remitted relating to EPF = Rs. 200,000 (20%).

Test 7: Foreign-currency concession FLAG.
Input: Payoneer service payout Rs. 480,000 to a freelancer.
Expected: include as business income at progressive rates by default; FLAG for reviewer to assess the max-15% foreign-currency-service concession. Do NOT auto-apply 15%.


## When to refuse or refer

#### Required Inputs

- **Minimum viable / Recommended / Ideal / Refusal**: Minimum viable: bank statement for the full year of assessment (1 Apr: 31 Mar) in CSV, PDF, or pasted text, plus confirmation of residence status (resident / non-resident citizen / non-citizen non-resident) and source of income (employment APIT, self-employment/business, or both). Recommended: sales invoices, purchase invoices/receipts, EPF/ETF contribution records, prior-year return or assessment, APIT certificate(s) from employer(s), withholding/AIT certificates (interest, rent, dividends), TIN. Ideal: complete income and expenditure statement, asset register, Statement of Estimated Tax (SET) and quarterly instalment receipts, foreign-currency remittance evidence (for the 15% concession). Refusal if minimum is missing: SOFT WARN. No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from a bank statement alone. The reviewer must verify all deductions are supported by valid documentation and that income source classifications (especially foreign-currency concessions and capital gains) are correct."

#### Refusal Catalogue

- **R-LK-1**: Residence status unknown. "Residence status determines whether the Rs. 1,800,000 personal relief applies and which rates are used. A non-citizen non-resident does not get the relief; a non-resident citizen does. This skill cannot compute tax without it. Please confirm."
- **R-LK-2**: Companies / partnerships filing. "This skill covers individuals and sole proprietors. Partnership-level returns and company income tax (corporate rates) are out of scope: escalate to a Sri Lankan tax professional."
- **R-LK-3**: Investment-asset (capital) gains. "Gains on realisation of investment assets are taxed at 15% from 3 June 2026 (10% before) and the personal relief does NOT apply to them. The base computation requires asset cost, proceeds, and dates. Escalate to a reviewer for capital gains."
- **R-LK-4**: Foreign-source / foreign-currency concessions. "The max-15% concessions for foreign-source income or foreign-currency service income remitted through a bank depend on remittance evidence and bank routing. Flag and escalate: do not apply the 15% cap without confirmation."
- **R-LK-5**: Arrears / enforcement / penalties. "Client has outstanding tax, EPF/ETF arrears, or is subject to IRD enforcement. Escalating surcharges (EPF/ETF up to 50%) and income-tax penalties/interest apply. Escalate to a Sri Lankan tax professional immediately."
- **R-LK-6**: VAT / SSCL return requested. "This skill covers personal income tax only. VAT and the Social Security Contribution Levy (SSCL) are separate turnover taxes: use `sri-lanka-vat` or `sri-lanka-sscl` for thresholds and returns."


### PROHIBITIONS

- NEVER apply the Rs. 1,800,000 personal relief to a non-citizen non-resident, or against investment-asset gains.
- NEVER auto-apply the max-15% foreign-currency / foreign-source concession: it requires reviewer confirmation of remittance routing.
- NEVER fully expense a capital asset: it is recovered via capital allowances (and the rate is a [RESEARCH GAP] pending confirmation).
- NEVER treat EPF/ETF as the proprietor's personal income-tax deduction without separating employer vs employee share.
- NEVER include VAT collected on sales as income for a VAT-registered person.
- NEVER allow entertainment, fines/penalties, drawings, or income tax itself as a deduction.
- NEVER apply the monthly APIT Table 01 formulas outside the employees it covers: see `sri-lanka-payroll`.
- NEVER base 2026/27 instalments on a current-year estimate unless the prior-year basis does not fit: see `sri-lanka-provisional-tax-ait`.
- NEVER present tax calculations as definitive: always label as estimated, pending reviewer sign-off.


## Filing and payment

| Step | Detail |
| --- | --- |
| Return | Asmt_IIT return of income on IRD e-Services, by 30 November 2027 for YA 2026/27 (eight months after the year end, section 93(1)) |
| Balance of tax | Self-assessed tax is due on the due date for the return (section 145(2)(b)) |
| Instalments | 15 August, 15 November, 15 February, 15 May for instalment payers (section 90(2)); prior-year basis from 2026/27 (`sri-lanka-provisional-tax-ait`) |
| TIN | Register with the IRD (section 102); a TIN certificate is needed for bank accounts, vehicle and land registration and other listed purposes from 1 April 2026 (section 103(6)) |

### Excel Working Paper Template

```
SRI LANKA INCOME TAX: INDIVIDUAL WORKING PAPER
Year of Assessment: 2026/2027 (1 Apr 2026 - 31 Mar 2027)
Client: ___________________________
Residence: Resident / Non-resident citizen / Non-citizen non-resident
Instalment payer? Yes / No

A. BUSINESS / SELF-EMPLOYMENT INCOME
  A1. Local client fees                          ___________
  A2. Foreign-currency service payouts (FLAG)    ___________
  A3. Platform payouts (Stripe/Payoneer/etc.)    ___________
  A4. Other business income                      ___________
  A5. TOTAL business income                      ___________

B. ALLOWABLE BUSINESS EXPENSES
  B1. Office rent                                ___________
  B2. Accountancy / legal fees                   ___________
  B3. Office supplies / stationery               ___________
  B4. Software subscriptions                     ___________
  B5. Marketing / advertising                    ___________
  B6. Bank / payment processing charges          ___________
  B7. Training                                   ___________
  B8. Utilities (business % of CEB/NWSDB/telco)  ___________
  B9. Home office (% of rent/utilities)          ___________
  B10. Vehicle (business %)                       ___________
  B11. Other allowable expenses                   ___________
  B12. TOTAL expenses                             ___________

C. NET PROFIT (A5 - B12)                          ___________

D. OTHER INCOME (employment APIT, rent, interest, dividends)
  D1. Employment income (per APIT certificate)    ___________
  D2. Rental income                               ___________
  D3. Interest (gross; note 10% WHT credit)       ___________
  D4. Dividends (note 15% final WHT)              ___________
  D5. TOTAL other income (as applicable)          ___________

E. ASSESSABLE INCOME (C + D, excl. final-tax items) ___________

F. LESS: PERSONAL RELIEF (Rs. 1,800,000)          ___________
   (residents / non-resident citizens only)

G. TAXABLE INCOME (E - F, not below 0)            ___________

H. TAX COMPUTATION (pass to deterministic engine)
   Slabs on G: 6% / 18% / 24% / 30% / 36%
  H1. Income tax on slabs                         ___________
  H2. Less: WHT / AIT credits (interest, rent)    ___________
  H3. Less: APIT deducted by employer             ___________
  H4. Less: Self-assessment instalments paid      ___________
  H5. Tax payable / refund                        ___________

REVIEWER FLAGS:
  [ ] Residence status confirmed?
  [ ] Foreign-currency 15% concession assessed?
  [ ] Capital gains (15% from 3 June 2026, 10% before) handled separately?
  [ ] Capital-allowance rates confirmed (Section 5.4 gap)?
  [ ] Home office / vehicle % documented?
  [ ] EPF/ETF employer vs employee split correct?
  [ ] WHT/AIT certificates reconciled?
  [ ] Instalments and APIT credited?
```

### Bank Statement Reading Guide

#### Sri Lankan Bank Statement Formats

**Sri Lankan Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Bank of Ceylon (BOC) | PDF, CSV | Date, Description, Debit, Credit, Balance | State bank; description carries counterparty + reference |
| People's Bank | PDF | Date, Particulars, Withdrawals, Deposits, Balance | State bank; shorter descriptions |
| Commercial Bank (ComBank) | PDF, CSV | Value Date, Description, Amount, Balance | CEFT lines = electronic transfers |
| Hatton National Bank (HNB) | PDF, CSV | Date, Description, Debit, Credit, Balance | Card transactions show merchant |
| Sampath Bank | CSV | Date, Counterparty, Amount, Reference | Clean counterparty names |

#### Key local banking / tax terms

**Key local banking / tax terms table**

| Term | Meaning | Classification hint |
| --- | --- | --- |
| CEFT / SLIPS / LankaPay | Electronic interbank transfer | Check direction for income/expense |
| Standing Order (SO) | Recurring transfer | Regular expense (rent, loan) |
| Direct Debit (DD) | Auto-debit | Utility / subscription expense |
| KULIYA | Rent (Sinhala) | Rental income or office-rent expense |
| MAASIKA | Monthly (pay) | Salary: employment income |
| WHT / AIT | Withholding / advance income tax | Tax credit, gross up income |
| APIT | Advance Personal Income Tax | Employer-deducted advance tax (PAYE-equivalent) |
| EPF / ETF | Provident / Trust Fund | Statutory payroll contribution (Tier 2 catalogue, 6.3 and 6.4) |
| SSCL | Social Security Contribution Levy | Turnover levy, not payroll (`sri-lanka-sscl`) |
| LKR / Rs. | Sri Lankan Rupee | Currency |

### Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Transaction Pattern Library).
2. Mark all Tier 2 items and concession-eligible income as "PENDING: reviewer must confirm".
3. Apply conservative defaults (Boundary and exception table).
4. Generate the working paper (Excel Working Paper Template) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS: SRI LANKA INCOME TAX
1. Residence: resident, non-resident citizen, or non-citizen non-resident?
2. Income source: business/self-employment, employment (APIT), or both?
3. Any foreign-currency service income remitted through a Sri Lankan bank?
4. Any realisation of investment assets (capital gains) this year?
5. Home office: dedicated space? If yes, what % of floor area?
6. Vehicle used for business? What % and is there a mileage log?
7. Telecoms/utilities: what % is business use?
8. Do you employ staff (EPF/ETF obligations)?
9. WHT/AIT deducted on interest, rent, or dividends? Have certificates?
10. APIT deducted by an employer? Self-assessment instalments paid?
11. Are you VAT- or SSCL-registered (turnover near Rs. 60m/Rs. 15m per quarter)?
12. Do you have a TIN?
```


## Completion checklist

- [ ] Residence and citizenship confirmed; relief applied only where allowed
- [ ] Special-rate income separated (investment gains with the sale date, 45%, terminal benefits, 15% remitted income with evidence)
- [ ] Slabs applied to taxable income after relief
- [ ] APIT, WHT and instalment credits deducted
- [ ] Return due date and penalties noted

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the personal relief history (Rs. 1,800,000 for years from 1 April 2025) and the list of amending Acts, with the certification date of Act No. 11 of 2026, on the IRD income tax page | https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Income%20Tax.aspx?menuid=1201 | 2026-11-14 |
| Read for First Schedule paragraphs 1 (individual rates, subparagraphs (1D), (2), (3), (6)) and 2 (partnerships), sections 90, 93, 145, 157, 159, 177 to 180, in the IRD consolidated Act | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf | 2026-11-14 |
| Read for sections 1(2) and (3) (operative dates), 2 (section 8(2)(c)), 12 (section 84(3)(f)), 19 (section 94(1)(d)), 21 (section 96A), 25 (section 113(1D)), 26 (section 135(7)), 31 (section 185A) and 36 (capital gains rates) of the Inland Revenue (Amendment) Act No. 11 of 2026 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf | 2026-11-14 |
| Read for the list of reliefs (rent, solar), the partnership rates, the terminal benefits scale and the withholding table in the IRD tax chart, the latest on the site | https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx | 2026-11-14 |
| Read for the EPF employer and employee rates and the payment deadline used in Example 5 and the tier 2 catalogue, on the EPF Department of the Central Bank of Sri Lanka site | https://epf.lk/?page_id=811 | 2026-11-14 |
| Read for the 3% ETF rate, the employer-only rule and the surcharge scale on the ETF Board employers page | https://etfb.lk/employers-faq/ | 2026-11-14 |

Not yet confirmed: an IRD 2026/27 tax chart (the latest page is the prior year's; the Act's individual rates are unchanged); capital allowance rates and asset classes; how the IRD applies the 15% maximum rate to slab income (this skill caps each slab); the final balance date of 30 September after the year end in the earlier version (the Act read here makes self-assessed tax due on the return due date); the earlier version's claim that the VAT threshold drops to Rs. 36 million from 1 April 2026 (not in VAT Acts No. 4 of 2025 or 14 of 2026, nor in PN/VAT/2025-01); the claim that 10% WHT on interest is a final tax for non-resident citizens (secondary source); gratuity conditions (5 years' service, 15 or more employees, half a month's salary per year) from a secondary source; the Rs. 1,800,000 relief applying to non-resident citizens and not to non-citizen non-residents is taken from the IRD chart wording, not the Act section.
