---
name: ie-income-tax-form11
description: >
  Use this skill whenever asked about Irish income tax for self-employed individuals filing Form 11. Trigger on phrases like "Form 11", "self-assessment Ireland", "Case I profits", "Case II profits", "USC", "PRSI Class S", "preliminary tax Ireland", "earned income credit", "trading profits", "self-employed tax Ireland", "ROS filing", or any question about computing or filing income tax for a self-employed person in Ireland. This skill covers income tax rates (20%/40%), USC bands, PRSI Class S, personal tax credits, allowable deductions, capital allowances, preliminary tax, and Form 11 structure. ALWAYS read this skill before touching any Irish income tax work.
version: 2.0
jurisdiction: IE
tax_year: 2025
category: international
depends_on:
  - income-tax-workflow-base
---

# Ireland Income Tax (Form 11) -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Ireland |
| Tax | Income Tax (20%/40%) + USC + PRSI Class S |
| Currency | EUR only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Taxes Consolidation Act 1997 (TCA 1997) |
| Supporting legislation | Finance Act 2024 (Budget 2025); Social Welfare Consolidation Act 2005 (PRSI); Part 18D TCA 1997 (USC) |
| Tax authority | Revenue Commissioners (revenue.ie) |
| Filing portal | Revenue Online Service (ROS) |
| Filing deadline | 31 October (paper) / mid-November (ROS e-filing) of following year |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires sign-off by a Chartered Accountant or CTA |
| Validation date | Pending |
| Skill version | 2.0 |

### Income Tax Rates and Standard Rate Band (2025)

| Filing Status | Standard Rate Band (20%) | Balance at 40% |
|---|---|---|
| Single | EUR 44,000 | Above EUR 44,000 |
| Married (one earner) | EUR 53,000 | Above EUR 53,000 |
| Married (two earners) | EUR 53,000 + EUR 35,000 (max EUR 88,000) | Above combined band |
| Single parent | EUR 48,000 | Above EUR 48,000 |

### USC Rates (2025)

| Band | Rate |
|---|---|
| First EUR 12,012 | 0.5% |
| EUR 12,012.01 -- EUR 27,382 | 2% |
| EUR 27,382.01 -- EUR 70,044 | 3% |
| Above EUR 70,044 | 8% |
| USC surcharge (non-PAYE income > EUR 100,000) | +3% |

USC exemption: total income not exceeding EUR 13,000 = no USC.

### PRSI Class S (2025)

| Item | Value |
|---|---|
| Rate (blended 2025) | 4.125% (4.1% Jan-Sep, 4.2% Oct-Dec) |
| Minimum contribution | EUR 650/year |
| Income threshold | EUR 5,000 (below = no PRSI) |

### Key Personal Tax Credits (2025)

| Credit | EUR |
|---|---|
| Single Person's Credit | 2,000 |
| Married Person's Credit | 4,000 |
| Earned Income Credit (self-employed) | 2,000 |
| Employee (PAYE) Credit | 2,000 |
| One Parent Family Credit | 1,800 |

### Form 11 Key Panels

| Panel | Description |
|---|---|
| Panel A | Personal details |
| Panel B | Self-employment (Case I/II) -- turnover, profit, capital allowances |
| Panel C | Other Irish income (PAYE, rental, investment) |
| Panel D | Foreign income |
| Panel E | Tax credits and reliefs |
| Panel F | Capital gains |
| Panel G | Property details |
| Panel H | Self-assessment (tax, preliminary tax, balance) |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Unknown filing status | Single |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether capital or revenue | Capital (depreciate) |
| Unknown motor vehicle cost | Cap at EUR 24,000 |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of filing status (single/married/single parent).

**Recommended** -- all sales invoices, purchase invoices, prior year Form 11 or Notice of Assessment, PPS number, capital asset records.

**Ideal** -- complete trading account, asset register with capital allowances schedule, preliminary tax payment records, employment P60/payslip (if dual income).

**Refusal if minimum is missing -- SOFT WARN.** No bank statement = hard stop. Bank statement without invoices = proceed with reviewer warning.

### Refusal Catalogue

**R-IE-1 -- Companies (Ltd, DAC, PLC).** "This skill covers self-employed individuals filing Form 11 only. Companies file Form CT1 (Corporation Tax). Out of scope."

**R-IE-2 -- Partnerships.** "Partnership profits are computed at partnership level (Form 1 Firms) and allocated to partners. Out of scope."

**R-IE-3 -- Non-resident / dual resident.** "Non-resident and dual-resident taxation has different rules. Escalate."

**R-IE-4 -- Capital gains tax (CGT).** "CGT computations require detailed disposal analysis. Escalate."

**R-IE-5 -- Revenue audit / appeal.** "Revenue audit or appeal situations require specialist advice. Escalate."

---

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits on Bank Statement)

| Pattern | Form 11 Line | Treatment | Notes |
|---|---|---|---|
| Client name + TRANSFER, LODGEMENT, EFT | Panel B -- Turnover | Business income | If VAT-registered, extract net (excl. 23% VAT) |
| PROFESSIONAL FEES, CONSULTANCY, INVOICE | Panel B -- Turnover | Business income | Case II profession typical |
| STRIPE PAYOUT, STRIPE TRANSFER | Panel B -- Turnover | Business income | Platform payout -- match to invoices |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Panel B -- Turnover | Business income | Match to underlying invoices |
| WISE PAYOUT, REVOLUT PAYOUT | Panel B -- Turnover | Business income | International platform payout |
| UPWORK, FIVERR, TOPTAL | Panel B -- Turnover | Business income | Net of platform commission |
| SALARY, WAGES, EMPLOYER [name] | Panel C -- Employment | NOT self-employment | PAYE income -- separate |
| RENT RECEIVED, TENANT [name] | Panel C -- Rental | NOT self-employment | Rental income -- Case V |
| DEPOSIT INTEREST, DIRT | Panel C -- Investment | NOT self-employment | DIRT already withheld at 33% |
| DIVIDEND | Panel C -- Investment | NOT self-employment | |
| REVENUE REFUND, TAX REFUND | EXCLUDE | Not income | Prior year refund |
| SOCIAL WELFARE, DEASP | Check nature | May be taxable | Some SW payments are taxable income |

### 3.2 Expense Patterns (Debits) -- Fully Deductible

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| OFFICE RENT, COMMERCIAL RENT, LEASE [premises] | Rent | Fully deductible | Dedicated business premises |
| PROFESSIONAL INDEMNITY, PI INSURANCE | Insurance | Fully deductible | |
| ACCOUNTANT, AUDITOR, TAX ADVISER | Professional fees | Fully deductible | |
| SOLICITOR, BARRISTER (business) | Legal fees | Fully deductible | Business-related only |
| OFFICE SUPPLIES, STATIONERY, VIKING | Supplies | Fully deductible | |
| MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Advertising | Fully deductible | |
| TRAINING, CPD, COURSE, CONFERENCE | Training | Fully deductible | Current business related |
| CPA IRELAND, ACCA, LAW SOCIETY, CHARTERED | Professional subs | Fully deductible | |
| BANK CHARGE, MAINTENANCE FEE, TRANSACTION FEE | Bank charges | Fully deductible | Business account |
| STRIPE FEE, PAYPAL FEE, SQUARE FEE | Payment processing | Fully deductible | |
| POSTAGE, AN POST (business) | Postage | Fully deductible | |
| DOMAIN, HOSTING, AWS, CLOUDFLARE | IT infrastructure | Fully deductible | |
| SOFTWARE, SUBSCRIPTION, SAAS | Software | Fully deductible | Recurring subscription = revenue |

### 3.3 Expense Patterns (Debits) -- Travel and Subsistence

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| RYANAIR, AER LINGUS, EASYJET | Flights | Fully deductible | Business purpose required |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Fully deductible | Business travel |
| IRISH RAIL, IARNROD EIREANN, BUS EIREANN | Transport | Fully deductible | Business travel |
| TAXI, FREE NOW, BOLT | Local transport | Fully deductible | Business purpose |
| SUBSISTENCE, PER DIEM | Subsistence | Civil service rates | Standard rates apply |

### 3.4 Expense Patterns (Debits) -- NOT Deductible

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| RESTAURANT, DINNER, LUNCH, ENTERTAINMENT | Entertainment | NOT deductible | Blocked under s.840 TCA 1997 |
| PERSONAL, GROCERIES, SUPERMARKET, TESCO, DUNNES | Personal | NOT deductible | Private living costs |
| FINE, PENALTY, PARKING FINE | Fines | NOT deductible | Public policy |
| REVENUE PAYMENT, INCOME TAX, USC, PRSI | Tax payments | NOT deductible | Tax on income |
| DRAWINGS, PERSONAL, ATM (personal) | Drawings | NOT deductible | Not an expense |

### 3.5 Expense Patterns (Debits) -- Capital Items

| Pattern | Category | Annual Rate | Notes |
|---|---|---|---|
| LAPTOP, COMPUTER, MACBOOK, IMAC | Computer equipment | 12.5% (8 years) | Capital allowance |
| PRINTER, SCANNER, COPIER | Plant/machinery | 12.5% (8 years) | |
| FURNITURE, DESK, CHAIR, FILING | Furniture/fittings | 12.5% (8 years) | |
| VEHICLE, CAR (business) | Motor vehicle | 12.5% (8 years, capped EUR 24,000) | Business % only |
| ENERGY EFFICIENT (SEAI listed) | ACA equipment | 100% year 1 | Accelerated Capital Allowance |

### 3.6 Expense Patterns -- Mixed Use (Tier 2)

| Pattern | Category | Treatment | Notes |
|---|---|---|---|
| ESB, ELECTRIC IRELAND, BORD GAIS | Utilities | T2 -- home office % only | If home office |
| EIRCELL, THREE, VODAFONE, 48 | Phone | T2 -- business % only | Default 0% |
| BROADBAND, EIRE, SKY, VIRGIN MEDIA | Internet | T2 -- business % only | Default 0% |
| FUEL, PETROL, DIESEL, CIRCLE K, MAXOL | Vehicle fuel | T2 -- business % only | Mileage log required |
| RENT (residential, for home office) | Home office | T2 -- proportional | Dedicated room required |

### 3.7 Exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| INTERNAL TRANSFER, OWN ACCOUNT, SAVINGS | EXCLUDE | Own-account transfer |
| LOAN REPAYMENT, MORTGAGE PRINCIPAL | EXCLUDE | Loan principal |
| LOAN INTEREST (business) | Deductible | Interest on business borrowings |
| VAT PAYMENT, REVENUE VAT | EXCLUDE | VAT liability payment |
| PRELIMINARY TAX, PT PAYMENT | Panel H (credit) | Not expense -- credit against liability |

### 3.8 Irish Banks -- Statement Format Reference

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| AIB (Allied Irish Banks) | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; description = counterparty + ref |
| BOI (Bank of Ireland) | PDF, CSV | Date, Details, Debit, Credit, Balance | Similar format to AIB |
| PTSB (Permanent TSB) | PDF, CSV | Date, Description, Amount, Balance | Less granular descriptions |
| Ulster Bank / NatWest | PDF, CSV | Date, Description, Paid Out, Paid In, Balance | UK-style format |
| Revolut Business | CSV | Date, Counterparty, Amount, Currency, Reference | Clean data |
| N26, Wise | CSV | Date, Counterparty, Amount, Reference | International neobanks |

---

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (VAT-registered)

**Input line:**
`15/03/2025 ; AIB CREDIT TRANSFER ; ABC CONSULTING LTD ; INV-2025-012 ; +6,150.00 ; EUR`

**Reasoning:**
Client payment. If VAT-registered at 23%, EUR 6,150 includes VAT. Net = EUR 5,000 (Panel B turnover). EUR 1,150 is VAT collected (excluded).

**Classification:** Panel B turnover = EUR 5,000.

### Example 2 -- Entertainment (Blocked)

**Input line:**
`22/04/2025 ; BOI VISA ; THE SHELBOURNE HOTEL ; CLIENT DINNER ; -120.00 ; EUR`

**Reasoning:**
Entertainment. Blocked under s.840 TCA 1997. No deduction.

**Classification:** NOT deductible. Remove from allowable deductions.

### Example 3 -- Motor Vehicle Capital Allowance

**Input line:**
`01/06/2025 ; AIB DD ; VOLKSWAGEN FINANCE ; CAR PAYMENT ; -450.00 ; EUR`

**Reasoning:**
Car finance payment. The capital cost (not finance payments) determines capital allowance. Motor vehicles capped at EUR 24,000. Annual allowance = EUR 24,000 x 12.5% = EUR 3,000 x business %. Ask for business-use percentage.

**Classification:** T2 -- capital allowance on capped cost, business % required.

### Example 4 -- Software Subscription

**Input line:**
`01/05/2025 ; BOI DD ; ADOBE SYSTEMS IRELAND ; CREATIVE CLOUD ; -29.99 ; EUR`

**Reasoning:**
Monthly SaaS subscription. Revenue expense, fully deductible.

**Classification:** Allowable deduction -- software subscription.

### Example 5 -- PRSI / USC Payment (NOT Deductible)

**Input line:**
`31/10/2025 ; AIB TRANSFER ; REVENUE COMMISSIONERS ; PRELIMINARY TAX ; -8,000.00 ; EUR`

**Reasoning:**
Preliminary tax payment (includes income tax, USC, PRSI). Not a deductible expense. Goes to Panel H as credit against liability.

**Classification:** Panel H -- preliminary tax paid. NOT a deduction.

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`15/05/2025 ; AIB TRANSFER ; OWN SAVINGS ACCOUNT ; ; -5,000.00 ; EUR`

**Reasoning:**
Transfer between own accounts. Neither income nor expense.

**Classification:** EXCLUDE.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Case I / Case II Trading Profits

**Legislation:** TCA 1997, Schedule D, Cases I and II

Gross turnover minus allowable revenue deductions minus capital allowances = adjusted profit. The "wholly and exclusively" test applies (TCA 1997, s.81).

### 5.2 Capital Allowances

| Asset Type | Annual Rate | Recovery Period |
|---|---|---|
| Plant and machinery | 12.5% | 8 years |
| Motor vehicles (capped EUR 24,000) | 12.5% | 8 years |
| Computer equipment | 12.5% | 8 years |
| Furniture/fittings | 12.5% | 8 years |
| Industrial buildings | 4% | 25 years |
| Energy-efficient (ACA) | 100% | Year 1 |

Motor vehicle cap: if car costs EUR 35,000, allowances calculated on EUR 24,000 only.

### 5.3 Non-Deductible Expenses

| Expense | Reason |
|---|---|
| Entertainment | Blocked under s.840 TCA 1997 |
| Personal living expenses | Not business-related |
| Fines, penalties, surcharges | Public policy |
| Income tax, USC, PRSI | Tax on income |
| Capital expenditure | Through capital allowances |
| General provisions (non-specific bad debts) | Must be specific |

### 5.4 Preliminary Tax

Must equal or exceed the lower of:
- 100% of prior year's final tax liability
- 90% of current year's actual liability

First year: no preliminary tax due. Direct debit option: 105% of pre-preceding year spread monthly.

### 5.5 Tax Computation Steps

1. Compute Case I/II adjusted profit
2. Add other income
3. Total income
4. Less deductions (pension, losses forward)
5. Taxable income
6. Apply income tax at 20%/40%
7. Less personal tax credits
8. Income tax payable
9. Compute USC on gross income
10. Compute PRSI Class S on gross income
11. Total liability = IT + USC + PRSI
12. Less preliminary tax and PAYE withholding
13. Balance due / refund

### 5.6 Filing Deadlines and Penalties

| Item | Deadline |
|---|---|
| Form 11 (paper) | 31 October |
| Form 11 (ROS) | Mid-November |
| Preliminary tax | Same as Form 11 |
| Late surcharge (within 2 months) | 5% of tax (max EUR 12,695) |
| Late surcharge (over 2 months) | 10% of tax (max EUR 63,485) |
| Late payment interest | 0.0219% per day (~8% p.a.) |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Expenses

- Proportional deduction based on dedicated room as % of total floor area
- Must be exclusively for business -- dual-use room does not qualify
- Utility costs (electricity, heat, broadband) apportioned

**Conservative default:** 0% until reviewer confirms arrangement.

### 6.2 Motor Vehicle Business Use

- Business-use % of running costs deductible
- Capital allowances on cost capped at EUR 24,000, multiplied by business %
- Civil service mileage rates may apply as alternative

**Conservative default:** 0% business use until mileage log provided.

### 6.3 Phone / Broadband Mixed Use

Default: 0%. Client must provide reasonable business-use estimate.

### 6.4 Bad Debt Write-Off

- Must be specific (not general provision)
- Previously included in income
- All reasonable recovery steps taken
- Flag for reviewer

### 6.5 Pension Contributions

- Age-related % limits (15% under 30 to 40% for 60+)
- Annual earnings cap EUR 115,000
- Flag for reviewer to confirm age bracket

### 6.6 Loss Relief

- Current year: set off against other income (s.381 TCA 1997)
- Carry forward: against future profits of same trade (s.382)
- Flag for reviewer for optimal utilisation

---

## Section 7 -- Excel Working Paper Template

```
IRELAND INCOME TAX -- FORM 11 WORKING PAPER
Tax Year: 2025
Client: ___________________________
Filing Status: Single / Married (1 earner) / Married (2 earners) / Single Parent

A. PANEL B -- SELF-EMPLOYMENT INCOME
  A1. Gross turnover (net of VAT if registered)  ___________
  A2. Less: Cost of sales                         ___________
  A3. Gross profit                                ___________
  A4. Less: Allowable revenue deductions           ___________
  A5. Net profit before capital allowances         ___________
  A6. Less: Capital allowances                     ___________
  A7. Adjusted Case I/II profit                    ___________

B. ALLOWABLE DEDUCTIONS BREAKDOWN
  B1. Office rent                                  ___________
  B2. Professional insurance                       ___________
  B3. Accountancy / legal fees                     ___________
  B4. Office supplies                              ___________
  B5. Software / IT                                ___________
  B6. Marketing / advertising                      ___________
  B7. Bank charges / payment processing            ___________
  B8. Training / CPD / professional subs           ___________
  B9. Travel and subsistence                       ___________
  B10. Telecoms (business %)                       ___________
  B11. Home office (% of utilities)                ___________
  B12. Vehicle running costs (business %)          ___________
  B13. Other allowable expenses                    ___________
  B14. TOTAL DEDUCTIONS                            ___________

C. TAX COMPUTATION
  C1. Income tax (20%/40%)                         ___________
  C2. Less: Tax credits                            ___________
  C3. Income tax payable                           ___________
  C4. USC                                          ___________
  C5. PRSI Class S                                 ___________
  C6. Total liability                              ___________
  C7. Less: Preliminary tax paid                   ___________
  C8. Balance due / refund                         ___________

REVIEWER FLAGS:
  [ ] Filing status confirmed?
  [ ] Home office arrangement confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/broadband business % confirmed?
  [ ] Motor vehicle cost cap applied (EUR 24,000)?
  [ ] Entertainment excluded?
  [ ] All T2 items flagged?
```

---

## Section 8 -- Bank Statement Reading Guide

### Irish Bank Statement Formats

| Bank | Format | Key Fields | Notes |
|---|---|---|---|
| AIB | PDF, CSV | Date, Description, Debit, Credit, Balance | Most common; good counterparty detail |
| BOI (Bank of Ireland) | PDF, CSV | Date, Details, Debit, Credit, Balance | Similar to AIB |
| PTSB | PDF, CSV | Date, Description, Amount, Balance | Less detail in descriptions |
| Ulster Bank | PDF, CSV | Date, Description, Paid Out, Paid In, Balance | UK-style naming |
| Revolut Business | CSV | Date, Counterparty, Amount, Currency | Clean; multi-currency |
| N26 | CSV | Date, Counterparty, Amount, Reference | Neobank format |

### Key Irish Banking Terms

| Term | Meaning | Classification Hint |
|---|---|---|
| LODGEMENT / LDG | Deposit/credit | Potential income |
| DD / DIRECT DEBIT | Direct debit | Regular expense |
| SO / STANDING ORDER | Standing order | Regular expense |
| EFT | Electronic funds transfer | Check direction |
| POS / CARD | Point of sale / card payment | Expense |
| ATM | Cash withdrawal | Ask purpose |
| CHG / FEE | Bank charge | Deductible |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm"
3. Apply conservative defaults (Section 1)
4. Generate the working paper with clear flags
5. Present the following questions:

```
ONBOARDING QUESTIONS -- IRELAND INCOME TAX
1. Filing status: single, married (one earner), married (two earners), or single parent?
2. Are you registered for VAT? If yes, at what rate?
3. Home office: dedicated room or shared space? Floor area %?
4. Vehicle: do you use a car for business? Business %? Mileage log?
5. Phone/broadband: business use %?
6. Any capital assets purchased during the year?
7. Preliminary tax paid in the year?
8. Any other income (employment, rental, investment)?
9. Age (for USC reduced rates and pension limits)?
10. Prior year Notice of Assessment available?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Income tax rates / bands | TCA 1997, as amended by Finance Act 2024 |
| USC | TCA 1997, Part 18D |
| PRSI Class S | Social Welfare Consolidation Act 2005 |
| Deductibility test | TCA 1997, s.81 (wholly and exclusively) |
| Entertainment block | TCA 1997, s.840 |
| Capital allowances | TCA 1997, Part 9 (ss.283-321) |
| Motor vehicle cap | EUR 24,000 |
| Preliminary tax | TCA 1997, ss.952-959 |
| Late filing surcharge | TCA 1997, s.1084 |
| Record keeping | TCA 1997, s.886 (6 years) |

### Test Suite

**Test 1 -- Single, mid-range income.**
Input: Single, gross EUR 60,000, expenses EUR 15,000, capital allowances EUR 1,250, first year.
Expected: Adjusted profit EUR 43,750. IT: EUR 43,750 x 20% = EUR 8,750 - EUR 4,000 credits = EUR 4,750. Plus USC + PRSI.

**Test 2 -- Married one earner, higher income.**
Input: Married (one earner), gross EUR 100,000, expenses EUR 25,000, capital allowances EUR 3,000.
Expected: Adjusted profit EUR 72,000. IT: EUR 53,000 x 20% + EUR 19,000 x 40% - EUR 6,000 credits.

**Test 3 -- Entertainment blocked.**
Input: EUR 3,000 client entertainment.
Expected: Remove entirely. Not deductible.

**Test 4 -- Motor vehicle cap.**
Input: Car EUR 40,000, 100% business.
Expected: Capped at EUR 24,000. Annual = EUR 3,000.

**Test 5 -- USC surcharge.**
Input: Non-PAYE income EUR 150,000.
Expected: Standard USC + 3% surcharge on EUR 50,000 above EUR 100,000.

**Test 6 -- PRSI below threshold.**
Input: Total income EUR 4,000.
Expected: No PRSI Class S. Below EUR 5,000.

---

## PROHIBITIONS

- NEVER apply a standard rate band without knowing filing status
- NEVER compute final tax directly -- pass to deterministic engine
- NEVER allow entertainment expenses
- NEVER allow income tax, USC, or PRSI as deductions
- NEVER apply capital allowances on motor vehicles above EUR 24,000
- NEVER allow capital items as revenue deductions
- NEVER ignore the USC surcharge for non-PAYE income over EUR 100,000
- NEVER present tax calculations as definitive

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
