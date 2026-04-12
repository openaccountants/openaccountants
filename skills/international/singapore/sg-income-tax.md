---
name: sg-income-tax
description: >
  Use this skill whenever asked about Singapore income tax for self-employed individuals. Trigger on phrases like "how much tax do I pay in Singapore", "Form B", "Form B1", "IRAS income tax", "trade income", "capital allowances Singapore", "personal reliefs", "tax residence 183 days", "Section 10(1)(a)", "CPF self-employed", "self-employed tax Singapore", "myTax Portal", "DBS Bank statement", "OCBC income", "PayNow transfer", "Stripe Singapore", or any question about filing or computing income tax for a Singapore sole proprietor or freelancer. This skill covers progressive rates (0--24%), trade income computation, capital allowances (Section 19/19A), approved deductions, personal reliefs, CPF MediSave, tax residence rules, filing deadlines, and penalties. ALWAYS read this skill before touching any Singapore income tax work.
version: 2.0
jurisdiction: SG
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Singapore Income Tax -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Singapore |
| Tax | Income Tax (progressive 0--24%) |
| Currency | SGD only |
| Tax year basis | Preceding year: YA 2026 = income earned in calendar year 2025 |
| Primary legislation | Income Tax Act 1947 (ITA) |
| Tax authority | Inland Revenue Authority of Singapore (IRAS) |
| Filing portal | myTax Portal (mytax.iras.gov.sg) via Singpass |
| Filing deadline | 18 April of the YA (e.g., 18 April 2026 for YA 2026) |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by an Accredited Tax Adviser (Singapore) |
| Skill version | 2.0 |

### Progressive Rate Table -- YA 2026 (Income Earned 2025) [T1]

| Chargeable Income (SGD) | Rate | Gross Tax Payable (Cumulative) |
|---|---|---|
| First 20,000 | 0% | 0 |
| Next 10,000 (20,001--30,000) | 2% | 200 |
| Next 10,000 (30,001--40,000) | 3.5% | 550 |
| Next 40,000 (40,001--80,000) | 7% | 3,350 |
| Next 40,000 (80,001--120,000) | 11.5% | 7,950 |
| Next 40,000 (120,001--160,000) | 15% | 13,950 |
| Next 40,000 (160,001--200,000) | 18% | 21,150 |
| Next 40,000 (200,001--240,000) | 19% | 28,750 |
| Next 40,000 (240,001--280,000) | 19.5% | 36,550 |
| Next 40,000 (280,001--320,000) | 20% | 44,550 |
| Next 180,000 (320,001--500,000) | 22% | 84,150 |
| Next 500,000 (500,001--1,000,000) | 23% | 199,150 |
| Above 1,000,000 | 24% | -- |

### Key Thresholds [T1]

| Item | Amount (SGD) |
|---|---|
| Personal relief cap | 80,000 per YA |
| GST registration threshold | 1,000,000 taxable turnover |
| Section 19A(10A) low-value asset cap | 30,000 per YA (individual assets < 5,000 each) |
| Must-file threshold | Taxable income > 22,000 or self-employed with net trade income |
| CPF MediSave (self-employed) | Mandatory based on net trade income and age |

### Conservative Defaults [T1]

| Ambiguity | Default |
|---|---|
| Tax residence unknown | STOP -- do not compute |
| GST status unknown | Non-GST registered (report gross including any GST component) |
| Vehicle type unknown | Private car (S-plate) -- NO capital allowances |
| Business vs capital expenditure unclear | Capital (no deduction until confirmed as revenue) |
| Home office apportionment unknown | 0% deduction until confirmed |
| Personal relief amounts unknown | Apply only confirmed reliefs |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the full calendar year (January--December) in CSV, PDF, or pasted text, plus confirmation of tax residence status and whether GST-registered.

**Recommended:** All client invoices, CPF contribution statements (for MediSave), SRS contribution statements, life insurance and course fee receipts (for reliefs).

**Ideal:** Capital asset register, prior year NOA (Notice of Assessment), Form IR8A (if also employed), GST returns (if GST-registered).

### Refusal Catalogue

**R-SG-1 -- Non-residents.** "Non-resident self-employment income from Singapore is taxable but at different rates. Non-resident computation is outside this skill scope. Escalate."

**R-SG-2 -- Companies (Pte Ltd, Ltd).** "Corporate income tax (CIT at 17%) and corporate filing are out of scope. This skill covers individual self-employed persons only."

**R-SG-3 -- Partnerships.** "Partnership income allocation determination is outside this skill scope. Escalate."

**R-SG-4 -- Capital gains / property disposals.** "Gains from property that are revenue in nature require specialist review. Escalate."

**R-SG-5 -- GST computation.** "GST registration, return filing, and input tax claims are outside this skill scope."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement line matches a pattern, apply the treatment directly. If no pattern matches, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| FAST [client name] / FAST CREDIT | Trade income (Section 10(1)(a)) | Gross revenue | Local fast payment from business client |
| PayNow [sender name] / PAYNOW CREDIT | Trade income | Revenue | PayNow (linked to NRIC/UEN) -- electronic payment |
| GIRO CREDIT [client] | Trade income | Revenue | GIRO standing instruction payment from client |
| TT FROM [client] / TELEGRAPHIC TRANSFER | Trade income | Revenue | Overseas client wire transfer |
| STRIPE PAYOUT SG / STRIPE TRANSFER | Trade income | Revenue | Stripe Singapore payout -- net of Stripe fees |
| WISE TRANSFER IN / WISE CREDIT | Trade income | Revenue | Wise (formerly TransferWise) international payout |
| PAYPAL SG TRANSFER / PAYPAL CREDIT | Trade income | Revenue | PayPal business payout |
| SHOPEE PAY SETTLEMENT / SHOPEE PAYOUT | Trade income | Revenue | Shopee e-commerce seller settlement |
| CAROUSELL PAYOUT / CAROUSELL SETTLEMENT | Trade income | Revenue | Carousell business seller payout |
| GRAB FOR BUSINESS / GRABPAY SETTLEMENT | Trade income | Revenue | GrabPay business payout |
| CHEQUE DEPOSIT / CHQ DEP [ref] | Trade income | Revenue | Client cheque |
| SALARY CREDIT [employer] | Employment income | NOT trade income | Separate head; Form IR8A / Form B1 |
| INTEREST CREDIT / INT EARNED [bank] | Interest income | NOT trade income | Bank interest -- may be exempt for individuals |
| DIVIDEND FROM [company] | Dividend income | NOT trade income | Singapore one-tier dividends are generally exempt |
| INCOME TAX REFUND / IRAS REFUND | EXCLUDE | Not income | Tax refund |
| LOAN DRAWDOWN / LOAN DISBURSEMENT | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

| Pattern | Expense Category | Treatment | Notes |
|---|---|---|---|
| OFFICE RENT [landlord] / COMMERCIAL LEASE | Rent | Fully deductible | Dedicated business premises |
| SERVICED OFFICE [WeWork/JustCo/The Work Project] | Rent | Fully deductible | Hot desks / co-working fully deductible |
| SP SERVICES / SP GROUP UTILITIES | Utilities | Business portion deductible | Home office: apportion |
| SINGTEL BROADBAND / STARHUB HOME / M1 FIBRE | Communications | Business portion deductible | Mixed use: apportion |
| SINGTEL MOBILE / STARHUB MOBILE / M1 MOBILE | Communications | Business portion deductible | Mixed use: apportion |
| GRAB [ride for business] / COMFORT TAXI | Travel | Deductible if business purpose | Keep receipts and log |
| SINGAPORE AIRLINES / SCOOT / JETSTAR | Travel | Deductible if business travel | Keep itinerary and business purpose |
| MRT / SBS TRANSIT / EZ-LINK | Travel | Deductible if business | Commuting to/from home is NOT deductible |
| GOOGLE ADS / META / LINKEDIN | Advertising | Fully deductible | |
| AMAZON.SG [supplies] / CHALLENGER [office] | Office supplies | Fully deductible | Business purchases |
| ADOBE / MICROSOFT 365 / NOTION / SLACK | Software | Fully deductible (subscription) | Subscriptions expense in year; owned software may be capital |
| CPFB [CPF BOARD] MEDISAVE | CPF (personal relief) | NOT business expense | MediSave is a personal relief (CPF relief) |
| AIA / PRUDENTIAL / GREAT EASTERN / NTUC INCOME | NOT business expense | Personal insurance | Life insurance = personal relief (limited) |
| IRAS INCOME TAX / IRAS NOA | EXCLUDE | Tax payment | Not deductible |
| IRAS GST PAYMENT | EXCLUDE | Indirect tax payment | Not income tax |
| BANK CHARGES / ADMIN FEE [DBS/OCBC/UOB] | Bank charges | Fully deductible | Business account only |
| STRIPE FEE / PAYPAL FEE / WISE FEE | Transaction fees | Fully deductible | Payment processing costs |
| HIRE PURCHASE / VEHICLE LOAN [bank] | Capital repayment | NOT deductible | Principal repayment; interest portion may be deductible |
| PERSONAL WITHDRAWAL / OWN TRANSFER | EXCLUDE | Drawings | Not business expense |

### 3.3 Capital Allowance Qualifying Assets

| Asset Purchased | Section 19A Option | Notes |
|---|---|---|
| Computer / laptop [Apple/Lenovo/Dell/HP] | One-year write-off (100%) | Below SGD 5,000: Section 19A(10A) |
| Office phone / tablet | One-year write-off | Below SGD 5,000: Section 19A(10A) |
| Office furniture / desk [IKEA/Harvey Norman/Gain City] | 3-year write-off or standard | 6-year standard useful life |
| Camera / video equipment (business) | One-year or 3-year | If revenue-earning asset |
| Private car (S-plate) | NO capital allowances | Running costs for business use may be claimed |
| Commercial van / lorry | Standard Section 19 | Capital allowances claimable |

---

## Section 4 -- Worked Examples

### Example 1 -- PayNow Business Receipt

**Input line (DBS Bank statement):**
`15 Mar 2025 | PayNow Credit ALPHA DESIGN PTE LTD | +8,500.00 | Balance 24,310.50`

**Reasoning:**
PayNow receipt from a business client for design services. This is trade income under Section 10(1)(a). If the taxpayer is GST-registered (above SGD 1M threshold), the SGD 8,500 may include 9% GST. If GST-registered: gross revenue = SGD 8,500/1.09 = SGD 7,798.17 (trade income) + SGD 701.83 (GST liability). If not GST-registered: full SGD 8,500 is trade income.

**Classification:** Trade income SGD 8,500 (or SGD 7,798.17 net if GST-registered).

### Example 2 -- Stripe Payout (Net of Stripe Fees)

**Input line (OCBC Bank statement):**
`22 Apr 2025 | STRIPE PAYOUT SG | +4,850.00 | Available Balance 31,200.00`

**Reasoning:**
Stripe processes payments and pays out net of its fees. If Stripe collected SGD 5,000 from clients and deducted SGD 150 in fees, the payout is SGD 4,850. The gross trade income is SGD 5,000; the Stripe fee of SGD 150 is a deductible business expense. Match to Stripe dashboard for exact gross and fee amounts.

**Classification:** Gross trade income SGD 5,000; Stripe fees SGD 150 deductible.

### Example 3 -- CPF MediSave Payment

**Input line (UOB Bank statement):**
`01 May 2025 | CPFB MEDISAVE CONTRIBUTION | -3,600.00 | Balance 15,400.00`

**Reasoning:**
Self-employed person's mandatory MediSave contribution to CPF Board. This is NOT a business expense. It is deductible as a CPF relief (personal relief) under the personal reliefs section. The exact amount depends on net trade income and age (rates range 4%--10.5%). Claim as CPF contribution relief, subject to the overall SGD 80,000 personal relief cap.

**Classification:** EXCLUDE from trade expenses. Record as CPF contribution relief (personal relief).

### Example 4 -- WeWork Office Subscription

**Input line (DBS Bank statement):**
`01 Jun 2025 | WEWORK SINGAPORE PTE LTD | -1,200.00 | Balance 28,750.00`

**Reasoning:**
WeWork hot desk / dedicated desk monthly fee. This is office rent -- a deductible business expense under Section 14(1) ITA (wholly and exclusively incurred in the production of income). No apportionment needed for a dedicated business workspace.

**Classification:** Rent / office costs SGD 1,200. Fully deductible.

### Example 5 -- Laptop Purchase

**Input line (OCBC Bank statement):**
`15 Jul 2025 | APPLE SINGAPORE PTE LTD | -2,899.00 | Balance 19,200.00`

**Reasoning:**
Apple MacBook purchase SGD 2,899. Capital asset under Section 19A(10A): assets costing below SGD 5,000 individually can be written off 100% in the year of acquisition. Total low-value assets in the year must not exceed SGD 30,000. Since SGD 2,899 < SGD 5,000 and within the cap, 100% capital allowance applies.

**Classification:** Capital allowance SGD 2,899 (100% write-off under Section 19A(10A)).

### Example 6 -- Private Car Expense

**Input line (UOB Bank statement):**
`10 Aug 2025 | SHELL SELECT QUEENSTOWN | -120.00 | Balance 22,100.00`

**Reasoning:**
Petrol purchased at Shell station SGD 120. The taxpayer drives a private car (S-plate). Capital allowances on private cars are NOT claimable. Running costs (petrol, parking, ERP) attributable to documented business trips may be deducted. Requires mileage log or trip records. Without documentation, default is 0% deduction.

**Classification:** Motor vehicle expense -- PENDING. Default: 0%. Flag for reviewer to confirm business trip documentation.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Trade Income Computation

**Legislation:** ITA Section 10(1)(a)

```
Gross revenue from trade/business/profession/vocation
Less: Allowable business expenses (Section 14)
Add: Balancing charges (if assets disposed)
Less: Capital allowances (Section 19/19A)
= Adjusted trade income
Less: Approved donations (250% deduction)
= Assessable income
Less: Personal reliefs (Section 36-40, capped at SGD 80,000)
= Chargeable income
Apply rate table
Less: Tax rebates
= Net tax payable
```

### 5.2 Capital Allowances

**Legislation:** ITA Sections 19, 19A, 19A(10A)

| Method | Details |
|---|---|
| Section 19 (standard) | Initial allowance 20% + annual allowance over prescribed working life (6, 12, or 16 years) |
| Section 19A (one-year) | 100% in year of acquisition (irrevocable; applies to ALL assets acquired in that YA) |
| Section 19A (three-year) | 33.33% per year over 3 years |
| Section 19A(10A) (low-value) | 100% for assets < SGD 5,000 each; cap SGD 30,000/year aggregate |

**Private cars (S-plate):** NO capital allowances.

### 5.3 Allowable Business Expenses

**Legislation:** ITA Section 14 -- "wholly and exclusively incurred in the production of income"

Fully deductible if the test is met: rent for business premises, professional indemnity insurance, accounting/tax fees, office supplies, software subscriptions, marketing, bank charges, travel for business, business entertainment (with documentation).

NOT deductible (Section 15): domestic/private expenses, capital expenditure (unless through CA), income tax itself, fines/penalties, drawings.

### 5.4 Personal Reliefs

**Legislation:** ITA Sections 36--40; cap SGD 80,000 per YA

| Relief | Amount (SGD) |
|---|---|
| Earned income relief (below 55) | Lower of actual earned income or 1,000 |
| Earned income relief (55--59) | Lower of actual earned income or 6,000 |
| Earned income relief (60+) | Lower of actual earned income or 8,000 |
| CPF relief (self-employed) | Mandatory MediSave contributions |
| CPF cash top-up | Up to 8,000 (own) + 8,000 (family) |
| SRS relief | Up to 15,300 (citizens/PRs) or 35,700 (foreigners) |
| Spouse relief | 2,000 (spouse income ≤ SGD 4,000) |
| Qualifying child relief | 4,000 per child |
| Handicapped child relief | 7,500 per child |
| Parent relief | 9,000 / 14,000 (handicapped) |
| Life insurance | Up to 5,000 (only if CPF contributions < 5,000) |
| Course fees | Up to 5,500 |
| Approved donations | 250% of donation (deducted from assessable income, NOT subject to SGD 80,000 cap) |

### 5.5 Filing Deadlines

| Item | Deadline |
|---|---|
| Form B (self-employed) -- e-filing | 18 April of the YA |
| Form B -- paper filing | 15 April of the YA |
| Tax payment | Within 1 month of NOA |
| GIRO instalment | 12 monthly instalments (apply by specified date) |

### 5.6 Penalties

| Offence | Penalty |
|---|---|
| Late filing | SGD 200--1,000 per offence |
| Non-filing (estimated assessment) | Estimated NOA issued; 5% penalty on tax owed |
| Incorrect return | Up to 200% of tax undercharged |
| Wilful tax evasion | Up to SGD 50,000 and/or 3 years imprisonment; 400% penalty |
| Late payment | 5% on unpaid tax after 30 days; +1%/month thereafter (max 12%) |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

IRAS does not have a blanket home office scheme. However, expenses attributable to the business use of a home (additional electricity, dedicated internet line, pro-rata rent if a room is exclusively for business) may be claimed if the home is an actual place of business. Apportionment basis must be reasonable (floor area ratio or time-based).

**Flag for reviewer:** Confirm apportionment basis, documentation, and whether IRAS has been notified that business is conducted from home.

### 6.2 Private Car Business Use

Running costs (petrol, parking, ERP, road tax) for documented business trips are potentially deductible. Capital allowances are NOT available for private (S-plate) cars. A mileage log or contemporaneous trip record is required.

**Flag for reviewer:** Confirm vehicle type, business-use percentage, and documentation method.

### 6.3 Capital vs Revenue Expenditure

IRAS distinguishes between revenue expenses (deductible in year incurred) and capital expenditure (deductible only through capital allowances). Renovation/refurbishment costs are generally capital but Section 14Q allows a 3-year deduction (capped at SGD 300,000 per 3-year period).

### 6.4 CPF MediSave Contributions

Mandatory MediSave contribution rates for self-employed persons vary by age and net trade income. The contribution is between 4% and 10.5% of net trade income, subject to a cap.

**Flag for reviewer:** Calculate exact contribution using IRAS/CPF tables for client's age group.

### 6.5 Working Mother's Child Relief (WMCR)

WMCR is available only to working mothers (citizens or PRs). The relief is 15%/20%/25% of earned income for 1st/2nd/3rd+ children. Combined QCR + WMCR capped at SGD 50,000 per child.

---

## Section 7 -- Excel Working Paper Template

```
SINGAPORE INCOME TAX WORKING PAPER
Taxpayer: _______________  NRIC/FIN: ___________
Year of Assessment: YA 2026 (income earned in 2025)
GST registered: Yes / No [circle one]

A. GROSS TRADE REVENUE
  A1. Total receipts from clients             ___________
  A2. Less: GST collected (if GST-registered) ___________
  A3. Net trade revenue                       ___________

B. ALLOWABLE BUSINESS EXPENSES
  B1. Rent / co-working space                 ___________
  B2. Utilities (business %)                  ___________
  B3. Communications (business %)             ___________
  B4. Travel (business)                       ___________
  B5. Advertising / marketing                 ___________
  B6. Professional fees (accounting, legal)   ___________
  B7. Software / subscriptions                ___________
  B8. Office supplies                         ___________
  B9. Business entertainment                  ___________
  B10. Bank / transaction fees                ___________
  B11. Other allowable expenses               ___________
  B12. Total business expenses                ___________

C. CAPITAL ALLOWANCES
  C1. Section 19A(10A) low-value assets       ___________
  C2. Section 19A one-year / three-year       ___________
  C3. Section 19 standard annual allowance    ___________
  C4. Total capital allowances                ___________

D. ADJUSTED TRADE INCOME (A3 - B12 - C4)      ___________

E. APPROVED DONATIONS (x 250%)               ___________

F. ASSESSABLE INCOME (D - E)                  ___________

G. PERSONAL RELIEFS
  G1. Earned income relief                    ___________
  G2. CPF MediSave contribution               ___________
  G3. SRS contribution                        ___________
  G4. Spouse relief                           ___________
  G5. Child reliefs (QCR / WMCR)             ___________
  G6. Parent relief                           ___________
  G7. Course fees relief                      ___________
  G8. Other reliefs                           ___________
  G9. Total reliefs (cap: SGD 80,000)         ___________

H. CHARGEABLE INCOME (F - G9)                 ___________

I. GROSS TAX (apply rate table)               ___________

J. LESS: TAX REBATES                          ___________

K. NET TAX PAYABLE (I - J)                    ___________

REVIEWER FLAGS:
  [ ] Tax residence confirmed (183 days / citizen / PR)?
  [ ] GST status confirmed?
  [ ] Capital vs revenue expenditure reviewed?
  [ ] Private car: no capital allowances?
  [ ] Personal relief cap SGD 80,000 checked?
  [ ] Donations deducted from assessable income (not personal reliefs)?
```

---

## Section 8 -- Bank Statement Reading Guide

### Singapore Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| DBS / POSB | CSV / PDF | Date, Reference, Debit, Credit, Balance |
| OCBC | CSV | Transaction Date, Description, Withdrawals (SGD), Deposits (SGD), Balance (SGD) |
| UOB | CSV / PDF | Trans. Date, Description, Debit, Credit, Available Balance |
| Standard Chartered SG | CSV | Date, Description, Debit, Credit, Running Balance |
| Citibank SG | CSV | Date, Description, Debit Amount, Credit Amount |
| Wise SG | CSV | Date, Description, Amount, Currency, Running Balance |

### Key Singapore Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| FAST / FAST CREDIT [name] | Funds transfer via FAST | Potential income from client |
| PayNow Credit [name/UEN] | PayNow receipt | Business income |
| GIRO Credit / GIRO Debit | Standing instruction | Regular income or recurring expense |
| IBG / INTERBANK GIRO | Interbank GIRO | Income or expense transfer |
| TT FROM [bank/name] | Telegraphic transfer in | Overseas client income |
| PAYNOW QR | PayNow QR code payment | Business income |
| ATM WITHDRAWAL | Cash withdrawal | Personal -- investigate |
| INTEREST CREDIT | Bank interest | Other income (may be exempt) |
| IRAS GIRO | IRAS tax payment | Tax payment -- exclude |
| CPFB | CPF Board payment | MediSave -- personal relief |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all FAST/PayNow/GIRO credits from non-personal sources as potential trade income
2. Classify all CPFB debits as MediSave (personal relief -- not business expense)
3. Apply conservative defaults: non-GST registered, no capital allowances for vehicles, 0% home office
4. Flag all large purchases > SGD 5,000 as potential capital expenditure requiring review
5. Generate working paper with PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- SINGAPORE INCOME TAX
1. Are you a Singapore citizen, PR, or foreigner (and if foreigner, how many days in Singapore)?
2. Are you GST-registered?
3. Are you filing as a sole proprietor (Form B) or employee (Form B1)?
4. What is your main business / profession?
5. Do you have an office outside your home, or do you work from home?
6. Do you use a vehicle for work? If so, is it a private car (S-plate) or commercial vehicle?
7. CPF: what MediSave contributions did you make this year?
8. SRS: did you make Supplementary Retirement Scheme contributions?
9. Do you have qualifying children or dependent parents?
10. Any approved donations to IPCs this year?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Section |
|---|---|
| Trade income | ITA Section 10(1)(a) |
| Allowable expenses | ITA Section 14 |
| Prohibited deductions | ITA Section 15 |
| Capital allowances (standard) | ITA Section 19 |
| Capital allowances (accelerated) | ITA Section 19A |
| Low-value asset write-off | ITA Section 19A(10A) |
| Renovation/refurbishment | ITA Section 14Q |
| Personal reliefs | ITA Sections 36--40 |
| Record keeping | ITA Section 67 |

### Known Gaps / Out of Scope

- Non-resident income tax
- GST computation and returns
- Corporate income tax (Pte Ltd, etc.)
- Partnership income allocation
- Property gains / capital gains
- NOR scheme (abolished after YA 2024)

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Singapore bank formats; local platform patterns (PayNow, Stripe SG, Shopee); worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Preceding year basis confirmed? (YA 2026 = 2025 income)
- [ ] GST excluded from trade income for GST-registered taxpayers?
- [ ] Personal relief cap SGD 80,000 applied?
- [ ] Approved donations deducted from assessable income (not personal reliefs)?
- [ ] Capital allowances for private cars NOT claimed?
- [ ] Section 19A election irrevocability noted?

---

## PROHIBITIONS

- NEVER apply resident tax rates without confirming tax residence (183-day rule, citizen, or PR status)
- NEVER include GST collected on sales as trade income for GST-registered taxpayers
- NEVER allow capital allowances on private S-plate cars
- NEVER allow income tax itself as a deductible expense
- NEVER allow personal or domestic expenses as business deductions
- NEVER allow personal reliefs to exceed SGD 80,000 (note: approved donations are NOT subject to this cap)
- NEVER apply NOR scheme concessions -- scheme is expired after YA 2024
- NEVER confuse Year of Assessment with basis period (YA 2026 ≠ 2026 income)
- NEVER present tax calculations as definitive -- always label as estimated and direct client to their Accredited Tax Adviser for confirmation

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an Accredited Tax Adviser, Chartered Accountant, or equivalent licensed practitioner in Singapore) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
