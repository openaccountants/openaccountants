---
name: sri-lanka-income-tax
description: Use this skill whenever asked about Sri Lanka income tax for individuals, sole proprietors, freelancers, and self-employed people. Trigger on phrases like "how much income tax do I pay in Sri Lanka", "APIT", "PAYE", "personal relief", "Inland Revenue Department", "IRD", "tax year of assessment", "self-assessment instalments", "EPF ETF", "TIN registration", "SET statement of estimated tax", "Asmt_IIT return", "withholding tax interest", "SSCL", "VAT registration Sri Lanka", "freelancer tax LKR", or any question about computing or filing personal income tax for a resident or non-resident-citizen individual in Sri Lanka. Also trigger when classifying LKR bank statement lines, computing EPF/ETF on-costs, or advising on quarterly instalment deadlines. This skill covers the 2025/2026 progressive rates (6%-36%), the Rs. 1,800,000 personal relief, APIT (the employer-deducted advance tax), EPF/ETF/gratuity, the 30 November return deadline, quarterly self-assessment instalments, TIN/VAT/SSCL registration thresholds, and withholding tax on interest/rent/dividends. ALWAYS read this skill before touching any Sri Lanka income tax work.
jurisdiction: LK
domain: international
tax_year: 2025
reviewed_by: Lal kumarasiri
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# sri-lanka-income-tax

## Sri Lanka Income Tax -- Individual / Self-Employed Skill v0.1

> **Tier 2 (research-verified).** Figures are sourced from the Inland Revenue Department (IRD), the EPF (Central Bank of Sri Lanka), the ETF Board, the Ministry of Labour, and Parliament. Items marked **[RESEARCH GAP -- reviewer to confirm]** were not extractable from a primary source at authoring time and MUST be confirmed by a Sri Lankan tax professional before filing.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Democratic Socialist Republic of Sri Lanka |
| Tax | Personal Income Tax (administered by IRD) |
| Currency | Sri Lankan Rupee (LKR / Rs.) only |
| Tax year of assessment (YA) | 1 April -- 31 March (current: YA 2025/2026) |
| Primary legislation | Inland Revenue Act No. 24 of 2017, as amended by Inland Revenue (Amendment) Act No. 02 of 2025 (effective 1 Apr 2025) |
| Tax authority | Inland Revenue Department (IRD), Sri Lanka |
| Filing portal | IRD e-Services (e-filing) |
| Annual return deadline | 30 November following the end of the YA (ss. 93-94, IRA No. 24 of 2017) |
| Personal relief (tax-free) | Rs. 1,800,000 / year (Rs. 150,000 / month) -- IRD PN/IT/2025-01 |
| Validated by | Pending -- requires sign-off by a Sri Lankan tax professional |
| Validation date | Pending |
| Skill version | 0.1 |

### Sri Lanka HAS a personal income tax

- **Progressive personal income tax applies** — Unlike some Gulf jurisdictions, Sri Lanka levies progressive personal income tax on resident individuals and on non-resident citizens. The 2025/2026 rules derive from the Inland Revenue (Amendment) Act No. 02 of 2025, effective 1 April 2025.  _(Inland Revenue (Amendment) Act No. 02 of 2025)_

### Personal Income Tax Brackets (Resident individuals, YA 2025/2026)

- **Personal relief application** — Personal relief: Rs. 1,800,000 / year is deducted from assessable income before the slabs apply. Relief does not apply to gains from realisation of investment assets. Available to residents and non-resident citizens of Sri Lanka (not to non-citizen non-residents).  _(IRD tax chart 2025/2026; IRD Notice PN/IT/2025-01 (26.03.2025))_

**Progressive rates on taxable income after the Rs. 1,800,000 relief**  _(IRD tax chart 2025/2026 -- https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx?menuid=1404 ; IRD PN/IT/2025-01)_

| Slab (taxable income after relief) | Width | Rate | Tax on slab | Cumulative tax at top of slab |
| --- | --- | --- | --- | --- |
| First Rs. 1,000,000 | 1,000,000 | 6% | Rs. 60,000 | Rs. 60,000 |
| Next Rs. 500,000 (1,000,001 -- 1,500,000) | 500,000 | 18% | Rs. 90,000 | Rs. 150,000 |
| Next Rs. 500,000 (1,500,001 -- 2,000,000) | 500,000 | 24% | Rs. 120,000 | Rs. 270,000 |
| Next Rs. 500,000 (2,000,001 -- 2,500,000) | 500,000 | 30% | Rs. 150,000 | Rs. 420,000 |
| Balance (above Rs. 2,500,000) | -- | 36% | -- | -- |

- **Structural changes from 1 Apr 2025** — first slab widened Rs. 500,000 -> Rs. 1,000,000; the former 12% band removed; top rate remains 36%.  _(IRD tax chart 2025/2026; IRD PN/IT/2025-01)_

### Special / concessionary rates (YA 2025/2026)

**Special / concessionary rates**  _(IRD tax chart 2025/2026)_

| Income type | Rate | Source |
| --- | --- | --- |
| Gains on realisation of investment assets (capital gains) | 10% | IRD tax chart 2025/2026 |
| Foreign-source income remitted through a bank | max 15% | IRD tax chart 2025/2026 |
| Service income earned in / remitted via foreign currency through a bank (relevant to IT/freelance exporters) | max 15% | IRD tax chart 2025/2026 |
| Income from betting & gaming, liquor, tobacco | 45% | IRD tax chart 2025/2026 |

### Partnerships (where a self-employed person trades in partnership)

- **Partnership taxation** — Taxed at the partnership level: taxable income up to Rs. 1,000,000 at 0%; excess at 6%; partnership investment-asset gains at 10%. Partners' shares are then exempt at the individual level.  _(IRD tax chart 2025/2026 -- https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx?menuid=1404)_

### Payroll contributions (EPF / ETF) -- summary

**EPF/ETF contribution table**  _(EPF (CBSL) Employer FAQ -- https://epf.lk/?page_id=811 ; ETF Board Employers FAQ -- https://etfb.lk/employers-faq/)_

| Contribution | Employee | Employer | Total |
| --- | --- | --- | --- |
| EPF (Employees' Provident Fund) | 8% | 12% | 20% |
| ETF (Employees' Trust Fund) | 0% | 3% | 3% |
| **Total of contributions** | **8%** | **15%** | **23%** |

- **Total typical employer on-cost** — Total typical employer on-cost over gross = 15% (EPF 12% + ETF 3%), plus gratuity provisioning.  _(EPF (CBSL) Employer FAQ; ETF Board Employers FAQ)_

### Conservative Defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown residence status | STOP -- relief and rates differ for non-citizen non-residents |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether income is foreign-source remitted via bank | Treat as ordinary income (progressive rates), flag for reviewer |
| Unknown whether person is an instalment payer | Assume instalment payer if any business / self-employment income |
| Unknown VAT registration status | Assume not registered; flag if turnover near threshold |
| Unknown gratuity entitlement | Flag -- depends on years of service and employer size |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable / Recommended / Ideal / Refusal** — Minimum viable -- bank statement for the full year of assessment (1 Apr -- 31 Mar) in CSV, PDF, or pasted text, plus confirmation of residence status (resident / non-resident citizen / non-citizen non-resident) and source of income (employment APIT, self-employment/business, or both). Recommended -- sales invoices, purchase invoices/receipts, EPF/ETF contribution records, prior-year return or assessment, APIT certificate(s) from employer(s), withholding/AIT certificates (interest, rent, dividends), TIN. Ideal -- complete income and expenditure statement, asset register, Statement of Estimated Tax (SET) and quarterly instalment receipts, foreign-currency remittance evidence (for the 15% concession). Refusal if minimum is missing -- SOFT WARN. No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This computation was produced from a bank statement alone. The reviewer must verify all deductions are supported by valid documentation and that income source classifications (especially foreign-currency concessions and capital gains) are correct."

### Refusal Catalogue

- **R-LK-1** — Residence status unknown. "Residence status determines whether the Rs. 1,800,000 personal relief applies and which rates are used. A non-citizen non-resident does not get the relief; a non-resident citizen does. This skill cannot compute tax without it. Please confirm."
- **R-LK-2** — Companies / partnerships filing. "This skill covers individuals and sole proprietors. Partnership-level returns and company income tax (corporate rates) are out of scope -- escalate to a Sri Lankan tax professional."
- **R-LK-3** — Investment-asset (capital) gains. "Gains on realisation of investment assets are taxed at 10% and the personal relief does NOT apply to them. The base computation requires asset cost, proceeds, and dates. Escalate to a reviewer for capital gains."
- **R-LK-4** — Foreign-source / foreign-currency concessions. "The max-15% concessions for foreign-source income or foreign-currency service income remitted through a bank depend on remittance evidence and bank routing. Flag and escalate -- do not apply the 15% cap without confirmation."
- **R-LK-5** — Arrears / enforcement / penalties. "Client has outstanding tax, EPF/ETF arrears, or is subject to IRD enforcement. Escalating surcharges (EPF/ETF up to 50%) and income-tax penalties/interest apply. Escalate to a Sri Lankan tax professional immediately."
- **R-LK-6** — VAT / SSCL return requested. "This skill covers personal income tax only. VAT and the Social Security Contribution Levy (SSCL) are separate turnover taxes -- see Section 10 for thresholds, then use the relevant indirect-tax skill."

## Section 3 -- Transaction Pattern Library

Deterministic pre-classifier. When a bank-statement transaction matches a pattern below, apply the treatment directly. Match by case-insensitive substring on the counterparty name or description as it appears on the statement. If multiple match, use the most specific. If none match, fall through to Tier 1 rules in Section 5. Local-language (Sinhala/Tamil transliteration and English) terms are included.

### 3.1 Income Patterns (Credits)

**Income Patterns (Credits)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFER, DEPOSIT, PAYMENT RECEIVED | Business income | If VAT-registered, extract net (excl. 18% VAT) |
| FEES, PROFESSIONAL FEES, CONSULTANCY, SERVICE CHARGE | Business income | Typical self-employment fee |
| STRIPE PAYOUT, PAYONEER, WISE, PAYPAL | Business income (often foreign-currency service income) | May qualify for max-15% concession -- FLAG, do not auto-apply |
| UPWORK, FIVERR, TOPTAL, FREELANCER | Business income | Freelance platform; net of platform commission; often foreign-currency -- FLAG concession |
| SALARY, SALARIES, EMP [name], MAASIKA (monthly pay) | Employment income | Subject to APIT at source -- reconcile to APIT certificate |
| RENT RECEIVED, KULIYA (rent) | Rental income | 10% AIT applies if rent > Rs. 100,000/month to resident individual |
| INTEREST, INTERESSI, FD INTEREST, SAVINGS INT | Investment income | 10% WHT/AIT deducted at source |
| DIVIDEND, DIVIDENDS | Investment income | 15% final WHT |
| IRD REFUND, TAX REFUND | EXCLUDE | Refund of prior-year tax, not income |
| GOVERNMENT GRANT, RELIEF GRANT | Check nature | Capital grants EXCLUDE; revenue grants = business income |

### 3.2 Expense Patterns (Debits) -- Deductible business expenses

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
| DOMAIN, HOSTING, AWS, AZURE, DIGITALOCEAN | IT infrastructure | Deductible | Capitalise if a long-lived asset -- see 3.5 |

### 3.3 Expense Patterns (Debits) -- SaaS / software subscriptions

**SaaS / software subscriptions**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |

### 3.4 Expense Patterns (Debits) -- Utilities (apportion if mixed)

**Utilities**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| CEB, LECO, ELECTRICITY BILL | Electricity | T2 if home office | 100% if dedicated office; proportional if home; default 0% |
| WATER BOARD, NWSDB | Water | T2 if home office | Same apportionment rule |
| DIALOG, MOBITEL, SLT, HUTCH, AIRTEL | Telecoms / broadband | T2 | Business-use portion only; default 0% if mixed |

### 3.5 Expense Patterns (Debits) -- Capital / depreciable assets

**Capital / depreciable assets**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTER, MACBOOK, DESKTOP | Computer hardware | Capital allowance (depreciation) | Do NOT fully expense; see Section 5.4 [RESEARCH GAP -- confirm rate] |
| PRINTER, SCANNER, COPIER | Office equipment | Capital allowance | [RESEARCH GAP -- confirm rate] |
| FURNITURE, DESK, CHAIR | Furniture/fittings | Capital allowance | [RESEARCH GAP -- confirm rate] |
| VEHICLE, CAR (business) | Motor vehicle | Capital allowance, business % only | [RESEARCH GAP -- confirm rate] |

### 3.6 Expense Patterns (Debits) -- NOT deductible

**NOT deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANT, ENTERTAINMENT, CLIENT MEAL | Entertainment | NOT deductible | Private / non-business |
| GROCERIES, SUPERMARKET, KEELLS, CARGILLS, ARPICO | Personal | NOT deductible | Private living costs |
| FINE, PENALTY, SURCHARGE | Fines/penalties | NOT deductible | Public policy |
| INCOME TAX, IRD PAYMENT, SELF-ASSESSMENT TAX | Tax payments | NOT deductible | Income tax cannot reduce income |
| DRAWINGS, PERSONAL WITHDRAWAL | Drawings | NOT deductible | Not an expense |

### 3.7 Exclusions and special routing (neither ordinary income nor expense)

**Exclusions and special routing**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| OWN ACCOUNT, INTERNAL TRANSFER, BETWEEN ACCOUNTS | EXCLUDE | Own-account transfer |
| LOAN, LOAN REPAYMENT (principal) | EXCLUDE | Capital movement (interest may be deductible if business) |
| EPF, ETF, PROVIDENT FUND | EXCLUDE from income tax expense | Statutory contribution -- see Section 6.3 |
| VAT PAYMENT, SSCL PAYMENT | EXCLUDE | Indirect-tax liability, not an income-tax expense |
| SELF-ASSESSMENT INSTALMENT, QUARTERLY TAX | Credit against liability | Not an expense -- it is tax paid on account |

### 3.8 Sri Lankan Banks -- Statement Format Reference

**Sri Lankan Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Bank of Ceylon (BOC) | TRANSFER, SLIP, STANDING ORDER, CHARGES | PDF/CSV; date DD/MM/YYYY |
| People's Bank | DEPOSIT, WITHDRAWAL, DD, CHARGE | PDF; description carries counterparty |
| Commercial Bank (ComBank) | FUND TRANSFER, CEFT, SLIPS, FEE | CSV/PDF; CEFT = electronic transfer |
| Hatton National Bank (HNB) | TRANSFER, SO, DD, COMMISSION | PDF/CSV |
| Sampath Bank | SLIPS, ONLINE TRF, CHARGE | CSV; clean counterparty names |

## Section 4 -- Worked Examples

### Example 1 -- Local client payment (not VAT-registered)

Input line:
`14/06/2025 ; BOC FUND TRANSFER IN ; PERERA TRADING (PVT) LTD ; INV-2025-021 ; +250,000.00 ; LKR`

Reasoning:
Local fee for services. Client is below VAT threshold and not registered, so the full Rs. 250,000 is business income. No VAT to strip out.

Classification: Business income = Rs. 250,000.

### Example 2 -- Foreign-currency freelance payout (concession FLAG)

Input line:
`28/06/2025 ; COMBANK CEFT ; PAYONEER INC ; USD SERVICE PAYOUT ; +480,000.00 ; LKR`

Reasoning:
Service income earned in / remitted via foreign currency through a bank may qualify for the max-15% concession (IRD tax chart 2025/2026). This is reviewer judgement -- it depends on remittance routing and documentation. Do NOT auto-apply the 15% cap. Default: include Rs. 480,000 as business income at progressive rates and FLAG for the reviewer to assess the concession.

Classification: Business income = Rs. 480,000. FLAG -- possible 15% foreign-currency-service concession (R-LK-4).

### Example 3 -- Bank interest with 10% WHT deducted

Input line:
`30/09/2025 ; HNB ; FD INTEREST CREDIT ; NET OF WHT ; +90,000.00 ; LKR`

Reasoning:
Interest and discount income carries 10% WHT/AIT at source from 1 Apr 2025 (up from 5%). If the credit is shown net of WHT, gross it up: Rs. 90,000 / 0.90 = Rs. 100,000 gross, with Rs. 10,000 WHT credit. For a resident with total annual income above Rs. 1,800,000, interest is included; the 10% deducted is a credit against the final liability. For a non-resident citizen, the 10% on bank interest is a final tax (not added to the progressive computation).
Source: IRD tax chart 2025/2026; https://www.taxadvisor.lk/article/ntri

Classification: Investment income gross = Rs. 100,000; WHT credit = Rs. 10,000. (Confirm whether net or gross is shown on the statement.)

### Example 4 -- SaaS subscription (deductible)

Input line:
`01/07/2025 ; SAMPATH ONLINE ; ADOBE SYSTEMS ; CREATIVE CLOUD ; -9,500.00 ; LKR`

Reasoning:
Recurring software subscription used in the business. Fully deductible operating expense.

Classification: Deductible expense = Rs. 9,500.

### Example 5 -- EPF/ETF remittance by a sole proprietor with staff

Input line:
`31/07/2025 ; BOC STANDING ORDER ; EPF DEPARTMENT ; JUN 2025 CONTRIB ; -160,000.00 ; LKR`

Reasoning:
This is the employer EPF remittance for staff (employee 8% + employer 12%). The employer share is a deductible business cost; the employee share was withheld from staff salaries and is not the proprietor's own expense. EPF must be remitted on or before the last working day of the following month. Do NOT classify as the proprietor's personal income-tax deduction line -- it sits in the payroll-cost computation. FLAG to confirm the employer/employee split.
Source: EPF (CBSL) Employer FAQ -- https://epf.lk/?page_id=811

Classification: Payroll cost (employer share deductible). FLAG -- confirm employer vs employee split.

### Example 6 -- Full-year resident self-employed computation

Inputs (resident individual, YA 2025/2026):
Gross business income Rs. 4,000,000; allowable business expenses Rs. 1,200,000. No other income, no capital gains, no foreign-currency concession.

Step 1 -- Net profit (assessable income): 4,000,000 - 1,200,000 = Rs. 2,800,000.

Step 2 -- Apply personal relief: 2,800,000 - 1,800,000 = Rs. 1,000,000 taxable income.

Step 3 -- Apply slabs: taxable income Rs. 1,000,000 falls entirely in the first slab (first Rs. 1,000,000 @ 6%).
Tax = 1,000,000 x 6% = Rs. 60,000.

Classification: Taxable income Rs. 1,000,000; income tax due Rs. 60,000 (before any WHT/instalment credits).

### Example 7 -- Higher-income resident hitting multiple slabs

Inputs (resident individual, YA 2025/2026):
Net profit (after expenses) Rs. 5,300,000. No other income.

Step 1 -- Apply relief: 5,300,000 - 1,800,000 = Rs. 3,500,000 taxable income.

Step 2 -- Apply slabs:
- First 1,000,000 @ 6% = 60,000
- Next 500,000 @ 18% = 90,000 (cumulative 150,000)
- Next 500,000 @ 24% = 120,000 (cumulative 270,000)
- Next 500,000 @ 30% = 150,000 (cumulative 420,000)
- Remaining 1,000,000 (3,500,000 - 2,500,000) @ 36% = 360,000

Total = 420,000 + 360,000 = Rs. 780,000.

Classification: Taxable income Rs. 3,500,000; income tax due Rs. 780,000 (before credits).

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 The wholly-and-exclusively / business-nexus test

- **Business-nexus test** — An expense is deductible only if incurred in producing the business income. Mixed-use expenses must be apportioned on a reasonable, documented basis. Domestic/private expenses are not deductible.  _(Inland Revenue Act No. 24 of 2017 (deductions provisions))_

### 5.2 Income recognition

- **Income recognition** — All business income goes into assessable income. Where the individual is VAT-registered, report income net of the 18% VAT collected (VAT is a liability to IRD, not income). Employment income subject to APIT is included but reconciled against the APIT certificate (the APIT already deducted is a credit).

### 5.3 Personal relief

- **Personal relief application detail** — Deduct Rs. 1,800,000/year from assessable income before applying the slabs (residents and non-resident citizens only). Relief does NOT apply against investment-asset gains. Monthly equivalent Rs. 150,000 is used in APIT.  _(IRD PN/IT/2025-01 (26.03.2025))_

### 5.4 Capital allowances (depreciation)

- **Capital allowances research gap** — Capital assets are not fully expensed in year one; they are written off over time via capital allowances under the Inland Revenue Act No. 24 of 2017. [RESEARCH GAP -- reviewer to confirm the current per-class capital-allowance rates and the depreciable-asset classes under IRA No. 24 of 2017 before applying any depreciation figure.] Until confirmed, flag every capital asset for reviewer treatment rather than guessing a rate.  _(Inland Revenue Act No. 24 of 2017)_

### 5.5 Concessionary rates (apply only when conditions are met)

**Concessionary rates**  _(IRD tax chart 2025/2026 -- https://www.ird.gov.lk/en/publications/SitePages/tax_chart_2526.aspx?menuid=1404)_

| Income | Rate | Condition |
| --- | --- | --- |
| Investment-asset gains | 10% | Realisation of an investment asset; relief does not apply |
| Foreign-source income remitted via a bank | max 15% | Remittance through a bank; documented |
| Foreign-currency service income via a bank | max 15% | Service income earned in / remitted via foreign currency through a bank |
| Betting & gaming, liquor, tobacco income | 45% | Specified activities |

### 5.6 Withholding / Advance Income Tax (AIT) credits

**WHT/AIT credits table**  _(IRD tax chart 2025/2026; taxadvisor.lk/ntri)_

| Income | Rate | Notes | Source |
| --- | --- | --- | --- |
| Interest & discount | 10% WHT/AIT | Up from 5% (1 Apr 2025). Individuals with total annual income below Rs. 1.8m may apply for exemption. For non-resident citizens, 10% on bank interest is a final tax. | IRD tax chart 2025/2026; taxadvisor.lk/ntri |
| Rent | 10% AIT | Where rent to a resident individual exceeds Rs. 100,000/month | IRD tax chart 2025/2026 |
| Dividends | 15% final WHT | Resident companies to shareholders | IRD tax chart 2025/2026 |
| Non-resident payments | per DTAA | May be reduced under an applicable double-tax treaty | taxadvisor.lk/ntri |

- **WHT/AIT credit treatment** — WHT/AIT already deducted is a credit against the final income-tax liability (except where stated to be a final tax).

### 5.7 Non-deductible expenses

**Non-deductible expenses table**

| Expense | Reason |
| --- | --- |
| Entertainment / private meals | Not in production of income |
| Personal living expenses, drawings | Private |
| Fines and penalties | Public policy |
| Income tax itself | Tax on income |
| Capital expenditure | Recovered via capital allowances, not expensed |

### 5.8 Filing and payment

**Filing and payment table**  _(IRD Tax Calendar -- https://www.ird.gov.lk/en/publications/sitepages/tax%20calendar.aspx ; Asmt_IIT guide -- https://www.ird.gov.lk/en/Downloads/IT_Individuals_Doc/Asmt_IIT_004_2023_2024_E.pdf ; SET guide -- https://www.ird.gov.lk/ta/Downloads/IT_SET_Doc/SET_25_26_Detail_Guide_E.pdf)_

| Item | Detail | Source |
| --- | --- | --- |
| Year of assessment | 1 April -- 31 March | IRA No. 24 of 2017 |
| Annual return deadline | 30 November following YA end | IRD; ss. 93-94 IRA |
| Return form | Asmt_IIT (Return of Income for individuals) | IRD forms portal |
| Filing method | IRD e-Services (e-filing) | IRD |
| Statement of Estimated Tax (SET) | Required from instalment payers | IRD SET guide 2025/26 |

### 5.9 Quarterly self-assessment (instalment) payments (s. 90 IRA)

**Quarterly instalment schedule**  _(IRD Tax Calendar 2025 -- https://www.ird.gov.lk/en/publications/Tax%20Calendar_Documents/Tax_Calender_2025_E.pdf ; 2026 -- https://www.ird.gov.lk/en/publications/Tax%20Calendar_Documents/Tax_Calendar_2026_E.pdf)_

| Instalment | Period covered | Due date |
| --- | --- | --- |
| 1st | Apr -- Jun | 15 August |
| 2nd | Jul -- Sep | 15 November |
| 3rd | Oct -- Dec | 15 February |
| 4th | Jan -- Mar | 15 May |
| Final balance payment | Whole YA | 30 September after year-end |

### 5.10 Penalties (selected)

**Penalties table**

| Item | Charge | Source |
| --- | --- | --- |
| Late instalment payment | 10% penalty on unpaid instalment if not paid within 14 days of due date (s.179(2)), plus interest 1.5%/month from due date (s.157(1)) | [RESEARCH GAP -- secondary source (simplebooks.com citing IRA No. 24 of 2017); confirm section numbers against the Act] |
| Late / non-filing of return | Statutory penalties / legal action under IRA No. 24 of 2017 | IRD notice via dailymirror.lk |
| EPF / ETF late payment | Escalating surcharge 5% -> 50% (see Section 6) | epf.lk; etfb.lk |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required) + Payroll Contributions

### 6.1 Home office deduction

- **Home office deduction rules** — - Calculate the proportion of the home used wholly for business (dedicated room / floor area). - Apply that percentage to rent, electricity (CEB/LECO), water (NWSDB), broadband. - A dual-use room does not qualify. Conservative default: 0% until reviewer confirms a dedicated workspace and basis. Flag for reviewer: confirm room/floor-area basis and that the space is genuinely dedicated.

### 6.2 Motor vehicle business use

- **Motor vehicle business use rules** — - Only the business-use percentage of fuel, insurance, maintenance and depreciation is deductible. - Requires a mileage log. Conservative default: 0% business use until a log is provided. Flag for reviewer: confirm business percentage and capital-allowance rate (see Section 5.4 research gap).

### 6.3 EPF -- Employees' Provident Fund

- **EPF rules** — - Employee: 8% of total monthly earnings (withheld from salary). - Employer: 12% of total monthly earnings. - Total: 20%. No statutory salary ceiling/floor on the percentage (applies to "total earnings"). - Remit on or before the last working day of the following month. - Late surcharge (escalating on the contribution): 1-10 days 5%; 11 days-1 month 15%; 1-3 months 20%; 3-6 months 30%; 6-12 months 40%; over 12 months 50%. Plus 2% surcharge for incomplete details.  _(EPF (CBSL) Employer FAQ -- https://epf.lk/?page_id=811 ; CBSL -- https://www.cbsl.gov.lk/en/employees-provident-fund)_

### 6.4 ETF -- Employees' Trust Fund

- **ETF rules** — - Employer: 3% of total monthly earnings. Employee: nil -- the employer may not deduct ETF from the employee. - Remit on or before the last working day of the succeeding month. - Late surcharge: same escalating 5% -> 50% scale; late half-yearly returns add a 1% surcharge per delayed month on face value.  _(ETF Board Employers FAQ -- https://etfb.lk/employers-faq/)_

### 6.5 Gratuity

- **Gratuity rules** — - Payable on termination to employees with 5+ years of service, at half a month's salary per year of service. - Applies to employers with 15+ employees. [RESEARCH GAP -- exact formula and employee-count threshold taken from a secondary source (simplebooks.com); confirm against the Payment of Gratuity Act text before relying on it.]  _(Payment of Gratuity Act No. 12 of 1983)_

### 6.6 Foreign-currency / foreign-source concession (max 15%)

- **Foreign-currency concession rule** — The max-15% rate on foreign-source income, or service income earned in/remitted via foreign currency through a bank, depends on remittance routing and documentation. Conservative default: apply ordinary progressive rates and FLAG; do not auto-apply 15% (R-LK-4).

### 6.7 Bad debt write-off

- **Bad debt write-off rule** — Deductible only if the income was previously brought to account, recovery steps were taken, and the debt is genuinely irrecoverable. Flag for reviewer to confirm all three.

## Section 7 -- Excel Working Paper Template

```
SRI LANKA INCOME TAX -- INDIVIDUAL WORKING PAPER
Year of Assessment: 2025/2026 (1 Apr 2025 - 31 Mar 2026)
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
  [ ] Capital gains (10%) handled separately?
  [ ] Capital-allowance rates confirmed (Section 5.4 gap)?
  [ ] Home office / vehicle % documented?
  [ ] EPF/ETF employer vs employee split correct?
  [ ] WHT/AIT certificates reconciled?
  [ ] Instalments and APIT credited?
```

## Section 8 -- Bank Statement Reading Guide

### Sri Lankan Bank Statement Formats

**Sri Lankan Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Bank of Ceylon (BOC) | PDF, CSV | Date, Description, Debit, Credit, Balance | State bank; description carries counterparty + reference |
| People's Bank | PDF | Date, Particulars, Withdrawals, Deposits, Balance | State bank; shorter descriptions |
| Commercial Bank (ComBank) | PDF, CSV | Value Date, Description, Amount, Balance | CEFT lines = electronic transfers |
| Hatton National Bank (HNB) | PDF, CSV | Date, Description, Debit, Credit, Balance | Card transactions show merchant |
| Sampath Bank | CSV | Date, Counterparty, Amount, Reference | Clean counterparty names |

### Key local banking / tax terms

**Key local banking / tax terms table**

| Term | Meaning | Classification hint |
| --- | --- | --- |
| CEFT / SLIPS / LankaPay | Electronic interbank transfer | Check direction for income/expense |
| Standing Order (SO) | Recurring transfer | Regular expense (rent, loan) |
| Direct Debit (DD) | Auto-debit | Utility / subscription expense |
| KULIYA | Rent (Sinhala) | Rental income or office-rent expense |
| MAASIKA | Monthly (pay) | Salary -- employment income |
| WHT / AIT | Withholding / advance income tax | Tax credit, gross up income |
| APIT | Advance Personal Income Tax | Employer-deducted advance tax (PAYE-equivalent) |
| EPF / ETF | Provident / Trust Fund | Statutory payroll contribution (Section 6) |
| SSCL | Social Security Contribution Levy | Turnover tax, not payroll (Section 10) |
| LKR / Rs. | Sri Lankan Rupee | Currency |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items and concession-eligible income as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- SRI LANKA INCOME TAX
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

## Section 10 -- Reference Material

### Registration thresholds

**Registration thresholds table**

| Item | Threshold | Source |
| --- | --- | --- |
| TIN / income-tax registration | Required for all individuals liable above the Rs. 1,800,000 relief, and all instalment payers, business owners, sole proprietors, partners | IRD -- https://www.ird.gov.lk/en/sitepages/default.aspx |
| VAT registration | Turnover > Rs. 60 million / year OR > Rs. 15 million in any taxable period (quarter); register within 15 days of exceeding; standard rate 18% | IRD VAT page -- https://www.ird.gov.lk/en/type%20of%20taxes/sitepages/value%20added%20tax%20(vat).aspx ; PN/VAT/2025-01 |
| VAT threshold change | Drops to Rs. 36 million / year from 1 April 2026 (Budget 2026) | IRD PN/VAT/2025-01 -- https://www.ird.gov.lk/en/Lists/Latest%20News%20%20Notices/Attachments/677/PN_VAT_2025-01_11042025_E.pdf |
| VAT on non-resident digital services | Register if Rs. 60m/12 months or Rs. 15m/3 months; 18% VAT on digital services from 1 Oct 2025 | IRD PN/VAT/2025-01 |
| SSCL (Social Security Contribution Levy) | Rate 2.5% of liable turnover; register if quarterly turnover > Rs. 15 million, or > Rs. 60 million across any 4 consecutive quarters | IRD SSCL page -- https://www.ird.gov.lk/en/Type%20of%20Taxes/SitePages/Social%20Security%20Contribution%20Levy%20(SSCL).aspx |
| SSCL amendment | SSCL (Amendment) Act No. 24 of 2025 (financial-services exemption from 1 Jan 2026; fuel clarified from 1 Jul 2025) | KPMG -- https://kpmg.com/us/en/taxnewsflash/news/2025/10/sri-lanka-amendments-social-security-contribution-levy-law.html |

### Minimum wage (from 1 April 2025)

**Minimum wage table**  _(Ministry of Labour -- https://labourmin.gov.lk/heres-how-the-private-sector-minimum-wage-is-set-to-rise/ ; National Minimum Wage (Amendment) Act -- https://www.parliament.lk/uploads/acts/gbills/english/6388.pdf)_

| Item | Value | Source |
| --- | --- | --- |
| National minimum monthly wage | Rs. 27,000 / month (up from Rs. 21,000) | Ministry of Labour; National Minimum Wage (Amendment) Act |
| National minimum daily wage | Rs. 1,080 / day (up from Rs. 700) | Ministry of Labour |
| Confirmed future increase | Rs. 30,000 / month and Rs. 1,200 / day from January 2026 | Ministry of Labour |

### APIT (Advance Personal Income Tax -- the PAYE-equivalent)

- **APIT definition** — APIT is the employer-deducted advance tax on employment income (replaced "PAYE"). Employers deduct monthly and remit to IRD. Monthly tax-free allowance Rs. 150,000 mirrors the annual Rs. 1,800,000 relief; the same 6%-36% slabs apply on a monthly-equivalent basis. [RESEARCH GAP -- reviewer to confirm the per-row monthly APIT figures.] The IRD APIT Table 1 PDF could not be machine-extracted at authoring time. The monthly bands derive arithmetically from the annual slabs (relief Rs. 150,000/month; first Rs. 83,333/month at 6%, etc.), but the authoritative monthly cut-by-cut figures must be taken directly from the IRD Table 1 PDF.  _(IRD APIT Table 1 2025/2026 -- https://www.ird.gov.lk/en/publications/APIT_Tax_Tables/2025-2026/Table%20-%201/02.%20APIT_2526_Table_01_Text.pdf ; IRD APIT Guideline 2025/2026 -- https://www.ird.gov.lk/en/publications/APIT_Tax_Tables/2025-2026/Guide/APIT_2526_Guideline.pdf)_

### Key legislation / authority references

**Key legislation / authority references table**

| Topic | Reference |
| --- | --- |
| Income tax (rates, relief, deductions) | Inland Revenue Act No. 24 of 2017, as amended by Act No. 02 of 2025 |
| Filing / assessment | IRA ss. 93-94 (return); s. 90 (instalments) |
| Penalties / interest | IRA s. 157(1), s. 179(2) [RESEARCH GAP -- confirm section numbers] |
| EPF | Employees' Provident Fund Act; EPF (CBSL) |
| ETF | Employees' Trust Fund Act; ETF Board |
| Gratuity | Payment of Gratuity Act No. 12 of 1983 [RESEARCH GAP] |
| VAT | Value Added Tax Act; IRD VAT page |
| SSCL | Social Security Contribution Levy Act, as amended by Act No. 24 of 2025 |
| Minimum wage | National Minimum Wage of Workers Act (as amended) |

### Test Suite

Test 1 -- Slab boundary, single slab.
Input: Resident, net profit Rs. 2,800,000, no other income.
Expected: relief 1,800,000 -> taxable 1,000,000; tax = 1,000,000 x 6% = Rs. 60,000.

Test 2 -- Multiple slabs.
Input: Resident, net profit Rs. 5,300,000.
Expected: taxable 3,500,000; tax = 60,000 + 90,000 + 120,000 + 150,000 + (1,000,000 x 36% = 360,000) = Rs. 780,000.

Test 3 -- Below relief, no tax.
Input: Resident, net profit Rs. 1,500,000.
Expected: 1,500,000 - 1,800,000 < 0 -> taxable Rs. 0; income tax = Rs. 0.

Test 4 -- Top slab reached exactly.
Input: Resident, net profit Rs. 4,300,000 -> taxable 2,500,000.
Expected: cumulative tax at top of 30% slab = Rs. 420,000; nothing in the 36% band; tax = Rs. 420,000.

Test 5 -- Interest gross-up with WHT credit.
Input: FD interest credited net Rs. 90,000 (10% WHT withheld).
Expected: gross = 90,000 / 0.90 = Rs. 100,000; WHT credit Rs. 10,000 against liability (or final tax if non-resident citizen).

Test 6 -- EPF/ETF employer on-cost.
Input: Monthly gross payroll Rs. 1,000,000 for staff.
Expected: EPF employer 12% = Rs. 120,000; ETF employer 3% = Rs. 30,000; employer on-cost = Rs. 150,000 (15%). Employee EPF 8% = Rs. 80,000 withheld from staff. Total contributions remitted relating to EPF = Rs. 200,000 (20%).

Test 7 -- Foreign-currency concession FLAG.
Input: Payoneer service payout Rs. 480,000 to a freelancer.
Expected: include as business income at progressive rates by default; FLAG for reviewer to assess the max-15% foreign-currency-service concession. Do NOT auto-apply 15%.

## PROHIBITIONS

- NEVER apply the Rs. 1,800,000 personal relief to a non-citizen non-resident, or against investment-asset gains.
- NEVER auto-apply the max-15% foreign-currency / foreign-source concession -- it requires reviewer confirmation of remittance routing.
- NEVER fully expense a capital asset -- it is recovered via capital allowances (and the rate is a [RESEARCH GAP] pending confirmation).
- NEVER treat EPF/ETF as the proprietor's personal income-tax deduction without separating employer vs employee share.
- NEVER include VAT collected on sales as income for a VAT-registered person.
- NEVER allow entertainment, fines/penalties, drawings, or income tax itself as a deduction.
- NEVER reproduce the monthly APIT table figures as authoritative -- they are a [RESEARCH GAP] until taken from the IRD Table 1 PDF.
- NEVER use current-year income for instalments without reconciling to the Statement of Estimated Tax.
- NEVER present tax calculations as definitive -- always label as estimated, pending reviewer sign-off.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
